# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from .top100 import (
    Top100Resource,
    AsyncTop100Resource,
    Top100ResourceWithRawResponse,
    AsyncTop100ResourceWithRawResponse,
    Top100ResourceWithStreamingResponse,
    AsyncTop100ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .checklist import (
    ChecklistResource,
    AsyncChecklistResource,
    ChecklistResourceWithRawResponse,
    AsyncChecklistResourceWithRawResponse,
    ChecklistResourceWithStreamingResponse,
    AsyncChecklistResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .lists.lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from .species_list import (
    SpeciesListResource,
    AsyncSpeciesListResource,
    SpeciesListResourceWithRawResponse,
    AsyncSpeciesListResourceWithRawResponse,
    SpeciesListResourceWithStreamingResponse,
    AsyncSpeciesListResourceWithStreamingResponse,
)

__all__ = ["ProductResource", "AsyncProductResource"]


class ProductResource(SyncAPIResource):
    @cached_property
    def lists(self) -> ListsResource:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return ListsResource(self._client)

    @cached_property
    def top100(self) -> Top100Resource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return Top100Resource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return StatsResource(self._client)

    @cached_property
    def species_list(self) -> SpeciesListResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return SpeciesListResource(self._client)

    @cached_property
    def checklist(self) -> ChecklistResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return ChecklistResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return ProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return ProductResourceWithStreamingResponse(self)


class AsyncProductResource(AsyncAPIResource):
    @cached_property
    def lists(self) -> AsyncListsResource:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncListsResource(self._client)

    @cached_property
    def top100(self) -> AsyncTop100Resource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncTop100Resource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncStatsResource(self._client)

    @cached_property
    def species_list(self) -> AsyncSpeciesListResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncSpeciesListResource(self._client)

    @cached_property
    def checklist(self) -> AsyncChecklistResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncChecklistResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return AsyncProductResourceWithStreamingResponse(self)


class ProductResourceWithRawResponse:
    def __init__(self, product: ProductResource) -> None:
        self._product = product

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return ListsResourceWithRawResponse(self._product.lists)

    @cached_property
    def top100(self) -> Top100ResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return Top100ResourceWithRawResponse(self._product.top100)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return StatsResourceWithRawResponse(self._product.stats)

    @cached_property
    def species_list(self) -> SpeciesListResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return SpeciesListResourceWithRawResponse(self._product.species_list)

    @cached_property
    def checklist(self) -> ChecklistResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return ChecklistResourceWithRawResponse(self._product.checklist)


class AsyncProductResourceWithRawResponse:
    def __init__(self, product: AsyncProductResource) -> None:
        self._product = product

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncListsResourceWithRawResponse(self._product.lists)

    @cached_property
    def top100(self) -> AsyncTop100ResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncTop100ResourceWithRawResponse(self._product.top100)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncStatsResourceWithRawResponse(self._product.stats)

    @cached_property
    def species_list(self) -> AsyncSpeciesListResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncSpeciesListResourceWithRawResponse(self._product.species_list)

    @cached_property
    def checklist(self) -> AsyncChecklistResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncChecklistResourceWithRawResponse(self._product.checklist)


class ProductResourceWithStreamingResponse:
    def __init__(self, product: ProductResource) -> None:
        self._product = product

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return ListsResourceWithStreamingResponse(self._product.lists)

    @cached_property
    def top100(self) -> Top100ResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return Top100ResourceWithStreamingResponse(self._product.top100)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return StatsResourceWithStreamingResponse(self._product.stats)

    @cached_property
    def species_list(self) -> SpeciesListResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return SpeciesListResourceWithStreamingResponse(self._product.species_list)

    @cached_property
    def checklist(self) -> ChecklistResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return ChecklistResourceWithStreamingResponse(self._product.checklist)


class AsyncProductResourceWithStreamingResponse:
    def __init__(self, product: AsyncProductResource) -> None:
        self._product = product

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        """
        The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
        """
        return AsyncListsResourceWithStreamingResponse(self._product.lists)

    @cached_property
    def top100(self) -> AsyncTop100ResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncTop100ResourceWithStreamingResponse(self._product.top100)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncStatsResourceWithStreamingResponse(self._product.stats)

    @cached_property
    def species_list(self) -> AsyncSpeciesListResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncSpeciesListResourceWithStreamingResponse(self._product.species_list)

    @cached_property
    def checklist(self) -> AsyncChecklistResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncChecklistResourceWithStreamingResponse(self._product.checklist)
