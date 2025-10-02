from ....NXOpen import *
from ...CAE import *
from ..Optimization import *

import typing
import enum

class TBSTopologySensitivityOptimizationParameters(CAE.Optimization.TBSOptimizationParameters):
    def __init__(self) -> None: ...
    DensityMove: float
    DensityUpdateOption: CAE.Optimization.TBSTopologySensitivityOptimizationParameters.DensityUpdate
    EigenvalueParameters: CAE.Optimization.TBSEigenvalueOptimizationParameters
    FilterRadius: Expression
    MaterialInterpolationOption: CAE.Optimization.TBSTopologySensitivityOptimizationParameters.MaterialInterpolation


    class MaterialInterpolation(enum.Enum):
        Simp = 0
        Ramp = 1
    

    class DensityUpdate(enum.Enum):
        Normal = 0
        Conservative = 1
        Agressive = 2
    

class TBSTopologyRestrictAreaBuilder(CAE.Optimization.TBSRestrictAreaBuilder):
    def __init__(self) -> None: ...
    CastCondition: CAE.Optimization.TBSCastCondition
    CheckingElementGroup: CAE.Optimization.TBSGroupDefinition
    CheckingType: CAE.Optimization.TBSTopologyRestrictAreaBuilder.CheckTypeOption
    Distance: Expression
    LinkCondition: CAE.Optimization.TBSTopologyLinkCondition
    MinimumThickness: Expression
    Radius: Expression
    Thickness: Expression


    class CheckTypeOption(enum.Enum):
        Frozen = 0
        LinkTopo = 1
        MaximumsSize = 2
        MinimumSize = 3
        Cast = 4
    

class TBSTopologyRestrictArea(CAE.Optimization.TBSRestrictArea):
    def __init__(self) -> None: ...


class TBSTopologyOptimizationSolutionBuilder(CAE.Optimization.TBSOptimizationSolutionBuilder):
    def __init__(self) -> None: ...


class TBSTopologyOptimizationSolution(CAE.Optimization.TBSOptimizationSolution):
    def __init__(self) -> None: ...


class TBSTopologyLinkCondition(TaggedObject):
    def __init__(self) -> None: ...
    Axis: CAE.Optimization.TBSTopologyLinkCondition.AxisType
    IgnoreFrozen: bool
    ReferenceCoordinateSystem: CoordinateSystem
    SymmetryType: CAE.Optimization.TBSTopologyLinkCondition.SymmetryOption
    TranslationAmount: int


    class SymmetryOption(enum.Enum):
        PlaneSymmetry = 0
        CyclicSymmetry = 1
    

    class AxisType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

class TBSTopologyControllerOptimizationParameters(CAE.Optimization.TBSOptimizationParameters):
    def __init__(self) -> None: ...
    AutomaticFrozenOption: CAE.Optimization.TBSTopologyControllerOptimizationParameters.AutoFrozen
    IterationNumbers: int
    SpeedOption: CAE.Optimization.TBSTopologyControllerOptimizationParameters.Speed
    StartDeleteVolume: float
    VolumeDefinitionOption: CAE.Optimization.TBSTopologyControllerOptimizationParameters.VolumeDefinitionMethod


    class VolumeDefinitionMethod(enum.Enum):
        Percent = 0
        Absolute = 1
    

    class Speed(enum.Enum):
        VerySlow = 0
        Slow = 1
        Moderate = 2
        Medium = 3
        Fast = 4
        Iteration = 5
    

    class AutoFrozen(enum.Enum):
        Load = 0
        Off = 1
        Spc = 2
        Both = 3
    

class TBSTestFunction(NXObject):
    def __init__(self) -> None: ...
    MaximumDisplacement: Expression
    NumberOfIncrements: int
    RunTest: bool
    TestDirectionOption: CAE.Optimization.TBSTestFunction.Direction


    class Direction(enum.Enum):
        Grow = 0
        Shrink = 1
        Random = 2
    

class TBSStopCondition(TaggedObject):
    def __init__(self) -> None: ...
    MaximumIterationNumber: int


class TBSSmoothCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.TBSSmooth]:
        ...
    def __init__(self, owner: CAE.Optimization.TBSOptimizationSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, smoothName: str) -> CAE.Optimization.TBSSmooth:
        ...
    def Tag(self) -> Tag: ...



