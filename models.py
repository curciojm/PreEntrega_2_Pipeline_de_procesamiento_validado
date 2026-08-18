from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI


def get_model(provider: str):
    if provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=200)
    elif provider == "anthropic":
        return ChatAnthropic(model="claude-sonnet-4-6", temperature=0, max_tokens=200)
    elif provider == "gemini":
        # Agregue max_tokens porque gemini es muy limitada
        return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_tokens=200)
    raise ValueError(f"Proveedor no soportado: {provider}")