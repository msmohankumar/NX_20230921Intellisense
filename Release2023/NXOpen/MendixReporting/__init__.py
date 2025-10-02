from ...NXOpen import *
from ..MendixReporting import *

import typing
import enum

class CheckerDataStatus(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetAvailableCheckerStatus(self) -> str:
        ...
    def Tag(self) -> Tag: ...



class CheckerData(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def GetCheckerData(self) -> str:
        ...
    def GetSummaryOfFeatures(self) -> str:
        ...
    def Tag(self) -> Tag: ...



class CadInfoManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def GetCreationDate(self) -> str:
        ...
    def GetCreatedBy(self) -> str:
        ...
    def GetLastModificationDate(self) -> str:
        ...
    def GetLastModifiedBy(self) -> str:
        ...
    def GetPartType(self) -> str:
        ...
    def GetCvfForPart(self, bGenerateCvfFiles: bool, psCvfStream: str, geometryCvfStream: str) -> None:
        ...
    def GetPersistentIdForPart(self, componentTag: TaggedObject) -> str:
        ...
    def GetPLLinkForPart(self) -> str:
        ...
    def GetPartInformation(self) -> MendixReporting.CadInfoManager.PartInformation:
        ...
    def Tag(self) -> Tag: ...



    class CadInfoManagerPartInformation():
        PartHasUdf: bool
        PartHasPosIndepWaveLink: bool
        PartHasPosDepWaveLink: bool
        PartHasInterpartExpression: bool
        PartHasInterpartReferences: bool
        PartHasProductInterface: bool
        PartHasBrokenLinks: bool
        PartHasAnyComponents: bool
        PartHasGeometryOverrides: bool
        PartHasPositionOverrides: bool
        PartHasReferenceComponents: bool
        PartHasSupressedComponents: bool
        PartHasRestructuredComponents: bool
        PartHasNonmasterComponent: bool
        PartHasMultipleArrangements: bool
        PartHasAltrepMetaData: bool
        PartHasOffcenterComponents: bool
        PartHasPartsList: bool
        PartHasConstraint: bool
        PartIsDrawing: bool
        PartHasCaeData: bool
        PartHasCamData: bool
        PartIsPartFamilyMember: bool
        PartIsPartFamilyTemplate: bool
        PartIsPart: bool
        PartHasMeasurableAttribute: bool
        PartHasBody: bool
        PartHasSuppressionOverride: bool
        PartHasVisStructureStream: bool
        PartHasVisRmStream: bool
        PartPartUnits: bool
        PartHasSheetMetalData: bool
        PartIsRoutingPart: bool
        PartIsRouteSystemAssembly: bool
        def ToString(self) -> str:
            ...
    

