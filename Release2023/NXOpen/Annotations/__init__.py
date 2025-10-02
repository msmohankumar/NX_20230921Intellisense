from ...NXOpen import *
from ..Annotations import *

import typing
import enum

class ZeroToleranceDisplayStyle(enum.Enum):
    BasedOnUnits = 0
    AsZero = 1
    OmittedAndInlined = 2
    Omitted = 3


class WeldStandard(enum.Enum):
    Ansi = 0
    Din = 1
    Jis = 2
    Iso = 3
    Eskd = 4
    Gb = 5
    Last = 6


class WeldCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Weld]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def NewLineWeldData(self) -> Annotations.LineWeldData:
        ...
    def CreateLineWeld(self, lineWeldData: Annotations.LineWeldData, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.LineWeld:
        ...
    def CreatePmiLineWeld(self, lineWeldData: Annotations.LineWeldData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.PmiLineWeld:
        ...
    def CreateLineWeldBuilder(self, weld: Annotations.LineWeld) -> Annotations.LineWeldBuilder:
        ...
    def CreatePmiLineWeldBuilder(self, weld: Annotations.PmiLineWeld) -> Annotations.PmiLineWeldBuilder:
        ...
    def Tag(self) -> Tag: ...



class Weld(Annotations.DraftingAid):
    def __init__(self) -> None: ...


class VerticalTextJustification(enum.Enum):
    Top = 1
    Middle = 2
    Bottom = 3


class VerticalOrdinateMargin(Annotations.OrdinateMargin):
    def __init__(self) -> None: ...


class VerticalOrdinateDimension(Annotations.OrdinateDimension):
    def __init__(self) -> None: ...


class VerticalDimension(Annotations.BaseVerticalDimension):
    def __init__(self) -> None: ...


class Value():
    ItemValue: float
    ValueExpression: Expression
    ValuePrecision: int
    def ToString(self) -> str:
        ...
    def __init__(self, ItemValue: float, ValueExpression: Expression, ValuePrecision: int) -> None: ...


class UserSymbolPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSize(self, sizeType: Annotations.UserSymbolPreferences.SizeType, lengthOrScale: float, heightOrAspectRatio: float) -> None:
        ...
    def SetScaleAndAspectRatio(self, scale: float, aspectRatio: float) -> None:
        ...
    def SetLengthAndHeight(self, length: float, height: float) -> None:
        ...


    class SizeType(enum.Enum):
        LengthHeight = 0
        ScaleAspectRatio = 1
    

class UrlBusinessModifierBuilder(Builder):
    def __init__(self) -> None: ...
    Title: str
    Url: str


class UrlBusinessModifier(Annotations.BusinessModifier):
    def __init__(self) -> None: ...


class UnitsStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AngularSuppressZeros: Annotations.AngularSuppressZeros
    ConvertPrimaryTolerance: bool
    DecimalPointCharacter: Annotations.DecimalPointCharacter
    DimensionAngularFormat: Annotations.AngularDimensionFormat
    DimensionLinearUnits: Annotations.DimensionUnit
    DimensionTolerancePlacement: Annotations.TolerancePlacement
    DisplayLeadingDimensionZeros: bool
    DisplayLeadingToleranceZeros: bool
    DisplayTrailingZeros: bool
    DualDimensionCenterDimensionLine: bool
    DualDimensionFormat: Annotations.DualDimensionPlacement
    DualDimensionUnits: Annotations.DimensionUnit
    DualFractionType: Annotations.DimensionTextFormat
    FractionalDisplay: bool
    LinearFractionType: Annotations.DimensionTextFormat
    NumeratorDegrees: int
    NumeratorFraction: float
    NumeratorMinutes: int
    NumeratorSeconds: int
    ToleranceAngularFormat: Annotations.AngularDimensionFormat


class UnitsFormatPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AngularDimensionFormat: Annotations.AngularDimensionFormat
    AngularToleranceFormat: Annotations.AngularDimensionFormat
    ConvertPrimaryToleranceToDualDimensionUnit: bool
    DecimalPointCharacter: Annotations.DecimalPointCharacter
    DimensionLeadingZero: bool
    DisplayTrailingZeros: bool
    DualDimensionCenterDimensionLine: bool
    DualDimensionPlacement: Annotations.DualDimensionPlacement
    DualDimensionTextFormat: Annotations.DimensionTextFormat
    DualDimensionUnit: Annotations.DimensionUnit
    FractionalDisplay: bool
    NumeratorDegrees: int
    NumeratorFraction: float
    NumeratorMinutes: int
    NumeratorSeconds: int
    PrimaryDimensionTextFormat: Annotations.DimensionTextFormat
    PrimaryDimensionUnit: Annotations.DimensionUnit
    SuppressAngularZerosOption: Annotations.AngularSuppressZeros
    ToleranceLeadingZero: bool
    TolerancePlacement: Annotations.TolerancePlacement


class TrueLengthTextPosition(enum.Enum):
    None = 0
    Prefix = 1
    Suffix = 2


class TrimDimensionLineStyle(enum.Enum):
    DoNotTrim = 0
    Trim = 1


class ToleranceZoneShape(enum.Enum):
    Planar = 0
    Cylindrical = 1
    Spherical = 2
    Last = 3


class ToleranceType(enum.Enum):
    None = 0
    LimitOneLine = 1
    LimitTwoLines = 2
    BilateralOneLine = 3
    BilateralTwoLines = 4
    UnilateralAbove = 5
    UnilateralBelow = 6
    Basic = 7
    Reference = 8
    LimitLargerFirst = 9
    LimitLargerBelow = 10
    LimitsAndFits = 11
    NotToScale = 12
    DiameterReference = 13
    BasicNotToScale = 14


class TolerancePlacement(enum.Enum):
    Below = 0
    After = 1
    Above = 2
    Last = 3


class TitleBlockPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AlignmentPosition: Annotations.AlignmentPosition
    AutomaticUpdate: bool


class TitleBlockCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.TitleBlock]:
        ...
    def __init__(self, owner: Drafting.DraftingApplicationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateEditTitleBlockBuilder(self, titleBlocks: typing.List[Annotations.TitleBlock]) -> Annotations.EditTitleBlockBuilder:
        ...
    def CreateDefineTitleBlockBuilder(self, titleblock: Annotations.TitleBlock) -> Annotations.DefineTitleBlockBuilder:
        ...
    def CreateCellBuilder(self, object: DisplayableObject, isLocked: bool, contentType: int, value: str, label: str, canLockStatusChange: bool) -> Annotations.TitleBlockCellBuilder:
        """[Obsolete("Deprecated in NX12.0.1.  Use overloaded NXOpen.Annotations.TitleBlockCollection.CreateCellBuilder instead.")"""
        ...
    def CreateCellBuilder(self, tableCell: DisplayableObject, lockStatus: bool, label: str) -> Annotations.TitleBlockCellBuilder:
        ...
    def Tag(self) -> Tag: ...



class TitleBlockCellBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.TitleBlockCellBuilder]) -> None:
        ...
    def Append(self, object: Annotations.TitleBlockCellBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.TitleBlockCellBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.TitleBlockCellBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.TitleBlockCellBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.TitleBlockCellBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.TitleBlockCellBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.TitleBlockCellBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.TitleBlockCellBuilder, object2: Annotations.TitleBlockCellBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.TitleBlockCellBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TitleBlockCellBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def EditCell(self, lockStatus: bool, contentType: int, value: str, label: str, canChangeLockStatus: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.1.  Instead use NXOpen.Annotations.TitleBlockCellBuilder.Lock for lock status, NXOpen.Annotations.TitleBlockCellBuilder.Label for label and NXOpen.Annotations.EditTitleBlockBuilder.SetCellValueForLabel for cell value. 'Content type' and 'Can change lock status' are automatically computed and need not be used by a user.")"""
        ...
    def Validate(self) -> bool:
        ...
    Cell: DisplayableObject
    EditableText: str
    Label: str
    Lock: bool
    Text: str


class TitleBlock(Annotations.Annotation):
    def __init__(self) -> None: ...
    def DoUpdate(self) -> None:
        ...
    def GetPreferences(self) -> Annotations.TitleBlockPreferences:
        ...
    def SetPreferences(self, prefs: Annotations.TitleBlockPreferences) -> None:
        ...


class ThicknessDimensionBuilder(Annotations.BaseThicknessDimensionBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class TextWithSymbolsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetText(self) -> str:
        ...
    def SetText(self, text: str) -> None:
        ...
    def AddSymbol(self, newObject: NXObject, name: str, lineNo: int, cursorPos: int) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Instead use NXOpen.Annotations.TextWithSymbolsBuilder.CreateEmbeddedAnnotationText for creating embedded symbol text.")"""
        ...
    def RemoveSymbol(self, path: str) -> None:
        ...
    def GetEmbeddedCustomSymbols(self) -> typing.List[Annotations.BaseCustomSymbol]:
        ...
    def GetSymbolAlignment(self, symbolName: str) -> Annotations.TextWithSymbolsBuilder.SymbolAlignmentType:
        ...
    def SetSymbolAlignment(self, symbolName: str, symbolAlignment: Annotations.TextWithSymbolsBuilder.SymbolAlignmentType) -> None:
        ...
    def AddAttributeReference(self, ownerTag: NXObject, title: str, displayTokens: bool, lineNo: int, cursorPos: int) -> None:
        ...
    def AddExpressionReference(self, expName: str, format: str, lineNo: int, cursorPos: int) -> None:
        ...
    def AddEmbeddedAnnotation(self, embeddedAnnotation: NXObject, lineNo: int, cursorPos: int) -> str:
        """[Obsolete("Deprecated in NX2007.0.0.  Instead use NXOpen.Annotations.TextWithSymbolsBuilder.CreateEmbeddedAnnotationText for creating embedded annotation text.")"""
        ...
    def CopyEmbeddedAnnotation(self, inputText: str, isCopied: bool) -> str:
        ...
    def CreateEmbeddedAnnotationText(self, embeddedAnnotation: NXObject) -> str:
        ...
    def Validate(self) -> bool:
        ...
    CustomSymbolScale: float
    SymbolAspectRatio: float
    SymbolHeight: float
    SymbolLength: float
    SymbolPreferences: Annotations.TextWithSymbolsBuilder.SymbolPreferencesType
    SymbolScale: float
    SymbolSizeMethod: Annotations.TextWithSymbolsBuilder.SymbolSizingMethod


    class SymbolSizingMethod(enum.Enum):
        ScaleAndAspectRatio = 0
        LengthAndHeight = 1
    

    class SymbolPreferencesType(enum.Enum):
        UseCurrent = 0
        UseDefinition = 1
    

    class SymbolAlignmentType(enum.Enum):
        None = 0
        Top = 1
        Middle = 2
        Bottom = 3
        AnchorPoint = 4
    

class TextWithEditControlsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetEditorText(self) -> str:
        ...
    def SetEditorText(self, text: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    TextBlock: Annotations.TextWithSymbolsBuilder


class TextType(enum.Enum):
    Mandatory = 0
    Arbitrary = 1
    Controlled = 2
    PartiallyControlled = 3
    Integer = 4
    Real = 5
    Last = 6


class TextPreferencesOption(enum.Enum):
    PartLettering = 0
    MasterSymbol = 1
    Last = 2


class TextPosition(enum.Enum):
    AfterStub = 0
    AboveStub = 1
    Last = 2


class TextPlacement(enum.Enum):
    Automatic = 0
    ManualArrowsIn = 1
    ManualArrowsOut = 2
    ManualArrowsInSameDirection = 3
    Last = 4


class TextOrientation(enum.Enum):
    Horizontal = 0
    Aligned = 1
    OverDimensionLine = 2
    ByAngle = 3
    Perpendicular = 4
    SplitByDimensionLine = 5
    Last = 6


class TextJustification(enum.Enum):
    Left = 1
    Center = 2
    Right = 3


class TextEditorBuilder(Builder):
    def __init__(self) -> None: ...
    Text: Annotations.TextWithEditControlsBuilder


class TextComponent(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetText(self) -> str:
        ...
    def GetDistanceToTop(self) -> float:
        ...
    def GetIntegerizedLength(self, nth: int) -> int:
        ...
    def GetAngle(self) -> float:
        ...
    AdjustedOrigin: Point3d
    Height: float
    Length: float
    NumberLines: int
    Origin: Point3d
    Type: Annotations.TextComponent.TextType


    class TextType(enum.Enum):
        Text = 0
        DualDimension = 1
        Tolerance = 2
        DualTolerance = 3
        DiameterRadius = 4
        AppendedAbove = 5
        AppendedBelow = 6
        AppendedBefore = 7
        AppendedAfter = 8
        ChamferBefore = 9
        ChamferAfter = 10
        ChamferSize = 11
        ChamferXSymbol = 12
        ChamferAngle = 13
    

class TextCfw():
    Color: int
    Font: int
    Width: Annotations.LineWidth
    def ToString(self) -> str:
        ...
    def __init__(self, Color: int, Font: int, Width: Annotations.LineWidth) -> None: ...


class TargetPointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.TargetPoint]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTargetPointBuilder(self, targetPt: Annotations.TargetPoint) -> Annotations.TargetPointBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.TargetPoint:
        ...
    def Tag(self) -> Tag: ...



class TargetPointBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: float
    Color: NXColor
    Height: float
    Inherit: SelectNXObject
    Location: SelectNXObject
    Width: Annotations.TargetPointBuilder.Thickness


    class Thickness(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 6
        Two = 7
        Three = 8
        Four = 9
        Five = 10
        Six = 11
        Seven = 12
        Eight = 13
        Nine = 14
    

class TargetPoint(Annotations.DraftingAid):
    def __init__(self) -> None: ...


class Tail(enum.Enum):
    None = 0
    Fork = 1
    Box = 2
    Last = 3


class TabularNoteStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AutomaticUpdate: bool
    LockTableContents: bool
    LockTableFormat: bool
    ShowLockedDeletedContent: Annotations.TabularNoteStyleBuilder.ShowLockedDeletedRowMethod


    class ShowLockedDeletedRowMethod(enum.Enum):
        Strikethru = 0
        Blank = 1
        Remove = 2
        Ordinary = 3
    

class TableStyleBuilder(Annotations.StyleBuilder):
    def __init__(self) -> None: ...
    BendTable: Annotations.BendTableSettingsBuilder
    HoleTableContent: Annotations.HoleTableSettingsContentBuilder
    HoleTableFormat: Annotations.HoleTableSettingsFormatBuilder
    HoleTableHoleFilters: Annotations.HoleTableSettingsHoleFiltersBuilder
    HoleTableLabel: Annotations.HoleTableSettingsLabelBuilder
    HoleTableWorkflow: Annotations.HoleTableSettingsWorkflowBuilder
    PartFamilyTable: Annotations.PartFamilyTableSettingsBuilder
    PartsListBuilder: Annotations.PartsListBuilder
    TableCellStyle: Annotations.TableCellStyleBuilder
    TableColumnSettingsBuilder: Annotations.TableColumnSettingsBuilder
    TableCommonSorting: Annotations.TableCommonSortingBuilder
    TableSectionStyle: Annotations.TableSectionStyleBuilder
    TabularNoteStyle: Annotations.TabularNoteStyleBuilder


class TableSectionStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlignmentPosition: Annotations.TableSectionStyleBuilder.AlignmentPositionType
    ApplyToAllSections: bool
    BorderOffset: float
    ContinuationNote: str
    ContinuationProperty: Annotations.TableSectionStyleBuilder.ContinuationPropertyType
    ContinuationSpacing: float
    DisplayContinuationNote: Annotations.TableSectionStyleBuilder.DisplayContinuationNoteType
    DoubleBorder: bool
    HeaderLocation: Annotations.TableSectionStyleBuilder.LocationOfHeader
    MaximumHeight: float
    RowHeight: float


    class LocationOfHeader(enum.Enum):
        Above = 0
        Below = 1
        None = 2
    

    class DisplayContinuationNoteType(enum.Enum):
        None = 0
        Above = 1
        Below = 2
    

    class ContinuationPropertyType(enum.Enum):
        Left = 0
        Right = 1
        Up = 2
        Down = 3
        NextSheet = 4
    

    class AlignmentPositionType(enum.Enum):
        TopLeft = 0
        TopRight = 1
        BottomLeft = 2
        BottomRight = 3
    

class TableSectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.TableSection]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTableSectionBuilder(self, section: Annotations.TableSection) -> Annotations.TableSectionBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.TableSection:
        ...
    def Tag(self) -> Tag: ...



class TableSectionBuilder(Builder):
    def __init__(self) -> None: ...
    ColumnWidth: float
    Leader: Annotations.LeaderBuilder
    NumberOfColumns: int
    NumberOfRows: int
    Origin: Annotations.OriginBuilder
    RowHeight: float
    Style: Annotations.TableStyleBuilder


class TableSection(Annotations.Annotation):
    def __init__(self) -> None: ...


class TableRowSortingBuilder(Drafting.BaseEditSettingsBuilder):
    def __init__(self) -> None: ...
    TableCommonSorting: Annotations.TableCommonSortingBuilder


class TableEditSettingsBuilder(Drafting.BaseEditSettingsBuilder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: DisplayableObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    BendTable: Annotations.BendTableSettingsBuilder
    DisplayStyle: Annotations.DisplayStyleBuilder
    HoleTableContent: Annotations.HoleTableSettingsContentBuilder
    HoleTableFormat: Annotations.HoleTableSettingsFormatBuilder
    HoleTableHoleFilters: Annotations.HoleTableSettingsHoleFiltersBuilder
    HoleTableLabel: Annotations.HoleTableSettingsLabelBuilder
    HoleTableWorkflow: Annotations.HoleTableSettingsWorkflowBuilder
    Ordinate: Annotations.OrdinateStyleBuilder
    PartFamilyTable: Annotations.PartFamilyTableSettingsBuilder
    PartsList: Annotations.PartsListBuilder
    RoutingBillOfMaterial: Annotations.BillOfMaterialBuilder
    TableCell: Annotations.TableCellStyleBuilder
    TableColumn: Annotations.TableColumnBuilder
    TableColumnSettingsBuilder: Annotations.TableColumnSettingsBuilder
    TableCommonSorting: Annotations.TableCommonSortingBuilder
    TableCutSheet: Annotations.CutSheetBuilder
    TableLettering: Annotations.LetteringStyleBuilder
    TableLineArrow: Annotations.LineArrowStyleBuilder
    TablePinList: Annotations.PinListBuilder
    TableSection: Annotations.TableSectionStyleBuilder
    TabularNote: Annotations.TabularNoteStyleBuilder


class TableCommonSortingBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetSortingData(self, sortingData: typing.List[Annotations.TableCommonSortingBuilder.SortData]) -> None:
        ...
    def GetSortingData(self) -> typing.List[Annotations.TableCommonSortingBuilder.SortData]:
        ...
    def GetManualSortRowList(self) -> int:
        ...
    def SetManualSortRowList(self, rowList: int) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Method: Annotations.TableCommonSortingBuilder.MethodType


    class SortingDirection(enum.Enum):
        Descending = 0
        Ascending = 1
    

    class TableCommonSortingBuilderSortData():
        ColumnPosition: int
        SortingDirection: Annotations.TableCommonSortingBuilder.SortingDirection
        def ToString(self) -> str:
            ...
        def __init__(self, ColumnPosition: int, SortingDirection: Annotations.TableCommonSortingBuilder.SortingDirection) -> None: ...
    

    class MethodType(enum.Enum):
        Alphabetic = 0
        Alphanumeric = 1
        Manual = 2
    

class TableColumnSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateTableColumnBuilder(self) -> Annotations.TableColumnBuilder:
        ...
    def CreateTableColumnBuilder(self, columnBuilderToInherit: Annotations.TableColumnBuilder) -> Annotations.TableColumnBuilder:
        ...
    def Validate(self) -> bool:
        ...
    TableColumnList: Annotations.TableColumnBuilderList


class TableColumnBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.TableColumnBuilder]) -> None:
        ...
    def Append(self, object: Annotations.TableColumnBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.TableColumnBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.TableColumnBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.TableColumnBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.TableColumnBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.TableColumnBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.TableColumnBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.TableColumnBuilder, object2: Annotations.TableColumnBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.TableColumnBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TableColumnBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AsRequiredText: str
    AttributeName: str
    Category: Annotations.TableColumnBuilder.CategoryType
    DefaultText: str
    IncludeNestedAssemblies: bool
    KeyField: bool
    NestedAssemblyQuantity: str
    ParentAssemblyQuantity: str
    ProtectCells: bool
    Scope: Annotations.TableColumnBuilder.ScopeType
    SelectParentComponent: SelectDisplayableObject
    ShowCombinedMassForAssemblies: bool
    Title: str


    class ScopeType(enum.Enum):
        CellsinNewRows = 0
        AllCellsinColumn = 1
    

    class CategoryType(enum.Enum):
        General = 0
        Callout = 1
        Quantity = 2
    

class TableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Table]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Annotations.Table:
        ...
    def Tag(self) -> Tag: ...



    class ZeroDisplayType(enum.Enum):
        Zero = 0
        Dash = 1
        Empty = 2
    

class TableCellStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetFitMethods(self) -> typing.List[Annotations.TableCellStyleBuilder.FitMethodType]:
        ...
    def SetFitMethods(self, fitMethods: typing.List[Annotations.TableCellStyleBuilder.FitMethodType]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    BorderColor: int
    BorderFont: int
    BorderLocation: Annotations.TableCellStyleBuilder.BorderLocationType
    BorderWidth: int
    CellFormatType: Annotations.TableCellStyleBuilder.CellFormatTypes
    DateFormatType: Annotations.TableCellStyleBuilder.DateFormatTypes
    Format: Annotations.TableCellStyleBuilder.FormatType
    IncrementIsPercentage: bool
    IncrementValue: float
    IsAFormula: bool
    Precision: int
    Prefix: str
    ProtectCell: bool
    ShowLeadingZeroes: bool
    ShowTrailingZeroes: bool
    SlantAngle: float
    Suffix: str
    TabDirection: Annotations.TableCellStyleBuilder.TabDirectionType
    TextAlignment: Annotations.TableCellStyleBuilder.TextAlignmentType
    TimeFormatType: Annotations.TableCellStyleBuilder.TimeFormatTypes
    Url: str
    ZeroDisplay: Annotations.TableCellStyleBuilder.ZeroDisplayType


    class TimeFormatTypes(enum.Enum):
        Hhmm24 = 0
        Hhmm12 = 1
        Hhmmss24 = 2
        Hhmmss12 = 3
    

    class TextAlignmentType(enum.Enum):
        TopLeft = 1
        TopCenter = 2
        TopRight = 3
        MidLeft = 4
        MidCenter = 5
        MidRight = 6
        BottomLeft = 7
        BottomCenter = 8
        BottomRight = 9
    

    class TabDirectionType(enum.Enum):
        Right = 0
        Left = 1
        Up = 2
        Down = 3
    

    class FormatType(enum.Enum):
        Text = 1
        Float = 2
        Fixed = 3
        General = 4
        Monetary = 5
        Comma = 6
        FractionHalfSize = 7
        FractionThreeQuarterSize = 8
        FractionFullSize = 9
        DegreesDegreeUnits = 10
        DegreesRadianUnits = 11
        Percent = 12
        Degrees = 13
        Hex = 14
        Logic = 15
        DateDmy = 16
        DateDm = 17
        DateMy = 18
        DateMdy = 19
        DateYmd = 20
        DateY4md = 21
        DateDmyDot = 22
        TimeHm = 23
        TimeHms = 24
        Hidden = 25
        Custom = 26
    

    class FitMethodType(enum.Enum):
        OverwriteBorder = 1
        AutoSizeText = 2
        Wrap = 3
        Abbreviate = 4
        RemoveSpaces = 5
        AutoSizeRow = 6
        AutoSizeCol = 7
        Truncate = 8
    

    class DateFormatTypes(enum.Enum):
        Ddmmmyyyy = 0
        Ddmmm = 1
        Mmmyyyy = 2
        Mmddyyyy = 3
        Yymmmdd = 4
        Yyyymmdd = 5
        Ddmmyyyy = 6
    

    class CellFormatTypes(enum.Enum):
        Text = 1
        Float = 2
        Fixed = 3
        General = 4
        Monetary = 5
        Comma = 6
        FractionHalfSize = 7
        FractionThreeQuarterSize = 8
        FractionFullSize = 9
        DegreesDegreeUnits = 10
        DegreesRadianUnits = 11
        Percent = 12
        Degrees = 13
        Hex = 14
        Logic = 15
        Hidden = 16
        Custom = 17
        Date = 18
        Time = 19
        DateTime = 20
    

    class BorderLocationType(enum.Enum):
        All = 0
        Left = 1
        Top = 2
        Right = 3
        Bottom = 4
        Middle = 5
        Center = 6
    

class Table(DisplayableObject):
    def __init__(self) -> None: ...
    def DoUpdate(self) -> None:
        ...
    def EvaluateRulesAndUpdate(self) -> None:
        ...
    def EditCellText(self, tableCell: DisplayableObject, text: str) -> None:
        ...
    def ResizeRowsCols(self, rowsOrColumns: typing.List[DisplayableObject], resizeValue: float) -> None:
        ...
    def LockUnlockRows(self, rows: typing.List[DisplayableObject]) -> None:
        ...
    def InsertRows(self, selectedRows: typing.List[DisplayableObject], insertRowsInTabularNote: Annotations.Table.InsertRowsType) -> None:
        ...
    def InsertColumns(self, selectedColumns: typing.List[DisplayableObject], insertColumnsInTabularNote: Annotations.Table.InsertColumnsType) -> None:
        ...
    def InsertHeaderRow(self) -> None:
        ...
    def IsRowLocked(self, row: DisplayableObject) -> bool:
        ...
    def SaveAsTemplate(self, filePath: str) -> None:
        ...


    class InsertRowsType(enum.Enum):
        Above = 0
        Below = 1
    

    class InsertColumnsType(enum.Enum):
        Left = 0
        Right = 1
    

class SymmetricalCenterlineSettingsBuilder(Annotations.CenterlineSettingsBuilder):
    def __init__(self) -> None: ...
    Extension: float
    IndividualDistance: bool
    Size: float


class SymmetricalCenterlineBuilder(Annotations.CenterlineBuilder):
    def __init__(self) -> None: ...
    End: SelectNXObject
    Face: SelectNXObject
    Inherit: SelectNXObject
    Settings: Annotations.SymmetricalCenterlineSettingsBuilder
    Start: SelectNXObject
    Type: Annotations.SymmetricalCenterlineBuilder.Types


    class Types(enum.Enum):
        FromFace = 0
        StartAndEnd = 1
    

class SymmetricalCenterline(Annotations.Centerline):
    def __init__(self) -> None: ...


class SymbolWorkflowBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SymbolAutoUpdate: bool
    SymbolSmashToSketch: bool


class SymbolStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AttachToIdSymbolVertex: bool
    BalloonType: Annotations.BalloonTypes
    CenterlineSymbolColor: NXColor
    CenterlineSymbolWidth: Annotations.LineWidth
    DatumLabelStartingLetter: str
    DraftingSurfaceFinishStandard: Annotations.SurfaceFinishStandard
    EdgeConditionColor: NXColor
    EdgeConditionSymbolExtendReferenceLine: bool
    EdgeConditionWidth: Annotations.LineWidth
    FcfAdditionalTextUnderline: Annotations.SymbolStyleBuilder.FcfTextUnderlineOption
    GdtSymbolColor: NXColor
    GdtSymbolFont: DisplayableObject.ObjectFont
    GdtSymbolWidth: Annotations.LineWidth
    IdSymbolColor: NXColor
    IdSymbolFont: DisplayableObject.ObjectFont
    IdSymbolSize: float
    IdSymbolWidth: Annotations.LineWidth
    IntersectionSymbolColor: NXColor
    IntersectionSymbolFont: DisplayableObject.ObjectFont
    IntersectionSymbolWidth: Annotations.LineWidth
    SurfaceFinishColor: NXColor
    SurfaceFinishFont: DisplayableObject.ObjectFont
    SurfaceFinishWidth: Annotations.LineWidth
    TargetSymbolColor: NXColor
    TargetSymbolFont: DisplayableObject.ObjectFont
    TargetSymbolWidth: Annotations.LineWidth
    UserDefinedSymbolColor: NXColor
    UserDefinedSymbolFont: DisplayableObject.ObjectFont
    UserDefinedSymbolWidth: Annotations.LineWidth
    WeldLineGap: float
    WeldSpaceFactor: float
    WeldSymbolColor: NXColor
    WeldSymbolFont: DisplayableObject.ObjectFont
    WeldSymbolSizeFactor: float
    WeldSymbolStandard: Annotations.WeldStandard
    WeldSymbolWidth: Annotations.LineWidth


    class FcfTextUnderlineOption(enum.Enum):
        None = 0
        Top = 1
        All = 2
    

class SymbolPreferencesOption(enum.Enum):
    PartSymbol = 0
    MasterSymbol = 1
    Last = 2


class SymbolPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetIdSymbolCfw(self) -> Annotations.LineCfw:
        ...
    def SetIdSymbolCfw(self, idSymbolCfw: Annotations.LineCfw) -> None:
        ...
    def GetUserDefinedSymbolCfw(self) -> Annotations.LineCfw:
        ...
    def SetUserDefinedSymbolCfw(self, userDefinedSymbolCfw: Annotations.LineCfw) -> None:
        ...
    def GetCenterlineSymbolCfw(self) -> Annotations.LineCfw:
        ...
    def SetCenterlineSymbolCfw(self, centerlineSymbolCfw: Annotations.LineCfw) -> None:
        ...
    def GetIntersectionSymbolCfw(self) -> Annotations.LineCfw:
        ...
    def SetIntersectionSymbolCfw(self, intersectionSymbolCfw: Annotations.LineCfw) -> None:
        ...
    def GetTargetSymbolCfw(self) -> Annotations.LineCfw:
        ...
    def SetTargetSymbolCfw(self, targetSymbolCfw: Annotations.LineCfw) -> None:
        ...
    def GetGdtSymbolCfw(self) -> Annotations.LineCfw:
        ...
    def SetGdtSymbolCfw(self, gdtSymbolCfw: Annotations.LineCfw) -> None:
        ...
    def GetWeldSymbolCfw(self) -> Annotations.LineCfw:
        ...
    def SetWeldSymbolCfw(self, weldSymbolCfw: Annotations.LineCfw) -> None:
        ...
    def GetWeldLineGap(self) -> float:
        ...
    def SetWeldLineGap(self, lineGap: float) -> None:
        ...
    def GetSurfaceFinishCfw(self) -> Annotations.LineCfw:
        ...
    def SetSurfaceFinishCfw(self, surfaceFinishCfw: Annotations.LineCfw) -> None:
        ...
    def GetWeldSpaceFactor(self) -> float:
        ...
    def SetWeldSpaceFactor(self, spaceFactor: float) -> None:
        ...
    def GetWeldSymbolSizeFactor(self) -> float:
        ...
    def SetWeldSymbolSizeFactor(self, symbolSizeFactor: float) -> None:
        ...
    DraftingSurfaceFinishStandard: Annotations.SurfaceFinishStandard
    IdSymbolSize: float
    WeldSymbolStandard: Annotations.WeldStandard


class SymbolFileCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.SymbolFile]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Annotations.SymbolFile:
        ...
    def CreateSymbolFileBuilder(self, object: Annotations.SymbolFile) -> Annotations.SymbolFileBuilder:
        ...
    def Tag(self) -> Tag: ...



class SymbolFileBuilder(Builder):
    def __init__(self) -> None: ...


class SymbolFile(NXObject):
    def __init__(self) -> None: ...


class SymbolCatalogParameterBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.SymbolCatalogParameterBuilder]) -> None:
        ...
    def Append(self, object: Annotations.SymbolCatalogParameterBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.SymbolCatalogParameterBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.SymbolCatalogParameterBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.SymbolCatalogParameterBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.SymbolCatalogParameterBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.SymbolCatalogParameterBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.SymbolCatalogParameterBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.SymbolCatalogParameterBuilder, object2: Annotations.SymbolCatalogParameterBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.SymbolCatalogParameterBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SymbolCatalogParameterBuilder(Builder):
    def __init__(self) -> None: ...
    Label: str
    LogicalName: str
    Value: str


class SymbolCatalogBuilder(Builder):
    def __init__(self) -> None: ...
    def GenerateItemNumber(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.SymbolCatalogBuilder.ItemNumber instead.")"""
        ...
    def GenerateRevision(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.SymbolCatalogBuilder.Revision instead.")"""
        ...
    def NewParameter(self) -> Annotations.SymbolCatalogParameterBuilder:
        ...
    def SetPartOperationCreateBuilder(self, partOperationBuilder: PDM.PartOperationCreateBuilder) -> None:
        ...
    def GetPartOperationCreateBuilder(self) -> PDM.PartOperationCreateBuilder:
        ...
    IsPartSymbol: bool
    ItemName: str
    ItemNumber: str
    NodeString: str
    ParameterList: Annotations.SymbolCatalogParameterBuilderList
    PartFileName: str
    Path: str
    Revision: str
    SymbolName: str


class Symbol(enum.Enum):
    None = 0
    ButtWithRaisedEdges = 1
    SingleFlange = 2
    SquareButt = 3
    VButt = 4
    VButtBroadRootFace = 5
    BevelButt = 6
    BevelButtBroadRootFace = 7
    UButt = 8
    JButt = 9
    FlareV = 10
    FlareBevel = 11
    KGroove = 12
    Fillet = 13
    Stake = 14
    PlugSlot = 15
    Edge = 16
    Edge2 = 17
    Spot = 18
    Spot2 = 19
    Seam = 20
    Seam2 = 21
    SteepFlankedV = 22
    SteepFlankedBevel = 23
    Backing = 24
    SurfaceJoint = 25
    SolderedJoint = 26
    InclinedJoint = 27
    FoldJoint = 28
    Stud = 29
    Surfacing = 30
    Intermittent = 31
    BackingPlate = 32
    NotSpecified = 33
    Last = 34


class SurfaceFinishStandard(enum.Enum):
    Ansi = 0
    Iso = 1
    Jis = 2
    Din = 3
    Iso2002 = 4
    Din2002 = 5
    Gb = 6
    Eskd = 7


class SurfaceFinishBuilder(Annotations.BaseSurfaceFinishBuilder):
    def __init__(self) -> None: ...
    def InheritFrom(self, inheritTag: Annotations.SurfaceFinish) -> None:
        ...
    A1: str
    A2: str
    Angle: float
    B: str
    C: str
    D: str
    E: str
    F1: str
    F2: str
    Finish: Annotations.SurfaceFinishBuilder.FinishType
    InvertSymbol: bool
    InvertText: bool
    LowerTolerance: float
    Parantheses: Annotations.BaseSurfaceFinishBuilder.ParanthesesType
    Parentheses: Annotations.BaseSurfaceFinishBuilder.ParenthesesType
    SingleRoughnessValue: bool
    Standard: Annotations.SurfaceFinishBuilder.StandardType
    Title: str
    Tolerance: float
    ToleranceType: Annotations.BaseSurfaceFinishBuilder.ToleranceOption


    class StandardType(enum.Enum):
        Ansi = 0
        Iso = 1
        Jis = 2
        Din = 3
        Iso2002 = 4
        Din2002 = 5
        Gb = 6
        Eskd = 7
    

    class FinishType(enum.Enum):
        Basic = 0
        Modifier = 1
        ModifierAllAround = 2
        MaterialRemovalRequired = 3
        ModifierMaterialRemovalRequired = 4
        ModifierMaterialRemovalRequiredAllAround = 5
        MaterialRemovalProhibited = 6
        ModifierMaterialRemovalProhibited = 7
        ModifierMaterialRemovalProhibitedAllAround = 8
    

class SurfaceFinish(Annotations.BaseSurfaceFinish):
    def __init__(self) -> None: ...


class SuppressPMIBuilder(Builder):
    def __init__(self) -> None: ...
    def SelectExpression(self, expression: Expression) -> None:
        ...
    SelectPMIObjects: SelectNXObjectList
    SuppressionMethod: Annotations.SuppressPMIBuilder.SuppressionMethodType


    class SuppressionMethodType(enum.Enum):
        None = 0
        Manual = 1
        CreateExpressionForEach = 2
        CreateSharedExpression = 3
        SelectExpression = 4
    

class SupplementarySymbol(enum.Enum):
    None = 0
    Convex = 1
    Flush = 2
    Concave = 3
    BlendedToes = 4
    BackingStripPermanent = 5
    BackingStripRemovable = 6
    MeltThrough = 7
    Last = 8


class StyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: DisplayableObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    BreakSettings: Annotations.BreakSettingsBuilder
    DimensionStyle: Annotations.DimensionStyleBuilder
    DisplayStyle: Annotations.DisplayStyleBuilder
    ForeshorteningSymbolSettings: Annotations.ForeshorteningSymbolSettingsBuilder
    FrameBarStyle: Annotations.FrameBarStyleBuilder
    HatchStyle: Annotations.HatchStyleBuilder
    HoleCalloutSettings: Annotations.HoleCalloutSettingsBuilder
    LetteringStyle: Annotations.LetteringStyleBuilder
    LineArrowStyle: Annotations.LineArrowStyleBuilder
    OrdinateStyle: Annotations.OrdinateStyleBuilder
    RadialStyle: Annotations.RadialStyleBuilder
    SheetMetalPMISettingsBuilder: Annotations.SheetMetalPMISettingsBuilder
    SingleSidedDisplay: Annotations.SingleSidedDisplayBuilder
    SymbolStyle: Annotations.SymbolStyleBuilder
    UnitsStyle: Annotations.UnitsStyleBuilder


class StubSymbolType(enum.Enum):
    None = 0
    AllAround = 1
    AllOver = 2


class StackVerticalAlignment(enum.Enum):
    Left = 0
    Center = 1
    Right = 2


class StackHorizontalAlignment(enum.Enum):
    Top = 0
    Middle = 1
    Bottom = 2


class StackAlignmentPosition(enum.Enum):
    Above = 0
    Below = 1
    Left = 2
    Right = 3


class SpecificNoteBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetText(self) -> str:
        ...
    def SetText(self, text: str) -> None:
        ...
    Category: str
    Identifier: str
    Revision: str
    Title: str


class SpecificNote(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class SmashCustomSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    Symbol: SelectDisplayableObjectList


class SizeLetterCode(enum.Enum):
    None = 0
    A = 1
    C = 2
    D = 3
    S = 4
    Z = 5
    P = 6
    Last = 7


class SingleSidedDisplayBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Flip(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    DisableAutoSingleSided: bool
    DisplayAsSingleSided: bool
    SingleSidedArrowLineLength: float


class SimpleDraftingAidPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetLetteringPreferences(self) -> Annotations.LetteringPreferences:
        ...
    def SetLetteringPreferences(self, preferences: Annotations.LetteringPreferences) -> None:
        ...
    def GetLineAndArrowPreferences(self) -> Annotations.LineAndArrowPreferences:
        ...
    def SetLineAndArrowPreferences(self, preferences: Annotations.LineAndArrowPreferences) -> None:
        ...
    def GetSymbolPreferences(self) -> Annotations.SymbolPreferences:
        ...
    def SetSymbolPreferences(self, preferences: Annotations.SymbolPreferences) -> None:
        ...
    def GetUserSymbolPreferences(self) -> Annotations.UserSymbolPreferences:
        ...
    def SetUserSymbolPreferences(self, preferences: Annotations.UserSymbolPreferences) -> None:
        ...


class SimpleDraftingAid(Annotations.DraftingAid):
    def __init__(self) -> None: ...
    def SetText(self, lines: str) -> None:
        ...
    def GetText(self) -> str:
        ...
    def SetUserSymbolPreferences(self, usymPrefs: Annotations.UserSymbolPreferences) -> None:
        ...
    def SetUserSymbolSize(self, sizeType: Annotations.UserSymbolPreferences.SizeType, lengthOrScale: float, heightOrAspectRatio: float) -> None:
        ...
    def GetUserSymbolSize(self, sizeType: Annotations.UserSymbolPreferences.SizeType, lengthOrScale: float, heightOrAspectRatio: float) -> None:
        ...
    def GetUserSymbolPreferences(self) -> Annotations.UserSymbolPreferences:
        ...


class ShipFrameBar(Annotations.BaseFrameBar):
    def __init__(self) -> None: ...


class ShipDraftingFramebarGeneralBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DecimalPlaces: int
    MainLine: bool
    MainLineColor: NXColor
    MainLineFont: DisplayableObject.ObjectFont
    MainLineWidth: Annotations.LineWidth
    TicDirection: Annotations.ShipDraftingFramebarGeneralBuilder.TicDirectionTypes


    class TicDirectionTypes(enum.Enum):
        TowardsView = 0
        AwayfromView = 1
    

class ShipDimensionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Dimension]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateShipDimensionBuilder(self, dimension: Annotations.Dimension) -> Annotations.ShipDimensionBuilder:
        ...
    def Tag(self) -> Tag: ...



class ShipDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    AppendedText: Annotations.AppendedTextBuilder
    Element: int
    ElementName: str
    FirstAssociativity: SelectDisplayableObject
    Group: Annotations.ShipDimensionBuilder.GroupType
    Inherit: SelectDisplayableObject
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder


    class GroupType(enum.Enum):
        MainShipItem = 0
        Decks = 1
        TransversalFrames = 2
        Bulkheads = 3
        LongitudinalFrames = 4
    

class SheetMetalPMISettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetPrefixForBendParameterType(self, parameterType: Annotations.SheetMetalPMISettingsBuilder.BendParameterType, prefix: str) -> None:
        ...
    def GetPrefixForBendParameterType(self, parameterType: Annotations.SheetMetalPMISettingsBuilder.BendParameterType) -> str:
        ...
    def SetPrefixForBodyParameterType(self, parameterType: Annotations.SheetMetalPMISettingsBuilder.BodyParameterType, prefix: str) -> None:
        ...
    def GetPrefixForBodyParameterType(self, parameterType: Annotations.SheetMetalPMISettingsBuilder.BodyParameterType) -> str:
        ...
    def Validate(self) -> bool:
        ...
    DecimalPlaces: int
    IncludeBendAngle: bool
    IncludeBendRadius: bool
    IncludeMaterial: bool
    IncludeNeutralFactor: bool
    IncludePhysicalMaterial: bool
    IncludeThickness: bool


    class SmPmiType(enum.Enum):
        Bend = 0
        Body = 1
    

    class BodyParameterType(enum.Enum):
        Materialthickness = 0
        PhysicalMaterial = 1
        Material = 2
    

    class BendParameterType(enum.Enum):
        BendRadius = 0
        BendAngle = 1
        NeutralFactor = 2
    

class SheetMetalPMIBuilder(Annotations.PmiNoteBuilder):
    def __init__(self) -> None: ...
    PMIType: Annotations.SheetMetalPMIBuilder.Types
    SelectedBody: SelectBody
    SelectedFace: SelectFaceList


    class Types(enum.Enum):
        Bend = 0
        Body = 1
    

class SelectTableSectionList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Annotations.TableSection) -> bool:
        ...
    def Add(self, objects: typing.List[Annotations.TableSection]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Annotations.TableSection, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Annotations.TableSection) -> bool:
        ...
    def Remove(self, object: Annotations.TableSection, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Annotations.TableSection, view1: View, point1: Point3d, selection2: Annotations.TableSection, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Annotations.TableSection]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Annotations.TableSection) -> bool:
        ...
    def SetArray(self, objects: typing.List[Annotations.TableSection]) -> None:
        ...
    def GetArray(self) -> typing.List[Annotations.TableSection]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Annotations.TableSection, view1: View, point1: Point3d, selection2: Annotations.TableSection, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Annotations.TableSection, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectPmiCadNeutralAnnotationList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Annotations.PmiCadNeutralAnnotation) -> bool:
        ...
    def Add(self, objects: typing.List[Annotations.PmiCadNeutralAnnotation]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Annotations.PmiCadNeutralAnnotation, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Annotations.PmiCadNeutralAnnotation) -> bool:
        ...
    def Remove(self, object: Annotations.PmiCadNeutralAnnotation, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Annotations.PmiCadNeutralAnnotation, view1: View, point1: Point3d, selection2: Annotations.PmiCadNeutralAnnotation, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Annotations.PmiCadNeutralAnnotation]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Annotations.PmiCadNeutralAnnotation) -> bool:
        ...
    def SetArray(self, objects: typing.List[Annotations.PmiCadNeutralAnnotation]) -> None:
        ...
    def GetArray(self) -> typing.List[Annotations.PmiCadNeutralAnnotation]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Annotations.PmiCadNeutralAnnotation, view1: View, point1: Point3d, selection2: Annotations.PmiCadNeutralAnnotation, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Annotations.PmiCadNeutralAnnotation, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectOrdinateDimensionList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Annotations.OrdinateDimension) -> bool:
        ...
    def Add(self, objects: typing.List[Annotations.OrdinateDimension]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Annotations.OrdinateDimension, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Annotations.OrdinateDimension) -> bool:
        ...
    def Remove(self, object: Annotations.OrdinateDimension, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Annotations.OrdinateDimension, view1: View, point1: Point3d, selection2: Annotations.OrdinateDimension, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Annotations.OrdinateDimension]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Annotations.OrdinateDimension) -> bool:
        ...
    def SetArray(self, objects: typing.List[Annotations.OrdinateDimension]) -> None:
        ...
    def GetArray(self) -> typing.List[Annotations.OrdinateDimension]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Annotations.OrdinateDimension, view1: View, point1: Point3d, selection2: Annotations.OrdinateDimension, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Annotations.OrdinateDimension, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectDimension(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Annotations.Dimension, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Annotations.Dimension, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Annotations.Dimension, view1: View, point1: Point3d, selection2: Annotations.Dimension, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Annotations.Dimension, view1: View, point1: Point3d, selection2: Annotations.Dimension, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Annotations.Dimension, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Annotations.Dimension:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Annotations.Dimension


class SelectBaseEdgeConditionSymbol(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Annotations.BaseEdgeConditionSymbol, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Annotations.BaseEdgeConditionSymbol, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Annotations.BaseEdgeConditionSymbol, view1: View, point1: Point3d, selection2: Annotations.BaseEdgeConditionSymbol, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Annotations.BaseEdgeConditionSymbol, view1: View, point1: Point3d, selection2: Annotations.BaseEdgeConditionSymbol, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Annotations.BaseEdgeConditionSymbol, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Annotations.BaseEdgeConditionSymbol:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Annotations.BaseEdgeConditionSymbol


class SelectBaseCustomSymbolList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Annotations.BaseCustomSymbol) -> bool:
        ...
    def Add(self, objects: typing.List[Annotations.BaseCustomSymbol]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Annotations.BaseCustomSymbol, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Annotations.BaseCustomSymbol) -> bool:
        ...
    def Remove(self, object: Annotations.BaseCustomSymbol, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Annotations.BaseCustomSymbol, view1: View, point1: Point3d, selection2: Annotations.BaseCustomSymbol, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Annotations.BaseCustomSymbol]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Annotations.BaseCustomSymbol) -> bool:
        ...
    def SetArray(self, objects: typing.List[Annotations.BaseCustomSymbol]) -> None:
        ...
    def GetArray(self) -> typing.List[Annotations.BaseCustomSymbol]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Annotations.BaseCustomSymbol, view1: View, point1: Point3d, selection2: Annotations.BaseCustomSymbol, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Annotations.BaseCustomSymbol, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectAnnotationList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Annotations.Annotation) -> bool:
        ...
    def Add(self, objects: typing.List[Annotations.Annotation]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Annotations.Annotation, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Annotations.Annotation) -> bool:
        ...
    def Remove(self, object: Annotations.Annotation, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Annotations.Annotation, view1: View, point1: Point3d, selection2: Annotations.Annotation, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Annotations.Annotation]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Annotations.Annotation) -> bool:
        ...
    def SetArray(self, objects: typing.List[Annotations.Annotation]) -> None:
        ...
    def GetArray(self) -> typing.List[Annotations.Annotation]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Annotations.Annotation, view1: View, point1: Point3d, selection2: Annotations.Annotation, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Annotations.Annotation, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectAnnotation(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Annotations.Annotation, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Annotations.Annotation, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Annotations.Annotation, view1: View, point1: Point3d, selection2: Annotations.Annotation, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Annotations.Annotation, view1: View, point1: Point3d, selection2: Annotations.Annotation, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Annotations.Annotation, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Annotations.Annotation:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Annotations.Annotation


class SearchModelViewCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.SearchModelView]:
        ...
    def __init__(self, owner: Annotations.PmiManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSearchModelViewBuilder(self, searchModelView: ModelingView) -> Annotations.SearchModelViewBuilder:
        ...
    def CreateSearchCriteriaDimensionBuilder(self, searchCriteria: NXObject) -> Annotations.SearchCriteriaDimensionBuilder:
        ...
    def CreateSearchCriteriaFeatureControlFrameBuilder(self, searchCriteria: NXObject) -> Annotations.SearchCriteriaFeatureControlFrameBuilder:
        ...
    def CreateSearchCriteriaDatumFeatureSymbolBuilder(self, searchCriteria: NXObject) -> Annotations.SearchCriteriaDatumFeatureSymbolBuilder:
        ...
    def CreateSearchCriteriaDatumTargetBuilder(self, searchCriteria: NXObject) -> Annotations.SearchCriteriaDatumTargetBuilder:
        ...
    def CreateSearchCriteriaSurfaceFinishBuilder(self, searchCriteria: NXObject) -> Annotations.SearchCriteriaSurfaceFinishBuilder:
        ...
    def CreateSearchCriteriaPminotesBuilder(self, searchCriteria: NXObject) -> Annotations.SearchCriteriaPMINotesBuilder:
        ...
    def Tag(self) -> Tag: ...



class SearchModelViewBuilder(Builder):
    def __init__(self) -> None: ...
    def ExecuteSearch(self) -> None:
        ...
    def SaveAsModelView(self) -> None:
        ...
    def GetResults(self) -> typing.List[NXObject]:
        ...
    def CreateCriteriaObject(self, searchType: Annotations.SearchModelViewBuilder.PmiTypes) -> NXObject:
        ...
    def DeleteCriteriaObject(self, criteriaObject: NXObject) -> None:
        ...
    CriteriaList: TaggedObjectList
    ModelViewName: str
    PmiType: Annotations.SearchModelViewBuilder.PmiTypes
    SearchScope: Annotations.SearchModelViewBuilder.SearchScopeOptions


    class ValueComparisionOptions(enum.Enum):
        Less = 0
        LessEqual = 1
        Equal = 2
        MoreEqual = 3
        More = 4
    

    class TextComparisionOptions(enum.Enum):
        Equals = 0
        Contains = 1
    

    class SearchScopeOptions(enum.Enum):
        WorkPart = 0
        WorkPartAndComponents = 1
    

    class PmiTypes(enum.Enum):
        Dimension = 0
        FeatureControlFrame = 1
        DatumFeatureSymbol = 2
        DatumTarget = 3
        SurfaceFinish = 4
        Note = 5
    

class SearchModelView(ModelingView):
    def __init__(self) -> None: ...


class SearchCriteriaSurfaceFinishBuilder(Builder):
    def __init__(self) -> None: ...
    ByCutoff: bool
    ByLaySymbol: bool
    ByLowerText: bool
    ByLowerTolerance: bool
    ByMachining: bool
    ByMachiningToleranceType: bool
    ByProductionProcess: bool
    ByRoughness: bool
    BySecondaryRoughness: bool
    BySurfaceFinishType: bool
    ByTertiaryRoughness: bool
    ByTolerance: bool
    ByUpperText: bool
    ByUpperTolerance: bool
    ByWavinessText: bool
    CutoffText: str
    CutoffType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    LaySymbolText: str
    LaySymbolType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    LowerTextText: str
    LowerTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    LowerToleranceType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    LowerToleranceValue: float
    MachiningText: str
    MachiningToleranceType: Annotations.SearchCriteriaSurfaceFinishBuilder.ToleranceTypeOptions
    MachiningType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    ProductionProcessText: str
    ProductionProcessType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    RoughnessText: str
    RoughnessType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    SecondaryRoughnessText: str
    SecondaryRoughnessType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    SurfaceFinishType: Annotations.SearchCriteriaSurfaceFinishBuilder.SurfaceFinishTypes
    TertiaryRoughnessText: str
    TertiaryRoughnessType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    ToleranceType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    ToleranceValue: float
    UpperTextText: str
    UpperTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    UpperToleranceType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    UpperToleranceValue: float
    WavinessText: str
    WavinessTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions


    class ToleranceTypeOptions(enum.Enum):
        NoTolerance = 0
        EqualBilateral = 1
        Bilateral = 2
        UnilateralPlus = 3
        UnilateralMinus = 4
        PlusLimit2Lines = 5
        MinusLimit2Lines = 6
        PlusLimit1Line = 7
        NegposlimitMinusLimit1Line = 8
    

    class SurfaceFinishTypes(enum.Enum):
        Open = 0
        OpenAndModifier = 1
        OpenAndModifierAndAllAround = 2
        Required = 3
        RequiredAndModifier = 4
        RequiredAndModifierAndAllAround = 5
        Prohibited = 6
        ProhibitedAndModifier = 7
        ProhibitedAndModifierAndAllAround = 8
    

class SearchCriteriaPMINotesBuilder(Builder):
    def __init__(self) -> None: ...
    ByText: bool
    Text: str
    TextType: Annotations.SearchModelViewBuilder.TextComparisionOptions


    class ZoneShapeOptions(enum.Enum):
        None = 0
        Diameter = 1
        SphericalDiameter = 2
        Square = 3
    

class SearchCriteriaFeatureControlFrameBuilder(Builder):
    def __init__(self) -> None: ...
    ByCharacteristic: bool
    ByCircleU: bool
    ByCircleUValue: bool
    ByCollectionPlane: bool
    ByDirectionFeature: bool
    ByFreeState: bool
    ByIndicator: bool
    ByIntersectionPlane: bool
    ByMaximum: bool
    ByOrientationPlane: bool
    ByPrimaryDatum: bool
    ByPrimaryDatumDual: bool
    ByPrimaryDatumDualMCM: bool
    ByPrimaryDatumMCM: bool
    ByProjected: bool
    ByProjectedValue: bool
    BySecondaryDatum: bool
    BySecondaryDatumDual: bool
    BySecondaryDatumDualMCM: bool
    BySecondaryDatumMCM: bool
    ByStatistical: bool
    ByTangentPlane: bool
    ByTertiaryDatum: bool
    ByTertiaryDatumDual: bool
    ByTertiaryDatumDualMCM: bool
    ByTertiaryDatumMCM: bool
    ByTolerance: bool
    ByToleranceMCM: bool
    ByZoneShape: bool
    CharacteristicType: Annotations.SearchCriteriaFeatureControlFrameBuilder.CharacteristicOptions
    CircleUType: Annotations.SearchCriteriaFeatureControlFrameBuilder.CircleUOptions
    CircleUValue: float
    CircleUValueType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    CollectionPlaneType: Annotations.SearchCriteriaFeatureControlFrameBuilder.CollectionPlaneOptions
    DatumExtendedText: str
    DatumExtendedTextToggle: bool
    DatumExtendedTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    DatumMCMToggle: bool
    DatumMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.PrimaryDatumMCMOptions
    DatumText: str
    DatumToggle: bool
    DirectionFeatureType: Annotations.SearchCriteriaFeatureControlFrameBuilder.DirectionFeatureOptions
    FrameStyleType: Annotations.SearchCriteriaFeatureControlFrameBuilder.FrameStyleOptions
    FreeStateType: Annotations.SearchCriteriaFeatureControlFrameBuilder.FreeStateOptions
    IndicatorType: Annotations.SearchCriteriaFeatureControlFrameBuilder.IndicatorOptions
    IntersectionPlaneType: Annotations.SearchCriteriaFeatureControlFrameBuilder.IntersectionPlaneOptions
    MaximumText: str
    MaximumTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    OrientationPlaneType: Annotations.SearchCriteriaFeatureControlFrameBuilder.OrientationPlaneOptions
    PrimaryDatumDualMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.PrimaryDatumDualMCMOptions
    PrimaryDatumDualText: str
    PrimaryDatumMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.PrimaryDatumMCMOptions
    PrimaryDatumText: str
    ProjectedType: Annotations.SearchCriteriaFeatureControlFrameBuilder.ProjectedOptions
    ProjectedValue: float
    ProjectedValueType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    SecondaryDatumDualMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.SecondaryDatumDualMCMOptions
    SecondaryDatumDualText: str
    SecondaryDatumMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.SecondaryDatumMCMOptions
    SecondaryDatumText: str
    StatisticalType: Annotations.SearchCriteriaFeatureControlFrameBuilder.StatisticalOptions
    TangentPlaneType: Annotations.SearchCriteriaFeatureControlFrameBuilder.TangentPlaneOptions
    TertiaryDatumDualMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.TertiaryDatumDualMCMOptions
    TertiaryDatumDualText: str
    TertiaryDatumMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.TertiaryDatumMCMOptions
    TertiaryDatumText: str
    ToleranceMCMType: Annotations.SearchCriteriaFeatureControlFrameBuilder.ToleranceMCMOptions
    ToleranceText: str
    ToleranceTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    ZoneShapeType: Annotations.SearchCriteriaFeatureControlFrameBuilder.ZoneShapeOptions


    class ToleranceMCMOptions(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessofFeatureSize = 3
    

    class TertiaryDatumMCMOptions(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessofFeatureSize = 3
    

    class TertiaryDatumDualMCMOptions(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessofFeatureSize = 3
    

    class TangentPlaneOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class StatisticalOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class SecondaryDatumMCMOptions(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessofFeatureSize = 3
    

    class SecondaryDatumDualMCMOptions(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessofFeatureSize = 3
    

    class ProjectedOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class PrimaryDatumMCMOptions(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessofFeatureSize = 3
    

    class PrimaryDatumDualMCMOptions(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessofFeatureSize = 3
    

    class OrientationPlaneOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class IntersectionPlaneOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class IndicatorOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class FreeStateOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class FrameStyleOptions(enum.Enum):
        SingleFrame = 0
        CompositeFrame = 1
    

    class DirectionFeatureOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class CollectionPlaneOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class CircleUOptions(enum.Enum):
        Yes = 0
        No = 1
    

    class CharacteristicOptions(enum.Enum):
        Straightness = 0
        Flatness = 1
        Circularity = 2
        Cylindricity = 3
        ProfileOfALine = 4
        ProfileOfASurface = 5
        Angularity = 6
        Perpendicularity = 7
        Parallelism = 8
        Position = 9
        Concentricity = 10
        Symmetry = 11
        CircularRunout = 12
        TotalRunout = 13
        AxisIntersection = 14
    

class SearchCriteriaDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    AboveText: str
    AboveTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    AfterText: str
    AfterTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    BeforeText: str
    BeforeTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    BelowText: str
    BelowTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    ByAboveText: bool
    ByAfterText: bool
    ByBeforeText: bool
    ByBelowText: bool
    ByDeviation: bool
    ByDiameterSymbol: bool
    ByDimensionType: bool
    ByDimensionValue: bool
    ByGrade: bool
    ByLowerTolerance: bool
    ByRadialSymbol: bool
    ByToleranceType: bool
    ByUpperTolerance: bool
    Callout: Annotations.SearchCriteriaCalloutBuilder
    Deviation: str
    DiameterSymbol: Annotations.SearchCriteriaDimensionBuilder.DiameterSymbolOptions
    DimensionType: Annotations.SearchCriteriaDimensionBuilder.DimensionTypes
    DimensionValue: float
    DimensionValueType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    Grade: str
    LowerToleranceType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    LowerToleranceValue: float
    MeasurementType: Annotations.SearchCriteriaDimensionBuilder.MeasurementTypes
    RadialSymbol: Annotations.SearchCriteriaDimensionBuilder.RadialSymbolOptions
    ToleranceType: Annotations.SearchCriteriaDimensionBuilder.ToleranceTypes
    UpperToleranceType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    UpperToleranceValue: float


    class ToleranceTypes(enum.Enum):
        NoTolerance = 0
        EqualBilateralTolerance = 1
        BilateralTolerance = 2
        UnilateralPlus = 3
        UnilateralMinus = 4
        PlusLimitTwoLines = 5
        MinusLimitTwoLines = 6
        PlusLimitOneLine = 7
        MinusLimitOneLine = 8
        LimitsAndFits = 9
        Basic = 10
        Reference = 11
        DiameterReference = 12
        NotToScale = 13
        BasicDimensionNotToScale = 14
    

    class RadialSymbolOptions(enum.Enum):
        R = 0
        Rad = 1
        Sr = 2
        Cr = 3
        UserDefined = 4
    

    class MeasurementTypes(enum.Enum):
        All = 0
        Directed = 1
        FeatureOfSize = 2
    

    class DimensionTypes(enum.Enum):
        Linear = 0
        Angular = 1
        Diameter = 2
        Radial = 3
        Chamfer = 4
        Thickness = 5
        ArcLength = 6
        Chain = 7
        Ordinate = 8
        Baseline = 9
    

    class DiameterSymbolOptions(enum.Enum):
        Diameter = 0
        Dia = 1
        SphericalDiameter = 2
        UserDefined = 3
    

class SearchCriteriaDatumTargetBuilder(Builder):
    def __init__(self) -> None: ...
    ByDatumMovable: bool
    ByDatumTargetLabel: bool
    ByDatumTargetType: bool
    ByHeight: bool
    ByInnerDiameter: bool
    ByOuterDiameter: bool
    ByText: bool
    ByWidth: bool
    DatumMovable: Annotations.SearchCriteriaDatumTargetBuilder.DatumTargetMovableOptions
    DatumTargetLabelText: str
    DatumTargetType: Annotations.SearchCriteriaDatumTargetBuilder.DatumTargetTypes
    HeightType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    HeightValue: float
    InnerDiameterType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    InnerDiameterValue: float
    OuterDiameterType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    OuterDiameterValue: float
    Text: str
    TextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    WidthType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    WidthValue: float


    class DatumTargetTypes(enum.Enum):
        Point = 0
        Line = 1
        Rectangular = 2
        Circular = 3
        Annular = 4
        Spherical = 5
        Cylindrical = 6
        Arbitrary = 7
    

    class DatumTargetMovableOptions(enum.Enum):
        No = 0
        Yes = 1
    

class SearchCriteriaDatumFeatureSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    ByDatumFeatureSymbolLabel: bool
    DatumFeatureSymbolLabel: str


class SearchCriteriaCalloutBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AngleType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    AngleValue: float
    ByAngle: bool
    ByCalloutType: bool
    ByCounterboreDepth: bool
    ByCounterboreDiameter: bool
    ByCountersinkAngle: bool
    ByCountersinkDiameter: bool
    ByDepth: bool
    ByDiameter: bool
    ByPitch: bool
    ByScrewSize: bool
    ByTaperAngle: bool
    ByThreadDepth: bool
    ByThreadSize: bool
    CalloutType: Annotations.SearchCriteriaCalloutBuilder.CalloutTypes
    CounterboreDepthType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    CounterboreDepthValue: float
    CounterboreDiameterType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    CounterboreDiameterValue: float
    CountersinkAngleType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    CountersinkAngleValue: float
    CountersinkDiameterType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    CountersinkDiameterValue: float
    DepthType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    DepthValue: float
    DiameterType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    DiameterValue: float
    PitchType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    PitchValue: float
    ScrewSizeText: str
    ScrewSizeTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions
    TaperAngleType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    TaperAngleValue: float
    ThreadDepthType: Annotations.SearchModelViewBuilder.ValueComparisionOptions
    ThreadDepthValue: float
    ThreadSizeText: str
    ThreadSizeTextType: Annotations.SearchModelViewBuilder.TextComparisionOptions


    class CalloutTypes(enum.Enum):
        Hole = 0
        Diameter = 1
        Cylindrical = 2
    

class SafetyClassBusinessModifierBuilder(Builder):
    def __init__(self) -> None: ...
    SafetyClass: str
    Title: str


class SafetyClassBusinessModifier(Annotations.ListBusinessModifier):
    def __init__(self) -> None: ...


class RevisionBusinessModifierBuilder(Builder):
    def __init__(self) -> None: ...
    Revision: str
    Title: str


class RevisionBusinessModifier(Annotations.BusinessModifier):
    def __init__(self) -> None: ...


class RetainedAnnotationsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    LineColorFontWidth: LineColorFontWidthBuilder
    ShowRetainedAnnotations: bool


class ReplaceSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    IsPartSymbol: bool
    ReplaceAll: bool
    Symbol: Annotations.SelectBaseCustomSymbolList
    SymbolName: str
    SymbolPath: str


class RegionBuilder(Builder):
    def __init__(self) -> None: ...
    Anchor: Annotations.RegionBuilder.AlignmentPosition
    ArbitraryAreaList: Annotations.ArbitraryAreaSeedBuilderList
    BoundaryColorFontWidth: LineColorFontWidthBuilder
    ConformToSurface: bool
    CrosshatchColor: NXColor
    CrosshatchSettings: Annotations.HatchFillSettingsBuilder
    DisplayCrosshatch: bool
    EndPoint: Point
    Height: Expression
    InnerDiameter: Expression
    Origin: Point
    OuterDiameter: Expression
    Plane: Annotations.PlaneBuilder
    SelectCylindricalFace: SelectDisplayableObjectList
    SelectFace: SelectDisplayableObjectList
    StartPoint: Point
    Type: Annotations.RegionBuilder.Types
    Width: Expression


    class Types(enum.Enum):
        RectangularRegion = 0
        CircularRegion = 1
        AnnularRegion = 2
        CylindricalRegion = 3
        ArbitraryRegion = 4
    

    class CrosshatchPatterns(enum.Enum):
        None = 0
        GeneralUse = 1
    

    class AlignmentPosition(enum.Enum):
        TopLeft = 0
        TopCenter = 1
        TopRight = 2
        MiddleLeft = 3
        MiddleCenter = 4
        MiddleRight = 5
        BottomLeft = 6
        BottomCenter = 7
        BottomRight = 8
    

class Region(Annotations.Annotation):
    def __init__(self) -> None: ...
    def GetBoundaryCurves(self, curves: typing.List[Curve]) -> None:
        ...
    def GetHatchCurves(self, curves: typing.List[Curve]) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class ReferenceIncludeType(enum.Enum):
    ValuePrefixTolerance = 0
    OnlyValue = 1


class RectangularTargetData(Annotations.DatumTargetData):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetLength(self) -> Annotations.Value:
        ...
    def SetLength(self, length: Annotations.Value) -> None:
        ...
    def GetWidth(self) -> Annotations.Value:
        ...
    def SetWidth(self, width: Annotations.Value) -> None:
        ...


class RectangularTarget(Annotations.AreaTarget):
    def __init__(self) -> None: ...
    def GetLength(self) -> Annotations.Value:
        ...
    def SetLength(self, length: Annotations.Value) -> None:
        ...
    def GetWidth(self) -> Annotations.Value:
        ...
    def SetWidth(self, width: Annotations.Value) -> None:
        ...


class RasterImageBuilder(Display.ImageBaseBuilder):
    def __init__(self) -> None: ...
    InsertPointView: View


class RasterImage(Display.ImageBase):
    def __init__(self) -> None: ...


class RapidDimensionBuilder(Annotations.BaseRapidDimensionBuilder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class RadiusSymbol(enum.Enum):
    R = 0
    RAD = 1
    UserDefined = 2
    SR = 3
    CR = 4
    Last = 5


class RadiusDimensionType(enum.Enum):
    ToCenter = 0
    NotToCenter = 1
    Last = 2


class RadiusDimension(Annotations.BaseRadiusDimension):
    def __init__(self) -> None: ...


class RadialStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DiameterRadiusPlacement: Annotations.DiameterRadiusSymbolPlacement
    DiameterSymbol: str
    DiameterSymbolType: Annotations.DiameterSymbol
    FoldedRadiusAngle: float
    RadiusSymbol: str
    RadiusSymbolType: Annotations.RadiusSymbol
    SymbolToDimensionTextDistance: float
    TextAboveLeader: Annotations.DiameterRadiusLeaderStub


class RadialDimensionBuilder(Annotations.BaseRadialDimensionBuilder):
    def __init__(self) -> None: ...
    def SetNthSecondaryOrigin(self, nth: int, secondaryOrigin: Point3d) -> None:
        ...
    def GetNthSecondaryOrigin(self, nth: int) -> Point3d:
        ...
    def SetNthSecondaryArrowheadOrientation(self, nth: int, secondaryArrowheadOrientation: Annotations.TextPlacement) -> None:
        ...
    def GetNthSecondaryArrowheadOrientation(self, nth: int) -> Annotations.TextPlacement:
        ...
    def GetSecondaryCallouts(self) -> typing.List[Annotations.Dimension]:
        ...
    Driving: Annotations.DrivingValueBuilder
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder
    IsAutoplaced: bool


class QueryPmiBuilder(Builder):
    def __init__(self) -> None: ...
    AreAllOccurrencesIncluded: bool
    AreAttachedPmiIncluded: bool
    AreReferencingMemberObjectsIncluded: bool
    CreateQueryResultsView: bool
    Geometry: SelectObjectList


class ProductGridStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    GridOverhang: float
    GridSpacing: float
    LabelDivisor: float
    LabelGap: float
    LineColor: NXColor
    LineFont: DisplayableObject.ObjectFont
    LineWidth: Annotations.LineWidth
    LocationRelativeGridHorizontal: Annotations.ProductGridStyleBuilder.HorizontalLabelDisplay
    LocationRelativeGridValue: Annotations.ProductGridStyleBuilder.GridLabelLocation
    LocationRelativeGridVertical: Annotations.ProductGridStyleBuilder.VerticalLabelDisplay
    ReferenceXAxisLabel: str
    ReferenceYAxisLabel: str
    ReferenceZAxisLabel: str
    ShowHorizontalGridLines: bool
    ShowVerticalGridLines: bool


    class VerticalLabelDisplay(enum.Enum):
        Below = 0
        Above = 1
        AboveBelow = 2
        None = 3
    

    class HorizontalLabelDisplay(enum.Enum):
        Before = 0
        After = 1
        BeforeAfter = 2
        None = 3
    

    class GridLabelLocation(enum.Enum):
        Before = 0
        After = 1
        Above = 2
        Below = 3
    

class ProductGridCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.BaseProductGrid]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateProductGridBuilder(self, productGrid: Annotations.ProductGrid) -> Annotations.ProductGridBuilder:
        ...
    def CreatePmiProductGridBuilder(self, productGrid: Annotations.PmiProductGrid) -> Annotations.PmiProductGridBuilder:
        ...
    def Tag(self) -> Tag: ...



class ProductGridBuilder(Annotations.BaseProductGridBuilder):
    def __init__(self) -> None: ...


class ProductGrid(Annotations.BaseProductGrid):
    def __init__(self) -> None: ...


class ProcessSpecificationBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetNomenclature(self) -> str:
        ...
    def SetNomenclature(self, nomenclature: str) -> None:
        ...
    def GetOpenField(self) -> str:
        ...
    def SetOpenField(self, openField: str) -> None:
        ...
    Identifier: str
    Revision: str
    Title: str


class ProcessSpecification(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class PointTarget(Annotations.DatumTarget):
    def __init__(self) -> None: ...
    PointCoordinates: Point3d


class PmiWaveLinkBuilder(Builder):
    def __init__(self) -> None: ...
    GeometryTypeToWAVELink: int
    SelectedPMI: Annotations.SelectAnnotationList
    SourcePart: TaggedObject
    TargetPart: TaggedObject


class PmiWaveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Pmi]:
        ...
    def __init__(self, owner: Annotations.PmiManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePmiWaveLinkBuilder(self, annotation: Annotations.Annotation) -> Annotations.PmiWaveLinkBuilder:
        ...
    def Tag(self) -> Tag: ...



class PmiWave(Annotations.Annotation):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiVerticalOrdinateDimension(Annotations.VerticalOrdinateDimension):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiVerticalDimension(Annotations.BaseVerticalDimension):
    def __init__(self) -> None: ...


class PmiUserDefinedBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    Title: str


class PmiUserDefined(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class PmiUrlNoteBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    Title: str
    UrlValue: str


class PmiUrlNote(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class PmiTrackingPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    def LoadDefaultSettings(self) -> None:
        ...
    def UpdateTrackingProperties(self) -> None:
        ...
    def SetPmiTrackingPropertyStatus(self, propertyName: str, propertyStatus: bool) -> None:
        ...
    def GetPmiTrackingPropertyStatus(self, propertyName: str) -> bool:
        ...


class PmiThicknessDimensionBuilder(Annotations.BaseThicknessDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiTableSectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.PmiTableSection]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePmiTableBuilder(self, section: Annotations.PmiTableSection) -> Annotations.PmiTableBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.PmiTableSection:
        ...
    def Tag(self) -> Tag: ...



class PmiTableSection(Annotations.TableSection):
    def __init__(self) -> None: ...


class PmiTableBuilder(Annotations.TableSectionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiSurfaceFinishData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    A1String: str
    A2String: str
    BString: str
    CString: str
    DString: str
    EString: str
    F1String: str
    F2String: str
    LowerDelta: float
    SingleRoughnessValue: bool
    Standard: Annotations.SurfaceFinishBuilder.StandardType
    SymbolType: Annotations.SurfaceFinishBuilder.FinishType
    Title: str
    UpperDelta: float


class PmiSupplementalGeometryRegionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    RegionBoundaryCurveCFW: LineColorFontWidthBuilder
    RegionHeight: float
    RegionInnerDiameter: float
    RegionOuterDiameter: float
    RegionWidth: float


class PmiSupplementalGeometryProductGridBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    GridCFW: LineColorFontWidthBuilder
    GridOverhang: float
    GridSpacing: float
    LabelDivisor: float
    LabelGap: float
    LocationRelativeGridHorizontal: Annotations.PmiSupplementalGeometryProductGridBuilder.HorizontalLabelDisplay
    LocationRelativeGridValue: Annotations.PmiSupplementalGeometryProductGridBuilder.GridLabelLocation
    LocationRelativeGridVertical: Annotations.PmiSupplementalGeometryProductGridBuilder.VerticalLabelDisplay
    ReferenceXAxisLabel: str
    ReferenceYAxisLabel: str
    ReferenceZAxisLabel: str
    ShowHorizontalGridLines: bool
    ShowVerticalGridLines: bool


    class VerticalLabelDisplay(enum.Enum):
        Below = 0
        Above = 1
        AboveBelow = 2
        None = 3
    

    class HorizontalLabelDisplay(enum.Enum):
        Before = 0
        After = 1
        BeforeAfter = 2
        None = 3
    

    class GridLabelLocation(enum.Enum):
        Before = 0
        After = 1
        Above = 2
        Below = 3
    

class PmiStringBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    StringValue: str
    Title: str


class PmiString(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class PmiSettingsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreatePreferencesBuilder(self) -> Annotations.PmiPreferencesBuilder:
        ...
    def CreatePmiEditSectionViewSettingsBuilder(self, viewTag: View) -> Annotations.PmiEditSectionViewSettingsBuilder:
        ...
    def Tag(self) -> Tag: ...



class PmiSemanticData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class PmiSectionViewViewBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AssemblyCrosshatching: bool
    AssociativePlane: bool
    ClipCoplanarObjects: bool
    ClipWireframeObjects: bool
    CrosshatchAdjacencyTolerance: float
    CrosshatchPatternDefinedBy: Annotations.PmiSectionViewViewBuilder.CrosshatchPatternBy
    DisplayCrosshatch: bool
    RestrictCrosshatchAngle: bool
    SectionNamePrefix: str


    class CrosshatchPatternBy(enum.Enum):
        User = 0
        Material = 1
    

class PmiSectionViewSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObject(self, selectedObject: NXObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Crosshatch: Annotations.HatchFillSettingsBuilder
    CuttingPlaneSymbol: Annotations.CuttingPlaneSymbolBuilder
    View: Annotations.PmiSectionViewViewBuilder


class PmiSectionViewCuttingPlaneSymbolBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ArrowDirection: Annotations.PmiSectionViewCuttingPlaneSymbolBuilder.ArrowDirectionOptions
    ArrowLineLength: float
    Color: NXColor
    DisplayCuttingPlaneSymbol: bool
    MarginPercentage: float
    SectionPrefix: str
    ShadedPlane: bool
    SizeBasedOnSectionCut: bool
    StartingLetter: str
    TextPlaneRelativeToArrow: Annotations.PmiSectionViewCuttingPlaneSymbolBuilder.TextPlaneRelativeToArrowOptions
    UseTwoArrows: bool
    ViewNameFormat: Annotations.PmiSectionViewCuttingPlaneSymbolBuilder.ViewNameFormatOption


    class ViewNameFormatOption(enum.Enum):
        UserDefined = 0
        A = 1
        AA = 2
    

    class TextPlaneRelativeToArrowOptions(enum.Enum):
        Parallel = 0
        Perpendicular = 1
    

    class ArrowDirectionOptions(enum.Enum):
        TowardPlane = 0
        AwayfromPlane = 1
    

class PmiResizeMethod(enum.Enum):
    ViewScale = 1
    ZoomFactor = 2
    Independent = 3
    PartPreferences = 4


class PmiRegionData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    Diameter: float
    Height: float
    InnerDiameter: float
    Point1: Point3d
    Point2: Point3d
    RegionType: Annotations.PmiRegionData.RegionTypes
    Width: float


    class RegionTypes(enum.Enum):
        Unspecified = 0
        AnnularType = 1
        CircularType = 2
        CylindricalType = 3
        RectangularType = 4
        ArbitraryType = 5
    

class PmiRegionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Region]:
        ...
    def __init__(self, owner: Annotations.PmiManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRegionBuilder(self, region: Annotations.Region) -> Annotations.RegionBuilder:
        ...
    def Tag(self) -> Tag: ...



class PmiRapidDimensionBuilder(Annotations.BaseRapidDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiRadiusDimension(Annotations.BaseRadiusDimension):
    def __init__(self) -> None: ...


class PmiRadialDimensionBuilder(Annotations.BaseRadialDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiProprietaryInfoData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetText(self) -> str:
        ...
    Identifier: str
    Title: str


class PmiProductGridBuilder(Annotations.BaseProductGridBuilder):
    def __init__(self) -> None: ...


class PmiProductGrid(Annotations.BaseProductGrid):
    def __init__(self) -> None: ...


class PmiProcessSpecificationData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetNomenclature(self, nomenclatureLines: str) -> None:
        ...
    def GetOpenField(self, openFieldLines: str) -> None:
        ...
    Identifier: str
    Revision: str
    Title: str


class PmiPreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObject(self, selectedObject: NXObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    AnnotationOriginAlignment: Annotations.OriginAlignmentBuilder
    AnnotationStyle: Annotations.StyleBuilder
    CommonWorkflow: Annotations.CommonWorkflowBuilder
    DimensionOriginAlignment: Annotations.OriginAlignmentBuilder
    DimensionWorkflow: Annotations.DimensionWorkflowBuilder
    PmiGeneralSetupDisplay: Annotations.PmiGeneralSetupDisplayBuilder
    PmiGeneralSetupEffectivity: Annotations.PmiGeneralSetupEffectivityBuilder
    PmiGeneralSetupGeneral: Annotations.PmiGeneralSetupGeneralBuilder
    PmiGeneralSetupParallelToScreen: Annotations.PmiGeneralSetupParallelToScreenBuilder
    PmiSectionViewCuttingPlaneSymbol: Annotations.PmiSectionViewCuttingPlaneSymbolBuilder
    PmiSectionViewView: Annotations.PmiSectionViewViewBuilder
    PmiSupplementalGeometryProductGrid: Annotations.PmiSupplementalGeometryProductGridBuilder
    PmiSupplementalGeometryRegion: Annotations.PmiSupplementalGeometryRegionBuilder
    RetainedAnnotations: Annotations.RetainedAnnotationsBuilder
    SymbolWorkflow: Annotations.SymbolWorkflowBuilder
    TableCellStyle: Annotations.TableCellStyleBuilder
    TableOriginAlignment: Annotations.OriginAlignmentBuilder
    TableSection: Annotations.TableSectionStyleBuilder
    TabularNoteStyle: Annotations.TabularNoteStyleBuilder


class PmiPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetShadedDisplay(self, shadedDisplay: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupDisplayBuilder.DisplayPmiShadedModel instead.")"""
        ...
    def SetEnableResize(self, enableResize: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupDisplayBuilder.EnableResize instead.")"""
        ...
    def SetResizeOnCreate(self, resizeOnCreate: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupDisplayBuilder.ResizeOnCreate instead.")"""
        ...
    def SetResizeOnViewSave(self, resizeOnViewSave: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupDisplayBuilder.ResizeOnViewSave instead.")"""
        ...
    def SetResizeMethod(self, resizeMethod: Annotations.PmiResizeMethod) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupDisplayBuilder.ResizeSettings instead.")"""
        ...
    def SetPmiSupportForGeometrySharing(self, pmiSupportForGeomSharing: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupGeneralBuilder.PmiSupportForGeometrySharing instead.")"""
        ...
    def SetDisplayPmiEffectivityMethod(self, displayPmiEffectivityMethod: Annotations.DisplayPmiEffectivityMethod) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupEffectivityBuilder.DisplayPmiAssociatedOnlyToPrimaryGeometry instead.")"""
        ...
    def SetDisplayPmiEffectivityReferenceMethod(self, displayPmiEffectivityReferenceMethod: Annotations.DisplayPmiEffectivityMethod) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupEffectivityBuilder.DisplayPmiAssociatedToReferenceGeometry instead.")"""
        ...
    def SetDisplayPmiAssociatedComponentsLoadedForReference(self, displayPmiAssociatedComponentsLoadedForReference: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupEffectivityBuilder.ComponentsLoadedForReference instead.")"""
        ...
    def SetDisplayEffectivityFilterNodesInPartNavigator(self, displayEffectivityFilterNodesInPartNavigator: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupEffectivityBuilder.DisplayEffectivityFilteredNodes instead.")"""
        ...
    def SetAssemblyCrosshatching(self, assemblyCrosshatching: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiSectionViewViewBuilder.AssemblyCrosshatching instead.")"""
        ...
    def SetRestrictCrosshatchAngle(self, restrictCrosshatchAngle: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiSectionViewViewBuilder.RestrictCrosshatchAngle instead.")"""
        ...
    def SetCrosshatchAdjacencyTolerance(self, crosshatchAdjacencyTolerance: float) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiSectionViewViewBuilder.CrosshatchAdjacencyTolerance instead.")"""
        ...
    def SetAssociativityForLightweightSectionViews(self, associativityOptionForLightweightSectionViews: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiSectionViewViewBuilder.AssociativePlane instead.")"""
        ...
    def GetParallelToScreenEnabledPmiTypes(self, parallelToScreenEnabledPmiTypes: typing.List[Annotations.PmiPreferences.PreferenceSymbolTypes]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupParallelToScreenBuilder.EnabledPmiTypes instead.")"""
        ...
    def SetParallelToScreenEnabledPmiTypes(self, parallelToScreenEnabledPmiTypes: typing.List[Annotations.PmiPreferences.PreferenceSymbolTypes]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.Annotations.PmiGeneralSetupParallelToScreenBuilder.EnabledPmiTypes instead.")"""
        ...
    AssemblyCrosshatching: bool
    AssociativityForLightweightSectionViews: bool
    ClipCoplanarObjectsForLightweightSectionViews: bool
    ClipWireframeObjects: bool
    CreateViewIndependent: bool
    CrosshatchAdjacencyTolerance: float
    CuttingPlaneSymbolArrowDirection: Annotations.CuttingPlaneSymbolBuilder.ArrowDirectionOption
    CuttingPlaneSymbolArrowLength: float
    CuttingPlaneSymbolColor: NXColor
    CuttingPlaneSymbolSectionPrefix: str
    CuttingPlaneSymbolShadedPlane: bool
    CuttingPlaneSymbolStartingLetter: str
    CuttingPlaneSymbolTextPlaneRelativeToArrow: Annotations.CuttingPlaneSymbolBuilder.TextPlaneRelativeArrow
    DatumLabel: str
    DefaultPlane: Annotations.PmiDefaultPlane
    DeleteEmptyUserDefinedModelViews: bool
    DisplayEffectivityFilterNodesInPartNavigator: bool
    DisplayPmiAssociatedComponentsLoadedForReference: bool
    DisplayPmiEffectivityMethod: Annotations.DisplayPmiEffectivityMethod
    DisplayPmiEffectivityReferenceMethod: Annotations.DisplayPmiEffectivityMethod
    DisplayPmiModelViewDisclosurePurpose: str
    DisplayPmiQueryDialogFromMb3: bool
    DisplayPmiUserDefinedModelViewDisclosure: bool
    EnableResize: bool
    LockSizeAndPosition: bool
    ParallelToScreen: bool
    PmiRegionHeight: float
    PmiRegionInnerDiameter: float
    PmiRegionOuterDiameter: float
    PmiRegionWidth: float
    PmiSupportForGeometrySharing: bool
    RegionBoundaryColor: NXColor
    RegionBoundaryFont: int
    RegionBoundaryWidth: int
    ResizeMethod: Annotations.PmiResizeMethod
    ResizeOnCreate: bool
    ResizeOnViewSave: bool
    RestrictCrosshatchAngle: bool
    SectionViewNamePrefix: str
    ShadedDisplay: bool
    SuppressRetainedPmis: bool


    class PreferenceSymbolTypes(enum.Enum):
        Note = 0
        GeneralNote = 1
        SpecificNote = 2
        EnterpriseId = 3
        MaterialSpecification = 4
        PartId = 5
        ProcessSpecification = 6
        UrlNote = 7
        StringNote = 8
        NumberNote = 9
        IntegerNote = 10
        BalloonNote = 11
        CustomSymbol = 12
        GovernmentSecurityInfo = 13
        CompanySpecificProprietaryInfo = 14
        ExportControl = 15
        Table = 16
        CoordinateNote = 17
        CuttingPlaneSymbol = 18
    

class PmiPerpendicularDimension(Annotations.BasePerpendicularDimension):
    def __init__(self) -> None: ...


class PmiPartIdentificationData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    DescriptiveModifier: str
    FirstNomenclature: str
    Identifier: str
    ItemName: str
    ItemNameModifier: str
    Revision: str
    SecondNomenclature: str
    ThirdNomenclature: str
    Title: str


class PmiParallelDimension(Annotations.BaseParallelDimension):
    def __init__(self) -> None: ...


class PmiOrdinateOriginDimension(Annotations.OrdinateOriginDimension):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiOrdinateDimensionBuilder(Annotations.BaseOrdinateDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiNumberBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    NumberValue: float
    Title: str


class PmiNumber(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class PmiNoteData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetText(self, textLines: str) -> None:
        ...
    AllAround: bool


class PmiNoteBuilder(Annotations.DraftingNoteBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiNote(Annotations.BaseNote):
    def __init__(self) -> None: ...


class PmiMinorAngularDimensionBuilder(Annotations.PmiAngularDimensionBuilder):
    def __init__(self) -> None: ...


class PmiMinorAngularDimension(Annotations.PmiAngularDimension):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiMaterialSpecificationData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetNomenclature(self) -> str:
        ...
    def GetOpenField(self) -> str:
        ...
    AlternateMaterialName: str
    Identifier: str
    MaterialCategory: str
    MaterialName: str
    MaterialType: str
    Revision: str
    Title: str


class PmiManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CopyObjects(self, inputObjects: typing.List[Annotations.Pmi]) -> typing.List[Annotations.Pmi]:
        ...
    def CopyDisplayInstanceObjects(self, inputObjects: typing.List[Annotations.Annotation], view: View) -> typing.List[Annotations.Annotation]:
        ...
    def CutDisplayInstanceObjects(self, inputObjects: typing.List[Annotations.Annotation], cutViews: typing.List[View], viewOfPaste: View) -> None:
        ...
    def RestoreUnpastedObjects(self) -> None:
        ...
    def IsInheritedPmi(self, object: Annotations.Annotation) -> bool:
        ...
    def GetInheritParent(self, inheritedPmi: Annotations.Annotation) -> Annotations.Annotation:
        ...
    def GetDisplayInstanceParent(self, displayInstance: Annotations.Annotation) -> Annotations.Pmi:
        ...
    def CreateArbitraryAreaSeedBuilder(self) -> Annotations.ArbitraryAreaSeedBuilder:
        ...
    def DeleteReplaceAnnotation(self, oldAnnotation: Annotations.Annotation, newAnnotation: Annotations.Annotation) -> None:
        ...
    def Resize(self) -> None:
        ...
    def ResetSize(self) -> None:
        ...
    def CreateExplicitOrderBuilder(self) -> Annotations.PMIExplicitOrderBuilder:
        ...
    def ApplyModelViewOrder(self, savedOrderName: str) -> None:
        ...
    def SaveModelViewOrder(self, orderList: str, saveName: str) -> None:
        ...
    def IsEffectivityFiltered(self, object: Annotations.Pmi) -> bool:
        ...
    def CreateSuppressPmibuilder(self) -> Annotations.SuppressPMIBuilder:
        ...
    def Position(self, view: View) -> None:
        ...
    def PositionSelected(self, view: View, selectedPmisTag: typing.List[TaggedObject]) -> None:
        ...
    def LoadPmi(self) -> None:
        ...
    def CreateConvertPmiBuilder(self) -> Annotations.ConvertPmiBuilder:
        ...
    def SetComponentPmiDisplay(self, selectedComponents: typing.List[Assemblies.Component], doDisplay: bool) -> None:
        ...
    def GetComponentPmiDisplayStatus(self, component: Assemblies.Component) -> Annotations.PmiManager.ComponentPmiDisplayStatus:
        ...
    def ResetComponentPmiDisplayStatus(self, selectedComponents: typing.List[Assemblies.Component]) -> None:
        ...
    def Tag(self) -> Tag: ...

    Pmis: Annotations.PmiCollection
    PmiAttributes: Annotations.PmiAttributeCollection
    PmiRegions: Annotations.PmiRegionCollection
    SearchModelViews: Annotations.SearchModelViewCollection
    PmiLightweightSections: Annotations.PmiLightweightSectionCollection
    PmiWave: Annotations.PmiWaveCollection


    class ComponentPmiDisplayStatus(enum.Enum):
        DoDisplay = 0
        DoNotDisplay = 1
        Unknown = 2
    

class PmiMajorAngularDimensionBuilder(Annotations.PmiAngularDimensionBuilder):
    def __init__(self) -> None: ...


class PmiMajorAngularDimension(Annotations.PmiAngularDimension):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiLocatorDesignatorData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    AttributeType: str
    ChangeLevelType: str
    CoordinatePlane: str
    DecimalPrecision: int
    FunctionalSubscript: str
    Group: str
    Hotspot: str
    Letter: str
    NormalDirection: Vector3d
    Note: str
    PartName: str
    PinDirection: Vector3d
    PunchDirection: Vector3d
    Subtype: str
    SymbolName: str
    Title: str


class PmiLineWeldData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    AllAround: bool
    AlongContour: Annotations.PmiLineWeldData.AlongContourTypes
    ArrowSideCompound: bool
    ArrowSideCompoundMainSize: str
    ArrowSideFinishSymbol: Annotations.PmiLineWeldData.FinishSymbolTypes
    ArrowSideGrooveAngle: str
    ArrowSideGrooveGap: str
    ArrowSideLongitudinalSize: str
    ArrowSideMainSize: str
    ArrowSideStaggeredSize: str
    ArrowSideSupplementalSymbol: Annotations.PmiLineWeldData.SupplementalSymbolTypes
    ArrowSideSymbol: Annotations.PmiLineWeldData.SymbolTypes
    Centered: bool
    Delta: bool
    Field: bool
    IncludeReferenceSign: bool
    OtheSideSupplementalSymbol: Annotations.PmiLineWeldData.SupplementalSymbolTypes
    OtherSideCompound: bool
    OtherSideCompoundMainSize: str
    OtherSideFinishSymbol: Annotations.PmiLineWeldData.FinishSymbolTypes
    OtherSideGrooveAngle: str
    OtherSideGrooveGap: str
    OtherSideLongitudinalSize: str
    OtherSideMainSize: str
    OtherSideStaggeredSize: str
    OtherSideSymbol: Annotations.PmiLineWeldData.SymbolTypes
    Staggered: bool
    StandardType: Annotations.PmiLineWeldData.StandardTypes


    class SymbolTypes(enum.Enum):
        None = 0
        EdgeFlange = 1
        DoubleFlange = 2
        FlareSingleVGroove = 3
        Square = 4
        SquareGroove = 5
        SingleV = 6
        SingleVGroove = 7
        SingleBevel = 8
        SingleBevelGroove = 9
        SingleFlange = 10
        FlareSingleBevelGroove = 11
        SingleVBroadRootFace = 12
        SingleBevelBroadRootFace = 13
        SingleU = 14
        SingleUGroove = 15
        SingleJ = 16
        SingleJGroove = 17
        Backing = 18
        Bead = 19
        KGroove = 20
        Fillet = 21
        JisFillet = 22
        Stake = 23
        Plug = 24
        PlugAndSlot = 25
        Seam = 26
        Seam2 = 27
        JisSeam = 28
        SteepFlankedSingleV = 29
        SteepFlankedSingleBevel = 30
        Edge = 31
        Edge2 = 32
        Surface = 33
        Overlay = 34
        SurfaceJoint = 35
        SolderedJoint = 36
        InclinedJoint = 37
        FoldJoint = 38
        Spot = 39
        Spot2 = 40
        Stud = 41
        SpotProjected = 42
        PermanentBackingStrip = 43
        RemovableBackingStrip = 44
        JisStaggeredFillet1 = 45
        JisStaggeredFillet2 = 46
    

    class SupplementalSymbolTypes(enum.Enum):
        None = 0
        Flush = 1
        Convex = 2
        Concave = 3
        ToesBlended = 4
        PermanentBackingStripSupplemental = 5
        RemovableBackingStripSupplemental = 6
        MeltThrough = 7
    

    class StandardTypes(enum.Enum):
        None = 0
        Ansi = 1
        Iso = 2
        Din = 3
        Jis = 4
        Eskd = 5
        Gb = 6
    

    class FinishSymbolTypes(enum.Enum):
        None = 0
        Chipping = 1
        Grinding = 2
        Machining = 3
        Hammering = 4
        Peening = 5
        Rolling = 6
        Finishing = 7
    

    class AlongContourTypes(enum.Enum):
        None = 0
        Closed = 1
        Unclosed = 2
        Trilateral = 3
        AllAround = 4
    

class PmiLineWeldBuilder(Annotations.LineWeldBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiLineWeld(Annotations.LineWeld):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiLinearDimensionBuilder(Annotations.BaseLinearDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder
    AssociatedObjectsSets: Annotations.AssociatedObjectsSetsBuilder


class PmiLightweightSectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.LightweightSection]:
        ...
    def __init__(self, owner: Annotations.PmiManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLightweightSectionBuilder(self, view: Annotations.LightweightSection) -> Annotations.LightweightSectionBuilder:
        ...
    def FindObject(self, name: str) -> Annotations.LightweightSection:
        ...
    def Tag(self) -> Tag: ...



class PmiLabel(Annotations.Label):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiInterpartSelectionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    SelectedPmi: SelectDisplayableObjectList


class PmiIntegerBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    IntegerValue: int
    Title: str


class PmiInteger(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class PmiHorizontalOrdinateDimension(Annotations.HorizontalOrdinateDimension):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiHorizontalDimension(Annotations.BaseHorizontalDimension):
    def __init__(self) -> None: ...


class PmiHoleDimension(Annotations.BaseHoleDimension):
    def __init__(self) -> None: ...


class PmiGovernmentSecurityInfoData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetText(self) -> str:
        ...
    Identifier: str
    Title: str


class PmiGeneralSetupParallelToScreenBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DisplayParallelToScreen: bool
    EnabledPmiTypes: int
    LockSizeAndPosition: bool


class PmiGeneralSetupGeneralBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DeleteEmptyUserDefinedModelViews: bool
    DisclosurePurpose: str
    PmiSupportForGeometrySharing: bool
    SuppressRetainedPMI: bool
    UserDefinedModelViews: bool


class PmiGeneralSetupEffectivityBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ComponentsLoadedForReference: bool
    DisplayEffectivityFilteredNodes: bool
    DisplayPmiAssociatedOnlyToPrimaryGeometry: Annotations.PmiGeneralSetupEffectivityBuilder.PrimaryGeometryType
    DisplayPmiAssociatedToReferenceGeometry: Annotations.PmiGeneralSetupEffectivityBuilder.ReferenceGeometryType


    class ReferenceGeometryType(enum.Enum):
        IfAllAssociatedOccurrencesareLoaded = 0
        IfAnyAssociatedOccurrencesareLoaded = 1
    

    class PrimaryGeometryType(enum.Enum):
        IfAllAssociatedOccurrencesareLoaded = 0
        IfAnyAssociatedOccurrencesareLoaded = 1
    

class PmiGeneralSetupDisplayBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AnnotationPlane: Annotations.PmiGeneralSetupDisplayBuilder.AnnotationPlaneType
    AnnotationPlaneColor: int
    AnnotationPlaneDisplay: Annotations.PmiGeneralSetupDisplayBuilder.AnnotationPlaneDisplayType
    AnnotationPlaneFont: LineFontBuilder
    AnnotationPlaneTranslucency: int
    BackgroundColor: NXColor
    DisplayInAllViews: bool
    DisplayPmiShadedModel: bool
    EnableBackground: bool
    EnableResize: bool
    ProjectOntoPlane: bool
    ResizeOnCreate: bool
    ResizeOnViewSave: bool
    ResizeSettings: Annotations.PmiGeneralSetupDisplayBuilder.ResizeSettingsType
    UpdateReadingDirection: bool


    class ResizeSettingsType(enum.Enum):
        RelativetoSavedViewScale = 0
        RelativetoViewZoomFactor = 1
        Independently = 2
        RelativetoPartPreferences = 3
    

    class AnnotationPlaneType(enum.Enum):
        XYPlaneofWCS = 0
        XZPlaneofWCS = 1
        YZPlaneofWCS = 2
        ModelViewPlane = 3
    

    class AnnotationPlaneDisplayType(enum.Enum):
        All = 0
        ActivePlaneOnly = 1
        None = 2
    

class PmiFoldedRadiusDimension(Annotations.BaseFoldedRadiusDimension):
    def __init__(self) -> None: ...


class PmiFilterCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.PmiFilter]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateByTypesFilter(self, componentMethod: Annotations.PmiFilter.ComponentMethod, components: typing.List[Assemblies.Component], types: typing.List[Annotations.PmiFilterByType.Type]) -> Annotations.PmiFilter:
        ...
    def CreateByViewsFilter(self, componentMethod: Annotations.PmiFilter.ComponentMethod, components: typing.List[Assemblies.Component], views: str) -> Annotations.PmiFilter:
        ...
    def CreateByPartsFilter(self, componentMethod: Annotations.PmiFilter.ComponentMethod, components: typing.List[Assemblies.Component]) -> Annotations.PmiFilter:
        ...
    def Tag(self) -> Tag: ...



class PmiFilterByView(Annotations.PmiFilter):
    def __init__(self) -> None: ...
    def GetPmiViews(self) -> str:
        ...
    def SetPmiViews(self, views: str) -> None:
        ...
    def AddPmiView(self, view: str) -> None:
        ...


class PmiFilterByType(Annotations.PmiFilter):
    def __init__(self) -> None: ...
    def GetPmiTypes(self) -> typing.List[Annotations.PmiFilterByType.Type]:
        ...
    def SetPmiTypes(self, types: typing.List[Annotations.PmiFilterByType.Type]) -> None:
        ...


    class Type(enum.Enum):
        Dimension = 0
        FeatureControlFrame = 1
        Datum = 2
        DatumTarget = 3
        Note = 4
        GeneralNote = 5
        SpecificNote = 6
        CoordinateNote = 7
        BalloonNote = 8
        CustomSymbol = 9
        Centerline = 10
        LineWeld = 11
        Crosshatch = 12
        Material = 13
        SurfaceFinish = 14
        Locator = 15
        EnterpriseIdentifier = 16
        Process = 17
        PartIdentifier = 18
        Emarking = 19
        Url = 20
        UserDefined = 21
        Geometry = 22
        CuttingPlaneSymbol = 23
        Table = 24
    

class PmiFilterByPart(Annotations.PmiFilter):
    def __init__(self) -> None: ...


class PmiFilter(NXObject):
    def __init__(self) -> None: ...
    def GetFilterType(self) -> Annotations.PmiFilter.FilterType:
        ...
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def SetComponents(self, components: typing.List[Assemblies.Component]) -> None:
        ...
    def GetComponentMethod(self) -> Annotations.PmiFilter.ComponentMethod:
        ...
    def SetComponentMethod(self, componentMethod: Annotations.PmiFilter.ComponentMethod) -> None:
        ...
    def ApplyToView(self, view: View) -> None:
        ...
    def RemoveFromView(self, view: View) -> None:
        ...
    def GetAppliedViews(self) -> typing.List[View]:
        ...
    def EnableInView(self, view: View, enabled: bool) -> None:
        ...
    def Copy(self) -> Annotations.PmiFilter:
        ...
    def IsEnabled(self, view: View) -> bool:
        ...
    def UpdatePmiDisplay(self) -> None:
        ...


    class FilterType(enum.Enum):
        ByType = 0
        ByView = 1
        ByComponent = 2
    

    class ComponentMethod(enum.Enum):
        Selected = 0
        SelectedAndChildren = 1
        All = 2
    

class PmiFeatureControlFrameBuilder(Annotations.FeatureControlFrameBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiFcfDatumData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    FreeState: bool
    Label: str
    MaterialModifier: Annotations.DatumReferenceBuilder.DatumReferenceMaterialCondition
    Projected: bool


class PmiFcfData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetAboveAppendedText(self, textLines: str) -> None:
        ...
    def GetBelowAppendedText(self, textLines: str) -> None:
        ...
    def GetBeforeAppendedText(self, textLines: str) -> None:
        ...
    def GetAfterAppendedText(self, textLines: str) -> None:
        ...
    def GetZoneShape(self, frameNumber: int) -> Annotations.FeatureControlFrameDataBuilder.ToleranceZoneShape:
        ...
    def GetToleranceValue(self, frameNumber: int) -> str:
        ...
    def GetToleranceZoneModifier(self, frameNumber: int) -> Annotations.FeatureControlFrameDataBuilder.ToleranceMaterialModifier:
        ...
    def GetReciprocityRequirement(self, frameNumber: int) -> bool:
        ...
    def GetFreeState(self, frameNumber: int) -> bool:
        ...
    def GetStatistical(self, frameNumber: int) -> bool:
        ...
    def GetTangential(self, frameNumber: int) -> bool:
        ...
    def GetCommonZone(self, frameNumber: int) -> bool:
        ...
    def GetProjectedZone(self, frameNumber: int) -> bool:
        ...
    def GetProjectedZoneValue(self, frameNumber: int) -> str:
        ...
    def GetUnequallyDisposedZone(self, frameNumber: int) -> bool:
        ...
    def GetUz(self, frameNumber: int) -> bool:
        ...
    def GetUnequallyDisposedZoneValue(self, frameNumber: int) -> str:
        ...
    def GetDynamicProfile(self, frameNumber: int) -> bool:
        ...
    def GetDerivedFeature(self, frameNumber: int) -> bool:
        ...
    def GetLeastSquaresFeature(self, frameNumber: int) -> bool:
        ...
    def GetMinmaxFeature(self, frameNumber: int) -> bool:
        ...
    def GetCircumscribedFeature(self, frameNumber: int) -> bool:
        ...
    def GetInscribedFeature(self, frameNumber: int) -> bool:
        ...
    def GetMaxTolerance(self, frameNumber: int) -> bool:
        ...
    def GetMaxToleranceValue(self, frameNumber: int) -> str:
        ...
    def GetUnitBasis(self, frameNumber: int) -> bool:
        ...
    def GetUnitBasisType(self, frameNumber: int) -> Annotations.PmiFcfData.PmiFcfDataUnitBasisType:
        ...
    def GetUnitBasisZoneShape(self, frameNumber: int) -> Annotations.FeatureControlFrameDataBuilder.AreaSymbolType:
        ...
    def GetUnitBasisValue(self, frameNumber: int) -> str:
        ...
    def GetUnitBasisXRange(self, frameNumber: int) -> str:
        ...
    def GetUnitBasisYRange(self, frameNumber: int) -> str:
        ...
    def GetPrimaryDatumReference(self, frameNumber: int, datums: typing.List[Annotations.PmiFcfDatumData]) -> None:
        ...
    def GetPrimaryDatumExtendedText(self, frameNumber: int) -> str:
        ...
    def GetSecondaryDatumReference(self, frameNumber: int, datums: typing.List[Annotations.PmiFcfDatumData]) -> None:
        ...
    def GetSecondaryDatumExtendedText(self, frameNumber: int) -> str:
        ...
    def GetTertiaryDatumReference(self, frameNumber: int, datums: typing.List[Annotations.PmiFcfDatumData]) -> None:
        ...
    def GetTertiaryDatumExtendedText(self, frameNumber: int) -> str:
        ...
    def GetBeforeIndicatorCount(self, frameNumber: int) -> int:
        ...
    def GetAfterIndicatorCount(self, frameNumber: int) -> int:
        ...
    def GetBeforeIndicatorType(self, frameNumber: int, indicatorNumber: int) -> Annotations.FeatureControlFrameIndicatorBuilder.FcfIndicatorType:
        ...
    def GetAfterIndicatorType(self, frameNumber: int, indicatorNumber: int) -> Annotations.FeatureControlFrameIndicatorBuilder.FcfIndicatorType:
        ...
    def GetBeforeIndicatorCharacteristic(self, frameNumber: int, indicatorNumber: int) -> Annotations.FeatureControlFrameIndicatorBuilder.FcfIndicatorCharacteristic:
        ...
    def GetAfterIndicatorCharacteristic(self, frameNumber: int, indicatorNumber: int) -> Annotations.FeatureControlFrameIndicatorBuilder.FcfIndicatorCharacteristic:
        ...
    def GetBeforeIndicatorDatumReference(self, frameNumber: int, indicatorNumber: int) -> Annotations.PmiFcfDatumData:
        ...
    def GetAfterIndicatorDatumReference(self, frameNumber: int, indicatorNumber: int) -> Annotations.PmiFcfDatumData:
        ...
    Characteristic: Annotations.FeatureControlFrameBuilder.FcfCharacteristic
    FrameCount: int


    class PmiFcfDataUnitBasisType(enum.Enum):
        None = 0
        Length = 1
        Area = 2
        CircularArea = 3
        SphericalArea = 4
        Square = 5
    

class PmiExportControlData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetText(self) -> str:
        ...
    Identifier: str
    Title: str


class PMIExplicitOrderBuilder(Gateway.BaseExplicitOrderBuilder):
    def __init__(self) -> None: ...


class PmiEnterpriseIdentifierData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetAddress(self, addressLines: str) -> None:
        ...
    CageCode: int
    CageCodeName: str
    CompanyName: str
    DivisionSite: str
    Revision: str
    Title: str


class PmiEditSectionViewSettingsBuilder(Drafting.BaseEditSettingsBuilder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObject(self, selectedObject: NXObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    Settings: Annotations.PmiSectionViewSettingsBuilder


class PmiEdgeConditionSymbolCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.PmiEdgeConditionSymbol]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePmiEdgeConditionSymbolBuilder(self, annotation: Annotations.PmiEdgeConditionSymbol) -> Annotations.PmiEdgeConditionSymbolBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.PmiEdgeConditionSymbol:
        ...
    def Tag(self) -> Tag: ...



class PmiEdgeConditionSymbolBuilder(Annotations.BaseEdgeConditionSymbolBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiEdgeConditionSymbol(Annotations.BaseEdgeConditionSymbol):
    def __init__(self) -> None: ...


class PmiDimensionData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetAboveAppendedText(self, textLines: str) -> None:
        ...
    def GetBelowAppendedText(self, textLines: str) -> None:
        ...
    def GetBeforeAppendedText(self, textLines: str) -> None:
        ...
    def GetAfterAppendedText(self, textLines: str) -> None:
        ...
    def GetNthParameterDimensionFeatureType(self, nth: int) -> Annotations.HoleCalloutSettingsBuilder.Parametertype:
        ...
    def GetNthParameterDimensionValue(self, nth: int) -> str:
        ...
    def GetNthParameterDimensionType(self, nth: int) -> str:
        ...
    def GetNthParameterDimensionPrefix(self, nth: int) -> str:
        ...
    def GetNthParameterDimensionSuffix(self, nth: int) -> str:
        ...
    def GetNthParameterDimensionHoleUpperDelta(self, nth: int) -> float:
        ...
    def GetNthParameterDimensionHoleLowerDelta(self, nth: int) -> float:
        ...
    def GetNthParameterDimensionHoleGrade(self, nth: int) -> int:
        ...
    def GetNthParameterDimensionHoleDeviation(self, nth: int) -> str:
        ...
    def GetNthParameterDimensionShaftUpperDelta(self, nth: int) -> float:
        ...
    def GetNthParameterDimensionShaftLowerDelta(self, nth: int) -> float:
        ...
    def GetNthParameterDimensionShaftGrade(self, nth: int) -> int:
        ...
    def GetNthParameterDimensionShaftDeviation(self, nth: int) -> str:
        ...
    def GetNthParameterDimensionUpperDelta(self, nth: int) -> float:
        ...
    def GetNthParameterDimensionLowerDelta(self, nth: int) -> float:
        ...
    def GetNthParameterDimensionGrade(self, nth: int) -> int:
        ...
    def GetNthParameterDimensionDeviation(self, nth: int) -> str:
        ...
    AllAround: bool
    AllOver: bool
    AngleNumerator: float
    Basic: bool
    Deviation: str
    DimensionValue: float
    Direction: Vector3d
    FeatureOfSize: bool
    FitGrade: int
    Grade: int
    HoleDeviation: str
    HoleGrade: int
    HoleLowerDelta: float
    HoleUpperDelta: float
    IsFitDesignation: bool
    LowerDelta: float
    Manual: bool
    NotToScale: bool
    NumberOfParameterDimensions: int
    PitchDiaDeviation: str
    PitchDiaGrade: int
    PitchDiaLowerDelta: float
    PitchDiaUpperDelta: float
    Reference: bool
    ReferenceDimensionPrefix: str
    ReferenceDimensionSuffix: str
    ShaftDeviation: str
    ShaftGrade: int
    ShaftLowerDelta: float
    ShaftUpperDelta: float
    ThreadClass: int
    Type: Annotations.PmiDimensionData.DimensionType
    UpperDelta: float


    class DimensionType(enum.Enum):
        None = 0
        Chamfer = 1
        Radial = 2
        Linear = 3
        Angular = 4
        CurveLength = 5
        Holecallout = 6
    

class PmiDiameterDimension(Annotations.BaseDiameterDimension):
    def __init__(self) -> None: ...


class PmiDefaultPlane(enum.Enum):
    XyOfWcs = 1
    ModelView = 2
    XzOfWcs = 3
    YzOfWcs = 4
    Last = 1000


class PmiDatumTargetData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    AreaSize: str
    Diameter: float
    FirstPoint: Point3d
    Index: int
    InnerDiameter: float
    IsMovable: bool
    Label: str
    Length: float
    MovableModifierAngle: float
    SecondPoint: Point3d
    Type: Annotations.PmiDatumTargetData.Types
    Width: float


    class Types(enum.Enum):
        None = 0
        Point = 1
        Line = 2
        Rectangular = 3
        Circular = 4
        Cylindrical = 5
        Spherical = 6
        Arbitrary = 7
    

class PmiDatumTargetBuilder(Annotations.DatumTargetBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder
    RegionSelection: SelectDisplayableObject


class PmiDatumFeatureSymbolBuilder(Annotations.DatumFeatureSymbolBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiDatumData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    AllAround: bool
    IndividuallyApplied: bool
    Label: str


class PmiData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    def GetIndex(self) -> int:
        ...
    def SetIndex(self, index: int) -> None:
        ...
    def GetNumAssociatedObjectsSets(self) -> int:
        ...
    def SetNumAssociatedObjectsSets(self, numAssocObjectsSets: int) -> None:
        ...


class PmiCylindricalDimension(Annotations.BaseCylindricalDimension):
    def __init__(self) -> None: ...


class PmiCustomSymbolBuilder(Annotations.BaseCustomSymbolBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiCustomSymbol(Annotations.BaseCustomSymbol):
    def __init__(self) -> None: ...


class PmiCurveLengthDimensionBuilder(Annotations.BaseCurveLengthDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiCoordinateNoteData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    Category: str
    CoordinateSystem: CoordinateSystem
    DecimalPlaces: int
    IPrefix: str
    ISuffix: str
    IncludeI: bool
    IncludeJ: bool
    IncludeK: bool
    IncludeLabel: bool
    IncludeLevel: bool
    IncludeX: bool
    IncludeY: bool
    IncludeZ: bool
    JPrefix: str
    JSuffix: str
    KPrefix: str
    KSuffix: str
    LabelPrefix: str
    LabelSuffix: str
    LevelPrefix: str
    LevelSuffix: str
    Revision: str
    Title: str
    TrackedObject: NXObject
    XPrefix: str
    XSuffix: str
    YPrefix: str
    YSuffix: str
    ZPrefix: str
    ZSuffix: str


class PmiConcentricCircleDimension(Annotations.BaseConcentricCircleDimension):
    def __init__(self) -> None: ...


class PmiCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Pmi]:
        ...
    def __init__(self, owner: Annotations.PmiManager) -> None: ...
    def __init__(self) -> None: ...
    def ExpandCollapsePmiNode(self, expand: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class PmiChamferDimensionBuilder(Annotations.BaseChamferDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiChamferDimension(Annotations.BaseChamferDimension):
    def __init__(self) -> None: ...


class PmiChainDimension(Annotations.ChainDimension):
    def __init__(self) -> None: ...


class PmiCenterMarkBuilder(Annotations.BaseCenterMarkBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder
    Plane: Annotations.PlaneBuilder


class PmiCenterMark(Annotations.BaseCenterMark):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiCenterline3dBuilder(Annotations.BaseCenterline3dBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder


class PmiCenterline3d(Annotations.BaseCenterline3d):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiCadNeutralAnnotation(Annotations.Annotation):
    def __init__(self) -> None: ...


class PmiBoltCircleCenterlineBuilder(Annotations.BaseBoltCircleCenterlineBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder
    Plane: Annotations.PlaneBuilder


class PmiBoltCircleCenterline(Annotations.BaseBoltCircleCenterline):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class PmiBaselineDimension(Annotations.BaselineDimension):
    def __init__(self) -> None: ...


class PmiBalloonNoteData(Annotations.PmiSemanticData):
    def __init__(self, ptr: int) -> None: ...
    def GetText(self) -> str:
        ...
    BalloonScale: float
    BalloonText: str
    Category: str
    Identifier: str
    Revision: str
    Title: str


class PmiAttributeValueUrlBuilder(Builder):
    def __init__(self) -> None: ...
    UrlValue: str


class PmiAttributeValueUrl(Annotations.PmiAttributeValue):
    def __init__(self) -> None: ...


class PmiAttributeValueStringBuilder(Builder):
    def __init__(self) -> None: ...
    StringValue: str


class PmiAttributeValueString(Annotations.PmiAttributeValue):
    def __init__(self) -> None: ...


class PmiAttributeValueNumberBuilder(Builder):
    def __init__(self) -> None: ...
    NumberValue: float


class PmiAttributeValueNumber(Annotations.PmiAttributeValue):
    def __init__(self) -> None: ...


class PmiAttributeValueMultipleStringBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMultipleStringValue(self) -> str:
        ...
    def SetMultipleStringValue(self, multipleStringValue: str) -> None:
        ...


class PmiAttributeValueMultipleString(Annotations.PmiAttributeValue):
    def __init__(self) -> None: ...


class PmiAttributeValueListBuilder(Builder):
    def __init__(self) -> None: ...
    ListValue: str


class PmiAttributeValueList(Annotations.PmiAttributeValue):
    def __init__(self) -> None: ...


class PmiAttributeValueIntegerBuilder(Builder):
    def __init__(self) -> None: ...
    IntegerValue: int


class PmiAttributeValueInteger(Annotations.PmiAttributeValue):
    def __init__(self) -> None: ...


class PmiAttributeValue(NXObject):
    def __init__(self) -> None: ...


class PmiAttributeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.PmiAttribute]:
        ...
    def __init__(self, owner: Annotations.PmiManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePmiAttributeBuilder(self, pmiAttr: Annotations.PmiAttribute) -> Annotations.PmiAttributeBuilder:
        ...
    def CreatePmiUserDefinedBuilder(self, userDefined: Annotations.PmiUserDefined) -> Annotations.PmiUserDefinedBuilder:
        ...
    def CreatePmiIntegerBuilder(self, pmiInteger: Annotations.PmiInteger) -> Annotations.PmiIntegerBuilder:
        ...
    def CreatePmiStringBuilder(self, pmiString: Annotations.PmiString) -> Annotations.PmiStringBuilder:
        ...
    def CreatePmiNumberBuilder(self, pmiNumber: Annotations.PmiNumber) -> Annotations.PmiNumberBuilder:
        ...
    def CreatePmiUrlNoteBuilder(self, pmiUrlNote: Annotations.PmiUrlNote) -> Annotations.PmiUrlNoteBuilder:
        ...
    def CreateGovernmentSecurityInformationBuilder(self, governmentSecurityInformation: Annotations.GovernmentSecurityInformation) -> Annotations.GovernmentSecurityInformationBuilder:
        ...
    def CreateCompanyProprietaryInformationBuilder(self, companyProprietaryInformation: Annotations.CompanyProprietaryInformation) -> Annotations.CompanyProprietaryInformationBuilder:
        ...
    def CreateGeneralNoteBuilder(self, generalNote: Annotations.GeneralNote) -> Annotations.GeneralNoteBuilder:
        ...
    def CreateSurfaceFinishBuilder(self, surfaceFinish: Annotations.SurfaceFinish) -> Annotations.SurfaceFinishBuilder:
        ...
    def CreateSpecificNoteBuilder(self, specificNote: Annotations.SpecificNote) -> Annotations.SpecificNoteBuilder:
        ...
    def CreateCoordinateNoteBuilder(self, coordinateNote: Annotations.CoordinateNote) -> Annotations.CoordinateNoteBuilder:
        ...
    def CreateEnterpriseIdentificationBuilder(self, enterpriseIdentification: Annotations.EnterpriseIdentification) -> Annotations.EnterpriseIdentificationBuilder:
        ...
    def CreatePartIdentificationBuilder(self, partIdentification: Annotations.PartIdentification) -> Annotations.PartIdentificationBuilder:
        ...
    def CreateProcessSpecificationBuilder(self, processSpecification: Annotations.ProcessSpecification) -> Annotations.ProcessSpecificationBuilder:
        ...
    def CreateMaterialSpecificationBuilder(self, materialSpecification: Annotations.MaterialSpecification) -> Annotations.MaterialSpecificationBuilder:
        ...
    def CreateLocatorDesignatorBuilder(self, locatorDesignator: Annotations.LocatorDesignator) -> Annotations.LocatorDesignatorBuilder:
        ...
    def CreateBalloonNoteBuilder(self, balloonNote: Annotations.BalloonNote) -> Annotations.BalloonNoteBuilder:
        ...
    def CreatePmiAttributeValueStringBuilder(self, pmiAttributeValueString: Annotations.PmiAttributeValueString) -> Annotations.PmiAttributeValueStringBuilder:
        ...
    def CreatePmiAttributeValueMultipleStringBuilder(self, pmiAttributeValueMultipleString: Annotations.PmiAttributeValueMultipleString) -> Annotations.PmiAttributeValueMultipleStringBuilder:
        ...
    def CreatePmiAttributeValueIntegerBuilder(self, pmiAttributeValueInteger: Annotations.PmiAttributeValueInteger) -> Annotations.PmiAttributeValueIntegerBuilder:
        ...
    def CreatePmiAttributeValueListBuilder(self, pmiAttributeValueList: Annotations.PmiAttributeValueList) -> Annotations.PmiAttributeValueListBuilder:
        ...
    def CreatePmiAttributeValueUrlBuilder(self, pmiAttributeValueUrl: Annotations.PmiAttributeValueUrl) -> Annotations.PmiAttributeValueUrlBuilder:
        ...
    def CreatePmiAttributeValueNumberBuilder(self, pmiAttributeValueNumber: Annotations.PmiAttributeValueNumber) -> Annotations.PmiAttributeValueNumberBuilder:
        ...
    def CreateExportControlBuilder(self, exportControl: Annotations.ExportControl) -> Annotations.ExportControlBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> TaggedObject:
        ...
    def Tag(self) -> Tag: ...



class PmiAttributeBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAttributeValues(self) -> typing.List[NXObject]:
        ...
    def SetAttributeValues(self, attributeValues: typing.List[NXObject]) -> None:
        ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder
    Attribute: Annotations.Pmi
    BusinessModifier: NXObject
    KnowledgeFusionClassName: str
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder


class PmiAttribute(Annotations.Annotation):
    def __init__(self) -> None: ...


class PmiArcLengthDimension(Annotations.BaseArcLengthDimension):
    def __init__(self) -> None: ...


class PmiAngularDimensionBuilder(Annotations.BaseAngularDimensionBuilder):
    def __init__(self) -> None: ...
    AssociatedObjects: Annotations.AssociatedObjectsBuilder
    AssociatedObjectsSets: Annotations.AssociatedObjectsSetsBuilder


class PmiAngularDimension(Annotations.BaseAngularDimension):
    def __init__(self) -> None: ...


class Pmi(NXObject):
    def __init__(self) -> None: ...
    def GetDisplayInstances(self) -> typing.List[Annotations.Annotation]:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    def GetDatumData(self) -> Annotations.PmiDatumData:
        ...
    def GetDimensionData(self) -> Annotations.PmiDimensionData:
        ...
    def GetFcfData(self) -> Annotations.PmiFcfData:
        ...
    def GetNoteData(self) -> Annotations.PmiNoteData:
        ...
    def GetLineWeldData(self) -> Annotations.PmiLineWeldData:
        ...
    def GetRegionData(self) -> Annotations.PmiRegionData:
        ...
    def GetProprietaryInfoData(self) -> Annotations.PmiProprietaryInfoData:
        ...
    def GetGovernmentSecurityInfoData(self) -> Annotations.PmiGovernmentSecurityInfoData:
        ...
    def GetExportControlData(self) -> Annotations.PmiExportControlData:
        ...
    def GetBalloonNoteData(self) -> Annotations.PmiBalloonNoteData:
        ...
    def GetMaterialSpecificationData(self) -> Annotations.PmiMaterialSpecificationData:
        ...
    def GetEnterpriseIdentifierData(self) -> Annotations.PmiEnterpriseIdentifierData:
        ...
    def GetProcessSpecificationData(self) -> Annotations.PmiProcessSpecificationData:
        ...
    def GetPartIdentificationData(self) -> Annotations.PmiPartIdentificationData:
        ...
    def GetLocatorDesignatorData(self) -> Annotations.PmiLocatorDesignatorData:
        ...
    def GetCoordinateNoteData(self) -> Annotations.PmiCoordinateNoteData:
        ...
    def GetSurfaceFinishData(self) -> Annotations.PmiSurfaceFinishData:
        ...
    def GetDatumTargetData(self) -> Annotations.PmiDatumTargetData:
        ...
    Type: Annotations.Pmi.PmiType
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


    class PmiType(enum.Enum):
        None = 0
        BalloonNote = 1
        Centerline = 2
        CoordinateNote = 3
        CustomSymbol = 4
        CuttingPlaneSymbol = 5
        Datum = 6
        DatumTarget = 7
        Dimension = 8
        EnterpriseIdentification = 9
        ExportControl = 10
        FeatureControlFrame = 11
        GovernmentSecurityInformation = 12
        LineWeld = 13
        LocatorDesignator = 14
        MaterialSpecification = 15
        Note = 16
        PartIdentification = 17
        ProcessSpecification = 18
        ProprietaryInformation = 19
        Region = 20
        SurfaceFinish = 21
        Table = 22
    

class PlistBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTemplateLocation(self, templateLocation: str) -> None:
        ...
    Balloons: Annotations.BalloonsBuilder
    Contents: Annotations.PartsListContentsBuilder
    Origin: Annotations.OriginBuilder
    Settings: Annotations.TableStyleBuilder


class PlaneBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    PlaneMethod: Annotations.PlaneBuilder.PlaneMethodType
    ProjectOntoPlane: bool
    UserDefinedPlane: Xform


    class PlaneMethodType(enum.Enum):
        XyPlane = 0
        XzPlane = 1
        YzPlane = 2
        ModelView = 3
        UserDefined = 4
    

class PinListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AutoUpdate: bool
    Filter: Annotations.PinListBuilder.FilterType
    FlattenHierarchy: bool


    class FilterType(enum.Enum):
        RoutedandUnroutedConnections = 0
        OnlyRoutedConnections = 1
        OnlyUnroutedConnections = 2
    

class PerpendicularDimension(Annotations.BasePerpendicularDimension):
    def __init__(self) -> None: ...


class PartSymbolFolderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.PartSymbolFolder]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePartSymbolFolderBuilder(self, currentFolder: Annotations.PartSymbolFolder) -> Annotations.PartSymbolFolderBuilder:
        ...
    def FindObject(self, name: str) -> Annotations.PartSymbolFolder:
        ...
    def Tag(self) -> Tag: ...



class PartSymbolFolderBuilder(Builder):
    def __init__(self) -> None: ...
    def GetFolderName(self) -> str:
        ...
    def SetFolderName(self, folderName: str) -> None:
        ...
    def GetCurrentFolder(self) -> Annotations.PartSymbolFolder:
        ...
    def GetParent(self) -> Annotations.PartSymbolFolder:
        ...
    def SetParent(self, parentfolder: Annotations.PartSymbolFolder) -> None:
        ...
    def GetRootFolder(self) -> Annotations.PartSymbolFolder:
        ...
    def IsRootFolder(self) -> bool:
        ...
    def GetChildren(self) -> typing.List[Annotations.PartSymbolFolder]:
        ...
    def GetFolderCount(self) -> int:
        ...
    def GetPartSymbolCount(self) -> int:
        ...
    def GetPartSymbols(self) -> typing.List[Annotations.MasterSymbol]:
        ...


class PartSymbolFolder(NXObject):
    def __init__(self) -> None: ...


class PartsListContentsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AddMember(self, member: TaggedObject, selectSubassemblies: bool) -> None:
        ...
    def RemoveMember(self, member: TaggedObject, removeSubassemblies: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Arrangement: Assemblies.ArrangementsBuilder
    IncludeSubOrdinateDesignElements: bool
    Scope: Annotations.PartsListContentsBuilder.ScopeType
    TopLevelAssembly: Annotations.PartsListContentsBuilder.TopLevelAssemblyType


    class TopLevelAssemblyType(enum.Enum):
        ChildPart = 1
        SubChildPart = 2
    

    class ScopeType(enum.Enum):
        AllLevels = 0
        TopLevelOnly = 1
        LeavesOnly = 2
    

class PartsListCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.PartsList]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePartsListBuilder(self, partsList: Annotations.Table) -> Annotations.PlistBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.PartsList:
        ...
    def Tag(self) -> Tag: ...



class PartsListBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AllowManualRows: bool
    AutomaticUpdate: bool
    CalloutSuffix: str
    CharToSkip: str
    CreateNewRowAsLocked: bool
    EnableCrossHighlighting: bool
    GrowDirectionOptions: Annotations.PartsListBuilder.PartsListGrowDirectionOptions
    HighlightColor: NXColor
    HighlightManualText: bool
    Increment: int
    InitialCallout: str
    LockPartsListSetup: bool
    MainSymbolCustomText: str
    MainSymbolText: Annotations.PartsListBuilder.PartsListMainSymbolText
    ReferenceSymbolCustomText: str
    ReferenceSymbolText: Annotations.PartsListBuilder.PartsListReferenceSymbolText
    ShowLockedDeletedRows: Annotations.PartsListBuilder.PartsListShowLockedDeletedRows
    ShowReferenceCalloutSuffix: bool
    SortOnUpdate: bool
    Symbol: Annotations.PartsListBuilder.PartsListSymbolType
    VerticalGroupAttachment: Annotations.PartsListBuilder.PartsListVerticalGroupLeaderAttachment


    class PartsListVerticalGroupLeaderAttachment(enum.Enum):
        Top = 0
        Bottom = 1
    

    class PartsListSymbolType(enum.Enum):
        None = 0
        Circle = 1
        DividedCircle = 2
        TrianglePointedDown = 3
        TrianglePointedUp = 4
        Square = 5
        DividedSquare = 6
        Hexagon = 7
        DividedHexagon = 8
        QuadrantCircle = 9
        RoundedBox = 10
        Underline = 11
        Label = 12
    

    class PartsListShowLockedDeletedRows(enum.Enum):
        Strikethrough = 0
        Blanked = 1
        Hidden = 2
        Ordinary = 3
    

    class PartsListReferenceSymbolText(enum.Enum):
        None = 0
        Callout = 1
        PartName = 2
        CalloutandQuantity = 3
        Custom = 4
    

    class PartsListMainSymbolText(enum.Enum):
        None = 0
        Callout = 1
        PartName = 2
        CalloutandQuantity = 3
        Custom = 4
    

    class PartsListGrowDirectionOptions(enum.Enum):
        Up = 0
        Down = 1
    

class PartsList(Annotations.Table):
    def __init__(self) -> None: ...
    def UpdateCalloutgroupForDeleteCallouts(self, calloutSymbols: typing.List[DisplayableObject]) -> None:
        ...
    def Update(self) -> None:
        ...
    def ShowBalloonsInView(self, viewTag: View) -> None:
        ...
    def AttachDetachRows(self, partsListRows: typing.List[DisplayableObject]) -> None:
        ...


class PartIdentificationBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    DescriptiveModifier: str
    ItemName: str
    ItemNameModifier: str
    PartIdentifier: str
    Revision: str
    Title: str


class PartIdentification(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class PartFamilyTableSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetColumnVisibility(self, columnIndex: int, columnVisibility: bool) -> None:
        ...
    def SetRowVisibility(self, rowIndex: int, rowVisibility: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AllowManualColumns: bool
    AllowManualRows: bool


class PartFamilyTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.PartFamilyTable]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePartFamilyTableBuilder(self, partFamilyTable: Annotations.Table) -> Annotations.PartFamilyTableBuilder:
        ...
    def Tag(self) -> Tag: ...



class PartFamilyTableBuilder(Builder):
    def __init__(self) -> None: ...
    def AssignTemplateName(self, templateName: str) -> None:
        ...
    Origin: Annotations.OriginBuilder
    SelectPartFamilyMember: Assemblies.SelectComponent
    Style: Annotations.TableStyleBuilder


class PartFamilyTable(Annotations.Table):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...
    def HideColumns(self, columns: typing.List[DisplayableObject]) -> None:
        ...
    def HideRows(self, rows: typing.List[DisplayableObject]) -> None:
        ...


class ParallelDimension(Annotations.BaseParallelDimension):
    def __init__(self) -> None: ...


class OriginUtils(Utilities.NXRemotableObject):
    def SetPmiOriginsRelativeToGeometry(self, part: Part) -> None:
        ...
    def __init__(self) -> None: ...


class OriginBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetAssociativeOrigin(self) -> Annotations.Annotation.AssociativeOriginData:
        ...
    def SetAssociativeOrigin(self, assocOrigin: Annotations.Annotation.AssociativeOriginData) -> None:
        ...
    def SetInferRelativeToGeometry(self, inferRelativeToGeometry: bool) -> None:
        ...
    def SetInferRelativeToGeometryFromLeader(self, inferFromLeader: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Anchor: Annotations.OriginBuilder.AlignmentPosition
    AnnotationView: Drawings.SelectDraftingView
    Origin: SelectDisplayableObject
    OriginPoint: Point3d
    Plane: Annotations.PlaneBuilder


    class AlignmentPosition(enum.Enum):
        TopLeft = 0
        TopCenter = 1
        TopRight = 2
        MidLeft = 3
        MidCenter = 4
        MidRight = 5
        BottomLeft = 6
        BottomCenter = 7
        BottomRight = 8
    

class OriginAlignmentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlignHorizontalVertical: bool
    AlignToDimensionLine: bool
    AutoAlignment: Annotations.OriginAlignmentBuilder.AutoAlignmentType
    PositionAtSnapPoint: bool
    PositionOnMargin: bool
    PositionRelativeToGeom: bool
    PositionRelativeToView: bool
    StackAnnotation: bool


    class AutoAlignmentType(enum.Enum):
        Associative = 0
        NonAssociative = 1
        Off = 2
    

class OrdinateStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlignSymbolWithBaseline: bool
    DisplayDimensionLine: Annotations.OrdinateLineArrowDisplayOption
    DisplayNameStyle: Annotations.OrdinateOriginDisplayOption
    DisplayZeroAtBaseline: bool
    DoglegAngle: float
    DoglegCreationOption: Annotations.OrdinateDoglegCreationOption
    DoglegEndOffset: float
    DoglegSetting: Annotations.OrdinateDoglegDefinition
    DoglegStartOffset: float
    MarginFirstOffset: float
    MarginSpacing: float
    NumberOfMargins: int
    OrdinateTextAngle: float
    OrdinateTextOrientation: Annotations.TextOrientation
    PositiveDirection: Annotations.OrdinatePositiveDirection
    SymbolAngle: float
    SymbolAspectRatio: float
    SymbolHeight: float
    SymbolLength: float
    SymbolScale: float
    UserDefinedText: str


class OrdinatePositiveDirection(enum.Enum):
    All = 0
    UpperRight = 1
    UpperLeft = 2
    LowerRight = 3
    LowerLeft = 4
    Last = 5


class OrdinateOriginDisplayOption(enum.Enum):
    UserDefinedSymbol = 0
    OrdinateSetName = 1
    NoText = 2
    Last = 3


class OrdinateOriginDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetOrdinateDimensions(self) -> typing.List[Annotations.OrdinateDimension]:
        ...


class OrdinateMarginCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.OrdinateMargin]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHorizontalMargin(self, ordinateOrigin: Annotations.OrdinateOriginDimension, associativity: Annotations.Associativity, offsetDistance: float) -> Annotations.HorizontalOrdinateMargin:
        ...
    def CreateVerticalMargin(self, ordinateOrigin: Annotations.OrdinateOriginDimension, associativity: Annotations.Associativity, offsetDistance: float) -> Annotations.VerticalOrdinateMargin:
        ...
    def AddMargin(self, ordinateOrigin: Annotations.OrdinateOriginDimension, editMargin: Annotations.OrdinateMargin, offsetDistance: float) -> Annotations.OrdinateMargin:
        ...
    def CreateInferredMargin(self, ordinateOrigin: Annotations.OrdinateOriginDimension, origin: Point3d, subtype: int) -> Annotations.OrdinateMargin:
        ...
    def Tag(self) -> Tag: ...



class OrdinateMargin(NXObject):
    def __init__(self) -> None: ...
    def DeleteMargin(self, ordinateOrigin: Annotations.OrdinateOriginDimension) -> None:
        ...
    def MoveMargin(self, offset: float) -> None:
        ...
    def RedefineMargin(self, ordinateOrigin: Annotations.OrdinateOriginDimension, associativity: Annotations.Associativity) -> None:
        ...


class OrdinateLineArrowDisplayOption(enum.Enum):
    None = 0
    All = 1
    Last = 2


class OrdinateDoglegDefinition(enum.Enum):
    StartAndEnd = 0
    StartAngle = 1
    EndAngle = 2
    Last = 3


class OrdinateDoglegCreationOption(enum.Enum):
    Infer = 0
    Yes = 1
    No = 2
    Last = 3


class OrdinateDimensionPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AlignSymbolWithBaseline: bool
    DisplayZeroAtBaseline: bool
    DoglegAngle: float
    DoglegCreationOption: Annotations.OrdinateDoglegCreationOption
    DoglegDefinition: Annotations.OrdinateDoglegDefinition
    DoglegEndOffset: float
    DoglegStartOffset: float
    FirstMarginOffset: float
    LineArrowDisplayOption: Annotations.OrdinateLineArrowDisplayOption
    MarginSpacing: float
    NumberOfMargins: float
    OriginDisplay: Annotations.OrdinateOriginDisplayOption
    PositiveDirection: Annotations.OrdinatePositiveDirection
    SymbolAngle: float
    SymbolAspectRatio: float
    SymbolHeight: float
    SymbolLength: float
    SymbolScale: float
    TextOrientation: Annotations.TextOrientation
    TextOrientationAngle: float
    UserDefinedText: str


class OrdinateDimensionBuilder(Annotations.BaseOrdinateDimensionBuilder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class OrdinateDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetDoglegData(self) -> Annotations.OrdinateDimension.DoglegPreferences:
        ...
    def SetDoglegData(self, ordinateDoglegPreferences: Annotations.OrdinateDimension.DoglegPreferences) -> None:
        ...
    def GetOrdinateOrigin(self) -> Annotations.OrdinateOriginDimension:
        ...
    def NavigateToOrigin(self) -> None:
        ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...


    class OrdinateDimensionDoglegPreferences():
        DoglegSetting: Annotations.OrdinateDoglegDefinition
        Angle: float
        StartOffset: float
        EndOffset: float
        DoglegOption: Annotations.OrdinateDoglegCreationOption
        def ToString(self) -> str:
            ...
    

class OrdinateBaselineBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ActivateBaseline: bool
    ActivatePerpendicular: bool
    BaselineVector: Direction
    IsBaselineDirectionReversed: bool
    IsPerpendicularBaselineDirectionReversed: bool


class OffsetCenterPointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.OffsetCenterPoint]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateOffsetCenterPointBuilder(self, centerPoint: Annotations.OffsetCenterPoint) -> Annotations.OffsetCenterPointBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.OffsetCenterPoint:
        ...
    def Tag(self) -> Tag: ...



class OffsetCenterPointBuilder(Annotations.BaseSymbolBuilder):
    def __init__(self) -> None: ...
    CenterCross: float
    Color: NXColor
    DisplayStyle: Annotations.OffsetCenterPointBuilder.Display
    Distance: float
    Extension: float
    Gap: float
    Inherit: SelectNXObject
    Location: SelectNXObject
    OffsetMethod: Annotations.OffsetCenterPointBuilder.Offset
    OffsetPosition: Point3d
    Width: Annotations.OffsetCenterPointBuilder.Thickness


    class Thickness(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 6
        Two = 7
        Three = 8
        Four = 9
        Five = 10
        Six = 11
        Seven = 12
        Eight = 13
        Nine = 14
    

    class Offset(enum.Enum):
        HorizontalDistanceFromArc = 0
        HorizontalDistanceFromCenter = 1
        HorizontalDistanceByPosition = 2
        VerticalDistanceFromArc = 3
        VerticalDistanceFromCenter = 4
        VerticalDistanceByPosition = 5
    

    class Display(enum.Enum):
        CenterPoint = 0
        CenterLine = 1
        CenterLineWithExtension = 2
    

class OffsetCenterPoint(Annotations.DraftingAid):
    def __init__(self) -> None: ...


class NoteData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetText(self) -> str:
        ...
    def SetText(self, lines: str) -> None:
        ...
    def GetSimpleDraftingAidPreferences(self) -> Annotations.SimpleDraftingAidPreferences:
        ...
    def SetSimpleDraftingAidPreferences(self, preferences: Annotations.SimpleDraftingAidPreferences) -> None:
        ...


class NoteCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.BaseNote]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def NewNoteData(self) -> Annotations.NoteData:
        ...
    def CreatePmiNote(self, noteData: Annotations.NoteData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiNote:
        ...
    def Tag(self) -> Tag: ...



class NoteBase(Annotations.SimpleDraftingAid):
    def __init__(self) -> None: ...


class Note(Annotations.BaseNote):
    def __init__(self) -> None: ...


class NarrowTextOrientation(enum.Enum):
    Horizontal = 0
    Parallel = 1
    Last = 2


class NarrowDisplayOption(enum.Enum):
    None = 0
    NoLeader = 1
    WithLeaderNoStub = 2
    AboveStub = 3
    AfterStub = 4
    Last = 5


class NarrowDimensionPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DimensionArrowheadType: Annotations.ArrowheadType
    DimensionDisplayOption: Annotations.NarrowDisplayOption
    DimensionLeaderAngle: float
    DimensionTextOffset: float
    DimensionTextOrientation: Annotations.NarrowTextOrientation


class NarrowDimensionData():
    DisplayType: Annotations.NarrowDisplayOption
    TextOrientation: Annotations.NarrowTextOrientation
    LeaderAngle: float
    TextOffset: float
    def ToString(self) -> str:
        ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MinorAngularDimensionBuilder(Annotations.AngularDimensionBuilder):
    def __init__(self) -> None: ...


class MinorAngularDimension(Annotations.AngularDimension):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class MaterialSpecificationBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetMaterialProperties(self) -> str:
        ...
    def SetMaterialProperties(self, materialProperties: str) -> None:
        ...
    def GetNomenclature(self) -> str:
        ...
    def SetNomenclature(self, nomenclature: str) -> None:
        ...
    def GetOpenField(self) -> str:
        ...
    def SetOpenField(self, openField: str) -> None:
        ...
    AvailableMaterial: str
    Category: str
    MaterialType: str
    Revision: str
    Title: str


class MaterialSpecification(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class MaterialConditionModifier(enum.Enum):
    Mmc = 0
    Lmc = 1
    Rfs = 2
    Tangential = 3
    None = 4
    Last = 5


class MasterSymbolListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.MasterSymbolListItemBuilder]) -> None:
        ...
    def Append(self, object: Annotations.MasterSymbolListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.MasterSymbolListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.MasterSymbolListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.MasterSymbolListItemBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.MasterSymbolListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.MasterSymbolListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.MasterSymbolListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.MasterSymbolListItemBuilder, object2: Annotations.MasterSymbolListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.MasterSymbolListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class MasterSymbolListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetMultilineString(self) -> str:
        ...
    def SetMultilineString(self, multilineString: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    DoubleDefault: float
    DoubleMax: float
    DoubleMin: float
    IntegerDefault: int
    IntegerMax: int
    IntegerMin: int
    NoteText: str
    NoteTitle: str
    Rule: str
    TextType: Annotations.MasterSymbolListItemBuilder.TextTypes


    class TextTypes(enum.Enum):
        Mandatory = 0
        Arbitrary = 1
        Controlled = 2
        PartiallyControlled = 3
        Integer = 4
        Real = 5
        Rule = 6
    

class MasterSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateNewListItem(self, noteTag: Annotations.Annotation, notes: str) -> Annotations.MasterSymbolListItemBuilder:
        ...
    def GenerateItemNumber(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.MasterSymbolBuilder.ItemNumber instead.")"""
        ...
    def GenerateRevision(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.MasterSymbolBuilder.Revision instead.")"""
        ...
    def GetLeaderAttachmentPoint(self, attachmentType: Annotations.MasterSymbolBuilder.LeaderAttachmentType) -> Point:
        ...
    def SetLeaderAttachmentPoint(self, attachmentType: Annotations.MasterSymbolBuilder.LeaderAttachmentType, leaderAttachmentPoint: Point) -> None:
        ...
    def GetMultilineString(self) -> str:
        ...
    def SetPath(self, path: str) -> None:
        ...
    def SetIsPartSymbol(self, isPartSymbol: bool) -> None:
        ...
    def Rename(self, currentSymbolTag: Annotations.MasterSymbol, newSymbolName: str) -> None:
        ...
    def EditImage(self, currentSymbolTag: Annotations.MasterSymbol, newImageName: str) -> None:
        ...
    def SetPartOperationCreateBuilder(self, partOperationBuilder: PDM.PartOperationCreateBuilder) -> None:
        ...
    def GetPartOperationCreateBuilder(self) -> PDM.PartOperationCreateBuilder:
        ...
    AnchorPoint: Point
    Contents: SelectNXObjectList
    ImageCapture: Gateway.ImageCaptureBuilder
    ImageName: str
    ItemName: str
    ItemNumber: str
    NoteList: NXObjectList
    PartFileName: str
    Revision: str
    SymbolName: str


    class LeaderAttachmentType(enum.Enum):
        Left = 0
        Right = 1
    

class MasterSymbol(NXObject):
    def __init__(self) -> None: ...


class MasterCustomSymbolData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolBuilder instead.")"""
        ...
    def SetGeometry(self, geom: typing.List[DisplayableObject]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolBuilder instead.")"""
        ...
    def GetPath(self) -> str:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolBuilder instead.")"""
        ...
    def SetPath(self, path: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolBuilder instead.")"""
        ...
    Anchor: Point
    PartName: str
    SymbolName: str


class MasterCustomSymbol(TaggedObject):
    def __init__(self) -> None: ...


class MajorAngularDimensionBuilder(Annotations.AngularDimensionBuilder):
    def __init__(self) -> None: ...


class MajorAngularDimension(Annotations.AngularDimension):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class LocatorDesignatorBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    CoordinatePlane: str
    HotSpot: Point
    HotSpotText: str
    LocatorLetter: str
    LocatorType: str
    NormalDirection: Direction
    NoteText: str
    PinDirection: Direction
    PunchDirection: Direction
    Subscript: str
    Title: str


class LocatorDesignator(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class ListBusinessModifier(Annotations.BusinessModifier):
    def __init__(self) -> None: ...
    def GetList(self) -> str:
        ...
    CurrentItemIndex: int


class LineWidth(enum.Enum):
    Normal = 1
    Thick = 2
    Thin = 3
    One = 6
    Two = 7
    Three = 8
    Four = 9
    Five = 10
    Six = 11
    Seven = 12
    Eight = 13
    Nine = 14


class LineWeldSideData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DepthRootOpeningNumberOfWelds: str
    FinishMethod: Annotations.FinishMethod
    GrooveAngle: str
    LengthPitch: str
    Size: str
    SizeLetterCode: Annotations.SizeLetterCode
    SupplementarySymbol: Annotations.SupplementarySymbol
    Symbol: Annotations.Symbol


class LineWeldDataBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CompoundWeldSize: str
    CompoundWeldSizeCode: Annotations.LineWeldDataBuilder.WeldSizeCodeType
    ContourSymbol: Annotations.LineWeldDataBuilder.ContourSymbolType
    FinishSymbol: Annotations.LineWeldDataBuilder.FinishSymbolType
    GrooveCountersinkAngle: str
    IsCompound: bool
    LengthPitch: str
    NumberRootDepth: str
    WeldSize: str
    WeldSizeCode: Annotations.LineWeldDataBuilder.WeldSizeCodeType
    WeldSymbol: Annotations.LineWeldDataBuilder.WeldSymbolType


    class WeldSymbolType(enum.Enum):
        None = 0
        ButtWeldWithRaisedEdges = 1
        SingleFlange = 2
        SquareButt = 3
        VButt = 4
        VButtWithBroadRootFace = 5
        BevelButt = 6
        BevelButtWithBroadRootFace = 7
        UButt = 8
        JButt = 9
        FlareV = 10
        FlareBevel = 11
        KGroove = 12
        Fillet = 13
        Stake = 14
        PlugSlot = 15
        Edge = 16
        Edge2 = 17
        Spot = 18
        Spot2 = 19
        Seam = 20
        Seam2 = 21
        SteepFlankedVButt = 22
        SteepFlankedBevelButt = 23
        Backing = 24
        SurfaceJoint = 25
        SolderedJoint = 26
        InclinedJoint = 27
        FoldJoint = 28
        Stud = 29
        Surfacing = 30
        Intermittent = 31
        BackingPlate = 32
        NotSpecified = 33
    

    class WeldSizeCodeType(enum.Enum):
        None = 0
        A = 1
        C = 2
        D = 3
        S = 4
        Z = 5
        P = 6
    

    class FinishSymbolType(enum.Enum):
        None = 0
        Chipping = 1
        Grinding = 2
        Hammering = 3
        Machining = 4
        Rolling = 5
        Peening = 6
    

    class ContourSymbolType(enum.Enum):
        None = 0
        Convex = 1
        Flat = 2
        Concave = 3
        BlendedToesIsoAndDinOnly = 4
        BackingStripPermanentIsoAndDinOnly = 5
        BackingStripRemovableIsoAndDinOnly = 6
        MeltThrough = 7
        Flush = 8
        MachiningGradedJunction = 9
    

class LineWeldData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetWeldStandard(self, standard: Annotations.WeldStandard) -> None:
        ...
    def GetArrowSideData(self) -> Annotations.LineWeldSideData:
        ...
    def SetArrowSideData(self, arrowSide: Annotations.LineWeldSideData) -> None:
        ...
    def GetOtherSideData(self) -> Annotations.LineWeldSideData:
        ...
    def SetOtherSideData(self, otherSide: Annotations.LineWeldSideData) -> None:
        ...
    def GetTailSpecificationText(self) -> str:
        ...
    def SetTailSpecificationText(self, lines: str) -> None:
        ...
    def GetTopSeamObjects(self) -> typing.List[DisplayableObject]:
        ...
    def SetTopSeamObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def GetSideSeamObjects(self) -> typing.List[DisplayableObject]:
        ...
    def SetSideSeamObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    AllroundSymbol: bool
    CenterSymbol: bool
    FieldWeld: bool
    IdentificationLineLocation: Annotations.IdentificationLineLocation
    SideSeamDisplay: bool
    SideSeamHorizontalFlip: bool
    SideSeamVerticalFlip: bool
    SideSeamView: Drawings.DraftingView
    StaggeredWeldSymbolDisplay: bool
    SymbolScale: float
    Tail: Annotations.Tail
    TopSeamDisplay: bool
    TopSeamReverse: bool
    TopSeamView: Drawings.DraftingView
    WeldStandard: Annotations.WeldStandard


class LineWeldBuilder(Builder):
    def __init__(self) -> None: ...
    def GetReference(self) -> str:
        ...
    def SetReference(self, reference: str) -> None:
        ...
    def InheritProperties(self, annotation: Annotations.Weld) -> None:
        ...
    def InheritPropertiesFromWeldFeature(self, feature: DisplayableObject) -> None:
        ...
    ArrowSideWeldData: Annotations.LineWeldDataBuilder
    FieldWeld: Annotations.LineWeldBuilder.FieldWeldType
    FlipDirection: bool
    FlipHorizontal: bool
    FlipVertical: bool
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder
    IdLine: Annotations.LineWeldBuilder.IdLineType
    Inherit: SelectDisplayableObject
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder
    OtherSideWeldData: Annotations.LineWeldDataBuilder
    Scale: float
    SideSeamObjects: SelectDisplayableObjectList
    SpaceFactor: float
    StaggeredWeld: Annotations.LineWeldBuilder.StaggeredWeldType
    Style: Annotations.StyleBuilder
    Tail: Annotations.LineWeldBuilder.TailType
    TopSeamObject: SelectDisplayableObject
    WeldAlongContour: Annotations.LineWeldBuilder.WeldSymbolWeldAlongContourType


    class WeldSymbolWeldAlongContourType(enum.Enum):
        None = 0
        Closed = 1
        Unclosed = 2
        TrilateralWeld = 3
        AllAround = 4
    

    class TailType(enum.Enum):
        NoTail = 0
        Tail = 1
        Box = 2
    

    class StaggeredWeldType(enum.Enum):
        NoStaggeredSymbol = 0
        StaggeredSymbol = 1
        StaggeredSymbolWeldSide = 2
    

    class IdLineType(enum.Enum):
        Plain = 0
        IdLineAbove = 1
        IdLineBelow = 2
        CenteredSpotWeld = 3
        CenteredSeamWeld = 4
        Centered = 5
    

    class FieldWeldType(enum.Enum):
        Plain = 0
        TopField = 1
        TopFieldSimpleFlag = 2
    

class LineWeld(Annotations.Weld):
    def __init__(self) -> None: ...
    def GetWeldData(self) -> Annotations.LineWeldData:
        ...
    def SetWeldData(self, data: Annotations.LineWeldData) -> None:
        ...
    def SetAutoWeldSymbol(self, isAutoWeldSymbol: bool) -> None:
        ...
    def SetEditAuto(self, isEditAuto: bool) -> None:
        ...
    def SetAutoWeldType(self, type: Annotations.LineWeld.AutoWeldType, flag: bool) -> None:
        ...


    class AutoWeldType(enum.Enum):
        OtherSideGrooveCountersinkAngle = 0
        ArrowSideGrooveCountersinkAngle = 1
        OtherSideNumberRootDepth = 2
        ArrowSideNumberRootDepth = 3
        OtherSideWeldSize = 4
        ArrowSideWeldSize = 5
        OtherSideCompoundWeldSize = 6
        ArrowSideCompoundWeldSize = 7
        OtherSideLengthPitch = 8
        ArrowSideLengthPitch = 9
        OtherSideWeldSizeCode = 10
        ArrowSideWeldSizeCode = 11
        OtherSideCompoundWeldSizeCode = 12
        ArrowSideCompoundWeldSizeCode = 13
        FieldWeldType = 14
    

class LineTarget(Annotations.DatumTarget):
    def __init__(self) -> None: ...
    EndPointCoordinates: Point3d
    StartPointCoordinates: Point3d


class LineComponent(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    EndPoint: Point3d
    Index: int
    StartPoint: Point3d
    Type: Annotations.LineComponent.LineType


    class LineType(enum.Enum):
        Extension = 0
        Leader = 1
        NarrowLeader = 2
        Stub = 3
        DualBracket = 4
        Annotation = 5
        Inspection = 6
        SecondaryExtension = 7
        Tolerance = 8
        Jog = 9
    

class LineCfw():
    Color: int
    Font: DisplayableObject.ObjectFont
    Width: Annotations.LineWidth
    def ToString(self) -> str:
        ...
    def __init__(self, Color: int, Font: DisplayableObject.ObjectFont, Width: Annotations.LineWidth) -> None: ...


class LinearTolerance(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetUpperToleranceInches(self) -> Annotations.Value:
        ...
    def SetUpperToleranceInches(self, upperToleranceInches: Annotations.Value) -> None:
        ...
    def GetLowerToleranceInches(self) -> Annotations.Value:
        ...
    def SetLowerToleranceInches(self, lowerToleranceInches: Annotations.Value) -> None:
        ...
    def GetUpperToleranceMm(self) -> Annotations.Value:
        ...
    def SetUpperToleranceMm(self, upperToleranceMm: Annotations.Value) -> None:
        ...
    def GetLowerToleranceMm(self) -> Annotations.Value:
        ...
    def SetLowerToleranceMm(self, lowerToleranceMm: Annotations.Value) -> None:
        ...
    DualDimensionDecimalPlaces: int
    DualToleranceDecimalPlaces: int
    LimitFitAnsiHoleType: Annotations.FitAnsiHoleType
    LimitFitDeviation: str
    LimitFitDisplayStyle: Annotations.FitDisplayStyle
    LimitFitGrade: int
    PrimaryDimensionDecimalPlaces: int
    ToleranceType: Annotations.ToleranceType
    ZeroToleranceDisplayStyle: Annotations.ZeroToleranceDisplayStyle


class LineArrowStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AllAroundSymbolSize: float
    ArrowheadIncludedAngle: float
    ArrowheadLength: float
    BalloonLeaderArrowHeadType: Annotations.ArrowheadType
    ClipOrdinateDimensionLine: bool
    DatumLengthPastArrow: float
    DotArrowheadDiameter: float
    FirstArrowLineColor: NXColor
    FirstArrowLineFont: DisplayableObject.ObjectFont
    FirstArrowLineWidth: Annotations.LineWidth
    FirstArrowType: Annotations.ArrowheadType
    FirstArrowheadColor: NXColor
    FirstArrowheadFont: DisplayableObject.ObjectFont
    FirstArrowheadWidth: Annotations.LineWidth
    FirstExtensionLineColor: NXColor
    FirstExtensionLineFont: DisplayableObject.ObjectFont
    FirstExtensionLineWidth: Annotations.LineWidth
    FirstJogAngle: float
    FirstJogDisplay: bool
    FirstJogEndOffset: float
    FirstJogOrientation: Annotations.JogOrientation
    FirstJogStartOffset: float
    FirstPosToExtensionLineDistance: float
    LeaderLocation: Annotations.VerticalTextJustification
    LeaderOrientation: Annotations.LeaderSide
    LinePastArrowDistance: float
    LinePastArrowDistance2: float
    ObliqueExtensionLineAngle: float
    SecondArrowLineColor: NXColor
    SecondArrowLineFont: DisplayableObject.ObjectFont
    SecondArrowLineWidth: Annotations.LineWidth
    SecondArrowType: Annotations.ArrowheadType
    SecondArrowheadColor: NXColor
    SecondArrowheadFont: DisplayableObject.ObjectFont
    SecondArrowheadWidth: Annotations.LineWidth
    SecondExtensionLineColor: NXColor
    SecondExtensionLineFont: DisplayableObject.ObjectFont
    SecondExtensionLineWidth: Annotations.LineWidth
    SecondJogAngle: float
    SecondJogDisplay: bool
    SecondJogEndOffset: float
    SecondJogOrientation: Annotations.JogOrientation
    SecondJogStartOffset: float
    SecondPosToExtensionLineDistance: float
    StubLength: float
    StubSymbolType: Annotations.StubSymbolType
    TextOverLeaderGapFactor: float
    TextOverStubFactor: float
    TextToLineDistance: float


class LinearDimensionBuilder(Annotations.BaseLinearDimensionBuilder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class LineAndArrowPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFirstExtensionLineCfw(self) -> Annotations.LineCfw:
        ...
    def SetFirstExtensionLineCfw(self, firstExtensionLineCfw: Annotations.LineCfw) -> None:
        ...
    def GetFirstArrowheadCfw(self) -> Annotations.LineCfw:
        ...
    def SetFirstArrowheadCfw(self, firstArrowheadCfw: Annotations.LineCfw) -> None:
        ...
    def GetFirstArrowLineCfw(self) -> Annotations.LineCfw:
        ...
    def SetFirstArrowLineCfw(self, firstArrowLineCfw: Annotations.LineCfw) -> None:
        ...
    def GetSecondExtensionLineCfw(self) -> Annotations.LineCfw:
        ...
    def SetSecondExtensionLineCfw(self, secondExtensionLineCfw: Annotations.LineCfw) -> None:
        ...
    def GetSecondArrowheadCfw(self) -> Annotations.LineCfw:
        ...
    def SetSecondArrowheadCfw(self, secondArrowheadCfw: Annotations.LineCfw) -> None:
        ...
    def GetSecondArrowLineCfw(self) -> Annotations.LineCfw:
        ...
    def SetSecondArrowLineCfw(self, secondArrowLineCfw: Annotations.LineCfw) -> None:
        ...
    AllAroundSymbol: float
    ArrowheadIncludedAngle: float
    ArrowheadLength: float
    ClipOrdinateDimensionLine: bool
    DatumLengthPastArrow: float
    DotArrowheadDiameter: float
    FirstArrowType: Annotations.ArrowheadType
    FirstPosToExtLineDist: float
    LeaderLocation: Annotations.VerticalTextJustification
    LinePastArrowDistance: float
    LinePastArrowDistance2: float
    ObliqueExtensionLineAngle: float
    SecondArrowType: Annotations.ArrowheadType
    SecondPosToExtLineDist: float
    StubLength: float
    TextOverLeaderGapFactor: float
    TextOverStubSpaceFactor: float
    TextToLineDistance: float


class LightweightSectionView(ModelingView):
    def __init__(self) -> None: ...
    def GetSectionCurvesVisibility(self) -> bool:
        ...
    def SetSectionCurvesVisibility(self, optionHideShow: bool) -> None:
        ...


class LightweightSectionBuilder(Display.DynamicSectionBuilder):
    def __init__(self) -> None: ...
    def GetSectionCurves(self, curves: typing.List[Curve]) -> None:
        ...
    AssemblyCrosshatching: bool
    BoundingBoxComponents: SelectDisplayableObjectList
    ClipCoplanarObjects: bool
    ClipWireframeObjects: bool
    CrosshatchSettings: Annotations.HatchFillSettingsBuilder
    CuttingPlaneSymbol: Annotations.CuttingPlaneSymbolBuilder
    DisplayCrosshatch: bool
    ObjectsToSection: SelectDisplayableObjectList
    PatternDefinedBy: int
    RestrictCrosshatch: bool
    SaveAssociativeCurves: bool
    Settings: Annotations.PmiSectionViewSettingsBuilder
    ToleranceCrosshatch: float
    ViewName: str


class LightweightSection(Display.DynamicSection):
    def __init__(self) -> None: ...


class LetteringStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlignPosition: Annotations.AlignmentPosition
    Angle: float
    AppendedNxTextCharacterSpaceFactor: float
    AppendedStandardTextCharacterSpaceFactor: float
    AppendedTextAspectRatio: float
    AppendedTextCharSpaceFactor: float
    AppendedTextColor: NXColor
    AppendedTextFont: int
    AppendedTextItalicized: bool
    AppendedTextLineSpaceFactor: float
    AppendedTextLineWidth: Annotations.LineWidth
    AppendedTextSize: float
    AppendedTextSpaceFactor: float
    AppendedTextSymbolAspectRatio: float
    DimLineSpaceFactor: float
    DimensionNxTextCharacterSpaceFactor: float
    DimensionStandardTextCharacterSpaceFactor: float
    DimensionTextAspectRatio: float
    DimensionTextCharSpaceFactor: float
    DimensionTextColor: NXColor
    DimensionTextFont: int
    DimensionTextItalicized: bool
    DimensionTextLineSpaceFactor: float
    DimensionTextLineWidth: Annotations.LineWidth
    DimensionTextSize: float
    DimensionTextSymbolAspectRatio: float
    GdtFrameHeightFactor: float
    GeneralNxTextCharacterSpaceFactor: float
    GeneralStandardTextCharacterSpaceFactor: float
    GeneralTextAspectRatio: float
    GeneralTextCharSpaceFactor: float
    GeneralTextColor: NXColor
    GeneralTextFont: int
    GeneralTextItalicized: bool
    GeneralTextLineSpaceFactor: float
    GeneralTextLineWidth: Annotations.LineWidth
    GeneralTextSize: float
    GeneralTextSymbolAspectRatio: float
    HorizontalTextJustification: Annotations.TextJustification
    StackAboveSpaceFactor: float
    StackAutospace: bool
    StackBelowSpaceFactor: float
    StackHorizontalAlignment: Annotations.StackHorizontalAlignment
    StackInheritAssociatedObjects: bool
    StackLeftSpaceFactor: float
    StackRightSpaceFactor: float
    StackVerticalAlignment: Annotations.StackVerticalAlignment
    SymbolFontFile: str
    ToleranceNxTextCharacterSpaceFactor: float
    ToleranceStandardTextCharacterSpaceFactor: float
    ToleranceTextAspectRatio: float
    ToleranceTextCharSpaceFactor: float
    ToleranceTextColor: NXColor
    ToleranceTextFont: int
    ToleranceTextItalicized: bool
    ToleranceTextLineSpaceFactor: float
    ToleranceTextLineWidth: Annotations.LineWidth
    ToleranceTextSize: float
    ToleranceTextSpaceFactor: float
    ToleranceTextSymbolAspectRatio: float
    TwoLineToleranceTextSize: float


class LetteringPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetDimensionText(self) -> Annotations.Lettering:
        ...
    def SetDimensionText(self, dimensionText: Annotations.Lettering) -> None:
        ...
    def GetAppendedText(self) -> Annotations.Lettering:
        ...
    def SetAppendedText(self, appendedText: Annotations.Lettering) -> None:
        ...
    def GetToleranceText(self) -> Annotations.Lettering:
        ...
    def SetToleranceText(self, toleranceText: Annotations.Lettering) -> None:
        ...
    def GetGeneralText(self) -> Annotations.Lettering:
        ...
    def SetGeneralText(self, generalText: Annotations.Lettering) -> None:
        ...
    AlignmentPosition: Annotations.AlignmentPosition
    Angle: float
    DimAppendedTextSpaceFactor: float
    DimDimLineSpaceFactor: float
    DimToleranceTextSpaceFactor: float
    GdtFrameHeightFactor: float
    HorizTextJust: Annotations.TextJustification
    StackAboveSpaceFactor: float
    StackAutospace: bool
    StackBelowSpaceFactor: float
    StackHorizontalAlignment: Annotations.StackHorizontalAlignment
    StackInheritAssociatedObjects: bool
    StackLeftSpaceFactor: float
    StackRightSpaceFactor: float
    StackVerticalAlignment: Annotations.StackVerticalAlignment


class Lettering():
    Size: float
    CharacterSpaceFactor: float
    AspectRatio: float
    LineSpaceFactor: float
    Cfw: Annotations.TextCfw
    Italic: bool
    SymbolAspectRatio: float
    def ToString(self) -> str:
        ...


class LeaderVerticalAttachment(enum.Enum):
    Null = -1
    Top = 0
    Center = 1
    Bottom = 2
    Legacy = 3
    Last = 4


class LeaderType(enum.Enum):
    Null = -1
    Plain = 0
    Around = 1
    PlainAligned = 2
    AroundAligned = 3
    Extension = 4
    DatumArrow = 5
    DatumExt = 6
    DatumDim = 7
    GbDatumArrow = 8
    GbDatumExt = 9
    GbDatumDim = 10
    OnAnnotation = 11
    OnStub = 12
    PlainNostub = 13
    AlignedNostub = 14
    OnCenterline = 15
    DatumOnDotTerminatedLeader = 16
    IdExtension = 17
    LinearExtension = 18
    LinearIdExtension = 19
    AllOver = 20
    Last = 21


class LeaderSide(enum.Enum):
    Null = -1
    Left = 0
    Right = 1
    Inferred = 2
    Last = 3


class LeaderOrientation(enum.Enum):
    FromLeft = 1
    FromRight = 2
    FromTop = 3
    FromBottom = 4
    Inferred = 5


class LeaderDataList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.LeaderData]) -> None:
        ...
    def Append(self, object: Annotations.LeaderData) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.LeaderData) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.LeaderData:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.LeaderData) -> None:
        ...
    def Erase(self, obj: Annotations.LeaderData, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.LeaderData]:
        ...
    def SetContents(self, objects: typing.List[Annotations.LeaderData]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.LeaderData, object2: Annotations.LeaderData) -> None:
        ...
    def Insert(self, location: int, object: Annotations.LeaderData) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class LeaderData(TaggedObject):
    def __init__(self) -> None: ...
    def HasStub(self) -> bool:
        ...
    def GetStubStartPoint(self) -> Point3d:
        ...
    def GetStubEndPoint(self) -> Point3d:
        ...
    def Validate(self) -> bool:
        ...
    Arrowhead: Annotations.LeaderData.ArrowheadType
    DatumOnDotTerminatedArrowhead: Annotations.LeaderData.ArrowheadType
    DatumOnDotTerminatedEndPoint: Point3d
    DatumOnDotTerminatedStartPoint: Point3d
    Jogs: SelectDisplayableObjectList
    Leader: SelectDisplayableObject
    LeaderPerpendicular: bool
    Perpendicular: bool
    StubSide: Annotations.LeaderSide
    StubSize: float
    TerminatorType: Annotations.LeaderData.LeaderType
    VerticalAttachment: Annotations.LeaderVerticalAttachment


    class LeaderType(enum.Enum):
        Plain = 0
        AllAround = 1
        PlainWithoutStub = 2
        Flag = 3
        Datum = 4
        DotTerminated = 5
        Extension = 6
        AllOver = 7
    

    class ArrowheadType(enum.Enum):
        ClosedArrow = 0
        ClosedSolidArrow = 1
        OpenArrow = 2
        FilledArrow = 3
        ClosedDoubleArrow = 4
        ClosedDoubleSolidArrow = 5
        OpenDoubleArrow = 6
        FilledDoubleArrow = 7
        None = 8
        Origin = 9
        Cross = 10
        Integral = 11
        Dot = 12
        FilledDot = 13
        Square = 14
        FilledSquare = 15
        Datum = 16
        FilledDatum = 17
        TopOpenArrow = 18
        BottomOpenArrow = 19
        TopFilledArrow = 20
        BottomFilledArrow = 21
    

class LeaderBundle(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetLeaderData(self, n: int, attachmentType: Annotations.LeaderAttachment, attachmentObject: NXObject, attachmentView: View, endPoint: Point3d, angle: float, intermediatePoints: typing.List[Point3d]) -> None:
        ...
    LeaderAlignment: Annotations.LeaderAlignment
    LeaderSide: Annotations.LeaderSide
    LeaderType: Annotations.LeaderType
    NumberOfLeaders: int


class LeaderBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Leaders: Annotations.LeaderDataList


class LeaderAttachment(enum.Enum):
    Null = -1
    OnObject = 0
    Screen = 1
    Last = 2


class LeaderAlignment(enum.Enum):
    Null = -1
    Top = 0
    Middle = 1
    Bottom = 2
    TextBottomMax = 3
    TextBottomMaxUnderline = 4
    TextBottom = 5
    TextBottomUnderline = 6
    TextTopMax = 7
    TextTopMaxUnderline = 8
    TextTop = 9
    TextTopUnderline = 10
    Last = 11


class LabelData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetText(self) -> str:
        ...
    def SetText(self, lines: str) -> None:
        ...
    def GetSimpleDraftingAidPreferences(self) -> Annotations.SimpleDraftingAidPreferences:
        ...
    def SetSimpleDraftingAidPreferences(self, preferences: Annotations.SimpleDraftingAidPreferences) -> None:
        ...


class LabelCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Label]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def NewLabelData(self) -> Annotations.LabelData:
        ...
    def CreatePmiLabel(self, labelData: Annotations.LabelData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.PmiLabel:
        ...
    def Tag(self) -> Tag: ...



class Label(Annotations.NoteBase):
    def __init__(self) -> None: ...


class JogOrientation(enum.Enum):
    JogIn = 1
    JogOut = 2


class ISlotDimension():
    def IsSlotDimension(self) -> bool:
        ...
    def ConvertSlotDimensionAssociativity(self) -> bool:
        ...


class IRectangularTarget():
    def GetLength(self) -> Annotations.Value:
        ...
    def SetLength(self, length: Annotations.Value) -> None:
        ...
    def GetWidth(self) -> Annotations.Value:
        ...
    def SetWidth(self, width: Annotations.Value) -> None:
        ...


class IPointTarget():
    PointCoordinates: Point3d


class IPmiSemantics():
    def GetDatumData(self) -> Annotations.PmiDatumData:
        ...
    def GetDimensionData(self) -> Annotations.PmiDimensionData:
        ...
    def GetFcfData(self) -> Annotations.PmiFcfData:
        ...
    def GetNoteData(self) -> Annotations.PmiNoteData:
        ...
    def GetLineWeldData(self) -> Annotations.PmiLineWeldData:
        ...
    def GetRegionData(self) -> Annotations.PmiRegionData:
        ...
    def GetProprietaryInfoData(self) -> Annotations.PmiProprietaryInfoData:
        ...
    def GetGovernmentSecurityInfoData(self) -> Annotations.PmiGovernmentSecurityInfoData:
        ...
    def GetExportControlData(self) -> Annotations.PmiExportControlData:
        ...
    def GetBalloonNoteData(self) -> Annotations.PmiBalloonNoteData:
        ...
    def GetMaterialSpecificationData(self) -> Annotations.PmiMaterialSpecificationData:
        ...
    def GetEnterpriseIdentifierData(self) -> Annotations.PmiEnterpriseIdentifierData:
        ...
    def GetProcessSpecificationData(self) -> Annotations.PmiProcessSpecificationData:
        ...
    def GetPartIdentificationData(self) -> Annotations.PmiPartIdentificationData:
        ...
    def GetLocatorDesignatorData(self) -> Annotations.PmiLocatorDesignatorData:
        ...
    def GetCoordinateNoteData(self) -> Annotations.PmiCoordinateNoteData:
        ...
    def GetSurfaceFinishData(self) -> Annotations.PmiSurfaceFinishData:
        ...
    def GetDatumTargetData(self) -> Annotations.PmiDatumTargetData:
        ...


class IPmi():
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class IntersectionSymbolCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.IntersectionSymbol]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateIntersectionSymbolBuilder(self, intersectionPt: Annotations.IntersectionSymbol) -> Annotations.IntersectionSymbolBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.IntersectionSymbol:
        ...
    def Tag(self) -> Tag: ...



class IntersectionSymbolBuilder(Annotations.BaseSymbolBuilder):
    def __init__(self) -> None: ...
    Color: NXColor
    Extension: float
    Inherit: SelectNXObject
    IntersectionObject1: SelectNXObject
    IntersectionObject2: SelectNXObject
    Width: Annotations.IntersectionSymbolBuilder.Thickness


    class Thickness(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 6
        Two = 7
        Three = 8
        Four = 9
        Five = 10
        Six = 11
        Seven = 12
        Eight = 13
        Nine = 14
    

class IntersectionSymbol(Annotations.DraftingAid):
    def __init__(self) -> None: ...


class InspectionSymbolAroundAppendedText(enum.Enum):
    None = 0
    Before = 1
    After = 2
    BeforeAfter = 3
    All = 4


class ImportSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    def StartImport(self) -> None:
        ...
    def GetFilesToProcess(self, files: str) -> None:
        ...
    def SetFilesToProcess(self, files: str) -> None:
        ...
    def GetExpandedFiles(self, files: str) -> None:
        ...
    def SetExpandedFiles(self, files: str) -> None:
        ...
    IncludeSubfolders: bool
    InputFolder: str
    IsPartSymbol: bool
    IsTeamcenter: bool
    LibraryPath: str
    PreserveFolderStructure: bool
    SelectMode: Annotations.ImportSymbolBuilder.FileFolder


    class FileFolder(enum.Enum):
        File = 0
        Folder = 1
    

class ImportAutocadBlockBuilder(Builder):
    def __init__(self) -> None: ...
    def AddFolder(self, folderName: str) -> None:
        ...
    def AddFile(self, fileName: str) -> None:
        ...
    def RemoveFolder(self, folderName: str) -> None:
        ...
    def RemoveFile(self, fileName: str) -> None:
        ...
    def SelectFolder(self, folderName: str, isSelected: bool) -> None:
        ...
    def SelectFile(self, fileName: str, isSelected: bool) -> None:
        ...
    def SelectBlock(self, fileName: str, blockName: str, isSelected: bool) -> None:
        ...
    ImportEntityType: Annotations.ImportAutocadBlockBuilder.EntityType
    ImportPolylineTo: int
    IncludeModelSpace: bool
    IncludeSubfolders: bool
    InputFolder: str
    LibraryPathName: str
    PreserveFolderStructure: bool
    SelectMode: Annotations.ImportAutocadBlockBuilder.FileFolder
    SettingsFile: str
    SymbolType: Annotations.ImportAutocadBlockBuilder.Type
    Unit: int


    class Type(enum.Enum):
        Teamcenter = 0
        Part = 1
        Native = 2
    

    class FileFolder(enum.Enum):
        File = 0
        Folder = 1
    

    class EntityType(enum.Enum):
        Symbol = 0
        Component = 1
    

class ILineTarget():
    EndPointCoordinates: Point3d
    StartPointCoordinates: Point3d


class ILinearTolerance():
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...


class IFcf():
    def GetFcfFrameData(self) -> Annotations.FcfFrameData:
        ...
    def SetFcfFrameData(self, data: Annotations.FcfFrameData) -> None:
        ...
    def GetFcfFrameDataArray(self) -> typing.List[Annotations.FcfFrameData]:
        ...
    def SetFcfFrameData(self, fcfFrameData: typing.List[Annotations.FcfFrameData]) -> None:
        ...


class IdSymbolCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.IdSymbol]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateIdSymbolBuilder(self, idsymbol: Annotations.IdSymbol) -> Annotations.IdSymbolBuilder:
        ...
    def CreateCalloutGroupBuilder(self) -> Annotations.CalloutGroupBuilder:
        ...
    def Tag(self) -> Tag: ...



class IdSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    def SetPreviewObject(self, symbol: Annotations.IdSymbol) -> None:
        """[Obsolete("Deprecated in NX6.0.0.  This functionality is no longer supported.")"""
        ...
    BalloonType: Annotations.BalloonTypes
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder
    Inherit: SelectObject
    Leader: Annotations.LeaderBuilder
    LowerText: str
    Origin: Annotations.OriginBuilder
    Placement: Annotations.AnnotationPlacement
    Size: float
    Style: Annotations.StyleBuilder
    Type: Annotations.IdSymbolBuilder.SymbolTypes
    UpperText: str


    class SymbolTypes(enum.Enum):
        Circle = 0
        DividedCircle = 1
        Triangle = 2
        TriangleUp = 3
        Square = 4
        DividedSquare = 5
        Hexagon = 6
        DividedHexagon = 7
        QuadrantCircle = 8
        RoundedBox = 9
        Underline = 10
    

class IdSymbol(Annotations.DraftingAid):
    def __init__(self) -> None: ...


class IdentificationLineLocation(enum.Enum):
    None = 0
    Top = 1
    Bottom = 2
    Last = 3


class IDatumTarget():
    DatumLabel: str
    TargetIndex: int


class IDatum():
    Label: str


class IContainer():
    def GetObjects(self) -> typing.List[NXObject]:
        ...
    def RemoveObject(self, object: NXObject) -> None:
        ...


class ICircularTarget():
    def GetDiameter(self) -> Annotations.Value:
        ...
    def SetDiameter(self, diameter: Annotations.Value) -> None:
        ...


class IArbitraryTarget():
    UpperText: str


class IAppendedText():
    def GetAppendedText(self) -> Annotations.AppendedText:
        ...
    def SetAppendedText(self, appendedText: Annotations.AppendedText) -> None:
        ...


class IAngularTolerance():
    def GetTolerance(self) -> Annotations.AngularTolerance:
        ...
    def SetTolerance(self, tolerances: Annotations.AngularTolerance) -> None:
        ...


class HorizontalOrdinateMargin(Annotations.OrdinateMargin):
    def __init__(self) -> None: ...


class HorizontalOrdinateDimension(Annotations.OrdinateDimension):
    def __init__(self) -> None: ...


class HorizontalDimension(Annotations.BaseHorizontalDimension):
    def __init__(self) -> None: ...


class HoleTableSettingsWorkflowBuilder(Annotations.TabularNoteStyleBuilder):
    def __init__(self) -> None: ...


class HoleTableSettingsLabelBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CharactersToSkip: str
    IndexFormat: Annotations.HoleTableSettingsLabelBuilder.IndexType
    RelativeLocation: Annotations.HoleTableSettingsLabelBuilder.RelativeLocationType
    ShowLabelWithLeader: bool


    class RelativeLocationType(enum.Enum):
        TopLeft = 0
        TopMiddle = 1
        TopRight = 2
        CenterLeft = 3
        Center = 4
        CenterRight = 5
        BottomLeft = 6
        BottomMiddle = 7
        BottomRight = 8
    

    class IndexType(enum.Enum):
        HoleTypeSymbolAndNumber = 0
        Number = 1
        LetterAndNumber = 2
    

class HoleTableSettingsHoleFiltersBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BlindHoles: bool
    CombinationHoles: bool
    CounterboredHoles: bool
    CountersinkAngle: float
    CountersunkHoles: bool
    DraftingSketchCircles: bool
    IncludePartialHoles: bool
    ModelingSketchCircles: bool
    NoseAngle: float
    PartialHoleAngle: float
    Scope: Annotations.HoleTableSettingsHoleFiltersBuilder.ScopeType
    ThreadedHoles: bool
    ThroughHoles: bool
    WireEDMStartHoles: bool


    class ScopeType(enum.Enum):
        OneSidedHoles = 0
        TwoSidedHoles = 1
    

class HoleTableSettingsFormatBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DecimalPlaces: int
    DeletedHolesDisplay: Annotations.HoleTableSettingsFormatBuilder.DeletedHolesDisplayType
    DepthMeasurementDatum: Annotations.HoleTableSettingsFormatBuilder.DepthMeasurementDatumType
    DisplayAllTextInUpperCase: bool
    DisplayPartBodyName: bool
    MergeCellsWithSameSize: bool
    ReportTapHoleSizeForThreadedHoles: bool
    ShowColumns: Annotations.HoleTableSettingsFormatBuilder.ShowColumnsType
    SizeFormat: Annotations.HoleTableSettingsFormatBuilder.SizeFormatType


    class SizeFormatType(enum.Enum):
        DisplayInSummaryRows = 0
        DisplayInColumn = 1
    

    class ShowColumnsType(enum.Enum):
        Xy = 0
        Xyz = 1
        All = 2
    

    class DepthMeasurementDatumType(enum.Enum):
        TopBottomFace = 0
        BaseFace = 1
        StepFace = 2
    

    class DeletedHolesDisplayType(enum.Enum):
        Strikethrough = 0
        HideText = 1
        Remove = 2
    

class HoleTableSettingsContentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetContentOrder(self) -> typing.List[Annotations.HoleTableSettingsContentBuilder.Content]:
        ...
    def SetContentOrder(self, contentOrder: typing.List[Annotations.HoleTableSettingsContentBuilder.Content]) -> None:
        ...
    def Validate(self) -> bool:
        ...


    class Content(enum.Enum):
        Diameter = 0
        DiameterFit = 1
        Depth = 2
        DepthFit = 3
        DrillType = 4
        DrillDirection = 5
    

class HoleTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.HoleTable]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHoleTableBuilder(self, holeTable: Annotations.Table) -> Annotations.HoleTableBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.HoleTable:
        ...
    def Tag(self) -> Tag: ...



class HoleTableBuilder(Builder):
    def __init__(self) -> None: ...
    def ResetHoletableOrdinateOrigin(self) -> None:
        ...
    def ResetLabelPosition(self) -> None:
        ...
    Baseline: Annotations.OrdinateBaselineBuilder
    Inherit: SelectDisplayableObject
    OrdinateOrigin: SelectDisplayableObject
    Origin: Annotations.OriginBuilder
    SelectedObjects: SelectNXObjectList
    Style: Annotations.TableStyleBuilder


class HoleTable(Annotations.Table):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...


class HoleDimension(Annotations.BaseHoleDimension):
    def __init__(self) -> None: ...


class HoleCalloutSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetListOfFeatures(self) -> typing.List[Annotations.HoleCalloutSettingsBuilder.Featuretype]:
        ...
    def GetListOfParameters(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype) -> typing.List[Annotations.HoleCalloutSettingsBuilder.Parametertype]:
        ...
    def ReorderParameters(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, parameters: typing.List[Annotations.HoleCalloutSettingsBuilder.Parametertype]) -> bool:
        ...
    def ShiftUp(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> None:
        ...
    def ShiftDown(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> None:
        ...
    def InsertLineBreak(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> None:
        ...
    def DeleteLineBreak(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> None:
        ...
    def GetNthParameterDisplay(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> bool:
        ...
    def SetNthParameterDisplay(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int, parameterDisplay: bool) -> None:
        ...
    def SetNthParameterValue(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int, value: str) -> None:
        ...
    def GetNthParameterValue(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> str:
        ...
    def GetNthParameterValueString(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> str:
        ...
    def SetNthParameterPrefix(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int, lines: str) -> None:
        ...
    def GetNthParameterPrefix(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> str:
        ...
    def SetNthParameterSuffix(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int, lines: str) -> None:
        ...
    def GetNthParameterSuffix(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> str:
        ...
    def GetNthParameterStyle(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, nth: int) -> Annotations.StyleBuilder:
        ...
    def ResetFromFeature(self, feature: TaggedObject, partOccurrence: Assemblies.Component, view: View, pickPoint: Point3d) -> None:
        ...
    def GetParameterSpaceFactor(self) -> float:
        ...
    def SetParameterSpaceFactor(self, parameterSpaceFactor: float) -> None:
        ...
    def GetLineSpaceFactor(self) -> float:
        ...
    def SetLineSpaceFactor(self, lineSpaceFactor: float) -> None:
        ...
    def GetLeaderAttachment(self) -> Annotations.HoleCalloutSettingsBuilder.LeaderAttachment:
        ...
    def SetLeaderAttachment(self, leaderAttachment: Annotations.HoleCalloutSettingsBuilder.LeaderAttachment) -> None:
        ...
    def GetThroughHoleTextOfType(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype) -> str:
        ...
    def SetThroughHoleTextOfType(self, featureType: Annotations.HoleCalloutSettingsBuilder.Featuretype, throughHoleTextString: str) -> None:
        ...
    def Validate(self) -> bool:
        ...


    class Parametertype(enum.Enum):
        Diameter = 0
        Depth = 1
        CounterBoreDiameter = 2
        CounterBoreDepth = 3
        CounterSinkDiameter = 4
        CounterSinkAngle = 5
        TaperAngle = 6
        PatternFeatureCount = 7
        ScrewSize = 8
        Fit = 9
        LineBreak = 10
        ThreadSize = 11
        ThreadDepth = 12
        Pitch = 13
        Angle = 14
        MinorDiameter = 15
        MajorDiameter = 16
        TapDrillDiameter = 17
        Callout = 18
        Length = 19
        ShaftSize = 20
        ThreadForm = 21
        ThreadInternalExternalSymbol = 22
        ThreadPitch = 23
        SymbolicThreadForm = 24
        SymbolicThreadInternalExternalSymbol = 25
        SymbolicThreadPitch = 26
        DrillSize = 27
        ThreadHandedness = 28
        ReliefDiameter = 29
        ReliefDepth = 30
        ReliefChamferDiameter = 31
        ReliefChamferAngle = 32
        StartChamferDiameter = 33
        StartChamferAngle = 34
        EndChamferDiameter = 35
        EndChamferAngle = 36
        NeckChamferDiameter = 37
        NeckChamferAngle = 38
        None = 39
    

    class LeaderAttachment(enum.Enum):
        Top = 0
        BelowBottomExtendedToMaximum = 1
        BelowTopExtendedToMaximum = 2
    

    class Featuretype(enum.Enum):
        GeneralHole = 0
        DrillSizeHole = 1
        ScrewClearanceHole = 2
        ThreadedHole = 3
        SymbolicThread = 4
        None = 5
    

class HatchStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AreaFillAngle: float
    AreaFillMaterial: Annotations.AreaFillMaterial
    AreaFillScale: float
    AutoTextIsland: bool
    Color: NXColor
    FindApparentIntersections: bool
    HatchAngle: float
    HatchDistance: float
    HatchFile: str
    HatchMaterial: str
    IslandMargin: float
    LineWidth: Annotations.LineWidth
    Tolerance: float


class HatchFillSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def FindCrosshatchFile(self, identifier: str) -> str:
        ...
    def Validate(self) -> bool:
        ...
    Angle: float
    AnnotationType: Annotations.HatchFillSettingsBuilder.AnnotationTypes
    ApplyToAllFromSameComp: bool
    AreafillAngle: float
    Color: NXColor
    CrosshatchFile: str
    Distance: float
    Material: Annotations.AreaFillMaterial
    Pattern: str
    Scale: float
    Tolerance: float
    Width: Annotations.LineWidth


    class AnnotationTypes(enum.Enum):
        Crosshatch = 0
        AreaFill = 1
    

class HatchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Hatch]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHatchBuilder(self, hatch: Annotations.Hatch) -> Annotations.HatchBuilder:
        ...
    def Tag(self) -> Tag: ...



class HatchBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMarginPercent(self, annotation: NXObject) -> float:
        ...
    def SetMarginPercent(self, annotation: NXObject, marginpercent: float) -> None:
        ...
    def SetNumCurrentDirectionMapElements(self, numCurrentDirectionMapElement: int) -> None:
        ...
    def SetCurveDirection(self, curveTag: NXObject, curveDirection: int) -> None:
        ...
    def SetSectionCurveDirections(self, section: NXObject, curve: NXObject, curveDirections: int) -> None:
        ...
    Angle: float
    AnnotationToExclude: SelectDisplayableObjectList
    AnnotationType: Annotations.HatchBuilder.AnnotationTypes
    AreafillAngle: float
    AutomaticallyExcludeText: bool
    Boundary: Annotations.BoundaryBuilder
    Color: NXColor
    CrosshatchFile: str
    Distance: float
    HatchFillSettings: Annotations.HatchFillSettingsBuilder
    Material: Annotations.AreaFillMaterial
    Pattern: str
    Scale: float
    Tolerance: float
    Width: Annotations.LineWidth


    class AnnotationTypes(enum.Enum):
        Crosshatch = 0
        AreaFill = 1
    

class Hatch(Annotations.Annotation):
    def __init__(self) -> None: ...


class GovernmentSecurityInformationBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetStringText(self) -> str:
        ...
    def SetStringText(self, stringText: str) -> None:
        ...
    Identifier: str
    Title: str


class GovernmentSecurityInformation(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class GeometricCharacteristic(enum.Enum):
    Straightness = 0
    Flatness = 1
    Circular = 2
    Cylindrical = 3
    LineProfile = 4
    SurfaceProfile = 5
    Angular = 6
    Perpendicular = 7
    Parallel = 8
    Position = 9
    Concentric = 10
    Symmetric = 11
    CircularRunout = 12
    TotalRunout = 13
    Last = 14


class GeodesicDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder
    Measurement: Annotations.DimensionMeasurementBuilder
    MeasurementPoint: SelectPoint
    Origin: Annotations.OriginBuilder
    OriginCurve: SelectEdge
    Style: Annotations.StyleBuilder


class GenericNote(Annotations.BaseNote):
    def __init__(self) -> None: ...


class GeneralVerticalDimension(Annotations.BaseVerticalDimension):
    def __init__(self) -> None: ...


class GeneralRadiusDimension(Annotations.BaseRadiusDimension):
    def __init__(self) -> None: ...


class GeneralPerpendicularDimension(Annotations.BasePerpendicularDimension):
    def __init__(self) -> None: ...


class GeneralParallelDimension(Annotations.BaseParallelDimension):
    def __init__(self) -> None: ...


class GeneralNoteBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetText(self) -> str:
        ...
    def SetText(self, text: str) -> None:
        ...
    Category: str
    Identifier: str
    Revision: str
    Title: str


class GeneralNote(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class GeneralMinorAngularDimension(Annotations.MinorAngularDimension):
    def __init__(self) -> None: ...


class GeneralMajorAngularDimension(Annotations.MajorAngularDimension):
    def __init__(self) -> None: ...


class GeneralLabel(Annotations.Label):
    def __init__(self) -> None: ...


class GeneralHorizontalDimension(Annotations.BaseHorizontalDimension):
    def __init__(self) -> None: ...


class GeneralHoleDimension(Annotations.BaseHoleDimension):
    def __init__(self) -> None: ...


class GeneralFoldedRadiusDimension(Annotations.BaseRadiusDimension):
    def __init__(self) -> None: ...


class GeneralDiameterDimension(Annotations.BaseDiameterDimension):
    def __init__(self) -> None: ...


class GeneralCylindricalDimension(Annotations.BaseCylindricalDimension):
    def __init__(self) -> None: ...


class GeneralCustomSymbol(Annotations.BaseCustomSymbol):
    def __init__(self) -> None: ...


class GeneralConcentricCircleDimension(Annotations.BaseConcentricCircleDimension):
    def __init__(self) -> None: ...


class GeneralChamferDimension(Annotations.BaseChamferDimension):
    def __init__(self) -> None: ...


class GeneralArcLengthDimension(Annotations.BaseArcLengthDimension):
    def __init__(self) -> None: ...


class GdtDatumCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Datum]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def NewDatumData(self) -> Annotations.DatumData:
        ...
    def CreateDatum(self, datumData: Annotations.DatumData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.Datum:
        ...
    def CreateDatum(self, datumData: Annotations.DatumData, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.DraftingDatum:
        ...
    def CreateDraftingDatumFeatureSymbolBuilder(self, datum: Annotations.DraftingDatum) -> Annotations.DraftingDatumFeatureSymbolBuilder:
        ...
    def CreatePmiDatumFeatureSymbolBuilder(self, datum: Annotations.Datum) -> Annotations.PmiDatumFeatureSymbolBuilder:
        ...
    def Tag(self) -> Tag: ...



class GdtCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Gdt]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class Gdt(Annotations.SimpleDraftingAid):
    def __init__(self) -> None: ...
    def SetSymbolCfw(self, cfw: Annotations.LineCfw) -> None:
        ...
    def GetFcfFrameData(self) -> Annotations.FcfFrameData:
        ...
    def SetFcfFrameData(self, data: Annotations.FcfFrameData) -> None:
        ...
    def GetFcfFrameDataArray(self) -> typing.List[Annotations.FcfFrameData]:
        ...
    def SetFcfFrameData(self, fcfFrameData: typing.List[Annotations.FcfFrameData]) -> None:
        ...
    CanChangeLeaderPositionParameter: bool
    HasLeaderPositionParameter: bool
    HasStubbedDatumStyle: bool
    LeaderPositionParameter: float


class FrameBarStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AftPerpendicularStyle: Annotations.FrameBarElementStyleBuilder
    AlongHullBaselineStyle: Annotations.FrameBarElementStyleBuilder
    AlongHullDecksStyle: Annotations.FrameBarElementStyleBuilder
    AlongHullLongitudinalZFramesStyle: Annotations.FrameBarElementStyleBuilder
    AlongHullLongitudinalZInsertFramesStyle: Annotations.FrameBarElementStyleBuilder
    AlongHullWaterlineStyle: Annotations.FrameBarElementStyleBuilder
    BaselineStyle: Annotations.FrameBarElementStyleBuilder
    BulkHeadsStyle: Annotations.FrameBarElementStyleBuilder
    CenterlineYStyle: Annotations.FrameBarElementStyleBuilder
    DecksStyle: Annotations.FrameBarElementStyleBuilder
    ForwardPerpendicularStyle: Annotations.FrameBarElementStyleBuilder
    InterTransverseFramesStyle: Annotations.FrameBarElementStyleBuilder
    LongitudinalBulkheadsStyle: Annotations.FrameBarElementStyleBuilder
    LongitudinalYFramesStyle: Annotations.FrameBarElementStyleBuilder
    LongitudinalYInsertFramesStyle: Annotations.FrameBarElementStyleBuilder
    LongitudinalZFramesStyle: Annotations.FrameBarElementStyleBuilder
    LongitudinalZInsertFramesStyle: Annotations.FrameBarElementStyleBuilder
    TransversalInsertAreaStyle: Annotations.FrameBarElementStyleBuilder
    TransverseFramesStyle: Annotations.FrameBarElementStyleBuilder
    WaterlineStyle: Annotations.FrameBarElementStyleBuilder


class FrameBarPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AftPerpendicularLabelColor: int
    AftPerpendicularLabelFont: int
    AftPerpendicularLabelItalicized: bool
    AftPerpendicularLabelWidth: int
    AftPerpendicularTicColor: int
    AftPerpendicularTicDisplay: int
    AftPerpendicularTicFont: int
    AftPerpendicularTicLength: float
    AftPerpendicularTicWidth: int
    BaselineLabelColor: int
    BaselineLabelFont: int
    BaselineLabelItalicized: bool
    BaselineLabelWidth: int
    BaselineTicColor: int
    BaselineTicDisplay: int
    BaselineTicFont: int
    BaselineTicLength: float
    BaselineTicWidth: int
    BulkHeadsLabelColor: int
    BulkHeadsLabelFont: int
    BulkHeadsLabelItalicized: bool
    BulkHeadsLabelName: int
    BulkHeadsLabelWidth: int
    BulkHeadsTicColor: int
    BulkHeadsTicDisplay: int
    BulkHeadsTicFont: int
    BulkHeadsTicLength: float
    BulkHeadsTicWidth: int
    CenterlineYLabelColor: int
    CenterlineYLabelFont: int
    CenterlineYLabelItalicized: bool
    CenterlineYLabelWidth: int
    CenterlineYTicColor: int
    CenterlineYTicDisplay: int
    CenterlineYTicFont: int
    CenterlineYTicLength: float
    CenterlineYTicWidth: int
    DecksLabelColor: int
    DecksLabelFont: int
    DecksLabelItalicized: bool
    DecksLabelName: int
    DecksLabelWidth: int
    DecksTicColor: int
    DecksTicDisplay: int
    DecksTicFont: int
    DecksTicLength: float
    DecksTicWidth: int
    ForwardPerpendicularLabelColor: int
    ForwardPerpendicularLabelFont: int
    ForwardPerpendicularLabelItalicized: bool
    ForwardPerpendicularLabelWidth: int
    ForwardPerpendicularTicColor: int
    ForwardPerpendicularTicDisplay: int
    ForwardPerpendicularTicFont: int
    ForwardPerpendicularTicLength: float
    ForwardPerpendicularTicWidth: int
    InterTransverseFramesExtendBegin: int
    InterTransverseFramesExtendColor: int
    InterTransverseFramesExtendFont: int
    InterTransverseFramesExtendFrequency: int
    InterTransverseFramesExtendLength: float
    InterTransverseFramesExtendWidth: int
    InterTransverseFramesLabelColor: int
    InterTransverseFramesLabelFont: int
    InterTransverseFramesLabelItalicized: bool
    InterTransverseFramesLabelName: int
    InterTransverseFramesLabelWidth: int
    InterTransverseFramesSkipLabelBegin: int
    InterTransverseFramesSkipLabelFrequency: int
    InterTransverseFramesSkipTicBegin: int
    InterTransverseFramesSkipTicFrequency: int
    InterTransverseFramesTicColor: int
    InterTransverseFramesTicDisplay: int
    InterTransverseFramesTicFont: int
    InterTransverseFramesTicLength: float
    InterTransverseFramesTicWidth: int
    LongitudinalYFramesExtendBegin: int
    LongitudinalYFramesExtendColor: int
    LongitudinalYFramesExtendFont: int
    LongitudinalYFramesExtendFrequency: int
    LongitudinalYFramesExtendLength: float
    LongitudinalYFramesExtendWidth: int
    LongitudinalYFramesLabelColor: int
    LongitudinalYFramesLabelFont: int
    LongitudinalYFramesLabelItalicized: bool
    LongitudinalYFramesLabelName: int
    LongitudinalYFramesLabelWidth: int
    LongitudinalYFramesSkipLabelBegin: int
    LongitudinalYFramesSkipLabelFrequency: int
    LongitudinalYFramesSkipTicBegin: int
    LongitudinalYFramesSkipTicFrequency: int
    LongitudinalYFramesTicColor: int
    LongitudinalYFramesTicDisplay: int
    LongitudinalYFramesTicFont: int
    LongitudinalYFramesTicLength: float
    LongitudinalYFramesTicWidth: int
    LongitudinalZFramesExtendBegin: int
    LongitudinalZFramesExtendColor: int
    LongitudinalZFramesExtendFont: int
    LongitudinalZFramesExtendFrequency: int
    LongitudinalZFramesExtendLength: float
    LongitudinalZFramesExtendWidth: int
    LongitudinalZFramesLabelColor: int
    LongitudinalZFramesLabelFont: int
    LongitudinalZFramesLabelItalicized: bool
    LongitudinalZFramesLabelName: int
    LongitudinalZFramesLabelWidth: int
    LongitudinalZFramesSkipLabelBegin: int
    LongitudinalZFramesSkipLabelFrequency: int
    LongitudinalZFramesSkipTicBegin: int
    LongitudinalZFramesSkipTicFrequency: int
    LongitudinalZFramesTicColor: int
    LongitudinalZFramesTicDisplay: int
    LongitudinalZFramesTicFont: int
    LongitudinalZFramesTicLength: float
    LongitudinalZFramesTicWidth: int
    TransversalInsertAreaLabelColor: int
    TransversalInsertAreaLabelFont: int
    TransversalInsertAreaLabelItalicized: bool
    TransversalInsertAreaLabelName: int
    TransversalInsertAreaLabelWidth: int
    TransversalInsertAreaTicColor: int
    TransversalInsertAreaTicDisplay: int
    TransversalInsertAreaTicFont: int
    TransversalInsertAreaTicLength: float
    TransversalInsertAreaTicWidth: int
    TransverseFramesExtendBegin: int
    TransverseFramesExtendColor: int
    TransverseFramesExtendFont: int
    TransverseFramesExtendFrequency: int
    TransverseFramesExtendLength: float
    TransverseFramesExtendWidth: int
    TransverseFramesLabelColor: int
    TransverseFramesLabelFont: int
    TransverseFramesLabelItalicized: bool
    TransverseFramesLabelName: int
    TransverseFramesLabelWidth: int
    TransverseFramesSkipLabelBegin: int
    TransverseFramesSkipLabelFrequency: int
    TransverseFramesSkipTicBegin: int
    TransverseFramesSkipTicFrequency: int
    TransverseFramesTicColor: int
    TransverseFramesTicDisplay: int
    TransverseFramesTicFont: int
    TransverseFramesTicLength: float
    TransverseFramesTicWidth: int
    WaterlineLabelColor: int
    WaterlineLabelFont: int
    WaterlineLabelItalicized: bool
    WaterlineLabelWidth: int
    WaterlineTicColor: int
    WaterlineTicDisplay: int
    WaterlineTicFont: int
    WaterlineTicLength: float
    WaterlineTicWidth: int


class FrameBarElementStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DisplayPosition: bool
    DisplayThicknessDirection: bool
    ExtendedTicBegin: int
    ExtendedTicColor: int
    ExtendedTicFont: int
    ExtendedTicFrequency: int
    ExtendedTicLength: float
    ExtendedTicWidth: int
    LabelColor: int
    LabelFont: int
    LabelItalicized: bool
    LabelName: int
    LabelTextAspectRatio: float
    LabelTextFontGapFactor: float
    LabelTextHeight: float
    LabelTextLetteringAngle: float
    LabelWidth: int
    NumberOfStartFrame: str
    SkipLabelBegin: int
    SkipLabelFrequency: int
    SkipTicBegin: int
    SkipTicFrequency: int
    TicColor: int
    TicDisplay: int
    TicFont: int
    TicLabelTextOrientation: Annotations.FrameBarElementStyleBuilder.LabelTextOrientation
    TicLength: float
    TicWidth: int


    class LabelTextOrientation(enum.Enum):
        AlongTic = 0
        PerpendicularToTic = 1
    

class FrameBarElements(enum.Enum):
    AftPerpendicular = 0
    ForwardPerpendicular = 1
    CenterlineY = 2
    Baseline = 3
    Waterline = 4
    TransversalInsertArea = 5
    BulkHeads = 6
    Decks = 7
    TransverseFrames = 8
    InterTransverseFrames = 9
    LongitudinalYFrames = 10
    LongitudinalZFrames = 11
    AlongHullBaseline = 12
    AlongHullWaterline = 13
    AlongHullDecks = 14
    AlongHullLongitudinalZFrames = 15
    LongitudinalBulkHeads = 16
    LongitudinalYInsertFrames = 17
    LongitudinalZInsertFrames = 18
    AlongHullLongitudinalZInsertFrames = 19
    Num = 20


class FrameBarCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.FrameBar]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFrameBarBuilder(self, framebar: Annotations.BaseFrameBar) -> Annotations.FrameBarBuilder:
        ...
    def CreateAddTicBuilder(self, framebar: Annotations.BaseFrameBar) -> Annotations.AddTicBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.FrameBar:
        ...
    def Tag(self) -> Tag: ...



class FrameBarBuilder(Annotations.BaseFrameBarBuilder):
    def __init__(self) -> None: ...


class FrameBar(Annotations.BaseFrameBar):
    def __init__(self) -> None: ...


class FractionDenominatorFormat(enum.Enum):
    One = 0
    Two = 1
    Four = 2
    Eight = 3
    Sixteen = 4
    ThirtyTwo = 5
    SixtyFour = 6
    Last = 7


class ForeshorteningSymbolSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Angle: float
    ForeshorteningSymbolMethodType: Annotations.ForeshorteningSymbolSettingsBuilder.MethodType
    ForeshorteningSymbolType: Annotations.ForeshorteningSymbolSettingsBuilder.SymbolType
    Height: float
    Width: float


    class SymbolType(enum.Enum):
        Regular = 0
        Stretched = 1
    

    class MethodType(enum.Enum):
        WidthAndAngle = 0
        WidthAndHeight = 1
    

class ForeshorteningSymbolBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetSymbols(self, indices: int) -> typing.List[Point3d]:
        ...
    def AddSymbol(self, locations: Point3d) -> None:
        ...
    def ModifySymbol(self, symbolIndex: int, locations: Point3d) -> None:
        ...
    def DeleteSymbol(self, symbolIndex: int) -> None:
        ...
    def Validate(self) -> bool:
        ...


class FoldedRadiusDimension(Annotations.BaseFoldedRadiusDimension):
    def __init__(self) -> None: ...


class FlipOption(enum.Enum):
    Horizontal = 0
    Vertical = 1
    Last = 2


class FitDisplayStyle(enum.Enum):
    FitSymbols = 0
    FitSymbolsAndLimits = 1
    FitSymbolsAndTolerances = 2
    TolerancesOnly = 3


class FitDisplaySplitByDimline(enum.Enum):
    None = 0
    ToleranceOnly = 1
    ToleranceAndValue = 2


class FitDisplayAlignment(enum.Enum):
    CenterValue = 0
    CenterValueAndFit = 1
    Bottom = 2


class FitAssemblyNewDisplayStyle(enum.Enum):
    SingleLine = 0
    DoubleLine = 1


class FitAssemblyDisplayStyle(enum.Enum):
    SingleLine = 0
    TwoLinesCentered = 1
    TwoLinesAligned = 2


class FitAnsiHoleType(enum.Enum):
    Hole = 0
    Shaft = 1
    Fit = 2


class FinishMethod(enum.Enum):
    None = 0
    Chipping = 1
    Grinding = 2
    Hammering = 3
    Machining = 4
    Rolling = 5
    Peening = 6
    Last = 7


class FeatureIdBusinessModifierBuilder(Builder):
    def __init__(self) -> None: ...
    FeatureId: str
    Title: str


class FeatureIdBusinessModifier(Annotations.ListBusinessModifier):
    def __init__(self) -> None: ...


class FeatureControlFrameIndicatorBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.FeatureControlFrameIndicatorBuilder]) -> None:
        ...
    def Append(self, object: Annotations.FeatureControlFrameIndicatorBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.FeatureControlFrameIndicatorBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.FeatureControlFrameIndicatorBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.FeatureControlFrameIndicatorBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.FeatureControlFrameIndicatorBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.FeatureControlFrameIndicatorBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.FeatureControlFrameIndicatorBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.FeatureControlFrameIndicatorBuilder, object2: Annotations.FeatureControlFrameIndicatorBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.FeatureControlFrameIndicatorBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FeatureControlFrameIndicatorBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Direction: Annotations.FeatureControlFrameIndicatorBuilder.FcfIndicatorDirection
    IndicatorType: Annotations.FeatureControlFrameIndicatorBuilder.FcfIndicatorType
    Label: Annotations.DatumReferenceBuilder
    Symbol: Annotations.FeatureControlFrameIndicatorBuilder.FcfIndicatorCharacteristic


    class FcfIndicatorType(enum.Enum):
        IntersectionPlane = 0
        OrientationPlane = 1
        CollectionPlane = 2
        DirectionFeature = 3
    

    class FcfIndicatorDirection(enum.Enum):
        After = 0
        Before = 1
    

    class FcfIndicatorCharacteristic(enum.Enum):
        Parallel = 0
        Perpendicular = 1
        Angular = 2
        Including = 3
    

class FeatureControlFrameDataBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.FeatureControlFrameDataBuilder]) -> None:
        ...
    def Append(self, object: Annotations.FeatureControlFrameDataBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.FeatureControlFrameDataBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.FeatureControlFrameDataBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.FeatureControlFrameDataBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.FeatureControlFrameDataBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.FeatureControlFrameDataBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.FeatureControlFrameDataBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.FeatureControlFrameDataBuilder, object2: Annotations.FeatureControlFrameDataBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.FeatureControlFrameDataBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class FeatureControlFrameDataBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AreaSymbol: Annotations.FeatureControlFrameDataBuilder.AreaSymbolType
    CircleU: bool
    CircleUvalue: str
    CommonZone: bool
    DerivedFeature: bool
    DynamicProfile: bool
    FeatureControlFrameIndicatorList: Annotations.FeatureControlFrameIndicatorBuilderList
    FreeState: bool
    LeastSquaresFeature: bool
    MaterialModifier: Annotations.FeatureControlFrameDataBuilder.ToleranceMaterialModifier
    MaxInscribedFeature: bool
    MaximumTolerance: bool
    MaximumToleranceValue: str
    MinCircumscribedFeature: bool
    MinimaxFeature: bool
    PrimaryCompoundDatumReference: Annotations.CompoundDatumReferenceBuilder
    PrimaryDatumExtendedText: str
    PrimaryDatumReference: Annotations.DatumReferenceBuilder
    Projected: bool
    ProjectedValue: str
    ReciprocityRequirement: bool
    SecondaryCompoundDatumReference: Annotations.CompoundDatumReferenceBuilder
    SecondaryDatumExtendedText: str
    SecondaryDatumReference: Annotations.DatumReferenceBuilder
    StatisticalTolerance: bool
    TangentPlane: bool
    TertiaryCompoundDatumReference: Annotations.CompoundDatumReferenceBuilder
    TertiaryDatumExtendedText: str
    TertiaryDatumReference: Annotations.DatumReferenceBuilder
    ToleranceValue: str
    UnitBasis: bool
    UnitBasisValue1: str
    UnitBasisValue2: str
    Uz: bool
    ZoneShape: Annotations.FeatureControlFrameDataBuilder.ToleranceZoneShape


    class ToleranceZoneShape(enum.Enum):
        None = 0
        Diameter = 1
        SphericalDiameter = 2
        Square = 3
    

    class ToleranceMaterialModifier(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessOfFeatureSize = 3
    

    class AreaSymbolType(enum.Enum):
        Rectangular = 0
        Circular = 1
        Spherical = 2
        Square = 3
    

class FeatureControlFrameData(TaggedObject):
    def __init__(self) -> None: ...


class FeatureControlFrameBuilder(Builder):
    def __init__(self) -> None: ...
    def FeatureControlFrameData(self, featureControlFrameDataBuilders: typing.List[Annotations.FeatureControlFrameDataBuilder]) -> None:
        ...
    def InheritFrom(self, inheritTag: Annotations.BaseFcf) -> None:
        ...
    Characteristic: Annotations.FeatureControlFrameBuilder.FcfCharacteristic
    FeatureControlFrameDataList: Annotations.FeatureControlFrameDataBuilderList
    FrameStyle: Annotations.FeatureControlFrameBuilder.FcfFrameStyle
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder
    Text: Annotations.TextWithSymbolsBuilder


    class FcfFrameStyle(enum.Enum):
        SingleFrame = 0
        CompositeFrame = 1
    

    class FcfCharacteristic(enum.Enum):
        Straightness = 0
        Flatness = 1
        Circularity = 2
        Cylindricity = 3
        ProfileOfALine = 4
        ProfileOfASurface = 5
        Angularity = 6
        Perpendicularity = 7
        Parallelism = 8
        Position = 9
        Concentricity = 10
        Symmetry = 11
        CircularRunout = 12
        TotalRunout = 13
        AxisIntersection = 14
    

class FcfFrameData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFrames(self) -> typing.List[Annotations.FcfFrame]:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameBuilder.FeatureControlFrameDataList instead.")"""
        ...
    def SetFrames(self, frames: typing.List[Annotations.FcfFrame]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameBuilder.FeatureControlFrameDataList instead.")"""
        ...
    GeometricCharacteristic: Annotations.GeometricCharacteristic


class FcfFrame(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetTolerance(self) -> Annotations.Value:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.ToleranceValue instead.")"""
        ...
    def SetTolerance(self, tolerance: Annotations.Value) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.ToleranceValue instead.")"""
        ...
    def GetMaterialConditionModifiers(self) -> typing.List[Annotations.MaterialConditionModifier]:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.MaterialModifier instead.")"""
        ...
    def SetMaterialConditionModifiers(self, modifiers: typing.List[Annotations.MaterialConditionModifier]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.MaterialModifier instead.")"""
        ...
    def GetPrimaryDatumReference(self) -> Annotations.DatumReference:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.PrimaryDatumReference instead.")"""
        ...
    def SetPrimaryDatumReference(self, primary: Annotations.DatumReference) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.PrimaryDatumReference instead.")"""
        ...
    def GetSecondaryDatumReference(self) -> Annotations.DatumReference:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.SecondaryDatumReference instead.")"""
        ...
    def SetSecondaryDatumReference(self, secondary: Annotations.DatumReference) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.SecondaryDatumReference instead.")"""
        ...
    def GetTertiaryDatumReference(self) -> Annotations.DatumReference:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.TertiaryDatumReference instead.")"""
        ...
    def SetTertiaryDatumReference(self, tertiary: Annotations.DatumReference) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Annotations.FeatureControlFrameDataBuilder.TertiaryDatumReference instead.")"""
        ...
    ToleranceZoneShape: Annotations.ToleranceZoneShape


class FcfDatumReference(TaggedObject):
    def __init__(self) -> None: ...


class FcfData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFrameData(self) -> Annotations.FcfFrameData:
        ...
    def SetFrameData(self, frameData: Annotations.FcfFrameData) -> None:
        ...
    def GetSimpleDraftingAidPreferences(self) -> Annotations.SimpleDraftingAidPreferences:
        ...
    def SetSimpleDraftingAidPreferences(self, preferences: Annotations.SimpleDraftingAidPreferences) -> None:
        ...


class FcfCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Fcf]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def NewFcfData(self) -> Annotations.FcfData:
        ...
    def CreateFcf(self, fcfData: Annotations.FcfData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.Fcf:
        ...
    def Tag(self) -> Tag: ...



class Fcf(Annotations.BaseFcf):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    def GetAppendedText(self) -> Annotations.AppendedText:
        ...
    def SetAppendedText(self, appendedText: Annotations.AppendedText) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class ExtensionLineDisplay(enum.Enum):
    Two = 0
    First = 1
    Second = 2
    None = 3
    Last = 4


class ExportControlBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetStringText(self) -> str:
        ...
    def SetStringText(self, stringText: str) -> None:
        ...
    Identifier: str
    Title: str


class ExportControl(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class EnterpriseIdentificationBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetCompanyAddress(self) -> str:
        ...
    def SetCompanyAddress(self, companyAddress: str) -> None:
        ...
    CageCode: str
    CompanyName: str
    Division: str
    Title: str


class EnterpriseIdentification(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class EditTitleBlockBuilder(Annotations.BaseTitleBlockBuilder):
    def __init__(self) -> None: ...
    def GetCellValueForLabel(self, label: str) -> str:
        ...
    def SetCellValueForLabel(self, label: str, value: str) -> None:
        ...


class EditSymbolDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    def SelectComponent(self, sid: str) -> None:
        ...
    def ApplyStyle(self) -> None:
        ...
    def ApplyCfw(self) -> None:
        ...
    Color: NXColor
    Font: Annotations.EditSymbolDisplayBuilder.FontTypes
    Style: Annotations.StyleBuilder
    Width: Annotations.EditSymbolDisplayBuilder.WidthTypes


    class WidthTypes(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        ThicknessOne = 6
        ThicknessTwo = 7
        ThicknessThree = 8
        ThicknessFour = 9
        ThicknessFive = 10
        ThicknessSix = 11
        ThicknessSeven = 12
        ThicknessEight = 13
        ThicknessNine = 14
    

    class FontTypes(enum.Enum):
        Solid = 0
        Dashed = 1
        Phantom = 2
        Centerline = 3
        Dotted = 4
        LongDashed = 5
        DottedDashed = 6
        Eight = 7
        Nine = 8
        Ten = 9
        Eleven = 10
    

class EditSettingsBuilder(Drafting.BaseEditSettingsBuilder):
    def __init__(self) -> None: ...
    def InheritSettingsFromSelectedObjects(self, selectedObject: DisplayableObject) -> None:
        ...
    def InheritSettingsFromCustomerDefault(self) -> None:
        ...
    def InheritSettingsFromPreferences(self) -> None:
        ...
    AnnotationStyle: Annotations.StyleBuilder
    DrawingFormatTitle: Annotations.DrawingFormatTitleBuilder
    ViewProjectedArrowSettings: Drawings.ViewProjectedArrowSettingsBuilder


class EditLeaderBuilder(Builder):
    def __init__(self) -> None: ...
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder


class EdgeConditionSymbolCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.EdgeConditionSymbol]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateEdgeConditionSymbolBuilder(self, annotation: Annotations.EdgeConditionSymbol) -> Annotations.EdgeConditionSymbolBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.EdgeConditionSymbol:
        ...
    def Tag(self) -> Tag: ...



class EdgeConditionSymbolBuilder(Annotations.BaseEdgeConditionSymbolBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class EdgeConditionSymbol(Annotations.BaseEdgeConditionSymbol):
    def __init__(self) -> None: ...


class DualDimensionPlacement(enum.Enum):
    Below = 0
    After = 1
    Above = 2
    Before = 3
    None = 4
    Last = 5


class DrivingValueBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DimensionValue: float
    DrivingMethod: Annotations.DrivingValueBuilder.DrivingValueMethod
    ExpressionMode: Annotations.DrivingValueBuilder.DrivingExpressionMode
    ExpressionName: str
    ExpressionValue: Expression
    Reference: bool


    class DrivingValueMethod(enum.Enum):
        Inferred = 0
        Driving = 1
        Reference = 2
        Constant = 3
    

    class DrivingExpressionMode(enum.Enum):
        MeasureGeometry = 0
        KeepExpression = 1
    

class DrawingFormatTitleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Automatic: bool
    TitleBlockAlignmentPosition: Annotations.DrawingFormatTitleBuilder.TitleBlockPositionType


    class TitleBlockPositionType(enum.Enum):
        TopLeft = 0
        TopRight = 1
        BottomLeft = 2
        BottomRight = 3
    

class DraftingSurfaceFinishCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.DraftingSurfaceFinish]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDraftingSurfaceFinishBuilder(self, draftingSurfaceFinish: Annotations.DraftingSurfaceFinish) -> Annotations.DraftingSurfaceFinishBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.DraftingSurfaceFinish:
        ...
    def Tag(self) -> Tag: ...



class DraftingSurfaceFinishBuilder(Annotations.BaseSurfaceFinishBuilder):
    def __init__(self) -> None: ...
    def InheritFrom(self, inheritTag: Annotations.BaseSurfaceFinish) -> None:
        ...
    A1: str
    A2: str
    Angle: float
    B: str
    C: str
    D: str
    E: str
    F1: str
    F2: str
    Finish: Annotations.DraftingSurfaceFinishBuilder.FinishType
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder
    InvertSymbol: bool
    InvertText: bool
    LowerTolerance: float
    Parantheses: Annotations.BaseSurfaceFinishBuilder.ParanthesesType
    Parentheses: Annotations.BaseSurfaceFinishBuilder.ParenthesesType
    SingleRoughnessValue: bool
    Tolerance: float
    ToleranceType: Annotations.BaseSurfaceFinishBuilder.ToleranceOption


    class FinishType(enum.Enum):
        Basic = 0
        Modifier = 1
        ModifierAllAround = 2
        MaterialRemovalRequired = 3
        ModifierMaterialRemovalRequired = 4
        ModifierMaterialRemovalRequiredAllAround = 5
        MaterialRemovalProhibited = 6
        ModifierMaterialRemovalProhibited = 7
        ModifierMaterialRemovalProhibitedAllAround = 8
    

class DraftingSurfaceFinish(Annotations.BaseSurfaceFinish):
    def __init__(self) -> None: ...


class DraftingPointTarget(Annotations.DraftingDatumTarget):
    def __init__(self) -> None: ...
    PointCoordinates: Point3d


class DraftingNoteBuilder(Builder):
    def __init__(self) -> None: ...
    def InheritProperties(self, annotation: Annotations.SimpleDraftingAid, recordNumber: int) -> None:
        ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder
    Inherit: SelectDisplayableObject
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder
    Text: Annotations.TextWithEditControlsBuilder
    TextAlignment: Annotations.DraftingNoteBuilder.TextAlign
    VerticalText: bool


    class ThicknessTypes(enum.Enum):
        Medium = 0
        Thick = 1
    

    class TextAlign(enum.Enum):
        Top = 0
        Middle = 1
        Bottom = 2
        BelowbottomExtToMax = 3
        BelowbottomExtToMaxUnderline = 4
        Belowbottom = 5
        BelowbottomUnderline = 6
        BelowTopExtToMax = 7
        BelowTopExtToMaxUnderline = 8
        BelowTop = 9
        BelowTopUnderline = 10
    

class DraftingLineTarget(Annotations.DraftingDatumTarget):
    def __init__(self) -> None: ...
    EndPointCoordinates: Point3d
    StartPointCoordinates: Point3d


class DraftingImageCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.DraftingImage]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Annotations.DraftingImage:
        ...
    def CreateDraftingImageBuilder(self, image: Annotations.DraftingImage) -> Annotations.DraftingImageBuilder:
        ...
    def CreateRasterImageBuilder(self, image: Annotations.RasterImage) -> Annotations.RasterImageBuilder:
        ...
    def Tag(self) -> Tag: ...



class DraftingImageBuilder(Builder):
    def __init__(self) -> None: ...
    Image: Annotations.RasterImageBuilder


class DraftingImage(Annotations.Annotation):
    def __init__(self) -> None: ...
    def GetFileType(self) -> Annotations.DraftingImage.FileType:
        ...
    def ExportFile(self, fileExist: bool) -> str:
        ...


    class FileType(enum.Enum):
        Png = 0
        Jpg = 1
        Tif = 2
    

class DraftingFeatureControlFrameBuilder(Annotations.FeatureControlFrameBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class DraftingFcf(Annotations.BaseFcf):
    def __init__(self) -> None: ...


class DraftingDatumTargetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.DraftingDatumTarget]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Annotations.DraftingDatumTarget:
        ...
    def Tag(self) -> Tag: ...



class DraftingDatumTargetBuilder(Annotations.DatumTargetBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class DraftingDatumTarget(Annotations.BaseDatumTarget):
    def __init__(self) -> None: ...
    def ConvertToPointTarget(self) -> Annotations.PointTarget:
        ...
    def ConvertToLineTarget(self) -> Annotations.LineTarget:
        ...
    def ConvertToAreaTarget(self) -> Annotations.ArbitraryTarget:
        ...
    def ConvertToDraftingPointTarget(self) -> Annotations.DraftingPointTarget:
        ...
    def ConvertToDraftingLineTarget(self) -> Annotations.DraftingLineTarget:
        ...
    def ConvertToDraftingAreaTarget(self) -> Annotations.DraftingArbitraryTarget:
        ...


class DraftingDatumFeatureSymbolBuilder(Annotations.DatumFeatureSymbolBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class DraftingDatum(Annotations.BaseDatum):
    def __init__(self) -> None: ...


class DraftingCustomSymbolBuilder(Annotations.BaseCustomSymbolBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class DraftingArbitraryTarget(Annotations.DraftingDatumTarget):
    def __init__(self) -> None: ...
    UpperText: str


class DraftingAid(Annotations.Annotation):
    def __init__(self) -> None: ...


class DisplayStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BackgroundColor: int
    EnableBackground: bool
    LockSizeAndPosition: bool
    ParallelToScreen: bool


class DisplayPmiEffectivityMethod(enum.Enum):
    AllAssocOccLoaded = 1
    AnyAssocOccLoaded = 2


class DimensionWorkflowBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AutomaticCreationIntersectionSymbol: bool
    EnableDirectedDimension: bool
    HoverSceneDialogDelay: int


class DimensionUnit(enum.Enum):
    Millimeters = 0
    Meters = 1
    Inches = 2
    ArchitecturalFeetInches = 3
    EngineeringFeetInches = 4
    Last = 5


class DimensionType(enum.Enum):
    AngularMajor = 0
    AngularMinor = 1
    ArcLength = 2
    Baseline = 3
    Chain = 4
    Chamfer = 5
    ConcentricCircle = 6
    Cylindrical = 7
    Diameter = 8
    FoldedRadius = 9
    Hole = 10
    Horizontal = 11
    OrdinateHorizontal = 12
    OrdinateOrigin = 13
    OrdinateVertical = 14
    Parallel = 15
    Perpendicular = 16
    Radius = 17
    Vertical = 18
    Last = 19


class DimensionTextFormat(enum.Enum):
    Decimal = 0
    HalfSizeFraction = 1
    TwoThirdSizeFraction = 2
    FullSizeFraction = 3
    Last = 4


class DimensionStyleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetOverriddenDimensionText(self) -> str:
        ...
    def SetOverriddenDimensionText(self, customizedText: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AngularDimensionValuePrecision: int
    AngularToleranceValuePrecision: int
    BaselineOffset: float
    ChainOffset: float
    ChamferForm: Annotations.ChamferForm
    ChamferLeaderType: Annotations.ChamferLeaderPlacement
    ChamferSeparator: Annotations.ChamferSeparatorType
    ChamferSpaceFactor: float
    ChamferStubType: Annotations.ChamferStubType
    ChamferSymbolName: str
    ChamferSymbolType: Annotations.ChamferSymbolPlacement
    DimArrowDisplay: Annotations.ArrowDisplay
    DimZeroToleranceDisplayStyle: Annotations.ZeroToleranceDisplayStyle
    DimensionReferenceIncludeType: Annotations.ReferenceIncludeType
    DimensionValuePrecision: int
    DualDimensionFractionDenominator: Annotations.FractionDenominatorFormat
    DualDimensionValuePrecision: int
    DualToleranceValuePrecision: int
    ExtensionLineDisplay: Annotations.ExtensionLineDisplay
    FitToleranceParentheses: bool
    FitToleranceSeparator: bool
    InspectionDimension: bool
    InspectionSymbolAroundAppendedText: Annotations.InspectionSymbolAroundAppendedText
    LimitFitAnsiHoleType: Annotations.FitAnsiHoleType
    LimitFitAssemblyDisplayStyle: Annotations.FitAssemblyDisplayStyle
    LimitFitAssemblyNewDisplayStyle: Annotations.FitAssemblyNewDisplayStyle
    LimitFitDeviation: str
    LimitFitDisplayAlignment: Annotations.FitDisplayAlignment
    LimitFitDisplaySplitByDimline: Annotations.FitDisplaySplitByDimline
    LimitFitDisplayStyle: Annotations.FitDisplayStyle
    LimitFitGrade: int
    LimitFitShaftDeviation: str
    LimitFitShaftGrade: int
    LineBetweenArrows: bool
    LowerToleranceDegrees: float
    LowerToleranceEnglish: float
    LowerToleranceMetric: float
    NarrowArrowType: Annotations.ArrowheadType
    NarrowDisplayType: Annotations.NarrowDisplayOption
    NarrowLeaderAngle: float
    NarrowTextOffset: float
    NarrowTextOrientation: Annotations.NarrowTextOrientation
    Orientation: Annotations.TextOrientation
    OverrideDimensionText: bool
    PrefixSuffixReference: bool
    PrimaryDimensionFractionDenominator: Annotations.FractionDenominatorFormat
    ReferenceDimension: bool
    ReferenceDimensionPrefix: str
    ReferenceDimensionSuffix: str
    ReverseArrowDirection: bool
    ShowAsReferenceDimension: bool
    TextAngle: float
    TextArrowPlacement: Annotations.TextPlacement
    TextCentered: bool
    TextPosition: Annotations.TextPosition
    ToleranceType: Annotations.ToleranceType
    ToleranceValuePrecision: int
    TrimDimLine: Annotations.TrimDimensionLineStyle
    TrueLengthText: str
    TrueLengthTextPosition: Annotations.TrueLengthTextPosition
    UpperToleranceDegrees: float
    UpperToleranceEnglish: float
    UpperToleranceMetric: float


class DimensionSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.DimensionSet]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHorizontalBaselineDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.BaselineDimension:
        ...
    def CreatePmiHorizontalBaselineDimension(self, dimensionData: Annotations.DimensionData, pmidata: typing.List[Annotations.PmiData], annotationPlane: Xform, origin: Point3d) -> Annotations.PmiBaselineDimension:
        ...
    def CreateVerticalBaselineDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.BaselineDimension:
        ...
    def CreatePmiVerticalBaselineDimension(self, dimensionData: Annotations.DimensionData, pmidata: typing.List[Annotations.PmiData], annotationPlane: Xform, origin: Point3d) -> Annotations.PmiBaselineDimension:
        ...
    def CreateHorizontalChainDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.ChainDimension:
        ...
    def CreatePmiHorizontalChainDimension(self, dimensionData: Annotations.DimensionData, pmidata: typing.List[Annotations.PmiData], annotationPlane: Xform, origin: Point3d) -> Annotations.PmiChainDimension:
        ...
    def CreateVerticalChainDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.ChainDimension:
        ...
    def CreatePmiVerticalChainDimension(self, dimensionData: Annotations.DimensionData, pmidata: typing.List[Annotations.PmiData], annotationPlane: Xform, origin: Point3d) -> Annotations.PmiChainDimension:
        ...
    def Tag(self) -> Tag: ...



class DimensionSetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DimensionOrSet: Annotations.SelectAnnotation
    Method: Annotations.DimensionSetBuilder.DimensionSetMethod


    class DimensionSetMethod(enum.Enum):
        None = 0
        Chain = 1
        Baseline = 2
    

class DimensionSet(Annotations.Annotation):
    def __init__(self) -> None: ...
    def AddDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d, autoAdjustNarrowDim: bool) -> Annotations.Dimension:
        ...
    def AddPmiDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, origin: Point3d, autoAdjustNarrowDim: bool) -> Annotations.Dimension:
        ...
    def AddPmiDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, autoAdjustNarrowDim: bool) -> Annotations.Dimension:
        ...
    def ReverseOffset(self) -> None:
        ...
    def GetAllSubDimensions(self) -> typing.List[Annotations.Dimension]:
        ...
    def GetObjects(self) -> typing.List[NXObject]:
        ...
    def RemoveObject(self, object: NXObject) -> None:
        ...
    DimensionOffset: float


class DimensionPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetUnitsFormatPreferences(self) -> Annotations.UnitsFormatPreferences:
        ...
    def SetUnitsFormatPreferences(self, preferences: Annotations.UnitsFormatPreferences) -> None:
        ...
    def GetNarrowDimensionPreferences(self) -> Annotations.NarrowDimensionPreferences:
        ...
    def SetNarrowDimensionPreferences(self, preferences: Annotations.NarrowDimensionPreferences) -> None:
        ...
    def GetDiameterRadiusPreferences(self) -> Annotations.DiameterRadiusPreferences:
        ...
    def SetDiameterRadiusPreferences(self, preferences: Annotations.DiameterRadiusPreferences) -> None:
        ...
    def GetChamferDimensionPreferences(self) -> Annotations.ChamferDimensionPreferences:
        ...
    def SetChamferDimensionPreferences(self, preferences: Annotations.ChamferDimensionPreferences) -> None:
        ...
    def GetOrdinateDimensionPreferences(self) -> Annotations.OrdinateDimensionPreferences:
        ...
    def SetOrdinateDimensionPreferences(self, preferences: Annotations.OrdinateDimensionPreferences) -> None:
        ...
    ArrowDisplay: Annotations.ArrowDisplay
    BaselineOffset: float
    ChainOffset: float
    DisplayFitParentheses: bool
    DisplayFitSeparator: bool
    DisplayLineBetweenArrows: bool
    DualDimensionFractionDenominator: Annotations.FractionDenominatorFormat
    ExtensionLineDisplay: Annotations.ExtensionLineDisplay
    IsInspectionDimension: bool
    IsReferenceDimension: bool
    LimitFitAnsiHoleType: Annotations.FitAnsiHoleType
    LimitFitAssemblyDisplayStyle: Annotations.FitAssemblyDisplayStyle
    LimitFitAssemblyNewDisplayStyle: Annotations.FitAssemblyNewDisplayStyle
    LimitFitDeviation: str
    LimitFitDisplayAlignment: Annotations.FitDisplayAlignment
    LimitFitDisplaySplitByDimline: Annotations.FitDisplaySplitByDimline
    LimitFitDisplayStyle: Annotations.FitDisplayStyle
    LimitFitGrade: int
    LimitFitShaftDeviation: str
    LimitFitShaftGrade: int
    PrefixSuffixReference: bool
    PrimaryDimensionFractionDenominator: Annotations.FractionDenominatorFormat
    ReferenceDimensionPrefix: str
    ReferenceDimensionSuffix: str
    ReverseArrowDirection: bool
    TextOrienationAngle: float
    TextOrientation: Annotations.TextOrientation
    TextPlacement: Annotations.TextPlacement
    TextPosition: Annotations.TextPosition
    TrimDimensionLineStyle: Annotations.TrimDimensionLineStyle
    TrueLengthText: str
    TrueLengthTextPosition: Annotations.TrueLengthTextPosition
    ZeroToleranceDisplayStyle: Annotations.ZeroToleranceDisplayStyle


class DimensionMeasurementBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Direction: Direction
    DirectionView: View
    Method: Annotations.DimensionMeasurementBuilder.MeasurementMethod
    PartOccurrence: Assemblies.Component
    SecondaryCalloutActive: bool


    class MeasurementMethod(enum.Enum):
        Inferred = 0
        Horizontal = 1
        Vertical = 2
        PointToPoint = 3
        Perpendicular = 4
        Cylindrical = 5
        Angular = 6
        Radial = 7
        Diametral = 8
        HoleCallout = 9
    

class DimensionData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetAssociativity(self, associativityIndex: int) -> typing.List[Annotations.Associativity]:
        ...
    def SetAssociativity(self, associativityIndex: int, associativity: typing.List[Annotations.Associativity]) -> None:
        ...
    def GetDimensionPreferences(self) -> Annotations.DimensionPreferences:
        ...
    def SetDimensionPreferences(self, preferences: Annotations.DimensionPreferences) -> None:
        ...
    def GetLineAndArrowPreferences(self) -> Annotations.LineAndArrowPreferences:
        ...
    def SetLineAndArrowPreferences(self, prefs: Annotations.LineAndArrowPreferences) -> None:
        ...
    def GetLetteringPreferences(self) -> Annotations.LetteringPreferences:
        ...
    def SetLetteringPreferences(self, letteringPrefs: Annotations.LetteringPreferences) -> None:
        ...
    def GetUserSymbolPreferences(self) -> Annotations.UserSymbolPreferences:
        ...
    def SetUserSymbolPreferences(self, userSymbolPrefs: Annotations.UserSymbolPreferences) -> None:
        ...
    def GetAppendedText(self) -> Annotations.AppendedText:
        ...
    def SetAppendedText(self, appendedText: Annotations.AppendedText) -> None:
        ...
    def GetInferredPlane(self, jaDefaultPlane: Annotations.PmiDefaultPlane, dimType: Annotations.DimensionType) -> Xform:
        ...
    def GetLinearTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetLinearTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetAngularTolerance(self) -> Annotations.AngularTolerance:
        ...
    def SetAngularTolerance(self, tolerance: Annotations.AngularTolerance) -> None:
        ...
    LeaderOrientation: Annotations.LeaderOrientation
    MeasurementDirection: Direction
    MeasurementDirectionView: View


class DimensionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Dimension]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateMajorAngularDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.MajorAngularDimension:
        ...
    def CreatePmiMajorAngularDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiMajorAngularDimension:
        ...
    def CreateMinorAngularDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.MinorAngularDimension:
        ...
    def CreatePmiMinorAngularDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiMinorAngularDimension:
        ...
    def CreateArcLengthDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.ArcLengthDimension:
        ...
    def CreatePmiArcLengthDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiArcLengthDimension:
        ...
    def CreateChamferDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.ChamferDimension:
        ...
    def CreatePmiChamferDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiChamferDimension:
        ...
    def CreateConcentricCircleDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.ConcentricCircleDimension:
        ...
    def CreatePmiConcentricCircleDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiConcentricCircleDimension:
        ...
    def CreateCylindricalDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.CylindricalDimension:
        ...
    def CreatePmiCylindricalDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiCylindricalDimension:
        ...
    def CreateDiameterDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.DiameterDimension:
        ...
    def CreatePmiDiameterDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiDiameterDimension:
        ...
    def CreateFoldedRadiusDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.FoldedRadiusDimension:
        ...
    def CreatePmiFoldedRadiusDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiFoldedRadiusDimension:
        ...
    def CreateHoleDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.HoleDimension:
        ...
    def CreatePmiHoleDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiHoleDimension:
        ...
    def CreateHorizontalDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.HorizontalDimension:
        ...
    def CreatePmiHorizontalDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiHorizontalDimension:
        ...
    def CreateHorizontalOrdinateDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.HorizontalOrdinateDimension:
        ...
    def CreatePmiHorizontalOrdinateDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiHorizontalOrdinateDimension:
        ...
    def CreateParallelDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.ParallelDimension:
        ...
    def CreatePmiParallelDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiParallelDimension:
        ...
    def CreatePerpendicularDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.PerpendicularDimension:
        ...
    def CreatePmiPerpendicularDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiPerpendicularDimension:
        ...
    def CreateRadiusDimension(self, dimensionData: Annotations.DimensionData, radiusType: Annotations.RadiusDimensionType, origin: Point3d) -> Annotations.RadiusDimension:
        ...
    def CreatePmiRadiusDimension(self, dimensionData: Annotations.DimensionData, radiusType: Annotations.RadiusDimensionType, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiRadiusDimension:
        ...
    def CreateVerticalDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.VerticalDimension:
        ...
    def CreatePmiVerticalDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiVerticalDimension:
        ...
    def CreateVerticalOrdinateDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.VerticalOrdinateDimension:
        ...
    def CreatePmiVerticalOrdinateDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiVerticalOrdinateDimension:
        ...
    def CreateOrdinateOriginDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d) -> Annotations.OrdinateOriginDimension:
        ...
    def CreatePmiOrdinateOriginDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d) -> Annotations.PmiOrdinateOriginDimension:
        ...
    def CreateHorizontalOrdinateAutoDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d, allowDuplicate: bool, repositionDim: bool) -> None:
        ...
    def CreatePmiHorizontalOrdinateAutoDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, allowDuplicate: bool, repositionDim: bool) -> None:
        ...
    def CreateVerticalOrdinateAutoDimension(self, dimensionData: Annotations.DimensionData, origin: Point3d, allowDuplicate: bool, repositionDim: bool) -> None:
        ...
    def CreatePmiVerticalOrdinateAutoDimension(self, dimensionData: Annotations.DimensionData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, allowDuplicate: bool, repositionDim: bool) -> None:
        ...
    def CreateThicknessDimensionBuilder(self, thicknessDimension: Annotations.BaseConcentricCircleDimension) -> Annotations.ThicknessDimensionBuilder:
        ...
    def CreatePmiThicknessDimensionBuilder(self, thicknessDimension: Annotations.PmiConcentricCircleDimension) -> Annotations.PmiThicknessDimensionBuilder:
        ...
    def CreateCurveLengthDimensionBuilder(self, curveLengthDimension: Annotations.BaseArcLengthDimension) -> Annotations.CurveLengthDimensionBuilder:
        ...
    def CreatePmiCurveLengthDimensionBuilder(self, curveLengthDimension: Annotations.PmiArcLengthDimension) -> Annotations.PmiCurveLengthDimensionBuilder:
        ...
    def CreateChamferDimensionBuilder(self, chamferDimension: Annotations.BaseChamferDimension) -> Annotations.ChamferDimensionBuilder:
        ...
    def CreatePmiChamferDimensionBuilder(self, chamferDimension: Annotations.PmiChamferDimension) -> Annotations.PmiChamferDimensionBuilder:
        ...
    def CreateLinearDimensionBuilder(self, linearDimension: Annotations.Dimension) -> Annotations.LinearDimensionBuilder:
        ...
    def CreatePmiLinearDimensionBuilder(self, linearDimension: Annotations.Dimension) -> Annotations.PmiLinearDimensionBuilder:
        ...
    def CreateRadialDimensionBuilder(self, radialDimension: Annotations.Dimension) -> Annotations.RadialDimensionBuilder:
        ...
    def CreatePmiRadialDimensionBuilder(self, radialDimension: Annotations.Dimension) -> Annotations.PmiRadialDimensionBuilder:
        ...
    def CreateRapidDimensionBuilder(self, rapidDimension: Annotations.Dimension) -> Annotations.RapidDimensionBuilder:
        ...
    def CreatePmiRapidDimensionBuilder(self, rapidDimension: Annotations.Dimension) -> Annotations.PmiRapidDimensionBuilder:
        ...
    def CreateAngularDimensionBuilder(self, angularDimension: Annotations.BaseAngularDimension) -> Annotations.AngularDimensionBuilder:
        ...
    def CreateMajorAngularDimensionBuilder(self, angularDimension: Annotations.BaseAngularDimension) -> Annotations.MajorAngularDimensionBuilder:
        ...
    def CreateMinorAngularDimensionBuilder(self, angularDimension: Annotations.BaseAngularDimension) -> Annotations.MinorAngularDimensionBuilder:
        ...
    def CreatePmiAngularDimensionBuilder(self, angularDimension: Annotations.Dimension) -> Annotations.PmiAngularDimensionBuilder:
        ...
    def CreatePmiMajorAngularDimensionBuilder(self, angularDimension: Annotations.BaseAngularDimension) -> Annotations.PmiMajorAngularDimensionBuilder:
        ...
    def CreatePmiMinorAngularDimensionBuilder(self, angularDimension: Annotations.BaseAngularDimension) -> Annotations.PmiMinorAngularDimensionBuilder:
        ...
    def CreateOrdinateDimensionBuilder(self, ordinateDimension: Annotations.OrdinateDimension) -> Annotations.OrdinateDimensionBuilder:
        ...
    def CreatePmiOrdinateDimensionBuilder(self, ordinateDimension: Annotations.OrdinateDimension) -> Annotations.PmiOrdinateDimensionBuilder:
        ...
    def CreateAppendedTextEditorBuilder(self, dimension: Annotations.Dimension) -> Annotations.AppendedTextEditorBuilder:
        ...
    def CreateGeodesicDimensionBuilder(self, dimension: Annotations.Dimension) -> Annotations.GeodesicDimensionBuilder:
        ...
    def Tag(self) -> Tag: ...



class Dimension(Annotations.Annotation):
    def __init__(self) -> None: ...
    def GetDimensionPreferences(self) -> Annotations.DimensionPreferences:
        ...
    def SetDimensionPreferences(self, preferences: Annotations.DimensionPreferences) -> None:
        ...
    def SetNarrowDimensionTextOffset(self, narrowTextOffset: float) -> None:
        ...
    def GetNarrowDimensionTextOffset(self) -> float:
        ...
    def SetNarrowDimensionPreferences(self, narrowDimensionData: Annotations.NarrowDimensionData) -> None:
        ...
    def GetNarrowDimensionPreferences(self) -> Annotations.NarrowDimensionData:
        ...
    def GetFirstAssociativity(self) -> Annotations.Associativity:
        ...
    def SetFirstAssociativity(self, newAssociativity: Annotations.Associativity) -> None:
        ...
    def GetSecondAssociativity(self) -> Annotations.Associativity:
        ...
    def SetSecondAssociativity(self, newAssociativity: Annotations.Associativity) -> None:
        ...
    def SetComputedSize(self, computedSize: float) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Annotations.Dimension.SetDimensionText instead.")"""
        ...
    def IsDriving(self) -> bool:
        ...
    def SetDimensionText(self, mainTextLines: str) -> None:
        ...
    def GetDimensionText(self, mainTextLines: str, dualTextLines: str) -> None:
        ...
    def IsApproximate(self) -> bool:
        ...
    def GetMeasurementType(self) -> Annotations.Dimension.MeasurementTypes:
        ...
    def UnretainForInconsistentSilhouette(self, index: int) -> None:
        ...
    def GetAppendedText(self) -> Annotations.AppendedText:
        ...
    def SetAppendedText(self, appendedText: Annotations.AppendedText) -> None:
        ...
    ComputedSize: float
    InspectionDimensionFlag: bool
    IsOriginCentered: bool
    LimitFitAnsiHoleType: Annotations.FitAnsiHoleType
    LimitFitDeviation: str
    LimitFitDisplayStyle: Annotations.FitDisplayStyle
    LimitFitEnhancedDisplayType: Annotations.FitAnsiHoleType
    LimitFitGrade: int
    LimitFitShaftDeviation: str
    LimitFitShaftGrade: int
    LowerMetricToleranceValue: float
    LowerToleranceValue: float
    MeasurementDirection: Direction
    MeasurementDirectionView: View
    MetricNominalDecimalPlaces: int
    MetricToleranceDecimalPlaces: int
    NominalDecimalPlaces: int
    ReferenceDimensionFlag: bool
    ShaftLowerToleranceValue: float
    ShaftUpperToleranceValue: float
    ToleranceDecimalPlaces: int
    ToleranceType: Annotations.ToleranceType
    UpperMetricToleranceValue: float
    UpperToleranceValue: float


    class MeasurementTypes(enum.Enum):
        General = 0
        Directed = 1
        FeatureOfSize = 2
    

class DiameterSymbol(enum.Enum):
    Dia = 0
    Standard = 1
    UserDefined = 2
    Spherical = 3
    Last = 4


class DiameterRadiusSymbolPlacement(enum.Enum):
    Below = 0
    Above = 1
    After = 2
    Before = 3
    Omit = 4
    Last = 5


class DiameterRadiusPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DiameterSymbol: Annotations.DiameterSymbol
    DiameterSymbolText: str
    DistanceBetweenSymbolAndDimensionText: float
    FoldedRadiusAngle: float
    LeaderStub: Annotations.DiameterRadiusLeaderStub
    RadiusSymbol: Annotations.RadiusSymbol
    RadiusSymbolText: str
    SymbolPlacement: Annotations.DiameterRadiusSymbolPlacement


class DiameterRadiusLeaderStub(enum.Enum):
    Before = 0
    Below = 1
    Last = 2


class DiameterDimension(Annotations.BaseDiameterDimension):
    def __init__(self) -> None: ...


class DefineTitleBlockBuilder(Annotations.BaseTitleBlockBuilder):
    def __init__(self) -> None: ...
    def UpdateCells(self) -> None:
        ...
    Components: Annotations.SelectTableSectionList
    Origin: Point3d


class DecimalPointCharacter(enum.Enum):
    Period = 0
    Comma = 1
    Last = 2


class DatumTargetData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSimpleDraftingAidPreferences(self) -> Annotations.SimpleDraftingAidPreferences:
        ...
    def SetSimpleDraftingAidPreferences(self, preferences: Annotations.SimpleDraftingAidPreferences) -> None:
        ...
    DatumLabel: str
    Index: int


class DatumTargetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.DatumTarget]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def NewTargetData(self) -> Annotations.DatumTargetData:
        ...
    def NewRectangularTargetData(self) -> Annotations.RectangularTargetData:
        ...
    def NewCircularTargetData(self) -> Annotations.CircularTargetData:
        ...
    def NewArbitraryTargetData(self) -> Annotations.ArbitraryTargetData:
        ...
    def CreatePointTarget(self, targetData: Annotations.DatumTargetData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.PointTarget:
        ...
    def CreatePointTarget(self, targetData: Annotations.DatumTargetData, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.DraftingPointTarget:
        ...
    def CreateLineTarget(self, targetData: Annotations.DatumTargetData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.LineTarget:
        ...
    def CreateLineTarget(self, targetData: Annotations.DatumTargetData, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.DraftingLineTarget:
        ...
    def CreateRectangularTarget(self, targetData: Annotations.RectangularTargetData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.RectangularTarget:
        ...
    def CreateCircularTarget(self, targetData: Annotations.CircularTargetData, data: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.CircularTarget:
        ...
    def CreateArbitraryTarget(self, targetData: Annotations.ArbitraryTargetData, data: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.ArbitraryTarget:
        ...
    def CreateArbitraryTarget(self, targetData: Annotations.ArbitraryTargetData, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.DraftingArbitraryTarget:
        ...
    def Tag(self) -> Tag: ...



class DatumTargetBuilder(Builder):
    def __init__(self) -> None: ...
    def InheritFrom(self, inheritTag: Annotations.BaseDatumTarget) -> None:
        ...
    def ReverseMovableModifier(self) -> None:
        ...
    AreaSize: str
    DatumTargetStandard: Annotations.DatumTargetBuilder.StandardTypes
    DrawX: bool
    Height: Expression
    Index: int
    InnerDiameter: Expression
    Label: str
    Leader: Annotations.LeaderBuilder
    Movable: bool
    MovableModifierAngle: Expression
    Origin: Annotations.OriginBuilder
    OuterDiameter: Expression
    Style: Annotations.StyleBuilder
    TerminatorType: Annotations.DatumTargetBuilder.TerminatorTypes
    Type: Annotations.DatumTargetBuilder.Types
    Width: Expression


    class Types(enum.Enum):
        Point = 0
        Line = 1
        Rectangular = 2
        Circular = 3
        Annular = 4
        Spherical = 5
        Cylindrical = 6
        Arbitrary = 7
    

    class TerminatorTypes(enum.Enum):
        Arrow = 0
        X = 1
        Plus = 2
    

    class StandardTypes(enum.Enum):
        NoStandard = 0
        AsmeY145m1982 = 1
        AsmeY145m1994 = 2
        AsmeIso11011983 = 3
        GmAddendum94 = 4
        Asig2000 = 5
        AsmeY1452009 = 6
    

class DatumTarget(Annotations.DraftingDatumTarget):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class DatumReferenceBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.DatumReferenceBuilder]) -> None:
        ...
    def Append(self, object: Annotations.DatumReferenceBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.DatumReferenceBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.DatumReferenceBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.DatumReferenceBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.DatumReferenceBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.DatumReferenceBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.DatumReferenceBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.DatumReferenceBuilder, object2: Annotations.DatumReferenceBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.DatumReferenceBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DatumReferenceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    FreeState: bool
    Letter: str
    MaterialCondition: Annotations.DatumReferenceBuilder.DatumReferenceMaterialCondition
    Projected: bool


    class DatumReferenceMaterialCondition(enum.Enum):
        None = 0
        LeastMaterialCondition = 1
        MaximumMaterialCondition = 2
        RegardlessOfFeatureSize = 3
    

class DatumReference(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetMaterialConditionModifiers(self) -> typing.List[Annotations.MaterialConditionModifier]:
        ...
    def SetMaterialConditionModifiers(self, modifiers: typing.List[Annotations.MaterialConditionModifier]) -> None:
        ...
    DatumLabel: str


class DatumFeatureSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    def InheritFrom(self, inheritTag: Annotations.BaseDatum) -> None:
        ...
    Leader: Annotations.LeaderBuilder
    Letter: str
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder


class DatumData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSimpleDraftingAidPreferences(self) -> Annotations.SimpleDraftingAidPreferences:
        ...
    def SetSimpleDraftingAidPreferences(self, preferences: Annotations.SimpleDraftingAidPreferences) -> None:
        ...
    AlwaysVertical: bool
    DrawX: bool
    Label: str


class Datum(Annotations.DraftingDatum):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class CylindricalDimension(Annotations.BaseCylindricalDimension):
    def __init__(self) -> None: ...


class CuttingPlaneSymbolBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def AlternateArrow(self) -> None:
        ...
    def AlternateArrowRotation(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ArrowDirection: Annotations.CuttingPlaneSymbolBuilder.ArrowDirectionOption
    ArrowLength: float
    Color: int
    CuttingPlaneSymbolText: str
    DisplayCuttingPlaneSymbol: bool
    Font: LineFontBuilder
    MarginPercentage: float
    ShadedPlane: bool
    SizeBasedOnSectionCut: bool
    Style: Annotations.StyleBuilder
    TextPlaneRelativeToArrow: Annotations.CuttingPlaneSymbolBuilder.TextPlaneRelativeArrow
    UseTwoArrows: bool
    ViewNameFormat: Annotations.CuttingPlaneSymbolBuilder.ViewNameFormatOption


    class ViewNameFormatOption(enum.Enum):
        UserDefined = 0
        A = 1
        AA = 2
    

    class TextPlaneRelativeArrow(enum.Enum):
        Parallel = 0
        Perpendicular = 1
    

    class ArrowDirectionOption(enum.Enum):
        Towards = 0
        Away = 1
    

class CuttingPlaneSymbol(Annotations.Annotation):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    SectionView: View
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class CutSheetBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AutoUpdate: bool
    FlattenHierarchy: bool


class CustomSymbolUtils(Utilities.NXRemotableObject):
    def GetSymbolList(self, path: str, subFolderNames: str, symbolNames: str, symbolIcons: str) -> None:
        ...
    def __init__(self) -> None: ...


class CustomSymbolTextData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolListItemBuilder instead. Use NXOpen.Annotations.BaseCustomSymbolBuilder.Texts to query list of custom symbol texts.")"""
        ...
    def GetText(self) -> str:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolListItemBuilder instead. Use NXOpen.Annotations.BaseCustomSymbolBuilder.Texts to query list of custom symbol texts.")"""
        ...
    def SetText(self, lines: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolListItemBuilder instead. Use NXOpen.Annotations.BaseCustomSymbolBuilder.Texts to query list of custom symbol texts.")"""
        ...
    ControlTextIndex: int
    IntegerValue: int
    RealValue: float
    StringValue: str
    TextType: Annotations.TextType


class CustomSymbolLeaderBuilder(Builder):
    def __init__(self) -> None: ...
    Leader: Annotations.LeaderBuilder
    Origin: Annotations.OriginBuilder


class CustomSymbolData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder for Drafting Custom Symbol and NXOpen.Annotations.PmiCustomSymbolBuilder for PMI Custom Symbol objects.")"""
        ...
    def GetTextData(self) -> typing.List[Annotations.CustomSymbolTextData]:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder for Drafting Custom Symbol and NXOpen.Annotations.PmiCustomSymbolBuilder for PMI Custom Symbol objects.")"""
        ...
    def SetTextData(self, data: typing.List[Annotations.CustomSymbolTextData]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder for Drafting Custom Symbol and NXOpen.Annotations.PmiCustomSymbolBuilder for PMI Custom Symbol objects.")"""
        ...
    Angle: float
    Scale: float
    ScaleExpression: Expression
    SymbolPreferencesOption: Annotations.SymbolPreferencesOption
    TextPreferencesOption: Annotations.TextPreferencesOption


class CustomSymbolCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.BaseCustomSymbol]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def NewCustomSymbolData(self, masterFileName: str) -> Annotations.CustomSymbolData:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder for Drafting Custom Symbol and NXOpen.Annotations.PmiCustomSymbolBuilder for PMI Custom Symbol objects.")"""
        ...
    def NewPartSymbolData(self, partSymbolName: str) -> Annotations.CustomSymbolData:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder for Drafting Custom Symbol and NXOpen.Annotations.PmiCustomSymbolBuilder for PMI Custom Symbol objects.")"""
        ...
    def CreateCustomSymbol(self, customSymbolData: Annotations.CustomSymbolData, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.CustomSymbol:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder instead.")"""
        ...
    def CreatePmiCustomSymbol(self, customSymbolData: Annotations.CustomSymbolData, pmiData: Annotations.PmiData, annotationPlane: Xform, origin: Point3d, leader: Annotations.LeaderBundle) -> Annotations.PmiCustomSymbol:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.PmiCustomSymbolBuilder instead.")"""
        ...
    def CreateSmashCustomSymbolBuilder(self) -> Annotations.SmashCustomSymbolBuilder:
        ...
    def CreateMasterSymbolBuilder(self, masterSymbolTag: Annotations.MasterSymbol) -> Annotations.MasterSymbolBuilder:
        ...
    def CreateMasterSymbolListItemBuilder(self) -> Annotations.MasterSymbolListItemBuilder:
        ...
    def CreateDraftingCustomSymbolBuilder(self, symbolTag: Annotations.CustomSymbol) -> Annotations.DraftingCustomSymbolBuilder:
        ...
    def CreatePmiCustomSymbolBuilder(self, symbolTag: Annotations.PmiCustomSymbol) -> Annotations.PmiCustomSymbolBuilder:
        ...
    def EditSymbolDisplayBuilder(self, symbolTag: Annotations.BaseCustomSymbol) -> Annotations.EditSymbolDisplayBuilder:
        ...
    def FindObject(self, name: str) -> Annotations.MasterSymbol:
        ...
    def CreateSymbolCatalogBuilder(self) -> Annotations.SymbolCatalogBuilder:
        ...
    def CreateReplaceSymbolBuilder(self) -> Annotations.ReplaceSymbolBuilder:
        ...
    def Tag(self) -> Tag: ...



class CustomSymbol(Annotations.BaseCustomSymbol):
    def __init__(self) -> None: ...


class CustomerValueBusinessModifierBuilder(Builder):
    def __init__(self) -> None: ...
    CustomerValue: str
    Title: str


class CustomerValueBusinessModifier(Annotations.ListBusinessModifier):
    def __init__(self) -> None: ...


class CurveLengthDimensionBuilder(Annotations.BaseCurveLengthDimensionBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class CoordinateNoteBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    Category: str
    DecimalPlace: int
    Identifier: str
    Revision: str
    StringPrefixI: str
    StringPrefixJ: str
    StringPrefixK: str
    StringPrefixLabel: str
    StringPrefixLevel: str
    StringPrefixX: str
    StringPrefixY: str
    StringPrefixZ: str
    StringSuffixI: str
    StringSuffixJ: str
    StringSuffixK: str
    StringSuffixLabel: str
    StringSuffixLevel: str
    StringSuffixX: str
    StringSuffixY: str
    StringSuffixZ: str
    Title: str
    ToggleI: bool
    ToggleJ: bool
    ToggleK: bool
    ToggleLabel: bool
    ToggleLevel: bool
    ToggleX: bool
    ToggleY: bool
    ToggleZ: bool
    TrackingCsys: CoordinateSystem
    TrackingPoint: Point


class CoordinateNote(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class ConvertPmiBuilder(Builder):
    def __init__(self) -> None: ...
    Selection: Annotations.SelectPmiCadNeutralAnnotationList
    ShowReport: bool


class Constants(enum.Enum):
    MaxLeaders = 7
    MaxLeaderIntermediatePoints = 7


class ConcentricCircleDimension(Annotations.BaseConcentricCircleDimension):
    def __init__(self) -> None: ...


class CompoundDatumReferenceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DatumReferenceList: Annotations.DatumReferenceBuilderList
    ExtendedText: Annotations.TextWithSymbolsBuilder


class ComponentData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetLineComponents(self) -> typing.List[Annotations.LineComponent]:
        ...
    def GetArrowComponents(self) -> typing.List[Annotations.ArrowComponent]:
        ...
    def GetArcComponents(self) -> typing.List[Annotations.ArcComponent]:
        ...
    def GetTextComponents(self) -> typing.List[Annotations.TextComponent]:
        ...
    def GetEntities(self) -> typing.List[DisplayableObject]:
        ...
    def GetEntitiesAutodelete(self) -> typing.List[DisplayableObject]:
        ...


class CompanyProprietaryInformationBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetStringText(self) -> str:
        ...
    def SetStringText(self, stringText: str) -> None:
        ...
    Identifier: str
    Title: str


class CompanyProprietaryInformation(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class CommonWorkflowBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DynamicAlignmentInGlobalSelection: bool


class CircularTargetData(Annotations.DatumTargetData):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetDiameter(self) -> Annotations.Value:
        ...
    def SetDiameter(self, diameter: Annotations.Value) -> None:
        ...


class CircularTarget(Annotations.AreaTarget):
    def __init__(self) -> None: ...
    def GetDiameter(self) -> Annotations.Value:
        ...
    def SetDiameter(self, diameter: Annotations.Value) -> None:
        ...


class CircularCenterlineBuilder(Annotations.CircleCenterlineBuilder):
    def __init__(self) -> None: ...


class CircularCenterline(Annotations.CircleCenterline):
    def __init__(self) -> None: ...


class CircleCenterlineSettingsBuilder(Annotations.CenterlineSettingsBuilder):
    def __init__(self) -> None: ...
    Extension: float
    IndividualDistance: bool
    Size: float


class CircleCenterlineBuilder(Annotations.CenterlineBuilder):
    def __init__(self) -> None: ...
    def RemoveLocation(self, index: int) -> None:
        ...
    FullCircle: bool
    Inherit: SelectNXObject
    Locations: SelectNXObjectList
    Settings: Annotations.CircleCenterlineSettingsBuilder
    Type: Annotations.CircleCenterlineBuilder.Types


    class Types(enum.Enum):
        Through3Points = 0
        Centerpoint = 1
    

class CircleCenterline(Annotations.Centerline):
    def __init__(self) -> None: ...


class CharacterSpaceFactor():
    General: float
    Dimension: float
    Tolerance: float
    Appended: float
    def ToString(self) -> str:
        ...


class ChamferSymbolPlacement(enum.Enum):
    None = 0
    Prefix = 1
    Suffix = 2
    Last = 3


class ChamferStubType(enum.Enum):
    NoneTextAboveLeader = 0
    NoneTextAfterLeader = 1
    TextAbove = 2
    TextAfter = 3
    Last = 4


class ChamferSeparatorType(enum.Enum):
    UppercaseX = 0
    LowercaseX = 1


class ChamferOrientationType(enum.Enum):
    Horizontal = 0
    Vertical = 1
    Parallel = 2


class ChamferLeaderPlacement(enum.Enum):
    Perpendicular = 0
    Parallel = 1
    Linear = 2
    Last = 3


class ChamferForm(enum.Enum):
    Symbol = 0
    Size = 1
    SizeAngle = 2
    AngleSize = 3
    Last = 4


class ChamferDimensionPreferences(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    CharacterSpacing: float
    Form: Annotations.ChamferForm
    LeaderPlacement: Annotations.ChamferLeaderPlacement
    Separator: Annotations.ChamferSeparatorType
    StubType: Annotations.ChamferStubType
    SymbolName: str
    SymbolPlacement: Annotations.ChamferSymbolPlacement


class ChamferDimensionBuilder(Annotations.BaseChamferDimensionBuilder):
    def __init__(self) -> None: ...
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class ChamferDimension(Annotations.BaseChamferDimension):
    def __init__(self) -> None: ...


class ChainDimension(Annotations.DimensionSet):
    def __init__(self) -> None: ...


class CenterMarkSettingsBuilder(Annotations.CenterlineSettingsBuilder):
    def __init__(self) -> None: ...
    Angle: float
    AssociativeAngle: Drawings.AssociativeAngleBuilder
    Extension: float
    IndividualDistance: bool
    InheritAngle: bool
    ShowCenterPoint: bool
    Size: float


class CenterMarkBuilder(Annotations.BaseCenterMarkBuilder):
    def __init__(self) -> None: ...
    Inherit: SelectNXObject


class CenterMark(Annotations.BaseCenterMark):
    def __init__(self) -> None: ...


class CenterlineSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Color: NXColor
    Gap: float
    Width: Annotations.CenterlineSettingsBuilder.CenterlineThickness


    class CenterlineThickness(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 6
        Two = 7
        Three = 8
        Four = 9
        Five = 10
        Six = 11
        Seven = 12
        Eight = 13
        Nine = 14
    

class CenterlineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.Centerline]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSymmetricalCenterlineBuilder(self, centerline: Annotations.SymmetricalCenterline) -> Annotations.SymmetricalCenterlineBuilder:
        ...
    def CreateBoltCircleCenterlineBuilder(self, centerline: Annotations.BoltCircleCenterline) -> Annotations.BoltCircleCenterlineBuilder:
        ...
    def CreateCircularCenterlineBuilder(self, centerline: Annotations.CircularCenterline) -> Annotations.CircularCenterlineBuilder:
        ...
    def CreateCenterMarkBuilder(self, centerline: Annotations.CenterMark) -> Annotations.CenterMarkBuilder:
        ...
    def CreatePmiCenterMarkBuilder(self, centerline: Annotations.PmiCenterMark) -> Annotations.PmiCenterMarkBuilder:
        ...
    def CreateCenterline2dBuilder(self, cline: Annotations.Centerline2d) -> Annotations.Centerline2dBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.Centerline:
        ...
    def CreateAutomaticCenterlineBuilder(self) -> Annotations.AutomaticCenterlineBuilder:
        ...
    def CreateCenterline3dBuilder(self, cline: Annotations.Centerline3d) -> Annotations.Centerline3dBuilder:
        ...
    def CreatePmiCenterline3dBuilder(self, cline: Annotations.PmiCenterline3d) -> Annotations.PmiCenterline3dBuilder:
        ...
    def CreatePmiBoltCircleCenterlineBuilder(self, centerline: Annotations.PmiBoltCircleCenterline) -> Annotations.PmiBoltCircleCenterlineBuilder:
        ...
    def Tag(self) -> Tag: ...



class CenterlineBuilder(Annotations.BaseSymbolBuilder):
    def __init__(self) -> None: ...
    def AddExtension(self, index: int, defaultValue: float) -> None:
        ...
    def RemoveExtension(self, index: int) -> None:
        ...
    def AddEndExtensions(self, start: float, end: float) -> None:
        ...
    def RemoveEndExtensions(self) -> None:
        ...
    def SetIndividualExtensions(self, index: int, value1: float, value2: float) -> None:
        ...
    def SetEndExtensions(self, start: float, end: float) -> None:
        ...
    def GetEndExtensions(self) -> float:
        ...
    def GetAllIndividualExtensions(self) -> float:
        ...
    def SetAllIndividualExtensions(self, extensionValues: float) -> None:
        ...
    def GetAllExtensions(self) -> float:
        ...
    def ResetAllExtensions(self, defaultValue: float) -> None:
        ...


class Centerline3dSettingsBuilder(Annotations.CenterlineSettingsBuilder):
    def __init__(self) -> None: ...
    Extension: float
    IndividualDistance: bool
    Size: float


class Centerline3dBuilder(Annotations.BaseCenterline3dBuilder):
    def __init__(self) -> None: ...
    AlignedCenterlines: bool
    Inherit: SelectNXObject
    OffsetDistance: float
    OffsetMethod: Annotations.Centerline3dBuilder.Offset
    OffsetObject: SelectNXObject


    class Offset(enum.Enum):
        None = 0
        DistanceMethod = 1
        ObjectMethod = 2
    

class Centerline3d(Annotations.BaseCenterline3d):
    def __init__(self) -> None: ...


class Centerline2dSettingsBuilder(Annotations.CenterlineSettingsBuilder):
    def __init__(self) -> None: ...
    Extension: float
    IndividualDistance: bool
    Size: float


class Centerline2dBuilder(Annotations.CenterlineBuilder):
    def __init__(self) -> None: ...
    Inherit: SelectNXObject
    OffsetDistance: float
    OffsetMethod: Annotations.Centerline2dBuilder.Offset
    OffsetObject: SelectNXObject
    Point1: SelectNXObject
    Point2: SelectNXObject
    Settings: Annotations.Centerline2dSettingsBuilder
    Side1: SelectNXObject
    Side2: SelectNXObject
    Type: Annotations.Centerline2dBuilder.Types


    class Types(enum.Enum):
        FromCurves = 0
        ByPoints = 1
    

    class Offset(enum.Enum):
        None = 0
        DistanceMethod = 1
        ObjectMethod = 2
    

class Centerline2d(Annotations.Centerline):
    def __init__(self) -> None: ...


class Centerline(Annotations.DraftingAid):
    def __init__(self) -> None: ...


class CalloutGroupBuilder(Builder):
    def __init__(self) -> None: ...
    def GetGroupSymbols(self) -> typing.List[Annotations.IdSymbol]:
        ...
    def SetGroupSymbols(self, symbols: typing.List[Annotations.IdSymbol]) -> None:
        ...
    CalloutModeType: Annotations.CalloutGroupBuilder.Mode
    LayoutType: Annotations.CalloutGroupBuilder.Layout
    SelectCallout: SelectDisplayableObjectList
    VerticalLeaderAttachment: Annotations.CalloutGroupBuilder.VerticalGroupLeaderAttachment


    class VerticalGroupLeaderAttachment(enum.Enum):
        Top = 0
        Bottom = 1
    

    class Mode(enum.Enum):
        Group = 0
        Ungroup = 1
    

    class Layout(enum.Enum):
        Horizontal = 0
        Vertical = 1
    

class BusinessModifierCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateUrlBusinessModifier(self, modifierName: str) -> Annotations.UrlBusinessModifier:
        """[Obsolete("Deprecated in NX6.0.0.  Use BusinessModifierCollection.CreateUrlBusinessModifier instead.")"""
        ...
    def CreateCustomerValueBusinessModifier(self, modifierName: str) -> Annotations.CustomerValueBusinessModifier:
        """[Obsolete("Deprecated in NX6.0.0.  Use BusinessModifierCollection.CreateCustomerValueBusinessModifierBuilder instead.")"""
        ...
    def CreateRevisonBusinessModifier(self, modifierName: str) -> Annotations.RevisionBusinessModifier:
        """[Obsolete("Deprecated in NX6.0.0.  Use BusinessModifierCollection.CreateRevisionBusinessModifierBuilder instead.")"""
        ...
    def CreateSafetyClassBusinessModifier(self, modifierName: str) -> Annotations.SafetyClassBusinessModifier:
        """[Obsolete("Deprecated in NX6.0.0.  Use BusinessModifierCollection.CreateSafetyClassBusinessModifierBuilder instead.")"""
        ...
    def CreateRevisionBusinessModifierBuilder(self, revisionbusinessModifier: Annotations.RevisionBusinessModifier) -> Annotations.RevisionBusinessModifierBuilder:
        ...
    def CreateSafetyClassBusinessModifierBuilder(self, safetyclassbusinessmodifier: Annotations.SafetyClassBusinessModifier) -> Annotations.SafetyClassBusinessModifierBuilder:
        ...
    def CreateFeatureIdBusinessModifierBuilder(self, featureidbusinessmodifier: Annotations.FeatureIdBusinessModifier) -> Annotations.FeatureIdBusinessModifierBuilder:
        ...
    def CreateCustomerValueBusinessModifierBuilder(self, customervaluebusinessmodifier: Annotations.CustomerValueBusinessModifier) -> Annotations.CustomerValueBusinessModifierBuilder:
        ...
    def CreateUrlBusinessModifierBuilder(self, urlbusinessmodifier: Annotations.UrlBusinessModifier) -> Annotations.UrlBusinessModifierBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> TaggedObject:
        ...
    def Tag(self) -> Tag: ...



class BusinessModifier(NXObject):
    def __init__(self) -> None: ...
    TextValue: str
    Title: str


class BreakSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    BreakSize: float
    CreateBreaks: bool


class BoundaryBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetView(self) -> View:
        ...
    def SetView(self, view: View) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CurveBoundaries: SectionList
    DistanceTolerance: float
    SelectionType: Annotations.BoundaryBuilder.SelectionMethod


    class SelectionMethod(enum.Enum):
        Curves = 0
        Location = 1
    

class BoltCircleCenterlineBuilder(Annotations.BaseBoltCircleCenterlineBuilder):
    def __init__(self) -> None: ...


class BoltCircleCenterline(Annotations.BaseBoltCircleCenterline):
    def __init__(self) -> None: ...


class BillOfMaterialBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DetailLevel: Annotations.BillOfMaterialBuilder.DetailLevelType
    FabricationNumbering: Annotations.BillOfMaterialBuilder.FabricationNumberingType
    IncludeComponents: bool
    IncludeGaskNutBolts: bool
    IncludeOverStock: bool
    IncludeStock: bool
    IncludeWireStock: bool
    StockLength: Annotations.BillOfMaterialBuilder.StockLengthType
    StockPieceCount: bool


    class StockLengthType(enum.Enum):
        SingleSum = 0
        ListEach = 1
    

    class FabricationNumberingType(enum.Enum):
        Sequential = 0
        Original = 1
    

    class DetailLevelType(enum.Enum):
        Summary = 0
        Itemized = 1
    

class BendTableSettingsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetColumnOrder(self) -> typing.List[Annotations.BendTableSettingsBuilder.ColumnType]:
        ...
    def SetColumnOrder(self, columnOrder: typing.List[Annotations.BendTableSettingsBuilder.ColumnType]) -> None:
        ...
    def Validate(self) -> bool:
        ...
    AutomaticUpdate: bool
    SortColumn: Annotations.BendTableSettingsBuilder.ColumnType
    SortOnUpdate: bool


    class ColumnType(enum.Enum):
        BendID = 0
        BendName = 1
        BendRadius = 2
        BendAngle = 3
        BendDirection = 4
        IncludedAngle = 5
    

class BendTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.BendTable]:
        ...
    def __init__(self, owner: Annotations.AnnotationManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBendTableBuilder(self, bendTable: Annotations.BendTable) -> Annotations.BendTableBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> Annotations.BendTable:
        ...
    def Tag(self) -> Tag: ...



class BendTableBuilder(Builder):
    def __init__(self) -> None: ...
    AnnotationOrigin: Annotations.OriginBuilder
    FlatPatternView: Drawings.SelectDraftingView
    Style: Annotations.TableStyleBuilder


class BendTable(Annotations.Table):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...


class BaseVerticalDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    def IsSlotDimension(self) -> bool:
        ...
    def ConvertSlotDimensionAssociativity(self) -> bool:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseTitleBlockBuilder(Builder):
    def __init__(self) -> None: ...
    Cells: Annotations.TitleBlockCellBuilderList


class BaseThicknessDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    AppendedText: Annotations.AppendedTextBuilder
    FirstAssociativity: SelectDisplayableObject
    Inherit: Annotations.SelectDimension
    Origin: Annotations.OriginBuilder
    SecondAssociativity: SelectDisplayableObject
    Style: Annotations.StyleBuilder


class BaseSymbolBuilder(Builder):
    def __init__(self) -> None: ...


class BaseSurfaceFinishBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...


    class ToleranceOption(enum.Enum):
        None = 0
        EqualBilateral = 1
        Bilateral = 2
        UnilateralPlus = 3
        UnilateralMinus = 4
        PlusLimitTwoLines = 5
        MinusLimitTwoLines = 6
        PlusLimitOneLine = 7
        MinusLimitOneLine = 8
    

    class ParenthesesType(enum.Enum):
        None = 0
        Left = 1
        Right = 2
        Both = 3
    

    class ParanthesesType(enum.Enum):
        None = 0
        Left = 1
        Right = 2
        Both = 3
    

class BaseSurfaceFinish(Annotations.PmiAttribute):
    def __init__(self) -> None: ...
    def GetUnitsFormatPrefs(self) -> Annotations.UnitsFormatPreferences:
        ...
    def SetUnitsFormatPrefs(self, unitsFormat: Annotations.UnitsFormatPreferences) -> None:
        ...
    def GetInvertSymbol(self) -> bool:
        ...
    def SetInvertSymbol(self, invertSymbol: bool) -> None:
        ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...


class BaseRapidDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetFirstAssociativityVectorFlipped(self, firstVectorFlipped: bool) -> None:
        ...
    def SetSecondAssociativityVectorFlipped(self, secondVectorFlipped: bool) -> None:
        ...
    def GetFirstAssociativityVectorFlipped(self) -> bool:
        ...
    def GetSecondAssociativityVectorFlipped(self) -> bool:
        ...
    AppendedText: Annotations.AppendedTextBuilder
    FirstAssociativity: SelectDisplayableObject
    Inherit: SelectDisplayableObject
    Measurement: Annotations.DimensionMeasurementBuilder
    Origin: Annotations.OriginBuilder
    SecondAssociativity: SelectDisplayableObject
    Style: Annotations.StyleBuilder


class BaseRadiusDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetRadiusDimensionType(self) -> Annotations.RadiusDimensionType:
        ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseRadialDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    AppendedText: Annotations.AppendedTextBuilder
    DiameterDimensionDimLineAngle: float
    FirstAssociativity: SelectNXObject
    FoldLocation: SelectDisplayableObject
    Inherit: SelectDisplayableObject
    IsFoldedRadius: bool
    IsHoleStyle: bool
    IsRadiusToCenter: bool
    Measurement: Annotations.DimensionMeasurementBuilder
    OffsetCenterPoint: SelectDisplayableObject
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder


class BaseProductGridBuilder(Builder):
    def __init__(self) -> None: ...
    CoordinateSystem: CoordinateSystem
    GridSpacing: float
    HorizontalMaximumValue: float
    HorizontalMinimumValue: float
    ShowHorizontalLines: bool
    ShowVerticalLines: bool
    Style: Annotations.StyleBuilder
    VerticalMaximumValue: float
    VerticalMinimumValue: float


class BaseProductGrid(Annotations.Annotation):
    def __init__(self) -> None: ...


class BasePerpendicularDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseParallelDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    def IsSlotDimension(self) -> bool:
        ...
    def ConvertSlotDimensionAssociativity(self) -> bool:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseOrdinateDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    ActiveHorizontalMargin: Annotations.OrdinateMargin
    ActiveVerticalMargin: Annotations.OrdinateMargin
    AllowDuplicates: bool
    AppendedText: Annotations.AppendedTextBuilder
    AutoAssociativities: SelectDisplayableObjectList
    Baseline: Annotations.OrdinateBaselineBuilder
    HorizontalInferredMarginLocation: Point3d
    Inherit: SelectDisplayableObject
    OrdinateOrigin: SelectDisplayableObject
    Origin: Annotations.OriginBuilder
    RespositionExisting: bool
    SecondAssociativities: SelectDisplayableObject
    Style: Annotations.StyleBuilder
    Type: Annotations.BaseOrdinateDimensionBuilder.Types
    VerticalInferredMarginLocation: Point3d


    class Types(enum.Enum):
        SingleDimension = 0
        MultipleDimension = 1
    

class BaseNote(Annotations.NoteBase):
    def __init__(self) -> None: ...
    def UpdateFromRule(self) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    IsVertical: bool
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaselineDimension(Annotations.DimensionSet):
    def __init__(self) -> None: ...


class BaseLinearDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetNthSecondaryOrigin(self, nth: int, secondaryOrigin: Point3d) -> None:
        ...
    def GetNthSecondaryOrigin(self, nth: int) -> Point3d:
        ...
    def SetNthSecondaryArrowheadOrientation(self, nth: int, secondaryArrowheadOrientation: Annotations.TextPlacement) -> None:
        ...
    def GetNthSecondaryArrowheadOrientation(self, nth: int) -> Annotations.TextPlacement:
        ...
    def GetSecondaryCallouts(self) -> typing.List[Annotations.Dimension]:
        ...
    AppendedText: Annotations.AppendedTextBuilder
    DimensionSet: Annotations.DimensionSetBuilder
    FirstAssociativity: SelectNXObject
    Inherit: SelectDisplayableObject
    IsAutoplaced: bool
    Measurement: Annotations.DimensionMeasurementBuilder
    MeasurementType: Annotations.Dimension.MeasurementTypes
    Origin: Annotations.OriginBuilder
    SecondAssociativity: SelectNXObject
    Style: Annotations.StyleBuilder
    UseBaseline: bool


class BaseHorizontalDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    def IsSlotDimension(self) -> bool:
        ...
    def ConvertSlotDimensionAssociativity(self) -> bool:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseHoleDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseFrameBarBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateFromConceptModel(self) -> None:
        ...
    def ReverseTics(self) -> None:
        ...
    def CreateFrameBarObject(self) -> None:
        ...
    def GetFramebar(self) -> Annotations.BaseFrameBar:
        ...
    def UpdateFrameBarFromStyle(self) -> None:
        ...
    def ReverseAlongHullSide(self) -> None:
        ...
    def DeleteFrameBarObject(self) -> None:
        ...
    AftPerpendicular: bool
    Axis: Annotations.BaseFrameBarBuilder.AxisType
    Baseline: bool
    BulkHeads: bool
    Centerline: bool
    Decks: bool
    ForwardPerpendicular: bool
    HorizontalDistance: float
    HorizontalPosition: Annotations.BaseFrameBarBuilder.HorizontalPositionType
    InterTransverseFrames: bool
    LongitudinalBulkheads: bool
    LongitudinalYFrames: bool
    LongitudinalYInsertFrames: bool
    LongitudinalZFrames: bool
    LongitudinalZInsertFrames: bool
    MainLine: bool
    MainLineColor: NXColor
    MainLineFont: DisplayableObject.ObjectFont
    MainLineWidth: Annotations.LineWidth
    Origin: Annotations.OriginBuilder
    OriginType: Annotations.BaseFrameBarBuilder.OriginOption
    Style: Annotations.StyleBuilder
    TransveralInsertArea: bool
    TransverseFrames: bool
    VerticalDistance: float
    VerticalPosition: Annotations.BaseFrameBarBuilder.VerticalPositionType
    View: Drawings.SelectDraftingView
    Waterline: bool


    class VerticalPositionType(enum.Enum):
        Left = 0
        ShipCenter = 1
        ViewCenter = 2
        Right = 3
    

    class OriginOption(enum.Enum):
        SpecifyPosition = 0
        Distance = 1
    

    class HorizontalPositionType(enum.Enum):
        Above = 0
        ShipCenter = 1
        ViewCenter = 2
        Below = 3
    

    class AxisType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        AlongHull = 3
    

class BaseFrameBar(Annotations.Annotation):
    def __init__(self) -> None: ...
    def GetFramebarPreferences(self) -> Annotations.FrameBarPreferences:
        ...
    def SetFramebarPreferences(self, framebarPrefs: Annotations.FrameBarPreferences) -> None:
        ...


class BaseFoldedRadiusDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseFcf(Annotations.Gdt):
    def __init__(self) -> None: ...


class BaseEdgeConditionSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    def InheritProperties(self, ecsTag: Annotations.BaseEdgeConditionSymbol) -> None:
        ...
    Inherit: Annotations.SelectBaseEdgeConditionSymbol
    Leader: Annotations.LeaderBuilder
    LimitDeviation: str
    LimitDeviationA1: str
    LimitDeviationA2: str
    LimitDeviationB1: str
    LimitDeviationB2: str
    LimitDeviationC1: str
    LimitDeviationC2: str
    Method: Annotations.BaseEdgeConditionSymbolBuilder.MethodType
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder
    SymbolElement: Annotations.BaseEdgeConditionSymbolBuilder.SymbolElementEnum


    class SymbolElementEnum(enum.Enum):
        Plus = 0
        Minus = 1
    

    class MethodType(enum.Enum):
        Basic = 0
        UndefinedDirectionandSize = 1
        UndefinedDirectionDefinedSize = 2
        UndefinedDirectionEqualBilateralSize = 3
        DefinedDirection = 4
    

class BaseEdgeConditionSymbol(Annotations.DraftingAid):
    def __init__(self) -> None: ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseDiameterDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    DiamDimLineAng: float
    DiameterDimensionLineAngle: float
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseDatumTarget(Annotations.Gdt):
    def __init__(self) -> None: ...
    DatumLabel: str
    TargetIndex: int


class BaseDatum(Annotations.Gdt):
    def __init__(self) -> None: ...
    Label: str


class BaseCylindricalDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseCustomSymbolBuilder(Builder):
    def __init__(self) -> None: ...
    def GetArbitraryNoteTitle(self) -> str:
        ...
    def SetArbitraryNoteTitle(self, arbitraryNoteTitle: str) -> None:
        ...
    def SelectSymbol(self, name: str) -> None:
        ...
    def SelectPartSymbol(self, name: str, path: str) -> None:
        ...
    def SelectText(self, index: int) -> None:
        ...
    def GetSymbol(self) -> Annotations.BaseCustomSymbol:
        ...
    Angle: Expression
    AnnotationPreference: Annotations.BaseCustomSymbolBuilder.AnnotationPreferences
    ControlledNoteTitle: int
    GeometryPreference: Annotations.BaseCustomSymbolBuilder.GeometryPreferences
    HorizontalFlip: bool
    Integer: int
    IsPartSymbol: bool
    Leader: Annotations.LeaderBuilder
    LockStatus: bool
    MasterSymbolName: str
    MasterSymbolPath: str
    Origin: Annotations.OriginBuilder
    PartiallyControlledNoteTitle: str
    Real: float
    Scale: Expression
    SmashSymbol: bool
    Style: Annotations.StyleBuilder
    Texts: Annotations.MasterSymbolListItemBuilderList
    VerticalFlip: bool


    class GeometryPreferences(enum.Enum):
        UseCurrent = 0
        UseDefinition = 1
    

    class AnnotationPreferences(enum.Enum):
        UseCurrent = 0
        UseDefinition = 1
    

class BaseCustomSymbol(Annotations.DraftingAid):
    def __init__(self) -> None: ...
    def GetSymbolData(self) -> Annotations.CustomSymbolData:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder for Drafting Custom Symbol and NXOpen.Annotations.PmiCustomSymbolBuilder for PMI Custom Symbol objects.")"""
        ...
    def SetSymbolData(self, data: Annotations.CustomSymbolData) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.DraftingCustomSymbolBuilder for Drafting Custom Symbol and NXOpen.Annotations.PmiCustomSymbolBuilder for PMI Custom Symbol objects.")"""
        ...
    def FlipSymbol(self, flipOption: Annotations.FlipOption) -> None:
        ...
    def UpdateSymbolGeometry(self, origin: Point3d, scale: float, angle: float) -> None:
        ...
    def AddLeader(self, leader: Annotations.LeaderBundle) -> None:
        ...
    def RemoveLeader(self, nthLeader: int) -> None:
        ...
    def SynchronizeSymbol(self) -> None:
        ...
    def ReplaceSymbol(self, name: str, path: str, isPartSymbol: bool) -> None:
        ...
    def GetAnchor(self) -> Point:
        ...
    def SetAnchor(self, anchorPoint: Point) -> None:
        ...
    def UpdateFromRule(self) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    SymbolName: str
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseCurveLengthDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    AppendedText: Annotations.AppendedTextBuilder
    FirstAssociativity: SelectDisplayableObject
    Inherit: Annotations.SelectDimension
    Origin: Annotations.OriginBuilder
    Style: Annotations.StyleBuilder


class BaseConcentricCircleDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseChamferDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    AppendedText: Annotations.AppendedTextBuilder
    FirstAssociativity: SelectDisplayableObject
    Inherit: Annotations.SelectDimension
    Orientation: Annotations.ChamferOrientationType
    Origin: Annotations.OriginBuilder
    SecondAssociativity: SelectDisplayableObject
    Style: Annotations.StyleBuilder


class BaseChamferDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    ChamferOrientation: Annotations.ChamferOrientationType
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseCenterMarkBuilder(Annotations.CenterlineBuilder):
    def __init__(self) -> None: ...
    def RemoveLocation(self, index: int) -> None:
        ...
    Locations: SelectNXObjectList
    MultipleCenterMarks: bool
    Settings: Annotations.CenterMarkSettingsBuilder


class BaseCenterMark(Annotations.Centerline):
    def __init__(self) -> None: ...


class BaseCenterline3dBuilder(Annotations.CenterlineBuilder):
    def __init__(self) -> None: ...
    Face: SelectNXObjectList
    ReferenceIndex: int
    Settings: Annotations.Centerline3dSettingsBuilder


class BaseCenterline3d(Annotations.Centerline):
    def __init__(self) -> None: ...


class BaseBoltCircleCenterlineBuilder(Annotations.CircleCenterlineBuilder):
    def __init__(self) -> None: ...


class BaseBoltCircleCenterline(Annotations.CircleCenterline):
    def __init__(self) -> None: ...


class BaseArrow(Annotations.Annotation):
    def __init__(self) -> None: ...


class BaseArcLengthDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.LinearTolerance:
        ...
    def SetTolerance(self, tolerance: Annotations.LinearTolerance) -> None:
        ...
    def GetBusinessModifiers(self) -> typing.List[Annotations.BusinessModifier]:
        ...
    def SetBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def AddBusinessModifiers(self, businessModifiers: typing.List[Annotations.BusinessModifier]) -> None:
        ...
    def GetAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def GetSharedAssociatedObject(self) -> Annotations.AssociatedObject:
        ...
    def SetAssociatedObject(self, assocObj: Annotations.AssociatedObject) -> None:
        ...
    Index: int
    IsMirrored: bool
    IsWaveLinked: bool
    LinkSource: Annotations.Annotation


class BaseAngularDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    def AlternateAngle(self) -> None:
        ...
    def SetFirstAssociativityVectorFlipped(self, firstVectorFlipped: bool) -> None:
        ...
    def SetSecondAssociativityVectorFlipped(self, secondVectorFlipped: bool) -> None:
        ...
    def GetFirstAssociativityVectorFlipped(self) -> bool:
        ...
    def GetSecondAssociativityVectorFlipped(self) -> bool:
        ...
    def SetNthAssociativityEdited(self, index: int, edited: bool) -> None:
        ...
    AppendedText: Annotations.AppendedTextBuilder
    FirstAssociativity: SelectDisplayableObject
    FirstVector: Direction
    FirstVectorView: View
    Inherit: Annotations.SelectDimension
    MeasurementType: Annotations.Dimension.MeasurementTypes
    Origin: Annotations.OriginBuilder
    SecondAssociativity: SelectDisplayableObject
    SecondVector: Direction
    SecondVectorView: View
    Style: Annotations.StyleBuilder


class BaseAngularDimension(Annotations.Dimension):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> Annotations.AngularTolerance:
        ...
    def SetTolerance(self, tolerances: Annotations.AngularTolerance) -> None:
        ...


class BalloonTypes(enum.Enum):
    Circle = 0
    DividedCircle = 1
    TriangleDown = 2
    TriangleUp = 3
    Square = 4
    DividedSquare = 5
    Hexagon = 6
    DividedHexagon = 7
    QuadrantCircle = 8
    RoundedBox = 9
    Underline = 10


class BalloonsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SelectDraftingViews: Drawings.SelectDraftingViewList
    ShowBalloons: bool


class BalloonNoteBuilder(Annotations.PmiAttributeBuilder):
    def __init__(self) -> None: ...
    def GetText(self) -> str:
        ...
    def SetText(self, text: str) -> None:
        ...
    BalloonText: str
    Category: str
    Identifier: str
    Revision: str
    Scale: float
    Title: str


class BalloonNote(Annotations.PmiAttribute):
    def __init__(self) -> None: ...


class AutomaticCenterlineBuilder(Builder):
    def __init__(self) -> None: ...
    Color: NXColor
    CylindricalExtension: float
    InheritAngle: bool
    Views: Drawings.SelectDraftingViewList
    Width: Annotations.AutomaticCenterlineBuilder.CenterlineThickness


    class CenterlineThickness(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 6
        Two = 7
        Three = 8
        Four = 9
        Five = 10
        Six = 11
        Seven = 12
        Eight = 13
        Nine = 14
    

class AssociativityPointOption(enum.Enum):
    None = 0
    Control = 1
    ArcCenter = 2
    Tangent = 3
    Intersection = 4
    ScreenPosition = 5
    OnCurve = 6
    Pole = 7
    Anchor = 8
    Defining = 9
    Last = 10


class AssociativityLineOption(enum.Enum):
    None = 0
    ExistingLine = 1
    PointVector = 2
    ExtensionLine = 3
    Centerline = 4
    Angle = 5
    HorizontalRight = 6
    VerticalUp = 7
    HorizontalLeft = 8
    VerticalDown = 9
    BaseLine = 10
    Last = 11


class AssociativityBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: float
    LineOption: Annotations.AssociativityLineOption
    SelectObject: SelectDisplayableObject
    Vector: SelectDisplayableObjectList


class Associativity(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Angle: float
    FirstDefinitionPoint: Point3d
    FirstObject: NXObject
    LineOption: Annotations.AssociativityLineOption
    ObjectView: View
    PickPoint: Point3d
    PointOption: Annotations.AssociativityPointOption
    SecondDefinitionPoint: Point3d
    SecondObject: NXObject


class AssociativeText(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetObjectPropertyText(self, object: NXObject, type: Annotations.AssociativeText.PropertyType) -> str:
        ...
    def GetObjectAttributeText(self, object: NXObject, attributeTitle: str) -> str:
        ...
    def GetObjectAttribute(self, text: str, object: NXObject, attributeTitle: str) -> bool:
        ...
    def GetPartAttributeText(self, attributeTitle: str) -> str:
        ...
    def GetPartAttribute(self, text: str, attributeTitle: str) -> bool:
        ...
    def GetEvaluatedText(self, ann: Annotations.Annotation, text: str) -> str:
        ...
    def CreateEmbeddedAnnotationText(self, embeddedAnnotation: Annotations.Annotation) -> str:
        ...


    class PropertyType(enum.Enum):
        DrawingNumberOfSheets = 0
        DrawingNumberOfPrimarySheets = 1
        DrawingSheetName = 2
        DrawingSheetNumber = 3
        DrawingSheetRevision = 4
        DrawingSheetScaleNumerator = 5
        DrawingSheetScaleDenominator = 6
        DrawingSheetSize = 7
        DrawingSheetUnits = 8
        DrawingSheetZone = 9
        DrawingSheetProjectionAngle = 10
        DrawingMasterPartName = 11
        DrawingPartName = 12
        DrawingViewPrefix = 13
        DrawingViewRotationAngle = 14
    

class AssociativeOriginType(enum.Enum):
    Drag = 0
    RelativeToView = 1
    RelativeToGeometry = 2
    VerticallyAligned = 3
    HorizontallyAligned = 4
    AlignedWithArrows = 5
    AtAPoint = 6
    OffsetFromText = 7
    AttachedToStack = 8


class AssociatedObjectsSetsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ObjectsSet1: Annotations.AssociatedObjectsBuilder
    ObjectsSet2: Annotations.AssociatedObjectsBuilder


class AssociatedObjectsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Nxobjects: SelectNXObjectList
    Objects: SelectDisplayableObjectList


class AssociatedObject(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetObjects(self) -> typing.List[NXObject]:
        ...
    def SetObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def GetObjectIndex(self, object: DisplayableObject) -> int:
        ...


class AssociateDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    Associativity1: Annotations.AssociativityBuilder
    Associativity2: Annotations.AssociativityBuilder


class ArrowheadType(enum.Enum):
    FilledDatumArrow = -2
    FilledDot = -1
    FilledArrow = 0
    ClosedArrow = 1
    OpenArrow = 2
    CrossArrow = 3
    DotArrow = 4
    OriginSymbolArrow = 5
    NoArrow = 6
    UnfilledDatumArrow = 7
    ClosedSolidArrow = 8
    ClosedDoubleArrow = 9
    ClosedDoubleSolidArrow = 10
    OpenDoubleArrow = 11
    IntegralArrow = 12
    BoxArrow = 13
    FilledBox = 14
    FilledDoubleArrow = 15
    TopOpenArrow = 16
    BottomOpenArrow = 17
    TopFilledArrow = 18
    BottomFilledArrow = 19


class ArrowDisplay(enum.Enum):
    Two = 0
    First = 1
    Second = 2
    None = 3
    Last = 4


class ArrowComponent(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    ArrowAngle: float
    IncludedArrowAngle: float
    Index: int
    Origin: Point3d
    Type: Annotations.ArrowheadType


class AreaTarget(Annotations.DatumTarget):
    def __init__(self) -> None: ...


class AreaFillMaterial(enum.Enum):
    CorkFelt = 0
    SoundInsulation = 1
    Concrete = 2
    Earth = 3
    Rock = 4
    Sand = 5
    Liquids = 6
    WoodAcrossGrain = 7
    WoodAlongGrain = 8
    SolidFill = 9


class ArcLengthDimension(Annotations.BaseArcLengthDimension):
    def __init__(self) -> None: ...


class ArcComponent(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    CenterPoint: Point3d
    EndAngle: float
    Index: int
    Radius: float
    StartAngle: float
    Type: Annotations.ArcComponent.ArcType


    class ArcType(enum.Enum):
        Extension = 0
        Dimension = 1
        AllAround = 2
        Annotation = 3
        Inspection = 4
        AllOver = 5
        GbDatum = 6
    

class ArbitraryTargetData(Annotations.DatumTargetData):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    UpperText: str


class ArbitraryTarget(Annotations.DatumTarget):
    def __init__(self) -> None: ...
    UpperText: str


class ArbitraryAreaSeedBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Annotations.ArbitraryAreaSeedBuilder]) -> None:
        ...
    def Append(self, object: Annotations.ArbitraryAreaSeedBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Annotations.ArbitraryAreaSeedBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Annotations.ArbitraryAreaSeedBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Annotations.ArbitraryAreaSeedBuilder) -> None:
        ...
    def Erase(self, obj: Annotations.ArbitraryAreaSeedBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Annotations.ArbitraryAreaSeedBuilder]:
        ...
    def SetContents(self, objects: typing.List[Annotations.ArbitraryAreaSeedBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Annotations.ArbitraryAreaSeedBuilder, object2: Annotations.ArbitraryAreaSeedBuilder) -> None:
        ...
    def Insert(self, location: int, object: Annotations.ArbitraryAreaSeedBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ArbitraryAreaSeedBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    SelectFace: SelectDisplayableObjectList
    SpecifyCurves: SelectDisplayableObjectList
    SpecifyPoint: Point


class AppendedTextEditorBuilder(Builder):
    def __init__(self) -> None: ...
    def SetDimensions(self, dimensions: typing.List[Annotations.Dimension]) -> None:
        ...
    AppendedTextBuilder: Annotations.AppendedTextBuilder


class AppendedTextBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetAbove(self) -> str:
        ...
    def SetAbove(self, lines: str) -> None:
        ...
    def GetAfter(self) -> str:
        ...
    def SetAfter(self, lines: str) -> None:
        ...
    def GetBelow(self) -> str:
        ...
    def SetBelow(self, lines: str) -> None:
        ...
    def GetBefore(self) -> str:
        ...
    def SetBefore(self, lines: str) -> None:
        ...
    def Validate(self) -> bool:
        ...
    UserDefinedSymbolAspectRatio: float
    UserDefinedSymbolHeight: float
    UserDefinedSymbolLength: float
    UserDefinedSymbolScale: float
    UserDefinedSymbolSizeMethod: int


class AppendedText(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetBeforeText(self) -> str:
        ...
    def SetBeforeText(self, lines: str) -> None:
        ...
    def GetAfterText(self) -> str:
        ...
    def SetAfterText(self, lines: str) -> None:
        ...
    def GetAboveText(self) -> str:
        ...
    def SetAboveText(self, lines: str) -> None:
        ...
    def GetBelowText(self) -> str:
        ...
    def SetBelowText(self, lines: str) -> None:
        ...


class AnnotationPlacement(TaggedObject):
    def __init__(self) -> None: ...
    def SetLeaderBundle(self, jaLeader: Annotations.LeaderBundle) -> None:
        ...
    def SetOrigin(self, originData: Annotations.Annotation.AssociativeOriginData, origin: Point3d) -> None:
        ...
    def GetOrigin(self, originData: Annotations.Annotation.AssociativeOriginData, origin: Point3d) -> None:
        ...


class AnnotationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateNote(self, textLines: str, origin: Point3d, orientation: AxisOrientation, letteringPreferences: Annotations.LetteringPreferences, userSymbolPreferences: Annotations.UserSymbolPreferences) -> Annotations.Note:
        ...
    def ConvertToLineWeld(self, draftingAid: Annotations.LineWeld, keepDraftingAid: bool, leader: Annotations.LeaderBundle) -> Annotations.LineWeld:
        ...
    def ConvertToNote(self, draftingAid: Annotations.SimpleDraftingAid, keepDraftingAid: bool) -> Annotations.Note:
        ...
    def ConvertToLabel(self, draftingAid: Annotations.SimpleDraftingAid, keepDraftingAid: bool, leader: Annotations.LeaderBundle) -> Annotations.Label:
        ...
    def ConvertToGdt(self, draftingAid: Annotations.SimpleDraftingAid, keepDraftingAid: bool, leader: Annotations.LeaderBundle) -> Annotations.Gdt:
        ...
    def ConvertToIdSymbol(self, draftingAid: Annotations.SimpleDraftingAid, keepDraftingAid: bool, leader: Annotations.LeaderBundle) -> Annotations.SimpleDraftingAid:
        ...
    def CreateLabel(self, textLines: str, origin: Point3d, letteringPreferences: Annotations.LetteringPreferences, userSymbolPreferences: Annotations.UserSymbolPreferences, lineArrowPreferences: Annotations.LineAndArrowPreferences, leader: Annotations.LeaderBundle) -> Annotations.Label:
        ...
    def CreateGdt(self, textLines: str, origin: Point3d, letteringPreferences: Annotations.LetteringPreferences, userSymbolPreferences: Annotations.UserSymbolPreferences, lineArrowPreferences: Annotations.LineAndArrowPreferences, alwaysVertical: bool, leader: Annotations.LeaderBundle) -> Annotations.Gdt:
        ...
    def NewUserSymbolPreferences(self, type: Annotations.UserSymbolPreferences.SizeType, lengthOrScale: float, heightOrAspectRatio: float) -> Annotations.UserSymbolPreferences:
        ...
    def NewLeaderBundle(self) -> Annotations.LeaderBundle:
        ...
    def LoadSymbolFontFromSbfFile(self, symbolName: str, symbolWidth: float, symbolHeight: float) -> SymbolFont:
        ...
    def ReadAllSymbolNamesFromSbfFile(self) -> str:
        ...
    def SaveUserSymbolPart(self, symData: Annotations.MasterCustomSymbolData) -> None:
        """[Obsolete("Deprecated in NX7.5.2.  Use NXOpen.Annotations.MasterSymbolBuilder instead.")"""
        ...
    def NewPmiData(self) -> Annotations.PmiData:
        ...
    def NewAppendedText(self) -> Annotations.AppendedText:
        ...
    def NewDimensionData(self) -> Annotations.DimensionData:
        ...
    def NewAssociativity(self) -> Annotations.Associativity:
        ...
    def NewFcfFrame(self) -> Annotations.FcfFrame:
        ...
    def NewDatumReference(self) -> Annotations.DatumReference:
        ...
    def NewMasterCustomSymbolData(self) -> Annotations.MasterCustomSymbolData:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Annotations.MasterSymbolBuilder instead.")"""
        ...
    def GetDefaultAnnotationPlane(self, jaDefaultPlane: Annotations.PmiDefaultPlane) -> Xform:
        ...
    def CreateQueryPmiBuilder(self) -> Annotations.QueryPmiBuilder:
        ...
    def QueryPmiFromGeometry(self, geom: typing.List[DisplayableObject]) -> typing.List[Annotations.Annotation]:
        ...
    def CreateQueryView(self, pmiSymbols: typing.List[Annotations.Annotation]) -> ModelingView:
        ...
    def NewFcfFrameData(self) -> Annotations.FcfFrameData:
        ...
    def CreateAssociativityBuilder(self, dimension: Annotations.Dimension, assocIndex: int) -> Annotations.AssociativityBuilder:
        ...
    def CreateAssociateDimensionBuilder(self, dimension: Annotations.Dimension) -> Annotations.AssociateDimensionBuilder:
        ...
    def CreateLeaderData(self) -> Annotations.LeaderData:
        ...
    def MakePmi(self, annotation: Annotations.Annotation) -> None:
        ...
    def RemovePmi(self, annotation: Annotations.Annotation) -> None:
        ...
    def CreateDraftingNoteBuilder(self, annotation: Annotations.SimpleDraftingAid) -> Annotations.DraftingNoteBuilder:
        ...
    def CreatePmiNoteBuilder(self, annotation: Annotations.SimpleDraftingAid) -> Annotations.PmiNoteBuilder:
        ...
    def CreateDraftingFeatureControlFrameBuilder(self, fcf: Annotations.Gdt) -> Annotations.DraftingFeatureControlFrameBuilder:
        ...
    def CreateDraftingDatumTargetBuilder(self, datumTarget: Annotations.DraftingDatumTarget) -> Annotations.DraftingDatumTargetBuilder:
        ...
    def CreatePmiDatumTargetBuilder(self, datumTarget: Annotations.DatumTarget) -> Annotations.PmiDatumTargetBuilder:
        ...
    def CreatePmiFeatureControlFrameBuilder(self, fcf: Annotations.Fcf) -> Annotations.PmiFeatureControlFrameBuilder:
        ...
    def CreateFeatureControlFrameDataBuilder(self, frame: Annotations.FeatureControlFrameData) -> Annotations.FeatureControlFrameDataBuilder:
        ...
    def CreateDatumReferenceBuilder(self, datumReference: Annotations.FcfDatumReference) -> Annotations.DatumReferenceBuilder:
        ...
    def CreateEmptyDatumReferenceBuilder(self) -> Annotations.DatumReferenceBuilder:
        ...
    def CreateCompoundDatumReferenceBuilder(self) -> Annotations.CompoundDatumReferenceBuilder:
        ...
    def CreateEditLeaderBuilder(self, tableTag: DisplayableObject) -> Annotations.EditLeaderBuilder:
        ...
    def CreateComponentData(self, annotationTag: Annotations.Annotation) -> Annotations.ComponentData:
        ...
    def SetMasterSymbolNameInQaf(self) -> None:
        ...
    def CreateAssociativeText(self) -> Annotations.AssociativeText:
        ...
    def GetStandardSymbolTextFont(self) -> str:
        ...
    def SetStandardSymbolTextFont(self, symbolTextFontName: str) -> None:
        ...
    def CreatePmiTrackingPropertiesBuilder(self) -> Annotations.PmiTrackingPropertiesBuilder:
        ...
    def SetParallelToScreen(self, parallelToScreen: bool, annotations: typing.List[Annotations.Annotation]) -> None:
        ...
    def CreateFeatureControlFrameIndicatorBuilder(self) -> Annotations.FeatureControlFrameIndicatorBuilder:
        ...
    def CreateTextEditorBuilder(self, text: str) -> Annotations.TextEditorBuilder:
        ...
    def Tag(self) -> Tag: ...

    Preferences: Preferences.AnnotationPreferences
    PmiFilters: Annotations.PmiFilterCollection
    Fcfs: Annotations.FcfCollection
    Datums: Annotations.GdtDatumCollection
    DatumTargets: Annotations.DatumTargetCollection
    DraftingDatumTargets: Annotations.DraftingDatumTargetCollection
    Welds: Annotations.WeldCollection
    CustomSymbols: Annotations.CustomSymbolCollection
    IdSymbols: Annotations.IdSymbolCollection
    BusinessModifiers: Annotations.BusinessModifierCollection
    OrdinateMargins: Annotations.OrdinateMarginCollection
    DimensionSets: Annotations.DimensionSetCollection
    Centerlines: Annotations.CenterlineCollection
    IntersectionSymbols: Annotations.IntersectionSymbolCollection
    TargetPoints: Annotations.TargetPointCollection
    OffsetCenterPoints: Annotations.OffsetCenterPointCollection
    Hatches: Annotations.HatchCollection
    DraftingSurfaceFinishSymbols: Annotations.DraftingSurfaceFinishCollection
    PartSymbolFolders: Annotations.PartSymbolFolderCollection
    TableSections: Annotations.TableSectionCollection
    Tables: Annotations.TableCollection
    HoleTables: Annotations.HoleTableCollection
    PmiTableSections: Annotations.PmiTableSectionCollection
    PartsLists: Annotations.PartsListCollection
    FrameBars: Annotations.FrameBarCollection
    SymbolFiles: Annotations.SymbolFileCollection
    DraftingImages: Annotations.DraftingImageCollection
    BendTables: Annotations.BendTableCollection
    ProductGrids: Annotations.ProductGridCollection
    PartFamilyTables: Annotations.PartFamilyTableCollection
    EdgeConditionSymbol: Annotations.EdgeConditionSymbolCollection
    PmiEdgeConditionSymbol: Annotations.PmiEdgeConditionSymbolCollection
    CurrentSbfFile: str
    WeldStandard: Annotations.WeldStandard


class Annotation(DisplayableObject):
    def __init__(self) -> None: ...
    def GetAssociativeOrigin(self, origin: Point3d) -> Annotations.Annotation.AssociativeOriginData:
        ...
    def SetAssociativeOrigin(self, assocOrigin: Annotations.Annotation.AssociativeOriginData, origin: Point3d) -> None:
        ...
    def GetLetteringPreferences(self) -> Annotations.LetteringPreferences:
        ...
    def SetLetteringPreferences(self, letteringPrefs: Annotations.LetteringPreferences) -> None:
        ...
    def GetLineAndArrowPreferences(self) -> Annotations.LineAndArrowPreferences:
        ...
    def SetLineAndArrowPreferences(self, lineArrowPrefs: Annotations.LineAndArrowPreferences) -> None:
        ...
    def GetSymbolPreferences(self) -> Annotations.SymbolPreferences:
        ...
    def SetSymbolPreferences(self, symbolPrefs: Annotations.SymbolPreferences) -> None:
        ...
    def GetAssociativity(self, associativityIndex: int) -> Annotations.Associativity:
        ...
    def SetAssociativity(self, associativityIndex: int, associativity: Annotations.Associativity) -> None:
        ...
    def GetInferredAnnotationPlane(self, jaDefaultPlane: Annotations.PmiDefaultPlane) -> Xform:
        ...
    def GetViews(self) -> typing.List[View]:
        ...
    def SetViews(self, modelViews: typing.List[View]) -> None:
        ...
    def InsertIntoStack(self, stack: Annotations.Annotation, position: Annotations.StackAlignmentPosition) -> None:
        ...
    def RemoveFromStack(self) -> None:
        ...
    AnnotationOrigin: Point3d
    AnnotationPlane: Xform
    Freeze: bool
    HasAssociativeOrigin: bool
    IsOutOfDate: bool
    IsRetained: bool
    LeaderOrientation: Annotations.LeaderOrientation
    NumberOfAssociativities: int
    ParallelToScreen: bool
    Suppressed: bool


    class AnnotationAssociativeOriginData():
        OriginType: Annotations.AssociativeOriginType
        View: View
        ViewOfGeometry: View
        PointOnGeometry: Point
        VertAnnotation: Annotations.Annotation
        VertAlignmentPosition: Annotations.AlignmentPosition
        HorizAnnotation: Annotations.Annotation
        HorizAlignmentPosition: Annotations.AlignmentPosition
        AlignedAnnotation: Annotations.Annotation
        DimensionLine: int
        AssociatedView: View
        AssociatedPoint: Point
        OffsetAnnotation: Annotations.Annotation
        OffsetAlignmentPosition: Annotations.AlignmentPosition
        XOffsetFactor: float
        YOffsetFactor: float
        StackAlignmentPosition: Annotations.StackAlignmentPosition
        def ToString(self) -> str:
            ...
    

    class Annotation_AssociativeOriginData():
        origin_type: Annotations.AssociativeOriginType
        view: Tag
        view_of_geometry: Tag
        point_on_geometry: Tag
        vert_annotation: Tag
        vert_alignment_position: Annotations.AlignmentPosition
        horiz_annotation: Tag
        horiz_alignment_position: Annotations.AlignmentPosition
        aligned_annotation: Tag
        dimension_line: int
        associated_view: Tag
        associated_point: Tag
        offset_annotation: Tag
        offset_alignment_position: Annotations.AlignmentPosition
        x_offset_factor: float
        y_offset_factor: float
        stack_alignment_position: Annotations.StackAlignmentPosition
    

class AngularTolerance(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetUpperToleranceDegrees(self) -> Annotations.Value:
        ...
    def SetUpperToleranceDegrees(self, upperToleranceDegrees: Annotations.Value) -> None:
        ...
    def GetLowerToleranceDegrees(self) -> Annotations.Value:
        ...
    def SetLowerToleranceDegrees(self, lowerToleranceDegrees: Annotations.Value) -> None:
        ...
    DimensionDecimalPlaces: int
    ToleranceType: Annotations.ToleranceType
    ZeroToleranceDisplayStyle: Annotations.ZeroToleranceDisplayStyle


class AngularSuppressZeros(enum.Enum):
    None = 0
    Leading = 1
    Any = 2
    Trailing = 3
    Last = 4


class AngularDimensionUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetAngularDimensionUtils(self, owner: Session) -> Annotations.AngularDimensionUtils:
        ...
    def InferQuadrantAngleFromLocation(self, dimension: Annotations.Dimension, location: Point3d) -> bool:
        ...
    def GetAllowSupplementaryAngle(self, dimension: Annotations.Dimension) -> bool:
        ...
    def SetAllowSupplementaryAngle(self, dimension: Annotations.Dimension, allowSupplementaryAngle: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class AngularDimensionFormat(enum.Enum):
    FractionalDegrees = 0
    WholeDegrees = 1
    DegreesMinutes = 2
    DegreesMinutesSeconds = 3
    Last = 4


class AngularDimensionBuilder(Annotations.BaseAngularDimensionBuilder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder
    ForeshorteningSymbol: Annotations.ForeshorteningSymbolBuilder


class AngularDimension(Annotations.BaseAngularDimension):
    def __init__(self) -> None: ...


class AlignmentPosition(enum.Enum):
    TopLeft = 1
    TopCenter = 2
    TopRight = 3
    MidLeft = 4
    MidCenter = 5
    MidRight = 6
    BottomLeft = 7
    BottomCeneter = 8
    BottomCenter = 8
    BottomRight = 9


class AddTicBuilder(Builder):
    def __init__(self) -> None: ...
    def SelectTic(self, index: int) -> None:
        ...
    def ShowTic(self, ticIdentifier: str) -> None:
        ...
    def HideTic(self, ticIdentifier: str) -> None:
        ...


class _Value():
    item_value: float
    value_expression: Tag
    value_precision: int


