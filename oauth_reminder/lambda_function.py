from typing import Any, Mapping
from slack_bot_client.slack_client import SlackClient, SlackChannel
import boto3
from boto3.dynamodb.conditions import Key
import oauth_reminder.config as config
from datetime import datetime, timedelta, timezone
import logging
from common.ssm import SSM
import urllib.parse

logging.basicConfig(
    level=config.get_logging_level(), format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)


def send_alert(session_id: str, days_to_expiration: int) -> None:
    tda_auth_url = config.get_tda_auth_base_url()
    query_parmas = {
        "redirect_uri": SSM().get_parameter("/tda/redirect_uri"),
        "client_id": SSM().get_parameter("/tda/client_id"),
        "response_type": "code",
    }
    oauth_url = f"{tda_auth_url}?{urllib.parse.urlencode(query_parmas)}"
    message = f"WARNING: OAuth session [{session_id}] expires in {days_to_expiration} days.\n Visit {oauth_url} to re-authenticate"
    logger.info(message)
    SlackClient().send(
        SlackChannel.ALERTS,
        message,
    )


def lambda_handler(event: Mapping[str, Any], context: Mapping[str, Any]) -> str:
    ddb_table = boto3.resource("dynamodb").Table(config.get_ddb_table_name())

    session_id = config.get_session_id()
    items = ddb_table.query(KeyConditionExpression=Key("id").eq(session_id))["Items"]

    refresh_token_expiration = datetime.fromisoformat(
        items[0]["refresh_token_expiration"]
    )
    now = datetime.now(timezone.utc)
    if refresh_token_expiration < now + timedelta(days=config.get_warning_days_ahead()):
        days_to_expiration = (refresh_token_expiration - now).days
        send_alert(session_id, days_to_expiration)

    return "OK"
