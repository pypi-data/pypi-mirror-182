from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from nopy.types import Props


class NopyError(Exception):
    """Base exception from which all Nopy errors inherit.

    This exception can be caught to catch all possible errors
    that may take place via the package.

    Attributes:
        message: The error message.
    """

    def __init__(self, message: str):

        self.message: str = message
        super().__init__(message)


class TokenNotFoundError(NopyError):
    """Error raised when no Notion token was found.

    Attributes:
        message (str): The error message.
    """

    pass


class HTTPError(NopyError):
    """Encompasses all errors that took place during the
    request to the Notion API.

    Attributes:
        message (str): The error message.
        status_code: The status code of the response.
        headers: The headers returned by the response.
        body: The body of the response as a string.
    """

    def __init__(self, response: httpx.Response, message: str = ""):

        if not message:
            message = f"Request to the Notion API failed with status code: {response.status_code}"

        super().__init__(message)
        self.status_code: int = response.status_code
        self.message: str = response.text
        self.body: httpx.Headers = response.headers


class APIResponseError(HTTPError):
    """Encompasses any error that is returned by the Notion API.

    Attributes:
        code: The error code returned by Notion.
        message (str): The error message returned by Notion.
    """

    def __init__(self, response: httpx.Response, code: str, message: str):

        error_message = f"{code.upper()} - {message}"
        super().__init__(response, error_message)

        self.code: str = code
        self.message: str = message


class UnuspportedError(NopyError):
    """An error raised when the user tries to do something that's not
    supported by the library or via the Notion API.

    Attributes:
        message (str): The error message.
    """

    pass


class UnsupportedByLibraryError(UnuspportedError):
    """An error raised when the user tries to do something that's not
    supported by the library currently.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str):

        message += " is currently unsupported by the library"
        super().__init__(message)


class UnsupportedByNotion(UnuspportedError):
    """An error raised when the user tries to do something that's not
    supported by the Notion API currently.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str):
        message += " is currently unsupported by the Notion API"
        super().__init__(message)


class NoClientFoundError(NopyError):
    """An error raised when the user tries to make an API call
    via a Notion Object that doesn't have a client.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str):

        message += " has no client set"
        super().__init__(message)


class PropertyExistsError(NopyError):
    """Raised when the property already exists."""

    pass


class PropertyNotFoundError(NopyError):
    """Raised when the property is not found."""

    pass


class SerializationError(NopyError):
    """Raised when there's some error during serialization."""

    def __init__(self, message: str, prop: "Props"):

        self.prop: "Props" = prop
        message += f" for '{prop.type.value}' properties"
        super().__init__(message)
