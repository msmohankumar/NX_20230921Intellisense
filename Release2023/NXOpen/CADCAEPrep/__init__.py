from ...NXOpen import *
from ..CADCAEPrep import *

import typing
import enum

class OrientationByVector(CADCAEPrep.IOrientation):
    def __init__(self) -> None: ...


    class OrientAxis(enum.Enum):
        Y = 2
        Z = 3
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class IOrientation(NXObject):
    def __init__(self) -> None: ...


class IdealizedBeamManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def GetSection(self, sectionName: str) -> CADCAEPrep.IBeamSection:
        ...
    def AddBeamSectionRod(self, sectionName: str, radius: float) -> CADCAEPrep.BeamSectionRod:
        ...
    def AddBeamSectionBox(self, sectionName: str, width: float, height: float, thicknessTopBottom: float, thicknessSides: float) -> CADCAEPrep.BeamSectionBox:
        ...
    def AddBeamSectionChan(self, sectionName: str, width: float, height: float, flangeThickness: float, webThickness: float) -> CADCAEPrep.BeamSectionChan:
        ...
    def AddBeamSectionHexa(self, sectionName: str, sideWidth: float, overallWidth: float, height: float) -> CADCAEPrep.BeamSectionHexa:
        ...
    def AddBeamSectionT(self, sectionName: str, width: float, height: float, flangeThickness: float, webThickness: float) -> CADCAEPrep.BeamSectionT:
        ...
    def AddBeamSectionBar(self, sectionName: str, width: float, height: float) -> CADCAEPrep.BeamSectionBar:
        ...
    def AddBeamSectionI(self, sectionName: str, height: float, widthBottomFlange: float, widthTopFlange: float, thicknessWeb: float, thicknessBottomFlange: float, thicknessTopFlange: float) -> CADCAEPrep.BeamSectionI:
        ...
    def AddBeamSectionL(self, sectionName: str, lengthVertical: float, lengthHorizontal: float, thicknessVertical: float, thicknessHorizontal: float) -> CADCAEPrep.BeamSectionL:
        ...
    def AddBeamSectionTube(self, sectionName: str, radiusOutside: float, radiusInside: float) -> CADCAEPrep.BeamSectionTube:
        ...
    def AddBeamSectionSketch(self, sectionName: str, sketchTag: Sketch) -> CADCAEPrep.BeamSectionSketch:
        ...
    def AddIdealizedBeam(self, curve: Curve) -> CADCAEPrep.IdealizedBeam:
        ...
    def GetIdealizedBeam(self, curve: Curve) -> CADCAEPrep.IdealizedBeam:
        ...
    def Tag(self) -> Tag: ...

    IBeamSectionCollection: CADCAEPrep.IBeamSectionCollection
    IdealizedBeamCollection: CADCAEPrep.IdealizedBeamCollection


class IdealizedBeamCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CADCAEPrep.IdealizedBeam]:
        ...
    def __init__(self, owner: CADCAEPrep.IdealizedBeamManager) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class IdealizedBeam(NXObject):
    def __init__(self) -> None: ...
    def GetOrientationByVector(self, orientVect: Vector3d, orientAxis: CADCAEPrep.OrientationByVector.OrientAxis, flipY: bool, flipZ: bool) -> None:
        ...
    def SetOrientationByVector(self, orientVect: Vector3d, orientAxis: CADCAEPrep.OrientationByVector.OrientAxis, flipY: bool, flipZ: bool) -> None:
        ...
    Curve: Curve
    Material: PhysicalMaterial
    MeshCollectorPrefix: str
    OffsetEnd: Point2d
    OffsetStart: Point2d
    Section: CADCAEPrep.IBeamSection
    XOffsetEnd: float
    XOffsetStart: float


class IBeamSectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CADCAEPrep.IBeamSection]:
        ...
    def __init__(self, owner: CADCAEPrep.IdealizedBeamManager) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class IBeamSection(NXObject):
    def __init__(self) -> None: ...
    Name: str
    Type: CADCAEPrep.IBeamSection.Sectiontype


    class Sectiontype(enum.Enum):
        Unknown = 0
        Sketch = 100
        Rod = 200
        Tube = 300
        Hexa = 400
        Bar = 500
        Box = 600
        T = 700
        L = 800
        I = 900
        Chan = 1000
    

class BeamSectionTube(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, radiusOutside: float, radiusInside: float) -> None:
        ...
    Ri: float
    Ro: float


class BeamSectionT(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, width: float, height: float, flangeThickness: float, webThickness: float) -> None:
        ...
    H: float
    Tf: float
    Tw: float
    W: float


class BeamSectionSketch(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, sketch: Sketch) -> None:
        ...
    OriginBoundingBoxCenterOffset: Point2d
    Sketch: Sketch


class BeamSectionRod(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, radius: float) -> None:
        ...
    R: float


class BeamSectionL(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, lengthVertical: float, lengthHorizontal: float, thicknessHorizontal: float, thicknessVertical: float) -> None:
        ...
    Lh: float
    Lv: float
    Th: float
    Tv: float


class BeamSectionI(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, height: float, widthBottomFlange: float, widthTopFlange: float, thicknessWeb: float, thicknessBottomFlange: float, thicknessTopFlange: float) -> None:
        ...
    H: float
    Tbf: float
    Ttf: float
    Tw: float
    Wbf: float
    Wtf: float


class BeamSectionHexa(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, sideWidth: float, overallWidth: float, height: float) -> None:
        ...
    H: float
    W: float
    Ws: float


class BeamSectionChan(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, width: float, height: float, webThickness: float, flangeThickness: float) -> None:
        ...
    H: float
    Tf: float
    Tw: float
    W: float


class BeamSectionBox(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, width: float, height: float, thicknessTopBottom: float, thicknessSides: float) -> None:
        ...
    H: float
    Tss: float
    Ttb: float
    W: float


class BeamSectionBar(CADCAEPrep.IBeamSection):
    def __init__(self) -> None: ...
    def Edit(self, width: float, height: float) -> None:
        ...
    H: float
    W: float


