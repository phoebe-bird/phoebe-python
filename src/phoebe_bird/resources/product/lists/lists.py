# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .historical import (
    HistoricalResource,
    AsyncHistoricalResource,
    HistoricalResourceWithRawResponse,
    AsyncHistoricalResourceWithRawResponse,
    HistoricalResourceWithStreamingResponse,
    AsyncHistoricalResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.product import list_retrieve_params
from ....types.product.list_retrieve_response import ListRetrieveResponse

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    """
    The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
    """

    @cached_property
    def historical(self) -> HistoricalResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return HistoricalResource(self._client)

    @cached_property
    def with_raw_response(self) -> ListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return ListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return ListsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        region_code: str,
        *,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveResponse:
        """
        Get information on the most recently submitted checklists for a region.

        Args:
          max_results: Only fetch this number of checklists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not region_code:
            raise ValueError(f"Expected a non-empty value for `region_code` but received {region_code!r}")
        return self._get(
            path_template("/product/lists/{region_code}", region_code=region_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"max_results": max_results}, list_retrieve_params.ListRetrieveParams),
            ),
            cast_to=ListRetrieveResponse,
        )


class AsyncListsResource(AsyncAPIResource):
    """
    The data/obs end-points are used to fetch observations submitted to eBird in checklists. There are two categories of end-point: 1. Fetch observations for a specific country, region or location. 2. Fetch observations for nearby locations - up to a distance of 50km. Each end-point supports optional query parameters which allow you to filter the list of observations returned.
    """

    @cached_property
    def historical(self) -> AsyncHistoricalResource:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncHistoricalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/phoebe-bird/phoebe-python#with_streaming_response
        """
        return AsyncListsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        region_code: str,
        *,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveResponse:
        """
        Get information on the most recently submitted checklists for a region.

        Args:
          max_results: Only fetch this number of checklists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not region_code:
            raise ValueError(f"Expected a non-empty value for `region_code` but received {region_code!r}")
        return await self._get(
            path_template("/product/lists/{region_code}", region_code=region_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"max_results": max_results}, list_retrieve_params.ListRetrieveParams
                ),
            ),
            cast_to=ListRetrieveResponse,
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve = to_raw_response_wrapper(
            lists.retrieve,
        )

    @cached_property
    def historical(self) -> HistoricalResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return HistoricalResourceWithRawResponse(self._lists.historical)


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve = async_to_raw_response_wrapper(
            lists.retrieve,
        )

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithRawResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncHistoricalResourceWithRawResponse(self._lists.historical)


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve = to_streamed_response_wrapper(
            lists.retrieve,
        )

    @cached_property
    def historical(self) -> HistoricalResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return HistoricalResourceWithStreamingResponse(self._lists.historical)


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve = async_to_streamed_response_wrapper(
            lists.retrieve,
        )

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithStreamingResponse:
        """
        The product end-points make it easy to get the information shown in various pages on the eBird web site: 1. The Top 100 contributors on a given date. 2. The checklists submitted on a given date. 3. The most recent checklists submitted. 4. A summary of the checklists submitted on a given date. 5. The details and all the observations of a checklist.
        """
        return AsyncHistoricalResourceWithStreamingResponse(self._lists.historical)
