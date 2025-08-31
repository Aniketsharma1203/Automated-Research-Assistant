from agents import create_agents

def main():

    # This line is crucial to initialize the DSPy configuration
    import config

    researcher, user_proxy = create_agents()

    research_plan = """
    I need a literature review on the topic: **'How AI will transoform the IT Jobs?'**

    Please follow these steps:
    1.  First, use the `generate_search_query` tool to create an expert-level search query for this topic.
    2.  Next, use the `search_and_scrape` tool with the generated query to find and retrieve the content of a relevant academic paper.
    3.  After that, use the `summarize_paper` tool on the retrieved text to get a concise summary.
    4.  Finally, use the `synthesize_review` tool with the summary you created to write a brief, one-paragraph literature review.
    5.  Report the final literature review and then say TERMINATE.
    """

    user_proxy.initiate_chat(
        researcher,
        message=research_plan
    )

if __name__ == "__main__":
    main()
