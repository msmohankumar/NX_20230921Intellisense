from ....NXOpen import *
from ...CAE import *
from ..QualityAudit import *

import typing
import enum

class WrongSupportSequenceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    LocationIndex: int


class UniversalConnectionSynthesisResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetRepresentedConnections(self) -> typing.List[CAE.Connections.IConnection]:
        ...
    Characteristic: str
    Count: int


class SupportSequenceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class Result(NXObject):
    def __init__(self) -> None: ...
    def GetSubResults(self, subResults: typing.List[CAE.QualityAudit.Result]) -> None:
        ...
    Description: str
    Outdated: bool
    OwningAction: CAE.QualityAudit.Action


class ProjectionCheckSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    def GetThresholdByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> Expression:
        ...
    Threshold: Expression


class ObjectLevelProjectionCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ObjectLevelLengthRatioRangeResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int
    Ratio: float
    Thickness1: float
    Thickness2: float


class ObjectLevelLengthRatioRangeCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ObjectLevelLengthRangeResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    Length: float
    LocationIndex: int


class ObjectLevelLengthRangeCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ObjectLevelFlatnessResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    Distance: float
    FlangeIndex: int
    LocationIndex: int
    Point: Point3d
    ResultEntity: TaggedObject


class ObjectLevelFlatnessCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ObjectLevelFailedProjectionToleranceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int
    OffendingDistance: float


class ObjectLevelFailedProjectionResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int


class ObjectLevelCorrectedProjectionResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int


class ObjectLevelConnectionAngleResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Angle: float
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int


class ObjectLevelConnectionAngleCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class NonModeledConnectionResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MinimumDistanceSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    def GetMinimumDistanceByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> Expression:
        ...
    MinimumDistance: Expression


class MeshSubResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetMesh(self) -> CAE.Mesh:
        ...
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...


class MeshLevelProjectionCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class MeshLevelLengthRatioRangeResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int
    Ratio: float
    Thickness1: float
    Thickness2: float


class MeshLevelLengthRatioRangeCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class MeshLevelLengthRangeResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    Length: float
    LocationIndex: int


class MeshLevelLengthRangeCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class MeshLevelFlatnessResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    Distance: float
    FlangeIndex: int
    LocationIndex: int
    Point: Point3d
    ResultEntity: TaggedObject


class MeshLevelFlatnessCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class MeshLevelFailedProjectionToleranceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int
    OffendingDistance: float


class MeshLevelFailedProjectionResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int


class MeshLevelFailedElementCreationResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int


class MeshLevelConnectionAngleResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Angle: float
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int


class MeshLevelConnectionAngleCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class MeshConnectivity(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class MergedNodesWithMeshesResult(CAE.QualityAudit.MergedNodesResult):
    def __init__(self) -> None: ...
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...


class MergedNodesWithComponentsResult(CAE.QualityAudit.MergedNodesResult):
    def __init__(self) -> None: ...
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...


class MergedNodesResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class MaximumAngleSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    def GetMaximumAngleByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> Expression:
        ...
    MaximumAngle: Expression


class ManualElementsWithMeshesResult(CAE.QualityAudit.ManualElementsResult):
    def __init__(self) -> None: ...
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...


class ManualElementsWithComponentsResult(CAE.QualityAudit.ManualElementsResult):
    def __init__(self) -> None: ...
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...


class ManualElementsResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class Manager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaeSession) -> None: ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def PerformActions(self, inputActions: typing.List[CAE.QualityAudit.Action], pObjects: typing.List[NXObject]) -> None:
        ...
    def ExportResults(self, actionsToExport: typing.List[CAE.QualityAudit.Action], resultsFIle: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActionList: CAE.QualityAudit.ActionList
    CurrentActionType: CAE.QualityAudit.Manager.ActionType
    InputList: CAE.QualityAudit.InputList
    UseInputListForSynthesis: bool


    class ActionType(enum.Enum):
        Global = 0
        Connection = 1
    

class ListNonModeledConnectionsResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection


class ListNonModeledConnections(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ListConnectionsResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: TaggedObject


class ListConnections(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class LengthRatioRangeSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    def GetMinimumRatioByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> Expression:
        ...
    def GetMaximumRatioByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> Expression:
        ...
    MaximumRatio: Expression
    MinimumRatio: Expression


class LengthRangeSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    def GetMinimumDistanceByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> Expression:
        ...
    def GetMaximumDistanceByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> Expression:
        ...
    MaximumDistance: Expression
    MinimumDistance: Expression


class InputList(NXObject):
    def __init__(self) -> None: ...
    def GetAllObjects(self) -> typing.List[NXObject]:
        ...
    def SelectAll(self) -> None:
        ...
    def DeselectAll(self) -> None:
        ...
    def Select(self, obj: NXObject) -> None:
        ...
    def Deselect(self, obj: NXObject) -> None:
        ...
    def IsSelected(self, obj: NXObject) -> bool:
        ...
    def GetSelectedObjects(self) -> typing.List[NXObject]:
        ...


class IConnectedMeshes():
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...


class IConnectedComponents():
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...


class FreeEdgeDistanceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetClosestConnectionPoint(self) -> Point3d:
        ...
    CaeEdge: CAE.CAEEdge
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    Distance: float
    EdgePoint: Point3d
    FeElementEdge: CAE.FEElemEdge
    FlangeIndex: int
    LocationIndex: int


class FreeEdgeDistanceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class FlatnessSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    ClosestPointFlag: bool
    Height: Expression
    Radius: Expression


class ConnectionWithMeshesResult(CAE.QualityAudit.ConnectionResult):
    def __init__(self) -> None: ...
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...


class ConnectionWithComponentsResult(CAE.QualityAudit.ConnectionResult):
    def __init__(self) -> None: ...
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...


class ConnectionSynthesis(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ConnectionResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: TaggedObject
    Femodel: CAE.FEModelOccurrence


class ConnectionPointsDistanceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex1: int
    CoordinateIndex2: int
    DefinitionIndex1: int
    DefinitionIndex2: int
    Distance: float
    LocationIndex1: int
    LocationIndex2: int


class ConnectionPointsDistanceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ConnectionDistanceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection1: CAE.Connections.IConnection
    Connection2: CAE.Connections.IConnection
    CoordinateIndex1: int
    CoordinateIndex2: int
    Coordinates1: Point3d
    Coordinates2: Point3d
    DefinitionIndex1: int
    DefinitionIndex2: int
    Distance: float
    LocationIndex1: int
    LocationIndex2: int


class ConnectionDistanceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ConnectedMeshesGroupResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...


class ConnectedComponentsGroupResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...


class ComponentSubResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetComponent(self) -> Assemblies.Component:
        ...
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...


class ComponentConnectivity(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ActionSettings(NXObject):
    def __init__(self) -> None: ...
    def ResetToDefaults(self) -> None:
        ...
    def GetSupportedConnectionTypes(self) -> typing.List[CAE.Connections.ConnectionType]:
        ...
    def AllowOverride(self, connectionType: CAE.Connections.ConnectionType, allowOverride: bool) -> None:
        ...
    def CanOverride(self, connectionType: CAE.Connections.ConnectionType) -> bool:
        ...
    Action: CAE.QualityAudit.Action


class ActionList(NXObject):
    def __init__(self) -> None: ...
    def GetAction(self, id: CAE.QualityAudit.Action.Id) -> CAE.QualityAudit.Action:
        ...
    def SelectAll(self) -> None:
        ...
    def DeselectAll(self) -> None:
        ...
    def IsSelected(self, pAction: CAE.QualityAudit.Action) -> bool:
        ...
    def Select(self, pAction: CAE.QualityAudit.Action) -> None:
        ...
    def Deselect(self, pAction: CAE.QualityAudit.Action) -> None:
        ...
    def GetSelectedActions(self) -> typing.List[CAE.QualityAudit.Action]:
        ...
    def LoadActionSettings(self, actionConfigFile: str) -> None:
        ...
    def SaveActionSettings(self, actionConfigFile: str) -> None:
        ...


class Action(NXObject):
    def __init__(self) -> None: ...
    def Perform(self, objects: typing.List[NXObject]) -> None:
        ...
    def GetResults(self) -> typing.List[CAE.QualityAudit.Result]:
        ...
    def ExportResults(self, resultsFIle: str) -> None:
        ...
    ActionId: CAE.QualityAudit.Action.Id
    Description: str
    Settings: CAE.QualityAudit.ActionSettings


    class Id(enum.Enum):
        AllConnectionsList = 0
        NonModeledConnectionsList = 1
        SubAssemblyComponentCheck = 2
        SubAssemblyMeshCheck = 3
        ObjectLevelProjectionCheck = 4
        MeshLevelProjectionCheck = 5
        DistanceBetweenConnectionPointsCheck = 6
        DistanceBetweenConnectionsCheck = 7
        FreeEdgeDistanceCheck = 8
        TargetSequenceCheck = 9
        ObjectLevelLengthCheck = 10
        MeshLevelLengthCheck = 11
        ObjectLevelLengthRatioCheck = 12
        MeshLevelLengthRatioCheck = 13
        ObjectLevelConnectionAngleCheck = 14
        MeshLevelConnectionAngleCheck = 15
        ObjectLevelFlatnessCheck = 16
        MeshLevelFlatnessCheck = 17
        ConnectionSynthesis = 18
    

