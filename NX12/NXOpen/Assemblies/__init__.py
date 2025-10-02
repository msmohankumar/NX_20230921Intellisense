from . import ProductInterface
from ...NXOpen import *
from ..Assemblies import *

import typing
import enum

class WaveQuery(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetPartPreview(self, partSpec: str, partIdentifier: int, height: int, width: int, pixels: int) -> None:
        ...
    def GetInSessionPartsXml(self, includeOnlyWithLinks: bool) -> str:
        ...
    def GetPartsInContextAssemblyXml(self, includeOnlyWithLinks: bool) -> str:
        ...
    def GetAllSelectedPartsXml(self, includeOnlyWithLinks: bool) -> str:
        ...
    def GetWorkPartWithPartRelationsXml(self) -> str:
        ...
    def GetChildPartRelationsXml(self, parentPartSpec: str, parentPartIdentifier: int, walkAll: bool) -> str:
        ...
    def GetParentPartRelationsXml(self, childPartSpec: str, childPartIdentifier: int, walkAll: bool) -> str:
        ...
    def GetProductInterfacesXml(self, partSpec: str, partIdentifier: int) -> str:
        ...
    def GetInterPartLinksXml(self, partSpec: str, partIdentifier: int) -> str:
        ...
    def GetReferencesToProductInterfaceXml(self, owningPartSpec: str, owningPartIdentifier: int, prodintHandle: str, prodintIdentifier: int) -> str:
        ...
    def HandleApplicationEvents(self, eventType: Assemblies.AssembliesEventTypes, eventDescription: str, entitySpecs: str, entityIdentifiers: int) -> int:
        ...
    def GetPartFeatureDependenciesXml(self, partSpec: str, partIdentifier: int) -> str:
        ...
    def AreAssemblyConstraintsDelayed(self) -> bool:
        ...
    def GetSpecifiedPartRelationsXml(self, partSpecs: str, partIdentifiers: int, includeOnlyWithLinks: bool) -> str:
        ...
    def GetSpecifiedPartRelationsXml(self, partSpecs: str, partIdentifiers: int, includeOnlyWithLinks: bool, forceQuery: bool) -> str:
        ...
    def SetChildRevisionOption(self, optionType: Assemblies.AssembliesChildRevisionOptions) -> None:
        ...
    def GetChildRevisionOption(self) -> Assemblies.AssembliesChildRevisionOptions:
        ...
    def SetQueryProductInterfaces(self, queryProductInterfaces: bool) -> None:
        ...
    def GetQueryProductInterfaces(self) -> bool:
        ...
    def SetIncludeTeamcenterRelations(self, includeTeamcenterRelations: bool) -> None:
        ...
    def GetIncludeTeamcenterRelations(self) -> bool:
        ...


class UpdateStructureBuilder(Builder):
    def __init__(self) -> None: ...
    IsUpdateAllLevels: bool
    NumberOfLevels: int
    StructureToUpdate: SelectDisplayableObjectList


class UpdateDesignElementPositionBuilder(Builder):
    def __init__(self) -> None: ...
    DesignElementsToUpdatePosition: SelectDisplayableObjectList


class SubsetRecipe(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.SearchTerm]:
        ...
    def __init__(self, owner: Assemblies.SubsetBuilder) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Assemblies.SearchTerm:
        ...
    def CreateExplicitSearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, searchResultElement: Assemblies.SearchResultElement) -> Assemblies.ExplicitSearchTerm:
        ...
    def CreateExplicitSearchTermGroup(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, searchResultElements: typing.List[Assemblies.SearchResultElement]) -> Assemblies.GroupSearchTerm:
        ...
    def AddSearchTermBuilder(self, searchTermBuilder: Assemblies.SearchTermBuilder) -> None:
        ...
    def CreateBoxSearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, overlapType: Assemblies.BoxSearchTerm.BoxOverlapLogicType, bottomCorner: Point3d, topCorner: Point3d, trueShapeRefinement: bool) -> Assemblies.BoxSearchTerm:
        ...
    def CreateProximitySearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, seeds: typing.List[Assemblies.SearchResultElement], distance: float, trueShapeRefinement: bool) -> Assemblies.ProximitySearchTerm:
        ...
    def CreateRunContentProximitySearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, seedRunName: str, distance: float, trueShapeRefinement: bool) -> Assemblies.RunContentProximitySearchTerm:
        ...
    def CreatePlaneSearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, overlapType: Assemblies.PlaneSearchTerm.PlaneOverlapLogicType, normal: Vector3d, displacement: float, pointOnPlane: Point3d, trueShapeRefinement: bool) -> Assemblies.PlaneSearchTerm:
        ...
    def CreateAttributeSearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, queryName: str, entries: str, values: str) -> Assemblies.AttributeSearchTerm:
        ...
    def CreatePartitionSearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, partition: Assemblies.Partition) -> Assemblies.PartitionSearchTerm:
        """[Obsolete("Deprecated in NX11.0.0.  Use the NXOpen.Assemblies.SubsetRecipe.CreatePartitionSearchTerm that gives specific control on whether or not to include children partition as well")"""
        ...
    def CreatePartitionSearchTermGroup(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, partitions: typing.List[Assemblies.Partition]) -> Assemblies.GroupSearchTerm:
        """[Obsolete("Deprecated in NX11.0.0.  Use the NXOpen.Assemblies.SubsetRecipe.CreatePartitionSearchTermGroup that gives specific control on whether or not to include children partition as well")"""
        ...
    def CreatePartitionSearchTerm(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, includeChildrenLogic: Assemblies.PartitionSearchTerm.IncludeChildren, partition: Assemblies.Partition) -> Assemblies.PartitionSearchTerm:
        ...
    def CreatePartitionSearchTermGroup(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, includeChildrenLogic: Assemblies.PartitionSearchTerm.IncludeChildren, partitions: typing.List[Assemblies.Partition]) -> Assemblies.GroupSearchTerm:
        ...
    def MoveUp(self, searchTerm: Assemblies.SearchTerm) -> None:
        ...
    def MoveDown(self, searchTerm: Assemblies.SearchTerm) -> None:
        ...
    def Group(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, searchTerms: typing.List[Assemblies.SearchTerm]) -> None:
        ...
    def Ungroup(self, searchTerms: typing.List[Assemblies.SearchTerm]) -> None:
        ...
    def DeleteSearchTerms(self, searchTerms: typing.List[Assemblies.SearchTerm]) -> None:
        ...
    def SetSearchTermLogic(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, searchTerms: typing.List[Assemblies.SearchTerm]) -> None:
        ...
    def SetPartitionSearchTermLogic(self, logicType: Assemblies.SearchTerm.SearchTermLogicType, includeChildrenLogic: Assemblies.PartitionSearchTerm.IncludeChildren, searchTerms: typing.List[Assemblies.SearchTerm]) -> None:
        ...
    def SetSearchOptionValue(self, optionSet: str, searchOption: str, optionValue: bool) -> None:
        ...
    def GetSearchOptionValue(self, optionSet: str, searchOption: str) -> bool:
        ...
    def GetAllSearchOptions(self, optionSet: str) -> str:
        ...
    def GetAllSearchOptionSets(self) -> str:
        ...
    def Tag(self) -> Tag: ...



class SubsetConfigurationBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Commit(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Effectivity: BasicEffectivityBuilder
    RevisionRule: str


class SubsetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.Subset]:
        ...
    def __init__(self, owner: Assemblies.ComponentAssembly) -> None: ...
    def __init__(self) -> None: ...
    def CreateSubsetBuilder(self, subset: Assemblies.Subset) -> Assemblies.SubsetBuilder:
        ...
    def CreateBoxSearchTermBuilder(self, boxSearchTerm: Assemblies.BoxSearchTerm) -> Assemblies.BoxSearchTermBuilder:
        ...
    def CreatePlaneSearchTermBuilder(self, planeSearchTerm: Assemblies.PlaneSearchTerm) -> Assemblies.PlaneSearchTermBuilder:
        ...
    def CreateAttributeSearchTermBuilder(self, attributeSearchTerm: Assemblies.AttributeSearchTerm) -> Assemblies.AttributeSearchTermBuilder:
        ...
    def CreateProximitySearchTermBuilder(self, proximitySearchTerm: Assemblies.ProximitySearchTerm) -> Assemblies.ProximitySearchTermBuilder:
        ...
    def CreateRunContentProximitySearchTermBuilder(self, runContentProximitySearchTerm: Assemblies.RunContentProximitySearchTerm) -> Assemblies.RunContentProximitySearchTermBuilder:
        ...
    def CreatePositioningTaskBuilder(self, positioningTask: Assemblies.PositioningTask) -> Assemblies.PositioningTaskBuilder:
        ...
    def CreateMechanicalRoutingSubsetBuilder(self, subsetBuilderTag: Assemblies.SubsetBuilder) -> Assemblies.MechanicalRoutingSubsetBuilder:
        ...
    def CreateMechanicalRoutingSubsetBuilderForSurroundingEdit(self, subsetBuilderTag: Assemblies.SubsetBuilder) -> Assemblies.MechanicalRoutingSubsetBuilder:
        ...
    def Tag(self) -> Tag: ...



class SubsetBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSubsets(self, subsets: typing.List[Assemblies.Subset]) -> None:
        ...
    def GenerateResults(self) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> NXObject:
        ...
    def GetSubsetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def UpdateConfigurationContext(self, logicalObject: PDM.LogicalObject) -> None:
        ...
    def UpdateSubsetConfigurationOfDependentSubset(self) -> None:
        ...
    def UpdateSubsetTargetPropertiesOfDependentSubset(self) -> None:
        ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...
    SearchResults: Assemblies.SearchResultCollection
    Recipe: Assemblies.SubsetRecipe
    AddAllSubordinates: bool
    CollaborativeDesign: CollaborativeDesign
    ConfigurationContext: PDM.ConfigurationContextBuilder
    ContentDefinition: ContentDefinition
    Finder: Assemblies.FindInCollaborativeDesign
    Subset: Assemblies.Subset
    SubsetConfiguration: Assemblies.SubsetConfigurationBuilder
    SubsetDescription: str
    SubsetName: str
    SubsetType: Assemblies.Subset.ContentType
    TargetEffectivity: BasicEffectivityBuilder
    TargetEffectivityTable: PDM.EffectivityTableBuilder
    TargetPartitionList: Assemblies.PartitionList
    ViewedPartitionScheme: Assemblies.PartitionScheme
    Workset: Assemblies.ComponentAssembly


class Subset(NXObject):
    def __init__(self) -> None: ...
    def ReplayRecipe(self) -> None:
        ...
    def RemoveDesignElements(self, designElements: typing.List[NXObject]) -> None:
        ...
    def DeleteFromCollaborativeDesign(self, designElement: typing.List[NXObject]) -> None:
        ...
    def AddInterpartParents(self) -> None:
        ...
    def AddConnectedByElements(self) -> None:
        ...
    def AddAllChildrenToSubset(self, reuseDesignElements: typing.List[Assemblies.Component]) -> None:
        ...
    def AddNewChildrenToSubset(self) -> None:
        ...
    def GetDesignElementRevisionMembers(self) -> typing.List[PDM.DesignElementRevision]:
        ...
    def GetDesignElementRevisionParents(self) -> typing.List[PDM.DesignElementRevision]:
        ...
    def GetDesignSubordinateRevisionMembers(self) -> typing.List[PDM.DesignSubordinateRevision]:
        ...
    def GetDesignSubordinateRevisionParents(self) -> typing.List[PDM.DesignSubordinateRevision]:
        ...
    def ShowCollaborativeDesignPreview(self) -> bool:
        ...
    def HideCollaborativeDesignPreview(self) -> None:
        ...
    def IsCollaborativeDesignPreviewDisplayed(self) -> bool:
        ...
    def GetTargetPartitionSet(self, partitions: typing.List[Assemblies.Partition]) -> None:
        ...
    def SetTargetPartitionSet(self, partitions: typing.List[Assemblies.Partition]) -> None:
        ...
    def GetAllPositioningTasks(self) -> typing.List[Assemblies.PositioningTask]:
        ...
    def DeletePositioningTask(self, positioningTask: Assemblies.PositioningTask) -> None:
        ...
    def SetContentDefinition(self, contentDefinition: ContentDefinition) -> None:
        ...
    def ReplaceContentDefinition(self, contentDefinition: ContentDefinition) -> None:
        ...
    def CanReplaceContentDefinition(self, contentDefinition: ContentDefinition) -> bool:
        ...
    def AddDesignElementsToSubset(self, designElements: typing.List[PDM.ModelElementRevision]) -> PartLoadStatus:
        ...
    AllowMultipleTargetPartitions: bool
    ComponentInWorkset: Assemblies.Component
    Description: str
    DisplayExcludedDesignElements: bool
    PartitionViewStyle: Assemblies.Subset.PartitionViewStyleType
    ShowSubsetStructure: bool
    SubsetType: Assemblies.Subset.ContentType


    class PartitionViewStyleType(enum.Enum):
        None = 0
        Flat = 1
        Hierarchical = 2
    

    class ContentType(enum.Enum):
        Public = 0
        Baseline = 1
        ChangeNotice = 2
    

class ShowComponentBuilder(Builder):
    def __init__(self) -> None: ...
    Components: SelectTaggedObjectList
    MaintainComponentsShown: bool
    Views: Drawings.SelectDraftingViewList


class SelectComponentList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Assemblies.Component) -> bool:
        ...
    def Add(self, objects: typing.List[Assemblies.Component]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Assemblies.Component, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Assemblies.Component) -> bool:
        ...
    def Remove(self, object: Assemblies.Component, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Assemblies.Component, view1: View, point1: Point3d, selection2: Assemblies.Component, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Assemblies.Component]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Assemblies.Component) -> bool:
        ...
    def SetArray(self, objects: typing.List[Assemblies.Component]) -> None:
        ...
    def GetArray(self) -> typing.List[Assemblies.Component]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Assemblies.Component, view1: View, point1: Point3d, selection2: Assemblies.Component, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Assemblies.Component, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectComponent(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Assemblies.Component, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Assemblies.Component, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Assemblies.Component, view1: View, point1: Point3d, selection2: Assemblies.Component, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Assemblies.Component, view1: View, point1: Point3d, selection2: Assemblies.Component, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Assemblies.Component, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Assemblies.Component:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Assemblies.Component


class SearchTermBuilder(Builder):
    def __init__(self) -> None: ...


class SearchTerm(NXObject):
    def __init__(self) -> None: ...


    class SearchTermLogicType(enum.Enum):
        Include = 0
        Exclude = 1
        Filter = 2
    

class SearchResultElement(NXObject):
    def __init__(self) -> None: ...
    ModelElementRevision: PDM.ModelElementRevision


class SearchResultCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.SearchResultElement]:
        ...
    def __init__(self, owner: Assemblies.SubsetBuilder) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Assemblies.SearchResultElement:
        ...
    def Tag(self) -> Tag: ...



class RunContentProximitySearchTermBuilder(Assemblies.SearchTermBuilder):
    def __init__(self) -> None: ...
    def GetSeedName(self) -> str:
        ...
    def SetSeedName(self, seedRunName: str) -> None:
        ...
    Distance: float
    SearchTermLogic: Assemblies.SearchTerm.SearchTermLogicType
    TrueShapeRefinement: bool


class RunContentProximitySearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...


class ReplaceComponentBuilder(Builder):
    def __init__(self) -> None: ...
    def GetComponentReferenceSetType(self, referenceSetName: str) -> Assemblies.ReplaceComponentBuilder.ComponentReferenceSet:
        ...
    def SetComponentReferenceSetType(self, componentReferenceSet: Assemblies.ReplaceComponentBuilder.ComponentReferenceSet, referenceSetName: str) -> None:
        ...
    def RegisterReplacePartLoadStatus(self) -> PartLoadStatus:
        ...
    def GetErrorList(self) -> ErrorList:
        ...
    AllowTemporaryPartsToReplace: bool
    ComponentLayer: int
    ComponentLayerOptionType: Assemblies.ReplaceComponentBuilder.ComponentLayerOption
    ComponentName: str
    ComponentNameType: Assemblies.ReplaceComponentBuilder.ComponentNameOption
    ComponentsToReplace: SelectDisplayableObjectList
    MaintainRelationships: bool
    ReplaceAllOccurrences: bool
    ReplacementPart: str


    class ComponentReferenceSet(enum.Enum):
        Maintain = 0
        EntirePart = 1
        Empty = 2
        Others = 3
    

    class ComponentNameOption(enum.Enum):
        Maintain = 0
        Original = 1
        AsSpecified = 2
    

    class ComponentLayerOption(enum.Enum):
        Maintain = 0
        Original = 1
        Work = 2
        AsSpecified = 3
    

class RelinkerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.RelinkerBuilder]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self) -> Assemblies.RelinkerBuilder:
        ...
    def Tag(self) -> Tag: ...



class RelinkerBuilder(Builder):
    def __init__(self) -> None: ...
    def ExecuteRelink(self) -> None:
        ...
    def SearchWavelinksInterpartExpressions(self) -> None:
        ...
    def ExportToInformationWindow(self) -> None:
        ...
    def UpdateSession(self) -> None:
        ...
    def UpdateSessionWithBreakDelayed(self) -> None:
        ...
    def ViewFeatureFailure(self) -> None:
        ...
    def GetExpressionSourceCount(self, partID: Part, expID: Expression, sourceID: Expression) -> int:
        ...
    def RelinkInterpartExpression(self, partID: Part, expID: Expression, sourceID: Expression) -> None:
        ...
    def RelinkWaveFeature(self, partID: Part, featID: Features.Feature, sourceID: NXObject) -> None:
        ...
    BreakInterpartExpression: bool
    BreakWaveLink: bool
    FaceCurveDirectionAdjustment: bool
    IncludeNonBrokenWaveLinks: bool
    IncludeSuppressedComponents: bool
    RelinkCategory: Assemblies.RelinkerBuilder.LinkCategory
    RelinkOption: Assemblies.RelinkerBuilder.LinkOption
    RelinkType: Assemblies.RelinkerBuilder.LinkType
    SearchExistingInterPartExpressionOnly: bool
    SearchingDestinationObject: str
    SearchingSourceObject: str
    SearchingSourcePart: str
    SearchingSourcePartAttribute: str
    SelectComponent: Assemblies.SelectComponentList
    SelectComponentSource: Assemblies.SelectComponentList
    SourceScope: Assemblies.RelinkerBuilder.LinkScope
    TargetScope: Assemblies.RelinkerBuilder.LinkScope


    class LinkType(enum.Enum):
        All = 0
        NotBroken = 1
        Broken = 2
        AutoLinked = 3
        WithMultipleSource = 4
    

    class LinkScope(enum.Enum):
        PartsInSession = 0
        PartsInAssembly = 1
        WorkPart = 2
        SelectedParts = 3
    

    class LinkOption(enum.Enum):
        InterpartExpression = 0
        WaveGeometry = 1
        Both = 2
    

    class LinkCategory(enum.Enum):
        WaveGeometry = 0
        InterpartExpression = 1
    

