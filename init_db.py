from models import engine
from models.article import *
from models.vote_record import *

Base.metadata.create_all(engine)