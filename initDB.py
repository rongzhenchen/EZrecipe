from main import app
from models import db, User
import json

db.create_all(app=app)

print('database initialized!')