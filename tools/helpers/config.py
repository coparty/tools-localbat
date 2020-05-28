import types
from os import path

def from_backup() -> list:
    config_data = {}
    config_path = path.abspath(path.join(path.dirname(__file__), "../../configs/backup.py"))

    module = types.ModuleType("config")
    module.__file__ = config_path

    try:
        with open(config_path, "rb") as f:
            exec(compile(f.read(), config_path, "exec"), module.__dict__)
    except OSError as e:
        e.strerror = "Unable to load the configuration file"
        raise

    # Convert `config.attr` to `config[attr]`
    for key in dir(module):
        if key.isupper():
            config_data[key] = getattr(module, key)

    return [
        config_data["SSH"],
        config_data["BACKUP"],
        config_data["DOWNLOAD"]
    ]
