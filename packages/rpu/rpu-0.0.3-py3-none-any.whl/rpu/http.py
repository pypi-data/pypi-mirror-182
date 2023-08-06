from typing import Literal, Optional
from urllib.parse import urlencode

from .consts import MISSING

__all__ = ["QueryParams", "Headers", "Route"]


class QueryParams:
    __slots__ = ["_internal"]

    def __init__(self, *, raw: dict[str, str] = MISSING):
        """Creates a QueryParams instance. Used for storing url params

        Parameters
        ----------
        raw: dict[`str`, `str`]
            headers to be used when creating the object

        Examples
        ----------
        >>> params = QueryParams(raw={'5' : '2'})
        >>> params['foo'] = 'bar'
        >>> params.unpack()
        ... 5=2&foo=bar
        """

        self._internal = raw or {}

    def __getitem__(self, key: str) -> Optional[str]:
        return self._internal.get(key)

    def __setitem__(self, key: str, value: str) -> None:
        self._internal[str(key)] = str(value)

    def unpack(self) -> str:
        """Unpacks the parameters into a form that can be used in a url

        Returns
        ----------
        str
        """

        return urlencode(self._internal)


class Headers:
    __slots__ = ["_internal"]

    def __init__(self, *, raw: dict[str, str] = MISSING):
        """Creates a Headers instance. Used for storing http headers.

        Parameters
        ----------
        raw: dict[`str`, `str`]
            headers to be used when creating the object

        Examples
        ----------
        >>> header = Headers(raw={'5' : '2'})
        >>> header['foo'] = 'bar'
        >>> header.unpack()
        ... {'5' : '2', 'foo' : 'bar'}
        """

        self._internal = raw or {}

    def __getitem__(self, key: str) -> Optional[str]:
        return self._internal.get(key)

    def __setitem__(self, key: str, value: str) -> None:
        self._internal[str(key)] = str(value)

        self._internal[key] = value

    def unpack(self) -> dict:
        """Unpacks the parameters into a dict

        Returns
        ----------
        dict[str, str]
        """

        return self._internal


class Route:
    __slots__ = ["method", "endpoint", "headers", "query_params"]

    def __init__(
        self,
        *,
        method: Literal["POST", "GET"],
        endpoint: str,
        headers: Optional[Headers] = None,
        query_params: Optional[QueryParams] = None,
    ):
        """Creates a route instance

        Parameters
        ----------
        method: typing.Literal["POST", "GET"]
            The method for the request
        endpoint: `str`
            the endpoint for the request
        headers: Optional[`Headers`]
            The headers
        query_params: Optional[`QueryParams`]
            the query params

        Attributes
        ----------
        method: typing.Literal["POST", "GET"]
            The method for the request
        endpoint: `str`
            the endpoint for the request
        headers: `Headers`
            The headers
        query_params: `QueryParams`
            the query params
        """

        self.method = method
        self.endpoint = endpoint
        self.headers = headers or Headers()
        self.query_params = query_params or QueryParams()
