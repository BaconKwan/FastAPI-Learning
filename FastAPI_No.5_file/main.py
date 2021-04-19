from typing import List
from fastapi import FastAPI
from fastapi.datastructures import UploadFile
from fastapi.params import File, Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/fileStat1/')
async def fileStat1(
    request:  Request,
    fileList: List[bytes]      = File(...),
    fileName: List[UploadFile] = File(...)
):
    return templates.TemplateResponse(
        'fileStat1.html',
        {
            'request': request,
            'fileSize': [len(file) for file in fileList],
            'fileName': [file.filename for file in fileName]
        }
    )

@app.post('/fileStat2/')
async def fileStat2(
    request: Request,
    file:    bytes      = File(...),
    fileb:   UploadFile = File(...),
    note:    str        = Form(...)
):
    return templates.TemplateResponse(
        'fileStat2.html',
        {
            'request': request,
            'fileSize': len(file),
            'fileName': fileb.filename,
            'note': fileb.content_type
        }
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)