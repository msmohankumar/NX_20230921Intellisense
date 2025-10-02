from ....NXOpen import *
from ...GeometricAnalysis import *
from ..SectionAnalysis import *

import typing
import enum

class XYZPlaneBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AnchorOrigin: Point3d
    AnchorXAxis: Vector3d
    AnchorYAxis: Vector3d
    IsNumberEnabled: bool
    IsSpacingEnabled: bool
    IsXEnabled: bool
    IsYEnabled: bool
    IsZEnabled: bool
    Number: int
    Spacing: float


class TriangularGridBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Spacing: GeometricAnalysis.SectionAnalysis.GridSpacingBuilder
    SpecifiedPlane: GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder
    TriangularFrame: GeometricUtilities.TriangularFrameBuilder


class SectionPlaneBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Origin: Point3d
    Plane: GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder.PlaneType
    XAxis: Vector3d
    YAxis: Vector3d


    class PlaneType(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
        View = 3
        Plane = 4
    

class SectionAnalysisExObject(GeometricAnalysis.AnalysisObject):
    def __init__(self) -> None: ...


class SectionAnalysisExBuilder(Builder):
    def __init__(self) -> None: ...
    Alignment: GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.AlignmentType
    CalculationMethod: GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.CalculationMethodType
    CombOptions: GeometricUtilities.CombOptionsBuilder
    CurveAligned: GeometricAnalysis.SectionAnalysis.CurveAlignedBuilder
    Interactive: GeometricAnalysis.SectionAnalysis.InteractiveBuilder
    IsShowInflectionPointsEnabled: bool
    IsShowLengthEnabled: bool
    IsShowPeakPointsEnabled: bool
    Isoparametric: GeometricAnalysis.SectionAnalysis.IsoparametricBuilder
    NeedleDirection: GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.NeedleDirectionType
    Output: GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.OutputType
    ParallelPlanes: GeometricAnalysis.SectionAnalysis.ParallelPlanesExBuilder
    Placement: GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.PlacementType
    Radial: GeometricAnalysis.SectionAnalysis.RadialBuilder
    ScalingMethod: GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.ScalingMethodType
    SelectObject: SelectTaggedObjectList
    SpecifyPoint: SelectPointList
    XYZPlane: GeometricAnalysis.SectionAnalysis.XYZPlaneBuilder


    class ScalingMethodType(enum.Enum):
        Linear = 0
        Logarithmic = 1
    

    class PlacementType(enum.Enum):
        Uniform = 0
        ThroughPoints = 1
        BetweenPoints = 2
        Interactive = 3
    

    class OutputType(enum.Enum):
        AnalysisObject = 0
        SectionCurves = 1
        Both = 2
    

    class NeedleDirectionType(enum.Enum):
        Inside = 0
        Outside = 1
    

    class CalculationMethodType(enum.Enum):
        Curvature = 0
        RadiusofCurvature = 1
    

    class AlignmentType(enum.Enum):
        XYZPlane = 0
        ParallelPlanes = 1
        CurveAligned = 2
        Isoparametric = 3
        Radial = 4
    

class SectionAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    CalculationMethod: GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.CalculationMethodType
    CircularGrid: GeometricAnalysis.SectionAnalysis.CircularGridBuilder
    CombOptions: GeometricUtilities.CombOptionsBuilder
    NeedleDirection: GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.NeedleDirectionType
    Output: GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.OutputType
    QuadrilateralGrid: GeometricAnalysis.SectionAnalysis.QuadrilateralGridBuilder
    References: SelectTaggedObjectList
    ScalingMethod: GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.ScalingMethodType
    ShowInflectionPoints: bool
    ShowPeakPoints: bool
    ShowSectionLength: bool
    TriangularGrid: GeometricAnalysis.SectionAnalysis.TriangularGridBuilder
    Type: GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types


    class Types(enum.Enum):
        Parallel = 0
        Isoparametric = 1
        AlongCurve = 2
        Quadrilateral = 3
        Triangular = 4
        Circular = 5
    

    class ScalingMethodType(enum.Enum):
        Linear = 0
        Logarithmic = 1
    

    class OutputType(enum.Enum):
        AnalysisObject = 0
        SectionCurves = 1
        Both = 2
    

    class NeedleDirectionType(enum.Enum):
        Inside = 0
        Outside = 1
    

    class CalculationMethodType(enum.Enum):
        Curvature = 0
        RadiusofCurvature = 1
    

class RadialBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    IsSpacingEnabled: bool
    Number: int
    Offset: float
    RotationAxis: GeometricAnalysis.SectionAnalysis.RadialBuilder.RotationAxisType
    RotationVector: Vector3d
    Spacing: float
    SpecifiedRotationPoint: Point
    StartPosition: SelectPoint


    class RotationAxisType(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
        View = 3
        ArbitraryVector = 4
    

class QuadrilateralGridBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    QuadrilateralFrame: GeometricUtilities.QuadrilateralFrameBuilder
    Spacing: GeometricAnalysis.SectionAnalysis.GridSpacingBuilder
    SpecifiedPlane: GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder


class ParallelPlanesExBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    IsNumberEnabled: bool
    IsSpacingEnabled: bool
    Number: int
    Offset: float
    Spacing: float
    SpecifiedPlane: GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder


class IsoparametricBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    IsSpacingEnabled: bool
    IsUEnabled: bool
    IsVEnabled: bool
    Number: int
    Spacing: float


class InteractiveBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    InteractiveSection: GeometricUtilities.InteractiveSectionBuilder
    IsCutInfiniteEnabled: bool


class GridSpacingBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BoundSections1: bool
    BoundSections2: bool
    Interval1: float
    Interval2: float
    LockInterval1: bool
    LockInterval2: bool
    SectionNumber1: int
    SectionNumber2: int


class CurveAlignedBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Curves: ScCollector
    IsSpacingEnabled: bool
    Number: int
    Offset: float
    Spacing: float
    SpecifiedPlane: GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder
    UseProjectedCurve: bool


class CircularGridBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CircularFrame: GeometricUtilities.CircularFrameBuilder
    Spacing: GeometricAnalysis.SectionAnalysis.GridSpacingBuilder
    SpecifiedPlane: GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder


