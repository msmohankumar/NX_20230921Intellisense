from ....NXOpen import *
from ...CAE import *
from ..Xyplot import *

import typing
import enum

class XYPlotManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def PlotRecords(self, plotParameters: CAE.Xyplot.PlotParameters) -> CAE.Xyplot.Plot:
        ...
    def OverlayRecords(self, overlayParameters: CAE.Xyplot.OverlayParameters) -> CAE.Xyplot.Plot:
        ...
    def GetCurrentPlot(self, deviceIndex: int, viewIndex: int) -> CAE.Xyplot.Plot:
        ...
    def ShowNextPlot(self, deviceIndex: int, viewIndex: int) -> None:
        ...
    def ShowPreviousPlot(self, deviceIndex: int, viewIndex: int) -> None:
        ...
    def NewPlotParameters(self) -> CAE.Xyplot.PlotParameters:
        ...
    def NewOverlayParameters(self) -> CAE.Xyplot.OverlayParameters:
        ...
    def GetAvailableWindowDevices(self) -> int:
        ...
    def GetWindowDevicesViews(self, windowDevice: int) -> int:
        ...
    def GetPlots(self, windowDevice: int, view: int) -> typing.List[CAE.Xyplot.Plot]:
        ...
    def ReturnToModelView(self, view: int) -> None:
        ...
    def WriteImageToClipBoard(self, deviceIndex: int, viewIndex: int, isUseWhiteBackGround: bool) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.Xyplot.Plot:
        ...
    def Tag(self) -> Tag: ...

    WindowManager: CAE.Xyplot.WindowManager
    Preference: CAE.Xyplot.Preference
    TemplateManager: CAE.Xyplot.BaseTemplateManager


class WindowManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Xyplot.XYPlotManager) -> None: ...
    def NewWindow(self) -> int:
        ...
    def CloseWindow(self, deviceIndex: int) -> None:
        ...
    def GetWindows(self) -> int:
        ...
    def Tag(self) -> Tag: ...



class WallDisplayStyles3D(CAE.Xyplot.WallDisplayStyles):
    def __init__(self) -> None: ...
    ViewOrientation: Matrix3x3


class WallDisplayStyles2DBarChart(CAE.Xyplot.WallDisplayStyles):
    def __init__(self) -> None: ...
    def GetArgumentAxisStyleSetting(self) -> CAE.Xyplot.ArgumentAxisStyleSetting:
        ...


class WallDisplayStyles2D(CAE.Xyplot.WallDisplayStyles):
    def __init__(self) -> None: ...
    def GetAngleAxisStyleSetting(self) -> CAE.Xyplot.AngleAxisStyleSetting:
        ...


class WallDisplayStyles(TaggedObject):
    def __init__(self) -> None: ...
    def GetTextStyleSetting(self, textType: CAE.Xyplot.TextType) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetAxisStyleSetting(self, axisDirection: CAE.Xyplot.AxisDirection) -> CAE.Xyplot.AxisStyleSetting:
        ...
    def GetLegendTableGroupStyle(self) -> CAE.Xyplot.LegendTableGroupStyle:
        ...
    GridLayoutStyleSetting: CAE.Xyplot.BaseGridLayoutStyleSetting
    ProbingStyle: CAE.Xyplot.ProbingStyle


class VectorStyle2DSetting(CAE.Xyplot.BaseLineStyleSetting):
    def __init__(self) -> None: ...
    def GetVectorColors(self) -> typing.List[NXColor]:
        ...
    def SetVectorColors(self, vectorColors: typing.List[NXColor]) -> None:
        ...
    def GetNthVectorColor(self, index: int) -> NXColor:
        ...
    def SetNthVectorColors(self, index: int, vectorColors: NXColor) -> None:
        ...
    DrawText: bool
    IsAutoTextCount: bool
    MaximumTextCount: int
    OverlapTextAndVector: bool


class UnknownResultScaleStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    Color: CAE.Xyplot.UnknownResultColor
    Visibility: bool


class UnknownResultColor(enum.Enum):
    White = 0
    Grey = 1


class UnitSystem(enum.Enum):
    Function = 0
    Model = 1
    Si = 2
    Mn = 3
    Mm = 4
    In = 5
    Custom = 6


class TextType(enum.Enum):
    None = 0
    Title = 1
    Legend = 2
    GraphName = 3
    PageNumber = 4
    Marker = 5
    Note = 6
    ProbingText = 7
    XLabel = 8
    YLabel = 9
    ZLabel = 10
    XNumber = 11
    YNumber = 12
    ZNumber = 13
    ColorAxisLabel = 14
    ColorAxisNumber = 15
    UnknownResultText = 16
    AngleAxisNumber = 17
    AnnotationText = 18
    ArgumentAxisNumber = 19
    BarChartValueText = 20
    LegendTableText = 21


class TextStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    Alignment: CAE.Xyplot.TextAlignment
    Color: NXColor
    Font: str
    FontStyle: Preferences.VisualizationFonts.StyleType
    FontType: CAE.Xyplot.Fonttype
    GlobalSizeScale: float
    IsGlobalSizeAutoScaled: bool
    LeaderStyle: CAE.Xyplot.LeaderStyle
    NumberFormat: CAE.NumberFormat
    Orientation: CAE.Xyplot.TextOrientation
    Size: int
    TextBoxStyle: CAE.Xyplot.TextBoxStyleSetting
    UseGlobalFontSetting: bool
    Weight: Display.TransientText.TextSize
    Visibility: bool


class TextOrientation(enum.Enum):
    Horizontal = 0
    Upward = 1
    Downward = 2


class TextBoxStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetLineStyle(self) -> CAE.Xyplot.CurveDisplaySettings:
        ...
    def GetMargin(self, marginOption: CAE.Xyplot.TextBoxMarginOption) -> float:
        ...
    def SetMargin(self, marginOption: CAE.Xyplot.TextBoxMarginOption, marginValue: float) -> None:
        ...
    Color: NXColor
    FillingColor: NXColor
    IsFilled: bool
    Visibility: bool


class TextBoxMarginOption(enum.Enum):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3


class TextAlignment(enum.Enum):
    Left = 0
    Center = 1
    Right = 2


class SurfaceStyleSetting(CAE.Xyplot.BaseSymbolStyleSetting):
    def __init__(self) -> None: ...
    ColorOption: CAE.Xyplot.SurfaceColorOption
    FillingColor: NXColor
    OutlineColor: NXColor
    ShowOutline: bool


class SurfaceColorOption(enum.Enum):
    None = 0
    Hidden = 1
    Shaded = 2


