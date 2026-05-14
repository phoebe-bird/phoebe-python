# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)
from .list import (
    ListResource,
    AsyncListResource,
    ListResourceWithRawResponse,
    AsyncListResourceWithRawResponse,
    ListResourceWithStreamingResponse,
    AsyncListResourceWithStreamingResponse,
)
from .adjacent import (
    AdjacentResource,
    AsyncAdjacentResource,
    AdjacentResourceWithRawResponse,
    AsyncAdjacentResourceWithRawResponse,
    AdjacentResourceWithStreamingResponse,
    AsyncAdjacentResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RegionResource", "AsyncRegionResource"]


class RegionResource(SyncAPIResource):
    @cached_property
    def adjacent(self) -> AdjacentResource:
        """With the ref/geo end-point you can find a country's or region's neighbours."""
        return AdjacentResource(self._client)

    @cached_property
    def info(self) -> InfoResource:
        """The ref/region end-points return information on regions."""
        return InfoResource(self._client)

    @cached_property
    def list(self) -> ListResource:
        """The ref/region end-points return information on regions."""
        return ListResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return RegionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return RegionResourceWithStreamingResponse(self)


class AsyncRegionResource(AsyncAPIResource):
    @cached_property
    def adjacent(self) -> AsyncAdjacentResource:
        """With the ref/geo end-point you can find a country's or region's neighbours."""
        return AsyncAdjacentResource(self._client)

    @cached_property
    def info(self) -> AsyncInfoResource:
        """The ref/region end-points return information on regions."""
        return AsyncInfoResource(self._client)

    @cached_property
    def list(self) -> AsyncListResource:
        """The ref/region end-points return information on regions."""
        return AsyncListResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return AsyncRegionResourceWithStreamingResponse(self)


class RegionResourceWithRawResponse:
    def __init__(self, region: RegionResource) -> None:
        self._region = region

    @cached_property
    def adjacent(self) -> AdjacentResourceWithRawResponse:
        """With the ref/geo end-point you can find a country's or region's neighbours."""
        return AdjacentResourceWithRawResponse(self._region.adjacent)

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        """The ref/region end-points return information on regions."""
        return InfoResourceWithRawResponse(self._region.info)

    @cached_property
    def list(self) -> ListResourceWithRawResponse:
        """The ref/region end-points return information on regions."""
        return ListResourceWithRawResponse(self._region.list)


class AsyncRegionResourceWithRawResponse:
    def __init__(self, region: AsyncRegionResource) -> None:
        self._region = region

    @cached_property
    def adjacent(self) -> AsyncAdjacentResourceWithRawResponse:
        """With the ref/geo end-point you can find a country's or region's neighbours."""
        return AsyncAdjacentResourceWithRawResponse(self._region.adjacent)

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        """The ref/region end-points return information on regions."""
        return AsyncInfoResourceWithRawResponse(self._region.info)

    @cached_property
    def list(self) -> AsyncListResourceWithRawResponse:
        """The ref/region end-points return information on regions."""
        return AsyncListResourceWithRawResponse(self._region.list)


class RegionResourceWithStreamingResponse:
    def __init__(self, region: RegionResource) -> None:
        self._region = region

    @cached_property
    def adjacent(self) -> AdjacentResourceWithStreamingResponse:
        """With the ref/geo end-point you can find a country's or region's neighbours."""
        return AdjacentResourceWithStreamingResponse(self._region.adjacent)

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        """The ref/region end-points return information on regions."""
        return InfoResourceWithStreamingResponse(self._region.info)

    @cached_property
    def list(self) -> ListResourceWithStreamingResponse:
        """The ref/region end-points return information on regions."""
        return ListResourceWithStreamingResponse(self._region.list)


class AsyncRegionResourceWithStreamingResponse:
    def __init__(self, region: AsyncRegionResource) -> None:
        self._region = region

    @cached_property
    def adjacent(self) -> AsyncAdjacentResourceWithStreamingResponse:
        """With the ref/geo end-point you can find a country's or region's neighbours."""
        return AsyncAdjacentResourceWithStreamingResponse(self._region.adjacent)

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        """The ref/region end-points return information on regions."""
        return AsyncInfoResourceWithStreamingResponse(self._region.info)

    @cached_property
    def list(self) -> AsyncListResourceWithStreamingResponse:
        """The ref/region end-points return information on regions."""
        return AsyncListResourceWithStreamingResponse(self._region.list)
