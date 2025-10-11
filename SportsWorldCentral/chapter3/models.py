"""SQLALchemy models for SportsWorldCentral database."""


# Firstly import the data types that SQLAlchemy will use for the database fields.
from sqlalchemy import Column, ForeignKey, Integer, String, Date

# Then import the relationship function from SQLAlchemy to define the relationships between the tables.
from sqlalchemy.orm import relationship

from database import Base # refers to the database.py file in the same directory.


# Player class to store data from the SQLite player table.
class Player(Base): # Base class is standard template for the classes in models.py file. 
    __tablename__ = "player" # magic command to tell SQLAlchemy to reference the player table.

    # Define attributes for the Player class.
    player_id = Column(Integer, primary_key=True, index=True) # primary_key definition is beneficial for query optimizatio, enforcing uniqueness and enabling relationaship between classes.
    gsis_id = Column(String, nullable=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    performances = relationship("Performance", back_populates="player")

    # Many-to-many relationship between Player and Team tables
    teams = relationship("Team", secondary="team_player",
                         back_populates="players")


class Performance(Base):
    __tablename__ = "performance"

    performance_id = Column(Integer, primary_key=True, index=True)
    week_number = Column(String, nullable=False)
    fantasy_points = Column(Float, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    player_id = Column(Integer, ForeignKey("player.player_id"))

    player = relationship("Player", back_populates="performances")


class League(Base):
    __tablename__ = "league"

    league_id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String, nullable=False)
    scoring_type = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    teams = relationship("Team", back_populates="league")


class Team(Base):
    __tablename__ = "team"
    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    league_id  = Column(Integer, ForeignKey("league.league_id"))

    league = relationship("League", back_populates="teams")

    players = relationship("Player", secondary="team_player", back_populates="teams")


class TeamPlayer(Base):
    __tablename_ = "team_player"

    team_id = Column(Integer, ForeignKey("team.team_id"), primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("player.player_id"), primary_key=True, index=True)
    last_changed_date = Column(Date, nullable=False)
