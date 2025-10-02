from ...NXOpen import *
from ..Positioning import *

import typing
import enum

class Positioner(NXObject):
    def __init__(self) -> None: ...
    def CreateConstraint(self, persistent: bool) -> Positioning.Constraint:
        ...
    def CreateConstraint(self) -> Positioning.Constraint:
        ...
    def EstablishNetwork(self) -> Positioning.Network:
        ...
    def ClearNetwork(self) -> None:
        ...
    def DeleteNonPersistentConstraints(self) -> None:
        ...
    Constraints: Positioning.ConstraintCollection


class Network(NXObject):
    def __init__(self) -> None: ...
    def AddConstraint(self, constraint: Positioning.Constraint) -> None:
        ...
    def RemoveConstraint(self, constraint: Positioning.Constraint) -> None:
        ...
    def RemoveAllConstraints(self) -> None:
        ...
    def AddMovableObject(self, movableObject: NXObject) -> None:
        ...
    def RemoveMovableObject(self, movableObject: NXObject) -> None:
        ...
    def ApplyToModel(self) -> None:
        ...
    def Solve(self) -> None:
        ...
    def ResetDisplay(self) -> None:
        ...
    def GetMovableObjectStatus(self, movableObject: NXObject) -> Positioning.Network.ObjectStatus:
        ...
    def BeginDrag(self) -> None:
        ...
    def DragByRay(self, point: Point3d, direction: Vector3d) -> None:
        ...
    def DragByTransform(self, translation: Vector3d, rotation: Matrix3x3) -> None:
        ...
    def DragByTranslation(self, translation: Vector3d) -> None:
        ...
    def EndDrag(self) -> None:
        ...
    def SetMovingGroup(self, movableObjects: typing.List[NXObject]) -> None:
        ...
    def EmptyMovingGroup(self) -> None:
        ...
    def IsReferencedGeometryLoaded(self) -> bool:
        ...
    def LoadReferencedGeometry(self) -> None:
        ...
    DisplayComponent: Assemblies.Component
    MoveObjectsState: bool
    NonMovingGroupGrounded: bool


    class ObjectStatus(enum.Enum):
        Unknown = 0
        Fixed = 1
        OverDefined = 2
        NotConsistentDims = 3
        NotConsistentOther = 4
        NotConsistentUnknown = 5
        NotChanged = 6
        WellDefined = 7
        UnderDefined = 8
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MatingConverter(TaggedObject):
    def __init__(self) -> None: ...
    def ConvertMatingConditions(self) -> None:
        ...
    def GetConvertedConstraints(self) -> typing.List[Positioning.Constraint]:
        ...
    def GetConvertedParts(self) -> typing.List[Positioning.Constraint]:
        ...
    def GetLatestResults(self, showAllResults: bool) -> str:
        ...
    def GetResults(self, showAllResults: bool) -> str:
        ...
    def DeleteResults(self) -> None:
        ...
    def Destroy(self) -> None:
        ...
    Context: Positioning.MatingConverter.PartContext
    LoadReferencedGeometry: bool
    LoadStatus: PartLoadStatus
    NumberOfConvertedParts: int


    class PartContext(enum.Enum):
        InOwningPart = 0
        InLoadedChildren = 1
        InAllChildren = 2
    

class DisplayedConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Positioning.DisplayedConstraint]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class DisplayedConstraint(DisplayableObject):
    def __init__(self) -> None: ...
    def GetConstraint(self) -> Positioning.Constraint:
        ...
    def GetConstraintPart(self) -> Part:
        ...
    def GetContextComponent(self) -> Assemblies.Component:
        ...


class ConstraintReference(NXObject):
    def __init__(self) -> None: ...
    def GetGeometry(self) -> NXObject:
        ...
    def GetPrototypeGeometry(self) -> NXObject:
        ...
    def GetMovableObject(self) -> NXObject:
        ...
    def GetUsesGeometryAxis(self) -> bool:
        ...
    def SetFixHint(self, set: bool) -> None:
        ...
    def SetFixHintForUpdate(self, set: bool) -> None:
        ...
    def GetUsePortRotate(self) -> bool:
        ...
    def GetHasPerpendicularVector(self) -> bool:
        ...
    def GetPrototypePerpendicularVector(self) -> Vector3d:
        ...
    def SetPrototypePerpendicularVector(self, perpendicularVector: Vector3d) -> None:
        ...
    ConstraintReferenceHalfSpace: Positioning.ConstraintReference.HalfSpace
    GeometryDirectionReversed: bool
    HelpPoint: Point3d
    Order: Positioning.ConstraintReference.ConstraintOrder
    SolverGeometryType: Positioning.ConstraintReference.GeometryType
    UsePortRotateFlag: bool


    class HalfSpace(enum.Enum):
        Infer = 0
        Positive = 1
        Negative = 2
    

    class GeometryType(enum.Enum):
        Unknown = -1
        Point = 0
        Line = 1
        Circle = 2
        Plane = 3
        Cylinder = 4
        Sphere = 5
        SweepSurface = 6
        ParametricSurface = 7
        ParametricCurve = 8
        SplineCurve = 9
        Torus = 10
        Cone = 11
        Ellipse = 12
        SplineSurface = 13
        CoordinateSystem = 1001
    

    class ConstraintOrder(enum.Enum):
        Unknown = 0
        Inside = 1
        Outside = 2
    

class ConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Positioning.Constraint]:
        ...
    def __init__(self, owner: Positioning.Positioner) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class Constraint(NXObject):
    def __init__(self) -> None: ...
    def GetReferences(self) -> typing.List[Positioning.ConstraintReference]:
        ...
    def DeleteConstraintReference(self, constraintReference: Positioning.ConstraintReference) -> None:
        ...
    def CreateConstraintReference(self, movableObject: NXObject, geometry: NXObject, usesAxis: bool, isIndirect: bool) -> Positioning.ConstraintReference:
        ...
    def CreateConstraintReference(self, movableObject: NXObject, geometry: NXObject, usesAxis: bool, isIndirect: bool, usePortRotate: bool) -> Positioning.ConstraintReference:
        ...
    def EditConstraintReference(self, constraintReference: Positioning.ConstraintReference, movableObject: NXObject, geometry: NXObject, usesAxis: bool, isIndirect: bool, usePortRotate: bool) -> None:
        ...
    def FlipAlignment(self) -> None:
        ...
    def SetExpression(self, expression: str) -> None:
        ...
    def GetConstraintStatus(self) -> Positioning.Constraint.SolverStatus:
        ...
    def SetAlignmentHint(self, alignment: Positioning.Constraint.Alignment) -> None:
        ...
    def GenerateConversionReport(self, lines: str) -> None:
        ...
    def ReverseDirection(self) -> None:
        ...
    def GetDisplayedConstraint(self) -> Positioning.DisplayedConstraint:
        ...
    def Renew(self) -> None:
        ...
    def CreateCouplerReference(self, coupledConstraint: NXObject) -> Positioning.ConstraintReference:
        ...
    def EditCouplerReference(self, couplerReference: Positioning.ConstraintReference, coupledConstraint: NXObject) -> None:
        ...
    Automatic: bool
    ConstraintAlignment: Positioning.Constraint.Alignment
    ConstraintSecondAlignment: Positioning.Constraint.Alignment
    ConstraintType: Positioning.Constraint.Type
    Expression: Expression
    ExpressionDriven: bool
    LowerLimitEnabled: bool
    LowerLimitExpression: Expression
    LowerLimitRightHandSide: str
    OffsetExpression: Expression
    OffsetRightHandSide: str
    Persistent: bool
    SecondExpression: Expression
    SecondExpressionDriven: bool
    SecondExpressionRightHandSide: str
    SecondLowerLimitEnabled: bool
    SecondLowerLimitExpression: Expression
    SecondLowerLimitRightHandSide: str
    SecondUpperLimitEnabled: bool
    SecondUpperLimitExpression: Expression
    SecondUpperLimitRightHandSide: str
    SplinePointsType: Positioning.Constraint.SplineType
    Suppressed: bool
    UpperLimitEnabled: bool
    UpperLimitExpression: Expression
    UpperLimitRightHandSide: str


    class Type(enum.Enum):
        Undefined = 0
        Touch = 1
        Concentric = 2
        Fix = 3
        Distance = 4
        Parallel = 5
        Perpendicular = 6
        Center12 = 7
        Center22 = 8
        Angle = 9
        Fit = 10
        Bond = 11
        OrientAngle = 12
        SplineData = 13
        SplineLength = 14
        LinearPattern = 15
        CircularPattern = 16
        Linear2dPattern = 17
        RadiantPattern = 18
        AlignLock = 19
        CommonOffsetTransform = 20
        Hinge = 21
        Slider = 22
        Cylindrical = 23
        Ball = 24
        Screw = 25
        Gear = 26
        RackPinion = 27
        Cable = 28
    

    class SplineType(enum.Enum):
        ByPoles = 0
        ByPoints = 1
        Invalid = 2
    

    class SolverStatus(enum.Enum):
        NewlyCreated = 0
        Suppressed = 1
        OutOfDate = 2
        OverConstrained = 3
        NotConsistentDims = 4
        NotConsistentOther = 5
        NotConsistentUnknown = 6
        BetweenFixed = 7
        NotSolved = 8
        Solved = 9
        CannotSolve = 10
        Delayed = 11
        IgnoredInArrangement = 12
        InternallyInconsistent = 13
        UnloadedGeometry = 14
        PendingConvertedMc = 15
        ConflictingWithWave = 16
        InconsistentLimits = 17
        BeyondLimits = 18
    

    class Alignment(enum.Enum):
        InferAlign = 0
        CoAlign = 1
        ContraAlign = 2
    

