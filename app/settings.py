import os

SECRET_KEY = os.getenv('SECRET_KEY', 'super secret key')

BASE_DIR = os.path.join(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
FILES_DIR = os.path.join(STATIC_DIR, "files")

CV_FILENAME = 'khokhlov_cv_actual.pdf'
# CV_FILENAME = 'khokhlov_cv_old.pdf'