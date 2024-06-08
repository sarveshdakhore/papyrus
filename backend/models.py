from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship  # Import the relationship class
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  full_name = Column(String)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  disabled = Column(Boolean, default=False)
  roles = relationship("User_roles", back_populates="user") 
  
  

class Company(Base):
  __tablename__ = 'companies'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  description = Column(String)
  company_owner = Column(Integer, ForeignKey('users.id'))
  teams = relationship("Team", back_populates="company")
  
class Team(Base):
  __tablename__ = 'teams'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  description = Column(String)
  company_id = Column(Integer, ForeignKey('companies.id'))
  company = relationship("Company", back_populates="teams")
  user_roles = relationship("User_roles", back_populates="team")
  
class User_roles(Base):
  __tablename__ = 'user_roles'
  id = Column(Integer, primary_key=True, index=True)
  role = Column(String, index=True)
  team_id = Column(Integer, ForeignKey('teams.id'))
  team = relationship("Team", back_populates="user_roles")
  user_id = Column(Integer, ForeignKey('users.id'))  
  user = relationship("User", back_populates="roles")