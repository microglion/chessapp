from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, 
                                                unique=True)
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), 
                                                       index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    puzzles: so.WriteOnlyMapped['Puzzle'] = so.relationship(
        back_populates='added_by_user')

    solutions: so.WriteOnlyMapped['PuzzleSolution'] = so.relationship(
        back_populates='solver')
    
    def __repr__(self):
        return '<User {}>'.format(self.username) 
    
class Puzzle(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    fen: so.Mapped[Optional[str]] = so.mapped_column(sa.String(100))
    source: so.Mapped[Optional[str]] = so.mapped_column(sa.String(200))
    page_number: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer())
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, 
                            default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), 
                                               index=True)

    added_by_user: so.Mapped[User] = so.relationship(back_populates='puzzles')
    solutions: so.WriteOnlyMapped['PuzzleSolution'] = so.relationship(
        back_populates='puzzle')
    def __repr__(self):
        return '<Puzzle {}>'.format(self.id)

class PuzzleSolution(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    analysis_text: so.Mapped[str] = so.mapped_column(sa.Text) #User's analysis
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, 
                            default=lambda: datetime.now(timezone.utc)) 
    
    puzzle_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Puzzle.id), 
                                                 index=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), 
                                               index=True)
    
    solver: so.Mapped[User] = so.relationship(back_populates='solutions')
    puzzle: so.Mapped[Puzzle] = so.relationship(back_populates='solutions')

    def __repr__(self):
        return '<PuzzleSolution {}>'.format(self.id)