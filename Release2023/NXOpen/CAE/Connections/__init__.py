from ....NXOpen import *
from ...CAE import *
from ..Connections import *

import typing
import enum

class Utils(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaeSession) -> None: ...
    def FilterConnectionsByType(self, iConnections: typing.List[CAE.Connections.IConnection], type: CAE.Connections.ConnectionType) -> typing.List[CAE.Connections.IConnection]:
        ...
    def GetInterchangeDataFromLumpedMass(self, conversionLengthUnit: Unit, conversionMassUnit: Unit, iConnections: typing.List[CAE.Connections.LumpedMass], iAbsoluteExportPath: str) -> typing.List[CAE.Connections.LMIEConnection]:
        ...
    def ExportLumpedMassInterchangeData(self, iConnections: typing.List[CAE.Connections.LMIEConnection], iAbsoluteExportPath: str, iConvertConnectionDataFromPartUnits: bool) -> None:
        ...
    def GetProjectionPoints(self, iConnections: typing.List[CAE.Connections.IConnection], oFlanges: typing.List[INXObject], oProjectionPoints: typing.List[Point3d], oFlangeObjectIndexList: int) -> None:
        ...
    def ImportLumpedMassInterchangeData(self, contextPart: INXObject, iAbsoluteImportPath: str) -> typing.List[CAE.Connections.LMIEConnection]:
        ...
    def CreateLmieconnection(self, contextPart: INXObject) -> CAE.Connections.LMIEConnection:
        ...
    def MapObject(self, femPart: CAE.FemPart, cadFeature: TaggedObject, syncGeomData: bool) -> TaggedObject:
        ...
    def ReimportMesh(self) -> None:
        ...
    def SplitWarpedQuads(self) -> None:
        ...
    def RelabelAfem(self) -> None:
        ...
    def GetNodeLabels(self, feModel: CAE.IFEModel, fromChildren: bool, labels: int) -> None:
        ...
    def GetElemLabels(self, feModel: CAE.IFEModel, fromChildren: bool, labels: int) -> None:
        ...
    def GetFreeEdgesFromElementCollectors(self, feModel: CAE.IFEModel, iElementCollectors: typing.List[CAE.Mesh], freeEdges: typing.List[CAE.FEElement]) -> None:
        ...
    def GetObjectAtProjectionOfLocation(self, iConnection: CAE.Connections.IConnection, locationIndex: int, coordinateIndex: int, flangeIndex: int) -> TaggedObject:
        ...
    def GetBoltSupportOfLocation(self, iBoltConnection: CAE.Connections.IConnection, locationIndex: int, coordinateIndex: int, boltSupportIndex: int) -> TaggedObject:
        ...
    def SearchNearestFlanges(self, iConnections: typing.List[CAE.Connections.IConnection], oNearestFlanges: typing.List[INXObject], oFlangeObjectIndices: int) -> None:
        ...
    def RelabelAfmOffsets(self, assyFemPart: CAE.AssyFemPart, nodeOffset: int, elemOffset: int, csysOffset: int, physOffset: int) -> None:
        ...
    def RelabelAFEMPhysicalProperty(self, assyFemPart: CAE.AssyFemPart) -> None:
        ...
    def GetBodyFromFeature(self, feature: Features.Feature, body: typing.List[Body]) -> None:
        ...
    def GetFeatureFromBody(self, body: Body) -> Features.Feature:
        ...
    def GetCoordinatesFromConstraintFile(self, constraintFilePath: str) -> typing.List[Point3d]:
        ...
    def WriteCoordinatesToConstraintFile(self, constraintFilePath: str, connectionName: str, coordinates: typing.List[Point3d]) -> None:
        ...
    def RemeshCompatibleConnectionComponents(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def Tag(self) -> Tag: ...



class UniversalConnectionState(enum.Enum):
    Unknown = 0
    Meshed = 1
    NotMeshed = 2
    Invalid = 3


class TargetDependencyType(enum.Enum):
    None = 0
    Dependent = 1
    Independent = 2


class StiffnessType(enum.Enum):
    PerElement = 0
    PerUnitLength = 1


class Spring(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedStiffnessTypes(self) -> typing.List[CAE.Connections.StiffnessType]:
        ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    RxStiffnessConstant: Expression
    RyStiffnessConstant: Expression
    RzStiffnessConstant: Expression
    StiffnessType: CAE.Connections.StiffnessType
    XStiffnessConstant: Expression
    YStiffnessConstant: Expression
    ZStiffnessConstant: Expression
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression
    Mass: Expression
    MassType: CAE.Connections.MassType
    IsMassOnBothTargets: bool


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
    def SetManualAdjustment(self, state: bool) -> None:
        ...
    def GetManualAdjustment(self) -> bool:
        ...
    def GetManualAdjustmentFactor(self) -> Expression:
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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
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
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool


class SmartTemplateTool(TaggedObject):
    def __init__(self) -> None: ...
    def Destroy(self) -> None:
        ...
    def ImportGroups(self, caePart: CAE.CaePart, iAbsoluteImportPath: str) -> typing.List[CAE.CaeGroup]:
        ...
    def ImportGroups(self, caePart: CAE.CaePart, iAbsoluteImportPath: str, selectedGroups: str) -> typing.List[CAE.CaeGroup]:
        ...
    def ExportPIDs(self, caePart: CAE.CaePart, iAbsoluteExportPath: str) -> None:
        ...
    def GetGroupPhysicalPropertyTables(self, caeGroup: CAE.CaeGroup) -> typing.List[CAE.PhysicalPropertyTable]:
        ...
    def ExportResults(self, pSimSolution: CAE.SimSolution, iAbsoluteExportPath: str) -> None:
        ...
    def ExportResultDataToExcel(self, pSimSolution: CAE.SimSolution, iAbsoluteExportPath: str, resultName: str, drivingPoints: bool, indexFile: str) -> None:
        ...
    def GetHardPointNameAndType(self, iAbsoluteFilePath: str, listOfHardPointTypes: typing.List[CAE.SelRecipeBaseStrategy.Type], listOfHardPointNames: str) -> None:
        ...


class SmartTemplateBuilder(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetSmartTemplateBuilder(self, owner: Session) -> CAE.Connections.SmartTemplateBuilder:
        ...
    def GetSmartTemplateTool(self) -> CAE.Connections.SmartTemplateTool:
        ...
    def Tag(self) -> Tag: ...



class ShankSegmentDiscretizationType(enum.Enum):
    None = 0
    SegmentLength = 1
    NumSegments = 2


class ShankLengthDiscretizationType(enum.Enum):
    None = 0
    UserDefined = 1
    PercentLength = 2
    PercentCurve = 3


class SelectionRecipeLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    SelectionRecipe: CAE.SelectionRecipe


class SeamWeldType(enum.Enum):
    WithMaterial = 0
    WithLaser = 1
    Resistance = 2
    Friction = 3
    Brazing = 4


class SeamWeldSide(enum.Enum):
    OnLargerSheetAngle = 0
    OnSmallerSheetAngle = 1
    OnBothSheetSides = 2


class SeamWeldShapeType(enum.Enum):
    Straight = 0
    Convex = 1
    Concave = 2


class SeamWeldSectionType(enum.Enum):
    I = 0
    V = 1
    U = 2
    X = 3
    Y = 4
    Hv = 5
    Hy = 6
    Fillet = 7
    Radius = 8


class SeamWeldNodeSelectionMethod(enum.Enum):
    ConnectionNodes = 0
    Specify = 1


class SeamWeldMcfType(enum.Enum):
    Other = 0
    YJoint = 1
    OverlapWeld = 2
    CornerWeld = 3
    ButtJoint = 4
    EdgeWeld = 5
    DoubleCornerWeld = 6
    CruciformJoint = 7
    KJoint = 8
    IWeld = 9
    SplitIWeld = 10


class SeamWeldMaterialType(enum.Enum):
    Angle = 0
    Overlap = 1
    Double = 2


class SeamWeldLocationType(enum.Enum):
    Vector = 0
    Flange1Side1 = 1
    Flange1Side2 = 2
    Flange2Side1 = 3
    Flange2Side2 = 4


class SeamWeld(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetMinMaxNumberOfWelds(self, minNumWelds: int, maxNumWelds: int) -> None:
        ...
    def GetNumberOfWelds(self) -> int:
        ...
    def SetNumberOfWelds(self, numWelds: int) -> None:
        ...
    def GetSeamWeldSectionType(self, weldIndex: int) -> CAE.Connections.SeamWeldSectionType:
        ...
    def SetSeamWeldSectionType(self, weldIndex: int, seamWeldSectionType: CAE.Connections.SeamWeldSectionType) -> None:
        ...
    def GetSeamWeldShapeType(self, weldIndex: int) -> CAE.Connections.SeamWeldShapeType:
        ...
    def SetSeamWeldShapeType(self, weldIndex: int, seamWeldShapeType: CAE.Connections.SeamWeldShapeType) -> None:
        ...
    def GetSeamWeldLocationType(self, weldIndex: int) -> CAE.Connections.SeamWeldLocationType:
        ...
    def SetSeamWeldLocationType(self, weldIndex: int, seamWeldLocationType: CAE.Connections.SeamWeldLocationType) -> None:
        ...
    def GetSeamWeldLocationParameter(self, weldIndex: int) -> float:
        ...
    def SetSeamWeldLocationParameter(self, weldIndex: int, locationParameter: float) -> None:
        ...
    def GetSeamWeldLocationVector(self, weldIndex: int) -> Direction:
        ...
    def SetSeamWeldLocationVector(self, weldIndex: int, locationVector: Direction) -> None:
        ...
    def GetSeamWeldMaterial(self, weldIndex: int) -> PhysicalMaterial:
        ...
    def SetSeamWeldMaterial(self, weldIndex: int, material: PhysicalMaterial) -> None:
        ...
    def GetWeldThickness(self, weldIndex: int) -> Expression:
        ...
    def GetWeldWidth(self, weldIndex: int) -> Expression:
        ...
    def GetWeldAngle(self, weldIndex: int) -> Expression:
        ...
    def GetWeldPenetration(self, weldIndex: int) -> Expression:
        ...
    def ConvertToVectorLocationType(self, weldIndex: int) -> None:
        ...
    def ConvertToFlangeSideLocationType(self, weldIndex: int) -> None:
        ...
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
    def GetFlangeGap(self, flangeIndex: int) -> Expression:
        ...
    def GetFlangeAngle(self, flangeIndex: int) -> Expression:
        ...
    def GetFlangeThickness(self, flangeIndex: int) -> Expression:
        ...
    def GetFlangeThicknessInherited(self, flangeIndex: int) -> bool:
        ...
    def SetFlangeThicknessInherited(self, flangeIndex: int, thicknessInherited: bool) -> None:
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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
        ...
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    SeamWeldMcfType: CAE.Connections.SeamWeldMcfType
    SeamWeldType: CAE.Connections.SeamWeldType
    Material: PhysicalMaterial
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    Height: Expression
    HeightType: CAE.Connections.HeightType
    NumberOfFlanges: int
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
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
    def GetSupportedStiffnessTypes(self) -> typing.List[CAE.Connections.StiffnessType]:
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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
        ...
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    WithOrientation: bool
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    NumberOfFlanges: int
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool
    RxStiffnessConstant: Expression
    RyStiffnessConstant: Expression
    RzStiffnessConstant: Expression
    StiffnessType: CAE.Connections.StiffnessType
    XStiffnessConstant: Expression
    YStiffnessConstant: Expression
    ZStiffnessConstant: Expression
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    Mass: Expression
    MassType: CAE.Connections.MassType


class Rivet(CAE.Connections.IConnection):
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
    def SetManualAdjustment(self, state: bool) -> None:
        ...
    def GetManualAdjustment(self) -> bool:
        ...
    def GetManualAdjustmentFactor(self) -> Expression:
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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
        ...
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> Direction:
        ...
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: Direction) -> None:
        ...
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> Expression:
        ...
    def GetJoinFeature(self, index: int, feature: Features.Feature, component: Assemblies.Component) -> None:
        ...
    def GetAllJoinFeatures(self, features: typing.List[Features.Feature], components: typing.List[Assemblies.Component]) -> None:
        ...
    def SetJoinData(self, features: typing.List[Features.Feature], components: typing.List[Assemblies.Component]) -> None:
        ...
    def AddJoinData(self, feature: Features.Feature, component: Assemblies.Component) -> None:
        ...
    def RemoveJoinData(self, feature: Features.Feature, component: Assemblies.Component) -> None:
        ...
    def RemoveJoinDataByIndex(self, index: int) -> None:
        ...
    def RemoveAllJoinData(self) -> None:
        ...
    def UnlinkJoinData(self) -> None:
        ...
    def GetNumberOfJoinData(self) -> int:
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
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool


class RingSearchType(enum.Enum):
    OneRing = 0
    TwoRings = 1
    ExpansionRadius = 2
    ExpansionRadiusFactor = 3


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


class PanelSearchType(enum.Enum):
    NearestSelectedPanel = 0
    AllSelectedPanels = 1


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
    LocalSpider = 4


class NodalTargetSpider(CAE.Connections.NodalTarget):
    def __init__(self) -> None: ...
    def GetLegsEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def IsCoincidentCenterTypeAllowed(self) -> bool:
        ...
    TargetCenter: TaggedObject
    CenterType: CAE.Connections.NodalTargetCenterType
    UseLegsCog: bool


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


class NodalTargetLocalSpider(CAE.Connections.NodalTarget):
    def __init__(self) -> None: ...
    def IsCoincidentCenterTypeAllowed(self) -> bool:
        ...
    def GetLocation(self, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfLocations(self) -> int:
        ...
    def RemoveLocation(self, indexOfLocation: int) -> None:
        ...
    def AddLocationNode(self, node: CAE.FENode) -> CAE.Connections.NodeLocation:
        ...
    def AddLocationPoint(self, point: Point) -> CAE.Connections.PointLocation:
        ...
    def AddLocationMeshPoint(self, meshPoint: CAE.MeshPoint) -> CAE.Connections.MeshPointLocation:
        ...
    def AddLocationSelectionRecipe(self, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    def GetRegionsEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddRegionsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveRegionsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    TargetCenter: TaggedObject
    CenterType: CAE.Connections.NodalTargetCenterType
    UseLegsCog: bool
    ExpansionRadius: Expression
    ExpansionRadiusFactor: Expression
    LocalSpiderCenterType: CAE.Connections.LocalSpiderCenterType
    MaxDistance: Expression
    PanelSearchType: CAE.Connections.PanelSearchType
    RingSearchType: CAE.Connections.RingSearchType
    SearchTolerance: Expression


class NodalTargetCenterType(enum.Enum):
    Manual = 0
    FromSpiderDefinition = 1
    Coincident = 2


class NodalTarget(NXObject):
    def __init__(self) -> None: ...
    TargetType: CAE.Connections.NodalTargetType


class NodalPairingMethod(enum.Enum):
    Proximity = 0
    OrientatedSearch = 1
    SelectionOrder = 2


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


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
    Friction = 12
    Contact = 13
    Mass = 14
    NonlinearStiffness = 15
    NonlinearDamping = 16


class ModelizationPPTRefTargetType(enum.Enum):
    None = 0
    Ec = 1
    Ecc = 2
    Ead = 3


class MeshPointLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    MeshPoint: CAE.MeshPoint


class MaterialType(enum.Enum):
    User = 0
    FromSupport = 1
    None = 2


class MassType(enum.Enum):
    OnNodes = 0
    WithSpiders = 1


class MassDistributionType(enum.Enum):
    Distributed = 0
    Repeated = 1


class MassConnectivityType(enum.Enum):
    NearestNodes = 0
    LocalSpiders = 1


class LumpedMass(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def GetPanels(self) -> typing.List[TaggedObject]:
        ...
    def AddPanels(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemovePanels(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def GetSupportEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddSupportEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveSupportEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def SetSupportEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    ExpansionRadiusFactorTolerance: Expression
    ExpansionRadiusTolerance: Expression
    MassConnectivityType: CAE.Connections.MassConnectivityType
    MaxDistanceTolerance: Expression
    PanelSearchDistance: Expression
    PanelSearchType: CAE.Connections.PanelSearchType
    RingSearchType: CAE.Connections.RingSearchType
    InertiaXX: Expression
    InertiaYX: Expression
    InertiaYY: Expression
    InertiaZX: Expression
    InertiaZY: Expression
    InertiaZZ: Expression
    Center: TaggedObject
    MassDistributionType: CAE.Connections.MassDistributionType
    UseCenterOfSlaveNodes: bool
    Mass: Expression
    MassType: CAE.Connections.MassType
    MassTypeValue: CAE.Connections.MassType


class LocationWithDir(CAE.Connections.Location):
    def __init__(self) -> None: ...
    DirectionPoint: Point
    DirectionType: CAE.Connections.LocationDirectionType
    DirectionValue: Vector3d
    DirectionVector: Direction
    EndSelectionRecipe: CAE.SelectionRecipe
    Point: Point
    StartSelectionRecipe: CAE.SelectionRecipe


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
    MeshPoint = 10
    Group = 11


class LocationDirectionType(enum.Enum):
    Point = 0
    Vector = 1
    Curve = 2
    SelectionRecipes = 3


class Location(TaggedObject):
    def __init__(self) -> None: ...
    def GetXyzCoordinates(self) -> typing.List[Point3d]:
        ...
    def GetDetails(self) -> str:
        ...
    def GetInfo(self) -> str:
        ...


class LocalSpiderCenterType(enum.Enum):
    MeanOfSpiderLegs = 0
    InputLegDefinition = 1


class LMIEUnitSystem(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    LengthUnit: str
    MassUnit: str


class LMIESelectionRecipe(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    RecipeName: str


class LMIERingOptions(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    ExpansionRadius: float
    ExpansionRadiusFactor: float
    RingType: CAE.Connections.RingSearchType


class LMIERegionSelection(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    def GetPids(self) -> typing.List[CAE.Connections.LMIEPid]:
        ...
    def SetPids(self, opt: typing.List[CAE.Connections.LMIEPid]) -> None:
        ...
    def CreatePid(self) -> CAE.Connections.LMIEPid:
        ...
    def GetSelectionRecipes(self) -> typing.List[CAE.Connections.LMIESelectionRecipe]:
        ...
    def SetSelectionRecipes(self, opt: typing.List[CAE.Connections.LMIESelectionRecipe]) -> None:
        ...
    def CreateSelectionRecipe(self) -> CAE.Connections.LMIESelectionRecipe:
        ...


class LMIEPoint(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    Coordinates: Point3d


class LMIEPid(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    Label: int


class LMIEPanelOptions(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    Distance: float
    SearchPanelsType: CAE.Connections.PanelSearchType


class LMIENode(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    Id: str


class LMIENearestNodes(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    def CreateRegionSelection(self) -> CAE.Connections.LMIERegionSelection:
        ...
    MaxSearchDistance: float
    RegionSelection: CAE.Connections.LMIERegionSelection


class LMIEMesh(TaggedObject):
    def __init__(self) -> None: ...


class LMIEMass(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    MassDistributionType: CAE.Connections.MassDistributionType
    MassType: CAE.Connections.MassType
    MassValue: float


class LMIELocalSpiders(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    def CreateRegionSelection(self) -> CAE.Connections.LMIERegionSelection:
        ...
    def CreateRingOptions(self) -> CAE.Connections.LMIERingOptions:
        ...
    def CreatePanelOptions(self) -> CAE.Connections.LMIEPanelOptions:
        ...
    MaxSearchDistance: float
    PanelOptions: CAE.Connections.LMIEPanelOptions
    RegionSelection: CAE.Connections.LMIERegionSelection
    RingOptions: CAE.Connections.LMIERingOptions


class LMIELegDefinition(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    def CreateNode(self) -> CAE.Connections.LMIENode:
        ...
    def CreatePoint(self) -> CAE.Connections.LMIEPoint:
        ...
    def CreateSelectionRecipe(self) -> CAE.Connections.LMIESelectionRecipe:
        ...
    Node: CAE.Connections.LMIENode
    Point: CAE.Connections.LMIEPoint
    SelectionRecipe: CAE.Connections.LMIESelectionRecipe


class LMIELegConnection(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    def CreateNearestNodes(self) -> CAE.Connections.LMIENearestNodes:
        ...
    def CreateLocalSpiders(self) -> CAE.Connections.LMIELocalSpiders:
        ...
    LegConnectionType: CAE.Connections.MassConnectivityType
    LocalSpiders: CAE.Connections.LMIELocalSpiders
    NearestNodes: CAE.Connections.LMIENearestNodes


class LMIEInertia(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    Ixx: float
    Iyx: float
    Iyy: float
    Izx: float
    Izy: float
    Izz: float


class LMIEError(NXObject):
    def __init__(self) -> None: ...
    def GetErrorMessages(self) -> str:
        ...
    def GetErrorCodes(self) -> str:
        ...
    def GetErrorValues(self, errorIndex: int) -> str:
        ...
    def HasErrors(self) -> bool:
        ...
    def GetWarningCodes(self) -> str:
        ...


class LMIEElementFace(TaggedObject):
    def __init__(self) -> None: ...
    FaceNumber: int
    Id: str


class LMIEElementEdge(TaggedObject):
    def __init__(self) -> None: ...
    EdgeNumber: int
    Id: str


class LMIEElement(TaggedObject):
    def __init__(self) -> None: ...
    Id: str


class LMIEConnection(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    def CreateMass(self) -> CAE.Connections.LMIEMass:
        ...
    def CreateLegConnection(self) -> CAE.Connections.LMIELegConnection:
        ...
    def CreateUnitSystem(self) -> CAE.Connections.LMIEUnitSystem:
        ...
    def CreateCenterDefinition(self) -> CAE.Connections.LMIECenterDefinition:
        ...
    def CreateInertia(self) -> CAE.Connections.LMIEInertia:
        ...
    def GetLegDefinitions(self) -> typing.List[CAE.Connections.LMIELegDefinition]:
        ...
    def SetLegDefinitions(self, opt: typing.List[CAE.Connections.LMIELegDefinition]) -> None:
        ...
    def CreateLegDefinition(self) -> CAE.Connections.LMIELegDefinition:
        ...
    CenterDefinition: CAE.Connections.LMIECenterDefinition
    ConnectionElementType: CAE.Connections.ElementType
    Description: str
    FolderName: str
    Id: int
    Inertia: CAE.Connections.LMIEInertia
    LegConnection: CAE.Connections.LMIELegConnection
    Mass: CAE.Connections.LMIEMass
    Plvc: str
    UnitSystem: CAE.Connections.LMIEUnitSystem


class LMIECenterDefinition(CAE.Connections.LMIEError):
    def __init__(self) -> None: ...
    def CreateNode(self) -> CAE.Connections.LMIENode:
        ...
    def CreatePoint(self) -> CAE.Connections.LMIEPoint:
        ...
    def CreateSelectionRecipe(self) -> CAE.Connections.LMIESelectionRecipe:
        ...
    Node: CAE.Connections.LMIENode
    Point: CAE.Connections.LMIEPoint
    SelectionRecipe: CAE.Connections.LMIESelectionRecipe
    UseCenterOfLegNodes: bool


class LMIEBody(TaggedObject):
    def __init__(self) -> None: ...


class Kinematic(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def GetDof(self, dof: CAE.Connections.Dof) -> CAE.Connections.DofType:
        ...
    def SetDof(self, dof: CAE.Connections.Dof, type: CAE.Connections.DofType) -> None:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType
    DofCombination: CAE.Connections.DofCombination
    CharacteristicLengthRadius: Expression
    FrictionCoefficient: Expression
    TighteningForce: Expression
    UseFriction: bool
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
    def GetSupportedStiffnessTypes(self) -> typing.List[CAE.Connections.StiffnessType]:
        ...
    RxStiffnessConstant: Expression
    RyStiffnessConstant: Expression
    RzStiffnessConstant: Expression
    StiffnessType: CAE.Connections.StiffnessType
    XStiffnessConstant: Expression
    YStiffnessConstant: Expression
    ZStiffnessConstant: Expression


class ISeamWeldFlangesContainer():
    def GetFlangeGap(self, flangeIndex: int) -> Expression:
        ...
    def GetFlangeAngle(self, flangeIndex: int) -> Expression:
        ...
    def GetFlangeThickness(self, flangeIndex: int) -> Expression:
        ...
    def GetFlangeThicknessInherited(self, flangeIndex: int) -> bool:
        ...
    def SetFlangeThicknessInherited(self, flangeIndex: int, thicknessInherited: bool) -> None:
        ...


class INonlinearStiffness():
    RxNonlinearStiffness: Fields.ScalarFieldWrapper
    RyNonlinearStiffness: Fields.ScalarFieldWrapper
    RzNonlinearStiffness: Fields.ScalarFieldWrapper
    XNonlinearStiffness: Fields.ScalarFieldWrapper
    YNonlinearStiffness: Fields.ScalarFieldWrapper
    ZNonlinearStiffness: Fields.ScalarFieldWrapper


class INonlinearDamping():
    RxNonlinearDamping: Fields.ScalarFieldWrapper
    RyNonlinearDamping: Fields.ScalarFieldWrapper
    RzNonlinearDamping: Fields.ScalarFieldWrapper
    XNonlinearDamping: Fields.ScalarFieldWrapper
    YNonlinearDamping: Fields.ScalarFieldWrapper
    ZNonlinearDamping: Fields.ScalarFieldWrapper


class INonlinearCylindricalStiffness():
    RNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper
    RrNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper
    RzNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper
    ZNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper


class INonlinearCylindricalDamping():
    RNonlinearCylindricalDamping: Fields.ScalarFieldWrapper
    RrNonlinearCylindricalDamping: Fields.ScalarFieldWrapper
    RzNonlinearCylindricalDamping: Fields.ScalarFieldWrapper
    ZNonlinearCylindricalDamping: Fields.ScalarFieldWrapper


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


class INodalTargetLocalSpiderDefinition():
    def GetLocation(self, indexOfLocation: int) -> CAE.Connections.Location:
        ...
    def GetNumberOfLocations(self) -> int:
        ...
    def RemoveLocation(self, indexOfLocation: int) -> None:
        ...
    def AddLocationNode(self, node: CAE.FENode) -> CAE.Connections.NodeLocation:
        ...
    def AddLocationPoint(self, point: Point) -> CAE.Connections.PointLocation:
        ...
    def AddLocationMeshPoint(self, meshPoint: CAE.MeshPoint) -> CAE.Connections.MeshPointLocation:
        ...
    def AddLocationSelectionRecipe(self, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    def GetRegionsEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddRegionsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveRegionsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    ExpansionRadius: Expression
    ExpansionRadiusFactor: Expression
    LocalSpiderCenterType: CAE.Connections.LocalSpiderCenterType
    MaxDistance: Expression
    PanelSearchType: CAE.Connections.PanelSearchType
    RingSearchType: CAE.Connections.RingSearchType
    SearchTolerance: Expression


class INodalTargetLegs():
    def GetLegsEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveLegsEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...


class INodalTargetCenterOption():
    def IsCoincidentCenterTypeAllowed(self) -> bool:
        ...
    CenterType: CAE.Connections.NodalTargetCenterType
    UseLegsCog: bool


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


class IMassType():
    MassTypeValue: CAE.Connections.MassType


class IMassTarget():
    def GetSupportEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddSupportEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemoveSupportEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def SetSupportEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    Center: TaggedObject
    MassDistributionType: CAE.Connections.MassDistributionType
    UseCenterOfSlaveNodes: bool


class IMassPhysicalParams():
    Mass: Expression
    MassType: CAE.Connections.MassType


class IMassInertia():
    InertiaXX: Expression
    InertiaYX: Expression
    InertiaYY: Expression
    InertiaZX: Expression
    InertiaZY: Expression
    InertiaZZ: Expression


class IMassConnectivity():
    def GetPanels(self) -> typing.List[TaggedObject]:
        ...
    def AddPanels(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def RemovePanels(self, entities: typing.List[TaggedObject]) -> None:
        ...
    ExpansionRadiusFactorTolerance: Expression
    ExpansionRadiusTolerance: Expression
    MassConnectivityType: CAE.Connections.MassConnectivityType
    MaxDistanceTolerance: Expression
    PanelSearchDistance: Expression
    PanelSearchType: CAE.Connections.PanelSearchType
    RingSearchType: CAE.Connections.RingSearchType


class IMassBothTargets():
    IsMassOnBothTargets: bool


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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
        ...


class ILocationsWithDirContainer():
    def AddLocationCoordinatesWithDirectionCoordinates(self, indexOfDefinition: int, point: Point, direction: Point) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationCoordinatesWithDirectionVector(self, indexOfDefinition: int, masterPoint: Point, direction: Direction) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationCoordinatesWithDirectionSelectionRecipes(self, indexOfDefinition: int, startSelectionRecipe: CAE.SelectionRecipe, endSelectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.LocationWithDir:
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
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool


class IJoinDataContainer():
    def GetJoinFeature(self, index: int, feature: Features.Feature, component: Assemblies.Component) -> None:
        ...
    def GetAllJoinFeatures(self, features: typing.List[Features.Feature], components: typing.List[Assemblies.Component]) -> None:
        ...
    def SetJoinData(self, features: typing.List[Features.Feature], components: typing.List[Assemblies.Component]) -> None:
        ...
    def AddJoinData(self, feature: Features.Feature, component: Assemblies.Component) -> None:
        ...
    def RemoveJoinData(self, feature: Features.Feature, component: Assemblies.Component) -> None:
        ...
    def RemoveJoinDataByIndex(self, index: int) -> None:
        ...
    def RemoveAllJoinData(self) -> None:
        ...
    def UnlinkJoinData(self) -> None:
        ...
    def GetNumberOfJoinData(self) -> int:
        ...


class IHeight():
    def GetSupportedHeightTypes(self) -> typing.List[CAE.Connections.HeightType]:
        ...
    Height: Expression
    HeightType: CAE.Connections.HeightType


class IFriction():
    CharacteristicLengthRadius: Expression
    FrictionCoefficient: Expression
    TighteningForce: Expression
    UseFriction: bool


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
    def SetManualAdjustment(self, state: bool) -> None:
        ...
    def GetManualAdjustment(self) -> bool:
        ...
    def GetManualAdjustmentFactor(self) -> Expression:
        ...
    Coefficient: Expression
    Diameter: Expression
    DiameterType: CAE.Connections.DiameterType
    TableFile: str


class ICylindricalViscousDampingDynamic():
    RCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper
    RrCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper
    RzCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper
    ZCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper


class ICylindricalViscousDamping():
    RCylindricalViscousDampingConstant: Expression
    RrCylindricalViscousDampingConstant: Expression
    RzCylindricalViscousDampingConstant: Expression
    ZCylindricalViscousDampingConstant: Expression


class ICylindricalStructuralDampingDynamic():
    RCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RrCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RzCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper
    ZCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper


class ICylindricalStructuralDamping():
    RCylindricalStructuralDampingConstant: Expression
    RrCylindricalStructuralDampingConstant: Expression
    RzCylindricalStructuralDampingConstant: Expression
    ZCylindricalStructuralDampingConstant: Expression


class ICylindricalStiffnessDynamic():
    RCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper
    RrCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper
    RzCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper
    ZCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper


class ICylindricalStiffness():
    RCylindricalStiffnessConstant: Expression
    RrCylindricalStiffnessConstant: Expression
    RzCylindricalStiffnessConstant: Expression
    ZCylindricalStiffnessConstant: Expression


class ICsys():
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType


class IConnection(DisplayableObject):
    def __init__(self) -> None: ...
    HasConnectionElement: bool
    State: CAE.Connections.UniversalConnectionState
    UserDescription: str


class IBushingType():
    BushingType: CAE.Connections.BushingType


class HeightType(enum.Enum):
    Undefined = -1
    User = 0
    MeanOfFlangesThickness = 1
    DistanceBetweenFlanges = 2
    DistanceBetweenFlangesMeanOfFlangesThickness = 3
    DistanceBetweenFlangesMaxOfFlangesThickness = 4
    DistanceBetweenFlangesAndMeanOfFlangesThickness = 5


class HeadDiameterType(enum.Enum):
    User = 0
    FactorOfDiameter = 1


class GroupLocation(CAE.Connections.Location):
    def __init__(self) -> None: ...
    Group: CAE.CaeGroup


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
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.Connections.Folder.MoveConnectionsToThisFolder instead.")"""
        ...
    def MoveConnectionsToThisFolder(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def ImportSpotWeldFromWcd(self, file: str, inputFileUnit: Unit) -> typing.List[CAE.Connections.SpotWeld]:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.Connections.Folder.ImportSpotWeldFromWcdWithHeight instead.")"""
        ...
    def ImportConnectionsFromMcf(self, file: str, inputFileUnit: Unit) -> typing.List[CAE.Connections.IConnection]:
        ...
    def CreateConnection(self, type: CAE.Connections.ConnectionType, name: str) -> CAE.Connections.IConnection:
        ...
    def ImportLumpedMassFromInterchangeData(self, lengthUnit: Unit, massUnit: Unit, reportErrors: bool, iConnections: typing.List[CAE.Connections.LMIEConnection]) -> typing.List[CAE.Connections.LumpedMass]:
        ...
    def ImportConnectionsFromXMcf(self, propertyList: CAE.CaeDataContainer) -> typing.List[CAE.Connections.IConnection]:
        ...
    def ExportConnectionsToXMcf(self, connections: typing.List[CAE.Connections.IConnection], propertyList: CAE.CaeDataContainer) -> None:
        ...
    def DetectConnections(self, propertyList: CAE.CaeDataContainer) -> typing.List[CAE.Connections.IConnection]:
        ...
    def DeleteObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def ImportSpotWeldFromWcdWithHeight(self, file: str, inputFileUnit: Unit, heightType: CAE.Connections.HeightType, heightValue: float) -> typing.List[CAE.Connections.SpotWeld]:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.CAE.Connections.Folder.ImportSpotWeldFromWcdWithHeightAndMaterial instead.")"""
        ...
    def ImportSpotWeldFromWcdWithHeightAndMaterial(self, file: str, inputFileUnit: Unit, heightType: CAE.Connections.HeightType, heightValue: float, useInputFileMaterial: bool, userDefinedMaterialType: CAE.Connections.MaterialType, userDefinedMaterial: PhysicalMaterial) -> typing.List[CAE.Connections.SpotWeld]:
        ...
    def CreateSpotWeldConnectionFromWcdFile(self, file: str, matfile: str, pDbData: CAE.Connections.ConnectionDBItemData) -> typing.List[CAE.Connections.SpotWeld]:
        ...
    def ExportSpotWeldConnectionsToWcdFile(self, filePath: str, outputLength: Unit, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
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
    EMassRigidSpider = 14
    EMassInterpolationSpider = 15
    EScalarSpringRigidSpider = 16
    EScalarSpringRigidInterpolationSpider = 17
    EJoint = 18
    EJointInterpolation = 19
    EBeamRigidSpider = 20
    EBar = 21
    EBarInterpolationSpider = 22
    ECbear2Fou3InterpolationSpider = 23
    ECbear2RigidSpider = 24
    ECbush2RigidSpider = 25
    EBeamSpider = 26
    ECbush2Fou3InterpolationSpider = 27
    EConstrainedJointMPCSpider = 28
    EMassFou3InterpolationSpider = 29
    EFou3InterpolationSpider = 30
    EBeam = 31
    ECWeld = 32


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
    def Create(self, elementType: CAE.Connections.ElementType, connectionType: CAE.Connections.ConnectionType, name: str) -> CAE.Connections.Element:
        ...
    def Tag(self) -> Tag: ...



class Element(NXObject):
    def __init__(self) -> None: ...
    def AddConnections(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def RemoveConnections(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def GetConnections(self, connections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def GenerateElements(self) -> None:
        ...
    def MarkAsModifiedByPropertyTable(self) -> None:
        ...
    def GetNodeGroups(self, groups: typing.List[CAE.CaeGroup]) -> None:
        ...
    def SetNodeGroups(self, groups: typing.List[CAE.CaeGroup]) -> None:
        ...
    def GetNodes(self, nodes: typing.List[CAE.FENode]) -> None:
        ...
    def SetNodes(self, nodes: typing.List[CAE.FENode]) -> None:
        ...
    def GetElementGroups(self, groups: typing.List[CAE.CaeGroup]) -> None:
        ...
    def SetElementGroups(self, groups: typing.List[CAE.CaeGroup]) -> None:
        ...
    def GetElements(self, elems: typing.List[CAE.FEElement]) -> None:
        ...
    def SetElements(self, elems: typing.List[CAE.FEElement]) -> None:
        ...
    def GetGeneratedElementsOfConnectionAtLocation(self, connection: CAE.Connections.IConnection, indexOfLocation: int, indexOfDefinitionInLocation: int, elems: typing.List[CAE.FEElement]) -> None:
        ...
    def GetGeneratedElementsOfConnection(self, connection: CAE.Connections.IConnection, elems: typing.List[CAE.FEElement]) -> None:
        ...
    def GetGeneratedNodesOfConnection(self, connection: CAE.Connections.IConnection, nodes: typing.List[CAE.FENode]) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    IsCompatibleType: bool
    Manual: bool
    MinBarLength: Expression
    NodeSelectionMethod: CAE.Connections.SeamWeldNodeSelectionMethod
    PropertyTable: CAE.PropertyTable
    Status: CAE.Connections.ElementStatusType
    Type: CAE.Connections.ElementType


class DofType(enum.Enum):
    Free = 0
    Fixed = 1


class DofCombination(enum.Enum):
    UserDefined = 0
    Fixed = 1
    Spherical = 2
    Inplane = 3
    Slider = 4
    Revolute = 5
    Cylindrical = 6
    Universal = 7
    SliderUniversal = 8
    Inline = 9


class Dof(enum.Enum):
    X = 0
    Y = 1
    Z = 2
    Rx = 3
    Ry = 4
    Rz = 5


class DiscretizationMethod(enum.Enum):
    StepLength = 0
    NumberOfPoints = 1


class DiameterType(enum.Enum):
    User = 0
    Formula = 1
    TableFile = 2
    FlangeHoleDetection = 3


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


class Crimp(CAE.Connections.IConnection):
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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
        ...
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    Material: PhysicalMaterial
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    Height: Expression
    HeightType: CAE.Connections.HeightType
    NumberOfFlanges: int
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool
    Width: Expression


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
    Rivet = 10
    LumpedMass = 11
    Clinch = 12
    Crimp = 13
    Bar = 14
    Bearing = 15


class ConnectionDBItemStiffnessType(enum.Enum):
    None = 0
    Rectangular = 1
    Spherical = 2
    Cylindrical = 3


class ConnectionDBItemData(TaggedObject):
    def __init__(self) -> None: ...
    def GetDofs(self) -> int:
        ...
    AdhesiveWidth: float
    Height: float
    HeightType: CAE.Connections.HeightType
    Mass: float
    MaterialID: int
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
    def GetPID1s(self) -> int:
        ...
    def SetPID1s(self, pID1s: int) -> None:
        ...
    def GetPID2s(self) -> int:
        ...
    def SetPID2s(self, pID2s: int) -> None:
        ...
    def GetPID3s(self) -> int:
        ...
    def SetPID3s(self, pID3s: int) -> None:
        ...
    def GetAxis(self) -> str:
        ...
    def SetAxis(self, axis: str) -> None:
        ...
    def GetInvalidDOF(self) -> int:
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
    DBItem: str
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
    WCDFile: str


class ComposerTool(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetComposerTool(self, owner: Session) -> CAE.Connections.ComposerTool:
        ...
    def CreateComposer(self) -> CAE.Connections.Composer:
        ...
    def Tag(self) -> Tag: ...



class ComposerData(TaggedObject):
    def __init__(self) -> None: ...
    def CreateComponent(self) -> CAE.Connections.ComponentData:
        ...
    def GetComponents(self) -> typing.List[CAE.Connections.ComponentData]:
        ...
    def SetComponents(self, components: typing.List[CAE.Connections.ComponentData]) -> None:
        ...
    def CreateConnection(self) -> CAE.Connections.ConnectionData:
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
    Adhesive = 8
    SpotWeld = 9
    Bar = 10


class Composer(TaggedObject):
    def __init__(self) -> None: ...
    def CreateComposerData(self) -> CAE.Connections.ComposerData:
        ...
    def ReadAssemblyDefinition(self, filePath: str) -> None:
        ...
    def WriteAssemblyDefinition(self, filePath: str) -> None:
        ...
    def ReadConnectionsDB(self, filePath: str) -> None:
        ...
    def GetMeshPartFromPID(self, pid: int, meshParts: typing.List[TaggedObject]) -> None:
        ...
    def GetAxisFromAlias(self, axisAlias: str, axes: typing.List[CoordinateSystem]) -> None:
        ...
    def CheckAssemblyConnections(self) -> str:
        ...
    def CheckAssemblyDocumentConnections(self, documentName: str) -> str:
        ...
    def SearchPIDs(self, documentName: str, isAssemblyOpen: bool, listOfConnPIDsResults: str, listOfMassPIDsResults: str) -> None:
        ...
    def GetMaterialsData(self, inputBdfFilePath: str) -> str:
        ...
    def SearchBoltComponentAndPIDs(self, documentName: str, listOfConnPIDsResults: str) -> None:
        ...
    def GetLumpedMassData(self) -> typing.List[CAE.Connections.LMIEConnection]:
        ...
    def SetLumpedMassData(self, iConnections: typing.List[CAE.Connections.LMIEConnection]) -> None:
        ...
    def Destroy(self) -> None:
        ...
    def ImportHardPointFromXml(self, tWorkPart: CAE.CaePart, file: str, isUpdate: bool) -> typing.List[CAE.SelectionRecipe]:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.Connections.Composer.ImportAndUpdateHardPointFromXml instead.")"""
        ...
    def ExportHardPointToXml(self, tWorkPart: CAE.CaePart, tUnit: Unit, file: str) -> None:
        ...
    def MigrateToHardPointFile(self, file: str) -> None:
        ...
    def ImportAndModifyHardPointLabel(self, tWorkPart: CAE.CaePart, file: str) -> typing.List[CAE.SelectionRecipe]:
        ...
    def GetMeshPartInContextFromPID(self, tWorkPart: CAE.CaePart, pid: int, meshParts: typing.List[TaggedObject]) -> None:
        ...
    def ImportAndUpdateHardPointFromXml(self, tWorkPart: CAE.CaePart, file: str, isUpdate: bool, selrecipes: typing.List[CAE.SelectionRecipe], updatedSelrecipes: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    ComposerData: CAE.Connections.ComposerData
    ConnectionDBData: CAE.Connections.ConnectionDBData


class ComponentData(TaggedObject):
    def __init__(self) -> None: ...
    ComponentName: str
    ConnectionPointsPath: str
    FilePath: str
    ImportedConnectionPointsPath: str
    MassPath: str
    MeshPath: str


class Clinch(CAE.Connections.IConnection):
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
    def SetManualAdjustment(self, state: bool) -> None:
        ...
    def GetManualAdjustment(self) -> bool:
        ...
    def GetManualAdjustmentFactor(self) -> Expression:
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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
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
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool


class BushingType(enum.Enum):
    Rectangular = 0
    Cylindrical = 1


class Bushing(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    def GetSupportedStiffnessTypes(self) -> typing.List[CAE.Connections.StiffnessType]:
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
    StiffnessType: CAE.Connections.StiffnessType
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
    RCylindricalStiffnessConstant: Expression
    RrCylindricalStiffnessConstant: Expression
    RzCylindricalStiffnessConstant: Expression
    ZCylindricalStiffnessConstant: Expression
    RCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper
    RrCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper
    RzCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper
    ZCylindricalStiffnessDynamic: Fields.ScalarFieldWrapper
    BushingType: CAE.Connections.BushingType
    RCylindricalStructuralDampingConstant: Expression
    RrCylindricalStructuralDampingConstant: Expression
    RzCylindricalStructuralDampingConstant: Expression
    ZCylindricalStructuralDampingConstant: Expression
    RCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RrCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RzCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper
    ZCylindricalStructuralDampingDynamic: Fields.ScalarFieldWrapper
    RCylindricalViscousDampingConstant: Expression
    RrCylindricalViscousDampingConstant: Expression
    RzCylindricalViscousDampingConstant: Expression
    ZCylindricalViscousDampingConstant: Expression
    RCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper
    RrCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper
    RzCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper
    ZCylindricalViscousDampingDynamic: Fields.ScalarFieldWrapper
    Mass: Expression
    MassType: CAE.Connections.MassType
    RxNonlinearStiffness: Fields.ScalarFieldWrapper
    RyNonlinearStiffness: Fields.ScalarFieldWrapper
    RzNonlinearStiffness: Fields.ScalarFieldWrapper
    XNonlinearStiffness: Fields.ScalarFieldWrapper
    YNonlinearStiffness: Fields.ScalarFieldWrapper
    ZNonlinearStiffness: Fields.ScalarFieldWrapper
    RNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper
    RrNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper
    RzNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper
    ZNonlinearCylindricalStiffness: Fields.ScalarFieldWrapper
    RxNonlinearDamping: Fields.ScalarFieldWrapper
    RyNonlinearDamping: Fields.ScalarFieldWrapper
    RzNonlinearDamping: Fields.ScalarFieldWrapper
    XNonlinearDamping: Fields.ScalarFieldWrapper
    YNonlinearDamping: Fields.ScalarFieldWrapper
    ZNonlinearDamping: Fields.ScalarFieldWrapper
    RNonlinearCylindricalDamping: Fields.ScalarFieldWrapper
    RrNonlinearCylindricalDamping: Fields.ScalarFieldWrapper
    RzNonlinearCylindricalDamping: Fields.ScalarFieldWrapper
    ZNonlinearCylindricalDamping: Fields.ScalarFieldWrapper
    IsMassOnBothTargets: bool


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
    def SetManualAdjustment(self, state: bool) -> None:
        ...
    def GetManualAdjustment(self) -> bool:
        ...
    def GetManualAdjustmentFactor(self) -> Expression:
        ...
    def AddLocationCoordinatesWithDirectionCoordinates(self, indexOfDefinition: int, point: Point, direction: Point) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationCoordinatesWithDirectionVector(self, indexOfDefinition: int, masterPoint: Point, direction: Direction) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationCoordinatesWithDirectionSelectionRecipes(self, indexOfDefinition: int, startSelectionRecipe: CAE.SelectionRecipe, endSelectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.LocationWithDir:
        ...
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    HeadDiameter: Expression
    HeadDiameterCoefficient: Expression
    HeadDiameterType: CAE.Connections.HeadDiameterType
    LimitCurveLength: bool
    LimitLocationEndpointsLength: bool
    MaxBoltLength: Expression
    ShankLengthDiscretizationType: CAE.Connections.ShankLengthDiscretizationType
    ShankLengthPercentage: Expression
    ShankLengthUser: Expression
    UseMasterPointAsCenter: bool
    Material: PhysicalMaterial
    NumberOfFlanges: int
    Coefficient: Expression
    Diameter: Expression
    DiameterType: CAE.Connections.DiameterType
    TableFile: str


class Bearing(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    def GetSupportedCsysTypes(self) -> typing.List[CAE.Connections.CsysType]:
        ...
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression
    Csys: CoordinateSystem
    CsysType: CAE.Connections.CsysType


class Bar(CAE.Connections.IConnection):
    def __init__(self) -> None: ...
    def GetSupportedDiameterTypes(self) -> typing.List[CAE.Connections.DiameterType]:
        ...
    def SetManualAdjustment(self, state: bool) -> None:
        ...
    def GetManualAdjustment(self) -> bool:
        ...
    def GetManualAdjustmentFactor(self) -> Expression:
        ...
    def IsInheritedMaterial(self) -> bool:
        ...
    def SetInheritedMaterial(self) -> None:
        ...
    def CanInheritMaterial(self) -> bool:
        ...
    def CanHaveNoMaterial(self) -> bool:
        ...
    def SetTargetType(self, index: int, type: CAE.Connections.NodalTargetType) -> None:
        ...
    def GetTarget(self, index: int) -> CAE.Connections.NodalTarget:
        ...
    Coefficient: Expression
    Diameter: Expression
    DiameterType: CAE.Connections.DiameterType
    TableFile: str
    Material: PhysicalMaterial
    PairingMethod: CAE.Connections.NodalPairingMethod
    SearchConeAngle: Expression
    SearchOrientation: Direction
    SearchRange: Expression


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
    def AddLocationGroup(self, indexOfDefinition: int, group: CAE.CaeGroup) -> CAE.Connections.GroupLocation:
        ...
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: CAE.SelectionRecipe) -> CAE.Connections.SelectionRecipeLocation:
        ...
    Material: PhysicalMaterial
    MaxAngleBetweenNormals: Expression
    MaxDistCGToElemCG: Expression
    MaxNormalDistCGToFlanges: Expression
    ProjectTolerance: Expression
    Height: Expression
    HeightType: CAE.Connections.HeightType
    NumberOfFlanges: int
    DiscretizationMethod: CAE.Connections.DiscretizationMethod
    DistanceFromStart: Expression
    DistanceToEnd: Expression
    LengthStep: Expression
    MaxLengthStep: Expression
    NumberOfDiscretizationPoints: int
    UseMaxLengthStep: bool
    UseOriginalNodesOfConnection: bool
    Width: Expression


