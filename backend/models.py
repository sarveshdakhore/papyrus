from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
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
  auth_tokens = relationship("AuthToken", back_populates="user")  # Add this line
  leave_balance = relationship("LeaveBalance", uselist=False, back_populates="user")
  

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
  tasks = relationship("Task", back_populates="team")  # Add this line

  
class User_roles(Base):
  __tablename__ = 'user_roles'
  id = Column(Integer, primary_key=True, index=True)
  role = Column(String, index=True)
  team_id = Column(Integer, ForeignKey('teams.id'))
  team = relationship("Team", back_populates="user_roles")
  user_id = Column(Integer, ForeignKey('users.id'))  
  user = relationship("User", back_populates="roles")
  
class Task(Base):
  __tablename__ = 'tasks'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  deadline = Column(DateTime)
  content = Column(String)
  completed = Column(Boolean, default=False)
  started = Column(Boolean, default=False)
  assigned_to = Column(Integer, ForeignKey('users.id'))
  assigned_from = Column(Integer, ForeignKey('users.id'))
  team_id = Column(Integer, ForeignKey('teams.id'))
  team = relationship("Team", back_populates="tasks")
  
class AuthToken(Base):
  __tablename__ = 'auth_tokens'
  id = Column(Integer, primary_key=True, index=True)
  usrname = Column(String, index=True)
  token = Column(String, index=True)
  type = Column(String, index=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship("User", back_populates="auth_tokens")
  
  def __init__(self, token, usrname, type, user_id):
    self.token = token
    self.usrname = usrname
    self.type = type
    self.user_id = user_id
    
class LeaveBalance(Base):
  __tablename__ = 'leave_balances'
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  sick_leave = Column(Integer, default=0)
  casual_leave = Column(Integer, default=0)
  unpaid_leave = Column(Integer, default=0)
  half_leave = Column(Integer, default=0)
  user = relationship("User", back_populates="leave_balance")

  def __init__(self, user_id, sick_leave=0, casual_leave=0, unpaid_leave=0, half_leave=0):
    self.user_id = user_id
    self.sick_leave = sick_leave
    self.casual_leave = casual_leave
    self.unpaid_leave = unpaid_leave
    self.half_leave = half_leave