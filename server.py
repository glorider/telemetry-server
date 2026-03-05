from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/collect")
async def collect(request: Request):
    data = await request.json()
    print(data)
    return {"status": "received"}
