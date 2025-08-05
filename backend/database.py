from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL="mysql+pymysql://root:ammu@2060@localhost:3306/edtech_platform"
engine=create_engine(DB_URL,pool_pre_ping=True,echo=True)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()