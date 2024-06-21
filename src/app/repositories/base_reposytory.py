import json
from typing import List

from pydantic import BaseModel, parse_obj_as


class BaseRepository:

    DATA_PATH: str
    SCHEMA: BaseModel

    @property
    def objects(self) -> List[BaseModel]:
        try:
            with open(self.DATA_PATH, "r") as file:
                objects: List[BaseModel] = parse_obj_as(List[self.SCHEMA], json.loads(file.read()))
            return objects
        except json.decoder.JSONDecodeError:
            return []

    def get_all_objects(self) -> List[BaseModel]:
        return self.objects

    def dump_data(self, objects: List[BaseModel]):
        with open(self.DATA_PATH, "w") as file:
            json.dump(
                [sub.model_dump() for sub in objects],
                file
            )

    def set_object(self, obj: BaseModel) -> None:
        with open(self.DATA_PATH, "w") as file:
            json.dump(
                [sub.model_dump() for sub in self.objects] + [obj.model_dump()],
                file
            )


