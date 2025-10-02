from ....NXOpen import *
from ...Features import *
from ..SheetMetal import *

import typing
import enum

class UnbendBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def ValidateBuilderData(self) -> int:
        ...
    AddedGeometry: Section
    ExtractGussetCurves: bool
    FaceCollector: ScCollector
    HideOriginalCurves: bool
    ReferenceEntity: NXObject


class ThreeBendCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AddFacePair(self, firstFace: Face, secondFace: Face) -> None:
        ...
    def RemoveFacePair(self, firstFace: Face, secondFace: Face) -> None:
        ...
    def GetFacePair(self, index: int, firstFace: Face, secondFace: Face) -> None:
        ...
    def SetDiameter(self, diameter: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.ThreeBendCornerBuilder.Diameter instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    BlendMiter: bool
    BlendMiterRadius: Expression
    Diameter: Expression
    FlangeClearance: Expression
    MiterCorner: bool
    MiterRootRadius: Expression
    NumberOfFacePairs: int
    Offset: Expression
    OriginType: Features.SheetMetal.ThreeBendCornerBuilder.OriginTypes
    TreatmentType: Features.SheetMetal.ThreeBendCornerBuilder.TreatmentTypeOptions
    VCutoutAngle1: Expression
    VCutoutAngle2: Expression


    class TreatmentTypeOptions(enum.Enum):
        Open = 0
        Closed = 1
        CircularCutout = 2
        UCutout = 3
        VCutout = 4
    

    class OriginTypes(enum.Enum):
        BendCenter = 0
        CornerPoint = 1
    

class TabBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def SetThickness(self, thickness: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.TabBuilder.Thickness instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    def UpdateReferenceCurves(self) -> Features.Feature:
        ...
    IsSecondary: bool
    MaterialSide: Features.SheetMetal.TabBuilder.SectionSideOptions
    MultiBendPropertiesList: Features.SheetMetal.FeatureBendPropertiesListBuilder
    Section: Section
    Sketch: Features.SketchFeature
    TargetBody: Body
    Thickness: Expression
    ThicknessSide: Features.SheetMetal.TabBuilder.ThicknessSideOptions


    class ThicknessSideOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

    class SectionSideOptions(enum.Enum):
        Left = 0
        Right = 1
    

class SolidPunchBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AutoCentroid: bool
    ConstantThickness: bool
    DieRadius: Expression
    FromCsys: CoordinateSystem
    HideTool: bool
    IncludeRounding: bool
    InferThickness: bool
    PierceFaces: SelectFaceList
    PunchRadius: Expression
    TargetFace: SelectFace
    Thickness: Expression
    ToCsys: CoordinateSystem
    ToolBody: SelectBody
    Type: Features.SheetMetal.SolidPunchBuilder.Types


    class Types(enum.Enum):
        PunchType = 0
        DieType = 1
    

class SMBoundaryConditionBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.SheetMetal.SMBoundaryConditionBuilder]) -> None:
        ...
    def Append(self, object: Features.SheetMetal.SMBoundaryConditionBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.SheetMetal.SMBoundaryConditionBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.SheetMetal.SMBoundaryConditionBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.SMBoundaryConditionBuilder) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.SMBoundaryConditionBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.SheetMetal.SMBoundaryConditionBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.SheetMetal.SMBoundaryConditionBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.SheetMetal.SMBoundaryConditionBuilder, object2: Features.SheetMetal.SMBoundaryConditionBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.SheetMetal.SMBoundaryConditionBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SMBoundaryConditionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ConstraintName: str
    ConstraintType: Features.SheetMetal.SMBoundaryConditionBuilder.ConstraintTypes
    EndRegionCurve: ScCollector
    EndRegionPoint: Point
    StartRegionCurve: ScCollector
    StartRegionPoint: Point


    class ConstraintTypes(enum.Enum):
        PointToPoint = 0
        PointAlongCurve = 1
        CurveToCurve = 2
        CurveAlongCurve = 3
    

class SheetmetalManagerTabType(enum.Enum):
    Base = 0
    Secondary = 1


class SheetmetalManagerTabSweepDir(enum.Enum):
    Normal = 0
    OppositeToNormal = 1


class SheetmetalManagerFlangeWidthOption(enum.Enum):
    CustomizeWidth = -1
    FullWidth = 0
    Centred = 1
    AtEnd = 2
    FromBothEnds = 3
    FromEnd = 4


class SheetmetalManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateDimpleFeatureBuilder(self, dimple: Features.Feature) -> Features.SheetMetal.DimpleBuilder:
        ...
    def CreateDrawnCutoutFeatureBuilder(self, dCutout: Features.Feature) -> Features.SheetMetal.DrawnCutoutBuilder:
        ...
    def CreateLighteningCutoutBuilder(self, lighteningCutout: Features.SheetMetal.LighteningCutout) -> Features.SheetMetal.LighteningCutoutBuilder:
        ...
    def CreateLouverFeatureBuilder(self, louver: Features.Feature) -> Features.SheetMetal.LouverBuilder:
        ...
    def CreateBeadFeatureBuilder(self, bead: Features.Feature) -> Features.SheetMetal.BeadBuilder:
        ...
    def CreateFlangeFeatureBuilder(self, dCutout: Features.Feature) -> Features.SheetMetal.FlangeBuilder:
        ...
    def CreateBreakCornerFeatureBuilder(self, brcorner: Features.Feature) -> Features.SheetMetal.BreakCornerBuilder:
        ...
    def CreateEdgeRipFeatureBuilder(self, edgeRip: Features.Feature) -> Features.SheetMetal.EdgeRipBuilder:
        ...
    def CreateConvertToSheetmetalFeatureBuilder(self, convertToSheetMetal: Features.Feature) -> Features.SheetMetal.ConvertToSheetmetalBuilder:
        ...
    def CreateNormalCutoutFeatureBuilder(self, ncutout: Features.Feature) -> Features.SheetMetal.NormalCutoutBuilder:
        ...
    def CreateTabFeatureBuilder(self, tab: Features.Feature) -> Features.SheetMetal.TabBuilder:
        ...
    def CreateLoftedFlangeFeatureBuilder(self, lflange: Features.Feature) -> Features.SheetMetal.LoftedFlangeBuilder:
        ...
    def CreateThreeBendCornerFeatureBuilder(self, threeBendCorner: Features.Feature) -> Features.SheetMetal.ThreeBendCornerBuilder:
        ...
    def CreateContourFlangeFeatureBuilder(self, contourFlange: Features.Feature) -> Features.SheetMetal.ContourFlangeBuilder:
        ...
    def CreateFlatSolidFeatureBuilder(self, flatSolid: Features.Feature) -> Features.SheetMetal.FlatSolidBuilder:
        ...
    def CreateFlatPatternBuilder(self, flatPattern: Features.Feature) -> Features.SheetMetal.FlatPatternBuilder:
        ...
    def CreateBendTaperBuilder(self, bendTaper: Features.Feature) -> Features.SheetMetal.BendTaperBuilder:
        ...
    def CreateBendFeatureBuilder(self, bend: Features.Feature) -> Features.SheetMetal.BendBuilder:
        ...
    def CreateClosedCornerFeatureBuilder(self, closedCorner: Features.Feature) -> Features.SheetMetal.ClosedCornerBuilder:
        ...
    def CreateJogFeatureBuilder(self, jog: Features.Feature) -> Features.SheetMetal.JogBuilder:
        ...
    def CreateUnbendFeatureBuilder(self, unbend: Features.Feature) -> Features.SheetMetal.UnbendBuilder:
        ...
    def CreateRebendFeatureBuilder(self, rebend: Features.Feature) -> Features.SheetMetal.RebendBuilder:
        ...
    def CreateMigratedPanelFeatureBuilder(self, migratedPanel: Features.Feature) -> Features.SheetMetal.MigratedPanelBuilder:
        ...
    def CreateResizeBendRadiusFeatureBuilder(self, resizeBendRadius: Features.Feature) -> Features.SheetMetal.ResizeBendRadiusBuilder:
        ...
    def CreateResizeBendAngleBuilder(self, resizeBendAngle: Features.Feature) -> Features.SheetMetal.ResizeBendAngleBuilder:
        ...
    def CreateHemFlangeFeatureBuilder(self, hemFalnge: Features.Feature) -> Features.SheetMetal.HemFlangeBuilder:
        ...
    def CreateResizeNeutralFactorBuilder(self, resizeNeutralFactor: Features.Feature) -> Features.SheetMetal.ResizeNeutralFactorBuilder:
        ...
    def CreateSolidPunchBuilder(self, solidPunch: Features.Feature) -> Features.SheetMetal.SolidPunchBuilder:
        ...
    def CreateBridgeTransitionBuilder(self, transition: Features.Feature) -> Features.SheetMetal.BridgeTransitionBuilder:
        ...
    def IsSheetmetalBody(self, inputBody: Body) -> bool:
        ...
    def GetBodyThickness(self, sheetmetalBody: Body) -> float:
        ...
    def GetInnerBendFaces(self, sheetmetalBody: Body, innerBendFaces: typing.List[Face], bendStates: typing.List[Features.SheetMetal.SheetmetalBendState]) -> None:
        ...
    def GetFaceType(self, inputFace: Face) -> Features.SheetMetal.SheetmetalFaceType:
        ...
    def GetFaceLayer(self, inputFace: Face) -> Features.SheetMetal.SheetmetalFaceLayer:
        ...
    def GetOppositeFace(self, inputFace: Face) -> Face:
        ...
    def GetBendParameters(self, bendFace: Face) -> Features.SheetMetal.SheetmetalBendParameters:
        ...
    def IsThicknessEdge(self, inputEdge: Edge) -> bool:
        ...
    def CreateSheetMetalFromSolidBuilder(self, sheetMetalFromSolid: Features.Feature) -> Features.SheetMetal.SheetMetalFromSolidBuilder:
        ...
    def CreateFlexibleCableBuilder(self, flexibleCable: Features.Feature) -> Features.SheetMetal.FlexibleCableBuilder:
        ...
    def CreateGussetBuilder(self, gusset: Features.Feature) -> Features.SheetMetal.GussetBuilder:
        ...
    def CreateEditBendBuilder(self, editBend: Features.Feature) -> Features.SheetMetal.EditBendBuilder:
        ...
    def CreateCleanUpUtilityBuilder(self) -> Features.SheetMetal.CleanUpUtilityBuilder:
        ...
    def CreateMetaformBuilder(self, metaform: Features.Feature) -> Features.SheetMetal.MetaformBuilder:
        ...
    def CreateEditCornerBuilder(self) -> Features.SheetMetal.EditCornerBuilder:
        ...
    def CreateExportFlatPatternBuilder(self) -> Features.SheetMetal.ExportFlatPatternBuilder:
        ...
    def CreateJoggleBuilder(self, joggle: Features.Feature) -> Features.SheetMetal.JoggleBuilder:
        ...
    def CreateAdvancedFlangeBuilder(self, joggle: Features.Feature) -> Features.SheetMetal.AdvancedFlangeBuilder:
        ...
    def CreateBendListBuilder(self) -> Features.SheetMetal.BendListBuilder:
        ...
    def CreateBendListItemBuilder(self) -> Features.SheetMetal.BendListItemBuilder:
        ...
    def CreateMultiFlangeBuilder(self, multiFlange: Features.SheetMetal.MultiFlange) -> Features.SheetMetal.MultiFlangeBuilder:
        ...
    def Tag(self) -> Tag: ...



class SheetMetalFromSolidBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def GetCandidateBendEdges(self) -> typing.List[Edge]:
        ...
    def GetAutomaticBendEdges(self) -> typing.List[Edge]:
        ...
    BendEdges: ScCollector
    BendOptions: Features.SheetMetal.BendOptions
    ReverseDirection: bool
    Thickness: Expression
    UseGlobalThickness: bool
    WebFaces: ScCollector


class SheetmetalFaceType(enum.Enum):
    Unknown = 0
    Web = 1
    Bend = 2
    Deform = 3
    Thickness = 4


class SheetmetalFaceLayer(enum.Enum):
    Unknown = 0
    Top = 1
    Bottom = 2


class SheetmetalComponentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetApplicationContext(self) -> Features.SheetMetal.ApplicationContext:
        ...
    def SetApplicationContext(self, appContext: Features.SheetMetal.ApplicationContext) -> None:
        ...
    def Validate(self) -> bool:
        ...


class SheetmetalBendState(enum.Enum):
    Unknown = 0
    Bent = 1
    Flat = 2


class SheetmetalBendParameters():
    InnerRadius: float
    NeutralFactor: float
    BendAngle: float
    BendState: Features.SheetMetal.SheetmetalBendState
    def ToString(self) -> str:
        ...


class SheetmetalBaseBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetApplicationContext(self) -> Features.SheetMetal.ApplicationContext:
        ...
    def SetApplicationContext(self, appContext: Features.SheetMetal.ApplicationContext) -> None:
        ...


class ResizeNeutralFactorBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BendFaces: ScCollector
    NeutralFactor: Expression
    UseGlobal: bool


class ResizeBendRadiusBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def SetBendReliefType(self, bendReliefType: Features.SheetMetal.ResizeBendRadiusBuilder.BendReliefTypeOptions) -> None:
        ...
    BendFaces: ScCollector
    BendRadius: Expression
    BendReliefDepth: Expression
    BendReliefType: Features.SheetMetal.ResizeBendRadiusBuilder.BendReliefTypeOptions
    BendReliefWidth: Expression
    ReferenceEntity: SelectDisplayableObject
    Type: Features.SheetMetal.ResizeBendRadiusBuilder.Types


    class Types(enum.Enum):
        FixedFoldedLength = 0
        FixedUnfoldedLength = 1
    

    class BendReliefTypeOptions(enum.Enum):
        Square = 0
        Round = 1
        None = 2
    

class ResizeBendAngleBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    BendFace: SelectFace
    KeepRadiusFixed: bool
    ReferenceEdge: SelectEdge
    ReferenceFace: SelectFace


class RebendBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def ValidateBuilderData(self) -> int:
        ...
    FaceCollector: ScCollector
    ReferenceEntity: NXObject


class NormalCutoutBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def SetDepth(self, depth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.NormalCutoutBuilder.Depth instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    CutType: Features.SheetMetal.NormalCutoutBuilder.CutTypeOptions
    Depth: Expression
    DepthSide: Features.SheetMetal.NormalCutoutBuilder.DepthSideOptions
    DepthType: Features.SheetMetal.NormalCutoutBuilder.DepthTypeOptions
    From: ISurface
    Section: Section
    SectionSide: Features.SheetMetal.NormalCutoutBuilder.SectionSideOptions
    Sketch: Features.SketchFeature
    TargetBody: Body
    To: ISurface
    Type: Features.SheetMetal.NormalCutoutBuilder.TypeOptions


    class TypeOptions(enum.Enum):
        SketchType = 0
        NonPlanarCurveType = 1
    

    class SectionSideOptions(enum.Enum):
        Left = 0
        Right = 1
    

    class DepthTypeOptions(enum.Enum):
        Finite = 0
        FromTo = 1
        ThroughNext = 2
        ThroughAll = 3
    

    class DepthSideOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
        Symmetric = 2
    

    class CutTypeOptions(enum.Enum):
        ThicknessCut = 0
        MidPlaneCut = 1
        NearestFaceCut = 2
    

class MultiFlangeBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    FlangePropertiesList: Features.SheetMetal.FeatureBendPropertiesListBuilder
    MatchFace: Features.SheetMetal.MultiFlangeBuilder.MatchFaceOptions
    Plane: Plane


    class MatchFaceOptions(enum.Enum):
        None = 0
        UntilSelected = 1
    

class MultiFlange(Features.Feature):
    def __init__(self) -> None: ...


class MultiBendBendPropertiesListBuilder(Features.SheetMetal.FeatureBendPropertiesListBuilder):
    def __init__(self) -> None: ...
    def CreateMultiBendBendProperties(self) -> Features.SheetMetal.MultiBendBendPropertiesBuilder:
        ...


class MultiBendBendPropertiesBuilder(Features.SheetMetal.FeatureBendPropertiesBuilder):
    def __init__(self) -> None: ...
    def DeleteMultiBendBendProperties(self) -> None:
        ...
    Inset: Features.SheetMetal.MultiBendBendPropertiesBuilder.Insets
    ParentPlane: Plane
    Plane: Plane
    SketchParentPlane: bool


    class Insets(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
    

class MiterOptions(TaggedObject):
    def __init__(self) -> None: ...
    def GetStartValue(self) -> Expression:
        ...
    def SetStartValue(self, startValue: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from Features.SheetMetal.MiterOptions.GetStartValue instead.")"""
        ...
    def GetEndValue(self) -> Expression:
        ...
    def SetEndValue(self, endValue: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from Features.SheetMetal.MiterOptions.GetEndValue instead.")"""
        ...
    def GetClosedCornerDiameter(self) -> Expression:
        ...
    def SetClosedCornerDiameter(self, endValue: str) -> None:
        ...
    BlendMiter: bool
    ClosedCornerGap: Expression
    ClosedCornerType: Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions
    ClosedCornerVAngle1: Expression
    ClosedCornerVAngle2: Expression
    CornerTreatmentOffset: Expression
    CornerTreatmentOriginType: Features.SheetMetal.MiterOptions.CornerTreatmentOriginTypeOptions
    EndType: Features.SheetMetal.MiterOptions.TypeOptions
    MiterCorner: bool
    MiterInteriorCornersIfNecessary: bool
    MiterRootRadius: Expression
    Position: Features.SheetMetal.MiterOptions.PositionOptions
    StartType: Features.SheetMetal.MiterOptions.TypeOptions
    ThreeBendCornerFlangeClearance: Expression
    UseNormalCutoutMethod: bool


    class TypeOptions(enum.Enum):
        NormalToSourceFace = 0
        NormalToThicknessFace = 1
    

    class PositionOptions(enum.Enum):
        None = 0
        Start = 1
        End = 2
        Both = 3
    

    class CornerTreatmentOriginTypeOptions(enum.Enum):
        BendCenter = 0
        CornerPoint = 1
    

    class ClosedCornerTypeOptions(enum.Enum):
        None = 0
        Open = 1
        Closed = 2
        CircularCutout = 3
        UCutout = 4
        VCutout = 5
    

class MigratedPanelBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlongFaceNormal: bool
    BendFace: Face
    BendOptions: Features.SheetMetal.BendOptions
    BendRadius: str
    CutoffAngle: str
    EndConditions: ExpressionCollectorSet
    GapTolerance: str
    MovingFace: Face
    NeutralOffset: str
    ParentSmBody: Body
    StationaryFace: Face


class MetaformBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateSMBoundaryCondition(self) -> Features.SheetMetal.SMBoundaryConditionBuilder:
        ...
    AngularTolerance: Expression
    ChordalTolerance: Expression
    ElasticModulus: Expression
    EndRegion: ScCollector
    HoleRemovalMinModulus: Expression
    InferThickness: bool
    LinearTolerance: Expression
    NeutralFactor: Expression
    OutputLayer: int
    PoissonsRatio: Expression
    RValue: Expression
    RemoveHoles: bool
    ReverseThicknessDirection: bool
    SMBoundaryConditions: Features.SheetMetal.SMBoundaryConditionBuilderList
    StartRegion: ScCollector
    TangentModulus: Expression
    Thickness: Expression
    TransformGeometry: SelectNXObjectList
    YieldStress: Expression


class LouverBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetDepth(self, depth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.LouverBuilder.Depth instead.")"""
        ...
    def SetWidth(self, width: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.LouverBuilder.Width instead.")"""
        ...
    def SetDieRadius(self, dieRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.LouverBuilder.DieRadius instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    Depth: Expression
    DepthSide: Features.SheetMetal.LouverBuilder.DepthSideOptions
    DieRadius: Expression
    EndType: Features.SheetMetal.LouverBuilder.EndTypeOptions
    IncludeRounding: bool
    MinimumToolClearance: Expression
    Section: Section
    SectionSide: Features.SheetMetal.LouverBuilder.SectionSideOptions
    Sketch: Features.SketchFeature
    Width: Expression


    class SectionSideOptions(enum.Enum):
        Left = 0
        Right = 1
    

    class EndTypeOptions(enum.Enum):
        Formed = 0
        Lanced = 1
    

    class DepthSideOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

class LoftedFlangeBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def GetThickness(self) -> Expression:
        ...
    def SetThickness(self, thickness: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Expression.RightHandSide on the Expression object returned from Features.SheetMetal.LoftedFlangeBuilder.GetThickness instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    BendOptions: Features.SheetMetal.BendOptions
    EndSection: Section
    EndSectionPoint: Point3d
    EndSketch: Features.SketchFeature
    IndexMarkLength: Expression
    IsSecondary: bool
    NumberOfBendSegments: int
    StartSection: Section
    StartSectionPoint: Point3d
    StartSketch: Features.SketchFeature
    ThicknessSide: Features.SheetMetal.LoftedFlangeBuilder.SectionSideOptions
    UseSegmentedBends: bool


    class SectionSideOptions(enum.Enum):
        Left = 0
        Right = 1
    

class LighteningCutoutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetStandards(self) -> str:
        ...
    Angle: Expression
    BendOptions: Features.SheetMetal.BendOptions
    CheckClearance: bool
    Clearance: Expression
    Diameter: Expression
    DieRadius: Expression
    HoleCenter: Section
    Length: Expression
    NeutralFactor: Expression
    ReverseBendDirection: bool
    SectionCornerRadius: Expression
    Sketch: Features.SketchFeature
    StandardName: str
    Type: Features.SheetMetal.LighteningCutoutBuilder.CutoutType
    UserDefinedSection: Section


    class CutoutType(enum.Enum):
        Hole = 0
        UserDefined = 1
    

class LighteningCutout(Features.BodyFeature):
    def __init__(self) -> None: ...


class JoggleSideOptionsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Clearance: Expression
    OffsetRadius: Expression
    Runout: Expression
    StationaryRadius: Expression


class JoggleInputListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.SheetMetal.JoggleInputListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.SheetMetal.JoggleInputListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.SheetMetal.JoggleInputListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.SheetMetal.JoggleInputListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.JoggleInputListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.JoggleInputListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.SheetMetal.JoggleInputListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.SheetMetal.JoggleInputListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.SheetMetal.JoggleInputListItemBuilder, object2: Features.SheetMetal.JoggleInputListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.SheetMetal.JoggleInputListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class JoggleInputListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Depth: Expression
    Faces: ScCollector
    ReverseDirection: bool


class JoggleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateJoggleInputListItem(self) -> Features.SheetMetal.JoggleInputListItemBuilder:
        ...
    Adjustment: Expression
    EndPlane: Plane
    FlatPatternCompensation: bool
    InputList: Features.SheetMetal.JoggleInputListItemBuilderList
    LimitType: Features.SheetMetal.JoggleBuilder.LimitTypes
    Side1Options: Features.SheetMetal.JoggleSideOptionsBuilder
    Side2Options: Features.SheetMetal.JoggleSideOptionsBuilder
    StartPlane: Plane
    SymmetricSides: bool
    UseMaterialTable: bool


    class LimitTypes(enum.Enum):
        Single = 0
        Twin = 1
    

class Joggle(Features.Feature):
    def __init__(self) -> None: ...


class JogBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def GetHeight(self) -> Expression:
        ...
    def SetHeight(self, height: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Expression.RightHandSide on the Expression object returned from Features.SheetMetal.JogBuilder.GetHeight instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    BendLocation: Features.SheetMetal.JogBuilder.BendLocationOptions
    BendOptions: Features.SheetMetal.BendOptions
    DimensionType: Features.SheetMetal.JogBuilder.DimensionTypeOptions
    DirectionType: Features.SheetMetal.JogBuilder.DirectionTypeOptions
    ExtendProfile: bool
    FixedSide: Features.SheetMetal.JogBuilder.FixedSideOptions
    Section: Section
    Sketch: Features.SketchFeature
    TargetFace: Face


    class FixedSideOptions(enum.Enum):
        SectionSideLeft = 0
        SectionSideRight = 1
    

    class DirectionTypeOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

    class DimensionTypeOptions(enum.Enum):
        Offset = 0
        Full = 1
    

    class BendLocationOptions(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
        BendOutside = 2
    

class HoleTreatmentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Diameter: Expression
    Treatment: Features.SheetMetal.HoleTreatmentBuilder.TreatmentType
    UseGlobal: bool


    class TreatmentType(enum.Enum):
        None = 0
        Centermark = 1
    

class HemFlangeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BendReliefDepth: Expression
    BendReliefType: Features.SheetMetal.HemFlangeBuilder.BendReliefOptions
    BendReliefWidth: Expression
    EdgeChain: ScCollector
    FirstBendRadius: Expression
    FirstFlangeLength: Expression
    InsetType: Features.SheetMetal.HemFlangeBuilder.InsetTypeOptions
    MiterAngle: Expression
    NeutralFactor: Expression
    SecondBendRadius: Expression
    SecondFlangeLength: Expression
    SweepAngle: Expression
    Type: Features.SheetMetal.HemFlangeBuilder.TypeOptions
    UseMiter: bool


    class TypeOptions(enum.Enum):
        ClosedHemType = 0
        OpenHemType = 1
        SFlangeHemType = 2
        CurlHemType = 3
        OpenLoopHemType = 4
        ClosedLoopHemType = 5
        CenteredLoopHemType = 6
    

    class InsetTypeOptions(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
        BendOutside = 2
    

    class BendReliefOptions(enum.Enum):
        Square = 0
        Round = 1
        None = 2
    

class GussetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetStartEdgeCandidates(self, candidateEdges: typing.List[Edge]) -> None:
        ...
    def GetPlacementOriginAndDirection(self, origin: Point3d) -> Vector3d:
        ...
    def AlternateSolution(self) -> None:
        ...
    def GetIsPreNx10(self) -> bool:
        ...
    BendFace: SelectFace
    CornerRadius: Expression
    DatumPlane: Plane
    Depth: Expression
    DieRadius: Expression
    PlacementCount: int
    PlacementDistance: Expression
    PlacementSpacing: Expression
    PlacementType: Features.SheetMetal.GussetBuilder.PlacementTypes
    PunchRadius: Expression
    Section: Section
    Shape: Features.SheetMetal.GussetBuilder.Shapes
    SideAngle: Expression
    StartEdge: SelectEdge
    Type: Features.SheetMetal.GussetBuilder.Types
    Width: Expression
    WidthSide: Features.SheetMetal.GussetBuilder.WidthSides


    class WidthSides(enum.Enum):
        Side1 = 0
        Side2 = 1
        Symmetric = 2
    

    class Types(enum.Enum):
        AutomaticProfile = 0
        UserDefinedProfile = 1
    

    class Shapes(enum.Enum):
        Square = 0
        Round = 1
    

    class PlacementTypes(enum.Enum):
        Single = 0
        Fit = 1
        Fill = 2
        Fixed = 3
    

class FlexibleCableSegment(NXObject):
    def __init__(self) -> None: ...
    def GetSegmentType(self) -> Features.SheetMetal.FlexibleCableBuilder.SegmentTypeOptions:
        ...
    BendAngle: Expression
    BendAngleDirection: Features.SheetMetal.FlexibleCableBuilder.BendAngleDirectionOptions
    BendRadius: Expression
    Length: Expression
    PathAdjustmentAngle: Expression
    PathAdjustmentAngleDirection: Features.SheetMetal.FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions


class FlexibleCableBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetIndexOfSegment(self, flexibleCableSegment: Features.SheetMetal.FlexibleCableSegment) -> int:
        ...
    def GetSegment(self, index: int) -> Features.SheetMetal.FlexibleCableSegment:
        ...
    def DeleteSegment(self, index: int) -> None:
        ...
    def DeleteAllSegments(self) -> None:
        ...
    def CreatePlanarSegment(self, length: str, segmentIndex: int) -> Features.SheetMetal.FlexibleCableSegment:
        ...
    def CreateBendSegment(self, bendAngle: str, bendRadius: str, pathAdjustmentAngle: str, bendAngleDirection: Features.SheetMetal.FlexibleCableBuilder.BendAngleDirectionOptions, pathAdjustmentAngleDirection: Features.SheetMetal.FlexibleCableBuilder.PathAdjustmentAngleDirectionOptions, segmentIndex: int) -> Features.SheetMetal.FlexibleCableSegment:
        ...
    def GetSegmentCount(self) -> int:
        ...
    CableDirection: Direction
    ConductorCount: int
    ConductorSpacing: Expression
    ConductorWidth: Expression
    CrossSectionWidth: Expression
    SegmentList: TaggedObjectList
    StartPoint: Point
    StrippingLength: Expression
    Thickness: Expression
    ThicknessDirection: Direction


    class SegmentTypeOptions(enum.Enum):
        Planar = 0
        Bend = 1
    

    class PathAdjustmentAngleDirectionOptions(enum.Enum):
        LeftDirection = 0
        RightDirection = 1
    

    class BendAngleDirectionOptions(enum.Enum):
        ReverseNormalDirection = 0
        NormalDirection = 1
    

class FlatSolidBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def ValidateBuilderData(self) -> int:
        ...
    AddedGeometry: Section
    Associative: bool
    FixAtTimestamp: bool
    InnerCornerTreatment: Features.SheetMetal.CornerTreatmentBuilder
    Orientation: Features.SheetMetal.FlatSolidBuilder.OrientationType
    OrientationCsys: CoordinateSystem
    OuterCornerTreatment: Features.SheetMetal.CornerTreatmentBuilder
    ReferenceVertex: Point3d
    StationaryFace: SelectFace
    TransformComponents: Features.SheetMetal.FlatSolidBuilder.TransformComponentsOption
    TransformRestrictionAreas: bool
    TransformToAbsoluteCsys: bool
    XAxisEdge: SelectEdge


    class TransformComponentsOption(enum.Enum):
        None = 0
        Body = 1
        Csys = 2
    

    class OrientationType(enum.Enum):
        Default = 0
        Edge = 1
        Csys = 2
    

class FlatPatternBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def GenerateMoldLines(self) -> None:
        ...
    AddedGeometry: Section
    Associative: bool
    FixAtTimestamp: bool
    FlatPatternViewName: str
    HoleTreatment: Features.SheetMetal.HoleTreatmentBuilder
    InnerCornerTreatment: Features.SheetMetal.CornerTreatmentBuilder
    Orientation: Features.SheetMetal.FlatSolidBuilder.OrientationType
    OrientationCsys: CoordinateSystem
    OuterCornerTreatment: Features.SheetMetal.CornerTreatmentBuilder
    ReferenceVertex: Point3d
    ShowInteriorFeatureCurves: bool
    TransformToAbsoluteCsys: bool
    UpwardFace: SelectFace
    XAxisEdge: SelectEdge


class FlangeBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def SetOffset(self, offset: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.FlangeBuilder.Offset instead.")"""
        ...
    def SetLength(self, length: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.FlangeBuilder.Length instead.")"""
        ...
    def SetFirstDistance(self, firstDistance: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance instead.")"""
        ...
    def SetSecondDistance(self, secondDistance: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance instead.")"""
        ...
    def SetBendAngle(self, bendAngle: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.FlangeBuilder.BendAngle instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    def GetSketch(self) -> Sketch:
        ...
    def EditSketch(self) -> None:
        ...
    def DeleteSketch(self) -> None:
        ...
    BendAngle: Expression
    BendOptions: Features.SheetMetal.BendOptions
    Edge: Edge
    FirstDistance: Expression
    InsetType: Features.SheetMetal.FlangeBuilder.InsetTypeOptions
    Length: Expression
    LengthType: Features.SheetMetal.FlangeBuilder.LengthTypeOptions
    MatchFaceOption: Features.SheetMetal.FlangeBuilder.MatchFaceOptions
    MatchPlane: Plane
    Offset: Expression
    OffsetType: Features.SheetMetal.FlangeBuilder.OffsetTypeOptions
    SecondDistance: Expression
    Vertex: Point3d
    WidthType: Features.SheetMetal.FlangeBuilder.WidthTypeOptions


    class WidthTypeOptions(enum.Enum):
        FullEdge = 0
        CenterOfEdge = 1
        AtEdgeEnd = 2
        FromEdgeEnd = 3
        FromBothEnds = 4
        Custom = 5
    

    class OffsetTypeOptions(enum.Enum):
        Inside = 0
        Outside = 1
    

    class MatchFaceOptions(enum.Enum):
        None = 0
        UntilSelected = 1
    

    class LengthTypeOptions(enum.Enum):
        InsideDimension = 0
        OutsideDimension = 1
        WebDimension = 2
    

    class InsetTypeOptions(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
        BendOutside = 2
    

class FlangeBendPropertiesListBuilder(Features.SheetMetal.FeatureBendPropertiesListBuilder):
    def __init__(self) -> None: ...
    def CreateFlangeBendProperties(self) -> Features.SheetMetal.FlangeBendPropertiesBuilder:
        ...


class FlangeBendPropertiesBuilder(Features.SheetMetal.FeatureBendPropertiesBuilder):
    def __init__(self) -> None: ...
    def DeleteFlangeBendProperties(self) -> None:
        ...
    Angle: Expression
    Distance1: Expression
    Distance2: Expression
    Edges: ScCollector
    Inset: Features.SheetMetal.FlangeBendPropertiesBuilder.Insets
    Length: Expression
    LengthReference: Features.SheetMetal.FlangeBendPropertiesBuilder.LengthReferences
    Miter: bool
    Offset: Expression
    Point: Point
    ReverseDirectionLength: bool
    ReverseDirectionOffset: bool
    UseRecipe: bool
    Width: Expression
    WidthOption: Features.SheetMetal.FlangeBendPropertiesBuilder.WidthOptions


    class WidthOptions(enum.Enum):
        Full = 0
        AtCenter = 1
        AtEnd = 2
        FromEnd = 3
        FromBothEnds = 4
    

    class LengthReferences(enum.Enum):
        Inside = 0
        Outside = 1
        Web = 2
    

    class Insets(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
        BendOutside = 2
    

class FeatureProperty(enum.Enum):
    IgNullConstant = 0
    IgLeft = 1
    IgRight = 2
    IgSymmetric = 3
    IgInside = 4
    IgOutside = 5
    IgBoth = 6
    IgNormalSidedummy = 7
    IgReverseNormalSidedummy = 8
    IgExtend = 9
    IgNoextend = 10
    IgThkinprofileplane = 11
    IgThkNormalToProfilePlane = 12
    IgFinite = 13
    IgTonext = 14
    IgFromTo = 15
    IgThroughAll = 16
    IgThreeHundredAndSixty = 17
    IgParallelDummy = 18
    IgAngularDummy = 19
    IgNormal = 20
    IgThroughAxis = 21
    IgSingleEdge = 22
    IgMultipleEdges = 23
    IgEdgesByLoop = 24
    IgEdgesByVertex = 25
    IgAll = 26
    IgConcave = 27
    IgConvex = 28
    IgStart = 29
    IgEnd = 30
    IgLinear = 31
    IgRadial = 32
    IgRegularHole = 33
    IgCounterBoreHole = 34
    IgCounterSinkHole = 35
    IgCounterDrillHole = 36
    IgTappedHole = 37
    IgTaperedHole = 38
    IgConstRadiusRound = 39
    IgVarRadiusRound = 40
    IgChamfer45degSetback = 41
    IgChamferAngleSetback = 42
    IgChamfer2Serbacks = 43
    IgNone = 44
    IgTaperByAngle = 45
    IgTaperByRatio = 46
    IgClosed = 47
    IgProfileBasedCrosssection = 48
    IgEdgeBasedCrosssection = 49
    IgTangent = 50
    IgRectangularBendRelief = 51
    IgFilletBendRelief = 52
    IgRipBendRelief = 53
    IgBendOnlyCornerRelief = 54
    IgBendAndFaceCornerRelief = 55
    IgRipCornerRelief = 56
    IgNftype = 57
    IgEquationType = 58
    IgPatternMirror = 59
    IgPatternRectangular = 60
    IgPatternCircular = 61
    IgPatternUserDefined = 62
    IgFromReferenceEnd = 64
    IgFromNonreferenceEnd = 65
    IgRndRollAcrossTnagentEdgesOn = 66
    IgRndRollAcrossTangentEdgesOff = 67
    IgRndCapAcrossSharpEdges = 68
    IgRndRollAcrossSharpEdges = 69
    IgRndRollAlongBlendEdgesOn = 70
    IgRndRollAlongBlendEdgesOff = 71
    IgToKepPoint = 72
    IgFlatten = 73
    IgAsConstruction = 74
    IgOffset = 75
    IgMitreParalletToThickness = 76
    IgMitreNormalToThickness = 77
    IgMitreByDist = 78
    IgMitreByAngle = 79
    IgMiterRegularCut = 80
    IgMitreManufacturingCut = 81
    IgProjectOptionProject = 82
    IgProjectOptionWrap = 83
    IgLip = 84
    IgGroove = 85
    IgPartingFromPlane = 86
    IgPartingFromSurface = 87
    IgPartingFromEdge = 88
    IgPartingFromCurve = 89
    IgSplitDraft = 90
    IgSplitAngle1Right = 91
    IgSplitAngle1Left = 92
    IgLouverformedendtype = 93
    IgLouverlancedendtype = 94
    IgLouverround = 95
    IgLouverroundnone = 96
    IgInsideDimension = 97
    IgOutsideDimension = 98
    IgFull = 99
    IgBend = 100
    IgAddRound = 101
    IgNoRound = 102
    IgCloseFaces = 103
    IgOverlapFaces = 104
    IgTreatmentOff = 105
    IgTreatmentIntersect = 106
    IgTreatmentCircleCutout = 107
    IgStepDreat = 108
    IgShowBoundaries = 109
    IgRemoveBoundaries = 110
    IgCornerRound = 111
    IgNoCornerRound = 112
    IgNatural = 113
    IgPeriodic = 114
    IgRoundAllVertexSetback = 115
    IgRoundSingleVertexSetback = 116
    IgRoundVertexEdgeSetback = 117
    IgRoundSetbackIsAbsolute = 118
    IgRoundSetbackIsRelative = 119
    IgCircular = 120
    IgUshaped = 121
    IgVshaped = 122
    IgPunchedEnd = 123
    IgLancedEnd = 124
    IgFormedEnd = 125
    IgSweepAlignParallel = 126
    IgSweepAlignNormal = 127
    IgRoundStartVertexEdgeSetback = 128
    IgRoundEndVertexEdgeSetback = 129
    IgSubtract = 130
    IgUnite = 131
    IgIntersect = 132
    IgContinuous = 133
    IgFlangeFulledge = 134
    IgFlangeCenterOfEdge = 135
    IgFlangeStartOnEndEdge = 136
    IgFlangeEndOnEndEdge = 137
    IgFlangeStartFromEndEdge = 138
    IgFlangeEndFromEndEdge = 139
    IgFlangeFromBothEndsOfEdge = 140
    IgFlangeOffset = 141
    IgChainedCornerRelief = 142
    IgTangentInterior = 143
    IgParallelToPlane = 144
    IgVbottomDimToFlat = 145
    IgVbottomDimToV = 146
    IgTaperDimAtTop = 147
    IgTaperDimAtBottom = 148
    IgCounterBoreProfileIsAtTop = 149
    IgCounterBoreProfileIsAtBottom = 150
    IgTaperByRlRatio = 151
    IgRndmiteratCorner = 152
    IgRndRollAroundCorner = 153
    IgRndPreserveTopologyon = 154
    IgRndPreserveTopologyOff = 155
    IgStepDraftPerpendicular = 156
    IgExtendBendRelief = 157
    IgEqualOffset = 158
    IgUnequalOffset = 159
    IgThickness = 160
    IgFacesTouchingCurvesOnly = 161
    IgCurvesetSeperator = 162
    IgSideInfosetSeperator = 163
    IgRegularThread = 164
    IgStraightPipethread = 165
    IgTaperedPipethread = 166
    IgRemoveInternalBoundaries = 167
    IgRemoveExternalBoundaries = 168
    IgDeleteFaceheal = 169
    IgEndcaps = 170
    IgCurvatureContinuous = 171
    IgNonsymmetric = 172
    IgTreatmentDraft = 173
    IgTreatmentCrown = 174
    IgCloseCornerNone = 175
    IgCloseCornerOpen = 176
    IgCloseCornerClosed = 177
    IgCloseCornerCircleCutout = 178
    IgPatternAlongCurve = 179
    IgPatternMountingBoss = 180
    IgSmClearanceCutout = 181
    IgSmMidplaceCutout = 182
    IgCentermark = 183


class FeatureBendPropertiesListBuilder(Features.SheetMetal.SheetmetalComponentBuilder):
    def __init__(self) -> None: ...
    def CreateFeatureProperties(self) -> Features.SheetMetal.FeatureBendPropertiesBuilder:
        ...
    FeatureBendPropertiesList: Features.SheetMetal.FeatureBendPropertiesBuilderList


class FeatureBendPropertiesBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.SheetMetal.FeatureBendPropertiesBuilder]) -> None:
        ...
    def Append(self, object: Features.SheetMetal.FeatureBendPropertiesBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.SheetMetal.FeatureBendPropertiesBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.SheetMetal.FeatureBendPropertiesBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.FeatureBendPropertiesBuilder) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.FeatureBendPropertiesBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.SheetMetal.FeatureBendPropertiesBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.SheetMetal.FeatureBendPropertiesBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.SheetMetal.FeatureBendPropertiesBuilder, object2: Features.SheetMetal.FeatureBendPropertiesBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.SheetMetal.FeatureBendPropertiesBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FeatureBendPropertiesBuilder(Features.SheetMetal.SheetmetalComponentBuilder):
    def __init__(self) -> None: ...
    BendOptions: Features.SheetMetal.BendOptions
    Value: Expression


class ExportFlatPatternBuilder(Builder):
    def __init__(self) -> None: ...
    AddedBottom: bool
    AddedTop: bool
    BendDown: bool
    BendTangent: bool
    BendUp: bool
    DeviationalTolerance: float
    DxfRevision: Features.SheetMetal.ExportFlatPatternBuilder.DxfRevisionType
    FlatPattern: Features.SelectFlatPattern
    InnerMold: bool
    InteriorCutout: bool
    InteriorFeature: bool
    OuterMold: bool
    OutputFile: str
    Type: Features.SheetMetal.ExportFlatPatternBuilder.FileType


    class FileType(enum.Enum):
        Dxf = 0
        TrumpfGeo = 1
    

    class DxfRevisionType(enum.Enum):
        R2005 = 0
        R2004 = 1
        R2000 = 2
        R14 = 3
        R2007 = 4
        R20102012 = 5
        R20132016 = 6
        R12 = 7
        R13 = 8
    

class EditCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AddFacePair(self, firstFace: Face, secondFace: Face) -> None:
        ...
    def GetFacePair(self, index: int, firstFace: Face, secondFace: Face) -> None:
        ...
    def GetNumberOfFacePairs(self) -> int:
        ...
    def RemoveFacePair(self, firstFace: Face, secondFace: Face) -> None:
        ...
    BendClosureType: Features.SheetMetal.EditCornerBuilder.BendClosureTypeOptions
    CornerReliefType: Features.SheetMetal.EditCornerBuilder.CornerReliefTypeOptions
    Diameter: Expression
    OverlapRatio: Expression
    PlateClosureType: Features.SheetMetal.EditCornerBuilder.PlateClosureTypeOptions
    PlateGap: Expression
    ReverseOverlap: bool


    class PlateClosureTypeOptions(enum.Enum):
        Closed = 0
        Overlapped = 1
    

    class CornerReliefTypeOptions(enum.Enum):
        None = 0
        CircularCutout = 1
    

    class BendClosureTypeOptions(enum.Enum):
        Open = 0
        Closed = 1
    

class EditBendBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    BendOptions: Features.SheetMetal.BendOptions
    SelectBend: ScCollector


class EdgeRipBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetRipEdges(self, ripEdges: typing.List[Edge]) -> None:
        ...
    def GetRipEdges(self) -> typing.List[Edge]:
        ...
    def ValidateBuilderData(self) -> int:
        ...
    Section: Section
    Sketch: Features.SketchFeature


class DrawnCutoutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetCutoutDepth(self, depth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DrawnCutoutBuilder.CutoutDepth instead.")"""
        ...
    def SetSideAngle(self, sideAngle: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DrawnCutoutBuilder.SideAngle instead.")"""
        ...
    def SetRadiusOfDie(self, dieRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DrawnCutoutBuilder.RadiusOfDie instead.")"""
        ...
    def SetCornerRadius(self, cornerRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DrawnCutoutBuilder.CornerRadius instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    CornerRadius: Expression
    CutoutDepth: Expression
    DepthType: Features.SheetMetal.DrawnCutoutBuilder.DepthTypeOptions
    FilletSectionCorners: bool
    IncludeRounding: bool
    MinimumToolClearance: Expression
    RadiusOfDie: Expression
    Section: Section
    SectionSide: Features.SheetMetal.DrawnCutoutBuilder.SectionSideOptions
    SideAngle: Expression
    SidewallType: Features.SheetMetal.DrawnCutoutBuilder.SidewallTypeOptions
    Sketch: Features.SketchFeature


    class SidewallTypeOptions(enum.Enum):
        Outside = 0
        Inside = 1
    

    class SectionSideOptions(enum.Enum):
        Left = 0
        Right = 1
    

    class DepthTypeOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

class DimpleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetDepth(self) -> Expression:
        ...
    def SetDepth(self, extent: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DimpleBuilder.GetDepth instead.")"""
        ...
    def GetTaperAngle(self) -> Expression:
        ...
    def SetTaperAngle(self, taperAngle: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DimpleBuilder.GetTaperAngle instead.")"""
        ...
    def GetPunchRadius(self) -> Expression:
        ...
    def SetPunchRadius(self, punchRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DimpleBuilder.GetPunchRadius instead.")"""
        ...
    def GetDieRadius(self) -> Expression:
        ...
    def SetDieRadius(self, dieRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DimpleBuilder.GetDieRadius instead.")"""
        ...
    def GetFilletRadius(self) -> Expression:
        ...
    def SetFilletRadius(self, filletRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.DimpleBuilder.GetFilletRadius instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    DepthType: Features.SheetMetal.DimpleBuilder.DepthTypeOptions
    DimensionType: Features.SheetMetal.DimpleBuilder.DimensionTypeOptions
    FilletSectionCorners: bool
    IncludeRounding: bool
    MinimumToolClearance: Expression
    Section: Section
    SectionSide: Features.SheetMetal.DimpleBuilder.SectionSideOptions
    SidewallType: Features.SheetMetal.DimpleBuilder.SidewallTypeOptions
    Sketch: Features.SketchFeature


    class SidewallTypeOptions(enum.Enum):
        Outside = 0
        Inside = 1
    

    class SectionSideOptions(enum.Enum):
        Left = 0
        Right = 1
    

    class DimensionTypeOptions(enum.Enum):
        Offset = 0
        Full = 1
    

    class DepthTypeOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

class CornerTreatmentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    TreatmentType: Features.SheetMetal.CornerTreatmentBuilder.CornerTreatmentType
    UseGlobal: bool
    Value: Expression


    class CornerTreatmentType(enum.Enum):
        None = 0
        Chamfer = 1
        Radius = 2
    

class ConvertToSheetmetalBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def GetRipEdges(self) -> typing.List[Edge]:
        ...
    def SetRipEdges(self, ripEdges: typing.List[Edge]) -> None:
        ...
    def SetBendReliefWidth(self, bendReliefWidth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Expression.RightHandSide on the Expression object returned from Features.SheetMetal.ConvertToSheetmetalBuilder.BendReliefWidth instead.")"""
        ...
    def SetBendReliefDepth(self, bendReliefDepth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Expression.RightHandSide on the Expression object returned from Features.SheetMetal.ConvertToSheetmetalBuilder.BendReliefDepth instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    def CreateConvertInputListItem(self) -> Features.SheetMetal.ConvertInputListItemBuilder:
        ...
    AdditionalFacesToConvert: ScCollector
    BaseFace: Face
    BendReliefDepth: Expression
    BendReliefType: Features.SheetMetal.ConvertToSheetmetalBuilder.BendReliefTypeOptions
    BendReliefWidth: Expression
    CornerList: Features.SheetMetal.ConvertInputListItemBuilderList
    LocalBaseFace: Face
    LocalRegionFaces: ScCollector
    MaintainZeroBendRadius: bool
    RipSection: Section
    Sketch: Features.SketchFeature


    class BendReliefTypeOptions(enum.Enum):
        None = 0
        Square = 1
        Round = 2
    

class ConvertInputListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.SheetMetal.ConvertInputListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.SheetMetal.ConvertInputListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.SheetMetal.ConvertInputListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.SheetMetal.ConvertInputListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.ConvertInputListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.ConvertInputListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.SheetMetal.ConvertInputListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.SheetMetal.ConvertInputListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.SheetMetal.ConvertInputListItemBuilder, object2: Features.SheetMetal.ConvertInputListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.SheetMetal.ConvertInputListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ConvertInputListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CornerFaces: ScCollector


class ContourFlangeBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def GetThickness(self) -> Expression:
        ...
    def SetThickness(self, thickness: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Expression.RightHandSide on the Expression object returned from Features.SheetMetal.ContourFlangeBuilder.GetThickness instead.")"""
        ...
    def GetSweepDistance(self) -> Expression:
        ...
    def SetSweepDistance(self, sweepDistance: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Expression.RightHandSide on the Expression object returned from Features.SheetMetal.ContourFlangeBuilder.GetSweepDistance instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    BendOptions: Features.SheetMetal.BendOptions
    EdgeChain: Section
    IsSecondary: bool
    MiterOptions: Features.SheetMetal.MiterOptions
    Section: Section
    Sketch: Features.SketchFeature
    SweepSide: Features.SheetMetal.ContourFlangeBuilder.SweepSideOptions
    SweepType: Features.SheetMetal.ContourFlangeBuilder.SweepTypeOptions
    ThicknessSide: Features.SheetMetal.ContourFlangeBuilder.SectionSideOptions


    class SweepTypeOptions(enum.Enum):
        Finite = 0
        Symmetric = 1
        ToEnd = 2
        Chain = 3
    

    class SweepSideOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

    class SectionSideOptions(enum.Enum):
        Left = 0
        Right = 1
    

class ClosedCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def AddFacePair(self, firstFace: Face, secondFace: Face) -> None:
        ...
    def GetFacePair(self, index: int, firstFace: Face, secondFace: Face) -> None:
        ...
    def GetNumberOfFacePairs(self) -> int:
        ...
    def ValidateBuilderData(self) -> int:
        ...
    def RemoveFacePair(self, firstFace: Face, secondFace: Face) -> None:
        ...
    BlendMiter: bool
    ClosureType: Features.SheetMetal.ClosedCornerBuilder.ClosureTypeOptions
    Diameter: Expression
    Gap: Expression
    MiterCorner: bool
    Offset: Expression
    Origin: Features.SheetMetal.ClosedCornerBuilder.OriginTypes
    Overlap: Expression
    RectangularLength: Expression
    RectangularWidth: Expression
    TreatmentType: Features.SheetMetal.ClosedCornerBuilder.TreatmentTypeOptions
    Type: Features.SheetMetal.ClosedCornerBuilder.Types
    VAngle1: Expression
    VAngle2: Expression


    class Types(enum.Enum):
        CloseAndRelief = 0
        Relief = 1
    

    class TreatmentTypeOptions(enum.Enum):
        Open = 0
        Closed = 1
        CircularCutout = 2
        UCutout = 3
        VCutout = 4
        RectangularCutout = 5
    

    class OriginTypes(enum.Enum):
        BendCenter = 0
        CornerPoint = 1
    

    class ClosureTypeOptions(enum.Enum):
        Close = 0
        Overlap = 1
    

class CleanUpUtilityBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    HideOriginal: bool
    InferThickness: bool
    SelectBaseFace: ScCollector
    SliverTol: float
    ThicknessValue: Expression
    UseGlobal: bool


class BridgeTransitionBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    AlternateSolution: bool
    EndEdge: SelectEdge
    EndRadius: Expression
    FoldBendOptions: Features.SheetMetal.BendOptions
    FoldTransitionType: int
    InsetType: Features.SheetMetal.BridgeTransitionBuilder.InsetOptions
    Length: Expression
    Plane: SelectISurface
    Point: Point
    ReferenceGeometryPlane: Plane
    StartAndEndParametersEqual: bool
    StartEdge: SelectEdge
    StartRadius: Expression
    TrimOrExtendToBend: bool
    Type: Features.SheetMetal.BridgeTransitionBuilder.TypeOptions
    Width: Expression
    WidthDirection: Features.SheetMetal.BridgeTransitionBuilder.WidthDirectionOptions
    WidthType: Features.SheetMetal.BridgeTransitionBuilder.WidthOptions
    ZuEndEdgeBendOptions: Features.SheetMetal.BendOptions
    ZuStartEdgeBendOptions: Features.SheetMetal.BendOptions


    class WidthOptions(enum.Enum):
        Finite = 0
        Symmetric = 1
        FullStartEdge = 2
        FullEndEdge = 3
        FullBothEdges = 4
    

    class WidthDirectionOptions(enum.Enum):
        Left = 0
        Right = 1
    

    class TypeOptions(enum.Enum):
        Zu = 0
        Fold = 1
    

    class InsetOptions(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
    

    class FoldTransitionTypeOptions(enum.Enum):
        Length = 0
        Bend = 1
    

class BreakCornerBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def SetValue(self, filletRadiusOrSetback: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use Expression.RightHandSide on the Expression object returned from Features.SheetMetal.BreakCornerBuilder.Value instead.")"""
        ...
    def SetEdges(self, edges: typing.List[Edge]) -> None:
        ...
    def GetEdges(self) -> typing.List[Edge]:
        ...
    def SetFaces(self, faces: typing.List[Face]) -> None:
        ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def ValidateBuilderData(self) -> int:
        ...
    Type: Features.SheetMetal.BreakCornerBuilder.TypeOptions
    Value: Expression


    class TypeOptions(enum.Enum):
        Fillet = 0
        ChamferEqualSetback = 1
    

class BendTaperBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    BendTaperAngle1: Expression
    BendTaperAngle2: Expression
    BendTaperInputMethod1: Features.SheetMetal.BendTaperBuilder.BendTaperInputMethod
    BendTaperInputMethod2: Features.SheetMetal.BendTaperBuilder.BendTaperInputMethod
    BendTaperSelectBendFace: ScCollector
    BendTaperType1: Features.SheetMetal.BendTaperBuilder.BendTaperType
    BendTaperType2: Features.SheetMetal.BendTaperBuilder.BendTaperType
    Chaining: Features.SheetMetal.BendTaperBuilder.ChainingType
    EndRadius1: Expression
    EndRadius2: Expression
    InferRadius1: bool
    InferRadius2: bool
    ReverseTaperDirection: bool
    StartRadius1: Expression
    StartRadius2: Expression
    StartType1: Features.SheetMetal.BendTaperBuilder.StartType
    StartType2: Features.SheetMetal.BendTaperBuilder.StartType
    StationaryEntity: NXObject
    TaperDistance1: Expression
    TaperDistance2: Expression
    TaperSides: Features.SheetMetal.BendTaperBuilder.BendTaperSides
    WebTaperAngle1: Expression
    WebTaperAngle2: Expression
    WebTaperType1: Features.SheetMetal.BendTaperBuilder.WebTaperType
    WebTaperType2: Features.SheetMetal.BendTaperBuilder.WebTaperType


    class WebTaperType(enum.Enum):
        None = 0
        Face = 1
        FaceChain = 2
    

    class StartType(enum.Enum):
        TaperFromBend = 0
        TaperFromWeb = 1
    

    class ChainingType(enum.Enum):
        BendOnly = 0
        BendFace = 1
        BendFaceChain = 2
    

    class BendTaperType(enum.Enum):
        Linear = 0
        Tangent = 1
        Square = 2
    

    class BendTaperSides(enum.Enum):
        Both = 0
        Side1 = 1
        Side2 = 2
        Symmetric = 3
    

    class BendTaperInputMethod(enum.Enum):
        Angle = 0
        Distance = 1
        ToEnd = 2
    

class BendOptions(TaggedObject):
    def __init__(self) -> None: ...
    def SetBendRadius(self, radius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from Features.SheetMetal.BendOptions.BendRadius instead.")"""
        ...
    def SetBendReliefDepth(self, depth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from Features.SheetMetal.BendOptions.BendReliefDepth instead.")"""
        ...
    def SetBendReliefWidth(self, width: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from Features.SheetMetal.BendOptions.BendReliefWidth instead.")"""
        ...
    def SetNeutralFactor(self, neutralFactor: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from Features.SheetMetal.BendOptions.NeutralFactor instead.")"""
        ...
    BendRadius: Expression
    BendReliefDepth: Expression
    BendReliefType: Features.SheetMetal.BendOptions.BendReliefTypeOptions
    BendReliefWidth: Expression
    CornerReliefType: Features.SheetMetal.BendOptions.CornerReliefTypeOptions
    DieToolId: int
    DieToolIdName: str
    ExtendBendRelief: bool
    NeutralFactor: Expression
    OverrideToolSet: bool
    PunchToolId: int
    PunchToolIdName: str
    UseGlobalBendRadius: bool
    UseGlobalNeutralFactor: bool
    UseGlobalReliefDepth: bool
    UseGlobalReliefWidth: bool


    class CornerReliefTypeOptions(enum.Enum):
        None = 0
        BendOnly = 1
        BendAndFace = 2
        BendAndFaceChain = 3
    

    class BendReliefTypeOptions(enum.Enum):
        None = 0
        Square = 1
        Round = 2
    

class BendListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.SheetMetal.BendListItemBuilder]) -> None:
        ...
    def Append(self, object: Features.SheetMetal.BendListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.SheetMetal.BendListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Features.SheetMetal.BendListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.BendListItemBuilder) -> None:
        ...
    def Erase(self, obj: Features.SheetMetal.BendListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.SheetMetal.BendListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Features.SheetMetal.BendListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.SheetMetal.BendListItemBuilder, object2: Features.SheetMetal.BendListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Features.SheetMetal.BendListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BendListItemBuilder(Builder):
    def __init__(self) -> None: ...
    BendID: int
    BendName: str


class BendListBuilder(Builder):
    def __init__(self) -> None: ...
    def PopulateBendListFromView(self, flatPatternView: View) -> None:
        ...
    def EditBendItem(self, existingBendId: int, newBendId: int, newBendName: str) -> None:
        ...
    BendList: Features.SheetMetal.BendListItemBuilderList


class BendBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def GetBendAngle(self) -> Expression:
        ...
    def SetBendAngle(self, bendAngle: str) -> None:
        ...
    def ValidateBuilderData(self) -> int:
        ...
    BendLocation: Features.SheetMetal.BendBuilder.BendLocationOptions
    BendOptions: Features.SheetMetal.BendOptions
    Direction: Features.SheetMetal.BendBuilder.BendDirectionOptions
    ExtendProfile: bool
    FixedSide: Features.SheetMetal.BendBuilder.FixedSideOptions
    Section: Section
    Sketch: Features.SketchFeature
    TargetFace: Face


    class FixedSideOptions(enum.Enum):
        SectionSideLeft = 0
        SectionSideRight = 1
    

    class BendLocationOptions(enum.Enum):
        OuterMoldLine = 0
        CenterLine = 1
        InnerMoldLine = 2
        MaterialInside = 3
        MaterialOutside = 4
    

    class BendDirectionOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

class BeadBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetHeight(self, beadHeight: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.BeadBuilder.Height instead.")"""
        ...
    def SetWidth(self, beadWidth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.BeadBuilder.Width instead.")"""
        ...
    def SetAngle(self, beadAngle: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.BeadBuilder.Angle instead.")"""
        ...
    def SetRadius(self, beadRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.BeadBuilder.Radius instead.")"""
        ...
    def SetPunchedWidth(self, punchedWidth: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.BeadBuilder.PunchedWidth instead.")"""
        ...
    def SetPunchRadius(self, punchRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.BeadBuilder.PunchRadius instead.")"""
        ...
    def SetDieRadius(self, beadDieRadius: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Expression.RightHandSide on the NXOpen.Expression object returned from NXOpen.Features.SheetMetal.BeadBuilder.DieRadius instead.")"""
        ...
    def ValidateBuilderData(self) -> int:
        ...
    Angle: Expression
    CrossSectionType: Features.SheetMetal.BeadBuilder.CrossSectionTypeOptions
    DieRadius: Expression
    EndType: Features.SheetMetal.BeadBuilder.EndTypeOptions
    Height: Expression
    HeightSide: Features.SheetMetal.BeadBuilder.HeightSideOptions
    IncludeRounding: bool
    MinimumToolClearance: Expression
    PunchRadius: Expression
    PunchedWidth: Expression
    Radius: Expression
    Section: Section
    Sketch: Features.SketchFeature
    TaperDistance: Expression
    Width: Expression


    class HeightSideOptions(enum.Enum):
        SectionNormalSide = 0
        SectionReverseNormalSide = 1
    

    class EndTypeOptions(enum.Enum):
        Punched = 0
        Lanced = 1
        Formed = 2
        Tapered = 3
    

    class CrossSectionTypeOptions(enum.Enum):
        Circular = 0
        Ushaped = 1
        Vshaped = 2
    

class ApplicationContext(enum.Enum):
    NxSheetMetal = 0
    FlexiblePrintedCircuitDesign = 1
    AerospaceSheetMetal = 2


class AeroUnformBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    BaseFace: Face
    FormFaces: ScCollector


class AeroSheetmetalManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FeatureCollection) -> None: ...
    def CreateFlangeBuilder(self, aerosmFlange: Features.Feature) -> Features.SheetMetal.AeroFlangeBuilder:
        ...
    def CreateJoggleBuilder(self, aerosmJoggle: Features.Feature) -> Features.SheetMetal.AeroJoggleBuilder:
        ...
    def CreateUnformBuilder(self, aerosmUnform: Features.Feature) -> Features.SheetMetal.AeroUnformBuilder:
        ...
    def CreateReformBuilder(self, aerosmReform: Features.Feature) -> Features.SheetMetal.AeroReformBuilder:
        ...
    def CreateFlatSolidBuilder(self, aerosmUnform: Features.Feature) -> Features.SheetMetal.FlatSolidBuilder:
        ...
    def CreateAeroLighteningCutoutBuilder(self, aeroLighteningCutout: Features.Feature) -> Features.SheetMetal.AeroLighteningCutoutBuilder:
        ...
    def CreateFlatPatternBuilder(self, aerosmUnform: Features.Feature) -> Features.SheetMetal.FlatPatternBuilder:
        ...
    def Tag(self) -> Tag: ...



class AeroReformBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    UnformFaceCollector: ScCollector


class AeroLighteningCutoutBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def GetStandards(self) -> str:
        ...
    Angle: Expression
    CheckClearance: bool
    Clearance: Expression
    CornerRadius: Expression
    CutoutProfile: Section
    Diameter: Expression
    DieRadius: Expression
    HoleCenter: Point
    HoleFace: SelectFace
    Length: Expression
    ReverseBendDirection: bool
    StandardName: str
    Type: Features.SheetMetal.AeroLighteningCutoutBuilder.Types


    class Types(enum.Enum):
        Hole = 0
        UserDefined = 1
    

class AeroJoggleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def SetStartPlane(self, startPlane: Plane) -> None:
        ...
    def GetStartPlane(self) -> Plane:
        ...
    def SetEndPlane(self, endPlane: Plane) -> None:
        ...
    def GetEndPlane(self) -> Plane:
        ...
    def SetDepth(self, depthStr: str) -> None:
        ...
    def SetClearance(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType, clearanceStr: str) -> None:
        ...
    def GetClearance(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType) -> Expression:
        ...
    def SetRunout(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType, runoutStr: str) -> None:
        ...
    def GetRunout(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType) -> Expression:
        ...
    def SetStationaryRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType, radiusStr: str) -> None:
        ...
    def GetStationaryRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType) -> Expression:
        ...
    def SetOffsetRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType, radiusStr: str) -> None:
        ...
    def GetOffsetRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType) -> Expression:
        ...
    def SetStandardRunout(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType, standardRunout: bool) -> None:
        ...
    def GetStandardRunout(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType) -> bool:
        ...
    def SetGlobalStationaryRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType, globalRadius: bool) -> None:
        ...
    def GetGlobalStationaryRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType) -> bool:
        ...
    def SetGlobalOffsetRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType, globalRadius: bool) -> None:
        ...
    def GetGlobalOffsetRadius(self, sideType: Features.SheetMetal.AeroJoggleBuilder.SideType) -> bool:
        ...
    BendFaces: ScCollector
    Depth: Expression
    FlipJoggleSide: bool
    IsSymmetric: bool
    IsTwin: bool
    JoggleCompensation: bool
    JoggleIn: bool


    class SideType(enum.Enum):
        Side1 = 0
        Side2 = 1
    

class AeroFlatSolidBuilder(Features.SheetMetal.FlatSolidBuilder):
    def __init__(self) -> None: ...


class AeroFlatPatternBuilder(Features.SheetMetal.FlatPatternBuilder):
    def __init__(self) -> None: ...


class AeroFlangeBuilder(Features.SheetMetal.SheetmetalBaseBuilder):
    def __init__(self) -> None: ...
    def SetAngle(self, angleExpression: str) -> None:
        ...
    def SetLength(self, type: Features.SheetMetal.AeroFlangeBuilder.LengthType, valueExpression: str) -> None:
        ...
    def GetLength(self, type: Features.SheetMetal.AeroFlangeBuilder.LengthType) -> Expression:
        ...
    def SetFlipDirection(self, type: Features.SheetMetal.AeroFlangeBuilder.DirType, flipFlag: bool) -> None:
        ...
    def GetFlipDirection(self, type: Features.SheetMetal.AeroFlangeBuilder.DirType) -> bool:
        ...
    def SetEndCompensation(self, endType: Features.SheetMetal.AeroFlangeBuilder.EndType, compType: Features.SheetMetal.AeroFlangeBuilder.CompType, valueExpression: str) -> None:
        ...
    def GetEndCompensation(self, endType: Features.SheetMetal.AeroFlangeBuilder.EndType, compType: Features.SheetMetal.AeroFlangeBuilder.CompType) -> Expression:
        ...
    def SetEndPlane(self, endType: Features.SheetMetal.AeroFlangeBuilder.EndType, endPlane: Plane) -> None:
        ...
    def GetEndPlane(self, endType: Features.SheetMetal.AeroFlangeBuilder.EndType) -> Plane:
        ...
    def SetContourFlag(self, showContour: bool) -> None:
        ...
    def GetContourFlag(self) -> bool:
        ...
    def SetMaterialType(self, matType: Features.SheetMetal.AeroFlangeBuilder.MatType) -> None:
        ...
    def GetMaterialType(self) -> Features.SheetMetal.AeroFlangeBuilder.MatType:
        ...
    def SetDimensionType(self, dimType: Features.SheetMetal.AeroFlangeBuilder.DimType) -> None:
        ...
    def GetDimensionType(self) -> Features.SheetMetal.AeroFlangeBuilder.DimType:
        ...
    Angle: Expression
    BaseEdges: ScCollector
    BendOptions: Features.SheetMetal.BendOptions
    RefFaces: ScCollector


    class MatType(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
        BendOutside = 2
    

    class LengthType(enum.Enum):
        Value = 0
        Infer = 1
    

    class EndType(enum.Enum):
        End1 = 0
        End2 = 1
        Closed = 2
    

    class DirType(enum.Enum):
        Bend = 0
        Discard = 1
    

    class DimType(enum.Enum):
        Inside = 0
        Outside = 1
    

    class CompType(enum.Enum):
        Automatic = 0
        Angle = 1
        Distance = 2
        None = 3
    

class AdvancedFlangeBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Angle: Expression
    BendOptions: Features.SheetMetal.BendOptions
    Edges: ScCollector
    EndAdjustment: Expression
    Faces: ScCollector
    FlatPatternCompensationAtEnd: bool
    FlatPatternCompensationAtStart: bool
    InferLength: bool
    Inset: Features.SheetMetal.AdvancedFlangeBuilder.Insets
    Length: Expression
    LengthReference: Features.SheetMetal.AdvancedFlangeBuilder.LengthReferences
    Plane1: Plane
    Plane2: Plane
    ReverseDirection: bool
    ReverseTrimSide: bool
    StartAdjustment: Expression
    Type: Features.SheetMetal.AdvancedFlangeBuilder.Types


    class Types(enum.Enum):
        ByValue = 0
        ToReference = 1
    

    class LengthReferences(enum.Enum):
        Inside = 0
        Outside = 1
        Web = 2
        Din6935 = 3
    

    class Insets(enum.Enum):
        MaterialInside = 0
        MaterialOutside = 1
        BendOutside = 2
    

class AdvancedFlange(Features.Feature):
    def __init__(self) -> None: ...


