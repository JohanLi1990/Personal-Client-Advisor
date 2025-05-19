from dotenv import load_dotenv
from fastapi import FastAPI
from app.api import api

load_dotenv()
app = FastAPI()
app.include_router(api.router)

@app.get("/hi")
def greet():
    return {"message": "Hello, World!"}

# use command line uvicorn main:app --reload to run the server
# To run the server, uncomment the following lines
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)