# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .recent.recent import (
    RecentResource,
    AsyncRecentResource,
    RecentResourceWithRawResponse,
    AsyncRecentResourceWithRawResponse,
    RecentResourceWithStreamingResponse,
    AsyncRecentResourceWithStreamingResponse,
)

__all__ = ["GeoResource", "AsyncGeoResource"]


class GeoResource(SyncAPIResource):
    @cached_property
    def recent(self) -> RecentResource:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return RecentResource(self._client)

    @cached_property
    def with_raw_response(self) -> GeoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return GeoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return GeoResourceWithStreamingResponse(self)


class AsyncGeoResource(AsyncAPIResource):
    @cached_property
    def recent(self) -> AsyncRecentResource:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncRecentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGeoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGeoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return AsyncGeoResourceWithStreamingResponse(self)


class GeoResourceWithRawResponse:
    def __init__(self, geo: GeoResource) -> None:
        self._geo = geo

    @cached_property
    def recent(self) -> RecentResourceWithRawResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return RecentResourceWithRawResponse(self._geo.recent)


class AsyncGeoResourceWithRawResponse:
    def __init__(self, geo: AsyncGeoResource) -> None:
        self._geo = geo

    @cached_property
    def recent(self) -> AsyncRecentResourceWithRawResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncRecentResourceWithRawResponse(self._geo.recent)


class GeoResourceWithStreamingResponse:
    def __init__(self, geo: GeoResource) -> None:
        self._geo = geo

    @cached_property
    def recent(self) -> RecentResourceWithStreamingResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return RecentResourceWithStreamingResponse(self._geo.recent)


class AsyncGeoResourceWithStreamingResponse:
    def __init__(self, geo: AsyncGeoResource) -> None:
        self._geo = geo

    @cached_property
    def recent(self) -> AsyncRecentResourceWithStreamingResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncRecentResourceWithStreamingResponse(self._geo.recent)
