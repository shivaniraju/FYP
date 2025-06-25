from fastapi import FastAPI,Response
from fastapi.params import Body
from pydantic import BaseModel,validator
from typing import Union
import re
from random import randrange

#create instance of fastAPI
app = FastAPI()

# contents of report:
# 1.	Report’s Deployment Environment
# 2.	Report Sequence Code
# 3.	Report Name
# 4.	Report Requestor
# 5.	Report Requestor’s Department 
# 6.	Report Creator
# 7.	Emails of Report Users
# 8.  Used in Daily OPS meeting 

# make sure frontend ensure proper format is sent back
class Report(BaseModel):
    Dashboard: str
    Report_Sequence_Code: str
    Report_Name: str
    Requestor: str
    Requestor_Department: str
    Creator: str
    User_Emails: list[str]
    Daily_OPS: bool = False

reports_database=[{ "ID":1,"Dashboard": "production",
    "Report_Sequence_Code": "00532",
    "Report_Name": "Report 1",
    "Requestor" : "Shivani",
    "Requestor_Department" : "System Automation",
    "Creator" : "Nelly",
    "User_Emails": ["rajushiv001@hoya.com", "chinnu.raju@hoya.com"]},{ "ID":2,"Dashboard": "uat",
    "Report_Sequence_Code": "00234",
    "Report_Name": "Report 2",
    "Requestor" : "Glenn",
    "Requestor_Department" : "EUV",
    "Creator" : "john",
    "User_Emails": ["rajushiv001@hoya.com", "chinnu.raju@hoya.com"]}]

#path operation
@app.get("/")
def root():
    return {"message":"Welcome"}

# to display the latest BCP and Statistics
# @app.get("/home")
# def get_latest_incident():
#     incident=incidents_database[len(incident_database)-1]
#     return{"detail": incident}


@app.get("/datactr/reports")
def view_reports():
    return {"reports_database": reports_database}


def find_report(id):
    for r in reports_database:
        if r["ID"]==id:
            return r
        
@app.get("/datactr/reports/{id}")
def get_report(id:int, response: Response):
    report=find_report(int(id))
    if not report:
        response.status_code = 404
    return{"report_detail": report}


@app.post("/datactr/reports")
def create_reports(new_report: Report):
    reports_dict = new_report.dict()
    reports_dict['ID'] = randrange(0, 1000000)
    reports_database.append(reports_dict)
    return{"new_rentry":reports_dict}
