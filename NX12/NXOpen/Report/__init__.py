from ...NXOpen import *
from ..Report import *

import typing
import enum

class UserTextItem(Report.TextItem):
    def __init__(self) -> None: ...
    def SetDisplayName(self, displayName: str) -> None:
        ...


class UserInput(TaggedObject):
    def __init__(self) -> None: ...
    def GetHint(self, inputHint: str) -> None:
        ...
    def SetHint(self, inputHint: str) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    InputType: Report.UserInput.Type
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


    class Type(enum.Enum):
        Text = 0
        Images = 1
    

class UserImagesGroupItem(Report.ImagesGroupItem):
    def __init__(self) -> None: ...
    def SetDisplayName(self, displayName: str) -> None:
        ...


class TextItem(Report.BaseItem):
    def __init__(self) -> None: ...
    def GetText(self, lineTexts: str) -> None:
        ...
    def SetText(self, lineTexts: str) -> None:
        ...


class TemplateItem(Report.BaseItem):
    def __init__(self) -> None: ...
    def GetChildItems(self, itemsLocation: Report.CommandBuilder.UserInputLocation, pItems: typing.List[Report.BaseItem]) -> None:
        ...


class StringArgument(Report.BaseArgument):
    def __init__(self) -> None: ...
    DefaultValue: str


class ResultXmlFileWriter(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddText(self, textContent: str) -> OpenXml.TextDocumentData:
        ...
    def AddImageGroup(self) -> OpenXml.ImageGroupDocumentData:
        ...
    def AddTable(self, columnSize: int, rowSize: int) -> OpenXml.TableDocumentData:
        ...
    def GetDataCount(self) -> int:
        ...
    def GetNthData(self, index: int) -> OpenXml.DocumentData:
        ...
    def DeleteNthData(self, index: int) -> None:
        ...
    def DeleteAllData(self) -> None:
        ...
    def SaveToFile(self, fileName: str) -> None:
        ...


class ReportPreference(TaggedObject):
    def __init__(self) -> None: ...
    def SaveMemoryFile(self) -> None:
        ...
    MaximumRecentReportDocumentCount: int
    OpenReportDocumentAfterExport: bool
    SearchTemplateFromSiteDirectory: bool
    UsePartDirectoryAsDefaultExportLocation: bool
    ViewImageAfterSnapshotting: bool


class ReportManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateResultXmlFileWriter(self) -> Report.ResultXmlFileWriter:
        ...
    def GetOriginalImageDimension(self, imageFullFileName: str, width: float, height: float) -> None:
        ...
    def Tag(self) -> Tag: ...

    AutomationLogger: Report.AutomationLogger
    CommandManager: Report.CommandManager
    Preference: Report.ReportPreference


class ReportImage(NXObject):
    def __init__(self) -> None: ...
    def SetImage(self, imageFile: str) -> None:
        ...
    Caption: str
    ImageOption: Report.ImageOption


class Report(NXObject):
    def __init__(self) -> None: ...
    def GetTemplateItems(self, pTemplateItems: typing.List[Report.TemplateItem]) -> None:
        ...
    def CreateUserItem(self, inputType: Report.UserInput.Type) -> Report.IUserItem:
        ...
    def CopyUserItem(self, userItem: Report.IUserItem) -> Report.IUserItem:
        ...
    def GetUserItems(self, userItems: typing.List[Report.IUserItem]) -> None:
        ...
    def MoveUserItems(self, userItems: typing.List[Report.IUserItem], newLocation: Report.Report.MoveItemLocation, referencedItem: Report.IUserItem) -> None:
        ...
    def Export(self, reportDocument: str, listError: bool) -> None:
        ...
    def ClearTemplateItems(self) -> None:
        ...
    def DeleteUserItems(self) -> None:
        ...
    def HideTempalteItemsWithoutInput(self, hideTemplateItemsWithoutInput: bool) -> None:
        ...
    def SynchronizeWithCommands(self) -> None:
        ...
    ReportCollection: Report.IReportCollection
    TemplateFile: str


    class MoveItemLocation(enum.Enum):
        Before = 0
        After = 1
    

class ProgramInformation(TaggedObject):
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    FunctionName: str
    Language: Report.ProgramInformation.LanguageType
    ProgramFile: str
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


    class LanguageType(enum.Enum):
        None = 0
        CPlusplus = 1
        CSharp = 2
        Vb = 3
        Java = 4
        Python = 5
    

class IUserItem():
    def SetDisplayName(self, displayName: str) -> None:
        ...


class IReportCollection():
    def CreateReport(self, templateFile: str, reportName: str, listError: bool) -> Report.Report:
        ...
    def GetReports(self, pReports: typing.List[Report.Report]) -> None:
        ...


class IntegerArgument(Report.BaseArgument):
    def __init__(self) -> None: ...
    DefaultValue: int
    IncludeLowerBound: bool
    IncludeUpperBound: bool
    MaximumValue: int
    MinimumValue: int


class ImagesGroupItem(NXObject):
    def __init__(self) -> None: ...
    def CreateImage(self, imageFile: str, displayName: str) -> Report.ReportImage:
        ...
    def CopyImage(self, pReportImage: Report.ReportImage) -> Report.ReportImage:
        ...
    def GetImages(self, pReportImages: typing.List[Report.ReportImage]) -> None:
        ...
    def MoveImages(self, pReportImages: typing.List[Report.ReportImage], newLocation: Report.Report.MoveItemLocation, pReferencedImage: Report.ReportImage) -> None:
        ...
    def DeleteImages(self) -> None:
        ...


class ImageOption(TaggedObject):
    def __init__(self) -> None: ...
    ImageHeight: float
    ImageRotation: float
    ImageWidth: float
    LockOriginalAspectRatio: bool


class EnumerationArgument(Report.BaseArgument):
    def __init__(self) -> None: ...
    def GetEnumerationOptions(self, enumerationOptions: str) -> None:
        ...
    def SetEnumerationOptions(self, enumerationOptions: str) -> None:
        ...
    DefaultValue: int


class DoubleArgument(Report.BaseArgument):
    def __init__(self) -> None: ...
    DefaultValue: float
    IncludeLowerBound: bool
    IncludeUpperBound: bool
    MaximumValue: float
    MimimumValue: float


class CommandManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Report.ReportManager) -> None: ...
    def ExportCommandsToLibraryFile(self, pCommands: typing.List[Report.Command], libraryFile: str) -> None:
        ...
    def GetCommandLibraries(self, pCommandLibraries: typing.List[Report.CommandLibrary]) -> None:
        ...
    def CreateCommandBuilder(self, commandLibrary: Report.CommandLibrary, command: Report.Command) -> Report.CommandBuilder:
        ...
    def NewCommandImporter(self, pCommandLibrary: Report.CommandLibrary, libraryFile: str) -> Report.CommandImporter:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def Tag(self) -> Tag: ...



