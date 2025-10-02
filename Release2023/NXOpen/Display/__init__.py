from ...NXOpen import *
from ..Display import *

import typing
import enum

class Wall(Builder):
    def __init__(self) -> None: ...
    Image: Display.Image
    ImageFilename: str
    PatternRepeatFactor: float
    Reflectivity: float
    WallMaterialTextureType: Display.Wall.MaterialTextureType
    WallMaterialType: Display.Wall.MaterialType


    class MaterialType(enum.Enum):
        ShadowCatcher = 0
        Reflective = 1
        Invisible = 2
    

    class MaterialTextureType(enum.Enum):
        ShadowCatcher = 0
        ImageFile = 1
        Invisible = 2
    

class UVTransformationData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    RotationX: float
    RotationY: float
    RotationZ: float
    TranslationX: float
    TranslationY: float
    TranslationZ: float


class UVMapCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.UVMap]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateUVMapBuilder(self, uvParam: Display.UVMap) -> Display.UVMapBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Display.UVMap:
        ...
    def Tag(self) -> Tag: ...



class UVMapBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str
    ObjectToUnwrap: SelectNXObjectList
    RipEdges: ScCollector
    UDirection: SelectSelectObject
    UVDiagnostics: bool


class UVMap(NXObject):
    def __init__(self) -> None: ...


class TrueStudioCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.TrueStudio]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateTrueStudioBuilder(self, sObj: Display.TrueStudio) -> Display.TrueStudioBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Display.TrueStudio:
        ...
    def Tag(self) -> Tag: ...



class TrueStudioBuilder(Builder):
    def __init__(self) -> None: ...
    GlobalMaterialType: Display.TrueStudioBuilder.GlobalMaterial
    ModeToggle: bool
    RenderMethodType: Display.TrueStudioBuilder.RenderMethod


    class RenderMethod(enum.Enum):
        FullRender = 0
        ImprovedRender = 1
        PreviewRender = 2
    

    class GlobalMaterial(enum.Enum):
        PlasticColorwash = 0
        ShinyMetalColorwash = 1
        Clay = 2
        Plasticine = 3
        Chrome = 4
    

class TrueStudio(NXObject):
    def __init__(self) -> None: ...


class TrueShadingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.TrueShading]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateTrueShadingBuilder(self, sObj: Display.TrueShading) -> Display.TrueShadingBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Display.TrueShading:
        ...
    def IsTrueShadeEnabled(self) -> bool:
        ...
    def Tag(self) -> Tag: ...



class TrueShadingBuilder(Builder):
    def __init__(self) -> None: ...
    def AssignOverrideMaterial(self, overrideMaterialType: Display.TrueShadingBuilder.MaterialType) -> None:
        ...
    def GButton0(self) -> None:
        ...
    def GButton1(self) -> None:
        ...
    def GButton2(self) -> None:
        ...
    def GButton3(self) -> None:
        ...
    def GButton4(self) -> None:
        ...
    def GButton5(self) -> None:
        ...
    def GButton6(self) -> None:
        ...
    def GButton7(self) -> None:
        ...
    def GButton8(self) -> None:
        ...
    def GButton9(self) -> None:
        ...
    def GButton10(self) -> None:
        ...
    def GButton11(self) -> None:
        ...
    def GButton12(self) -> None:
        ...
    def GButton13(self) -> None:
        ...
    def GButton14(self) -> None:
        ...
    def GButton15(self) -> None:
        ...
    def GButton16(self) -> None:
        ...
    def GButton17(self) -> None:
        ...
    def GButton18(self) -> None:
        ...
    def GButton19(self) -> None:
        ...
    def GButton20(self) -> None:
        ...
    def GButton21(self) -> None:
        ...
    def GButton22(self) -> None:
        ...
    def GButton23(self) -> None:
        ...
    def GButton24(self) -> None:
        ...
    def GButton25(self) -> None:
        ...
    def GButton26(self) -> None:
        ...
    def GButton27(self) -> None:
        ...
    def GButton28(self) -> None:
        ...
    def GButton29(self) -> None:
        ...
    def OButton0(self) -> None:
        ...
    def OButton1(self) -> None:
        ...
    def OButton2(self) -> None:
        ...
    def OButton3(self) -> None:
        ...
    def OButton4(self) -> None:
        ...
    def OButton5(self) -> None:
        ...
    def OButton6(self) -> None:
        ...
    def OButton7(self) -> None:
        ...
    def OButton8(self) -> None:
        ...
    def OButton9(self) -> None:
        ...
    def OButton10(self) -> None:
        ...
    def OButton11(self) -> None:
        ...
    def OButton12(self) -> None:
        ...
    def OButton13(self) -> None:
        ...
    def OButton14(self) -> None:
        ...
    def OButton15(self) -> None:
        ...
    def OButton16(self) -> None:
        ...
    def OButton17(self) -> None:
        ...
    def OButton18(self) -> None:
        ...
    def OButton19(self) -> None:
        ...
    def OButton20(self) -> None:
        ...
    def OButton21(self) -> None:
        ...
    def OButton22(self) -> None:
        ...
    def OButton23(self) -> None:
        ...
    def OButton24(self) -> None:
        ...
    def OButton25(self) -> None:
        ...
    def OButton26(self) -> None:
        ...
    def OButton27(self) -> None:
        ...
    def OButton28(self) -> None:
        ...
    def ORemoveButton(self) -> None:
        ...
    def GetBgdTopRgbcolorPicker(self) -> float:
        ...
    def SetBgdTopRgbcolorPicker(self, bgdTopRGBColorPicker: float) -> None:
        ...
    def GetBgdBottomRgbcolorPicker(self) -> float:
        ...
    def SetBgdBottomRgbcolorPicker(self, bgdBottomRGBColorPicker: float) -> None:
        ...
    def GetGridRgbcolorPicker(self) -> float:
        ...
    def SetGridRgbcolorPicker(self, gridRGBColorPicker: float) -> None:
        ...
    def ProtectUpdate(self) -> None:
        ...
    BgdImageEnum: Display.TrueShadingBuilder.BgdImageType
    BgdImageFileBrowser: str
    BgdTypeEnum: Display.TrueShadingBuilder.BgdType
    EnvironmentMapEnum: Display.TrueShadingBuilder.EnvironmentMapType
    EnvironmentMapFileBrowser: str
    GlobalMaterialType: Display.TrueShadingBuilder.MaterialType
    InheritModelTogggle: bool
    LightCollectionEnum: Display.TrueShadingBuilder.SHEDLightCollectionType
    LightDimmerValue: float
    ObjSpecificSelection: SelectNXObjectList
    PlanarReflectionToggle: bool
    PlanarShadowToggle: bool
    PlaneGridToggle: bool
    PlaneOffsetFixedToggle: bool
    PlaneOffsetValue: float
    ReflectivityValue: float
    ShedModeToggle: bool
    SnapFloorToggle: bool
    SoftShadowsToggle: bool
    SpecifyPlane: Plane
    SurfaceOrientEnum: Display.TrueShadingBuilder.SurfaceOrientType


    class SurfaceOrientType(enum.Enum):
        None = 0
        Bottom = 1
        Back = 2
        BottomFixed = 3
    

    class SHEDLightCollectionType(enum.Enum):
        DefaultLights = 0
        Lighting1 = 1
        Lighting2 = 2
        Lighting3 = 3
        Lighting4 = 4
        Custom = 5
    

    class MaterialType(enum.Enum):
        GlobalWashShinyMetal = 0
        GlobalWashBrushedMetal = 1
        GlobalWashShinyPlastic = 2
        GlobalWashAnalysis = 3
        GlobalWashFlat = 4
        GlobalRedGlossyPlastic = 5
        GlobalBlueGlossyPlastic = 6
        GlobalGreenGlossyPlastic = 7
        GlobalGrayGlossyPlastic = 8
        GlobalBlackGlossyPlastic = 9
        GlobalBrownGlossyPlastic = 10
        GlobalYellowGlossyPlastic = 11
        GlobalTealGlossyPlastic = 12
        GlobalWhiteGlossyPlastic = 13
        GlobalClearPlastic = 14
        GlobalChrome = 15
        GlobalCopper = 16
        GlobalGold = 17
        GlobalBrass = 18
        GlobalSteel = 19
        GlobalBrushedChrome = 20
        GlobalBrushedAluminum = 21
        GlobalBrushedTitanium = 22
        GlobalGlassClear = 23
        GlobalGlassSmokey = 24
        GlobalMetallicPaintRed = 25
        GlobalMetallicPaintGray = 26
        GlobalMetallicPaintBlack = 27
        GlobalMetallicPaintBlue = 28
        GlobalRubber = 29
        OverrideRedGlossyPlastic = 30
        OverrideBlueGlossyPlastic = 31
        OverrideGreenGlossyPlastic = 32
        OverrideGrayGlossyPlastic = 33
        OverrideBlackGlossyPlastic = 34
        OverrideBrownGlossyPlastic = 35
        OverrideYellowGlossyPlastic = 36
        OverrideTealGlossyPlastic = 37
        OverrideWhiteGlossyPlastic = 38
        OverrideClearPlastic = 39
        OverrideChrome = 40
        OverrideCopper = 41
        OverrideGold = 42
        OverrideBrass = 43
        OverrideSteel = 44
        OverrideBrushedChrome = 45
        OverrideBrushedAluminum = 46
        OverrideBrushedTitanium = 47
        OverrideGlassClear = 48
        OverrideGlassSmokey = 49
        OverrideMetallicPaintRed = 50
        OverrideMetallicPaintGray = 51
        OverrideMetallicPaintBlack = 52
        OverrideMetallicPaintBlue = 53
        OverrideRubber = 54
        OverrideRoughMetalMedGray = 55
        OverrideRoughMetalDkGray = 56
        OverrideRoughPlasticBlueGray = 57
        OverrideRoughPlasticTan = 58
    

    class EnvironmentMapType(enum.Enum):
        Default = 0
        MetalShiny1 = 1
        MetalShiny2 = 2
        MetalBrushed1 = 3
        MetalBrushed2 = 4
        Glossy1 = 5
        Glossy2 = 6
        SurfaceAnalysisLines = 7
        SurfaceAnalysisHorizon = 8
        AutoPhotoStudio = 9
        CustomImage = 10
    

    class BgdType(enum.Enum):
        DarkGraduated = 0
        LightGraduated = 1
        Black = 2
        White = 3
        CustomPlain = 4
        CustomGraduated = 5
        InheritShadedBackground = 6
        ImageBackground = 7
        PureWhite = 8
    

    class BgdImageType(enum.Enum):
        Image1 = 0
        Image2 = 1
        Image3 = 2
        Image4 = 3
        Image5 = 4
        Image6 = 5
        CustomImage = 6
    

class TrueShading(NXObject):
    def __init__(self) -> None: ...


