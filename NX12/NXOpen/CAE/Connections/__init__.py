from ....NXOpen import *
from ...CAE import *
from ..Connections import *

import typing
import enum

class Utils(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Connections.Folder) -> None: ...
    def FilterConnectionsByType(self, iConnections: typing.List[CAE.Connections.IConnection], type: CAE.Connections.ConnectionType) -> typing.List[CAE.Connections.IConnection]:
        ...
    def Tag(self) -> Tag: ...



class TargetDependencyType(enum.Enum):
    None = 0
    Dependent = 1
    Independent = 2


class Spring(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    RxStiffnessConstant: Expression
    RyStiffnessConstant: Expression
    RzStiffnessConstant: Expression
    XStiffnessConstant: Expression
    YStiffnessConstant: Expression
    ZStiffnessConstant: Expression
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression


class SpotWeld(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def IsInheritedMaterial(self) -> bool:
        ...
    def SetInheritedMaterial(self) -> None:
        ...
    def CanInheritMaterial(self) -> bool:
        ...
    def CanHaveNoMaterial(self) -> bool:
        ...
    def GetSupportedDiameterTypes(self) -> typing.List[CAE.Connections.DiameterType]:
        ...
    def GetSupportedHeightTypes(self) -> typing.List[CAE.Connections.HeightType]:
        ...
    def GetFlangeEntities(self, flangeIndex: int) -> typing.List[TaggedObject]:
        ...
    def AddFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def GetMaxNumberOfFlanges(self) -> int:
        ...
    def GetMinNumberOfFlanges(self) -> int:
        ...
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        ...
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        ...
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfDefinitions(self) -> int:
        ...
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        ...
    def AddLocationNode(self, indexOfDefinition: int, node: CAE.FENode) -> CAE.Connections.NodeLocation:
        ...
    def AddLocationCoordinates(self, indexOfDefinition: int, coordinates: Point3d) -> CAE.Connections.CoordinatesLocation:
        ...
    def AddLocationPoint(self, indexOfDefinition: int, point: Point) -> CAE.Connections.PointLocation:
        ...
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: typing.List[CAE.FENode]) -> CAE.Connections.NodeSeriesLocation:
        ...
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: typing.List[Point]) -> CAE.Connections.PointSeriesLocation:
        ...
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: typing.List[Point3d]) -> CAE.Connections.CoordinatesSeriesLocation:
        ...
    def AddLocationCurve(self, indexOfDefinition: int, curve: IBaseCurve) -> CAE.Connections.CurveLocation:
        ...
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: typing.List[CAE.FEElemEdge]) -> CAE.Connections.FeEdgesLocation:
        ...
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> Direction:
        ...
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: Direction) -> None:
        ...
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> Expression:
        ...
    Material: PhysicalMaterial
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    Coefficient: Expression
    Diameter: Expression
    DiameterType: CAE.Connections.DiameterType
    TableFile: str
    Height: Expression
    HeightType: CAE.Connections.HeightType
    NumberOfFlanges: int
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool


class SelectionRecipeLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    SelectionRecipe: CAE.SelectionRecipe


class SeamWeldType(enum.Enum):
    WithMaterial = 0
    WithLaser = 1


class SeamWeldMaterialType(enum.Enum):
    Angle = 0
    Overlap = 1
    Double = 2


class SeamWeld(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def IsInheritedMaterial(self) -> bool:
        ...
    def SetInheritedMaterial(self) -> None:
        ...
    def CanInheritMaterial(self) -> bool:
        ...
    def CanHaveNoMaterial(self) -> bool:
        ...
    def GetSupportedHeightTypes(self) -> typing.List[CAE.Connections.HeightType]:
        ...
    def GetFlangeEntities(self, flangeIndex: int) -> typing.List[TaggedObject]:
        ...
    def AddFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def GetMaxNumberOfFlanges(self) -> int:
        ...
    def GetMinNumberOfFlanges(self) -> int:
        ...
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        ...
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        ...
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfDefinitions(self) -> int:
        ...
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        ...
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> Direction:
        ...
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: Direction) -> None:
        ...
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> Expression:
        ...
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: typing.List[CAE.FENode]) -> CAE.Connections.NodeSeriesLocation:
        ...
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: typing.List[Point]) -> CAE.Connections.PointSeriesLocation:
        ...
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: typing.List[Point3d]) -> CAE.Connections.CoordinatesSeriesLocation:
        ...
    def AddLocationCurve(self, indexOfDefinition: int, curve: IBaseCurve) -> CAE.Connections.CurveLocation:
        ...
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: typing.List[CAE.FEElemEdge]) -> CAE.Connections.FeEdgesLocation:
        ...
    SeamWeldType: CAE.Connections.SeamWeldType
    Material: PhysicalMaterial
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    Height: Expression
    HeightType: CAE.Connections.HeightType
    NumberOfFlanges: int
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool
    Width: Expression