class TBSSmoothBuilder(Builder):
    def __init__(self) -> None: ...
    def GetFormatOption(self) -> typing.List[CAE.Optimization.TBSSmoothBuilder.Format]:
        ...
    def SetFormatOption(self, formatOption: typing.List[CAE.Optimization.TBSSmoothBuilder.Format]) -> None:
        ...
    Border: bool
    ComponentLimitingSize: Expression
    IsoTypeOption: CAE.Optimization.TBSSmoothBuilder.IsoType
    IsoValue: float
    MinimumAngle: Expression
    MixedMesh: bool
    NameDescription: CAE.Optimization.NameDescription
    OriginalSurfaceSmooth: CAE.Optimization.TBSSmoothBuilder.OriginalSurfaceSmoothingOption
    ReductionAngle: Expression
    ReductionRate: float
    ResultFilteringOption: CAE.Optimization.TBSSmoothBuilder.ResultFiltering
    SelfIntersectionChecking: CAE.Optimization.TBSSmoothBuilder.SelfIntersectionCheckingOption
    SliceFormat: CAE.Optimization.TBSSmoothBuilder.SliceFormatOption
    SliceNormalVector: Direction
    SliceNumber: int
    SmoothArea: CAE.Optimization.TBSGroupDefinition
    SmoothCycles: int
    TargetVolume: float
    UseAdditionalParameters: bool


    class SliceFormatOption(enum.Enum):
        IgsPolygon = 0
        IgsCurves = 1
        Cli = 2
        All = 3
    

    class SelfIntersectionCheckingOption(enum.Enum):
        Off = 0
        Check = 1
        Runtime = 2
        Iterative = 3
    

    class ResultFiltering(enum.Enum):
        Off = 0
        Moderate = 1
        Full = 2
    

    class OriginalSurfaceSmoothingOption(enum.Enum):
        Off = 0
        Shrink = 1
        Full = 2
    

    class IsoType(enum.Enum):
        Original = 0
        New = 1
        Both = 2
    

    class Format(enum.Enum):
        Bdf = 0
        Stl = 1
        Iges = 2
    

class TBSSmooth(NXObject):
    def __init__(self) -> None: ...
    def Execute(self) -> None:
        ...
    def Rename(self, name: str, renameResults: bool) -> None:
        ...
    def GetResults(self) -> str:
        ...
    def Destroy(self, deleteResult: bool) -> None:
        ...


class TBSSingleObjective(TaggedObject):
    def __init__(self) -> None: ...
    DesignResponse: CAE.Optimization.TBSDesignResponse
    ReferenceValue: float
    Weight: float


class TBSShapeRestrictAreaBuilder(CAE.Optimization.TBSRestrictAreaBuilder):
    def __init__(self) -> None: ...
    ActLinkConditionButton: CAE.Optimization.TBSShapeLinkCondition
    CheckBoundaryCondition: bool
    CheckDof: bool
    CheckElementGroup: bool
    CheckLinkCondition: bool
    CheckMaximumGrowValue: bool
    CheckMaximumShrinkValue: bool
    CheckedElements: CAE.Optimization.TBSGroupDefinition
    DofSettings: CAE.Optimization.TBSCheckDOF
    MaximumGrowValue: Expression
    MaximumShrinkValue: Expression
    RestrictedNodes: CAE.Optimization.TBSGroupDefinition


class TBSShapeRestrictArea(CAE.Optimization.TBSRestrictArea):
    def __init__(self) -> None: ...


class TBSShapeOptimizationSolutionBuilder(CAE.Optimization.TBSOptimizationSolutionBuilder):
    def __init__(self) -> None: ...


class TBSShapeOptimizationSolution(CAE.Optimization.TBSOptimizationSolution):
    def __init__(self) -> None: ...
    def SolveTest(self) -> None:
        ...
    def GetTestResultFile(self) -> str:
        ...
    MeshSmooth: CAE.Optimization.TBSMeshSmooth
    TestFunction: CAE.Optimization.TBSTestFunction


class TBSShapeOptimizationParameters(CAE.Optimization.TBSOptimizationParameters):
    def __init__(self) -> None: ...
    DisplacementStepSize: CAE.Optimization.TBSShapeOptimizationParameters.DisplacementStepsize
    Scale: float


    class DisplacementStepsize(enum.Enum):
        Minimum = 0
        Average = 1
    

