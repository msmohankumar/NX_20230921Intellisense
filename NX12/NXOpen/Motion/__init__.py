from ...NXOpen import *
from ..Motion import *

import typing
import enum

class VobjectCsysType(enum.Enum):
    Userdefined = 0
    Absolute = 1


class VobjectApplicationType(enum.Enum):
    ActionReaction = 0
    ActionOnly = 1


class VObject(TaggedObject):
    def __init__(self) -> None: ...
    ActionLink: Motion.SelectLink
    Applicationtype: Motion.VobjectApplicationType
    Csys: Motion.VobjectCsysType
    Direction: Direction
    DisplayScale: float
    MagFunction: CAE.Function
    MagnitudeExpression: Expression
    MagnitudeProfile: Motion.SelectFieldData
    Name: str
    Origin: Point
    ReactionLink: Motion.SelectLink
    ReferenceCsys: CoordinateSystem
    ReferenceDirection: Direction
    ReferenceLink: Motion.SelectLink
    ReferenceOrigin: Point
    ValueType: Motion.ForceValueTypes
    XExpression: Expression
    XFunction: CAE.Function
    XProfile: Motion.SelectFieldData
    YExpression: Expression
    YFunction: CAE.Function
    YProfile: Motion.SelectFieldData
    ZExpression: Expression
    ZFunction: CAE.Function
    ZProfile: Motion.SelectFieldData


class VectorTorqueCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.VectorTorque]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateVectorTorqueBuilder(self, vectortorque: Motion.VectorTorque) -> Motion.VectorTorqueBuilder:
        ...
    def FindObject(self, name: str) -> Motion.VectorTorque:
        ...
    def Tag(self) -> Tag: ...



class VectorTorqueBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    VObject: Motion.VObject


class VectorTorque(Motion.MotionObject):
    def __init__(self) -> None: ...


class VectorForceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.VectorForce]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateVectorForceBuilder(self, vectorforce: Motion.VectorForce) -> Motion.VectorForceBuilder:
        ...
    def FindObject(self, name: str) -> Motion.VectorForce:
        ...
    def Tag(self) -> Tag: ...



class VectorForceBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    VObject: Motion.VObject


class VectorForce(Motion.MotionObject):
    def __init__(self) -> None: ...


class UserDefinedSectionBuilder(Motion.BaseSectionBuilder):
    def __init__(self) -> None: ...
    Area: Expression
    InertiaIyy: Expression
    InertiaIzy: Expression
    InertiaIzz: Expression
    InertiaJ: Expression


class UserDefinedSection(Motion.BaseSection):
    def __init__(self) -> None: ...


class TirePropertyTnoCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.TirePropertyTno]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTirePropertyTnoBuilder(self, tireProperty: Motion.TirePropertyTno) -> Motion.TirePropertyTnoBuilder:
        ...
    def FindObject(self, name: str) -> Motion.TirePropertyTno:
        ...
    def Tag(self) -> Tag: ...



class TirePropertyTnoBuilder(Motion.TirePropertyBuilder):
    def __init__(self) -> None: ...
    ContactMethod: Motion.TirePropertyTnoBuilder.ContactMethodType
    Dynamics: Motion.TirePropertyTnoBuilder.DynamicsType
    Iswitch: Expression
    IswitchDefinition: Motion.TirePropertyTnoBuilder.IswitchDefinitionType
    Lkx: Expression
    Lky: Expression
    Lkyc: Expression
    Lkzc: Expression
    Lmux: Expression
    Lmuy: Expression
    Ltr: Expression
    Name: str
    SlipForces: Motion.TirePropertyTnoBuilder.SlipForcesType
    StaticHold: bool
    StaticRadius: Expression
    StaticVerticalStiffness: Expression
    TireSide: Motion.TirePropertyTnoBuilder.TireSideType
    TnoFile: str
    TrackSide: Motion.TirePropertyTnoBuilder.TrackSideType
    VerticalDamping: Expression
    VerticalStiffness: Expression


    class TrackSideType(enum.Enum):
        Left = 0
        Right = 1
    

    class TireSideType(enum.Enum):
        Left = 0
        Right = 1
        Symmetric = 2
        Mirrored = 3
    

    class SlipForcesType(enum.Enum):
        NoMagicFormula = 0
        Longitudinal = 1
        Lateral = 2
        Uncombined = 3
        Combined = 4
        TurnSlip = 5
    

    class IswitchDefinitionType(enum.Enum):
        Detailed = 0
        Integer = 1
    

    class DynamicsType(enum.Enum):
        SteadyState = 0
        RelaxationLinear = 1
        RelaxationNonLinear = 2
        RigidRing = 3
        RigidRingWithInitStatics = 4
    

    class ContactMethodType(enum.Enum):
        SmoothRoad = 0
        CircularCrossSection = 1
        MovingRoad = 2
        Road2D = 3
        Road3D = 4
    

class TirePropertyTno(Motion.TireProperty):
    def __init__(self) -> None: ...
    def CopyParameters(self, source: Motion.TirePropertyTno) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.CopyParameters instead.")"""
        ...


class TirePropertyNonInertialCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.TirePropertyNonInertial]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTirePropertyNonInertialBuilder(self, tireProperty: Motion.TirePropertyNonInertial) -> Motion.TirePropertyNonInertialBuilder:
        ...
    def FindObject(self, name: str) -> Motion.TirePropertyNonInertial:
        ...
    def Tag(self) -> Tag: ...



class TirePropertyNonInertialBuilder(Motion.TirePropertyBuilder):
    def __init__(self) -> None: ...
    AligningMomentArm: Expression
    CorneringStiffness: Expression
    DistributedContact: bool
    FrictionCoefficient: Expression
    Name: str
    NumDivisions: Expression
    Radius: Expression
    RollingResistance: Expression
    StaticHold: bool
    VerticalDamping: Expression
    VerticalStiffness: Motion.ExpressionFunctionBuilder


class TirePropertyNonInertial(Motion.TireProperty):
    def __init__(self) -> None: ...
    def CopyParameters(self, source: Motion.TirePropertyNonInertial) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.CopyParameters instead.")"""
        ...


class TirePropertyMotorcycleCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.TirePropertyMotorcycle]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTirePropertyMotorcycleBuilder(self, tireProperty: Motion.TirePropertyMotorcycle) -> Motion.TirePropertyMotorcycleBuilder:
        ...
    def FindObject(self, name: str) -> Motion.TirePropertyMotorcycle:
        ...
    def Tag(self) -> Tag: ...



class TirePropertyMotorcycleBuilder(Motion.TirePropertyBuilder):
    def __init__(self) -> None: ...
    AdvancedTab: Motion.TirePropertyAdvancedParameters
    BasicTab: Motion.TirePropertyBasicParameters
    HighOrderEffectsTab: Motion.TirePropertyHighOrderParameters


class TirePropertyMotorcycle(Motion.TireProperty):
    def __init__(self) -> None: ...
    def CopyParameters(self, source: Motion.TirePropertyMotorcycle) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.CopyParameters instead.")"""
        ...


class TirePropertyHighOrderParameters(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CarcassMass: Expression
    LateralDamping: Expression
    LateralEffects: bool
    LateralStiffness: Expression
    LongDamping: Expression
    LongStiffness: Expression
    LongitudinalEffects: bool
    RollMoment: bool
    UnloadingVerticalStiffness: Motion.MotionFunction
    UnloadingVerticalStiffnessProfile: Motion.SelectFieldData
    UnloadingVerticalStiffnessType: Motion.TirePropertyHighOrderParameters.UnloadingVertStiffType
    VerticalCarcassEffects: bool
    VerticalStiffnessTransVelocity: Expression


    class UnloadingVertStiffType(enum.Enum):
        Function = 0
        Profile = 1
    

class TirePropertyFtCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.TirePropertyFt]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTirePropertyFtBuilder(self, tireProperty: Motion.TirePropertyFt) -> Motion.TirePropertyFtBuilder:
        ...
    def FindObject(self, name: str) -> Motion.TirePropertyFt:
        ...
    def Tag(self) -> Tag: ...



class TirePropertyFtBuilder(Motion.TirePropertyBuilder):
    def __init__(self) -> None: ...
    FtireFile: str
    IdRoad: Expression
    Name: str
    Radius: Expression
    RunInParallel: bool
    StaticHold: bool
    StaticVerticalStiffness: Expression


class TirePropertyFt(Motion.TireProperty):
    def __init__(self) -> None: ...
    def CopyParameters(self, source: Motion.TirePropertyFt) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.CopyParameters instead.")"""
        ...


class TirePropertyCdCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.TirePropertyCd]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTirePropertyCdBuilder(self, tireProperty: Motion.TirePropertyCd) -> Motion.TirePropertyCdBuilder:
        ...
    def FindObject(self, name: str) -> Motion.TirePropertyCd:
        ...
    def Tag(self) -> Tag: ...



class TirePropertyCdBuilder(Motion.TirePropertyBuilder):
    def __init__(self) -> None: ...
    AmbientTempFunction: Motion.MotionFunction
    AmbientTempProfile: Motion.SelectFieldData
    AmbientTempTypeSelection: Motion.TirePropertyCdBuilder.AmbientTempType
    AmbientTempValue: Expression
    ContactKinematics: bool
    ContactLengthWidth: bool
    ContactPointGlobal: bool
    ContactPointRoadRef: bool
    CorrectorIter: Expression
    EnergyLoss: bool
    EnergyLossOfSpecificEntities: bool
    EnergyLossPerSegment: bool
    Inclination: bool
    InflationPressureFunction: Motion.MotionFunction
    InflationPressureProfile: Motion.SelectFieldData
    InflationPressureTypeSelection: Motion.TirePropertyCdBuilder.InflationPressureType
    InflationPressureValue: Expression
    ModelTypeSelection: Motion.TirePropertyCdBuilder.ModelType
    Name: str
    PrimaryParamFile: str
    RimRoadGlobal: bool
    RimRoadTydexW: bool
    RimTydexCH: bool
    RoadGlobal: bool
    SolverResults: bool
    StaticHold: bool
    StaticRadius: Expression
    StaticVerticalStiffness: Expression
    TimeStatistics: bool
    TireControlFile: str
    WearIndicatorPerSegment: bool
    WheelGlobal: bool
    WheelRoadRef: bool


    class ModelType(enum.Enum):
        Cdt30 = 0
        Cdt30Hps = 1
        Cdt40 = 2
        Cdt50 = 3
    

    class InflationPressureType(enum.Enum):
        TireParameterFile = 0
        Constant = 1
        Function = 2
        Profile = 3
    

    class AmbientTempType(enum.Enum):
        TireParameterFile = 0
        Constant = 1
        Function = 2
        Profile = 3
    

class TirePropertyCd(Motion.TireProperty):
    def __init__(self) -> None: ...
    def CopyParameters(self, source: Motion.TirePropertyCd) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.CopyParameters instead.")"""
        ...


class TirePropertyBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...


class TirePropertyBasicParameters(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CorneringStiffness: Expression
    CorneringTableFile: str
    CorneringTableProfile: Motion.SelectFieldData
    FrictionCoefficient: Expression
    LateralForceType: Motion.TirePropertyBasicParameters.CorneringType
    MagicFile: str
    Name: str
    Radius: Expression
    RollingResistance: Expression
    VerticalDamping: Motion.ExpressionFunctionBuilder
    VerticalStiffness: Motion.ExpressionFunctionBuilder


    class CorneringType(enum.Enum):
        Cornering = 0
        Carpet = 1
    

class TirePropertyBasicCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.TirePropertyBasic]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTirePropertyBasicBuilder(self, tireProperty: Motion.TirePropertyBasic) -> Motion.TirePropertyBasicBuilder:
        ...
    def FindObject(self, name: str) -> Motion.TirePropertyBasic:
        ...
    def Tag(self) -> Tag: ...



class TirePropertyBasicBuilder(Motion.TirePropertyBuilder):
    def __init__(self) -> None: ...
    AdvancedTab: Motion.TirePropertyAdvancedParameters
    BasicTab: Motion.TirePropertyBasicParameters
    HighOrderEffectsTab: Motion.TirePropertyHighOrderParameters


class TirePropertyBasic(Motion.TireProperty):
    def __init__(self) -> None: ...
    def CopyParameters(self, source: Motion.TirePropertyBasic) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.CopyParameters instead.")"""
        ...


class TirePropertyAdvancedParameters(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AligningMomentArm: Expression
    ConeIndex: Expression
    ContactAreaFunction: Motion.MotionFunction
    ContactAreaProfile: Motion.SelectFieldData
    ContactAreaType: Motion.TirePropertyAdvancedParameters.ContactType
    DistributedContact: bool
    FrictionFunction: Motion.MotionFunction
    FrictionProfile: Motion.SelectFieldData
    FrictionSurfaceFile: str
    FrictionSurfaceProfile: Motion.SelectFieldData
    FrictionType: Motion.TirePropertyAdvancedParameters.FrictType
    NumDivisions: Expression
    RelaxationLength: Expression
    RollingRadiusType: Motion.TirePropertyAdvancedParameters.RollingType
    RollingRadiusValue: Expression
    SectionHeight: Expression
    SectionWidth: Expression
    StaticHold: bool
    SurfaceType: Motion.TirePropertyAdvancedParameters.SurfType
    TransDampingDeflection: Expression


    class SurfType(enum.Enum):
        Simple = 0
        Hard = 1
        Soil = 2
        VelFrictCurve = 3
        FrictCurve = 4
        VelFrictSurface = 5
        FrictSurface = 6
    

    class RollingType(enum.Enum):
        None = 0
        Bias = 1
        Belted = 2
    

    class FrictType(enum.Enum):
        Function = 0
        Profile = 1
    

    class ContactType(enum.Enum):
        Function = 0
        Profile = 1
    

class TireProperty(Motion.MotionObject):
    def __init__(self) -> None: ...
    def SaveToFile(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.ExportParameters instead.")"""
        ...
    def LoadFromFile(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.ImportParameters instead.")"""
        ...


class TireCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Tire]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTireBuilder(self, tire: Motion.Tire) -> Motion.TireBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Tire:
        ...
    def Tag(self) -> Tag: ...



class TireBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    BodyLink: Motion.SelectLink
    BodyPoint: Point
    BodyVector: Direction
    CarrierCsys: CoordinateSystem
    CarrierLink: Motion.SelectLink
    CarrierPoint: Point
    ChassisCsys: CoordinateSystem
    ChassisLink: Motion.SelectLink
    ChassisPoint: Point
    Name: str
    PropertyBasic: Motion.SelectTirePropertyBasic
    PropertyCd: Motion.SelectTirePropertyCd
    PropertyFTire: Motion.SelectTirePropertyFt
    PropertyMotorcycle: Motion.SelectTirePropertyMotorcycle
    PropertyNonInertial: Motion.SelectTirePropertyNonInertial
    PropertyTno: Motion.SelectTirePropertyTno
    Road: Motion.SelectRoad
    TireType: Motion.TireBuilder.Type


    class Type(enum.Enum):
        Basic = 0
        Tno = 1
        CDTire = 2
        FTire = 3
        Motorcycle = 4
        NonInertial = 5
    

class Tire(Motion.MotionObject):
    def __init__(self) -> None: ...


class TextBasedElementCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.TextBasedElement]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTextBasedElementBuilder(self, textBasedElement: Motion.TextBasedElement) -> Motion.TextBasedElementBuilder:
        ...
    def FindObject(self, name: str) -> Motion.TextBasedElement:
        ...
    def Tag(self) -> Tag: ...



class TextBasedElementBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Definition: str
    Type: Motion.TextBasedElementBuilder.TypeChoices


    class TypeChoices(enum.Enum):
        ThreePointForce = 0
        ThreePointTorque = 1
        AllKinematicDirectionSensor = 2
        AllForceDirectionSensor = 3
        AeroAeroForce = 4
        AeroHydroForce = 5
        AeroVehicleForce = 6
        CustomizedSolver = 7
        StiTire = 8
        StiTireProperty = 9
        BumpStopContact = 10
        SphereToGroundContact = 11
        GearContact = 12
        ThreeLinkSuspension = 13
        FourLinkSuspension = 14
        FiveLinkSuspension = 15
        RollIaxSuspension = 16
        SteerIaxSuspension = 17
        HotchKissSuspension = 18
        McPhersonSuspension = 19
        DoubleAArmSuspension = 20
        PivotBeamSuspension = 21
        Vehicle = 22
        SpeedSweep = 23
        SystemProperty = 24
        DynamicProperty = 25
        KinematicProperty = 26
        StaticProperty = 27
        PreloadProperty = 28
        InverseProperty = 29
        LinearizationProperty = 30
        RestartProperty = 31
        AdvancedSolution = 32
        Gear = 33
        Generic = 34
        Fmi = 35
        PointToPointConstraint = 36
        OrientationConstraint = 37
        FunctioncurveControlInput = 38
        PathFollowerControlInput = 39
        UserDefinedControlInput = 40
        SpecialControlInput = 41
        LinearControlOutput = 42
        MassPropertyControlOutput = 43
        LinkInitialCondition = 44
        ScrewJointOrSpringInitialCondition = 45
        FlexibleLinkInitialCondition = 46
        TireInitialCondition = 47
        StaticVehicleAlignment = 48
        SprungMass = 49
        UserDefinedForce = 50
        GlobalDirectionsLinkDriver = 51
        DotOneLinkDriver = 52
        DotTwoLinkDriver = 53
        CurveOnCurveConstraintDriver = 54
        FixedJointDriver = 55
        LinkCouplerDriver = 56
        LinkDriver = 57
        JointDriver = 58
        LinkControlOutput = 59
        JointOrConstraintControlOutput = 60
        Amesim = 61
        Matlab = 62
    

class TextBasedElement(Motion.MotionObject):
    def __init__(self) -> None: ...


class SubmechanismPositionerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.SubmechanismPositioner]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePositionerBuilder(self, positioner: Motion.SubmechanismPositioner) -> Motion.SubmechanismPositionerBuilder:
        ...
    def FindObject(self, name: str) -> Motion.SubmechanismPositioner:
        ...
    def Tag(self) -> Tag: ...



