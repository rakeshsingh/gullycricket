import uuid
from flask.ext.login import LoginManager, UserMixin, login_required
from gullycricket import app,models


def get_uuid():
        return str(uuid.uuid4())


def get_login_manager():
    """
    Configure and return login manager for gully cricket app
    :return: login_manager
    """
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view='login'
    return login_manager

login_manager=get_login_manager()
@login_manager.user_loader
def load_user(playerid):
    return models.Player.get(playerid)

