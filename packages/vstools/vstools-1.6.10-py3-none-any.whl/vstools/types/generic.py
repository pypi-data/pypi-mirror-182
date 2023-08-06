from __future__ import annotations

from typing import Any, Callable, Literal, Protocol, TypeAlias, TypeVar, Union
from enum import Enum, auto
import vapoursynth as vs

from .builtins import F, SingleOrArr, SingleOrArrOpt, SupportsString

__all__ = [
    'MissingT', 'MISSING',

    'FuncExceptT',

    'DataType', 'VSMapValue', 'BoundVSMapValue', 'VSMapValueCallback',

    'VideoFormatT',

    'HoldsVideoFormatT', 'HoldsPropValueT',

    'VSFunction', 'GenericVSFunction',

    'StrArr', 'StrArrOpt',

    'PassthroughC',

    'ConstantFormatVideoNode'
]


class MissingTBase(Enum):
    MissingT = auto()


MissingT: TypeAlias = Literal[MissingTBase.MissingT]
MISSING = MissingTBase.MissingT


DataType = Union[str, bytes, bytearray, SupportsString]

VSMapValue = Union[
    SingleOrArr[int],
    SingleOrArr[float],
    SingleOrArr[DataType],
    SingleOrArr[vs.VideoNode],
    SingleOrArr[vs.VideoFrame],
    SingleOrArr[vs.AudioNode],
    SingleOrArr[vs.AudioFrame],
    SingleOrArr['VSMapValueCallback[Any]']
]

BoundVSMapValue = TypeVar('BoundVSMapValue', bound=VSMapValue)

VSMapValueCallback = Callable[..., BoundVSMapValue]

VideoFormatT = Union[vs.PresetFormat, vs.VideoFormat]

# TODO change to | when mypy fixes bug upstream
HoldsVideoFormatT = Union[vs.VideoNode, vs.VideoFrame, vs.VideoFormat]
HoldsPropValueT = Union[vs.FrameProps, vs.VideoFrame, vs.AudioFrame, vs.VideoNode, vs.AudioNode]

FuncExceptT = str | Callable[..., Any] | tuple[Callable[..., Any] | str, str]  # type: ignore


class VSFunction(Protocol):
    def __call__(self, clip: vs.VideoNode, *args: Any, **kwargs: Any) -> vs.VideoNode:
        ...


GenericVSFunction = Callable[..., vs.VideoNode]


StrArr = SingleOrArr[SupportsString]
StrArrOpt = SingleOrArrOpt[SupportsString]

PassthroughC = Callable[[F], F]


class ConstantFormatVideoNode(vs.VideoNode):
    format: vs.VideoFormat
