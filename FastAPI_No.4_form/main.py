from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/login/')
def getItem(request:Request, username: str = Form(...), password: str = Form(...)):
    #print(username + password)
    #Form表单返回格式{'peramA': 'AAA', 'peramsB': 'BBB'}
    return templates.TemplateResponse('login.html', {'request': request, 'username': username, 'password': password})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)