from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
app = FastAPI()



@app.get("/")
async def read_root():
    data = {"message": "This is a simple FastAPI application."}
    return JSONResponse(content=data)

@app.get("/jokes")
def get_jokes():
    return JSONResponse(content={"joke": "Why did the scarecrow win an award? Because he was outstanding in his field!"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)