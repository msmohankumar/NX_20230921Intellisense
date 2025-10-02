from ...NXOpen import *
from ..Drawings import *

import typing
import enum

class ZoneOrigin(enum.Enum):
    BottomRight = 0
    TopLeft = 1
    TopRight = 2
    BottomLeft = 3


class VisualDrawingComparePrefsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CompareMethodType: Drawings.VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsMethodType
    OverlayColor: NXColor
    OverlayDataToUse: Drawings.VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsOverlayDataToUse


    class VisualDrawingComparePrefsOverlayDataToUse(enum.Enum):
        AskatRuntime = 0
        AlwaysUseExistingData = 1
        AlwaysCreateNewData = 2
        CreateNewDataifNoneExists = 3
    

    class VisualDrawingComparePrefsMethodType(enum.Enum):
        AgainstAnotherDrawing = 0
        AgainstOverlayDatainActiveDrawing = 1
    

class VisibleLinesViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    VisibleColor: int
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class VisibleAndHiddenLinesColorFontWidthBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    HiddenCFW: LineColorFontWidthBuilder
    VisibleCFW: LineColorFontWidthBuilder


class VirtualIntersectionsViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    AdjacentBlends: bool
    AdjacentBlendsColor: int
    AdjacentBlendsEndGaps: bool
    AdjacentBlendsEndGapsData: float
    AdjacentBlendsFont: Preferences.Font
    AdjacentBlendsWidth: Preferences.Width
    VirtualIntersection: bool


class ViewWorkflowBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ActiveSketchViewColor: NXColor
    AssociativeAlignment: bool
    BorderColor: NXColor
    CursorTracking: bool
    DisplayBorders: bool
    EnableSmoothEdgesForLWView: bool
    FaceDisplay: Drawings.ViewWorkflowBuilder.Display
    HandlingBodies: Drawings.ViewWorkflowBuilder.Handlingbodies
    HandlingBodiesTypes: Drawings.ViewWorkflowBuilder.HandlingBodiesType
    LargeAssemblyStepThreshold: int
    LoadComponentsOnDemand: bool
    OnLegacyViewUpdate: bool
    OnViewSelection: bool
    PreviewStyle: Drawings.ViewWorkflowBuilder.Style
    SelectGeometryProjectedAsArcs: Drawings.ViewWorkflowBuilder.Splarcs
    ShowFacetEdges: bool
    UseLineAntialiasing: bool
    UseTranslucency: bool


    class Style(enum.Enum):
        Border = 0
        Wireframe = 1
        HiddenWireframe = 2
        Shaded = 3
    

    class Splarcs(enum.Enum):
        Always = 0
        NeverForAutomatic = 1
        Never = 2
    

    class HandlingBodiesType(enum.Enum):
        OmitBodiesfromView = 0
        StopUpdateandNotifyUser = 1
        StopUpdate = 2
        Generate = 3
    

    class Handlingbodies(enum.Enum):
        OmitBodiesfromView = 0
        StopUpdateandNotifyUser = 1
        StopUpdate = 2
        Generate = 3
    

    class Display(enum.Enum):
        DisplayandEmphasize = 0
        CurvesOnly = 1
    

class ViewStyleVisibleLinesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    VisibleColor: NXColor
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class ViewStyleVirtualIntersectionsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AdjacentBlends: bool
    Color: NXColor
    EndGaps: bool
    EndGapsDistance: float
    Font: Preferences.Font
    VirtualIntersections: bool
    Width: Preferences.Width


class ViewStyleTraceLinesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateGaps: bool
    GapSize: float
    HiddenColor: NXColor
    HiddenFont: Preferences.Font
    HiddenWidth: Preferences.Width
    VisibleColor: NXColor
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class ViewStyleThreadsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    MinimumPitchFieldData: float
    OverrideVisibleThreadColor: NXColor
    StandardData: int
    TrueHiddenLine: bool


class ViewStyleSmoothEdgesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Color: NXColor
    EndGaps: bool
    EndGapsDistance: float
    Font: Preferences.Font
    SmoothEdge: bool
    Tolerance: bool
    ToleranceValue: float
    Width: Preferences.Width


class ViewStyleShipbuildingLinesBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Drawings.ViewStyleShipbuildingLinesBuilder]) -> None:
        ...
    def Append(self, object: Drawings.ViewStyleShipbuildingLinesBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Drawings.ViewStyleShipbuildingLinesBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Drawings.ViewStyleShipbuildingLinesBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Drawings.ViewStyleShipbuildingLinesBuilder) -> None:
        ...
    def Erase(self, obj: Drawings.ViewStyleShipbuildingLinesBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Drawings.ViewStyleShipbuildingLinesBuilder]:
        ...
    def SetContents(self, objects: typing.List[Drawings.ViewStyleShipbuildingLinesBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Drawings.ViewStyleShipbuildingLinesBuilder, object2: Drawings.ViewStyleShipbuildingLinesBuilder) -> None:
        ...
    def Insert(self, location: int, object: Drawings.ViewStyleShipbuildingLinesBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ViewStyleShipbuildingLinesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    HiddenColor: NXColor
    HiddenFont: Preferences.Font
    HiddenWidth: Preferences.Width
    SingleLineRepresentation: bool
    VisibleColor: NXColor
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class ViewStyleShadingBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AngleTolerance: float
    CutFaceColor: NXColor
    EdgeTolerance: float
    FaceTolerance: float
    HiddenWireframeColor: NXColor
    RenderingStyle: Preferences.ShadingRenderingStyleOption
    ShadeTolerance: Preferences.ShadingToleranceOption
    ShininessScale: float
    TwoSidedLight: bool
    VisibleWireframeColor: NXColor


class ViewStyleSectionConstraintsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Align: bool
    Offset: bool
    Orient: bool
    Scale: bool
    Sheet: bool


class ViewStyleSectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AdjacencyToleranceData: float
    AssemblyTolerance: bool
    Background: bool
    Bendlines: bool
    Crosshatch: bool
    DisplaySectionLine: bool
    Foreground: bool
    HiddenLineHatching: bool
    RestrictCrosshatchAngle: bool
    SheetBodies: bool


class ViewStyleSecondaryComponentsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    PrimaryHiddenBySecondaryCFW: Drawings.VisibleAndHiddenLinesColorFontWidthBuilder
    ProcessPrimaryHiddenBySecondary: bool
    ProcessSecondaryComponents: bool
    ProcessSecondaryHiddenByPrimary: bool
    SecondaryComponentsCFW: Drawings.VisibleAndHiddenLinesColorFontWidthBuilder
    SecondaryHiddenByPrimaryCFW: Drawings.VisibleAndHiddenLinesColorFontWidthBuilder
    ShowSmoothEdges: bool
    ShowVirtualIntersections: bool


class ViewStyleProjectedBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Align: bool
    Gdt: bool
    Offset: bool
    Orient: bool
    Scale: bool
    Sheet: bool


class ViewStylePerspectiveBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BackClip: bool
    BackClipDistance: float
    FrontClip: bool
    FrontClipDistance: float
    Perspective: bool
    PerspectiveDistance: float
    ViewOrigin: Point3d


class ViewStyleOrientationBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    HingeLine: Drawings.HingeLineBuilder
    Ovt: Drawings.OvtBuilder


class ViewStyleInheritPmiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CrosshatchPmiLwsv: bool
    Gdt: Preferences.GdtOption
    Pmi: Preferences.PmiOption
    PmiFromRevolved: bool
    PmiToDrawing: bool
    PmiTypeMask: int
    ReferenceSetBehavior: Preferences.ReferenceSetBehavior


class ViewStyleHiddenLinesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Color: NXColor
    EdgesHiddenByEdges: bool
    Font: Preferences.Font
    HiddenLine: bool
    IncludeModelCurves: bool
    IncludeModelCurvesOption: Preferences.IncludeModelCurvesOption
    InterferingSolids: Preferences.HiddenLineInterferingSolidsOption
    ReferenceEdgesOnly: bool
    SelfHidden: bool
    SmallFeature: Preferences.HiddenLineSmallFeatureOption
    SmallFeaturesTolerance: float
    Width: Preferences.Width


class ViewStyleGeneralBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetRenderSet(self) -> typing.List[Drawings.RenderSet]:
        ...
    def SetRenderSet(self, renderSets: typing.List[Drawings.RenderSet]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AngleDecimalPointCharacter: Preferences.DecimalPointCharacter
    AngleFormat: Preferences.AngleFormat
    AnglePrecision: int
    AngleSetting: Drawings.AssociativeAngleBuilder
    AngleShowLeadingZeros: bool
    AngleShowTrailingZeros: bool
    AngleValue: float
    AutomaticAnchorPoint: bool
    AutomaticUpdate: bool
    BoundaryStatus: bool
    Centerlines: bool
    DisplayId: Preferences.GeneralDisplayIdOption
    ExtractedEdges: Preferences.GeneralExtractedEdgesOption
    FramebarHorizontal: bool
    FramebarVertical: bool
    LegacyView: bool
    LightweightView: bool
    LockmethodView: Preferences.GeneralViewLockmethodOption
    Reference: bool
    Scale: Drawings.ViewScaleBuilder
    ScaleLabel: bool
    Silhouettes: bool
    SnapshotView: bool
    Tolerance: Preferences.GeneralToleranceOption
    ToleranceValue: float
    UVGrid: bool
    ViewLabel: bool
    ViewQuality: Preferences.GeneralViewQualityOption
    ViewRepresentation: Preferences.GeneralViewRepresentationOption
    ViewStyleFrameBar: Drawings.ViewStyleFrameBarBuilder
    WireframeColorSource: Preferences.GeneralWireframeColorSourceOption


class ViewStyleFrameBarBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Horizontal: bool
    HorizontalDistance: float
    HorizontalPosition: Annotations.BaseFrameBarBuilder.HorizontalPositionType
    Vertical: bool
    VerticalDistance: float
    VerticalPosition: Annotations.BaseFrameBarBuilder.VerticalPositionType


class ViewStyleFPCurvesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Color: NXColor
    Font: Preferences.Font
    State: bool
    Type: SheetMetal.FlatPatternSettings.FlatPatternObjectType
    Width: Preferences.Width


class ViewStyleFPCalloutsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    State: bool
    Type: str


class ViewStyleFPCalloutConfigBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetContents(self, calloutType: str) -> str:
        ...
    def SetContents(self, calloutType: str, contents: str) -> None:
        ...
    def GetOrientationType(self) -> Drawings.ViewStyleFPCalloutConfigBuilder.OrientationType:
        ...
    def SetOrientationType(self, orientation: Drawings.ViewStyleFPCalloutConfigBuilder.OrientationType) -> None:
        ...
    def GetCalloutOffsetDistance(self) -> float:
        ...
    def SetCalloutOffsetDistance(self, calloutOffset: float) -> None:
        ...
    def Validate(self) -> bool:
        ...


    class OrientationType(enum.Enum):
        Leadered = 0
        Aligned = 1
    

class ViewStyleDetailBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Align: bool
    Circular: bool
    ClipViewBoundary: bool
    CreateIndependentDetailView: bool
    Offset: bool
    Orient: bool
    Scale: bool
    Sheet: bool
    ViewBoundaryColor: NXColor
    ViewBoundaryFont: Preferences.Font
    ViewBoundaryWidth: Preferences.Width


class ViewStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetViewStyleFPCallout(self, type: str) -> Drawings.ViewStyleFPCalloutsBuilder:
        ...
    def GetAllViewStyleFPCallouts(self) -> typing.List[Drawings.ViewStyleFPCalloutsBuilder]:
        ...
    def GetViewStyleFPCurve(self, type: SheetMetal.FlatPatternSettings.FlatPatternObjectType) -> Drawings.ViewStyleFPCurvesBuilder:
        ...
    def GetAllViewStyleFPCurves(self) -> typing.List[Drawings.ViewStyleFPCurvesBuilder]:
        ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    def GetViewStyleFPCalloutConfig(self) -> Drawings.ViewStyleFPCalloutConfigBuilder:
        ...
    def FindShipDraftingViewLinesBuilderByName(self, featureName: str, featureSubName: str) -> Drawings.ShipDraftingViewLinesBuilder:
        ...
    def FindShipGeneralArrangementViewLinesBuilderByName(self, viewPlan: str, displayName: str) -> Drawings.ShipGeneralArrangementViewLinesBuilder:
        ...
    def Validate(self) -> bool:
        ...
    ProjectedViewOrientation: Drawings.ProjectedViewOrientationBuilder
    SecondaryComponents: Drawings.ViewStyleSecondaryComponentsBuilder
    ViewCommonViewLabel: Drawings.ViewCommonViewLabelBuilder
    ViewProjectedArrowSettings: Drawings.ViewProjectedArrowSettingsBuilder
    ViewProjectedViewSettings: Drawings.ViewProjectedViewSettingsBuilder
    ViewSectionLineStyleBuilder: Drawings.ViewSectionLineBuilder
    ViewStyleBase: Drawings.ViewStyleBaseBuilder
    ViewStyleDetail: Drawings.ViewStyleDetailBuilder
    ViewStyleGeneral: Drawings.ViewStyleGeneralBuilder
    ViewStyleHiddenLines: Drawings.ViewStyleHiddenLinesBuilder
    ViewStyleInheritPmi: Drawings.ViewStyleInheritPmiBuilder
    ViewStyleOrientation: Drawings.ViewStyleOrientationBuilder
    ViewStylePerspective: Drawings.ViewStylePerspectiveBuilder
    ViewStyleProjected: Drawings.ViewStyleProjectedBuilder
    ViewStyleSection: Drawings.ViewStyleSectionBuilder
    ViewStyleSectionConstraints: Drawings.ViewStyleSectionConstraintsBuilder
    ViewStyleShading: Drawings.ViewStyleShadingBuilder
    ViewStyleShipDraftingViewLinesList: Drawings.ShipDraftingViewLinesBuilderList
    ViewStyleShipGeneralArrangementViewLinesList: Drawings.ShipGeneralArrangementViewLinesBuilderList
    ViewStyleSingleLineList: Drawings.ViewStyleShipbuildingLinesBuilderList
    ViewStyleSmoothEdges: Drawings.ViewStyleSmoothEdgesBuilder
    ViewStyleThreads: Drawings.ViewStyleThreadsBuilder
    ViewStyleTraceLines: Drawings.ViewStyleTraceLinesBuilder
    ViewStyleVirtualIntersections: Drawings.ViewStyleVirtualIntersectionsBuilder
    ViewStyleVisibleLines: Drawings.ViewStyleVisibleLinesBuilder


class ViewStyleBaseBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Arrangement: Assemblies.ArrangementsBuilder
    ArrangementName: str
    FacetedRepresentation: bool
    InheritClippingBoundary: bool
    Part: Part
    PartName: str
    TransferAnnotation: bool


class ViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.DraftingView) -> None: ...
    def Tag(self) -> Tag: ...

    General: Drawings.GeneralViewStyle
    BaseView: Drawings.BaseViewStyle
    Projected: Drawings.ProjectedViewStyle
    InheritPmi: Drawings.InheritPmiViewStyle
    Section: Drawings.SectionViewStyle
    VirtualIntersections: Drawings.VirtualIntersectionsViewStyle
    SmoothEdges: Drawings.SmoothEdgesViewStyle
    Perspective: Drawings.PerspectiveViewStyle
    Orientation: Drawings.OrientationViewStyle
    VisibleLines: Drawings.VisibleLinesViewStyle
    Threads: Drawings.ThreadsViewStyle
    TraceLines: Drawings.TraceLinesViewStyle
    HiddenLines: Drawings.HiddenLinesViewStyle
    Shading: Drawings.ShadingViewStyle
    FlatPattern: Drawings.FlatPatternViewStyle
    ShipbuildingLines: Drawings.ShipbuildingLinesViewStyle
    ShipDraftingViewLines: Drawings.ShipDraftingViewLinesViewStyle
    ShipGeneralArrangementViewLines: Drawings.ShipGeneralArrangementViewLinesViewStyle


class ViewSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AddSheetName: bool
    AddSheetNumber: bool
    ApplyCrosshatchToSectionView: bool
    ConvertAnnotation: bool
    Prefix: str
    RenderingStyle: Drawings.ViewSettingsBuilder.RenderingStyleEnum
    SectionGeometryTolerance: float
    Separator: str
    UseAssemblyCrosshatch: bool


    class RenderingStyleEnum(enum.Enum):
        Shaded = 0
        DrawingViewSetting = 1
    

class ViewSectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ArrowLength: float
    ArrowheadAngle: float
    ArrowheadLength: float
    BendAndEndSegmentWidthFactor: float
    BorderToArrowDistance: float
    Display: bool
    DisplayLettersOnBends: bool
    DisplayRotationLetter: bool
    Gap: float
    LabelLocation: Drawings.ViewSectionLineBuilder.LocationType
    LineColorFontWidth: LineColorFontWidthBuilder
    LineLength: float
    Overhang: float
    SelectRotationLetter: SelectTaggedObject
    ShowSectionLine: Drawings.ViewSectionLineBuilder.ShowSectionLineType
    Style: Drawings.ViewSectionLineBuilder.StyleType
    TypeStandard: Drawings.ViewSectionLineBuilder.DisplayType
    UseLineLength: bool
    UseOffset: bool


    class StyleType(enum.Enum):
        Open = 0
        Closed = 1
        Filled = 2
    

    class ShowSectionLineType(enum.Enum):
        WithSectionView = 0
        WithoutSectionView = 1
    

    class LocationType(enum.Enum):
        OnArrow = 0
        OnEnd = 1
    

    class DisplayType(enum.Enum):
        ArrowsAwayfromLine = 0
        ArrowstowardsLine = 1
        ThickEndsArrowstowardsLine = 2
        ThickEndsArrowsAwayfromLine = 3
    

class ViewSectionLabelBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetCustomizedViewLabelText(self) -> str:
        ...
    def SetCustomizedViewLabelText(self, customizedText: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CustomizedViewLabel: bool
    IncludeParentheses: bool
    IncludeRotationAngle: bool
    IncludeRotationSymbol: bool
    LabelCharacterHeightFactor: float
    LabelPosition: Drawings.LabelPositionTypes
    LabelPrefix: str
    LetterFormat: Drawings.LetterFormatTypes
    PrefixCharacterHeightFactor: float
    ReferenceToShow: Drawings.ReferenceShowTypes
    RotationSymbolType: Drawings.RotationSymbolTypes
    ScaleCharacterHeightFactor: float
    ScalePosition: Drawings.ScalePositionTypes
    ScalePrefix: str
    ShowViewLabel: bool
    ShowViewScale: bool
    ValueFormat: Drawings.ScaleValueFormatTypes
    ViewLabelOption: Drawings.ViewLabelTypes


class ViewScaleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Denominator: float
    Expression: Expression
    Numerator: float
    ScaleType: Drawings.ViewScaleBuilder.Type


    class Type(enum.Enum):
        Ratio = 0
        Expression = 1
    

class ViewProjectionPlaneBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Axis: Axis
    DepthValue: Expression
    PlaneOption: Drawings.ViewProjectionPlaneBuilder.PlaneOptions
    View: Drawings.SelectDraftingView


    class PlaneOptions(enum.Enum):
        Inferred = 0
        DepthValue = 1
    

class ViewProjectionBuilder(Builder):
    def __init__(self) -> None: ...
    CurvePoints: Section
    CurveTypeEdges: Drawings.ViewProjectionBuilder.CurveType
    CurveTypePlane1: Drawings.ViewProjectionBuilder.CurveType
    CurveTypePlane2: Drawings.ViewProjectionBuilder.CurveType
    FromView: View
    Plane1: Drawings.ViewProjectionPlaneBuilder
    Plane2: Drawings.ViewProjectionPlaneBuilder
    ToViews: Drawings.SelectDraftingViewList
    Type: Drawings.ViewProjectionBuilder.Types


    class Types(enum.Enum):
        ProjectOnOnePlane = 0
        ProjectOnTwoPlanes = 1
    

    class CurveType(enum.Enum):
        Active = 0
        Reference = 1
        None = 2
    

class ViewProjectedViewSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DisplayArrowOnParentView: Drawings.ViewProjectedViewSettingsBuilder.DisplayArrowOnParentViewType


    class DisplayArrowOnParentViewType(enum.Enum):
        No = 0
        NonOrtho = 1
        All = 2
    

class ViewProjectedLabelBuilder(Drawings.ViewLabelBuilder):
    def __init__(self) -> None: ...


class ViewProjectedArrowSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ArrowHeadAngle: float
    ArrowHeadLength: float
    ArrowHeadStyle: Drawings.ViewProjectedArrowSettingsBuilder.DimensionsStyleType
    ArrowLineDistanceToGeometry: float
    ArrowLineLength: float
    DisplayLabel: Drawings.ViewProjectedArrowSettingsBuilder.DispalyLabelType
    LineColorFontWidth: LineColorFontWidthBuilder
    SizeFactor: float


    class DispalyLabelType(enum.Enum):
        No = 0
        OnReferenceArrow = 1
        OnReferenceArrowAndView = 2
    

    class DimensionsStyleType(enum.Enum):
        Filled = 0
        Closed = 1
        Open = 2
    

class ViewPlacementBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlignmentMethod: Drawings.ViewPlacementBuilder.Method
    AlignmentOption: Drawings.ViewPlacementBuilder.Option
    AlignmentPoint: SelectTaggedObject
    AlignmentVector: Direction
    AlignmentView: Drawings.SelectDraftingView
    Associative: bool
    CandidatePoint: SelectTaggedObject
    LockOffset: bool
    Offset: float
    Placement: SelectNXObject


    class Option(enum.Enum):
        ToView = 0
        ModelPoint = 1
        PointToPoint = 2
    

    class Method(enum.Enum):
        Infer = 0
        Horizontal = 1
        Vertical = 2
        PerpendicularToLine = 3
        Overlay = 4
        PerpendicularToHingeLine = 5
        Max = 6
    

class ViewOrientationBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    OrientationType: Drawings.ViewOrientationBuilder.Orientation
    SelectView: SelectView


    class Orientation(enum.Enum):
        Orthographic = 0
        InheritOrientation = 1
        UseParentOrientation = 2
        UseParentOrienation = 2
        SectionExisting = 3
    

class ViewLabelTypes(enum.Enum):
    Name = 0
    Letter = 1


class ViewLabelBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetCustomizedViewLabelText(self) -> str:
        ...
    def SetCustomizedViewLabelText(self, customizedText: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CustomizedViewLabel: bool
    IncludeParentheses: bool
    IncludeRotationAngle: bool
    IncludeRotationSymbol: bool
    LabelCharacterHeightFactor: float
    LabelPosition: Drawings.LabelPositionTypes
    LabelPrefix: str
    LetterFormat: Drawings.LetterFormatTypes
    PrefixCharacterHeightFactor: float
    ReferenceToShow: Drawings.ReferenceShowTypes
    RotationSymbolType: Drawings.RotationSymbolTypes
    ScaleCharacterHeightFactor: float
    ScalePosition: Drawings.ScalePositionTypes
    ScalePrefix: str
    ShowViewLabel: bool
    ShowViewScale: bool
    ValueFormat: Drawings.ScaleValueFormatTypes
    ViewLabelOption: Drawings.ViewLabelTypes


class ViewingDirectionArrowLabel(Annotations.Note):
    def __init__(self) -> None: ...


class ViewingDirectionArrow(Annotations.BaseArrow):
    def __init__(self) -> None: ...


class ViewDetailLabelBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetCustomizedViewLabelText(self) -> str:
        ...
    def SetCustomizedViewLabelText(self, customizedText: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CustomizedViewLabel: bool
    IncludeParentheses: bool
    LabelCharacterHeightFactor: float
    LabelParentDisplay: Drawings.ViewDetailLabelBuilder.LabelParentDisplayTypes
    LabelPosition: Drawings.LabelPositionTypes
    LabelPrefix: str
    LetterFormat: Drawings.LetterFormatTypes
    ParentLabelPrefix: str
    PrefixCharacterHeightFactor: float
    ReferenceToShow: Drawings.ReferenceShowTypes
    ScaleCharacterHeightFactor: float
    ScalePosition: Drawings.ScalePositionTypes
    ScalePrefix: str
    ShowViewLabel: bool
    ShowViewScale: bool
    TextGapFactor: float
    TextPlacement: Drawings.ViewDetailLabelBuilder.LabelParentTextPlacement
    ValueFormat: Drawings.ScaleValueFormatTypes
    ViewLabelOption: Drawings.ViewLabelTypes


    class LabelParentTextPlacement(enum.Enum):
        BeforeOrAfterStub = 0
        AboveStub = 1
    

    class LabelParentDisplayTypes(enum.Enum):
        None = 0
        Circle = 1
        Note = 2
        Label = 3
        Embedded = 4
        Boundary = 5
        LabelOnBoundary = 6
    

class ViewCreationWizardBuilder(Builder):
    def __init__(self) -> None: ...
    AssociativeAlignment: bool
    AutoScale: bool
    BackView: bool
    BaseView: str
    BottomView: bool
    CenterLines: bool
    CrosshatchInheritedSectionViews: bool
    CustomViewSettingsBuilder: Drawings.CustomViewSettingsBuilder
    ExtractedEdges: bool
    FrontView: bool
    HiddenLineColor: int
    HiddenLineFont: int
    HiddenLineWidth: int
    HiddenLines: bool
    IgnoreTitleBlock: bool
    InheritPMI: int
    InheritPmiOntoDrawing: bool
    IsometricView: bool
    LeftView: bool
    LockMethod: Preferences.GeneralViewLockmethodOption
    MarginBetweenViews: float
    MarginToBorder: float
    MultipleViewPlacement: Drawings.MultipleViewPlacementBuilder
    OptimizeSettings: bool
    OrientViewTool: Drawings.OvtBuilder
    Part: Part
    PlacementOption: Drawings.ViewCreationWizardBuilder.Option
    PmiDimensionFromRevolved: bool
    PmiTypes: int
    Resolution: Drawings.ViewCreationWizardBuilder.ResolutionOption
    RightView: bool
    Silhouettes: bool
    SnapShot: bool
    SpecialBaseView: bool
    Tolerance: float
    TopView: bool
    TrimetricView: bool
    ViewBoundary: Drawings.ViewCreationWizardBuilder.ViewBoundaryOption
    ViewLabels: bool
    ViewRepresentation: Drawings.ViewCreationWizardBuilder.ViewRepresentations
    ViewScale: Drawings.ViewScaleBuilder
    ViewStyle: Drawings.ViewStyleBuilder


    class ViewRepresentations(enum.Enum):
        Exact = 0
        SmartLightweight = 1
        Lightweight = 2
        PreNx85Exact = 3
    

    class ViewBoundaryOption(enum.Enum):
        Automatic = 0
        Manual = 1
    

    class ResolutionOption(enum.Enum):
        Coarse = 0
        Medium = 1
        Fine = 2
    

    class Option(enum.Enum):
        Automatic = 0
        Manual = 1
    

class ViewCopyTo3dBuilder(Builder):
    def __init__(self) -> None: ...
    def Commit(self, offset: float, curves: bool, sketches: bool, option: int) -> None:
        """[Obsolete("Deprecated in NX7.5.0.  This method is no longer relevant and calls to this can be safely removed.")"""
        ...
    BoundingBox: Drawings.ViewCopyTo3dBuilder.BoundingBoxOption
    BoundingViews: Drawings.SelectDrawingViewList
    CreateSketches: bool
    Curves: SelectNXObjectList
    DestinationPart: str
    DistanceFromViewPlane: Drawings.ViewCopyTo3dBuilder.DistanceFromViewPlaneOption
    ExtrudeSolidBody: bool
    Offset: Expression
    Output: Drawings.ViewCopyTo3dBuilder.OutputOption
    ProcessSketchCurves: bool
    ProcessViewCurves: bool
    RepositionGeometry: bool
    Type: Drawings.ViewCopyTo3dBuilder.Types
    View: Drawings.SelectDrawingView
    Views: Drawings.SelectDrawingViewList


    class Types(enum.Enum):
        SelectedCurves = 0
        SelectedViews = 1
    

    class OutputOption(enum.Enum):
        Sketches = 0
        SimpleCurves = 1
        SketchesSolid = 2
        PartsGroup = 3
    

    class Option(enum.Enum):
        Automatic = 0
        Specify = 1
    

    class DistanceFromViewPlaneOption(enum.Enum):
        Automatic = 0
        Specify = 1
    

    class BoundingBoxOption(enum.Enum):
        CurvesToCopy = 0
        EntireViews = 1
    

class ViewCommonViewLabelBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Letter: str
    SecondaryAlignment: Drawings.ViewCommonViewLabelBuilder.SecondaryAlignmentType
    SecondaryIndexing: Drawings.ViewCommonViewLabelBuilder.SecondaryIndexingType
    SubscriptSizeFactor: float


    class SecondaryIndexingType(enum.Enum):
        Alphabetic = 0
        Numeric = 1
    

    class SecondaryAlignmentType(enum.Enum):
        Inline = 0
        Subscript = 1
    

class ViewCenterCoordinateBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    XCoordinate: float
    XCoordinateExp: Expression
    YCoordinate: float
    YCoordinateExp: Expression
    ZCoordinate: float
    ZCoordinateExp: Expression


class ViewBreakCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.ViewBreak]:
        ...
    def __init__(self, owner: Drawings.DraftingView) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Drawings.ViewBreak:
        ...
    def Tag(self) -> Tag: ...



class ViewBreakBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AddForeshorteningSymbol: bool
    BreakGap: float
    BreakLineAmplitude: float
    BreakLineColorWidth: LineColorFontWidthBuilder
    BreakLineExtension: float
    BreakLineStyle: Drawings.ViewBreakBuilder.Viewbreaklinestyle
    PropagateViewBreak: bool
    ShowBreakLines: bool


    class Viewbreaklinestyle(enum.Enum):
        Simple = 0
        Straight = 1
        Sawtooth = 2
        LongBreak = 3
        Tubular = 4
        SolidTubular = 5
        SolidRod = 6
        Jigsaw = 7
        Wood = 8
        CopyCurve = 9
        TemplateCurve = 10
    

class ViewBreak(NXObject):
    def __init__(self) -> None: ...
    def GetViewBreakDisplayableObjectsAndOffsets(self, displayObjects: typing.List[DisplayableObject]) -> typing.List[Vector3d]:
        ...


class ViewBoundaryBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BoundaryPoint1: Point
    BoundaryPoint2: Point
    BoundaryType: Drawings.ViewBoundaryBuilder.Type


    class Type(enum.Enum):
        Automatic = 0
        Manual = 1
        BreakLine = 2
        Bound = 3
    

class ViewAlignmentCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.ViewAlignment]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateViewAlignmentBuilder(self) -> Drawings.ViewAlignmentBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Drawings.ViewAlignment:
        ...
    def Tag(self) -> Tag: ...



class ViewAlignmentBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteCurrentAlignment(self) -> None:
        ...
    CandidateView: Drawings.DraftingView
    InEditMode: bool
    Placement: Drawings.ViewPlacementBuilder
    SelectedAlignment: Drawings.ViewAlignment
    View: Drawings.SelectDraftingView


class ViewAlignment(NXObject):
    def __init__(self) -> None: ...


class View2dOrientBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetCustomNormalX(self) -> float:
        ...
    def SetCustomNormalX(self, component: float) -> None:
        ...
    def GetCustomNormalY(self) -> float:
        ...
    def SetCustomNormalY(self, component: float) -> None:
        ...
    def GetCustomNormalZ(self) -> float:
        ...
    def SetCustomNormalZ(self, component: float) -> None:
        ...
    def GetInferredPrimary(self) -> bool:
        ...
    def SetInferredPrimary(self, inferred: bool) -> None:
        ...
    def GetCustomPrimaryX(self) -> float:
        ...
    def SetCustomPrimaryX(self, component: float) -> None:
        ...
    def GetCustomPrimaryY(self) -> float:
        ...
    def SetCustomPrimaryY(self, component: float) -> None:
        ...
    def GetCustomPrimaryZ(self) -> float:
        ...
    def SetCustomPrimaryZ(self, component: float) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CustomOrientationMethod: Drawings.View2dOrientBuilder.CustomMethod
    CustomXAngle: float
    CustomYAngle: float
    CustomZAngle: float
    OrientationType: Drawings.View2dOrientBuilder.Type


    class Type(enum.Enum):
        None = 0
        Top = 1
        Front = 2
        Right = 3
        Back = 4
        Bottom = 5
        Left = 6
        Iso = 7
        Tri = 8
        Custom = 9
    

    class CustomMethod(enum.Enum):
        Angles = 0
        Vector = 1
    

class VerticalCenteringMarkType(enum.Enum):
    None = 0
    BottomArrow = 1
    TopArrow = 2
    BottomandTopArrow = 3
    BottomandTopLine = 4


class UpdateViewsBuilder(Builder):
    def __init__(self) -> None: ...
    Views: SelectObjectList


class TrimmingMarkStyleType(enum.Enum):
    Triangle = 0
    Corner = 1


class TrackDrawingChangesReportFilterBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetReportFilterStatus(self, reportFilterType: Drawings.TrackDrawingChangesReportFilterBuilder.Filter) -> bool:
        ...
    def SetReportFilterStatus(self, reportFilterType: Drawings.TrackDrawingChangesReportFilterBuilder.Filter, reportFilterStatus: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...


    class Filter(enum.Enum):
        Sheets = 0
        Views = 1
        DimensionsAll = 2
        DimensionsRetainedStatus = 3
        DimensionsSize = 4
        DimensionsOrigin = 5
        AnnotationNotes = 6
        AnnotationNotesRetainedStatus = 7
        AnnotationNotesText = 8
        AnnotationNotesOrigin = 9
        AnnotationNotesLeaderTerminator = 10
        AnnotationFCF = 11
        AnnotationFCFRetainedStatus = 12
        AnnotationFCFText = 13
        AnnotationFCFOrigin = 14
        AnnotationFCFLeaderTerminator = 15
        AnnotationDFS = 16
        AnnotationDFSRetainedStatus = 17
        AnnotationDFSText = 18
        AnnotationDFSOrigin = 19
        AnnotationDFSLeaderTerminator = 20
        AnnotationDTS = 21
        AnnotationDTSRetainedStatus = 22
        AnnotationDTSText = 23
        AnnotationDTSOrigin = 24
        AnnotationDTSLeaderTerminator = 25
        AnnotationBalloons = 26
        AnnotationBalloonsRetainedStatus = 27
        AnnotationBalloonsText = 28
        AnnotationBalloonsOrigin = 29
        AnnotationBalloonsLeaderTerminator = 30
        AnnotationSFS = 31
        AnnotationSFSRetainedStatus = 32
        AnnotationSFSText = 33
        AnnotationSFSOrigin = 34
        AnnotationSFSLeaderTerminator = 35
        AnnotationWeldSymbol = 36
        AnnotationWeldSymbolRetainedStatus = 37
        AnnotationWeldSymbolText = 38
        AnnotationWeldSymbolOrigin = 39
        AnnotationWeldSymbolLeaderTerminator = 40
        AnnotationTPS = 41
        AnnotationInterSymbol = 42
        AnnotationCrosshatch = 43
        AnnotationCenterlines = 44
        Symbols = 45
        SymbolsRetainedStatus = 46
        SymbolsText = 47
        SymbolsOrigin = 48
        SymbolsLeaderTerminator = 49
        Tables = 50
        PartsLists = 51
        HoleTable = 52
        SketchCurvesLines = 53
        SketchCurvesArcs = 54
        SketchCurvesCircles = 55
        SketchCurvesConics = 56
        SketchCurvesSplines = 57
    

class TrackDrawingChangesGeneralBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BaselineOfComparison: Drawings.TrackDrawingChangesGeneralBuilder.BaselineOfComparisonType
    ChangeSymbolLineColorFontWidth: LineColorFontWidthBuilder
    ChangeSymbolSize: float
    ChangeSymbolType: Drawings.TrackDrawingChangesGeneralBuilder.SymbolType
    CompareMethod: Drawings.TrackDrawingChangesGeneralBuilder.CompareMethodType
    CompareTolerance: float
    CreateOverlayDataWithSnapshotData: bool
    DisplayChangeSymbol: bool
    IncrementIDNumberPerReport: bool
    PreserveChangeSymbolDisplay: bool
    RestartIDNumbersWithNewReport: bool
    SnapshotDataToUse: Drawings.TrackDrawingChangesGeneralBuilder.SnapshotDataToUseType


    class SymbolType(enum.Enum):
        Circle = 0
        TriangleUp = 1
        TriangleDown = 2
        Square = 3
        Hexagon = 4
    

    class SnapshotDataToUseType(enum.Enum):
        AskAtRunTime = 0
        AlwaysUseExistingData = 1
        AlwaysCreateNewData = 2
        CreateNewDataifNoneExists = 3
    

    class CompareMethodType(enum.Enum):
        AgainstAnotherDrawing = 0
        AgainstSnapshotDataInActiveDrawing = 1
        OpenSavedComparisonReport = 2
    

    class BaselineOfComparisonType(enum.Enum):
        Snapshot = 0
        TrackedChanges = 1
    

class TraceLinesViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    CreateGapsStatus: bool
    GapSize: float
    HiddenColor: int
    HiddenFont: Preferences.Font
    HiddenWidth: Preferences.Width
    VisibleColor: int
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class ThreadsViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    MinimumPitchField: float
    OverrideVisibleThreadColor: int
    RenderTrueHiddenLine: bool
    ThreadsStandardOptionData: int


class SvtBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BackgroundFaces: SelectFaceList
    NormalDirection: Direction
    Orientation: bool
    XDirection: Direction


class SteppedSectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use Drawings.SectionViewBuilder.SectionViewType instead..")"""
        ...
    EndLocation1: Point
    EndLocation2: Point
    Leg1: Drawings.SectionLineSegmentBuilderList


class SteppedSectionLine(Drawings.BaseSteppedSectionLine):
    def __init__(self) -> None: ...


class StandardViewsBuilder(Builder):
    def __init__(self) -> None: ...
    Autoscale: bool
    Coordinate: Drawings.ViewCenterCoordinateBuilder
    FirstCorner: Drawings.ViewPlacementBuilder
    HiddenObjects: Drawings.HiddenObjectsBuilder
    LayoutType: Drawings.StandardViewsBuilder.Type
    MarginBetweenViews: float
    MarginToBorder: float
    MultipleViewPlacement: Drawings.MultipleViewPlacementBuilder
    NonSectionedObjects: Drawings.HiddenObjectsBuilder
    Part: Part
    PlacementType: Drawings.StandardViewsBuilder.Placement
    Scale: Drawings.ViewScaleBuilder
    SecondCorner: Drawings.ViewPlacementBuilder
    SecondaryComponents: Drawings.DraftingComponentSelectionBuilder
    ViewPlacement: Drawings.ViewPlacementBuilder
    ViewStyle: Drawings.ViewStyleBuilder
    ViewType: Drawings.StandardViewsBuilder.View


    class View(enum.Enum):
        Drawing = 0
        Base = 1
    

    class Type(enum.Enum):
        FrontTop = 0
        FrontRight = 1
        FrontLeft = 2
        FrontTopRight = 3
        FrontTopLeft = 4
        FrontTopRightIso = 5
        FrontTopLeftIso = 6
    

    class Placement(enum.Enum):
        Center = 0
        Corner = 1
    

class SpecifySectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SectionLine: Drawings.SelectSectionLine


class SmoothEdgesViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    SmoothEdge: bool
    SmoothEdgeColor: int
    SmoothEdgeEndGaps: bool
    SmoothEdgeEndGapsData: float
    SmoothEdgeFont: Preferences.Font
    SmoothEdgeTolerance: bool
    SmoothEdgeToleranceData: float
    SmoothEdgeWidth: Preferences.Width


class SketchSectionLineBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSketch(self, sketch: Sketch) -> None:
        ...
    AssociateToSketch: bool
    FoldedToggle: bool
    ParentView: Drawings.ParentViewBuilder
    ReverseDirection: bool
    SectionLineType: Drawings.SketchSectionLineBuilder.SectionLineTypes
    SectionType: Drawings.SketchSectionLineBuilder.Type
    Settings: Drawings.SectionLineSettingsBuilder
    SketchSection: Section
    SourceView: Drawings.SelectDraftingView


    class Type(enum.Enum):
        StandAlone = 0
        Derived = 1
    

    class SectionLineTypes(enum.Enum):
        SimpleStepped = 0
        Half = 1
        PoinToPoint = 2
    

class SketchedSteppedSectionLine(Drawings.BaseSteppedSectionLine):
    def __init__(self) -> None: ...


class SketchedPointToPointSectionLine(Drawings.BasePointToPointSectionLine):
    def __init__(self) -> None: ...


class SketchedHalfSectionLine(Drawings.BaseHalfSectionLine):
    def __init__(self) -> None: ...


class ShipGeneralArrangementViewLinesViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def SetAttributeName(self, viewPlan: str, displayName: str, attributeName: str) -> None:
        ...
    def GetAttributeName(self, viewPlan: str, displayName: str) -> str:
        ...
    def SetAttributeValue(self, viewPlan: str, displayName: str, attributeValue: str) -> None:
        ...
    def GetAttributeValue(self, viewPlan: str, displayName: str) -> str:
        ...
    def SetColor(self, viewPlan: str, displayName: str, linesType: Drawings.ShipGeneralArrangementViewLinesViewStyle.Lines, color: NXColor) -> None:
        ...
    def GetColor(self, viewPlan: str, displayName: str, linesType: Drawings.ShipGeneralArrangementViewLinesViewStyle.Lines) -> NXColor:
        ...
    def SetFont(self, viewPlan: str, displayName: str, linesType: Drawings.ShipGeneralArrangementViewLinesViewStyle.Lines, font: Preferences.Font) -> None:
        ...
    def GetFont(self, viewPlan: str, displayName: str, linesType: Drawings.ShipGeneralArrangementViewLinesViewStyle.Lines) -> Preferences.Font:
        ...
    def SetWidth(self, viewPlan: str, displayName: str, linesType: Drawings.ShipGeneralArrangementViewLinesViewStyle.Lines, width: Preferences.Width) -> None:
        ...
    def GetWidth(self, viewPlan: str, displayName: str, linesType: Drawings.ShipGeneralArrangementViewLinesViewStyle.Lines) -> Preferences.Width:
        ...
    def Tag(self) -> Tag: ...



    class Lines(enum.Enum):
        Visible = 0
        Hidden = 1
    

class ShipGeneralArrangementViewLinesBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Drawings.ShipGeneralArrangementViewLinesBuilder]) -> None:
        ...
    def Append(self, object: Drawings.ShipGeneralArrangementViewLinesBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Drawings.ShipGeneralArrangementViewLinesBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Drawings.ShipGeneralArrangementViewLinesBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Drawings.ShipGeneralArrangementViewLinesBuilder) -> None:
        ...
    def Erase(self, obj: Drawings.ShipGeneralArrangementViewLinesBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Drawings.ShipGeneralArrangementViewLinesBuilder]:
        ...
    def SetContents(self, objects: typing.List[Drawings.ShipGeneralArrangementViewLinesBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Drawings.ShipGeneralArrangementViewLinesBuilder, object2: Drawings.ShipGeneralArrangementViewLinesBuilder) -> None:
        ...
    def Insert(self, location: int, object: Drawings.ShipGeneralArrangementViewLinesBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ShipGeneralArrangementViewLinesBuilder(Builder):
    def __init__(self) -> None: ...
    AttributeName: str
    AttributeValue: str
    HiddenColor: NXColor
    HiddenFont: Preferences.Font
    HiddenWidth: Preferences.Width
    VisibleColor: NXColor
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class ShipDraftingViewLinesViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def SetShipDrawingObject(self, featureName: str, singleLine: bool) -> None:
        ...
    def GetShipDrawingObject(self, featureName: str) -> bool:
        ...
    def SetColor(self, featureName: str, linesType: Drawings.ShipDraftingViewLinesViewStyle.Lines, color: NXColor) -> None:
        ...
    def GetColor(self, featureName: str, linesType: Drawings.ShipDraftingViewLinesViewStyle.Lines) -> NXColor:
        ...
    def SetFont(self, featureName: str, linesType: Drawings.ShipDraftingViewLinesViewStyle.Lines, font: Preferences.Font) -> None:
        ...
    def GetFont(self, featureName: str, linesType: Drawings.ShipDraftingViewLinesViewStyle.Lines) -> Preferences.Font:
        ...
    def SetWidth(self, featureName: str, linesType: Drawings.ShipDraftingViewLinesViewStyle.Lines, width: Preferences.Width) -> None:
        ...
    def GetWidth(self, featureName: str, linesType: Drawings.ShipDraftingViewLinesViewStyle.Lines) -> Preferences.Width:
        ...
    def Tag(self) -> Tag: ...



    class Lines(enum.Enum):
        HiddenNonsection = 0
        VisibleNonsection = 1
        HiddenSection = 2
        VisibleSection = 3
        SecondaryHiddenNonsection = 4
        SecondaryVisibleNonsection = 5
        SecondaryHiddenSection = 6
        SecondaryVisibleSection = 7
    

class ShipDraftingViewLinesBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Drawings.ShipDraftingViewLinesBuilder]) -> None:
        ...
    def Append(self, object: Drawings.ShipDraftingViewLinesBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Drawings.ShipDraftingViewLinesBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Drawings.ShipDraftingViewLinesBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Drawings.ShipDraftingViewLinesBuilder) -> None:
        ...
    def Erase(self, obj: Drawings.ShipDraftingViewLinesBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Drawings.ShipDraftingViewLinesBuilder]:
        ...
    def SetContents(self, objects: typing.List[Drawings.ShipDraftingViewLinesBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Drawings.ShipDraftingViewLinesBuilder, object2: Drawings.ShipDraftingViewLinesBuilder) -> None:
        ...
    def Insert(self, location: int, object: Drawings.ShipDraftingViewLinesBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ShipDraftingViewLinesBuilder(Builder):
    def __init__(self) -> None: ...
    NonSectionedHiddenColor: NXColor
    NonSectionedHiddenFont: Preferences.Font
    NonSectionedHiddenWidth: Preferences.Width
    NonSectionedSecondaryHiddenColor: NXColor
    NonSectionedSecondaryHiddenFont: Preferences.Font
    NonSectionedSecondaryHiddenWidth: Preferences.Width
    NonSectionedSecondaryVisibleColor: NXColor
    NonSectionedSecondaryVisibleFont: Preferences.Font
    NonSectionedSecondaryVisibleWidth: Preferences.Width
    NonSectionedVisibleColor: NXColor
    NonSectionedVisibleFont: Preferences.Font
    NonSectionedVisibleWidth: Preferences.Width
    SectionedHiddenColor: NXColor
    SectionedHiddenFont: Preferences.Font
    SectionedHiddenWidth: Preferences.Width
    SectionedSecondaryHiddenColor: NXColor
    SectionedSecondaryHiddenFont: Preferences.Font
    SectionedSecondaryHiddenWidth: Preferences.Width
    SectionedSecondaryVisibleColor: NXColor
    SectionedSecondaryVisibleFont: Preferences.Font
    SectionedSecondaryVisibleWidth: Preferences.Width
    SectionedVisibleColor: NXColor
    SectionedVisibleFont: Preferences.Font
    SectionedVisibleWidth: Preferences.Width
    SingleLineRepresentation: bool


class ShipbuildingLinesViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def SetSingleLineRepresentation(self, featureType: Drawings.ShipbuildingLinesViewStyle.ShipbuildingLines, featureName: str, singleLine: bool) -> None:
        ...
    def GetSingleLineRepresentation(self, featureType: Drawings.ShipbuildingLinesViewStyle.ShipbuildingLines, featureName: str) -> bool:
        ...
    def SetColor(self, featureName: str, linesType: Drawings.ShipbuildingLinesViewStyle.Lines, color: int) -> None:
        ...
    def GetColor(self, featureName: str, linesType: Drawings.ShipbuildingLinesViewStyle.Lines) -> int:
        ...
    def SetFont(self, featureName: str, linesType: Drawings.ShipbuildingLinesViewStyle.Lines, font: Preferences.Font) -> None:
        ...
    def GetFont(self, featureName: str, linesType: Drawings.ShipbuildingLinesViewStyle.Lines) -> Preferences.Font:
        ...
    def SetWidth(self, featureName: str, linesType: Drawings.ShipbuildingLinesViewStyle.Lines, width: Preferences.Width) -> None:
        ...
    def GetWidth(self, featureName: str, linesType: Drawings.ShipbuildingLinesViewStyle.Lines) -> Preferences.Width:
        ...
    def Tag(self) -> Tag: ...



    class ShipbuildingLines(enum.Enum):
        Profile = 0
        Plate = 1
    

    class Lines(enum.Enum):
        Hidden = 0
        Visible = 1
    

class SheetZoneSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ContinueZoneIndexingAcrossSheets: bool
    CornerZoneModification: float
    CreateZoneLabels: bool
    CreateZoneMarkings: bool
    CreateZones: bool
    HorizontalSize: float
    LabelColor: int
    LabelFont: int
    LabelHeight: float
    LabelItalicized: bool
    LabelWidth: int
    LabelsToSkip: str
    MarkingHeight: float
    MarkingLineColorWidth: LineColorFontWidthBuilder
    Origin: Drawings.ZoneOrigin
    VerticalSize: float


class SheetZoneReferenceBuilder(Builder):
    def __init__(self) -> None: ...
    SelectView: Drawings.SelectDraftingView


class SheetTemplateManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.DrawingSheetCollection) -> None: ...
    def Create(self, pathToPartName: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class SheetSectionLineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.SectionLine]:
        ...
    def __init__(self, owner: Drawings.DrawingSheet) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class SheetMarginSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BottomTrimmedMargin: float
    BottomUntrimmedMargin: float
    CreateUntrimmedMargins: bool
    LeftTrimmedMargin: float
    LeftUntrimmedMargin: float
    MarginLineColorFontWidth: LineColorFontWidthBuilder
    RightTrimmedMargin: float
    RightUntrimmedMargin: float
    TopTrimmedMargin: float
    TopUntrimmedMargin: float


class SheetDraftingViewCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DraftingView]:
        ...
    def __init__(self, owner: Drawings.DrawingSheet) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Drawings.DraftingView:
        ...
    def CreateBaseView(self, modelView: ModelingView, drawingReferencePoint: Point3d, viewScale: float, inheritClippingBoundry: bool) -> Drawings.BaseView:
        ...
    def CreateProjectedView(self, parentView: Drawings.DraftingView, drawingReferencePoint: Point3d) -> Drawings.ProjectedView:
        ...
    def CreateProjectedView(self, parentView: Drawings.DraftingView, drawingReferencePoint: Point3d, hingeLine: Direction) -> Drawings.ProjectedView:
        ...
    def CreateProjectedView(self, parentView: Drawings.DraftingView, drawingReferencePoint: Point3d, reverseDirection: bool) -> Drawings.ProjectedView:
        ...
    def DeleteView(self, currentView: Drawings.DraftingView) -> None:
        ...
    def Tag(self) -> Tag: ...



class SheetBorderSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ArrowAngle: float
    ArrowDirection: Drawings.ArrowDirectionType
    ArrowHeadTail: float
    ArrowLength: float
    ArrowStyle: Drawings.ArrowStyleType
    BorderLineWidth: float
    CenteringMarkLength: float
    CenteringMarksColorWidth: LineColorFontWidthBuilder
    CenteringMarksExtension: float
    CenteringMarksHorizontal: Drawings.HorizontalCenteringMarkType
    CenteringMarksVertical: Drawings.VerticalCenteringMarkType
    CreateBorders: bool
    CreateTrimmingMarks: bool
    DisplaySheetSizeInBorder: bool
    DistanceFromInnerBorder: float
    InnerLineCFW: LineColorFontWidthBuilder
    Method: Drawings.Method
    OuterLineCFW: LineColorFontWidthBuilder
    TrimmingMarkColor: NXColor
    TrimmingMarkLength: float
    TrimmingMarkStyle: Drawings.TrimmingMarkStyleType
    TrimmingMarkWidth: float


class ShadingViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    CustomAngleTolerance: float
    CustomEdgeTolerance: float
    CustomFaceTolerance: float
    OverrideHiddenWireframeColor: int
    OverrideVisibleWireframeColor: int
    RenderingStyle: Preferences.ShadingRenderingStyleOption
    ShadedCutFaceColor: int
    ShadingTolerance: Preferences.ShadingToleranceOption
    Shininess: float
    TwoSidedLight: bool


class SettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SaveConfigurationFile(self, saveAsFile: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AnnotationSettings: Drawings.AnnotationSettingsBuilder
    ConversionSettings: Drawings.ConversionProcessSettingsBuilder
    ViewSettings: Drawings.ViewSettingsBuilder


class SelectSectionLine(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Drawings.SectionLine, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Drawings.SectionLine, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.SectionLine, view1: View, point1: Point3d, selection2: Drawings.SectionLine, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.SectionLine, view1: View, point1: Point3d, selection2: Drawings.SectionLine, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Drawings.SectionLine, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Drawings.SectionLine:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Drawings.SectionLine


class SelectRegionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetAssociatedObjects(self, associateObject: typing.List[NXObject]) -> None:
        ...
    SelectedRegion: Drawings.SelectDrawingRegion


class SelectModelViewBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SelectedView: ModelingView


class SelectDrawingViewList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Drawings.DrawingView) -> bool:
        ...
    def Add(self, objects: typing.List[Drawings.DrawingView]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Drawings.DrawingView, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Drawings.DrawingView) -> bool:
        ...
    def Remove(self, object: Drawings.DrawingView, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Drawings.DrawingView, view1: View, point1: Point3d, selection2: Drawings.DrawingView, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Drawings.DrawingView]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Drawings.DrawingView) -> bool:
        ...
    def SetArray(self, objects: typing.List[Drawings.DrawingView]) -> None:
        ...
    def GetArray(self) -> typing.List[Drawings.DrawingView]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Drawings.DrawingView, view1: View, point1: Point3d, selection2: Drawings.DrawingView, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Drawings.DrawingView, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectDrawingView(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Drawings.DrawingView, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Drawings.DrawingView, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.DrawingView, view1: View, point1: Point3d, selection2: Drawings.DrawingView, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.DrawingView, view1: View, point1: Point3d, selection2: Drawings.DrawingView, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Drawings.DrawingView, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Drawings.DrawingView:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Drawings.DrawingView


class SelectDrawingRegion(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Drawings.DrawingRegion, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Drawings.DrawingRegion, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.DrawingRegion, view1: View, point1: Point3d, selection2: Drawings.DrawingRegion, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.DrawingRegion, view1: View, point1: Point3d, selection2: Drawings.DrawingRegion, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Drawings.DrawingRegion, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Drawings.DrawingRegion:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Drawings.DrawingRegion


class SelectDraftingViewList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Drawings.DraftingView) -> bool:
        ...
    def Add(self, objects: typing.List[Drawings.DraftingView]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Drawings.DraftingView, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Drawings.DraftingView) -> bool:
        ...
    def Remove(self, object: Drawings.DraftingView, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Drawings.DraftingView, view1: View, point1: Point3d, selection2: Drawings.DraftingView, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Drawings.DraftingView]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Drawings.DraftingView) -> bool:
        ...
    def SetArray(self, objects: typing.List[Drawings.DraftingView]) -> None:
        ...
    def GetArray(self) -> typing.List[Drawings.DraftingView]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Drawings.DraftingView, view1: View, point1: Point3d, selection2: Drawings.DraftingView, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Drawings.DraftingView, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectDraftingView(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Drawings.DraftingView, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Drawings.DraftingView, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.DraftingView, view1: View, point1: Point3d, selection2: Drawings.DraftingView, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Drawings.DraftingView, view1: View, point1: Point3d, selection2: Drawings.DraftingView, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Drawings.DraftingView, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Drawings.DraftingView:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Drawings.DraftingView


class SectionViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    AssemblyCrossHatching: bool
    Background: bool
    Bendlines: bool
    CrossHatch: bool
    CrosshatchAdjacencyTolarance: float
    DisplaySectionLine: bool
    Foreground: bool
    HiddenLineHatching: bool
    RestrictCrosshatchAngle: bool
    SectionSheetBodies: bool


class SectionViewBuilder(Builder):
    def __init__(self) -> None: ...
    CreateFolded: bool
    HiddenObjects: Drawings.HiddenObjectsBuilder
    NonSectionedObjects: Drawings.HiddenObjectsBuilder
    ParentView: Drawings.ParentViewBuilder
    SecondaryComponents: Drawings.DraftingComponentSelectionBuilder
    SectionLine: Drawings.SpecifySectionLineBuilder
    SectionLineSegments: Drawings.SectionLineSegmentsBuilder
    SectionViewMode: Drawings.SectionViewBuilder.SectionViewModeType
    SectionViewTool: Drawings.SvtBuilder
    SectionViewType: Drawings.SectionViewBuilder.SectionLineType
    ViewOrientation: Drawings.ViewOrientationBuilder
    ViewPlacement: Drawings.ViewPlacementBuilder
    ViewStyle: Drawings.ViewStyleBuilder
    ViewUnfolded: bool


    class SectionViewModeType(enum.Enum):
        Dynamic = 0
        StandAlone = 1
    

    class SectionLineType(enum.Enum):
        SimpleStepped = 0
        Half = 1
        Revolved = 2
        PointToPoint = 3
        PointAndAngle = 4
    

    class SectionCutType(enum.Enum):
        FullPart = 0
        SectionedPart = 1
    

class SectionView(Drawings.DraftingView):
    def __init__(self) -> None: ...


class SectionLineStyleBuilder(Builder):
    def __init__(self) -> None: ...
    def GetColor(self) -> NXColor:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Drawings.ViewSectionLineBuilder.LineColorFontWidth instead.")"""
        ...
    def SetColor(self, color: NXColor) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Drawings.ViewSectionLineBuilder.LineColorFontWidth instead.")"""
        ...
    ArrowLength: float
    ArrowheadAngle: float
    ArrowheadLength: float
    ArrowheadStyle: Drawings.SectionLineStyleBuilder.ArrowheadStyleType
    BorderToArrowDistance: float
    CreateSectionLine: Drawings.SectionLineStyleBuilder.CreateSectionLineType
    DisplayJisrotationLetter: bool
    DisplayLabel: bool
    Font: Drawings.SectionLineStyleBuilder.FontStyle
    LabelLocation: Drawings.SectionLineStyleBuilder.LabelLocationStyle
    Letter: str
    LineLength: float
    Offset: float
    SelectLetter: SelectTaggedObject
    Standard: Drawings.SectionLineStyleBuilder.StandardStyle
    StubLength: float
    UseOffset: bool
    Width: Drawings.SectionLineStyleBuilder.WidthStyle


    class WidthStyle(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        ThicknessOne = 5
        ThicknessTwo = 6
        ThicknessThree = 7
        ThicknessFour = 8
        ThicknessFive = 9
        ThicknessSix = 10
        ThicknessSeven = 11
        ThicknessEight = 12
        ThicknessNine = 13
    

    class StandardStyle(enum.Enum):
        AnsiStandard = 0
        IsoStandard = 1
        Iso128Standard = 2
        JisStandard = 3
        GbStandard = 4
        EskdStandard = 5
    

    class LabelLocationStyle(enum.Enum):
        OnArrow = 0
        OnEnd = 1
    

    class FontStyle(enum.Enum):
        None = 0
        Solid = 1
        Dashed = 2
        Phantom = 3
        Centerline = 4
        Dotted = 5
        LongDashed = 6
        DottedDashed = 7
        Eight = 8
        Nine = 9
        Ten = 10
        Eleven = 11
    

    class CreateSectionLineType(enum.Enum):
        WithView = 0
        WithoutView = 1
    

    class ArrowheadStyleType(enum.Enum):
        Open = 0
        Closed = 1
        Filled = 2
    

class SectionLineSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: Drawings.SectionLine) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ViewCommonViewLabel: Drawings.ViewCommonViewLabelBuilder
    ViewSectionLine: Drawings.ViewSectionLineBuilder


class SectionLineSegmentsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateAfterParentViewMove(self) -> None:
        ...
    RotationPoint: Point
    SectionLineOnlyPlacementOrigin: Point3d
    SegmentLocation: Drawings.SectionLineSegmentPointListBuilder
    SegmentLocationForSecondLeg: Drawings.SectionLineSegmentPointListBuilder
    SingleLeg: bool


class SectionLineSegmentPointListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateSectionLineSegmentPointBuilder(self) -> Drawings.SectionLineSegmentPointBuilder:
        ...
    def AddCutSegment(self, location: Point) -> Drawings.SectionLineSegmentPointBuilder:
        ...
    def AddCutSegment(self, location: Point, referencedCutSegment: Drawings.SectionLineSegmentPointBuilder) -> Drawings.SectionLineSegmentPointBuilder:
        ...
    def Append(self, pointData: Drawings.SectionLineSegmentPointBuilder) -> None:
        ...
    def Insert(self, insertBeforeIndex: int, point: Drawings.SectionLineSegmentPointBuilder) -> None:
        ...
    def Delete(self, point: Drawings.SectionLineSegmentPointBuilder) -> None:
        ...
    def Delete(self, index: int) -> None:
        ...
    def Clear(self) -> None:
        ...
    def GetContents(self) -> typing.List[Drawings.SectionLineSegmentPointBuilder]:
        ...
    def SetContents(self, points: typing.List[Drawings.SectionLineSegmentPointBuilder]) -> None:
        ...
    def FindItem(self, index: int) -> Drawings.SectionLineSegmentPointBuilder:
        ...
    def GetIndex(self, point: Drawings.SectionLineSegmentPointBuilder) -> int:
        ...
    def MoveSegment(self, point: Drawings.SectionLineSegmentPointBuilder, pointspecified: Point) -> None:
        ...
    Length: int


class SectionLineSegmentPointBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Point: Point
    SegmentType: Drawings.SectionLineSegmentPointBuilder.SegmentTypes


    class SegmentTypes(enum.Enum):
        Arrow = 1
        Cut = 2
        Bend = 3
    

class SectionLineSegmentBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Drawings.SectionLineSegmentBuilder]) -> None:
        ...
    def Append(self, object: Drawings.SectionLineSegmentBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Drawings.SectionLineSegmentBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Drawings.SectionLineSegmentBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Drawings.SectionLineSegmentBuilder) -> None:
        ...
    def Erase(self, obj: Drawings.SectionLineSegmentBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Drawings.SectionLineSegmentBuilder]:
        ...
    def SetContents(self, objects: typing.List[Drawings.SectionLineSegmentBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Drawings.SectionLineSegmentBuilder, object2: Drawings.SectionLineSegmentBuilder) -> None:
        ...
    def Insert(self, location: int, object: Drawings.SectionLineSegmentBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SectionLineSegmentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Angle: Expression
    Point: Point
    Type: Drawings.SectionLineSegmentBuilder.Types


    class Types(enum.Enum):
        Angle = 0
        Cut = 1
        Bend = 2
    

class SectionLineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.SectionLine]:
        ...
    def __init__(self, owner: DraftingManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSectionLineBuilder(self, sectionLine: Drawings.SectionLine) -> Drawings.SectionLineBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use Drawings.SectionViewBuilder.SectionLineSegments instead.")"""
        ...
    def CreateSectionLineSegmentBuilder(self) -> Drawings.SectionLineSegmentBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use Drawings.SectionViewBuilder.SectionLineSegments instead.")"""
        ...
    def CreateSectionLineStyleBuilder(self, sectionline: Drawings.SectionLine) -> Drawings.SectionLineStyleBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Drawings.ViewSectionLineBuilder instead.")"""
        ...
    def CreateSketchSectionLineBuilder(self, sectionLine: Drawings.SectionLine) -> Drawings.SketchSectionLineBuilder:
        ...
    def GenerateSectionLineLabelAttribute(self, note: Annotations.BaseNote) -> str:
        ...
    def Tag(self) -> Tag: ...



class SectionLineBuilder(Builder):
    def __init__(self) -> None: ...
    ArrowDirection: Direction
    CutDirection: Direction
    Half: Drawings.HalfSectionLineBuilder
    HalfPictorial: Drawings.HalfSectionLineBuilder
    HingeDirection: Direction
    Oriented: Drawings.OrientedSectionLineBuilder
    ParentView: Drawings.ParentViewBuilder
    Pictorial: Drawings.SteppedSectionLineBuilder
    PointAndAngle: Drawings.PointAndAngleSectionLineBuilder
    PointToPoint: Drawings.PointToPointSectionLineBuilder
    Revolved: Drawings.RevolvedSectionLineBuilder
    SimpleOrStepped: Drawings.SteppedSectionLineBuilder
    Style: Drawings.SectionLineStyleBuilder
    Type: Drawings.SectionLineBuilder.Types


    class Types(enum.Enum):
        SimpleOrStepped = 0
        Half = 1
        Revolved = 2
        PointToPoint = 3
        PointAndAngle = 4
        Pictorial = 5
        HalfPictorial = 6
        Oriented = 7
    

class SectionLine(DisplayableObject):
    def __init__(self) -> None: ...
    IsRetained: bool


class SectionInViewBuilder(Builder):
    def __init__(self) -> None: ...
    EditObjects: Drawings.HiddenObjectsBuilder
    EditType: Drawings.SectionInViewBuilder.EditSxtype
    Views: Drawings.SelectDraftingViewList


    class EditSxtype(enum.Enum):
        MakeNonSectioned = 0
        MakeSectioned = 1
        RemoveViewSpecific = 2
    

class SecondaryGeometryInViewsBuilder(Builder):
    def __init__(self) -> None: ...
    Components: Drawings.DraftingComponentSelectionBuilder
    Views: Drawings.SelectDraftingViewList


class ScaleValueFormatTypes(enum.Enum):
    Ratio = 0
    CommonFraction = 1
    SingleLineFraction = 2
    Nx = 3


class ScalePositionTypes(enum.Enum):
    Above = 0
    Below = 1
    Before = 2
    After = 3


class RotationSymbolTypes(enum.Enum):
    None = 0
    Full = 1
    Right = 2
    Left = 3


class RevolvedSectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use Drawings.SectionViewBuilder.SectionViewType instead..")"""
        ...
    EndLocation1: Point
    EndLocation2: Point
    Leg1: Drawings.SectionLineSegmentBuilderList
    Leg2: Drawings.SectionLineSegmentBuilderList
    RotationPoint: Point
    SingleLeg: bool


class RevolvedSectionLine(Drawings.SectionLine):
    def __init__(self) -> None: ...


class ReportBuilder(Builder):
    def __init__(self) -> None: ...


class RenderSet(NXObject):
    def __init__(self) -> None: ...


class RemoveObjectsBuilder(Builder):
    def __init__(self) -> None: ...
    def SetRegion(self, region: Drawings.DrawingRegion) -> None:
        ...
    Selection: SelectNXObjectList


class RefineDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryPoint1: Point
    BoundaryPoint2: Point
    View: Drawings.SelectDraftingView


class ReferenceShowTypes(enum.Enum):
    SheetandZone = 0
    Sheet = 1
    Zone = 2


class ProjectedViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...



class ProjectedViewOrientationBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Restore(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    NormalDirection: Xform
    XDirection: Direction


class ProjectedViewBuilder(Builder):
    def __init__(self) -> None: ...
    HiddenObjects: Drawings.HiddenObjectsBuilder
    NonSectionedObjects: Drawings.HiddenObjectsBuilder
    Parent: Drawings.ParentViewBuilder
    Placement: Drawings.ViewPlacementBuilder
    SecondaryComponents: Drawings.DraftingComponentSelectionBuilder
    Style: Drawings.ViewStyleBuilder


class ProjectedView(Drawings.DraftingView):
    def __init__(self) -> None: ...


class PointToPointSectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use Drawings.SectionViewBuilder.SectionViewType instead..")"""
        ...
    EndLocation1: Point
    EndLocation2: Point
    Leg1: Drawings.SectionLineSegmentBuilderList


class PointToPointSectionLine(Drawings.BasePointToPointSectionLine):
    def __init__(self) -> None: ...


class PointAndAngleSectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  This API is not supported yet and should not be used..")"""
        ...
    EndLocation1: Point
    EndLocation2: Point
    Leg1: Drawings.SectionLineSegmentBuilderList


class PointAndAngleSectionLine(Drawings.SectionLine):
    def __init__(self) -> None: ...


class PictorialSectionLine(Drawings.SteppedSectionLine):
    def __init__(self) -> None: ...


class PerspectiveViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    BackClipping: bool
    BackClippingDistance: float
    FrontClipping: bool
    FrontClippingDistance: float
    Perspective: bool
    PerspectiveDistance: float


class ParentViewBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    View: Drawings.SelectDraftingView


class OvtBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AssociativeOrientation: bool
    NormalDirection: Direction
    XDirection: Direction


class OrientedSectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  This API is not supported yet and should not be used..")"""
        ...
    CutLocation3D: Point
    EndLocation1: Point
    EndLocation2: Point


class OrientedSectionLine(Drawings.SectionLine):
    def __init__(self) -> None: ...


class OrientationViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def ReverseRotationVector(self) -> None:
        ...
    def ReverseHingeLine(self) -> None:
        ...
    def Restore(self) -> None:
        ...
    def OrientView(self, matrix: Matrix3x3) -> None:
        ...
    def Tag(self) -> Tag: ...

    HingeLine: Direction
    RotationPlane: Xform
    RotationXDirection: Direction


class OrderManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Layout2d.ComponentCollection) -> None: ...
    def GetAvailableOrdersNames(self, parentObject: Sketch, ordersNames: str) -> None:
        ...
    def IsSystemOrder(self, parentObject: Sketch, orderName: str) -> bool:
        ...
    def GetCurrentOrderName(self, parentObject: Sketch) -> str:
        ...
    def ApplyOrder(self, parentObject: Sketch, orderName: str) -> None:
        ...
    def CreateNewOrder(self, parentObject: Sketch, newOrderName: str, objectsInOrder: typing.List[Layout2d.Component]) -> None:
        ...
    def RenameOrder(self, parentObject: Sketch, orderName: str, newOrderName: str) -> None:
        ...
    def DeleteOrder(self, parentObject: Sketch, newOrderName: str) -> None:
        ...
    def Reorder(self, parentObject: Sketch, objectsInOrder: typing.List[Layout2d.Component]) -> None:
        ...
    def Tag(self) -> Tag: ...



class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MultipleViewPlacementBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AssociativeAlignment: bool
    OptionType: Drawings.MultipleViewPlacementBuilder.Option
    ViewPlacementCenter: Drawings.ViewPlacementBuilder
    ViewPlacementFirstCorner: Drawings.ViewPlacementBuilder
    ViewPlacementSecondCorner: Drawings.ViewPlacementBuilder


    class Option(enum.Enum):
        Center = 0
        Corners = 1
    

class Method(enum.Enum):
    None = 0
    Standard = 1
    Custom = 2


class MarkAsTemplateBuilder(Builder):
    def __init__(self) -> None: ...
    ActionType: Drawings.MarkAsTemplateBuilder.ActionTypeEnum
    Description: str
    ItemType: Drawings.MarkAsTemplateBuilder.ItemTypeEnum
    ItemTypeString: str
    PaxFileName: str
    PresentationName: str
    RelationType: Drawings.MarkAsTemplateBuilder.RelationTypeEnum
    TemplateType: Drawings.MarkAsTemplateBuilder.TemplateTypeEnum


    class TemplateTypeEnum(enum.Enum):
        Sheet = 0
        ReferenceExistingPart = 1
        Standalone = 2
    

    class RelationTypeEnum(enum.Enum):
        Master = 0
        Specification = 1
        Manifestation = 2
    

    class ItemTypeEnum(enum.Enum):
        Any = 0
        NXPart = 1
        NXDrawing = 2
    

    class ActionTypeEnum(enum.Enum):
        TemplateOnly = 0
        TemplateAndPax = 1
    

class LetterFormatTypes(enum.Enum):
    A = 0
    AA = 1
    AA1 = 2


class LabelPositionTypes(enum.Enum):
    Above = 0
    Below = 1


class InheritPmiViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def SetInheritGdt(self, gdtOption: Preferences.GdtOption) -> None:
        ...
    def SetCrosshatchPmiLwsv(self, crosshatch: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    CrosshatchPmiLwsv: bool
    InheritPmiMode: Preferences.PmiOption
    InheritPmiToDrawing: bool
    InheritPmiTypeMask: int
    PmiDimensionFromRevolved: bool


class HorizontalCenteringMarkType(enum.Enum):
    None = 0
    LeftArrow = 1
    RightArrow = 2
    LeftandRightArrow = 3
    LeftandRightLine = 4


class HingeLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Associative: bool
    ReverseDirection: bool
    SpecifyVector: Direction
    VectorOption: Drawings.HingeLineBuilder.Hingeline


    class Hingeline(enum.Enum):
        Inferred = 0
        Defined = 1
    

class HiddenObjectsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Objects: SelectNXObjectList


class HiddenLinesViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def Tag(self) -> Tag: ...

    EdgesHiddenByEdges: bool
    Hiddenline: bool
    HiddenlineColor: int
    HiddenlineFont: Preferences.Font
    HiddenlineWidth: Preferences.Width
    IncludeModelCurves: bool
    InterferingSolids: bool
    InterferingSolidsOption: Preferences.HiddenLineInterferingSolidsOption
    ReferenceEdgesOnly: bool
    SelfHidden: bool
    SmallFeature: Preferences.HiddenLineSmallFeatureOption
    SmallFeaturesTolerance: float


class HalfSectionLineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use Drawings.SectionViewBuilder.SectionViewType instead..")"""
        ...
    BendLocation: Point
    CutLocation: Point
    EndLocation1: Point


class HalfSectionLine(Drawings.BaseHalfSectionLine):
    def __init__(self) -> None: ...


class HalfPictorialSectionLine(Drawings.HalfSectionLine):
    def __init__(self) -> None: ...


class GeneralWorkFlowBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CreateDraftingComponent: bool
    GridSettings: Drawings.GeneralWorkFlowBuilder.GridSettingsType
    ModelBasedAlwaysStart: Drawings.GeneralWorkFlowBuilder.ModelBasedAlwaysStartType
    ModelBasedInsertSheet: bool
    ModelBasedProjectedView: bool
    SettingsOrigination: Drawings.GeneralWorkFlowBuilder.SettingsOrientationType
    StandAloneInsertSheet: bool
    StandAloneProjectToView: bool
    StandAloneProjectedView: bool
    StandAloneViewCreation: bool


    class SettingsOrientationType(enum.Enum):
        DrawingTemplate = 0
        DrawingStandard = 1
    

    class ModelBasedAlwaysStartType(enum.Enum):
        ViewCreationWizard = 0
        BaseViewCommand = 1
        NoViewCommands = 2
    

    class GridSettingsType(enum.Enum):
        Drafting = 0
        Sketch = 1
        SheetZone = 2
    

class GeneralViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def SetCenterlines(self, centerlines: bool) -> None:
        ...
    def SetFramebarHorizontal(self, framebarHorizontal: bool) -> None:
        ...
    def SetFramebarVertical(self, framebarVertical: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    Angle: float
    AngleDecimalPointFormat: Preferences.DecimalPointCharacter
    AngleFormat: Preferences.AngleFormat
    AnglePrecision: int
    AssociativeAngle: Scalar
    AutomaticAnchorPoint: bool
    AutomaticUpdate: bool
    BoundaryStatus: bool
    DisplayId: Preferences.GeneralDisplayIdOption
    ExpressionForScale: Expression
    ExtractedEdges: Preferences.GeneralExtractedEdgesOption
    LegacyView: bool
    LightweightView: bool
    LockmethodView: Preferences.GeneralViewLockmethodOption
    Reference: bool
    RenderCount: int
    Scale: float
    ScaleLabel: bool
    ShowAngleLeadingZeros: bool
    ShowAngleTrailingZeros: bool
    Silhouettes: bool
    SnapshotView: bool
    Tolerance: float
    UvGrid: bool
    ViewLabel: bool
    ViewQuality: Preferences.GeneralViewQualityOption
    ViewRepresentation: Preferences.GeneralViewRepresentationOption
    WireframeColorSource: Preferences.GeneralWireframeColorSourceOption


class FontEnum(enum.Enum):
    Blockfont = 0


class FlatPatternViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def GetPropertiesObject(self) -> SheetMetal.FlatPatternSettings:
        ...
    def Commit(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class FlatPatternObject(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetFlatSolidObject(self) -> CartesianCoordinateSystem:
        ...
    def GetOrigin(self) -> Point3d:
        ...
    def GetDirections(self, xDirection: Vector3d, yDirection: Vector3d) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class EditViewSettingsBuilder(Drafting.BaseEditSettingsBuilder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: Drawings.DraftingView) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    ViewDetailLabel: Drawings.ViewDetailLabelBuilder
    ViewLabel: Drawings.ViewLabelBuilder
    ViewProjectedLabel: Drawings.ViewProjectedLabelBuilder
    ViewSectionLabel: Drawings.ViewSectionLabelBuilder
    ViewStyle: Drawings.ViewStyleBuilder


class EditViewLabelSettingsBuilder(Drafting.BaseEditSettingsBuilder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    AnnotationStyle: Annotations.StyleBuilder
    ViewCommonViewLabel: Drawings.ViewCommonViewLabelBuilder
    ViewDetailLabel: Drawings.ViewDetailLabelBuilder
    ViewLabel: Drawings.ViewLabelBuilder
    ViewProjectedLabel: Drawings.ViewProjectedLabelBuilder
    ViewSectionLabel: Drawings.ViewSectionLabelBuilder


class EditSectionLineSettingsBuilder(Drafting.BaseEditSettingsBuilder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: Drawings.SectionLine) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    ViewCommonViewLabel: Drawings.ViewCommonViewLabelBuilder
    ViewSectionLine: Drawings.ViewSectionLineBuilder


class DrawingViewBuilder(Builder):
    def __init__(self) -> None: ...
    CenterCoordinate: Drawings.ViewCenterCoordinateBuilder
    MultipleViewPlacement: Drawings.MultipleViewPlacementBuilder
    Scale: Drawings.ViewScaleBuilder
    TwodOrientation: Drawings.View2dOrientBuilder
    ViewBoundary: Drawings.ViewBoundaryBuilder
    ViewPlacement: Drawings.ViewPlacementBuilder
    ViewStyle: Drawings.ViewStyleBuilder


class DrawingView(Drawings.DraftingView):
    def __init__(self) -> None: ...


class DrawingsPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    SecondaryComponent: Drawings.DrawingsPropertiesBuilder.SecondaryComponentOptions
    SelectedObjects: Assemblies.SelectComponentList


    class SecondaryComponentOptions(enum.Enum):
        No = 0
        Yes = 1
        Mixed = 2
    

class DrawingSheetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DrawingSheet]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def InsertSheet(self, drawingName: str, drawingUnits: Drawings.DrawingSheet.Unit, width: float, height: float, numerator: float, denominator: float, projectionAngle: Drawings.DrawingSheet.ProjectionAngleType) -> Drawings.DrawingSheet:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Drawings.DraftingDrawingSheetCollection.InsertSheet instead.")"""
        ...
    def InsertSheet(self, drawingName: str, sheetSize: Drawings.DrawingSheet.StandardSheetSize, numerator: float, denominator: float, projectionAngle: Drawings.DrawingSheet.ProjectionAngleType) -> Drawings.DrawingSheet:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Drawings.DraftingDrawingSheetCollection.InsertSheet instead.")"""
        ...
    def FindObject(self, journalIdentifier: str) -> Drawings.DrawingSheet:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Drawings.DraftingDrawingSheetCollection.FindObject instead.")"""
        ...
    def DrawingSheetBuilder(self, sheet: Drawings.DrawingSheet) -> Drawings.DrawingSheetBuilder:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Drawings.DraftingDrawingSheetCollection.CreateDraftingDrawingSheetBuilder instead.")"""
        ...
    def RefreshCurrentSheet(self) -> None:
        ...
    def PasteDrawingSheets(self, dwgSheets: typing.List[Drawings.DrawingSheet], newPastedDwgSheets: typing.List[Drawings.DrawingSheet]) -> None:
        ...
    def Tag(self) -> Tag: ...

    SheetTemplates: Drawings.SheetTemplateManager
    CurrentDrawingSheet: Drawings.DrawingSheet


class DrawingSheetBuilder(Builder):
    def __init__(self) -> None: ...
    AutoStartBaseView: bool
    AutoStartViewCreation: bool
    BaseordrawingView: Drawings.DrawingSheetBuilder.SheetBaseordrawingView
    EnglishSheetTemplateLocation: str
    Height: float
    Length: float
    MetricSheetTemplateLocation: str
    Name: str
    Number: str
    Option: Drawings.DrawingSheetBuilder.SheetOption
    ProjectionAngle: Drawings.DrawingSheetBuilder.SheetProjectionAngle
    Revision: str
    ScaleDenominator: float
    ScaleNumerator: float
    SecondaryNumber: str
    StandardEnglishScale: Drawings.DrawingSheetBuilder.SheetStandardEnglishScale
    StandardMetricScale: Drawings.DrawingSheetBuilder.SheetStandardMetricScale
    Units: Drawings.DrawingSheetBuilder.SheetUnits


    class SheetUnits(enum.Enum):
        Metric = 0
        English = 1
    

    class SheetStandardMetricScale(enum.Enum):
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
    

    class SheetStandardEnglishScale(enum.Enum):
        S81 = 0
        S41 = 1
        S21 = 2
        S11 = 3
        S12 = 4
        S14 = 5
        S18 = 6
        Custom = 7
    

    class SheetProjectionAngle(enum.Enum):
        First = 0
        Third = 1
    

    class SheetOption(enum.Enum):
        UseTemplate = 0
        StandardSize = 1
        CustomSize = 2
    

    class SheetMode(enum.Enum):
        Create = 0
        Edit = 1
    

    class SheetBaseordrawingView(enum.Enum):
        Base = 0
        Drawing = 1
    

class DrawingSheet(NXObject):
    def __init__(self) -> None: ...
    def Open(self) -> None:
        ...
    def GetDraftingViews(self) -> typing.List[Drawings.DraftingView]:
        ...
    def GetScale(self, numerator: float, denominator: float) -> None:
        ...
    def SetParameters(self, height: float, length: float, numerator: float, denominator: float, units: Drawings.DrawingSheet.Unit, projectionAngle: Drawings.DrawingSheet.ProjectionAngleType, associatedViews: typing.List[Drawings.DraftingView]) -> None:
        ...
    def ActivateForSketching(self) -> None:
        ...
    def ResetActiveForSketching(self) -> None:
        ...
    def GetZoneReference(self, viewTag: Drawings.DraftingView) -> str:
        ...
    def GetSheetZoneReference(self, viewTag: Drawings.DraftingView) -> str:
        ...
    def GetDraftingSketches(self) -> typing.List[Sketch]:
        ...
    SheetDraftingViews: Drawings.SheetDraftingViewCollection
    SheetSectionLines: Drawings.SheetSectionLineCollection
    BordersAndZones: Drawings.BordersAndZones
    Height: float
    IsActiveForSketching: bool
    IsOutOfDate: bool
    Length: float
    ProjectionAngle: Drawings.DrawingSheet.ProjectionAngleType
    Units: Drawings.DrawingSheet.Unit
    View: View


    class Unit(enum.Enum):
        Inches = 1
        Millimeters = 2
    

    class StandardSheetSize(enum.Enum):
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        F = 5
        H = 6
        J = 7
        A0 = 8
        A1 = 9
        A2 = 10
        A3 = 11
        A4 = 12
    

    class ProjectionAngleType(enum.Enum):
        FirstAngle = 1
        ThirdAngle = 2
    

class DrawingRegionRulesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetRules(self) -> str:
        ...
    def SetRules(self, rules: str) -> None:
        ...
    def RemoveRules(self, rules: str) -> None:
        ...
    def Validate(self) -> bool:
        ...


class DrawingRegionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DrawingRegion]:
        ...
    def __init__(self, owner: Drafting.AutomationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDrawingRegionBuilder(self, object: Drawings.DrawingRegion) -> Drawings.DrawingRegionBuilder:
        ...
    def CreateAddObjectsToRegionBuilder(self) -> Drawings.AddObjectsToRegionBuilder:
        ...
    def CreateSelectRegionBuilder(self) -> Drawings.SelectRegionBuilder:
        ...
    def CreateRemoveObjectsBuilder(self) -> Drawings.RemoveObjectsBuilder:
        ...
    def FindObject(self, name: str) -> Drawings.DrawingRegion:
        ...
    def Tag(self) -> Tag: ...



class DrawingRegionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetNextLinkedRegion(self, nextLinkedRegion: Drawings.DrawingRegion) -> None:
        ...
    DrawingRegionRulesBuilder: Drawings.DrawingRegionRulesBuilder
    Gap: float
    GrowthDirection: Drawings.DrawingRegionBuilder.RegionGrowthDirection
    Height: Expression
    HorizontalGrowthDirection: Drawings.DrawingRegionBuilder.RegionHorizontalGrowthDirection
    Length: Expression
    MoveContent: Drawings.DrawingRegionBuilder.ContentToMove
    Name: str
    ObjectType: Drawings.DrawingRegionBuilder.RegionDraftingObjectType
    Origin: Point
    Priority: int
    SpecifyContinuation: Drawings.DrawingRegionBuilder.RegionContinuation
    VerticalGrowthDirection: Drawings.DrawingRegionBuilder.RegionVerticalGrowthDirection


    class RegionVerticalGrowthDirection(enum.Enum):
        Up = 0
        Down = 1
    

    class RegionHorizontalGrowthDirection(enum.Enum):
        Left = 0
        Right = 1
    

    class RegionGrowthDirection(enum.Enum):
        RightfromTopLeft = 0
        RightfromBottomLeft = 1
        LeftfromTopRight = 2
        LeftfromBottomRight = 3
        DownfromTopLeft = 4
        DownfromTopRight = 5
        UpfromBottomLeft = 6
        UpfromBottomRight = 7
        None = 8
    

    class RegionDraftingObjectType(enum.Enum):
        View = 0
        Table = 1
        Annotation = 2
        Symbol = 3
        Blank = 4
        None = 5
    

    class RegionContinuation(enum.Enum):
        None = 0
        NewSheet = 1
        NextRegion = 2
        NewSheetRight = 3
        NewSheetLeft = 4
        NewSheetUp = 5
        NewSheetDown = 6
    

    class ContentToMove(enum.Enum):
        All = 0
        OnlyOverlapping = 1
    

class DrawingRegion(DisplayableObject):
    def __init__(self) -> None: ...


class DrawingFormatSheetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    InitialSecondarySheetNumber: str
    InitialSheetNumber: str
    SecondaryNumberDelimiter: str


class DrawingCompareSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    BaselineForComparison: Drawings.DrawingCompareSettingsBuilder.ComparisonBaseline
    CenterlineCompare: bool
    Color: NXColor
    CompareTolerance: float
    CrosshatchAreaFillsCompare: bool
    DatumFeatureSymbolCompare: bool
    DatumFeatureSymbolLeaderTerminatorCompare: bool
    DatumFeatureSymbolOriginCompare: bool
    DatumFeatureSymbolRetainedStatusCompare: bool
    DatumFeatureSymbolTextCompare: bool
    DatumTargetCompare: bool
    DatumTargetLeaderTerminatorCompare: bool
    DatumTargetOriginCompare: bool
    DatumTargetRetainedStatusCompare: bool
    DatumTargetTextCompare: bool
    DimCompare: bool
    DimOriginCompare: bool
    DimRetainedStatusCompare: bool
    DimSizeCompare: bool
    DisplayChangeSymbol: bool
    FcfCompare: bool
    FcfLeaderTerminatorCompare: bool
    FcfOriginCompare: bool
    FcfRetainedStatusCompare: bool
    FcfTextCompare: bool
    NoteCompare: bool
    NoteLeaderTerminatorCompare: bool
    NoteOriginCompare: bool
    NoteRetainedStatusCompare: bool
    NoteTextCompare: bool
    PartListCompare: bool
    RestartNumbers: bool
    SheetCompare: bool
    SymbolCompare: bool
    SymbolFont: Drawings.DrawingCompareSettingsBuilder.FontType
    SymbolLeaderTerminatorCompare: bool
    SymbolOriginCompare: bool
    SymbolRetainedStatusCompare: bool
    SymbolSize: float
    SymbolTextCompare: bool
    SymbolType: Drawings.DrawingCompareSettingsBuilder.ChangeSymbolType
    SymbolWidth: Drawings.DrawingCompareSettingsBuilder.WidthType
    TableCompare: bool
    ViewCompare: bool


    class WidthType(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class FontType(enum.Enum):
        Solid = 0
        Dashed = 1
        Phantom = 2
        Centerline = 3
        Dotted = 4
        LongDash = 5
        DottedDash = 6
        Eight = 10
        Nine = 11
        Ten = 12
        Eleven = 13
    

    class ComparisonBaseline(enum.Enum):
        Snapshot = 0
        TrackedChanges = 1
    

    class ChangeSymbolType(enum.Enum):
        Circle = 0
        TriangleUp = 1
        TriangleDown = 2
        Square = 3
        Hexagon = 4
    

class DraftingViewCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DraftingView]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def UpdateViews(self, updateOption: Drawings.DraftingViewCollection.ViewUpdateOption) -> None:
        ...
    def UpdateViews(self, updateOption: Drawings.DraftingViewCollection.ViewUpdateOption, drawing: Drawings.DrawingSheet) -> None:
        ...
    def UpdateViews(self, views: typing.List[Drawings.DraftingView]) -> None:
        ...
    def SuppressViewBreaks(self, view: Drawings.DraftingView) -> None:
        ...
    def RestoreViewBreaks(self, view: Drawings.DraftingView) -> None:
        ...
    def UpdateViewBreaks(self, view: Drawings.DraftingView) -> None:
        ...
    def PasteViews(self, drawing: Drawings.DrawingSheet, views: typing.List[Drawings.DraftingView], detailOption: Drawings.DraftingViewCollection.ViewCopyDetailOption, annotOption: Drawings.DraftingViewCollection.ViewCopyAnnotOption, newViews: typing.List[Drawings.DraftingView]) -> None:
        ...
    def MoveViewsToDrawing(self, views: typing.List[Drawings.DraftingView], drawing: Drawings.DrawingSheet) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> Drawings.DraftingView:
        ...
    def GetParentOfView(self, view: View) -> ModelingView:
        ...
    def DeleteViewsInOriginalPart(self, views: typing.List[Drawings.DraftingView]) -> None:
        ...
    def CreateUpdateViewsBuilder(self) -> Drawings.UpdateViewsBuilder:
        ...
    def CreateBaseViewBuilder(self, view: Drawings.BaseView) -> Drawings.BaseViewBuilder:
        ...
    def CreateProjectedViewBuilder(self, view: Drawings.ProjectedView) -> Drawings.ProjectedViewBuilder:
        ...
    def CreateSectionViewBuilder(self, sectionViewOrSectionLine: NXObject) -> Drawings.SectionViewBuilder:
        ...
    def CreateSectionInViewBuilder(self) -> Drawings.SectionInViewBuilder:
        ...
    def CreateDrawingViewBuilder(self, drawingview: Drawings.DrawingView) -> Drawings.DrawingViewBuilder:
        ...
    def CreateDetailViewBuilder(self, view: Drawings.DetailView) -> Drawings.DetailViewBuilder:
        ...
    def CreateCopyTo3dBuilder(self) -> Drawings.ViewCopyTo3dBuilder:
        ...
    def CreateStandardViewsBuilder(self) -> Drawings.StandardViewsBuilder:
        ...
    def CreateViewProjectionBuilder(self) -> Drawings.ViewProjectionBuilder:
        ...
    def CreateBrokenViewBuilder(self, viewbreak: Drawings.ViewBreak) -> Drawings.BrokenViewBuilder:
        ...
    def ConvertLegacyViewsToLightweight(self, views: typing.List[Drawings.DraftingView]) -> None:
        ...
    def CreateRefineDisplayBuilder(self) -> Drawings.RefineDisplayBuilder:
        ...
    def CreateAddRemoveBoxViewBuilder(self, activeView: Drawings.DraftingView) -> Drawings.AddRemoveBoxViewBuilder:
        ...
    def CreateViewCreationWizardBuilder(self) -> Drawings.ViewCreationWizardBuilder:
        ...
    def CreateShipbuildingLineBuilder(self) -> Drawings.ViewStyleShipbuildingLinesBuilder:
        ...
    def CreateCustomViewSettingsBuilder(self) -> Drawings.CustomViewSettingsBuilder:
        ...
    def CreateSecondaryGeometryInViewsBuilder(self) -> Drawings.SecondaryGeometryInViewsBuilder:
        ...
    def UpdateSheetsAndViews(self, inputViews: typing.List[NXObject]) -> None:
        ...
    def Tag(self) -> Tag: ...



    class ViewUpdateOption(enum.Enum):
        All = 0
        OutOfDate = 1
        OutOfDateAutomatic = 2
    

    class ViewCopyDetailOption(enum.Enum):
        DetailView = 0
        DuplicateView = 1
        ModelView = 2
    

    class ViewCopyAnnotOption(enum.Enum):
        CopyAnnotation = 0
        DontCopyAnnotation = 1
    

class DraftingView(View):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...
    def GetDrawingReferencePoint(self) -> Point3d:
        ...
    def SetDrawingReferencePoint(self, drawingReferencePoint: Point3d) -> None:
        ...
    def MoveView(self, drawingReferencePoint: Point3d) -> None:
        ...
    def HideComponents(self, components: typing.List[NXObject]) -> None:
        ...
    def ShowComponents(self, components: typing.List[NXObject]) -> None:
        ...
    def ActivateForSketching(self) -> None:
        ...
    def Commit(self) -> None:
        ...
    def GetToolMarkers(self, markers: typing.List[Drawings.FlatPatternObject]) -> None:
        ...
    def RestoreViewBorder(self) -> None:
        ...
    def CheckForInvalidParentModelView(self) -> None:
        ...
    def GetBrokenViewMaster(self) -> Drawings.DraftingView:
        ...
    def GetBrokenViewDecoration(self) -> Drawings.DraftingView:
        ...
    def GetBrokenViewInternalViews(self, views: typing.List[Drawings.DraftingView]) -> None:
        ...
    def HideViewBorder(self) -> None:
        ...
    def ShowViewBorder(self) -> None:
        ...
    def SetDeleteSectionLine(self, deleteSectionLine: bool) -> None:
        ...
    def UpdateAutomaticViewBound(self) -> None:
        ...
    def UpdateAutomaticViewBound(self, updateDependent: bool) -> None:
        ...
    def GetDraftingSketches(self) -> typing.List[Sketch]:
        ...
    Style: Drawings.ViewStyle
    ViewBreaks: Drawings.ViewBreakCollection
    DraftingBodies: Drawings.DraftingBodyCollection
    IsActiveForSketching: bool
    IsBroken: bool
    IsDecoration: bool
    IsOutOfDate: bool
    IsSlave: bool


class DraftingPointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DraftingPoint]:
        ...
    def __init__(self, owner: Drawings.DraftingBody) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Drawings.DraftingPoint:
        ...
    def Tag(self) -> Tag: ...



class DraftingPoint(Point):
    def __init__(self) -> None: ...
    def GetDraftingPointInfo(self) -> Drawings.DraftingCurveInfo:
        ...


class DraftingDrawingSheetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DraftingDrawingSheet]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Drawings.DraftingDrawingSheet:
        ...
    def CreateDraftingDrawingSheetBuilder(self, draftingDrawingSheet: Drawings.DraftingDrawingSheet) -> Drawings.DraftingDrawingSheetBuilder:
        ...
    def InsertSheet(self, drawingName: str, drawingUnits: Drawings.DrawingSheet.Unit, width: float, height: float, numerator: float, denominator: float, projectionAngle: Drawings.DrawingSheet.ProjectionAngleType) -> Drawings.DraftingDrawingSheet:
        ...
    def InsertSheet(self, drawingName: str, sheetSize: Drawings.DrawingSheet.StandardSheetSize, numerator: float, denominator: float, projectionAngle: Drawings.DrawingSheet.ProjectionAngleType) -> Drawings.DraftingDrawingSheet:
        ...
    def Tag(self) -> Tag: ...

    CurrentDrawingSheet: Drawings.DraftingDrawingSheet


class DraftingDrawingSheetBuilder(Drawings.DrawingSheetBuilder):
    def __init__(self) -> None: ...


class DraftingDrawingSheet(Drawings.DrawingSheet):
    def __init__(self) -> None: ...


class DraftingCurveInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetParents(self) -> typing.List[NXObject]:
        ...
    CurveType: Drawings.DraftingCurveInfo.DraftingCurveType


    class DraftingCurveType(enum.Enum):
        NonDraftingCurve = -1
        ExtractedEdge = 0
        ExtractedModelCurve = 1
        SilhouetteCurve = 2
        ThreadSilhouetteCurve = 3
        SectionEdge = 4
        ThreadSectionEdge = 5
        VICurve = 6
        UVHatchCurve = 7
        TracelineCurve = 8
        SimplifiedCurve = 9
        InterferenceCurve = 10
        ExtractedPoint = 11
    

class DraftingCurveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DraftingCurve]:
        ...
    def __init__(self, owner: Drawings.DraftingBody) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Drawings.DraftingCurve:
        ...
    def Tag(self) -> Tag: ...



class DraftingCurve(DisplayableObject):
    def __init__(self) -> None: ...
    def GetDraftingCurveInfo(self) -> Drawings.DraftingCurveInfo:
        ...
    def IsDraftingCurve(self) -> bool:
        ...
    def GetLength(self) -> float:
        ...
    def GetLocations(self) -> typing.List[GeometricUtilities.CurveLocation]:
        ...
    IsReference: bool


class DraftingComponentSelectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def ResetListToGlobal(self) -> None:
        ...
    def InitializeListFromObject(self, inputObject: NXObject) -> None:
        ...
    def ClearSecondaryComponentList(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ObjectType: Drawings.DraftingComponentSelectionBuilder.Geometry
    Objects: SelectNXObjectList
    Part: Part
    PartForKF: Part


    class Geometry(enum.Enum):
        PrimaryGeometry = 0
        SecondaryGeometry = 1
    

class DraftingBodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.DraftingBody]:
        ...
    def __init__(self, owner: Drawings.DraftingView) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Drawings.DraftingBody:
        ...
    def Tag(self) -> Tag: ...



class DraftingBody(DisplayableObject):
    def __init__(self) -> None: ...
    DraftingCurves: Drawings.DraftingCurveCollection
    DraftingPoints: Drawings.DraftingPointCollection


class DetailViewBuilder(Builder):
    def __init__(self) -> None: ...
    Associative: bool
    BoundaryPoint1: Point
    BoundaryPoint2: Point
    HiddenObjects: Drawings.HiddenObjectsBuilder
    LabelOnParent: Drawings.DetailViewBuilder.LabelOnParentType
    NonSectionedObjects: Drawings.HiddenObjectsBuilder
    Origin: Drawings.ViewPlacementBuilder
    Parent: Drawings.ParentViewBuilder
    Scale: Drawings.ViewScaleBuilder
    SecondaryComponents: Drawings.DraftingComponentSelectionBuilder
    Style: Drawings.ViewStyleBuilder
    Type: Drawings.DetailViewBuilder.Types


    class Types(enum.Enum):
        Undefined = -1
        Circular = 0
        RectangleByCorners = 1
        RectangleByCenterAndCorner = 2
        Custom = 3
    

    class LabelOnParentType(enum.Enum):
        None = 0
        Circle = 1
        Note = 2
        Label = 3
        Embedded = 4
        Boundary = 5
        LabelOnBoundary = 6
    

class DetailView(Drawings.DraftingView):
    def __init__(self) -> None: ...
    def LogUpdate(self, reason: int) -> None:
        ...


class CustomViewSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    DelayUpdateOnCreation: bool
    DelayViewUpdate: bool
    HiddenLinesColor: NXColor
    HiddenLinesFont: Drawings.CustomViewSettingsBuilder.Font
    HiddenLinesWidth: Drawings.CustomViewSettingsBuilder.Width
    InterferingSolids: Drawings.CustomViewSettingsBuilder.Interfering
    MinimumPitch: float
    RenderTrueHiddenLine: bool
    ShowAdjacentBlends: bool
    ShowCenterLines: bool
    ShowCheckBoundaryStatus: bool
    ShowEdgesHiddenByEdges: bool
    ShowHiddenLines: bool
    ShowSelfHiddenLines: bool
    ShowSmoothEdgeEndGapsLock: bool
    ShowSmoothEdgeEndGapsValue: float
    ShowSmoothEdges: bool
    ShowTraceLines: bool
    ShowUVGrids: bool
    ShowVIEndGapsLock: bool
    ShowVIEndGapsValue: float
    ShowVirtualIntersections: bool
    SmallFeatures: Drawings.CustomViewSettingsBuilder.Features
    SmoothEdgeColor: NXColor
    SmoothEdgeFont: Drawings.CustomViewSettingsBuilder.Font
    SmoothEdgeWidth: Drawings.CustomViewSettingsBuilder.Width
    ThreadStandard: Drawings.CustomViewSettingsBuilder.ThreadStandards
    TraceLineCreateGapsLock: bool
    TraceLineCreateGapsValue: float
    TraceLineHiddenColor: NXColor
    TraceLineHiddenFont: Drawings.CustomViewSettingsBuilder.Font
    TraceLineHiddenWidth: Drawings.CustomViewSettingsBuilder.Width
    TraceLineVisibleColor: NXColor
    TraceLineVisibleFont: Drawings.CustomViewSettingsBuilder.Font
    TraceLineVisibleWidth: Drawings.CustomViewSettingsBuilder.Width
    VirtualInterSectionColor: NXColor
    VirtualInterSectionFont: Drawings.CustomViewSettingsBuilder.Font
    VirtualInterSectionWidth: Drawings.CustomViewSettingsBuilder.Width


    class Width(enum.Enum):
        Original = 0
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class ThreadStandards(enum.Enum):
        None = 0
        AnsiSimplified = 1
        AnsiSchematic = 2
        AnsiDetailed = 3
        IsoSimplified = 4
        IsoDetailed = 5
        EskdSimplified = 6
    

    class Interfering(enum.Enum):
        None = 0
        WithoutInterference = 1
        WithInterference = 2
    

    class Font(enum.Enum):
        Invisible = 0
        Solid = 1
        Dashed = 2
        Phantom = 3
        Centerline = 4
        Dotted = 5
        LongDashed = 6
        DottedDashed = 7
        Eight = 8
        Nine = 9
        Ten = 10
        Eleven = 11
    

    class Features(enum.Enum):
        ShowAll = 0
        Simplify = 1
        Hide = 2
    

class ConvertToPMIBuilderManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateConvertDraftingContentsBuilder(self) -> Drawings.ConvertDraftingContentsBuilder:
        ...
    def CreateReportBuilder(self) -> Drawings.ReportBuilder:
        ...
    def DeleteConversionReport(self, reportIndex: int) -> None:
        ...
    def GetConversionReportsCount(self) -> int:
        ...
    def DeleteConvertedData(self, reportIndex: int) -> None:
        ...
    def Tag(self) -> Tag: ...



class ConvertDraftingContentsBuilder(Builder):
    def __init__(self) -> None: ...
    def SetContextAssembly(self, contextAssembly: str) -> None:
        ...
    ConfigurationFile: str
    OpenConvertedPmiDestinationPart: bool
    SelectDraftingSheet: SelectViewList
    SelectDraftingView: Drawings.SelectDraftingViewList
    SelectObjectsToConvert: SelectNXObjectList
    SelectionType: Drawings.ConvertDraftingContentsBuilder.SelectConversionEntityType
    SettingsBuilder: Drawings.SettingsBuilder
    UseContextAssembly: bool


    class SelectConversionEntityType(enum.Enum):
        Drawing = 0
        Sheet = 1
        View = 2
        Annotation = 3
    

class ConversionProcessSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ActionOnError: Drawings.ConversionProcessSettingsBuilder.ActionOnErrorEnum
    ConfigurationFile: str
    CreateInMasterModelPart: bool
    ErrorLimit: int
    JTGeometryTolerance: float
    JTPartNameAttribute: str
    LogFileLocation: str
    MultiCADAssembly: bool
    SaveAsLocation: str
    SourcePartNameAttribute: str
    StoreLogFileInTeamCenter: bool


    class ActionOnErrorEnum(enum.Enum):
        SkipObjectAndContinue = 0
        StopProcessingAfterLimit = 1
        StopProcessing = 2
    

class CompareReportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSummary(self) -> str:
        ...
    def GetDetailSummary(self) -> str:
        ...
    def GetChangesSummary(self) -> str:
        ...
    SummaryStatusLine: str


class BrokenViewBuilder(Builder):
    def __init__(self) -> None: ...
    Amplitude: Expression
    BreakLine1Anchor: Point
    BreakLine1ModelAnchor: Point
    BreakLine1Offset: Expression
    BreakLine2Anchor: Point
    BreakLine2ModelAnchor: Point
    BreakLine2Offset: Expression
    BreakLineType: Drawings.BrokenViewBuilder.BreakLineStyle
    BreakType: Drawings.BrokenViewBuilder.TypeBreak
    BreakVisibility: bool
    Color: NXColor
    CrossHatch: Annotations.HatchFillSettingsBuilder
    DirectionType: Drawings.BrokenViewBuilder.TypeDirection
    DirectionVector: Direction
    ExistingCurve: ScCollector
    Extension1: Expression
    Extension2: Expression
    Gap: Expression
    IsBreakLine1Associative: bool
    IsBreakLine2Associative: bool
    MasterView: Drawings.SelectDraftingView
    Repetition: int
    Suppress: bool
    Width: Drawings.BrokenViewBuilder.LineWidth


    class VerticalBreakSide(enum.Enum):
        TopEnd = 0
        BottomEnd = 1
    

    class TypeDirection(enum.Enum):
        Parallel = 0
        Perpendicular = 1
        Vector = 2
    

    class TypeBreak(enum.Enum):
        Regular = 0
        SingleSided = 1
    

    class LineWidth(enum.Enum):
        Thin = 0
        Medium = 1
        Thick = 2
        WidthOne = 5
        WidthTwo = 6
        WidthThree = 7
        WidthFour = 8
        WidthFive = 9
        WidthSix = 10
        WidthSeven = 11
        WidthEight = 12
        WidthNine = 13
    

    class HorizontalBreakSide(enum.Enum):
        LeftEnd = 0
        RightEnd = 1
    

    class BreakLineStyle(enum.Enum):
        Simple = 0
        Straight = 1
        Sawtooth = 2
        LongBreak = 3
        Tubular = 4
        SolidTubular = 5
        SolidRod = 6
        Jigsaw = 7
        Wood = 8
        CopyCurve = 9
        TemplateCurve = 10
    

class BordersAndZonesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Drawings.BordersAndZones]:
        ...
    def __init__(self, owner: DraftingManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Drawings.BordersAndZones:
        ...
    def CreateBordersAndZonesBuilder(self, bordersAndZones: Drawings.BordersAndZones) -> Drawings.BordersAndZonesBuilder:
        ...
    def Tag(self) -> Tag: ...



    class ZoneOrigin(enum.Enum):
        BottomRight = 0
        TopLeft = 1
        TopRight = 2
        BottomLeft = 3
    

    class ZoneMethod(enum.Enum):
        None = 0
        Standard = 1
        Custom = 2
    

class BordersAndZonesBuilder(Builder):
    def __init__(self) -> None: ...
    BorderAndZoneStyle: Drawings.BorderAndZoneStyleBuilder
    BottomMargin: float
    CenteringMarkExtension: float
    CreateBorders: bool
    CreateTrimmingMarks: bool
    CreateZoneLabels: bool
    CreateZoneMarking: bool
    HorizontalCenteringMark: Drawings.BordersAndZonesBuilder.HorizontalCenteringMarkType
    HorizontalSize: float
    LabelFont: int
    LabelHeight: float
    LeftMargin: float
    MarkingHeight: float
    Method: Drawings.BordersAndZonesBuilder.ZoneMethod
    Origin: Drawings.BordersAndZonesBuilder.ZoneOrigin
    RightMargin: float
    TopMargin: float
    TrimmingMarkLength: float
    TrimmingMarkThickness: float
    VerticalCenteringMark: Drawings.BordersAndZonesBuilder.VerticalCenteringMarkType
    VerticalSize: float
    Width: float


    class VerticalCenteringMarkType(enum.Enum):
        None = 0
        BottomArrow = 1
        TopArrow = 2
        BottomandTopArrow = 3
        BottomandTopLine = 4
    

    class HorizontalCenteringMarkType(enum.Enum):
        None = 0
        LeftArrow = 1
        RightArrow = 2
        LeftandRightArrow = 3
        LeftandRightLine = 4
    

    class FontEnum(enum.Enum):
        Blockfont = 0
    

class BordersAndZones(NXObject):
    def __init__(self) -> None: ...


class BorderAndZoneStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    BorderAndZoneStandard: int
    SheetBorderSettingsStyle: Drawings.SheetBorderSettingsBuilder
    SheetMarginSettingsStyle: Drawings.SheetMarginSettingsBuilder
    SheetZoneSettingsStyle: Drawings.SheetZoneSettingsBuilder


class BaseViewStyle(Utilities.NXRemotableObject):
    def __init__(self, owner: Drawings.ViewStyle) -> None: ...
    def SetFacetedRepresentation(self, isFacetedRepresentation: bool) -> None:
        """[Obsolete("Deprecated in NX8.5.1.  Use Drawings.GeneralViewStyle.ViewRepresentation instead.")"""
        ...
    def SetInheritClippingBoundary(self, isInheritClippingBoundary: bool) -> None:
        ...
    def SetTransferAnnotation(self, isTransferAnnotation: bool) -> None:
        ...
    def SetAssemblyArrangement(self, config: str) -> None:
        ...
    def LoadModelFromPart(self, loadPartName: str, loadPartToggle: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class BaseViewBuilder(Builder):
    def __init__(self) -> None: ...
    HiddenObjects: Drawings.HiddenObjectsBuilder
    NonSectionedObjects: Drawings.HiddenObjectsBuilder
    Placement: Drawings.ViewPlacementBuilder
    Scale: Drawings.ViewScaleBuilder
    SecondaryComponents: Drawings.DraftingComponentSelectionBuilder
    SelectModelView: Drawings.SelectModelViewBuilder
    Style: Drawings.ViewStyleBuilder


class BaseView(Drawings.DraftingView):
    def __init__(self) -> None: ...


class BaseSteppedSectionLine(Drawings.SectionLine):
    def __init__(self) -> None: ...


class BasePointToPointSectionLine(Drawings.SectionLine):
    def __init__(self) -> None: ...


class BaseHalfSectionLine(Drawings.SectionLine):
    def __init__(self) -> None: ...


class AutomationTemplateRegionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DisplayRegionLabel: bool
    DisplayTemplatePart: bool
    LineColorFontWidth: LineColorFontWidthBuilder


class AutomationBookletBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    HiddenLineColorFontWidth: LineColorFontWidthBuilder
    VisibleLineColorFontWidth: LineColorFontWidthBuilder


class AssociativeAngleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AlternateAngle(self) -> None:
        ...
    def CreateScalarObject(self) -> None:
        ...
    def SetIsMeasure(self, isMeasure: bool) -> None:
        ...
    def CreateScalarObjectFromData(self, scalarTag: Scalar, angleValue: float) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Angle: Expression
    AngleValue: float
    Associative: bool
    EvaluationPlane: Drawings.AssociativeAngleBuilder.EvaluationPlaneType
    FirstMapView: View
    FirstObject: SelectNXObject
    FirstObjectType: Drawings.AssociativeAngleBuilder.ObjectType
    FirstVector: Direction
    Plane: Plane
    ScalarObject: Scalar
    SecondMapView: View
    SecondObject: SelectNXObject
    SecondObjectType: Drawings.AssociativeAngleBuilder.ObjectType
    SecondVector: Direction


    class ObjectType(enum.Enum):
        Object = 0
        Vector = 1
    

    class EvaluationPlaneType(enum.Enum):
        DrawingSheet = 0
        TrueAngle = 1
        SpecifyPlane = 2
    

class ArrowStyleType(enum.Enum):
    Filled = 0
    Closed = 1
    ClosedSolid = 2
    Open = 3


class ArrowDirectionType(enum.Enum):
    OutofSheet = 0
    IntoSheet = 1


class AnnotationSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SaveAnnotationType(self, annType: Drawings.AnnotationSettingsBuilder.AnnotationTypeEnum, annValue: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ConvertToOriginalModelView: bool
    LinearDimensionTolerance: float
    PreserveDraftingLayer: bool
    PreserveHiddenStatus: bool
    ProcessObjectsHidden: bool
    Units: Drawings.AnnotationSettingsBuilder.UnitsEnum


    class UnitsEnum(enum.Enum):
        UseTargetPartUnits = 0
        UseDrawingUnits = 1
    

    class AnnotationTypeEnum(enum.Enum):
        Dimension = 0
        Note = 1
        FeatureControlFrame = 2
        DatumFeatureSymbol = 3
        DatumTarget = 4
        Balloon = 5
        SurfaceFinishSymbol = 6
        WeldSymbol = 7
        CustomSymbol = 8
        CenterLine = 9
        UserDefinedSymbol = 10
        MaxAnnotationYypes = 11
    

class AddRemoveBoxViewBuilder(Builder):
    def __init__(self) -> None: ...
    Mode: Drawings.AddRemoveBoxViewBuilder.ModeType
    SelectedView: ModelingView


    class ModeType(enum.Enum):
        Add = 0
        Remove = 1
    

class AddObjectsToRegionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetMasterSymbolFilePaths(self, symbolPath: str) -> None:
        ...
    SelectedRegion: Drawings.SelectDrawingRegion


