from fastapi import FastAPI
import uvicorn
from endpoints import registration_route
from db import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    registration_route(app)
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)