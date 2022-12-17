from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/hello")
def hello():
    return JSONResponse({"message": "Hello Ahmet Kartal Huawei Computer"})
