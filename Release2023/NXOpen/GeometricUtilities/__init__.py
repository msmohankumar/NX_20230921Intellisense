from . import UVMapping
from ...NXOpen import *
from ..GeometricUtilities import *

import typing
import enum

class WaveLinkRepository(NXObject):
    def __init__(self) -> None: ...
    def SetBuilder(self, builder: Builder) -> None:
        ...
    def SetLink(self, linkFeature: Features.Feature) -> None:
        ...
    def Destroy(self) -> None:
        ...
    def SetNonFeatureApplication(self, flag: bool) -> None:
        ...


class VoronoiItemListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateVoronoiItemBuilder(self) -> GeometricUtilities.VoronoiItemBuilder:
        ...
    def Validate(self) -> bool:
        ...
    List: GeometricUtilities.VoronoiItemBuilderList


class VoronoiItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.VoronoiItemBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.VoronoiItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.VoronoiItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.VoronoiItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.VoronoiItemBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.VoronoiItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.VoronoiItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.VoronoiItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.VoronoiItemBuilder, object2: GeometricUtilities.VoronoiItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.VoronoiItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class VoronoiItemBuilder(Builder):
    def __init__(self) -> None: ...
    PoreSize: Expression
    RodDiameter: Expression
    Selection: SelectDisplayableObjectList


class UnnestModuleBuilder(Builder):
    def __init__(self) -> None: ...
    ModuleToUnnest: Features.SelectFeature


class UnitCellBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ApproximateSourceHexMeshSize: Expression
    CellType: GeometricUtilities.UnitCellBuilder.UnitCellType
    CellTypeName: str
    CustomUnitCellFile: str
    EdgeLength: Expression
    IsUniformCube: bool
    SizeX: Expression
    SizeY: Expression
    SizeZ: Expression
    UnitCellBody: ScCollector


    class UnitCellType(enum.Enum):
        BiTriangle = 0
        TriDiametral = 1
        TriDiametralChevron = 2
        QuadDiametral = 3
        QuadDiametralLine = 4
        QuadDiametralCross = 5
        Dodecahedron = 6
        Star = 7
        HexStar = 8
        PseudoSierpinski = 9
        HexVase = 10
        HexVaseMod = 11
        Cubeplex = 12
        Octapeak = 13
        Octahedroid = 14
        FromFile = 15
        FromPart = 16
    

class Type(enum.Enum):
    NoOffset = 0
    NonsymmetricOffset = 1
    SymmetricOffset = 2
    SingleOffset = 3


class TwoExpressionsSectionSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.TwoExpressionsSectionSet]) -> None:
        ...
    def Append(self, object: GeometricUtilities.TwoExpressionsSectionSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.TwoExpressionsSectionSet) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.TwoExpressionsSectionSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TwoExpressionsSectionSet) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TwoExpressionsSectionSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.TwoExpressionsSectionSet]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.TwoExpressionsSectionSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.TwoExpressionsSectionSet, object2: GeometricUtilities.TwoExpressionsSectionSet) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.TwoExpressionsSectionSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TwoExpressionsSectionSet(ExpressionSectionSet):
    def __init__(self) -> None: ...
    ItemValueTwo: Expression


class TwoExpressionsCollectorSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.TwoExpressionsCollectorSet]) -> None:
        ...
    def Append(self, object: GeometricUtilities.TwoExpressionsCollectorSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.TwoExpressionsCollectorSet) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.TwoExpressionsCollectorSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TwoExpressionsCollectorSet) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TwoExpressionsCollectorSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.TwoExpressionsCollectorSet]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.TwoExpressionsCollectorSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.TwoExpressionsCollectorSet, object2: GeometricUtilities.TwoExpressionsCollectorSet) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.TwoExpressionsCollectorSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TwoExpressionsCollectorSet(ExpressionCollectorSet):
    def __init__(self) -> None: ...
    ItemValueTwo: Expression


class TrimCurveBoundingObjectBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.TrimCurveBoundingObjectBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.TrimCurveBoundingObjectBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.TrimCurveBoundingObjectBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.TrimCurveBoundingObjectBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TrimCurveBoundingObjectBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TrimCurveBoundingObjectBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.TrimCurveBoundingObjectBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.TrimCurveBoundingObjectBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.TrimCurveBoundingObjectBuilder, object2: GeometricUtilities.TrimCurveBoundingObjectBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.TrimCurveBoundingObjectBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TrimCurveBoundingObjectBuilder(TaggedObject):
    def __init__(self) -> None: ...
    BoundingObject: SelectDisplayableObject
    BoundingObjectList: SelectDisplayableObjectList
    BoundingObjectMethodType: GeometricUtilities.TrimCurveBoundingObjectBuilder.Method
    BoundingPlane: Plane


    class Method(enum.Enum):
        SelectObject = 0
        SelectPlane = 1
    

class TriangularFrameBuilder(GeometricUtilities.ShapeFrameBuilder):
    def __init__(self) -> None: ...
    Subtype: GeometricUtilities.TriangularFrameBuilder.Subtypes


    class Subtypes(enum.Enum):
        Arbitrary = 0
        Isosceles = 1
        Equilateral = 2
        Rightangle = 3
    

class TransitionLawNodeBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.TransitionLawNodeBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.TransitionLawNodeBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.TransitionLawNodeBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.TransitionLawNodeBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TransitionLawNodeBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TransitionLawNodeBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.TransitionLawNodeBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.TransitionLawNodeBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.TransitionLawNodeBuilder, object2: GeometricUtilities.TransitionLawNodeBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.TransitionLawNodeBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TransitionLawNodeBuilder(GeometricUtilities.OnPathDimWithValueBuilder):
    def __init__(self) -> None: ...
    Transition: GeometricUtilities.TransitionLawNodeBuilder.TransitionType


    class TransitionType(enum.Enum):
        Unknown = 0
        Constant = 1
        Linear = 2
        Blend = 3
        Minmax = 4
    

class TransitionCurveBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.TransitionCurveBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.TransitionCurveBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.TransitionCurveBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.TransitionCurveBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TransitionCurveBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.TransitionCurveBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.TransitionCurveBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.TransitionCurveBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.TransitionCurveBuilder, object2: GeometricUtilities.TransitionCurveBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.TransitionCurveBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TransitionCurveBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndTangentDirection: GeometricUtilities.TransitionCurveBuilder.TangentDirections
    EndTangentMagnitude: Expression
    StartTangentDirection: GeometricUtilities.TransitionCurveBuilder.TangentDirections
    StartTangentMagnitude: Expression


    class TangentDirections(enum.Enum):
        Rail = 0
        Limit = 1
    

class TransformerData(TaggedObject):
    def __init__(self) -> None: ...
    def Reverse(self, axisType: GeometricUtilities.TransformerData.ObjectType) -> None:
        ...
    def StartTransformation(self) -> None:
        ...
    def UpdateOnOriginMove(self) -> None:
        ...
    def Translate(self, axisType: GeometricUtilities.TransformerData.ObjectType, distance: float) -> None:
        ...
    def Rotate(self, axisType: GeometricUtilities.TransformerData.ObjectType, angle: float) -> None:
        ...
    def Scale(self, axisType: GeometricUtilities.TransformerData.ObjectType, factor: float) -> None:
        ...
    def Activate(self, objectType: GeometricUtilities.TransformerData.ObjectType) -> None:
        ...
    def Reposition(self, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def RepositionByOrigin(self, origin: Point3d) -> None:
        ...
    def ReorientByCoordinateSystem(self, matrix: Matrix3x3) -> None:
        ...
    def ReorientByDirection(self, objectType: GeometricUtilities.TransformerData.ObjectType, direction: Vector3d) -> None:
        ...
    def RepositionByPlane(self, objectType: GeometricUtilities.TransformerData.ObjectType, planeOrigin: Point3d, planeNormal: Vector3d) -> None:
        ...
    def AlignToWorkCoordinateSystem(self) -> None:
        ...
    def AlignToAbsoluteCoordinateSystem(self) -> None:
        ...
    def SetTransformationObject(self, objectType: GeometricUtilities.TransformerData.ObjectType) -> None:
        ...
    def Validate(self) -> bool:
        ...


    class ObjectType(enum.Enum):
        None = 0
        Origin = 1
        TranslationX = 2
        TranslationY = 3
        TranslationZ = 4
        RotationXY = 5
        RotationYZ = 6
        RotationXZ = 7
        ScaleX = 8
        ScaleY = 9
        ScaleZ = 10
        DirectionX = 11
        DirectionY = 12
        DirectionZ = 13
        PlaneXY = 14
        PlaneYZ = 15
        PlaneXZ = 16
        ArcXY = 17
        ArcYZ = 18
        ArcXZ = 19
    

class TangentMagnitudeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndTangentMagnitude: Expression
    StartTangentMagnitude: Expression


class SurfaceType(enum.Enum):
    Rubber = 0
    Planar = 1
    Cylindrical = 2
    Conical = 3
    Spherical = 4
    Toroidal = 5
    Parametric = 6
    Blending = 7
    Offset = 8
    Swept = 9
    Convergent = 10
    Undefined = 50


class SurfaceRangeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AnchorPosition: GeometricUtilities.SurfaceRangeBuilder.AnchorPositionType
    UEnd: GeometricUtilities.OnPathDimensionBuilder
    UStart: GeometricUtilities.OnPathDimensionBuilder
    VEnd: GeometricUtilities.OnPathDimensionBuilder
    VStart: GeometricUtilities.OnPathDimensionBuilder


    class AnchorPositionType(enum.Enum):
        Center = 0
        Vertex1 = 1
        Vertex2 = 2
        Vertex3 = 3
        Vertex4 = 4
    

class SupportPlaneData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ExistingPlane: DisplayableObject
    SupportPlane: Plane
    SupportPlaneLockStatus: GeometricUtilities.SupportPlaneData.LockPlaneStatus
    WorkView: View


    class LockPlaneStatus(enum.Enum):
        No = 0
        AfterFirstConstraint = 1
        AfterSecondConstraint = 2
        AfterThirdConstraint = 3
        AfterFirstAndSecondConstraint = 4
        AfterFirstAndThirdConstraint = 5
        AfterSecondAndThirdConstraint = 6
        AfterAllConstraint = 7
        LockExistingPlane = 8
        CenterPointDirection = 9
    

class StyledSweepReferenceMethodBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateOnReferenceVectorReversal(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    HasHingeVector: bool
    ReferenceCurve: Section
    ReferenceOption: GeometricUtilities.StyledSweepReferenceMethodBuilder.ReferenceOptions
    ReferenceVector: Direction


    class ReferenceOptions(enum.Enum):
        ToGuide = 0
        ToCurve = 1
        ToVector = 2
    

class StyledSweepDoubleOnPathDimBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.StyledSweepDoubleOnPathDimBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.StyledSweepDoubleOnPathDimBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.StyledSweepDoubleOnPathDimBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.StyledSweepDoubleOnPathDimBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.StyledSweepDoubleOnPathDimBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.StyledSweepDoubleOnPathDimBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.StyledSweepDoubleOnPathDimBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.StyledSweepDoubleOnPathDimBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.StyledSweepDoubleOnPathDimBuilder, object2: GeometricUtilities.StyledSweepDoubleOnPathDimBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.StyledSweepDoubleOnPathDimBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class StyledSweepDoubleOnPathDimBuilder(NXObject):
    def __init__(self) -> None: ...
    def ResetExtraData(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    FirstLocation: GeometricUtilities.OnPathDimensionBuilder
    SecondLocation: GeometricUtilities.OnPathDimensionBuilder


class StrokeGestureData(TaggedObject):
    def __init__(self) -> None: ...
    def AddPoint(self, point: GeometricUtilities.StrokeGestureData.Point) -> None:
        ...
    def GetPoints(self) -> typing.List[GeometricUtilities.StrokeGestureData.Point]:
        ...
    def Clear(self) -> None:
        ...
    def SetDrawingPlane(self, matrix: Matrix3x3) -> None:
        ...
    def Validate(self) -> bool:
        ...
    DrawingScale: float


    class StrokeGestureDataPoint():
        Position: Point3d
        Speed: float
        def ToString(self) -> str:
            ...
        def __init__(self, Position: Point3d, Speed: float) -> None: ...
    

class StepOptionBehavior(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    StepOption: GeometricUtilities.StepOptionBehavior.StepOptionType


    class StepOptionType(enum.Enum):
        None = 0
        ExtendNeighborsatSmoothEdge = 1
    

class StartHoleData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BooleanOperation: GeometricUtilities.BooleanOperation
    CounterboreDepth: Expression
    CounterboreDiameter: Expression
    CountersinkAngle: Expression
    CountersinkDiameter: Expression
    EndChamferAngle: Expression
    EndChamferEnabled: bool
    EndChamferOffset: Expression
    FitOption: str
    HoleDiameter: Expression
    HoleForm: GeometricUtilities.StartHoleData.HoleForms
    NeckChamferAngle: Expression
    NeckChamferEnabled: bool
    NeckChamferOffset: Expression
    ReliefDepth: Expression
    ReliefEnabled: bool
    ScrewSize: str
    ScrewType: str
    StartChamferAngle: Expression
    StartChamferEnabled: bool
    StartChamferOffset: Expression


    class HoleForms(enum.Enum):
        Simple = 0
        Counterbored = 1
        Countersink = 2
    

class SShapedLawBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateSpine(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    EndNode: GeometricUtilities.OnPathDimWithValueBuilder
    SlopeNode: GeometricUtilities.OnPathDimWithValueBuilder
    Spine: Section
    StartNode: GeometricUtilities.OnPathDimWithValueBuilder


class SplineExtensionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndExtensionOption: GeometricUtilities.SplineExtensionBuilder.ExtensionOption
    EndPoint: Point
    EndValue: Expression
    IsSymmetric: bool
    StartExtensionOption: GeometricUtilities.SplineExtensionBuilder.ExtensionOption
    StartPoint: Point
    StartValue: Expression


    class ExtensionOption(enum.Enum):
        None = 0
        ByValue = 1
        ByPoint = 2
    

class SpiralPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DirectionType: GeometricUtilities.SpiralPattern.OrientType
    HorizontalRef: GeometricUtilities.HorizontalReference
    NumberOfTurns: Expression
    PitchAlongSpiral: GeometricUtilities.OnPathDistancePatternSpacing
    RadialPitch: Expression
    SizeSpiralType: GeometricUtilities.SpiralPattern.SpiralDefineSize
    SpiralNormal: Direction
    TotalAngle: Expression


    class SpiralDefineSize(enum.Enum):
        NumberOfTurns = 0
        TotalAngle = 1
    

    class OrientType(enum.Enum):
        Lefthand = 0
        Righthand = 1
    

class SpinePointDataCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricUtilities.SpinePointData]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateSpinePointData(self, lawValue: float, parameter: float, parent: Section) -> GeometricUtilities.SpinePointData:
        ...
    def CreateSpinePointData(self, lawValueExpression: Expression, parameter: float, parent: Section) -> GeometricUtilities.SpinePointData:
        ...
    def Tag(self) -> Tag: ...



class SpinePointData(TaggedObject):
    def __init__(self) -> None: ...
    def GetLawValueAtPoint(self) -> Expression:
        ...
    def SetLawValueAtPoint(self, valString: str) -> None:
        ...
    def GetParentSpine(self) -> Section:
        ...
    def SetParentSpine(self, parent: Section) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ParameterLength: float
    ParameterPercent: float


    class ParameterType(enum.Enum):
        Normal = 0
        Percent = 1
        Length = 2
    

class SpinePlaneBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.SpinePlaneBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.SpinePlaneBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.SpinePlaneBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.SpinePlaneBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.SpinePlaneBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.SpinePlaneBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.SpinePlaneBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.SpinePlaneBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.SpinePlaneBuilder, object2: GeometricUtilities.SpinePlaneBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.SpinePlaneBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SpinePlaneBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AlternateSolution(self) -> None:
        ...
    Plane: Plane


class SpineDefinitionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Method: GeometricUtilities.SpineDefinitionBuilder.MethodOptions
    Section: Section
    Vector: Direction


    class MethodOptions(enum.Enum):
        None = 0
        Curve = 1
        Vector = 2
    

class SnipIntoPatchesBuilder(Builder):
    def __init__(self) -> None: ...
    def SnipSurfaceIntoPatches(self, targetFace: Face) -> None:
        ...
    def CreateRegionsPreview(self, targetFace: Face, allCurves: typing.List[Curve]) -> None:
        ...
    def DeleteInternalPatch(self, targetFace: Face, allCurves: typing.List[Curve]) -> None:
        ...
    def GetExtractFace(self) -> Face:
        ...
    def GetIsoCurves(self, targetFace: Face, allCurves: typing.List[Curve]) -> None:
        ...
    def DeleteExtractFace(self, extractFace: Face) -> None:
        ...
    def DeleteIsoCurve(self, allCurves: typing.List[Curve]) -> None:
        ...
    Face: SelectFace
    HideOriginal: bool
    Region: RegionPointList


class SmartVolumeProfileBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CloseProfileRule: GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType
    OpenProfileSmartVolumeOption: bool


    class CloseProfileRuleType(enum.Enum):
        Fci = 0
        Lci = 1
        Cci = 2
    

class SimpleDraft(TaggedObject):
    def __init__(self) -> None: ...
    def SetDraftAngle(self, draftAngle: str) -> None:
        """[Obsolete("Deprecated in NX5.0.0.  To set the value of the expression modify the expression directly using GeometricUtilities.SimpleDraft.DraftAngle and Expression.RightHandSide.")"""
        ...
    def Validate(self) -> bool:
        ...
    DraftAngle: Expression
    DraftType: GeometricUtilities.SimpleDraft.SimpleDraftType


    class SimpleDraftType(enum.Enum):
        NoDraft = 0
        SimpleFromStart = 1
        SimpleFromProfile = 2
        Symmetric = 3
        MatchedEnds = 4
        Asymmetric = 5
    

class ShapeFrameBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetVertexCoords(self, index: int) -> Point2d:
        ...
    def SetVertexCoords(self, index: int, coords: Point2d) -> None:
        ...
    def GetMidpointCoords(self, index: int) -> Point2d:
        ...
    def SetMidpointCoords(self, index: int, coords: Point2d) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Anchor: GeometricUtilities.AnchorLocatorBuilder
    AnchorAttachment: GeometricUtilities.ShapeFrameBuilder.AnchorAttachmentType
    NumberVertices: int


    class AnchorAttachmentType(enum.Enum):
        None = 0
        Center = 1
        Vertex1 = 2
        Vertex2 = 3
        Vertex3 = 4
        Vertex4 = 5
    

class SelectionListList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.SelectionList]) -> None:
        ...
    def Append(self, object: GeometricUtilities.SelectionList) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.SelectionList) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.SelectionList:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.SelectionList) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.SelectionList, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.SelectionList]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.SelectionList]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.SelectionList, object2: GeometricUtilities.SelectionList) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.SelectionList) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SelectionList(NXObject):
    def __init__(self) -> None: ...
    SelectObjectList: SelectDisplayableObjectList


class SelectDividingObjectBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ConstraintManager: Features.GeometricConstraintDataManager
    CurvesToOffset: Section
    DividingObjectsList: SelectDisplayableObjectList
    EndPoint: Point
    IsoparametricDirection: GeometricUtilities.SelectDividingObjectBuilder.IsoparametricDirectionType
    OffsetDirection: bool
    OffsetDistance: Expression
    StartPoint: Point
    ToolOption: GeometricUtilities.SelectDividingObjectBuilder.ToolType


    class ToolType(enum.Enum):
        Object = 0
        LineByTwoPoints = 1
        OffsetCurveInFace = 2
        IsoparametricCurve = 3
    

    class IsoparametricDirectionType(enum.Enum):
        U = 0
        V = 1
    

class SectionPlaneData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    PlaneNormal: Direction
    PlaneOrigin: Point
    PlanePoint1: Point
    PlanePoint2: Point


class SecondarySectionData(NXObject):
    def __init__(self) -> None: ...
    def GetSecondarySectionValues(self) -> str:
        ...
    def SetSecondarySectionValues(self, expressions: str) -> None:
        ...
    def GetMasterExpressionValues(self) -> typing.List[Expression]:
        ...
    def SetMasterExpressionValues(self, expressions: typing.List[Expression]) -> None:
        ...
    def SetPathLocation(self, pathLocationPercent: float) -> None:
        ...
    def Destroy(self) -> None:
        ...
    def SetMasterSection(self, masterSection: Section) -> None:
        ...
    def CreateSketch(self, pathLocation: float) -> None:
        ...
    def DeleteSketch(self) -> None:
        ...
    IsEndSection: bool
    IsStartSection: bool
    OnPathDimData: GeometricUtilities.Extend


class ScalingSetBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.ScalingSetBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.ScalingSetBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.ScalingSetBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.ScalingSetBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ScalingSetBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ScalingSetBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.ScalingSetBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.ScalingSetBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.ScalingSetBuilder, object2: GeometricUtilities.ScalingSetBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.ScalingSetBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ScalingSetBuilder(GeometricUtilities.OnPathDimWithValueBuilder):
    def __init__(self) -> None: ...
    ScalingValue: Expression


class ScalingMethodBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AreaLaw: GeometricUtilities.LawBuilder
    BlendingFunctionType: GeometricUtilities.ScalingMethodBuilder.BlendingFunctionTypes
    EndBlendScaleFactor: float
    PerimeterLaw: GeometricUtilities.LawBuilder
    ScaleFactor: float
    ScalingCurve: Section
    ScalingOption: GeometricUtilities.ScalingMethodBuilder.ScalingOptions
    ScalingPoint: Point
    StartBlendScaleFactor: float


    class ScalingOptions(enum.Enum):
        Constant = 0
        ByBlendingFunction = 1
        ByAnotherCurve = 2
        ByAPoint = 3
        ByAreaLaw = 4
        ByPerimeterLaw = 5
        Uniform = 6
        Lateral = 7
    

    class BlendingFunctionTypes(enum.Enum):
        Linear = 0
        Cubic = 1
    

class SaveConstraintsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SaveConstraints: bool


class RotationSetBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.RotationSetBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.RotationSetBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.RotationSetBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.RotationSetBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.RotationSetBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.RotationSetBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.RotationSetBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.RotationSetBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.RotationSetBuilder, object2: GeometricUtilities.RotationSetBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.RotationSetBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class RotationSetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def ResetExtraData(self) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Location: GeometricUtilities.OnPathDimensionBuilder
    Value: Expression
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


class RodItemListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateRodItemBuilder(self) -> GeometricUtilities.RodItemBuilder:
        ...
    def Validate(self) -> bool:
        ...
    RodItemList: GeometricUtilities.RodItemBuilderList


class RodItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.RodItemBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.RodItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.RodItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.RodItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.RodItemBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.RodItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.RodItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.RodItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.RodItemBuilder, object2: GeometricUtilities.RodItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.RodItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class RodItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Destroy(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    EndPoint: Point
    GraphEdge: Section
    Method: GeometricUtilities.RodItemBuilder.CurveCreateType
    NumberOfSegments: int
    StartPoint: Point


    class CurveCreateType(enum.Enum):
        ByPoints = 0
        ExistingCurves = 1
    

class ReplAsstBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Enter(self) -> None:
        ...
    def Exit(self) -> None:
        ...
    def CreateEmptyMatch(self) -> GeometricUtilities.ParentEquivalencyMap:
        ...
    def QueryFeatureOutputUsage(self) -> int:
        ...
    def CreateNameBasedMaps(self, maps: typing.List[GeometricUtilities.ParentEquivalencyMap]) -> None:
        ...
    def CreateInferredMaps(self, maps: typing.List[GeometricUtilities.ParentEquivalencyMap]) -> None:
        ...
    def CreateGeometricMaps(self, maps: typing.List[GeometricUtilities.ParentEquivalencyMap]) -> None:
        ...
    def SetNewParents(self, replacementObjects: typing.List[DisplayableObject]) -> None:
        ...
    def SetProdInt(self, prodInt: TaggedObject) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Allowance: float
    MatchList: GeometricUtilities.ParentEquivalencyMapList
    MatchObjectsWithDependentsOnly: bool
    MatchSheetBoundariesOnly: bool
    OneToOne: bool
    UsageInfoList: GeometricUtilities.EntityUsageInfoList


class ReplaceMatchListItemList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.ReplaceMatchListItem]) -> None:
        ...
    def Append(self, object: GeometricUtilities.ReplaceMatchListItem) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.ReplaceMatchListItem) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.ReplaceMatchListItem:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ReplaceMatchListItem) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ReplaceMatchListItem, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.ReplaceMatchListItem]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.ReplaceMatchListItem]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.ReplaceMatchListItem, object2: GeometricUtilities.ReplaceMatchListItem) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.ReplaceMatchListItem) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ReplaceMatchListItem(Builder):
    def __init__(self) -> None: ...


class ReplaceManualMatchBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateReplaceMatchListItem(self, parentEntity: TaggedObject, parentFrec: TaggedObject) -> GeometricUtilities.ReplaceMatchListItem:
        ...
    ReplaceMatchList: GeometricUtilities.ReplaceMatchListItemList


class RenewFeatureBuilder(Builder):
    def __init__(self) -> None: ...
    FeatureList: Features.FeatureList


class RenameLinkedPartModulePartBuilder(Builder):
    def __init__(self) -> None: ...
    def SetLinkedPartNameToBeSavedAs(self, linkedPartTag: Part, fileName: str) -> None:
        ...
    def GetLinkedPartNameToBeSavedAs(self, linkedPartTag: Part) -> str:
        ...
    def SetLinkedPartNameToBeSavedAs(self, linkedPartTag: typing.List[Part], fileName: str) -> None:
        ...
    def GetLinkedPartNameToBeSavedAs(self, fileName: str) -> None:
        ...
    def GetAllAssociatedLinkedPartModulePartTags(self, mainPartTag: Part, linkedPartTags: typing.List[Part]) -> None:
        ...


