from . import login_manager, app, admin
from .database import user,db, chat
from flask_admin.contrib.sqla import ModelView


@login_manager.user_loader
def user_loader(id):
    return user.query.get(int(id))


@app.template_filter('datetime')
def datetimeformat(value, format='%d-%m-%Y'):
    return value.strftime(format)

admin.add_view(ModelView(user, db.session))
admin.add_view(ModelView(chat, db.session))
