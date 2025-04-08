from fastapi import FastAPI

app = FastAPI()

@app.get("/") # root
def top():
    return "top here"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)



