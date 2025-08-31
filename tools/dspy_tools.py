import dspy

# --- DSPy Signatures ---

class generateSearchQuery(dspy.Signature):
    """Generates a concise, expert-level search query for an academic search engine."""
    research_topic = dspy.InputField(desc = "The research topic or question to be explored.")
    search_query = dspy.OutputField(desc = "A concise, expert-level search query for an academic search engine.")

class summarizePaper(dspy.Signature):
   """Summarizes a research paper, focusing on methodology, findings, and conclusions."""
   paper_text = dspy.InputField(desc = "The full text of the research paper to be summarized.")
   summary = dspy.OutputField(desc = "A concise summary of the paper's key points.")

class SynthesizeReview(dspy.Signature):
    """Synthesizes multiple paper summaries into a coherent literature review."""
    research_topic = dspy.InputField(desc = "The research topic or question being explored.")
    paper_summaries = dspy.InputField(desc = "A list of summaries from various research papers.")
    literature_review = dspy.OutputField(desc = "A synthesized literature review based on the provided summaries.")


# --- DSPy Module: The Toolbox ---
class ResearchAssistantModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.query_generate = dspy.Predict(generateSearchQuery)
        self.summarizer = dspy.Predict(summarizePaper)
        self.synthesizer = dspy.Predict(SynthesizeReview)

    def forward(self, task, **kwargs):
        if task == "generate_query":
            return self.query_generate(research_topic = kwargs['research_topic'])
        elif task == "summarize_paper":
            return self.summarizer(paper_text=kwargs['paper_text'])
        elif task == "synthesize":
            return self.synthesizer(research_topic=kwargs['research_topic'],paper_summaries=kwargs['paper_summaries'])
        
research_toolbox = ResearchAssistantModule()
print("✅ DSPy expert tools are built.")


# --- Wrapper Functions for AutoGen ---

def generate_search_query(research_topic: str) -> str:
    print(f"\n>>>> Calling DSPy (Groq) to generate search query for: {research_topic}")
    result = research_toolbox.forward('generate_query', research_topic=research_topic)
    return result.search_query

def summarize_paper(paper_text: str) -> str:
    print("\n>>>> Calling DSPy (Groq) to summarize paper...")
    result = research_toolbox.forward('summarize_paper', paper_text=paper_text)
    return result.summary

def syntesize_review(research_topic: str, summaries: str) -> str:
    print("\n>>>> Calling DSPy (Groq) to synthesize the final review...")
    result = research_toolbox.forward('synthesize', research_topic = research_topic, paper_summaries = summaries)
    return result.literature_review
