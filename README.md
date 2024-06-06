# DSPy Resume Infromation Extraction w/ Frontend
This project shows how to use DSPy to extract information from document, specifically resumes.
*IMPORTANT* - LLMs contain bias, thus this should be modified and used responsibly.

## Setup
1. Create virtual environment `python3 -m venv dspy-venv`
    - Initialize environment `source dspy-venv/bin/activate`
2. Install libraries
    - `pip install anthropic dspy python-dotenv fastapi pydantic`
3. Create environment file
    - `touch .env`
4. Install Nuxt 3 Files
    - `cd frontend && npm install`
5. Run API server
    - `cd .. && fastapi dev start.py`
6. Run Frontend
    - `cd frontend && npm run dev`

Enjoy!