from pydantic import BaseModel

class newusers(BaseModel):
    id:"int"
    name:"str"
    email:"str"
    phone_number:"str"
    password:"str"