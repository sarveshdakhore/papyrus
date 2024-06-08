from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from typing import Optional
from sqlalchemy.orm import sessionmaker
from models import *
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from sqlalchemy import and_

DATABASE_URL = "sqlite:///./papyrus.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()
SECRET_KEY = "hhdjkh-cdhjvcn6456mc-cnb"  # Replace with your actual secret key
ALGORITHM = "HS256"  # or "RS256"

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(username: str):
  db = SessionLocal()
  user = db.query(User).filter(User.username == username).first()
  db.close()
  return user

def get_user_by_email(email: str):
  db = SessionLocal()
  user = db.query(User).filter(User.email == email).first()
  db.close()
  return user



def get_user_companies(username: str, db: Session):
  user = db.query(User).filter(User.username == username).first()
  if not user:
    return None

  user_roles = db.query(User_roles).filter(User_roles.user_id == user.id).all()

  companies = []
  for user_role in user_roles:
    team = db.query(Team).filter(Team.id == user_role.team_id).first()
    if team:
      company = db.query(Company).filter(Company.id == team.company_id).first()
      if company and company not in companies:
        companies.append(company)

  return companies


def get_user_teams_in_company(username: str, company_id: int, db: Session):
  user = db.query(User).filter(User.username == username).first()
  if not user:
    return None

  user_roles = db.query(User_roles).filter(User_roles.user_id == user.id).all()

  teams = []
  for user_role in user_roles:
    team = db.query(Team).filter(Team.id == user_role.team_id, Team.company_id == company_id).first()
    if team and team not in teams:
      teams.append(team)

  return teams








async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "YOUR_SECRET_KEY", algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
  user = get_user(form_data.username)  # Replace with your actual DB call
  if not user:
    user = get_user_by_email(form_data.username)  # Replace with your actual DB call
  if not user or not pwd_context.verify(form_data.password, user.hashed_password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password",
      headers={"WWW-Authenticate": "Bearer"},
    )
  token = jwt.encode({"sub": user.username}, SECRET_KEY, algorithm=ALGORITHM)
  return {"access_token": token, "token_type": "bearer"}
# {
#   "username": "your_username",
#   "password": "your_password"
# }
# This endpoint is expecting form data, so make sure to send this JSON body as form data (x-www-form-urlencoded) and not as raw JSON. If you're using a tool like Postman, you can select "x-www-form-urlencoded" under the "Body" tab.

# Regarding JWT (JSON Web Token), after successful login, the server generates a JWT with the user's username as the subject ("sub": user.username) and returns it in the response. This token is then used for authentication in subsequent requests.

# The client should include this token in the Authorization header of their requests, prefixed with the word Bearer. Here's an example:
# Authorization: Bearer your_jwt_token

@app.post("/signup")
def create_user(username: str, email: str, password: str):
  db_user = get_user(username)
  if db_user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Username already registered",
    )
  db_user = get_user_by_email(email)
  if db_user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Email already registered",
    )
  hashed_password = pwd_context.hash(password)
  db_user = User(username=username, email=email, hashed_password=hashed_password)
  db = SessionLocal()
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  db.close()
  return {"username": db_user.username, "email": db_user.email}

# {
#   "username": "your_username",
#   "email": "your_email@example.com",
#   "password": "your_password"
# }

def get_metadata():
    return Base.metadata
@app.get("/")
def get_data():
  data = {"result": "OK"}
  return JSONResponse(content=data, status_code=200)


@app.get("/user/{username}/companies")
async def read_user_companies(username: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
  if current_user != username:
    raise HTTPException(status_code=403, detail="Unauthorized")
  companies = get_user_companies(username, db)
  if companies is None:
    raise HTTPException(status_code=404, detail="User not found")
  return companies

@app.get("/user/{username}/teams/{company_id}")
async def read_user_teams_in_company(username: str, company_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
  if current_user != username:
    raise HTTPException(status_code=403, detail="Unauthorized")
  teams = get_user_teams_in_company(username, company_id, db)
  if teams is None:
    raise HTTPException(status_code=404, detail="User or company not found")
  return teams