class SubmechanismPositionerBuilder(Builder):
    def __init__(self) -> None: ...
    ChildCsys: SelectCoordinateSystem
    Name: str
    ParentCsys: SelectCoordinateSystem
    Submechanism: Assemblies.SelectComponent


class SubmechanismPositioner(DisplayableObject):
    def __init__(self) -> None: ...


class StandardSectionBuilder(Motion.BaseSectionBuilder):
    def __init__(self) -> None: ...
    Dim1: Expression
    Dim2: Expression
    Dim3: Expression
    Dim4: Expression
    Dim5: Expression
    Dim6: Expression
    SectionType: Motion.StandardSectionBuilder.StandardSectionType


    class StandardSectionType(enum.Enum):
        Rod = 0
        Tube = 1
        Bar = 2
        Box = 3
        Box1 = 4
        I = 5
        I1 = 6
        T = 7
        T1 = 8
        T2 = 9
        Chan = 10
        Chan1 = 11
        Chan2 = 12
        Hat = 13
        Hat1 = 14
        H = 15
        L = 16
        Z = 17
        Hexa = 18
        Cross = 19
    

class StandardSection(Motion.BaseSection):
    def __init__(self) -> None: ...


class SpringCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Spring]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSpringBuilder(self, spring: Motion.Spring) -> Motion.SpringBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Spring:
        ...
    def Tag(self) -> Tag: ...



class SpringBuilder(Motion.ConnectorBuilder):
    def __init__(self) -> None: ...
    ActuatorCurveProfile: Motion.SelectFieldData
    ActuatorForceExpression: Expression
    ActuatorFunction: CAE.Function
    ActuatorMomentExpression: Expression
    ActuatorType: Motion.ConnectorCoefficientTypes
    CoefficientCurveProfile: Motion.SelectFieldData
    CoefficientExpression: Expression
    CoefficientFunction: CAE.Function
    CoefficientType: Motion.ConnectorCoefficientTypes
    CreateDamper: bool
    DamperAppDirection: Motion.ConnectorBuilder.ApplicationDirection
    DamperCustomizedSolver: bool
    DamperName: str
    FreeAngleExpression: Expression
    FreeLengthExpression: Expression
    InitialLengthExpression: Expression
    LengthFlag: bool
    Name: str
    PreloadAngleExpression: Expression
    PreloadExpression: Expression
    PreloadForceExpression: Expression
    PreloadMomentExpression: Expression
    PreloadedAngleExpression: Expression
    PreloadedLengthExpression: Expression
    SpringAppDirection: Motion.ConnectorBuilder.ApplicationDirection
    SpringCustomizedSolver: bool
    StiffnessCurveProfile: Motion.SelectFieldData
    StiffnessExpression: Expression
    StiffnessFunction: CAE.Function
    StiffnessSurfaceProfile: Motion.SelectFieldData
    StiffnessType: Motion.ConnectorCoefficientTypes
    TorsionalCoefficientExpression: Expression
    TorsionalStiffnessExpression: Expression


class Spring(Motion.Connector):
    def __init__(self) -> None: ...


class SpreadsheetRunControl(Motion.PostControl):
    def __init__(self) -> None: ...
    def Finish(self) -> None:
        ...
    def StepTo(self, step: int) -> None:
        ...
    def Solve(self) -> None:
        ...
    def StepForward(self) -> None:
        ...
    def StepBackward(self) -> None:
        ...
    def StepToDesignPosition(self) -> None:
        ...
    def StepToAssemblyPosition(self) -> None:
        ...
    def Stop(self) -> None:
        ...
    def UpdateFromSpreadsheet(self) -> None:
        ...
    def QuitSpreadsheet(self) -> None:
        ...
    ActiveView: Motion.ActiveView
    Delay: int
    JointsLimits: bool
    PlayMode: int


class SplineBeamPropertyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.SplineBeamProperty]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSplineBeamPropertyBuilder(self, splineBeamProperty: Motion.SplineBeamProperty) -> Motion.SplineBeamPropertyBuilder:
        ...
    def FindObject(self, name: str) -> Motion.SplineBeamProperty:
        ...
    def Tag(self) -> Tag: ...



class SplineBeamPropertyBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    AsyTimoshenkoCorrection: Expression
    AszTimoshenkoCorrection: Expression
    CustomizedMaterial: Motion.CustomizedMaterialBuilder
    DampingRatio: Expression
    DampingType: Motion.SplineBeamPropertyBuilder.DampingTypes
    IsBeamCrossDamping: bool
    Name: str


    class DampingTypes(enum.Enum):
        Viscous = 0
        Structural = 1
    

class SplineBeamProperty(Motion.MotionObject):
    def __init__(self) -> None: ...


class SplineBeamCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.SplineBeam]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSplineBeamBuilder(self, splineBeam: Motion.SplineBeam) -> Motion.SplineBeamBuilder:
        ...
    def FindObject(self, name: str) -> Motion.SplineBeam:
        ...
    def Tag(self) -> Tag: ...



class SplineBeamBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def InsertEmptyPoint(self, index: int) -> None:
        ...
    def AssignPoint(self, index: int, point: Point) -> None:
        ...
    def RemovePoint(self, index: int) -> None:
        ...
    def SwapPoints(self, index1: int, index2: int) -> None:
        ...
    def GeneratePoints(self) -> None:
        ...
    def ImportPointsFromFile(self, filePath: str) -> None:
        ...
    def ExportPointsToFile(self, filePath: str) -> None:
        ...
    def GetMarkerItems(self) -> typing.List[Motion.MarkerToNodeData]:
        ...
    def RemoveAllMarkers(self) -> None:
        ...
    def CreateMarkerToNode(self, marker: NXObject, markerPosition: int, pointID: int, useClosestNode: bool) -> Motion.MarkerToNodeData:
        ...
    Curves: SelectCurveList
    DefinitionMethod: Motion.SplineBeamBuilder.DefinitionMethodType
    Link: Motion.SelectLink
    Name: str
    NumberOfSections: Expression
    PointList: PointList
    SectionAxis: Motion.SplineBeamBuilder.SectionAxisType
    SectionShape: Motion.SelectBaseSection
    SectionVector: Direction
    StructuralProperty: Motion.SelectSplineBeamProperty
    Tolerance: Expression


    class SectionAxisType(enum.Enum):
        Y = 0
        Z = 1
    

    class DefinitionMethodType(enum.Enum):
        Manual = 0
        Curve = 1
    

class SplineBeam(Motion.MotionObject):
    def __init__(self) -> None: ...


class SignalChartListItemList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Motion.SignalChartListItem]) -> None:
        ...
    def Append(self, object: Motion.SignalChartListItem) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Motion.SignalChartListItem) -> int:
        ...
    def FindItem(self, index: int) -> Motion.SignalChartListItem:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Motion.SignalChartListItem) -> None:
        ...
    def Erase(self, obj: Motion.SignalChartListItem, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Motion.SignalChartListItem]:
        ...
    def SetContents(self, objects: typing.List[Motion.SignalChartListItem]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Motion.SignalChartListItem, object2: Motion.SignalChartListItem) -> None:
        ...
    def Insert(self, location: int, object: Motion.SignalChartListItem) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SignalChartListItem(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AlwaysEvaluated: bool
    DelayTimeExpression: Expression
    EventCondition: Motion.SignalChartListItem.Condition
    Sensor: Motion.MotionSensor
    SignalExpression: Expression
    ThresholdExpression: Expression
    TimeSensor: Motion.SignalChartListItem.Timer


    class Timer(enum.Enum):
        Timer = 0
        AbsoluteTime = 1
        Undefined = 2
    

    class Condition(enum.Enum):
        LessThan = 0
        GreaterThan = 1
    

class SignalChartCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.SignalChart]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSignalChartBuilder(self, signalchart: Motion.SignalChart) -> Motion.SignalChartBuilder:
        ...
    def CreateSignalChartListItem(self) -> Motion.SignalChartListItem:
        ...
    def FindObject(self, name: str) -> Motion.SignalChart:
        ...
    def Tag(self) -> Tag: ...



class SignalChartBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def NewListItemExpression(self, sensor: Motion.MotionSensor, alwaysEvaluated: bool, timeSensor: int, condition: int, threshold: Expression, delayTime: Expression, signal: Expression) -> Motion.SignalChartListItem:
        ...
    ClosedSignalList: Motion.SignalChartListItemList
    InitialSignalExpression: Expression
    Name: str
    OpenSignalFunction: CAE.Function
    SignalChartType: Motion.SignalChartBuilder.Type


    class Type(enum.Enum):
        OpenLoop = 0
        ClosedLoop = 1
    

class SignalChart(NXObject):
    def __init__(self) -> None: ...


