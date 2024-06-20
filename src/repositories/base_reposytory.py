import json
from typing import List

from pydantic import BaseModel, parse_obj_as


class BaseRepository:

    DATA_PATH: str
    SCHEMA: BaseModel

    def __init__(self):
        with open(self.DATA_PATH, "r") as file:
            self.objects: List[BaseModel] = parse_obj_as(List[self.SCHEMA], json.loads(file.read()))

    def get_all_objects(self) -> List[BaseModel]:
        return self.objects

    def set_object(self, obj: BaseModel) -> None:
        self.objects.append(obj)
        with open(self.DATA_PATH, "w") as file:
            json.dump(
                [sub.model_dump() for sub in self.objects],
                file
            )


