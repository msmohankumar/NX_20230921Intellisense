from ...NXOpen import *
from ..Mechatronics import *

import typing
import enum

class VirtualAxisCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.VirtualAxis]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateVirtualAxisBuilder(self, objectSrc: Mechatronics.VirtualAxis) -> Mechatronics.VirtualAxisBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.VirtualAxis:
        ...
    def Tag(self) -> Tag: ...



class VirtualAxisBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AnchorPoint: Point
    AxisType: Mechatronics.VirtualAxisBuilder.VirtualAxisType
    Direction: Direction
    StartPosition: Expression


    class VirtualAxisType(enum.Enum):
        Linear = 0
        Angular = 1
    

class VirtualAxis(DisplayableObject):
    def __init__(self) -> None: ...


class VelocitySensorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.VelocitySensor]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateVelocitySensorBuilder(self, velocitySensor: Mechatronics.VelocitySensor) -> Mechatronics.VelocitySensorBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.VelocitySensor:
        ...
    def Tag(self) -> Tag: ...



class VelocitySensorBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    AxisJoint: SelectNXObject
    AxisType: Mechatronics.VelocitySensorBuilder.AxisJointType
    LowerOutputRange: Expression
    LowerTrimRange: Expression
    MeasureType: Mechatronics.VelocitySensorBuilder.OutputMeasureType
    UpperOutputRange: Expression
    UpperTrimRange: Expression
    UseScale: bool
    UseTrim: bool


    class OutputMeasureType(enum.Enum):
        Constant = 0
        Voltage = 1
        Current = 2
    

    class AxisJointType(enum.Enum):
        Angular = 0
        Linear = 1
    

class VelocitySensor(DisplayableObject):
    def __init__(self) -> None: ...


class UDPSignalServerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetInstanceNames(self) -> str:
        ...
    def SetConnectionNames(self, names: str) -> None:
        ...
    def GetConnectionInformation(self, connectionName: str, castMode: int, remoteIP: str, remotePort: int, localIP: str, localPort: int, groupIP: str, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.UDPSignalServerBuilder.Signal]) -> None:
        ...
    def SetConnectionInformation(self, connectionName: str, castMode: int, remoteIP: str, remotePort: int, localIP: str, localPort: int, groupIP: str, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.UDPSignalServerBuilder.Signal]) -> None:
        ...
    SelectedConfigurationName: str


    class UDPSignalServerBuilderSignal():
        SignalTag: NXObject
        BChecked: bool
        Offset: str
        def ToString(self) -> str:
            ...
        def __init__(self, SignalTag: NXObject, BChecked: bool, Offset: str) -> None: ...
    

    class Protocol(enum.Enum):
        Tcpserver = 0
        Tcpclient = 1
        Udpserver = 2
        Udpclient = 3
    

    class CastMode(enum.Enum):
        Unicast = 0
        Multicast = 1
        Broadcast = 2
    

class UDPSignalClientBuilder(Builder):
    def __init__(self) -> None: ...
    def GetConnectionNames(self, ownerParts: typing.List[Part]) -> str:
        ...
    def SetConnectionNames(self, ownerParts: typing.List[Part], names: str) -> None:
        ...
    def GetConnectionInformation(self, connectionName: str, ownerPart: Part, castMode: int, remoteIP: str, remotePort: int, localIP: str, localPort: int, groupIP: str, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.UDPSignalClientBuilder.Signal]) -> None:
        ...
    def SetConnectionInformation(self, connectionName: str, ownerPart: Part, castMode: int, remoteIP: str, remotePort: int, localIP: str, localPort: int, groupIP: str, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.UDPSignalClientBuilder.Signal]) -> None:
        ...
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part


    class UDPSignalClientBuilderSignal():
        Name: str
        EIOType: Mechatronics.SignalBuilder.IOType
        EDataType: Mechatronics.SignalBuilder.DataType
        Offset: str
        def ToString(self) -> str:
            ...
    

class TransportSurfaceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.TransportSurface]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTransportSurfaceBuilder(self, transportSurface: Mechatronics.TransportSurface) -> Mechatronics.TransportSurfaceBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.TransportSurface:
        ...
    def Tag(self) -> Tag: ...



class TransportSurfaceBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFaces(self, faces: typing.List[NXObject]) -> None:
        ...
    AxisVector: Direction
    CenterPoint: Point
    Faces: SelectFaceList
    Material: Mechatronics.CollisionMaterial
    MedianRadius: Expression
    MedianStartPosition: Expression
    MedianVelocity: Expression
    MotionType: Mechatronics.TransportSurfaceBuilder.MoveType
    Name: str
    ParallelInitialPosition: Expression
    ParallelVelocity: Expression
    PerpendicularInitialPosition: Expression
    PerpendicularVelocity: Expression
    VelocityVector: Direction


    class MoveType(enum.Enum):
        Straight = 0
        Circle = 1
    

class TransportSurface(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class TransmitterExitCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.TransmitterExit]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTransmitterExitBuilder(self, transmitterExit: Mechatronics.TransmitterExit) -> Mechatronics.TransmitterExitBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.TransmitterExit:
        ...
    def Tag(self) -> Tag: ...



class TransmitterExitBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def QueryPorts(self, ports: int) -> None:
        ...
    Orientation: CoordinateSystem
    Port: int
    Position: Point
    RigidBody: Mechatronics.SelectRigidBody


class TransmitterExit(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class TransmitterEntryCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.TransmitterEntry]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTransmitterEntryBuilder(self, transmitterEntry: Mechatronics.TransmitterEntry) -> Mechatronics.TransmitterEntryBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.TransmitterEntry:
        ...
    def Tag(self) -> Tag: ...



class TransmitterEntryBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    Candidate: SelectNXObjectList
    CandidateType: Mechatronics.TransmitterEntryBuilder.TransmitterEntryCandidateType
    CollisionSensor: Mechatronics.SelectCollisionSensorList
    ExecuteOnce: bool
    Port: int


    class TransmitterEntryCandidateType(enum.Enum):
        AnyObject = 0
        OnlySelected = 1
    

class TransmitterEntry(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class TracerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Tracer]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTracerBuilder(self, tracer: Mechatronics.Tracer) -> Mechatronics.TracerBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Tracer:
        ...
    def Tag(self) -> Tag: ...



class TracerBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str
    SelectPoint: Point
    Selection: Mechatronics.SelectRigidBody
    TraceRateSetting: Expression


class Tracer(DisplayableObject):
    def __init__(self) -> None: ...


class ThreeJointCouplerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ThreeJointCoupler]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateThreeJointCouplerBuilder(self, threeJointCouplerConstraint: Mechatronics.ThreeJointCoupler) -> Mechatronics.ThreeJointCouplerBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ThreeJointCoupler:
        ...
    def Tag(self) -> Tag: ...



class ThreeJointCouplerBuilder(Mechatronics.CouplingBuilder):
    def __init__(self) -> None: ...
    AxisType: Mechatronics.ThreeJointCouplerBuilder.AxisJointType
    ExpressionMasterMultiple: Expression
    ExpressionSlaveMultiple: Expression
    ExpressionThirdJointMultiple: Expression
    SlaveAxisType: Mechatronics.ThreeJointCouplerBuilder.AxisJointType
    ThirdAxisJoint: Mechatronics.SelectPhysicsJoint
    ThirdJointAxisType: Mechatronics.ThreeJointCouplerBuilder.AxisJointType


    class AxisJointType(enum.Enum):
        Linear = 0
        Angular = 1
    

class ThreeJointCoupler(Mechatronics.Coupling):
    def __init__(self) -> None: ...


class TCPSignalServerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetConnectionNames(self) -> str:
        ...
    def SetConnectionNames(self, names: str) -> None:
        ...
    def GetConnectionInformation(self, connectionName: str, remoteIP: str, remotePort: int, localIP: str, localPort: int, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.TCPSignalServerBuilder.Signal]) -> None:
        ...
    def SetConnectionInformation(self, connectionName: str, remoteIP: str, remotePort: int, localIP: str, localPort: int, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.TCPSignalServerBuilder.Signal]) -> None:
        ...
    SelectedConfigurationName: str


    class TCPSignalServerBuilderSignal():
        SignalTag: NXObject
        BChecked: bool
        Offset: str
        def ToString(self) -> str:
            ...
        def __init__(self, SignalTag: NXObject, BChecked: bool, Offset: str) -> None: ...
    

class TCPClientBuilder(Builder):
    def __init__(self) -> None: ...
    def GetConnectionNames(self, ownerParts: typing.List[Part], names: str) -> None:
        ...
    def SetConnectionNames(self, ownerParts: typing.List[Part], names: str) -> None:
        ...
    def GetConnectionInformation(self, instanceName: str, ownerPart: Part, remoteIP: str, remotePort: int, localIP: str, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.TCPClientBuilder.Signal]) -> None:
        ...
    def SetConnectionInformation(self, instanceName: str, ownerPart: Part, remoteIP: str, remotePort: int, localIP: str, rcvBufSize: int, sendBufSize: int, updateTime: float, signals: typing.List[Mechatronics.TCPClientBuilder.Signal]) -> None:
        ...
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part


    class TCPClientBuilderSignal():
        Name: str
        EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType
        EDataType: Mechatronics.SignalBuilder.DataType
        Offset: str
        def ToString(self) -> str:
            ...
    

class TagTableObject(NXObject):
    def __init__(self) -> None: ...


class TagTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.TagTableObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTagTableBuilder(self, tagTableObject: Mechatronics.TagTableObject) -> Mechatronics.TagTableBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.TagTableObject:
        ...
    def Tag(self) -> Tag: ...



class TagTableBuilder(Builder):
    def __init__(self) -> None: ...
    def Getform(self) -> Mechatronics.TagFormObject:
        ...
    def SetForm(self, form: Mechatronics.TagFormObject) -> None:
        ...
    def GenerateNewValue(self) -> str:
        ...
    def ChangeId(self, oldId: str, newId: str) -> None:
        ...
    def GetIds(self) -> str:
        ...
    def GetParameterNamesAndTypesByID(self, id: str, types: typing.List[Mechatronics.ParameterStockBuilder.DataType]) -> str:
        ...
    def GetBoolParameter(self, id: str, name: str) -> bool:
        ...
    def GetIntParameter(self, id: str, name: str) -> int:
        ...
    def GetRealParameter(self, id: str, name: str, unit: Unit) -> float:
        ...
    def GetStringParameter(self, id: str, name: str) -> str:
        ...
    def GetListParameter(self, id: str, name: str, selectedIndex: int) -> str:
        ...
    def EditBoolParameter(self, id: str, name: str, value: bool) -> None:
        ...
    def EditIntParameter(self, id: str, name: str, value: int) -> None:
        ...
    def EditRealParameter(self, id: str, name: str, value: float) -> None:
        ...
    def EditStringParameter(self, id: str, name: str, value: str) -> None:
        ...
    def EditListParameter(self, id: str, name: str, newSelectedIndex: int) -> None:
        ...
    def MoveParameterUp(self, id: str) -> None:
        ...
    def MoveParameterDown(self, id: str) -> None:
        ...
    def DeleteParameter(self, id: str) -> None:
        ...
    def DeleteAllParameters(self) -> None:
        ...
    Name: str


class TagFormObject(NXObject):
    def __init__(self) -> None: ...


class TagFormCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.TagFormObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTagFormBuilder(self, tagFormObject: Mechatronics.TagFormObject) -> Mechatronics.TagFormBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.TagFormObject:
        ...
    def Tag(self) -> Tag: ...



class TagFormBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str
    ParameterStock: Mechatronics.ParameterStockBuilder


class SystemRoot(Mechatronics.SystemObject):
    def __init__(self) -> None: ...


    class Type(enum.Enum):
        Function = 0
        Logical = 1
        Requirement = 2
    

class SystemObjectBuilder(Builder):
    def __init__(self) -> None: ...
    InstanceName: str


class SystemObject(NXObject):
    def __init__(self) -> None: ...
    def AddComponent(self, comps: typing.List[Assemblies.Component]) -> None:
        ...
    def RemoveComponent(self, comps: typing.List[Assemblies.Component]) -> None:
        ...
    def AddOperation(self, opers: typing.List[NXObject]) -> None:
        ...
    def RemoveOperation(self, opers: typing.List[NXObject]) -> None:
        ...
    def AddSignalAdapters(self, adapters: typing.List[NXObject]) -> None:
        ...
    def RemoveSignalAdapters(self, adapters: typing.List[NXObject]) -> None:
        ...
    def RestructureObject(self, pDestination: Mechatronics.SystemObject) -> None:
        ...
    def AddPhysicsObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def RemovePhysicsObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def GetPhysicsObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def ReorderObject(self, pDestination: Mechatronics.SystemObject, beforeOrAfter: Mechatronics.SystemObject.ReorderType) -> None:
        ...
    def RenameInstance(self, name: str) -> None:
        ...
    def CreateTraceLink(self, pComplying: Mechatronics.SystemObject) -> None:
        ...
    def RemoveTraceLink(self, pComplying: Mechatronics.SystemObject) -> None:
        ...
    def GetSingleDesignation(self) -> str:
        ...
    def SetSingleDesignation(self, designation: str) -> None:
        ...
    def ApplyNamingRule(self) -> None:
        ...
    def AssociateItem(self, type: Mechatronics.SystemObject.RelationType, itemMFKID: str, revisionID: str) -> None:
        ...
    def GetAssociateItem(self, type: Mechatronics.SystemObject.RelationType, itemMFKID: str, revisionID: str) -> None:
        ...
    def DissociateItem(self, itemMFKID: str, revisionID: str) -> None:
        ...


    class ReorderType(enum.Enum):
        Before = 1
        After = 2
    

    class RelationType(enum.Enum):
        Ecad = 1
    

class SymbolTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SymbolTable]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSymbolTableBuilder(self, symbolTable: Mechatronics.SymbolTable) -> Mechatronics.SymbolTableBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.SymbolTable:
        ...
    def Tag(self) -> Tag: ...



class SymbolTableBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSymbols(self) -> typing.List[Mechatronics.SymbolTableBuilder.Symbol]:
        ...
    def SetSymbols(self, symbols: typing.List[Mechatronics.SymbolTableBuilder.Symbol]) -> None:
        ...
    Name: str


    class SymbolTableBuilderSymbol():
        Name: str
        EIOType: Mechatronics.SymbolTableBuilder.IOType
        EDataType: Mechatronics.SymbolTableBuilder.DataType
        Address: str
        Comment: str
        def ToString(self) -> str:
            ...
    

    class IOType(enum.Enum):
        Input = 0
        Output = 1
        Inout = 2
    

    class DataType(enum.Enum):
        Bool = 0
        Int = 1
        Double = 2
    

class SymbolTable(NXObject):
    def __init__(self) -> None: ...


class SpringDamperCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SpringDamper]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSpringDamperBuilder(self, springDamper: Mechatronics.SpringDamper) -> Mechatronics.SpringDamperBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.SpringDamper:
        ...
    def Tag(self) -> Tag: ...



class SpringDamperBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    AxisJoint: Mechatronics.SelectPhysicsJoint
    AxisType: Mechatronics.SpringDamperBuilder.AxisJointType
    Damping: Expression
    RelaxedPosition: Expression
    SpringConstant: Expression


    class AxisJointType(enum.Enum):
        Angular = 0
        Linear = 1
    

class SpringDamper(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class SpeedPositionControlDirectiontype(enum.Enum):
    Parallel = 0
    Perpendicular = 1


class SpeedControlCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SpeedControl]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSpeedControlBuilder(self, speedControl: Mechatronics.SpeedControl) -> Mechatronics.SpeedControlBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.SpeedControl:
        ...
    def Tag(self) -> Tag: ...



class SpeedControlBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetAxisJoint(self, axisJoint: NXObject) -> None:
        ...
    AxisJoint: Mechatronics.SelectPhysicsJoint
    AxisType: Mechatronics.SpeedControlBuilder.AxisJointType
    DirectionType: Mechatronics.SpeedPositionControlDirectiontype
    EnableLimitForce: bool
    ForwardForce: Expression
    LimitJerk: bool
    MaxAcceleration: Expression
    MaxJerk: Expression
    ReverseForce: Expression
    Signal: SelectNXObject
    Speed: Expression
    UseAcceleration: bool


    class AxisJointType(enum.Enum):
        Angular = 0
        Linear = 1
        Mixed = 2
    