class SelectTirePropertyTno(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.TirePropertyTno, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.TirePropertyTno, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyTno, view1: View, point1: Point3d, selection2: Motion.TirePropertyTno, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyTno, view1: View, point1: Point3d, selection2: Motion.TirePropertyTno, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.TirePropertyTno, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.TirePropertyTno:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.TirePropertyTno


class SelectTirePropertyNonInertial(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.TirePropertyNonInertial, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.TirePropertyNonInertial, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyNonInertial, view1: View, point1: Point3d, selection2: Motion.TirePropertyNonInertial, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyNonInertial, view1: View, point1: Point3d, selection2: Motion.TirePropertyNonInertial, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.TirePropertyNonInertial, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.TirePropertyNonInertial:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.TirePropertyNonInertial


class SelectTirePropertyMotorcycle(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.TirePropertyMotorcycle, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.TirePropertyMotorcycle, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyMotorcycle, view1: View, point1: Point3d, selection2: Motion.TirePropertyMotorcycle, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyMotorcycle, view1: View, point1: Point3d, selection2: Motion.TirePropertyMotorcycle, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.TirePropertyMotorcycle, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.TirePropertyMotorcycle:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.TirePropertyMotorcycle


class SelectTirePropertyFt(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.TirePropertyFt, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.TirePropertyFt, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyFt, view1: View, point1: Point3d, selection2: Motion.TirePropertyFt, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyFt, view1: View, point1: Point3d, selection2: Motion.TirePropertyFt, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.TirePropertyFt, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.TirePropertyFt:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.TirePropertyFt


class SelectTirePropertyCd(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.TirePropertyCd, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.TirePropertyCd, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyCd, view1: View, point1: Point3d, selection2: Motion.TirePropertyCd, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyCd, view1: View, point1: Point3d, selection2: Motion.TirePropertyCd, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.TirePropertyCd, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.TirePropertyCd:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.TirePropertyCd


class SelectTirePropertyBasic(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.TirePropertyBasic, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.TirePropertyBasic, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyBasic, view1: View, point1: Point3d, selection2: Motion.TirePropertyBasic, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.TirePropertyBasic, view1: View, point1: Point3d, selection2: Motion.TirePropertyBasic, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.TirePropertyBasic, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.TirePropertyBasic:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.TirePropertyBasic


class SelectSplineBeamProperty(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.SplineBeamProperty, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.SplineBeamProperty, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.SplineBeamProperty, view1: View, point1: Point3d, selection2: Motion.SplineBeamProperty, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.SplineBeamProperty, view1: View, point1: Point3d, selection2: Motion.SplineBeamProperty, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.SplineBeamProperty, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.SplineBeamProperty:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.SplineBeamProperty


class SelectRoad(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.Road, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.Road, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Road, view1: View, point1: Point3d, selection2: Motion.Road, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Road, view1: View, point1: Point3d, selection2: Motion.Road, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.Road, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.Road:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.Road


class SelectMarker(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.Marker, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.Marker, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Marker, view1: View, point1: Point3d, selection2: Motion.Marker, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Marker, view1: View, point1: Point3d, selection2: Motion.Marker, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.Marker, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.Marker:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.Marker


class SelectLink(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.Link, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.Link, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Link, view1: View, point1: Point3d, selection2: Motion.Link, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Link, view1: View, point1: Point3d, selection2: Motion.Link, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.Link, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.Link:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.Link


class SelectJoint(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.Joint, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.Joint, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Joint, view1: View, point1: Point3d, selection2: Motion.Joint, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.Joint, view1: View, point1: Point3d, selection2: Motion.Joint, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.Joint, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.Joint:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.Joint


class SelectFieldData(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.FieldData, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.FieldData, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.FieldData, view1: View, point1: Point3d, selection2: Motion.FieldData, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.FieldData, view1: View, point1: Point3d, selection2: Motion.FieldData, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.FieldData, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.FieldData:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.FieldData


class SelectControlPort(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.ControlPort, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.ControlPort, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.ControlPort, view1: View, point1: Point3d, selection2: Motion.ControlPort, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.ControlPort, view1: View, point1: Point3d, selection2: Motion.ControlPort, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.ControlPort, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.ControlPort:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.ControlPort


class SelectBaseSection(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.BaseSection, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.BaseSection, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.BaseSection, view1: View, point1: Point3d, selection2: Motion.BaseSection, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.BaseSection, view1: View, point1: Point3d, selection2: Motion.BaseSection, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.BaseSection, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.BaseSection:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.BaseSection


class SelectAnalyticalContactProperty(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Motion.AnalyticalContactProperty, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Motion.AnalyticalContactProperty, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.AnalyticalContactProperty, view1: View, point1: Point3d, selection2: Motion.AnalyticalContactProperty, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Motion.AnalyticalContactProperty, view1: View, point1: Point3d, selection2: Motion.AnalyticalContactProperty, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Motion.AnalyticalContactProperty, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Motion.AnalyticalContactProperty:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Motion.AnalyticalContactProperty


class SegmentCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Segment]:
        ...
    def __init__(self, owner: Motion.Road) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Motion.Segment:
        ...
    def Tag(self) -> Tag: ...



class SegmentBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Motion.SegmentBuilder]) -> None:
        ...
    def Append(self, object: Motion.SegmentBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Motion.SegmentBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Motion.SegmentBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Motion.SegmentBuilder) -> None:
        ...
    def Erase(self, obj: Motion.SegmentBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Motion.SegmentBuilder]:
        ...
    def SetContents(self, objects: typing.List[Motion.SegmentBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Motion.SegmentBuilder, object2: Motion.SegmentBuilder) -> None:
        ...
    def Insert(self, location: int, object: Motion.SegmentBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SegmentBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Angle: Expression
    BankAngleCurve: Motion.MotionFunction
    BankAngleCurveProfile: Motion.SelectFieldData
    ConstantRadiusBankAngle: Expression
    ConstantRadiusElevationChange: Expression
    LaneChangeElevationChange: Expression
    LaneChangeForwardLength: Expression
    LateralAmplitude: Expression
    LateralShiftLength: Expression
    Length: Expression
    Name: str
    NumberOfPylons: Expression
    Radius: Expression
    SegmentType: Motion.SegmentBuilder.TypeChoices
    SlalomElevationChange: Expression
    SlalomForwardLength: Expression
    SplineType: Motion.SegmentBuilder.SplineDatatypeChoices
    StraightElevationChange: Expression
    TransitionType: Motion.SegmentBuilder.StraightTransitionTypeChoices
    YCurve: Motion.MotionFunction
    YCurveProfile: Motion.SelectFieldData
    ZCurve: Motion.MotionFunction
    ZCurveProfile: Motion.SelectFieldData


    class TypeChoices(enum.Enum):
        Straight = 0
        ConstantRadius = 1
        LaneChange = 2
        Slalom = 3
        UserDefined = 4
    

    class StraightTransitionTypeChoices(enum.Enum):
        Linear = 0
        Cubic = 1
    

    class SplineDatatypeChoices(enum.Enum):
        Function = 0
        Profile2D = 1
    

class Segment(NXObject):
    def __init__(self) -> None: ...


class ScalarTorqueCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ScalarTorque]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateScalarTorqueBuilder(self, scalarTorque: Motion.ScalarTorque) -> Motion.ScalarTorqueBuilder:
        ...
    def FindObject(self, name: str) -> Motion.ScalarTorque:
        ...
    def Tag(self) -> Tag: ...



class ScalarTorqueBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ActionCsys: CoordinateSystem
    ActionLink: Motion.SelectLink
    ActionPoint: Point
    ApplicationType: Motion.ScalarTorqueBuilder.AppType
    BaseCsys: CoordinateSystem
    BaseLink: Motion.SelectLink
    BasePoint: Point
    Direction: Motion.ScalarTorqueBuilder.DirectionType
    Function: CAE.Function
    Joint: Motion.SelectJoint
    Name: str
    Profile: Motion.SelectFieldData
    TorqueType: Motion.ScalarTorqueBuilder.ScalarTorqueType
    ValueExpression: Expression
    ValueType: Motion.ForceValueTypes


    class ScalarTorqueType(enum.Enum):
        Joint = 0
        Link = 1
    

    class DirectionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class AppType(enum.Enum):
        ActionReaction = 0
        ActionOnly = 1
    

class ScalarTorque(Motion.MotionObject):
    def __init__(self) -> None: ...


class ScalarForceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ScalarForce]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateScalarForceBuilder(self, scalarForce: Motion.ScalarForce) -> Motion.ScalarForceBuilder:
        ...
    def FindObject(self, name: str) -> Motion.ScalarForce:
        ...
    def Tag(self) -> Tag: ...



class ScalarForceBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ActionCsys: CoordinateSystem
    ActionLink: Motion.SelectLink
    ActionPoint: Point
    Applicationtype: Motion.ScalarForceBuilder.ApplicationType
    Direction: Motion.ScalarForceBuilder.DirectionType
    Function: CAE.Function
    Name: str
    Profile: Motion.SelectFieldData
    ReactionCsys: CoordinateSystem
    ReactionLink: Motion.SelectLink
    ReactionPoint: Point
    ValueExpression: Expression
    ValueType: Motion.ForceValueTypes


    class DirectionType(enum.Enum):
        Translational = 0
        X = 1
        Y = 2
        Z = 3
    

    class ApplicationType(enum.Enum):
        ActionReaction = 0
        ActionOnly = 1
    

class ScalarForce(Motion.MotionObject):
    def __init__(self) -> None: ...


class RoadCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Road]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateRoadBuilder(self, road: Motion.Road) -> Motion.RoadBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Road:
        ...
    def Tag(self) -> Tag: ...



class RoadBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def CreateSegmentBuilder(self) -> Motion.SegmentBuilder:
        ...
    def GetSegmentBuilder(self, segmentBuilderIndex: int) -> Motion.SegmentBuilder:
        ...
    def RemoveSegmentBuilder(self, segment: Motion.SegmentBuilder) -> None:
        ...
    def RemoveAllSegmentBuilders(self) -> None:
        ...
    def SwapSegment(self, firstSegment: Motion.SegmentBuilder, secondSegment: Motion.SegmentBuilder) -> None:
        ...
    BankAngleCurve: Motion.MotionFunction
    BankAngleCurveProfile: Motion.SelectFieldData
    Color: NXColor
    Csys: CoordinateSystem
    GridDensity: Expression
    Length: Expression
    Link: Motion.SelectLink
    Name: str
    PathDatatype: Motion.RoadBuilder.PathDatatypeChoices
    PathFileName: str
    ReferencePoint: Point
    RoadObject: Motion.Road
    RoadType: Motion.RoadBuilder.TypeChoices
    SegmentBuilderList: Motion.SegmentBuilderList
    ShowVisualization: bool
    SplineCurve: Motion.MotionFunction
    SplineCurveProfile: Motion.SelectFieldData
    SplineType: Motion.RoadBuilder.SplineDatatypeChoices
    SurfaceDatatype: Motion.RoadBuilder.SurfaceDatatypeChoices
    SurfaceFileName: str
    SurfaceProfile: Motion.SelectFieldData
    Width: Expression
    XCurve: Motion.MotionFunction
    XCurveProfile: Motion.SelectFieldData
    XSegmentOriginCoord: Expression
    YCurve: Motion.MotionFunction
    YCurveProfile: Motion.SelectFieldData
    YSegmentOriginCoord: Expression
    ZCurve: Motion.MotionFunction
    ZCurveProfile: Motion.SelectFieldData
    ZSegmentOriginCoord: Expression


    class TypeChoices(enum.Enum):
        Surface = 0
        Path = 1
    

    class SurfaceDatatypeChoices(enum.Enum):
        SplineCurve = 0
        SplineSurface = 1
        Rsm1000 = 2
        Rsm1002 = 3
        Rsm2000 = 4
        Rsm3000 = 5
        OpenCRG = 6
        RoadDataFile = 7
        Profile2D = 8
    

    class SplineDatatypeChoices(enum.Enum):
        Function = 0
        Profile2D = 1
    

    class PathDatatypeChoices(enum.Enum):
        SplineCurves = 0
        Segments = 1
        FileImport = 2
    

class Road(Motion.MotionObject):
    def __init__(self) -> None: ...
    Segments: Motion.SegmentCollection


class ResultMeasureCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ResultMeasure]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateResultMeasureBuilder(self, resultMeasure: Motion.ResultMeasure) -> Motion.ResultMeasureBuilder:
        ...
    def Find(self, name: str) -> Motion.ResultMeasure:
        ...
    def UpdateResultMeasures(self, resultMeasure: typing.List[Motion.ResultMeasure]) -> None:
        ...
    def DeleteResultMeasures(self, resultMeasure: typing.List[Motion.ResultMeasure]) -> None:
        ...
    def Tag(self) -> Tag: ...



class ResultMeasureBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitResultMeasure(self) -> TaggedObject:
        ...
    ExpName: str
    InterferenceType: Motion.ResultMeasure.InterferenceType
    ReferenceObject: SelectNXObject
    ResultType: Motion.ResultMeasure.ResultType
    Solution: Motion.MotionSolution


class ResultMeasure(TaggedObject):
    def __init__(self) -> None: ...
    def GetExpressionObject(self) -> Expression:
        ...


    class ResultType(enum.Enum):
        Interference = 0
        Measure = 1
        GraphObject = 2
        Time = 3
    

    class InterferenceType(enum.Enum):
        Condition = 0
        Result = 1
    

class RecurdynSolverProperty(TaggedObject):
    def __init__(self) -> None: ...
    CosimSampleTimeExpression: Expression
    CosimSimModel: str
    DynamicErrorToleranceExpression: Expression
    DynamicInitialStepSizeExpression: Expression
    DynamicMaxKinIteration: int
    DynamicMaxStepSizeExpression: Expression
    DynamicNumericalDampingExpression: Expression
    RedundantViolationToleranceForAngleExpression: Expression
    RedundantViolationToleranceForLengthExpression: Expression
    StaticErrorToleranceExpression: Expression
    StaticInitialStepSizeExpression: Expression
    StaticIntegratorType: Motion.RecurdynSolverProperty.StaticIntegratorTypes
    StaticMaxIteration: int
    StaticMaxStepSizeExpression: Expression
    StaticStabilityExpression: Expression


    class StaticIntegratorTypes(enum.Enum):
        NewtonRapson = 0
        RobustNewtonRapson = 1
    

class PostToolsControl(NXObject):
    def __init__(self) -> None: ...
    def Finish(self) -> None:
        ...
    def CalculateMeasure(self, measure: Motion.PackagingMeasure) -> None:
        ...
    def CalculateMeasures(self, measures: typing.List[Motion.PackagingMeasure]) -> None:
        ...


class PostProcess(Utilities.NXRemotableObject):
    def __init__(self, owner: Motion.MotionSession) -> None: ...
    def CaptureArrangement(self, arrangementName: str, animationStep: int) -> Assemblies.Arrangement:
        ...
    def CaptureArrangement(self, arrangementName: str, arrangementType: int, animationStep: int) -> Assemblies.Arrangement:
        ...
    def CreateEnvelope(self, tPostControl: Motion.IPostControl, destinationPart: NXObject, addToRefSets: bool, referenceFrameObj: NXObject, sourceObjs: typing.List[NXObject], stepFrom: int, stepTo: int, toleranceSetting: Motion.PostProcess.EnvelopeTolerance, sweptBodies: typing.List[NXObject], skipedObj: typing.List[NXObject], failedObjs: typing.List[NXObject], aborted: bool) -> None:
        ...
    def UpdateDesignPosition(self) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  This functionality is no longer supported.")"""
        ...
    def CreateSequence(self, sequenceName: str) -> NXObject:
        ...
    def TraceCurrentPosition(self) -> None:
        ...
    def TraceEntireMechanism(self) -> None:
        ...
    def TraceIntersectionCurve(self) -> None:
        ...
    def ExplodeMechanism(self, explosionName: str) -> Assemblies.Explosion:
        ...
    def ExportToMovie(self, movieName: str) -> None:
        ...
    def ListMeasure(self) -> None:
        ...
    def ListInterference(self) -> None:
        ...
    def GetInterferenceOption(self) -> bool:
        ...
    def SetInterferenceOption(self, interferenceOn: bool) -> None:
        ...
    def GetMeasureOption(self) -> bool:
        ...
    def SetMeasureOption(self, measureOn: bool) -> None:
        ...
    def GetTraceOption(self) -> bool:
        ...
    def SetTraceOption(self, traceOn: bool) -> None:
        ...
    def GetStopOnEventOption(self) -> bool:
        ...
    def SetStopOnEventOption(self, stopOnEventOn: bool) -> None:
        ...
    def GetSpeed(self) -> int:
        ...
    def SetSpeed(self, speed: int) -> None:
        ...
    def RegisterUserButton(self, buttonName: str, buttonTips: str, buttonMenuScriptName: str, functionBeforeUIDestroy: Motion.PostProcess.UserFunctionBeforeDialogDestroy) -> None:
        ...
    def ExportRealTimeMovie(self, movieName: str) -> None:
        ...
    def Tag(self) -> Tag: ...



    

    class EnvelopeToleranceTypes(enum.Enum):
        Percentage = 0
        Absolute = 1
    

    class PostProcessEnvelopeTolerance():
        AccuracyMode: Motion.PostProcess.EnvelopeAccuracyModes
        ToleranceType: Motion.PostProcess.EnvelopeToleranceTypes
        Tolerance: float
        DecimationEnabled: bool
        DecimationFactor: float
        DecimationMaxError: float
        def ToString(self) -> str:
            ...
    

    class EnvelopeAccuracyModes(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
        Custom = 3
    

class PostControl(NXObject):
    def __init__(self) -> None: ...


class PortVariableList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Motion.PortVariable]) -> None:
        ...
    def Append(self, object: Motion.PortVariable) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Motion.PortVariable) -> int:
        ...
    def FindItem(self, index: int) -> Motion.PortVariable:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Motion.PortVariable) -> None:
        ...
    def Erase(self, obj: Motion.PortVariable, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Motion.PortVariable]:
        ...
    def SetContents(self, objects: typing.List[Motion.PortVariable]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Motion.PortVariable, object2: Motion.PortVariable) -> None:
        ...
    def Insert(self, location: int, object: Motion.PortVariable) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PortVariableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ControlPort]:
        ...
    def __init__(self, owner: Motion.Mechatronics) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Motion.ControlPort:
        ...
    def Tag(self) -> Tag: ...



class PortVariable(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    AssociatedPortName: str
    Name: str
    Port: Motion.ControlPort
    Unit: int


class PortAssociation(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Name: str
    Offset: Expression
    ScaleFactor: Expression


class PointOnSurfaceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.PointOnSurface]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePointOnSurfaceBuilder(self, pointonsurface: Motion.PointOnSurface) -> Motion.PointOnSurfaceBuilder:
        ...
    def FindObject(self, name: str) -> Motion.PointOnSurface:
        ...
    def Tag(self) -> Tag: ...



class PointOnSurfaceBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def SetFaces(self, faces: typing.List[Face]) -> None:
        ...
    Link: Motion.SelectLink
    Name: str
    Point: Point


class PointOnSurface(Motion.MotionObject):
    def __init__(self) -> None: ...


class PointOnCurveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.PointOnCurve]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePointOnCurveBuilder(self, pointOnCurve: Motion.PointOnCurve) -> Motion.PointOnCurveBuilder:
        ...
    def FindObject(self, name: str) -> Motion.PointOnCurve:
        ...
    def Tag(self) -> Tag: ...



class PointOnCurveBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def GetCurves(self) -> typing.List[NXObject]:
        ...
    def SetCurves(self, curves: typing.List[NXObject]) -> None:
        ...
    CurveParameterizedType: Motion.CurveParameterizedTypes
    Link: Motion.SelectLink
    Name: str
    Point: Point
    SpacingExpression: Expression


class PointOnCurve(Motion.MotionObject):
    def __init__(self) -> None: ...


class PMDCMotorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.PMDCMotor]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePmdcMotorBuilder(self, pmdcMotor: Motion.PMDCMotor) -> Motion.PMDCMotorBuilder:
        ...
    def FindObject(self, name: str) -> Motion.PMDCMotor:
        ...
    def Tag(self) -> Tag: ...



class PMDCMotorBuilder(Motion.MotorBuilder):
    def __init__(self) -> None: ...
    DampingCoefficient: float
    InductanceExpression: Expression
    InitialCurrentExpression: Expression
    InitialSpeed: float
    MotorType: Motion.PMDCMotorBuilder.Type
    Name: str
    NominalVoltageExpression: Expression
    ResistanceExpression: Expression
    RotorInteria: float
    VoltageConstantExpression: Expression


    class Type(enum.Enum):
        WithRotor = 0
        WithoutRotor = 1
    

class PMDCMotor(Motion.Motor):
    def __init__(self) -> None: ...


class PlayMode(enum.Enum):
    PlayOnce = 0
    Loop = 1
    Retrace = 2


class PlantOutputCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.PlantOutput]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePlantOutputBuilder(self, platoutput: Motion.PlantOutput) -> Motion.PlantOutputBuilder:
        ...
    def FindObject(self, name: str) -> Motion.PlantOutput:
        ...
    def Tag(self) -> Tag: ...



class PlantOutputBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Function: CAE.Function
    Name: str
    Sensor: NXObject
    Type: Motion.PlantOutputBuilder.Poutype


    class Poutype(enum.Enum):
        Func = 0
        Sensor = 1
    

class PlantOutput(NXObject):
    def __init__(self) -> None: ...


class PlantInputCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.PlantInput]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePlantInputBuilder(self, plantinput: Motion.PlantInput) -> Motion.PlantInputBuilder:
        ...
    def FindObject(self, name: str) -> Motion.PlantInput:
        ...
    def Tag(self) -> Tag: ...



class PlantInputBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Name: str


class PlantInput(NXObject):
    def __init__(self) -> None: ...


class PhysicsConversionBuilder(Builder):
    def __init__(self) -> None: ...
    def ActiveAll(self) -> None:
        ...
    def DeactiveAll(self) -> None:
        ...
    def GetPhysics(self, physicsProto: typing.List[NXObject], partOccurrence: typing.List[Assemblies.Component]) -> None:
        ...
    def UpdateStatus(self, physicsProto: typing.List[NXObject], partOccurrence: typing.List[Assemblies.Component], active: bool) -> None:
        ...


class ParamRedefineState(enum.Enum):
    NotRedefined = 0
    Redefined = 1


class PackagingTraceBuilder(Motion.PackagingBuilder):
    def __init__(self) -> None: ...
    def GetRelativeLinks(self) -> typing.List[DisplayableObject]:
        ...
    def SetRelativeLinks(self, links: typing.List[DisplayableObject]) -> None:
        ...
    FrameType: Motion.PackagingTraceBuilder.Frame
    TargetLayer: int


    class Frame(enum.Enum):
        Absolute = 0
        Relative = 1
    

class PackagingTrace(Motion.Packaging):
    def __init__(self) -> None: ...


class PackagingMeasureBuilder(Motion.PackagingBuilder):
    def __init__(self) -> None: ...
    def GetList2(self) -> typing.List[DisplayableObject]:
        ...
    def SetList2(self, list2: typing.List[DisplayableObject]) -> None:
        ...
    def GetSourceList(self, sourceGeometryData: typing.List[Motion.PackagingMeasureBuilder.GeometryData]) -> None:
        ...
    def SetSourceList(self, sourceGeometryData: typing.List[Motion.PackagingMeasureBuilder.GeometryData]) -> None:
        ...
    def GetTargetList(self, targetGeometryData: typing.List[Motion.PackagingMeasureBuilder.GeometryData]) -> None:
        ...
    def SetTargetList(self, targetGeometryData: typing.List[Motion.PackagingMeasureBuilder.GeometryData]) -> None:
        ...
    Condition: Motion.PackagingMeasureBuilder.MeasureCondition
    MsType: Motion.PackagingMeasureBuilder.MeasureType
    StopOnEvent: bool
    ThresholdAngleExpression: Expression
    ThresholdExpression: Expression
    ToleranceAngleExpression: Expression
    ToleranceExpression: Expression


    class MeasureType(enum.Enum):
        MinimumDistance = 0
        Angle = 1
    

    class MeasureCondition(enum.Enum):
        LessThan = 0
        GreaterThan = 1
        EqualTo = 2
    

    class PackagingMeasureBuilderGeometryData():
        Geometry: DisplayableObject
        Point: Point3d
        Vector: Vector3d
        Direction: Direction
        def ToString(self) -> str:
            ...
    

class PackagingMeasure(Motion.Packaging):
    def __init__(self) -> None: ...


class PackagingInterferenceBuilder(Motion.PackagingBuilder):
    def __init__(self) -> None: ...
    def GetList2(self) -> typing.List[DisplayableObject]:
        ...
    def SetList2(self, list2: typing.List[DisplayableObject]) -> None:
        ...
    def GetRelativeLinks(self) -> typing.List[DisplayableObject]:
        ...
    def SetRelativeLinks(self, links: typing.List[DisplayableObject]) -> None:
        ...
    ActionType: Motion.PackagingInterferenceBuilder.Action
    ClearanceExpression: Expression
    FrameType: Motion.PackagingInterferenceBuilder.Frame
    ModeType: Motion.PackagingInterferenceBuilder.Mode
    StopOnEvent: bool


    class Mode(enum.Enum):
        Faceted = 0
        PreciseSolid = 1
    

    class Frame(enum.Enum):
        Absolute = 0
        FirstSet = 1
        SecondSet = 2
        BothSets = 3
        Selected = 4
    

    class Action(enum.Enum):
        Highlight = 0
        CreateSolids = 1
        ShowIntersectionCurve = 2
    

class PackagingInterference(Motion.Packaging):
    def __init__(self) -> None: ...


class PackagingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Packaging]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateInterferenceBuilder(self, interference: Motion.PackagingInterference) -> Motion.PackagingInterferenceBuilder:
        ...
    def CreateMeasureBuilder(self, measure: Motion.PackagingMeasure) -> Motion.PackagingMeasureBuilder:
        ...
    def CreateTraceBuilder(self, trace: Motion.PackagingTrace) -> Motion.PackagingTraceBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Packaging:
        ...
    def SetDistanceMeausreBodyOnlyFilterStatus(self, enableBodyOnly: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class PackagingBuilder(Builder):
    def __init__(self) -> None: ...
    def GetList1(self) -> typing.List[DisplayableObject]:
        ...
    def SetList1(self, list1: typing.List[DisplayableObject]) -> None:
        ...
    Enable: bool
    Name: str


class Packaging(NXObject):
    def __init__(self) -> None: ...


class OutputPortAssociationList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Motion.OutputPortAssociation]) -> None:
        ...
    def Append(self, object: Motion.OutputPortAssociation) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Motion.OutputPortAssociation) -> int:
        ...
    def FindItem(self, index: int) -> Motion.OutputPortAssociation:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Motion.OutputPortAssociation) -> None:
        ...
    def Erase(self, obj: Motion.OutputPortAssociation, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Motion.OutputPortAssociation]:
        ...
    def SetContents(self, objects: typing.List[Motion.OutputPortAssociation]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Motion.OutputPortAssociation, object2: Motion.OutputPortAssociation) -> None:
        ...
    def Insert(self, location: int, object: Motion.OutputPortAssociation) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class OutputPortAssociation(Motion.PortAssociation):
    def __init__(self) -> None: ...
    AssociatedPortName: str
    Port: Motion.ControlPort


