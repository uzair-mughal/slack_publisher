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

    def on_failure_callback(self, context: dict):
        try:
            task_id = context["task_instance"].task_id
            dag_id = context["task_instance"].dag_id
            response = self.webhook_client.send(text=f"Task {task_id} in DAG {dag_id} failed")
            if response.status_code != 200:
                raise Exception(f"Slack API returned an error: {response.status_code} - {response.body}")
        except Exception as e:
            logger.error(e, exc_info=True)
