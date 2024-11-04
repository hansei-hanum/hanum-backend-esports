from database.core import Base, engine
import sqlalchemy

Base.metadata.create_all(engine)