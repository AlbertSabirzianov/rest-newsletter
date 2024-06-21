from typing import List

from .base_reposytory import BaseRepository
from ..schemas.schema import Subscription


class SubscriptionRepository(BaseRepository):

    DATA_PATH = "data/subscriptions.json"
    SCHEMA = Subscription

    def get_subscriptions_by_subject_name(self, name: str) -> List[Subscription]:
        return list(
            filter(
                lambda x: x.subject_name == name,
                self.objects
            )
        )

    def delete_subscription(self, subscription: Subscription) -> None:
        objects = [
            obj for obj in self.objects if obj.url != subscription.url or obj.subject_name != subscription.subject_name
        ]
        self.dump_data(objects)

    def delete_subscriptions_by_subject_name(self, subject_name: str) -> None:
        objects = [
            obj for obj in self.objects if obj.subject_name != subject_name
        ]
        self.dump_data(objects)


subscription_repository = SubscriptionRepository()

