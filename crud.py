from sqlalchemy.orm import Session
import model
import schema


def get_user_by_email(db: Session, user_email: str):
    return db.query(model.Users).filter(model.Users.email == user_email).first()


def get_user_by_id(db: Session, select_id: int):
    return db.query(model.Users).filter(model.Users.id == select_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Users).offset(skip).limit(limit).all()


def add_users_data_to_db(db: Session, user: schema.UserAdd):
    user_data = model.Users(
        username=user.username,
        email=user.email,
        password=user.password,
        register_date=user.register_date
    )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return model.Users(**user.dict())


def update_user_password(db: Session, select_id: int, details: schema.UpdateUser):
    db.query(model.Users).filter(model.Users.id == select_id).update(vars(details))
    db.commit()
    return db.query(model.Users).filter(model.Users.id == select_id).first()


def delete_user(db: Session, select_id: int):
    try:
        db.query(model.Users).filter(model.Users.id == select_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
