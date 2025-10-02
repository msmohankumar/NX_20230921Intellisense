from ....NXOpen import *
from ...Schematic import *
from ..Model import *

import typing
import enum

class BaseObject(NXObject):
    def __init__(self) -> None: ...
    Identifier: str


