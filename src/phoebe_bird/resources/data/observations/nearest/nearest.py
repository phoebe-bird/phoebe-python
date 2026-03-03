# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .geo_species import (
    GeoSpeciesResource,
    AsyncGeoSpeciesResource,
    GeoSpeciesResourceWithRawResponse,
    AsyncGeoSpeciesResourceWithRawResponse,
    GeoSpeciesResourceWithStreamingResponse,
    AsyncGeoSpeciesResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["NearestResource", "AsyncNearestResource"]


class NearestResource(SyncAPIResource):
    @cached_property
    def geo_species(self) -> GeoSpeciesResource:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return GeoSpeciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> NearestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return NearestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NearestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return NearestResourceWithStreamingResponse(self)


class AsyncNearestResource(AsyncAPIResource):
    @cached_property
    def geo_species(self) -> AsyncGeoSpeciesResource:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncGeoSpeciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNearestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNearestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNearestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return AsyncNearestResourceWithStreamingResponse(self)


class NearestResourceWithRawResponse:
    def __init__(self, nearest: NearestResource) -> None:
        self._nearest = nearest

    @cached_property
    def geo_species(self) -> GeoSpeciesResourceWithRawResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return GeoSpeciesResourceWithRawResponse(self._nearest.geo_species)


class AsyncNearestResourceWithRawResponse:
    def __init__(self, nearest: AsyncNearestResource) -> None:
        self._nearest = nearest

    @cached_property
    def geo_species(self) -> AsyncGeoSpeciesResourceWithRawResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncGeoSpeciesResourceWithRawResponse(self._nearest.geo_species)


class NearestResourceWithStreamingResponse:
    def __init__(self, nearest: NearestResource) -> None:
        self._nearest = nearest

    @cached_property
    def geo_species(self) -> GeoSpeciesResourceWithStreamingResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return GeoSpeciesResourceWithStreamingResponse(self._nearest.geo_species)


class AsyncNearestResourceWithStreamingResponse:
    def __init__(self, nearest: AsyncNearestResource) -> None:
        self._nearest = nearest

    @cached_property
    def geo_species(self) -> AsyncGeoSpeciesResourceWithStreamingResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncGeoSpeciesResourceWithStreamingResponse(self._nearest.geo_species)
