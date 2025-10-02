from ....NXOpen import *
from ...CAE import *
from ..ResponseSimulation import *

import typing
import enum

class VelocityImpactParameters(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DropHeight: Expression
    PulseDuration: Expression
    StartPosition: CAE.ResponseSimulation.VelocityImpactParameters.StartPositionType
    TimeStep: Expression
    Velocity: Expression


    class StartPositionType(enum.Enum):
        AtDrop = 0
        BeforeImpact = 1
        AtImpact = 2
    

class VelocityImpactExcitationBuilder(CAE.ResponseSimulation.ExcitationBuilder):
    def __init__(self) -> None: ...
    ImpactDirection: CAE.ResponseSimulation.VelocityImpactDirection
    ImpactMethod: CAE.ResponseSimulation.VelocityImpactExcitationBuilder.ImpactMethodType
    ImpactParameters: CAE.ResponseSimulation.VelocityImpactParameters


    class ImpactMethodType(enum.Enum):
        ConstantVelocity = 0
        DropImpact = 1
    

class VelocityImpactExcitation(CAE.ResponseSimulation.Excitation):
    def __init__(self) -> None: ...


class VelocityImpactDirection(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DirectionOption: CAE.ResponseSimulation.VelocityImpactDirection.DirectionType
    NodalComponent: CAE.ResponseSimulation.VelocityImpactDirection.NodalComponentType
    ReverseDirection: bool
    UserDefinedDirection: Direction


    class NodalComponentType(enum.Enum):
        Dof1 = 0
        Dof2 = 1
        Dof3 = 2
    

    class DirectionType(enum.Enum):
        NodalComponent = 0
        UserDefined = 1
    

class TransmissibilityEvaluationSettingBuilder(CAE.ResponseSimulation.ModalResultsEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    InputMotionType: CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder.MotionType


    class MotionType(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
    

class TransmissibilityEvaluationSetting(CAE.ResponseSimulation.ModalResultsEvaluationSetting):
    def __init__(self) -> None: ...


class TranslationalNodalFunctionExcitationBuilder(CAE.ResponseSimulation.NodalFunctionExcitationBuilder):
    def __init__(self) -> None: ...
    EnableUserDefinedDirection: bool
    EnableUserDefinedRotation: bool
    FunctionComponentX: CAE.ResponseSimulation.FunctionComponentData
    FunctionComponentY: CAE.ResponseSimulation.FunctionComponentData
    FunctionComponentZ: CAE.ResponseSimulation.FunctionComponentData
    RotationAxis: CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder.RotationAxisType
    UserDefinedDirection: Direction
    UserDefinedFunction: CAE.ResponseSimulation.FunctionComponentData


    class RotationAxisType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

class TranslationalNodalFunctionExcitation(CAE.ResponseSimulation.NodalFunctionExcitation):
    def __init__(self) -> None: ...


class TranslationalDDAMExcitationBuilder(CAE.ResponseSimulation.DDAMExcitationBuilder):
    def __init__(self) -> None: ...


class TranslationalDDAMExcitation(CAE.ResponseSimulation.DDAMExcitation):
    def __init__(self) -> None: ...


class StrengthStressOption(enum.Enum):
    ElementMaximum = 0
    NodeOnElement = 1


class StrengthStressMaterialDefinitionMethod(enum.Enum):
    UltimateSafety = 0
    YieldSafety = 1


class StrengthStressCriteria(enum.Enum):
    VonMises = 0
    MaxPrinciple = 1
    MinPrinciple = 2


class StrengthResultsEvaluationSettingBuilder(CAE.ResponseSimulation.DynamicResultEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    def GetDestinationElements(self) -> typing.List[CAE.FEElement]:
        ...
    def SetDestinationElements(self, destinationElement: typing.List[CAE.FEElement]) -> None:
        ...
    CombinationOptionsBuilder: CAE.ResponseSimulation.CombinationEvaluationOptions
    DataLocation: CAE.ResponseSimulation.DataLocation
    MaterialDefinitionType: CAE.ResponseSimulation.StrengthStressMaterialDefinitionMethod
    MaterialOverrideOption: bool
    MaterialSafetyFactor: float
    StandardDeviation: float
    StressCriteriaType: CAE.ResponseSimulation.StrengthStressCriteria
    StressOptionType: CAE.ResponseSimulation.StrengthStressOption


class StrengthResultsEvaluationSetting(CAE.ResponseSimulation.DynamicResultEvaluationSetting):
    def __init__(self) -> None: ...


class StrainGageType(enum.Enum):
    UniAxial = 0
    BiAxial = 1
    Rosette45DegreeIncrement = 2
    Rosette60DegreeIncrement = 3


class StrainGageShellElementFaceType(enum.Enum):
    Top = 0
    Botton = 1


class StrainGageResult(enum.Enum):
    Strain = 0
    Stress = 1


class StrainGagePlacementType(enum.Enum):
    Node = 0
    ElementFaceCenter = 1


class StrainGageOrientationPlane(enum.Enum):
    FacePlane = 0
    Csys = 1


class StrainGageEvaluationSettingBuilder(CAE.ResponseSimulation.FunctionEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    DataComponent: CAE.ResponseSimulation.DirectionDataComponent
    StrainGage: SelectDisplayableObjectList


class StrainGageEvaluationSetting(CAE.ResponseSimulation.DynamicResultEvaluationSetting):
    def __init__(self) -> None: ...


class StrainGageCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ResponseSimulation.StrainGage]:
        ...
    def __init__(self, owner: CAE.ResponseSimulation.Manager) -> None: ...
    def __init__(self) -> None: ...
    def CreateStrainGageBuilder(self, strainGage: CAE.ResponseSimulation.StrainGage) -> CAE.ResponseSimulation.StrainGageBuilder:
        ...
    def FindObject(self, name: str) -> CAE.ResponseSimulation.StrainGage:
        ...
    def Tag(self) -> Tag: ...



class StrainGageBuilder(CAE.ResponseSimulation.BaseBuilder):
    def __init__(self) -> None: ...
    Csys: SmartObject
    GageType: CAE.ResponseSimulation.StrainGageType
    Placement: CAE.ResponseSimulation.StrainGagePlacementType
    Plane: CAE.ResponseSimulation.StrainGageOrientationPlane
    ResultType: CAE.ResponseSimulation.StrainGageResult
    RotationAngle: Expression
    SelectedElementFaces: CAE.SelectFEElemFaceList
    SelectedNode: CAE.SelectFENodeList
    ShellElementFace: CAE.ResponseSimulation.StrainGageShellElementFaceType


class StrainGage(DisplayableObject):
    def __init__(self) -> None: ...
    def GetDisplayAttribute(self) -> CAE.ResponseSimulation.RSDisplayObject:
        ...


class StaticLoadExcitationBuilder(CAE.ResponseSimulation.ExcitationBuilder):
    def __init__(self) -> None: ...
    ExcitationFunction: CAE.ResponseSimulation.FunctionComponentData


class StaticLoadExcitation(CAE.ResponseSimulation.Excitation):
    def __init__(self) -> None: ...


class SolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ResponseSimulation.Solution]:
        ...
    def __init__(self, owner: CAE.ResponseSimulation.Manager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSolutionBuilder(self, raSolution: CAE.ResponseSimulation.Solution) -> CAE.ResponseSimulation.SolutionBuilder:
        ...
    def CloneSolution(self, oldSolution: CAE.ResponseSimulation.Solution, suggestedName: str) -> CAE.ResponseSimulation.Solution:
        ...
    def FindObject(self, solutionName: str) -> CAE.ResponseSimulation.Solution:
        ...
    def Tag(self) -> Tag: ...

    ActiveSolution: CAE.ResponseSimulation.Solution


class SolutionBuilder(CAE.ResponseSimulation.BaseBuilder):
    def __init__(self) -> None: ...
    Attributes: CAE.ResponseSimulation.SolutionAttributes
    ImportedEefFile: str
    ReferencedSolution: CAE.SimSolution
    ScratchDir: str
    UseScratchDir: bool


class SolutionAttributes(TaggedObject):
    def __init__(self) -> None: ...
    RigidBodyToleranceExp: Expression


class Solution(NXObject):
    def __init__(self) -> None: ...
    def GetSolutionName(self) -> str:
        ...
    def SetSolutionName(self, solutionName: str, renameResultFile: bool) -> None:
        ...
    def Destroy(self, deleteResultFile: bool) -> None:
        ...
    def GetModalProperties(self) -> CAE.ResponseSimulation.ModalProperties:
        ...
    def GetEvaluationParameters(self) -> CAE.ResponseSimulation.EvaluationParameters:
        ...
    def GetEvents(self) -> typing.List[CAE.ResponseSimulation.RSEvent]:
        ...
    def ImportEvent(self, eventDefinitionFile: str, suggestedName: str) -> CAE.ResponseSimulation.RSEvent:
        ...
    def CloneEvent(self, sourceEvent: CAE.ResponseSimulation.RSEvent, suggestedName: str) -> CAE.ResponseSimulation.RSEvent:
        ...
    def GetResultFileName(self) -> str:
        ...
    def EvaluateFrf(self, evaluationSetting: CAE.ResponseSimulation.FrfEvaluationSetting) -> None:
        ...
    def EvaluateTransmissibility(self, evaluationSetting: CAE.ResponseSimulation.TransmissibilityEvaluationSetting) -> None:
        ...
    def CloneSensor(self, sourceSensor: CAE.ResponseSimulation.Sensor, suggestedName: str) -> CAE.ResponseSimulation.Sensor:
        ...
    def CloneStrainGage(self, sourceGage: CAE.ResponseSimulation.StrainGage, suggestedName: str) -> CAE.ResponseSimulation.StrainGage:
        ...
    def CheckObsoleteStatus(self) -> None:
        """public void CheckObsoleteStatus()"""
        ...
    ActiveEvent: CAE.ResponseSimulation.RSEvent


class ShellElementEvaluationLocation(enum.Enum):
    Top = 0
    Middle = 1
    Bottom = 2


class SensorType(enum.Enum):
    Component = 0
    Direction = 1
    Normal = 2


class SensorResultType(enum.Enum):
    Displacement = 0
    Velocity = 1
    Acceleration = 2
    ReactionForce = 3


class SensorEvaluationSettingBuilder(CAE.ResponseSimulation.FunctionEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    Sensor: SelectDisplayableObjectList


class SensorEvaluationSetting(CAE.ResponseSimulation.DynamicResultEvaluationSetting):
    def __init__(self) -> None: ...


class SensorCoordinateType(enum.Enum):
    NodalCs = 0
    GlobalCs = 1


class SensorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ResponseSimulation.Sensor]:
        ...
    def __init__(self, owner: CAE.ResponseSimulation.Manager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSensorBuilder(self, rsSensor: CAE.ResponseSimulation.Sensor) -> CAE.ResponseSimulation.SensorBuilder:
        ...
    def DeleteSensor(self, rsSensor: CAE.ResponseSimulation.Sensor) -> None:
        ...
    def FindObject(self, name: str) -> CAE.ResponseSimulation.Sensor:
        ...
    def Tag(self) -> Tag: ...



class SensorBuilder(CAE.ResponseSimulation.BaseBuilder):
    def __init__(self) -> None: ...
    def GetSelectedNodes(self) -> typing.List[CAE.FENode]:
        ...
    def SetSelectedNodes(self, destinationNodes: typing.List[CAE.FENode]) -> None:
        ...
    ReverseNormalDirection: bool
    SensorCoordinateType: CAE.ResponseSimulation.SensorCoordinateType
    SensorDirectionX: bool
    SensorDirectionY: bool
    SensorDirectionZ: bool
    SensorResultType: CAE.ResponseSimulation.SensorResultType
    SensorRotationX: bool
    SensorRotationY: bool
    SensorRotationZ: bool
    SensorType: CAE.ResponseSimulation.SensorType
    SensorVector: Direction


class Sensor(DisplayableObject):
    def __init__(self) -> None: ...
    def GetDisplayAttribute(self) -> CAE.ResponseSimulation.RSDisplayObject:
        ...


class RSEventSolverParameters(TaggedObject):
    def __init__(self) -> None: ...
    def GetDdamCoefficient(self, coefficientType: CAE.ResponseSimulation.RSEventSolverParameters.DdamCoefficientType) -> float:
        ...
    def SetDdamCoefficient(self, coefficientType: CAE.ResponseSimulation.RSEventSolverParameters.DdamCoefficientType, coefficient: float) -> None:
        ...
    DdamCoefficientA: float
    DdamCoefficientV: float


    class DdamCoefficientType(enum.Enum):
        Af = 0
        Vf = 1
        Aa = 2
        Ab = 3
        Ac = 4
        Ad = 5
        Va = 6
        Vb = 7
        Vc = 8
    

class RSEventOutputSetting(TaggedObject):
    def __init__(self) -> None: ...
    FemGeometrySaveOption: bool


class RSEventCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ResponseSimulation.RSEvent]:
        ...
    def __init__(self, owner: CAE.ResponseSimulation.Manager) -> None: ...
    def __init__(self) -> None: ...
    def CreateEventBuilder(self, raEvent: CAE.ResponseSimulation.RSEvent) -> CAE.ResponseSimulation.RSEventBuilder:
        ...
    def DeleteEvent(self, raEvent: CAE.ResponseSimulation.RSEvent) -> None:
        ...
    def FindObject(self, name: str) -> CAE.ResponseSimulation.RSEvent:
        ...
    def Tag(self) -> Tag: ...



class RSEventBuilder(CAE.ResponseSimulation.BaseBuilder):
    def __init__(self) -> None: ...
    Attributes: CAE.ResponseSimulation.RSEventAttributes
    EventType: CAE.ResponseSimulation.RSEvent.Type
    InitialConditions: CAE.ResponseSimulation.InitialConditions
    OutputSetting: CAE.ResponseSimulation.RSEventOutputSetting
    ResponseSimulationSolution: CAE.ResponseSimulation.Solution


class RSEventAttributes(TaggedObject):
    def __init__(self) -> None: ...
    AnalysisType: CAE.ResponseSimulation.RSEvent.AnalysisType
    CoefficientDefinitionMethod: CAE.ResponseSimulation.DDAMExcitation.CoefficientDefinitionType
    CoefficientFile: str
    Duration: float
    DurationOption: CAE.ResponseSimulation.RSEvent.DurationOption
    FastRmsMethod: bool
    Formulation: CAE.ResponseSimulation.RSEvent.DdamFormulationType
    InterpolationMethod: CAE.ResponseSimulation.InterpolationMethod
    MinimumGValue: float
    MountingType: CAE.ResponseSimulation.DDAMExcitation.MountingType
    ResponseType: CAE.ResponseSimulation.DDAMExcitation.ResponseType
    ShipType: CAE.ResponseSimulation.DDAMExcitation.ShipType
    Spacing: CAE.ResponseSimulation.RSEvent.SpacingType
    SpectralLines: int


class RSEvent(NXObject):
    def __init__(self) -> None: ...
    def GetSolverParameters(self) -> CAE.ResponseSimulation.RSEventSolverParameters:
        ...
    def GetCalculateStaticOffset(self) -> bool:
        ...
    def SetCalculateStaticOffset(self, calculateStaticOffset: bool) -> None:
        ...
    def GetEventName(self) -> str:
        ...
    def SetEventName(self, eventName: str, renameResultFile: bool) -> None:
        ...
    def Destroy(self, deleteResultFile: bool) -> None:
        ...
    def GetExcitations(self) -> typing.List[CAE.ResponseSimulation.Excitation]:
        ...
    def GetResultFileName(self, resultFileType: CAE.ResponseSimulation.RSEvent.ResultFileType) -> str:
        ...
    def Export(self, eventDefinitionFile: str) -> None:
        ...
    def EvaluateModalFunctionResponse(self) -> None:
        ...
    def EvaluateNodalFunctionResponse(self, evaluationSetting: CAE.ResponseSimulation.NodalFunctionEvaluationSetting) -> None:
        ...
    def EvaluateElementalFunctionResponse(self, evaluationSetting: CAE.ResponseSimulation.ElementalFunctionEvaluationSetting) -> None:
        ...
    def EvaluateCsd(self, evaluationSetting: CAE.ResponseSimulation.CsdEvaluationSetting) -> None:
        ...
    def EvaluateModalResponse(self) -> None:
        ...
    def EvaluateResponseResults(self, evaluationSetting: CAE.ResponseSimulation.ResponseResultsEvaluationSetting) -> None:
        ...
    def EvaluateStrengthResults(self, evaluationSetting: CAE.ResponseSimulation.StrengthResultsEvaluationSetting) -> None:
        ...
    def EvaluatePeakValueResults(self, evaluationSetting: CAE.ResponseSimulation.PeakValueEvaluationSetting) -> None:
        ...
    def EvaluateRmsResults(self, evaluationSetting: CAE.ResponseSimulation.RmsResultsEvaluationSetting) -> None:
        ...
    def EvaluateLcrResults(self, evaluationSetting: CAE.ResponseSimulation.LcrResultsEvaluationSetting) -> None:
        ...
    def EvaluateSensorResponse(self) -> None:
        ...
    def EvaluateSensorResponse(self, evaluationSetting: CAE.ResponseSimulation.SensorEvaluationSetting) -> None:
        ...
    def EvaluateStrainGageResponse(self, evaluationSetting: CAE.ResponseSimulation.StrainGageEvaluationSetting) -> None:
        ...


    class Type(enum.Enum):
        Transient = 0
        Frequency = 1
        Random = 2
        ResponseSpectrum = 3
        Ddam = 4
        Static = 5
    

    class SpacingType(enum.Enum):
        Even = 0
        Uneven = 1
    

    class ResultFileType(enum.Enum):
        ModalResponse = 0
        FunctionResponse = 1
        DynamicResponse = 2
    

    class DurationOption(enum.Enum):
        ExcitationFunction = 0
        UserDefined = 1
    

    class DdamFormulationType(enum.Enum):
        Standard = 0
        UserDefined = 1
    

    class AnalysisType(enum.Enum):
        ModeAcceleration = 0
        ModeDisplacement = 1
    

class RSDisplayObject(NXObject):
    def __init__(self) -> None: ...
    DisplayName: bool
    Scale: Expression


class RotationalNodalFunctionExcitationBuilder(CAE.ResponseSimulation.NodalFunctionExcitationBuilder):
    def __init__(self) -> None: ...
    FunctionComponentRx: CAE.ResponseSimulation.FunctionComponentData
    FunctionComponentRy: CAE.ResponseSimulation.FunctionComponentData
    FunctionComponentRz: CAE.ResponseSimulation.FunctionComponentData


class RotationalNodalFunctionExcitation(CAE.ResponseSimulation.NodalFunctionExcitation):
    def __init__(self) -> None: ...


class RotationalDDAMExcitationBuilder(CAE.ResponseSimulation.DDAMExcitationBuilder):
    def __init__(self) -> None: ...


class RotationalDDAMExcitation(CAE.ResponseSimulation.DDAMExcitation):
    def __init__(self) -> None: ...


class RmsResultsEvaluationSettingBuilder(CAE.ResponseSimulation.PrlResultsEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    EvaluationMethod: CAE.ResponseSimulation.RmsLcrEvaluationMethod
    UserDefinedDirection: Direction
    UsingUserDefinedDirection: bool


class RmsResultsEvaluationSetting(CAE.ResponseSimulation.PrlResultsEvaluationSetting):
    def __init__(self) -> None: ...


class RmsLcrEvaluationMethod(enum.Enum):
    SmallNumberItems = 0
    LargeNumberItems = 1
    AutomaticSelection = 2


class ResponseResultsEvaluationSettingBuilder(CAE.ResponseSimulation.DynamicResultEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    def GetDestinationNodes(self) -> typing.List[CAE.FENode]:
        ...
    def SetDestinationNodes(self, destinationNodes: typing.List[CAE.FENode]) -> None:
        ...
    def GetDestinationElements(self) -> typing.List[CAE.FEElement]:
        ...
    def SetDestinationElements(self, destinationElement: typing.List[CAE.FEElement]) -> None:
        ...
    def GetOutputOptions(self) -> typing.List[CAE.ResponseSimulation.EvaluationResultType]:
        ...
    def SetOutputOptions(self, outputOptions: typing.List[CAE.ResponseSimulation.EvaluationResultType]) -> None:
        ...
    def GetPointsValueList(self) -> float:
        ...
    def SetPointsValueList(self, pointsValueList: float) -> None:
        ...
    DecimationOrder: int
    EndPoint: float
    PointValue: float
    ResponseDomainDefinitionOption: CAE.ResponseSimulation.ResponseDomainDefinitionMethod
    StartPoint: float


class ResponseResultsEvaluationSetting(CAE.ResponseSimulation.DynamicResultEvaluationSetting):
    def __init__(self) -> None: ...


class ResponseDomainDefinitionMethod(enum.Enum):
    StartEndPoint = 0
    KeyIn = 1
    NaturalFrequency = 2


class PrlResultsEvaluationSettingBuilder(CAE.ResponseSimulation.DynamicResultEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    def GetOutputNodes(self) -> typing.List[CAE.FENode]:
        ...
    def SetOutputNodes(self, destinationNodes: typing.List[CAE.FENode]) -> None:
        ...
    def GetOutputElements(self) -> typing.List[CAE.FEElement]:
        ...
    def SetOutputElements(self, destinationElements: typing.List[CAE.FEElement]) -> None:
        ...
    def GetDataComponents(self) -> typing.List[CAE.ResponseSimulation.DirectionDataComponent]:
        ...
    def SetDataComponents(self, dataComponent: typing.List[CAE.ResponseSimulation.DirectionDataComponent]) -> None:
        ...
    CoordinateSystem: CAE.ResponseSimulation.CoordinateSystem
    ObservationNode: CAE.FENode
    Relative: bool
    ResultType: CAE.ResponseSimulation.EvaluationResultType


class PrlResultsEvaluationSetting(CAE.ResponseSimulation.DynamicResultEvaluationSetting):
    def __init__(self) -> None: ...


class PhysicalDampingSettings(TaggedObject):
    def __init__(self) -> None: ...
    PhysicalHystereticScalingFactor: float
    PhysicalViscousScalingFactor: float
    UsingPhysicalHysteretic: bool
    UsingPhysicalViscous: bool


class PeakValueEvaluationSettingBuilder(CAE.ResponseSimulation.PrlResultsEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    CombinationOptions: CAE.ResponseSimulation.CombinationEvaluationOptions


class PeakValueEvaluationSetting(CAE.ResponseSimulation.PrlResultsEvaluationSetting):
    def __init__(self) -> None: ...


class ObjectLabel(TaggedObject):
    def __init__(self) -> None: ...
    def GetDescriptions(self) -> str:
        ...
    def SetDescriptions(self, description: str) -> None:
        ...
    Name: str


class NormalMode(NXObject):
    def __init__(self) -> None: ...
    def GetModeId(self) -> int:
        ...
    def GetFrequency(self) -> float:
        ...
    def GetStiffeness(self) -> float:
        ...
    def GetMass(self) -> float:
        ...
    def GetXMass(self) -> float:
        ...
    def GetYMass(self) -> float:
        ...
    def GetZMass(self) -> float:
        ...
    def GetRxMass(self) -> float:
        ...
    def GetRyMass(self) -> float:
        ...
    def GetRzMass(self) -> float:
        ...
    def GetPhysicalViscous(self) -> float:
        ...
    def GetPhysicalHysteretic(self) -> float:
        ...
    Active: bool
    Hysteretic: float
    Viscous: float


class NodalFunctionExcitationBuilder(CAE.ResponseSimulation.ExcitationBuilder):
    def __init__(self) -> None: ...


class NodalFunctionExcitation(CAE.ResponseSimulation.Excitation):
    def __init__(self) -> None: ...


    class Type(enum.Enum):
        NodalForce = 0
        EnforcedMotion = 1
    

class NodalFunctionEvaluationSettingBuilder(CAE.ResponseSimulation.FunctionEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    def GetDestinationNodes(self) -> typing.List[CAE.FENode]:
        ...
    def SetDestinationNodes(self, destinationNodes: typing.List[CAE.FENode]) -> None:
        ...
    BeamDataLocation: CAE.ResponseSimulation.NodalFunctionEvalBeamLocation
    CoordinateSystem: CAE.ResponseSimulation.CoordinateSystem
    DataComponent: CAE.ResponseSimulation.DirectionDataComponent
    RelativeNode: CAE.FENode
    ShellDataLocation: CAE.ResponseSimulation.NodalFunctionEvalShellLocation
    UserDefinedDirection: Direction
    UsingUserDefinedDirection: CAE.ResponseSimulation.NodalFunctionEvalRequest


class NodalFunctionEvaluationSetting(CAE.ResponseSimulation.FunctionEvaluationSetting):
    def __init__(self) -> None: ...


class NodalFunctionEvalShellLocation(enum.Enum):
    Top = 0
    Middle = 1
    Bottom = 2
    All = 3


class NodalFunctionEvalRequest(enum.Enum):
    UserDefinedDirection = 0
    DataComponent = 1


class NodalFunctionEvalBeamLocation(enum.Enum):
    C = 0
    D = 1
    E = 2
    F = 3
    All = 4


class NodalAveragingOption(enum.Enum):
    Shells = 0
    Solids = 1


class ModeInitialData(NXObject):
    def __init__(self) -> None: ...
    def GetModeId(self) -> int:
        ...
    InitialDisplacement: float
    InitialVelocity: float


class ModalResultsEvaluationSettingBuilder(CAE.ResponseSimulation.FunctionEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    def GetOutputNodes(self) -> typing.List[CAE.FENode]:
        ...
    def SetOutputNodes(self, destinationNode: typing.List[CAE.FENode]) -> None:
        ...
    def GetOutputElements(self) -> typing.List[CAE.FEElement]:
        ...
    def SetOutputElements(self, destinationElements: typing.List[CAE.FEElement]) -> None:
        ...
    DataLocation: CAE.ResponseSimulation.DataLocation
    EvaluationProperty: CAE.ResponseSimulation.FrequencyDefinition
    InputDirection: CAE.ResponseSimulation.DirectionDataComponent
    InputNode: CAE.FENode
    ObservationNode: CAE.FENode
    OutputRequest: CAE.ResponseSimulation.DirectionDataComponent


class ModalResultsEvaluationSetting(CAE.ResponseSimulation.FunctionEvaluationSetting):
    def __init__(self) -> None: ...


class ModalProperties(NXObject):
    def __init__(self) -> None: ...
    def GetNormalModeCount(self) -> int:
        ...
    def GetConstrainModeCount(self) -> int:
        ...
    def GetAttachmentModeCount(self) -> int:
        ...
    def GetNormalModeById(self, modeId: int) -> CAE.ResponseSimulation.NormalMode:
        ...
    def GetNormalModes(self) -> typing.List[CAE.ResponseSimulation.NormalMode]:
        ...
    def Activate(self, activate: bool) -> None:
        ...
    def SetDampingFactors(self, viscousDamping: float, hystereticDamping: float) -> None:
        ...
    def SetRayleighDamping(self, alphaFactor: float, beltaFactor: float) -> None:
        ...
    def GetPhysicalDampingSettings(self) -> CAE.ResponseSimulation.PhysicalDampingSettings:
        ...


class Manager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def Tag(self) -> Tag: ...

    Solutions: CAE.ResponseSimulation.SolutionCollection
    Events: CAE.ResponseSimulation.RSEventCollection
    Excitations: CAE.ResponseSimulation.ExcitationCollection
    EvaluationSettingManager: CAE.ResponseSimulation.EvaluationSettingManager
    Sensors: CAE.ResponseSimulation.SensorCollection
    StrainGages: CAE.ResponseSimulation.StrainGageCollection


class LcrResultsEvaluationSettingBuilder(CAE.ResponseSimulation.RmsResultsEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    CrossingLevel: float
    CrossingLevelExpression: Expression


class LcrResultsEvaluationSetting(CAE.ResponseSimulation.RmsResultsEvaluationSetting):
    def __init__(self) -> None: ...


class InterpolationMethod(enum.Enum):
    LogLog = 0
    LinearLinear = 1
    LinearLog = 2
    LogLinear = 3


class InitialConditions(NXObject):
    def __init__(self) -> None: ...
    def GetCustomizedInitialDataById(self, modeId: int) -> CAE.ResponseSimulation.ModeInitialData:
        ...
    def GetAllCustomizedInitialData(self) -> typing.List[CAE.ResponseSimulation.ModeInitialData]:
        ...
    EntryMethodOption: CAE.ResponseSimulation.InitialConditions.EntryMethod
    ExistingEefFile: str
    InitialConditionType: CAE.ResponseSimulation.InitialConditions.Type


    class Type(enum.Enum):
        QuasiStatic = 0
        Zero = 1
        UserDefined = 2
    

    class EntryMethod(enum.Enum):
        ManualData = 0
        FromEef = 1
    

class FunctionEvaluationSettingBuilder(Builder):
    def __init__(self) -> None: ...
    OutputSettings: CAE.ResponseSimulation.FunctionEvaluationOutputSettings
    ResultType: CAE.ResponseSimulation.EvaluationResultType


class FunctionEvaluationSetting(CAE.ResponseSimulation.EvaluationSetting):
    def __init__(self) -> None: ...


class FunctionEvaluationOutputSettings(TaggedObject):
    def __init__(self) -> None: ...
    RecordPrefix: str
    ShowPlot: bool
    StoreOption: bool


class FunctionComponentData(TaggedObject):
    def __init__(self) -> None: ...
    def GetComponentType(self) -> CAE.ResponseSimulation.Excitation.Component:
        ...
    Enable: bool
    Function: CAE.Function
    PhaseAngle: float
    ScalarFactor: float


class FrfEvaluationSettingBuilder(CAE.ResponseSimulation.ModalResultsEvaluationSettingBuilder):
    def __init__(self) -> None: ...


class FrfEvaluationSetting(CAE.ResponseSimulation.ModalResultsEvaluationSetting):
    def __init__(self) -> None: ...


class FrequencyDefinition(TaggedObject):
    def __init__(self) -> None: ...
    def GetFrequencies(self) -> float:
        ...
    def SetFrequencies(self, frequencies: float) -> None:
        ...
    ContributorNumber: int
    EndValue: float
    EvaluationType: CAE.ResponseSimulation.FrequencyDefinition.Definition
    GenerateMaximumContributors: bool
    InterpolationMethodOption: CAE.ResponseSimulation.FrequencyDefinition.InterpolationMethod
    NormalizeResults: bool
    SpectralLine: int
    StartValue: float


    class InterpolationMethod(enum.Enum):
        LogLog = 0
        LogLinear = 1
        LinearLinear = 2
    

    class Definition(enum.Enum):
        Range = 0
        ModalContribution = 1
    

class ExcitationLocationDefinition(TaggedObject):
    def __init__(self) -> None: ...
    ExcitationLocation: SelectObject
    ExcitationLocationId: int
    ExcitationLocationType: CAE.ResponseSimulation.ExcitationBuilder.ExcitationLocationType


class ExcitationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ResponseSimulation.Excitation]:
        ...
    def __init__(self, owner: CAE.ResponseSimulation.Manager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTranslationalNodalFunctionExcitationBuilder(self, excitation: CAE.ResponseSimulation.TranslationalNodalFunctionExcitation) -> CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder:
        ...
    def CreateRotationalNodalFunctionExcitationBuilder(self, excitation: CAE.ResponseSimulation.RotationalNodalFunctionExcitation) -> CAE.ResponseSimulation.RotationalNodalFunctionExcitationBuilder:
        ...
    def CreateDistributedLoadExcitationBuilder(self, excitation: CAE.ResponseSimulation.DistributedLoadExcitation) -> CAE.ResponseSimulation.DistributedLoadExcitationBuilder:
        ...
    def CreateDdamExcitationBuilder(self, excitation: CAE.ResponseSimulation.DDAMExcitation) -> CAE.ResponseSimulation.DDAMExcitationBuilder:
        ...
    def CreateTranslationalDdamExcitationBuilder(self, excitation: CAE.ResponseSimulation.DDAMExcitation) -> CAE.ResponseSimulation.DDAMExcitationBuilder:
        ...
    def CreateRotationalDdamExcitationBuilder(self, excitation: CAE.ResponseSimulation.DDAMExcitation) -> CAE.ResponseSimulation.DDAMExcitationBuilder:
        ...
    def CreateCsdExcitationBuilder(self, excitation: CAE.ResponseSimulation.CSDExcitation) -> CAE.ResponseSimulation.CSDExcitationBuilder:
        ...
    def CreateVelocityImpactExcitationBuilder(self, excitation: CAE.ResponseSimulation.VelocityImpactExcitation) -> CAE.ResponseSimulation.VelocityImpactExcitationBuilder:
        ...
    def CreateStaticLoadExcitationBuilder(self, excitation: CAE.ResponseSimulation.StaticLoadExcitation) -> CAE.ResponseSimulation.StaticLoadExcitationBuilder:
        ...
    def DeleteExcitation(self, excitation: CAE.ResponseSimulation.Excitation) -> None:
        ...
    def FindObject(self, name: str) -> CAE.ResponseSimulation.Excitation:
        ...
    def Tag(self) -> Tag: ...



class ExcitationBuilder(CAE.ResponseSimulation.BaseBuilder):
    def __init__(self) -> None: ...
    DynamicEvent: CAE.ResponseSimulation.RSEvent
    ExcitationLocationDefinition: CAE.ResponseSimulation.ExcitationLocationDefinition


    class ExcitationLocationType(enum.Enum):
        StaticLoad = -2
        DistributedLoad = -1
        NodalForce = 0
        EnforcedMotion = 1
    

class Excitation(NXObject):
    def __init__(self) -> None: ...
    def Destroy(self) -> None:
        ...
    ExcitationName: str


    class Component(enum.Enum):
        DistributedLoad = -1
        X = 0
        Y = 1
        Z = 2
        Rx = 3
        Ry = 4
        Rz = 5
        UserDefined = 6
    

class EvaluationSettingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.ResponseSimulation.Manager) -> None: ...
    def CreateFrfEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.FrfEvaluationSetting) -> CAE.ResponseSimulation.FrfEvaluationSettingBuilder:
        ...
    def CreateCsdEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.CsdEvaluationSetting) -> CAE.ResponseSimulation.CsdEvaluationSettingBuilder:
        ...
    def CreateTransmissibilityEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.TransmissibilityEvaluationSetting) -> CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder:
        ...
    def CreateNodalFunctionEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.NodalFunctionEvaluationSetting) -> CAE.ResponseSimulation.NodalFunctionEvaluationSettingBuilder:
        ...
    def CreateElementalFunctionEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.ElementalFunctionEvaluationSetting) -> CAE.ResponseSimulation.ElementalFunctionEvaluationSettingBuilder:
        ...
    def CreateResponseResultsEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.ResponseResultsEvaluationSetting) -> CAE.ResponseSimulation.ResponseResultsEvaluationSettingBuilder:
        ...
    def CreateStrengthResultsEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.StrengthResultsEvaluationSetting) -> CAE.ResponseSimulation.StrengthResultsEvaluationSettingBuilder:
        ...
    def CreatePeakValueEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.PeakValueEvaluationSetting) -> CAE.ResponseSimulation.PeakValueEvaluationSettingBuilder:
        ...
    def CreateRmsResultsEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.RmsResultsEvaluationSetting) -> CAE.ResponseSimulation.RmsResultsEvaluationSettingBuilder:
        ...
    def CreateLcrResultsEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.LcrResultsEvaluationSetting) -> CAE.ResponseSimulation.LcrResultsEvaluationSettingBuilder:
        ...
    def CreateStrainGageEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.StrainGageEvaluationSetting) -> CAE.ResponseSimulation.StrainGageEvaluationSettingBuilder:
        ...
    def CreateSensorEvaluationSettingBuilder(self, setting: CAE.ResponseSimulation.SensorEvaluationSetting) -> CAE.ResponseSimulation.SensorEvaluationSettingBuilder:
        ...
    def Tag(self) -> Tag: ...



