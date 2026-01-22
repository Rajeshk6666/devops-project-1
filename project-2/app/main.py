from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Project 2 live ✅ DevSecOps CI/CD pipeline running!"}

@app.get("/health")
def health():
    return {"status": "ok"}
