from pydantic import BaseModel
from typing import List,Optional
class StudentCreate(BaseModel):
    name:str
    email:str
    password:str
    phno:str
    role:Optional[str]="student"
class Token(BaseModel):
    access_token:str
    token_type:str
class CourseCreate(BaseModel):
    #same field names created in models course table
    coursename:str
    coursedesc:str
    price:str
class LessonCreate(BaseModel):
    courseid:int
    lesson_title:str
    video_url:str