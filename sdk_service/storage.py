from typing import Dict, Optional


class Storage:

    def __init__(self) -> None:
        self._storage_data: Dict[str, dict] = {}

    def save(self, key: str, stored_item: dict) -> None:
        self._storage_data[key] = stored_item

    def get(self, key: str) -> Optional[dict]:
        return self._storage_data.get(key)

    def delete(self, key: str) -> None:
        self._storage_data.pop(key, None)

    def get_all(self) -> Dict[str, dict]:
        return self._storage_data
