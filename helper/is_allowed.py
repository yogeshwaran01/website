from app.config import Configaration


def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Configaration.ALLOWED_EXTENSIONS
