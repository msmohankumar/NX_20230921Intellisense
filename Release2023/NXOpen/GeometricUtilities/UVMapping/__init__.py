from ....NXOpen import *
from ...GeometricUtilities import *
from ..UVMapping import *

import typing
import enum

class UVParameterizationBuilder(Builder):
    def __init__(self) -> None: ...
    def Evaluate(self) -> None:
        ...
    Faces: ScCollector
    NumberOfGridLines: int
    OuterBoundarySeedEdge: SelectEdge
    RipEdges: Section
    TessellationResolution: GeometricUtilities.UVMapping.UVParameterizationBuilder.TessellationResolutions
    Type: GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes
    UDirectionCurve: SelectTaggedObject


    class TessellationResolutions(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        ExtraFine = 3
    

    class ParameterizationTypes(enum.Enum):
        ShapePreserving = 0
        LengthPreserving = 1
    

class UVMeshManipulatorData(GeometricUtilities.UVMapping.SelectUVMeshObjectData):
    def __init__(self) -> None: ...
    def SetTransformerToObject(self, selectionData: GeometricUtilities.UVMapping.UVMeshManipulatorData.ObjectSelectionData) -> None:
        ...
    def SetUAxisDirection(self, canAlignToUDirection: bool) -> None:
        ...
    def SetVAxisDirection(self, canAlignToVDirection: bool) -> None:
        ...
    Transformer: GeometricUtilities.TransformerData


    class UVMeshManipulatorDataObjectSelectionData():
        SelectedObject: NXObject
        SelectionPosition: Point3d
        ViewDirection: Vector3d
        IsSnappedPosition: bool
        def ToString(self) -> str:
            ...
    

    class UVMeshManipulatorData_ObjectSelectionData():
        selectedObject: Tag
        selectionPosition: Point3d
        viewDirection: Vector3d
        isSnappedPosition: bool
    

class UVMappingCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateUVParameterizationBuilder(self) -> GeometricUtilities.UVMapping.UVParameterizationBuilder:
        ...
    def CreateTransformUVParameterizationData(self) -> GeometricUtilities.UVMapping.TransformUVParameterizationData:
        ...
    def CreateReverseUVParameterizationData(self) -> GeometricUtilities.UVMapping.ReverseUVParameterizationData:
        ...
    def CreateMakeSymmetricParameterizationData(self) -> GeometricUtilities.UVMapping.MakeSymmetricParameterizationData:
        ...
    def Tag(self) -> Tag: ...



class TransformUVParameterizationData(Builder):
    def __init__(self) -> None: ...
    def Update(self) -> None:
        ...
    CanMoveToolOnly: bool
    CanRelocateToolToSelection: bool
    CanReorientToolToSelection: bool
    CanScaleUniformly: bool
    UVMeshManipulator: GeometricUtilities.UVMapping.UVMeshManipulatorData


class SelectUVMeshObjectData(TaggedObject):
    def __init__(self) -> None: ...
    def ClearAndAdd(self, objects: typing.List[NXObject], view: View, point: Point3d) -> None:
        ...
    def SetCursorLocation(self, point: Point3d) -> None:
        ...
    def SetViewDirection(self, direction: Vector3d) -> None:
        ...
    def Validate(self) -> bool:
        ...
    SelectionList: SelectDisplayableObjectList


class ReverseUVParameterizationData(Builder):
    def __init__(self) -> None: ...
    CanReverseU: bool
    CanReverseV: bool
    Patches: SelectDisplayableObjectList


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MakeSymmetricParameterizationData(Builder):
    def __init__(self) -> None: ...
    Point: Point
    ReverseDirection: bool
    Type: GeometricUtilities.UVMapping.MakeSymmetricParameterizationData.Types
    UVPatches: SelectNXObject


    class Types(enum.Enum):
        SymmetryInU = 0
        SymmetryInV = 1
    

