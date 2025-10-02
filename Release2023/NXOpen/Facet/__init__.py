from ...NXOpen import *
from ..Facet import *

import typing
import enum

class WrapMeshBuilder(Builder):
    def __init__(self) -> None: ...
    AngleThreshold: float
    AverageSize: Expression
    ChordalTolerance: float
    GapFaces: ScCollector
    InputBodyCollector: ScCollector
    InputBodyOption: Facet.WrapMeshBuilder.KeepInputBodyType
    IntendedGapSize: Expression
    KeepSharpEdges: bool
    MaxGapSize: Expression
    MaximumSize: Expression
    Method: Facet.WrapMeshBuilder.MethodType
    SeedPoint: SelectDisplayableObjectList
    WrapMeshMode: Facet.WrapMeshBuilder.WrapMeshModeType


    class WrapMeshModeType(enum.Enum):
        Constant = 0
        Variable = 1
    

    class MethodType(enum.Enum):
        External = 0
        LargestInternal = 1
        InternalBySeedPoint = 2
    

    class KeepInputBodyType(enum.Enum):
        Keep = 0
        Hide = 1
    

class SubdivideFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    AngleThreshold: float
    Bodies: SelectDisplayableObjectList
    EdgeLength: float
    FacetBodies: Facet.SelectFacetedBodyList
    FacetCollector: FacetCollector
    InterpolationMethod: Facet.SubdivideFacetBodyBuilder.InterpolationMethodType
    IsEditCopy: bool
    IsOptimize: bool
    RegionList: GeometricUtilities.BoundaryDefinitionBuilderList
    SubdivisionMethod: Facet.SubdivideFacetBodyBuilder.SubdivisionMethodType


    class SubdivisionMethodType(enum.Enum):
        SubdivideIntoFour = 0
        SubdividebyEdgeLength = 1
    

    class InterpolationMethodType(enum.Enum):
        Linear = 0
        Cubic = 1
    

class STLImportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTopology(self) -> typing.List[Part]:
        ...
    AngularTolerance: Facet.STLImportBuilder.AngularToleranceTypes
    CleanUp: bool
    FacetBodyType: Facet.STLImportBuilder.FacetBodyTypes
    File: str
    HideSmoothEdges: bool
    MinimumAngleFoldedFacets: float
    MinimumFacetNumber: int
    STLFileUnits: Facet.STLImportBuilder.STLFileUnitsTypes
    ShowInformationWindow: bool


    class STLFileUnitsTypes(enum.Enum):
        Meters = 0
        Millimeters = 1
        Inches = 2
    

    class FacetBodyTypes(enum.Enum):
        Psm = 0
        Nx = 1
        Jt = 2
    

    class AngularToleranceTypes(enum.Enum):
        Coarse = 0
        Medium = 1
        Fine = 2
    

class SplitCurveMethodListDataManager(TaggedObject):
    def __init__(self) -> None: ...
    SplitCurveMethodList: TaggedObjectList


class SplitCurveMethodBuilder(Builder):
    def __init__(self) -> None: ...
    def AddCurveOnBodies(self, bodyArray: typing.List[Body]) -> None:
        ...
    def CreateSplitCurveWithUseExisting(self) -> typing.List[Spline]:
        ...
    ExistingCurves: Section
    ProjectDirection: GeometricUtilities.ProjectionOptions


    class ProjectOption(enum.Enum):
        NormalToFace = 0
        AlongVector = 1
    

class SnipFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    def SwitchRegion(self) -> None:
        ...
    AlongDirection: Facet.SnipFacetBodyBuilder.DirectionType
    AutomaticFillType: Facet.SnipFacetBodyBuilder.AutomaticFillTypes
    Bodies: SelectDisplayableObjectList
    BoundaryFacetTreatmentType: Facet.SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod
    CanDivide: bool
    FacetBodies: Facet.SelectFacetedBodyList
    FacetCollector: FacetCollector
    IsEditCopy: bool
    IsSnipNearFacets: bool
    Plane: Plane
    ProfileList: SectionList
    ProjectionVector: Direction
    RegionList: GeometricUtilities.BoundaryDefinitionBuilderList
    RegionPoint: SelectPointList
    RegionsOption: Facet.SnipFacetBodyBuilder.RegionsOptionType
    Type: Facet.SnipFacetBodyBuilder.Types
    ViewDirection: Vector3d


    class Types(enum.Enum):
        SnipByBoundary = 0
        SnipByRegion = 1
        SnipWithCurves = 2
        SnipAtPlane = 3
    

    class RegionsOptionType(enum.Enum):
        RemoveSelected = 0
        KeepSelected = 1
        Divide = 2
    

    class DirectionType(enum.Enum):
        ViewDirection = 0
        FacetNormal = 1
        AlongVector = 2
    

    class BoundaryFacetTreatmentMethod(enum.Enum):
        SnipFacets = 0
        RemoveFacets = 1
    

    class AutomaticFillTypes(enum.Enum):
        None = 0
        Linear = 1
        Refined = 2
        TangentBased = 3
        CurvatureBased = 4
    

class SmoothFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    Bodies: SelectDisplayableObjectList
    FaceEdge: SelectNXObjectList
    FacetBodies: Facet.SelectFacetedBodyList
    FacetCollector: FacetCollector
    IsEditCopy: bool
    IsLockBoundary: bool
    IsSmoothOverEdges: bool
    ModifyPercent: int
    NumberOfIterations: int
    RegionList: GeometricUtilities.BoundaryDefinitionBuilderList
    SmoothFactor: int
    Type: Facet.SmoothFacetBodyBuilder.Types


    class Types(enum.Enum):
        Mesh = 0
        Edge = 1
    

class SewFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    def FlipRange(self) -> None:
        ...
    DeformBody: Facet.SelectFacetedBody
    DeformDistance: Expression
    DistanceTolerance: float
    InputStatus: Facet.SewFacetBodyBuilder.Input
    TargetBody: Facet.SelectFacetedBody
    Vertex1: Point
    Vertex2: Point


    class VertexIndex(enum.Enum):
        First = 0
        Second = 1
    

    class Input(enum.Enum):
        Keep = 0
        Delete = 1
        Hide = 2
    

class SelectFacetedBodyList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Facet.FacetedBody) -> bool:
        ...
    def Add(self, objects: typing.List[Facet.FacetedBody]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Facet.FacetedBody, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Facet.FacetedBody) -> bool:
        ...
    def Remove(self, object: Facet.FacetedBody, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Facet.FacetedBody, view1: View, point1: Point3d, selection2: Facet.FacetedBody, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Facet.FacetedBody]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Facet.FacetedBody) -> bool:
        ...
    def SetArray(self, objects: typing.List[Facet.FacetedBody]) -> None:
        ...
    def GetArray(self) -> typing.List[Facet.FacetedBody]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Facet.FacetedBody, view1: View, point1: Point3d, selection2: Facet.FacetedBody, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Facet.FacetedBody, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectFacetedBody(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Facet.FacetedBody, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Facet.FacetedBody, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Facet.FacetedBody, view1: View, point1: Point3d, selection2: Facet.FacetedBody, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Facet.FacetedBody, view1: View, point1: Point3d, selection2: Facet.FacetedBody, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Facet.FacetedBody, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Facet.FacetedBody:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Facet.FacetedBody


class ReplaceMeshWithFaceBuilder(Builder):
    def __init__(self) -> None: ...
    ConeAverageConstrainToDirectionToggle: bool
    ConeAverageConstrainToDirectionVector: Direction
    ConeColinearConstraintAxis: Axis
    ConeConstraintTypes: Facet.ReplaceMeshWithFaceBuilder.ConeConstraint
    ConeHalfAngle: Expression
    ConeParallelConstraintVector: Direction
    CylinderAverageConstrainToDirectionToggle: bool
    CylinderAverageConstrainToDirectionVector: Direction
    CylinderColinearConstraintAxis: Axis
    CylinderConstraintTypes: Facet.ReplaceMeshWithFaceBuilder.CylinderConstraint
    CylinderOrSphereRadius: Expression
    CylinderParallelConstraintVector: Direction
    FacetCollector: FacetCollector
    HalfAngleToggle: bool
    MaxDeviation: Expression
    MinimumFacetNumber: int
    OrthogonalOrCoplanarConstraintPlane: Plane
    PlaneAverageConstrainToNormalToggle: bool
    PlaneAverageConstrainToNormalVector: Direction
    PlaneConstraintTypes: Facet.ReplaceMeshWithFaceBuilder.PlaneConstraint
    PlaneParallelConstraintNormal: Direction
    RadiusToggle: bool
    ReplaceMeshOn: Facet.ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption
    SphereConcentricConstraintPoint: Point
    SphereConstraintTypes: Facet.ReplaceMeshWithFaceBuilder.SphereConstraint
    Type: Facet.ReplaceMeshWithFaceBuilder.Types


    class Types(enum.Enum):
        Plane = 0
        Cylinder = 1
        Cone = 2
        Sphere = 3
    

    class SphereConstraint(enum.Enum):
        None = 0
        Concentric = 1
        AverageConcentric = 2
    

    class ReplaceMeshOnOption(enum.Enum):
        OriginalBody = 0
        NewBody = 1
    

    class PlaneConstraint(enum.Enum):
        None = 0
        Orthogonal = 1
        Parallel = 2
        Coplanar = 3
        AverageParallel = 4
        AverageCoplanar = 5
    

    class CylinderConstraint(enum.Enum):
        None = 0
        Parallel = 1
        Colinear = 2
        AverageParallel = 3
        AverageColinear = 4
    

    class ConeConstraint(enum.Enum):
        None = 0
        Parallel = 1
        Colinear = 2
        AverageParallel = 3
        AverageColinear = 4
    

class RemoveUndercutsBuilder(Builder):
    def __init__(self) -> None: ...
    def GenerateIsoclines(self) -> None:
        ...
    DraftAngle: Expression
    DrawDirection: Direction
    FacetBody: SelectDisplayableObject
    IsEditCopy: bool
    MatchFace: bool
    PartingObject: SelectDisplayableObject
    SelectedCurve: ScCollector


class RemeshFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    AngularThreshold: float
    AverageSize: Expression
    ChordalTolerance: float
    FacetRegion: FacetCollector
    IsEditCopy: bool
    IsLockBoundary: bool
    IsShowDeviationPlot: bool
    MaximumSize: Expression
    RemeshMode: Facet.RemeshFacetBodyBuilder.RemeshModeType
    SharpEdgesLockOption: Facet.RemeshFacetBodyBuilder.SharpEdgesLockType


    class SharpEdgesLockType(enum.Enum):
        NoLock = 0
        SoftLock = 1
        HardLock = 2
    

    class RemeshModeType(enum.Enum):
        Constant = 0
        Variable = 1
    

class PolygonModelingBuilder(Builder):
    def __init__(self) -> None: ...
    def RemoveParameterOfBody(self, bodyTag: Body) -> None:
        ...
    def MergeAllFaces(self, bodyTag: Body) -> None:
        ...
    ConvertType: Facet.PolygonModelingBuilder.ConvertTypes
    EditCopy: bool
    SelectFacetBodies: SelectNXObjectList


    class ConvertTypes(enum.Enum):
        Convergent = 0
        Facet = 1
    

class PlugLeakageBuilder(Builder):
    def __init__(self) -> None: ...
    def FindPath(self) -> None:
        ...
    def CreatePatch(self) -> None:
        ...
    HoleMinimumSize: Expression
    InnerPoint: Point3d
    InputBodyCollector: ScCollector
    OuterPoint: Point3d
    RegionList: GeometricUtilities.BoundaryDefinitionBuilderList


class PaintFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPaintBrushColor(self) -> float:
        ...
    def SetPaintBrushColor(self, paintBrushColor: float) -> None:
        ...
    def SetupBodyColorData(self, bodies: typing.List[DisplayableObject]) -> None:
        ...
    def SetupColorData(self, facets: typing.List[Facet.FacetedBody]) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Facet.PaintFacetBodyBuilder.SetupBodyColorData instead.")"""
        ...
    def PaintBodiesBackgroundColor(self, bodies: typing.List[DisplayableObject]) -> None:
        ...
    def PaintFacetsBackGroundColor(self, facets: typing.List[Facet.FacetedBody]) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Facet.PaintFacetBodyBuilder.PaintBodiesBackgroundColor instead.")"""
        ...
    def PaintSelectedFacets(self) -> None:
        ...
    FacetCollector: FacetCollector
    InheritBodyColorPick: SelectDisplayableObject
    InheritColorPick: Facet.SelectFacetedBody
    PaintBrush: Facet.PaintBrushBuilder
    PaintBrushSize: Expression


class PaintBrushBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPaintBrushColor(self) -> float:
        ...
    def SetPaintBrushColor(self, paintBrushColor: float) -> None:
        ...
    def SetFacetBeingPainted(self, facet: Facet.FacetedBody) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Facet.PaintBrushBuilder.SetBodyBeingPainted instead.")"""
        ...
    def SetBodyBeingPainted(self, body: DisplayableObject) -> None:
        ...
    def PaintVertexColor(self, position: Point3d) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  No replacement for this api.")"""
        ...
    def ClearThePaintPath(self) -> None:
        ...
    def SetupPaintFacetBody(self) -> None:
        ...
    def SetTemporaryFacetDisplay(self, tempDisplay: bool) -> None:
        ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MultiPatchAlignmentBuilder(Builder):
    def __init__(self) -> None: ...
    AlignFacetPatches: SelectDisplayableObjectList
    AlignmentBodies: Facet.SelectFacetedBodyList
    Iteration: int
    MaximumCheckingDistance: float
    ReferenceFacetPatches: SelectDisplayableObjectList
    ReferencePatches: Facet.SelectFacetedBodyList
    Resolution: Facet.MultiPatchAlignmentBuilder.ResolutionType
    Tolerance: float


    class ResolutionType(enum.Enum):
        High = 0
        Medium = 1
        Low = 2
    

class MeshFromCloudBuilder(Builder):
    def __init__(self) -> None: ...
    def SuggestNeighborhoodSize(self) -> None:
        ...
    AnalyzeMeshQuality: bool
    ModeOptions: Facet.MeshFromCloudBuilder.ModeOption
    NeighborhoodSize: float
    PointFile: str
    SelectPoints: SelectPointList
    SmoothingFactor: int
    SourceOptions: Facet.MeshFromCloudBuilder.SourceOption
    TargetVertexNumber: int
    TessellationPercentage: float


    class SourceOption(enum.Enum):
        FromFile = 0
        ExistingPoints = 1
    

    class ModeOption(enum.Enum):
        UniformDensity = 0
        VariableDensity = 1
        KeepAllPoints = 2
    

class MergeFacetFacesBuilder(Builder):
    def __init__(self) -> None: ...
    FaceCollector: ScCollector
    IsEditCopy: bool


class MergeFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    AngleTolerance: float
    ChordHeight: Expression
    DistanceTolerance: float
    EdgeLength: Expression
    FacetBodyOne: Facet.SelectFacetedBody
    FacetBodyTwo: Facet.SelectFacetedBody
    InputStatus: Facet.MergeFacetBodyBuilder.Input


    class Input(enum.Enum):
        Keep = 0
        Delete = 1
        Hide = 2
    

class LocalOffsetBuilder(Builder):
    def __init__(self) -> None: ...
    FacetRegion: FacetCollector
    FacetTransitionRegions: FacetCollector
    IsEditCopy: bool
    IsRegenerateOffsetMesh: bool
    IsReverseDirection: bool
    IsSmoothEdge: bool
    OffsetDistance: Expression
    RegionDistance: Expression
    ShapeMethod: Facet.LocalOffsetBuilder.ShapeMethodType
    TransitionMethod: Facet.LocalOffsetBuilder.TransitionMethodType


    class TransitionMethodType(enum.Enum):
        None = 0
        ByConstantOffset = 1
        ByRegionSelection = 2
    

    class ShapeMethodType(enum.Enum):
        Sharp = 0
        Smooth = 1
    

class FillMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def FlipRangeStart(self) -> None:
        ...
    def FlipRangeEnd(self) -> None:
        ...
    def SetCloseNotchVertex1(self, facetVertexData: Facet.FillMeshBuilder.FacetVertexData) -> None:
        ...
    def SetCloseNotchVertex2(self, facetVertexData: Facet.FillMeshBuilder.FacetVertexData) -> None:
        ...
    def SetBridgeGapStartEdgeVertex1(self, facetVertexData: Facet.FillMeshBuilder.FacetVertexData) -> None:
        ...
    def SetBridgeGapStartEdgeVertex2(self, facetVertexData: Facet.FillMeshBuilder.FacetVertexData) -> None:
        ...
    def SetBridgeGapEndEdgeVertex1(self, facetVertexData: Facet.FillMeshBuilder.FacetVertexData) -> None:
        ...
    def SetBridgeGapEndEdgeVertex2(self, facetVertexData: Facet.FillMeshBuilder.FacetVertexData) -> None:
        ...
    def UpdateHoles(self) -> None:
        ...
    EdgeHole: SelectNXObjectList
    EdgeSelectionMethod: Facet.FillMeshBuilder.EdgeOptionMenu
    EditCopy: bool
    EndEdgeVertex1: Point
    EndEdgeVertex2: Point
    EndHole: SelectNXObjectList
    FacetBodies: SelectNXObjectList
    InnerHole: SelectNXObjectList
    MaxEdges: int
    OuterHole: SelectNXObjectList
    SmoothnessOption: Facet.FillMeshBuilder.SmoothnessOptionMenu
    StartEdgeVertex1: Point
    StartEdgeVertex2: Point
    StartHole: SelectNXObjectList
    Type: Facet.FillMeshBuilder.Types
    Vertex1: Point
    Vertex2: Point


    class Types(enum.Enum):
        FillHole = 0
        CloseNotch = 1
        FillIsland = 2
        ConnectHoles = 3
        BridgeGap = 4
    

    class SmoothnessOptionMenu(enum.Enum):
        Linear = 0
        Refined = 1
        TangentBased = 2
        CurvatureBased = 3
    

    class FillMeshBuilderFacetVertexData():
        Face: NXObject
        NxFacetIndex: int
        PointCoord: Point3d
        def ToString(self) -> str:
            ...
        def __init__(self, Face: NXObject, NxFacetIndex: int, PointCoord: Point3d) -> None: ...
    

    class EdgeOptionMenu(enum.Enum):
        All = 0
        UserSelected = 1
        ByNumberofEdges = 2
    

    class FillMeshBuilder_FacetVertexData():
        face: Tag
        nxFacetIndex: int
        pointCoord: Point3d
    

class FillHoleBuilder(Builder):
    def __init__(self) -> None: ...
    def ClearHoles(self) -> None:
        ...
    def FindHoles(self) -> None:
        ...
    def ClearHoleFills(self) -> None:
        ...
    def FillHoles(self, globalUpdate: bool) -> DisplayableObject:
        ...
    def SwitchHoleFillType(self) -> None:
        ...
    def GetHoleFillsOnly(self) -> DisplayableObject:
        ...
    def GetAllHoles(self, holeCurveTags: typing.List[DisplayableObject]) -> None:
        ...
    def GetNumberOfHoles(self) -> int:
        ...
    def GetHoleByIndex(self, index: int) -> ICurve:
        ...
    def GetTargetHolesByEdgeNumber(self, numMaxEdges: int, holeCurveTags: typing.List[DisplayableObject]) -> None:
        ...
    BridgeEdges1: SelectICurveList
    BridgeEdges2: SelectICurveList
    InnerHole: SelectICurveList
    IsEditCopy: bool
    MaxEdges: int
    OuterHole: SelectICurveList
    SmoothType: Facet.FillHoleBuilder.SmoothTypes
    TargetBody: SelectDisplayableObject
    TargetFacetBody: Facet.SelectFacetedBody
    TargetHole: SelectICurveList
    TargetType: Facet.FillHoleBuilder.TargetTypes
    Type: Facet.FillHoleBuilder.Types


    class Types(enum.Enum):
        FillHole = 0
        FillIsland = 1
        BridgeGap = 2
    

    class TargetTypes(enum.Enum):
        UserDefined = 0
        ByNumberOfEdges = 1
    

    class SmoothTypes(enum.Enum):
        Linear = 0
        Refined = 1
        TangentBased = 2
        CurvatureBased = 3
    

class FeatureExtractionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetExtractedRegions(self) -> typing.List[Facet.FacetedBody]:
        ...
    def GetExtractedBorders(self) -> typing.List[Spline]:
        ...
    AreBordersEnabled: bool
    AreRegionsEnabled: bool
    FacetBodies: Facet.SelectFacetedBodyList
    InputAction: Facet.FeatureExtractionBuilder.InputActions
    IsSmoothingEnabled: bool
    MinimumBorderLength: float
    SmoothingFactor: float


    class InputActions(enum.Enum):
        Blank = 0
        Retain = 1
        Delete = 2
    

class FacetModelingCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Facet.FacetedBodyCollection) -> None: ...
    def CreateConvertFacetBodyBuilder(self) -> Facet.ConvertFacetBodyBuilder:
        ...
    def CreateCleanupFacetBodyBuilder(self) -> Facet.CleanupFacetBodyBuilder:
        ...
    def CreateCombineFacetBodyBuilder(self) -> Facet.CombineFacetBodyBuilder:
        ...
    def CreateFacetBodyFromBodyBuilder(self) -> Facet.FacetBodyFromBodyBuilder:
        ...
    def CreateDetectPrimitivesBuilder(self) -> Facet.DetectPrimitivesBuilder:
        ...
    def CreatePaintFacetBodyBuilder(self) -> Facet.PaintFacetBodyBuilder:
        ...
    def CreatePaintBrushBuilder(self) -> Facet.PaintBrushBuilder:
        ...
    def CreateRemoveUndercutsBuilder(self) -> Facet.RemoveUndercutsBuilder:
        ...
    def CreateCreateTransitionBuilder(self) -> Facet.CreateTransitionBuilder:
        ...
    def CreateLocalOffsetBuilder(self) -> Facet.LocalOffsetBuilder:
        ...
    def CreateMergeFacetFacesBuilder(self) -> Facet.MergeFacetFacesBuilder:
        ...
    def CreateFacetAdjustMinimumRadiusBuilder(self) -> Facet.AdjustMinimumRadiusBuilder:
        ...
    def CreateDivideFacetFaceBuilder(self) -> Facet.DivideFacetFaceBuilder:
        ...
    def CreatePolygonModelingBuilder(self) -> Facet.PolygonModelingBuilder:
        ...
    def CreateRemeshFacetBodyBuilder(self) -> Facet.RemeshFacetBodyBuilder:
        ...
    def CreateSplitCurveMethodBuilder(self) -> Facet.SplitCurveMethodBuilder:
        ...
    def CreateSplitCurveMethodListDataManager(self) -> Facet.SplitCurveMethodListDataManager:
        ...
    def CreateFillMeshBuilder(self) -> Facet.FillMeshBuilder:
        ...
    def CreateMeshFromCloudBuilder(self) -> Facet.MeshFromCloudBuilder:
        ...
    def CreateCombineFacetBodiesBuilder(self) -> Facet.CombineFacetBodiesBuilder:
        ...
    def CreateWrapMeshBuilder(self) -> Facet.WrapMeshBuilder:
        ...
    def CreatePlugLeakageBuilder(self) -> Facet.PlugLeakageBuilder:
        ...
    def CreateReplaceMeshWithFaceBuilder(self) -> Facet.ReplaceMeshWithFaceBuilder:
        ...
    def CreateTubeLatticeBuilder(self, tubeLattice: Features.TubeLattice) -> Features.TubeLatticeBuilder:
        ...
    def Tag(self) -> Tag: ...



