from fastapi import FastAPI
from fastapi.params import Form
from starlette.requests import Request
from starlette.routing import Host
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
template = Jinja2Templates(directory='templates')
app.mount(path='/static', app=StaticFiles(directory='static'), name='static')

@app.post('/login/')
async def login(
    request: Request,
    username: str     = Form(...),
    password: str     = Form(...)
):
    print(f'用户名是{username}，密码是{password}')
    return template.TemplateResponse(
        'index.html',
        {
            'request': request,
            'username': username
        }
    )

@app.get('/')
async def root(requset: Request):
    return template.TemplateResponse('signin.html', {'request': requset})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)