class Sealing(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetFlangeEntities(self, flangeIndex: int) -> typing.List[TaggedObject]:
        ...
    def AddFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def GetMaxNumberOfFlanges(self) -> int:
        ...
    def GetMinNumberOfFlanges(self) -> int:
        ...
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        ...
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        ...
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfDefinitions(self) -> int:
        ...
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        ...
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> Direction:
        ...
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: Direction) -> None:
        ...
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> Expression:
        ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: typing.List[CAE.FENode]) -> CAE.Connections.NodeSeriesLocation:
        ...
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: typing.List[Point]) -> CAE.Connections.PointSeriesLocation:
        ...
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: typing.List[Point3d]) -> CAE.Connections.CoordinatesSeriesLocation:
        ...
    def AddLocationCurve(self, indexOfDefinition: int, curve: IBaseCurve) -> CAE.Connections.CurveLocation:
        ...
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: typing.List[CAE.FEElemEdge]) -> CAE.Connections.FeEdgesLocation:
        ...
    WithOrientation: bool
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    NumberOfFlanges: int
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool
    RxStiffnessConstant: Expression
    RyStiffnessConstant: Expression
    RzStiffnessConstant: Expression
    XStiffnessConstant: Expression
    YStiffnessConstant: Expression
    ZStiffnessConstant: Expression
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType


