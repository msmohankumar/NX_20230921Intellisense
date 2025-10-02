from . import GeneralArrangement
from ....NXOpen import *
from ...Features import *
from ..ShipDesign import *

import typing
import enum

class ZFrameBuilder(Features.ShipDesign.TransFrameBuilder):
    def __init__(self) -> None: ...


class YFrameBuilder(Features.ShipDesign.TransFrameBuilder):
    def __init__(self) -> None: ...


class WeldCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CoordSystem: CoordinateSystem
    KeepCoordSystem: bool
    KeepSelectCSYSFace: bool
    KeepSelectGuideCurve: bool
    KeepSelectTargetFace: bool
    PlacementType: Features.ShipDesign.WeldCutBuilder.CreationMethod
    SelectCSYSFace: SelectFace
    SelectGuideCurve: SelectTaggedObject
    SelectTargetFace: SelectFace
    SketchBlock: SketchExpressionModifierBuilder
    WeldLocation: Point


    class CreationMethod(enum.Enum):
        Corner = 0
        AlongGuide = 1
        SpecifyCSYS = 2
    

class WeldCut2Builder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CSYSTargetFace: SelectFace
    CoordinateSystem: CoordinateSystem
    CornerPoint: Point
    CornerTargetFace: SelectFace
    CurveTargetFace: SelectFace
    DistanceTolerance: float
    GuideCurve: SelectTaggedObject
    PlacementType: Features.ShipDesign.WeldCut2Builder.CreationMethod
    Spreadsheet: Features.ShipDesign.SteelFeatureSpreadsheetBuilder


    class CreationMethod(enum.Enum):
        Corner = 0
        AlongGuide = 1
        SpecifyCSYS = 2
    

class WeldCut2(Features.BodyFeature):
    def __init__(self) -> None: ...


class WeldCut(Features.BodyFeature):
    def __init__(self) -> None: ...


class WeightAndCGBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFrameParts(self, frameParts: typing.List[Part]) -> None:
        ...
    SelectionMethod: Features.ShipDesign.WeightAndCGBuilder.SelectionMethods
    VolumeBody: SelectBody


    class SelectionMethods(enum.Enum):
        Volume = 0
        Frame = 1
    

class VerifyPenetrationBuilder(Builder):
    def __init__(self) -> None: ...
    RoutingObjectCollector: SelectNXObjectList
    SelectionType: Features.ShipDesign.VerifyPenetrationBuilder.SelectionDialogType
    StructurePartCollector: SelectNXObjectList


    class SelectionDialogType(enum.Enum):
        StructureForRequest = 0
        RouteForRequest = 1
        StructureForVerify = 2
        RouteForVerify = 4
        CutoutForRequest = 8
    

class VentilationHoles2Builder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngularDimOffset: Expression
    EnumSpacing: Features.ShipDesign.VentilationHoles2Builder.ArraySpacing
    GuideOffset: Expression
    IntNumVents: int
    OnPathEndOffset: GeometricUtilities.OnPathDimensionBuilder
    OnPathStartOffset: GeometricUtilities.OnPathDimensionBuilder
    SectionGuide: Section
    SelectEndTrim: SelectTaggedObject
    SelectStartTrim: SelectTaggedObject
    SelectTargetFace: SelectTaggedObjectList
    SketchBlock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    ToggleSymmetricOffsets: bool
    VentSpacing: Expression


    class ArraySpacing(enum.Enum):
        EvenDistribution = 0
        CustomDefined = 1
    

class VentilationHoles2(Features.BodyFeature):
    def __init__(self) -> None: ...


class VentHolesMarkingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    GridPlanes: SelectDatumPlaneList
    TabNoteGroup: Features.TabNoteCfgBuilder


class VentHolesMarking(Features.BodyFeature):
    def __init__(self) -> None: ...


class ValidateModelBuilder(Builder):
    def __init__(self) -> None: ...
    CheckCircularReference: bool
    CheckKnuckleStiffener: bool
    CheckPlateIntersectedPlate: bool
    CheckPlateIntersectedStiffener: bool
    CheckStiffenerIntersectedStiffener: bool
    CheckThickenPlate: bool
    CreateTransientStructures: bool
    SelectPart: Features.ShipDesign.SelectPartBuilder


class UpdateShipLibraryBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AssemblyOptions: Features.ShipDesign.UpdateShipLibraryBuilder.ShipLibAssemblyOption
    FileBrowser: str
    ShipLibType: Features.ShipDesign.UpdateShipLibraryBuilder.ShipLibOptionType


    class ShipLibOptionType(enum.Enum):
        Profile = 0
        Belt = 1
        Cutout = 2
        Endcut = 3
        Support = 4
        SupportCap = 5
        WeldOnEdge = 6
        Bracket = 7
        WeldAlongEdge = 8
    

    class ShipLibAssemblyOption(enum.Enum):
        WorkPart = 0
        WorkPartandComponents = 1
        WorkPartandComponentswithLibraries = 2
    

class UpdateShipLibrary(Features.BodyFeature):
    def __init__(self) -> None: ...


class UpdateProjectBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCandidatePMI(self, pmi: typing.List[Annotations.PmiNote]) -> None:
        ...
    PMIEquipment: bool
    PMIRoom: bool
    RoomColor: bool
    RoomThickness: bool


class UnfoldedMinRecBuilder(Builder):
    def __init__(self) -> None: ...
    SelectionObjects: SelectDisplayableObjectList


class TransverseBulkheadBuilder(Features.ShipDesign.PlateSystemBuilder):
    def __init__(self) -> None: ...
    MoldFacePlaneList: Features.ShipDesign.PlaneListBuilderList
    MoldFacePlanes: SelectDatumPlaneList
    MoldFaceSheet: SelectBody
    Type: Features.ShipDesign.TransverseBulkheadBuilder.Types


    class Types(enum.Enum):
        SheetBody = 0
        Planes = 1
    

class TransverseBulkhead(Features.BodyFeature):
    def __init__(self) -> None: ...


class TransitionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSectionBlockParts(self, sectionParts: str) -> None:
        ...
    def SetFrameParts(self, framePartFilenames: str) -> None:
        ...
    def DryRun(self) -> None:
        ...
    SectionMappingFile: str
    SelectPart: Features.ShipDesign.SelectPartBuilder
    TransitionMethod: Features.ShipDesign.TransitionBuilder.TransitionMethods
    TransitionType: Features.ShipDesign.TransitionBuilder.TransitionTypes


    class TransitionTypes(enum.Enum):
        Section = 0
        Frame = 1
    

    class TransitionMethods(enum.Enum):
        UpdateExisting = 0
        CreateNew = 1
    

class TransFrameListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.TransFrameListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.TransFrameListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.TransFrameListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.TransFrameListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.TransFrameListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.TransFrameListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.TransFrameListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.TransFrameListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.TransFrameListItemBuilder, object2: Features.ShipDesign.TransFrameListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.TransFrameListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TransFrameListItemBuilder(NXObject):
    def __init__(self) -> None: ...
    EndFrame: int
    FrameSpacing: Expression


class TransFrameBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateTransFrameListItem(self) -> Features.ShipDesign.TransFrameListItemBuilder:
        ...
    AttribName: str
    AttribRef: str
    FeatureNameSuffix: str
    FrameFeatureType: Features.ShipDesign.TransFrameBuilder.FrameFeatureTypes
    NegateFrame: int
    TransFrameNegList: Features.ShipDesign.TransFrameListItemBuilderList
    TransFramePosList: Features.ShipDesign.TransFrameListItemBuilderList


    class FrameFeatureTypes(enum.Enum):
        Insert = -1
        Transverse = 0
        LongitudnalY = 1
        LongitudnalZ = 2
    

class TransFrame(Features.BodyFeature):
    def __init__(self) -> None: ...


class TraceLinesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    CurveCount: int
    DatumPlanes: SelectDisplayableObjectList
    Direction: bool
    EndCurve: Section
    Offset: Expression
    OffsetCurveCount: int
    OffsetType: Features.ShipDesign.TraceLinesBuilder.TraceLineType
    PlacementFace: ScCollector
    ReferenceCurve: Section
    StartCurve: Section


    class TraceLineType(enum.Enum):
        EqualSpacing = 0
        Offset = 1
    

class TraceLines(Features.CurveFeature):
    def __init__(self) -> None: ...


class ThicknessDirectionBuilder(Builder):
    def __init__(self) -> None: ...
    ThicknessDirection: Features.ShipDesign.ThicknessDirectionBuilder.ThicknessDirectionType
    ThicknessDirectionOnReference: Features.ShipDesign.ThicknessDirectionBuilder.ThicknessDirectionType


    class ThicknessDirectionType(enum.Enum):
        FwdPortInUp = 0
        AftStbdOutDn = 1
        Ctr = 2
        PortToInCtr = 3
        StbdFrOutCtr = 4
    

class SynchronizeDesignViewBuilder(Builder):
    def __init__(self) -> None: ...
    def SynchronizeDesignView(self) -> int:
        ...
    DesignElementToSynchronizeDesignView: SelectNXObjectList


