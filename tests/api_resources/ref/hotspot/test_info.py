# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from phoebe_bird import Phoebe, AsyncPhoebe
from tests.utils import assert_matches_type
from phoebe_bird.types.ref.hotspot import InfoRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Phoebe) -> None:
        info = client.ref.hotspot.info.retrieve(
            "locId",
        )
        assert_matches_type(InfoRetrieveResponse, info, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Phoebe) -> None:
        response = client.ref.hotspot.info.with_raw_response.retrieve(
            "locId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        info = response.parse()
        assert_matches_type(InfoRetrieveResponse, info, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Phoebe) -> None:
        with client.ref.hotspot.info.with_streaming_response.retrieve(
            "locId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            info = response.parse()
            assert_matches_type(InfoRetrieveResponse, info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Phoebe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loc_id` but received ''"):
            client.ref.hotspot.info.with_raw_response.retrieve(
                "",
            )


class TestAsyncInfo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPhoebe) -> None:
        info = await async_client.ref.hotspot.info.retrieve(
            "locId",
        )
        assert_matches_type(InfoRetrieveResponse, info, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPhoebe) -> None:
        response = await async_client.ref.hotspot.info.with_raw_response.retrieve(
            "locId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        info = await response.parse()
        assert_matches_type(InfoRetrieveResponse, info, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPhoebe) -> None:
        async with async_client.ref.hotspot.info.with_streaming_response.retrieve(
            "locId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            info = await response.parse()
            assert_matches_type(InfoRetrieveResponse, info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPhoebe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loc_id` but received ''"):
            await async_client.ref.hotspot.info.with_raw_response.retrieve(
                "",
            )