class SpeedControl(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class SlidingJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SlidingJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSlidingJointBuilder(self, slide: Mechatronics.SlidingJoint) -> Mechatronics.SlidingJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.SlidingJoint:
        ...
    def Tag(self) -> Tag: ...



class SlidingJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AttachPoint: Point
    EnableLowerLimit: bool
    EnableUpperLimit: bool
    FeedbackPoint: Point
    LowerLimit: Expression
    Offset: Expression
    UpperLimit: Expression
    Vector: Direction


class SlidingJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class SignalMappingConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SignalMappingConnection]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Mechatronics.SignalMappingConnection:
        ...
    def CreateConnectionBuilder(self, connection: Mechatronics.SignalMappingConnection) -> Mechatronics.SignalMappingConnectionBuilder:
        ...
    def Tag(self) -> Tag: ...



class SignalMappingConnectionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.SignalMappingConnectionBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.SignalMappingConnectionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.SignalMappingConnectionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.SignalMappingConnectionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.SignalMappingConnectionBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.SignalMappingConnectionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.SignalMappingConnectionBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.SignalMappingConnectionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.SignalMappingConnectionBuilder, object2: Mechatronics.SignalMappingConnectionBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.SignalMappingConnectionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SignalMappingConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    Adapter: Mechatronics.SignalAdapter
    ClientType: Mechatronics.SignalMappingBuilder.AppOption
    ConfigurationName: str
    ConfigurationPart: NXObject
    ConnectionName: str
    ExternalSignalName: str
    Signal: NXObject


class SignalMappingConnection(DisplayableObject):
    def __init__(self) -> None: ...


class SignalMappingBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFolder(self, tgFolder: Mechatronics.PMNavFolderObject) -> None:
        ...
    ConnectionList: Mechatronics.SignalMappingConnectionBuilderList
    MATLABSignalConnectionList: Mechatronics.MATLABSignalConnectionBuilderList
    SHMSignalConnectionList: Mechatronics.SHMSignalConnectionBuilderList
    SignalConnectionList: Mechatronics.SignalConnectionBuilderList


    class AppOption(enum.Enum):
        Opcda = 0
        Opcua = 1
        Shm = 2
        Matlab = 3
        Plcsimadv = 4
        Tcp = 5
        Udp = 6
        Profinet = 7
    

class SignalConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SignalConnection]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Mechatronics.SignalConnection:
        ...
    def CreateSignalConnectionBuilder(self, connection: Mechatronics.SignalConnection) -> Mechatronics.SignalConnectionBuilder:
        ...
    def Tag(self) -> Tag: ...



class SignalConnectionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.SignalConnectionBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.SignalConnectionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.SignalConnectionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.SignalConnectionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.SignalConnectionBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.SignalConnectionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.SignalConnectionBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.SignalConnectionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.SignalConnectionBuilder, object2: Mechatronics.SignalConnectionBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.SignalConnectionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SignalConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    AdapterTag: Mechatronics.SignalAdapter
    OPCServerName: str
    OPCSignalAccess: Mechatronics.OPCClientBuilder.TagAccess
    OPCSignalName: str
    OPCSignalType: Mechatronics.SignalConnectionBuilder.DataType
    ResultName: str
    SignalTag: NXObject
    StreamIO: int


    class DataType(enum.Enum):
        Unknown = 0
        Integer = 1
        Float = 2
        Boolean = 3
        String = 4
    

class SignalConnection(DisplayableObject):
    def __init__(self) -> None: ...


class SignalCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Signal]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSignalBuilder(self, symbolTable: Mechatronics.Signal) -> Mechatronics.SignalBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Signal:
        ...
    def Tag(self) -> Tag: ...



class SignalBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSignalData(self) -> Mechatronics.SignalBuilder.Signal:
        ...
    def SetSignalData(self, signalData: Mechatronics.SignalBuilder.Signal) -> None:
        ...
    Name: str


    class SignalBuilderSignal():
        TgPhysicsObject: NXObject
        NPhysicsPropTag: int
        EIOType: Mechatronics.SignalBuilder.IOType
        EDataType: Mechatronics.SignalBuilder.DataType
        BoolValueExp: Expression
        IntValueExp: Expression
        DoubleValueExp: Expression
        def ToString(self) -> str:
            ...
    

    class IOType(enum.Enum):
        Input = 0
        Output = 1
    

    class ExternalSignalIOType(enum.Enum):
        Input = 0
        Output = 1
        Inout = 2
    

    class DataType(enum.Enum):
        Bool = 0
        Int = 1
        Double = 2
    

class SignalAdapterCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SignalAdapter]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSignalAdapterBuilder(self, object: Mechatronics.SignalAdapter) -> Mechatronics.SignalAdapterBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.SignalAdapter:
        ...
    def Tag(self) -> Tag: ...



class SignalAdapterBuilder(Builder):
    def __init__(self) -> None: ...
    def GetParameterData(self) -> typing.List[Mechatronics.SignalAdapterBuilder.ParameterData]:
        ...
    def SetParameterData(self, parameterData: typing.List[Mechatronics.SignalAdapterBuilder.ParameterData]) -> None:
        ...
    def GetSignalData(self) -> typing.List[Mechatronics.SignalAdapterBuilder.SignalData]:
        ...
    def SetSignalData(self, signalData: typing.List[Mechatronics.SignalAdapterBuilder.SignalData]) -> None:
        ...
    MaxSignalId: int
    Name: str


    class SignalAdapterBuilderSignalData():
        Name: str
        DataType: Mechatronics.SignalAdapterBuilder.DataType
        PortType: Mechatronics.SignalAdapterBuilder.DataPortType
        BoolValue: bool
        IntValue: int
        DoubleValue: float
        Unit: Unit
        SignalId: int
        EditedSignal: Mechatronics.AdapterSignal
        AssignedFormula: Mechatronics.AdapterFormula
        Formula: str
        Comment: str
        def ToString(self) -> str:
            ...
    

    class SignalAdapterBuilderParameterData():
        AliasName: str
        PhysicsObject: NXObject
        PhysicsPropTag: int
        AssignedFormula: Mechatronics.AdapterFormula
        Formula: str
        Comment: str
        def ToString(self) -> str:
            ...
    

    class DataType(enum.Enum):
        Bool = 0
        Int = 1
        Double = 2
    

    class DataPortType(enum.Enum):
        Input = 0
        Output = 1
    

class SignalAdapter(DisplayableObject):
    def __init__(self) -> None: ...


class Signal(NXObject):
    def __init__(self) -> None: ...


class SHMSignalProviderBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSHMSignals(self) -> typing.List[Mechatronics.SHMSignalProviderBuilder.SignalInfo]:
        ...
    def SetSHMSignals(self, signalInfos: typing.List[Mechatronics.SHMSignalProviderBuilder.SignalInfo]) -> None:
        ...
    CreateShm: bool
    IsLittleEndian: bool
    ShmMutex: str
    ShmName: str


    class SHMSignalProviderBuilderSignalInfo():
        SignalTag: NXObject
        BChecked: bool
        Address: str
        def ToString(self) -> str:
            ...
        def __init__(self, SignalTag: NXObject, BChecked: bool, Address: str) -> None: ...
    

class SHMSignalConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.SHMSignalConnection]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Mechatronics.SHMSignalConnection:
        ...
    def CreateSHMSignalConnectionBuilder(self, connection: Mechatronics.SHMSignalConnection) -> Mechatronics.SHMSignalConnectionBuilder:
        ...
    def Tag(self) -> Tag: ...



class SHMSignalConnectionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.SHMSignalConnectionBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.SHMSignalConnectionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.SHMSignalConnectionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.SHMSignalConnectionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.SHMSignalConnectionBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.SHMSignalConnectionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.SHMSignalConnectionBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.SHMSignalConnectionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.SHMSignalConnectionBuilder, object2: Mechatronics.SHMSignalConnectionBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.SHMSignalConnectionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SHMSignalConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    AdapterObject: Mechatronics.SignalAdapter
    Endian: Mechatronics.SHMSignalConnectionBuilder.EndianType
    ResultName: str
    SHMName: str
    SHMSignalAccess: Mechatronics.SHMSignalConnectionBuilder.SHMSignalAccessType
    SHMSignalName: str
    SHMSignalType: Mechatronics.SHMSignalConnectionBuilder.DataType
    SignalObject: NXObject
    StreamIO: Mechatronics.SHMSignalConnectionBuilder.StreamIOType


    class StreamIOType(enum.Enum):
        Tomcd = 0
        Toshm = 1
    

    class SHMSignalAccessType(enum.Enum):
        Read = 0
        Write = 1
    

    class EndianType(enum.Enum):
        Little = 0
        Big = 1
    

    class DataType(enum.Enum):
        Bool = 0
        Int = 1
        Double = 2
    

class SHMSignalConnection(DisplayableObject):
    def __init__(self) -> None: ...


class SHMSignalClientBuilder(Builder):
    def __init__(self) -> None: ...
    def RefreshRegisteredInstances(self, instanceNames: str) -> None:
        ...
    def SetSignals(self, configurationName: str, signalInfo: typing.List[Mechatronics.SHMSignalClientBuilder.SHMSignal]) -> None:
        ...
    def GetSignals(self, configurationName: str) -> typing.List[Mechatronics.SHMSignalClientBuilder.SHMSignal]:
        ...
    def SetSHMInstance(self, instanceName: str, eEndianType: Mechatronics.SHMSignalClientBuilder.EndianType, strStatus: str) -> None:
        ...
    def GetSHMInstance(self, instanceName: str, eEndianType: Mechatronics.SHMSignalClientBuilder.EndianType, strStatus: str) -> None:
        ...
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part


    class SHMSignalClientBuilderSHMSignal():
        SignalName: str
        EDataType: Mechatronics.SignalBuilder.DataType
        Value: str
        EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType
        def ToString(self) -> str:
            ...
    

    class SHMSignalClientBuilderSHMInfo():
        Name: str
        EndianType: Mechatronics.SHMSignalClientBuilder.EndianType
        Status: str
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, EndianType: Mechatronics.SHMSignalClientBuilder.EndianType, Status: str) -> None: ...
    

    class EndianType(enum.Enum):
        Little = 0
        Big = 1
    

class SHMConfigurationBuilder(Builder):
    def __init__(self) -> None: ...
    SHMSignalConnectionList: Mechatronics.SHMSignalConnectionBuilderList


class SensorsActuatorsListBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.SensorsActuatorsListBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.SensorsActuatorsListBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.SensorsActuatorsListBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.SensorsActuatorsListBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.SensorsActuatorsListBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.SensorsActuatorsListBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.SensorsActuatorsListBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.SensorsActuatorsListBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.SensorsActuatorsListBuilder, object2: Mechatronics.SensorsActuatorsListBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.SensorsActuatorsListBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SensorsActuatorsListBuilder(Builder):
    def __init__(self) -> None: ...
    def GetParameterData(self) -> typing.List[Mechatronics.SensorsActuatorsListBuilder.ParameterData]:
        ...
    def SetParameterData(self, parameterData: typing.List[Mechatronics.SensorsActuatorsListBuilder.ParameterData]) -> None:
        ...
    ObjectName: str
    SimitFolder: str
    SimitTemplate: str


    class SensorsActuatorsListBuilderParameterData():
        Name: str
        Value: str
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, Value: str) -> None: ...
    

class SelectTagFormObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Mechatronics.TagFormObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Mechatronics.TagFormObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.TagFormObject, view1: View, point1: Point3d, selection2: Mechatronics.TagFormObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.TagFormObject, view1: View, point1: Point3d, selection2: Mechatronics.TagFormObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Mechatronics.TagFormObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Mechatronics.TagFormObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Mechatronics.TagFormObject


class SelectSystemObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Mechatronics.SystemObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Mechatronics.SystemObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.SystemObject, view1: View, point1: Point3d, selection2: Mechatronics.SystemObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.SystemObject, view1: View, point1: Point3d, selection2: Mechatronics.SystemObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Mechatronics.SystemObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Mechatronics.SystemObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Mechatronics.SystemObject


