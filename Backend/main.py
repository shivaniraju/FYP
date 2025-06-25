from fastapi import FastAPI

#create instance of fastAPI
app = FastAPI()

#path operation
@app.get("/")
def root():
    return {"message":"Welcome"}

@app.get("/datactr/reports")
def view_reports():
    return {"data": "this is the list of reports"}

@app.get("/datactr/errorflow")
def view_ef():
    return {"data":"this is the error flow"}