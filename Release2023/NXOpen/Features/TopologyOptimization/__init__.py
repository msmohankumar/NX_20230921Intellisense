from ....NXOpen import *
from ...Features import *
from ..TopologyOptimization import *

import typing
import enum

class ViewXygraphBuilder(Builder):
    def __init__(self) -> None: ...
    OptimizationConstraint: Features.TopologyOptimization.OptimizationConstraint
    Study: Features.TopologyOptimization.Study
    SubcaseName: str
    TargetWindowDevice: int
    XygraphContent: Features.TopologyOptimization.ViewXygraphBuilder.ContentOption


    class ContentOption(enum.Enum):
        OptimizationObjective = 0
        OptimizationConstraint = 1
    

class ViewTabularResultBuilder(Builder):
    def __init__(self) -> None: ...
    def GetStudies(self) -> typing.List[Features.TopologyOptimization.Study]:
        ...
    def SetStudies(self, studies: typing.List[Features.TopologyOptimization.Study]) -> None:
        ...
    Bodies: SelectTaggedObjectList
    ReportContent: Features.TopologyOptimization.ViewTabularResultBuilder.ReportContentOption


    class ReportContentOption(enum.Enum):
        OptimizationObjective = 0
        OptimizationConstraint = 1
        All = 2
    

class ViewContourBuilder(Builder):
    def __init__(self) -> None: ...
    Bodies: SelectTaggedObjectList
    ColorScaleRangeType: Features.TopologyOptimization.ViewContourBuilder.ColorScaleRangeOption
    ContourDisplayStyle: Features.TopologyOptimization.ViewContourBuilder.ContourDisplayStyleOption
    DisplayType: Features.TopologyOptimization.ViewContourBuilder.DisplayOption
    FirstStudy: Features.TopologyOptimization.Study
    ResultComponentType: Features.TopologyOptimization.ViewContourBuilder.ResultComponentOption
    SecondStudy: Features.TopologyOptimization.Study
    SubcaseIndexForFirstStudy: int
    SubcaseIndexForSecondStudy: int


    class ResultComponentOption(enum.Enum):
        DisplacementMagnitude = 0
        DisplacementWorstInXYZ = 1
        DisplacementX = 2
        DisplacementY = 3
        DisplacementZ = 4
        DisplacementAll = 5
        StressVonMises = 6
        StressWorstPrincipal = 7
    

    class DisplayOption(enum.Enum):
        Single = 0
        Comparison = 1
    

    class ContourDisplayStyleOption(enum.Enum):
        Smooth = 0
        Banded = 1
    

    class ColorScaleRangeOption(enum.Enum):
        PerView = 0
        CommonAcrossViews = 1
    

class SubcaseManager(Builder):
    def __init__(self) -> None: ...
    def CreateSubcase(self) -> Features.TopologyOptimization.SubcaseItem:
        ...
    SubcaseList: Features.TopologyOptimization.SubcaseItemList


class SubcaseItemList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.TopologyOptimization.SubcaseItem]) -> None:
        ...
    def Append(self, object: Features.TopologyOptimization.SubcaseItem) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.TopologyOptimization.SubcaseItem) -> int:
        ...
    def FindItem(self, index: int) -> Features.TopologyOptimization.SubcaseItem:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.TopologyOptimization.SubcaseItem) -> None:
        ...
    def Erase(self, obj: Features.TopologyOptimization.SubcaseItem, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.TopologyOptimization.SubcaseItem]:
        ...
    def SetContents(self, objects: typing.List[Features.TopologyOptimization.SubcaseItem]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.TopologyOptimization.SubcaseItem, object2: Features.TopologyOptimization.SubcaseItem) -> None:
        ...
    def Insert(self, location: int, object: Features.TopologyOptimization.SubcaseItem) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SubcaseItem(TaggedObject):
    def __init__(self) -> None: ...
    def AddReference(self, reference: NXObject) -> None:
        ...
    def RemoveReference(self, reference: NXObject) -> None:
        ...
    IncludedInOptimization: bool
    Name: str


    class ItemType(enum.Enum):
        Load = 0
        Constraint = 1
    

class Subcase(Features.TopologyOptimization.Container):
    def __init__(self) -> None: ...
    def AddReference(self, reference: NXObject) -> None:
        ...
    def RemoveReference(self, reference: NXObject) -> None:
        ...
    def GetReferences(self, references: typing.List[NXObject]) -> None:
        ...
    IsIncludedInOptimization: Features.TopologyOptimization.Subcase.IncludeInOptimization


    class IncludeInOptimization(enum.Enum):
        True = 0
        False = 1
    

