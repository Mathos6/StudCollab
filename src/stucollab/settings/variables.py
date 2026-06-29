import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

DATABASE_URL = os.environ["DATABASE_URL"]
DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL
    )
}


STORAGE_ACCESS_KEY = os.environ["STORAGE_ACCESS_KEY"]
STORAGE_BUCKET_NAME = os.environ["STORAGE_BUCKET_NAME"]
STORAGE_ENDPOINT_URL = os.environ["STORAGE_ENDPOINT_URL"]
STORAGE_SECRET_KEY = os.environ["STORAGE_SECRET_KEY"]
STORAGE_DEFAULT_REGION = os.environ["STORAGE_DEFAULT_REGION"]
STORAGE_USE_SSL = os.getenv("DEBUG", "True") == "True"




ANYMAIL = {
    "BREVO_API_KEY": os.getenv('BREVO_API_KEY'),
}

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
