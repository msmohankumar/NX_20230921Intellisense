from ....NXOpen import *
from ...SIM import *
from ..PostConfigurator import *

import typing
import enum

class UpdatePostprocessorBuilder(Builder):
    def __init__(self) -> None: ...
    CreateBackup: bool
    CurrentPostprocessorVersion: str
    PostRegistryPath: str
    UpdatePostprocessor: SIM.PostConfigurator.UpdatePostprocessorBuilder.UpdatePostprocessorType
    UpdateToVersion: str


    class UpdatePostprocessorType(enum.Enum):
        FromCurrentNXVersion = 0
        FromPostRegistry = 1
        Kinematic = 2
    

class UdeParameterBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[SIM.PostConfigurator.UdeParameterBuilder]) -> None:
        ...
    def Append(self, object: SIM.PostConfigurator.UdeParameterBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: SIM.PostConfigurator.UdeParameterBuilder) -> int:
        ...
    def FindItem(self, index: int) -> SIM.PostConfigurator.UdeParameterBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: SIM.PostConfigurator.UdeParameterBuilder) -> None:
        ...
    def Erase(self, obj: SIM.PostConfigurator.UdeParameterBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[SIM.PostConfigurator.UdeParameterBuilder]:
        ...
    def SetContents(self, objects: typing.List[SIM.PostConfigurator.UdeParameterBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: SIM.PostConfigurator.UdeParameterBuilder, object2: SIM.PostConfigurator.UdeParameterBuilder) -> None:
        ...
    def Insert(self, location: int, object: SIM.PostConfigurator.UdeParameterBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class UdeParameterBuilder(Builder):
    def __init__(self) -> None: ...
    def GetEnumerationItems(self) -> str:
        ...
    def SetEnumerationItems(self, enumerationItems: str) -> None:
        ...
    def SetGroup(self, parentBuilder: SIM.PostConfigurator.UdeParameterBuilder) -> None:
        ...
    DoubleDefaultValue: float
    EnumerationDefaultValue: str
    GroupState: SIM.PostConfigurator.UdeParameterBuilder.GroupStateType
    IntegerDefaultValue: int
    ItemType: SIM.PostConfigurator.UdeParameterBuilder.Type
    ParameterID: str
    ParameterStatus: SIM.PostConfigurator.UdeParameterBuilder.ParameterStatusType
    StringDefaultValue: str
    ToggleDefaultValue: bool
    UILabel: str


    class Type(enum.Enum):
        Group = 0
        Double = 1
        Integer = 2
        String = 3
        Boolean = 4
        Enumeration = 5
        Vector = 6
        Point = 7
        Bitmap = 8
    

    class ParameterStatusType(enum.Enum):
        None = 0
        On = 1
        Off = 2
    

    class GroupStateType(enum.Enum):
        Open = 0
        Closed = 1
        End = 2
    

class UdeEditorBuilder(Builder):
    def __init__(self) -> None: ...
    def GetUdeBuilder(self, eventHandlerID: str) -> SIM.PostConfigurator.UdeBuilder:
        ...
    def AddNewEvent(self) -> SIM.PostConfigurator.UdeBuilder:
        ...
    def DuplicateEvent(self, udeBuilder: SIM.PostConfigurator.UdeBuilder) -> SIM.PostConfigurator.UdeBuilder:
        ...
    def RemoveEvent(self, udeBuilder: SIM.PostConfigurator.UdeBuilder) -> None:
        ...
    def ListEvent(self, udeBuilder: SIM.PostConfigurator.UdeBuilder) -> None:
        ...
    UdeBuilderList: SIM.PostConfigurator.UdeBuilderList


class UdeBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[SIM.PostConfigurator.UdeBuilder]) -> None:
        ...
    def Append(self, object: SIM.PostConfigurator.UdeBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: SIM.PostConfigurator.UdeBuilder) -> int:
        ...
    def FindItem(self, index: int) -> SIM.PostConfigurator.UdeBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: SIM.PostConfigurator.UdeBuilder) -> None:
        ...
    def Erase(self, obj: SIM.PostConfigurator.UdeBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[SIM.PostConfigurator.UdeBuilder]:
        ...
    def SetContents(self, objects: typing.List[SIM.PostConfigurator.UdeBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: SIM.PostConfigurator.UdeBuilder, object2: SIM.PostConfigurator.UdeBuilder) -> None:
        ...
    def Insert(self, location: int, object: SIM.PostConfigurator.UdeBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class UdeBuilder(Builder):
    def __init__(self) -> None: ...
    def AddItem(self, itemBuilder: SIM.PostConfigurator.UdeParameterBuilder) -> None:
        ...
    def DeleteItem(self, itemBuilder: SIM.PostConfigurator.UdeParameterBuilder) -> None:
        ...
    def DeleteItems(self) -> None:
        ...
    def GetUdeParameterBuilder(self, parameterID: str) -> SIM.PostConfigurator.UdeParameterBuilder:
        ...
    def RenameParameterID(self, itemBuilder: SIM.PostConfigurator.UdeParameterBuilder, oldParameterID: str, newParameterID: str) -> None:
        ...
    EventCategoryDrilling: bool
    EventCategoryMilling: bool
    EventCategoryTurning: bool
    EventCategoryWireEDM: bool
    EventDescription: SIM.PostConfigurator.UdeBuilder.EventDescriptionType
    EventHelpDescription: str
    EventHelpLocation: str
    EventID: str
    EventName: str
    PostEvent: str
    UdeParameterList: SIM.PostConfigurator.UdeParameterBuilderList


    class EventDescriptionType(enum.Enum):
        None = 0
        Specify = 1
    

class ScannerPostBuilder(Builder):
    def __init__(self) -> None: ...
    BrowseNcFile: str
    CreateDirectoryForPostprocessor: bool
    PostprocessorName: str
    PostprocessorOutputDirectory: str


class PostConfiguratorManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateScannerPostBuilder(self) -> SIM.PostConfigurator.ScannerPostBuilder:
        ...
    def CreateCreationPostBuilder(self) -> SIM.PostConfigurator.CreationPostBuilder:
        ...
    def CreatePostConfiguratorBuilder(self, postProcessorFilename: str) -> SIM.PostConfigurator.PostConfiguratorBuilder:
        ...
    def CreateUdeBuilder(self) -> SIM.PostConfigurator.UdeBuilder:
        ...
    def CreateUdeParameterBuilder(self) -> SIM.PostConfigurator.UdeParameterBuilder:
        ...
    def CreatePostConfiguratorDebugBuilder(self) -> SIM.PostConfigurator.PostConfiguratorDebugBuilder:
        ...
    def CreateEncryptPostprocessorFilesBuilder(self, postProcessorFilename: str) -> SIM.PostConfigurator.EncryptPostprocessorFilesBuilder:
        ...
    def Tag(self) -> Tag: ...



class PostConfiguratorDebugBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTrace(self, type: SIM.PostConfigurator.PostConfiguratorDebugBuilder.TraceType) -> bool:
        ...
    def SetTrace(self, type: SIM.PostConfigurator.PostConfiguratorDebugBuilder.TraceType, state: bool) -> None:
        ...
    Dump: SIM.PostConfigurator.PostConfiguratorDebugBuilder.DumpType
    Output: SIM.PostConfigurator.PostConfiguratorDebugBuilder.OutputType
    OutputToFileName: str


    class TraceType(enum.Enum):
        CreatePostprocessor = 0
        SelectPostprocessor = 1
    

    class OutputType(enum.Enum):
        Syslog = 0
        ListingWindow = 1
        Xml = 2
        ToFile = 3
    

    class DumpType(enum.Enum):
        None = 0
        ShowChanges = 1
    

class PostConfiguratorBuilder(Builder):
    def __init__(self) -> None: ...
    def Reset(self) -> None:
        ...
    def ShowChanges(self) -> None:
        ...
    def EncryptPostConfiguratorFiles(self, soldToID: str, expirationDate: str) -> None:
        ...
    def EncryptPostConfiguratorFile(self, sourceFile: str, destFile: str, soldToID: str, expirationDate: str) -> None:
        ...
    def Save(self) -> None:
        ...
    def SaveAs(self, postprocessorName: str, outputDirectory: str) -> None:
        ...
    def CreateCustomCdlFile(self) -> None:
        ...
    def PostProcess(self, objects: typing.List[CAM.CAMObject], outputFilename: str, showOutputToListingWindow: bool) -> None:
        ...
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: str) -> None:
        ...
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: str) -> None:
        ...
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: int) -> None:
        ...
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: float) -> None:
        ...
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, firstValue: float, secondValue: float, thirdValue: float) -> None:
        ...
    def SetPropertyToDefaultValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        ...
    def AddProperty(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        ...
    def RemoveProperty(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        ...
    def GetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        ...
    def GetPropertyDefaultValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        ...
    def GetPropertyOptionsValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        ...
    def GetPropertyOptionsIdValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        ...
    def GetPropertyDescriptionText(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        ...
    def GetPropertyDescriptionImage(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        ...
    def GetPropertyDataType(self, chainID: str, configurationObjectID: str, propertyID: str) -> SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataType:
        ...
    def GetPropertyDataFieldType(self, chainID: str, configurationObjectID: str, propertyID: str) -> SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataFieldType:
        ...
    def GetPropertyOptionType(self, chainID: str, configurationObjectID: str, propertyID: str) -> SIM.PostConfigurator.PostConfiguratorBuilder.PropertyOptionType:
        ...
    def GetPropertyAccessType(self, chainID: str, configurationObjectID: str, propertyID: str) -> SIM.PostConfigurator.PostConfiguratorBuilder.PropertyAccessType:
        ...
    def GetPropertyValueChangedStatus(self, chainID: str, configurationObjectID: str, propertyID: str) -> SIM.PostConfigurator.PostConfiguratorBuilder.PropertyValueChangedStatusType:
        ...
    def GetPropertyChainIds(self) -> str:
        ...
    def GetPropertyConfigurationObjectIds(self) -> str:
        ...
    def GetPropertyIds(self) -> str:
        ...
    def OpenDocumentation(self) -> None:
        ...
    def ListPropertyDataInInformationWindow(self, configurationObjectID: str, propertyID: str) -> None:
        ...
    def CopyPropertyDataToClipboard(self, configurationObjectID: str, propertyID: str) -> None:
        ...
    def CreateCustomDefFile(self) -> SIM.PostConfigurator.PostConfiguratorBuilder.DefWriterErrorType:
        ...
    DateValue: DateBuilder
    DefEditorBuilder: SIM.PostConfigurator.DefEditorBuilder
    LayerManagerBuilder: SIM.PostConfigurator.LayerManagerBuilder
    UdeEditorBuilder: SIM.PostConfigurator.UdeEditorBuilder
    Units: SIM.PostConfigurator.PostConfiguratorBuilder.UnitsType
    UpdatePostprocessorBuilder: SIM.PostConfigurator.UpdatePostprocessorBuilder


    class UnitsType(enum.Enum):
        Millimeters = 0
        Inches = 1
        MillimetersAndInches = 2
    

    class PropertyValueChangedStatusType(enum.Enum):
        Unchanged = 0
        Changed = 1
        UnremoveUnchanged = 2
        UnremoveChanged = 3
        UnaddUnchanged = 4
        UnaddChanged = 5
    

    class PropertyOptionType(enum.Enum):
        Unknown = 0
        Value = 1
        Enum = 2
    

    class PropertyDataType(enum.Enum):
        Unknown = 0
        Integer = 1
        Double = 2
        String = 3
        Option = 4
        Vector = 5
        Multistring = 6
        Point = 7
    

    class PropertyDataFieldType(enum.Enum):
        Unknown = 0
        Single = 1
        Option = 2
    

    class PropertyAccessType(enum.Enum):
        No = 0
        Read = 1
        Full = 2
    

    class DefWriterErrorType(enum.Enum):
        NoError = 0
        DirWriteprotectError = 1
        NoCustomerError = 2
        CustomFileExistError = 3
        FileWriteprotectError = 4
        UnknownError = 5
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class LayerManagerBuilder(Builder):
    def __init__(self) -> None: ...
    AddLayerBuilder: SIM.PostConfigurator.AddLayerBuilder


class EncryptPostprocessorFilesBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEncryptPostprocessorFiles(self, encryptFilename: str) -> None:
        ...
    def GetEncryptPostprocessorFiles(self) -> str:
        ...
    def SetSoldToIds(self, soldToIDs: str) -> None:
        ...
    def GetSoldToIds(self) -> str:
        ...
    ExpirationDate: str


class DefEditorBuilder(Builder):
    def __init__(self) -> None: ...
    def AddBlockTemplate(self, blockTemplateName: str, blockAddressName: str, blockItemType: typing.List[SIM.PostConfigurator.DefEditorBuilder.BlockItemType], expression: str, addressIndex: int, isOptional: bool, hasNoWordSeparator: bool) -> None:
        ...
    def DeleteBlockTemplate(self, blockTemplateName: str) -> None:
        ...
    def AddAddress(self, addressName: str, formatName: str, zeroLimitName: str, forceType: SIM.PostConfigurator.DefEditorBuilder.AddressForceType, leader: str, leaderType: SIM.PostConfigurator.DefEditorBuilder.AddressLeaderType, trailer: str, trailerType: SIM.PostConfigurator.DefEditorBuilder.AddressTrailerType, maxIsDefine: bool, maxLimit: float, maxHandeType: SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType, minIsDefine: bool, minLimit: float, minHandeType: SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType) -> None:
        ...
    def AddAddressWithOmit(self, addressName: str, formatName: str, zeroLimitName: str, forceType: SIM.PostConfigurator.DefEditorBuilder.AddressForceType, leader: str, leaderType: SIM.PostConfigurator.DefEditorBuilder.AddressLeaderType, trailer: str, trailerType: SIM.PostConfigurator.DefEditorBuilder.AddressTrailerType, maxIsDefine: bool, maxLimit: float, maxHandeType: SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType, minIsDefine: bool, minLimit: float, minHandeType: SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType, omit: str) -> None:
        ...
    def DeleteAddress(self, addressName: str) -> None:
        ...
    def DeleteBlockAddress(self, blockTemplateName: str, addressName: str) -> None:
        ...
    def AddBlockAddress(self, blockTemplateName: str, blockAddressName: str, blockItemType: int, expression: str, addressIndex: int, isOptional: bool, hasNoWordSeparator: bool) -> None:
        ...
    def AddFormat(self, formatName: str, isOutputLeaderPlusSign: bool, isOutputLeadingZeros: bool, isOutputDecimalPoint: bool, isOutputTrailingZeros: bool, visibleDigits: int, visibleDecimals: int, formatType: SIM.PostConfigurator.DefEditorBuilder.FormatType) -> None:
        ...
    def DeleteFormat(self, formatName: str) -> None:
        ...
    CurrentLayer: str


    class FormatType(enum.Enum):
        Numeric = 0
        Text = 1
    

    class BlockItemType(enum.Enum):
        Literal = 0
        Address = 1
        TurboAddress = 2
    

    class AddressTrailerType(enum.Enum):
        Literal = 0
        Expression = 1
    

    class AddressLimitHandleType(enum.Enum):
        TruncateValue = 0
        WarnUser = 1
        AbortProcess = 2
    

    class AddressLeaderType(enum.Enum):
        Literal = 0
        Expression = 1
    

    class AddressForceType(enum.Enum):
        On = 0
        Once = 1
        Always = 2
    

class CreationPostBuilder(Builder):
    def __init__(self) -> None: ...
    def GetControllerNames(self) -> str:
        ...
    def GetManufacturerNames(self) -> str:
        ...
    def GetMachineNames(self) -> str:
        ...
    def GetLayerNameValue(self, layerName: str) -> str:
        ...
    def SetLayerNameValue(self, layerName: str, value: str) -> None:
        ...
    def GetLayerNames(self, layerName: str) -> str:
        ...
    ControllerName: str
    CreateDirectoryForPostprocessor: bool
    MachineName: str
    ManufacturerName: str
    PostprocessorName: str
    PostprocessorOutputDirectory: str


class AddLayerBuilder(Builder):
    def __init__(self) -> None: ...
    CreateDefinitionFile: bool
    CreateDirectoryForLayer: bool
    CreateTclFile: bool
    CreateUserDefinedEventFile: bool
    LayerFileName: str
    LayerName: str


