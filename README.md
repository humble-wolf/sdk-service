# Hunter.io SDK

A simple Python SDK for interacting with the [Hunter.io API](https://hunter.io/api-documentation).
It supports email verification with in-memory caching.

## Installation

```sh
git clone https://github.com/humble-wolf/sdk-service.git
cd sdk-service
pip install -r requirements.txt
```

## Usage

```python
from sdk_service.service import HunterService

service = HunterService()
print(service.verify_email("test@example.com"))
```

## Running Tests

```sh
pytest
```

## Code Quality

```sh
flake8 .   # Linting
mypy sdk_service/  # Type checking
```
