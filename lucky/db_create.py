from database import db
from database import user

db.create_all()

db.session.add(user("test","test","test"))

db.session.commit()