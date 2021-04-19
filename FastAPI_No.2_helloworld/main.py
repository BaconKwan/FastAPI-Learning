from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return{'msg': 'Hello, World!'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)

# 官方推荐用CLI来执行uvicron
# uvicorn main.py:app --reload