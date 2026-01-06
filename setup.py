from setuptools import setup, find_packages

setup(
    name="ai-cli",
    version="2.0",
    description="AI-powered CLI assistant with Gemini LLM command generation",
    packages=find_packages(),
    install_requires=[
        "google-generativeai>=0.3.0",  # For Gemini API
        "requests>=2.28.0",  # For Ollama API
        "python-dotenv>=0.19.0",  # For loading .env files
    ],
    entry_points={
        "console_scripts": [
            "ai-cli=ai_cli.main:main"
        ]
    },
    python_requires=">=3.10",
)
