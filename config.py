import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'


    #BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image19'
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image19new'
    #BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'f48PPzbtI08VIDONxiDptUE3H/cN3VU1SPVjUgaY0Zr5fZnLE0++Cha13IG94Kig81AOYE8xh1Nk+AStPWmBeQ=='
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'tygRIMIIsrR1dChzZFF+VBii7eSYi9VLhysRygYXPgmofnm9RzTmf0TgqJKPXgc9Gectvr5v/LQT+ASt/mtZgA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'


    #SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms19.database.windows.net'
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsnew.database.windows.net'
    #SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmsnew'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
    # Below URI may need some adjustments for driver version, baazuresed on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    #CLIENT_SECRET = "Fxb8Q~aHi~5xfAKnJ5jVziwzntsTFAcX5FONjbXv"
    CLIENT_SECRET = "BCS8Q~Y7Oy6oE0wPU78J9zEn4Gg4QXJZBuGmibbU"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")


    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"


    #CLIENT_ID = "0ffdb341-d5c0-42b4-814b-e9b94fb76024"
    CLIENT_ID = "3494caa0-f78c-4fd1-9ebd-b98970887627"


    #REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/https://image19.azurewebsites.net/getAToken"
    #REDIRECT_PATH = "/https://cmswebapp-f0d7f4e4f3g5f0fy.canadacentral-01.azurewebsites.net/getAToken"



    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app


    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
