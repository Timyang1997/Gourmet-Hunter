from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AccountBase(BaseModel):
    cid: str
    name: str
    roles: List[str] = []
    updated_at: Optional[datetime] = None

class AccountCreate(AccountBase):
    pass  # 用於建立新帳戶時的輸入

class AccountResponse(AccountBase):
    id: str  # MongoDB 會使用 `_id`，但我們轉換為 `id`

    class Config:
        orm_mode = True
        from_attributes = True