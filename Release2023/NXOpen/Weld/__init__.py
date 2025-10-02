from ...NXOpen import *
from ..Weld import *

import typing
import enum

class WeldTaperMethod(enum.Enum):
    FromEndFace = 0
    FromSideFace = 1


class WeldSpacingCalcMethod(enum.Enum):
    Arclength = 0
    ParallelXPlane = 1
    ParallelYPlane = 2
    ParallelZPlane = 3
    MiddleOfCurve = 4
    NormalToBody = 5


class WeldSelectionType(enum.Enum):
    General = 0
    Surface = 1
    Curve = 2


class WeldRootUpdate(enum.Enum):
    Automatic = 0
    None = 1


class WeldProjectionMethod(enum.Enum):
    None = 0
    FaceNormal = 1
    AlongVector = 2


class WeldPrepareEdges(enum.Enum):
    None = 0
    EntireEdge = 1
    WeldLimits = 2
    Complex = 3


class WeldPreferenceBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDatumSelectedPrefix(self) -> str:
        ...
    def SetDatumSelectedPrefix(self, datumSelectedPrefix: str) -> None:
        ...
    def GetDatumSelectedSuffix(self) -> str:
        ...
    def SetDatumSelectedSuffix(self, datumSelectedSuffix: str) -> None:
        ...
    def GetMeasurementSelectedPrefix(self) -> str:
        ...
    def SetMeasurementSelectedPrefix(self, measurementSelectedPrefix: str) -> None:
        ...
    def GetMeasurementSelectedSuffix(self) -> str:
        ...
    def SetMeasurementSelectedSuffix(self, measurementSelectedSuffix: str) -> None:
        ...
    CurrentGroupIDColorIndex: Weld.WeldGroupIdColor
    DatumIdLowerRange: int
    DatumIdUpperRange: int
    DatumNamePrefix: str
    DatumObjectColor: NXColor
    DatumObjectLayer: int
    DatumPartNumber: str
    MeasurementIdLowerRange: int
    MeasurementIdUpperRange: int
    MeasurementNamePrefix: str
    MeasurementObjectColor: NXColor
    MeasurementObjectLayer: int
    MeasurementPartNumber: str
    WeldArcGridLineEndCapDisp: float
    WeldArcGridLineTopDisp: float
    WeldAssoColor: NXColor
    WeldConstLayer: int
    WeldFixedColor: NXColor
    WeldGroupIdLowerRange: str
    WeldGroupIdUpperRange: str
    WeldIdLowerRange: int
    WeldIdUpperRange: int
    WeldNamePrefix: str
    WeldObjectLayer: int
    WeldPartNumber: str
    WeldRetainedColor: NXColor
    WeldSymbolDecimalPlaces: int


class WeldPointSpacingMethod(enum.Enum):
    Distance = 0
    NumPoints = 1


class WeldPointReferenceSheetType(enum.Enum):
    Overlap = 0
    Top = 1
    None = 2


class WeldPointMethod(enum.Enum):
    Multiple = 0
    Single = 1
    Mirror = 2
    Translate = 3
    FromPoints = 4


class WeldPointLocation(enum.Enum):
    AlongGuideCurve = 0
    AlongGuideEdge = 1
    AlongCenterLine = 2
    SectionPlane = 3


class WeldPointExtendMethod(enum.Enum):
    None = 0
    Boundary = 1


class WeldPointExitBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetFeatureInformation(self, features: typing.List[Weld.WeldPointExitBuilder.FeatureInfo]) -> None:
        """[Obsolete("Deprecated in NX12.0.1.  Use NXOpen.Weld.WeldPointExitBuilder.GetFeatureDetails instead.")"""
        ...
    def GetFeatureDetails(self, features: typing.List[Weld.WeldPointExitBuilder.FeatureDetails]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CommandUsed: Weld.WeldPointExitBuilder.CommandName


    class MethodUsed(enum.Enum):
        None = 0
        Mirror = 1
        Translate = 2
        GuideCurve = 3
        Points = 4
        GuideCurveMovedOff = 5
    

    class FeatureStatus(enum.Enum):
        Modified = 0
        NewlyCreated = 1
        NotUsed = 2
    

    class WeldPointExitBuilderFeatureInfo():
        Feature: Features.Feature
        MethodUsed: Weld.WeldPointExitBuilder.MethodUsed
        Parent: Features.Feature
        IsNewlyCreated: bool
        def ToString(self) -> str:
            ...
    

    class WeldPointExitBuilderFeatureDetails():
        Feature: Features.Feature
        MethodUsed: Weld.WeldPointExitBuilder.MethodUsed
        Parent: Features.Feature
        IsNewlyCreated: Weld.WeldPointExitBuilder.FeatureStatus
        def ToString(self) -> str:
            ...
    

    class CommandName(enum.Enum):
        None = 0
        WeldPoint = 1
        DatumLocator = 2
        MeasurementLocator = 3
        Jointmark = 4
        WeldPointWizard = 5
        EasySpot = 6
        EasySpotSelected = 7
        EasySpotApply = 8
        EasySpotEnded = 9
    

    class WeldPointExitBuilder_FeatureInfo():
        feature: Tag
        methodUsed: Weld.WeldPointExitBuilder.MethodUsed
        parent: Tag
        isNewlyCreated: bool
    

    class WeldPointExitBuilder_FeatureDetails():
        feature: Tag
        methodUsed: Weld.WeldPointExitBuilder.MethodUsed
        parent: Tag
        isNewlyCreated: Weld.WeldPointExitBuilder.FeatureStatus
    

class WeldPointDirection(enum.Enum):
    StartToEnd = 0
    EndToStart = 1


class WeldPointBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSectionCurves(self, section: Section, curves: typing.List[Curve]) -> None:
        ...
    def GetFaceSet(self, facesetIndex: int, objects: typing.List[DisplayableObject], frecs: typing.List[Features.Feature]) -> None:
        ...
    def SetFaceSet(self, facesetIndex: Weld.WeldFacesetIndex, objects: typing.List[DisplayableObject]) -> None:
        ...
    def CommitReferenceSheets(self, createStatus: Weld.WeldOverlapStatus) -> None:
        ...
    def ClearFaceSets(self) -> None:
        ...
    def CommitFaceSets(self) -> None:
        ...
    def GetCurrentReferenceSheet(self) -> int:
        ...
    def SetCurrentReferenceSheet(self, currentRefSheet: int) -> None:
        ...
    def CreateSingleWeldPoint(self, pointCoord: Point3d) -> None:
        ...
    def SetFirstSection(self, section: Section) -> None:
        ...
    def UpdateFirstSection(self, totalSection: Section) -> None:
        ...
    def UpdateSecondSection(self, totalSection: Section) -> None:
        ...
    def SetSecondSection(self, section: Section) -> None:
        ...
    def CreateOffsetCurve(self) -> Section:
        ...
    def CalculateWeldPoints(self, points: typing.List[Point3d]) -> None:
        ...
    def SetPoint(self, index: int) -> None:
        ...
    def SetCharacteristics(self, attrTitle: str, attrType: Weld.WeldAttribType, attrValue: str) -> None:
        ...
    def UpdateCsys(self, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def MovePoint(self, origin: Point3d) -> None:
        ...
    def CreateCenterLine(self) -> Section:
        ...
    def CommitSection(self, path: Section) -> None:
        ...
    def SetSelectionType(self, selectionType: Weld.WeldSelectionType) -> None:
        ...
    def FlipZAxis(self) -> None:
        ...
    def CreateSectionPlaneCurves(self) -> Section:
        ...
    def SetMirrorTranslateReferenceObjects(self, refs: typing.List[TaggedObject]) -> None:
        ...
    def GetMirrorTranslateReferenceObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def CalculateDatumMeasurementDefaultDirection(self) -> None:
        ...
    def RemoveCharacteristics(self, attrTitle: str, attrType: Weld.WeldAttribType, attrValue: str) -> None:
        ...
    def RemoveWeldPoint(self) -> None:
        ...
    def GetNumFaceSets(self) -> int:
        ...
    def GetFirstSection(self) -> Section:
        ...
    def GetSecondSection(self) -> Section:
        ...
    def GetReferenceSheets(self) -> Features.Feature:
        ...
    def GetCsys(self, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def ProjectPoints(self) -> None:
        ...
    ConnectingOnlyOnePart: bool
    CreationDirection: Weld.WeldCreationDirection
    CsysAssemblyState: bool
    CsysWorkPartState: bool
    CustomCylinderAbove: float
    CustomRadius: float
    CustomTotalCylinderLength: float
    DatumFirstReferenceDirection: Weld.WeldDatumControlDirection
    DatumMajorDirection: Weld.WeldDatumControlDirection
    DatumSecondReferenceDirection: Weld.WeldDatumControlDirection
    DistanceTolerance: float
    EndDistance: str
    EndDistanceLocation: Weld.WeldParasetLocation
    ExtendMethod: Weld.WeldPointExtendMethod
    Location: Weld.WeldPointLocation
    MeasurementDefaultHeight: float
    MeasurementDefaultWidth: float
    MeasurementHoleSize: float
    MeasurementSlotLength: float
    MeasurementSlotWidth: float
    MeasurementStudSize: float
    MirrorByType: bool
    MirrorPlane: Plane
    NumberConnectedPanels: int
    OffsetDistance: str
    OutputType: Weld.OutputType
    PointMethod: Weld.WeldPointMethod
    PointsGuideDistance: float
    ProjectDirection: Vector3d
    ProjectDirectionObject: Direction
    ProjectionMethod: Weld.WeldProjectionMethod
    ReferenceSheetSpacingMethod: Weld.WeldPointSpacingMethod
    ReferenceSheetType: Weld.WeldPointReferenceSheetType
    SectionPlaneEntity: Plane
    SequenceNumber: int
    ShowThroughAssemblyState: bool
    ShowThroughWorkPartState: bool
    SizeMethod: Weld.WeldMeasurementSizeMethod
    SolidType: Weld.WeldCustom
    SpacingCalculateMethod: Weld.WeldSpacingCalcMethod
    SpacingNumber: str
    StartDistance: str
    StartDistanceLocation: Weld.WeldParasetLocation
    TranslateCsys: CoordinateSystem
    TranslateXDistance: str
    TranslateYDistance: str
    TranslateZDistance: str
    WeldType: Weld.WeldFeatureSetType


class WeldPoint(Features.Feature):
    def __init__(self) -> None: ...


class WeldPmiBuilder(Builder):
    def __init__(self) -> None: ...
    GroupWeldSymbols: Weld.WeldPmiBuilder.GroupWeldSymbolsType
    Objects: SelectNXObjectList
    PlaneType: Weld.WeldPmiBuilder.OrientationPlaneType
    SpaceFactor: float
    Style: Annotations.StyleBuilder
    UserCoordinateSystem: CoordinateSystem


    class OrientationPlaneType(enum.Enum):
        XYPlane = 0
        XZPlane = 1
        YZPlane = 2
        ModelView = 3
        LastUserDefined = 4
        UserDefined = 5
    

    class GroupWeldSymbolsType(enum.Enum):
        None = 0
        All = 1
        ByStructureDesignerObjects = 2
    

class WeldParasetLocation(enum.Enum):
    Length = 0
    Percent = 1
    ThroughPoint = 2


class WeldOverlapStatus(enum.Enum):
    Invalid = -1
    Creation = 0
    NonCreation = 1


class WeldObjectBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetFeatureInformation(self, features: typing.List[Weld.WeldObjectBuilder.FeatureInfo]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CommandUsed: Weld.WeldObjectBuilder.CommandName


    class WeldObjectBuilderFeatureInfo():
        Feature: Features.Feature
        IsNewlyCreated: bool
        def ToString(self) -> str:
            ...
        def __init__(self, Feature: Features.Feature, IsNewlyCreated: bool) -> None: ...
    

    class CommandName(enum.Enum):
        None = 0
        Groove = 1
        Fillet = 2
        UserDefined = 3
        WeldPoint = 4
        Bead = 5
        Fill = 6
        ImportCsv = 7
        EasySpot = 8
        DatumLocator = 9
        MeasurementLocator = 10
        EasyMeasurementPattern = 11
        PlugSlot = 12
        Joint = 13
        DatumSurface = 14
        DatumPin = 15
        SurfaceWeld = 16
        Compound = 17
        WeldAttribute = 18
        JointDefinition = 19
        Jointmark = 20
        WeldPointWizard = 21
        Transform = 22
    

    class WeldObjectBuilder_FeatureInfo():
        feature: Tag
        isNewlyCreated: bool
    

class WeldMeasurementSizeMethod(enum.Enum):
    Invalid = -1
    Auto = 0
    Manual = 1


class WeldManager(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Feature]:
        ...
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def __init__(self) -> None: ...
    def CreateWeldGrooveBuilder(self, weldGroove: Features.Feature) -> Weld.GrooveBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilderinstead.")"""
        ...
    def CreateWeldPointBuilder(self, weldPoint: Features.Feature) -> Weld.WeldPointBuilder:
        ...
    def CreateImportBuilder(self) -> Weld.WeldImportBuilder:
        ...
    def CreateJointBuilder(self, weldJoint: Weld.WeldJoint) -> Weld.WeldJointBuilder:
        ...
    def CreateJointExitBuilder(self, weldJoint: Weld.WeldJoint) -> Weld.JointExitBuilder:
        ...
    def CreateJointExitBuilderCurve(self, curve: Curve) -> Weld.JointExitBuilder:
        ...
    def CreateExportWeldBuilder(self) -> Weld.ExportWeldBuilder:
        ...
    def CreateEdgePrepValuesBuilder(self) -> Weld.EdgePrepValuesBuilder:
        ...
    def CreateAutoPointBuilder(self, unused: Features.Feature) -> Weld.AutoPointBuilder:
        ...
    def CreatePreferenceBuilder(self) -> Weld.WeldPreferenceBuilder:
        ...
    def CreateUserDefinedWeldBuilder(self, featureSet: Features.Feature) -> Weld.UserDefinedWeldBuilder:
        ...
    def CreateCharacteristicsBuilder(self, object: NXObject, weldType: int) -> Weld.CharacteristicsBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use overloaded function with enum instead.")"""
        ...
    def CreateCharacteristicsBuilder(self, object: NXObject, charxType: Weld.CharacteristicsBuilder.Type) -> Weld.CharacteristicsBuilder:
        ...
    def CreateWeldAdvisorBuilder(self) -> Weld.WeldAdvisorBuilder:
        ...
    def CreateFillBuilder(self, fillFeature: Weld.Fill) -> Weld.WeldFillBuilder:
        ...
    def CreateWeldBeadBuilder(self, beadFeature: Features.Feature) -> Weld.WeldBeadBuilder:
        ...
    def CreateEasyPatternBuilder(self, patternFeatureSet: Features.Feature) -> Weld.EasyPatternBuilder:
        ...
    def CreatePlugSlotBuilder(self, feature: Features.Feature) -> Weld.PlugSlotBuilder:
        ...
    def CreateFilletBuilder(self, feature: Features.Feature) -> Weld.FilletBuilder:
        ...
    def CreateEdgePrepBuilder(self, edgePrepFeature: Weld.EdgePrep) -> Weld.EdgePrepBuilder:
        ...
    def CreateAutoWeldSymbolsBuilder(self) -> Weld.AutoWeldSymbolsBuilder:
        ...
    def CreateWeldObjectBuilder(self) -> Weld.WeldObjectBuilder:
        ...
    def CreateExportWeldJointBuilder(self) -> Weld.ExportWeldJointBuilder:
        ...
    def CreateDatumSurfaceBuilder(self, feature: Weld.DatumSurface) -> Weld.DatumSurfaceBuilder:
        ...
    def CreateDatumPinBuilder(self, feature: Weld.DatumPin) -> Weld.DatumPinBuilder:
        ...
    def CreateWeldLabelBuilder(self, annotation: Annotations.Annotation) -> Weld.WeldLabelBuilder:
        ...
    def CreateWeldGroove1Builder(self, grooveFeature: Features.Feature) -> Weld.WeldGrooveBuilder:
        ...
    def CreateWeldPointExitBuilder(self) -> Weld.WeldPointExitBuilder:
        ...
    def CreateJointmarkBuilder(self, jointmarkFeature: Weld.Jointmark) -> Weld.JointmarkBuilder:
        ...
    def EditSingleJointmarkFeature(self, elementFeature: Features.Feature) -> Weld.JointmarkBuilder:
        ...
    def CreateSurfaceWeldBuilder(self, surfaceWeld: Weld.SurfaceWeld) -> Weld.SurfaceWeldBuilder:
        ...
    def CreateConnectedFaceFinderOperation(self) -> Weld.ConnectedFaceFinderBuilder:
        ...
    def CreateConnectedFaceFinderBuilder(self, weldFeatures: typing.List[Features.Feature]) -> Weld.ConnectedFaceFinderBuilder:
        ...
    def CreateCompoundWeldBuilder(self, compoundWeld: Weld.CompoundWeld) -> Weld.CompoundWeldBuilder:
        ...
    def CreateInformationBuilder(self) -> Weld.InformationBuilder:
        ...
    def CreateWeldPmiBuilder(self) -> Weld.WeldPmiBuilder:
        ...
    def CreatePointMarkBuilder(self, pointMarkFeature: Weld.PointMark) -> Weld.PointMarkBuilder:
        ...
    def EditSinglePointMarkFeature(self, elementFeature: Weld.PointMarkPoint) -> Weld.PointMarkBuilder:
        ...
    def CreateLocatorReferenceBuilder(self) -> Weld.LocatorReferenceBuilder:
        ...
    def CreateBeadDesignFeature(self) -> None:
        ...
    def CreateTransformBuilder(self, feature: Weld.Transform) -> Weld.TransformBuilder:
        ...
    def Tag(self) -> Tag: ...



class WeldLabelBuilder(Builder):
    def __init__(self) -> None: ...
    IncludeLeader: bool
    Leader: Annotations.LeaderBuilder
    Objects: SelectNXObjectList
    Origin: Annotations.OriginBuilder
    PlaneType: Weld.WeldLabelBuilder.OrientationPlaneType
    Style: Annotations.StyleBuilder
    Text: Annotations.TextWithEditControlsBuilder
    UserCsys: CoordinateSystem


    class OrientationPlaneType(enum.Enum):
        XYPlane = 0
        XZPlane = 1
        YZPlane = 2
        ModelView = 3
        LastUserDefined = 4
        UserDefined = 5
    

class WeldJointBuilder(Weld.StructureWeldBuilder):
    def __init__(self) -> None: ...
    def Delete(self) -> None:
        ...
    def Split(self) -> None:
        ...
    def UpdateJointType(self, type: Weld.WeldJointBuilder.WeldTypes) -> None:
        ...
    def DeleteAllUnMarkedJoints(self) -> None:
        ...
    def AddCharacteristicsInheritaceInformation(self) -> None:
        ...
    def DeleteCharacteristicsInheritaceInformation(self) -> None:
        ...
    def MarkJointsToKeep(self) -> None:
        ...
    def ShowJoints(self) -> None:
        ...
    def GetJointLimits(self, curve: Curve) -> Die.DieLimitsBuilder:
        ...
    def GetSingleJoint(self, curve: Curve) -> Weld.JointItemBuilder:
        ...
    def GetJointChanged(self, curve: Curve) -> bool:
        ...
    def SetJointChanged(self, curve: Curve, changed: bool) -> None:
        ...
    def CreateLimitsPath(self, jointCurve: Curve) -> Curve:
        ...
    def UpdateCollectors(self, jointCurve: Curve) -> None:
        ...
    def UpdateJointAfterLimitsChange(self) -> None:
        ...
    def UpdateJointAfterLimitsChange(self, limits: Die.DieLimitsBuilder) -> None:
        ...
    def CopyLimits(self, limits: Die.DieLimitsBuilder) -> None:
        ...
    def CreateSingleJointFromFeature(self, featureCurve: Curve, updateBuilder: bool) -> None:
        ...
    def SetVariableBevelAngles(self, variableAngles: float) -> None:
        ...
    def GetVariableBevelAngles(self, variableAngles: float) -> None:
        ...
    def GetConnectedParts(self, parts: typing.List[Assemblies.Component]) -> None:
        ...
    def FindPortsInParts(self, parts: typing.List[Assemblies.Component], ports: typing.List[Routing.Port]) -> None:
        ...
    def GetPrimaryThickness(self, curve: Curve) -> float:
        ...
    def GetSecondaryThickness(self, curve: Curve) -> float:
        ...
    def GetAngleBetween(self) -> float:
        ...
    def GetIsLongPoint(self) -> bool:
        ...
    def IsCornerOpen(self) -> bool:
        ...
    def IsPipeJoint(self) -> bool:
        ...
    def NewItem(self) -> Weld.JointItemBuilder:
        ...
    def GetNewlyCreatedJoints(self, curves: typing.List[Curve], newItemBuilder: typing.List[Weld.JointItemBuilder]) -> None:
        ...
    def SetCallbackMessage(self, message: str) -> None:
        ...
    def SetErrorMessage(self, message: str) -> None:
        ...
    def GetMidPointInformation(self, desiredCoordinateSystem: Weld.WeldJointBuilder.CoordinateSystem, jointMidPointData: Weld.WeldJointBuilder.JointMidPointData) -> bool:
        ...
    AssociativeSplit: bool
    BackingFace: ScCollector
    BossColorFontWidth: LineColorFontWidthBuilder
    ButtColorFontWidth: LineColorFontWidthBuilder
    CombineConnectedJoints: bool
    CornerColorFontWidth: LineColorFontWidthBuilder
    CreateMethod: Weld.WeldJointBuilder.Types
    CreatedApplication: Weld.WeldJointBuilder.Application
    Destination: Weld.WeldJointBuilder.DestinationTypes
    DuplicateCheck: bool
    Joint: SelectCurveList
    JointList: Weld.JointItemBuilderList
    JointPrefix: str
    LapColorFontWidth: LineColorFontWidthBuilder
    LimitList: Die.DieLimitsBuilderList
    Limits: Die.DieLimitsBuilder
    MasterEdge: ScCollector
    MaximumFaceGap: float
    MechanicalColorFontWidth: LineColorFontWidthBuilder
    NamePrefix: str
    NumberSegments: int
    PlacementFace: ScCollector
    PrimaryEdge: ScCollector
    PrimaryFace: ScCollector
    SecondaryEdge: ScCollector
    SecondaryFace: ScCollector
    ShipComponent: SelectNXObjectList
    SleeveColorFontWidth: LineColorFontWidthBuilder
    SocketColorFontWidth: LineColorFontWidthBuilder
    SpacingLength: float
    SplitAngle: float
    SplitLength: float
    SplitOption: Weld.WeldJointBuilder.SplitTypes
    SubsetPart: Part
    TJointColorFontWidth: LineColorFontWidthBuilder
    TargetFace: ScCollector
    Type: Weld.WeldJointBuilder.Types
    WeldType: Weld.WeldJointBuilder.WeldTypes
    WeldingCharacteristics: Weld.CharacteristicsBuilder
    WorkPart: Part


    class WeldTypes(enum.Enum):
        Any = 0
        Groove = 1
        Fillet = 2
        Corner = 3
        Lap = 4
        Socket = 5
        Mechanical = 6
        Sleeve = 7
        Boss = 8
    

    class Types(enum.Enum):
        CreateAutomatic = 0
        CreateManual = 1
        CreateMultiple = 2
        CreateAttributes = 3
        CreateSingleSided = 4
    

    class SplitTypes(enum.Enum):
        EqualSegments = 0
        Limits = 1
        Angle = 2
        ComputedAngle = 3
        Length = 4
        None = 5
        Skip = 6
        SkipNumberLength = 7
        SkipLengthPitch = 8
    

    class WeldJointBuilderJointMidPointData():
        JointMidPoint: Point3d
        JointTangent: Vector3d
        PrimaryFaceNormal: Vector3d
        SecondaryFaceNormal: Vector3d
        GroovePrimaryDirection: Vector3d
        GrooveAlignedWithPrimary: bool
        def ToString(self) -> str:
            ...
    

    class DestinationTypes(enum.Enum):
        WorkPart = 0
        NewComponent = 1
    

    class CoordinateSystem(enum.Enum):
        Absolute = 0
        Ship = 1
    

    class Application(enum.Enum):
        StructureWelding = 0
        Routing = 1
        StructureDesign = 2
    

class WeldJoint(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class WeldImportBuilder(Builder):
    def __init__(self) -> None: ...
    ConfirmWarningMessages: bool
    CreateFeatureGroups: bool
    InputFile: str
    TemplateFile: str


class WeldGroupIdColor(enum.Enum):
    None = 0
    First = 1
    Second = 2
    Third = 3
    Fourth = 4
    Fifth = 5
    Sixth = 6
    Seventh = 7
    Eighth = 8
    Ninth = 9
    Tenth = 10
    Eleventh = 11
    Twelfth = 12
    Thirteenth = 13
    Fourteenth = 14


class WeldGrooveType(enum.Enum):
    EdgesNotPrepared = 0
    EdgesPrepared = 1


class WeldGrooveShape(enum.Enum):
    SquareButt = 0
    VGroove = 1
    Bevel = 2
    UGroove = 3
    JGroove = 4
    FlaredV = 5
    FlaredBevel = 6
    FillinFlaredV = 7
    FillinFlaredBevel = 8


class WeldGrooveExtension(enum.Enum):
    Tangent = 0
    Project = 1
    ReverseProject = 2


class WeldGrooveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AssignWeldPMI: bool
    Characteristics: Weld.CharacteristicsBuilder
    ContourHeight: Expression
    ContourType: Weld.WeldGrooveBuilder.Contour
    CreateSkipWelds: bool
    DistanceTolerance: float
    EdgeSet1: Section
    EdgeSet2: Section
    EdgeType: Weld.WeldGrooveBuilder.Edge
    EndAngle: Expression
    EndDistance: GeometricUtilities.OnPathDimensionBuilder
    FaceSet1: ScCollector
    FaceSet2: ScCollector
    GrooveAngle: Expression
    GrooveRadius: Expression
    IsRootOpening: bool
    IsRootPenetration: bool
    Method: Weld.WeldGrooveBuilder.SkipWeldMethod
    NumberOfWelds: Expression
    PenetrationDepth: Expression
    PrepareEdges: Weld.WeldGrooveBuilder.Prepare
    RecreateDeletedWelds: bool
    RootOpening: Expression
    RootPenetration: Expression
    SecondPenetrationDepth: Expression
    SeedFace1: Face
    SeedFace2: Face
    SeedPoint1: Point3d
    SeedPoint2: Point3d
    SegmentLength: Expression
    SingleFaceSet: bool
    Spacing: Expression
    StartAngle: Expression
    StartDistance: GeometricUtilities.OnPathDimensionBuilder
    TaperMethod: Weld.WeldGrooveBuilder.Taper
    Type: Weld.WeldGrooveBuilder.Types
    Uparameter1: float
    Uparameter2: float
    UseFillin: bool
    Vparameter1: float
    Vparameter2: float
    WeldSymmetric: bool


    class Types(enum.Enum):
        SquareButt = 0
        VGroove = 1
        BevelGroove = 2
        UGroove = 3
        JGroove = 4
        FlaredVGroove = 5
        FlaredBevelGroove = 6
        FillinFlaredVGroove = 7
        FillinFlaredBevelGroove = 8
    

    class Taper(enum.Enum):
        FromEndFace = 0
        FromTopFace = 1
    

    class SkipWeldMethod(enum.Enum):
        NumberLength = 0
        NumberSpacing = 1
        SpacingLength = 2
    

    class Prepare(enum.Enum):
        None = 0
        EntireLength = 1
        WeldLimits = 2
        Complex = 3
    

    class Edge(enum.Enum):
        NotPrepared = 0
        Prepared = 1
    

    class Contour(enum.Enum):
        None = 0
        Convex = 1
        Flush = 2
        Concave = 3
    

class WeldGroove(Features.BodyFeature):
    def __init__(self) -> None: ...


class WeldFillStripBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Weld.WeldFillStripBuilder]) -> None:
        ...
    def Append(self, object: Weld.WeldFillStripBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Weld.WeldFillStripBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Weld.WeldFillStripBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Weld.WeldFillStripBuilder) -> None:
        ...
    def Erase(self, obj: Weld.WeldFillStripBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Weld.WeldFillStripBuilder]:
        ...
    def SetContents(self, objects: typing.List[Weld.WeldFillStripBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Weld.WeldFillStripBuilder, object2: Weld.WeldFillStripBuilder) -> None:
        ...
    def Insert(self, location: int, object: Weld.WeldFillStripBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class WeldFillStripBuilder(Builder):
    def __init__(self) -> None: ...
    def MoveToPoint(self, newCenter: Point3d) -> None:
        ...
    def MoveDelta(self, lengthDelta: float, widthDelta: float) -> None:
        ...
    def Split(self) -> Weld.WeldFillStripBuilder:
        ...
    def StretchPositive(self, lengthDelta: float) -> None:
        ...
    def StretchNegative(self, lengthDelta: float) -> None:
        ...
    def AlignPositive(self, alignStrip: Weld.WeldFillStripBuilder) -> None:
        ...
    def AlignNegative(self, alignStrip: Weld.WeldFillStripBuilder) -> None:
        ...
    def JoinPositive(self, joinStrip: Weld.WeldFillStripBuilder) -> None:
        ...
    def JoinNegative(self, joinStrip: Weld.WeldFillStripBuilder) -> None:
        ...
    Center: Point3d
    Length: float
    ToBeDeleted: bool


class WeldFillBuilder(Builder):
    def __init__(self) -> None: ...
    def NewFillStrip(self, center: Point3d, length: float) -> Weld.WeldFillStripBuilder:
        ...
    def DeleteFillStrip(self, fillStrip: Weld.WeldFillStripBuilder) -> None:
        ...
    Boundary: Section
    BoundaryMethod: Weld.WeldFillBuilder.BoundaryMethodType
    ChangeViewOrientation: bool
    Characteristics: Weld.CharacteristicsBuilder
    Corner1: Point
    Corner2: Point
    DistanceTolerance: float
    ExtendDistance: float
    ExtrudeHeight: float
    FillStripList: Weld.WeldFillStripBuilderList
    InnerBoundary: Section
    Orientation: CoordinateSystem
    PlacementFace: ScCollector
    SubdivideRegion: bool
    UseSeedFace: bool
    Width: float
    WidthAlong: Weld.WeldFillBuilder.WidthAlongType


    class WidthAlongType(enum.Enum):
        Xc = 0
        Yc = 1
    

    class BoundaryMethodType(enum.Enum):
        Rectangle = 0
        Curve = 1
    

class WeldFeatureSetType(enum.Enum):
    FilletWeld = 0
    GrooveWeld = 1
    ResistanceSpot = 2
    ArcSpot = 3
    Clinch = 4
    Dollop = 5
    WeldNut = 6
    WeldStud = 7
    Custom1Point = 8
    Custom2Point = 9
    Custom3Point = 10
    Custom4Point = 11
    Custom5Point = 12
    BiwDatumSurface = 13
    BiwDatumPin = 14
    BiwDatumCustomer1 = 15
    BiwDatumCustomer2 = 16
    BiwDatumCustomer3 = 17
    BiwMeasurementSurface = 18
    BiwMeasurementHole = 19
    BiwMeasurementSlot = 20
    BiwMeasurementStud = 21
    BiwMeasurementTrim = 22
    BiwMeasurementHem = 23
    BiwMeasurementCustomer1 = 24
    BiwMeasurementCustomer2 = 25
    BiwMeasurementCustomer3 = 26


class WeldFeatureOutput(enum.Enum):
    Curves = 0
    Solid = 1
    Both = 2


class WeldFacesetIndex(enum.Enum):
    First = 0
    Second = 1
    Third = 2
    Forth = 3


class WeldDatumControlDirection(enum.Enum):
    Invalid = -1
    X = 0
    Y = 1
    Z = 2


class WeldCustom(enum.Enum):
    SolidNone = 0
    SolidSphere = 1
    SolidCylinder = 2
    SolidCone = 3
    SolidDefault = 4


class WeldCreationDirection(enum.Enum):
    Default = 0
    Opposite = 1


class WeldCpdUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetJointCurvesFromWeldFeature(self, featureTag: NXObject) -> typing.List[Curve]:
        ...
    def GetDesignFeatureFromWeldFeature(self, featureTag: NXObject) -> typing.List[NXObject]:
        ...
    def Tag(self) -> Tag: ...



class WeldContourShape(enum.Enum):
    None = 0
    Convex = 1
    Flush = 2
    Concave = 3


class WeldBeadSizeBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Weld.WeldBeadSizeBuilder]) -> None:
        ...
    def Append(self, object: Weld.WeldBeadSizeBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Weld.WeldBeadSizeBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Weld.WeldBeadSizeBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Weld.WeldBeadSizeBuilder) -> None:
        ...
    def Erase(self, obj: Weld.WeldBeadSizeBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Weld.WeldBeadSizeBuilder]:
        ...
    def SetContents(self, objects: typing.List[Weld.WeldBeadSizeBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Weld.WeldBeadSizeBuilder, object2: Weld.WeldBeadSizeBuilder) -> None:
        ...
    def Insert(self, location: int, object: Weld.WeldBeadSizeBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class WeldBeadSizeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CustomSection: Section
    PathLocation: GeometricUtilities.OnPathDimensionBuilder
    RectangleBase: float
    RectangleHeight: float
    SemiMajor: float
    SemiMinor: float
    SizeString: Weld.WeldBeadSizeBuilder.Size
    ThroatThickness: float
    TriangleBase: float
    TriangleHeight: float
    TriangleMethod: Weld.WeldBeadSizeBuilder.TriangleMethodType
    TriangleType: Weld.WeldBeadSizeBuilder.TriangleTypes
    TubeDiameter: float


    class TriangleTypes(enum.Enum):
        OneSided = 0
        TwoSided = 1
    

    class TriangleMethodType(enum.Enum):
        LegLength = 0
        ThroatThickness = 1
    

    class Size(enum.Enum):
        Default1 = 0
        Default2 = 1
        Default3 = 2
        Default4 = 3
        Default5 = 4
        Custom = 5
    

class WeldBeadPathBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Weld.WeldBeadPathBuilder]) -> None:
        ...
    def Append(self, object: Weld.WeldBeadPathBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Weld.WeldBeadPathBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Weld.WeldBeadPathBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Weld.WeldBeadPathBuilder) -> None:
        ...
    def Erase(self, obj: Weld.WeldBeadPathBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Weld.WeldBeadPathBuilder]:
        ...
    def SetContents(self, objects: typing.List[Weld.WeldBeadPathBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Weld.WeldBeadPathBuilder, object2: Weld.WeldBeadPathBuilder) -> None:
        ...
    def Insert(self, location: int, object: Weld.WeldBeadPathBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class WeldBeadPathBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdatePath(self, pointFound: bool, evaluationPoint: Point3d, pathTangent: Vector3d, faceNormalWithFin: Vector3d, faceNormalOppositeFin: Vector3d) -> None:
        ...
    def GetSweepPath(self) -> Spline:
        ...
    def Validate(self) -> bool:
        ...
    CreateEndToStart: bool
    EndPath: GeometricUtilities.OnPathDimensionBuilder
    OffsetAlongNormal: Expression
    OffsetInFace: Expression
    OffsetMethod: Weld.WeldBeadPathBuilder.OffsetMethodType
    PathSection: Section
    ReverseOffsetDirection: bool
    StartPath: GeometricUtilities.OnPathDimensionBuilder


    class OffsetMethodType(enum.Enum):
        InFace = 0
        Centerline = 1
    

class WeldBeadBuilder(Builder):
    def __init__(self) -> None: ...
    def NewPath(self) -> Weld.WeldBeadPathBuilder:
        ...
    def NewSize(self) -> Weld.WeldBeadSizeBuilder:
        ...
    def GetPreviewPath(self) -> Spline:
        ...
    def CreatePreviewPath(self) -> Spline:
        ...
    BeadLocation: Weld.WeldBeadBuilder.BeadLocationMethod
    Characteristics: Weld.CharacteristicsBuilder
    DistanceTolerance: float
    ExtendToBoundary: bool
    FaceInferMethod: Weld.WeldBeadBuilder.FaceInferMethodType
    OutputType: Weld.WeldBeadBuilder.OutputTypes
    PathList: Weld.WeldBeadPathBuilderList
    SelectBottomParts: ScCollector
    SelectTopParts: ScCollector
    SizeList: Weld.WeldBeadSizeBuilderList
    TangentAngle: float
    TransformSketchToBeadCenterline: bool
    Type: Weld.WeldBeadBuilder.Types


    class Types(enum.Enum):
        Ellipse = 0
        Tube = 1
        Sketch = 2
        Triangle = 3
        Rectangle = 4
    

    class OutputTypes(enum.Enum):
        Fixed = 0
        Associative = 1
    

    class FaceInferMethodType(enum.Enum):
        TangentFaces = 0
        None = 1
    

    class BeadLocationMethod(enum.Enum):
        SecondaryParts = 0
        PrimaryParts = 1
        InSpace = 2
    

class WeldBead(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsWeldBead(self) -> bool:
        ...
    def GetConnectedBodies(self, connectedBodies: typing.List[Body]) -> None:
        ...
    def GetOutputCurve(self) -> Curve:
        ...
    def RemoveOutputCurveNoDelete(self) -> None:
        ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class WeldAttribType(enum.Enum):
    Integer = 1
    Real = 2
    Null = 4
    String = 5


class WeldArcMethod(enum.Enum):
    Continuous = 0
    Skip = 1


class WeldAdvisorCustomerDefault(enum.Enum):
    ResistanceSpot = 0
    ArcSpot = 1
    Clinch = 2
    Dollop = 3
    WeldNut = 4
    WeldStud = 5
    Custom1Point = 6
    Custom2Point = 7
    Custom3Point = 8
    Custom4Point = 9
    Custom5Point = 10
    Datum = 11
    Measurement = 12
    Num = 13


class WeldAdvisorCheckerType(enum.Enum):
    CoincidentPoint = 0
    MinimumPointDistance = 1
    MinimumEdgeDistance = 2
    StackUpGap = 3
    FacePlanarity = 4
    FaceParallelism = 5
    PointFaceDistance = 6
    CsysFaceNormalAngle = 7
    MetalStackUp = 8
    MetalMinimumPointDatumDistance = 9
    MetalMinimumPointMeasurementDistance = 10
    SpacingPerPanelCombination = 11
    WeldFlange = 12
    Bead = 13
    Number = 14


class WeldAdvisorBuilder(Builder):
    def __init__(self) -> None: ...
    def SetObjects(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def GetObjects(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def SetCheckers(self, checkers: typing.List[Weld.WeldAdvisorCheckerType]) -> None:
        ...
    def GetCheckers(self, checkers: typing.List[Weld.WeldAdvisorCheckerType]) -> None:
        ...
    def ReportResult(self, filePath: str) -> None:
        ...
    def SaveResult(self) -> None:
        ...
    def GetFailedObjects(self, checker: Weld.WeldAdvisorCheckerType, weldId: str, weldObjects: typing.List[Weld.LogInfo]) -> None:
        ...
    def GetReferenceObjects(self, weldObject: TaggedObject, checker: Weld.WeldAdvisorCheckerType, weldObjects: typing.List[Weld.LogInfo]) -> None:
        ...
    def SetMinimumEdgeDistance(self, type: Weld.WeldAdvisorCustomerDefault, minEdgeDist: float) -> None:
        ...
    def GetMinimumEdgeDistance(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMinimumEdgeDistanceWithSealer(self, type: Weld.WeldAdvisorCustomerDefault, minEdgeDistWithSealer: float) -> None:
        ...
    def GetMinimumEdgeDistanceWithSealer(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMinimumPointDistance(self, type: Weld.WeldAdvisorCustomerDefault, minPointDist: float) -> None:
        ...
    def GetMinimumPointDistance(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMaximumStackUpGap(self, type: Weld.WeldAdvisorCustomerDefault, maxFaceDist: float) -> None:
        ...
    def GetMaximumStackUpGap(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMaximumPointFaceDistance(self, type: Weld.WeldAdvisorCustomerDefault, pointFaceDist: float) -> None:
        ...
    def GetMaximumPointFaceDistance(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMaximumCsysFaceNormalAngle(self, type: Weld.WeldAdvisorCustomerDefault, csysFaceNmlAngle: float) -> None:
        ...
    def GetMaximumCsysFaceNormalAngle(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetCheckZoneRadius(self, type: Weld.WeldAdvisorCustomerDefault, faceRadius: float) -> None:
        ...
    def GetCheckZoneRadius(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetSealerCheckZoneRadius(self, type: Weld.WeldAdvisorCustomerDefault, faceRadiusWithSealer: float) -> None:
        ...
    def GetSealerCheckZoneRadius(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetPlanarityTolerance(self, type: Weld.WeldAdvisorCustomerDefault, facePlanarityTolerance: float) -> None:
        ...
    def GetPlanarityTolerance(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetParallelismTolerance(self, type: Weld.WeldAdvisorCustomerDefault, faceParallelismTolerance: float) -> None:
        ...
    def GetParallelismTolerance(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetFlangeCheckRadius(self, type: Weld.WeldAdvisorCustomerDefault, flangeRadius: float) -> None:
        ...
    def GetFlangeCheckRadius(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetFlangeCheckHeight(self, type: Weld.WeldAdvisorCustomerDefault, flangeHeight: float) -> None:
        ...
    def GetFlangeCheckHeight(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMinimumClosedAngle(self, type: Weld.WeldAdvisorCustomerDefault, minClosedAngle: float) -> None:
        ...
    def GetMinimumClosedAngle(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMaximumTotalMetalThickness(self, type: Weld.WeldAdvisorCustomerDefault, totalMetalThickness: float) -> None:
        ...
    def GetMaximumTotalMetalThickness(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetThicknessRatio(self, type: Weld.WeldAdvisorCustomerDefault, thicknessRatio: float) -> None:
        ...
    def GetThicknessRatio(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetThicknessOuterRatio(self, type: Weld.WeldAdvisorCustomerDefault, thicknessOuterRatio: float) -> None:
        ...
    def GetThicknessOuterRatio(self, type: Weld.WeldAdvisorCustomerDefault) -> float:
        ...
    def SetMaximumNumberLoosePanels(self, type: Weld.WeldAdvisorCustomerDefault, maxNumOfLoosePanels: int) -> None:
        ...
    def GetMaximumNumberLoosePanels(self, type: Weld.WeldAdvisorCustomerDefault) -> int:
        ...
    def InitializeSettings(self) -> None:
        ...
    def SetIncludeSealer(self, includeSealer: bool) -> None:
        ...
    def GetIncludeSealer(self) -> bool:
        ...
    def DeleteFeaturesFromResult(self, objects: typing.List[TaggedObject]) -> None:
        ...


class UserDefinedWeldBuilder(Builder):
    def __init__(self) -> None: ...
    AssignWeldPMI: bool
    Characteristics: Weld.CharacteristicsBuilder
    Class4gd: Weld.UserDefinedWeldBuilder.WeldTypes
    SelectBody: SelectDisplayableObjectList
    SelectConnectParts: ScCollector
    SelectEdge: SelectDisplayableObjectList


    class WeldTypes(enum.Enum):
        Groove = 0
        Fillet = 1
        PlugSlot = 2
        Bead = 3
        Fill = 4
    

class UserDefinedWeld(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class TransformBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    Characteristics: Weld.CharacteristicsBuilder
    ConnectedPartMethod: Weld.TransformBuilder.ConnectedPartMethods
    ConnectedPartTolerance: Expression
    Features: SelectNXObjectList
    MirrorPlane: Plane
    TranslateCsys: CoordinateSystem
    TranslateX: Expression
    TranslateY: Expression
    TranslateZ: Expression
    Type: Weld.TransformBuilder.TransformationTypes


    class TransformationTypes(enum.Enum):
        Mirror = 0
        Translate = 1
    

    class ConnectedPartMethods(enum.Enum):
        TransformBody = 0
        ParentFaces = 1
    

class Transform(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class SurfaceWeldBuilder(Weld.StructureWeldBuilder):
    def __init__(self) -> None: ...
    Boundary: Section
    Characteristics: Weld.CharacteristicsBuilder
    Destination: Weld.SurfaceWeldBuilder.DestinationTypes
    DistanceTolerance: float
    LineColorFontWidth: LineColorFontWidthBuilder
    NamePrefix: str
    Panel: ScCollector
    ProjectionDirection: GeometricUtilities.ProjectionOptions
    Thickness: Expression
    Width: Expression


    class DestinationTypes(enum.Enum):
        WorkPart = 0
        NewComponent = 1
    

class SurfaceWeld(Features.CurveFeature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class StructureWeldBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCommittedComponents(self) -> typing.List[Assemblies.Component]:
        ...


class SelectDatumSurface(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Weld.DatumSurface, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Weld.DatumSurface, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Weld.DatumSurface, view1: View, point1: Point3d, selection2: Weld.DatumSurface, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Weld.DatumSurface, view1: View, point1: Point3d, selection2: Weld.DatumSurface, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Weld.DatumSurface, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Weld.DatumSurface:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Weld.DatumSurface


class SelectDatumPin(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Weld.DatumPin, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Weld.DatumPin, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Weld.DatumPin, view1: View, point1: Point3d, selection2: Weld.DatumPin, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Weld.DatumPin, view1: View, point1: Point3d, selection2: Weld.DatumPin, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Weld.DatumPin, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Weld.DatumPin:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Weld.DatumPin


class PointMarkPointBuilder(Weld.JointmarkPointsBuilder):
    def __init__(self) -> None: ...


class PointMarkPoint(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetPointMarker(self) -> int:
        ...
    def IsPointMarkPoint(self) -> bool:
        ...
    def GetReferencePoint(self) -> Point:
        ...
    def GetConnectedBodies(self, connectedBodies: typing.List[Body]) -> None:
        ...
    def GetOutputPoint(self) -> Point:
        ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class PointMarkBuilder(Weld.JointmarkBuilder):
    def __init__(self) -> None: ...
    def NewPointsOverride(self) -> Weld.PointMarkPointBuilder:
        ...
    def AppendPointsOverride(self, create: bool) -> None:
        ...
    ShowSolids: bool
    WeldType: Weld.PointMarkBuilder.WeldTypes


    class WeldTypes(enum.Enum):
        ResistanceSpot = 0
        ArcSpot = 1
        Clinch = 2
        Dollop = 3
        WeldNut = 4
        WeldStud = 5
        Custom1 = 6
        Custom2 = 7
        Custom3 = 8
        Custom4 = 9
        Custom5 = 10
    

class PointMark(Features.Feature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class PlugSlotBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AssignWeldPMI: bool
    Characteristics: Weld.CharacteristicsBuilder
    ContourDepth: Expression
    ContourHeight: Expression
    ContourType: Weld.PlugSlotBuilder.EnumContour
    Edge1: Section
    Face1: ScCollector
    Face2: ScCollector
    FieldWeld: bool
    SeedFace1: Face
    SeedFace2: Face


    class EnumContour(enum.Enum):
        None = 0
        Convex = 1
        Flush = 2
        Concave = 3
    

    class ArcProcessEnum(enum.Enum):
        Gmaw = 0
        Gtaw = 1
        Gtac = 2
        Smaw = 3
        Paw = 4
    

class PlugSlot(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class OutputType(enum.Enum):
    Associative = 0
    Fixed = 1


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class LogInfo():
    Entity: TaggedObject
    LogMessage: str
    def ToString(self) -> str:
        ...
    def __init__(self, Entity: TaggedObject, LogMessage: str) -> None: ...


class LocatorReferenceBuilder(Builder):
    def __init__(self) -> None: ...
    def SetAdditionalReferenceFromFeature(self, additionalReference: Features.Feature) -> None:
        ...
    AdditionalReferences: Assemblies.SelectComponentList
    SelectLocator: SelectNXObjectList


class JointmarkPointsBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Weld.JointmarkPointsBuilder]) -> None:
        ...
    def Append(self, object: Weld.JointmarkPointsBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Weld.JointmarkPointsBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Weld.JointmarkPointsBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Weld.JointmarkPointsBuilder) -> None:
        ...
    def Erase(self, obj: Weld.JointmarkPointsBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Weld.JointmarkPointsBuilder]:
        ...
    def SetContents(self, objects: typing.List[Weld.JointmarkPointsBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Weld.JointmarkPointsBuilder, object2: Weld.JointmarkPointsBuilder) -> None:
        ...
    def Insert(self, location: int, object: Weld.JointmarkPointsBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class JointmarkPointsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateCsys(self, matrix: Matrix3x3) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Angle: Expression
    FlipDirection: bool
    MappingFeature: Features.SelectFeature
    Point: Point


    class PointPosition(enum.Enum):
        None = 0
        MovedAlongGuide = 1
        MovedOffGuide = 2
    

class JointmarkGuideBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Weld.JointmarkGuideBuilder]) -> None:
        ...
    def Append(self, object: Weld.JointmarkGuideBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Weld.JointmarkGuideBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Weld.JointmarkGuideBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Weld.JointmarkGuideBuilder) -> None:
        ...
    def Erase(self, obj: Weld.JointmarkGuideBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Weld.JointmarkGuideBuilder]:
        ...
    def SetContents(self, objects: typing.List[Weld.JointmarkGuideBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Weld.JointmarkGuideBuilder, object2: Weld.JointmarkGuideBuilder) -> None:
        ...
    def Insert(self, location: int, object: Weld.JointmarkGuideBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class JointmarkGuideBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateGuideCurves(self) -> None:
        ...
    def GetGuideCurves(self, guideCurves: typing.List[ICurve], instanceGuideCurves: typing.List[NXObject]) -> None:
        ...
    def RediscoverGuideEnds(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    EndDistance: GeometricUtilities.OnPathDimensionBuilder
    ExtendOffset: bool
    GuideCurve: Section
    LocationOption: Weld.JointmarkGuideBuilder.Location
    NumberOfPoints: int
    OffsetDistance: Expression
    RespacePoints: bool
    ReverseDirection: bool
    Section1: Section
    Section2: Section
    Section3: Section
    Section4: Section
    Spacing: Expression
    SpacingMethod: Weld.JointmarkGuideBuilder.SpaceMethod
    SpacingOption: Weld.JointmarkGuideBuilder.SpaceOption
    StartDistance: GeometricUtilities.OnPathDimensionBuilder


    class SpaceOption(enum.Enum):
        Distance = 0
        Number = 1
        MinimumDistance = 2
    

    class SpaceMethod(enum.Enum):
        ArcLength = 0
        ParallelXPlane = 1
        ParallelYPlane = 2
        ParallelZPlane = 3
    

    class Location(enum.Enum):
        CenterLine = 0
        OffsetFromEdge = 1
        ExistingCurve = 2
    

class JointmarkFaceSetsBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Weld.JointmarkFaceSetsBuilder]) -> None:
        ...
    def Append(self, object: Weld.JointmarkFaceSetsBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Weld.JointmarkFaceSetsBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Weld.JointmarkFaceSetsBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Weld.JointmarkFaceSetsBuilder) -> None:
        ...
    def Erase(self, obj: Weld.JointmarkFaceSetsBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Weld.JointmarkFaceSetsBuilder]:
        ...
    def SetContents(self, objects: typing.List[Weld.JointmarkFaceSetsBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Weld.JointmarkFaceSetsBuilder, object2: Weld.JointmarkFaceSetsBuilder) -> None:
        ...
    def Insert(self, location: int, object: Weld.JointmarkFaceSetsBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class JointmarkFaceSetsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FaceSelect: ScCollector


class JointmarkElement(Features.Feature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class JointmarkBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateFeatures(self) -> None:
        ...
    def UpdatePoint(self) -> None:
        ...
    def RediscoverFaces(self) -> None:
        ...
    def CreateReferenceData(self) -> None:
        ...
    def DeleteReferenceData(self) -> None:
        ...
    def SetDisplayCsys(self, status: bool) -> None:
        ...
    def SetShowThruState(self, status: bool) -> None:
        ...
    def NewGuide(self) -> Weld.JointmarkGuideBuilder:
        ...
    def NewFaceSets(self) -> Weld.JointmarkFaceSetsBuilder:
        ...
    def NewPoints(self) -> Weld.JointmarkPointsBuilder:
        ...
    def UpdateReferenceSheet(self, facesModified: bool) -> Features.Feature:
        ...
    def GetReferenceSheet(self) -> Features.Feature:
        ...
    def GetSheetEdges(self, edges: typing.List[Edge]) -> None:
        ...
    def CreateSymbolCurve(self, path: str, name: str) -> Curve:
        ...
    def AppendPoints(self, mode: bool, curve: Curve) -> None:
        ...
    def MapFeaturesToPoints(self) -> None:
        ...
    def FromReuseFeatures(self, faceSetsUpdated: bool, guideCurvesUpdated: bool, pointSelectionUpdated: bool) -> None:
        ...
    def GetSelectedReferences(self, references: typing.List[NXObject]) -> None:
        ...
    def GetCreateReferenceDataMessages(self, messages: str) -> None:
        ...
    def MoveReferenceSheet(self) -> None:
        ...
    def AskConnectedFaces(self) -> Weld.ConnectedPart:
        ...
    Associativity: bool
    Characteristics: Weld.CharacteristicsBuilder
    ConnectPart: bool
    ConnectPartType: Weld.JointmarkBuilder.ConnectPartTypes
    ConnectedPanelType: Weld.JointmarkBuilder.ConnectedPanelTypes
    ConstructionMethod: Weld.JointmarkBuilder.Method
    CreateSingleFeatures: bool
    DistanceTolerance: float
    FaceSetsList: Weld.JointmarkFaceSetsBuilderList
    FixedCsys: CoordinateSystem
    GuideCurvesList: Weld.JointmarkGuideBuilderList
    NotifyIfParentPointMoved: bool
    OrientationMethod: Weld.JointmarkBuilder.OrientationMethodTypes
    Plane: Plane
    PointList: Weld.JointmarkPointsBuilderList
    ProjectionDirectionOption: Weld.JointmarkBuilder.ProjectionDirectionOptions
    ReferenceSheetType: Weld.JointmarkBuilder.ReferenceSheetTypes
    ReuseFeatures: Features.SelectFeatureList
    ReuseFeaturesMethod: Weld.JointmarkBuilder.ReuseMethod
    SelectMirrorObject: SelectTaggedObjectList
    SelectPointsObject: SelectPointList
    SelectTranslateObject: SelectTaggedObjectList
    ShowWorkCsys: bool
    TranslateCsys: CoordinateSystem
    TranslateX: Expression
    TranslateY: Expression
    TranslateZ: Expression
    Vector: Direction


    class ReuseMethod(enum.Enum):
        SameConnectingParts = 0
        AnyConnectingParts = 1
    

    class ReferenceSheetTypes(enum.Enum):
        Overlap = 0
        Top = 1
    

    class ProjectionDirectionOptions(enum.Enum):
        None = 0
        AlongFaceNormal = 1
        PricipalAxis = 2
        X = 3
        Y = 4
        Z = 5
    

    class OrientationMethodTypes(enum.Enum):
        SurfaceNormal = 0
        CoordinateSystem = 1
    

    class Method(enum.Enum):
        GuideCurve = 0
        Mirror = 1
        Points = 2
        Translate = 3
        ExistingPoints = 4
    

    class ConnectPartTypes(enum.Enum):
        AllUniqueParts = 0
        OnlyOnePart = 1
        IgnoreFiltering = 2
    

    class ConnectedPanelTypes(enum.Enum):
        Two = 0
        Three = 1
        Four = 2
    

class Jointmark(Features.Feature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class JointItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Weld.JointItemBuilder]) -> None:
        ...
    def Append(self, object: Weld.JointItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Weld.JointItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Weld.JointItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Weld.JointItemBuilder) -> None:
        ...
    def Erase(self, obj: Weld.JointItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Weld.JointItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Weld.JointItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Weld.JointItemBuilder, object2: Weld.JointItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Weld.JointItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class JointItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def DeleteCurve(self) -> None:
        ...
    def ReadEdgePrepValues(self) -> Weld.EdgePrepValuesBuilder:
        ...
    def SaveEdgePrepValues(self, valuesBuilder: Weld.EdgePrepValuesBuilder) -> None:
        ...
    def GetPortEngagement(self) -> float:
        ...
    def SetCallbackMessage(self, message: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    BackingFace: ScCollector
    Curve: Curve
    Limits: Die.DieLimitsBuilder
    MasterEdge: ScCollector
    PlacementFace: ScCollector
    PrimaryEdge: ScCollector
    PrimaryFace: ScCollector
    RoutingObject: Routing.SelectPort
    SecondaryEdge: ScCollector
    SecondaryFace: ScCollector
    TargetFace: ScCollector
    UseCallbackValues: bool
    WeldType: int
    WeldingCharacteristics: Weld.CharacteristicsBuilder


class JointExitBuilder(Weld.WeldJointBuilder):
    def __init__(self) -> None: ...
    def GetEdgePrepValues(self, position: Weld.JointExitBuilder.Positions, thickness: float, angle: float) -> None:
        ...
    def SetEdgePrepValues(self, position: Weld.JointExitBuilder.Positions, thickness: float, angle: float) -> None:
        ...
    def GetFilletLengths(self) -> Weld.JointExitBuilder.FilletSizes:
        ...
    def SetFilletLengths(self, sizes: Weld.JointExitBuilder.FilletSizes) -> None:
        ...
    def GetOppositeFilletLengths(self) -> Weld.JointExitBuilder.FilletSizes:
        ...
    def SetOppositeFilletLengths(self, sizes: Weld.JointExitBuilder.FilletSizes) -> None:
        ...
    def SetBothFilletLengths(self, sizes: Weld.JointExitBuilder.FilletSizes) -> None:
        ...
    FinishMethod: Annotations.FinishMethod
    LeaveLooseEndValue: float
    LeaveLooseStartValue: float
    OtherSideSymbol: Annotations.Symbol
    RootOpening: float
    Side: Weld.JointExitBuilder.BodySide
    SymbolType: Annotations.Symbol


    class Positions(enum.Enum):
        UpperChamfer = 0
        Upper = 1
        Middle = 2
        Lower = 3
        LowerChamfer = 4
    

    class JointExitBuilderFilletSizes():
        ThroatThickness: float
        LegLength1: float
        LegLength2: float
        def ToString(self) -> str:
            ...
        def __init__(self, ThroatThickness: float, LegLength1: float, LegLength2: float) -> None: ...
    

    class BodySide(enum.Enum):
        First = 0
        Second = 1
    

class InformationBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTotalLength(self) -> float:
        ...
    def GetTotalVolume(self) -> float:
        ...
    AttributeOrigin: Weld.InformationBuilder.AttributeOriginType
    ConnectedToInformation: bool
    FabricationObjects: SelectNXObjectList
    OutputAttributes: bool
    OutputLengthAndVolume: bool


    class AttributeOriginType(enum.Enum):
        Object = 0
        Df = 1
    

class IFeature():
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class GrooveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetFirstFacesetStartAdjacentFaces(self, objects: typing.List[Face]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def GetFirstFacesetStartAdjacentFaces(self) -> typing.List[Face]:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def SetFirstFacesetEndAdjacentFaces(self, objects: typing.List[Face]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def GetFirstFacesetEndAdjacentFaces(self) -> typing.List[Face]:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def SetSecondFacesetStartAdjacentFaces(self, objects: typing.List[Face]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def GetSecondFacesetStartAdjacentFaces(self) -> typing.List[Face]:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def SetSecondFacesetEndAdjacentFaces(self, objects: typing.List[Face]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def GetSecondFacesetEndAdjacentFaces(self) -> typing.List[Face]:
        """[Obsolete("Deprecated in NX9.0.0.  This functionality is no longer supported.")"""
        ...
    def GetContourHeight(self) -> Expression:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.ContourHeightinstead.")"""
        ...
    def SetContourHeight(self, contourHeight: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.ContourHeightinstead.")"""
        ...
    def GetRootOpening(self) -> Expression:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.RootOpeninginstead.")"""
        ...
    def SetRootOpening(self, rootOpening: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.RootOpeninginstead.")"""
        ...
    def GetRootPenetration(self) -> Expression:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.RootPenetrationinstead.")"""
        ...
    def SetRootPenetration(self, rootPenetration: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.RootPenetrationinstead.")"""
        ...
    def GetGrooveAngle(self) -> Expression:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.GrooveAngleinstead.")"""
        ...
    def SetGrooveAngle(self, grooveAngle: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.GrooveAngleinstead.")"""
        ...
    def GetGrooveRadius(self) -> Expression:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.GrooveRadiusinstead.")"""
        ...
    def SetGrooveRadius(self, grooveAngle: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.GrooveRadiusinstead.")"""
        ...
    def GetPenetrationDepth(self) -> Expression:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.PenetrationDepthinstead.")"""
        ...
    def SetPenetrationDepth(self, penetrationDepth: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.PenetrationDepthinstead.")"""
        ...
    def GetSecondPenetrationDepth(self) -> Expression:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.SecondPenetrationDepthinstead.")"""
        ...
    def SetSecondPenetrationDepth(self, secondPenetrationDepth: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.SecondPenetrationDepthinstead.")"""
        ...
    def SetDistanceFromStart(self, startDistance: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.StartDistanceinstead.")"""
        ...
    def SetDistanceFromEnd(self, endDistance: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.EndDistanceinstead.")"""
        ...
    def SetTaperAtStart(self, startTaper: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.StartAngleinstead.")"""
        ...
    def SetTaperAtEnd(self, endTaper: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.EndAngleinstead.")"""
        ...
    def SetSpacingDistance(self, spacingDistance: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.Spacinginstead.")"""
        ...
    def SetNumberOfSegments(self, numSegments: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.NumberOfWeldsinstead.")"""
        ...
    def SetSegmentLength(self, segmentLength: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Weld.WeldGrooveBuilder.SegmentLengthinstead.")"""
        ...
    BottomExtension: Weld.WeldGrooveExtension
    ContourShape: Weld.WeldContourShape
    DistanceFromEnd: Expression
    DistanceFromStart: Expression
    FirstFaceset: ScCollector
    FirstFacesetBottomEdges: Section
    FirstFacesetHelpPoint: Point3d
    FirstFacesetTopEdges: Section
    GrooveShape: Weld.WeldGrooveShape
    GrooveType: Weld.WeldGrooveType
    IsFieldWeld: bool
    IsFirstFacesetNormalReversed: bool
    IsNumberOfSegments: bool
    IsSecondFacesetNormalReversed: bool
    IsSegmentLength: bool
    IsSpacing: bool
    Method: Weld.WeldArcMethod
    NumberOfSegments: Expression
    NumberRequiredFaceSets: int
    OutputGeometryType: Weld.WeldFeatureOutput
    OutputType: Weld.OutputType
    PrepareEdges: Weld.WeldPrepareEdges
    RootUpdate: Weld.WeldRootUpdate
    SecondFaceset: ScCollector
    SecondFacesetBottomEdges: Section
    SecondFacesetHelpPoint: Point3d
    SecondFacesetTopEdges: Section
    SegmentLength: Expression
    SequenceNumber: int
    SpacingDistance: Expression
    TaperAtEnd: Expression
    TaperAtStart: Expression
    TaperMethod: Weld.WeldTaperMethod
    TopExtension: Weld.WeldGrooveExtension


class Groove(Features.Feature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class FilletBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AddCosmeticEnd: bool
    AllowBroken: bool
    AssignWeldPMI: bool
    Associative: bool
    ConstructionMethod: Weld.FilletBuilder.EnumConstructionMethod
    ContourHeight: Expression
    ContourType: Weld.FilletBuilder.EnumContour
    DirectToggle: bool
    DirectionVector1: bool
    DirectionVector2: bool
    DistTolerance: float
    EdgeSet1: Section
    EdgeSet2: Section
    EndDist: GeometricUtilities.OnPathDimensionBuilder
    EndVector: bool
    EnumMethod: Weld.FilletBuilder.EnumSkipWeldMethod
    ExtendEdges: Weld.FilletBuilder.EnumExtendEdges
    ExtensionDistance: Expression
    ExtensionMethod: Weld.FilletBuilder.EnumExtensionMethod
    FaceFillGapDistance: float
    FaceSet1: ScCollector
    FaceSet2: ScCollector
    FieldWeld: bool
    FillFaceHoles: Weld.FilletBuilder.EnumFillFaceHolesType
    FilletType: Weld.FilletBuilder.EnumWeldingType
    FirstLeg: Expression
    NumberOfWelds: Expression
    Pmi: NXObject
    SecondLeg: Expression
    SeedFace1: Face
    SeedFace2: Face
    SeedPoint1: Point3d
    SeedPoint2: Point3d
    SegmentLength: Expression
    Spacing: Expression
    StartDist: GeometricUtilities.OnPathDimensionBuilder
    StartVector: bool
    ThroatThickToggle: bool
    ToggleCreateSkipWelds: bool
    ToggleRecreateDeletedWelds: bool
    Uparameter1: float
    Uparameter2: float
    Vparameter1: float
    Vparameter2: float
    WeldingCharacteristics: Weld.CharacteristicsBuilder


    class EnumWeldingType(enum.Enum):
        T = 0
        Lap = 1
        Corner = 2
    

    class EnumSkipWeldMethod(enum.Enum):
        NumberLength = 0
        NumberSpacing = 1
        SpacingLength = 2
    

    class EnumFillFaceHolesType(enum.Enum):
        None = 0
        Set1 = 1
        Set2 = 2
        Both = 3
    

    class EnumExtensionMethod(enum.Enum):
        Automatic = 0
        ByValue = 1
    

    class EnumExtendEdges(enum.Enum):
        Manual = 0
        Automatic = 1
    

    class EnumContour(enum.Enum):
        None = 0
        Convex = 1
        Flush = 2
        Concave = 3
    

    class EnumConstructionMethod(enum.Enum):
        Default = 0
        RollAround = 1
    

class Fillet(Features.BodyFeature):
    def __init__(self) -> None: ...
    def IsFillet(self) -> bool:
        ...
    def GetConnectedBodies(self, connectedBodies: typing.List[Body]) -> None:
        ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class Fill(Features.BodyFeature):
    def __init__(self) -> None: ...
    def GetFeatureDiagnostics(self, diagnosticCodes: int) -> None:
        ...
    def GetFeatureIconName(self) -> str:
        ...
    def GetFeatureLayer(self) -> int:
        ...
    def GetFeatureObjectColor(self) -> int:
        ...
    def GetFeatureReferenceSets(self, refSet: typing.List[ReferenceSet]) -> None:
        ...
    def GetFeatureReferenceSetStrings(self, refSet: str) -> None:
        ...


class Extract(Features.Feature):
    def __init__(self) -> None: ...
    def CompressFace(self) -> None:
        ...


class ExportWeldJointBuilder(Weld.ExportWeldBuilder):
    def __init__(self) -> None: ...
    ChordalTolerance: Expression
    IncludeAttributesFromMAG: bool
    OutputFaceInfo: Weld.ExportWeldJointBuilder.OutputFaceInfoTypes
    OutputFilletFaceInfo: bool
    ProjectToTarget: bool
    WorkCoordinateSystem: CoordinateSystem


    class OutputFaceInfoTypes(enum.Enum):
        None = 0
        ForFilletsOnly = 1
        All = 2
    

class ExportWeldBuilder(Builder):
    def __init__(self) -> None: ...
    def GetExportedAttributes(self) -> str:
        ...
    def SetExportedAttributes(self, exportedAttributes: str) -> None:
        ...
    def GetConnectedPartAttributes(self) -> str:
        ...
    def SetConnectedPartAttributes(self, connectedPartAttributes: str) -> None:
        ...
    def ReadAttributesFromWelds(self) -> None:
        ...
    def SaveAsDefault(self) -> None:
        ...
    def RestoreDefault(self) -> None:
        ...
    def SaveToFile(self) -> None:
        ...
    def OpenFromFile(self) -> None:
        ...
    AttributeOrigin: Weld.ExportWeldBuilder.AttributeOriginType
    ConnectedPartAttrToggle: bool
    CsvFileName: str
    Output: Weld.ExportWeldBuilder.OutputType
    TemplateFileName: str
    WeldPoints: SelectNXObjectList


    class OutputType(enum.Enum):
        IntermediateFile = 0
        InformationWindow = 1
    

    class AttributeOriginType(enum.Enum):
        Object = 0
        Df = 1
    

class EdgePrepValuesBuilder(Builder):
    def __init__(self) -> None: ...
    def RecreateCurves(self) -> None:
        ...
    def DeleteExitBuilder(self) -> None:
        ...
    def ReadEdgePrepValues(self, feature: Features.Feature) -> None:
        ...
    def ReadEdgePrepValuesFromCurve(self, curve: Curve) -> None:
        ...
    def GetSegmentFromIndex(self, value: int) -> Curve:
        ...
    def CreatePathCurvesForLeaveLoose(self, path: Curve, reversedPath: Curve) -> None:
        ...
    EdgesPrepared: bool
    EditingManagedAttributeGroup: bool
    Joint: SelectCurveList
    JointExitBuilder: Weld.JointExitBuilder
    LeaveLooseEndValue: GeometricUtilities.OnPathDimensionBuilder
    LeaveLooseStartValue: GeometricUtilities.OnPathDimensionBuilder
    PrimaryThicknessUser: float
    RootOpening: float
    SecondaryThicknessUser: float
    ValueSegment: SelectCurve
    ValuesApplyOption: Weld.EdgePrepValuesBuilder.Apply
    ValuesOption: Weld.EdgePrepValuesBuilder.Option


    class Option(enum.Enum):
        Entered = 0
        Computed = 1
    

    class Apply(enum.Enum):
        ToAllValues = 0
        ToChangedValuesOnly = 1
    

class EdgePrepBuilder(Builder):
    def __init__(self) -> None: ...
    def GetNoResultsInfo(self) -> typing.List[Curve]:
        ...
    ErrorCode: int
    WeldObjects: SelectNXObjectList


class EdgePrep(Features.BodyFeature):
    def __init__(self) -> None: ...


class EasyPatternBuilder(Builder):
    def __init__(self) -> None: ...
    BackEdgeOffset: float
    DistanceTolerance: float
    GridAngleTolerance: float
    GridIncrement: float
    Height: float
    HemMethod: Weld.EasyPatternBuilder.HemMethodTypes
    LengthAndWidth: float
    MaximumSpacing: float
    MinimumFlangeWidth: float
    NumberSurfaceVectors: int
    PatternPath: Section
    PlaneLocation: float
    PlaneMethod: Weld.EasyPatternBuilder.PlaneMethodTypes
    ReverseDirection: bool
    SpacingMethod: Weld.EasyPatternBuilder.SpacingMethodTypes
    SurfaceVectorFace: ScCollector
    TrimEdgeOffset: float
    Type: Weld.EasyPatternBuilder.Types


    class Types(enum.Enum):
        TrimAndSurface = 0
        HemAndSurface = 1
    

    class SpacingMethodTypes(enum.Enum):
        Grid = 0
        SinglePlane = 1
    

    class PlaneMethodTypes(enum.Enum):
        InferPlanes = 0
        ParallelXCPlanes = 1
        ParallelYCPlanes = 2
        ParallelZCPlanes = 3
    

    class HemMethodTypes(enum.Enum):
        MidPoint = 0
        NormalToBody = 1
    

class DatumSurfaceBuilder(Weld.DatumCommonBuilder):
    def __init__(self) -> None: ...
    def MoveMinimumDistance(self) -> None:
        ...
    def InitializeAxis(self, approximatePoint: Point3d) -> None:
        ...
    def UpdateAxisData(self) -> None:
        ...
    def UpdateWithReferenceDatum(self) -> None:
        ...
    DerivedDatum: Weld.SelectDatumSurface
    GridSnapTolerance: float
    MirrorPlane: Plane
    RestingFace: ScCollector
    SnapPointToGrid: bool
    Type: Weld.DatumSurfaceBuilder.Types
    XCoordinate: float
    YCoordinate: float
    ZCoordinate: float


    class Types(enum.Enum):
        Direct = 0
        Mirror = 1
    

class DatumSurface(Features.Feature):
    def __init__(self) -> None: ...


class DatumPinBuilder(Weld.DatumCommonBuilder):
    def __init__(self) -> None: ...
    def MoveToCenter(self) -> None:
        ...
    def InitializeAxis(self) -> None:
        ...
    def UpdateAxisData(self) -> None:
        ...
    BoundaryCurve: ScCollector
    DerivedDatum: Weld.SelectDatumPin


class DatumPin(Features.Feature):
    def __init__(self) -> None: ...


class DatumIconBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CustomType: Weld.DatumCommonBuilder.CustomTypes
    DatumPin: Weld.DatumPin
    DatumSurface: Weld.DatumSurface
    Derived: bool
    IconName: str


class DatumCommonBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateWithDerivedDatum(self) -> None:
        ...
    AdditionalReferences: Assemblies.SelectComponentList
    Characteristics: Weld.CharacteristicsBuilder
    ControlMethod: Weld.DatumCommonBuilder.ControlMethodTypes
    CreateDirectionVector: bool
    CreatePlane: bool
    CreatePoint: bool
    CreationDirection: Weld.DatumCommonBuilder.CreationDirectionMethods
    CustomAboveLength: float
    CustomRadius: float
    CustomTotalLength: float
    CustomType: Weld.DatumCommonBuilder.CustomTypes
    CustomTypeName: str
    Derived: bool
    DirectionAxis: Axis
    DirectionLength: float
    ModelingTolerance: float
    PlaneHeight: float
    PlaneWidth: float
    PrincipalAxisX: bool
    PrincipalAxisY: bool
    PrincipalAxisZ: bool
    ProjectAlongDirection: bool
    SectionPlaneNormal: Direction
    SolidType: Weld.DatumCommonBuilder.SolidTypes


    class SolidTypes(enum.Enum):
        Sphere = 0
        Cylinder = 1
        Cone = 2
    

    class CustomTypes(enum.Enum):
        Default = 0
        Custom1 = 1
        Custom2 = 2
        Custom3 = 3
        Custom4 = 4
        Custom5 = 5
        Custom6 = 6
        Custom7 = 7
    

    class CreationDirectionMethods(enum.Enum):
        Default = 0
        Opposite = 1
    

    class ControlMethodTypes(enum.Enum):
        PrincipalAxis = 0
        UseSectionPlane = 1
    

class CustomManager(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Weld.EdgePrep]:
        ...
    def __init__(self, owner: Session) -> None: ...
    def __init__(self) -> None: ...
    def AddWeldJointHandler(self, handler: Weld.CustomManager.WeldJointHandler) -> int:
        ...
    def RemoveWeldJointHandler(self, id: int) -> None:
        ...
    def AddVariableBevelHandler(self, handler: Weld.CustomManager.VariableBevelHandler) -> int:
        ...
    def RemoveVariableBevelHandler(self, id: int) -> None:
        ...
    def AddModifyFeatureHandler(self, handler: Weld.CustomManager.ModifyFeatureHandler) -> int:
        ...
    def RemoveModifyFeatureHandler(self, id: int) -> None:
        ...
    def AddPointExitHandler(self, handler: Weld.CustomManager.PointExitHandler) -> int:
        ...
    def RemovePointExitHandler(self, id: int) -> None:
        ...
    def AddDatumIconHandler(self, handler: Weld.CustomManager.DatumIconHandler) -> int:
        ...
    def RemoveDatumIconHandler(self, id: int) -> None:
        ...
    def AddPipeJointSetType(self, handler: Weld.CustomManager.PipeJointSetType) -> int:
        ...
    def RemovePipeJointSetType(self, id: int) -> None:
        ...
    def AddJointPmiCreated(self, handler: Weld.CustomManager.JointPmiCreated) -> int:
        ...
    def RemoveJointPmiCreated(self, id: int) -> None:
        ...
    def ShowSolids(self, showSolids: bool) -> None:
        ...
    def LocateWelds(self, searchEntireAssembly: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool, foundObjectsArray: typing.List[NXObject]) -> None:
        ...
    def LocateWelds(self, searchEntireAssembly: bool, excludeInvisibleComponents: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool, foundObjectsArray: typing.List[NXObject]) -> None:
        ...
    def LocateWelds(self, searchEntireAssembly: bool, excludeInvisibleComponents: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool, wantStructureWelds: bool, foundObjectsArray: typing.List[NXObject]) -> None:
        ...
    def ConvertLegacy(self) -> None:
        ...
    def ConvertLegacy(self, fsetFeatures: typing.List[Features.Feature]) -> None:
        ...
    def ConvertLegacy(self, fsetFeatures: typing.List[Features.Feature], createSingleFeatures: bool) -> None:
        ...
    def CreateFeatureGroupsForCommonConnectedParts(self, weldFeatures: typing.List[Weld.JointmarkElement]) -> None:
        ...
    def AskConnectedParts(self, weldTag: NXObject) -> Weld.ConnectedPart:
        ...
    def ImpactAnalysisCheck(self, selectedObjects: typing.List[NXObject]) -> None:
        ...
    def ImpactAnalysisConfirm(self, selectedObjects: typing.List[NXObject]) -> None:
        ...
    def ImpactAnalysisCheckConnectedParts(self, selectedObjects: typing.List[NXObject]) -> None:
        ...
    def ConvertTransformWeld(self, selectedObjects: typing.List[Features.Feature]) -> None:
        ...
    def DeleteDesignFeatures(self, deleteOption: Weld.CustomManager.DeleteOption, designObject: TaggedObject) -> None:
        ...
    def HasSourceFacesInWeldPart(self, weldFeature: Features.Feature) -> bool:
        ...
    def Tag(self) -> Tag: ...



    

    

    

    class PmiSource(enum.Enum):
        Preview = 0
        FabricationPmi = 1
    

    

    

    

    class DeleteOption(enum.Enum):
        All = 0
        InputOnly = 1
    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

class ConnectionFinderBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def ReorderBeforeFaceNode(self, parentTag: NXObject, faceSetIndexToMove: int, faceSetIndexToReoderBefore: int) -> None:
        ...
    def ReorderAfterFaceNode(self, parentTag: NXObject, faceSetIndexToMove: int, faceSetIndexToReoderAfter: int) -> None:
        ...
    def CenterNode(self, nodeTag: NXObject) -> None:
        ...
    def DeleteNode(self, nodeTag: NXObject) -> None:
        ...
    def SaveAllTree(self) -> None:
        ...
    def ClearAllTree(self) -> None:
        ...
    def SaveNode(self, nodeTag: NXObject) -> None:
        ...
    def ReassignFaceNode(self, ownerTag: NXObject, nodeTag: NXObject) -> None:
        ...
    def ClearMarking(self, nodeTag: NXObject) -> None:
        ...
    def IsFaceNodeEmpty(self, weldObject: NXObject, faceNodeIndex: int) -> bool:
        ...
    def GetFaceNodeCollector(self, weldObject: NXObject, faceNodeIndex: int) -> ScCollector:
        ...
    def ReorderBeforeEdgeNode(self, parentTag: NXObject, edgeSetIndexToMove: int, edgeSetIndexToReoderBefore: int) -> None:
        ...
    def ReorderAfterEdgeNode(self, parentTag: NXObject, edgeSetIndexToMove: int, edgeSetIndexToReoderAfter: int) -> None:
        ...
    def ReassignEdgeNode(self, ownerTag: NXObject, nodeTag: NXObject) -> None:
        ...
    def IsEdgeNodeEmpty(self, weldObject: NXObject, edgeNodeIndex: int) -> bool:
        ...
    def GetEdgeNodeCollector(self, weldObject: NXObject, edgeNodeIndex: int) -> ScCollector:
        ...
    def RequiredFaceNode(self, nodeTag: NXObject, isRequired: bool) -> None:
        ...
    def GetFaces(self, weldObject: NXObject) -> typing.List[ScCollector]:
        ...
    def Validate(self) -> bool:
        ...
    Filter: Weld.ConnectionFinderBuilder.FilterTypes
    ListFeatureSet: bool
    ReassignEdge: ScCollector
    ReassignFace: ScCollector
    UpdateCoordinateSystem: bool


    class FilterTypes(enum.Enum):
        All = 0
        Passed = 1
        Warning = 2
        Failed = 3
        Saved = 4
        NotSaved = 5
        Deleted = 6
    

class ConnectedPart(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNumberSets(self) -> int:
        ...
    def GetSetInformation(self, setIndex: int, eids: typing.List[NXObject]) -> None:
        ...


class ConnectedFaceFinderBuilder(Builder):
    def __init__(self) -> None: ...
    def PerformAnalysis(self) -> None:
        ...
    ConnectionFinder: Weld.ConnectionFinderBuilder
    ListFeatureSet: bool
    RetainedWelds: SelectTaggedObjectList


class CompoundWeldBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Side1Welds: Features.SelectFeatureList
    Side2Welds: Features.SelectFeatureList
    Staggered: bool


class CompoundWeld(Features.Feature):
    def __init__(self) -> None: ...


class CharacteristicsValueBuilder(NXObject):
    def __init__(self) -> None: ...
    def GetOptionStrings(self, strings: str) -> None:
        ...
    Active: bool
    AttributeType: Weld.CharacteristicsValueBuilder.Type
    Inherited: bool
    Required: bool
    Title: str
    ValueChanged: bool
    ValueDouble: float
    ValueInteger: int
    ValueString: str


    class Type(enum.Enum):
        String = 0
        Integer = 1
        Double = 2
        Option = 3
        None = 4
    

class CharacteristicsSelectionBuilder(NXObject):
    def __init__(self) -> None: ...
    def CreateIntegerAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: int) -> Weld.CharacteristicsValueBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Weld.CharacteristicsSelectionBuilder.CreateIntegerAttributeListEntry with inherited parameter instead.")"""
        ...
    def CreateIntegerAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: int) -> Weld.CharacteristicsValueBuilder:
        ...
    def CreateDoubleAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: float) -> Weld.CharacteristicsValueBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Weld.CharacteristicsSelectionBuilder.CreateDoubleAttributeListEntry with inherited parameter instead.")"""
        ...
    def CreateDoubleAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: float) -> Weld.CharacteristicsValueBuilder:
        ...
    def CreateAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str) -> Weld.CharacteristicsValueBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Weld.CharacteristicsSelectionBuilder.CreateAttributeListEntry with inherited parameter instead.")"""
        ...
    def CreateAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str) -> Weld.CharacteristicsValueBuilder:
        ...
    def CreateStringAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str) -> Weld.CharacteristicsValueBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Weld.CharacteristicsSelectionBuilder.CreateStringAttributeListEntry with inherited parameter instead.")"""
        ...
    def CreateStringAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str) -> Weld.CharacteristicsValueBuilder:
        ...
    def CreateOptionAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str, options: str) -> Weld.CharacteristicsValueBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Weld.CharacteristicsSelectionBuilder.CreateOptionAttributeListEntry with inherited parameter instead.")"""
        ...
    def CreateOptionAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str, options: str) -> Weld.CharacteristicsValueBuilder:
        ...
    AttributeList: NXObjectList
    SelectObjectList: SelectNXObjectList


class CharacteristicsBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateSelectionSet(self, weldType: int, data: NXObject) -> Weld.CharacteristicsSelectionBuilder:
        """[Obsolete("Deprecated in NX9.0.0.  Use overloaded function with enum instead.")"""
        ...
    def CreateSelectionSet(self, charxType: Weld.CharacteristicsBuilder.Type, data: NXObject) -> Weld.CharacteristicsSelectionBuilder:
        ...
    def ApplyAttributes(self, objects: typing.List[NXObject]) -> None:
        ...
    def RemoveInheritedAttributes(self) -> None:
        ...
    def RemoveAllAttributes(self, objects: typing.List[NXObject]) -> None:
        ...
    def ApplyAttributesToSelected(self) -> None:
        ...
    def InheritAttributesFromObject(self, object: NXObject) -> None:
        ...
    def CopyAttributesFromObject(self, object: NXObject) -> None:
        ...
    def CopyNonActiveAttributesFromObject(self, object: NXObject) -> None:
        ...
    def DoesObjectHaveAttributes(self, object: NXObject) -> bool:
        ...
    def HasActiveValues(self) -> bool:
        ...
    def AreAttributesDefault(self, weldType: int) -> bool:
        """[Obsolete("Deprecated in NX9.0.0.  Use overloaded function with enum instead.")"""
        ...
    def AreAttributesDefault(self, charxType: Weld.CharacteristicsBuilder.Type) -> bool:
        ...
    def ChangeFeatureType(self, weldType: int) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use overloaded function with enum instead.")"""
        ...
    def ChangeFeatureType(self, charxType: Weld.CharacteristicsBuilder.Type) -> None:
        ...
    def SetAllAttributesChanged(self) -> None:
        ...
    def SetAllAttributesChanged(self, status: bool) -> None:
        ...
    def CopyAttributesFromObjectForPaint(self, objectTag: NXObject) -> None:
        ...
    InheritObject: SelectNXObject
    Selected: Weld.CharacteristicsValueBuilder
    SelectionList: NXObjectList


    class Type(enum.Enum):
        None = 0
        FilletFeature = 24
        GrooveFeature = 25
        ResistanceSpotFeature = 26
        ArcSpotFeature = 27
        ClinchFeature = 28
        DollopFeature = 29
        WeldNutFeature = 30
        WeldStudFeature = 31
        Custom1PointFeature = 32
        Custom2PointFeature = 33
        Custom3PointFeature = 34
        Custom4PointFeature = 35
        Custom5PointFeature = 36
        DatumSurfaceFeature = 37
        DatumPinFeature = 38
        DatumCustom1Feature = 39
        DatumCustom2Feature = 40
        DatumCustom3Feature = 41
        MeasurementSurfaceFeature = 42
        MeasurementHoleFeature = 43
        MeasurementSlotFeature = 44
        MeasurementStudFeature = 45
        MeasurementTrimFeature = 46
        MeasurementHemFeature = 47
        MeasurementCustom1Feature = 48
        MeasurementCustom2Feature = 49
        MeasurementCustom3Feature = 50
        UserDefinedFeature = 51
        SealerFillFeature = 52
        SealerBeadFeature = 53
        JointFeature = 54
        PlugSlotFeature = 55
        ShipHull = 57
        ShipDeck = 58
        ShipTransverseBulkhead = 59
        ShipLongitudinalBulkhead = 60
        ShipGenericPlate = 61
        ShipStiffener = 62
        ShipEdgeReinforcement = 63
        ShipSeam = 64
        DatumSurfaceCustom0 = 65
        DatumSurfaceCustom1 = 66
        DatumSurfaceCustom2 = 67
        DatumSurfaceCustom3 = 68
        DatumSurfaceCustom4 = 69
        DatumSurfaceCustom5 = 70
        DatumSurfaceCustom6 = 71
        DatumSurfaceCustom7 = 72
        DatumPinCustom0 = 73
        DatumPinCustom1 = 74
        DatumPinCustom2 = 75
        DatumPinCustom3 = 76
        DatumPinCustom4 = 77
        DatumPinCustom5 = 78
        DatumPinCustom6 = 79
        DatumPinCustom7 = 80
        SurfaceWeld = 81
        ShipProfileCutOut = 82
        JointmarkFeature = 83
        ShipStandardPart = 84
        PointMarkResistanceSpot = 85
        PointMarkArcSpot = 86
        PointMarkDollop = 87
        PointMarkClinch = 88
        PointMarkWeldNut = 89
        PointMarkWeldStud = 90
        PointMarkCustom1 = 91
        PointMarkCustom2 = 92
        PointMarkCustom3 = 93
        PointMarkCustom4 = 94
        PointMarkCustom5 = 95
        ShipBracket = 96
        ShipCollarPlate = 97
    

class AutoWeldSymbolsBuilder(Builder):
    def __init__(self) -> None: ...
    DraftingViews: Drawings.SelectDraftingViewList
    Welds: SelectNXObjectList


    class ZDirection(enum.Enum):
        FaceNormal = 0
        Opposite = 1
    

class AutoPointBuilder(Builder):
    def __init__(self) -> None: ...
    def FindNumberOfInterferenceRegions(self) -> int:
        ...
    def CreateFeatureSet(self, interferenceIndex: int) -> NXObject:
        ...
    def GetInterferenceDetails(self, interferenceIndex: int) -> Weld.AutoPointBuilder.InterferenceDetails:
        ...
    def GetWeldType(self) -> Weld.PointMarkBuilder.WeldTypes:
        ...
    def SetWeldType(self, weldType: Weld.PointMarkBuilder.WeldTypes) -> None:
        ...
    def SetDisplayCsys(self, showCsys: bool) -> None:
        ...
    def SetShowThruState(self, showThruState: bool) -> None:
        ...
    def SetShowSolids(self, showSolids: bool) -> None:
        ...
    ComponentsToJoin: Assemblies.SelectComponentList
    ComponentsTreatAsUnit: Assemblies.SelectComponentList
    DefaultZDirection: Weld.AutoPointBuilder.ZDirection
    DistanceFromEnds: float
    FaceGapDistance: float
    ManipulatorMatrix: Matrix3x3
    MaximumBendRadius: float
    MaximumCenterlineWidth: float
    MaximumSingleThickness: float
    MaximumSpacingBetweenPoints: float
    MimimumNumberPointsOnOverlap: int
    MinimumFlangeWidth: float
    MinimumSpacingBetweenPoints: float
    OffsetDistanceFromEdge: float
    OrientationMethod: Weld.AutoPointBuilder.OrientationMethodTypes
    ReuseFeatures: Features.SelectFeatureList
    ReuseMatchTolerance: float
    Type: Weld.AutoPointBuilder.Types
    UniformSpacingTolerance: float
    WeldType: Weld.WeldFeatureSetType


    class Types(enum.Enum):
        New = 0
        Move = 1
    

    class OrientationMethodTypes(enum.Enum):
        SurfaceNormal = 0
        CoordinateSystem = 1
    

    class InterferenceDetails(enum.Enum):
        NoWeldsNearBodies = 0
        Same = 1
        Replaced = 2
        Added = 3
        Deleted = 4
    

class AutoPoint(Features.Feature):
    def __init__(self) -> None: ...


class _LogInfo():
    entity: Tag
    log_message: int


