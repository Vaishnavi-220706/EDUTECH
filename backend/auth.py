from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database, models, schema, utils
router = APIRouter(tags=["Auth"])
@router.post("/register")
def register(user: schema.StudentCreate, db: Session = Depends(database.get_db)):
    if db.query(models.Student).filter(models.Student.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pwd = utils.hash_password(user.password)
    new_user = models.Student(name=user.name, email=user.email, 
    password_hash=hashed_pwd, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
