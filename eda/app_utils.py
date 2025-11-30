from agentic.crew import CodeToSummary, SummaryToSpec, SpecToCode
from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Optional
from pydantic import Field, BaseModel
from crewai_tools import SerperDevTool
from crewai.tools import tool
from crewai.flow.flow import Flow, listen, start
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from custom.dependency_parser import JspDependencyParser, GithubTools
load_dotenv()
import asyncio
import nest_asyncio
nest_asyncio.apply()


##############################################################################
# Structured Output
##############################################################################

class FileCluster(BaseModel):
    cluster_id: int = Field(description="Cluster identifier", default=0)

    files: List[str] = Field(
        description="List of files associated with this cluster")


class GitRepo(BaseModel):
    repo_id: str = Field(description="Git repo identifier", default="0")

    repo_url: str = Field(description="Git repo URI")

    repo_branch_sha: str = Field(description="Git branch SHA")

    summary: Optional[str] = Field(
        description="Summary of the aggregated file content", default="")

    clusters: Optional[List[FileCluster]] = Field(
        description="Ranked list of file clusters ordered by number of dependencies",
        default=[])


##############################################################################
# Helper Functions
##############################################################################

def rank_relevant_files(github_repo: str, tree_sha: str):
    def get_clusters(files, start_index=0):
        """Splits the list of files into clusters."""

        idx = start_index

        while idx < len(files):
            current_degree = files[idx][0]

            cluster_size = len(
                [degree for degree, _ in files if degree == current_degree])

            cluster = files[idx:idx + cluster_size]

            cluster_files = [f for _, f in cluster]

            yield cluster_files

            idx = idx + cluster_size

    parser = JspDependencyParser(github_repo, tree_sha)

    ranked_files = parser.get_ranked_files_by_outdegree()

    ranked_file_clusters = list(get_clusters(ranked_files))

    return ranked_file_clusters


def get_github_files(github_repo: str, tree_sha: str):
    repo_api = GithubTools.get_git_repo_api(github_repo)

    return GithubTools.get_relevant_files(tree_sha, repo_api)


def get_aggregated_github_file_content(github_repo: str,
                                       repo_files: List[str]):
    repo_api = GithubTools.get_git_repo_api(github_repo)

    output = [
        f"""============={f}\n{GithubTools.get_github_file_content(f.strip(), repo_api)}"""
        for f in repo_files]

    output = "\n".join(output)

    return output