from typing import Optional

from .base_reposytory import BaseRepository
from ..schemas.schema import Subject


class SubjectRepository(BaseRepository):

    DATA_PATH: str = "data/subjects.json"
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

    def delete_subject_by_name(self, name: str) -> None:
        self.objects = [obj for obj in self.objects if obj.name != name]
        self.dump_data()


subject_repository = SubjectRepository()

