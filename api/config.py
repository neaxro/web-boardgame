import os

class Config:
    def __init__(self):
        # App config
        self.APP_HOST  = os.environ.get("APP_HOST", "0.0.0.0")
        self.APP_PORT  = os.environ.get("APP_PORT", "5000")
        self.APP_DEBUG  = os.environ.get("APP_DEBUG", "True") == "True"

        # Database config
        self.DB_HOST = os.environ.get("DB_HOST", "localhost")
        self.DB_USER = os.environ.get("DB_USER", "root")
        self.DB_PASSWORD = os.environ.get("DB_PASSWORD", "pass")
        self.DB_DATABASE = os.environ.get("DB_DATABASE", "boardgame_web")

        # Monitoring config
        self.METRICS_PREFIX = os.environ.get("METRICS_PREFIX", "boardgame_web")