class NormalModeProperty(NXObject):
    def __init__(self) -> None: ...
    Active: bool
    Frequency: float
    Hysteretic: float
    Mass: float
    ModeId: int
    PhysicalHysteretic: float
    PhysicalViscous: float
    RxMass: float
    RyMass: float
    RzMass: float
    Stiffness: float
    Viscous: float
    XMass: float
    YMass: float
    ZMass: float


class MotorBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...


class Motor(Motion.MotionObject):
    def __init__(self) -> None: ...


class MotionSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.MotionSolution]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSolutionBuilder(self, solution: Motion.MotionSolution) -> Motion.MotionSolutionBuilder:
        ...
    def FindObject(self, name: str) -> Motion.MotionSolution:
        ...
    def GetActiveSolution(self) -> Motion.MotionSolution:
        ...
    def SetActiveSolution(self, activeSolution: Motion.MotionSolution) -> None:
        ...
    def DeleteSolution(self, tSolution: Motion.MotionSolution, ifDeleteResult: bool) -> None:
        ...
    def CreateAdvancedSolutionBuilder(self, advancedSolution: Motion.AdvancedSolution) -> Motion.AdvancedSolutionBuilder:
        ...
    def Tag(self) -> Tag: ...



class MotionSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    AdamsSolverProperty: Motion.AdamsSolverProperty
    AnalysisType: Motion.MotionSolutionBuilder.AnalysisTypes
    Description: str
    GravityValueExpression: Expression
    GravityVector: Direction
    IsSkipStep: bool
    LmsSolverProperty: Motion.LmsSolverProperty
    Name: str
    RecurdynSolverProperty: Motion.RecurdynSolverProperty
    SkipSteps: str
    SolutionType: Motion.MotionSolutionBuilder.SolutionTypes
    StaticAnalysis: bool
    Step: int
    TimeExpression: Expression


    class SolutionTypes(enum.Enum):
        Normal = 0
        Articulation = 1
        Spreadsheet = 2
        Flexbody = 3
    

    class AnalysisTypes(enum.Enum):
        Dynamic = 0
        Static = 1
        Control = 2
    

class MotionSolution(NXObject):
    def __init__(self) -> None: ...
    def SolveNormalRunSolution(self) -> None:
        ...
    def ExportMotionHostCosimMfiles(self) -> None:
        ...
    def EditRunsimulinkMfile(self) -> None:
        ...
    def ExportSimulinkHostCosimMfiles(self) -> None:
        ...
    def CalculateGrueblerCount(self) -> int:
        ...
    def AddObject(self, object: NXObject) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Motion.MotionSolution.RemoveSuppressedObject")"""
        ...
    def RemoveObject(self, object: NXObject) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Motion.MotionSolution.AddSuppressedObject")"""
        ...
    def AddSuppressedObject(self, object: NXObject) -> None:
        ...
    def RemoveSuppressedObject(self, object: NXObject) -> None:
        ...
    def RemoveSuppressedObject(self, motionObject: NXObject, forceOk: bool) -> None:
        ...
    def GetIsSuppressed(self, objectTag: NXObject) -> bool:
        ...
    def GetName(self) -> str:
        ...
    def SetName(self, solutionName: str, renameResultFile: bool) -> None:
        ...
    def GetAnimationControl(self) -> Motion.AnimationControl:
        ...
    def GetArticulationControl(self) -> Motion.ArticulationControl:
        ...
    def GetSpreadsheetRunControl(self, spreadsheetName: str) -> Motion.SpreadsheetRunControl:
        ...
    def GetLoadTransferControl(self) -> Motion.LoadTransferControl:
        ...
    def GetPostToolsControl(self) -> Motion.PostToolsControl:
        ...
    def GetGraphObjectResult(self, graph: Motion.Graph, resultPoints: float, unit: Unit) -> None:
        ...
    def SaveGraphObjectToSpreadsheet(self, xGraph: Motion.Graph, yGraphs: typing.List[Motion.Graph], showGraph: bool, writeTime: bool) -> None:
        ...
    def SaveGraphObjectToAfu(self, fileName: str, xGraph: Motion.Graph, yGraph: Motion.Graph) -> None:
        ...
    def LoadResult(self) -> None:
        ...
    def ExportSolverInputFile(self) -> None:
        ...


