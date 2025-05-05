# from pydantic import BaseModel
# from datetime import datetime
# from typing import List, Optional

# class MemberBase(BaseModel):
#     name: str
#     email: str
#     phone: str

# class Member(MemberBase):
#     id: int
#     total_points: int

#     class Config:
#         orm_mode = True

# class ChallengeBase(BaseModel):
#     title: str
#     description: str
#     reward_points: int
#     valid_from: datetime
#     valid_to: datetime

# class Challenge(ChallengeBase):
#     id: int

#     class Config:
#         orm_mode = True

# class ChallengeAttemptBase(BaseModel):
#     challenge_id: int
#     points_earned: int

# class ChallengeAttempt(ChallengeAttemptBase):
#     attempt_time: datetime

#     class Config:
#         orm_mode = True
