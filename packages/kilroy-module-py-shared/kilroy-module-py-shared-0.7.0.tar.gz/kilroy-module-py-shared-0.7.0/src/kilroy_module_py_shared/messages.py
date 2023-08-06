from dataclasses import dataclass
from typing import List

import betterproto


class Status(betterproto.Enum):
    """Possible module statuses."""

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
class GenerateRequest(betterproto.Message):
    """Request for Generate."""

    quantity: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class GenerateResponse(betterproto.Message):
    """Response from Generate."""

    content: str = betterproto.string_field(1)
    metadata: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class FitSupervisedRequest(betterproto.Message):
    """Request for FitSupervised."""

    content: str = betterproto.string_field(1)
    score: float = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class FitSupervisedResponse(betterproto.Message):
    """Response from FitSupervised."""

    pass


@dataclass(eq=False, repr=False)
class FitReinforcedRequest(betterproto.Message):
    """Request for FitReinforced."""

    content: str = betterproto.string_field(1)
    metadata: str = betterproto.string_field(2)
    score: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class FitReinforcedResponse(betterproto.Message):
    """Response from FitReinforced."""

    pass


@dataclass(eq=False, repr=False)
class MetricConfig(betterproto.Message):
    """Metric configuration data."""

    id: str = betterproto.string_field(1)
    label: str = betterproto.string_field(2)
    config: str = betterproto.string_field(3)
    tags: List[str] = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class GetMetricsConfigRequest(betterproto.Message):
    """Request for GetMetricsConfig."""

    pass


@dataclass(eq=False, repr=False)
class GetMetricsConfigResponse(betterproto.Message):
    """Response from GetMetricsConfig."""

    configs: List["MetricConfig"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class WatchMetricsRequest(betterproto.Message):
    """Request for WatchMetrics."""

    pass


@dataclass(eq=False, repr=False)
class WatchMetricsResponse(betterproto.Message):
    """Response from WatchMetrics."""

    metric_id: str = betterproto.string_field(1)
    dataset_id: int = betterproto.uint64_field(2)
    data: str = betterproto.string_field(3)


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
