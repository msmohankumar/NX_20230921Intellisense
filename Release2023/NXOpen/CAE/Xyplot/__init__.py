from ....NXOpen import *
from ...CAE import *
from ..Xyplot import *

import typing
import enum

class XYZFunctionDataAccessor(CAE.Xyplot.IFunctionDataAccessor):
    def __init__(self, ptr: int) -> None: ...
    def AskSectionCount(self) -> int:
        ...
    def AskSectionDisplayData(self, sectionIndex: int, indenpendent1Values: float, indenpendent2Value: float, dependentValues: float) -> None:
        ...


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
    def MakeCurrentPlot(self, plot: CAE.Xyplot.Plot) -> None:
        ...
    def AlignAxesOfPlots(self, part: BasePart) -> None:
        ...
    def CreateResultAccessor(self, plot: CAE.Xyplot.Plot) -> CAE.Xyplot.ResultAccessor:
        ...
    def CreateResultAccessorOnCanvas(self, plot: CAE.Xyplot.Plot, canvasIndex: int) -> CAE.Xyplot.ResultAccessor:
        ...
    def Tag(self) -> Tag: ...

    WindowManager: CAE.Xyplot.WindowManager
    DataExporter: CAE.Xyplot.DataExporter
    AutotestUtils: CAE.Xyplot.AutotestUtils
    Preference: CAE.Xyplot.Preference
    TemplateManager: CAE.Xyplot.BaseTemplateManager


class XYFunctionDataAccessor(CAE.Xyplot.IFunctionDataAccessor):
    def __init__(self, ptr: int) -> None: ...
    def AskDisplayData(self, indenpendentValue: float, dependentValue: float) -> None:
        ...


class WindowManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Xyplot.XYPlotManager) -> None: ...
    def NewWindow(self) -> int:
        ...
    def CloseWindow(self, deviceIndex: int) -> None:
        ...
    def GetWindows(self) -> int:
        ...
    def GetWindowTitle(self, deviceIndex: int) -> str:
        ...
    def SetWindowTitle(self, deviceIndex: int, windowTitle: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class WallDisplayStyles3D(CAE.Xyplot.WallDisplayStyles):
    def __init__(self) -> None: ...
    ViewOrientation: Matrix3x3


class WallDisplayStyles2D(CAE.Xyplot.WallDisplayStyles):
    def __init__(self) -> None: ...
    def GetAngleAxisStyleSetting(self) -> CAE.Xyplot.AngleAxisStyleSetting:
        ...
    def GetFormulaGridStyle(self) -> CAE.Xyplot.FormulaGridStyle:
        ...


class WallDisplayStyles(TaggedObject):
    def __init__(self) -> None: ...
    def GetTextStyleSetting(self, textType: CAE.Xyplot.TextType) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetLegendTableGroupStyle(self) -> CAE.Xyplot.LegendTableGroupStyle:
        ...
    def GetCalculationLegendTableStyle(self) -> CAE.Xyplot.LegendTableStyle:
        ...
    def GetAxisStyle(self, axisDirection: CAE.Xyplot.AxisDirection) -> CAE.Xyplot.IAxisStyle:
        ...
    GridLayoutStyleSetting: CAE.Xyplot.BaseGridLayoutStyleSetting
    PanStyle: CAE.Xyplot.PanStyle
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


class UnknownResultColor(enum.Enum):
    White = 0
    Grey = 1


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
    ResultLegendText = 22
    FormulaGridValueText = 23


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


class SurfaceColorOption(enum.Enum):
    None = 0
    Hidden = 1
    Shaded = 2


class StackedPlot(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def GetSubplotCount(self) -> int:
        ...
    def GetPostEnvironmentSettingsOfSubplot(self, plotIndex: int) -> TaggedObject:
        ...
    def EditRecord(self, nthRecordIdx: int, record: CAE.FTK.BaseRecord) -> None:
        ...


class SourceDataExportParameters(CAE.Xyplot.DataExportParameters):
    def __init__(self, ptr: int) -> None: ...
    def GetSectionDataIndices(self) -> int:
        ...
    def SetSectionDataIndices(self, sectionDataIndices: int) -> None:
        ...
    ComplexDataSaveSetting: CAE.Xyplot.SourceDataExportParameters.ComplextDataSaveOption


    class ComplextDataSaveOption(enum.Enum):
        RealImag = 0
        MagPhase = 1
    

class SoundPlayer(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def Play(self) -> None:
        ...
    def Stop(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    Cyclestate: bool


class ScatterStyleSetting(CAE.Xyplot.BaseSymbolStyleSetting):
    def __init__(self) -> None: ...
    Color: NXColor


class ResultLegendStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    OverflowResultColorOption: CAE.Xyplot.FlowResultColor
    OverflowResultShadedColor: NXColor
    UnderflowResultColorOption: CAE.Xyplot.FlowResultColor
    UnderflowResultShadedColor: NXColor
    UnknownResultColorOption: CAE.Xyplot.UnknownResultColor
    Visibility: bool


class ResultAccessor(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AskFunctionDataAccessorType(self, graphIndex: int, recordIndex: int) -> CAE.Xyplot.FunctionDataAccessor:
        ...
    def AskXYFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> CAE.Xyplot.XYFunctionDataAccessor:
        ...
    def AskArgand3DFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> CAE.Xyplot.Argand3DFunctionDataAccessor:
        ...
    def AskXYZFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> CAE.Xyplot.XYZFunctionDataAccessor:
        ...
    def AskBarChartFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> CAE.Xyplot.BarChartFunctionDataAccessor:
        ...
    def AskMatrixFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> CAE.Xyplot.MatrixFunctionDataAccessor:
        ...
    def AskCampbellFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> CAE.Xyplot.CampbellFunctionDataAccessor:
        ...
    def AskPostEnvironment(self) -> TaggedObject:
        ...
    def GetNthGraph(self, graphIdx: int) -> CAE.Xyplot.Graph:
        ...
    def FreeResource(self) -> None:
        ...
    CanvasIndex: int
    GraphCount: int
    OnCanvas: bool
    Plot: CAE.Xyplot.Plot
    RecordCount: int


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
    MaximumDisplayableColumnsInMatrix: int
    MaximumDisplayableRowsInMatrix: int
    MaximumSubGraphsInStack: int
    NewWindowSetting: CAE.Xyplot.Preference.NewWindowChoice
    TargetWindowSetting: CAE.Xyplot.Preference.TargetGraphicWindowOption


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
    PlotMatrix2D = 6
    PlotCampbell = 7


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
    def DeleteAllRecords(self) -> None:
        ...
    def CommitRecordsChange(self) -> None:
        ...
    def GetLegendTables(self) -> typing.List[CAE.Xyplot.LegendTable]:
        ...
    def GetPostEnvironmentSettings(self) -> TaggedObject:
        ...
    def GetCalculationLegendTables(self) -> typing.List[CAE.Xyplot.LegendTable]:
        ...
    PlotTemplate: CAE.Xyplot.PlotGraphTemplate
    SubGraphCountInStack: int


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


class PanToolSize(enum.Enum):
    Small = 0
    Normal = 1
    Large = 2


class PanStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetAnnotationStyle(self) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetLabelDisplayStyle(self) -> CAE.Xyplot.CustomTextStyleSetting:
        ...
    ToolPosition: Point3d
    ToolSize: CAE.Xyplot.PanToolSize


class PanDirection(enum.Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3


class OverlayParameters(CAE.Xyplot.BasePlotParameters):
    def __init__(self, ptr: int) -> None: ...
    SubGraphInStack: int


class OverallMarkerModel(CAE.Xyplot.BasicModel):
    def __init__(self) -> None: ...
    def GetResult(self) -> float:
        ...
    def Delete(self) -> None:
        ...
    def GetTexts(self, textValues: str) -> None:
        ...


class OverallLevelAccessor(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AskOverallLevelResult(self, resultValue: float) -> bool:
        ...
    def FreeResource(self) -> None:
        ...


class OrderMarkerModel(CAE.Xyplot.BasicModel):
    def __init__(self) -> None: ...
    def GetOrderValue(self) -> float:
        ...
    def Delete(self) -> None:
        ...
    def GetTexts(self, textValues: str) -> None:
        ...


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


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


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
    ResultLegend = 27
    FormulaGrid = 28
    FormulaGridValueText = 29
    CalculationLegendTable = 30


class MatrixPlot2DLayoutMode(enum.Enum):
    FillEachCellAsSquare = 0
    FillAllAvailableDisplayArea = 1


class MatrixPlot2D(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecord(self, nthRecordIdx: int, record: CAE.FTK.BaseRecord) -> None:
        ...


class MatrixGraph2D(CAE.Xyplot.Graph):
    def __init__(self) -> None: ...
    def GetSourcePointCount(self, recordIndex: int, sectionIndex: int) -> int:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, pointIndex: int) -> CAE.Xyplot.MarkerModel:
        ...
    def CreateMarker(self, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> CAE.Xyplot.MarkerModel:
        ...


class MatrixFunctionDataAccessor(CAE.Xyplot.IFunctionDataAccessor):
    def __init__(self, ptr: int) -> None: ...
    def AskDisplayData(self, dependentValues: float) -> None:
        ...
    def AskPointLabels(self, rowLabels: str, columnLabels: str) -> None:
        ...


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
    Visibility: bool


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


class LegendAccessor(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    FreeText: str


class LeaderStyle(TaggedObject):
    def __init__(self) -> None: ...
    AnchorColor: NXColor
    LineStyle: CAE.Xyplot.CurveDisplaySettings
    PointMarker: CAE.Xyplot.PointMarker


class IVisibleDisplayStyle():
    Visibility: bool


class ITextModel():
    def GetTexts(self, textValues: str) -> None:
        ...


class IFunctionDataAccessor(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AskAxisAccessor(self, axisDirection: CAE.Xyplot.AxisDirection) -> CAE.Xyplot.AxisAccessor:
        ...
    def AskColorAxisAccessor(self) -> CAE.Xyplot.AxisAccessor:
        ...
    def AskLegendAccessor(self) -> CAE.Xyplot.LegendAccessor:
        ...
    def FreeResource(self) -> None:
        ...
    def AskFunctionLegendAccessor(self) -> CAE.Xyplot.FunctionLegendAccessor:
        ...
    def AskOverallLevelAccessor(self) -> CAE.Xyplot.OverallLevelAccessor:
        ...
    FunctionType: str
    RecordName: str
    Type: CAE.Xyplot.FunctionDataAccessor


class IDisplayStyle():
    def CommitChange(self) -> None:
        ...
    Owner: CAE.Xyplot.IDisplayStyle


class IDisplayableModel():
    def UpdateDisplay(self) -> None:
        ...


class IDeletableModel():
    def Delete(self) -> None:
        ...


class ICurveDisplaySettings():
    Color: NXColor
    Font: DisplayableObject.ObjectFont
    Width: DisplayableObject.ObjectWidth


class IAxisStyle():
    def GetAnnotationStyle(self) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetLabelDisplayStyle(self) -> CAE.Xyplot.CustomTextStyleSetting:
        ...


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
    Surface = 3
    Scatter = 4
    ColorBar = 5
    ColorMap = 6
    BarChart = 7
    Vector = 8
    Matrix2D = 9


class GraphOptionsStyleColorMap(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    FreqBandSummationStyle: CAE.Xyplot.FrequencyBandSummationStyle


class GraphOptionsStyle2D(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    FrequencyBandSummationBandType: CAE.Xyplot.FrequencyBandSummationBandType
    FrequencyBandSummationBandTypeMode: CAE.Xyplot.FrequencyBandSummationBandTypeMode
    FrequencyBandSummationDisplayMode: CAE.Xyplot.FrequencyBandSummationDisplayMode
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
    def GetAbscissaAxes(self) -> typing.List[CAE.Xyplot.BasicModel]:
        ...
    def GetOrdinateAxes(self) -> typing.List[CAE.Xyplot.BasicModel]:
        ...
    def GetZAxis(self) -> CAE.Xyplot.BasicModel:
        ...
    def GetDisplayStyleOfRecord(self, recordIndex: int) -> int:
        ...
    def SetDisplayStyleOfRecord(self, recordIndex: int, displayStyleIndex: int) -> None:
        ...
    def RestoreStyleAssignments(self) -> None:
        ...
    def SaveStyleAssignmentsToTemplate(self) -> None:
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
    def CreateOverallMarker(self, recordIndex: int) -> CAE.Xyplot.OverallMarkerModel:
        ...
    def CreateOrderMarker(self, recordIndex: int) -> CAE.Xyplot.OrderMarkerModel:
        ...
    def CreateSoundPlayer(self, recordIndex: int) -> CAE.Xyplot.SoundPlayer:
        ...
    RecordCount: int


class GeneralDisplayStylesMatrix2D(CAE.Xyplot.GeneralDisplayStyles):
    def __init__(self) -> None: ...
    def SwitchXYAxis(self) -> None:
        ...
    ComplexOption: CAE.Xyplot.ComplexOptionMatrix2D
    LayoutMode: CAE.Xyplot.MatrixPlot2DLayoutMode


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


class GeneralDisplayStyles(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    PhaseAngle: float
    PhaseRangeOption: CAE.Xyplot.PhaseRangeOption


class FunctionLegendAccessor(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AskFunctionName(self, funcType: CAE.Xyplot.CalculationFunctionType) -> str:
        ...
    def AskFunctionResult(self, funcType: CAE.Xyplot.CalculationFunctionType, results: float) -> bool:
        ...
    def FreeResource(self) -> None:
        ...


class FunctionDataAccessor(enum.Enum):
    None = 0
    Xy = 1
    Xyz = 2
    Argand3D = 3
    BarChart = 4
    Matrix = 5
    Campbell = 6


class FrequencyBandSummationStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    BandType: CAE.Xyplot.FrequencyBandSummationBandType
    BandTypeMode: CAE.Xyplot.FrequencyBandSummationBandTypeMode
    DisplayMode: CAE.Xyplot.FrequencyBandSummationDisplayMode
    Visibility: bool


class FrequencyBandSummationDisplayMode(enum.Enum):
    StepLines = 0
    ConnectCentralFrequencies = 1


class FrequencyBandSummationBandTypeMode(enum.Enum):
    Infer = 0
    UserDefined = 1


class FrequencyBandSummationBandType(enum.Enum):
    Octave = 0
    OneThirdOctave = 1
    OneTwelfthOctave = 2


class FormulaGridType(enum.Enum):
    None = 0
    DiagonalLineInHaighDiagram = 1


class FormulaGridStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetExpressionStyle(self) -> CAE.Xyplot.FormulaExpressionStyle:
        ...
    def GetGridLineStyle(self) -> CAE.Xyplot.CurveDisplaySettings:
        ...
    def GetGridValueTextStyle(self) -> CAE.Xyplot.TextStyleSetting:
        ...
    Visibility: bool


class FormulaExpressionStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetVariableValues(self) -> float:
        ...
    def SetVariableValues(self, variableValues: float) -> None:
        ...
    FormulaGridType: CAE.Xyplot.FormulaGridType
    IsIncludeNegativeInfinity: bool
    IsIncludePositiveInfinity: bool


class Fonttype(enum.Enum):
    Nx = 0
    Standard = 1


class FlowResultColor(enum.Enum):
    None = 0
    Shaded = 1


class DisplayDataExportParameters(CAE.Xyplot.DataExportParameters):
    def __init__(self, ptr: int) -> None: ...
    def GetGraphIndices(self) -> int:
        ...
    def SetGraphIndices(self, graphIndices: int) -> None:
        ...


class Direction(enum.Enum):
    X = 0
    Z = 1
    Xz = 2


class DiagramDisplayStylesColorMap(CAE.Xyplot.DiagramDisplayStyles):
    def __init__(self) -> None: ...
    GraphOptionsStyle: CAE.Xyplot.GraphOptionsStyleColorMap


class DiagramDisplayStylesCampbell(CAE.Xyplot.DiagramDisplayStyles):
    def __init__(self) -> None: ...
    GraphType: CAE.Xyplot.CampbellGraphType
    LineWidth: DisplayableObject.ObjectWidth
    PointMarker: CAE.Xyplot.PointMarker
    PointSizeScale: float
    PointSizeType: CAE.Xyplot.CampbellPointSizeType
    ShowBackground: bool


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
    def GetScatterStyleSetting(self, styleIndex: int) -> CAE.Xyplot.ScatterStyleSetting:
        ...
    def GetSurfaceStyleSetting(self, styleIndex: int) -> CAE.Xyplot.SurfaceStyleSetting:
        ...
    def GetVectorStyleSetting(self, styleIndex: int) -> CAE.Xyplot.VectorStyle2DSetting:
        ...
    def SetGraphStyleName(self, styleIndex: int, graphStyleName: str) -> None:
        ...
    def GetGraphStyleName(self, styleIndex: int) -> str:
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


class DataExportParameters(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetPlots(self, plots: typing.List[CAE.Xyplot.Plot]) -> None:
        ...
    def SetPlots(self, plots: typing.List[CAE.Xyplot.Plot]) -> None:
        ...
    def GetRecordIndices(self) -> int:
        ...
    def SetRecordIndices(self, plotDataIndices: int) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    Plot: CAE.Xyplot.Plot


class DataExporter(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Xyplot.XYPlotManager) -> None: ...
    def ExportToFiles(self, exportDataParam: CAE.Xyplot.DataExportParameters, exportFilesParam: CAE.FTK.ExportFilesParameter) -> None:
        ...
    def ExportToTableField(self, exportParam: CAE.Xyplot.DataExportParameters, customFieldNames: str, tables: typing.List[Fields.FieldTable]) -> None:
        ...
    def NewSourceDataExportParameters(self) -> CAE.Xyplot.SourceDataExportParameters:
        ...
    def NewDisplayDataExportParameters(self) -> CAE.Xyplot.DisplayDataExportParameters:
        ...
    def NewExportFilesParameters(self) -> CAE.FTK.ExportFilesParameter:
        ...
    def Tag(self) -> Tag: ...



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


class ComplexOptionMatrix2D(enum.Enum):
    Magnitude = 0
    Phase = 1
    Real = 2
    Imaginary = 3
    AtPhaseAngle = 4
    SignedMagnitude = 5


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


class ColorSpectrum(enum.Enum):
    Structural = 0
    Thermal = 1
    Grayscale = 2
    Stoplight = 3


class ColorScaleStyle(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetColorLegendValuesOverridden(self, overridedValues: float) -> None:
        ...
    def SetColorLegendValuesOverridden(self, overridedValues: float) -> None:
        ...
    def GetColorLegendColorsOverridden(self, legendColors: int) -> None:
        ...
    def SetColorLegendColorsOverridden(self, legendColors: int) -> None:
        ...
    AreColorLegendColorsOverridden: bool
    AreColorLegendValuesOverridden: bool
    AutoLevel: bool
    ColorSpectrumType: CAE.Xyplot.ColorSpectrum
    InvertionSpectrum: bool
    Level: int
    MeasureName: str


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
    ResultLegendStyleSetting: CAE.Xyplot.ResultLegendStyle


class ColorAxis(CAE.Xyplot.AxisModel):
    def __init__(self) -> None: ...
    def GetColorLegendLevelCount(self) -> int:
        ...


class CampbellPointSizeType(enum.Enum):
    Const = 0
    Variable = 1


class CampbellPlot(CAE.Xyplot.Plot):
    def __init__(self) -> None: ...
    def EditRecords(self, records: typing.List[CAE.FTK.BaseRecord]) -> None:
        ...


class CampbellGraphType(enum.Enum):
    Point = 0
    Line = 1


class CampbellFunctionDataAccessor(CAE.Xyplot.IFunctionDataAccessor):
    def __init__(self, ptr: int) -> None: ...
    def AskDisplayData(self, independentValues: float, dependentValues: float, rpmValues: float) -> float:
        ...


class CalculationFunctionType(enum.Enum):
    MaxAmplitude = 0
    MinAmplitude = 1
    MaximumRange = 2
    Rss = 3
    Rms = 4
    LinearAveraging = 5
    IntegratedValue = 6
    SignalPower = 7


class BasicModel(CAE.Xyplot.BaseModel):
    def __init__(self) -> None: ...
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


class BaseModel(NXObject):
    def __init__(self) -> None: ...
    def UpdateDisplay(self) -> None:
        ...
    StyleSetting: CAE.Xyplot.BaseDisplayStyleSetting


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
    DenseGridDisplayStyleSettings: CAE.Xyplot.CurveDisplaySettings
    DisplayContouring: bool
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
    ConstantWidth: float
    ShowConstantWidth: bool


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


class BarChartFunctionDataAccessor(CAE.Xyplot.IFunctionDataAccessor):
    def __init__(self, ptr: int) -> None: ...
    def AskDisplayData(self, indenpendentValues: float, dependentValues: float) -> None:
        ...
    def AskPointLabels(self, pointLabels: str) -> None:
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
    def GetAnnotationStyle(self) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetLabelDisplayStyle(self) -> CAE.Xyplot.CustomTextStyleSetting:
        ...
    AxisType: CAE.Xyplot.AxisType
    GraphOverhead: int
    LimitsType: CAE.Xyplot.LimitsType
    LogDecades: int
    UnitSystemType: CAE.XyFunctionUnitSystem
    UseAbsoluteValue: bool


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


class AxisAccessor(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetLabel(self, axisLabels: str) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    AxisType: CAE.Xyplot.AxisType
    Unit: CAE.FTK.BaseUnit


class AutotestUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Xyplot.XYPlotManager) -> None: ...
    def CreateHaighDiagramPlot(self, windowDevice: int, viewPortId: int, records: typing.List[CAE.FTK.BaseRecord]) -> CAE.Xyplot.Plot:
        ...
    def Tag(self) -> Tag: ...



class ArgumentAxisStyleSetting(CAE.Xyplot.BaseDisplayStyleSetting):
    def __init__(self) -> None: ...
    def GetCustomerRange(self) -> int:
        ...
    def SetCustomerIndices(self, customerIndices: int) -> None:
        ...
    def GetNthItemLabel(self, nth: int) -> str:
        ...
    def GetIndicesOfLabel(self, itemLabel: str) -> int:
        ...
    def LogUnitChangedEvent(self) -> None:
        ...
    def GetDisplayUnit(self) -> CAE.FTK.BaseUnit:
        ...
    def GetAnnotationStyle(self) -> CAE.Xyplot.TextStyleSetting:
        ...
    def GetLabelDisplayStyle(self) -> CAE.Xyplot.CustomTextStyleSetting:
        ...
    RangeAuto: bool
    UnitSystemType: CAE.XyFunctionUnitSystem


class Argand3DFunctionDataAccessor(CAE.Xyplot.IFunctionDataAccessor):
    def __init__(self, ptr: int) -> None: ...
    def AskDisplayData(self, indenpendent1Values: float, indenpendent2Values: float) -> float:
        ...


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