class FacetingParameters():
    MaximumFacetEdges: int
    SpecifySurfaceTolerance: bool
    SurfaceDistanceTolerance: float
    SurfaceAngularTolerance: float
    SpecifyCurveTolerance: bool
    CurveDistanceTolerance: float
    CurveAngularTolerance: float
    CurveMaximumLength: float
    SpecifyConvexFacets: bool
    SpecifyMaximumFacetSize: bool
    MaximumFacetSize: float
    SpecifyParameters: bool
    NumberStorageType: int
    SpecifyViewDirection: bool
    SilhouetteViewDirection: Vector3d
    SilhouetteChordTolerance: float
    StoreFaceTag: bool
    WithLODS: bool
    def ToString(self) -> str:
        ...


class FacetedFace(DisplayableObject):
    def __init__(self) -> None: ...
    def GetNumberOfEdges(self) -> int:
        ...
    def GetEdges(self) -> typing.List[Facet.FacetedEdge]:
        ...
    def GetBody(self) -> Facet.FacetedBody:
        ...
    def GetSurfaceData(self, position: Point3d, dir: Point3d, radius: float, radiusOrAngle: float, sense: bool) -> None:
        ...
    FaceType: Facet.FacetedFace.FacetedfaceType


    class FacetedfaceType(enum.Enum):
        Undefined = 0
        Planar = 1
        Cylindrical = 2
        Conical = 3
        Spherical = 4
        Toroidal = 5
        Parametric = 6
    

