##############################################################################
# Naive JSP Dependency Resolver
##############################################################################

"""
The code search is implemented using a naive JSP dependency resolver which represents the JSP relevant files as a Directed Acyclic Graph (DAG):

The nodes in the DAG represent the files.
The edges are directed and represent a depends-on relationship between the files. This is measured with a simple rule-based heuristic that uses regular expressions to identify direct dependencies by import statements. This does not cover transitive, virtual, reflection-based, polymorphic or unused dependencies.
The edges are weighted based on the in-degree of the connected nodes, which is in turn determined by their dependency count. Nodes with lower dependency counts will be treated as dependents and explored first, while nodes with higher dependency count will be treated as integration points / entry points and explored last. This is a bottom-up approach, which is ideal for capturing as many low-level details of the code as possible, as well as composability. A top-down approach assumes prior understanding of the entire codebase and can miss low-level details.
The most relevant JSP files from each git repository will be sorted using topological sort, weighted by their out-degree, and grouped by their dependency correlation.
"""

from abc import ABC, abstractmethod
from custom.github_tools import GithubTools
import re
import networkx as nx
import xml.etree.ElementTree as ET
import fnmatch

class NaiveDependencyParser(ABC):

    @abstractmethod
    def __init__(self, git_repo, tree_sha, **kwargs):
        """
        Constructor
        """
        self.repo_api = GithubTools.get_git_repo_api(git_repo)

        self.git_repo = git_repo

        self.tree_sha = tree_sha

        if not self.include_patterns:

            self.include_patterns = kwargs.get("include_patterns", r"\.[^.]+?$")

        self.initialize_data()

    @abstractmethod
    def get_singleline_regexes(self, file_path):
        """
        Returns the import regexes associated with this type of file
        based on the file extension.
        """
        pass

    @abstractmethod
    def get_multiline_regexes(self, file_path):
        """
        Returns a list of regexes constructed from dynamic properties about this instance,
        such as file names, object names (Java classes/JSP object instances etc), and so on.
        """
        pass

    
    @abstractmethod
    def get_object_names(self, file_path):
        """
        Returns a list of language-specific objects associated with this path 
        (JSP objects, Java classes etc)
        """
        pass
        

    def initialize_data(self):
        """
        Initializes relevant data for this instance
        """

        print(f"Initializing data for dependency resolver for {self.git_repo}...")
        
        self.file_names = GithubTools.get_relevant_files(self.tree_sha, self.repo_api)
    
        self.file_names = [f for f in self.file_names if re.search(self.include_patterns, f)]

        self.file_contents = {f: GithubTools.get_github_file_content(f, self.repo_api) for f in self.file_names}

        self.object_to_file_name = {name: f for f in self.file_names for name in self.get_object_names(f)}

        self.dag = nx.DiGraph()

        print(f"Initialization complete. Filtered files: {self.file_names} ({len(self.file_names)} files total)")


    def get_dag(self):
        """
        Constructs a DAG with files as the nodes and "depends-on" relationships as the edges.
        The "depends-on" relationship is based on the presence of matched regular expressions in the imports.
        For example,
        If JSP A includes a matched regex for one of the object names for Class B, then JSP A "depends-on" Class B.
        """
        for file_path, file_content in self.file_contents.items():

            singleline_regexes, multiline_regexes = self.get_singleline_regexes(file_path), self.get_multiline_regexes(file_path)

            regexes = [("s",regex) for regex in singleline_regexes] + [("m",regex) for regex in multiline_regexes]
            
            for regex_type, regex in regexes:

                iterator = re.finditer(regex, file_content, re.MULTILINE | re.DOTALL) if regex_type=="m" else re.finditer(regex, file_content)

                for matched in iterator:

                    for idx in range(len(matched.groups())+1):

                        matched_object = matched.group(idx)
    
                        if matched_object in self.object_to_file_name:
        
                            self.dag.add_edge(file_path, self.object_to_file_name[matched_object])

            if not file_path in self.dag:
                
                self.dag.add_node(file_path)

        return self.dag

    def get_ranked_files_by_outdegree(self, ascending=True):
        """
        Returns a list of relevant files from the git repository associated with this instance
        ranked by out-degree.
        """
        out_degree_view = dict(self.get_dag().out_degree())

        print(f"Out-degree: {out_degree_view}")

        ranked = sorted(out_degree_view.items(), key=lambda item: item[1])

        ranked = [(value, key) for key, value in ranked]

        return ranked

class JspDependencyParser(NaiveDependencyParser):

    def __init__(self, git_repo, tree_sha, **kwargs):

        self.include_patterns = kwargs.pop("include_patterns", r"\.(jsp|java)$")
        
        super().__init__(git_repo, tree_sha, **kwargs)

    def get_singleline_regexes(self, file_path):
        
        if file_path.endswith(".jsp"):
            
            return [
                r"<%@ page import\s?=\s?\"(.+?)\"",
                                                  
                r"<%@ taglib.+?uri\s?=\s?\"(.+?)\"",
        
                r"<jsp:useBean.+?class\s?=\s?\"(.+?)\"",
        
                r"<%@ include.+?file\s?=\s?\"(.+?)\"",
        
                r"<jsp:include.+?page\s?=\s?\"(.+?)\"",
                                                  
                r"<%^(.+?)",
            ]

        if file_path.endswith(".java"):

            return [
                r"import (.+);",
            ]

        return []

    def get_multiline_regexes(self, file_path):

        regex, keys = rf"", list(self.object_to_file_name.keys())

        if keys:
            
            first_obj_name = keys[0]
            
            regex = rf"^(\s*?{first_obj_name}|\w+?<({first_obj_name})>)"
            
            for name in keys[1:]:
                
                regex += rf"|^(\s*?{name}|\w+?<({name})>)"

        return [regex]

    

    def get_object_names(self, file_path):

        content = self.file_contents[file_path] or GithubTools.get_github_file_content(f, self.repo_api)

        names = set()
        
        if file_path.endswith(".java"):

            try:
            
                package_name = re.search(r"package (.+?);", content).group(1)
                
                class_name = re.search(r"class ([a-zA-Z]+)", content).group(1)

                names.add(f"{package_name}.{class_name}")

                names.add(f"{package_name}.*")

                names.add(f"{class_name}")

            except Exception as e:

                print(f"Could not parse Java class from {file_path}: {e}")
                

        if file_path.endswith(".tld"):

            try:

                root = ET.fromstring(content)

                names.add(root.find("uri").text)
    
                for tag in root.findall("tag"):
                    
                    names.add(tag.find("tag-class").text)
    
                return names

            except Exception as e:

                print(f"Could not parse JSP tag from {file_path}: {e}")

        return names