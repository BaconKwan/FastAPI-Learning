from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'name': 'Bacon'})

@app.get('/{item}')
def getItem(request:Request, item: int):
    return templates.TemplateResponse('index.html', {'request': request, 'name': item})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)