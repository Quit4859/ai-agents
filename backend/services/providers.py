PROVIDERS = {
    "nebius": {"base_url": "https://api.studio.nebius.ai/v1", "env": "NEBIUS_API_KEY", "default_model": "nvidia/nemotron-4-340b-instruct"},
    "openai": {"base_url": "https://api.openai.com/v1", "env": "OPENAI_API_KEY", "default_model": "gpt-4o-mini"},
    "gemini": {"base_url": "https://generativelanguage.googleapis.com/v1beta/openai", "env": "GEMINI_API_KEY", "default_model": "gemini-1.5-flash"},
    "groq": {"base_url": "https://api.groq.com/openai/v1", "env": "GROQ_API_KEY", "default_model": "llama-3.3-70b-versatile"},
    "together": {"base_url": "https://api.together.xyz/v1", "env": "TOGETHER_API_KEY", "default_model": "meta-llama/Llama-3.3-70B-Instruct-Turbo"},
    "mistral": {"base_url": "https://api.mistral.ai/v1", "env": "MISTRAL_API_KEY", "default_model": "mistral-small-latest"},
}
