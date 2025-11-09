from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

class UserManager:
    @staticmethod
    def get_user(user_id):
        session = Session()
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                return {
                    "id": user.id,
                    "name": user.name,
                    "age": user.age
                }
            else:
                return None
        finally:
            session.close()


    @staticmethod
    def get_all_user():
        session = Session()
        try:
            users = session.query(User).all()
            listUsers = []
            for user in users:
                listUsers.append({
                    "id": user.id,
                    "name": user.name,
                    "age": user.age
                })
            return listUsers
        finally:
            session.close()



    @staticmethod
    def add_user(info_user):
        session = Session()
        try:
            user = User(name=info_user["name"], age=info_user["age"])
            session.add(user)
            session.commit()
            session.refresh(user)
            return {
                "id": user.id,
                "name": user.name,
                "age": user.age
            }
        finally:
            session.close()

    @staticmethod
    def update_user(user_id, user_info):
        session = Session()
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                return False
            user.name = user_info["name"]
            user.age = user_info["age"]
            session.commit()
            return {
                "id": user.id,
                "name": user.name,
                "age": user.age
            }
        finally:
            session.close()

    @staticmethod
    def delete_user(user_id):
        session = Session()
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                return False
            session.delete(user)
            session.commit()
            return {
                "id": user.id,
                "name": user.name,
                "age": user.age
            }
        finally:
            session.close()