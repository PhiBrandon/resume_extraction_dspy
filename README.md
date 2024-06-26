# DSPy Resume Infromation Extraction w/ Frontend
This project shows how to use DSPy to extract information from document, specifically resumes.

*IMPORTANT* - LLMs contain bias, thus this should be modified and used responsibly.

## Setup
1. Create virtual environment `python3 -m venv dspy-venv`
    - Initialize environment `source dspy-venv/bin/activate`
2. Install libraries
    - `pip install -r requirements.txt`
3. Create environment file
    - `touch .env`
4. Install Nuxt 3 Files
    - `cd frontend && npm install`
5. Run API server
    - `cd .. && fastapi dev start.py`
6. Run Frontend
    - `cd frontend && npm run dev`

If you are following the tutorial the `resume.json` is a properly formatted json object of the parameters that need to be passed to the API.

Tutorial: https://youtu.be/iAPfIZ-gAGc

Enjoy!