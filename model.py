from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# from sqlalchemy_imageattchment.entity import Image,image_attachment
# from sqlalchemy_utils import URLType,EmailType
from database import Base

#Creating models for users

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True,nullable=False)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone_number=Column(String)
    # profiles=relationship('Profiles',back_populates="user")
class ProfilePicture(Base):
    __tablename__ = "profile"
    id = Column(Integer,primary_key=True, unique=True)
    profile_picture = Column(ForeignKey("users.id"))
    # user=relationship('User',back_populates="profiles")