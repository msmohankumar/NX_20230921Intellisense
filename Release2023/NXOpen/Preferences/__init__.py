from ...NXOpen import *
from ..Preferences import *

import typing
import enum

class WorkPlane(NXObject):
    def __init__(self) -> None: ...
    def GetRectangularUniformGridSize(self) -> Preferences.WorkPlane.GridSize:
        ...
    def SetRectangularUniformGridSize(self, gridSize: Preferences.WorkPlane.GridSize) -> None:
        ...
    def GetRectangularNonuniformGridSize(self) -> Preferences.WorkPlane.NonuniformGridSize:
        ...
    def SetRectangularNonuniformGridSize(self, nonuniformGridSize: Preferences.WorkPlane.NonuniformGridSize) -> None:
        ...
    def GetPolarGridSize(self) -> Preferences.WorkPlane.PolarGridSize:
        ...
    def SetPolarGridSize(self, polarGridSize: Preferences.WorkPlane.PolarGridSize) -> None:
        ...
    GridColor: int
    GridIsNonUniform: bool
    GridOnTop: bool
    GridType: Preferences.WorkPlane.Grid
    PolarShowMajorLines: bool
    RectangularShowMajorLines: bool
    ShowGrid: bool
    ShowLabels: bool
    SnapToGrid: bool


    class WorkPlanePolarGridSize():
        RadialGridSize: Preferences.WorkPlane.GridSize
        AngularGridSize: Preferences.WorkPlane.GridSize
        def ToString(self) -> str:
            ...
        def __init__(self, RadialGridSize: Preferences.WorkPlane.GridSize, AngularGridSize: Preferences.WorkPlane.GridSize) -> None: ...
    

    class WorkPlaneNonuniformGridSize():
        XcGridSize: Preferences.WorkPlane.GridSize
        YcGridSize: Preferences.WorkPlane.GridSize
        def ToString(self) -> str:
            ...
        def __init__(self, XcGridSize: Preferences.WorkPlane.GridSize, YcGridSize: Preferences.WorkPlane.GridSize) -> None: ...
    

    class WorkPlaneGridSize():
        MajorGridSpacing: float
        MinorLinesPerMajor: int
        SnapPointsPerMinor: int
        def ToString(self) -> str:
            ...
        def __init__(self, MajorGridSpacing: float, MinorLinesPerMajor: int, SnapPointsPerMinor: int) -> None: ...
    

    class Grid(enum.Enum):
        Polar = 0
        Rectangular = 1
    

class WiringPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def GetCompMatchMethodPriorityList(self) -> typing.List[Preferences.WiringPreferences.CompMatchMethod]:
        ...
    def SetCompMatchMethodPriorityList(self, priorityList: typing.List[Preferences.WiringPreferences.CompMatchMethod]) -> None:
        ...
    def Tag(self) -> Tag: ...

    BundleColor: NXColor
    CompAttributeTitle: str
    CompListColHeading: Preferences.WiringPreferences.CompListColumnHeading
    ComponentListColumnTitle: str
    ComponentMatchMethod: Preferences.WiringPreferences.CompMatchMethod
    DefaultHarnessName: str
    DeleteStockOnRoute: bool
    RouteLevelEnum: Preferences.WiringPreferences.RouteLevelGroupEnumOptions
    StockStyleEnum: Preferences.WiringPreferences.StockStyleGroupEnumOptions
    WirePath: bool
    WireStock: bool


    class StockStyleGroupEnumOptions(enum.Enum):
        Centerline = 0
        Simple = 1
    

    class RouteLevelGroupEnumOptions(enum.Enum):
        PinLevel = 1
        ComponentLevel = 2
    

    class CompMatchMethod(enum.Enum):
        Attribute = 0
        ComponentName = 1
        FileName = 2
    

    class CompListColumnHeading(enum.Enum):
        DeviceID = 0
        ConnectorID = 1
        PartName = 2
        Description = 3
    

class Width(enum.Enum):
    Original = 0
    Thin = 1
    Normal = 2
    Thick = 3
    One = 5
    Two = 6
    Three = 7
    Four = 8
    Five = 9
    Six = 10
    Seven = 11
    Eight = 12
    Nine = 13


