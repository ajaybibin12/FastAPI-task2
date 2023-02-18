from fastapi import FastAPI,Depends,Response,status,HTTPException,File,UploadFile
import schemas,model

app = FastAPI()

from database import engine,SessionLocal
model.Base.metadata.create_all(engine)
from sqlalchemy.orm import Session  

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Here is the function that add a user into a database
@app.post("/",status_code=200)
def create(request: schemas.newusers,db: Session = Depends(get_db)):
    new_users = model.User(name=request.name,email=request.email,password=request.password,phone_number=request.phone_number)
    if request.email == model.User.email and request.phone_number==model.User.phone_number:
            # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=404,detail="User already exists")
    else:
        db.add(new_users)
        db.commit()
        db.refresh(new_users)
        return new_users


#Here is the function that add a user profile picutre into a database
@app.post("/file_upload")
def profile(file:UploadFile,db: Session = Depends(get_db)):
    profiles=model.ProfilePicture(profile_picture=file.filename)
    db.add(profiles)
    db.commit()
    db.refresh(profiles)
    # return {"user profile":file.filename}
    return profiles

#showing all the users here
@app.get("/show_users")
def show_users(db: Session = Depends(get_db)):
    show_all=db.query(model.User).all()
    return show_all