from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI

class UserInput(BaseModel):
    email: EmailStr  # Pydantic automatically validates this
#  EmailStr ensures it's a valid RFC-compliant email (safer than regex)
@app.post("/submit")
def submit_email(data:UserInput):
    return {"message": "Email accepted!", "email": data.email}