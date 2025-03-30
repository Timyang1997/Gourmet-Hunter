from bson import ObjectId
from datetime import datetime
from src.rbac_applet.schema import AccountCreate, AccountResponse

class Account:
    collection_name = "rbac_accounts"

    @staticmethod
    async def create(db, account: AccountCreate):
        """新增帳戶"""
        account_data = account.dict()
        account_data["updated_at"] = datetime.now()
        result = await db[Account.collection_name].insert_one(account_data)
        return str(result.inserted_id)

    @staticmethod
    async def get_by_id(db, account_id: str):
        """透過 ID 取得帳戶"""
        account = await db[Account.collection_name].find_one({"_id": ObjectId(account_id)})
        if account:
            account["id"] = str(account["_id"])  # 轉換 ObjectId
            return AccountResponse(**account)
        return None

    @staticmethod
    async def get_by_cid(db, cid: str):
        """透過 CID 取得帳戶"""
        accounts = await db[Account.collection_name].find({"cid": cid}).to_list(100)
        for account in accounts:
            account["id"] = str(account["_id"])
        return [AccountResponse(**account) for account in accounts]

    @staticmethod
    async def update(db, account_id: str, update_data: dict):
        """更新帳戶資訊"""
        update_data["updated_at"] = datetime.now()
        result = await db[Account.collection_name].update_one(
            {"_id": ObjectId(account_id)}, {"$set": update_data}
        )
        return result.modified_count > 0

    @staticmethod
    async def delete(db, account_id: str):
        """刪除帳戶"""
        result = await db[Account.collection_name].delete_one({"_id": ObjectId(account_id)})
        return result.deleted_count > 0
