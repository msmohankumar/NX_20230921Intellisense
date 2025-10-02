from ....NXOpen import *
from ...Features import *
from ..StructureDesign import *

import typing
import enum

class SuperFrameBuilder(Features.StructureDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    def AddAction(self, sourceCurves: typing.List[Curve], actionType: Features.StructureDesign.SuperFrameBuilder.TransformTypes, actionDirection: Vector3d, actionDistance: float) -> None:
        ...
    def UndoAction(self) -> None:
        ...
    def CreateCurves(self) -> None:
        ...
    def CopyCurve(self, curveTag: Curve) -> Curve:
        ...
    def UpdateCurve(self, curveTag: Curve, startPoint: Point3d, endPoint: Point3d) -> None:
        ...
    def DeleteCurve(self, curveTag: Curve) -> None:
        ...
    def ReparentAndDeleteCurve(self, curveTag: Curve) -> None:
        ...
    BoundaryCurve: ScCollector
    Height: Expression
    InputMode0: Features.StructureDesign.SuperFrameBuilder.InputModes
    InputMode1: Features.StructureDesign.SuperFrameBuilder.InputModes
    InputMode2: Features.StructureDesign.SuperFrameBuilder.InputModes
    Length: Expression
    Point0: Point
    Point0X: Expression
    Point0Y: Expression
    Point0Z: Expression
    Point1: Point
    Point1X: Expression
    Point1Y: Expression
    Point2: Point
    Point2Z: Expression
    SplitCurve: ScCollector
    Width: Expression


    class TransformTypes(enum.Enum):
        Move = 0
        Copy = 1
        Split = 2
        Delete = 3
        None = 4
    

    class InputModes(enum.Enum):
        Coordinates = 0
        Parameters = 1
    

    class BaseTypes(enum.Enum):
        None = 0
        Corners = 1
        Transform = 2
    

class SuperFrame(Features.BodyFeature):
    def __init__(self) -> None: ...


class StiffenerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Alignment: SelectTaggedObjectList
    AttachmentSide: Features.StructureDesign.StiffenerBuilder.AttachmentSides
    DepthOffset: Expression
    FillType: Features.StructureDesign.StiffenerBuilder.FillTypes
    Height: Expression
    HeightType: Features.StructureDesign.StiffenerBuilder.HeightTypes
    OffsetDistance: Expression
    ReverseOffset: bool
    SelectObject: SelectTaggedObject
    StiffenerName: str
    StockData: Features.StructureDesign.FeatureSpreadsheetBuilder
    ThicknessDir: Features.StructureDesign.StiffenerBuilder.ThicknessDirs


    class ThicknessDirs(enum.Enum):
        Upper = 0
        Lower = 1
        Center = 2
    

    class HeightTypes(enum.Enum):
        Default = 0
        Input = 1
    

    class FillTypes(enum.Enum):
        UppperHalf = 0
        LowerHalf = 1
        Full = 2
        MatchedCope = 3
    

    class AttachmentSides(enum.Enum):
        Left = 0
        Right = 1
        Both = 2
    

class Stiffener(Features.BodyFeature):
    def __init__(self) -> None: ...


class SelectCornerList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Features.StructureDesign.Corner) -> bool:
        ...
    def Add(self, objects: typing.List[Features.StructureDesign.Corner]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Features.StructureDesign.Corner, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Features.StructureDesign.Corner) -> bool:
        ...
    def Remove(self, object: Features.StructureDesign.Corner, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Features.StructureDesign.Corner, view1: View, point1: Point3d, selection2: Features.StructureDesign.Corner, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Features.StructureDesign.Corner]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Features.StructureDesign.Corner) -> bool:
        ...
    def SetArray(self, objects: typing.List[Features.StructureDesign.Corner]) -> None:
        ...
    def GetArray(self) -> typing.List[Features.StructureDesign.Corner]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Features.StructureDesign.Corner, view1: View, point1: Point3d, selection2: Features.StructureDesign.Corner, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Features.StructureDesign.Corner, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCorner(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Features.StructureDesign.Corner, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Features.StructureDesign.Corner, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Features.StructureDesign.Corner, view1: View, point1: Point3d, selection2: Features.StructureDesign.Corner, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Features.StructureDesign.Corner, view1: View, point1: Point3d, selection2: Features.StructureDesign.Corner, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Features.StructureDesign.Corner, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Features.StructureDesign.Corner:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Features.StructureDesign.Corner


class RuleBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    ButtOption: Features.StructureDesign.RuleBuilder.ButtOptions
    CopeOption: Features.StructureDesign.RuleBuilder.CopeOptions
    Cutback: Expression
    HorizontalCornerType: Features.StructureDesign.RuleBuilder.CornerTypes
    InnerCornerType: Features.StructureDesign.RuleBuilder.CornerTypes
    Placement: Features.StructureDesign.RuleBuilder.Placements
    VerticalCornerType: Features.StructureDesign.RuleBuilder.CornerTypes


    class Placements(enum.Enum):
        Inside = 0
        Center = 1
        Outside = 2
    

    class CornerTypes(enum.Enum):
        None = 0
        Miter = 1
        Butt = 2
        Cope = 3
        MatchedCope = 4
    

    class CopeOptions(enum.Enum):
        CopeShortest = 0
        CopeLongest = 1
    

    class ButtOptions(enum.Enum):
        ButtShortest = 0
        ButtLongest = 1
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MemberPathBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CoordSystem: CoordinateSystem
    PathMethod: Features.StructureDesign.MemberPathBuilder.MemberPathMethod
    PathOffset: Expression
    PathPoint: Point
    SelectFirstMember: SelectNXObject
    SelectSecondMember: SelectNXObject


    class MemberPathMethod(enum.Enum):
        Members = 0
        Csys = 1
        Point = 2
    

class MemberBuilder(Features.StructureDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    def FlipX(self) -> None:
        ...
    def FlipY(self) -> None:
        ...
    def EvaluateStructurePositionInformation(self, curves: typing.List[NXObject]) -> None:
        ...
    def SetEditingPreviewCorner(self, corner: Features.StructureDesign.Corner) -> None:
        ...
    def GetEditingPreviewCorner(self) -> Features.StructureDesign.Corner:
        ...
    def PrepareBeforeEditingCorner(self, corner: Features.StructureDesign.Corner) -> None:
        ...
    def CleanAfterEditingCorner(self, corner: Features.StructureDesign.Corner) -> None:
        ...
    def CreatePreviewBodies(self) -> int:
        ...
    def DestroyPreviewBodies(self) -> None:
        ...
    def DestroyPreviewBodyMap(self) -> None:
        ...
    def SetPreviewbodyChecksumAttribute(self) -> None:
        ...
    def DeletePreviewCorners(self) -> None:
        ...
    def ClearCombinedCurveMap(self, curves: typing.List[NXObject]) -> None:
        ...
    def ClearAllCombinedCurveMap(self) -> None:
        ...
    def ClearAllAdjustedPath(self) -> None:
        ...
    AlternateOrigin: int
    EnableMergeColinearPath: bool
    EndCornerEnd: Features.StructureDesign.MemberBuilder.EndCornerTypes
    EndCornerStart: Features.StructureDesign.MemberBuilder.EndCornerTypes
    EndLimit: Expression
    FileName: str
    MemberPathEnd: Features.StructureDesign.MemberPathBuilder
    MemberPathStart: Features.StructureDesign.MemberPathBuilder
    PathGeometry: Section
    RotateAngle: Expression
    StartLimit: Expression
    StockData: Features.StructureDesign.FeatureSpreadsheetBuilder
    XOffset: Expression
    YOffset: Expression


    class EndCornerTypes(enum.Enum):
        None = 0
        Miter = 1
        Butt = 2
        Cope = 3
        MatchedCope = 4
        SmartExtend = 5
    

class Member(Features.BodyFeature):
    def __init__(self) -> None: ...


class LibraryBuilder(Builder):
    def __init__(self) -> None: ...
    Catalog: str


class GussetBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AlignmentType: Features.StructureDesign.GussetBuilder.AlignmentTypes
    AngularTolerance: float
    AttachmentOffset: Expression
    AttachmentPointNormal: Vector3d
    DistanceTolerance: float
    FirstFaceSelect: ScCollector
    FlangeData: Features.StructureDesign.FeatureSpreadsheetBuilder
    GussetName: str
    OffsetDistance: Expression
    OrientVector: Direction
    PickPointOnAttachment: Point3d
    PickPointOnReinforcement: Point3d
    PositionType: Features.StructureDesign.GussetBuilder.PositionTypes
    ReinforcementOffset: Expression
    ReinforcementPointNormal: Vector3d
    ReverseAlignEdge: bool
    ReverseAttachmentOffsetFlange: bool
    ReverseFirstFace: bool
    ReverseFlange: bool
    ReverseReinforcementOffsetFlange: bool
    ReverseSecondFace: bool
    SecondFaceSelect: ScCollector
    ThicknessType: Features.StructureDesign.GussetBuilder.ThicknessTypes


    class ThicknessTypes(enum.Enum):
        BothSides = 0
        InnerSide = 1
        OuterSide = 2
    

    class PositionTypes(enum.Enum):
        Offset = 0
        Center = 1
        AlignToEdge = 2
    

    class AlignmentTypes(enum.Enum):
        GussetPlate = 0
        LappedPlate = 1
    

class Gusset(Features.BodyFeature):
    def __init__(self) -> None: ...


class GrabTabBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AnchorPoint: Features.StructureDesign.GrabTabBuilder.AnchorPoints
    Attachment: ScCollector
    GrabTabName: str
    OrientVector: Direction
    PlaceDirection: Features.StructureDesign.GrabTabBuilder.PlaceDirections
    Reference1: SelectNXObject
    Reference1Offset: Expression
    Reference1ReverseFlange: bool
    Reference2: SelectNXObject
    Reference2Offset: Expression
    Reference2ReverseFlange: bool
    RotateAngle: Expression
    StockData: Features.StructureDesign.FeatureSpreadsheetBuilder


    class PlaceDirections(enum.Enum):
        Horizontal = 0
        Vertical = 1
    

    class AnchorPoints(enum.Enum):
        Left = 0
        Center = 1
        Right = 2
    

class GrabTab(Features.BodyFeature):
    def __init__(self) -> None: ...


class FeatureSpreadsheetBuilder(Features.ShipDesign.SteelFeatureSpreadsheetBuilder):
    def __init__(self) -> None: ...


class FeatureParmsBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    AngularTolerance: float
    DistanceTolerance: float


class EndcapBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    Chamfer: bool
    ChamferLength: Expression
    DistanceTolerance: float
    EndCapName: str
    EnumCornerTreatmentType: Features.StructureDesign.EndcapBuilder.CornerTreatmentTypes
    Member: ScCollector
    Offset: Expression
    OffsetRatio: float
    PlacementType: Features.StructureDesign.EndcapBuilder.PlacementTypes
    PreserveOverallLength: bool
    Thickness: Expression


    class PlacementTypes(enum.Enum):
        Inside = 0
        Outside = 1
    

    class CornerTreatmentTypes(enum.Enum):
        None = 0
        Chamfer = 1
        Fillet = 2
    

class Endcap(Features.BodyFeature):
    def __init__(self) -> None: ...


class EditStructureBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateReferenceInfomation(self, selStructure: NXObject) -> None:
        ...
    Catalog: str
    Reference: SelectTaggedObjectList
    ReferenceOrientation: Direction
    Structure: SelectTaggedObject


class EditStockBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def FlipX(self) -> None:
        ...
    def FlipY(self) -> None:
        ...
    def UpdateStockInformation(self, member: NXObject) -> None:
        ...
    AlternateOrigin: int
    EnableTransform: bool
    EndLimit: Expression
    Member: SelectTaggedObjectList
    RotateAngle: Expression
    StartLimit: Expression
    StockData: Features.StructureDesign.FeatureSpreadsheetBuilder
    XOffset: Expression
    YOffset: Expression


class EditCornerBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CreateCorners(self, body: Body, endPoint: Point3d, corners: typing.List[Features.StructureDesign.CornerNodeBuilder]) -> None:
        ...
    def GetCorners(self, corners: typing.List[Features.StructureDesign.CornerNodeBuilder]) -> None:
        ...
    def RemoveCorners(self, corners: typing.List[Features.StructureDesign.CornerNodeBuilder]) -> None:
        ...
    def SetCornerObject(self, corner: Features.StructureDesign.Corner) -> None:
        ...
    def SetEndCorner(self, iNodeIndex: int, endCorner: Features.StructureDesign.MemberBuilder.EndCornerTypes) -> None:
        ...
    def SetMemberIndex(self, iNodeIndex: int, iMemberIndex: int) -> None:
        ...
    def UpdateStockData(self, bOnlyUpdateSize: bool) -> None:
        ...
    def UpdateCopeMemberStockData(self, iMemberIndex: int, bOnlyUpdateSize: bool) -> None:
        ...
    def UpdateAllCopeStockData(self) -> None:
        ...
    def SetInitialStockData(self, bInitial: bool) -> None:
        ...
    def GetStockDataByMember(self, iMemberIndex: int) -> Features.StructureDesign.FeatureSpreadsheetBuilder:
        ...
    def SetCurrentStockData(self, stockData: Features.StructureDesign.FeatureSpreadsheetBuilder) -> None:
        ...
    def ResetStockData(self) -> None:
        ...
    def SetCutback(self, iMemberIndex: int, usCutback: str) -> None:
        ...
    def SetCopeMemberIndex(self, iMemberIndex: int, iRefCopeMemberIndex: int) -> None:
        ...
    def SetParamtersChanged(self, bChanged: bool) -> None:
        ...
    def ClearReferenceMemberFaceInformation(self, iMemberIndex: int) -> None:
        ...
    def ClearReferencedMemberInformation(self, iMemberIndex: int) -> None:
        ...
    def AddReferenceMemberFaceInformation(self, iMemberIndex: int, iRefMemberIndex: int, facePoint: Point3d, faceNormal: Vector3d) -> None:
        ...
    def SetCopeMemberIndexArray(self, iMemberIndex: int, refCopeMemberIndexArray: int) -> None:
        ...
    Corner: Features.StructureDesign.SelectCorner
    StockData: Features.StructureDesign.FeatureSpreadsheetBuilder


class CreateStructureBuilder(Builder):
    def __init__(self) -> None: ...
    Catalog: str
    FileName: str
    Reference: SelectTaggedObjectList
    ReferenceOrientation: Direction
    StructreRootNode: ShipDesign.NavigatorNode
    UpOrientation: Direction


class CornerNodeBuilder(NXObject):
    def __init__(self) -> None: ...
    EndCorner: Features.StructureDesign.MemberBuilder.EndCornerTypes


class Corner(DisplayableObject):
    def __init__(self) -> None: ...


class ContainerBuilder(Builder):
    def __init__(self) -> None: ...
    SelectStructure: Part


class ConsolidateBuilder(Builder):
    def __init__(self) -> None: ...
    Container: Part
    FileName: str
    Structures: SelectTaggedObjectList


class BoltedConnectionBuilder(Features.StructureDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    def UpdateStockSectionTypes(self, sectionModified: bool) -> None:
        ...
    AddFasteners: bool
    BeamColumnConnectionSubType: Features.StructureDesign.BoltedConnectionBuilder.BeamColumnConnectionSubTypes
    BodyOne: ScCollector
    BodyTwo: ScCollector
    BoltedConnectionName: str
    ConfigurationName: str
    ConnectionType: Features.StructureDesign.BoltedConnectionBuilder.ConnectionTypes
    FaceOne: ScCollector
    FaceTwo: ScCollector
    SpliceConnectionSubType: Features.StructureDesign.BoltedConnectionBuilder.SpliceConnectionSubTypes
    StockData: Features.StructureDesign.FeatureSpreadsheetBuilder


    class SpliceConnectionSubTypes(enum.Enum):
        End = 0
        Flange = 1
        Web = 2
    

    class ConnectionTypes(enum.Enum):
        Splice = 0
        BeamColumn = 1
    

    class BeamColumnConnectionSubTypes(enum.Enum):
        End = 0
        LPlate = 1
        FlatPlate = 2
    

class BoltedConnection(Features.BodyFeature):
    def __init__(self) -> None: ...


class BeamPreparationBuilder(Features.StructureDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...
    ComponentName: str
    NonStructureBodies: SelectDisplayableObjectList
    ShowBodies: bool
    StructureComponents: SelectDisplayableObjectList


class BeamPreparation(Features.BodyFeature):
    def __init__(self) -> None: ...


class BeamCurveBuilder(Features.StructureDesign.FeatureParmsBuilder):
    def __init__(self) -> None: ...


class BeamCurve(Features.BodyFeature):
    def __init__(self) -> None: ...


class AssignWeldingAttributesBuilder(Builder):
    def __init__(self) -> None: ...
    SelectionButtWeldingEdges: SelectEdgeList
    SelectionCorners: Features.StructureDesign.SelectCornerList
    SelectionEdgesToBeClear: SelectEdgeList
    SelectionFilletWeldingEdges: SelectEdgeList


