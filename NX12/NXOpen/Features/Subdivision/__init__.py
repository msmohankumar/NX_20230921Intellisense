from ....NXOpen import *
from ...Features import *
from ..Subdivision import *

import typing
import enum

class TransformCageData(Builder):
    def __init__(self) -> None: ...
    def ResetFallOffToLinear(self) -> None:
        ...
    CageManipulator: Features.Subdivision.CageManipulatorData
    CanMoveToolOnly: bool
    CanRelocateToolToSelection: bool
    CanReorientToolToSelection: bool
    FallOffFactor: float
    FallOffMethod: Features.Subdivision.TransformCageData.FallOffMethodType
    FallOffObjects: Features.Subdivision.SelectCageObjectData
    MovementMethod: Features.Subdivision.TransformCageData.MovementMethodType
    MovementPlane: Plane
    MovementVector: Direction
    ScalingMethod: Features.Subdivision.TransformCageData.ScalingMethodType
    TransformationMethod: Features.Subdivision.TransformCageData.TransformationMethodType
    WCSOption: Features.Subdivision.TransformCageData.WCSOptionType


    class WCSOptionType(enum.Enum):
        InferredAxis = 0
        X = 1
        Y = 2
        Z = 3
        YZ = 4
        XZ = 5
        XY = 6
    

    class TransformationMethodType(enum.Enum):
        Drag = 0
        Transform = 1
    

    class ScalingMethodType(enum.Enum):
        Linear = 0
        Planar = 1
        Uniform = 2
    

    class MovementMethodType(enum.Enum):
        WCS = 0
        View = 1
        Vector = 2
        Plane = 3
        Normal = 4
        Edge = 5
    

    class FallOffMethodType(enum.Enum):
        None = 0
        Selected = 1
        All = 2
    

class SubdivisionTubeBuilder(Builder):
    def __init__(self) -> None: ...
    NumberOfSegments: int
    PathObject: Features.Subdivision.SelectCageObjectData
    Size: Expression