class ProximitySearchTermBuilder(Assemblies.SearchTermBuilder):
    def __init__(self) -> None: ...
    def GetSeeds(self, seeds: typing.List[Assemblies.SearchResultElement]) -> None:
        ...
    def SetSeeds(self, seeds: typing.List[Assemblies.SearchResultElement]) -> None:
        ...
    Distance: float
    SearchTermLogic: Assemblies.SearchTerm.SearchTermLogicType
    TrueShapeRefinement: bool


class ProximitySearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...


class ProductOutlineManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateProductOutlineBuilder(self) -> Assemblies.ProductOutlineBuilder:
        ...
    def ShowProductOutline(self, isShow: bool) -> None:
        ...
    def ShowSelectableProductOutline(self, isSelectable: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    IsProductOutlineDefined: bool


class ProductOutlineBuilder(Builder):
    def __init__(self) -> None: ...
    LineFontType: Assemblies.ProductOutlineBuilder.LineFont
    OutlineColor: NXColor
    OverrideColor: bool
    SelectObject: SelectDisplayableObjectList
    Translucency: int


    class LineFont(enum.Enum):
        Solid = 0
        Dashed = 1
        Phantom = 2
        Centerline = 3
        Dotted = 4
        Longdash = 5
        Dotdash = 6
    

class PositionOverrideType(enum.Enum):
    None = 0
    Unloaded = 1
    Explicit = 2
    MatingImplicit = 3
    ConstraintImplicit = 4


class PositioningTaskBuilder(Builder):
    def __init__(self) -> None: ...
    ContextCollection: SelectDisplayableObjectList
    OwningSubset: Assemblies.Subset
    WorkCollection: SelectDisplayableObjectList


class PositioningTask(NXObject):
    def __init__(self) -> None: ...
    def IsInWorkCollection(self, component: Assemblies.Component) -> bool:
        ...
    def GetAllWorkCollectionMembers(self) -> typing.List[Assemblies.Component]:
        ...
    def IsInContextCollection(self, component: Assemblies.Component) -> bool:
        ...
    def GetAllContextCollectionMembers(self) -> typing.List[Assemblies.Component]:
        ...
    def ActivatePositioningGroup(self, positioningGroup: Assemblies.PositioningGroup) -> None:
        ...
    def DeactivatePositioningGroup(self, positioningGroup: Assemblies.PositioningGroup) -> None:
        ...
    def CheckOutPositioningGroups(self, positioningGroups: typing.List[Assemblies.PositioningGroup]) -> ErrorList:
        ...
    def CheckInPositioningGroups(self, positioningGroups: typing.List[Assemblies.PositioningGroup]) -> ErrorList:
        ...
    def Ungroup(self, positioningGroup: Assemblies.PositioningGroup) -> None:
        ...
    def RemoveFromTask(self, positioningGroup: Assemblies.PositioningGroup) -> None:
        ...
    def GetAllPositioningGroups(self) -> typing.List[Assemblies.PositioningGroup]:
        ...
    def Activate(self) -> None:
        ...
    def Deactivate(self) -> None:
        ...
    DisplayConstraints: bool
    DisplaySuppressedConstraints: bool


class PositioningGroupBuilder(Builder):
    def __init__(self) -> None: ...
    MakeActive: bool
    OwningPositioningTask: Assemblies.PositioningTask
    PositioningGroupDataMembers: SelectDisplayableObjectList
    PositioningGroupName: str


class PositioningGroup(NXObject):
    def __init__(self) -> None: ...
    def GetStatus(self) -> Assemblies.PositioningGroup.Status:
        ...
    DisplayConstraints: bool
    DisplaySuppressedConstraints: bool


    class Status(enum.Enum):
        OutOfDate = 0
        UpToDate = 1
        Unknown = 2
    

class PlaneSearchTermBuilder(Assemblies.SearchTermBuilder):
    def __init__(self) -> None: ...
    Displacement: float
    Normal: Vector3d
    PlaneOverlapLogic: Assemblies.PlaneSearchTerm.PlaneOverlapLogicType
    PointOnPlane: Point3d
    SearchTermLogic: Assemblies.SearchTerm.SearchTermLogicType
    TrueShapeRefinement: bool


class PlaneSearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...


    class PlaneOverlapLogicType(enum.Enum):
        Above = 0
        Below = 1
        Intersects = 2
        AboveOrIntersects = 3
        BelowOrIntersects = 4
    

class PatternMember(NXObject):
    def __init__(self) -> None: ...
    def GetAllComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def IsPatternMaster(self) -> bool:
        ...


class PatternMaster(Assemblies.PatternMember):
    def __init__(self) -> None: ...


class PatternInstance(Assemblies.PatternMember):
    def __init__(self) -> None: ...
    def GetIndices(self, index1: int) -> int:
        ...
    def GetSuppressedStatus(self) -> bool:
        ...
    def GetDeletedStatus(self) -> bool:
        ...
    def GetClockedStatus(self) -> bool:
        ...


class PartitionSearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...
    Partition: Assemblies.Partition


    class IncludeChildren(enum.Enum):
        False = 0
        True = 1
    

class PartitionScheme(NXObject):
    def __init__(self) -> None: ...
    def GetRootPartitions(self, rootPartitions: typing.List[Assemblies.Partition]) -> None:
        ...
    CollaborativeDesign: CollaborativeDesign


class PartitionList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Assemblies.Partition]) -> None:
        ...
    def Append(self, object: Assemblies.Partition) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Assemblies.Partition) -> int:
        ...
    def FindItem(self, index: int) -> Assemblies.Partition:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Assemblies.Partition) -> None:
        ...
    def Erase(self, obj: Assemblies.Partition, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Assemblies.Partition]:
        ...
    def SetContents(self, objects: typing.List[Assemblies.Partition]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Assemblies.Partition, object2: Assemblies.Partition) -> None:
        ...
    def Insert(self, location: int, object: Assemblies.Partition) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class Partition(NXObject):
    def __init__(self) -> None: ...
    def LoadImmediateChildPartitions(self) -> None:
        ...
    def GetImmediateChildPartitions(self, partitionChildren: typing.List[Assemblies.Partition]) -> None:
        ...


class OrderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.Order]:
        ...
    def __init__(self, owner: Assemblies.ComponentAssembly) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Assemblies.Order:
        ...
    def Tag(self) -> Tag: ...



class Order(NXObject):
    def __init__(self) -> None: ...
    def GetReversed(self) -> bool:
        ...
    def SetReversed(self, isReversed: bool) -> None:
        ...
    def Activate(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    def Save(self) -> None:
        ...
    def SaveAs(self, newName: str) -> Assemblies.Order:
        ...
    def GetChildrenOrder(self, parent: Assemblies.Component, children: typing.List[Assemblies.Component]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Assemblies.ComponentOrder.AskChildrenOrder instead to get children order in this NXOpen.Assemblies.ComponentOrder.")"""
        ...
    def IsActive(self) -> bool:
        ...
    OrderState: Assemblies.Order.State
    OrderType: Assemblies.Order.Type


    class Type(enum.Enum):
        UserDefinedComponent = 0
        SequentialComponent = 1
        ChronologicalComponent = 2
        AlphanumericComponent = 3
        AlphabeticComponent = 4
    

    class State(enum.Enum):
        UnSaved = 0
        Saved = 1
    

class MechanicalRoutingSubsetBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSearchSubsetBuilder(self) -> Assemblies.SubsetBuilder:
        ...
    def SetSearchSubsetBuilder(self, subsetBuilder: Assemblies.SubsetBuilder) -> None:
        ...
    def GetConfigurationContextBuilder(self) -> PDM.ConfigurationContextBuilder:
        ...
    def AppendSearchResultElementToSelectedList(self, runID: str) -> None:
        ...
    def RemoveSearchResultElementFromSelectedList(self, runID: str) -> None:
        ...
    def RemoveAllSearchResultElementsFromSelectedList(self) -> None:
        ...
    def UpdateSubsetUsingConfigurationContext(self, inputSubsetBuilder: Assemblies.SubsetBuilder) -> Assemblies.SubsetBuilder:
        ...
    def SetRoutingSubsetAsWorkPart(self) -> None:
        ...
    Fixtures: bool
    Insulation: bool
    SurroundingDataProximityDistance: float
    SurroundingDataRecipeMethodType: Assemblies.MechanicalRoutingSubsetBuilder.SurroundingDataRecipeMethod


    class SurroundingDataRecipeMethod(enum.Enum):
        None = 0
        ProximitytoRoutingContent = 1
        Manual = 2
    

class MakeUniquePartBuilder(Builder):
    def __init__(self) -> None: ...
    CopyChoices: Assemblies.MakeUniquePartBuilder.Option
    SelectedComponents: SelectDisplayableObjectList


    class Option(enum.Enum):
        CopyAssemblyOnly = 0
    

class LoadInterpartDataBuilder(Builder):
    def __init__(self) -> None: ...
    def GetFailedParts(self) -> typing.List[BasePart]:
        ...
    def GetLoadInterpartDataStatus(self, part: BasePart, loadStatus: PartLoadStatus, delayedUpdateStatus: PartDelayedUpdateStatus) -> None:
        ...
    OpenUnloadedParents: Assemblies.LoadInterpartDataBuilder.OpenUnloadedParentsType
    SelectionScope: Assemblies.LoadInterpartDataBuilder.SelectionScopeType


    class SelectionScopeType(enum.Enum):
        AllPartsInDisplayedAssembly = 0
        AllPartsInSession = 1
    

    class OpenUnloadedParentsType(enum.Enum):
        None = 0
        ImmediateLevel = 1
        AllLevels = 2
    

class HideComponentBuilder(Builder):
    def __init__(self) -> None: ...
    Components: SelectTaggedObjectList
    Views: Drawings.SelectDraftingViewList


class GroupSearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...


class FindInCollaborativeDesign(NXObject):
    def __init__(self) -> None: ...
    def PerformFind(self, objectType: Assemblies.FindInCollaborativeDesign.ObjectType, searchType: Assemblies.FindInCollaborativeDesign.SearchType, searchText: str) -> None:
        ...
    def PerformFind(self, partition: Assemblies.Partition, objectType: Assemblies.FindInCollaborativeDesign.ObjectType, searchType: Assemblies.FindInCollaborativeDesign.SearchType, searchText: str) -> None:
        ...
    def PerformFind(self, objectType: Assemblies.FindInCollaborativeDesign.ObjectType, searchType: Assemblies.FindInCollaborativeDesign.SearchType, criteriaTitles: str, criteriaValues: str) -> None:
        ...
    def GetPartitions(self) -> typing.List[Assemblies.Partition]:
        ...
    def GetSearchResultElements(self) -> typing.List[Assemblies.SearchResultElement]:
        ...


    class SearchType(enum.Enum):
        ItemQuery = 0
    

    class ObjectType(enum.Enum):
        Partition = 0
        DesignElement = 1
        RunElement = 2
    

class ExplosionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.Explosion]:
        ...
    def __init__(self, owner: Assemblies.ComponentAssembly) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, explosionName: str) -> Assemblies.Explosion:
        ...
    def FindObject(self, name: str) -> Assemblies.Explosion:
        ...
    def Tag(self) -> Tag: ...



