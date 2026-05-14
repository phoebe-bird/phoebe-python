# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .geo import (
    GeoResource,
    AsyncGeoResource,
    GeoResourceWithRawResponse,
    AsyncGeoResourceWithRawResponse,
    GeoResourceWithStreamingResponse,
    AsyncGeoResourceWithStreamingResponse,
)
from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.ref import hotspot_list_params
from ...._base_client import make_request_options
from ....types.ref.hotspot_list_response import HotspotListResponse

__all__ = ["HotspotResource", "AsyncHotspotResource"]


class HotspotResource(SyncAPIResource):
    """
    With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
    """

    @cached_property
    def geo(self) -> GeoResource:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return GeoResource(self._client)

    @cached_property
    def info(self) -> InfoResource:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return InfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> HotspotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return HotspotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HotspotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return HotspotResourceWithStreamingResponse(self)

    def list(
        self,
        region_code: str,
        *,
        back: int | Omit = omit,
        fmt: Literal["csv", "json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HotspotListResponse:
        """
        Hotspots in a region

        Args:
          back: The number of days back to fetch hotspots.

          fmt: Fetch the records in CSV or JSON format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not region_code:
            raise ValueError(f"Expected a non-empty value for `region_code` but received {region_code!r}")
        return self._get(
            path_template("/ref/hotspot/{region_code}", region_code=region_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "back": back,
                        "fmt": fmt,
                    },
                    hotspot_list_params.HotspotListParams,
                ),
            ),
            cast_to=HotspotListResponse,
        )


class AsyncHotspotResource(AsyncAPIResource):
    """
    With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
    """

    @cached_property
    def geo(self) -> AsyncGeoResource:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return AsyncGeoResource(self._client)

    @cached_property
    def info(self) -> AsyncInfoResource:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return AsyncInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHotspotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHotspotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHotspotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return AsyncHotspotResourceWithStreamingResponse(self)

    async def list(
        self,
        region_code: str,
        *,
        back: int | Omit = omit,
        fmt: Literal["csv", "json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HotspotListResponse:
        """
        Hotspots in a region

        Args:
          back: The number of days back to fetch hotspots.

          fmt: Fetch the records in CSV or JSON format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not region_code:
            raise ValueError(f"Expected a non-empty value for `region_code` but received {region_code!r}")
        return await self._get(
            path_template("/ref/hotspot/{region_code}", region_code=region_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "back": back,
                        "fmt": fmt,
                    },
                    hotspot_list_params.HotspotListParams,
                ),
            ),
            cast_to=HotspotListResponse,
        )


class HotspotResourceWithRawResponse:
    def __init__(self, hotspot: HotspotResource) -> None:
        self._hotspot = hotspot

        self.list = to_raw_response_wrapper(
            hotspot.list,
        )

    @cached_property
    def geo(self) -> GeoResourceWithRawResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return GeoResourceWithRawResponse(self._hotspot.geo)

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return InfoResourceWithRawResponse(self._hotspot.info)


class AsyncHotspotResourceWithRawResponse:
    def __init__(self, hotspot: AsyncHotspotResource) -> None:
        self._hotspot = hotspot

        self.list = async_to_raw_response_wrapper(
            hotspot.list,
        )

    @cached_property
    def geo(self) -> AsyncGeoResourceWithRawResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return AsyncGeoResourceWithRawResponse(self._hotspot.geo)

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return AsyncInfoResourceWithRawResponse(self._hotspot.info)


class HotspotResourceWithStreamingResponse:
    def __init__(self, hotspot: HotspotResource) -> None:
        self._hotspot = hotspot

        self.list = to_streamed_response_wrapper(
            hotspot.list,
        )

    @cached_property
    def geo(self) -> GeoResourceWithStreamingResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return GeoResourceWithStreamingResponse(self._hotspot.geo)

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return InfoResourceWithStreamingResponse(self._hotspot.info)


class AsyncHotspotResourceWithStreamingResponse:
    def __init__(self, hotspot: AsyncHotspotResource) -> None:
        self._hotspot = hotspot

        self.list = async_to_streamed_response_wrapper(
            hotspot.list,
        )

    @cached_property
    def geo(self) -> AsyncGeoResourceWithStreamingResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return AsyncGeoResourceWithStreamingResponse(self._hotspot.geo)

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        """
        With the ref/hotspot end-points you can find the hotspots for a given country or region or nearby hotspots
        """
        return AsyncInfoResourceWithStreamingResponse(self._hotspot.info)
