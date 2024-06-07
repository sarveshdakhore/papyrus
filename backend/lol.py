from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "sqlite:///./papyrus.db"
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)
