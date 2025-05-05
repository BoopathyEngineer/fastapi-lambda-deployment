# from fastapi import FastAPI
# from mangum import Mangum

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# #   # Mangum is used to adapt FastAPI for Lambda
# # handler = Mangum(app)
# from mangum import Mangum

# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# import crud, models, schemas
# from database import SessionLocal, engine
# from typing import List, Optional

# # Initialize the database
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# @app.get("/")
# def read_root():
#     return {"success": "The API is running!"}
# @app.post("/register", response_model=schemas.Member)
# def register_member(member: schemas.MemberBase, db: Session = Depends(get_db)):
#     return crud.create_member(db=db, member=member)

# @app.get("/challenges/today", response_model=List[schemas.Challenge])
# def get_challenges_today(db: Session = Depends(get_db)):
#     return crud.get_challenges(db=db)

# @app.post("/challenges/{challenge_id}/attempt", response_model=schemas.ChallengeAttempt)
# def attempt_challenge(challenge_id: int, member_id: int, db: Session = Depends(get_db)):
#     return crud.attempt_challenge(db=db, member_id=member_id, challenge_id=challenge_id)

# @app.get("/profile", response_model=schemas.Member)
# def get_member_profile(member_id: int, db: Session = Depends(get_db)):
#     return crud.get_profile(db=db, member_id=member_id)
# handler = Mangum(app)
# from fastapi import FastAPI
# from mangum import Mangum

# app = FastAPI()

# @app.get("")
# def read_root():
#     return {"success": "The API is running!"}

# # Create the handler that AWS Lambda will use
# handler = Mangum(app)  # Mangum is used to adapt FastAPI for Lambda
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Lambda!"}
