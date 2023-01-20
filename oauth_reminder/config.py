import os
import logging
from typing import Union


class ConfigException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_or_throw(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        raise ConfigException(f"Missing config for [{key}]")
    return value


def get_with_default(key: str, default: str) -> str:
    result = None
    if key in os.environ:
        result = os.environ.get(key)
    if result is None:
        result = default
    return result


def get_logging_level() -> Union[str, int]:
    return os.environ.get("LOG_LEVEL") or logging.INFO


def get_ddb_table_name() -> str:
    return get_with_default("DDB_SESSIONS_TABLE_NAME", "tda_sessions")


def get_warning_days_ahead() -> int:
    return int(get_with_default("WARNING_DAYS_AHEAD", "7"))


def get_session_id() -> str:
    return get_with_default("SESSION_ID", "general")


def get_tda_auth_base_url() -> str:
    return get_with_default("TDA_AUTH_URL", "https://auth.tdameritrade.com/oauth")