class EvaluationSettingBuilder(Builder):
    def __init__(self) -> None: ...


class EvaluationSetting(NXObject):
    def __init__(self) -> None: ...
    def Destroy(self) -> None:
        ...


class EvaluationResultType(enum.Enum):
    Receptance = 0
    Mobility = 1
    Inertance = 2
    Displacement = 3
    Velocity = 4
    Acceleration = 5
    Stress = 6
    Strain = 7
    StrainEnergy = 8
    ShellResultant = 9
    ElementForce = 10
    BeamElementForce = 11
    ShellStressResultant = 12
    ReactionForce = 13


class EvaluationParameters(TaggedObject):
    def __init__(self) -> None: ...
    HypermatrixBufferSize: int
    IntegrationMethod: CAE.ResponseSimulation.EvaluationParameters.AnalysisIntegrationMethod
    MaxArraySize: int
    MinDampingStatus: bool
    ZeroMeanCorrection: bool


    class AnalysisIntegrationMethod(enum.Enum):
        DuhameldIntegral = 0
        NewmarkBeta = 1
    

class ElementLocation(enum.Enum):
    Both = 0
    Centroid = 1
    Corners = 2


class ElementalFunctionEvaluationSettingBuilder(CAE.ResponseSimulation.FunctionEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    def GetDestinationElements(self) -> typing.List[CAE.FEElement]:
        ...
    def SetDestinationElements(self, destinationElement: typing.List[CAE.FEElement]) -> None:
        ...
    BeamDataLocation: CAE.ResponseSimulation.ElementalFunctionEvalBeamLocation
    CoordinateSystem: CAE.ResponseSimulation.CoordinateSystem
    DataComponent: CAE.ResponseSimulation.DirectionDataComponent
    ElementLocation: CAE.ResponseSimulation.ElementLocation
    ShellEvaluationLocation: CAE.ResponseSimulation.ShellElementEvaluationLocation


class ElementalFunctionEvaluationSetting(CAE.ResponseSimulation.FunctionEvaluationSetting):
    def __init__(self) -> None: ...


class ElementalFunctionEvalBeamLocation(enum.Enum):
    C = 0
    D = 1
    E = 2
    F = 3


class DynamicResultEvaluationSettingBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescriptionString(self) -> str:
        ...
    def SetDescriptionString(self, description: str) -> None:
        ...


class DynamicResultEvaluationSetting(CAE.ResponseSimulation.EvaluationSetting):
    def __init__(self) -> None: ...


class DynamicEvaluationOutputSettings(TaggedObject):
    def __init__(self) -> None: ...
    PreviewOption: bool
    RecordPrefix: str


class DistributedLoadExcitationBuilder(CAE.ResponseSimulation.ExcitationBuilder):
    def __init__(self) -> None: ...
    ExcitationFunction: CAE.ResponseSimulation.FunctionComponentData


class DistributedLoadExcitation(CAE.ResponseSimulation.Excitation):
    def __init__(self) -> None: ...


class DirectionDataComponent(enum.Enum):
    X = 0
    Y = 1
    Z = 2
    Rx = 3
    Ry = 4
    Rz = 5
    Xx = 6
    Yy = 7
    Zz = 8
    Xy = 9
    Xz = 10
    Yz = 11
    Ax = 12
    Sy = 13
    Sz = 14
    Tx = 15
    Byy = 16
    Bz = 17
    Fxx = 18
    Fyy = 19
    Fzz = 20
    Fxy = 21
    Mx = 22
    My = 23
    Mz = 24
    Mxy = 25
    Mxz = 26
    Myz = 27
    Vx = 28
    Vy = 29
    TranslationalMagnitude = 30
    Vonmises = 31
    MaxPrincipal = 32
    MinPrincipal = 33
    MaxShear = 34
    AllNormals = 35
    AllTranslational = 36
    AllForces = 37
    AllDirections = 38
    AllDataComponents = 39
    All = 40
    AllXyPlane = 41
    Leg1 = 42
    Leg2 = 43
    Leg3 = 44
    AllLegs = 45


class DDAMExcitationBuilder(CAE.ResponseSimulation.ExcitationBuilder):
    def __init__(self) -> None: ...
    def SetComponentStatus(self, component: CAE.ResponseSimulation.Excitation.Component, enable: bool) -> None:
        ...
    def GetComponentStatus(self, component: CAE.ResponseSimulation.Excitation.Component) -> bool:
        ...
    LoadingType: CAE.ResponseSimulation.DDAMExcitation.LoadingType
    ResponseType: CAE.ResponseSimulation.DDAMExcitation.ResponseType


class DDAMExcitation(CAE.ResponseSimulation.Excitation):
    def __init__(self) -> None: ...


    class ShipType(enum.Enum):
        Surface = 0
        Submarine = 1
    

    class ResponseType(enum.Enum):
        Elastic = 0
        ElasticPlastic = 1
    

    class MountingType(enum.Enum):
        Hull = 0
        Duck = 1
        ShellPlating = 2
    

    class LoadingType(enum.Enum):
        Vertical = 0
        Athwartship = 1
        ForeAndAft = 2
    

    class CoefficientDefinitionType(enum.Enum):
        ByFile = 0
        InputManually = 1
    

class DDAMComponentData(TaggedObject):
    def __init__(self) -> None: ...
    def GetComponentType(self) -> CAE.ResponseSimulation.Excitation.Component:
        ...
    def GetEnable(self) -> bool:
        ...
    LoadingTypeOption: CAE.ResponseSimulation.DDAMComponentData.LoadingType
    ResponseTypeOption: CAE.ResponseSimulation.DDAMComponentData.ResponseType


    class ResponseType(enum.Enum):
        Elastic = 0
        ElasticPlastic = 1
    

    class LoadingType(enum.Enum):
        Vertical = 0
        Athwartship = 1
        ForeAndAft = 2
    

class DataLocation(TaggedObject):
    def __init__(self) -> None: ...
    BeamLocation: CAE.ResponseSimulation.DataLocation.Beam
    ElementLocation: CAE.ResponseSimulation.DataLocation.Element
    LayerSelection: int
    ShellLocation: CAE.ResponseSimulation.DataLocation.Shell


    class Shell(enum.Enum):
        Top = 0
        Bottom = 1
        Middle = 2
    

    class Element(enum.Enum):
        Both = 0
        Centroid = 1
        Corners = 2
    

    class Beam(enum.Enum):
        C = 0
        D = 1
        E = 2
        F = 3
    

class CSDExcitationBuilder(CAE.ResponseSimulation.ExcitationBuilder):
    def __init__(self) -> None: ...
    def GetFromFunction(self, componentType: CAE.ResponseSimulation.Excitation.Component) -> CAE.ResponseSimulation.Excitation:
        ...
    def SetFromFunction(self, fromExcitation: CAE.ResponseSimulation.Excitation, componentType: CAE.ResponseSimulation.Excitation.Component) -> None:
        ...
    def GetToFunction(self, componentType: CAE.ResponseSimulation.Excitation.Component) -> CAE.ResponseSimulation.Excitation:
        ...
    def SetToFunction(self, toExcitation: CAE.ResponseSimulation.Excitation, componentType: CAE.ResponseSimulation.Excitation.Component) -> None:
        ...
    CorrelationType: CAE.ResponseSimulation.CSDExcitation.CorrelationType
    CorrelationValue: float


class CSDExcitation(CAE.ResponseSimulation.Excitation):
    def __init__(self) -> None: ...


    class CorrelationType(enum.Enum):
        PhaseAngle = 0
        TimeDelay = 1
    

class CsdEvaluationSettingBuilder(CAE.ResponseSimulation.FunctionEvaluationSettingBuilder):
    def __init__(self) -> None: ...
    def GetResponseNodes(self) -> typing.List[CAE.FENode]:
        ...
    def SetResponseNodes(self, responseNode: typing.List[CAE.FENode]) -> None:
        ...
    def GetResponseElements(self) -> typing.List[CAE.FEElement]:
        ...
    def SetResponseElements(self, responseElements: typing.List[CAE.FEElement]) -> None:
        ...
    ReferenceCoordinateSystem: CAE.ResponseSimulation.CoordinateSystem
    ReferenceDataLocation: CAE.ResponseSimulation.DataLocation
    ReferenceElement: CAE.FEElement
    ReferenceElementDataComponent: CAE.ResponseSimulation.DirectionDataComponent
    ReferenceNode: CAE.FENode
    ReferenceNodeDataComponent: CAE.ResponseSimulation.DirectionDataComponent
    ReferenceUserDefinedDirection: Direction
    ReferenceUsingUserDefinedDirection: CAE.ResponseSimulation.NodalFunctionEvalRequest
    ResponseCoordinateSystem: CAE.ResponseSimulation.CoordinateSystem
    ResponseDataLocation: CAE.ResponseSimulation.DataLocation
    ResponseElementDataComponent: CAE.ResponseSimulation.DirectionDataComponent
    ResponseNodeDataComponent: CAE.ResponseSimulation.DirectionDataComponent
    ResponseUserDefinedDirection: Direction
    ResponseUsingUserDefinedDirection: CAE.ResponseSimulation.NodalFunctionEvalRequest


class CsdEvaluationSetting(CAE.ResponseSimulation.FunctionEvaluationSetting):
    def __init__(self) -> None: ...


class CoordinateSystem(enum.Enum):
    Nodal = 0
    Global = 1
    Elemental = 2
    Material = 3


class CombinationEvaluationOptions(TaggedObject):
    def __init__(self) -> None: ...
    CombinationMethod: CAE.ResponseSimulation.CombinationEvaluationOptions.MultipleExcitationCombinationMethod
    EvaluationMethodOption: CAE.ResponseSimulation.CombinationEvaluationOptions.EvaluationMethod
    NeighboringFactor: float
    TimeDuration: float


    class MultipleExcitationCombinationMethod(enum.Enum):
        Abs = 0
        Srs = 1
    

    class EvaluationMethod(enum.Enum):
        Abs = 0
        Srss = 1
        Nrl = 2
        Cqc = 3
        NqcDoubleSum = 4
    

class BaseBuilder(Builder):
    def __init__(self) -> None: ...
    ObjectLabel: CAE.ResponseSimulation.ObjectLabel


