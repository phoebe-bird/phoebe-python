# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HotspotListResponse", "HotspotListResponseItem"]


class HotspotListResponseItem(BaseModel):
    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    lat: Optional[float] = None

    latest_obs_dt: Optional[str] = FieldInfo(alias="latestObsDt", default=None)

    lng: Optional[float] = None

    loc_id: Optional[str] = FieldInfo(alias="locId", default=None)

    loc_name: Optional[str] = FieldInfo(alias="locName", default=None)

    num_species_all_time: Optional[int] = FieldInfo(alias="numSpeciesAllTime", default=None)

    subnational1_code: Optional[str] = FieldInfo(alias="subnational1Code", default=None)

    subnational2_code: Optional[str] = FieldInfo(alias="subnational2Code", default=None)


HotspotListResponse = List[HotspotListResponseItem]
