from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import model
import schema
from data_base import SessionLocal, engine


model.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/search', response_model=schema.User)
def get_user_info(user_email: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db=db, user_email=user_email)
    return user


@app.get('/get-user-list', response_model=List[schema.User])
def get_user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@app.post('/create-user', response_model=schema.UserBase)
def create_user(user: schema.UserAdd, db: Session = Depends(get_db)):
    return crud.add_users_data_to_db(db=db, user=user)


@app.put('/update-password', response_model=schema.User)
def update_user_password(select_id: int, update_param: schema.UpdateUser, db: Session = Depends(get_db)):
    details = crud.get_user_by_id(db=db, select_id=select_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_user_password(db=db, details=update_param, select_id=select_id)


@app.delete('/delete-user')
def delete_user(select_id: int, db: Session = Depends(get_db)):
    details = crud.get_users(db=db)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete.")

    try:
        crud.delete_user(db=db, select_id=select_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete {e}")
    return {'delete status': 'success'}
