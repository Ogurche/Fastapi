from fastapi import FastAPI

app = FastAPI(
    title = 'First site'
)

@app.get('/')
async def root():
    """Root get"""
    return {"message": "Hello World"}
