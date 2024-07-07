# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AdjacentListResponse", "AdjacentRegion"]


class AdjacentRegion(BaseModel):
    code: Optional[str] = None

    name: Optional[str] = None


class AdjacentListResponse(BaseModel):
    adjacent_regions: Optional[List[AdjacentRegion]] = FieldInfo(alias="adjacentRegions", default=None)
