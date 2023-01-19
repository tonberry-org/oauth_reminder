from typing import Any, Mapping
from datetime import date
from slack_bot_client.slack_client import SlackClient, SlackChannel


def lambda_handler(event: Mapping[str, Any], context: Mapping[str, Any]) -> str:
    SlackClient().send(SlackChannel.MONITORING, "OK")
    return "OK"