class StudyBuilder(Builder):
    def __init__(self) -> None: ...
    def SetResolutionVoxelSizeByStudyQuality(self, studyQualityFactor: int) -> None:
        ...
    AnalysisType: Features.TopologyOptimization.StudyBuilder.AnalysisOption
    ConstantTemperature: Expression
    GravityDirection: Direction
    GravityEnabled: bool
    GravityMagnitude: Expression
    OptimizationObjectiveType: Features.TopologyOptimization.StudyBuilder.OptimizationObjectiveOption
    ResolutionVoxelSize: Expression
    StudyName: str
    StudyQuality: int


    class OptimizationObjectiveOption(enum.Enum):
        MinimumMass = 0
        MinimumVolume = 1
        MaximumStiffness = 2
        MaximumFirstFlexibleMode = 3
    

    class AnalysisOption(enum.Enum):
        LinearStatics = 0
        NormalModes = 1
    

class Study(Features.TopologyOptimization.Container):
    def __init__(self) -> None: ...
    def RunOptimization(self) -> None:
        ...
    def AbortOptimizationProcess(self) -> bool:
        ...
    def RetrieveOptimizationResults(self) -> None:
        ...
    def DiscardUnretrievedOptimizationResults(self) -> None:
        ...
    def Unlock(self) -> None:
        ...
    def GetOptimizedBodies(self) -> typing.List[Body]:
        ...
    def DiscardOptimizationResults(self) -> None:
        ...
    def CreateSceneryBodyBuilder(self, topOptSceneryBody: Features.TopologyOptimization.SceneryBody) -> Features.TopologyOptimization.SceneryBodyBuilder:
        ...
    def GetAllSceneryBodies(self, topOptSceneryBodies: typing.List[Features.TopologyOptimization.SceneryBody]) -> None:
        ...
    def CreateConnectionBuilder(self, connection: Features.TopologyOptimization.Connection) -> Features.TopologyOptimization.ConnectionBuilder:
        ...
    def GetAllConnections(self, topOptConnections: typing.List[Features.TopologyOptimization.Connection]) -> None:
        ...
    def CreateAnalysisConstraintBuilder(self, constraint: Features.TopologyOptimization.AnalysisConstraint) -> Features.TopologyOptimization.AnalysisConstraintBuilder:
        ...
    def GetAllAnalysisConstraints(self, analysisConstraints: typing.List[Features.TopologyOptimization.AnalysisConstraint]) -> None:
        ...
    def CreateDesignSpaceBuilder(self, designSpace: Features.TopologyOptimization.DesignSpace) -> Features.TopologyOptimization.DesignSpaceBuilder:
        ...
    def GetAllDesignSpaces(self, designSpaces: typing.List[Features.TopologyOptimization.DesignSpace]) -> None:
        ...
    def CreateAnalysisLoadBuilder(self, load: Features.TopologyOptimization.AnalysisLoad) -> Features.TopologyOptimization.AnalysisLoadBuilder:
        ...
    def GetAllAnalysisLoads(self, analysisLoads: typing.List[Features.TopologyOptimization.AnalysisLoad]) -> None:
        ...
    def CreateOptimizationConstraintBuilder(self, optConstraint: Features.TopologyOptimization.OptimizationConstraint) -> Features.TopologyOptimization.OptimizationConstraintBuilder:
        ...
    def CreateSubcaseManager(self) -> Features.TopologyOptimization.SubcaseManager:
        ...
    def GetAllSubcases(self, subcases: typing.List[Features.TopologyOptimization.Subcase]) -> None:
        ...
    def CreateConstructionBodyBuilder(self, topOptConstructionBody: Features.TopologyOptimization.ConstructionBody) -> Features.TopologyOptimization.ConstructionBodyBuilder:
        ...
    def CreateConstructionBodyCollectorBuilder(self, constrBodyCollector: Features.TopologyOptimization.ConstructionBodyCollector) -> Features.TopologyOptimization.ConstructionBodyBuilder:
        ...
    def CreateShapeConstraintBuilder(self, topOptShapeConstraint: Features.TopologyOptimization.ShapeConstraint) -> Features.TopologyOptimization.ShapeConstraintBuilder:
        ...
    def CloneSubcase(self, existingSubcase: Features.TopologyOptimization.Subcase) -> Features.TopologyOptimization.Subcase:
        ...
    def CloneAnalysisLoad(self, existingload: Features.TopologyOptimization.AnalysisLoad) -> Features.TopologyOptimization.AnalysisLoad:
        ...
    def CloneAnalysisConstraint(self, existingConstraint: Features.TopologyOptimization.AnalysisConstraint) -> Features.TopologyOptimization.AnalysisConstraint:
        ...
    AnalysisType: Features.TopologyOptimization.StudyBuilder.AnalysisOption
    OptimizationObjective: Features.TopologyOptimization.StudyBuilder.OptimizationObjectiveOption


class ShapeConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    DesignSpace: Features.TopologyOptimization.DesignSpace
    DraftAngle: Expression
    DraftDrawDirection: Direction
    DraftPartingFace: ScCollector
    DraftPartingObjectOptions: Features.TopologyOptimization.ShapeConstraintBuilder.DraftPartingObjectType
    DraftPartingPlane: Plane
    ExtrudeBiDirectionFlag: bool
    ExtrudeDirection: Direction
    FirstLimitPlane: Plane
    MaxOverhangAngle: Features.TopologyOptimization.ShapeConstraintBuilder.MaxOverhangAngleValue
    MaximumDiameter: Expression
    MaximumWallThickness: Expression
    MinimumDiameter: Expression
    MinimumWallThickness: Expression
    Name: str
    NumberOfSegments: int
    OverhangVector: Direction
    PlanarSymmetryInputMode: Features.TopologyOptimization.ShapeConstraintBuilder.PlanarSymmetryInputOption
    PlanarSymmetryPlane1: Plane
    PlanarSymmetryPlane2: Plane
    RotationalSymmetryAxis: Axis
    SecondLimitPlane: Plane
    SegmentLimitHelpAxis: Axis
    Type: Features.TopologyOptimization.ShapeConstraintBuilder.ConstraintType
    UserSetName: bool


    class PlanarSymmetryInputOption(enum.Enum):
        Segment = 0
        Whole = 1
    

    class MaxOverhangAngleValue(enum.Enum):
        Degrees27 = 0
        Degrees45 = 1
        Degrees65 = 2
    

    class DraftPartingObjectType(enum.Enum):
        SpecifiedPlane = 0
        SpecifiedFace = 1
        AutomaticFace = 2
    

    class ConstraintType(enum.Enum):
        PlanarSymmetry = 0
        RepeatedRotationalSymmetry = 1
        SegmentalRotationalSymmetry = 2
        ExtrudeAlongVector = 3
        DraftAngle = 4
        MinimumMemberSize = 5
        MaximumMemberSize = 6
        MinimumWallThickness = 7
        MaximumWallThickness = 8
        OverhangingGeometryPrevention = 9
        SelfSupporting = 10
    

class ShapeConstraint(NXObject):
    def __init__(self) -> None: ...


class SceneryBodyBuilder(Builder):
    def __init__(self) -> None: ...
    Bodies: SelectBodyList
    Material: Material
    SceneryBodyName: str


class SceneryBody(NXObject):
    def __init__(self) -> None: ...


class PostManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.TopologyOptimizationFeature) -> None: ...
    def CreateViewContourBuilder(self) -> Features.TopologyOptimization.ViewContourBuilder:
        ...
    def ShowContour(self) -> None:
        ...
    def HideContour(self) -> None:
        ...
    def CreateViewTabularResultBuilder(self) -> Features.TopologyOptimization.ViewTabularResultBuilder:
        ...
    def CreateViewXygraphBuilder(self) -> Features.TopologyOptimization.ViewXygraphBuilder:
        ...
    def IsContourShown(self) -> bool:
        ...
    def ExportAnimationToGif(self, fileName: str) -> None:
        ...
    def IsAnimationPlaying(self) -> bool:
        ...
    def CreateAnimationController(self) -> Features.TopologyOptimization.AnimationController:
        ...
    def Tag(self) -> Tag: ...



class OptimizationConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    DesignSpace: Features.TopologyOptimization.DesignSpace
    DisplacementLocation: Point
    DisplacementType: Features.TopologyOptimization.OptimizationConstraintBuilder.DisplacementOption
    DisplacementVector: Direction
    FirstFlexibleFrequency: Expression
    Mass: Expression
    MaxDisplacement: Expression
    MaxFirstFlexFrequency: Expression
    MaxPercentOfStress: Expression
    MaximumMass: Expression
    MaximumStressType: Features.TopologyOptimization.OptimizationConstraintBuilder.MaximumStressOption
    MinFirstFlexFrequency: Expression
    MinimumMass: Expression
    Name: str
    SelectFace: ScCollector
    Type: Features.TopologyOptimization.OptimizationConstraintBuilder.ConstraintType
    UserSetName: bool


    class MaximumStressOption(enum.Enum):
        UltimateTensileStrength = 0
        Yield = 1
    

    class DisplacementOption(enum.Enum):
        AbsoluteMagnitude = 0
        X = 1
        Y = 2
        Z = 3
        AlongVector = 4
    

    class ConstraintType(enum.Enum):
        MassTarget = 0
        MinimumMassLimit = 1
        MaximumMassLimit = 2
        MaximumStressLimit = 3
        MaximumDisplacementLimit = 4
        FirstFlexibleModeTarget = 5
        MinimumFirstFlexibleModeLimit = 6
        MaximumFirstFlexibleModeLimit = 7
    

