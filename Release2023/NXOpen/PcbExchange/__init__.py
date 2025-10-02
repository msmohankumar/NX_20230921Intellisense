from ...NXOpen import *
from ..PcbExchange import *

import typing
import enum

class TemplateBuilder(Builder):
    def __init__(self) -> None: ...
    AreaItemType: str
    AreaTemplate: int
    AssemblyItemType: str
    AssemblyTemplate: int
    BoardItemType: str
    BoardTemplate: int
    ComponentItemType: str
    ComponentTemplate: int
    FemItemType: str
    FemTemplate: int
    SimItemType: str
    SimTemplate: int
    SubAssemblyItemType: str
    SubAssemblyTemplate: int


class ReportBuilder(Builder):
    def __init__(self) -> None: ...
    ReportType: PcbExchange.ReportBuilder.TypeEnum


    class TypeEnum(enum.Enum):
        Validation = 0
        LightweightValidation = 1
        Component = 2
        ThermalDatabase = 3
    

class PreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMcadEntityFilter(self) -> PcbExchange.EntityFilter:
        ...
    def SetMcadEntityFilter(self, filter: PcbExchange.EntityFilter) -> None:
        ...
    def GetEcadEntityFilter(self) -> PcbExchange.EntityFilter:
        ...
    def SetEcadEntityFilter(self, filter: PcbExchange.EntityFilter) -> None:
        ...
    def GetAreaMapping(self) -> PcbExchange.AreaMapping:
        ...
    def SetAreaMapping(self, areaMapping: PcbExchange.AreaMapping) -> None:
        ...
    def GetMailRecipients(self) -> str:
        ...
    def SetMailRecipients(self, mMailRecipients: str) -> None:
        ...
    AreaNamePrefix: str
    AreaNameSuffix: str
    AreasAsAssemblyComponents: bool
    AssociateAreaBodies: bool
    AssociateComponentBodies: bool
    AutomaticallySaveAllCreatedParts: bool
    BoardAsAssemblyComponent: bool
    BoardColor: NXColor
    BoardDefaultPlatingThickness: Expression
    BoardDefaultThickness: Expression
    BoardDefaultTraceThickness: Expression
    BoardElementColor: NXColor
    BoardElementSize: Expression
    BoardLayer: int
    BoardNamePrefix: str
    BoardNameSuffix: str
    BoardThickness: Expression
    BoardThicknessSource: PcbExchange.PreferencesBuilder.BoardThicknessSourceTypeName
    BoardTranslucency: int
    BrowseEcadFilesFromDir: str
    ComparePrimaryPinLocations: bool
    ComponentLoadOptions: PcbExchange.PreferencesBuilder.ComponentLoadOptionsTypeName
    ComponentNamePrefix: str
    ComponentNameSuffix: str
    ComponentXMLFileBrowse: str
    ComponentsCaseMaterial: int
    ComponentsColor: NXColor
    ComponentsConnectionToBoard: PcbExchange.PreferencesBuilder.ComponentsConnectionToBoardTypeName
    ComponentsDefaultHeight: Expression
    ComponentsDefaultMass: Expression
    ComponentsDissipation: Expression
    ComponentsElementColor: NXColor
    ComponentsElementSizeOptions: PcbExchange.PreferencesBuilder.ComponentsElementSizeOptionsTypeName
    ComponentsElementSizeValue: Expression
    ComponentsElementThicknessOptions: PcbExchange.PreferencesBuilder.ComponentsElementThicknessOptionsTypeName
    ComponentsElementThicknessValue: Expression
    ComponentsHeightFrom: PcbExchange.PreferencesBuilder.ComponentsHeightFromTypeName
    ComponentsJunctionCapacitance: Expression
    ComponentsJunctionCapacity: Expression
    ComponentsMaterialFrom: PcbExchange.PreferencesBuilder.ComponentsMaterialFromTypeName
    ComponentsModel: PcbExchange.PreferencesBuilder.ComponentsModelTypeName
    ComponentsThetaCB: Expression
    ComponentsThetaJB: Expression
    ComponentsThetaJC: Expression
    ComponentsTmax: Expression
    ComponentsTmaxCase: Expression
    ComponentsTmaxJunction: Expression
    ComponentsTranslucency: int
    ConnectComponentsToPads: bool
    CreateNewComponentInDir: str
    CreateNewComponentsIn: PcbExchange.PreferencesBuilder.CreateNewComponentsInTypeName
    DefaultPcaName: PcbExchange.PreferencesBuilder.DefaultPcaNameTypeName
    EcadFilePostProcessor: str
    EcadFilePreProcessor: str
    EcadFloatTolerance: Expression
    EdmdDir: str
    ElementColorForStructuralAnalysis: NXColor
    ElementSizeForStructuralAnalysis: Expression
    ElementTypeForStructuralAnalysis: PcbExchange.PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName
    ErrorChecking: bool
    ExportBends: bool
    FilterEcadToggle: bool
    FilterMcadToggle: bool
    GenericMaxNumber: int
    GenericNamePrefix: str
    GenericNameSuffix: str
    GroupEntityComponentsBy: PcbExchange.PreferencesBuilder.GroupEntityComponentsByTypeName
    GroupPads: bool
    HolesDefaultDiameter: Expression
    IdfFloatPrecision: int
    IdfFloatWidth: int
    ImportBends: bool
    ImportExportFlexBent: PcbExchange.PreferencesBuilder.ImportExportFlexBentType
    ImportGenericMenu: PcbExchange.PreferencesBuilder.ImportGenericMenuTypeName
    ImportGenericToggle: bool
    ImportMaskMenu: PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName
    ImportMaskToggle: bool
    ImportPadMenu: PcbExchange.PreferencesBuilder.ImportPadMenuTypeName
    ImportPadToggle: bool
    ImportPasteMaskMenu: PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName
    ImportPasteMaskToggle: bool
    ImportTraceMenu: PcbExchange.PreferencesBuilder.ImportTraceMenuTypeName
    ImportTraceToggle: bool
    InternalLayers: bool
    KeepInColor: NXColor
    KeepInLayer: int
    KeepInTranslucency: int
    KeepOutColor: NXColor
    KeepOutLayer: int
    KeepOutTranslucency: int
    MailNotify: bool
    MailProtocol: PcbExchange.PreferencesBuilder.MailProtocolTypeName
    MaskMaxNumber: int
    MaskNamePrefix: str
    MaskNameSuffix: str
    MergeTracesAndPads: bool
    ModelForStructuralAnalysis: PcbExchange.PreferencesBuilder.ModelForStructuralAnalysisTypeName
    ModelForThermalAnalysis: PcbExchange.PreferencesBuilder.ModelForThermalAnalysisTypeName
    MonitorEDMDToggle: bool
    Negative: bool
    OtherColor: NXColor
    OtherLayer: int
    OtherTranslucency: int
    PadMaxNumber: int
    PadNamePrefix: str
    PadNameSuffix: str
    PasteMaskMaxNumber: int
    PasteMaskNamePrefix: str
    PasteMaskNameSuffix: str
    PcaNamePrefix: str
    PcaNameSuffix: str
    ProjectView: str
    ProjectViewToggle: bool
    ReadWriteDir: str
    ResistorModel: PcbExchange.PreferencesBuilder.ResistorModelTypeName
    SettingsSource: PcbExchange.PreferencesBuilder.SettingsSourceTypeName
    SpecifiedSettingsFolder: str
    SpecifyNewCompDir: str
    StructuralAlgorithm: PcbExchange.PreferencesBuilder.StructuralAlgorithmTypeName
    ThermalAlgorithm: PcbExchange.PreferencesBuilder.ThermalAlgorithmTypeName
    ThicknessForStructuralAnalysis: Expression
    ThicknessSourceForStructuralAnalysis: PcbExchange.PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName
    TraceMaxNumber: int
    TraceNamePrefix: str
    TraceNameSuffix: str


    class ThicknessSourceForStructuralAnalysisTypeName(enum.Enum):
        FromPart = 0
        Specify = 1
    

    class ThermalAlgorithmTypeName(enum.Enum):
        Discretized = 0
        Equivalent = 1
    

    class StructuralAlgorithmTypeName(enum.Enum):
        Equivalent = 0
    

    class SettingsSourceTypeName(enum.Enum):
        IniFiles = 0
        SpecifiedSettingsFolder = 1
        CustomerDefaults = 2
    

    class ResistorModelTypeName(enum.Enum):
        None = 0
        DissipationOnly = 1
        ThetaCB = 2
        ThetaJCJB = 3
        ThetaJCCB = 4
    

    class ModelForThermalAnalysisTypeName(enum.Enum):
        SingleLayer = 0
        TopAndBottom = 1
        MultiLayer = 2
        Solid = 3
    

    class ModelForStructuralAnalysisTypeName(enum.Enum):
        SingleLayer = 0
        MultiLayer = 1
    

    class MailProtocolTypeName(enum.Enum):
        Mapi = 0
        Smtp = 1
    

    class ImportTraceMenuTypeName(enum.Enum):
        Curves = 0
        Sheets = 1
        Bodies = 2
    

    class ImportPadMenuTypeName(enum.Enum):
        Curves = 0
        Sheets = 1
        Bodies = 2
    

    class ImportMaskMenuTypeName(enum.Enum):
        Curves = 0
        Sheets = 1
        Bodies = 2
    

    class ImportGenericMenuTypeName(enum.Enum):
        Curves = 0
        Sheets = 1
        Bodies = 2
    

    class ImportExportFlexBentType(enum.Enum):
        No = 0
        ExportOnly = 1
        ImportAndExport = 2
    

    class GroupEntityComponentsByTypeName(enum.Enum):
        None = 0
        Type = 1
        Layer = 2
    

    class ElementTypeForStructuralAnalysisTypeName(enum.Enum):
        Ctria3 = 0
        Cquad4 = 1
        Ctria6 = 2
        Cquad8 = 3
    

    class DefaultPcaNameTypeName(enum.Enum):
        CurrentNXModel = 0
        ECADModelName = 1
        SpecifyAtImport = 2
    

    class CreateNewComponentsInTypeName(enum.Enum):
        DirectoryOfECADFiles = 0
        DirectoryOfNXParts = 1
        Specify = 2
    

    class ComponentsModelTypeName(enum.Enum):
        ZeroResistor = 0
        OneResistor = 1
        TwoResistor = 2
        None = 3
    

    class ComponentsMaterialFromTypeName(enum.Enum):
        Pcb = 0
        Nx = 1
    

    class ComponentsHeightFromTypeName(enum.Enum):
        FootprintDefinition = 0
        PartDefinition = 1
    

    class ComponentsElementThicknessOptionsTypeName(enum.Enum):
        Null = 0
        Specify = 1
    

    class ComponentsElementSizeOptionsTypeName(enum.Enum):
        Auto = 0
        Specify = 1
    

    class ComponentsConnectionToBoardTypeName(enum.Enum):
        Rbe2 = 0
        Rbe3 = 1
    

    class ComponentLoadOptionsTypeName(enum.Enum):
        LoadAndCreateAssemblyComponents = 0
        CreateBodiesOnly = 1
        LoadAssemblyComponentsCreateBodies = 2
    

    class BoardThicknessSourceTypeName(enum.Enum):
        FromPart = 0
        Specify = 1
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class Manager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetManager(self, owner: Session) -> PcbExchange.Manager:
        ...
    def CreateBoardAttributesBuilder(self, part: NXObject) -> PcbExchange.BoardAttributesBuilder:
        ...
    def CreateComponentAttributesBuilder(self, part: NXObject) -> PcbExchange.ComponentAttributesBuilder:
        ...
    def CreateHoleAttributesBuilder(self, part: NXObject) -> PcbExchange.HoleAttributesBuilder:
        ...
    def CreateAreaAttributesBuilder(self, part: NXObject) -> PcbExchange.AreaAttributesBuilder:
        ...
    def CreateEcadImportBuilder(self, part: NXObject) -> PcbExchange.EcadImportBuilder:
        ...
    def CreateEcadExportBuilder(self, part: NXObject) -> PcbExchange.EcadExportBuilder:
        ...
    def CreateCompareAndUpdateBuilder(self, part: NXObject) -> PcbExchange.CompareAndUpdateBuilder:
        ...
    def CreateIdxImportBuilder(self, part: NXObject) -> PcbExchange.IdxImportBuilder:
        ...
    def CreateIdxExportBuilder(self, part: NXObject) -> PcbExchange.IdxExportBuilder:
        ...
    def CreateIdxCompareBuilder(self, part: NXObject) -> PcbExchange.IdxCompareBuilder:
        ...
    def CreateBoardPropertiesBuilder(self, part: NXObject) -> PcbExchange.BoardPropertiesBuilder:
        ...
    def CreateEntityFilterBuilder(self, part: NXObject, entityFilter: PcbExchange.EntityFilter) -> PcbExchange.EntityFilterBuilder:
        ...
    def CreateDesignRuleBuilder(self, part: NXObject) -> PcbExchange.DesignRuleBuilder:
        ...
    def CreateDesignRuleBuilder(self, ruleToEdit: PcbExchange.DesignRule) -> PcbExchange.DesignRuleBuilder:
        ...
    def CreateDesignValidator(self, part: NXObject) -> PcbExchange.DesignValidator:
        ...
    def CreateEcadPanelImportBuilder(self, part: NXObject) -> PcbExchange.EcadPanelImportBuilder:
        ...
    def CreateExternalDataImportBuilder(self, part: NXObject) -> PcbExchange.ExternalDataImportBuilder:
        ...
    def ReplaceWithLibraryComponent(self, components: typing.List[NXObject]) -> None:
        ...
    def CreateReportBuilder(self, part: NXObject) -> PcbExchange.ReportBuilder:
        ...
    def CreatePreferencesBuilder(self, part: NXObject) -> PcbExchange.PreferencesBuilder:
        ...
    def CreateIncrementalImportBuilder(self, part: NXObject) -> PcbExchange.IncrementalImportBuilder:
        ...
    def TagModelAsBaseline(self) -> None:
        ...
    def CreateIncrementalExportBuilder(self, part: NXObject) -> PcbExchange.IncrementalExportBuilder:
        ...
    def CreateIncrementalChange(self) -> PcbExchange.IncrementalChange:
        ...
    def CreateAreaMappingBuilder(self, part: NXObject, areaMapping: PcbExchange.AreaMapping) -> PcbExchange.AreaMappingBuilder:
        ...
    def CreateAdvancedConductivityBuilder(self, part: NXObject) -> PcbExchange.AdvancedConductivityBuilder:
        ...
    def CreateTemplateBuilder(self, part: NXObject) -> PcbExchange.TemplateBuilder:
        ...
    def PrintPcbxAssembly(self, validateLayers: bool, validateBoard: bool, validateComponents: bool, validateAreas: bool, validateHoles: bool, validateTraces: bool, validatePads: bool, validateSymbols: bool, validateTestPoints: bool, validateDrawing: bool, validateMasks: bool, validateGenericShapes: bool, validateNets: bool, validateVariants: bool) -> None:
        ...
    def PrepareSmartDiffFiles(self, fileName: str, masterFile: str, diffFile: str) -> None:
        ...
    def PrintPreferences(self, fileName: str) -> None:
        ...
    def CreateComponentPlacementOutlineBuilder(self, part: NXObject) -> PcbExchange.ComponentPlacementOutlineBuilder:
        ...
    def SuspendNavigatorUpdate(self) -> None:
        ...
    def ResumeNavigatorUpdate(self, refreshNavigator: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class IncrementalImportBuilder(Builder):
    def __init__(self) -> None: ...
    def AcceptAll(self) -> None:
        ...
    def RejectAll(self) -> None:
        ...
    def AcknowledgeAll(self) -> None:
        ...
    def IgnoreAll(self) -> None:
        ...
    def AcknowledgeResponse(self, id: str) -> None:
        ...
    def IgnoreResponse(self, id: str) -> None:
        ...
    def AcceptChange(self, id: str) -> None:
        ...
    def RejectChange(self, id: str) -> None:
        ...
    def RejectBoardChange(self, id: str) -> None:
        ...
    def AcceptBoardChange(self, id: str) -> None:
        ...
    def AddNewComment(self, id: str, comment: str) -> None:
        ...
    def PreviewChanges(self) -> None:
        ...
    def UnhighlightAll(self) -> None:
        ...
    def ReadImportFile(self) -> None:
        ...
    def SetExistingPart(self) -> DisplayableObject:
        ...
    def SetBoardUpdated(self, updated: bool) -> None:
        ...
    def CancelIncrementReview(self) -> None:
        ...
    def ClearProcessedIncrementalGroupVec(self) -> None:
        ...
    Filename: str
    Output: str


class IncrementalExportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetIncrementalChanges(self) -> typing.List[PcbExchange.IncrementalChange]:
        ...
    def SetIncrementalChanges(self, changes: typing.List[PcbExchange.IncrementalChange]) -> None:
        ...
    def RunPreExportIncrementalHook(self) -> None:
        ...
    CloneAssembly: bool
    FileFormat: PcbExchange.IncrementalExportBuilder.FormatEnum
    FileNote: str
    Output: str
    SelectedObjects: SelectNXObjectList
    TargetLocation: PcbExchange.IncrementalExportBuilder.TargetLocationEnum
    UseCloneSelection: bool


    class TargetLocationEnum(enum.Enum):
        Os = 0
        TeamcenterCS = 1
    

    class FormatEnum(enum.Enum):
        Idx2 = 0
        Idx3 = 1
    

class IncrementalChange(TaggedObject):
    def __init__(self) -> None: ...
    def GetAttributes(self, names: str) -> str:
        ...
    Accepted: bool
    Comments: str
    Transaction: str


class IdxImportBuilder(Builder):
    def __init__(self) -> None: ...
    AssemblyName: str
    AssemblyNumber: str
    AssemblyRevision: str
    BaselineFile: str
    CollaborationDir: str
    IdxDataFrom: PcbExchange.IdxImportBuilder.DataLocation
    IdxNumber: str
    IdxRevision: str
    OutputPartFile: str
    UseCurrentPart: bool
    UseExistComp: bool


    class DataLocation(enum.Enum):
        Local = 0
        TeamcenterDS = 1
        TeamcenterCS = 2
    

class IdxExportBuilder(Builder):
    def __init__(self) -> None: ...
    def RunPreExportBaselineHook(self) -> None:
        ...
    BaselineFile: str
    BaselineLocation: PcbExchange.IdxExportBuilder.IdxLocationEnum
    BaselineNumber: str
    BaselineRevision: str
    CloneAssembly: bool
    FileFormat: PcbExchange.IdxExportBuilder.FileFormatEnum
    FileNote: str
    FileUnits: PcbExchange.IdxExportBuilder.ExportUnitsEnum
    SelectedObjects: SelectNXObjectList
    ShowLog: bool
    TagModel: bool
    UseCloneSelection: bool
    UseCurrentWorkPart: bool


    class IdxLocationEnum(enum.Enum):
        Os = 0
        TeamcenterDS = 1
        TeamcenterCS = 2
    

    class FileFormatEnum(enum.Enum):
        Idx2 = 0
        Idx3 = 1
    

    class ExportUnitsEnum(enum.Enum):
        Mm = 0
        Thou = 1
    

class IdxCompareBuilder(Builder):
    def __init__(self) -> None: ...
    SourceFile: str
    SourceType: PcbExchange.IdxCompareBuilder.SourceTypeEnum
    TargetFile: str


    class SourceTypeEnum(enum.Enum):
        Nx = 0
        Idx = 1
    

class HoleAttributesBuilder(Builder):
    def __init__(self) -> None: ...
    AssociatedPart: PcbExchange.HoleAttributesBuilder.AssociatedPartEnum
    Features: Features.SelectFeatureList
    HoleType: PcbExchange.HoleAttributesBuilder.TypeEnum
    Owner: PcbExchange.HoleAttributesBuilder.OwnerEnum
    PlatingStyle: PcbExchange.HoleAttributesBuilder.PlatingStyleEnum
    SpecifiedPart: str


    class TypeEnum(enum.Enum):
        Pin = 1
        Via = 2
        Mounting = 3
        Tool = 4
        Other = 5
    

    class PlatingStyleEnum(enum.Enum):
        PlatedThru = 1
        NonPlatedThru = 2
    

    class OwnerEnum(enum.Enum):
        Mcad = 1
        Ecad = 2
        Unowned = 3
    

    class AssociatedPartEnum(enum.Enum):
        Board = 1
        Norefdes = 2
        Specify = 3
    

class ExternalDataImportBuilder(Builder):
    def __init__(self) -> None: ...
    def QueryEntities(self) -> None:
        ...
    def GetLayerNames(self) -> str:
        ...
    def GetLayerImported(self, name: str) -> PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        ...
    def SetLayerImported(self, name: str, importOption: PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        ...
    def GetNetNames(self) -> str:
        ...
    def GetNetImported(self, name: str) -> PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        ...
    def SetNetImported(self, name: str, importOption: PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        ...
    def GetPadstackNames(self) -> str:
        ...
    def GetPadstackImported(self, name: str) -> PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        ...
    def SetPadstackImported(self, name: str, importOption: PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        ...
    def GetPadstackPart(self, name: str) -> str:
        ...
    def SetPadstackPart(self, name: str, part: str) -> None:
        ...
    Filename: str
    NetsFilterString: str
    NetsFilterStringEnabled: bool
    ShowLog: bool


    class JaPcbExternalDataImportBuilderImportoption(enum.Enum):
        Import = 0
        DoNotImport = 1
    

class ExtdataUpdator(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetExtdataUpdator(self, owner: Session) -> PcbExchange.ExtdataUpdator:
        ...
    def Read(self, fName: str, layerNames: str) -> str:
        ...
    def Update(self, fName: str, layerNames: str, netNames: str, bTextualFilter: bool, textualFilterStr: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class EntityFilterBuilder(Builder):
    def __init__(self) -> None: ...
    def SetUserDefiniedFilters(self, filters: str) -> None:
        ...
    ComponentMaxHeight: float
    ComponentMaxSize: float
    ComponentMinHeight: float
    ComponentMinSize: float
    HoleMaxDiameter: float
    HoleMaxSize: float
    HoleMinDiameter: float
    HoleMinSize: float
    LengthUnits: PcbExchange.EntityFilterBuilder.LengthUnitsEnum
    RemoveBlindBuriedViaHoles: bool
    RemoveComponentsWithHeight: bool
    RemoveComponentsWithSize: bool
    RemoveEcadComponents: bool
    RemoveHolesWithDiameter: bool
    RemoveHolesWithSize: bool
    RemoveMcadComponents: bool
    RemoveMountingHoles: bool
    RemoveOtherHoles: bool
    RemoveOtherKeepoutAreas: bool
    RemovePinHoles: bool
    RemovePlacedComponents: bool
    RemovePlacementGroupKeepinAreas: bool
    RemovePlacementKeepinAreas: bool
    RemovePlacementKeepoutAreas: bool
    RemoveRoutingKeepinAreas: bool
    RemoveRoutingKeepoutAreas: bool
    RemoveToolingHoles: bool
    RemoveUnplacedComponents: bool
    RemoveViaHoles: bool
    RemoveViaKeepoutAreas: bool


    class LengthUnitsEnum(enum.Enum):
        Millimeters = 0
        Inches = 1
    

class EntityFilter(NXObject):
    def __init__(self) -> None: ...


class EntityCategory(enum.Enum):
    Component = 0
    Board = 1
    Mechanical = 2
    KeepOut = 3
    Copper = 4


class EcadPanelImportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetOutputParts(self) -> str:
        ...
    def SetOutputParts(self, outputsParts: str) -> None:
        ...
    def GetOutputNames(self) -> str:
        ...
    def SetOutputNames(self, outputsNames: str) -> None:
        ...
    def PrepareOdbFolder(self) -> str:
        ...
    def GetEntityFilter(self) -> PcbExchange.EntityFilter:
        ...
    def SetEntityFilter(self, filter: PcbExchange.EntityFilter) -> None:
        ...
    Breakaway: bool
    IsPanelFolder: bool
    OptimizationMethod: PcbExchange.EcadPanelImportBuilder.OptimizationMethodOptions
    PanelFile: str
    PanelFolder: str
    PanelLocation: PcbExchange.EcadPanelImportBuilder.PanelLocationEnum
    ShowLog: bool
    SolderMasks: bool
    TcItemNumber: str
    TcItemRevision: str
    Thieving: PcbExchange.EcadPanelImportBuilder.ThievingOptions
    UseCurrentWorkPart: bool
    UseEntityFilter: bool


    class ThievingOptions(enum.Enum):
        None = 0
        Curve = 1
        SolidBody = 2
    

    class PanelLocationEnum(enum.Enum):
        Os = 0
        Tc = 1
    

    class OptimizationMethodOptions(enum.Enum):
        None = 0
        Pattern = 1
    

class EcadImportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetEntityFilter(self) -> PcbExchange.EntityFilter:
        ...
    def SetEntityFilter(self, filter: PcbExchange.EntityFilter) -> None:
        ...
    BoardFile: str
    BoardFolder: str
    BoardThickness: Expression
    EcadLocation: PcbExchange.EcadImportBuilder.EcadLocationEnum
    EcadNumber: str
    EcadRevision: str
    ImportOption: PcbExchange.EcadImportBuilder.ImportOptionEnum
    IsOdbFolder: bool
    LibraryFile: str
    OnlyUseExistingComponents: bool
    OutputPart: str
    OverrideBoardThickness: bool
    PartName: str
    PartNumber: str
    PartRevision: str
    ShowLog: bool
    UseCurrentWorkPart: bool
    UseEntityFilter: bool


    class ImportOptionEnum(enum.Enum):
        All = 0
        BoardOnly = 1
    

    class EcadLocationEnum(enum.Enum):
        Os = 0
        Tc = 1
    

class EcadExportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetEntityFilter(self) -> PcbExchange.EntityFilter:
        ...
    def SetEntityFilter(self, filter: PcbExchange.EntityFilter) -> None:
        ...
    def GetAreaMapping(self) -> PcbExchange.AreaMapping:
        ...
    def SetAreaMapping(self, areaMapping: PcbExchange.AreaMapping) -> None:
        ...
    def RunPreExportEcadHook(self) -> None:
        ...
    BoardFile: str
    BoardOnly: bool
    EcadLocation: PcbExchange.EcadExportBuilder.EcadLocationEnum
    EcadNumber: str
    EcadRevision: str
    FileFormat: PcbExchange.EcadExportBuilder.FileFormatEnum
    FileUnits: PcbExchange.EcadExportBuilder.ExportUnitsEnum
    LibraryFile: str
    ShowLog: bool
    UseCurrentWorkPart: bool
    UseEntityFilter: bool


    class FileFormatEnum(enum.Enum):
        Idf2 = 0
        Idf3 = 1
        Idf4 = 2
        Zbmb = 3
        Zpcb = 4
        Idx2 = 5
        Idx3 = 6
    

    class ExportUnitsEnum(enum.Enum):
        Mm = 0
        Thou = 1
    

    class EcadLocationEnum(enum.Enum):
        Os = 0
        Tc = 1
    

class DesignValidator(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetInterferences(self) -> typing.List[PcbExchange.DesignInterference]:
        ...
    def PerformAnalysis(self) -> None:
        ...
    def ResetAnalysis(self) -> None:
        ...
    def ExportInterferences(self, filename: str) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    InterferenceCount: int


class DesignRuleType(enum.Enum):
    Ortho = 0
    Distance = 1
    EdgeToEdge = 2


class DesignRuleSeverity(enum.Enum):
    Minimum = 0
    Optimal = 1


class DesignRuleMargin(enum.Enum):
    OrthoXY = 0
    OrthoZ = 1
    Xyz = 2
    LongToLong = 3
    ShortToShort = 4
    LongToShort = 5
    ShortToLong = 6
    Z = 7


class DesignRuleBuilder(Builder):
    def __init__(self) -> None: ...
    def GetEntityType(self, filterIndex: int) -> PcbExchange.EntityCategory:
        ...
    def SetEntityType(self, filterIndex: int, entityType: PcbExchange.EntityCategory) -> None:
        ...
    def GetComponentFilter(self, filterIndex: int) -> PcbExchange.DesignRuleBuilder.ComponentFilter:
        ...
    def SetComponentFilter(self, filterIndex: int, componentFilter: PcbExchange.DesignRuleBuilder.ComponentFilter) -> None:
        ...
    def GetFilterData(self, filterIndex: int) -> str:
        ...
    def SetFilterData(self, filterIndex: int, data: str) -> None:
        ...
    def SetFilterData(self, filterIndex: int, data: str) -> None:
        ...
    def GetBoardSide(self, filterIndex: int) -> PcbExchange.BoardSide:
        ...
    def SetBoardSide(self, filterIndex: int, side: PcbExchange.BoardSide) -> None:
        ...
    def GetConductiveLayerSide(self, filterIndex: int) -> PcbExchange.ConductiveLayerSide:
        ...
    def SetConductiveLayerSide(self, filterIndex: int, side: PcbExchange.ConductiveLayerSide) -> None:
        ...
    def GetClearance(self, direction: PcbExchange.DesignRuleMargin) -> float:
        ...
    def SetClearance(self, direction: PcbExchange.DesignRuleMargin, clearance: float) -> None:
        ...
    ConstraintType: PcbExchange.DesignRuleType
    Name: str
    Severity: PcbExchange.DesignRuleSeverity


    class ComponentFilter(enum.Enum):
        Any = 0
        ByPackage = 1
        ByOwner = 2
        ByRefDes = 3
        ByPartNumber = 4
        ByCompType = 5
        ByPartName = 6
        ByAreaName = 7
        ByAreaSubtype = 8
        ByAreaOwner = 9
        ByAreaLayer = 10
        Specify = 11
        ByNetName = 12
        ByPackageClearanceType = 13
    

class DesignRule(TaggedObject):
    def __init__(self) -> None: ...
    def IncreasePriority(self) -> PcbExchange.DesignRule:
        ...
    def DecreasePriority(self) -> PcbExchange.DesignRule:
        ...
    def Destroy(self) -> None:
        ...
    Name: str


class DesignInterference(TaggedObject):
    def __init__(self) -> None: ...
    Rule: PcbExchange.DesignRule
    RuleName: str


class ConductiveLayerSide(enum.Enum):
    All = 0
    Top = 1
    Bottom = 2
    Outer = 3
    Inner = 4


class ComponentPlacementOutlineBuilder(Builder):
    def __init__(self) -> None: ...
    Sketch: SelectTaggedObjectList


class ComponentAttributesBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPackageClearanceTypes(self) -> str:
        ...
    def SetPackageClearanceTypes(self, data: str) -> None:
        ...
    Components: SelectNXObjectList
    PackageClearanceTypesModification: bool
    PackageName: str
    PackageNameModification: bool
    PartNumber: str
    PartNumberModification: bool
    PlacementOwner: PcbExchange.ComponentAttributesBuilder.PlacementOwnerEnum
    ReferenceDesignator: str
    ReferenceDesignatorModification: bool


    class PlacementOwnerEnum(enum.Enum):
        Mcad = 0
        Ecad = 1
        Placed = 2
        Unplaced = 3
    

class CompareAndUpdateBuilder(Builder):
    def __init__(self) -> None: ...
    def Compare(self) -> None:
        ...
    def SetUpdateOption(self, resDef: str, status: bool) -> None:
        ...
    def PreviewChanges(self) -> None:
        ...
    def UnhighlightAll(self) -> None:
        ...
    AssemblyUpdateOptions: PcbExchange.CompareAndUpdateBuilder.AssemblyUpdateEnum
    BoardFile: str
    BoardFolder: str
    BoardThickness: Expression
    BoardUpdateOptions: PcbExchange.CompareAndUpdateBuilder.BoardUpdateEnum
    CompareOptions: PcbExchange.CompareAndUpdateBuilder.CompareEnum
    ECADEntityFilter: PcbExchange.EntityFilter
    FilterEcadModel: bool
    FilterNxModel: bool
    FromOdbFolder: bool
    LibraryFile: str
    NXEntityFilter: PcbExchange.EntityFilter
    OnlyUseExistingComponents: bool
    OverrideBoardThickness: bool
    ShowLog: bool


    class CompareEnum(enum.Enum):
        All = 0
        BoardOnly = 1
    

    class BoardUpdateEnum(enum.Enum):
        All = 0
        None = 1
    

    class AssemblyUpdateEnum(enum.Enum):
        All = 0
        None = 1
        Specify = 2
    

class BoardSide(enum.Enum):
    Both = 0
    Top = 1
    Bottom = 2


class BoardPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    AdvancedOptionsFromFile: bool
    AdvancedOptionsFromPart: bool
    BoardPropertyFile: str
    BoardStackup: PcbExchange.BoardPropertiesBuilder.BoardStackupOption
    BoardStackupFile: str
    BoardStackupODBFolder: str
    CalculationPointsPrecision: int
    DefaultHolePlatingThickness: Expression
    DielectricNxMaterial: int
    DielectricPcbMaterial: int
    MaterialsFrom: PcbExchange.BoardPropertiesBuilder.MaterialsFromOption
    NumberOfCalculationPoints: int
    ReadViasFromFile: bool
    StructuralAlgorithm: PcbExchange.BoardPropertiesBuilder.StructuralAlgorithmOption
    ThermalAlgorithm: PcbExchange.BoardPropertiesBuilder.ThermalAlgorithmOption
    TraceNxMaterial: int
    TracePcbMaterial: int
    ViaNxMaterial: int
    ViaPcbMaterial: int
    ViewCalculationReport: bool


    class ThermalAlgorithmOption(enum.Enum):
        Discretized = 0
        Equivalent = 1
    

    class StructuralAlgorithmOption(enum.Enum):
        Equivalent = 0
    

    class MaterialsFromOption(enum.Enum):
        PCBMaterialLibrary = 0
        NXMaterialLibrary = 1
    

    class BoardStackupOption(enum.Enum):
        FromPart = 0
        FromFile = 1
        FromODB = 2
    

class BoardAttributesBuilder(Builder):
    def __init__(self) -> None: ...
    BoardFeature: SelectBody
    CsysSelection: Features.SelectDatumCsys
    Owner: PcbExchange.BoardAttributesBuilder.OwnerEnum
    Part: str
    Revision: int


    class OwnerEnum(enum.Enum):
        Unowned = 0
        Mcad = 1
        Ecad = 2
    

class AttributeRemover(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetAttributeRemover(self, owner: Session) -> PcbExchange.AttributeRemover:
        ...
    def RemoveAttributes(self, action: PcbExchange.AttributeRemover.Option, objTags: typing.List[TaggedObject]) -> None:
        ...
    def Tag(self) -> Tag: ...



    class Option(enum.Enum):
        Board = 0
        Components = 1
        Areas = 2
        Holes = 3
        Traces = 4
        Pads = 5
        All = 6
    

class AreaMappingBuilder(Builder):
    def __init__(self) -> None: ...
    def SetKeepinAreas(self, keepinAreaList: str) -> None:
        ...
    def SetKeepoutAreas(self, keepoutAreaList: str) -> None:
        ...
    def SetOtherAreas(self, otherAreaList: str) -> None:
        ...
    def SetCopperAreas(self, copperAreaList: str) -> None:
        ...
    def PrintMapping(self) -> None:
        ...


class AreaMapping(NXObject):
    def __init__(self) -> None: ...


class AreaAttributesBuilder(Builder):
    def __init__(self) -> None: ...
    AreaType: PcbExchange.AreaAttributesBuilder.TypeEnum
    Color: int
    Height: Expression
    InvertedVolume: bool
    Layer: PcbExchange.AreaAttributesBuilder.LayerEnum
    Name: str
    Objects: SelectNXObjectList
    Owner: PcbExchange.AreaAttributesBuilder.OwnerEnum
    Subtype: str


    class TypeEnum(enum.Enum):
        Keepout = 0
        Keepin = 1
        Other = 2
        Copper = 3
    

    class OwnerEnum(enum.Enum):
        Unowned = 0
        Mcad = 1
        Ecad = 2
    

    class LayerEnum(enum.Enum):
        Current = 0
        Both = 1
        Inner = 2
        All = 3
    

class AdvancedConductivityBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTextualFilter(self) -> bool:
        ...
    def SetTextualFilter(self, filter: bool) -> None:
        ...
    def GetNetsToFilterString(self) -> str:
        ...
    def SetNetsToFilterString(self, nets: str) -> None:
        ...
    def GetNetsList(self, nets: str) -> None:
        ...
    def SetNetsList(self, nets: str) -> None:
        ...
    def GetPadstacks(self, padstacks: str) -> None:
        ...
    def SetPadstacks(self, nets: str) -> None:
        ...
    def GetTypes(self, types: int) -> None:
        ...
    def SetTypes(self, types: int) -> None:
        ...
    def GetDiameters(self, diameters: float) -> None:
        ...
    def SetDiameters(self, diameters: float) -> None:
        ...
    def GetStartLayers(self, startLayers: int) -> None:
        ...
    def SetStartLayers(self, startLayers: int) -> None:
        ...
    def GetEndLayers(self, endLayers: int) -> None:
        ...
    def SetEndLayers(self, endLayers: int) -> None:
        ...
    def GetT(self, t: int) -> None:
        ...
    def SetT(self, t: int) -> None:
        ...
    def GetHolesCounts(self, holesCounts: int) -> None:
        ...
    def SetHolesCounts(self, holesCounts: int) -> None:
        ...
    def GetPlatingThicknesses(self, platingThicknesses: float) -> None:
        ...
    def SetPlatingThicknesses(self, platingThicknesses: float) -> None:
        ...
    def GetPlatingMaterials(self, platingMaterials: int) -> None:
        ...
    def SetPlatingMaterials(self, platingMaterials: int) -> None:
        ...
    def GetFilled(self, bFilleds: bool) -> None:
        ...
    def SetFilled(self, bFilleds: int) -> None:
        ...
    def GetFillMaterials(self, fillMaterials: int) -> None:
        ...
    def SetFillMaterials(self, fillMaterials: int) -> None:
        ...


