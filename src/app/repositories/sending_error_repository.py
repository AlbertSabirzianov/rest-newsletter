from .base_reposytory import BaseRepository
from ..schemas.schema import SendingError


class SendingErrorRepository(BaseRepository):
    DATA_PATH = "data/sending_errors.json"
    SCHEMA = SendingError


sending_error_repository = SendingErrorRepository()