class Rigid(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetDof(self, dof: CAE.Connections.Dof) -> CAE.Connections.DofType:
        ...
    def SetDof(self, dof: CAE.Connections.Dof, type: CAE.Connections.DofType) -> None:
        ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression


class PointSeriesLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    def GetPoints(self) -> typing.List[Point]:
        ...
    def AddPoints(self, points: typing.List[Point]) -> None:
        ...
    def SetPoints(self, points: typing.List[Point]) -> None:
        ...


class PointLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    Point: Point


class NodeSeriesLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...
    def AddNodes(self, nodes: typing.List[CAE.FENode]) -> None:
        ...
    def SetNodes(self, nodes: typing.List[CAE.FENode]) -> None:
        ...


class NodeLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    Node: CAE.FENode


class NodalTargetType(enum.Enum):
    SinglePoint = 0
    SetOfPoints = 1
    Spider = 2
    None = 3


class NodalTargetSpider(CAE.Connections.NodalTarget):
    def __init__(self) -> None: ...
    def GetLegsEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    TargetCenter: TaggedObject


class NodalTargetSinglePoint(CAE.Connections.NodalTarget):
    def __init__(self) -> None: ...
    TargetCenter: TaggedObject


class NodalTargetSetOfPoints(CAE.Connections.NodalTarget):
    def __init__(self) -> None: ...
    def GetLegsEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...


class NodalTarget(NXObject):
    def __init__(self) -> None: ...
    TargetType: CAE.Connections.NodalTargetType


class NodalPairingMethod(enum.Enum):
    Proximity = 0
    OrientatedSearch = 1
    SelectionOrder = 2


class ModelizationResultType(enum.Enum):
    None = 0
    Material = 1
    Weights = 2
    Section = 3
    Csys = 4
    Stiffness = 5
    ViscousDamping = 6
    StructuralDamping = 7
    Dofs = 8
    DynamicStiffness = 9
    DynamicViscousDamping = 10
    DynamicStructuralDamping = 11


class ModelizationPPTRefTargetType(enum.Enum):
    None = 0
    Ec = 1
    Ecc = 2
    Ead = 3


class MaterialType(enum.Enum):
    User = 0
    FromSupport = 1


class LocationWithDir(CAE.Connections.Location):
    def __init__(self) -> None: ...
    DirectionPoint: Point
    DirectionType: CAE.Connections.LocationDirectionType
    DirectionValue: Vector3d
    DirectionVector: Direction
    Point: Point


class LocationType(enum.Enum):
    Coordinates = 0
    Point = 1
    Node = 2
    SeriesOfNodes = 3
    SeriesOfCoordinates = 4
    Curve = 5
    FeEdgeGroup = 6
    SeriesOfPoints = 7
    LocationWithDirection = 8
    SelectionRecipe = 9


class LocationDirectionType(enum.Enum):
    Point = 0
    Vector = 1
    Curve = 2


class Location(TaggedObject):
    def __init__(self) -> None: ...
    def GetXyzCoordinates(self) -> typing.List[Point3d]:
        ...


class Kinematic(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetDof(self, dof: CAE.Connections.Dof) -> CAE.Connections.DofType:
        ...
    def SetDof(self, dof: CAE.Connections.Dof, type: CAE.Connections.DofType) -> None:
        ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    DofCombination: CAE.Connections.DofCombination
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression


class IWidth():
    Width: Expression


class IViscousDampingDynamic():
    RxViscousDampingDynamic: Fields.ScalarFieldWrapper
    RyViscousDampingDynamic: Fields.ScalarFieldWrapper
    RzViscousDampingDynamic: Fields.ScalarFieldWrapper
    XViscousDampingDynamic: Fields.ScalarFieldWrapper
    YViscousDampingDynamic: Fields.ScalarFieldWrapper
    ZViscousDampingDynamic: Fields.ScalarFieldWrapper


class IViscousDamping():
    RxViscousDampingConstant: Expression
    RyViscousDampingConstant: Expression
    RzViscousDampingConstant: Expression
    XViscousDampingConstant: Expression
    YViscousDampingConstant: Expression
    ZViscousDampingConstant: Expression


class ITolerance():
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression


class IStructuralDampingDynamic():
    RxStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RyStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RzStructuralDampingDynamic: Fields.ScalarFieldWrapper
    XStructuralDampingDynamic: Fields.ScalarFieldWrapper
    YStructuralDampingDynamic: Fields.ScalarFieldWrapper
    ZStructuralDampingDynamic: Fields.ScalarFieldWrapper


class IStructuralDamping():
    RxStructuralDampingConstant: Expression
    RyStructuralDampingConstant: Expression
    RzStructuralDampingConstant: Expression
    XStructuralDampingConstant: Expression
    YStructuralDampingConstant: Expression
    ZStructuralDampingConstant: Expression


class IStiffnessDynamic():
    RxStiffnessDynamic: Fields.ScalarFieldWrapper
    RyStiffnessDynamic: Fields.ScalarFieldWrapper
    RzStiffnessDynamic: Fields.ScalarFieldWrapper
    XStiffnessDynamic: Fields.ScalarFieldWrapper
    YStiffnessDynamic: Fields.ScalarFieldWrapper
    ZStiffnessDynamic: Fields.ScalarFieldWrapper


class IStiffness():
    RxStiffnessConstant: Expression
    RyStiffnessConstant: Expression
    RzStiffnessConstant: Expression
    XStiffnessConstant: Expression
    YStiffnessConstant: Expression
    ZStiffnessConstant: Expression


class INodalTargetsPairing():
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression


class INodalTargetsContainer():
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...


class INodalTargetLegs():
    def GetLegsEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...


class INodalTargetCenter():
    TargetCenter: TaggedObject


class IMaterial():
    def IsInheritedMaterial(self) -> bool:
        ...
    def SetInheritedMaterial(self) -> None:
        ...
    def CanInheritMaterial(self) -> bool:
        ...
    def CanHaveNoMaterial(self) -> bool:
        ...
    Material: PhysicalMaterial


class ILocationsWithDiscretizationContainer():
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: typing.List[CAE.FENode]) -> CAE.Connections.NodeSeriesLocation:
        ...
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: typing.List[Point]) -> CAE.Connections.PointSeriesLocation:
        ...
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: typing.List[Point3d]) -> CAE.Connections.CoordinatesSeriesLocation:
        ...
    def AddLocationCurve(self, indexOfDefinition: int, curve: IBaseCurve) -> CAE.Connections.CurveLocation:
        ...
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: typing.List[CAE.FEElemEdge]) -> CAE.Connections.FeEdgesLocation:
        ...


