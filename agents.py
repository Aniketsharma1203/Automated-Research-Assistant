import autogen
from config import AUTOGEN_CONFIG_LIST
from tools.dspy_tools import generate_search_query, summarize_paper, syntesize_review
from tools.web_tools import search_and_scrape

def create_agents():
    """Creates and configures the researcher and user proxy agents."""
    researcher = autogen.AssistantAgent(
        name = 'Researcher',
        system_message="You are an expert researcher. Use the provided tools to follow the user's plan step-by-step. Only use one tool at a time. Do not make up information. Use a tool to get new information.",
        llm_config={"config_list": AUTOGEN_CONFIG_LIST},
    )

    user_proxy = autogen.UserProxyAgent(
        name="User_Proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config=False,
    )

    # Register all tools with the user_proxy

    user_proxy.register_function(
        function_map={
            "generate_search_query": generate_search_query,
            "search_and_scrape": search_and_scrape,
            "summarize_paper": summarize_paper,
            "synthesize_review": syntesize_review,
        }
    )
    print("✅ AutoGen agents created and tools registered.")
    return researcher, user_proxy