class FacetedEdge(DisplayableObject):
    def __init__(self) -> None: ...
    def GetFaces(self) -> typing.List[Facet.FacetedFace]:
        ...
    def GetVertices(self, vertex1: Point3d, vertex2: Point3d) -> None:
        ...
    def GetBody(self) -> Facet.FacetedBody:
        ...
    def GetCurveData(self, position: Point3d, dirOrEndPt: Point3d, xAxis: Point3d, radius: float, minorRadius: float) -> None:
        ...
    def GetLength(self) -> float:
        ...
    def GetLocations(self) -> typing.List[GeometricUtilities.CurveLocation]:
        ...
    EdgeType: Facet.FacetedEdge.FacetededgeType
    IsReference: bool


    class FacetededgeType(enum.Enum):
        Undefined = 0
        Linear = 1
        Circular = 2
        Elliptical = 3
        Intersection = 4
        Spline = 5
    

class FacetedBodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Facet.FacetedBody]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Facet.FacetedBody:
        ...
    def CreateFacetCurvatureBuilder(self) -> Facet.CurvatureBuilder:
        ...
    def CreateFacetFeatureExtractionBuilder(self) -> Facet.FeatureExtractionBuilder:
        ...
    def Convert(self, fromBody: Facet.FacetedBody, toFacetType: Facet.FacetedBodyCollection.Type) -> None:
        ...
    def Copy(self, fromBody: Facet.FacetedBody, toPart: Part, toFacetType: Facet.FacetedBodyCollection.Type) -> Facet.FacetedBody:
        ...
    def GetAssociatedFacetedBodies(self, solidBody: Body, numberOfUnloadedFacetedBodies: int) -> typing.List[Facet.FacetedBody]:
        ...
    def DeleteTemporaryFacesAndEdges(self) -> None:
        ...
    def CreateBestFitAlignBuilder(self) -> Facet.BestFitAlignBuilder:
        ...
    def CreateFillHoleBuilder(self) -> Facet.FillHoleBuilder:
        ...
    def CreateSTLImportBuilder(self) -> Facet.STLImportBuilder:
        ...
    def CreateDecimateFacetBodyBuilder(self) -> Facet.DecimateFacetBodyBuilder:
        ...
    def CreateMultiPatchAlignmentBuilder(self) -> Facet.MultiPatchAlignmentBuilder:
        ...
    def CreateSubdivideFacetBodyBuilder(self) -> Facet.SubdivideFacetBodyBuilder:
        ...
    def CreateSmoothFacetBodyBuilder(self) -> Facet.SmoothFacetBodyBuilder:
        ...
    def CreateSnipFacetBodyBuilder(self) -> Facet.SnipFacetBodyBuilder:
        ...
    def CreateFacetBody(self, solidBodies: typing.List[Body], facetBodies: typing.List[Facet.FacetedBody], errorTable: int) -> None:
        ...
    def CreateFacetBodyFromFaces(self, solidFaces: typing.List[Face], facetBodies: typing.List[Facet.FacetedBody], errorTable: int) -> None:
        ...
    def CreateExtrudeFacetBodyBuilder(self) -> Facet.ExtrudeFacetBodyBuilder:
        ...
    def CreateExtrudeProfileBuilder(self) -> Facet.ExtrudeProfileBuilder:
        ...
    def CreateMergeFacetBodyBuilder(self) -> Facet.MergeFacetBodyBuilder:
        ...
    def CreateBridgeFacetBodyBuilder(self) -> Facet.BridgeFacetBodyBuilder:
        ...
    def CreateSewFacetBodyBuilder(self) -> Facet.SewFacetBodyBuilder:
        ...
    def Tag(self) -> Tag: ...

    FacetModelingCollection: Facet.FacetModelingCollection


    class Type(enum.Enum):
        Nx = 0
        Jt = 1
    

