from typing import NewType, Union

Token = NewType('Token', str)
AccessToken = NewType('AccessToken', Token)
RefreshToken = NewType('RefreshToken', Token)
