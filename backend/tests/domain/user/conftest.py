import pytest


@pytest.fixture
def valid_email() -> str:
    return 'example@mail.com'


@pytest.fixture
def invalid_email() -> str:
    return 'example....@mail.com'


@pytest.fixture
def valid_username() -> str:
    return 'Bol4onok'


@pytest.fixture
def invalid_username() -> str:
    return ''


@pytest.fixture
def valid_password() -> str:
    return 'Ab1' + 'b' * 8


@pytest.fixture
def invalid_passwords() -> list[str]:
    return [
        'Ab1',
        'A' * 8,
        'b' * 8,
        '1' * 8
    ]