class SubdivisionSweepBuilder(Builder):
    def __init__(self) -> None: ...
    CanSew: bool
    Continuity: Features.Subdivision.SubdivisionSweepBuilder.ContinuityType
    Guides: Features.Subdivision.CageSectionDataList
    Sections: Features.Subdivision.CageSectionDataList


    class ContinuityType(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionSubdivideFaceBuilder(Builder):
    def __init__(self) -> None: ...
    def Subdivide(self) -> None:
        ...
    FacesToSubdivide: Features.Subdivision.SelectCageObjectData
    Scale: Expression


class SubdivisionSplitFaceBuilder(Builder):
    def __init__(self) -> None: ...
    def AddSplitPoint(self, location: Point3d, object: DisplayableObject) -> None:
        ...
    def ClearSplitPoints(self) -> None:
        ...
    def UpdateSplitPositions(self, splitLineIndex: int, positions: typing.List[Point3d]) -> None:
        ...
    FacesToSplit: Features.Subdivision.SelectCageObjectData
    Number: int
    ReferenceEdge: Features.Subdivision.SelectCageObjectData
    Type: Features.Subdivision.SubdivisionSplitFaceBuilder.Types


    class Types(enum.Enum):
        Uniform = 0
        ThroughLines = 1
    

class SubdivisionSewCageBuilder(Builder):
    def __init__(self) -> None: ...
    SelectedEdges1: Features.Subdivision.SelectCageObjectData
    SelectedEdges2: Features.Subdivision.SelectCageObjectData


class SubdivisionSetWeightBuilder(Builder):
    def __init__(self) -> None: ...
    TargetObject: Features.Subdivision.SelectCageObjectData
    WeightPercent: int


class SubdivisionSetContinuityBuilder(Builder):
    def __init__(self) -> None: ...
    ContinuityType: Features.Subdivision.SubdivisionSetContinuityBuilder.ContinuityTypes
    TargetObject: Features.Subdivision.SelectCageObjectData


    class ContinuityTypes(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionRevolveBuilder(Builder):
    def __init__(self) -> None: ...
    AxisPoint: SelectNXObject
    AxisVector: Direction
    CanSew: bool
    Continuity: Features.Subdivision.SubdivisionRevolveBuilder.ContinuityType
    EndAngle: Expression
    NumOfSegments: int
    SectionObject: Features.Subdivision.SelectCageObjectData
    StartAngle: Expression


    class ContinuityType(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionProjectCageBuilder(Builder):
    def __init__(self) -> None: ...
    def OnTargetPlane(self) -> None:
        ...
    def OnTargetDynamicPlane(self) -> None:
        ...
    Mode: Features.Subdivision.SubdivisionProjectCageBuilder.ModeOptions
    ObjectsToProject: Features.Subdivision.SelectCageObjectData
    Target: SelectDisplayableObject
    TargetCageObjects: Features.Subdivision.SelectCageObjectData
    TargetDynamicPlane: CoordinateSystem
    TargetPlane: Plane
    TargetType: Features.Subdivision.SubdivisionProjectCageBuilder.TargetTypes
    Type: Features.Subdivision.SubdivisionProjectCageBuilder.Types


    class Types(enum.Enum):
        ToTarget = 0
        ToAverage = 1
        AlignNormal = 2
    

    class TargetTypes(enum.Enum):
        InferredPlane = 0
        InferredAxis = 1
        YcZcPlane = 2
        XcZcPlane = 3
        XcYcPlane = 4
        XcAxis = 5
        YcAxis = 6
        ZcAxis = 7
        Object = 8
        Plane = 9
        DynamicPlane = 10
    

    class ModeOptions(enum.Enum):
        Linear = 0
        Planar = 1
    

class SubdivisionPrimitiveShapeBuilderEx(Builder):
    def __init__(self) -> None: ...
    def UpdateMesh(self) -> None:
        ...
    CircularSegments: int
    Height: Expression
    HeightZ: Expression
    InnerSize: Expression
    LengthX: Expression
    LinearSegments: int
    Origin: Point
    OuterSize: Expression
    RadialSegments: int
    Size: Expression
    SphereSubdivisionLevelOption: Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel
    Transformer: GeometricUtilities.TransformerData
    Type: Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.Types
    WidthY: Expression
    XSegments: int
    YSegments: int
    ZSegments: int


    class Types(enum.Enum):
        Sphere = 0
        Cylinder = 1
        Block = 2
        Circle = 3
        Rectangle = 4
        Torus = 5
    

    class SphereSubdivisionLevel(enum.Enum):
        Base = 0
        First = 1
        Second = 2
    

class SubdivisionPrimitiveShapeBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateMesh(self) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx instead..")"""
        ...
    CircularSegments: int
    Height: Expression
    HeightZ: Expression
    InnerSize: Expression
    LengthX: Expression
    Origin: Point
    OuterSize: Expression
    RadialSegments: int
    Size: Expression
    Transformer: GeometricUtilities.TransformerData
    Type: Features.Subdivision.SubdivisionPrimitiveShapeBuilder.Types
    WidthY: Expression


    class Types(enum.Enum):
        Sphere = 0
        Cylinder = 1
        Block = 2
        Circle = 3
        Rectangle = 4
        Torus = 5
    

class SubdivisionMergeFaceBuilder(Builder):
    def __init__(self) -> None: ...
    FacesToMerge: Features.Subdivision.SelectCageObjectData


class SubdivisionLoftBuilder(Builder):
    def __init__(self) -> None: ...
    CanSew: bool
    Continuity: Features.Subdivision.SubdivisionLoftBuilder.ContinuityType
    IsClosed: bool
    NumberOfSegments: int
    Sections: Features.Subdivision.CageSectionDataList


    class ContinuityType(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionFillBuilder(Builder):
    def __init__(self) -> None: ...
    CanConnectSymmetrically: bool
    Continuity: Features.Subdivision.SubdivisionFillBuilder.ContinuityType
    SelectedEdges: Features.Subdivision.SelectCageObjectData


    class ContinuityType(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionExtrudeCageBuilder(Builder):
    def __init__(self) -> None: ...
    def Extrude(self) -> None:
        ...
    CanMoveToolOnly: bool
    CanRelocateToolToSelection: bool
    CanReorientToolToSelection: bool
    Continuity: Features.Subdivision.SubdivisionExtrudeCageBuilder.ContinuityType
    DirectionOption: Features.Subdivision.SubdivisionExtrudeCageBuilder.DirectionType
    Distance: Expression
    NumberOfSegments: int
    ScalingMethod: Features.Subdivision.SubdivisionExtrudeCageBuilder.ScalingMethodType
    SelectionObject: Features.Subdivision.SelectCageObjectData
    TransformationMethod: Features.Subdivision.SubdivisionExtrudeCageBuilder.TransformationMethodType
    Transformer: GeometricUtilities.TransformerData
    Vector: Direction


    class TransformationMethodType(enum.Enum):
        DragLinear = 0
        Transform = 1
    

    class ScalingMethodType(enum.Enum):
        Linear = 0
        Planar = 1
        Uniform = 2
    

    class DirectionType(enum.Enum):
        Inferred = 0
        Vector = 1
        Perpendicular = 2
    

    class ContinuityType(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionDeleteObjectBuilder(Builder):
    def __init__(self) -> None: ...
    Objects: Features.Subdivision.SelectCageObjectData


class SubdivisionDeleteFaceBuilder(Builder):
    def __init__(self) -> None: ...
    FaceToDelete: Features.Subdivision.SelectCageObjectData


class SubdivisionDeleteCageBuilder(Builder):
    def __init__(self) -> None: ...
    SelectCageObject: Features.Subdivision.SelectCageObjectData


class SubdivisionConnectCageBuilder(Builder):
    def __init__(self) -> None: ...
    CageEdgeToEdit: Features.Subdivision.SelectCageObjectData
    ContinuityType: Features.Subdivision.SubdivisionConnectCageBuilder.ContinuityTypes
    ExternalReference: Section


    class ContinuityTypes(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionBridgeFaceBuilder(Builder):
    def __init__(self) -> None: ...
    Continuity: Features.Subdivision.SubdivisionBridgeFaceBuilder.ContinuityType
    FaceSet1: Features.Subdivision.SelectCageObjectData
    FaceSet2: Features.Subdivision.SelectCageObjectData
    NumSegments: int


    class ContinuityType(enum.Enum):
        Smooth = 0
        Sharp = 1
    

class SubdivisionBodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Features.Subdivision.SubdivisionBody]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateSubdivisionPrimitiveShapeBuilder(self) -> Features.Subdivision.SubdivisionPrimitiveShapeBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionPrimitiveShapeBuilderEx instead")"""
        ...
    def CreateSubdivisionPrimitiveShapeBuilderEx(self) -> Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx:
        ...
    def CreateSubdivisionExtrudeCageBuilder(self) -> Features.Subdivision.SubdivisionExtrudeCageBuilder:
        ...
    def CreateSubdivisionSetWeightBuilder(self) -> Features.Subdivision.SubdivisionSetWeightBuilder:
        ...
    def CreateSubdivisionSetContinuityBuilder(self) -> Features.Subdivision.SubdivisionSetContinuityBuilder:
        ...
    def CreateSubdivisionDeleteFaceBuilder(self) -> Features.Subdivision.SubdivisionDeleteFaceBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use  Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionDeleteCageBuilder  instead.")"""
        ...
    def CreateTransformCageData(self) -> Features.Subdivision.TransformCageData:
        ...
    def CreateSubdivisionFillBuilder(self) -> Features.Subdivision.SubdivisionFillBuilder:
        ...
    def CreateSubdivisionBridgeFaceBuilder(self) -> Features.Subdivision.SubdivisionBridgeFaceBuilder:
        ...
    def CreateStartSymmetricModelingBuilder(self) -> Features.Subdivision.StartSymmetricModelingBuilder:
        ...
    def StopSymmetricModeling(self) -> None:
        ...
    def CreateSubdivisionProjectCageBuilder(self) -> Features.Subdivision.SubdivisionProjectCageBuilder:
        ...
    def CreateSubdivisionMergeFaceBuilder(self) -> Features.Subdivision.SubdivisionMergeFaceBuilder:
        ...
    def CreateSubdivisionSplitFaceBuilder(self) -> Features.Subdivision.SubdivisionSplitFaceBuilder:
        ...
    def CreateSubdivisionSubdivideFaceBuilder(self) -> Features.Subdivision.SubdivisionSubdivideFaceBuilder:
        ...
    def CreateImportSubdivisionGeometryBuilder(self) -> Features.Subdivision.ImportSubdivisionGeometryBuilder:
        ...
    def CreateCagePolylineBuilder(self, polyline: Polyline) -> Features.Subdivision.CagePolylineBuilder:
        ...
    def CreateExtractCagePolylineBuilder(self) -> Features.Subdivision.ExtractCagePolylineBuilder:
        ...
    def CreateSubdivisionRevolveBuilder(self) -> Features.Subdivision.SubdivisionRevolveBuilder:
        ...
    def CreateSubdivisionTubeBuilder(self) -> Features.Subdivision.SubdivisionTubeBuilder:
        ...
    def CreateCopyCageBuilder(self) -> Features.Subdivision.CopyCageBuilder:
        ...
    def CreateEmptyCageSectionBuilder(self) -> Features.Subdivision.CageSectionData:
        ...
    def CreateSubdivisionLoftBuilder(self) -> Features.Subdivision.SubdivisionLoftBuilder:
        ...
    def CreateSubdivisionSweepBuilder(self) -> Features.Subdivision.SubdivisionSweepBuilder:
        ...
    def CreateSubdivisionSewCageBuilder(self) -> Features.Subdivision.SubdivisionSewCageBuilder:
        ...
    def CreateSubdivisionDeleteCageBuilder(self) -> Features.Subdivision.SubdivisionDeleteCageBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use  Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionDeleteObjectBuilder  instead.")"""
        ...
    def CreateSplitSubdivisionBodyBuilder(self) -> Features.Subdivision.SplitSubdivisionBodyBuilder:
        ...
    def CreateMergeSubdivisionBodiesBuilder(self) -> Features.Subdivision.MergeSubdivisionBodiesBuilder:
        ...
    def CreateCopyCageData(self) -> Features.Subdivision.CopyCageData:
        ...
    def CreatePasteCageData(self) -> Features.Subdivision.PasteCageData:
        ...
    def CreateDefineWorkRegionBuilder(self) -> Features.Subdivision.DefineWorkRegionBuilder:
        ...
    def CreateMirrorCageBuilder(self) -> Features.Subdivision.MirrorCageBuilder:
        ...
    def CreateOffsetCageBuilder(self) -> Features.Subdivision.OffsetCageBuilder:
        ...
    def CreateSubdivisionDeleteObjectBuilder(self) -> Features.Subdivision.SubdivisionDeleteObjectBuilder:
        ...
    def CreateDeleteConstraintBuilder(self) -> Features.Subdivision.DeleteConstraintBuilder:
        ...
    def CreateSubdivisionConnectCageBuilder(self) -> Features.Subdivision.SubdivisionConnectCageBuilder:
        ...
    def CreateExportSubdivisionGeometryBuilder(self) -> Features.Subdivision.ExportSubdivisionGeometryBuilder:
        ...
    def Tag(self) -> Tag: ...



class SubdivisionBody(Features.BodyFeature):
    def __init__(self) -> None: ...


class StartSymmetricModelingBuilder(Builder):
    def __init__(self) -> None: ...
    EdgesToProject: Features.Subdivision.SelectCageObjectData
    MirrorProcedureOptions: Features.Subdivision.StartSymmetricModelingBuilder.MirrorProcedureOption
    Plane: Plane
    SwitchSide: bool


    class MirrorProcedureOption(enum.Enum):
        CutBody = 0
        ProjectEdge = 1
    

class SplitSubdivisionBodyBuilder(Builder):
    def __init__(self) -> None: ...
    InputBodyOption: Features.Subdivision.SplitSubdivisionBodyBuilder.InputBodyOptions
    SubdivisionBodiesToSplit: Features.Subdivision.SelectSubdivisionBodyList


    class InputBodyOptions(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

class SelectSubdivisionBodyList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Features.Subdivision.SubdivisionBody) -> bool:
        ...
    def Add(self, objects: typing.List[Features.Subdivision.SubdivisionBody]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Features.Subdivision.SubdivisionBody, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Features.Subdivision.SubdivisionBody) -> bool:
        ...
    def Remove(self, object: Features.Subdivision.SubdivisionBody, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Features.Subdivision.SubdivisionBody, view1: View, point1: Point3d, selection2: Features.Subdivision.SubdivisionBody, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Features.Subdivision.SubdivisionBody]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Features.Subdivision.SubdivisionBody) -> bool:
        ...
    def SetArray(self, objects: typing.List[Features.Subdivision.SubdivisionBody]) -> None:
        ...
    def GetArray(self) -> typing.List[Features.Subdivision.SubdivisionBody]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Features.Subdivision.SubdivisionBody, view1: View, point1: Point3d, selection2: Features.Subdivision.SubdivisionBody, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Features.Subdivision.SubdivisionBody, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCageObjectData(TaggedObject):
    def __init__(self) -> None: ...
    def ClearAndAdd(self, objects: typing.List[NXObject], view: View, point: Point3d) -> None:
        ...
    def SetCursorLocation(self, point: Point3d) -> None:
        ...
    def SetViewDirection(self, direction: Vector3d) -> None:
        ...
    def Validate(self) -> bool:
        ...
    CanDeselectObjectsAutomatically: bool
    SelectionList: SelectDisplayableObjectList


class PasteCageData(Builder):
    def __init__(self) -> None: ...
    CanMoveToolOnly: bool
    Transformer: GeometricUtilities.TransformerData


class OffsetCageBuilder(Builder):
    def __init__(self) -> None: ...
    CanReverseOffsetDirection: bool
    NumberOfCopies: int
    Objects: Features.Subdivision.SelectCageObjectData
    OffsetDistance: Expression


class MirrorCageBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateOnMirrorPlane(self) -> None:
        ...
    MirrorPlane: Plane
    Objects: Features.Subdivision.SelectCageObjectData


class MergeSubdivisionBodiesBuilder(Builder):
    def __init__(self) -> None: ...
    InputBodyOption: Features.Subdivision.MergeSubdivisionBodiesBuilder.InputBodyOptions
    SubdivisionBodiesToMerge: Features.Subdivision.SelectSubdivisionBodyList


    class InputBodyOptions(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

class ImportSubdivisionGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    CanCreateSingleFeature: bool
    FileName: str


class ExtractCagePolylineBuilder(Builder):
    def __init__(self) -> None: ...
    CurveToExtract: ScCollector
    InputCurveOptions: Features.Subdivision.ExtractCagePolylineBuilder.InputCurveOption
    NumberOfSegments: int


    class InputCurveOption(enum.Enum):
        Keep = 0
        Hide = 1
        Delete = 2
    

class ExportSubdivisionGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    FeatureSet: Features.SelectFeatureList
    FileName: str


class DeleteConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    Objects: Features.Subdivision.SelectCageObjectData


class DefineWorkRegionBuilder(Builder):
    def __init__(self) -> None: ...
    FrozenColor: NXColor
    FrozenRegionDefinitionMethod: Features.Subdivision.DefineWorkRegionBuilder.FrozenRegionDefinitionMethods
    WorkRegionDefinitionMethod: Features.Subdivision.DefineWorkRegionBuilder.WorkRegionDefinitionMethods
    WorkRegionObjects: Features.Subdivision.SelectCageObjectData


    class WorkRegionDefinitionMethods(enum.Enum):
        All = 0
        Selected = 1
    

    class FrozenRegionDefinitionMethods(enum.Enum):
        Hidden = 0
        Colored = 1
    

class CopyCageData(Builder):
    def __init__(self) -> None: ...
    def GetObjects(self) -> typing.List[NXObject]:
        ...
    def SetObjects(self, objects: typing.List[NXObject]) -> None:
        ...


class CopyCageBuilder(Builder):
    def __init__(self) -> None: ...
    def ResetTransformerToCentroidOfSelection(self) -> None:
        ...
    def SetTransformerToObject(self, selectionData: Features.Subdivision.CageManipulatorData.ObjectSelectionData) -> None:
        ...
    CanMoveToolOnly: bool
    CanRelocateToolToSelection: bool
    CanReorientToolToSelection: bool
    NumberOfCopies: int
    Objects: Features.Subdivision.SelectCageObjectData
    Transformer: GeometricUtilities.TransformerData


class CageSectionDataList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Features.Subdivision.CageSectionData]) -> None:
        ...
    def Append(self, object: Features.Subdivision.CageSectionData) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Features.Subdivision.CageSectionData) -> int:
        ...
    def FindItem(self, index: int) -> Features.Subdivision.CageSectionData:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Features.Subdivision.CageSectionData) -> None:
        ...
    def Erase(self, obj: Features.Subdivision.CageSectionData, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Features.Subdivision.CageSectionData]:
        ...
    def SetContents(self, objects: typing.List[Features.Subdivision.CageSectionData]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Features.Subdivision.CageSectionData, object2: Features.Subdivision.CageSectionData) -> None:
        ...
    def Insert(self, location: int, object: Features.Subdivision.CageSectionData) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class CageSectionData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CanReverseDirection: bool
    SelectionObject: Features.Subdivision.SelectCageObjectData


class CagePolylineBuilder(Features.PolylineBuilder):
    def __init__(self) -> None: ...


class CageManipulatorData(Features.Subdivision.SelectCageObjectData):
    def __init__(self) -> None: ...
    def PrepareToMove(self, moveData: Features.Subdivision.CageManipulatorData.ObjectMoveData) -> None:
        ...
    def Move(self, moveToPoint: Point3d, isSnapGesture: bool) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Features.Subdivision.CageManipulatorData.Move with optional constraint point instead.")"""
        ...
    def Move(self, moveToPoint: Point3d, point: Point, isSnapGesture: bool) -> None:
        ...
    def EndMove(self) -> None:
        ...
    def StepMove(self, step: float) -> None:
        ...
    def ResetTransformerToCentroidOfSelection(self) -> None:
        ...
    def SetTransformerToObject(self, selectionData: Features.Subdivision.CageManipulatorData.ObjectSelectionData) -> None:
        ...
    Transformer: GeometricUtilities.TransformerData


    class CageManipulatorDataObjectSelectionData():
        SelectedObject: NXObject
        SelectionPosition: Point3d
        ViewDirection: Vector3d
        IsSnappedPosition: bool
        def ToString(self) -> str:
            ...
    

    class CageManipulatorDataObjectMoveData():
        DraggedObject: NXObject
        BeginDragCursorPosition: Point3d
        BeginDragObjectPosition: Point3d
        View: View
        MicropositioningScale: float
        ViewDirection: Vector3d
        def ToString(self) -> str:
            ...
    