class OptimizationConstraint(NXObject):
    def __init__(self) -> None: ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class DesignSpaceBuilder(Builder):
    def __init__(self) -> None: ...
    Material: Material
    Name: str
    SelectBody: SelectBody


class DesignSpace(NXObject):
    def __init__(self) -> None: ...
    def CreateConstructionBodyGroup(self, constructionBodies: typing.List[Features.TopologyOptimization.ConstructionBody]) -> Features.TopologyOptimization.ConstructionBodyCollector:
        ...
    def AddConstraint(self, constraintObjectTag: NXObject) -> None:
        ...
    def RemoveConstraint(self, constraintObjectTag: NXObject) -> None:
        ...


class Container(NXObject):
    def __init__(self) -> None: ...
    def GetMembers(self, members: typing.List[NXObject]) -> None:
        ...
    def Reorder(self, source: NXObject, target: NXObject, type: Features.TopologyOptimization.Container.ReorderType) -> None:
        ...


    class ReorderType(enum.Enum):
        Before = 0
        After = 1
        Into = 2
    

class ConstructionBodyCollector(NXObject):
    def __init__(self) -> None: ...
    def AddMember(self, bFromCollectorToCollector: bool, constructionBody: Features.TopologyOptimization.ConstructionBody) -> None:
        ...
    def RemoveMember(self, bFromCollectorToCollector: bool, constructionBody: Features.TopologyOptimization.ConstructionBody) -> None:
        ...
    def Ungroup(self) -> None:
        ...


class ConstructionBodyBuilder(Builder):
    def __init__(self) -> None: ...
    BlendRadius: Expression
    Bodies: SelectBodyList
    BodyCollector: ScCollector
    DesignSpace: Features.TopologyOptimization.DesignSpace
    GroupingOption: Features.TopologyOptimization.ConstructionBodyBuilder.GroupingType
    Method: Features.TopologyOptimization.ConstructionBodyBuilder.MethodOption
    Name: str
    Offset: Expression
    OffsetEdgesType: Features.TopologyOptimization.ConstructionBodyBuilder.OffsetType
    WallThickness: Expression


    class OffsetType(enum.Enum):
        None = 0
        WithRadius = 1
    

    class MethodOption(enum.Enum):
        KeepIn = 0
        KeepOut = 1
        Shell = 2
    

    class GroupingType(enum.Enum):
        Separate = 0
        Collection = 1
    

class ConstructionBody(NXObject):
    def __init__(self) -> None: ...


class ConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    ConnectionName: str
    SelectBody1: SelectBody
    SelectBody2: SelectBody
    SelectFaces1: ScCollector
    SelectFaces2: ScCollector
    ShellOffset1: Expression
    ShellOffset2: Expression
    Type: Features.TopologyOptimization.ConnectionBuilder.Types
    UserSetName: bool


    class Types(enum.Enum):
        BodyToBody = 0
        FaceToFace = 1
    

class Connection(NXObject):
    def __init__(self) -> None: ...


class AnimationController(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AnimateContour(self, animState: Features.TopologyOptimization.AnimationController.State) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    FullCycle: bool


    class State(enum.Enum):
        Play = 0
        Stop = 1
        Pause = 2
        Next = 3
        Previous = 4
    

class AnalysisLoadBuilder(Builder):
    def __init__(self) -> None: ...
    Acceleration: Expression
    BearingAngular: Expression
    FaceVector: Direction
    Force: Expression
    ForceType: Features.TopologyOptimization.AnalysisLoadBuilder.AnalysisLoadForceType
    ForceX: Expression
    ForceY: Expression
    ForceZ: Expression
    MaxDisplacement: Expression
    Name: str
    Pressure: Expression
    ReverseBearingLoadDirection: bool
    ReversePressureDirection: bool
    SelectFace: ScCollector
    Torque: Expression
    TorqueAxis: Axis
    Type: Features.TopologyOptimization.AnalysisLoadBuilder.AnalysisLoadType
    UserSetName: bool


    class AnalysisLoadType(enum.Enum):
        Force = 0
        BearingLoad = 1
        Pressure = 2
        Torque = 3
        Acceleration = 4
        EnforcedDisplacement = 5
    

    class AnalysisLoadForceType(enum.Enum):
        ByVector = 0
        ByComponent = 1
    

class AnalysisLoad(NXObject):
    def __init__(self) -> None: ...


class AnalysisConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    LinearSliderVector: Direction
    Name: str
    PinnedAxis: Axis
    PlanarSliderPlane: Plane
    SelectFace: ScCollector
    Type: Features.TopologyOptimization.AnalysisConstraintBuilder.ConstraintType
    UserSetName: bool


    class ConstraintType(enum.Enum):
        Fixed = 0
        Pinned = 1
        PinnedSlider = 2
        LinearSlider = 3
        PlanarSlider = 4
    

class AnalysisConstraint(NXObject):
    def __init__(self) -> None: ...