class ComponentPositioner(Positioning.Positioner):
    def __init__(self) -> None: ...
    def BeginMoveComponent(self) -> None:
        ...
    def EndMoveComponent(self) -> None:
        ...
    def BeginAssemblyConstraints(self) -> None:
        ...
    def EndAssemblyConstraints(self) -> None:
        ...
    def BeginMoveComponentInWorkset(self) -> None:
        ...
    def EndMoveComponentInWorkset(self) -> None:
        ...
    def LoadConstraintGeometry(self, constraints: typing.List[Positioning.ComponentConstraint]) -> None:
        ...
    def SolvePostponedConstraints(self) -> None:
        ...
    DisplayConstraints: bool
    DisplaySuppressedConstraints: bool
    MoveDumbGeometry: bool
    PrimaryArrangement: Assemblies.Arrangement


class ComponentNetwork(Positioning.Network):
    def __init__(self) -> None: ...
    NetworkArrangementsMode: Positioning.ComponentNetwork.ArrangementsMode
    NetworkSolveInWorksetMode: bool


    class ArrangementsMode(enum.Enum):
        Existing = 0
        InUsed = 1
    

class ComponentConstraintGroupBuilder(Builder):
    def __init__(self) -> None: ...
    def GetContextComponent(self) -> Assemblies.Component:
        ...
    ConstraintCollectionType: Positioning.ComponentConstraintGroup.ConstraintsCollectionType
    ConstraintGroupName: str
    RememberComponentState: bool
    SelectedComponentList: SelectDisplayableObjectList
    SelectedConstraintsList: SelectDisplayableObjectList


class ComponentConstraintGroup(NXObject):
    def __init__(self) -> None: ...
    def GetMemberConstraints(self) -> typing.List[Positioning.ComponentConstraint]:
        ...
    def GetDefiningConstraints(self) -> typing.List[Positioning.ComponentConstraint]:
        ...
    def SetDefiningConstraints(self, constraints: typing.List[Positioning.ComponentConstraint]) -> None:
        ...
    def GetDefiningComponents(self) -> typing.List[Assemblies.Component]:
        ...
    def SetDefiningComponents(self, constraints: typing.List[Assemblies.Component]) -> None:
        ...
    def GetConstraintCollectionType(self) -> Positioning.ComponentConstraintGroup.ConstraintsCollectionType:
        ...
    def SetConstraintCollectionType(self, constraintCollectionType: Positioning.ComponentConstraintGroup.ConstraintsCollectionType) -> None:
        ...
    def GetRememberComponentState(self) -> bool:
        ...
    def SetRememberComponentState(self, rememberComponentState: bool) -> None:
        ...
    def UpdateMemberConstraints(self) -> bool:
        ...


    class ConstraintsCollectionType(enum.Enum):
        BetweenSelectedComponents = 0
        ConnectedToSelectedComponents = 1
    

class ComponentConstraint(Positioning.Constraint):
    def __init__(self) -> None: ...
    def RememberOnComponent(self, component: Assemblies.Component) -> None:
        ...
    def GetSpecificInArrangement(self, arrangement: Assemblies.Arrangement) -> bool:
        ...
    def SetSpecificInArrangement(self, arrangement: Assemblies.Arrangement, arrangementSpecific: bool) -> None:
        ...
    def GetSuppressedInArrangement(self, arrangement: Assemblies.Arrangement) -> bool:
        ...
    def SetSuppressedInArrangement(self, arrangement: Assemblies.Arrangement, suppressed: bool) -> None:
        ...
    def GetSharedSuppressed(self) -> bool:
        ...
    def SetSharedSuppressed(self, suppressed: bool) -> None:
        ...
    def GetInherited(self) -> bool:
        ...
    def GetDirectionToFixed(self, component: Assemblies.Component, arrangement: Assemblies.Arrangement) -> Positioning.ComponentConstraint.DirectionToFixed:
        ...
    def CopyToOverride(self) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use ComponentConstraint.CopyInheritedToOverride instead.")"""
        ...
    def CopyInheritedToOverride(self) -> Positioning.ComponentConstraint:
        ...
    def GetSeparateSuppression(self) -> bool:
        ...
    def SetSeparateSuppression(self, separateSuppression: bool) -> None:
        ...
    ArrangementSpecific: bool


    class DirectionToFixed(enum.Enum):
        Unknown = -1
        Toward = 0
        AwayFrom = 1
        NothingFixed = 2
        Fix = 3
        Suppressed = 4
        IgnoredInArrangement = 5
    