class ILocationsWithDirContainer():
    def AddLocationCoordinatesWithDirectionCoordinates(self, indexOfDefinition: int, point: Point, direction: Point) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationCoordinatesWithDirectionVector(self, indexOfDefinition: int, masterPoint: Point, direction: Direction) -> CAE.Connections.LocationWithDir:
        ...


class ILocationsSinglePointContainer():
    def AddLocationNode(self, indexOfDefinition: int, node: CAE.FENode) -> CAE.Connections.NodeLocation:
        ...
    def AddLocationCoordinates(self, indexOfDefinition: int, coordinates: Point3d) -> CAE.Connections.CoordinatesLocation:
        ...
    def AddLocationPoint(self, indexOfDefinition: int, point: Point) -> CAE.Connections.PointLocation:
        ...


class ILocationsMultiPointContainer():
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...


class ILocationsContainer():
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        ...
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        ...
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfDefinitions(self) -> int:
        ...
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        ...


class ILineOffset():
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> Direction:
        ...
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: Direction) -> None:
        ...
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> Expression:
        ...


class ILineDiscretization():
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool


class IHeight():
    def GetSupportedHeightTypes(self) -> typing.List[CAE.Connections.HeightType]:
        ...
    Height: Expression
    HeightType: CAE.Connections.HeightType


class IFlangesContainer():
    def GetFlangeEntities(self, flangeIndex: int) -> typing.List[TaggedObject]:
        ...
    def AddFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def GetMaxNumberOfFlanges(self) -> int:
        ...
    def GetMinNumberOfFlanges(self) -> int:
        ...
    NumberOfFlanges: int


class IDofCombination():
    DofCombination: CAE.Connections.DofCombination


class IDof():
    def GetDof(self, dof: CAE.Connections.Dof) -> CAE.Connections.DofType:
        ...
    def SetDof(self, dof: CAE.Connections.Dof, type: CAE.Connections.DofType) -> None:
        ...


class IDiameter():
    def GetSupportedDiameterTypes(self) -> typing.List[CAE.Connections.DiameterType]:
        ...
    Coefficient: Expression
    Diameter: Expression
    DiameterType: CAE.Connections.DiameterType
    TableFile: str


class ICsys():
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType


class IConnection(DisplayableObject):
    def __init__(self) -> None: ...
    UserDescription: str


class HeightType(enum.Enum):
    Undefined = -1
    User = 0
    MeanOfFlangesThickness = 1
    DistanceBetweenFlanges = 2
    DistanceBetweenFlangesMeanOfFlangesThickness = 3
    DistanceBetweenFlangesMaxOfFlangesThickness = 4


class HeadDiameterType(enum.Enum):
    User = 0
    FactorOfDiameter = 1


class Folder(NXObject):
    def __init__(self) -> None: ...
    def GetChildFolders(self) -> typing.List[CAE.Connections.Folder]:
        ...
    def GetConnections(self) -> typing.List[CAE.Connections.IConnection]:
        ...
    def GetAllConnections(self) -> typing.List[CAE.Connections.IConnection]:
        ...
    def CreateFolder(self, name: str) -> CAE.Connections.Folder:
        ...
    def AddFolder(self, subfolder: CAE.Connections.Folder) -> None:
        ...
    def MoveConnectionToThisFolder(self, connection: CAE.Connections.IConnection) -> None:
        ...
    def ImportSpotWeldFromWcd(self, file: str, inputFileUnit: Unit) -> typing.List[CAE.Connections.SpotWeld]:
        ...
    def ImportConnectionsFromMcf(self, file: str, inputFileUnit: Unit) -> typing.List[CAE.Connections.IConnection]:
        ...
    def CreateConnection(self, type: CAE.Connections.ConnectionType, name: str) -> CAE.Connections.IConnection:
        ...
    ConnectionUtils: CAE.Connections.Utils
    Parent: CAE.Connections.Folder


class FeEdgesLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    def GetFeEdges(self) -> typing.List[CAE.FEElemEdge]:
        ...
    def SetFeEdges(self, edges: typing.List[CAE.FEElemEdge]) -> None:
        ...


class ElementType(enum.Enum):
    None = 0
    EHex8 = 1
    EHex8Spider = 2
    E1d = 3
    E1DSpider = 4
    ESpider = 5
    EBushing = 6
    ESpring = 7
    EDamper = 8
    ERigid = 9
    EKinematic = 10
    ERigidConnector = 11
    ERigidRigidConnector = 12
    EInterpolationSpider = 13


