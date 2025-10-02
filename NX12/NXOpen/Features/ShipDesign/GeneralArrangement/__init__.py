from .....NXOpen import *
from ....Features import *
from ...ShipDesign import *
from ..GeneralArrangement import *

import typing
import enum

class FaceCharacteristicsBuilder(Builder):
    def __init__(self) -> None: ...
    CharacteristicColor: NXColor
    CharacteristicValue: int
    SelectFace: ScCollector


