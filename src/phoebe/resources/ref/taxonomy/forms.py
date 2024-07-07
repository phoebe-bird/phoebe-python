# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.ref.taxonomy.form_list_response import FormListResponse

__all__ = ["FormsResource", "AsyncFormsResource"]


class FormsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FormsResourceWithRawResponse:
        return FormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormsResourceWithStreamingResponse:
        return FormsResourceWithStreamingResponse(self)

    def list(
        self,
        species_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormListResponse:
        """For a species, get the list of subspecies recognised in the taxonomy.

        The
        results include the species that was passed in.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not species_code:
            raise ValueError(f"Expected a non-empty value for `species_code` but received {species_code!r}")
        return self._get(
            f"/ref/taxon/forms/{species_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormListResponse,
        )


class AsyncFormsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFormsResourceWithRawResponse:
        return AsyncFormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormsResourceWithStreamingResponse:
        return AsyncFormsResourceWithStreamingResponse(self)

    async def list(
        self,
        species_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormListResponse:
        """For a species, get the list of subspecies recognised in the taxonomy.

        The
        results include the species that was passed in.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not species_code:
            raise ValueError(f"Expected a non-empty value for `species_code` but received {species_code!r}")
        return await self._get(
            f"/ref/taxon/forms/{species_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormListResponse,
        )


class FormsResourceWithRawResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.list = to_raw_response_wrapper(
            forms.list,
        )


class AsyncFormsResourceWithRawResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.list = async_to_raw_response_wrapper(
            forms.list,
        )


class FormsResourceWithStreamingResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.list = to_streamed_response_wrapper(
            forms.list,
        )


class AsyncFormsResourceWithStreamingResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.list = async_to_streamed_response_wrapper(
            forms.list,
        )