class SelectRigidBody(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Mechatronics.RigidBody, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Mechatronics.RigidBody, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.RigidBody, view1: View, point1: Point3d, selection2: Mechatronics.RigidBody, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.RigidBody, view1: View, point1: Point3d, selection2: Mechatronics.RigidBody, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Mechatronics.RigidBody, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Mechatronics.RigidBody:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Mechatronics.RigidBody


class SelectPneumaticCylinderList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Mechatronics.PneumaticCylinder) -> bool:
        ...
    def Add(self, objects: typing.List[Mechatronics.PneumaticCylinder]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Mechatronics.PneumaticCylinder, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Mechatronics.PneumaticCylinder) -> bool:
        ...
    def Remove(self, object: Mechatronics.PneumaticCylinder, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.PneumaticCylinder, view1: View, point1: Point3d, selection2: Mechatronics.PneumaticCylinder, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Mechatronics.PneumaticCylinder]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Mechatronics.PneumaticCylinder) -> bool:
        ...
    def SetArray(self, objects: typing.List[Mechatronics.PneumaticCylinder]) -> None:
        ...
    def GetArray(self) -> typing.List[Mechatronics.PneumaticCylinder]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.PneumaticCylinder, view1: View, point1: Point3d, selection2: Mechatronics.PneumaticCylinder, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Mechatronics.PneumaticCylinder, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectPhysicsJoint(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Mechatronics.PhysicsJoint, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Mechatronics.PhysicsJoint, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.PhysicsJoint, view1: View, point1: Point3d, selection2: Mechatronics.PhysicsJoint, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.PhysicsJoint, view1: View, point1: Point3d, selection2: Mechatronics.PhysicsJoint, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Mechatronics.PhysicsJoint, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Mechatronics.PhysicsJoint:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Mechatronics.PhysicsJoint


class SelectPhysicsConstraint(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Mechatronics.PhysicsConstraint, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Mechatronics.PhysicsConstraint, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.PhysicsConstraint, view1: View, point1: Point3d, selection2: Mechatronics.PhysicsConstraint, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.PhysicsConstraint, view1: View, point1: Point3d, selection2: Mechatronics.PhysicsConstraint, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Mechatronics.PhysicsConstraint, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Mechatronics.PhysicsConstraint:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Mechatronics.PhysicsConstraint


class SelectLogicObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Mechatronics.LogicObject) -> bool:
        ...
    def Add(self, objects: typing.List[Mechatronics.LogicObject]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Mechatronics.LogicObject, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Mechatronics.LogicObject) -> bool:
        ...
    def Remove(self, object: Mechatronics.LogicObject, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.LogicObject, view1: View, point1: Point3d, selection2: Mechatronics.LogicObject, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Mechatronics.LogicObject]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Mechatronics.LogicObject) -> bool:
        ...
    def SetArray(self, objects: typing.List[Mechatronics.LogicObject]) -> None:
        ...
    def GetArray(self) -> typing.List[Mechatronics.LogicObject]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.LogicObject, view1: View, point1: Point3d, selection2: Mechatronics.LogicObject, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Mechatronics.LogicObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectHydraulicCylinderList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Mechatronics.HydraulicCylinder) -> bool:
        ...
    def Add(self, objects: typing.List[Mechatronics.HydraulicCylinder]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Mechatronics.HydraulicCylinder, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Mechatronics.HydraulicCylinder) -> bool:
        ...
    def Remove(self, object: Mechatronics.HydraulicCylinder, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.HydraulicCylinder, view1: View, point1: Point3d, selection2: Mechatronics.HydraulicCylinder, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Mechatronics.HydraulicCylinder]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Mechatronics.HydraulicCylinder) -> bool:
        ...
    def SetArray(self, objects: typing.List[Mechatronics.HydraulicCylinder]) -> None:
        ...
    def GetArray(self) -> typing.List[Mechatronics.HydraulicCylinder]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.HydraulicCylinder, view1: View, point1: Point3d, selection2: Mechatronics.HydraulicCylinder, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Mechatronics.HydraulicCylinder, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCollisionSensorList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Mechatronics.CollisionSensor) -> bool:
        ...
    def Add(self, objects: typing.List[Mechatronics.CollisionSensor]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Mechatronics.CollisionSensor, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Mechatronics.CollisionSensor) -> bool:
        ...
    def Remove(self, object: Mechatronics.CollisionSensor, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.CollisionSensor, view1: View, point1: Point3d, selection2: Mechatronics.CollisionSensor, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Mechatronics.CollisionSensor]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Mechatronics.CollisionSensor) -> bool:
        ...
    def SetArray(self, objects: typing.List[Mechatronics.CollisionSensor]) -> None:
        ...
    def GetArray(self) -> typing.List[Mechatronics.CollisionSensor]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.CollisionSensor, view1: View, point1: Point3d, selection2: Mechatronics.CollisionSensor, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Mechatronics.CollisionSensor, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCollisionSensor(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Mechatronics.CollisionSensor, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Mechatronics.CollisionSensor, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.CollisionSensor, view1: View, point1: Point3d, selection2: Mechatronics.CollisionSensor, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.CollisionSensor, view1: View, point1: Point3d, selection2: Mechatronics.CollisionSensor, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Mechatronics.CollisionSensor, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Mechatronics.CollisionSensor:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Mechatronics.CollisionSensor


class SelectClassificationBuilder(Tooling.SelectReuseLibraryItemBuilder):
    def __init__(self) -> None: ...
    ClassId: str


class SelectAdapterSignal(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Mechatronics.AdapterSignal, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Mechatronics.AdapterSignal, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.AdapterSignal, view1: View, point1: Point3d, selection2: Mechatronics.AdapterSignal, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Mechatronics.AdapterSignal, view1: View, point1: Point3d, selection2: Mechatronics.AdapterSignal, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Mechatronics.AdapterSignal, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Mechatronics.AdapterSignal:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Mechatronics.AdapterSignal


class ScrewJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ScrewJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateScrewJointBuilder(self, cylinJoint: Mechatronics.ScrewJoint) -> Mechatronics.ScrewJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ScrewJoint:
        ...
    def Tag(self) -> Tag: ...



class ScrewJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AxisVector: Direction
    ExpressionRatio: Expression
    PointOrigin: Point


class ScrewJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class SCOUTImportBuilder(Builder):
    def __init__(self) -> None: ...
    def ImportFromScout(self, camProfile: Mechatronics.CamProfileBuilder) -> None:
        ...
    ImportFile: str


class SCOUTExportBuilder(Builder):
    def __init__(self) -> None: ...
    def ExportToScout(self, camProfile: Builder) -> None:
        ...
    def ExportToScoutWithFormula(self, camProfile: Mechatronics.CamProfileBuilder) -> None:
        ...
    def ExportToPointXyValue(self, camProfile: Mechatronics.CamProfileBuilder) -> None:
        ...
    ExportFile: str
    ExportFileFormat: Mechatronics.SCOUTExportBuilder.ExportFileType


    class ExportFileType(enum.Enum):
        Csv = 0
        Xml = 1
        Vdi = 2
    

class RuntimeNCObject(NXObject):
    def __init__(self) -> None: ...


class RuntimeNCCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.RuntimeNCObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRuntimeNcBuilder(self, runtimeNCObject: Mechatronics.RuntimeNCObject) -> Mechatronics.RuntimeNCBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.RuntimeNCObject:
        ...
    def Tag(self) -> Tag: ...



class RuntimeNCBuilder(Builder):
    def __init__(self) -> None: ...
    def LoadNCFile(self, ncFile: str) -> None:
        ...
    def UpdateNCCode(self, ncCodeLines: str) -> None:
        ...
    def ExportNCCode(self, ncFile: str) -> None:
        ...
    def RunCSE(self, isRunningOK: bool, errMsg: str, lineNum: int, ncLine: str) -> None:
        ...
    def GetAxesAndMachineEvents(self, axisNames: str, machineEventNames: str) -> None:
        ...
    def GetMCDConnection(self, isAxis: bool, axisOrEventName: str) -> TaggedObject:
        ...
    def SetMCDConnection(self, isAxis: bool, axisOrEventName: str, mcdConnectedTag: TaggedObject) -> None:
        ...
    FlagOfUsingContainer: bool
    FlagOfUsingSpecifiedMCF: bool
    Name: str
    SpecifiedMCF: str


class RuntimeFormulaParameterBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.RuntimeFormulaParameterBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.RuntimeFormulaParameterBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.RuntimeFormulaParameterBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.RuntimeFormulaParameterBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.RuntimeFormulaParameterBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.RuntimeFormulaParameterBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.RuntimeFormulaParameterBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.RuntimeFormulaParameterBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.RuntimeFormulaParameterBuilder, object2: Mechatronics.RuntimeFormulaParameterBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.RuntimeFormulaParameterBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class RuntimeFormulaParameterBuilder(Builder):
    def __init__(self) -> None: ...
    Alias: str
    ParameterPhysics: NXObject
    RuntimePropertyTag: int


class RuntimeFormulaParameter(NXObject):
    def __init__(self) -> None: ...


class RuntimeFormulaCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.RuntimeFormula]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRuntimeFormulaBuilder(self, formula: Mechatronics.RuntimeFormula) -> Mechatronics.RuntimeFormulaBuilder:
        ...
    def CreateRuntimeFormulaParameterBuilder(self, obj: Mechatronics.RuntimeFormulaParameter) -> Mechatronics.RuntimeFormulaParameterBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.RuntimeFormula:
        ...
    def Tag(self) -> Tag: ...



class RuntimeFormulaBuilder(Builder):
    def __init__(self) -> None: ...
    DestPropertyId: int
    FormulaName: str
    FormulaString: str
    ObjectToAssignParamSelection: SelectNXObject
    ParameterBuilderList: Mechatronics.RuntimeFormulaParameterBuilderList
    SelectionInputObject: SelectNXObjectList


class RuntimeFormula(NXObject):
    def __init__(self) -> None: ...


class RuntimeBehaviorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.RuntimeBehavior]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRuntimeBehaviorBuilder(self, codeObj: Mechatronics.RuntimeBehavior) -> Mechatronics.RuntimeBehaviorBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.RuntimeBehavior:
        ...
    def Tag(self) -> Tag: ...



class RuntimeBehaviorBuilder(Builder):
    def __init__(self) -> None: ...
    def StoreExecutableCode(self, fileSpec: str, source: str) -> None:
        ...
    def SetPhysicsObject(self, className: str, propIndex: int, physicsObject: NXObject) -> None:
        ...
    def SetReplacementCode(self, physicsObject: NXObject) -> None:
        ...
    Name: str
    Source: str


class RuntimeBehavior(NXObject):
    def __init__(self) -> None: ...


class RigidBodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.RigidBody]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRigidBodyBuilder(self, rigidBody: Mechatronics.RigidBody) -> Mechatronics.RigidBodyBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.RigidBody:
        ...
    def Tag(self) -> Tag: ...



class RigidBodyBuilder(Builder):
    def __init__(self) -> None: ...
    def SetGeometry(self, geometries: typing.List[NXObject]) -> None:
        ...
    AngularVelocityDirection: Direction
    AngularVelocityMagnitude: Expression
    Geometry: SelectNXObjectList
    InertiaIxx: Expression
    InertiaIxy: Expression
    InertiaIxz: Expression
    InertiaIyy: Expression
    InertiaIyz: Expression
    InertiaIzz: Expression
    LinearVelocityDirection: Direction
    LinearVelocityMagnitude: Expression
    Mass: Expression
    MassCenterPoint: Point
    MassProperty: Mechatronics.RigidBodyBuilder.MassPropertiesOption
    Name: str
    Orientation: CoordinateSystem
    TagForm: Mechatronics.SelectTagFormObject


    class MassPropertiesOption(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

class RigidBody(DisplayableObject):
    def __init__(self) -> None: ...


class RequirementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Requirement]:
        ...
    def __init__(self, owner: Mechatronics.MechatronicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRequirementBuilder(self, object: Mechatronics.Requirement) -> Mechatronics.RequirementBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Requirement:
        ...
    def Tag(self) -> Tag: ...



class RequirementBuilder(Mechatronics.SystemObjectBuilder):
    def __init__(self) -> None: ...
    ObjectInformation: Mechatronics.ObjectInformationBuilder
    ParentFunction: NXObject


class Requirement(Mechatronics.SystemObject):
    def __init__(self) -> None: ...


class ReplacePhysicsBuilder(Builder):
    def __init__(self) -> None: ...
    def ScanPhysicsObject(self, replacedPartOcc: Assemblies.Component) -> None:
        ...
    def MappingNewphysicsFileid(self, originalPhysicsObjectPrototypeFileId: str, newFileId: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Mechatronics.ReplacePhysicsBuilder.MappingNewphysicsObject instead.")"""
        ...
    def MappingNewphysicsObject(self, originalPhysicsObjectPrototypeFileId: str, newPhysicsObj: NXObject) -> None:
        ...
    def SetReplacementStatus(self, status: bool) -> None:
        ...


class RelayCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Relay]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRelayBuilder(self, relay: Mechatronics.Relay) -> Mechatronics.RelayBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Relay:
        ...
    def Tag(self) -> Tag: ...



class RelayBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    LowerLimit: Expression
    PersistentTag: int
    SelectedPhysicsObject: SelectNXObject
    UpperLimit: Expression


class Relay(DisplayableObject):
    def __init__(self) -> None: ...


class ReadWriteDeviceObject(NXObject):
    def __init__(self) -> None: ...


class ReadWriteDeviceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ReadWriteDeviceObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateReadWriteDeviceBuilder(self, readWriteObject: Mechatronics.ReadWriteDeviceObject) -> Mechatronics.ReadWriteDeviceBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ReadWriteDeviceObject:
        ...
    def Tag(self) -> Tag: ...



class ReadWriteDeviceBuilder(Builder):
    def __init__(self) -> None: ...
    def GetForm(self) -> Mechatronics.TagFormObject:
        ...
    def SetForm(self, form: Mechatronics.TagFormObject) -> None:
        ...
    def GetTable(self) -> Mechatronics.TagTableObject:
        ...
    def SetTable(self, table: Mechatronics.TagTableObject) -> None:
        ...
    def GetDeviceType(self) -> Mechatronics.ReadWriteDeviceBuilder.DeviceType:
        ...
    def SetDeviceType(self, type: Mechatronics.ReadWriteDeviceBuilder.DeviceType) -> None:
        ...
    def GetExecuteMode(self) -> Mechatronics.ReadWriteDeviceBuilder.ExecuteMode:
        ...
    def SetExecuteMode(self, mode: Mechatronics.ReadWriteDeviceBuilder.ExecuteMode) -> None:
        ...
    Name: str
    Sensor: Mechatronics.SelectCollisionSensor


    class ExecuteMode(enum.Enum):
        None = 0
        Always = 1
        OnceOnly = 2
    

    class DeviceType(enum.Enum):
        Reader = 0
        Writer = 1
    

class RackPinionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.RackPinion]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRackPinionBuilder(self, rackPinion: Mechatronics.RackPinion) -> Mechatronics.RackPinionBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.RackPinion:
        ...
    def Tag(self) -> Tag: ...



class RackPinionBuilder(Mechatronics.CouplingBuilder):
    def __init__(self) -> None: ...
    ContactPoint: Point
    Radius: Expression


class RackPinion(Mechatronics.Coupling):
    def __init__(self) -> None: ...


class ProxyOverrideObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ProxyOverrideObject]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self, proxyObjectOcc: NXObject) -> Mechatronics.ProxyOverrideObjectBuilder:
        ...
    def CreateProxyObjectParameterBuilder(self) -> Mechatronics.ProxyObjectParameterBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ProxyOverrideObject:
        ...
    def Tag(self) -> Tag: ...



class ProxyOverrideObjectBuilder(Builder):
    def __init__(self) -> None: ...
    Attachment: SelectNXObject
    Context: BasePart
    HasAttachment: bool
    ParameterList: Mechatronics.ProxyObjectParameterBuilderList
    ProxyObject: NXObject
    ProxyOverrideObjectName: str


    class AttrType(enum.Enum):
        Bool = 0
        Int = 1
        Double = 2
    

    class AttrBoolValue(enum.Enum):
        False = 0
        True = 1
    

class ProxyOverrideObject(NXObject):
    def __init__(self) -> None: ...


class ProxyObjectParameterBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.ProxyObjectParameterBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.ProxyObjectParameterBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.ProxyObjectParameterBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.ProxyObjectParameterBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.ProxyObjectParameterBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.ProxyObjectParameterBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.ProxyObjectParameterBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.ProxyObjectParameterBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.ProxyObjectParameterBuilder, object2: Mechatronics.ProxyObjectParameterBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.ProxyObjectParameterBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ProxyObjectParameterBuilder(Builder):
    def __init__(self) -> None: ...
    AttrName: str
    AttrType: int
    BoolValue: Expression
    IntValue: Expression
    ParamId: int
    RealValue: Expression


class ProxyObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ProxyObject]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateProxyObjectBuilder(self, proxyObject: Mechatronics.ProxyObject) -> Mechatronics.ProxyObjectBuilder:
        ...
    def CreateProxyObjectParameterBuilder(self) -> Mechatronics.ProxyObjectParameterBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ProxyObject:
        ...
    def Tag(self) -> Tag: ...



class ProxyObjectBuilder(Builder):
    def __init__(self) -> None: ...
    BuilderType: Mechatronics.ProxyObjectBuilder.Type
    Context: BasePart
    MaxParamId: int
    ParameterList: Mechatronics.ProxyObjectParameterBuilderList
    ProxyObjectName: str
    SelectGeomObject: SelectNXObjectList
    SelectPhysicsObject: SelectNXObjectList
    UseType: int


    class Type(enum.Enum):
        RuntimeParameters = 0
        ProxyObject = 1
    

class ProxyObject(DisplayableObject):
    def __init__(self) -> None: ...


class ProfinetClientBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTags(self, tagInfos: typing.List[Mechatronics.ProfinetClientBuilder.TagInfo]) -> None:
        ...
    def GetTags(self) -> typing.List[Mechatronics.ProfinetClientBuilder.TagInfo]:
        ...
    InstanceName: str
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part


    class ProfinetClientBuilderTagInfo():
        StrName: str
        EDataType: Mechatronics.SignalBuilder.DataType
        EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType
        Address: str
        BDint: bool
        def ToString(self) -> str:
            ...
    

class PreventCollisionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PreventCollision]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePreventCollisionBuilder(self, preventCollision: Mechatronics.PreventCollision) -> Mechatronics.PreventCollisionBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PreventCollision:
        ...
    def Tag(self) -> Tag: ...



class PreventCollisionBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetFirstBody(self, firstBody: DisplayableObject) -> None:
        ...
    def SetSecondBody(self, secondBody: DisplayableObject) -> None:
        ...
    FirstBody: SelectDisplayableObject
    SecondBody: SelectDisplayableObject


class PreventCollision(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class PreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    AngularDampingExpression: Expression
    CoSimulation: bool
    CollisionPrecision: float
    CollisionPrecisionExpression: Expression
    ConnectURL: str
    DynamicFriction: float
    DynamicFrictionExpression: Expression
    EnablePlcSimAdvTimeSyn: bool
    EnableTimeSync: bool
    ErrorReduction: float
    ErrorReductionExpression: Expression
    FilePicker: str
    ForwardStepTime: Expression
    GeometryHighlight: bool
    Gx: Expression
    Gy: Expression
    Gz: Expression
    InvokeExport: bool
    LinearDampingExpression: Expression
    LoadAsSaved: bool
    MasterType: Mechatronics.PreferencesBuilder.MasterTypes
    MaxIteration: int
    MaxIterationExpression: Expression
    RefreshPrecision: float
    Restitution: float
    RestitutionExpression: Expression
    RevisionRule: str
    RollingFrictionExpression: Expression
    ShapeHighlight: bool
    SpringForceMultiplier: float
    SpringForceMultiplierExpression: Expression
    StaticFriction: float
    StaticFrictionExpression: Expression
    StepSize: Expression
    StepTime: float
    StepTimeExpression: Expression
    StickyFactor: float
    StickyForce: Expression
    SynchronizationTime: Expression
    TimeScaleFactor: float
    Tolerance: float
    ToleranceExpression: Expression


    class MasterTypes(enum.Enum):
        Mcd = 0
        Simit = 1
    

class PositionSensorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PositionSensor]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePositionSensorBuilder(self, positionSensor: Mechatronics.PositionSensor) -> Mechatronics.PositionSensorBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PositionSensor:
        ...
    def Tag(self) -> Tag: ...



class PositionSensorBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    AxisJoint: SelectNXObject
    AxisType: Mechatronics.PositionSensorBuilder.AxisJointType
    LowerOutputRange: Expression
    LowerTrimRange: Expression
    MeasureType: Mechatronics.PositionSensorBuilder.OutputMeasureType
    UpperOutputRange: Expression
    UpperTrimRange: Expression
    UseScale: bool
    UseTrim: bool


    class OutputMeasureType(enum.Enum):
        Constant = 0
        Voltage = 1
        Current = 2
    

    class AxisJointType(enum.Enum):
        Angular = 0
        Linear = 1
    

class PositionSensor(DisplayableObject):
    def __init__(self) -> None: ...


class PositionControlCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PositionControl]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePositionControlBuilder(self, positionControl: Mechatronics.PositionControl) -> Mechatronics.PositionControlBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PositionControl:
        ...
    def Tag(self) -> Tag: ...



class PositionControlBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetAxisJoint(self, axisJoint: NXObject) -> None:
        ...
    AngularPath: Mechatronics.PositionControlBuilder.AngularPathOptions
    AxisJoint: Mechatronics.SelectPhysicsJoint
    AxisType: Mechatronics.PositionControlBuilder.Axis
    Destination: Expression
    DirectionType: Mechatronics.SpeedPositionControlDirectiontype
    EnableLimitForce: bool
    ForwardForce: Expression
    LimitJerk: bool
    MaxAcceleration: Expression
    MaxDeceleration: Expression
    MaxJerk: Expression
    ReverseForce: Expression
    Signal: SelectNXObject
    Speed: Expression
    UseAcceleration: bool


    class Axis(enum.Enum):
        Angular = 0
        Linear = 1
        Mixed = 2
    

    class AngularPathOptions(enum.Enum):
        FollowShortestPath = 0
        RotateClockwise = 1
        RotateCounterclockwise = 2
        TrackMultipleTurns = 3
    

class PositionControl(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class PointOnCurveJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PointOnCurveJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePointOnCurveJointBuilder(self, joint: Mechatronics.PointOnCurveJoint) -> Mechatronics.PointOnCurveJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PointOnCurveJoint:
        ...
    def Tag(self) -> Tag: ...



class PointOnCurveJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    def GetConnectedCurves(self) -> typing.List[NXObject]:
        ...
    def SetConnectedCurves(self, curves: typing.List[NXObject]) -> None:
        ...
    def EvaluatePath(self, curves: typing.List[NXObject]) -> None:
        ...
    AxisVector: Direction
    Offset: Expression
    PointOnCurve: Point


class PointOnCurveJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class PneumaticValveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PneumaticValve]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePneumaticValveBuilder(self, pneumaticValve: Mechatronics.PneumaticValve) -> Mechatronics.PneumaticValveBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PneumaticValve:
        ...
    def Tag(self) -> Tag: ...



class PneumaticValveBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetCylinders(self, cylinders: typing.List[Mechatronics.PneumaticCylinder]) -> None:
        ...
    ControlInput: Expression
    Cylinders: Mechatronics.SelectPneumaticCylinderList
    ExhaustPressure: Expression
    NominalFlow: Expression
    NominalPressure: Expression
    SupplyPressure: Expression
    ValveType: Mechatronics.PneumaticValveBuilder.OutputValveType


    class OutputValveType(enum.Enum):
        FourWay = 0
        ThreeWay = 1
    

class PneumaticValve(DisplayableObject):
    def __init__(self) -> None: ...


class PneumaticCylinderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PneumaticCylinder]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePneumaticCylinderBuilder(self, pneumaticCylinder: Mechatronics.PneumaticCylinder) -> Mechatronics.PneumaticCylinderBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PneumaticCylinder:
        ...
    def Tag(self) -> Tag: ...



class PneumaticCylinderBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    AxisJoint: Mechatronics.SelectPhysicsJoint
    GasR: Expression
    Kappa: Expression
    PistonDiameter: Expression
    PistonRodDiameter: Expression
    PressureA: Expression
    PressureB: Expression
    RodType: Mechatronics.PneumaticCylinderBuilder.OutputRodType
    StrokeLength: Expression
    Temperature: Expression
    VolumeExtendA: Expression
    VolumeExtendB: Expression


    class OutputRodType(enum.Enum):
        Single = 0
        Double = 1
    

class PneumaticCylinder(DisplayableObject):
    def __init__(self) -> None: ...


class PMNavFolderObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PMNavFolderObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Mechatronics.PMNavFolderObject:
        ...
    def FindByObject(self, object: TaggedObject) -> Mechatronics.PMNavFolderObject:
        ...
    def Create(self, name: str) -> Mechatronics.PMNavFolderObject:
        ...
    def Delete(self, folder: Mechatronics.PMNavFolderObject, isDeleteMember: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class PMNavFolderObject(NXObject):
    def __init__(self) -> None: ...
    def IsDefault(self) -> bool:
        ...
    def GetObjects(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def AddObjects(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def MoveObjects(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def RestoreObjects(self, restoreAllMembers: bool, objects: typing.List[TaggedObject]) -> None:
        ...


class PMNavFolderLocatorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PMNavFolderLocator]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Mechatronics.PMNavFolderLocator:
        ...
    def Tag(self) -> Tag: ...



class PMNavFolderLocator(NXObject):
    def __init__(self) -> None: ...
    def AddFolderObjects(self, objects: typing.List[Mechatronics.PMNavFolderObject]) -> None:
        ...
    def MoveFolderObject(self, draggedObject: Mechatronics.PMNavFolderObject, targetObject: Mechatronics.PMNavFolderObject) -> None:
        ...


class PlcSimAdvClientBuilder(Builder):
    def __init__(self) -> None: ...
    def RefreshRegisteredInstances(self) -> None:
        ...
    def GetInstanceNames(self, ownerParts: typing.List[Part]) -> str:
        ...
    def SetInstanceNames(self, ownerParts: typing.List[Part], names: str) -> None:
        ...
    def GetInstanceInformation(self, instanceName: str, ownerPart: Part, tagInfos: typing.List[Mechatronics.PlcSimAdvClientBuilder.TagInfo]) -> None:
        ...
    def SetInstanceInformation(self, instanceName: str, ownerPart: Part, tagInfos: typing.List[Mechatronics.PlcSimAdvClientBuilder.TagInfo]) -> None:
        ...
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part


    class PlcSimAdvClientBuilderTagInfo():
        Name: str
        EAreaType: Mechatronics.PlcSimAdvClientBuilder.AreaType
        EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType
        EDataType: Mechatronics.SignalBuilder.DataType
        BChecked: bool
        def ToString(self) -> str:
            ...
    

    class AreaType(enum.Enum):
        Unknow = -1
        Input = 1
        Output = 2
        Marker = 4
        Datablock = 8
    

class PlanarJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PlanarJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePlanarJointBuilder(self, cylinJoint: Mechatronics.PlanarJoint) -> Mechatronics.PlanarJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PlanarJoint:
        ...
    def Tag(self) -> Tag: ...



class PlanarJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AxisVector: Direction
    PointOrigin: Point


class PlanarJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class PhysicsPreferenceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PhysicsPreference]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePreferenceBuilder(self, physicsPreference: Mechatronics.PhysicsPreference) -> Mechatronics.PreferencesBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PhysicsPreference:
        ...
    def Tag(self) -> Tag: ...



class PhysicsPreference(NXObject):
    def __init__(self) -> None: ...


class PhysicsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreatePreferenceBuilder(self) -> Mechatronics.PreferencesBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Mechatronics.PhysicsPreferenceCollection.CreatePreferenceBuilder instead")"""
        ...
    def CreateReplacePhysicsBuilder(self) -> Mechatronics.ReplacePhysicsBuilder:
        ...
    def CreateOpcclientBuilder(self) -> Mechatronics.OPCClientBuilder:
        ...
    def CreateMatlabclientBuilder(self) -> Mechatronics.MATLABClientBuilder:
        ...
    def RemapPhysicsReferences(self, replacedPartOcc: Assemblies.Component) -> None:
        ...
    def LogPhysicsToDelete(self, physicsObject: NXObject) -> None:
        ...
    def SetName(self, physicsObject: NXObject, name: str) -> None:
        ...
    def ExportToCsv(self, path: str, signal: bool, connection: bool) -> None:
        ...
    def ExportSignalsToCsv(self, path: str, names: str, owners: str, ioTypes: typing.List[Mechatronics.SignalBuilder.IOType], dataTypes: typing.List[Mechatronics.SignalBuilder.DataType], bValues: bool, nValues: int, dValues: float, connectionNames: str, signal: bool, connection: bool) -> None:
        ...
    def ExportToTxt(self, path: str) -> None:
        ...
    def ExportSignalsToTxt(self, path: str, names: str, ioTypes: typing.List[Mechatronics.SignalBuilder.IOType], dataTypes: typing.List[Mechatronics.SignalBuilder.DataType], bValues: bool, nValues: int, dValues: float, addresses: str, comments: str) -> None:
        ...
    def ExportSignalsToExcel(self, path: str, names: str, ioTypes: typing.List[Mechatronics.SignalBuilder.IOType], dataTypes: typing.List[Mechatronics.SignalBuilder.DataType], bValues: bool, nValues: int, dValues: float, addresses: str, comments: str) -> None:
        ...
    def CreateECADExportBuilder(self) -> Mechatronics.ECADExportBuilder:
        ...
    def CreateECADImportBuilder(self) -> Mechatronics.ECADImportBuilder:
        ...
    def CreateSignalMappingBuilder(self) -> Mechatronics.SignalMappingBuilder:
        ...
    def CreateSHMConfigurationBuilder(self) -> Mechatronics.SHMConfigurationBuilder:
        ...
    def CreateConvertFromMtbbuilder(self) -> Mechatronics.ConvertFromMTBBuilder:
        ...
    def CreateSCOUTExportBuilder(self) -> Mechatronics.SCOUTExportBuilder:
        ...
    def CreateSCOUTImportBuilder(self) -> Mechatronics.SCOUTImportBuilder:
        ...
    def CreateChangeOwnerBuilder(self) -> Mechatronics.ChangeOwnerBuilder:
        ...
    def CreateExportSensorsActuatorsBuilder(self) -> Mechatronics.ExportSensorsActuatorsBuilder:
        ...
    def CreateSensorsActuatorsListBuilder(self) -> Mechatronics.SensorsActuatorsListBuilder:
        ...
    def AdoptAssemblyJoint(self) -> None:
        ...
    def AdoptAssemblyJoint(self, joint: Positioning.Constraint) -> None:
        ...
    def QueryAdoption(self, joint: Positioning.Constraint) -> DisplayableObject:
        ...
    def CreateChainJointBuilder(self) -> Mechatronics.ChainJointBuilder:
        ...
    def CreateAnimationConversionBuilder(self) -> Mechatronics.AnimationConversionBuilder:
        ...
    def Tag(self) -> Tag: ...

    RigidBodies: Mechatronics.RigidBodyCollection
    CollisionBodies: Mechatronics.CollisionBodyCollection
    MotionProfiles: Mechatronics.MotionProfileCollection
    RuntimeBehaviors: Mechatronics.RuntimeBehaviorCollection
    RuntimeNCs: Mechatronics.RuntimeNCCollection
    CollisionMaterials: Mechatronics.CollisionMaterialCollection
    TransportSurfaces: Mechatronics.TransportSurfaceCollection
    HingeJoints: Mechatronics.HingeJointCollection
    SpeedControls: Mechatronics.SpeedControlCollection
    PositionControls: Mechatronics.PositionControlCollection
    ForceTorqueControls: Mechatronics.ForceTorqueControlCollection
    SlidingJoints: Mechatronics.SlidingJointCollection
    CollisionSensors: Mechatronics.CollisionSensorCollection
    CylindricalJoints: Mechatronics.CylindricalJointCollection
    ScrewJoints: Mechatronics.ScrewJointCollection
    PlanarJoints: Mechatronics.PlanarJointCollection
    RackPinions: Mechatronics.RackPinionCollection
    FixedJoints: Mechatronics.FixedJointCollection
    BallJoints: Mechatronics.BallJointCollection
    AngularSpringJoints: Mechatronics.AngularSpringJointCollection
    LinearSpringJoints: Mechatronics.LinearSpringJointCollection
    Gears: Mechatronics.GearCollection
    ThreeJointCouplers: Mechatronics.ThreeJointCouplerCollection
    Cams: Mechatronics.CamCollection
    AngularLimitJoints: Mechatronics.AngularLimitJointCollection
    LinearLimitJoints: Mechatronics.LinearLimitJointCollection
    BreakingConstraints: Mechatronics.BreakingConstraintCollection
    PreventCollisions: Mechatronics.PreventCollisionCollection
    ChangeMaterials: Mechatronics.ChangeMaterialCollection
    VirtualAxis: Mechatronics.VirtualAxisCollection
    ObjectSources: Mechatronics.ObjectSourceCollection
    ObjectSinks: Mechatronics.ObjectSinkCollection
    GraphControls: Mechatronics.GraphControlCollection
    ExternalConnections: Mechatronics.ExternalConnectionCollection
    RuntimeFormulas: Mechatronics.RuntimeFormulaCollection
    SignalAdapters: Mechatronics.SignalAdapterCollection
    AdapterSignals: Mechatronics.AdapterSignalCollection
    AdapterFormulas: Mechatronics.AdapterFormulaCollection
    Signals: Mechatronics.SignalCollection
    ExpressionBlocks: Mechatronics.ExpressionBlockCollection
    ExpressionBlockFormulas: Mechatronics.ExpressionBlockFormulaCollection
    SignalConnections: Mechatronics.SignalConnectionCollection
    SHMSignalConnections: Mechatronics.SHMSignalConnectionCollection
    MATLABSignalConnections: Mechatronics.MATLABSignalConnectionCollection
    SignalMappingConnections: Mechatronics.SignalMappingConnectionCollection
    PointOnCurveJoints: Mechatronics.PointOnCurveJointCollection
    CurveOnCurveJoints: Mechatronics.CurveOnCurveJointCollection
    PhysicsPreference: Mechatronics.PhysicsPreferenceCollection
    PMNavFolderObject: Mechatronics.PMNavFolderObjectCollection
    PMNavFolderLocator: Mechatronics.PMNavFolderLocatorCollection
    CamProfiles: Mechatronics.CamProfileCollection
    ObjectTransformer: Mechatronics.ObjectTransformerCollection
    SpringDampers: Mechatronics.SpringDamperCollection
    TagForms: Mechatronics.TagFormCollection
    TagTables: Mechatronics.TagTableCollection
    ReadWriteDevices: Mechatronics.ReadWriteDeviceCollection
    DisplayChanger: Mechatronics.DisplayChangerCollection
    PathConstraintJoints: Mechatronics.PathConstraintJointCollection
    SymbolTables: Mechatronics.SymbolTableCollection
    DistanceSensors: Mechatronics.DistanceSensorCollection
    PositionSensors: Mechatronics.PositionSensorCollection
    VelocitySensors: Mechatronics.VelocitySensorCollection
    GenericSensors: Mechatronics.GenericSensorCollection
    LimitSwitchs: Mechatronics.LimitSwitchCollection
    Relays: Mechatronics.RelayCollection
    Inclinometers: Mechatronics.InclinometerCollection
    Accelerometers: Mechatronics.AccelerometerCollection
    PneumaticCylinders: Mechatronics.PneumaticCylinderCollection
    PneumaticValves: Mechatronics.PneumaticValveCollection
    HydraulicCylinders: Mechatronics.HydraulicCylinderCollection
    HydraulicValves: Mechatronics.HydraulicValveCollection
    TransmitterEntry: Mechatronics.TransmitterEntryCollection
    TransmitterExit: Mechatronics.TransmitterExitCollection
    AlignBodies: Mechatronics.AlignBodyCollection
    DynamicObjectTables: Mechatronics.DynamicObjectTableCollection
    Tracers: Mechatronics.TracerCollection
    ExternalSignalConfigurations: Mechatronics.ExternalSignalConfigurationCollection
    MCDSignalServerConfigurations: Mechatronics.MCDSignalServerConfigurationCollection


class PhysicsJointBuilder(Builder):
    def __init__(self) -> None: ...
    def SetAttachment(self, attachment: NXObject) -> None:
        ...
    def SetBase(self, base: NXObject) -> None:
        ...
    Attachment: SelectNXObject
    Base: SelectNXObject
    BaseAnchorPoint: Point
    BaseAxisVector: Direction
    Name: str
    Positioning: bool


class PhysicsJoint(DisplayableObject):
    def __init__(self) -> None: ...


class PhysicsConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str


class PhysicsConstraint(DisplayableObject):
    def __init__(self) -> None: ...


class PathConstraintJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.PathConstraintJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePathConstraintJointBuilder(self, slide: Mechatronics.PathConstraintJoint) -> Mechatronics.PathConstraintJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.PathConstraintJoint:
        ...
    def Tag(self) -> Tag: ...



class PathConstraintJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    def GetPathCurves(self) -> typing.List[NXObject]:
        ...
    def SetPathCurvesFromCurves(self, pathCurves: typing.List[NXObject]) -> None:
        ...
    def EvaluatePath(self, curves: typing.List[NXObject]) -> None:
        ...
    def NewPathFrame(self) -> Mechatronics.PathConstraintFrameBuilder:
        ...
    def GeneratePathCurves(self) -> None:
        ...
    AxisVector: Direction
    FrameList: Mechatronics.PathConstraintFrameBuilderList
    PathPreview: bool
    PathType: Mechatronics.PathConstraintJointBuilder.PathTypes
    PointOnCurve: Point


    class PathTypes(enum.Enum):
        FromCoordinateSystems = 0
        FromCurves = 1
    

class PathConstraintJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class PathConstraintFrameBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.PathConstraintFrameBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.PathConstraintFrameBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.PathConstraintFrameBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.PathConstraintFrameBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.PathConstraintFrameBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.PathConstraintFrameBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.PathConstraintFrameBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.PathConstraintFrameBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.PathConstraintFrameBuilder, object2: Mechatronics.PathConstraintFrameBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.PathConstraintFrameBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PathConstraintFrameBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AssociatedCurve: NXObject
    CurveType: Mechatronics.PathConstraintFrameBuilder.CurveTypes
    PathFrame: CoordinateSystem
    PathParameter: float


    class CurveTypes(enum.Enum):
        Line = 0
        Spline = 1
    

class ParameterStockBuilder(Builder):
    def __init__(self) -> None: ...
    def AddBoolParameter(self, name: str, value: bool, predefined: bool, readOnly: bool) -> None:
        ...
    def AddIntParameter(self, name: str, value: int, predefined: bool, readOnly: bool) -> None:
        ...
    def AddRealParameter(self, name: str, value: float, unit: Unit, predefined: bool, readOnly: bool) -> None:
        ...
    def AddStringParameter(self, name: str, value: str, predefined: bool, readOnly: bool) -> None:
        ...
    def AddListParameter(self, name: str, values: str, eAssignment: Mechatronics.ParameterStockBuilder.Assignment, predefined: bool, readOnly: bool) -> None:
        ...
    def GetParameterNamesAndTypes(self, types: typing.List[Mechatronics.ParameterStockBuilder.DataType]) -> str:
        ...
    def GetBoolParameter(self, name: str, predefined: bool, readOnly: bool) -> bool:
        ...
    def GetIntParameter(self, name: str, predefined: bool, readOnly: bool) -> int:
        ...
    def GetRealParameter(self, name: str, unit: Unit, predefined: bool, readOnly: bool) -> float:
        ...
    def GetStringParameter(self, name: str, predefined: bool, readOnly: bool) -> str:
        ...
    def GetListParameter(self, name: str, eAssignment: Mechatronics.ParameterStockBuilder.Assignment, predefined: bool, readOnly: bool) -> str:
        ...
    def EditBoolParameter(self, name: str, value: bool) -> None:
        ...
    def EditIntParameter(self, name: str, value: int) -> None:
        ...
    def EditRealParameter(self, name: str, value: float, unit: Unit) -> None:
        ...
    def EditStringParameter(self, name: str, value: str) -> None:
        ...
    def EditListParameter(self, name: str, values: str, eAssignment: Mechatronics.ParameterStockBuilder.Assignment) -> None:
        ...
    def DeleteParameter(self, name: str) -> None:
        ...
    ApplicationName: str


    class DataType(enum.Enum):
        Bool = 0
        Int = 1
        Real = 2
        String = 3
        List = 4
    

    class Assignment(enum.Enum):
        None = 0
        ByOrder = 1
        Random = 2
    

class OPCUAClientBuilder(Builder):
    def __init__(self) -> None: ...
    def GetServerNames(self) -> str:
        ...
    def GetServerTags(self, serverName: str) -> typing.List[Mechatronics.OPCUAClientBuilder.TagInfo]:
        ...
    def SetServerTags(self, serverName: str, tagInfos: typing.List[Mechatronics.OPCUAClientBuilder.TagInfo]) -> None:
        ...
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part


    class OPCUAClientBuilderTagInfo():
        Name: str
        EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType
        EDataType: Mechatronics.SignalBuilder.DataType
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType, EDataType: Mechatronics.SignalBuilder.DataType) -> None: ...
    

class OPCClientBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteTags(self) -> None:
        ...
    def AddTags(self) -> None:
        ...
    def GetAvailableItems(self, tagName: str, tagType: typing.List[Mechatronics.OPCClientBuilder.TagDataType]) -> None:
        ...
    def SetAvailableItems(self, tagName: str, tagType: typing.List[Mechatronics.OPCClientBuilder.TagDataType]) -> None:
        ...
    def GetItemAttributes(self, attr: typing.List[Mechatronics.OPCClientBuilder.TagAttribute]) -> None:
        ...
    def SetItemAttributes(self, attr: typing.List[Mechatronics.OPCClientBuilder.TagAttribute]) -> None:
        ...
    def GetServerNames(self) -> str:
        ...
    def GetServerTags(self, serverName: str) -> typing.List[Mechatronics.OPCClientBuilder.TagInfo]:
        ...
    HostName: str
    OpcFileBrowser: str
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part
    ServerProgID: str
    ServerType: Mechatronics.OPCClientBuilder.ServerOption
    UpdateTime: Expression


    class OPCClientBuilderTagInfo():
        Name: str
        EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType
        EDataType: Mechatronics.SignalBuilder.DataType
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType, EDataType: Mechatronics.SignalBuilder.DataType) -> None: ...
    

    class TagDataType(enum.Enum):
        Unknown = 0
        Integer = 1
        Float = 2
        Boolean = 3
    

    class OPCClientBuilderTagAttribute():
        TagName: str
        TagType: Mechatronics.OPCClientBuilder.TagDataType
        TagAccess: Mechatronics.OPCClientBuilder.TagAccess
        def ToString(self) -> str:
            ...
        def __init__(self, TagName: str, TagType: Mechatronics.OPCClientBuilder.TagDataType, TagAccess: Mechatronics.OPCClientBuilder.TagAccess) -> None: ...
    

    class TagAccess(enum.Enum):
        ReadOnly = 1
        WriteOnly = 2
        ReadWrite = 3
    

    class ServerOption(enum.Enum):
        Local = 0
        Remote = 1
        InProc = 2
    

class ObjectTransformerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ObjectTransformer]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateObjectTransformerBuilder(self, objectSrc: Mechatronics.ObjectTransformer) -> Mechatronics.ObjectTransformerBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ObjectTransformer:
        ...
    def Tag(self) -> Tag: ...



class ObjectTransformerBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    CollisionSensor: Mechatronics.SelectCollisionSensorList
    ExecuteOnce: bool
    RigidBody: Mechatronics.SelectRigidBody
    Source: SelectNXObjectList
    SourceType: Mechatronics.ObjectTransformerBuilder.TransformSourceType


    class TransformSourceType(enum.Enum):
        AnyObject = 0
        OnlySelected = 1
    

class ObjectTransformer(DisplayableObject):
    def __init__(self) -> None: ...


class ObjectSourceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ObjectSource]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateObjectSourceBuilder(self, objectSrc: Mechatronics.ObjectSource) -> Mechatronics.ObjectSourceBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ObjectSource:
        ...
    def Tag(self) -> Tag: ...



class ObjectSourceBuilder(Builder):
    def __init__(self) -> None: ...
    def SetObjectsToCopy(self, objects: typing.List[NXObject]) -> None:
        ...
    CopyEventTrigger: Mechatronics.ObjectSourceBuilder.CopyEventTriggerOption
    Name: str
    ObjectToCopy: SelectNXObjectList
    StartOffset: Expression
    TimeInterval: Expression


    class CopyEventTriggerOption(enum.Enum):
        TimeBased = 0
        OncePerActivation = 1
    

class ObjectSource(DisplayableObject):
    def __init__(self) -> None: ...


class ObjectSinkCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ObjectSink]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateObjectSinkBuilder(self, objectSrc: Mechatronics.ObjectSink) -> Mechatronics.ObjectSinkBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ObjectSink:
        ...
    def Tag(self) -> Tag: ...



class ObjectSinkBuilder(Builder):
    def __init__(self) -> None: ...
    def SetCollisionSensor(self, objects: typing.List[Mechatronics.CollisionSensor]) -> None:
        ...
    def SetSource(self, objects: typing.List[NXObject]) -> None:
        ...
    CollisionSensor: Mechatronics.SelectCollisionSensorList
    DeleteSource: Mechatronics.ObjectSinkBuilder.DeleteSourceType
    Name: str
    Source: SelectNXObjectList


    class DeleteSourceType(enum.Enum):
        Anycopiedobjects = 0
        Selectedsources = 1
    

class ObjectSink(DisplayableObject):
    def __init__(self) -> None: ...


class ObjectInformationBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    ItemID: str
    ItemName: str
    ItemTypes: str
    RevisionID: str


class MotionProfileCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.MotionProfile]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMotionProfileBuilder(self, functionTable: Mechatronics.MotionProfile) -> Mechatronics.MotionProfileBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.MotionProfile:
        ...
    def Tag(self) -> Tag: ...



class MotionProfileBuilder(Builder):
    def __init__(self) -> None: ...
    def AddElement(self, part: NXObject, name: str, masterPos: float, slavePos: float, vin: float, vout: float, ain: float, aout: float, vinEqVout: bool, ainEqAout: bool, constantSpeed: bool) -> None:
        ...
    CyclicType: Mechatronics.MotionProfileBuilder.ProfileCyclicType
    IsForElecCam: bool
    MasterMaximum: Expression
    MasterMinimum: Expression
    MasterUnit: Mechatronics.MotionProfileBuilder.MasterValueUnit
    Name: str
    SlaveMaximum: Expression
    SlaveMinimum: Expression
    SlaveUnit: Mechatronics.MotionProfileBuilder.SlaveValueUnit


    class SlaveValueUnit(enum.Enum):
        LinearPosition = 0
        RotaryPosition = 1
        LinearSpeed = 2
        RotarySpeed = 3
    

    class ProfileCyclicType(enum.Enum):
        RelativeCyclic = 0
        Cyclic = 1
        NonCyclic = 2
    

    class MasterValueUnit(enum.Enum):
        Linear = 0
        Rotary = 1
        Time = 2
    

class MotionProfile(NXObject):
    def __init__(self) -> None: ...


class MechatronicsSession(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def PerformSimulation(self, action: Mechatronics.MechatronicsSession.SimulationAction) -> None:
        ...
    def GetLogicalTypes(self, logicalTypeNames: str, logicalTypeBitmaps: str) -> None:
        ...
    def GetLogicalAttributeNames(self, attributeNames: str) -> None:
        ...
    def GetLogicalAttributeValues(self, logicalObject: Mechatronics.LogicObject, attributeNames: str) -> str:
        ...
    def GetExportableLogicalObjects(self, logicalObject: Mechatronics.LogicObject) -> typing.List[Mechatronics.LogicObject]:
        ...
    def Tag(self) -> Tag: ...



    class SimulationAction(enum.Enum):
        Start = 0
        Restart = 1
        Pause = 2
        Resume = 3
        Stop = 4
    

class MechatronicsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def LogEntityToDelete(self, object: NXObject) -> None:
        ...
    def ExportModel(self, path: str, bFunction: bool, bLogical: bool) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Please use another method with the same name instead.")"""
        ...
    def ImportModel(self, path: str, bFunction: bool, bLogical: bool) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Please use another method with the same name instead.")"""
        ...
    def SaveToTeamcenter(self) -> None:
        ...
    def RefreshFromTeamcenter(self, bFunction: bool, bLogical: bool) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Please use another method with the same name instead.")"""
        ...
    def SaveToTeamcenter(self, requirement: bool, function: bool, logic: bool) -> None:
        ...
    def ExportModel(self, path: str, requirement: bool, function: bool, logic: bool) -> None:
        ...
    def ImportModel(self, path: str, overrideModel: bool, requirement: bool, function: bool, logic: bool) -> None:
        ...
    def RefreshFromTeamcenter(self, requirement: bool, function: bool, logic: bool) -> None:
        ...
    def OpenFunctionModel(self, itemMFKID: str, variantRule: str) -> None:
        ...
    def OpenLogicalModel(self, itemMFKID: str, variantRule: str) -> None:
        ...
    def OpenRequirementModel(self, itemMFKID: str, variantRule: str) -> None:
        ...
    def AddExistingFunction(self, object: Mechatronics.SystemObject, itemMFKID: str, instanceName: str) -> None:
        ...
    def AddExistingLogical(self, object: Mechatronics.SystemObject, itemMFKID: str, instanceName: str) -> None:
        ...
    def AddExistingRequirement(self, object: Mechatronics.SystemObject, itemMFKID: str, instanceName: str) -> None:
        ...
    def PasteTraceLink(self, object: Mechatronics.SystemObject) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Please use SystemObject.CreateTraceLink instead.")"""
        ...
    def CreateSystemRoot(self, rootType: Mechatronics.SystemRoot.Type) -> Mechatronics.SystemRoot:
        ...
    def CreateDependencyCreatorBuilder(self) -> Mechatronics.DependencyCreatorBuilder:
        ...
    def LoadAsSaved(self) -> str:
        ...
    def GetSystemRoot(self, rootType: Mechatronics.SystemRoot.Type) -> Mechatronics.SystemRoot:
        ...
    def CopySystemObject(self, objects: typing.List[Mechatronics.SystemObject]) -> None:
        ...
    def CutSystemObject(self, objects: typing.List[Mechatronics.SystemObject]) -> None:
        ...
    def PasteSystemObject(self, parent: Mechatronics.SystemObject) -> None:
        ...
    def Tag(self) -> Tag: ...

    FunctionObjectCollection: Mechatronics.FunctionObjectCollection
    LogicObjectCollection: Mechatronics.LogicObjectCollection
    RequirementCollection: Mechatronics.RequirementCollection
    ElectricalPartCollection: Mechatronics.ElectricalPartCollection


class McdSignalServerConfigurationtype(enum.Enum):
    Shm = 0
    Tcp = 1
    Udp = 2


class MCDSignalServerConfigurationObject(NXObject):
    def __init__(self) -> None: ...


class MCDSignalServerConfigurationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.MCDSignalServerConfigurationObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMCDSignalServerConfigurationBuilder(self, pMCDSignalServerConfigurationObject: Mechatronics.MCDSignalServerConfigurationObject) -> Mechatronics.MCDSignalServerConfigurationBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.MCDSignalServerConfigurationObject:
        ...
    def Tag(self) -> Tag: ...



class MCDSignalServerConfigurationBuilder(Builder):
    def __init__(self) -> None: ...
    SHMSignalProvider: Mechatronics.SHMSignalProviderBuilder
    TCPSignalServer: Mechatronics.TCPSignalServerBuilder
    UDPSignalServer: Mechatronics.UDPSignalServerBuilder


class MATLABSignalConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.MATLABSignalConnection]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Mechatronics.MATLABSignalConnection:
        ...
    def CreateSignalConnectionBuilder(self, connection: Mechatronics.MATLABSignalConnection) -> Mechatronics.MATLABSignalConnectionBuilder:
        ...
    def Tag(self) -> Tag: ...



class MATLABSignalConnectionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.MATLABSignalConnectionBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.MATLABSignalConnectionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.MATLABSignalConnectionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.MATLABSignalConnectionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.MATLABSignalConnectionBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.MATLABSignalConnectionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.MATLABSignalConnectionBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.MATLABSignalConnectionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.MATLABSignalConnectionBuilder, object2: Mechatronics.MATLABSignalConnectionBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.MATLABSignalConnectionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class MATLABSignalConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    AdapterIdentify: Mechatronics.SignalAdapter
    MATLABSignalName: str
    MATLABSignalPort: Mechatronics.MATLABClientBuilder.DataPortType
    MATLABSignalType: Mechatronics.MATLABSignalConnectionBuilder.DataType
    ModelName: str
    ResultName: str
    SignalIdentify: NXObject
    StreamIO: int


    class DataType(enum.Enum):
        Unknown = 0
        Int = 1
        Double = 2
        Bool = 3
        String = 4
    

class MATLABSignalConnection(DisplayableObject):
    def __init__(self) -> None: ...


