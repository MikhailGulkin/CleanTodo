import re

EMAIL_REGEX = re.compile(r'([A-Za-z0-9]+)[.-_]?([A-Za-z0-9]+)@([A-Za-z0-9-]+)(\.[A-Z|a-z]{2,})+')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d].+$')
