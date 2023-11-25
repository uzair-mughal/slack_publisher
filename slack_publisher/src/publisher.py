import logging
from slack_sdk.webhook import WebhookClient

logger = logging.getLogger(__name__)


class SlackPublisher:
    def __init__(self, webhook_url: str):
        self.webhook_client = WebhookClient(url=webhook_url)

    def publish(self, message: str):
        try:
            response = self.webhook_client.send(text=message)
            if response.status_code != 200:
                raise Exception(f"Slack API returned an error: {response.status_code} - {response.body}")
        except Exception as e:
            logger.error(e, exc_info=True)