from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LinkedIn Insights Server is running"}

