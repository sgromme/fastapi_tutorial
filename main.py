from fastapi import FastAPI

app = FastAPI()

@app.get("/") # root
def top():
    return "top here"

@app.get("/echo/{thing}") # command line parameter
def echo(thing: str):
    return f"echoing the man {thing}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)