class MotionSimulation(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def SaveSimulation(self, masterPart: NXObject, motionSimName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.BasePart.Save")"""
        ...
    def SaveSimulation(self, masterPart: NXObject, motionSimPart: NXObject) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.BasePart.Save")"""
        ...
    def LoadSimulation(self, masterPart: NXObject, motionSimName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.PartCollection.OpenDisplay and NXOpen.Motion.MotionSession.InitializeSimulation")"""
        ...
    def UnloadSimulation(self, masterPart: NXObject, motionSimName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.BasePart.Close")"""
        ...
    def UnloadSimulation(self, masterPart: NXObject, motionSimPart: NXObject) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.BasePart.Close")"""
        ...
    def RenameSimulation(self, masterPart: NXObject, oldMotionSimName: str, newMotionSimName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.BasePart.SaveAs")"""
        ...
    def CalculateGrueblerCount(self, motionPart: NXObject) -> int:
        ...
    def ExportRecurdynSdk(self, fullFileName: str) -> None:
        ...
    def AddMaster(self, motionPart: Part, masterPart: NXObject) -> None:
        ...
    def RemoveMaster(self, motionPart: Part, deleteMotionObjects: bool) -> None:
        ...
    def GetMasterCadPart(self, motionPart: Part) -> Part:
        ...
    def RenameSubmechanism(self, submechanism: NXObject, name: str) -> None:
        ...
    def ReadDeactivatedStates(self, sumbmechanism: NXObject, solution: Motion.MotionSolution) -> None:
        ...
    def CreateAddSubmechanismBuilder(self, part: NXObject) -> Motion.AddSubmechanismBuilder:
        ...
    def AddSuppressedObjectForAllSolutions(self, motionPart: Part, obj: NXObject) -> None:
        ...
    def RemoveSuppressedObjectForAllSolutions(self, motionPart: Part, obj: NXObject) -> None:
        ...
    def Tag(self) -> Tag: ...



class MotionSession(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CloneSimulation(self, masterPart: NXObject, motionSimName: str) -> str:
        ...
    def DeleteSimulation(self, masterPart: NXObject, motionSimName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def CreateSimulation(self, masterPart: NXObject) -> str:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.FileNew and NXOpen.Motion.MotionSession.InitializeSimulation")"""
        ...
    def CreateNamingSimulation(self, masterPart: NXObject, inputSimName: str) -> str:
        ...
    def DirectOpenSimulation(self, motionSimName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.PartCollection.OpenDisplay and NXOpen.Motion.MotionSession.InitializeSimulation")"""
        ...
    def ReparentSimulation(self, motionSimFullName: str, destinationDirectory: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def InitializeMechanisms(self) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Motion.MotionSession.InitializeSimulation")"""
        ...
    def InitializeSimulation(self, simulationPart: Part) -> None:
        ...
    def ConstraintsToMotionObject(self, scenarioPart: NXObject, masterPart: NXObject) -> NXObject:
        ...
    def FixLinkToGround(self, link: NXObject) -> NXObject:
        ...
    def GetScenarioNames(self, masterPart: NXObject) -> str:
        ...
    def GetFullName(self, masterPart: NXObject, scenarioName: str) -> str:
        ...
    def CreatePhysicsConversionBuilder(self, scenarioPart: NXObject) -> Motion.PhysicsConversionBuilder:
        ...
    def ExportProcessSimulateKinematics(self) -> None:
        ...
    def GetAdoptionManager(self, scenarioPart: NXObject) -> Motion.AdoptionManager:
        ...
    def GetReferencingMotionObjects(self, scenarioPart: NXObject, originObject: NXObject) -> typing.List[NXObject]:
        ...
    def GetReferencedMotionObjects(self, scenarioPart: NXObject, originObject: NXObject) -> typing.List[NXObject]:
        ...
    def GetReferencingFunctions(self, scenarioPart: NXObject, originObject: NXObject) -> typing.List[Motion.MotionFunction]:
        ...
    def GetReferencedFunctions(self, scenarioPart: NXObject, originObject: NXObject) -> typing.List[Motion.MotionFunction]:
        ...
    def GetFunctionReferencingMotionObjects(self, scenarioPart: NXObject, funcObject: Motion.MotionFunction) -> typing.List[NXObject]:
        ...
    def GetFunctionReferencedMotionObjects(self, scenarioPart: NXObject, funcObject: Motion.MotionFunction) -> typing.List[NXObject]:
        ...
    def Tag(self) -> Tag: ...

    Environments: Motion.MotionEnvironment
    PostProcess: Motion.PostProcess
    MotionMethods: Motion.MotionMethods
    MechanismImport: Motion.MechanismImport
    MechanismExport: Motion.MechanismExport


class MotionSensorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.MotionSensor]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMotionSensorBuilder(self, sensor: Motion.MotionSensor) -> Motion.MotionSensorBuilder:
        ...
    def FindObject(self, name: str) -> Motion.MotionSensor:
        ...
    def Tag(self) -> Tag: ...



class MotionSensorBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ComponentType: Motion.MotionSensorBuilder.Component
    MeasurementObject: SelectNXObject
    Name: str
    ReferenceFrame: Motion.MotionSensorBuilder.Reference
    ReferenceMarker: Motion.SelectMarker
    RelativeMarker: Motion.SelectMarker
    Type: Motion.MotionSensorBuilder.Types


    class Types(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
        Force = 3
    

    class Reference(enum.Enum):
        Absolute = 0
        Relative = 1
        UserDefined = 2
    

    class Component(enum.Enum):
        LinearMagnitude = 0
        X = 1
        Y = 2
        Z = 3
        AngularMagnitude = 4
        Rx = 5
        Ry = 6
        Rz = 7
    

class MotionSensor(Motion.MotionObject):
    def __init__(self) -> None: ...


class MotionObject(DisplayableObject):
    def __init__(self) -> None: ...
    DisplayScale: float
    GroupName: str
    GroupTypeOption: Motion.MotionObject.GroupType


    class GroupType(enum.Enum):
        None = 0
        Import = 1
    

class MotionMethods(Utilities.NXRemotableObject):
    def __init__(self, owner: Motion.MotionSession) -> None: ...
    def CopyConnectorParameters(self, sourceConnector: NXObject, destinationConnector: NXObject) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use MotionMethods.CopyParameters instead.")"""
        ...
    def ModelCheck(self, listWarning: bool) -> None:
        ...
    def CopyParameters(self, source: NXObject, destination: NXObject) -> None:
        ...
    def ExportParameters(self, entity: NXObject, fileName: str) -> None:
        ...
    def ImportParameters(self, entity: NXObject, fileName: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class MotionManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def Tag(self) -> Tag: ...

    Joints: Motion.JointCollection
    Links: Motion.LinkCollection
    JointDrivers: Motion.JointDriverCollection
    ScalarForces: Motion.ScalarForceCollection
    ScalarTorques: Motion.ScalarTorqueCollection
    Graphs: Motion.GraphManager
    SignalCharts: Motion.SignalChartCollection
    PMDCMotors: Motion.PMDCMotorCollection
    MotionSolutions: Motion.MotionSolutionCollection
    BodyContacts: Motion.BodyContactCollection
    CurveContacts: Motion.CurveContactCollection
    PointOnSurfaces: Motion.PointOnSurfaceCollection
    PointOnCurves: Motion.PointOnCurveCollection
    CurveOnCurves: Motion.CurveOnCurveCollection
    VectorForces: Motion.VectorForceCollection
    VectorTorques: Motion.VectorTorqueCollection
    Couplers: Motion.CouplerCollection
    MotionSensors: Motion.MotionSensorCollection
    PlantOutputs: Motion.PlantOutputCollection
    PlantInputs: Motion.PlantInputCollection
    Springs: Motion.SpringCollection
    Dampers: Motion.DamperCollection
    Bushings: Motion.BushingCollection
    FlexBodies: Motion.FlexBodyCollection
    GeneralCouplers: Motion.GeneralCouplerCollection
    LoadTransfers: Motion.LoadTransferCollection
    AdoptionPairs: Motion.AdoptionPairCollection
    ResultMeasures: Motion.ResultMeasureCollection
    Roads: Motion.RoadCollection
    ControlInputs: Motion.ControlInputCollection
    Tires: Motion.TireCollection
    TirePropertiesFt: Motion.TirePropertyFtCollection
    TirePropertiesTno: Motion.TirePropertyTnoCollection
    TirePropertiesCd: Motion.TirePropertyCdCollection
    ControlOutputs: Motion.ControlOutputCollection
    Mechatronics: Motion.MechatronicsCollection
    LinkDrivers: Motion.LinkDriverCollection
    TirePropertiesBasic: Motion.TirePropertyBasicCollection
    TirePropertiesMotorcycle: Motion.TirePropertyMotorcycleCollection
    TirePropertiesNonInertial: Motion.TirePropertyNonInertialCollection
    LinkCouplers: Motion.LinkCouplerCollection
    AnalyticalContacts: Motion.AnalyticalContactCollection
    AnalyticalContactPropertys: Motion.AnalyticalContactPropertyCollection
    FieldDatas: Motion.FieldDataCollection
    TextBasedElements: Motion.TextBasedElementCollection
    SplineBeams: Motion.SplineBeamCollection
    SplineBeamProperties: Motion.SplineBeamPropertyCollection
    BeamForces: Motion.BeamForceCollection
    SubmechanismPositioners: Motion.SubmechanismPositionerCollection
    BeamSections: Motion.BaseSectionCollection


class MotionFunction(CAE.Function):
    def __init__(self) -> None: ...


class MotionEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Motion.MotionSession) -> None: ...
    def SetAnalysisType(self, analysisType: Motion.MotionEnvironment.Analysis) -> None:
        ...
    def SetJointWizardStatus(self, setting: Motion.MotionEnvironment.JointWizardStatus) -> None:
        ...
    def GetJointWizardStatus(self) -> Motion.MotionEnvironment.JointWizardStatus:
        ...
    def SetAdoptAssemblyJointStatus(self, setting: Motion.MotionEnvironment.AdoptAssemblyJointStatus) -> None:
        ...
    def GetAdoptAssemblyJointStatus(self) -> Motion.MotionEnvironment.AdoptAssemblyJointStatus:
        ...
    def CheckMotorLicense(self, checkMotorLicense: bool) -> None:
        ...
    def CheckCosimLicense(self, checkCosimLicense: bool) -> None:
        ...
    def CheckFlexbodyLicense(self, checkFlexbodyLicense: bool) -> None:
        ...
    def SetComponentBasedMechanism(self, componentBasedMech: bool) -> None:
        ...
    def SetSolver(self, solver: Motion.MotionEnvironment.Solver) -> None:
        ...
    def GetSolver(self) -> Motion.MotionEnvironment.Solver:
        ...
    def EnableMechatronics(self, enableMechatronicsLicense: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def EnableLmsflexbody(self, enableLmsflexbody: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def EnableStdtire(self, enableStdtire: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def EnableTnotire(self, enableTnotiree: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def EnableSwifttire(self, enableSwifttire: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def EnableCdtire(self, enableCdtire: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Removed without replacement.")"""
        ...
    def Tag(self) -> Tag: ...



    class Solver(enum.Enum):
        None = -1
        Recurdyn = 0
        Adams = 1
        Simcenter = 2
        Lms = 2
        ScDesigner = 3
    

    class JointWizardStatus(enum.Enum):
        Undefined = -1
        Off = 0
        On = 1
    

    class Analysis(enum.Enum):
        NoType = 0
        Kinematics = 1
        Dynamics = 2
    

    class AdoptAssemblyJointStatus(enum.Enum):
        Undefined = -1
        Off = 0
        On = 1
    

class MotionBuilder(Builder):
    def __init__(self) -> None: ...
    DisplayScale: float
    GroupName: str
    GroupType: Motion.MotionObject.GroupType


class MechatronicsPortCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ControlPort]:
        ...
    def __init__(self, owner: Motion.Mechatronics) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Motion.ControlPort:
        ...
    def Tag(self) -> Tag: ...



class MechatronicsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Mechatronics]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateMechatronicsBuilder(self, mechatronics: Motion.Mechatronics) -> Motion.MechatronicsBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Mechatronics:
        ...
    def Tag(self) -> Tag: ...



class MechatronicsBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def ReadInterfaceFromFile(self, filePath: str) -> None:
        ...
    def RefreshLists(self) -> None:
        ...
    def GetParameterGroupNames(self) -> str:
        ...
    def GetPortVariableGroupNames(self) -> str:
        ...
    def GetInput(self, inputName: str) -> Motion.InputPortAssociation:
        ...
    def GetOutput(self, inputName: str) -> Motion.OutputPortAssociation:
        ...
    def GetPortVariable(self, inputName: str) -> Motion.PortVariable:
        ...
    def GetConfigurationParameter(self, inputName: str) -> Motion.ConfigurationParameter:
        ...
    def NewOutputListItem(self) -> Motion.OutputPortAssociation:
        ...
    def NewInputListItem(self) -> Motion.InputPortAssociation:
        ...
    ActiveParameterGroupName: str
    ActivePortVariableGroupName: str
    CommunicationInterval: Expression
    CommunicationIntervalType: Motion.MechatronicsBuilder.SolverCommunicationIntervalType
    ConfigurationParametersList: Motion.ConfigurationParameterList
    HeaderFile: str
    InputPortsList: Motion.InputPortAssociationList
    IntegrationType: Motion.MechatronicsBuilder.SolverIntegrationType
    MechatronicsType: Motion.MechatronicsBuilder.MechatronicsModelType
    ModelFile: str
    Name: str
    OutputPortsList: Motion.OutputPortAssociationList
    PortVariablesList: Motion.PortVariableList
    Purpose: Motion.MechatronicsBuilder.PurposeType


    class SolverIntegrationType(enum.Enum):
        CoSimulation = 0
        ModelExchange = 1
    

    class SolverCommunicationIntervalType(enum.Enum):
        Constant = 0
        Variable = 1
    

    class PurposeType(enum.Enum):
        Import = 0
        Export = 1
    

    class MechatronicsModelType(enum.Enum):
        Amesim = 0
        Matlab = 1
    

class Mechatronics(Motion.MotionObject):
    def __init__(self) -> None: ...
    PortVariables: Motion.PortVariableCollection
    Outputs: Motion.MechatronicsPortCollection


class MechanismImport(Utilities.NXRemotableObject):
    def __init__(self, owner: Motion.MotionSession) -> None: ...
    def ImportMdef(self, workPart: NXObject, fileName: str, namingRule: Motion.MechanismImport.NamingRule, addString: str, reportToInfoWindow: bool, replaceExistingElements: bool) -> None:
        ...
    def ImportXML(self, workPart: Part, fileName: str, namingRule: Motion.MechanismImport.NamingRule, appendixString: str, reportToInfoWindow: bool) -> None:
        ...
    def ImportFromSubassembly(self, compOcc: Assemblies.Component, motionPart: Part, workPart: Part, namingRule: Motion.MechanismImport.NamingRule, appendixString: str, reportToInfoWindow: bool, abortOnFailure: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



    class NamingRule(enum.Enum):
        None = 0
        AddPrefix = 1
        AddSuffix = 2
    

class MechanismExport(Utilities.NXRemotableObject):
    def __init__(self, owner: Motion.MotionSession) -> None: ...
    def ExportMdef(self, fileName: str, posOrientFormat: Motion.MechanismExport.PositionOrientationFormat, exportEmptyInputFields: bool, exportUnusedOptions: bool, exportSubmechAsMdef: bool, enablePublish: bool, publishedFolder: str, objects: typing.List[NXObject]) -> None:
        ...
    def ExportPlmxml(self, fileName: str, objects: typing.List[NXObject]) -> None:
        ...
    def Tag(self) -> Tag: ...



    class PositionOrientationFormat(enum.Enum):
        TransformationMatrix = 0
        Pqr = 1
        BryantAngles = 2
        EulerAngles = 3
        EulerParameters = 4
    

class MarkerToNodeData(TaggedObject):
    def __init__(self) -> None: ...
    def GetNodeLocation(self) -> float:
        ...
    def SetNodeLocation(self, nodeLocation: float) -> None:
        ...
    def GetUseClosestNode(self) -> bool:
        ...
    def SetUseClosestNode(self, useClosestNode: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Marker: NXObject
    MarkerPosition: int
    Move: bool
    NodeId: int


class MarkerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Marker]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, name: str, subtype: Motion.Marker.MarkerType, link: Motion.Link, origin: Point, orientation: NXMatrix) -> Motion.Marker:
        ...
    def FindObject(self, name: str) -> Motion.Marker:
        ...
    def CreateMarkerBuilder(self, marker: Motion.Marker) -> Motion.MarkerBuilder:
        ...
    def Tag(self) -> Tag: ...



class MarkerBuilder(Builder):
    def __init__(self) -> None: ...
    Csys: CoordinateSystem
    DisplayScale: float
    Name: str
    OriginPoint: Point
    SelectLink: SelectNXObject


class Marker(DisplayableObject):
    def __init__(self) -> None: ...


    class MarkerType(enum.Enum):
        Undefined = 0
        Inertia = 1
        UserDefined = 2
        CenterOfMass = 3
    

class LoadTransferControl(NXObject):
    def __init__(self) -> None: ...
    def SetRigidLink(self, link: Motion.Link) -> None:
        ...
    def SetFlexibleLink(self, link: Motion.FlexBody) -> None:
        ...
    def SetSplineBeam(self, link: Motion.SplineBeam) -> None:
        ...
    def SetViewPort(self, viewPort: int) -> None:
        ...
    def SetLoadVectorScale(self, scale: float, updateDisplay: bool) -> None:
        ...
    def SetAnimationCurrentStep(self, step: int) -> None:
        ...
    def AnimationStepForward(self) -> None:
        ...
    def AnimationStepBackward(self) -> None:
        ...
    def PlayAnimation(self) -> None:
        ...
    def StopAnimation(self) -> None:
        ...
    def UpdateFromSpreadsheet(self) -> None:
        ...
    def ExportToSpreadsheet(self) -> None:
        ...
    def Finish(self) -> None:
        ...


class LoadTransferCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.LoadTransfer]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLoadTransferBuilder(self, loadTransfer: Motion.LoadTransfer) -> Motion.LoadTransferBuilder:
        ...
    def FindObject(self, name: str) -> Motion.LoadTransfer:
        ...
    def Tag(self) -> Tag: ...



class LoadTransferBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def GetRecordedSteps(self) -> int:
        ...
    def SetRecordedSteps(self, steps: int) -> None:
        ...
    def CreateGraphObjects(self) -> typing.List[Motion.Graph]:
        ...
    def StoreGraphInAfu(self, afu: str) -> None:
        ...
    Link: SelectNXObjectList
    VectorScale: float


class LoadTransfer(Motion.MotionObject):
    def __init__(self) -> None: ...


class LmsSolverProperty(TaggedObject):
    def __init__(self) -> None: ...
    AssemblyTolerance: Expression
    DoubleArraySize: int
    DynamicInitialVelocityMethod: int
    DynamicIntegrationTolerance: Expression
    DynamicMaxIntegrationStep: Expression
    DynamicSolutionTolerance: Expression
    DynamicSolverAccelerationMethod: int
    IntArraySize: int
    KinematicSolutionTolerance: Expression
    LuTolerance: Expression
    RoadHeightAdjustment: Motion.LmsSolverProperty.RoadHeightAdjustmentTypes
    StaticForceTolerance: Expression
    StaticJacobianType: int
    StaticQuasiIteration: int
    StaticSolutionTolerance: Expression
    StaticStepSize: Expression


    class StaticJacobianTypes(enum.Enum):
        Exact = 0
        Finite = 1
    

    class RoadHeightAdjustmentTypes(enum.Enum):
        None = 0
        Road = 1
        Vehicle = 2
    

    class DynamicInitialVelocityMethods(enum.Enum):
        Qr = 0
        MoorePenrosePseudoinverse = 1
        MinimumKineticEnergy = 2
    

    class DynamicAccelerationMethods(enum.Enum):
        Banded = 0
        Harwell = 1
        Iterative = 2
    

class LinkMassProperty(TaggedObject):
    def __init__(self) -> None: ...
    InertiaCsys: CoordinateSystem
    IxxExpression: Expression
    IxyExpression: Expression
    IxzExpression: Expression
    IyyExpression: Expression
    IyzExpression: Expression
    IzzExpression: Expression
    MassCenter: Point
    MassExpression: Expression
    MassType: Motion.LinkMassProperty.MassPropertyType


    class MassPropertyType(enum.Enum):
        Automatic = 0
        UserDefined = 1
        None = 2
    

class LinkInitialVelocity(TaggedObject):
    def __init__(self) -> None: ...
    RotateCsys: CoordinateSystem
    RotateExpression: Expression
    RotateType: Motion.LinkInitialVelocity.AngularVelocityType
    RotateVector: Direction
    TranslateExpression: Expression
    TranslateVector: Direction
    WxExpression: Expression
    WyExpression: Expression
    WzExpression: Expression


    class AngularVelocityType(enum.Enum):
        Magnitude = 0
        Component = 1
    

class LinkDriverCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.LinkDriver]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLinkDriverBuilder(self, linkDriver: Motion.LinkDriver) -> Motion.LinkDriverBuilder:
        ...
    def FindObject(self, name: str) -> Motion.LinkDriver:
        ...
    def Tag(self) -> Tag: ...



class LinkDriverBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ActionLinkAttachment: Motion.LinkAttachmentData
    BaseLinkAttachment: Motion.LinkAttachmentData
    DriverMotions: Motion.DriverMotionsData
    Name: str


class LinkDriver(Motion.MotionObject):
    def __init__(self) -> None: ...


class LinkCouplerCoupleBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ActionLinkAttachment: Motion.LinkAttachmentData
    BaseLinkAttachment: Motion.LinkAttachmentData
    MeasurementType: Motion.LinkCouplerCoupleBuilder.MeasurementChoices
    ScaleExpression: Expression
    ScaleFunction: Motion.MotionFunction
    ScaleProfile: Motion.SelectFieldData
    ScaleType: Motion.LinkCouplerCoupleBuilder.ScaleChoices


    class ScaleChoices(enum.Enum):
        Expression = 0
        Function = 1
        Profile = 2
    

    class MeasurementChoices(enum.Enum):
        Translation = 0
        Rotation = 1
        Distance = 2
    

class LinkCouplerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.LinkCoupler]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLinkCouplerBuilder(self, linkCoupler: Motion.LinkCoupler) -> Motion.LinkCouplerBuilder:
        ...
    def FindObject(self, name: str) -> Motion.LinkCoupler:
        ...
    def Tag(self) -> Tag: ...



class LinkCouplerBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Curve: Motion.MotionFunction
    CurveProfile: Motion.SelectFieldData
    CurveType: Motion.LinkCouplerBuilder.CurveChoices
    FirstCouple: Motion.LinkCouplerCoupleBuilder
    Method: Motion.LinkCouplerBuilder.MethodChoices
    Name: str
    SecondCouple: Motion.LinkCouplerCoupleBuilder
    Type: Motion.LinkCouplerBuilder.TypeChoices


    class TypeChoices(enum.Enum):
        TwoLink = 0
        ThreeLink = 1
        FourLink = 2
    

    class MethodChoices(enum.Enum):
        Scales = 0
        CouplingCurve = 1
    

    class CurveChoices(enum.Enum):
        Function = 0
        Profile = 1
    

class LinkCoupler(Motion.MotionObject):
    def __init__(self) -> None: ...


class LinkCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Link]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateLinkBuilder(self, link: Motion.Link) -> Motion.LinkBuilder:
        ...
    def CreateFixedJoint(self, link: Motion.Link) -> Motion.Joint:
        ...
    def FindObject(self, name: str) -> Motion.Link:
        ...
    def Tag(self) -> Tag: ...



class LinkBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Fixed: bool
    Geometries: SelectNXObjectList
    InitialVelocity: Motion.LinkInitialVelocity
    MassProperty: Motion.LinkMassProperty
    Name: str


class LinkAttachmentData(TaggedObject):
    def __init__(self) -> None: ...
    def GetOrientation(self) -> Matrix3x3:
        ...
    def Validate(self) -> bool:
        ...
    Csys: CoordinateSystem
    Link: Motion.SelectLink
    Origin: Point
    Vector: Direction


class Link(Motion.MotionObject):
    def __init__(self) -> None: ...


class JointFrictionRecurDyn(TaggedObject):
    def __init__(self) -> None: ...
    BallRadiusExpression: Expression
    BendMoment: bool
    BendingArmExpression: Expression
    Effect: Motion.JointFrictionRecurDyn.FrictionEffect
    EnableForce: bool
    EnableTorque: bool
    ForcePreloadExpression: Expression
    FrictionArmExpression: Expression
    InitialOverlapExpression: Expression
    MaxFrictionForceExpression: Expression
    MaxFrictionTorqueExpression: Expression
    MaxStictionDeformationExpression: Expression
    MuDynamicExpression: Expression
    MuStaticExpression: Expression
    OverlapDelta: Motion.JointFrictionRecurDyn.FrictionOverlapDelta
    PinRadiusExpression: Expression
    Preload: bool
    ReactionArmExpression: Expression
    ReactionForce: bool
    StaticEqu: bool
    StictionTransitionVelocityExpression: Expression
    TorquePreloadExpression: Expression
    TorsionalMoment: bool
    YokeType: Motion.JointFrictionRecurDyn.FrictionYokeType


    class FrictionYokeType(enum.Enum):
        I = 0
        J = 1
    

    class FrictionOverlapDelta(enum.Enum):
        Constant = 0
        Increase = 1
        Decrease = 2
    

    class FrictionEffect(enum.Enum):
        All = 0
        Stiction = 1
        Sliding = 2
    

class JointFrictionLms(TaggedObject):
    def __init__(self) -> None: ...
    BallRadius: Expression
    BendingReactionArm: Expression
    FrictionArm: Expression
    InitialOverlap: Expression
    MuDynamic: Expression
    MuStatic: Expression
    PinRadius: Expression
    ReactionArm: Expression
    RotationalStictionTransitionVelocity: Expression
    TranslationalStictionTransitionVelocity: Expression


class JointFrictionAdams(TaggedObject):
    def __init__(self) -> None: ...
    BallRadiusExpression: Expression
    BendMoment: bool
    BendingArmExpression: Expression
    Effect: Motion.JointFrictionAdams.FrictionEffect
    ForcePreloadExpression: Expression
    FrictionArmExpression: Expression
    InitialOverlapExpression: Expression
    MaxStictionDeformationExpression: Expression
    MuDynamicExpression: Expression
    MuStaticExpression: Expression
    OverlapDelta: Motion.JointFrictionAdams.FrictionOverlapDelta
    PinRadiusExpression: Expression
    Preload: bool
    ReactionArmExpression: Expression
    ReactionForce: bool
    StaticEqu: bool
    StictionTransitionVelocityExpression: Expression
    TorquePreloadExpression: Expression
    TorsionalMoment: bool
    YokeType: Motion.JointFrictionAdams.FrictionYokeType


    class FrictionYokeType(enum.Enum):
        I = 0
        J = 1
    

    class FrictionOverlapDelta(enum.Enum):
        Constant = 0
        Increase = 1
        Decrease = 2
    

    class FrictionEffect(enum.Enum):
        All = 0
        Stiction = 1
        Sliding = 2
    

class JointFriction(TaggedObject):
    def __init__(self) -> None: ...
    AdamsFriction: Motion.JointFrictionAdams
    Enable: bool
    LmsFriction: Motion.JointFrictionLms
    RecurDynFriction: Motion.JointFrictionRecurDyn


class JointDriverCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.JointDriver]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateJointDriverBuilder(self, jointdriver: Motion.JointDriver) -> Motion.JointDriverBuilder:
        ...
    def FindObject(self, name: str) -> Motion.JointDriver:
        ...
    def Tag(self) -> Tag: ...



class JointDriverBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    DriverMultiOperations: Motion.DriverMultiOperations
    Joint: SelectTaggedObject
    Name: str


class JointDriver(Motion.MotionObject):
    def __init__(self) -> None: ...


class JointDefine(TaggedObject):
    def __init__(self) -> None: ...
    AxisType: Motion.JointDefine.UniversalJointAxisType
    DisplCurveType: Motion.JointDefine.ScrewJointDisplCurveType
    DisplayScale: float
    ExcludeRxConstraint: bool
    ExcludeRyConstraint: bool
    ExcludeRzConstraint: bool
    ExcludeXConstraint: bool
    ExcludeYConstraint: bool
    ExcludeZConstraint: bool
    FirstCsys: CoordinateSystem
    FirstLink: Motion.Link
    FirstMatrix: NXMatrix
    FirstOrientationType: Motion.JointDefine.OrientationType
    FirstOrigin: Point
    FirstVector: Direction
    JointType: Motion.JointDefine.Type
    LimitsDefined: bool
    LowerLimitAngleExpression: Expression
    LowerLimitDefined: bool
    LowerLimitExpression: Expression
    MethodType: Motion.JointDefine.ScrewJointMethodType
    Name: str
    RatioType: Motion.JointDefine.ScrewJointRatioType
    RotationAllowed: bool
    ScrewDisplCurveFunction: CAE.Function
    ScrewDisplCurveProfile: Motion.SelectFieldData
    ScrewRatioExpression: Expression
    ScrewRatioProfile: Motion.SelectFieldData
    ScrewSplineFunction: CAE.Function
    SecondCsys: CoordinateSystem
    SecondLink: Motion.Link
    SecondMatrix: NXMatrix
    SecondOrientationType: Motion.JointDefine.OrientationType
    SecondOrigin: Point
    SecondVector: Direction
    SnapLinks: bool
    TranslationAllowed: bool
    UpperLimitAngleExpression: Expression
    UpperLimitDefined: bool
    UpperLimitExpression: Expression


    class UniversalJointAxisType(enum.Enum):
        Rotational = 0
        CrossPin = 1
    

    class Type(enum.Enum):
        Revolute = 0
        Slider = 1
        Cylindrical = 2
        Screw = 3
        Universal = 4
        Spherical = 5
        Planar = 6
        Fixed = 7
        Constantvelocity = 8
        Atpoint = 9
        Inline = 10
        Inplane = 11
        Orientation = 12
        Parallel = 13
        Perpendicular = 14
    

    class ScrewJointRatioType(enum.Enum):
        Expression = 0
        Spline = 1
        Profile = 2
    

    class ScrewJointMethodType(enum.Enum):
        Ratio = 0
        Displacementcurve = 1
    

    class ScrewJointDisplCurveType(enum.Enum):
        Spline = 0
        Profile = 1
    

    class OrientationType(enum.Enum):
        Vector = 0
        Csys = 1
    

class JointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Joint]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateJointBuilder(self, joint: Motion.Joint) -> Motion.JointBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Joint:
        ...
    def Tag(self) -> Tag: ...



class JointBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    JointDefine: Motion.JointDefine
    JointFriction: Motion.JointFriction
    JointMultiDrivers: Motion.DriverMultiOperations


class Joint(Motion.MotionObject):
    def __init__(self) -> None: ...




class InputPortAssociationList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Motion.InputPortAssociation]) -> None:
        ...
    def Append(self, object: Motion.InputPortAssociation) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Motion.InputPortAssociation) -> int:
        ...
    def FindItem(self, index: int) -> Motion.InputPortAssociation:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Motion.InputPortAssociation) -> None:
        ...
    def Erase(self, obj: Motion.InputPortAssociation, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Motion.InputPortAssociation]:
        ...
    def SetContents(self, objects: typing.List[Motion.InputPortAssociation]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Motion.InputPortAssociation, object2: Motion.InputPortAssociation) -> None:
        ...
    def Insert(self, location: int, object: Motion.InputPortAssociation) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class InputPortAssociation(Motion.PortAssociation):
    def __init__(self) -> None: ...
    AssociatedPortName: str
    Port: Motion.ControlPort




class GraphObjectBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def GetQuantityTypes(self, typeStrings: str, valueStrings: str) -> None:
        ...
    def SetQuantityType(self, typeString: str, valueString: str) -> None:
        ...
    def FindEquivalent(self) -> Motion.Graph:
        ...
    AdvancedSolutionObject: Motion.AdvancedSolution
    ReferenceObject: Motion.IGraphSource
    SolutionObject: Motion.MotionSolution


class GraphManager(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Graph]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateGraphBuilder(self, graph: Motion.Graph) -> Motion.GraphBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphManager.CreateGraphObjectBuilder instead.")"""
        ...
    def Find(self, name: str) -> Motion.Graph:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphManager.FindObject instead.")"""
        ...
    def FindObject(self, name: str) -> Motion.Graph:
        ...
    def CreateGraphObjectBuilder(self, graph: Motion.Graph) -> Motion.GraphObjectBuilder:
        ...
    def Tag(self) -> Tag: ...



class GraphLegendData(NXObject):
    def __init__(self) -> None: ...
    def AskNumberOfDisplayableAttributes(self) -> int:
        ...
    def AskNthDisplayableAttributeName(self, nth: int) -> str:
        ...
    def AskNthDisplayableAttributeValue(self, nth: int) -> str:
        ...


class GraphBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMotionObjects(self) -> typing.List[NXObject]:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    def SetMotionObjects(self, motionObjects: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    def MoveUpYCurves(self, selectedIndices: int) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    def MoveDownYCurves(self, selectedIndices: int) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    def GetYCurves(self) -> typing.List[Motion.GraphBuilder.CurveData]:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    def AddYCurves(self, curves: typing.List[Motion.GraphBuilder.CurveData]) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    def RemoveYCurve(self, yCurve: Motion.GraphBuilder.CurveData) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    def SetXCurve(self, newCurve: Motion.GraphBuilder.CurveData) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use Motion.GraphObjectBuilder instead..")"""
        ...
    AfuFile: str
    Component: Motion.GraphBuilder.ComponentChoices
    CoordinateSystemType: Motion.GraphBuilder.CsysChoices
    GraphTitle: str
    Mode: int
    ModeRequest: Motion.GraphBuilder.RequestChoices
    Object: NXObject
    PlotEnable: bool
    PlotStyle: Motion.GraphBuilder.PlotStyleChoices
    Request: Motion.GraphBuilder.RequestChoices
    StoreEnable: bool
    XAxisType: Motion.GraphBuilder.XAxisTypeChoices
    XCurve: Motion.GraphBuilder.CurveData


    class XAxisTypeChoices(enum.Enum):
        DefaultTime = 0
        UserDefined = 1
    

    class RequestChoices(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
        Force = 3
        MotorDriver = 4
    

    class PlotStyleChoices(enum.Enum):
        Ftk = 0
        Spreadsheet = 1
    

    class GraphBuilderCurveData():
        MotionObject: NXObject
        RequestIndex: int
        ComponentIndex: int
        RequestCsysIndex: int
        def ToString(self) -> str:
            ...
    

    class CsysChoices(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class ComponentChoices(enum.Enum):
        Mag = 0
        X = 1
        Y = 2
        Z = 3
        Amag = 4
        Xy = 5
        Yz = 6
        Zx = 7
        InputVoltage = 8
        ElectricCurrent = 9
        ElectricTorque = 10
        SignalChart = 11
    

class Graph(NXObject):
    def __init__(self) -> None: ...
    def CreateGraphLegendData(self) -> CAE.FTK.IApplicationData:
        ...


class GeneralCouplerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.GeneralCoupler]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateGeneralCouplerBuilder(self, gcoupler: Motion.GeneralCoupler) -> Motion.GeneralCouplerBuilder:
        ...
    def FindObject(self, name: str) -> Motion.GeneralCoupler:
        ...
    def Tag(self) -> Tag: ...



class GeneralCouplerBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Attachment: Motion.GeneralCouplerBuilder.AttachmentType
    FirstJoint: Motion.SelectJoint
    FirstScaleExpression: Expression
    FirstType: Motion.GcouplerMovementTypes
    Name: str
    SecondJoint: Motion.SelectJoint
    SecondScaleExpression: Expression
    SecondType: Motion.GcouplerMovementTypes
    ThirdJoint: Motion.SelectJoint
    ThirdScaleExpression: Expression
    ThirdType: Motion.GcouplerMovementTypes


    class AttachmentType(enum.Enum):
        Two = 0
        Three = 1
    

class GeneralCoupler(Motion.MotionObject):
    def __init__(self) -> None: ...


class GcouplerMovementTypes(enum.Enum):
    Rotation = 0
    Translation = 1


class ForceValueTypes(enum.Enum):
    Constant = 0
    Function = 1
    Profile = 2


class FlexPhysicalDampingSettings(TaggedObject):
    def __init__(self) -> None: ...
    PhysicalHystereticScalingFactor: float
    PhysicalViscousScalingFactor: float
    UsingPhysicalHysteretic: bool
    UsingPhysicalViscous: bool


class FlexBodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.FlexBody]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFlexBodyBuilder(self, flexbody: Motion.FlexBody) -> Motion.FlexBodyBuilder:
        ...
    def FindObject(self, name: str) -> Motion.FlexBody:
        ...
    def Tag(self) -> Tag: ...



class FlexBodyBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def GetOffsetPoints(self) -> float:
        ...
    def SetOffsetPoints(self, offsetPoints: float) -> None:
        ...
    def GetOffsetOrientations(self) -> float:
        ...
    def SetOffsetOrientations(self, offsetOrientations: float) -> None:
        ...
    def GetMarkerItems(self) -> typing.List[Motion.MarkerToNodeData]:
        ...
    def SetMarkerItems(self, markerToNodeListItem: typing.List[Motion.MarkerToNodeData]) -> None:
        ...
    def NewListMarkerToNode(self, marker: NXObject, markerPosition: int, nodeID: int, move: bool, nodeLocationX: float, nodeLocationY: float, nodeLocationZ: float) -> Motion.MarkerToNodeData:
        ...
    def ExportRfiRelatedResults(self, caeFileSpec: str, resultName: str) -> str:
        ...
    CutoffDamping: Expression
    CutoffFrequencyIncrement: Expression
    CutoffLowerFrequency: Expression
    CutoffUpperFrequency: Expression
    FileTceName: str
    MassMatrix0: bool
    MassMatrix1: bool
    MassMatrix2: bool
    MassMatrix3: bool
    MassMatrix4: bool
    MassScalar0: bool
    MassScalar1: bool
    MassScalar2: bool
    MassVector0: bool
    MassVector1: bool
    MassVector2: bool
    MassVector3: bool
    MassVector4: bool
    Name: str
    NativeRfiFileName: str
    NodeTolerance: Expression
    PositioningType: Motion.FlexBodyBuilder.Positioning
    SelectionLink: Motion.SelectLink
    SourceOption: Motion.FlexBodyBuilder.SourceType
    TransientTime: Expression
    TreatAsRigid: bool
    UnitSystem: Motion.FlexBodyBuilder.UnitSystemType
    UseFrequencyFiltering: bool
    UseTransientDamping: bool


    class UnitSystemType(enum.Enum):
        Infered = 0
        MeterNewton = 1
        FootPoundalF = 2
        MeterKilogramF = 3
        FootPoundal = 4
        MillimeterMillinewton = 5
        CentimeterCentinewton = 6
        InchPoundF = 7
        MillimeterKilogramF = 8
        MillimeterNewton = 9
    

    class SourceType(enum.Enum):
        Localfolder = 0
        Teamcenter = 1
    

    class Positioning(enum.Enum):
        AbsoluteOrigin = 0
        ComponentPosition = 1
        ThreePointMethod = 2
    

class FlexBody(Motion.MotionObject):
    def __init__(self) -> None: ...
    def GetNormalModeById(self, modeId: int) -> Motion.NormalModeProperty:
        ...
    def GetNormalModes(self) -> typing.List[Motion.NormalModeProperty]:
        ...
    def Activate(self, activate: bool) -> None:
        ...
    def SetDampingFactors(self, viscousDamping: float, hystereticDamping: float) -> None:
        ...
    def GetPhysicalDampingSettings(self) -> Motion.FlexPhysicalDampingSettings:
        ...
    NormalModeCount: int


class FieldDataCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.FieldData]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFieldData(self, field: Fields.Field) -> Motion.FieldData:
        ...
    def FindObject(self, name: str) -> Motion.FieldData:
        ...
    def Tag(self) -> Tag: ...



class FieldData(NXObject):
    def __init__(self) -> None: ...
    Field: Fields.Field


class ExpressionFunctionBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DataType: Motion.ExpressionFunctionBuilder.Type
    Expression: Expression
    Function: Motion.MotionFunction
    Profile: Motion.SelectFieldData


    class Type(enum.Enum):
        Expression = 0
        Function = 1
        Profile = 2
    

class DriverOperation(TaggedObject):
    def __init__(self) -> None: ...
    AccelerationExpression: Expression
    AmplitudeExpression: Expression
    ControlPort: Motion.SelectControlPort
    DisplacementExpression: Expression
    FrequencyExpression: Expression
    Function: NXObject
    HarmonicDisplacementExpression: Expression
    InitialDisplacementExpression: Expression
    InitialVelocityExpression: Expression
    IntegrationTypeOption: Motion.DriverOperation.IntegrationType
    JerkExpression: Expression
    Motor: Motion.PMDCMotor
    PhaseAngleExpression: Expression
    Profile: SelectNXObject
    SignalChart: Motion.SignalChart
    TypeOption: Motion.DriverOperation.Type
    VelocityExpression: Expression


    class Type(enum.Enum):
        Undefined = 0
        Constant = 1
        Polynomial = 1
        Harmonic = 2
        Function = 3
        Articulation = 4
        Motor = 5
        Control = 6
        Profile = 7
    

    class IntegrationType(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
    

class DriverMultiOperations(TaggedObject):
    def __init__(self) -> None: ...
    MotionEulerAngle1: Motion.DriverOperation
    MotionPointOnCurve: Motion.DriverOperation
    MotionTranslationZ: Motion.DriverOperation


class DriverMotionsData(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DataType: Motion.DriverMotionsData.DriverDataType
    RotationType: Motion.DriverMotionsData.DriverRotationType
    RotationX: Motion.DriverOperation
    RotationY: Motion.DriverOperation
    RotationZ: Motion.DriverOperation
    TranslationX: Motion.DriverOperation
    TranslationY: Motion.DriverOperation
    TranslationZ: Motion.DriverOperation


    class DriverRotationType(enum.Enum):
        Successive = 0
        Fixed = 1
    

    class DriverDataType(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
    

class DamperCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Damper]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDamperBuilder(self, damper: Motion.Damper) -> Motion.DamperBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Damper:
        ...
    def Tag(self) -> Tag: ...



class DamperBuilder(Motion.ConnectorBuilder):
    def __init__(self) -> None: ...
    CoefficientCurveProfile: Motion.SelectFieldData
    CoefficientExpression: Expression
    CoefficientFunction: CAE.Function
    CoefficientType: Motion.ConnectorCoefficientTypes
    DamperAppDirection: Motion.ConnectorBuilder.ApplicationDirection
    DamperCustomizedSolver: bool
    Name: str
    TorsionalCoefficientExpression: Expression


class Damper(Motion.Connector):
    def __init__(self) -> None: ...


class CustomizedMaterialBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Density: Expression
    IsCustomizedMaterial: bool
    Material: PhysicalMaterial
    PoissonRatio: Expression
    YoungModulus: Expression


class CurveParameterizedTypes(enum.Enum):
    Curvature = 0
    Spacing = 1


class CurveOnCurveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.CurveOnCurve]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCurveOnCurveBuilder(self, curveOnCurve: Motion.CurveOnCurve) -> Motion.CurveOnCurveBuilder:
        ...
    def FindObject(self, name: str) -> Motion.CurveOnCurve:
        ...
    def Tag(self) -> Tag: ...



class CurveOnCurveBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def GetICurve(self) -> typing.List[NXObject]:
        ...
    def SetICurve(self, curves: typing.List[NXObject]) -> None:
        ...
    def GetJCurve(self) -> typing.List[NXObject]:
        ...
    def SetJCurve(self, curves: typing.List[NXObject]) -> None:
        ...
    LockSlip: bool
    Name: str


class CurveOnCurve(Motion.MotionObject):
    def __init__(self) -> None: ...


class CurveContactRecurdyn(NXObject):
    def __init__(self) -> None: ...
    BufferRadiusFactorExpression: Expression
    CurveToleranceFactorExpression: Expression
    DynamicCoefficientExpression: Expression
    FirstCurveMaximumPenetrationExpression: Expression
    ForceExponentExpression: Expression
    MaterialDampingExpression: Expression
    MaximumStepSizeFactorExpression: Expression
    PenetrationDepthExpression: Expression
    SecondCurveMaximumPenetrationExpression: Expression
    SlipVelocityExpression: Expression
    StaticCoefficientExpression: Expression
    StiffnessExpression: Expression
    TransitionVelocityExpression: Expression


class CurveContactCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.CurveContact]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCurveContactBuilder(self, contactobj: Motion.CurveContact) -> Motion.CurveContactBuilder:
        ...
    def FindObject(self, name: str) -> Motion.CurveContact:
        ...
    def Tag(self) -> Tag: ...



class CurveContactBuilder(Builder):
    def __init__(self) -> None: ...
    AdamsParameters: Motion.CurveContactAdams
    ContactName: str
    DisplayScale: float
    FirstContactCurve: SelectNXObjectList
    FirstGeometryMaterialDirection: Motion.CurveContactBuilder.GeometryMaterialSide
    RecurdynParameters: Motion.CurveContactRecurdyn
    SecondContactCurve: SelectNXObjectList
    SecondGeometryMaterialDirection: Motion.CurveContactBuilder.GeometryMaterialSide


    class GeometryMaterialSide(enum.Enum):
        Direction = 0
        DirectionReverse = 1
    

class CurveContactAdams(NXObject):
    def __init__(self) -> None: ...
    DynamicCoefficientExpression: Expression
    ForceExponentExpression: Expression
    MaterialDampingExpression: Expression
    PenetrationDepthExpression: Expression
    SlipVelocityExpression: Expression
    StaticCoefficientExpression: Expression
    StiffnessExpression: Expression
    TransitionVelocityExpression: Expression


class CurveContact(Motion.MotionObject):
    def __init__(self) -> None: ...


class CouplerRckpnBuilder(Motion.CouplerBuilder):
    def __init__(self) -> None: ...


class CouplerRckpn(Motion.Coupler):
    def __init__(self) -> None: ...


class CouplerGearBuilder(Motion.CouplerBuilder):
    def __init__(self) -> None: ...


class CouplerGear(Motion.Coupler):
    def __init__(self) -> None: ...


class CouplerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Coupler]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateCouplerGearBuilder(self, coupler: Motion.CouplerGear) -> Motion.CouplerGearBuilder:
        ...
    def CreateCouplerRckpnBuilder(self, coupler: Motion.CouplerRckpn) -> Motion.CouplerRckpnBuilder:
        ...
    def CreateCouplerCableBuilder(self, coupler: Motion.CouplerCable) -> Motion.CouplerCableBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Coupler:
        ...
    def Tag(self) -> Tag: ...



class CouplerCableBuilder(Motion.CouplerBuilder):
    def __init__(self) -> None: ...


class CouplerCable(Motion.Coupler):
    def __init__(self) -> None: ...


class CouplerBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ContactPoint: Point
    FirstJoint: Motion.SelectJoint
    FirstRadiusExpression: Expression
    Name: str
    RatioExpression: Expression
    SecondJoint: Motion.SelectJoint
    SecondRadiusExpression: Expression


class Coupler(Motion.MotionObject):
    def __init__(self) -> None: ...


class ControlPortCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ControlPort]:
        ...
    def __init__(self, owner: Motion.ControlInput) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Motion.ControlPort:
        ...
    def Tag(self) -> Tag: ...



class ControlPort(Motion.MotionObject):
    def __init__(self) -> None: ...


class ControlOutputCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ControlOutput]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateControlOutputBuilder(self, controlOutput: Motion.ControlOutput) -> Motion.ControlOutputBuilder:
        ...
    def FindObject(self, name: str) -> Motion.ControlOutput:
        ...
    def Tag(self) -> Tag: ...



class ControlOutputBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ActionLinkAttachment: Motion.LinkAttachmentData
    BaseLinkAttachment: Motion.LinkAttachmentData
    Direction: Motion.ControlOutputBuilder.DirectionType
    JointSelection: Motion.SelectJoint
    Name: str
    OutputType: Motion.ControlOutputBuilder.ControlOutputType
    PortSelection: Motion.SelectControlPort
    Variable: Motion.ControlOutputBuilder.VariableType


    class VariableType(enum.Enum):
        Force = 0
        Torque = 1
        ActionTorque = 2
        BaseTorque = 3
    

    class DirectionType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class ControlOutputType(enum.Enum):
        Link = 0
        JointOrConstraint = 1
    

class ControlOutput(Motion.MotionObject):
    def __init__(self) -> None: ...


class ControlInputPortBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Motion.ControlInputPortBuilder]) -> None:
        ...
    def Append(self, object: Motion.ControlInputPortBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Motion.ControlInputPortBuilder) -> int:
        ...
    def FindItem(self, index: int) -> Motion.ControlInputPortBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Motion.ControlInputPortBuilder) -> None:
        ...
    def Erase(self, obj: Motion.ControlInputPortBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Motion.ControlInputPortBuilder]:
        ...
    def SetContents(self, objects: typing.List[Motion.ControlInputPortBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Motion.ControlInputPortBuilder, object2: Motion.ControlInputPortBuilder) -> None:
        ...
    def Insert(self, location: int, object: Motion.ControlInputPortBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ControlInputPortBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Component: Motion.ControlInputPortBuilder.MeasuredComponent
    Digital: bool
    Name: str
    SampleRate: Expression
    Variable: Motion.ControlInputPortBuilder.MeasuredVariable


    class MeasuredVariable(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
    

    class MeasuredComponent(enum.Enum):
        LinearMagnitude = 0
        X = 1
        Y = 2
        Z = 3
        AngularMagnitude = 4
        Rx = 5
        Ry = 6
        Rz = 7
    

class ControlInputCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.ControlInput]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateControlInputBuilder(self, controlinput: Motion.ControlInput) -> Motion.ControlInputBuilder:
        ...
    def FindObject(self, name: str) -> Motion.ControlInput:
        ...
    def Tag(self) -> Tag: ...



class ControlInputBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    def CreateControlInputPortBuilder(self) -> Motion.ControlInputPortBuilder:
        ...
    MeasurementLinkAttachment: Motion.LinkAttachmentData
    Name: str
    PortsList: Motion.ControlInputPortBuilderList
    ReferenceLinkAttachment: Motion.LinkAttachmentData
    RelativeLinkAttachment: Motion.LinkAttachmentData
    Type: Motion.ControlInputBuilder.InputType


    class InputType(enum.Enum):
        Link = 0
    

class ControlInput(Motion.MotionObject):
    def __init__(self) -> None: ...
    ControlPorts: Motion.ControlPortCollection


class ConnectorCoefficientTypes(enum.Enum):
    Constant = 0
    Spline = 1
    Profile2d = 2
    Profile3d = 3
    ExpressionAndSpline = 4
    ExpressionAndProfile2d = 5
    ExpressionAndProfile3d = 6


class ConnectorBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ActionLink: Motion.SelectLink
    ActionPoint: Point
    Attachment: Motion.ConnectorBuilder.AttachmentType
    Joint: Motion.SelectJoint
    ReactionLink: Motion.SelectLink
    ReactionPoint: Point


    class AttachmentType(enum.Enum):
        Link = 0
        SliderJoint = 1
        RevoluteJoint = 2
    

    class ApplicationDirection(enum.Enum):
        Bidirectional = 0
        TensionOnly = 1
        CompressionOnly = 2
    

class Connector(Motion.MotionObject):
    def __init__(self) -> None: ...


class ConfigurationTextParameter(Motion.ConfigurationParameter):
    def __init__(self) -> None: ...
    ActualValue: str
    InitialValue: str


class ConfigurationParameterList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Motion.ConfigurationParameter]) -> None:
        ...
    def Append(self, object: Motion.ConfigurationParameter) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Motion.ConfigurationParameter) -> int:
        ...
    def FindItem(self, index: int) -> Motion.ConfigurationParameter:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Motion.ConfigurationParameter) -> None:
        ...
    def Erase(self, obj: Motion.ConfigurationParameter, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Motion.ConfigurationParameter]:
        ...
    def SetContents(self, objects: typing.List[Motion.ConfigurationParameter]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Motion.ConfigurationParameter, object2: Motion.ConfigurationParameter) -> None:
        ...
    def Insert(self, location: int, object: Motion.ConfigurationParameter) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ConfigurationParameter(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Name: str


class ConfigurationIntegerParameter(Motion.ConfigurationParameter):
    def __init__(self) -> None: ...
    ActualValue: int
    InitialValue: int


class ConfigurationFloatParameter(Motion.ConfigurationParameter):
    def __init__(self) -> None: ...
    ActualValue: Expression
    InitialValue: Expression


class BushingStiffnessCoefficients(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CylindricalStiffnessCoefficients: Motion.BushingCylindricalCoefficientsComponent
    GeneralTorsionalStiffnessCoefficients: Motion.BushingGeneralCoefficientsComponent
    GeneralTranslationalStiffnessCoefficients: Motion.BushingGeneralCoefficientsComponent
    SphericalStiffnessCoefficients: Motion.BushingSphericalCoefficientsComponent


class BushingSphericalCoefficientTypes(enum.Enum):
    Stiffness = 0
    Damping = 1
    Preload = 2


class BushingSphericalCoefficientsComponent(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ConicalCurveProfile: Motion.SelectFieldData
    ConicalExpression: Expression
    ConicalFunction: CAE.Function
    ConicalType: Motion.ConnectorCoefficientTypes
    RadialCurveProfile: Motion.SelectFieldData
    RadialExpression: Expression
    RadialFunction: CAE.Function
    RadialType: Motion.ConnectorCoefficientTypes


class BushingSphericalCoefficients(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DampingCoefficients: Motion.BushingSphericalCoefficientsComponent
    PreloadCoefficients: Motion.BushingSphericalCoefficientsComponent
    StiffnessCoefficients: Motion.BushingSphericalCoefficientsComponent


class BushingGeneralCoefficientTypes(enum.Enum):
    TranslationalStiffness = 0
    TranslationalDamping = 1
    TranslationalPreload = 2
    TorsionalStiffness = 3
    TorsionalDamping = 4
    TorsionalPreload = 5


class BushingGeneralCoefficientsComponent(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CoefficientsType: Motion.ConnectorCoefficientTypes
    XCoefficientsType: Motion.ConnectorCoefficientTypes
    XCurveProfile: Motion.SelectFieldData
    XExpression: Expression
    XFunction: CAE.Function
    YCoefficientsType: Motion.ConnectorCoefficientTypes
    YCurveProfile: Motion.SelectFieldData
    YExpression: Expression
    YFunction: CAE.Function
    ZCoefficientsType: Motion.ConnectorCoefficientTypes
    ZCurveProfile: Motion.SelectFieldData
    ZExpression: Expression
    ZFunction: CAE.Function


class BushingGeneralCoefficients(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DampingCoefficients: Motion.BushingGeneralCoefficientsComponent
    PreloadCoefficients: Motion.BushingGeneralCoefficientsComponent
    StiffnessCoefficients: Motion.BushingGeneralCoefficientsComponent


class BushingGeneralCoefficientMoveTypes(enum.Enum):
    Translational = 0
    Torsional = 1


class BushingDefine(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ActionLink: Motion.SelectLink
    ActionOffsetX: Expression
    ActionOffsetY: Expression
    ActionOffsetZ: Expression
    ActionPoint: Point
    AngleCalculation: Motion.BushingDefine.AngleCalculationOption
    ApplyActionOffset: bool
    ApplyBaseOffset: bool
    BaseOffsetX: Expression
    BaseOffsetY: Expression
    BaseOffsetZ: Expression
    Csys: CoordinateSystem
    Dipole: bool
    Direction: Direction
    ForceCalculation: Motion.BushingDefine.ForceCalculationOption
    Name: str
    Orientation: NXMatrix
    OrientationType: Motion.BushingDefine.OrientationTypes
    ReactionLink: Motion.SelectLink
    ReactionPoint: Point


    class OrientationTypes(enum.Enum):
        Vector = 0
        Csys = 1
    

    class ForceCalculationOption(enum.Enum):
        Abc = 0
        Standard = 1
        Bab = 2
    

    class AngleCalculationOption(enum.Enum):
        LargeAngle = 0
        SmallAngle = 1
    

class BushingDampingCoefficients(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CylindricalDampingCoefficients: Motion.BushingCylindricalCoefficientsComponent
    GeneralTorsionalDampingCoefficients: Motion.BushingGeneralCoefficientsComponent
    GeneralTranslationalDampingCoefficients: Motion.BushingGeneralCoefficientsComponent
    SphericalDampingCoefficients: Motion.BushingSphericalCoefficientsComponent


class BushingCylindricalCoefficientTypes(enum.Enum):
    Stiffness = 0
    Damping = 1
    Preload = 2


class BushingCylindricalCoefficientsComponent(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    ConicalCurveProfile: Motion.SelectFieldData
    ConicalExpression: Expression
    ConicalFunction: CAE.Function
    ConicalType: Motion.ConnectorCoefficientTypes
    LongCurveProfile: Motion.SelectFieldData
    LongitudinalExpression: Expression
    LongitudinalFunction: CAE.Function
    LongitudinalType: Motion.ConnectorCoefficientTypes
    RadialCurveProfile: Motion.SelectFieldData
    RadialExpression: Expression
    RadialFunction: CAE.Function
    RadialType: Motion.ConnectorCoefficientTypes
    TorsionalCurveProfile: Motion.SelectFieldData
    TorsionalExpression: Expression
    TorsionalFunction: CAE.Function
    TorsionalType: Motion.ConnectorCoefficientTypes


class BushingCylindricalCoefficients(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    DampingCoefficients: Motion.BushingCylindricalCoefficientsComponent
    PreloadCoefficients: Motion.BushingCylindricalCoefficientsComponent
    StiffnessCoefficients: Motion.BushingCylindricalCoefficientsComponent


class BushingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.Bushing]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBushingBuilder(self, bushing: Motion.Bushing) -> Motion.BushingBuilder:
        ...
    def FindObject(self, name: str) -> Motion.Bushing:
        ...
    def Tag(self) -> Tag: ...



class BushingCoefficients(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX12.0.0.  Use Motion.BushingStiffnessCoefficients, Motion.BushingDampingCoefficients and Motion.BushingActuatorCoefficients instead..")"""
        ...
    CylindricalCoefficients: Motion.BushingCylindricalCoefficients
    SphericalCoefficients: Motion.BushingSphericalCoefficients
    TorsionalCoefficients: Motion.BushingGeneralCoefficients
    TranslationalCoefficients: Motion.BushingGeneralCoefficients


class BushingBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    BushingActuatorCoefficients: Motion.BushingActuatorCoefficients
    BushingCoefficients: Motion.BushingCoefficients
    BushingDampingCoefficients: Motion.BushingDampingCoefficients
    BushingDefine: Motion.BushingDefine
    BushingStiffnessCoefficients: Motion.BushingStiffnessCoefficients
    BushingType: Motion.BushingBuilder.BushingTypes


    class BushingTypes(enum.Enum):
        Cylindrical = 0
        General = 1
        Spherical = 2
    

class BushingActuatorCoefficients(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    CylindricalActuatorCoefficients: Motion.BushingCylindricalCoefficientsComponent
    GeneralTorsionalActuatorCoefficients: Motion.BushingGeneralCoefficientsComponent
    GeneralTranslationalActuatorCoefficients: Motion.BushingGeneralCoefficientsComponent
    SphericalActuatorCoefficients: Motion.BushingSphericalCoefficientsComponent


class Bushing(Motion.MotionObject):
    def __init__(self) -> None: ...


class BodyContactSphereToCAD(NXObject):
    def __init__(self) -> None: ...
    BodyAngleTolerance: Expression
    BodyDistanceTolerance: Expression
    BodyEnableMaxFacetSize: bool
    BodyMaxFacetSize: Expression
    CoulombFrictionOption: Motion.BodyContactSphereToCAD.CoulombFriction
    DynamicCoefficient: Expression
    ForceExponent: Expression
    FrictionVelocity: Expression
    MaterialDamping: Expression
    MaxPenetrationDepth: Expression
    PartialSphereAngle: Expression
    PartialSphereOption: bool
    PartialSphereVector: Direction
    SphereMaxFacetSize: Expression
    SphereRadius: Expression
    StaticCoefficient: Expression
    StictionVelocity: Expression
    Stiffness: Expression
    SuperElementIncrement: int
    SuperElementLink: Motion.SelectLink
    SuperElementReportInstance: int
    TessellationFile: str
    UseTessellationFile: bool


    class CoulombFriction(enum.Enum):
        Off = 0
        On = 1
    

class BodyContactRecurdyn(NXObject):
    def __init__(self) -> None: ...
    AutoGlobalMaxPenetrationFlag: int
    AutoLocalMaxPenetrationFlag: int
    BufferRadiusFactorExpression: Expression
    ContactTypeOption: Motion.BodyContactRecurdyn.ContactType
    CoulombFrictionOption: Motion.BodyContactRecurdyn.CoulombFriction
    DynamicCoefficientExpression: Expression
    FirstGeometryBoundingBufferLengthExpression: Expression
    FirstGeometryMaxFacetSizeFactorExpression: Expression
    FirstGeometryMaxFacetSizeFactorFlag: bool
    FirstGeometryMaximumPenetrationExpression: Expression
    FirstGeometryPlaneToleranceFactorExpression: Expression
    FirstGeometryPlaneToleranceFactorSolidContactExpression: Expression
    ForceExponentExpression: Expression
    ForceModelType: Motion.BodyContactRecurdyn.ForceModel
    FrictionVelocityExpression: Expression
    GlobalMaxPenetrationExpression: Expression
    LocalMaxPenetrationExpression: Expression
    MaterialDampingExpression: Expression
    MaximumStepSizeFactorExpression: Expression
    PenetrationDepthExpression: Expression
    ReboundDampingFactorExpression: Expression
    ReboundDampingFactorFlag: bool
    SecondGeometryBoundingBufferLengthExpression: Expression
    SecondGeometryMaxFacetSizeFactorExpression: Expression
    SecondGeometryMaxFacetSizeFactorFlag: bool
    SecondGeometryMaximumPenetrationExpression: Expression
    SecondGeometryPlaneToleranceFactorExpression: Expression
    SecondGeometryPlaneToleranceFactorSolidContactExpression: Expression
    StaticCoefficientExpression: Expression
    StictionVelocityExpression: Expression
    StiffnessExpression: Expression
    SurfaceTypeOption: Motion.BodyContactRecurdyn.SurfaceType


    class SurfaceType(enum.Enum):
        Faceted = 0
        Fitted = 1
    

    class ForceModel(enum.Enum):
        Impact = 0
        Poisson = 1
    

    class CoulombFriction(enum.Enum):
        Off = 0
        On = 1
    

    class ContactType(enum.Enum):
        Patch = 0
        Surface = 1
        Solid = 2
    

class BodyContactLms(NXObject):
    def __init__(self) -> None: ...
    ActionAngleTolerance: Expression
    ActionDistanceTolerance: Expression
    ActionEnableMaxFacetSize: bool
    ActionMaxFacetSize: Expression
    ActionTessellationFile: str
    ActionUseTessellationFile: bool
    BaseAngleTolerance: Expression
    BaseDistanceTolerance: Expression
    BaseEnableMaxFacetSize: bool
    BaseMaxFacetSize: Expression
    BaseTessellationFile: str
    BaseUseTessellationFile: bool
    CoulombFrictionOption: Motion.BodyContactLms.CoulombFriction
    DynamicCoefficient: Expression
    ForceExponent: Expression
    ForceModel: Motion.BodyContactLms.ForceModelType
    ForceModelTolerance: Expression
    FrictionVelocity: Expression
    MaterialDamping: Expression
    MaxPenetrationDepth: Expression
    StaticCoefficient: Expression
    StictionVelocity: Expression
    Stiffness: Expression


    class ForceModelType(enum.Enum):
        Auto = 0
        ProjectedVertex = 1
        Midplane = 2
    

    class CoulombFriction(enum.Enum):
        Off = 0
        On = 1
    

class BodyContactCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.BodyContact]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBodyContactBuilder(self, contactobj: Motion.BodyContact) -> Motion.BodyContactBuilder:
        ...
    def FindObject(self, name: str) -> Motion.BodyContact:
        ...
    def Tag(self) -> Tag: ...



class BodyContactBuilder(Builder):
    def __init__(self) -> None: ...
    AdamsParameters: Motion.BodyContactAdams
    ContactType: Motion.BodyContactBuilder.ContactTypeOption
    FirstContactGeometry: SelectNXObjectList
    LmsParameters: Motion.BodyContactLms
    Name: str
    RecurdynParameters: Motion.BodyContactRecurdyn
    SecondContactGeometry: SelectNXObjectList
    SphereCenter: Point
    SphereLink: Motion.SelectLink
    SphereToCadParameters: Motion.BodyContactSphereToCAD


    class ContactTypeOption(enum.Enum):
        CADToCADContact = 0
        SphereToCADContact = 1
    

class BodyContactAdams(NXObject):
    def __init__(self) -> None: ...
    CoulombFrictionOption: Motion.BodyContactAdams.CoulombFriction
    DynamicCoefficientExpression: Expression
    ForceExponentExpression: Expression
    ForceModelType: Motion.BodyContactAdams.ForceModel
    FrictionVelocityExpression: Expression
    MaterialDampingExpression: Expression
    PenetrationDepthExpression: Expression
    RestitutionCoefficentExpression: Expression
    StaticCoefficientExpression: Expression
    StictionVelocityExpression: Expression
    StiffnessExpression: Expression


    class ForceModel(enum.Enum):
        Impact = 0
        Poisson = 1
    

    class CoulombFriction(enum.Enum):
        Off = 0
        On = 1
    

class BodyContact(Motion.MotionObject):
    def __init__(self) -> None: ...


class BeamForceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.BeamForce]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateBeamForceBuilder(self, beamForce: Motion.BeamForce) -> Motion.BeamForceBuilder:
        ...
    def FindObject(self, name: str) -> Motion.BeamForce:
        ...
    def Tag(self) -> Tag: ...



class BeamForceBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ActionLink: Motion.SelectLink
    ActionPoint: Point
    Area: Expression
    AsyTimoshenkoCorrection: Expression
    AszTimoshenkoCorrection: Expression
    BaseLink: Motion.SelectLink
    BasePoint: Point
    CustomizedMaterial: Motion.CustomizedMaterialBuilder
    DampingRatio: Expression
    DampingType: Motion.BeamForceBuilder.DampingTypes
    Direction: Direction
    FreeLength: Expression
    InertiaIyy: Expression
    InertiaIzz: Expression
    InertiaK: Expression
    IsBeamCrossDamping: bool
    Name: str
    VectorType: Motion.BeamForceBuilder.VectorTypes


    class VectorTypes(enum.Enum):
        Y = 0
        Z = 1
    

    class DampingTypes(enum.Enum):
        Viscous = 0
        Structural = 1
    

class BeamForce(Motion.MotionObject):
    def __init__(self) -> None: ...


class BaseSectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.BaseSection]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateUserDefinedSectionBuilder(self, userDefinedSection: Motion.UserDefinedSection) -> Motion.UserDefinedSectionBuilder:
        ...
    def CreateStandardSectionBuilder(self, standardSection: Motion.StandardSection) -> Motion.StandardSectionBuilder:
        ...
    def FindObject(self, name: str) -> Motion.BaseSection:
        ...
    def Tag(self) -> Tag: ...



class BaseSectionBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Name: str


class BaseSection(Motion.MotionObject):
    def __init__(self) -> None: ...


class ArticulationControl(Motion.PostControl):
    def __init__(self) -> None: ...
    def GetArticulationJointsDisplacement(self, jointTag: Motion.Joint, currentStep: int, displacement: float, displacementUnit: Unit) -> None:
        ...
    def ArticulationSolve(self, numSteps: int, jointTags: typing.List[Motion.Joint], stepSize: float, stepSizeUnit: typing.List[Unit]) -> None:
        ...
    def ArticulationSolve(self, jointTags: typing.List[Motion.Joint], displacement: float, displacementUnit: typing.List[Unit]) -> None:
        ...
    def StepToDesignPosition(self) -> None:
        ...
    def StepToAssemblyPosition(self) -> None:
        ...
    def Stop(self) -> None:
        ...
    def Finish(self) -> None:
        ...
    def GetArticulationJoints(self, jointTags: typing.List[Motion.Joint]) -> None:
        ...
    ActiveView: Motion.ActiveView
    Delay: int
    JointsLimits: bool


class AnimationControl(Motion.PostControl):
    def __init__(self) -> None: ...
    def Play(self) -> None:
        ...
    def PlayBackward(self) -> None:
        ...
    def Pause(self) -> None:
        ...
    def Stop(self) -> None:
        ...
    def StepTo(self, step: int) -> None:
        ...
    def StepForward(self) -> None:
        ...
    def StepBackward(self) -> None:
        ...
    def StepFirst(self) -> None:
        ...
    def StepLast(self) -> None:
        ...
    def StepToDesignPosition(self) -> None:
        ...
    def StepToAssemblyPosition(self) -> None:
        ...
    def Finish(self) -> None:
        ...
    def GetLinkTransformatioinMatrix(self, linkTag: Motion.Link, currentStep: int) -> float:
        ...
    CurrentStep: int
    Delay: int
    Mode: Motion.PlayMode
    NumberSteps: int


class AnalyticalContactPropertyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.AnalyticalContactProperty]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAnalyticalContactPropertyBuilder(self, analyticalContactProperty: Motion.AnalyticalContactProperty) -> Motion.AnalyticalContactPropertyBuilder:
        ...
    def FindObject(self, name: str) -> Motion.AnalyticalContactProperty:
        ...
    def Tag(self) -> Tag: ...



class AnalyticalContactPropertyBuilder(Builder):
    def __init__(self) -> None: ...
    DampingCurve: Motion.MotionFunction
    DampingOption: Motion.AnalyticalContactPropertyBuilder.DampingType
    DampingProfile: Motion.SelectFieldData
    DampingValue: Expression
    FirstCustomizedMaterial: Motion.CustomizedMaterialBuilder
    FrictionCoefficientCurve: Motion.MotionFunction
    FrictionCoefficientOption: Motion.AnalyticalContactPropertyBuilder.FrictionCoefficientType
    FrictionCoefficientProfile: Motion.SelectFieldData
    FrictionCoefficientValue: Expression
    Name: str
    RestitutionCoefficient: Expression
    SecondCustomizedMaterial: Motion.CustomizedMaterialBuilder
    StiffnessCurve: Motion.MotionFunction
    StiffnessOption: Motion.AnalyticalContactPropertyBuilder.StiffnessType
    StiffnessProfile: Motion.SelectFieldData
    StiffnessValue: Expression
    TransitionVelocity: Expression


    class StiffnessType(enum.Enum):
        Expression = 0
        Function = 1
        Profile = 2
        ExpressionAndFunction = 3
        ExpressionAndProfile = 4
    

    class FrictionCoefficientType(enum.Enum):
        Expression = 0
        Function = 1
        Profile = 2
    

    class DampingType(enum.Enum):
        Expression = 0
        Function = 1
        Profile = 2
        ExpressionAndFunction = 3
        ExpressionAndProfile = 4
    

class AnalyticalContactProperty(Motion.MotionObject):
    def __init__(self) -> None: ...


class AnalyticalContactCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.AnalyticalContact]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateAnalyticalContactBuilder(self, analyticalContact: Motion.AnalyticalContact) -> Motion.AnalyticalContactBuilder:
        ...
    def FindObject(self, name: str) -> Motion.AnalyticalContact:
        ...
    def Tag(self) -> Tag: ...



class AnalyticalContactBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    ContactProperty: Motion.SelectAnalyticalContactProperty
    ContactType: Motion.AnalyticalContactBuilder.ContactTypeOption
    EffectiveContactDepth: Expression
    ExtrusionBodies: SelectNXObjectList
    ExtrusionGeometryData: bool
    ExtrusionGeometryDataFile: str
    ExtrusionLink: Motion.SelectLink
    ExtrusionMaterialSide: bool
    FindAllRoots: bool
    FirstSuperElementIncrement: int
    FirstSuperElementLink: Motion.SelectLink
    InfiniteExtrusion: bool
    InfiniteSweep: bool
    MaxTesselationLength: Expression
    Name: str
    PartialSphereAngle: Expression
    PartialSphereOption: bool
    PartialSphereVector: Direction
    Profile: Motion.AnalyticalContactBuilder.ProfileType
    RadiusOfExclusion: Expression
    RailBodies: SelectNXObjectList
    RailCurve: Section
    RailGeometryData: bool
    RailGeometryDataFile: str
    RailLink: Motion.SelectLink
    RailMaterialSide: bool
    RailRollAngleCurve: Motion.MotionFunction
    RailSplineFunctions: bool
    RailXCurve: Motion.MotionFunction
    RailYCurve: Motion.MotionFunction
    RailZCurve: Motion.MotionFunction
    RevolutionBodies: SelectNXObjectList
    RevolutionGeometryData: bool
    RevolutionGeometryDataFile: str
    RevolutionLink: Motion.SelectLink
    RevolutionMaterialSide: bool
    SecondRevolutionBodies: SelectNXObjectList
    SecondRevolutionGeometryData: bool
    SecondRevolutionGeometryDataFile: str
    SecondRevolutionLink: Motion.SelectLink
    SecondRevolutionMaterialSide: bool
    SecondSphereLink: Motion.SelectLink
    SecondSpherePoint: Point
    SecondSphereRadius: Expression
    SecondSuperElementIncrement: int
    SecondSuperElementLink: Motion.SelectLink
    SphereLink: Motion.SelectLink
    SpherePoint: Point
    SphereRadius: Expression
    SuperElementReportInstance: int


    class ProfileType(enum.Enum):
        None = 0
        Circular = 1
        Road = 2
    

    class ContactTypeOption(enum.Enum):
        SphereToSphere = 0
        SphereToExtrusion = 1
        SphereToRevolution = 2
        ExtrusionToRevolution = 3
        RevolutionToRevolution = 4
        SphereToRail = 5
    

class AnalyticalContact(Motion.MotionObject):
    def __init__(self) -> None: ...


class AdvancedSolutionBuilder(Motion.MotionBuilder):
    def __init__(self) -> None: ...
    Definition: str


class AdvancedSolution(Motion.MotionSolution):
    def __init__(self) -> None: ...


class AdoptionPairCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Motion.AdoptionPair]:
        ...
    def __init__(self, owner: Motion.MotionManager) -> None: ...
    def __init__(self) -> None: ...
    def CreatePair(self, source: NXObject, adoption: Motion.MotionObject) -> Motion.AdoptionPair:
        ...
    def FindObject(self, name: str) -> Motion.AdoptionPair:
        ...
    def Tag(self) -> Tag: ...



class AdoptionPair(NXObject):
    def __init__(self) -> None: ...
    Adoption: Motion.MotionObject
    Source: NXObject


class AdoptionManager(NXObject):
    def __init__(self) -> None: ...
    def AdoptKinematicsFromAssembly(self) -> None:
        ...


class AddSubmechanismBuilder(Builder):
    def __init__(self) -> None: ...
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...
    LayerOption: Motion.AddSubmechanismBuilder.Layer
    SelectedPart: NXObject
    UserLayer: int


    class Layer(enum.Enum):
        Original = 0
        Work = 1
        Specified = 2
    

class AdamsSolverProperty(TaggedObject):
    def __init__(self) -> None: ...
    MaxIteration: int
    MaxKinematicIteration: int
    MaxSolverErrorExpression: Expression
    MaxStaticIteration: int
    MaxStepSizeExpression: Expression


class ActiveView(enum.Enum):
    All = 0
    Work = 1