class SubSystemsBuilder(Features.ShipDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    Seams: SelectNXObjectList
    SubPillarDefinitionList: Features.ShipDesign.SubSystemBuilderList
    SubPlateDefinitionList: Features.ShipDesign.SubSystemBuilderList
    SubProfileDefinitionList: Features.ShipDesign.SubSystemBuilderList


    class Types(enum.Enum):
        Plate = 0
        Profile = 1
        Pillar = 2
    

class SubSystems(Features.BodyFeature):
    def __init__(self) -> None: ...


class SubSystemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.SubSystemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.SubSystemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.SubSystemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.SubSystemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SubSystemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SubSystemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.SubSystemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.SubSystemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.SubSystemBuilder, object2: Features.ShipDesign.SubSystemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.SubSystemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SubSystemBuilder(Features.ShipDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    EndCutEnd: Features.ShipDesign.StiffenerSystemBuilder.EndCutTypes
    EndCutStart: Features.ShipDesign.StiffenerSystemBuilder.EndCutTypes
    EndEndCut: Features.ShipDesign.EndCutBuilder
    EndEndCutChanged: bool
    EndPillarTreatment: Features.ShipDesign.PillarTreatmentBlockBuilder
    MountingMethod: Features.ShipDesign.StiffenerSystemBuilder.MountingMethods
    Name: str
    Offset: Expression
    OrientationAngle: Expression
    OrientationLinePillar: SelectCurve
    OrientationMethod: Features.ShipDesign.StiffenerSystemBuilder.OrientationMethods
    OrientationVector: Direction
    PillarStockData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    PlateStockData: Features.ShipDesign.PlateStockBuilder
    ProfileStockData: Features.ShipDesign.StiffenerStockBuilder
    Reverse: bool
    StartEndCut: Features.ShipDesign.EndCutBuilder
    StartEndCutChanged: bool
    StartPillarTreatment: Features.ShipDesign.PillarTreatmentBlockBuilder
    SubSystem: SelectNXObjectList
    Tightness: int


class SubAssemblyDrawingBuilder(Builder):
    def __init__(self) -> None: ...
    def InitializeContainer(self) -> None:
        ...
    AllLeaves: bool
    DrawingTemplate: Features.ShipDesign.DrawingTemplateBuilder
    EditMode: bool
    Scale: float
    SubAssemblyContainerPart: SelectDisplayableObject
    ViewCount: int


class StiffenerSystemBuilder(Features.ShipDesign.ProfileSystemBuilder):
    def __init__(self) -> None: ...
    def CreatePlanePairBuilder(self) -> Features.ShipDesign.PlanePairBuilder:
        ...
    def GetStiffenerBySupportBoundaryAttachedPlate(self, boundary: Body) -> Body:
        ...
    ApplyFlangeSetback: bool
    ApplyWebSetback: bool
    BuildSolid: bool
    ConnectAngle: float
    CreateSeamsAtKnuckles: bool
    Curves: Section
    EndCutEnd: Features.ShipDesign.StiffenerSystemBuilder.EndCutTypes
    EndCutStart: Features.ShipDesign.StiffenerSystemBuilder.EndCutTypes
    EndEndCut: Features.ShipDesign.EndCutBuilder
    KnuckleLocationTolerance: float
    MeasureAlongMode: Features.ShipDesign.StiffenerSystemBuilder.MeasureAlongModes
    MountingMethod: Features.ShipDesign.StiffenerSystemBuilder.MountingMethods
    OffsetDistance: Expression
    OffsetDistanceEnd: Expression
    OffsetDistanceStart: Expression
    OffsetNumber: int
    OffsetPlane: Plane
    OffsetSpacing: Expression
    OffsetSpacingEnd: Expression
    OffsetSpacingMode: Features.ShipDesign.StiffenerSystemBuilder.OffsetSpacingModes
    OffsetSpacingStart: Expression
    OrientationAngle: Expression
    OrientationDefinitionBuilder: Features.ShipDesign.OrientationDefinitionBuilder
    OrientationMethod: Features.ShipDesign.StiffenerSystemBuilder.OrientationMethods
    OrientationVector: Direction
    PlaneList: Features.ShipDesign.PlaneListBuilderList
    PlanePairList: NXObjectList
    Planes: SelectNXObjectList
    PointList: NXObjectList
    PointMethod: Features.ShipDesign.StiffenerSystemBuilder.PointMethods
    ProjectionDirection: GeometricUtilities.ProjectionOptions
    Reverse: bool
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    ShipStructure: SelectNXObjectList
    StartEndCut: Features.ShipDesign.EndCutBuilder
    StiffenerBySupportPathData: Features.ShipDesign.StiffenerBySupportPathBuilder
    StockData: Features.ShipDesign.StiffenerStockBuilder
    SwitchSide: bool
    Type: Features.ShipDesign.StiffenerSystemBuilder.Types
    Weld: Weld.CharacteristicsBuilder


    class Types(enum.Enum):
        Curves = 0
        Planes = 1
        OffsetPlanes = 2
        Points = 3
        BySupport = 4
    

    class PointMethods(enum.Enum):
        Planes = 0
        Points = 1
    

    class OrientationMethods(enum.Enum):
        FaceNormal = 0
        Vector = 1
    

    class OffsetSpacingModes(enum.Enum):
        Single = 0
        Double = 1
    

    class MountingMethods(enum.Enum):
        NoOffset = 0
        AlongWeb = 1
        FaceNormal = 2
    

    class MeasureAlongModes(enum.Enum):
        AlongSurfaceLength = 0
        NormaltoPlane = 1
        AlongSurfaceChord = 2
    

    class EndCutTypes(enum.Enum):
        Connected = 0
        FlangeFree = 1
        Sniped = 2
        SnipedSquare = 3
        None = 4
    

class StiffenerSystem(Features.CurveFeature):
    def __init__(self) -> None: ...


class StiffenerStockBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def PopulateAnchorPointList(self) -> None:
        ...
    def GetAvailableAnchorPointNames(self) -> str:
        ...
    def Validate(self) -> bool:
        ...
    AnchorPoint: int
    BuiltUpStockData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    PlateHeight: Expression
    PlateStockData: Features.ShipDesign.PlateStockBuilder
    ProfileStockData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    SectionType: Features.ShipDesign.StiffenerStockBuilder.StockSectionType


    class StockSectionType(enum.Enum):
        Profile = 0
        Plate = 1
        BuiltUp = 2
    

class StiffenerLimitBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    LimitGeometry: SelectDisplayableObject
    LimitMethod: Features.ShipDesign.StiffenerLimitBuilder.LimitType
    LimitValue: Expression
    SquareCutClearance: Expression


    class LimitType(enum.Enum):
        Value = 0
        SquareCut = 1
        NeatTrim = 2
        Boundary = 3
    

class StiffenerBySupportPathBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def ClearBoundaryToAttachedBoundaryMap(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Angle: Expression
    EndBoundary: SelectDisplayableObject
    LengthAlignMethod: Features.ShipDesign.StiffenerBySupportPathBuilder.AlignedTo
    LengthParams: Expression
    MultipleSelectionEndBoundary: SelectDisplayableObjectList
    OrientationBySupport: bool
    RefParallelLine: SelectNXObject
    SetbackMethod: Features.ShipDesign.StiffenerBySupportPathBuilder.SetBackMethod
    SetbackMethods: Features.ShipDesign.StiffenerBySupportPathBuilder.SetBackOption
    StartBoundary: SelectDisplayableObjectList
    StiffenerBySupportMethod: Features.ShipDesign.StiffenerBySupportPathBuilder.Method
    SwitchSide: bool
    ThroughPointLocation: Point


    class SetBackOption(enum.Enum):
        BoundingStiffenerHeight = 0
        SbsWebThickness = 1
    

    class SetBackMethod(enum.Enum):
        BoundingStiffenerHeight = 0
        SBSWebThickeness = 1
    

    class Scenario(enum.Enum):
        BasicDesign = 0
        DetailDesign = 1
    

    class Method(enum.Enum):
        AlignedBoundary = 0
        AlignedLength = 1
        BoundToBound = 2
        ParallelToLine = 3
        Horizontal = 4
        Vertical = 5
        NormalToCurve = 6
        ThroughPoint = 7
    

    class AlignedTo(enum.Enum):
        Web = 0
        Flange = 1
    

class StiffenerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetShowMigratedBody(self) -> bool:
        ...
    def SetShowMigratedBody(self, showMigratedBody: bool) -> None:
        ...
    def CreatePath(self, curves: typing.List[NXObject], faces: typing.List[DisplayableObject]) -> None:
        ...
    def DestroyPath(self, curves: typing.List[NXObject]) -> None:
        ...
    def GetStiffenerBySupportBoundaryAttachedPlate(self, boundary: Body) -> Body:
        ...
    AddNeatTrim: bool
    AdoptionAnchorPointList: NXObjectList
    AdoptionBaseFaces: ScCollector
    AdoptionBodies: SelectTaggedObjectList
    AdoptionEndCutFaces1: ScCollector
    AdoptionEndCutFaces2: ScCollector
    AdoptionMoldFaces: ScCollector
    AdoptionOpposingMoldFaces: ScCollector
    AdoptionTopFaces: ScCollector
    AngularTolerance: float
    ApplyFlangeSetback: bool
    ApplyWebSetback: bool
    AttachmentPlate: SelectDisplayableObject
    AttachmentPlateOption: Features.ShipDesign.StiffenerBuilder.AttachmentOption
    ConnectAngle: float
    DistanceTolerance: float
    EdgeReinforcementAlignment: Features.ShipDesign.StiffenerBuilder.EdgeReinforcementAlignmentMethod
    EdgeReinforcementPlacementMethod: Features.ShipDesign.StiffenerBuilder.EdgeReinforcementPlacementMethods
    EndCutType: Features.ShipDesign.StiffenerBuilder.EndCutTypes
    EndEndCut: Features.ShipDesign.EndCutBuilder
    EndLimit: Features.ShipDesign.StiffenerLimitBuilder
    FaceOffset: Expression
    FaceReverseDirection: bool
    IncludeRelief: bool
    KnuckleOption: Features.ShipDesign.StiffenerBuilder.KnuckleOptions
    MountingAngle: Expression
    MountingMethod: Features.ShipDesign.StiffenerBuilder.MountingMethods
    OrientCsys: Features.SelectDatumCsysList
    OrientType: Features.ShipDesign.StiffenerBuilder.OrientationMethod
    OrientVector: Direction
    OrientationAngleRule: Features.ShipDesign.FeatureParmsBuilder.OrientationAngleRuleTypes
    OrientationDefinitionBuilder: Features.ShipDesign.OrientationDefinitionBuilder
    PathGeometry: SelectTaggedObjectList
    PathOffset: Expression
    PathReverseDirection: bool
    PlacementGeometry: SelectDisplayableObjectList
    ReferenceDirection: Vector3d
    ReferencePoint: Point3d
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    StartEndCut: Features.ShipDesign.EndCutBuilder
    StartLimit: Features.ShipDesign.StiffenerLimitBuilder
    StiffenerBySupportPathData: Features.ShipDesign.StiffenerBySupportPathBuilder
    StockData: Features.ShipDesign.StiffenerStockBuilder
    Type: Features.ShipDesign.StiffenerBuilder.Types


    class Types(enum.Enum):
        Stiffener = 0
        EdgeReinforcement = 1
        AdoptStiffener = 2
        AdoptEdgeReinforcement = 3
        StiffenerBySupport = 4
    

    class OrientationMethod(enum.Enum):
        FaceNormal = 0
        Vector = 1
        DatumCSYS = 2
    

    class MountingMethods(enum.Enum):
        NoOffset = 0
        AlongWeb = 1
        FaceNormal = 2
    

    class KnuckleOptions(enum.Enum):
        None = 0
        Split = 1
        Bend = 2
    

    class EndCutTypes(enum.Enum):
        None = 0
        Symmetric = 1
        TwoSided = 2
    

    class EdgeReinforcementPlacementMethods(enum.Enum):
        OnEdge = 0
        OnFace = 1
    

    class EdgeReinforcementAlignmentMethod(enum.Enum):
        Center = 0
        GuideEdge = 1
        OppositeGuide = 2
    

    class AttachmentOption(enum.Enum):
        Inferred = 0
        Override = 1
    

class Stiffener(Features.BodyFeature):
    def __init__(self) -> None: ...


class SteelVentHolesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngularDim: Expression
    GuideOffset: Expression
    KeepReverseGuideOffset: bool
    KeepSectionGuide: bool
    KeepSelectEndTrim: bool
    KeepSelectStartTrim: bool
    KeepSelectTargetFace: bool
    NumVents: int
    OnPathEndOffset: GeometricUtilities.OnPathDimensionBuilder
    OnPathStartOffset: GeometricUtilities.OnPathDimensionBuilder
    ReverseGuideOffset: bool
    SectionGuide: Section
    SelectEndTrim: SelectTaggedObject
    SelectStartTrim: SelectTaggedObject
    SelectTargetFace: SelectTaggedObjectList
    SketchBlock: SketchExpressionModifierBuilder
    ToggleEqualSpacing: bool
    ToggleSymmetricOffset: bool
    VentSpacing: Expression


class SteelVentHoles(Features.BodyFeature):
    def __init__(self) -> None: ...


class SteelSupportBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetAvailableSupportTypes(self) -> str:
        ...
    def GetAvailableSupportSizes(self) -> str:
        ...
    def GetAvailableCapTypes(self) -> str:
        ...
    def GetAvailableStartCapSizes(self) -> str:
        ...
    def GetAvailableEndCapSizes(self) -> str:
        ...
    def GetAvailableAttributeNames(self) -> str:
        ...
    def GetAvailableAttributeMaterials(self) -> str:
        ...
    AngularDim: Expression
    AttributeMaterial: int
    AttributeName: int
    CoordSystem: CoordinateSystem
    EndCapSize: int
    EndCapThickness: Expression
    EndCapType: int
    EndOffset: Expression
    EndPlane: Plane
    KeepCoordSystem: bool
    KeepEndPlane: bool
    KeepReverseEndOffset: bool
    KeepReverseLine1Offset: bool
    KeepReverseLine2Offset: bool
    KeepReverseStartOffset: bool
    KeepSelectGuideCurve: bool
    KeepSelectLine1: bool
    KeepSelectLine2: bool
    KeepSelectOrientationLine: bool
    KeepStartPlane: bool
    Line1Offset: Expression
    Line2Offset: Expression
    PlacementMethod: Features.ShipDesign.SteelSupportBuilder.CreationMethod
    ReverseEndOffset: bool
    ReverseLine1Offset: bool
    ReverseLine2Offset: bool
    ReverseStartOffset: bool
    SelectGuideCurve: SelectTaggedObject
    SelectLine1: SelectTaggedObject
    SelectLine2: SelectTaggedObject
    SelectOrientationLine: SelectTaggedObject
    StartCapSize: int
    StartCapThickness: Expression
    StartCapType: int
    StartOffset: Expression
    StartPlane: Plane
    SupportCapOptions: Features.ShipDesign.SteelSupportBuilder.CapOptions
    SupportSize: int
    SupportType: int


    class CreationMethod(enum.Enum):
        TwoPlanesandLines = 0
        SpecifyLine = 1
        SpecifyCsys = 2
    

    class CapOptions(enum.Enum):
        None = 0
        TwoSided = 1
        Symmetric = 2
    

class SteelSupport(Features.BodyFeature):
    def __init__(self) -> None: ...


class SteelInsulationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateSteelInsulationBoundary(self) -> Features.ShipDesign.SteelInsulationBoundaryBuilder:
        ...
    BoundaryList: Features.ShipDesign.SteelInsulationBoundaryBuilderList
    DistanceTolerance: float
    EnableBoundaryAdjustment: bool
    InsulateProfile: bool
    InsulationHeight: Expression
    MaterialType: int
    SteelFaces: ScCollector
    ThickenDirection: bool
    Thickness: Expression


class SteelInsulationBoundaryBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.SteelInsulationBoundaryBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.SteelInsulationBoundaryBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.SteelInsulationBoundaryBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.SteelInsulationBoundaryBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SteelInsulationBoundaryBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SteelInsulationBoundaryBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.SteelInsulationBoundaryBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.SteelInsulationBoundaryBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.SteelInsulationBoundaryBuilder, object2: Features.ShipDesign.SteelInsulationBoundaryBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.SteelInsulationBoundaryBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SteelInsulationBoundaryBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateOffsetExpressions(self) -> None:
        ...
    def GetOffsetExpressions(self) -> typing.List[Expression]:
        ...
    def Validate(self) -> bool:
        ...
    Boundaries: SelectNXObjectList


class SteelInsulation(Features.BodyFeature):
    def __init__(self) -> None: ...


class SteelFeatureSpreadsheetBuilder(Builder):
    def __init__(self) -> None: ...
    def SetContextEntity(self, contextEntity: TaggedObject) -> None:
        ...
    def SetPossibleContextAttributeCount(self, possibleContextAttributeCount: int) -> None:
        ...
    def SetPossibleContextAttribute(self, possibleContextAttributeIndex: int, possibleContextAttribute: str) -> None:
        ...
    def SetSectionType(self, strSectionType: str) -> None:
        ...
    def SetSectionSubType1(self, strSectionType: str) -> None:
        ...
    def SetSectionSubType2(self, strSectionType: str) -> None:
        ...
    def SetsDefaultTypesFromContext(self) -> None:
        ...
    def ImportSketch(self) -> None:
        ...
    def GetImportedSketches(self) -> typing.List[Features.Feature]:
        ...
    def EditPrimaryParameter(self, parameterName: str, parameterValue: str) -> None:
        ...
    def EditParameter(self, parameterName: str, parameterValue: str) -> None:
        ...
    def GetParameterValues(self) -> typing.List[Tooling.SpreadsheetDataParameter]:
        ...
    def GetSpreadsheetData(self) -> Tooling.SpreadsheetData:
        ...
    def SetSpreadsheetData(self, pKRUData: Tooling.SpreadsheetData) -> None:
        ...
    def ResetBuilderData(self) -> None:
        ...
    def CacheSpreadsheetData(self) -> None:
        ...
    def UpdateSpreadsheetData(self, paramNames: str, paramValues: str) -> None:
        ...
    def SetSpreadsheetDataStatus(self, paramNames: str, paramStatus: int) -> None:
        ...
    def RestoreSpreadsheetData(self) -> None:
        ...
    def GetAvailableSectionTypes(self) -> str:
        ...
    def SetRuleInputs(self, inputNames: str, inputValues: str) -> None:
        ...
    def UpdateParametersUsingRules(self) -> None:
        ...
    def DeleteImportedSketch(self) -> None:
        ...
    SectionType: int
    SteelFeatureType: str


class SteelDistributionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AssemblyPart: str
    Description: str
    FeatureName: str
    Form: Features.ShipDesign.SteelDistributionBuilder.SaForm
    ItemType: str
    Material: Features.ShipDesign.SteelDistributionBuilder.SaMaterial
    Name: Features.ShipDesign.SteelDistributionBuilder.SaName
    SaProject: str
    SectionNumber: str
    Size: Features.ShipDesign.SteelDistributionBuilder.SaSize
    SteelBodies: SelectBodyList
    SubComponent: bool
    TemplateCategoryName: str
    TemplateName: str
    Type: Features.ShipDesign.SteelDistributionBuilder.SaType


    class SaType(enum.Enum):
        FirstValue = 0
    

    class SaSize(enum.Enum):
        FirstValue = 0
    

    class SaName(enum.Enum):
        FirstValue = 0
    

    class SaMaterial(enum.Enum):
        FirstValue = 0
    

    class SaForm(enum.Enum):
        FirstValue = 0
    

class SteelDistribution(Features.BodyFeature):
    def __init__(self) -> None: ...


class SteelCollarPlateBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetAvailablePlateSizes(self) -> str:
        ...
    IsInternal: bool
    KeepSelectFace: bool
    KeepSelectProfileBody: bool
    PlateSize: int
    SelectFace: SelectFace
    SelectProfileBody: SelectBody


class SteelCollarPlate(Features.BodyFeature):
    def __init__(self) -> None: ...


class StandardPartSCAssist(Features.Feature):
    def __init__(self) -> None: ...


class StandardPartItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.StandardPartItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.StandardPartItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.StandardPartItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.StandardPartItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.StandardPartItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.StandardPartItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.StandardPartItemBuilder, object2: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class StandardPartItemBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateReferences(self, bToUpdateGeometry: bool) -> None:
        ...
    def LookupRegistration(self) -> str:
        ...
    def SetOptionalGeometry(self, selectedGeometry: DisplayableObject) -> None:
        ...
    def CheckScallopSize(self) -> bool:
        ...
    def ResetItem(self) -> None:
        ...
    def SetTransitionGeometry(self, index: int, transitionGeometry: DisplayableObject) -> None:
        ...
    def ConvertReferenceGeometry(self, index: int, selObj: DisplayableObject) -> None:
        ...
    def AddAcrossObject(self, acrossObject: DisplayableObject) -> None:
        ...
    def RemoveAcrossObject(self, acrossObject: DisplayableObject) -> None:
        ...
    def AddDeselectedAcrossObject(self, acrossObject: DisplayableObject) -> None:
        ...
    def RemoveDeselectedAcrossObject(self, acrossObject: DisplayableObject) -> None:
        ...
    FifthObject: SelectDisplayableObject
    FirstAdoptionCurve: ScCollector
    FirstChainInstallDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    FirstChainObject: ScCollector
    FirstObject: SelectDisplayableObject
    FirstPlane: SelectDisplayableObject
    FourthObject: SelectDisplayableObject
    InstallFifthDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    InstallFirstDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    InstallFourthDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    InstallSecondDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    InstallThirdDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    SecondAdoptionCurve: ScCollector
    SecondChainInstallDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    SecondChainObject: ScCollector
    SecondObject: SelectDisplayableObject
    SecondPlane: SelectDisplayableObject
    ThirdObject: SelectDisplayableObject


    class Direction(enum.Enum):
        Fore = 0
        Aft = 1
        Up = 2
        Down = 3
        Port = 4
        Starboard = 5
        In = 6
        Out = 7
        Center = 8
    

class StandardPartFrameworkBuilder(Builder):
    def __init__(self) -> None: ...
    def SetView(self) -> None:
        ...
    def GetStandardPartName(self, bFullName: bool) -> str:
        ...
    def GetModelFile(self) -> str:
        ...
    def GetDataFile(self, updateConfiguration: bool) -> None:
        ...
    def ModifySpreadsheetData(self, strParamName: str, strParamValue: str) -> None:
        ...
    def UpdateSpreadsheetData(self, strParamName: str, strParamValue: str, pnParamStatus: int) -> None:
        ...
    def UpdateModel(self) -> None:
        ...
    def AddStandardPart(self) -> None:
        ...
    def RunSmartRule(self, pItemBuilder: Features.ShipDesign.StandardPartItemBuilder, stage: Features.ShipDesign.StandardPartFrameworkBuilder.SmartRuleStage, ppStrParamName: str, ppStrParamValue: str, ppStrParamDescription: str) -> None:
        ...
    def CheckSpreadsheetInput(self, pItemBuilder: Features.ShipDesign.StandardPartItemBuilder, ppStrParamName: str, ppStrParamValue: str) -> None:
        ...
    def EndRunSmartRule(self, pItemBuilder: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def ApplySmartRuleResult(self, pStrParamName: str, pStrParamValue: str) -> None:
        ...
    def RemoveInstance(self, itemBuilder: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def FlipThicknessDirection(self, bUpdateModel: bool) -> None:
        """[Obsolete("Deprecated in NX8.0.3.  Use NXOpen.Features.ShipDesign.StandardPartFrameworkBuilder.ModifySpreadSheetData() instead.")"""
        ...
    def CreateStandardPartItem(self, refBuilder: Features.ShipDesign.StandardPartItemBuilder) -> Features.ShipDesign.StandardPartItemBuilder:
        ...
    def PostUpdate(self) -> None:
        ...
    def ResetRuleInputCache(self) -> None:
        ...
    def CheckInterference(self) -> None:
        ...
    def ResetPartIndex(self) -> None:
        ...
    def SetCurrentStandardPartItem(self, pCurItemBuilder: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def UpdateThicknessDirection(self, bUpdateModel: bool) -> None:
        ...
    def UpdateSpreadsheetDataNoUpdate(self, strParamName: str, strParamValue: str, pnParamStatus: int) -> None:
        ...
    def CopyFromWeldCharacteristics(self, stdPartItemBuilder: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def CopyToWeldCharacteristics(self, stdPartItemBuilder: Features.ShipDesign.StandardPartItemBuilder) -> None:
        ...
    def SetStandardPartVersion(self, standardPartVersion: float) -> None:
        ...
    def UpdateShipNames(self, shipNamesType: Features.ShipDesign.ShipnamesBuilderType) -> None:
        ...
    ConfigAttribute: str
    FirstCompartment: str
    ManufacturingStock: Features.ShipDesign.ManufacturingStockBuilder
    PartCategory: str
    PartCreationType: Features.ShipDesign.StandardPartFrameworkBuilder.CreationType
    PartSubType: str
    PartType: str
    SecondCompartment: str
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    StandardPartGroupOption: bool
    StandardPartItem: Features.ShipDesign.StandardPartItemBuilder
    StandardPartList: Features.ShipDesign.StandardPartItemBuilderList
    Thickness: Expression
    ThicknessDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    WeldCharacteristics: Weld.CharacteristicsBuilder


    class SmartRuleStage(enum.Enum):
        PreUpdate = 0
        PostUpdate = 1
    

    class CreationType(enum.Enum):
        Creation = 0
        Adoption = 1
    

class StandardPart(Features.CurveFeature):
    def __init__(self) -> None: ...


class StabilityBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPartOperationBuilder(self, partOperationBuilder: PDM.PartOperationCreateBuilder) -> None:
        ...
    AftPerpendicular: Expression
    CreateNewItem: bool
    DesignDraught: Expression
    Distance: Expression
    ExportNativeFilename: str
    ForwardPerpendicular: Expression
    FreshWaterDensity: Expression
    GZCurve: bool
    Hull: SelectBodyList
    InitialGravityCenterX: Expression
    InitialGravityCenterY: Expression
    InitialGravityCenterZ: Expression
    Level: Features.ShipDesign.StabilityBuilder.LevelType
    MaxDraught: Expression
    MinDraught: Expression
    NumberOfSteps: int
    SeaWaterDensity: Expression
    SingleDraught: Expression
    Subdivision: Features.ShipDesign.StabilityBuilder.SubdivisionType
    ThicknessFactor: Expression


    class SubdivisionType(enum.Enum):
        Distance = 0
        NumberOfSteps = 1
    

    class LevelType(enum.Enum):
        MultipleLevels = 0
        SingleLevel = 1
    

class SplitStandardPartBuilder(Builder):
    def __init__(self) -> None: ...
    def ConvertObjectsToAdd(self, selectedObjectTags: typing.List[DisplayableObject]) -> None:
        ...
    def ConvertObjectsToRemove(self, selectedObjectTags: typing.List[DisplayableObject]) -> None:
        ...
    def Reset(self) -> None:
        ...
    AngularTolerance: float
    BaseCornerCut: Features.ShipDesign.CornerCutBuilder
    DistanceTolerance: float
    LocationOffset: Expression
    OrientationAngle: Expression
    ReinforceOffset: Expression
    ReinforcementCornerCut: Features.ShipDesign.CornerCutBuilder
    ReverseSplitDirection: bool
    SplitReinforcement: bool
    ToolCurve: Section
    ToolFacePlane: SelectNXObject
    ToolType: int
    WeldCharacteristics: Weld.CharacteristicsBuilder


    class ToolTypes(enum.Enum):
        FacePlane = 0
        Curve = 1
    

class SplitStandardPart(Features.Feature):
    def __init__(self) -> None: ...


class SplitProfilePlateBuilder(Builder):
    def __init__(self) -> None: ...
    ApplyEndCut: bool
    BuiltUpOffset: Features.ShipDesign.BuiltUpOffsetBuilder
    DistanceTolerance: float
    DoTrimWithoutCopy: bool
    ReverseDirection: bool
    SplitDirectionOption: Features.ShipDesign.SplitProfilePlateBuilder.SplitDirectionOptionType
    TargetBuiltUps: SelectNXObjectList
    TargetProfileOrPlates: SelectNXObjectList
    TargetType: Features.ShipDesign.SplitProfilePlateBuilder.ProfileType
    ToolBodies: SelectBodyList
    ToolCurves: SelectNXObjectList
    ToolCurvesSection: Section
    ToolFaces: SelectNXObjectList
    ToolNewPlane: Plane
    ToolOption: Features.ShipDesign.SplitProfilePlateBuilder.ToolOptionType
    ToolVector: Direction
    TrimDirection: Vector3d


    class ToolOptionType(enum.Enum):
        Plane = 0
        NewPlane = 1
        Extrude = 2
        Body = 3
    

    class SplitDirectionOptionType(enum.Enum):
        PerpendicularToMoldingFace = 0
        AlongPlaneOrFace = 1
    

    class ProfileType(enum.Enum):
        ProfileOrPlate = 0
        BuiltUp = 1
    

class SpatialBreakdownExportBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ExportNativeFilename: str
    RootNodeSelection: Features.ShipDesign.NodeSelectionBuilder


class SpatialBreakdownBuilder(Builder):
    def __init__(self) -> None: ...
    def GetBreakdownType(self) -> str:
        ...
    def SetBreakdownType(self, breakdownType: str) -> None:
        ...
    def GetBreakdownSubType(self) -> str:
        ...
    def SetBreakdownSubType(self, subBreakdownType: str) -> None:
        ...
    def GetCurrentNode(self) -> TaggedObject:
        ...
    def SetCurrentNode(self, tNode: TaggedObject) -> None:
        ...
    def GetParentNode(self) -> TaggedObject:
        ...
    def SetParentNode(self, tNode: TaggedObject) -> None:
        ...
    BreakdownName: str
    NodeSelection: Features.ShipDesign.NodeSelectionBuilder
    Room: SelectNXObjectList
    Type: Features.ShipDesign.SpatialBreakdownBuilder.Types


    class Types(enum.Enum):
        Breakdown = 0
        Volume = 1
    

class SmartRuleBuilder(Features.ShipDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    RuleFeatures: Features.SelectFeatureList


class SmartRule(Features.Feature):
    def __init__(self) -> None: ...


class ShipTrimBodyBuilder(Builder):
    def __init__(self) -> None: ...
    ApplyEndCut: bool
    BuiltUpOffset: Features.ShipDesign.BuiltUpOffsetBuilder
    ReverseDirection: bool
    SplitDirectionOption: Features.ShipDesign.SplitProfilePlateBuilder.SplitDirectionOptionType
    TargetBody: SelectNXObject
    ToolCurves: SelectNXObjectList
    ToolFaces: SelectNXObjectList
    ToolOption: Features.ShipDesign.SplitProfilePlateBuilder.ToolOptionType
    ToolVector: Direction


class ShipTrimBody(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetPillarStartPoints(self) -> typing.List[Point]:
        ...
    def GetPillarEndPoints(self) -> typing.List[Point]:
        ...


class ShipStructureBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AdditionalObjects: SelectNXObjectList
    AdditionalStructures: Assemblies.SelectComponentList
    FocusPlates: SelectNXObjectList
    HiddenObjects: SelectNXObjectList


    class ZFilter(enum.Enum):
        All = 0
        DeckFrames = 1
        LongitudinalFrames = 2
    

class ShipSectionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetDeckContainer(self, isDeckContainer: bool) -> None:
        ...
    AssemblyPart: str
    BottomDeckSectionName: str
    ReadDataSet: Features.ShipDesign.ReadDataSetBuilder
    ReferenceGeometry: SelectDisplayableObjectList
    SectionName: str
    SectionPart: str
    SectionType: Features.ShipDesign.ShipSectionBuilder.Type
    SectionXMax: int
    SectionXMin: int
    SectionYMax: int
    SectionYMin: int
    SectionZMax: int
    SectionZMin: int
    ShipBodies: SelectDisplayableObjectList
    ShipBody: SelectBody
    XDatumFilter: Features.ShipDesign.ShipSectionBuilder.XFilter
    XMaxDatumFilter: int
    XMaxOffset: Expression
    XMinDatumFilter: int
    XMinOffset: Expression
    YDatumFilter: int
    YMaxDatumFilter: int
    YMaxOffset: Expression
    YMinDatumFilter: int
    YMinOffset: Expression
    ZDatumFilter: Features.ShipDesign.ShipSectionBuilder.ZFilter
    ZMaxDatumFilter: int
    ZMaxOffset: Expression
    ZMinDatumFilter: int
    ZMinOffset: Expression


    class XFilter(enum.Enum):
        All = 0
        TransverseFrames = 1
        Bulkheads = 2
    

    class Type(enum.Enum):
        Manual = 0
        Spreadsheet = 1
        Decks = 2
    

class ShipSection(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShipProfileCutoutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    PierceFaces: SelectFaceList
    ProfileBodies: SelectBodyList
    Size: str


class ShipProfileCutout(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShipPrimarySectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AddPrimarySection(self, sectionName: str) -> None:
        ...
    def RemovePrimarySection(self, sectionName: str) -> None:
        ...
    def Validate(self) -> bool:
        ...


class ShipPreparationInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSourceData(self, sourceData: typing.List[NXObject]) -> None:
        ...
    def SetSourceData(self, sourceData: typing.List[NXObject]) -> None:
        ...
    def GetLinkedData(self, linkedData: typing.List[NXObject]) -> None:
        ...
    def GetImprintData(self, imprintData: typing.List[NXObject]) -> None:
        ...
    def SetImprintData(self, imprintData: typing.List[NXObject]) -> None:
        ...
    BasicDesignFeature: Features.Feature
    BlendRadius: float
    ExtendImprints: bool
    Feature: Features.Feature
    HoleDiameter: float
    MaximumExtensionDistance: float
    Parent: Features.ShipDesign.ShipPreparationInfo
    RemoveBlends: bool
    RemoveOpenings: bool
    SourcePart: Assemblies.Component
    Target: Features.ShipDesign.ShipPreparationInfo
    TargetBody: Body
    ToBeDeleted: bool
    Type: Features.ShipDesign.ShipPreparationInfo.Types


    class Types(enum.Enum):
        Unknown = 0
        LinkedBody = 1
        LinkedBodyBracket = 2
        LinkedEdges = 3
        LinkedCurves = 4
        LinkedFaces = 5
        PlateDivide = 6
        StiffenerDivide = 7
        StiffenerBySupportDivide = 8
        EdgeReinforcementDivide = 9
        EdgeReinforcementEdges = 10
        StandardPartBracketDivide = 11
        Pillar = 12
        BracketDivide = 13
        UserDefined = 14
    

class ShipPreparationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def FindShipComponents(self, components: typing.List[Assemblies.Component], componentsProcessed: bool) -> None:
        ...
    def FindBasicDesignData(self, components: typing.List[Assemblies.Component], data: typing.List[Features.ShipDesign.ShipPreparationInfo]) -> None:
        ...
    def WaveLinkCaePrepareBoundary(self, boundarys: typing.List[TaggedObject]) -> None:
        ...
    def WaveLinkBasicDesignData(self, data: Features.ShipDesign.ShipPreparationInfo) -> None:
        ...
    def CreateUpdateDivide(self, data: Features.ShipDesign.ShipPreparationInfo) -> None:
        ...
    def ConvertSeamCurves(self, data: typing.List[Features.ShipDesign.ShipPreparationInfo]) -> None:
        ...
    def UpdateEdgePairing(self) -> None:
        ...
    def FinalizeProcessing(self) -> None:
        ...
    def CreateBasicDesignData(self) -> Features.ShipDesign.ShipPreparationInfo:
        ...
    def SetEdgePair(self, edge1: Edge, edge2: Edge) -> None:
        ...
    def GetPairedEdge(self, inEdge: Edge) -> Edge:
        ...
    def AssignMeshAttributes(self, data: Features.ShipDesign.ShipPreparationInfo) -> None:
        ...
    def CacheCaePrepareComponent(self, component: Assemblies.Component) -> None:
        ...
    BlendRadius: float
    BoundaryObjects: SelectDisplayableObjectList
    DistanceTolerance: float
    HoleDiameter: float
    RemoveBlends: bool
    RemoveOpenings: bool
    ShipComponents: SelectDisplayableObjectList


class ShipPaintParametersBuilder(Features.PaintParametersBuilder):
    def __init__(self) -> None: ...
    def GetSourceObjectParameters(self) -> ShipDesign.PaintParametersData:
        ...
    def SetSectionType(self, spreadsheetData: ShipDesign.PaintParametersData, strSectionType: str, categoryName: str) -> None:
        ...
    def SetSectionSubType1(self, spreadsheetData: ShipDesign.PaintParametersData, strSectionType: str, categoryName: str) -> None:
        ...
    def SetSectionSubType2(self, spreadsheetData: ShipDesign.PaintParametersData, strSectionType: str, categoryName: str) -> None:
        ...
    def ModifyParameterImpactTypes(self, spreadsheetData: ShipDesign.PaintParametersData, strParameterName: str, strParameterValue: str) -> None:
        ...
    def SetPaintParametersData(self, pPaintParametersData: ShipDesign.PaintParametersData) -> None:
        ...
    def SetFrecBuilder(self, builderTag: Builder) -> None:
        ...
    def UpdateParameters(self, pPaintParametersData: ShipDesign.PaintParametersData, checkedPara: typing.List[ShipDesign.PaintParametersParameterValue]) -> typing.List[ShipDesign.PaintParametersParameterValue]:
        ...
    def SetPrimaryParameterValue(self, spreadsheetData: ShipDesign.PaintParametersData, parameterName: str, categoryName: str, parameterValue: str) -> None:
        ...
    def UpdatePossibleContextAttributes(self, spreadsheetData: ShipDesign.PaintParametersData, categoryName: str) -> None:
        ...
    def UpdateParametersUsingRules(self, spreadsheetData: ShipDesign.PaintParametersData) -> None:
        ...
    def EditPrimaryParameter(self, spreadsheetData: ShipDesign.PaintParametersData, categoryName: str, parameterName: str, parameterValue: str) -> None:
        ...
    def EditParameter(self, spreadsheetData: ShipDesign.PaintParametersData, categoryName: str, parameterName: str, parameterValue: str) -> None:
        ...
    def SetSuppressFlag(self) -> None:
        ...
    def UnsetSuppressFlag(self) -> None:
        ...


class ShipNamesListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetObjectTypes(self, objects: typing.List[NXObject]) -> typing.List[Features.ShipDesign.ShipNamesBuilder]:
        ...
    def ResetNameList(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ShipNamesList: Features.ShipDesign.ShipNamesBuilderList


class ShipnamesBuilderVersion(enum.Enum):
    Legacy = 0
    PositionInformation = 1


class ShipnamesBuilderType(enum.Enum):
    None = 0
    Hull = 1
    Deck = 2
    LongitudinalBulkhead = 3
    TransverseBulkhead = 4
    StiffenerSystem = 5
    EdgeReinforcementSystem = 6
    PillarSystem = 7
    Seam = 8
    GenericPlateSystem = 9
    StandardPart = 10
    CollarPlate = 11
    Bracket = 12
    Plate = 13
    Profile = 14
    Pillar = 15
    StandardPartCollarPlate = 16
    StandardPartBracket = 17
    Grid = 18
    Room = 19
    BasicDesignCollarPlate = 20
    BasicDesignBracket = 21
    BasicDesignStandardPartCollarPlate = 22
    BasicDesignStandardPartBracket = 23
    FlatBar = 24
    StructuredesignStructure = 25
    StructuredesignMember = 26
    StructuredesignCorner = 27
    StructuredesignEndcap = 28
    StructuredesignGusset = 29
    StructuredesignMountingfeet = 30
    StructuredesignGrabtab = 31
    StructuredesignBeampreparation = 32
    StructuredesignConsolidate = 33
    StructuredesignBoltedconnection = 34
    StructuredesignConsolidatemember = 35
    StructuredesignStiffener = 36


class ShipnamesBuilderMethod(enum.Enum):
    Unknown = -1
    MoldingFace = 0
    Point = 1
    ParentBody = 2


class ShipNamesBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.ShipNamesBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.ShipNamesBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.ShipNamesBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.ShipNamesBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.ShipNamesBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.ShipNamesBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.ShipNamesBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.ShipNamesBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.ShipNamesBuilder, object2: Features.ShipDesign.ShipNamesBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.ShipNamesBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ShipNamesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetFieldcount(self) -> int:
        ...
    def GetField(self, idx: int) -> Features.ShipDesign.ShipNameFieldBuilder:
        ...
    def SetGridPartUID(self, gridPartUID: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ContextAttribute: str
    ShipObjectType: Features.ShipDesign.ShipnamesBuilderType


class ShipnameFieldBuilderType(enum.Enum):
    Fixed = 0
    Option = 1
    Index = 2
    Any = 3
    PositionInformation = 4
    ContextAttributeMap = 5
    SectionInformation = 6
    AttributeMap = 7
    ParentPartPosition = 8
    FrameName = 9
    PortOrStarboard = 10
    DirectionInformation = 11
    SmartFixed = 12
    None = 13


class ShipNameFieldBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetOptionValues(self) -> str:
        ...
    def Validate(self) -> bool:
        ...
    Value: str


class ShipIntersectionsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BulkheadEnum: Features.ShipDesign.ShipIntersectionsBuilder.Type
    DeckEnum: Features.ShipDesign.ShipIntersectionsBuilder.Type
    InterSectionsType: Features.ShipDesign.ShipIntersectionsBuilder.CreationType
    InterTransFrameEnum: Features.ShipDesign.ShipIntersectionsBuilder.Type
    ReadDataSet: Features.ShipDesign.ReadDataSetBuilder
    TransFrameEnum: Features.ShipDesign.ShipIntersectionsBuilder.Type
    YFrameEnum: Features.ShipDesign.ShipIntersectionsBuilder.Type
    ZFrameEnum: Features.ShipDesign.ShipIntersectionsBuilder.Type


    class Type(enum.Enum):
        None = 0
        SheetBodies = 1
        Curves = 2
        All = 3
    

    class CreationType(enum.Enum):
        Manual = 0
        Spreadsheet = 1
    

class ShipIntersections(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShipGridBuilder(Builder):
    def __init__(self) -> None: ...
    GridPart: str


class ShipFeatureConverter(Builder):
    def __init__(self) -> None: ...
    NumCandidateFeatures: int
    NumConvertedFeatures: int
    Scope: Features.ShipDesign.ShipFeatureConverter.PartScope


    class PartScope(enum.Enum):
        WorkPart = 0
        WorkPartandComponents = 1
    

class ShipEndCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CoordSystem: CoordinateSystem
    EndCutBlock: EndCutBlockBuilder
    PlacementType: Features.ShipDesign.ShipEndCutBuilder.CreationMethod
    SelectCSYSFace: SelectTaggedObject
    SelectEdge: SelectTaggedObject
    SelectTargetFace: SelectTaggedObject


    class CreationMethod(enum.Enum):
        FaceEdge = 0
        SpecifyCSYS = 1
    

class ShipEndCut(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShipDesignVersionUpBuilder(Builder):
    def __init__(self) -> None: ...
    SelectFeatures: Features.SelectFeatureList


class ShipDesignPreferencesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def ApplyDisplayOption(self) -> None:
        ...
    AnalysisSpacing: float
    AngleRule: Features.ShipDesign.ShipDesignPreferencesBuilder.AngleRuleTypes
    Color: NXColor
    ColorOption: Features.ShipDesign.ShipDesignPreferencesBuilder.ColorType
    DisplayOption: Features.ShipDesign.ShipDesignPreferencesBuilder.DisplayType
    Font: Preferences.PartObject.LineFontType
    Layer: int
    NonTightColor: NXColor
    NonTightColorOption: Features.ShipDesign.ShipDesignPreferencesBuilder.NonTightColorType
    ShipStructureType: Features.ShipDesign.ShipDesignPreferencesBuilder.Types
    SurfaceAngleAcceptableColor: NXColor
    SurfaceAngleFailureColor: NXColor
    SurfaceAngleFailureLimit: float
    SurfaceAngleWarningColor: NXColor
    SurfaceAngleWarningLimit: float
    TwistRateAcceptableColor: NXColor
    TwistRateFailureColor: NXColor
    TwistRateFailureLimit: float
    TwistRateWarningColor: NXColor
    TwistRateWarningLimit: float
    Type: Features.ShipDesign.ShipDesignPreferencesBuilder.Types
    Width: Preferences.PartObject.WidthType


    class Types(enum.Enum):
        Hull = 0
        Deck = 1
        TransverseBulkhead = 2
        LongitudinalBulkhead = 3
        GenericPlateSystem = 4
        StiffenerSystem = 5
        EdgeReinforcementSystem = 6
        PillarSystem = 7
        ScantlingSeam = 8
        ErectionSeam = 9
        StrakingSeam = 10
        IntersectionSeam = 11
        Bracket = 12
        CollarPlate = 13
    

    class NonTightColorType(enum.Enum):
        Default = 0
        Set = 1
    

    class DisplayType(enum.Enum):
        Curve = 0
        CurveAndSolid = 1
    

    class ColorType(enum.Enum):
        Default = 0
        Set = 1
    

    class AngleRuleTypes(enum.Enum):
        RightHand = 0
        ShipOrientation = 1
    

class ShipCutoutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngularDim: Expression
    CoordSystem: CoordinateSystem
    KeepCoordSystem: bool
    KeepReverseDirection1: bool
    KeepReverseDirection2: bool
    KeepSelectCSYSFace: bool
    KeepSelectLine1: bool
    KeepSelectLine2: bool
    KeepSelectTargetFace: bool
    LinearOffset1: Expression
    LinearOffset2: Expression
    PlacementType: Features.ShipDesign.ShipCutoutBuilder.CreationMethod
    ReverseDirection1: bool
    ReverseDirection2: bool
    SelectCSYSFace: SelectFace
    SelectLine1: SelectNXObject
    SelectLine2: SelectNXObject
    SelectTargetFace: SelectNXObject
    SketchBlock: SketchExpressionModifierBuilder


    class CreationMethod(enum.Enum):
        Face2Lines = 0
        SpecifyCSYS = 1
    

class ShipCutout(Features.BodyFeature):
    def __init__(self) -> None: ...


    class ZDirectionType(enum.Enum):
        Above = 0
        Below = 1
    

class ShipCoordinatesBuilder(Builder):
    def __init__(self) -> None: ...
    def CycleRoutingPorts(self) -> None:
        ...
    def CreatePointByCoordinates(self) -> None:
        ...
    def SetPosition(self, position: Point3d) -> None:
        ...
    def GetPorts(self, ports: typing.List[TaggedObject]) -> None:
        ...
    def EvaluateSinglePortInformation(self, portIndex: int) -> None:
        ...
    def EvaluatePointInformation(self, position: Point3d) -> None:
        ...
    def SetPointSelectionView(self, tgView: View) -> None:
        ...
    def SetCurrentDisplayPort(self, port: TaggedObject) -> None:
        ...
    def AppendPointToInformation(self) -> None:
        ...
    def CreatePMILabelInModel(self, pointTag: Point, targetView: ModelingView, labelType: int) -> Annotations.PmiNote:
        ...
    AbsXValue: float
    AbsYValue: float
    AbsZValue: float
    CreateByCoordinates: bool
    CreateCoordSymbol: bool
    CreatePmiWithLeader: bool
    DeltaX: float
    DeltaY: float
    DeltaZ: float
    OutputToInformation: bool
    Point: Point
    PointSymbolType: Features.ShipDesign.ShipCoordinatesBuilder.SymbolType
    PortName: str
    RoutingComponent: SelectDisplayableObject
    SelectionType: Features.ShipDesign.ShipCoordinatesBuilder.Selection
    Type: Features.ShipDesign.ShipCoordinatesBuilder.Selection
    XDirection: Features.ShipDesign.ShipCoordinatesBuilder.XDirectionType
    XDistance: float
    XFrameOption: str
    XValueLabel: bool
    YDirection: Features.ShipDesign.ShipCoordinatesBuilder.YDirectionType
    YDistance: float
    YFrameOption: str
    YValueLabel: bool
    ZDirection: Features.ShipDesign.ShipCoordinatesBuilder.ZDirectionType
    ZDistance: float
    ZFrameOption: str
    ZValueLabel: bool


    class YDirectionType(enum.Enum):
        Port = 0
        Starboard = 1
    

    class XDirectionType(enum.Enum):
        Forward = 0
        Aft = 1
    

    class SymbolType(enum.Enum):
        ShipAbsoluteCoordinate = 0
        ShipGridCoordinate = 1
    

    class Selection(enum.Enum):
        Point = 0
        Component = 1
    

class ShipCoordinates(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShipContainerBuilder(Builder):
    def __init__(self) -> None: ...
    ContainerName: str
    ContainerPart: str


class ShipAttributeHolder(Builder):
    def __init__(self) -> None: ...
    def SetAttributesToObjects(self, object: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX8.0.1.  Use NXOpen.Features.ShipDesign.ShipAttributeHolder.SetAttributesToProxy instead.")"""
        ...
    def CopyAttributesToPart(self, object: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX8.0.1.  This method is no longer valid. Use the un-deprecated method with the same method name.")"""
        ...
    def SetAttributesToObjects(self, bCreate: bool, featBuilder: Features.FeatureBuilder) -> None:
        """[Obsolete("Deprecated in NX8.0.2.  Use NXOpen.Features.ShipDesign.ShipAttributeHolder.SetAttributesToProxy instead.")"""
        ...
    def CopyAttributesToObjects(self, bCreate: bool, featBuilder: Features.FeatureBuilder) -> None:
        ...
    def CopyAttributesToPart(self, bCreate: bool, featBuilder: Features.FeatureBuilder) -> None:
        ...
    def SetAttributesToProxy(self, object: NXObject) -> None:
        ...
    def GetAttributeProxy(self) -> NXObject:
        ...
    def SetAttributeToProxyFromBuilder(self, featBuilder: Features.FeatureBuilder) -> None:
        ...
    def GetContextAttributeFromNamesBuilder(self, featBuilder: Features.FeatureBuilder) -> None:
        ...
    def SetAttributeToObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def UpdateContextName(self, featureTag: NXObject) -> None:
        ...
    def UpdateContextNameAndRenameFeature(self, featureTag: NXObject) -> None:
        ...


class ShellTemplateBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    CoordinateSystem: CoordinateSystem
    CornerCutType: Features.ShipDesign.ShellTemplateBuilder.CornerCutTypes
    CreateSeparateParts: bool
    DistanceTolerance: float
    EndXTemplateOffset: Expression
    EndYTemplateOffset: Expression
    MarkingLinesDirectionType: Features.ShipDesign.ShellTemplateBuilder.MarkingTypes
    PlaneAutomatic: SelectIBasePlaneList
    PlaneMethod: Features.ShipDesign.ShellTemplateBuilder.PlaneLocationTypes
    SightLineCutType: Features.ShipDesign.ShellTemplateBuilder.SightLineCutTypes
    SpecifyXPlane: Plane
    SpecifyYPlane: Plane
    StartXTemplateOffset: Expression
    StartYTemplateOffset: Expression
    Surface: ScCollector
    TemplateSetName: str
    Thickness: Expression
    Type: Features.ShipDesign.ShellTemplateBuilder.Types
    XOffset: Expression
    XPlaneUserDefined: bool
    YOffset: Expression
    YPlaneUserDefined: bool


    class Types(enum.Enum):
        Manual = 0
        InferCoordinateSystem = 1
    

    class SightLineCutTypes(enum.Enum):
        None = 0
        TowardStart = 1
        TowardEnd = 2
    

    class PlaneLocationTypes(enum.Enum):
        Existing = 0
        Offset = 1
    

    class MarkingTypes(enum.Enum):
        None = 0
        XDirectionOnly = 1
        YDirectionOnly = 2
        XandYDirections = 3
    

    class CornerCutTypes(enum.Enum):
        None = 0
        Start = 1
        End = 2
    

class ShellTemplate(Features.BodyFeature):
    def __init__(self) -> None: ...


class ShellExpansionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AdditionalPlanesPerFrame: int
    AftLimitPlane: SelectDatumPlane
    Associative: bool
    BasePlane: SelectDatumPlane
    CurvesToMap: Section
    FacesToFlatten: ScCollector
    ForeLimitPlane: SelectDatumPlane
    MapFaceEdges: bool
    MapTransverseFrames: bool
    Tolerance: float
    UpperLimitPlane: SelectDatumPlane


class ShellExpansion(Features.Feature):
    def __init__(self) -> None: ...


class SetModeBuilder(Builder):
    def __init__(self) -> None: ...
    def SetMode(self) -> int:
        ...
    DesignElementToSetMode: SelectNXObjectList
    ManufacturingDesignMode: Features.ShipDesign.SetModeBuilder.DesMfgMode


    class DesMfgMode(enum.Enum):
        DesignMode = 0
        ManufacturingMode = 1
    

class SelectViewBuilder(Builder):
    def __init__(self) -> None: ...
    View: Drawings.SelectDraftingViewList


class SelectStructuresBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetFinalStructuresByRule(self) -> typing.List[Assemblies.Component]:
        ...
    def AddStructuresByRule(self, structures: typing.List[Assemblies.Component]) -> None:
        ...
    def RemoveStructuresByRule(self, structures: typing.List[Assemblies.Component]) -> None:
        ...
    def ResetStructuresByRule(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AdditionalStructures: SelectNXObjectList


class SelectPartBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetSectionBlockParts(self, sectionParts: str) -> None:
        ...
    def SetFrameParts(self, framePartFilenames: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    SectionFrameType: Features.ShipDesign.SelectPartBuilder.Types


    class Types(enum.Enum):
        Section = 0
        Frame = 1
    

class SectionViewBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.SectionViewBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.SectionViewBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.SectionViewBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.SectionViewBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SectionViewBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SectionViewBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.SectionViewBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.SectionViewBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.SectionViewBuilder, object2: Features.ShipDesign.SectionViewBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.SectionViewBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SectionViewBuilder(Builder):
    def __init__(self) -> None: ...
    def GetViewDirection(self) -> Features.ShipDesign.SectionViewBuilder.DirectionOptions:
        ...
    AdditionalStructures: SelectNXObjectList
    BackProximity: float
    DrawingName: str
    DrawingSheet: Features.ShipDesign.DrawingSheetBuilder
    DrawingTemplate: Features.ShipDesign.DrawingTemplateBuilder
    FlipViewDirection: bool
    FrontProximity: float
    HiddenObjects: SelectNXObjectList
    Margin: float
    Offset: float
    PlaneType: Features.ShipDesign.SectionViewBuilder.PlaneTypes
    SectionPlane: Plane
    SectionPlaneName: str
    SectionRule: Features.ShipDesign.SectionViewBuilder.SectionRuleOptions
    SelectFrame: SelectDatumPlaneList
    SheetScale: float
    ShipStructure: Features.ShipDesign.ShipStructureBuilder
    SymmetricalStructure: Features.ShipDesign.SectionViewBuilder.SymmetricalStructureOptions
    ViewName: str
    XPosition: float
    YPosition: float


    class SymmetricalStructureOptions(enum.Enum):
        Full = 0
        Port = 1
        Starboard = 2
    

    class SectionRuleOptions(enum.Enum):
        ByRule = 0
        SimpleSection = 1
    

    class PlaneTypes(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        UserSpecified = 3
    

    class DirectionOptions(enum.Enum):
        Fw = 0
        Af = 1
        In = 2
        Ot = 3
        P = 4
        S = 5
        Up = 6
        Dn = 7
    

class SectionEditorBuilder(Builder):
    def __init__(self) -> None: ...
    def FindFocusPlates(self, origin: Point3d, normal: Vector3d, frontProximity: float, backProximity: float) -> typing.List[NXObject]:
        ...
    def FindFocusPlates(self, sectionPlane: Plane) -> typing.List[NXObject]:
        ...
    BackProximity: Expression
    Denominator: int
    FrontProximity: Expression
    Numerator: int
    SectionRule: Features.ShipDesign.SectionViewBuilder.SectionRuleOptions
    SectionView: Features.ShipDesign.SectionViewBuilder
    ShipStructure: Features.ShipDesign.ShipStructureBuilder
    SymmetricalStructure: Features.ShipDesign.SectionViewBuilder.SymmetricalStructureOptions
    ViewList: Drawings.SelectDraftingViewList


class SectionDrawingBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateSectionViewBuilder(self) -> Features.ShipDesign.SectionViewBuilder:
        ...
    def FindFocusPlates(self, frame: NXObject, offset: float, frontProximity: float, backProximity: float) -> typing.List[NXObject]:
        ...
    def FindFocusPlates(self, frame: NXObject, direction: Features.ShipDesign.SectionViewBuilder.DirectionOptions, offset: float, frontProximity: float, backProximity: float) -> typing.List[NXObject]:
        ...
    def CreateDrawingPartBuilder(self, drawingPart: Part) -> Features.ShipDesign.DrawingPartBuilder:
        ...
    DrawingPartList: Features.ShipDesign.DrawingPartBuilderList
    SectionsPerDrawing: Features.ShipDesign.SectionDrawingBuilder.SectionsPerDrawingOptions
    ShipPrimarySection: Features.ShipDesign.ShipPrimarySectionBuilder
    ViewList: Features.ShipDesign.SectionViewBuilderList
    ViewType: Features.ShipDesign.SectionDrawingBuilder.ViewTypeOptions
    ViewsPerSheet: Features.ShipDesign.SectionDrawingBuilder.ViewsPerSheetOptions


    class ViewTypeOptions(enum.Enum):
        BasicDesign = 0
        DetailDesign = 1
    

    class ViewsPerSheetOptions(enum.Enum):
        One = 0
        Two = 1
        Three = 2
        Four = 3
        Five = 4
        Six = 5
    

    class SectionsPerDrawingOptions(enum.Enum):
        Single = 0
        Multiple = 1
    

class SeamBuilder(Features.ShipDesign.ProfileSystemBuilder):
    def __init__(self) -> None: ...
    def GetAttachedProfiles(self, plateOrProfile: NXObject, profiles: typing.List[Curve]) -> None:
        ...
    BuiltUpOffset: Features.ShipDesign.BuiltUpOffsetBuilder
    DefinitionCurves: Section
    DefinitionEquallySpacedCurve1: Section
    DefinitionEquallySpacedCurve2: Section
    DefinitionEquallySpacedNumber: Expression
    DefinitionEquallySpacedPlaneList: Features.ShipDesign.PlaneListBuilderList
    DefinitionMethod: Features.ShipDesign.SeamBuilder.DefinitionMethods
    DefinitionObjects: SelectNXObjectList
    DefinitionPlaneList: Features.ShipDesign.PlaneListBuilderList
    DefinitionProjectionDirection: GeometricUtilities.ProjectionOptions
    DefinitionRectangularCorner: Point
    DefinitionRectangularLength: Expression
    DefinitionRectangularLengthDirection: Direction
    DefinitionRectangularPlane: Plane
    DefinitionRectangularWidth: Expression
    EndCut: Features.ShipDesign.EndCutBuilder
    EndCutSplit: Features.ShipDesign.StiffenerSystemBuilder.EndCutTypes
    ErectionSplitSystem: bool
    IntersectionSplitSystem: bool
    PointProfileTolerance: float
    ReparentFrecsReferencingSeamedObject: bool
    ScantlingSplitSystem: bool
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    ShipStructure: SelectNXObjectList
    StaggerDistanceList: NXObjectList
    StaggerShiftAlongMethod: Features.ShipDesign.SeamBuilder.StaggerShiftAlongMethods
    StrakingSplitSystem: bool
    Type: Features.ShipDesign.SeamBuilder.Types
    WeldingCharacteristics: Weld.CharacteristicsBuilder


    class Types(enum.Enum):
        Scantling = 0
        Erection = 1
        Straking = 2
        Intersection = 3
        Eggbox = 4
    

    class StaggerShiftAlongMethods(enum.Enum):
        Length = 0
        Width = 1
    

    class DefinitionMethods(enum.Enum):
        CurvesPlanesShip = 0
        EquallySpaced = 1
        Rectangular = 2
    

class SeamBlockBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.SeamBlockBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.SeamBlockBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.SeamBlockBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.SeamBlockBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SeamBlockBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.SeamBlockBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.SeamBlockBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.SeamBlockBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.SeamBlockBuilder, object2: Features.ShipDesign.SeamBlockBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.SeamBlockBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SeamBlockBuilder(NXObject):
    def __init__(self) -> None: ...
    FlangeWidth: Expression
    PlateStock: Features.ShipDesign.PlateStockBuilder
    SeamOption: Features.ShipDesign.SeamBlockBuilder.SeamType
    SeamSelection: SelectTaggedObject


    class SeamType(enum.Enum):
        FlangeOnly = 0
        WebOnly = 1
        NoFlange = 2
    

class Seam(Features.CurveFeature):
    def __init__(self) -> None: ...


class ScantlingTableBuilder(Builder):
    def __init__(self) -> None: ...
    def SwapScantlingTableInfo(self, index1: int, index2: int) -> None:
        ...
    def UpdateScantlingTableSpecialMark(self, index: int, strNewSpeicalMark: str) -> None:
        ...
    def UpdateToggleForScantlingTable(self, index: int, bToggleOn: bool) -> None:
        ...
    def UpdateScantlingTableDisplay(self) -> None:
        ...
    def UpdateLetteringLineSpaceFactor(self) -> None:
        ...
    LetteringLineSpaceFactor: float


class RoomThicknessItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.RoomThicknessItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.RoomThicknessItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.RoomThicknessItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.RoomThicknessItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.RoomThicknessItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.RoomThicknessItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.RoomThicknessItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.RoomThicknessItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.RoomThicknessItemBuilder, object2: Features.ShipDesign.RoomThicknessItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.RoomThicknessItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class RoomThicknessItemBuilder(Builder):
    def __init__(self) -> None: ...
    Label: str
    Thickness: Expression
    Type: Features.ShipDesign.RoomThicknessItemBuilder.Types


    class Types(enum.Enum):
        Wall = 0
        Floor = 1
        Ceiling = 2
    

class RoomPanelBuilder(Builder):
    def __init__(self) -> None: ...
    AdoptBodySelect: ScCollector
    FaceCharacteristics: Features.ShipDesign.GeneralArrangement.FaceCharacteristicsBuilder
    PanelSketchSection: Section
    RoomBodySelect: ScCollector
    Thickness: Expression
    ThicknessDirection: bool
    ThicknessType: Features.ShipDesign.RoomPanelBuilder.JaRoomPanelThicknessTypes
    Tolerance: float
    Type: Features.ShipDesign.RoomPanelBuilder.Types


    class Types(enum.Enum):
        Create = 0
        Adopt = 1
    

    class JaRoomPanelThicknessTypes(enum.Enum):
        Symmetric = 0
        SingleSided = 1
    

class RoomContainerBuilder(Builder):
    def __init__(self) -> None: ...
    def AddRoomAndPurpose(self, room: str, purpose: str) -> None:
        ...
    DeckBody: ScCollector
    DeckPlanSketch: Section
    RoomNamePrefix: str


class RoomBuilder(Builder):
    def __init__(self) -> None: ...
    def EvaluateAttributes(self, bUpdateRoomAreaAndVolume: bool) -> None:
        ...
    def UpdateTypeForAttributeListBuilder(self) -> None:
        ...
    def AdoptChanged(self) -> None:
        ...
    def GetCreatedRoomBodies(self, createdRoomBodies: typing.List[TaggedObject]) -> None:
        ...
    def CloneSectionBuilder(self, builderTo: Features.ShipDesign.RoomBuilder) -> None:
        ...
    def UpdateSection(self, needDeleteOldSettion: bool, section: Section) -> None:
        ...
    def UpdateSectionCurves(self, section: Section) -> None:
        ...
    def AddNewRoomBuilder(self, newBuilder: Features.ShipDesign.RoomBuilder) -> None:
        ...
    def RemoveRoomBuilder(self, roomBuilder: Features.ShipDesign.RoomBuilder) -> None:
        ...
    def UpdateRoomID(self, roomID: str) -> None:
        ...
    def ResetAttributes(self, bUpdateRoomAreaAndVolume: bool) -> None:
        ...
    def UpdateSpaceType(self, spaceType: str) -> None:
        ...
    def ClearDeckBodies(self) -> None:
        ...
    def AddDeckBody(self, deckBody: TaggedObject) -> None:
        ...
    AdoptionBody: SelectBody
    AttributeList: Features.ShipDesign.RoomAttributeListBuilder
    CalculateRoomAttributes: bool
    CreateCogPoints: bool
    CreateRoomWithReferenceComponent: bool
    CreateRoomWithWall: bool
    Deck: SelectBodyList
    DistanceTolerance: float
    RoomColor: NXColor
    Section: Section
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    ThicknessList: Features.ShipDesign.RoomThicknessItemBuilderList
    Type: Features.ShipDesign.RoomBuilder.Types
    WallThickness: Expression


    class Types(enum.Enum):
        Create = 0
        Adopt = 1
    

class RoomAttributesBuilder(Builder):
    def __init__(self) -> None: ...
    def ClearRoomAttributes(self) -> None:
        ...
    RoomAttributes: Features.ShipDesign.RoomAttributeListBuilder
    SelectRoom: SelectTaggedObjectList


class RoomAttributeListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def InitFromObject(self, objectTag: TaggedObject) -> None:
        ...
    def UpdateAttributes(self, attrNames: str, attrValues: str) -> None:
        ...
    def SetAttribute(self, index: int, attrName: str, attrValue: str) -> None:
        ...
    def SetRoomPurpose(self, roomPurpose: str) -> None:
        ...
    def SetRoomSubPurpose(self, roomSubPurpose: str) -> None:
        ...
    def InitializeFromMultipleObjects(self, objs: typing.List[TaggedObject]) -> None:
        ...
    def EditItem(self, row: int, roomPurpose: str, roomSubPurpose: str) -> None:
        ...
    def UpdateAttributeValue(self, row: int, headString: str, value: str) -> None:
        ...
    def UpdateEvaluatdValue(self, rowIndex: int) -> bool:
        ...
    def Validate(self) -> bool:
        ...


class RollingLineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    AngleDivisions: Expression
    AngleTolerance: float
    ConstructionMethodOption: Features.ShipDesign.RollingLineBuilder.ConstructionMethodTypes
    DistanceTolerance: float
    DupinIndicatrix: GeometricAnalysis.DupinBuilder
    EvaluationPoint: Point
    EvaluationPointOption: Features.ShipDesign.RollingLineBuilder.StartEvaluationTypes
    HideConstructionProcess: bool
    Offset: Expression
    PlanarRadiusLimit: Expression
    PlaneOrientation: Plane
    PointOnFace: Point3d
    SpecifyDirection: Direction
    Surface: ScCollector
    Type: Features.ShipDesign.RollingLineBuilder.Types


    class Types(enum.Enum):
        Manual = 0
        Pressure = 1
        Geodesic = 2
        SteppedPressure = 3
    

    class StartEvaluationTypes(enum.Enum):
        SheetMidpoint = 0
        PointOnFace = 1
        NewPoint = 2
    

    class ConstructionMethodTypes(enum.Enum):
        MarchingAngle = 0
        MarchingCurvature = 1
        ParallelPlane = 2
        MinimumCurvature = 3
        MaximumCurvature = 4
        Highlight = 5
        Asymptote = 6
    

class RollingLine(Features.CurveFeature):
    def __init__(self) -> None: ...


class ReverseSplitBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    IntersectionSeam: SelectNXObjectList


class RemoveSplitBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentSelection: SelectDisplayableObject
    SplitFeatureGroup: Features.Feature
    SplitParts: SelectNXObjectList


class ReferenceLineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FramePlane: SelectDatumPlaneList
    Offset: Expression
    ReferenceFace: ScCollector


class ReferenceLine(Features.CurveFeature):
    def __init__(self) -> None: ...


class RebaseBuilder(Builder):
    def __init__(self) -> None: ...
    def Rebase(self) -> int:
        ...
    DesignElementToRebase: SelectNXObjectList


class ReadDataSetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetDataSetNames(self, dataSetNames: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CreateDataSetToggle: bool
    DataSets: int
    NativeFileBrowser: str
    NativeToggle: bool


class QualifySketchBuilder(Builder):
    def __init__(self) -> None: ...
    def OpenRegistrationSpreadSheetToEdit(self) -> None:
        ...
    def ReloadRegisterSpreadSheet(self) -> None:
        ...
    def OpenPartFile(self) -> None:
        ...
    def ValidateCurves(self) -> None:
        ...
    def ValidateSketchCurves(self) -> None:
        ...
    def ValidatePartAttributes(self) -> None:
        ...
    def OpenParameterSpreadSheetToEdit(self) -> None:
        ...
    def ReloadParameterSpreadSheet(self) -> None:
        ...
    def ValidateParameterSpreadSheet(self) -> None:
        ...
    def ReloadTable(self) -> None:
        ...
    def UpdateSketch(self) -> None:
        ...
    def PreviewLeftImage(self) -> None:
        ...
    def PreviewRightImage(self) -> None:
        ...
    def CreateNewAnchorPoint(self) -> Features.ShipDesign.AnchorPoint:
        ...
    def AssignAttribute(self, entity: TaggedObject, category: str, title: str, value: str, attrType: int, objName: str) -> None:
        ...
    def RemoveAttribute(self, entity: TaggedObject, category: str, title: str, attrType: int) -> None:
        ...
    ActiveRowIndex: int
    BaseLine: SelectCurve
    ContextAttribute: int
    Feature: int
    ModelFile: str
    ModelList: Features.ShipDesign.AnchorPointList
    ModelPath: str
    MoldLine: SelectCurve
    OpposingMoldLine: SelectCurve
    SectionType: int
    ShearLine: SelectCurve
    ShipNo: int
    SpreadSheetFile: str
    SpreadSheetPath: str
    TaperLine: SelectCurve
    TopLine: SelectCurve


class ProjectStructureNode(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.Features.Industry.ProjectStructureNode.")"""
        ...
    def GetChildNodes(self, childNodes: typing.List[Features.ShipDesign.ProjectStructureNode]) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.Features.Industry.ProjectStructureNode.")"""
        ...
    Checked: bool
    CreateAsRootPart: bool
    SelectedSpecialization: str


class ProjectSetupBuilder(Builder):
    def __init__(self) -> None: ...
    def AddSharedParts(self, parts: typing.List[Part]) -> None:
        ...
    def GetRootNode(self) -> Features.ShipDesign.ProjectStructureNode:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.Features.ShipDesign.ProjectSetupBuilder.GetProjectRootNode.")"""
        ...
    def GetProjectRootNode(self) -> Features.Industry.ProjectStructureNode:
        ...
    def SetHullTemplateIdentifier(self, hullTemplateID: str) -> None:
        ...
    IsNewStructure: bool
    IsSaveAsSharePart: bool
    KeepFramebarEnabled: bool
    ProjectName: str


class ProfileTransitionBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngularTolerance: float
    Boundaries: ScCollector
    DistanceTolerance: float
    FeatureMode: Features.ShipDesign.ProfileTransitionBuilder.FeatureModeType
    MisalignedMode: Features.ShipDesign.ProfileTransitionBuilder.MisalignedModeType
    Spreadsheet: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    Targets: ScCollector


    class MisalignedModeType(enum.Enum):
        NotAllowed = 0
        ToBoundary = 1
        Bisect = 2
    

    class FeatureModeType(enum.Enum):
        Target = 0
        SeparateWebAndFace = 1
        SeparateFace = 2
    

class ProfileTransition(Features.BodyFeature):
    def __init__(self) -> None: ...


class ProfileSystemBuilder(Features.ShipDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    def SetBoundaryOnePoints(self, points: typing.List[Point3d]) -> None:
        ...
    def SetBoundaryTwoPoints(self, points: typing.List[Point3d]) -> None:
        ...
    def CreatePathCurves(self, curves: typing.List[NXObject]) -> None:
        ...
    def DeletePathCurves(self) -> None:
        ...
    def GetLastPathCurves(self, curves: typing.List[NXObject]) -> None:
        ...
    def DeleteLastPathCurves(self) -> None:
        ...
    def SetRegionPoints(self, points: typing.List[Point3d]) -> None:
        ...
    def CreatOrientationPathCurve(self) -> None:
        ...
    def UpdateEndcutChangeStatus(self, isChangeStart: bool, isChangeEnd: bool, isAllInBoudary: bool) -> None:
        ...
    Boundary1: SelectNXObjectList
    Boundary1Plane: Plane
    Boundary2: SelectNXObjectList
    Boundary2Plane: Plane
    BoundaryOneModified: bool
    BoundaryReverse: bool
    BoundaryTwoModified: bool
    FirstIntersectionPoints: SelectPointList
    ReversePathDirection: bool
    SecondIntersectionPoints: SelectPointList
    SplitKnuckleLocations: SelectPointList
    UseNewDefaultSectionAlgorithm: bool


class ProfileSystem(Features.CurveFeature):
    def __init__(self) -> None: ...


class ProfileSketchBuilder(Builder):
    def __init__(self) -> None: ...
    def AddSelectedProfile(self, part: TaggedObject) -> None:
        ...
    CreateAllProfilesSketch: bool
    CreateNewBooklet: bool
    RelatedBooklets: int


class ProfileListBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Component: SelectDisplayableObject
    CuttingInterfaceConfigFile: str
    CuttingInterfaceOutputFile: str
    IncludePlateTemplates: bool
    InverseBending: bool
    KnuckledProfile: bool
    ListFile: str
    ManufacturingCollector: Assemblies.SelectComponent
    OutputType: Features.ShipDesign.ProfileListBuilder.OutputTypes
    PartSet: Assemblies.SelectComponentList
    VentilationHoles: bool


    class OutputTypes(enum.Enum):
        ProfileList = 0
        XMLOut = 1
        All = 2
        PlateList = 3
    

class ProfileList(Features.BodyFeature):
    def __init__(self) -> None: ...


class ProfileCutoutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def FindOrientation(self) -> Features.ShipDesign.ProfileCutoutBuilder.Orientation:
        ...
    def SetDefaultScallopTypes(self, strProfileCutoutType: str) -> None:
        ...
    def RemoveSlaves(self) -> None:
        ...
    def ResetContextEntity(self, tgTargetBody: TaggedObject, tgProfileBody: TaggedObject) -> None:
        ...
    def EvaluateProfileCutoutParameters(self, tgTargetBody: TaggedObject, tgProfileBody: TaggedObject) -> None:
        ...
    def SynchronizeParametersWithProfileBody(self, tgProfileBody: TaggedObject) -> None:
        ...
    def UpdateScallopBuilder(self, pScallopBuilder: Features.ShipDesign.SteelFeatureSpreadsheetBuilder, tgTargetBody: TaggedObject, tgProfileBody: TaggedObject) -> None:
        ...
    AngularTolerance: float
    CollarPlateCreationApproach: Features.ShipDesign.ProfileCutoutBuilder.CollarPlateCreationApproaches
    CutoutData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    DistanceTolerance: float
    EnableCollarPlate: bool
    EnableCornerCut: bool
    EnableSquareCut: bool
    ManufacturingInformation: Features.ShipDesign.ManufacturingStockBuilder
    ManufacturingStock: Features.ShipDesign.ManufacturingStockBuilder
    MoldingSideScallop: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    MoldingSideScallopInUserControl: bool
    OpposingSideScallop: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    OpposingSideScallopInUserControl: bool
    ParametersInUserControl: bool
    ProfileBodies: SelectDisplayableObjectList
    SectionTypesInUserControl: bool
    TargetObjects: SelectDisplayableObjectList
    WeldCharacteristics: Weld.CharacteristicsBuilder


    class Orientation(enum.Enum):
        None = 0
        Normal = 1
        Flipped = 2
    

    class CollarPlateCreationApproaches(enum.Enum):
        Template = 0
        SteelFeature = 1
    

class ProfileCutout(Features.BodyFeature):
    def __init__(self) -> None: ...


class ProfileBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetAvailableAttributeNames(self) -> str:
        ...
    def GetAvailableAttributeMaterials(self) -> str:
        ...
    def GetAvailableBeltTypes(self) -> str:
        ...
    def GetAvailableBeltSizes(self) -> str:
        ...
    def GetAvailableProfileTypes(self) -> str:
        ...
    def GetAvailableProfileSizes(self) -> str:
        ...
    AngleOfRotation: Expression
    AngularTolerance: float
    AttributeMaterial: int
    AttributeName: int
    BeltAlignment: Features.ShipDesign.ProfileBuilder.Alignment
    BeltSize: int
    BeltType: int
    CurveLengthData: GeometricUtilities.CurveLengthData
    DistanceTolerance: float
    EndCutType: Features.ShipDesign.ProfileBuilder.EndCutOption
    EndEndCutBlock: EndCutBlockBuilder
    FaceOffsetExpression: Expression
    FaceOffsetVector: bool
    GuideOffsetExpression: Expression
    GuideOffsetVector: bool
    GuideSection: Section
    KeepFace: bool
    KeepGuide: bool
    OrientType: Features.ShipDesign.ProfileBuilder.OrientationOption
    OrientationVector: Direction
    PlateHeight: Expression
    PlateWIdth: Expression
    ProfileSize: int
    ProfileType: int
    SectionType: Features.ShipDesign.ProfileBuilder.SectionOption
    SelectCsys: Features.SelectFeatureList
    SelectFace: ScCollector
    StartEndCutBlock: EndCutBlockBuilder
    Type: Features.ShipDesign.ProfileBuilder.TypeOption


    class TypeOption(enum.Enum):
        Profile = 0
        Belt = 1
    

    class SectionOption(enum.Enum):
        Plate = 0
        Profile = 1
    

    class OrientationOption(enum.Enum):
        FaceNormal = 0
        DatumCsys = 1
        Vector = 2
    

    class EndCutOption(enum.Enum):
        None = 0
        Symmetric = 1
        TwoSided = 2
    

    class Alignment(enum.Enum):
        Center = 0
        GuideEdge = 1
        OppositeGuide = 2
    

class Profile(Features.BodyFeature):
    def __init__(self) -> None: ...


class PointPairBuilder(NXObject):
    def __init__(self) -> None: ...
    Point1: Point
    Point2: Point


class PointDimBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.PointDimBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.PointDimBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.PointDimBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.PointDimBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.PointDimBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.PointDimBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.PointDimBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.PointDimBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.PointDimBuilder, object2: Features.ShipDesign.PointDimBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.PointDimBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PointDimBuilder(NXObject):
    def __init__(self) -> None: ...
    Dimension: Expression
    ItemIndex: int
    Point: Point


class PlateSystemBuilder(Features.ShipDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    def SetRegionPoints(self, regionPoints: typing.List[Point3d]) -> None:
        ...
    def CreateRegionBody(self) -> Body:
        ...
    def DeleteRegionBody(self) -> None:
        ...
    def SetKnuckleEdges(self, knuckleEdges: typing.List[TaggedObject]) -> None:
        ...
    def SetSplitEdgeUpdateFlag(self, isSplitEdgeUpdate: bool) -> None:
        ...
    def CleanUpTemporaryCurves(self) -> None:
        ...
    def SetRegionIndex(self, indexArray: int) -> None:
        ...
    def DeletePreviewBody(self, bDelete: bool) -> None:
        ...
    def SetPreviewOption(self, bPreview: bool) -> None:
        ...
    BoundaryPlane: Plane
    BoundarySection: Section
    BoundarySheets: SelectNXObjectList
    Offset: Expression
    Primary: Features.ShipDesign.PlateSystemBuilder.StiffenerDirectionType
    PrimaryOnReference: Features.ShipDesign.PlateSystemBuilder.StiffenerDirectionType
    ProjectionDirection: GeometricUtilities.ProjectionOptions
    Regions: RegionPointList
    Secondary1: Features.ShipDesign.PlateSystemBuilder.StiffenerDirectionType
    Secondary1OnReference: Features.ShipDesign.PlateSystemBuilder.StiffenerDirectionType
    Secondary2: Features.ShipDesign.PlateSystemBuilder.StiffenerDirectionType
    Secondary2OnReference: Features.ShipDesign.PlateSystemBuilder.StiffenerDirectionType
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    SplitKnuckleEdges: SelectNXObjectList
    Stock: Features.ShipDesign.PlateStockBuilder
    ThicknessDirection: Features.ShipDesign.ThicknessDirectionBuilder
    Tightness: int
    Weld: Weld.CharacteristicsBuilder


    class StiffenerDirectionType(enum.Enum):
        FwdPortToInUp = 0
        AftStbdFrOutDn = 1
        FwdPortToInCtr = 2
        AftStbdFrOutCtr = 3
    

class PlateSystem(Features.BodyFeature):
    def __init__(self) -> None: ...


class PlateStockBuilder(Builder):
    def __init__(self) -> None: ...
    KnuckleRatio: float
    KnuckleSmoothAngle: float
    MassDensity: Expression
    MaterialGradeName: str
    MaterialGradeOption: int
    MaterialName: str
    MaterialOption: int
    OppositeThickness: Expression
    RestrictThicknessToMaterial: bool
    ThickenOption: Features.ShipDesign.PlateStockBuilder.ThickenOptions
    Thickness: Expression
    ThicknessOption: int
    ThicknessSourceOption: Features.ShipDesign.PlateStockBuilder.ThicknessSourceOptions
    ThicknessStr: str
    WeightRating: str


    class ThicknessSourceOptions(enum.Enum):
        File = 0
        List = 1
    

    class ThickenOptions(enum.Enum):
        SingleSided = 0
        TwoSided = 1
        Symmetric = 2
    

class PlatePreparationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def RemovePart(self, partName: str) -> None:
        ...
    def AddPart(self, partName: str) -> None:
        ...
    AngleTolerance: float
    CalculationMethod: int
    CoordinateSystem: CoordinateSystem
    DistanceTolerance: float
    Length: Expression
    Width: Expression
    XCount: Expression
    XDirectionType: int
    XWidth: Expression
    YCount: Expression
    YWidth: Expression


class PlatePreparation(Features.BodyFeature):
    def __init__(self) -> None: ...


class PlatePlaneListBuilder(Features.ShipDesign.PlaneListBuilder):
    def __init__(self) -> None: ...


class PlateDivideBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BlendRadius: float
    DistanceTolerance: float
    ExtendImprints: bool
    HoleDiameter: float
    RemoveBlends: bool
    RemoveOpenings: bool
    ToolSelect: SelectNXObjectList


class PlateDivide(Features.BodyFeature):
    def __init__(self) -> None: ...


class PlateChamferBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleOption: Features.ShipDesign.PlateChamferBuilder.AngleMethod
    AngularDimension: Expression
    ChamferBothSides: bool
    ChordalTolerance: float
    ClearanceTolerance: float
    Depth: Expression
    EndPlane: Plane
    OffsetOption: Features.ShipDesign.PlateChamferBuilder.OffsetMethod
    Ratio: Expression
    RestDepth: Expression
    ReverseDirection: bool
    SelectEdge: ScCollector
    SelectTarget: ScCollector
    SelectThinnerPlate: ScCollector
    SelectTool: ScCollector
    StartPlane: Plane
    Type: Features.ShipDesign.PlateChamferBuilder.Types
    UseLimits: bool


    class Types(enum.Enum):
        OnEdge = 0
        ToPlate = 1
    

    class OffsetMethod(enum.Enum):
        Depth = 0
        RestDepth = 1
        ThinnerPlate = 2
    

    class AngleMethod(enum.Enum):
        Angle = 0
        Ratio = 1
    

class PlateChamfer(Features.BodyFeature):
    def __init__(self) -> None: ...


class PlateBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateMoldFacePlane(self, moldFacePlane: Plane) -> Plane:
        ...
    def CreatePlaneForList(self) -> Features.ShipDesign.PlatePlaneListBuilder:
        ...
    def GetShowMigratedBody(self) -> bool:
        ...
    def SetShowMigratedBody(self, showMigratedBody: bool) -> None:
        ...
    def CreateRegions(self) -> typing.List[Body]:
        ...
    def DeleteRegions(self) -> None:
        ...
    def SetKnuckleEdges(self, knuckleEdges: typing.List[Edge]) -> None:
        ...
    def AddRegionPoint(self, regionPoint: Point3d) -> None:
        ...
    def RemoveRegionPoint(self, regionPoint: Point3d) -> None:
        ...
    def GetMultipleRegionPoints(self) -> typing.List[Point3d]:
        ...
    def MapRegionToRegionPoint(self, plateRegionString: str, regionPoint: Point3d) -> None:
        ...
    def RemoveAllRegionPoints(self) -> None:
        ...
    def CreatePlateBoundaryOptionBuilder(self) -> Features.ShipDesign.PlateBoundaryOptionBuilder:
        ...
    def SetPlateBoundaryTrimType(self, nItem: int, type: Features.ShipDesign.PlateBoundaryOptionBuilder.TrimTypes) -> None:
        ...
    def GetPlateBoundaryTrimType(self, nItem: int) -> Features.ShipDesign.PlateBoundaryOptionBuilder.TrimTypes:
        ...
    def AddMergeRegionPoint(self, regionPoint: Point3d) -> None:
        ...
    def RemoveMergeRegionPoint(self, regionPoint: Point3d) -> None:
        ...
    def UpdatePlateBoundaryOptionList(self, type: Features.ShipDesign.PlateBoundaryOptionBuilder.BoundaryTypes) -> None:
        ...
    AdoptionBodies: SelectBodyList
    AdoptionBodiesMoldFace: ScCollector
    BodyBoundary: SelectBodyList
    CurveBoundary: Section
    DistanceTolerance: float
    FacePlaneBoundary: ExpressionCollectorSetList
    FlipDirection: bool
    MergeRegions: SelectBodyList
    MoldFace: ScCollector
    MoldFaceOffset: Expression
    MoldFacePlane: Plane
    MoldFacePlaneValid: bool
    PlaneBoundaryList: Features.ShipDesign.PlaneListBuilderList
    PlateBoundaryOptionList: Features.ShipDesign.PlateBoundaryOptionBuilderList
    PlateStock: Features.ShipDesign.PlateStockBuilder
    ProjectDirection: GeometricUtilities.ProjectionOptions
    RegionOption: Features.ShipDesign.PlateBuilder.RegionOptions
    RegionPoint: Point3d
    Regions: SelectNXObjectList
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    SplitKnuckleEdges: SelectEdgeList
    Tightness: Features.ShipDesign.PlateBuilder.TightnessOptions
    Type: Features.ShipDesign.PlateBuilder.Types


    class Types(enum.Enum):
        Create = 0
        Adopt = 1
    

    class TightnessOptions(enum.Enum):
        NonTight = 0
        WaterTight = 1
        OilTight = 2
        AirTight = 3
    

    class RegionOptions(enum.Enum):
        All = 0
        InsideBody = 1
        OutsideBody = 2
    

    class BodyTypes(enum.Enum):
        SheetBody = 0
        SolidBody = 1
    

class PlateBoundaryOptionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.PlateBoundaryOptionBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.PlateBoundaryOptionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.PlateBoundaryOptionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.PlateBoundaryOptionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.PlateBoundaryOptionBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.PlateBoundaryOptionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.PlateBoundaryOptionBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.PlateBoundaryOptionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.PlateBoundaryOptionBuilder, object2: Features.ShipDesign.PlateBoundaryOptionBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.PlateBoundaryOptionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PlateBoundaryOptionBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryType: Features.ShipDesign.PlateBoundaryOptionBuilder.BoundaryTypes
    TrimType: Features.ShipDesign.PlateBoundaryOptionBuilder.TrimTypes


    class TrimTypes(enum.Enum):
        SquareCut = 0
        NeatTrim = 1
    

    class SplitKnuckleTypes(enum.Enum):
        Mitered = 0
        SquareCut = 1
    

    class BoundaryTypes(enum.Enum):
        Curve = 0
        Solid = 1
        FacePlane = 2
        KnuckleEdge = 3
    

class Plate(Features.BodyFeature):
    def __init__(self) -> None: ...


class PlanePairBuilder(NXObject):
    def __init__(self) -> None: ...
    Plane1: Plane
    Plane2: Plane


class PlaneListBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.PlaneListBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.PlaneListBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.PlaneListBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.PlaneListBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.PlaneListBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.PlaneListBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.PlaneListBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.PlaneListBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.PlaneListBuilder, object2: Features.ShipDesign.PlaneListBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.PlaneListBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PlaneListBuilder(Builder):
    def __init__(self) -> None: ...
    Plane: Plane
    Valid: bool


class PinjigDrawingBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPlatePartName(self, partName: str) -> None:
        ...


class PinJigBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AdditionalStructures: ScCollector
    DrawingSuffixName: str
    OrientationCsys: CoordinateSystem
    PinJigData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    Plates: ScCollector
    XDirectionEdge: SelectEdge


class PinJig(Features.BodyFeature):
    def __init__(self) -> None: ...


class PillarTreatmentBlockBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CapPlateStock: Features.ShipDesign.PlateStockBuilder
    CapStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    EndCut: Features.ShipDesign.EndCutBuilder
    TreatmentType: Features.ShipDesign.PillarBuilder.EndTreatmentTypes


class PillarSystemBuilder(Features.ShipDesign.ProfileSystemBuilder):
    def __init__(self) -> None: ...
    def CreatePointPairBuilder(self) -> Features.ShipDesign.PointPairBuilder:
        ...
    def PopulateAnchorPointList(self) -> None:
        ...
    def GetAvailableAnchorPointNames(self) -> str:
        ...
    AnchorPoint: int
    BuildSolid: bool
    BuiltUpStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    Direction: Direction
    EndCapPlateStock: Features.ShipDesign.PlateStockBuilder
    EndCapStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    EndCapThickness: Expression
    EndEndCut: Features.ShipDesign.EndCutBuilder
    EndTreatmentType: Features.ShipDesign.PillarBuilder.EndTreatmentTypes
    IntersectingShipStructure: SelectNXObjectList
    LimitingShipStructure: SelectNXObjectList
    OrientationAngle: Expression
    OrientationLine: SelectTaggedObject
    PointPairList: NXObjectList
    ReverseOrientationDirection: bool
    ReverseReferenceDirection: bool
    SectionType: Features.ShipDesign.PillarSystemBuilder.StockSectionType
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    StartCapPlateStock: Features.ShipDesign.PlateStockBuilder
    StartCapStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    StartCapThickness: Expression
    StartEndCut: Features.ShipDesign.EndCutBuilder
    StartTreatmentType: Features.ShipDesign.PillarBuilder.EndTreatmentTypes
    StockData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    Type: Features.ShipDesign.PillarSystemBuilder.Types


    class Types(enum.Enum):
        ShipStructure = 0
        Points = 1
    

    class StockSectionType(enum.Enum):
        Profile = 0
        BuiltUp = 1
    

class PillarSystem(Features.CurveFeature):
    def __init__(self) -> None: ...


class PillarBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetShowMigratedBody(self) -> bool:
        ...
    def SetShowMigratedBody(self, showMigratedBody: bool) -> None:
        ...
    def CreatePointPairBuilder(self) -> Features.ShipDesign.PointPairBuilder:
        ...
    def PopulateAnchorPointList(self) -> None:
        ...
    def GetAvailableAnchorPointNames(self) -> str:
        ...
    AdoptionBody: SelectTaggedObject
    AnchorPoint: int
    AngleTolerance: float
    AngularDim: Expression
    BuiltUpBlock: Features.ShipDesign.BuiltUpBlockBuilder
    CoordSystem: CoordinateSystem
    Direction: Direction
    DistanceTolerance: float
    EndCapPlateStock: Features.ShipDesign.PlateStockBuilder
    EndCapStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    EndCapThickness: Expression
    EndCutType: Features.ShipDesign.PillarBuilder.EndCutTypes
    EndEndCut: Features.ShipDesign.EndCutBuilder
    EndLimit: Features.ShipDesign.StiffenerLimitBuilder
    EndOffset: Expression
    EndPlane: Plane
    EndTreatmentType: Features.ShipDesign.PillarBuilder.EndTreatmentTypes
    EndTypeOption: Features.ShipDesign.PillarBuilder.EndTypeOptions
    GuideCurve: SelectTaggedObject
    IntersectingObjects: SelectNXObjectList
    Line1: SelectTaggedObject
    Line1Offset: Expression
    Line2: SelectTaggedObject
    Line2Offset: Expression
    MainStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    OrientationLine: SelectTaggedObject
    PlacementMethod: Features.ShipDesign.PillarBuilder.CreationMethod
    PointPairList: NXObjectList
    ReverseEndOffset: bool
    ReverseLine1Offset: bool
    ReverseLine2Offset: bool
    ReverseOrientationDirection: bool
    ReverseReferenceDirection: bool
    ReverseStartOffset: bool
    SectionType: Features.ShipDesign.PillarBuilder.StockSectionType
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    StartCapPlateStock: Features.ShipDesign.PlateStockBuilder
    StartCapStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    StartCapThickness: Expression
    StartEndCut: Features.ShipDesign.EndCutBuilder
    StartLimit: Features.ShipDesign.StiffenerLimitBuilder
    StartOffset: Expression
    StartPlane: Plane
    StartTreatmentType: Features.ShipDesign.PillarBuilder.EndTreatmentTypes
    SupportCapOptions: Features.ShipDesign.PillarBuilder.CapOptions


    class StockSectionType(enum.Enum):
        Profile = 0
        BuiltUp = 1
    

    class EndTypeOptions(enum.Enum):
        None = 0
        Endcut = 1
        Cap = 2
    

    class EndTreatmentTypes(enum.Enum):
        Endcut = 0
        Cap = 1
    

    class EndCutTypes(enum.Enum):
        None = 0
        Symmetric = 1
        TwoSided = 2
    

    class CreationMethod(enum.Enum):
        TwoPlanesandLines = 0
        SpecifyLine = 1
        SpecifyCsys = 2
        Adoption = 3
        Structure = 4
        Points = 5
    

    class CapOptions(enum.Enum):
        None = 0
        TwoSided = 1
        Symmetric = 2
    

class Pillar(Features.BodyFeature):
    def __init__(self) -> None: ...


class PhysicalCompartmentBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetParentNodeTag(self, parentNodeTag: TaggedObject) -> None:
        ...
    def GetParentNode(self) -> TaggedObject:
        ...
    BoundarySelection: SelectNXObjectList


class PhysicalCompartment(Features.BodyFeature):
    def __init__(self) -> None: ...


class PenetrationUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.ShipDesign.PenetrationManager) -> None: ...
    def CreatePenetrationSite(self, part: Part) -> Features.ShipDesign.PenetrationSite:
        ...
    def CreatePenetrationList(self, site: Features.ShipDesign.PenetrationSite) -> Features.ShipDesign.PenetrationList:
        ...
    def CreatePenetrationFolder(self, parent: Features.ShipDesign.PenetrationFolder) -> Features.ShipDesign.PenetrationFolder:
        ...
    def CreatePenetrationAttachment(self, site: Features.ShipDesign.PenetrationSite) -> Features.ShipDesign.PenetrationAttachment:
        ...
    def AskCurrentSite(self) -> Features.ShipDesign.PenetrationSite:
        ...
    def SetCurrentSite(self, site: Features.ShipDesign.PenetrationSite) -> None:
        ...
    def AskWorkingList(self) -> Features.ShipDesign.PenetrationList:
        ...
    def SetWorkingList(self, site: Features.ShipDesign.PenetrationSite, list: Features.ShipDesign.PenetrationList) -> None:
        ...
    def AskRequestLists(self, list: typing.List[Features.ShipDesign.PenetrationList]) -> None:
        ...
    def ReloadRequests(self, list: Features.ShipDesign.PenetrationList) -> None:
        ...
    def AskReferenceFolder(self, request: Features.ShipDesign.PenetrationRequest, refType: Features.ShipDesign.PenetrationUtils.Referencetype) -> Features.ShipDesign.PenetrationFolder:
        ...
    def AskAttachments(self, folder: Features.ShipDesign.PenetrationFolder, relation: str, attachments: typing.List[Features.ShipDesign.PenetrationAttachment]) -> None:
        ...
    def InsertAttachment(self, folder: Features.ShipDesign.PenetrationFolder, part: Part, name: str, relation: str) -> None:
        ...
    def RemoveAttachment(self, folder: Features.ShipDesign.PenetrationFolder, attachments: Features.ShipDesign.PenetrationAttachment) -> None:
        ...
    def AssociateRequests(self, requests: typing.List[Features.ShipDesign.PenetrationRequest]) -> None:
        ...
    def AskAssociateRequests(self, request: Features.ShipDesign.PenetrationRequest, requests: typing.List[Features.ShipDesign.PenetrationRequest]) -> None:
        ...
    def VerifyPenetrations(self, routingPart: typing.List[Part], states: typing.List[Features.ShipDesign.PenetrationUtils.RequestState], requests: typing.List[Features.ShipDesign.PenetrationRequest], reason: int) -> None:
        ...
    def AskRequestsOfPenetratedPart(self, part: Part, requests: typing.List[Features.ShipDesign.PenetrationRequest]) -> None:
        ...
    def AskRequestsOfPenetratingPart(self, part: Part, requests: typing.List[Features.ShipDesign.PenetrationRequest]) -> None:
        ...
    def SetRootPart(self, part: Part) -> None:
        ...
    def GetAttachmentPartsFromRequest(self, request: Features.ShipDesign.PenetrationRequest, relation: str, loadParts: bool, pParts: typing.List[Part]) -> None:
        ...
    def SaveRequests(self, eSaveRequestType: int, requests: typing.List[Features.ShipDesign.PenetrationRequest]) -> None:
        ...
    def SendToWorkflowRequests(self, requests: typing.List[Features.ShipDesign.PenetrationRequest]) -> None:
        ...
    def ReviewRequests(self, requests: typing.List[Features.ShipDesign.PenetrationRequest], pchReviewDecision: str, pchReviewComments: str, pchDueDate: str) -> None:
        ...
    def RequestCreateCutout(self, request: Features.ShipDesign.PenetrationRequest) -> None:
        ...
    def SetContextValues(self, rootPart: Part, workPart: Part, workView: View, workOcc: NXObject) -> None:
        ...
    def Tag(self) -> Tag: ...



    class RequestState(enum.Enum):
        New = 0
        Modified = 1
        NoChange = 2
        Deleted = 3
        PenetrationAttachOutOfDate = 4
    

    class Referencetype(enum.Enum):
        Penetrated = 0
        Penetrating = 1
        Reference = 2
        Subset = 3
        Implemented = 4
    

class PenetrationSite(Issue.IssueSite):
    def __init__(self) -> None: ...
    def RefreshSelectedList(self, listName: str, searchParts: typing.List[NXObject]) -> Features.ShipDesign.PenetrationList:
        ...


class PenetrationReviewRequestBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMultilineStringComments(self) -> str:
        ...
    def SetMultilineStringComments(self, multilineStringComments: str) -> None:
        ...
    DueDate: str
    ReviewDecisions: int


class PenetrationRequestForCutoutBuilder(Builder):
    def __init__(self) -> None: ...
    SelectionCutout: SelectNXObjectList


class PenetrationRequestCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.ShipDesign.PenetrationRequestBuilder]:
        ...
    def __init__(self, owner: Features.ShipDesign.PenetrationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePenetrationRequestBuilder(self, penetrationrequest: Features.ShipDesign.PenetrationRequest) -> Features.ShipDesign.PenetrationRequestBuilder:
        ...
    def CreatePenetrationCutoutBuilder(self, penetrationrequest: Features.ShipDesign.PenetrationRequest) -> Features.ShipDesign.PenetrationCutoutBuilder:
        ...
    def CreatePenetrationAssociationBuilder(self, isEditMode: bool, penetrationrequest: Features.ShipDesign.PenetrationRequest) -> Features.ShipDesign.PenetrationAssociationBuilder:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded function with enum instead.")"""
        ...
    def CreatePenetrationAssociationBuilder(self, type: Features.ShipDesign.PenetrationRequestBuilder.RequestDialogType, penetrationrequest: Features.ShipDesign.PenetrationRequest) -> Features.ShipDesign.PenetrationAssociationBuilder:
        ...
    def CreatePenetrationReviewRequestBuilder(self, requests: typing.List[Features.ShipDesign.PenetrationRequest]) -> Features.ShipDesign.PenetrationReviewRequestBuilder:
        ...
    def CreateVerifyPenetrationBuilder(self) -> Features.ShipDesign.VerifyPenetrationBuilder:
        ...
    def CreatePenetrationRequestForCutoutBuilder(self) -> Features.ShipDesign.PenetrationRequestForCutoutBuilder:
        ...
    def FindObject(self, name: str) -> NXObject:
        ...
    def Tag(self) -> Tag: ...



class PenetrationRequestBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRequestDescription(self) -> str:
        ...
    def SetRequestDescription(self, stringDesc: str) -> None:
        ...
    def AddAdjacentStructure(self, adjacentStructure: Body) -> None:
        ...
    def AddNonIntersectedStructure(self, structure: Body) -> None:
        ...
    def RemoveNonIntersectedStructures(self) -> None:
        ...
    def RemoveAllAdjacentStructures(self) -> None:
        ...
    def SetApplyOffset(self, applyOffset: bool) -> None:
        ...
    def SetOffsetValue(self, offsetValue: float) -> None:
        ...
    CompensationNumber: str
    CompensationType: Features.ShipDesign.PenetrationRequest.CompensationType
    CornerRadius: Expression
    CoutoutType: Features.ShipDesign.PenetrationRequest.CoutoutType
    Cut: bool
    DialogType: Features.ShipDesign.PenetrationRequestBuilder.RequestDialogType
    Diameter: Expression
    DirectionType: Features.ShipDesign.PenetrationRequest.DirectionType
    DueDate: str
    Hanger: bool
    HangerNumber: str
    Height: Expression
    HoleSubType: str
    HoleType: str
    HorizontalDirection: Direction
    ModifiedSketch: Sketch
    Offset: Expression
    Orientation: Direction
    PenetrationType: Features.ShipDesign.PenetrationRequest.PenetrationType
    Point: Point
    Radius: Expression
    RequestName: str
    RequestType: Features.ShipDesign.PenetrationRequest.RequestType
    RouteObjectCollector: SelectNXObjectList
    RoutePenetrating: SelectNXObjectList
    SelectedSegment: NXObject
    SelectionCompensation: SelectNXObject
    SelectionHanger: SelectNXObject
    SelectionStructure: SelectNXObject
    Sketch: Section
    Spill: bool
    Width: Expression


    class RequestDialogType(enum.Enum):
        Unknown = 0
        Create = 1
        Modify = 2
        Revise = 3
        Associate = 4
        EditAssociate = 5
        ReviseAssociate = 6
    

class PenetrationRequest(Issue.IssueContent):
    def __init__(self) -> None: ...


    class RequestType(enum.Enum):
        Single = 0
        Multiple = 1
    

    class PenetrationType(enum.Enum):
        PenetratingObject = 0
        PenetratingPoint = 1
    

    class DirectionType(enum.Enum):
        PerpendiculartoStructure = 0
        ParalleltoRoute = 1
        UserDefined = 2
    

    class CoutoutType(enum.Enum):
        Circular = 0
        Rectangular = 1
        FlatOval = 2
        UserDefined = 3
        ExistingSketch = 4
        NewSketch = 5
        None = 6
    

    class CompensationType(enum.Enum):
        NotRequired = 0
        Standard = 1
        NonStandard = 2
        Sleeve = 3
        DoubleSleeve = 4
        Flange = 5
    

class PenetrationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def Tag(self) -> Tag: ...

    PenetrationUtils: Features.ShipDesign.PenetrationUtils
    PenetrationRequestCollection: Features.ShipDesign.PenetrationRequestCollection


class PenetrationList(Issue.IssueList):
    def __init__(self) -> None: ...


class PenetrationFolder(Issue.IssueFolder):
    def __init__(self) -> None: ...


class PenetrationCutoutBuilder(Builder):
    def __init__(self) -> None: ...
    def AddNonIntersectedStructure(self, structure: Body) -> None:
        ...
    def RemoveNonIntersectedStructures(self) -> None:
        ...
    def SetDialogType(self, dialogType: Features.ShipDesign.PenetrationRequestBuilder.RequestDialogType) -> None:
        ...
    CornerRadius: Expression
    CoutoutType: Features.ShipDesign.PenetrationRequest.CoutoutType
    Diameter: Expression
    DirectionType: Features.ShipDesign.PenetrationRequest.DirectionType
    Height: Expression
    HoleSubType: str
    HoleType: str
    HorizontalDirection: Direction
    ModifiedSketch: Sketch
    Offset: Expression
    Orientation: Direction
    Radius: Expression
    Sketch: Section
    Width: Expression


class PenetrationAttachment(Issue.IssueAttachment):
    def __init__(self) -> None: ...


class PenetrationAssociationBuilder(Builder):
    def __init__(self) -> None: ...
    def ButtonCutout(self) -> None:
        ...
    def AddRequest(self, request: Features.ShipDesign.PenetrationRequest) -> None:
        ...
    def AddAdjacentStructure(self, adjacentStructure: Body) -> None:
        ...
    def AddNonIntersectedStructure(self, structure: Body) -> None:
        ...
    def RemoveNonIntersectedStructures(self) -> None:
        ...
    def AddSelectedCurve(self, curve: Body) -> None:
        ...
    def RemoveSelectedCurves(self) -> None:
        ...
    def SetCompensationPartNumber(self, selectionCompensationNumber: str) -> None:
        ...
    CornerRadius: Expression
    CoutoutType: Features.ShipDesign.PenetrationRequest.CoutoutType
    CutoutPart: Part
    Diameter: Expression
    DirectionType: Features.ShipDesign.PenetrationRequest.DirectionType
    Height: Expression
    IsEditMode: bool
    IsKeepAssociation: bool
    ModifiedSketch: Sketch
    Offset: Expression
    Point: Point
    Radius: Expression
    SketchSection: Section
    Width: Expression


class OrientationRegionItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.OrientationRegionItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.OrientationRegionItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.OrientationRegionItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.OrientationRegionItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.OrientationRegionItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.OrientationRegionItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.OrientationRegionItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.OrientationRegionItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.OrientationRegionItemBuilder, object2: Features.ShipDesign.OrientationRegionItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.OrientationRegionItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class OrientationRegionItemBuilder(Builder):
    def __init__(self) -> None: ...
    AngleMethods: Features.ShipDesign.OrientationAngleMethodsBuilder
    EndAngleMethods: Features.ShipDesign.OrientationAngleMethodsBuilder
    EndPointMethods: Features.ShipDesign.OrientationPointMethodsBuilder
    OrientationMethod: Features.ShipDesign.OrientationRegionItemBuilder.OrientationMethodTypes
    StartAngleMethods: Features.ShipDesign.OrientationAngleMethodsBuilder
    StartPointMethods: Features.ShipDesign.OrientationPointMethodsBuilder


    class OrientationMethodTypes(enum.Enum):
        NormalToSurface = 0
        Orthogonal = 1
        LinearTwist = 2
        CubicTwist = 3
        AlongVector = 4
        PlanarAtAngle = 5
    

class OrientationPointMethodsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Distance: Expression
    MeasureAlong: Features.ShipDesign.OrientationPointMethodsBuilder.MeasureAlongTypes
    PointMethod: Features.ShipDesign.OrientationPointMethodsBuilder.PointMethodTypes
    Reference: SelectNXObject
    SpecifyPoint: Point


    class PointMethodTypes(enum.Enum):
        ByPoint = 0
        ByDistance = 1
        FromStart = 2
        FromEnd = 3
    

    class MeasureAlongTypes(enum.Enum):
        Curve = 0
        Axis = 1
    

class OrientationDefinitionBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateNewRegion(self, regionPoint: NXObject) -> Features.ShipDesign.OrientationRegionItemBuilder:
        ...
    def DeleteRegion(self, region: Features.ShipDesign.OrientationRegionItemBuilder) -> None:
        ...
    def GetNextRegion(self, region: Features.ShipDesign.OrientationRegionItemBuilder) -> Features.ShipDesign.OrientationRegionItemBuilder:
        ...
    def CreatePathCurve(self, curves: typing.List[NXObject]) -> None:
        ...
    def SetPlacementFaces(self, faces: typing.List[DisplayableObject]) -> None:
        ...
    def CreateRegionsAtFrames(self, regions: typing.List[Features.ShipDesign.OrientationRegionItemBuilder]) -> None:
        ...
    def SetAnglesNormal(self, regions: typing.List[Features.ShipDesign.OrientationRegionItemBuilder]) -> None:
        ...
    AngleTolerance: float
    DistanceTolerance: float
    MeasureAngles: Features.ShipDesign.OrientationDefinitionBuilder.MeasureAngleTypes
    NewRegionPoint: SelectNXObject
    PlacementSide: Features.ShipDesign.OrientationDefinitionBuilder.PlacementSideTypes
    RegionItemData: Features.ShipDesign.OrientationRegionItemBuilder
    RegionList: Features.ShipDesign.OrientationRegionItemBuilderList
    ShowSurfaceAngles: bool
    ShowTwistRate: bool
    ShowWebAngles: bool


    class PlacementSideTypes(enum.Enum):
        SameAsNormal = 0
        OppositeNormal = 1
    

    class MeasureAngleTypes(enum.Enum):
        NormaltoCurve = 0
        Orthogonal = 1
    

class OrientationDefinition(Features.Feature):
    def __init__(self) -> None: ...


class OrientationAngleMethodsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlignAt: Features.ShipDesign.OrientationAngleMethodsBuilder.AlignAtTypes
    AlignVector: Direction
    AngleMethod: Features.ShipDesign.OrientationAngleMethodsBuilder.MethodTypes
    AngleReference: Plane
    MountingAngle: Expression


    class MethodTypes(enum.Enum):
        Angle = 0
        Vector = 1
        Aligned = 2
    

    class AlignAtTypes(enum.Enum):
        Start = 0
        End = 1
    

class NodeSelectionBuilder(Builder):
    def __init__(self) -> None: ...
    Nodes: SelectNXObjectList


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MoveToContainerBuilder(Builder):
    def __init__(self) -> None: ...
    DetailComponents: SelectDisplayableObjectList


class MirrorShipStructureBuilder(Builder):
    def __init__(self) -> None: ...
    def SortComponentByInterPartDependency(self, nonBreakableCircles: str, brokenCircles: str) -> int:
        ...
    AlgorithmVersion: Features.ShipDesign.MirrorShipStructureBuilder.VersionID
    AngularTolerance: float
    ApplicationType: Features.ShipDesign.MirrorShipStructureBuilder.AppTypes
    LinearToleranceFactor: float
    MirrorApproachOption: Features.ShipDesign.MirrorShipStructureBuilder.MirrorApproach
    MirrorPlane: Plane
    OriginalFeatures: Features.SelectFeatureList
    OriginalParts: Assemblies.SelectComponentList
    ReportMirrorResultXML: bool
    SelectionType: Features.ShipDesign.MirrorShipStructureBuilder.Types
    TargetPart: Assemblies.SelectComponentList


    class VersionID(enum.Enum):
        Undefined = 0
        Nx11 = 1
        Nx12 = 2
    

    class Types(enum.Enum):
        StructureSystem = 0
        Feature = 1
    

    class MirrorApproach(enum.Enum):
        CreateLinkedMirrorBody = 0
        CopySourceFeaturesAndReparent = 1
    

    class AppTypes(enum.Enum):
        ShipDetailDesign = 0
        ShipBasicDesign = 1
    

class MaterialEstimationBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFrameParts(self, nPartCount: int) -> Part:
        ...
    SelectionMethod: Features.ShipDesign.MaterialEstimationBuilder.SelectionMethods
    ShipStructures: SelectDisplayableObjectList
    VolumeBody: SelectBody


    class SelectionMethods(enum.Enum):
        Volume = 0
        Frame = 1
        ShipStructure = 2
    

class MaterialAllowanceBuilder(Builder):
    def __init__(self) -> None: ...
    AllowanceValue: float
    ValidFace: SelectNXObjectList


class MarkInsulationAreaBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: float
    BoundaryCurves: Section
    Color: NXColor
    Distance: float
    Pattern: str
    Tolerance: float
    Width: Annotations.LineWidth


class MarkingLineDesignBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetMarkingLineInformation(self, curve: ICurve, placementFaces: typing.List[Face], targetFaces: typing.List[Face]) -> None:
        ...
    def IsMarkingLineFeature(self, frecTag: Features.Feature) -> bool:
        ...
    AngleTolerance: float
    DistanceTolerance: float
    GridPlanes: SelectDisplayableObjectList
    Parts: Assemblies.SelectComponentList
    UseExistingCuttingSideFace: bool


class MarkingLineDesign(Features.Feature):
    def __init__(self) -> None: ...


class MarkingLineBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    CuttingSideFaces: ScCollector
    HideOriginal: bool
    Tolerance: float


class MarkingLine(Features.Feature):
    def __init__(self) -> None: ...


class ManufacturingStockBuilder(Builder):
    def __init__(self) -> None: ...
    def EditDataItem(self, name: str, eCheckBoxStatus: Features.ShipDesign.ManufacturingStockBuilder.CheckBoxStatus, valueNew: str) -> None:
        ...
    def InitializeDataFromDataSource(self, eDataSourceType: Features.ShipDesign.ManufacturingStockBuilder.StockDataSourceType, dataSource: str) -> None:
        ...
    DataSource: str
    DataSourceType: Features.ShipDesign.ManufacturingStockBuilder.StockDataSourceType


    class StockDataSourceType(enum.Enum):
        None = 0
        CustomerDefault = 1
    

    class ObjectType(enum.Enum):
        None = 0
        Edge = 1
        Face = 2
        Body = 3
        Feature = 4
        Part = 5
        Num = 6
    

    class LockedStatus(enum.Enum):
        Unlocked = 0
        Locked = 1
    

    class CheckBoxStatus(enum.Enum):
        Unchecked = 0
        Checked = 1
        Required = 2
    

class ManufacturingPreparationBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def InitializeDesignElementAttributes(self, designElement: DisplayableObject) -> None:
        ...
    def GetDesignElementAttributeValue(self, designElement: DisplayableObject, attrType: Features.ShipDesign.ManufacturingPreparationBuilder.AttributeType) -> str:
        ...
    def SetDesignElementAttributeValue(self, designElement: DisplayableObject, attrType: Features.ShipDesign.ManufacturingPreparationBuilder.AttributeType, attrValue: str) -> None:
        ...
    def UpdateSeamsMap(self, selectedComps: int) -> None:
        ...
    def GetComponentSeams(self, selectedComp: int) -> None:
        ...
    def FindIntersectingParts(self, intersectionParts: typing.List[Assemblies.Component]) -> None:
        ...
    def FilterDesignParts(self, designPartoccTags: typing.List[NXObject]) -> typing.List[NXObject]:
        ...
    AftStiffenerExtension: Expression
    AssemblyComponent: Assemblies.SelectComponent
    CreateTransientFeature: bool
    FeatureName: str
    ForwardStiffenerExtension: Expression
    Mirror: bool
    PartitionSchemeNotRequired: bool
    ReassignPositionNumbers: bool
    ReferenceFeatureName: str
    SaProject: str
    SeamingObjects: SelectTaggedObjectList
    SectionNumber: str
    SteelComponents: Assemblies.SelectComponentList
    TargetSeamObjects: SelectTaggedObjectList
    Trim: bool


    class AttributeType(enum.Enum):
        SaName = 0
        SaType = 1
        SaSize = 2
        SaMaterial = 3
        SaForm = 4
        SaDescription = 5
    

class ManufacturingPreparation(Features.CurveFeature):
    def __init__(self) -> None: ...


class ManufacturingOutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetParts(self, parts: typing.List[NXObject]) -> None:
        ...
    Component: SelectDisplayableObject
    ConfigFile: str
    ManufacturingCollector: Assemblies.SelectComponent
    MarkOnlySection: Section
    OutputFile: str
    OutputType: Features.ShipDesign.ManufacturingOutBuilder.OutputTypes
    ProfileXmlOutputFile: str


    class OutputTypes(enum.Enum):
        Plate = 0
        Profile = 1
    

class ManufacturingOut(Features.BodyFeature):
    def __init__(self) -> None: ...


class ManufacturingDataBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateMfgData(self) -> int:
        ...
    DesignElementToGenMfgData: SelectNXObjectList


class ManufacturingAssemblyNavigatorBuilder(Builder):
    def __init__(self) -> None: ...
    def DistributeWelds(self, containerOccTag: NXObject) -> None:
        ...
    def RemoveComponent(self, containerOccTag: NXObject) -> None:
        ...
    def CreateChild(self, containerOccTag: NXObject, containerType: Features.ShipDesign.ManufacturingAssemblyNavigatorBuilder.ContainerType) -> NXObject:
        ...
    def CreateMasterContainer(self, containerName: str) -> NXObject:
        ...
    def CreateMasterContainer(self, containerName: str, parentPartOccTag: NXObject) -> NXObject:
        ...
    def MoveComponents(self, containerOccTag: NXObject, partOccsToMove: typing.List[NXObject]) -> None:
        ...
    def SetOrientation(self, containerOccTag: NXObject, orientationType: Features.ShipDesign.ManufacturingAssemblyNavigatorBuilder.OrientationType) -> None:
        ...
    def SetOrientationUpFace(self, containerOccTag: NXObject, upFace: TaggedObject) -> None:
        ...
    def ExportToXML(self, masterContainerPartOccTag: NXObject) -> None:
        ...
    def SetManufacturingAttribute(self, componentTag: NXObject, attrName: str, attrValue: str) -> None:
        ...
    def SetContainerName(self, componentTag: NXObject) -> None:
        ...
    def SetContainerMass(self, componentTag: NXObject) -> None:
        ...
    def SetContainerCenterOfGravity(self, componentTag: NXObject) -> None:
        ...
    def SetContainerWeldLength(self, componentTag: NXObject) -> None:
        ...
    def CreateCustomView(self, componentTag: NXObject) -> None:
        ...
    def SetNavigatorRootComponent(self, componentTag: NXObject) -> None:
        ...
    def DefinePanels(self, masterContainerName: str) -> None:
        ...
    def GetSuperPlate(self) -> NXObject:
        ...
    def CreateSuperPlate(self, sourcePartOccs: typing.List[NXObject]) -> None:
        ...
    def GetSuperPlateName(self) -> str:
        ...
    def SetSuperPlateName(self, superPlateName: str) -> None:
        ...
    def GetSuperPlateContainerName(self) -> str:
        ...
    def SetSuperPlateContainerName(self, superPlateContainerName: str) -> None:
        ...
    def SetSuperPlateContainer(self, partTag: NXObject) -> None:
        ...
    def GetSuperPlateContainer(self) -> NXObject:
        ...


    class OrientationType(enum.Enum):
        Aft = 0
        Starboard = 1
        Up = 2
        Forward = 3
        Port = 4
        Down = 5
        Custom = 6
    

    class ContainerType(enum.Enum):
        Structure = 0
        Weld = 1
    

class MainDimensionsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AftPerpendicular: Expression
    Baseline: Expression
    ForwardPerpendicular: Expression
    GridID: str
    Midship: Expression
    ShipBody: SelectBody
    Waterline: Expression
    XMax: Expression
    XMin: Expression
    YMax: Expression
    ZMax: Expression
    ZMin: Expression


class MainDimensions(Features.BodyFeature):
    def __init__(self) -> None: ...


class LongitudinalBulkheadBuilder(Features.ShipDesign.PlateSystemBuilder):
    def __init__(self) -> None: ...
    ExtrusionLimit: Plane
    MoldFacePlane: Plane
    MoldFacePlaneList: Features.ShipDesign.PlaneListBuilderList
    MoldFacePlanes: SelectDatumPlaneList
    MoldFaceSection: Section
    MoldFaceSheet: SelectBody
    Type: Features.ShipDesign.LongitudinalBulkheadBuilder.Types


    class Types(enum.Enum):
        SheetBody = 0
        Planes = 1
        Extrusion = 2
    

class LongitudinalBulkhead(Features.BodyFeature):
    def __init__(self) -> None: ...


class LabellingRoomsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPmiNoteTags(self, pmiNoteTags: typing.List[Annotations.PmiNote]) -> None:
        ...
    Associativity: bool
    ExsitingLabelOption: Features.ShipDesign.LabellingRoomsBuilder.ExisingLabelOptions
    RoomsSelection: Assemblies.SelectComponentList


    class ExisingLabelOptions(enum.Enum):
        Preserve = 0
        Delete = 1
    

class KnuckledProfilesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    TabNoteGroup: Features.TabNoteCfgBuilder


class KnuckledProfiles(Features.BodyFeature):
    def __init__(self) -> None: ...


class ItFramesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateInterTransverseFrameListItem(self) -> Features.ShipDesign.ItFrameListItemBuilder:
        ...
    InterTransverseFrameList: Features.ShipDesign.ItFrameListItemBuilderList


class ItFrames(Features.BodyFeature):
    def __init__(self) -> None: ...


class ItFrameListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.ItFrameListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.ItFrameListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.ItFrameListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.ItFrameListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.ItFrameListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.ItFrameListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.ItFrameListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.ItFrameListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.ItFrameListItemBuilder, object2: Features.ShipDesign.ItFrameListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.ItFrameListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ItFrameListItemBuilder(NXObject):
    def __init__(self) -> None: ...
    EndFrameName: str
    NumberOfFrames: int
    StartFrameName: str


class InverseBendingLinesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetFailedProfiles(self, failedReasons: int) -> typing.List[Body]:
        ...
    DrawVentHoles: bool
    Extension: Expression
    FillingCoefficient: float
    GridSpacing: Expression
    LowerMargin: Expression
    MaxNumberOfCurves: int
    Measure: Features.ShipDesign.InverseBendingLinesBuilder.MeasureType
    Method: Features.ShipDesign.InverseBendingLinesBuilder.MethodType
    NeutralAxisPercent: float
    NeutralMethod: Features.ShipDesign.InverseBendingLinesBuilder.NeutralMethodType
    NonlinearityCoefficient: float
    NumberOfCurves: int
    NumberOfRows: int
    OffsetBetweenDiagrams: float
    Overlap: Expression
    ProfileBodies: SelectBodyList
    ReferencePlane: Features.ShipDesign.InverseBendingLinesBuilder.ReferencePlaneType
    ReferencePlanePoint: Point
    SideMargin: Expression
    UpperMargin: Expression
    UserCsys: CoordinateSystem
    VarMarginIncrement: Expression
    VarMarginMax: Expression
    VarMarginMin: Expression
    VarOverlapMax: int
    VarOverlapMin: int


    class ReferencePlaneType(enum.Enum):
        XCYCPlane = 0
        YCZCPlane = 1
        ZCXCPlane = 2
        NegativeXCYCPlane = 3
        NegativeYCZCPlane = 4
        NegativeZCXCPlane = 5
        DefineCSYS = 6
    

    class NeutralMethodType(enum.Enum):
        BaseLine = 0
        CenterLine = 1
        NeutralAxis = 2
    

    class MethodType(enum.Enum):
        Automatic = 0
        NumberOfCurves = 1
        FillingCoefficient = 2
        EvenFit = 3
    

    class MeasureType(enum.Enum):
        LeftToRight = 0
        RightToLeft = 1
    

class InverseBendingLines(Features.CurveFeature):
    def __init__(self) -> None: ...


class InteractiveAnnotationTableBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSelectPoint(self, pos: float) -> None:
        ...
    def CreateTable(self) -> Annotations.Table:
        ...
    def DeleteExistTable(self) -> None:
        ...
    TableList: int
    ViewPlan: str
    ViewScope: Features.ShipDesign.InteractiveAnnotationTableBuilder.ViewScopeOptions
    ViewSelect: Drawings.SelectDraftingViewList


    class ViewScopeOptions(enum.Enum):
        ActiveSheet = 0
        AllSheets = 1
        SelectedView = 2
    

class InteractiveAnnotationSubBaseBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateAnnotation(self) -> Annotations.Annotation:
        ...


class InteractiveAnnotationReferenceLinesBuilder(Features.ShipDesign.InteractiveAnnotationSubBaseBuilder):
    def __init__(self) -> None: ...
    Baseline: bool
    BaselineColor: NXColor
    BaselineFont: DisplayableObject.ObjectFont
    BaselineWidth: Annotations.LineWidth
    Centerline: bool
    CenterlineColor: NXColor
    CenterlineFont: DisplayableObject.ObjectFont
    CenterlineWidth: Annotations.LineWidth
    ViewListWithCandidateViewList: Drawings.SelectDraftingViewList


class InteractiveAnnotationDeckBulkheadBuilder(Features.ShipDesign.InteractiveAnnotationSubBaseBuilder):
    def __init__(self) -> None: ...
    def GetSymbolText(self, symbolTexts: str) -> None:
        ...
    def SetSymbolText(self, symbolTexts: str) -> None:
        ...
    Direction: Features.ShipDesign.InteractiveAnnotationDeckBulkheadBuilder.DirectionType
    ReferenceObject: NXObject


    class DirectionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

class InteractiveAnnotationBuilder(Builder):
    def __init__(self) -> None: ...
    def AddAnnotationOfStructureIdAndScantling(self, createIDAnnotation: bool, createScantlingAnnotation: bool, draftingBody: Drawings.DraftingBody) -> None:
        ...
    def AddAnnotationOfEndCuts(self, createEndCutsSymbol: bool, draftingBody: Drawings.DraftingBody) -> None:
        ...
    def AddAnnotationOfOpeningFillingLine(self, createOpeningFillingLine: bool, draftingbody: Drawings.DraftingBody) -> None:
        ...
    def AddAnnotationOfBracket(self, createBracketSymbol: bool, draftingbody: Drawings.DraftingBody) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use JA_INTERACTIVE_ANNOTATION_BUILDER_HandleAnnotationOfBracket instead.")"""
        ...
    def AddAnnotationOfSeamForDetailDesign(self, createSeamSymbol: bool, tgView: Drawings.DraftingView, objects: typing.List[Drawings.DraftingBody], selectedObjecty: Drawings.DraftingBody) -> None:
        ...
    def HandleSeamForNonSectionedPlateForBasicDesign(self, createSeamSymbol: bool, draftingVDCurve: Drawings.DraftingCurve, tgCurve: NXObject) -> None:
        ...
    def HandleSeamForSectionedPlateForBasicDesign(self, createSeamSymbol: bool, tgDraftingBody: Drawings.DraftingBody, objects: typing.List[Drawings.DraftingCurve], selectedObject: Drawings.DraftingCurve) -> None:
        ...
    def AddAnnotationOfExpansionStiffenerSturctureIdAndScantling(self, tgView: Drawings.DraftingView, shipStructure: NXObject, createIDAnnotation: bool, createScantlingAnnotation: bool) -> None:
        ...
    def AddAnnotationOfExpansionStiffenerEndCuts(self, tgView: Drawings.DraftingView, shipStructure: NXObject, createEndCutsSymbol: bool) -> None:
        ...
    def AddAnnotationOfExpansionPlate(self, tgView: Drawings.DraftingView, shipStructure: NXObject, createScantlingAnnotation: bool) -> None:
        ...
    def HandleAnnotationForBasicDesign(self, createIDAnnotation: bool, createScantlingAnnotation: bool, createEndCutsAnnotation: bool, draftingVDCurve: Drawings.DraftingCurve, shipEntity: NXObject, view: Drawings.DraftingView) -> NXObject:
        """[Obsolete("Deprecated in NX1980.0.0.  Use JA_INTERACTIVE_ANNOTATION_BUILDER_HandleAnnotationsForBasicDesign instead.")"""
        ...
    def AddFillingLineByChain(self, curves: typing.List[Drawings.DraftingCurve], createChainAnnotation: bool) -> None:
        ...
    def AddFillingLineByPoints(self, spiderPoint: Point, strikingPoint: Point) -> Line:
        ...
    def ModifyFillingLineByPoints(self, spiderPoint: Point, strikingPoint: Point, line: Line) -> None:
        ...
    def DeleteExistingAnnotations(self) -> None:
        ...
    def DeleteOpeningFillingLine(self, line: Line) -> None:
        ...
    def SetTableIndex(self, inx: int) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use Features.ShipDesign.InteractiveAnnotationTableBuilder.SetTableIndex() instead.")"""
        ...
    def SetPosition(self, pos: float) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use Features.ShipDesign.InteractiveAnnotationTableBuilder.SetSelectPoint() instead.")"""
        ...
    def CreateTable(self) -> Annotations.Table:
        """[Obsolete("Deprecated in NX1872.0.0.  Use Features.ShipDesign.InteractiveAnnotationBuilder.TableDefinition.CreateTable() instead.")"""
        ...
    def CreateTableByViewPlan(self, viewPlan: str) -> Annotations.Table:
        """[Obsolete("Deprecated in NX1872.0.0.  Use Features.ShipDesign.InteractiveAnnotationBuilder.TableDefinition.CreateTable() instead.")"""
        ...
    def GetTableIndex(self) -> int:
        """[Obsolete("Deprecated in NX1872.0.0.  Use Features.ShipDesign.InteractiveAnnotationBuilder.TableDefinition.GetTableIndex() instead.")"""
        ...
    def DeleteLines(self, curves: typing.List[Drawings.DraftingCurve]) -> None:
        ...
    def AddFillingLinesByModelBody(self, draftingbody: Drawings.DraftingBody, curves: typing.List[Drawings.DraftingCurve]) -> bool:
        ...
    def AddAnnotationOfFireAndSafetyPlan(self, bCreate: bool, tgView: Drawings.DraftingView, tgComponent: Assemblies.Component) -> None:
        ...
    def UpdateSymbolPart(self) -> Annotations.BaseCustomSymbol:
        ...
    def AddAnnotationOfWeldSeamForDetailDesign(self, createSeamSymbol: bool, draftingVDCurve: Drawings.DraftingCurve, tgCurve: NXObject) -> None:
        ...
    def DisplayShipTicPositionSymbol(self, bShow: bool, tgShipTic: DisplayableObject) -> None:
        ...
    def DisplayShipTicThicknessSymbol(self, bShow: bool, tgShipTic: DisplayableObject) -> None:
        ...
    def UpdateMFGViewState(self, tgView: Drawings.DraftingView) -> None:
        ...
    def AddAnnotationOfCollarPlate(self, createCollarPlateSymbol: bool, draftingbody: Drawings.DraftingBody) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use JA_INTERACTIVE_ANNOTATION_BUILDER_HandleAnnotationOfCollarPlate instead.")"""
        ...
    def AddCSYSSymbol(self, createCSYSSymbol: bool, tgView: Drawings.DraftingView) -> None:
        ...
    def UpdateDefultGrades(self, defaultGrades: str) -> None:
        ...
    def HandleAnnotationOfBracket(self, bScantling: bool, bStructureId: bool, draftingbody: Drawings.DraftingBody) -> None:
        ...
    def HandleAnnotationOfCollarPlate(self, bScantling: bool, bStructureId: bool, draftingbody: Drawings.DraftingBody) -> None:
        ...
    def HandleAnnotationOfSectionSymbol(self, createSectionSymbol: bool, draftingBody: Drawings.DraftingBody) -> None:
        ...
    def HandleAnnotationsForBasicDesign(self, createIDAnnotation: bool, createScantlingAnnotation: bool, createEndCutsAnnotation: bool, createCrossSectionAnnotation: bool, draftingVDCurve: Drawings.DraftingCurve, shipEntity: NXObject, view: Drawings.DraftingView) -> NXObject:
        ...
    def HandleShipCoordinateSymbol(self, createSymbol: bool, tgPoint: Point, bShipGridCoordinate: bool) -> None:
        ...
    def GetReferenceLines(self) -> Features.ShipDesign.InteractiveAnnotationReferenceLinesBuilder:
        ...
    def GetDeckBulkhead(self) -> Features.ShipDesign.InteractiveAnnotationDeckBulkheadBuilder:
        ...
    def HandleShipCoordinateSymbolWithToggles(self, createSymbol: bool, tgPoint: Point, bShipGridCoordinate: bool, bCreateX: bool, bCreateY: bool, bCreateZ: bool) -> None:
        ...
    def HandleShipCoordinateSymbolWithToggles2(self, createSymbol: bool, tgView: Drawings.DraftingView, pointIdentityString: str, bShipGridCoordinate: bool, bCreateX: bool, bCreateY: bool, bCreateZ: bool) -> None:
        ...
    FireAndSafetyPlanMethod: int
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder
    Scale: Expression
    ShipType: int
    Style: Annotations.StyleBuilder
    SymbolType: int
    TableDefinition: Features.ShipDesign.InteractiveAnnotationTableBuilder
    ViewListWithCandidateViewList: Drawings.SelectDraftingViewList


class InsertSheetBodyBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    FramePlane: SelectDatumPlane
    FrameSheet: SelectBodyList
    ReplacedBulkheadColor: NXColor
    ReplacedDeckColor: NXColor


class InsertSheetBody(Features.BodyFeature):
    def __init__(self) -> None: ...


class InsertFramesBuilder(Features.ShipDesign.TransFrameBuilder):
    def __init__(self) -> None: ...
    StartFrameName: str
    Type: Features.ShipDesign.InsertFramesBuilder.Types


    class Types(enum.Enum):
        Transverse = 0
        LongitudnalZ = 1
        LongitudnalY = 2
    

class ImportStructureXMLBuilder(Builder):
    def __init__(self) -> None: ...
    StructureXMLFile: str


class HullBuilder(Features.ShipDesign.PlateSystemBuilder):
    def __init__(self) -> None: ...
    Centerline: Plane
    MoldFaceSheet: SelectBody
    MoldFaces: ScCollector
    Type: Features.ShipDesign.HullBuilder.Types


    class Types(enum.Enum):
        SheetBody = 0
        Faces = 1
    

class Hull(Features.BodyFeature):
    def __init__(self) -> None: ...


class GenericPlateSystemBuilder(Features.ShipDesign.PlateSystemBuilder):
    def __init__(self) -> None: ...
    MoldFacePlaneList: Features.ShipDesign.PlaneListBuilderList
    MoldFacePlanes: SelectDatumPlaneList
    MoldFaceSheet: SelectBody
    Type: Features.ShipDesign.GenericPlateSystemBuilder.Types


    class Types(enum.Enum):
        SheetBody = 0
        Planes = 1
    

class GenericPlateSystem(Features.BodyFeature):
    def __init__(self) -> None: ...


class GeneralArrangementViewBuilder(Builder):
    def __init__(self) -> None: ...
    def SetViewPosition(self, xPosition: float, yPosition: float) -> None:
        ...
    def GetSelectedModelViewNames(self, modelViewNames: str) -> None:
        ...
    def SetSelectedModelViewNames(self, modelViewNames: str) -> None:
        ...
    AlignmentType: Features.ShipDesign.GeneralArrangementViewBuilder.ViewAlignmentType
    Decks: Features.ShipDesign.DeckListBuilder
    DrawingSheet: Drawings.DrawingSheet
    EndFrame: NXObject
    EndFrameOffset: float
    FrameAlignment: SelectNXObject
    InheritedPMISource: Features.ShipDesign.GeneralArrangementViewBuilder.InheritedPMISourceOption
    MasterView: Drawings.SelectDraftingView
    Placement: Drawings.ViewPlacementBuilder
    Scale: float
    SelectStructures: Features.ShipDesign.SelectStructuresBuilder
    SelectedModelView: SelectModelingViewList
    SourcePart: TaggedObject
    StartFrame: NXObject
    StartFrameOffset: float
    ViewCreation: Features.ShipDesign.GeneralArrangementViewBuilder.ViewCreationType
    ViewDirection: Features.ShipDesign.GeneralArrangementViewBuilder.ViewDirectionType
    ViewName: str
    ViewStyle: Drawings.ViewStyleBuilder
    ViewType: str


    class ViewDirectionType(enum.Enum):
        XPositive = 0
        XNegative = 1
        YPositive = 2
        YNegative = 3
        ZPositive = 4
        ZNegative = 5
        Deck = 6
    

    class ViewCreationType(enum.Enum):
        ProjectView = 0
        SectionView = 1
    

    class ViewAlignmentType(enum.Enum):
        Frame = 0
        Automatically = 1
        NoAlignment = 2
    

    class InheritedPMISourceOption(enum.Enum):
        NoChange = 0
        None = 1
        FromGARoot = 2
        FromGAContainer = 3
        FromGADrawing = 4
        FromDeckContainers = 5
        FromSourcePart = 6
    

class FrameBarOutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ConfigFile: str
    OutputFile: str


class FrameBarOut(Features.BodyFeature):
    def __init__(self) -> None: ...


class FilterBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAvailableProperties(self, properties: str) -> None:
        ...
    def GetPropertyStatus(self, property: str) -> bool:
        ...
    def SetPropertyStatus(self, property: str, onOrOff: bool) -> None:
        ...
    def FreeAvailableProperties(self, properties: str) -> None:
        ...
    def IsObjectValid(self, object: NXObject) -> bool:
        ...
    CompareObject: TaggedObject


class FeaturesToTagBuilder(Builder):
    def __init__(self) -> None: ...
    def ManageFeatureTag(self, addMark: bool, featureToMark: Features.Feature) -> None:
        ...
    FeatureToTag: Features.SelectFeatureList


class FeaturesBatchOperationBuilder(Builder):
    def __init__(self) -> None: ...
    def ClearFeatureTypes(self) -> None:
        ...
    def AddFeatureType(self, featureType: str) -> None:
        ...
    ConfigurationFile: str
    Parts: SelectPartList
    Type: Features.ShipDesign.FeaturesBatchOperationBuilder.Types


    class Types(enum.Enum):
        Delete = 0
        Hide = 1
        Show = 2
        Create = 3
    

class FeatureParmsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreatePlaneForList(self) -> Features.ShipDesign.PlaneListBuilder:
        ...
    AngleTolerance: float
    DistanceTolerance: float
    OrientationAngleRule: Features.ShipDesign.FeatureParmsBuilder.OrientationAngleRuleTypes


    class OrientationAngleRuleTypes(enum.Enum):
        RightHand = 0
        ShipOrientation = 1
    

class ExportStructureXMLBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPartOperationBuilder(self, partOperationBuilder: PDM.PartOperationCreateBuilder) -> None:
        ...
    def SetStructureParts(self, structurePartFilenames: str) -> None:
        ...
    ExportFormat: Features.ShipDesign.ExportStructureXMLBuilder.ExportFormats
    SectionBodies: ScCollector
    StructureXMLFile: str
    Type: Features.ShipDesign.ExportStructureXMLBuilder.Types


    class Types(enum.Enum):
        Section = 0
        Structure = 1
    

    class ExportFormats(enum.Enum):
        ShipPLMXML = 0
        Dnvglocxxml = 1
    

class ExpansionDrawingBuilder(Builder):
    def __init__(self) -> None: ...
    AftPlane: Plane
    BasePlane: Plane
    BasicDesignMode: bool
    DrawingTemplate: Features.ShipDesign.DrawingTemplateBuilder
    EnglishScale: Features.ShipDesign.ExpansionDrawingBuilder.JaExpansiondrawingbuilderEnglishScale
    ForePlane: Plane
    IsEdit: bool
    MetricScale: Features.ShipDesign.ExpansionDrawingBuilder.JaExpansiondrawingbuilderMetricScale
    PlatesToExpand: SelectNXObjectList
    ScaleDenominator: float
    ScaleNumerator: float
    Tolerance: float
    UpperPlane: Plane


    class JaExpansiondrawingbuilderMetricScale(enum.Enum):
        S501 = 0
        S201 = 1
        S101 = 2
        S51 = 3
        S21 = 4
        S11 = 5
        S12 = 6
        S15 = 7
        S110 = 8
        S120 = 9
        S150 = 10
        S1100 = 11
        Custom = 12
        Default = 13
    

    class JaExpansiondrawingbuilderEnglishScale(enum.Enum):
        S81 = 0
        S41 = 1
        S21 = 2
        S11 = 3
        S12 = 4
        S14 = 5
        S18 = 6
        Custom = 7
        Default = 8
    

class ExpansionDrawing(Features.CurveFeature):
    def __init__(self) -> None: ...


class ExcessMaterialBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    EndOffset: Expression
    ExtendEndFace: bool
    ExtendStartFace: bool
    OffsetDistance: Expression
    OffsetType: Features.ShipDesign.ExcessMaterialBuilder.Offset
    SelectFace: SelectFace
    SelectFaces: ScCollector
    StartOffset: Expression
    Type: Features.ShipDesign.ExcessMaterialBuilder.Types
    Version: Features.ShipDesign.ExcessMaterialBuilder.VersionID


    class VersionID(enum.Enum):
        Original = 0
        Nx902 = 1
    

    class Types(enum.Enum):
        ExcessMaterial = 0
        FitUp = 1
    

    class Offset(enum.Enum):
        Constant = 0
        LinearVarying = 1
    

class ExcessMaterial(Features.BodyFeature):
    def __init__(self) -> None: ...


class ExamineSteelFeatureBuilderResult(enum.Enum):
    NoCheck = 0
    Pass = 1
    Fail = 2
    NoResult = 3


class ExamineSteelFeatureBuilderCheck(enum.Enum):
    ProfileWidth = 0
    CutoutToHole = 1
    CutoutToSeam = 2
    CutoutClearance = 3
    CutoutAngle = 4
    StandardInterference = 5
    CollarPlateToSeam = 6
    CollarPlateToHole = 7
    WideCollarPlate = 8
    NumChecks = 9


class ExamineSteelFeatureBuilder(Builder):
    def __init__(self) -> None: ...
    def SetCheck(self, check: Features.ShipDesign.ExamineSteelFeatureBuilderCheck, status: bool) -> None:
        ...
    def GetCheckResult(self, check: Features.ShipDesign.ExamineSteelFeatureBuilderCheck) -> Features.ShipDesign.ExamineSteelFeatureBuilderResult:
        ...
    def HighlightCheckResult(self, check: Features.ShipDesign.ExamineSteelFeatureBuilderCheck, highlight: bool) -> None:
        ...
    def Examine(self) -> None:
        ...
    def DisplayInformation(self) -> None:
        ...
    SelectObject: SelectDisplayableObjectList


class EndCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def InheritParametersFromEndcutFace(self, endcutFace: Face) -> None:
        ...
    def UpdateContextEntity(self, tEntity: NXObject) -> None:
        ...
    ConnectionType: Features.ShipDesign.EndCutBuilder.ConnectionTypes
    DraftAngle: Expression
    DraftOffset: Expression
    DraftType: Features.ShipDesign.EndCutBuilder.DraftTypes
    EndFaceType: Features.ShipDesign.EndCutBuilder.EndFaceTypes
    FlangeBoundary: SelectBody
    FlangeSketchData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    LimitGeometry: SelectDisplayableObject
    LimitType: Features.ShipDesign.EndCutBuilder.LimitTypes
    Offset: Expression
    PlacementEdge: SelectEdge
    PlacementFaces: SelectFaceList
    Plane: Plane
    SelectionType: Features.ShipDesign.EndCutBuilder.SelectionTypes
    ShearAngle: Expression
    TiltAngle: Expression
    ToeSketchData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    WebSketchData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder


    class SelectionTypes(enum.Enum):
        FacesWithAttributes = 0
        FaceAndEdge = 1
    

    class LimitTypes(enum.Enum):
        Value = 0
        Plane = 1
        NeatTrim = 2
    

    class EndFaceTypes(enum.Enum):
        SquareCut = 0
        NeatTrim = 1
    

    class DraftTypes(enum.Enum):
        Trim = 0
        Extend = 1
    

    class ConnectionTypes(enum.Enum):
        Connected = 0
        FlangeFree = 1
        Sniped = 2
        SnipedSquare = 3
        None = 4
    

class EndCut(Features.BodyFeature):
    def __init__(self) -> None: ...


class EditWeldingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Seams: SelectNXObjectList
    WeldCharacteristics: Weld.CharacteristicsBuilder


class EditStockBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateStockInformation(self, shipStructure: NXObject) -> None:
        ...
    def SetPillarDirection(self, direction: Direction) -> None:
        ...
    BuiltUpPillarStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    EndCapThickness: Expression
    EndCutEnd: Features.ShipDesign.StiffenerSystemBuilder.EndCutTypes
    EndCutStart: Features.ShipDesign.StiffenerSystemBuilder.EndCutTypes
    EndEndCut: Features.ShipDesign.EndCutBuilder
    EndTreatment: Features.ShipDesign.PillarTreatmentBlockBuilder
    MountingMethod: Features.ShipDesign.StiffenerSystemBuilder.MountingMethods
    Offset: Expression
    OrientationAngle: Expression
    OrientationAnglePillar: Expression
    OrientationLinePillar: SelectCurve
    OrientationMethod: Features.ShipDesign.StiffenerSystemBuilder.OrientationMethods
    OrientationVector: Direction
    PillarStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    PlateStock: Features.ShipDesign.PlateStockBuilder
    Reverse: bool
    SectionType: Features.ShipDesign.PillarSystemBuilder.StockSectionType
    ShipStructure: SelectTaggedObjectList
    StartCapThickness: Expression
    StartEndCut: Features.ShipDesign.EndCutBuilder
    StartTreatment: Features.ShipDesign.PillarTreatmentBlockBuilder
    StiffenerStock: Features.ShipDesign.StiffenerStockBuilder
    Tightness: int


class EditContextAttributesBuilder(Builder):
    def __init__(self) -> None: ...
    ObjectsToEdit: SelectDisplayableObjectList


class EditBoundaryBuilder(Features.ShipDesign.ProfileSystemBuilder):
    def __init__(self) -> None: ...
    def GetSelectedKnuckles(self, profile: Curve, knucklePoints: typing.List[Point]) -> None:
        ...
    def UpdateEndCutInformation(self, shipStructure: NXObject) -> None:
        ...
    EndEndCut: Features.ShipDesign.EndCutBuilder
    ProfileSystem: SelectTaggedObjectList
    StartEndCut: Features.ShipDesign.EndCutBuilder


class EdgeReinforcementBuilder(Features.ShipDesign.ProfileSystemBuilder):
    def __init__(self) -> None: ...
    BuildSolid: bool
    CreateSeamsAtKnuckles: bool
    Edges: Section
    EndCutEnd: Features.ShipDesign.EdgeReinforcementBuilder.EndCutTypes
    EndCutStart: Features.ShipDesign.EdgeReinforcementBuilder.EndCutTypes
    EndEndCut: Features.ShipDesign.EndCutBuilder
    KnuckleLocationTolerance: float
    Offset: Expression
    OrientationAngle: Expression
    OrientationDefinitionBuilder: Features.ShipDesign.OrientationDefinitionBuilder
    OrientationMethod: Features.ShipDesign.EdgeReinforcementBuilder.OrientationMethods
    OrientationVector: Direction
    Reverse: bool
    ReverseAttachmentDirection: bool
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    StartEndCut: Features.ShipDesign.EndCutBuilder
    StockData: Features.ShipDesign.StiffenerStockBuilder
    Type: Features.ShipDesign.EdgeReinforcementBuilder.Types
    Weld: Weld.CharacteristicsBuilder


    class Types(enum.Enum):
        OnEdge = 0
        OnFace = 1
    

    class OrientationMethods(enum.Enum):
        FaceNormal = 0
        Vector = 1
    

    class EndCutTypes(enum.Enum):
        Connected = 0
        FlangeFree = 1
        Sniped = 2
        SnipedSquare = 3
        None = 4
    

class EdgeReinforcement(Features.CurveFeature):
    def __init__(self) -> None: ...


class EdgeCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CutCount: int
    CutOrientationAngle: Expression
    EndPositionOnGuide: GeometricUtilities.OnPathDimensionBuilder
    GuideCurve: Section
    GuideOffset: Expression
    HorizontalReference: Direction
    ManufacturingInformation: Features.ShipDesign.ManufacturingStockBuilder
    PathGeometry: SelectTaggedObjectList
    PathReverseDirection: bool
    PlacementGeometry: SelectDisplayableObjectList
    ReferenceDirection: Vector3d
    ReferencePoint: Point3d
    SelectEndLimit: SelectNXObject
    SelectStartLimit: SelectNXObject
    SelectTargetFace: SelectFaceList
    SketchBlock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    SpaceBetweenCuts: Expression
    Spacing: Features.ShipDesign.EdgeCutBuilder.ArraySpacing
    SpacingReference: Direction
    StartPositionOnGuide: GeometricUtilities.OnPathDimensionBuilder
    SymmetricOffsets: bool
    Version: Features.ShipDesign.EdgeCutBuilder.VersionID


    class VersionID(enum.Enum):
        Nx85 = 0
        Nx901 = 1
        IgnoreEndCuts = 2
    

    class ArraySpacing(enum.Enum):
        EvenDistribution = 0
        CustomDefined = 1
    

class EdgeCut(Features.BodyFeature):
    def __init__(self) -> None: ...


class DvToMvMappingBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AdoptedDesignBody: Body
    AdoptedMfgBody: Body
    DesignFeatureGroup: Features.Feature
    MfgFeatureGroup: Features.Feature
    OriginalDesignBody: Body
    OriginalMfgBody: Body


class DvToMvMapping(Features.BodyFeature):
    def __init__(self) -> None: ...


class DrawingTemplateBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    TemplateName: str


class DrawingSheetBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.DrawingSheetBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.DrawingSheetBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.DrawingSheetBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.DrawingSheetBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.DrawingSheetBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.DrawingSheetBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.DrawingSheetBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.DrawingSheetBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.DrawingSheetBuilder, object2: Features.ShipDesign.DrawingSheetBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.DrawingSheetBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DrawingSheetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ColumnCount: int
    DrawingTemplate: Features.ShipDesign.DrawingTemplateBuilder
    Layout: Features.ShipDesign.DrawingSheetBuilder.LayoutOptions
    RowCount: int
    SheetName: str
    SheetScale: str
    SymbolFlag: bool
    ViewList: Features.ShipDesign.SectionViewBuilderList


    class LayoutOptions(enum.Enum):
        Horizontal = 0
        Vertical = 1
    

class DrawingPartBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.DrawingPartBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.DrawingPartBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.DrawingPartBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.DrawingPartBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.DrawingPartBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.DrawingPartBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.DrawingPartBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.DrawingPartBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.DrawingPartBuilder, object2: Features.ShipDesign.DrawingPartBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.DrawingPartBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DrawingPartBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateDrawingSheetBuilder(self, drawingSheet: Drawings.DrawingSheet) -> Features.ShipDesign.DrawingSheetBuilder:
        ...
    def Validate(self) -> bool:
        ...
    CreateNewDrawingPart: bool
    DrawingName: str
    DrawingSheetList: Features.ShipDesign.DrawingSheetBuilderList


class DrawingAnnotationBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateDefaultGrades(self, defaultGrades: str) -> None:
        ...
    ExistingAutomaticAnnotation: Features.ShipDesign.DrawingAnnotationBuilder.Annotation
    IsCreateContinuitySymbolForBoundingStructureOfBracket: bool
    IsCreateContinuitySymbolOnSectionStiffener: bool
    IsCreateFireAndSafetyPlan: bool
    IsCreateOpeningFillLines: bool
    IsCreateReferenceLines: bool
    IsCreateScantling: bool
    IsCreateScantlingTable: bool
    IsCreateStiffenerSectionSymbol: bool
    IsCreateStructureID: bool
    ShowDefaultGradeInScantlingTable: bool
    ViewList: Drawings.SelectDraftingViewList


    class Annotation(enum.Enum):
        Preserve = 0
        Delete = 1
    

class DivideBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ExtendImprints: bool


class Divide(Features.BodyFeature):
    def __init__(self) -> None: ...


class DisplaySolidBuilder(Builder):
    def __init__(self) -> None: ...
    DisplayOption: Features.ShipDesign.DisplaySolidBuilder.DisplayOptionTypes
    ShipStructure: SelectNXObjectList


    class DisplayOptionTypes(enum.Enum):
        Curve = 0
        CurveAndSolid = 2
    

class DeleteSeamBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Seams: SelectTaggedObjectList


class DecksBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateDeckListItemBuilder(self) -> Features.ShipDesign.DeckListItemBuilder:
        ...
    AutoDeckName: str
    AutoNameToggle: bool
    DeckList: Features.ShipDesign.DeckListItemBuilderList


class Decks(Features.BodyFeature):
    def __init__(self) -> None: ...


class DeckListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.DeckListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.DeckListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.DeckListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.DeckListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.DeckListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.DeckListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.DeckListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.DeckListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.DeckListItemBuilder, object2: Features.ShipDesign.DeckListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.DeckListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DeckListItemBuilder(NXObject):
    def __init__(self) -> None: ...
    DeckCoord: Expression
    DeckName: str
    NormalDir: Features.ShipDesign.DeckListItemBuilder.DatumDir


    class DatumDir(enum.Enum):
        Plus = 0
        Minus = 1
        Neutral = 2
    

class DeckListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, deck: Assemblies.Component) -> None:
        ...
    def Remove(self, deck: Assemblies.Component) -> None:
        ...
    def Validate(self) -> bool:
        ...


class DeckBuilder(Features.ShipDesign.PlateSystemBuilder):
    def __init__(self) -> None: ...
    CamberHeight: Expression
    CamberOffset: Expression
    CenterHeight: Expression
    Hull: SelectBody
    MoldFacePlane: Plane
    MoldFacePlaneList: Features.ShipDesign.PlaneListBuilderList
    MoldFacePlanes: SelectDatumPlaneList
    MoldFaceSheet: SelectBody
    Type: Features.ShipDesign.DeckBuilder.Types


    class Types(enum.Enum):
        SheetBody = 0
        Planes = 1
        RoundCamber = 2
        StraightCamber = 3
    

class Deck(Features.BodyFeature):
    def __init__(self) -> None: ...


class CuttingSideFacesBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CuttingSideFaces: ScCollector
    DistanceTolerance: float
    ProcessCoplanar: bool
    ProcessTangent: bool
    ReverseSide: bool
    TangentFaceThreshold: Expression
    Type: Features.ShipDesign.CuttingSideFacesBuilder.Types
    WeldGapThreshold: Expression


    class Types(enum.Enum):
        Automatic = 0
        Manual = 1
        Reverse = 2
    

class Cutout2Builder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateEmptyPointDimBuilder(self) -> Features.ShipDesign.PointDimBuilder:
        ...
    def CreatePointDimBuilder(self, dimension: Expression, index: int) -> Features.ShipDesign.PointDimBuilder:
        ...
    AngularDimension: Expression
    CoordSystem: CoordinateSystem
    CornerRadiusList: Features.ShipDesign.PointDimBuilderList
    CustomShape: Section
    DefaultCornerRadius: Expression
    FacePlaneBoundaryList: ExpressionCollectorSetList
    HorizontalReference: Direction
    LinearOffset1: Expression
    LinearOffset2: Expression
    ManufacturingInformation: Features.ShipDesign.ManufacturingStockBuilder
    PlacementType: Features.ShipDesign.Cutout2Builder.CreationMethod
    ProjectionDirection: GeometricUtilities.ProjectionOptions
    ReferenceOffset1: Expression
    ReferenceOffset2: Expression
    ReferenceOffset3: Expression
    ReverseDirection1: bool
    ReverseDirection2: bool
    ReverseDirection3: bool
    SelectCSYSFace: SelectNXObject
    SelectLine1: SelectNXObject
    SelectLine2: SelectNXObject
    SelectReference1: SelectNXObject
    SelectReference2: SelectNXObject
    SelectReference3: SelectNXObject
    SelectTargetFace: SelectNXObject
    SelectTargetFaces: SelectNXObjectList
    SketchBlock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder


    class CreationMethod(enum.Enum):
        Face2Lines = 0
        SpecifyCSYS = 1
        Faces2Surfaces = 2
        FacesBetweenSurfacesSurface = 3
        FacesCentered = 4
        CustomShape = 5
        BoundingObjects = 6
        CenteredBoundingObjects = 7
    

class Cutout2(Features.BodyFeature):
    def __init__(self) -> None: ...


class CustomBracketBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetAvailableAttributeNames(self) -> str:
        ...
    def GetAvailableAttributeMaterials(self) -> str:
        ...
    AttributeMaterial: int
    AttributeName: int
    CoordSystem: CoordinateSystem
    HeelOffset: Expression
    HeelPoint: Point
    KeepCoordSystem: bool
    KeepHeelPoint: bool
    KeepPlacementPlane: bool
    KeepReferencePlane: bool
    KeepReverseDirection: bool
    KeepSelectTrimFace: bool
    PlacementPlane: Plane
    PlacementType: Features.ShipDesign.CustomBracketBuilder.CreationMethod
    ReferencePlane: Plane
    ReverseDirection: bool
    SelectTrimFace: ScCollector
    SketchBlock: SketchExpressionModifierBuilder
    Thickness: Expression


    class CreationMethod(enum.Enum):
        PlanesAndPoint = 0
        SpecifyCSYS = 1
    

class CustomBracket(Features.BodyFeature):
    def __init__(self) -> None: ...


class CornerCutListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.CornerCutListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.CornerCutListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.CornerCutListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.CornerCutListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.CornerCutListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.CornerCutListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.CornerCutListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.CornerCutListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.CornerCutListItemBuilder, object2: Features.ShipDesign.CornerCutListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.CornerCutListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CornerCutListItemBuilder(Builder):
    def __init__(self) -> None: ...
    CornerPoint: Point
    PlacementFace: SelectTaggedObject
    SeamCurve: SelectTaggedObject


class CornerCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    CornerList: Features.ShipDesign.CornerCutListItemBuilderList
    CornerPoint: Point
    DistanceTolerance: float
    ManufacturingInformation: Features.ShipDesign.ManufacturingStockBuilder
    PlacementFace: SelectTaggedObject
    PlacementType: Features.ShipDesign.CornerCutBuilder.CutOption
    PlateBodyCollector: ScCollector
    Spreadsheet: Features.ShipDesign.SteelFeatureSpreadsheetBuilder


    class CutOption(enum.Enum):
        Corner = 0
        Plate = 1
    

class CornerCut(Features.BodyFeature):
    def __init__(self) -> None: ...


class CopyPasteNewBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetOperationFailures(self) -> ErrorList:
        ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...
    AlgorithmVersion: Features.ShipDesign.CopyPasteNewBuilder.VersionID
    AngularTolerance: float
    ComponentsToCopy: SelectNXObjectList
    CopyApproachOption: Features.ShipDesign.CopyPasteNewBuilder.CopyApproach
    CopySection: bool
    LinearTolerance: float
    SelectionFrom: SelectNXObject
    SelectionTo: SelectNXObjectList
    ShipNames: Features.ShipDesign.ShipNamesListBuilder
    ShowXmlReport: bool


    class VersionID(enum.Enum):
        Nx11 = 0
        Nx12 = 1
    

    class CopyApproach(enum.Enum):
        TransferringLinkedBody = 0
        CopySourceFeaturesAndReparent = 1
    

class CopyObjectsBuilder(Builder):
    def __init__(self) -> None: ...
    AlgorithmVersion: Features.ShipDesign.CopyObjectsBuilder.VersionID
    AngularTolerance: float
    CopyFrom: SelectNXObject
    CopySection: bool
    CopyTo: SelectNXObjectList
    InputObjects: SelectNXObjectList
    LinearTolerance: float
    ObjectType: Features.ShipDesign.CopyObjectsBuilder.Type
    ShipNames: Features.ShipDesign.ShipNamesListBuilder
    ShowXmlReport: bool


    class VersionID(enum.Enum):
        Nx11 = 0
        Nx12 = 1
    

    class Type(enum.Enum):
        Part = 0
        Feature = 1
    

class ConceptFromSpreadsheetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ConceptPart: str
    CreateConcept: bool
    GridPart: str
    GridType: Features.ShipDesign.ConceptFromSpreadsheetBuilder.Type
    ReadDataSet: Features.ShipDesign.ReadDataSetBuilder
    ShipBody: SelectBody


    class Type(enum.Enum):
        GeneralArrangement = 0
        BasicDesign = 1
        DetailDesign = 2
        Manufacturing = 3
    

class ConceptFromSpreadsheet(Features.BodyFeature):
    def __init__(self) -> None: ...


class CompareModeBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateDisplay(self) -> int:
        ...
    def RestoreDisplay(self, singleparttorestore: Assemblies.Component) -> None:
        ...
    CompareEmphasizeMode: Features.ShipDesign.CompareModeBuilder.CompareMode
    DesignElementToCompare: SelectNXObjectList


    class CompareMode(enum.Enum):
        DesignMode = 0
        ManufacturingMode = 1
    

class CollarPlateBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateCollarPlateSizeInformation(self) -> None:
        ...
    AngularTolerance: float
    DistanceTolerance: float
    FromTargetPlate: bool
    InstallDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    ManufacturingStock: Features.ShipDesign.ManufacturingStockBuilder
    ProfileCutout: ScCollector
    SectionData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    SquareCut: bool
    WeldCharacteristics: Weld.CharacteristicsBuilder


class CollarPlate(Features.BodyFeature):
    def __init__(self) -> None: ...


class CloneWeldsBuilder(Builder):
    def __init__(self) -> None: ...
    Override: bool
    WeldComponents: SelectDisplayableObjectList


class BulkHeadsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateBulkheadListItem(self, bulkheadsType: Features.ShipDesign.BulkHeadsBuilder.BulkheadType) -> Features.ShipDesign.BulkHeadListItemBuilder:
        ...
    AutoBulkHeadName: str
    AutoNameToggle: bool
    BulkHeadList: Features.ShipDesign.BulkHeadListItemBuilderList
    Type: Features.ShipDesign.BulkHeadsBuilder.BulkheadType


    class BulkheadType(enum.Enum):
        Transverse = 0
        Longitudinal = 1
    

class BulkHeads(Features.BodyFeature):
    def __init__(self) -> None: ...


class BulkHeadListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.BulkHeadListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.BulkHeadListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.BulkHeadListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.BulkHeadListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.BulkHeadListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.BulkHeadListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.BulkHeadListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.BulkHeadListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.BulkHeadListItemBuilder, object2: Features.ShipDesign.BulkHeadListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.BulkHeadListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BulkHeadListItemBuilder(NXObject):
    def __init__(self) -> None: ...
    BulkHeadName: str
    FrameName: str
    FrameOffset: Expression


class BuiltUpOffsetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FlangeAngle: Expression
    FlangeOffset: Expression
    WebAngle: Expression
    WebOffset: Expression


class BuiltUpManModeBuilder(Builder):
    def __init__(self) -> None: ...
    BuiltupComps: Assemblies.SelectComponentList
    BuiltupManMode: Features.ShipDesign.BuiltUpManModeBuilder.BuiltUpManModeType


    class BuiltUpManModeType(enum.Enum):
        CutToShape = 0
        BendAfterJoin = 1
        None = 2
    

class BuiltUpBlockBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateSeamBlockBuilder(self) -> Features.ShipDesign.SeamBlockBuilder:
        ...
    def Validate(self) -> bool:
        ...
    BuiltUpSeams: Features.ShipDesign.SeamBlockBuilderList
    BuiltUpStock: Features.ShipDesign.SteelFeatureSpreadsheetBuilder


class BracketBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlignmentAngle: Expression
    AlignmentPlane: SelectDisplayableObject
    AlignmentType: Features.ShipDesign.BracketBuilder.AlignmentTypes
    AngularTolerance: float
    AttachmentDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    AttachmentFace: ScCollector
    AttachmentStiffener: SelectDisplayableObjectList
    BracketOffset: Expression
    DisableFlangeRule: bool
    DistanceTolerance: float
    EndAttachment: ScCollector
    FlangeData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    LimitType: Features.ShipDesign.BracketBuilder.LimitTypes
    ManufacturingStock: Features.ShipDesign.ManufacturingStockBuilder
    PickPointOnAttachment: Point3d
    PickPointOnReinforcement: Point3d
    ReinforcementDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    ReinforcementFace: ScCollector
    ReinforcementStiffener: SelectDisplayableObjectList
    ReinforcementType: Features.ShipDesign.BracketBuilder.ReinforcementTypes
    ReverseFlange: bool
    ReverseFlatBarThicknessDirection: bool
    SectionData: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    ShipNames: Features.ShipDesign.ShipNamesBuilder
    SquareCut: bool
    StartAttachment: ScCollector
    StartAttachmentLimit: ScCollector
    ThicknessDirection: Features.ShipDesign.StandardPartItemBuilder.Direction
    WeldCharacteristics: Weld.CharacteristicsBuilder
    WithFlange: bool


    class ReinforcementTypes(enum.Enum):
        NoReinforcement = 0
        WithFlange = 1
        WithFlatBar = 2
    

    class LimitTypes(enum.Enum):
        NoLimit = 0
        OneLimit = 1
        TwoLimit = 2
        ThreeLimit = 3
    

    class AlignmentTypes(enum.Enum):
        DatumPlaneAlignment = 0
        AutoAlignment = 1
        Lapped = 2
    

class Bracket(Features.BodyFeature):
    def __init__(self) -> None: ...


class AssemblyViewBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.AssemblyViewBuilder]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.AssemblyViewBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.AssemblyViewBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.AssemblyViewBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.AssemblyViewBuilder) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.AssemblyViewBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.AssemblyViewBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.AssemblyViewBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.AssemblyViewBuilder, object2: Features.ShipDesign.AssemblyViewBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.AssemblyViewBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class AssemblyViewBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateDrawingSheet(self, drawingSheet: Features.ShipDesign.DrawingSheetBuilder) -> None:
        ...
    ContainerParts: int
    DrawingName: str
    DrawingSheet: Features.ShipDesign.DrawingSheetBuilder
    DrawingTemplate: Features.ShipDesign.DrawingTemplateBuilder
    Index: int
    Level: int
    Orientation: int
    PartsList: int
    PartsListString: str
    SheetScale: float
    ShowList: bool
    Symbol: bool
    UpdateFlag: bool
    ViewTag: Drawings.DraftingView


class AssemblyDrawingBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateAssemblyViewBuilder(self) -> Features.ShipDesign.AssemblyViewBuilder:
        ...
    def CreateDrawingPartBuilder(self, drawingPart: Part) -> Features.ShipDesign.DrawingPartBuilder:
        ...
    DrawingPartList: Features.ShipDesign.DrawingPartBuilderList
    ViewList: Features.ShipDesign.AssemblyViewBuilderList


class AnchorPointList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.ShipDesign.AnchorPoint]) -> None:
        ...
    def Append(self, object: Features.ShipDesign.AnchorPoint) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.ShipDesign.AnchorPoint) -> int:
        ...
    def FindItem(self, index: int) -> Features.ShipDesign.AnchorPoint:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.AnchorPoint) -> None:
        ...
    def Erase(self, obj: Features.ShipDesign.AnchorPoint, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.ShipDesign.AnchorPoint]:
        ...
    def SetContents(self, objects: typing.List[Features.ShipDesign.AnchorPoint]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.ShipDesign.AnchorPoint, object2: Features.ShipDesign.AnchorPoint) -> None:
        ...
    def Insert(self, location: int, object: Features.ShipDesign.AnchorPoint) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class AnchorPoint(Builder):
    def __init__(self) -> None: ...
    Name: str
    Point: SelectPoint


class AlongGuideCutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ArrowHeadAngle: Expression
    ArrowHeadHeight: Expression
    ArrowHeight: Expression
    DirectionOption: Features.ShipDesign.AlongGuideCutBuilder.DirectionMethod
    DistanceTolerance: float
    GuideCurve: SelectNXObject
    GuideCurveList: SelectNXObjectList
    LeftOffsetDistance: Expression
    ManufacturingInformation: Features.ShipDesign.ManufacturingStockBuilder
    PlacementType: Features.ShipDesign.AlongGuideCutBuilder.CreationMethod
    RightOffsetDistance: Expression
    ShipStructure: SelectBodyList
    ShipStructureEdge: SelectEdgeList
    Spreadsheet: Features.ShipDesign.SteelFeatureSpreadsheetBuilder
    WaterStopOffsetOption: Features.ShipDesign.AlongGuideCutBuilder.WaterStopOffsetMethod
    WaterStopShape: SelectNXObject
    WaterStopShapeList: SelectNXObjectList


    class WaterStopOffsetMethod(enum.Enum):
        Symmetric = 0
        Asymmetric = 1
    

    class DirectionMethod(enum.Enum):
        PerpendicularToMoldFace = 0
        AlongGuide = 1
    

    class CreationMethod(enum.Enum):
        WeldClearance = 0
        WaterStop = 1
        EggBoxTop = 2
        EggBoxBottom = 3
        EggBox = 4
        Notch = 5
    

class AlongGuideCut(Features.BodyFeature):
    def __init__(self) -> None: ...


class AddDataSetBuilder(Builder):
    def __init__(self) -> None: ...
    Component: SelectDisplayableObject
    DataSetFile: str