class VisualizationLine(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def RegenerateFromToleranceChange(self, updateModeChange: bool, studio: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Preferences.PartVisualizationLine.RegenerateFromToleranceChange instead.")"""
        ...
    def UpdateLineFontObjects(self, doSoftwareUpdate: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Preferences.PartVisualizationLine.UpdateLineFontObjects instead.")"""
        ...
    def Tag(self) -> Tag: ...

    DepthSortedWireframe: bool
    WireframeContrast: bool


class VisualizationHandles(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    HandleSize: int
    ShowHandleHints: bool


    class HandleSizeValue(enum.Enum):
        Small = 0
        Medium = 1
        Large = 2
    

class VisualizationFonts(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def GetDefaultStandardTextFont(self, fontFamily: str, fontStyle: Preferences.VisualizationFonts.StyleType, fontSize: int) -> None:
        ...
    def SetDefaultStandardTextFont(self, fontFamily: str, fontStyle: Preferences.VisualizationFonts.StyleType, fontSize: int) -> None:
        ...
    def Tag(self) -> Tag: ...



    class StyleType(enum.Enum):
        Regular = 0
        Bold = 1
        Italic = 2
        BoldItalic = 3
    

class VisibleLinesViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    VisibleColor: int
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class VirtualIntersectionsViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AdjacentBlends: bool
    AdjacentBlendsColor: int
    AdjacentBlendsEndGaps: bool
    AdjacentBlendsEndGapsData: float
    AdjacentBlendsFont: Preferences.Font
    AdjacentBlendsWidth: Preferences.Width
    VirtualIntersection: bool


class ViewVisualizationVisual(Utilities.NXRemotableObject):
    def __init__(self, owner: View) -> None: ...
    def Tag(self) -> Tag: ...

    DisplayAppearance: Preferences.ViewVisualizationVisual.DisplayAppearanceOptions
    HiddenEdgeStyle: Preferences.ViewVisualizationVisual.HiddenEdgeStyleType
    ShadedEdgeColor: int
    ShadedEdgeStyle: Preferences.ViewVisualizationVisual.ShadedEdgeStyleType
    ShininessData: float
    SurfaceDisplay: Preferences.ViewVisualizationVisual.SurfaceDisplayOptions
    TrueSurfaceDisplay: Preferences.ViewVisualizationVisual.TrueSurfaceDisplayPref
    TwoSidedLight: bool


    class ViewVisualizationVisualTrueSurfaceDisplayPref():
        HiddenEdgesType: Preferences.ViewVisualizationVisual.HiddenEdgesType
        Silhouettes: bool
        SmoothEdges: bool
        SmoothEdgesColor: int
        SmoothEdgesFont: Preferences.ViewVisualizationVisual.SmoothEdgeFont
        SmoothEdgesWidth: Preferences.ViewVisualizationVisual.SmoothEdgeWidth
        DisplayMode: Preferences.ViewVisualizationVisual.DisplayModeType
        def ToString(self) -> str:
            ...
    

    class ViewVisualizationVisualSurfaceDisplayOptions():
        RenderingStyle: Preferences.ViewVisualizationVisual.RenderingStyle
        HiddenEdges: Preferences.ViewVisualizationVisual.HiddenEdges
        Silhouettes: bool
        SmoothEdges: bool
        SmoothEdgeColor: int
        SmoothEdgeFont: Preferences.ViewVisualizationVisual.SmoothEdgeFont
        SmoothEdgeWidth: Preferences.ViewVisualizationVisual.SmoothEdgeWidth
        def ToString(self) -> str:
            ...
    

    class SmoothEdgeWidth(enum.Enum):
        Original = 0
        Thin = 1
        Normal = 2
        Thick = 3
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class SmoothEdgeFont(enum.Enum):
        Original = 0
        Solid = 1
        Dashed = 2
        Phantom = 3
        CenterLine = 4
        Dotted = 5
        LongDashed = 6
        DottedDashed = 7
        Eight = 11
        Nine = 12
        Ten = 13
        Eleven = 14
    

    class ShadedEdgeStyleType(enum.Enum):
        ShadedEdgeColor = 0
        BodyColor = 1
        None = 2
    

    class RenderingStyle(enum.Enum):
        Shaded = 0
        Wireframe = 1
        Studio = 2
        FaceAnalysis = 3
        PartiallyShaded = 4
        StaticWireframe = 5
    

    class InterferingSolids(enum.Enum):
        Off = 0
        On = 1
        WithCurves = 2
    

    class HiddenEdgesType(enum.Enum):
        Visible = 0
        Invisible = 1
        Dashed = 2
        GrayThin = 3
        HiddenSurface = 4
    

    class HiddenEdgeStyleType(enum.Enum):
        Invisible = 0
        HiddenGeometryColor = 1
        Dashed = 2
    

    class HiddenEdges(enum.Enum):
        Visible = 0
        Invisible = 1
        GrayThin = 2
        Dashed = 3
    

    class DisplayModeType(enum.Enum):
        Wireframe = 0
        PartiallyShaded = 1
        FullyShaded = 2
        FaceAnalysis = 3
        Studio = 4
    

    class ViewVisualizationVisualDisplayAppearanceOptions():
        RenderingStyle: Preferences.ViewVisualizationVisual.RenderingStyle
        HiddenEdges: Preferences.ViewVisualizationVisual.HiddenEdges
        InterferingSolids: Preferences.ViewVisualizationVisual.InterferingSolids
        Silhouettes: bool
        SmoothEdges: bool
        SmoothEdgeColor: int
        SmoothEdgeFont: Preferences.ViewVisualizationVisual.SmoothEdgeFont
        SmoothEdgeWidth: Preferences.ViewVisualizationVisual.SmoothEdgeWidth
        SmoothEdgeAngleTolerance: float
        def ToString(self) -> str:
            ...
    

class ViewVisualizationSpecialEffects(Utilities.NXRemotableObject):
    def __init__(self, owner: View) -> None: ...
    def UpdateFogDisplay(self, fogData: Preferences.ViewVisualizationSpecialEffects.FogData) -> None:
        ...
    def Tag(self) -> Tag: ...

    FogBackValue: int
    FogBackgroundColor: bool
    FogColorHLSValue: Preferences.ViewVisualizationSpecialEffects.ColorHLS
    FogColorHSVValue: Preferences.ViewVisualizationSpecialEffects.ColorHSV
    FogColorRGBValue: Preferences.ViewVisualizationSpecialEffects.ColorRGB
    FogFrontValue: int
    FogRateValue: int
    FogSetting: Preferences.ViewVisualizationSpecialEffects.FogType
    FogSettingOption: bool


    class FogType(enum.Enum):
        Linear = 0
        Light = 1
        Heavy = 2
    

    class ViewVisualizationSpecialEffectsFogData():
        FogMode: int
        FogColorFlag: bool
        FogColor: Preferences.ViewVisualizationSpecialEffects.ColorRGB
        FogStart: float
        FogEnd: float
        FogDensity: float
        def ToString(self) -> str:
            ...
    

    class ViewVisualizationSpecialEffectsColorRGB():
        RedColor: float
        GreenColor: float
        BlueColor: float
        def ToString(self) -> str:
            ...
        def __init__(self, RedColor: float, GreenColor: float, BlueColor: float) -> None: ...
    

    class ViewVisualizationSpecialEffectsColorHSV():
        Hue: float
        Saturation: float
        Value: float
        def ToString(self) -> str:
            ...
        def __init__(self, Hue: float, Saturation: float, Value: float) -> None: ...
    

    class ViewVisualizationSpecialEffectsColorHLS():
        Hue: float
        Lightness: float
        Saturation: float
        def ToString(self) -> str:
            ...
        def __init__(self, Hue: float, Lightness: float, Saturation: float) -> None: ...
    

class ViewSection(Builder):
    def __init__(self) -> None: ...
    def SetDefaults(self) -> None:
        ...
    LoadExact: bool
    TranslucentPlanes: bool


class ViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def Tag(self) -> Tag: ...

    General: Preferences.GeneralViewPreferences
    BaseView: Preferences.BaseViewPreferences
    Projected: Preferences.ProjectedViewPreferences
    InheritPmi: Preferences.InheritPmiPreferences
    Detail: Preferences.DetailViewPreferences
    Section: Preferences.SectionViewPreferences
    VirtualIntersections: Preferences.VirtualIntersectionsViewPreferences
    SmoothEdges: Preferences.SmoothEdgesViewPreferences
    VisibleLines: Preferences.VisibleLinesViewPreferences
    Threads: Preferences.ThreadsViewPreferences
    TraceLines: Preferences.TraceLinesViewPreferences
    HiddenLines: Preferences.HiddenLinesViewPreferences
    Shading: Preferences.ShadingViewPreferences
    FlatPattern: Preferences.FlatPatternViewPreferences
    ShipbuildingLines: Preferences.ShipbuildingLinesViewPreferences
    ShipDraftingViewLines: Preferences.ShipDraftingViewLinesViewPreferences
    ShipGeneralArrangementViewLines: Preferences.ShipGeneralArrangementViewLinesViewPreferences


class TraceLinesViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CreateGapsStatus: bool
    GapSize: float
    HiddenColor: int
    HiddenFont: Preferences.Font
    HiddenWidth: Preferences.Width
    VisibleColor: int
    VisibleFont: Preferences.Font
    VisibleWidth: Preferences.Width


class ThreadsViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    MinimumPitchField: float
    OverrideVisibleThreadColor: int
    RenderTrueHiddenLine: bool
    ThreadsStandardOptionData: int


class TextureModelingPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def DisplayDistortion(self, display: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    ReversedUVPatchColor: int
    RipEdgesColor: int
    RipEdgesFont: DisplayableObject.ObjectFont
    RipEdgesWidth: DisplayableObject.ObjectWidth
    Show2DGrid: bool
    Show3DGrid: bool
    ULineColor: int
    ULineFont: DisplayableObject.ObjectFont
    ULineWidth: DisplayableObject.ObjectWidth
    UVPatchColor: int
    VLineColor: int
    VLineFont: DisplayableObject.ObjectFont
    VLineWidth: DisplayableObject.ObjectWidth


class SubdivisionModelingPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CagePolylineColor: int
    CagePolylineFont: int
    CagePolylineVertexColor: int
    CagePolylineVertexSize: Preferences.SubdivisionModelingPreferences.CagePolylineVertexSizes
    CagePolylineVertexStyle: Preferences.SubdivisionModelingPreferences.CagePolylineVertexStyles
    CagePolylineWidth: int
    CanAllowBackSideSelection: bool
    CanShowWeight: bool
    ConstraintColor: int
    DisplayMode: Preferences.SubdivisionModelingPreferences.DisplayModes
    HighlightFaceTranslucency: int
    IsXRayCage: bool
    LineColor: int
    LineFont: int
    LineWidth: int
    SharpEdgeLineFont: int
    VertexColor: int
    VertexSize: Preferences.SubdivisionModelingPreferences.VertexSizeTypes
    VertexStyle: Preferences.SubdivisionModelingPreferences.VertexStyleTypes


    class VertexStyleTypes(enum.Enum):
        Square = 0
        Triangle = 1
        Circle = 2
        Plus = 3
        Cross = 4
    

    class VertexSizeTypes(enum.Enum):
        Small = 0
        Medium = 1
        Large = 2
    

    class DisplayModes(enum.Enum):
        CageAndBody = 0
        CageOnly = 1
        BodyOnly = 2
    

    class CagePolylineVertexStyles(enum.Enum):
        None = 0
        Square = 1
        Triangle = 2
        Circle = 3
        Plus = 4
        Cross = 5
    

    class CagePolylineVertexSizes(enum.Enum):
        Small = 0
        Medium = 1
        Large = 2
    

class SmoothEdgesViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    SmoothEdge: bool
    SmoothEdgeColor: int
    SmoothEdgeEndGaps: bool
    SmoothEdgeEndGapsData: float
    SmoothEdgeFont: Preferences.Font
    SmoothEdgeTolerance: bool
    SmoothEdgeToleranceData: float
    SmoothEdgeWidth: Preferences.Width


class SketchPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Sketch) -> None: ...
    def ApplySketchPreferences(self, dimDisplayFlag: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    ConstraintSymbolSize: float
    ContinuousAutoDimensioningSetting: bool
    CreateInferredConstraints: bool
    DimensionLabel: Preferences.SketchPreferences.DimensionLabelType
    DimensionTextScale: float
    DisplayObjectColor: bool
    DisplayObjectName: bool
    DisplayParenthesesOnReferenceDimensions: bool
    DisplayReferenceGeometry: bool
    DisplayShadedRegions: bool
    DisplayVertices: bool
    FixedTextSize: float
    SolvingTolerance: float
    TextSizeFixed: bool
    TextSizeMode: Preferences.SketchPreferences.DimensionTextSizeMode
    UseSolvingTolerance: bool


    class DimensionTextSizeMode(enum.Enum):
        DraftingStandard = 0
        FixedOnScreen = 1
        Variable = 2
    

    class DimensionLabelType(enum.Enum):
        Expression = 0
        Name = 1
        Value = 2
    

class ShipGeneralArrangementViewLinesViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def SetAttributeName(self, viewPlan: str, displayName: str, attributeName: str) -> None:
        ...
    def GetAttributeName(self, viewPlan: str, displayName: str) -> str:
        ...
    def SetAttributeValue(self, viewPlan: str, displayName: str, attributeValue: str) -> None:
        ...
    def GetAttributeValue(self, viewPlan: str, displayName: str) -> str:
        ...
    def SetColor(self, viewPlan: str, displayName: str, linesType: Preferences.ShipGeneralArrangementViewLinesViewPreferences.Lines, color: NXColor) -> None:
        ...
    def GetColor(self, viewPlan: str, displayName: str, linesType: Preferences.ShipGeneralArrangementViewLinesViewPreferences.Lines) -> NXColor:
        ...
    def SetFont(self, viewPlan: str, displayName: str, linesType: Preferences.ShipGeneralArrangementViewLinesViewPreferences.Lines, font: Preferences.Font) -> None:
        ...
    def GetFont(self, viewPlan: str, displayName: str, linesType: Preferences.ShipGeneralArrangementViewLinesViewPreferences.Lines) -> Preferences.Font:
        ...
    def SetWidth(self, viewPlan: str, displayName: str, linesType: Preferences.ShipGeneralArrangementViewLinesViewPreferences.Lines, width: Preferences.Width) -> None:
        ...
    def GetWidth(self, viewPlan: str, displayName: str, linesType: Preferences.ShipGeneralArrangementViewLinesViewPreferences.Lines) -> Preferences.Width:
        ...
    def Tag(self) -> Tag: ...



    class Lines(enum.Enum):
        Visible = 0
        Hidden = 1
    

class ShipDraftingViewLinesViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def SetShipDrawingObject(self, featureName: str, singleLine: bool) -> None:
        ...
    def GetShipDrawingObject(self, featureName: str) -> bool:
        ...
    def SetColor(self, featureName: str, linesType: Preferences.ShipDraftingViewLinesViewPreferences.Lines, color: int) -> None:
        ...
    def GetColor(self, featureName: str, linesType: Preferences.ShipDraftingViewLinesViewPreferences.Lines) -> int:
        ...
    def SetFont(self, featureName: str, linesType: Preferences.ShipDraftingViewLinesViewPreferences.Lines, font: Preferences.Font) -> None:
        ...
    def GetFont(self, featureName: str, linesType: Preferences.ShipDraftingViewLinesViewPreferences.Lines) -> Preferences.Font:
        ...
    def SetWidth(self, featureName: str, linesType: Preferences.ShipDraftingViewLinesViewPreferences.Lines, width: Preferences.Width) -> None:
        ...
    def GetWidth(self, featureName: str, linesType: Preferences.ShipDraftingViewLinesViewPreferences.Lines) -> Preferences.Width:
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
    

class ShipbuildingLinesViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def SetSingleLineRepresentation(self, featureType: Preferences.ShipbuildingLinesViewPreferences.ShipbuildingLines, featureName: str, singleLine: bool) -> None:
        ...
    def GetSingleLineRepresentation(self, featureType: Preferences.ShipbuildingLinesViewPreferences.ShipbuildingLines, featureName: str) -> bool:
        ...
    def SetColor(self, featureName: str, linesType: Preferences.ShipbuildingLinesViewPreferences.Lines, color: int) -> None:
        ...
    def GetColor(self, featureName: str, linesType: Preferences.ShipbuildingLinesViewPreferences.Lines) -> int:
        ...
    def SetFont(self, featureName: str, linesType: Preferences.ShipbuildingLinesViewPreferences.Lines, font: Preferences.Font) -> None:
        ...
    def GetFont(self, featureName: str, linesType: Preferences.ShipbuildingLinesViewPreferences.Lines) -> Preferences.Font:
        ...
    def SetWidth(self, featureName: str, linesType: Preferences.ShipbuildingLinesViewPreferences.Lines, width: Preferences.Width) -> None:
        ...
    def GetWidth(self, featureName: str, linesType: Preferences.ShipbuildingLinesViewPreferences.Lines) -> Preferences.Width:
        ...
    def Tag(self) -> Tag: ...



    class ShipbuildingLines(enum.Enum):
        Profile = 0
        Plate = 1
    

    class Lines(enum.Enum):
        Hidden = 0
        Visible = 1
    

class ShadingViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
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


class ShadingToleranceOption(enum.Enum):
    Coarse = 0
    Standard = 1
    Fine = 2
    ExtraFine = 3
    UltraFine = 4
    Customize = 5


class ShadingRenderingStyleOption(enum.Enum):
    FullyShaded = 0
    PartiallyShaded = 1
    Wireframe = 2


class SessionWorkPlane(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    ObjectOffWorkPlane: Preferences.SessionWorkPlane.ObjectDisplay


    class ObjectDisplay(enum.Enum):
        Normal = 0
        DimAndSelectable = 1
        DimAndNonSelectable = 2
    

class SessionVisualizationVisual(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def GetViewFromPoint(self, screenX: int, screenY: int, view: View, viewPoint: Point3d) -> None:
        ...
    def Tag(self) -> Tag: ...

    DecalStickersInShadedDisplay: bool
    EnableFlatShading: bool
    FullSceneAntialiasing: bool
    LineAntialiasing: bool
    ReduceEdgeBleedThrough: bool
    Translucency: bool


class SessionVisualizationView(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    MaintainViewOriginWhenZooming: bool
    SetViewOriginWhenRotationReferenceIsSet: bool


class SessionVisualizationSpecialEffects(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    EnableStereo: bool
    ParallaxFactor: int
    SupportStereo: bool


class SessionVisualizationShade(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def RegenerateStudioAnalysisViewsFromTolChange(self, updateEnvOption: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Preferences.PartVisualizationShade.RegenerateStudioAnalysisViewsFromToleranceChange instead.")"""
        ...
    def RegenerateShadedViewsFromToleranceChange(self) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Preferences.PartVisualizationShade.RegenerateShadedViewsFromToleranceChange instead.")"""
        ...
    def Tag(self) -> Tag: ...

    EdgesEmphasis: bool
    LwrtStudioDisplay: bool
    ShowFacetEdges: bool


class SessionVisualizationScreen(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CsysFixedSizeOnScreen: bool
    CsysShowThrough: bool
    DisplayCenterOfRotation: bool
    DoFitOnHideOrShow: bool
    ExcludeDatumsFromFit: bool
    FitPercentage: int
    FitToSectionClipPlanes: bool
    HighPrecisionPanning: bool
    HighPrecisionRotation: bool
    IgnoreLockVerticalAxis: bool
    InferEdgeOutput: bool
    LockVerticalAxis: bool
    PreserveFieldOfViewAngleForFit: bool
    RotationPointDelay: int
    TiltSnapAngle: float
    TriadLocation: Preferences.SessionVisualizationScreen.ViewTriadLocation
    TriadVisibility: int


    class ViewTriadLocation(enum.Enum):
        BottomLeft = 0
        BottomRight = 1
    

class SessionVisualizationPerformance(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    RenderSolidsUsingStoredFacets: bool


class SessionVisualizationHighQualityImage(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def GetImageSize(self, imageSize: Preferences.SessionVisualizationHighQualityImage.ImageSizeType, xSize: int, ySize: int) -> None:
        ...
    def SetImageSize(self, imageSize: Preferences.SessionVisualizationHighQualityImage.ImageSizeType, xSize: int, ySize: int) -> None:
        ...
    def GetResolution(self, dotsPerInch: int) -> Preferences.SessionVisualizationHighQualityImage.ResolutionType:
        ...
    def SetResolution(self, resolution: Preferences.SessionVisualizationHighQualityImage.ResolutionType, dotsPerInch: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    Orientation: Preferences.SessionVisualizationHighQualityImage.OrientationType
    PlotQuality: Preferences.SessionVisualizationHighQualityImage.PlotQualityType
    SubRegion: bool


    class ResolutionType(enum.Enum):
        Draft = 0
        Low = 1
        Medium = 2
        High = 3
        UserDefined = 4
    

    class PlotQualityType(enum.Enum):
        Fine = 0
        Medium = 1
        Rough = 2
        Coarse = 3
    

    class OrientationType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class ImageSizeType(enum.Enum):
        FillView = 0
        AnsiA = 1
        AnsiB = 2
        AnsiC = 3
        AnsiD = 4
        AnsiE = 5
        IsoA4 = 6
        IsoA3 = 7
        IsoA2 = 8
        IsoA1 = 9
        IsoA0 = 10
        UserDefined = 11
        TrueSize = 12
    

class SessionVisualizationHighEndRendering(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AllowApplyingMaterialsToAllBodiesOfComponents: bool
    StudioMaterialEditorEditingMode: Preferences.SessionVisualizationHighEndRendering.MaterialEditorEditingMode


    class MaterialEditorEditingMode(enum.Enum):
        Basic = 0
        Full = 1
    

class SessionVisualizationEmphasis(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    ObjectsOffSketchWorkPlaneNonSelectable: bool
    ObjectsOffWcsWorkPlaneNonSelectable: bool
    ProductInterfaceEmphasis: bool
    SeeThruAll: bool
    SeeThruDeEmphasizedObjects: bool
    SeeThruPreview: bool
    SeeThruSection: bool
    SketchPlaneEmphasis: bool
    SketchWorkPlaneEmphasis: bool
    WcsWorkPlaneEmphasis: bool
    WorkPartEmphasis: bool


class SessionVisualizationColorSetting(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    HandlesColor: int


class SessionUserInterfaceUI(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def ResetDialogBoxSettings(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    ConfirmUndo: bool
    DialogBarDecimalPlaces: int
    DialogBarTracking: bool
    DisplayAlertsOnInformation: bool
    DisplayAlertsOnWarnings: bool
    DisplayDialogsInPlayback: bool
    DisplayResourceBarOption: Preferences.SessionUserInterfaceUI.DisplayResourceBar
    HomePageURL: str
    InitialDialogDisplay: bool
    ListingDecimalPlaces: int
    PagesAutomaticallyFlyOut: bool
    PauseDuration: int
    RecordAllTransform: bool
    SaveLayoutAtExit: bool
    SpeechRecognitionMode: Preferences.SessionUserInterfaceUI.SpeechMode
    UseSystemPrecision: bool


    class SpeechMode(enum.Enum):
        Single = 0
        Continuous = 1
    

    class DisplayResourceBar(enum.Enum):
        Left = 0
        Right = 1
    

class SessionUserInterface(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    InsetMenuDialogComments: bool
    JournalFileFormat: Preferences.SessionUserInterface.JournalFileFormatType
    JournalLanguage: Preferences.SessionUserInterface.JournalLanguageType


    class JournalLanguageType(enum.Enum):
        VisualBasic = 0
        CPlusPlus = 1
        Java = 2
        Cs = 3
        Python = 4
    

    class JournalFileFormatType(enum.Enum):
        Ascii = 0
        Unicode = 1
        UnicodeBigEndian = 2
        Utf8 = 3
    

class SessionSketch(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AutoDimensionsToArcCenter: bool
    AutoReverse: bool
    BackgroundOption: Preferences.SessionSketch.BackgroundType
    ChangeViewOrientation: bool
    ConstraintSymbolSize: float
    ContinuousAutoDimensioning: bool
    CreateDimensionForTypedValues: bool
    CreateInferredConstraints: bool
    CreatePersistentRelations: bool
    DefaultArcNamePrefix: str
    DefaultConicNamePrefix: str
    DefaultLineNamePrefix: str
    DefaultSketchNamePrefix: str
    DefaultSplineNamePrefix: str
    DefaultVertexNamePrefix: str
    DelayEvaluation: bool
    DimensionLabel: Preferences.SketchPreferences.DimensionLabelType
    DisplayAutoDimensions: bool
    DisplayConstraintSymbols: bool
    DisplayDOFArrows: bool
    DisplayObjectColor: bool
    DisplayObjectName: bool
    DisplayParenthesesOnReferenceDimensions: bool
    DisplayReferenceGeometry: bool
    DisplaySectionMappingWarning: bool
    DisplayShadedRegions: bool
    DisplayVertices: bool
    DynamicConstraintDisplay: bool
    EditDimensionOnCreation: bool
    FindMovableObjects: bool
    FixedTextSize: float
    GroupConstraintOption: Preferences.SessionSketch.GroupConstraintType
    LayoutDimensionTextMode: Preferences.SketchPreferences.DimensionTextSizeMode
    MaintainBlankStatus: bool
    MaintainLayerStatus: bool
    OriginOption: Preferences.SessionSketch.OriginType
    OverrideConstraints: bool
    RelaxDimensions: bool
    RetainDimensions: bool
    RigidSetConstraintOption: Preferences.SessionSketch.RigidSetConstraintType
    ScaleOnFirstDrivingDimension: bool
    SectionView: bool
    SliceOption: bool
    SnapAngle: float
    SolvingTolerance: float
    TextSizeFixed: bool
    UpdateSketchOnly: bool
    UseSolvingTolerance: bool


    class RigidSetConstraintType(enum.Enum):
        PreventConflict = 0
        PreserveAll = 1
    

    class OriginType(enum.Enum):
        InferFromPlaneSelection = 0
        ProjectWorkPartOrigin = 1
    

    class GroupConstraintType(enum.Enum):
        PreventConflict = 0
        PreserveAll = 1
    

    class BackgroundType(enum.Enum):
        Inherit = 0
        Plain = 1
    

class SessionPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateViewSectionPreference(self) -> Preferences.ViewSection:
        ...
    def CreateModelingPreferencesBuilder(self) -> Preferences.ModelingPreferencesBuilder:
        ...
    def Tag(self) -> Tag: ...

    Sketch: Preferences.SessionSketch
    NXGateway: Preferences.SessionNXGateway
    Assemblies: Preferences.SessionAssemblies
    WorkPlane: Preferences.SessionWorkPlane
    Modeling: Preferences.SessionModeling
    Drafting: Preferences.SessionDrafting
    Pmi: Preferences.SessionPmi
    UserInterface: Preferences.SessionUserInterface
    PerformanceVisualization: Preferences.SessionVisualizationPerformance
    ScreenVisualization: Preferences.SessionVisualizationScreen
    ColorSettingVisualization: Preferences.SessionVisualizationColorSetting
    HighQualityImageVisualization: Preferences.SessionVisualizationHighQualityImage
    SpecialEffectsVisualization: Preferences.SessionVisualizationSpecialEffects
    RoutingApplicationView: Preferences.RoutingApplicationView
    KnowledgeFusion: Preferences.RulePreferences
    Pdm: Preferences.SessionPdm
    SessionMeasureReq: Preferences.SessionMeasureRequirements
    VisualizationHandles: Preferences.VisualizationHandles
    SubdivisionModeling: Preferences.SubdivisionModelingPreferences
    MorphMesh: Preferences.MorphMeshPreferences
    VisualizationFonts: Preferences.VisualizationFonts
    EmphasisVisualization: Preferences.SessionVisualizationEmphasis
    PostProcessing: Preferences.PostProcessing
    HighEndRenderingVisualization: Preferences.SessionVisualizationHighEndRendering
    SessionNavigation: Preferences.SessionNavigation
    TextureModeling: Preferences.TextureModelingPreferences
    RoutingPreferences: Preferences.RoutingPreferences
    ViewVisualization: Preferences.SessionVisualizationView
    DrawShape: Preferences.DrawShapeTaskPrefs
    AppearanceManagementPref: Preferences.SessionAppearanceMgrPreference
    WiringPreferences: Preferences.WiringPreferences
    CoatingPreferences: Preferences.CoatingPreferences


class SessionPmi(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def UpdateTrackingPropertiesFromXml(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    AssocHighlightColor: int
    ReadingDirection: bool


class SessionPdm(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def SetDefaultSeed(self, seedName: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    JtUpdateFromSource: Preferences.SessionPdm.JtUpdateFromSourceType
    MessagesInconsistentRevisions: Preferences.SessionPdm.MessagesInconsistentRevisionsType
    SynchroniseOnLoad: Preferences.SessionPdm.SynchroniseOnLoadType
    SynchroniseOnSave: Preferences.SessionPdm.SynchroniseOnSaveType
    UnpopulatedBehaviour: Preferences.SessionPdm.UnpopulatedBehaviourType
    UnpopulatedWithJtBehaviour: Preferences.SessionPdm.UnpopulatedBehaviourType


    class UnpopulatedBehaviourType(enum.Enum):
        OnSave = 0
        ModifiedPrompt = 1
        ModifiedNoPrompt = 2
        Never = 3
        PreNx4 = 4
    

    class SynchroniseOnSaveType(enum.Enum):
        Complete = 0
        None = 1
    

    class SynchroniseOnLoadType(enum.Enum):
        Complete = 0
        AddWithTransforms = 1
        None = 2
    

    class MessagesInconsistentRevisionsType(enum.Enum):
        None = 0
        Warning = 1
        Error = 2
    

    class JtUpdateFromSourceType(enum.Enum):
        Complete = 0
        None = 1
    

class SessionNXGateway(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AngularTolerance: float
    AttachFidelityCheckData: bool
    AutomaticallyCheckItemRevisions: bool
    HealGeometryOnImport: bool
    IgnoreUpdateOfIdenticalVersions: bool
    LoadConstructionGeometry: bool
    LoadProductManufacturingInformation: bool
    LoadSolidEdgeAssemblyFeatures: bool
    LoadSolidEdgeConstructionGeometry: bool
    LoadSolidEdgeProductManufacturingInformation: bool
    MinimumSmallEdgeLength: float
    OnlyImportDesignParts: bool
    PerformFidelityCheckOnImport: bool
    PreserveNominalGeometry: bool
    ReferenceGeometryImportColor: int
    ReferenceGeometryImportLayer: int
    RemoveDiscontinuity: bool
    RemoveSelfIntersections: bool
    RemoveSmallEdges: bool
    RepairTolerance: float
    RetainFidelityCheckingInformation: bool
    SaveComponentPartFilesDuringLoad: bool
    SuppressSurfaceModification: bool
    Tolerance: float
    UseRepairTolerance: bool
    WireframeGeometryImportColor: int
    WireframeGeometryImportLayer: int


class SessionNavigation(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AdaptiveSpeed: bool
    NavigationSpeed: float
    PerspectiveOnFlyThoughExit: Preferences.SessionNavigation.PerspectiveStatusOnExit


    class PerspectiveStatusOnExit(enum.Enum):
        Retain = 0
        RevertToPreviousState = 1
    

class SessionModeling(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def SetDelayModelUpdatesAndGranularity(self, delayModelUpdates: bool, modelDelayUpdateGranularityOption: Preferences.SessionModeling.ModelDelayUpdateGranilarityType, undoMarkId: Session.UndoMarkId) -> None:
        ...
    def Tag(self) -> Tag: ...

    AccelerationColor: int
    ActivateFeatureGroupWithRollback: bool
    AllowEditingOfDimensionOfInternalSketch: bool
    AssociativeEditFreeForm: bool
    BodyType: Preferences.SessionModeling.BodyTypeOption
    BooleanFaceProperties: Preferences.SessionModeling.BooleanFacePropertiesInheritance
    ConvertAnalyticToConvergentAngularTolerance: float
    ConvertAnalyticToConvergentDistanceTolerance: float
    CurvatureColor: int
    CurveFitMethod: Preferences.SessionModeling.CurveFitMethodType
    DelayModelUpdates: bool
    DeleteChildFeaturesOption: Preferences.SessionModeling.DeleteChildFeaturesOptionType
    DisplayLegacyFeatureName: bool
    DynamicUpdate: Preferences.SessionModeling.DynamicUpdateType
    EditWithRollbackUponDoubleClick: bool
    EnableTrimmedAnimation: bool
    EndpointDisplayColor: int
    EndpointDisplayInheritColor: bool
    EndpointDisplayStyle: Preferences.SessionModeling.EndpointDisplayStyleType
    FreeFormConstructionResult: Preferences.SessionModeling.FreeFormConstructionResultType
    ImmediateChildren: Preferences.SessionModeling.ImmediateChildrenType
    InterruptUpdateOnError: bool
    InterruptUpdateOnMissingReferences: bool
    InterruptUpdateOnWarning: bool
    LinkedAndExtractedGeometryProperties: Preferences.SessionModeling.LinkedAndExtractedGeometryPropertiesInheritance
    MakeCurrentOnError: bool
    MakeDatumsInternal: bool
    MakeSketchesInternal: bool
    ModelDelayUpdateGranilarity: Preferences.SessionModeling.ModelDelayUpdateGranilarityType
    NewFaceProperties: Preferences.SessionModeling.NewFacePropertiesInheritance
    NotifyOnDelete: bool
    PoleDisplayColor: int
    PoleDisplayInheritColor: bool
    PoleDisplayStyle: Preferences.SessionModeling.PoleDisplayStyleType
    PoleEditColor: int
    PoleEditInheritColor: bool
    PoleEditStyle: Preferences.SessionModeling.PoleEditStyleType
    PolylineDisplayColor: int
    PolylineDisplayInheritColor: bool
    PolylineDisplayStyle: Preferences.SessionModeling.PolylineStyleType
    PolylineEditColor: int
    PolylineEditInheritColor: bool
    PolylineEditStyle: Preferences.SessionModeling.PolylineStyleType
    PositionColor: int
    PreviewResolution: Preferences.SessionModeling.PreviewResolutionType
    SaveDataForFeatureEdit: Preferences.SessionModeling.SaveDataForFeatureEditOption
    ShareGeometriesOption: Preferences.SessionModeling.ShareGeometriesOnSaveType
    ShowSimuationUiInModeling: bool
    SketchDefaultAction: Preferences.SessionModeling.SketchDefaultActionType
    SketchEditOption: Preferences.SessionModeling.SketchEditType
    SplineDefaultActionType: Preferences.SessionModeling.SplineDefaultActionTypes
    SurfaceExtension: Preferences.SessionModeling.SurfaceExtensionOption
    TangentColor: int
    TreatOneDegreeBsplineAsPolyline: bool
    UpdateDelayed: bool
    UpdateFailureReportPreference: bool
    UpdatePending: bool
    UseTriangularMesh: bool


    class SurfaceExtensionOption(enum.Enum):
        Linear = 0
        Soft = 1
        Reflective = 2
        Natural = 3
        Arc = 4
    

    class SplineDefaultActionTypes(enum.Enum):
        StudioSpline = 0
        Xform = 1
    

    class SketchEditType(enum.Enum):
        InTaskEnvironment = 0
        Direct = 1
    

    class SketchDefaultActionType(enum.Enum):
        EditWithRollback = 0
        Edit = 1
    

    class ShareGeometriesOnSaveType(enum.Enum):
        DontShare = 0
        Share = 1
    

    class SaveDataForFeatureEditOption(enum.Enum):
        None = 0
        FastRollback = 1
        FastRollbackAndPreviousStateOfFailedFeature = 2
    

    class PreviewResolutionType(enum.Enum):
        None = 0
        Coarse = 1
        Standard = 2
        Fine = 3
        ExtraFine = 4
        SuperFine = 5
        UltraFine = 6
    

    class PolylineStyleType(enum.Enum):
        Solid = 1
        Dashed = 2
        Phantom = 3
        Centerline = 4
        Dotted = 5
        Longdashed = 6
        Dotteddashed = 7
        Eight = 11
        Nine = 12
        Ten = 13
        Eleven = 14
    

    class PoleEditStyleType(enum.Enum):
        Sphere3d = 0
        OpenCircle = 1
        FilledCircle = 2
        PlusSign = 3
        Cross = 4
    

    class PoleDisplayStyleType(enum.Enum):
        None = 0
        OpenCircle = 1
        FilledCircle = 2
        PlusSign = 3
        Cross = 4
    

    class NewFacePropertiesInheritance(enum.Enum):
        Body = 0
        PartDefault = 1
    

    class ModelDelayUpdateGranilarityType(enum.Enum):
        Group = 0
        Feature = 1
    

    class LinkedAndExtractedGeometryPropertiesInheritance(enum.Enum):
        ParentObject = 0
        PartDefault = 1
    

    class ImmediateChildrenType(enum.Enum):
        FirstLevel = 0
        All = 1
    

    class FreeFormConstructionResultType(enum.Enum):
        Plane = 0
        BSurface = 1
    

    class EndpointDisplayStyleType(enum.Enum):
        OpenCircle = 0
        FilledCircle = 1
        PlusSign = 2
        Cross = 3
    

    class DynamicUpdateType(enum.Enum):
        None = 0
        Incremental = 1
        Continuous = 2
    

    class DeleteChildFeaturesOptionType(enum.Enum):
        Yes = 1
        No = 2
        Ask = 3
    

    class CurveFitMethodType(enum.Enum):
        Cubic = 0
        Quintic = 1
        Advanced = 2
    

    class BooleanFacePropertiesInheritance(enum.Enum):
        TargetBody = 0
        ToolBody = 1
    

    class BodyTypeOption(enum.Enum):
        Solid = 0
        Sheet = 1
    

class SessionMeasureRequirements(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    UpdateFrameRate: int
    ViolationAction: Preferences.SessionMeasureRequirements.ActionOnViolation


    class ActionOnViolation(enum.Enum):
        HightlightMeasure = 0
        StopPlayback = 1
    

class SessionDrafting(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AutomaticCustomSymbolUpdate: bool
    DynamicAlignment: bool
    ExtractedEdgeFaceDisplay: Preferences.SessionDrafting.EdgeFaceDisplayType
    ForcedWelcomeMode: int
    GridObject: Preferences.SessionDrafting.GridObjectType
    LoadComponentOnFacetedViewSelection: bool
    LoadComponentOnFacetedViewUpdate: bool
    SmartlightweightViewsLoadComponentOnDemand: bool


    class GridObjectType(enum.Enum):
        Drafting = 0
        Sketch = 1
        Sheetzone = 2
    

    class EdgeFaceDisplayType(enum.Enum):
        DisplayAndEmphasize = 0
        CurvesOnly = 1
    

    class AnnotationStyleType(enum.Enum):
        TextboxAndLeaders = 0
        Detailed = 1
    

class SessionAssemblies(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CheckNewerRevisionsOfTemplatePart: bool
    ComponentMemberSelect: bool
    DisplayUpdateReport: bool
    DragHandlePositionPreference: Preferences.SessionAssemblies.DragHandlePositionOption
    InterpartPositioning: bool
    PartNameAttribute: str
    PartNameStyle: Preferences.SessionAssemblies.PartNameOption
    PositioningTaskCollectionForDesignElements: Preferences.SessionAssemblies.PositioningTaskCollectionOptionForDesignElements
    PreviewComponentOnAdd: bool
    ProductInterfaceEmphasize: bool
    SimplifyPrepopulate: bool
    TemplateOptionForNewAssembly: Preferences.SessionAssemblies.TemplateTypeOptionForNewAssemblyTemplate
    TemplateOptionForNewComponent: Preferences.SessionAssemblies.TemplateTypeOptionForNewComponentTemplate
    TemplateOptionForNewParent: Preferences.SessionAssemblies.TemplateTypeOptionForNewParentTemplate
    TolerantPositioning: bool
    TrueShapeFiltering: bool
    UpdateDesignElementPositionOnLoad: bool
    UpdateStructureOnExpand: bool
    WarnOnDelete: bool
    WarnOnDragDrop: bool
    WorkPartDisplayAsEntirePart: bool
    WorkPartEmphasize: bool
    WorkPartMaintain: bool
    WorkPartWarnOnAutomaticChange: bool


    class TemplateTypeOptionForNewParentTemplate(enum.Enum):
        Gateway = 0
        Assemblies = 1
        SelectFromFile = 2
    

    class TemplateTypeOptionForNewComponentTemplate(enum.Enum):
        Modeling = 0
        Gateway = 1
        Assemblies = 2
        SelectFromFileNew = 3
    

    class TemplateTypeOptionForNewAssemblyTemplate(enum.Enum):
        Gateway = 0
        Assemblies = 1
        SelectFromFileNew = 2
    

    class PositioningTaskCollectionOptionForDesignElements(enum.Enum):
        Work = 0
        Context = 1
    

    class PartNameOption(enum.Enum):
        FileName = 0
        Description = 1
        SpecifiedAttributes = 2
    

    class DragHandlePositionOption(enum.Enum):
        CenterOfBoundingBox = 0
        OriginOfComponent = 1
    

class SessionAppearanceMgrPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def GetDirectoryOfStudioMaterial(self) -> str:
        ...
    def SetDirectoryOfStudioMaterial(self, studioMaterialDirectory: str) -> None:
        ...
    def GetDirectoryOfTexture(self) -> str:
        ...
    def SetDirectoryOfTexture(self, textureDir: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    DispSceneLabels: bool
    DispSeeThru: bool
    ExcludeFromSelection: bool


class SectionViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AssemblyCrossHatching: bool
    Background: bool
    Bendlines: bool
    CrossHatch: bool
    CrosshatchAdjacencyTolarance: float
    Foreground: bool
    HiddenLineHatching: bool
    RestrictCrosshatchAngle: bool
    SectionSheetBodies: bool


class RulePreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def GetSearchLibraries(self) -> str:
        ...
    def SetSearchLibraries(self, userLibraries: str) -> None:
        ...
    def InitializeDisplayToAbsoluteTemperatureFunctionDefinition(self, definition: Preferences.RulePreferences.AbsoluteTemperatureConversionDefinition) -> None:
        ...
    def AddDisplayToAbsoluteTemperatureFunction(self, definition: Preferences.RulePreferences.AbsoluteTemperatureConversionDefinition) -> None:
        ...
    def Tag(self) -> Tag: ...



    class RulePreferencesAbsoluteTemperatureConversionDefinition():
        MathFunctionName: str
        CanReturnUnits: bool
        CanHaveOptionalBaseParameter: bool
        CanHaveOptionalUseUnitsParameter: bool
        OptionLocation: int
        IsDependentOnOptionalParameter: bool
        NotConvertingParameterWithNoOption: bool
        NotConvertingParameterIfOptionIsOff: bool
        IsFinalAdjustmentNotNeccessaryIfUnitless: bool
        DontConvertParameterLastResort: bool
        AddCelsiusToMissingParameters: bool
        def ToString(self) -> str:
            ...
    

    class RulePreferences_AbsoluteTemperatureConversionDefinition():
        mathFunctionName: int
        canReturnUnits: bool
        canHaveOptionalBaseParameter: bool
        canHaveOptionalUseUnitsParameter: bool
        optionLocation: int
        isDependentOnOptionalParameter: bool
        notConvertingParameterWithNoOption: bool
        notConvertingParameterIfOptionIsOff: bool
        isFinalAdjustmentNotNeccessaryIfUnitless: bool
        dontConvertParameterLastResort: bool
        addCelsiusToMissingParameters: bool
    

class RoutingUserPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def GetStringPreference(self, name: str, value: str) -> bool:
        ...
    def SetStringPreference(self, name: str, value: str) -> None:
        ...
    def GetStringArrayPreference(self, name: str, values: str) -> bool:
        ...
    def SetStringArrayPreference(self, name: str, values: str) -> None:
        ...
    def GetIntegerPreference(self, name: str, value: int) -> bool:
        ...
    def SetIntegerPreference(self, name: str, value: int) -> None:
        ...
    def GetIntegerArrayPreference(self, name: str, values: int) -> bool:
        ...
    def SetIntegerArrayPreference(self, name: str, values: int) -> None:
        ...
    def GetDoublePreference(self, name: str, value: float) -> bool:
        ...
    def SetDoublePreference(self, name: str, value: float) -> None:
        ...
    def GetDoubleArrayPreference(self, name: str, values: float) -> bool:
        ...
    def SetDoubleArrayPreference(self, name: str, values: float) -> None:
        ...
    def Tag(self) -> Tag: ...



class RoutingStock(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def SetDefaultStock(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def GetDefaultStock(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def SetPreferredFillerStock(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def GetPreferredFillerStock(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def SetPreferredSpaceReservation(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def GetPreferredSpaceReservation(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def SetPreferredOverstock(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def GetPreferredOverstock(self, stockPart: Routing.CharacteristicList, dataCharx: Routing.CharacteristicList) -> None:
        ...
    def Tag(self) -> Tag: ...

    CurrentTile: str
    DefaultStockStyle: Routing.StockStyle
    DeleteOverstock: bool
    SpaceReservationMode: Preferences.RoutingStock.SpaceReservationModeFlag
    SpaceReservationTranslucency: int
    StockAnchor: str
    StockFolder: str
    StockMode: Preferences.RoutingStock.StockModeFlag


    class StockModeFlag(enum.Enum):
        LegacyStock = 0
        StockAsComponent = 1
    

    class SpaceReservationModeFlag(enum.Enum):
        LegacySpaceReservation = 0
        SpaceReservationAsComponent = 1
    

class RoutingPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def GetAllAvailableDisciplines(self) -> str:
        ...
    def Tag(self) -> Tag: ...

    CurrentDiscipline: str
    DisciplineIndex: int
    DisplayConnectedPorts: bool
    InsulationTranslucency: int
    OffsetExpressionString: str
    PortLength: float
    SpaceReservationTranslucency: int
    StockComponentFolder: str
    StockTranslucency: int
    SubdivideSegmentForFixturePartPlacement: bool
    UsePreferredPortPlacement: bool


class RoutingPath(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def GetAllowedCurves(self) -> typing.List[Preferences.RoutingPath.CurveType]:
        ...
    def SetAllowedCurves(self, allowedCurves: typing.List[Preferences.RoutingPath.CurveType]) -> None:
        ...
    def GetAllowedCorners(self) -> typing.List[Preferences.RoutingPath.AllowedCornerType]:
        ...
    def SetAllowedCorners(self, allowedCorners: typing.List[Preferences.RoutingPath.AllowedCornerType]) -> None:
        ...
    def GetDefaultCorner(self) -> Preferences.RoutingPath.DefaultCornerType:
        ...
    def SetDefaultCorner(self, defaultCorner: Preferences.RoutingPath.DefaultCornerType) -> None:
        ...
    def GetBendRadiusMethod(self) -> Preferences.RoutingPath.RadiusMethod:
        ...
    def SetBendRadiusMethod(self, radiusMethod: Preferences.RoutingPath.RadiusMethod) -> None:
        ...
    def GetBendRadius(self) -> float:
        ...
    def SetBendRadius(self, bendRadius: float) -> None:
        ...
    def GetBendRadiusUnits(self) -> Preferences.RoutingPath.RadiusUnits:
        ...
    def SetBendRadiusUnits(self, radiusUnits: Preferences.RoutingPath.RadiusUnits) -> None:
        ...
    def GetBendRatio(self) -> float:
        ...
    def SetBendRatio(self, bendRatio: float) -> None:
        ...
    def GetBendRatioToAttribute(self) -> float:
        ...
    def SetBendRatioToAttribute(self, bendRatioToAttribute: float) -> None:
        ...
    def GetBendAttributeName(self) -> str:
        ...
    def SetBendAttributeName(self, bendAttributeName: str) -> None:
        ...
    def GetBendRadiusTable(self) -> str:
        ...
    def SetBendRadiusTable(self, bendTableSpreadsheet: str) -> None:
        ...
    def GetBendRadiusTableDataForStock(self, stockPartNumber: str) -> typing.List[Routing.CharacteristicList]:
        ...
    def GetCreateSmartRcps(self) -> Preferences.RoutingPath.CreateSmartRcps:
        ...
    def SetCreateSmartRcps(self, createSmart: Preferences.RoutingPath.CreateSmartRcps) -> None:
        ...
    def GetMergeDuplicateRcps(self) -> Preferences.RoutingPath.MergeDupRcps:
        ...
    def SetMergeDuplicateRcps(self, mergeDuplicates: Preferences.RoutingPath.MergeDupRcps) -> None:
        ...
    def GetConfirmBranchSelection(self) -> Preferences.RoutingPath.ConfirmBranchSel:
        ...
    def SetConfirmBranchSelection(self, confirmBranchSel: Preferences.RoutingPath.ConfirmBranchSel) -> None:
        ...
    def GetStockOffsetExpression(self) -> str:
        ...
    def SetStockOffsetExpression(self, stockOffsetExp: str) -> None:
        ...
    def GetContinueUpdateOnError(self) -> Preferences.RoutingPath.ContinueUpdOnError:
        ...
    def SetContinueUpdateOnError(self, update: Preferences.RoutingPath.ContinueUpdOnError) -> None:
        ...
    def GetCreateSlopeConstraints(self) -> Preferences.RoutingPath.CreateSlopeConstraints:
        ...
    def SetCreateSlopeConstraints(self, createSlopeConstraints: Preferences.RoutingPath.CreateSlopeConstraints) -> None:
        ...
    def GetCurveChainingMethod(self) -> Preferences.RoutingPath.ChainMethod:
        """[Obsolete("Deprecated in NX1926.0.0.  No replacement.")"""
        ...
    def SetCurveChainingMethod(self, chainMethod: Preferences.RoutingPath.ChainMethod) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  No replacement.")"""
        ...
    def GetChainableCurveTypes(self) -> typing.List[Preferences.RoutingPath.CurveType]:
        """[Obsolete("Deprecated in NX1926.0.0.  No replacement.")"""
        ...
    def SetChainableCurveTypes(self, chainableCurveTypes: typing.List[Preferences.RoutingPath.CurveType]) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  No replacement.")"""
        ...
    def GetOccurrenceChainable(self) -> Preferences.RoutingPath.OccChainable:
        """[Obsolete("Deprecated in NX1926.0.0.  No replacement.")"""
        ...
    def SetOccurrenceChainable(self, occChainable: Preferences.RoutingPath.OccChainable) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  No replacement.")"""
        ...
    def GetDisplayRcps(self) -> Preferences.RoutingPath.DisplayObject:
        ...
    def SetDisplayRcps(self, displayRcps: Preferences.RoutingPath.DisplayObject) -> None:
        ...
    def GetDisplayPorts(self) -> Preferences.RoutingPath.DisplayObject:
        ...
    def SetDisplayPorts(self, displayPorts: Preferences.RoutingPath.DisplayObject) -> None:
        ...
    def GetDisplaySegmentConstraints(self) -> Preferences.RoutingPath.DisplayObject:
        ...
    def SetDisplaySegmentConstraints(self, displayConstraints: Preferences.RoutingPath.DisplayObject) -> None:
        ...
    def GetDisplayAnchors(self) -> Preferences.RoutingPath.DisplayObject:
        ...
    def SetDisplayAnchors(self, displayAnchors: Preferences.RoutingPath.DisplayObject) -> None:
        ...
    def GetDisplayPortLength(self) -> float:
        ...
    def SetDisplayPortLength(self, displayPortLength: float) -> None:
        ...
    def GetHealPathCurveType(self) -> Preferences.RoutingPath.CurveType:
        ...
    def SetHealPathCurveType(self, healPathCurveType: Preferences.RoutingPath.CurveType) -> None:
        ...
    def GetCreateSplineTangency(self) -> Preferences.RoutingPath.CreateTangency:
        ...
    def SetCreateSplineTangency(self, applyTangency: Preferences.RoutingPath.CreateTangency) -> None:
        ...
    def GetCreateNewPointsOnSubdivide(self) -> Preferences.RoutingPath.AddPointsToSpline:
        ...
    def SetCreateNewPointsOnSubdivide(self, addPoints: Preferences.RoutingPath.AddPointsToSpline) -> None:
        ...
    def GetDisplayConnectedPorts(self) -> Preferences.RoutingPath.DisplayObject:
        ...
    def SetDisplayConnectedPorts(self, displayConnectedPorts: Preferences.RoutingPath.DisplayObject) -> None:
        ...
    def Tag(self) -> Tag: ...



    class RadiusUnits(enum.Enum):
        None = 0
        Inches = 1
        Millimeters = 2
    

    class RadiusMethod(enum.Enum):
        Radius = 0
        Ratio = 1
        Table = 2
        InnerRadius = 3
        RatioToAttribute = 4
    

    class OccChainable(enum.Enum):
        False = 0
        True = 1
    

    class MergeDupRcps(enum.Enum):
        False = 0
        True = 1
    

    class DisplayObject(enum.Enum):
        False = 0
        True = 1
    

    class DefaultCornerType(enum.Enum):
        None = -1
        Bend = 0
        Miter = 1
        BendTable = 2
    

    class CurveType(enum.Enum):
        Line = 0
        Arc = 1
        Spline = 2
    

    class CreateTangency(enum.Enum):
        False = 0
        True = 1
    

    class CreateSmartRcps(enum.Enum):
        False = 0
        True = 1
    

    class CreateSlopeConstraints(enum.Enum):
        False = 0
        True = 1
    

    class ContinueUpdOnError(enum.Enum):
        False = 0
        True = 1
    

    class ConfirmBranchSel(enum.Enum):
        False = 0
        True = 1
    

    class ChainMethod(enum.Enum):
        NoBranch = 0
        Continuous = 1
        Tangent = 2
        Cycle = 3
        MinDist = 4
        MaxDist = 5
    

    class AllowedCornerType(enum.Enum):
        None = 0
        Bend = 1
        Cope = 2
        Miter = 3
        Sbend = 4
    

    class AddPointsToSpline(enum.Enum):
        False = 0
        True = 1
    

class RoutingPartLibrary(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingPart) -> None: ...
    def GetRoot(self) -> str:
        ...
    def GetFilteredRoot(self, rootType: Preferences.RoutingPartLibrary.RootType) -> str:
        ...
    def GetChildrenNodes(self, parent: str) -> str:
        ...
    def GetNodeType(self, node: str) -> Preferences.RoutingPartLibrary.NodeType:
        ...
    def GetTableDefinition(self, node: str) -> typing.List[Preferences.RoutingPartLibrary.Column]:
        ...
    def GetPartDefinition(self, node: str) -> Routing.CharacteristicList:
        ...
    def CreateCriteria(self) -> Routing.CharacteristicList:
        ...
    def MatchCriteria(self, startNode: str, criteria: Routing.CharacteristicList) -> typing.List[Routing.CharacteristicList]:
        ...
    def MatchCriteriaWithFilter(self, startNode: str, criteria: Routing.CharacteristicList) -> typing.List[Routing.CharacteristicList]:
        ...
    def FilterOnCurrentSpecifications(self, match: Routing.CharacteristicList, partClasses: str) -> bool:
        ...
    def Tag(self) -> Tag: ...



    class RootType(enum.Enum):
        Top = 0
        Stock = 1
        Wire = 2
        Part = 3
    

    class NodeType(enum.Enum):
        Normal = 0
        Table = 1
        Part = 2
    

    class ColumnType(enum.Enum):
        Integer = 0
        Real = 1
        String = 4
    

    class ColumnStatus(enum.Enum):
        NotHidden = 0
        Hidden = 1
    

    class RoutingPartLibraryColumn():
        Name: str
        Hidden: Preferences.RoutingPartLibrary.ColumnStatus
        Type: Preferences.RoutingPartLibrary.ColumnType
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, Hidden: Preferences.RoutingPartLibrary.ColumnStatus, Type: Preferences.RoutingPartLibrary.ColumnType) -> None: ...
    

    class RoutingPartLibrary_Column():
        name: int
        hidden: Preferences.RoutingPartLibrary.ColumnStatus
        type: Preferences.RoutingPartLibrary.ColumnType
    

class RoutingPart(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def SetPreferredPortName(self, desiredPort: str) -> None:
        ...
    def GetPreferredPortName(self) -> str:
        ...
    def SetPreferredPortAttribute(self, attributeName: str, attributeValue: str) -> None:
        ...
    def GetPreferredPortAttribute(self, attributeName: str, attributeValue: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    PartLibrary: Preferences.RoutingPartLibrary
    BomDetailLevelFlag: Preferences.RoutingPart.DetailLevel
    BomFormatPart: str
    DefaultElbowNode: str
    FabricationNumberingFlag: Preferences.RoutingPart.FabricationNumbering
    InvalidSequenceCharacters: str
    Layer: int
    MaximumSolutions: int
    PreferredPortMethodFlag: Preferences.RoutingPart.PreferredPortMethod
    StockLengthDisplayFlag: Preferences.RoutingPart.StockLengthDisplay
    UsePreferredPortFlag: Preferences.RoutingPart.UsePreferredPort


    class UsePreferredPort(enum.Enum):
        False = 0
        True = 1
    

    class StockLengthDisplay(enum.Enum):
        Sum = 0
        Item = 1
    

    class PreferredPortMethod(enum.Enum):
        Attribute = 0
        Name = 1
    

    class FabricationNumbering(enum.Enum):
        Sequence = 0
        Original = 1
    

    class DetailLevel(enum.Enum):
        Summary = 0
        Itemized = 1
    

class RoutingMechanical(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def GetIsInitialized(self) -> bool:
        ...
    def GetRunTypeNames(self) -> str:
        ...
    def GetLineFontIndices(self) -> int:
        ...
    def GetLineFonts(self) -> str:
        ...
    def GetLineWidths(self) -> int:
        ...
    def GetLineColorTypes(self) -> typing.List[Preferences.RoutingMechanical.LineColorType]:
        ...
    def GetLineColors(self) -> str:
        ...
    def Tag(self) -> Tag: ...



    class LineColorType(enum.Enum):
        Unknown = -1
        Name = 0
        Index = 1
        Rgb = 2
        Hex = 3
        Max = 4
    

class RoutingLogical(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def Tag(self) -> Tag: ...

    FlowArrowParameterA: float
    FlowArrowParameterB: float
    FlowArrowType: Preferences.RoutingLogical.FlowArrowEnumType


    class FlowArrowEnumType(enum.Enum):
        Open = 0
        Closed = 1
        Filled = 2
    

class RoutingElectrical(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def GetDefaultHarnessName(self) -> str:
        ...
    def SetDefaultHarnessName(self, defaultHarnessName: str) -> None:
        ...
    def GetComponentMatchColumnHeading(self) -> str:
        ...
    def SetComponentMatchColumnHeading(self, columnHeading: str) -> None:
        ...
    def GetComponentMatchComponentAttributeTitle(self) -> str:
        ...
    def SetComponentMatchComponentAttributeTitle(self, componentAttributeTitle: str) -> None:
        ...
    def GetFilterBlankingAttribute(self) -> str:
        ...
    def SetFilterBlankingAttribute(self, attributeName: str) -> None:
        ...
    def GetFilterFormatFileName(self) -> str:
        ...
    def SetFilterFormatFileName(self, filterFormatFileName: str) -> None:
        ...
    def GetFormboardFrameSizes(self) -> str:
        ...
    def SetFormboardFrameSizes(self, frameSizes: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    AutoRouteStockStyle: Routing.StockStyle
    AutomaticRouteLevel: bool
    BundleColor: int
    ComponentMatchMethod: Preferences.RoutingElectrical.ComponentMatchType
    CreateTerminalsOption: Preferences.RoutingElectrical.CreateTerminalsType
    DefaultJumperLength: str
    ExportFormatInLegacyFile: bool
    FormboardSynchronizationLengthTolerance: float
    HighlightWire: bool
    RecordNetlistHistory: bool
    ReportRouteErrors: bool
    StandaloneFilterFormatFile: bool
    TerminalSegmentSolidDisplay: bool


    class CreateTerminalsType(enum.Enum):
        All = 0
        Listed = 1
        Routed = 2
    

    class ComponentMatchType(enum.Enum):
        FileName = 0
        ComponentName = 1
        AttributeName = 2
    

class RoutingCharacteristics(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.RoutingApplicationView) -> None: ...
    def GetStockRequiredCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def GetComponentRequiredCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def GetStockOptionalCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def GetComponentOptionalCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def GetDestintationCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def GetStockCharacteristicValues(self) -> Routing.CharacteristicList:
        ...
    def UpdateStockCharacteristicValues(self, values: Routing.CharacteristicList) -> None:
        ...
    def GetComponentCharacteristicValues(self) -> Routing.CharacteristicList:
        ...
    def UpdateComponentCharacteristicValues(self, values: Routing.CharacteristicList) -> None:
        ...
    def GetDefaultElbowCharacteristicValues(self) -> Routing.CharacteristicList:
        ...
    def UpdateDefaultElbowCharacteristicValues(self, values: Routing.CharacteristicList) -> None:
        ...
    def Tag(self) -> Tag: ...



class RoutingApplicationView(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def LoadAppView(self, fileName: str) -> None:
        ...
    def GetDisciplines(self) -> str:
        ...
    def GetSpecifications(self) -> str:
        ...
    def GetRequiredCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def GetOptionalCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def GetFabricationCharacteristics(self) -> typing.List[Routing.CharacteristicList.CharacteristicInformation]:
        ...
    def Tag(self) -> Tag: ...

    PartPreferences: Preferences.RoutingPart
    CharacteristicPreferences: Preferences.RoutingCharacteristics
    RoutingStock: Preferences.RoutingStock
    RoutingPath: Preferences.RoutingPath
    RoutingMechanical: Preferences.RoutingMechanical
    RoutingLogical: Preferences.RoutingLogical
    RoutingElectrical: Preferences.RoutingElectrical
    RoutingUserPreferences: Preferences.RoutingUserPreferences
    ApplicationType: Preferences.RoutingApplicationView.AppType
    CurrentDiscipline: str
    CurrentSpecification: str
    Description: str
    Filename: str
    Name: str


    class AppType(enum.Enum):
        None = 0
        Mechanical = 1
        Electrical = 2
        Logical = 3
        RsdMechanical = 4
        RsdElectrical = 5
    

class ReferenceSetBehavior(enum.Enum):
    None = 0
    Partial = 1
    All = 2


class ProjectedViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...



class PostProcessing(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    NoModelDisplayOnPostviewCreation: bool


class PmiOption(enum.Enum):
    None = 0
    FromModelView = 1
    InDrawingPlaneFromView = 2
    InDrawingPlaneFromPart = 3


class PartVisualizationVisual(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    UpdateHiddenEdge: bool


class PartVisualizationShade(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetShadedViewFacetTolerances(self, shadedViewToleranceSet: Preferences.PartVisualizationShade.ShadedViewToleranceType, edgeTolerance: float, faceTolerance: float, angleTolerance: float) -> None:
        ...
    def SetShadedViewFacetTolerances(self, shadedViewToleranceSet: Preferences.PartVisualizationShade.ShadedViewToleranceType, edgeTolerance: float, faceTolerance: float, angleTolerance: float) -> None:
        ...
    def GetAdvVisViewFacetTolerances(self, advVisViewToleranceSet: Preferences.PartVisualizationShade.AdvViewToleranceType, edgeTolerance: float, faceTolerance: float, angleTolerance: float, widthTolerance: float) -> None:
        ...
    def SetAdvVisViewFacetTolerances(self, advVisViewToleranceSet: Preferences.PartVisualizationShade.AdvViewToleranceType, edgeTolerance: float, faceTolerance: float, angleTolerance: float, widthTolerance: float) -> None:
        ...
    def RegenerateStudioAnalysisViewsFromToleranceChange(self, updateEnvCube: bool) -> None:
        ...
    def RegenerateShadedViewsFromToleranceChange(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    AdvancedVisViewTolerance: Preferences.PartVisualizationShade.AdvViewToleranceType
    AdvancedVisViewUpdateMode: Preferences.PartVisualizationShade.ViewUpdateModeType
    AlignAdvVisViewFacetsAlongEdges: bool
    AlignShadedViewFacetsAlongEdges: bool
    HiddenGeometryColor: int
    ShadedViewTolerance: Preferences.PartVisualizationShade.ShadedViewToleranceType
    ShadedViewUpdateMode: Preferences.PartVisualizationShade.ViewUpdateModeType


    class ViewUpdateModeType(enum.Enum):
        VisibleObject = 0
        VisibleFacesAndCurves = 0
        AllObject = 1
        None = 2
        VisibleBodiesAndCurves = 3
    

    class ShadedViewToleranceType(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        Extrafine = 3
        Ultrafine = 4
        Customize = 5
    

    class ShadedFaceEdge(enum.Enum):
        Off = 0
        BodyColor = 1
        SpecifyColor = 2
    

    class HiddenShadedFaceEdges(enum.Enum):
        Invisible = 0
        Dashed = 1
        HiddenColor = 2
    

    class AdvViewToleranceType(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        Extrafine = 3
        Superfine = 4
        Ultrafine = 5
        Customize = 6
    

class PartVisualizationScreen(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CsysFixedSizeOnScreen: bool
    CsysShowThrough: bool
    PointShowThrough: bool
    TriadLocation: Preferences.PartVisualizationScreen.ViewTriadLocation
    TriadVisibility: bool


    class ViewTriadLocation(enum.Enum):
        BottomLeft = 0
        BottomRight = 1
    

class PartVisualizationPerformance(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    SaveAdvancedDisplayFacets: bool


class PartVisualizationNamesBorders(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CharacterSize: float
    ObjectNameDisplay: Preferences.PartVisualizationNamesBorders.NameDisplay
    ShowModelViewBorders: bool
    ShowModelViewNames: bool


    class NameDisplay(enum.Enum):
        Off = 0
        ViewOfDefinition = 1
        WorkView = 2
        AllViews = 3
        ObjectDisplaySpecific = 4
    

class PartVisualizationLine(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetWidthOptions(self, showWidths: bool, widthScale: float) -> None:
        ...
    def SetWidthOptions(self, showWidths: bool, widthScale: float) -> None:
        ...
    def GetPixelWidths(self, pixelWidths: int) -> None:
        ...
    def SetPixelWidths(self, pixelWidths: int) -> None:
        ...
    def GetPixelWidthOptions(self, useWidthScale: bool, widthScale: float, pixelWidths: int) -> None:
        ...
    def SetPixelWidthOptions(self, useWidthScale: bool, widthScale: float, pixelWidths: int) -> None:
        ...
    def ResetPixelWidthOptions(self) -> None:
        ...
    def RegenerateFromToleranceChange(self, updateModeChanged: bool, studio: bool) -> None:
        ...
    def UpdateLineFontObjects(self, softwareUpdate: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    CurveTolerance: float
    DashSize: float
    LineFontDisplay: Preferences.PartVisualizationLine.LineFontDisplayType
    ShowWidths: bool
    SpaceSize: float
    SymbolSize: float
    WidthScale: float


    class LineFontDisplayType(enum.Enum):
        Software = 0
        Hardware = 1
    

class PartVisualizationEmphasis(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetWireframeBlendOptions(self) -> Preferences.PartVisualizationEmphasis.WireframeBlendOptions:
        ...
    def SetWireframeBlendOptions(self, wireframeBlendOptions: Preferences.PartVisualizationEmphasis.WireframeBlendOptions) -> None:
        ...
    def GetShellOptions(self) -> Preferences.PartVisualizationEmphasis.ShellOptions:
        ...
    def SetShellOptions(self, shellOptions: Preferences.PartVisualizationEmphasis.ShellOptions) -> None:
        ...
    def GetOriginalColorShellOptions(self) -> Preferences.PartVisualizationEmphasis.OriginalColorShellOptions:
        ...
    def SetOriginalColorShellOptions(self, originalColorShellOptions: Preferences.PartVisualizationEmphasis.OriginalColorShellOptions) -> None:
        ...
    def GetLayersOptions(self) -> Preferences.PartVisualizationEmphasis.LayersOptions:
        ...
    def SetLayersOptions(self, layersOptions: Preferences.PartVisualizationEmphasis.LayersOptions) -> None:
        ...
    def Tag(self) -> Tag: ...

    SeeThruStyle: Preferences.PartVisualizationEmphasis.SeeThruStyleType


    class PartVisualizationEmphasisWireframeBlendOptions():
        BlendColor: NXColor
        BlendPercentage: int
        def ToString(self) -> str:
            ...
        def __init__(self, BlendColor: NXColor, BlendPercentage: int) -> None: ...
    

    class PartVisualizationEmphasisShellOptions():
        Rgb: NXColor.Rgb
        Edges: Preferences.PartVisualizationEmphasis.EdgesType
        EdgesRgb: NXColor.Rgb
        Translucency: int
        def ToString(self) -> str:
            ...
    

    class SeeThruStyleType(enum.Enum):
        Shell = 0
        OriginalColorShell = 1
        Layers = 2
    

    class PartVisualizationEmphasisOriginalColorShellOptions():
        Edges: Preferences.PartVisualizationEmphasis.EdgesType
        EdgesRgb: NXColor.Rgb
        Translucency: int
        def ToString(self) -> str:
            ...
        def __init__(self, Edges: Preferences.PartVisualizationEmphasis.EdgesType, EdgesRgb: NXColor.Rgb, Translucency: int) -> None: ...
    

    class PartVisualizationEmphasisLayersOptions():
        Rgb: NXColor.Rgb
        Edges: Preferences.PartVisualizationEmphasis.EdgesType
        EdgesRgb: NXColor.Rgb
        Translucency: int
        def ToString(self) -> str:
            ...
    

    class EdgesType(enum.Enum):
        Off = 0
        Normal = 1
    

    class PartVisualizationEmphasis_WireframeBlendOptions():
        blendColor: int
        blendPercentage: int
    

class PartVisualizationColorSetting(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def ShuffleRandomColor(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    AttentionColor: int
    HandleActiveColor: NXColor
    HandleColor: NXColor
    HandleOrientxpressColor: NXColor
    HandlePreselectionColor: NXColor
    HandleSelectionColor: NXColor
    HiddenGeometryColor: int
    MonochromeBackgroundColor: int
    MonochromeDisplay: bool
    MonochromeForegroundColor: int
    MonochromePreselectionColor: int
    MonochromeSelectionColor: int
    PreselectionColor: int
    RandomColorDisplay: Preferences.PartVisualizationColorSetting.RandomColorDisplayFor
    RandomColorDisplayOption: bool
    SelectionColor: int
    ShowWidths: bool


    class RandomColorDisplayFor(enum.Enum):
        Faces = 0
        Bodies = 1
    

class PartUserInterface(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    DialogBoxDecimalPlaces: int


class PartSketch(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    AutomaticDimensionColor: int
    ConflictingColor: int
    ConstantDimensionColor: NXColor
    CurveColor: int
    DOFColor: int
    DimensionColor: int
    FullyDefinedColor: int
    GeometricConstraintColor: NXColor
    InactiveSketchColor: int
    LockedObjectColor: NXColor
    MovableCurveColor: NXColor
    NonWorkRegionColor: NXColor
    OutOfDateColor: int
    OverconstrainedColor: int
    PartiallyDefinedColor: int
    ParticipatingDatumColor: int
    PersistentRelationColor: NXColor
    PreviewDimensionColor: NXColor
    ReferenceCurveColor: int
    ReferenceDimensionColor: int
    RelationColor: NXColor
    ShadedRegionColor: NXColor
    UnsolvedCurvesColor: int
    WorkRegionBoundaryColor: NXColor


class PartSheetmetal(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetThickness(self) -> Expression:
        ...
    def SetThickness(self, updateModel: bool, thickness: str) -> None:
        ...
    def GetBendRadius(self) -> Expression:
        ...
    def SetBendRadius(self, updateModel: bool, bendRadius: str) -> None:
        ...
    def GetBendReliefDepth(self) -> Expression:
        ...
    def SetBendReliefDepth(self, updateModel: bool, bendReliefDepth: str) -> None:
        ...
    def GetBendReliefWidth(self) -> Expression:
        ...
    def SetBendReliefWidth(self, updateModel: bool, bendReliefWidth: str) -> None:
        ...
    def GetNeutralFactor(self) -> Expression:
        ...
    def SetNeutralFactor(self, updateModel: bool, neutralFactor: str) -> None:
        ...
    def GetOuterCornerTreatmentValue(self) -> Expression:
        ...
    def SetOuterCornerTreatmentValue(self, updateModel: bool, outerCornerTreatment: str) -> None:
        ...
    def GetOuterCornerTreatmentType(self) -> Features.SheetMetal.FeatureProperty:
        ...
    def SetOuterCornerTreatmentType(self, updateModel: bool, outerCornerTreatmentType: Features.SheetMetal.FeatureProperty) -> None:
        ...
    def GetInnerCornerTreatmentValue(self) -> Expression:
        ...
    def SetInnerCornerTreatmentValue(self, updateModel: bool, innerCornerTreatment: str) -> None:
        ...
    def GetInnerCornerTreatmentType(self) -> Features.SheetMetal.FeatureProperty:
        ...
    def SetInnerCornerTreatmentType(self, updateModel: bool, innerCornerTreatmentType: Features.SheetMetal.FeatureProperty) -> None:
        ...
    def GetIsBsplineSimplifiedInFlatSolid(self) -> bool:
        ...
    def SetIsBsplineSimplifiedInFlatSolid(self, updateModel: bool, isBsplineSimplifiedInFlatSolid: bool) -> None:
        ...
    def GetIsSystemGeneratedBendReliefRemovedInFlatSolid(self) -> bool:
        ...
    def SetIsSystemGeneratedBendReliefRemovedInFlatSolid(self, updateModel: bool, isSystemGeneratedBendReliefRemoved: bool) -> None:
        ...
    def GetMinimumArcToleranceInFlatSolid(self) -> float:
        ...
    def SetMinimumArcToleranceInFlatSolid(self, updateModel: bool, minimumArcToleranceInFlatSolid: float) -> None:
        ...
    def GetDeviationalToleranceInFlatSolid(self) -> float:
        ...
    def SetDeviationalToleranceInFlatSolid(self, updateModel: bool, deviationalToleranceInFlatSolid: float) -> None:
        ...
    def GetBendDefinitionMethodOption(self) -> Preferences.PartSheetmetal.BendDefinitionMethodOptions:
        ...
    def SetBendDefinitionMethodOption(self, updateModel: bool, bendDefinitionMethod: Preferences.PartSheetmetal.BendDefinitionMethodOptions) -> None:
        ...
    def GetBendTable(self) -> str:
        ...
    def SetBendTable(self, updateModel: bool, bendTable: str) -> None:
        ...
    def GetBendAllowanceFormula(self) -> str:
        ...
    def SetBendAllowanceFormula(self, updateModel: bool, bendAllowanceFormula: str) -> None:
        ...
    def GetBendDeductionFormula(self) -> str:
        ...
    def SetBendDeductionFormula(self, updateModel: bool, bendDeductionFormula: str) -> None:
        ...
    def GetSecondaryToolName(self) -> str:
        ...
    def SetSecondaryToolName(self, updateModel: bool, secondaryToolName: str) -> None:
        ...
    def GetMaterialNames(self) -> str:
        ...
    def GetMaterial(self) -> str:
        ...
    def GetMaterialProperties(self, materialName: str, propertyNames: str) -> str:
        ...
    def SetMaterial(self, updateModel: bool, standardName: str) -> None:
        ...
    def Commit(self) -> None:
        ...
    def GetFlatPatternObjectTypeDisplay(self, objectType: Preferences.PartSheetmetal.FlatPatternObjectType) -> Preferences.PartSheetmetal.FlatPatternObjectTypeDisplay:
        ...
    def SetFlatPatternObjectTypeDisplay(self, updateModel: bool, objectType: Preferences.PartSheetmetal.FlatPatternObjectType, displayData: Preferences.PartSheetmetal.FlatPatternObjectTypeDisplay) -> None:
        ...
    def GetTabCurveTypeDisplayData(self, curveType: Preferences.PartSheetmetal.TabCurveType) -> Preferences.PartSheetmetal.TabCurveTypeDisplayData:
        ...
    def SetTabCurveTypeDisplayData(self, updateModel: bool, curveType: Preferences.PartSheetmetal.TabCurveType, displayData: Preferences.PartSheetmetal.TabCurveTypeDisplayData) -> None:
        ...
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> Preferences.PartSheetmetal.FlatPatternCalloutTypeDisplay:
        ...
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: Preferences.PartSheetmetal.FlatPatternCalloutTypeDisplay) -> None:
        ...
    def GetFlatPatternAllObjectTypeDisplay(self, displayData: typing.List[Preferences.PartSheetmetal.FlatPatternObjectTypeDisplay]) -> None:
        ...
    def GetFlatPatternAllCalloutTypeDisplay(self, displayData: typing.List[Preferences.PartSheetmetal.FlatPatternCalloutTypeDisplay]) -> None:
        ...
    def GetMaintainCircularShapeForHolesInFlatSolid(self) -> bool:
        ...
    def SetMaintainCircularShapeForHolesInFlatSolid(self, updateModel: bool, isMaintainCircularShapeForHoles: bool) -> None:
        ...
    def GetMinimumToolClearance(self) -> Expression:
        ...
    def SetMinimumToolClearance(self, updateModel: bool, minToolClearance: str) -> None:
        ...
    def GetMinimumWebLength(self) -> Expression:
        ...
    def SetMinimumWebLength(self, updateModel: bool, minWebLength: str) -> None:
        ...
    def GetToolNames(self) -> str:
        ...
    def GetTool(self) -> str:
        ...
    def GetToolProperties(self, toolName: str, propertyNames: str) -> str:
        ...
    def SetTool(self, updateModel: bool, standardName: str) -> None:
        ...
    def GetFlexibleCableTopFaceColor(self) -> NXColor:
        ...
    def SetFlexibleCableTopFaceColor(self, topFaceColor: NXColor) -> None:
        ...
    def GetFlexibleCableBottomFaceColor(self) -> NXColor:
        ...
    def SetFlexibleCableBottomFaceColor(self, bottomFaceColor: NXColor) -> None:
        ...
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> str:
        ...
    def SetFlatPatternCalloutTypeContents(self, calloutType: str, contents: str) -> None:
        ...
    def GetFlatPatternCalloutOrientationType(self) -> Preferences.PartSheetmetal.FlatPatternCalloutOrientationType:
        ...
    def SetFlatPatternCalloutOrientationType(self, orientation: Preferences.PartSheetmetal.FlatPatternCalloutOrientationType) -> None:
        ...
    def GetStationaryRadius(self) -> Expression:
        ...
    def SetStationaryRadius(self, updateModel: bool, stationaryRadius: str) -> None:
        ...
    def GetOffsetRadius(self) -> Expression:
        ...
    def SetOffsetRadius(self, updateModel: bool, offsetRadius: str) -> None:
        ...
    def GetDistanceThreshold(self) -> Expression:
        ...
    def SetDistanceThreshold(self, updateModel: bool, distanceThreshold: str) -> None:
        ...
    def GetDepthThreshold(self) -> Expression:
        ...
    def SetDepthThreshold(self, updateModel: bool, depthThreshold: str) -> None:
        ...
    def GetHoleTreatmentDiameter(self) -> Expression:
        ...
    def SetHoleTreatmentDiameter(self, updateModel: bool, diameter: str) -> None:
        ...
    def GetHoleTreatmentType(self) -> Features.SheetMetal.FeatureProperty:
        ...
    def SetHoleTreatmentType(self, updateModel: bool, holeTreatmentType: Features.SheetMetal.FeatureProperty) -> None:
        ...
    def GetFlatPatternCalloutOffsetDistance(self) -> float:
        ...
    def SetFlatPatternCalloutOffsetDistance(self, calloutOffset: float) -> None:
        ...
    def SetParameterEntryType(self, updateModel: bool, parameterEntryType: Preferences.PartSheetmetal.ParameterEntryType) -> None:
        ...
    def GetParameterEntryType(self) -> Preferences.PartSheetmetal.ParameterEntryType:
        ...
    def SetPhysicalMaterialIntegrationFlag(self, setPhysicalMaterialIntegrationFlag: bool) -> None:
        ...
    def GetPhysicalMaterialIntegrationFlag(self) -> bool:
        ...
    def GetFlatSolidColor(self) -> int:
        ...
    def SetFlatSolidColor(self, updateModel: bool, flatSolidColor: int) -> None:
        ...
    def GetFlatSolidLayer(self) -> int:
        ...
    def SetFlatSolidLayer(self, updateModel: bool, flatSolidLayer: int) -> None:
        ...
    def Tag(self) -> Tag: ...



    class PartSheetmetalTabCurveTypeDisplayData():
        Type: Preferences.PartSheetmetal.TabCurveType
        IsEnabled: int
        Color: NXColor
        Font: DisplayableObject.ObjectFont
        Width: DisplayableObject.ObjectWidth
        def ToString(self) -> str:
            ...
    

    class TabCurveType(enum.Enum):
        BendCenterLine = 0
        BendTangentLine = 1
    

    class ParameterEntryType(enum.Enum):
        Value = 0
        MaterialTable = 1
        ToolIdTable = 2
    

    class PartSheetmetalFlatPatternObjectTypeDisplay():
        Type: Preferences.PartSheetmetal.FlatPatternObjectType
        IsEnabled: int
        Color: NXColor
        Layer: int
        Font: DisplayableObject.ObjectFont
        Width: DisplayableObject.ObjectWidth
        def ToString(self) -> str:
            ...
    

    class FlatPatternObjectType(enum.Enum):
        BendCenterLine = 0
        BendUpCenterLine = 1
        BendDownCenterLine = 2
        BendTangentLine = 3
        OuterMoldLine = 4
        InnerMoldLine = 5
        ExteriorCurves = 6
        InteriorCurves = 7
        InteriorCutoutCurves = 8
        InteriorFeatureCurves = 9
        StrikePoint = 10
        LighteningHoleCenter = 11
        JoggleLine = 12
        AddedTopGeometry = 13
        AddedBottomGeometry = 14
        ToolMarker = 15
        Hole = 16
        Centermark = 17
    

    class PartSheetmetalFlatPatternCalloutTypeDisplay():
        Type: str
        IsEnabled: int
        Name: str
        def ToString(self) -> str:
            ...
        def __init__(self, Type: str, IsEnabled: int, Name: str) -> None: ...
    

    class FlatPatternCalloutOrientationType(enum.Enum):
        Leadered = 0
        Aligned = 1
    

    class BendDefinitionMethodOptions(enum.Enum):
        NeutralFactorValue = 0
        BendTable = 1
        BendAllowanceFormula = 2
        MaterialTable = 3
        ToolTable = 4
        BendAllowanceTable = 5
        BendDeductionTable = 6
        BendDeductionFormula = 7
        Din6935Formula = 8
    

    class PartSheetmetal_TabCurveTypeDisplayData():
        type: Preferences.PartSheetmetal.TabCurveType
        is_enabled: int
        color: int
        font: DisplayableObject.ObjectFont
        width: DisplayableObject.ObjectWidth
    

    class PartSheetmetal_FlatPatternObjectTypeDisplay():
        type: Preferences.PartSheetmetal.FlatPatternObjectType
        is_enabled: int
        color: int
        layer: int
        font: DisplayableObject.ObjectFont
        width: DisplayableObject.ObjectWidth
    

    class PartSheetmetal_FlatPatternCalloutTypeDisplay():
        type: int
        is_enabled: int
        name: int
    

class PartPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def Tag(self) -> Tag: ...

    Modeling: Preferences.PartModeling
    Drafting: Preferences.PartDrafting
    ObjectPreferences: Preferences.PartObject
    UserInterface: Preferences.PartUserInterface
    VisualVisualization: Preferences.PartVisualizationVisual
    LineVisualization: Preferences.PartVisualizationLine
    NamesBorderVisualization: Preferences.PartVisualizationNamesBorders
    ColorSettingVisualization: Preferences.PartVisualizationColorSetting
    ShadeVisualization: Preferences.PartVisualizationShade
    PartSheetmetal: Preferences.PartSheetmetal
    PartFlexiblePrintedCircuitDesign: Preferences.PartFlexiblePrintedCircuitDesign
    PartAeroSheetmetal: Preferences.PartAeroSheetmetal
    PartSketch: Preferences.PartSketch
    DraftingPreference: Preferences.DraftingPreferenceManager
    EmphasisVisualization: Preferences.PartVisualizationEmphasis
    PerformanceVisualization: Preferences.PartVisualizationPerformance
    ScreenVisualization: Preferences.PartVisualizationScreen
    AppearanceMgmtPreference: Preferences.PartAppearanceMgrPreference
    Workplane: Preferences.WorkPlane


class PartObject(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetColor(self, type: Preferences.PartObject.ObjectType) -> int:
        ...
    def SetColor(self, type: Preferences.PartObject.ObjectType, color: int) -> None:
        ...
    def GetLineFont(self, type: Preferences.PartObject.ObjectType) -> Preferences.PartObject.LineFontType:
        ...
    def SetLineFont(self, type: Preferences.PartObject.ObjectType, lineFont: Preferences.PartObject.LineFontType) -> None:
        ...
    def GetWidth(self, type: Preferences.PartObject.ObjectType) -> Preferences.PartObject.WidthType:
        ...
    def SetWidth(self, type: Preferences.PartObject.ObjectType, width: Preferences.PartObject.WidthType) -> None:
        ...
    def ConvertColorNumberToRGBValue(self, colorNumber: int) -> Preferences.ViewVisualizationSpecialEffects.ColorRGB:
        ...
    def ConvertRGBValueToColorNumber(self, fogColorRgbValue: Preferences.ViewVisualizationSpecialEffects.ColorRGB) -> int:
        ...
    def GetLegacyLineWidthMap(self, newLineWidths: typing.List[Preferences.PartObject.WidthType]) -> None:
        ...
    def SetLegacyLineWidthMap(self, newLineWidths: typing.List[Preferences.PartObject.WidthType]) -> None:
        ...
    def MigrateLegacyLineWidths(self) -> bool:
        ...
    def Tag(self) -> Tag: ...

    FaceAnalysis: bool
    PartiallyShaded: bool
    PointSymbol: int
    Translucency: int


    class WidthType(enum.Enum):
        PartDefault = 1
        ThinWidth = 2
        NormalWidth = 3
        ThickWidth = 4
        WidthOne = 5
        WidthTwo = 6
        WidthThree = 7
        WidthFour = 8
        WidthFive = 9
        WidthSix = 10
        WidthSeven = 11
        WidthEight = 12
        WidthNine = 13
    

    class ObjectType(enum.Enum):
        General = 0
        Line = 1
        Arc = 2
        Conic = 3
        Spline = 4
        Solidbody = 5
        Sheetbody = 6
        Datum = 7
        Point = 8
        CoordinateSystem = 9
        AllButDefault = 10
        DatumCsys = 11
        Traceline = 12
        InfiniteLine = 13
        PointCloud = 14
    

    class LineFontType(enum.Enum):
        PartDefault = 1
        Solid = 2
        Dashed = 3
        Phantom = 4
        Centerline = 5
        Dotted = 6
        LongDashed = 7
        DottedDashed = 8
        Eight = 9
        Nine = 10
        Ten = 11
        Eleven = 12
    

    class ColorSelection(enum.Enum):
        NoChange = 0
        DefaultColor = 1
        Color = 2
    

class PartModeling(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetHistoryMode(self) -> bool:
        ...
    def SetHistoryMode(self) -> None:
        ...
    def SetHistoryFreeMode(self) -> None:
        ...
    def GetKeepLocalFeatures(self) -> bool:
        ...
    def SetKeepLocalFeatures(self, keepLocalFeatures: bool) -> None:
        ...
    def GetIsSavedByWebApp(self) -> bool:
        ...
    def SetIsSavedByWebApp(self, isSavedByWebApp: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    AngleToleranceData: float
    C0KnotLineColor: int
    C0KnotLineFont: Preferences.PartModeling.GridKnotLineFontType
    C0KnotUseBodyColor: bool
    C0KnotUseBodyFont: bool
    C1KnotLineColor: int
    C1KnotLineFont: Preferences.PartModeling.GridKnotLineFontType
    C1KnotUseBodyColor: bool
    C1KnotUseBodyFont: bool
    C2KnotLineColor: int
    C2KnotLineFont: Preferences.PartModeling.GridKnotLineFontType
    C2KnotUseBodyColor: bool
    C2KnotUseBodyFont: bool
    ConvertAnalyticToConvergentAngularTolerance: float
    ConvertAnalyticToConvergentDistanceTolerance: float
    ConvertAnalyticToConvergentMaximumChordLength: float
    ConvertAnalyticToConvergentMaximumFacetWidth: float
    CurveCurvatureDisplay: Preferences.PartModeling.CurveCurvatureDisplayType
    CurveCurvatureShowCap: bool
    CurveCurvatureStyle: int
    CutViewUpdateDelayed: bool
    Density: float
    DensityUnit: Preferences.PartModeling.DensityUnitType
    DisplayCurveCurvatureOutside: bool
    DistanceToleranceData: float
    GridLineColor: int
    GridLineFont: Preferences.PartModeling.GridKnotLineFontType
    GridLinesUCount: int
    GridLinesVCount: int
    GridResolution: Preferences.PartModeling.GridResolutionType
    GridUseBodyColor: bool
    GridUseBodyFont: bool
    MaxChordLengthOption: bool
    MaxFacetWidthOption: bool
    OptimizeCurve: bool
    OptimizeCurveAngleToleranceFactor: float
    OptimizeCurveDistanceToleranceFactor: float
    OptimizeCurveToleranceFactor: float
    TreatOneDegreeBsplineAsPolyline: bool


    class GridResolutionType(enum.Enum):
        None = 0
        Coarse = 1
        Standard = 2
        Fine = 3
        ExtraFine = 4
        UltraFine = 5
    

    class GridKnotLineFontType(enum.Enum):
        Solid = 1
        Dashed = 2
        Phantom = 3
        Centerline = 4
        Dotted = 5
        LongDashed = 6
        DottedDashed = 7
        Eight = 11
        Nine = 12
        Ten = 13
        Eleven = 14
    

    class DensityUnitType(enum.Enum):
        LbPerCuInch = 0
        LbPerCuFeet = 1
        GmPerCuCm = 2
        KgPerCuMeter = 3
    

    class CurveCurvatureDisplayType(enum.Enum):
        Comb = 0
        RadiusOfComb = 1
    

class PartFlexiblePrintedCircuitDesign(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetThickness(self) -> Expression:
        ...
    def SetThickness(self, updateModel: bool, thickness: str) -> None:
        ...
    def GetBendRadius(self) -> Expression:
        ...
    def SetBendRadius(self, updateModel: bool, bendRadius: str) -> None:
        ...
    def GetBendReliefDepth(self) -> Expression:
        ...
    def SetBendReliefDepth(self, updateModel: bool, bendReliefDepth: str) -> None:
        ...
    def GetBendReliefWidth(self) -> Expression:
        ...
    def SetBendReliefWidth(self, updateModel: bool, bendReliefWidth: str) -> None:
        ...
    def GetNeutralFactor(self) -> Expression:
        ...
    def SetNeutralFactor(self, updateModel: bool, neutralFactor: str) -> None:
        ...
    def GetOuterCornerTreatmentValue(self) -> Expression:
        ...
    def SetOuterCornerTreatmentValue(self, updateModel: bool, outerCornerTreatment: str) -> None:
        ...
    def GetOuterCornerTreatmentType(self) -> Features.SheetMetal.FeatureProperty:
        ...
    def SetOuterCornerTreatmentType(self, updateModel: bool, outerCornerTreatmentType: Features.SheetMetal.FeatureProperty) -> None:
        ...
    def GetInnerCornerTreatmentValue(self) -> Expression:
        ...
    def SetInnerCornerTreatmentValue(self, updateModel: bool, innerCornerTreatment: str) -> None:
        ...
    def GetInnerCornerTreatmentType(self) -> Features.SheetMetal.FeatureProperty:
        ...
    def SetInnerCornerTreatmentType(self, updateModel: bool, innerCornerTreatmentType: Features.SheetMetal.FeatureProperty) -> None:
        ...
    def GetIsBsplineSimplifiedInFlatSolid(self) -> bool:
        ...
    def SetIsBsplineSimplifiedInFlatSolid(self, updateModel: bool, isBsplineSimplifiedInFlatSolid: bool) -> None:
        ...
    def GetIsSystemGeneratedBendReliefRemovedInFlatSolid(self) -> bool:
        ...
    def SetIsSystemGeneratedBendReliefRemovedInFlatSolid(self, updateModel: bool, isSystemGeneratedBendReliefRemoved: bool) -> None:
        ...
    def GetMinimumArcToleranceInFlatSolid(self) -> float:
        ...
    def SetMinimumArcToleranceInFlatSolid(self, updateModel: bool, minimumArcToleranceInFlatSolid: float) -> None:
        ...
    def GetDeviationalToleranceInFlatSolid(self) -> float:
        ...
    def SetDeviationalToleranceInFlatSolid(self, updateModel: bool, deviationalToleranceInFlatSolid: float) -> None:
        ...
    def GetMaterialNames(self) -> str:
        ...
    def GetMaterial(self) -> str:
        ...
    def GetMaterialProperties(self, materialName: str, propertyNames: str) -> str:
        ...
    def SetMaterial(self, updateModel: bool, standardName: str) -> None:
        ...
    def GetFlatPatternObjectTypeDisplay(self, objectType: Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternObjectType) -> Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay:
        ...
    def SetFlatPatternObjectTypeDisplay(self, updateModel: bool, objectType: Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternObjectType, displayData: Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay) -> None:
        ...
    def GetPlanarSegmentCurveTypeDisplayData(self, curveType: Preferences.PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType) -> Preferences.PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveTypeDisplayData:
        ...
    def SetPlanarSegmentCurveTypeDisplayData(self, updateModel: bool, curveType: Preferences.PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType, displayData: Preferences.PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveTypeDisplayData) -> None:
        ...
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay:
        ...
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay) -> None:
        ...
    def GetFlatPatternAllObjectTypeDisplay(self, displayData: typing.List[Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay]) -> None:
        ...
    def GetFlatPatternAllCalloutTypeDisplay(self, displayData: typing.List[Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay]) -> None:
        ...
    def Commit(self) -> None:
        ...
    def GetFlexibleCableConductorWidth(self) -> Expression:
        ...
    def SetFlexibleCableConductorWidth(self, conductorWidth: str) -> None:
        ...
    def GetFlexibleCableConductorSpacing(self) -> Expression:
        ...
    def SetFlexibleCableConductorSpacing(self, conductorSpacing: str) -> None:
        ...
    def GetFlexibleCableStrippingLength(self) -> Expression:
        ...
    def SetFlexibleCableStrippingLength(self, strippingLength: str) -> None:
        ...
    def GetFlexibleCableContactFace(self) -> Preferences.PartFlexiblePrintedCircuitDesign.FlexibleCableContactFaceOptions:
        ...
    def SetFlexibleCableContactFace(self, faceOption: Preferences.PartFlexiblePrintedCircuitDesign.FlexibleCableContactFaceOptions) -> None:
        ...
    def GetFlexibleCableTopFaceColor(self) -> NXColor:
        ...
    def SetFlexibleCableTopFaceColor(self, topFaceColor: NXColor) -> None:
        ...
    def GetFlexibleCableBottomFaceColor(self) -> NXColor:
        ...
    def SetFlexibleCableBottomFaceColor(self, bottomFaceColor: NXColor) -> None:
        ...
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> str:
        ...
    def SetFlatPatternCalloutTypeContents(self, calloutType: str, contents: str) -> None:
        ...
    def GetFlatPatternCalloutOrientationType(self) -> Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutOrientationType:
        ...
    def SetFlatPatternCalloutOrientationType(self, orientation: Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutOrientationType) -> None:
        ...
    def GetHoleTreatmentDiameter(self) -> Expression:
        ...
    def SetHoleTreatmentDiameter(self, updateModel: bool, diameter: str) -> None:
        ...
    def GetHoleTreatmentType(self) -> Features.SheetMetal.FeatureProperty:
        ...
    def SetHoleTreatmentType(self, updateModel: bool, holeTreatmentType: Features.SheetMetal.FeatureProperty) -> None:
        ...
    def GetFlatPatternCalloutOffsetDistance(self) -> float:
        ...
    def SetFlatPatternCalloutOffsetDistance(self, calloutOffset: float) -> None:
        ...
    def SetMultiThicknessLayerScheme(self, updateModel: bool, multiHeightLayerScheme: str) -> None:
        ...
    def GetMultiThicknessLayerScheme(self) -> str:
        ...
    def SetParameterEntryType(self, updateModel: bool, parameterEntryType: Preferences.PartFlexiblePrintedCircuitDesign.ParameterEntryType) -> None:
        ...
    def GetParameterEntryType(self) -> Preferences.PartFlexiblePrintedCircuitDesign.ParameterEntryType:
        ...
    def SetPhysicalMaterialIntegrationFlag(self, setPhysicalMaterialIntegrationFlag: bool) -> None:
        ...
    def GetPhysicalMaterialIntegrationFlag(self) -> bool:
        ...
    def GetFlatSolidColor(self) -> int:
        ...
    def SetFlatSolidColor(self, updateModel: bool, flatSolidColor: int) -> None:
        ...
    def GetFlatSolidLayer(self) -> int:
        ...
    def SetFlatSolidLayer(self, updateModel: bool, flatSolidLayer: int) -> None:
        ...
    def GetMaintainCircularShapeForHolesInFlatSolid(self) -> bool:
        ...
    def SetMaintainCircularShapeForHolesInFlatSolid(self, updateModel: bool, isMaintainCircularShapeForHoles: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



    class PartFlexiblePrintedCircuitDesignPlanarSegmentCurveTypeDisplayData():
        Type: Preferences.PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType
        IsEnabled: int
        Color: NXColor
        Font: DisplayableObject.ObjectFont
        Width: DisplayableObject.ObjectWidth
        def ToString(self) -> str:
            ...
    

    class PlanarSegmentCurveType(enum.Enum):
        BendCenterLine = 0
        BendTangentLine = 1
    

    class ParameterEntryType(enum.Enum):
        Value = 0
        MaterialTable = 1
    

    class FlexibleCableContactFaceOptions(enum.Enum):
        TopFace = 0
        BottomFace = 1
    

    class PartFlexiblePrintedCircuitDesignFlatPatternObjectTypeDisplay():
        Type: Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternObjectType
        IsEnabled: int
        Color: NXColor
        Layer: int
        Font: DisplayableObject.ObjectFont
        Width: DisplayableObject.ObjectWidth
        def ToString(self) -> str:
            ...
    

    class FlatPatternObjectType(enum.Enum):
        BendCenterLine = 0
        BendUpCenterLine = 1
        BendDownCenterLine = 2
        BendTangentLine = 3
        OuterMoldLine = 4
        InnerMoldLine = 5
        ExteriorCurves = 6
        InteriorCurves = 7
        InteriorCutoutCurves = 8
        InteriorFeatureCurves = 9
        LighteningHoleCenter = 10
        JoggleLine = 11
        AddedTopGeometry = 12
        AddedBottomGeometry = 13
        ToolMarker = 14
        Hole = 15
        Centermark = 16
    

    class PartFlexiblePrintedCircuitDesignFlatPatternCalloutTypeDisplay():
        Type: str
        IsEnabled: int
        Name: str
        def ToString(self) -> str:
            ...
        def __init__(self, Type: str, IsEnabled: int, Name: str) -> None: ...
    

    class FlatPatternCalloutOrientationType(enum.Enum):
        Leadered = 0
        Aligned = 1
    

    class PartFlexiblePrintedCircuitDesign_PlanarSegmentCurveTypeDisplayData():
        type: Preferences.PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType
        is_enabled: int
        color: int
        font: DisplayableObject.ObjectFont
        width: DisplayableObject.ObjectWidth
    

    class PartFlexiblePrintedCircuitDesign_FlatPatternObjectTypeDisplay():
        type: Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternObjectType
        is_enabled: int
        color: int
        layer: int
        font: DisplayableObject.ObjectFont
        width: DisplayableObject.ObjectWidth
    

    class PartFlexiblePrintedCircuitDesign_FlatPatternCalloutTypeDisplay():
        type: int
        is_enabled: int
        name: int
    

class PartDrafting(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    ActiveViewColor: NXColor
    AssociativeAlignment: bool
    BorderColor: int
    BreakLineAmplitude: float
    BreakLineColor: NXColor
    BreakLineExtension: float
    BreakLineGap: float
    BreakLineType: Preferences.PartDrafting.BreakLineStyle
    BreakLineWidth: int
    BreakLinesVisibility: bool
    Color: int
    CustomSymbolSmashToSketch: bool
    DelayUpdateOnCreation: bool
    DelayViewUpdate: bool
    Delimiter: str
    DisplayBorders: bool
    EnableSmoothEdgesForLWView: bool
    Font: Preferences.PartDrafting.FontType
    FrameBarPrecision: int
    FrameBarTicDirection: int
    InitialSecondaryNumber: str
    InitialSheetNumber: str
    LineAntialiasing: bool
    MinimumComponentsForLargeAssemblyOption: int
    PropagateBreakLines: bool
    RetainAnnotations: bool
    ShowFacetEdges: bool
    Translucency: bool
    UpdateViewWithoutLwData: Preferences.PartDrafting.UpdateViewWithoutLwDataOption
    VersionObjects: bool
    ViewStyle: Preferences.PartDrafting.ViewStyleType
    ViewTracking: bool
    Width: Preferences.PartDrafting.WidthType


    class WidthType(enum.Enum):
        Original = 0
        Thin = 1
        Normal = 2
        Thick = 3
        ThicknessOne = 5
        ThicknessTwo = 6
        ThicknessThree = 7
        ThicknessFour = 8
        ThicknessFive = 9
        ThicknessSix = 10
        ThicknessSeven = 11
        ThicknessEight = 12
        ThicknessNine = 13
    

    class ViewStyleType(enum.Enum):
        Border = 0
        Wireframe = 1
        HiddenWireframe = 2
        Shaded = 3
    

    class UpdateViewWithoutLwDataOption(enum.Enum):
        Ignore = 0
        Notify = 1
        DoNotNotify = 2
        Generate = 3
    

    class FontType(enum.Enum):
        Original = 0
        Invisible = 1
        Solid = 2
        Dashed = 3
        Phantom = 4
        Centerline = 5
        Dotted = 6
        LongDashed = 7
        DottedDashed = 8
        Eight = 12
        Nine = 13
        Ten = 14
        Eleven = 15
    

    class BreakLineStyle(enum.Enum):
        Existing = 0
        Simple = 1
        Straight = 2
        Sawtooth = 3
        LongBreak = 4
        Tubular = 5
        SolidTubular = 6
        SolidRod = 7
        Jigsaw = 8
        Wood = 9
    

class PartAppearanceMgrPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetDesignatorLibraryFile(self) -> str:
        ...
    def SetDesignatorLibraryFile(self, designatorFile: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    DesignatorLibSource: Preferences.PartAppearanceMgrPreference.DesignatorSourceType
    PrefixAppearanceAreas: str
    PrefixAppearanceDesignators: str
    PrefixAppearanceSchemes: str


    class DesignatorSourceType(enum.Enum):
        ProductStructure = 0
        File = 1
    

class PartAeroSheetmetal(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def GetJoggleStationaryRadius(self) -> Expression:
        ...
    def SetJoggleStationaryRadius(self, updateModel: bool, stationaryRadius: str) -> None:
        ...
    def GetJoggleOffsetRadius(self) -> Expression:
        ...
    def SetJoggleOffsetRadius(self, updateModel: bool, offsetRadius: str) -> None:
        ...
    def GetJoggleDepthThreshold(self) -> Expression:
        ...
    def SetJoggleDepthThreshold(self, updateModel: bool, depthThreshold: str) -> None:
        ...
    def GetJoggleDistanceThreshold(self) -> Expression:
        ...
    def SetJoggleDistanceThreshold(self, updateModel: bool, distanceThreshold: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class ObjectPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def ResetSessionTranslucency(self, option: bool, sessionTranslucency: Preferences.ObjectPreferences.Translucency) -> None:
        ...
    def SetSessionTranslucency(self, option: Preferences.ObjectPreferences.Translucency, sessionTranslucency: Preferences.ObjectPreferences.Translucency) -> None:
        ...
    def Tag(self) -> Tag: ...



    class Translucency(enum.Enum):
        Disabled = 0
        Enabled = 1
        TemporarilyEnabled = 2
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MorphMeshPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CagePolylineColor: int
    CagePolylineStyle: int
    CagePolylineVertexColor: int
    CagePolylineVertexSize: Preferences.MorphMeshPreferences.CagePolylineVertexSizes
    CagePolylineVertexStyle: Preferences.MorphMeshPreferences.CagePolylineVertexStyles
    CagePolylineWidth: int
    CanAllowBackSideSelection: bool
    CanRefineMesh: bool
    ConstraintColor: int
    HighlightFaceTranslucency: int
    IsXRayCage: bool
    LineColor: int
    LineStyle: int
    LineWidth: int
    RefinementRatio: float
    VertexColor: int
    VertexSize: Preferences.MorphMeshPreferences.VertexSizeTypes
    VertexStyle: Preferences.MorphMeshPreferences.VertexStyleTypes


    class VertexStyleTypes(enum.Enum):
        Square = 0
        Triangle = 1
        Circle = 2
        Plus = 3
        Cross = 4
    

    class VertexSizeTypes(enum.Enum):
        Small = 0
        Medium = 1
        Large = 2
    

    class CagePolylineVertexStyles(enum.Enum):
        None = 0
        Square = 1
        Triangle = 2
        Circle = 3
        Plus = 4
        Cross = 5
    

    class CagePolylineVertexSizes(enum.Enum):
        Small = 0
        Medium = 1
        Large = 2
    

class ModelingPreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    ActionAfterInterruptValue: Preferences.ModelingPreferencesBuilder.ActionAfternterrupt
    ActivateTrimmedAnimation: bool
    AngleTolerance: float
    AssociativeFreeFormEdit: bool
    BodyTypeValue: Preferences.ModelingPreferencesBuilder.BodyType
    C0KnotLineColorValue: Preferences.ModelingPreferencesBuilder.C0KnotLineColor
    C0KnotLineStyleValue: LineFontBuilder
    C1KnotLineColorValue: Preferences.ModelingPreferencesBuilder.C1KnotLineColor
    C1KnotLineStyleValue: LineFontBuilder
    C2KnotLineColorValue: Preferences.ModelingPreferencesBuilder.C2KnotLineColor
    C2KnotLineStyleValue: LineFontBuilder
    CurveFitMethodValue: Preferences.ModelingPreferencesBuilder.CurveFitMethod
    DelayModelUpdate: bool
    DeleteChildFeaturesValue: Preferences.ModelingPreferencesBuilder.DeleteChildFeatures
    DensityUnitsValue: Preferences.ModelingPreferencesBuilder.DensityUnits
    DensityValue: float
    DistanceTolerance: float
    DynamicsUpdateLevelValue: Preferences.ModelingPreferencesBuilder.DynamicsUpdateLevel
    DynamicsUpdateModeValue: Preferences.ModelingPreferencesBuilder.DynamicUpdateMode
    EditDuringUpdateDialogOnError: bool
    EditDuringUpdateDialogOnWarning: bool
    EditPoleColorValue: Preferences.ModelingPreferencesBuilder.EditPoleColor
    EditPoleStyleValue: Preferences.ModelingPreferencesBuilder.EditPoleStyle
    EditPolylineColorValue: Preferences.ModelingPreferencesBuilder.EditPolylineColor
    EditPolylineStyleValue: LineFontBuilder
    EditSpecifcPoleColor: NXColor
    EditSpecificPolylineColorValue: NXColor
    EndPointColorValue: Preferences.ModelingPreferencesBuilder.EndPointColor
    EndPointStyleValue: Preferences.ModelingPreferencesBuilder.EndPointStyle
    FacesModifiedByBooleanValue: Preferences.ModelingPreferencesBuilder.FaceModifiedByBoolean
    FacetAngleTolerance: float
    FacetDistanceTolerance: float
    FeatureDoubleClickActionValue: Preferences.ModelingPreferencesBuilder.FeatureDoubleClickAction
    GridLineColorValue: Preferences.ModelingPreferencesBuilder.GridLineColor
    GridLineStyleValue: LineFontBuilder
    LimitChordLengthToMax: bool
    LimitFacetWidthToMaximum: bool
    LinkOrExtractGeometryValue: Preferences.ModelingPreferencesBuilder.LinkOrExtractGeometry
    MakeCurrentFeatureOnError: bool
    MakeSketchInternal: bool
    MaxChordLength: float
    MaxFacetWidth: float
    MaxRebuildDegree: int
    MaxRebuildSegments: int
    ModelDelayAndUpdateGranularityValue: Preferences.ModelingPreferencesBuilder.ModelDelayAndUpdateGranularity
    ModelingModeValue: Preferences.ModelingPreferencesBuilder.ModelingMode
    NewFacesValue: Preferences.ModelingPreferencesBuilder.NewFaces
    NotifyOnDelete: bool
    OptimizeCurve: bool
    OptimizeCurveAngleTol: float
    OptimizeCurveDitanceTol: float
    PlanarFaceTypeValue: Preferences.ModelingPreferencesBuilder.PlanarFaceType
    PoleColorValue: Preferences.ModelingPreferencesBuilder.PoleColor
    PoleStyleValue: Preferences.ModelingPreferencesBuilder.PoleStyle
    PolylineColorValue: Preferences.ModelingPreferencesBuilder.PolylineColor
    PolylineStyleValue: LineFontBuilder
    PreviewResolutionValue: Preferences.ModelingPreferencesBuilder.PreviewResolution
    ReportWarningAfterUpdate: bool
    ShowParentSketchDim: bool
    ShowSimulation: bool
    SketchDoubleClickActionValue: Preferences.ModelingPreferencesBuilder.SketchDoubleClickAction
    SpecificC0KnotLineColor: NXColor
    SpecificC1KnotLineColor: NXColor
    SpecificC2KnotLineColor: NXColor
    SpecificEndPointColor: NXColor
    SpecificGridLineColor: NXColor
    SpecificPoleColor: NXColor
    SpecificPolylineColor: NXColor
    SplineDoubleClickActionValue: Preferences.ModelingPreferencesBuilder.SplineDefaultClickAction
    SurfaceExtensionValue: Preferences.ModelingPreferencesBuilder.SurfaceExtension
    TreatDegrre1SplineAsPolyline: bool
    UGridLines: int
    UseTriangularMesh: bool
    VGridLines: int
    WarnOnMissingReference: bool


    class SurfaceExtension(enum.Enum):
        Linear = 0
        Soft = 1
    

    class SplineDefaultClickAction(enum.Enum):
        StudioSpline = 0
        XForm = 1
    

    class SketchDoubleClickAction(enum.Enum):
        EditwithRollback = 0
        DirectEdit = 1
    

    class PreviewResolution(enum.Enum):
        None = 0
        Coarse = 1
        Standard = 2
        Fine = 3
        ExtraFine = 4
        SuperFine = 5
        UltraFine = 6
    

    class PolylineColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class PoleStyle(enum.Enum):
        ThreeDimensionSphere = 0
        OpenCircle = 1
        FilledCircle = 2
        PlusSign = 3
        Cross = 4
    

    class PoleColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class PlanarFaceType(enum.Enum):
        Plane = 0
        Bsurface = 1
    

    class NewFaces(enum.Enum):
        InheritfromParent = 0
        InheritObjectPreferences = 1
    

    class ModelingMode(enum.Enum):
        HistoryFree = 0
        History = 1
    

    class ModelDelayAndUpdateGranularity(enum.Enum):
        Group = 0
        Feature = 1
    

    class LinkOrExtractGeometry(enum.Enum):
        InheritfromParent = 0
        InheritObjectPreferences = 1
    

    class GridLineColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class FeatureDoubleClickAction(enum.Enum):
        EditParameter = 0
        EditwithRollback = 1
    

    class FaceModifiedByBoolean(enum.Enum):
        InheritfromTargetBody = 0
        InheritfromToolBody = 1
    

    class EndPointStyle(enum.Enum):
        OpenCircle = 0
        FilledCircle = 1
        PlusSign = 2
        Cross = 3
    

    class EndPointColor(enum.Enum):
        CurveColor = 0
        SpecificColor = 1
    

    class EditPolylineColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class EditPoleStyle(enum.Enum):
        ThreeDimensionSphere = 0
        OpenCircle = 1
        FilledCircle = 2
        PlusSign = 3
        Cross = 4
    

    class EditPoleColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class DynamicUpdateMode(enum.Enum):
        None = 0
        Incremental = 1
        Continuous = 2
    

    class DynamicsUpdateLevel(enum.Enum):
        First = 0
        All = 1
    

    class DensityUnits(enum.Enum):
        Lbmin3 = 0
        Lbmft3 = 1
        Gcm3 = 2
        Kgm3 = 3
    

    class DeleteChildFeatures(enum.Enum):
        Yes = 1
        No = 2
        Ask = 3
    

    class CurveFitMethod(enum.Enum):
        Cubic = 0
        Quintic = 1
        Advanced = 2
    

    class C2KnotLineColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class C1KnotLineColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class C0KnotLineColor(enum.Enum):
        BodyColor = 0
        SpecificColor = 1
    

    class BodyType(enum.Enum):
        Solid = 0
        Sheet = 1
    

    class ActionAfternterrupt(enum.Enum):
        MakeLastSuccessfulFeatureCurrent = 0
        Undo = 1
    

class LoadDraftingStandardBuilder(Builder):
    def __init__(self) -> None: ...
    Level: Preferences.LoadDraftingStandardBuilder.LoadLevel
    Name: str
    WelcomeMode: bool


    class LoadLevel(enum.Enum):
        Shipped = 0
        Package = 1
        Site = 2
        Group = 3
        User = 4
    





















class InheritPmiPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CrosshatchPmiLightweightSectionView: bool
    InheritGdt: Preferences.GdtOption
    InheritPmiMode: Preferences.PmiOption
    InheritPmiToDrawing: bool


class IncludeModelCurvesOption(enum.Enum):
    No = 0
    Yes = 1










class HiddenLinesViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
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


class HiddenLineSmallFeatureOption(enum.Enum):
    ShowAll = 0
    Simplify = 1
    Hide = 2


class HiddenLineInterferingSolidsOption(enum.Enum):
    None = 0
    Yes = 1
    InterferenceCurves = 2


class GeneralWireframeColorSourceOption(enum.Enum):
    FromBody = 0
    FromFace = 1


class GeneralViewRepresentationOption(enum.Enum):
    Exact = 0
    SmartLightweight = 1
    Lightweight = 2
    PreNx85Exact = 3


class GeneralViewQualityOption(enum.Enum):
    Coarse = 0
    Medium = 1
    Fine = 2


class GeneralViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    FrameBar: Preferences.FrameBarPreferences
    AngleDecimalPointFormat: Preferences.DecimalPointCharacter
    AngleFormat: Preferences.AngleFormat
    AnglePrecision: int
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
    ShowAngleLeadingZeros: bool
    ShowAngleTrailingZeros: bool
    Silhouettes: bool
    SnapshotView: bool
    Tolerance: float
    UvGrid: bool
    ViewQuality: Preferences.GeneralViewQualityOption
    ViewRepresentation: Preferences.GeneralViewRepresentationOption
    WireframeColorSource: Preferences.GeneralWireframeColorSourceOption


class GeneralViewLockmethodOption(enum.Enum):
    None = 0
    Snapshot = 1
    Complete = 2


class GeneralToleranceOption(enum.Enum):
    Coarse = 0
    Medium = 1
    Standard = 2
    Fine = 3
    ExtraFine = 4
    Customize = 5


class GeneralExtractedEdgesOption(enum.Enum):
    None = 0
    Associative = 1
    NonAssociative = 2


class GeneralDisplayIdOption(enum.Enum):
    None = 0
    Orientation = 1
    Name = 2


class GdtOption(enum.Enum):
    None = 0
    InDrawingPlane = 1
    FromModelView = 2


class FrameBarPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.GeneralViewPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    Horizontal: bool
    HorizontalDistance: float
    HorizontalPosition: Annotations.BaseFrameBarBuilder.HorizontalPositionType
    Vertical: bool
    VerticalDistance: float
    VerticalPosition: Annotations.BaseFrameBarBuilder.VerticalPositionType


class Font(enum.Enum):
    Invisible = 0
    Solid = 1
    Dashed = 2
    Phantom = 3
    Centerline = 4
    Dotted = 5
    LongDashed = 6
    DottedDashed = 7
    Original = 8
    Eight = 11
    Nine = 12
    Ten = 13
    Eleven = 14


class FlatPatternViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def GetPropertiesObject(self) -> SheetMetal.FlatPatternSettings:
        ...
    def Commit(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class DrawShapeTaskPrefs(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CurveColor: NXColor
    CurveThickness: DisplayableObject.ObjectWidth
    StrokeColor: NXColor
    StrokeThickness: DisplayableObject.ObjectWidth
    SymmetryCurveFont: DisplayableObject.ObjectFont
    TangentAtSymmetryPlane: bool
    TrimAtSymmetryPlane: bool


class DraftingPreferenceManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.PartPreferences) -> None: ...
    def CreateLoadDraftingStandardBuilder(self) -> Preferences.LoadDraftingStandardBuilder:
        ...
    def Tag(self) -> Tag: ...



class DetailViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def SetCircularBoundary(self, circularBoundaryOption: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    CreateIndependent: int
    ViewBoundaryColor: NXColor
    ViewBoundaryFont: Preferences.Font
    ViewBoundaryWidth: Preferences.Width


class DetailBoundaryOption(enum.Enum):
    Circular = 0
    Rectangular = 1


class DecimalPointCharacter(enum.Enum):
    Period = 0
    Comma = 1


class CoatingPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.SessionPreferences) -> None: ...
    def Tag(self) -> Tag: ...

    CreateNgc: bool


class BaseViewPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Preferences.ViewPreferences) -> None: ...
    def SetFacetedRepresentation(self, isFacetedRepresentation: bool) -> None:
        """[Obsolete("Deprecated in NX8.5.1.  Use Preferences.GeneralViewPreferences.ViewRepresentation instead.")"""
        ...
    def SetInheritClippingBoundary(self, isInheritClippingBoundary: bool) -> None:
        ...
    def SetTransferAnnotation(self, isTransferAnnotation: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class AnnotationPreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def GetLetteringPreferences(self) -> Annotations.LetteringPreferences:
        ...
    def GetLineAndArrowPreferences(self) -> Annotations.LineAndArrowPreferences:
        ...
    def GetSymbolPreferences(self) -> Annotations.SymbolPreferences:
        ...
    def GetDimensionPreferences(self) -> Annotations.DimensionPreferences:
        ...
    def GetAngularTolerances(self) -> Annotations.AngularTolerance:
        ...
    def GetLinearTolerances(self) -> Annotations.LinearTolerance:
        ...
    def GetPmiPreferences(self) -> Annotations.PmiPreferences:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiSettingsManager.CreatePreferencesBuilder instead.")"""
        ...
    def GetNxFontCharacterSpaceFactor(self) -> Annotations.CharacterSpaceFactor:
        ...
    def GetStandardFontCharacterSpaceFactor(self) -> Annotations.CharacterSpaceFactor:
        ...
    def GetFrameBarPreferences(self) -> Annotations.FrameBarPreferences:
        ...
    def SetLetteringPreferences(self, letteringPrefs: Annotations.LetteringPreferences) -> None:
        ...
    def SetLineAndArrowPreferences(self, prefs: Annotations.LineAndArrowPreferences) -> None:
        ...
    def SetSymbolPreferences(self, prefs: Annotations.SymbolPreferences) -> None:
        ...
    def SetDimensionPreferences(self, prefs: Annotations.DimensionPreferences) -> None:
        ...
    def SetAngularTolerances(self, prefs: Annotations.AngularTolerance) -> None:
        ...
    def SetLinearTolerances(self, prefs: Annotations.LinearTolerance) -> None:
        ...
    def SetPmiPreferences(self, pmiPrefs: Annotations.PmiPreferences) -> None:
        ...
    def SetNxFontCharacterSpaceFactor(self, nxFontCharacterSpaceFactor: Annotations.CharacterSpaceFactor) -> None:
        ...
    def SetStandardFontCharacterSpaceFactor(self, standardFontCharacterSpaceFactor: Annotations.CharacterSpaceFactor) -> None:
        ...
    def SetFrameBarPreferences(self, frameBarPrefs: Annotations.FrameBarPreferences) -> None:
        ...
    def Tag(self) -> Tag: ...



class AngleFormat(enum.Enum):
    FractionalDegrees = 0
    DegreesMinutes = 1
    DegreesMinutesSeconds = 2
    WholeDegrees = 3


