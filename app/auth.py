# import jwt
# from datetime import datetime, timedelta
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from pydantic import BaseModel
# from app import models
# from sqlalchemy.orm import Session
# from app.database import SessionLocal

# SECRET_KEY = "your_secret_key_here"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30  # The token will expire after 30 minutes

# # OAuth2PasswordBearer is a FastAPI helper to handle token-based authentication.
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Function to create JWT token
# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# # Function to verify JWT token
# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
#     except jwt.JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
# # Dependency to get the current user from the token
# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(SessionLocal)):
#     payload = verify_token(token)
#     user_id = payload.get("sub")
#     if user_id is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#     user = db.query(models.Member).filter(models.Member.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
#     return user

# # A Pydantic model for handling login requests and returning a token
# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class LoginRequest(BaseModel):
#     email: str
#     password: str  # You may need to hash the password when storing and checking it in your database

# # Endpoint to handle user login and return a token (you'll need to implement password checking)
# @app.post("/token", response_model=Token)
# def login_for_access_token(login_request: LoginRequest, db: Session = Depends(SessionLocal)):
#     user = db.query(models.Member).filter(models.Member.email == login_request.email).first()
#     if user is None or login_request.password != "your_password_check_logic_here":  # Replace with actual password check
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
#     access_token = create_access_token(data={"sub": user.id})
#     return {"access_token": access_token, "token_type": "bearer"}
