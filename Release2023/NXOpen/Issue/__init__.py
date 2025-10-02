from ...NXOpen import *
from ..Issue import *

import typing
import enum

class SnapshotWorksetBuilder(Builder):
    def __init__(self) -> None: ...
    ImpactedSubset: Issue.SnapshotSubsetBuilder
    ProblemSubset: Issue.SnapshotSubsetBuilder
    ReferenceSubset: Issue.SnapshotSubsetBuilder


class SnapshotSubsetBuilder(Builder):
    def __init__(self) -> None: ...
    Context: Issue.SnapshotSubsetBuilder.ContextType
    SelectParts: Assemblies.SelectComponentList


    class ContextType(enum.Enum):
        Problem = 0
        Impacted = 1
        Reference = 2
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class IssueSite(NXObject):
    def __init__(self) -> None: ...
    def IsConnected(self) -> bool:
        ...
    def RemoveList(self, list: Issue.IssueList) -> None:
        ...
    def CreateList(self, listName: str, queryName: str, criteriaTitles: str, criteriaValues: str) -> Issue.IssueList:
        ...
    def GetQuickSearchList(self) -> Issue.IssueList:
        ...


class IssueProperty(NXObject):
    def __init__(self) -> None: ...
    def GetChoices(self) -> str:
        ...
    def GetDefaultChoice(self) -> str:
        ...
    IsReadOnly: bool
    StringValue: str
    ValueType: Issue.IssueProperty.Type


    class Type(enum.Enum):
        Text = 0
        Note = 1
        User = 2
        Choice = 3
        Url = 4
        Boolean = 5
        Date = 6
        Number = 7
        Integer = 8
        Point3D = 9
        Vector3D = 10
    

class IssueManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateIssueContent(self, list: Issue.IssueList) -> Issue.IssueContent:
        ...
    def CreateIssueAttachment(self, fileSpec: str, name: str, type: Issue.IssueAttachment.Type) -> Issue.IssueAttachment:
        ...
    def CreateIssueContentBuilder(self, issue: Issue.IssueContent) -> Issue.IssueContentBuilder:
        ...
    def Connect(self, siteUrl: str, userName: str, password: str) -> Issue.IssueSite:
        """[Obsolete("Deprecated in NX12.0.2.  This functionality is no longer supported.")"""
        ...
    def Disconnect(self) -> None:
        """[Obsolete("Deprecated in NX12.0.2.  This functionality is no longer supported.")"""
        ...
    def GetWorkingList(self) -> Issue.IssueList:
        ...
    def SetWorkingList(self, list: Issue.IssueList) -> None:
        ...
    def GetIssueState(self, issue: Issue.IssueContent) -> Issue.IssueManager.State:
        ...
    def GetAttachmentState(self, attachment: Issue.IssueAttachment) -> Issue.IssueManager.State:
        ...
    def GetPropertyState(self, property: Issue.IssueProperty) -> Issue.IssueManager.State:
        ...
    def CreateIssueSnapshotSubsetBuilder(self, subsetPart: Part) -> Issue.SnapshotSubsetBuilder:
        ...
    def CreateIssueSnapshotWorksetBuilder(self, issue: Issue.IssueContent) -> Issue.SnapshotWorksetBuilder:
        ...
    def CreateAttachmentForSnapshot(self, bookmarkFileSpec: str, imageFileSpec: str, name: str) -> Issue.IssueAttachment:
        ...
    def CreateAttachmentForScreenImage(self) -> Issue.IssueAttachment:
        ...
    def CreateAttachmentForBookMark(self) -> Issue.IssueAttachment:
        ...
    def CaptureAndCreateAttachmentForSnapshot(self) -> Issue.IssueAttachment:
        ...
    def CreateBriefcase(self, briefcaseName: str, filePath: str) -> Issue.IssueBriefcase:
        ...
    def OpenBriefcase(self, filePath: str) -> Issue.IssueBriefcase:
        ...
    def Tag(self) -> Tag: ...

    IssueListCollection: Issue.IssueListCollection
    CurrentMode: Issue.IssueManager.Mode
    CurrentSite: Issue.IssueSite


    class State(enum.Enum):
        Original = 0
        Created = 1
        Modified = 2
        Removed = 3
    

    class Mode(enum.Enum):
        TeamcenterCommunity = 0
        Teamcenter = 1
        Briefcase = 2
    

class IssueListCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Issue.IssueList]:
        ...
    def __init__(self, owner: Issue.IssueManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Issue.IssueList:
        ...
    def Tag(self) -> Tag: ...



class IssueList(NXObject):
    def __init__(self) -> None: ...
    def ReloadIssues(self) -> None:
        ...
    def GetIssues(self) -> typing.List[Issue.IssueContent]:
        ...
    def ExistsInDatabase(self) -> bool:
        ...
    def SaveChanges(self) -> None:
        ...
    def DiscardChanges(self) -> None:
        ...
    def SaveConfig(self) -> None:
        ...
    def ResetConfig(self) -> None:
        ...
    def ChangeConfig(self, queryName: str, criteriaTitles: str, criteriaValues: str) -> None:
        ...
    def SetRelatedParts(self, parts: typing.List[NXObject]) -> None:
        ...


class IssueFolder(NXObject):
    def __init__(self) -> None: ...
    def GetAttachments(self) -> typing.List[Issue.IssueAttachment]:
        ...
    def AddAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...
    def RemoveAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...
    FolderType: Issue.IssueFolder.Type


    class Type(enum.Enum):
        ProblemItems = 0
        ImpactedItems = 1
        ReferenceItems = 2
        ImplementedBy = 3
        IssueImage = 4
        IssueFixedImage = 5
        SnapshotBeforeFix = 6
        SnapshotAfterFix = 7
        ValidationResults = 8
    

class IssueContentBuilder(Builder):
    def __init__(self) -> None: ...
    def GetEditableUserProperties(self) -> typing.List[Issue.IssueProperty]:
        ...
    def SetPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    def GetPropertyValue(self, propertyName: str) -> str:
        ...
    def GetAllAttachments(self) -> typing.List[Issue.IssueAttachment]:
        ...
    def GetAttachment(self, attachmentName: str) -> Issue.IssueAttachment:
        ...
    def AddAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...
    def RemoveAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...
    def SetPreviewImage(self, attachment: Issue.IssueAttachment) -> None:
        ...
    AssignedUser: str
    Comment: str
    DueDate: str
    Priority: str
    Status: str
    Title: str


class IssueContent(NXObject):
    def __init__(self) -> None: ...
    def GetUserProperties(self) -> typing.List[Issue.IssueProperty]:
        ...
    def GetProperty(self, propertyName: str) -> Issue.IssueProperty:
        ...
    def ReloadProperties(self) -> None:
        ...
    def SetPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    def GetPropertyValue(self, propertyName: str) -> str:
        ...
    def GetAllAttachments(self) -> typing.List[Issue.IssueAttachment]:
        ...
    def GetChildAttachments(self) -> typing.List[Issue.IssueAttachment]:
        ...
    def GetAttachment(self, attachmentName: str) -> Issue.IssueAttachment:
        ...
    def GetPartAttachment(self) -> Issue.IssueAttachment:
        ...
    def LoadAttachments(self) -> None:
        ...
    def AddAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...
    def RemoveAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...
    def GetFolders(self) -> typing.List[Issue.IssueFolder]:
        ...
    def SaveChanges(self) -> None:
        ...
    def DiscardIssue(self) -> None:
        ...
    def IsCheckedOut(self, user: str) -> bool:
        ...
    def Close(self, coseNote: str) -> None:
        ...
    def IsClosed(self) -> bool:
        ...
    def IsReadOnly(self) -> bool:
        ...
    def SendToWorkflow(self, workflowTemplate: str) -> None:
        ...
    def Review(self, reviewDecision: str, comment: str) -> None:
        ...
    AssignedUser: str
    Comment: str
    DueDate: str
    IsLocked: bool
    IssueId: str
    PreviewImage: Issue.IssueAttachment
    Priority: str
    Status: str
    Title: str


class IssueBriefcaseSynchronizeBuilder(Builder):
    def __init__(self) -> None: ...
    def AddPartAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...
    def RemovePartAttachment(self, attachment: Issue.IssueAttachment) -> None:
        ...


class IssueBriefcase(Issue.IssueList):
    def __init__(self) -> None: ...
    def AddIssue(self, issue: Issue.IssueContent) -> None:
        ...
    def RemoveIssue(self, issue: Issue.IssueContent) -> None:
        ...
    def Save(self) -> None:
        ...
    def Close(self) -> None:
        ...
    def CreateSynchronizeContentBuilder(self) -> Issue.IssueBriefcaseSynchronizeBuilder:
        ...
    Location: str


class IssueAttachment(NXObject):
    def __init__(self) -> None: ...
    def RecaptureSnapshot(self, bookmarkFileSpec: str, imageFileSpec: str) -> None:
        ...
    AttachmentType: Issue.IssueAttachment.Type
    ReferencedAttachmentId: str


    class Type(enum.Enum):
        Generic = 0
        Text = 1
        Part = 2
        Xml = 3
        Image = 4
        ValidationLog = 5
        Bookmark = 6
        Snapshot = 7
        ValidationResult = 8
        Workset = 9
        ShapeDesignElement = 10
        ReuseDesignElement = 11
        SubordinateDesignElement = 12
        PromissoryDesignElement = 13
        DesignControlElement = 14
        Subset = 15
        MSWord = 16
        MSExcel = 17
        MSPowerPoint = 18
        VisualizationSession = 19
    

