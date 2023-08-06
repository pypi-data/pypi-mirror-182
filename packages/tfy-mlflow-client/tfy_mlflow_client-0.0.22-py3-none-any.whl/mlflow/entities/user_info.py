from typing import List

from pydantic import BaseModel, Field, constr


class UserInfo(BaseModel):
    user_id: constr(strict=True, min_length=1)
    tenant_name: constr(strict=True, min_length=1)
    tenant_id: constr(strict=True, min_length=1)
    roles: List[str] = Field(default_factory=list)  # these are roles from auth server