class TBSShapeLinkCondition(TaggedObject):
    def __init__(self) -> None: ...
    Angle: Expression
    DemoldGroup: CAE.Optimization.TBSGroupDefinition
    Direction: Direction
    ManufacturingType: CAE.Optimization.TBSShapeLinkCondition.ManufacturingOption
    SymmetryPlane: Plane
    Tolerance: Expression
    UndercutTolerance: Expression
    UseCylindricalCsys: bool
    UseSplineToDefineSurface: bool


    class ManufacturingOption(enum.Enum):
        PlaneSymmetry = 0
        RotationSymmetry = 1
        SurfaceStamp = 2
        SurfaceTurn = 3
        SurfaceDrill = 4
        SurfaceDemold = 5
    

class TBSRestrictAreaCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.TBSRestrictArea]:
        ...
    def __init__(self, owner: CAE.Optimization.TBSOptimizationSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.Optimization.TBSRestrictArea:
        ...
    def Tag(self) -> Tag: ...



class TBSRestrictAreaBuilder(Builder):
    def __init__(self) -> None: ...
    NameDescription: CAE.Optimization.NameDescription


class TBSRestrictArea(NXObject):
    def __init__(self) -> None: ...


class TBSOutputControlOptions(TaggedObject):
    def __init__(self) -> None: ...
    CustomScratchDirectory: str
    HasCustomScratchDirectory: bool
    IsJobRunInForeground: bool
    Op2OutputOption: CAE.Optimization.TBSOutputControlOptions.Op2Option


    class Op2Option(enum.Enum):
        None = 0
        FirstLast = 1
        All = 2
    

class TBSOptimizationSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.TBSOptimizationSolution]:
        ...
    def __init__(self, owner: CAE.Optimization.TBSOptimizationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, solutionName: str) -> CAE.Optimization.TBSOptimizationSolution:
        ...
    def CloneSolution(self, sourceSolution: CAE.Optimization.TBSOptimizationSolution, cloneResult: bool) -> CAE.Optimization.TBSOptimizationSolution:
        ...
    def Tag(self) -> Tag: ...



class TBSOptimizationSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    NameDescription: CAE.Optimization.NameDescription
    ReferencedSolution: CAE.SimSolution
    Strategy: CAE.Optimization.TBSOptimizationSolutionBuilder.StrategyType


    class StrategyType(enum.Enum):
        Sensitivity = 0
        Controller = 1
    

class TBSOptimizationSolution(NXObject):
    def __init__(self) -> None: ...
    def Solve(self) -> None:
        ...
    def GetIterationNumber(self) -> int:
        ...
    def GetPostResult(self, iterationID: int, postResultName: str) -> CAE.Optimization.TBSOptimizationSolution.ResultStatus:
        ...
    def GetSmoothResult(self, smooth: CAE.Optimization.TBSSmooth, smoothResultName: str) -> CAE.Optimization.TBSOptimizationSolution.ResultStatus:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.CAE.Optimization.TBSSmooth.GetResults instead.")"""
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def Rename(self, name: str, renameResults: bool) -> None:
        ...
    def Destroy(self, deleteResult: bool) -> None:
        ...
    RestrictAreas: CAE.Optimization.TBSRestrictAreaCollection
    Constraints: CAE.Optimization.TBSConstraintCollection
    DesignVariables: CAE.Optimization.TBSDesignVariableCollection
    Smoothings: CAE.Optimization.TBSSmoothCollection
    ControlParameters: CAE.Optimization.TBSOptimizationParameters
    DesignArea: CAE.Optimization.TBSDesignArea
    Objectives: CAE.Optimization.TBSObjectives
    OutputControlOptions: CAE.Optimization.TBSOutputControlOptions
    StopCondition: CAE.Optimization.TBSStopCondition


    class ResultStatus(enum.Enum):
        Valid = 0
        OutOfDate = 1
        Invalid = 2
    

class TBSOptimizationParameters(TaggedObject):
    def __init__(self) -> None: ...


class TBSOptimizationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def CreateTopologyOptimizationSolutionBuilder(self, topoSolution: CAE.Optimization.TBSTopologyOptimizationSolution) -> CAE.Optimization.TBSTopologyOptimizationSolutionBuilder:
        ...
    def CreateShapeOptimizationSolutionBuilder(self, shapeSolution: CAE.Optimization.TBSShapeOptimizationSolution) -> CAE.Optimization.TBSShapeOptimizationSolutionBuilder:
        ...
    def CreateDesignVariableBuilder(self, designVariable: CAE.Optimization.TBSDesignVariable) -> CAE.Optimization.TBSDesignVariableBuilder:
        ...
    def CreateDesignResponseBuilder(self, designResponse: CAE.Optimization.TBSDesignResponse) -> CAE.Optimization.TBSDesignResponseBuilder:
        ...
    def CreateResponseConstraintBuilder(self, responseConstraint: CAE.Optimization.TBSConstraint) -> CAE.Optimization.TBSConstraintBuilder:
        ...
    def CreateTopologyRestrictAreaBuilder(self, restrictArea: CAE.Optimization.TBSTopologyRestrictArea) -> CAE.Optimization.TBSTopologyRestrictAreaBuilder:
        ...
    def CreateShapeRestrictAreaBuilder(self, restrictArea: CAE.Optimization.TBSShapeRestrictArea) -> CAE.Optimization.TBSShapeRestrictAreaBuilder:
        ...
    def CreateSmoothBuilder(self, smooth: CAE.Optimization.TBSSmooth) -> CAE.Optimization.TBSSmoothBuilder:
        ...
    def CreateSingleObjective(self, designResponse: CAE.Optimization.TBSDesignResponse, weight: float, referenceValue: float) -> CAE.Optimization.TBSSingleObjective:
        ...
    def CreateLoadCase(self) -> CAE.Optimization.TBSLoadCase:
        ...
    def Tag(self) -> Tag: ...

    OptimizationSolutions: CAE.Optimization.TBSOptimizationSolutionCollection


class TBSObjectives(TaggedObject):
    def __init__(self) -> None: ...
    def GetObjectives(self) -> typing.List[CAE.Optimization.TBSSingleObjective]:
        ...
    def SetObjectives(self, objectives: typing.List[CAE.Optimization.TBSSingleObjective]) -> None:
        ...
    def AddObjectives(self, objectives: typing.List[CAE.Optimization.TBSSingleObjective]) -> None:
        ...
    def RemoveObjectives(self, objectives: typing.List[CAE.Optimization.TBSSingleObjective], deleteObject: bool) -> None:
        ...
    TargetObjective: CAE.Optimization.TBSObjectives.ObjectiveType


    class ObjectiveType(enum.Enum):
        Minimum = 0
        Maximum = 1
        MaxMin = 2
    

class TBSMeshSmooth(NXObject):
    def __init__(self) -> None: ...
    FixSurfaceNodes: bool
    MeshSmoothElements: CAE.Optimization.TBSGroupDefinition
    MeshSmoothStrategy: CAE.Optimization.TBSMeshSmooth.Strategy
    UseHighestQuality: bool


    class Strategy(enum.Enum):
        ConstrainedLaplacian = 0
        LocalGradient = 1
    

class TBSLoadCaseManager(TaggedObject):
    def __init__(self) -> None: ...
    def GetLoadCases(self) -> typing.List[CAE.Optimization.TBSLoadCase]:
        ...
    def SetLoadCases(self, loadCases: typing.List[CAE.Optimization.TBSLoadCase]) -> None:
        ...
    def AddLoadCases(self, loadCases: typing.List[CAE.Optimization.TBSLoadCase]) -> None:
        ...
    def RemoveLoadCases(self, loadCases: typing.List[CAE.Optimization.TBSLoadCase], deleteLoadCase: bool) -> None:
        ...
    SelectionOption: CAE.Optimization.TBSLoadCaseManager.SelectionType


    class SelectionType(enum.Enum):
        Maximum = 0
        Minimum = 1
        Sum = 2
    

class TBSLoadCase(TaggedObject):
    def __init__(self) -> None: ...
    def GetSubcase(self, subcaseId: int) -> bool:
        ...
    def SetSubcase(self, allSubcases: bool, subcaseId: int) -> None:
        ...
    def GetSubstep(self, subSteps: int) -> bool:
        ...
    def SetSubstep(self, allSubSteps: bool, subSteps: int) -> None:
        ...
    ShellLayer: CAE.Optimization.TBSLoadCase.LayerOption


    class LayerOption(enum.Enum):
        None = 0
        Maximum = 1
        Minimum = 2
        Top = 3
        Middle = 4
        Bottom = 5
    

class TBSIOptimizationTest():
    def SolveTest(self) -> None:
        ...
    def GetTestResultFile(self) -> str:
        ...


