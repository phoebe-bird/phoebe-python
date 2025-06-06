# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .notable import (
    NotableResource,
    AsyncNotableResource,
    NotableResourceWithRawResponse,
    AsyncNotableResourceWithRawResponse,
    NotableResourceWithStreamingResponse,
    AsyncNotableResourceWithStreamingResponse,
)
from .species import (
    SpeciesResource,
    AsyncSpeciesResource,
    SpeciesResourceWithRawResponse,
    AsyncSpeciesResourceWithRawResponse,
    SpeciesResourceWithStreamingResponse,
    AsyncSpeciesResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.data.observations.geo import recent_list_params
from ......types.data.observations.geo.recent_list_response import RecentListResponse

__all__ = ["RecentResource", "AsyncRecentResource"]


class RecentResource(SyncAPIResource):
    @cached_property
    def species(self) -> SpeciesResource:
        return SpeciesResource(self._client)

    @cached_property
    def notable(self) -> NotableResource:
        return NotableResource(self._client)

    @cached_property
    def with_raw_response(self) -> RecentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return RecentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return RecentResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        lat: float,
        lng: float,
        back: int | NotGiven = NOT_GIVEN,
        cat: Literal["species", "slash", "issf", "spuh", "hybrid", "domestic", "form", "intergrade"]
        | NotGiven = NOT_GIVEN,
        dist: int | NotGiven = NOT_GIVEN,
        hotspot: bool | NotGiven = NOT_GIVEN,
        include_provisional: bool | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sort: Literal["date", "species"] | NotGiven = NOT_GIVEN,
        spp_locale: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecentListResponse:
        """
        Get the list of recent observations (up to 30 days ago) of birds seen at
        locations within a radius of up to 50 kilometers, from a given set of
        coordinates. Results include only the most recent observation for each species
        in the region specified.

        Args:
          back: The number of days back to fetch observations.

          cat: Only fetch observations from these taxonomic categories

          dist: The search radius from the given position, in kilometers.

          hotspot: Only fetch observations from hotspots

          include_provisional: Include observations which have not yet been reviewed.

          max_results: Only fetch this number of observations

          sort: Sort observations by taxonomy or by date, most recent first.

          spp_locale: Use this language for species common names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data/obs/geo/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "back": back,
                        "cat": cat,
                        "dist": dist,
                        "hotspot": hotspot,
                        "include_provisional": include_provisional,
                        "max_results": max_results,
                        "sort": sort,
                        "spp_locale": spp_locale,
                    },
                    recent_list_params.RecentListParams,
                ),
            ),
            cast_to=RecentListResponse,
        )


class AsyncRecentResource(AsyncAPIResource):
    @cached_property
    def species(self) -> AsyncSpeciesResource:
        return AsyncSpeciesResource(self._client)

    @cached_property
    def notable(self) -> AsyncNotableResource:
        return AsyncNotableResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRecentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return AsyncRecentResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        lat: float,
        lng: float,
        back: int | NotGiven = NOT_GIVEN,
        cat: Literal["species", "slash", "issf", "spuh", "hybrid", "domestic", "form", "intergrade"]
        | NotGiven = NOT_GIVEN,
        dist: int | NotGiven = NOT_GIVEN,
        hotspot: bool | NotGiven = NOT_GIVEN,
        include_provisional: bool | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sort: Literal["date", "species"] | NotGiven = NOT_GIVEN,
        spp_locale: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecentListResponse:
        """
        Get the list of recent observations (up to 30 days ago) of birds seen at
        locations within a radius of up to 50 kilometers, from a given set of
        coordinates. Results include only the most recent observation for each species
        in the region specified.

        Args:
          back: The number of days back to fetch observations.

          cat: Only fetch observations from these taxonomic categories

          dist: The search radius from the given position, in kilometers.

          hotspot: Only fetch observations from hotspots

          include_provisional: Include observations which have not yet been reviewed.

          max_results: Only fetch this number of observations

          sort: Sort observations by taxonomy or by date, most recent first.

          spp_locale: Use this language for species common names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data/obs/geo/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "back": back,
                        "cat": cat,
                        "dist": dist,
                        "hotspot": hotspot,
                        "include_provisional": include_provisional,
                        "max_results": max_results,
                        "sort": sort,
                        "spp_locale": spp_locale,
                    },
                    recent_list_params.RecentListParams,
                ),
            ),
            cast_to=RecentListResponse,
        )


class RecentResourceWithRawResponse:
    def __init__(self, recent: RecentResource) -> None:
        self._recent = recent

        self.list = to_raw_response_wrapper(
            recent.list,
        )

    @cached_property
    def species(self) -> SpeciesResourceWithRawResponse:
        return SpeciesResourceWithRawResponse(self._recent.species)

    @cached_property
    def notable(self) -> NotableResourceWithRawResponse:
        return NotableResourceWithRawResponse(self._recent.notable)


class AsyncRecentResourceWithRawResponse:
    def __init__(self, recent: AsyncRecentResource) -> None:
        self._recent = recent

        self.list = async_to_raw_response_wrapper(
            recent.list,
        )

    @cached_property
    def species(self) -> AsyncSpeciesResourceWithRawResponse:
        return AsyncSpeciesResourceWithRawResponse(self._recent.species)

    @cached_property
    def notable(self) -> AsyncNotableResourceWithRawResponse:
        return AsyncNotableResourceWithRawResponse(self._recent.notable)


class RecentResourceWithStreamingResponse:
    def __init__(self, recent: RecentResource) -> None:
        self._recent = recent

        self.list = to_streamed_response_wrapper(
            recent.list,
        )

    @cached_property
    def species(self) -> SpeciesResourceWithStreamingResponse:
        return SpeciesResourceWithStreamingResponse(self._recent.species)

    @cached_property
    def notable(self) -> NotableResourceWithStreamingResponse:
        return NotableResourceWithStreamingResponse(self._recent.notable)


class AsyncRecentResourceWithStreamingResponse:
    def __init__(self, recent: AsyncRecentResource) -> None:
        self._recent = recent

        self.list = async_to_streamed_response_wrapper(
            recent.list,
        )

    @cached_property
    def species(self) -> AsyncSpeciesResourceWithStreamingResponse:
        return AsyncSpeciesResourceWithStreamingResponse(self._recent.species)

    @cached_property
    def notable(self) -> AsyncNotableResourceWithStreamingResponse:
        return AsyncNotableResourceWithStreamingResponse(self._recent.notable)
