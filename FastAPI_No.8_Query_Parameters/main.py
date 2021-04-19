from fastapi import FastAPI
from starlette import templating
from starlette.templating import Jinja2Templates

app = FastAPI()

@app.get('/')
async def root():
    return Jinja2Templates.TemplateResponse()