class CommandLibrary(TaggedObject):
    def __init__(self) -> None: ...
    def GetCommands(self, pCommands: typing.List[Report.Command]) -> None:
        ...
    def Save(self) -> None:
        ...
    def MoveCommands(self, pCommand: typing.List[Report.Command], newLocation: Report.CommandLibrary.MoveCommandLocation, pReferenceCommand: Report.Command) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


    class MoveCommandLocation(enum.Enum):
        Before = 0
        After = 1
    

class CommandImporter(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetImportCandidates(self, pCommands: typing.List[Report.Command]) -> None:
        ...
    def ImportCommands(self, pCommandIndexes: int) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    ImportOption: Report.CommandImporter.OverrideOption


    class OverrideOption(enum.Enum):
        Ignore = 0
        Replace = 1
        Copy = 2
    

class CommandBuilder(Builder):
    def __init__(self) -> None: ...
    def GetHint(self, commandHint: str) -> None:
        ...
    def SetHint(self, commandHint: str) -> None:
        ...
    def SetNamespaces(self, pNamespaces: str) -> None:
        ...
    def GetNamespaces(self, pNamespaces: str) -> None:
        ...
    def AddArgument(self, argumentType: Report.BaseArgument.Type) -> Report.BaseArgument:
        ...
    def GetArguments(self, pArguments: typing.List[Report.BaseArgument]) -> None:
        ...
    def RemoveArguments(self, pArguments: typing.List[Report.BaseArgument]) -> None:
        ...
    def AddUserInput(self, userInputLocation: Report.CommandBuilder.UserInputLocation, userInputType: Report.UserInput.Type) -> Report.UserInput:
        ...
    def GetUserInputs(self, userInputLocation: Report.CommandBuilder.UserInputLocation, pUserInputs: typing.List[Report.UserInput]) -> None:
        ...
    def RemoveUserInputs(self, userInputLocation: Report.CommandBuilder.UserInputLocation, pUserInputs: typing.List[Report.UserInput]) -> None:
        ...
    def MoveUserInputs(self, userInputLocation: Report.CommandBuilder.UserInputLocation, pUserInputs: typing.List[Report.UserInput], isBeforeRefUserInput: bool, pRefUserInputs: Report.UserInput) -> None:
        ...
    Active: bool
    DisplayName: str
    Name: str
    ProgramInformation: Report.ProgramInformation


    class UserInputLocation(enum.Enum):
        BeforeAutomation = 0
        AfterAutomation = 1
    

class Command(NXObject):
    def __init__(self) -> None: ...
    def Delete(self) -> None:
        ...


class BaseItem(NXObject):
    def __init__(self) -> None: ...
    def Clear(self) -> None:
        ...
    DisplayName: str
    Hint: str


class BaseArgument(TaggedObject):
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    DisplayName: str
    Hint: str
    Optional: bool
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


    class Type(enum.Enum):
        Integer = 0
        Double = 1
        String = 2
        Enumeration = 3
    

class AutomationLogger(Utilities.NXRemotableObject):
    def __init__(self, owner: Report.ReportManager) -> None: ...
    def LogMessage(self, message: str) -> None:
        ...
    def LogMessage(self, message: str, messageType: Report.AutomationLogger.MessageType) -> None:
        ...
    def Clear(self) -> None:
        ...
    def SaveLog(self, logFileName: str) -> None:
        ...
    def IsEmpty(self) -> bool:
        ...
    def Tag(self) -> Tag: ...



    class MessageType(enum.Enum):
        Empty = 0
        Information = 1
        Debug = 2
        Exception = 3
    

