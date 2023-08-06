from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import betterproto


class Status(betterproto.Enum):
    """Possible face statuses."""

    STATUS_UNSPECIFIED = 0
    STATUS_LOADING = 1
    STATUS_READY = 2


@dataclass(eq=False, repr=False)
class GetMetadataRequest(betterproto.Message):
    """Request for GetMetadata."""

    pass


@dataclass(eq=False, repr=False)
class GetMetadataResponse(betterproto.Message):
    """Response from GetMetadata."""

    key: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetPostSchemaRequest(betterproto.Message):
    """Request for GetPostSchema."""

    pass


@dataclass(eq=False, repr=False)
class GetPostSchemaResponse(betterproto.Message):
    """Response from GetPostSchema."""

    schema: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetStatusRequest(betterproto.Message):
    """Request for GetStatus."""

    pass


@dataclass(eq=False, repr=False)
class GetStatusResponse(betterproto.Message):
    """Response from GetStatus."""

    status: "Status" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class WatchStatusRequest(betterproto.Message):
    """Request for WatchStatus."""

    pass


@dataclass(eq=False, repr=False)
class WatchStatusResponse(betterproto.Message):
    """Response from WatchStatus."""

    status: "Status" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class GetConfigSchemaRequest(betterproto.Message):
    """Request for GetConfigSchema."""

    pass


@dataclass(eq=False, repr=False)
class GetConfigSchemaResponse(betterproto.Message):
    """Response from GetConfigSchema."""

    schema: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetConfigRequest(betterproto.Message):
    """Request for GetConfig."""

    pass


@dataclass(eq=False, repr=False)
class GetConfigResponse(betterproto.Message):
    """Response from GetConfig."""

    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class WatchConfigRequest(betterproto.Message):
    """Request for WatchConfig."""

    pass


@dataclass(eq=False, repr=False)
class WatchConfigResponse(betterproto.Message):
    """Response from WatchConfig."""

    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SetConfigRequest(betterproto.Message):
    """Request for SetConfig."""

    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SetConfigResponse(betterproto.Message):
    """Response from SetConfig."""

    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PostRequest(betterproto.Message):
    """Request for Post."""

    content: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PostResponse(betterproto.Message):
    """Response from Post."""

    id: str = betterproto.string_field(1)
    url: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ScoreRequest(betterproto.Message):
    """Request for Score."""

    id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ScoreResponse(betterproto.Message):
    """Response from Score."""

    score: float = betterproto.double_field(1)


@dataclass(eq=False, repr=False)
class ScrapRequest(betterproto.Message):
    """Request for Scrap."""

    limit: Optional[int] = betterproto.uint64_field(
        1, optional=True, group="_limit"
    )
    before: Optional[datetime] = betterproto.message_field(
        2, optional=True, group="_before"
    )
    after: Optional[datetime] = betterproto.message_field(
        3, optional=True, group="_after"
    )


@dataclass(eq=False, repr=False)
class ScrapResponse(betterproto.Message):
    """Response from Scrap."""

    id: str = betterproto.string_field(1)
    content: str = betterproto.string_field(2)
    score: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class ResetRequest(betterproto.Message):
    """Request for Reset."""

    pass


@dataclass(eq=False, repr=False)
class ResetResponse(betterproto.Message):
    """Response from Reset."""

    pass


@dataclass(eq=False, repr=False)
class SaveRequest(betterproto.Message):
    """Request for Save."""

    pass


@dataclass(eq=False, repr=False)
class SaveResponse(betterproto.Message):
    """Response from Save."""

    pass