class TBSGroupDefinition(TaggedObject):
    def __init__(self) -> None: ...
    def GetElementType(self) -> CAE.Optimization.TBSGroupDefinition.GroupElementType:
        ...
    Definition: CAE.Optimization.TBSGroupDefinition.DefinitionType
    TargetSet: CAE.SetManager


    class GroupElementType(enum.Enum):
        Element = 0
        Node = 1
    

    class DefinitionType(enum.Enum):
        All = 0
        Selected = 1
        DesignArea = 2
        MeshSmoothingArea = 3
    

class TBSEigenvalueOptimizationParameters(TaggedObject):
    def __init__(self) -> None: ...
    ModeNumber: int
    TrackingMode: bool
    TrackingNodes: CAE.Optimization.TBSGroupDefinition


class TBSDesignVariableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.TBSDesignVariable]:
        ...
    def __init__(self, owner: CAE.Optimization.TBSOptimizationSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, variableName: str) -> CAE.Optimization.TBSDesignVariable:
        ...
    def Tag(self) -> Tag: ...



class TBSDesignVariableBuilder(CAE.Optimization.TBSBaseDesignVariableBuilder):
    def __init__(self) -> None: ...


class TBSDesignVariable(NXObject):
    def __init__(self) -> None: ...


class TBSDesignResponseBuilder(CAE.Optimization.TBSBaseDesignVariableBuilder):
    def __init__(self) -> None: ...
    VariableType: CAE.Optimization.TBSDesignResponseBuilder.Response


    class Response(enum.Enum):
        DynamicFrequency = 0
        DynamicFrequencyKressissel = 1
        Volume = 2
        VolumeFill = 3
        Weight = 4
        DisplacementAbsolute = 5
        DisplacementX = 6
        DisplacementY = 7
        DisplacementZ = 8
        DisplacementXAbsolute = 9
        DisplacementYAbsolute = 10
        DisplacementZAbsolute = 11
        RotationAbsolute = 12
        RotationX = 13
        RotationY = 14
        RotationZ = 15
        RotationXAbsolute = 16
        RotationYAbsolute = 17
        RotationZAbsolute = 18
        StrainEnergy = 19
        CenterGravityX = 20
        CenterGravityY = 21
        CenterGravityZ = 22
        InertiaXx = 23
        InertiaXy = 24
        InertiaXz = 25
        InertiaYy = 26
        InertiaYz = 27
        InertiaZz = 28
        ReactionForceAbsolute = 29
        ReactionForceX = 30
        ReactionForceY = 31
        ReactionForceZ = 32
        ReactionForceXAbsolute = 33
        ReactionForceYAbsolute = 34
        ReactionForceZAbsolute = 35
        ReactionForceRotationAbsolute = 36
        ReactionForceRotationX = 37
        ReactionForceRotationY = 38
        ReactionForceRotationZ = 39
        ReactionForceRotationXAbsolute = 40
        ReactionForceRotationYAbsolute = 41
        ReactionForceRotationZAbsolute = 42
        InternalForceAbsolute = 43
        InternalForceX = 44
        InternalForceY = 45
        InternalForceZ = 46
        InternalForceXAbsolute = 47
        InternalForceYAbsolute = 48
        InternalForceZAbsolute = 49
        InternalForceRotationAbsolute = 50
        InternalForceRotationX = 51
        InternalForceRotationY = 52
        InternalForceRotationZ = 53
        InternalForceRotationXAbsolute = 54
        InternalForceRotationYAbsolute = 55
        InternalForceRotationZAbsolute = 56
        FrequencyResponseAccelerationX = 57
        FrequencyResponseAccelerationY = 58
        FrequencyResponseAccelerationZ = 59
        FrequencyResponseCompliance = 60
        FrequencyResponseDbaPressure = 61
        FrequencyResponseDbPressure = 62
        FrequencyResponseDisplacementAbsolute = 63
        FrequencyResponseDisplacementXAbsolute = 64
        FrequencyResponseDisplacementYAbsolute = 65
        FrequencyResponseDisplacementZAbsolute = 66
        FrequencyResponsePhaseXAbsolute = 67
        FrequencyResponsePhaseYAbsolute = 68
        FrequencyResponsePhaseZAbsolute = 69
        FrequencyResponsePressure = 70
        FrequencyResponseRmsPressure = 71
        FrequencyResponseVelocityXAbsolute = 72
        FrequencyResponseVelocityYAbsolute = 73
        FrequencyResponseVelocityZAbsolute = 74
        FrequencyResponseNvhSolid = 75
        FrequencyResponseNvhShell = 76
        MisesStressHypothesis = 77
        MaximumPrincipalStress = 78
        MinimumAbsolutePrincipalStress = 79
        MaximumAbsolutePrincipalStress = 80
    

