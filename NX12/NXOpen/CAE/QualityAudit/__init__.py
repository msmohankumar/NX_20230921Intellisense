from ....NXOpen import *
from ...CAE import *
from ..QualityAudit import *

import typing
import enum

class SupportSequenceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class Result(NXObject):
    def __init__(self) -> None: ...
    Description: str
    OwningAction: CAE.QualityAudit.Action


class ProjectionCheckSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    Threshold: Expression


class ObjectLevelProjectionCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ObjectLevelFailedProjectionToleranceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    FlangeIndex: int
    LocationIndex: int


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


class MinimumDistanceSettings(CAE.QualityAudit.ActionSettings):
    def __init__(self) -> None: ...
    MinimumDistance: Expression


class MeshLevelProjectionCheck(CAE.QualityAudit.Action):
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


class MergedNodesResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
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
    def Tag(self) -> Tag: ...

    ActionList: CAE.QualityAudit.ActionList
    CurrentActionType: CAE.QualityAudit.Manager.ActionType
    InputList: CAE.QualityAudit.InputList


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


class FreeEdgeDistanceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    CaeEdge: CAE.CAEEdge
    Connection: CAE.Connections.IConnection
    CoordinateIndex: int
    DefinitionIndex: int
    EdgePoint: Point3d
    FeElementEdge: CAE.FEElemEdge
    FlangeIndex: int
    LocationIndex: int


class FreeEdgeDistanceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class DiameterResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...


class DiameterCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ConnectivityCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ConnectionPointsDistanceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...
    Connection: CAE.Connections.IConnection
    CoordinateIndex1: int
    CoordinateIndex2: int
    DefinitionIndex1: int
    DefinitionIndex2: int
    LocationIndex1: int
    LocationIndex2: int


class ConnectionPointsDistanceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ConnectionDistanceResult(CAE.QualityAudit.Result):
    def __init__(self) -> None: ...


class ConnectionDistanceCheck(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ComponentSynthesis(CAE.QualityAudit.Action):
    def __init__(self) -> None: ...


class ActionSettings(NXObject):
    def __init__(self) -> None: ...
    def ResetToDefaults(self) -> None:
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
    Description: str
    Settings: CAE.QualityAudit.ActionSettings


    class Id(enum.Enum):
        ListAllConnections = 0
        ListNonModeledConnections = 1
        CheckComponentConnectivity = 2
        CheckComponentSynthesis = 3
        CheckDiameterRange = 4
        ObjectLevelCheckProjection = 5
        MeshLevelCheckProjection = 6
        CheckDistanceBetweenConnectionPoints = 7
        CheckDistanceBetweenConnections = 8
        CheckFreeEdgeDistance = 9
        CheckTargetSequence = 10
    

