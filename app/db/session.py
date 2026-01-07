from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database file
DATABASE_URL = "sqlite:///./app.db"

# Create engine (connects Python to DB)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # required for SQLite
)

# Session = DB connection per request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
