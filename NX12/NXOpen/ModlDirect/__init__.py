from ...NXOpen import *
from ..ModlDirect import *

import typing
import enum

class SelectBlend(TaggedObject):
    def __init__(self) -> None: ...
    def RecognizeBlends(self, baseFaces: typing.List[Face], blends: typing.List[Face]) -> None:
        ...
    def IncludeBlend(self, blendFace: Face) -> None:
        ...
    def ExcludeBlend(self, blendFace: Face) -> None:
        ...
    def Validate(self) -> bool:
        ...
    FaceCollector: ScCollector


