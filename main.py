from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.ollama_service import ask_qwen

app = FastAPI(title="Bank Statement Extractor")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Bank Statement Extractor</title>
        </head>
        <body>
            <h1>🚀 Bank Statement Extractor</h1>
            <p>FastAPI is running successfully.</p>
        </body>
    </html>
    """


@app.get("/ask")
def ask():
    response = ask_qwen("Say hello in one sentence.")
    return {
        "response": response
    }