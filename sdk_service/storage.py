from typing import Dict, Optional

class Storage:

    def __init__(self) -> None:
        self._data: Dict[str, dict] = {}

    def save(self, key: str, value: dict) -> None:
        self._data[key] = value

    def get(self, key: str) -> Optional[dict]:
        return self._data.get(key)

    def delete(self, key: str) -> None:
        if key in self._data:
            del self._data[key]

    def get_all(self) -> Dict[str, dict]:
        return self._data
