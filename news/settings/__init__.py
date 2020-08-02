from .base import *

env_name = os.getenv('ENV_NAME', 'local')

if env_name == 'stagi':
    from .stagi import *
elif env_name == 'production':
    from .production import *
else:
    from .local import *
