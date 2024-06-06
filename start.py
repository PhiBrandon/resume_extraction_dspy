import dspy
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from fastapi import FastAPI


load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")


app =FastAPI()


class ResumeInput(BaseModel):
    resume: str

class ResumeExtraction(BaseModel):
    education: list[str]
    job_titles: list[str]
    years_of_experience: int
    certifications: list[str]


llm = dspy.dsp.modules.anthropic.Claude(model="claude-3-haiku-20240307", api_key=api_key, max_tokens=4000)
dspy.settings.configure(lm=llm)



class ResumeExtractor(dspy.Signature):
    resume: str = dspy.InputField()
    resume_extracted: ResumeExtraction = dspy.OutputField()

class ResumeModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.resume_extraction = dspy.TypedPredictor(ResumeExtractor)
    
    def forward(self, resume):
        return self.resume_extraction(resume=resume).resume_extracted


""" output = ResumeModule()
runed = output(resume=open("resume.txt", "r").read())
print(runed) """


@app.post("/extract", response_model=ResumeExtraction)
def run_extraction(resume: ResumeInput) -> ResumeExtraction:
    output = ResumeModule()
    runed = output(resume=resume.resume)
    print(runed)
    return runed