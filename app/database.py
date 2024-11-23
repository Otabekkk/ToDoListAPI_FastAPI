from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DBURL = 'postgresql://postgres:ztw02@localhost:5432/QuizApplication'

engine = create_engine(DBURL)

SessionaLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Базовый класс для моделей #
Base = declarative_base()


# Фнукция для получения сессии
def get_db():
    db = SessionaLocal()

    try:
        yield db
    
    finally:
        db.close()

  