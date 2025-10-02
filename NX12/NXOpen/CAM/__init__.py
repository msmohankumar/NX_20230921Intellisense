from . import FBM
from ...NXOpen import *
from ..CAM import *

import typing
import enum

class ZLevelMillingBuilder(CAM.PlanarOperationBuilder):
    def __init__(self) -> None: ...
    CutLevel: CAM.CutLevel
    TrimBoundary: CAM.Boundary


class ZLevelMilling(CAM.PlanarOperation):
    def __init__(self) -> None: ...


class ZAxisSmoothing(TaggedObject):
    def __init__(self) -> None: ...
    Option: CAM.ZAxisSmoothing.Options
    Radius: CAM.InheritableToolDepBuilder
    RampAngle: CAM.InheritableDoubleBuilder


    class Options(enum.Enum):
        None = 0
        On = 1
    

class WorkInstructionOutputBuilder(Builder):
    def __init__(self) -> None: ...
    def Publish(self, objects: typing.List[CAM.CAMObject], firstSelObj: CAM.CAMObject, currentView: int) -> None:
        ...
    OpenFile: bool
    OutputFile: str
    OutputFormat: CAM.WorkInstructionOutputBuilder.OutputFormatType
    PageOrientation: CAM.WorkInstructionOutputBuilder.PageOrientationType
    PageSize: CAM.WorkInstructionOutputBuilder.PageSizeType
    ScaleFactor: float


    class PageSizeType(enum.Enum):
        A0 = 0
        A1 = 1
        A2 = 2
        A3 = 3
        A4 = 4
        B1 = 5
        B2 = 6
        B3 = 7
        B4 = 8
        B5 = 9
        Executive = 10
        Folio = 11
        Legal = 12
        Letter = 13
        Tabloid = 14
    

    class PageOrientationType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class OutputFormatType(enum.Enum):
        Html = 0
        Pdf = 1
        Csv = 2
        Xml = 3
    

class WorkInstructionBuilder(Builder):
    def __init__(self) -> None: ...
    def CaptureCurrentView(self) -> None:
        ...
    def GetRichText(self) -> str:
        ...
    def SetRichText(self, multiLineText: str) -> None:
        ...
    def GetTextColor(self) -> float:
        ...
    def SetTextColor(self, textColor: float) -> None:
        ...
    def AddSheet(self) -> int:
        ...
    def DeleteSheet(self, sheetNum: int) -> None:
        ...
    def MoveSheet(self, sheetNum: int, up: bool) -> None:
        ...
    def CommitMaster(self) -> None:
        ...
    def CommitItem(self) -> None:
        ...
    def UpdateItemsInCurrentSheet(self, itemNames: str) -> None:
        ...
    def ActivateCapturedView(self) -> None:
        ...
    def RestorePreviousView(self) -> None:
        ...
    def DeleteViewCamera(self) -> None:
        ...
    def SetToolDisplayMotion(self, eventType: int, eventIndex: int) -> None:
        ...
    def SpecifyDrawingSheet(self, partName: str, drawingName: str) -> None:
        ...
    CameraName: str
    Drawing: str
    DrawingSheet: NXObject
    FontFace: str
    FontSize: int
    ImageFile: str
    ItemName: str
    NoBackground: bool
    OperListProgramGroup: str
    SheetNumber: int
    SheetTitle: str
    TemplateName: str
    TimeEstimate: float
    ToolListProgramGroup: str
    ToolSetupSheet: str
    VideoFile: str
    ViewTool: bool


class WireTool(CAM.ToolBuilder):
    def __init__(self) -> None: ...
    def CreateWireGuide(self) -> CAM.WireGuide:
        ...
    AdjReg: CAM.InheritableIntBuilder
    CutcomReg: CAM.InheritableIntBuilder
    Diameter: CAM.InheritableDoubleBuilder
    WireGuideList: CAM.WireGuideList


class WireGuideList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.WireGuide]) -> None:
        ...
    def Append(self, object: CAM.WireGuide) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.WireGuide) -> int:
        ...
    def FindItem(self, index: int) -> CAM.WireGuide:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.WireGuide) -> None:
        ...
    def Erase(self, obj: CAM.WireGuide, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.WireGuide]:
        ...
    def SetContents(self, objects: typing.List[CAM.WireGuide]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.WireGuide, object2: CAM.WireGuide) -> None:
        ...
    def Insert(self, location: int, object: CAM.WireGuide) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class WireGuide(TaggedObject):
    def __init__(self) -> None: ...
    CornerRadius: float
    Diameter: float
    Length: float
    TaperAngle: float


class WedmUserDefinedBuilder(CAM.UserDefinedOprBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder


class WedmUserDefined(CAM.UserDefinedOpr):
    def __init__(self) -> None: ...


class WedmStepoverBuilder(CAM.StepoverBuilder):
    def __init__(self) -> None: ...
    StepoverTypeType: CAM.StepoverBuilder.StepoverTypes


class WedmStatusControlCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    StatusControl: CAM.WedmStatusControlCiBuilder.StatusTypes


    class StatusTypes(enum.Enum):
        None = 0
        ApproachOnly = 1
        DepartureOnly = 2
        ApproachAndDeparture = 3
    

class WedmPointDefinitionBuilder(Builder):
    def __init__(self) -> None: ...
    Axis: NXObject
    AxisOption: CAM.WedmPointDefinitionBuilder.WireAxisStates
    Point: Point
    PointOption: CAM.WedmPointDefinitionBuilder.PointStates


    class WireAxisStates(enum.Enum):
        Zm = 0
        Specify = 1
    

    class PointStates(enum.Enum):
        None = 0
        Specify = 1
    

class WedmOrientGeomBuilder(CAM.OrientGeomBuilder):
    def __init__(self) -> None: ...


class WedmOperationBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetInPathEventSetData(self, passNumber: int, inPathEventType: CAM.WedmOperationBuilder.InPathUdeSetTypes) -> CAM.InPathEventSetData:
        ...
    def ExecuteApiExit(self) -> None:
        ...
    ApiExitName: str
    BackburnDistanceBuilder: CAM.InheritableDoubleBuilder
    BackburnFlag: int
    BackburnPasses: CAM.WedmOperationBuilder.BackburnPassesTypes
    ConvexCorner: CAM.WedmOperationBuilder.ConvexCornerTypes
    CornerMaximumAngleBuilder: CAM.InheritableDoubleBuilder
    CornerMinimumAngleBuilder: CAM.InheritableDoubleBuilder
    CornerRadiusBuilder: CAM.InheritableDoubleBuilder
    CustomBoundaryDataList: CAM.WedmCustomBoundaryDataBuilderList
    CutParameters: CAM.WedmCutParameters
    CutPattern: CAM.CutPatternBuilder
    CutoffDistanceBuilder: CAM.InheritableDoubleBuilder
    CutoffFlag: int
    CutoffFlagBuilder: CAM.InheritableIntBuilder
    CutoffStockBuilder: CAM.InheritableDoubleBuilder
    FeedsBuilder: CAM.FeedsWedmBuilder
    FinishPassesBuilder: CAM.InheritableIntBuilder
    LayoutCiBuilder: CAM.LayoutCiBuilder
    LeadInCircleAngleBuilder: CAM.InheritableDoubleBuilder
    LeadInPointBuilder: CAM.WedmPointDefinitionBuilder
    LeadInRadiusBuilder: CAM.InheritableDoubleBuilder
    LeadOutCircleAngleBuilder: CAM.InheritableDoubleBuilder
    LeadOutPointBuilder: CAM.WedmPointDefinitionBuilder
    LeadOutRadiusBuilder: CAM.InheritableDoubleBuilder
    LoopRadius: CAM.InheritableDoubleBuilder
    MaximumLoopAngle: CAM.InheritableDoubleBuilder
    MinimumLoopAngle: CAM.InheritableDoubleBuilder
    NcmWedmBuilder: CAM.NcmWedmBuilder
    NocoreStockBuilder: CAM.InheritableDoubleBuilder
    NumTabs: int
    RegionMethod: int
    RetractPointBuilder: CAM.WedmPointDefinitionBuilder
    RoughPassesBuilder: CAM.InheritableIntBuilder
    SmoothLeadInDistanceBuilder: CAM.InheritableDoubleBuilder
    SmoothLeadInOption: CAM.WedmOperationBuilder.SmoothLeadInTypes
    SmoothLeadOutDistanceBuilder: CAM.InheritableDoubleBuilder
    SmoothLeadOutOption: CAM.WedmOperationBuilder.SmoothLeadOutTypes
    Smoothing: CAM.WedmOperationBuilder.CornerSmoothingType
    StopPointDistanceBuilder: CAM.InheritableDoubleBuilder
    StopPointFlag: CAM.WedmOperationBuilder.StopPointFlagTypes
    StopPointType: CAM.WedmOperationBuilder.StopPointTypes
    ThreadHolePointBuilder: CAM.WedmPointDefinitionBuilder
    WedmArcOutputTypeCiBuilder: CAM.WedmArcOutputTypeCiBuilder
    WedmStatusControlCiBuilder: CAM.WedmStatusControlCiBuilder
    WedmTaperAngleBuilder: CAM.InheritableDoubleBuilder


    class StopPointTypes(enum.Enum):
        Opstop = 0
        Stop = 1
    

    class StopPointFlagTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class SmoothLeadOutTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class SmoothLeadInTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class InPathUdeSetTypes(enum.Enum):
        Start = 1
        End = 2
    

    class CornerSmoothingType(enum.Enum):
        None = 0
        AllPasses = 1
    

    class ConvexCornerTypes(enum.Enum):
        RollAround = 0
        Loops = 1
        ExtendAndTrim = 2
    

    class BackburnPassesTypes(enum.Enum):
        Single = 0
        MultipleRegionFirst = 1
        MultipleCutoffFirst = 2
        SingleLastFinish = 3
    

class WedmOpenGeomBuilder(CAM.WedmBasedGeomBuilder):
    def __init__(self) -> None: ...
    LeadOutPoint: NXObject


class WedmNocoreGeomBuilder(CAM.WedmBasedGeomBuilder):
    def __init__(self) -> None: ...
    NocoreStock: float


class WedmMoveControlBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...


class WedmMethodBuilder(CAM.MethodBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsWedmBuilder


class WedmMachineControlBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    UdeSet: CAM.UdeSet


class WedmMachineControl(CAM.Operation):
    def __init__(self) -> None: ...


class WedmLeadInOutBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...


class WedmIntGeomBuilder(CAM.WedmBasedGeomBuilder):
    def __init__(self) -> None: ...
    BackburnDistance: float
    BackburnFlag: int


class WedmGeomBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def ExecuteApiExit(self) -> None:
        ...
    ApiExitName: str
    BackburnDistanceBuilder: CAM.InheritableDoubleBuilder
    BackburnFlag: int
    BackburnPasses: CAM.WedmGeomBuilder.BackburnPassesTypes
    Boundary: CAM.BoundaryWireEDM
    ConvexCorner: CAM.WedmGeomBuilder.ConvexCornerTypes
    CornerMaximumAngleBuilder: CAM.InheritableDoubleBuilder
    CornerMinimumAngleBuilder: CAM.InheritableDoubleBuilder
    CornerRadiusBuilder: CAM.InheritableDoubleBuilder
    CustomBoundaryDataList: CAM.WedmCustomBoundaryDataBuilderList
    CutParameters: CAM.WedmCutParameters
    CutoffDistanceBuilder: CAM.InheritableDoubleBuilder
    CutoffFlag: int
    CutoffFlagBuilder: CAM.InheritableIntBuilder
    CutoffStockBuilder: CAM.InheritableDoubleBuilder
    FinishPassesBuilder: CAM.InheritableIntBuilder
    LayoutCiBuilder: CAM.LayoutCiBuilder
    LeadInCircleAngleBuilder: CAM.InheritableDoubleBuilder
    LeadInPoint: CAM.WedmPointDefinitionBuilder
    LeadInRadiusBuilder: CAM.InheritableDoubleBuilder
    LeadOutCircleAngleBuilder: CAM.InheritableDoubleBuilder
    LeadOutPoint: CAM.WedmPointDefinitionBuilder
    LeadOutRadiusBuilder: CAM.InheritableDoubleBuilder
    LoopRadius: CAM.InheritableDoubleBuilder
    MaximumLoopAngle: CAM.InheritableDoubleBuilder
    MinimumLoopAngle: CAM.InheritableDoubleBuilder
    NcmWedmBuilder: CAM.NcmWedmBuilder
    NocoreStockBuilder: CAM.InheritableDoubleBuilder
    NumTabs: int
    RegionMethod: int
    RetractPoint: CAM.WedmPointDefinitionBuilder
    RoughPassesBuilder: CAM.InheritableIntBuilder
    SmoothLeadInOption: CAM.WedmGeomBuilder.SmoothLeadInTypes
    SmoothLeadOutDistanceBuilder: CAM.InheritableDoubleBuilder
    SmoothLeadOutOption: CAM.WedmGeomBuilder.SmoothLeadOutTypes
    Smoothing: CAM.WedmGeomBuilder.CornerSmoothingType
    StopPointDistanceBuilder: CAM.InheritableDoubleBuilder
    StopPointFlag: CAM.WedmGeomBuilder.StopPointFlagTypes
    StopPointType: CAM.WedmGeomBuilder.StopPointTypes
    ThreadHolePoint: CAM.WedmPointDefinitionBuilder
    WedmArcOutputTypeCiBuilder: CAM.WedmArcOutputTypeCiBuilder
    WedmStatusControlCiBuilder: CAM.WedmStatusControlCiBuilder
    WedmTaperAngleBuilder: CAM.InheritableDoubleBuilder


    class StopPointTypes(enum.Enum):
        Opstop = 0
        Stop = 1
    

    class StopPointFlagTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class SmoothLeadOutTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class SmoothLeadInTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class CornerSmoothingType(enum.Enum):
        None = 0
        AllPasses = 1
    

    class ConvexCornerTypes(enum.Enum):
        RollAround = 0
        Loops = 1
        ExtendAndTrim = 2
    

    class BackburnPassesTypes(enum.Enum):
        Single = 0
        MultipleRegionFirst = 1
        MultipleCutoffFirst = 2
        SingleLastFinish = 3
    

class WedmFeatureGeomBuilder(CAM.WedmBasedGeomBuilder):
    def __init__(self) -> None: ...


class WedmExtGeomBuilder(CAM.WedmBasedGeomBuilder):
    def __init__(self) -> None: ...


class WedmCuttingBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...


class WedmCutParameters(CAM.CutParameters):
    def __init__(self) -> None: ...
    CutDirection: CAM.WedmCutParameters.CutDirectionTypes
    Intol: float
    LowerGuideOffset: CAM.InheritableDoubleBuilder
    LowerPlaneBuilder: CAM.InheritableDoubleBuilder
    Outtol: float
    OverlapDistanceBuilder: CAM.InheritableDoubleBuilder
    UpperGuideOffset: CAM.InheritableDoubleBuilder
    UpperPlaneBuilder: CAM.InheritableDoubleBuilder
    WedmStepoverBuilder: CAM.StepoverBuilder
    WireDiameterBuilder: CAM.InheritableDoubleBuilder
    WirePosition: CAM.WedmCutParameters.WirePositionTypes


    class WirePositionTypes(enum.Enum):
        On = 0
        Tanto = 1
    

    class CutDirectionTypes(enum.Enum):
        Alternate = 0
        Clockwise = 1
        CounterClockwise = 2
    

class WedmCutOrderBuilder(Builder):
    def __init__(self) -> None: ...
    CutOrder: CAM.WedmCutOrderBuilder.Type


    class Type(enum.Enum):
        PassFirst = 0
        RegionFirst = 1
    

class WedmCustomBoundaryDataBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.WedmCustomBoundaryDataBuilder]) -> None:
        ...
    def Append(self, object: CAM.WedmCustomBoundaryDataBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.WedmCustomBoundaryDataBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.WedmCustomBoundaryDataBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.WedmCustomBoundaryDataBuilder) -> None:
        ...
    def Erase(self, obj: CAM.WedmCustomBoundaryDataBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.WedmCustomBoundaryDataBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.WedmCustomBoundaryDataBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.WedmCustomBoundaryDataBuilder, object2: CAM.WedmCustomBoundaryDataBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.WedmCustomBoundaryDataBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class WedmCustomBoundaryDataBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateTabPointDataBuilder(self) -> CAM.TabPointDataBuilder:
        ...
    def CreateInpathEventDataBuilder(self) -> CAM.InPathEventDataBuilder:
        ...
    InpathEventDataList: CAM.InPathEventDataBuilderList
    LeadInPoint: CAM.WedmPointDefinitionBuilder
    LeadOutPoint: CAM.WedmPointDefinitionBuilder
    RetractPoint: CAM.WedmPointDefinitionBuilder
    TabPointList: CAM.TabPointDataBuilderList
    ThreadHolePoint: CAM.WedmPointDefinitionBuilder


class WedmCornerControlBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...


class WedmBasedGeomBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...
    BackburnPasses: int
    CustomBoundaryDataList: CAM.WedmCustomBoundaryDataBuilderList
    CutDirection: int
    CutoffDistance: float
    CutoffFlag: int
    CutoffStock: float
    FinishPasses: int
    FromPoint: NXObject
    FromPointStatus: int
    FromPointToolAxis: NXObject
    GoHomePoint: NXObject
    GoHomePointStatus: int
    GoHomePointToolAxis: NXObject
    Intol: float
    LayoutCiBuilder: CAM.LayoutCiBuilder
    LeadInPoint: NXObject
    LeadInPointStatus: int
    LeadOutPointStatus: int
    LowerPlane: float
    NumTabs: int
    Outtol: float
    RegionMethod: int
    RetractPoint: NXObject
    RetractPointStatus: int
    RetractPointToolAxis: NXObject
    RoughPasses: int
    SmoothLeadinDistance: float
    SmoothLeadinFlag: int
    SmoothLeadoutDistance: float
    SmoothLeadoutFlag: int
    StepoverBuilder: CAM.StepoverBuilder
    StopPointDistance: float
    StopPointFlag: int
    StopPointType: int
    ThreadHolePoint: NXObject
    ThreadHolePointStatus: int
    ThreadHolePointToolAxis: NXObject
    UpperPlane: float
    WireDiameter: float


class WedmArcOutputTypeCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    OutputType: CAM.WedmArcOutputTypeCiBuilder.OutputTypes


    class OutputTypes(enum.Enum):
        LinearOnly = 0
        CirPerpToTaxis = 1
        Synchronized = 2
    

class VolumeBased25DMillingOperationBuilder(CAM.FaceMillingBuilder):
    def __init__(self) -> None: ...
    BlankGeometry: CAM.Geometry
    CutDepths: CAM.VolumeBased25DMillingOperationBuilder.CutDepthsType
    ExtendWalls: bool
    FollowNonVerticalWalls: bool
    TopOffset: CAM.InheritableToolDepBuilder
    UseCleanupPass: bool
    UseExactPositioning: bool
    WallBlankThickness: CAM.InheritableDoubleBuilder
    ZDepthOffset: CAM.InheritableDoubleBuilder


    class CutDepthsType(enum.Enum):
        Levels = 0
        RampByDepth = 1
        RampByAngle = 2
    

class VolumeBased25DMillingOperation(CAM.FaceMilling):
    def __init__(self) -> None: ...


class VerticalPosition(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    OffsetType: CAM.VerticalPosition.OffsetTypes
    TeethNumber: float


    class OffsetTypes(enum.Enum):
        Distance = 0
        TeethNumber = 1
        Auto = 2
    

class VectorDistanceMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Distance: float
    DistanceBuilder: CAM.ExpressionDouble
    EndPoint: Point
    EndPointBuilder: CAM.ReferencePoint
    MoveEnd: CAM.VectorDistanceMoveBuilder.EndType
    Vector: Direction
    VectorBuilder: CAM.ReferenceVector


    class EndType(enum.Enum):
        Distance = 0
        Point = 1
    

class VazlMillingBuilder(CAM.PlanarOperationBuilder):
    def __init__(self) -> None: ...
    CutLevel: CAM.CutLevel
    TrimBoundary: CAM.Boundary


class VariableZLevelMilling(CAM.PlanarOperation):
    def __init__(self) -> None: ...


class UserDefinedOprBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    EnvVarName: str


class UserDefinedOpr(CAM.Operation):
    def __init__(self) -> None: ...
    def GetSourceUdop(self) -> CAM.UserDefinedOpr:
        ...
    def SetStatusToRegenerate(self) -> None:
        ...


class UserDefinedMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...


class UpDownCutting(TaggedObject):
    def __init__(self) -> None: ...
    ApplyAtStepover: bool
    ExtendToBoundary: bool
    OptimizePath: bool
    RampDownAngle: CAM.InheritableDoubleBuilder
    RampUpAngle: CAM.InheritableDoubleBuilder


class UdtSectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Delete(self, nodeIndex: int) -> None:
        ...
    def Get(self, index: int, length: float, angle: float, radius: float, sweep: float) -> None:
        ...
    def CreateWithParameter(self, length: float, angle: float, radius: float, sweep: float) -> int:
        ...
    def ModifyWithParameter(self, index: int, length: float, angle: float, radius: float, sweep: float) -> None:
        ...
    NumberOfSections: int


class UdeSet(TaggedObject):
    def __init__(self) -> None: ...
    def CreateUde(self) -> CAM.Ude:
        ...
    def CreateUdeByName(self, udeName: str) -> CAM.Ude:
        ...
    UdeList: CAM.UdeList


class UdeParameter(TaggedObject):
    def __init__(self) -> None: ...
    BooleanValue: bool
    Csys: NXObject
    DoubleValue: float
    IntegerValue: int
    NameOfParameter: str
    OptionText: str
    OptionValue: str
    ParameterActive: bool
    ParameterOptional: bool
    Point: Point
    StringText: str
    StringValue: str
    TypeOfParameter: CAM.UdeParameter.ParameterTypes
    Vector: NXObject


    class ParameterTypes(enum.Enum):
        Integer = 0
        Double = 1
        Boolean = 2
        String = 3
        Option = 4
        Point = 5
        Vector = 6
        Legend = 7
        Group = 8
        Csys = 9
    

class UdeMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    UdeSet: CAM.UdeSet


class UdeList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.Ude]) -> None:
        ...
    def Append(self, object: CAM.Ude) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.Ude) -> int:
        ...
    def FindItem(self, index: int) -> CAM.Ude:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.Ude) -> None:
        ...
    def Erase(self, obj: CAM.Ude, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.Ude]:
        ...
    def SetContents(self, objects: typing.List[CAM.Ude]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.Ude, object2: CAM.Ude) -> None:
        ...
    def Insert(self, location: int, object: CAM.Ude) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class Ude(TaggedObject):
    def __init__(self) -> None: ...
    def GetParameter(self, parameterName: str) -> CAM.UdeParameter:
        ...
    def GetParameter(self, index: int) -> CAM.UdeParameter:
        ...
    def GetParameterNames(self) -> str:
        ...
    NumberOfParameters: int
    OutputLoadTool: bool
    UdeName: str


class TurnToolProbingBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder
    FlipToolAroundHolder: bool
    ProbeParamsBuilder: CAM.ProbeParamsBuilder
    ReorientToolHolder: bool
    ToolHolderAngle: CAM.InheritableDoubleBuilder
    TrackingPointStatus: CAM.TurnToolProbingBuilder.TrackingPointTypes


    class TrackingPointTypes(enum.Enum):
        Fixed = 0
        Rotate = 1
        Auto = 2
    

class TurnToolProbing(CAM.Operation):
    def __init__(self) -> None: ...


class TurnToolBuilder(CAM.TurningToolBuilder):
    def __init__(self) -> None: ...
    ButtonDiameterBuilder: CAM.InheritableDoubleBuilder
    HolderControlAngleBuilder: CAM.InheritableDoubleBuilder
    HolderControlWidthBuilder: CAM.InheritableDoubleBuilder
    HolderHand: CAM.TurnToolBuilder.HolderHands
    HolderShankDefinitionMode: CAM.TurnToolBuilder.HolderShankDefinitionModes
    HolderStyle: CAM.TurnToolBuilder.HolderStyles
    InsertShape: CAM.TurnToolBuilder.InsertShapes
    NoseAngleBuilder: CAM.InheritableDoubleBuilder
    ReliefAngleBuilder: CAM.InheritableDoubleBuilder
    ReliefAngleType: CAM.TurnToolBuilder.ReliefAngleTypes
    SizeBuilder: CAM.InheritableDoubleBuilder
    SizeOption: CAM.TurnToolBuilder.SizeOptions
    ThicknessType: CAM.TurnToolBuilder.ThicknessTypes


    class ThicknessTypes(enum.Enum):
        Thickness01 = 0
        ThicknessT1 = 1
        Thickness02 = 2
        ThicknessT2 = 3
        Thickness03 = 4
        ThicknessT3 = 5
        Thickness04 = 6
        Thickness05 = 7
        Thickness06 = 8
        Thickness07 = 9
        Thickness09 = 10
        Thickness11 = 11
        Thickness12 = 12
        ThicknessUserDefined = 13
    

    class SizeOptions(enum.Enum):
        CutEdgeLength = 0
        InscribedCircle = 1
        InscribedCircleAnsi = 2
    

    class ReliefAngleTypes(enum.Enum):
        A3 = 0
        B5 = 1
        C7 = 2
        D15 = 3
        E20 = 4
        F25 = 5
        G30 = 6
        N0 = 7
        P11 = 8
        OOther = 9
    

    class InsertShapes(enum.Enum):
        Parallelogram85 = 0
        Parallelogram82 = 1
        Diamond80 = 2
        Diamond100 = 3
        Diamond55 = 4
        Diamond75 = 5
        Hexagon = 6
        Parallelogram55 = 7
        Rectangle = 8
        Diamond86 = 9
        Octagon = 10
        Pentagon = 11
        Round = 12
        Square = 13
        Triangle = 14
        Diamond35 = 15
        Trigon = 16
        User = 17
    

    class HolderStyles(enum.Enum):
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        F = 5
        G = 6
        H = 7
        I = 8
        J = 9
        K = 10
        L = 11
        M = 12
        N = 13
        P = 14
        Q = 15
        R = 16
        S = 17
        T = 18
        U = 19
        V = 20
        Ud = 21
    

    class HolderShankDefinitionModes(enum.Enum):
        InsertAndHolder = 0
        CuttingEdgeAngle = 1
    

    class HolderHands(enum.Enum):
        Left = 0
        Neutral = 1
        Right = 2
    

class TurnThreadFinishPassesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, numberOfPasses: int, increment: float) -> None:
        ...
    def Modify(self, index: int, numberOfPasses: int, increment: float) -> None:
        ...
    def Delete(self, nodeIndex: int) -> None:
        ...


class TurnThreadEngageRetractBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Angle: float
    EngageRetractType: CAM.TurnThreadEngageRetractBuilder.EngageRetractTypes
    MoveType: CAM.TurnThreadEngageRetractBuilder.MoveTypes
    VectorXc: float
    VectorYc: float


    class MoveTypes(enum.Enum):
        Engage = 0
        Thread = 1
    

    class EngageRetractTypes(enum.Enum):
        Automatic = 0
        Vector = 1
        Angle = 2
        SameAsEngage = 3
    

class TurnStock(TaggedObject):
    def __init__(self) -> None: ...
    Constant: CAM.InheritableDoubleBuilder
    Face: CAM.InheritableDoubleBuilder
    Radial: CAM.InheritableDoubleBuilder


class TurnRoughVariableIncrementBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, index: int, numOfPasses: int, increment: float) -> None:
        ...
    def Modify(self, index: int, numOfPasses: int, increment: float) -> None:
        ...
    def Delete(self, index: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...


class TurnRoughFinishTestCut(TaggedObject):
    def __init__(self) -> None: ...
    CutType: CAM.TurnRoughFinishTestCut.CutTypes
    Direction: CAM.TurnRoughFinishTestCut.DirectionTypes
    EndOfTestCut: CAM.PostEventsCiBuilder
    FeedIn: CAM.TurnRoughFinishTestCut.FeedInTypes
    FeedInAngle: float
    FeedInLength: float
    FeedOut: CAM.TurnRoughFinishTestCut.FeedOutTypes
    FeedOutAngle: float
    FeedOutLength: float
    MeasuringPoint: Point
    MeasuringPosition: CAM.TurnRoughFinishTestCut.MeasuringPositionTypes
    MeasuringStop: CAM.PostEventsCiBuilder
    NumberOfPasses: int
    ReturnMoveOption: CAM.TurnRoughFinishTestCut.ReturnMoveTypes
    ReturnMovePoint: Point
    SecondaryEndOfTestCut: CAM.PostEventsCiBuilder
    SecondaryMeasuringStop: CAM.PostEventsCiBuilder
    SecondarySequence: CAM.TurnRoughFinishTestCut.SecondarySequenceTypes
    SecondaryStartOfTestCut: CAM.PostEventsCiBuilder
    Sequence: CAM.TurnRoughFinishTestCut.SequenceTypes
    StartOfFinishPass: CAM.PostEventsCiBuilder
    StartOfTestCut: CAM.PostEventsCiBuilder
    Stock: float
    StockMode: CAM.TurnRoughFinishTestCut.StockModeTypes
    StopDistance: float
    StopPercentage: float
    StopPoint: Point
    StopPosition: CAM.TurnRoughFinishTestCut.StopPositionTypes


    class StopPositionTypes(enum.Enum):
        Automatic = 0
        Point = 1
        Length = 2
        Percent = 3
        SameAsFirstTestCut = 4
    

    class StockModeTypes(enum.Enum):
        Automatic = 0
        Specify = 1
        SameAsFirstTestCut = 2
    

    class SequenceTypes(enum.Enum):
        None = 0
        TestCutAndFinish = 1
        TestCutOnly = 2
    

    class SecondarySequenceTypes(enum.Enum):
        None = 0
        Diameter = 1
        Face = 2
    

    class ReturnMoveTypes(enum.Enum):
        Direct = 0
        RadialAxial = 1
        AxialRadial = 2
        SameAsFirstTestCut = 3
    

    class MeasuringPositionTypes(enum.Enum):
        Automatic = 0
        Point = 1
        SameAsFirstTestCut = 2
    

    class FeedOutTypes(enum.Enum):
        None = 0
        Linear = 1
        SameAsProfileRetract = 2
        SameAsFirstTestCut = 3
    

    class FeedInTypes(enum.Enum):
        None = 0
        Linear = 1
        SameAsProfileEngage = 2
        SameAsFirstTestCut = 3
    

    class DirectionTypes(enum.Enum):
        Reverse = 0
        Forward = 1
    

    class CutTypes(enum.Enum):
        Axial = 0
        Contour = 1
    

class TurnRoughFinishLocalReturnBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetLowerLimitType(self) -> CAM.TurnRoughFinishLocalReturnBuilder.LimitTypes:
        ...
    def SetLowerLimitType(self, lowerLimitModeValue: CAM.TurnRoughFinishLocalReturnBuilder.LimitTypes) -> None:
        ...
    def GetUpperLimitType(self) -> CAM.TurnRoughFinishLocalReturnBuilder.LimitTypes:
        ...
    def SetUpperLimitType(self, upperLimitModeValue: CAM.TurnRoughFinishLocalReturnBuilder.LimitTypes) -> None:
        ...
    AdjustmentMode: CAM.TurnRoughFinishLocalReturnBuilder.AdjustmentModeTypes
    Distance: float
    Dwell: float
    DwellUnit: CAM.TurnRoughFinishLocalReturnBuilder.DwellUnitTypes
    EndOfPathBuilder: CAM.PostEventsCiBuilder
    LowerLimit: float
    Mode: CAM.TurnRoughFinishLocalReturnBuilder.ModeTypes
    NumberOfCuts: int
    NumberOfLevels: int
    NumberOfPasses: int
    OperatorMessage: str
    OutputOperatorMessage: bool
    OutputOpskip: bool
    OutputOpstop: bool
    OutputStop: bool
    Point: Point
    ReturnMoveMode: CAM.TurnRoughFinishLocalReturnBuilder.ReturnMoveModeTypes
    StartOfPathBuilder: CAM.PostEventsCiBuilder
    Time: float
    UpperLimit: float


    class ReturnMoveModeTypes(enum.Enum):
        None = 0
        Direct = 1
        RadialAxial = 2
        AxialRadial = 3
        ClearRadialDirect = 4
        ClearAxialDirect = 5
        ClearRadial = 6
        ClearAxial = 7
        RadialClearAxialDirect = 8
        RadialAxialRadial = 9
        RadialClearAxial = 10
        ClearRadialClearAxialDirect = 11
        ClearRadialAxialRadial = 12
        ClearRadialClearAxial = 13
        SameAsDeparture = 14
    

    class ModeTypes(enum.Enum):
        None = 0
        Distance = 1
        Time = 2
        NumberOfPasses = 3
        NumberOfCuts = 4
        NumberOfLevels = 5
    

    class LimitTypes(enum.Enum):
        DistanceOrTime = 0
        Percent = 1
    

    class DwellUnitTypes(enum.Enum):
        None = 0
        Seconds = 1
        Revolutions = 2
    

    class AdjustmentModeTypes(enum.Enum):
        None = 0
        Range = 1
        Alignment = 2
    

class TurnProbeInspectPointMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    def ReverseDirection(self) -> None:
        ...
    Direction: CAM.TurnProbeInspectPointMoveBuilder.DirectionTypes
    Point: Point
    PointBuilder: CAM.ReferencePoint
    ProbeControlParameters: CAM.ProbeControlParametersBuilder
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    ProbeStockParameters: CAM.ProbeStockParametersBuilder
    ProbeToleranceParameters: CAM.ProbeToleranceParametersBuilder
    Vector: NXObject


    class DirectionTypes(enum.Enum):
        Radial = 0
        Axial = 1
        NormalToCurve = 2
        Vector = 3
    

class TurnProbeClearanceBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    AxialPlaneMode: CAM.TurnProbeClearanceBuilder.AxialPlaneModes
    AxialPlanePoint: Point
    AxialPlaneValue: float
    RadialPlaneMode: CAM.TurnProbeClearanceBuilder.RadialPlaneModes
    RadialPlanePoint: Point
    RadialPlaneValue: float


    class RadialPlaneModes(enum.Enum):
        None = 0
        Point = 1
        Distance = 2
    

    class AxialPlaneModes(enum.Enum):
        None = 0
        Point = 1
        Distance = 2
    

class TurnPartProbingBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder
    ProbeParamsBuilder: CAM.ProbeParamsBuilder


class TurnPartProbing(CAM.Operation):
    def __init__(self) -> None: ...


class TurnOverlap(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    Percentage: float
    Type: CAM.TurnOverlap.Types


    class Types(enum.Enum):
        None = 0
        Distance = 1
        Percentage = 2
    

class TurnOrientWcs(TaggedObject):
    def __init__(self) -> None: ...
    WcsOffset: float
    XcMapping: CAM.TurnOrientWcs.XcMappingTypes
    YcMapping: CAM.TurnOrientWcs.YcMappingTypes


    class YcMappingTypes(enum.Enum):
        RadialAxis = 0
        ReversedRadialAxis = 1
        SpindleAxis = 2
        ReversedSpindleAxis = 3
    

    class XcMappingTypes(enum.Enum):
        SpindleAxis = 0
        ReversedSpindleAxis = 1
        RadialAxis = 2
        ReversedRadialAxis = 3
    

class TurnOrientGeomBuilder(CAM.OrientGeomBuilder):
    def __init__(self) -> None: ...
    LatheWorkPlaneType: CAM.TurnOrientGeomBuilder.LatheWorkPlaneTypes
    TurnOrientWcs: CAM.TurnOrientWcs


    class LatheWorkPlaneTypes(enum.Enum):
        XmYm = 0
        ZmXm = 1
    

class TurnMoveToPointBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Direction: CAM.TurnMoveToPointBuilder.DirectionTypes
    OffsetData: CAM.OffsetDataBuilder
    Point: Point
    RoundPoint: CAM.RoundPointBuilder


    class DirectionTypes(enum.Enum):
        Direct = 0
        Radial = 1
        Axial = 2
        RadialAxial = 3
        AxialRadial = 4
    

class TurnMethodBuilder(CAM.MethodBuilder):
    def __init__(self) -> None: ...
    def GetTurnDisplCollTog(self) -> int:
        ...
    def SetTurnDisplCollTog(self, displayValue: int) -> None:
        ...
    FaceStockBuilder: CAM.InheritableDoubleBuilder
    FeedsBuilder: CAM.FeedsTurnBuilder
    RadStockBuilder: CAM.InheritableDoubleBuilder
    StockPartBuilder: CAM.InheritableDoubleBuilder
    TurnEngRetMinDistBuilder: CAM.InheritableDoubleBuilder


class TurningToolBuilder(CAM.ToolBuilder):
    def __init__(self) -> None: ...
    AdapterBlockDepth: float
    AdapterBlockHeight: float
    AdapterBlockLength: float
    AdapterDepth: float
    AdapterDiameter: float
    AdapterHeight: float
    AdapterLength: float
    AdapterStepDiameter: float
    AdapterStepLength: float
    AdapterStyle: CAM.TurningToolBuilder.AdapterStyleTypes
    AdapterTaperAngle: float
    AdapterTaperLength: float
    AdapterUse: bool
    AdapterZOffset: float
    HolderAngleBuilder: CAM.InheritableDoubleBuilder
    HolderLengthBuilder: CAM.InheritableDoubleBuilder
    HolderLock: bool
    HolderShankLineBuilder: CAM.InheritableDoubleBuilder
    HolderShankType: CAM.TurningToolBuilder.HolderShankTypes
    HolderShankWidthBuilder: CAM.InheritableDoubleBuilder
    HolderUse: bool
    HolderWidthBuilder: CAM.InheritableDoubleBuilder
    InsertLengthBuilder: CAM.InheritableDoubleBuilder
    InsertPosition: CAM.TurningToolBuilder.InsertPositions
    InsertWidthBuilder: CAM.InheritableDoubleBuilder
    LeftAngleBuilder: CAM.InheritableDoubleBuilder
    ManageToolPartBuilder: CAM.ManageToolPartBuilder
    MaxDepthBuilder: CAM.InheritableDoubleBuilder
    MaxDepthToggle: bool
    MaxFacingDiameterBuilder: CAM.InheritableDoubleBuilder
    MaxFacingDiameterToggle: bool
    MaxToolReachBuilder: CAM.InheritableDoubleBuilder
    MaxToolReachToggle: bool
    McsSpindleGroup: CAM.NCGroup
    MinBoringDiameterBuilder: CAM.InheritableDoubleBuilder
    MinBoringDiameterToggle: bool
    MinFacingDiameterBuilder: CAM.InheritableDoubleBuilder
    MinFacingDiameterToggle: bool
    NoseRadiusBuilder: CAM.InheritableDoubleBuilder
    NoseWidthBuilder: CAM.InheritableDoubleBuilder
    OrientAngleBuilder: CAM.InheritableDoubleBuilder
    RightAngleBuilder: CAM.InheritableDoubleBuilder
    ThicknessBuilder: CAM.InheritableDoubleBuilder
    TrackingBuilder: CAM.TrackingBuilder
    XMountBuilder: CAM.InheritableDoubleBuilder
    YMountBuilder: CAM.InheritableDoubleBuilder


    class InsertPositions(enum.Enum):
        Topside = 0
        Underside = 1
    

    class HolderShankTypes(enum.Enum):
        Square = 0
        Round = 1
    

    class AdapterStyleTypes(enum.Enum):
        Axial = 0
        Radial = 1
    

class TurningOperationBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    AdditionalCommands: str
    FeedsBuilder: CAM.FeedsTurnBuilder
    FlipToolAroundHolder: bool
    MachineCycleSubroutineName: str
    MotionOutput: CAM.TurningOperationBuilder.MotionOutputOptions
    ReorientToolHolder: bool
    ReorientToolHolderMode: CAM.TurningOperationBuilder.ReorientToolHolderModeOptions
    RotateTrackingPoint: bool
    ToolHolderAngle: CAM.InheritableDoubleBuilder
    TrackingPointStatus: CAM.TurningOperationBuilder.TrackingPointType
    UpdateIpw: bool
    UseMachineCycle: bool


    class TrackingPointType(enum.Enum):
        Fixed = 0
        Rotate = 1
        Auto = 2
    

    class ReorientToolHolderModeOptions(enum.Enum):
        None = 0
        Fixed = 1
        Variable = 2
    

    class MotionOutputOptions(enum.Enum):
        LinearOnly = 0
        Circular = 1
        MachineCycle = 2
    

class TurningOperation(CAM.Operation):
    def __init__(self) -> None: ...


class TurnGrooveCornerControl(TaggedObject):
    def __init__(self) -> None: ...
    CornerType: CAM.TurnGrooveCornerControl.CornerTypes
    CutSequence: CAM.TurnGrooveCornerControl.CutSequenceTypes
    RadiusOrDistance: float
    ReliefPlungeDistance: float
    ReliefPlungeOffset: float
    ReliefPlungeType: CAM.TurnGrooveCornerControl.ReliefPlungeTypes


    class ReliefPlungeTypes(enum.Enum):
        None = 0
        Depth = 1
        WallDepth = 2
        Distance = 3
    

    class CutSequenceTypes(enum.Enum):
        CornersFirst = 0
        CornersFirstAndLast = 1
        CornerWithWall = 2
        CornerAfterWall = 3
        CornersLast = 4
    

    class CornerTypes(enum.Enum):
        None = 0
        FollowPart = 1
        Round = 2
        Break = 3
        RoundIpw = 4
        BreakIpw = 5
    

class TurnGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...


class TurnFeatureGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    AxialTrimPlane1Builder: CAM.TrimPlane
    AxialTrimPlane2Builder: CAM.TrimPlane
    CutRegionSelectionMode: CAM.TurnFeatureGeomBuilder.CutRegionSelectionModes
    CutRegionSelectionPoint: Point
    RadialTrimPlane1Builder: CAM.TrimPlane
    RadialTrimPlane2Builder: CAM.TrimPlane
    SurfaceSensitivityMode: CAM.TurnFeatureGeomBuilder.SurfaceSensitivityModes
    SurfaceSensitivityTolerance: float
    ToleranceOffsetMode: CAM.TurnFeatureGeomBuilder.ToleranceOffsetModes
    TrimPoint1Builder: CAM.TrimPoint
    TrimPoint2Builder: CAM.TrimPoint


    class ToleranceOffsetModes(enum.Enum):
        AfterContainment = 0
        BeforeContainment = 1
    

    class SurfaceSensitivityModes(enum.Enum):
        None = 0
        Distance = 1
    

    class CutRegionSelectionModes(enum.Enum):
        Automatic = 0
        Manual = 1
    

class TurnEngageRetractBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Angle: float
    AutomaticOption: CAM.TurnEngageRetractBuilder.AutoOptions
    DeltaXc: float
    DeltaYc: float
    DirectEngageRetractMode: CAM.TurnEngageRetractBuilder.DirectEngageRetractModes
    DirectTrimPoint: bool
    Distance: float
    EngageRetractType: CAM.TurnEngageRetractBuilder.Types
    ExtendDistance: float
    ExtendMethod: CAM.TurnEngageRetractBuilder.ExtendMethods
    FirstRadius: float
    IgnoreWorkpiece: bool
    Point: Point
    Radius: float
    SafeDistance: float
    SecondRadius: float
    TangentialExtension: bool


    class Types(enum.Enum):
        AutoCircular = 0
        AutoLinear = 1
        Delta = 2
        AngleAndDistance = 3
        RelativeLinear = 4
        FromAPoint = 5
        TwoCircles = 6
        TwoPointTangent = 7
        SameAsEngage = 8
    

    class ExtendMethods(enum.Enum):
        Distance = 0
        ToBlank = 1
    

    class DirectEngageRetractModes(enum.Enum):
        None = 0
        ToOrFromTrimPointOnly = 1
        Always = 2
    

    class AutoOptions(enum.Enum):
        UserDefinedValues = 0
        AutomaticValues = 1
        ClearWallsByAngleAndDistance = 2
        Withdraw = 3
        WithdrawByDistance = 4
        ClearWalls = 5
        ClearWallsByDistance = 6
        SameAsPlungeRetract = 7
    

class TurnDirection(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.TurnDirection.Types


    class Types(enum.Enum):
        Reverse = 0
        Forward = 1
    

class TurnCutterClearance(TaggedObject):
    def __init__(self) -> None: ...
    FirstCuttingEdge: float
    LastCuttingEdge: float


class TurnCutParameters(CAM.CutParameters):
    def __init__(self) -> None: ...
    AdditionalProfiling: bool
    AllowUndercut: bool
    ChipControl: CAM.ChipControl
    CleanupControl: CAM.CutParametersCleanupControlTypes
    ConcaveCornerControl: CAM.TurnConcaveCornerControl
    ContourDiameterAngle: CAM.ContourAngle
    ContourFaceAngle: CAM.ContourAngle
    ContourLevelAngle: CAM.ContourAngle
    ContourSteepAngle: CAM.ContourAngle
    CutConnection: CAM.CutParametersCutConnectionTypes
    CutDwell: CAM.CutDwell
    CutFillets: CAM.CutParametersFilletsTypes
    ExtendAtStart: CAM.CutParametersExtendAtStartMode
    FacesSequence: CAM.FacesSequence
    FinishDwell: CAM.FinishDwell
    FinishPasses: CAM.CutParametersFinishPassesTypes
    GrooveCornerControl: CAM.TurnGrooveCornerControl
    InitialProfilePlunge: CAM.InitialProfilePlunge
    MinCutDepth: CAM.MinCutDepth
    MinCutLength: CAM.MinCutLength
    MultiPasses: CAM.StepoverBuilder
    MultiRamp: CAM.MultiRamp
    NormalCorner: CAM.TurnCornerControl
    OmitLastPass: bool
    ProfileCutRegions: CAM.CutParametersProfileCutRegionsTypes
    ProfileDirection: CAM.TurnDirection
    ProfileStrategy: CAM.ProfileStrategy
    RampingMode: CAM.RampingMode
    ReliefCut: CAM.ReliefCut
    ReliefPlunge: CAM.ReliefPlunge
    SecondaryTestCut: CAM.TurnRoughFinishTestCut
    ShallowCorner: CAM.TurnCornerControl
    SpringPasses: CAM.SpringPasses
    StopPosition: CAM.StopPosition
    TestCut: CAM.TurnRoughFinishTestCut
    TurnBlankStock: CAM.TurnStock
    TurnCutterClearance: CAM.TurnCutterClearance
    TurnOverlap: CAM.TurnOverlap
    TurnPartStock: CAM.TurnStock
    TurnProfileStock: CAM.TurnStock


class TurnCornerControl(TaggedObject):
    def __init__(self) -> None: ...
    MinAngle: float
    Radius: float
    Type: CAM.TurnCornerControl.Types


    class Types(enum.Enum):
        RollAround = 0
        ExtendTangents = 1
        Round = 2
        Break = 3
    

class TurnConcaveCornerControl(TaggedObject):
    def __init__(self) -> None: ...
    Radius: float
    RadiusOption: CAM.TurnConcaveCornerControl.RadiusOptions
    Type: CAM.TurnConcaveCornerControl.Types


    class Types(enum.Enum):
        ExtendTangents = 0
        Round = 1
    

    class RadiusOptions(enum.Enum):
        Specify = 0
        ToolRadius = 1
        AddToToolRadius = 2
    

class TurnBoundaryGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    Blank: CAM.BoundaryTurnBlank
    PartBoundary: CAM.Boundary


class TurnAvoidanceStartOfEngageBuilder(TaggedObject):
    def __init__(self) -> None: ...
    StartOfEngageMotionType: CAM.TurnAvoidanceStartOfEngageBuilder.StartOfEngageMotionTypes


    class StartOfEngageMotionTypes(enum.Enum):
        Automatic = 0
        Direct = 1
        RadialThenAxial = 2
        AxialThenRadial = 3
        ClearRadialThenDirect = 4
        ClearAxialThenDirect = 5
    

class TurnAvoidanceStartBuilder(TaggedObject):
    def __init__(self) -> None: ...
    StartDeltaAngle: float
    StartDeltaDistance: float
    StartDeltaVector: NXObject
    StartDeltaX: float
    StartDeltaY: float
    StartPoint: Point
    StartPointMode: CAM.TurnAvoidanceStartBuilder.StartPointModes
    StartPointMotionType: CAM.TurnAvoidanceStartBuilder.StartPointMotionTypes


    class StartPointMotionTypes(enum.Enum):
        None = 0
        Direct = 1
        RadialThenAxial = 2
        AxialThenRadial = 3
        ClearRadialThenDirect = 4
        ClearAxialThenDirect = 5
    

    class StartPointModes(enum.Enum):
        Point = 0
        DeltaAngleDistance = 1
        DeltaVectorDistance = 2
        DeltaMove = 3
    

class TurnAvoidanceReturnBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ReturnDeltaAngle: float
    ReturnDeltaDistance: float
    ReturnDeltaVector: NXObject
    ReturnDeltaX: float
    ReturnDeltaY: float
    ReturnPoint: Point
    ReturnPointMode: CAM.TurnAvoidanceReturnBuilder.ReturnPointModes
    ReturnPointMotionType: CAM.TurnAvoidanceReturnBuilder.ReturnPointMotionTypes


    class ReturnPointMotionTypes(enum.Enum):
        None = 0
        Automatic = 1
        Direct = 2
        RadialThenAxial = 3
        AxialThenRadial = 4
        ClearRadialThenDirect = 5
        ClearAxialThenDirect = 6
        ClearRadialOnly = 7
        ClearAxialOnly = 8
    

    class ReturnPointModes(enum.Enum):
        Point = 0
        DeltaAngleDistance = 1
        DeltaVectorDistance = 2
        DeltaMove = 3
        SameAsStart = 4
    

class TurnAvoidancePathPointsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetPointListData(self, index: int, specifyPoint: NXObject, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes) -> None:
        ...
    def GetPointData(self, index: int, specifyPoint: NXObject, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes, pointStatus: CAM.TurnAvoidancePathPointsBuilder.PointStatus, startEventFlag: int, startEventPath: NXObject, endEventFlag: int, endEventPath: NXObject) -> None:
        ...
    def GetPointData(self, index: int, specifyPoint: Point, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes, pointStatus: CAM.TurnAvoidancePathPointsBuilder.PointStatus, startEventFlag: int, startEventPath: NXObject, endEventFlag: int, endEventPath: NXObject, toolHolderAngle: float) -> None:
        ...
    def SetPointListData(self, index: int, specifyPoint: NXObject, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes) -> None:
        ...
    def SetPointData(self, index: int, specifyPoint: NXObject, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes, pointStatus: CAM.TurnAvoidancePathPointsBuilder.PointStatus, startEventFlag: int, startEventPath: NXObject, endEventFlag: int, endEventPath: NXObject) -> None:
        ...
    def SetPointData(self, index: int, specifyPoint: Point, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes, pointStatus: CAM.TurnAvoidancePathPointsBuilder.PointStatus, startEventFlag: int, startEventPath: NXObject, endEventFlag: int, endEventPath: NXObject, toolHolderAngle: float) -> None:
        ...
    def Modify(self, index: int, specifyPoint: NXObject, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes) -> None:
        ...
    def ModifyData(self, index: int, specifyPoint: NXObject, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes, pointStatus: CAM.TurnAvoidancePathPointsBuilder.PointStatus, startEventFlag: int, startEventPath: NXObject, endEventFlag: int, endEventPath: NXObject) -> None:
        ...
    def ModifyData(self, index: int, specifyPoint: Point, motionType: CAM.TurnAvoidancePathPointsBuilder.MotionTypes, feedrateType: CAM.TurnAvoidancePathPointsBuilder.FeedrateModesTypes, customFeedrateValue: float, customFeedrateUnit: CAM.TurnAvoidancePathPointsBuilder.CustomFeedrateUnitTypes, pointStatus: CAM.TurnAvoidancePathPointsBuilder.PointStatus, startEventFlag: int, startEventPath: NXObject, endEventFlag: int, endEventPath: NXObject, toolHolderAngle: float) -> None:
        ...
    def Delete(self, index: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...
    CsMode: CAM.TurnAvoidancePathPointsBuilder.CsTypes
    PointListDataNumberOfTrackPoints: int


    class PointStatus(enum.Enum):
        Inactive = 0
        Active = 1
    

    class MotionTypes(enum.Enum):
        Automatic = 0
        Direct = 1
        RadialThenAxial = 2
        AxialThenRadial = 3
    

    class FeedrateModesTypes(enum.Enum):
        Rapid = 0
        ApproachOrDepature = 1
        EngageOrReturn = 2
        Cut = 3
        Custom = 4
    

    class CustomFeedrateUnitTypes(enum.Enum):
        None = 0
        IpmOrMmpm = 1
        IprOrMmpr = 2
    

    class CsTypes(enum.Enum):
        Wcs = 0
        Mcs = 1
    

class TurnAvoidanceGohomeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    GohomePoint: Point
    GohomePointMode: CAM.TurnAvoidanceGohomeBuilder.GohomePointModes
    GohomePointMotionType: CAM.TurnAvoidanceGohomeBuilder.GohomePointMotionTypes


    class GohomePointMotionTypes(enum.Enum):
        None = 0
        Direct = 1
        RadialThenAxial = 2
        AxialThenRadial = 3
        ClearRadialThenDirect = 4
        ClearAxialThenDirect = 5
    

    class GohomePointModes(enum.Enum):
        Point = 0
        SameAsFrom = 1
    

class TurnAvoidanceGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    AvoidanceApproachBuilder: CAM.TurnAvoidanceApproachBuilder
    AvoidanceClearanceBuilder: CAM.TurnAvoidanceClearanceBuilder
    AvoidanceDepartureBuilder: CAM.TurnAvoidanceDepartureBuilder
    AvoidanceFromBuilder: CAM.TurnAvoidanceFromBuilder
    AvoidanceGohomeBuilder: CAM.TurnAvoidanceGohomeBuilder
    AvoidanceReturnBuilder: CAM.TurnAvoidanceReturnBuilder
    AvoidanceStartBuilder: CAM.TurnAvoidanceStartBuilder
    AvoidanceStartOfEngageBuilder: CAM.TurnAvoidanceStartOfEngageBuilder


class TurnAvoidanceFromBuilder(TaggedObject):
    def __init__(self) -> None: ...
    FromPoint: Point
    FromPointMode: CAM.TurnAvoidanceFromBuilder.FromPointModes


    class FromPointModes(enum.Enum):
        None = 0
        Point = 1
    

class TurnAvoidanceDepartureBuilder(TaggedObject):
    def __init__(self) -> None: ...
    DeparturePathMode: CAM.TurnAvoidanceDepartureBuilder.DeparturePathModes
    DeparturePathPointsListBuilder: CAM.TurnAvoidancePathPointsBuilder
    DeparturePathReorientToolHolderMode: CAM.TurnAvoidanceDepartureBuilder.DeparturePathReorientToolHolderModes


    class DeparturePathReorientToolHolderModes(enum.Enum):
        None = 0
        Variable = 1
    

    class DeparturePathModes(enum.Enum):
        None = 0
        Points = 1
        SameAsApproach = 2
        PointsBeforeToolChange = 3
        SameAsApproachBeforeToolChange = 4
    

class TurnAvoidanceClearanceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AxialPlaneMode: CAM.TurnAvoidanceClearanceBuilder.AxialPlaneModes
    AxialPlanePoint: Point
    AxialPlaneValue: float
    RadialPlaneMode: CAM.TurnAvoidanceClearanceBuilder.RadialPlaneModes
    RadialPlanePoint: Point
    RadialPlaneValue: float


    class RadialPlaneModes(enum.Enum):
        None = 0
        Point = 1
        Distance = 2
    

    class AxialPlaneModes(enum.Enum):
        None = 0
        Point = 1
        Distance = 2
    

class TurnAvoidanceApproachBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ApproachPathMode: CAM.TurnAvoidanceApproachBuilder.ApproachPathModes
    ApproachPathPointsListBuilder: CAM.TurnAvoidancePathPointsBuilder
    ApproachPathReorientToolHolderMode: CAM.TurnAvoidanceApproachBuilder.ApproachPathReorientToolHolderModes


    class ApproachPathReorientToolHolderModes(enum.Enum):
        None = 0
        Variable = 1
    

    class ApproachPathModes(enum.Enum):
        None = 0
        Points = 1
        PointsAfterToolChange = 2
    

class TToolBuilder(CAM.MillingToolBuilder):
    def __init__(self) -> None: ...


class TrochoidalSettings(TaggedObject):
    def __init__(self) -> None: ...
    MinWidth: CAM.InheritableToolDepBuilder
    StepAhead: CAM.InheritableToolDepBuilder
    Width: CAM.InheritableToolDepBuilder


class TrimPoint(TaggedObject):
    def __init__(self) -> None: ...
    Angle: CAM.InheritableDoubleBuilder
    AngleOffset: CAM.InheritableDoubleBuilder
    AngleOption: CAM.TrimPoint.AngleOptions
    CheckPartGeometryBeyondTrim: bool
    ExtendDistance: CAM.InheritableDoubleBuilder
    Option: CAM.TrimPoint.Options
    Point: Point
    RampAngle: CAM.InheritableDoubleBuilder
    RampAngleOffset: CAM.InheritableDoubleBuilder
    RampAngleOption: CAM.TrimPoint.RampAngleOptions
    RampAngleVector: NXObject
    Vector: NXObject


    class RampAngleOptions(enum.Enum):
        None = 0
        Aligned = 1
        Vector = 2
        Angle = 3
    

    class Options(enum.Enum):
        None = 0
        Point = 1
    

    class AngleOptions(enum.Enum):
        Auto = 0
        Vector = 1
        Angle = 2
    

class TrimPlane(TaggedObject):
    def __init__(self) -> None: ...
    LimitOption: CAM.TrimPlane.LimitOptions
    Point: Point
    Radius: CAM.InheritableDoubleBuilder


    class LimitOptions(enum.Enum):
        None = 0
        Point = 1
        Distance = 2
    

    class Content(enum.Enum):
        Radial = 0
        Axial = 1
    

class TrackPointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.TrackPoint]:
        ...
    def __init__(self, owner: CAM.Tool) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.TrackPoint:
        ...
    def Tag(self) -> Tag: ...



class TrackpointBuilder(Builder):
    def __init__(self) -> None: ...
    TlAdjReg: int
    TlCutcomReg: int
    TrackingName: str


class TrackPoint(CAM.CAMObject):
    def __init__(self) -> None: ...


class TrackingBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Create(self, name: str, radiusId: int, tpNumber: int, angle: float, radius: float, xOffset: float, yOffset: float, adjustReg: int, cutcomReg: int) -> NXObject:
        ...
    def Modify(self, pointTag: NXObject, name: str, radiusId: int, tpNumber: int, angle: float, radius: float, xOffset: float, yOffset: float, adjustReg: int, cutcomReg: int) -> None:
        ...
    def Delete(self, pointTag: NXObject) -> None:
        ...
    def Get(self, pointTag: NXObject, name: str, radiusId: int, tpNumber: int, angle: float, radius: float, xOffset: float, yOffset: float, adjustReg: int, cutcomReg: int) -> None:
        ...
    def GetTrackPoint(self, position: int) -> NXObject:
        ...
    NumberOfTrackPoints: int


class Topology(Builder):
    def __init__(self) -> None: ...
    def GetShellCount(self) -> int:
        ...
    def Rebuild(self) -> None:
        ...
    def UnifyMaterialSide(self, shellIndex: int) -> None:
        ...
    def ReverseMaterialSide(self, shellIndex: int) -> None:
        ...
    def RemoveShell(self, shellIndex: int) -> None:
        ...
    AngleTolerance: float
    DistanceTolerance: float


class ToolTrackingPointBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    def GetTrackingPoint(self) -> int:
        ...
    def SetTrackingPoint(self, index: int) -> None:
        ...
    def GetXoffsetToggle(self) -> bool:
        ...
    def SetXoffsetToggle(self, index: int, xoffstat: bool) -> None:
        ...
    def GetXoffset(self) -> float:
        ...
    def SetXoffset(self, index: int, xoff: float) -> None:
        ...
    def GetYoffsetToggle(self) -> bool:
        ...
    def SetYoffsetToggle(self, index: int, yoffstat: bool) -> None:
        ...
    def GetYoffset(self) -> float:
        ...
    def SetYoffset(self, index: int, yoff: float) -> None:
        ...
    def GetZoffsetToggle(self) -> bool:
        ...
    def SetZoffsetToggle(self, index: int, zoffstat: bool) -> None:
        ...
    def GetZoffset(self) -> float:
        ...
    def SetZoffset(self, index: int, zoff: float) -> None:
        ...
    def GetAdjustRegisterToggle(self) -> bool:
        ...
    def SetAdjustRegisterToggle(self, index: int, adjregstat: bool) -> None:
        ...
    def GetAdjustRegister(self) -> int:
        ...
    def SetAdjustRegister(self, index: int, adjreg: int) -> None:
        ...


class ToolPositioningBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ToolPositioningMethod: CAM.ToolPositioningBuilder.ToolPositioning


    class ToolPositioning(enum.Enum):
        On = 0
        NearTanto = 1
        FarTanto = 2
    

class ToolPathTiltTilting(Builder):
    def __init__(self) -> None: ...
    def GetTiltingDriveCurve(self, curves: typing.List[TaggedObject]) -> None:
        ...
    def SetTiltingDriveCurve(self, curves: typing.List[TaggedObject]) -> None:
        ...
    FanDistance: CAM.InheritableToolDepBuilder
    ManualTiltingType: CAM.ToolPathTiltTilting.ManualTiltTypes
    ReferenceType: CAM.ToolPathTiltTilting.ReferenceTypes
    TiltAngle: float
    TiltingDistanceType: CAM.ToolPathTiltTilting.ToolAxisTiltingDistTypes
    TiltingDrivePoint: TaggedObject
    TiltingRotationAngle: float
    TiltingRuleType: CAM.ToolPathTiltTilting.ToolAxisTiltingRuleTypes
    ToolTiltMethodType: CAM.ToolPathTiltTilting.ToolAxisTypes


    class ToolAxisTypes(enum.Enum):
        TowardCurve = 0
        FromCurve = 1
        TowardPoint = 2
        FromPoint = 3
        RelativeAngle = 4
    

    class ToolAxisTiltingRuleTypes(enum.Enum):
        MainDir = 0
        AwayFrom = 1
        TowardConst = 2
        Through = 3
    

    class ToolAxisTiltingDistTypes(enum.Enum):
        TwoD = 0
        ThreeD = 1
    

    class ReferenceTypes(enum.Enum):
        Initial = 0
        Zm = 1
    

    class ManualTiltTypes(enum.Enum):
        KeepOriginal = 0
        UserDefined = 1
    

    class AxisType(enum.Enum):
        ThreeToFive = 0
        FiveToFive = 1
    

class ToolPathTiltMachine(Builder):
    def __init__(self) -> None: ...
    MachineMaxStep: CAM.InheritableToolDepBuilder
    MachineToolMainMcs: CAM.ToolPathTiltMachine.ToolMainMcsTypes
    MaxTiltAngle: float
    MaxToolAxisChange: float
    MinTiltAngle: float


    class ToolMainMcsTypes(enum.Enum):
        Xm = 0
        Ym = 1
        Zm = 2
    

class ToolPathTiltClearance(Builder):
    def __init__(self) -> None: ...
    MinHolderClearance: CAM.InheritableToolDepBuilder
    MinNeckClearance: CAM.InheritableToolDepBuilder
    MinShankClearance: CAM.InheritableToolDepBuilder
    TiltClearanceAngle: float


class ToolPathTiltBuilder(Builder):
    def __init__(self) -> None: ...
    FanDistance: CAM.InheritableToolDepBuilder
    MaintainTilt: bool
    MaxMaintainTiltDistance: CAM.InheritableToolDepBuilder
    MaxTiltAngle: float
    MinHolderClearance: CAM.InheritableToolDepBuilder
    MinNeckClearance: CAM.InheritableToolDepBuilder
    MinSafeClearance: CAM.InheritableToolDepBuilder
    MinShankClearance: CAM.InheritableToolDepBuilder
    PreferredTiltAngle: float
    TiltAvoidance: CAM.ToolPathTiltAvoidance
    TiltClearance: CAM.ToolPathTiltClearance
    TiltMachine: CAM.ToolPathTiltMachine
    TiltTilting: CAM.ToolPathTiltTilting
    ToolAxisChange: float


class ToolPathTiltAvoidance(Builder):
    def __init__(self) -> None: ...
    AvoidanceMethod: CAM.ToolPathTiltAvoidance.MethodType
    FanDistance: CAM.InheritableToolDepBuilder
    MaintainTilt: bool
    MaxMaintainTiltDistance: CAM.InheritableToolDepBuilder
    PreferredTiltAngle: float


    class MethodType(enum.Enum):
        Tilt = 0
        Retract = 1
        None = 2
        Warning = 3
        Stop = 4
        Tiltstop = 5
    

    class AxisType(enum.Enum):
        ThreeToFive = 0
        FiveToFive = 1
    

class ToolPathSplitParametersBuilder(Builder):
    def __init__(self) -> None: ...
    MinimumCutLength: CAM.InheritableDoubleBuilder
    OverlapDistance: CAM.InheritableDoubleBuilder
    SplitType: CAM.ToolPathSplitParametersBuilder.SplitTypes
    TransferHeight: float
    TransferHeightBuilder: CAM.InheritableDoubleBuilder
    TransferType: CAM.ToolPathSplitParametersBuilder.TransferTypes
    TransferUsingMethod: CAM.ToolPathSplitParametersBuilder.TransferUsingMethods
    TrimmingSteepAngle: float


    class TransferUsingMethods(enum.Enum):
        None = 0
        RampOnShape = 1
        LiftAndPlunge = 2
    

    class TransferTypes(enum.Enum):
        Direct = 0
        Clearance = 1
        LowestSafeZ = 2
        Smooth = 3
        Plane = 4
    

    class SplitTypes(enum.Enum):
        ByCollision = 0
        ByTransfer = 1
    

class ToolPathSplitItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.ToolPathSplitItemBuilder]) -> None:
        ...
    def Append(self, object: CAM.ToolPathSplitItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.ToolPathSplitItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.ToolPathSplitItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.ToolPathSplitItemBuilder) -> None:
        ...
    def Erase(self, obj: CAM.ToolPathSplitItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.ToolPathSplitItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.ToolPathSplitItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.ToolPathSplitItemBuilder, object2: CAM.ToolPathSplitItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.ToolPathSplitItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ToolPathSplitItemBuilder(Builder):
    def __init__(self) -> None: ...
    Operation: CAM.Operation


class ToolPathSplitBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateToolPathSplitItemBuilder(self) -> CAM.ToolPathSplitItemBuilder:
        ...
    HolderClearance: CAM.InheritableToolDepBuilder
    NeckClearance: CAM.InheritableToolDepBuilder
    OperationList: CAM.ToolPathSplitItemBuilderList
    ShankClearance: CAM.InheritableToolDepBuilder
    SplitType: CAM.ToolPathSplitBuilder.SplitTypes
    ToolPathSplitParametersBuilder: CAM.ToolPathSplitParametersBuilder
    TransferHeight: float
    TransferType: CAM.ToolPathSplitBuilder.TransferTypes
    TransferUsingMethod: CAM.ToolPathSplitBuilder.TransferUsingMethods


    class TransferUsingMethods(enum.Enum):
        None = 0
        RampOnShape = 1
        LiftAndPlunge = 2
    

    class TransferTypes(enum.Enum):
        Direct = 0
        Clearance = 1
        LowestSafeZ = 2
    

    class SplitTypes(enum.Enum):
        ByCollision = 0
        ByTransfer = 1
    

class ToolpathEventType(enum.Enum):
    None = 0
    EndOfPath = 1
    StartOfPath = 2
    StartPointOutput = 3
    MomPostEvent = 4
    SpindleMarker = 5
    ToolChangeMarker = 6
    A3xLinear = 7
    A3xLinearWithFeed = 8
    A3xLinearCustFeed = 9
    A3xCircular = 10
    A3xCircularWithFeed = 11
    A3xCircularCustFeed = 12
    A5xCircular = 13
    A5xCircularWithFeed = 14
    A5xCircularCustFeed = 15
    A3xHelical = 16
    A3xHelicalWithFeed = 17
    A3xHelicalCustFeed = 18
    A5xHelical = 19
    A5xHelicalWithFeed = 20
    A5xHelicalCustFeed = 21
    A3xNurbs = 22
    A3xNurbsWithFeed = 23
    A3xNurbsCustFeed = 24
    A5xNurbs = 25
    A5xNurbsWithFeed = 26
    A5xNurbsCustFeed = 27
    A3xCntctLin = 28
    A3xCntctLinWithFeed = 29
    A3xCntctLinCustFeed = 30
    A3xCntctCir = 31
    A3xCntctCirWithFeed = 32
    A3xCntctCirCustFeed = 33
    A3xCntctHel = 34
    A3xCntctHelWithFeed = 35
    A3xCntctHelCustFeed = 36
    A5xCntctLin = 37
    A5xCntctLinWithFeed = 38
    A5xCntctLinCustFeed = 39
    A5xCntctCir = 40
    A5xCntctCirWithFeed = 41
    A5xCntctCirCustFeed = 42
    A5xCntctHel = 43
    A5xCntctHelWithFeed = 44
    A5xCntctHelCustFeed = 45
    MceFromPoint = 46
    MceStartPoint = 47
    MceStartEngage = 48
    MceReturnPoint = 49
    MceGohomePoint = 50
    MceToolChange = 51
    MceOrigin = 52
    MceSeqno = 53
    MceSetModes = 54
    MceSelectHead = 55
    MceCutcom = 56
    MceSpindleOn = 57
    MceSpindleOff = 58
    MceCoolantOn = 59
    MceCoolantOff = 60
    MceOptStop = 61
    MceStop = 62
    MceOptSkipOn = 63
    MceOptSkipOff = 64
    MceDwell = 65
    MceCycle = 66
    MceAuxfun = 67
    McePrefun = 68
    MceClamp = 69
    MceToolLengthComp = 70
    MceRotate = 71
    MceToolPreselect = 72
    MceUserDefined = 73
    McePprint = 74
    MceOpMessage = 75
    MceGoto = 76
    MceThreadWire = 77
    MceCutWire = 78
    MceFlush = 79
    MceFlushTank = 80
    McePower = 81
    MceWireGuides = 82
    MceWireAngle = 83
    MceFedrat = 84
    MceWireCutcom = 85
    MceLatheThread = 86
    MceGoDelta = 87
    MceFrom = 88
    MceGoHome = 89
    Ude = 90
    UdPath = 91
    StartOfPass = 92
    EndOfPass = 93
    MceSmoothLeadIn = 94
    MceSmoothLeadOut = 95
    MfMessage = 96
    MfCloseDebugFiles = 97
    MfDumpBuffers = 98
    MfChangeStatus = 99
    MfLastClsfEvent = 100
    MfStartOfFillet = 101
    MfOutputGohome = 102
    MfHighlight = 103
    MfFilletParams = 104
    MfOperationName = 105
    MfTldata = 106
    MfMsys = 107
    MfListDeletion = 108
    MfLocalReturnStart = 109
    MfLocalReturnEnd = 110
    MfDisplayFont = 111
    MfSlowdownParams = 112
    MfCutLevelPlane = 113
    MfCounterValue = 114
    MfGouge = 115
    MfUnpropagableEvent = 116
    MfFinalDepartureOutput = 117
    ScudUpdownCut = 118
    SetMarker = 119
    ManualPatternAction = 120
    Udc = 121
    UdcOff = 122
    RegionStartEvent = 123
    RegionEndEvent = 124
    MnActionStartEvent = 125
    MnActionEndEvent = 126
    StartOfConicMotion = 127
    EndOfConicMotion = 128
    MceSpindleReverse = 129
    MceTrackingPointChange = 130
    ParamStartEvent = 131
    ParamEndEvent = 132
    PostangLinear = 133
    PathMarkerEvent = 134
    MceTrackingPointChangeMill = 135
    MceRotateTool = 136
    InspEvent = 137
    PathBlockNcm = 138
    PathBlockRegion = 139
    PathBlockFeature = 140
    MceMeasuringStop = 141
    MceMeasuringAfterFinishing = 142
    MceSuppressWorkpiece = 143
    MceGenericCycle = 144
    CannedCycleOn = 145
    CannedCycleOff = 146
    PostangCircular = 147
    MceUserUsefined = 148
    System = 149


class ToolPathEditorBuilder(Builder):
    def __init__(self) -> None: ...
    def Move(self) -> None:
        ...
    def Extend(self) -> None:
        ...
    def GougeCheck(self) -> None:
        ...
    def SelectAllGouges(self) -> None:
        ...
    def SelectPreviousGouge(self) -> None:
        ...
    def SelectNextGouge(self) -> None:
        ...
    def MoveToClearancePlane(self) -> None:
        ...
    def GetNumberOfGouges(self) -> int:
        ...
    def Reverse(self) -> None:
        ...
    def Trim(self) -> None:
        ...
    ArcAngle: float
    ArcRadius: float
    DeltaXC: float
    DeltaYC: float
    DeltaZC: float
    ExtendDirection: Axis
    ExtendMethod: CAM.ToolPathEditorBuilder.ExtendMethodType
    FirstLinearDistance: float
    GougeCheckClearanceMethod: CAM.ToolPathEditorBuilder.ClearanceMethodType
    GougeCheckClearancePlane: NXObject
    HolderCheck: bool
    MotionMethod: CAM.ToolPathEditorBuilder.MotionMethodType
    MoveStartPoint: bool
    PermanentBoundary: NXObject
    ReferencePoint: Point
    SecondLinearDistance: float
    ToPoint: Point
    TransformCircles: bool
    TrimClearanceMethod: CAM.ToolPathEditorBuilder.ClearanceMethodType
    TrimClearancePlane: NXObject
    TrimConnectionMethod: CAM.ToolPathEditorBuilder.ConnectionMethodType
    TrimDirection: Axis
    TrimGeometry: CAM.ToolPathEditorBuilder.TrimGeometryType
    TrimLine: NXObject
    TrimPlane: NXObject
    TrimSide: CAM.ToolPathEditorBuilder.TrimSideType


    class TrimSideType(enum.Enum):
        Outside = 0
        Inside = 1
    

    class TrimPathType(enum.Enum):
        Single = 0
        Range = 1
        BetweenRapids = 2
        CutLevel = 3
    

    class TrimMethod(enum.Enum):
        Geometry = 0
        Path = 1
    

    class TrimGeometryType(enum.Enum):
        Plane = 0
        LineInView = 1
        Boundary = 2
        PermanentBoundary = 3
        SelectionInView = 4
    

    class MotionMethodType(enum.Enum):
        Delta = 0
        ToAPoint = 1
    

    class ExtendMethodType(enum.Enum):
        Linear = 0
        Arc = 1
        LinearArc = 2
        ArcLinear = 3
        LinearArcLinear = 4
    

    class ConnectionMethodType(enum.Enum):
        ClearancePlane = 0
        Direct = 1
    

    class ClearanceMethodType(enum.Enum):
        Specify = 0
        UseOperation = 1
    

class ToolPathDivideBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAllDivideEvents(self) -> int:
        ...
    def RemoveAllDivideEvents(self) -> None:
        ...
    def AddDivideEvent(self, divideEvent: int) -> None:
        ...
    def GetDivideEvent(self, index: int) -> int:
        ...
    def RemoveDivideEvent(self, divideEvent: int) -> None:
        ...
    ClearancePlane: NXObject
    DistanceLimit: float
    DivideType: CAM.ToolPathDivideBuilder.PathDivideType
    NumberOfDivideEvents: int
    TimeLimit: float
    TolerancePercent: float
    UdeEndOfPath: NXObject
    UdeStartOfPath: NXObject


    class PathDivideType(enum.Enum):
        ByTime = 0
        ByDistance = 1
        ByEvents = 2
    

class ToolChangePositionBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Point: Point
    Vector: Direction


class ToolChangeCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AdjustRegister: CAM.InheritableIntBuilder
    AdjustRegisterToggle: bool
    Angle: CAM.InheritableDoubleBuilder
    AngleToggle: bool
    CutcomRegister: CAM.InheritableIntBuilder
    CutcomRegisterToggle: bool
    HeadDesignation: CAM.ToolChangeCiBuilder.HeadDesignationTypes
    HolderNumber: CAM.InheritableIntBuilder
    HolderToggle: bool
    ManualToolChange: bool
    Number: CAM.InheritableIntBuilder
    NumberToggle: bool
    Radius: CAM.InheritableDoubleBuilder
    RadiusToggle: bool
    TextToggle: bool
    TextValue: str
    Xoffset: CAM.InheritableDoubleBuilder
    XoffsetToggle: bool
    Yoffset: CAM.InheritableDoubleBuilder
    YoffsetToggle: bool
    Zoffset: CAM.InheritableDoubleBuilder
    ZoffsetToggle: bool


    class HeadDesignationTypes(enum.Enum):
        None = 0
        Front = 1
        Rear = 2
        Right = 3
        Left = 4
        Side = 5
        Saddle = 6
    

class ToolBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def GetMaterial(self) -> str:
        ...
    def SetMaterial(self, libRef: str) -> None:
        ...
    def GetMaterialData(self, libRef: str, name: str, description: str, code: str) -> None:
        ...
    ChannelName: str
    CutterExportBuilder: CAM.CutterExport
    HolderDescription: str
    HolderLibraryReference: str
    IncrementalTurretRotationBuilder: CAM.InheritableDoubleBuilder
    IndexNotchBuilder: CAM.InheritableDoubleBuilder
    LibraryParametersBuilder: CAM.Ude
    TlCtlgNum: str
    TlDescription: str
    TlHolderNumberBuilder: CAM.InheritableIntBuilder
    TlLibref: str
    TlManualToolChange: bool
    TlNumberBuilder: CAM.InheritableIntBuilder
    TlText: str


class ToolAxisVariable(CAM.ToolAxisBase):
    def __init__(self) -> None: ...
    ApplySmoothing: bool
    FanDistance: CAM.InheritableToolDepBuilder
    InterpolateAngleToDrive: CAM.InterpolateAngle
    InterpolateAngleToPart: CAM.InterpolateAngle
    InterpolateVector: CAM.InterpolateVector
    LeadAngle: float
    MaximumLeadAngle: float
    MaximumLeadAngleType: CAM.ToolAxisVariable.MaximumLeadAngleTypes
    MaximumTiltAngle: float
    MinimumHeelClearanceDistance: float
    MinimumLeadAngle: float
    MinimumTiltAngle: float
    NominalLeadAngle: float
    NominalLeadAngleType: CAM.ToolAxisVariable.NominalLeadAngleTypes
    RotationAngle: float
    RotationAxis: Direction
    RulingType: CAM.ToolAxisVariable.RulingTypes
    SwarfTiltAngle: float
    TiltAngle: float
    ToolAxisType: CAM.ToolAxisVariable.Types
    ZagLeadAngle: float
    ZagRotationAngle: float
    ZagRotationAxis: Direction
    ZagTiltAngle: float


    class Types(enum.Enum):
        AwayFromPoint = 0
        TowardPoint = 1
        AwayFromLine = 2
        TowardLine = 3
        RelativeToVector = 4
        NormalToPart = 5
        RelativeToPart = 6
        FourAxisNormalToPart = 7
        FourAxisRelativeToPart = 8
        DualFourAxisOnPart = 9
        InterpolateVector = 10
        InterpolateAngleToPart = 11
        InterpolateAngleToDrive = 12
        OptimizedToDrive = 13
        NormalToDrive = 14
        SwarfDrive = 15
        RelativeToDrive = 16
        FourAxisNormalToDrive = 17
        FourAxisRelativeToDrive = 18
        DualFourAxisOnDrive = 19
        SameAsDrivePath = 20
        UserDefined = 21
        Automatic = 22
        AlignToEdges = 23
        SwarfBaseUV = 24
        FourAxisAroundRotaryAxis = 25
        TiltTowardCurve = 26
        TiltAwayFromCurve = 27
        Fixed = 28
    

    class RulingTypes(enum.Enum):
        GridOrTrim = 0
        BaseUv = 1
    

    class NominalLeadAngleTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class MaximumLeadAngleTypes(enum.Enum):
        None = 0
        Specify = 1
    

class ToolAxisTilt(TaggedObject):
    def __init__(self) -> None: ...
    def GetCurves(self, curves: typing.List[Curve]) -> None:
        ...
    def SetCurves(self, curves: typing.List[Curve]) -> None:
        ...
    Angle: float
    MaxWallHeight: float
    Point: Point
    TiltAngleType: CAM.ToolAxisTilt.TiltAngleTypes
    Type: CAM.ToolAxisTilt.Types


    class Types(enum.Enum):
        None = 0
        AwayFromPart = 7
        AwayFromPoint = 9
        TowardPoint = 10
        AwayFromCurve = 13
        TowardCurve = 14
    

    class TiltAngleTypes(enum.Enum):
        Automatic = 0
        Specify = 1
    

class ToolAxisInterpolate(TaggedObject):
    def __init__(self) -> None: ...
    def ResetToDefault(self) -> None:
        ...
    def GetPoint(self, index: int) -> Point:
        ...
    def GetTotalNumberOfPoints(self) -> int:
        ...
    ControlDirection: CAM.ToolAxisInterpolate.ControlDirectionTypes
    InterpolationMethod: CAM.ToolAxisInterpolate.InterpolationMethodTypes
    TurnInputMode: CAM.ToolAxisInterpolate.TurnInputModeTypes
    TurnInterpolationMethod: CAM.ToolAxisInterpolate.TurnInterpolationMethodTypes


    class TurnInterpolationMethodTypes(enum.Enum):
        Absolute = 0
        Relative = 1
    

    class TurnInputModeTypes(enum.Enum):
        HolderAngleFromPart = 0
        ClearanceAngle = 1
        CuttingAngle = 2
    

    class InterpolationMethodTypes(enum.Enum):
        Linear = 0
        CubicSpline = 1
        Smooth = 2
    

    class InterpolateTypes(enum.Enum):
        Vector = 0
        AngleToPart = 1
        AngleToDrive = 2
    

    class ControlDirectionTypes(enum.Enum):
        Uandv = 0
        U = 1
        V = 2
    

class ToolAxisFixed(CAM.ToolAxisBase):
    def __init__(self) -> None: ...
    IsPreferredAnglesDefined: bool
    PreferredFifthAngle: float
    PreferredFourthAngle: float
    TangentToCurveAngle: float
    ToolAxisType: CAM.ToolAxisFixed.Types


    class Types(enum.Enum):
        None = 0
        Fixed = 1
        NormalToPart = 2
        NormalToFirstFace = 3
        Dynamic = 4
        TangentToCurve = 5
        TangentToCurveAtAngle = 6
    

class ToolAxisCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ToolAxis: int


class ToolAxisChange(TaggedObject):
    def __init__(self) -> None: ...
    ExtendAtConvexCorner: bool
    LiftAtConvexCorner: bool
    MaxCornerAngle: CAM.InheritableDoubleBuilder
    MaxToolAxisChange: CAM.InheritableDoubleBuilder
    Method: CAM.ToolAxisChange.MethodTypes
    MinToolAxisChange: CAM.InheritableDoubleBuilder
    TiltAngle: CAM.InheritableDoubleBuilder


    class MethodTypes(enum.Enum):
        PerStep = 0
        PerMinute = 1
    

class ToolAxisBase(TaggedObject):
    def __init__(self) -> None: ...
    Point: Point
    Vector: Direction


class ToolAxisAdvanced(TaggedObject):
    def __init__(self) -> None: ...
    InterpolateVector: CAM.InterpolateVector
    LeadingAngle: float
    MinimumLeadAngle: float
    PreviewMaximumDistanceBuilder: CAM.InheritableToolDepBuilder
    PrimaryLeadAngles: CAM.LeadAngles
    RotateAbout: CAM.ToolAxisAdvanced.RotateAboutType
    SecondaryLeadAngles: CAM.LeadAngles
    SmoothingMethod: int
    SplitterAngle: float
    SwarfGougeCheck: bool
    TiltAngle: float
    ToolAxisType: CAM.ToolAxisAdvanced.Type
    TrailingAngle: float
    TrailingEdgeClearanceAngle: float


    class Type(enum.Enum):
        Automatic = 0
        InterpolateVector = 1
        BladeSwarf = 2
        FollowBladeUv = 3
    

    class RotateAboutType(enum.Enum):
        PartAxis = 0
        Blade = 1
    

class Tool(CAM.NCGroup):
    def __init__(self) -> None: ...
    def CreateSolidTrackingBuilder(self, csoObject: CAM.SolidTrackPoint) -> CAM.SolidTrackingBuilder:
        ...
    def CreateGenericTrackingBuilder(self, csoObject: CAM.SolidTrackPoint) -> CAM.GenericTrackingBuilder:
        ...
    def CreateProbeTrackingBuilder(self, csoObject: CAM.ProbeTrackPoint) -> CAM.ProbeTrackingBuilder:
        ...
    def UpdateFromLibrary(self) -> None:
        ...
    def GetTypeAndSubtype(self, type: CAM.Tool.Types, subtype: CAM.Tool.Subtypes) -> None:
        ...
    def RetrieveHolder(self, libRef: str) -> bool:
        ...
    def ExportPart(self, libRef: str) -> None:
        ...
    CAMTrackPointCollection: CAM.TrackPointCollection


    class Types(enum.Enum):
        Mill = 0
        Drill = 1
        Turn = 2
        Groove = 3
        Thread = 4
        Wedm = 5
        Barrel = 6
        Tcutter = 7
        Form = 8
        DrillSpcGroove = 9
        Solid = 10
        MillForm = 11
        Laser = 12
        Soft = 12
    

    class Subtypes(enum.Enum):
        Undefined = 0
        Mill5 = 1
        Mill7 = 2
        Mill10 = 3
        MillBall = 4
        DrillStandard = 5
        DrillCenterBell = 6
        DrillCountersink = 7
        DrillSpotFace = 8
        DrillSpotDrill = 9
        DrillBore = 10
        DrillReam = 11
        DrillCounterbore = 12
        DrillTap = 13
        DrillBurnishing = 14
        DrillThreadMill = 15
        DrillBackSpotFace = 16
        DrillStep = 17
        TurnStandard = 18
        TurnButton = 19
        TurnBoringBar = 20
        GrooveStandard = 21
        GrooveRing = 22
        GrooveFullNoseRadius = 23
        GrooveUserDefined = 24
        ThreadStandard = 25
        ThreadButress = 26
        ThreadAcme = 27
        ThreadTrapezoidal = 28
        Generic = 29
        Probe = 30
        MillChamfer = 31
        MillSpherical = 32
        DrillCore = 33
        StdLaser = 34
        Laser = 34
        DrillBackCountersink = 35
        CoaxialLaser = 36
        DrillBoringBar = 37
        DrillChamferBoringBar = 38
    

class ThreadTurningBuilder(CAM.TurningOperationBuilder):
    def __init__(self) -> None: ...
    CrestLine: NXObject
    CrestLineDirection: bool
    CrestOffset: CAM.InheritableDoubleBuilder
    CutParameters: CAM.ThreadCutParameters
    DepthOption: CAM.ThreadTurningBuilder.DepthOptionTypes
    EndLine: NXObject
    EndOffset: CAM.InheritableDoubleBuilder
    InfeedLength: CAM.InheritableDoubleBuilder
    InfeedLengthType: CAM.ThreadTurningBuilder.InfeedLengthTypes
    InfeedMode: CAM.ThreadTurningBuilder.InfeedModes
    InfeedMoveAngle: CAM.InheritableDoubleBuilder
    InfeedStartLineAngle: CAM.InheritableDoubleBuilder
    NonCuttingBuilder: CAM.NcmTurnThreadBuilder
    RootLine: NXObject
    RootOffset: CAM.InheritableDoubleBuilder
    StartOffset: CAM.InheritableDoubleBuilder
    ThreadAngleBuilder: CAM.CutAngle
    TotalDepth: CAM.InheritableDoubleBuilder


    class InfeedModes(enum.Enum):
        None = 0
        Auto = 1
        Specify = 2
    

    class InfeedLengthTypes(enum.Enum):
        Auto = 0
        Specify = 1
    

    class DepthOptionTypes(enum.Enum):
        RootLine = 0
        DepthAndAngle = 1
    

class ThreadTurning(CAM.TurningOperation):
    def __init__(self) -> None: ...


class ThreadToolBuilder(CAM.TurningToolBuilder):
    def __init__(self) -> None: ...
    InsertShape: CAM.ThreadToolBuilder.InsertShapes
    TipOffsetBuilder: CAM.InheritableDoubleBuilder


    class InsertShapes(enum.Enum):
        Standard = 0
        Trapezoidal = 1
    

class ThreadMillingCutParameters(CAM.CylindricalMillingCutParameters):
    def __init__(self) -> None: ...
    CutDirection: CAM.ThreadMillingCutParameters.CutDirectionTypes


    class CutDirectionTypes(enum.Enum):
        Climb = 0
        Conventional = 1
    

class ThreadMillingBuilder(CAM.CylindricalMillingBuilder):
    def __init__(self) -> None: ...
    CutParameters: CAM.ThreadMillingCutParameters
    OppositeDirectionBuilder: CAM.OppositeDirection
    SpringPasses: int


class ThreadMilling(CAM.Operation):
    def __init__(self) -> None: ...


class ThreadedHoleSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.ThreadedHoleSet]) -> None:
        ...
    def Append(self, object: CAM.ThreadedHoleSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.ThreadedHoleSet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.ThreadedHoleSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.ThreadedHoleSet) -> None:
        ...
    def Erase(self, obj: CAM.ThreadedHoleSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.ThreadedHoleSet]:
        ...
    def SetContents(self, objects: typing.List[CAM.ThreadedHoleSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.ThreadedHoleSet, object2: CAM.ThreadedHoleSet) -> None:
        ...
    def Insert(self, location: int, object: CAM.ThreadedHoleSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ThreadedHoleSet(CAM.HoleBossSet):
    def __init__(self) -> None: ...
    def GetStandard(self) -> str:
        ...
    def SetStandard(self, standard: str) -> None:
        ...
    RadialEngage: str
    TapDrillSize: float
    TapDrillSizeBuilder: CAM.InferredDouble


class ThreadedBossSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.ThreadedBossSet]) -> None:
        ...
    def Append(self, object: CAM.ThreadedBossSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.ThreadedBossSet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.ThreadedBossSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.ThreadedBossSet) -> None:
        ...
    def Erase(self, obj: CAM.ThreadedBossSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.ThreadedBossSet]:
        ...
    def SetContents(self, objects: typing.List[CAM.ThreadedBossSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.ThreadedBossSet, object2: CAM.ThreadedBossSet) -> None:
        ...
    def Insert(self, location: int, object: CAM.ThreadedBossSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ThreadedBossSet(CAM.HoleBossSet):
    def __init__(self) -> None: ...
    Height: float


class ThreadCutParameters(CAM.CutParameters):
    def __init__(self) -> None: ...
    ChasePasses: int
    CutDepth: CAM.StepoverBuilder
    FinishPasses: CAM.TurnThreadFinishPassesBuilder
    NumberOfStarts: int
    PitchSetting: CAM.PitchSetting
    Tolerance: CAM.InheritableDoubleBuilder


class TeachmodeTurningBuilder(CAM.TurningOperationBuilder):
    def __init__(self) -> None: ...
    NonCuttingBuilder: CAM.NcmTurningBuilder


class TeachmodeTurning(CAM.TurningOperation):
    def __init__(self) -> None: ...


class TeachmodeRetractSettingsBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    RetractBuilder: CAM.TurnEngageRetractBuilder


class TeachmodeProfileMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    ApplyEngageSettings: bool
    ApplyRetractSettings: bool
    AxialSafeClearance: float
    CornerControlNormal: CAM.TurnCornerControl
    CornerControlShallow: CAM.TurnCornerControl
    CustomDriveCurve: CAM.Boundary
    CutterClearance: CAM.TurnCutterClearance
    Direction: CAM.TurnDirection
    DriveGeometryType: CAM.TeachmodeProfileMoveBuilder.DriveGeometryTypes
    EndCheckBoundary: CAM.Boundary
    Feeds: CAM.FeedsTurnBuilder
    FinishStock: CAM.TurnStock
    NewDriveCurve: CAM.Boundary
    RadialSafeClearance: float
    StartCheckBoundary: CAM.Boundary
    StartCheckConstantStock: float
    StartCheckFaceStock: float
    StartCheckRadialStock: float
    StartPoint: Point
    StartPositionMethod: CAM.TeachmodeProfileMoveBuilder.StartStopPositionMethods
    StartStopBeforeBoundaryOffset: bool
    StopCheckConstantStock: float
    StopCheckFaceStock: float
    StopCheckRadialStock: float
    StopPoint: Point
    StopPositionMethod: CAM.TeachmodeProfileMoveBuilder.StartStopPositionMethods
    Tolerances: CAM.Inheritable2dLength


    class StartStopPositionMethods(enum.Enum):
        Drive = 0
        Point = 1
        Check = 2
        ContourPosition = 3
    

    class DriveGeometryTypes(enum.Enum):
        PreviousCheck = 0
        PreviousDrive = 1
        NewDrive = 2
    

class TeachmodeLinearMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    EndPositionType: CAM.TeachmodeLinearMoveBuilder.EndPositionTypes
    FirstCurve: NXObject
    FirstCurveStock: float
    FirstCurveToolPosition: CAM.TeachmodeLinearMoveBuilder.CurveToolPositionTypes
    InitialRetractAngle: float
    InitialRetractDistance: float
    InitialRetractType: CAM.TeachmodeLinearMoveBuilder.InitialRetractTypes
    MoveType: CAM.TeachmodeLinearMoveBuilder.MoveTypes
    Point: Point
    SecondCurve: NXObject
    SecondCurveStock: float
    SecondCurveToolPosition: CAM.TeachmodeLinearMoveBuilder.CurveToolPositionTypes


    class MoveTypes(enum.Enum):
        Direct = 0
        Radial = 1
        Axial = 2
        RadialAxial = 3
        AxialRadial = 4
    

    class InitialRetractTypes(enum.Enum):
        None = 0
        LinearAuto = 1
        Linear = 2
    

    class EndPositionTypes(enum.Enum):
        Point = 0
        Curves = 1
    

    class CurveToolPositionTypes(enum.Enum):
        To = 0
        On = 1
        Past = 2
    

class TeachmodeEngageSettingsBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    EngageBuilder: CAM.TurnEngageRetractBuilder


class Teaching(Builder):
    def __init__(self) -> None: ...
    def AddNewClass(self, name: str, packageName: str, superName: str) -> None:
        ...
    def RemoveClass(self, name: str, packageName: str) -> None:
        ...
    def RenameClass(self, name: str, packageName: str, newName: str) -> None:
        ...
    def AddNewRule(self, name: str) -> None:
        ...
    def RemoveRule(self) -> None:
        ...
    def RenameRule(self, newName: str) -> None:
        ...
    def GetRulePath(self) -> str:
        ...
    def SetRulePath(self, path: str) -> None:
        ...
    def GetRuleLibraryPath(self) -> str:
        ...
    def SetRuleLibraryPath(self, path: str) -> None:
        ...
    def GetRulePriority(self) -> float:
        ...
    def SetRulePriority(self, priority: float) -> None:
        ...
    def GetRuleCondition(self) -> str:
        ...
    def SetRuleCondition(self, condition: str) -> None:
        ...


class TabPointDataBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.TabPointDataBuilder]) -> None:
        ...
    def Append(self, object: CAM.TabPointDataBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.TabPointDataBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.TabPointDataBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.TabPointDataBuilder) -> None:
        ...
    def Erase(self, obj: CAM.TabPointDataBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.TabPointDataBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.TabPointDataBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.TabPointDataBuilder, object2: CAM.TabPointDataBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.TabPointDataBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TabPointDataBuilder(NXObject):
    def __init__(self) -> None: ...
    EndPoint: Point
    StartPoint: Point
    TabMethod: CAM.TabPointDataBuilder.TabMethodType
    TabThreadMethod: CAM.TabPointDataBuilder.TabThreadMethodType
    TabThreadPoint: Point
    TabWidth: float


    class TabThreadMethodType(enum.Enum):
        SameAsTabStartPoint = 0
        UserDefined = 1
        ThreadAtLeadIn = 2
    

    class TabMethodType(enum.Enum):
        StartAndEndPoint = 0
        PointAndWidth = 1
    

class SurfaceRegions(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    AtTimestamp: bool
    Bodies: SelectBodyList
    BoundaryFaces: SelectFaceList
    CreateRegionsOption: CAM.SurfaceRegions.CreateRegionsTypes
    CutDirection: Direction
    Direction: Direction
    ExcludedFaces: SelectFaceList
    Faces: SelectFaceList
    FeatureType: CAM.SurfaceRegions.FeatureTypes
    IsoclineAngle: float
    LimitSteepByCutDirection: bool
    SeedFace: Face
    SteepBody: Body
    SurfaceRegionName: str
    TraverseInteriorEdges: bool
    UseTangentEdgeAngles: bool


    class FeatureTypes(enum.Enum):
        Face = 0
        RegionOfFaces = 1
        Body = 2
        Steep = 3
    

    class CreateRegionsTypes(enum.Enum):
        Steep = 0
        NonSteep = 1
        SteepAndNonSteep = 2
    

class SurfaceDriveGeometrySetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.SurfaceDriveGeometrySet]) -> None:
        ...
    def Append(self, object: CAM.SurfaceDriveGeometrySet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.SurfaceDriveGeometrySet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.SurfaceDriveGeometrySet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.SurfaceDriveGeometrySet) -> None:
        ...
    def Erase(self, obj: CAM.SurfaceDriveGeometrySet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.SurfaceDriveGeometrySet]:
        ...
    def SetContents(self, objects: typing.List[CAM.SurfaceDriveGeometrySet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.SurfaceDriveGeometrySet, object2: CAM.SurfaceDriveGeometrySet) -> None:
        ...
    def Insert(self, location: int, object: CAM.SurfaceDriveGeometrySet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SurfaceDriveGeometrySet(TaggedObject):
    def __init__(self) -> None: ...
    CustomFeed: bool
    CustomStock: bool
    CustomTolerance: bool
    DriveStock: float
    FeedUnit: CAM.FeedRateUnit
    FeedValue: float
    InitialStock: float
    Intol: float
    Outtol: float
    SafeClearance: float
    Surface: NXObject


class SurfaceDriveGeometry(TaggedObject):
    def __init__(self) -> None: ...
    def CreateEmptyGeometrySet(self) -> CAM.SurfaceDriveGeometrySet:
        ...
    def CreateGeometrySet(self, surface: NXObject) -> CAM.SurfaceDriveGeometrySet:
        ...
    def StartNextRow(self, surface: NXObject) -> CAM.SurfaceDriveGeometrySet:
        ...
    def Commit(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    GeometryList: CAM.SurfaceDriveGeometrySetList


class SurfaceContourBuilder(CAM.MillOperationBuilder):
    def __init__(self) -> None: ...
    def GetDriveMethod(self) -> CAM.SurfaceContourBuilder.DriveMethodTypes:
        ...
    def SetDriveMethod(self, driveMethod: CAM.SurfaceContourBuilder.DriveMethodTypes) -> None:
        ...
    def GetCutRegionsBuilder(self) -> CAM.CutRegionsBuilder:
        ...
    AccessVectorMethod: CAM.SurfaceContourBuilder.AccessVectorMethodType
    AutomaticAuxiliaryFloor: bool
    AutomaticAuxiliaryFloorDistance: float
    AuxiliaryFloorGeometry: CAM.Geometry
    AvoidanceMethods: CAM.AvoidanceMethodsBuilder
    BladeFinish: CAM.BladeFinish
    BladeRough: CAM.BladeRough
    BlendFinish: CAM.BlendFinish
    CheckGeometry: CAM.Geometry
    CheckToolAboveBall: bool
    CleanupType: CAM.SurfaceContourBuilder.CleanupTypes
    CurveOffset: CAM.InheritableToolDepBuilder
    CutAreaGeometry: CAM.Geometry
    CutDirection: CAM.SurfaceContourBuilder.CutDirectionTypes
    CutLevels: CAM.BladeCutLevels
    DmCmBuilder: CAM.DmCmBuilder
    DmSpiralBuilder: CAM.DmSpiralBuilder
    DmSurfBuilder: CAM.DmSurfBuilder
    DmareaMillingBuilder: CAM.DmAmBuilder
    DmboundaryBuilder: CAM.DmBndBuilder
    DmcurveBuilder: CAM.DmCurveBuilder
    DmradBuilder: CAM.DmRadBuilder
    DmtpBuilder: CAM.DmTpBuilder
    EdgeFinish: CAM.EdgeFinish
    FlowBuilder: CAM.FlowBuilder
    GuidedCurveBuilder: CAM.GuidedCurveBuilder
    HubFinish: CAM.HubFinish
    NonCuttingBuilder: CAM.NcmScBuilder
    NumberOfBlades: CAM.InheritableIntBuilder
    PartGeometry: CAM.Geometry
    ProjectionVector: CAM.ProjVecCiBuilder
    RotaryFloorFinishBuilder: CAM.DmRotaryFloorFinishBuilder
    SmoothingRadius: CAM.InheritableToolDepBuilder
    StepoverLift: CAM.InheritableToolDepBuilder
    StreamlineCutPattern: CAM.CutPatternBuilder
    StreamlineCutStep: CAM.DmStreamlineCutStep
    StreamlineStepover: CAM.StepoverBuilder
    StreamlineToolPosition: CAM.DmToolPosition
    StreamlineTrimAndExtend: CAM.DmTrimExtend
    ToolAxis: CAM.ToolAxisCiBuilder
    ToolAxisAdvanced: CAM.ToolAxisAdvanced
    ToolAxisFixed: CAM.ToolAxisFixed
    ToolAxisVariable: CAM.ToolAxisVariable
    ToolContactShift: CAM.InheritableToolDepBuilder
    TrimBoundary: CAM.Boundary
    UserExitCiBuilder: CAM.DmUserExitCiBuilder
    WallGeometry: CAM.Geometry


    class DriveMethodTypes(enum.Enum):
        Undef = 0
        Curve = 1
        Spiral = 2
        Boundary = 3
        AreaMilling = 4
        SurfaceArea = 5
        InterpolatedToolPath = 6
        ToolPath = 7
        RadialCut = 8
        ContourProfile = 9
        FlowCut = 10
        Text = 11
        UserDefined = 12
        BladeRough = 13
        BladeFinish = 14
        HubFinish = 15
        BlendFinish = 16
        EdgeFinish = 17
        RotaryFloorFinish = 18
        TubeFinish = 19
        FreeForm = 20
        FreeFormBuildup = 21
        GuidedCurve = 22
        TubeRough = 23
        TubeAdditiveThinwall = 24
        TubeAdditive = 25
    

    class CutDirectionTypes(enum.Enum):
        Climb = 0
        Conventional = 1
    

    class CleanupTypes(enum.Enum):
        Off = 0
        UncutValley = 1
        SteepArea = 2
        Both = 3
        FlowcutContacts = 4
        FlowcutToolend = 5
        FlowcutBoth = 6
    

    class AccessVectorMethodType(enum.Enum):
        Zm = 0
        NegZm = 1
        Specify = 2
        AwayFromLine = 3
        TowardLine = 4
    

class SurfaceContour(CAM.MillOperation):
    def __init__(self) -> None: ...


class StringList(TaggedObject):
    def __init__(self) -> None: ...
    def GetText(self) -> str:
        ...
    def SetText(self, text: str) -> None:
        ...


class StopPosition(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    Percentage: float
    Point: Point
    Type: CAM.StopPosition.Types


    class Types(enum.Enum):
        None = 0
        Distance = 1
        Percentage = 2
        Point = 3
    

class StockPerPassBuilder(Builder):
    def __init__(self) -> None: ...
    def Modify(self, pass: int, stock: float) -> None:
        ...
    def UpdateList(self, roughPass: int, finishPass: int) -> None:
        ...
    def GetStockOfPass(self, passIndex: int) -> float:
        ...
    ToolDiameter: float


class StepUpBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Distance: CAM.InheritableToolDepBuilder


class StepParamsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, inputIndex: int, diameter: float, length: float, angle: float, radius: float) -> int:
        ...
    def Modify(self, nodeIndex: int, diameter: float, length: float, angle: float, radius: float) -> None:
        ...
    def Delete(self, nodeIndex: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...
    def Get(self, step: int, diameter: float, length: float, angle: float, cornerRadius: float) -> None:
        ...
    NumberOfSteps: int


class StepoverBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AdditionalPasses: int
    Angular: float
    ApplyOn: CAM.StepoverBuilder.ApplyTypes
    BlankContourDepth: CAM.InheritableToolDepBuilder
    BlankContourNoLevels: int
    DistanceBuilder: CAM.InheritableToolDepBuilder
    DistanceMaximumBuilder: CAM.InheritableToolDepBuilder
    DistanceMinimumBuilder: CAM.InheritableToolDepBuilder
    FirstDistance: CAM.InheritableToolDepBuilder
    HorizontalLimitBuilder: CAM.InheritableToolDepBuilder
    InheritableDistance: CAM.InheritableDoubleBuilder
    MaximumAverage: float
    MaximumAverageBuilder: CAM.InheritableToolDepBuilder
    MaximumAverageOnlyBuilder: CAM.InheritableToolDepBuilder
    MaximumBuilder: CAM.InheritableToolDepBuilder
    MaximumPercentBuilder: CAM.InheritableDoubleBuilder
    MinimumAverage: float
    MinimumAverageBuilder: CAM.InheritableToolDepBuilder
    MinimumDistance: CAM.InheritableToolDepBuilder
    MinimumPercentBuilder: CAM.InheritableDoubleBuilder
    MultipleBuilder: CAM.MultipleStepoverBuilder
    NumberAtFirstDirection: int
    NumberAtSecondDirection: int
    NumberOfStepovers: int
    PercentFluteLength: CAM.InheritableDoubleBuilder
    PercentOfDegression: float
    PercentOfRemainingBuilder: CAM.InheritableDoubleBuilder
    PercentThreadLength: CAM.InheritableDoubleBuilder
    PercentToolFlatBuilder: CAM.InheritableDoubleBuilder
    PercentWireBuilder: CAM.InheritableDoubleBuilder
    ScallopBuilder: CAM.InheritableDoubleBuilder
    StepoverType: CAM.StepoverBuilder.StepoverTypes
    StockPerPassBuilder: CAM.StockPerPassBuilder
    UserDefined: CAM.MultipleStepoverBuilder
    ValueOfDegression: CAM.InheritableToolDepBuilder
    VariableMaximumBuilder: CAM.InheritableToolDepBuilder
    VariableMaximumOnlyBuilder: CAM.InheritableToolDepBuilder
    VariableMinimumBuilder: CAM.InheritableToolDepBuilder
    VerticalLimitBuilder: CAM.InheritableToolDepBuilder


    class StepoverTypes(enum.Enum):
        None = 0
        Constant = 1
        Scallop = 2
        PercentToolFlat = 3
        Multiple = 4
        Number = 5
        Maximum = 6
        Angular = 7
        VariableAverage = 8
        VariableMaximum = 9
        UseCutDepth = 10
        PercentRemaining = 11
        PercentWire = 12
        StockPerPass = 13
        PercentThreadLength = 14
        Exact = 15
        PercentFluteLength = 16
        BlankContourConstant = 17
        Degression = 18
        PercentDegression = 19
        UserDefined = 20
    

    class ApplyTypes(enum.Enum):
        OnPlane = 0
        OnPart = 1
    

class SteepContainment(TaggedObject):
    def __init__(self) -> None: ...
    Angle: CAM.InheritableDoubleBuilder
    Type: CAM.SteepContainment.Types


    class Types(enum.Enum):
        None = 0
        SteepOnly = 1
    

class SpunOutlineGeom(TaggedObject):
    def __init__(self) -> None: ...
    def SetPlanesAtAngles(self, startAngle: float, incrementAngle: float, numberOfPlanes: int) -> None:
        ...
    def SetPlanesThroughPoints(self, points: typing.List[Point], incrementAngle: float, numberOfPlanes: int) -> None:
        ...
    def GetPlanesAtAngles(self, startAngle: float, incrementAngle: float, numberOfPlanes: int) -> None:
        ...
    def GetPlanesThroughPoints(self, points: typing.List[Point], incrementAngle: float, numberOfPlanes: int) -> None:
        ...
    def Generate(self) -> bool:
        ...
    def Validate(self) -> bool:
        ...
    CreationMethod: CAM.SpunOutlineGeom.CreationTypes


    class CreationTypes(enum.Enum):
        Automatic = 0
        PlanesAtAngles = 1
        PlanesThroughPoints = 2
        SameAsPart = 3
        None = 4
    

class SpringPasses(TaggedObject):
    def __init__(self) -> None: ...
    Number: int
    Type: CAM.SpringPasses.Types


    class Types(enum.Enum):
        None = 0
        Maintain = 1
        Alternate = 2
    

class SplitterList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.Splitter]) -> None:
        ...
    def Append(self, object: CAM.Splitter) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.Splitter) -> int:
        ...
    def FindItem(self, index: int) -> CAM.Splitter:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.Splitter) -> None:
        ...
    def Erase(self, obj: CAM.Splitter, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.Splitter]:
        ...
    def SetContents(self, objects: typing.List[CAM.Splitter]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.Splitter, object2: CAM.Splitter) -> None:
        ...
    def Insert(self, location: int, object: CAM.Splitter) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class Splitter(TaggedObject):
    def __init__(self) -> None: ...
    def GetWallFaces(self) -> typing.List[NXObject]:
        ...
    def SetWallFaces(self, wallFaces: typing.List[NXObject]) -> None:
        ...
    def RemoveWallFaces(self, faces: typing.List[NXObject]) -> None:
        ...
    def GetBlendFaces(self) -> typing.List[NXObject]:
        ...
    def SetBlendFaces(self, blendFaces: typing.List[NXObject]) -> None:
        ...
    def RemoveBlendFaces(self, faces: typing.List[NXObject]) -> None:
        ...
    CountOfFaces: int


class SplitSubopCommand(Builder):
    def __init__(self) -> None: ...
    DividePlane: Plane
    EndPoint: Point
    LinePlaneType: CAM.SplitSubopCommand.LinePlaneTypes
    RotateAngle: float
    StartPoint: Point
    Type: CAM.SplitSubopCommand.Types


    class Types(enum.Enum):
        Line = 0
        Plane = 1
        Point = 2
    

    class LinePlaneTypes(enum.Enum):
        ParallelToToolaxis = 0
        NormalToToolaxis = 1
        SpecifyAngle = 2
    

class SolidTrackPoint(CAM.TrackPoint):
    def __init__(self) -> None: ...


class SolidTrackingBuilder(CAM.TrackpointBuilder):
    def __init__(self) -> None: ...
    Location: NXObject
    TrackingXOff: float
    TrackingYOff: float
    TrackingZOff: float


class SolidToolBuilder(CAM.ToolBuilder):
    def __init__(self) -> None: ...
    TlMountingJunction: NXObject


class SoftTool(CAM.ToolBuilder):
    def __init__(self) -> None: ...
    HolderSection: CAM.HolderSectionBuilder


class SmallAreaAvoidance(TaggedObject):
    def __init__(self) -> None: ...
    AreaSize: CAM.InheritableToolDepBuilder
    SmallAreaStatus: CAM.SmallAreaAvoidance.StatusTypes


    class StatusTypes(enum.Enum):
        Cut = 0
        Ignore = 1
    

class SimulationOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSkipLevel(self, nLevel: int) -> bool:
        ...
    def SetSkipLevel(self, nLevel: int, bValue: bool) -> None:
        ...
    AnalyzeMachiningTime: bool
    AnimationAccuracy: CAM.SimulationOptionsBuilder.Accuracy
    CacheNcProgram: bool
    CheckLimitViolation: bool
    CheckToolHolder: bool
    CheckToolHolderGougeCheck: bool
    CheckToolHolderIpw: bool
    ChordalTolerance: float
    CollisionConfigurationBuilder: CAM.CollisionConfigurationBuilder
    Collshape: CAM.SimulationOptionsBuilder.ToolShapeColl
    DetectAirCuttingTime: bool
    DisplayByTime: bool
    DisplayIpw: bool
    DisplayStationary: CAM.SimulationOptionsBuilder.Stationary
    EnableCollision: CAM.SimulationOptionsBuilder.Enable
    EnableDisplay: CAM.SimulationOptionsBuilder.Enable
    EnableIpw: CAM.SimulationOptionsBuilder.IpwEnable
    EnableMachineCollision: bool
    EnableMaterialRemoval: bool
    HideBlankGeometry: bool
    HidePartGeometry: bool
    HistoryBuffer: int
    InterpretContactContour: bool
    IpwColor: NXColor
    IpwResolution: CAM.SimulationOptionsBuilder.Resolution
    IpwUpdate: CAM.SimulationOptionsBuilder.IpwUpdateMode
    MaxAngularIncr: float
    MaxLengthIncr: float
    MaxTimeIncr: float
    MinSimulationTime: float
    Mrshape: CAM.SimulationOptionsBuilder.ToolShapeMR
    SaveAsPartfile: bool
    SimulationDisplay: CAM.SimulationOptionsBuilder.SimulationDisplayMode
    SkipAllLevels: bool
    StockSetting: CAM.SimulationOptionsBuilder.StockType
    StockValue: float
    StopOnCollision: bool
    StopOnHistoryBuffer: bool
    StopOnLimitViolation: bool
    StopOnM1: bool
    StopOnRapidThroughIpw: bool
    ToolIpwCollision: bool
    ToolPartCollision: bool
    ToolShape: CAM.SimulationOptionsBuilder.ToolShapeType
    ToolTraceSize: int
    TranslucencyValue: int


    class ToolShapeType(enum.Enum):
        Parameter = 1
        Assembly = 2
    

    class ToolShapeMR(enum.Enum):
        Parameter = 1
        Assembly = 2
    

    class ToolShapeColl(enum.Enum):
        Unknown = 0
        Parameter = 1
        Assembly = 2
    

    class StockType(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

    class Stationary(enum.Enum):
        Eath = 0
        Part = 1
        Tool = 2
    

    class SimulationDisplayMode(enum.Enum):
        SuppressAll = 0
        SuppressGraphics = 1
        All = 2
    

    class Resolution(enum.Enum):
        Fast = 0
        Normal = 1
        Fine = 2
        ExtraFine = 3
    

    class IpwUpdateMode(enum.Enum):
        MotionBased = 0
        LengthIncrement = 1
    

    class IpwEnable(enum.Enum):
        Off = 0
        MotionBased = 1
        LengthIncrement = 2
    

    class Enable(enum.Enum):
        No = 0
        Yes = 1
    

    class DialogType(enum.Enum):
        Simulate = 0
        MachineToolBuilder = 1
        Synchronize = 2
        Inspection = 3
    

    class Accuracy(enum.Enum):
        Fine = 0
        Coarse = 1
    

class Sequence(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.Sequence.Types


    class Types(enum.Enum):
        InsideOut = 0
        OutsideIn = 1
        SteepLast = 2
        SteepFirst = 3
        InsideOutAlternate = 4
        OutsideInAlternate = 5
    

class SelectCAMFeatureList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAM.CAMFeature) -> bool:
        ...
    def Add(self, objects: typing.List[CAM.CAMFeature]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAM.CAMFeature, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAM.CAMFeature) -> bool:
        ...
    def Remove(self, object: CAM.CAMFeature, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAM.CAMFeature, view1: View, point1: Point3d, selection2: CAM.CAMFeature, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAM.CAMFeature]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAM.CAMFeature) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAM.CAMFeature]) -> None:
        ...
    def GetArray(self) -> typing.List[CAM.CAMFeature]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAM.CAMFeature, view1: View, point1: Point3d, selection2: CAM.CAMFeature, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAM.CAMFeature, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCAMFeature(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: CAM.CAMFeature, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: CAM.CAMFeature, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: CAM.CAMFeature, view1: View, point1: Point3d, selection2: CAM.CAMFeature, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: CAM.CAMFeature, view1: View, point1: Point3d, selection2: CAM.CAMFeature, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: CAM.CAMFeature, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> CAM.CAMFeature:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: CAM.CAMFeature


class RoundPointBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Decimals: CAM.RoundPointBuilder.Output
    Rounding: bool


    class Output(enum.Enum):
        NoRounding = 0
        Thousand = 1
        Hundred = 2
        Ten = 3
        One = 4
        Tenth = 5
        Hundredth = 6
        Thousandth = 7
        TenThousandth = 8
        HundredThousandth = 9
        Millionth = 10
        TenMillionth = 11
    

class RoughTurningBuilder(CAM.RoughFinishTurningBuilder):
    def __init__(self) -> None: ...
    Cleanup: CAM.RoughTurningBuilder.CleanupTypes
    CutStrategy: CAM.CutStrategy
    Direction: CAM.TurnDirection
    FirstPlunge: CAM.FirstPlunge
    LevelDepth: float
    LevelDepthMode: CAM.RoughTurningBuilder.LevelDepthModeTypes
    NonCuttingBuilder: CAM.NcmTurnRoughBuilder
    PartOffDepthMode: CAM.RoughTurningBuilder.PartOffDepthModeTypes
    PartOffDepthValue: float
    PartOffEvents: CAM.PostEventsCiBuilder
    PartOffPositionMode: CAM.RoughTurningBuilder.PartOffPositionModeTypes
    PartOffPositionPoint: Point
    ReversalMode: CAM.RoughTurningBuilder.ReversalModeTypes
    SafeDistance: float
    Stepover: CAM.StepoverBuilder


    class ReversalModeTypes(enum.Enum):
        AsLevel = 0
        Inverse = 1
        Closest = 2
        CutLater = 3
        Omit = 4
    

    class PartOffPositionModeTypes(enum.Enum):
        Automatic = 0
        Specify = 1
    

    class PartOffDepthModeTypes(enum.Enum):
        Divide = 0
        CleanFirstWall = 1
        CleanBothWalls = 2
        Stock = 3
        Distance = 4
    

    class LevelDepthModeTypes(enum.Enum):
        FromTool = 0
        Specify = 1
    

    class CleanupTypes(enum.Enum):
        None = 0
        All = 1
        SteepOnly = 2
        AllButSteep = 3
        LevelOnly = 4
        AllButLevel = 5
        DownOnly = 6
        PerReversal = 7
    

class RoughTurning(CAM.RoughFinishTurning):
    def __init__(self) -> None: ...


class RoughFinishTurningBuilder(CAM.TurningOperationBuilder):
    def __init__(self) -> None: ...
    AxialTrimPlane1: CAM.TrimPlane
    AxialTrimPlane2: CAM.TrimPlane
    CustomMemberData: CAM.RoughFinishTurningBuilder.CustomMemberDataTypes
    CustomMemberDataDistance: float
    CustomPartBoundary: CAM.Boundary
    CutParameters: CAM.TurnCutParameters
    CutRegions: CAM.RoughFinishTurningBuilder.CutRegionsTypes
    EndAngle: float
    EndOffset: float
    ExtendMode: CAM.RoughFinishTurningBuilder.ExtendModeTypes
    IgnoreMinimumBoringDiameter: bool
    LevelAngleBuilder: CAM.CutAngle
    MaximumAreaMode: CAM.RoughFinishTurningBuilder.MaximumAreaModes
    MaximumAreaSize: float
    MaximumAreaUnit: CAM.RoughFinishTurningBuilder.MinmaxAreaUnits
    MaximumSizeAxial: CAM.InheritableToolDepBuilder
    MaximumSizeMode: CAM.RoughFinishTurningBuilder.MinmaxSizeModes
    MaximumSizeRadial: CAM.InheritableToolDepBuilder
    MinimumArea: CAM.RoughFinishTurningBuilder.MinimumAreaTypes
    MinimumAreaSize: float
    MinimumAreaUnit: CAM.RoughFinishTurningBuilder.MinmaxAreaUnits
    MinimumSizeAxial: CAM.InheritableToolDepBuilder
    MinimumSizeMode: CAM.RoughFinishTurningBuilder.MinmaxSizeModes
    MinimumSizeRadial: CAM.InheritableToolDepBuilder
    MultiChannelTurningLeadDistance: float
    MultiChannelTurningMode: CAM.RoughFinishTurningBuilder.MultiChannelTurningModeTypes
    MultiChannelTurningSecondTool: CAM.Tool
    OmitReversals: bool
    RadialTrimPlane1: CAM.TrimPlane
    RadialTrimPlane2: CAM.TrimPlane
    RegionMachining: CAM.RoughFinishTurningBuilder.RegionMachiningTypes
    RegionSelection: CAM.RoughFinishTurningBuilder.RegionSelectionTypes
    RegionSelectionPoint: Point
    StartAngle: float
    StartOffset: float
    StepAngleBuilder: CAM.CutAngle
    ToleranceOffset: CAM.RoughFinishTurningBuilder.ToleranceOffsetTypes
    TrimPoint1: CAM.TrimPoint
    TrimPoint2: CAM.TrimPoint


    class ToleranceOffsetTypes(enum.Enum):
        AfterContainment = 0
        BeforeContainment = 1
    

    class RegionSelectionTypes(enum.Enum):
        Automatic = 0
        Manual = 1
    

    class RegionMachiningTypes(enum.Enum):
        Single = 0
        Multiple = 1
    

    class MultiChannelTurningModeTypes(enum.Enum):
        None = 0
        Balanced = 1
        Merged = 2
    

    class MinmaxSizeUnits(enum.Enum):
        Length = 0
        Percentage = 1
    

    class MinmaxSizeModes(enum.Enum):
        None = 0
        Axial = 1
        Radial = 2
        AxialAndRadial = 3
    

    class MinmaxAreaUnits(enum.Enum):
        Square = 0
        Percentage = 1
    

    class MinimumAreaTypes(enum.Enum):
        None = 0
        Specify = 1
        Partunit = 1
        Tool = 2
    

    class MaximumAreaModes(enum.Enum):
        None = 0
        Partunit = 1
        Tool = 2
    

    class ExtendModeTypes(enum.Enum):
        Specify = 0
        Tagential = 1
        Tangential = 1
    

    class CutRegionsTypes(enum.Enum):
        SingleRegion = 0
        SingleDirection = 1
        ReverseDirection = 2
        BiDirectional = 3
        Alternate = 4
    

    class CustomMemberDataTypes(enum.Enum):
        WithinRegion = 0
        WithinDistance = 1
    

class RoughFinishTurning(CAM.TurningOperation):
    def __init__(self) -> None: ...


class RotateToolMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Adjreg: int
    AdjregToggle: bool
    Angle: float
    Xoffset: float
    XoffsetToggle: bool
    Yoffset: float
    YoffsetToggle: bool
    Zoffset: float
    ZoffsetToggle: bool


class RotaryPolarMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    LockAxis: CAM.RotaryPolarMoveBuilder.LockAxisDirection
    LockPlane: CAM.RotaryPolarMoveBuilder.LockPlaneType
    LockPos: float
    OffsetData: CAM.OffsetDataBuilder
    Point: Point
    RoundPoint: CAM.RoundPointBuilder


    class LockPlaneType(enum.Enum):
        Xy = 0
        Yz = 1
        Zx = 2
    

    class LockAxisDirection(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

class RotaryPointMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    OffsetData: CAM.OffsetDataBuilder
    Point: Point
    PointBuilder: CAM.ReferencePoint
    RoundPoint: CAM.RoundPointBuilder
    ToolPositioning: CAM.ToolPositioningBuilder
    Vector: Direction
    VectorBuilder: CAM.ReferenceVector


class RotaryFinishGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    AxisOfRotation: CAM.RotaryFinishGeomBuilder.PartAxisOfRotationTypes
    PartAxisBuilder: CAM.PartAxisBuilder
    PartAxisPoint: Point
    PartAxisVector: SmartObject


    class PartAxisOfRotationTypes(enum.Enum):
        Zm = 0
        Specify = 1
        Xm = 2
        Ym = 3
    

class RobotPoseMove(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    def SetPose(self, poseNames: str, poseValues: float) -> None:
        ...
    def GetPoseNames(self) -> str:
        ...
    def GetPoseValues(self) -> float:
        ...


class RobotMountMove(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    ComponentName: str
    MountType: CAM.RobotMountMove.Types


    class Types(enum.Enum):
        NoChange = 0
        Mount = 1
        Unmount = 2
    

class RobotCartesianMove(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Configuration: int
    OffsetMatrix: Matrix3x3
    OffsetOrigin: Point3d
    Target: CartesianCoordinateSystem


class ReliefPlunge(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    Type: CAM.ReliefPlunge.Types
    Unit: CAM.ReliefPlunge.UnitTypes


    class UnitTypes(enum.Enum):
        Distance = 0
        Percent = 1
    

    class Types(enum.Enum):
        None = 0
        DistanceToWall = 1
    

class ReliefCut(TaggedObject):
    def __init__(self) -> None: ...
    Depth: float
    DepthUnit: CAM.ReliefCut.DepthUnits
    Distance: float
    DistanceUnit: CAM.ReliefCut.DistanceUnits
    Mode: CAM.ReliefCut.Modes
    Number: int


    class Modes(enum.Enum):
        None = 0
        Number = 1
        Depth = 2
        NumberAndDepth = 3
    

    class DistanceUnits(enum.Enum):
        Length = 0
        Percent = 1
    

    class DepthUnits(enum.Enum):
        Length = 0
        Percent = 1
    

class RegionMarker(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DelayTime: float
    MarkerLocation: CAM.RegionMarker.Location
    Time: float


    class Location(enum.Enum):
        Start = 0
        End = 1
    

class ReferenceVector(CAM.BaseBuilder):
    def __init__(self) -> None: ...
    def GetReferenceVectors(self, subop: CAM.ManualMove) -> None:
        ...
    Reference: str
    Vector: Direction


class ReferencePoint(CAM.BaseBuilder):
    def __init__(self) -> None: ...
    def GetReferencePoints(self, subop: CAM.ManualMove) -> None:
        ...
    Point: Point
    Reference: str


class RampingMode(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.RampingMode.Types


    class Types(enum.Enum):
        RampOutOnEveryOtherPass = 0
        RampInOnEveryOtherPass = 1
        RampOutFirst = 2
        RampInFirst = 3
    

class RadialGrooveMillingBuilder(CAM.CylindricalMillingBuilder):
    def __init__(self) -> None: ...
    LevelSequencing: CAM.GrooveMillingBuilder.LevelSequencingType
    OffsetFromStartDiameter: CAM.InheritableToolDepBuilder


class RadialGrooveMilling(CAM.Operation):
    def __init__(self) -> None: ...


class ProjVecCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetDpmProjType(self) -> CAM.ProjVecCiBuilder.DpmProjTypes:
        ...
    def SetDpmProjType(self, projType: CAM.ProjVecCiBuilder.DpmProjTypes) -> None:
        ...
    BackOffDistance: CAM.InheritableToolDepBuilder
    Point: Point
    Vector: Direction


    class DpmProjTypes(enum.Enum):
        ProjVecFixed = 0
        ProjVecToolAxis = 1
        ProjVecFromPoint = 2
        ProjVecToPoint = 3
        ProjVecFromLine = 4
        ProjVecToLine = 5
        ProjVecNormToDrive = 6
        ProjVecToDrive = 7
        ProjVecRuling = 8
        ProjVecUserDefined = 9
        ProjVecToolAxisUp = 10
        ProjVecTotal = 11
    

class ProgramOrderGroupBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...


class Program(CAM.NCGroup):
    def __init__(self) -> None: ...


class ProfileStrategy(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.ProfileStrategy.Types


    class Types(enum.Enum):
        DiametersOnly = 0
        FacesOnly = 1
        DiametersThenFaces = 2
        FacesThenDiameters = 3
        TowardsCorner = 4
        AwayFromCorner = 5
        DownOnly = 6
        FinishAll = 7
    

class ProbeTrackPoint(CAM.SolidTrackPoint):
    def __init__(self) -> None: ...


class ProbeTrackingBuilder(CAM.SolidTrackingBuilder):
    def __init__(self) -> None: ...
    Axis: NXObject
    StemTop: NXObject


class ProbeToolBuilder(CAM.SolidToolBuilder):
    def __init__(self) -> None: ...


class ProbeToleranceParametersBuilder(TaggedObject):
    def __init__(self) -> None: ...
    CylTolerance: float
    NullBandTolerance: float
    OutputCylTolerance: bool
    OutputNullBandTolerance: bool
    OutputTolerance: bool
    OutputUpperTolerance: bool
    Tolerance: float
    UpperTolerance: float


class ProbeStockParametersBuilder(TaggedObject):
    def __init__(self) -> None: ...
    StockAllowance: float


class ProbeProtectedParametersBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ApproachFlag: CAM.ProbeProtectedParametersBuilder.AppMethodTypes
    ClearanceDistance: float
    CollisionFlag: CAM.ProbeProtectedParametersBuilder.CollisionFlagTypes
    ReturnFlag: CAM.ProbeProtectedParametersBuilder.DepMethodTypes
    StandoffDistance: float


    class DepMethodTypes(enum.Enum):
        None = 0
        Clearance = 1
    

    class CollisionFlagTypes(enum.Enum):
        Alarm = 0
        Flag = 1
    

    class AppMethodTypes(enum.Enum):
        None = 0
        Clearance = 1
        Direct = 2
        RadialAxial = 3
        AxialRadial = 4
        RadialAxialWithClearance = 5
        AxialRadialWithClearance = 6
    

class ProbeParamsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ProbeControlParameters: CAM.ProbeControlParametersBuilder
    ProbeOutputControl: CAM.ProbeOutputControl
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    ProbeStockParameters: CAM.ProbeStockParametersBuilder
    ProbeToleranceParameters: CAM.ProbeToleranceParametersBuilder


class ProbeOutputControl(TaggedObject):
    def __init__(self) -> None: ...
    Output: CAM.ProbeOutputControl.OutputType


    class OutputType(enum.Enum):
        Center = 0
        Contact = 1
    

class ProbeInspectSurfacePointMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    DirectionType: CAM.ProbeInspectSurfacePointMoveBuilder.Direction
    MeasurementType: CAM.ProbeInspectSurfacePointMoveBuilder.Measurement
    Point: Point
    PointBuilder: CAM.ReferencePoint
    ProbeControlParameters: CAM.ProbeControlParametersBuilder
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    ProbeStockParameters: CAM.ProbeStockParametersBuilder
    ProbeToleranceParameters: CAM.ProbeToleranceParametersBuilder
    ToolAxisType: CAM.ProbeInspectSurfacePointMoveBuilder.ToolAxis
    Vector: NXObject


    class ToolAxis(enum.Enum):
        None = 0
        Normal = 1
        Automatic = 2
    

    class Measurement(enum.Enum):
        Axis2 = 0
        Axis3 = 1
    

    class Direction(enum.Enum):
        Normal = 0
        Vector = 7
    

class ProbeInspectPointMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    DirectionType: CAM.ProbeInspectPointMoveBuilder.Direction
    Point: Point
    PointBuilder: CAM.ReferencePoint
    ProbeControlParameters: CAM.ProbeControlParametersBuilder
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    ProbeStockParameters: CAM.ProbeStockParametersBuilder
    ProbeToleranceParameters: CAM.ProbeToleranceParametersBuilder


    class Direction(enum.Enum):
        Inferred = 0
        Xm = 1
        Negxm = 2
        Ym = 3
        Negym = 4
        Zm = 5
        Negzm = 6
    

class ProbeInspectBorebossMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Angle1: float
    Angle2: float
    Angle3: float
    AngleType: CAM.ProbeInspectBorebossMoveBuilder.Angle
    ArcVector: NXObject
    BossDimension: float
    BossDimensionBuilder: CAM.ExpressionDouble
    CycleType: CAM.ProbeInspectBorebossMoveBuilder.Cycle
    Cylinder: NXObject
    DepthType: CAM.ProbeInspectBorebossMoveBuilder.Depth
    Diameter: float
    DiameterBuilder: CAM.ExpressionDouble
    GeometryType: CAM.ProbeInspectBorebossMoveBuilder.Geometry
    MeasurementDepth: float
    MeasurementDepthBuilder: CAM.ExpressionDouble
    Point: Point
    PointBuilder: CAM.ReferencePoint
    ProbeControlParameters: CAM.ProbeControlParametersBuilder
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    ProbeStockParameters: CAM.ProbeStockParametersBuilder
    ProbeToleranceParameters: CAM.ProbeToleranceParametersBuilder


    class Geometry(enum.Enum):
        Cylinder = 0
        Point = 1
    

    class Depth(enum.Enum):
        Midpoint = 0
        Specify = 1
    

    class Cycle(enum.Enum):
        Bore = 0
        Boss = 1
    

    class Angle(enum.Enum):
        Predefined = 0
        Custom = 1
    

class ProbeControlParametersBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Adjustment: CAM.ProbeControlParametersBuilder.AdjustmentTypes
    Experience: int
    OutputExperience: bool
    OutputOvertravel: bool
    OutputPercentFeedback: bool
    OutputToolOffset: bool
    OutputWorkOffset: bool
    Overtravel: float
    PercentFeedback: float
    Print: CAM.ProbeControlParametersBuilder.PrintType
    ToolOffset: int
    WorkOffset: int


    class PrintType(enum.Enum):
        None = 0
        Feature = 1
        Component = 2
    

    class AdjustmentTypes(enum.Enum):
        None = 0
        Xy = 1
        Xyz = 2
        Contact = 3
    

class ProbeClearanceMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    ClearanceBuilder: CAM.NcmClearanceBuilder


class ProbeCalibrateStylusMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    ArcVector: NXObject
    CalibrationDepth: float
    CalibrationDepthBuilder: CAM.ExpressionDouble
    CalibrationType: CAM.ProbeCalibrateStylusMoveBuilder.CalibrateStylusType
    Cylinder: NXObject
    DepthType: CAM.ProbeCalibrateStylusMoveBuilder.Depth
    Diameter: float
    DiameterBuilder: CAM.ExpressionDouble
    GeometryType: CAM.ProbeCalibrateStylusMoveBuilder.Geometry
    OutputWorkOffset: bool
    Point: Point
    PointBuilder: CAM.ReferencePoint
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    WorkOffset: int


    class Geometry(enum.Enum):
        Cylinder = 0
        Point = 1
    

    class Depth(enum.Enum):
        Midpoint = 0
        Specify = 1
    

    class CalibrateStylusType(enum.Enum):
        Offsets = 0
        Radius = 1
        VectorRadius = 2
    

class ProbeCalibrateSphereMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Diameter: float
    DiameterBuilder: CAM.ExpressionDouble
    GeometryType: CAM.ProbeCalibrateSphereMoveBuilder.Geometry
    Point: Point
    PointBuilder: CAM.ReferencePoint
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    Sphere: NXObject
    ToolOffset: int


    class Geometry(enum.Enum):
        Sphere = 0
        Point = 1
    

class ProbeCalibrateLengthMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Point: Point
    PointBuilder: CAM.ReferencePoint
    ProbeProtectedParameters: CAM.ProbeProtectedParametersBuilder
    ToolOffset: int


class PreprocessGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    def Create(self, obj: NXObject, tolerance: float, vector: NXObject) -> None:
        ...
    def Delete(self, obj: NXObject) -> None:
        ...
    def GetParameter(self, obj: NXObject, tolerance: float, vector: NXObject) -> None:
        ...
    def SetParameter(self, obj: NXObject, tolerance: float, vector: NXObject) -> None:
        ...
    def GetObjects(self, solidBodies: typing.List[NXObject], facetBodies: typing.List[NXObject]) -> None:
        ...
    FixedVector: SmartObject
    TriangleTolerance: float


class Preferences(Builder):
    def __init__(self) -> None: ...
    def GetSelection(self, geomType: CAM.Preferences.GeometryTypes) -> CAM.Preferences.SelectionTypes:
        ...
    def SetSelection(self, geomType: CAM.Preferences.GeometryTypes, selection: CAM.Preferences.SelectionTypes) -> None:
        ...
    def GetDefaultIpwFolder(self) -> str:
        ...
    def GetDefaultConfigurationFile(self) -> str:
        ...
    def GetDefaultTemplateFile(self) -> str:
        ...
    AlwaysUpdateDialogs: bool
    AutomaticallySetMachingData: bool
    AuxiliaryFloorColor: NXColor
    AuxiliaryFloorColorSelection: CAM.Preferences.AuxiliaryFloorColorSelectionTypes
    BladeBlendColor: NXColor
    BladeColor: NXColor
    BlankColor: NXColor
    BlankSelection: CAM.Preferences.BlankSelectionTypes
    CheckColor: NXColor
    CheckSelection: CAM.Preferences.CheckSelectionTypes
    ClearanceColor: NXColor
    ClsfDecimals: int
    ClsfForceLoadTurret: bool
    ConfigurationFile: str
    CsysInformationListing: CAM.Preferences.CsysInformationListingTypes
    CsysOrientWcsToMcs: bool
    CutAreaColor: NXColor
    CutAreaSelection: CAM.Preferences.CutAreaSelectionTypes
    DisplaySelectedObjects: bool
    DisplayTurningIpw: bool
    DriveColor: NXColor
    EnableLevelBasedIpw: bool
    ForceRegenerate: bool
    GeneratePaths: bool
    GenerationFullRegeneration: bool
    GenerationPauseAfterEachPath: bool
    GenerationRefreshBeforeEachPath: bool
    GenerationSmartRegeneration: bool
    GenerationUpdateInstances: bool
    HubColor: NXColor
    IncludeInstances: bool
    IpwNeedleCountCoarse: int
    IpwNeedleCountFine: int
    IpwNeedleCountMedium: int
    IpwNeedleDistanceCoarse: float
    IpwNeedleDistanceFine: float
    IpwNeedleDistanceMedium: float
    IpwPartsFolder: str
    IpwToleranceMode: CAM.Preferences.IpwToleranceModeTypes
    IpwUseDirectoryOfOriginalPart: bool
    LinkMcsRcs: bool
    OptimizedCutLevelColor: NXColor
    PartColor: NXColor
    PartSelection: CAM.Preferences.PartSelectionTypes
    RelocateParameters: bool
    ReplayRefreshBeforeEachPath: bool
    RunProcessAssistant: bool
    SaveIpwModel: bool
    SaveLevelBasedIpw: bool
    ScrollAreaSize: int
    ShowPictures: bool
    ShroudColor: NXColor
    SplitterColor: NXColor
    StepoverDisplayAsNCM: bool
    SuspectBoundingBoxColor: NXColor
    TemplateFile: str
    TopOffLevelColor: NXColor
    TrimColor: NXColor
    UncutRegionColor: NXColor
    UnlinkInstances: bool
    Visualize2dTool1Color: NXColor
    Visualize2dTool2Color: NXColor
    Visualize2dTool3Color: NXColor
    Visualize2dTool4Color: NXColor
    Visualize2dTool5Color: NXColor
    VisualizeAnimationAccuracy: CAM.Preferences.AnimationAccuracyTypes
    VisualizeAutoBlockColor: NXColor
    VisualizeBackgroundColor: NXColor
    VisualizeChordalTolerance: float
    VisualizeCollisionsColor: NXColor
    VisualizeDynamicToolAxis: bool
    VisualizeExcessMaterialColor: NXColor
    VisualizeGougesColor: NXColor
    VisualizeIpwColor: NXColor
    VisualizeIpwDmrColor1: NXColor
    VisualizeIpwDmrColor10: NXColor
    VisualizeIpwDmrColor2: NXColor
    VisualizeIpwDmrColor3: NXColor
    VisualizeIpwDmrColor4: NXColor
    VisualizeIpwDmrColor5: NXColor
    VisualizeIpwDmrColor6: NXColor
    VisualizeIpwDmrColor7: NXColor
    VisualizeIpwDmrColor8: NXColor
    VisualizeIpwDmrColor9: NXColor
    VisualizeIpwDmrColoringMode: CAM.Preferences.IpwDmrColoringTypes
    VisualizeIpwTranslucency: int
    VisualizeSafeToolColor: NXColor
    VisualizeTemporaryContainmentCurveColor: NXColor
    VisualizeToolAxisTiltTolerance: float
    VisualizeToolDisplayColor: NXColor
    VisualizeToolEditAndDisplay: bool
    VisualizeToolHolderColor: NXColor
    VisualizeToolInsertOrFluteColor: NXColor
    VisualizeToolShankColor: NXColor
    VisualizeToolTranslucency: int
    WallColor: NXColor
    WallSelection: CAM.Preferences.WallSelectionTypes


    class WallSelectionTypes(enum.Enum):
        Bodies = 0
        Faces = 1
        SurfaceRegion = 2
    

    class SelectionTypes(enum.Enum):
        NoSelectionFilter = 0
        Curves = 1
        Edges = 2
        Faces = 3
        Feature = 4
        SolidBodies = 5
        SheetBodies = 6
        FacetBodies = 7
        Groups = 8
        SurfaceRegionFeatures = 9
    

    class PartSelectionTypes(enum.Enum):
        Bodies = 0
        Faces = 1
        Curves = 2
        SurfaceRegion = 3
        FacetedBodies = 4
    

    class IpwToleranceModeTypes(enum.Enum):
        NeedleDistance = 0
        NeedleCount = 1
    

    class IpwDmrColoringTypes(enum.Enum):
        Off = 0
        PerTool = 1
        PerOperation = 2
    

    class GeometryTypes(enum.Enum):
        Part = 0
        Blank = 1
        Check = 2
        CutArea = 3
        AuxiliaryFloor = 4
        Walls = 5
        SurfaceAreaDrive = 6
    

    class CutAreaSelectionTypes(enum.Enum):
        Bodies = 0
        Faces = 1
        SurfaceRegion = 2
    

    class CsysInformationListingTypes(enum.Enum):
        Wcs = 0
        Mcs = 1
    

    class CheckSelectionTypes(enum.Enum):
        Bodies = 0
        Faces = 1
        Curves = 2
    

    class BlankSelectionTypes(enum.Enum):
        Bodies = 0
        Faces = 1
        Curves = 2
        SurfaceRegion = 3
        FacetedBodies = 4
    

    class AuxiliaryFloorColorSelectionTypes(enum.Enum):
        Bodies = 0
        Faces = 1
        SurfaceRegion = 2
    

    class AnimationAccuracyTypes(enum.Enum):
        Fine = 0
        Coarse = 1
    

class PostEventsCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    PostEvent: bool
    UdeSet: CAM.UdeSet


class PointToPointBuilder(CAM.MillOperationBuilder):
    def __init__(self) -> None: ...
    BottomSurface: CAM.DrillSurfaceBuilder
    TopSurface: CAM.DrillSurfaceBuilder


    class TlaxisTypes(enum.Enum):
        None = 0
        Fixed = 1
        NormalToPart = 2
    

    class ProjectVectorTypes(enum.Enum):
        None = 0
        SpecifyVetor = 1
        ToolAxis = 2
    

    class MaterialSideTypes(enum.Enum):
        None = 0
        SpecifyVetor = 1
        ToolAxis = 2
    

    class CycleTypes(enum.Enum):
        NoCycle = 0
        PeckDrill = 1
        BreakChip = 2
        StandardText = 3
        StandardDrill = 4
        StandardDrillCsink = 5
        StandardDrillDeep = 6
        StandardDrillBreakChip = 7
        StandardTap = 8
        StandardBore = 9
        StandardBoreDrag = 10
        StandardBoreNoDrag = 11
        StandardBoreBack = 12
        StandardBoreManual = 13
    

class PmopToolAxisCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    FixedVector: SmartObject
    ToolAxis: CAM.PmopToolAxisCiBuilder.ToolAxisTypes


    class ToolAxisTypes(enum.Enum):
        None = 0
        Vector = 1
        NormalToPart = 2
        NormalToFirstFace = 3
    

class PlungeMillingBuilder(CAM.PlanarOperationBuilder):
    def __init__(self) -> None: ...
    BlankGeometry: CAM.Geometry
    CutLevel: CAM.CutLevel
    MaxCutWidth: CAM.InheritableToolDepBuilder
    MinClearance: CAM.InheritableDoubleBuilder
    RetractAngle: CAM.InheritableDoubleBuilder
    StepAhead: CAM.InheritableToolDepBuilder
    StepUp: CAM.StepUpBuilder
    TransferMethod: CAM.PlungeMillingBuilder.TransferMethodTypes
    TrimBoundary: CAM.Boundary
    VerticalClearance: CAM.InheritableDoubleBuilder


    class TransferMethodTypes(enum.Enum):
        ClearancePlane = 0
        AutomaticPlane = 1
    

class PlungeMilling(CAM.PlanarOperation):
    def __init__(self) -> None: ...


class PlanarOperationBuilder(CAM.MillOperationBuilder):
    def __init__(self) -> None: ...
    AdditionalPasses: int
    AutomaticPartBoundaryMethod: CAM.PlanarOperationBuilder.AutomaticPartBoundaryMethodTypes
    AvoidanceMethods: CAM.AvoidanceMethodsBuilder
    BndStepover: CAM.StepoverBuilder
    CheckGeometry: CAM.Geometry
    CornerLoops: bool
    CutAreaGeometry: CAM.Geometry
    CutPattern: CAM.CutPatternBuilder
    DeferCuttingStatus: bool
    DepthPerCut: CAM.InheritableDoubleBuilder
    IslandCleanup: bool
    NonCuttingBuilder: CAM.NcmPlanarBuilder
    PartGeometry: CAM.Geometry
    ToolAxisFix: CAM.ToolAxisFixed
    ToolMinimumLengthUsage: bool


    class AutomaticPartBoundaryMethodTypes(enum.Enum):
        FollowWallBottom = 0
        FollowWallTop = 1
    

class PlanarOperation(CAM.MillOperation):
    def __init__(self) -> None: ...


class PlanarMillingBuilder(CAM.PlanarOperationBuilder):
    def __init__(self) -> None: ...
    def SetDrivePointSpecified(self, drivePointSpecified: bool) -> None:
        ...
    BlankBoundary: CAM.BoundaryPlanarMill
    CheckBoundary: CAM.BoundaryPlanarMill
    CutLevel: CAM.CutLevelPlanar
    DrivePoint: int
    MultiplePasses: CAM.MultiplePassesBuilder
    PartBoundary: CAM.BoundaryPlanarMill
    Save2dIpw: bool
    TrimBoundary: CAM.BoundaryPlanarMill
    WallGeometry: CAM.Geometry
    ZdepthOffset: float


class PlanarMilling(CAM.PlanarOperation):
    def __init__(self) -> None: ...


class PitchSetting(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    End: float
    Increment: float
    Option: CAM.PitchSetting.OptionTypes
    OutputUnit: CAM.PitchSetting.OutputUnitTypes
    Start: float
    ThreadPerUnit: float
    Variance: CAM.PitchSetting.VarianceTypes


    class VarianceTypes(enum.Enum):
        Constant = 0
        StartAndEnd = 1
        StartAndIncrement = 2
    

    class OutputUnitTypes(enum.Enum):
        SameAsInput = 0
        Pitch = 1
        Lead = 2
        ThreadsPerUnit = 3
    

    class OptionTypes(enum.Enum):
        Pitch = 0
        Lead = 1
        ThreadsPerUnit = 2
    

class PatternTypeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    PatternType: CAM.PatternTypeBuilder.Option


    class Option(enum.Enum):
        None = 0
        Offset = 1
        Morph = 2
        OffsetAroundShortGuide = 3
    

class PatternMarker(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    MarkerLocation: CAM.PatternMarker.Location
    PassNumber: int
    PassShapeType: CAM.PatternMarker.ShapeType
    PatternType: CAM.PatternMarker.Type


    class Type(enum.Enum):
        Undefined = 0
        Finish = 1
        SpringPass = 2
        Infill = 3
    

    class ShapeType(enum.Enum):
        Undefined = 0
        Outer = 1
        Inner = 2
    

    class Location(enum.Enum):
        Start = 0
        End = 1
    

class PathMarker(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    MarkerType: CAM.PathMarker.Type
    PatternMarker: CAM.PatternMarker
    RegionMarker: CAM.RegionMarker


    class Type(enum.Enum):
        System = 0
        Pattern = 1
        Region = 2
    

class PathLinearMotion(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFeedrate(self, feedValue: float, feedUnit: CAM.CamPathFeedUnitType) -> None:
        ...
    def SetFeedrate(self, feedValue: float, feedUnit: CAM.CamPathFeedUnitType) -> None:
        ...
    ContactData: CAM.PathContactMotion
    EndPoint: Point3d
    IsContact: bool
    IsCustomFeedrate: bool
    MotionType: CAM.CamPathMotionType
    ToolAxis: Vector3d


class PathLevelMarker(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    LevelDepth: float
    LevelNormal: Vector3d
    LevelNumber: int
    OperationName: str


class PathLaserProcessorData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetResolution(self) -> int:
        ...
    def GetPowerRoundingValue(self) -> float:
        ...


class PathLaserPowderData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetMaterial(self) -> str:
        ...


class PathLaserOptimizationData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetVersionNumber(self) -> int:
        ...
    def GetIsValid(self) -> bool:
        ...
    def GetLaserGeometryData(self) -> CAM.PathLaserGeometryData:
        ...
    def GetLaserDepositionData(self) -> CAM.PathLaserDepositionData:
        ...
    def GetLaserPowderData(self) -> CAM.PathLaserPowderData:
        ...
    def GetLaserMachineData(self) -> CAM.PathLaserMachineData:
        ...
    def GetLaserProcessorData(self) -> CAM.PathLaserProcessorData:
        ...


class PathLaserMachineData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetMaxLaserPower(self) -> float:
        ...


class PathLaserGeometryData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetInProcessBodies(self) -> typing.List[TaggedObject]:
        ...
    def GetAmFeatureBody(self) -> TaggedObject:
        ...
    def GetNumberOfInProcessBodies(self) -> int:
        ...


class PathLaserDepositionData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetLayerThickness(self) -> float:
        ...
    def GetLaserWidth(self) -> float:
        ...


class PathHelixMotion(CAM.PathCircularMotion):
    def __init__(self, ptr: int) -> None: ...
    NumberOfRevolutions: float


class PathEvent(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNext(self) -> CAM.PathEvent:
        ...
    def GetPrevious(self) -> CAM.PathEvent:
        ...


class PathDisplayColors(TaggedObject):
    def __init__(self) -> None: ...
    def SetAllCommonColor(self) -> None:
        ...
    Approach: NXColor
    Common: NXColor
    Crossover: NXColor
    Cut: NXColor
    Departure: NXColor
    Engage: NXColor
    FirstCut: NXColor
    LastCut: NXColor
    Rapid: NXColor
    Retract: NXColor
    ReturnColor: NXColor
    SideCut: NXColor
    Stepover: NXColor
    Traversal: NXColor


class PathDisplay(Utilities.NXRemotableObject):
    def __init__(self, owner: CAM.CAMSession) -> None: ...
    def ShowToolPath(self, opr: CAM.CAMObject) -> None:
        ...
    def HideToolPath(self, opr: CAM.CAMObject) -> None:
        ...
    def Play(self, isFwd: bool) -> None:
        ...
    def Step(self, isFwd: bool) -> None:
        ...
    def StepDisplay(self, isFwd: bool) -> None:
        ...
    def SetAnimationSpeed(self, speed: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    ColorBy: CAM.PathDisplay.ColorByType
    ShowCutting: bool
    ShowEndpoints: bool
    ShowNoncutting: bool
    ShowToolCenter: bool


    class ColorByType(enum.Enum):
        MotionType = 0
        Operation = 1
        Tool = 2
        MotionLength = 3
        MotionGeometry = 4
        Finding = 5
    

class PathContactMotion(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    ArcAxis: Vector3d
    ArcCenter: Point3d
    ArcDirection: CAM.CamPathDir
    ArcRadius: float
    MotionShape: CAM.CamPathContactMotionShapeType
    Point: Point3d


class PathCircularMotion(CAM.PathLinearMotion):
    def __init__(self, ptr: int) -> None: ...
    ArcAxis: Vector3d
    ArcCenter: Point3d
    ArcRadius: float
    Direction: CAM.CamPathDir


class Path(TaggedObject):
    def __init__(self) -> None: ...
    def NewPathLinearMotion(self) -> CAM.PathLinearMotion:
        ...
    def NewPathCircularMotion(self) -> CAM.PathCircularMotion:
        ...
    def NewPathHelixMotion(self) -> CAM.PathHelixMotion:
        ...
    def GetToolpathEvent(self, eventNumber: int) -> CAM.PathEvent:
        ...
    def GetToolpathEventType(self, eventNumber: int) -> CAM.CamPathToolpathEventType:
        ...
    def GetToolpathEventType(self, pathEvent: CAM.PathEvent) -> CAM.CamPathToolpathEventType:
        ...
    def MoveEvent(self, fromIndex: int, toIndex: int) -> None:
        ...
    def MoveEvent(self, eventToMove: CAM.PathEvent, location: CAM.CamPathToolpathEventLocation, referenceEvent: CAM.PathEvent) -> None:
        ...
    def IsToolpathEventAMotion(self, eventNumber: int, motionType: CAM.CamPathMotionType, motionShape: CAM.CamPathMotionShapeType) -> bool:
        ...
    def IsToolpathEventAMotion(self, eventOfInterest: CAM.PathEvent, motionType: CAM.CamPathMotionType, motionShape: CAM.CamPathMotionShapeType) -> bool:
        ...
    def IsToolpathEventUde(self, eventOfInterest: CAM.PathEvent, udeName: str) -> bool:
        ...
    def GetLinearMotion(self, index: int) -> CAM.PathLinearMotion:
        ...
    def SetLinearMotion(self, index: int, data: CAM.PathLinearMotion) -> None:
        ...
    def AppendLinearMotion(self, data: CAM.PathLinearMotion) -> None:
        ...
    def InsertLinearMotionBefore(self, data: CAM.PathLinearMotion, index: int) -> None:
        ...
    def InsertLinearMotionAfter(self, data: CAM.PathLinearMotion, index: int) -> None:
        ...
    def GetLinearMotion(self, eventOfInterest: CAM.PathEvent) -> CAM.PathLinearMotion:
        ...
    def SetLinearMotion(self, eventOfInterest: CAM.PathEvent, data: CAM.PathLinearMotion) -> None:
        ...
    def AddLinearMotion(self, data: CAM.PathLinearMotion, location: CAM.CamPathToolpathEventLocation, referenceEvent: CAM.PathEvent) -> CAM.PathEvent:
        ...
    def GetCircularMotion(self, index: int) -> CAM.PathCircularMotion:
        ...
    def SetCircularMotion(self, index: int, data: CAM.PathCircularMotion) -> None:
        ...
    def AppendCircularMotion(self, data: CAM.PathCircularMotion) -> None:
        ...
    def InsertCircularMotionBefore(self, data: CAM.PathCircularMotion, index: int) -> None:
        ...
    def InsertCircularMotionAfter(self, data: CAM.PathCircularMotion, index: int) -> None:
        ...
    def GetCircularMotion(self, eventOfInterest: CAM.PathEvent) -> CAM.PathCircularMotion:
        ...
    def SetCircularMotion(self, eventOfInterest: CAM.PathEvent, data: CAM.PathCircularMotion) -> None:
        ...
    def AddCircularMotion(self, data: CAM.PathCircularMotion, location: CAM.CamPathToolpathEventLocation, referenceEvent: CAM.PathEvent) -> CAM.PathEvent:
        ...
    def GetHelixMotion(self, index: int) -> CAM.PathHelixMotion:
        ...
    def SetHelixMotion(self, index: int, data: CAM.PathHelixMotion) -> None:
        ...
    def AppendHelixMotion(self, data: CAM.PathHelixMotion) -> None:
        ...
    def InsertHelixMotionBefore(self, data: CAM.PathHelixMotion, index: int) -> None:
        ...
    def InsertHelixMotionAfter(self, data: CAM.PathHelixMotion, index: int) -> None:
        ...
    def GetHelixMotion(self, eventOfInterest: CAM.PathEvent) -> CAM.PathHelixMotion:
        ...
    def SetHelixMotion(self, eventOfInterest: CAM.PathEvent, data: CAM.PathHelixMotion) -> None:
        ...
    def AddHelixMotion(self, data: CAM.PathHelixMotion, location: CAM.CamPathToolpathEventLocation, referenceEvent: CAM.PathEvent) -> CAM.PathEvent:
        ...
    def GetUde(self, index: int) -> CAM.Ude:
        ...
    def SetUde(self, index: int, data: CAM.Ude) -> None:
        ...
    def AppendUde(self, udeName: str) -> None:
        ...
    def InsertUdeBefore(self, udeName: str, index: int) -> None:
        ...
    def InsertUdeAfter(self, udeName: str, index: int) -> None:
        ...
    def GetUde(self, eventOfInterest: CAM.PathEvent) -> CAM.Ude:
        ...
    def SetUde(self, eventOfInterest: CAM.PathEvent, data: CAM.Ude) -> None:
        ...
    def AddUde(self, udeName: str, location: CAM.CamPathToolpathEventLocation, referenceEvent: CAM.PathEvent) -> CAM.PathEvent:
        ...
    def EmptyPath(self) -> None:
        ...
    def DeleteOneEvent(self, index: int) -> None:
        ...
    def DeleteOneEvent(self, pathEvent: CAM.PathEvent) -> None:
        ...
    def GetLaserOptimizationData(self) -> CAM.PathLaserOptimizationData:
        ...
    def GetLevelMarker(self, index: int) -> CAM.PathLevelMarker:
        ...
    def SetLevelMarker(self, index: int, data: CAM.PathLevelMarker) -> None:
        ...
    def AppendLevelMarker(self, data: CAM.PathLevelMarker) -> None:
        ...
    def InsertLevelMarkerBefore(self, data: CAM.PathLevelMarker, index: int) -> None:
        ...
    def InsertLevelMarkerAfter(self, data: CAM.PathLevelMarker, index: int) -> None:
        ...
    def GetLevelMarker(self, eventOfInterest: CAM.PathEvent) -> CAM.PathLevelMarker:
        ...
    def SetLevelMarker(self, eventOfInterest: CAM.PathEvent, data: CAM.PathLevelMarker) -> None:
        ...
    def AddLevelMarker(self, data: CAM.PathLevelMarker, location: CAM.CamPathToolpathEventLocation, referenceEvent: CAM.PathEvent) -> CAM.PathEvent:
        ...
    def GetFirstEvent(self) -> CAM.PathEvent:
        ...
    def GetLastEvent(self) -> CAM.PathEvent:
        ...
    def DeleteAllUdesOfName(self, udeName: str) -> None:
        ...
    def NewPathMarker(self, markerType: CAM.PathMarker.Type) -> CAM.PathMarker:
        ...
    def GetMarker(self, index: int) -> CAM.PathMarker:
        ...
    def SetMarker(self, index: int, data: CAM.PathMarker) -> None:
        ...
    def AppendMarker(self, data: CAM.PathMarker) -> None:
        ...
    def InsertMarkerBefore(self, data: CAM.PathMarker, index: int) -> None:
        ...
    def InsertMarkerAfter(self, data: CAM.PathMarker, index: int) -> None:
        ...
    def GetMarker(self, eventOfInterest: CAM.PathEvent) -> CAM.PathMarker:
        ...
    def SetMarker(self, eventOfInterest: CAM.PathEvent, data: CAM.PathMarker) -> None:
        ...
    def AddMarker(self, data: CAM.PathMarker, location: CAM.CamPathToolpathEventLocation, referenceEvent: CAM.PathEvent) -> CAM.PathEvent:
        ...
    ContactType: CAM.CamPathContactType
    NumberOfToolpathEvents: int
    ToolAxisType: CAM.CamPathToolAxisType


class PartAxisBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AxisOfRotation: CAM.PartAxisBuilder.PartAxisOfRotationTypes
    PartAxisPoint: Point
    PartAxisVector: SmartObject


    class PartAxisOfRotationTypes(enum.Enum):
        Xm = 0
        Ym = 1
        Zm = 2
        Specify = 3
    

class ParamValueIntent(enum.Enum):
    PartUnits = 0
    ToolDep = 1
    Function = 2


class ParamBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCustomizableItemBuilder(self, name: str) -> TaggedObject:
        ...
    def GetCustomizableItemNames(self) -> str:
        ...
    CycleEvent: CAM.Ude
    CycleTable: CAM.Cycle
    OptimizationMethod: CAM.ParamBuilder.OptimizationTypes


    class OptimizationTypes(enum.Enum):
        None = 0
        MinimizeTravel = 1
        Band = 2
    

class OutputUncutRegions(TaggedObject):
    def __init__(self) -> None: ...
    AutoSaveBoundary: bool
    OverlapDistance: float


class OrientGeometry(CAM.NCGroup):
    def __init__(self) -> None: ...


class OrientGeomBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def GetCsysPurposeMode(self) -> CAM.OrientGeomBuilder.CsysPurposeModes:
        ...
    def SetCsysPurposeMode(self, csysPurposeMode: CAM.OrientGeomBuilder.CsysPurposeModes) -> None:
        ...
    def GetSpecialOutputMode(self) -> CAM.OrientGeomBuilder.SpecialOutputModes:
        ...
    def SetSpecialOutputMode(self, specialOutputMode: CAM.OrientGeomBuilder.SpecialOutputModes) -> None:
        ...
    def GetToolAxisMode(self) -> CAM.OrientGeomBuilder.ToolAxisModes:
        ...
    def SetToolAxisMode(self, toolAxisMode: CAM.OrientGeomBuilder.ToolAxisModes) -> None:
        ...
    FixtureOffsetBuilder: CAM.InheritableIntBuilder
    LayoutCiBuilder: CAM.LayoutCiBuilder
    LinkRcsToMcs: bool
    Mcs: CartesianCoordinateSystem
    Rcs: CartesianCoordinateSystem
    ToolAxisVector: NXObject


    class ToolAxisModes(enum.Enum):
        PositiveZOfMcs = 0
        FixedAxis = 1
        AllAxes = 2
    

    class SpecialOutputModes(enum.Enum):
        None = 0
        UseMainMcs = 1
        FixtureOffset = 2
        CsysRotation = 3
    

    class CsysPurposeModes(enum.Enum):
        Local = 0
        Main = 1
    

class OptimizeTraverseGroupBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    CutParameters: CAM.CutParameters
    FeatureGeometry: CAM.OptimizeFeatureGeometry
    NonCuttingBuilder: CAM.NcmOptimizeGroup


class OptimizeFeatureGeometry(CAM.FBM.FeatureGeometry):
    def __init__(self) -> None: ...
    def ReloadListFromOperations(self) -> None:
        ...


class OppositeDirection(TaggedObject):
    def __init__(self) -> None: ...
    Value: bool


class OperationTransformBuilder(Builder):
    def __init__(self) -> None: ...
    def RemoveTransformation(self) -> None:
        ...
    AngleEndPoint: Point
    AngleMethod: CAM.OperationTransformBuilder.Angle
    AnglePivotPoint: Point
    AngleStartPoint: Point
    AngleValue: float
    ArrayAngle: float
    ArrayCircularIncrementAngle: float
    ArrayCircularNumber: int
    ArrayCircularRadius: float
    ArrayCircularStartAngle: float
    ArrayNumberAlongXc: int
    ArrayNumberAlongYc: int
    ArrayOffsetXc: float
    ArrayOffsetYc: float
    ArrayOriginPoint: Point
    DeltaXc: float
    DeltaYc: float
    DeltaZc: float
    DistanceAngleDivision: int
    LineEndPoint: Point
    LineMethod: CAM.OperationTransformBuilder.Line
    LinePoint: Point
    LineSelection: SelectLine
    LineStartPoint: Point
    LineVector: Direction
    MotionType: CAM.OperationTransformBuilder.Motion
    MoveCopyInstance: CAM.OperationTransformBuilder.Result
    NumOfCopyInstance: int
    Plane: Plane
    ReferencePoint: Point
    RepositionFromCsys: CoordinateSystem
    RepositionToCsys: CoordinateSystem
    ScaleFactor: float
    ToPoint: Point
    TransformType: CAM.OperationTransformBuilder.Transform


    class Transform(enum.Enum):
        Translate = 0
        Scale = 1
        RotateAboutPoint = 2
        RotateAboutLine = 3
        MirrorThroughALine = 4
        MirrorThroughAPlane = 5
        CircularArray = 6
        RectangularArray = 7
        Reposition = 8
    

    class Result(enum.Enum):
        Move = 0
        Copy = 1
        Instance = 2
    

    class Motion(enum.Enum):
        Delta = 0
        ToAPoint = 1
    

    class Line(enum.Enum):
        Specify = 0
        TwoPoint = 1
        PointAndVector = 2
    

    class Angle(enum.Enum):
        Specify = 0
        TwoPoint = 1
    

class OperationTeaching(Builder):
    def __init__(self) -> None: ...
    def GetLibraryPath(self) -> str:
        ...
    def SetLibraryPath(self, path: str) -> None:
        ...
    def GetFeature(self) -> CAM.CAMFeature:
        ...
    def SetFeature(self, feature: CAM.CAMFeature) -> None:
        ...
    def GetOperations(self) -> typing.List[CAM.Operation]:
        ...
    def SetOperations(self, aOperations: typing.List[CAM.Operation]) -> None:
        ...
    def Teach(self) -> str:
        ...


class OperationSetTeaching(CAM.Teaching):
    def __init__(self) -> None: ...
    def GetFeatureGroupPriority(self, name: str) -> float:
        ...
    def SetFeatureGroupPriority(self, name: str, priority: float) -> None:
        ...
    def GetFeatureGroupCondition(self, name: str) -> str:
        ...
    def SetFeatureGroupCondition(self, name: str, condition: str) -> None:
        ...
    def GetOperationCondition(self, name: str) -> str:
        ...
    def SetOperationCondition(self, name: str, condition: str) -> None:
        ...
    def GetOperationAddonCondition(self, name: str, operationName: str) -> str:
        ...
    def SetOperationAddonCondition(self, name: str, operationName: str, condition: str) -> None:
        ...
    def GetFeatureGroups(self) -> typing.List[CAM.FeatureGeometry]:
        ...
    def SetFeatureGroups(self, aFeatureGroups: typing.List[CAM.FeatureGeometry]) -> None:
        ...
    def Teach(self) -> None:
        ...


class OperationDisplayOptionsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ArrowDisplayFlag: bool
    DisplayCutRegionsFlag: bool
    FeedDisplayFlag: bool
    LineNumberDisplayFlag: bool
    PaintDisplay: CAM.DisplayPaint
    PathDisplay: CAM.DisplayPath
    PathDisplayColors: CAM.PathDisplayColors
    PathDisplayType: CAM.OperationDisplayOptionsBuilder.PathDisplayTypes
    PathNormalType: CAM.OperationDisplayOptionsBuilder.PathNormalTypes
    PathVector: Direction
    PatternDisplayFrequency: int
    PatternDisplayType: CAM.OperationDisplayOptionsBuilder.PatternDisplayTypes
    PatternFile: str
    PatternXOffset: float
    PatternYOffset: float
    PatternZOffset: float
    PauseAfterDisplayFlag: bool
    PercentOfTool: float
    RefreshBeforeDisplayFlag: bool
    ReplaySpeed: int
    SaveContactDisplayDataFlag: bool
    SilhouDisplay: CAM.DisplaySilhouette
    SuppressPathDisplayFlag: bool
    ToolDisplay: CAM.DisplayTool
    ToolDisplayFrequency: int
    ToolDisplayType: CAM.OperationDisplayOptionsBuilder.ToolDisplayTypes


    class ToolDisplayTypes(enum.Enum):
        None = 0
        Tool2d = 1
        Tool3d = 2
        Axis = 3
    

    class PatternDisplayTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class PathNormalTypes(enum.Enum):
        TypesToolAxis = 0
        TypesSpecify = 1
    

    class PathDisplayTypes(enum.Enum):
        SolidCenter = 0
        DashedCenter = 1
        Silhouette = 2
        Fill = 3
        SilhouetteFill = 4
    

class OperationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.Operation]:
        ...
    def __init__(self, owner: CAM.CAMSetup) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.Operation:
        ...
    def Create(self, parentProgramGroup: CAM.NCGroup, parentMethodGroup: CAM.NCGroup, parentToolGroup: CAM.NCGroup, parentGeometryGroup: CAM.NCGroup, typeName: str, subtypeName: str, useDefaultName: CAM.OperationCollection.UseDefaultName, newOperationName: str) -> CAM.Operation:
        ...
    def CreateSurfaceContourBuilder(self, param: CAM.CAMObject) -> CAM.SurfaceContourBuilder:
        ...
    def CreateFaceMillingBuilder(self, param: CAM.CAMObject) -> CAM.FaceMillingBuilder:
        ...
    def CreateCavityMillingBuilder(self, param: CAM.CAMObject) -> CAM.CavityMillingBuilder:
        ...
    def CreatePlanarMillingBuilder(self, param: CAM.CAMObject) -> CAM.PlanarMillingBuilder:
        ...
    def CreateEngravingBuilder(self, param: CAM.CAMObject) -> CAM.EngravingBuilder:
        ...
    def CreateZlevelMillingBuilder(self, param: CAM.CAMObject) -> CAM.ZLevelMillingBuilder:
        ...
    def CreateFeatureMillingBuilder(self, param: CAM.CAMObject) -> CAM.FeatureMillingBuilder:
        ...
    def CreatePlungeMillingBuilder(self, param: CAM.CAMObject) -> CAM.PlungeMillingBuilder:
        ...
    def CreateHoleMakingBuilder(self, param: CAM.CAMObject) -> CAM.HoleMakingBuilder:
        ...
    def CreateLatheUserDefinedBuilder(self, param: CAM.CAMObject) -> CAM.LatheUserDefinedBuilder:
        ...
    def CreateMillUserDefinedBuilder(self, param: CAM.CAMObject) -> CAM.MillUserDefinedBuilder:
        ...
    def CreateWedmUserDefinedBuilder(self, param: CAM.CAMObject) -> CAM.WedmUserDefinedBuilder:
        ...
    def CreateWedmMachineControlBuilder(self, param: CAM.CAMObject) -> CAM.WedmMachineControlBuilder:
        ...
    def CreateLatheMachineControlBuilder(self, param: CAM.CAMObject) -> CAM.LatheMachineControlBuilder:
        ...
    def CreateMillMachineControlBuilder(self, param: CAM.CAMObject) -> CAM.MillMachineControlBuilder:
        ...
    def CreateGmcopBuilder(self, param: CAM.CAMObject) -> CAM.GmcOpBuilder:
        ...
    def CreatePointToPointBuilder(self, param: CAM.CAMObject) -> CAM.PointToPointBuilder:
        ...
    def CreateDpmitpBuilder(self, param: CAM.CAMObject) -> CAM.DPMItpBuilder:
        ...
    def CreateVazlMillingBuilder(self, param: CAM.CAMObject) -> CAM.VazlMillingBuilder:
        ...
    def CreateRoughTurningBuilder(self, param: CAM.CAMObject) -> CAM.RoughTurningBuilder:
        ...
    def CreateFinishTurningBuilder(self, param: CAM.CAMObject) -> CAM.FinishTurningBuilder:
        ...
    def CreateThreadTurningBuilder(self, param: CAM.CAMObject) -> CAM.ThreadTurningBuilder:
        ...
    def CreateCenterlineDrillTurningBuilder(self, param: CAM.CAMObject) -> CAM.CenterlineDrillTurningBuilder:
        ...
    def CreateWedmOperationBuilder(self, param: CAM.CAMObject) -> CAM.WedmOperationBuilder:
        ...
    def CreateTeachmodeTurningBuilder(self, param: CAM.CAMObject) -> CAM.TeachmodeTurningBuilder:
        ...
    def CreateThreadMillingBuilder(self, param: CAM.CAMObject) -> CAM.ThreadMillingBuilder:
        ...
    def CreateCylinderMillingBuilder(self, param: CAM.CAMObject) -> CAM.CylinderMillingBuilder:
        ...
    def CreateVolumeBased25dMillingOperationBuilder(self, param: CAM.CAMObject) -> CAM.VolumeBased25DMillingOperationBuilder:
        ...
    def CreateMillToolProbingBuilder(self, param: CAM.CAMObject) -> CAM.MillToolProbingBuilder:
        ...
    def CreateTurnToolProbingBuilder(self, param: CAM.CAMObject) -> CAM.TurnToolProbingBuilder:
        ...
    def CreateTurnPartProbingBuilder(self, param: CAM.CAMObject) -> CAM.TurnPartProbingBuilder:
        ...
    def CreateHoleDrillingBuilder(self, param: CAM.CAMObject) -> CAM.HoleDrillingBuilder:
        ...
    def CreateGrooveMillingBuilder(self, param: CAM.CAMObject) -> CAM.GrooveMillingBuilder:
        ...
    def CreateLaserTeachMode(self, param: CAM.CAMObject) -> CAM.LaserTeachMode:
        ...
    def CreateChamferMillingBuilder(self, param: CAM.CAMObject) -> CAM.ChamferMillingBuilder:
        ...
    def CreateRadialGrooveMillingBuilder(self, param: CAM.CAMObject) -> CAM.RadialGrooveMillingBuilder:
        ...
    def CreateDocumentationBuilder(self, param: CAM.CAMObject) -> CAM.DocumentationBuilder:
        ...
    def CreateManualControlBuilder(self, param: CAM.CAMObject) -> CAM.ManualControlBuilder:
        ...
    def CreateGenericFeatureOperationBuilder(self, param: CAM.CAMObject) -> CAM.GenericFeatureOperationBuilder:
        ...
    def Tag(self) -> Tag: ...



    class UseDefaultName(enum.Enum):
        False = 0
        True = 1
    

class OperationBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...
    def GetHoleAxisValues(self) -> float:
        ...
    def SetHoleAxisValues(self, holeAxis: float) -> None:
        ...
    ChannelName: str
    Description: str
    EndOfPath: CAM.PostEventsCiBuilder
    EndUdeSet: CAM.UdeSet
    Geometry: CAM.GeometryCiBuilder
    GougeChecking: bool
    HoleAxisType: CAM.OperationBuilder.HoleAxisTypes
    HoleDepth: CAM.InheritableDoubleBuilder
    HoleDepthType: CAM.OperationBuilder.HoleDepthTypes
    LayoutAndLayer: CAM.LayoutCiBuilder
    MotionOutputBuilder: CAM.ArcOutputTypeCiBuilder
    Notes: CAM.Notes
    OptimizationBasedOn: CAM.OperationBuilder.OptimizationBasedOnTypes
    OptimizationDistanceMethod: CAM.OperationBuilder.OptimizationDistanceTypes
    OptimizationLevel: CAM.OperationBuilder.OptimizationLevelTypes
    PathDisplayOptions: CAM.OperationDisplayOptionsBuilder
    PostToolPathExit: str
    RetractDistance: CAM.InheritableDoubleBuilder
    RetractDistanceOnToolAxisChange: CAM.InheritableDoubleBuilder
    SafeClearance: CAM.InheritableDoubleBuilder
    SelectToolFlag: bool
    StartOfPath: CAM.PostEventsCiBuilder
    StartUdeSet: CAM.UdeSet
    ToolChangeSetting: CAM.ToolChangeCiBuilder
    ToolPathEditor: CAM.ToolPathEditorBuilder
    ToolPathSplitParametersBuilder: CAM.ToolPathSplitParametersBuilder


    class OptimizationLevelTypes(enum.Enum):
        Standard = 0
        Advanced = 1
    

    class OptimizationDistanceTypes(enum.Enum):
        Direct = 0
        Transition = 1
    

    class OptimizationBasedOnTypes(enum.Enum):
        Dist = 0
        Orient = 1
    

    class HoleDepthTypes(enum.Enum):
        Point = 0
        Rule = 1
    

    class HoleAxisTypes(enum.Enum):
        Vector = 0
        Rule = 1
        RuleIfNoVector = 2
    

class Operation(CAM.CAMObject):
    def __init__(self) -> None: ...
    def AppendMove(self, move: CAM.Move) -> None:
        ...
    def InsertMove(self, insertAfter: CAM.Move, move: CAM.Move) -> None:
        ...
    def GetUserDefinedMoveTypes(self) -> str:
        ...
    def CreateToolPathEditorBuilder(self) -> CAM.ToolPathEditorBuilder:
        ...
    def GetToolpathTime(self) -> float:
        ...
    def SetToolpathTime(self, time: float) -> None:
        ...
    def GetToolpathLength(self) -> float:
        ...
    def SetToolpathLength(self, length: float) -> None:
        ...
    def GetToolpathCuttingTime(self) -> float:
        ...
    def SetToolpathCuttingTime(self, time: float) -> None:
        ...
    def GetToolpathCuttingLength(self) -> float:
        ...
    def SetToolpathCuttingLength(self, length: float) -> None:
        ...
    def GetParent(self, branch: CAM.CAMSetup.View) -> CAM.NCGroup:
        ...
    def UnlinkInstance(self) -> None:
        ...
    def GetInputIpw(self) -> NXObject:
        ...
    def InsertFeature(self, tagMachiningFeature: CAM.CAMFeature) -> CAM.FBM.Feature:
        ...
    def RemoveFeature(self, tagFeature: CAM.CAMFeature) -> None:
        ...
    def GetInProcessFeatureType(self) -> str:
        ...
    def SetInProcessFeatureType(self, type: str) -> None:
        ...
    def SetMachiningArea(self, type: str) -> None:
        ...
    def PerformGougeCheck(self, gougeOption: CAM.GougeCheckResults.Option) -> CAM.GougeCheckResults:
        ...
    def ResetGougeChecking(self) -> None:
        ...
    def SaveMasterPath(self, inThePart: bool) -> None:
        ...
    def LoadMasterPathFromPart(self, masterPathPartName: str) -> bool:
        ...
    def LoadMasterPath(self) -> bool:
        ...
    def HasMasterPath(self) -> bool:
        ...
    def DeleteMasterPath(self) -> None:
        ...
    def GetOtherInstances(self) -> typing.List[CAM.Operation]:
        ...
    def GetDividedOperations(self) -> typing.List[CAM.Operation]:
        ...
    def GetFirstOfDivide(self) -> CAM.Operation:
        ...
    def IsAdditive(self) -> bool:
        ...
    def ComparePath(self, positionTolerance: float, angleTolerance: float) -> bool:
        ...
    def ComparePath(self, positionTolerance: float, angleTolerance: float, exactCompare: bool, realCompare: bool, tubeCompare: bool) -> bool:
        ...
    def IsMirror(self) -> bool:
        ...
    def IsMaintainCutDirection(self) -> bool:
        ...
    def IsMaintainCutAngle(self) -> bool:
        ...
    def GetNumberOfFindings(self, type: CAM.Operation.FindingTypes) -> int:
        ...
    CAMMoveCollection: CAM.MoveCollection
    CutRegionsData: CAM.CutRegionsData
    GougeCheckResults: CAM.GougeCheckResults
    GougeCheckStatus: bool
    HasOtherInstances: bool
    IsDivided: bool
    IsFirstOfDivide: bool


    class FindingTypes(enum.Enum):
        Gouge = 1
        Spike = 2
    

class OffsetDataBuilder(TaggedObject):
    def __init__(self) -> None: ...
    OffsetDirection: bool
    OffsetDistance: float
    OffsetType: CAM.OffsetDataBuilder.OffsetDirectionMethod
    OffsetVector: Direction


    class OffsetDirectionMethod(enum.Enum):
        Normal = 0
        Specify = 1
    

class ObjectWorkInstructionBuilder(Builder):
    def __init__(self) -> None: ...
    Work: CAM.WorkInstructionBuilder


class ObjectsUdeSet(Builder):
    def __init__(self) -> None: ...
    UdeSet: CAM.UdeSet


class ObjectsFeedsBuilder(Builder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder


class ObjectNotes(Builder):
    def __init__(self) -> None: ...
    Notes: CAM.Notes


class ObjectContainer(TaggedObject):
    def __init__(self) -> None: ...
    def Cut(self, current: int) -> None:
        ...
    def Copy(self, current: int) -> None:
        ...
    def Paste(self, current: int) -> None:
        ...
    def PasteBefore(self, current: int) -> None:
        ...
    def Delete(self, indices: int) -> None:
        ...


class Notes(TaggedObject):
    def __init__(self) -> None: ...
    def GetText(self) -> str:
        ...
    def SetText(self, text: str) -> None:
        ...


class NormalToToolAxisMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Angle: float
    AngleBuilder: CAM.ExpressionDouble
    Distance: float
    DistanceBuilder: CAM.ExpressionDouble
    EndPointBuilder: CAM.ReferencePoint
    MoveType: CAM.NormalToToolAxisMoveBuilder.Orientation
    Point: Point
    RoundPoint: CAM.RoundPointBuilder
    Vector: Direction
    VectorBuilder: CAM.ReferenceVector


    class Orientation(enum.Enum):
        AlongVector = 0
        TowardsPoint = 1
    

class NcmWedmBuilder(CAM.NcmSubopBuilder):
    def __init__(self) -> None: ...
    CutcomOff: CAM.NcmWedmBuilder.CutcomOffTypes
    CutcomOn: CAM.NcmWedmBuilder.CutcomOnTypes
    CutcomReg: int
    CutcomRegBuilder: CAM.InheritableIntBuilder
    CutcomRegisterFlag: bool
    FromPointBuilder: CAM.WedmPointDefinitionBuilder
    GlobalStopPointDistanceBuilder: CAM.InheritableDoubleBuilder
    GlobalStopPointMethod: CAM.NcmWedmBuilder.GlobalStopPointMethodTypes
    GlobalStopPointType: CAM.NcmWedmBuilder.GlobalStopPointTypes
    GoHomePointBuilder: CAM.WedmPointDefinitionBuilder
    LeadInAngleBuilder: CAM.InheritableDoubleBuilder
    LeadInCutcomAngleBuilder: CAM.InheritableDoubleBuilder
    LeadInCutcomDistanceBuilder: CAM.InheritableDoubleBuilder
    LeadInDistanceBuilder: CAM.InheritableDoubleBuilder
    LeadInMethod: CAM.NcmWedmBuilder.LeadInMethodTypes
    LeadOutAngleBuilder: CAM.InheritableDoubleBuilder
    LeadOutCutcomAngleBuilder: CAM.InheritableDoubleBuilder
    LeadOutCutcomDistanceBuilder: CAM.InheritableDoubleBuilder
    LeadOutDistanceBuilder: CAM.InheritableDoubleBuilder
    LeadOutMethod: CAM.NcmWedmBuilder.LeadOutMethodTypes
    LeadOutSameAsLeadIn: CAM.NcmWedmBuilder.LeadOutSameAsLeadInTypes
    NonTiltLeadIn: CAM.NcmWedmBuilder.NonTiltLeadInTypes


    class NonTiltLeadInTypes(enum.Enum):
        Zm = 0
        FourAxis = 1
    

    class LeadOutSameAsLeadInTypes(enum.Enum):
        No = 0
        Yes = 1
    

    class LeadOutMethodTypes(enum.Enum):
        SameAsLeadIn = 0
        Direct = 1
        Angular = 2
        Circular = 3
    

    class LeadInMethodTypes(enum.Enum):
        Direct = 0
        Angular = 1
        Circular = 2
    

    class GlobalStopPointTypes(enum.Enum):
        Opstop = 0
        Stop = 1
    

    class GlobalStopPointMethodTypes(enum.Enum):
        None = 0
        Specify = 1
    

    class CutcomOnTypes(enum.Enum):
        None = 0
        BeforeLeadIn = 1
        AfterLeadIn = 2
        AtThreadPoint = 3
    

    class CutcomOffTypes(enum.Enum):
        None = 0
        BeforeLeadOut = 1
        AfterLeadOut = 2
        BeforeThreadPoint = 3
    

class NcmTurnThreadBuilder(CAM.NcmTurningBuilder):
    def __init__(self) -> None: ...
    EngageBuilder: CAM.TurnThreadEngageRetractBuilder
    LocalReturnFinishGetEndEvents: CAM.PostEventsCiBuilder
    LocalReturnFinishGetStartEvents: CAM.PostEventsCiBuilder
    LocalReturnFinishMode: CAM.NcmTurnThreadBuilder.LocalReturnModes
    LocalReturnFinishMove: CAM.NcmTurnThreadBuilder.LocalReturnTypes
    LocalReturnFinishNumberOfPasses: int
    LocalReturnFinishPoint: Point
    LocalReturnMode: CAM.NcmTurnThreadBuilder.LocalReturnMainModes
    LocalReturnMove: CAM.NcmTurnThreadBuilder.LocalReturnTypes
    LocalReturnPoint: Point
    LocalReturnRoughGetEndEvents: CAM.PostEventsCiBuilder
    LocalReturnRoughGetStartEvents: CAM.PostEventsCiBuilder
    LocalReturnRoughMode: CAM.NcmTurnThreadBuilder.LocalReturnModes
    LocalReturnRoughMove: CAM.NcmTurnThreadBuilder.LocalReturnTypes
    LocalReturnRoughNumberOfPasses: int
    LocalReturnRoughPoint: Point
    MinimumClearanceBuilder: CAM.InheritableDoubleBuilder
    Opstops: int
    RetractBuilder: CAM.TurnThreadEngageRetractBuilder


    class LocalReturnTypes(enum.Enum):
        None = 0
        Direct = 1
        RadialAxial = 2
        AxialRadial = 3
        ClearRadialDirect = 4
        ClearAxialDirect = 5
        ClearRadial = 6
        ClearAxial = 7
        RadialClearAxialDirect = 8
        RadialAxialRadial = 9
        RadialClearAxial = 10
        ClearRadialClearAxialDirect = 11
        ClearRadialAxialRadial = 12
        ClearRadialClearAxial = 13
    

    class LocalReturnModes(enum.Enum):
        None = 0
        NumberOfStarts = 1
        NumberOfPasses = 2
    

    class LocalReturnMainModes(enum.Enum):
        Opstop = 0
        ThreadPasses = 1
    

class NcmTurnRoughFinishBuilder(CAM.NcmTurningBuilder):
    def __init__(self) -> None: ...
    AvoidanceForAutomaticEngage: bool
    AvoidanceForAutomaticRetract: bool
    AvoidanceForMinimumClearance: bool
    AxialSafeClearance: float
    EngageProfileBuilder: CAM.TurnEngageRetractBuilder
    LocalReturnBuilder: CAM.TurnRoughFinishLocalReturnBuilder
    RadialSafeClearance: float
    RetractProfileBuilder: CAM.TurnEngageRetractBuilder


class NcmTurnRoughBuilder(CAM.NcmTurnRoughFinishBuilder):
    def __init__(self) -> None: ...
    EngageFirstPlungeBuilder: CAM.TurnEngageRetractBuilder
    EngageLevelBlankBuilder: CAM.TurnEngageRetractBuilder
    EngageLevelPartBuilder: CAM.TurnEngageRetractBuilder
    EngageLevelSafeBuilder: CAM.TurnEngageRetractBuilder
    EngagePlungeBuilder: CAM.TurnEngageRetractBuilder
    ProfillingLocalReturnBuilder: CAM.TurnRoughFinishLocalReturnBuilder
    RetractFirstPlungeBuilder: CAM.TurnEngageRetractBuilder
    RetractLevelBlankBuilder: CAM.TurnEngageRetractBuilder
    RetractLevelPartBuilder: CAM.TurnEngageRetractBuilder
    RetractPlungeBuilder: CAM.TurnEngageRetractBuilder


class NcmTurningBuilder(CAM.NcmSubopBuilder):
    def __init__(self) -> None: ...
    AvoidanceAfterLastRetract: bool
    AvoidanceApproachBuilder: CAM.TurnAvoidanceApproachBuilder
    AvoidanceBetweenRegions: bool
    AvoidanceClearanceBuilder: CAM.TurnAvoidanceClearanceBuilder
    AvoidanceDepartureBuilder: CAM.TurnAvoidanceDepartureBuilder
    AvoidanceFromBuilder: CAM.TurnAvoidanceFromBuilder
    AvoidanceGohomeBuilder: CAM.TurnAvoidanceGohomeBuilder
    AvoidanceReturnBuilder: CAM.TurnAvoidanceReturnBuilder
    AvoidanceStartBuilder: CAM.TurnAvoidanceStartBuilder
    AvoidanceStartOfEngageBuilder: CAM.TurnAvoidanceStartOfEngageBuilder
    AvoidanceToStartOfEngage: bool
    Cutcom: CAM.Cutcom
    NcmHoleMachiningBuilder: CAM.NcmHoleMachining


class NcmTransferTypes(TaggedObject):
    def __init__(self) -> None: ...
    FinalSafeDistance: CAM.InheritableToolDepBuilder
    FinalType: CAM.NcmTransferTypes.FinalTypes
    InitialSafeDistance: CAM.InheritableToolDepBuilder
    InitialType: CAM.NcmTransferTypes.InitialTypes
    TransferInitialFinal: CAM.NcmTransferBuilder


    class InitialTypes(enum.Enum):
        Clearance = 0
        Distance = 1
        None = 2
        BlankPlane = 3
        ClearanceShortestDistance = 4
        ClearanceCutPlane = 5
    

    class FinalTypes(enum.Enum):
        Clearance = 0
        Distance = 1
        None = 2
        ClearanceShortestDistance = 3
        ClearanceCutPlane = 4
    

class NcmTransferBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AppUdeSet: CAM.UdeSet
    ApproachClearanceBuilder: CAM.NcmClearanceBuilder
    ApproachHeightBuilder: CAM.InheritableToolDepBuilder
    ApproachLengthBuilder: CAM.InheritableToolDepBuilder
    ApproachMethod: CAM.NcmTransferBuilder.AppDepMethodTypes
    ApproachPostCommands: TaggedObject
    ApproachToolAxis: SmartObject
    ApproachToolAxisOption: CAM.NcmTransferBuilder.AppDepToolAxisOptions
    ApproachVector: SmartObject
    DepUdeSet: CAM.UdeSet
    DepartureClearanceBuilder: CAM.NcmClearanceBuilder
    DepartureHeightBuilder: CAM.InheritableToolDepBuilder
    DepartureLengthBuilder: CAM.InheritableToolDepBuilder
    DepartureMethod: CAM.NcmTransferBuilder.AppDepMethodTypes
    DeparturePostCommands: TaggedObject
    DepartureToolAxis: SmartObject
    DepartureToolAxisOption: CAM.NcmTransferBuilder.AppDepToolAxisOptions
    DepartureVector: SmartObject
    TraUdeSet: CAM.UdeSet
    TraverseClearanceBuilder: CAM.NcmClearanceBuilder
    TraverseDistanceBuilder: CAM.InheritableToolDepBuilder
    TraversePostCommands: TaggedObject
    TraverseType: CAM.NcmTransferBuilder.TraverseTypes


    class TraverseTypes(enum.Enum):
        Same = 0
        ShortestToClearance = 1
        LowestSafeZ = 2
        Direct = 3
        Smooth = 4
    

    class LongMotionTypes(enum.Enum):
        Stepover = 0
        RetractTraverseEngage = 1
    

    class AppDepToolAxisOptions(enum.Enum):
        NoChange = 0
        Specify = 1
    

    class AppDepMethodTypes(enum.Enum):
        Same = 0
        None = 1
        AlongToolAxis = 2
        AlongVector = 3
        ToolAxisClearance = 4
        ShortestDistanceClearance = 5
        VectorClearance = 6
        TangentClearance = 7
        Automatic = 8
    

class NcmTransfer(TaggedObject):
    def __init__(self) -> None: ...
    ApplySafetyToDirect: bool
    MaxToolAxisChange: float
    SafeDistanceBuilder: CAM.InheritableToolDepBuilder
    Type: CAM.NcmTransfer.TransferTypes


    class TransferTypes(enum.Enum):
        Clearance = 0
        PrevPlane = 1
        Direct = 2
        LowestSafeZ = 3
        BlankPlane = 4
        ShortestToClearance = 5
        CutPlaneToClearance = 6
        Smooth = 7
        DirectPreviousPlaneBackup = 8
    

class NcmSubopBuilder(CAM.BaseBuilder):
    def __init__(self) -> None: ...
    def GetRegionStartPoints(self, regionStartPoints: typing.List[Point]) -> None:
        ...
    def SetRegionStartPoints(self, regionStartPoints: typing.List[Point]) -> None:
        ...
    DefaultRegionStartType: CAM.NcmSubopBuilder.DefaultRegionStartTypes
    StartPointsEffectDistBuilder: CAM.InheritableToolDepBuilder
    StartPointsUseEffectDist: bool


    class DefaultRegionStartTypes(enum.Enum):
        MidPoint = 0
        Corner = 1
    

class NcmSmoothingBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ApplyCornersSmoothing: bool
    ApplyCornersSmoothingTransfers: bool
    EngRetMaxToolAxisChange: float
    EngRetTolerance: float
    EngRetToleranceSource: CAM.NcmSmoothingBuilder.SmoothToleranceSources
    MaxStepoverDistance: CAM.InheritableToolDepBuilder
    OverrideWithSmoothConnections: bool
    PartSafeClearance: CAM.InheritableToolDepBuilder
    RegionDistance: CAM.InheritableToolDepBuilder
    SmoothHeight: CAM.InheritableToolDepBuilder
    SmoothLength: CAM.InheritableToolDepBuilder
    SmoothingRadius: CAM.InheritableToolDepBuilder
    TransferMaxToolAxisChange: float
    TransferTolerance: float
    TransferToleranceSource: CAM.NcmSmoothingBuilder.SmoothToleranceSources


    class SmoothToleranceSources(enum.Enum):
        MinimizePoints = 0
        Cutting = 1
        Specify = 2
    

class NcmScEngRetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetPoints(self, points: typing.List[Point]) -> None:
        ...
    def SetPoints(self, points: typing.List[Point]) -> None:
        ...
    ArcAngle: float
    DiameterBuilder: CAM.InheritableToolDepBuilder
    EffectDistBuilder: CAM.InheritableToolDepBuilder
    EngRetType: CAM.NcmScEngRetBuilder.EngRetTypes
    ExtendAfterArc: CAM.InheritableToolDepBuilder
    ExtendBeforeArc: CAM.InheritableToolDepBuilder
    HeightBuilder: CAM.InheritableToolDepBuilder
    HelicalRampAngle: float
    HelicalRampAngleBuilder: CAM.InheritableDoubleBuilder
    LengthBuilder: CAM.InheritableToolDepBuilder
    LinearExtensionBuilder: CAM.InheritableToolDepBuilder
    MeasureFrom: CAM.NcmScEngRetBuilder.MeasureFromTypes
    Plane: Plane
    RadiusBuilder: CAM.InheritableToolDepBuilder
    RampAngle: float
    SwingAngle: float
    UseEffectDist: bool
    Vector: SmartObject


    class MeasureFromTypes(enum.Enum):
        Distance = 0
        Plane = 1
    

    class EngRetTypes(enum.Enum):
        SameAsDefault = 0
        SameAsEngage = 1
        Linear = 2
        LinearAlongVector = 3
        LinearNormalToPart = 4
        ArcParallelToToolAxis = 5
        ArcNormalToToolAxis = 6
        ArcTangentToApproach = 7
        ArcNormalToPart = 8
        HelicalClw = 9
        HelicalCclw = 10
        PlungeLift = 11
        None = 12
        Points = 13
        Smooth = 14
    

class NcmScBuilder(CAM.NcmSubopBuilder):
    def __init__(self) -> None: ...
    CollisionCheck: bool
    EngageAgainstCheckBuilder: CAM.NcmScEngRetBuilder
    EngageInitialBuilder: CAM.NcmScEngRetBuilder
    EngageOpenAreaBuilder: CAM.NcmScEngRetBuilder
    MaxToolAxisChange: float
    OutputContactData: bool
    PartSafeClearance: CAM.InheritableToolDepBuilder
    RetractAgainstCheckBuilder: CAM.NcmScEngRetBuilder
    RetractFinalBuilder: CAM.NcmScEngRetBuilder
    RetractOpenAreaBuilder: CAM.NcmScEngRetBuilder
    SmoothingBuilder: CAM.NcmSmoothingBuilder
    SmoothingOption: CAM.NcmScBuilder.SmoothingOptions
    SmoothingRadiusBuilder: CAM.InheritableToolDepBuilder
    TransferAvoidanceFromBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceGohomeBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceReturnBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceStartBuilder: CAM.NcmAvoidancePointBuilder
    TransferBetweenRegionsBuilder: CAM.NcmTransferBuilder
    TransferCommonClearanceBuilder: CAM.NcmClearanceBuilder
    TransferInitialFinalBuilder: CAM.NcmTransferBuilder
    TransferRegionDistanceBuilder: CAM.InheritableToolDepBuilder
    TransferWithinRegionsBuilder: CAM.NcmTransferBuilder


    class SmoothingOptions(enum.Enum):
        On = 0
        Off = 1
    

class NcmPlanarEngRetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetPoints(self, points: typing.List[Point]) -> None:
        ...
    def SetPoints(self, points: typing.List[Point]) -> None:
        ...
    ArcAngle: float
    DiameterBuilder: CAM.InheritableToolDepBuilder
    EffectDistBuilder: CAM.InheritableToolDepBuilder
    EngRetType: CAM.NcmPlanarEngRetBuilder.EngRetTypes
    ExtendAfterArc: CAM.InheritableToolDepBuilder
    ExtendBeforeArc: CAM.InheritableToolDepBuilder
    HeightBuilder: CAM.InheritableToolDepBuilder
    HeightFrom: CAM.NcmPlanarEngRetBuilder.MeasureHeightFrom
    HelicalRampAngleBuilder: CAM.InheritableDoubleBuilder
    IfEngageDoesNotFit: CAM.NcmPlanarEngRetBuilder.IfEngageDoesNotFitTypes
    IgnoreBlankOnTrimSide: bool
    LengthBuilder: CAM.InheritableToolDepBuilder
    MaxWidthBuilder: CAM.InheritableToolDepBuilder
    MinClearanceBuilder: CAM.InheritableToolDepBuilder
    MinRampLengthBuilder: CAM.InheritableToolDepBuilder
    MinimumClearance: CAM.NcmPlanarEngRetBuilder.MinClearanceTypes
    Plane: SmartObject
    RadiusBuilder: CAM.InheritableToolDepBuilder
    RampAngle: float
    StartAtArcCenter: bool
    SwingAngle: float
    Trim: bool
    UseEffectDist: bool
    UseMaxWidth: bool
    Vector: SmartObject


    class MinClearanceTypes(enum.Enum):
        None = 0
        ExtendAndTrim = 1
        ExtendOnly = 2
        SameAsOpenEngage = 3
        SameAsRetract = 4
    

    class MeasureHeightFrom(enum.Enum):
        CurrentLevel = 0
        PreviousLevel = 1
        Plane = 2
    

    class IfEngageDoesNotFitTypes(enum.Enum):
        Plunge = 0
        Skip = 1
    

    class EngRetTypes(enum.Enum):
        SameAsDefault = 0
        SameAsClosed = 1
        SameAsEngage = 2
        Helical = 3
        RampOnShape = 4
        ZigzagRamp = 5
        Linear = 6
        Arc = 7
        ArcParallelToToolAxis = 8
        ArcNormalToToolAxis = 9
        ArcNormalToPart = 10
        HighSpeedArc = 11
        Points = 12
        PlungeLift = 13
        AlongVector = 14
        AngAngPlane = 15
        VectorPlane = 16
        None = 17
        LinearRelativeCut = 18
        Smooth = 19
    

class NcmPlanarBuilder(CAM.NcmSubopBuilder):
    def __init__(self) -> None: ...
    def GetPredrillPoints(self) -> typing.List[Point]:
        ...
    def SetPredrillPoints(self, predrillPoints: typing.List[Point]) -> None:
        ...
    ApplySafetyToDirect: bool
    ClearanceBuilder: CAM.NcmClearanceBuilder
    CollisionCheck: bool
    CutcomMinimumAngle: float
    CutcomMinimumMoveBuilder: CAM.InheritableToolDepBuilder
    CutcomOutputContactPoint: bool
    CutcomOutputPlane: bool
    CutcomTrackingPointType: int
    CutcomType: CAM.NcmPlanarBuilder.CutcomTypes
    EngageClosedAreaBuilder: CAM.NcmPlanarEngRetBuilder
    EngageInitialClosedBuilder: CAM.NcmPlanarEngRetBuilder
    EngageInitialOpenBuilder: CAM.NcmPlanarEngRetBuilder
    EngageOpenAreaBuilder: CAM.NcmPlanarEngRetBuilder
    FinalSafeDistanceBuilder: CAM.InheritableToolDepBuilder
    FinalType: CAM.NcmPlanarBuilder.FinalTypes
    InitialSafeDistanceBuilder: CAM.InheritableToolDepBuilder
    InitialType: CAM.NcmPlanarBuilder.InitialTypes
    LimitEngRetToCutRegion: bool
    OverlapDistanceBuilder: CAM.InheritableToolDepBuilder
    PredrillPointsEffectDistBuilder: CAM.InheritableToolDepBuilder
    PredrillPointsOutput: CAM.NcmPlanarBuilder.PredrillPointsOutputOptions
    PredrillPointsUseEffectDist: bool
    RetractAreaBuilder: CAM.NcmPlanarEngRetBuilder
    RetractFinalBuilder: CAM.NcmPlanarEngRetBuilder
    SmoothingBuilder: CAM.NcmSmoothingBuilder
    SuppressCutcom: bool
    TransferAvoidanceFromBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceGohomeBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceReturnBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceStartBuilder: CAM.NcmAvoidancePointBuilder
    TransferBetweenLevelsSafeDistanceBuilder: CAM.InheritableToolDepBuilder
    TransferBetweenLevelsType: CAM.NcmPlanarBuilder.TransferBetweenLevelsTypes
    TransferBetweenRegionsBuilder: CAM.NcmTransfer
    TransferBetweenRegionsSafeDistanceBuilder: CAM.InheritableToolDepBuilder
    TransferBetweenRegionsType: CAM.NcmPlanarBuilder.TransferBetweenRegionsTypes
    TransferWithinLevelsHeightBuilder: CAM.InheritableToolDepBuilder
    TransferWithinLevelsMaxFollowDistanceBuilder: CAM.InheritableToolDepBuilder
    TransferWithinLevelsSafeDistanceBuilder: CAM.InheritableToolDepBuilder
    TransferWithinLevelsType: CAM.NcmPlanarBuilder.TransferWithinLevelsTypes
    TransferWithinLevelsWith: CAM.NcmPlanarBuilder.TransferWithinLevelsWiths


    class TransferWithinLevelsWiths(enum.Enum):
        UseEngret = 0
        FollowBoundary = 1
        LiftPlunge = 2
        None = 3
        Smooth = 4
    

    class TransferWithinLevelsTypes(enum.Enum):
        LowestSafeZ = 0
        PrevPlane = 1
        Direct = 2
        Clearance = 3
        BlankPlane = 4
        ShortestToClearance = 5
        CutPlaneToClearance = 6
        Smooth = 7
        DirectPreviousPlaneBackup = 8
        CutPlane = 9
    

    class TransferBetweenRegionsTypes(enum.Enum):
        Clearance = 0
        PrevPlane = 1
        Direct = 2
        LowestSafeZ = 3
        BlankPlane = 4
        ShortestToClearance = 5
        CutPlaneToClearance = 6
    

    class TransferBetweenLevelsTypes(enum.Enum):
        PrevPlane = 0
        Direct = 1
        Clearance = 2
    

    class PredrillPointsOutputOptions(enum.Enum):
        None = 0
        AllRegions = 1
        BottomRegions = 2
    

    class InitialTypes(enum.Enum):
        Clearance = 0
        Distance = 1
        None = 2
        BlankPlane = 3
        ShortestDistanceToClearance = 4
        CutPlaneToClearance = 5
    

    class InitialEng(enum.Enum):
        Inherit = 0
        Lift = 1
        None = 2
    

    class FinalTypes(enum.Enum):
        Clearance = 0
        Distance = 1
        None = 2
        ShortestDistanceToClearance = 3
        CutPlaneToClearance = 4
    

    class FinalRet(enum.Enum):
        Inherit = 0
        Plunge = 1
        None = 2
    

    class CutcomTypes(enum.Enum):
        None = 0
        AllFinishPasses = 1
        FinalFinishPass = 2
    

class NcmOptimizeGroup(CAM.NcmSubopBuilder):
    def __init__(self) -> None: ...
    CollisionCheck: bool
    NcmSmoothing: CAM.NcmSmoothingBuilder
    TransferAvoidanceFrom: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceGohome: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceReturn: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceStart: CAM.NcmAvoidancePointBuilder
    TransferBetweenRegions: CAM.NcmTransfer
    TransferClearance: CAM.NcmClearanceBuilder
    TransferInitialFinal: CAM.NcmTransferTypes


class NcmLaserRetract(TaggedObject):
    def __init__(self) -> None: ...
    ArcAngle: CAM.InheritableDoubleBuilder
    ExtendDistance: CAM.InheritableToolDepBuilder
    Length: CAM.InheritableToolDepBuilder
    Radius: CAM.InheritableToolDepBuilder
    RetractType: CAM.NcmLaserRetract.Type
    SwingAngle: CAM.InheritableDoubleBuilder


    class Type(enum.Enum):
        LinearRelToCut = 0
        Arc = 1
    

class NcmLaserEngage(TaggedObject):
    def __init__(self) -> None: ...
    ArcAngle: CAM.InheritableDoubleBuilder
    EngageType: CAM.NcmLaserEngage.Type
    ExtendDistance: CAM.InheritableToolDepBuilder
    Length: CAM.InheritableToolDepBuilder
    Radius: CAM.InheritableToolDepBuilder
    SwingAngle: CAM.InheritableDoubleBuilder


    class Type(enum.Enum):
        LinearRelToCut = 0
        Arc = 1
    

class NcmHoleMachiningEngRet(TaggedObject):
    def __init__(self) -> None: ...
    EngRetType: CAM.NcmHoleMachiningEngRet.EngRetTypes
    Height: CAM.InheritableToolDepBuilder
    MinClearance: CAM.InheritableToolDepBuilder
    StartFromCenter: bool


    class EngRetTypes(enum.Enum):
        SameAsDefault = 0
        SameAsEngage = 1
        Helical = 2
        Linear = 3
        Circular = 4
        None = 5
        MinimumClearance = 6
    

class NcmHoleMachining(CAM.NcmSubopBuilder):
    def __init__(self) -> None: ...
    CollisionCheck: bool
    CutcomMinimumAngle: float
    CutcomMinimumMove: CAM.InheritableToolDepBuilder
    CutcomOutputContactPoint: bool
    CutcomOutputPlane: bool
    CutcomType: CAM.NcmHoleMachining.CutcomTypes
    Engage: CAM.NcmHoleMachiningEngRet
    FinalRetract: CAM.NcmHoleMachiningEngRet
    FinalSafeDistance: CAM.InheritableToolDepBuilder
    FinalType: CAM.NcmHoleMachining.FinalTypes
    InitialEngage: CAM.NcmHoleMachiningEngRet
    InitialSafeDistance: CAM.InheritableToolDepBuilder
    InitialType: CAM.NcmHoleMachining.InitialTypes
    NcmSmoothing: CAM.NcmSmoothingBuilder
    NumberOfThreads: float
    OverlapAngle: float
    OverlapDistance: float
    OverlapType: CAM.NcmHoleMachining.OverlapTypes
    RegionStartAngle: float
    Retract: CAM.NcmHoleMachiningEngRet
    StartFromCenter: bool
    SuppressCutcom: bool
    TrackingData: str
    TransferAvoidanceFrom: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceGohome: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceReturn: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceStart: CAM.NcmAvoidancePointBuilder
    TransferBetweenRegions: CAM.NcmTransfer
    TransferClearance: CAM.NcmClearanceBuilder
    TransferInitialFinal: CAM.NcmTransferBuilder


    class OverlapTypes(enum.Enum):
        Axial = 0
        AlongCut = 1
        Angle = 2
    

    class InitialTypes(enum.Enum):
        Clearance = 0
        Distance = 1
        None = 2
        BlankPlane = 3
        ClearanceShortestDistance = 4
        ClearanceCutPlane = 5
    

    class FinalTypes(enum.Enum):
        Clearance = 0
        Distance = 1
        None = 2
        ClearanceShortestDistance = 3
        ClearanceCutPlane = 4
    

    class CutcomTypes(enum.Enum):
        None = 0
        AllPasses = 1
        FinalPass = 2
    

class NcmHoleDrilling(CAM.NcmHoleMachining):
    def __init__(self) -> None: ...


class NcmEngRetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    EngageRetractType: CAM.NcmEngRetBuilder.EngageRetractTypes
    HeightBuilder: CAM.InheritableToolDepBuilder
    LengthBuilder: CAM.InheritableToolDepBuilder
    RampAngle: float
    SafeClearanceBuilder: CAM.InheritableToolDepBuilder
    SwingAngle: float


    class EngageRetractTypes(enum.Enum):
        Linear = 0
        PlungeLift = 1
        Smooth = 2
        None = 3
    

class NcmctPartMountingBuilder(Builder):
    def __init__(self) -> None: ...
    Geometry: SelectNXObjectList
    Layer: int
    LayerOptions: CAM.NcmctPartMountingBuilder.LayerTypes
    PartMountJunction: CartesianCoordinateSystem
    Positioning: CAM.NcmctPartMountingBuilder.PositioningTypes


    class PositioningTypes(enum.Enum):
        OrientMachineZeroToMainMcs = 0
        UseAssemblyPositioning = 1
        UsePartMountJunction = 2
        UseOldMachineTransformation = 3
        KeepAssemblyConstraints = 4
    

    class LayerTypes(enum.Enum):
        Original = 0
        OriginalMakeVisible = 1
        Work = 2
        AsSpecified = 3
    

class NcmClearanceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Axis: NXObject
    BoundingBoxClearance: float
    ClearanceType: CAM.NcmClearanceBuilder.ClearanceTypes
    PlaneXform: NXObject
    Point: NXObject
    Radius: float
    SafeDistance: float


    class ClearanceTypes(enum.Enum):
        UseCommon = 0
        None = 1
        Automatic = 2
        Plane = 3
        Point = 4
        Cylinder = 5
        Sphere = 6
        BoundingBox = 7
        BoundingCylinder = 8
    

class NcmAvoidancePointBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Point: Point
    PointStatus: CAM.NcmAvoidancePointBuilder.PointStates
    ToolAxis: NXObject
    ToolAxisStatus: int
    ToolAxisUsage: CAM.NcmAvoidancePointBuilder.ToolAxisUsages


    class ToolAxisUsages(enum.Enum):
        None = 0
        Specify = 1
    

    class PointStates(enum.Enum):
        None = 0
        UseOther = 1
        NoPoint = 2
        UsePoint = 3
    

class NCGroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.NCGroup]:
        ...
    def __init__(self, owner: CAM.CAMSetup) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.NCGroup:
        ...
    def CreateProgram(self, parentGroup: CAM.NCGroup, typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newProgramName: str) -> CAM.NCGroup:
        ...
    def CreateMethod(self, parentGroup: CAM.NCGroup, typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newMethodName: str) -> CAM.NCGroup:
        ...
    def CreateTool(self, parentGroup: CAM.NCGroup, typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newToolName: str) -> CAM.NCGroup:
        ...
    def CreateGeometry(self, parentGroup: CAM.NCGroup, typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newGeometryName: str) -> CAM.NCGroup:
        ...
    def CreateGeometry(self, parentGroup: CAM.NCGroup, features: typing.List[CAM.CAMFeature], typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newGeometryName: str) -> CAM.NCGroup:
        ...
    def CreateNcmPlanarBuilder(self) -> CAM.NcmPlanarBuilder:
        ...
    def CreateNcmScBuilder(self) -> CAM.NcmScBuilder:
        ...
    def CreateMillMethodBuilder(self, param: CAM.CAMObject) -> CAM.MillMethodBuilder:
        ...
    def CreateTurnMethodBuilder(self, param: CAM.CAMObject) -> CAM.TurnMethodBuilder:
        ...
    def CreateDrillMethodBuilder(self, param: CAM.CAMObject) -> CAM.DrillMethodBuilder:
        ...
    def CreateWedmMethodBuilder(self, param: CAM.CAMObject) -> CAM.WedmMethodBuilder:
        ...
    def CreateWedmBasedGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmBasedGeomBuilder:
        ...
    def CreateWedmCornerControlBuilder(self, param: CAM.CAMObject) -> CAM.WedmCornerControlBuilder:
        ...
    def CreateWedmCuttingBuilder(self, param: CAM.CAMObject) -> CAM.WedmCuttingBuilder:
        ...
    def CreateWedmExtGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmExtGeomBuilder:
        ...
    def CreateWedmFeatureGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmFeatureGeomBuilder:
        ...
    def CreateWedmIntGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmIntGeomBuilder:
        ...
    def CreateWedmLeadInOutBuilder(self, param: CAM.CAMObject) -> CAM.WedmLeadInOutBuilder:
        ...
    def CreateWedmMoveControlBuilder(self, param: CAM.CAMObject) -> CAM.WedmMoveControlBuilder:
        ...
    def CreateWedmNocoreGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmNocoreGeomBuilder:
        ...
    def CreateWedmOpenGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmOpenGeomBuilder:
        ...
    def CreateWedmGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmGeomBuilder:
        ...
    def CreateWedmOrientGeomBuilder(self, param: CAM.CAMObject) -> CAM.WedmOrientGeomBuilder:
        ...
    def CreateMillOrientGeomBuilder(self, param: CAM.CAMObject) -> CAM.MillOrientGeomBuilder:
        ...
    def CreateTurnOrientGeomBuilder(self, param: CAM.CAMObject) -> CAM.TurnOrientGeomBuilder:
        ...
    def CreateFeatureBasedGeomBuilder(self, param: CAM.CAMObject) -> CAM.FeatureBasedGeomBuilder:
        ...
    def CreateDrillGeomBuilder(self, param: CAM.CAMObject) -> CAM.DrillGeomBuilder:
        ...
    def CreateMillGeomBuilder(self, param: CAM.CAMObject) -> CAM.MillGeomBuilder:
        ...
    def CreateMillAreaGeomBuilder(self, param: CAM.CAMObject) -> CAM.MillAreaGeomBuilder:
        ...
    def CreateMillVolumeGeomBuilder(self, param: CAM.CAMObject) -> CAM.MillVolumeGeomBuilder:
        ...
    def CreateMillBoundaryGeomBuilder(self, param: CAM.CAMObject) -> CAM.MillBoundaryGeomBuilder:
        ...
    def CreateMillTextGeomBuilder(self, param: CAM.CAMObject) -> CAM.MillTextGeomBuilder:
        ...
    def CreateTurnGeomBuilder(self, param: CAM.CAMObject) -> CAM.TurnGeomBuilder:
        ...
    def CreateTurnBoundaryGeomBuilder(self, param: CAM.CAMObject) -> CAM.TurnBoundaryGeomBuilder:
        ...
    def CreateTurnFeatureGeomBuilder(self, param: CAM.CAMObject) -> CAM.TurnFeatureGeomBuilder:
        ...
    def CreateTurnAvoidanceGeomBuilder(self, param: CAM.CAMObject) -> CAM.TurnAvoidanceGeomBuilder:
        ...
    def CreateOptimizeTraverseGroupBuilder(self, param: CAM.CAMObject) -> CAM.OptimizeTraverseGroupBuilder:
        ...
    def CreateMachineGroupBuilder(self, param: CAM.CAMObject) -> CAM.MachineGroupBuilder:
        ...
    def CreateMachineTurretGroupBuilder(self, param: CAM.CAMObject) -> CAM.MachineTurretGroupBuilder:
        ...
    def CreateMultiToolBuilder(self, param: CAM.CAMObject) -> CAM.MultiToolBuilder:
        ...
    def CreateMachinePocketGroupBuilder(self, param: CAM.CAMObject) -> CAM.MachinePocketGroupBuilder:
        ...
    def CreateMachineHeadGroupBuilder(self, param: CAM.CAMObject) -> CAM.MachineHeadGroupBuilder:
        ...
    def CreateMillToolBuilder(self, param: CAM.CAMObject) -> CAM.MillToolBuilder:
        ...
    def CreateDrillStdToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillStdToolBuilder:
        ...
    def CreateTurnToolBuilder(self, param: CAM.CAMObject) -> CAM.TurnToolBuilder:
        ...
    def CreateMillFormToolBuilder(self, param: CAM.CAMObject) -> CAM.MillFormToolBuilder:
        ...
    def CreateTToolBuilder(self, param: CAM.CAMObject) -> CAM.TToolBuilder:
        ...
    def CreateThreadToolBuilder(self, param: CAM.CAMObject) -> CAM.ThreadToolBuilder:
        ...
    def CreateGrooveToolBuilder(self, param: CAM.CAMObject) -> CAM.GrooveToolBuilder:
        ...
    def CreateBarrelToolBuilder(self, param: CAM.CAMObject) -> CAM.BarrelToolBuilder:
        ...
    def CreateFormToolBuilder(self, param: CAM.CAMObject) -> CAM.FormToolBuilder:
        ...
    def CreateDrillCenterBellToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillCenterBellToolBuilder:
        ...
    def CreateDrillCounterboreToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillCounterboreToolBuilder:
        ...
    def CreateDrillCtskToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillCtskToolBuilder:
        ...
    def CreateDrillReamerToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillReamerToolBuilder:
        ...
    def CreateDrillSpotdrillToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillSpotdrillToolBuilder:
        ...
    def CreateDrillSpotfaceToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillSpotfaceToolBuilder:
        ...
    def CreateDrillStepToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillStepToolBuilder:
        ...
    def CreateDrillTapToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillTapToolBuilder:
        ...
    def CreateDrillThreadMillToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillThreadMillToolBuilder:
        ...
    def CreateDrillBurnishingToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillBurnishingToolBuilder:
        ...
    def CreateDrillBackSpotfacingToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillBackSpotfacingToolBuilder:
        ...
    def CreateDrillBoreToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillBoreToolBuilder:
        ...
    def CreateProgramOrderGroupBuilder(self, param: CAM.CAMObject) -> CAM.ProgramOrderGroupBuilder:
        ...
    def CreateProbeToolBuilder(self, param: CAM.CAMObject) -> CAM.ProbeToolBuilder:
        ...
    def CreateGenericToolBuilder(self, param: CAM.CAMObject) -> CAM.GenericToolBuilder:
        ...
    def CreateMultiBladeGeometryBuilder(self, param: CAM.CAMObject) -> CAM.MultiBladeGeomBuilder:
        ...
    def CreateHoleBossGeometryBuilder(self, param: CAM.CAMObject) -> CAM.HoleBossGeometry:
        ...
    def CreateDrillCoreToolBuilder(self, param: CAM.CAMObject) -> CAM.DrillCoreToolBuilder:
        ...
    def CreateWireTool(self, param: CAM.CAMObject) -> CAM.WireTool:
        ...
    def CreateLaserTool(self, param: CAM.CAMObject) -> CAM.LaserTool:
        ...
    def CreateLaserMethod(self, param: CAM.CAMObject) -> CAM.LaserMethod:
        ...
    def CreateGroupFeatures(self) -> CAM.GroupFeatures:
        ...
    def CreateRotaryFinishGeometryBuilder(self, param: CAM.CAMObject) -> CAM.RotaryFinishGeomBuilder:
        ...
    def CreateFeatureGroupBuilder(self, param: CAM.CAMObject) -> CAM.FeatureGroupBuilder:
        ...
    def CreateDrillBackCountersinkTool(self, param: CAM.CAMObject) -> CAM.DrillBackCountersinkTool:
        ...
    def CreateDrillBoringBarTool(self, param: CAM.CAMObject) -> CAM.DrillBoringBarTool:
        ...
    def CreateDrillChamferBoringBarTool(self, param: CAM.CAMObject) -> CAM.DrillChamferBoringBarTool:
        ...
    def Tag(self) -> Tag: ...



    class UseDefaultName(enum.Enum):
        False = 0
        True = 1
    

class NCGroupBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...
    Description: str
    EndUdeSet: CAM.UdeSet
    StartUdeSet: CAM.UdeSet


class NCGroup(CAM.CAMObject):
    def __init__(self) -> None: ...
    def GetParent(self) -> CAM.NCGroup:
        ...
    def GetMembers(self) -> typing.List[CAM.CAMObject]:
        ...
    def FindObject(self, sid: str) -> INXObject:
        ...


class NCAssistantBuilder(Builder):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def AnalyzeGeometry(self) -> None:
        ...
    def GetResults(self, analyzedFaces: typing.List[Face], doubleValue: float) -> bool:
        ...
    AnalysisType: CAM.NCAssistantBuilder.AnalysisTypes
    AngleTolerance: float
    DistanceTolerance: float
    FacesToAnalyze: SelectFaceList
    MaximumAngle: float
    MaximumLevel: float
    MaximumRadius: float
    MinimumAngle: float
    MinimumLevel: float
    MinimumRadius: float
    RadiusTolerance: float
    ReferencePlane: Plane
    ReferenceVector: Direction
    SaveFaceColors: bool


    class AnalysisTypes(enum.Enum):
        Levels = 0
        Corners = 1
        Blends = 2
        Draft = 3
    

class MultiToolExport(TaggedObject):
    def __init__(self) -> None: ...
    def SetAttributeAndValue(self, attributes: str, values: str) -> None:
        ...
    def Export(self) -> None:
        ...
    def GetValidTargetClasses(self, saveFlag: CAM.MultiToolExport.SaveFlags, replaceLibref: str) -> str:
        ...
    def GetValidAttributes(self, targetClass: str) -> str:
        ...
    def GetValidValuesOfAttribute(self, attr: str, valueIds: str, valueTexts: str) -> None:
        ...
    Libref: str
    SaveFlag: CAM.MultiToolExport.SaveFlags
    TargetClass: str


    class SaveFlags(enum.Enum):
        Replace = 0
        CreateNew = 1
    

class MultiToolBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def UpdateFromLibrary(self) -> None:
        ...
    MultiToolDescription: str
    MultiToolLibraryReference: str


class MultiRamp(TaggedObject):
    def __init__(self) -> None: ...
    MaxRampLength: CAM.InheritableDoubleBuilder
    Pattern: CAM.MultiRamp.Types


    class Types(enum.Enum):
        None = 0
        RampOutOrInOnly = 1
        RampOutOrIn = 2
    

class MultipleStepoverBuilder(Builder):
    def __init__(self) -> None: ...
    def Add(self, indexAfter: int, numOfPasses: int, distance: float, intent: int) -> None:
        ...
    def Modify(self, index: int, numOfPasses: int, distance: float, intent: int) -> None:
        ...
    def Delete(self, index: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...
    def GetNumberOfStepovers(self) -> int:
        ...
    def GetData(self, index: int, numOfPasses: int, distance: float, intent: int) -> None:
        ...


class MultiplePassesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    DepthIncrement: CAM.InheritableDoubleBuilder
    DepthStepMethod: CAM.MultiplePassesBuilder.StepMethodTypes
    DoDepthPasses: bool
    DoSidePasses: bool
    NumberOfDepthPasses: CAM.InheritableIntBuilder
    NumberOfSidePasses: CAM.InheritableIntBuilder
    Order: CAM.MultiplePassesBuilder.OrderTypes
    SideIncrement: CAM.InheritableDoubleBuilder
    SideStepMethod: CAM.MultiplePassesBuilder.StepMethodTypes
    TotalDepth: CAM.InheritableDoubleBuilder
    TotalThickness: CAM.InheritableDoubleBuilder


    class StepMethodTypes(enum.Enum):
        Increment = 0
        Passes = 1
    

    class OrderTypes(enum.Enum):
        SidePassesFirst = 0
        DepthPassesFirst = 1
    

class MultiDepthCut(TaggedObject):
    def __init__(self) -> None: ...
    Increment: CAM.InheritableDoubleBuilder
    NumberOfPasses: CAM.InheritableIntBuilder
    StepMethod: CAM.MultiDepthCut.Types
    Toggle: bool


    class Types(enum.Enum):
        Increment = 0
        Passes = 1
    

class MultiBladeSplittersGeometry(TaggedObject):
    def __init__(self) -> None: ...
    def CreateSplitter(self, wallFaces: typing.List[NXObject], blendFaces: typing.List[NXObject]) -> CAM.Splitter:
        ...
    SplitterList: CAM.SplitterList


class MultiBladeGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    AxisOfRotation: CAM.MultiBladeGeomBuilder.PartAxisOfRotationTypes
    NumberOfBlades: CAM.InheritableIntBuilder
    PartAxisBuilder: CAM.PartAxisBuilder
    PartAxisPoint: Point
    PartAxisVector: SmartObject


    class PartAxisOfRotationTypes(enum.Enum):
        Zm = 0
        Specify = 1
    

class MultiBladeBaseGeometry(TaggedObject):
    def __init__(self) -> None: ...
    def GetFaces(self) -> typing.List[NXObject]:
        ...
    def SetFaces(self, faces: typing.List[NXObject]) -> None:
        ...
    def RemoveFaces(self, faces: typing.List[NXObject]) -> None:
        ...


class MoveToPointBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    OffsetData: CAM.OffsetDataBuilder
    Point: Point
    PointBuilder: CAM.ReferencePoint
    RoundPoint: CAM.RoundPointBuilder


class MoveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.Move]:
        ...
    def __init__(self, owner: CAM.Operation) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.Move:
        ...
    def CreateMoveToPointBuilder(self, param: CAM.Move) -> CAM.MoveToPointBuilder:
        ...
    def CreateDeltaMoveBuilder(self, param: CAM.Move) -> CAM.DeltaMoveBuilder:
        ...
    def CreateVectorDistanceMoveBuilder(self, param: CAM.Move) -> CAM.VectorDistanceMoveBuilder:
        ...
    def CreateAlongToolAxisMoveBuilder(self, param: CAM.Move) -> CAM.AlongToolAxisMoveBuilder:
        ...
    def CreateNormalToToolAxisMoveBuilder(self, param: CAM.Move) -> CAM.NormalToToolAxisMoveBuilder:
        ...
    def CreateAlongMcsAxisMoveBuilder(self, param: CAM.Move) -> CAM.AlongMcsAxisMoveBuilder:
        ...
    def CreateRotaryPointMoveBuilder(self, param: CAM.Move) -> CAM.RotaryPointMoveBuilder:
        ...
    def CreateRotaryPolarMoveBuilder(self, param: CAM.Move) -> CAM.RotaryPolarMoveBuilder:
        ...
    def CreateCircularAboutAxisMoveBuilder(self, param: CAM.Move) -> CAM.CircularAboutAxisMoveBuilder:
        ...
    def CreateAlongMachineAxisMoveBuilder(self, param: CAM.Move) -> CAM.AlongMachineAxisMoveBuilder:
        ...
    def CreateUdeMoveBuilder(self, param: CAM.Move) -> CAM.UdeMoveBuilder:
        ...
    def CreateRotateToolMoveBuilder(self, param: CAM.Move, insertAfterTag: CAM.Move) -> CAM.RotateToolMoveBuilder:
        ...
    def CreateProbeCalibrateLengthMoveBuilder(self, param: CAM.Move) -> CAM.ProbeCalibrateLengthMoveBuilder:
        ...
    def CreateProbeCalibrateStylusMoveBuilder(self, param: CAM.Move) -> CAM.ProbeCalibrateStylusMoveBuilder:
        ...
    def CreateProbeCalibrateSphereMoveBuilder(self, param: CAM.Move) -> CAM.ProbeCalibrateSphereMoveBuilder:
        ...
    def CreateProbeInspectPointMoveBuilder(self, param: CAM.Move) -> CAM.ProbeInspectPointMoveBuilder:
        ...
    def CreateProbeInspectSurfacePointMoveBuilder(self, param: CAM.Move) -> CAM.ProbeInspectSurfacePointMoveBuilder:
        ...
    def CreateProbeInspectBorebossMoveBuilder(self, param: CAM.Move) -> CAM.ProbeInspectBorebossMoveBuilder:
        ...
    def CreateProbeClearanceMoveBuilder(self, param: CAM.Move) -> CAM.ProbeClearanceMoveBuilder:
        ...
    def CreateTeachmodeLinearMoveBuilder(self, param: CAM.Move) -> CAM.TeachmodeLinearMoveBuilder:
        ...
    def CreateTeachmodeEngageSettingsBuilder(self, param: CAM.Move) -> CAM.TeachmodeEngageSettingsBuilder:
        ...
    def CreateTeachmodeRetractSettingsBuilder(self, param: CAM.Move) -> CAM.TeachmodeRetractSettingsBuilder:
        ...
    def CreateTeachmodeProfileMoveBuilder(self, param: CAM.Move) -> CAM.TeachmodeProfileMoveBuilder:
        ...
    def CreateFollowCurveMoveBuilder(self, param: CAM.Move) -> CAM.FollowCurveMoveBuilder:
        ...
    def CreateFollowPartMoveBuilder(self, param: CAM.Move) -> CAM.FollowPartMoveBuilder:
        ...
    def CreateUserDefinedMoveBuilder(self, param: CAM.Move, typeName: str) -> CAM.UserDefinedMoveBuilder:
        ...
    def CreateToolTrackingPointBuilder(self, param: CAM.Move) -> CAM.ToolTrackingPointBuilder:
        ...
    def CreateTurnProbeInspectPointMoveBuilder(self, param: CAM.Move) -> CAM.TurnProbeInspectPointMoveBuilder:
        ...
    def CreateTurnProbeClearanceBuilder(self, param: CAM.Move) -> CAM.TurnProbeClearanceBuilder:
        ...
    def CreateTurnMoveToPointBuilder(self, param: CAM.Move) -> CAM.TurnMoveToPointBuilder:
        ...
    def CreateLaserLinearMove(self, param: CAM.Move) -> CAM.LaserLinearMove:
        ...
    def CreateLaserCircleCutout(self, param: CAM.Move) -> CAM.LaserCircleCutout:
        ...
    def CreateLaserRectangleCutout(self, param: CAM.Move) -> CAM.LaserRectangleCutout:
        ...
    def CreateLaserSlotCutout(self, param: CAM.Move) -> CAM.LaserSlotCutout:
        ...
    def CreateLaserHexagonCutout(self, param: CAM.Move) -> CAM.LaserHexagonCutout:
        ...
    def CreateLaserProfileMove(self, param: CAM.Move) -> CAM.LaserProfileMove:
        ...
    def CreateRobotCartesianMove(self, param: CAM.Move) -> CAM.RobotCartesianMove:
        ...
    def CreateRobotPoseMove(self, param: CAM.Move) -> CAM.RobotPoseMove:
        ...
    def CreateRobotMountMove(self, param: CAM.Move) -> CAM.RobotMountMove:
        ...
    def CreateContainerMoveBuilder(self, param: CAM.Move, moveType: int) -> CAM.ContainerMoveBuilder:
        ...
    def CreateToolChangePositionBuilder(self, param: CAM.Move) -> CAM.ToolChangePositionBuilder:
        ...
    def CreateMachineLimitMoveBuilder(self, param: CAM.Move) -> CAM.MachineLimitMoveBuilder:
        ...
    def CreateAngularCircularMoveBuilder(self, param: CAM.Move) -> CAM.AngularAboutAxisMoveBuilder:
        ...
    def CreateAngularHelicalMoveBuilder(self, param: CAM.Move) -> CAM.AngularAboutAxisMoveBuilder:
        ...
    def CreateAngularSpiralMoveBuilder(self, param: CAM.Move) -> CAM.AngularAboutAxisMoveBuilder:
        ...
    def CreateAngularConicalMoveBuilder(self, param: CAM.Move) -> CAM.AngularAboutAxisMoveBuilder:
        ...
    def CreateLinearGoDeltaMoveBuilder(self, param: CAM.Move) -> CAM.LinearLocalCsysMoveBuilder:
        ...
    def CreateLinearGotoMoveBuilder(self, param: CAM.Move) -> CAM.LinearLocalCsysMoveBuilder:
        ...
    def Tag(self) -> Tag: ...



class MoveBuilder(Builder):
    def __init__(self) -> None: ...
    def SetParent(self, parent: CAM.CAMObject) -> None:
        ...
    def SetSibling(self, sibling: CAM.CAMObject) -> None:
        ...
    def GetUserParameter(self, parameterName: str) -> CAM.UdeParameter:
        ...
    def GetUserParameter(self, index: int) -> CAM.UdeParameter:
        ...
    FeedRate: float
    FeedType: CAM.MoveBuilder.Feed
    FeedUnit: CAM.FeedRateUnit
    MotionType: CAM.MoveBuilder.Motion
    NumberOfUserParameters: int
    ProtectedMove: bool
    SubopLabel: str


    class Motion(enum.Enum):
        Rapid = 1
        Engage = 2
        Cut = 3
        Stepover = 4
        Retract = 5
        Approach = 6
        Traversal = 7
        Departure = 8
        Return = 9
        FirstCut = 10
        LastCut = 11
        Crossover = 12
    

    class Feed(enum.Enum):
        Motion = 0
        Custom = 1
    

class Move(CAM.CAMObject):
    def __init__(self) -> None: ...


class MirrorBuilder(Builder):
    def __init__(self) -> None: ...
    GenerateToolPath: bool
    GeometryGroup: CAM.NCGroup
    MaintainCutAngle: bool
    MaintainCutDirection: bool
    Plane: Plane
    ProgramGroup: CAM.NCGroup


class MinCutVolume(TaggedObject):
    def __init__(self) -> None: ...
    SuppressBasedOnVolume: bool
    VolumeThreshold: float


class MinCutLength(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    Status: CAM.MinCutLength.Types


    class Types(enum.Enum):
        None = 0
        Specify = 1
    

class MinCutDepth(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    Status: CAM.MinCutDepth.Types


    class Types(enum.Enum):
        None = 0
        Specify = 1
    

class MillVolumeGeomBuilder(CAM.MillGeomBuilder):
    def __init__(self) -> None: ...


class MillUserDefinedBuilder(CAM.UserDefinedOprBuilder):
    def __init__(self) -> None: ...


class MillUserDefined(CAM.UserDefinedOpr):
    def __init__(self) -> None: ...


class MillToolProbingBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder
    ProbeParamsBuilder: CAM.ProbeParamsBuilder


class MillToolProbing(CAM.Operation):
    def __init__(self) -> None: ...


class MillToolBuilder(CAM.MillingToolBuilder):
    def __init__(self) -> None: ...
    ChamferLengthBuilder: CAM.InheritableDoubleBuilder
    CutterSubtype: CAM.MillToolBuilder.CutterSubtypes
    TlCor1RadBuilder: CAM.InheritableDoubleBuilder
    TlCor2RadBuilder: CAM.InheritableDoubleBuilder
    TlTipAngBuilder: CAM.InheritableDoubleBuilder
    TlXcenCor1Builder: CAM.InheritableDoubleBuilder
    TlXcenCor2Builder: CAM.InheritableDoubleBuilder
    TlYcenCor1Builder: CAM.InheritableDoubleBuilder
    TlYcenCor2Builder: CAM.InheritableDoubleBuilder


    class CutterSubtypes(enum.Enum):
        Mill5 = 1
        Mill7 = 2
        Mill10 = 3
        MillBall = 4
        ChamferTool = 5
        SphericalMill = 6
    

class MillTextGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...


class MillOrientGeomBuilder(CAM.OrientGeomBuilder):
    def __init__(self) -> None: ...
    def GetLowerLimitMode(self) -> CAM.MillOrientGeomBuilder.LowerLimitModes:
        ...
    def SetLowerLimitMode(self, lowerLimitMode: CAM.MillOrientGeomBuilder.LowerLimitModes) -> None:
        ...
    LowerLimitPlane: NXObject
    TransferAvoidanceFromBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceGohomeBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceReturnBuilder: CAM.NcmAvoidancePointBuilder
    TransferAvoidanceStartBuilder: CAM.NcmAvoidancePointBuilder
    TransferClearanceBuilder: CAM.NcmClearanceBuilder


    class LowerLimitModes(enum.Enum):
        None = 0
        Plane = 1
    

class MillOperationBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    CutParameters: CAM.MillCutParameters
    FeedsBuilder: CAM.FeedsBuilder
    MinCutLength: CAM.InheritableToolDepBuilder
    MotionOutput: CAM.ArcOutputTypeCiBuilder
    ReferenceTool: CAM.Tool
    WallCleanupType: CAM.MillOperationBuilder.WallCleanupTypes


    class WallCleanupTypes(enum.Enum):
        None = 0
        AtStart = 1
        AtEnd = 2
        Automatic = 3
    

class MillOperation(CAM.Operation):
    def __init__(self) -> None: ...


class MillMethodBuilder(CAM.MethodBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder


class MillMachineControlBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder
    UdeSet: CAM.UdeSet


class MillMachineControl(CAM.Operation):
    def __init__(self) -> None: ...


class MillingTrackpointBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, inputIndex: int, name: str, diameter: float, distance: float, zOffset: float, zOffsetUsed: int, adjust: int, adjustUsed: int, cutcom: int, cutcomUsed: int, newName: str) -> int:
        """[Obsolete("Deprecated in NX10.0.0.  Use new version with additional arguments instead.")"""
        ...
    def Modify(self, index: int, name: str, diameter: float, distance: float, zOffset: float, zOffsetUsed: int, adjust: int, adjustUsed: int, cutcom: int, cutcomUsed: int) -> str:
        """[Obsolete("Deprecated in NX10.0.0.  Use new version with additional arguments instead.")"""
        ...
    def Delete(self, index: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...
    def Get(self, pointTag: NXObject, name: str, diameter: float, distance: float, zOffset: float, zOffsetUsed: int, adjust: int, adjustUsed: int, cutcom: int, cutcomUsed: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use new version _tp with additional arguments instead.")"""
        ...
    def GetTrackPoint(self, position: int) -> NXObject:
        ...
    def Add(self, inputIndex: int, name: str, definitionType: int, diameter: float, distance: float, zOffset: float, zOffsetUsed: int, adjust: int, adjustUsed: int, cutcom: int, cutcomUsed: int, newName: str) -> int:
        ...
    def Modify(self, index: int, name: str, definitionType: int, diameter: float, distance: float, zOffset: float, zOffsetUsed: int, adjust: int, adjustUsed: int, cutcom: int, cutcomUsed: int) -> str:
        ...
    def GetTrackPoint(self, pointTag: NXObject, name: str, definitionType: int, diameter: float, distance: float, zOffset: float, zOffsetUsed: int, adjust: int, adjustUsed: int, cutcom: int, cutcomUsed: int) -> None:
        ...
    def CalculateDistance(self, definitionType: int, diameter: float) -> float:
        ...
    NumberOfTrackPoints: int


    class Types(enum.Enum):
        Full = 0
        ByDiameter = 1
    

class MillingToolBuilder(CAM.ToolBuilder):
    def __init__(self) -> None: ...
    CoolantThrough: bool
    HelicalDiameter: CAM.InheritableToolDepBuilder
    HelicalRampAngle: CAM.InheritableDoubleBuilder
    HolderSectionBuilder: CAM.HolderSectionBuilder
    MaxCutWidth: CAM.InheritableToolDepBuilder
    MillingTrackpointBuilder: CAM.MillingTrackpointBuilder
    MinRampLength: CAM.InheritableToolDepBuilder
    TaperedShankDiameterBuilder: CAM.InheritableDoubleBuilder
    TaperedShankLengthBuilder: CAM.InheritableDoubleBuilder
    TaperedShankTaperLengthBuilder: CAM.InheritableDoubleBuilder
    TlAdjRegBuilder: CAM.InheritableIntBuilder
    TlCutcomReg: int
    TlCutcomRegBuilder: CAM.InheritableIntBuilder
    TlDiameterBuilder: CAM.InheritableDoubleBuilder
    TlDirection: CAM.MillingToolBuilder.ToolDirectionTypes
    TlFluteLnBuilder: CAM.InheritableDoubleBuilder
    TlHeightBuilder: CAM.InheritableDoubleBuilder
    TlHolderDescription: str
    TlHolderLibref: str
    TlLowCorRadBuilder: CAM.InheritableDoubleBuilder
    TlNumFlutesBuilder: CAM.InheritableIntBuilder
    TlShankDiaBuilder: CAM.InheritableDoubleBuilder
    TlTaperAngBuilder: CAM.InheritableDoubleBuilder
    TlUpCorRadBuilder: CAM.InheritableDoubleBuilder
    TlZMountBuilder: CAM.InheritableDoubleBuilder
    TlZOffsetBuilder: CAM.InheritableDoubleBuilder
    UseTaperedShank: bool


    class ToolDirectionTypes(enum.Enum):
        None = 0
        Clw = 1
        Cclw = 2
    

class MillGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    BlankGeometry: CAM.GeometryGroup
    CheckGeometry: CAM.Geometry
    PartGeometry: CAM.Geometry


class MillFormToolBuilder(CAM.MillingToolBuilder):
    def __init__(self) -> None: ...
    Segments: CAM.UdtSectionBuilder


class MillCutParameters(CAM.CutParameters):
    def __init__(self) -> None: ...
    AcrossVoids: CAM.AcrossVoids
    ActionWhenGouging: CAM.CutParametersActionWhenGougingTypes
    AdjacentBlades: CAM.CutParametersAdjacentBladesTypes
    AllowUndercutting: bool
    ApplyToLastPass: bool
    BladeStock: CAM.InheritableDoubleBuilder
    BlankDistance: CAM.InheritableDoubleBuilder
    BlankOverhang: CAM.InheritableToolDepBuilder
    BlankStock: CAM.InheritableDoubleBuilder
    BlendStock: CAM.InheritableDoubleBuilder
    BoundaryApproximation: bool
    BoundaryInTol: float
    BoundaryOutTol: float
    BoundaryStock: float
    CheckStock: CAM.InheritableDoubleBuilder
    CleanupOutput: CAM.CleanupOutput
    CleanupSettings: CAM.CleanupSettings
    CornerControl: CAM.CornerControlBuilder
    CornerFindingOptions: CAM.CutParametersCornerFindingTypes
    CutAngle: CAM.CutAngle
    CutAreaExtensionDistance: CAM.InheritableToolDepBuilder
    CutBelowOverhangingBlank: bool
    CutBelowToolContact: bool
    CutBetweenLevels: bool
    CutDirection: CAM.CutDirection
    CutOrder: CAM.CutParametersCutOrderTypes
    CutWallsOnly: bool
    ExtendAcrossUndercut: bool
    ExtendAtEdges: CAM.ExtendAtEdges
    ExtendFloorTo: CAM.CutParametersExtendFloorTypes
    ExtendToPart: bool
    FinishPasses: CAM.FinishPassesBuilder
    FloorSameAsPartStock: bool
    FloorStock: CAM.InheritableDoubleBuilder
    FollowCheck: bool
    FromLeadingEdge: CAM.InheritableToolDepBuilder
    FromTrailingEdge: CAM.InheritableToolDepBuilder
    GlobalOptimization: bool
    HubStock: CAM.InheritableDoubleBuilder
    IncludeBodiesOfSurfaceRegion: bool
    LevelToLevel: CAM.LevelToLevel
    LowerLimit: CAM.LowerLimit
    MaxCutStep: CAM.InheritableToolDepBuilder
    MaxCutTraverse: CAM.MaxCutTraverse
    MergeDistance: CAM.InheritableToolDepBuilder
    MinCutVolume: CAM.MinCutVolume
    MinMaterialThickness: CAM.InheritableDoubleBuilder
    MinimizeNumberOfEngages: bool
    MultiDepthCut: CAM.MultiDepthCut
    OutputUncutRegions: CAM.OutputUncutRegions
    PartStockOffset: CAM.InheritableDoubleBuilder
    PatternDirection: CAM.CutParametersPatternDirectionTypes
    PlungeDirection: CAM.CutParametersPlungeDirectionTypes
    PreventUndercutting: bool
    RegionConnection: bool
    RegionSequencing: CAM.CutParametersRegionSequencingTypes
    RollToolOverEdges: bool
    RotaryMaxAngleLimit: float
    RotaryMinAngleLimit: float
    SelfIntersection: bool
    ShroudStock: CAM.InheritableDoubleBuilder
    SimplifyShapes: CAM.CutParametersSimplifyShapesTypes
    SinglePassOffset: CAM.InheritableToolDepBuilder
    SmallAreaAvoidance: CAM.SmallAreaAvoidance
    SteepContainment: CAM.SteepContainment
    Stepover: CAM.StepoverBuilder
    StepoverLimit: CAM.InheritableDoubleBuilder
    TextDepth: CAM.InheritableDoubleBuilder
    TlaxisBladeRollAngle: float
    TolerantMachining: bool
    ToolAxisChange: CAM.ToolAxisChange
    ToolAxisSmoothing: int
    ToolAxisTilt: CAM.ToolAxisTilt
    ToolRunOff: CAM.InheritableToolDepBuilder
    ToolRunOffType: CAM.CutParametersToolRunOffTypes
    ToolRunOn: CAM.InheritableToolDepBuilder
    ToolpathSmoothing: int
    TraverseOpenPasses: CAM.CutParametersTraverseOpenPassesTypes
    TrimControl: CAM.CutParametersTrimControlTypes
    TrimStock: CAM.InheritableDoubleBuilder
    TrochoidalSettings: CAM.TrochoidalSettings
    UpDownCutting: CAM.UpDownCutting
    UsePrevious2dIpw: bool
    ValleyOverlapDistance: CAM.InheritableDoubleBuilder
    WallStock: CAM.InheritableDoubleBuilder
    ZAxisSmoothing: CAM.ZAxisSmoothing


class MillBoundaryGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    BlankBoundary: CAM.Boundary
    CheckBoundary: CAM.Boundary
    PartBoundary: CAM.Boundary
    TrimBoundary: CAM.Boundary


class MillAreaGeomBuilder(CAM.MillGeomBuilder):
    def __init__(self) -> None: ...
    CutAreaGeometry: CAM.Geometry
    TrimBoundary: CAM.Boundary
    WallGeometry: CAM.Geometry


class MethodBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def GetCutMethod(self) -> str:
        ...
    def SetCutMethod(self, libRef: str) -> None:
        ...
    CutParameters: CAM.CutParameters
    PaintDisplay: CAM.DisplayPaint
    PathDisplay: CAM.DisplayPath
    PathDisplayColors: CAM.PathDisplayColors
    SilhouDisplay: CAM.DisplaySilhouette
    ToolDisplay: CAM.DisplayTool


class Method(CAM.NCGroup):
    def __init__(self) -> None: ...


class MergeSubopCommand(TaggedObject):
    def __init__(self) -> None: ...
    def GetTargetRegions(self) -> int:
        ...
    def SetTargetRegions(self, targets: int) -> None:
        ...
    def GetToolRegions(self) -> int:
        ...
    def SetToolRegions(self, tools: int) -> None:
        ...


class MaxCutTraverse(TaggedObject):
    def __init__(self) -> None: ...
    Distance: CAM.InheritableToolDepBuilder
    FeedOnShortMoves: bool
    Type: CAM.MaxCutTraverse.Types


    class Types(enum.Enum):
        Inactive = 0
        Distance = 1
        PercentToolDiameter = 2
    

class MapFeatureTeaching(CAM.Teaching):
    def __init__(self) -> None: ...
    def GetInputTypeName(self) -> str:
        ...
    def SetInputTypeName(self, name: str) -> None:
        ...
    def GetOutputTypeName(self) -> str:
        ...
    def SetOutputTypeName(self, name: str) -> None:
        ...
    def GetFeature(self) -> CAM.CAMFeature:
        ...
    def SetFeature(self, feature: CAM.CAMFeature) -> None:
        ...
    def AddNewMappingRule(self, name: str) -> None:
        ...
    def Teach(self) -> None:
        ...


class ManualMove(CAM.Move):
    def __init__(self) -> None: ...
    def InsertMove(self, insertedMover: CAM.ManualMove) -> None:
        ...
    def InsertMoveAfter(self, insertAfter: CAM.ManualMove, insertedMove: CAM.ManualMove) -> None:
        ...


class ManualFeatureBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.ManualFeatureBuilder]) -> None:
        ...
    def Append(self, object: CAM.ManualFeatureBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.ManualFeatureBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.ManualFeatureBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.ManualFeatureBuilder) -> None:
        ...
    def Erase(self, obj: CAM.ManualFeatureBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.ManualFeatureBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.ManualFeatureBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.ManualFeatureBuilder, object2: CAM.ManualFeatureBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.ManualFeatureBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ManualFeatureBuilder(Builder):
    def __init__(self) -> None: ...
    FloorFaces: ScCollector
    Name: str
    WallFaces: ScCollector


class ManualControlBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetOperatorMessage(self) -> str:
        ...
    def SetOperatorMessage(self, multiLineText: str) -> None:
        ...
    StopActive: bool


class ManualControl(CAM.Operation):
    def __init__(self) -> None: ...


class ManageToolPartBuilder(Builder):
    def __init__(self) -> None: ...
    def AskR1ToolTipJunction(self, r1ToolTipJunction: NXObject, r1ToolTipTrackingPoint: int) -> None:
        ...
    def UpdateR1ToolTipJunction(self, r1ToolTipJunction: NXObject, r1ToolTipTrackingPoint: int) -> None:
        ...
    def AskToolTipJunction(self, toolTipJunction: NXObject, toolTipTrackingPoint: int, toolTipRadiusId: int) -> None:
        ...
    def UpdateToolTipJunction(self, r1ToolTipJunction: NXObject, toolTipTrackingPoint: int, toolTipRadiusId: int) -> None:
        ...
    def SetToolCutter(self, tagArray: typing.List[NXObject]) -> None:
        ...
    def GetToolCutter(self, tagArray: typing.List[NXObject]) -> None:
        ...
    def GetNumToolCutter(self) -> int:
        ...
    def SetToolNonCuttingObjects(self, tagArray: typing.List[NXObject]) -> None:
        ...
    def GetToolNonCuttingObjects(self, tagArray: typing.List[NXObject]) -> None:
        ...
    def GetNumToolNonCuttingObjects(self) -> int:
        ...
    ExportToggleState: bool
    ToolMountingJunction: NXObject


class MachiningRegionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    EntryEndOffset: float
    EntryStartOffset: float
    ExitEndOffset: float
    ExitStartOffset: float
    RangeDepthType: int
    SidesType: int


class MachiningFeatureGeom(TaggedObject):
    def __init__(self) -> None: ...
    Features: CAM.CAMFeatureList


class MachiningFeature(TaggedObject):
    def __init__(self) -> None: ...
    CoordinateSystem: CoordinateSystem
    Faces: ScCollector
    FeatureType: str
    Features: CAM.CAMFeatureList


class MachineTurretGroupBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    CarrierName: CAM.InheritableTextBuilder
    ChannelName: str
    MctTurrentId: str
    MctTurrentWpl: CartesianCoordinateSystem
    MctTurrentWplType: CAM.MachineTurretGroupBuilder.MctTurrentWplTypes


    class MctTurrentWplTypes(enum.Enum):
        Xy = 0
        Xz = 1
    

class MachinePocketGroupBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def CreateHoldingSystemBuilder(self, position: int, name: str) -> CAM.HoldingSystemBuilder:
        ...
    AdjustIdBuilder: CAM.InheritableIntBuilder
    AdjustRegisterType: CAM.MachinePocketGroupBuilder.RegisterType
    ChannelName: str
    CutcomIdBuilder: CAM.InheritableIntBuilder
    CutcomRegisterType: CAM.MachinePocketGroupBuilder.RegisterType
    HoldingSystemsList: CAM.HoldingSystemBuilderList
    NumberOfTools: int
    PocketIdBuilder: CAM.InheritableIntBuilder
    PocketIdStringBuilder: CAM.InheritableTextBuilder


    class RegisterType(enum.Enum):
        SameAsPocketId = 0
        Specify = 1
    

class MachineLimitMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Location: CAM.MachineLimitMoveBuilder.LocationTypes


    class LocationTypes(enum.Enum):
        Before = 0
        Next = 1
    

class MachineHeadGroupBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    IDirectionBuilder: float
    JDirectionBuilder: float
    KDirectionBuilder: float
    XDistanceBuilder: float
    YDistanceBuilder: float
    ZDistanceBuilder: float


class MachineGroupBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def UpdateToolPathTime(self) -> None:
        ...
    def RemoveMachine(self) -> None:
        ...
    def RemoveKinematics(self) -> None:
        ...
    def UpdateCamSetup(self, retrieveFlag: CAM.MachineGroupBuilder.RetrieveToolPocketInformation, ncmctPartMountingBuilder: CAM.NcmctPartMountingBuilder) -> None:
        ...
    MachinePartOccurrence: Assemblies.Component
    RapidFeed: CAM.InheritableFeedBuilder
    ToolChangeTime: CAM.InheritableDoubleBuilder


    class RetrieveToolPocketInformation(enum.Enum):
        No = 0
        Yes = 1
    

class LowerLimit(TaggedObject):
    def __init__(self) -> None: ...
    Action: CAM.LowerLimit.ActionTypes
    Mode: CAM.LowerLimit.ModeTypes
    Plane: NXObject


    class ModeTypes(enum.Enum):
        UseInherited = 0
        None = 1
        Plane = 2
    

    class ActionTypes(enum.Enum):
        NormalToPlane = 0
        AlongToolAxis = 1
        Warnings = 2
    

class LinearLocalCsysMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    AxisValueX: CAM.ExpressionDouble
    AxisValueY: CAM.ExpressionDouble
    AxisValueZ: CAM.ExpressionDouble


class LevelToLevel(TaggedObject):
    def __init__(self) -> None: ...
    RampAngle: CAM.InheritableDoubleBuilder
    Type: CAM.LevelToLevel.Types


    class Types(enum.Enum):
        UseTransferMethod = 0
        DirectOnPart = 1
        RampOnPart = 2
        StaggerRampOnPart = 3
    

class LeadAngles(TaggedObject):
    def __init__(self) -> None: ...
    AtLeadingEdge: float
    AtTrailingEdge: float
    ControlType: CAM.LeadAngles.ControlTypes


    class ControlTypes(enum.Enum):
        SameAsLeadingToTrailing = 0
        Specify = 1
    

class LayoutCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SaveLayout(self) -> None:
        ...
    LayoutName: str
    LayoutSaveSettings: int


class LatheUserDefinedBuilder(CAM.UserDefinedOprBuilder):
    def __init__(self) -> None: ...


class LatheUserDefined(CAM.UserDefinedOpr):
    def __init__(self) -> None: ...


class LatheMachineControlBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsTurnBuilder
    UdeSet: CAM.UdeSet


class LatheMachineControl(CAM.Operation):
    def __init__(self) -> None: ...


class LaserTool(CAM.SoftTool):
    def __init__(self) -> None: ...
    Diameter: CAM.InheritableDoubleBuilder
    FocalDiameter: CAM.InheritableDoubleBuilder
    FocalDistance: CAM.InheritableDoubleBuilder
    Length: CAM.InheritableDoubleBuilder
    MaxPower: CAM.InheritableDoubleBuilder
    MinPower: CAM.InheritableDoubleBuilder
    TaperLength: CAM.InheritableDoubleBuilder
    TipDiameter: CAM.InheritableDoubleBuilder


class LaserTeachMode(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    Feeds: CAM.FeedsBuilder
    NcmEngage: CAM.NcmLaserEngage
    NcmRetract: CAM.NcmLaserRetract
    OverlapDistance: CAM.InheritableToolDepBuilder


class LaserSlotCutout(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    CutDirection: CAM.LaserCutDirection
    CutoutDefinition: CAM.LaserCutoutDefinition
    HeadOrientation: CAM.LaserHeadOrientation
    PiercingPoint: CAM.LaserPiercingPoint


class LaserRectangleCutout(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    CutDirection: CAM.LaserCutDirection
    CutoutDefinition: CAM.LaserCutoutDefinition
    HeadOrientation: CAM.LaserHeadOrientation
    PiercingPoint: CAM.LaserPiercingPoint


class LaserProfileMove(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    def CreateControlPoint(self, headOrientType: int, pointTag: Point, csysTag: CartesianCoordinateSystem, processType: int, toggle: bool, udePathTag: NXObject, pointType: int) -> CAM.LaserControlPoint:
        ...
    CollisionCheck: CAM.LaserProfileMove.CollisionChecks
    CutDirection: CAM.LaserCutDirection
    HeadOrientation: CAM.LaserHeadOrientation
    InterpMethod: CAM.LaserProfileMove.InterpMethods
    List: CAM.LaserControlPointList
    MaxGapDist: float
    MaxTiltAngle: float
    ProfileSection: Section
    ShapeType: CAM.LaserProfileMove.ShapeTypes
    ToolSide: CAM.LaserProfileMove.ToolSides


    class ToolSides(enum.Enum):
        On = 0
        Left = 1
        Right = 2
    

    class ShapeTypes(enum.Enum):
        ExternalTrim = 0
        InternalTrim = 1
        OpenProfile = 2
    

    class InterpMethods(enum.Enum):
        Linear = 0
        CubicSpline = 1
        Smooth = 2
    

    class CollisionChecks(enum.Enum):
        None = 0
        NozzleOnly = 1
        NozzleAndHolder = 2
        SolidLaserHead = 3
    

class LaserPiercingPoint(TaggedObject):
    def __init__(self) -> None: ...
    Point: Point
    PointType: CAM.LaserPiercingPoint.Types


    class Types(enum.Enum):
        None = 0
        Specify = 1
    

class LaserMethod(CAM.MethodBuilder):
    def __init__(self) -> None: ...
    CutGasPressure: CAM.InheritableDoubleBuilder
    CutGasType: CAM.InheritableIntBuilder
    CutLaserDelay: CAM.InheritableDoubleBuilder
    CutLaserFrequency: CAM.InheritableDoubleBuilder
    CutLaserPower: CAM.InheritableDoubleBuilder
    Feeds: CAM.FeedsBuilder
    PierceGasPressure: CAM.InheritableDoubleBuilder
    PierceGasType: CAM.InheritableIntBuilder
    PierceLaserDelay: CAM.InheritableDoubleBuilder
    PierceLaserFrequency: CAM.InheritableDoubleBuilder
    PierceLaserPower: CAM.InheritableDoubleBuilder


class LaserLinearMove(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    DeltaXc: float
    DeltaXm: float
    DeltaYc: float
    DeltaYm: float
    DeltaZc: float
    DeltaZm: float
    Distance: float
    HeadOrientation: CAM.LaserHeadOrientation
    MotionEnd: CAM.LaserLinearMove.MotionEnds
    MoveType: CAM.LaserLinearMove.MoveTypes
    Point: Point
    RefType: CAM.LaserLinearMove.RefTypes
    Vector: Direction


    class RefTypes(enum.Enum):
        Wcs = 0
        Mcs = 1
    

    class MoveTypes(enum.Enum):
        Direct = 0
        ZmXmYm = 1
        ZmYmXm = 2
        XmYmZm = 3
        XmZmYm = 4
        YmZmXm = 5
        YmXmZm = 6
    

    class MotionEnds(enum.Enum):
        Point = 0
        Delta = 1
        AlongToolAxis = 2
        AlongVector = 3
    

class LaserHexagonCutout(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    CutDirection: CAM.LaserCutDirection
    CutoutDefinition: CAM.LaserCutoutDefinition
    HeadOrientation: CAM.LaserHeadOrientation
    PiercingPoint: CAM.LaserPiercingPoint


class LaserHeadOrientation(TaggedObject):
    def __init__(self) -> None: ...
    Csys: CartesianCoordinateSystem
    OrientationType: CAM.LaserHeadOrientation.Types


    class Types(enum.Enum):
        NoChange = 0
        McsZy = 1
        Specify = 2
        Dynamic = 3
        NormalToPart = 4
    

class LaserCutoutDefinition(TaggedObject):
    def __init__(self) -> None: ...
    Angle: float
    CenterPoint: Point
    CornerRadius: float
    CutoutDefType: CAM.LaserCutoutDefinition.Types
    CutoutSection: Section
    Diameter: float
    Length: float
    Width: float
    WrenchSize: float


    class Types(enum.Enum):
        Geometry = 0
        Dimensions = 1
    

class LaserCutDirection(TaggedObject):
    def __init__(self) -> None: ...
    CutDirType: CAM.LaserCutDirection.Types


    class Types(enum.Enum):
        Cclw = 0
        Clw = 1
    

class LaserControlPointList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.LaserControlPoint]) -> None:
        ...
    def Append(self, object: CAM.LaserControlPoint) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.LaserControlPoint) -> int:
        ...
    def FindItem(self, index: int) -> CAM.LaserControlPoint:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.LaserControlPoint) -> None:
        ...
    def Erase(self, obj: CAM.LaserControlPoint, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.LaserControlPoint]:
        ...
    def SetContents(self, objects: typing.List[CAM.LaserControlPoint]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.LaserControlPoint, object2: CAM.LaserControlPoint) -> None:
        ...
    def Insert(self, location: int, object: CAM.LaserControlPoint) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class LaserControlPoint(TaggedObject):
    def __init__(self) -> None: ...
    Csys: CartesianCoordinateSystem
    EventFlag: bool
    LocalHeadOrientType: CAM.LaserControlPoint.HeadOrientTypes
    Point: Point
    ProcessType: CAM.LaserControlPoint.ProcessTypes
    UdeSet: CAM.UdeSet


    class ProcessTypes(enum.Enum):
        ProjectToToolPath = 0
        DriveToPoint = 1
    

    class HeadOrientTypes(enum.Enum):
        None = 0
        Specify = 1
        Dynamic = 2
    

    class ControlPointTypes(enum.Enum):
        Sys = 0
        Adj = 1
        Coll = 2
        Mod = 3
        User = 4
    

class LaserCircleCutout(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    CutDirection: CAM.LaserCutDirection
    CutoutDefinition: CAM.LaserCutoutDefinition
    HeadOrientation: CAM.LaserHeadOrientation
    PiercingPoint: CAM.LaserPiercingPoint


class IpwContainmentCurvesBuilder(Builder):
    def __init__(self) -> None: ...
    FeatureName: str
    SmoothingTolerance: float
    SpecifyDistance: float
    SpecifyPoint: Point
    ThicknessMode: CAM.IpwContainmentCurvesBuilder.ThicknessModeValue


    class ThicknessModeValue(enum.Enum):
        Point = 0
        Distance = 1
    

class IpwAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateIpwContainmentCurvesBuilder(self, position: int) -> CAM.IpwContainmentCurvesBuilder:
        ...
    ColorControlType: CAM.IpwAnalysisBuilder.ColorControl


    class ColorControl(enum.Enum):
        Sharp = 0
        Blend = 1
    

class IntStatusData():
    Value: int
    Inheritance: CAM.Inheritance
    def ToString(self) -> str:
        ...
    def __init__(self, Value: int, Inheritance: CAM.Inheritance) -> None: ...


class InterpolateVector(CAM.ToolAxisInterpolate):
    def __init__(self) -> None: ...
    def Insert(self, inputIndex: int, point: Point, view: NXObject, vector: Direction) -> None:
        ...
    def Modify(self, index: int, point: Point, vector: Direction) -> None:
        ...
    def Modify(self, index: int, point: Point, vector: Direction, ignorePoint: bool) -> None:
        ...
    def Erase(self, index: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...
    def GetVector(self, index: int) -> Direction:
        ...
    def GetLeadAngle(self, index: int) -> float:
        ...
    def SetLeadAngle(self, index: int, leadAngle: float) -> None:
        ...
    def GetTiltAngle(self, index: int) -> float:
        ...
    def SetTiltAngle(self, index: int, tiltAngle: float) -> None:
        ...
    def GetPreviewMaximumDistanceBuilder(self) -> CAM.InheritableToolDepBuilder:
        ...
    ApplyLeadTilt: bool
    MinimumLeadAngle: float
    SmoothingMethod: int
    TiltAngle: float


class InterpolateAngle(CAM.ToolAxisInterpolate):
    def __init__(self) -> None: ...
    def Insert(self, inputIndex: int, point: Point, view: NXObject, leadAngle: float, tiltAngle: float) -> None:
        ...
    def Modify(self, index: int, point: Point, tiltAngle: float, leadAngle: float) -> None:
        ...
    def Modify(self, index: int, point: Point, tiltAngle: float, leadAngle: float, ignorePoint: bool) -> None:
        ...
    def Erase(self, index: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...
    def GetTiltAngle(self, index: int) -> float:
        ...
    def GetLeadAngle(self, index: int) -> float:
        ...


class InspectionUVGridBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    def SetLayoutChanged(self, flag: bool) -> None:
        ...
    def SetPointCoverageChanged(self, flag: bool) -> None:
        ...
    def SetAppDistChanged(self, flag: bool) -> None:
        ...
    def SetRetDistChanged(self, flag: bool) -> None:
        ...
    def SetPointSequenceChanged(self, flag: bool) -> None:
        ...
    def CopyAttributes(self, target: CAM.InspectionUVGridBuilder) -> None:
        ...
    AlignMachineAxes: bool
    ApproachDist: CAM.InheritableDoubleBuilder
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    EndU: CAM.InheritableDoubleBuilder
    EndUDeg: CAM.InheritableDoubleBuilder
    EndUDist: CAM.InheritableDoubleBuilder
    EndUMode: CAM.InspectionMethodBuilder.UVModeTypes
    EndUSweep: CAM.InheritableDoubleBuilder
    EndV: CAM.InheritableDoubleBuilder
    EndVDeg: CAM.InheritableDoubleBuilder
    EndVDist: CAM.InheritableDoubleBuilder
    EndVMode: CAM.InspectionMethodBuilder.UVModeTypes
    EndVSweep: CAM.InheritableDoubleBuilder
    MeasuredGeometry: NXObject
    NumberOfUPoints: CAM.InheritableIntBuilder
    NumberOfVPoints: CAM.InheritableIntBuilder
    NumberOfValidPoints: int
    PointSequenceDirection: CAM.InspectionMethodBuilder.PointSequenceDirectionTypes
    PointSequenceMode: CAM.InspectionMethodBuilder.PointSequenceModeTypes
    PointSequenceStart: CAM.InspectionMethodBuilder.PointSequenceStartTypes
    RetractDist: CAM.InheritableDoubleBuilder
    SearchDist: CAM.InheritableDoubleBuilder
    SequenceOptimization: CAM.InspectionPathBuilder.SequenceType
    SphereAxisMethod: CAM.InspectionUVGridBuilder.SphereAxisType
    SphereAxisVector: Direction
    StartPointMode: CAM.InspectionUVGridBuilder.StartPointType
    StartU: CAM.InheritableDoubleBuilder
    StartUDeg: CAM.InheritableDoubleBuilder
    StartUDist: CAM.InheritableDoubleBuilder
    StartUMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartUSweep: CAM.InheritableDoubleBuilder
    StartV: CAM.InheritableDoubleBuilder
    StartVDeg: CAM.InheritableDoubleBuilder
    StartVDist: CAM.InheritableDoubleBuilder
    StartVMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartVSweep: CAM.InheritableDoubleBuilder
    UseFeatureCollisionAvoidance: bool
    UsePartCollisionAvoidance: bool


    class StartPointType(enum.Enum):
        Nearest = 0
        UminVmin = 1
        UmaxVmin = 2
        UminVmax = 3
        UmaxVmax = 4
    

    class SphereAxisType(enum.Enum):
        AlignWithProbe = 0
        SelectDirection = 1
        SetupZAxis = 2
    

class InspectionTrackPointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.TrackPoint]:
        ...
    def __init__(self, owner: CAM.InspectionTool) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.TrackPoint:
        ...
    def Tag(self) -> Tag: ...



class InspectionTorusFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipAxisDirection(self) -> None:
        ...
    AxisDirectionI: float
    AxisDirectionJ: float
    AxisDirectionK: float
    CenterPointX: float
    CenterPointY: float
    CenterPointZ: float
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    InnerOuterType: CAM.CamInspectionOperationInneroutertypes
    MajorRadius: float
    MinorRadius: float
    Name: str
    ReverseDirection: bool
    SelectedTorus: SelectNXObject


class InspectionTool(CAM.InspectionGroup):
    def __init__(self) -> None: ...
    def CreateProbeTrackingBuilder(self, csoObject: CAM.ProbeTrackPoint) -> CAM.ProbeTrackingBuilder:
        ...
    def CreateInspectionProbeTrackingBuilder(self, csoObject: CAM.ProbeTrackPoint) -> CAM.InspectionProbeTrackingBuilder:
        ...
    CMMInspectionTrackPointCollection: CAM.InspectionTrackPointCollection


class InspectionToleranceOperationBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParameters(self) -> None:
        ...
    CompositeToleranceValueSource: CAM.InspectionToleranceOperationBuilder.ToleranceSource
    DatumPlaneFittingModeBuilder: CAM.InspectionDatumPlaneFittingModeBuilder
    DirVec: Direction
    DofCsysMode: CAM.InspectionMethodBuilder.ToleranceDegreeOfFreedomCsysMode
    DoubleDirVecI: float
    DoubleDirVecJ: float
    DoubleDirVecK: float
    DoubleLower: float
    DoubleLowerParamOuterProfile: float
    DoubleNominal: float
    DoubleParamExtArea: float
    DoubleParamExtLength: float
    DoubleParamOuterProfile: float
    DoubleParamTolValue: float
    DoubleParamTolValue1: float
    DoubleUpper: float
    DoubleViewVecI: float
    DoubleViewVecJ: float
    DoubleViewVecK: float
    EnumPCSABS: CAM.InspectionToleranceOperationBuilder.SirVecPCSABS
    EnumParamPriMatModifier: CAM.InspectionToleranceOperationBuilder.ParamPriDatumModifier
    EnumParamPriMatModifier1: CAM.InspectionToleranceOperationBuilder.ParamPriDatumModifier
    EnumParamSecMatModifier: CAM.InspectionToleranceOperationBuilder.ParamSecDatumModifier
    EnumParamSecMatModifier1: CAM.InspectionToleranceOperationBuilder.ParamSecDatumModifier
    EnumParamSubType: CAM.InspectionToleranceOperationBuilder.ParamSubType
    EnumParamTerMatModifier: CAM.InspectionToleranceOperationBuilder.ParamTerDatumModifier
    EnumParamTerMatModifier1: CAM.InspectionToleranceOperationBuilder.ParamTerDatumModifier
    EnumParamTolDistbCalcMode: CAM.InspectionToleranceOperationBuilder.ParamTolDistbCalcMode
    EnumParamTolMatModifier: CAM.InspectionToleranceOperationBuilder.ParamTolMatModifier
    EnumParamTolMatModifier1: CAM.InspectionToleranceOperationBuilder.ParamTolMatModifier
    EnumParamTolMatModifierDup: CAM.InspectionToleranceOperationBuilder.ParamTolMatModifierDup
    EnumParamTolZoneShape: CAM.InspectionToleranceOperationBuilder.ParamTolZoneShape
    EnumParamTolZoneShape1: CAM.InspectionToleranceOperationBuilder.ParamTolZoneShape
    EnumParamXYZAxis: CAM.InspectionToleranceOperationBuilder.ParamXYZAxis
    EnumParameterExtent: CAM.InspectionToleranceOperationBuilder.ParamExtent
    EnumTorusCharacteristic: CAM.InspectionToleranceOperationBuilder.ParamXYZAxis
    IsAlignVector: bool
    IsComposite: bool
    LimitsOfSizeModeBuilder: CAM.InspectionLimitsOfSizeModeBuilder
    LowerDMS: str
    LowerSource: CAM.InspectionToleranceOperationBuilder.ToleranceSource
    NominalDMS: str
    NominalSource: CAM.InspectionToleranceOperationBuilder.ToleranceSource
    ProfileDispositionModeBuilder: CAM.InspectionProfileDispositionModeBuilder
    SelectionFeature: SelectNXObject
    SelectionOriginFeature: SelectNXObject
    SelectionPMI: SelectNXObject
    SelectionTolerancedFeature: SelectNXObject
    StringDatumFeatName: str
    StringDatumLetter: str
    StringOriginFeatName: str
    StringPriDatum: str
    StringPriDatum1: str
    StringSecDatum: str
    StringSecDatum1: str
    StringTerDatum: str
    StringTerDatum1: str
    StringTolName: str
    StringTolerancedFeat: str
    SurfaceProfileModeBuilder: CAM.InspectionSurfaceProfileModeBuilder
    TolOpType: CAM.InspectionToleranceOperationBuilder.TolType
    ToleranceValueSource: CAM.InspectionToleranceOperationBuilder.ToleranceSource
    UpperDMS: str
    UpperSource: CAM.InspectionToleranceOperationBuilder.ToleranceSource
    UseDegMin: CAM.InspectionToleranceOperationBuilder.AngleFormat
    VectorDirection: Direction
    VectorViewVec: Direction
    XRotationDOFMode: CAM.InspectionMethodBuilder.ToleranceDegreeOfFreedomMode
    XRotationLowerLimit: float
    XRotationUpperLimit: float
    XTranslationDOFMode: CAM.InspectionMethodBuilder.ToleranceDegreeOfFreedomMode
    XTranslationLowerLimit: float
    XTranslationUpperLimit: float
    YRotationDOFMode: CAM.InspectionMethodBuilder.ToleranceDegreeOfFreedomMode
    YRotationLowerLimit: float
    YRotationUpperLimit: float
    YTranslationDOFMode: CAM.InspectionMethodBuilder.ToleranceDegreeOfFreedomMode
    YTranslationLowerLimit: float
    YTranslationUpperLimit: float
    ZRotationDOFMode: CAM.InspectionMethodBuilder.ToleranceDegreeOfFreedomMode
    ZRotationLowerLimit: float
    ZRotationUpperLimit: float
    ZTranslationDOFMode: CAM.InspectionMethodBuilder.ToleranceDegreeOfFreedomMode
    ZTranslationLowerLimit: float
    ZTranslationUpperLimit: float


    class TolType(enum.Enum):
        DistanceBetween = 0
        AngleBetween = 1
        CoordinateTolerance = 2
        Diameter = 3
        Radius = 4
        Width = 5
        ConeAngle = 6
        DatumDefinition = 7
        Flatness = 8
        Straightness = 9
        Circularity = 10
        Cylindricity = 11
        LineProfile = 12
        SurfaceProfile = 13
        Angularity = 14
        Parallelism = 15
        Perpendicularity = 16
        Position = 17
        Concentricity = 18
        Symmetry = 19
        CircularRunout = 20
        TotalRunout = 21
        DatumTarget = 22
    

    class ToleranceSource(enum.Enum):
        Unknown = 0
        Pmi = 1
        CheckedGdt = 2
        Geometry = 3
        TwoDAnnot = 4
        User = 5
    

    class SirVecPCSABS(enum.Enum):
        RelativetoPCS = 0
        Absolute = 1
    

    class ParamXYZAxis(enum.Enum):
        XAxis = 0
        YAxis = 1
        ZAxis = 2
        MajorAxis = 3
        MinorAxis = 4
    

    class ParamTolZoneShape(enum.Enum):
        None = 0
        Cylindrical = 1
        Circular = 2
        Spherical = 3
        Radial = 4
        Angular = 5
    

    class ParamTolMatModifierDup(enum.Enum):
        None = 0
        Mmc = 1
        Lmc = 2
        Rfs = 3
    

    class ParamTolMatModifier(enum.Enum):
        None = 0
        Mmc = 1
        Lmc = 2
        Rfs = 3
    

    class ParamTolDistbCalcMode(enum.Enum):
        Average = 0
        Minimum = 1
        Maximum = 2
    

    class ParamTerDatumModifier(enum.Enum):
        None = 0
        Mmc = 1
        Lmc = 2
        Rfs = 3
    

    class ParamTerDatum(enum.Enum):
        A = 0
        B = 1
        C = 2
    

    class ParamSubType(enum.Enum):
        Surface = 0
        Axis = 1
    

    class ParamSecDatumModifier(enum.Enum):
        None = 0
        Mmc = 1
        Lmc = 2
        Rfs = 3
    

    class ParamSecDatum(enum.Enum):
        A = 0
        B = 1
        C = 2
    

    class ParamPriDatumModifier(enum.Enum):
        None = 0
        Mmc = 1
        Lmc = 2
        Rfs = 3
    

    class ParamPriDatum(enum.Enum):
        A = 0
        B = 1
        C = 2
    

    class ParamExtent(enum.Enum):
        Total = 0
        UnitAreaLength = 1
    

    class AngleFormat(enum.Enum):
        DecimalDegree = 0
        DegMinSec = 1
    

class InspectionSurfaceProfileModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMethodBuilder.SurfaceProfileTypes


class InspectionSurfaceFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def PreviewPointData(self, showExisting: bool) -> None:
        ...
    def ErasePointDefinitionDisplay(self) -> None:
        ...
    EndUDistance: float
    EndUPercent: float
    EndVDistance: float
    EndVPercent: float
    IsPointDefinitionChanged: bool
    Name: str
    NumberOfUPoints: int
    NumberOfVPoints: int
    PointDataDefinition: CAM.InspectionSurfaceFeatureBuilder.PointDataDefinitionType
    PointSelector: SelectPointList
    ReverseDirection: bool
    SelectedFace: SelectFace
    StartUDistance: float
    StartUPercent: float
    StartVDistance: float
    StartVPercent: float
    UStartEndMode: CAM.InspectionSurfaceFeatureBuilder.StartEndModeType
    VStartEndMode: CAM.InspectionSurfaceFeatureBuilder.StartEndModeType


    class StartEndModeType(enum.Enum):
        Percentage = 0
        Distance = 1
    

    class PointDataDefinitionType(enum.Enum):
        None = 0
        PointSet = 1
        IndividualPoints = 2
    

class InspectionSphereFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    CenterPointX: float
    CenterPointY: float
    CenterPointZ: float
    CsysRefType: CAM.CamInspectionOperationCsysreferencetypes
    Diameter: float
    InnerOuterType: CAM.CamInspectionOperationInneroutertypes
    Name: str
    SelectSphere: SelectNXObject


class InspectionSetup(CAM.CAMObject):
    def __init__(self) -> None: ...
    def Postprocess(self, objects: typing.List[CAM.CAMObject], machineType: str, outfileName: str, outputUnits: CAM.CAMSetup.OutputUnits) -> None:
        ...
    def PostprocessWithSetting(self, objects: typing.List[CAM.CAMObject], machineType: str, outfileName: str, outputUnits: CAM.CAMSetup.OutputUnits, outputWarning: CAM.CAMSetup.PostprocessSettingsOutputWarning, reviewTool: CAM.CAMSetup.PostprocessSettingsReviewTool) -> None:
        ...
    def CutObjects(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject]) -> None:
        ...
    def MoveObjects(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject], destinationObject: CAM.CAMObject, pastePosition: CAM.CAMSetup.Paste) -> None:
        ...
    def PasteObjects(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject], destinationObject: CAM.CAMObject, pastePosition: CAM.CAMSetup.Paste) -> None:
        ...
    def BufferObjects(self, view: CAM.CAMSetup.View, objectsToBeBuffered: typing.List[CAM.CAMObject]) -> None:
        ...
    def CopyObjects(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject], destinationObject: CAM.CAMObject, pastePosition: CAM.CAMSetup.Paste) -> typing.List[CAM.CAMObject]:
        ...
    def GenerateToolPath(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def SetTemplateStatus(self, objects: typing.List[CAM.CAMObject], useAsParent: bool, createIfParentCreated: bool) -> None:
        ...
    def RetrieveTool(self, libRef: str, success: bool) -> CAM.InspectionTool:
        ...
    def RetrieveTool(self, libRef: str, target: CAM.CAMObject, nextTarget: CAM.CAMObject, success: bool) -> CAM.InspectionTool:
        ...
    def LockToolPaths(self, objects: typing.List[CAM.CAMObject], lock: bool) -> None:
        ...
    def CreateNcmctPartMountingBuilder(self, libRef: str) -> CAM.NcmctPartMountingBuilder:
        ...
    def RetrieveDevice(self, libRef: str) -> CAM.InspectionGroup:
        ...
    def ResequencePaths(self, paths: typing.List[CAM.CAMObject]) -> None:
        ...
    def ResequenceTols(self, tols: typing.List[CAM.CAMObject]) -> None:
        ...
    def RetrievePathMessages(self, objects: typing.List[CAM.CAMObject]) -> str:
        ...
    def CreateObjectsUdeSet(self, params: typing.List[CAM.CAMObject], udeType: CAM.CAMSetup.Ude) -> CAM.ObjectsUdeSet:
        ...
    def GetRoot(self, branch: CAM.CAMSetup.View) -> CAM.InspectionGroup:
        ...
    def UpdateFeatureNames(self, originalFeatName: str, newFeatName: str) -> None:
        ...
    def UpdateToleranceNames(self, originalTolName: str, newTolName: str) -> None:
        ...
    CmmInspectionGroupCollection: CAM.InspectionGroupCollection
    CmmInspectionOperationCollection: CAM.InspectionOperationCollection


class InspectionSensorStrategyBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMoveBuilder.SensorStrategyTypes


class InspectionSensorMassEditBuilder(Builder):
    def __init__(self) -> None: ...
    AngleA: float
    AngleB: float
    SensorName: str
    SensorStrategy: CAM.InspectionSensorMassEditBuilder.SensorStrategyType
    TipNumber: int


    class SensorStrategyType(enum.Enum):
        Createasneeded = 0
        Useexistingonly = 1
    

    class SensorSelectModeType(enum.Enum):
        Automatic = 0
        SpecifySensor = 1
        SpecifyProbeAngles = 2
        SpecifyProbeTip = 3
        SpecifyAnglesandTip = 4
    

class InspectionSensorBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetSensorTipXyz(self) -> float:
        ...
    def SetSensorTipXyz(self, xyz: float) -> None:
        ...
    def GetSensorTipIjk(self) -> float:
        ...
    def SetSensorTipIjk(self, ijk: float) -> None:
        ...
    AngleA: float
    AngleB: float
    MasterOpLabel: str
    SensorOpLabel: str
    SensorOpName: str
    SensorTipDiameter: float
    SensorTipLength: float
    SensorTipLocation: CAM.InspectionSensorBuilder.SensorTipLocationTypes
    SensorTipSize: float
    SensorTipType: CAM.InspectionSensorBuilder.SensorTipTypes
    SensorType: CAM.InspectionSensorBuilder.SensorTypes
    TipNumber: int
    ToolName: str


    class SensorTypes(enum.Enum):
        Fixed = 0
        Index = 1
    

    class SensorTipTypes(enum.Enum):
        Sphere = 0
        Cylinder = 1
        Disk = 2
    

    class SensorTipLocationTypes(enum.Enum):
        Cartesian = 0
        Polar = 1
        Vector = 2
    

class InspectionScanLineBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    ApproachDist: CAM.InheritableDoubleBuilder
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    EndDistance: float
    EndDistanceBuilder: CAM.InheritableDoubleBuilder
    EndPercentage: CAM.InheritableDoubleBuilder
    Line: NXObject
    RetractDist: CAM.InheritableDoubleBuilder
    Reversedirection: bool
    ScanModeType: CAM.InspectionMethodBuilder.ScanModeTypes
    ScanSpeed: CAM.InheritableDoubleBuilder
    StartDistance: float
    StartDistanceBuilder: CAM.InheritableDoubleBuilder
    StartEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartPercentage: CAM.InheritableDoubleBuilder
    StepSize: CAM.InheritableDoubleBuilder


class InspectionScanHelixBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    ApproachDist: CAM.InheritableDoubleBuilder
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    EndDistance: CAM.InheritableDoubleBuilder
    EndPercentage: CAM.InheritableDoubleBuilder
    Pitch: CAM.InheritableDoubleBuilder
    RetractDist: CAM.InheritableDoubleBuilder
    Reversedirection: bool
    Revolutions: CAM.InheritableDoubleBuilder
    ScanModeType: CAM.InspectionMethodBuilder.ScanModeTypes
    ScanSpeed: CAM.InheritableDoubleBuilder
    StartDistance: CAM.InheritableDoubleBuilder
    StartEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartPercentage: CAM.InheritableDoubleBuilder
    StepSize: CAM.InheritableDoubleBuilder
    Sweep: CAM.InheritableDoubleBuilder
    TurnDirection: CAM.InspectionMethodBuilder.ScanHelixTurnDirectionTypes
    TurnType: CAM.InspectionMethodBuilder.ScanHelixTurnTypes


class InspectionScanCurveBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    ApproachDist: CAM.InheritableDoubleBuilder
    CurvatureFactor: CAM.InheritableDoubleBuilder
    Curve: NXObject
    CurveMode: CAM.InspectionMethodBuilder.ScanCurveModeTypes
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    EndDistance: float
    EndDistanceBuilder: CAM.InheritableDoubleBuilder
    EndPercentage: CAM.InheritableDoubleBuilder
    MaxSpacing: CAM.InheritableDoubleBuilder
    MinSpacing: CAM.InheritableDoubleBuilder
    NbPointsBuilder: CAM.InheritableIntBuilder
    Nbpoints: int
    RetractDist: CAM.InheritableDoubleBuilder
    Reversedirection: bool
    ScanSpeed: CAM.InheritableDoubleBuilder
    StartDistance: float
    StartDistanceBuilder: CAM.InheritableDoubleBuilder
    StartEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartPercentage: CAM.InheritableDoubleBuilder
    StepSize: CAM.InheritableDoubleBuilder


class InspectionScanCurve5AxisBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    ApproachDist: CAM.InheritableDoubleBuilder
    CurvatureFactor: CAM.InheritableDoubleBuilder
    Curve: NXObject
    CurveMode: CAM.InspectionMethodBuilder.ScanCurveModeTypes
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    EndDistance: float
    EndDistanceBuilder: CAM.InheritableDoubleBuilder
    EndPercentage: CAM.InheritableDoubleBuilder
    MaxSpacing: CAM.InheritableDoubleBuilder
    MergePrevious: bool
    MinSpacing: CAM.InheritableDoubleBuilder
    NbPointsBuilder: CAM.InheritableIntBuilder
    Nbpoints: int
    RetractDist: CAM.InheritableDoubleBuilder
    Reversedirection: bool
    ScanSpeed: CAM.InheritableDoubleBuilder
    StartDistance: float
    StartDistanceBuilder: CAM.InheritableDoubleBuilder
    StartEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartPercentage: CAM.InheritableDoubleBuilder
    StepSize: CAM.InheritableDoubleBuilder


class InspectionScanArcBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    ApproachDist: CAM.InheritableDoubleBuilder
    Arc: NXObject
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    EndDistance: float
    EndDistanceBuilder: CAM.InheritableDoubleBuilder
    EndPercentage: CAM.InheritableDoubleBuilder
    RetractDist: CAM.InheritableDoubleBuilder
    Reversedirection: bool
    ScanModeType: CAM.InspectionMethodBuilder.ScanModeTypes
    ScanSpeed: CAM.InheritableDoubleBuilder
    StartDistance: float
    StartDistanceBuilder: CAM.InheritableDoubleBuilder
    StartEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartPercentage: CAM.InheritableDoubleBuilder
    StepSize: CAM.InheritableDoubleBuilder


class InspectionSaveToLayerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSelectedOps(self) -> typing.List[CAM.CAMObject]:
        ...
    def SetSelectedOps(self, selectedOps: typing.List[CAM.CAMObject]) -> None:
        ...
    def SaveToLayer(self) -> None:
        ...
    GroupName: str
    Layer: int


class InspectionReferenceFeatureModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMethodBuilder.ReferenceFeatureModeTypes


class InspectionProfileDispositionModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMethodBuilder.ProfileDispositionTypes


class InspectionProbeTrackingBuilder(CAM.SolidTrackingBuilder):
    def __init__(self) -> None: ...
    def SetLocationParameters(self, tpLocation: NXObject) -> None:
        ...
    AxialPercent: float
    Axis: NXObject
    StemTop: NXObject
    TipType: CAM.InspectionProbeTrackingBuilder.TipTypes


    class TipTypes(enum.Enum):
        Sphere = 0
        Cylinder = 1
        Disk = 2
    

class InspectionProbeToolBuilder(CAM.SolidToolBuilder):
    def __init__(self) -> None: ...


class InspectionProbeTipTypeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMoveBuilder.ProbeTipTypes


class InspectionPolarGridBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    def SetLayoutChanged(self, flag: bool) -> None:
        ...
    def SetPointCoverageChanged(self, flag: bool) -> None:
        ...
    def SetAppDistChanged(self, flag: bool) -> None:
        ...
    def SetRetDistChanged(self, flag: bool) -> None:
        ...
    def SetPointSequenceChanged(self, flag: bool) -> None:
        ...
    def CopyAttributes(self, target: CAM.InspectionPolarGridBuilder) -> None:
        ...
    def UpdateParamsFromGeometry(self) -> None:
        ...
    def UpdateFromSubOperation(self, source: CAM.InspectionMoveSubop) -> None:
        ...
    AlignMachineAxes: bool
    AngleEndPoint: Point
    AngleMode: CAM.InspectionMethodBuilder.PolarAngleModeTypes
    AngleStartPoint: Point
    ApproachDist: CAM.InheritableDoubleBuilder
    CenterPoint: Point
    MaximumRadius: CAM.InheritableDoubleBuilder
    MaximumRadiusMode: CAM.InspectionMethodBuilder.PolarRadiusModeTypes
    MaximumRadiusPoint: Point
    MeasuredGeometry: NXObject
    MinimumRadius: CAM.InheritableDoubleBuilder
    MinimumRadiusMode: CAM.InspectionMethodBuilder.PolarRadiusModeTypes
    MinimumRadiusPoint: Point
    NumberOfAngularPoints: CAM.InheritableIntBuilder
    NumberOfRadialPoints: CAM.InheritableIntBuilder
    OffsetEndAngle: CAM.InheritableDoubleBuilder
    OffsetMaximumRadius: CAM.InheritableDoubleBuilder
    OffsetMinimumRadius: CAM.InheritableDoubleBuilder
    OffsetStartAngle: CAM.InheritableDoubleBuilder
    PointSequence: CAM.InspectionMethodBuilder.PolarPointSequenceTypes
    RetractDist: CAM.InheritableDoubleBuilder
    SequenceDirection: CAM.InspectionMethodBuilder.PolarSequenceDirectionTypes
    SequenceStart: CAM.InspectionMethodBuilder.PolarSequenceStartTypes
    UseFeatureCollisionAvoidance: bool
    UsePartCollisionAvoidance: bool


class InspectionPointFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def SetProjectionFaces(self, projectionFaces: typing.List[Face]) -> None:
        ...
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    Name: str
    NormalVectorI: float
    NormalVectorJ: float
    NormalVectorK: float
    PointX: float
    PointY: float
    PointZ: float
    ProjectToFace: bool
    ReverseDirection: bool
    SelectPoint: Point
    SelectProjectionFaces: SelectNXObjectList


class InspectionPlaneFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def UpdateNormalVector(self, vector: Vector3d) -> None:
        ...
    BasePointX: float
    BasePointY: float
    BasePointZ: float
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    ExtentType: CAM.CamInspectionOperationExtenttypes
    Name: str
    NormalVector: Direction
    NormalVectorI: float
    NormalVectorJ: float
    NormalVectorK: float
    ReverseFaceNormal: bool
    SelectedPlane: SelectNXObjectList


class InspectionPatternFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetSubFeatures(self) -> str:
        ...
    def SetSubFeatures(self, subFeatures: str) -> None:
        ...
    FeatureFilter: CAM.InspectionPatternFeatureBuilder.FeatureFilterTypes
    Name: str
    SelectFeatures: SelectNXObjectList


    class FeatureFilterTypes(enum.Enum):
        None = 0
        Points = 1
        Lines = 2
        Planes = 3
        Curves = 4
        Holes = 5
        Pins = 6
        Spheres = 7
        Surfaces = 8
    

class InspectionPathPointBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetPointData(self, index: int, point: NXObject, angleA: float, angleB: float) -> None:
        ...
    def SetPointData(self, index: int, point: NXObject, angleA: float, angleB: float) -> None:
        ...
    def ModifyData(self, index: int, point: NXObject, angleA: float, angleB: float) -> None:
        ...
    def Delete(self, index: int) -> None:
        ...


class InspectionPathBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetApproachDirection(self) -> float:
        ...
    def SetApproachDirection(self, direction: float) -> None:
        ...
    def FlipApproachDirection(self) -> None:
        ...
    def ReGenerateInSafePlane(self, firstLast: CAM.InspectionPathBuilder.FirstLastType) -> bool:
        ...
    def ReGenerateEntryExit(self, entryExit: CAM.InspectionPathBuilder.EntryExitType) -> bool:
        ...
    def UpdateSensors(self, setup: CAM.InspectionSetup, parentProgramGroup: CAM.InspectionGroup, parentMethodGroup: CAM.InspectionGroup, parentToolGroup: CAM.InspectionGroup, parentGeometryGroup: CAM.InspectionGroup, typeName: str) -> None:
        ...
    def UpdateParameters(self) -> None:
        ...
    def EditStartEndPoints(self, regenerate: bool) -> None:
        ...
    def EditEntryExitPoints(self, regenerate: bool) -> None:
        ...
    def GetReferenceFeatureModeValue(self) -> CAM.InspectionMethodBuilder.ReferenceFeatureModeTypes:
        ...
    def SetReferenceFeatureModeValue(self, mode: CAM.InspectionMethodBuilder.ReferenceFeatureModeTypes) -> None:
        ...
    def GetReferenceFeaturePointCountValue(self) -> int:
        ...
    def SetReferenceFeaturePointCountValue(self, count: int) -> None:
        ...
    def GetReferenceFeatureOffsetDistanceValue(self) -> float:
        ...
    def SetReferenceFeatureOffsetDistanceValue(self, distance: float) -> None:
        ...
    def GetReferenceFeatureZoneRadiusValue(self) -> float:
        ...
    def SetReferenceFeatureZoneRadiusValue(self, radius: float) -> None:
        ...
    def UpdateReferenceParameters(self, featOpTag: NXObject) -> None:
        ...
    def GenerateReferenceFeature(self) -> int:
        ...
    def RemoveReferenceFeature(self) -> int:
        ...
    def UpdatePath(self) -> None:
        ...
    CreateEntryPoint: bool
    CreateExitPoint: bool
    FeatureOpName: str
    HeightAboveFeature: CAM.InheritableDoubleBuilder
    InspectionMode: CAM.InspectionPathBuilder.InspectModeType
    NumPoints: CAM.InheritableIntBuilder
    PathOpName: str
    ProjectLastPointToSafePlane: bool
    ProjectStartPointToSafePlane: bool
    ReferenceFeatureAutoName: str
    ReferenceFeatureModeBuilder: CAM.InspectionReferenceFeatureModeBuilder
    ReferenceFeatureName: str
    ReferenceFeatureOffsetDistanceBuilder: CAM.InheritableDoubleBuilder
    ReferenceFeaturePointCountBuilder: CAM.InheritableIntBuilder
    ReferenceFeatureZoneRadiusBuilder: CAM.InheritableDoubleBuilder
    SafePlaneXform: NXObject
    SelectFeature: SelectNXObjectList
    SelectReferenceFeature: SelectNXObjectList
    SequenceOptimization: CAM.InspectionPathBuilder.SequenceType
    UseEntryAvoidance: bool
    UseExitAvoidance: bool


    class SequenceType(enum.Enum):
        None = 0
        Nearest = 1
        UStrip = 2
        VStrip = 3
    

    class InspectModeType(enum.Enum):
        Default = 0
        Program = 1
        Manual = 2
        Auto = 3
    

    class FirstLastType(enum.Enum):
        First = 0
        Last = 1
    

    class EntryExitType(enum.Enum):
        Entry = 0
        Exit = 1
    

class InspectionParplnFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    ExtentType: CAM.CamInspectionOperationExtenttypes
    InnerOuterType: CAM.CamInspectionOperationInneroutertypes
    Name: str
    SelectedSide1: SelectNXObjectList
    SelectedSide2: SelectNXObjectList
    Side1NormalVectorI: float
    Side1NormalVectorJ: float
    Side1NormalVectorK: float
    Side1PointX: float
    Side1PointY: float
    Side1PointZ: float
    Side2NormalVectorI: float
    Side2NormalVectorJ: float
    Side2NormalVectorK: float
    Side2PointX: float
    Side2PointY: float
    Side2PointZ: float
    Width: float


class InspectionOutputOperationBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    EnumTypeOutput: CAM.InspectionOutputOperationBuilder.TypeOutput
    StringFeatureName1: str
    StringFeatureName2: str
    StringTolName: str


    class TypeOutput(enum.Enum):
        Output1 = 0
        Output2 = 1
    

class InspectionOperationTransformBuilder(Builder):
    def __init__(self) -> None: ...
    def RemoveTransformation(self) -> None:
        ...
    AngleEndPoint: Point
    AngleMethod: CAM.InspectionOperationTransformBuilder.Angle
    AnglePivotPoint: Point
    AngleStartPoint: Point
    AngleTolerance: float
    AngleValue: float
    ArrayAngle: float
    ArrayCircularIncrementAngle: float
    ArrayCircularNumber: int
    ArrayCircularRadius: float
    ArrayCircularStartAngle: float
    ArrayNumberAlongXc: int
    ArrayNumberAlongYc: int
    ArrayOffsetXc: float
    ArrayOffsetYc: float
    ArrayOriginPoint: Point
    DeltaXc: float
    DeltaYc: float
    DeltaZc: float
    DistanceAngleDivision: int
    DistanceTolerance: float
    LineEndPoint: Point
    LineMethod: CAM.InspectionOperationTransformBuilder.Line
    LinePoint: Point
    LineSelection: SelectLine
    LineStartPoint: Point
    LineVector: Direction
    MotionType: CAM.InspectionOperationTransformBuilder.Motion
    MoveCopyInstance: CAM.InspectionOperationTransformBuilder.Result
    NumOfCopyInstance: int
    Plane: Plane
    ReferencePoint: Point
    RepositionFromCsys: CoordinateSystem
    RepositionToCsys: CoordinateSystem
    ScaleFactor: float
    ToPoint: Point
    TransformType: CAM.InspectionOperationTransformBuilder.Transform


    class Transform(enum.Enum):
        Translate = 0
        Scale = 1
        RotateAboutPoint = 2
        RotateAboutLine = 3
        MirrorThroughALine = 4
        MirrorThroughAPlane = 5
        CircularArray = 6
        RectangularArray = 7
        Reposition = 8
    

    class Result(enum.Enum):
        Move = 0
        Copy = 1
        Instance = 2
    

    class Motion(enum.Enum):
        Delta = 0
        ToAPoint = 1
    

    class Line(enum.Enum):
        Specify = 0
        TwoPoint = 1
        PointAndVector = 2
    

    class Angle(enum.Enum):
        Specify = 0
        TwoPoint = 1
    

class InspectionOperationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.InspectionOperation]:
        ...
    def __init__(self, owner: CAM.InspectionSetup) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.InspectionOperation:
        ...
    def Create(self, parentProgramGroup: CAM.InspectionGroup, parentMethodGroup: CAM.InspectionGroup, parentToolGroup: CAM.InspectionGroup, parentGeometryGroup: CAM.InspectionGroup, typeName: str, subtypeName: str, useDefaultName: CAM.OperationCollection.UseDefaultName, newOperationName: str) -> CAM.InspectionOperation:
        ...
    def CreateInspectionOutputOperationBuilder(self, param: CAM.CAMObject) -> CAM.InspectionOutputOperationBuilder:
        ...
    def CreateInspectionArcFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionArcFeatureBuilder:
        ...
    def CreateInspectionPointFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionPointFeatureBuilder:
        ...
    def CreateInspectionPlaneFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionPlaneFeatureBuilder:
        ...
    def CreateInspectionPathBuilder(self, param: CAM.CAMObject) -> CAM.InspectionPathBuilder:
        ...
    def CreateInspectionCylinderFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionCylinderFeatureBuilder:
        ...
    def CreateInspectionCurveFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionCurveFeatureBuilder:
        ...
    def CreateInspectionSurfaceFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionSurfaceFeatureBuilder:
        ...
    def CreateInspectionPatternFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionPatternFeatureBuilder:
        ...
    def CreateInspectionToleranceOperationBuilder(self, param: CAM.CAMObject) -> CAM.InspectionToleranceOperationBuilder:
        ...
    def CreateInspectionAlignmentBuilder(self, param: CAM.CAMObject) -> CAM.InspectionAlignmentBuilder:
        ...
    def CreateInspectionCmmCommandBuilder(self, param: CAM.CAMObject) -> CAM.InspectionCmmCommandBuilder:
        ...
    def CreateInspectionConeFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionConeFeatureBuilder:
        ...
    def CreateInspectionSphereFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionSphereFeatureBuilder:
        ...
    def CreateInspectionCircleFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionCircleFeatureBuilder:
        ...
    def CreateInspectionTorusFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionTorusFeatureBuilder:
        ...
    def CreateInspectionCparlnFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionCparlnFeatureBuilder:
        ...
    def CreateInspectionParplnFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionParplnFeatureBuilder:
        ...
    def CreateInspectionConstructedFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionConstructedFeatureBuilder:
        ...
    def CreateInspectionSensorBuilder(self, param: CAM.CAMObject) -> CAM.InspectionSensorBuilder:
        ...
    def CreateInspectionCreatePathsBuilder(self, param: CAM.CAMObject) -> CAM.InspectionCreatePathsBuilder:
        ...
    def CreateInspectionLineFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionLineFeatureBuilder:
        ...
    def CreateInspectionLinkPmiBuilder(self, param: CAM.CAMObject) -> CAM.InspectionLinkPmiBuilder:
        ...
    def SetPathFeature(self, inspectionPath: CAM.CAMObject, featureName: str) -> None:
        ...
    def CreateInspectionCollisionAvoidanceBuilder(self, param: CAM.CAMObject) -> CAM.InspectionCollisionAvoidanceBuilder:
        ...
    def CreateInspectionMeasDataBuilder(self, param: CAM.CAMObject) -> CAM.InspectionMeasDataBuilder:
        ...
    def CreateInspectionAnalyzeBuilder(self, param: CAM.CAMObject) -> CAM.InspectionAnalyzeBuilder:
        ...
    def CreateInspectionAnalyzeOutputBuilder(self, param: CAM.CAMObject) -> CAM.InspectionAnalyzeOutputBuilder:
        ...
    def CreateInspectionEdgePointFeatureBuilder(self, param: CAM.CAMObject) -> CAM.InspectionEdgePointFeatureBuilder:
        ...
    def CreateInspectionSaveToLayerBuilder(self, param: CAM.CAMObject) -> CAM.InspectionSaveToLayerBuilder:
        ...
    def CreateInspectionSaveToLayerBuilderSel(self, selOps: typing.List[CAM.CAMObject]) -> CAM.InspectionSaveToLayerBuilder:
        ...
    def CreateInspectionDeleteMeaPtsBuilderSel(self, selOps: typing.List[CAM.CAMObject]) -> CAM.InspectionDeleteMeaPtsBuilder:
        ...
    def CreateInspectionOperationTransformBuilder(self, objectsToTransform: typing.List[CAM.CAMObject]) -> CAM.InspectionOperationTransformBuilder:
        ...
    def CreateInspectionAlignmentAssistantBuilder(self, param: CAM.CAMObject) -> CAM.InspectionAlignmentAssistantBuilder:
        ...
    def CreateGraphicalReportBuilder(self, param: CAM.CAMObject) -> CAM.InspectionGraphicalReportBuilder:
        ...
    def CreateGraphicalReportOutputBuilder(self, objectsToOutput: typing.List[CAM.CAMObject]) -> CAM.InspectionGraphicalReportOutputBuilder:
        ...
    def CreateGraphicalVariableBuilder(self) -> CAM.InspectionGraphicalVariableBuilder:
        ...
    def CreateImportDmisBuilder(self, programGroup: CAM.InspectionGroup) -> CAM.InspectionImportDmisBuilder:
        ...
    def Tag(self) -> Tag: ...



class InspectionOperation(CAM.Operation):
    def __init__(self) -> None: ...
    def GetFeatureType(self) -> CAM.CamInspectionOperationFeaturetypes:
        ...
    def AppendSubopMove(self, move: CAM.Move) -> None:
        ...
    def InsertSubopMove(self, insertAfter: CAM.Move, move: CAM.Move) -> None:
        ...
    CmmInspectionMoveCollection: CAM.InspectionMoveCollection


class InspectionMoveSubopCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.InspectionMoveSubop]:
        ...
    def __init__(self, owner: CAM.InspectionMoveSubop) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.InspectionMoveSubop:
        ...
    def Tag(self) -> Tag: ...



class InspectionMoveSubop(CAM.Move):
    def __init__(self) -> None: ...
    CmmInspectionMoveSubopCollection: CAM.InspectionMoveSubopCollection


class InspectionMoveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.InspectionMoveSubop]:
        ...
    def __init__(self, owner: CAM.InspectionOperation) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.InspectionMoveSubop:
        ...
    def CreateInspectionLinearMoveToPointBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionLinearMoveToPointBuilder:
        ...
    def CreateInspectionUvgridBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionUVGridBuilder:
        ...
    def CreateInspectionMeasurePointBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionMeasurePointBuilder:
        ...
    def CreateInspectionScanCurveBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionScanCurveBuilder:
        ...
    def CreateInspectionScanLineBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionScanLineBuilder:
        ...
    def CreateInspectionScanArcBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionScanArcBuilder:
        ...
    def CreateInspectionDeltaMoveBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionDeltaMoveBuilder:
        ...
    def CreateInspectionScanCurve5axisBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionScanCurve5AxisBuilder:
        ...
    def CreateInspectionSensorMassEditBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionSensorMassEditBuilder:
        ...
    def CreateInspectionLinear5axisMoveToPointBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionLinear5axisMoveToPointBuilder:
        ...
    def CreateInspectionScanHelixBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionScanHelixBuilder:
        ...
    def CreateInspectionPolarGridBuilder(self, param: CAM.InspectionMoveSubop) -> CAM.InspectionPolarGridBuilder:
        ...
    def Tag(self) -> Tag: ...



class InspectionMoveBuilder(Builder):
    def __init__(self) -> None: ...
    def SetParent(self, parent: CAM.CAMObject) -> None:
        ...
    def SetSibling(self, sibling: CAM.CAMObject) -> None:
        ...
    def SetProbeAngles(self) -> None:
        ...
    def SetProbeTip(self) -> None:
        ...
    def LockMove(self, lock: bool) -> None:
        ...
    AngleA: float
    AngleB: float
    ApproachDistance: float
    MotionType: CAM.MoveBuilder.Motion
    ProbeTipType: CAM.InspectionMoveBuilder.ProbeTipTypes
    ProbeTipTypeBuilder: CAM.InspectionProbeTipTypeBuilder
    RetractDistance: float
    SensorOpName: str
    SensorStrategy: CAM.InspectionMoveBuilder.SensorStrategyTypes
    SensorStrategyBuilder: CAM.InspectionSensorStrategyBuilder
    TipAngleMode: CAM.InspectionMoveBuilder.TipAngleTypes
    TipMode: CAM.InspectionMoveBuilder.TipModeTypes
    TipNumber: int


    class TipModeTypes(enum.Enum):
        Auto = 0
        Specify = 1
        Existing = 2
    

    class TipAngleTypes(enum.Enum):
        Auto = 0
        Specify = 1
        Existing = 2
    

    class SensorStrategyTypes(enum.Enum):
        CreateAsNeeded = 0
        UseExisting = 1
    

    class ProbeTipTypes(enum.Enum):
        Any = -1
        Sphere = 0
        Cylinder = 1
        Disk = 2
    

    class DepthMethodTypes(enum.Enum):
        Auto = -1
        Distance = 0
        FromFeatureNominal = 1
        FromFeatureActual = 2
        FromDatum = 3
    

class InspectionMethodBuilder(CAM.MethodBuilder):
    def __init__(self) -> None: ...
    AdvanceAngle: float
    AngleMode: CAM.InspectionMethodBuilder.PolarAngleModeTypes
    AngularPointCount: int
    ApproachDistance: float
    AxisExtrapolationMode: CAM.InspectionMethodBuilder.AxisExtrapolationTypes
    CircularScan: bool
    ColorApproach: NXColor
    ColorEntryExit: NXColor
    ColorLine: NXColor
    ColorMeasurePoint: NXColor
    ColorRetract: NXColor
    ColorTransition: NXColor
    CurvatureFactor: float
    CurveScan: bool
    CylinderCircleFitMode: CAM.InspectionMethodBuilder.CylinderFittingTypes
    DatumPlaneFittingMode: CAM.InspectionMethodBuilder.DatumPlaneFittingTypes
    DefaultOperationType: CAM.InspectionMethodBuilder.OperationTypes
    DepthDistance: float
    EndDistance: float
    EndPercentage: float
    EntryAvoidance: bool
    EntryExitDistance: float
    EntryPoint: bool
    EntryTransition: CAM.InspectionMethodBuilder.TransitionTypes
    ExitAvoidance: bool
    ExitPoint: bool
    ExitTransition: CAM.InspectionMethodBuilder.TransitionTypes
    FeatureOffsetDistance: float
    InspectionMode: CAM.InspectionMethodBuilder.InspectionModes
    LimitsOfSizeMode: CAM.InspectionMethodBuilder.LimitsOfSizeTypes
    LineScan: bool
    ManualPoint: bool
    MaxSpacing: float
    MaximumRadius: float
    MaximumRadiusMode: CAM.InspectionMethodBuilder.PolarRadiusModeTypes
    MethodType: CAM.InspectionMethodBuilder.MethodTypes
    MinSpacing: float
    MinimumRadius: float
    MinimumRadiusMode: CAM.InspectionMethodBuilder.PolarRadiusModeTypes
    NbScanPoints: int
    OffsetDistance: float
    OffsetEndAngle: float
    OffsetMaximumRadius: float
    OffsetMinimumRadius: float
    OffsetStartAngle: float
    Pitch: float
    PointCount: int
    PointHelix: bool
    PointSequenceDirection: CAM.InspectionMethodBuilder.PointSequenceDirectionTypes
    PointSequenceMode: CAM.InspectionMethodBuilder.PointSequenceModeTypes
    PointSequenceStart: CAM.InspectionMethodBuilder.PointSequenceStartTypes
    PolarGrid: bool
    PolarPointSequence: CAM.InspectionMethodBuilder.PolarPointSequenceTypes
    PolarSequenceDirection: CAM.InspectionMethodBuilder.PolarSequenceDirectionTypes
    PolarSequenceStart: CAM.InspectionMethodBuilder.PolarSequenceStartTypes
    ProbeTipType: CAM.InspectionMoveBuilder.ProbeTipTypes
    ProfileDispositionMode: CAM.InspectionMethodBuilder.ProfileDispositionTypes
    RadialPointCount: int
    ReferenceFeatureMode: CAM.InspectionMethodBuilder.ReferenceFeatureModeTypes
    ReferenceFeatureOffsetDistance: float
    ReferenceFeaturePointCount: int
    ReferenceFeatureZoneRadius: float
    RetractDistance: float
    Revolutions: float
    ScanCurveMode: CAM.InspectionMethodBuilder.ScanCurveModeTypes
    ScanForce: float
    ScanModeType: CAM.InspectionMethodBuilder.ScanModeTypes
    ScanSpeed: float
    SensorStrategy: CAM.InspectionMoveBuilder.SensorStrategyTypes
    Speed: int
    StartDistance: float
    StartEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    StartPercentage: float
    StepSize: float
    StopRadius: float
    SurfaceProfileMode: CAM.InspectionMethodBuilder.SurfaceProfileTypes
    Sweep: float
    TiltAngle: float
    TurnDirection: CAM.InspectionMethodBuilder.ScanHelixTurnDirectionTypes
    TurnType: CAM.InspectionMethodBuilder.ScanHelixTurnTypes
    UCount: int
    UEnd: float
    UEndDeg: float
    UEndDist: float
    UEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    UEndSweep: float
    UStart: float
    UStartDeg: float
    UStartDist: float
    UStartMode: CAM.InspectionMethodBuilder.UVModeTypes
    UStartSweep: float
    UVGrid: bool
    VCount: int
    VEnd: float
    VEndDeg: float
    VEndDist: float
    VEndMode: CAM.InspectionMethodBuilder.UVModeTypes
    VEndSweep: float
    VStart: float
    VStartDeg: float
    VStartDist: float
    VStartMode: CAM.InspectionMethodBuilder.UVModeTypes
    VStartSweep: float


    class UVModeTypes(enum.Enum):
        Percentage = 0
        Distance = 1
        Full = 2
        Degrees = 3
        Sweep = 4
    

    class TransitionTypes(enum.Enum):
        None = 0
        Manual = 1
        SafePlane = 2
    

    class ToleranceDegreeOfFreedomMode(enum.Enum):
        Tolerance = 0
        On = 1
        Off = 2
        Limits = 3
    

    class ToleranceDegreeOfFreedomCsysMode(enum.Enum):
        Drf = 0
        Pcs = 1
    

    class SurfaceProfileTypes(enum.Enum):
        MinimumDeviationNormal = 0
        MinimumDeviation3D = 1
        LeastSquaresNormal = 2
        LeastSquares3D = 3
    

    class ScanModeTypes(enum.Enum):
        Mode3axis = 0
        Mode5axis = 1
    

    class ScanHelixTurnTypes(enum.Enum):
        Pitch = 0
        SweepAngle = 1
        Revolutions = 2
    

    class ScanHelixTurnDirectionTypes(enum.Enum):
        Right = 0
        Left = 1
    

    class ScanCurveModeTypes(enum.Enum):
        ExistingCurve = 0
        AutoCurve = 1
        OffsetCurve = 2
    

    class ReferenceFeatureModeTypes(enum.Enum):
        None = 0
        Existing = 1
        Automatic = 2
    

    class ProfileDispositionTypes(enum.Enum):
        Standard = 0
        Upper = 1
        Lower = 2
    

    class PolarSequenceStartTypes(enum.Enum):
        RminAmin = 0
        RminAmax = 1
        RmaxAmin = 2
        RmaxAmax = 3
    

    class PolarSequenceDirectionTypes(enum.Enum):
        Radial = 0
        Angular = 1
    

    class PolarRadiusModeTypes(enum.Enum):
        Distance = 0
        Geometry = 1
    

    class PolarPointSequenceTypes(enum.Enum):
        Zig = 0
        ZigZag = 1
        Nearest = 2
    

    class PolarAngleModeTypes(enum.Enum):
        Full = 0
        Partial = 1
    

    class PointSequenceStartTypes(enum.Enum):
        UminVmin = 0
        UminVmax = 1
        UmaxVmin = 2
        UmaxVmax = 3
    

    class PointSequenceModeTypes(enum.Enum):
        Zig = 0
        ZigZag = 1
        Nearest = 2
    

    class PointSequenceDirectionTypes(enum.Enum):
        U = 0
        V = 1
    

    class OperationTypes(enum.Enum):
        None = 0
        ManualPoint = 1
        UVGrid = 2
        PointHelix = 3
        LineScan = 4
        CircularScan = 5
        CurveScan = 6
        HelicalScan = 7
        CurveScan5axis = 8
        LinearSafeMoveToPoint = 9
        DeltaMove = 10
        Linear5axisMoveToPoint = 11
        PolarGrid = 12
    

    class MethodTypes(enum.Enum):
        None = 0
        Arc = 1
        Circle = 2
        Point = 3
        Sphere = 4
        Surface = 5
        Pattern = 6
        Curve = 7
        Cylinder = 8
        Cone = 9
        Plane = 10
        Line = 11
        CParln = 12
        SlotTab = 13
        SurfaceOfRevolution = 14
        Torus = 15
        EdgePt = 16
    

    class LimitsOfSizeTypes(enum.Enum):
        Average = 0
        Functional = 1
        TwoPoint = 2
    

    class InspectionModes(enum.Enum):
        ProgramDefault = 0
        Program = 1
        Manual = 2
        Auto = 3
    

    class DatumPlaneFittingTypes(enum.Enum):
        LeastSquares = 0
        HighPoint = 1
    

    class CylinderFittingTypes(enum.Enum):
        LeastSquares = 0
        MinimumDeviation = 1
        CrossSectionCenters = 2
        ExternalFunction = 3
    

    class AxisExtrapolationTypes(enum.Enum):
        On = 0
        Off = 1
    

class InspectionMeasurePointBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    ApproachDist: CAM.InheritableDoubleBuilder
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    I: float
    J: float
    K: float
    PointTypeEnum: CAM.InspectionMeasurePointBuilder.PointTypes
    RetractDist: CAM.InheritableDoubleBuilder
    SelectExistingPoint: SelectPoint
    TargetPoint: Point
    X: float
    Y: float
    Z: float


    class PointTypes(enum.Enum):
        ExistingPoint = 0
        CursorLocation = 1
        PointConstructor = 2
    

class InspectionMeasDataBuilder(Builder):
    def __init__(self) -> None: ...
    def LoadMea(self) -> None:
        ...
    def UnloadMea(self) -> None:
        ...
    def SaveToLayer(self) -> None:
        ...
    def AppendExternalPoints(self, pointTags: typing.List[NXObject]) -> int:
        ...
    def RemoveExternalPoints(self, pointTags: typing.List[NXObject]) -> int:
        ...
    def AcceptRejectExternalPoints(self, acceptedPointCount: int, rejectedPointCount: int) -> None:
        ...
    DisplayTransform: CAM.InspectionMeasDataBuilder.DisplayTransformTypes
    FeatDisplayDesPoints: bool
    FeatDisplayMeaPoints: bool
    FeatDisplayReconstruct: bool
    FeatHighlightNominal: bool
    HolePinMatching: CAM.InspectionMeasDataBuilder.BoundingType
    InputFormat: CAM.InspectionMeasDataBuilder.InputFormatType
    InspectionDate: str
    Layer: int
    MeaFile: str
    MeasuredPartName: str
    NeedleScale: float
    OffsetDist: float
    PcsName: str
    PointDistanceTolerance: float
    ProjectLimit: float
    RunNumber: str
    SelectedPoints: SelectNXObjectList
    SpecifyPointDistance: bool
    TolDisplayActDRF: bool
    TolDisplayDesDRF: bool
    TolDisplayDesPoints: bool
    TolDisplayGauge: bool
    TolDisplayMeaPoints: bool
    TolDisplayNeedles: bool
    TolDisplayPoints: bool
    TolDisplayReconstruct: bool
    TolHighlightNominal: bool


    class InputFormatType(enum.Enum):
        Mea = 0
        Dml = 1
        Csv = 2
        Points = 3
    

    class DisplayTransformTypes(enum.Enum):
        DesignDRF = 0
        ActualDRF = 1
        OuterProfile = 2
        InnerProfile = 3
    

    class BoundingType(enum.Enum):
        Bounded = 0
        Unbounded = 1
    

class InspectionLinkPmiBuilder(Builder):
    def __init__(self) -> None: ...
    def SafePlaneSelectAction(self) -> None:
        ...
    def SafePlaneDisplayAction(self) -> None:
        ...
    def LinkToPmi(self) -> None:
        ...
    def GetResults(self) -> str:
        ...
    def OutputResults(self, deviceType: ListingWindow.DeviceType, fileName: str) -> None:
        ...
    AngleA: float
    AngleB: float
    AngleString: str
    CollisionAvoidanceEnum: CAM.InspectionLinkPmiBuilder.CollisionAvoidanceEnumType
    ComponentSelection: SelectNXObjectList
    CreatePathsEnum: CAM.InspectionLinkPmiBuilder.CreatePathsOptions
    IncludeSubComponents: bool
    PathOrderEnum: CAM.InspectionLinkPmiBuilder.PathOrderTypes
    PointOrderEnum: CAM.InspectionLinkPmiBuilder.PointOrderTypes
    ProbeTipType: CAM.InspectionMoveBuilder.ProbeTipTypes
    ProgramLocationString: str
    ScopeEnum: CAM.InspectionLinkPmiBuilder.PmiScopeTypes
    TipString: str
    ToolString: str
    ViewString: str
    WorkpieceString: str


    class PointOrderTypes(enum.Enum):
        Off = 0
        NearestNeighbor = 1
        ShortestPath = 2
    

    class PmiScopeTypes(enum.Enum):
        WorkpieceOnly = 0
        WorkpieceandComponents = 1
    

    class PathOrderTypes(enum.Enum):
        Off = 0
        BySensor = 1
        NearestNeighbor = 2
        ShortestPath = 3
    

    class CreatePathsOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class CollisionAvoidanceEnumType(enum.Enum):
        Off = 0
        On = 1
    

class InspectionLineFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipLineDirection(self) -> None:
        ...
    def UpdateNormal(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def SetNormalSurface(self, normalSurface: Face) -> None:
        ...
    def ReverseOffsetDirection(self) -> None:
        ...
    def UpdateOffset(self) -> None:
        ...
    CsysRefType: CAM.CamInspectionOperationCsysreferencetypes
    ExtentType: CAM.CamInspectionOperationExtenttypes
    ILine: float
    INormal: float
    JLine: float
    JNormal: float
    KLine: float
    KNormal: float
    Length: float
    LineDirection: Direction
    Name: str
    OffsetDistance: CAM.InheritableDoubleBuilder
    ReverseDirection: bool
    SelectLine: SelectNXObject
    SelectNormalSurface: SelectNXObject
    X: float
    Y: float
    Z: float


class InspectionLinearMoveToPointBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    PointTypeEnum: CAM.InspectionLinearMoveToPointBuilder.PointTypeEnums
    PointX: float
    PointY: float
    PointZ: float
    SelectExistingPoint: SelectPoint
    TargetPoint: Point


    class PointTypeEnums(enum.Enum):
        ExistingPoint = 0
        DeltaXYZ = 1
        PointConstructor = 2
    

class InspectionLinear5axisMoveToPointBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    GotoAangle: float
    GotoBangle: float
    TargetPoint: Point


class InspectionLimitsOfSizeModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMethodBuilder.LimitsOfSizeTypes


class InspectionImportDmisBuilder(Builder):
    def __init__(self) -> None: ...
    def ImportDmis(self) -> None:
        ...
    DmisFile: str
    GeomTol: float
    McsCsys: CoordinateSystem


class InspectionGroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.InspectionGroup]:
        ...
    def __init__(self, owner: CAM.InspectionSetup) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.InspectionGroup:
        ...
    def CreateProgram(self, parentGroup: CAM.InspectionGroup, typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newProgramName: str) -> CAM.InspectionGroup:
        ...
    def CreateMethod(self, parentGroup: CAM.InspectionGroup, typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newMethodName: str) -> CAM.InspectionGroup:
        ...
    def CreateTool(self, parentGroup: CAM.InspectionGroup, typeName: str, subtypeName: str, useDefaultName: CAM.NCGroupCollection.UseDefaultName, newToolName: str) -> CAM.InspectionGroup:
        ...
    def CreateProgramOrderGroupBuilder(self, param: CAM.CAMObject) -> CAM.ProgramOrderGroupBuilder:
        ...
    def CreateInspectionMethodBuilder(self, param: CAM.CAMObject) -> CAM.InspectionMethodBuilder:
        ...
    def CreateProbeToolBuilder(self, param: CAM.CAMObject) -> CAM.ProbeToolBuilder:
        ...
    def CreateInspectionProbeToolBuilder(self, param: CAM.CAMObject) -> CAM.InspectionProbeToolBuilder:
        ...
    def CreateMachineGroupBuilder(self, param: CAM.CAMObject) -> CAM.MachineGroupBuilder:
        ...
    def CreateMachineTurretGroupBuilder(self, param: CAM.CAMObject) -> CAM.MachineTurretGroupBuilder:
        ...
    def CreateMachinePocketGroupBuilder(self, param: CAM.CAMObject) -> CAM.MachinePocketGroupBuilder:
        ...
    def Tag(self) -> Tag: ...



class InspectionGroup(CAM.NCGroup):
    def __init__(self) -> None: ...


class InspectionGraphicalVariableBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.InspectionGraphicalVariableBuilder]) -> None:
        ...
    def Append(self, object: CAM.InspectionGraphicalVariableBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.InspectionGraphicalVariableBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.InspectionGraphicalVariableBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.InspectionGraphicalVariableBuilder) -> None:
        ...
    def Erase(self, obj: CAM.InspectionGraphicalVariableBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.InspectionGraphicalVariableBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.InspectionGraphicalVariableBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.InspectionGraphicalVariableBuilder, object2: CAM.InspectionGraphicalVariableBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.InspectionGraphicalVariableBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class InspectionGraphicalVariableBuilder(Builder):
    def __init__(self) -> None: ...
    VariableKeyword: str
    VariableValue: str


class InspectionGraphicalReportOutputBuilder(Builder):
    def __init__(self) -> None: ...
    def Publish(self) -> None:
        ...
    OpenFile: bool
    OutputFile: str
    OutputFormat: CAM.InspectionGraphicalReportOutputBuilder.OutputFormatType
    PageOrientation: CAM.InspectionGraphicalReportOutputBuilder.PageOrientationType
    PageSize: CAM.InspectionGraphicalReportOutputBuilder.PageSizeType
    ScaleFactor: float


    class PageSizeType(enum.Enum):
        A0 = 0
        A1 = 1
        A2 = 2
        A3 = 3
        A4 = 4
        B1 = 5
        B2 = 6
        B3 = 7
        B4 = 8
        B5 = 9
        Executive = 10
        Folio = 11
        Legal = 12
        Letter = 13
        Tabloid = 14
    

    class PageOrientationType(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class OutputFormatType(enum.Enum):
        Html = 0
        Pdf = 1
    

class InspectionGraphicalReportBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def SaveViewCacheSettings(self) -> None:
        ...
    def CaptureCurrentView(self) -> None:
        ...
    def ActivateView(self) -> None:
        ...
    def RestoreOriginalView(self) -> None:
        ...
    AvailableSelection: SelectNXObjectList
    Camera: str
    FilterEnum: CAM.InspectionGraphicalReportBuilder.GraphicalReportFilter
    MaxCrossSection: bool
    MaxOutOfRound: bool
    MinCrossSection: bool
    MinOutOfRound: bool
    ReportFilterObject: str
    ReportFilterType: CAM.InspectionGraphicalReportBuilder.GraphicalReportFilterType
    ReportName: str
    ReportTitle: str
    VariablesList: CAM.InspectionGraphicalVariableBuilderList


    class GraphicalReportFilterType(enum.Enum):
        Tolerances = 0
        Points = 1
        TitlePage = 2
        Summary = 3
        MinMaxDiameter = 4
    

    class GraphicalReportFilter(enum.Enum):
        None = 0
    

class InspectionEdgePointFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def FlipSurfaceNormal(self) -> None:
        ...
    def UpdateOffset(self) -> None:
        ...
    def SetAdjacentSurface(self, adjacentSurface: Face) -> None:
        ...
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    Name: str
    NormalVectorI: float
    NormalVectorJ: float
    NormalVectorK: float
    OffsetValue: CAM.InheritableDoubleBuilder
    PointX: float
    PointY: float
    PointZ: float
    ReverseEdgeDirection: bool
    ReverseSurfaceDirection: bool
    SelectAdjacentSurface: SelectNXObjectList
    SelectPoint: Point
    SurfaceNormalVectorI: float
    SurfaceNormalVectorJ: float
    SurfaceNormalVectorK: float


class InspectionDeltaMoveBuilder(CAM.InspectionMoveBuilder):
    def __init__(self) -> None: ...
    DeltaX: float
    DeltaY: float
    DeltaZ: float
    DepthDistance: float
    DepthMethod: CAM.InspectionMoveBuilder.DepthMethodTypes
    Intent: CAM.InspectionDeltaMoveBuilder.IntentType


    class IntentType(enum.Enum):
        Wcs = 0
        Mcs = 1
    

class InspectionDeleteMeaPtsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSelectedOps(self) -> typing.List[CAM.CAMObject]:
        ...
    def SetSelectedOps(self, selectedOps: typing.List[CAM.CAMObject]) -> None:
        ...
    def DeleteMeaPoints(self) -> None:
        ...
    SelectedPoints: SelectPointList


class InspectionDatumPlaneFittingModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMethodBuilder.DatumPlaneFittingTypes


class InspectionCylinderFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipAxisDirection(self) -> None:
        ...
    def UpdateAxisDirection(self, vector: Vector3d) -> None:
        ...
    AxisDirectionI: float
    AxisDirectionJ: float
    AxisDirectionK: float
    AxisExtrapolationModeBuilder: CAM.InspectionAxisExtrapolationModeBuilder
    AxisVector: Direction
    BasePointX: float
    BasePointY: float
    BasePointZ: float
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    CylinderCircleFitModeBuilder: CAM.InspectionCylinderCircleFitModeBuilder
    Diameter: float
    ExtentType: CAM.CamInspectionOperationExtenttypes
    InnerOuterType: CAM.CamInspectionOperationInneroutertypes
    Length: float
    Name: str
    SelectedCylinder: SelectNXObject
    SelectedGeometry: SelectNXObjectList


class InspectionCylinderCircleFitModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMethodBuilder.CylinderFittingTypes


class InspectionCurveFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def SetSelectedSurfaces(self, selectedSurfaces: typing.List[Face]) -> None:
        ...
    def ReverseFeatureNormal(self) -> None:
        ...
    def UpdateParams(self) -> None:
        ...
    def ReverseOffsetDirection(self) -> None:
        ...
    def UpdateOffset(self) -> None:
        ...
    def PreviewPointData(self, showExisting: bool) -> None:
        ...
    def ErasePointDefinitionDisplay(self) -> None:
        ...
    ApproachDirection: Direction
    CurvatureFactor: float
    EndDistance: float
    EndPercentage: float
    IsPointDefinitionChanged: bool
    MaximumSpacing: float
    MinimumNumberOfPoints: int
    MinimumSpacing: float
    Name: str
    OffsetDistance: CAM.InheritableDoubleBuilder
    PointDataDefinition: CAM.InspectionCurveFeatureBuilder.PointDataDefinitionType
    PointSelector: SelectPointList
    SelectedCurves: SelectNXObjectList
    SelectedSurfaces: SelectNXObjectList
    StartDistance: float
    StartEndMode: CAM.InspectionCurveFeatureBuilder.StartEndModeType
    StartPercentage: float


    class StartEndModeType(enum.Enum):
        Percentage = 0
        Distance = 1
    

    class PointDataDefinitionType(enum.Enum):
        None = 0
        PointSet = 1
        IndividualPoints = 2
    

class InspectionCreatePathsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSelectedFeatures(self) -> str:
        ...
    def SetSelectedFeatures(self, selectedFeatures: str) -> None:
        ...
    def CreatePaths(self) -> None:
        ...
    def GetFeatureMethods(self) -> typing.List[CAM.InspectionGroup]:
        ...
    def SetFeatureMethods(self, featureMethods: typing.List[CAM.InspectionGroup]) -> None:
        ...
    AngleA: float
    AngleB: float
    AngleString: str
    GeometryGroup: CAM.InspectionGroup
    ProbeTipType: CAM.InspectionMoveBuilder.ProbeTipTypes
    ProgramGroup: CAM.InspectionGroup
    ProgramLocationString: str
    SelectFeatures: SelectNXObjectList
    SensorGroup: CAM.InspectionGroup
    SensorOpName: str
    SensorStrategy: CAM.InspectionMoveBuilder.SensorStrategyTypes
    Setup: CAM.InspectionSetup
    TipAngleMode: CAM.InspectionMoveBuilder.TipAngleTypes
    TipMode: CAM.InspectionMoveBuilder.TipModeTypes
    TipNumber: int
    TipString: str
    ToolGroup: CAM.InspectionGroup
    ToolString: str
    TypeName: str


class InspectionCparlnFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def UpdateOffset(self) -> None:
        ...
    def ReverseOffsetDirection(self) -> None:
        ...
    def UpdateEndType(self) -> None:
        ...
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    EndType: CAM.InspectionCparlnFeatureBuilder.EndTypes
    InnerOuterType: CAM.CamInspectionOperationInneroutertypes
    Length: float
    LengthDirVector: Direction
    LengthDirectionI: float
    LengthDirectionJ: float
    LengthDirectionK: float
    LocationPointX: float
    LocationPointY: float
    LocationPointZ: float
    Name: str
    NormalDirectionI: float
    NormalDirectionJ: float
    NormalDirectionK: float
    OffsetDistance: CAM.InheritableDoubleBuilder
    ReverseDirection: bool
    SelectProjectionFaces: SelectFace
    SelectedGeometry: SelectNXObjectList
    Width: float


    class EndTypes(enum.Enum):
        Round = 0
        Square = 1
    

class InspectionConstructedFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def CycleSolution(self) -> None:
        ...
    def CreateNominal(self) -> None:
        ...
    def GetSubFeatures(self) -> str:
        ...
    def SetSubFeatures(self, subFeatures: str) -> None:
        ...
    def UpdateDirectionVector(self, vector: Vector3d) -> None:
        ...
    def GetSubFeatureStates(self) -> typing.List[CAM.InspectionConstructedFeatureBuilder.CurrentStateType]:
        ...
    def SetSubFeatureStates(self, subFeatureStates: typing.List[CAM.InspectionConstructedFeatureBuilder.CurrentStateType]) -> None:
        ...
    AvailFilterToggle: bool
    AvailStateEnum: CAM.InspectionConstructedFeatureBuilder.AvailableStateType
    AvailableSelection: SelectNXObjectList
    ConstName: str
    CurrentStateEnum: CAM.InspectionConstructedFeatureBuilder.CurrentStateType
    DesignCreation: CAM.InspectionConstructedFeatureBuilder.DesignCreationType
    DesignOffsetGeometry: NXObject
    DestinationPcsEnum: CAM.InspectionConstructedFeatureBuilder.DestPcsEnumType
    DirectionSpecifiedEnum: CAM.InspectionConstructedFeatureBuilder.DirectionType
    DirectionVector: Direction
    ExtractEdgeDistance: CAM.InspectionConstructedFeatureBuilder.ExtractEdgeDistanceType
    ExtractEndDistance: float
    ExtractStartDistance: float
    FeatureTypeEnum: CAM.InspectionConstructedFeatureBuilder.ConstFeatType
    MethodEnum: CAM.InspectionConstructedFeatureBuilder.MethodEnumType
    MoveDistance: float
    NominalName: str
    PcsName: str
    SelectNominalFeature: SelectNXObject
    StepSize: float
    SubFeat1Filter: bool
    SubFeat1Name: str
    SubFeat1Select: SelectNXObject
    SubFeat1StateEnum: CAM.InspectionConstructedFeatureBuilder.SubFeat1StateType
    SubFeat2Filter: bool
    SubFeat2Name: str
    SubFeat2Select: SelectNXObject
    SubFeat2StateEnum: CAM.InspectionConstructedFeatureBuilder.SubFeat2StateType


    class SubFeat2StateType(enum.Enum):
        Nominal = 0
        Actual = 1
    

    class SubFeat1StateType(enum.Enum):
        Nominal = 0
        Actual = 1
    

    class MethodEnumType(enum.Enum):
        BestFit = 0
        Transform = 1
        Intersection = 2
        Minimum = 3
        Maximum = 4
        Projection = 5
        MoveByFeature = 6
        MoveByVector = 7
        PerpendicularTo = 8
        ParallelTo = 9
        Offset = 10
        Middle = 11
        ConeDiameter = 12
        ConeDistance = 13
        Extract = 14
    

    class ExtractEdgeDistanceType(enum.Enum):
        Absolute = 0
        Percentage = 1
    

    class DirectionType(enum.Enum):
        SpecifiedVector = 0
        Radial = 1
        Feature = 2
    

    class DestPcsEnumType(enum.Enum):
        CurrentPCS = 0
        NominalPCS = 1
        ActualPCS = 2
    

    class DesignCreationType(enum.Enum):
        SelectExisting = 0
        CreateNew = 1
    

    class CurrentStateType(enum.Enum):
        Nominal = 0
        Actual = 1
    

    class ConstFeatType(enum.Enum):
        Point = 0
        Line = 1
        Plane = 2
        Arc = 3
        Circle = 4
        Cylinder = 5
        Cone = 6
        Sphere = 7
        Curve = 8
        Torus = 9
        Surface = 10
        SlotTab = 11
    

    class AvailableStateType(enum.Enum):
        Nominal = 0
        Actual = 1
    

class InspectionConeFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    AxisDirectionI: float
    AxisDirectionJ: float
    AxisDirectionK: float
    AxisExtrapolationModeBuilder: CAM.InspectionAxisExtrapolationModeBuilder
    AxisVector: Direction
    CsysReferenceType: CAM.CamInspectionOperationCsysreferencetypes
    CylinderCircleFitModeBuilder: CAM.InspectionCylinderCircleFitModeBuilder
    ExtentType: CAM.CamInspectionOperationExtenttypes
    IncludedAngle: float
    InnerOuterType: CAM.CamInspectionOperationInneroutertypes
    Name: str
    SelectedCone: SelectNXObject
    VertexPointX: float
    VertexPointY: float
    VertexPointZ: float


class InspectionCollisionAvoidanceBuilder(Builder):
    def __init__(self) -> None: ...
    def DoCollisionAvoidance(self) -> None:
        ...
    def GetSelectedOps(self) -> str:
        ...
    def SetSelectedOps(self, selectedOps: str) -> None:
        ...
    def UpdateSimDisplayOptions(self) -> None:
        ...
    ChangeApproachRetract: bool
    ChangeProbeAngles: bool
    ChangeProbeTip: bool
    ClearanceDistance: float
    DeleteMeasurementPoints: bool
    DeleteUserSafePoints: bool
    FacetTolerance: float
    FinishAtSafePlane: bool
    ListOutput: bool
    MaxAngularIncrement: float
    MaxLengthIncrement: float
    MoveMeasurementPoints: bool
    NewSensors: bool
    ProbeRotationsAtSafePlane: bool
    SafePlane: NXObject
    StartFromSafePlane: bool
    TableRotationsAtSafePlane: bool
    ToolChangesAtSafePlane: bool
    TransitionsBetweenPaths: bool
    TransitionsWithinPaths: bool


class InspectionCmmCommandBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetProgStatements(self) -> str:
        ...
    def SetProgStatements(self, progStatements: str) -> None:
        ...
    AngularPlaces: int
    AngularUnits: CAM.InspectionCmmCommandBuilder.AngularUnitsOptions
    AutoToggle: bool
    CommandType: CAM.InspectionCmmCommandBuilder.CommandTypes
    DevTolPlaces: int
    DeviceName: str
    DeviceType: CAM.InspectionCmmCommandBuilder.DeviceTypeOptions
    GotoAangle: float
    GotoBangle: float
    HomePtMethod: CAM.InspectionCmmCommandBuilder.HomePtMethods
    HomePtPoint: Point
    HumidityPlaces: int
    IdName: str
    IdnameMethod: CAM.InspectionCmmCommandBuilder.IdnameMethods
    IndexSize: int
    IntermediatePoint: Point
    JumpLabel: str
    LinearPlaces: int
    LinearUnits: CAM.InspectionCmmCommandBuilder.LinearUnitsOptions
    ManualToggle: bool
    MaxToggle: bool
    MaxValue: float
    MinToggle: bool
    MinValue: float
    MoveType: CAM.InspectionCmmCommandBuilder.MoveTypes
    NumChar: int
    OpName: str
    ProgramName: str
    ProgramNameMethod: CAM.InspectionCmmCommandBuilder.ProgramNameMethods
    ProgramToggle: bool
    PromptVar: CAM.InspectionCmmCommandBuilder.PromptVars
    QisvarType: CAM.InspectionCmmCommandBuilder.QisvarTypes
    QisvarValue: str
    RevMethod: CAM.InspectionCmmCommandBuilder.RevMethods
    RevName: str
    SaveDmlDidLabel: str
    SaveDmlPcsLabel: str
    SaveDmlPointData: bool
    SaveDmlVersion: str
    SensorName: str
    TargetPoint: Point
    TemperaturePlaces: int
    TemperatureUnits: CAM.InspectionCmmCommandBuilder.TemperatureUnitsOptions
    ToolName: str
    UserPrompt: str
    VarName: str
    VarScope: CAM.InspectionCmmCommandBuilder.VarScopes
    VarType: CAM.InspectionCmmCommandBuilder.VarTypes
    VectorPlaces: int


    class VarTypes(enum.Enum):
        Boolean = 0
        Integer = 1
        Long = 2
        Real = 3
        Double = 4
        Character = 5
        Vector = 6
    

    class VarScopes(enum.Enum):
        Global = 0
        Common = 1
        Local = 2
    

    class TemperatureUnitsOptions(enum.Enum):
        Fahrenheit = 0
        Centigrade = 1
    

    class RevMethods(enum.Enum):
        CurrentPartRevision = 0
        UserSpecified = 1
    

    class QisvarTypes(enum.Enum):
        Null = 0
    

    class PromptVars(enum.Enum):
        Null = 0
    

    class ProgramNameMethods(enum.Enum):
        CurrentPartName = 0
        UserSpecified = 1
    

    class MoveTypes(enum.Enum):
        LinearMove = 0
        ArcMove = 1
        HomeLocation = 2
        Linear5axis = 3
    

    class LinearUnitsOptions(enum.Enum):
        PartUnits = 0
        Millimeters = 1
        Centimeters = 2
        Meters = 3
        Inches = 4
        Feet = 5
    

    class IdnameMethods(enum.Enum):
        CurrentPartName = 0
        UserSpecified = 1
    

    class HomePtMethods(enum.Enum):
        MachineZero = 0
        UserSpecifiedPoint = 1
    

    class DeviceTypeOptions(enum.Enum):
        Stor = 0
        Term = 1
        Print = 2
        Comm = 3
        Incr = 4
    

    class CommandTypes(enum.Enum):
        EnterStatement = 0
        MeasurementMode = 1
        DefineHomePoint = 2
        MoveMachine = 3
        OutputDecimalPlaces = 4
        DeclareVariable = 5
        QISVariable = 6
        PromptforInput = 7
        ProgramLabel = 8
        JumptoLabel = 9
        ProgramHeader = 10
        SensorSelect = 11
        Device = 12
        SaveDml = 13
    

    class AngularUnitsOptions(enum.Enum):
        DecimalDegrees = 0
        Radians = 1
        DegreesMinutesSeconds = 2
    

class InspectionCircleFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def UpdateOffset(self) -> None:
        ...
    def ReverseOffsetDirection(self) -> None:
        ...
    CenterPointX: float
    CenterPointY: float
    CenterPointZ: float
    CsysRefType: CAM.CamInspectionOperationCsysreferencetypes
    CylinderCircleFitModeBuilder: CAM.InspectionCylinderCircleFitModeBuilder
    Diameter: float
    InnerOuterType: CAM.CamInspectionOperationInneroutertypes
    Name: str
    NormalVectorI: float
    NormalVectorJ: float
    NormalVectorK: float
    OffsetDistance: CAM.InheritableDoubleBuilder
    ReverseDirection: bool
    SelectProjectionFaces: SelectNXObject
    SelectedCircle: SelectNXObjectList


class InspectionAxisExtrapolationModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.InspectionMethodBuilder.AxisExtrapolationTypes


class InspectionArcFeatureBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def UpdateParams(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def UpdateOffset(self) -> None:
        ...
    def ReverseOffsetDirection(self) -> None:
        ...
    CenterPointX: float
    CenterPointY: float
    CenterPointZ: float
    CsysRefType: CAM.CamInspectionOperationCsysreferencetypes
    CylinderCircleFitModeBuilder: CAM.InspectionCylinderCircleFitModeBuilder
    EndAngle: float
    InOutType: CAM.CamInspectionOperationInneroutertypes
    Name: str
    NormalVectorI: float
    NormalVectorJ: float
    NormalVectorK: float
    OffsetDistance: CAM.InheritableDoubleBuilder
    Radius: float
    ReverseDirection: bool
    SelectArc: SelectNXObjectList
    StartAngle: float
    StartVectorI: float
    StartVectorJ: float
    StartVectorK: float


class InspectionAnalyzeOutputBuilder(Builder):
    def __init__(self) -> None: ...
    def OutputText(self) -> None:
        ...
    def OutputDml(self) -> None:
        ...
    def GetSelectedOps(self) -> str:
        ...
    def SetSelectedOps(self, selectedOps: str) -> None:
        ...
    DmlExtension: str
    DmlPcs: str
    DrfTransform: bool
    FeatureDetail: bool
    FeatureSummary: bool
    ListOutput: bool
    OutputFile: str
    OutputFormat: CAM.InspectionAnalyzeOutputBuilder.OutputFormatType
    PointDetail: bool
    ReportHeader: bool
    ReportingCsys: CAM.InspectionAnalyzeOutputBuilder.ReportingCsysType
    TextExtension: str
    ToleranceDetail: bool
    ToleranceSummary: bool


    class ReportingCsysType(enum.Enum):
        Pcs = 0
        Drf = 1
        SetupABS = 2
        PartABS = 3
    

    class OutputFormatType(enum.Enum):
        StandardTextListing = 0
        DimensionalMarkupLanguage = 1
        Pdf = 2
    

class InspectionAnalyzeBuilder(Builder):
    def __init__(self) -> None: ...
    def UseDefault(self) -> None:
        ...
    def AnalyzeSelected(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def AnalyzeAll(self) -> None:
        ...
    AxisExtrapolation: CAM.InspectionMethodBuilder.AxisExtrapolationTypes
    CylinderFitting: CAM.InspectionMethodBuilder.CylinderFittingTypes
    DatumPlaneFitting: CAM.InspectionMethodBuilder.DatumPlaneFittingTypes
    LimitsOfSize: CAM.InspectionMethodBuilder.LimitsOfSizeTypes
    ProfileDisposition: CAM.InspectionMethodBuilder.ProfileDispositionTypes
    Rx: CAM.InspectionAnalyzeBuilder.DofTypes
    RxLower: float
    RxUpper: float
    Ry: CAM.InspectionAnalyzeBuilder.DofTypes
    RyLower: float
    RyUpper: float
    Rz: CAM.InspectionAnalyzeBuilder.DofTypes
    RzLower: float
    RzUpper: float
    SurfaceProfile: CAM.InspectionMethodBuilder.SurfaceProfileTypes
    ToleranceName: str
    Tx: CAM.InspectionAnalyzeBuilder.DofTypes
    TxLower: float
    TxUpper: float
    Ty: CAM.InspectionAnalyzeBuilder.DofTypes
    TyLower: float
    TyUpper: float
    Tz: CAM.InspectionAnalyzeBuilder.DofTypes
    TzLower: float
    TzUpper: float


    class DofTypes(enum.Enum):
        On = 0
        Off = 1
        Tolerance = 2
        Limits = 3
    

    class ZtMethods(enum.Enum):
        Distance = 0
        Datum = 1
        NominalFeature = 2
        MeasuredFeature = 3
    

    class YtMethods(enum.Enum):
        Distance = 0
        Datum = 1
        NominalFeature = 2
        MeasuredFeature = 3
    

class InspectionAlignmentBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetLocateFeatures(self) -> str:
        ...
    def SetLocateFeatures(self, locateFeatures: str) -> None:
        ...
    def GetRPSFeatures(self) -> str:
        ...
    def SetRPSFeatures(self, rpsFeatures: str) -> None:
        ...
    def GetRPSXFeatures(self) -> str:
        ...
    def SetRPSXFeatures(self, rpsXFeatures: str) -> None:
        ...
    def GetRPSYFeatures(self) -> str:
        ...
    def SetRPSYFeatures(self, rpsYFeatures: str) -> None:
        ...
    def GetRPSZFeatures(self) -> str:
        ...
    def SetRPSZFeatures(self, rpsZFeatures: str) -> None:
        ...
    AlignOpName: str
    AlignType: CAM.InspectionAlignmentBuilder.AlignTypes
    ComponentSelection: Assemblies.SelectComponent
    CsysPick: CoordinateSystem
    FailGroupName: str
    IterAvailSelect: SelectNXObject
    IterConvergeVar: str
    IterDev: float
    IterDevType: CAM.InspectionAlignmentBuilder.IterDevTypes
    IterGroupName: str
    IterMax: int
    LocateAvailSelect: SelectNXObject
    LocateXrot: bool
    LocateXtrans: bool
    LocateYrot: bool
    LocateYtrans: bool
    LocateZrot: bool
    LocateZtrans: bool
    PcsName: str
    PriDatLetter: str
    PriDirection: CAM.InspectionAlignmentBuilder.AlignmentDirections
    PriXorigin: bool
    PriYorigin: bool
    PriZorigin: bool
    RPSAvailSelect: SelectNXObject
    RecallCsys: CoordinateSystem
    RecallDid: str
    RecallExtName: str
    RecallIntName: str
    RecallState: CAM.InspectionAlignmentBuilder.RecallStates
    RotateTableAngle: float
    RotateTableAngularDeviation: float
    RotateTableDirection: CAM.InspectionAlignmentBuilder.RotateTableDirections
    RotateTableFeature: str
    RotateTableFeatureSelect: SelectNXObject
    RotateTableMethod: CAM.InspectionAlignmentBuilder.RotateTableMethods
    RotateTableName: str
    RotateTablePcsUpdateOption: CAM.InspectionAlignmentBuilder.RotateTablePcsUpdateOptions
    RotationAngle: float
    RotationAxis: CAM.InspectionAlignmentBuilder.RotationAxisOptions
    RotationDatumLetter: str
    RotationDirection: CAM.InspectionAlignmentBuilder.RotationDirections
    RotationFeature: str
    RotationFeatureSelect: SelectNXObject
    RotationMethod: CAM.InspectionAlignmentBuilder.RotationMethods
    SaveDid: str
    SavePcsLabel: str
    SaveState: CAM.InspectionAlignmentBuilder.SaveStates
    SecDatLetter: str
    SecDirection: CAM.InspectionAlignmentBuilder.AlignmentDirections
    SecXorigin: bool
    SecYorigin: bool
    SecZorigin: bool
    TerDatLetter: str
    TerDirection: CAM.InspectionAlignmentBuilder.AlignmentDirections
    TerXorigin: bool
    TerYorigin: bool
    TerZorigin: bool
    WcsOrientOption: bool
    XtDatumLetter: str
    XtDistance: float
    XtFeature: str
    XtFeatureSelect: SelectNXObject
    XtMethod: CAM.InspectionAlignmentBuilder.XtMethods
    YtDatumLetter: str
    YtDistance: float
    YtFeature: str
    YtFeatureSelect: SelectNXObject
    YtMethod: CAM.InspectionAlignmentBuilder.YtMethods
    ZtDatumLetter: str
    ZtDistance: float
    ZtFeature: str
    ZtFeatureSelect: SelectNXObject
    ZtMethod: CAM.InspectionAlignmentBuilder.ZtMethods


    class XtMethods(enum.Enum):
        Distance = 0
        Datum = 1
        NominalFeature = 2
        MeasuredFeature = 3
    

    class SaveStates(enum.Enum):
        Actual = 0
        Nominal = 1
    

    class RotationMethods(enum.Enum):
        Angle = 0
        Datum = 1
        NominalFeature = 2
        MeasuredFeature = 3
    

    class RotationDirections(enum.Enum):
        Pxdir = 0
        Pydir = 1
        Pzdir = 2
        Mxdir = 3
        Mydir = 4
        Mzdir = 5
    

    class RotationAxisOptions(enum.Enum):
        Xaxis = 0
        Yaxis = 1
        Zaxis = 2
    

    class RotateTablePcsUpdateOptions(enum.Enum):
        Total = 0
        Origin = 1
        Null = 2
    

    class RotateTableMethods(enum.Enum):
        Absolute = 0
        Incremental = 1
        NominalFeature = 2
        MeasuredFeature = 3
    

    class RotateTableDirections(enum.Enum):
        Clockwise = 0
        CounterClockwise = 1
        Shortest = 2
    

    class RecallStates(enum.Enum):
        Internal = 0
        External = 1
    

    class IterDevTypes(enum.Enum):
        Absolute = 0
        Incremental = 1
    

    class AlignTypes(enum.Enum):
        SetPCStoMCS = 0
        SetPCStoCSYS = 1
        TranslatePCSOrigin = 2
        RotatePCS = 3
        DefinePCSfromDatums = 4
        Iterate = 5
        DefinePCSfromActualDeviations = 6
        SavePCS = 7
        RecallPCS = 8
        RotateTable = 9
        SetPCStoCADABS = 10
        Rps = 11
    

    class AlignmentDirections(enum.Enum):
        None = 0
        Pxdir = 1
        Pydir = 2
        Pzdir = 3
        Mxdir = 4
        Mydir = 5
        Mzdir = 6
    

class InspectionAlignmentAssistantBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    AlignmentType: CAM.InspectionAlignmentAssistantBuilder.AlignType
    CreateIterativeAlignment: bool
    IterativeMax: int
    IterativeRotation: float
    IterativeToggle: bool
    IterativeTranslation: float
    IterativeType: CAM.InspectionAlignmentAssistantBuilder.IterativeTypes
    LocateSelection: SelectNXObjectList
    OperationName: str
    PrimaryDirection: CAM.InspectionAlignmentAssistantBuilder.Direction
    PrimaryOffsetGeometry: NXObject
    PrimarySelection: SelectNXObjectList
    PrimaryState: CAM.InspectionAlignmentAssistantBuilder.State
    PrimaryType: CAM.InspectionAlignmentAssistantBuilder.FeatureType
    RPSXSelection: SelectNXObjectList
    RPSYSelection: SelectNXObjectList
    RPSZSelection: SelectNXObjectList
    SecondaryDirection: CAM.InspectionAlignmentAssistantBuilder.Direction
    SecondaryOffsetGeometry: NXObject
    SecondarySelection: SelectNXObjectList
    SecondaryState: CAM.InspectionAlignmentAssistantBuilder.State
    SecondaryType: CAM.InspectionAlignmentAssistantBuilder.FeatureType
    TertiaryDirection: CAM.InspectionAlignmentAssistantBuilder.Direction
    TertiaryOffsetGeometry: NXObject
    TertiarySelection: SelectNXObjectList
    TertiaryState: CAM.InspectionAlignmentAssistantBuilder.State
    TertiaryType: CAM.InspectionAlignmentAssistantBuilder.FeatureType


    class State(enum.Enum):
        Actual = 0
        Nominal = 1
    

    class IterativeTypes(enum.Enum):
        Absolute = 0
        Incremental = 1
    

    class FeatureType(enum.Enum):
        Plane = 0
        BestFitPlane = 1
        OffsetPlane = 2
        MidPlane = 3
        Cylinder = 4
        BestFitCylinder = 5
        Line = 6
        BestFitLine = 7
        IntersectLine = 8
        Circle = 9
        BestFitCircle = 10
        Point = 11
        BestFitPoint = 12
    

    class Direction(enum.Enum):
        None = 0
        Pxdir = 1
        Pydir = 2
        Pzdir = 3
        Mxdir = 4
        Mydir = 5
        Mzdir = 6
    

    class AlignType(enum.Enum):
        PlanePlanePlane = 0
        PlaneLinePoint = 1
        PlaneCylinderCylinder = 2
        PlaneBoltHoleCircle = 3
        CylinderPlanePlane = 4
        CylinderPlanePoint = 5
        CylinderPlaneCylinder = 6
        SixPointNest = 7
        SPFTolerance = 8
        Lsq = 9
        Rps = 10
    

class InPathEventSetData(TaggedObject):
    def __init__(self) -> None: ...
    UdeSet: CAM.UdeSet
    UdeSetStatus: bool


class InPathEventDataBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.InPathEventDataBuilder]) -> None:
        ...
    def Append(self, object: CAM.InPathEventDataBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.InPathEventDataBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.InPathEventDataBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.InPathEventDataBuilder) -> None:
        ...
    def Erase(self, obj: CAM.InPathEventDataBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.InPathEventDataBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.InPathEventDataBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.InPathEventDataBuilder, object2: CAM.InPathEventDataBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.InPathEventDataBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class InPathEventDataBuilder(NXObject):
    def __init__(self) -> None: ...
    Distance: float
    Method: CAM.InPathEventDataBuilder.LocationMethod
    Pass: int
    Point: Point
    Status: bool
    Udeset: NXObject
    UdesetBuilder: CAM.UdeSet


    class LocationMethod(enum.Enum):
        Specify = 0
        DistanceFromStart = 1
        DistanceFromEnd = 2
    

class InitialProfilePlunge(TaggedObject):
    def __init__(self) -> None: ...
    AxialCoordinate: CAM.InheritableDoubleBuilder
    ExtendDistance: CAM.InheritableDoubleBuilder
    Mode: CAM.InitialProfilePlunge.Modes
    Point: Point
    RadialCoordinate: CAM.InheritableDoubleBuilder
    StopDistance: CAM.InheritableDoubleBuilder


    class Modes(enum.Enum):
        None = 0
        Automatic = 1
        AxialOrRadial = 2
        Specify = 3
    

class Inheritance(enum.Enum):
    No = 0
    Yes = 1


class InheritableToolDepBuilder(CAM.InheritableDoubleBuilder):
    def __init__(self) -> None: ...
    Intent: CAM.ParamValueIntent


class InheritableTextBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: str


class InheritableIntBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: int


class InheritableFeedModeBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: CAM.FeedRapidOutputMode


class InheritableFeedBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Unit: CAM.FeedRateUnit
    Value: float


class InheritableDoubleBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: float


class InheritableColorPickerBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: int


class InheritableBuilder(TaggedObject):
    def __init__(self) -> None: ...
    InheritanceStatus: bool


class InheritableBoolBuilder(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value: bool


class Inheritable2dLength(CAM.InheritableBuilder):
    def __init__(self) -> None: ...
    Value0: float
    Value1: float


class InferredDouble(TaggedObject):
    def __init__(self) -> None: ...
    InferredStatus: CAM.InferredDouble.Lock
    Value: float


    class Lock(enum.Enum):
        UserDefined = 0
        FromGeometry = 1
    

class HubFinish(CAM.Blade):
    def __init__(self) -> None: ...
    CutStart: CAM.BladeCutStart
    Stepover: CAM.StepoverBuilder


class HoleMakingBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    AllowOversizeTool: bool
    BlindHoleStockBuilder: CAM.InheritableDoubleBuilder
    CheckFluteLength: bool
    CheckToolLength: bool
    ClrDistBuilder: CAM.InheritableDoubleBuilder
    ClrVertBuilder: CAM.InheritableDoubleBuilder
    ControlPointType: CAM.HoleMakingBuilder.ControlPointTypes
    CutParameters: CAM.CutParameters
    EngageFeedRate: float
    FeedsBuilder: CAM.FeedsBuilder
    ModelDepthType: CAM.HoleMakingBuilder.ModelDepthTypes
    OversizeToolPercentBuilder: CAM.InheritableDoubleBuilder
    RapidFeedRate: float
    RaptoOffsetBuilder: CAM.InheritableDoubleBuilder
    RaptoOffsetToggle: bool
    ThruClearBuilder: CAM.InheritableDoubleBuilder
    ToolAxisType: CAM.HoleMakingBuilder.ToolAxisTypes
    ToolAxisVector: NXObject
    UseQuery: bool
    UseUserDefinedTp: bool


    class ToolAxisTypes(enum.Enum):
        PositiveZOfMcs = 0
        FixedAxis = 1
        AllAxes = 2
    

    class ModelDepthTypes(enum.Enum):
        Always = 0
        Rule = 1
    

    class ControlPointTypes(enum.Enum):
        ToolTip = 0
        Shoulder = 1
    

class HoleMaking(CAM.Operation):
    def __init__(self) -> None: ...


class HoleMachiningCutParameters(CAM.CutParameters):
    def __init__(self) -> None: ...
    BottomStock: CAM.InheritableDoubleBuilder
    CornerControl: CAM.CornerControlBuilder
    TopOffset: CAM.VerticalPosition


class HoleMachiningBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    def GetFeatureGeometry(self) -> CAM.FBM.FeatureGeometry:
        ...
    def UnlockFeatures(self) -> None:
        ...
    def RemoveOverrides(self) -> None:
        ...
    CollisionCheck: bool
    CuttingParameters: CAM.HoleMachiningCutParameters
    FeedsBuilder: CAM.FeedsBuilder
    NonCuttingBuilder: CAM.NcmHoleMachining
    PredefinedDepth: CAM.DimensionRule


class HoleDrillingCutParameters(CAM.HoleMachiningCutParameters):
    def __init__(self) -> None: ...
    BottomOffset: CAM.VerticalPosition
    RaptoOffset: CAM.VerticalPosition


class HoleDrillingBuilder(CAM.HoleMachiningBuilder):
    def __init__(self) -> None: ...
    def GetToolDrivePoint(self) -> str:
        ...
    def SetToolDrivePoint(self, toolDrivePoint: str) -> None:
        ...
    ControlPointOffset: CAM.HoleDrillingBuilder.ControlPointOffsetType
    CrossOverDistance: CAM.InheritableToolDepBuilder
    CutParameters: CAM.HoleDrillingCutParameters
    IgnoreToolTip: bool
    IntersectionStrategy: CAM.HoleDrillingBuilder.IntersectionStrategyType
    OppositeDirection: CAM.OppositeDirection
    RetractOutputMode: CAM.HoleDrillingBuilder.RetractOutputModeType


    class RetractOutputModeType(enum.Enum):
        ClearanceOnly = 0
        ClearanceInitial = 1
        Always = 2
    

    class IntersectionStrategyType(enum.Enum):
        None = 0
        Part = 1
        Ipw = 2
        IpwAndPart = 3
    

    class ControlPointOffsetType(enum.Enum):
        None = 0
        Feature = 1
    

class HoleDrilling(CAM.Operation):
    def __init__(self) -> None: ...
    UseModelDepth: bool


class HoleBossSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.HoleBossSet]) -> None:
        ...
    def Append(self, object: CAM.HoleBossSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.HoleBossSet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.HoleBossSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.HoleBossSet) -> None:
        ...
    def Erase(self, obj: CAM.HoleBossSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.HoleBossSet]:
        ...
    def SetContents(self, objects: typing.List[CAM.HoleBossSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.HoleBossSet, object2: CAM.HoleBossSet) -> None:
        ...
    def Insert(self, location: int, object: CAM.HoleBossSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class HoleBossSet(TaggedObject):
    def __init__(self) -> None: ...
    def InferLogic(self, entity: NXObject) -> None:
        ...
    def ReverseDirection(self) -> None:
        ...
    def GetFeature(self) -> CAM.FBM.Feature:
        ...
    def GetMachiningFeature(self) -> CAM.CAMFeature:
        ...
    Depth: float
    DepthBuilder: CAM.InferredDouble
    DepthLimit: CAM.HoleBossSet.DepthLimitTypes
    Diameter: float
    DiameterBuilder: CAM.InferredDouble
    Length: float
    LengthBuilder: CAM.InferredDouble
    MajorDiameter: float
    MinorDiameter: float
    Size: str
    StartDiameter: CAM.CAMAttribute
    TipAngle: CAM.CAMAttribute
    ToolAxis: NXObject


    class DepthLimitTypes(enum.Enum):
        Through = 0
        Blind = 1
    

class HoleBossGeometry(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    FeatureGeometry: CAM.FBM.FeatureGeometry
    HoleBossGeom: CAM.HoleBossGeom


class HoleBossGeom(TaggedObject):
    def __init__(self) -> None: ...
    def GetForm(self, type: CAM.HoleBossGeom.FormTypes, formCustom: str) -> None:
        ...
    def SetForm(self, type: CAM.HoleBossGeom.FormTypes, formCustom: str) -> None:
        ...
    def CreateThreadedHoleBuilder(self, entities: typing.List[NXObject], tapDrillSize: float, depth: float, toolAxis: NXObject, majorDiameter: float, minorDiameter: float, lengh: float, size: str, radialEngage: str, pitch: float, rotation: int, form: CAM.HoleBossGeom.FormTypes, formUserDefined: str, tableStandard: str, depthLimit: int) -> CAM.ThreadedHoleSet:
        ...
    def CreateThreadedBossBuilder(self, entities: typing.List[NXObject], diameter: float, height: float, toolAxis: NXObject, majorDiameter: float, minorDiameter: float, lengh: float, size: str, pitch: float, rotation: int, form: CAM.HoleBossGeom.FormTypes, formUserDefined: str) -> CAM.ThreadedBossSet:
        ...
    def CreateHoleBossBuilder(self, entities: typing.List[NXObject], diameter: float, depth: float, toolAxis: NXObject, depthLimit: int) -> CAM.HoleBossSet:
        ...
    def ReorderList(self) -> None:
        ...
    def GetCenterHoleGeometry(self) -> CAM.FBM.MachiningFeatureGeometry:
        ...
    def GetChamferHoleGeometry(self) -> CAM.FBM.MachiningFeatureGeometry:
        ...
    BossList: CAM.HoleBossSetList
    DepthLimit: CAM.HoleBossGeom.DepthLimitTypes
    FormAndPitch: CAM.HoleBossGeom.FormPitchTypes
    HoleBossGeomType: CAM.HoleBossGeom.HoleBossTypes
    HoleList: CAM.HoleBossSetList
    Optimization: CAM.HoleBossGeom.OptimizationTypes
    Pitch: float
    Rotation: CAM.HoleBossGeom.RotationTypes
    Selection: SelectTaggedObject
    ThreadedBossList: CAM.ThreadedBossSetList
    ThreadedHoleList: CAM.ThreadedHoleSetList


    class RotationTypes(enum.Enum):
        RightHand = 0
        LeftHand = 1
    

    class OptimizationTypes(enum.Enum):
        Closest = 0
        ShortestPath = 1
    

    class HoleBossTypes(enum.Enum):
        Hole = 0
        Boss = 1
        ThreadedHole = 2
        ThreadedBoss = 3
        CenterHole = 4
        ChamferHole = 5
    

    class FormTypes(enum.Enum):
        Unified = 0
        Metric = 1
        Trapezoidal = 2
        Acme = 3
        StubAcme = 4
        Lowernherz = 5
        Buttress = 6
        SparkPlug = 7
        Npt = 8
        HoseCoupling = 9
        FireHose = 10
        Unj = 11
        Nps = 12
        Bsp = 13
        Bstp = 14
        Helicoil = 15
        Ns = 16
        UserDefined = 17
    

    class FormPitchTypes(enum.Enum):
        Specify = 0
        FromTable = 1
        FromTool = 2
        FromModel = 3
    

    class DepthLimitTypes(enum.Enum):
        Through = 0
        Blind = 1
        Unknown = 2
    

class HoldingSystemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.HoldingSystemBuilder]) -> None:
        ...
    def Append(self, object: CAM.HoldingSystemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.HoldingSystemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.HoldingSystemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.HoldingSystemBuilder) -> None:
        ...
    def Erase(self, obj: CAM.HoldingSystemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.HoldingSystemBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.HoldingSystemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.HoldingSystemBuilder, object2: CAM.HoldingSystemBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.HoldingSystemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class HoldingSystemBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str


class HolderSectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Create(self, diameter: float, length: float, taperAngle: float, cornerRadius: float) -> NXObject:
        ...
    def Modify(self, section: NXObject, diameter: float, length: float, taperAngle: float, cornerRadius: float) -> None:
        ...
    def Modify(self, index: int, diameter: float, length: float, taperAngle: float, cornerRadius: float) -> None:
        ...
    def Delete(self, section: NXObject) -> None:
        ...
    def Delete(self, index: int) -> None:
        ...
    def MoveUp(self, index: int) -> None:
        ...
    def MoveDown(self, index: int) -> None:
        ...
    def Get(self, section: NXObject, diameter: float, length: float, taperAngle: float, cornerRadius: float) -> None:
        ...
    def GetSection(self, position: int) -> NXObject:
        ...
    def Add(self, inputIndex: int, diameter: float, length: float, taperAngle: float, cornerRadius: float) -> int:
        ...
    def AddByUpperDiameter(self, inputIndex: int, lowerDiameter: float, length: float, upperDiameter: float, cornerRadius: float) -> int:
        ...
    def ModifyByUpperDiameter(self, index: int, lowerDiameter: float, length: float, upperDiameter: float, cornerRadius: float) -> None:
        ...
    def GetAllParameters(self, section: NXObject, lowerDiameter: float, length: float, taperAngle: float, upperDiameter: float, cornerRadius: float) -> None:
        ...
    NumberOfSections: int
    TlHolderOffsetBuilder: CAM.InheritableDoubleBuilder


class GuidingCurvesCutDir(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CutDir: CAM.GuidingCurvesCutDir.Option


    class Option(enum.Enum):
        Clockwise = 0
        Counterclockwise = 1
        AlongGuide = 2
        OppositeGuide = 3
    

class GuidedCurveCutOrder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CutOrderType: CAM.GuidedCurveCutOrder.CutOrderOption


    class CutOrderOption(enum.Enum):
        FromFirstCurve = 0
        OutsideInAlternate = 1
        InsideOutAlternate = 2
        LeftToRight = 3
        RightToLeft = 4
        Toward = 5
        Away = 6
        ToFirstCurve = 7
    

class GuidedCurveBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CutDir: CAM.GuidingCurvesCutDir
    CutOrder: CAM.GuidedCurveCutOrder
    CutSide: CAM.CutSideBuilder
    ExtendGuideCurve: bool
    FromCurveList: SectionList
    GcCutPattern: CAM.CutPatternBuilder
    PatternType: CAM.PatternTypeBuilder
    Smoothing: bool
    StepoverBuilder: CAM.StepoverBuilder
    ToolPosition: CAM.DmToolPosition


    class GcCutPatternTypes(enum.Enum):
        ParallelLines = 0
    

class GroupFeatures(Builder):
    def __init__(self) -> None: ...
    def SetInputFeatures(self, ftrs: typing.List[CAM.CAMFeature]) -> None:
        ...
    def SetFeatureTypes(self, ftrTypes: str) -> None:
        ...
    def SetMachiningAccessDirections(self, vecDirectionTags: typing.List[Direction], dTolerance: float) -> None:
        ...
    def CreateFeatureGroups(self) -> None:
        ...
    FeaturesToGroupType: CAM.GroupFeatures.FeaturesToGroupTypes
    GeometryLocation: str
    GroupByAttributes: str
    GroupByIdenticalAttributes: bool
    GroupByMachiningAccessDirection: bool
    TopFaceCollector: ScCollector


    class FeaturesToGroupTypes(enum.Enum):
        All = 0
        BelowTopFace = 1
        SpecifyFeatures = 2
    

class GrooveToolBuilder(CAM.TurningToolBuilder):
    def __init__(self) -> None: ...
    HolderGrooveHand: CAM.GrooveToolBuilder.HolderGrooveHands
    HolderHand: CAM.GrooveToolBuilder.HolderHands
    HolderInsertExtensionBuilder: CAM.InheritableDoubleBuilder
    HolderStyle: CAM.GrooveToolBuilder.HolderStyles
    InsertShape: CAM.GrooveToolBuilder.InsertShapes
    LeftRadiusBuilder: CAM.InheritableDoubleBuilder
    RadiusBuilder: CAM.InheritableDoubleBuilder
    RightRadiusBuilder: CAM.InheritableDoubleBuilder
    SideAngleBuilder: CAM.InheritableDoubleBuilder
    TipAngleBuilder: CAM.InheritableDoubleBuilder


    class InsertShapes(enum.Enum):
        Std = 0
        Fnr = 1
        Rtj = 2
        User = 3
    

    class HolderStyles(enum.Enum):
        Deg0 = 0
        Deg45 = 1
        Deg90 = 2
        UserDefined = 3
    

    class HolderHands(enum.Enum):
        Left0 = 0
        Left90 = 1
        Right0 = 2
        Right90 = 3
    

    class HolderGrooveHands(enum.Enum):
        Left = 0
        Right = 1
    

class GrooveMillingBuilder(CAM.VolumeBased25DMillingOperationBuilder):
    def __init__(self) -> None: ...
    AxialStepover: CAM.StepoverBuilder
    GrooveGeometry: CAM.FBM.MachiningFeatureGeometry
    LevelSequencing: CAM.GrooveMillingBuilder.LevelSequencingType


    class LevelSequencingType(enum.Enum):
        CeilingToFloor = 0
        FloorToCeiling = 1
        CenterCeilingFloor = 2
        CenterFloorCeiling = 3
        CenterAlternateCeilingFirst = 4
        CenterAlternateFloorFirst = 5
    

class GrooveMilling(CAM.VolumeBased25DMillingOperation):
    def __init__(self) -> None: ...


class GougeCheckResults(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetGougePoints(self) -> typing.List[Point3d]:
        ...
    def GetHolderCollisionPoints(self) -> typing.List[Point3d]:
        ...
    GougeOption: CAM.GougeCheckResults.Option
    NumberGouges: int
    NumberHolderCollisions: int


    class Option(enum.Enum):
        None = 0
        GougeOnly = 1
        GougeAndHolderCollisions = 2
        UseOperation = 3
    

    class Constants(enum.Enum):
        MaxGouges = 100
    

class GougeCheckBuilder(Builder):
    def __init__(self) -> None: ...
    CheckToolAndHolder: bool
    GougeCheckStockOptions: CAM.GougeCheckBuilder.GougeCheckStock
    GougeCheckStockUserDefinedValue: float
    PauseOnFirstGougeOrCollision: bool
    StopWhenLimitReached: bool
    StopWhenLimitReachedMaximumLimit: int
    ToolShape: CAM.GougeCheckBuilder.ToolShapeType


    class ToolShapeType(enum.Enum):
        ToolParameters = 0
        SolidAssembly = 1
    

    class GougeCheckStock(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

class GmcOpBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder
    MoveContainer: CAM.ObjectContainer
    ProbeParamsBuilder: CAM.ProbeParamsBuilder


class GeometrySetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.GeometrySet]) -> None:
        ...
    def Append(self, object: CAM.GeometrySet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.GeometrySet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.GeometrySet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.GeometrySet) -> None:
        ...
    def Erase(self, obj: CAM.GeometrySet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.GeometrySet]:
        ...
    def SetContents(self, objects: typing.List[CAM.GeometrySet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.GeometrySet, object2: CAM.GeometrySet) -> None:
        ...
    def Insert(self, location: int, object: CAM.GeometrySet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class GeometrySet(TaggedObject):
    def __init__(self) -> None: ...
    def RemoveSelectionIntent(self) -> None:
        ...
    def ApplyEdgeSelection(self) -> None:
        ...
    def SetName(self, name: str, useDefaultName: bool) -> None:
        ...
    def GetItems(self) -> typing.List[TaggedObject]:
        ...
    AngleToleranceEdges: float
    BoundaryEdges: ScCollector
    CheckStock: float
    CustomFeed: bool
    CustomPartOffset: bool
    CustomStock: bool
    CustomTolerance: bool
    DraftAngle: float
    DriveStock: float
    FeedUnit: CAM.FeedRateUnit
    FeedValue: float
    FinalStock: float
    HoleList: CAM.CustomLoops
    IgnoreLoopsStatus: CAM.GeometrySet.LoopsIgnoreTypes
    InitialStock: float
    Intol: float
    MaterialSide: CAM.GeometrySet.MaterialSideTypes
    Outtol: float
    PartOffset: float
    SafeClearance: float
    ScCollector: ScCollector
    SeedFace: Face
    Selection: SelectTaggedObjectList
    TraverseInteriorEdges: bool
    UseTangentEdgeAngles: bool


    class MaterialSideTypes(enum.Enum):
        None = 0
        Same = 1
        Opposite = 2
    

    class LoopsIgnoreTypes(enum.Enum):
        None = 0
        All = 1
        Specify = 2
    

class GeometryGroup(CAM.Geometry):
    def __init__(self) -> None: ...
    AutoBlockOffsetNegativeX: float
    AutoBlockOffsetNegativeY: float
    AutoBlockOffsetNegativeZ: float
    AutoBlockOffsetPositiveX: float
    AutoBlockOffsetPositiveY: float
    AutoBlockOffsetPositiveZ: float
    BlankDefinitionType: CAM.GeometryGroup.BlankDefinitionTypes
    BlankIpw: CAM.BlankIpw
    Csys: CartesianCoordinateSystem
    DirectionType: CAM.GeometryGroup.DirectionTypes
    IpwPositionCsys: CoordinateSystem
    IpwPositionType: CAM.GeometryGroup.PositionTypes
    OffsetFromPart: float
    OffsetNegativeZ: float
    OffsetPositiveZ: float
    OrientationType: CAM.GeometryGroup.OrientationTypes
    Vector: Direction


    class PositionTypes(enum.Enum):
        Part = 0
        Coordinate = 1
    

    class OrientationTypes(enum.Enum):
        Mcs = 0
        Specify = 1
    

    class DirectionTypes(enum.Enum):
        Zm = 0
        Specify = 1
    

    class BlankDefinitionTypes(enum.Enum):
        FromGeometry = 0
        OffsetFromPart = 1
        AutoBlock = 2
        Ipw = 3
        BoundingCylinder = 4
        PartOutline = 5
        PartConvexHull = 6
    

class GeometryCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AutoWallSelection: bool
    BladeBlendGeometry: CAM.MultiBladeBaseGeometry
    BladeGeometry: CAM.MultiBladeBaseGeometry
    BlankSpunOutline: CAM.SpunOutlineGeom
    CutVolumeGeom: CAM.CutVolumeGeom
    FloorPlane: Plane
    HoleBossGeom: CAM.HoleBossGeom
    HubGeometry: CAM.MultiBladeBaseGeometry
    PartSpunOutline: CAM.SpunOutlineGeom
    ShroudGeometry: CAM.MultiBladeBaseGeometry
    SplittersGeometry: CAM.MultiBladeSplittersGeometry


class Geometry(TaggedObject):
    def __init__(self) -> None: ...
    def InitializeData(self, reloadGeometry: bool) -> None:
        ...
    def CreateGeometrySet(self) -> CAM.GeometrySet:
        ...
    def AppendGeometrySet(self, templateSet: CAM.GeometrySet, entities: typing.List[DisplayableObject]) -> CAM.GeometrySet:
        ...
    def ExpandSets(self, sets: typing.List[CAM.GeometrySet]) -> None:
        ...
    def PreselectGeometry(self) -> None:
        ...
    def AppendNamedGeometry(self, namedGeometry: typing.List[ScCollector]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    GeometryList: CAM.GeometrySetList
    Topology: CAM.Topology


class GenericTrackingBuilder(CAM.SolidTrackingBuilder):
    def __init__(self) -> None: ...


class GenericToolBuilder(CAM.SolidToolBuilder):
    def __init__(self) -> None: ...


class GenericMotionControl(CAM.Operation):
    def __init__(self) -> None: ...


class GenericFeatureOperationBuilder(CAM.HoleMachiningBuilder):
    def __init__(self) -> None: ...


class GenericFeatureOperation(CAM.Operation):
    def __init__(self) -> None: ...


class GeneralPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    Name: str
    SelectedObjects: SelectNXObjectList


class FormToolBuilder(CAM.TurningToolBuilder):
    def __init__(self) -> None: ...
    FormEdges: CAM.FormEdgesBuilder


class FormEdgesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Create(self, noseRadius: float, noseAngle: float, edgeLength: float) -> int:
        ...
    def Modify(self, nodeIndex: int, noseRadius: float, noseAngle: float, edgeLength: float) -> None:
        ...
    def Delete(self, nodeIndex: int) -> None:
        ...
    def Get(self, position: int, noseRadius: float, noseAngle: float, edgeLength: float) -> None:
        ...
    Angle: float
    EdgeLength: float
    NumberOfFormEdges: int


class FollowPartMoveBuilder(CAM.FollowGeometryMoveBuilder):
    def __init__(self) -> None: ...
    EndPoint: Point
    MoveDirection: CAM.FollowPartMoveBuilder.MoveDirectionTypes


    class MoveDirectionTypes(enum.Enum):
        Undefined = 0
        Forward = 1
        Reverse = 2
    

class FollowGeometryMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    EndExtension: CAM.InheritableToolDepBuilder
    StartExtension: CAM.InheritableToolDepBuilder
    StartPoint: Point
    StartToolAxis: Direction


class FollowCurveMoveBuilder(CAM.FollowGeometryMoveBuilder):
    def __init__(self) -> None: ...
    EndPoint: Point
    EndToolAxis: Direction
    Geometry: Section


class FlowCutSteepContainment(TaggedObject):
    def __init__(self) -> None: ...
    AddCenterPasses: bool
    CutBetweenLevels: bool
    CutLevelType: CAM.FlowCutSteepContainment.CutLevelTypes
    CutPattern: CAM.CutPatternBuilder
    DepthPerCut: CAM.StepoverBuilder
    FlowCutDirection: CAM.FlowCutSteepContainment.CutDirectionTypes
    NumberOfStepoversPerSide: CAM.InheritableIntBuilder
    PatternDirection: CAM.FlowCutSteepContainment.PatternDirectionTypes
    Sequence: CAM.Sequence
    SteepCutDirection: CAM.FlowCutSteepContainment.SteepCutDirectionTypes
    Stepover: CAM.StepoverBuilder


    class SteepCutDirectionTypes(enum.Enum):
        Mixed = 0
        HighToLow = 1
        LowToHigh = 2
    

    class PatternDirectionTypes(enum.Enum):
        Outward = 0
        Inward = 1
    

    class CutLevelTypes(enum.Enum):
        Constant = 0
        Optimized = 1
    

    class CutDirectionTypes(enum.Enum):
        Mixed = 0
        Climb = 1
        Conventional = 2
    

class FlowBuilder(TaggedObject):
    def __init__(self) -> None: ...
    CenterCurve: bool
    ContactBnd: bool
    FlowEdit: CAM.FlowBuilder.FlowEditTypes
    FlowOffsetMode: CAM.FlowBuilder.FlowOffsetModeType
    FlowOverlapDistBuilder: CAM.InheritableDoubleBuilder
    MaxConcavityAngleBuilder: CAM.InheritableDoubleBuilder
    MergeDistBuilder: CAM.InheritableToolDepBuilder
    MinCutLengthBuilder: CAM.InheritableToolDepBuilder
    NonSteepCutting: CAM.FlowCutSteepContainment
    SteepAngleBuilder: CAM.InheritableDoubleBuilder
    SteepCutting: CAM.FlowCutSteepContainment
    TlDiameter: float


    class FlowOffsetModeType(enum.Enum):
        Single = 0
        Multiple = 1
        Reftool = 2
    

    class FlowEditTypes(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

class FirstPlunge(TaggedObject):
    def __init__(self) -> None: ...
    AxialCoordinate: CAM.InheritableDoubleBuilder
    Point: Point
    Position: CAM.FirstPlunge.Positions
    RadialCoordinate: CAM.InheritableDoubleBuilder


    class Positions(enum.Enum):
        Automatic = 0
        AxialOrRadial = 1
        Specified = 2
    

class FinishTurningBuilder(CAM.RoughFinishTurningBuilder):
    def __init__(self) -> None: ...
    NonCuttingBuilder: CAM.NcmTurnRoughFinishBuilder


class FinishTurning(CAM.RoughFinishTurning):
    def __init__(self) -> None: ...


class FinishPassesBuilder(TaggedObject):
    def __init__(self) -> None: ...
    FinishStepoverBuilder: CAM.InheritableToolDepBuilder
    NumberOfFinishPasses: int


class FinishDwell(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.FinishDwell.Types
    Value: float


    class Types(enum.Enum):
        None = 0
        Time = 1
        Revolutions = 2
    

class FeedsWedmBuilder(TaggedObject):
    def __init__(self) -> None: ...
    FeedApproachBuilder: CAM.InheritableFeedBuilder
    FeedCutBuilder: CAM.InheritableFeedBuilder
    FeedDepartureBuilder: CAM.InheritableFeedBuilder
    FeedEngageBuilder: CAM.InheritableFeedBuilder
    FeedFirstCutBuilder: CAM.InheritableFeedBuilder
    FeedRapidBuilder: CAM.InheritableFeedBuilder
    FeedRetractBuilder: CAM.InheritableFeedBuilder
    FeedReturnBuilder: CAM.InheritableFeedBuilder
    FeedSideCutBuilder: CAM.InheritableFeedBuilder
    FeedStepoverBuilder: CAM.InheritableFeedBuilder
    FeedTraversalBuilder: CAM.InheritableFeedBuilder
    OutputMode: CAM.FeedsWedmBuilder.OutputTypes
    UnitsToggle: bool


    class OutputTypes(enum.Enum):
        None = 0
        RapidMovesOnly = 1
        AllMoves = 2
    

class FeedsTurnBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ChamferFeed: CAM.InheritableFeedBuilder
    EngageSpindleSpeedBuilder: CAM.InheritableDoubleBuilder
    EngageSpindleSpeedToggleBuilder: CAM.InheritableIntBuilder
    FeedApproachBuilder: CAM.InheritableFeedBuilder
    FeedCutBuilder: CAM.InheritableFeedBuilder
    FeedDepartureBuilder: CAM.InheritableFeedBuilder
    FeedEngageBuilder: CAM.InheritableFeedBuilder
    FeedFirstCutBuilder: CAM.InheritableFeedBuilder
    FeedMaxApproachLengthBuilder: CAM.InheritableDoubleBuilder
    FeedMaxApproachLengthFlagBuilder: CAM.InheritableIntBuilder
    FeedMinAccelerateDecelerateLengthBuilder: CAM.InheritableDoubleBuilder
    FeedMinAccelerateDecelerateLengthFlagBuilder: CAM.InheritableIntBuilder
    FeedPerToothBuilder: CAM.InheritableDoubleBuilder
    FeedRapidBuilder: CAM.InheritableFeedBuilder
    FeedRapidOutput: CAM.InheritableFeedModeBuilder
    FeedRetractBuilder: CAM.InheritableFeedBuilder
    FeedReturnBuilder: CAM.InheritableFeedBuilder
    FeedSideCutBuilder: CAM.InheritableFeedBuilder
    FeedStepoverBuilder: CAM.InheritableFeedBuilder
    FeedTraversalBuilder: CAM.InheritableFeedBuilder
    FeedrateAccelerateBuilder: CAM.InheritableFeedBuilder
    FeedrateAccelerateLengthBuilder: CAM.InheritableFeedBuilder
    FeedrateCircCcwBuilder: CAM.InheritableFeedBuilder
    FeedrateCircCwBuilder: CAM.InheritableFeedBuilder
    FeedrateCleanupCircCcwBuilder: CAM.InheritableFeedBuilder
    FeedrateCleanupCircCwBuilder: CAM.InheritableFeedBuilder
    FeedrateCleanupCutBuilder: CAM.InheritableFeedBuilder
    FeedrateCleanupDiameterBuilder: CAM.InheritableFeedBuilder
    FeedrateCleanupFaceBuilder: CAM.InheritableFeedBuilder
    FeedrateCleanupLinearBuilder: CAM.InheritableFeedBuilder
    FeedrateClearBuilder: CAM.InheritableFeedBuilder
    FeedrateDecelerateBuilder: CAM.InheritableFeedBuilder
    FeedrateDecelerateLengthBuilder: CAM.InheritableFeedBuilder
    FeedrateDiameterBuilder: CAM.InheritableFeedBuilder
    FeedrateFaceBuilder: CAM.InheritableFeedBuilder
    FeedrateFinishAccelerateBuilder: CAM.InheritableFeedBuilder
    FeedrateFinishAccelerateLengthBuilder: CAM.InheritableFeedBuilder
    FeedrateFinishDecelerateBuilder: CAM.InheritableFeedBuilder
    FeedrateFinishDecelerateLengthBuilder: CAM.InheritableFeedBuilder
    FeedrateFinishRampInBuilder: CAM.InheritableFeedBuilder
    FeedrateFinishRampLevelBuilder: CAM.InheritableFeedBuilder
    FeedrateFinishRampOutBuilder: CAM.InheritableFeedBuilder
    FeedrateLinearBuilder: CAM.InheritableFeedBuilder
    FeedrateProfileCutBuilder: CAM.InheritableFeedBuilder
    FeedrateRampInBuilder: CAM.InheritableFeedBuilder
    FeedrateRampLevelBuilder: CAM.InheritableFeedBuilder
    FeedrateRampOutBuilder: CAM.InheritableFeedBuilder
    FeedrateRoughLastCutBuilder: CAM.InheritableFeedBuilder
    FeedrateRoughLastCutForEntirePassTogBuilder: CAM.InheritableIntBuilder
    RoundFeed: CAM.InheritableFeedBuilder
    SpindleDirectionAutomaticBuilder: CAM.InheritableIntBuilder
    SpindleDirectionBuilder: CAM.InheritableIntBuilder
    SpindleMaximumRpmBuilder: CAM.InheritableDoubleBuilder
    SpindleModeBuilder: CAM.InheritableIntBuilder
    SpindlePresetRpmBuilder: CAM.InheritableDoubleBuilder
    SpindlePresetRpmToggleBuilder: CAM.InheritableIntBuilder
    SpindleRangeBuilder: CAM.InheritableTextBuilder
    SpindleRpmBuilder: CAM.InheritableDoubleBuilder
    SpindleRpmToggleBuilder: CAM.InheritableIntBuilder
    SpindleTextBuilder: CAM.InheritableTextBuilder
    SurfaceSpeedBuilder: CAM.InheritableDoubleBuilder
    ToolDirectionBuilder: CAM.InheritableIntBuilder


class FeedStatusData():
    Value: float
    Unit: CAM.FeedRateUnit
    Inheritance: CAM.Inheritance
    def ToString(self) -> str:
        ...
    def __init__(self, Value: float, Unit: CAM.FeedRateUnit, Inheritance: CAM.Inheritance) -> None: ...


class FeedsOptimizeBuilder(Builder):
    def __init__(self) -> None: ...
    FeedsOptimizationData: CAM.FeedsOptimizationData


class FeedsOptimizationData(TaggedObject):
    def __init__(self) -> None: ...
    ConstantLowerLimit: float
    ConstantUpperLimit: float
    FeedRateRange: CAM.FeedsOptimizationData.FeedRateRangeType
    LengthInterval: float
    NominalDepthPerCut: float
    NominalStepover: float
    PercentLowerLimit: float
    PercentUpperLimit: float


    class FeedRateRangeType(enum.Enum):
        Percent = 0
        Constant = 1
    

class FeedsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetMachiningData(self) -> None:
        ...
    def RecalculateData(self, type: CAM.FeedsBuilder.RecalcuateBasedOn) -> None:
        ...
    CutGasPressure: CAM.InheritableDoubleBuilder
    CutGasType: CAM.InheritableIntBuilder
    CutLaserDelay: CAM.InheritableDoubleBuilder
    CutLaserFrequency: CAM.InheritableDoubleBuilder
    CutLaserPower: CAM.InheritableDoubleBuilder
    FeedApproachBuilder: CAM.InheritableFeedBuilder
    FeedCrossoverBuilder: CAM.InheritableFeedBuilder
    FeedCutBuilder: CAM.InheritableFeedBuilder
    FeedDepartureBuilder: CAM.InheritableFeedBuilder
    FeedEngageBuilder: CAM.InheritableFeedBuilder
    FeedFirstCutBuilder: CAM.InheritableFeedBuilder
    FeedLastCutBuilder: CAM.InheritableFeedBuilder
    FeedPerToothBuilder: CAM.InheritableDoubleBuilder
    FeedRapidBuilder: CAM.InheritableFeedBuilder
    FeedRapidOutput: CAM.InheritableFeedModeBuilder
    FeedRetractBuilder: CAM.InheritableFeedBuilder
    FeedReturnBuilder: CAM.InheritableFeedBuilder
    FeedSideCutBuilder: CAM.InheritableFeedBuilder
    FeedStepoverBuilder: CAM.InheritableFeedBuilder
    FeedTraversalBuilder: CAM.InheritableFeedBuilder
    FeedsOptimizationData: CAM.FeedsOptimizationData
    OptimizeFeedRateWhenGenerating: bool
    PierceGasPressure: CAM.InheritableDoubleBuilder
    PierceGasType: CAM.InheritableIntBuilder
    PierceLaserDelay: CAM.InheritableDoubleBuilder
    PierceLaserFrequency: CAM.InheritableDoubleBuilder
    PierceLaserPower: CAM.InheritableDoubleBuilder
    RetractSpeed: CAM.InheritableDoubleBuilder
    RetractSpeedToggle: int
    SpindleModeBuilder: CAM.InheritableIntBuilder
    SpindleRangeBuilder: CAM.InheritableTextBuilder
    SpindleRpmBuilder: CAM.InheritableDoubleBuilder
    SpindleRpmToggle: int
    SpindleTextBuilder: CAM.InheritableTextBuilder
    SurfaceSpeedBuilder: CAM.InheritableDoubleBuilder
    ToolDirectionBuilder: CAM.InheritableIntBuilder


    class RecalcuateBasedOn(enum.Enum):
        SurfaceSpeed = 0
        SpindleSpeed = 1
        FeedPerTooth = 2
        CutFeedRate = 3
    

class FeedRateUnit(enum.Enum):
    None = 0
    PerMinute = 1
    PerRevolution = 2
    Rapid = 3
    CutPercent = 4


class FeedRapidOutputMode(enum.Enum):
    G0 = 0
    G1 = 1


class FeatureTeaching(Builder):
    def __init__(self) -> None: ...
    def GetRulePath(self) -> str:
        ...
    def SetRulePath(self, path: str) -> None:
        ...
    def GetFaces(self) -> typing.List[DisplayableObject]:
        ...
    def SetFaces(self, aFaces: typing.List[DisplayableObject]) -> None:
        ...
    def AddNewFeatureType(self, name: str, superName: str) -> None:
        ...
    def RemoveFeatureType(self, name: str) -> None:
        ...
    def RenameFeatureType(self, name: str, newName: str) -> None:
        ...
    def AddNewRule(self, name: str, libraryPath: str, featureTypeName: str) -> None:
        ...
    def RemoveRule(self, path: str) -> None:
        ...
    def RenameRule(self, path: str, newName: str) -> None:
        ...
    def Teach(self) -> None:
        ...
    def Test(self) -> typing.List[CAM.CAMFeature]:
        ...
    RuleMatchOptions: CAM.FeatureTeaching.RuleMatchOptionType


    class RuleMatchOptionType(enum.Enum):
        PmiConds = 1
        GeomAttrs = 2
        GeomNames = 4
        FaceColors = 8
    

class FeatureRecognitionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSearchGeometry(self) -> typing.List[DisplayableObject]:
        ...
    def SetSearchGeometry(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def SetMachiningAccessDirection(self, vecDirections: typing.List[Direction], dTolerance: float) -> None:
        ...
    def SetMachiningAccessDirection(self, tagPoint: Point, tagAxis: Direction, bIsTowardAxis: bool) -> None:
        ...
    def SetMachiningAccessDirection(self, focalPt: Point, bIsTowardPt: bool) -> None:
        ...
    def FindFeatures(self) -> typing.List[CAM.CAMFeature]:
        ...
    def GetFoundFeatures(self) -> typing.List[CAM.CAMFeature]:
        ...
    def SetFeatureTypes(self, featureTypes: str) -> None:
        ...
    def GetRegisteredFeatureTypes(self, featureTypes: str) -> None:
        ...
    def CreateManualFeatureBuilder(self) -> CAM.ManualFeatureBuilder:
        ...
    def MakeFeature(self, featureName: str, faces: typing.List[Face], wallFaces: typing.List[Face], deleteFeatures: bool) -> CAM.CAMFeature:
        ...
    def DeleteFeature(self, feature: CAM.CAMFeature) -> None:
        ...
    def GetModelingFeatureTypes(self, featureTypes: str) -> None:
        ...
    AddCadFeatureAttributes: bool
    AssignColor: bool
    FeatureMapperEnabled: bool
    FloorFaces: ScCollector
    GeometrySearchType: CAM.FeatureRecognitionBuilder.GeometrySearch
    IgnoreExistingFeatures: bool
    IgnoreWarnings: bool
    LimitFaces: ScCollector
    LstManualFeatures: CAM.ManualFeatureBuilderList
    MapFeatures: bool
    RecognitionType: CAM.FeatureRecognitionBuilder.RecognitionEnum
    UseFeatureNameAsType: bool
    VecDirection: Direction


    class RecognitionEnum(enum.Enum):
        Identify = 0
        Parametric = 1
        Legacy = 2
        Generic = 3
        Manual = 4
    

    class GeometrySearch(enum.Enum):
        Workpiece = 0
        AllGeometry = 1
        Selected = 2
    

class FeatureProcessBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTemplate(self, activeTemplate: str, featureProcesTemplate: str) -> None:
        ...
    def SetTemplate(self, activeTemplate: str, featureProcesTemplate: str) -> None:
        ...
    def SetRuleLibraries(self, ruleLibraries: str) -> None:
        ...
    def GetRuleLibraries(self, ruleLibraries: str) -> None:
        ...
    def GetGeometryLocation(self) -> str:
        ...
    def SetGeometryLocation(self, geometryLocation: str) -> None:
        ...
    def CreateFeatureProcesses(self, features: typing.List[CAM.CAMFeature], resultStatus: FeatureProcessBuilderStatus) -> typing.List[CAM.Operation]:
        ...
    def RecreateFeatureProcesses(self, groups: typing.List[CAM.FeatureGeometryGroup], resultStatus: FeatureProcessBuilderStatus) -> typing.List[CAM.Operation]:
        ...
    FeatureGrouping: CAM.FeatureProcessBuilder.FeatureGroupingType
    Type: CAM.FeatureProcessBuilder.FeatureProcessType


    class FeatureProcessType(enum.Enum):
        RuleBased = 0
        TemplateBased = 1
        OperationSetBased = 2
    

    class FeatureGroupingType(enum.Enum):
        AlwaysCreateNew = 0
        PerFeature = 1
        UseExisting = 2
    

class FeatureMillingCutParameters(CAM.HoleMachiningCutParameters):
    def __init__(self) -> None: ...
    CuttingDirection: CAM.FeatureMillingCutParameters.CuttingDirectionTypes


    class CuttingDirectionTypes(enum.Enum):
        Climb = 0
        Conventional = 1
    

class FeatureMillingBuilder(CAM.PlanarOperationBuilder):
    def __init__(self) -> None: ...


    class TransferMethodTypes(enum.Enum):
        ClearancePlane = 0
        PreviousPlane = 1
        BlankPlane = 2
        Direct = 3
    

    class EngretAutoTypeTypes(enum.Enum):
        Linear = 0
        Circular = 1
    

    class EngAutoRampMethodTypes(enum.Enum):
        OnLines = 0
        OnLinesAndArcs = 1
        HelicalRamping = 2
    

    class CutterCompensationTypes(enum.Enum):
        None = 0
        EngageRetract = 1
        AgainstWall = 2
    

class FeatureMilling(CAM.PlanarOperation):
    def __init__(self) -> None: ...


class FeatureGroupBuilder(CAM.FeatureBasedGeomBuilder):
    def __init__(self) -> None: ...
    GeometryBuilder: CAM.Geometry


class FeatureGeometryGroup(CAM.FeatureGeometry):
    def __init__(self) -> None: ...
    def GetFeatures(self) -> typing.List[CAM.CAMFeature]:
        ...
    def GetOperations(self) -> typing.List[CAM.Operation]:
        ...
    def AddFeature(self, feature: CAM.CAMFeature) -> None:
        ...
    def RemoveFeature(self, feature: CAM.CAMFeature) -> None:
        ...
    def Redistribute(self) -> None:
        ...
    Name: str
    Status: CAM.FeatureGeometryGroup.ProcessStatus
    Type: str


    class ProcessStatus(enum.Enum):
        Unknown = 0
        Ok = 1
        Suspect = 2
    

class FeatureGeometry(CAM.NCGroup):
    def __init__(self) -> None: ...


class FeatureGeomBuilder(CAM.NCGroupBuilder):
    def __init__(self) -> None: ...
    def GetMaterial(self) -> str:
        ...
    def SetMaterial(self, libRef: str) -> None:
        ...
    def GetMaterialData(self, libRef: str, name: str, description: str, code: str, hardness: str) -> None:
        ...
    BlankOffsetBuilder: CAM.InheritableDoubleBuilder
    CheckOffsetBuilder: CAM.InheritableDoubleBuilder
    GeometryCiBuilder: CAM.GeometryCiBuilder
    LayoutCiBuilder: CAM.LayoutCiBuilder
    PartMaterialBuilder: NXObject
    PartOffsetBuilder: CAM.InheritableDoubleBuilder
    TrimOffsetBuilder: CAM.InheritableDoubleBuilder


class FeatureBasedGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    def SetGeomParentStringValue(self, value: str) -> None:
        ...
    def GetGeomParentStringValue(self) -> str:
        ...


class FacesSequence(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.FacesSequence.Types


    class Types(enum.Enum):
        SameAsFacesDiameters = 0
        Reversed = 1
    

class FaceMillingBuilder(CAM.PlanarOperationBuilder):
    def __init__(self) -> None: ...
    BlankBoundary: CAM.Boundary
    CheckBoundary: CAM.Boundary
    RoundPoint: CAM.RoundPointBuilder
    TrimBoundary: CAM.Boundary
    WallGeometry: CAM.Geometry


class FaceMilling(CAM.PlanarOperation):
    def __init__(self) -> None: ...


class ExtendAtEdges(TaggedObject):
    def __init__(self) -> None: ...
    Distance: CAM.InheritableToolDepBuilder
    Status: bool


class ExpressionDouble(CAM.BaseBuilder):
    def __init__(self) -> None: ...
    Expression: str
    Intent: CAM.ParamValueIntent
    Value: float


class EngravingBuilder(CAM.PlanarMillingBuilder):
    def __init__(self) -> None: ...


class Engraving(CAM.PlanarMilling):
    def __init__(self) -> None: ...


class ElementStringBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Value: str


class ElementIntBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Value: int


class ElementDoubleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Value: float


class EditSubopCommand(TaggedObject):
    def __init__(self) -> None: ...
    def GetStartPoints(self, startPoint: typing.List[Point]) -> None:
        ...
    def SetStartPoints(self, startPoint: typing.List[Point]) -> None:
        ...
    ContainmentType: CAM.EditSubopCommand.ContainmentTypes
    PointType: CAM.EditSubopCommand.PointTypes


    class PointTypes(enum.Enum):
        Specify = 0
        Automatic = 1
    

    class ContainmentTypes(enum.Enum):
        Steep = 0
        NonSteep = 1
        Flat = 2
    

class EdgeFinish(CAM.Blade):
    def __init__(self) -> None: ...


class DriveMode(TaggedObject):
    def __init__(self) -> None: ...
    FloorOverlap: CAM.InheritableDoubleBuilder
    Mode: CAM.DriveMode.Type
    ReferenceHubToolDiameter: float
    ReferenceToolDiameter: float
    WallOverlap: CAM.InheritableDoubleBuilder


    class Type(enum.Enum):
        LowerBlendEdge = 0
        ReferenceTool = 1
    

class DriveChainItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.DriveChainItemBuilder]) -> None:
        ...
    def Append(self, object: CAM.DriveChainItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.DriveChainItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.DriveChainItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.DriveChainItemBuilder) -> None:
        ...
    def Erase(self, obj: CAM.DriveChainItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.DriveChainItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.DriveChainItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.DriveChainItemBuilder, object2: CAM.DriveChainItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.DriveChainItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DriveChainItemBuilder(Builder):
    def __init__(self) -> None: ...
    CurveItem: Section
    FeedCutBuilder: CAM.InheritableFeedBuilder
    FeedrateFlag: bool


class DrillToolBuilder(CAM.MillingToolBuilder):
    def __init__(self) -> None: ...
    TlCoolantThro: bool
    TlCor1RadBuilder: CAM.InheritableDoubleBuilder
    TlDesignation: str
    TlIncludedAngBuilder: CAM.InheritableDoubleBuilder
    TlPilotDiaBuilder: CAM.InheritableDoubleBuilder
    TlPilotLengthBuilder: CAM.InheritableDoubleBuilder
    TlPitchBuilder: CAM.InheritableDoubleBuilder
    TlPointAngBuilder: CAM.InheritableDoubleBuilder
    TlPointLengthBuilder: CAM.InheritableDoubleBuilder
    TlTaperDiaDistBuilder: CAM.InheritableDoubleBuilder
    TlTipDiameterBuilder: CAM.InheritableDoubleBuilder
    TlTipLengthBuilder: CAM.InheritableDoubleBuilder
    TlXOffsetBuilder: CAM.InheritableDoubleBuilder
    TlYzOffsetBuilder: CAM.InheritableDoubleBuilder


class DrillThreadMillToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...
    FormName: str
    TlFormType: CAM.DrillThreadMillToolBuilder.ToolFormTypeTypes


    class ToolFormTypeTypes(enum.Enum):
        Unified = 0
        Metric = 1
        Trapezoidal = 2
        Acme = 3
        Stubacme = 4
        Lowenherz = 5
        Buttress = 6
        Sparkplug = 7
        Npt = 8
        Hosecoupling = 9
        Firehose = 10
        Unj = 11
        Nps = 12
        Bsp = 13
        Bstp = 14
        Helicoil = 15
        Ns = 16
        UserDefined = 17
    

class DrillTapToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...
    TlTapHolderType: CAM.DrillTapToolBuilder.ToolTapHolderTypeTypes
    TlThreadFormMethod: CAM.DrillTapToolBuilder.ToolThreadFormMethodTypes


    class ToolThreadFormMethodTypes(enum.Enum):
        Cutting = 0
        Roll = 1
    

    class ToolTapHolderTypeTypes(enum.Enum):
        Rigid = 0
        Floating = 1
    

class DrillSurfaceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    Surface: NXObject
    SurfaceOption: CAM.DrillSurfaceBuilder.SurfaceType
    ZcConstant: float


    class SurfaceType(enum.Enum):
        Face = 0
        Plane = 1
        ZcConstant = 2
        None = 3
    

class DrillStepToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...
    StepParamsBuilder: CAM.StepParamsBuilder
    TlShoulderDistBuilder: CAM.InheritableDoubleBuilder


class DrillStdToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillSpotfaceToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillSpotdrillToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillReamerToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillMethodBuilder(CAM.MethodBuilder):
    def __init__(self) -> None: ...
    FeedsBuilder: CAM.FeedsBuilder


class DrillGeomBuilder(CAM.FeatureGeomBuilder):
    def __init__(self) -> None: ...
    def GetToolAxisType(self) -> int:
        ...
    def SetToolAxisType(self, value: int) -> None:
        ...
    BottomSurface: CAM.DrillSurfaceBuilder
    ToolAxisAsArcAxis: int
    ToolAxisVector: NXObject
    TopSurface: CAM.DrillSurfaceBuilder


class DrillCtskToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillCounterboreToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillCoreToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillChamferBoringBarTool(CAM.DrillBoringBarTool):
    def __init__(self) -> None: ...
    UpperCornerRadius: CAM.InheritableDoubleBuilder


class DrillCenterBellToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...
    TlBellAngBuilder: CAM.InheritableDoubleBuilder
    TlBellDiameterBuilder: CAM.InheritableDoubleBuilder


class DrillBurnishingToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillBoringBarTool(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...
    BackInsertLength: CAM.InheritableDoubleBuilder
    FrontInsertLength: CAM.InheritableDoubleBuilder
    InsertAngle: CAM.InheritableDoubleBuilder
    LeadAngle: CAM.InheritableDoubleBuilder
    ReliefLength: CAM.InheritableDoubleBuilder
    ReliefWidth: CAM.InheritableDoubleBuilder


class DrillBoreToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillBackSpotfacingToolBuilder(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...


class DrillBackCountersinkTool(CAM.DrillToolBuilder):
    def __init__(self) -> None: ...
    InsertSize: CAM.InheritableDoubleBuilder
    MinimumHoleDiameter: CAM.InheritableDoubleBuilder


class DPMTubeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    CutDirection: int
    CutType: CAM.CutPatternBuilder
    MaximumDepthPerCut: CAM.InheritableToolDepBuilder
    MaximumStepover: CAM.InheritableToolDepBuilder
    MinimumRadius: CAM.InheritableToolDepBuilder
    Stepover: CAM.StepoverBuilder


class DPMItpBuilder(CAM.ParamBuilder):
    def __init__(self) -> None: ...
    def GetExtendValues(self) -> float:
        """[Obsolete("Deprecated in NX10.0.1.  Use NXOpen.CAM.DmTrimExtend instead.")"""
        ...
    def SetExtendValues(self, values: float) -> None:
        """[Obsolete("Deprecated in NX10.0.1.  Use NXOpen.CAM.DmTrimExtend instead.")"""
        ...
    def MPreview(self) -> None:
        ...
    def GetCrossCurveNormalToFlowCurve(self, curves: typing.List[TaggedObject]) -> None:
        ...
    def SetCrossCurveNormalToFlowCurve(self, curves: typing.List[TaggedObject]) -> None:
        ...
    CrossCurveCount: int
    CrossCurveList: SectionList
    CrossCurveNormalToFlowCount: int
    CrossCurveNormalToFlowSide: CAM.DPMItpBuilder.CrossCurveNormalToFlowSideOption
    CrossCurvesMethod: CAM.DPMItpBuilder.CrossCurvesMethodOption
    CutPatternBuilder: CAM.CutPatternBuilder
    CutStepBuilder: CAM.DmStreamlineCutStep
    CutStepFirstCut: int
    CutStepSecondCut: int
    CutStepThirdCut: int
    CutType: CAM.DPMItpBuilder.CutTypeOption
    FlowCurveCount: int
    FlowCurveList: SectionList
    PreviewEnabled: bool
    SelectionMethod: CAM.DPMItpBuilder.SelectionMethodOption
    StepIntol: CAM.InheritableDoubleBuilder
    StepMethod: CAM.DPMItpBuilder.StepMethodOption
    StepOuttol: CAM.InheritableDoubleBuilder
    StepoverBuilder: CAM.StepoverBuilder
    StepoverDis: float
    StepoverNum: int
    StepoverScallopHeight: float
    StepoverType: CAM.DPMItpBuilder.StepoverTypeOption
    ToolPosition: CAM.DPMItpBuilder.ToolPositionOption
    ToolPositionBuilder: CAM.DmToolPosition
    TrimExtendBuilder: CAM.DmTrimExtend
    UsePartNormal: bool


    class ToolPositionOption(enum.Enum):
        On = 0
        Tanto = 1
        Contact = 2
    

    class StepoverTypeOption(enum.Enum):
        Number = 0
        Distance = 1
        Scallop = 2
    

    class StepMethodOption(enum.Enum):
        Tolerance = 0
        Points = 1
    

    class SelectionMethodOption(enum.Enum):
        Automatic = 0
        Specify = 1
        OnPart = 2
    

    class CutTypeOption(enum.Enum):
        Zig = 0
        Zigzag = 1
        ZigzagWithLifts = 2
        SpiralHelix = 3
    

    class CrossCurvesMethodOption(enum.Enum):
        OnPart = 0
        NormalToFlow = 1
    

    class CrossCurveNormalToFlowSideOption(enum.Enum):
        Both = 0
        Left = 1
        Right = 2
    

class DoubleStatusData():
    Value: float
    Inheritance: CAM.Inheritance
    def ToString(self) -> str:
        ...
    def __init__(self, Value: float, Inheritance: CAM.Inheritance) -> None: ...


class DoubleIntentData():
    Value: float
    Intent: CAM.ParamValueIntent
    Inheritance: CAM.Inheritance
    def ToString(self) -> str:
        ...
    def __init__(self, Value: float, Intent: CAM.ParamValueIntent, Inheritance: CAM.Inheritance) -> None: ...


class DocumentationBuilder(CAM.OperationBuilder):
    def __init__(self) -> None: ...


class Documentation(CAM.Operation):
    def __init__(self) -> None: ...


class DmUserExitCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    DmUserExitCi: str


class DmTrimExtend(TaggedObject):
    def __init__(self) -> None: ...
    EndCut: float
    EndStep: float
    StartCut: float
    StartStep: float


class DmTpBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SpecifyClsf(self, clsfFileName: str) -> None:
        ...
    def SpecifyToolPath(self, toolPathName: str) -> None:
        ...


class DmToolPosition(TaggedObject):
    def __init__(self) -> None: ...
    ToolPosition: CAM.DPMItpBuilder.ToolPositionOption
    ToolPositionType: CAM.DmToolPosition.ToolPositionOption


    class ToolPositionOption(enum.Enum):
        On = 0
        Tanto = 1
        Contact = 2
    

class DmSurfBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetCutDirection(self, cutDirection: CAM.DmSurfBuilder.CutDirection) -> None:
        ...
    def GetCutDirection(self) -> CAM.DmSurfBuilder.CutDirection:
        ...
    def SetSurfacePercentageStartFirst(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageStartFirst(self) -> float:
        ...
    def SetSurfacePercentageEndFirst(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageEndFirst(self) -> float:
        ...
    def SetSurfacePercentageStartStep(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageStartStep(self) -> float:
        ...
    def SetSurfacePercentageEndStep(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageEndStep(self) -> float:
        ...
    def SetSurfacePercentageStartLast(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageStartLast(self) -> float:
        ...
    def SetSurfacePercentageEndLast(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageEndLast(self) -> float:
        ...
    def FlipMaterial(self) -> None:
        ...
    CutPatternBuilder: CAM.CutPatternBuilder
    DmSurfCutArea: CAM.DmSurfBuilder.DmSurfCutAreaType
    DmSurfCutPattern: CAM.DmSurfBuilder.DmSurfCutPatternType
    DmSurfCutStep: CAM.DmSurfBuilder.DmSurfCutStepType
    DmSurfCutStepFirstCut: int
    DmSurfCutStepSecondCut: int
    DmSurfCutStepThirdCut: int
    DmSurfCutTraversal: CAM.DmSurfBuilder.DmSurfCutTraversalType
    DmSurfGouge: CAM.DmSurfBuilder.GougeActionType
    DmSurfToolPos: CAM.DmSurfBuilder.ToolPositionType
    DriveGeometry: CAM.SurfaceDriveGeometry
    StepIntolBuilder: CAM.InheritableDoubleBuilder
    StepOuttolBuilder: CAM.InheritableDoubleBuilder
    StepoverBuilder: CAM.StepoverBuilder
    StockDriveBuilder: CAM.InheritableDoubleBuilder


    class ToolPositionType(enum.Enum):
        On = 0
        Tanto = 1
    

    class MatSideType(enum.Enum):
        Same = 0
        Opp = 1
    

    class GougeActionType(enum.Enum):
        None = 0
        Warning = 1
        Skip = 2
        Retract = 3
    

    class DmSurfCutTraversalType(enum.Enum):
        ZigZag = 0
        ZigZagLift = 1
        Zig = 2
    

    class DmSurfCutStepType(enum.Enum):
        Tolerance = 0
        Points = 1
    

    class DmSurfCutPatternType(enum.Enum):
        FollowPeriphery = 0
        Sep1 = 1
        ParallelLines = 2
        Sep2 = 3
        Helical = 4
    

    class DmSurfCutAreaType(enum.Enum):
        SurfacePercent = 0
        DiagonalPoints = 1
    

    class CutDirection(enum.Enum):
        Corner1U = 1
        Corner1V = 2
        Corner2U = 3
        Corner2V = 4
        Corner3U = 5
        Corner3V = 6
        Corner4U = 7
        Corner4V = 8
    

class DmStreamlineCutStep(TaggedObject):
    def __init__(self) -> None: ...
    CutStepType: CAM.DPMItpBuilder.StepMethodOption
    FirstCut: int
    SecondCut: int
    StepIntol: CAM.InheritableDoubleBuilder
    StepOutol: CAM.InheritableDoubleBuilder
    ThirdCut: int


class DmSpiralBuilder(TaggedObject):
    def __init__(self) -> None: ...
    DmSpiralStepoverMenu: CAM.DmSpiralBuilder.DmSpiralStepoverTypes
    PatternCenterPoint: Point
    SpiralRadiusBuilder: CAM.InheritableDoubleBuilder
    SpiralStepoverBuilder: CAM.StepoverBuilder
    SpiralStepoverDistance: float
    SpiralStepoverPercent: float


    class DmSpiralStepoverTypes(enum.Enum):
        Constant = 0
        ToolDiameter = 1
    

class DmRotaryFloorFinishBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetCutDirection(self, cutDirection: CAM.DmRotaryFloorFinishBuilder.CutDirection) -> None:
        ...
    def GetCutDirection(self) -> CAM.DmRotaryFloorFinishBuilder.CutDirection:
        ...
    def FlipMaterial(self) -> None:
        ...
    def SetSurfacePercentageStartFirst(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageStartFirst(self) -> float:
        ...
    def GetSurfacePercentageEndFirst(self) -> float:
        ...
    def SetSurfacePercentageEndFirst(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageStartStep(self) -> float:
        ...
    def SetSurfacePercentageStartStep(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageEndStep(self) -> float:
        ...
    def SetSurfacePercentageEndStep(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageStartLast(self) -> float:
        ...
    def SetSurfacePercentageStartLast(self, dValue: float) -> None:
        ...
    def GetSurfacePercentageEndLast(self) -> float:
        ...
    def SetSurfacePercentageEndLast(self, dValue: float) -> None:
        ...
    CutDirectionType: CAM.DmRotaryFloorFinishBuilder.CutDirType
    CutPatternBuilder: CAM.CutPatternBuilder
    DirectionAxisType: CAM.DmRotaryFloorFinishBuilder.DirectionType
    DmSurfCutArea: CAM.DmRotaryFloorFinishBuilder.DmSurfCutAreaType
    DmSurfCutStep: CAM.DmRotaryFloorFinishBuilder.DmSurfCutStepTypes
    DmSurfCutStepFirstCut: int
    DmSurfCutStepSecondCut: int
    DmSurfCutStepThirdCut: int
    DmSurfGouge: CAM.DmRotaryFloorFinishBuilder.GougeActionTypes
    PartAxisBuilder: CAM.PartAxisBuilder
    StepIntolBuilder: CAM.InheritableDoubleBuilder
    StepOuttolBuilder: CAM.InheritableDoubleBuilder
    TiltAngle: float


    class MatSideType(enum.Enum):
        Same = 0
        Opp = 1
    

    class GougeActionTypes(enum.Enum):
        None = 0
        Warning = 1
        Skip = 2
        Retract = 3
    

    class DmSurfCutStepTypes(enum.Enum):
        Tolerance = 0
        Points = 1
    

    class DmSurfCutAreaType(enum.Enum):
        SurfacePercent = 0
        DiagonalPoints = 1
    

    class DirectionType(enum.Enum):
        AroundAxis = 0
        AlongAxis = 1
    

    class CutDirType(enum.Enum):
        Climb = 0
        Conventional = 1
        Mixed = 2
    

    class CutDirection(enum.Enum):
        Corner1U = 1
        Corner1V = 2
        Corner2U = 3
        Corner2V = 4
        Corner3U = 5
        Corner3V = 6
        Corner4U = 7
        Corner4V = 8
    

class DmRadBuilder(TaggedObject):
    def __init__(self) -> None: ...
    CutPatternBuilder: CAM.CutPatternBuilder
    DpmStepoverBuilder: CAM.StepoverBuilder
    DpmStepoverMaxBuilder: CAM.InheritableDoubleBuilder
    DpmStepoverMinBuilder: CAM.InheritableDoubleBuilder
    DpmrcBoundaryLeftBuilder: CAM.InheritableDoubleBuilder
    DpmrcBoundaryRightBuilder: CAM.InheritableDoubleBuilder
    RadCutMethod: CAM.DmRadBuilder.RadCutMethodType
    RadStepoverType: CAM.DmRadBuilder.RadStepoverTypeType
    RadTraverseDir: CAM.DmRadBuilder.RadTraverseDirType
    StepoverPercentBuilder: CAM.InheritableDoubleBuilder
    StepoverScallopBuilder: CAM.InheritableDoubleBuilder


    class RadTraverseDirType(enum.Enum):
        Forward = 0
        Backward = 1
    

    class RadStepoverTypeType(enum.Enum):
        Constant = 0
        Scallop = 1
        Tool = 2
        Maximum = 3
    

    class RadCutMethodType(enum.Enum):
        Zigzag = 0
        Zig = 1
    

class DmCurveBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateDpmcvDriveCurve(self, section: Section) -> CAM.DriveChainItemBuilder:
        ...
    DpmcvDriveCurves: CAM.DriveChainItemBuilderList
    DpmcvEndPercBuilder: CAM.InheritableDoubleBuilder
    DpmcvNumSegsBuilder: CAM.InheritableIntBuilder
    DpmcvStartPercBuilder: CAM.InheritableDoubleBuilder
    DpmcvStepTolBuilder: CAM.InheritableDoubleBuilder
    DpmcvStepType: CAM.DmCurveBuilder.DpmcvStepTypes


    class DpmcvStepTypes(enum.Enum):
        Tolerance = 0
        Number = 1
    

class DmCmMultiplePassesCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AuxFloor: bool
    CutOnlyAlongFloorAndWall: bool
    Floor: bool
    FloorIncrementBuilder: CAM.InheritableDoubleBuilder
    FloorNumberPassesBuilder: CAM.InheritableIntBuilder
    FloorStepMethodBuilder: NXObject
    FloorStockOffsetBuilder: CAM.InheritableDoubleBuilder
    Order: CAM.DmCmMultiplePassesCiBuilder.OrderType
    Wall: bool
    WallIncrementBuilder: CAM.InheritableDoubleBuilder
    WallNumberPassesBuilder: CAM.InheritableIntBuilder
    WallStepMethod: CAM.DmCmMultiplePassesCiBuilder.WallStepMethodType
    WallStockOffsetBuilder: CAM.InheritableDoubleBuilder


    class WallStepMethodType(enum.Enum):
        Increment = 0
        Passes = 1
    

    class OrderType(enum.Enum):
        WallFirst = 0
        FloorFirst = 1
    

class DmCmBuilder(TaggedObject):
    def __init__(self) -> None: ...
    ContactPositionBottomDistance: CAM.InheritableToolDepBuilder
    ContactPositionDistance: CAM.InheritableToolDepBuilder
    ContactPositionRingHeight: CAM.DmCmBuilder.ContactPositionRingHeightType
    ContactPositionTopDistance: CAM.InheritableToolDepBuilder
    DmCmEndCutDisType: CAM.DmCmBuilder.ExtDisType
    DmCmEndCutExtend: bool
    DmCmEndCutRadio: CAM.DmCmBuilder.DmCmCutPointType
    DmCmEndCutToolAxisGuideVector: CAM.DmCmBuilder.ToolAxisGuideVectorType
    DmCmFloorWallStockFloorBuilder: CAM.InheritableDoubleBuilder
    DmCmFloorWallStockSame: bool
    DmCmFloorWallStockWallBuilder: CAM.InheritableDoubleBuilder
    DmCmMultiplePassesBuilder: CAM.DmCmMultiplePassesCiBuilder
    DmCmStartCutDisType: CAM.DmCmBuilder.ExtDisType
    DmCmStartCutExtend: bool
    DmCmStartCutRadio: CAM.DmCmBuilder.DmCmCutPointType
    DmCmStartCutToolAxisGuideVector: CAM.DmCmBuilder.ToolAxisGuideVectorType
    EndExtDistSpecValueBuilder: CAM.InheritableToolDepBuilder
    FollowWallBottom: bool
    StartExtDistSpecValueBuilder: CAM.InheritableToolDepBuilder
    ToolPositionOffsetBuilder: CAM.InheritableDoubleBuilder


    class ToolAxisGuideVectorType(enum.Enum):
        Auto = 0
        Guide = 1
    

    class ExtDisType(enum.Enum):
        None = 0
        Fixed = 1
        Percent = 2
    

    class DmCmCutPointType(enum.Enum):
        Custom = 0
        Automatic = 1
    

    class ContactPositionRingHeightType(enum.Enum):
        None = 0
        Constant = 1
        Variable = 2
    

class DmBndBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetDmBndIntolOuttol(self) -> float:
        ...
    def SetDmBndIntolOuttol(self, values: float) -> None:
        ...
    def GetBndCutPattern(self) -> CAM.DmBndBuilder.BndCutPatternTypes:
        ...
    def SetBndCutPattern(self, bndCutPattern: CAM.DmBndBuilder.BndCutPatternTypes) -> None:
        ...
    def GetBndCutTraversal(self) -> CAM.DmBndBuilder.BndCutTraversalTypes:
        ...
    def SetBndCutTraversal(self, bndCutTraversal: CAM.DmBndBuilder.BndCutTraversalTypes) -> None:
        ...
    def GetDmBndCutZigDir(self) -> float:
        ...
    def SetDmBndCutZigDir(self, bndCutZigDir: float) -> None:
        ...
    ApplyAtBoundary: bool
    ApplyAtPartSurface: bool
    ApplyFilletAt: CAM.DmBndBuilder.ApplyFilletAtTypes
    BndAddPasses: int
    BndCustomStart: CAM.DmBndBuilder.BndCustomStartTypes
    BndPocketDir: CAM.DmBndBuilder.BndPocketDirTypes
    BndProfilePass: bool
    BndProfilePassStock: float
    CutAngle: CAM.CutAngle
    CutPatternBuilder: CAM.CutPatternBuilder
    CutPatternCenter: CAM.DmBndBuilder.BndPatternCenterTypes
    DisToolEndProj: bool
    DispContact: bool
    DispContactNormal: bool
    DispToolEnd: bool
    DmBndStock: float
    IslandCleanup: bool
    IslandCleanupStatus: bool
    PatternCenterPoint: Point
    RegionConnection: bool
    StepoverBuilder: CAM.StepoverBuilder
    UsePart: CAM.DmBndBuilder.UsePartTypes


    class UsePartTypes(enum.Enum):
        PartContainOff = 0
        PartContainLargestLoop = 1
        PartContainAllLoops = 2
    

    class BndPocketDirTypes(enum.Enum):
        Outward = 0
        Inward = 1
    

    class BndPatternCenterTypes(enum.Enum):
        MethodAutomatic = 0
        MethodSpecify = 1
    

    class BndCutTraversalTypes(enum.Enum):
        ZigZag = 0
        Zig = 1
        ZigContour = 2
        Stepover = 3
    

    class BndCutPatternTypes(enum.Enum):
        FollowPeriphery = 0
        Profile = 1
        Sep1 = 2
        ParallelLines = 3
        RadialLines = 4
        ConcArcs = 5
        Sep2 = 6
        StandardDrive = 7
    

    class BndCustomStartTypes(enum.Enum):
        Custom = 0
        Automatic = 1
    

    class ApplyFilletAtTypes(enum.Enum):
        Boundary = 0
        Surface = 1
        BoundaryAndSurface = 2
    

class DmAmBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AmAddPasses: int
    AmAutoPatCenter: CAM.DmAmBuilder.AutoPatCenterTypes
    AmCutPattern: CAM.DmAmBuilder.AmCutPatternTypes
    AmCutRegionStartEnum: CAM.DmAmBuilder.AmCustomStartTypes
    AmCutTraversal: CAM.DmAmBuilder.AmCutTraversalTypes
    AmPocketDir: CAM.AreaMillingNonSteepContainment.AmPocketDirTypes
    AmSteepOption: CAM.DmAmBuilder.SteepOptTypes
    CutAngle: CAM.CutAngle
    CutPatternBuilder: CAM.CutPatternBuilder
    DmAmRegionCon: bool
    NonSteepCutting: CAM.AreaMillingNonSteepContainment
    OrderRegionsType: CAM.DmAmBuilder.OrderRegionsOptTypes
    PatternCenterPoint: Point
    ProfilePass: bool
    RecognizeFlatOption: bool
    SteepAngle: CAM.InheritableDoubleBuilder
    SteepCutting: CAM.AreaMillingSteepContainment
    SteepOverlapAngle: CAM.InheritableDoubleBuilder
    SteepOverlapDistance: CAM.InheritableToolDepBuilder
    SteepOverlapOption: bool
    SteepOverlapType: CAM.DmAmBuilder.SteepOverlapOptTypes
    StepoverBuilder: CAM.StepoverBuilder


    class SteepOverlapOptTypes(enum.Enum):
        None = 0
        Angle = 1
        Distance = 2
    

    class SteepOptTypes(enum.Enum):
        SteepContainNone = 0
        NonSteepNonDirectional = 1
        SteepDirectional = 2
        SteepAndNonsteep = 3
        Steep = 4
    

    class OrderRegionsOptTypes(enum.Enum):
        Default = 0
        Topdown = 1
        TopdownDepthFirst = 2
    

    class AutoPatCenterTypes(enum.Enum):
        Automatic = 0
        Specify = 1
    

    class AmPocketDirTypes(enum.Enum):
        Outward = 0
        Inward = 1
    

    class AmCutTraversalTypes(enum.Enum):
        ZigZag = 0
        ZigZagWithLifts = 1
        Zig = 2
        Contour = 3
        Stepover = 4
    

    class AmCutPatternTypes(enum.Enum):
        FollowPeriphery = 0
        Profile = 1
        Sep1 = 2
        ParallelLines = 3
        RadialLines = 4
        ConcArcs = 5
    

    class AmCustomStartTypes(enum.Enum):
        Custom = 0
        Automatic = 1
    

class DisplayTool(TaggedObject):
    def __init__(self) -> None: ...
    ToolDisplayFrequency: int
    ToolDisplayType: CAM.DisplayTool.ToolDisplayTypes


    class ToolDisplayTypes(enum.Enum):
        None = 0
        Tool2d = 1
        Tool3d = 2
        Axis = 3
    

class DisplaySilhouette(TaggedObject):
    def __init__(self) -> None: ...
    PercentOfTool: float


class DisplayPath(TaggedObject):
    def __init__(self) -> None: ...
    PathDisplayType: CAM.DisplayPath.PathDisplayTypes
    ReplaySpeed: int


    class PathDisplayTypes(enum.Enum):
        SolidCenter = 0
        DashedCenter = 1
        Silhouette = 2
        Fill = 3
        SilhouetteFill = 4
    

class DisplayPaint(TaggedObject):
    def __init__(self) -> None: ...
    ArrowDisplayFlag: bool
    FeedDisplayFlag: bool


class DimensionRule(TaggedObject):
    def __init__(self) -> None: ...
    Status: bool
    Type: CAM.DimensionRule.Types
    Value: float


    class Types(enum.Enum):
        Value = 0
        ToolDiameter = 1
        FluteLength = 2
    

class DeltaMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    DeltaX: float
    DeltaY: float
    DeltaZ: float
    Intent: CAM.DeltaMoveBuilder.IntentType
    RoundPoint: CAM.RoundPointBuilder


    class IntentType(enum.Enum):
        Wcs = 0
        Mcs = 1
    

class CylindricalMillingCutParameters(CAM.FeatureMillingCutParameters):
    def __init__(self) -> None: ...
    BottomOffset: CAM.VerticalPosition
    ContinuousCut: bool


class CylindricalMillingBuilder(CAM.HoleMachiningBuilder):
    def __init__(self) -> None: ...
    AxialStepover: CAM.StepoverBuilder
    RadialStepover: CAM.StepoverBuilder


class CylinderMillingCutParameters(CAM.CylindricalMillingCutParameters):
    def __init__(self) -> None: ...
    CutDirection: CAM.CylinderMillingCutParameters.CutDirectionTypes


    class CutDirectionTypes(enum.Enum):
        Climb = 0
        Conventional = 1
    

class CylinderMillingBuilder(CAM.CylindricalMillingBuilder):
    def __init__(self) -> None: ...
    AxialDistance: CAM.InheritableToolDepBuilder
    BlankDiameter: CAM.CylinderMillingBuilder.BlankDiameterTypes
    BlankDistance: CAM.InheritableToolDepBuilder
    CleanupPasses: bool
    CutParameters: CAM.CylinderMillingCutParameters
    CutPattern: CAM.CylinderMillingBuilder.CutPatternTypes
    DepthPerRevolution: CAM.CylinderMillingBuilder.DepthPerRevolutionTypes
    DiameterForHelix: CAM.CylinderMillingBuilder.DiameterForHelixTypes
    HelixDiameter: CAM.InheritableToolDepBuilder
    MinimumHelixDiameter: CAM.InheritableToolDepBuilder
    OffsetFromStartDiameter: CAM.InheritableToolDepBuilder
    OppositeDirection: bool
    OppositeDirectionBuilder: CAM.OppositeDirection
    RampAngle: CAM.InheritableDoubleBuilder
    SpiralThickness: CAM.InheritableToolDepBuilder
    StartDiameter: CAM.InheritableToolDepBuilder


    class DiameterForHelixTypes(enum.Enum):
        Diameter = 0
        SpiralThickness = 1
        OffsetFromStartDiameter = 2
    

    class DepthPerRevolutionTypes(enum.Enum):
        Distance = 0
        RampAngle = 1
    

    class CutPatternTypes(enum.Enum):
        Spiral = 0
        Helical = 1
        HelicalAndSpiral = 2
        Circular = 3
    

    class BlankDiameterTypes(enum.Enum):
        Diameter = 0
        Distance = 1
    

class CylinderMilling(CAM.Operation):
    def __init__(self) -> None: ...


class CycleTipRelease(TaggedObject):
    def __init__(self) -> None: ...
    Distance: float
    IsActive: bool


class CycleStepRetract(TaggedObject):
    def __init__(self) -> None: ...
    IsActive: bool
    RetractValue: float


class CycleSpindle(TaggedObject):
    def __init__(self) -> None: ...
    IsActive: bool
    IsReversed: bool
    SpindleMode: CAM.CycleSpindle.Mode
    SpindleSpeed: float


    class Mode(enum.Enum):
        Off = 0
        On = 1
        Rpm = 2
    

class CycleNodragClearance(TaggedObject):
    def __init__(self) -> None: ...
    IsActive: bool
    NodragValue: float


class CycleDwell(TaggedObject):
    def __init__(self) -> None: ...
    Dwell: float
    DwellMode: CAM.CycleDwell.Mode
    IsActive: bool


    class Mode(enum.Enum):
        On = 0
        Off = 1
        Seconds = 2
        Revolutions = 3
    

class CycleCoolant(TaggedObject):
    def __init__(self) -> None: ...
    Coolant: str
    FlowIsActive: bool
    FlowMode: CAM.CycleCoolant.Flow
    IsActive: bool


    class Flow(enum.Enum):
        Low = 0
        Medium = 1
        Hight = 2
    

class Cycle(TaggedObject):
    def __init__(self) -> None: ...
    def GetParameterActive(self, cycleParamName: str) -> bool:
        ...
    def SetParameterActive(self, cycleParamName: str, parameterActive: bool) -> None:
        ...
    def GetIntegerValue(self, cycleParamName: str) -> int:
        ...
    def SetIntegerValue(self, cycleParamName: str, integerValue: int) -> None:
        ...
    def GetDoubleValue(self, cycleParamName: str) -> float:
        ...
    def SetDoubleValue(self, cycleParamName: str, doubleValue: float) -> None:
        ...
    def GetBooleanValue(self, cycleParamName: str) -> bool:
        ...
    def SetBooleanValue(self, cycleParamName: str, booleanValue: bool) -> None:
        ...
    def GetPointValue(self, cycleParamName: str) -> Point3d:
        ...
    def SetPointValue(self, cycleParamName: str, point: Point3d) -> None:
        ...
    def GetVectorValue(self, cycleParamName: str) -> Vector3d:
        ...
    def SetVectorValue(self, cycleParamName: str, vector: Vector3d) -> None:
        ...
    def GetStringValue(self, cycleParamName: str) -> str:
        ...
    def SetStringValue(self, cycleParamName: str, stringValue: str) -> None:
        ...
    AxialStepover: CAM.StepoverBuilder
    CamStatus: bool
    CamValue: int
    CoolantBeforeCut: CAM.CycleCoolant
    CoolantBeforeEngage: CAM.CycleCoolant
    CoolantBeforeRetract: CAM.CycleCoolant
    CsinkDiameter: float
    CycleTrackingPoint: str
    CycleType: str
    Dwell: CAM.Cycle.DwellType
    DwellAtDepth: CAM.CycleDwell
    DwellAtFinalDepth: CAM.CycleDwell
    DwellAtStartPoint: CAM.CycleDwell
    DwellBeforeCut: CAM.CycleDwell
    DwellBeforeEngage: CAM.CycleDwell
    DwellBeforeRetract: CAM.CycleDwell
    DwellFinal: CAM.Cycle.DwellType
    DwellFinalValue: float
    DwellStart: CAM.Cycle.DwellType
    DwellStartValue: float
    DwellValue: float
    EntranceDiameter: float
    FirstCutMode: CAM.Cycle.CutMode
    FirstCutValue: float
    LastCutMode: CAM.Cycle.CutMode
    LastCutValue: float
    MotionOutput: CAM.Cycle.MotionOutputTypes
    NodragClearance: CAM.CycleNodragClearance
    Option: bool
    Orientation: float
    OrientationStatus: bool
    Shift: float
    ShiftStatus: bool
    SpindleBeforeEngage: CAM.CycleSpindle
    SpindleBeforeRetract: CAM.CycleSpindle
    StepClearance: float
    StepClearanceStatus: bool
    StepRetract: CAM.CycleStepRetract
    Text: str
    Times: int
    TimesStatus: bool
    TipRelease: CAM.CycleTipRelease


    class MotionOutputTypes(enum.Enum):
        MachineCycle = 0
        SingleMoves = 1
        InterruptedMoves = 2
    

    class DwellType(enum.Enum):
        On = 0
        Off = 1
        Seconds = 2
        Revolutions = 3
    

    class CutMode(enum.Enum):
        Off = 0
        Value = 1
        Percentage = 2
    

class CutVolumeList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.CutVolume]) -> None:
        ...
    def Append(self, object: CAM.CutVolume) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.CutVolume) -> int:
        ...
    def FindItem(self, index: int) -> CAM.CutVolume:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.CutVolume) -> None:
        ...
    def Erase(self, obj: CAM.CutVolume, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.CutVolume]:
        ...
    def SetContents(self, objects: typing.List[CAM.CutVolume]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.CutVolume, object2: CAM.CutVolume) -> None:
        ...
    def Insert(self, location: int, object: CAM.CutVolume) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CutVolumeGeom(TaggedObject):
    def __init__(self) -> None: ...
    def CreateCutVolume(self) -> CAM.CutVolume:
        ...
    CutVolumes: CAM.CutVolumeList
    Selection: CAM.SelectCAMFeature


class CutVolume(TaggedObject):
    def __init__(self) -> None: ...
    FloorStock: float
    Selection: CAM.SelectCAMFeatureList
    WallStock: float


class CutterExport(TaggedObject):
    def __init__(self) -> None: ...
    def GetHolderExportStatus(self) -> CAM.CutterExport.HolderExportStatus:
        ...
    def GetTrackpointExportStatus(self) -> CAM.CutterExport.TrackpointExportStatus:
        ...
    def SetAttributeAndValue(self, attributes: str, values: str) -> None:
        ...
    def Export(self) -> None:
        ...
    def ExportHolder(self) -> None:
        ...
    def GetValidTargetClasses(self, saveFlag: CAM.CutterExport.SaveFlags, replaceLibref: str) -> str:
        ...
    def GetValidAttributes(self, targetClass: str) -> str:
        ...
    def GetValidValuesOfAttribute(self, attr: str, valueIds: str, valueTexts: str) -> None:
        ...
    HolderLibref: str
    HolderSaveFlag: CAM.CutterExport.SaveFlags
    Libref: str
    SaveFlag: CAM.CutterExport.SaveFlags
    TargetClass: str


    class TrackpointExportStatus(enum.Enum):
        Ok = 0
        Unchanged = 1
        Undefined = 2
        Untried = 3
        Fail = 4
    

    class SaveFlags(enum.Enum):
        Replace = 0
        CreateNew = 1
    

    class HolderExportStatus(enum.Enum):
        Ok = 0
        Unchanged = 1
        Undefined = 2
        Untried = 3
        Fail = 4
    

class CutStrategy(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.CutStrategy.Types


    class Types(enum.Enum):
        LevelZ = 0
        LevelZz = 1
        RampingZ = 2
        RampingZz = 3
        ContourZ = 4
        ContourZz = 5
        PlungeZ = 6
        PlungeZz = 7
        PlungeAlt = 8
        PlungeCastleing = 9
        PartOff = 10
        BlankContourZ = 11
    

class CutSides(TaggedObject):
    def __init__(self) -> None: ...
    Side: CAM.CutSides.SideType


    class SideType(enum.Enum):
        All = 0
        Left = 1
        Right = 2
        LeftRight = 3
        Opposing = 4
        LeftRightLeadingEdge = 5
        LeadingEdge = 6
        TrailingEdge = 7
    

class CutSideBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CutSide: CAM.CutSideBuilder.Option


    class Option(enum.Enum):
        Both = 0
        Left = 1
        Right = 2
    

class CutRegionsData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SortRegions(self) -> None:
        ...
    def GetCentroidPoints(self) -> typing.List[Point3d]:
        ...
    def GetAreas(self) -> float:
        ...
    def GetOrder(self) -> int:
        ...
    IsSorted: bool
    NumberRegions: int


class CutRegionsBuilder(CAM.ObjectContainer):
    def __init__(self) -> None: ...
    def CreateRegions(self) -> None:
        ...
    def ImportRegions(self) -> None:
        ...
    def DeleteAllRegions(self) -> None:
        ...
    def ExecuteSplitCommand(self) -> int:
        ...
    def ExecuteMergeCommand(self) -> int:
        ...
    def ExecuteEditCommand(self) -> int:
        ...
    def ExecuteDeleteCommand(self, value: int, targetSubop: int) -> int:
        ...
    def ExecuteGougeCheckCommand(self) -> int:
        ...
    def ExecuteDeferCommand(self, value: int, targetSubop: int) -> int:
        ...
    def GetSplitSubopCommandBuilder(self, value: int, targetSubop: int) -> CAM.SplitSubopCommand:
        ...
    def GetEditSubopCommandBuilder(self, value: int, targetSubop: int) -> CAM.EditSubopCommand:
        ...
    def GetMergeSubopCommandBuilder(self, value: int, targetSubop: int) -> CAM.MergeSubopCommand:
        ...
    def GetGougeChkSubopCommandBuilder(self, value: int, targetSubop: int) -> CAM.ParamBuilder:
        ...
    def ExecuteReverseCommand(self, value: int, targetSubop: int) -> int:
        ...
    def ExecuteSaveToolAxisCommand(self, value: int, targetSubop: int) -> int:
        ...
    CutRegionsContainment: CAM.CutRegionsBuilder.CutRegionsContainmentTypes
    CutRegionsProgram: CAM.CutRegionsBuilder.CutRegionsProgramTypes
    CutRegionsStatus: CAM.CutRegionsBuilder.CutRegionsStatusTypes


    class CutRegionsStatusTypes(enum.Enum):
        All = 0
        Deferred = 1
        Collision = 2
    

    class CutRegionsProgramTypes(enum.Enum):
        All = 0
        ProgramGroup = 1
    

    class CutRegionsContainmentTypes(enum.Enum):
        All = 0
        Steep = 1
        NonSteep = 2
        Flat = 3
        Mixed = 4
    

class CutPatternBuilder(TaggedObject):
    def __init__(self) -> None: ...
    CutPattern: CAM.CutPatternBuilder.Types


    class Types(enum.Enum):
        None = 0
        FollowPart = 1
        FollowPeriphery = 2
        Helical = 3
        Spiral = 4
        HelicalSpiral = 5
        Mixed = 6
        Profile = 7
        StandardDrive = 8
        Trochoidal = 9
        Zig = 10
        ZigZag = 11
        ZigZagWithLifts = 14
        ZigWithContour = 15
        ZigWithStepover = 16
        ConcentricZig = 17
        ConcentricZigZag = 18
        ConcentricZigWithContour = 19
        ConcentricZigWithStepover = 20
        RadialZig = 21
        RadialZigZag = 22
        RadialZigZagWithLifts = 23
        RadialZigWithContour = 24
        RadialZigWithStepover = 25
        CrosscutZig = 26
        CrosscutZigZag = 27
        CrosscutZigZagWithLifts = 28
        ZlevelZig = 29
        ZlevelZigZag = 30
        ZlevelZigZagWithLifts = 31
        SameAsNonSteep = 32
        AdaptiveZig = 33
        HelicalAroundPart = 34
        AdaptiveRoughing = 35
        ZlevelHelical = 36
        PlanarSpiral = 37
    

class CutParametersTrimControlTypes(enum.Enum):
    None = 0
    Silhoutte = 1
    ExteriorEdges = 2


class CutParametersTraverseOpenPassesTypes(enum.Enum):
    Zig = 0
    ZigZag = 1


class CutParametersToolRunOffTypes(enum.Enum):
    ExtendToRegion = 0
    Specify = 1


class CutParametersSimplifyShapesTypes(enum.Enum):
    None = 0
    ConvexHull = 1
    MinimumBox = 2


class CutParametersRegionSequencingTypes(enum.Enum):
    Standard = 0
    Optimize = 1
    RegionPoints = 2
    PredrillPoints = 3


class CutParametersProfileCutRegionsTypes(enum.Enum):
    AutomaticDetection = 0
    SameAsRoughing = 1


class CutParametersPlungeDirectionTypes(enum.Enum):
    CutDown = 0
    UpAndDown = 1


class CutParametersPatternDirectionTypes(enum.Enum):
    Outward = 0
    Inward = 1
    Automatic = 2


class CutParametersIpwTypes(enum.Enum):
    Thickness = 0
    None = 1
    ThreeDimension = 2
    LevelBased = 3
    TwoDimension = 4
    UseReferenceTool = 5
    Local = 6


class CutParametersFinishPassesTypes(enum.Enum):
    Maintain = 0
    Alternate = 1


class CutParametersFilletsTypes(enum.Enum):
    AddIntoFaces = 0
    AddIntoDiameters = 1
    Split = 2
    Omit = 3


class CutParametersExtendFloorTypes(enum.Enum):
    None = 0
    PartOutline = 1
    BlankOutline = 2


class CutParametersExtendAtStartMode(enum.Enum):
    None = 0
    ToContainmentGeometry = 1
    IncludeAdjacentChamfersOrRounds = 2


class CutParametersCutOrderTypes(enum.Enum):
    LevelFirst = 0
    DepthFirst = 1
    DepthFirstAlways = 2


class CutParametersCutConnectionTypes(enum.Enum):
    Traverse = 0
    ContinuousCuts = 1


class CutParametersCornerFindingTypes(enum.Enum):
    WithinCutArea = 0
    IncludeAdjacentPart = 1


class CutParametersCleanupControlTypes(enum.Enum):
    FollowShoulder = 0
    CutToShoulder = 1


class CutParametersAdjacentBladesTypes(enum.Enum):
    UseBladeStock = 0
    UseCheckStock = 1


class CutParametersActionWhenGougingTypes(enum.Enum):
    Warning = 0
    Skip = 1
    Retract = 2
    Tilt = 3


class CutParameters(TaggedObject):
    def __init__(self) -> None: ...
    CheckIpwCollisions: bool
    CheckSafeClearance: CAM.InheritableToolDepBuilder
    HolderClearance: CAM.InheritableToolDepBuilder
    IpwType: CAM.CutParametersIpwTypes
    NeckClearance: CAM.InheritableToolDepBuilder
    PartSafeClearance: CAM.InheritableToolDepBuilder
    PartStock: CAM.InheritableDoubleBuilder
    ShankClearance: CAM.InheritableToolDepBuilder
    Tolerances: CAM.Inheritable2dLength
    UseToolHolder: bool


class CutLevelPlanar(TaggedObject):
    def __init__(self) -> None: ...
    CommonDepth: CAM.InheritableDoubleBuilder
    CutLevelType: CAM.CutLevelPlanar.Types
    DistanceFromFloor: CAM.InheritableDoubleBuilder
    DistanceFromTop: CAM.InheritableDoubleBuilder
    IncrementalSideStock: CAM.InheritableDoubleBuilder
    MinimumDepth: CAM.InheritableDoubleBuilder
    TopOffCriticalDepths: bool


    class Types(enum.Enum):
        UserDefined = 0
        FloorOnly = 1
        FloorAndCriticalDepth = 2
        CriticalDepth = 3
        Constant = 4
    

class CutLevel(TaggedObject):
    def __init__(self) -> None: ...
    def ApplyGlobalDepthPerCut(self) -> None:
        ...
    def SetTopGeometry(self, currentValue: NXObject) -> None:
        ...
    def InitializeData(self) -> bool:
        ...
    def AddRangeFromDepth(self, rangeDepth: float, depthPerCut: float, measureType: CAM.CutLevel.MeasureTypes, referencedRange: int) -> int:
        ...
    def AddRangeFromGeometry(self, selectedObject: NXObject, depthPerCut: float) -> int:
        ...
    def DeleteRange(self, index: int) -> None:
        ...
    def SetRangeDepth(self, index: int, rangeDepth: float, measureType: CAM.CutLevel.MeasureTypes) -> None:
        ...
    def SetRangeDepthPerCut(self, index: int, depthPerCut: float) -> None:
        ...
    def SetRangeGeometry(self, index: int, geometry: NXObject) -> None:
        ...
    CutLevelType: CAM.CutLevel.Types
    DistanceBelow: CAM.InheritableToolDepBuilder
    GlobalDepthPerCut: CAM.StepoverBuilder
    RangeType: CAM.CutLevel.RangeTypes
    TopOffCriticalDepths: bool
    TopZc: float


    class Types(enum.Enum):
        Constant = 0
        Optimized = 1
        RangeBottom = 2
    

    class RangeTypes(enum.Enum):
        Automatic = 0
        UserDefined = 1
        Single = 2
    

    class MeasureTypes(enum.Enum):
        TopLevel = 0
        RangeTop = 1
        RangeBottom = 2
        WcsOrigin = 3
    

class CutDwell(TaggedObject):
    def __init__(self) -> None: ...
    Revolutions: float
    Time: float
    Type: CAM.CutDwell.Types


    class Types(enum.Enum):
        None = 0
        Time = 1
        Revolutions = 2
    

class CutDirection(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.CutDirection.Types


    class Types(enum.Enum):
        Climb = 0
        Conventional = 1
        Forward = 2
        Reverse = 3
        Mixed = 4
    

class CutDepthChecker(Builder):
    def __init__(self) -> None: ...
    def PerformCheck(self) -> None:
        ...
    CheckNeck: bool
    CreateCurvesForGouges: bool
    CutVolume: float
    DisplayGouges: bool
    MaxCutDepthViolation: float
    NumCutDepthViolations: int
    OperationToCheck: CAM.Operation
    PauseOnGouge: bool
    StopLimit: int
    StopOnLimit: bool


class Cutcom(TaggedObject):
    def __init__(self) -> None: ...
    MinimumAngle: float
    MinimumMove: CAM.InheritableToolDepBuilder
    OutputContactPoint: bool
    OutputPlane: bool
    Suppress: bool
    TrackingPointType: int
    Type: CAM.Cutcom.Types


    class Types(enum.Enum):
        None = 0
        AllFinishPasses = 1
        FinalFinishPass = 2
    

class CutBand(TaggedObject):
    def __init__(self) -> None: ...
    RegionBandBottomDistance: CAM.InheritableDoubleBuilder
    RegionBandBottomNumber: int
    RegionBandTopDistance: CAM.InheritableDoubleBuilder
    RegionBandTopNumber: int
    Type: CAM.CutBand.Types


    class Types(enum.Enum):
        Offsets = 0
        Stepovers = 1
    

class CutAngle(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.CutAngle.Types
    Value: float
    Vector: Direction


    class Types(enum.Enum):
        Auto = 0
        Specify = 1
        LongestLine = 2
        Vector = 3
        TwoWayVector = 4
    

class CustomLoopSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.CustomLoopSet]) -> None:
        ...
    def Append(self, object: CAM.CustomLoopSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.CustomLoopSet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.CustomLoopSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.CustomLoopSet) -> None:
        ...
    def Erase(self, obj: CAM.CustomLoopSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.CustomLoopSet]:
        ...
    def SetContents(self, objects: typing.List[CAM.CustomLoopSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.CustomLoopSet, object2: CAM.CustomLoopSet) -> None:
        ...
    def Insert(self, location: int, object: CAM.CustomLoopSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CustomLoopSet(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.PatchOpeningsBuilder instead..")"""
        ...
    Ignored: bool


class CustomLoops(TaggedObject):
    def __init__(self) -> None: ...
    def CreateLoopSet(self) -> CAM.CustomLoopSet:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.PatchOpeningsBuilder instead..")"""
        ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Features.PatchOpeningsBuilder instead..")"""
        ...
    LoopList: CAM.CustomLoopSetList


class CornerControlBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AdjustFeedRateOption: CAM.CornerControlBuilder.AdjustFeedRateOptions
    CornerControlMethod: CAM.CornerControlBuilder.CornerControlMethods
    FilletingRadius: CAM.InheritableToolDepBuilder
    MaxCompensationFactor: CAM.InheritableDoubleBuilder
    MaximumCornerAngle: CAM.InheritableDoubleBuilder
    MinCompensationFactor: CAM.InheritableDoubleBuilder
    MinimumCornerAngle: CAM.InheritableDoubleBuilder
    NumberOfSteps: int
    PreviousToolDiameter: CAM.InheritableDoubleBuilder
    SlowdownDistanceOption: CAM.CornerControlBuilder.SlowdownDistanceOptions
    SlowdownPercent: CAM.InheritableDoubleBuilder
    SmoothCornersAt: CAM.CornerControlBuilder.SmoothCornersAtOptions
    SmoothingOption: CAM.CornerControlBuilder.SmoothingOptions
    ToolDiameterPercent: CAM.InheritableDoubleBuilder


    class SmoothingOptions(enum.Enum):
        None = 0
        AllPasses = 1
        AllButLastPass = 2
    

    class SmoothCornersAtOptions(enum.Enum):
        Boundary = 0
        PartSurface = 1
        BoundaryAndPartSurface = 2
    

    class SlowdownDistanceOptions(enum.Enum):
        None = 0
        CurrentTool = 1
        PreviousTool = 2
    

    class CornerControlMethods(enum.Enum):
        RollAround = 0
        ExtendAndTrim = 1
        Extend = 2
    

    class AdjustFeedRateOptions(enum.Enum):
        None = 0
        OnAllArcs = 1
    

class ConvertFromMCDBuilder(Builder):
    def __init__(self) -> None: ...
    CounterSpindleFace: Face
    MachineBaseJunctionName: str
    MachineType: CAM.ConvertFromMCDBuilder.MachineTypes
    MachineZeroCsys: CoordinateSystem
    MainSpindleFace: Face
    MillPocketLocation: CAM.ConvertFromMCDBuilder.PocketLocationTypes
    MillPocketNumber: int
    SpindleFace: Face
    ToolMagazine: NXObject
    Turret: NXObject
    TurretPocketNumber: int
    WorkpieceFace: Face


    class PocketLocationTypes(enum.Enum):
        Spindle = 0
        ToolMagazine = 1
    

    class MachineTypes(enum.Enum):
        Mill = 0
        Turn = 1
        MillTurn = 2
    

class ContourAngle(TaggedObject):
    def __init__(self) -> None: ...
    Maximum: float
    Minimum: float


class ContainerMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...


class CollisionPairBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.CollisionPairBuilder]) -> None:
        ...
    def Append(self, object: CAM.CollisionPairBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.CollisionPairBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAM.CollisionPairBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.CollisionPairBuilder) -> None:
        ...
    def Erase(self, obj: CAM.CollisionPairBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.CollisionPairBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAM.CollisionPairBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.CollisionPairBuilder, object2: CAM.CollisionPairBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAM.CollisionPairBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CollisionPairBuilder(Builder):
    def __init__(self) -> None: ...
    CollisionClearance: float
    CollisionEnable: bool
    FirstObjectFilter: CAM.CollisionPairBuilder.Filter
    FirstObjectName: str
    SecondObjectFilter: CAM.CollisionPairBuilder.Filter
    SecondObjectName: str


    class Filter(enum.Enum):
        Component = 0
        Class = 1
        ComponentParent = 2
    

class CollisionConfigurationBuilder(Builder):
    def __init__(self) -> None: ...
    List: CAM.CollisionPairBuilderList


class CleanupSettings(TaggedObject):
    def __init__(self) -> None: ...
    AutoSave: bool
    Directional: bool
    ExtraCrossDrive: bool
    SteepAngle: CAM.InheritableDoubleBuilder
    SteepAreas: bool
    Valleys: bool


class CleanupOutput(TaggedObject):
    def __init__(self) -> None: ...
    OutputType: CAM.CleanupOutput.GeomTypes
    SteepMergeDistance: CAM.InheritableDoubleBuilder
    SteepOverlapDistance: CAM.InheritableDoubleBuilder
    ValleyMergeDistance: CAM.InheritableDoubleBuilder
    ValleyOverlapDistance: CAM.InheritableDoubleBuilder


    class GeomTypes(enum.Enum):
        Point = 0
        Bnd = 1
    

class CircularAboutAxisMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    ArcAxis: Direction
    ArcAxisType: CAM.CircularAboutAxisMoveBuilder.AxisType
    ArcAxisVectorBuilder: CAM.ReferenceVector
    ArcExtendMethod: CAM.CircularAboutAxisMoveBuilder.ExtensionType
    CenterPoint: Point
    CenterPointBuilder: CAM.ReferencePoint
    EndPoint: Point
    EndPointBuilder: CAM.ReferencePoint
    ExtendAngle: float
    ExtendAngleBuilder: CAM.ExpressionDouble
    ExtendDistance: float
    ExtendDistanceBuilder: CAM.ExpressionDouble
    MotionEndType: CAM.CircularAboutAxisMoveBuilder.EndType
    SweepAngle: float
    SweepAngleBuilder: CAM.ExpressionDouble


    class ExtensionType(enum.Enum):
        Angle = 0
        Distance = 1
    

    class EndType(enum.Enum):
        Angle = 0
        Point = 1
    

    class AxisType(enum.Enum):
        Tool = 0
        Vector = 1
    

class ChipControl(TaggedObject):
    def __init__(self) -> None: ...
    ConstantIncrement: CAM.InheritableDoubleBuilder
    DepartureDistance: CAM.InheritableDoubleBuilder
    FirstPlungeOnly: bool
    Type: CAM.ChipControl.Types
    VariableIncrement: CAM.TurnRoughVariableIncrementBuilder


    class Types(enum.Enum):
        None = 0
        ConstBreak = 1
        VarBreak = 2
        ConstClear = 3
        VarClear = 4
    

class ChamferMillingBuilder(CAM.HoleMachiningBuilder):
    def __init__(self) -> None: ...
    ChamferOffset: float
    ChamferReference: CAM.ChamferMillingBuilder.ChamferReferenceType
    CutParameters: CAM.FeatureMillingCutParameters
    DrivePoint: str


    class ChamferReferenceType(enum.Enum):
        MaxDiameter = 0
        MinDiameter = 1
    

class ChamferMilling(CAM.Operation):
    def __init__(self) -> None: ...


class CenterlineDrillVariableIncrementBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetVariableIncrementListData(self, index: int, numberOfCuts: int, increment: float) -> None:
        ...
    def SetVariableIncrementListData(self, numberOfCuts: int, increment: float) -> None:
        ...
    def ModifyVariableIncrementListData(self, index: int, numberOfCuts: int, increment: float) -> None:
        ...
    def DeleteVariableIncrementListData(self, index: int) -> None:
        ...


class CenterlineDrillTurningBuilder(CAM.TurningOperationBuilder):
    def __init__(self) -> None: ...
    def GetCycleTrackingPoint(self) -> str:
        ...
    def SetCycleTrackingPoint(self, name: str) -> None:
        ...
    BreakThrough: bool
    BreakThroughDistance: CAM.InheritableDoubleBuilder
    CenterlineCycle: CAM.CenterlineDrillTurningBuilder.CycleTypes
    ChipRemovalIncrementType: CAM.CenterlineDrillTurningBuilder.RemovalIncrementTypes
    ClearanceDistance: CAM.InheritableDoubleBuilder
    ConstantIncrement: CAM.InheritableDoubleBuilder
    CrossHoleAngle: CAM.InheritableDoubleBuilder
    CrossHoleCircle: NXObject
    CrossHoleDiameter: CAM.InheritableDoubleBuilder
    CrossHoleDistance: CAM.InheritableDoubleBuilder
    DepthDistance: CAM.InheritableDoubleBuilder
    DepthEndPoint: Point
    DepthOffset: CAM.InheritableDoubleBuilder
    DepthOption: CAM.CenterlineDrillTurningBuilder.DepthTypes
    DepthReference: CAM.CenterlineDrillTurningBuilder.DepthReferenceTypes
    DrillStep: CAM.InheritableDoubleBuilder
    DrillStepModifier1: CAM.InheritableDoubleBuilder
    DrillStepModifier2: CAM.InheritableDoubleBuilder
    DrillingLocation: CAM.CenterlineDrillTurningBuilder.DrillingLocationTypes
    DwellType: CAM.CenterlineDrillTurningBuilder.DwellTypes
    DwellValue: CAM.InheritableDoubleBuilder
    EngageDistance: CAM.InheritableDoubleBuilder
    EntranceDiameter: CAM.InheritableDoubleBuilder
    FinalRetractDistance: CAM.InheritableDoubleBuilder
    FinalRetractType: CAM.CenterlineDrillTurningBuilder.FinalRetractTypes
    NonCuttingBuilder: CAM.NcmTurningBuilder
    OffCenterDistance: CAM.InheritableDoubleBuilder
    OutputOption: CAM.CenterlineDrillTurningBuilder.OutputOptionTypes
    RepositionDistance: CAM.InheritableDoubleBuilder
    ReverseDirection: bool
    SafeOrDepartureDistance: CAM.InheritableDoubleBuilder
    SpindleStop: CAM.CenterlineDrillTurningBuilder.SpindleStopTypes
    StartPosition: CAM.CenterlineDrillTurningBuilder.StartPositionTypes
    StartPositionPoint: Point
    VariableIncrementList: CAM.CenterlineDrillVariableIncrementBuilder


    class StartPositionTypes(enum.Enum):
        Automatic = 0
        Specify = 1
    

    class SpindleStopTypes(enum.Enum):
        None = 0
        BeforeRetract = 1
    

    class RemovalIncrementTypes(enum.Enum):
        Constant = 0
        Variable = 1
    

    class OutputOptionTypes(enum.Enum):
        MachineCycle = 0
        Simulated = 1
    

    class FinalRetractTypes(enum.Enum):
        ToStartPosition = 0
        Manual = 1
    

    class DwellTypes(enum.Enum):
        None = 0
        Time = 1
        Revolutions = 2
    

    class DrillingLocationTypes(enum.Enum):
        OnCenterline = 0
        OffCenterline = 1
    

    class DepthTypes(enum.Enum):
        Distance = 0
        EndPoint = 1
        CrossHoleDimensions = 2
        CrossHole = 3
        ShoulderDepth = 4
        CountersinkDiameter = 5
    

    class DepthReferenceTypes(enum.Enum):
        ToolTip = 0
        ToolShoulder = 1
        CycleTrackingPoint = 2
    

    class CycleTypes(enum.Enum):
        Drill = 0
        DrillDeep = 1
        DrillBreakChip = 2
        Tap = 3
        TapFloat = 4
        Bore = 5
    

class CenterlineDrillTurning(CAM.TurningOperation):
    def __init__(self) -> None: ...


class CavityMillingBuilder(CAM.PlanarOperationBuilder):
    def __init__(self) -> None: ...
    BlankGeometry: CAM.Geometry
    CutLevel: CAM.CutLevel
    TrimBoundary: CAM.Boundary


class CavityMilling(CAM.PlanarOperation):
    def __init__(self) -> None: ...


class CAMSetup(CAM.CAMObject):
    def __init__(self) -> None: ...
    def Show2dWorkpiece(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def Show2dWorkpieceIn(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def Show2dWorkpieceOut(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def Show3dWorkpiece(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def ParallelCreate3d(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def ShowSpinning3dWorkpiece(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def Delete3dWorkpieces(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def GenerateToolPath(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def ReplayToolPath(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def ListToolPath(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def DeleteToolPath(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def OutputClsf(self, objects: typing.List[CAM.CAMObject], clsfFormat: str, outfileName: str, outputUnits: CAM.CAMSetup.OutputUnits) -> None:
        ...
    def Postprocess(self, objects: typing.List[CAM.CAMObject], machineType: str, outfileName: str, outputUnits: CAM.CAMSetup.OutputUnits) -> None:
        ...
    def PostprocessWithSetting(self, objects: typing.List[CAM.CAMObject], machineType: str, outfileName: str, outputUnits: CAM.CAMSetup.OutputUnits, outputWarning: CAM.CAMSetup.PostprocessSettingsOutputWarning, reviewTool: CAM.CAMSetup.PostprocessSettingsReviewTool) -> None:
        ...
    def CutObjects(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject]) -> None:
        ...
    def MoveObjects(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject], destinationObject: CAM.CAMObject, pastePosition: CAM.CAMSetup.Paste) -> None:
        ...
    def BufferObjects(self, view: CAM.CAMSetup.View, objectsToBeBuffered: typing.List[CAM.CAMObject]) -> None:
        ...
    def CopyObjects(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject], destinationObject: CAM.CAMObject, pastePosition: CAM.CAMSetup.Paste) -> typing.List[CAM.CAMObject]:
        ...
    def CopyObjectsWithReference(self, view: CAM.CAMSetup.View, objectsToBeMoved: typing.List[CAM.CAMObject], destinationObject: CAM.CAMObject, pastePosition: CAM.CAMSetup.Paste) -> typing.List[CAM.CAMObject]:
        ...
    def CreateToolPathDivideBuilder(self, tpObjectsToDivide: typing.List[CAM.CAMObject]) -> CAM.ToolPathDivideBuilder:
        ...
    def DivideToolPaths(self, objects: typing.List[CAM.CAMObject], builder: CAM.ToolPathDivideBuilder) -> None:
        ...
    def LockToolPaths(self, objects: typing.List[CAM.CAMObject], lock: bool) -> None:
        ...
    def IsToolPathLocked(self, object: CAM.CAMObject) -> bool:
        ...
    def ApproveObjects(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def UnapproveObjects(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def CreateOperationTransformBuilder(self, objectsToTransform: typing.List[CAM.CAMObject]) -> CAM.OperationTransformBuilder:
        ...
    def CreatePreprocessGeometryBuilder(self) -> CAM.PreprocessGeometryBuilder:
        ...
    def CreateSurfaceRegions(self, feature: Features.Feature) -> CAM.SurfaceRegions:
        ...
    def CreateFeatureRecognitionBuilder(self, param: CAM.CAMObject) -> CAM.FeatureRecognitionBuilder:
        ...
    def CreateFeatureTeaching(self, param: CAM.CAMObject) -> CAM.FeatureTeaching:
        ...
    def CreateMapFeatureTeaching(self, param: CAM.CAMObject) -> CAM.MapFeatureTeaching:
        ...
    def CreateOperationTeaching(self, param: CAM.CAMObject) -> CAM.OperationTeaching:
        ...
    def CreateOperationSetTeaching(self, param: CAM.CAMObject) -> CAM.OperationSetTeaching:
        ...
    def Optimize(self, objects: typing.List[CAM.CAMObject], consolidateTools: bool, minimizeToolChanges: bool, createOptimizationGroup: bool) -> None:
        ...
    def SetTemplateStatus(self, objects: typing.List[CAM.CAMObject], useAsParent: bool, createIfParentCreated: bool) -> None:
        ...
    def GougeCheck(self, objects: typing.List[CAM.CAMObject], checkForHolderCollision: bool) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use new version with additional arguments instead.")"""
        ...
    def GougeCheck(self, objects: typing.List[CAM.CAMObject], checkForHolderCollision: bool, useParametric: bool, useUserdefStock: bool, userdefStock: float) -> None:
        ...
    def CustomizationUpdateFromTemplate(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def CustomizationUpdateFromObject(self, destinationObject: CAM.CAMObject, sourceObject: CAM.CAMObject) -> None:
        ...
    def SetMachiningData(self, objects: typing.List[CAM.CAMObject]) -> typing.List[CAM.CAMObject.ErrorItem]:
        ...
    def HasSuppressedGeom(self, param: CAM.CAMObject) -> bool:
        ...
    def RemoveSuppressedGeom(self, param: CAM.CAMObject) -> None:
        ...
    def CreateToolPathSplitBuilder(self, tpObjectsToDivide: typing.List[CAM.CAMObject]) -> CAM.ToolPathSplitBuilder:
        ...
    def SplitToolPaths(self, objects: typing.List[CAM.CAMObject], builder: CAM.ToolPathSplitBuilder) -> None:
        ...
    def CreateFeedsBuilder(self, params: typing.List[CAM.CAMObject]) -> CAM.ObjectsFeedsBuilder:
        ...
    def CreateObjectNotes(self, opr: CAM.CAMObject) -> CAM.ObjectNotes:
        ...
    def IsOperation(self, camobject: CAM.CAMObject) -> bool:
        ...
    def IsGroup(self, camObject: CAM.CAMObject) -> bool:
        ...
    def GetRoot(self, branch: CAM.CAMSetup.View) -> CAM.NCGroup:
        ...
    def CreateNCAssistantBuilder(self) -> CAM.NCAssistantBuilder:
        ...
    def CreateFeedsOptimizeBuilder(self, param: CAM.CAMObject) -> CAM.FeedsOptimizeBuilder:
        ...
    def CreateObjectsUdeSet(self, params: typing.List[CAM.CAMObject], udeType: CAM.CAMSetup.Ude) -> CAM.ObjectsUdeSet:
        ...
    def CreateObjectsUdeSet(self, params: typing.List[CAM.CAMObject], udeType: CAM.CAMSetup.Ude, features: typing.List[CAM.CAMFeature]) -> CAM.ObjectsUdeSet:
        ...
    def MinToolLen(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def CreateFeatureProcessBuilder(self) -> CAM.FeatureProcessBuilder:
        ...
    def RetrieveTool(self, libRef: str, success: bool) -> CAM.Tool:
        ...
    def RetrieveTool(self, libRef: str, target: CAM.CAMObject, nextTarget: CAM.CAMObject, success: bool) -> CAM.Tool:
        ...
    def CreateToolPathTiltBuilder(self, tpObjectsToTilt: typing.List[CAM.CAMObject]) -> CAM.ToolPathTiltBuilder:
        ...
    def TiltToolPaths(self, objects: typing.List[CAM.CAMObject], builder: CAM.ToolPathTiltBuilder) -> None:
        ...
    def CreateNcmctPartMountingBuilder(self, libRef: str) -> CAM.NcmctPartMountingBuilder:
        ...
    def RetrieveDevice(self, libRef: str) -> CAM.NCGroup:
        ...
    def ParallelGenerate(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def GetPartMaterial(self) -> str:
        ...
    def SetPartMaterial(self, libRef: str) -> None:
        ...
    def CreateCutDepthChecker(self) -> CAM.CutDepthChecker:
        ...
    def RemoveMachine(self) -> None:
        ...
    def DeleteVnckMachineData(self) -> None:
        ...
    def GetCamExitObject(self) -> CAM.CAMObject:
        ...
    def GetPartMaterialData(self, libref: str, name: str, description: str, code: str, hardness: str) -> None:
        ...
    def GetMachineLibref(self) -> str:
        ...
    def RestoreDependencies(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def UpdateGeometryDependencies(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def RemoveDependencies(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def SwitchLayerLayout(self, object: CAM.CAMObject) -> None:
        ...
    def TrimToolPath(self, operationBuilder: CAM.OperationBuilder) -> None:
        ...
    def CreateMirrorBuilder(self, objectsToMirror: typing.List[CAM.CAMObject]) -> CAM.MirrorBuilder:
        ...
    def CreateEditMirrorBuilder(self, objectsToMirror: typing.List[CAM.CAMObject]) -> CAM.MirrorBuilder:
        ...
    def CreateObjectWorkInstructionBuilder(self, param: CAM.CAMObject) -> CAM.ObjectWorkInstructionBuilder:
        ...
    def CreateWorkInstructionOutputBuilder(self) -> CAM.WorkInstructionOutputBuilder:
        ...
    def DeleteWorkInstructions(self, objects: typing.List[CAM.CAMObject]) -> None:
        ...
    def CreateWorkInstructionBuilder(self, param: CAM.CAMObject) -> CAM.WorkInstructionBuilder:
        ...
    def UpdateResourcesOnRule(self) -> bool:
        ...
    def CreateGougeCheckBuilder(self, objects: typing.List[CAM.CAMObject]) -> CAM.GougeCheckBuilder:
        ...
    def CopyFromComponent(self) -> None:
        ...
    def CreateTransitionPath(self, nctask: CAM.NCGroup) -> None:
        ...
    def DeleteTransitionPath(self, nctask: CAM.NCGroup) -> None:
        ...
    CAMGroupCollection: CAM.NCGroupCollection
    CAMOperationCollection: CAM.OperationCollection
    IsLibrarySetup: bool
    LibraryReference: str
    OutputBallCenter: bool


    class View(enum.Enum):
        ProgramOrder = 0
        MachineMethod = 1
        Geometry = 2
        MachineTool = 3
    

    class Ude(enum.Enum):
        Start = 0
        End = 1
    

    class PostprocessSettingsReviewTool(enum.Enum):
        On = 0
        Off = 1
        PostDefined = 2
    

    class PostprocessSettingsOutputWarning(enum.Enum):
        Yes = 0
        No = 1
        PostDefined = 2
    

    class Paste(enum.Enum):
        Before = 0
        Inside = 1
        After = 2
    

    class OutputUnits(enum.Enum):
        Inch = 0
        Metric = 1
        PostDefined = 2
    

class CAMSession(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def SpecifyConfiguration(self, configFile: str) -> None:
        ...
    def GetTemplateTypes(self) -> str:
        ...
    def GetTemplateSubtypes(self, typeName: str, subtypeClass: CAM.CAMSession.ObjectSubtype) -> str:
        ...
    def CreateCamPreferences(self) -> CAM.Preferences:
        ...
    def SetMcsDisplay(self, displayMCS: bool) -> None:
        ...
    def GetMcsDisplay(self) -> bool:
        ...
    def InitializeSystemDialogCustomization(self, locationForCustomizationFile: str) -> None:
        ...
    def EndSystemDialogCustomization(self) -> None:
        ...
    def MakeSystemDialogs(self, templateType: str, part: Part) -> None:
        ...
    def IsSystemDialog(self, paramObj: CAM.CAMObject) -> bool:
        ...
    def GetDialogCustomization(self, paramObj: CAM.CAMObject, itemIds: int, itemLabels: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    PathDisplay: CAM.PathDisplay


    class ObjectSubtype(enum.Enum):
        Setup = 0
        Operation = 1
        Program = 2
        Tool = 3
        Method = 4
        Geometry = 5
    

class CamPathToolpathEventType(enum.Enum):
    Motion = 0
    Ude = 1
    System = 2
    LevelMarker = 3
    Marker = 4


class CamPathToolpathEventLocation(enum.Enum):
    Before = 0
    After = 1
    End = 2


class CamPathToolAxisType(enum.Enum):
    Three = 0
    Five = 1


class CamPathMotionType(enum.Enum):
    Undefined = 0
    Rapid = 1
    Engage = 2
    Cut = 3
    Retract = 4
    FirstCut = 5
    Approach = 6
    Stepover = 7
    Departure = 8
    Return = 9
    Traversal = 10
    SideCut = 11
    From = 12
    Gohome = 13
    Cycle = 14
    InternalLift = 15


class CamPathMotionShapeType(enum.Enum):
    Undefined = 0
    Linear = 1
    Circular = 2
    Helical = 3
    Nurbs = 4


class CamPathFeedUnitType(enum.Enum):
    PerMinute = 0
    PerRevolution = 1
    None = 2


class CamPathDir(enum.Enum):
    Clockwise = 0
    Counterclockwise = 1


class CamPathContactType(enum.Enum):
    None = 0
    TwoDimensional = 1
    ThreeDimensional = 2


class CamPathContactMotionShapeType(enum.Enum):
    Undefined = 0
    Linear = 1
    Circular = 2


class CamOperationMotionType(enum.Enum):
    Undefined = 0
    Rapid = 1
    Engage = 2
    Cut = 3
    Retract = 4
    FirstCut = 5
    Approach = 6
    Stepover = 7
    Departure = 8
    Return = 9
    Traversal = 10
    SideCut = 11
    From = 12
    Gohome = 13
    Cycle = 14
    InternalLift = 15


class CamOperationMotionShapeType(enum.Enum):
    Undefined = 0
    Linear = 1
    CircularCw = 2
    CircularCcw = 3
    Point = 4
    HelicalCw = 5
    HelicalCcw = 6
    Nurbs = 7


class CamOperationMotionPosType():
    ToolEnd: Point3d
    ToolAxis: Vector3d
    def ToString(self) -> str:
        ...
    def __init__(self, ToolEnd: Point3d, ToolAxis: Vector3d) -> None: ...


class CamOperationMotionPostDataType():
    FifthAnglePos: float
    PrevPosDataFlag: bool
    def ToString(self) -> str:
        ...
    def __init__(self, FifthAnglePos: float, PrevPosDataFlag: bool) -> None: ...


class CamOperationMotionContactDataType():
    ContactPt: CAM.CamOperationMotionPosType
    ContactArcAxis: Vector3d
    ContactArcCenter: Point3d
    ContactArcRadius: float
    ContactShape: CAM.CamOperationMotionShapeType
    def ToString(self) -> str:
        ...


class CamOperationLinearMotionDataType():
    EventType: CAM.ToolpathEventType
    MotionType: CAM.CamOperationMotionType
    MotionShape: CAM.CamOperationMotionShapeType
    Feedrate: CAM.CamOperationFeedContentType
    FeedFactor: float
    EndPt: Point3d
    ToolAxis: Vector3d
    def ToString(self) -> str:
        ...


class CamOperationHelicalMotionDataType():
    EventType: CAM.ToolpathEventType
    MotionType: CAM.CamOperationMotionType
    MotionShape: CAM.CamOperationMotionShapeType
    Feedrate: CAM.CamOperationFeedContentType
    FeedFactor: float
    EndPt: Point3d
    ToolAxis: Vector3d
    ArcAxis: Vector3d
    ArcCenter: Point3d
    ArcRadius: float
    Tolerance: float
    Slope: float
    def ToString(self) -> str:
        ...


class CamOperationFeedUnitType(enum.Enum):
    Undefined = 0
    None = 1
    PerMinute = 2
    PerRevolution = 3


class CamOperationFeedContentType():
    Value: float
    Unit: CAM.CamOperationFeedUnitType
    def ToString(self) -> str:
        ...
    def __init__(self, Value: float, Unit: CAM.CamOperationFeedUnitType) -> None: ...


class CamOperationCircularMotionDataType():
    EventType: CAM.ToolpathEventType
    MotionType: CAM.CamOperationMotionType
    MotionShape: CAM.CamOperationMotionShapeType
    Feedrate: CAM.CamOperationFeedContentType
    FeedFactor: float
    EndPt: Point3d
    ToolAxis: Vector3d
    ArcAxis: Vector3d
    ArcCenter: Point3d
    ArcRadius: float
    Tolerance: float
    def ToString(self) -> str:
        ...


class CAMObject(NXObject):
    def __init__(self) -> None: ...
    def SetIntegerValue(self, title: str, value: int) -> None:
        ...
    def SetRealValue(self, title: str, value: float) -> None:
        ...
    def SetStringValue(self, title: str, value: str) -> None:
        ...
    def SetBooleanValue(self, title: str, value: bool) -> None:
        ...
    def SetObject(self, title: str, value: NXObject) -> None:
        ...
    def SetFeedRate(self, title: str, value: float, unit: CAM.CAMObject.FeedRateUnit) -> None:
        ...
    def SetWireEdmFeedRate(self, title: str, value: float, side: int) -> None:
        ...
    def SetFeedRateColor(self, title: str, value: int) -> None:
        ...
    def SetIntegerArrayValue(self, title: str, value: int) -> None:
        ...
    def SetRealArrayValue(self, title: str, value: float) -> None:
        ...
    def SetStringArrayValue(self, title: str, value: str) -> None:
        ...
    def SetObjectArrayValue(self, title: str, value: typing.List[NXObject]) -> None:
        ...
    def GetIntegerValue(self, title: str) -> int:
        ...
    def GetRealValue(self, title: str) -> float:
        ...
    def GetBooleanValue(self, title: str) -> bool:
        ...
    def GetStringValue(self, title: str) -> str:
        ...
    def GetObject(self, title: str) -> NXObject:
        ...
    def GetFeedRate(self, title: str, value: float) -> CAM.CAMObject.FeedRateUnit:
        ...
    def GetWireEdmFeedRate(self, title: str, value: float) -> int:
        ...
    def GetFeedRateColor(self, title: str) -> int:
        ...
    def GetIntegerArrayValue(self, title: str) -> int:
        ...
    def GetRealArrayValue(self, title: str) -> float:
        ...
    def GetStringArrayValue(self, title: str) -> str:
        ...
    def GetObjectArrayValue(self, title: str) -> typing.List[NXObject]:
        ...
    def GetStatus(self) -> CAM.CAMObject.Status:
        ...
    def Remove911Attribute(self, attrId: CAM.CAMObject.Attr) -> None:
        ...
    def RemoveAll911Attributes(self) -> None:
        ...
    def Has911Attribute(self, attrId: CAM.CAMObject.Attr) -> bool:
        ...
    def GetPath(self) -> CAM.Path:
        ...
    def SavePath(self, theBuilder: CAM.Path) -> None:
        ...
    def AskPathExists(self) -> bool:
        ...
    def CreateEmptyPath(self) -> CAM.Path:
        ...
    def ConvertToExplorerDialog(self) -> None:
        ...


    class Status(enum.Enum):
        Complete = 0
        Repost = 1
        Regen = 2
        Approved = 4
    

    class FeedRateUnit(enum.Enum):
        None = 0
        PerMinute = 1
        PerRevolution = 2
    

    class CAMObjectErrorItem():
        ObjectTag: CAM.CAMObject
        ErrorCode: int
        def ToString(self) -> str:
            ...
        def __init__(self, ObjectTag: CAM.CAMObject, ErrorCode: int) -> None: ...
    

    class Attr(enum.Enum):
        ProjDiffTaxis = 1
        ProfileFlipMside = 2
        BndSplineTangent = 3
        BlankNormalDiffTaxis = 4
        BndHasSleepObj = 5
        ClrnrNotParallelTaxis = 6
        BndNotParallelFloor = 7
        FloorNotUpToDate = 8
        SingleProfileWithFirstCut = 9
        CutterConversionProblem = 10
        AcceptDrivePosition = 100
        Reparametrization = 110
        BetweenFromStart = 120
        CurveCutRange = 130
        FixGssmCornerData = 140
        PlmConversion = 150
        PlmFeedcomp = 151
        PlmFillet = 152
        PlmSlowdown = 153
        PlmGeometry = 154
        WedmPoints = 160
        CavityMillInheritTrimBnds = 170
        RtdObsolete = 1000
        ZlevelHolderParamChange = 2000
        NcmObsoleteSeqControl = 2100
        NcmObsoleteCustomFeed = 2101
        NcmObsoleteLocalRetract = 2102
        NcmClearTraversalZero = 2103
        NcmObsoleteEngretToClearance = 2104
        GmcInvalidNxVersion = 2201
        ProbingInvalidNxVersion = 2202
        InspPathInvalidNxVersion = 2300
        CustomDataGougingObsolete = 2301
        CustomDataGougingPartObsolete = 2302
        CustomDataGougingDriveObsolete = 2303
        CustomDataIgnoreLoopsObsolete = 2304
        CustomDataIgnoreLoopsRemoved = 2305
        LimitToolRunOn = 2400
        ScoprNcmChangeLinearNormalToPart = 2401
        PossibleToolAxisProblem = 2402
    

class CamInspectionOperationInneroutertypes(enum.Enum):
    Inner = 0
    Outer = 1


class CamInspectionOperationFeaturetypes(enum.Enum):
    None = -1
    Arc = 0
    Circle = 1
    Point = 2
    Sphere = 3
    Surface = 4
    Pattern = 5
    Curve = 6
    Cylinder = 7
    Cone = 8
    Plane = 9
    Line = 10
    Cparln = 11
    SlotTab = 12
    SurfaceOfRevolution = 13
    Torus = 14
    EdgePoint = 15


class CamInspectionOperationExtenttypes(enum.Enum):
    Bounded = 0
    Unbounded = 1


class CamInspectionOperationCsysreferencetypes(enum.Enum):
    RelativetoPCS = 0
    Absolute = 1


class CAMFeatureList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.CAMFeature]) -> None:
        ...
    def Append(self, object: CAM.CAMFeature) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.CAMFeature) -> int:
        ...
    def FindItem(self, index: int) -> CAM.CAMFeature:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.CAMFeature) -> None:
        ...
    def Erase(self, obj: CAM.CAMFeature, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.CAMFeature]:
        ...
    def SetContents(self, objects: typing.List[CAM.CAMFeature]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.CAMFeature, object2: CAM.CAMFeature) -> None:
        ...
    def Insert(self, location: int, object: CAM.CAMFeature) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CAMFeatureCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.CAMFeature]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.CAMFeature:
        ...
    def Tag(self) -> Tag: ...



class CAMFeature(CAM.FBM.Feature):
    def __init__(self) -> None: ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def GetProcessStatus(self, group: CAM.NCGroup) -> CAM.CAMFeature.ProcessStatus:
        ...
    def GetGroups(self) -> typing.List[CAM.NCGroup]:
        ...
    def GetOperations(self) -> typing.List[CAM.Operation]:
        ...
    def ApproveChanges(self) -> None:
        ...
    def GetGeometry(self) -> typing.List[DisplayableObject]:
        ...
    Attributes: CAM.CAMAttributeCollection
    CoordinateSystem: CartesianCoordinateSystem
    Name: str
    SourceType: str
    Status: CAM.CAMFeature.State
    Type: str


    class State(enum.Enum):
        Deleted = 0
        Changed = 1
        Updated = 2
        UpToDate = 3
    

    class ProcessStatus(enum.Enum):
        Empty = 0
        Regenerate = 1
        Incomplete = 2
        Complete = 3
    

class CAMAttributeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAM.CAMAttribute]:
        ...
    def __init__(self, owner: CAM.CAMFeature) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, sid: str) -> CAM.CAMAttribute:
        ...
    def AddAttribute(self, name: str, type: CAM.CAMAttribute.ValueType) -> CAM.CAMAttribute:
        ...
    def Tag(self) -> Tag: ...



class CAMAttribute(NXObject):
    def __init__(self) -> None: ...
    def GetIntegerValue(self) -> int:
        ...
    def SetIntegerValue(self, attributeValue: int) -> None:
        ...
    def GetDoubleValue(self) -> float:
        ...
    def SetDoubleValue(self, attributeValue: float) -> None:
        ...
    def GetBoolValue(self) -> bool:
        ...
    def SetBoolValue(self, attributeValue: bool) -> None:
        ...
    def GetStringValue(self) -> str:
        ...
    def SetStringValue(self, name: str) -> None:
        ...
    def GetPoint3Value(self) -> Point3d:
        ...
    def SetPoint3Value(self, attributeValue: Point3d) -> None:
        ...
    def GetVector3Value(self) -> Vector3d:
        ...
    def SetVector3Value(self, attributeValue: Vector3d) -> None:
        ...
    def RemoveValue(self) -> None:
        ...
    def RemoveOverriddenValue(self) -> None:
        ...
    DisplayName: str
    IsOverridden: bool
    Name: str
    Type: CAM.CAMAttribute.ValueType


    class ValueType(enum.Enum):
        Integer = 0
        Double = 1
        String = 2
        Bool = 3
        Point3 = 4
        Vector3 = 5
    

class BoundaryWireEDM(CAM.Boundary):
    def __init__(self) -> None: ...


class BoundaryTurnVariableStockSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.BoundaryTurnVariableStockSet]) -> None:
        ...
    def Append(self, object: CAM.BoundaryTurnVariableStockSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.BoundaryTurnVariableStockSet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.BoundaryTurnVariableStockSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.BoundaryTurnVariableStockSet) -> None:
        ...
    def Erase(self, obj: CAM.BoundaryTurnVariableStockSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.BoundaryTurnVariableStockSet]:
        ...
    def SetContents(self, objects: typing.List[CAM.BoundaryTurnVariableStockSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.BoundaryTurnVariableStockSet, object2: CAM.BoundaryTurnVariableStockSet) -> None:
        ...
    def Insert(self, location: int, object: CAM.BoundaryTurnVariableStockSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BoundaryTurnVariableStockSet(TaggedObject):
    def __init__(self) -> None: ...
    DistanceFromBoundary: float
    Feed: CAM.BoundaryTurnVariableStockSet.FeedType
    FeedUnit: CAM.BoundaryTurnSet.FeedUnitTypes
    FeedValue: float
    PositionFromStart: float


    class FeedType(enum.Enum):
        None = 0
        Specify = 1
    

class BoundaryTurnVariableStock(TaggedObject):
    def __init__(self) -> None: ...
    def CreateItemBuilder(self) -> CAM.BoundaryTurnVariableStockSet:
        ...
    PositionalValues: CAM.BoundaryTurnVariableStock.PositionType
    StockList: CAM.BoundaryTurnVariableStockSetList


    class PositionType(enum.Enum):
        Distance = 0
        Percent = 1
    

class BoundaryTurnSet(CAM.BoundarySet):
    def __init__(self) -> None: ...
    CustomStock: bool
    FeedUnit: CAM.BoundaryTurnSet.FeedUnitTypes
    FeedValue: float
    IgnoreFineFinishOffset: bool
    Stock: float


    class FeedUnitTypes(enum.Enum):
        None = 0
        PerMinute = 1
        PerRevolution = 2
    

class BoundaryTurnMemberSet(CAM.BoundaryMemberSet):
    def __init__(self) -> None: ...
    ConcaveCorners: CAM.BoundaryTurnMemberSet.ConcaveCornersTypeValue
    Corner1: CAM.BoundaryTurnMemberCorner
    Corner2: CAM.BoundaryTurnMemberCorner
    CustomFeed: CAM.BoundaryTurnMemberFeed
    Events: CAM.BoundaryTurnMemberEvents
    FineFinishCorner1: CAM.BoundaryTurnMemberFineFinishCorner
    FineFinishCorner2: CAM.BoundaryTurnMemberFineFinishCorner
    FineFinishOffset: CAM.BoundaryTurnMemberFineFinishOffset
    IgnoreFineFinishOffset: bool
    IgnoreMember: bool
    OffsetBuilder: CAM.BoundaryTurnMemberOffset


    class ConcaveCornersTypeValue(enum.Enum):
        Extend = 0
        ConnectLinear = 1
    

class BoundaryTurnMemberOffset(Builder):
    def __init__(self) -> None: ...
    AxialDistance: float
    Distance: float
    DistanceType: CAM.BoundaryTurnMemberOffset.DistanceTypeMode
    EndDistance: float
    Method: CAM.BoundaryTurnMemberOffset.MethodType
    Mode: CAM.BoundaryTurnMemberOffset.ModeType
    RadialDistance: float
    StartDistance: float
    VariableStock: CAM.BoundaryTurnVariableStock
    Vector: NXObject
    VectorDistance: float


    class ModeType(enum.Enum):
        None = 0
        General = 1
        Tolerance = 2
        Legacy = 3
    

    class MethodType(enum.Enum):
        Constant = 0
        Axial = 1
        Vector = 2
        Conical = 3
        Variable = 4
    

    class DistanceTypeMode(enum.Enum):
        Nominal = 0
        Diameter = 1
    

class BoundaryTurnMemberFineFinishOffset(Builder):
    def __init__(self) -> None: ...
    Status: CAM.BoundaryTurnMemberFineFinishOffset.StatusValue
    Type: CAM.BoundaryTurnMemberFineFinishOffset.TypeValue
    Value: float


    class TypeValue(enum.Enum):
        Nominal = 0
        Diameter = 1
    

    class StatusValue(enum.Enum):
        None = 0
        Specify = 1
    

class BoundaryTurnMemberFineFinishCorner(Builder):
    def __init__(self) -> None: ...
    AngleValue: float
    AppliedToType: CAM.BoundaryTurnMemberFineFinishCorner.AppliedTo
    CleanupType: CAM.BoundaryTurnMemberFineFinishCorner.Cleanup
    Distance: float
    Type: CAM.BoundaryTurnMemberFineFinishCorner.ValueType


    class ValueType(enum.Enum):
        General = 0
        AngularLine = 1
        TangentialLine = 2
        ShortenArcOrChamfer = 3
    

    class Cleanup(enum.Enum):
        None = 0
        Automatic = 1
        Manual = 2
    

    class AppliedTo(enum.Enum):
        CurrentSegment = 0
        PreviousSegment = 1
    

class BoundaryTurnMemberFeed(Builder):
    def __init__(self) -> None: ...
    CustomFeedType: CAM.BoundaryTurnMemberFeed.FeedType
    FeedUnit: CAM.BoundaryTurnSet.FeedUnitTypes
    FeedValue: float


    class FeedType(enum.Enum):
        None = 0
        Specify = 1
    

class BoundaryTurnMemberEvents(Builder):
    def __init__(self) -> None: ...
    EndOfPath: CAM.PostEventsCiBuilder
    StartOfPath: CAM.PostEventsCiBuilder


class BoundaryTurnMemberCorner(Builder):
    def __init__(self) -> None: ...
    Angle: float
    AngleType: CAM.BoundaryTurnMemberCorner.AngleValueType
    CornerFeedType: CAM.BoundaryTurnMemberCorner.FeedType
    Distance: float
    FeedUnit: CAM.BoundaryTurnSet.FeedUnitTypes
    FeedValue: float
    Radius: float
    Shape: CAM.BoundaryTurnMemberCorner.ShapeType
    Type: CAM.BoundaryTurnMemberCorner.CornerType


    class ShapeType(enum.Enum):
        None = 0
        Roundbeforestock = 1
        Breakbeforestock = 2
        Roundafterstock = 3
        Breakafterstock = 4
    

    class FeedType(enum.Enum):
        None = 0
        Specify = 1
    

    class CornerType(enum.Enum):
        General = 0
        ConstantRadiusChamfer = 1
        KeepTangentPoint = 2
    

    class AngleValueType(enum.Enum):
        None = 0
        Currentsegment = 1
        Previoussegment = 2
    

class BoundaryTurnBlank(Builder):
    def __init__(self) -> None: ...
    AutoPosition: bool
    BlankType: CAM.BoundaryTurnBlank.Type
    Boundary: CAM.Boundary
    Diameter: float
    EquidistantStock: float
    FaceStock: float
    FlipDirection: bool
    InnerDiameter: float
    Length: float
    MountingPosition: CAM.BoundaryTurnBlank.Position
    OuterDiameter: float
    Point: Point
    RadialStock: float
    ReferencePoint: Point
    TargetPoint: Point


    class Type(enum.Enum):
        Bar = 0
        Tube = 1
        Curve = 2
        Workspace = 3
    

    class Position(enum.Enum):
        AtHeadstock = 0
        AwayfromHeadstock = 1
    

class BoundarySetWireEDM(CAM.BoundarySet):
    def __init__(self) -> None: ...
    def CreateBoundaryMemberSetWireEdm(self) -> CAM.BoundaryMemberSetWireEDM:
        ...
    def AddTopFace(self, face: TaggedObject, pickPoint: Point3d) -> None:
        ...
    def AppendSideFaces(self, faces: typing.List[TaggedObject], pickPoint: Point3d) -> None:
        ...
    def RemoveSideFace(self, face: TaggedObject) -> None:
        ...
    def AppendCurvesToWireframe(self, curves: typing.List[NXObject], pickPoint: Point3d, matrix: Matrix3x3) -> None:
        ...
    def RemoveCurvesFromWireframe(self, curves: typing.List[NXObject]) -> None:
        ...
    ControlPoints: CAM.WedmCustomBoundaryDataBuilder
    CustomStock: bool
    CustomTolerances: bool
    InTolerance: float
    OutTolerance: float
    Stock: float


class BoundarySetPlanarMill(CAM.BoundarySet):
    def __init__(self) -> None: ...
    def CreateBoundaryMemberSetPlanarMill(self) -> CAM.BoundaryMemberSetPlanarMill:
        ...
    def ExtendOrTrimStartPoint(self, distance: float) -> None:
        ...
    def ExtendOrTrimEndPoint(self, distance: float) -> None:
        ...
    def MoveStartPoint(self, bndSet: CAM.BoundaryMemberSetPlanarMill, distance: float) -> None:
        ...
    def CreateCurveBoundaryFromPermanent(self) -> None:
        ...
    BlankDistance: float
    CustomBlankDistance: bool
    CustomFeed: bool
    CustomStock: bool
    CustomTolerance: bool
    FeedUnit: CAM.BoundarySetPlanarMill.FeedUnitTypes
    FeedValue: float
    InTolerance: float
    OutTolerance: float
    Stock: float


    class TrimExtendPosition(enum.Enum):
        AtStart = 0
        AtEnd = 1
        AtStartAndEnd = 2
        Unknown = 3
    

    class FeedUnitTypes(enum.Enum):
        None = 0
        PerMinute = 1
        PerRevolution = 2
    

class BoundarySetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.BoundarySet]) -> None:
        ...
    def Append(self, object: CAM.BoundarySet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.BoundarySet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.BoundarySet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.BoundarySet) -> None:
        ...
    def Erase(self, obj: CAM.BoundarySet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.BoundarySet]:
        ...
    def SetContents(self, objects: typing.List[CAM.BoundarySet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.BoundarySet, object2: CAM.BoundarySet) -> None:
        ...
    def Insert(self, location: int, object: CAM.BoundarySet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BoundarySet(TaggedObject):
    def __init__(self) -> None: ...
    def AppendCurves(self, curves: typing.List[NXObject], pickPoint: Point3d, matrix: Matrix3x3) -> None:
        ...
    def RemoveCurves(self, curves: typing.List[NXObject]) -> None:
        ...
    def CreateBoundaryMemberSet(self) -> CAM.BoundaryMemberSet:
        ...
    BoundaryMemberList: CAM.BoundaryMemberSetList
    BoundaryType: CAM.BoundarySet.BoundaryTypes
    CustomOffset: bool
    Offset: float
    OffsetIntent: CAM.ParamValueIntent
    Plane: Plane
    PlaneType: CAM.BoundarySet.PlaneTypes
    PointList: SelectTaggedObjectList
    SelectObject: SelectTaggedObject
    ToolPosition: CAM.BoundarySet.ToolPositionTypes
    ToolSide: CAM.BoundarySet.ToolSideTypes


    class ToolSideTypes(enum.Enum):
        InsideOrLeft = 0
        OutsideOrRight = 1
    

    class ToolPositionTypes(enum.Enum):
        On = 0
        Contact = 1
    

    class PlaneTypes(enum.Enum):
        Automatic = 0
        UserDefined = 1
    

    class BoundaryTypes(enum.Enum):
        Closed = 0
        Open = 1
    

class BoundaryPlanarMill(CAM.Boundary):
    def __init__(self) -> None: ...
    def AppendFaceBoundary(self, face: TaggedObject, ignoreHole: bool, ignoreIsland: bool, ignoreChamfer: bool, toolSide: CAM.BoundarySet.ToolSideTypes, convexEdges: int, concaveEdges: int) -> typing.List[CAM.BoundarySet]:
        ...


class BoundaryMillingSet(CAM.BoundarySet):
    def __init__(self) -> None: ...
    def CreateBoundaryMillingMemberSet(self) -> CAM.BoundaryMillingMemberSet:
        ...
    CustomFeedRate: bool
    CustomStock: bool
    FeedUnit: CAM.BoundaryMillingMemberSet.FeedUnitTypes
    FeedValue: float
    Stock: float


class BoundaryMillingMemberSet(CAM.BoundaryMemberSet):
    def __init__(self) -> None: ...
    CustomFeedRate: bool
    CustomStock: bool
    EndEventsBuilder: CAM.PostEventsCiBuilder
    FeedUnit: CAM.BoundaryMillingMemberSet.FeedUnitTypes
    FeedValue: float
    StartEventsBuilder: CAM.PostEventsCiBuilder
    Stock: float


    class FeedUnitTypes(enum.Enum):
        None = 0
        PerMinute = 1
        PerRevolution = 2
    

class BoundaryMemberSetWireEDM(CAM.BoundaryMemberSet):
    def __init__(self) -> None: ...
    def CreateMemberEvent(self) -> CAM.BoundaryMemberEvents:
        ...
    CustomStock: bool
    CustomTolerances: bool
    InTolerance: float
    OutTolerance: float
    PostEventsList: CAM.BoundaryMemberEventsList
    Stock: float


class BoundaryMemberSetPlanarMill(CAM.BoundaryMemberSet):
    def __init__(self) -> None: ...
    def StartOnThisMember(self) -> None:
        ...
    CustomFeed: bool
    CustomStock: bool
    CustomTolerance: bool
    FeedUnit: CAM.BoundaryMemberSetPlanarMill.FeedUnitTypes
    FeedValue: float
    InTolerance: float
    OutTolerance: float
    Stock: float
    ToolPosition: int


    class FeedUnitTypes(enum.Enum):
        None = 0
        PerMinute = 1
        PerRevolution = 2
    

class BoundaryMemberSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.BoundaryMemberSet]) -> None:
        ...
    def Append(self, object: CAM.BoundaryMemberSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.BoundaryMemberSet) -> int:
        ...
    def FindItem(self, index: int) -> CAM.BoundaryMemberSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.BoundaryMemberSet) -> None:
        ...
    def Erase(self, obj: CAM.BoundaryMemberSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.BoundaryMemberSet]:
        ...
    def SetContents(self, objects: typing.List[CAM.BoundaryMemberSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.BoundaryMemberSet, object2: CAM.BoundaryMemberSet) -> None:
        ...
    def Insert(self, location: int, object: CAM.BoundaryMemberSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BoundaryMemberSet(TaggedObject):
    def __init__(self) -> None: ...
    ConnectMember: CAM.BoundaryMemberSet.ConnectMemberType
    CustomOffset: bool
    Offset: float


    class ConnectMemberType(enum.Enum):
        Extend = 0
        Direct = 1
    

class BoundaryMemberEventsList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAM.BoundaryMemberEvents]) -> None:
        ...
    def Append(self, object: CAM.BoundaryMemberEvents) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAM.BoundaryMemberEvents) -> int:
        ...
    def FindItem(self, index: int) -> CAM.BoundaryMemberEvents:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAM.BoundaryMemberEvents) -> None:
        ...
    def Erase(self, obj: CAM.BoundaryMemberEvents, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAM.BoundaryMemberEvents]:
        ...
    def SetContents(self, objects: typing.List[CAM.BoundaryMemberEvents]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAM.BoundaryMemberEvents, object2: CAM.BoundaryMemberEvents) -> None:
        ...
    def Insert(self, location: int, object: CAM.BoundaryMemberEvents) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BoundaryMemberEvents(Builder):
    def __init__(self) -> None: ...
    EndOfPath: CAM.PostEventsCiBuilder
    StartOfPath: CAM.PostEventsCiBuilder


class Boundary(TaggedObject):
    def __init__(self) -> None: ...
    def CreateBoundarySet(self) -> CAM.BoundarySet:
        ...
    def CreateBoundaryMillingSet(self) -> CAM.BoundaryMillingSet:
        ...
    def CreateBoundaryTurnSet(self) -> CAM.BoundaryTurnSet:
        ...
    def CreateBoundarySetWireEdm(self) -> CAM.BoundarySetWireEDM:
        ...
    def AppendFaceBoundary(self, face: TaggedObject, ignoreHole: bool, ignoreIsland: bool, ignoreChamfer: bool, toolSide: CAM.BoundarySet.ToolSideTypes) -> typing.List[CAM.BoundarySet]:
        ...
    def RemoveFaceBoundary(self, face: TaggedObject) -> None:
        ...
    def CreateBoundarySetPlanarMill(self) -> CAM.BoundarySetPlanarMill:
        ...
    def Validate(self) -> bool:
        ...
    BoundaryList: CAM.BoundarySetList


class BlendFinish(CAM.Blade):
    def __init__(self) -> None: ...
    CutBand: CAM.CutBand
    DriveMode: CAM.DriveMode
    GeometryToFinish: CAM.BladeFinishGeom
    Sequence: CAM.Sequence
    SidesToCut: CAM.CutSides
    StartPoint: CAM.BladeStartPoint
    Stepover: CAM.StepoverBuilder


class BlankIpw(TaggedObject):
    def __init__(self) -> None: ...
    def SetSource(self, sourcePartName: str, sourceName: str) -> None:
        ...
    def GetSource(self, sourcePart: NXObject) -> CAM.CAMObject:
        ...
    def GetStatus(self) -> CAM.BlankIpw.StatusTypes:
        ...
    def Update(self) -> CAM.BlankIpw.StatusTypes:
        ...
    def IsValidSource(self, object: CAM.CAMObject) -> bool:
        ...


    class StatusTypes(enum.Enum):
        UpToDate = 0
        OutOfDate = 1
        UnableToUpdate = 2
        None = 3
        Unknown = 4
    

class BladeStartPoint(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.BladeStartPoint.Types


    class Types(enum.Enum):
        LeadingEdge = 0
        TrailingEdge = 1
    

class BladeRough(CAM.Blade):
    def __init__(self) -> None: ...
    BladeCleanupPasses: bool
    CutStart: CAM.BladeCutStart
    StartClosestToPreviousRetract: bool
    Stepover: CAM.StepoverBuilder


class BladeFinishGeom(TaggedObject):
    def __init__(self) -> None: ...
    Type: CAM.BladeFinishGeom.Types


    class Types(enum.Enum):
        Blade = 0
        SplitterOne = 1
        SplitterTwo = 2
        SplitterThree = 3
        SplitterFour = 4
        SplitterFive = 5
    

class BladeFinish(CAM.Blade):
    def __init__(self) -> None: ...
    GeometryToFinish: CAM.BladeFinishGeom
    SidesToCut: CAM.CutSides
    StartPoint: CAM.BladeStartPoint


class BladeEdge(TaggedObject):
    def __init__(self) -> None: ...
    BackoffAngle: CAM.InheritableDoubleBuilder
    BackoffDistance: CAM.InheritableToolDepBuilder
    BladeEdgePoint: CAM.BladeEdge.EdgePointType
    EdgeDefinition: CAM.BladeEdge.EdgeDefinitionType
    ExtendRadialDistance: CAM.InheritableToolDepBuilder
    ExtendTangentialDistance: CAM.InheritableToolDepBuilder


    class EdgePointType(enum.Enum):
        AlongBladeDirection = 0
        AlongPartAxis = 1
        NoCurling = 2
    

    class EdgeDefinitionType(enum.Enum):
        Inherit = 0
        Specify = 1
    

class BladeCutStart(TaggedObject):
    def __init__(self) -> None: ...
    From: CAM.BladeCutStart.Type


    class Type(enum.Enum):
        LeftOppositeRotaryaxis = 1
        CenterOppositeRotaryaxis = 2
        RightOppositeRotaryaxis = 3
        LeftAlongRotaryaxis = 4
        CenterAlongRotaryaxis = 5
        RightAlongRotaryaxis = 6
    

class BladeCutLevels(Builder):
    def __init__(self) -> None: ...
    DepthMode: CAM.BladeCutLevels.DepthModeTypes
    DepthPerCut: CAM.BladeCutLevels.DepthPerCutTypes
    Distance: CAM.InheritableToolDepBuilder
    EndPercent: float
    FinishPassAtEnd: bool
    FinishPassAtStart: bool
    HubExtensions: CAM.BladeCutLevels.HubExtensionsTypes
    IncompleteLevels: CAM.BladeCutLevels.IncompleteLevelsTypes
    NumberOfCuts: int
    NumberOfIntermediateCuts: int
    RangeDepth: CAM.BladeCutLevels.RangeDepthTypes
    ReduceDepthPerCutWhenEmbeded: bool
    ScallopDistance: CAM.InheritableDoubleBuilder
    StartPercent: float
    StripeEndPercent: float
    StripeStartPercent: float
    StripeType: CAM.BladeCutLevels.StripeTypes


    class StripeTypes(enum.Enum):
        Top = 0
        Intermediate = 1
        Bottom = 2
    

    class RangeDepthTypes(enum.Enum):
        Automatic = 0
        Specify = 1
        MultiStripes = 2
    

    class IncompleteLevelsTypes(enum.Enum):
        OutputAndWarn = 0
        Omit = 1
    

    class HubExtensionsTypes(enum.Enum):
        None = 0
        ToPreviousDepth = 1
        ToTrailingEdge = 2
    

    class DepthPerCutTypes(enum.Enum):
        Constant = 0
        Scallop = 1
    

    class DepthModeTypes(enum.Enum):
        OffsetsFromHub = 0
        OffsetsFromShroud = 1
        OffsetsAlongToolAxis = 2
        InterpolateFromShroudToHub = 3
    

class Blade(TaggedObject):
    def __init__(self) -> None: ...
    CutDirection: CAM.CutDirection.Types
    CutPattern: CAM.CutPatternBuilder
    LeadingEdge: CAM.BladeEdge
    TrailingEdge: CAM.BladeEdge


    class MaterialSideType(enum.Enum):
        Same = 0
        Opposite = 1
    

class BaseBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetCustomizableItemBuilder(self, name: str) -> TaggedObject:
        ...
    def GetCustomizableItemNames(self) -> str:
        ...
    def Validate(self) -> bool:
        ...


class BarrelToolBuilder(CAM.MillingToolBuilder):
    def __init__(self) -> None: ...
    TlBarrelRadBuilder: CAM.InheritableDoubleBuilder
    TlYcenBarrelBuilder: CAM.InheritableDoubleBuilder


class AxisMoveBuilder(CAM.BaseBuilder):
    def __init__(self) -> None: ...
    Length: float
    Type: CAM.AxisMoveBuilder.Types


    class Types(enum.Enum):
        Omit = 0
        Automatic = 1
        Specify = 2
        MachineLimit = 3
    

class AvoidanceMethodsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AvoidanceMethod: CAM.AvoidanceMethodsBuilder.JaOperationAvoidanceMethodType


    class JaOperationAvoidanceMethodType(enum.Enum):
        None = 0
        Retract = 1
        Tilt = 2
        Warning = 3
        Stop = 4
        Tiltstop = 5
    

class AreaMillingSteepContainment(CAM.AreaMillingContainment):
    def __init__(self) -> None: ...
    AreaMillingCutDirection: CAM.AreaMillingContainment.CutDirectionTypes
    CutLevelType: CAM.AreaMillingSteepContainment.CutLevelTypes
    DepthPerCut: CAM.StepoverBuilder


    class CutLevelTypes(enum.Enum):
        Constant = 0
        Optimized = 1
    

class AreaMillingNonSteepContainment(CAM.AreaMillingContainment):
    def __init__(self) -> None: ...
    AddCenterPasses: bool
    AmAddPasses: int
    AmAutoPatCenter: CAM.AreaMillingNonSteepContainment.AutoPatCenterTypes
    AmPocketDir: CAM.AreaMillingNonSteepContainment.AmPocketDirTypes
    CutAngleBuilder: CAM.CutAngle
    NumberOfStepoversPerSide: CAM.InheritableIntBuilder
    PatternCenterPoint: Point
    PatternDirection: CAM.AreaMillingNonSteepContainment.PatternDirectionTypes
    PatternSmooth: bool


    class PatternDirectionTypes(enum.Enum):
        Outward = 0
        Inward = 1
    

    class AutoPatCenterTypes(enum.Enum):
        Automatic = 0
        Specify = 1
    

    class AmPocketDirTypes(enum.Enum):
        Outward = 0
        Inward = 1
    

class AreaMillingContainment(TaggedObject):
    def __init__(self) -> None: ...
    CutPattern: CAM.CutPatternBuilder
    Stepover: CAM.StepoverBuilder


    class CutDirectionTypes(enum.Enum):
        Climb = 0
        Conventional = 1
    

class ArcOutputTypeCiBuilder(TaggedObject):
    def __init__(self) -> None: ...
    NurbAngleTolerance: float
    NurbFitTolerance: float
    NurbJoinSegments: bool
    OutputType: CAM.ArcOutputTypeCiBuilder.OutputTypes
    SplineArcOutputType: CAM.ArcOutputTypeCiBuilder.SplineArcOutputTypes
    SplineFitTolerance: float
    SplineFitToleranceType: CAM.ArcOutputTypeCiBuilder.SplineFitToleranceTypes
    SplineLineOutputType: CAM.ArcOutputTypeCiBuilder.SplineLineOutputTypes


    class SplineLineOutputTypes(enum.Enum):
        Spline = 0
        Line = 1
    

    class SplineFitToleranceTypes(enum.Enum):
        Percent = 0
        Value = 1
    

    class SplineArcOutputTypes(enum.Enum):
        Spline = 0
        ArcPerpToTaxis = 1
        ArcPerpParallelToTaxis = 2
    

    class OutputTypes(enum.Enum):
        LinearOnly = 0
        CirPerpToTaxis = 1
        CirPerpParallelToTaxis = 2
        Nurbs = 3
        Spline = 4
    

class AngularAboutAxisMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    DeltaX: CAM.ExpressionDouble
    DeltaY: CAM.ExpressionDouble
    HelicalPitch: CAM.ExpressionDouble
    SpiralPitch: CAM.ExpressionDouble
    SweepAngle: CAM.ExpressionDouble


class AlongToolAxisMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    Distance: float
    DistanceBuilder: CAM.ExpressionDouble
    RoundPoint: CAM.RoundPointBuilder


class AlongMcsAxisMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    XAxis: float
    YAxis: float
    ZAxis: float


class AlongMachineAxisMoveBuilder(CAM.MoveBuilder):
    def __init__(self) -> None: ...
    AAxis: float
    AAxisMove: CAM.AxisMoveBuilder
    AOutput: bool
    BAxis: float
    BAxisMove: CAM.AxisMoveBuilder
    BOutput: bool
    CAxis: float
    CAxisMove: CAM.AxisMoveBuilder
    COutput: bool
    XAxis: float
    XAxisMove: CAM.AxisMoveBuilder
    XOutput: bool
    YAxis: float
    YAxisMove: CAM.AxisMoveBuilder
    YOutput: bool
    ZAxis: float
    ZAxisMove: CAM.AxisMoveBuilder
    ZOutput: bool


class AcrossVoids(TaggedObject):
    def __init__(self) -> None: ...
    MinTraverseDistance: CAM.InheritableToolDepBuilder
    MotionType: CAM.AcrossVoids.MotionTypes


    class MotionTypes(enum.Enum):
        Follow = 0
        Cut = 1
        Traverse = 2
    

