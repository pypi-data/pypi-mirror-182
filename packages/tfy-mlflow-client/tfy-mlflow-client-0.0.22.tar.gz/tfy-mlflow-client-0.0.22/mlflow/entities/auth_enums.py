import enum

from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST

ENTITY_ID_ALL = "*"


@enum.unique
class SubjectType(enum.Enum):
    USER = "USER"

    @classmethod
    def _missing_(cls, value):
        raise MlflowException(f"Unknown Subject Type: {value}", error_code=BAD_REQUEST)


@enum.unique
class EntityType(enum.Enum):
    EXPERIMENT = "EXPERIMENT"

    @classmethod
    def _missing_(cls, value):
        raise MlflowException(f"Unknown Entity Type: {value}", error_code=BAD_REQUEST)


@enum.unique
class Role(enum.IntEnum):
    READ = 1
    WRITE = 3
    ADMIN = 7


@enum.unique
class PrivacyType(enum.Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

    @classmethod
    def _missing_(cls, value):
        raise MlflowException(f"Unknown Privacy Type: {value}", error_code=BAD_REQUEST)