class FacetedBody(DisplayableObject):
    def __init__(self) -> None: ...
    def GetNumberOfFacets(self, levelOfDetail: int) -> int:
        ...
    def GetFaces(self) -> typing.List[Facet.FacetedFace]:
        ...
    def GetNumberOfEdges(self) -> int:
        ...
    def GetEdges(self) -> typing.List[Facet.FacetedEdge]:
        ...
    def HasTopologyInformation(self) -> bool:
        ...
    def HasLightWeightAnalytics(self) -> bool:
        ...
    def GetParameters(self) -> Facet.FacetingParameters:
        ...
    def SetParameters(self, parameters: Facet.FacetingParameters) -> None:
        ...
    def DestroyOwnedFacets(self) -> None:
        ...
    AssociatedBody: Body
    BodyType: Facet.FacetedBody.FacetedbodyType
    IsAssemblyLevel: bool
    IsAssociatedBodyLoaded: bool
    IsSheetBody: bool
    IsSolidBody: bool
    NumberOfFaces: int
    NumberOfLevelsOfDetail: int
    SurfaceArea: float
    Volume: float


    class FacetedbodyType(enum.Enum):
        Undefined = 0
        SolidBody = 1
        SheetBody = 2
    

class FacetBodyFromBodyBuilder(Builder):
    def __init__(self) -> None: ...
    Associative: bool
    MaximumDeviation: float
    NonFacetedBodiesToConvert: SelectDisplayableObjectList
    OriginalBodyOption: Facet.FacetBodyFromBodyBuilder.OriginalBodyOptions
    OutputType: Facet.FacetBodyFromBodyBuilder.OutputTypes


    class OutputTypes(enum.Enum):
        ConvergentBody = 0
        NXFacetBody = 1
        JTFacetBody = 2
    

    class OriginalBodyOptions(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

class ExtrudeProfileBuilder(Builder):
    def __init__(self) -> None: ...
    Direction: Direction
    FirstDistance: Expression
    Offset: Expression
    Profile: Section
    SecondDistance: Expression
    Tolerance: Expression


class ExtrudeFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    Direction: Direction
    Distance: Expression
    DistanceTolerance: float
    FacetBody: SelectDisplayableObjectList
    Offset: Expression
    Plane: Plane
    Type: Facet.ExtrudeFacetBodyBuilder.LimitType


    class LimitType(enum.Enum):
        Distance = 0
        ToPlane = 1
    

class DivideFacetFaceBuilder(Builder):
    def __init__(self) -> None: ...
    Degree: int
    FacetBodyCollector: ScCollector
    FacetCollector: FacetCollector
    IsEditCopy: bool
    IsSmoothEdge: bool
    Segments: int
    SplitCurveMethodListDataManager: Facet.SplitCurveMethodListDataManager
    Type: Facet.DivideFacetFaceBuilder.DivideFacetTypes


    class DivideFacetTypes(enum.Enum):
        ByColor = 0
        ByRegion = 1
        ByCurves = 2
    

class DetectPrimitivesBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPlaneColor(self) -> float:
        ...
    def SetPlaneColor(self, planeColor: float) -> None:
        ...
    def GetSphereColor(self) -> float:
        ...
    def SetSphereColor(self, sphereColor: float) -> None:
        ...
    def GetCylinderColor(self) -> float:
        ...
    def SetCylinderColor(self, cylinderColor: float) -> None:
        ...
    def GetConeColor(self) -> float:
        ...
    def SetConeColor(self, coneColor: float) -> None:
        ...
    def GetBlendColor(self) -> float:
        ...
    def SetBlendColor(self, blendColor: float) -> None:
        ...
    def GetOtherColor(self) -> float:
        ...
    def SetOtherColor(self, otherColor: float) -> None:
        ...
    def AdjustShapeBoundary(self) -> None:
        ...
    BlendFactor: Expression
    CurvatureSensitivity: int
    FacetSelection: SelectDisplayableObjectList


class DecimateFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    AngleThreshold: float
    Bodies: SelectDisplayableObjectList
    DecimateMethod: Facet.DecimateFacetBodyBuilder.DecimateMethodType
    FacetBodies: Facet.SelectFacetedBodyList
    FacetCollector: FacetCollector
    IsEditCopy: bool
    IsLockBoundary: bool
    MinimumArea: float
    Percentage: float
    RegionList: GeometricUtilities.BoundaryDefinitionBuilderList
    Tolerance: float


    class DecimateMethodType(enum.Enum):
        ChordalDeviation = 0
        SmallestFacet = 1
        Percentage = 2
    

class CurvatureBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteCurvature(self) -> None:
        ...
    Bodies: SelectDisplayableObjectList
    ConcaveRadius: float
    ConvexRadius: float
    FacetBodies: Facet.SelectFacetedBodyList
    IsDirectionReversed: bool
    SmoothingFactor: float


class CreateTransitionBuilder(Builder):
    def __init__(self) -> None: ...
    Distance: Expression
    IsClosed: bool
    IsEditCopy: bool
    Radius: Expression
    SelectedBody: DisplayableObject
    SelectedPoints: Features.GeometricConstraintDataManager
    Type: Facet.CreateTransitionBuilder.Types


    class Types(enum.Enum):
        Round = 0
        Flat = 1
    

class ConvertFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    CleanUp: bool
    FacetedBodiesToConvert: SelectDisplayableObjectList
    MinimumAngleFoldedFacets: float
    MinimumFacetNumber: int
    OriginalBodyOption: Facet.ConvertFacetBodyBuilder.OriginalBodyOptions
    OutputType: Facet.ConvertFacetBodyBuilder.OutputTypes


    class OutputTypes(enum.Enum):
        ConvergentBody = 0
        NXFacetBody = 1
        JTFacetBody = 2
    

    class OriginalBodyOptions(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

class CombineFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    FacetedBodiesToCombine: SelectDisplayableObjectList


class CombineFacetBodiesBuilder(Builder):
    def __init__(self) -> None: ...
    AnalyzeMeshQuality: bool
    AverageFacetSize: float
    InputBodiesOptions: Facet.CombineFacetBodiesBuilder.InputBodiesOption
    InputFacetBodies: SelectNXObjectList


    class InputBodiesOption(enum.Enum):
        Delete = 0
        Keep = 1
        Hide = 2
    

class CleanupFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    def SetAllOptionsToNone(self) -> None:
        ...
    def SetAllOptionsToAnalyze(self) -> None:
        ...
    def SetAllOptionsToRepair(self) -> None:
        ...
    def DisplayCleanupReportInListWindow(self) -> None:
        ...
    DistanceTolerance: float
    FoldedEdges: Facet.CleanupFacetBodyBuilder.CleanupOptions
    InconsistentNormals: Facet.CleanupFacetBodyBuilder.CleanupOptions
    InputBodies: SelectDisplayableObjectList
    LaminarSlits: Facet.CleanupFacetBodyBuilder.CleanupOptions
    LongFacets: Facet.CleanupFacetBodyBuilder.CleanupOptions
    MaxRatioLongFacets: float
    MinAngleFoldedFacets: float
    MinFacetNumberPerBody: int
    OriginalBodyOption: Facet.CleanupFacetBodyBuilder.OriginalBodyOptions
    SelfIntersections: Facet.CleanupFacetBodyBuilder.CleanupOptions
    ShowInfo: bool
    ThinFacets: Facet.CleanupFacetBodyBuilder.CleanupOptions
    ToleranceFactor: float


    class OriginalBodyOptions(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

    class CleanupOptions(enum.Enum):
        None = 0
        Analyze = 1
        Repair = 2
    

class BridgeFacetBodyBuilder(Builder):
    def __init__(self) -> None: ...
    def FlipRange1(self) -> None:
        ...
    def FlipRange2(self) -> None:
        ...
    DistanceTolerance: float
    FacetBodyOne: Facet.SelectFacetedBody
    FacetBodyTwo: Facet.SelectFacetedBody
    InputStatus: Facet.BridgeFacetBodyBuilder.Input
    Smoothness: Facet.BridgeFacetBodyBuilder.SmoothTypes
    Vertex1Range1: Point
    Vertex1Range2: Point
    Vertex2Range1: Point
    Vertex2Range2: Point


    class SmoothTypes(enum.Enum):
        Linear = 0
        TangentBased = 1
    

    class Input(enum.Enum):
        Keep = 0
        Delete = 1
        Hide = 2
    

class BestFitAlignBuilder(Builder):
    def __init__(self) -> None: ...
    DestinationObjects: SelectNXObjectList
    Direction: Direction
    FitConstraints: Facet.BestFitAlignBuilder.ConstraintOptions
    GlobalSearch: bool
    MobileObjects: SelectNXObjectList
    RotateCenter: Point
    SourceObjects: SelectNXObjectList


    class ConstraintOptions(enum.Enum):
        Free = 0
        OnlyTranslation = 1
        TranslationInPlane = 2
        TranslationAlongDirection = 3
        OnlyRotation = 4
        RotationAroundPoint = 5
        RotationAroundLine = 6
        HoldToPlane = 7
        HoldToLine = 8
    

class AdjustMinimumRadiusBuilder(Builder):
    def __init__(self) -> None: ...
    Facets: FacetCollector
    IsEditCopy: bool
    MinimumRadius: float


