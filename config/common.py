import pathlib

class BaseConfig:

    debug = True
    app_name = 'Social Network'
    database_name = 'baldej_db'
    secret_key = b'TyzLMReLCWUiPsTFMActw_0dtEU7kAcFXHNYYm64DNI='

    PROJECT_ROOT = pathlib.Path(__file__).parent.parent
    STATIC_DIR = str(PROJECT_ROOT / 'static')
