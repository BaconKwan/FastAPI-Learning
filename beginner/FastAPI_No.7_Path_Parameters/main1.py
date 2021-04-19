from fastapi import FastAPI

app = FastAPI()

@app.get('/api/xx')
async def xx():
    return {'msg': 'xx'}

@app.get('/api/{itemID}')
async def itemID(itemID:str):
    return {itemID: itemID}

# 固定参数的API不能放在后面
# @app.get('/api/xx')
# async def xx():
#     return {'msg': 'xx'}

@app.get('/')
async def root():
    return {'msg': 'Hello, FastAPI!'}

if __name__ == '__main__':
    import uvicorn
    #uvicorn.run(app, host='127.0.0.1', port=8000)
    uvicorn.run('main1:app', host='127.0.0.1', port=8000, reload=True)