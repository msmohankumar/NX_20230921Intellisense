from ....NXOpen import *
from ...Features import *
from ..DrawShapes import *

import typing
import enum

class TrimBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryObjects: SelectCurveList
    ExtendBound: bool
    Point: SelectDisplayableObject
    Targets: GeometricUtilities.CrayonSelectionData


class TransformData(Builder):
    def __init__(self) -> None: ...
    CanMoveToolOnly: bool
    CanRelocateToolToSelection: bool
    CanReorientToolToSelection: bool
    NumberOfCopies: int
    ObjectsToTransform: SelectNXObjectList
    ResultOption: Features.DrawShapes.TransformData.ResultOptions
    Scaling: Features.DrawShapes.TransformData.ScalingOptions
    Transformer: GeometricUtilities.TransformerData


    class ScalingOptions(enum.Enum):
        Linear = 0
        Planar = 1
        Uniform = 2
    

    class ResultOptions(enum.Enum):
        MoveOriginal = 0
        CopyOriginal = 1
    

class StartSymmetryModeBuilder(Builder):
    def __init__(self) -> None: ...
    CreateSymmetricCopiesOfExistingCurves: bool
    Plane: Plane


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MirrorData(Builder):
    def __init__(self) -> None: ...
    Objects: SelectCurveList
    Plane: Plane


class ExtendBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryObjects: SelectCurveList
    ExtendBound: bool
    Targets: GeometricUtilities.CrayonSelectionData


class EraseBuilder(Builder):
    def __init__(self) -> None: ...
    StrokeGesture: GeometricUtilities.StrokeGestureData
    Thickness: float


class EditDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    Color: NXColor
    Objects: SelectCurveList
    Thickness: DisplayableObject.ObjectWidth


class EditCurveBuilder(Builder):
    def __init__(self) -> None: ...
    def EvaluateCurve(self) -> None:
        ...
    CircleDefinitionOptions: Features.DrawShapes.EditCurveBuilder.CircleDefinitionOption
    ConstraintManager: Features.GeometricConstraintDataManager
    IsClosed: bool
    PointNumber: int
    Radius: Expression


    class CircleDefinitionOption(enum.Enum):
        ThreePoints = 0
        CenterandRadius = 1
    

class DrawStrokeData(Builder):
    def __init__(self) -> None: ...
    CanDrawOnNearestFace: bool
    Color: NXColor
    StrokeGesture: GeometricUtilities.StrokeGestureData
    Thickness: DisplayableObject.ObjectWidth


class DrawShapeData(Builder):
    def __init__(self) -> None: ...
    Associative: bool
    CoordinateSystem: CoordinateSystem
    DrawingBaseType: Features.DrawShapes.DrawShapeData.DrawingBaseTypes
    Faces: ScCollector


    class DrawingBaseTypes(enum.Enum):
        Faces = 0
        Plane = 1
    

class DrawShapeCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Features.FreeformCurveCollection) -> None: ...
    def CreateDrawShapeData(self) -> Features.DrawShapes.DrawShapeData:
        ...
    def CreateDrawStrokeData(self) -> Features.DrawShapes.DrawStrokeData:
        ...
    def CreateDrawCurveData(self) -> Features.DrawShapes.DrawCurveData:
        ...
    def CreateCurveFromStrokeData(self) -> Features.DrawShapes.CurveFromStrokeData:
        ...
    def CreateEditCurveBuilder(self, curveToEdit: Curve) -> Features.DrawShapes.EditCurveBuilder:
        ...
    def CreateEditDisplayBuilder(self) -> Features.DrawShapes.EditDisplayBuilder:
        ...
    def CreateStartSymmetryModeBuilder(self) -> Features.DrawShapes.StartSymmetryModeBuilder:
        ...
    def StopSymmetryMode(self) -> bool:
        ...
    def CreateDeleteData(self) -> Features.DrawShapes.DeleteData:
        ...
    def CreateMirrorData(self) -> Features.DrawShapes.MirrorData:
        ...
    def CreateTrimBuilder(self) -> Features.DrawShapes.TrimBuilder:
        ...
    def CreateExtendBuilder(self) -> Features.DrawShapes.ExtendBuilder:
        ...
    def CreateEraseBuilder(self) -> Features.DrawShapes.EraseBuilder:
        ...
    def CreateTransformData(self) -> Features.DrawShapes.TransformData:
        ...
    def Tag(self) -> Tag: ...



class DrawCurveData(Builder):
    def __init__(self) -> None: ...
    def SetOverSketchTolerance(self, overSketchTolerance: float) -> None:
        ...
    CanCreatePrimitives: bool
    CanDrawOnNearestFace: bool
    Color: NXColor
    DetectionSensitivity: Features.DrawShapes.DrawCurveData.DetectionSensitivityOption
    OversketchExistingCurves: bool
    Snapping: Features.DrawShapes.DrawCurveData.SnappingOption
    StrokeGesture: GeometricUtilities.StrokeGestureData
    Thickness: DisplayableObject.ObjectWidth


    class SnappingOption(enum.Enum):
        None = 0
        CurveEndPoints = 1
        IsoparametricGrid = 2
    

    class DetectionSensitivityOption(enum.Enum):
        Low = 0
        Standard = 1
        High = 2
    

class DeleteData(Builder):
    def __init__(self) -> None: ...
    Objects: SelectCurveList


class CurveFromStrokeData(Builder):
    def __init__(self) -> None: ...
    def SetMergeTolerance(self, mergeTolerance: float) -> None:
        ...
    CanCreatePrimitives: bool
    CanMergeConnectedStrokes: bool
    DetectionSensitivity: Features.DrawShapes.CurveFromStrokeData.DetectionSensitivityOption
    Strokes: SelectDisplayableObjectList


    class DetectionSensitivityOption(enum.Enum):
        Low = 0
        Standard = 1
        High = 2
    

