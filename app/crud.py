from sqlalchemy.orm import Session
import models, schemas

def create_member(db: Session, member: schemas.MemberBase):
    db_member = models.Member(name=member.name, email=member.email, phone=member.phone)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_challenges(db: Session):
    return db.query(models.Challenge).filter(models.Challenge.valid_from <= datetime.datetime.now(), models.Challenge.valid_to >= datetime.datetime.now()).all()

def attempt_challenge(db: Session, member_id: int, challenge_id: int):
    challenge = db.query(models.Challenge).filter(models.Challenge.id == challenge_id).first()
    member = db.query(models.Member).filter(models.Member.id == member_id).first()

    if challenge and member:
        points_earned = challenge.reward_points
        challenge_attempt = models.ChallengeAttempt(member_id=member.id, challenge_id=challenge.id, points_earned=points_earned)
        db.add(challenge_attempt)
        db.commit()

        member.total_points += points_earned
        db.commit()

        return challenge_attempt

def get_profile(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.id == member_id).first()