class TransientText(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def DisplayTemporaryAbsoluteGeometry(self, fontIndex: int, view: View, viewType: Display.TransientText.ViewType, object: DisplayableObject, position: Point3d) -> None:
        ...
    def DisplayTemporaryScreenGeometry(self, fontIndex: int, view: View, viewType: Display.TransientText.ViewType, object: DisplayableObject, position: Point3d) -> None:
        ...
    def DisplayTemporaryAbsRotScreenSizeGeometry(self, fontIndex: int, view: View, viewType: Display.TransientText.ViewType, object: DisplayableObject, position: Point3d) -> None:
        ...
    def AddTextString(self, textString: str) -> None:
        ...
    def GetAbsoluteTextSize(self, glyphWidth: float, glyphHeight: float) -> None:
        ...
    def SetAbsoluteTextSize(self, glyphWidth: float, glyphHeight: float) -> None:
        ...
    Color: int
    FontStyle: str
    ReferencePositionType: Display.TransientText.StandardTextRef
    ScreenTextSize: Display.TransientText.TextSize


    class ViewType(enum.Enum):
        WorkViewOnly = 0
        AllActiveViews = 1
        ViewOfLastCursor = 2
        AllViewsButDrawing = 3
        AllActiveMemberViews = 4
        FirstViewFound = 5
    

    class TextSize(enum.Enum):
        Small = 0
        Normal = 1
        Medium = 1
        Large = 2
        NumSizes = 3
    

    class StandardTextRef(enum.Enum):
        SystemDefault = 0
        BaselineStart = 0
        BaselineCenter = 1
        BaselineEnd = 2
        TopLeft = 3
        TopCenter = 4
        TopRight = 5
        MiddleLeft = 6
        MiddleCenter = 7
        MiddleRight = 8
        BottomLeft = 9
        BottomCenter = 10
        BottomRight = 11
    

class StudioImageCaptureBuilder(Builder):
    def __init__(self) -> None: ...
    def GetImageDimensionsDouble(self) -> float:
        ...
    def SetImageDimensionsDouble(self, imageDimensionsDouble: float) -> None:
        ...
    def GetImageDimensionsInteger(self) -> int:
        ...
    def SetImageDimensionsInteger(self, imageDimensionsInteger: int) -> None:
        ...
    def GetCustomBackgroundColor(self) -> float:
        ...
    def SetCustomBackgroundColor(self, customBackgroundColor: float) -> None:
        ...
    AASamplesEnum: Display.StudioImageCaptureBuilder.AASamplesEnumType
    BackgroundOption: Display.StudioImageCaptureBuilder.BackgroundOptions
    DpiEnum: Display.StudioImageCaptureBuilder.DPIEnumType
    DrawingSizeEnum: Display.StudioImageCaptureBuilder.DrawingSizeEnumType
    EnhanceEdges: bool
    NativeFileBrowser: str
    OrientEnum: Display.StudioImageCaptureBuilder.OrientEnumType
    UnitsEnum: Display.StudioImageCaptureBuilder.UnitsEnumType


    class UnitsEnumType(enum.Enum):
        Pixels = 0
        Mm = 1
        Inches = 2
    

    class OrientEnumType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class DrawingSizeEnumType(enum.Enum):
        Isoa4 = 0
        Isoa3 = 1
        Isoa2 = 2
        Isoa1 = 3
        Isoa0 = 4
        Ansia = 5
        Ansib = 6
        Ansic = 7
        Ansid = 8
        Ansie = 9
        Custom = 10
    

    class DPIEnumType(enum.Enum):
        Dpi72 = 0
        Dpi150 = 1
        Dpi400 = 2
    

    class BackgroundOptions(enum.Enum):
        Original = 0
        CustomColor = 1
        Transparent = 2
    

    class AASamplesEnumType(enum.Enum):
        Sam0X = 0
        Sam2X = 1
        Sam4X = 2
        Sam8X = 3
        Sam16X = 4
    

class Stage(Builder):
    def __init__(self) -> None: ...
    def FloorXaxis(self) -> None:
        ...
    def FloorYaxis(self) -> None:
        ...
    def FloorZaxis(self) -> None:
        ...
    def AlignFloorPlane(self, specifyFloorPlane: Plane) -> None:
        ...
    def GetWallFromList(self, index: Display.Stage.WallType) -> Display.Wall:
        ...
    def SetWallInList(self, index: Display.Stage.WallType, wall: Display.Wall) -> None:
        ...
    def CommitWall(self, view: View, currentWallIndex: int, updateStageDatabase: bool) -> None:
        ...
    def CommitOffset(self, view: View) -> None:
        ...
    FloorOrientationType: Display.Stage.OrientationType
    Offset: float
    OffsetExpression: Expression
    Size: float
    SizeExpression: Expression
    SpecifyFloorPlane: Plane


    class WallType(enum.Enum):
        Left = 0
        Right = 1
        Top = 2
        Bottom = 3
        Front = 4
        Back = 5
        Total = 6
    

    class OrientationType(enum.Enum):
        Yz = 0
        Xz = 1
        Xy = 2
        UserDefined = 3
    

class Shadows(Builder):
    def __init__(self) -> None: ...
    AmbientOcclusion: bool
    GenerateHqiShadows: bool
    RealTimeType: Display.Shadows.RealTimeState
    ShadowCatcherSelection: SelectNXObjectList
    ShadowsEnabled: bool
    ShadowsShadedViewsShowGroundShadows: bool
    SoftShadowsBiasOffset: float
    SoftShadowsEdges: int
    SoftShadowsEnabled: bool
    SoftShadowsGradientClamp: float
    SoftShadowsQuality: int
    SsaoBlurRadius: float
    SsaoContrast: Display.Shadows.SsaoContrastType
    SsaoQuality: Display.Shadows.SsaoQualityType
    SsaoRadius: float
    UseShadowCatcher: bool


    class SsaoQualityType(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
        VeryHigh = 3
    

    class SsaoContrastType(enum.Enum):
        None = 0
        Low = 1
        Medium = 2
        High = 3
        ExtraHigh = 4
    

    class RealTimeState(enum.Enum):
        Disabled = 0
        EnvironmentShadowCatcherOnly = 1
        InterObject = 2
    

class SelPrefCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.SelPref]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateSelPref(self) -> Display.SelPref:
        ...
    def Tag(self) -> Tag: ...



class SelPref(Builder):
    def __init__(self) -> None: ...
    Delay: int
    FaceAnalysisViewsType: Display.SelPref.FaceAnalysisViews
    HighlightHiddenEdgesToggle: bool
    HighlightOriginalToggle: bool
    HighlightSelectionOnRolloverToggle: bool
    HighlightWithThickWidthToggle: bool
    MethodType: Display.SelPref.Method
    MouseGestureType: Display.SelPref.MouseGesture
    QuickPickLockDialogPosition: bool
    QuickPickOnDelayToggle: bool
    QuickPickSeeThruToggle: bool
    RolloverDelay: int
    SelectionRadiusType: Display.SelPref.SelectionRadius
    SelectionRuleType: Display.SelPref.SelectionRule
    ShadedViewsType: Display.SelPref.ShadedViews
    ShowCrosshairsToggle: bool
    TangencyTolerance: float
    Tolerance: float
    TooltipOnRolloverToggle: bool


    class ShadedViews(enum.Enum):
        HighlightEdges = 0
        HighlightFaces = 1
    

    class SelectionRule(enum.Enum):
        Inside = 0
        Outside = 1
        Crossing = 2
        InsideCrossing = 3
        OutsideCrossing = 4
    

    class SelectionRadius(enum.Enum):
        Medium = 0
        Small = 1
        Large = 2
    

    class MouseGesture(enum.Enum):
        Lasso = 0
        Rectangle = 1
        Circle = 2
    

    class Method(enum.Enum):
        Simple = 0
        Wcs = 1
        WcsLeft = 2
        WcsRight = 3
    

    class FaceAnalysisViews(enum.Enum):
        HighlightEdges = 0
        HighlightFaces = 1
    

class SectionCurveSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Color: NXColor
    ColorOption: Display.SectionCurveSettingsBuilder.ColorOptionType
    Show: bool


    class ColorOptionType(enum.Enum):
        Body = 0
        Any = 1
    

class Scene(Builder):
    def __init__(self) -> None: ...
    Background: Display.Background
    EnvironmentBuilder: Display.EnvironmentBuilder
    ImageBasedLighting: Display.ImageBasedLighting
    Lighting: Display.Lighting
    Reflection: Display.Reflection
    Stage: Display.Stage


class SaveImageFileBrowserBuilder(Builder):
    def __init__(self) -> None: ...
    FileFormat: Display.SaveImageFileBrowserBuilder.FileFormats
    NativeImageFileBrowser: str
    UseTransparentBackground: bool


    class FileFormats(enum.Enum):
        Tif = 0
        Png = 1
        Jpg = 2
    

class Reflection(Builder):
    def __init__(self) -> None: ...
    Image: Display.Image
    ImageFilename: str
    ReflectionMap: Display.Reflection.Type


    class Type(enum.Enum):
        Background = 0
        Stage = 1
        Ibl = 2
        Image = 3
    

class RayTracedStudioPreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    DynamicRayTracedStudioTilingQuality: Display.RayTracedStudioPreferencesBuilder.DynamicRayTracedStudioTilingQualityType
    RayTracedStudioDisplayGamma: float
    RayTracedStudioStaticImageDotsPerInch: int
    RayTracedStudioStaticImageDoubleHeight: float
    RayTracedStudioStaticImageDoubleWidth: float
    RayTracedStudioStaticImageFileFormat: Display.RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageFileFormatType
    RayTracedStudioStaticImageLockAspectRatio: bool
    RayTracedStudioStaticImageOrientation: Display.RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageOrientationType
    RayTracedStudioStaticImagePixelHeight: int
    RayTracedStudioStaticImagePixelWidth: int
    RayTracedStudioStaticImageResolution: Display.RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageResolutionType
    RayTracedStudioStaticImageSize: Display.RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageSizeType
    RayTracedStudioStaticImageUnits: Display.RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageUnitsType
    StaticAntialiasing: Display.RayTracedStudioPreferencesBuilder.StaticAntialiasingType
    StaticRayTracedStudioQuality: Display.RayTracedStudioPreferencesBuilder.StaticRayTracedStudioQualityType
    StaticRayTracedStudioRenderDepth: int
    StationaryAntialiasing: Display.RayTracedStudioPreferencesBuilder.StationaryAntialiasingType
    StationaryRayTracedStudioQuality: Display.RayTracedStudioPreferencesBuilder.StationaryRayTracedStudioQualityType
    StationaryRayTracedStudioshowStatusIndicator: bool


    class StationaryRayTracedStudioQualityType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
    

    class StationaryAntialiasingType(enum.Enum):
        Medium = 0
        Low = 1
        None = 2
    

    class StaticRayTracedStudioQualityType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        UserDefined = 3
    

    class StaticAntialiasingType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        None = 3
    

    class RayTracedStudioStaticImageUnitsType(enum.Enum):
        Pixels = 0
        Millimeters = 1
        Inches = 2
    

    class RayTracedStudioStaticImageSizeType(enum.Enum):
        RenderWindow = 0
        UserDefined = 1
    

    class RayTracedStudioStaticImageResolutionType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        UserDefined = 3
    

    class RayTracedStudioStaticImageOrientationType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class RayTracedStudioStaticImageFileFormatType(enum.Enum):
        Tif = 0
        Png = 1
        Jpg = 2
    

    class DynamicRayTracedStudioTilingQualityType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
    

class RayTracedStudioEditorBuilder(Builder):
    def __init__(self) -> None: ...
    DynamicRayTracedStudioTilingQuality: Display.RayTracedStudioEditorBuilder.DynamicRayTracedStudioTilingQualityType
    RayTracedStudioDisplayGamma: float
    RayTracedStudioStaticImageDotsPerInch: int
    RayTracedStudioStaticImageDoubleHeight: float
    RayTracedStudioStaticImageDoubleWidth: float
    RayTracedStudioStaticImageFileFormat: Display.RayTracedStudioEditorBuilder.RayTracedStudioStaticImageFileFormatType
    RayTracedStudioStaticImageLockAspectRatio: bool
    RayTracedStudioStaticImageOrientation: Display.RayTracedStudioEditorBuilder.RayTracedStudioStaticImageOrientationType
    RayTracedStudioStaticImagePixelHeight: int
    RayTracedStudioStaticImagePixelWidth: int
    RayTracedStudioStaticImageResolution: Display.RayTracedStudioEditorBuilder.RayTracedStudioStaticImageResolutionType
    RayTracedStudioStaticImageSize: Display.RayTracedStudioEditorBuilder.RayTracedStudioStaticImageSizeType
    RayTracedStudioStaticImageUnits: Display.RayTracedStudioEditorBuilder.RayTracedStudioStaticImageUnitsType
    StaticAntialiasing: Display.RayTracedStudioEditorBuilder.StaticAntialiasingType
    StaticRayTracedStudioQuality: Display.RayTracedStudioEditorBuilder.StaticRayTracedStudioQualityType
    StaticRayTracedStudioRenderDepth: int
    StationaryAntialiasing: Display.RayTracedStudioEditorBuilder.StationaryAntialiasingType
    StationaryRayTracedStudioQuality: Display.RayTracedStudioEditorBuilder.StationaryRayTracedStudioQualityType
    StationaryRayTracedStudioshowStatusIndicator: bool


    class StationaryRayTracedStudioQualityType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
    

    class StationaryAntialiasingType(enum.Enum):
        Medium = 0
        Low = 1
        None = 2
    

    class StaticRayTracedStudioQualityType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        UserDefined = 3
    

    class StaticAntialiasingType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        None = 3
    

    class RayTracedStudioStaticImageUnitsType(enum.Enum):
        Pixels = 0
        Millimeters = 1
        Inches = 2
    

    class RayTracedStudioStaticImageSizeType(enum.Enum):
        RenderWindow = 0
        UserDefined = 1
    

    class RayTracedStudioStaticImageResolutionType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        UserDefined = 3
    

    class RayTracedStudioStaticImageOrientationType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class RayTracedStudioStaticImageFileFormatType(enum.Enum):
        Tif = 0
        Png = 1
        Jpg = 2
    

    class DynamicRayTracedStudioTilingQualityType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
    

class RayTracedStudioBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateRayTracedDisplay(self) -> None:
        ...
    def StartRayTracedDisplay(self) -> None:
        ...
    def StopRayTracedDisplay(self) -> None:
        ...
    def RayTracedPreferences(self) -> None:
        ...
    def RayTracedEditor(self) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Display.RayTracedStudioBuilder.RayTracedPreferences instead.")"""
        ...
    def RayTracedRenderingStart(self) -> None:
        ...
    def RayTracedRenderingErase(self) -> None:
        ...
    def RayTracedRenderingSave(self) -> None:
        ...
    def RayTracedAnimationStart(self) -> None:
        ...
    def RayTracedAnimationResume(self) -> None:
        ...
    def RayTracedAnimationPause(self) -> None:
        ...
    def RayTracedAnimationStop(self) -> None:
        ...
    Brightness: float
    StationaryQuality: Display.RayTracedStudioBuilder.StationaryDisplayQualityType


    class StationaryDisplayQualityType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
    

class RasterImageBuilder(Display.ImageBaseBuilder):
    def __init__(self) -> None: ...
    Target: Plane


class RasterImage(Display.ImageBase):
    def __init__(self) -> None: ...


class PointCloudCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.PointCloud]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Display.PointCloud:
        ...
    def CreatePointCloudBuilder(self, referencePointCloud: Display.PointCloud) -> Display.PointCloudBuilder:
        ...
    def Tag(self) -> Tag: ...



class PointCloudClippingBoxesListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Display.PointCloudClippingBoxesListItemBuilder]) -> None:
        ...
    def Append(self, object: Display.PointCloudClippingBoxesListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Display.PointCloudClippingBoxesListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Display.PointCloudClippingBoxesListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Display.PointCloudClippingBoxesListItemBuilder) -> None:
        ...
    def Erase(self, obj: Display.PointCloudClippingBoxesListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Display.PointCloudClippingBoxesListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Display.PointCloudClippingBoxesListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Display.PointCloudClippingBoxesListItemBuilder, object2: Display.PointCloudClippingBoxesListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Display.PointCloudClippingBoxesListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PointCloudClippingBoxesListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ClippingEndPoint: Point
    ClippingSide: Display.PointCloudClippingBoxesListItemBuilder.ClippingSides
    ClippingStartPoint: Point
    Orientation: Matrix3x3


    class ClippingSides(enum.Enum):
        Inside = 0
        Outside = 1
        None = 2
    

class PointCloudBuilder(Builder):
    def __init__(self) -> None: ...
    def LoadPointData(self) -> None:
        ...
    def CreateClippingBoxesListItemBuilder(self) -> Display.PointCloudClippingBoxesListItemBuilder:
        ...
    ClippingBoxesList: Display.PointCloudClippingBoxesListItemBuilderList
    LoadPointDataWithPart: bool
    PointBrightnessMode: Display.PointCloudBuilder.BrightnessModes
    PointColorMode: Display.PointCloudBuilder.ColorModes
    PointDataFile: str
    PointDensity: float
    PointSize: int


    class ColorModes(enum.Enum):
        Individual = 0
        Uniform = 1
    

    class BrightnessModes(enum.Enum):
        Uniform = 0
        Shaded = 1
    

class PointCloud(DisplayableObject):
    def __init__(self) -> None: ...
    def Load(self) -> None:
        ...
    def Unload(self) -> None:
        ...


class PlaneGridBuilder(Display.BoundedGridBuilder):
    def __init__(self) -> None: ...
    Plane: Plane


class PlaneGrid(Display.BoundedGrid):
    def __init__(self) -> None: ...


class PlanarShipGridBuilder(Builder):
    def __init__(self) -> None: ...
    def GetExtent(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> bool:
        ...
    def SetExtent(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> bool:
        ...
    def GetIntersectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetIntersectedObjects(self, intersectedObjects: typing.List[TaggedObject]) -> None:
        ...
    def SwitchLabelLocationX(self) -> None:
        ...
    def SwitchLabelLocationY(self) -> None:
        ...
    def SwitchLabelLocationZ(self) -> None:
        ...
    BasePlane: DatumPlane
    IntersectType: Display.PlanarShipGridBuilder.IntersectOption
    LabelColor: NXColor
    LabelDisplayType: Display.PlanarShipGridBuilder.LabelDisplayOption
    LabelSettingInheritted: bool
    LineColor: NXColor
    LineFontType: DisplayableObject.ObjectFont
    LineSettingInheritted: bool
    LineWidthType: DisplayableObject.ObjectWidth


    class LabelDisplayOption(enum.Enum):
        ShowAll = 0
        ShowEveryOther = 1
        ShowEveryThird = 2
        ShowEveryFourth = 3
        HideAll = 4
    

    class IntersectOption(enum.Enum):
        Everything = 0
        SelectedObjects = 1
        ShipGridAndSelected = 2
    

class PlanarShipGrid(Display.EntitySelectionPlane):
    def __init__(self) -> None: ...
    def IsDatumPlaneInGrid(self, datumplaneTag: DatumPlane) -> bool:
        ...
    def AddDatumPlanes(self, datumplaneTags: typing.List[DatumPlane]) -> None:
        ...
    def RemoveDatumPlanes(self, datumplaneTags: typing.List[DatumPlane]) -> None:
        ...


class PerspectiveOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    def ApplyLastDistanceChange(self) -> None:
        ...
    def Cancel(self) -> None:
        ...
    CameraDistance: float


class NonProportionalZoom(Builder):
    def __init__(self) -> None: ...
    def Start(self, view: View) -> None:
        ...
    def FirstPoint(self, point1: Point3d, view: View) -> None:
        ...
    def SecondPoint(self, point2: Point3d, view: View) -> None:
        ...
    def Finish(self, view: View) -> None:
        ...
    def Enable(self, enable: bool) -> None:
        ...
    AnchorCenter: bool
    Method: Display.NonProportionalZoom.MethodType
    ZoomSensitivity: int


    class MethodType(enum.Enum):
        Rectangle = 0
        Dynamic = 1
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class Lighting(Builder):
    def __init__(self) -> None: ...
    def GetLightBuilderFromList(self, index: int) -> Display.LightBuilder:
        ...
    def SetLightBuilderInList(self, index: int, light: Display.LightBuilder) -> None:
        ...
    def SetLightBuilderInList(self, lightName: str, lightIntensity: float) -> None:
        ...
    def RemoveLightBuilderInList(self, lightName: str) -> None:
        ...
    def GetNumLightBuilders(self) -> int:
        ...
    LightsShadedViewsLightingCollection: Display.Lighting.LightingCollectionType
    LightsShadedViewsSceneDimmerValue: float


    class LightingCollectionType(enum.Enum):
        Lighting1 = 0
        Lighting2 = 1
        Lighting3 = 2
        Lighting4 = 3
        Lighting5 = 4
        UserDefined = 5
    

class LightBuilder(Builder):
    def __init__(self) -> None: ...
    ConeAngle: float
    DestinationPosition: Point
    Intensity: float
    LightShadowType: Display.LightBuilder.ShadowType
    LightType: LightType
    SourcePosition: Point
    UseWithAdvancedStudioImageBasedLighting: bool
    UseWithIbl: bool
    UseWithRayTracedImageBasedLighting: bool


    class ShadowType(enum.Enum):
        None = 0
        SoftEdged = 1
        HardEdged = 2
        TranslucentHard = 3
    

    class LightMode(enum.Enum):
        FixedToObserver = 0
        FixedToThePart = 1
    

class LayerSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def IsValidLayerOption(self, layerOption: Display.LayerSettingsBuilder.LayerOptionType) -> bool:
        ...
    def Validate(self) -> bool:
        ...
    Layer: int
    LayerOption: Display.LayerSettingsBuilder.LayerOptionType


    class LayerOptionType(enum.Enum):
        Maintain = 0
        Original = 1
        Work = 2
        UserDefined = 3
    

class IRayPlusStudioPreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    AutoCompletionCustomPixelRatio: float
    AutoCompletionCustomQualityFactor: float
    DynamicIRayPlusCaustics: bool
    DynamicIRayPlusStudioRenderMode: Display.IRayPlusStudioPreferencesBuilder.DynamicIRayPlusStudioRenderModeType
    DynamicIRayPlusStudioTime: DateBuilder
    EyeSeparation: float
    IRayPlusStudioDenoiserToggle: bool
    IRayPlusStudioStaticImageDotsPerInch: int
    IRayPlusStudioStaticImageDoubleHeight: float
    IRayPlusStudioStaticImageDoubleWidth: float
    IRayPlusStudioStaticImageFileFormat: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageFileFormatType
    IRayPlusStudioStaticImageLockAspectRatio: bool
    IRayPlusStudioStaticImageOrientation: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageOrientationType
    IRayPlusStudioStaticImagePixelHeight: int
    IRayPlusStudioStaticImagePixelWidth: int
    IRayPlusStudioStaticImageResolution: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageResolutionType
    IRayPlusStudioStaticImageSize: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageSizeType
    IRayPlusStudioStaticImageUnits: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageUnitsType
    IRayPlusStudioStaticImageVrHeight: int
    IRayPlusStudioStaticImageVrWidth: int
    IRayPlusStudioshowStatusIndicator: bool
    LensType: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioLensType
    RemoteRenderFormat: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderFormatType
    RemoteRenderIP: str
    RemoteRenderPassword: str
    RemoteRenderReserveNodes: int
    RemoteRenderSecurityToken: str
    RemoteRenderToggle: bool
    RemoteRenderType: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderType
    RemoteRenderUsername: str
    RemoteRenderVideoMode: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderVideoType
    StaticAutoCompletionType: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioAutoCompletionType
    StaticIRayPlusStudioTime: DateBuilder
    StaticRenderDuration: Display.IRayPlusStudioPreferencesBuilder.StaticRenderDurationType
    StaticRenderNumberOfIterations: int
    StereoLayout: Display.IRayPlusStudioPreferencesBuilder.IRayPlusStudioStereoLayoutType
    VrCamera: CartesianCoordinateSystem
    VrEnabledToggle: bool


    class StaticRenderDurationType(enum.Enum):
        NumberOfIterations = 0
        TimeLimit = 1
        AutoComplete = 2
        TimeLimitedAutoComplete = 3
    

    class IRayPlusStudioStereoLayoutType(enum.Enum):
        TopBottom = 0
        SideBySide = 1
    

    class IRayPlusStudioStaticImageUnitsType(enum.Enum):
        Pixels = 0
        Millimeters = 1
        Inches = 2
    

    class IRayPlusStudioStaticImageSizeType(enum.Enum):
        RenderWindow = 0
        UserDefined = 1
    

    class IRayPlusStudioStaticImageResolutionType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        UserDefined = 3
    

    class IRayPlusStudioStaticImageOrientationType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class IRayPlusStudioStaticImageFileFormatType(enum.Enum):
        Tif = 0
        Png = 1
        Jpg = 2
    

    class IRayPlusStudioRemoteRenderVideoType(enum.Enum):
        Streaming = 0
        Synchronous = 1
    

    class IRayPlusStudioRemoteRenderType(enum.Enum):
        Cluster = 0
        Vca = 1
        SecuredCluster = 2
    

    class IRayPlusStudioRemoteRenderFormatType(enum.Enum):
        H264 = 0
        Lossless = 1
        Png = 2
        Jpeg = 3
    

    class IRayPlusStudioLensType(enum.Enum):
        Monospherical = 0
        Stereospherical = 1
    

    class IRayPlusStudioAutoCompletionType(enum.Enum):
        Simple = 0
        Normal = 1
        Complex = 2
        None = 3
        Custom = 4
    

    class DynamicIRayPlusStudioRenderModeType(enum.Enum):
        Photoreal = 0
        QualityInteractive = 1
        FastInteractive = 2
    

class IRayPlusStudioEditorBuilder(Builder):
    def __init__(self) -> None: ...
    AutoCompletionCustomPixelRatio: float
    AutoCompletionCustomQualityFactor: float
    DynamicIRayPlusCaustics: bool
    DynamicIRayPlusStudioRenderMode: Display.IRayPlusStudioEditorBuilder.DynamicIRayPlusStudioRenderModeType
    DynamicIRayPlusStudioTime: DateBuilder
    EyeSeparation: float
    IRayPlusStudioDenoiserToggle: bool
    IRayPlusStudioStaticImageDotsPerInch: int
    IRayPlusStudioStaticImageDoubleHeight: float
    IRayPlusStudioStaticImageDoubleWidth: float
    IRayPlusStudioStaticImageFileFormat: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType
    IRayPlusStudioStaticImageLockAspectRatio: bool
    IRayPlusStudioStaticImageOrientation: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageOrientationType
    IRayPlusStudioStaticImagePixelHeight: int
    IRayPlusStudioStaticImagePixelWidth: int
    IRayPlusStudioStaticImageResolution: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageResolutionType
    IRayPlusStudioStaticImageSize: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType
    IRayPlusStudioStaticImageUnits: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageUnitsType
    IRayPlusStudioStaticImageVrHeight: int
    IRayPlusStudioStaticImageVrWidth: int
    IRayPlusStudioshowStatusIndicator: bool
    LensType: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioLensType
    RemoteRenderFormat: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderFormatType
    RemoteRenderIP: str
    RemoteRenderPassword: str
    RemoteRenderReserveNodes: int
    RemoteRenderSecurityToken: str
    RemoteRenderToggle: bool
    RemoteRenderType: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderType
    RemoteRenderUsername: str
    RemoteRenderVideoMode: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderVideoType
    StaticAutoCompletionType: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioAutoCompletionType
    StaticIRayPlusStudioTime: DateBuilder
    StaticRenderDuration: Display.IRayPlusStudioEditorBuilder.StaticRenderDurationType
    StaticRenderNumberOfIterations: int
    StereoLayout: Display.IRayPlusStudioEditorBuilder.IRayPlusStudioStereoLayoutType
    VrCamera: CartesianCoordinateSystem
    VrEnabledToggle: bool


    class StaticRenderDurationType(enum.Enum):
        NumberOfIterations = 0
        TimeLimit = 1
        AutoComplete = 2
        TimeLimitedAutoComplete = 3
    

    class IRayPlusStudioStereoLayoutType(enum.Enum):
        TopBottom = 0
        SideBySide = 1
    

    class IRayPlusStudioStaticImageUnitsType(enum.Enum):
        Pixels = 0
        Millimeters = 1
        Inches = 2
    

    class IRayPlusStudioStaticImageSizeType(enum.Enum):
        RenderWindow = 0
        UserDefined = 1
    

    class IRayPlusStudioStaticImageResolutionType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
        UserDefined = 3
    

    class IRayPlusStudioStaticImageOrientationType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class IRayPlusStudioStaticImageFileFormatType(enum.Enum):
        Tif = 0
        Png = 1
        Jpg = 2
    

    class IRayPlusStudioRemoteRenderVideoType(enum.Enum):
        Streaming = 0
        Synchronous = 1
    

    class IRayPlusStudioRemoteRenderType(enum.Enum):
        Cluster = 0
        Vca = 1
        SecuredCluster = 2
    

    class IRayPlusStudioRemoteRenderFormatType(enum.Enum):
        H264 = 0
        Lossless = 1
        Png = 2
        Jpeg = 3
    

    class IRayPlusStudioLensType(enum.Enum):
        Monospherical = 0
        Stereospherical = 1
    

    class IRayPlusStudioAutoCompletionType(enum.Enum):
        Simple = 0
        Normal = 1
        Complex = 2
        None = 3
        Custom = 4
    

    class DynamicIRayPlusStudioRenderModeType(enum.Enum):
        Photoreal = 0
        QualityInteractive = 1
        FastInteractive = 2
    

class IrayPlusStudioAnimationBuilder(Builder):
    def __init__(self) -> None: ...
    AnimationCustomEndTime: float
    AnimationCustomHeight: int
    AnimationCustomStartTime: float
    AnimationCustomWidth: int
    AnimationFileOutput: Display.IrayPlusStudioAnimationBuilder.AnimationFileOutputType
    AnimationFrameNumOfIterations: int
    AnimationFrameTimeLimit: DateBuilder
    AnimationResolution: Display.IrayPlusStudioAnimationBuilder.AnimationResolutionType
    AnimationSolution: str
    AutoCompletionCustomPixelRatio: float
    AutoCompletionCustomQualityFactor: float
    AutoCompletionType: Display.IrayPlusStudioAnimationBuilder.AnimationAutoCompletionType
    Caustics: bool
    CustomFrameRate: int
    Denoiser: bool
    FileInput: str
    FolderInput: str
    FrameRate: Display.IrayPlusStudioAnimationBuilder.FramesPerSecondRateType
    LockAspectRatio: bool
    ProcessingType: Display.IrayPlusStudioAnimationBuilder.AnimationProcessingType
    RemoteRender: bool
    RenderDuration: Display.IrayPlusStudioAnimationBuilder.AnimationRenderDurationType
    RenderQuality: Display.IrayPlusStudioAnimationBuilder.AnimationRenderQualityType
    ScheduledTaskName: str
    ScheduledTaskPriority: int
    TimeRange: Display.IrayPlusStudioAnimationBuilder.AnimationTimeRangeType


    class FramesPerSecondRateType(enum.Enum):
        Fps15 = 0
        Fps24 = 1
        Fps30 = 2
        Fps60 = 3
        Fps120 = 4
        UserDefined = 5
    

    class AnimationTimeRangeType(enum.Enum):
        EntireTimeline = 0
        UserDefined = 1
    

    class AnimationResolutionType(enum.Enum):
        RenderWindow = 0
        UserDefined = 1
    

    class AnimationRenderQualityType(enum.Enum):
        Photoreal = 0
        QualityInteractive = 1
        FastInteractive = 2
    

    class AnimationRenderDurationType(enum.Enum):
        IterationsperFrame = 0
        TimeperFrame = 1
        AutoComplete = 2
        TimeLimitedAutoComplete = 3
    

    class AnimationProcessingType(enum.Enum):
        Interactive = 0
        Offline = 1
    

    class AnimationFileOutputType(enum.Enum):
        MicrosoftAVI = 0
        SeriesofPNG = 1
        SeriesofJPG = 2
        SeriesofTIF = 3
    

    class AnimationAutoCompletionType(enum.Enum):
        Complex = 0
        Normal = 1
        Simple = 2
        None = 3
        Custom = 4
    

class IrayPlusSimpleMaterialEditorBuilder(Builder):
    def __init__(self) -> None: ...
    def GetColorPicker(self) -> float:
        ...
    def SetColorPicker(self, colorPicker: float) -> None:
        ...
    def SaveMaterialsButton(self) -> None:
        ...
    def ExportXMLButton(self) -> None:
        ...
    AspectRatio: float
    FileBrowser: str
    LatitudeScale: float
    LongitudeScale: float
    NameString: str
    NormalVector: Direction
    Scale: float
    TextureSpaceEnum: Display.IrayPlusSimpleMaterialEditorBuilder.TextureSpace
    TexturedToggle: bool
    UScale: float
    UpVector: Direction
    VScale: float


    class TextureSpace(enum.Enum):
        Box = 0
        Planar = 1
        Cylindrical = 2
        Spherical = 3
        UVMap = 4
    

class IrayPlusMaterialEditorBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMaterialLayersInfo(self, typeList: str, uniqueNameList: str) -> None:
        ...
    def GetComponentInfo(self, componentName: str, attribueObject: Display.IrayPlusMaterialAttribute, attribList: str) -> None:
        ...
    def AddComponent(self, componentType: str, addedLayerIndex: int) -> str:
        ...
    def RemoveComponent(self, index: int, componentType: str) -> None:
        ...
    def MoveComponent(self, index: int, componentType: str, moveUp: bool) -> None:
        ...
    def GetComponentParameter(self, attribueName: str) -> Display.IrayPlusMaterialAttribute:
        ...
    def GetComponentParameterValue(self, attribueName: str) -> str:
        ...
    def SetComponentParameter(self, attribueName: str, attribueObject: Display.IrayPlusMaterialAttribute, changedAttrib: str) -> None:
        ...
    def SetComponentParameterValue(self, attribueName: str, attribueValue: str, changedAttrib: str) -> None:
        ...
    def SaveToSystemStudioMaterials(self, saveXmlFileName: str) -> None:
        ...
    def ExportToXMLFile(self, exportXmlFileName: str) -> None:
        ...
    def ExportToMDLFile(self, exportMdlFileName: str) -> None:
        ...
    def GetImageParameterFullPath(self, imageAttribueName: str) -> str:
        ...
    MaterialName: str
    PreviewToggle: bool


    class MappingProjections(enum.Enum):
        Uv = 0
        Planar = 1
        Box = 2
        Spherical = 3
        Cylindrical = 4
    

    class LayerType(enum.Enum):
        Coatings = 0
        Base = 1
        Geometry = 2
        TextureSpace = 3
        MaxNumber = 4
    

    class CoordinateSpaceType(enum.Enum):
        Model = 0
        World = 1
    

class IrayPlusMaterialAttributeEnum(Display.IrayPlusMaterialAttribute):
    def __init__(self) -> None: ...
    EnumValue: int


class IrayPlusMaterialAttribute(TaggedObject):
    def __init__(self) -> None: ...
    def SetValueFromString(self, attribueValue: str) -> None:
        ...
    def GetValueAsString(self) -> str:
        ...
    ParameterName: str


class ImageDataCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.ImageData]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Display.ImageData:
        ...
    def Tag(self) -> Tag: ...



class ImageData(NXObject):
    def __init__(self) -> None: ...


class ImageCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.ImageBase]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Display.ImageBase:
        ...
    def CreateRasterImageBuilder(self, image: Display.RasterImage) -> Display.RasterImageBuilder:
        ...
    def Tag(self) -> Tag: ...



class ImageBasedLighting(Builder):
    def __init__(self) -> None: ...
    def CommitAndDisplay(self, view: View, updateDisplay: bool) -> None:
        ...
    Accuracy: float
    ColorSaturation: float
    Image: Display.Image
    ImageBlur: Display.ImageBasedLighting.ImageBlurType
    ImageFilename: str
    ImageRotation: float
    ImageType: Display.ImageBasedLighting.ImagesType
    ImageUpVector: Direction
    ImageUpVectorType: Display.ImageBasedLighting.ImageUpVectorTypes
    Intensity: float
    LwrtAngle: float
    LwrtIntensity: float
    LwrtQuality: float
    ShadowSoftness: float
    ShadowType: Display.ImageBasedLighting.ShadowsType
    UseImageBasedLighting: bool
    UseLightsForShadowCatcherInHqi: bool
    UseLightsForShadowCatcherInLwrt: bool
    UseLwrtImageBasedLighting: bool


    class ShadowsType(enum.Enum):
        None = 0
        SoftEdged = 1
        HardEdged = 2
        TranslucentHard = 3
    

    class ImageUpVectorTypes(enum.Enum):
        AlignWithFloorPlane = 0
        UserDefined = 1
    

    class ImagesType(enum.Enum):
        Background = 0
        Stage = 1
        UserDefined = 2
        LightingOnly = 3
    

    class ImageBlurType(enum.Enum):
        None = 0
        Low = 1
        Medium = 2
        High = 3
    

class ImageBaseBuilder(Builder):
    def __init__(self) -> None: ...
    def AlignImageToReferenceDirection(self) -> None:
        ...
    def RotateLeft(self) -> None:
        ...
    def RotateRight(self) -> None:
        ...
    def FlipHorizontal(self) -> None:
        ...
    def FlipVertical(self) -> None:
        ...
    def OrientViewToImage(self) -> None:
        ...
    def GetImagesInPart(self) -> str:
        ...
    def SetImageFromPart(self, imageName: str) -> None:
        ...
    def GetCornerPoints(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> None:
        ...
    def SetCornerPoints(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> None:
        ...
    def GetTransparentPixelColor(self) -> float:
        ...
    def SetTransparentPixelColor(self, transparencyColor: float) -> None:
        ...
    def GetForegroundColor(self) -> float:
        ...
    def SetForegroundColor(self, foregroundColor: float) -> None:
        ...
    def GetBackgroundColor(self) -> float:
        ...
    def SetBackgroundColor(self, backgroundColor: float) -> None:
        ...
    def ResetImageSize(self) -> None:
        ...
    BasePointChoice: Display.ImageBaseBuilder.BasePointChoices
    ColorMode: Display.ImageBaseBuilder.ImageColorModes
    Height: Expression
    ImageFile: str
    ImageReferencePoint1: Point
    ImageReferencePoint2: Point
    ImageReferencePoint3: Point
    InsertionPointLocation: Point3d
    InsertionPointOption: Display.ImageBaseBuilder.InsertionPoint
    LockAspectRatio: bool
    ModelReferencePoint1: Point
    ModelReferencePoint2: Point
    ModelReferencePoint3: Point
    OverallTranslucency: int
    PixelColorTolerance: int
    ReferenceDirectionOption: Display.ImageBaseBuilder.ReferenceDirection
    RotateAngleOfReferenceVector: Expression
    SizeOption: Display.ImageBaseBuilder.SizeOptions
    TransparencyColorOption: Display.ImageBaseBuilder.TransparencyColorFrom
    UserBasePoint: Point
    UserInsertionPoint: Point
    UserReferenceDirection: Direction
    Width: Expression


    class TransparencyColorFrom(enum.Enum):
        None = 0
        FromImage = 1
        PixelColor = 2
    

    class SizeOptions(enum.Enum):
        UserDefined = 0
        ImageSize = 1
        ReferenceScaling = 2
    

    class ReferenceDirection(enum.Enum):
        Horizontal = 0
        Vertical = 1
    

    class InsertionPoint(enum.Enum):
        Default = 0
        UserDefined = 1
    

    class ImageColorModes(enum.Enum):
        Rgb = 0
        Greyscale = 1
        Monochrome = 2
    

    class BasePointChoices(enum.Enum):
        BottomLeft = 0
        BottomCenter = 1
        BottomRight = 2
        MiddleLeft = 3
        MiddleCenter = 4
        MiddleRight = 5
        TopLeft = 6
        TopCenter = 7
        TopRight = 8
        UserDefined = 9
    

class ImageBase(DisplayableObject):
    def __init__(self) -> None: ...


class Image(Builder):
    def __init__(self) -> None: ...
    def ImageFileSelect(self) -> None:
        ...
    def ImagePaletteSelect(self) -> None:
        ...
    ImagePreviewToggle: bool
    PatternRepeatFactor: float


class IDynamicSectionCutCreator():
    def Find(self, journalIdentifier: str) -> Display.DynamicSectionCut:
        ...
    def GetSectionCuts(self, contextOccurrence: NXObject, view: View, sectionCuts: typing.List[Display.DynamicSectionCut]) -> None:
        ...


class GridCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.Grid]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreatePlaneGridBuilder(self, grid: Display.PlaneGrid) -> Display.PlaneGridBuilder:
        ...
    def CreateDatumPlaneGridBuilder(self, grid: Display.DatumPlaneGrid) -> Display.DatumPlaneGridBuilder:
        ...
    def CreateDatumPlaneGridBuilder(self, datumPlanes: typing.List[DatumPlane]) -> Display.DatumPlaneGridBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Display.Grid:
        ...
    def GetDatumPlaneGrid(self, datumPlane: DatumPlane) -> Display.DatumPlaneGrid:
        ...
    def CreatePlanarShipGridBuilder(self, grid: Display.PlanarShipGrid) -> Display.PlanarShipGridBuilder:
        ...
    def Tag(self) -> Tag: ...



class GridBuilder(Builder):
    def __init__(self) -> None: ...
    def InheritSettings(self, grid: Display.Grid) -> None:
        ...
    LineColor: NXColor
    MajorLineSpacing: float
    MajorLineStyle: Display.GridBuilder.LineStyleType
    MajorLineWeight: Display.GridBuilder.LineWeightType
    MinorLineStyle: Display.GridBuilder.LineStyleType
    MinorLineWeight: Display.GridBuilder.LineWeightType
    MinorLinesPerMajor: int
    Show: bool
    ShowMajorLines: bool
    ShowOnTop: bool
    SnapPointsPerMinor: int
    SnapToGrid: bool


    class LineWeightType(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 3
        Two = 4
        Three = 5
        Four = 6
        Five = 7
        Six = 8
        Seven = 9
        Eight = 10
        Nine = 11
    

    class LineStyleType(enum.Enum):
        Solid = 0
        Dashed = 1
        Phantom = 2
        Centerline = 3
        Dotted = 4
        Longdash = 5
        Dotdash = 6
        Eight = 7
        Nine = 8
        Ten = 9
        Eleven = 10
    

class Grid(DisplayableObject):
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> Display.DynamicSectionCut:
        ...
    def GetSectionCuts(self, contextOccurrence: NXObject, view: View, sectionCuts: typing.List[Display.DynamicSectionCut]) -> None:
        ...


class GlobalIlluminationBuilder(Builder):
    def __init__(self) -> None: ...
    IntensityDouble: float
    StaticFinalGatherQuality: float
    StationaryFinalGatherQuality: float


class FacetSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetShadedEdgeTol(self, shadedTolerance: Display.FacetSettingsBuilder.ShadedToleranceSetting) -> float:
        ...
    def SetShadedEdgeTol(self, shadedTolerance: Display.FacetSettingsBuilder.ShadedToleranceSetting, shadedEdgeTol: float) -> None:
        ...
    def GetShadedFaceTol(self, shadedTolerance: Display.FacetSettingsBuilder.ShadedToleranceSetting) -> float:
        ...
    def SetShadedFaceTol(self, shadedTolerance: Display.FacetSettingsBuilder.ShadedToleranceSetting, shadedFaceTol: float) -> None:
        ...
    def GetShadedAngleTol(self, shadedTolerance: Display.FacetSettingsBuilder.ShadedToleranceSetting) -> float:
        ...
    def SetShadedAngleTol(self, shadedTolerance: Display.FacetSettingsBuilder.ShadedToleranceSetting, shadedAngleTol: float) -> None:
        ...
    def GetAdvVisEdgeTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        ...
    def SetAdvVisEdgeTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting, advVisEdgeTol: float) -> None:
        ...
    def GetAdvVisFaceTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        ...
    def SetAdvVisFaceTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting, advVisFaceTol: float) -> None:
        ...
    def GetAdvVisAngleTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        ...
    def SetAdvVisAngleTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting, advVisAngleTol: float) -> None:
        ...
    def GetAdvVisWidthTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        ...
    def SetAdvVisWidthTol(self, advVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting, advVisWidthTol: float) -> None:
        ...
    def RegenerateDisplayFacets(self, deleteSavedDisplayFacets: bool, regenerateChildren: bool, partScope: BasePart) -> None:
        ...
    AdvVisAlignFacets: bool
    AdvVisFacetRatio: float
    AdvVisFacetScale: Display.FacetSettingsBuilder.FacetScale
    AdvVisFacetToViewRatio: Display.FacetSettingsBuilder.FacetToViewRatio
    AdvVisRefinementFactor: float
    AdvVisTolerance: Display.FacetSettingsBuilder.AdvVisToleranceSetting
    AdvVisUpdate: Display.FacetSettingsBuilder.FacetUpdate
    FullLoadToSaveDisplayFacets: bool
    ShadedAlignFacets: bool
    ShadedFacetRatio: float
    ShadedFacetScale: Display.FacetSettingsBuilder.FacetScale
    ShadedFacetToViewRatio: Display.FacetSettingsBuilder.FacetToViewRatio
    ShadedRefinementFactor: float
    ShadedTolerance: Display.FacetSettingsBuilder.ShadedToleranceSetting
    ShadedUpdate: Display.FacetSettingsBuilder.FacetUpdate
    ShowFacetEdges: bool


    class ShadedToleranceSetting(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        ExtraFine = 3
        UltraFine = 4
        UserDefined = 5
    

    class FacetUpdate(enum.Enum):
        VisibleObjects = 0
        AllObjects = 1
        None = 2
    

    class FacetToViewRatio(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

    class FacetScale(enum.Enum):
        Fixed = 0
        Part = 1
        View = 2
    

    class AdvVisToleranceSetting(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        ExtraFine = 3
        SuperFine = 4
        UltraFine = 5
        UserDefined = 6
    

class ExtractScene(Builder):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def ImageFileSelect(self) -> None:
        ...
    def GetSceneDescription(self) -> str:
        ...
    def SetSceneDescription(self, sceneDescription: str) -> None:
        ...
    SceneName: str


class EnvironmentBuilder(Builder):
    def __init__(self) -> None: ...
    def GetGroundReflectionColor(self) -> float:
        ...
    def SetGroundReflectionColor(self, groundReflectionColor: float) -> None:
        ...
    def CommitAndDisplay(self, view: View, updateIblDisplay: bool, updateEnvCubeDisplay: bool) -> None:
        ...
    def CommitOffset(self, view: View) -> None:
        ...
    def FloorXaxis(self) -> None:
        ...
    def FloorYaxis(self) -> None:
        ...
    def FloorZaxis(self) -> None:
        ...
    def AlignFloorPlane(self, specifyFloorPlane: Plane) -> None:
        ...
    ColorSaturation: float
    EnvironmentShadedViewsFixGroundPlaneOffset: bool
    EnvironmentShadedViewsGlobalFinish: int
    EnvironmentShadedViewsGroundPlane: int
    EnvironmentShadedViewsGroundPlaneCustom: Plane
    EnvironmentShadedViewsGroundPlaneOffset: float
    EnvironmentShadedViewsGroundRefReflectivity: float
    EnvironmentShadedViewsShowGroundReflection: bool
    GroundGlossiness: float
    GroundPlaneType: Display.EnvironmentBuilder.GroundPlaneTypes
    GroundReflection: bool
    GroundVisibility: bool
    Image: Display.Image
    ImageBlur: Display.EnvironmentBuilder.ImageBlurType
    ImageFilename: str
    ImageRotation: float
    ImageUpVector: Direction
    ImageUpVectorType: Display.EnvironmentBuilder.ImageUpVectorTypes
    LightIntensity: float
    LwrtAngle: float
    LwrtIntensity: float
    LwrtQuality: float
    OffsetExpression: Expression
    Reflectivity: float
    SizeExpression: Expression
    SpecifyGroundPlane: Plane
    UseEnvironment: bool
    UseLightsForShadowCatcherInLwrt: bool
    UseLwrtEnvironment: bool
    ViewFitToStage: bool


    class ToneMappingTypes(enum.Enum):
        SystemScene = 0
        UserDefined = 1
    

    class ImageUpVectorTypes(enum.Enum):
        AlignWithFloorPlane = 0
        UserDefined = 1
    

    class ImageBlurType(enum.Enum):
        None = 0
        Low = 1
        Medium = 2
        High = 3
    

    class GroundPlaneTypes(enum.Enum):
        Yz = 0
        Xz = 1
        Xy = 2
        UserDefined = 3
    

    class GlobalFinishType(enum.Enum):
        ShinyPlastic = 0
        ClassicSatin = 1
        MattePlastic = 2
        Flat = 3
        UserDefined = 4
    

class EntitySelectionPlane(DisplayableObject):
    def __init__(self) -> None: ...


class DynamicSectionTypes(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class Type(enum.Enum):
        OnePlane = 0
        TwoParallelPlanes = 1
        Box = 2
    

    class CurveColorOption(enum.Enum):
        Body = 0
        Any = 1
    

    class CoordinateSystem(enum.Enum):
        Absolute = 0
        Wcs = 1
    

    class Clip(enum.Enum):
        Section = 0
        Slice = 1
    

    class CapColorOption(enum.Enum):
        Body = 0
        Any = 1
    

    class Axis(enum.Enum):
        None = 0
        X = 1
        Y = 2
        Z = 3
    

    class ActivePlane(enum.Enum):
        Primary = 0
        Secondary = 1
    

class DynamicSectionCut(NXObject):
    def __init__(self) -> None: ...
    def PrepareForMeasure(self, contextOccurrence: NXObject, view: View) -> None:
        ...
    def PrepareForMeasure(self, exactMeasure: bool, contextOccurrence: NXObject, view: View) -> None:
        ...
    CutObject: INXObject


class DynamicSectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.DynamicSection]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateSectionBuilder(self, section: Display.DynamicSection, view: ModelingView) -> Display.DynamicSectionBuilder:
        ...
    def CreateSectionBuilder(self, view: ModelingView) -> Display.DynamicSectionBuilder:
        ...
    def CopySections(self, sections: typing.List[Display.DynamicSection], deleteOriginals: bool) -> typing.List[Display.DynamicSection]:
        ...
    def DeleteSections(self, addUndoMark: bool, sections: typing.List[Display.DynamicSection]) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> Display.DynamicSection:
        ...
    def MoveToDefaultLayer(self, dynamicSections: typing.List[Display.DynamicSection]) -> None:
        ...
    def Tag(self) -> Tag: ...



class DynamicSectionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetActivePlane(self, planeAxis: Display.DynamicSectionTypes.Axis, activePlane: Display.DynamicSectionTypes.ActivePlane) -> None:
        ...
    def SetActivePlane(self, planeAxis: Display.DynamicSectionTypes.Axis, activePlane: Display.DynamicSectionTypes.ActivePlane) -> None:
        ...
    def AlternatePlane(self) -> None:
        ...
    def CreateDatumPlane(self) -> DatumPlane:
        ...
    def EditView(self, view: ModelingView) -> None:
        ...
    def ShowCurvePreview(self, showCurvePreview: bool) -> None:
        ...
    def GetGridSettings(self) -> Display.PlaneGridBuilder:
        ...
    def GetName(self) -> str:
        ...
    def SetName(self, sectionName: str) -> bool:
        ...
    def GetNormal(self) -> Vector3d:
        ...
    def SetNormal(self, normal: Vector3d) -> None:
        ...
    def GetOffset(self) -> float:
        ...
    def SetOffset(self, offset: float) -> None:
        ...
    def GetOffsetLimits(self, minimumOffset: float, maximumOffset: float) -> None:
        ...
    def GetOrigin(self) -> Point3d:
        ...
    def SetOrigin(self, origin: Point3d) -> None:
        ...
    def OffsetOriginInPlane(self, xOffset: float, yOffset: float) -> None:
        ...
    def GetPlaneThickness(self) -> float:
        ...
    def SetPlaneThickness(self, planeThickness: float) -> None:
        ...
    def GetRotationAngle(self, rotationAxis: Display.DynamicSectionTypes.Axis) -> float:
        ...
    def SetRotationAngle(self, rotationAxis: Display.DynamicSectionTypes.Axis, angle: float) -> None:
        ...
    def GetRotationMatrix(self) -> Matrix3x3:
        ...
    def SetRotationMatrix(self, rotationAxis: Display.DynamicSectionTypes.Axis, rotationMatrix: Matrix3x3) -> None:
        ...
    def LoadAllIntersecting(self, loadStatus: PartLoadStatus) -> bool:
        ...
    def LoadNearIntersecting(self, loadStatus: PartLoadStatus) -> bool:
        ...
    def PlaneX(self) -> None:
        ...
    def PlaneY(self) -> None:
        ...
    def PlaneZ(self) -> None:
        ...
    def RestoreView(self) -> None:
        ...
    def ReverseDirection(self) -> None:
        ...
    def SaveCurves(self, groupName: str) -> None:
        ...
    def IsDefaultPlane(self) -> bool:
        ...
    def SetDefaultPlane(self) -> None:
        ...
    def SetDefaults(self) -> None:
        ...
    def SetOffsetByPoint(self, point: Point3d) -> None:
        ...
    def SetPlane(self, axisOrigin: Point3d, origin: Point3d, rotationMatrix: Matrix3x3) -> None:
        ...
    def SetAssociativePlane(self, planeTag: Plane) -> None:
        ...
    def IsAssociativitySupported(self) -> bool:
        ...
    def ShowSectionCurves(self, showCurves: bool) -> None:
        ...
    def UpdateBoxExtents(self) -> None:
        ...
    def GetAllPlanesGeometry(self, planeOrigins: typing.List[Point3d], planeMetrices: typing.List[Matrix3x3]) -> None:
        ...
    def GetPlaneGeometry(self, axisType: Display.DynamicSectionTypes.Axis, planeType: Display.DynamicSectionTypes.ActivePlane, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def SetAllPlanesGeometry(self, planeOrigins: typing.List[Point3d], planeMetrices: typing.List[Matrix3x3]) -> bool:
        ...
    def GetBoundingBox(self, minCornerPt: Point3d, maxCornerPt: Point3d) -> None:
        ...
    def SetBoundingBox(self, minCornerPt: Point3d, maxCornerPt: Point3d) -> None:
        ...
    BoxExtentDelayUpdate: bool
    BoxExtentMargin: float
    BoxExtentObjects: SelectINXObjectList
    BoxExtentSupported: bool
    CapColor: NXColor
    CapColorOption: Display.DynamicSectionTypes.CapColorOption
    ClipType: Display.DynamicSectionTypes.Clip
    CsysType: Display.DynamicSectionTypes.CoordinateSystem
    CurveColor: NXColor
    CurveColorOption: Display.DynamicSectionTypes.CurveColorOption
    DefaultPlaneAxis: Display.DynamicSectionTypes.Axis
    DeferCurveUpdate: bool
    InterferenceColor: NXColor
    LayerSettings: Display.LayerSettingsBuilder
    LockPlanes: bool
    NumberInSeries: int
    ReverseSeries: bool
    SeriesSpacing: float
    ShowCap: bool
    ShowClip: bool
    ShowCurves: bool
    ShowGrid: bool
    ShowInterference: bool
    ShowViewer: bool
    Type: Display.DynamicSectionTypes.Type
    View: ModelingView


class DynamicSection(NXObject):
    def __init__(self) -> None: ...
    def UpdateSectionCuts(self, updateOption: Update.Option) -> None:
        ...
    def Find(self, journalIdentifier: str) -> Display.DynamicSectionCut:
        ...
    def GetSectionCuts(self, contextOccurrence: NXObject, view: View, sectionCuts: typing.List[Display.DynamicSectionCut]) -> None:
        ...


class DownloadOfflineRenderingBuilder(Builder):
    def __init__(self) -> None: ...
    AVICompression: int
    AVIFileName: str
    CustomFrameRate: int
    FrameRate: Display.DownloadOfflineRenderingBuilder.FrameRateType
    SelectedBatchJob: str


    class FrameRateType(enum.Enum):
        Fps15 = 0
        Fps24 = 1
        Fps30 = 2
        Fps60 = 3
        Fps120 = 4
        UserDefined = 5
    

class DecalStickerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetManipulatorData(self, origin: Point3d, csys: Matrix3x3) -> None:
        ...
    def SetManipulatorData(self, origin: Point3d, csys: Matrix3x3) -> None:
        ...
    def ResetImageSize(self) -> None:
        ...
    def GetTransparencyPixelColor(self) -> Display.DecalStickerBuilder.Color:
        ...
    def SetTransparencyPixelColor(self, transparencyColor: Display.DecalStickerBuilder.Color) -> None:
        ...
    def UpdateDecalStickerOnImageDimensionChange(self) -> None:
        ...
    AnchorType: Display.DecalStickerBuilder.AnchorTypes
    Bump: bool
    DecalName: str
    FaceOrBody: SelectNXObjectList
    FilterDecalImages: bool
    FitPreview: bool
    Height: Expression
    ImageName: str
    LockAspectRatio: bool
    MaximumPixelSize: Display.DecalStickerBuilder.PixelSizes
    Origin: Point
    PixelColorTolerance: int
    ProjectionType: Display.DecalStickerBuilder.ProjectionTypes
    ReflectivityType: Display.DecalStickerBuilder.ReflectivityTypes
    RotationAngle: Expression
    ScalingMethodType: Display.DecalStickerBuilder.ScalingMethodTypes
    Strength: float
    TransparencyType: Display.DecalStickerBuilder.TransparencyTypes
    UVTransformationData: Display.UVTransformationData
    Width: Expression


    class TransparencyTypes(enum.Enum):
        None = 0
        FromImage = 1
        PixelColor = 2
    

    class ScalingMethodTypes(enum.Enum):
        UserDefined = 0
        ImageSize = 1
    

    class ReflectivityTypes(enum.Enum):
        FromVisualMaterial = 0
        Matte = 1
        Plastic = 2
        Mirror = 3
        Metal = 4
        Glass = 5
    

    class ProjectionTypes(enum.Enum):
        Planar = 0
        Cylindrical = 1
        Spherical = 2
        Uv = 3
    

    class PixelSizes(enum.Enum):
        TrueSize = 0
        OneTwentyEight = 1
        TwoFiftySix = 2
        FiveTwleve = 3
        OneZeroTwoFour = 4
        TwoZeroFourEight = 5
        FourZeroNineSix = 6
    

    class DecalStickerBuilderColor():
        Color1: float
        Color2: float
        Color3: float
        def ToString(self) -> str:
            ...
        def __init__(self, Color1: float, Color2: float, Color3: float) -> None: ...
    

    class AnchorTypes(enum.Enum):
        BottomLeft = 0
        BottomCenter = 1
        BottomRight = 2
        MiddleLeft = 3
        MiddleCenter = 4
        MiddleRight = 5
        TopLeft = 6
        TopCenter = 7
        TopRight = 8
    

class DecalCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Decal]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateDecalBuilder(self, decal: TaggedObject) -> Display.DecalBuilder:
        """[Obsolete("Deprecated in NX1980.0.0.  Please use NXOpen.Display.DecalCollection.CreateDecalStickerBuilder instead.")"""
        ...
    def CreateDecalBuilderFull(self, decal: TaggedObject) -> Display.DecalBuilder:
        """[Obsolete("Deprecated in NX1980.0.0.  Please use NXOpen.Display.DecalCollection.CreateDecalStickerBuilder instead.")"""
        ...
    def CreateDecalStickerBuilder(self, decal: TaggedObject) -> Display.DecalStickerBuilder:
        ...
    def FindDecalObject(self, journalIdentifier: str) -> Decal:
        ...
    def Tag(self) -> Tag: ...



class DecalBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTransparencyColor(self) -> float:
        """[Obsolete("Deprecated in NX1980.0.0.  Please use NXOpen.Display.DecalStickerBuilder instead.")"""
        ...
    def SetTransparencyColor(self, transparencyColor: float) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Please use NXOpen.Display.DecalStickerBuilder instead.")"""
        ...
    def GetImagesInPart(self) -> str:
        """[Obsolete("Deprecated in NX1980.0.0.  Please use NXOpen.Display.DecalStickerBuilder instead.")"""
        ...
    def SetImageFromPart(self, imageName: str) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Please use NXOpen.Display.DecalStickerBuilder instead.")"""
        ...
    AnchorType: Display.DecalBuilder.Anchor
    AspectRatio: float
    AxialRotation: float
    DecalName: str
    DecalReflectivity: float
    EnableEngraving: bool
    EngravingAmplitude: float
    EngravingSoftness: float
    HeightScale: float
    IlluminationType: Display.DecalBuilder.DecalIllumination
    Image: Display.Image
    ImageFilename: str
    ImageSizeType: Display.DecalBuilder.ImageSize
    NormalVector: Direction
    NormalVectorValue: Vector3d
    Object: SelectNXObjectList
    Origin: Point
    OriginPosition: Point3d
    OverwriteExistingFile: bool
    ProjectionType: Display.DecalBuilder.Projection
    ReflectivityType: Display.DecalBuilder.DecalReflectivities
    Rotation: float
    RotationX: float
    RotationY: float
    RotationZ: float
    Scale: float
    ScalingType: Display.DecalBuilder.Scaling
    StencilPreview: bool
    TranslationX: float
    TranslationY: float
    TranslationZ: float
    TransparencyTolerance: int
    UpVector: Direction
    UpVectorValue: Vector3d
    WidthScale: float


    class Scaling(enum.Enum):
        ToFace = 0
        ToImageSize = 1
        ToUniformScale = 2
        ToNonUniformScale = 3
    

    class Projection(enum.Enum):
        Planar = 0
        Cylindrical = 1
        Spherical = 2
        Uv = 3
    

    class ImageSize(enum.Enum):
        TrueSize = 0
        OneTwentyEight = 1
        TwoFiftySix = 2
        FiveTwelve = 3
        OneOTwoFour = 4
        TwoOFourEight = 5
        FourONineSix = 6
    

    class DecalReflectivities(enum.Enum):
        UseMatte = 0
        UsePlastic = 1
        UseMirror = 2
        UseMetal = 3
        UseGlass = 4
    

    class DecalIllumination(enum.Enum):
        UseUnderlyingMaterial = 0
        UseDecalMaterial = 1
    

    class Anchor(enum.Enum):
        TopLeft = 0
        Center = 1
        BottomLeft = 2
        TopMiddle = 3
        TopRight = 4
        LeftMiddle = 5
        RightMiddle = 6
        BottomMiddle = 7
        BottomRight = 8
    

class DatumPlaneGridBuilder(Display.BoundedGridBuilder):
    def __init__(self) -> None: ...
    def GetDatumPlanes(self) -> typing.List[DatumPlane]:
        ...
    def SetDatumPlanes(self, datumPlanes: typing.List[DatumPlane]) -> None:
        ...
    GridOrientation: Display.DatumPlaneGridBuilder.GridOrientationType


    class GridOrientationType(enum.Enum):
        FromDatumPlane = 0
        Custom = 1
    

class DatumPlaneGrid(Display.BoundedGrid):
    def __init__(self) -> None: ...


class CgfxMattexCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.CgfxMattex]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateCgfxMattexBuilder(self, cgfxmattex: TaggedObject) -> Display.CgfxMattexBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def Tag(self) -> Tag: ...



class CgfxMattexBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAttributeValues(self) -> typing.List[NXObject]:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def SetAttributeValues(self, attributeValues: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def UpdateMaterialsInPartPaletteEntry(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    MaterialName: str
    ShadowCastingDisabled: bool
    TechniqueType: Display.CgfxMattexBuilder.Technique
    TextureSpaceShaderType: Display.CgfxMattexBuilder.TextureSpaceShader
    UseCameraDirectionPlaneOption: Display.CgfxMattexBuilder.UseCameraDirectionPlane


    class UseCameraDirectionPlane(enum.Enum):
        NormalVector = 0
        NormalAndUpVector = 1
    

    class TextureSpaceShader(enum.Enum):
        ArbitraryPlane = 0
        Cylindrical = 1
        Spherical = 2
        WcsAutoAxis = 3
        Uv = 4
        CameraDirectionPlane = 5
    

    class TextureSpace(enum.Enum):
        DefaultUv = 0
        Edited = 1
    

    class Technique(enum.Enum):
        Base = 0
    

class CgfxMattex(TaggedObject):
    def __init__(self) -> None: ...


class CgfxAttributeValueNumberBuilder(Builder):
    def __init__(self) -> None: ...
    NumberValue: float


class CgfxAttributeValueIntegerBuilder(Builder):
    def __init__(self) -> None: ...
    IntegerValue: int


class CgfxAttributeValueFloat4Builder(Builder):
    def __init__(self) -> None: ...
    def GetFloat4Value(self) -> float:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def SetFloat4Value(self, doubleTableValue: float) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...


class CgfxAttributeValueFloat3Builder(Builder):
    def __init__(self) -> None: ...
    def GetFloat3Value(self) -> float:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def SetFloat3Value(self, doubleTableValue: float) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...


class CgfxAttributeValueFileBuilder(Builder):
    def __init__(self) -> None: ...
    def GetFilename(self) -> str:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def SetFilename(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...


class CgfxAttributeValueColor4Builder(Builder):
    def __init__(self) -> None: ...
    def GetColor4Value(self) -> float:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def SetColor4Value(self, color4Value: float) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...


class CgfxAttributeValueColor3Builder(Builder):
    def __init__(self) -> None: ...
    def GetColor3Value(self) -> float:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def SetColor3Value(self, color3Value: float) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...


class CgfxAttrCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.CgfxAttr]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateAttributeValueIntegerBuilder(self, cgfxAttribute: TaggedObject) -> Display.CgfxAttributeValueIntegerBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def CreateAttributeValueNumberBuilder(self, cgfxAttribute: TaggedObject) -> Display.CgfxAttributeValueNumberBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def CreateAttributeValueColor3Builder(self, cgfxAttribute: TaggedObject) -> Display.CgfxAttributeValueColor3Builder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def CreateAttributeValueColor4Builder(self, cgfxAttribute: TaggedObject) -> Display.CgfxAttributeValueColor4Builder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def CreateAttributeValueFileBuilder(self, cgfxAttribute: TaggedObject) -> Display.CgfxAttributeValueFileBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def CreateAttributeValueFloat3Builder(self, cgfxAttribute: TaggedObject) -> Display.CgfxAttributeValueFloat3Builder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def CreateAttributeValueFloat4Builder(self, cgfxAttribute: TaggedObject) -> Display.CgfxAttributeValueFloat4Builder:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        """[Obsolete("Deprecated in NX10.0.0.  No alternative provided for this class.")"""
        ...
    def Tag(self) -> Tag: ...



class CgfxAttr(TaggedObject):
    def __init__(self) -> None: ...


class CameraCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.Camera]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateCameraBuilder(self, camera: Display.Camera) -> Display.CameraBuilder:
        ...
    def CreateCameraBuilder(self, camera: Display.Camera, applyCameraToView: bool) -> Display.CameraBuilder:
        ...
    def CreateCameraBuilder(self, view: View, layout: Layout, camera: Display.Camera) -> Display.CameraBuilder:
        ...
    def CreateCameraBuilder(self, view: View, layout: Layout, camera: Display.Camera, applyCameraToView: bool) -> Display.CameraBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Display.Camera:
        ...
    def Tag(self) -> Tag: ...



class CameraBuilder(Builder):
    def __init__(self) -> None: ...
    ApertureType: Display.CameraBuilder.Aperture
    AspectRatioHeight: float
    AspectRatioType: Display.CameraBuilder.AspectRatio
    AspectRatioWidth: float
    BackClippingDistance: float
    CameraMatrix: Matrix3x3
    CameraName: str
    CameraNameChar: str
    CameraPosition: Point3d
    DepthOfFieldToggle: bool
    FieldOfViewAngle: float
    FieldOfViewMeasured: Display.CameraBuilder.FovMeasured
    FocalDistance: float
    FrontClippingDistance: float
    HiddenLensFlareToggle: bool
    LensAngleType: Display.CameraBuilder.LensAngle
    LensFlareIntensity: float
    LensFlareToggle: bool
    LensFlareType: Display.CameraBuilder.LensFlare
    Magnification: float
    PerspectiveDistance: float
    StockLensType: Display.CameraBuilder.StockLens
    TargetMatrix: Matrix3x3
    TargetPosition: Point3d
    Type: Display.CameraBuilder.Types
    UseTargetPoint: bool


    class Types(enum.Enum):
        Parallel = 0
        Perspective = 1
    

    class StockLens(enum.Enum):
        S28 = 0
        S35 = 1
        S50 = 2
        S70 = 3
        S105 = 4
        S135 = 5
        S210 = 6
        S300 = 7
    

    class LensFlare(enum.Enum):
        Standard = 0
        S35 = 1
        S50 = 2
        S105 = 3
        Polygonal = 4
        P35 = 5
        P50 = 6
        P105 = 7
        Spark = 8
        Star = 9
    

    class LensAngle(enum.Enum):
        Stock = 0
        Fov = 1
        Magnification = 2
    

    class FovMeasured(enum.Enum):
        Horizontally = 0
        Vertically = 1
    

    class AspectRatio(enum.Enum):
        GraphicsWindow = 0
        ImageBasedBackground = 1
        SquareFormat = 2
        StandardPhotoPrintFormat = 3
        StandardVideoFormat = 4
        HdtvFormat = 5
        UserDefined = 6
    

    class Aperture(enum.Enum):
        F28 = 0
        F56 = 1
        F8 = 2
        F11 = 3
        F16 = 4
        F22 = 5
    

class Camera(NXObject):
    def __init__(self) -> None: ...
    def ApplyToView(self, view: ModelingView) -> None:
        ...
    def CopyToClipboard(self) -> None:
        ...
    def ListInformation(self) -> None:
        ...


class BoundedGridBuilder(Display.GridBuilder):
    def __init__(self) -> None: ...
    def GetCornerPoints(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> bool:
        ...
    def SetCornerPoints(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> bool:
        ...
    def SaveCurves(self, groupName: str) -> None:
        ...
    Associative: bool
    LabelReference: Display.BoundedGridBuilder.LabelReferenceType
    LocalOrigin: Point3d
    SectionCurveSettings: Display.SectionCurveSettingsBuilder
    ShowLabel: Display.BoundedGridBuilder.ShowLabelType


    class ShowLabelType(enum.Enum):
        Always = 0
        ParalleltoView = 1
        None = 2
    

    class LabelReferenceType(enum.Enum):
        Local = 0
        Wcs = 1
        Absolute = 2
    

class BoundedGrid(Display.Grid):
    def __init__(self) -> None: ...


class Background(Builder):
    def __init__(self) -> None: ...
    def GetBottomColor(self) -> float:
        ...
    def SetBottomColor(self, bottomColor: float) -> None:
        ...
    def GetTopColor(self) -> float:
        ...
    def SetTopColor(self, topColor: float) -> None:
        ...
    def GetBackgroundShadedViewsPlain(self) -> float:
        ...
    def SetBackgroundShadedViewsPlain(self, plainColor: float) -> None:
        ...
    def GetBackgroundShadedViewsGraduatedTop(self) -> float:
        ...
    def SetBackgroundShadedViewsGraduatedTop(self, topColor: float) -> None:
        ...
    def GetBackgroundShadedViewsGraduatedBottom(self) -> float:
        ...
    def SetBackgroundShadedViewsGraduatedBottom(self, bottomColor: float) -> None:
        ...
    def GetBackgroundWireframeViewsPlain(self) -> float:
        ...
    def SetBackgroundWireframeViewsPlain(self, plainColor: float) -> None:
        ...
    def GetBackgroundWireframeViewsGraduatedTop(self) -> float:
        ...
    def SetBackgroundWireframeViewsGraduatedTop(self, topColor: float) -> None:
        ...
    def GetBackgroundWireframeViewsGraduatedBottom(self) -> float:
        ...
    def SetBackgroundWireframeViewsGraduatedBottom(self, bottomColor: float) -> None:
        ...
    def ImageFileSelect(self) -> None:
        ...
    def ShadedBackgroundOptionWhite(self) -> None:
        ...
    def ShadedBackgroundOptionLight(self) -> None:
        ...
    def ShadedBackgroundOptionGraduatedLight(self) -> None:
        ...
    def ShadedBackgroundOptionGraduatedDark(self) -> None:
        ...
    def ShadedBackgroundOptionDark(self) -> None:
        ...
    def ShadedBackgroundOptionLightImage(self) -> None:
        ...
    def ShadedBackgroundOptionDarkImage(self) -> None:
        ...
    def WireframeBackgroundOptionWhite(self) -> None:
        ...
    def WireframeBackgroundOptionLight(self) -> None:
        ...
    def WireframeBackgroundOptionGraduatedLight(self) -> None:
        ...
    def WireframeBackgroundOptionGraduatedDark(self) -> None:
        ...
    def WireframeBackgroundOptionDark(self) -> None:
        ...
    BackgroundCategory: Display.Background.CategoryType
    BackgroundShadedViewsBackgroundImage: int
    BackgroundShadedViewsType: int
    BackgroundType: Display.Background.Type
    BackgroundWireframeViewsType: int
    BackgroundWireframeViewsUsedShadedViewsSetting: bool
    DomeImage: Display.Image
    DomeImageFilename: str
    DomeOrigin: Point
    DomeSize: float
    DomeType: Display.Background.BackgroundDomeType
    Image: Display.Image
    ImageFilename: str
    ImageHorizon: float
    ImageRotation: float
    ImageUpVector: Direction
    UseStageSizeAndOrientation: bool


    class Type(enum.Enum):
        Plain = 0
        Graduated = 1
        Image = 2
        HemiDome = 3
    

    class SystemBackgroundType(enum.Enum):
        White = 0
        Light = 1
        GraduatedLight = 2
        GraduatedDark = 3
        Dark = 4
        LightImage = 5
        DarkImage = 6
    

    class ShadedType(enum.Enum):
        SystemBackground = 0
        Plain = 1
        Graduated = 2
        Image = 3
    

    class CategoryType(enum.Enum):
        Flat = 0
        Dome = 1
    

    class BackgroundImageType(enum.Enum):
        LightBackground1 = 0
        LightBackground2 = 1
        DarkBackground1 = 2
        DarkBackground2 = 3
        ClassicBackground1 = 4
        ClassicBackground2 = 5
        SystemBackground = 6
        CustomImage = 7
    

    class BackgroundDomeType(enum.Enum):
        Finite = 0
        Infinite = 1
    

class AnimationCameraCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Display.AnimationCamera]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateAnimationCameraBuilder(self, camera: Display.AnimationCamera) -> Display.AnimationCameraBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Display.AnimationCamera:
        ...
    def Tag(self) -> Tag: ...



class AnimationCameraBuilder(Display.CameraBuilder):
    def __init__(self) -> None: ...
    CameraConstrainedPoint: Point
    CameraConstrainedUpperVector: Direction
    CameraPositioningConstrained: bool
    CameraTransformSource: SelectTaggedObject
    TargetConstrainedPoint: Point
    TargetPositioningConstrained: bool
    TargetTransformSource: SelectTaggedObject


class AnimationCamera(Display.Camera):
    def __init__(self) -> None: ...


