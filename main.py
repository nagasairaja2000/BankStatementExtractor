from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.upload import router as upload_router

app = FastAPI(title="Bank Statement Extractor")

templates = Jinja2Templates(directory="templates")

app.include_router(upload_router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )