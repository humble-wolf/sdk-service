from typing import Dict, Any, Optional


class Storage:

    def __init__(self) -> None:
        self._storage_data: Dict[str, Dict[str, Any]] = {}

    def save(self, key: str, stored_item: Dict[str, Any]) -> None:
        self._storage_data[key] = stored_item

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        return self._storage_data.get(key)

    def delete(self, key: str) -> None:
        self._storage_data.pop(key, None)

    def get_all(self) -> Dict[str, Dict[str, Any]]:
        return self._storage_data