class ElementStatusType(enum.Enum):
    Invalid = 0
    NotUpdated = 1
    Updated = 2


class ElementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Connections.Element]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, elementType: CAE.Connections.ElementType, name: str, connections: typing.List[CAE.Connections.IConnection]) -> CAE.Connections.Element:
        ...
    def Tag(self) -> Tag: ...



class Element(CAE.NamedPropertyTable):
    def __init__(self) -> None: ...
    def AddConnections(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def RemoveConnections(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def GetConnections(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def GenerateElements(self) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    IsCompatibleType: bool
    MinBarLength: Expression
    Status: CAE.Connections.ElementStatusType
    Type: CAE.Connections.ElementType


class DofType(enum.Enum):
    Free = 0
    Fixed = 1


class DofCombination(enum.Enum):
    UserDefined = 0
    Clamp = 1
    Spheric = 2
    Point = 3
    Slider = 4
    Pivot = 5
    SliderPivot = 6
    Cardan = 7


class Dof(enum.Enum):
    X = 0
    Y = 1
    Z = 2
    Rx = 3
    Ry = 4
    Rz = 5


class DiameterType(enum.Enum):
    User = 0
    Formula = 1
    TableFile = 2


class Damper(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    RxViscousDampingConstant: Expression
    RyViscousDampingConstant: Expression
    RzViscousDampingConstant: Expression
    XViscousDampingConstant: Expression
    YViscousDampingConstant: Expression
    ZViscousDampingConstant: Expression
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression


class CurveLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    Curve: IBaseCurve


class CsysType(enum.Enum):
    Existing = 0
    Predefined = 1
    Absolute = 2
    LocalCartesian = 3
    LocalCylindrical = 4
    LocalSpherical = 5


class CoordinatesSeriesLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    def GetCoordinates(self) -> typing.List[Point3d]:
        ...
    def SetCoordinates(self, coordinates: typing.List[Point3d]) -> None:
        ...


class CoordinatesLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    def GetCoordinates(self) -> Point3d:
        ...
    def SetCoordinates(self, coordinates: Point3d) -> None:
        ...


class ConnectionType(enum.Enum):
    SpotWeld = 0
    Adhesive = 1
    Bolt = 2
    Spring = 3
    Rigid = 4
    Bushing = 5
    Damper = 6
    Kinematic = 7
    SeamWeld = 8
    Sealing = 9


class ConnectionDBItemStiffnessType(enum.Enum):
    None = 0
    Rectangular = 1
    Spherical = 2
    Cylindrical = 3


class ConnectionDBItemData(TaggedObject):
    def __init__(self) -> None: ...
    Mass: float
    MaterialName: str
    Name: str
    ScrewDiameter: float
    StiffnessR: float
    StiffnessRR: float
    StiffnessRS: float
    StiffnessRX: float
    StiffnessRY: float
    StiffnessRZ: float
    StiffnessS: float
    StiffnessType: CAE.Connections.ConnectionDBItemStiffnessType
    StiffnessX: float
    StiffnessY: float
    StiffnessZ: float


class ConnectionDBData(TaggedObject):
    def __init__(self) -> None: ...
    def GetConnectionDBItemDatas(self) -> typing.List[CAE.Connections.ConnectionDBItemData]:
        ...
    def SetConnectionDBItemDatas(self, components: typing.List[CAE.Connections.ConnectionDBItemData]) -> None:
        ...


class ConnectionData(TaggedObject):
    def __init__(self) -> None: ...
    def GetPointNameCoord1(self) -> str:
        ...
    def SetPointNameCoord1(self, pointNameCoord1s: str) -> None:
        ...
    def GetPointNameCoord2(self) -> str:
        ...
    def SetPointNameCoord2(self, pointNameCoord2s: str) -> None:
        ...
    def GetPointNameCoord3(self) -> str:
        ...
    def SetPointNameCoord3(self, pointNameCoord3s: str) -> None:
        ...
    def GetPID1s(self) -> typing.List[TaggedObject]:
        ...
    def SetPID1s(self, pID1s: typing.List[TaggedObject]) -> None:
        ...
    def GetPID2s(self) -> typing.List[TaggedObject]:
        ...
    def SetPID2s(self, pID2s: typing.List[TaggedObject]) -> None:
        ...
    def GetPID3s(self) -> typing.List[TaggedObject]:
        ...
    def SetPID3s(self, pID3s: typing.List[TaggedObject]) -> None:
        ...
    def GetAxis(self) -> str:
        ...
    def SetAxis(self, axis: str) -> None:
        ...
    def GetLineFEEdgeRecipe1(self) -> str:
        ...
    def SetLineFEEdgeRecipe1(self, lineFEEdgeRecipe1s: str) -> None:
        ...
    def GetLineFEEdgeRecipe2(self) -> str:
        ...
    def SetLineFEEdgeRecipe2(self, lineFEEdgeRecipe2s: str) -> None:
        ...
    Comp1: CAE.Connections.ComponentData
    Comp2: CAE.Connections.ComponentData
    Comp3: CAE.Connections.ComponentData
    ConnectionType: CAE.Connections.ComposerConnectionType
    DBItem: CAE.Connections.ConnectionDBItemData
    Dof1: bool
    Dof2: bool
    Dof3: bool
    Dof4: bool
    Dof5: bool
    Dof6: bool
    ExpansionRadius1: float
    ExpansionRadius2: float
    ExpansionRadiusFactor1: float
    ExpansionRadiusFactor2: float
    FlangeSearchTolerance1: float
    FlangeSearchTolerance2: float
    FlangeType1: str
    FlangeType2: str
    HeadDiameter: float
    LengthStep: float
    LinePart1: str
    LinePart2: str
    MaximumDistanceTolerance1: float
    MaximumDistanceTolerance2: float
    Name: str
    SearchType1: str
    SearchType2: str
    ShankDiameter: float


class ComposerData(TaggedObject):
    def __init__(self) -> None: ...
    def GetComponents(self) -> typing.List[CAE.Connections.ComponentData]:
        ...
    def SetComponents(self, components: typing.List[CAE.Connections.ComponentData]) -> None:
        ...
    def GetConnections(self) -> typing.List[CAE.Connections.ConnectionData]:
        ...
    def SetConnections(self, connections: typing.List[CAE.Connections.ConnectionData]) -> None:
        ...
    AssemblyName: str
    InputFileDir: str
    MaterialDBDir: str
    OutputFileDir: str
    StartNumAxisSystems: int
    StartNumNodeAndElement: int
    StartNumProperties: int


class ComposerConnectionType(enum.Enum):
    Bolt = 0
    Spring = 1
    Latch = 2
    Bushing = 3
    BumpStop = 4
    Kinematic = 5
    WeatherStrip = 6
    SeamWeld = 7


class Composer(TaggedObject):
    def __init__(self) -> None: ...
    def ReadAssemblyDefinition(self, filePath: str) -> None:
        ...
    def WriteAssemblyDefinition(self, filePath: str) -> None:
        ...
    def ReadConnectionsDB(self, filePath: str) -> None:
        ...
    def GetMeshPartFromPID(self, pid: TaggedObject, meshParts: typing.List[TaggedObject]) -> None:
        ...
    def GetAxisFromAlias(self, axisAlias: str, axes: typing.List[CoordinateSystem]) -> None:
        ...
    def GetGroupFromAlias(self, axisAlias: str, groups: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    def CheckAssemblyConnections(self) -> str:
        ...
    def CheckAssemblyDocumentConnections(self) -> str:
        ...
    ComposerData: CAE.Connections.ComposerData
    ConnectionDBData: CAE.Connections.ConnectionDBData


class ComponentData(TaggedObject):
    def __init__(self) -> None: ...
    ComponentName: str
    ConnectionPointsPath: str
    FilePath: str
    IOSetPath: str
    MassPath: str
    MeshPath: str


class Bushing(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    RxStiffnessConstant: Expression
    RyStiffnessConstant: Expression
    RzStiffnessConstant: Expression
    XStiffnessConstant: Expression
    YStiffnessConstant: Expression
    ZStiffnessConstant: Expression
    RxStructuralDampingConstant: Expression
    RyStructuralDampingConstant: Expression
    RzStructuralDampingConstant: Expression
    XStructuralDampingConstant: Expression
    YStructuralDampingConstant: Expression
    ZStructuralDampingConstant: Expression
    RxViscousDampingConstant: Expression
    RyViscousDampingConstant: Expression
    RzViscousDampingConstant: Expression
    XViscousDampingConstant: Expression
    YViscousDampingConstant: Expression
    ZViscousDampingConstant: Expression
    RxStiffnessDynamic: Fields.ScalarFieldWrapper
    RyStiffnessDynamic: Fields.ScalarFieldWrapper
    RzStiffnessDynamic: Fields.ScalarFieldWrapper
    XStiffnessDynamic: Fields.ScalarFieldWrapper
    YStiffnessDynamic: Fields.ScalarFieldWrapper
    ZStiffnessDynamic: Fields.ScalarFieldWrapper
    RxViscousDampingDynamic: Fields.ScalarFieldWrapper
    RyViscousDampingDynamic: Fields.ScalarFieldWrapper
    RzViscousDampingDynamic: Fields.ScalarFieldWrapper
    XViscousDampingDynamic: Fields.ScalarFieldWrapper
    YViscousDampingDynamic: Fields.ScalarFieldWrapper
    ZViscousDampingDynamic: Fields.ScalarFieldWrapper
    RxStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RyStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RzStructuralDampingDynamic: Fields.ScalarFieldWrapper
    XStructuralDampingDynamic: Fields.ScalarFieldWrapper
    YStructuralDampingDynamic: Fields.ScalarFieldWrapper
    ZStructuralDampingDynamic: Fields.ScalarFieldWrapper
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression


class Bolt(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def IsInheritedMaterial(self) -> bool:
        ...
    def SetInheritedMaterial(self) -> None:
        ...
    def CanInheritMaterial(self) -> bool:
        ...
    def CanHaveNoMaterial(self) -> bool:
        ...
    def GetFlangeEntities(self, flangeIndex: int) -> typing.List[TaggedObject]:
        ...
    def AddFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def GetMaxNumberOfFlanges(self) -> int:
        ...
    def GetMinNumberOfFlanges(self) -> int:
        ...
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        ...
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        ...
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfDefinitions(self) -> int:
        ...
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        ...
    def GetSupportedDiameterTypes(self) -> typing.List[CAE.Connections.DiameterType]:
        ...
    def AddLocationCoordinatesWithDirectionCoordinates(self, indexOfDefinition: int, point: Point, direction: Point) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationCoordinatesWithDirectionVector(self, indexOfDefinition: int, masterPoint: Point, direction: Direction) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    HeadDiameter: Expression
    HeadDiameterCoefficient: Expression
    HeadDiameterType: CAE.Connections.HeadDiameterType
    MaxBoltLength: Expression
    Material: PhysicalMaterial
    NumberOfFlanges: int
    Coefficient: Expression
    Diameter: Expression
    DiameterType: CAE.Connections.DiameterType
    TableFile: str


class Adhesive(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def IsInheritedMaterial(self) -> bool:
        ...
    def SetInheritedMaterial(self) -> None:
        ...
    def CanInheritMaterial(self) -> bool:
        ...
    def CanHaveNoMaterial(self) -> bool:
        ...
    def GetSupportedHeightTypes(self) -> typing.List[CAE.Connections.HeightType]:
        ...
    def GetFlangeEntities(self, flangeIndex: int) -> typing.List[TaggedObject]:
        ...
    def AddFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveFlangeEntities(self, flangeIndex: int, entities: typing.List[TaggedObject]) -> None:
        ...
    def GetMaxNumberOfFlanges(self) -> int:
        ...
    def GetMinNumberOfFlanges(self) -> int:
        ...
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        ...
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        ...
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfDefinitions(self) -> int:
        ...
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        ...
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> Direction:
        ...
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: Direction) -> None:
        ...
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> Expression:
        ...
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: typing.List[CAE.FENode]) -> CAE.Connections.NodeSeriesLocation:
        ...
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: typing.List[Point]) -> CAE.Connections.PointSeriesLocation:
        ...
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: typing.List[Point3d]) -> CAE.Connections.CoordinatesSeriesLocation:
        ...
    def AddLocationCurve(self, indexOfDefinition: int, curve: IBaseCurve) -> CAE.Connections.CurveLocation:
        ...
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: typing.List[CAE.FEElemEdge]) -> CAE.Connections.FeEdgesLocation:
        ...
    Material: PhysicalMaterial
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    Height: Expression
    HeightType: CAE.Connections.HeightType
    NumberOfFlanges: int
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool
    Width: Expression