class RegionTracker(TaggedObject):
    def __init__(self) -> None: ...
    def GetFaceSelectors(self, entities: typing.List[Face]) -> None:
        ...
    def SetFaceSelectors(self, entities: typing.List[Face]) -> None:
        ...
    def SetOneFaceSelector(self, entity: Face) -> None:
        ...
    def GetEdgeSelectors(self, entities: typing.List[Face]) -> None:
        ...
    def SetEdgeSelectors(self, entities: typing.List[Edge]) -> None:
        ...
    def SetOneEdgeSelector(self, entity: Edge) -> None:
        ...
    def GetVertexSelectors(self, entities: typing.List[Edge], extremities: typing.List[GeometricUtilities.RegionTracker.ExtremityType]) -> None:
        ...
    def SetOneVertexSelector(self, entity: Edge, extremity: GeometricUtilities.RegionTracker.ExtremityType) -> None:
        ...
    def SetVertexSelectors(self, entities: typing.List[Edge], extremities: typing.List[GeometricUtilities.RegionTracker.ExtremityType]) -> None:
        ...
    def SetOnePointSelector(self, location: Point3d) -> None:
        ...
    def GetOwningBody(self) -> Body:
        ...
    def SetOwningBody(self, owningBodyEid: Body) -> None:
        ...
    def AppendOneBoundaryBody(self, boundaryBodyEid: Body, sideness: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    OnTool: bool


    class ExtremityType(enum.Enum):
        Start = 0
        End = 1
    

class RefitControlBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DegreesAndSegmentsOrPatches: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    RefitDirection: GeometricUtilities.RefitControlBuilder.RefitControlDirection
    RefitMethod: GeometricUtilities.RefitControlBuilder.RefitControlMethod
    Tolerance: float


    class RefitControlMethod(enum.Enum):
        KeepParameterization = 0
        DegreePatches = 1
        DegreeTolerance = 2
        PatchTolerance = 3
    

    class RefitControlDirection(enum.Enum):
        UV = 0
        U = 1
        V = 2
    

class ReferencePattern(TaggedObject):
    def __init__(self) -> None: ...
    def SetBaseInstance(self, firstIndex: int, secondIndex: int) -> None:
        ...
    def ResetBaseInstance(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ReferencedPattern: SelectNXObject


class ReduceSurfaceRadiusFaceGroupBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder, object2: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ReduceSurfaceRadiusFaceGroupBuilder(Builder):
    def __init__(self) -> None: ...
    EndLimit: GeometricUtilities.OnPathDimensionBuilder
    SelectFace: ScCollector
    StartLimit: GeometricUtilities.OnPathDimensionBuilder


class ReduceSurfaceRadiusBuilder(Builder):
    def __init__(self) -> None: ...
    Direction: bool
    FaceGroupList: GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilderList
    HighRadius: float
    IndexListItem: int
    LowRadius: float
    OnPathDimEnd: GeometricUtilities.OnPathDimensionBuilder
    OnPathDimStart: GeometricUtilities.OnPathDimensionBuilder
    PercentReduction: float
    PositionTolerance: float
    ReduceValueType: GeometricUtilities.ReduceSurfaceRadiusBuilder.ReduceValueTypeSpecification
    ReducedFaceType: GeometricUtilities.ReduceSurfaceRadiusBuilder.ReducedFaceTypeSpecification
    SelectChain: ScCollector
    SelectFace: ScCollector
    TangentTolerance: float
    TargetReduction: float
    ValueReduction: float


    class ReduceValueTypeSpecification(enum.Enum):
        Percentage = 0
        Value = 1
        Delta = 2
    

    class ReducedFaceTypeSpecification(enum.Enum):
        FaceGroup = 0
        SingleChainInGroup = 1
        SingleChain = 2
    

    class FaceSelectionSpecification(enum.Enum):
        Radius = 0
        Chain = 1
        Select = 2
    

class RectangularPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateLastStaggered: bool
    HorizontalRef: GeometricUtilities.HorizontalReference
    SimplifiedLayoutType: GeometricUtilities.RectangularPattern.SimplifiedLayoutTypes
    StaggerType: GeometricUtilities.RectangularPattern.StaggerOptions
    UseYDirectionToggle: bool
    XDirection: Direction
    XFlip: bool
    XSelection: SelectNXObject
    XSpacing: GeometricUtilities.DistancePatternSpacing
    XSymmetryToggle: bool
    YDirection: Direction
    YFlip: bool
    YSelection: SelectNXObject
    YSpacing: GeometricUtilities.DistancePatternSpacing
    YSymmetryToggle: bool


    class StaggerOptions(enum.Enum):
        None = 0
        Row = 1
        Column = 2
    

    class SimplifiedLayoutTypes(enum.Enum):
        Square = 0
        Triangle = 1
        Diamond = 2
    

class RectangularFrameBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateOnCoordinateSystem(self) -> None:
        ...
    def EditCoordinateSystem(self, origin: Point, csys: Matrix3x3) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AnchorLocation: GeometricUtilities.RectangularFrameBuilder.AnchorLocationType
    AnchorLocator: SelectSmartObject
    CoordinateSystem: CoordinateSystem
    Height: Expression
    Length: Expression
    Shear: Expression
    WScale: float


    class AnchorLocationType(enum.Enum):
        TopLeft = 0
        TopCenter = 1
        TopRight = 2
        MiddleLeft = 3
        MiddleCenter = 4
        MiddleRight = 5
        BottomLeft = 6
        BottomCenter = 7
        BottomRight = 8
    

class Rebuild(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Degree: int
    DegreeType: GeometricUtilities.Rebuild.DegreeTypes
    ManualDegree: int
    MaximumDegree: int
    MaximumSegments: int
    RebuildType: GeometricUtilities.Rebuild.RebuildTypes


    class RebuildTypes(enum.Enum):
        None = 0
        Manual = 1
        Advanced = 2
        KeepParameterization = 3
    

    class DegreeTypes(enum.Enum):
        Cubic = 0
        Quintic = 1
    

class RadiusMethod(enum.Enum):
    Constant = 0
    Law = 1
    Tangency = 2


class QuadrilateralFrameBuilder(GeometricUtilities.ShapeFrameBuilder):
    def __init__(self) -> None: ...
    Subtype: GeometricUtilities.QuadrilateralFrameBuilder.Subtypes


    class Subtypes(enum.Enum):
        Arbitrary = 0
        Parallelogram = 1
        Rectangle = 2
        Square = 3
    

class ProjectionOptions(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ProjectDirectionMethod: GeometricUtilities.ProjectionOptions.DirectionType
    ProjectVector: Direction


    class DirectionType(enum.Enum):
        FaceNormal = 0
        CrvPlaneNormal = 1
        Vector = 2
    

class PolygonPatternSpacing(GeometricUtilities.PatternSpacing):
    def __init__(self) -> None: ...
    PitchDistance: Expression
    SpanAngle: Expression


class PolygonPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Flip: bool
    HorizontalRef: GeometricUtilities.HorizontalReference
    NumberOfSides: Expression
    PolygonSizeOption: GeometricUtilities.PolygonPattern.SizeOptions
    PolygonSpacing: GeometricUtilities.PolygonPatternSpacing
    RadialSpacing: GeometricUtilities.DistancePatternSpacing
    RotationAxis: Axis
    RotationCenter: Point
    UseRadialDirectionToggle: bool


    class SizeOptions(enum.Enum):
        Inscribed = 0
        Circumscribed = 1
    

class PointsFromFileBuilder(Builder):
    def __init__(self) -> None: ...
    CoordinateOption: GeometricUtilities.PointsFromFileBuilder.Options
    FileName: str
    PathName: str


    class Options(enum.Enum):
        Absolute = 0
        Wcs = 1
    

class PointSetAlignmentBuilder(Builder):
    def __init__(self) -> None: ...
    Constraint: GeometricUtilities.PointSetAlignmentBuilder.ConstraintOptions
    FromPointSet: SelectPointList
    ObjectsToMove: SelectDisplayableObjectList
    ToPointSet: SelectPointList


    class ConstraintOptions(enum.Enum):
        None = 0
        X = 1
        Y = 2
        Z = 3
    

class PointFacePlaneSelectionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.PointFacePlaneSelectionBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.PointFacePlaneSelectionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.PointFacePlaneSelectionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.PointFacePlaneSelectionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.PointFacePlaneSelectionBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.PointFacePlaneSelectionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.PointFacePlaneSelectionBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.PointFacePlaneSelectionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.PointFacePlaneSelectionBuilder, object2: GeometricUtilities.PointFacePlaneSelectionBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.PointFacePlaneSelectionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PointFacePlaneSelectionBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateLengthLimitPointBuilder(self, mOnPathExp: Expression, mOnPath: GeometricUtilities.OnPathDimensionBuilder, mIsFlipped: bool, mThruPoint: Point) -> GeometricUtilities.LengthLimitPointBuilder:
        ...
    IsOk: bool
    LengthLimitPoint: GeometricUtilities.LengthLimitPointBuilder
    LimitTopolSwitchFinFlag: bool
    PlaneHelpPoint: Point
    SelectEdge: ScCollector
    SelectFace: GeometricUtilities.FaceSetData
    SelectPlane: Plane
    TrimObject: GeometricUtilities.PointFacePlaneSelectionBuilder.TrimObjectType
    UseFaceCapBlend: bool
    UsePlaneCapBlend: bool


    class TrimObjectType(enum.Enum):
        Point = 0
        Plane = 1
        Face = 2
        Edge = 3
    

class PlayButtonsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Stop(self) -> None:
        ...
    def RewindToStart(self) -> None:
        ...
    def StepBackward(self) -> None:
        ...
    def PlayBackward(self) -> None:
        ...
    def PlayForward(self) -> None:
        ...
    def StepForward(self) -> None:
        ...
    def ForwardToEnd(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CurrentStep: int
    PlayModes: GeometricUtilities.PlayButtonsBuilder.PlayModeValues
    ScaleSpeed: float
    ScaleStep: float
    Speed: float


    class PlayModeValues(enum.Enum):
        PlayOnce = 0
        LoopOver = 1
        Retrace = 2
    

class PatternSpacingsListItemList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.PatternSpacingsListItem]) -> None:
        ...
    def Append(self, object: GeometricUtilities.PatternSpacingsListItem) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.PatternSpacingsListItem) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.PatternSpacingsListItem:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.PatternSpacingsListItem) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.PatternSpacingsListItem, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.PatternSpacingsListItem]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.PatternSpacingsListItem]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.PatternSpacingsListItem, object2: GeometricUtilities.PatternSpacingsListItem) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.PatternSpacingsListItem) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PatternSpacingsListItem(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SpacingExpression: Expression
    SpacingOnPath: GeometricUtilities.OnPathDimensionBuilder


class PatternSpacingsList(TaggedObject):
    def __init__(self) -> None: ...
    def CreatePatternSpacingsListItem(self) -> GeometricUtilities.PatternSpacingsListItem:
        ...
    def Validate(self) -> bool:
        ...
    List: GeometricUtilities.PatternSpacingsListItemList


class PatternSpacing(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    NCopies: Expression
    SpaceType: GeometricUtilities.PatternSpacing.SpacingType
    SpacingsList: GeometricUtilities.PatternSpacingsList


    class SpacingType(enum.Enum):
        Offset = 0
        Span = 1
        PitchAndSpan = 2
        Pitch = 3
        List = 4
        PolygonCountPerSide = 5
        PolygonPitchAlongSide = 6
    

class PatternReferencePointServiceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    IsReferencePointInferred: bool
    Point: Point


class PatternOrientation(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlongOrientationOption: GeometricUtilities.PatternOrientation.Enum
    AlongPathRotationAngle: Expression
    CircularOrientationOption: GeometricUtilities.PatternOrientation.Enum
    FollowFaceProjDirOption: GeometricUtilities.PatternOrientation.ProjDirEnum
    FollowFaceSelection: ScCollector
    FollowFaceToggle: bool
    FromCSYS: CoordinateSystem
    GeneralOrientationOption: GeometricUtilities.PatternOrientation.Enum
    HelixOrientationOption: GeometricUtilities.PatternOrientation.Enum
    LinearOrientationOption: GeometricUtilities.PatternOrientation.Enum
    MirrorOrientationOption: GeometricUtilities.PatternOrientation.Enum
    OrientationOption: GeometricUtilities.PatternOrientation.Enum
    PolygonOrientationOption: GeometricUtilities.PatternOrientation.Enum
    RepeatTransformSetting: bool
    SpiralOrientationOption: GeometricUtilities.PatternOrientation.Enum
    ToCSYS: CoordinateSystem
    UserDefinedProjDir: Direction
    VectorForAlong: Direction


    class ProjDirEnum(enum.Enum):
        PatternPlaneNormal = 0
        NormalToFace = 1
        RadialDir = 2
        UserDefinedVector = 3
    

    class Enum(enum.Enum):
        Fixed = 0
        NormalToPath = 1
        NormalToVector = 2
        ParallelToVector = 3
        ThroughAxis = 4
        FollowPattern = 5
        FollowCSYS = 6
        CSYStoCSYS = 7
    

class PatternInstanceEditBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSelectedInstances(self, firstIndexOfSelectedInstances: int, secondIndexOfSelectedInstances: int) -> None:
        ...
    EditedExpressionsList: GeometricUtilities.InstanceEditedExpressionsList


class PatternIncrementsList(TaggedObject):
    def __init__(self) -> None: ...
    def CreatePatternIncrementItem(self) -> GeometricUtilities.PatternIncrementItem:
        ...
    def CreatePatternIncrementItem(self, masterExpression: Expression) -> GeometricUtilities.PatternIncrementItem:
        ...
    def Validate(self) -> bool:
        ...
    List: GeometricUtilities.PatternIncrementItemList


class PatternIncrementsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    IncrementsListInDirection1: GeometricUtilities.PatternIncrementsList
    IncrementsListInDirection2: GeometricUtilities.PatternIncrementsList


class PatternIncrementItemList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.PatternIncrementItem]) -> None:
        ...
    def Append(self, object: GeometricUtilities.PatternIncrementItem) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.PatternIncrementItem) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.PatternIncrementItem:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.PatternIncrementItem) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.PatternIncrementItem, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.PatternIncrementItem]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.PatternIncrementItem]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.PatternIncrementItem, object2: GeometricUtilities.PatternIncrementItem) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.PatternIncrementItem) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PatternIncrementItem(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    IncrementExpression: Expression
    MasterExpression: Expression
    Operation: GeometricUtilities.PatternIncrementItem.OperationEnum


    class OperationEnum(enum.Enum):
        Add = 0
        Multiply = 1
    

class PatternFill(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ApplyMarginToInnerBoundToggle: bool
    FaceBoundary: Section
    FillBoundary: Section
    FillMargin: Expression
    FillOptions: GeometricUtilities.PatternFill.PatternFillOptions
    InternalBoundary: Section
    SimplifiedBoundaryToggle: bool


    class PatternFillOptions(enum.Enum):
        None = 0
        FillbyFace = 1
        FillbyBoundary = 2
        ExcludeAreaOnly = 3
    

class PatternDefinition(TaggedObject):
    def __init__(self) -> None: ...
    def CreatePatternInstanceEditBuilder(self) -> GeometricUtilities.PatternInstanceEditBuilder:
        ...
    def GetSuppressState(self, index1: int, index2: int) -> bool:
        ...
    def SetSuppressState(self, index1: int, index2: int, suppressState: bool) -> None:
        ...
    def GetDeleteState(self, index1: int, index2: int) -> bool:
        ...
    def SetDeleteState(self, index1: int, index2: int, deleteState: bool) -> None:
        ...
    def CreateClockingBuilder(self, ix: int, iy: int) -> GeometricUtilities.PatternClockingBuilder:
        ...
    def GetClocking(self, index1: int, index2: int) -> GeometricUtilities.PatternClocking:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.GeometricUtilities.PatternDefinition.CreateClockingBuilder instead.")"""
        ...
    def RemoveClocking(self, index1: int, index2: int) -> None:
        ...
    def RemoveVariance(self, index1: int, index2: int) -> None:
        ...
    def SetSpreadsheetData(self, spreadsheetTableArray: float, locationTableArray: float, defaultTableArray: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AlongPathDefinition: GeometricUtilities.AlongPathPattern
    CircularDefinition: GeometricUtilities.CircularPattern
    FrameOnlyToggle: bool
    GeneralDefinition: GeometricUtilities.GeneralPattern
    HelixDefinition: GeometricUtilities.HelixPattern
    MirrorDefinition: GeometricUtilities.MirrorPattern
    PatternFill: GeometricUtilities.PatternFill
    PatternIncrementsBuilder: GeometricUtilities.PatternIncrementsBuilder
    PatternOrientation: GeometricUtilities.PatternOrientation
    PatternType: GeometricUtilities.PatternDefinition.PatternEnum
    PolygonDefinition: GeometricUtilities.PolygonPattern
    RectangularDefinition: GeometricUtilities.RectangularPattern
    ReferenceDefinition: GeometricUtilities.ReferencePattern
    SeedOnlyToggle: bool
    SpiralDefinition: GeometricUtilities.SpiralPattern


    class PatternEnum(enum.Enum):
        Linear = 0
        Circular = 1
        Polygon = 2
        Spiral = 3
        AlongPath = 4
        General = 5
        Reference = 6
        Mirror = 7
        Helix = 8
    

class PatternClockingBuilder(Builder):
    def __init__(self) -> None: ...
    def AddInstance(self, index1: int, index2: int) -> None:
        ...
    def RemoveInstance(self, index1: int, index2: int) -> None:
        ...
    AngularDelta: Expression
    ClockType: GeometricUtilities.PatternClockingBuilder.ClockingType
    Direction1Delta: Expression
    Direction2Delta: Expression
    Motion: GeometricUtilities.ModlMotion
    RadialDelta: Expression


    class ClockingType(enum.Enum):
        WithinPatternDefinitionLinear = 0
        WithinPatternDefinitionCircular = 1
        UserDefined = 2
    

class PatternClocking(TaggedObject):
    def __init__(self) -> None: ...
    def SetXDirectionDelta(self, direction1Exp: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  This functionality is no longer supported.")"""
        ...
    def SetYDirectionDelta(self, direction2Exp: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  This functionality is no longer supported.")"""
        ...
    def SetAngularDelta(self, angularDeltaExp: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  This functionality is no longer supported.")"""
        ...
    def SetRadialDelta(self, radialDelta: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  This functionality is no longer supported.")"""
        ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX8.0.0.  This functionality is no longer supported..")"""
        ...
    AngularDelta: Expression
    ClockType: GeometricUtilities.PatternClocking.ClockingType
    Direction1Delta: Expression
    Direction2Delta: Expression
    RadialDelta: Expression


    class ClockingType(enum.Enum):
        WithinPatternDefinitionLinear = 0
        WithinPatternDefinitionCircular = 1
    

class PathLimits(GeometricUtilities.Limits):
    def __init__(self) -> None: ...


class PartModuleRelationshipBuilder(Builder):
    def __init__(self) -> None: ...
    LinkedPartModule: Features.SelectPartModule
    PartModule: Features.SelectPartModule


class PartModuleReferencesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ExpressionList: SelectExpressionList
    GeometryList: GeometricUtilities.SelectionListList


class PartModuleOutputBuilder1(Builder):
    def __init__(self) -> None: ...
    OutputReferences1: Features.PartGeometryCopyBuilder


class PartModuleOutputBuilder(Builder):
    def __init__(self) -> None: ...
    Activate: bool
    Deactivate: bool
    OutputReferences: GeometricUtilities.PartModuleReferencesBuilder


class PartModuleInputBuilder(Builder):
    def __init__(self) -> None: ...
    DefineSharedBodyInput: bool
    InputReferences: Features.PartGeometryCopyBuilder
    ModifiableGeometry: ScCollectorList
    ModifiableGeometryOption: GeometricUtilities.PartModuleInputBuilder.ModifiableGeometryOptions
    SharedBodyInput: Features.PartGeometryCopyBuilder


    class ModifiableGeometryOptions(enum.Enum):
        WholeBody = 0
        Selected = 1
    

class ParentEquivalencyMapList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.ParentEquivalencyMap]) -> None:
        ...
    def Append(self, object: GeometricUtilities.ParentEquivalencyMap) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.ParentEquivalencyMap) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.ParentEquivalencyMap:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ParentEquivalencyMap) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ParentEquivalencyMap, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.ParentEquivalencyMap]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.ParentEquivalencyMap]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.ParentEquivalencyMap, object2: GeometricUtilities.ParentEquivalencyMap) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.ParentEquivalencyMap) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ParentEquivalencyMap(TaggedObject):
    def __init__(self) -> None: ...
    def GetEntitiesFromCurrentObject(self, entitiesFromCurrentObject: typing.List[DisplayableObject]) -> None:
        ...
    def GetEntitiesFromReplacementObject(self, entitiesFromReplacementObject: typing.List[DisplayableObject]) -> None:
        ...
    def SetMappedEntities(self, oldEntities: typing.List[DisplayableObject], newEntities: typing.List[DisplayableObject]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    MapStatus: GeometricUtilities.ParentEquivalencyMap.Status
    MapType: GeometricUtilities.ParentEquivalencyMap.Type


    class Type(enum.Enum):
        Undefined = 0
        UserDefined = 1
        NameBased = 2
        Geometric = 3
        Inferred = 4
        Internal = 5
        Inherited = 6
        Mixed = 7
    

    class Status(enum.Enum):
        Incomplete = 0
        Tentative = 1
        Accepted = 2
    

class OrientXpressBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AxisOption: GeometricUtilities.OrientXpressBuilder.Axis
    Csys: CoordinateSystem
    FixedCsys: NXObject
    PlaneOption: GeometricUtilities.OrientXpressBuilder.Plane
    ProgramDefinedCsys: NXObject
    ReferenceOption: GeometricUtilities.OrientXpressBuilder.Reference


    class Reference(enum.Enum):
        AcsWorkPart = 0
        AcsDisplayPart = 1
        WcsWorkPart = 2
        WcsDisplayPart = 3
        Csys = 4
        Fixed = 5
        ProgramDefined = 6
    

    class Plane(enum.Enum):
        Yz = 0
        Xz = 1
        Xy = 2
        Passive = 3
    

    class Axis(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        Passive = 3
    

class OrientationMethodBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AngularLaw: GeometricUtilities.LawBuilder
    Faces: ScCollector
    NormalFaceList: SelectFaceList
    OrientationCurve: Section
    OrientationOption: GeometricUtilities.OrientationMethodBuilder.OrientationOptions
    OrientationPoint: Point
    OrientationVector: Direction


    class OrientationOptions(enum.Enum):
        Fixed = 0
        ByFaceNormals = 1
        ByVectorDirection = 2
        ByAnotherCurve = 3
        ByAPoint = 4
        ByAngularLaw = 5
        ByForcedDirection = 6
    

class OnPathDistancePatternSpacing(GeometricUtilities.PatternSpacing):
    def __init__(self) -> None: ...
    OnPathPitchDistance: GeometricUtilities.OnPathDimensionBuilder
    OnPathSpanDistance: GeometricUtilities.OnPathDimensionBuilder


class OnPathDimWithValueBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def InheritLocation(self, sourceBuilder: GeometricUtilities.OnPathDimWithValueBuilder) -> None:
        ...
    def InheritValue(self, sourceBuilder: GeometricUtilities.OnPathDimWithValueBuilder) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Location: GeometricUtilities.OnPathDimensionBuilder
    Value: Expression
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


class OnPathDimensionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Update(self, updateReason: GeometricUtilities.OnPathDimensionBuilder.UpdateReason) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Expression: Expression
    IsFlipped: bool
    IsParameterUsed: bool
    IsPercentUsed: bool
    Path: SelectObject
    ThroughPoint: Point


    class UpdateReason(enum.Enum):
        Path = 1
        ThroughPoint = 2
        All = 3
    

class OmnicadManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateFtmFixedCurvesBuilder(self) -> GeometricUtilities.FtmFixedCurvesBuilder:
        ...
    def CreateFtmTransformCurvesBuilder(self) -> GeometricUtilities.FtmTransformCurvesBuilder:
        ...
    def CreateFtmTransformPointsBuilder(self) -> GeometricUtilities.FtmTransformPointsBuilder:
        ...
    def Tag(self) -> Tag: ...



class NonInflectingLawBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateSpine(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    EndNode: GeometricUtilities.OnPathDimWithValueBuilder
    MiddleNode: GeometricUtilities.OnPathDimWithValueBuilder
    Spine: Section
    StartNode: GeometricUtilities.OnPathDimWithValueBuilder


class NestModuleBuilder(Builder):
    def __init__(self) -> None: ...
    DestinationModule: Features.SelectFeature
    ModuleToNest: Features.SelectFeature


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MultiTransitionLawBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateNode(self) -> GeometricUtilities.TransitionLawNodeBuilder:
        ...
    def UpdateSpine(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    NodeList: GeometricUtilities.TransitionLawNodeBuilderList
    Spine: Section


class MultiDraft(GeometricUtilities.SimpleDraft):
    def __init__(self) -> None: ...
    def GetDrafts(self, section: Section) -> typing.List[Features.EmbossTaper]:
        ...
    def GetAngleOption(self) -> GeometricUtilities.MultiDraft.AngleOption:
        ...
    def SetAngleOption(self, type: GeometricUtilities.MultiDraft.AngleOption) -> None:
        ...
    BackDraftAngle: Expression
    DraftOption: GeometricUtilities.SimpleDraft.SimpleDraftType
    FrontDraftAngle: Expression


    class AngleOption(enum.Enum):
        Single = 0
        Multiple = 1
    

class MoveToGroupBuilder(Builder):
    def __init__(self) -> None: ...
    SelectedFeatures: Features.SelectFeatureList
    TargetDesignGroup: NXObject


class MovePoleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ControlPoleManager: GeometricUtilities.ControlPoleManagerData
    DegreesAndPatches: GeometricUtilities.DegreesAndSegmentsOrPatchesBuilder
    Entity: NXObject
    MoveMethod: GeometricUtilities.MovePoleBuilder.MoveMethodType
    Plane: Plane
    Vector: Direction
    WCSDirection: GeometricUtilities.MovePoleBuilder.WCSDirectionType


    class WCSDirectionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        YZ = 3
        XZ = 4
        XY = 5
    

    class MoveMethodType(enum.Enum):
        Wcs = 0
        View = 1
        Vector = 2
        Plane = 3
        Normal = 4
        Polygon = 5
    

class ModlMotion(TaggedObject):
    def __init__(self) -> None: ...
    def SetMotionToTwoDimensions(self, plane: Plane) -> None:
        ...
    def SetDependentView(self, view: View) -> None:
        ...
    def ResetMotionToThreeDimensions(self) -> None:
        ...
    def SetUpdateOption(self, option: SmartObject.UpdateOption) -> None:
        ...
    def GetTransformation(self, transformation: float) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AlignVector: Axis
    AlongCurveAngle: GeometricUtilities.ModlAlongCurveAngle
    Angle: Expression
    AngularAxis: Axis
    DeltaEnum: GeometricUtilities.ModlMotion.Delta
    DeltaX: float
    DeltaXc: Expression
    DeltaY: float
    DeltaYc: Expression
    DeltaZ: float
    DeltaZc: Expression
    DistanceAngle: GeometricUtilities.ModlDistanceAngle
    DistanceBetweenPointsDistance: Expression
    DistanceBetweenPointsMeasurePoint: Point
    DistanceBetweenPointsOriginDistance: Expression
    DistanceBetweenPointsOriginPoint: Point
    DistanceBetweenPointsVector: Direction
    DistanceValue: Expression
    DistanceVector: Direction
    EndPoint: Point
    FromCsys: CoordinateSystem
    FromPoint: Point
    ManipulatorMatrix: Matrix3x3
    ManipulatorOrigin: Point3d
    MoveHandle: bool
    Option: GeometricUtilities.ModlMotion.Options
    OrientXpress: GeometricUtilities.OrientXpressBuilder
    RadialAxis: Axis
    RadialDistance: Expression
    RadialMeasurePoint: Point
    RadialOriginDistance: Expression
    RotateVector: Axis
    StartPoint: Point
    TempManipulatorOrigin: Point3d
    ToCsys: CoordinateSystem
    ToPoint: Point
    ToVector: Direction


    class Options(enum.Enum):
        AlongCurveAngle = 0
        DistanceAngle = 1
        Distance = 2
        Angle = 3
        DistanceBetweenPoints = 4
        RadialDistance = 5
        PointToPoint = 6
        RotateByThreePoints = 7
        AlignAxisVector = 8
        CsysToCsys = 9
        Dynamic = 10
        DeltaXyz = 11
        None = 12
    

    class Delta(enum.Enum):
        ReferenceAcsWorkPart = 0
        ReferenceAcsDisplayPart = 1
        ReferenceWcsWorkPart = 2
        ReferenceWcsDisplayPart = 3
    

class ModlDistanceAngle(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Angle: Expression
    AngularDirection: Vector3d
    Distance: Expression
    LinearAxis: Axis
    OrientXpress: GeometricUtilities.OrientXpressBuilder


class ModlAlongCurveAngle(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlongCurve: GeometricUtilities.OnPathDimensionBuilder
    AlongCurveAngle: Expression
    Curve: SelectCurve
    ReverseCurveDirection: bool


class MirrorPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ExistingPlane: SelectISurface
    NewPlane: Plane
    PlaneOption: GeometricUtilities.MirrorPattern.PlaneOptions


    class PlaneOptions(enum.Enum):
        Existing = 0
        New = 1
    

class MiddleHoleData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BooleanOperation: GeometricUtilities.BooleanOperation
    EndChamferAngle: Expression
    EndChamferEnabled: bool
    EndChamferOffset: Expression
    FitOption: str
    HoleDiameter: Expression
    MatchDimOfStartHole: bool
    StartChamferAngle: Expression
    StartChamferEnabled: bool
    StartChamferOffset: Expression


class MatchSurfaceBuilder(Builder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    Constraint: GeometricUtilities.MatchSurfaceBuilder.MatchConstaint
    DistanceTolerance: float
    EditEdge: SelectEdge
    EndToEnd: bool
    KeepSheet: bool
    MatchExact: bool
    Reference: SelectEdge
    ReferenceFace: SelectFace
    RegionLimit: GeometricUtilities.OnPathDimensionBuilder


    class MatchConstaint(enum.Enum):
        Position = 0
        Tangent = 1
    

class LocalUntrimManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateBuilder(self) -> GeometricUtilities.LocalUntrimBuilder:
        ...
    def Tag(self) -> Tag: ...



class LocalUntrimBuilder(Builder):
    def __init__(self) -> None: ...
    def SetCurrentFeature(self, object: Features.Feature) -> None:
        ...
    def UpdateBoundingBox(self) -> None:
        ...
    def CreateProductBoundingBox(self) -> None:
        ...
    def CleanUpFeaturesCreated(self) -> None:
        ...
    def CreateCopyFace(self) -> None:
        ...
    def SetOriginalFace(self, originalFace: Face) -> None:
        ...
    def SetLimitChangeValue(self, limitType: int) -> None:
        ...
    def SetInitialDistanceValue(self, distanceValues: float) -> None:
        ...
    EdgeCollector: ScCollector
    EditCopy: bool
    Face: SelectFace
    RemoveBoundary: bool
    UEndDistance: Expression
    UEndLimit: GeometricUtilities.OnPathDimensionBuilder
    UStartDistance: Expression
    UStartLimit: GeometricUtilities.OnPathDimensionBuilder
    VEndDistance: Expression
    VEndLimit: GeometricUtilities.OnPathDimensionBuilder
    VStartDistance: Expression
    VStartLimit: GeometricUtilities.OnPathDimensionBuilder


class LinearLimits(GeometricUtilities.Limits):
    def __init__(self) -> None: ...


class Limits(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndExtend: GeometricUtilities.Extend
    StartExtend: GeometricUtilities.Extend
    SymmetricOption: bool


class LengthLimitsListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreatePointFacePlaneSelectionBuilder(self, seed: TaggedObject) -> GeometricUtilities.PointFacePlaneSelectionBuilder:
        ...
    def DestroyPointFacePlaneSelectionBuilder(self, entityBuilderData: GeometricUtilities.PointFacePlaneSelectionBuilder) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CapsList: GeometricUtilities.PointFacePlaneSelectionBuilderList


class LengthLimitPointBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Destroy(self) -> None:
        ...
    def FlipPath(self, isStartOfEdge: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    OnPathDim: GeometricUtilities.OnPathDimensionBuilder


class LawBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetSpineIntoBuilder(self, spine: Section) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AlongSpineData: GeometricUtilities.AlongSpineBuilder
    BaseLine: SelectLine
    EndValue: Expression
    Function: str
    IsSimpleCubicAlongSpine: bool
    LawCurve: Section
    LawCurveOption: GeometricUtilities.LawBuilder.RetainLawCurveOption
    LawType: GeometricUtilities.LawBuilder.Type
    MultiTransitionLaw: GeometricUtilities.MultiTransitionLawBuilder
    NonInflectingLaw: GeometricUtilities.NonInflectingLawBuilder
    Parameter: str
    ReverseDirection: bool
    SShapedLaw: GeometricUtilities.SShapedLawBuilder
    StartValue: Expression
    Value: Expression


    class Type(enum.Enum):
        Constant = 0
        Linear = 1
        Cubic = 2
        LinearAlongSpine = 3
        CubicAlongSpine = 4
        ByEquation = 5
        ByLawCurve = 6
        MultiTransition = 7
        NonInflecting = 8
        SShaped = 9
    

    class RetainLawCurveOption(enum.Enum):
        KeepOriginal = 0
        Replace = 1
    

class LatticeItemListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateLatticeItemBuilder(self) -> GeometricUtilities.LatticeItemBuilder:
        ...
    def Validate(self) -> bool:
        ...
    LatticeItemList: GeometricUtilities.LatticeItemBuilderList


class LatticeItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.LatticeItemBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.LatticeItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.LatticeItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.LatticeItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.LatticeItemBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.LatticeItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.LatticeItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.LatticeItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.LatticeItemBuilder, object2: GeometricUtilities.LatticeItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.LatticeItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class LatticeItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Destroy(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ClippingBody: SelectBodyList
    ClippingMode: GeometricUtilities.LatticeItemBuilder.ClippingModeTypes
    ExportMode: GeometricUtilities.LatticeItemBuilder.ExportTypes
    LatticeBodies: SelectBodyList


    class ExportTypes(enum.Enum):
        GraphOnly = 0
        GraphandBody = 1
    

    class ClippingModeTypes(enum.Enum):
        None = 0
        Inside = 1
        Outside = 2
    

class InteractiveSectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AppendPlane(self, point1: Point3d, point2: Point3d, origin: Point3d, normal: Vector3d) -> None:
        ...
    def DeleteLast(self) -> None:
        ...
    def GetNumPlanes(self) -> int:
        ...
    def GetNthPlane(self, index: int) -> GeometricUtilities.SectionPlaneData:
        ...
    def Validate(self) -> bool:
        ...


class InstanceEditedExpressionsList(TaggedObject):
    def __init__(self) -> None: ...
    def EditInstanceExpression(self) -> GeometricUtilities.InstanceEditedExpressionItem:
        ...
    def EditInstanceExpression(self, masterExpression: Expression, instanceExpression: Expression) -> GeometricUtilities.InstanceEditedExpressionItem:
        ...
    def Validate(self) -> bool:
        ...
    List: GeometricUtilities.InstanceEditedExpressionItemList


class InstanceEditedExpressionItemList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.InstanceEditedExpressionItem]) -> None:
        ...
    def Append(self, object: GeometricUtilities.InstanceEditedExpressionItem) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.InstanceEditedExpressionItem) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.InstanceEditedExpressionItem:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.InstanceEditedExpressionItem) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.InstanceEditedExpressionItem, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.InstanceEditedExpressionItem]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.InstanceEditedExpressionItem]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.InstanceEditedExpressionItem, object2: GeometricUtilities.InstanceEditedExpressionItem) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.InstanceEditedExpressionItem) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class InstanceEditedExpressionItem(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    MasterExpression: Expression
    ValueExpression: Expression


class IComponentBuilder():
    def Validate(self) -> bool:
        ...


class HorizontalReference(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Flip: bool
    HorizontalRefObject: SelectNXObject
    HorizontalRefVector: Direction
    RotationAngle: Expression


class HelixPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AnglePitch: Expression
    CountOfInstances: Expression
    DirectionType: GeometricUtilities.HelixPattern.DirectionTypes
    DistancePitch: Expression
    HelixPitch: Expression
    HelixSpan: Expression
    NumberOfTurns: Expression
    RotationAxis: Axis
    SizeOption: GeometricUtilities.HelixPattern.SizeOptions


    class SizeOptions(enum.Enum):
        CountAngleDistance = 0
        CountHelixPitchAndTurns = 1
        CountHelixPitchAndSpan = 2
        AngleHelixPitchAndTurns = 3
        AngleHelixPitchAndSpan = 4
    

    class DirectionTypes(enum.Enum):
        Righthand = 0
        Lefthand = 1
    

class GeometryLocationDataCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricUtilities.GeometryLocationData]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateGeometryLocationData(self) -> GeometricUtilities.GeometryLocationData:
        ...
    def Tag(self) -> Tag: ...



class GeometryLocationData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Csys: SelectObject
    EntityType: GeometricUtilities.GeometryLocationData.EntityTypes
    Point: Point


    class EntityTypes(enum.Enum):
        Point = 0
        Csys = 1
    

class GeneralPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FromLocationCsys2d: SelectNXObject
    FromLocationCsys3d: CoordinateSystem
    FromLocationPoint: Point
    FromLocationType: GeometricUtilities.GeneralPattern.FromLocationOptions
    ToCsysList: SelectCoordinateSystemList
    ToPoints: Section


    class FromLocationOptions(enum.Enum):
        Point = 0
        Csys = 1
    

class FtmTransformPointsBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.FtmTransformPointsBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.FtmTransformPointsBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.FtmTransformPointsBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.FtmTransformPointsBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FtmTransformPointsBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FtmTransformPointsBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.FtmTransformPointsBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.FtmTransformPointsBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.FtmTransformPointsBuilder, object2: GeometricUtilities.FtmTransformPointsBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.FtmTransformPointsBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FtmTransformPointsBuilder(Builder):
    def __init__(self) -> None: ...
    TransformEndPoint: Point
    TransformStartPoint: Point


class FtmTransformCurvesBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.FtmTransformCurvesBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.FtmTransformCurvesBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.FtmTransformCurvesBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.FtmTransformCurvesBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FtmTransformCurvesBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FtmTransformCurvesBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.FtmTransformCurvesBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.FtmTransformCurvesBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.FtmTransformCurvesBuilder, object2: GeometricUtilities.FtmTransformCurvesBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.FtmTransformCurvesBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FtmTransformCurvesBuilder(Builder):
    def __init__(self) -> None: ...
    AlignBreakPoints: bool
    OppositeSense: bool
    OppositeSide: bool
    TransformCurvesContinuity: GeometricUtilities.FtmTransformCurvesBuilder.TransformCurvesContinuityType
    TransformCurvesMagnitude: Expression
    TransformEndCurves: Section
    TransformStartCurves: Section


    class TransformCurvesContinuityType(enum.Enum):
        G0 = 0
        G1 = 1
        G2 = 2
    

class FtmFixedCurvesBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.FtmFixedCurvesBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.FtmFixedCurvesBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.FtmFixedCurvesBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.FtmFixedCurvesBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FtmFixedCurvesBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FtmFixedCurvesBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.FtmFixedCurvesBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.FtmFixedCurvesBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.FtmFixedCurvesBuilder, object2: GeometricUtilities.FtmFixedCurvesBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.FtmFixedCurvesBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FtmFixedCurvesBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateContinuityOnClassAChange(self, classAOption: bool) -> None:
        ...
    FixedCurves: Section
    FixedCurvesContinuity: GeometricUtilities.FtmFixedCurvesBuilder.FixedCurvesContinuityType


    class FixedCurvesContinuityType(enum.Enum):
        G0 = 0
        G1 = 1
        G2 = 2
        G3 = 3
        G4 = 4
    

class FrameOnPathBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AnchorLocation: GeometricUtilities.FrameOnPathBuilder.AnchorLocationType
    AnchorPosition: GeometricUtilities.OnPathDimensionBuilder
    Height: Expression
    IsApexReversed: bool
    Length: Expression
    Offset: Expression
    WScale: float


    class AnchorLocationType(enum.Enum):
        Center = 0
        Right = 1
        Left = 2
    

class FlowDirection(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FlowDirectionType: GeometricUtilities.FlowDirection.Type


    class Type(enum.Enum):
        NotSpecified = 0
        Isoparametric = 1
        IsoCurveU = 2
        IsoCurveV = 3
        Perpendicular = 4
        AdjacentEdges = 5
    

class FeatureOptions(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BodyType: GeometricUtilities.FeatureOptions.BodyStyle


    class BodyStyle(enum.Enum):
        Solid = 0
        Sheet = 1
    

class FeatureOffset(TaggedObject):
    def __init__(self) -> None: ...
    def SetStartOffset(self, valueExpression: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  To set the value of the expression modify the expression directly using GeometricUtilities.FeatureOffset.StartOffset and Expression.RightHandSide.")"""
        ...
    def SetEndOffset(self, valueExpression: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  To set the value of the expression modify the expression directly using GeometricUtilities.FeatureOffset.EndOffset and Expression.RightHandSide.")"""
        ...
    def Validate(self) -> bool:
        ...
    EndOffset: Expression
    Option: GeometricUtilities.Type
    StartOffset: Expression


class FaceSetOffsetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.FaceSetOffset]) -> None:
        ...
    def Append(self, object: GeometricUtilities.FaceSetOffset) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.FaceSetOffset) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.FaceSetOffset:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FaceSetOffset) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.FaceSetOffset, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.FaceSetOffset]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.FaceSetOffset]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.FaceSetOffset, object2: GeometricUtilities.FaceSetOffset) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.FaceSetOffset) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FaceSetOffsetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricUtilities.FaceSetOffset]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateFaceSet(self, offset: str, faceCollector: ScCollector, flipValue: bool, index: int) -> GeometricUtilities.FaceSetOffset:
        ...
    def CreateEmptyFaceSet(self) -> GeometricUtilities.FaceSetOffset:
        ...
    def Tag(self) -> Tag: ...