class Explosion(NXObject):
    def __init__(self) -> None: ...
    def Copy(self, destinationExplosion: Assemblies.Explosion) -> None:
        ...
    def Show(self, view: View) -> None:
        ...
    def Hide(self, view: View) -> None:
        ...
    def Delete(self) -> None:
        ...
    RootComponent: Assemblies.ExplodedComponent


class ExplodedComponent(Assemblies.Component):
    def __init__(self) -> None: ...
    def GetExplosion(self) -> Assemblies.Explosion:
        ...
    def GetComponent(self) -> Assemblies.Component:
        ...


class ExplicitSearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...
    SearchResultElement: Assemblies.SearchResultElement


class DrawingExplosionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.DrawingExplosion]:
        ...
    def __init__(self, owner: Assemblies.ComponentAssembly) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Assemblies.DrawingExplosion:
        ...
    def Tag(self) -> Tag: ...



class DrawingExplosion(NXObject):
    def __init__(self) -> None: ...
    RootComponent: Assemblies.ExplodedComponent


class DesignElementBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPosition(self, position: Point3d, orientation: Matrix3x3) -> None:
        ...
    def SetPosition(self, position: Point3d, orientation: Matrix3x3) -> None:
        ...
    def GetAddPartitions(self, partitions: typing.List[Assemblies.Partition]) -> None:
        ...
    def AddToPartitions(self, partitions: typing.List[Assemblies.Partition]) -> None:
        ...
    def GetRemovePartitions(self, partitions: typing.List[Assemblies.Partition]) -> None:
        ...
    def RemoveFromPartitions(self, partitions: typing.List[Assemblies.Partition]) -> None:
        ...
    def CreateLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def PartiallyCommit(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetOperationFailures(self) -> ErrorList:
        ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...
    Count: int
    DesignElementType: str
    DesignElementsToOperate: SelectDisplayableObjectList
    EditAction: Assemblies.DesignElementBuilder.EditActionType
    Effectivity: BasicEffectivityBuilder
    EffectivityTable: PDM.EffectivityTableBuilder
    FileNewDescriptor: FileNew
    KeepOriginalDesignElement: bool
    Layer: int
    LayerOption: Assemblies.DesignElementBuilder.LayerOptionType
    OwningSubsetInstance: Assemblies.Subset
    PartToUse: BasePart
    PositioningOptionValue: Assemblies.DesignElementBuilder.PositioningOption
    ReferenceSet: Assemblies.DesignElementBuilder.ReferenceSetType
    ReferenceSetName: str
    SaveAsAction: Assemblies.DesignElementBuilder.SaveAsActionType
    Scatter: bool
    State: Assemblies.DesignElementBuilder.StateType


    class StateType(enum.Enum):
        Shape = 0
        Reuse = 1
        Promissory = 2
    

    class SaveAsActionType(enum.Enum):
        NewRevision = 0
        NewDesignElement = 1
    

    class ReferenceSetType(enum.Enum):
        Model = 0
        EntirePart = 1
        AsSpecified = 2
    

    class PositioningOption(enum.Enum):
        AbsoluteOrigin = 0
        Maintain = 1
        AsSpecified = 2
    

    class OperationType(enum.Enum):
        Create = 0
        Edit = 1
        SaveAs = 2
        Save = 3
        SaveAndClose = 4
        Undefined = 5
    

    class LayerOptionType(enum.Enum):
        Original = 0
        Work = 1
        AsSpecified = 2
    

    class EditActionType(enum.Enum):
        Category = 0
        Partitions = 1
        Effectivity = 2
    

class DeleteOverridePartBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentSelectionList: Assemblies.SelectComponentList


class DegreesOfFreedomStatus(enum.Enum):
    NotUsed = 0
    Static = 1
    Free = 2
    Instantaneous = 3
    StaticNormal = 4
    FreeNormal = 5
    InstantaneousNormal = 6


class DegreesOfFreedomResult(enum.Enum):
    Unknown = 0
    Success = 1


class DegreesOfFreedom():
    Result: Assemblies.DegreesOfFreedomResult
    NumRotational: int
    NumTranslational: int
    NumInstantaneousRotational: int
    NumInstantaneousTranslational: int
    BasePoint1Status: Assemblies.DegreesOfFreedomStatus
    BasePoint1: Point3d
    RotationDirection1Status: Assemblies.DegreesOfFreedomStatus
    RotationDirection1: Vector3d
    BasePoint2Status: Assemblies.DegreesOfFreedomStatus
    BasePoint2: Point3d
    RotationDirection2Status: Assemblies.DegreesOfFreedomStatus
    RotationDirection2: Vector3d
    TranslationDirection1Status: Assemblies.DegreesOfFreedomStatus
    TranslationDirection1: Vector3d
    TranslationDirection2Status: Assemblies.DegreesOfFreedomStatus
    TranslationDirection2: Vector3d
    def ToString(self) -> str:
        ...


class CreateOverridePartBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentSelectionList: Assemblies.SelectComponentList
    MakeWorkPart: bool


class CreateNewComponentBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentCam: Assemblies.CreateNewComponentBuilder.ComponentCamType
    ComponentOrigin: Assemblies.CreateNewComponentBuilder.ComponentOriginType
    DefiningObjectsAdded: bool
    LayerNumber: int
    LayerOption: Assemblies.CreateNewComponentBuilder.ComponentLayerOptionType
    NewComponentName: str
    NewFile: FileNew
    ObjectForNewComponent: SelectDisplayableObjectList
    OriginalObjectsDeleted: bool
    ReferenceSet: Assemblies.CreateNewComponentBuilder.ComponentReferenceSetType
    ReferenceSetName: str


    class ComponentReferenceSetType(enum.Enum):
        Model = 0
        EntirePartOnly = 1
        Other = 2
    

    class ComponentOriginType(enum.Enum):
        Wcs = 0
        Absolute = 1
    

    class ComponentLayerOptionType(enum.Enum):
        Original = 0
        Work = 1
        AsSpecified = 2
    

    class ComponentCamType(enum.Enum):
        Target = 0
        Resource = 1
        Workpiece = 2
    

class CreateComponentBuilder(Builder):
    def __init__(self) -> None: ...


class CopyDesignElementBuilder(Builder):
    def __init__(self) -> None: ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetOperationFailures(self) -> ErrorList:
        ...
    def PartiallyCommit(self) -> None:
        ...
    def CreateDesignElementLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def DeleteCopiedComponents(self) -> None:
        ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...
    DesignElementsToCopy: SelectDisplayableObjectList


class ConstraintDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    ChangeComponentVisibility: bool
    FilterNavigator: bool
    ObjectSelection: SelectDisplayableObjectList
    VisibleConstraintsRule: Assemblies.ConstraintDisplayBuilder.VisibleConstraintsRuleOptions


    class VisibleConstraintsRuleOptions(enum.Enum):
        BetweenComponents = 0
        ConnectedToComponents = 1
    

class ComponentQuantity(enum.Enum):
    None = 0
    Integer = 1
    Real = 2
    AsRequired = 3


class ComponentPatternCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.ComponentPattern]:
        ...
    def __init__(self, owner: Assemblies.ComponentAssembly) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Assemblies.ComponentPattern:
        ...
    def GetAllComponentPatterns(self, componentPatterns: typing.List[Assemblies.ComponentPattern]) -> None:
        ...
    def Tag(self) -> Tag: ...



class ComponentPatternBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDynamicPositioning(self) -> bool:
        ...
    def SetDynamicPositioning(self, isDynamicPositioning: bool) -> None:
        ...
    def SetObject(self, compPattern: Assemblies.ComponentPattern) -> None:
        ...
    Associative: bool
    ComponentPatternSet: SelectDisplayableObjectList
    CopyConstraintPattern: bool
    PatternService: GeometricUtilities.PatternDefinition


class ComponentPattern(NXObject):
    def __init__(self) -> None: ...
    def Delete(self, deleteComponents: bool) -> None:
        ...
    def Suppress(self) -> None:
        ...
    def Unsuppress(self) -> None:
        ...
    def DisplayInformation(self) -> None:
        ...
    def LoadRelatedGeometry(self) -> PartLoadStatus:
        ...
    def GetPatternName(self) -> str:
        ...
    def GetPatternSuppressedStatus(self) -> bool:
        ...
    def GetPatternDeferredStatus(self) -> bool:
        ...
    def GetAllPatternMembers(self) -> typing.List[Assemblies.PatternMember]:
        ...
    def GetComponentsToPattern(self) -> typing.List[Assemblies.Component]:
        ...
    def ChangeReferencePatternTemplate(self, firstBaseInstanceIndex: int, secondBaseInstanceIndex: int) -> None:
        ...


class ComponentOrder(Assemblies.Order):
    def __init__(self) -> None: ...
    def AskChildrenOrder(self, parent: Assemblies.Component) -> typing.List[Assemblies.Component]:
        ...


class ComponentGroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.ComponentGroup]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Assemblies.ComponentGroup:
        ...
    def CreateComponentGroup(self, name: str) -> Assemblies.ComponentGroup:
        ...
    def Tag(self) -> Tag: ...



class ComponentGroup(NXObject):
    def __init__(self) -> None: ...
    def Open(self) -> PartLoadStatus:
        ...
    def GetComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def AddComponent(self, component: Assemblies.Component, andChildren: bool) -> None:
        ...
    def RemoveComponent(self, component: Assemblies.Component) -> None:
        ...
    NumberOfComponents: int


