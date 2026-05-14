# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PhoebeError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import ref, data, product
    from .resources.ref.ref import RefResource, AsyncRefResource
    from .resources.data.data import DataResource, AsyncDataResource
    from .resources.product.product import ProductResource, AsyncProductResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Phoebe", "AsyncPhoebe", "Client", "AsyncClient"]


class Phoebe(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Phoebe client instance.

        This automatically infers the `api_key` argument from the `EBIRD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("EBIRD_API_KEY")
        if api_key is None:
            raise PhoebeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the EBIRD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PHOEBE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.ebird.org/v2"

        custom_headers_env = os.environ.get("PHOEBE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def data(self) -> DataResource:
        from .resources.data import DataResource

        return DataResource(self)

    @cached_property
    def product(self) -> ProductResource:
        from .resources.product import ProductResource

        return ProductResource(self)

    @cached_property
    def ref(self) -> RefResource:
        from .resources.ref import RefResource

        return RefResource(self)

    @cached_property
    def with_raw_response(self) -> PhoebeWithRawResponse:
        return PhoebeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoebeWithStreamedResponse:
        return PhoebeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-eBirdApiToken": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPhoebe(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPhoebe client instance.

        This automatically infers the `api_key` argument from the `EBIRD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("EBIRD_API_KEY")
        if api_key is None:
            raise PhoebeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the EBIRD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PHOEBE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.ebird.org/v2"

        custom_headers_env = os.environ.get("PHOEBE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def data(self) -> AsyncDataResource:
        from .resources.data import AsyncDataResource

        return AsyncDataResource(self)

    @cached_property
    def product(self) -> AsyncProductResource:
        from .resources.product import AsyncProductResource

        return AsyncProductResource(self)

    @cached_property
    def ref(self) -> AsyncRefResource:
        from .resources.ref import AsyncRefResource

        return AsyncRefResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPhoebeWithRawResponse:
        return AsyncPhoebeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoebeWithStreamedResponse:
        return AsyncPhoebeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-eBirdApiToken": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PhoebeWithRawResponse:
    _client: Phoebe

    def __init__(self, client: Phoebe) -> None:
        self._client = client

    @cached_property
    def data(self) -> data.DataResourceWithRawResponse:
        from .resources.data import DataResourceWithRawResponse

        return DataResourceWithRawResponse(self._client.data)

    @cached_property
    def product(self) -> product.ProductResourceWithRawResponse:
        from .resources.product import ProductResourceWithRawResponse

        return ProductResourceWithRawResponse(self._client.product)

    @cached_property
    def ref(self) -> ref.RefResourceWithRawResponse:
        from .resources.ref import RefResourceWithRawResponse

        return RefResourceWithRawResponse(self._client.ref)


class AsyncPhoebeWithRawResponse:
    _client: AsyncPhoebe

    def __init__(self, client: AsyncPhoebe) -> None:
        self._client = client

    @cached_property
    def data(self) -> data.AsyncDataResourceWithRawResponse:
        from .resources.data import AsyncDataResourceWithRawResponse

        return AsyncDataResourceWithRawResponse(self._client.data)

    @cached_property
    def product(self) -> product.AsyncProductResourceWithRawResponse:
        from .resources.product import AsyncProductResourceWithRawResponse

        return AsyncProductResourceWithRawResponse(self._client.product)

    @cached_property
    def ref(self) -> ref.AsyncRefResourceWithRawResponse:
        from .resources.ref import AsyncRefResourceWithRawResponse

        return AsyncRefResourceWithRawResponse(self._client.ref)


class PhoebeWithStreamedResponse:
    _client: Phoebe

    def __init__(self, client: Phoebe) -> None:
        self._client = client

    @cached_property
    def data(self) -> data.DataResourceWithStreamingResponse:
        from .resources.data import DataResourceWithStreamingResponse

        return DataResourceWithStreamingResponse(self._client.data)

    @cached_property
    def product(self) -> product.ProductResourceWithStreamingResponse:
        from .resources.product import ProductResourceWithStreamingResponse

        return ProductResourceWithStreamingResponse(self._client.product)

    @cached_property
    def ref(self) -> ref.RefResourceWithStreamingResponse:
        from .resources.ref import RefResourceWithStreamingResponse

        return RefResourceWithStreamingResponse(self._client.ref)


class AsyncPhoebeWithStreamedResponse:
    _client: AsyncPhoebe

    def __init__(self, client: AsyncPhoebe) -> None:
        self._client = client

    @cached_property
    def data(self) -> data.AsyncDataResourceWithStreamingResponse:
        from .resources.data import AsyncDataResourceWithStreamingResponse

        return AsyncDataResourceWithStreamingResponse(self._client.data)

    @cached_property
    def product(self) -> product.AsyncProductResourceWithStreamingResponse:
        from .resources.product import AsyncProductResourceWithStreamingResponse

        return AsyncProductResourceWithStreamingResponse(self._client.product)

    @cached_property
    def ref(self) -> ref.AsyncRefResourceWithStreamingResponse:
        from .resources.ref import AsyncRefResourceWithStreamingResponse

        return AsyncRefResourceWithStreamingResponse(self._client.ref)


Client = Phoebe

AsyncClient = AsyncPhoebe