class MATLABClientBuilder(Builder):
    def __init__(self) -> None: ...
    def GetServerTags(self, serverName: str) -> typing.List[Mechatronics.MATLABClientBuilder.TagInfo]:
        ...
    def GetAvailableItems(self, signalName: str, signalType: typing.List[Mechatronics.MATLABClientBuilder.DataType]) -> None:
        ...
    def SetAvailableItems(self, signalName: str, signalType: typing.List[Mechatronics.MATLABClientBuilder.DataType]) -> None:
        ...
    def GetItemAttributes(self, attr: typing.List[Mechatronics.MATLABClientBuilder.TagAttribute]) -> None:
        ...
    def SetItemAttributes(self, attr: typing.List[Mechatronics.MATLABClientBuilder.TagAttribute]) -> None:
        ...
    def GetMATLABInformation(self, instanceName: str, tagInfos: typing.List[Mechatronics.MATLABClientBuilder.TagInfo]) -> None:
        ...
    def SetMATLABInformation(self, instanceName: str, tagInfos: typing.List[Mechatronics.MATLABClientBuilder.TagInfo]) -> None:
        ...
    MATLABServerProgID: str
    MatlabFileBrowser: str
    SelectedConfigurationName: str
    SelectedConfigurationPart: Part
    UpdateTime: Expression


    class MATLABClientBuilderTagInfo():
        Name: str
        EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType
        EDataType: Mechatronics.SignalBuilder.DataType
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, EIOType: Mechatronics.SignalBuilder.ExternalSignalIOType, EDataType: Mechatronics.SignalBuilder.DataType) -> None: ...
    

    class MATLABClientBuilderTagAttribute():
        SignalName: str
        SignalType: Mechatronics.MATLABClientBuilder.DataType
        SignalportType: Mechatronics.MATLABClientBuilder.DataPortType
        def ToString(self) -> str:
            ...
        def __init__(self, SignalName: str, SignalType: Mechatronics.MATLABClientBuilder.DataType, SignalportType: Mechatronics.MATLABClientBuilder.DataPortType) -> None: ...
    

    class MATLABClientBuilderSignalData():
        Name: str
        DataType: str
        PortType: str
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, DataType: str, PortType: str) -> None: ...
    

    class DataType(enum.Enum):
        Bool = 0
        Int = 1
        Double = 2
    

    class DataPortType(enum.Enum):
        Input = 0
        Output = 1
    

class LogicObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.LogicObject]:
        ...
    def __init__(self, owner: Mechatronics.MechatronicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLogicObjectBuilder(self, object: Mechatronics.LogicObject) -> Mechatronics.LogicObjectBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.LogicObject:
        ...
    def Tag(self) -> Tag: ...



class LogicObjectBuilder(Mechatronics.SystemObjectBuilder):
    def __init__(self) -> None: ...
    def GetParameterData(self) -> typing.List[Mechatronics.LogicObjectBuilder.ParameterData]:
        ...
    def SetParameterData(self, parameterData: typing.List[Mechatronics.LogicObjectBuilder.ParameterData]) -> None:
        ...
    Aspect: str
    ClassificationItem: Mechatronics.SelectClassificationBuilder
    LetterDescription: str
    LetterName: str
    Modified: bool
    NavigatorObject: NXObject
    ObjectInformation: Mechatronics.ObjectInformationBuilder
    Parent: NXObject
    TypeName: str


    class LogicObjectBuilderParameterData():
        ParameterName: str
        ParameterValue: str
        def ToString(self) -> str:
            ...
        def __init__(self, ParameterName: str, ParameterValue: str) -> None: ...
    

class LogicObject(Mechatronics.SystemObject):
    def __init__(self) -> None: ...


class LinearSpringJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.LinearSpringJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLinearSpringJointBuilder(self, linearSpringJoint: Mechatronics.LinearSpringJoint) -> Mechatronics.LinearSpringJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.LinearSpringJoint:
        ...
    def Tag(self) -> Tag: ...



class LinearSpringJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AttachmentPoint: Point
    BasePoint: Point
    Damping: Expression
    RelaxedPosition: Expression
    SpringConstant: Expression


class LinearSpringJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class LinearLimitJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.LinearLimitJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLinearLimitJointBuilder(self, linearLimit: Mechatronics.LinearLimitJoint) -> Mechatronics.LinearLimitJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.LinearLimitJoint:
        ...
    def Tag(self) -> Tag: ...



class LinearLimitJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AttachmentPoint: Point
    BasePoint: Point
    MaximumPosition: Expression
    MinimumPosition: Expression


class LinearLimitJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class LimitSwitchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.LimitSwitch]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLimitSwitchBuilder(self, limitSwitch: Mechatronics.LimitSwitch) -> Mechatronics.LimitSwitchBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.LimitSwitch:
        ...
    def Tag(self) -> Tag: ...



class LimitSwitchBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    EnableLowerLimit: bool
    EnableUpperLimit: bool
    LowerLimit: Expression
    PersistentTag: int
    SelectedPhysicsObject: SelectNXObject
    UpperLimit: Expression


class LimitSwitch(DisplayableObject):
    def __init__(self) -> None: ...


class InclinometerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Inclinometer]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateInclinometerBuilder(self, inclinometer: Mechatronics.Inclinometer) -> Mechatronics.InclinometerBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Inclinometer:
        ...
    def Tag(self) -> Tag: ...



class InclinometerBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    AngleType: Mechatronics.InclinometerBuilder.OutputAngleType
    LowerOutputRange: Expression
    LowerTrimRange: Expression
    MeasureType: Mechatronics.InclinometerBuilder.OutputMeasureType
    Orientation: CoordinateSystem
    RigidBody: Mechatronics.SelectRigidBody
    UpperOutputRange: Expression
    UpperTrimRange: Expression
    UseScale: bool
    UseTrim: bool


    class OutputMeasureType(enum.Enum):
        Constant = 0
        Voltage = 1
        Current = 2
    

    class OutputAngleType(enum.Enum):
        YawPitchRoll = 0
        Euler = 1
    

class Inclinometer(DisplayableObject):
    def __init__(self) -> None: ...


class HydraulicValveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.HydraulicValve]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHydraulicValveBuilder(self, hydraulicValve: Mechatronics.HydraulicValve) -> Mechatronics.HydraulicValveBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.HydraulicValve:
        ...
    def Tag(self) -> Tag: ...



class HydraulicValveBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetCylinders(self, cylinders: typing.List[Mechatronics.HydraulicCylinder]) -> None:
        ...
    ControlInput: Expression
    Cylinders: Mechatronics.SelectHydraulicCylinderList
    ExhaustPressure: Expression
    NominalFlow: Expression
    NominalPressure: Expression
    SupplyPressure: Expression
    ValveType: Mechatronics.HydraulicValveBuilder.OutputValveType


    class OutputValveType(enum.Enum):
        FourWay = 0
        ThreeWay = 1
    

class HydraulicValve(DisplayableObject):
    def __init__(self) -> None: ...


class HydraulicCylinderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.HydraulicCylinder]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHydraulicCylinderBuilder(self, hydraulicCylinder: Mechatronics.HydraulicCylinder) -> Mechatronics.HydraulicCylinderBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.HydraulicCylinder:
        ...
    def Tag(self) -> Tag: ...



class HydraulicCylinderBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    AxisJoint: Mechatronics.SelectPhysicsJoint
    PistonDiameter: Expression
    PistonRodDiameter: Expression
    PressureA: Expression
    PressureB: Expression
    RodType: Mechatronics.HydraulicCylinderBuilder.OutputRodType
    StrokeLength: Expression


    class OutputRodType(enum.Enum):
        Single = 0
        Double = 1
    

class HydraulicCylinder(DisplayableObject):
    def __init__(self) -> None: ...


class HingeJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.HingeJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHingeJointBuilder(self, hinge: Mechatronics.HingeJoint) -> Mechatronics.HingeJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.HingeJoint:
        ...
    def Tag(self) -> Tag: ...



class HingeJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AxisVector: Direction
    EnableLowerLimit: bool
    EnableUpperLimit: bool
    LowerLimit: Expression
    Point: Point
    StartAngle: Expression
    UpperLimit: Expression


class HingeJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class GraphControlCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.GraphControl]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateGraphControlBuilder(self, graphControl: Mechatronics.GraphControl) -> Mechatronics.GraphControlBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.GraphControl:
        ...
    def Tag(self) -> Tag: ...



class GraphControlBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    CamProfile: Mechatronics.CamProfile
    GraphEndAction: Mechatronics.GraphControlBuilder.EndAction
    InitialTime: Expression
    MasterAxisType: Mechatronics.GraphControlBuilder.MasterJointType
    MasterBaseType: Mechatronics.GraphControlBuilder.MasterType
    MasterOffset: Expression
    MasterScaleFactor: Expression
    MasterUnit: Mechatronics.GraphControlBuilder.MasterValueUnit
    MotionProfile: Mechatronics.MotionProfile
    SelectAxisControl: Mechatronics.SelectPhysicsConstraint
    SelectMasterJoint: Mechatronics.SelectPhysicsJoint
    SelectMasterSignal: Mechatronics.SelectAdapterSignal
    SlaveOffset: Expression
    SlaveScaleFactor: Expression
    SlaveUnit: Mechatronics.GraphControlBuilder.SlaveValueUnit
    ValueOffset: Expression


    class SlaveValueUnit(enum.Enum):
        LinearPosition = 0
        RotaryPosition = 1
        LinearSpeed = 2
        RotarySpeed = 3
    

    class MasterValueUnit(enum.Enum):
        Linear = 0
        Rotary = 1
        Time = 2
    

    class MasterType(enum.Enum):
        Time = 0
        Axis = 1
        Signal = 2
    

    class MasterJointType(enum.Enum):
        Linear = 0
        Rotary = 1
    

    class EndAction(enum.Enum):
        RestartfromBeginning = 0
        DeactivateGraphControl = 1
    

class GraphControl(DisplayableObject):
    def __init__(self) -> None: ...


class GenericSensorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.GenericSensor]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateGenericSensorBuilder(self, genericSensor: Mechatronics.GenericSensor) -> Mechatronics.GenericSensorBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.GenericSensor:
        ...
    def Tag(self) -> Tag: ...



class GenericSensorBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    LowerOutputRange: Expression
    LowerTrimRange: Expression
    MeasureType: Mechatronics.GenericSensorBuilder.OutputMeasureType
    PersistentTag: int
    SelectedPhysicsObject: SelectNXObject
    UpperOutputRange: Expression
    UpperTrimRange: Expression
    UseScale: bool
    UseTrim: bool


    class OutputMeasureType(enum.Enum):
        Constant = 0
        Voltage = 1
        Current = 2
    

class GenericSensor(DisplayableObject):
    def __init__(self) -> None: ...


class GearCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Gear]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateGearBuilder(self, gearConstraint: Mechatronics.Gear) -> Mechatronics.GearBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Gear:
        ...
    def Tag(self) -> Tag: ...



class GearBuilder(Mechatronics.CouplingBuilder):
    def __init__(self) -> None: ...
    AxisType: Mechatronics.GearBuilder.AxisJointType
    ExpressionMasterMultiple: Expression
    ExpressionSlaveMultiple: Expression
    MasterMultiple: float
    SlaveMultiple: float


    class AxisJointType(enum.Enum):
        Linear = 0
        Angular = 1
    

class Gear(Mechatronics.Coupling):
    def __init__(self) -> None: ...


class GanttOperationParameterBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.GanttOperationParameterBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.GanttOperationParameterBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.GanttOperationParameterBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.GanttOperationParameterBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.GanttOperationParameterBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.GanttOperationParameterBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.GanttOperationParameterBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.GanttOperationParameterBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.GanttOperationParameterBuilder, object2: Mechatronics.GanttOperationParameterBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.GanttOperationParameterBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class GanttOperationParameterBuilder(Builder):
    def __init__(self) -> None: ...
    def PutExpressionValue(self, exp: Expression) -> None:
        ...
    ExpressionValue: Expression
    IOStatus: bool
    ObjectValue: NXObject
    Operator: Mechatronics.GanttOperationParameterBuilder.OperatorOption
    ParameterName: str
    ParameterValue: str
    PropertyId: int


    class OperatorOption(enum.Enum):
        None = 0
        Increment = 1
        Decrement = 2
        Multiply = 3
        Not = 4
    

class GanttOperationObject(NXObject):
    def __init__(self) -> None: ...


class GanttOperationConditionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.GanttOperationConditionBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.GanttOperationConditionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.GanttOperationConditionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.GanttOperationConditionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.GanttOperationConditionBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.GanttOperationConditionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.GanttOperationConditionBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.GanttOperationConditionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.GanttOperationConditionBuilder, object2: Mechatronics.GanttOperationConditionBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.GanttOperationConditionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class GanttOperationConditionBuilder(Builder):
    def __init__(self) -> None: ...
    def PutExpressionValue(self, exp: Expression) -> None:
        ...
    Condition: str
    ConditionId: str
    ConditionValue: str
    ExpressionValue: Expression
    Index: int
    IsGroup: bool
    ObjectValue: NXObject
    OperatorValue: str
    ParentId: str
    PhysicsObject: NXObject
    PropertyId: int
    PropertyName: str
    SignalObject: NXObject


class GanttOperationBuilder(Builder):
    def __init__(self) -> None: ...
    def AddParameterList(self, parameters: typing.List[Mechatronics.GanttOperationParameterBuilder]) -> None:
        ...
    def AddConditionList(self, conditions: typing.List[Mechatronics.GanttOperationConditionBuilder]) -> None:
        ...
    ActiveStatus: bool
    ConditionList: Mechatronics.GanttOperationConditionBuilderList
    Context: BasePart
    Duration: float
    ExpressionDuration: Expression
    OperationID: str
    OperationName: str
    OperationTypes: Mechatronics.GanttOperationBuilder.OperationType
    ParameterList: Mechatronics.GanttOperationParameterBuilderList
    ParentID: str
    Physics: NXObject
    StartTime: float
    Type: Mechatronics.GanttOperationBuilder.SimpleOperationType


    class SimpleOperationType(enum.Enum):
        Simple = 0
        Pause = 1
    

    class OperationType(enum.Enum):
        Simple = 0
        Commpound = 16
        Trigger = 32
        Pause = 64
    

class GanttLinkerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.GanttLinker]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateGanttLinkerBuilder(self, other: Mechatronics.GanttLinker) -> Mechatronics.GanttLinkerBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.GanttLinker:
        ...
    def Tag(self) -> Tag: ...



class GanttLinkerBuilder(Builder):
    def __init__(self) -> None: ...
    LogicType: Mechatronics.GanttLinkerBuilder.LinkerLogicType
    Primary: Mechatronics.GanttOperationObject
    Secondary: Mechatronics.GanttOperationObject


    class LinkerLogicType(enum.Enum):
        And = 0
        Or = 1
    

class GanttLinker(NXObject):
    def __init__(self) -> None: ...


class GanttExportPLCopenBuilder(Builder):
    def __init__(self) -> None: ...
    NativeFileBrowser: str
    ToggleLongName: bool


class GanttCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.GanttOperationObject]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateGanttOperationBuilder(self, object: Mechatronics.GanttOperationObject) -> Mechatronics.GanttOperationBuilder:
        ...
    def CreateGanttOperationParameterBuilder(self) -> Mechatronics.GanttOperationParameterBuilder:
        ...
    def CreateGanttOperationConditionBuilder(self) -> Mechatronics.GanttOperationConditionBuilder:
        ...
    def CreateGanttExportPlcopenBuilder(self, object: Mechatronics.GanttOperationObject) -> Mechatronics.GanttExportPLCopenBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.GanttOperationObject:
        ...
    def Tag(self) -> Tag: ...



class FunctionObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.FunctionObject]:
        ...
    def __init__(self, owner: Mechatronics.MechatronicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFunctionObjectBuilder(self, object: Mechatronics.FunctionObject) -> Mechatronics.FunctionObjectBuilder:
        ...
    def CreateAddComponentBuilder(self) -> Mechatronics.AddComponentBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.FunctionObject:
        ...
    def DeleteFunction(self, functionObject: Mechatronics.FunctionObject) -> None:
        ...
    def RenameFunction(self, newName: str, functionObject: Mechatronics.FunctionObject) -> None:
        ...
    def Tag(self) -> Tag: ...



class FunctionObjectBuilder(Mechatronics.SystemObjectBuilder):
    def __init__(self) -> None: ...
    def GetChildren(self, children: typing.List[NXObject]) -> None:
        ...
    def SetChildren(self, children: typing.List[NXObject]) -> None:
        ...
    def GetOccurrences(self, occurrences: typing.List[NXObject]) -> None:
        ...
    def SetOccurrences(self, occurrences: typing.List[NXObject]) -> None:
        ...
    def GetOperations(self, operations: typing.List[NXObject]) -> None:
        ...
    def SetOperations(self, operations: typing.List[NXObject]) -> None:
        ...
    def GetParameterData(self) -> typing.List[Mechatronics.FunctionObjectBuilder.ParameterData]:
        ...
    def SetParameterData(self, parameterData: typing.List[Mechatronics.FunctionObjectBuilder.ParameterData]) -> None:
        ...
    def GetRequirementData(self) -> typing.List[Mechatronics.FunctionObjectBuilder.RequirementData]:
        """[Obsolete("Deprecated in NX8.5.0.  Please use NXOpen.Mechatronics.RequirementBuilder instead.")"""
        ...
    def SetRequirementData(self, requirementData: typing.List[Mechatronics.FunctionObjectBuilder.RequirementData]) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Please use NXOpen.Mechatronics.RequirementBuilder instead.")"""
        ...
    ExampleDesc: str
    FunctionItemRevisionId: str
    FunctionOptionSet: str
    LetterName: str
    Modified: bool
    NavigatorObject: NXObject
    ObjectInformation: Mechatronics.ObjectInformationBuilder
    ObjectName: str
    Parent: NXObject
    PlmxmlFileName: str
    TypeDesc: str


    class FunctionObjectBuilderRequirementData():
        RequirementName: str
        RequirementDesc: str
        RequirementId: str
        def ToString(self) -> str:
            ...
        def __init__(self, RequirementName: str, RequirementDesc: str, RequirementId: str) -> None: ...
    

    class FunctionObjectBuilderParameterData():
        ParameterName: str
        ParameterValue: str
        def ToString(self) -> str:
            ...
        def __init__(self, ParameterName: str, ParameterValue: str) -> None: ...
    

class FunctionObject(Mechatronics.SystemObject):
    def __init__(self) -> None: ...


class ForceTorqueControlCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ForceTorqueControl]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateForceTorqueControlBuilder(self, forceControl: Mechatronics.ForceTorqueControl) -> Mechatronics.ForceTorqueControlBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ForceTorqueControl:
        ...
    def Tag(self) -> Tag: ...



class ForceTorqueControlBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    AxisJoint: Mechatronics.SelectPhysicsJoint
    AxisType: Mechatronics.ForceTorqueControlBuilder.AxisJointType
    ForceTorque: Expression


    class AxisJointType(enum.Enum):
        Angular = 0
        Linear = 1
        Mixed = 2
    

class ForceTorqueControl(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class FixedJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.FixedJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFixedJointBuilder(self, slide: Mechatronics.FixedJoint) -> Mechatronics.FixedJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.FixedJoint:
        ...
    def Tag(self) -> Tag: ...



class FixedJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    FeedbackPoint: Point


class FixedJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class ExternalSignalConfigurationObject(NXObject):
    def __init__(self) -> None: ...


class ExternalSignalConfigurationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ExternalSignalConfigurationObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateExternalSignalConfigurationBuilder(self, externalSignalConfigurationObject: Mechatronics.ExternalSignalConfigurationObject) -> Mechatronics.ExternalSignalConfigurationBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ExternalSignalConfigurationObject:
        ...
    def Tag(self) -> Tag: ...



class ExternalSignalConfigurationBuilder(Builder):
    def __init__(self) -> None: ...
    MatlabClient: Mechatronics.MATLABClientBuilder
    OPCDAClient: Mechatronics.OPCClientBuilder
    OPCUAClient: Mechatronics.OPCUAClientBuilder
    PlcSimAdvClient: Mechatronics.PlcSimAdvClientBuilder
    ProfinetClient: Mechatronics.ProfinetClientBuilder
    ShmClient: Mechatronics.SHMSignalClientBuilder
    TcpClient: Mechatronics.TCPClientBuilder
    UdpClient: Mechatronics.UDPSignalClientBuilder


class ExternalConnectionElementBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Mechatronics.ExternalConnectionElementBuilder]) -> None:
        ...
    def Append(self, object: Mechatronics.ExternalConnectionElementBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Mechatronics.ExternalConnectionElementBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Mechatronics.ExternalConnectionElementBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Mechatronics.ExternalConnectionElementBuilder) -> None:
        ...
    def Erase(self, obj: Mechatronics.ExternalConnectionElementBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Mechatronics.ExternalConnectionElementBuilder]:
        ...
    def SetContents(self, objects: typing.List[Mechatronics.ExternalConnectionElementBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Mechatronics.ExternalConnectionElementBuilder, object2: Mechatronics.ExternalConnectionElementBuilder) -> None:
        ...
    def Insert(self, location: int, object: Mechatronics.ExternalConnectionElementBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ExternalConnectionElementBuilder(Builder):
    def __init__(self) -> None: ...
    ConditionOption: Mechatronics.ExternalConnectionElementBuilder.ConditionType
    ConditionValue: float
    Inverse: bool
    Multiplier: float
    OffsetValue: float
    PropertyDataType: Mechatronics.ExternalConnectionElementBuilder.DataType
    PropertyId: int
    SignalDataType: Mechatronics.ExternalConnectionElementBuilder.DataType
    SignalName: str
    StreamOption: Mechatronics.ExternalConnectionElementBuilder.StreamType


    class StreamType(enum.Enum):
        R = 0
        W = 1
        Rw = 2
    

    class DataType(enum.Enum):
        Unknown = 0
        Integer = 1
        Float = 2
        Boolean = 3
    

    class ConditionType(enum.Enum):
        Eq = 0
        Gt = 1
        Lt = 2
        Ge = 3
        Le = 4
        Ne = 5
    

class ExternalConnectionElement(NXObject):
    def __init__(self) -> None: ...


class ExternalConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ExternalConnection]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateExternalConnectionBuilder(self, exteral: Mechatronics.ExternalConnection) -> Mechatronics.ExternalConnectionBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ExternalConnection:
        ...
    def CreateExternalConnectionElementBuilder(self, element: Mechatronics.ExternalConnectionElement) -> Mechatronics.ExternalConnectionElementBuilder:
        ...
    def Tag(self) -> Tag: ...



class ExternalConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    def RemoveAllElements(self) -> None:
        """[Obsolete("Deprecated in NX8.0.1.  Please use NXOpen.Mechatronics.ExternalConnectionElementBuilder instead.")"""
        ...
    def AddElement(self, propTag: int, signalType: int, signalName: str, propertyType: int, streamIO: int, conditionType: int, conditionValue: float, multiplier: float, offsetValue: float, boolOperator: int) -> None:
        """[Obsolete("Deprecated in NX8.0.1.  Please use NXOpen.Mechatronics.ExternalConnectionElementBuilder instead.")"""
        ...
    ConnectionList: Mechatronics.ExternalConnectionElementBuilderList
    Name: str
    SelectPhysics: SelectNXObject


    class ConditionType(enum.Enum):
        Eq = 0
        Gt = 1
        Lt = 2
        Ge = 3
        Le = 4
        Ne = 5
    

class ExternalConnection(DisplayableObject):
    def __init__(self) -> None: ...


class ExpressionBlockObject(NXObject):
    def __init__(self) -> None: ...


class ExpressionBlockFormulaCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ExpressionBlockFormula]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateExpressionBlockFormulaBuilder(self, expressionBlockFormula: Mechatronics.ExpressionBlockFormula) -> Mechatronics.ExpressionBlockFormulaBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ExpressionBlockFormula:
        ...
    def Tag(self) -> Tag: ...



class ExpressionBlockFormulaBuilder(Mechatronics.RuntimeFormulaBuilder):
    def __init__(self) -> None: ...
    FormulaComment: str


class ExpressionBlockFormula(NXObject):
    def __init__(self) -> None: ...


class ExpressionBlockCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ExpressionBlockObject]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateExpressionBlockBuilder(self, expressionBlockObject: Mechatronics.ExpressionBlockObject) -> Mechatronics.ExpressionBlockBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ExpressionBlockObject:
        ...
    def Tag(self) -> Tag: ...



class ExpressionBlockBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, descLines: str) -> None:
        ...
    def GetSlots(self) -> typing.List[Mechatronics.ExpressionBlockBuilder.Slot]:
        ...
    def SetSlots(self, slots: typing.List[Mechatronics.ExpressionBlockBuilder.Slot]) -> None:
        ...
    def SaveToXmlFile(self, templateFile: str) -> None:
        ...
    def LoadFromXmlFile(self, templateFile: str) -> None:
        ...
    Name: str


    class SlotType(enum.Enum):
        None = -1
        Input = 0
        Output = 1
        Param = 2
        State = 3
        Custom = 4
        Num = 5
    

    class ExpressionBlockBuilderSlot():
        ESlotType: Mechatronics.ExpressionBlockBuilder.SlotType
        Name: str
        EDataType: Mechatronics.ExpressionBlockBuilder.DataType
        BoolValue: bool
        IntValue: int
        DoubleValue: float
        Unit: Unit
        Formula: str
        Comment: str
        TgPhysicsObject: NXObject
        NPhysicsPropTag: int
        def ToString(self) -> str:
            ...
    

    class DataType(enum.Enum):
        Bool = 0
        Int = 1
        Double = 2
    

class ExportSensorsActuatorsBuilder(Builder):
    def __init__(self) -> None: ...
    ExportFile: str
    SensorActuatorList: Mechatronics.SensorsActuatorsListBuilderList


class ElectricalPartCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ElectricalPart]:
        ...
    def __init__(self, owner: Mechatronics.MechatronicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateElectricalPartBuilder(self, object: Mechatronics.ElectricalPart) -> Mechatronics.ElectricalPartBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ElectricalPart:
        ...
    def Tag(self) -> Tag: ...



class ElectricalPartBuilder(Builder):
    def __init__(self) -> None: ...
    def GetOwner(self) -> Mechatronics.SystemObject:
        ...
    def SetOwner(self, owner: Mechatronics.SystemObject) -> None:
        ...
    def GetAttributes(self) -> typing.List[Mechatronics.ElectricalPartBuilder.Attribute]:
        ...
    def SetAttributes(self, attribute: typing.List[Mechatronics.ElectricalPartBuilder.Attribute]) -> None:
        ...
    PartNumber: str


    class ElectricalPartBuilderAttribute():
        AttributeName: str
        AttributeValue: str
        def ToString(self) -> str:
            ...
        def __init__(self, AttributeName: str, AttributeValue: str) -> None: ...
    

class ElectricalPart(NXObject):
    def __init__(self) -> None: ...
    def GetComponent(self) -> Assemblies.Component:
        ...
    def SetComponent(self, component: Assemblies.Component) -> None:
        ...


class ECADImportBuilder(Builder):
    def __init__(self) -> None: ...
    def CompareObjects(self) -> Mechatronics.ComparisonResultContext:
        ...
    def GenerateEcadModelComponent(self, partName: str) -> BasePart:
        """[Obsolete("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.")"""
        ...
    def CreateLogicalNode(self, referenceDesignator: str) -> Mechatronics.LogicObject:
        """[Obsolete("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.")"""
        ...
    def EditLogicalNode(self, logicalNode: Mechatronics.LogicObject, itemName: str, itemId: str, oldPartOcc: Assemblies.Component, newPartOcc: Assemblies.Component, parameterData: typing.List[Mechatronics.LogicObjectBuilder.ParameterData]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.")"""
        ...
    ImportFile: str
    PositionMethod: Mechatronics.ECADImportBuilder.PositionMode


    class PositionMode(enum.Enum):
        InferredOnly = 0
        AbsoluteOrigin = 1
        SelectOrigin = 2
        ByConstraints = 3
        Move = 4
    

class ECADExportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetExportAttributesName(self) -> str:
        """[Obsolete("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.")"""
        ...
    def SetExportAttributesName(self, exportAttributesName: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.")"""
        ...
    ExportFile: str
    ExportFileFormat: Mechatronics.ECADExportBuilder.ExportFileType
    SelectLogicals: Mechatronics.SelectLogicObjectList


    class ExportFileType(enum.Enum):
        Xml = 0
        Csv = 1
        Eplan = 2
    

class DynamicObjectTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.DynamicObjectTable]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDynamicObjectTableBuilder(self, dynamicObjectTable: Mechatronics.DynamicObjectTable) -> Mechatronics.DynamicObjectTableBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.DynamicObjectTable:
        ...
    def Tag(self) -> Tag: ...



class DynamicObjectTableBuilder(Builder):
    def __init__(self) -> None: ...
    def GetInstances(self) -> typing.List[Mechatronics.DynamicObjectTableBuilder.Instance]:
        ...
    def SetInstances(self, instances: typing.List[Mechatronics.DynamicObjectTableBuilder.Instance]) -> None:
        ...
    Name: str


    class DynamicObjectTableBuilderInstance():
        Name: str
        TDefiningSnap: NXObject
        TDynamicObject: NXObject
        TComplyingSnap: NXObject
        def ToString(self) -> str:
            ...
    

class DynamicObjectTable(NXObject):
    def __init__(self) -> None: ...


class DistanceSensorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.DistanceSensor]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDistanceSensorBuilder(self, distanceSensor: Mechatronics.DistanceSensor) -> Mechatronics.DistanceSensorBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.DistanceSensor:
        ...
    def Tag(self) -> Tag: ...



class DistanceSensorBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: Expression
    Category: int
    Direction: Direction
    HighlightOnCollision: bool
    LowerOutputRange: Expression
    MeasureType: Mechatronics.DistanceSensorBuilder.OutputMeasureType
    Name: str
    Point: Point
    Range: Expression
    RigidBody: Mechatronics.SelectRigidBody
    UpperOutputRange: Expression
    UseScale: bool


    class OutputMeasureType(enum.Enum):
        Constant = 0
        Voltage = 1
        Current = 2
    

class DistanceSensor(DisplayableObject):
    def __init__(self) -> None: ...


class DisplayChangerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.DisplayChanger]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDisplayChangerBuilder(self, objectSrc: Mechatronics.DisplayChanger) -> Mechatronics.DisplayChangerBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.DisplayChanger:
        ...
    def Tag(self) -> Tag: ...



class DisplayChangerBuilder(Builder):
    def __init__(self) -> None: ...
    CollisionSensor: Mechatronics.SelectCollisionSensor
    Color: int
    ExecuteMode: Mechatronics.DisplayChangerBuilder.ExecuteModes
    InitVisibility: bool
    Name: str
    Translucency: int


    class ExecuteModes(enum.Enum):
        None = 0
        Always = 1
        OnceOnly = 2
    

class DisplayChanger(DisplayableObject):
    def __init__(self) -> None: ...


class DependencyCreatorBuilder(Builder):
    def __init__(self) -> None: ...
    DependentObject: SelectNXObjectList
    ParentObject: Mechatronics.SelectSystemObject


class CylindricalJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.CylindricalJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCylindricalJointBuilder(self, cylinJoint: Mechatronics.CylindricalJoint) -> Mechatronics.CylindricalJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.CylindricalJoint:
        ...
    def Tag(self) -> Tag: ...



class CylindricalJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AnchorPoint: Point
    AngularLowerLimit: Expression
    AngularUpperLimit: Expression
    AxisVector: Direction
    EnableAngularLowerLimit: bool
    EnableAngularUpperLimit: bool
    EnableLinearLowerLimit: bool
    EnableLinearUpperLimit: bool
    LinearLowerLimit: Expression
    LinearUpperLimit: Expression
    Offset: Expression
    StartAngle: Expression


class CylindricalJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class CurveOnCurveJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.CurveOnCurveJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCurveOnCurveJointBuilder(self, joint: Mechatronics.CurveOnCurveJoint) -> Mechatronics.CurveOnCurveJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.CurveOnCurveJoint:
        ...
    def Tag(self) -> Tag: ...



class CurveOnCurveJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    def GetSectionCurve(self) -> typing.List[NXObject]:
        ...
    def SetSectionCurve(self, curves: typing.List[NXObject]) -> None:
        ...
    def GetConnectedCurve(self) -> typing.List[NXObject]:
        ...
    def SetConnectedCurve(self, curves: typing.List[NXObject]) -> None:
        ...
    def EvaluatePath(self, curves: typing.List[NXObject]) -> None:
        ...
    AxisVector: Direction
    Offset: Expression
    PointOnCurve: Point
    Sliding: bool


class CurveOnCurveJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class CouplingBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetMasterAxisJoint(self, master: Mechatronics.PhysicsJoint) -> None:
        ...
    def SetSlaveAxisJoint(self, slave: Mechatronics.PhysicsJoint) -> None:
        ...
    AllowSlip: bool
    MasterAxisJoint: Mechatronics.SelectPhysicsJoint
    SlaveAxisJoint: Mechatronics.SelectPhysicsJoint


