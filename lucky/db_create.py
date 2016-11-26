from database import db
from database import user

db.create_all()

db.session.add(user("test","test@gmx.de","test"))
db.session.add(user("test2","test2@gmx.de","test2"))
db.session.add(user("kaiser","kaiser@gmx.de","kaiser"))
db.session.commit()