class ComponentAssembly(NXObject):
    def __init__(self) -> None: ...
    def AddComponent(self, partToAdd: str, referenceSetName: str, componentName: str, basePoint: Point3d, orientation: Matrix3x3, layer: int, loadStatus: PartLoadStatus) -> Assemblies.Component:
        ...
    def AddComponent(self, partToAdd: str, referenceSetName: str, componentName: str, basePoint: Point3d, orientation: Matrix3x3, layer: int, loadStatus: PartLoadStatus, uomAsNgc: bool) -> Assemblies.Component:
        ...
    def AddComponents(self, partsToAdd: typing.List[Part], point: Point3d, orientation: Matrix3x3, layer: int, referenceSetName: str, count: int, scatter: bool, components: typing.List[Assemblies.Component]) -> None:
        ...
    def AddComponent(self, partToAdd: BasePart, referenceSetName: str, componentName: str, basePoint: Point3d, orientation: Matrix3x3, layer: int, loadStatus: PartLoadStatus) -> Assemblies.Component:
        ...
    def AddMasterPartComponent(self, partToAdd: str, referenceSetName: str, componentName: str, basePoint: Point3d, orientation: Matrix3x3, layer: int, loadStatus: PartLoadStatus) -> Assemblies.Component:
        ...
    def AddMasterPartComponent(self, partToAdd: Part, referenceSetName: str, componentName: str, basePoint: Point3d, orientation: Matrix3x3, layer: int, loadStatus: PartLoadStatus) -> Assemblies.Component:
        ...
    def InsertProduct(self, productPart: Part, layer: int, loadStatus: PartLoadStatus) -> Assemblies.Component:
        ...
    def SubstituteComponent(self, component: Assemblies.Component, part: BasePart, newName: str, referenceSet: str, layer: int, mode: Assemblies.ComponentAssembly.SubstitutionMode) -> Assemblies.Component:
        ...
    def RemoveComponent(self, component: Assemblies.Component) -> None:
        ...
    def MapComponentFromParent(self, component: Assemblies.Component) -> Assemblies.Component:
        ...
    def MapComponentsFromSubassembly(self, component: Assemblies.Component) -> typing.List[Assemblies.Component]:
        ...
    def ChangeByName(self, name: str, partOccs: typing.List[Assemblies.Component]) -> None:
        ...
    def SetDefault(self, arrangement: Assemblies.Arrangement) -> None:
        ...
    def SuppressComponents(self, components: typing.List[Assemblies.Component], arrangements: typing.List[Assemblies.Arrangement]) -> ErrorList:
        ...
    def SuppressComponents(self, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def SuppressComponents(self, components: typing.List[Assemblies.Component], arrangements: typing.List[Assemblies.Arrangement], expression: str) -> ErrorList:
        ...
    def UnsuppressComponents(self, components: typing.List[Assemblies.Component], arrangements: typing.List[Assemblies.Arrangement]) -> ErrorList:
        ...
    def UnsuppressComponents(self, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def ReleaseSuppression(self, components: typing.List[Assemblies.Component], arrangements: typing.List[Assemblies.Arrangement]) -> ErrorList:
        ...
    def ReleaseSuppression(self, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def SetEntirePartRefset(self, component: Assemblies.Component) -> None:
        ...
    def SetEmptyRefset(self, component: Assemblies.Component) -> None:
        ...
    def ReplaceReferenceSetInOwners(self, newReferenceSet: str, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def ReplaceReferenceSet(self, component: Assemblies.Component, newReferenceSet: str) -> None:
        ...
    def MoveComponent(self, component: Assemblies.Component, translation: Vector3d, rotation: Matrix3x3) -> None:
        ...
    def CreateMatingConverter(self) -> Positioning.MatingConverter:
        ...
    def DeleteMatingConditions(self) -> None:
        ...
    def ConvertRememberedMcs(self) -> None:
        ...
    def SetNonGeometricState(self, component: Assemblies.Component, nonGeometricState: bool) -> None:
        ...
    def GetNonGeometricState(self, component: Assemblies.Component) -> bool:
        ...
    def GetComponentQuantityType(self, component: Assemblies.Component) -> Assemblies.ComponentQuantity:
        ...
    def SetIntegerQuantity(self, component: Assemblies.Component, integerQuantity: int) -> None:
        ...
    def GetIntegerQuantity(self, component: Assemblies.Component) -> int:
        ...
    def SetRealQuantity(self, component: Assemblies.Component, realQuantity: float, quantityUnits: str) -> None:
        ...
    def GetRealQuantity(self, component: Assemblies.Component, units: str) -> float:
        ...
    def SetAsRequiredQuantity(self, component: Assemblies.Component) -> None:
        ...
    def GetAsRequiredQuantity(self, component: Assemblies.Component) -> str:
        ...
    def CopyComponents(self, components: typing.List[Assemblies.Component]) -> typing.List[Assemblies.Component]:
        ...
    def RestructureComponents(self, origComponents: typing.List[Assemblies.Component], newParentComponent: Assemblies.Component, deleteFlag: bool, newComponents: typing.List[Assemblies.Component], errorList: ErrorList) -> None:
        ...
    def OpenComponents(self, openOption: Assemblies.ComponentAssembly.OpenOption, componentsToOpen: typing.List[Assemblies.Component], openStatus: typing.List[Assemblies.ComponentAssembly.OpenComponentStatus]) -> PartLoadStatus:
        ...
    def CloseComponents(self, componentsToClose: typing.List[Assemblies.Component], wholeTree: BasePart.CloseWholeTree, closeModified: Assemblies.ComponentAssembly.CloseModified) -> PartCloseStatus:
        ...
    def GetSuppressionExpression(self, component: Assemblies.Component) -> Expression:
        ...
    def GetSuppressionExpression(self, component: Assemblies.Component, arrangement: Assemblies.Arrangement) -> Expression:
        ...
    def GetSuppressedState(self, component: Assemblies.Component, controlled: bool) -> Assemblies.ComponentAssembly.SuppressedState:
        ...
    def GetSuppressedState(self, component: Assemblies.Component, arrangement: Assemblies.Arrangement, controlled: bool) -> Assemblies.ComponentAssembly.SuppressedState:
        ...
    def CreateComponentPatternBuilder(self, compPattern: Assemblies.ComponentPattern) -> Assemblies.ComponentPatternBuilder:
        ...
    def AddPendingComponent(self, partToAdd: str, pendingComponent: NXObject, referenceSetName: str, componentName: str, basePoint: Point3d, orientation: Matrix3x3, layer: int, uomAsNgc: bool) -> PartLoadStatus:
        ...
    def CreateConstraintGroupBuilder(self, group: Positioning.ComponentConstraintGroup, contextComponent: Assemblies.Component) -> Positioning.ComponentConstraintGroupBuilder:
        ...
    def CheckinComponents(self, partOccs: typing.List[Assemblies.Component], checkinInputOption: Assemblies.ComponentAssembly.CheckinCheckoutOption) -> ErrorList:
        ...
    def CheckoutComponents(self, partOccs: typing.List[Assemblies.Component], checkoutInputOption: Assemblies.ComponentAssembly.CheckinCheckoutOption) -> ErrorList:
        ...
    def CheckoutWorkset(self) -> ErrorList:
        ...
    def CheckinWorkset(self) -> ErrorList:
        ...
    def CheckoutAllModifiedObjects(self, checkedOutObjects: typing.List[NXObject]) -> ErrorList:
        ...
    def GetCheckedoutStatusOfObjects(self, checkedOutObjects: typing.List[NXObject], uncheckedOutObjects: typing.List[NXObject]) -> None:
        ...
    def ReorderComponents(self, order: Assemblies.ComponentOrder, componentsToReorder: typing.List[Assemblies.Component], targetComponent: Assemblies.Component, beforeOrAfter: Assemblies.ComponentAssembly.OrderTargetLocation) -> None:
        ...
    def ReorderChildrenOfParent(self, order: Assemblies.ComponentOrder, parentComponent: Assemblies.Component, componentsToReorder: typing.List[Assemblies.Component]) -> None:
        ...
    def GetComponentOrders(self, orders: typing.List[Assemblies.ComponentOrder]) -> None:
        ...
    def MoveToPendingComponent(self, component: NXObject) -> None:
        ...
    def GetActiveOrder(self) -> Assemblies.Order:
        ...
    def CreateIsolateViewWithComponents(self, components: typing.List[Assemblies.Component], view: View) -> ErrorList:
        ...
    def ShowComponentsInIsolateView(self, components: typing.List[Assemblies.Component], view: View) -> ErrorList:
        ...
    def HideComponentsInIsolateView(self, components: typing.List[Assemblies.Component], view: View) -> ErrorList:
        ...
    Arrangements: Assemblies.ArrangementCollection
    Explosions: Assemblies.ExplosionCollection
    DrawingExplosions: Assemblies.DrawingExplosionCollection
    ComponentPatterns: Assemblies.ComponentPatternCollection
    Subsets: Assemblies.SubsetCollection
    ClearanceSets: Assemblies.ClearanceSetCollection
    OrdersSet: Assemblies.OrderCollection
    ActiveArrangement: Assemblies.Arrangement
    Positioner: Positioning.ComponentPositioner
    RootComponent: Assemblies.Component


    class SuppressedState(enum.Enum):
        Inherit = 0
        Suppressed = 1
        Unsuppressed = 2
        SuppressedByExp = 3
        UnsuppressedByExp = 4
    

    class SubstitutionMode(enum.Enum):
        NonAssociative = 0
        SingleComponent = 1
        All = 2
    

    class OrderTargetLocation(enum.Enum):
        PlaceBefore = 0
        PlaceAfter = 1
    

    class OpenOption(enum.Enum):
        ComponentOnly = 0
        ImmediateChildren = 1
        WholeAssembly = 2
        ReapplyRevRule = 3
    

    class OpenComponentStatus(enum.Enum):
        SuccessfullyOpened = 0
        DeletedByOpen = 1
        CouldNotOpen = 2
    

    class CloseModified(enum.Enum):
        False = 0
        True = 1
    

    class CheckinCheckoutOption(enum.Enum):
        DesignElement = 0
        SourceItem = 1
        Both = 2
        Default = 3
    

class Component(DisplayableObject):
    def __init__(self) -> None: ...
    def GetChildren(self) -> typing.List[Assemblies.Component]:
        ...
    def FindOccurrence(self, proto: NXObject) -> NXObject:
        ...
    def GetLayerOption(self) -> int:
        ...
    def SetLayerOption(self, layer: int) -> None:
        ...
    def GetPosition(self, position: Point3d, orientation: Matrix3x3) -> None:
        ...
    def EstablishPositionOverride(self, parent: Assemblies.Component) -> None:
        ...
    def EstablishIsolatedPositionOverride(self, parent: Assemblies.Component, arrangement: Assemblies.Arrangement) -> None:
        ...
    def SetPositioningIsolated(self, arrangement: Assemblies.Arrangement) -> None:
        ...
    def IsPositioningIsolated(self, arrangement: Assemblies.Arrangement) -> bool:
        ...
    def RemovePositionOverride(self, parent: Assemblies.Component) -> None:
        ...
    def GetPositionOverrideParent(self) -> Assemblies.Component:
        ...
    def GetPositionOverrideType(self) -> Assemblies.PositionOverrideType:
        ...
    def GetArrangements(self, arrangements: typing.List[Assemblies.Arrangement]) -> None:
        ...
    def SetUsedArrangement(self, newArrangement: Assemblies.Arrangement) -> None:
        ...
    def SetPositioningVaried(self, components: typing.List[Assemblies.Component], setAsVaried: bool) -> None:
        ...
    def Suppress(self) -> None:
        ...
    def Suppress(self, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def Unsuppress(self) -> None:
        ...
    def Unsuppress(self, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def UpdateStructure(self, components: typing.List[Assemblies.Component], nLevels: int) -> None:
        ...
    def UpdateStructure(self, components: typing.List[Assemblies.Component], nLevels: int, checkComponentsVisited: bool) -> None:
        ...
    def GetConstraints(self) -> typing.List[Positioning.ComponentConstraint]:
        ...
    def GetDegreesOfFreedom(self) -> Assemblies.DegreesOfFreedom:
        ...
    def GetDegreesOfFreedom(self, components: typing.List[Assemblies.Component]) -> Assemblies.DegreesOfFreedom:
        ...
    def RecallConstraints(self) -> None:
        ...
    def RecallAndListConstraints(self) -> typing.List[Positioning.ComponentConstraint]:
        ...
    def RemoveRememberedConstraints(self) -> None:
        ...
    def GetNonGeometricState(self) -> bool:
        ...
    def GetComponentQuantityType(self) -> Assemblies.ComponentQuantity:
        ...
    def GetIntegerQuantity(self) -> int:
        ...
    def GetRealQuantity(self, quantityUnits: str) -> float:
        ...
    def GetAsRequiredQuantity(self) -> str:
        ...
    def DisplayComponentsLightweight(self, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def DisplayComponentsExact(self, components: typing.List[Assemblies.Component]) -> ErrorList:
        ...
    def GetComponentRepresentationMode(self) -> Assemblies.Component.RepresentationMode:
        ...
    def SetInstanceUserAttribute(self, info: NXObject.AttributeInformation, option: Update.Option) -> None:
        ...
    def SetInstanceUserAttribute(self, title: str, index: int, value: int, option: Update.Option) -> None:
        ...
    def SetInstanceUserAttribute(self, title: str, index: int, value: float, option: Update.Option) -> None:
        ...
    def SetInstanceUserAttribute(self, title: str, index: int, value: str, option: Update.Option) -> None:
        ...
    def SetInstanceUserAttribute(self, title: str, index: int, option: Update.Option) -> None:
        ...
    def SetInstanceTimeUserAttribute(self, title: str, index: int, value: str, option: Update.Option) -> None:
        ...
    def SetInstanceBooleanUserAttribute(self, title: str, index: int, value: bool, option: Update.Option) -> None:
        ...
    def HasInstanceUserAttribute(self, title: str, type: NXObject.AttributeType, index: int) -> bool:
        ...
    def GetInstanceUserAttribute(self, title: str, type: NXObject.AttributeType, index: int) -> NXObject.AttributeInformation:
        ...
    def GetInstanceBooleanUserAttribute(self, title: str, index: int) -> bool:
        ...
    def GetInstanceIntegerUserAttribute(self, title: str, index: int) -> int:
        ...
    def GetInstanceRealUserAttribute(self, title: str, index: int) -> float:
        ...
    def GetInstanceStringUserAttribute(self, title: str, index: int) -> str:
        ...
    def GetInstanceTimeUserAttribute(self, title: str, index: int) -> str:
        ...
    def GetInstanceUserAttributes(self) -> typing.List[NXObject.AttributeInformation]:
        ...
    def GetInstanceUserAttributes(self, includeUnset: bool) -> typing.List[NXObject.AttributeInformation]:
        ...
    def GetInstanceUserAttributeAsString(self, title: str, type: NXObject.AttributeType, index: int) -> str:
        ...
    def GetInstanceUserAttributesAsStrings(self) -> str:
        ...
    def DeleteInstanceUserAttribute(self, type: NXObject.AttributeType, title: str, deleteEntireArray: bool, option: Update.Option) -> None:
        ...
    def DeleteInstanceUserAttributes(self, type: NXObject.AttributeType, option: Update.Option) -> None:
        ...
    def SetInstanceUserAttributeLock(self, title: str, type: NXObject.AttributeType, lock: bool) -> None:
        ...
    def GetInstanceUserAttributeLock(self, title: str, type: NXObject.AttributeType) -> bool:
        ...
    def CreateEmptyPartFamilyInstanceSelectionCriteria(self, family: PartFamily.Template) -> PartFamily.InstanceSelectionCriteria:
        ...
    def GetPartFamilyInstanceSelectionCriteria(self) -> PartFamily.InstanceSelectionCriteria:
        ...
    def SetPartFamilyInstanceSelectionCriteria(self, selectionCriteria: PartFamily.InstanceSelectionCriteria) -> None:
        ...
    def DeletePartFamilyInstanceSelectionCriteria(self) -> None:
        ...
    def FindComponentPatterns(self, patternDefinition: Assemblies.ComponentPattern, patternDefinitions: typing.List[Assemblies.ComponentPattern]) -> None:
        ...
    def GetCharacteristics(self) -> Routing.CharacteristicList:
        ...
    def SetCharacteristics(self, values: Routing.CharacteristicList) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Routing.ICharacteristic.SetCharacteristics2 instead.")"""
        ...
    def GetIntegerCharacteristic(self, name: str) -> int:
        ...
    def SetCharacteristic(self, name: str, value: int) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Routing.ICharacteristic.SetCharacteristic2 instead.")"""
        ...
    def GetRealCharacteristic(self, name: str) -> float:
        ...
    def SetCharacteristic(self, name: str, value: float) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Routing.ICharacteristic.SetCharacteristic2 instead.")"""
        ...
    def GetStringCharacteristic(self, name: str) -> str:
        ...
    def SetCharacteristic(self, name: str, value: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Routing.ICharacteristic.SetCharacteristic2 instead.")"""
        ...
    def DeleteCharacterstics(self, values: Routing.CharacteristicList) -> None:
        ...
    def GetDestinationCharacteristics(self) -> Routing.CharacteristicList:
        ...
    def SetCharacteristic2(self, title: str, value: int) -> None:
        ...
    def SetCharacteristic2(self, title: str, value: float) -> None:
        ...
    def SetCharacteristic2(self, title: str, value: str) -> None:
        ...
    def SetCharacteristics2(self, values: Routing.CharacteristicList) -> None:
        ...
    CollaborativeContentType: Assemblies.CollaborativeContentType
    DesignElementRevision: PDM.DesignElementRevision
    DesignSubordinateRevision: PDM.DesignSubordinateRevision
    DirectOwner: Assemblies.ComponentAssembly
    DisplayName: str
    EmptyPartRefsetName: str
    EntirePartRefsetName: str
    FixConstraint: Positioning.ComponentConstraint
    IsFixed: bool
    IsSuppressed: bool
    ModelElementRevision: PDM.ModelElementRevision
    Parent: Assemblies.Component
    ReferenceSet: str
    Subset: Assemblies.Subset
    SuppressingArrangement: Assemblies.Arrangement
    UsedArrangement: Assemblies.Arrangement


    class RepresentationMode(enum.Enum):
        Lightweight = 0
        Partial = 1
        Exact = 2
        None = 3
    

class CollaborativeContentType(enum.Enum):
    Workset = 0
    Subset = 1
    ShapeDesignElement = 2
    ReuseDesignElement = 3
    PromissoryDesignElement = 4
    Subordinate = 5
    DesignFeature = 6
    DesignControlElement = 7
    NotAssigned = 8


class ClearanceSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.ClearanceSet]:
        ...
    def __init__(self, owner: Assemblies.ComponentAssembly) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Assemblies.ClearanceSet:
        ...
    def CountClearanceSets(self) -> int:
        ...
    def DeleteAllAnalysisData(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class ClearanceSet(NXObject):
    def __init__(self) -> None: ...
    def PerformAnalysis(self, reanalyzeOption: Assemblies.ClearanceSet.ReanalyzeOutOfDateExcludedPairs) -> None:
        ...
    def ReanalyzePairs(self, firstObjects: typing.List[DisplayableObject], secondObjects: typing.List[DisplayableObject], calculationMethod: Assemblies.ClearanceSet.ReanalyzePairCalculationMethod) -> None:
        ...
    def CreateInterferenceGeometry(self, firstObjects: typing.List[DisplayableObject], secondObjects: typing.List[DisplayableObject]) -> None:
        ...
    def CalculatePenetrationDepth(self, firstObjects: typing.List[DisplayableObject], secondObjects: typing.List[DisplayableObject]) -> None:
        ...
    def Delete(self) -> None:
        ...
    def GetVersion(self) -> int:
        ...
    def GetInterferenceData(self, object1: DisplayableObject, object2: DisplayableObject, type: Assemblies.ClearanceSet.InterferenceType, newInterference: bool, interfBodies: typing.List[DisplayableObject], point1: Point3d, point2: Point3d, text: str, interfNum: int, config: int, depthResult: int, depth: float, direction: Vector3d, minPoint: Point3d, maxPoint: Point3d) -> None:
        ...
    def GetResults(self) -> Assemblies.ClearanceSet.Summary:
        ...
    def GetNumberOfInterferences(self) -> int:
        ...
    def DeleteInterference(self, object1: DisplayableObject, object2: DisplayableObject) -> None:
        ...
    def GetIsPairChanged(self, object1: DisplayableObject, object2: DisplayableObject) -> bool:
        ...
    def GetNextInterference(self, object1: DisplayableObject, object2: DisplayableObject, nextObject1: DisplayableObject, nextObject2: DisplayableObject) -> None:
        ...
    def Copy(self, name: str, mode: Assemblies.ClearanceSet.CopyMode) -> Assemblies.ClearanceSet:
        ...
    def SetInterferenceText(self, object1: DisplayableObject, object2: DisplayableObject, text: str) -> None:
        ...
    def DetectObsoleteSettings(self, doCleanupNow: bool) -> bool:
        """public bool DetectObsoleteSettings(bool doCleanupNow)"""
        ...


    class ClearanceSetSummary():
        StartTime: int
        EndTime: int
        RunTime: int
        Version: int
        AnalysisMode: Assemblies.ClearanceAnalysisBuilder.CalculationMethodType
        NumCollections: int
        NumCollection1: int
        NumCollection2: int
        NumPairs: int
        NumExcludedPairs: int
        NumChangedPairs: int
        NumChangedObjs: int
        NumCheckedPairs: int
        NumNewHard: int
        NumNewSoft: int
        NumNewTouching: int
        NumNewContainment: int
        NumNewAllInterf: int
        NumHard: int
        NumSoft: int
        NumTouching: int
        NumContainment: int
        NumAllInterf: int
        JobStatus: Assemblies.ClearanceSet.JobStatus
        NumZones: int
        def ToString(self) -> str:
            ...
    

    class ReanalyzePairCalculationMethod(enum.Enum):
        UseStoredMethod = 0
        Lightweight = 1
        ExactIfLoaded = 2
        Exact = 3
    

    class ReanalyzeOutOfDateExcludedPairs(enum.Enum):
        CustomerDefault = 0
        True = 1
        False = 2
    

    class PenetrationDepthResult(enum.Enum):
        NotAttempted = 0
        Success = 1
        NoClash = 2
        Touching = 3
        BothSheets = 4
        UnspecifiedError = 5
    

    class JobStatus(enum.Enum):
        NotAborted = 0
        AbortedByUser = 1
        AbortedOnError = 2
    

    class InterferenceType(enum.Enum):
        Soft = 0
        Touch = 1
        Hard = 2
        Cont1In2 = 3
        Cont2In1 = 4
        NoInterference = 5
    

    class CopyMode(enum.Enum):
        NoResults = 0
        Results = 1
        InterfBodies = 2
    

    class ZoneType(enum.Enum):
        Object = 0
        Pair = 1
    

class ClearanceAnalysisBuilder(Builder):
    def __init__(self) -> None: ...
    def AddException(self, isExclude: bool, comp1: DisplayableObject, comp2: DisplayableObject, text: str) -> None:
        ...
    def DeleteException(self, comp1: DisplayableObject, comp2: DisplayableObject) -> None:
        ...
    def CreateClearanceZoneExpression(self, rhsExpression: str) -> Expression:
        ...
    def SetDefaultClearanceZone(self, expression: Expression) -> None:
        ...
    def GetDefaultClearanceZone(self) -> Expression:
        ...
    def AddPairClearanceZone(self, object1: DisplayableObject, object2: DisplayableObject, expression: Expression) -> None:
        ...
    def GetPairClearanceZone(self, object1: DisplayableObject, object2: DisplayableObject, expression: Expression) -> Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource:
        ...
    def DeletePairClearanceZone(self, object1: DisplayableObject, object2: DisplayableObject) -> None:
        ...
    def GetIsPairIncluded(self, object1: DisplayableObject, object2: DisplayableObject, reason: Assemblies.ClearanceAnalysisBuilder.PairExcludedReason, text: str) -> bool:
        ...
    def AddObjectClearanceZone(self, object: DisplayableObject, expression: Expression) -> None:
        ...
    def GetObjectClearanceZone(self, object: DisplayableObject, expression: Expression) -> Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource:
        ...
    def DeleteObjectClearanceZone(self, object: DisplayableObject) -> None:
        ...
    CalculationMethod: Assemblies.ClearanceAnalysisBuilder.CalculationMethodType
    ClearanceBetween: Assemblies.ClearanceAnalysisBuilder.ClearanceBetweenEntity
    ClearanceSetName: str
    CollectionOneObjects: SelectDisplayableObjectList
    CollectionOneRange: Assemblies.ClearanceAnalysisBuilder.CollectionRange
    CollectionTwoObjects: SelectDisplayableObjectList
    CollectionTwoRange: Assemblies.ClearanceAnalysisBuilder.CollectionRange
    InterferenceColor: NXColor
    IsCalculatePenetrationDepth: bool
    IsIgnorePairsWithinSameGroup: bool
    IsIgnorePairsWithinSamePart: bool
    IsIgnorePairsWithinSameSubassembly: bool
    IsIgnorePairsWithinSelectedSubassemblies: bool
    Layer: int
    SaveInterferenceGeometry: bool
    TotalCollectionCount: Assemblies.ClearanceAnalysisBuilder.NumberOfCollections
    UnitSubassemblies: SelectDisplayableObjectList


    class PairExcludedReason(enum.Enum):
        NoReason = 0
        UserDefined = 1
        SameCompRule = 2
        SameGroupRule = 3
        MatedCompRule = 4
        SamePartRule = 5
        CompSuppressed = 6
        NonGeom = 7
        UnitSubassy = 8
    

    class NumberOfCollections(enum.Enum):
        One = 0
        Two = 1
    

    class CollectionRange(enum.Enum):
        AllObjects = 0
        AllVisibleObjects = 1
        SelectedObjects = 2
        AllButSelectedObjects = 3
    

    class ClearanceZoneSource(enum.Enum):
        Pair = 0
        Object1 = 1
        Object2 = 2
        Default = 3
        Defined = 4
    

    class ClearanceBetweenEntity(enum.Enum):
        Components = 0
        Bodies = 1
    

    class CalculationMethodType(enum.Enum):
        Lightweight = 0
        ExactifLoaded = 1
        Exact = 2
    

class BoxSearchTermBuilder(Assemblies.SearchTermBuilder):
    def __init__(self) -> None: ...
    BottomCorner: Point3d
    BoxOverlapLogic: Assemblies.BoxSearchTerm.BoxOverlapLogicType
    SearchTermLogic: Assemblies.SearchTerm.SearchTermLogicType
    TopCorner: Point3d
    TrueShapeRefinement: bool


class BoxSearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...


    class BoxOverlapLogicType(enum.Enum):
        Inside = 0
        Outside = 1
        Intersects = 2
        InsideOrIntersects = 3
        OutsideOrIntersects = 4
    

class AttributeSearchTermBuilder(Assemblies.SearchTermBuilder):
    def __init__(self) -> None: ...
    def GetCriteria(self, titles: str, values: str) -> None:
        ...
    def SetCriteria(self, titles: str, values: str) -> None:
        ...
    QueryName: str
    SearchTermLogic: Assemblies.SearchTerm.SearchTermLogicType


class AttributeSearchTerm(Assemblies.SearchTerm):
    def __init__(self) -> None: ...


class AssemblyManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateHideComponentBuilder(self) -> Assemblies.HideComponentBuilder:
        ...
    def CreateShowComponentBuilder(self) -> Assemblies.ShowComponentBuilder:
        ...
    def CreateUpdateStructureBuilder(self) -> Assemblies.UpdateStructureBuilder:
        ...
    def CreateReplaceComponentBuilder(self) -> Assemblies.ReplaceComponentBuilder:
        ...
    def CreateLoadInterpartDataBuilder(self) -> Assemblies.LoadInterpartDataBuilder:
        ...
    def CreateNewComponentBuilder(self) -> Assemblies.CreateNewComponentBuilder:
        ...
    def CreateConstraintDisplayBuilder(self) -> Assemblies.ConstraintDisplayBuilder:
        ...
    def CreateMakeUniquePartBuilder(self) -> Assemblies.MakeUniquePartBuilder:
        ...
    def CreateClearanceAnalysisBuilder(self, clearanceSet: Assemblies.ClearanceSet) -> Assemblies.ClearanceAnalysisBuilder:
        ...
    def CreateAddComponentBuilder(self) -> Assemblies.AddComponentBuilder:
        ...
    def CreateCreateComponentBuilder(self) -> Assemblies.CreateComponentBuilder:
        ...
    def Tag(self) -> Tag: ...



class Assembly(NXObject):
    def __init__(self) -> None: ...


class AssembliesParameterPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    Arrangements: Assemblies.AssembliesParameterPropertiesBuilder.ArrangementOptions
    SelectedObjects: Assemblies.SelectComponentList


    class ArrangementOptions(enum.Enum):
        IndividuallyPositioned = 0
        SamePositionInAll = 1
        Mixed = 2
    

class AssembliesGeneralPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    def SynchronizeLayers(self) -> None:
        ...
    def SynchronizeDisplay(self) -> None:
        ...
    def SynchronizeAttributes(self) -> None:
        ...
    Hidden: Assemblies.AssembliesGeneralPropertiesBuilder.HiddenOptions
    IntegerQuantity: int
    Layer: int
    LayerOption: Assemblies.AssembliesGeneralPropertiesBuilder.LayerOptions
    NonGeometric: bool
    QuantityType: Assemblies.AssembliesGeneralPropertiesBuilder.QuantityOptions
    RealQuantity: float
    ReferenceComponent: Assemblies.AssembliesGeneralPropertiesBuilder.ReferenceComponentOptions
    SelectedObjects: Assemblies.SelectComponentList
    SpecificColor: bool
    SpecificPartialShade: bool
    SpecificTranslucency: bool


    class ReferenceComponentOptions(enum.Enum):
        No = 0
        Yes = 1
        Mixed = 2
    

    class QuantityOptions(enum.Enum):
        Number = 0
        AsRequired = 1
    

    class LayerOptions(enum.Enum):
        OriginalLayer = 0
        SpecifiedLayer = 1
        Mixed = 2
    

    class HiddenOptions(enum.Enum):
        No = 0
        Yes = 1
        Mixed = 2
    

class AssembliesEventTypes(enum.Enum):
    BrowserUpdate = 0
    DeselectAll = 1
    PartSelectAll = 2
    PartDeselectAll = 3
    PartSelect = 4
    PartDeselect = 5
    PartFullyLoad = 6
    PartMakeDisplayed = 7
    PartMakeWork = 8
    LinkedObjectSelectAll = 9
    LinkedObjectDeselectAll = 10
    LinkedObjectSelect = 11
    LinkedObjectDeselect = 12
    LinkedFeatureEdit = 13
    LinkedFeatureBreak = 14
    LinkedFeatureAcceptBroken = 15
    Launch = 16
    Exit = 17


class AssembliesChildRevisionOptions(enum.Enum):
    AllRevisions = 0
    UseRevRule = 1
    LatestRevisionWithRelation = 2


class ArrangementsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    InheritArrangementFromParent: bool
    SelectedArrangement: Assemblies.Arrangement


class ArrangementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Assemblies.Arrangement]:
        ...
    def __init__(self, owner: Assemblies.ComponentAssembly) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, templateArrangement: Assemblies.Arrangement, name: str) -> Assemblies.Arrangement:
        ...
    def CreateIsolated(self, templateArrangement: Assemblies.Arrangement, name: str) -> Assemblies.Arrangement:
        ...
    def FindObject(self, journalIdentifier: str) -> Assemblies.Arrangement:
        ...
    def Tag(self) -> Tag: ...



class Arrangement(NXObject):
    def __init__(self) -> None: ...
    def Delete(self, forgetPositioning: bool) -> None:
        ...
    def GetMaintainsConstraints(self) -> bool:
        ...
    def GetHasPostponedConstraints(self) -> bool:
        ...
    def SolvePostponedConstraints(self) -> None:
        ...
    def IsIsolated(self) -> bool:
        ...
    IgnoringConstraints: bool
    Owner: Assemblies.ComponentAssembly


class AddComponentBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPartsToAdd(self, partsToUse: typing.List[BasePart]) -> None:
        ...
    def SetPartsToAdd(self, partsToUse: typing.List[BasePart]) -> None:
        ...
    def RemoveAddedComponents(self) -> None:
        ...
    def GetCount(self) -> int:
        ...
    def SetCount(self, count: int) -> None:
        ...
    def GetInitialLocationType(self) -> Assemblies.AddComponentBuilder.LocationType:
        ...
    def SetInitialLocationType(self, locationType: Assemblies.AddComponentBuilder.LocationType) -> None:
        ...
    def GetInitialLocationAndOrientation(self, initialLocation: Point, initialOrientation: CoordinateSystem) -> None:
        ...
    def SetInitialLocationAndOrientation(self, initialLocation: Point, initialOrientation: CoordinateSystem) -> None:
        ...
    def SetInitialLocationAndOrientation(self, point: Point3d, orientation: Matrix3x3) -> None:
        ...
    def GetScatterOption(self) -> bool:
        ...
    def SetScatterOption(self, scatterOption: bool) -> None:
        ...
    def GetKeepConstraintsOption(self) -> bool:
        ...
    def SetKeepConstraintsOption(self, keepConstraintsOption: bool) -> None:
        ...
    def GetComponentAnchor(self) -> Assemblies.ProductInterface.InterfaceObject:
        ...
    def SetComponentAnchor(self, componentAnchor: Assemblies.ProductInterface.InterfaceObject) -> None:
        ...
    def GetAllProductInterfaceObjects(self, productInterfaceObjects: typing.List[Assemblies.ProductInterface.InterfaceObject]) -> None:
        ...
    def GetLogicalObjects(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self, logicalObjects: typing.List[PDM.LogicalObject]) -> None:
        ...
    def GetOperationFailures(self) -> ErrorList:
        ...
    def ResetToSnapped(self) -> None:
        ...
    def OrientToWCS(self) -> None:
        ...
    def ReverseZDirection(self) -> None:
        ...
    def RotateAlongZDirection(self) -> None:
        ...
    def SetSynchDisplayProperties(self, synchDisplayProperties: bool) -> None:
        ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...
    ComponentName: str
    DesignElementType: str
    FileNewDescriptor: FileNew
    Layer: int
    ReferenceSet: str


    class LocationType(enum.Enum):
        Snap = 0
        WorkPartAbsolute = 1
        DisplayedPartAbsolute = 2
        DisplayedPartWCS = 3
    

class AbsolutePositionBuilder(Builder):
    def __init__(self) -> None: ...
    AbsolutelyPosition: bool
    ObjectsToAbsolutePosition: SelectDisplayableObjectList


