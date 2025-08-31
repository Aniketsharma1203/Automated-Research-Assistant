import os
import dspy
from dotenv import load_dotenv

def setup_env():
    """Load environment variables from a .env file."""
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    return api_key


def configure_dspy(api_key):
    """Configures the DSPy language model."""
    # When using dspy.OpenAI for a non-OpenAI service, you must provide the api_base.
    groq_llama3 = dspy.LM(
       model='llama-3.3-70b-versatile',
        api_base='https://api.groq.com/openai/v1',
        api_key=api_key,
    )

    dspy.settings.configure(lm=groq_llama3)
    print("✅ DSPy configured for Llama 3 via Groq.")

def get_autogen_config(api_key):
    """Returns the AutoGen model configuration."""
    return [{
        'model': 'llama-3.3-70b-versatile',
        'base_url': 'https://api.groq.com/openai/v1',
        'api_key': api_key
    }]

# Initial setup
GROQ_API_KEY = setup_env()
configure_dspy(GROQ_API_KEY)
AUTOGEN_CONFIG_LIST = get_autogen_config(GROQ_API_KEY)