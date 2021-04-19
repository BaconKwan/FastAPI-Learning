from typing import Dict
from fastapi import FastAPI
from enum import Enum

class Name(str, Enum):
    Alan  = 'AAA'
    Bacon = 'BBBB'
    Candy = 'CCCCC'

app = FastAPI()

@app.get('/api/{name}')
async def name(name: Name):
    if name == Name.Alan:
        return {'name': f'{Name.Alan.name}', 'msg': f'{Name.Alan.name} say: {name.value}!'}
    elif name.value == 'BBBB':
        return {'name': f'{Name.Bacon.name}', 'msg': f'Bacon say: BBBBBBBBBBB'}
    else:
        return {'name': 'Candy', 'msg': 'Candy say nothing.'}

@app.get('/')
async def root():
    return {'msg': 'Hello, FastAPI!'}

if __name__ == '__main__':
    import uvicorn
    # uvicorn.run(app, host='127.0.0.1', port=8000)
    uvicorn.run('main2:app', host='127.0.0.1', port=8000, reload=True)