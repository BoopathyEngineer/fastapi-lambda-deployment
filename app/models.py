# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from database import Base

# class Member(Base):
#     __tablename__ = "members"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     phone = Column(String, unique=True)
#     total_points = Column(Integer, default=0)

#     challenges = relationship("Challenge", secondary="challenge_attempts")

# class Challenge(Base):
#     __tablename__ = "challenges"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String)
#     reward_points = Column(Integer)
#     valid_from = Column(DateTime)
#     valid_to = Column(DateTime)

# class ChallengeAttempt(Base):
#     __tablename__ = "challenge_attempts"

#     member_id = Column(Integer, ForeignKey("members.id"), primary_key=True)
#     challenge_id = Column(Integer, ForeignKey("challenges.id"), primary_key=True)
#     attempt_time = Column(DateTime, server_default=func.now())
#     points_earned = Column(Integer)

#     member = relationship("Member")
#     challenge = relationship("Challenge")
