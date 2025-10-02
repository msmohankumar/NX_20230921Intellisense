from ...NXOpen import *
from ..BodyDes import *

import typing
import enum

class OnestepUnformCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[BodyDes.OnestepUnformBuilder]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateOnestepBuilder(self, onestepunform: Features.Feature) -> BodyDes.OnestepUnformBuilder:
        ...
    def Tag(self) -> Tag: ...



class OnestepUnformBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def Mesh(self) -> None:
        ...
    def Calculation(self) -> None:
        ...
    def GetThickness(self, thickness: float) -> None:
        ...
    def Constructor(self, tOnestepSolverType: int) -> None:
        ...
    def Destructor(self) -> None:
        ...
    def GetSolverType(self) -> int:
        ...
    def SetDrawDirection(self, tdx: int, tdy: int, tdz: int) -> None:
        ...
    def SetBlankThickness(self, thickness: float) -> None:
        ...
    def GetRefNode(self) -> int:
        ...
    def SetSurfaceType(self, tOnestepSolverSurfaceType: int) -> None:
        ...
    def GetMinNodeID(self) -> int:
        ...
    def SetNodeIDsOnFreeEdge(self, index: int, nids: int) -> None:
        ...
    def GetNodeIdsOnFreeEdge(self, index: int, nodeIdentifications: int) -> None:
        ...
    def GetMeshes(self, vnode: float, constraintId: int, element: int) -> None:
        ...
    def GetBlankShape(self, nodes: float) -> None:
        ...
    def GetStrain(self, strains: float) -> None:
        ...
    def GetStress(self, stress: float) -> None:
        ...
    def GetSpringbackShape(self, nodes: float) -> None:
        ...
    def GetTopSurfaceStress(self, nodes: float) -> None:
        ...
    def GetTopSurfaceStrain(self, nodes: float) -> None:
        ...
    def GetBottomSurfaceStress(self, nodes: float) -> None:
        ...
    def GetBottomSurfaceStrain(self, nodes: float) -> None:
        ...
    def IsResultExist(self) -> None:
        ...
    def SetBorderInfo(self, edgeTags: typing.List[TaggedObject], nids: int, groupInfo: int) -> None:
        ...
    def UpdateInputMeshDataToSolver(self) -> None:
        ...
    def GetBorderLoops(self, index: int, nodeIdentifications: int) -> None:
        ...
    def OnestepUnformRegisterProjectCallback(self) -> None:
        ...
    def DisplayProfile(self, readResultFromFeature: bool) -> None:
        ...
    def CreateSheetBody(self, readResultFromFeature: bool) -> None:
        ...
    def SetResultThickness(self, thickness: float) -> None:
        ...
    def SetResultStrain(self, strain: float) -> None:
        ...
    def SetResultStress(self, stress: float) -> None:
        ...
    def SetResultSpringBack(self, springback: float) -> None:
        ...
    def SetResultBlankShape(self, blankshape: float) -> None:
        ...
    def SetResultNodesIdsOnProfile(self, nids: int) -> None:
        ...
    def SetResultNodesNumEachProfileCurve(self, indexs: int) -> None:
        ...
    def SetResultRefNodeId(self, resultRefNodeId: int) -> None:
        ...
    def SetConstraintInformation(self, noCommonEdges: bool, revisedDirU: int, revisedDirT: int, index: int, constraintType: int, cacNumsUnform: int, cacNumsTarget: int, consCurveFromUnform: typing.List[TaggedObject], consCurveFromTarget: typing.List[TaggedObject], consPointFromUnform: typing.List[Point], consPointFromTarget: typing.List[Point], startPtOfConsCrvsUnform: float, startPtOfConsCrvsTarget: float) -> None:
        ...
    def SetAdvancedConstraintInformation(self, advancedConstraintPartType: int, blankHolderWithAddendumBinderRegion: typing.List[TaggedObject], blankHolderWithoutAddendumBoundaryOfPart: typing.List[TaggedObject], blankHolderWithAddendumPressure: float, blankHolderWithAddendumForce: float, blankHolderWithoutAddendumTension: float, blankHolderWithoutAddendumForce: float, blankHolderWithoutAddendumForceStrength: float, drawbeadTag: typing.List[TaggedObject], drawbeadTtension: float, drawbeadNtension: float, drawbeadForceStrength: float) -> None:
        ...
    def GetContactNodeIds(self) -> int:
        ...
    def SetFacesOnOffsetSheet(self, unfoldBody: Body) -> bool:
        ...
    BinderRegion: ScCollector
    ConstraintType: BodyDes.OnestepUnformBuilder.Constraint
    ContactPointsTolerance: float
    DrawDirection: Direction
    Force: float
    ForceStrength: float
    InferElementSize: bool
    InferThickness: bool
    MatchPointOne: Point
    MatchPointThree: Point
    MatchPointTwo: Point
    MaterialPropertyDensity: float
    MaterialPropertyE: float
    MaterialPropertyF: float
    MaterialPropertyInitialStrain: float
    MaterialPropertyK: float
    MaterialPropertyN: float
    MaterialPropertyPoisson: float
    MaterialPropertyR0: float
    MaterialPropertyR45: float
    MaterialPropertyR90: float
    MaterialPropertyYieldStress: float
    MeshAttemptMapping: bool
    MeshElementSize: float
    MeshElementType: BodyDes.OnestepUnformBuilder.MeshElement
    MeshMaxJacobian: float
    MeshMaxWarp: float
    MeshProcessFillet: bool
    MeshSizeVariation: int
    MeshSmallFeature: float
    MeshSplitQuad: bool
    ObjectType: BodyDes.OnestepUnformBuilder.Object
    PartBoundary: ScCollector
    PartType: BodyDes.OnestepUnformBuilder.Part
    Pressure: float
    ProcessType: BodyDes.OnestepUnformBuilder.Process
    ReportDisplayFlattenShape: bool
    ReportDisplaySpringback: bool
    ReportDisplayStrain: bool
    ReportDisplayStress: bool
    ReportDisplayThickness: bool
    ReportDisplayViewControl: bool
    ReverseSide: bool
    SolverConvergencyLevel: BodyDes.OnestepUnformBuilder.Convergency
    SolverDisplaySpringbackMode: BodyDes.OnestepUnformBuilder.DisplaySpringbackMode
    SolverDoSpringbackCalculation: bool
    SolverJoinOutputCurves: bool
    SolverMaxIterationSteps: int
    SolverSaveAnalysisResultsIntoFeature: bool
    SurfaceType: BodyDes.OnestepUnformBuilder.Surface
    TargetRegion: ScCollector
    Thickness: float
    ThicknessDirection: Direction
    TrimlinePoint: Point
    UnfoldModeType: BodyDes.OnestepUnformBuilder.UnfoldMode
    UnfoldSolid: Body
    UnfoldSolidRegion: SelectBodyList
    UnformRegion: ScCollector
    UnformSection: Section


    class UnfoldMode(enum.Enum):
        Complete = 0
        Intermediate = 1
        Trimline = 2
        Unknown = 3
    

    class Surface(enum.Enum):
        Inner = 0
        Middle = 1
        Outer = 2
    

    class Process(enum.Enum):
        EntireUnform = 0
        IntermediateUnform = 1
        AdvancedUnform = 2
        TrimLine = 3
    

    class Part(enum.Enum):
        WithAddendum = 0
        WithoutAddendum = 1
    

    class Object(enum.Enum):
        Solid = 0
        Face = 1
    

    class MeshElement(enum.Enum):
        Triangle = 0
        Quadrate = 1
    

    class DisplaySpringbackMode(enum.Enum):
        Displacement = 0
        Alongx = 1
        Alongy = 2
        Alongz = 3
    

    class Convergency(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
    

    class Constraint(enum.Enum):
        CurveToCurve = 0
        PointToPoint = 1
        CurveAlongCurve = 2
    

class OnestepUnform(Features.Feature):
    def __init__(self) -> None: ...


