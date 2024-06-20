from typing import List

from .base_reposytory import BaseRepository
from ..schemas.schema import Subscription


class SubscriptionRepository(BaseRepository):

    DATA_PATH = "src/data/subscriptions.json"
    SCHEMA = Subscription

    def get_subscriptions_by_subject_name(self, name: str) -> List[Subscription]:
        return list(
            filter(
                lambda x: x.subject_name == name,
                self.objects
            )
        )


subscription_repository = SubscriptionRepository()