class TBSDesignResponse(CAE.Optimization.TBSDesignVariable):
    def __init__(self) -> None: ...


class TBSDesignArea(NXObject):
    def __init__(self) -> None: ...
    DesignElements: CAE.Optimization.TBSGroupDefinition


class TBSConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.TBSConstraint]:
        ...
    def __init__(self, owner: CAE.Optimization.TBSOptimizationSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, constraintName: str) -> CAE.Optimization.TBSConstraint:
        ...
    def Tag(self) -> Tag: ...



class TBSConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    ConstraintType: CAE.Optimization.TBSConstraintBuilder.ConstraintOption
    ConstraintValue: Expression
    DesignResponse: CAE.Optimization.TBSDesignResponse
    Magnitude: CAE.Optimization.TBSConstraintBuilder.MagnitudeType
    NameDescription: CAE.Optimization.NameDescription


    class MagnitudeType(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class ConstraintOption(enum.Enum):
        Eq = 0
        Lt = 1
        Gt = 2
    

class TBSConstraint(NXObject):
    def __init__(self) -> None: ...


class TBSCheckDOF(NXObject):
    def __init__(self) -> None: ...
    Dofs: CAE.Optimization.TBSCheckDOF.DofSettings
    ReferencedCoordinateSystem: CoordinateSystem


    class TBSCheckDOFDofSettings():
        Dof1: CAE.Optimization.TBSCheckDOF.CheckDofOption
        Dof2: CAE.Optimization.TBSCheckDOF.CheckDofOption
        Dof3: CAE.Optimization.TBSCheckDOF.CheckDofOption
        def ToString(self) -> str:
            ...
        def __init__(self, Dof1: CAE.Optimization.TBSCheckDOF.CheckDofOption, Dof2: CAE.Optimization.TBSCheckDOF.CheckDofOption, Dof3: CAE.Optimization.TBSCheckDOF.CheckDofOption) -> None: ...
    

    class CheckDofOption(enum.Enum):
        Fix = 0
        Free = 1
    

class TBSCastCondition(TaggedObject):
    def __init__(self) -> None: ...
    CheckingGroup: CAE.Optimization.TBSGroupDefinition
    DraftAngle: Expression
    MiddlePlane: CAE.Optimization.TBSCastCondition.MiddlePlaneType
    MiddlePlanePoint: Point
    PullCoordinateSystem: CoordinateSystem
    PullDirection: Direction
    Radius: Expression


    class MiddlePlaneType(enum.Enum):
        None = 0
        Automatic = 1
        AutomaticTight = 2
        Point = 3
        Surface = 4
        Stamp = 5
    

class TBSBaseDesignVariableBuilder(Builder):
    def __init__(self) -> None: ...
    DesignElements: CAE.Optimization.TBSGroupDefinition
    DesignNodes: CAE.Optimization.TBSGroupDefinition
    GroupOperatorOption: CAE.Optimization.TBSBaseDesignVariableBuilder.GroupOperator
    LoadCases: CAE.Optimization.TBSLoadCaseManager
    NameDescription: CAE.Optimization.NameDescription
    ReferenceCoordinateSystem: CoordinateSystem
    SelectionAreaType: CAE.Optimization.TBSGroupDefinition.GroupElementType


    class GroupOperator(enum.Enum):
        Max = 0
        Min = 1
        Sum = 2
        Count = 3
        Deviation = 4
    

class Solver(enum.Enum):
    Optimization = 0
    GlobalSensitivity = 1
    AltairHyperOpt = 2


class Response(enum.Enum):
    None = 0
    Weight = 1
    Volume = 2
    Frequency = 3
    Temperature = 4
    StressVonMises = 5
    StrainVonMises = 6
    TranslationX = 7
    TranslationY = 8
    TranslationZ = 9
    RotationX = 10
    RotationY = 11
    RotationZ = 12
    Stress2DMaximumShear = 13
    Stress2DMajorPrincipal = 14
    Stress2DMinorPrincipal = 15
    Stress2DVonMises = 16
    Stress2DMaximumShearBottom = 17
    Stress2DMajorPrincipalBottom = 18
    Stress2DMinorPrincipalBottom = 19
    Stress2DVonMisesBottom = 20
    Strain2DMaximumShear = 21
    Strain2DMajorPrincipal = 22
    Strain2DMinorPrincipal = 23
    Strain2DVonMises = 24
    Strain2DMaximumShearBottom = 25
    Strain2DMajorPrincipalBottom = 26
    Strain2DMinorPrincipalBottom = 27
    Strain2DVonMisesBottom = 28
    Stress1DVonMisesStressRecoveryPointC = 29
    Stress1DVonMisesStressRecoveryPointD = 30
    Stress1DVonMisesStressRecoveryPointE = 31
    Stress1DVonMisesStressRecoveryPointF = 32
    Stress1DVonMisesMaximum = 33
    Stress1DVonMisesMinimum = 34
    Strain1DVonMisesStressRecoveryPointC = 35
    Strain1DVonMisesStressRecoveryPointD = 36
    Strain1DVonMisesStressRecoveryPointE = 37
    Strain1DVonMisesStressRecoveryPointF = 38
    Strain1DVonMisesMaximum = 39
    Strain1DVonMisesMinimum = 40
    Stress3DFirstPrincipal = 41
    Stress3DSecondPrincipal = 42
    Stress3DThirdPrincipal = 43
    Stress3DVonMises = 44
    Strain3DFirstPrincipal = 45
    Strain3DSecondPrincipal = 46
    Strain3DThirdPrincipal = 47
    Strain3DVonMises = 48
    ResultMeasure = 49


class NameDescription(TaggedObject):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    Name: str


class Limit(enum.Enum):
    Upper = 0
    Lower = 1


class Hookes(enum.Enum):
    Top = 0
    Bottom = 1
    Middle = 2
    Minimum = 3
    Maximum = 4


class Goal(enum.Enum):
    Minimum = 0
    Maximum = 1
    Target = 2


class Geometry(enum.Enum):
    Body = 0
    Face = 1
    Edge = 2
    Point = 3
    Curve = 4


class DAOStopCondition(NXObject):
    def __init__(self) -> None: ...
    AbsoluteConvergence: float
    ConstraintChecking: bool
    MaxConstraintViolation: float
    MaxIterations: int
    PerturbationFraction: float
    RelativeConvergence: float
    SaveAllIterationResults: bool


class DAOSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.DAOSolution]:
        ...
    def __init__(self, owner: CAE.Optimization.DAOOptimizationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateOptimizationBuilder(self, optimizationSolution: CAE.Optimization.DAOSolution) -> CAE.Optimization.DAOSolutionBuilder:
        ...
    def FindObject(self, solutionName: str) -> CAE.Optimization.DAOSolution:
        ...
    def CreateConstraintBuilder(self, designConstraint: CAE.Optimization.DAOConstraint) -> CAE.Optimization.DAOConstraintBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.CAE.Optimization.DAOSolution.CreateConstraintBuilder instead.")"""
        ...
    def CreateDesignVariableBuilder(self, designVariable: CAE.Optimization.DAODesignVariable) -> CAE.Optimization.DAODesignVariableBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.CAE.Optimization.DAOSolution.CreateDesignVariableBuilder instead.")"""
        ...
    def Tag(self) -> Tag: ...



class DAOSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    AnalysisSolution: CAE.SimSolution
    Name: str
    SolverType: CAE.Optimization.Solver


class DAOSolution(NXObject):
    def __init__(self) -> None: ...
    def GetDesignObjective(self) -> CAE.Optimization.DAOObjective:
        ...
    def GetDesignConstraints(self) -> typing.List[CAE.Optimization.DAOConstraint]:
        ...
    def SetDesignConstraints(self, designConstraints: typing.List[CAE.Optimization.DAOConstraint]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Not a valid method. Use NXOpen.CAE.Optimization.DAOSolution.CreateConstraintBuilder instead.")"""
        ...
    def GetOptimizationDesignVariables(self) -> typing.List[CAE.Optimization.DAODesignVariable]:
        ...
    def SetOptimizationDesignVariables(self, designVariables: typing.List[CAE.Optimization.DAOConstraint]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Not a valid method. Use NXOpen.CAE.Optimization.DAOSolution.CreateDesignVariableBuilder instead.")"""
        ...
    def GetGlobalSensitivityDesignVariables(self) -> typing.List[CAE.Optimization.DAODesignVariable]:
        ...
    def SetGlobalSensitivityDesignVariables(self, designVariables: typing.List[CAE.Optimization.DAODesignVariable]) -> None:
        ...
    def GetSolutionControls(self) -> CAE.Optimization.DAOStopCondition:
        ...
    def Solve(self) -> None:
        ...
    def DeleteSolution(self) -> None:
        ...
    def ActivateSolution(self) -> None:
        ...
    def CreateConstraintBuilder(self, optimizationConstraint: CAE.Optimization.DAOConstraint) -> CAE.Optimization.DAOConstraintBuilder:
        ...
    def CreateDesignVariableBuilder(self, optimizationDesvar: CAE.Optimization.DAODesignVariable) -> CAE.Optimization.DAODesignVariableBuilder:
        ...
    DesignConstraint: CAE.Optimization.DAOConstraintCollection
    DesignVariable: CAE.Optimization.DAODesignVariableCollection
    Name: str
    OptimizerControl: CAE.Optimization.DAOStopCondition
    SolverType: CAE.Optimization.Solver


class DAOOptimizationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def Tag(self) -> Tag: ...

    OptimizationSolution: CAE.Optimization.DAOSolutionCollection


class DAOObjective(NXObject):
    def __init__(self) -> None: ...
    def GetGeometry(self) -> typing.List[DisplayableObject]:
        ...
    def SetGeometry(self, geometry: typing.List[DisplayableObject]) -> None:
        ...
    def GetNumberResultGroup(self) -> int:
        ...
    def GetResults(self, resultGroupIndex: int) -> float:
        ...
    CategoryType: CAE.Optimization.Category
    GeometryType: CAE.Optimization.Geometry
    LoadCase: int
    ModeNumber: int
    ObjectiveGoal: CAE.Optimization.Goal
    Response: CAE.Optimization.Response
    ResultMeasure: CAE.ResultMeasure
    TargetUnit: Unit
    TargetValue: float


class DAODesignVariableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.DAODesignVariable]:
        ...
    def __init__(self, owner: CAE.Optimization.DAOSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, designVariableName: str) -> CAE.Optimization.DAODesignVariable:
        ...
    def Tag(self) -> Tag: ...



class DAODesignVariableBuilder(Builder):
    def __init__(self) -> None: ...
    def GetVariable(self, variableType: CAE.Optimization.DAODesignVariableBuilder.Variable, variableExpression: Expression) -> None:
        ...
    def SetVariable(self, variableType: CAE.Optimization.DAODesignVariableBuilder.Variable, variableExpression: Expression) -> None:
        ...
    GlobalSensitivityFlag: bool
    LowerLimit: float
    Name: str
    UpperLimit: float


    class Variable(enum.Enum):
        SectionProperty = 0
        ShellProperty = 1
        FeatureDimension = 2
        SketchDimension = 3
        AllExpressions = 4
        Count = 5
    

class DAODesignVariable(NXObject):
    def __init__(self) -> None: ...
    def GetResults(self) -> float:
        ...


class DAOConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Optimization.DAOConstraint]:
        ...
    def __init__(self, owner: CAE.Optimization.DAOSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, designConstraintName: str) -> CAE.Optimization.DAOConstraint:
        ...
    def Tag(self) -> Tag: ...



class DAOConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    def GetGeometry(self) -> typing.List[DisplayableObject]:
        ...
    def SetGeometry(self, geometry: typing.List[DisplayableObject]) -> None:
        ...
    CategoryType: CAE.Optimization.Category
    GeometryType: CAE.Optimization.Geometry
    LimitType: CAE.Optimization.Limit
    LimitUnit: Unit
    LimitValue: float
    LoadCase: int
    ModeNumber: int
    Response: CAE.Optimization.Response
    ResultMeasure: CAE.ResultMeasure


class DAOConstraint(NXObject):
    def __init__(self) -> None: ...
    def GetNumberResultGroup(self) -> int:
        ...
    def GetResults(self, resultGroupIndex: int) -> float:
        ...


class Category(enum.Enum):
    OneDimension = 0
    TwoDimension = 1
    ThreeDimension = 2
    All = 3


