from datetime import datetime
from typing import Dict, Any

from app.models.schemas.user import UserResponse


class UserService:
    def __init__(self):
        pass

    def _valid_email(self, email: str) -> bool:
        return True

    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        if not self._valid_email(email):
            raise ValueError("Invalid email format")
        # save 추가
        return UserResponse(
                id=0,
                name=name,
                email=email,
                created_at=str(datetime.now())
    )
