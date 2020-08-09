
from .base import *

env_name = env('ENV_NAME')

if env_name == 'stagi':
    from .stagi import *
elif env_name == 'production':
    from .production import *
else:
    from .local import *
