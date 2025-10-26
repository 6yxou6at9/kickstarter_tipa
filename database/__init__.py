from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# Указываем типа базы данных (sqlite3, postgresql)
SQL_DATABASE = 'sqlite:///sm.db'

# Создание бд
engine = create_engine(SQL_DATABASE)

# Создаем сессию чтобы хранить данные
SessionLocal = sessionmaker(bind=engine)

# Создаем полноценную базу
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()