class FaceSetOffset(ExpressionCollectorSet):
    def __init__(self) -> None: ...
    def SetOffset(self, offsetValue: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  To set the value of the expression modify the expression directly using GeometricUtilities.FaceSetOffset.Offset and Expression.RightHandSide.")"""
        ...
    def FlipDirection(self) -> None:
        ...
    FaceCollector: ScCollector
    Offset: Expression


class FaceSetDataCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricUtilities.FaceSetData]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, mFaceCollector: ScCollector, mReverseNormalFlag: bool) -> GeometricUtilities.FaceSetData:
        """[Obsolete("Deprecated in NX8.5.0.  This class is never used and can be safely removed")"""
        ...
    def Tag(self) -> Tag: ...



class FaceSetData(NXObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FaceCollector: ScCollector
    ReverseNormalFlag: bool


class FacePlaneToolBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ToolFaces: GeometricUtilities.FaceSetData
    ToolPlane: Plane


class FacePlaneSelectionBuilderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricUtilities.FacePlaneSelectionBuilder]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def Create(self) -> GeometricUtilities.FacePlaneSelectionBuilder:
        ...
    def Destroy(self, entityBuilderData: GeometricUtilities.FacePlaneSelectionBuilder) -> None:
        ...
    def Tag(self) -> Tag: ...



class FacePlaneSelectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    IsOk: bool
    LimitTopolSwitchFinFlag: bool
    PlaneHelpPoint: Point
    SelectEdge: ScCollector
    SelectFace: GeometricUtilities.FaceSetData
    SelectPlane: Plane
    TrimObject: GeometricUtilities.FacePlaneSelectionBuilder.TrimObjectType
    UseFaceCapBlend: bool
    UsePlaneCapBlend: bool


    class TrimObjectType(enum.Enum):
        Plane = 0
        Face = 1
        Edge = 2
    

class FaceChangeOverflowBehavior(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FaceChangeOption: GeometricUtilities.FaceChangeOverflowBehavior.Option


    class Option(enum.Enum):
        Automatic = 0
        ExtendChangeFace = 1
        ExtendIncidentFace = 2
        ExtendCapFace = 3
    

class ExtrudeRevolveToolBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ToolAxis: Axis
    ToolDirection: Direction
    ToolSection: Section


class ExtensionSide(enum.Enum):
    StartEnd = 0
    Start = 1
    End = 2
    Symmetric = 3


class ExtensionMethod(enum.Enum):
    Incremental = 0
    Total = 1


class ExtensionDirection(enum.Enum):
    Natural = 0
    Linear = 1
    Circular = 2


class Extend(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, valueExpression: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  To set the value of the expression modify the expression directly using GeometricUtilities.Extend.Value and Expression.RightHandSide.")"""
        ...
    def Validate(self) -> bool:
        ...
    Target: DisplayableObject
    TrimType: GeometricUtilities.Extend.ExtendType
    Value: Expression


    class ExtendType(enum.Enum):
        Value = 0
        ValueFromStartLimit = 1
        UntilNext = 2
        UntilSelected = 3
        UntilExtended = 4
        OffsetFromSelected = 5
        ThroughAll = 6
        Symmetric = 7
        Percent = 8
        ArcLength = 9
        ThruPoint = 10
    

class EntityUsageInfoList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.EntityUsageInfo]) -> None:
        ...
    def Append(self, object: GeometricUtilities.EntityUsageInfo) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.EntityUsageInfo) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.EntityUsageInfo:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.EntityUsageInfo) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.EntityUsageInfo, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.EntityUsageInfo]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.EntityUsageInfo]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.EntityUsageInfo, object2: GeometricUtilities.EntityUsageInfo) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.EntityUsageInfo) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class EntityUsageInfo(TaggedObject):
    def __init__(self) -> None: ...
    def GetDependentFeatures(self, typeOfUsage: GeometricUtilities.EntityUsageInfo.Status, dependentFeatures: typing.List[Features.Feature], detailedUsageInfo: str) -> None:
        ...
    def GetOtherDependents(self, typeOfUsage: GeometricUtilities.EntityUsageInfo.Status, otherDependents: typing.List[NXObject], detailedUsageInfo: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Entity: DisplayableObject
    UsageStatus: GeometricUtilities.EntityUsageInfo.Status


    class Status(enum.Enum):
        Unused = 0
        IntraPart = 1
        InterPart = 2
    

class EndHoleData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BooleanOperation: GeometricUtilities.BooleanOperation
    DepthOption: GeometricUtilities.EndHoleData.HoleDepthOptions
    FitOption: str
    FormOption: GeometricUtilities.EndHoleData.FormOptions
    HoleDepth: Expression
    HoleDepthLimitOption: GeometricUtilities.EndHoleData.HoleDepthLimitOptions
    HoleDiameter: Expression
    MatchDimOfStartHole: bool
    RadialEngageOption: str
    ReliefChamferEnabled: bool
    ScrewClearanceEndChamferAngle: Expression
    ScrewClearanceEndChamferEnabled: bool
    ScrewClearanceEndChamferOffset: Expression
    ScrewClearanceStartChamferAngle: Expression
    ScrewClearanceStartChamferEnabled: bool
    ScrewClearanceStartChamferOffset: Expression
    TapDrillDiameter: Expression
    ThreadDepth: Expression
    ThreadLengthOption: GeometricUtilities.EndHoleData.ThreadLengthOptions
    ThreadRotation: GeometricUtilities.EndHoleData.ThreadRotationOptions
    ThreadSize: str
    ThreadedEndChamferAngle: Expression
    ThreadedEndChamferDiameter: Expression
    ThreadedEndChamferEnabled: bool
    ThreadedReliefAngle: Expression
    ThreadedReliefChamferAngle: Expression
    ThreadedReliefChamferOffset: Expression
    ThreadedReliefDepth: Expression
    ThreadedReliefDiameter: Expression
    ThreadedReliefEnabled: bool
    ThreadedStartChamferAngle: Expression
    ThreadedStartChamferDiameter: Expression
    ThreadedStartChamferEnabled: bool
    TipAngle: Expression
    UntilSelectedTarget: SelectFace


    class ThreadRotationOptions(enum.Enum):
        Right = 0
        Left = 1
    

    class ThreadLengthOptions(enum.Enum):
        Diameterx1 = 0
        Diameterx15 = 1
        Diameterx20 = 2
        Diameterx25 = 3
        Diameterx30 = 4
        Standard = 5
        Custom = 6
        Full = 7
    

    class HoleDepthOptions(enum.Enum):
        ToCylinderBottom = 0
        ToConeTip = 1
    

    class HoleDepthLimitOptions(enum.Enum):
        Value = 0
        UntilSelected = 1
        UntilNext = 2
        ThroughBody = 3
    

    class FormOptions(enum.Enum):
        ScrewClearance = 0
        Threaded = 1
        Through = 2
    

class Dummy(enum.Enum):
    Line = 0


class DraftVariableAngleData(TaggedObject):
    def __init__(self) -> None: ...
    def AddDraftPoints(self, points: typing.List[GeometricUtilities.DraftPointData]) -> None:
        ...
    def RemoveDraftPoints(self, points: typing.List[GeometricUtilities.DraftPointData]) -> None:
        ...
    def GetDraftPoints(self) -> typing.List[GeometricUtilities.DraftPointData]:
        ...
    def GetNumberOfDraftPoints(self) -> int:
        ...
    def Validate(self) -> bool:
        ...


class DraftPointData(TaggedObject):
    def __init__(self) -> None: ...
    def SetAngle(self, angle: str) -> None:
        ...
    def GetAngle(self) -> Expression:
        ...
    def Validate(self) -> bool:
        ...
    Parameter: float


class DistancePatternSpacing(GeometricUtilities.PatternSpacing):
    def __init__(self) -> None: ...
    PitchDistance: Expression
    SpanDistance: Expression


class DisplayResolutionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AngleTolerance: float
    EdgeTolerance: float
    FaceTolerance: float
    Resolution: Preferences.PartVisualizationShade.AdvViewToleranceType
    WidthTolerance: float


class DesignMeshVertex(DisplayableObject):
    def __init__(self) -> None: ...
    def GetBody(self) -> GeometricUtilities.DesignMeshBody:
        ...
    def GetFaces(self) -> typing.List[GeometricUtilities.DesignMeshFace]:
        ...
    def GetEdges(self) -> typing.List[GeometricUtilities.DesignMeshEdge]:
        ...
    def GetCoordinates(self) -> Point3d:
        ...


class DesignMeshFace(DisplayableObject):
    def __init__(self) -> None: ...
    def GetBody(self) -> GeometricUtilities.DesignMeshBody:
        ...
    def GetEdges(self) -> typing.List[GeometricUtilities.DesignMeshEdge]:
        ...
    def GetVertices(self) -> typing.List[GeometricUtilities.DesignMeshVertex]:
        ...


class DesignMeshEdge(DisplayableObject):
    def __init__(self) -> None: ...
    def GetBody(self) -> GeometricUtilities.DesignMeshBody:
        ...
    def GetFaces(self, face1: GeometricUtilities.DesignMeshFace, face2: GeometricUtilities.DesignMeshFace) -> None:
        ...
    def GetVertices(self, vertex1: GeometricUtilities.DesignMeshVertex, vertex2: GeometricUtilities.DesignMeshVertex) -> None:
        ...


class DesignMeshBody(DisplayableObject):
    def __init__(self) -> None: ...
    def GetFaces(self) -> typing.List[GeometricUtilities.DesignMeshFace]:
        ...
    def GetEdges(self) -> typing.List[GeometricUtilities.DesignMeshEdge]:
        ...
    def GetVertices(self) -> typing.List[GeometricUtilities.DesignMeshVertex]:
        ...


class DepthSkewBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Depth: Expression
    Skew: Expression


class DegreesAndSegmentsOrPatchesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Degree: int
    SegmentsOrPatches: int
    UDegree: int
    UPatches: int
    VDegree: int
    VPatches: int
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


class CurveType(enum.Enum):
    Rubber = 0
    Line = 1
    Circle = 2
    Ellipse = 3
    Intersection = 4
    Spline = 5
    SpCurve = 6
    Foreign = 7
    ConstantParameter = 8
    TrimmedCurve = 9
    Undefined = 50


class CurveShapingBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AddCurve(self, curve: Curve) -> None:
        ...
    def RemoveCurve(self, curve: Curve) -> None:
        ...
    def SetActivePoints(self, points: typing.List[Point], masterPoint: Point) -> None:
        ...
    def Deform(self) -> None:
        ...
    def ApplyParameterValue(self, sourcePoint: Point, destinationPoints: typing.List[Point]) -> None:
        ...
    def DeleteAllPoints(self, curve: Spline) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CanMoveAlongCurve: bool
    ConstraintManager: Features.GeometricConstraintDataManager
    EndContinuity: GeometricUtilities.Continuity.ContinuityTypes
    HasLinearTransition: bool
    InsertionMethod: GeometricUtilities.CurveShapingBuilder.InsertionMethodOptions
    MovementMethod: GeometricUtilities.CurveShapingBuilder.MovementMethodType
    MovementPlane: Plane
    MovementVector: Direction
    Number: int
    OrientExpress: GeometricUtilities.OrientXpressBuilder
    SelectCurves: SelectSplineList
    SpecifyPoints: SelectPointList
    StartContinuity: GeometricUtilities.Continuity.ContinuityTypes
    WCSOption: GeometricUtilities.CurveShapingBuilder.WCSOptionType


    class WCSOptionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        YZ = 3
        XZ = 4
        XY = 5
    

    class MovementMethodType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Plane = 3
        Normal = 4
    

    class InsertionMethodOptions(enum.Enum):
        Uniform = 0
        ThroughPoints = 1
        BetweenPoints = 2
    

class CurveSettings(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CurveFitData: GeometricUtilities.CurveFitData
    InputCurvesOption: GeometricUtilities.CurveOptions


class CurveRangeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AnchorPosition: GeometricUtilities.CurveRangeBuilder.AnchorPositionType
    Center: GeometricUtilities.OnPathDimensionBuilder
    End: GeometricUtilities.OnPathDimensionBuilder
    Start: GeometricUtilities.OnPathDimensionBuilder


    class AnchorPositionType(enum.Enum):
        Start = 0
        Center = 1
        End = 2
    

class CurveOptions(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Associative: bool
    InputCurveOption: GeometricUtilities.CurveOptions.InputCurve


    class InputCurve(enum.Enum):
        Retain = 0
        Blank = 1
        Delete = 2
        Replace = 3
    

class CurveLocationType(enum.Enum):
    Start = 0
    End = 1
    Center = 2
    Mid = 3


class CurveLocation():
    Type: GeometricUtilities.CurveLocationType
    Location: Point3d
    def ToString(self) -> str:
        ...
    def __init__(self, Type: GeometricUtilities.CurveLocationType, Location: Point3d) -> None: ...


class CurveLimitsData(TaggedObject):
    def __init__(self) -> None: ...
    def ComplementArc(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    EndLimit: GeometricUtilities.CurveExtendData
    FullCircle: bool
    StartLimit: GeometricUtilities.CurveExtendData


class CurveLengthData(TaggedObject):
    def __init__(self) -> None: ...
    def SetStartDistance(self, startDistance: str) -> None:
        ...
    def SetEndDistance(self, endDistance: str) -> None:
        ...
    def SetTotalLength(self, totalLength: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    EndDistance: Expression
    ExtensionDirection: GeometricUtilities.ExtensionDirection
    ExtensionMethod: GeometricUtilities.ExtensionMethod
    ExtensionSide: GeometricUtilities.ExtensionSide
    StartDistance: Expression
    TotalLength: Expression


class CurveLengthBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndOffset0: Expression
    EndOffset1: Expression
    EndSelection0: SelectDisplayableObjectList
    EndSelection1: SelectDisplayableObjectList
    EndType0: GeometricUtilities.CurveLengthBuilder.EndObjectType
    EndType1: GeometricUtilities.CurveLengthBuilder.EndObjectType
    ReverseEndOffset0Direction: bool
    ReverseEndOffset1Direction: bool
    ReverseGuideCurveLoopDirection: bool


    class EndObjectType(enum.Enum):
        Value = 0
        FromSelected = 1
    

class CurveFitOptions(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FitOption: GeometricUtilities.CurveFitOptions.FitMethod
    MaximumDegree: int
    MaximumSegments: int


    class FitMethod(enum.Enum):
        Cubic = 0
        Quintic = 1
        Advanced = 2
    

class CurveFitJoin(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CurveFitOptions: GeometricUtilities.CurveFitOptions
    CurveJoinMethod: GeometricUtilities.CurveFitJoin.JoinMethod


    class JoinMethod(enum.Enum):
        No = 0
        Cubic = 1
        Genernal = 2
        Quintic = 3
    

class CurveFitData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AngleTolerance: float
    CurveJoinMethod: GeometricUtilities.CurveFitData.Join
    Degree: int
    FitMethod: GeometricUtilities.CurveFitData.Method
    IsAdvancedFit: bool
    IsAlignShape: bool
    MaximumDegree: int
    MaximumSegments: int
    MinimumDegree: int
    Segments: int
    Tolerance: float


    class Method(enum.Enum):
        DegreeAndSegments = 0
        DegreeAndTolerance = 1
        KeepParameterization = 2
        AutoFit = 3
    

    class Join(enum.Enum):
        No = 0
        Cubic = 1
        General = 2
        Quintic = 3
    

class CurveExtensionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    EndExtensionOption: GeometricUtilities.CurveExtensionBuilder.ExtensionOption
    EndPoint: Point
    EndValue: Expression
    IsSymmetric: bool
    StartExtensionOption: GeometricUtilities.CurveExtensionBuilder.ExtensionOption
    StartPoint: Point
    StartValue: Expression


    class ExtensionOption(enum.Enum):
        None = 0
        ByValue = 1
        ByPoint = 2
    

class CurveExtendData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Distance: Expression
    LimitOption: GeometricUtilities.CurveExtendData.LimitOptions
    UntilSelectedObject: SelectDisplayableObject


    class LimitOptions(enum.Enum):
        Value = 0
        AtPoint = 1
        UntilSelected = 2
    

class CurveAlignedListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateCurveAlignedItemBuilder(self) -> GeometricUtilities.CurveAlignedItemBuilder:
        ...
    def Validate(self) -> bool:
        ...
    List: GeometricUtilities.CurveAlignedItemBuilderList


class CurveAlignedItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.CurveAlignedItemBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.CurveAlignedItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.CurveAlignedItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.CurveAlignedItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.CurveAlignedItemBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.CurveAlignedItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.CurveAlignedItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.CurveAlignedItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.CurveAlignedItemBuilder, object2: GeometricUtilities.CurveAlignedItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.CurveAlignedItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CurveAlignedItemBuilder(Builder):
    def __init__(self) -> None: ...
    CurveAlignedSelection: Section
    CurveControl: GeometricUtilities.CurveAlignedItemBuilder.CurveControlTypes


    class CurveControlTypes(enum.Enum):
        U = 0
        V = 1
    

class CrayonSelectionData(TaggedObject):
    def __init__(self) -> None: ...
    def SelectEntity(self, entity: GeometricUtilities.CrayonSelectionData.EntityData) -> None:
        ...
    def SelectEntities(self, entities: typing.List[GeometricUtilities.CrayonSelectionData.EntityData]) -> None:
        ...
    def GetEntities(self) -> typing.List[GeometricUtilities.CrayonSelectionData.EntityData]:
        ...
    def Clear(self) -> None:
        ...
    def Validate(self) -> bool:
        ...


    class CrayonSelectionDataEntityData():
        Entity: NXObject
        PickPoint: Point3d
        View: View
        def ToString(self) -> str:
            ...
        def __init__(self, Entity: NXObject, PickPoint: Point3d, View: View) -> None: ...
    

    class CrayonSelectionData_EntityData():
        entity: Tag
        pickPoint: Point3d
        view: Tag
    

class ConvertFeatureGroupsToModulesBuilder(Builder):
    def __init__(self) -> None: ...
    def AddAll(self) -> None:
        ...
    def RemoveAll(self) -> None:
        ...
    def AddFeatureGroupIntoConvertibleSet(self, featureGroups: typing.List[Features.FeatureGroup]) -> None:
        ...
    def RemoveFeatureGroupFromConvertibleSet(self, featureGroups: typing.List[Features.FeatureGroup]) -> None:
        ...


class ConvertFeatureGroupsToDesignGroupsBuilder(Builder):
    def __init__(self) -> None: ...
    def AnalyzePart(self) -> None:
        ...
    Scheme: GeometricUtilities.ConvertFeatureGroupsToDesignGroupsBuilder.ConversionScheme
    SelectedFeatureGroupList: Features.SelectFeatureList
    TypeOptionMenu: GeometricUtilities.ConvertFeatureGroupsToDesignGroupsBuilder.TypeOptionsMenu


    class TypeOptionsMenu(enum.Enum):
        SingleFeatureGroup = 0
        AllFeatureGroups = 1
    

    class ConversionScheme(enum.Enum):
        Convert = 0
        EmbedDesignGroupInFeatureGroup = 1
        EmbedFeatureGroupInDesignGroup = 2
    

class ControlPoleManagerData(TaggedObject):
    def __init__(self) -> None: ...
    def SetPoles(self, groupIndex: int, polesIndex: int, poles: typing.List[Point]) -> None:
        ...
    def GetPoles(self, groupIndex: int, polesIndex: int, poles: typing.List[Point]) -> None:
        ...
    def SelectPoles(self, groupIndex: int, polesIndex: int, poles: typing.List[Point]) -> None:
        ...
    def DeselectPoles(self, groupIndex: int, polesIndex: int, poles: typing.List[Point]) -> None:
        ...
    def GetSelectedPoles(self, groupIndex: int, polesIndex: int, poles: typing.List[Point]) -> None:
        ...
    def CreatePolesGroup(self) -> int:
        ...
    def DeletePolesGroup(self, groupIndex: int) -> None:
        ...
    def GetUDimension(self, groupIndex: int) -> int:
        ...
    def SetUDimension(self, groupIndex: int, uDimension: int) -> None:
        ...
    def GetVDimension(self, groupIndex: int) -> int:
        ...
    def SetVDimension(self, groupIndex: int, vDimension: int) -> None:
        ...
    def GetIsUPeriodic(self, groupIndex: int) -> bool:
        ...
    def SetIsUPeriodic(self, groupIndex: int, uPeriodicity: bool) -> None:
        ...
    def GetIsVPeriodic(self, groupIndex: int) -> bool:
        ...
    def SetIsVPeriodic(self, groupIndex: int, vPeriodicity: bool) -> None:
        ...
    def UpdatePolePositions(self, groupIndex: int, poleIndex: int, newPosition: typing.List[Point3d]) -> None:
        ...
    def SetPoleGroupEntity(self, groupIndex: int, face: Face) -> None:
        ...
    def SetPoleGroupEntity(self, groupIndex: int, curve: Curve) -> None:
        ...
    def Validate(self) -> bool:
        ...


class Continuity(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ConstraintFaces: ScCollector
    ContinuityType: GeometricUtilities.Continuity.ContinuityTypes
    IsFixed: bool


    class ContinuityTypes(enum.Enum):
        G0 = 0
        G1 = 1
        G2 = 2
        G3 = 3
        Free = 4
    

class ConicCrossSection(TaggedObject):
    def __init__(self) -> None: ...
    def SetFirstOffset(self, offset: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  To set the value of the expression modify the expression directly using NXOpen.GeometricUtilities.ConicCrossSection.FirstOffset and NXOpen.Expression.RightHandSide.")"""
        ...
    def SetSecondOffset(self, offset: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  To set the value of the expression modify the expression directly using NXOpen.GeometricUtilities.ConicCrossSection.SecondOffset and NXOpen.Expression.RightHandSide.")"""
        ...
    def SetRho(self, rho: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  To set the value of the expression modify the expression directly using NXOpen.GeometricUtilities.ConicCrossSection.Rho and NXOpen.Expression.RightHandSide.")"""
        ...
    def SetLawControlConstantFirstOffset(self, radius: str) -> None:
        ...
    def SetLawControlFirstOffsetStartRadius(self, radius: str) -> None:
        ...
    def SetLawControlFirstOffsetEndRadius(self, radius: str) -> None:
        ...
    def SetLawControlConstantSecondOffset(self, radius: str) -> None:
        ...
    def SetLawControlSecondOffsetStartRadius(self, radius: str) -> None:
        ...
    def SetLawControlSecondOffsetEndRadius(self, radius: str) -> None:
        ...
    def SetLawControlConstantRho(self, radius: str) -> None:
        ...
    def SetLawControlRhoStartRadius(self, radius: str) -> None:
        ...
    def SetLawControlRhoEndRadius(self, radius: str) -> None:
        ...
    def SetLawControlConstantDepth(self, radius: str) -> None:
        ...
    def SetLawControlDepthStartRadius(self, radius: str) -> None:
        ...
    def SetLawControlDepthEndRadius(self, radius: str) -> None:
        ...
    def SetLawControlConstantShapeSkew(self, radius: str) -> None:
        ...
    def SetLawControlShapeSkewStartRadius(self, radius: str) -> None:
        ...
    def SetLawControlShapeSkewEndRadius(self, radius: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ConicMethod: GeometricUtilities.ConicCrossSection.DefineMethod
    Depth: Expression
    DepthLawControl: GeometricUtilities.LawBuilder
    DepthOption: GeometricUtilities.ConicCrossSection.DepthMethod
    FirstConstraintCurveCollector: ScCollector
    FirstLawControl: GeometricUtilities.LawBuilder
    FirstOffset: Expression
    FirstOffsetOption: GeometricUtilities.ConicCrossSection.OffsetMethod
    OffsetSkewRatio: Expression
    Rho: Expression
    RhoLawControl: GeometricUtilities.LawBuilder
    RhoOption: GeometricUtilities.ConicCrossSection.RhoMethod
    SecondConstraintCurveCollector: ScCollector
    SecondLawControl: GeometricUtilities.LawBuilder
    SecondOffset: Expression
    SecondOffsetOption: GeometricUtilities.ConicCrossSection.OffsetMethod
    ShapeSkew: Expression
    ShapeSkewLawControl: GeometricUtilities.LawBuilder
    ShapeSkewOption: GeometricUtilities.ConicCrossSection.ShapeSkewMethod
    TransitionLinkFlag: bool


    class ShapeSkewMethod(enum.Enum):
        Constant = 0
        Law = 1
    

    class RhoMethod(enum.Enum):
        Constant = 0
        Law = 1
        AutoEllipse = 2
    

    class OffsetMethod(enum.Enum):
        Constant = 0
        Law = 1
    

    class DepthMethod(enum.Enum):
        Constant = 0
        Law = 1
    

    class DefineMethod(enum.Enum):
        BoundaryPlusCenter = 0
        BoundaryPlusRho = 1
        CenterPlusRho = 2
    

class CompareManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetCompareManager(self, owner: Session) -> GeometricUtilities.CompareManager:
        ...
    def CreateBodyCompareBuilder(self, part: Part) -> GeometricUtilities.BodyCompareBuilder:
        ...
    def Tag(self) -> Tag: ...



class CombOptionsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AnalysisType: GeometricUtilities.CombOptionsBuilder.AnalysisTypes
    AutoScale: bool
    Density: int
    HasMaxNeedleLength: bool
    IntermediateDensity: int
    IsMaximumLabelEnabled: bool
    IsMinimumLabelEnabled: bool
    IsNormalToGridPlane: bool
    MaxNeedleLength: float
    ReverseNeedles: bool
    SampleDistance: float
    ScaleFactor: float
    ShowNeedles: bool


    class LabelTypes(enum.Enum):
        None = 0
        Minimum = 1
        Maximum = 2
        MinimumMaximum = 3
    

    class AnalysisTypes(enum.Enum):
        None = 0
        Curvature = 1
        Radius = 2
    

class ColorCodedRegionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def BuildColoredRegion(self, facetBody: Facet.FacetedBody, facetId: int, localVertexId: int) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.GeometricUtilities.ColorCodedRegionBuilder.BuildBodyColoredRegion instead.")"""
        ...
    def BuildBodyColoredRegion(self, body: DisplayableObject, facetId: int, localVertexId: int) -> None:
        ...
    def DeselectColoredRegion(self, objIndex: int) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AllSameColor: bool


class CircularPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AngularSpacing: GeometricUtilities.AngularPatternSpacing
    CenterPoint: SelectNXObject
    CreateLastStaggered: bool
    Flip: bool
    HorizontalRef: GeometricUtilities.HorizontalReference
    IncludeSeedToggle: bool
    RadialSpacing: GeometricUtilities.DistancePatternSpacing
    RotationAxis: Axis
    RotationCenter: Point
    StaggerType: GeometricUtilities.CircularPattern.StaggerOptions
    UseRadialDirectionToggle: bool


    class StaggerOptions(enum.Enum):
        None = 0
        Row = 1
    

class CircularFrameBuilder(GeometricUtilities.ShapeFrameBuilder):
    def __init__(self) -> None: ...
    def GetRadius(self, index: int) -> float:
        ...
    def SetRadius(self, index: int, radius: float) -> None:
        ...
    def GetAngle(self, index: int) -> float:
        ...
    def SetAngle(self, index: int, angle: float) -> None:
        ...
    Subtype: GeometricUtilities.CircularFrameBuilder.Subtypes


    class Subtypes(enum.Enum):
        Arbitrary = 0
        Half = 1
        Quarter = 2
        Full = 3
    

class CircularCrossSection(TaggedObject):
    def __init__(self) -> None: ...
    def SetRadius(self, radius: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  To set the value of the expression modify the expression directly using GeometricUtilities.CircularCrossSection.Radius and Expression.RightHandSide.")"""
        ...
    def SetLawControlConstantRadius(self, radius: str) -> None:
        ...
    def SetLawControlStartRadius(self, radius: str) -> None:
        ...
    def SetLawControlEndRadius(self, radius: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    LawControl: GeometricUtilities.LawBuilder
    Radius: Expression
    RadiusOption: GeometricUtilities.RadiusMethod


class ChamferEdgeManager(TaggedObject):
    def __init__(self) -> None: ...
    def CreateChamferEdgeChainSetBuilder(self) -> GeometricUtilities.ChamferEdgeChainSetBuilder:
        ...
    def Validate(self) -> bool:
        ...
    EdgeChainSetList: GeometricUtilities.ChamferEdgeChainSetBuilderList


class ChamferEdgeChainSetBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.ChamferEdgeChainSetBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.ChamferEdgeChainSetBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.ChamferEdgeChainSetBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.ChamferEdgeChainSetBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ChamferEdgeChainSetBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.ChamferEdgeChainSetBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.ChamferEdgeChainSetBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.ChamferEdgeChainSetBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.ChamferEdgeChainSetBuilder, object2: GeometricUtilities.ChamferEdgeChainSetBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.ChamferEdgeChainSetBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ChamferEdgeChainSetBuilder(Builder):
    def __init__(self) -> None: ...
    Angular: Expression
    CrossSectionOptions: GeometricUtilities.ChamferEdgeChainSetBuilder.CrossSectionType
    Distance1: Expression
    Distance2: Expression
    Edges: ScCollector
    ReverseDirection: bool


    class CrossSectionType(enum.Enum):
        Symmetric = 0
        Asymmetric = 1
        OffsetandAngle = 2
    

class CAMDataPrepManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateMatchSurfaceBuilder(self) -> GeometricUtilities.MatchSurfaceBuilder:
        ...
    def CreateReduceSurfaceRadiusBuilder(self) -> GeometricUtilities.ReduceSurfaceRadiusBuilder:
        ...
    def CreateReduceSurfaceRadiusFaceGroupBuilder(self) -> GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder:
        ...
    def CreateSnipIntoPatchesBuilder(self) -> GeometricUtilities.SnipIntoPatchesBuilder:
        ...
    def Tag(self) -> Tag: ...



class BridgeCurveConnectivity(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateOnDirectionAtPointReversal(self) -> None:
        ...
    def EditUVPercentage(self, uPercent: float, vPercent: float) -> None:
        ...
    def UpdateBasedOnLocationOnSection(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CanReverseDirection: bool
    Continuity: GeometricUtilities.Continuity
    CurveDirectionOption: GeometricUtilities.BridgeCurveConnectivity.CurveDirectionOptions
    DirectionAtPoint: Direction
    FaceDirectionOption: GeometricUtilities.BridgeCurveConnectivity.FaceDirectionOptions
    LocationOnSection: GeometricUtilities.OnPathDimensionBuilder
    PerpendicularFace: SelectFace
    SectionAngle: Expression
    UPercentage: Expression
    VPercentage: Expression


    class FaceDirectionOptions(enum.Enum):
        Sectional = 0
        IsoU = 1
        IsoV = 2
    

    class CurveDirectionOptions(enum.Enum):
        Tangent = 0
        Perpendicular = 1
    

class BoundingObjectBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.BoundingObjectBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.BoundingObjectBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.BoundingObjectBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.BoundingObjectBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.BoundingObjectBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.BoundingObjectBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.BoundingObjectBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.BoundingObjectBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.BoundingObjectBuilder, object2: GeometricUtilities.BoundingObjectBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.BoundingObjectBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BoundingObjectBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BoundingCurve: SelectDisplayableObject
    BoundingObjectMethod: GeometricUtilities.BoundingObjectBuilder.Method
    BoundingPlane: Plane
    BoundingPoint: Point
    BoundingPoint1: Point
    BoundingPoint2: Point
    BoundingProjectPoint: Point
    BoundingVector: Direction
    IntersectionReference: Point


    class Method(enum.Enum):
        ExistingCurve = 0
        ProjectPoint = 1
        LineBy2Points = 2
        PointAndVector = 3
        ByPlane = 4
    

class BoundaryDefinitionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.BoundaryDefinitionBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.BoundaryDefinitionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.BoundaryDefinitionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.BoundaryDefinitionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.BoundaryDefinitionBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.BoundaryDefinitionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.BoundaryDefinitionBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.BoundaryDefinitionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.BoundaryDefinitionBuilder, object2: GeometricUtilities.BoundaryDefinitionBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.BoundaryDefinitionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BoundaryDefinitionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AppendPoint(self, point: Point3d, isKeyPoint: bool) -> None:
        ...
    def Close(self) -> bool:
        ...
    def DeleteAll(self) -> None:
        ...
    def DeleteLastKeyPoint(self) -> None:
        ...
    def GetPoints(self) -> typing.List[Point3d]:
        ...
    def SetPlaneNormal(self, direction: Vector3d) -> None:
        ...
    def Translate(self, vector: Vector3d) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Depth: Expression


class BooleanToolBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ExtrudeRevolveTool: GeometricUtilities.ExtrudeRevolveToolBuilder
    FacePlaneTool: GeometricUtilities.FacePlaneToolBuilder
    ReverseDirection: bool
    ToolOption: GeometricUtilities.BooleanToolBuilder.BooleanToolType


    class BooleanToolType(enum.Enum):
        FaceOrPlane = 0
        NewPlane = 1
        Extrude = 2
        Revolve = 3
    

class BooleanRegionSelect(TaggedObject):
    def __init__(self) -> None: ...
    def AppendOneRegionTracker(self) -> GeometricUtilities.RegionTracker:
        ...
    def AssignTargets(self, targets: typing.List[TaggedObject]) -> None:
        ...
    def NotifyBodiesHaveChanged(self, bodySelectionList: ScCollector) -> None:
        ...
    def ClearRegions(self) -> None:
        ...
    def ClearAllRegionTrackers(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    KeepRemoveTargetMethod: GeometricUtilities.BooleanRegionSelect.KeepRemoveOption
    KeepRemoveToolMethod: GeometricUtilities.BooleanRegionSelect.KeepRemoveOption
    SelectMethod: GeometricUtilities.BooleanRegionSelect.SelectOption


    class SelectOption(enum.Enum):
        None = 0
        KeepOrRemove = 1
        KeepAndRemove = 2
    

    class KeepRemoveOption(enum.Enum):
        Keep = 0
        Remove = 1
    

class BooleanOperation(TaggedObject):
    def __init__(self) -> None: ...
    def GetBooleanOperationAndBody(self, type: GeometricUtilities.BooleanOperation.BooleanType, targetBody: Body) -> None:
        """[Obsolete("Deprecated in NX4.0.0.  Use GeometricUtilities.BooleanOperation.Type and GeometricUtilities.BooleanOperation.GetTargetBodies instead.")"""
        ...
    def SetBooleanOperationAndBody(self, type: GeometricUtilities.BooleanOperation.BooleanType, targetBody: Body) -> None:
        """[Obsolete("Deprecated in NX4.0.0.  Use GeometricUtilities.BooleanOperation.Type and GeometricUtilities.BooleanOperation.SetTargetBodies instead.")"""
        ...
    def GetTargetBodies(self) -> typing.List[Body]:
        ...
    def SetTargetBodies(self, targetBodies: typing.List[Body]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Type: GeometricUtilities.BooleanOperation.BooleanType


    class BooleanType(enum.Enum):
        Create = 0
        Unite = 1
        Subtract = 2
        Intersect = 3
        Sew = 4
    

class BodyCompareBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateControlBodiesToEngine(self) -> None:
        ...
    def UpdateSampleBodiesToEngine(self) -> None:
        ...
    def SetControlPart(self, part: Part) -> None:
        ...
    def SetSamplePart(self, part: Part) -> None:
        ...
    def CompareAction(self) -> None:
        ...
    def ReportAction(self) -> None:
        ...
    def RecreateVisualizer(self) -> None:
        ...
    def PreVisualizationProcess(self) -> None:
        ...
    def DisposeVisualization(self) -> None:
        ...
    def CreateConvergentCompareStrategy(self) -> None:
        ...
    def ClearAllComparedPairs(self) -> None:
        ...
    ColorPickerAbsent: NXColor
    ColorPickerChanged: NXColor
    ColorPickerNew: NXColor
    ColorPickerSame: NXColor
    CompareMethod: GeometricUtilities.BodyCompareBuilder.CompareOptionType
    DeviationFloor: float
    FloorRange: float
    IsCompareDone: bool
    OptionMenu: GeometricUtilities.BodyCompareBuilder.FaceChangeCriteriaOption
    SelectControlBody: SelectBodyList
    SelectSampleBody: SelectBodyList
    TessellationTolerance: float
    TranslucentControl: int


    class FaceChangeCriteriaOption(enum.Enum):
        Shape = 0
        Any = 1
        Deviation = 2
    

    class CompareOptionType(enum.Enum):
        Face = 0
        DistanceMap = 1
    

class BlendStopshortBuilderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricUtilities.BlendStopshortBuilder]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, mChoice: GeometricUtilities.BlendStopshortBuilder.Choices, mOnPathExp: Expression, mPath: Edge, mIsFlipped: bool, mThruPoint: Point) -> GeometricUtilities.BlendStopshortBuilder:
        ...
    def Tag(self) -> Tag: ...



class BlendStopshortBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Destroy(self) -> None:
        ...
    def FlipPath(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Choice: GeometricUtilities.BlendStopshortBuilder.Choices
    OnPath: GeometricUtilities.OnPathDimensionBuilder


    class Choices(enum.Enum):
        AtDistance = 0
        AtIntersection = 1
    

class BlendSetbackBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[GeometricUtilities.BlendSetbackBuilder]) -> None:
        ...
    def Append(self, object: GeometricUtilities.BlendSetbackBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: GeometricUtilities.BlendSetbackBuilder) -> int:
        ...
    def FindItem(self, index: int) -> GeometricUtilities.BlendSetbackBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.BlendSetbackBuilder) -> None:
        ...
    def Erase(self, obj: GeometricUtilities.BlendSetbackBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[GeometricUtilities.BlendSetbackBuilder]:
        ...
    def SetContents(self, objects: typing.List[GeometricUtilities.BlendSetbackBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: GeometricUtilities.BlendSetbackBuilder, object2: GeometricUtilities.BlendSetbackBuilder) -> None:
        ...
    def Insert(self, location: int, object: GeometricUtilities.BlendSetbackBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BlendSetbackBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Direction: GeometricUtilities.BlendSetbackBuilder.Directions
    Face: ScCollector
    HandlePoint: Point
    IsDirectionFlipped: bool
    Plane: Plane
    SetbackPoint: Point


    class Directions(enum.Enum):
        U = 0
        V = 1
        Plane = 2
    

class BlendLimitsData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CapsList: TaggedObjectList
    UserSelectedObjects: bool


class BetweenLocationsData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FromLocation: GeometricUtilities.GeometryLocationData
    ToLocationList: TaggedObjectList


class AngularPatternSpacing(GeometricUtilities.PatternSpacing):
    def __init__(self) -> None: ...
    PitchAngle: Expression
    PitchDistance: Expression
    SpanAngle: Expression
    UsePitchOption: GeometricUtilities.AngularPatternSpacing.UsePitchOptions


    class UsePitchOptions(enum.Enum):
        Angle = 0
        Distance = 1
    

class AngularLimits(GeometricUtilities.Limits):
    def __init__(self) -> None: ...
    Distance: float


class AnchorLocatorBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Origin: Point3d
    XAxis: Vector3d
    YAxis: Vector3d


class AlongSpineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetSpinePoints(self, spPoints: typing.List[GeometricUtilities.OnPathDimWithValueBuilder]) -> None:
        ...
    def SetFeatureSpine(self, featureSpine: Section) -> None:
        ...
    def ResetSpine(self) -> None:
        ...
    def CreateSpinePoint(self) -> GeometricUtilities.OnPathDimWithValueBuilder:
        ...
    def Validate(self) -> bool:
        ...
    FeatureSpine: Section
    Spine: Section
    SpineOption: GeometricUtilities.AlongSpineBuilder.RetainSpineOption
    SpinePointList: ObjectList


    class RetainSpineOption(enum.Enum):
        KeepOriginal = 0
        Replace = 1
    

class AlongPathPattern(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    UseYDirectionToggle: bool
    XOnPathSpacing: GeometricUtilities.OnPathDistancePatternSpacing
    XPath: Section
    XPathOption: GeometricUtilities.AlongPathPattern.PathOptions
    YDirection: Direction
    YDirectionOption: GeometricUtilities.AlongPathPattern.YDirectionOptions
    YOnPathSpacing: GeometricUtilities.OnPathDistancePatternSpacing
    YPath: Section
    YPathOption: GeometricUtilities.AlongPathPattern.PathOptions
    YSpacing: GeometricUtilities.DistancePatternSpacing


    class YDirectionOptions(enum.Enum):
        Vector = 0
        Section = 1
    

    class PathOptions(enum.Enum):
        Rigid = 0
        Offset = 1
        Translate = 2
    

class AlignmentMethodBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetSections(self, sections: typing.List[Section]) -> None:
        ...
    def CreateOnPathDimBuilder(self, sec: Section, pnt: Point3d) -> GeometricUtilities.OnPathDimensionBuilder:
        ...
    def UnloadSections(self) -> None:
        ...
    def AddSection(self, sectionIndex: int, sec: Section) -> None:
        ...
    def RemoveSection(self, sec: Section) -> None:
        ...
    def RemoveSectionAtIndex(self, secIndex: int) -> None:
        ...
    def UpdateSectionAtIndex(self, secIndex: int) -> None:
        ...
    def ComputeDefaultPoints(self) -> None:
        ...
    def GetAllPoints(self, numSection: int) -> typing.List[GeometricUtilities.OnPathDimensionBuilder]:
        ...
    def GetPoint(self, sectionIndex: int, pointIndex: int) -> GeometricUtilities.OnPathDimensionBuilder:
        ...
    def SetAlignPoints(self, alignPoints: typing.List[GeometricUtilities.OnPathDimensionBuilder]) -> None:
        ...
    def RemoveAllPoints(self) -> None:
        ...
    def AddPoint(self, alignPoint: GeometricUtilities.OnPathDimensionBuilder) -> int:
        ...
    def RemovePoint(self, alignPoint: GeometricUtilities.OnPathDimensionBuilder) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AlignAxis: Axis
    AlignCurve: Section
    AlignType: GeometricUtilities.AlignmentMethodBuilder.Type
    AlignVector: Direction
    EndAlignFillerSurfaceOption: GeometricUtilities.AlignmentMethodBuilder.AlignFillerSurfaceType
    NumberOfPointsPerSection: int
    NumberOfSections: int
    StartAlignFillerSurfaceOption: GeometricUtilities.AlignmentMethodBuilder.AlignFillerSurfaceType


    class Type(enum.Enum):
        Parameter = 0
        ArcLength = 1
        Points = 2
        Distance = 3
        Angle = 4
        SpineCurve = 5
        SplinePoints = 6
        Segments = 7
        Developable = 8
    

    class AlignFillerSurfaceType(enum.Enum):
        NoFiller = 0
        Cone = 1
        Cylinder = 2
        Trimmed = 3
    

