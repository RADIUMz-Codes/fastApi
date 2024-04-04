from fastapi import FastAPI, UploadFile, File
import shutil
from fastapi.middleware.cors import CORSMiddleware
# Create a FastAPI application
app = FastAPI()

# app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define a route at the root web address ("/")
@app.get("/")
def read_root():
	return {"message": "Hello, FastAPI!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"./uploads/cv/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"./uploads/cv/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.post("/uploadjd/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"./uploads/jd/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}