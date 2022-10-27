API_TOKEN = "BAD TOKEN"

# for locally rewrite settings add it to settings_local.py
try:
    from settings_local import *
except ModuleNotFoundError as err:
    pass
