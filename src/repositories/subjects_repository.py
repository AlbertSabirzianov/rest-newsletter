from typing import Optional

from ..schemas.schema import Subject
from .base_reposytory import BaseRepository


class SubjectRepository(BaseRepository):

    DATA_PATH: str = "src/data/subjects.json"
    SCHEMA = Subject

    def get_subject_by_name(self, name: str) -> Optional[Subject]:
        try:
            return list(
                filter(
                    lambda x: x.name == name,
                    self.objects
                )
            )[0]
        except IndexError:
            return None


subject_repository = SubjectRepository()