class Coupling(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class ConvertFromMTBBuilder(Builder):
    def __init__(self) -> None: ...


class ComparisonResultElectricalPart(Mechatronics.ComparisonResultBase):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetAttributes(self, attributeNames: str, attributeValues: str) -> None:
        ...
    ComparisonStatus: Mechatronics.ComparisonResultElectricalPart.Status
    PartNumber: str


    class Status(enum.Enum):
        Added = 0
        Removed = 1
        Updated = 2
        Identical = 3
    

class ComparisonResultContext(Mechatronics.ComparisonResultBase):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetResults(self, results: typing.List[Mechatronics.ComparisonResult]) -> None:
        ...
    def ResolveConflictResult(self, conflictResult: Mechatronics.ComparisonResult, action: Mechatronics.ComparisonResultContext.ResolveConflictAction, replacements: typing.List[Mechatronics.ComparisonResult]) -> None:
        ...
    EcadProjectId: str
    PartName: str


    class ResolveConflictAction(enum.Enum):
        Ignore = 0
        Create = 1
        Update = 2
    

class ComparisonResultBase(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Ignored: bool


class ComparisonResultAttribute(Mechatronics.ComparisonResultBase):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    EcadValue: str
    LogicalValue: str
    Name: str


class ComparisonResult(Mechatronics.ComparisonResultBase):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetAttributes(self, attributes: typing.List[Mechatronics.ComparisonResultAttribute]) -> None:
        ...
    def GetElectricalParts(self, electricalParts: typing.List[Mechatronics.ComparisonResultElectricalPart]) -> None:
        ...
    ConflictLogicalObject: Mechatronics.LogicObject
    LogicalObject: Mechatronics.LogicObject
    ResultCategory: Mechatronics.ComparisonResult.Category
    ResultName: str
    ResultType: str


    class Category(enum.Enum):
        Create = 0
        UpdateAttributes = 1
        UpdateParts = 2
        Move = 3
        Delete = 4
        CreateConflict = 5
        MoveConflict = 6
        NotFoundConflict = 7
        NoAction = 8
    

class CollisionShapeBuilder(Builder):
    def __init__(self) -> None: ...
    CenterPoint: Point
    Height: Expression
    Length: Expression
    Orientation: CoordinateSystem
    Radius: Expression
    Width: Expression


class CollisionSensorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.CollisionSensor]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCollisionSensorBuilder(self, triggerBody: Mechatronics.CollisionSensor) -> Mechatronics.CollisionSensorBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.CollisionSensor:
        ...
    def Tag(self) -> Tag: ...



class CollisionSensorBuilder(Mechatronics.CollisionShapeBuilder):
    def __init__(self) -> None: ...
    def SetGeometry(self, geometries: typing.List[NXObject]) -> None:
        ...
    Category: int
    CollisionShape: Mechatronics.CollisionSensorBuilder.CollisionShapeTypes
    Geometry: SelectNXObjectList
    HighlightOnCollision: bool
    Name: str
    ShapeProperties: Mechatronics.CollisionSensorBuilder.ShapePropertiesOption


    class ShapePropertiesOption(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

    class CollisionShapeTypes(enum.Enum):
        Box = 0
        Sphere = 1
        Line = 2
    

class CollisionSensor(DisplayableObject):
    def __init__(self) -> None: ...


class CollisionMaterialCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.CollisionMaterial]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCollisionMaterialBuilder(self, collisionMaterial: Mechatronics.CollisionMaterial) -> Mechatronics.CollisionMaterialBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.CollisionMaterial:
        ...
    def Tag(self) -> Tag: ...



class CollisionMaterialBuilder(Builder):
    def __init__(self) -> None: ...
    DynamicFriction: Expression
    Name: str
    Restitution: Expression
    RollingFriction: Expression
    StaticFriction: Expression


class CollisionMaterial(NXObject):
    def __init__(self) -> None: ...


class CollisionBodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.CollisionBody]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCollisionBodyBuilder(self, collideBody: Mechatronics.CollisionBody) -> Mechatronics.CollisionBodyBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.CollisionBody:
        ...
    def Tag(self) -> Tag: ...



class CollisionBodyBuilder(Mechatronics.CollisionShapeBuilder):
    def __init__(self) -> None: ...
    def SetGeometry(self, geometries: typing.List[NXObject]) -> None:
        ...
    def CalculateConvex(self) -> None:
        ...
    def CalculateMesh(self) -> None:
        ...
    def CalculateMultiConvex(self) -> None:
        ...
    Category: int
    CollisionFactor: float
    CollisionMaterial: Mechatronics.CollisionMaterial
    CollisionProperties: Mechatronics.CollisionBodyBuilder.ShapePropertyTypes
    CollisionShape: Mechatronics.CollisionBodyBuilder.CollisionShapeTypes
    Geometry: SelectNXObjectList
    HighlightOnCollision: bool
    Name: str
    StickCollision: bool


    class ShapePropertyTypes(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

    class CollisionShapeTypes(enum.Enum):
        Box = 0
        Sphere = 1
        Cylinder = 2
        Capsule = 3
        Convex = 4
        MultiConvex = 5
        Mesh = 6
    

class CollisionBody(DisplayableObject):
    def __init__(self) -> None: ...


class ChangeOwnerBuilder(Builder):
    def __init__(self) -> None: ...
    def CheckButton(self) -> None:
        ...
    Component: Assemblies.SelectComponent
    PhysicsObject: SelectNXObjectList


class ChangeMaterialCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.ChangeMaterial]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateChangeMaterialBuilder(self, changeMaterial: Mechatronics.ChangeMaterial) -> Mechatronics.ChangeMaterialBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.ChangeMaterial:
        ...
    def Tag(self) -> Tag: ...



class ChangeMaterialBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetFirstBody(self, firstBody: DisplayableObject) -> None:
        ...
    def SetSecondBody(self, secondBody: DisplayableObject) -> None:
        ...
    CollisionMaterial: Mechatronics.CollisionMaterial
    FirstBody: SelectDisplayableObject
    SecondBody: SelectDisplayableObject


class ChangeMaterial(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class ChainJointBuilder(Builder):
    def __init__(self) -> None: ...
    AnchorPointSecond: Point
    AngularLowerLimit: Expression
    AngularUpperLimit: Expression
    BaseAnchorPoint: Point
    BaseAxisVector: Direction
    EnableAngularLowerLimit: bool
    EnableAngularUpperLimit: bool
    EnableSecondAnchor: bool
    Geometry: SelectNXObjectList
    Name: str
    StartAngle: Expression


class CamProfileCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.CamProfile]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCamProfileBuilder(self, segmentTable: Mechatronics.CamProfile) -> Mechatronics.CamProfileBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.CamProfile:
        ...
    def Tag(self) -> Tag: ...



class CamProfileBuilder(Builder):
    def __init__(self) -> None: ...
    def FindElementIndex(self, element: Mechatronics.CamProfileBuilder.Element) -> int:
        ...
    def AddElement(self, part: NXObject, element: Mechatronics.CamProfileBuilder.Element) -> None:
        ...
    def EditElement(self, index: int, part: NXObject, element: Mechatronics.CamProfileBuilder.Element) -> None:
        ...
    def RemoveElementByIndex(self, index: int) -> None:
        ...
    def ClearElements(self) -> None:
        ...
    def SetSegmentTable(self, segmentTableObject: Mechatronics.CamProfile) -> None:
        ...
    def AskElementByIndex(self, index: int) -> Mechatronics.CamProfileBuilder.Element:
        ...
    def AskElementsLength(self) -> int:
        ...
    def SwitchSegmentTable(self, segmentTableObject: Mechatronics.CamProfile) -> None:
        ...
    CheckingG2Continuity: bool
    CyclicType: Mechatronics.CamProfileBuilder.ProfileCyclicType
    IsForElecCam: bool
    MasterMaximum: Expression
    MasterMinimum: Expression
    MasterUnit: Mechatronics.CamProfileBuilder.MasterValueUnit
    Name: str
    SlaveMaximum: Expression
    SlaveMinimum: Expression
    SlaveUnit: Mechatronics.CamProfileBuilder.SlaveValueUnit


    class SlaveValueUnit(enum.Enum):
        LinearPosition = 0
        RotaryPosition = 1
        LinearSpeed = 2
        RotarySpeed = 3
    

    class ProfileCyclicType(enum.Enum):
        RelativeCyclic = 0
        Cyclic = 1
        NonCyclic = 2
    

    class MasterValueUnit(enum.Enum):
        Linear = 0
        Rotary = 1
        Time = 2
    

    class CamProfileBuilderElement():
        Id: int
        SegmentName: str
        SegmentType: int
        CurveType: int
        Slope: float
        Curvature: float
        MasterMin: float
        MasterMax: float
        SlaveMin: float
        SlaveMax: float
        Xn1: float
        Xn2: float
        A0: float
        A1: float
        A2: float
        A3: float
        A4: float
        A5: float
        A6: float
        Amplitude: float
        AngularFrequency: float
        Phase: float
        SlopeEqualPrev: bool
        SlopeEqualNext: bool
        CurveEqualPrev: bool
        CurveEqualNext: bool
        Slope2: float
        Jerk: float
        FormulaType: int
        LambdaValue: float
        OptimizeType: int
        YnMin: float
        YnMax: float
        def ToString(self) -> str:
            ...
    

class CamProfile(NXObject):
    def __init__(self) -> None: ...


class CamCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Cam]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCamBuilder(self, camConstraint: Mechatronics.Cam) -> Mechatronics.CamBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Cam:
        ...
    def Tag(self) -> Tag: ...



class CamBuilder(Mechatronics.CouplingBuilder):
    def __init__(self) -> None: ...
    def GetCurveFeatures(self) -> typing.List[Features.Feature]:
        ...
    def SetCurveFeatures(self, curveFeatures: typing.List[Features.Feature]) -> None:
        ...
    def AddCurveFeature(self, curveFeature: Features.Feature) -> None:
        ...
    def GetExtrudeFeature(self) -> Features.Feature:
        ...
    def SetExtrudeFeature(self, extrudeFeature: Features.Feature) -> None:
        ...
    def AddCamDiskToMasterAxis(self, update: bool) -> bool:
        ...
    AddCamDiskToMasterJointOption: Mechatronics.CamBuilder.AddCamDiskToMasterOption
    CamDiskRefPoint: Point
    CamDiskType: Mechatronics.CamBuilder.CreateCamDiskType
    CamProfile: Mechatronics.CamProfile
    CreateCamDisk: bool
    ExtrudeLength: Expression
    LayerSettings: Display.LayerSettingsBuilder
    MasterAxisType: Mechatronics.CamBuilder.AxisJointType
    MasterOffset: Expression
    MasterScaleFactor: Expression
    MotionProfile: Mechatronics.MotionProfile
    RefPointOption: int
    SlaveAxisType: Mechatronics.CamBuilder.AxisJointType
    SlaveOffset: Expression
    SlaveScaleFactor: Expression


    class CreateCamDiskType(enum.Enum):
        Curve = 0
        Solid = 1
    

    class AxisJointType(enum.Enum):
        Linear = 0
        Angular = 1
    

    class AddCamDiskToMasterOption(enum.Enum):
        None = 0
        Edit = 1
        Replace = 2
    

class Cam(Mechatronics.Coupling):
    def __init__(self) -> None: ...


class BreakingConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.BreakingConstraint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBreakingConstraintBuilder(self, hinge: Mechatronics.BreakingConstraint) -> Mechatronics.BreakingConstraintBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.BreakingConstraint:
        ...
    def Tag(self) -> Tag: ...



class BreakingConstraintBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    def SetJoint(self, joint: Mechatronics.PhysicsJoint) -> None:
        ...
    BreakingMode: Mechatronics.BreakingConstraintBuilder.BreakingModeType
    Direction: Direction
    FixedDirection: bool
    Joint: Mechatronics.SelectPhysicsJoint
    MaximumMagnitude: Expression


    class BreakingModeType(enum.Enum):
        Force = 0
        Torque = 1
    

class BreakingConstraint(Mechatronics.PhysicsConstraint):
    def __init__(self) -> None: ...


class BallJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.BallJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBallJointBuilder(self, slide: Mechatronics.BallJoint) -> Mechatronics.BallJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.BallJoint:
        ...
    def Tag(self) -> Tag: ...



class BallJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AnchorPoint: Point


class BallJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class AnimationConversionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTentativePhysics(self, physics: typing.List[NXObject]) -> None:
        ...
    def EnableObjectsConversion(self, physics: typing.List[NXObject], enable: bool) -> None:
        ...
    Associative: bool


class AngularSpringJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.AngularSpringJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAngularSpringJointBuilder(self, angularSpring: Mechatronics.AngularSpringJoint) -> Mechatronics.AngularSpringJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.AngularSpringJoint:
        ...
    def Tag(self) -> Tag: ...



class AngularSpringJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AttachmentVector: Direction
    BaseVector: Direction
    Damping: Expression
    FeedbackPoint: Point
    RelaxedPosition: Expression
    SpringConstant: Expression


class AngularSpringJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class AngularLimitJointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.AngularLimitJoint]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAngularLimitJointBuilder(self, angularLimit: Mechatronics.AngularLimitJoint) -> Mechatronics.AngularLimitJointBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.AngularLimitJoint:
        ...
    def Tag(self) -> Tag: ...



class AngularLimitJointBuilder(Mechatronics.PhysicsJointBuilder):
    def __init__(self) -> None: ...
    AttachmentVector: Direction
    BaseVector: Direction
    FeedbackPoint: Point
    MaximumPosition: Expression
    MinimumPosition: Expression


class AngularLimitJoint(Mechatronics.PhysicsJoint):
    def __init__(self) -> None: ...


class AlignBodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.AlignBody]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAlignBodyBuilder(self, snapPoint: Mechatronics.AlignBody) -> Mechatronics.AlignBodyBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.AlignBody:
        ...
    def Tag(self) -> Tag: ...



class AlignBodyBuilder(Builder):
    def __init__(self) -> None: ...
    def SetAttachbody(self, rigid: NXObject) -> None:
        ...
    AttachBody: Mechatronics.SelectRigidBody
    AttachPoint: Point
    Category: int
    JunctionName: str
    Name: str
    Orientation: CoordinateSystem
    Proximity: Expression
    SnapRole: Mechatronics.AlignBodyBuilder.RoleType


    class RoleType(enum.Enum):
        Source = 0
        Target = 1
    

class AlignBody(NXObject):
    def __init__(self) -> None: ...


class AddComponentBuilder(Builder):
    def __init__(self) -> None: ...


class AdapterSignalCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.AdapterSignal]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAdapterSignalBuilder(self, object: Mechatronics.AdapterSignal) -> Mechatronics.AdapterSignalBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.AdapterSignal:
        ...
    def Tag(self) -> Tag: ...



class AdapterSignalBuilder(Mechatronics.ProxyObjectBuilder):
    def __init__(self) -> None: ...
    AssignedFormula: Mechatronics.AdapterFormula
    InputOutput: int


class AdapterSignal(DisplayableObject):
    def __init__(self) -> None: ...


class AdapterFormulaCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.AdapterFormula]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAdapterFormulaBuilder(self, object: Mechatronics.AdapterFormula) -> Mechatronics.AdapterFormulaBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.AdapterFormula:
        ...
    def Tag(self) -> Tag: ...



class AdapterFormulaBuilder(Mechatronics.RuntimeFormulaBuilder):
    def __init__(self) -> None: ...
    FormulaComment: str


class AdapterFormula(NXObject):
    def __init__(self) -> None: ...


class AccelerometerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Mechatronics.Accelerometer]:
        ...
    def __init__(self, owner: Mechatronics.PhysicsManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAccelerometerBuilder(self, accelerometer: Mechatronics.Accelerometer) -> Mechatronics.AccelerometerBuilder:
        ...
    def FindObject(self, name: str) -> Mechatronics.Accelerometer:
        ...
    def Tag(self) -> Tag: ...



class AccelerometerBuilder(Mechatronics.PhysicsConstraintBuilder):
    def __init__(self) -> None: ...
    LowerAngularTrimRange: Expression
    LowerOutputRange: Expression
    LowerTrimRange: Expression
    MeasureType: Mechatronics.AccelerometerBuilder.OutputMeasureType
    RigidBody: Mechatronics.SelectRigidBody
    UpperAngularTrimRange: Expression
    UpperOutputRange: Expression
    UpperTrimRange: Expression
    UseScale: bool
    UseTrim: bool


    class OutputMeasureType(enum.Enum):
        Constant = 0
        Voltage = 1
        Current = 2
    

class Accelerometer(DisplayableObject):
    def __init__(self) -> None: ...


