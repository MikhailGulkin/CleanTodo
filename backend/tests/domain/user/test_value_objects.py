# import pytest
#
# from src.domain.user.exceptions import (
#     IncorrectUserEmail,
#     IncorrectUserName,
#     IncorrectPassword
# )
# from src.domain.user.value_objects import (
#     UserEmail,
#     UserName,
#     UserPassword
# )
#
#
# @pytest.mark.domain
# def test_email_validation(valid_email: str, invalid_email: str) -> None:
#     email = UserEmail(value=valid_email)
#     assert email.value == valid_email
#
#     with pytest.raises(IncorrectUserEmail):
#         UserEmail(value=invalid_email)
#
#
# @pytest.mark.domain
# def test_username_validation(valid_username: str, invalid_username: str) -> None:
#     username = UserName(value=valid_username)
#     assert username.value == valid_username
#
#     with pytest.raises(IncorrectUserName):
#         UserName(value=invalid_username)
#
#
# @pytest.mark.domain
# def test_password_validation(valid_password: str, invalid_passwords: list[str]) -> None:
#     password = UserPassword(value=valid_password)
#     assert password.value == valid_password
#
#     with pytest.raises(IncorrectPassword):
#         for password in invalid_passwords:
#             UserPassword(value=password)