class StackedPlot(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecord(self, nthRecordIdx: int, record: CAE.FTK.BaseRecord) -> None:
        ...


class ScatterStyleSetting(CAE.Xyplot.BaseSymbolStyleSetting):
    def __init__(self) -> None: ...
    Color: NXColor


class ProbingStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    HelpLineStyle: CAE.Xyplot.CurveDisplaySettings
    StepLineStyle: CAE.Xyplot.CurveDisplaySettings
    TextStyle: CAE.Xyplot.TextStyleSetting


class Preference(TaggedObject):
    def __init__(self) -> None: ...
    def Save(self) -> None:
        ...
    AfuRecordZValue: CAE.FTK.DataManager.AfuRecordZValue
    MaximumLegendsInGraph: int
    MaximumSubGraphsInStack: int
    NewWindowSetting: CAE.Xyplot.Preference.NewWindowChoice
    TargetWindowSetting: CAE.Xyplot.Preference.TargetGraphicWindowOption
    UpdateOverlayingAxisLimitsAutomatically: bool


    class TargetGraphicWindowOption(enum.Enum):
        Main = 0
        Separate = 1
        Both = 2
    

    class NewWindowChoice(enum.Enum):
        Prompt = 0
        Always = 1
    

class PointMarker(enum.Enum):
    None = 0
    Plus = 1
    Dot = 2
    Asterisk = 3
    Circle = 4
    Poundsign = 5
    Cross = 6
    Square = 7
    Triangle = 8
    Diamond = 9
    CenterLine = 10


class PlotType(enum.Enum):
    Plot2D = 0
    Plot2DInStack = 1
    Plot3D = 2
    PlotColorBar = 3
    PlotColorMap = 4
    PlotBarChart = 5


class PlotParameters(CAE.Xyplot.BasePlotParameters):
    def __init__(self, ptr: int) -> None: ...
    ComplexOption: int
    IsToCreateStandalonePlot: bool
    PlotTemplate: CAE.Xyplot.PlotGraphTemplate
    PlotType: CAE.Xyplot.PlotType


class PlotGraphTemplate(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def ResetToDefault(self) -> None:
        ...
    def ImportTemplate(self, strXmlFile: str) -> None:
        ...
    def ExportTemplate(self, strXmlFile: str) -> None:
        ...
    AbscissaCustomMarkerLabel: str
    DiagramDisplayStyles: CAE.Xyplot.DiagramDisplayStyles
    GeneralDisplayStyles: CAE.Xyplot.GeneralDisplayStyles
    OrdinateCustomMarkerLabel: str
    WallDisplayStyles: CAE.Xyplot.WallDisplayStyles
    ZCustomMarkerLabel: str


class Plot3D(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecords(self, records: typing.List[CAE.FTK.BaseRecord]) -> None:
        ...


class Plot2D(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecord(self, nthRecordIdx: int, record: CAE.FTK.BaseRecord) -> None:
        ...


class Plot(CAE.Xyplot.BaseModel):
    def __init__(self) -> None: ...
    def GetRecordCount(self) -> int:
        ...
    def GetApplicationDataOfRecord(self, recordIndex: int) -> CAE.FTK.IApplicationData:
        ...
    def SaveRecords(self, recordIndexes: int, recordNames: str, outputFileName: str, reportError: bool) -> None:
        ...
    def GetDeviceAndViewIndex(self, viewIndex: int) -> int:
        ...
    def GetGraphs(self, graphs: typing.List[CAE.Xyplot.Graph]) -> None:
        ...
    def FitAxisLimit(self) -> None:
        ...
    def SaveRecordsToCsv(self, recordIndex: int, recordNames: str, csvFileName: str, isWriteHeader: bool) -> None:
        ...
    def CreateNote(self, lines: str, textPosition: Point2d) -> CAE.Xyplot.NoteModel:
        ...
    def GetNotes(self) -> typing.List[CAE.Xyplot.NoteModel]:
        ...
    def GetTitles(self) -> typing.List[CAE.Xyplot.BasicModel]:
        ...
    def GetViewBoundingBox(self, leftBottom: Point3d, rightTop: Point3d) -> None:
        ...
    def WriteToTemplateFile(self, inputTemplateFile: str) -> str:
        ...
    def GetRecordDisplayVisibility(self, recordIndex: int) -> bool:
        ...
    def SetRecordDisplayVisibility(self, recordIndex: int, visibility: bool) -> None:
        ...
    def GetModels(self, type: CAE.Xyplot.ModelType) -> typing.List[CAE.Xyplot.BasicModel]:
        ...
    def FitView(self) -> None:
        ...
    def DeleteRecord(self, recordIndex: int) -> None:
        ...
    def CommitRecordsChange(self) -> None:
        ...
    def GetLegendTables(self) -> typing.List[CAE.Xyplot.LegendTable]:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.INXObject.FindObject")"""
        ...
    PlotTemplate: CAE.Xyplot.PlotGraphTemplate
    SubGraphCountInStack: int


class PlateStyle3DSetting(CAE.Xyplot.BasePlateStyleSetting):
    def __init__(self) -> None: ...
    ColorOption: CAE.Xyplot.PlateColorOption
    Direction: CAE.Xyplot.Direction


class PlateStyle2DSetting(CAE.Xyplot.BasePlateStyleSetting):
    def __init__(self) -> None: ...


class PlateColorOption(enum.Enum):
    Fill = 0
    Hidden = 1
    Shaded = 2


class PhaseRangeOption(enum.Enum):
    NegativeTwoPiToZero = 0
    ZeroToTwoPi = 1
    NegativePiToPi = 2
    NegativeOneHalfPiToHalfPi = 3
    NegativeHalfPiToOneHalfPi = 4


class OverlayParameters(CAE.Xyplot.BasePlotParameters):
    def __init__(self, ptr: int) -> None: ...
    SubGraphInStack: int


class NoteStyleSetting(CAE.Xyplot.TextStyleSetting):
    def __init__(self) -> None: ...
    def GetNoteTexts(self) -> str:
        ...
    def SetNoteTexts(self, noteTexts: str) -> None:
        ...


class NoteModel(CAE.Xyplot.BasicModel):
    def __init__(self) -> None: ...
    def GetTexts(self) -> str:
        ...
    def SetTexts(self, content: str) -> None:
        ...
    def GetTextPosition(self) -> Point2d:
        ...
    def SetTextPosition(self, position: Point2d) -> None:
        ...
    def Delete(self) -> None:
        ...


class ModelType(enum.Enum):
    Plot = 1
    Graph = 2
    RecordDisplay = 3
    Marker = 4
    Note = 5
    Title = 6
    GraphName = 7
    FunctionName = 8
    XAxis = 9
    XAxisLabel = 10
    XAxisNumber = 11
    YAxis = 12
    YAxisLabel = 13
    YAxisNumber = 14
    ZAxis = 15
    ZAxisLabel = 16
    ZAxisNumber = 17
    ColorAxis = 18
    ColorAxisLabel = 19
    ColorAxisNumber = 20
    AngleAxis = 21
    AngleAxisNumber = 22
    UnknownResult = 23
    PageNumber = 24
    Legend = 25
    LegendTable = 26


class MarkerStyleSetting(CAE.Xyplot.TextStyleSetting):
    def __init__(self) -> None: ...
    def GetNoteTexts(self) -> str:
        ...
    def SetNoteTexts(self, noteTexts: str) -> None:
        ...
    AbsPercentage: float
    AttachmentType: CAE.Xyplot.AnchorType
    NoteTextVisibility: bool
    NumberTextVisibility: bool
    SnapToData: bool


class MarkerModel(CAE.Xyplot.BasicModel):
    def __init__(self) -> None: ...
    def Delete(self) -> None:
        ...
    PointIndex: int
    RecordIndex: int


class LineStyle3DSetting(CAE.Xyplot.BaseLineStyleSetting):
    def __init__(self) -> None: ...
    Direction: CAE.Xyplot.Direction


class LineStyle2DSetting(CAE.Xyplot.BaseLineStyleSetting):
    def __init__(self) -> None: ...


class LimitsType(enum.Enum):
    FreeLimits = 0
    OptimizedLimits = 1
    FixedLimits = 2


class LegendTableTextStyle(CAE.Xyplot.TextStyleSetting):
    def __init__(self) -> None: ...
    def GetMargin(self, marginOption: CAE.Xyplot.TextBoxMarginOption) -> float:
        ...
    def SetMargin(self, marginOption: CAE.Xyplot.TextBoxMarginOption, marginValue: float) -> None:
        ...


class LegendTableStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetPositionType(self) -> CAE.Xyplot.LegendTablePositionType:
        ...
    def GetTextStyle(self) -> CAE.Xyplot.LegendTableTextStyle:
        ...
    def GetGridLineStyle(self) -> CAE.Xyplot.CurveDisplaySettings:
        ...
    def GetBorderLineStyle(self) -> CAE.Xyplot.CurveDisplaySettings:
        ...
    def GetColumnTitles(self, columnTitles: str) -> None:
        ...
    def SetColumnTitles(self, columnTitles: str) -> None:
        ...
    BackgroundColor: NXColor
    GridBackgroundColor: NXColor
    IsBorderLineVisible: bool
    IsGridBackgroundFilled: bool
    IsGridLineVisible: bool
    IsHeaderVisible: bool
    MaximumLegendItemCount: int


class LegendTablePositionType(enum.Enum):
    Floating = 0
    Docked = 1


class LegendTableGroupStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetLegendTableStyle(self, legendTablePositionType: CAE.Xyplot.LegendTablePositionType) -> CAE.Xyplot.LegendTableStyle:
        ...
    ActiveLegendTablePosition: CAE.Xyplot.LegendTablePositionType
    Visibility: bool


class LegendTable(CAE.Xyplot.BaseModel):
    def __init__(self) -> None: ...
    def GetFreeTextOfLegendItem(self, dataIndex: int) -> str:
        ...
    def SetFreeTextOfLegendItem(self, dataIndex: int, freeText: str) -> None:
        ...
    def ResetFreeTextOfLegendItem(self, dataIndex: int) -> None:
        ...
    LegendTableStyle: CAE.Xyplot.LegendTableStyle


class LeaderStyle(TaggedObject):
    def __init__(self) -> None: ...
    AnchorColor: NXColor
    LineStyle: CAE.Xyplot.CurveDisplaySettings
    PointMarker: CAE.Xyplot.PointMarker


class IVisibleDisplayStyle():
    Visibility: bool


class IDisplayStyle():
    def CommitChange(self) -> None:
        ...
    Owner: CAE.Xyplot.IDisplayStyle


class IDisplayableModel():
    def UpdateDisplay(self) -> None:
        ...


class ICurveDisplaySettings():
    Color: NXColor
    Font: DisplayableObject.ObjectFont
    Width: DisplayableObject.ObjectWidth


class I3DDataPlot():
    def EditRecords(self, records: typing.List[CAE.FTK.BaseRecord]) -> None:
        ...


class I3DDataGraph():
    def GetSourcePointCount(self, recordIndex: int, sectionIndex: int) -> int:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, pointIndex: int) -> CAE.Xyplot.MarkerModel:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> CAE.Xyplot.MarkerModel:
        ...


class I2DDataPlot():
    def EditRecord(self, nthRecordIdx: int, record: CAE.FTK.BaseRecord) -> None:
        ...


class GridStyle2DColorContour(CAE.Xyplot.BaseGridLayoutStyleSetting):
    def __init__(self) -> None: ...
    IsAutoOrderGrid: bool
    OrderGridCount: int
    OrderInterval: float
    ShowOrderGrid: bool


class GridStyle(enum.Enum):
    NoGrid = 0
    GridOnly = 1
    TicksOnly = 2
    GridAndTicks = 3
    DenseGrid = 4


class GridLayoutStyle3DSetting(CAE.Xyplot.BaseGridLayoutStyleSetting):
    def __init__(self) -> None: ...
    ZxGridStyle: CAE.Xyplot.GridStyle
    ZyGridStyle: CAE.Xyplot.GridStyle


class GridLayoutStyle2DSetting(CAE.Xyplot.BaseGridLayoutStyleSetting):
    def __init__(self) -> None: ...


class GraphStyle(enum.Enum):
    Line = 0
    Bar = 1
    Plate = 2
    Surface = 3
    Scatter = 4
    ColorBar = 5
    ColorMap = 6
    BarChart = 7
    Vector = 8


class GraphOptionsStyle2D(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    FrequencyBandSummationBandType: CAE.Xyplot.FrequencyBandSummationBandType
    ShowFrequencyBandSummation: bool
    ShowTotalResponseLineForPolar: bool
    ShowTotalResponseLineForVector: bool
    TotalResponseLineSetting: CAE.Xyplot.CurveDisplaySettings


class GraphNameStyle(CAE.Xyplot.TextStyleSetting):
    def __init__(self) -> None: ...
    PositionOption: CAE.Xyplot.GraphNamePositionOption


class GraphNamePositionOption(enum.Enum):
    TopLeft = 0
    TopCenter = 1
    TopRight = 2
    BottomLeft = 3
    BottomCenter = 4
    BottomRight = 5


class Graph3D(CAE.Xyplot.Graph):
    def __init__(self) -> None: ...
    def GetSourcePointCount(self, recordIndex: int, sectionIndex: int) -> int:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, pointIndex: int) -> CAE.Xyplot.MarkerModel:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> CAE.Xyplot.MarkerModel:
        ...


class Graph(CAE.Xyplot.BaseModel):
    def __init__(self) -> None: ...
    def GetPointCount(self, recordIndex: int) -> int:
        ...
    def CreateMarker(self, recordIndex: int, pointIndex: int) -> CAE.Xyplot.MarkerModel:
        ...
    def CreateMarker(self, recordIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> CAE.Xyplot.MarkerModel:
        ...
    def CreateAssociativeMarker(self, recordIndex: int, attachType: CAE.Xyplot.AnchorType, absPercentage: float) -> CAE.Xyplot.MarkerModel:
        ...
    def GetMarkers(self, markers: typing.List[CAE.Xyplot.MarkerModel]) -> None:
        ...
    def GetAnchorPointOfRecord(self, recordIndex: int, anchorType: CAE.Xyplot.AnchorType, anchorPoint: Point3d) -> bool:
        ...
    def GetRecordName(self, recordIndex: int) -> str:
        ...
    def GetGridBoundingBox(self, leftBottom: Point3d, rightTop: Point3d) -> None:
        ...
    def GetAbscissaAxis(self) -> CAE.Xyplot.BasicModel:
        ...
    def GetOrdinateAxes(self) -> typing.List[CAE.Xyplot.BasicModel]:
        ...
    def GetZAxis(self) -> CAE.Xyplot.BasicModel:
        ...
    def SetDisplayStyleOfRecord(self, recordIndex: int, displayStyleIndex: int) -> None:
        ...
    def ZoomAlongX(self, startScale: float, endScale: float) -> None:
        ...
    def ZoomAlongY(self, startScale: float, endScale: float) -> None:
        ...
    def ZoomAlongZ(self, startScale: float, endScale: float) -> None:
        ...
    def ZoomAlongXY(self, xStartScale: float, xEndScale: float, yStartScale: float, yEndScale: float) -> None:
        ...
    def Unzoom(self) -> None:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.INXObject.FindObject")"""
        ...
    RecordCount: int


class GeneralDisplayStyles3D(CAE.Xyplot.GeneralDisplayStyles):
    def __init__(self) -> None: ...
    ComplexOption: CAE.Xyplot.ComplexOption3D


class GeneralDisplayStyles2DColorContour(CAE.Xyplot.GeneralDisplayStyles):
    def __init__(self) -> None: ...
    ComplexOption: CAE.Xyplot.ComplexOption2DColorContour


class GeneralDisplayStyles2DBarChart(CAE.Xyplot.GeneralDisplayStyles):
    def __init__(self) -> None: ...
    ComplexOption: CAE.Xyplot.ComplexOption2DBarChart


class GeneralDisplayStyles2D(CAE.Xyplot.GeneralDisplayStyles):
    def __init__(self) -> None: ...
    def SwitchXYAxis(self) -> None:
        ...
    ComplexOption: CAE.Xyplot.ComplexOption2D
    ShowOrderedAbscissa: bool


class GeneralDisplayStyles(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    PhaseAngle: float
    PhaseRangeOption: CAE.Xyplot.PhaseRangeOption


class FrequencyBandSummationBandType(enum.Enum):
    Octave = 0
    OneThirdOctave = 1
    OneTwelfthOctave = 2


class Fonttype(enum.Enum):
    Nx = 0
    Standard = 1


class Direction(enum.Enum):
    X = 0
    Z = 1
    Xz = 2


class DiagramDisplayStyles2DBarChart(CAE.Xyplot.DiagramDisplayStyles):
    def __init__(self) -> None: ...
    def GetBarChartStyleSetting(self, styleIndex: int) -> CAE.Xyplot.BarChartStyleSetting:
        ...
    SpaceBetweenFunctions: int
    SpaceBetweenItems: int


class DiagramDisplayStyles2D(CAE.Xyplot.DiagramDisplayStyles):
    def __init__(self) -> None: ...
    def GetGraphOptionsStyle(self, styleIndex: int) -> CAE.Xyplot.GraphOptionsStyle2D:
        ...


class DiagramDisplayStyles(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetGraphStyle(self, styleIndex: int) -> CAE.Xyplot.GraphStyle:
        ...
    def SetGraphStyle(self, styleIndex: int, graphStyle: CAE.Xyplot.GraphStyle) -> None:
        ...
    def GetLineStyleSetting(self, styleIndex: int) -> CAE.Xyplot.BaseLineStyleSetting:
        ...
    def GetBarStyleSetting(self, styleIndex: int) -> CAE.Xyplot.BaseBarStyleSetting:
        ...
    def GetPlateStyleSetting(self, styleIndex: int) -> CAE.Xyplot.BasePlateStyleSetting:
        """[Obsolete("Deprecated in NX12.0.0.  There is no replacement for this function")"""
        ...
    def GetScatterStyleSetting(self, styleIndex: int) -> CAE.Xyplot.ScatterStyleSetting:
        ...
    def GetSurfaceStyleSetting(self, styleIndex: int) -> CAE.Xyplot.SurfaceStyleSetting:
        ...
    def GetVectorStyleSetting(self, styleIndex: int) -> CAE.Xyplot.VectorStyle2DSetting:
        ...
    StyleCount: int


class DecimalFormat(enum.Enum):
    Actual = 0
    X = 1
    Xx = 2
    Xxx = 3
    Xxxx = 4
    Xexx = 5
    Xxexx = 6
    Xxxexx = 7
    Xxxxexx = 8


class CustomTextStyleSetting(CAE.Xyplot.TextStyleSetting):
    def __init__(self) -> None: ...
    def GetUserDefinedText(self) -> str:
        ...
    def SetUserDefinedText(self, text: str) -> None:
        ...
    UseAutomatic: bool


class CurveDisplaySettings(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    Color: NXColor
    Font: DisplayableObject.ObjectFont
    Width: DisplayableObject.ObjectWidth


class CoordinateType(enum.Enum):
    Xy = 0
    Yx = 1
    Xyz = 2
    Yxz = 3
    Zyx = 4
    Yzx = 5
    Xzy = 6
    Zxy = 7


class ContouringRange(enum.Enum):
    BorderGrid = 0
    FullGrid = 1


class ComplexOption3D(enum.Enum):
    Magnitude = 0
    Phase = 1
    Real = 2
    Imaginary = 3
    Argand = 4
    Orbit = 5
    Nichols = 6
    AtPhaseAngle = 7
    SignedMagnitude = 8


class ComplexOption2DColorContour(enum.Enum):
    Magnitude = 0
    Phase = 1
    Real = 2
    Imaginary = 3
    AtPhaseAngle = 4
    SignedMagnitude = 5


class ComplexOption2DBarChart(enum.Enum):
    Magnitude = 0
    Phase = 1
    Real = 2
    Imaginary = 3
    AtPhaseAngle = 4
    SignedMagnitude = 5


class ComplexOption2D(enum.Enum):
    Magnitude = 0
    MagnitudePhase = 1
    Phase = 2
    Real = 3
    RealImaginary = 4
    RealImaginaryPhase = 5
    Polar = 6
    Argand = 7
    Polar3D = 8
    Argand3D = 9
    PhaseMagnitude = 10
    ImaginaryReal = 11
    PhaseRealImaginary = 12
    ImaginaryRealPhase = 13
    PhaseImaginaryReal = 14
    Nichols = 15
    AtPhaseAngle = 16
    SignedMagnitude = 17
    Directivity = 18
    Vector = 19


class ColorScaleStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    AutoLevel: bool
    Level: int


class ColorMapPlot(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecords(self, records: typing.List[CAE.FTK.BaseRecord]) -> None:
        ...


class ColorMapGraph(CAE.Xyplot.Graph):
    def __init__(self) -> None: ...
    def CreateOrderMarker(self, orderValue: float) -> CAE.Xyplot.MarkerModel:
        ...
    def GetSourcePointCount(self, recordIndex: int, sectionIndex: int) -> int:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, pointIndex: int) -> CAE.Xyplot.MarkerModel:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> CAE.Xyplot.MarkerModel:
        ...


class ColorBarPlot(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecord(self, nthRecordIdx: int, record: CAE.FTK.BaseRecord) -> None:
        ...


class ColorAxisStyleSetting(CAE.Xyplot.AxisStyleSetting):
    def __init__(self) -> None: ...
    ColorScaleStyleSetting: CAE.Xyplot.ColorScaleStyle
    UnknownResultScaleStyleSetting: CAE.Xyplot.UnknownResultScaleStyle


class BasicModel(CAE.Xyplot.BaseModel):
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.INXObject.FindObject")"""
        ...
    DisplayStyle: CAE.Xyplot.IDisplayStyle


class BaseTemplateManager(NXObject):
    def __init__(self) -> None: ...
    def LoadTemplate(self, templateFile: str) -> None:
        ...
    def UnloadTemplate(self, templateFile: str) -> None:
        ...
    def UnloadAllTemplates(self) -> None:
        ...
    def ResetTemplate(self, templateFile: str) -> None:
        ...
    def DeleteTemplate(self, templateFile: str) -> None:
        ...
    def SaveTemplate(self, templateFile: str) -> None:
        ...
    def SaveAsTemplate(self, sourceTemplateFile: str, destinationTemplateFile: str) -> None:
        ...
    def RenameTemplateFile(self, oldTemplateFile: str, newTemplateFileName: str) -> None:
        ...
    def SaveAllTemplates(self) -> None:
        ...
    def ResetSystemTemplate(self) -> None:
        ...
    def GetDefaultTemplate(self) -> str:
        ...
    def SetDefaultTemplate(self, templateFile: str) -> None:
        ...
    def ReloadAllTemplateFiles(self) -> None:
        ...
    ActiveTemplate: str


class BaseSymbolStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    PointMarker: CAE.Xyplot.PointMarker


class BasePlotParameters(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetRecords(self) -> typing.List[CAE.FTK.BaseRecord]:
        ...
    def SetRecords(self, records: typing.List[CAE.FTK.BaseRecord]) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    DeviceIndex: int
    ViewPortIndex: int


class BasePlateStyleSetting(CAE.Xyplot.BaseSymbolStyleSetting):
    def __init__(self) -> None: ...
    FillingColor: NXColor
    OutlineColor: NXColor
    ShowOutline: bool


class BaseModel(NXObject):
    def __init__(self) -> None: ...
    def UpdateDisplay(self) -> None:
        ...


class BaseLineStyleSetting(CAE.Xyplot.BaseSymbolStyleSetting):
    def __init__(self) -> None: ...
    Color: NXColor
    Font: DisplayableObject.ObjectFont
    Width: DisplayableObject.ObjectWidth


class BaseGridLayoutStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    BackgroundColor: NXColor
    ColorOfBackgroundPlane: NXColor
    ContouringLevel: int
    ContouringRange: CAE.Xyplot.ContouringRange
    DenseColor: NXColor
    DenseGridDisplayStyleSettings: CAE.Xyplot.CurveDisplaySettings
    DisplayContouring: bool
    GridColor: NXColor
    GridFont: DisplayableObject.ObjectFont
    GridWidth: DisplayableObject.ObjectWidth
    MajorGridDisplayStyleSettings: CAE.Xyplot.CurveDisplaySettings
    ShowBackground: bool
    ShowBackgroundPlane: bool
    TicksDisplayStyleSettings: CAE.Xyplot.CurveDisplaySettings
    XyGridStyle: CAE.Xyplot.GridStyle


class BaseDisplayStyleSetting(TaggedObject):
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def CommitChange(self) -> None:
        ...
    JournalIdentifier: str
    Owner: CAE.Xyplot.IDisplayStyle


class BaseBarStyleSetting(CAE.Xyplot.BaseSymbolStyleSetting):
    def __init__(self) -> None: ...
    FillingColor: NXColor
    OutlineColor: NXColor
    ShowOutline: bool
    Width: int


class BarStyle3DSetting(CAE.Xyplot.BaseBarStyleSetting):
    def __init__(self) -> None: ...
    ColorOption: CAE.Xyplot.BarColorOption
    Depth: int


class BarStyle2DSetting(CAE.Xyplot.BaseBarStyleSetting):
    def __init__(self) -> None: ...


class BarColorOption(enum.Enum):
    Fill = 0
    Hidden = 1
    Shaded = 2


class BarChartStyleSetting(CAE.Xyplot.BaseSymbolStyleSetting):
    def __init__(self) -> None: ...
    FillingColor: NXColor
    OutlineColor: NXColor
    PointMarkerIdx: CAE.Xyplot.PointMarker
    ShowOutline: bool
    ShowText: bool
    SpaceBetweenTextAndBar: int


class BarChartPlot(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecord(self, nthRecordIdx: int, record: CAE.FTK.BaseRecord) -> None:
        ...


class AxisYStyleSetting(CAE.Xyplot.AxisStyleSetting):
    def __init__(self) -> None: ...
    BarLowerLimit: bool


class AxisType(enum.Enum):
    Auto = 0
    Linear = 1
    Log = 2
    Db = 3
    Octave = 4
    OneThirdOctave = 5
    OneTwelfthOctave = 6


class AxisStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetLabelStyle(self) -> CAE.Xyplot.CustomTextStyleSetting:
        ...
    def GetNumberStyle(self) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetDBSettings(self) -> CAE.SignalProcessingDBSettings:
        ...
    def GetFixedLimits(self, lowerLimit: float, upperLimit: float) -> None:
        ...
    def SetFixedLimits(self, lowerLimit: float, upperLimit: float) -> None:
        ...
    def LogUnitChangedEvent(self) -> None:
        ...
    def GetDisplayUnit(self) -> CAE.FTK.BaseUnit:
        ...
    AxisType: CAE.Xyplot.AxisType
    DbDecades: int
    DbRef: float
    DbScale: CAE.Xyplot.AxisDBScale
    GraphOverhead: int
    LimitsType: CAE.Xyplot.LimitsType
    LogDecades: int
    UnitSystem: CAE.Xyplot.UnitSystem
    UnitSystemType: CAE.XyFunctionUnitSystem


class AxisModel(CAE.Xyplot.BasicModel):
    def __init__(self) -> None: ...
    def GetDisplayLimits(self, startDisplayLimit: float, endDisplayLimit: float) -> None:
        ...
    def CalculateZoomScale(self, newStartDisplayLimit: float, newEndDisplayLimit: float, startScale: float, endScale: float) -> None:
        ...


class AxisLabelStyle(CAE.Xyplot.CustomTextStyleSetting):
    def __init__(self) -> None: ...
    IncludeMeasureType: bool
    IncludeUnit: bool
    UseSingleLine: bool


class AxisItemStyle(CAE.Xyplot.TextStyleSetting):
    def __init__(self) -> None: ...
    MaximumCharacterCount: int


class AxisDirection(enum.Enum):
    X = 0
    Y = 1
    Z = 2


class AxisDBScale(enum.Enum):
    Ten = 0
    Twenty = 1


class ArgumentAxisStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetAbsCustomerRange(self) -> str:
        ...
    def SetAbsCustomerRange(self, absCustomerRange: str) -> None:
        ...
    def GetAxisItemStyleSetting(self) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetLabelStyle(self) -> CAE.Xyplot.CustomTextStyleSetting:
        ...
    RangeAuto: bool


class AngleUnit(enum.Enum):
    Degree = 0
    Radian = 1
    Rev = 2


class AngleAxisStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    AngleUnit: CAE.Xyplot.AngleUnit
    LineDisplaySettings: CAE.Xyplot.CurveDisplaySettings
    Visibility: bool


class AnchorType(enum.Enum):
    None = 0
    Start = 1
    End = 2
    MaximumValue = 3
    MinimumValue = 4
    AbsPercentage = 5


