import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from agentic.crew import CodeToSummary, SummaryToSpec, SpecToCode
from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from crewai.tools import tool
from crewai.flow.flow import Flow, listen, start
import app_utils
from custom.dependency_parser import GithubTools
from urllib.parse import urlparse
import traceback
import litellm
litellm.set_verbose=True
import nest_asyncio
nest_asyncio.apply()


st.set_page_config(page_title="AI Code Generation", page_icon="🧠",
                   layout="wide")


st.title("🧠️ AI Legacy Code Translation - Demo")
st.markdown("<br>Translates <b>JSP</b> code to <b>NodeJS</b> and "
            "<b>React.</b>", unsafe_allow_html=True)
st.markdown("---")

# Main content area
col1, col2 = st.columns(2, vertical_alignment="bottom")

with col1:
    git_repo = st.text_input("Git repository",
                          placeholder="https://github.com/user/repo")
    git_branch_sha = st.text_input("Git branch",
                          placeholder="main, master, etc.")
    selected_model = st.selectbox(
        "Model",
        ("", "CANDIDATE_LORA", "CANDIDATE_DORA"),
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    run_button = st.button("🚀 Run", type="primary",
                           use_container_width=True)

# Status and output area
status_container = st.container()
output_container = st.container()


##############################################################################
# Flows
##############################################################################


class CodeTranslationFlow(Flow):
    """Flow for CodeTranslation."""

    @start()
    def retrieve_code(self):

        print(
            f"Starting flow {self.state['id']} for {self.state["repo_url"]}#{self.state["repo_branch_sha"]}...")

        github_repo, tree_sha = self.state["repo_url"], self.state[
            "repo_branch_sha"]

        clusters = app_utils.rank_relevant_files(github_repo, tree_sha)

        self.state["clusters"] = [{"files": cluster} for cluster in clusters]

        self.state["summary"] = ""

    @listen(retrieve_code)
    def analyze_code(self):

        def analyze_code_cluster(cluster, cluster_id, running_summary):

            repo_files = cluster["files"]

            repo_url = self.state["repo_url"]

            repo_id = self.state["repo_id"]

            inputs = app_utils.get_aggregated_github_file_content(repo_url,
                                                           repo_files)

            output = CodeToSummary(self.state["selected_model"]).crew().kickoff(inputs={"inputs": inputs,

                                                            "summary": running_summary,

                                                            "output_base_path": f"{repo_id}/{cluster_id}",})

            return output

        # Get aggregate summary of code

        running_summary = self.state.get("summary", "")

        for cluster_id, cluster in enumerate(self.state["clusters"]):

            self.state["cluster_id"] = cluster_id

            output_section = analyze_code_cluster(cluster, cluster_id,
                                                  running_summary)

            files_section = "\n  -".join(cluster["files"])

            if not running_summary:
                running_summary = "Context:\n=======\n"

            running_summary += f"\n -{files_section}\n=======\n{output_section}"

        # Get spec from aggregate summary
        spec = SummaryToSpec(self.state["selected_model"]).crew().kickoff(
            inputs={"inputs": running_summary,

                    "output_base_path": f"{self.state["repo_id"]}",})

        return spec.raw

    @listen(analyze_code)
    def generate_code(self, spec):

        print("Generating code!...")

        repo_id = self.state["repo_id"]

        SpecToCode(self.state["selected_model"]).crew().kickoff(inputs={"spec": spec,

                                            "output_base_path": f"{repo_id}",

                                            "code_base_path": f"{repo_id}/code",})


# Run the workflow when button is clicked
if run_button:
    if not git_repo or not git_branch_sha or not selected_model:
        st.error("⚠️ Git repository, branch and model are required fields.")
    else:
        with status_container:
            with st.spinner("🤖 Working on it..."):
                try:
                    progress_bar = st.progress(0)

                    status_text = st.empty()

                    flow = CodeTranslationFlow()

                    flow.plot("CodeTranslationFlowPlot")

                    repo_id = ("_").join(
                        urlparse(git_repo).path.split("/")[1:])

                    status_text.text(
                        "🔍 Code Analyzer is analyzing the code information...")

                    progress_bar.progress(33)

                    result = flow.kickoff(inputs={"repo_url": git_repo,

                                                  "repo_branch_sha": git_branch_sha,

                                                  "repo_id": repo_id,

                                                  "selected_model": selected_model})

                    progress_bar.progress(100)

                    status_text.text("✅ Code translation complete.")

                    # Display the result
                    with output_container:
                        st.markdown("---")
                        st.subheader("📄 Generated Code")
                        st.markdown(result)

                        # Download button
                        st.download_button(
                            label="Download Code",
                            data=str(result),
                            file_name=f"generated_code.md",
                            mime="text/plain"
                        )

                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
                    traceback.print_exc()

# Footer
st.markdown("---")
