from ...NXOpen import *
from ..CloudDM import *

import typing
import enum

class PartUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: CloudDM.DataManager) -> None: ...
    def GetDocumentIdentifier(self, inputPart: Part) -> CloudDM.DocumentIdentifier:
        ...
    def SaveAs(self, inputPart: Part, newFileName: str, newDesignInfo: CloudDM.NewPartBuilder) -> PartSaveStatus:
        ...
    def CheckoutParts(self, partsToCheckOut: typing.List[Part]) -> None:
        ...
    def CheckinParts(self, partsToCheckIn: typing.List[Part]) -> None:
        ...
    def FreezeParts(self, partsToFreeze: typing.List[Part]) -> None:
        ...
    def GetRelatedDrawings(self, inputPart: Part) -> typing.List[CloudDM.DocumentIdentifier]:
        ...
    def Tag(self) -> Tag: ...



class PartOperationObject(NXObject):
    def __init__(self) -> None: ...


class PartOperationBuilder(Builder):
    def __init__(self) -> None: ...
    def SetOperationType(self, optype: CloudDM.PartOperationBuilder.OperationType) -> None:
        ...
    def GetOperationType(self) -> CloudDM.PartOperationBuilder.OperationType:
        ...
    def SetSourceParts(self, sourceParts: typing.List[BasePart]) -> None:
        ...
    def CreatePartOperationObjects(self, partOperationObjects: typing.List[CloudDM.PartOperationObject], errorMsgs: str, status: int) -> None:
        ...
    def ValidatePartOperationObjects(self) -> None:
        ...
    def SetTargetPath(self, targetPath: str) -> None:
        ...
    def GetOperationFailures(self) -> ErrorList:
        ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...


    class OperationType(enum.Enum):
        CreateSpecification = 0
        NamePart = 1
        MakeUnique = 2
        Revise = 3
        SaveAs = 4
        Mirror = 5
        Max = 6
    

class NewPartBuilder(Builder):
    def __init__(self) -> None: ...
    def AutoAssignDesignNumber(self) -> None:
        ...
    def SynchronizeAttributes(self) -> None:
        ...
    def SetTemplatePartContext(self, templatePartContext: CloudDM.NewPartBuilder.TemplatePartContextinfo) -> None:
        ...
    AttributeHolder: NXObject
    DesignDescription: str
    DesignName: str
    DesignNumber: str
    DesignRevision: str
    Folder: str
    Project: str
    TemplatePart: str


    class NewPartBuilderTemplatePartContextinfo():
        CollaborationSpaceId: str
        ContainerId: str
        ContainerType: str
        def ToString(self) -> str:
            ...
        def __init__(self, CollaborationSpaceId: str, ContainerId: str, ContainerType: str) -> None: ...
    

    class NewPartBuilder_TemplatePartContextinfo():
        collaborationSpaceId: int
        containerId: int
        containerType: int
    

class NewPartAttributeHolder(NXObject):
    def __init__(self) -> None: ...


class FileManagement(Utilities.NXRemotableObject):
    def __init__(self, owner: CloudDM.DataManager) -> None: ...
    def GetAssociatedDocumentList(self, inputPart: BasePart) -> typing.List[CloudDM.DocumentIdentifier]:
        ...
    def DownloadAssociatedDocuments(self, inputPart: BasePart, documents: typing.List[CloudDM.DocumentIdentifier]) -> None:
        ...
    def GetAssociatedFileListForUpload(self, inputPart: BasePart) -> typing.List[CloudDM.FileManagement.FileInfo]:
        ...
    def UploadAssociatedDocuments(self, inputPart: BasePart, fileList: typing.List[CloudDM.FileManagement.FileInfo]) -> None:
        ...
    def Tag(self) -> Tag: ...



    class FileManagementFileInfo():
        FilePath: str
        FileType: str
        IsText: bool
        def ToString(self) -> str:
            ...
        def __init__(self, FilePath: str, FileType: str, IsText: bool) -> None: ...
    

    class FileManagement_FileInfo():
        filePath: int
        fileType: int
        isText: bool
    

class DocumentIdentifier(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DateModified: str
    DocumentUrn: str
    LockInfo: CloudDM.DocumentIdentifier.LockInformation
    Name: str
    Owner: str
    RevisionUrn: str


    class DocumentIdentifierLockInformation():
        LockedAt: str
        LockExpires: str
        LockedBy: str
        def ToString(self) -> str:
            ...
        def __init__(self, LockedAt: str, LockExpires: str, LockedBy: str) -> None: ...
    

    class DocumentIdentifier_LockInformation():
        lockedAt: int
        lockExpires: int
        lockedBy: int
    

class DataManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetDataManager(self, owner: Session) -> CloudDM.DataManager:
        ...
    def GetCheckedoutStatusOfAllObjectsInSession(self, checkedOutObjects: typing.List[NXObject], uncheckedOutObjects: typing.List[NXObject]) -> None:
        ...
    def CreatePartOperationBuilder(self, operation: CloudDM.PartOperationBuilder.OperationType) -> CloudDM.PartOperationBuilder:
        ...
    def Tag(self) -> Tag: ...

    FileManagement: CloudDM.FileManagement
    PartUtils: CloudDM.PartUtils


    class DataManagerImportPartInput():
        LocalFileName: str
        RelativeFilePath: str
        def ToString(self) -> str:
            ...
        def __init__(self, LocalFileName: str, RelativeFilePath: str) -> None: ...
    

    class DataManagerImportPartDesign():
        InputPart: str
        RevisionUrn: str
        DownloadTicket: str
        def ToString(self) -> str:
            ...
        def __init__(self, InputPart: str, RevisionUrn: str, DownloadTicket: str) -> None: ...
    

    class DataManagerContainerInfo():
        Name: str
        Description: str
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, Description: str) -> None: ...
    

    class DataManager_ImportPartInput():
        localFileName: int
        relativeFilePath: int
    

    class DataManager_ImportPartDesign():
        inputPart: int
        revisionUrn: int
        downloadTicket: int
    

    class DataManager_ContainerInfo():
        name: int
        description: int
    

