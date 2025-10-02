from . import Optimization
from . import ContactPreview
from . import PenetrationCheck
from . import QualityAudit
from . import ModelDependencyCheck
from . import FTK
from . import ModelCheck
from . import Connections
from . import ResponseSimulation
from . import AeroStructures
from . import MeshMapping
from . import Xyplot
from . import RotorDynamics
from ...NXOpen import *
from ..CAE import *

import typing
import enum

class XyFunctionUnitSystem(enum.Enum):
    Function = 0
    Model = 1
    MetricBase = 2
    EnglishBase = 3
    MetricCaeBase = 4
    EnglishCaeBase = 5
    Si = 6
    Custom = 7


class XyFunctionUnit(enum.Enum):
    Unknown = 0
    DisplacementM = 1
    DisplacementMm = 2
    DisplacementIn = 3
    DisplacementFt = 4
    DisplacementCm = 126
    DisplacementKm = 250
    DisplacementMi = 251
    DisplacementMicron = 252
    DisplacementNm = 253
    DisplacementAngstrom = 254
    ForceN = 5
    ForceMn = 6
    ForceBf = 7
    ForcePoundal = 91
    ForceCn = 127
    ForceKgf = 128
    TemperatureC = 8
    TemperatureF = 9
    TemperatureK = 10
    TemperatureR = 283
    TimeSec = 11
    TimeMin = 12
    TimeHour = 13
    FrequencyHz = 14
    FrequencyKhz = 284
    FrequencyMhz = 285
    FrequencyGhz = 286
    MassKg = 15
    MassG = 16
    MassBm = 17
    MassTon = 18
    MassLbfIn = 19
    MassSlug = 89
    MassKgfM = 129
    MassKgfMm = 130
    MassKgfCm = 131
    MassMg = 287
    VelocityM = 20
    VelocityMm = 21
    VelocityIn = 22
    VelocityFt = 23
    VelocityCm = 132
    VelocityKmHr = 255
    VelocityMiHr = 256
    VelocityFtMin = 257
    AccelerationM = 24
    AccelerationMm = 25
    AccelerationIn = 26
    AccelerationFt = 27
    AccelerationGs = 28
    AccelerationCm = 133
    AngularDisplacementRadian = 29
    AngularDisplacementDegree = 30
    AngularDisplacementRev = 167
    AngularDisplacementPiRad = 288
    AngularVelocityRadian = 31
    AngularVelocityDegree = 32
    AngularVelocityRevSec = 168
    AngularVelocityRevMin = 169
    AngularAccelerationRadian = 33
    AngularAccelerationDegree = 34
    AngularAccelerationRevSec2 = 170
    AngularAccelerationRevMin2 = 171
    MomentMnMm = 35
    MomentNMm = 36
    MomentNM = 37
    MomentBfIn = 38
    MomentBfFt = 39
    MomentCnCm = 134
    MomentKgfM = 135
    MomentKgfMm = 136
    MomentKgfCm = 137
    PressureKpa = 40
    PressureMpa = 41
    PressurePa = 42
    PressurePsi = 43
    PressureLbfFt = 44
    PressureBar = 45
    PressureAt = 46
    PressureCnCm2 = 138
    PressureKgfCm2 = 139
    PressureKgfM2 = 140
    PressureKgfMm2 = 141
    PressureNCm2 = 289
    PressureMmH2o = 290
    PressureMmHg = 291
    PressureInH2o = 292
    PressureInHg = 293
    StressKpa = 47
    StressMpa = 48
    StressPa = 49
    StressPsi = 50
    StressLbfFt = 90
    StressCnCm2 = 142
    StressKgfM2 = 143
    StressKgfMm2 = 144
    StressKgfCm2 = 145
    StressNCm2 = 294
    StrainMm = 51
    StrainIn = 52
    StrainM = 146
    StrainCm = 147
    RpmRpm = 53
    RpmRadian = 316
    RpmDegree = 317
    RpmRevSec = 318
    OrderOrder = 54
    CyclesDuty = 55
    TorqueMnMm = 56
    TorqueNMm = 57
    TorqueNM = 58
    TorqueBfIn = 59
    TorqueBfFt = 60
    TorqueCnCm = 148
    TorqueKgfM = 149
    TorqueKgfMm = 150
    TorqueKgfCm = 151
    GravitationalAccelerationM = 61
    GravitationalAccelerationMm = 62
    GravitationalAccelerationIn = 63
    GravitationalAccelerationFt = 64
    GravitationalAccelerationGs = 65
    GravitationalAccelerationCm = 161
    ElementForceMnMm = 70
    ElementForceNMm = 71
    ElementForceNM = 72
    ElementForceBfIn = 73
    ElementForceBfFt = 74
    ElementForceCnCm = 152
    ElementForceKgfM = 153
    ElementForceKgfMm = 154
    ElementForceKgfCm = 155
    ElementForceJM2 = 295
    ElementMomentMnMm = 75
    ElementMomentNMm = 76
    ElementMomentNM = 77
    ElementMomentBfIn = 78
    ElementMomentBfFt = 79
    ElementMomentCnCm = 156
    ElementMomentKgfM = 157
    ElementMomentKgfMm = 158
    ElementMomentKgfCm = 159
    VoltageV = 80
    VoltageMv = 81
    VoltageMicrov = 296
    VoltageLbfInAS = 297
    ElectricCurrentA = 82
    ElectricCurrentMa = 83
    ElectricCurrentMicroa = 298
    LoadfactorNone = 84
    MotorSignalNone = 85
    UnitlessScalarNone = 86
    UnitlessRealNone = 87
    UnitlessIntegerNone = 88
    DampingMnMm = 92
    DampingNMm = 93
    DampingNM = 94
    DampingBfIn = 95
    DampingCnCm = 162
    DampingKgfM = 163
    DampingKgfMm = 164
    DampingKgfCm = 165
    DampingLbmSec = 299
    DampingKgSec = 300
    AreaM2 = 122
    AreaMm2 = 123
    AreaIn2 = 124
    AreaFt2 = 125
    AreaCm2 = 160
    MomentPerAngleMnMmDeg = 172
    MomentPerAngleMnMmRad = 173
    MomentPerAngleNMmDeg = 174
    MomentPerAngleNMmRad = 175
    MomentPerAngleNMDeg = 176
    MomentPerAngleNMRad = 177
    MomentPerAngleLbfInDeg = 178
    MomentPerAngleLbfInRad = 179
    MomentPerAngleLbfFtDeg = 180
    MomentPerAngleLbfFtRad = 181
    DynamicViscosityKgMSec = 182
    DynamicViscosityKgMmSec = 183
    DynamicViscosityGCmSec = 184
    DynamicViscosityLbfSecIn2 = 185
    DynamicViscosityLbfSecFt2 = 186
    DynamicViscosityLbmInSec = 187
    DynamicViscosityLbmFtSec = 188
    DynamicViscosityMnSecMm2 = 189
    DynamicViscosityNSecMm2 = 190
    DynamicViscosityNSecCm2 = 191
    DynamicViscosityNSecM2 = 192
    HeatFluxMicrowattMm2 = 205
    HeatFluxWattMm2 = 206
    HeatFluxBtuSecIn2 = 207
    HeatFluxMwattMm2 = 208
    HeatFluxWattCm2 = 209
    HeatFluxWattM2 = 210
    HeatFluxWattIn2 = 211
    HeatFluxBtuSecFt2 = 212
    HeatFluxBtuHrIn2 = 213
    HeatFluxBtuHrFt2 = 214
    HeatFluxLbfinSecIn2 = 215
    LengthPerAngleMmDeg = 268
    LengthPerAngleMmRad = 269
    LengthPerAngleMmRev = 270
    LengthPerAngleCmDeg = 271
    LengthPerAngleCmRad = 272
    LengthPerAngleCmRev = 273
    LengthPerAngleMDeg = 274
    LengthPerAngleMRad = 275
    LengthPerAngleMRev = 276
    LengthPerAngleInDeg = 277
    LengthPerAngleInRad = 278
    LengthPerAngleInRev = 279
    LengthPerAngleFtDeg = 280
    LengthPerAngleFtRad = 281
    LengthPerAngleFtRev = 282
    PowerLbmft2sp3 = 96
    PowerLbfinps = 97
    PowerMuw = 98
    PowerW = 99
    PowerKw = 100
    PowerMw = 101
    PowerBtuph = 102
    PowerBtupm = 103
    PowerBtups = 104
    FrequencySquaredHz2 = 303
    FrequencySquaredKhz2 = 304
    FrequencySquaredMhz2 = 305
    FrequencySquaredGhz2 = 306
    FrequencyCubedHz3 = 307
    FrequencyCubedKhz3 = 308
    FrequencyCubedMhz3 = 309
    FrequencyCubedGhz3 = 310
    Curv1M = 66
    Curv1Mm = 67
    Curv1In = 68
    Curv1Ft = 69
    Curv1Cm = 166
    Curv1Micron = 311
    Curv1Nm = 312
    Curv1Angstrom = 313
    Curv1Km = 314
    Curv1Mi = 315
    MassFlowKgSec = 105
    MassFlowGSec = 106
    MassFlowLbfSecFt = 107
    MassFlowLbfSecIn = 108
    MassFlowLbmSec = 109
    MassFlowKgHr = 110
    MassFlowKgMin = 111
    MassFlowGHr = 112
    MassFlowGMin = 113
    MassFlowLbmHr = 114
    MassFlowLbmMin = 115
    MassFlowMgSec = 116
    EnergyLbmFt2Sec2 = 117
    EnergyLbfin = 118
    EnergyMicroj = 119
    EnergyJ = 120
    EnergyBtu = 121
    EnergyMj = 301
    ConvectionCoefficientMicrowattMm2Degc = 193
    ConvectionCoefficientWattMm2Degc = 194
    ConvectionCoefficientBtuSecIn2Degf = 195
    ConvectionCoefficientMwattMm2Degc = 196
    ConvectionCoefficientWattCm2Degc = 197
    ConvectionCoefficientWattM2Degc = 198
    ConvectionCoefficientWattIn2Degc = 199
    ConvectionCoefficientBtuSecFt2Degf = 200
    ConvectionCoefficientBtuHrIn2Degf = 201
    ConvectionCoefficientBtuHrFt2Degf = 202
    ConvectionCoefficientLbfinSecIn2Degf = 203
    ConvectionCoefficientMwattMm2Degk = 204
    ConvectionCoefficientWM2Degk = 302
    MessDensityLbmFt3 = 216
    MessDensityMgMm3 = 217
    MessDensityGMm3 = 218
    MessDensityGCm3 = 219
    MessDensityKgM3 = 220
    MessDensityKgMm3 = 221
    MessDensityTM3 = 222
    MessDensityTMm3 = 223
    MessDensityLbfsec2In4 = 224
    MessDensitySlugFt3 = 225
    MessDensityLbmIn3 = 226
    SpecificHeatMicrojKgDegk = 227
    SpecificHeatJKgDegk = 228
    SpecificHeatKjKgDegk = 229
    SpecificHeatMjMgDegk = 230
    SpecificHeatBtuLbmDegf = 231
    SpecificHeatBtuInLbfSec2Degf = 232
    SpecificHeatLbfinLbmDegf = 233
    SpecificHeatLbfinInLbfSec2Degf = 234
    ThermalConductivityMicrowattMmDegc = 235
    ThermalConductivityWattMmDegc = 236
    ThermalConductivityWattMDegk = 237
    ThermalConductivityBtuSecInDegf = 238
    ThermalConductivityBtuHrFtDegf = 239
    ThermalConductivityWattMDegc = 240
    ThermalConductivityBtuHrInDegf = 241
    ThermalConductivityMwattMmDegc = 242
    ThermalConductivityWattCmDegc = 243
    ThermalConductivityMwattMmDegk = 244
    ThermalConductivityBtuSecFtDegf = 245
    ThermalConductivityLbfinSecInDegf = 246
    ThermalExpansionCoefficientDegc = 247
    ThermalExpansionCoefficientDegf = 248
    ThermalExpansionCoefficientDegk = 249
    VelocityPerPressureMm3NSec = 258
    VelocityPerPressureM3NSec = 259
    VelocityPerPressureMm3MnSec = 260
    VelocityPerPressureM3MnSec = 261
    VelocityPerPressureIn3LbfSec = 262
    VelocityPerPressureFt3LbfSec = 263
    VelocityPerPressureM2SecKg = 264
    VelocityPerPressureMm2SecKg = 265
    VelocityPerPressureIn2SecLbm = 266
    VelocityPerPressureFt2SecLbm = 267
    ForcePerAngleMnDeg = 319
    ForcePerAngleNDeg = 320
    ForcePerAngleLbfDeg = 321
    ForcePerAnglePoundalDeg = 322
    ForcePerAngleKgfDeg = 323
    ForcePerAngleCnDeg = 324
    ForcePerAngleMnRad = 325
    ForcePerAngleNRad = 326
    ForcePerAngleLbfRad = 327
    ForcePerAnglePoundalRad = 328
    ForcePerAngleKgfRad = 329
    ForcePerAngleCnRad = 330
    ForcePerLengthMnMm = 331
    ForcePerLengthNMm = 332
    ForcePerLengthNM = 333
    ForcePerLengthLbfIn = 334
    ForcePerLengthLbfFt = 335
    ForcePerLengthCnCm = 336
    ForcePerLengthKgfM = 337
    ForcePerLengthKgfMm = 338
    ForcePerLengthKgfCm = 339
    ForcePerLengthJM2 = 340
    Number = 341


class XyFunctionResponseType(enum.Enum):
    General = 0
    Time = 1
    Spectrum = 2
    PowerSpectralDensity = 3
    ShockResponseSpectrum = 4
    FrequencyResponseFunction = 5
    CrossSpectrum = 6
    Transmissibility = 7
    FastRmsFittedPsd = 8


class XyFunctionMotionType(enum.Enum):
    Time = 0
    TimingChart = 1
    StiffnessAndDamping = 2
    Vehicle = 3
    MotionGeneral = 4
    Number = 5


class XyFunctionMeasure(enum.Enum):
    General = 0
    Displacement = 1
    Force = 2
    Temperature = 3
    Time = 4
    Frequency = 5
    Mass = 6
    Velocity = 7
    Acceleration = 8
    AngularDisplacement = 9
    AngularVelocity = 10
    AngularAcceleration = 11
    Moment = 12
    Pressure = 13
    Stress = 14
    Strain = 15
    Rpm = 16
    Order = 17
    Cycles = 18
    Loadfactor = 19
    Torque = 20
    Gravity = 21
    Curvature = 22
    ElementForce = 23
    ElementMoment = 24
    MotorSignal = 25
    UnitlessScalar = 26
    UnitlessReal = 27
    UnitlessInteger = 28
    Voltage = 29
    ElectricCurrent = 30
    Damping = 31
    Power = 32
    MassFlow = 33
    Energy = 34
    Area = 35
    MomentPerAngle = 36
    DynamicViscosity = 37
    ConvectionCoefficient = 38
    HeatFlux = 39
    VelocityPerPressure = 40
    MessDensity = 41
    SpecificHeat = 42
    ThermalConductivity = 43
    ThermalExpansionCoefficient = 44
    LengthPerAngle = 45
    FrequencySquared = 46
    FrequencyCubed = 47
    ForcePerAngle = 48
    ForcePerLength = 49
    Number = 50


class XyFunctionMaterialType(enum.Enum):
    General = 0
    Time = 1
    Temperature = 2
    StressStrain = 3
    Life = 4


class XyFunctionMacroType(enum.Enum):
    General = 0
    Motion = 1
    Response = 2
    Load = 3
    Material = 4


class XyFunctionLoadType(enum.Enum):
    General = 0
    Time = 1
    Spectrum = 2
    PowerSpectralDensity = 3
    ShockResponseSpectrum = 4
    FastRmsFittedPsd = 5


class XyFunctionGeneralType(enum.Enum):
    General = 0
    Time = 1
    Spectrum = 2
    PowerSpectralDensity = 3
    ShockResponseSpectrum = 4
    FrequencyResponseFunction = 5
    Temperature = 6
    StressStrain = 7
    Life = 8
    CrossSpectrum = 9
    Transmissibility = 10
    CampbellDiagram = 11
    TimingChart = 12
    StiffnessAndDamping = 13
    FastRmsFittedPsd = 14
    Vehicle = 15
    MotionGeneral = 16
    Number = 17


class XyFunctionDataType(enum.Enum):
    General = 0
    Time = 1
    CrossSpectrum = 3
    FrequencyResponseFunction = 4
    Transmissibility = 5
    PowerSpectralDensity = 9
    Spectrum = 12
    ShockResponseSpectrum = 24
    Temperature = 31
    StressStrain = 32
    Life = 33
    CampbellDiagram = 34
    TimingChart = 35
    StiffnessAndDamping = 36
    FastRmsFittedPsd = 37
    Vehicle = 38
    MotionGeneral = 39
    AutoPower = 40
    CrossPower = 41


class XyFunctionDataComplexType(enum.Enum):
    RealOnly = 0
    RealImaginary = 1
    MagnitudePhase = 2


class WireframeFromDOFSetBuilder(Builder):
    def __init__(self) -> None: ...
    Dofset: CAE.CaeDOFSet
    MaxDistanceRatio: float
    MaxNumberOfWiresPerNode: int
    MinAngleBetweenWires: Expression


class WireframeElementsBuilder(Builder):
    def __init__(self) -> None: ...
    MaxDistanceRatio: float
    MaxNumberOfNodes: int
    MaxNumberOfWiresPerNode: int
    MinAngleBetweenWires: Expression
    MinDistance: Expression
    Nodes: CAE.SelectFENodeList
    UseSizeReduction: bool


class WeldRow(CAE.MeshControl):
    def __init__(self) -> None: ...


class WeldBuilder(Builder):
    def __init__(self) -> None: ...
    DistanceBetween: Expression
    EdgeSelection: SelectTaggedObjectList
    ElementSideASelection: CAE.SelectElementsBuilder
    ElementSideBSelection: CAE.SelectElementsBuilder
    ElementType: CAE.ElementTypeBuilder
    EndOffset: Expression
    FlipState: int
    InputFile: str
    Location: CAE.WeldBuilder.WeldLocation
    LocationType: CAE.WeldBuilder.WeldLocationType
    NodeSelection: CAE.SelectFENodeList
    NumberOfPointsOnEdge: int
    NumberOfPointsOption: CAE.WeldBuilder.NumberOfPointsOnEdgeType
    OffsetDistance: Expression
    OffsetVector: Direction
    Pattern: str
    PointOnEdgeOption: CAE.WeldBuilder.PointOnEdgeType
    PointSideA: SelectTaggedObjectList
    PointSideB: SelectTaggedObjectList
    PointsSelection: SelectTaggedObjectList
    SearchDistance: Expression
    SideAPid: CAE.NamedPropertyTable
    SideBPid: CAE.NamedPropertyTable
    SpecifiedNumberOfPoints: int
    StartOffset: Expression
    SupportAllPids: bool
    WeldType: CAE.WeldBuilder.WeldConnectionType


    class WeldLocationType(enum.Enum):
        Single = 0
        TwoSide = 1
    

    class WeldLocation(enum.Enum):
        Point = 0
        File = 1
        Edge = 2
        Node = 3
    

    class WeldConnectionType(enum.Enum):
        Partpat = 0
        Elpat = 1
    

    class PointOnEdgeType(enum.Enum):
        ByNumber = 0
        ByDistance = 1
        ByPattern = 2
    

    class NumberOfPointsOnEdgeType(enum.Enum):
        MaximumNumber = 0
        SpecifiedNumber = 1
    

class ViewportSynchronizationOptions(TaggedObject):
    def __init__(self) -> None: ...
    def ConnectViewport(self, viewportIndex: int) -> None:
        ...
    def DisconnectViewport(self, viewportIndex: int) -> None:
        ...
    def DisconnectAllViewports(self) -> None:
        ...
    def IsViewportConnected(self, viewportIndex: int) -> bool:
        ...
    def Destroy(self) -> None:
        ...
    def SetSynchronizedStackSelection(self, viewportIndex: int, synchronize: bool) -> None:
        ...
    def IsStackSelectionSynchronized(self, viewportIndex: int) -> bool:
        ...


class ViewLayoutManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def SetArrangement(self, arrangementType: CAE.ViewLayoutManager.ArrangementType) -> None:
        ...
    def GetViewXY(self, viewXY: typing.List[CAE.ViewLayoutManager.ViewXY]) -> None:
        ...
    def SetViewXY(self, viewIndex: int, viewXY: CAE.ViewLayoutManager.ViewXY) -> None:
        ...
    def ReturnToModel(self, viewIndex: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    Arrangement: CAE.ViewLayoutManager.ArrangementType


    class ViewLayoutManagerViewXY():
        XMin: float
        XMax: float
        YMin: float
        YMax: float
        def ToString(self) -> str:
            ...
    

    class ArrangementType(enum.Enum):
        Ly1 = 0
        Ly2v = 1
        Ly2h = 2
        Ly4 = 3
        Ly6v = 4
        Ly9 = 5
        Ly3 = 6
        Ly3h = 7
        Ly6h = 8
    

class ViewLaminateBuilder(Builder):
    def __init__(self) -> None: ...


class VatvSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.VatvSet]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self, pVatvSet: CAE.VatvSet) -> CAE.VatvSetBuilder:
        ...
    def Find(self, name: str) -> CAE.VatvSet:
        ...
    def Delete(self, atvSetTag: CAE.VatvSet) -> None:
        ...
    def Tag(self) -> Tag: ...



class VatvSetBuilder(CAE.AlternateFemRepresentationSourceBuilder):
    def __init__(self) -> None: ...


class VatvSet(CAE.AlternateFemRepresentationSource):
    def __init__(self) -> None: ...


class UserDefinedSolidBeamSectionBuilder(CAE.IBeamSectionBuilder):
    def __init__(self) -> None: ...
    DescriptorName: str
    DirectionType: CAE.BeamSection.DirectionOption
    ReferenceVector: Direction
    SolidFace: CAE.SelectCAEFace


class UserDefinedSolidBeamSection(CAE.BeamSection):
    def __init__(self) -> None: ...


class UnStitchEdgeBuilder(Builder):
    def __init__(self) -> None: ...
    SourceEdgeSelection: CAE.SelectCAEEdgeList


class UnifiedDatabaseOptions(CAE.DataReaderDatabaseOptions):
    def __init__(self) -> None: ...
    def GetFlags(self) -> typing.List[CAE.UnifiedDatabaseOptions.Flag]:
        ...
    def SetFlags(self, flags: typing.List[CAE.UnifiedDatabaseOptions.Flag]) -> None:
        ...
    DisplayName: str
    Name: str


    class UnifiedDatabaseOptionsFlag():
        FlagName: str
        FlagSet: bool
        def ToString(self) -> str:
            ...
        def __init__(self, FlagName: str, FlagSet: bool) -> None: ...
    

    class UnifiedDatabaseOptions_Flag():
        flagName: int
        flagSet: bool
    

class Type(enum.Enum):
    All = 0
    OnlyFeature = 1
    Free = 2
    Nonmanifold = 3
    FreeAndNonmanifold = 4


class TransientResultsReductionBuilder(CAE.ResultsManipulationBuilder):
    def __init__(self) -> None: ...
    def SetResult(self, result: CAE.Result, parameters: typing.List[CAE.ResultParameters], names: str) -> None:
        ...
    def SetLastIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    def SetFormula(self, formula: str) -> None:
        ...
    def SetIncompatibleResultsOption(self, incompatibleResultsOption: CAE.TransientResultsReductionBuilder.IncompatibleResults) -> None:
        ...
    def SetNoDataOption(self, noDataOption: CAE.TransientResultsReductionBuilder.NoData) -> None:
        ...
    def SetEvaluationErrorOption(self, evaluationErrorOption: CAE.TransientResultsReductionBuilder.EvaluationError) -> None:
        ...


    class NoData(enum.Enum):
        Skip = 0
        ZeroFill = 1
    

    class IncompatibleResults(enum.Enum):
        Skip = 0
        Abort = 1
    

    class EvaluationError(enum.Enum):
        Skip = 0
        ZeroFill = 1
        Abort = 2
    

class ThicknessPlotContoursBuilder(Builder):
    def __init__(self) -> None: ...
    def SetMeshesToPlot(self, pMeshTags: typing.List[CAE.Mesh]) -> None:
        ...
    def CreatePlotObject(self) -> CAE.ThicknessPlotContours:
        ...


class ThicknessPlotContours(TaggedObject):
    def __init__(self) -> None: ...
    def PlotContour(self, viewIndex: int) -> None:
        ...


class ThicknessBuilder(Builder):
    def __init__(self) -> None: ...
    def GetNodeThickness(self, node: TaggedObject, fFound: bool) -> float:
        ...
    def GetElementThickness(self, element: TaggedObject, fFound: bool) -> float:
        ...
    def Plot(self) -> None:
        ...
    def Clear(self) -> None:
        ...
    def CreateField(self) -> None:
        ...
    AllMeshContext: bool
    Element: CAE.SelectElementsBuilder
    EntityOption: CAE.ThicknessBuilder.EntityType
    HighThicknessColor: NXColor
    LowThicknessColor: NXColor
    MeshContext: CAE.Mesh
    MidThicknessColor: NXColor
    Node: CAE.SelectFENodeList
    Scale: float
    ZeroThicknessColor: NXColor


    class EntityType(enum.Enum):
        Node = 0
        Element = 1
    

class ThickenMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def AutomaticThicknessValue(self) -> None:
        ...
    ElementType: CAE.ElementTypeBuilder
    SelectMesh: SelectTaggedObjectList
    ThicknessValue: Expression


class ThermoOpticalPropMgr(TaggedObject):
    def __init__(self) -> None: ...
    def Export(self, fileName: str, selectedObjects: typing.List[NXObject]) -> None:
        ...
    def ImportFromXml(self, fileName: str) -> None:
        ...
    def Destroy(self) -> None:
        ...


class TestModelCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.TestModel]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.TestModel:
        ...
    def DeleteTestModel(self, testModel: CAE.TestModel) -> None:
        ...
    def GetInformation(self, testModels: typing.List[CAE.TestModel]) -> None:
        ...
    def Tag(self) -> Tag: ...



class TestModel(NXObject):
    def __init__(self) -> None: ...
    def Align(self, alignmentMatrix: Matrix4x4, alignMode: CAE.TestModel.AlignMode) -> None:
        ...
    def Reset(self) -> None:
        ...
    def AlignXml(self, fileName: str) -> None:
        ...
    def ExportAlignment(self, fileName: str) -> None:
        ...
    def Show(self, show: bool) -> None:
        ...
    def Rename(self, name: str) -> None:
        ...
    CorrelTestNodes: CAE.CorrelTestNodeCollection


    class AlignMode(enum.Enum):
        Compound = 0
        Reset = 1
        ProvidedXform = 2
    

class TargetEntitiesBuilder(Builder):
    def __init__(self) -> None: ...
    def SetGroupObjects(self, entityObjs: typing.List[CAE.CaeGroup]) -> None:
        ...
    EntitiesType: CAE.TargetEntitiesBuilder.Type
    GroupMoreState: bool
    GroupToggle: bool
    Selection: SelectTaggedObjectList


    class Type(enum.Enum):
        Nodes = 0
        Elements = 1
    

class TargetEntities(NXObject):
    def __init__(self) -> None: ...


class TangentFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class TangentContinuousEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEdges(self) -> typing.List[CAE.CAEEdge]:
        ...


class SweptMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class SweepBetweenMeshBuilder(Builder):
    def __init__(self) -> None: ...
    AutomaticSweepBetween: CAE.AutomaticSweepBetweenSelection
    ElementType: CAE.ElementTypeBuilder
    ManualSweepBetween: CAE.ManualSweepBetweenSelection
    NumLayers: int
    Type: CAE.SweepBetweenMeshBuilder.Types


    class Types(enum.Enum):
        Automatic = 0
        Manual = 1
    

class SwapDiagonalBuilder(Builder):
    def __init__(self) -> None: ...
    FirstElement: CAE.SelectElementsBuilder
    SecondElement: CAE.SelectElementsBuilder


class SurfaceCoatBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> CAE.Mesh:
        ...
    ElementFace: CAE.SelectElementsBuilder
    ElementType: CAE.ElementTypeBuilder
    ExportToSolver: bool
    SelectGeometry: SelectTaggedObjectList
    SelectionMethodType: CAE.SurfaceCoatBuilder.SelectionMethod
    SourceMesh: SelectTaggedObjectList


    class SelectionMethod(enum.Enum):
        ThreeDimensionMesh = 0
        ElementFreeFace = 1
        Geometry = 2
    

class SuppressHoleBuilder(Builder):
    def __init__(self) -> None: ...
    BodySelect: SelectTaggedObjectList
    Choice: CAE.SuppressHoleBuilder.OptionChoice
    EdgeSelect: SelectTaggedObjectList
    HoleDiameter: Expression
    PointCreate: CAE.SuppressHoleBuilder.OptionPointCreate


    class OptionPointCreate(enum.Enum):
        None = 0
        Point = 1
        MeshPoint = 2
    

    class OptionChoice(enum.Enum):
        Automatic = 0
        Manual = 1
    

class StressLinearizationResult(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetMembrane(self) -> typing.List[CAE.StressLinearizationResult.StressState]:
        ...
    def GetBending(self) -> typing.List[CAE.StressLinearizationResult.StressState]:
        ...
    def GetMembranePlusBending(self) -> typing.List[CAE.StressLinearizationResult.StressState]:
        ...
    def GetPeak(self) -> typing.List[CAE.StressLinearizationResult.StressState]:
        ...
    def GetTotal(self) -> typing.List[CAE.StressLinearizationResult.StressState]:
        ...
    def GetContext(self) -> typing.List[CAE.StressLinearizationResult.Context]:
        ...
    def FreeResource(self) -> None:
        ...
    AverageTemperature: float
    AverageTemperatureLoad: float
    IterationIndex: int
    IterationName: str
    SubcaseName: str


    class StressLinearizationResultStressState():
        Location: Point3d
        XLocal: float
        XX: float
        YY: float
        ZZ: float
        XY: float
        YZ: float
        ZX: float
        Sigma11: float
        Sigma22: float
        Sigma33: float
        MaxShear: float
        Intensity: float
        VonMises: float
        def ToString(self) -> str:
            ...
    

    class StressLinearizationResultContext():
        Location: Point3d
        XLocal: float
        Temperature: float
        TemperatureLoad: float
        def ToString(self) -> str:
            ...
    

class StressLinearizationMgr(TaggedObject):
    def __init__(self) -> None: ...


class StressLinearizationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.StressLinearization]:
        ...
    def __init__(self, owner: CAE.SimSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.StressLinearization:
        ...
    def GetStressLinearizationMgr(self) -> CAE.StressLinearizationMgr:
        ...
    def Tag(self) -> Tag: ...



class StressLinearizationBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, desc: str) -> None:
        ...
    def GetLoadCaseNames(self) -> str:
        ...
    def SetLoadCaseNames(self, lcName: str) -> None:
        ...
    def GetSubcases(self) -> typing.List[CAE.SimSolutionStep]:
        ...
    def SetSubcases(self, subcases: typing.List[CAE.SimSolutionStep]) -> None:
        ...
    def GetBendingTensorComponents(self) -> bool:
        ...
    def SetBendingTensorComponents(self, bendingComps: bool) -> None:
        ...
    ExtractTemperature: bool
    ExtractTemperatureLoad: bool
    Iteration: int
    IterationRange: str
    IterationSelection: CAE.StressLinearization.ResultSelection
    LoadCaseName: str
    LoadCaseSelection: CAE.StressLinearization.LcaseSelection
    Name: str
    ResultType: CAE.StressLinearization.ResultType
    Rho: Expression
    RhoInfinite: bool
    Scl: CAE.QueryCurveUsageOptions
    StructureType: CAE.StressLinearization.StructureTypes
    Subcase: CAE.SimSolutionStep
    TemperatureResultType: CAE.StressLinearization.ResultTypeTemperature


class StressLinearization(NXObject):
    def __init__(self) -> None: ...
    def GetLoadCaseNames(self) -> str:
        ...
    def GetResultType(self) -> CAE.StressLinearization.ResultType:
        ...
    def Compute(self, parameters: CAE.StressLinearization.Parameters, membranes: typing.List[CAE.StressLinearization.StressState], bendings: typing.List[CAE.StressLinearization.StressState], membranePlusBending: typing.List[CAE.StressLinearization.StressState], peaks: typing.List[CAE.StressLinearization.StressState], totals: typing.List[CAE.StressLinearization.StressState]) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.StressLinearization.ComputeAll to take all iterations into account.")"""
        ...
    def ComputeAll(self, parameters: CAE.StressLinearization.Parameters, results: typing.List[CAE.StressLinearizationResult]) -> None:
        ...
    def GetMax(self, slresults: typing.List[CAE.StressLinearizationResult], tensorType: CAE.StressLinearization.TensorType, tensorComponent: CAE.StressLinearization.TensorComponent, lcName: str, location: float, iteration: int) -> CAE.StressLinearization.ExtremumResult:
        ...
    def GetMin(self, slresults: typing.List[CAE.StressLinearizationResult], tensorType: CAE.StressLinearization.TensorType, tensorComponent: CAE.StressLinearization.TensorComponent, lcName: str, location: float, iteration: int) -> CAE.StressLinearization.ExtremumResult:
        ...
    def GetWorst(self, slresults: typing.List[CAE.StressLinearizationResult], tensorType: CAE.StressLinearization.TensorType, tensorComponent: CAE.StressLinearization.TensorComponent, lcName: str, location: float, iteration: int) -> CAE.StressLinearization.ExtremumResult:
        ...
    AnyIteration: int
    AnyLoadCase: str
    AnyLocation: float
    BendingComponents: CAE.StressLinearization.BendingTensorComponents
    Description: str
    ExtractTemperature: bool
    ExtractTemperatureLoad: bool
    Iteration: int
    IterationRange: str
    IterationSelection: CAE.StressLinearization.ResultSelection
    LoadCaseName: str
    LoadCaseSelection: CAE.StressLinearization.LcaseSelection
    Name: str
    NumIntervals: int
    Rho: Expression
    RhoInfinite: bool
    Scl: CAE.QueryCurve
    SclEnds: CAE.StressLinearization.SclEndsSupports
    StructureType: CAE.StressLinearization.StructureTypes
    TemperatureResultType: CAE.StressLinearization.ResultTypeTemperature


    class TensorType(enum.Enum):
        Membrane = 0
        Bending = 1
        MembranePlusBending = 2
        Peak = 3
        Total = 4
    

    class TensorComponent(enum.Enum):
        Xx = 0
        Yy = 1
        Zz = 2
        Xy = 3
        Yz = 4
        Zx = 5
        Sigma11 = 6
        Sigma22 = 7
        Sigma33 = 8
        MaxShear = 9
        Intensity = 10
        VonMises = 11
    

    class StructureTypes(enum.Enum):
        Nonaxisymmetric = 0
        Axisymmetric = 1
    

    class StressLinearizationStressState():
        Location: Point3d
        XLocal: float
        XX: float
        YY: float
        ZZ: float
        XY: float
        YZ: float
        ZX: float
        Sigma11: float
        Sigma22: float
        Sigma33: float
        MaxShear: float
        Intensity: float
        VonMises: float
        def ToString(self) -> str:
            ...
    

    class SclEndsSupports(enum.Enum):
        Unknown = -1
        Points = 0
        Nodes = 1
    

    class ResultTypeTemperature(enum.Enum):
        Nodal = 0
        Elemental = 1
    

    class ResultType(enum.Enum):
        StressElemental = 0
        StressElementNodal = 1
    

    class ResultSelection(enum.Enum):
        First = 0
        Last = 1
        Index = 2
        All = 3
        FirstToIndex = 4
        IndexToLast = 5
        ByName = 6
    

    class StressLinearizationParameters():
        A: Point3d
        B: Point3d
        AxisSymmetry: Vector3d
        AxisRadial: Vector3d
        LocalCsys: Matrix3x3
        RA: float
        RB: float
        RC: float
        T: float
        CosPhi: float
        Xf: float
        Xh: float
        D: float
        def ToString(self) -> str:
            ...
    

    class LcaseSelection(enum.Enum):
        ByList = 0
        Range = 1
        All = 2
    

    class StressLinearizationExtremumResult():
        Stress: float
        Extras: CAE.StressLinearization.ExtremumExtras
        def ToString(self) -> str:
            ...
        def __init__(self, Stress: float, Extras: CAE.StressLinearization.ExtremumExtras) -> None: ...
    

    class StressLinearizationExtremumExtras():
        Location: Point3d
        XLocal: float
        LcName: str
        IterName: str
        IterIndex: int
        Temperature: float
        TemperatureLoad: float
        def ToString(self) -> str:
            ...
    

    class StressLinearizationBendingTensors():
        XX: bool
        YY: bool
        ZZ: bool
        XY: bool
        YZ: bool
        ZX: bool
        def ToString(self) -> str:
            ...
    

    class StressLinearizationBendingTensorComponents():
        XX: bool
        YY: bool
        ZZ: bool
        XY: bool
        YZ: bool
        ZX: bool
        def ToString(self) -> str:
            ...
    

    class StressLinearization_ExtremumResult():
        stress: float
        extras: CAE.StressLinearization._ExtremumExtras
    

    class StressLinearization_ExtremumExtras():
        location: Point3d
        xLocal: float
        lcName: int
        iterName: int
        iterIndex: int
        temperature: float
        temperatureLoad: float
    

class StlImportBuilder(Builder):
    def __init__(self) -> None: ...
    ElementType: CAE.ElementTypeBuilder
    FileUnits: CAE.StlImportBuilder.StlFileUnitType
    ReportSummary: bool
    StlFileBrowser: str


    class StlFileUnitType(enum.Enum):
        PartUnits = 0
        Meters = 1
        Millimeters = 2
        Inches = 3
    

class StepManager(CAE.LbcAssociationMgr):
    def __init__(self) -> None: ...
    def AddBc(self, tSolutionStep: CAE.SimSolutionStep, tBc: CAE.SimBC) -> None:
        ...
    def RemoveBc(self, tSolutionStep: CAE.SimSolutionStep, tBc: CAE.SimBC) -> None:
        ...
    def AddFolder(self, tSolutionStep: CAE.SimSolutionStep, tBc: CAE.SimLbcFolder) -> None:
        ...
    def RemoveFolder(self, tSolutionStep: CAE.SimSolutionStep, tBc: CAE.SimLbcFolder) -> None:
        ...
    def ScaleBc(self, tSolution: CAE.SimSolutionStep, tBc: CAE.SimBC, scale: float) -> None:
        ...
    def ScaleFolder(self, tSolution: CAE.SimSolutionStep, tBc: CAE.SimLbcFolder, scale: float) -> None:
        ...
    def AddLoadset(self, tSolutionStep: CAE.SimSolutionStep, tBc: CAE.SimLoadSet) -> None:
        ...
    def RemoveLoadset(self, tSolutionStep: CAE.SimSolutionStep, tBc: CAE.SimLoadSet) -> None:
        ...
    def ScaleLoadset(self, tSolution: CAE.SimSolutionStep, tBc: CAE.SimLoadSet, scale: float) -> None:
        ...
    def AddGlobalBc(self, tBc: CAE.SimBC) -> None:
        ...
    def RemoveGlobalBc(self, tBc: CAE.SimBC) -> None:
        ...
    def AddGlobalFolder(self, tBc: CAE.SimLbcFolder) -> None:
        ...
    def RemoveGlobalFolder(self, tBc: CAE.SimLbcFolder) -> None:
        ...
    def ScaleGlobalBc(self, tBc: CAE.SimBC, scale: float) -> None:
        ...
    def ScaleGlobalFolder(self, tBc: CAE.SimLbcFolder, scale: float) -> None:
        ...
    def AddGlobalLoadset(self, tBc: CAE.SimLoadSet) -> None:
        ...
    def RemoveGlobalLoadset(self, tBc: CAE.SimLoadSet) -> None:
        ...
    def ScaleGlobalLoadset(self, tBc: CAE.SimLoadSet, scale: float) -> None:
        ...


class StandardIdealizedBeamSectionBuilder(CAE.StandardBeamSectionBuilder):
    def __init__(self) -> None: ...


class StandardBeamSectionBuilder(CAE.IBeamSectionBuilder):
    def __init__(self) -> None: ...
    DescriptorName: str


class StandardBeamSection(CAE.BeamSection):
    def __init__(self) -> None: ...


class SpringEADBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentEndAState: CAE.SpringEADBuilder.State
    ComponentEndBState: CAE.SpringEADBuilder.State
    Elements: CAE.SelectElementsBuilder
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.SpringEADBuilder.State
    RotationalComponentEndA: CAE.SpringEADBuilder.RotationalComponentEnd
    RotationalComponentEndB: CAE.SpringEADBuilder.RotationalComponentEnd
    RotationalStiffness: Expression
    StiffnessState: CAE.SpringEADBuilder.State
    TranslationalComponentEndA: CAE.SpringEADBuilder.TranslationalComponentEnd
    TranslationalComponentEndB: CAE.SpringEADBuilder.TranslationalComponentEnd
    TranslationalStiffness: Expression


    class TranslationalComponentEnd(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class State(enum.Enum):
        Apply = 0
        Clear = 1
        Ignore = 2
    

    class RotationalComponentEnd(enum.Enum):
        Rx = 0
        Ry = 1
        Rz = 2
    

class SpiderElementBuilder(Builder):
    def __init__(self) -> None: ...
    CollectorName: str
    CoreNode: CAE.SelectFENode
    Label: int
    LegNodes: CAE.SelectFENodeList
    MeshName: str
    NeutralName: str
    NewMeshOption: CAE.SpiderElementBuilder.NewMeshType


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

class SpiderCoreNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class SphereBoundingVolume(CAE.BoundingVolumePrimitive):
    def __init__(self) -> None: ...
    def GetCenterDiameter(self, centerPoint: Point, diameter: Expression) -> None:
        ...
    def SetCenterDiameter(self, centerPoint: Point, diameter: Expression) -> None:
        ...
    def GetCenterDiameters(self, centerPoint: Point, innerDiameter: Expression, outerDiameter: Expression) -> None:
        ...
    def SetCenterDiameters(self, centerPoint: Point, innerDiameter: Expression, outerDiameter: Expression) -> None:
        ...


class SolverAppendOption(NXObject):
    def __init__(self) -> None: ...
    def GetHighestNodeLabel(self) -> int:
        ...
    def GetHighestElementLabel(self) -> int:
        ...
    def GetHighestCoordinateSystemLabel(self) -> int:
        ...
    def GetHighestPhysicalPropertyLabel(self) -> int:
        ...
    def GetHighestOthersLabel(self) -> int:
        ...
    CoordinateSystemOffset: int
    DoAppendMerge: bool
    ElementOffset: int
    ImportBehavior: CAE.SolverAppendOption.ImportBehaviorOption
    MaterialMergeOption: CAE.SolverAppendOption.MergeOption
    NodeMergeOption: CAE.SolverAppendOption.MergeOption
    NodeOffset: int
    OthersOffset: int
    PhysicalPropertyOffset: int
    PptMergeOption: CAE.SolverAppendOption.MergeOption
    SolutionMergeOption: CAE.SolverAppendOption.SolutionOption
    SolverName: str


    class SolutionOption(enum.Enum):
        DontCreate = 0
        CreateNew = 1
    

    class MergeOption(enum.Enum):
        UseExisting = 0
        ModifyExisting = 1
        AppendNew = 2
    

    class ImportBehaviorOption(enum.Enum):
        AppendModel = 0
        MergeWithExisting = 1
    

class SolutionResult(CAE.Result):
    def __init__(self) -> None: ...
    def CombineLoadcases(self, part: CAE.SimPart, solution: CAE.SimSolution, lcaseas: typing.List[CAE.SimSolutionStep], factors: float, desc: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded function with Result Reference instead.")"""
        ...
    def CombineLoadcases(self, part: CAE.SimPart, tResultRef: CAE.SimResultReference, lcaseas: typing.List[CAE.SimSolutionStep], factors: float, desc: str) -> None:
        ...
    Solution: CAE.SimSolution


class SolutionManager(CAE.LbcAssociationMgr):
    def __init__(self) -> None: ...
    def AddBc(self, tSolution: CAE.SimSolution, tBc: CAE.SimBC) -> None:
        ...
    def RemoveBc(self, tSolution: CAE.SimSolution, tBc: CAE.SimBC) -> None:
        ...
    def AddFolder(self, tSolution: CAE.SimSolution, tBc: CAE.SimLbcFolder) -> None:
        ...
    def RemoveFolder(self, tSolution: CAE.SimSolution, tBc: CAE.SimLbcFolder) -> None:
        ...
    def ScaleBc(self, tSolution: CAE.SimSolution, tBc: CAE.SimBC, scale: float) -> None:
        ...
    def ScaleFolder(self, tSolution: CAE.SimSolution, tBc: CAE.SimLbcFolder, scale: float) -> None:
        ...
    def AddLoadset(self, tSolution: CAE.SimSolution, tBc: CAE.SimLoadSet) -> None:
        ...
    def RemoveLoadset(self, tSolution: CAE.SimSolution, tBc: CAE.SimLoadSet) -> None:
        ...
    def ScaleLoadset(self, tSolution: CAE.SimSolution, tBc: CAE.SimLoadSet, scale: float) -> None:
        ...


class SolidPropertyCheckBuilder(Builder):
    def __init__(self) -> None: ...
    def SetElementsForValueRequest(self, elements: typing.List[CAE.FEElement]) -> None:
        ...
    def GetSolidPropertyValues(self, valueTypes: typing.List[CAE.SolidPropertyCheckBuilder.ValueRequest], valueUnits: typing.List[Unit], values: float) -> None:
        ...
    def GetCenterOfGravity(self, cgUnit: Unit) -> Vector3d:
        ...
    def GetCenterOfGravityMomentOfInertia(self, mmoiUnit: Unit) -> Matrix3x3:
        ...
    def GetGlobalMomentOfInertia(self, mmoiUnit: Unit) -> Matrix3x3:
        ...
    def GetReferenceCsysMomentOfInertia(self, mmoiUnit: Unit) -> Matrix3x3:
        ...
    def GetPrincipalMomentOfInertia(self, mmoiUnit: Unit) -> Matrix3x3:
        ...
    def GetPrincipalAxes(self) -> Matrix3x3:
        ...
    CoupledSolutionOption: CAE.SolidPropertyCheckBuilder.CoupledSolutionOutput
    DefaultTemperatureOption: bool
    DisplayCgOption: bool
    Elements: CAE.SelectElementsBuilder
    EvaluationTemparature: Expression
    GroupObject: TaggedObject
    GroupOption: bool
    MeshObject: CAE.Mesh
    MeshOption: bool
    OutputOption: bool
    ReferenceCsys: CoordinateSystem
    SplitMass: bool
    UserSpecifiedUnit: CAE.SolidPropertyCheckBuilder.UserUnit
    ValueRequestOption: bool


    class ValueRequest(enum.Enum):
        Volume = 0
        TotalMass = 1
        StructuralMass = 2
        NonStructuralMass = 3
        SurfaceArea = 4
        TotalMassThermalCapacitance = 5
        StructuralMassThermalCapacitance = 6
        NonStructuralMassThermalCapacitance = 7
        Length = 8
    

    class UserUnit(enum.Enum):
        DefaultUnit = 0
        KgMilli = 1
        LbmIn = 2
        LbfInSec = 3
    

    class CoupledSolutionOutput(enum.Enum):
        Structural = 0
        Thermal = 1
    

class SolidEADBuilder(Builder):
    def __init__(self) -> None: ...
    Elements: CAE.SelectElementsBuilder
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.SolidEADBuilder.State


    class State(enum.Enum):
        Apply = 0
        Clear = 1
        Ignore = 2
    

class SMTOutputBuilder(Builder):
    def __init__(self) -> None: ...
    def SetNfrList(self, nfrList: typing.List[CAE.NodalForceReport]) -> None:
        ...
    AxialForceZ: bool
    BendingMomentX: bool
    BendingMomentY: bool
    GraphNamePrefix: str
    Iteration: CAE.BaseIteration
    Loadcase: CAE.BaseLoadcase
    ShearForceX: bool
    ShearForceY: bool
    SubIteration: CAE.BaseIteration
    TorqueZ: bool


    class Outsmttype(enum.Enum):
        ShearForceX = 0
        ShearForceY = 1
        ShearForceZ = 2
        BendingMomentX = 3
        BendingMomentY = 4
        TorqueZ = 5
    

class SMTDiagramsBuilder(Builder):
    def __init__(self) -> None: ...
    AllnodesToggle: bool
    BoundingBoxZdirLinearDim: Expression
    Coordsys: CoordinateSystem
    CsysTypeEnum: CAE.SMTDiagramsBuilder.Csystype
    ElemSelectEntities: CAE.TargetEntitiesBuilder
    ForceTypeEnum: CAE.SMTDiagramsBuilder.Forcetype
    NodeSelectEntities: CAE.TargetEntitiesBuilder
    QueryCurveUsageOptions: CAE.QueryCurveUsageOptions


    class Forcetype(enum.Enum):
        GridPoint = 0
        Reaction = 1
        Mpc = 2
        Applied = 3
        Glue = 4
        Contact = 5
    

    class Csystype(enum.Enum):
        Global = 0
        Cartesian = 1
        Cylindrical = 2
        Spherical = 3
    

class SmoothOptResultsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSolidAreaColor(self) -> float:
        ...
    def SetSolidAreaColor(self, solidAreaColor: float) -> None:
        ...
    def GetLatticeAreaColor(self) -> float:
        ...
    def SetLatticeAreaColor(self, latticeAreaColor: float) -> None:
        ...
    def DisplayUpdate(self) -> None:
        ...
    def Export(self) -> None:
        ...
    def CreateVerificationSolution(self) -> None:
        ...
    AdditionalSmoothingOption: CAE.SmoothOptResultsBuilder.AdditionalSmoothingType
    AutomaticDisplayOption: bool
    GenerateBdf: bool
    GenerateDensityCsv: bool
    GenerateStl: bool
    Iteration: int
    LoadCase: int
    LowerBoundLatticeArea: float
    LowerBoundSolidArea: float
    Result: CAE.Result
    SmoothDisplayOption: bool
    SmoothLevel: float
    Solution: CAE.SimSolution
    ViewPortIndex: int


    class AdditionalSmoothingType(enum.Enum):
        None = 0
        Laplace = 1
    

class SmartSelectionManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateAdjacentFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.AdjacentFaceMethod:
        ...
    def CreateAdjacentFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.AdjacentFaceMethod:
        ...
    def CreateAdjacentFaceMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.AdjacentFaceMethod:
        ...
    def CreateCircularEdgeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        ...
    def CreateCylinderFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        ...
    def CreateCylinderFaceMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        ...
    def CreateCylinderFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        ...
    def CreatePathEnclosedElemFaceMethod(self, inputMethod: CAE.ElemEdgePathMethod, doEntityVisibilityCheck: bool, flipLoopDirection: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.PathEnclosedElemFaceMethod:
        ...
    def CreateEdgePathMethod(self, seedEdgeTag: CAE.CAEEdge, seedStartVertexTag: CAE.CAEVertex, preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float, pathMethodType: CAE.PathType, dTangentAngleTolerance: float) -> CAE.EdgePathMethod:
        ...
    def CreateClosedEdgePathMethod(self, seedEdgeTag: CAE.CAEEdge, flipEdge: bool) -> CAE.EdgePathMethod:
        ...
    def CreateElemEdgePathMethod(self, seedElemEdgeTag: CAE.FEElemEdge, seedStartNodeTag: CAE.FENode, preferFreeEdges: bool, preferGeometryAssociatedEdges: bool, preferFeatureElementEdge: bool, featureAngleTolerance: float, allowGapJumping: bool, gapJumpingTolerance: float, pathMethodType: CAE.PathType, dTangentAngleTolerance: float) -> CAE.ElemEdgePathMethod:
        ...
    def CreateFeatureEdgeNodeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewFeatureEdgeNodeMethodFromMethod.")"""
        ...
    def CreateFeatureEdgeNodeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewFeatureEdgeNodeMethodFromElemEdges.")"""
        ...
    def NewFeatureEdgeNodeMethodOptions(self) -> CAE.FeatureEdgeNodeMethodOptions:
        ...
    def CreateNewFeatureEdgeNodeMethodFromMethod(self, inputMethod: SelectionMethod, options: CAE.FeatureEdgeNodeMethodOptions) -> CAE.FeatureEdgeNodeMethod:
        ...
    def CreateNewFeatureEdgeNodeMethodFromElemEdges(self, seedTags: typing.List[CAE.FEElemEdge], options: CAE.FeatureEdgeNodeMethodOptions) -> CAE.FeatureEdgeNodeMethod:
        ...
    def CreateFeatureElemEdgeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        ...
    def CreateFeatureElemEdgeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        ...
    def CreateFeatureElemEdgeMethod(self, seedTags: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        ...
    def CreateFeatureElemFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureElemFaceMethod:
        ...
    def CreateFeatureElemFaceMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureElemFaceMethod:
        ...
    def CreateFeatureElemMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureElemMethod:
        ...
    def CreateFeatureElemMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureElemMethod:
        ...
    def CreateFeatureShellElemMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureShellElemMethod:
        ...
    def CreateFeatureShellElemMethod(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureShellElemMethod:
        ...
    def CreateFeatureNodeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewFeatureNodeMethodFromMethod.")"""
        ...
    def CreateFeatureNodeMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewFeatureNodeMethodFromElemFaces.")"""
        ...
    def NewFeatureNodeMethodOptions(self) -> CAE.FeatureNodeMethodOptions:
        ...
    def CreateNewFeatureNodeMethodFromMethod(self, inputMethod: SelectionMethod, options: CAE.FeatureNodeMethodOptions) -> CAE.FeatureNodeMethod:
        ...
    def CreateNewFeatureNodeMethodFromElemFaces(self, seedTags: typing.List[CAE.FEElemFace], options: CAE.FeatureNodeMethodOptions) -> CAE.FeatureNodeMethod:
        ...
    def CreateFilletFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        ...
    def CreateFilletFaceMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        ...
    def CreateFilletFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        ...
    def CreateGroupMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupMethod:
        ...
    def CreateGroupElemMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool, elemOption: CAE.GroupElemMethodElemOption.ElemOption) -> CAE.GroupElemMethod:
        ...
    def CreateGroupElemEdgeMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupElemEdgeMethod:
        ...
    def CreateGroupElemFaceMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupElemFaceMethod:
        ...
    def CreateGroupEdgeMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupEdgeMethod:
        ...
    def CreateGroupFaceMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupFaceMethod:
        ...
    def CreateGroupNodeMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewGroupNodeMethod.")"""
        ...
    def CreateNewGroupNodeMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.GroupNodeMethod:
        ...
    def CreateShowAdjacentGroupMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.ShowAdjacentGroupMethod:
        ...
    def CreateShowHideGroupMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.ShowHideGroupMethod:
        ...
    def CreateOrderedEdgeNodeMethod(self, seed: CAE.CAEEdge, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeNodeMethod:
        ...
    def CreateOrderedEdgeNodeMethod(self, seed: Line, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeNodeMethod:
        ...
    def CreateOrderedEdgeNodeMethod(self, seed: Arc, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeNodeMethod:
        ...
    def CreateOrderedEdgeNodeMethod(self, seed: Conic, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeNodeMethod:
        ...
    def CreateOrderedEdgeNodeMethod(self, seed: Spline, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeNodeMethod:
        ...
    def CreateOrderedEdgeElemMethod(self, seed: CAE.CAEEdge, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeElemMethod:
        ...
    def CreateOrderedEdgeElemMethod(self, seed: Line, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeElemMethod:
        ...
    def CreateOrderedEdgeElemMethod(self, seed: Arc, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeElemMethod:
        ...
    def CreateOrderedEdgeElemMethod(self, seed: Conic, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeElemMethod:
        ...
    def CreateOrderedEdgeElemMethod(self, seed: Spline, doEntityVisibilityCheck: bool, flipSeedStart: bool) -> CAE.OrderedEdgeElemMethod:
        ...
    def CreateOrderedFeatureEdgeNodeMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, flipSeedStart: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.OrderedFeatureEdgeNodeMethod:
        ...
    def CreateOrderedFeatureEdgeElemMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, flipSeedStart: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.OrderedFeatureEdgeNodeMethod:
        ...
    def CreateRelatedCurveMethod(self, seeds: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedCurveMethod:
        ...
    def CreateRelatedCurveMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedCurveMethod:
        ...
    def CreateRelatedCurveMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedCurveMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedCurveMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedCurveMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedEdgeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.CAEVertex], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.MeshControl], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seed: CAE.CAEEdge, doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seed: Spline, doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes argument selectOnly3DElementsFaces.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes argument selectOnly3DElementsFaces.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes argument selectOnly3DElementsFaces.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes as input an array of NXOpen.CAE.Mesh objects.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seed: CAE.CAEFace, doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects.")"""
        ...
    def CreateRelatedElemMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Line], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Arc], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Conic], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Spline], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Point], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: CAE.CAEBody, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: CAE.CAEFace, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: CAE.CAEEdge, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: CAE.FENode, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: Line, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: Arc, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: Conic, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTag: Spline, doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seed: CAE.FENode, doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seedTag: CAE.FEElemFace, seedElemFaceId: int, doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedNodeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromMethod.")"""
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.MeshControl], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromMeshes.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromBodies.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromFaces.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromEdges.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEVertex], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromVertices.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromElems.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.MeshPoint], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromMeshPoints.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Point], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromPoints.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Line], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromLines.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Arc], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromArcs.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Conic], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromConics.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Spline], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromSplines.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromElemEdges.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromElemFaces.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromMesh.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEBody, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromBody.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEFace, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromFace.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEEdge, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromEdge.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.FEElement, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromElem.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.MeshPoint, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromMeshPoint.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: Point, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromPoint.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: Line, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromLine.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: Arc, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromArc.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: Conic, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromConic.")"""
        ...
    def CreateRelatedNodeMethod(self, seed: Spline, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromSpline.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromElemEdge.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTag: CAE.FEElemFace, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewRelatedNodeMethodFromElemFace.")"""
        ...
    def CreateNewRelatedNodeMethodFromMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromMeshes(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromBodies(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromFaces(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromEdges(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromVertices(self, seeds: typing.List[CAE.CAEVertex], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromElems(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromMeshPoints(self, seedTags: typing.List[CAE.MeshPoint], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromPoints(self, seedTags: typing.List[Point], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromLines(self, seedTags: typing.List[Line], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromArcs(self, seedTags: typing.List[Arc], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromConics(self, seedTags: typing.List[Conic], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromSplines(self, seedTags: typing.List[Spline], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromElemEdges(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromElemFaces(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromMesh(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromBody(self, seed: CAE.CAEBody, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromFace(self, seed: CAE.CAEFace, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromEdge(self, seed: CAE.CAEEdge, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromElem(self, seed: CAE.FEElement, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromMeshPoint(self, seed: CAE.MeshPoint, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromPoint(self, seed: Point, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromLine(self, seed: Line, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromArc(self, seed: Arc, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromConic(self, seed: Conic, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromSpline(self, seed: Spline, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromElemEdge(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateNewRelatedNodeMethodFromElemFace(self, seedTag: CAE.FEElemFace, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedVertexMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedVertexMethod:
        ...
    def CreateRelatedVertexMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedVertexMethod:
        ...
    def CreateRelatedVertexMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedVertexMethod:
        ...
    def CreateRelatedVertexMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedVertexMethod:
        ...
    def CreateRelatedVertexMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedVertexMethod:
        ...
    def CreateRelatedVertexMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedVertexMethod:
        ...
    def CreateShortEdgeMethodFromMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, dEdgeTolerance: float) -> CAE.ShortEdgeMethod:
        ...
    def CreateShortEdgeMethodFromBodies(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, dEdgeTolerance: float) -> CAE.ShortEdgeMethod:
        ...
    def CreateShortEdgeMethodFromFaces(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dEdgeTolerance: float) -> CAE.ShortEdgeMethod:
        ...
    def CreateShortEdgeMethodFromEdges(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool, dEdgeTolerance: float) -> CAE.ShortEdgeMethod:
        ...
    def CreateSliverFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, dSliverTolerance: float) -> CAE.SliverFaceMethod:
        ...
    def CreateSliverFaceMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, dSliverTolerance: float) -> CAE.SliverFaceMethod:
        ...
    def CreateSliverFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dSliverTolerance: float) -> CAE.SliverFaceMethod:
        ...
    def CreateTangentFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, stopAtNonManifoldJunctions: bool, dTangentTolerance: float) -> CAE.TangentFaceMethod:
        ...
    def CreateTangentFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, stopAtNonManifoldJunctions: bool, dTangentTolerance: float) -> CAE.TangentFaceMethod:
        ...
    def CreateTangentContinuousEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool, dFeatureAngle: float) -> CAE.TangentContinuousEdgeMethod:
        ...
    def CreateTangentContinuousEdgeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, dFeatureAngle: float) -> CAE.TangentContinuousEdgeMethod:
        ...
    def CreateHoleElementEdgeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, dMinElementEdgeHoleRadius: float, dMaxElementEdgeHoleRadius: float, allowNonCircularHoles: bool) -> CAE.HoleElementEdgeMethod:
        ...
    def CreateHoleElementEdgeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool, dMinElementEdgeHoleRadius: float, dMaxElementEdgeHoleRadius: float, allowNonCircularHoles: bool) -> CAE.HoleElementEdgeMethod:
        ...
    def CreateHoleElementEdgeMethod(self, seedElemEdgeTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, dMinElementEdgeHoleRadius: float, dMaxElementEdgeHoleRadius: float, allowNonCircularHoles: bool) -> CAE.HoleElementEdgeMethod:
        ...
    def CreateElemLabelMethod(self, doEntityVisibilityCheck: bool, startLabel: int, endLabel: int, labelIncrement: int) -> CAE.ElemLabelMethod:
        ...
    def CreateNodeLabelMethod(self, doEntityVisibilityCheck: bool, startLabel: int, endLabel: int, labelIncrement: int) -> CAE.NodeLabelMethod:
        ...
    def CreateFilterElemMethod(self, seeds: typing.List[CAE.FEElement], physical: CAE.NamedPropertyTable, material: PhysicalMaterial, neutraltype: int, thicknessCriteria: CAE.Criteria, minThickness: float, maxThickness: float, thicknesses: float) -> CAE.FilterElemMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFilterElemMethod.")"""
        ...
    def CreateFilterElemMethod(self, inputMethod: SelectionMethod, physical: CAE.NamedPropertyTable, material: PhysicalMaterial, neutraltype: int, thicknessCriteria: CAE.Criteria, minThickness: float, maxThickness: float, thicknesses: float) -> CAE.FilterElemMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFilterElemMethod.")"""
        ...
    def CreateFilterElemMethod(self, seeds: typing.List[CAE.FEElement], physical: CAE.NamedPropertyTable, material: PhysicalMaterial, elemDimension: CAE.ElementTypes.Dimension, neutralType: CAE.ElementTypes.NeutralType, thicknessCriteria: CAE.Criteria, minThickness: float, maxThickness: float, thicknesses: float) -> CAE.FilterElemMethod:
        ...
    def CreateFilterElemMethod(self, inputMethod: SelectionMethod, physical: CAE.NamedPropertyTable, material: PhysicalMaterial, elemDimension: CAE.ElementTypes.Dimension, neutralType: CAE.ElementTypes.NeutralType, thicknessCriteria: CAE.Criteria, minThickness: float, maxThickness: float, thicknesses: float) -> CAE.FilterElemMethod:
        ...
    def CreateFilterElemMethodFromModel(self, doEntityVisibilityCheck: bool, physical: CAE.NamedPropertyTable, material: PhysicalMaterial, elemDimension: CAE.ElementTypes.Dimension, neutralType: CAE.ElementTypes.NeutralType, thicknessCriteria: CAE.Criteria, minThickness: float, maxThickness: float, thicknesses: float) -> CAE.FilterElemMethod:
        ...
    def CreateFilterNodeMethod(self, seeds: typing.List[CAE.FENode], selectOnlyCornerNodes: bool) -> CAE.FilterNodeMethod:
        ...
    def CreateFilterNodeMethodFromMethod(self, inputMethod: SelectionMethod, selectOnlyCornerNodes: bool) -> CAE.FilterNodeMethod:
        ...
    def CreateFilterNodeMethodFromModel(self, doEntityVisibilityCheck: bool, selectOnlyCornerNodes: bool) -> CAE.FilterNodeMethod:
        ...
    def CreateFilterBodyMethod(self, seeds: typing.List[CAE.CAEBody], material: PhysicalMaterial, filterbyVolume: bool, minVolume: float, maxVolume: float) -> CAE.FilterBodyMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFilterBodyMethod which takes argument bodyType.")"""
        ...
    def CreateFilterBodyMethod(self, inputMethod: SelectionMethod, material: PhysicalMaterial, filterbyVolume: bool, minVolume: float, maxVolume: float) -> CAE.FilterBodyMethod:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFilterBodyMethod which takes argument bodyType.")"""
        ...
    def CreateFilterFaceMethod(self, seeds: typing.List[CAE.CAEFace], minArea: float, maxArea: float) -> CAE.FilterFaceMethod:
        ...
    def CreateFilterFaceMethod(self, inputMethod: SelectionMethod, minArea: float, maxArea: float) -> CAE.FilterFaceMethod:
        ...
    def CreateFilterEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], minLength: float, maxLength: float) -> CAE.FilterEdgeMethod:
        ...
    def CreateFilterEdgeMethod(self, inputMethod: SelectionMethod, minLength: float, maxLength: float) -> CAE.FilterEdgeMethod:
        ...
    def CreateFilterBodyMethod(self, inputMethod: SelectionMethod, material: PhysicalMaterial, filterbyVolume: bool, minVolume: float, maxVolume: float, bodyType: CAE.BodyType) -> CAE.FilterBodyMethod:
        ...
    def CreateFilterBodyMethod(self, seeds: typing.List[CAE.CAEBody], material: PhysicalMaterial, filterbyVolume: bool, minVolume: float, maxVolume: float, bodyType: CAE.BodyType) -> CAE.FilterBodyMethod:
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool, facePreference: CAE.FacePref) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1953.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes argument Free Face Computation.")"""
        ...
    def CreateRelatedElemFaceMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, facePreference: CAE.FacePref) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1953.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes argument Free Face Computation.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, facePreference: CAE.FacePref) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1953.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes argument Free Face Computation.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, facePreference: CAE.FacePref) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX1953.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes argument Free Face Computation.")"""
        ...
    def CreateSpiderCoreNodeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.SpiderCoreNodeMethod:
        ...
    def CreateSpiderCoreNodeMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.SpiderCoreNodeMethod:
        ...
    def CreateAttachedElemMethod(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, isLimitIterations: bool, numIterations: int, attachedByOption: CAE.AttachedByOption) -> CAE.AttachedElemMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewAttachedElemMethodFromElems.")"""
        ...
    def CreateAttachedElemMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, isLimitIterations: bool, numIterations: int, attachedByOption: CAE.AttachedByOption) -> CAE.AttachedElemMethod:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.SmartSelectionManager.CreateNewAttachedElemMethodFromMethod.")"""
        ...
    def CreateRelatedElemFaceMethodFromMeshes(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool, facePreference: CAE.FacePref, computeFreeFacesOnVisibleModel: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemFaceMethodFromMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, nodeRelationship: CAE.NodeRelationshipType, facePreference: CAE.FacePref, computeFreeFacesOnVisibleModel: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemFaceMethodFromFaces(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, facePreference: CAE.FacePref, computeFreeFacesOnVisibleModel: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemFaceMethodFromElems(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, facePreference: CAE.FacePref, computeFreeFacesOnVisibleModel: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemFaceMethodFromNodes(self, seedTags: typing.List[CAE.FENode], doEntityVisibilityCheck: bool, nodeRelationship: CAE.NodeRelationshipType, facePreference: CAE.FacePref, computeFreeFacesOnVisibleModel: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedBodyMethodFromMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.RelatedBodyMethod:
        ...
    def CreateRelatedBodyMethodFromNodes(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedBodyMethod:
        ...
    def CreateRelatedBodyMethodFromElems(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool) -> CAE.RelatedBodyMethod:
        ...
    def CreateRelatedBodyMethodFromMeshes(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedBodyMethod:
        ...
    def CreateRelatedBodyMethodFromFaces(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedBodyMethod:
        ...
    def CreateRelatedBodyMethodFromEdges(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedBodyMethod:
        ...
    def CreateRelatedBodyMethodFromVertices(self, seeds: typing.List[CAE.CAEVertex], doEntityVisibilityCheck: bool) -> CAE.RelatedBodyMethod:
        ...
    def CreateNewAttachedElemMethodFromElems(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, doJumpContactandGluing: bool, isLimitIterations: bool, numIterations: int, attachedByOption: CAE.AttachedByOption) -> CAE.AttachedElemMethod:
        ...
    def CreateNewAttachedElemMethodFromMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool, doJumpContactandGluing: bool, isLimitIterations: bool, numIterations: int, attachedByOption: CAE.AttachedByOption) -> CAE.AttachedElemMethod:
        ...
    def CreateFreeElemEdgeMethodFromElems(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool) -> CAE.FreeElemEdgeMethod:
        ...
    def CreateFreeElemEdgeMethodFromMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.FreeElemEdgeMethod:
        ...
    def CreateFreeElemFaceMethodFromElems(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool) -> CAE.FreeElemFaceMethod:
        ...
    def CreateFreeElemFaceMethodFromMethod(self, inputMethod: SelectionMethod, doEntityVisibilityCheck: bool) -> CAE.FreeElemFaceMethod:
        ...
    def Tag(self) -> Tag: ...



class SliverFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class SketchCurvesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SketchCurves]:
        ...
    def __init__(self, owner: CAE.BaseFemPart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.SketchCurves:
        ...
    def Tag(self) -> Tag: ...



class SketchCurves(NXObject):
    def __init__(self) -> None: ...


class SingleLabelSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    def SetLabel(self, label: int) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeSingleLabelStrategy.SetLabel instead.")"""
        ...
    Label: int


class SimulationInterface(NXObject):
    def __init__(self) -> None: ...
    def AddBc(self, bc: CAE.SimBC) -> None:
        ...
    def RemoveBc(self, bc: CAE.SimBC) -> None:
        ...
    def AddFolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def RemoveFolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def AddLoadSet(self, loadSet: CAE.SimLoadSet) -> None:
        ...
    def RemoveLoadSet(self, loadSet: CAE.SimLoadSet) -> None:
        ...
    def AddConstraintSet(self, set: CAE.SimConstraintSet) -> None:
        ...
    def RemoveConstraintSet(self, set: CAE.SimConstraintSet) -> None:
        ...


class SimSoundProcessingTreatmentsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimSoundProcessingTreatment]:
        ...
    def __init__(self, owner: CAE.SimSoundProcessing) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.SimSoundProcessingTreatment:
        ...
    def CreateBuilder(self, treatmentType: CAE.SimSoundProcessingTreatmentsCollection.TreatmentType) -> CAE.SimSoundProcessingTreatmentBuilder:
        ...
    def EditBuilder(self, source: CAE.SimSoundProcessingTreatment) -> CAE.SimSoundProcessingTreatmentBuilder:
        ...
    def Delete(self, source: CAE.SimSoundProcessingTreatment) -> None:
        ...
    def Tag(self) -> Tag: ...



    class TreatmentType(enum.Enum):
        Ocss = 0
        Ifft = 1
    

class SimSoundProcessingTreatmentBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str


class SimSoundProcessingTreatment(NXObject):
    def __init__(self) -> None: ...


class SimSoundProcessingTracksCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimSoundProcessingTrack]:
        ...
    def __init__(self, owner: CAE.SimSoundProcessing) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.SimSoundProcessingTrack:
        ...
    def CreateBuilder(self) -> CAE.SimSoundProcessingTrackBuilder:
        ...
    def Create(self) -> CAE.SimSoundProcessingTrack:
        ...
    def Delete(self, track: CAE.SimSoundProcessingTrack) -> None:
        ...
    def Tag(self) -> Tag: ...



class SimSoundProcessingTrackBuilder(Builder):
    def __init__(self) -> None: ...
    Gain: int
    IsEnabled: bool
    Name: str
    Source: CAE.SimSoundProcessingSource
    Treatment: CAE.SimSoundProcessingTreatment


class SimSoundProcessingTrack(NXObject):
    def __init__(self) -> None: ...
    Gain: int
    ImpulseResponse: CAE.SimSoundProcessingImpulseResponse
    IsEnabled: bool
    Source: CAE.SimSoundProcessingSource
    Treatment: CAE.SimSoundProcessingTreatment


class SimSoundProcessingSourcesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimSoundProcessingSource]:
        ...
    def __init__(self, owner: CAE.SimSoundProcessing) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.SimSoundProcessingSource:
        ...
    def CreateBuilder(self, sourceType: CAE.SimSoundProcessingSourcesCollection.SourceType) -> CAE.SimSoundProcessingSourceBuilder:
        ...
    def EditBuilder(self, source: CAE.SimSoundProcessingSource) -> CAE.SimSoundProcessingSourceBuilder:
        ...
    def Delete(self, source: CAE.SimSoundProcessingSource) -> None:
        ...
    def Tag(self) -> Tag: ...



    class SourceType(enum.Enum):
        DataFile = 0
        Audio = 1
    

class SimSoundProcessingSourceBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str


class SimSoundProcessingSource(NXObject):
    def __init__(self) -> None: ...


class SimSoundProcessingOCSSTreatmentBuilder(CAE.SimSoundProcessingTreatmentBuilder):
    def __init__(self) -> None: ...
    RpmProfile: Fields.ScalarFieldWrapper


class SimSoundProcessingOCSSTreatment(CAE.SimSoundProcessingTreatment):
    def __init__(self) -> None: ...


class SimSoundProcessingImpulseResponsesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimSoundProcessingImpulseResponse]:
        ...
    def __init__(self, owner: CAE.SimSoundProcessing) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.SimSoundProcessingImpulseResponse:
        ...
    def CreateBuilder(self, irType: CAE.SimSoundProcessingImpulseResponsesCollection.ImpulseResponseType) -> CAE.SimSoundProcessingImpulseResponseBuilder:
        ...
    def EditBuilder(self, impulseResponse: CAE.SimSoundProcessingImpulseResponse) -> CAE.SimSoundProcessingImpulseResponseBuilder:
        ...
    def Delete(self, impulseResponse: CAE.SimSoundProcessingImpulseResponse) -> None:
        ...
    def Tag(self) -> Tag: ...



    class ImpulseResponseType(enum.Enum):
        DataFile = 0
        Audio = 1
    

class SimSoundProcessingImpulseResponseBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str


class SimSoundProcessingImpulseResponse(NXObject):
    def __init__(self) -> None: ...


class SimSoundProcessingDataSourceOptions(NXObject):
    def __init__(self) -> None: ...
    def Plot(self, deviceIndex: int, viewportIndex: int) -> None:
        ...
    BinauralOnly: bool
    DataSetName: str
    DatabaseOptions: CAE.DataReaderDatabaseOptions
    FileName: str
    NodeLabel: int
    SubcaseName: str


class SimSoundProcessingDataSource(NXObject):
    def __init__(self) -> None: ...


class SimSoundProcessingDataFileSourceBuilder(CAE.SimSoundProcessingSourceBuilder):
    def __init__(self) -> None: ...
    DataSource: CAE.SimSoundProcessingDataSourceOptions


class SimSoundProcessingDataFileSource(CAE.SimSoundProcessingSource):
    def __init__(self) -> None: ...


class SimSoundProcessingDataFileImpulseResponseBuilder(CAE.SimSoundProcessingImpulseResponseBuilder):
    def __init__(self) -> None: ...
    DataSource: CAE.SimSoundProcessingDataSourceOptions
    EnableUpperTimeLimit: bool
    UpperTimeLimit: Expression


class SimSoundProcessingDataFileImpulseResponse(CAE.SimSoundProcessingImpulseResponse):
    def __init__(self) -> None: ...


class SimSoundProcessingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimSoundProcessing]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def Create(self) -> CAE.SimSoundProcessing:
        ...
    def Delete(self, soundProcessing: CAE.SimSoundProcessing) -> None:
        ...
    def FindObject(self, name: str) -> CAE.SimSoundProcessing:
        ...
    def Tag(self) -> Tag: ...



class SimSoundProcessingAudioSourceBuilder(CAE.SimSoundProcessingSourceBuilder):
    def __init__(self) -> None: ...
    def Play(self, playInLoop: bool) -> None:
        ...
    def Stop(self) -> None:
        ...
    def Plot(self, deviceIndex: int, viewportIndex: int) -> None:
        ...
    EnableNormalization: bool
    EnableWavUpperTimeLimit: bool
    FileName: str
    NormalizationValue: int
    RmsNormalization: bool
    WavUpperTimeLimit: Expression


class SimSoundProcessingAudioSource(CAE.SimSoundProcessingSource):
    def __init__(self) -> None: ...


class SimSoundProcessing(NXObject):
    def __init__(self) -> None: ...
    def Play(self, loop: bool) -> None:
        ...
    def Stop(self) -> None:
        ...
    def Plot(self, deviceIndex: int, viewportIndex: int) -> None:
        ...
    def Save(self, fileName: str) -> None:
        ...
    Sources: CAE.SimSoundProcessingSourcesCollection
    Treatments: CAE.SimSoundProcessingTreatmentsCollection
    ImpulseResponses: CAE.SimSoundProcessingImpulseResponsesCollection
    Tracks: CAE.SimSoundProcessingTracksCollection
    Name: str


class SimSolveManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetSimSolveManager(self, owner: Session) -> CAE.SimSolveManager:
        ...
    def GetChainOfPrerequisites(self, pSol: CAE.SimSolution, pSolutions: typing.List[CAE.SimSolution], hasResult: bool) -> None:
        ...
    def SolveChainOfSolutions(self, pSolutions: typing.List[CAE.SimSolution], solveOption: CAE.SimSolution.SolveOption, setupCheckOption: CAE.SimSolution.SetupCheckOption, runModeOption: CAE.SimSolution.SolveMode, numSolutionsSolved: int, numSolutionsFailed: int, numSolutionsSkipped: int) -> None:
        ...
    def SolveAllSolutions(self, solveOption: CAE.SimSolution.SolveOption, setupCheckOption: CAE.SimSolution.SetupCheckOption, runModeOption: CAE.SimSolution.SolveMode, skipSolutionWithResults: bool, numSolutionsSolved: int, numSolutionsFailed: int, numSolutionsSkipped: int) -> None:
        ...
    def SolveAllMetaSolutions(self, solveOption: CAE.SimSolution.SolveOption, setupCheckOption: CAE.SimSolution.SetupCheckOption, runModeOption: CAE.SimSolution.SolveMode, skipSolutionWithResults: bool, numSolutionsSolved: int, numSolutionsFailed: int, numSolutionsSkipped: int) -> None:
        ...
    def Tag(self) -> Tag: ...



class SimSolutionStep(CAE.SimGroupContainer):
    def __init__(self) -> None: ...
    def AddBc(self, bc: CAE.SimBC) -> None:
        ...
    def RemoveBc(self, bc: CAE.SimBC) -> None:
        ...
    def RemoveAllConstraints(self) -> None:
        ...
    def RemoveAllLoads(self) -> None:
        ...
    def RemoveAllSimulationObjects(self) -> None:
        ...
    def AddFolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def RemoveFolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def GetBcs(self) -> typing.List[CAE.SimBC]:
        ...
    def GetFolders(self) -> typing.List[CAE.SimLbcFolder]:
        ...
    def GetUnfolderedBcs(self) -> typing.List[CAE.SimBC]:
        ...
    def CloneStep(self, suggestedName: str) -> CAE.SimSolutionStep:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    PropertyTable: CAE.PropertyTable
    Solution: CAE.SimSolution
    StepType: int


class SimSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimSolution]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class SimSolution(CAE.SimGroupContainer):
    def __init__(self) -> None: ...
    def Rename(self, name: str, renameResults: bool) -> None:
        ...
    def AddStep(self, step: CAE.SimSolutionStep) -> None:
        ...
    def CreateStep(self, stepType: int, stepName: str) -> CAE.SimSolutionStep:
        ...
    def CreateStep(self, stepType: int, makeActive: bool, stepName: str) -> CAE.SimSolutionStep:
        ...
    def CreateStep(self, stepType: int, makeActive: bool, stepName: str, position: CAE.SimSolution.StepPosition, relativeStep: CAE.SimSolutionStep) -> CAE.SimSolutionStep:
        ...
    def MoveStep(self, stepToMove: CAE.SimSolutionStep, position: CAE.SimSolution.StepPosition, relativeStep: CAE.SimSolutionStep) -> None:
        ...
    def DeleteStep(self, step: CAE.SimSolutionStep) -> None:
        ...
    def GetStepByIndex(self, stepIndex: int) -> CAE.SimSolutionStep:
        ...
    def AddPrerequisite(self, prerequisite: CAE.SimSolution) -> None:
        ...
    def RemovePrerequisite(self, prerequisite: CAE.SimSolution) -> None:
        ...
    def GetDisplayNameOfSolverType(self) -> str:
        ...
    def GetDisplayNameOfSolutionType(self) -> str:
        ...
    def AddBc(self, bc: CAE.SimBC) -> None:
        ...
    def RemoveBc(self, bc: CAE.SimBC) -> None:
        ...
    def RemoveAllConstraints(self) -> None:
        ...
    def RemoveAllLoads(self) -> None:
        ...
    def RemoveAllSimulationObjects(self) -> None:
        ...
    def AddFolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def RemoveFolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def GetBcs(self) -> typing.List[CAE.SimBC]:
        ...
    def GetFolders(self) -> typing.List[CAE.SimLbcFolder]:
        ...
    def GetUnfolderedBcs(self) -> typing.List[CAE.SimBC]:
        ...
    def Solve(self, solveOption: CAE.SimSolution.SolveOption, setupCheckOption: CAE.SimSolution.SetupCheckOption) -> None:
        ...
    def GetConflictBcPairByIndex(self, index: int, tBc1: CAE.SimBC, tGroupContainer1: CAE.SimGroupContainer, tBc2: CAE.SimBC, tGroupContainer2: CAE.SimGroupContainer, ignored: bool) -> None:
        ...
    def GetConflictBcOverrideByIndex(self, index: int, tBc: CAE.SimBC, tGroupContainer: CAE.SimGroupContainer, tOverride: CAE.Override, ignored: bool) -> None:
        ...
    def CreateConflictResolutionBuilder(self, tStep: CAE.SimGroupContainer, tBc1: CAE.SimBC, tBc2: CAE.SimBC) -> CAE.ConflictResolutionBuilder:
        ...
    def CreateConflictResolutionBuilder(self, tBc1: CAE.SimBC, tStep1: CAE.SimGroupContainer, tBc2: CAE.SimBC, tStep2: CAE.SimGroupContainer) -> CAE.ConflictResolutionBuilder:
        ...
    def CreateConflictResolutionBuilder(self, tBc: CAE.SimBC, tStep: CAE.SimGroupContainer, tOverride: CAE.Override) -> CAE.ConflictResolutionBuilder:
        ...
    def ApplySolverLanguageExportOptions(self, propertyList: CAE.CaeDataContainer) -> None:
        ...
    def SetFemValidInPost(self, valid: bool) -> None:
        ...
    def SetTimePropsFromConditionSequence(self, conditionSeqeunce: CAE.SimConditionSequence) -> None:
        ...
    def SetTimePropsFromConditionSequence(self, conditionSeqeunce: CAE.SimConditionSequence, numSteps: int) -> None:
        ...
    def SetTimePropsFromConditionSequence(self, conditionSeqeunce: CAE.SimConditionSequence, stepSize: float, stepUnit: Unit) -> None:
        ...
    def CreateResultProbeBuilder(self, resultProbe: CAE.ResultProbe) -> CAE.ResultProbeBuilder:
        ...
    def CreateNodalForceReportBuilder(self, nodalForceReport: CAE.NodalForceReport) -> CAE.NodalForceReportBuilder:
        ...
    def CreateStressLinearizationBuilder(self, stressLin: CAE.StressLinearization) -> CAE.StressLinearizationBuilder:
        ...
    def CreateSmtDiagramsBuilder(self) -> CAE.SMTDiagramsBuilder:
        ...
    def CreateSmtOutputBuilder(self) -> CAE.SMTOutputBuilder:
        ...
    def GetResultReferenceByIndex(self, resultIndex: int) -> CAE.SimResultReference:
        ...
    def UpdateFromLoadRecipe(self) -> None:
        ...
    def DetachLoadRecipe(self) -> None:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def GetAllResultProbes(self, resultProbes: typing.List[CAE.ResultProbe]) -> None:
        ...
    def CheckAnalysisQuality(self) -> None:
        ...
    def RegisterResults(self) -> bool:
        ...
    def VerifyResults(self) -> CAE.SimSolution.EnumVerifyResults:
        ...
    def UnregisterResults(self) -> None:
        ...
    def GetApplicationObjectManagerByName(self, name: str) -> CAE.IApplicationObjectManager:
        ...
    def GetReferenceSet(self) -> ReferenceSet:
        ...
    def SetReferenceSet(self, refset: ReferenceSet) -> None:
        ...
    def CreateOptimizeLatticeBuilder(self) -> CAE.OptimizeLatticeBuilder:
        ...
    def CreateExportLatticeDiameterFieldBuilder(self) -> CAE.ExportLatticeDiameterFieldBuilder:
        ...
    def CreateReport(self, templateFile: str, reportName: str, listError: bool) -> Report.Report:
        ...
    def GetReports(self, pReports: typing.List[Report.Report]) -> None:
        ...
    StressLinearizations: CAE.StressLinearizationCollection
    AbstractionType: CAE.SimSimulation.AxisymAbstractionType
    ActiveStep: CAE.SimSolutionStep
    AllowedStepTypeCount: int
    AnalysisType: str
    AttachedLoadRecipe: CAE.SimLoadRecipe
    ConflictBcOverrideCount: int
    ConflictBcPairCount: int
    PropertyTable: CAE.PropertyTable
    ResultReferenceCount: int
    SolutionType: str
    SolverOptionsPropertyTable: CAE.PropertyTable
    SolverType: str
    StepCount: int


    class StepPosition(enum.Enum):
        First = 0
        Last = 1
        Before = 2
        After = 3
    

    class SolveOption(enum.Enum):
        Solve = 0
        WriteSolverInputFile = 1
        SolveInputFile = 2
        WriteEditAndSolveInputFile = 3
        EditSolverInputFile = 4
        SolveModelQualityResults = 5
    

    class SolveMode(enum.Enum):
        Background = 0
        Foreground = 1
    

    class SetupCheckOption(enum.Enum):
        DoNotCheck = 0
        CheckAndStopAtFirstError = 1
        CompleteCheckAndOutputErrors = 2
        DeepCheckAndStopAtFirstError = 3
        CompleteDeepCheckAndOutputErrors = 4
    

    class EnumVerifyResults(enum.Enum):
        VerificationSuccess = 0
        ChecksumCalFailed = 1
        ResultsChanged = 2
        ResultsOutOfDate = 3
    

class SimSimulationObjectGroup(CAE.SimBcGroup):
    def __init__(self) -> None: ...
    def GetSimulationObjects(self) -> typing.List[CAE.SimSimulationObject]:
        ...
    def Add(self, tSimulationObject: CAE.SimSimulationObject) -> None:
        ...
    def Remove(self, pSimulationObject: CAE.SimSimulationObject) -> None:
        ...
    def RemoveAll(self) -> None:
        ...


class SimSimulationObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimSimulationObject]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateSimulationObject(self, descriptorName: str, name: str) -> CAE.SimSimulationObject:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimSimulationObject:
        ...
    def Tag(self) -> Tag: ...



class SimSimulationObject(CAE.SimBC):
    def __init__(self) -> None: ...
    def AncillaryDisplay(self) -> None:
        ...


class SimSimulation(NXObject):
    def __init__(self) -> None: ...
    def CreateSolution(self, solverType: str, analysisType: str, solutionType: str, name: str) -> CAE.SimSolution:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.SimSimulation.CreateSolution with abstraction type input instead.")"""
        ...
    def CreateSolution(self, solverType: str, analysisType: str, solutionType: str, name: str, abstractionType: CAE.SimSimulation.AxisymAbstractionType) -> CAE.SimSolution:
        ...
    def CreateSolution(self, conditionSeqeunce: CAE.SimConditionSequence, solverType: str, analysisType: str, solutionType: str, name: str) -> CAE.SimSolution:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.SimSimulation.CreateSolution and NXOpen.CAE.SimSolution.SetTimePropsFromConditionSequence instead.")"""
        ...
    def CreateSolution(self, conditionSeqeunce: CAE.SimConditionSequence, numSteps: int, solverType: str, analysisType: str, solutionType: str, name: str) -> CAE.SimSolution:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.SimSimulation.CreateSolution and NXOpen.CAE.SimSolution.SetTimePropsFromConditionSequence with number of steps input instead.")"""
        ...
    def CreateSolution(self, conditionSeqeunce: CAE.SimConditionSequence, stepSize: float, stepUnit: Unit, solverType: str, analysisType: str, solutionType: str, name: str) -> CAE.SimSolution:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.SimSimulation.CreateSolution and NXOpen.CAE.SimSolution.SetTimePropsFromConditionSequence with step size input instead.")"""
        ...
    def CreateSolution(self, nodalForceReport: CAE.NodalForceReport, name: str, subcaseOption: CAE.NodalForceReport.SubcaseOption, stepTag: CAE.SimSolutionStep, createForce: bool, createMoment: bool) -> CAE.SimSolution:
        ...
    def DeleteSolution(self, solution: CAE.SimSolution) -> None:
        ...
    def CloneSolution(self, oldSolution: CAE.SimSolution, suggestedName: str) -> CAE.SimSolution:
        ...
    def CreateSolutionStep(self, solution: CAE.SimSolution, stepType: int, name: str) -> CAE.SimSolutionStep:
        ...
    def CreateBcBuilderForLoadDescriptor(self, bcDescName: str, bcName: str) -> CAE.SimBCBuilder:
        ...
    def CreateBcBuilderForLoadDescriptor(self, bcDescName: str, bcName: str, label: int) -> CAE.SimBCBuilder:
        ...
    def CreateBcBuilderForConstraintDescriptor(self, bcDescName: str, bcName: str) -> CAE.SimBCBuilder:
        ...
    def CreateBcBuilderForConstraintDescriptor(self, bcDescName: str, bcName: str, label: int) -> CAE.SimBCBuilder:
        ...
    def CreateBcBuilderForSimulationObjectDescriptor(self, bcDescName: str, bcName: str) -> CAE.SimBCBuilder:
        ...
    def CreateBcBuilderForSimulationObjectDescriptor(self, bcDescName: str, bcName: str, label: int) -> CAE.SimBCBuilder:
        ...
    def CreateBcBuilderForBc(self, bc: CAE.SimBC) -> CAE.SimBCBuilder:
        ...
    def CreateMultiBcEditBuilder(self, bcs: typing.List[CAE.SimBC]) -> CAE.SimMultiBCEditBuilder:
        ...
    def AddBc(self, bc: CAE.SimBC, solution: CAE.SimSolution, solutionStep: CAE.SimSolutionStep) -> None:
        ...
    def CreateAutoPairsBuilder(self, pcBCDescName: str) -> CAE.AutoPairsBuilder:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.CAE.SimSimulation.CreateAutoFacePairsBuilder.")"""
        ...
    def CreateAutoFacePairsBuilder(self, pcBCDescName: str) -> CAE.AutoPairsBuilder:
        ...
    def CreateAutoEdgePairsBuilder(self, pcBCDescName: str) -> CAE.AutoEdgePairsBuilder:
        ...
    def CreateAutoCyclicSymmetryPairsBuilder(self, pcBCDescName: str) -> CAE.AutoCyclicSymmetryPairsBuilder:
        ...
    def CreateAutoBcBuilder(self, pcBCDescName: str, pcRecipeName: str) -> CAE.AutoBCBuilder:
        """[Obsolete("Deprecated in NX1926.0.0.  Use NXOpen.CAE.SimSimulation.CreateAutoFaceBcBuilder.")"""
        ...
    def CreateAutoFaceBcBuilder(self, pcBCDescName: str, pcRecipeName: str) -> CAE.AutoBCBuilder:
        ...
    def CreateAutoEdgeBcBuilder(self, pcBCDescName: str, pcRecipeName: str) -> CAE.AutoEdgeBCBuilder:
        ...
    def CreateMotionLoadsBuilder(self) -> CAE.SimMotionLoadsBuilder:
        ...
    def CreateMotionLoadsListItemBuilder(self) -> CAE.SimMotionLoadsListItemBuilder:
        ...
    def CreateCaeRegionBuilder(self, pcRegionDescName: str, tRegion: CAE.CaeRegion) -> CAE.CaeRegionBuilder:
        ...
    def CreateSimBcPlotContoursBuilder(self) -> CAE.SimBcPlotContoursBuilder:
        ...
    def CreateSimBcXyPlotBuilder(self) -> CAE.SimBcXyPlotBuilder:
        ...
    def CreateBcSelectionDisplayBuilder(self) -> CAE.BCSelectionDisplayBuilder:
        ...
    def BcSequenceDisplay(self, objects: typing.List[NXObject]) -> None:
        ...
    def CreateStepManager(self, tSol: CAE.SimSolution) -> CAE.StepManager:
        ...
    def CreateSolutionManager(self) -> CAE.SolutionManager:
        ...
    def CreateLoadSetBuilder(self, pcLoadSetDescName: str, pName: str, tLoadSet: CAE.SimLoadSet, iLabel: int) -> CAE.SimLoadSetBuilder:
        ...
    def CreateImportedSolutionBuilder(self) -> CAE.ImportedSolutionBuilder:
        ...
    def CreateResultSourceBuilder(self, tSolution: CAE.SimSolution) -> CAE.ResultSourceBuilder:
        ...
    def CreateConstraintSetBuilder(self, pcConstraintSetDescName: str, tConstraintSet: CAE.SimConstraintSet) -> CAE.SimConstraintSetBuilder:
        ...
    def SmoothOptResultsCreateBuilder(self) -> CAE.SmoothOptResultsBuilder:
        ...
    def CreateBcLabelManagerBuilder(self) -> CAE.BcLabelManagerBuilder:
        ...
    def CreateDeleteUnreferencedEntitiesBuilder(self) -> CAE.DeleteUnreferencedEntitiesBuilder:
        ...
    def UpdateFemodel(self) -> None:
        ...
    def CreateTargetEntitiesBuilder(self) -> CAE.TargetEntitiesBuilder:
        ...
    def CreateLoadcaseCombinationBuilder(self, tResult: CAE.SimResultReference) -> CAE.LoadcaseCombinationBuilder:
        ...
    def CreateEnergyDistributionTableBuilder(self) -> CAE.EnergyDistributionTableBuilder:
        ...
    def CreateSimFieldFromBcBuilder(self) -> CAE.SimFieldFromBcBuilder:
        ...
    def CreateDirectionalityFieldBuilder(self) -> CAE.DirectionalityFieldBuilder:
        ...
    def CreateBcMultiCopyBuilder(self) -> CAE.SimBCMultiCopyBuilder:
        ...
    def CreateMultiTargetsetCopyBuilder(self) -> CAE.MultiTargetsetCopyBuilder:
        ...
    def CreateLoadMappingBuilder(self) -> CAE.LoadMappingBuilder:
        ...
    Loads: CAE.SimLoadCollection
    Constraints: CAE.SimConstraintCollection
    SimulationObjects: CAE.SimSimulationObjectCollection
    ResponseSimulationManager: CAE.ResponseSimulation.Manager
    CorrelManager: CAE.CorrelManager
    SimulationRecipes: CAE.SimRecipeCollection
    CaeRegions: CAE.CaeRegionCollection
    CaeDOFSets: CAE.CaeDOFSetCollection
    DurabilityManager: CAE.DurabilityManager
    Solutions: CAE.SimSolutionCollection
    LaminateManager: CAE.LaminateManager
    TBSOptimizationManager: CAE.Optimization.TBSOptimizationManager
    OptimizationManager: CAE.Optimization.DAOOptimizationManager
    ResultMeasures: CAE.ResultMeasureCollection
    LbcFolders: CAE.SimLbcFolderCollection
    AdaptivitySolutions: CAE.AdaptivityMetaSolutionCollection
    LoadRecipes: CAE.SimLoadRecipeCollection
    LoadSets: CAE.SimLoadSetCollection
    ConstraintSets: CAE.SimConstraintSetCollection
    DurSpecialistManager: CAE.DurSpecialistManager
    DataProcessings: CAE.DataProcessingCollection
    AeroStructManager: CAE.AeroStructManager
    ModelAndLoadPreProcessor: CAE.ModelAndLoadPreProcessor
    AcousticsAndVibrationManager: CAE.AcousticsAndVibrationManager
    Acoustics: CAE.Acoustics
    TestModels: CAE.TestModelCollection
    SimInterfaces: CAE.SimInterfaceCollection
    ImportedSimInterfaces: CAE.ImportedSimInterfaceCollection
    SoundProcessors: CAE.SimSoundProcessingCollection
    ActiveSolution: CAE.SimSolution
    ConditionSeqManager: CAE.SimConditionSeqMgr
    Femodel: CAE.FEModelOccurrence


    class AxisymAbstractionType(enum.Enum):
        None = 0
        ZxPlane = 1
        XyPlane = 2
        XxyPlane = 3
    

class SimResultReference(TaggedObject):
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def SetLocalResultFile(self, dirpath: str, filename: str) -> None:
        ...
    def SetManagedResultFile(self, file: str) -> None:
        ...
    def SetInferredResultFile(self) -> None:
        ...
    def GetResultFile(self, resultfiledir: str, resfilename: str) -> None:
        ...
    def DeleteResultFile(self) -> None:
        ...
    def GetManagedResultFile(self) -> str:
        ...
    def GetResultFileUnits(self, units: typing.List[Unit]) -> None:
        ...
    def SetResultFileUnits(self, units: typing.List[Unit]) -> None:
        ...
    def SetInferredResultFileUnits(self) -> None:
        ...
    def AskResultsExist(self) -> bool:
        ...
    CompanionResults: CAE.CompanionResultCollection


    class Type(enum.Enum):
        Structural = 0
        Thermal = 1
        Flow = 2
        Magnetics = 3
        Acoustic = 4
        VibroAcoustic = 5
    

class SimRecipeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimRecipe]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateAutoBcRecipe(self, descriptorName: str, recipeName: str) -> CAE.SimAutoBcRecipe:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimRecipe:
        ...
    def Tag(self) -> Tag: ...



class SimRecipe(NXObject):
    def __init__(self) -> None: ...
    DescriptorName: str
    RecipeName: str


class SimPart(CAE.CaePart):
    def __init__(self) -> None: ...
    def FinalizeCreation(self, femPart: CAE.CaePart, description: str) -> None:
        ...
    def FinalizeCreation(self, femPart: CAE.CaePart, femLayerOpt: int, description: str) -> None:
        ...
    def ImportSim(self, fileName: str, prependString: str, selOptions: CAE.SimPart.ImportOptions, selectedFemoccs: typing.List[CAE.FEModelOccurrence]) -> CAE.SimPart.ImportErrorCodes:
        ...
    def CreateImportSimBuilder(self) -> CAE.ImportSimulationBuilder:
        ...
    def RelabelEntitiesByOffsets(self, csysOffset: int, physOffset: int, groupOffset: int, ssmoOffset: int) -> None:
        ...
    def CompressEntityLabels(self, compressCsysLabels: bool, compressPhysLabels: bool, compressGroupLabels: bool, compressSsmoLabels: bool) -> None:
        ...
    FemPart: CAE.CaePart
    Simulation: CAE.SimSimulation


    class SimPartImportOptions():
        ImportLoads: bool
        ImportConstraints: bool
        ImportSimulationobjects: bool
        ImportMaterials: bool
        ImportFields: bool
        ImportModelingobjects: bool
        ImportPhysicals: bool
        ImportGroups: bool
        ImportRegions: bool
        ImportSolutions: bool
        ImportDofsets: bool
        ImportAll: bool
        def ToString(self) -> str:
            ...
    

    class SimPartImportErrorCodes():
        Importloads: int
        Importconstraints: int
        Importsimulationobjects: int
        Importmaterials: int
        Importfields: int
        Importmodelingobjects: int
        Importphysicals: int
        Importgroups: int
        Importregions: int
        Importsolutions: int
        Importdofsets: int
        def ToString(self) -> str:
            ...
    

class SimMultiBCEditBuilder(Builder):
    def __init__(self) -> None: ...
    def GetNthBcPropertyTable(self, i: int) -> CAE.PropertyTable:
        ...


class SimMotionLoadsListItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    LinkName: str
    SolutionName: str


class SimMotionLoadsBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateNewListItem(self, linkName: str, solutionName: str) -> CAE.SimMotionLoadsListItemBuilder:
        ...
    def GetLoadTransferListItemCount(self) -> int:
        ...
    def GetLoadTransferListItemByIndex(self, index: int) -> CAE.SimMotionLoadsListItemBuilder:
        ...
    MotionSimFile: Part
    SelectedLoadTransferListItem: CAE.SimMotionLoadsListItemBuilder


class SimLoadSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimLoadSet]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateLoadSet(self, descriptorName: str, name: str, label: int) -> CAE.SimLoadSet:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimLoadSet:
        ...
    def Tag(self) -> Tag: ...



class SimLoadSetBuilder(Builder):
    def __init__(self) -> None: ...
    LoadSet: CAE.SimLoadSet
    PropertyTable: CAE.PropertyTable


class SimLoadSet(CAE.NamedPropertyTable):
    def __init__(self) -> None: ...
    def AddMemberSet(self, tmember: CAE.SimLoadSet) -> None:
        ...
    def RemoveMemberSet(self, tmember: CAE.SimLoadSet) -> None:
        ...
    def GetMemberSet(self) -> CAE.SimLoadSet:
        ...
    def AddMemberLoads(self, tmembers: typing.List[CAE.SimLoad]) -> None:
        ...
    def RemoveMemberLoads(self, tmembers: typing.List[CAE.SimLoad]) -> None:
        ...
    def GetMemberLoads(self, tmembers: typing.List[CAE.SimLoad]) -> None:
        ...
    def AddMemberFolders(self, tmembers: typing.List[CAE.SimLbcFolder]) -> None:
        ...
    def RemoveMemberFolders(self, tmembers: typing.List[CAE.SimLbcFolder]) -> None:
        ...
    def GetMemberFolders(self, tmembers: typing.List[CAE.SimLbcFolder]) -> None:
        ...
    def GetMemberFolderValidLoads(self, tFolder: CAE.SimLbcFolder, tmembers: typing.List[CAE.SimLoad]) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    DescriptorName: str
    LoadSetType: CAE.SimLoadSet.Type


    class Type(enum.Enum):
        Invalid = -1
        Static = 0
        Frequency = 1
        Transient = 2
        Acoustic = 3
        Temperature = 4
        Bolt = 5
        FrequencyGust = 6
        TransientGust = 7
    

class SimLoadRecipeValidation(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def HasErrors(self) -> bool:
        ...
    def HasWarnings(self) -> bool:
        ...


class SimLoadRecipeTypes(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class TargetTypes(enum.Enum):
        FiniteElementModel = 0
        ModeSet = 1
    

    class MappingTypes(enum.Enum):
        UserDefined = 0
        FileBased = 1
    

    class LoadConditionHandling(enum.Enum):
        Single = 0
        PerDataSource = 1
    

    class DataTypes(enum.Enum):
        TimeData = 0
        FrequencySpectra = 1
        WaterfallofTimeData = 2
        WaterfallofFrequencySpectra = 3
        OrderCut = 4
    

class SimLoadRecipeSourceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimLoadRecipeSource]:
        ...
    def __init__(self, owner: CAE.SimLoadRecipe) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, path: str) -> CAE.SimLoadRecipeSource:
        ...
    def Create(self, path: str, readerType: str, formatType: str) -> CAE.SimLoadRecipeSource:
        ...
    def Delete(self, sources: typing.List[CAE.SimLoadRecipeSource]) -> None:
        ...
    def Tag(self) -> Tag: ...



class SimLoadRecipeSource(TaggedObject):
    def __init__(self) -> None: ...
    def GetPropertyTable(self) -> BasePropertyTable:
        ...
    DefaultFunctionAttributes: CAE.SimLoadRecipeFunctionAttributes
    FormatType: str
    Path: str
    ReaderType: str
    SourceLabel: str


class SimLoadRecipeMappingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimLoadRecipeMapping]:
        ...
    def __init__(self, owner: CAE.SimLoadRecipe) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.SimLoadRecipeMapping:
        ...
    def Tag(self) -> Tag: ...



class SimLoadRecipeMapping(TaggedObject):
    def __init__(self) -> None: ...
    Entries: CAE.SimLoadRecipeMapEntryCollection
    LoadType: str
    OrientationType: CAE.SimLoadRecipeMapping.OrientationTypes


    class OrientationTypes(enum.Enum):
        Unknown = 0
        DataSource = 1
        Nodal = 2
        Global = 3
    

class SimLoadRecipeMapEntryTargetTypes(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class TargetTypes(enum.Enum):
        Unknown = 0
        Node = 1
        NodeGroup = 2
        NodeMesh = 3
        Face = 4
        FaceGroup = 5
        FaceMesh = 6
        NodeFem = 7
        FaceFem = 8
        NodeSelectionRecipe = 9
        FaceSelectionRecipe = 10
    

class SimLoadRecipeMapEntryCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimLoadRecipeMapEntry]:
        ...
    def __init__(self, owner: CAE.SimLoadRecipeMapping) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.SimLoadRecipeMapEntry:
        ...
    def Create(self, targetType: CAE.SimLoadRecipeMapEntryTargetTypes.TargetTypes, target: str) -> CAE.SimLoadRecipeMapEntry:
        ...
    def Delete(self, mapEntries: typing.List[CAE.SimLoadRecipeMapEntry]) -> None:
        ...
    def Tag(self) -> Tag: ...



class SimLoadRecipeMapEntry(TaggedObject):
    def __init__(self) -> None: ...
    def GetParameters(self) -> str:
        ...
    def SetParameters(self, parameters: str) -> None:
        ...
    Target: str
    TargetType: CAE.SimLoadRecipeMapEntryTargetTypes.TargetTypes


class SimLoadRecipeLbcGenerator(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Generate(self, solution: CAE.SimSolution) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use method taking LBC hierarchy type as input. This method always creates separated LBCs.")"""
        ...
    def Generate(self, solution: CAE.SimSolution, stepType: int) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use method taking LBC hierarchy type as input. This method always creates separated LBCs.")"""
        ...
    def GetAllowedStepTypeCount(self, solution: CAE.SimSolution) -> int:
        ...
    def Generate(self, solution: CAE.SimSolution, lbcHierarchyType: CAE.SimLoadRecipeLbcGenerator.LbcHierarchyTypes) -> None:
        ...
    def Generate(self, solution: CAE.SimSolution, stepType: int, lbcHierarchyType: CAE.SimLoadRecipeLbcGenerator.LbcHierarchyTypes) -> None:
        ...
    def UpdateSolution(self, solution: CAE.SimSolution, lbcHierarchyType: CAE.SimLoadRecipeLbcGenerator.LbcHierarchyTypes) -> None:
        ...


    class LbcHierarchyTypes(enum.Enum):
        Aggregated = 0
        Separated = 1
        FileReference = 2
    

class SimLoadRecipeFunctionAttributes(TaggedObject):
    def __init__(self) -> None: ...
    AcousticalWeighting: CAE.SimLoadRecipeFunctionAttributes.AcousticalWeightings
    AmplitudeCorrectionFactor: float
    CorrectionMode: CAE.SimLoadRecipeFunctionAttributes.CorrectionModes
    EnergyCorrectionFactor: float
    SpectrumScaling: CAE.SimLoadRecipeFunctionAttributes.ScalingType


    class ScalingType(enum.Enum):
        Unknown = 0
        Peak = 1
        Rms = 2
    

    class CorrectionModes(enum.Enum):
        Unknown = 0
        Energy = 1
        Amplitude = 2
    

    class AcousticalWeightings(enum.Enum):
        Unknown = 0
        None = 1
        A = 2
        B = 3
        C = 4
        D = 5
        Ab = 6
        Bc = 7
    

class SimLoadRecipeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimLoadRecipe]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.SimLoadRecipe:
        ...
    def Create(self, name: str, description: str, targetType: CAE.SimLoadRecipeTypes.TargetTypes, dataType: CAE.SimLoadRecipeTypes.DataTypes) -> CAE.SimLoadRecipe:
        ...
    def Create(self, name: str, description: str, dataType: CAE.SimLoadRecipeTypes.DataTypes) -> CAE.SimLoadRecipe:
        """[Obsolete("Deprecated in NX1926.0.0.  Use CAE.SimLoadRecipeCollection.Create created in NX1926.0.0 instead.")"""
        ...
    def Create(self, name: str, description: str, dataType: CAE.SimLoadRecipeTypes.DataTypes, mappingType: CAE.SimLoadRecipeTypes.MappingTypes) -> CAE.SimLoadRecipe:
        """[Obsolete("Deprecated in NX1926.0.0.  Use CAE.SimLoadRecipeCollection.Create created in NX1926.0.0 instead.")"""
        ...
    def Create(self, name: str, description: str, dataType: CAE.SimLoadRecipeTypes.DataTypes, mappingType: CAE.SimLoadRecipeTypes.MappingTypes, valuesOutsideTableOption: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> CAE.SimLoadRecipe:
        """[Obsolete("Deprecated in NX1926.0.0.  Use CAE.SimLoadRecipeCollection.Create created in NX1926.0.0 instead.")"""
        ...
    def Copy(self, recipeToCopy: CAE.SimLoadRecipe) -> CAE.SimLoadRecipe:
        ...
    def Delete(self, recipes: typing.List[CAE.SimLoadRecipe]) -> None:
        ...
    def Tag(self) -> Tag: ...



class SimLoadRecipe(TaggedObject):
    def __init__(self) -> None: ...
    def GetLoadConditionHandlingType(self) -> CAE.SimLoadRecipeTypes.LoadConditionHandling:
        ...
    def SetLoadConditionHandlingType(self, lcHandling: CAE.SimLoadRecipeTypes.LoadConditionHandling) -> None:
        ...
    def GetLoadConditions(self) -> str:
        ...
    def GetTrackingValues(self) -> str:
        ...
    def GetMpfModes(self) -> int:
        ...
    def DisableLoadCondition(self, loadCondition: str) -> None:
        ...
    def EnableLoadCondition(self, loadCondition: str) -> None:
        ...
    def DisableTrackingValue(self, trackingValue: str) -> None:
        ...
    def EnableTrackingValue(self, trackingValue: str) -> None:
        ...
    def DisableMpfMode(self, mode: int) -> None:
        ...
    def EnableMpfMode(self, mode: int) -> None:
        ...
    def NewLbcGeneratorFromLoadRecipe(self) -> CAE.SimLoadRecipeLbcGenerator:
        ...
    def NewValidationFromLoadRecipe(self) -> CAE.SimLoadRecipeValidation:
        ...
    def ImportFromCSVFile(self, filePath: str, csvDelim: str, noParsedContent: bool, invalidLoadType: bool, invalidEntityType: bool, invalidNbrOfParameters: bool) -> None:
        ...
    def ExportToCSVFile(self, filePath: str) -> bool:
        ...
    def Autofill(self) -> None:
        ...
    def Autofill(self, feModelOcc: CAE.FEModelOccurrence) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.SimLoadRecipe.SetAutofillAssemblyComponent and NXOpen.CAE.SimLoadRecipe.Autofill instead.")"""
        ...
    def AutofillSelectionRecipeBased(self) -> None:
        ...
    def Validation(self) -> None:
        ...
    def LoadLoadConditions(self) -> None:
        ...
    def LoadTrackingValues(self) -> None:
        ...
    def LoadMpfModes(self) -> None:
        ...
    def SetAutofillAssemblyComponent(self, feModelOcc: CAE.FEModelOccurrence) -> None:
        ...
    MappingCollection: CAE.SimLoadRecipeMappingCollection
    SourceCollection: CAE.SimLoadRecipeSourceCollection
    DataType: CAE.SimLoadRecipeTypes.DataTypes
    Description: str
    MappingType: CAE.SimLoadRecipeTypes.MappingTypes
    Name: str
    ValuesOutsideTableOption: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum


class SimLoadGroup(CAE.SimBcGroup):
    def __init__(self) -> None: ...
    def GetLoads(self) -> typing.List[CAE.SimLoad]:
        ...
    def Add(self, tLoad: CAE.SimLoad) -> None:
        ...
    def Remove(self, tLoad: CAE.SimLoad) -> None:
        ...
    def RemoveAll(self) -> None:
        ...
    def AddLoadSet(self, tLoadSet: CAE.SimLoadSet) -> None:
        ...
    def RemoveLoadSet(self, tLoadSet: CAE.SimLoadSet) -> None:
        ...
    def GetLoadSets(self) -> typing.List[CAE.SimLoadSet]:
        ...
    def RemoveAllLoadSets(self) -> None:
        ...


class SimLoadCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimLoad]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateLoad(self, descriptorName: str, name: str) -> CAE.SimLoad:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimLoad:
        ...
    def Tag(self) -> Tag: ...



class SimLoad(CAE.SimBC):
    def __init__(self) -> None: ...


class SimLbcFolderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimLbcFolder]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateFolder(self, name: str, folderType: CAE.SimLbcFolder.Type, parent: CAE.SimLbcFolder) -> CAE.SimLbcFolder:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimLbcFolder:
        ...
    def Tag(self) -> Tag: ...



class SimLbcFolder(NXObject):
    def __init__(self) -> None: ...
    def AddSubfolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def RemoveSubfolder(self, folder: CAE.SimLbcFolder) -> None:
        ...
    def AddBc(self, bc: CAE.SimBC) -> None:
        ...
    def RemoveBc(self, bc: CAE.SimBC) -> None:
        ...
    def CloneFolder(self) -> CAE.SimLbcFolder:
        ...
    def GetParent(self) -> CAE.IFolder:
        ...
    def GetChildren(self) -> typing.List[CAE.IFolder]:
        ...
    def GetMembers(self) -> typing.List[NXObject]:
        ...
    FolderType: CAE.SimLbcFolder.Type
    Parent: CAE.SimLbcFolder


    class Type(enum.Enum):
        None = 0
        Load = 1
        Constraint = 2
        SimulationObject = 3
    

class SimInterfaceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimulationInterface]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateSimulationInterface(self, name: str) -> CAE.SimulationInterface:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimulationInterface:
        ...
    def Tag(self) -> Tag: ...



class SimGroupContainer(NXObject):
    def __init__(self) -> None: ...
    def GetGroupCount(self) -> int:
        ...
    def GetGroups(self) -> typing.List[CAE.SimBcGroup]:
        ...
    def CreateLoadGroup(self) -> CAE.SimLoadGroup:
        ...
    def CreateConstraintGroup(self) -> CAE.SimConstraintGroup:
        ...
    def CreateSimulationObjectGroup(self) -> CAE.SimSimulationObjectGroup:
        ...
    def DeleteGroup(self, lbGroup: CAE.SimBcGroup) -> None:
        ...
    IsConstraintGroupAllowed: bool
    IsLoadGroupAllowed: bool
    IsSimulationObjectGroupAllowed: bool


class SimFieldFromBcBuilder(Builder):
    def __init__(self) -> None: ...
    def SetProperties(self, propNames: str) -> None:
        ...
    def SetEvaluationPoints(self, values: float, units: typing.List[Unit]) -> None:
        ...
    Bc: CAE.SimBC
    Strategy: CAE.SimFieldFromBcBuilder.MagnitudeStrategy


    class MagnitudeStrategy(enum.Enum):
        None = 0
        ForceOrientToCompPressure = 1
        MagOrientToComp = 2
        ForceOrientToCompForcePerLenth = 3
    

class SimConstraintSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimConstraintSet]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateConstraintSet(self, descriptorName: str, name: str, label: int) -> CAE.SimConstraintSet:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimConstraintSet:
        ...
    def Tag(self) -> Tag: ...



class SimConstraintSetBuilder(Builder):
    def __init__(self) -> None: ...
    DescriptorName: str
    Label: int
    Name: str
    PropertyTable: CAE.PropertyTable


class SimConstraintSet(CAE.NamedPropertyTable):
    def __init__(self) -> None: ...
    def AddMemberConstraints(self, tmembers: typing.List[CAE.SimConstraint]) -> None:
        ...
    def RemoveMemberConstraints(self, tmembers: typing.List[CAE.SimConstraint]) -> None:
        ...
    def GetMemberConstraints(self, tmembers: typing.List[CAE.SimConstraint]) -> None:
        ...
    def AddMemberFolders(self, tmembers: typing.List[CAE.SimLbcFolder]) -> None:
        ...
    def RemoveMemberFolders(self, tmembers: typing.List[CAE.SimLbcFolder]) -> None:
        ...
    def GetMemberFolders(self, tmembers: typing.List[CAE.SimLbcFolder]) -> None:
        ...
    DescriptorName: str


class SimConstraintGroup(CAE.SimBcGroup):
    def __init__(self) -> None: ...
    def GetConstraints(self) -> typing.List[CAE.SimConstraint]:
        ...
    def Add(self, tConstraint: CAE.SimConstraint) -> None:
        ...
    def Remove(self, tConstraint: CAE.SimConstraint) -> None:
        ...
    def RemoveAll(self) -> None:
        ...
    def AddConstraintSet(self, tConstraintSet: CAE.SimConstraintSet) -> None:
        ...
    def RemoveConstraintSet(self, tConstraintSet: CAE.SimConstraintSet) -> None:
        ...
    def GetConstraintSets(self) -> typing.List[CAE.SimConstraintSet]:
        ...
    def RemoveAllConstraintSets(self) -> None:
        ...


class SimConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimConstraint]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateConstraint(self, descriptorName: str, name: str) -> CAE.SimConstraint:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SimConstraint:
        ...
    def Tag(self) -> Tag: ...



class SimConstraint(CAE.SimBC):
    def __init__(self) -> None: ...


class SimConditionTimeStepCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimConditionTimeStep]:
        ...
    def __init__(self, owner: CAE.SimConditionSequence) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, time: float, condition: CAE.SimCondition, description: str) -> CAE.SimConditionTimeStep:
        ...
    def Delete(self, step: CAE.SimConditionTimeStep) -> None:
        ...
    def ModifyTime(self, step: CAE.SimConditionTimeStep, time: float) -> None:
        ...
    def Get(self, time: float) -> CAE.SimConditionTimeStep:
        ...
    def GetAll(self) -> typing.List[CAE.SimConditionTimeStep]:
        ...
    def GetInRange(self, fromTime: float, toTime: float) -> typing.List[CAE.SimConditionTimeStep]:
        ...
    def GetWithReferenceToCondition(self, condition: CAE.SimCondition) -> typing.List[CAE.SimConditionTimeStep]:
        ...
    def Find(self, time: str) -> CAE.SimConditionTimeStep:
        ...
    def Tag(self) -> Tag: ...



class SimConditionTimeStep(TaggedObject):
    def __init__(self) -> None: ...
    Condition: CAE.SimCondition
    Description: str
    Time: float


class SimConditionSequenceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimCondition]:
        ...
    def __init__(self, owner: CAE.SimConditionSeqMgr) -> None: ...
    def __init__(self) -> None: ...
    def Get(self, label: int) -> CAE.SimConditionSequence:
        ...
    def Find(self, label: str) -> CAE.SimConditionSequence:
        ...
    def Create(self, name: str, label: int) -> CAE.SimConditionSequence:
        ...
    def Create(self, name: str) -> CAE.SimConditionSequence:
        ...
    def Create(self, label: int) -> CAE.SimConditionSequence:
        ...
    def Create(self) -> CAE.SimConditionSequence:
        ...
    def Delete(self, conditionSeq: CAE.SimConditionSequence) -> int:
        ...
    def GetAll(self) -> typing.List[CAE.SimConditionSequence]:
        ...
    def NextLabel(self) -> int:
        ...
    def IsLabelValid(self, label: int) -> bool:
        ...
    def Tag(self) -> Tag: ...



class SimConditionSequence(TaggedObject):
    def __init__(self) -> None: ...
    def GetTimeUnits(self) -> Unit:
        ...
    def SetTimeUnits(self, units: Unit) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def GetValue(self, param: CAE.SimConditionParam, time: float) -> float:
        ...
    def GetValue(self, param: CAE.SimConditionParam, time: float, behavior: CAE.SimConditionSequence.OutOfRangeBehavior) -> float:
        ...
    def Evaluate(self, time: float) -> None:
        ...
    def Evaluate(self, time: float, update: bool) -> None:
        ...
    def GetSolutions(self) -> typing.List[CAE.SimSolution]:
        ...
    ConditionTimeStepCollection: CAE.SimConditionTimeStepCollection
    Name: str


    class OutOfRangeBehavior(enum.Enum):
        Clip = 0
        Extrapolate = 1
    

class SimConditionSeqMgr(TaggedObject):
    def __init__(self) -> None: ...
    def IsReferenced(self, condition: CAE.SimCondition) -> bool:
        ...
    def ImportFile(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat) -> None:
        ...
    def ImportOnlyConditionSequencesFromFile(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat) -> None:
        ...
    def ImportConditionSequencesFromFile(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat) -> None:
        ...
    def ExportFile(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat) -> None:
        ...
    def ExportConditionSequencesToFile(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat, conditionSeqs: typing.List[CAE.SimConditionSequence]) -> None:
        ...
    def ExportConditionSequencesToFileWithError(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat, conditionSeqs: typing.List[CAE.SimConditionSequence]) -> str:
        ...
    def ExportFileWithError(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat) -> str:
        ...
    def WrapUp(self) -> None:
        ...
    def SetNameCollisionsBehavior(self, namecollisionsbehavior: CAE.SimConditionSeqMgr.ImportNameCollisionsBehavior) -> None:
        ...
    def SetMissingConditionsBehavior(self, missingconditionsbehavior: CAE.SimConditionSeqMgr.ImportMissingConditionsBehavior) -> None:
        ...
    ConditionParamCollection: CAE.SimConditionParamCollection
    ConditionCollection: CAE.SimConditionCollection
    ConditionSequenceCollection: CAE.SimConditionSequenceCollection
    ActiveConditionSequence: CAE.SimConditionSequence


    class ImportNameCollisionsBehavior(enum.Enum):
        RenameExisting = 0
        RenameIncoming = 1
    

    class ImportMissingConditionsBehavior(enum.Enum):
        Delete = 0
        Settoundefined = 1
    

    class FileFormat(enum.Enum):
        Bdd = 0
        Xml = 1
    

class SimConditionParamCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimConditionParam]:
        ...
    def __init__(self, owner: CAE.SimConditionSeqMgr) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, name: str, units: Unit) -> CAE.SimConditionParam:
        ...
    def Delete(self, param: CAE.SimConditionParam) -> int:
        ...
    def Get(self, name: str) -> CAE.SimConditionParam:
        ...
    def GetAll(self) -> typing.List[CAE.SimConditionParam]:
        ...
    def Find(self, name: str) -> CAE.SimConditionParam:
        ...
    def Tag(self) -> Tag: ...



class SimConditionParam(TaggedObject):
    def __init__(self) -> None: ...
    def Modify(self, name: str, units: Unit) -> None:
        ...
    Name: str
    Units: Unit


class SimConditionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SimCondition]:
        ...
    def __init__(self, owner: CAE.SimConditionSeqMgr) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, name: str, label: int) -> CAE.SimCondition:
        ...
    def Create(self, name: str) -> CAE.SimCondition:
        ...
    def Create(self, label: int) -> CAE.SimCondition:
        ...
    def Create(self) -> CAE.SimCondition:
        ...
    def Delete(self, condition: CAE.SimCondition) -> int:
        ...
    def Get(self, label: int) -> CAE.SimCondition:
        ...
    def GetAll(self) -> typing.List[CAE.SimCondition]:
        ...
    def NextLabel(self) -> int:
        ...
    def IsLabelValid(self, label: int) -> bool:
        ...
    def Find(self, label: str) -> CAE.SimCondition:
        ...
    def Tag(self) -> Tag: ...



class SimCondition(TaggedObject):
    def __init__(self) -> None: ...
    def GetValue(self, param: CAE.SimConditionParam) -> float:
        ...
    def IsValueDefined(self, param: CAE.SimConditionParam) -> bool:
        ...
    def SetValue(self, param: CAE.SimConditionParam, value: float) -> None:
        ...
    Label: int
    Name: str


class SimBcXyPlotBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAvailableBcsToPlot(self) -> typing.List[CAE.SimBC]:
        ...
    def GetAvailablePropertyNamesToPlot(self, tBc: CAE.SimBC) -> str:
        ...
    def SetBcsToPlot(self, bcs: typing.List[CAE.SimBC], propertyNames: str) -> None:
        ...
    def SetBcsToPlot(self, bcs: typing.List[CAE.SimBC]) -> None:
        ...
    def SetPropertyNameToPlot(self, pPropertyName: str) -> None:
        ...
    def Plot(self, deviceIndex: int, viewIndex: int) -> CAE.Xyplot.Plot:
        ...
    def SetLocationNode(self, node: CAE.FENode) -> None:
        ...
    def SetLocationElement(self, element: CAE.FEElement) -> None:
        ...
    def SetLocationElementEdge(self, elementEdge: CAE.FEElemEdge) -> None:
        ...
    def SetLocationElementFace(self, elementFace: CAE.FEElemFace) -> None:
        ...
    MultipleMatches: CAE.SimBcXyPlotBuilder.ResolveMultipleMatches


    class ResolveMultipleMatches(enum.Enum):
        Add = 0
        Average = 1
        Minimum = 2
        Maximum = 3
        MultipleCurves = 4
    

class SimBcPlotContoursBuilder(Builder):
    def __init__(self) -> None: ...
    def GetAvailableBcsToPlot(self) -> typing.List[CAE.SimBC]:
        ...
    def GetAvailablePropertyNamesToPlot(self, tBc: CAE.SimBC) -> str:
        ...
    def GetAvailablePropertyNamesAndIndicesToPlot(self, tBc: CAE.SimBC, pPropIndices: int, pPropNames: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  There is no replacement for this method.")"""
        ...
    def SetBcsToPlot(self, bcs: typing.List[CAE.SimBC]) -> None:
        ...
    def SetBcsToPlot(self, bcs: typing.List[CAE.SimBC], propertyNames: str) -> None:
        ...
    def CreatePlotObject(self) -> CAE.NxBcPlotContours:
        ...
    def GetPlotType(self) -> CAE.SimBcPlotContoursBuilder.PlotType:
        ...
    def SetPlotType(self, plotType: CAE.SimBcPlotContoursBuilder.PlotType) -> None:
        ...
    def SetAnimationPoints(self, startValue: float, startUnit: Unit, endValue: float, endUnit: Unit, numFrames: int) -> None:
        ...
    def SetAnimationValues(self, startValue: float, startUnit: Unit, endValue: float, endUnit: Unit, varName: str, numFrames: int) -> None:
        ...
    def SetEvaluationPoints(self, values: float, units: typing.List[Unit]) -> None:
        ...
    def SetEvaluationValues(self, values: float, varNames: str, units: typing.List[Unit]) -> None:
        ...
    def CreateResult(self) -> CAE.Result:
        ...
    PropertyIndexToPlot: int
    PropertyNameToPlot: str
    ResolveOverlap: CAE.SimBcPlotContoursBuilder.ResolveOverlapType
    ResolveOverlapValue: float
    ResolveOverlapValueUnit: Unit


    class ResolveOverlapType(enum.Enum):
        Add = 0
        Average = 1
        Maximum = 2
        Minimum = 3
        Specify = 4
    

    class PlotType(enum.Enum):
        Static = 0
        Animation = 1
    

class SimBCMultiCopyBuilder(Builder):
    def __init__(self) -> None: ...
    def AddCopySet(self, prefix: str, suffix: str, destination: CAE.SimBCMultiCopyBuilder.Destination, folder: CAE.SimLbcFolder, retainAssociation: bool) -> None:
        ...
    def EditCopySet(self, index: int, prefix: str, suffix: str, destination: CAE.SimBCMultiCopyBuilder.Destination, folder: CAE.SimLbcFolder, retainAssociation: bool) -> None:
        ...
    def RemoveCopySet(self, index: int) -> None:
        ...
    def DeleteAllCopySets(self) -> None:
        ...
    Selection: CAE.SelectSimBCList


    class Destination(enum.Enum):
        SameAsOriginal = 0
        Root = 1
        Specify = 2
    

class SimBcGroup(TaggedObject):
    def __init__(self) -> None: ...
    def SetBoltLoadSequence(self, objects: typing.List[NXObject]) -> None:
        ...
    GroupContainer: CAE.SimGroupContainer


class SimBCDisplay(TaggedObject):
    def __init__(self) -> None: ...
    def GetDisplayGrid(self, numUPoints: int, numVPoints: int) -> None:
        ...
    def SetDisplayGrid(self, numUPoints: int, numVPoints: int) -> None:
        ...
    def UpdateDisplay(self) -> None:
        ...
    def GetSubColor(self, index: int) -> int:
        ...
    def SetSubColor(self, index: int, color: int) -> None:
        ...
    def GetDistributeType(self, targetSetIndex: int) -> CAE.SimBCDisplay.Distribute:
        ...
    def SetDistributeType(self, targetSetIndex: int, distribute: CAE.SimBCDisplay.Distribute) -> None:
        ...
    DisplayMagnitudeProperty: str
    DisplayMode: CAE.SimBCDisplay.Mode
    DistValueDisplayFlag: bool
    DofDisplayFlag: bool
    FreeFacesObjectsDisplayFlag: bool
    GraphicSymbolDisplayFlag: bool
    GraphicsThreshold: int
    GraphicsThresholdFlag: bool
    HighlightTargets: bool
    NameDisplayFlag: bool
    NodeIdDisplayFlag: bool
    RotateDisplayTextFlag: bool
    Scale: int
    ShadeGraphicSymbol: bool
    SolverCardNameDisplayFlag: bool
    SpectrumColorsDisplayFlag: bool
    TextSymbolDisplayFlag: bool
    Translucency: int
    ValueDisplayFlag: bool


    class Mode(enum.Enum):
        Collapse = 0
        Expand = 1
        Offset = 2
    

    class Distribute(enum.Enum):
        Default = -1
        Nodes = 0
        Elements = 1
        ElementFaces = 2
        ElementEdges = 3
    

class SimBCBuilder(NXObject):
    def __init__(self) -> None: ...
    def CommitBc(self) -> CAE.SimBC:
        ...
    def CommitAddBc(self) -> CAE.SimBC:
        ...
    def Destroy(self) -> None:
        ...
    Bc: CAE.SimBC
    BcLabel: int
    BcName: str
    DestinationFolder: CAE.SimLbcFolder
    PropertyTable: CAE.PropertyTable
    TargetSetManager: CAE.SetManager


class SimBC(DisplayableObject):
    def __init__(self) -> None: ...
    def GetDisplay(self) -> CAE.SimBCDisplay:
        ...
    def CloneBc(self) -> CAE.SimBC:
        ...
    def IsAsleep(self) -> bool:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    BcLabel: int
    DescriptorName: str
    FamilyName: str
    PropertyTable: CAE.PropertyTable
    TargetSetManager: CAE.SetManager


class SimAutoEdgeBcRecipe(CAE.SimRecipe):
    def __init__(self) -> None: ...
    def GetBcList(self, bcList: typing.List[CAE.SimBC]) -> None:
        ...


class SimAutoBcRecipe(CAE.SimRecipe):
    def __init__(self) -> None: ...
    def GetBcList(self, bcList: typing.List[CAE.SimBC]) -> None:
        ...


class SimAbaqusFieldAttributes(NXObject):
    def __init__(self) -> None: ...
    def GetApplication(self) -> Fields.IApplication:
        ...
    def DeleteApplicationData(self) -> None:
        ...
    def CopyToField(self, field: Fields.Field) -> None:
        ...
    AmplitudeTimeAttribute: CAE.SimAbaqusFieldAttributes.AmplitudeTime


    class AmplitudeTime(enum.Enum):
        StepTime = 0
        TotalTime = 1
    

class SimAbaqusFieldApplication(Fields.IApplication):
    def __init__(self) -> None: ...
    def CreateAttributes(self, amplitudeTime: CAE.SimAbaqusFieldAttributes.AmplitudeTime) -> CAE.SimAbaqusFieldAttributes:
        ...


class SignalProcessingPlotData(NXObject):
    def __init__(self) -> None: ...
    def AskNumberOfDisplayableAttributes(self) -> int:
        ...
    def AskNthDisplayableAttributeName(self, nth: int) -> str:
        ...
    def AskNthDisplayableAttributeValue(self, nth: int) -> str:
        ...
    TargetCorrectionMode: CAE.SignalProcessingPlotData.CorrectionMode
    TargetScaling: CAE.SignalProcessingPlotData.ScalingType
    TargetWeighting: CAE.SignalProcessingPlotData.AcousticalWeighting


    class ScalingType(enum.Enum):
        Unknown = 0
        Peak = 1
        Rms = 2
    

    class CorrectionMode(enum.Enum):
        Unknown = 0
        Energy = 1
        Amplitude = 2
    

    class AcousticalWeighting(enum.Enum):
        Unknown = 0
        None = 1
        A = 2
        B = 3
        C = 4
        D = 5
        Ab = 6
        Bc = 7
    

class SignalProcessingDBSettings(TaggedObject):
    def __init__(self) -> None: ...
    def GetReferenceForTargetUnit(self, targetUnit: Unit) -> float:
        ...
    DBFormat: CAE.SignalProcessingDBSettings.DBFormats
    DBReference: float


    class DBFormats(enum.Enum):
        Db10 = 0
        Db20 = 1
    

class ShowOnlyBuilder(Builder):
    def __init__(self) -> None: ...
    Selection: SelectObjectList


class ShowHideManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateShowAdjacentBuilder(self) -> CAE.ShowAdjacentBuilder:
        ...
    def CreateShowOnlyBuilder(self) -> CAE.ShowOnlyBuilder:
        ...
    def CreateShowHideBuilder(self) -> CAE.ShowHideBuilder:
        ...
    def ReverseFaceDisplay(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class ShowHideGroupMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEntities(self) -> typing.List[TaggedObject]:
        ...


class ShowHideBuilder(Builder):
    def __init__(self) -> None: ...
    Selection: SelectObjectList
    ShowFlag: bool


class ShowElemNodeLabelsBuilder(Builder):
    def __init__(self) -> None: ...
    Selection: SelectTaggedObjectList


class ShowAdjacentGroupMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEntities(self) -> typing.List[TaggedObject]:
        ...


class ShowAdjacentBuilder(Builder):
    def __init__(self) -> None: ...
    Selection: SelectObjectList


class ShortEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEdges(self) -> typing.List[CAE.CAEEdge]:
        ...


class ShipMeshAutomationBuilder(Builder):
    def __init__(self) -> None: ...
    AttemptFreeMappedMeshing: bool
    AttemptMultiBlockDecomposition: bool
    CurvatureSizeSetting: float
    CurvatureSizeThreshold: Expression
    DefaultElementSize: bool
    ElementSize: Expression
    Mapped2dMesh: bool
    MethodType: CAE.ShipMeshAutomationBuilder.MeshingMethodType
    ObjectsToBeMeshed: SelectDisplayableObjectList


    class MeshingMethodType(enum.Enum):
        Subdivision = 0
        Paver = 1
    

class ShipMeshAutomation(CAE.Mesh):
    def __init__(self) -> None: ...


class ShellTo3dHybridBuilder(CAE.Shell2SolidBuilder):
    def __init__(self) -> None: ...
    def SetHybridParams(self, hexElementSize: float, elementOrder: int, distanceToBoundary: int, csysMatrix: Matrix3x3) -> None:
        ...


class ShellEADBuilder(Builder):
    def __init__(self) -> None: ...
    CoordinateSystem: CoordinateSystem
    CsysDataType: CAE.ShellEADBuilder.CoordinateSystemDataType
    Elements: CAE.SelectElementsBuilder
    GapThicknessExpression: Expression
    GapThicknessState: CAE.ShellEADBuilder.State
    MaterialOrientationState: CAE.ShellEADBuilder.State
    Node: CAE.SelectFENodeList
    NodeGaps: CAE.SelectFENodeList
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.ShellEADBuilder.State
    PointInPlane: Point
    PointOnZaxis: Point
    PointOrigin: Point
    PreferredLabel: int
    SetMatOriMethod: CAE.ShellEADBuilder.MaterialOrientationMethod
    ThicknessExpression: Expression
    ThicknessState: CAE.ShellEADBuilder.State
    Vector: Direction
    ZoffsetExpression: Expression
    ZoffsetState: CAE.ShellEADBuilder.State


    class State(enum.Enum):
        Ignore = 0
        Apply = 1
        Clear = 2
    

    class MaterialOrientationMethod(enum.Enum):
        CoordinateSystem = 0
        VectorProjection = 1
        CoordinateSystemData = 2
    

    class CoordinateSystemDataType(enum.Enum):
        Cartesian = 0
        Cylindrical = 1
        Spherical = 2
    

class Shell2SolidBuilder(Builder):
    def __init__(self) -> None: ...
    BoundingVolumeSelectionList: SelectTaggedObjectList
    ElementType: CAE.ElementTypeBuilder
    FillHolesOption: bool
    MaxEdgeLengthOption: bool
    MaxEdgeLengthValue: Expression
    MeshGradation: float
    MeshName: str
    MeshSizeVariation: float
    PyramidTransition: bool
    SelectionList: SelectTaggedObjectList


class ShapeMetricViewerBuilder(Builder):
    def __init__(self) -> None: ...


class SetObject():
    Obj: TaggedObject
    SubType: CAE.CaeSetObjectSubType
    SubId: int
    def ToString(self) -> str:
        ...
    def __init__(self, Obj: TaggedObject, SubType: CAE.CaeSetObjectSubType, SubId: int) -> None: ...


class SetManager(NXObject):
    def __init__(self) -> None: ...
    def CreateCaeSet(self) -> CAE.CAESet:
        ...
    def SetTargetSetEdgePath(self, setIndex: int, seedEdges: typing.List[CAE.CAEEdge], seedVertices: typing.List[CAE.CAEVertex], preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float, pathMethodType: typing.List[CAE.PathType], dTangentAngleTolerance: float) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.SetManager.SetTargetSetEdgePathWithLimits.")"""
        ...
    def SetTargetSetEdgePathWithLimits(self, setIndex: int, seedEdges: typing.List[CAE.CAEEdge], seedVertices: typing.List[CAE.CAEVertex], preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float, pathMethodType: typing.List[CAE.PathType], dTangentAngleTolerance: float, startPoint: Point, endPoint: Point) -> None:
        ...
    def SetTargetSetClosedEdgePath(self, setIndex: int, seedEdge: CAE.CAEEdge, flipEdge: bool, startPoint: Point, endPoint: Point) -> None:
        ...
    def GetTargetSetEdgePathLimits(self, setIndex: int, startPoint: Point, endPoint: Point) -> None:
        ...
    def SetTargetSetPlaneWithOffset(self, setIndex: int, planePosition: Point3d, planeNormal: Vector3d, offsetValue: Expression) -> None:
        ...
    def GetTargetSetPlaneWithOffset(self, setIndex: int, planePosition: Point3d, planeNormal: Vector3d, offsetValue: Expression) -> None:
        ...
    def SetTargetSetPlaneObject(self, setIndex: int, plane: Plane) -> None:
        ...
    def GetTargetSetPlaneObject(self, setIndex: int) -> Plane:
        ...
    def SetTargetSetPointLocation(self, setIndex: int, position: Point3d) -> None:
        ...
    def GetTargetSetPointLocation(self, setIndex: int) -> Point3d:
        ...
    def SetTargetSetPointLocation(self, setIndex: int, point: Point) -> None:
        ...
    def GetTargetSetPoint(self, setIndex: int) -> Point:
        ...
    def SetTargetSetDistributedPlanes(self, setIndex: int, centerMethod: CAE.SetManager.DistributedPlanesPosition, centerPoint: Point, radiusMethod: CAE.SetManager.DistributedPlanesPosition, radiusFactor: Expression, radiusValue: Expression, bboxOption: CAE.SetManager.DistributedPlanesBboxType, bboxElems: typing.List[CAE.FEElement], spaceDefinition: CAE.SetManager.DistributedPlanesBoundingSphereType, sphereDirection: CAE.SetManager.DistributedPlanesBoundingSphereDirection, sphereDirectionVector: Direction, sphereDirectionPoint1: Point, sphereDirectionPoint2: Point, sphereDirectionPoint3: Point, flipNormal: bool, refinementLevel: int) -> None:
        ...
    def GetTargetSetDistributedPlanes(self, setIndex: int, centerMethod: CAE.SetManager.DistributedPlanesPosition, centerPoint: Point, radiusMethod: CAE.SetManager.DistributedPlanesPosition, radiusFactor: Expression, radiusValue: Expression, bboxOption: CAE.SetManager.DistributedPlanesBboxType, bboxElems: typing.List[CAE.FEElement], spaceDefinition: CAE.SetManager.DistributedPlanesBoundingSphereType, sphereDirection: CAE.SetManager.DistributedPlanesBoundingSphereDirection, sphereDirectionVector: Direction, sphereDirectionPoint1: Point, sphereDirectionPoint2: Point, sphereDirectionPoint3: Point, flipNormal: bool, refinementLevel: int) -> None:
        ...
    def SetTargetSetElemEdgePath(self, setIndex: int, seedEdges: typing.List[CAE.FEElemEdge], seedVertices: typing.List[CAE.FENode], preferFreeEdges: bool, preferGeometryAssociatedEdges: bool, preferFeatureElementEdges: bool, featureAngleTolerance: float, allowGapJumping: bool, gapJumpingTolerance: float, pathMethodType: typing.List[CAE.PathType], dTangentAngleTolerance: float) -> None:
        ...
    def SetTargetSetGroup(self, setIndex: int, filterType: CAE.CaeSetGroupFilterType, group: CAE.CaeGroup) -> None:
        ...
    def GetTargetSetGroup(self, setIndex: int) -> CAE.CaeGroup:
        ...
    def SetTargetSetMembers(self, setIndex: int, objects: typing.List[CAE.SetObject]) -> None:
        ...
    def SetTargetSetMembers(self, setIndex: int, selRecipeFilter: CAE.CaeSetGroupFilterType, objects: typing.List[CAE.SetObject]) -> None:
        ...
    def SetTargetSetExcludedMembers(self, setIndex: int, excludedObjects: typing.List[CAE.SetObject]) -> None:
        ...
    def SetTargetSetExcludedMembers(self, setIndex: int, selRecipeFilter: CAE.CaeSetGroupFilterType, objects: typing.List[CAE.SetObject]) -> None:
        ...
    def GetTargetSetMembers(self, setIndex: int, displayCoordinateSystem: NXObject, objects: typing.List[CAE.SetObject]) -> None:
        ...
    def GetTargetSetExcludedMembers(self, setIndex: int, objects: typing.List[CAE.SetObject]) -> None:
        ...
    def CleanTargetSet(self, setIndex: int) -> None:
        ...
    def SetTargetSetComponent(self, setIndex: int, comp: CAE.FEModelOccurrence) -> None:
        ...
    def GetTargetSetComponent(self, setIndex: int) -> CAE.FEModelOccurrence:
        ...
    def SetTargetSetSharedEdgeWithFaces(self, setIndex: int, edges: typing.List[CAE.CAEEdge], faces: typing.List[CAE.CAEFace]) -> None:
        ...
    def GetTargetSetSharedEdgeFaces(self, setIndex: int, faces: typing.List[CAE.CAEFace]) -> None:
        ...
    def SetTargetSetSegments(self, setIndex: int, curves: typing.List[Curve]) -> None:
        ...
    def GetTargetSetSegments(self, setIndex: int, curves: typing.List[Curve]) -> None:
        ...
    def SetTargetSetRevolutionSegments(self, setIndex: int, curves: typing.List[Curve]) -> None:
        ...
    def GetTargetSetRevolutionSegments(self, setIndex: int, curves: typing.List[Curve]) -> None:
        ...
    def DeleteTargetSet(self, setIndex: int) -> None:
        ...
    def SetTargetSetFacesCurve(self, setIndex: int, faces: typing.List[CAE.CAEFace], curve: Curve, reverse: bool) -> None:
        ...
    TargetSetCount: int


    class DistributedPlanesPosition(enum.Enum):
        Bbox = 0
        Manual = 1
    

    class DistributedPlanesBoundingSphereType(enum.Enum):
        Half = 0
        Full = 1
    

    class DistributedPlanesBoundingSphereDirection(enum.Enum):
        Vector = 0
        ThreePointsNormal = 1
    

    class DistributedPlanesBboxType(enum.Enum):
        Model = 0
        Selection = 1
    

class SensorSetRef(CAE.ISensorSet):
    def __init__(self) -> None: ...
    def SetName(self, name: str) -> None:
        ...
    def SetDofs(self, dofMasks: int, dofNegativeMasks: int) -> None:
        ...


class SensorSetMgr(CAE.IApplicationObjectManager):
    def __init__(self) -> None: ...
    def ShowSensorSetInformation(self, sensorSet: CAE.ISensorSet) -> None:
        ...
    def GetSensorset(self, sensorSetIndex: int) -> CAE.ISensorSet:
        ...
    def GetSensorSetByName(self, sensorSetName: str) -> CAE.ISensorSet:
        ...
    def CloneSensorSet(self, masterSensorSet: CAE.ISensorSet) -> CAE.ISensorSet:
        ...
    def ActivateSensorset(self, sensorSet: CAE.ISensorSet) -> None:
        ...
    def DeleteSensorset(self, sensorSet: CAE.ISensorSet) -> None:
        ...
    NumberOfSensorsets: int


class SensorSet(CAE.ISensorSet):
    def __init__(self) -> None: ...


class SelRecipeStrategy(CAE.SelRecipeBaseStrategy):
    def __init__(self) -> None: ...
    InputFilter: TaggedObject


class SelRecipeSingleLabelStrategy(CAE.SelRecipeStrategy):
    def __init__(self) -> None: ...
    def SetLabel(self, label: int) -> None:
        ...
    Label: int


class SelRecipeProximityStrategy(CAE.SelRecipeStrategy):
    def __init__(self) -> None: ...
    def GetEntities(self) -> typing.List[TaggedObject]:
        ...
    def SetEntitiesAndTolerance(self, objects: typing.List[TaggedObject], tolerance: float) -> None:
        ...
    Tolerance: float


class SelRecipePointStrategy(CAE.SelRecipeStrategy):
    def __init__(self) -> None: ...
    def SetPointAndTolerance(self, point: Point, tolerance: float) -> None:
        ...
    def SetResolvePreference(self, resolvePref: CAE.SelRecipeCoordinateStrategy.Pref) -> None:
        ...
    Point: Point
    ResolvePreference: CAE.SelRecipeCoordinateStrategy.Pref
    Tolerance: float


class SelRecipeLabelRangeStrategy(CAE.SelRecipeStrategy):
    def __init__(self) -> None: ...
    def GetLabelRanges(self, singleLabels: int, startLabels: int, endLabels: int, increments: int) -> None:
        ...
    def SetLabelRanges(self, singleLabels: int, startLabels: int, endLabels: int, increments: int) -> None:
        ...


class SelRecipeCoordinateStrategy(CAE.SelRecipeStrategy):
    def __init__(self) -> None: ...
    def SetCoordinatesAndTolerance(self, coordinates: Point3d, tolerance: float) -> None:
        ...
    def SetResolvePreference(self, resolvePref: CAE.SelRecipeCoordinateStrategy.Pref) -> None:
        ...
    Coordinates: Point3d
    ResolvePreference: CAE.SelRecipeCoordinateStrategy.Pref
    Tolerance: float


    class Pref(enum.Enum):
        LowestLabel = 0
        HighestLabel = 1
        ClosestNode = 2
    

class SelRecipeBuilder(Builder):
    def __init__(self) -> None: ...
    def AddBoxBoundingVolumeStrategy(self, centerPoint: Point, targetPoint: Point, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddBoxBoundingVolumeStrategy(self, centerCsys: CoordinateSystem, length: Expression, width: Expression, height: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddCylinderBoundingVolumeStrategy(self, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.SelRecipeBuilder.AddCylinderCsysDiametersHeightBoundingVolumeStrategy which uses additional inner dimensions as arguments.")"""
        ...
    def AddCylinderCsysDiametersHeightBoundingVolumeStrategy(self, centerCsys: CoordinateSystem, innerDiaOption: CAE.SelRecipeBuilder.InnerDiameter, outerDiaOption: CAE.SelRecipeBuilder.OuterDiameter, innerDiameter: Expression, outerDiameter: Expression, cylinderHeight: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddCylinderSectorBoundingVolumeStrategy(self, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression, isStartActive: bool, startAngle: Expression, isEndActive: bool, endAngle: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.SelRecipeBuilder.AddCylinderWithDimensionBoundingVolumeStrategy which uses inner dimensions as arguments.")"""
        ...
    def AddCylinderWithDimensionBoundingVolumeStrategy(self, centerCsys: CoordinateSystem, innerDiameter: Expression, outerDiameter: Expression, startHeight: Expression, endHeight: Expression, startAngle: Expression, endAngle: Expression, innerDiaOption: CAE.SelRecipeBuilder.InnerDiameter, outerDiaOption: CAE.SelRecipeBuilder.OuterDiameter, startHeightOption: CAE.SelRecipeBuilder.StartHeight, endHeightOption: CAE.SelRecipeBuilder.EndHeight, startAngleOption: CAE.SelRecipeBuilder.StartAngle, endAngleOption: CAE.SelRecipeBuilder.EndAngle, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddCylinderBoundingVolumeStrategy(self, diameter: Expression, baseCenter: Point, topCenter: Point, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.SelRecipeBuilder.AddCylinderEndpointsDiametersBoundingVolumeStrategy which uses additional inner diameter as arguments.")"""
        ...
    def AddCylinderEndpointsDiametersBoundingVolumeStrategy(self, innerDiaOption: CAE.SelRecipeBuilder.InnerDiameter, outerDiaOption: CAE.SelRecipeBuilder.OuterDiameter, innerDiameter: Expression, outerDiameter: Expression, baseCenter: Point, topCenter: Point, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddSphereBoundingVolumeStrategy(self, centerPoint: Point, diameter: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddSphereWithDiametersBoundingVolumeStrategy(self, centerPoint: Point, innerDiameter: Expression, outerDiameter: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddArbitraryVolMeshStrategy(self, mesh: CAE.Mesh, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddArbitraryVolPolygonBodyStrategy(self, body: CAE.CAEBody, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeBoundingVolumeStrategy:
        ...
    def AddAttributeStrategy(self, entityType: CAE.CaeSetGroupFilterType, inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeAttributeStrategy:
        ...
    def ResetEntityTypes(self, strategy: CAE.SelRecipeStrategy, entityTypes: typing.List[CAE.CaeSetGroupFilterType], inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> None:
        ...
    def AddProximityStrategy(self, selectedObject: typing.List[TaggedObject], tolerance: float, entityType: CAE.CaeSetGroupFilterType, inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeProximityStrategy:
        ...
    def AddAdapter(self, selectionMethod: SelectionMethod) -> CAE.SelRecipeAdapter:
        ...
    def AddCoordinateStrategy(self, coordinates: Point3d, tolerance: float, inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeCoordinateStrategy:
        ...
    def AddPointStrategy(self, point: Point, tolerance: float, inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipePointStrategy:
        ...
    def AddSingleLabelStrategy(self, nodeLabel: int, inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeSingleLabelStrategy:
        ...
    def AddLabelRangeStrategy(self, singleLabels: int, startLabels: int, endLabels: int, increments: int, entityType: CAE.CaeSetGroupFilterType, inputFilterType: CAE.SelRecipeBuilder.InputFilterType, inputFilter: TaggedObject) -> CAE.SelRecipeLabelRangeStrategy:
        ...
    def GetNthStrategy(self, index: int) -> CAE.SelRecipeBaseStrategy:
        ...
    def DeleteLastNStrategies(self, nStrategies: int) -> None:
        ...
    RecipeName: str


    class StartHeight(enum.Enum):
        NotDefined = 0
        Value = 1
        PositiveInfinity = 2
        NegativeInfinity = 3
    

    class StartAngle(enum.Enum):
        NotDefined = 0
        Value = 1
    

    class OuterDiameter(enum.Enum):
        Value = 0
        Infinity = 1
    

    class InputFilterType(enum.Enum):
        EntireModel = 0
        Mesh = 1
        Body = 2
        Component = 3
    

    class InnerDiameter(enum.Enum):
        NotDefined = 0
        Value = 1
    

    class EndHeight(enum.Enum):
        Value = 0
        PositiveInfinity = 1
        NegativeInfinity = 2
    

    class EndAngle(enum.Enum):
        NotDefined = 0
        Value = 1
    

class SelRecipeBoundingVolumeStrategy(CAE.SelRecipeStrategy):
    def __init__(self) -> None: ...
    BoundingVolume: CAE.BoundingVolumePrimitive


class SelRecipeBaseStrategy(TaggedObject):
    def __init__(self) -> None: ...
    StrategyType: CAE.SelRecipeBaseStrategy.Type


    class Type(enum.Enum):
        Invalid = -1
        BoundingVolume = 0
        Attribute = 1
        LabelRange = 2
        SingleLabel = 3
        Coordinate = 4
        Point = 5
        Proximity = 6
        AdjacentFaces = 7
        CircularEdges = 8
        CylinderFaces = 9
        FeatureEdgeNodes = 10
        FeatureElements = 11
        FeatureElementEdges = 12
        FeatureElementFaces = 13
        FeatureNodes = 14
        FeatureShellElements = 15
        FilletFaces = 16
        FilterBodies = 17
        FilterEdges = 18
        FilterElements = 19
        FilterFaces = 20
        HoleElementEdges = 21
        RelatedEdges = 22
        RelatedElementEdges = 23
        RelatedElementFaces = 24
        RelatedElements = 25
        RelatedCurves = 26
        RelatedFaces = 27
        RelatedNodes = 28
        RelatedVertices = 29
        SliverFaces = 30
        SpiderCoreNodes = 31
        TangentContinuousEdges = 32
        TangentFaces = 33
        AttachedElements = 34
        ShortEdges = 35
        RelatedBodies = 36
        FilterNodes = 37
        FreeElementEdges = 38
        FreeElementFaces = 39
        Count = 40
    

class SelRecipeAttributeStrategy(CAE.SelRecipeStrategy):
    def __init__(self) -> None: ...
    def GetNameAttribute(self, names: str) -> None:
        ...
    def SetNameAttribute(self, name: str) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloadedCAE.SelRecipeAttributeStrategy.SetNameAttribute that sets multiple strings instead.")"""
        ...
    def SetNameAttribute(self, names: str) -> None:
        ...
    def RemoveNameAttribute(self) -> None:
        ...
    def SetColorAttribute(self, color: int) -> None:
        ...
    def RemoveColorAttribute(self) -> None:
        ...
    def GetUserAttributeNames(self, userAttributeNames: str) -> None:
        ...
    def GetHasUserAttributes(self, attributeName: str) -> bool:
        ...
    def GetUserAttributes(self, attributeName: str, lowValueAttribute: typing.List[NXObject.AttributeInformation], highValueAttribute: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    def SetUserAttributes(self, attributeName: str, lowValueAttributes: typing.List[NXObject.AttributeInformation], highValueAttributes: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    def RemoveUserAttributes(self, attributeName: str) -> None:
        ...
    def ClearAllAttributes(self) -> None:
        ...
    def SetUserAttributes(self, setNameAttribute: bool, nameAttribute: str, setColorAttribute: bool, colorAttribute: int, lowValueAttributes: typing.List[NXObject.AttributeInformation], highValueAttributes: typing.List[NXObject.AttributeInformation]) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use overloadedCAE.SelRecipeAttributeStrategy.SetUserAttributes that sets multiple name attribute values instead.")"""
        ...
    def SetUserAttributes(self, setNameAttribute: bool, nameAttribute: str, setColorAttribute: bool, colorAttribute: int, lowValueAttributes: typing.List[NXObject.AttributeInformation], highValueAttributes: typing.List[NXObject.AttributeInformation]) -> None:
        ...
    ColorAttribute: int
    HasColorAttribute: bool
    HasNameAttribute: bool
    NameAttribute: str


class SelRecipeAdapter(CAE.SelRecipeBaseStrategy):
    def __init__(self) -> None: ...
    def ResetAdapter(self, selectionMethod: SelectionMethod) -> None:
        ...


class SelectSimBCList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAE.SimBC) -> bool:
        ...
    def Add(self, objects: typing.List[CAE.SimBC]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAE.SimBC, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAE.SimBC) -> bool:
        ...
    def Remove(self, object: CAE.SimBC, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAE.SimBC, view1: View, point1: Point3d, selection2: CAE.SimBC, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAE.SimBC]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAE.SimBC) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAE.SimBC]) -> None:
        ...
    def GetArray(self) -> typing.List[CAE.SimBC]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAE.SimBC, view1: View, point1: Point3d, selection2: CAE.SimBC, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAE.SimBC, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectMeshList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAE.Mesh) -> bool:
        ...
    def Add(self, objects: typing.List[CAE.Mesh]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAE.Mesh, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAE.Mesh) -> bool:
        ...
    def Remove(self, object: CAE.Mesh, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAE.Mesh, view1: View, point1: Point3d, selection2: CAE.Mesh, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAE.Mesh]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAE.Mesh) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAE.Mesh]) -> None:
        ...
    def GetArray(self) -> typing.List[CAE.Mesh]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAE.Mesh, view1: View, point1: Point3d, selection2: CAE.Mesh, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAE.Mesh, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectionRecipeDisplay(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SelectionRecipe) -> None: ...
    def Update(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    IsGraphicSymbolDisplayed: bool
    IsNameDisplayed: bool
    IsSingleSelectionEntityNameDisplayed: bool


class SelectionRecipeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.SelectionRecipe]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateBoxBoundingVolumeRecipe(self, name: str, centerCsys: CoordinateSystem, length: Expression, width: Expression, height: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateBoxBoundingVolumeRecipe(self, name: str, centerPoint: Point, targetPoint: Point, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateCylinderBoundingVolumeRecipe(self, name: str, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateCylinderBoundingVolumeRecipe(self, name: str, diameter: Expression, baseCenter: Point, topCenter: Point, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateSphereBoundingVolumeRecipe(self, name: str, centerPoint: Point, diameter: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateSingleLabelRecipe(self, name: str, nodeLabel: int) -> CAE.SingleLabelSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateLabelRangeRecipe(self, name: str, singleLabels: int, startLabels: int, endLabels: int, increments: int, entityType: CAE.CaeSetGroupFilterType) -> CAE.LabelRangeSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateCoordinateRecipe(self, name: str, coordinates: Point3d, tolerance: float) -> CAE.CoordinateSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreatePointRecipe(self, name: str, point: Point, tolerance: float) -> CAE.PointSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateAttributeRecipe(self, name: str, entityType: CAE.CaeSetGroupFilterType, resolveRelatedFeEntity: bool, relatedFeEntityType: CAE.CaeSetGroupFilterType) -> CAE.AttributeSelectionRecipe:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.SelRecipeBuilder instead.")"""
        ...
    def CreateSelRecipeBuilder(self) -> CAE.SelRecipeBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SelectionRecipe:
        ...
    def Copy(self, recipeToCopy: CAE.SelectionRecipe, name: str) -> CAE.SelectionRecipe:
        ...
    def Delete(self, recipes: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    def CreateCloneSelRecipeBuilder(self, deleteSourceRecipe: bool, sourceSelRecipe: CAE.SelectionRecipe) -> CAE.CloneSelRecipeBuilder:
        ...
    def Tag(self) -> Tag: ...



class SelectionRecipe(DisplayableObject):
    def __init__(self) -> None: ...
    def GetName(self) -> str:
        ...
    def SetName(self, name: str) -> None:
        ...
    def GetEntityTypes(self, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> None:
        ...
    def GetEntities(self) -> typing.List[TaggedObject]:
        ...
    def ShowContentsOnly(self) -> None:
        ...
    def ShowContents(self) -> None:
        ...
    def HideContents(self) -> None:
        ...
    def Information(self) -> None:
        ...
    def HasNonDisplayableEntities(self) -> bool:
        ...
    def GetNthStrategy(self, index: int) -> CAE.SelRecipeBaseStrategy:
        ...
    Display: CAE.SelectionRecipeDisplay


class SelectGroupsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateSelectGroupsBuilder(self) -> CAE.SelectGroupsBuilder:
        ...
    def Tag(self) -> Tag: ...



class SelectGroupsBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSelectedGroups(self, selectedGroups: typing.List[NXObject]) -> None:
        ...


class SelectFENodeList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAE.FENode) -> bool:
        ...
    def Add(self, objects: typing.List[CAE.FENode]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAE.FENode, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAE.FENode) -> bool:
        ...
    def Remove(self, object: CAE.FENode, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAE.FENode, view1: View, point1: Point3d, selection2: CAE.FENode, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAE.FENode]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAE.FENode) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAE.FENode]) -> None:
        ...
    def GetArray(self) -> typing.List[CAE.FENode]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAE.FENode, view1: View, point1: Point3d, selection2: CAE.FENode, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAE.FENode, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectFENode(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: CAE.FENode, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: CAE.FENode, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.FENode, view1: View, point1: Point3d, selection2: CAE.FENode, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.FENode, view1: View, point1: Point3d, selection2: CAE.FENode, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: CAE.FENode, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> CAE.FENode:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: CAE.FENode


class SelectFEElemFaceList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAE.FEElemFace) -> bool:
        ...
    def Add(self, objects: typing.List[CAE.FEElemFace]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAE.FEElemFace, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAE.FEElemFace) -> bool:
        ...
    def Remove(self, object: CAE.FEElemFace, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAE.FEElemFace, view1: View, point1: Point3d, selection2: CAE.FEElemFace, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAE.FEElemFace]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAE.FEElemFace) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAE.FEElemFace]) -> None:
        ...
    def GetArray(self) -> typing.List[CAE.FEElemFace]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAE.FEElemFace, view1: View, point1: Point3d, selection2: CAE.FEElemFace, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAE.FEElemFace, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectElementsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateSelectElementsBuilder(self) -> CAE.SelectElementsBuilder:
        ...
    def Tag(self) -> Tag: ...



class SelectElementsBuilder(Builder):
    def __init__(self) -> None: ...
    Selection: SelectTaggedObjectList


class SelectCAEFaceList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAE.CAEFace) -> bool:
        ...
    def Add(self, objects: typing.List[CAE.CAEFace]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAE.CAEFace, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAE.CAEFace) -> bool:
        ...
    def Remove(self, object: CAE.CAEFace, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEFace, view1: View, point1: Point3d, selection2: CAE.CAEFace, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAE.CAEFace]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAE.CAEFace) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAE.CAEFace]) -> None:
        ...
    def GetArray(self) -> typing.List[CAE.CAEFace]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEFace, view1: View, point1: Point3d, selection2: CAE.CAEFace, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAE.CAEFace, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCAEFace(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: CAE.CAEFace, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: CAE.CAEFace, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEFace, view1: View, point1: Point3d, selection2: CAE.CAEFace, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEFace, view1: View, point1: Point3d, selection2: CAE.CAEFace, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: CAE.CAEFace, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> CAE.CAEFace:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: CAE.CAEFace


class SelectCAEEdgeList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAE.CAEEdge) -> bool:
        ...
    def Add(self, objects: typing.List[CAE.CAEEdge]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAE.CAEEdge, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAE.CAEEdge) -> bool:
        ...
    def Remove(self, object: CAE.CAEEdge, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEEdge, view1: View, point1: Point3d, selection2: CAE.CAEEdge, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAE.CAEEdge]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAE.CAEEdge) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAE.CAEEdge]) -> None:
        ...
    def GetArray(self) -> typing.List[CAE.CAEEdge]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEEdge, view1: View, point1: Point3d, selection2: CAE.CAEEdge, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAE.CAEEdge, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCAEEdge(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: CAE.CAEEdge, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: CAE.CAEEdge, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEEdge, view1: View, point1: Point3d, selection2: CAE.CAEEdge, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEEdge, view1: View, point1: Point3d, selection2: CAE.CAEEdge, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: CAE.CAEEdge, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> CAE.CAEEdge:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: CAE.CAEEdge


class SelectCAEBodyList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CAE.CAEBody) -> bool:
        ...
    def Add(self, objects: typing.List[CAE.CAEBody]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CAE.CAEBody, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CAE.CAEBody) -> bool:
        ...
    def Remove(self, object: CAE.CAEBody, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEBody, view1: View, point1: Point3d, selection2: CAE.CAEBody, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CAE.CAEBody]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CAE.CAEBody) -> bool:
        ...
    def SetArray(self, objects: typing.List[CAE.CAEBody]) -> None:
        ...
    def GetArray(self) -> typing.List[CAE.CAEBody]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEBody, view1: View, point1: Point3d, selection2: CAE.CAEBody, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CAE.CAEBody, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCAEBody(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: CAE.CAEBody, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: CAE.CAEBody, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEBody, view1: View, point1: Point3d, selection2: CAE.CAEBody, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: CAE.CAEBody, view1: View, point1: Point3d, selection2: CAE.CAEBody, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: CAE.CAEBody, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> CAE.CAEBody:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: CAE.CAEBody


class RigidEADBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDofs(self) -> typing.List[CAE.RigidEADBuilder.Dof]:
        ...
    def SetDofs(self, dofs: typing.List[CAE.RigidEADBuilder.Dof]) -> None:
        ...
    DofsState: CAE.RigidEADBuilder.State
    Elements: CAE.SelectElementsBuilder
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.RigidEADBuilder.State


    class State(enum.Enum):
        Apply = 0
        Clear = 1
        Ignore = 2
    

    class Dof(enum.Enum):
        Off = 0
        On = 1
    

class ResultVariable(Fields.NameVariable):
    def __init__(self) -> None: ...
    def Rename(self, expname: str) -> None:
        ...
    Abs: bool
    AcousticWeighting: CAE.SignalProcessingPlotData.AcousticalWeighting
    Addfillets: bool
    BeamSect: CAE.Result.Section
    BeamSection: CAE.Result.BeamSection
    Comp: CAE.Result.Component
    Complex: CAE.Result.Complex
    Complexopt: CAE.ResultVariable.ComplexType
    Computetype: CAE.Result.ComputationType
    Csys: CAE.Result.CoordinateSystem
    Derivebeamres: bool
    Elementcriteria: CAE.Result.ElementValueCriterion
    Elemtypes: bool
    Expname: str
    Filletradscale: float
    IncludeInternalElement: bool
    Layer: int
    Loc: CAE.Result.Location
    Mids: bool
    Nodalcombinetype: CAE.ResultVariable.NodalCombination
    Numberofcomponent: int
    Phase: float
    Pids: bool
    Plyid: int
    ProjectOnNodeNormal: bool
    Quan: CAE.Result.Quantity
    Selectedcsys: CoordinateSystem
    ShellSect: CAE.Result.Section
    ShellSection: CAE.Result.ShellSection
    SpectrumScaling: CAE.SignalProcessingPlotData.ScalingType
    Usertypename: str


    class NodalCombination(enum.Enum):
        None = 0
        Nodal = 1
        Elemental = 2
    

    class ComplexType(enum.Enum):
        Real = 0
        Imaginary = 1
        Amplitude = 2
        SignedAmplitude = 3
        PhaseAngle = 4
        RealImaginary = 5
    

class ResultUnitSystem(TaggedObject):
    def __init__(self) -> None: ...
    AmountOfSubstanceUnit: Unit
    AngleUnit: Unit
    DeltaTemperatureUnit: Unit
    ElectricChargeUnit: Unit
    LengthUnit: Unit
    LumiousIntensityUnit: Unit
    MassUnit: Unit
    TemperatureUnit: Unit
    TimeUnit: Unit


class ResultType(CAE.BaseResultType):
    def __init__(self) -> None: ...
    Subtitle: str
    Title: str


class ResultToSCD5Converter(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def Convert(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    ExportMidNodeResult: bool
    Outputfile: str
    Result: CAE.Result
    ResultFileUnitUsed: bool
    TemperatureUnit: CAE.ResultToSCD5Converter.Temperature
    TemperatureUnitSpecified: bool
    UnitSystemOption: CAE.ResultToSCD5Converter.UnitSystem


    class UnitSystem(enum.Enum):
        MeterNewton = 0
        FootPoundForce = 1
        MeterKilogramForce = 2
        FootPoundal = 3
        MillimeterMilliNewton = 4
        CentimeterCentiNewton = 5
        InchPoundForce = 6
        MillimeterKilogramForce = 7
        MillimeterNewton = 8
    

    class Temperature(enum.Enum):
        Celsius = 0
        Fahrenheit = 1
        Kelvin = 2
        Rankine = 3
    

class ResultsReductionBuilder(CAE.ResultsManipulationBuilder):
    def __init__(self) -> None: ...
    def SetResults(self, results: typing.List[CAE.Result], parameters: typing.List[CAE.ResultParameters], names: str) -> None:
        ...
    def SetFormula(self, formula: str) -> None:
        ...
    def SetIncompatibleResultsOption(self, incompatibleResultsOption: CAE.ResultsReductionBuilder.IncompatibleResults) -> None:
        ...
    def SetNoDataOption(self, noDataOption: CAE.ResultsReductionBuilder.NoData) -> None:
        ...
    def SetEvaluationErrorOption(self, evaluationErrorOption: CAE.ResultsReductionBuilder.EvaluationError) -> None:
        ...
    def SetOutput(self, output: CAE.ResultsReductionBuilder.Output) -> None:
        ...
    def SetResultTypeName(self, resultTypeName: str) -> None:
        ...
    def SetResultUnit(self, unit: Unit) -> None:
        ...
    def SetViewIndexForPostView(self, viewIndex: int) -> None:
        ...
    def SetFieldName(self, fieldName: str) -> None:
        ...
    def SetIndependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsReductionBuilder.SetIndependentDomain instead.")"""
        ...
    def SetDependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsReductionBuilder.SetDependentDomain instead.")"""
        ...
    def SetElementValueAtNode(self, value: CAE.ResultsManipulationBuilder.ElementValueAtNode) -> None:
        ...
    def SetIndependentDomain(self, domain: Fields.FieldDomain) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultsReductionBuilder.SetIndependentEnum instead.")"""
        ...
    def SetDependentDomain(self, domain: Fields.FieldDomain) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultsReductionBuilder.SetDependentEnum instead.")"""
        ...
    def SetIndependentEnum(self, indepenDomain: int) -> None:
        ...
    def SetDependentEnum(self, depenDomain: int) -> None:
        ...


    class Output(enum.Enum):
        ExportResultFile = 0
        CreatePostView = 1
        CreateField = 2
    

    class NoData(enum.Enum):
        Skip = 0
        ZeroFill = 1
    

    class IncompatibleResults(enum.Enum):
        Skip = 0
        Abort = 1
    

    class EvaluationError(enum.Enum):
        Skip = 0
        ZeroFill = 1
        Abort = 2
    

class ResultSourceBuilder(Builder):
    def __init__(self) -> None: ...
    def GetResfiles(self) -> str:
        ...
    def SetResfiles(self, files: str) -> None:
        ...
    Name: str


class ResultsModelExportBuilder(CAE.ResultsManipulationBuilder):
    def __init__(self) -> None: ...
    def SetResult(self, result: CAE.Result) -> None:
        ...


class ResultsManipulationUnitsSystem(TaggedObject):
    def __init__(self) -> None: ...
    def GetUserDefinedSystemUnits(self) -> CAE.Result.ResultBasicUnit:
        ...
    def SetUserDefinedSystemUnits(self, userDefinedSystemUnits: CAE.Result.ResultBasicUnit) -> None:
        ...
    Result: CAE.Result
    UnitsSystemType: CAE.ResultsManipulationUnitsSystem.Type


    class Type(enum.Enum):
        None = 0
        FromResult = 1
        UserDefined = 2
    

class ResultsManipulationInputSettings(TaggedObject):
    def __init__(self) -> None: ...
    def GetResultsAndParameters(self, results: typing.List[CAE.Result], parameters: typing.List[CAE.ResultParameters]) -> None:
        ...
    def SetResultsAndParameters(self, results: typing.List[CAE.Result], parameters: typing.List[CAE.ResultParameters]) -> None:
        ...
    EntitiesSelection: CAE.PostEntitiesSelection


class ResultsManipulationErrorHandling(TaggedObject):
    def __init__(self) -> None: ...
    IncompatibleResultsOption: CAE.ResultsManipulationErrorHandling.IncompatibleResults
    NoDataOption: CAE.ResultsManipulationErrorHandling.NoData


    class NoData(enum.Enum):
        Skip = 0
        ZeroFill = 1
    

    class IncompatibleResults(enum.Enum):
        Skip = 0
        Abort = 1
    

class ResultsManipulationEnvelopeBuilder(Builder):
    def __init__(self) -> None: ...
    ApproachOption: CAE.ResultsManipulationEnvelopeBuilder.Approach
    ErrorHandling: CAE.ResultsManipulationErrorHandling
    InputSettings: CAE.ResultsManipulationInputSettings
    NeedOutputIDResults: bool
    OperationOption: CAE.ResultsManipulationEnvelopeBuilder.Operation
    OutputFieldSettings: CAE.ResultsManipOutputFieldSettings
    OutputFileSettings: CAE.ResultsManipOutputFileSettings
    OutputOption: CAE.ResultsManipulationEnvelopeBuilder.Output
    UnitSystem: CAE.ResultsManipulationUnitsSystem


    class Output(enum.Enum):
        ExportToUniversalFile = 0
        CreateField = 1
    

    class Operation(enum.Enum):
        Maximum = 0
        Minimum = 1
        AbsoluteMaximum = 2
        AbsoluteMinimum = 3
    

    class Approach(enum.Enum):
        ThroughLoadCases = 0
        ThroughLoadCasesandResults = 1
    

class ResultsManipulationBuilder(Builder):
    def __init__(self) -> None: ...
    def SetAction(self, action: CAE.ResultsManipulationBuilder.Action) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.CAE.ResultsManipulationBuilder.SetOutputResultType instead.")"""
        ...
    def SetOutputName(self, outputName: str) -> None:
        ...
    def SetLoadcaseName(self, loadcaseName: str) -> None:
        ...
    def SetOutputFile(self, outputFile: str) -> None:
        ...
    def SetImportedSolutionName(self, importedSolutionName: str) -> None:
        ...
    def SetCompanionSolution(self, solution: CAE.SimSolution) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use SetCompanionResultReference instead.")"""
        ...
    def SetCompanionResultName(self, companionResultName: str) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use SetCompanionIdentifier instead.")"""
        ...
    def SetAppendMethod(self, appendMethod: CAE.ResultsManipulationBuilder.ResultAppendMethod) -> None:
        ...
    def SetUnitsSystem(self, unitsSystem: CAE.ResultsManipulationBuilder.UnitsSystem) -> None:
        ...
    def SetUserDefinedUnitsSystem(self, unitsSystem: CAE.Result.ResultBasicUnit) -> None:
        ...
    def SetUnitsSystemResult(self, result: CAE.Result) -> None:
        ...
    def SetOutputQuantity(self, quantity: CAE.Result.Quantity) -> None:
        ...
    def SetIncludeModel(self, includeModel: bool) -> None:
        ...
    def SetImportResult(self, importResult: bool) -> None:
        ...
    def SetOutputResultType(self, type: CAE.ResultsManipulationBuilder.OutputResultType) -> None:
        ...
    def SetCreateSolution(self, createSolution: bool) -> None:
        ...
    def SetCompanionResultReference(self, tResultRef: CAE.SimResultReference) -> None:
        ...
    def SetCompanionIdentifier(self, companionIdentifier: str) -> None:
        ...


    class UnitsSystem(enum.Enum):
        None = 0
        FromResult = 1
        UserDefined = 2
    

    class ResultAppendMethod(enum.Enum):
        CreateNewLoadCases = 0
        MergeWithPrimaryResultsData = 1
    

    class OutputResultType(enum.Enum):
        Companion = 0
        Full = 1
    

    class ElementValueAtNode(enum.Enum):
        Average = 0
        Maximum = 1
        Minimum = 2
        Sum = 3
    

    class Action(enum.Enum):
        Export = 0
        ExportResultsOnly = 1
        ExportResultsAndModel = 2
        CreateImportedResult = 3
        CreateCompanionResult = 4
        CreateCompanionResultWithModel = 5
        CreateImportedSolution = 6
    

class ResultsManipOutputFileSettings(TaggedObject):
    def __init__(self) -> None: ...
    AppendMethodOption: CAE.ResultsManipOutputFileSettings.AppendMethod
    CompanionName: str
    CompanionResultReference: CAE.SimResultReference
    LoadCaseName: str
    NeedCreateSolution: bool
    NeedExportModel: bool
    NeedLoadImmediately: bool
    OutputFile: str
    OutputName: str
    ResultModeOption: CAE.ResultsManipOutputFileSettings.ResultMode
    SolutionName: str


    class ResultMode(enum.Enum):
        Companion = 0
        Full = 1
    

    class AppendMethod(enum.Enum):
        CreateNewLoadCase = 0
        MergeIntoPrimaryResultData = 1
    

class ResultsManipOutputFieldSettings(TaggedObject):
    def __init__(self) -> None: ...
    def GetFieldDescription(self) -> str:
        ...
    def SetFieldDescription(self, fieldDescription: str) -> None:
        ...
    CalculationMethodForValueAtNode: CAE.ResultsManipOutputFieldSettings.CalculationMethodForValueAtNodeOptions
    DepDomain: int
    FieldLabel: int
    FieldName: str
    IndepDomain: int
    IndependentDomainForElementNodalResult: CAE.ResultsManipOutputFieldSettings.IndepDomainDefinitionOptions
    IndependentDomainForElementalResult: CAE.ResultsManipOutputFieldSettings.IndepDomainDefinitionOptions
    IndependentDomainForNodalResult: CAE.ResultsManipOutputFieldSettings.IndepDomainDefinitionOptions


    class IndepDomainDefinitionOptions(enum.Enum):
        Cartesian = 0
        NodeID = 1
        ElementID = 2
        ElementNodeID = 3
    

    class CalculationMethodForValueAtNodeOptions(enum.Enum):
        Average = 0
        Maximum = 1
        Minimum = 2
        Sum = 3
    

class ResultsEnvelopeBuilder(CAE.ResultsManipulationBuilder):
    def __init__(self) -> None: ...
    def SetOutput(self, output: CAE.ResultsEnvelopeBuilder.Output) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetResults(self, results: typing.List[CAE.Result], parameters: typing.List[CAE.ResultParameters]) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetResults(self, ids: int, results: typing.List[CAE.Result], parameters: typing.List[CAE.ResultParameters]) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetOperation(self, operation: CAE.ResultsEnvelopeBuilder.Operation) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetIncompatibleResultsOption(self, incompatibleResultsOption: CAE.ResultsEnvelopeBuilder.IncompatibleResults) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetNoDataOption(self, noDataOption: CAE.ResultsEnvelopeBuilder.NoData) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetFieldName(self, fieldName: str) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetIndependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsEnvelopeBuilder.SetIndependentDomain instead.")"""
        ...
    def SetDependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsEnvelopeBuilder.SetDependentDomain instead.")"""
        ...
    def SetElementValueAtNode(self, value: CAE.ResultsManipulationBuilder.ElementValueAtNode) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetIndependentDomain(self, domain: Fields.FieldDomain) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultsEnvelopeBuilder.SetIndependentEnum instead.")"""
        ...
    def SetDependentDomain(self, domain: Fields.FieldDomain) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultsEnvelopeBuilder.SetDependentEnum instead.")"""
        ...
    def SetIndependentEnum(self, indepenDomain: int) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...
    def SetDependentEnum(self, depenDomain: int) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultsManipulationEnvelopeBuilder")"""
        ...


    class Output(enum.Enum):
        ExportResultFile = 0
        CreateField = 1
    

    class Operation(enum.Enum):
        Minimum = 0
        Maximum = 1
    

    class NoData(enum.Enum):
        Skip = 0
        ZeroFill = 1
    

    class IncompatibleResults(enum.Enum):
        Skip = 0
        Abort = 1
    

class ResultsCombinationBuilder(CAE.ResultsManipulationBuilder):
    def __init__(self) -> None: ...
    def SetOutput(self, output: CAE.ResultsCombinationBuilder.Output) -> None:
        ...
    def SetResultTypes(self, types: typing.List[CAE.BaseResultType], names: str) -> None:
        ...
    def SetResultTypes(self, types: typing.List[CAE.BaseResultType], names: str, units: typing.List[Unit]) -> None:
        ...
    def SetFormula(self, formula: str) -> None:
        ...
    def SetIncompatibleResultsOption(self, incompatibleResultsOption: CAE.ResultsCombinationBuilder.IncompatibleResults) -> None:
        ...
    def SetNoDataOption(self, noDataOption: CAE.ResultsCombinationBuilder.NoData) -> None:
        ...
    def SetEvaluationErrorOption(self, evaluationErrorOption: CAE.ResultsCombinationBuilder.EvaluationError) -> None:
        ...
    def SetFieldName(self, fieldName: str) -> None:
        ...
    def SetIndependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsCombinationBuilder.SetIndependentDomain instead.")"""
        ...
    def SetDependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsCombinationBuilder.SetDependentDomain instead.")"""
        ...
    def SetElementValueAtNode(self, value: CAE.ResultsManipulationBuilder.ElementValueAtNode) -> None:
        ...
    def SetIndependentDomain(self, domain: Fields.FieldDomain) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultsCombinationBuilder.SetIndependentEnum instead.")"""
        ...
    def SetDependentDomain(self, domain: Fields.FieldDomain) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultsCombinationBuilder.SetDependentEnum instead.")"""
        ...
    def SetIndependentEnum(self, indepenDomain: int) -> None:
        ...
    def SetDependentEnum(self, depenDomain: int) -> None:
        ...


    class Output(enum.Enum):
        ExportResultFile = 0
        CreateField = 1
    

    class NoData(enum.Enum):
        Skip = 0
        ZeroFill = 1
    

    class IncompatibleResults(enum.Enum):
        Skip = 0
        Abort = 1
    

    class EvaluationError(enum.Enum):
        Skip = 0
        ZeroFill = 1
        Abort = 2
    

class ResultProbeBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def SetEntityObjects(self, entityObjs: typing.List[TaggedObject]) -> None:
        ...
    def GetDefaultUnit(self) -> Unit:
        ...
    AcousticModeIndex: int
    BandCombinationType: CAE.ResultProbeBuilder.BandCombinationOpt
    BoltSequenceIndex: int
    CombineAcross: bool
    CombineAcrossIteration: bool
    CombineAcrossLcase: bool
    CombineIterOption: CAE.ResultProbeBuilder.CombineAcrossIterations
    CombineLcaseOption: CAE.ResultProbeBuilder.CombineAcrossLoadcases
    CombinedValue: CAE.ResultProbeBuilder.CombineAcrossEntities
    ConvertOrderToWF: bool
    DesignCycleIndex: int
    EdgeIntegralOption: CAE.ResultProbeBuilder.EdgeIntegral
    ElemIntegralOption: CAE.ResultProbeBuilder.ElemIntegral
    EndIterIndex: int
    EndIterValForIterSweep: float
    EndIterValue: float
    EndLcaseIndex: int
    EndLcaseValue: float
    ErrorHndl: CAE.ResultProbeBuilder.ErrorHandling
    FaceIntegralOption: CAE.ResultProbeBuilder.FaceIntegral
    Formula: str
    FrequencyPacking: bool
    FrequencyPackingType: CAE.ResultProbeBuilder.FrequencyPackingOpt
    GeometryAverageValue: CAE.ResultProbeBuilder.GeometryValue
    GroupIntegralOption: CAE.ResultProbeBuilder.GroupIntegral
    GroupsSelectBuilder: CAE.SelectGroupsBuilder
    HarmonicIndex: int
    InterpolationType: CAE.ResultProbeBuilder.Interpolation
    IterNearValue: float
    Iteration: CAE.ResultProbeBuilder.IterationSelection
    IterationIndex: int
    IterationListSelOption: CAE.ResultProbeBuilder.IterationListSelOpt
    IterationListSweepOption: CAE.ResultProbeBuilder.IterationListSweepOpt
    IterationTypeOption: CAE.ResultProbeBuilder.IterationType
    Loadcase: CAE.ResultProbeBuilder.LoadcaseSelection
    LoadcaseIndex: int
    LogBaseForIterSweep: float
    ModelSelectionType: CAE.ResultProbeBuilder.SelectionType
    NodalAveraging: CAE.ResultProbeBuilder.NodalCombination
    NumOfStepsForIterSweep: int
    PickSequentially: bool
    ProbeName: str
    QueryCurveUsageOptions: CAE.QueryCurveUsageOptions
    ResultReferenceType: CAE.SimResultReference.Type
    ResultType: CAE.Result.Quantity
    RotationSpeedValue: float
    SkipSteps: int
    StartIterIndex: int
    StartIterValForLinearSweep: float
    StartIterValForLogSweep: float
    StartIterValue: float
    StartLcaseIndex: int
    StartLcaseValue: float
    StepValForIterSweep: float
    SuperIterationType: CAE.ResultProbeBuilder.SuperIterType
    Unit: Unit


    class SuperIterType(enum.Enum):
        None = 0
        Harmonic = 1
        RotationSpeed = 2
        DesignCycle = 3
        Acoustic = 4
        BoltSequence = 5
    

    class SelectionType(enum.Enum):
        EntireModel = 0
        Nodes = 1
        Elements = 2
        Points = 3
        Edges = 4
        Faces = 5
        Bodies = 6
        QueryCurve = 7
        None = 8
        Group = 9
        SelectionRecipe = 10
    

    class NodalCombination(enum.Enum):
        ArithmeticMean = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
    

    class LoadcaseSelection(enum.Enum):
        First = 0
        Last = 1
        SpecifyIndex = 2
        All = 3
        Ignore = 4
        None = 5
        SpecifyRange = 6
        BetweenValues = 7
    

    class IterationType(enum.Enum):
        Time = 0
        Frequency = 1
        LoadFactor = 2
        EigenValue = 3
        All = 4
    

    class IterationSelection(enum.Enum):
        First = 0
        Last = 1
        NeartoValue = 2
        SpecifyIndex = 3
        All = 4
        SpecifyRange = 5
        BetweenValues = 6
        None = 7
        AtValue = 8
        AtValues = 9
    

    class IterationListSweepOpt(enum.Enum):
        Interval = 0
        Base = 1
        NumberOfSteps = 2
        StepValue = 3
    

    class IterationListSelOpt(enum.Enum):
        LinearSweep = 0
        LogSweep = 1
    

    class Interpolation(enum.Enum):
        AmplitudePhase = 0
        RealImaginary = 1
        RealImaginaryWithUnwrappedPhase = 2
    

    class GroupIntegral(enum.Enum):
        Area = 0
        Volume = 1
    

    class GeometryValue(enum.Enum):
        ArithmeticMean = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
        WeightedAverage = 4
        Integral = 5
        AbsoluteMaximum = 6
        AbsoluteMinimum = 7
        SignedAbsoluteMaximum = 8
        SignedAbsoluteMinimum = 9
        None = 10
        Rms = 11
        Rss = 12
        WeightedRMS = 13
        WeightedRSS = 14
    

    class FrequencyPackingOpt(enum.Enum):
        Octave = 0
        OneThirdOctave = 1
        OneTwelfthOctave = 2
        SingleBand = 3
    

    class FaceIntegral(enum.Enum):
        Area = 0
        Volume = 1
    

    class ErrorHandling(enum.Enum):
        Fillzero = 0
        Skip = 1
    

    class ElemIntegral(enum.Enum):
        Area = 0
        Volume = 1
    

    class EdgeIntegral(enum.Enum):
        Length = 0
        Area = 1
    

    class CombineAcrossLoadcases(enum.Enum):
        ArithmeticMean = 0
        AbsoluteMaximum = 1
        Maximum = 2
        AbsoluteMinimum = 3
        Minimum = 4
        Sum = 5
        SignedAbsoluteMaximum = 6
        SignedAbsoluteMinimum = 7
        Rss = 8
        Rms = 9
        UseIterCombination = 10
    

    class CombineAcrossIterations(enum.Enum):
        ArithmeticMean = 0
        AbsoluteMaximum = 1
        Maximum = 2
        AbsoluteMinimum = 3
        Minimum = 4
        Sum = 5
        SignedAbsoluteMaximum = 6
        SignedAbsoluteMinimum = 7
    

    class CombineAcrossEntities(enum.Enum):
        ArithmeticMean = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
        Difference = 4
        WeightedAverage = 5
        Integral = 6
        AbsoluteMaximum = 7
        AbsoluteMinimum = 8
        SignedAbsoluteMaximum = 9
        SignedAbsoluteMinimum = 10
        Rms = 11
        Rss = 12
        WeightedRMS = 13
        WeightedRSS = 14
    

    class BandCombinationOpt(enum.Enum):
        ArithmeticMean = 0
        Rms = 1
        Rss = 2
        Sum = 3
        WeightedAverage = 4
        Integral = 5
        WeightedRMS = 6
        WeightedRSS = 7
    

class ResultProbe(Fields.Field):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def CopyToSolution(self, targetSolution: CAE.SimSolution) -> CAE.ResultProbe:
        ...
    def GetOutputOptions(self) -> typing.List[CAE.ResultProbe.OutputOption]:
        ...
    def GetOutputRecipes(self) -> typing.List[CAE.ProbeOutputRecipe]:
        ...
    def GetOutputRecipe(self, recipeType: CAE.ProbeOutputRecipe.Type) -> CAE.ProbeOutputRecipe:
        ...
    def CreateTableField(self) -> Fields.Field:
        ...


    class OutputOption(enum.Enum):
        Information = 0
        Graph = 1
        Graph3D = 2
        Field = 3
        UnvFile = 4
        PostView = 5
        ExportField = 6
    

class ResultParametersWithProbe(TaggedObject):
    def __init__(self) -> None: ...
    def GetResultProbe(self) -> CAE.ResultProbe:
        ...
    def GetCurrentLoadcase(self) -> CAE.BaseLoadcase:
        ...
    def SetCurrentLoadcase(self, loadcase: CAE.BaseLoadcase) -> None:
        ...
    def GetCurrentIteration(self) -> CAE.BaseIteration:
        ...
    def SetCurrentIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    def GetUnit(self) -> Unit:
        ...
    def SetUnit(self, unit: Unit) -> None:
        ...
    def GetIterationValue(self) -> float:
        ...
    def SetIterationValue(self, value: float) -> None:
        ...
    def GetInterpolated(self) -> bool:
        ...
    def SetInterpolated(self, value: bool) -> None:
        ...
    def GetComplexType(self) -> CAE.Result.Complex:
        ...
    def SetComplexType(self, complexType: CAE.Result.Complex) -> None:
        ...
    def GetPhaseAngle(self) -> float:
        ...
    def SetPhaseAngle(self, value: float) -> None:
        ...
    def GetDBScaling(self) -> bool:
        ...
    def SetDBScaling(self, dBscaling: bool) -> None:
        ...
    def GetDBreference(self) -> float:
        ...
    def SetDBReference(self, dBreference: float) -> None:
        ...
    def GetDBFormat(self) -> CAE.Result.DbScale:
        ...
    def SetDBFormat(self, dbScale: CAE.Result.DbScale) -> None:
        ...
    def SetSpectrumScaling(self, scaling: CAE.SignalProcessingPlotData.ScalingType) -> None:
        ...
    def GetSpectrumScaling(self) -> CAE.SignalProcessingPlotData.ScalingType:
        ...
    def SetAcousticWeighting(self, weighting: CAE.SignalProcessingPlotData.AcousticalWeighting) -> None:
        ...
    def GetAcousticWeighting(self) -> CAE.SignalProcessingPlotData.AcousticalWeighting:
        ...
    def GetLcaseValue(self) -> float:
        ...
    def SetLcaseValue(self, value: float) -> None:
        ...


class ResultParametersWithNodalForceReport(TaggedObject):
    def __init__(self) -> None: ...
    def GetNodalForceReport(self) -> CAE.NodalForceReport:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.ResultParametersWithNodalForceReport.GetNodalForceReports")"""
        ...
    def GetCurrentIteration(self) -> CAE.BaseIteration:
        ...
    def SetCurrentIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    def GetUnit(self) -> Unit:
        ...
    def SetUnit(self, unit: Unit) -> None:
        ...
    def GetCurrentResultType(self) -> CAE.ResultParametersWithNodalForceReport.ResultType:
        ...
    def SetCurrentResultType(self, resultType: CAE.ResultParametersWithNodalForceReport.ResultType) -> None:
        ...
    def GetCurrentResultComp(self) -> CAE.Result.Component:
        ...
    def SetCurrentResultComp(self, resultComp: CAE.Result.Component) -> None:
        ...
    def GetNodalForceReports(self, freebodyList: typing.List[CAE.NodalForceReport]) -> None:
        ...
    def SetDisplayAtCentroid(self, displayAtCentroid: bool) -> None:
        ...
    def GetDisplayAtCentroid(self) -> bool:
        ...


    class ResultType(enum.Enum):
        Force = 0
        Moment = 1
    

class ResultParametersMultiValue(CAE.ResultParameters):
    def __init__(self) -> None: ...
    IsAllBeamSections: bool
    IsAllPlyLocations: bool
    IsAllPrimaryComponents: bool
    IsAllShellSections: bool


class ResultParameters(TaggedObject):
    def __init__(self) -> None: ...
    def GetLoadcase(self) -> int:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def GetIteration(self) -> int:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def SetLoadcaseIteration(self, loadcase: int, iteration: int) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.SetGenericResultType instead.")"""
        ...
    def GetResultDataLocation(self) -> CAE.Result.Location:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.BaseResultType.Location instead.")"""
        ...
    def SetResultDataLocation(self, location: CAE.Result.Location) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def GetDBScaling(self) -> bool:
        ...
    def SetDBScaling(self, dBscaling: int) -> None:
        ...
    def GetDBreference(self) -> float:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultParameters.GetDbSettings instead.")"""
        ...
    def SetDBReference(self, dBreference: float) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultParameters.GetDbSettings instead.")"""
        ...
    def GetDBscale(self) -> CAE.Result.DbScale:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultParameters.GetDbSettings instead.")"""
        ...
    def SetDBscale(self, dbScale: CAE.Result.DbScale) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultParameters.GetDbSettings instead.")"""
        ...
    def GetResultDataSection(self) -> CAE.Result.Section:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def SetResultDataSection(self, section: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def GetResultBeamSection(self) -> CAE.Result.Section:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultParameters.GetBeamSection instead.")"""
        ...
    def SetResultBeamSection(self, section: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultParameters.SetBeamSection instead.")"""
        ...
    def GetResultShellSection(self) -> CAE.Result.Section:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultParameters.GetShellSection instead.")"""
        ...
    def SetResultShellSection(self, section: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ResultParameters.SetShellSection instead.")"""
        ...
    def GetResultDataQuantity(self) -> CAE.Result.Quantity:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def SetResultDataQuantity(self, quantity: CAE.Result.Quantity) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def GetResultType(self) -> CAE.Result.Type:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def SetResultType(self, type: CAE.Result.Type) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.CAE.ResultParameters.GetGenericResultType instead.")"""
        ...
    def GetGenericResultType(self) -> CAE.BaseResultType:
        ...
    def SetCyclicSymmetricParameters(self, type: CAE.CyclicSymmetricParameters) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.ResultParameters.SetCyclicSymmParameters instead. There can be more than 1 CyclicSymmetricParameters now.")"""
        ...
    def GetCyclicSymmetricParameters(self) -> CAE.CyclicSymmetricParameters:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.ResultParameters.GetCyclicSymmParameters instead. There can be more than 1 CyclicSymmetricParameters now.")"""
        ...
    def SetAxiSymmetricParameters(self, type: CAE.AxiSymmetricParameters) -> None:
        ...
    def GetAxiSymmetricParameters(self) -> CAE.AxiSymmetricParameters:
        ...
    def SetGenericResultType(self, type: CAE.BaseResultType) -> None:
        ...
    def GetResultComponent(self) -> CAE.Result.Component:
        ...
    def SetResultComponent(self, component: CAE.Result.Component) -> None:
        ...
    def GetCoordinateSystem(self) -> CAE.Result.CoordinateSystem:
        ...
    def SetCoordinateSystem(self, coordinate: CAE.Result.CoordinateSystem) -> None:
        ...
    def GetSelectedCoordinateSystem(self, source: CAE.Result.CoordinateSystemSource, id: int) -> None:
        ...
    def SetSelectedCoordinateSystem(self, source: CAE.Result.CoordinateSystemSource, id: int) -> None:
        ...
    def SetRotationAxisOfAbsoluteCyndricalCSYS(self, axis: CAE.Post.AxisymetricAxis) -> None:
        ...
    def GetRotationAxisOfAbsoluteCyndricalCSYS(self) -> CAE.Post.AxisymetricAxis:
        ...
    def SetBeamResultsInLocalCoordinateSystem(self, local: bool) -> None:
        ...
    def GetBeamResultsInLocalCoordinateSystem(self) -> bool:
        ...
    def MakeElementResult(self, elementResult: bool) -> None:
        ...
    def IsForcedElementResult(self) -> bool:
        ...
    def GetElementValueCriterion(self) -> CAE.Result.ElementValueCriterion:
        ...
    def SetElementValueCriterion(self, criteria: CAE.Result.ElementValueCriterion) -> None:
        ...
    def InitAveragingCriteria(self) -> CAE.Result.Averaging:
        ...
    def GetAveragingCriteria(self) -> CAE.Result.Averaging:
        ...
    def SetAveragingCriteria(self, average: CAE.Result.Averaging) -> None:
        ...
    def SetComputationType(self, computeType: CAE.Result.ComputationType) -> None:
        ...
    def GetComputationType(self) -> CAE.Result.ComputationType:
        ...
    def SetExcludeElementsNotVisible(self, excludeElements: bool) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultParameters.SetComputeOnVisible instead.")"""
        ...
    def GetExcludeElementsNotVisible(self) -> bool:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultParameters.GetComputeOnVisible instead.")"""
        ...
    def GetComplexCriterion(self) -> CAE.Result.Complex:
        ...
    def SetComplexCriterion(self, complex: CAE.Result.Complex) -> None:
        ...
    def GetPhaseAngle(self) -> float:
        ...
    def SetPhaseAngle(self, angle: float) -> None:
        ...
    def AskSectionPlyLayer(self, section: int, ply: int) -> int:
        ...
    def SetSectionPlyLayer(self, section: int, ply: int, layer: int) -> None:
        ...
    def GetScale(self) -> float:
        ...
    def SetScale(self, scale: float) -> None:
        ...
    def GetUnit(self) -> Unit:
        ...
    def SetUnit(self, unit: Unit) -> None:
        ...
    def SetAbsoluteValue(self, absolute: bool) -> None:
        ...
    def GetAbsoluteValue(self) -> bool:
        ...
    def SetCalculateBeamStrResults(self, calcBeamStrResults: bool) -> None:
        ...
    def GetCalculateBeamStrResults(self) -> bool:
        ...
    def SetBeamFillets(self, beamFillets: bool) -> None:
        ...
    def GetBeamFillets(self) -> bool:
        ...
    def SetBeamFilletRadius(self, beamFilletRadius: float) -> None:
        ...
    def GetBeamFilletRadius(self) -> float:
        ...
    def DisplayMidnodeValue(self, display: bool) -> None:
        """[Obsolete("Deprecated in NX1984.0.0.  Use NXOpen.CAE.ResultParameters.SetIncludeMidNode instead.")"""
        ...
    def IsMidnodeValueDisplayed(self) -> bool:
        """[Obsolete("Deprecated in NX1984.0.0.  Use NXOpen.CAE.ResultParameters.GetIncludeMidNode instead.")"""
        ...
    def SetTensorComponentAbsoluteValue(self, absolute: CAE.Result.TensorDerivedAbsolute) -> None:
        ...
    def GetTensorComponentAbsoluteValue(self) -> CAE.Result.TensorDerivedAbsolute:
        ...
    def GetIsReferenceNode(self) -> bool:
        ...
    def SetIsReferenceNode(self, isReferenceNode: bool) -> None:
        ...
    def GetReferenceNodeLabel(self) -> int:
        """[Obsolete("Deprecated in NX1872.0.0.  use NXOpen.CAE.ResultParameters.GetReferenceNode")"""
        ...
    def SetReferenceNodeLabel(self, referenceNodeLabel: int) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  use NXOpen.CAE.ResultParameters.SetReferenceNode")"""
        ...
    def GetDbSettings(self) -> CAE.SignalProcessingDBSettings:
        ...
    def GetDiscontinuityMethod(self) -> CAE.Result.DiscontinuityMethod:
        ...
    def SetDiscontinuityMethod(self, discontinuity: CAE.Result.DiscontinuityMethod) -> None:
        ...
    def GetConvertedDBref(self) -> float:
        ...
    def SetComputeOnVisible(self, excludeElements: bool) -> None:
        ...
    def GetComputeOnVisible(self) -> bool:
        ...
    def SetShellResultsInProjectedCoordinateSystem(self, projected: bool) -> None:
        ...
    def GetShellResultsInProjectedCoordinateSystem(self) -> bool:
        ...
    def SetPlyID(self, plyId: int) -> None:
        ...
    def SetPlyLocation(self, plyLocation: CAE.Result.PlyLocation) -> None:
        ...
    def GetPlyID(self) -> int:
        ...
    def GetPlyLocation(self) -> CAE.Result.PlyLocation:
        ...
    def GetShellSection(self) -> CAE.Result.ShellSection:
        ...
    def SetShellSection(self, section: CAE.Result.ShellSection) -> None:
        ...
    def GetBeamSection(self) -> CAE.Result.BeamSection:
        ...
    def SetBeamSection(self, section: CAE.Result.BeamSection) -> None:
        ...
    def SetSpectrumScaling(self, scaling: CAE.SignalProcessingPlotData.ScalingType) -> None:
        ...
    def GetSpectrumScaling(self) -> CAE.SignalProcessingPlotData.ScalingType:
        ...
    def SetAcousticWeighting(self, weighting: CAE.SignalProcessingPlotData.AcousticalWeighting) -> None:
        ...
    def GetAcousticWeighting(self) -> CAE.SignalProcessingPlotData.AcousticalWeighting:
        ...
    def GetReferenceNode(self) -> CAE.PostSelectionEntity:
        ...
    def SetReferenceNode(self, referenceNode: CAE.PostSelectionEntity) -> None:
        ...
    def IsProjectOnNodeNormal(self) -> bool:
        ...
    def SetProjectOnNodeNormal(self, projectOnNodeNormal: bool) -> None:
        ...
    def GetEntitiesToLoad(self) -> typing.List[CAE.PostSelectionEntity]:
        ...
    def SetEntitiesToLoad(self, loadEntities: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    def SetCyclicSymmParameters(self, cycParams: typing.List[CAE.CyclicSymmetricParameters]) -> None:
        ...
    def GetCyclicSymmParameters(self, cycParams: typing.List[CAE.CyclicSymmetricParameters]) -> None:
        ...
    def SetIncludeMidNode(self, includeMidNode: bool) -> None:
        ...
    def GetIncludeMidNode(self) -> bool:
        ...


class ResultMeasureResultSectionOptions(CAE.ResultMeasureResultOptions):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetBeamSection(self, eBeamSect: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultMeasureResultSectionOptions.SetResultBeamSection instead")"""
        ...
    def SetShellSection(self, eShellSect: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultMeasureResultSectionOptions.SetResultShellSection instead")"""
        ...
    def SetResultBeamSection(self, eBeamSect: CAE.Result.BeamSection) -> None:
        ...
    def SetResultShellSection(self, eShellSect: CAE.Result.ShellSection) -> None:
        ...


class ResultMeasureResultOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetUnit(self, tUnit: Unit) -> None:
        ...
    def SetAbsoluteValue(self, bAbsValue: bool) -> None:
        ...
    def SetOperation(self, eOperation: CAE.ResultMeasure.Operation) -> None:
        ...
    def SetPlynum(self, plynum: int) -> None:
        ...
    def SetPlylocation(self, plylocation: int) -> None:
        ...


class ResultMeasureResultDirectionSectionOptions(CAE.ResultMeasureResultOptions):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetCoordinateSystem(self, eCsys: CAE.Result.CoordinateSystem) -> None:
        ...
    def SetBeamSection(self, eBeamSect: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultMeasureResultDirectionSectionOptions.SetResultBeamSection instead")"""
        ...
    def SetShellSection(self, eShellSect: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultMeasureResultDirectionSectionOptions.SetResultShellSection instead")"""
        ...
    def SetResultBeamSection(self, eBeamSect: CAE.Result.BeamSection) -> None:
        ...
    def SetResultShellSection(self, eShellSect: CAE.Result.ShellSection) -> None:
        ...


class ResultMeasureResultDirectionOptions(CAE.ResultMeasureResultOptions):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetCoordinateSystem(self, eCsys: CAE.Result.CoordinateSystem) -> None:
        ...


class ResultMeasureResultAllOptions(CAE.ResultMeasureResultOptions):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetCoordinateSystem(self, eCsys: CAE.Result.CoordinateSystem) -> None:
        ...
    def SetShellSection(self, eShellSect: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultMeasureResultAllOptions.SetResultShellSection instead")"""
        ...
    def SetBeamSection(self, eBeamSect: CAE.Result.Section) -> None:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultMeasureResultAllOptions.SetResultBeamSection instead")"""
        ...
    def SetResultShellSection(self, eShellSect: CAE.Result.ShellSection) -> None:
        ...
    def SetResultBeamSection(self, eBeamSect: CAE.Result.BeamSection) -> None:
        ...
    def SetCalculateBeamResults(self, bCalcBeamResults: bool) -> None:
        ...
    def SetAddBeamFillets(self, bAddBeamFillets: bool) -> None:
        ...
    def SetBeamFilletRadius(self, beamFilletRadius: float) -> None:
        ...


class ResultMeasureModelSubsetGeom(CAE.ResultMeasureModelSubset):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetEntities(self, entities: typing.List[DisplayableObject]) -> None:
        ...


class ResultMeasureModelSubsetFE(CAE.ResultMeasureModelSubset):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetElements(self, elements: typing.List[CAE.FEElement]) -> None:
        ...
    def SetNodes(self, elements: typing.List[CAE.FENode]) -> None:
        ...


class ResultMeasureModelSubset(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class ResultMeasureCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ResultMeasure]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateResultMeasure(self, tSol: CAE.SimSolution, iStepIndex: int, iIterIndex: int, pType: CAE.Result.Type, eComp: CAE.Result.Component, expName: str) -> CAE.ResultMeasure:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.ResultMeasureCollection.CreateResultMeasureNew instead.")"""
        ...
    def Find(self, journalIdentifier: str) -> CAE.ResultMeasure:
        ...
    def UpdateMeasures(self, objects: typing.List[CAE.ResultMeasure]) -> None:
        ...
    def DeleteMeasures(self, objects: typing.List[CAE.ResultMeasure]) -> None:
        ...
    def CreateResultOptions(self, tSol: CAE.SimSolution, iStepIndex: int, iIterIndex: int, pType: CAE.Result.Type, eComp: CAE.Result.Component) -> CAE.ResultMeasureResultOptions:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:CreateResultMeasureNew instead.")"""
        ...
    def CreateResultOptionsNew(self, tSol: CAE.SimSolution, tResultReference: CAE.SimResultReference, iStepIndex: int, iIterIndex: int, pType: CAE.Result.Type, eComp: CAE.Result.Component) -> CAE.ResultMeasureResultOptions:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.Iteration:CreateNewResultOptions instead.")"""
        ...
    def CreateModelSubset(self, eSubset: CAE.ResultMeasure.SubsetSelection) -> CAE.ResultMeasureModelSubset:
        ...
    def CreateResultMeasureNew(self, pResOpt: CAE.ResultMeasureResultOptions, pSubset: CAE.ResultMeasureModelSubset, expName: str) -> CAE.ResultMeasure:
        ...
    def CreateNewResultOptions(self, tSol: CAE.SimSolution, tResultReference: CAE.SimResultReference, tResultLoadcase: CAE.Loadcase, tResultIteration: CAE.Iteration, bAllSubiterations: bool, tResultSubIteration: CAE.Iteration, pType: CAE.Result.Type, eComp: CAE.Result.Component) -> CAE.ResultMeasureResultOptions:
        ...
    def CreateNewResultOptions(self, tSol: CAE.SimSolution, tResultReference: CAE.SimResultReference, tResultLoadcase: CAE.Loadcase, tResultIteration: CAE.Iteration, bAllSubiterations: bool, tResultSubIteration: CAE.Iteration, pType: CAE.Result.Type, eComp: CAE.Result.Component, resultUserName: str) -> CAE.ResultMeasureResultOptions:
        ...
    def Tag(self) -> Tag: ...



class ResultMeasure(TaggedObject):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    Result: float


    class SubsetSelection(enum.Enum):
        None = 0
        Geometry = 1
        FiniteElement = 2
    

    class Operation(enum.Enum):
        Minimum = 0
        Maximum = 1
        MeanAverage = 2
    

class ResultManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def OpenImportedResult(self, filename: str, resultname: str, unitsystem: CAE.Result.ResultBasicUnit) -> CAE.ImportedResult:
        ...
    def CreateImportedResult(self, filename: str, unitsystem: CAE.Result.ResultBasicUnit) -> CAE.ImportedResult:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.ResultManager.CreateResultFromImportParameters")"""
        ...
    def CreateImportedResult(self, filename: str, resultname: str, unitsystem: CAE.Result.ResultBasicUnit) -> CAE.ImportedResult:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.ResultManager.CreateResultFromImportParameters")"""
        ...
    def CreateImportedResult(self, filename: str, resultname: str) -> CAE.ImportedResult:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.ResultManager.CreateResultFromImportParameters")"""
        ...
    def CreateResultFromImportParameters(self, parameters: CAE.ImportResultParameters) -> CAE.ImportedResult:
        ...
    def CreateSolutionResult(self, solution: CAE.SimSolution) -> CAE.SolutionResult:
        ...
    def CreateReferenceResult(self, solution: CAE.SimResultReference) -> CAE.SolutionResult:
        ...
    def CreateSeResult(self, parentResult: CAE.Result, seid: int) -> CAE.Result:
        ...
    def CreateResponseSolutionResult(self, responseSolution: CAE.ResponseSimulation.Solution) -> CAE.SolutionResult:
        ...
    def CreateResponseEventResult(self, responseSolution: CAE.ResponseSimulation.RSEvent) -> CAE.SolutionResult:
        ...
    def CreateDurabilityEventResult(self, durablityEvent: CAE.DurabilityEvent) -> CAE.SolutionResult:
        ...
    def CreateTbsOptimizationSolutionResult(self, tbsOptimizationSolution: CAE.Optimization.TBSOptimizationSolution) -> CAE.SolutionResult:
        ...
    def CreateDaoOptimizationSolutionResult(self, daoOptimizationSolution: CAE.Optimization.DAOSolution) -> CAE.SolutionResult:
        ...
    def CreateLaminateDynamicEventResult(self, dynEvent: CAE.LaminateDynamicEvent) -> CAE.SolutionResult:
        ...
    def CreateLaminateGraphicalReportResult(self, lamGraphReport: CAE.LaminateGraphicalReport) -> CAE.SolutionResult:
        ...
    def CreateResultParameters(self) -> CAE.ResultParameters:
        ...
    def CreateCrossSectionParameters(self) -> CAE.CrossSectionParameters:
        ...
    def CreateResultParametersWithProbe(self, resultProbe: CAE.ResultProbe) -> CAE.ResultParametersWithProbe:
        ...
    def CreateTableFieldFromProbe(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], resultProbe: CAE.ResultProbe, createTableOfFields: bool) -> Fields.Field:
        ...
    def CreateResultAccess(self, result: CAE.Result, parameters: CAE.ResultParameters) -> CAE.ResultAccess:
        ...
    def CreateResultAccess(self, postViewID: int) -> CAE.ResultAccess:
        ...
    def CreateCyclicSymmetricParameters(self) -> CAE.CyclicSymmetricParameters:
        ...
    def CreateAxiSymmetricParameters(self) -> CAE.AxiSymmetricParameters:
        ...
    def DeleteResult(self, result: CAE.Result) -> None:
        ...
    def DeleteResultAccess(self, result: CAE.ResultAccess) -> None:
        ...
    def DeleteResultParameters(self, result: CAE.ResultParameters) -> None:
        ...
    def DeleteCrossSectionParameters(self, crossSection: CAE.CrossSectionParameters) -> None:
        ...
    def DeleteResultParametersWithProbe(self, result: CAE.ResultParametersWithProbe) -> None:
        ...
    def DeleteCyclicSymmetricParameters(self, cyclicSymmetricParameter: CAE.CyclicSymmetricParameters) -> None:
        ...
    def DeleteAxiSymmetricParameters(self, axiSymmetricParameter: CAE.AxiSymmetricParameters) -> None:
        ...
    def ConvertOdbFile(self, inputFileName: str, outputFileName: str) -> None:
        ...
    def CreateDeformationParameters(self) -> CAE.DeformationParameters:
        ...
    def DeleteDeformationParameters(self, result: CAE.DeformationParameters) -> None:
        ...
    def CreateFreeBodyResultsBuilder(self) -> CAE.FreeBodyResultsBuilder:
        ...
    def DeleteFreeBodyResultsBuilder(self, builder: CAE.FreeBodyResultsBuilder) -> None:
        ...
    def CreateResultsCombinationBuilder(self) -> CAE.ResultsCombinationBuilder:
        ...
    def CreateResultsEnvelopeBuilder(self) -> CAE.ResultsEnvelopeBuilder:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.ResultManager.CreateResultsManipulationEnvelopeBuilder")"""
        ...
    def CreateResultsReductionBuilder(self) -> CAE.ResultsReductionBuilder:
        ...
    def CreateTransientResultsReductionBuilder(self) -> CAE.TransientResultsReductionBuilder:
        ...
    def CreateExtractingResultsToCsvBuilder(self) -> CAE.ExtractingResultsToCsvBuilder:
        ...
    def CreateExtractingResultsToScd5Builder(self) -> CAE.ExtractingResultsToScd5Builder:
        ...
    def FindObject(self, journalIdentifier: str) -> TaggedObject:
        ...
    def CreateClippingParameters(self) -> CAE.ClippingParameters:
        ...
    def DeleteClippingParameters(self, result: CAE.ClippingParameters) -> None:
        ...
    def CreatePostCoordinatesystem(self, result: CAE.Result, source: CAE.Result.CoordinateSystemSource, selectedcsysid: int) -> CAE.PostCoordinateSystem:
        ...
    def CreatePostCoordinatesystem(self, orientation: Matrix3x3, origin: Point3d, csysType: CAE.PostCoordinateSystem.CoordinateSystemType) -> CAE.PostCoordinateSystem:
        ...
    def CreatePostCoordinatesystemFromGlobal(self, csysType: CAE.PostCoordinateSystem.CoordinateSystemType) -> CAE.PostCoordinateSystem:
        ...
    def DeletePostCoordinatesystem(self, result: CAE.PostCoordinateSystem) -> None:
        ...
    def CreateJtBuilder(self) -> CAE.CreateJtBuilder:
        ...
    def CreatePostJtBuilder(self) -> CAE.PostJtExportBuilder:
        ...
    def DeletePostJtBuilder(self, builder: CAE.PostJtExportBuilder) -> None:
        ...
    def CreateResultsModelExportBuilder(self) -> CAE.ResultsModelExportBuilder:
        ...
    def CreateGraphAcrossIterationsBuilder(self, pvid: int) -> CAE.PostGraphAcrossIterationsBuilder:
        ...
    def CreateGraphAcrossIterationsBuilder(self, firstpvid: int, secondpvid: int) -> CAE.PostGraphAcrossIterationsBuilder:
        ...
    def CreateGraphAcrossIterationsBuilder(self, result: CAE.Result, parameter: CAE.ResultParameters) -> CAE.PostGraphAcrossIterationsBuilder:
        ...
    def CreateGraphAcrossIterationsBuilder(self, parameter: CAE.ResultProbe) -> CAE.PostGraphAcrossIterationsBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.ResultManager.CreateGraphFromResultProbesBuilder instead.")"""
        ...
    def CreateGraphFromResultProbesBuilder(self) -> CAE.GraphFromResultProbeBuilder:
        ...
    def CreateGraphAcrossIterationsBuilder(self, result: CAE.Result, parameter1: CAE.ResultParameters, parameter2: CAE.ResultParameters) -> CAE.PostGraphAcrossIterationsBuilder:
        ...
    def CreateGraphAcrossIterationsBuilder(self, result: CAE.Result, parameters: typing.List[CAE.ResultParameters], names: str, formula: str) -> CAE.PostGraphAcrossIterationsBuilder:
        ...
    def CreateGraphAlongPathBuilder(self, pvid: int) -> CAE.PostGraphAlongPathBuilder:
        ...
    def CreateGraphAlongPathBuilder(self, firstpvid: int, secondpvid: int) -> CAE.PostGraphAlongPathBuilder:
        ...
    def CreateGraphAlongPathBuilder(self, result: CAE.Result, parameter: CAE.ResultParameters) -> CAE.PostGraphAlongPathBuilder:
        ...
    def CreateGraphAlongPathBuilder(self, parameter: CAE.ResultProbe) -> CAE.PostGraphAlongPathBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.ResultManager.CreateGraphFromResultProbesBuilder instead.")"""
        ...
    def CreateGraphAlongPathBuilder(self, result: CAE.Result, parameter1: CAE.ResultParameters, parameter2: CAE.ResultParameters) -> CAE.PostGraphAlongPathBuilder:
        ...
    def CreateGraphOrbitBuilder(self, pvid: int) -> CAE.PostGraphOrbitBuilder:
        ...
    def CreateGraphOrbitBuilder(self, result: CAE.Result, parameter: CAE.ResultParameters) -> CAE.PostGraphOrbitBuilder:
        ...
    def CreateResultAccessReferenceField(self, fieldManager: Fields.FieldManager, result: CAE.Result, parameters: CAE.ResultParameters, depDomainName: str, fieldName: str) -> Fields.FieldReference:
        ...
    def CreateResultAccessReferenceField(self, fieldManager: Fields.FieldManager, result: CAE.Result, parameters: CAE.ResultParameters, indepDomainName: str, depDomainName: str, fieldName: str) -> Fields.FieldReference:
        ...
    def CreateIdResultAccessReferenceField(self, fieldManager: Fields.FieldManager, result: CAE.Result, parameters: CAE.ResultParameters, depDomainName: str, fieldName: str) -> Fields.FieldReference:
        ...
    def Create4dResultAccessReferenceField(self, fieldManager: Fields.FieldManager, result: CAE.Result, parameters: CAE.ResultParameters, indepDomainName: str, depDomainName: str, fieldName: str) -> Fields.FieldReference:
        ...
    def CreateResultvariable(self, sim: CAE.SimSimulation, quan: CAE.Result.Quantity, loc: CAE.Result.Location, comp: CAE.Result.Component, restypename: str, name: str) -> CAE.ResultVariable:
        ...
    def Create3dGraphBuilder(self, parameter: CAE.ResultProbe) -> CAE.Post3DGraphBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.ResultManager.CreateGraphFromResultProbesBuilder instead.")"""
        ...
    def ExportUnvFromProbe(self, fileName: str, probeArray: typing.List[CAE.ResultProbe]) -> None:
        ...
    def CreateQueryCurvePost(self, result: CAE.Result, name: str, entities: typing.List[CAE.QueryCurvePost.Entity], numInsertPointsPerSegment: int) -> CAE.QueryCurvePost:
        ...
    def DeleteQueryCurve(self, queryCurvePost: CAE.QueryCurvePost) -> None:
        ...
    def ConstructSubmodelForResultAccessReferenceField(self, refField: Fields.FieldReference, fieldManager: Fields.FieldManager, result: CAE.Result, elem: int, includeOrExculde: bool) -> None:
        ...
    def CreateTableFieldForModel(self, fieldName: str, indepDomainType: int, depDomainType: int, nodevalshare: int, pvid: int, isdeform: bool, elem: int, includeOrExculde: bool) -> Fields.FieldTable:
        """[Obsolete("Deprecated in NX1926.0.0.  Use new version of NXOpen.CAE.ResultManager.JA_RESULT_MANAGER_create_table_field_for_model instead.")"""
        ...
    def CreateTableOfFieldsForModel(self, fieldName: str, indepDomainType: int, depDomainType: int, nodevalshare: int, pvid: int, isdeform: bool, elem: int, node: int, includeOrExculde: bool, primValues: float, lcases: int, iters: int, subiters: int) -> Fields.FieldLinksTable:
        """[Obsolete("Deprecated in NX1926.0.0.  Use new version of NXOpen.CAE.ResultManager.JA_RESULT_MANAGER_create_table_of_fields_for_model instead.")"""
        ...
    def GetIterationsWithLimits(self, resid: int, lcase: int, iteration: int, superiter: int, minLimit: int, maxLimit: int, primValues: float, lcases: int, iters: int, subiters: int) -> None:
        ...
    def Create4dResultAccessReferenceFieldWithLimits(self, fieldManager: Fields.FieldManager, result: CAE.Result, parameters: CAE.ResultParameters, indepDomainName: str, depDomainName: str, fieldName: str, minLimit: int, maxLimit: int) -> Fields.FieldReference:
        ...
    def CreateTableFieldFromNodalForceReport(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], nodalForceReport: CAE.NodalForceReport) -> Fields.Field:
        ...
    def ExportNodalForceReportToFieldFile(self, nodalForceReport: CAE.NodalForceReport, fileName: str, indepVarArray: typing.List[Fields.FieldVariable], exportForceField: bool, exportMomemtField: bool) -> None:
        ...
    def CreateResultParametersWithNodalForceReport(self, nodalForceReport: CAE.NodalForceReport) -> CAE.ResultParametersWithNodalForceReport:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.ResultManager.CreateResultParametersWithNodalForceReports")"""
        ...
    def CreateResultParametersWithNodalForceReports(self, freebodyList: typing.List[CAE.NodalForceReport]) -> CAE.ResultParametersWithNodalForceReport:
        ...
    def DeleteResultParametersWithNodalForceReport(self, result: CAE.ResultParametersWithNodalForceReport) -> None:
        ...
    def CreatePostSelectionEntity(self) -> CAE.PostSelectionEntity:
        ...
    def CreateResultCacheRecipeBuilder(self, iresult: CAE.Result) -> CAE.CacheResultRecipeBuilder:
        ...
    def ExportProbesToFieldFile(self, probes: typing.List[CAE.ResultProbe], filename: str) -> None:
        ...
    def CreateDurabilityMetaSolutionResult(self, durMetaSol: CAE.DurabilityMetaSolution) -> CAE.SolutionResult:
        ...
    def CreateHotspotRecipeBuilder(self, part: CAE.SimSimulation, recipe: CAE.HotspotRecipe) -> CAE.HotspotRecipeBuilder:
        ...
    def CreateDbSettings(self) -> CAE.SignalProcessingDBSettings:
        ...
    def DeleteDbSettings(self, dBSettings: CAE.SignalProcessingDBSettings) -> None:
        ...
    def CreateResultsManipulationEnvelopeBuilder(self) -> CAE.ResultsManipulationEnvelopeBuilder:
        ...
    def CreateTableOfFieldsForModel(self, fieldName: str, primIndepVarArray: typing.List[Fields.FieldVariable], secondIndepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], nodevalshare: CAE.ResultsManipulationBuilder.ElementValueAtNode, pvid: int, isdeform: bool, elem: int, node: int, includeOrExculde: bool, primValues: float, lcases: int, iters: int, subiters: int, duplicateValueOption: Fields.FieldTable.DuplicateValueOption) -> Fields.FieldLinksTable:
        ...
    def CreateTableFieldForModel(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], nodevalshare: CAE.ResultsManipulationBuilder.ElementValueAtNode, pvid: int, isdeform: bool, elem: int, node: int, includeOrExculde: bool, duplicateValueOption: Fields.FieldTable.DuplicateValueOption) -> Fields.FieldTable:
        ...
    def CreateImportResultParameters(self) -> CAE.ImportResultParameters:
        ...
    def CreateResultUnitSystem(self, part: BasePart) -> CAE.ResultUnitSystem:
        ...
    def CreateScd5Converter(self) -> CAE.ResultToSCD5Converter:
        ...
    def CreateGeometryQueryHelper(self, result: CAE.Result) -> CAE.GeometryQueryHelper:
        """[Obsolete("Deprecated in NX1953.0.0.  This functionality is no longer needed.")"""
        ...
    def CreateResultParametersMultiValue(self) -> CAE.ResultParametersMultiValue:
        ...
    def DeleteImportResultParameters(self, importResultParameters: CAE.ImportResultParameters) -> None:
        ...
    def DeleteResultUnitSystem(self, resultUnitSystem: CAE.ResultUnitSystem) -> None:
        ...
    def Tag(self) -> Tag: ...



class ResultAccess(TaggedObject):
    def __init__(self) -> None: ...
    def GetResult(self) -> CAE.Result:
        ...
    def GetParameters(self) -> CAE.ResultParameters:
        ...
    def SetParameters(self, resultParameters: CAE.ResultParameters) -> None:
        ...
    def AskMinimum(self) -> float:
        ...
    def AskMaximum(self) -> float:
        ...
    def AskNMinMaxLocation(self, numExtreme: int, location: CAE.Result.Location, min: float, max: float, minID: int, minSubID: int, maxID: int, maxSubID: int) -> None:
        ...
    def AskMinMaxLocation(self, location: CAE.Result.Location, min: float, max: float, minID: int, maxID: int, minSubID: int, maxSubID: int) -> None:
        ...
    def IsResultDefined(self, indices: int) -> bool:
        ...
    def IsResultDefined(self, entityIndices: int, subentityIndices: int) -> bool:
        ...
    def AskNodalResult(self, nodeIndex: int) -> float:
        ...
    def AskNodalResult(self, nodeIndices: int) -> float:
        ...
    def AskNodalResultAllComponents(self, nodeIndex: int, value: float) -> None:
        ...
    def AskElementResult(self, elementIndex: int) -> float:
        ...
    def AskElementResult(self, elementIndices: int) -> float:
        ...
    def AskElementResultAllComponents(self, elementIndex: int, value: float) -> None:
        ...
    def AskElementNodalResult(self, elementIndex: int, nodeLabels: int, value: float) -> None:
        ...
    def AskElementNodalResultAllComponents(self, elementIndex: int, nodeIndex: int, numComponents: int, value: float) -> None:
        ...
    def AskResultAtLocation(self, location: Point3d) -> float:
        ...
    def AskResultAtLocationAllComponents(self, position: Point3d, value: float) -> None:
        ...
    def AskCurrentResultDataType(self) -> CAE.Result.DataType:
        ...
    def AskResultComponents(self, components: typing.List[CAE.Result.Component]) -> str:
        ...
    def IsFullyAveraged(self) -> bool:
        ...
    def AskElementFaceResult(self, elementIndex: int, faceIndex: int) -> float:
        ...
    def AskElementEdgeResult(self, elementIndex: int, edgeIndex: int) -> float:
        ...
    def AskElementFaceNodalResult(self, elementIndex: int, faceIndex: int, nodeIndex: int) -> float:
        ...
    def AskElementEdgeNodalResult(self, elementIndex: int, edgeIndex: int, nodeIndex: int) -> float:
        ...
    def AskElementFaceResultAllComponents(self, elementIndex: int, faceIndex: int, value: float) -> None:
        ...
    def AskElementEdgeResultAllComponents(self, elementIndex: int, edgeIndex: int, value: float) -> None:
        ...
    def AskElementFaceNodalResultAllComponents(self, elementIndex: int, faceIndex: int, nodeIndex: int, value: float) -> None:
        ...
    def AskElementEdgeNodalResultAllComponents(self, elementIndex: int, edgeIndex: int, nodeIndex: int, value: float) -> None:
        ...
    def AskElementNodalResult(self, elementIndex: int, nodeIndex: int) -> float:
        ...
    def AskElementNodalResultAllComponents(self, elementIndex: int, nodeIndex: int, value: float) -> None:
        ...
    def AskResultLocation(self) -> CAE.Result.Location:
        ...
    def AskElementPlyIds(self, elementIndex: int, plyIDs: int) -> None:
        ...
    def SetGeometryQueryHelper(self, geometryqueryhelper: CAE.GeometryQueryHelper) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  This functionality is no longer needed.")"""
        ...
    def AskResultAtLocationsAllComponents(self, position: typing.List[Point3d], components: typing.List[CAE.Result.Component], value: float, returnCode: int) -> None:
        ...
    def AskResultAtLocationInElementAllComponents(self, pointInterpolationData: CAE.PointInterpolationData, components: typing.List[CAE.Result.Component], value: float) -> None:
        ...
    def AskResultAtLocationsInElementAllComponents(self, pointInterpolationData: typing.List[CAE.PointInterpolationData], components: typing.List[CAE.Result.Component], value: float, returnCode: int) -> None:
        ...


class Result(NXObject):
    def __init__(self) -> None: ...
    def AskNumLoadcases(self) -> int:
        ...
    def AskLoadcases(self) -> str:
        ...
    def AskNumIterations(self, loadcaseIndex: int) -> int:
        ...
    def AskIterations(self, loadcaseIndex: int) -> str:
        ...
    def AskNumNodes(self) -> int:
        ...
    def AskNumElements(self) -> int:
        ...
    def AskElementNodes(self, elementIndex: int, nodeIndex: int) -> None:
        ...
    def AskNodeCoordinates(self, nodeIndex: int) -> typing.List[Point3d]:
        ...
    def AskResultTypes(self, loadcaseIndex: int, iterationIndex: int, types: typing.List[CAE.Result.Type], description: str) -> None:
        ...
    def AskNumGroupsInContainer(self, type: CAE.Result.GroupContainer) -> int:
        ...
    def AskNumElementsOfGroup(self, type: CAE.Result.GroupContainer, groupIndex: int, elementIndex: int) -> None:
        ...
    def AskNodeIndex(self, nodeLabel: int) -> int:
        ...
    def AskElementIndex(self, elementLabel: int) -> int:
        ...
    def AskNodeLabel(self, nodeIndex: int) -> int:
        ...
    def AskElementLabel(self, elementIndex: int) -> int:
        ...
    def AskResultSections(self, loadcaseIndex: int, iterationIndex: int, resultType: CAE.Result.Type, sectionNums: int) -> None:
        ...
    def AskSectionDescription(self, sect: CAE.Result.Section) -> str:
        ...
    def AskResultLoadcaseValue(self, loadcaseIndex: int, description: str, value: float) -> CAE.Result.LoadcaseValueType:
        ...
    def AskElementShape(self, elementIndex: int) -> CAE.ElementTypes.Shape:
        ...
    def AskResultDataType(self, loadcaseIndex: int, iterationIndex: int, resultType: CAE.Result.Type) -> CAE.Result.DataType:
        ...
    def IsResultTypeComplex(self, loadcaseIndex: int, iterationIndex: int, resultType: CAE.Result.Type) -> bool:
        ...
    def GetLoadcases(self) -> typing.List[CAE.BaseLoadcase]:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def GetResultCoordinateSystems(self) -> int:
        ...
    def GetResultCoordinateSystemDefinition(self, id: int, type: CAE.Result.CoordinateSystem, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def AskNumberOfSectors(self) -> int:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CAE.Result.GetCyclicSymmetricStages instead, And use that object for the query.")"""
        ...
    def AskNumFacesOnElement(self, elementIndex: int) -> int:
        ...
    def AskNumEdgesOnElement(self, elementIndex: int) -> int:
        ...
    def AskNodeIndicesOnElementFace(self, elementIndex: int, faceIndex: int, nodeIndices: int) -> None:
        ...
    def AskNodeIndicesOnElementEdge(self, elementIndex: int, edgeIndex: int, nodeIndices: int) -> None:
        ...
    def GetMeshes(self, meshes: typing.List[CAE.PostMesh]) -> None:
        ...
    def GetMeshesOfGivenDimension(self, dimension: int, meshes: typing.List[CAE.PostMesh]) -> None:
        ...
    def AskAllPliesInModel(self, plyIDs: int) -> None:
        ...
    def GetCacheResultRecipeManager(self) -> CAE.CacheResultRecipeManager:
        ...
    def GetEnvironmentDefinition(self) -> CAE.PostEnvironmentsManager.DefinitionType:
        ...
    def SetEnvironmentDefinition(self, definition: CAE.PostEnvironmentsManager.DefinitionType) -> None:
        ...
    def GetEnvironmentType(self) -> CAE.PostEnvironmentsManager.PostEnvironment:
        ...
    def SetEnvironmentType(self, environmentType: CAE.PostEnvironmentsManager.PostEnvironment) -> None:
        ...
    def GetPostMeshCollector(self) -> CAE.PostMeshCollector:
        ...
    def GetCyclicSymmetricStages(self, stages: typing.List[CAE.CyclicSymmetricStageProperties]) -> None:
        ...
    def GetPostMeshCollectorFromMeshfid(self, meshfid: int) -> CAE.PostMeshCollector:
        ...
    def AskUserGroups(self) -> str:
        ...
    def AskElementAtLocations(self, locations: typing.List[Point3d], inputElements: int) -> typing.List[CAE.PointInterpolationData]:
        ...


    class ResultVelocityParameters():
        LoadCaseIndex: int
        IterationIndex: int
        Type: CAE.Result.Type
        def ToString(self) -> str:
            ...
        def __init__(self, LoadCaseIndex: int, IterationIndex: int, Type: CAE.Result.Type) -> None: ...
    

    class ResultType():
        Quantity: CAE.Result.Quantity
        Location: CAE.Result.Location
        Section: CAE.Result.Section
        def ToString(self) -> str:
            ...
        def __init__(self, Quantity: CAE.Result.Quantity, Location: CAE.Result.Location, Section: CAE.Result.Section) -> None: ...
    

    class TensorDerivedAbsolute(enum.Enum):
        AllComponents = 0
        DerivedComponent = 1
    

    class SuperElementRep(enum.Enum):
        Symbolic = 1
        Simplified = 2
        ThreeDim = 3
    

    class SolutionType(enum.Enum):
        Unknown = 0
        Static = 1
        Vibration = 2
        Buckling = 3
        Transient = 4
        Freqresponse = 5
        Complexeigen = 6
        Quasistatic = 7
    

    class ShellSection(enum.Enum):
        NotApplicable = 0
        Top = 1
        Bottom = 2
        Middle = 3
        Minimum = 4
        Maximum = 5
        Average = 6
        TopBot = 7
        Bending = 8
        AbsoluteMinimum = 9
        AbsoluteMaximum = 10
        TrueMinimum = 11
        TrueMaximum = 12
    

    class Section(enum.Enum):
        NotApplicable = 0
        Top = 1
        Middle = 2
        Bottom = 3
        Minimum = 4
        Maximum = 5
        StressRecoveryPointC = 6
        StressRecoveryPointD = 7
        StressRecoveryPointE = 8
        StressRecoveryPointF = 9
        All = 10
        Bending = 11
    

    class ResultResultSection():
        Beamsection: CAE.Result.Section
        Shellsection: CAE.Result.Section
        def ToString(self) -> str:
            ...
        def __init__(self, Beamsection: CAE.Result.Section, Shellsection: CAE.Result.Section) -> None: ...
    

    class ResultResultParameters():
        LoadCaseIndex: int
        IterationIndex: int
        Type: CAE.Result.Type
        Component: CAE.Result.Component
        ResSection: CAE.Result.ResultSection
        Section: int
        Plynumber: int
        Layer: int
        Averaging: CAE.Result.Averaging
        IncludeMidnode: bool
        CoordinateSystem: CAE.Result.CoordinateSystem
        DisplayBeamResultInLocalCsys: bool
        ElementValue: CAE.Result.ElementValue
        Complex: CAE.Result.Complex
        PhaseAngle: float
        AbsoluteValue: bool
        ScaleValue: float
        Unit: Unit
        CalculateBeamStrResults: bool
        AddBeamStrFillets: bool
        BeamFilletRadius: float
        def ToString(self) -> str:
            ...
    

    class ResultResultBasicUnit():
        MassUnit: Unit
        LengthUnit: Unit
        TimeUnit: Unit
        TemperatureUnit: Unit
        AngleUnit: Unit
        ThermalenergyUnit: Unit
        def ToString(self) -> str:
            ...
    

    class Quantity(enum.Enum):
        Displacement = 0
        Rotation = 1
        TranslationalDeformation = 2
        RotationalDeformation = 3
        ContactDisplacement = 4
        Velocity = 5
        AngularVelocity = 6
        Acceleration = 7
        AngularAcceleration = 8
        VonMisesStress = 9
        VonMisesStrain = 10
        Stress = 11
        Strain = 12
        StrainEnergy = 13
        StrainEnergyDensity = 14
        StrainEnergyError = 15
        EquivalentPlasticStrain = 16
        EquivalentCreepStrain = 17
        KineticEnergy = 18
        KineticEnergyDensity = 19
        KineticEnergyPercent = 20
        Thickness = 21
        Temperature = 22
        TemperatureGradient = 23
        HeatFlux = 24
        ThermalEnergy = 25
        HeatFlow = 26
        AppliedForce = 27
        AppliedMoment = 28
        ReactionForce = 29
        ReactionMoment = 30
        ReactionForceMPC = 31
        ReactionMomentMPC = 32
        ContactTraction = 33
        ContactForce = 34
        ElementForce = 35
        ElementMoment = 36
        ContactPressure = 37
        FatigueLife = 38
        FatigueDamage = 39
        FatigueSafetyFactor = 40
        StrengthSafetyFactor = 41
        ElementError = 42
        ElementResultants = 43
        ElementStrainResultants = 44
        MaximumTemperature = 45
        MinimumTemperature = 46
        TimeAtMaximumTemperature = 47
        TimeAtMinimumTemperature = 48
        ConductiveFlux = 49
        TotalHeatLoad = 50
        TotalHeatFlux = 51
        HeatResidual = 52
        ConvectionCoefficient = 53
        ViewFactorsSum = 54
        AdjustedVelocity = 55
        PressureOnPositiveSide = 56
        PressureOnNegativeSide = 57
        StaticPressure = 58
        TotalPressure = 59
        TurbulenceEnergy = 60
        TurbulenceDissipation = 61
        FluidDensity = 62
        ShearStressOnPositiveSide = 63
        ShearStressOnNegativeSide = 64
        RoughnessOnPositiveSide = 65
        RoughnessOnNegativeSide = 66
        YPlusOnPositiveSide = 67
        YPlusOnNegativeSide = 68
        MassFlux = 69
        FluidTemperature = 70
        ConvectiveFlux = 71
        LocalConvectionCoefficient = 72
        BulkConvectionCoefficient = 73
        Pressure = 74
        VelocityComponent = 75
        MassFlow = 76
        ElementHeatLoad = 77
        SafetyFactor = 78
        ShellResultants = 79
        BeamResultants = 80
        SpringDashpotResultant = 81
        ShellStrainResultants = 82
        BeamStrainResultants = 83
        SpringDashpotStrainResultant = 84
        PlyFailureIndex = 85
        BondFailureIndex = 86
        PlyStress = 87
        PlyStrain = 88
        BondSafetyMargin = 89
        PlySafetyMargin = 90
        TorsionStress = 91
        GridPointForce = 92
        GridPointMoment = 93
        RadiativeSourceHeatFlux = 94
        Radiance = 95
        ApparentTemperature = 96
        Fluence = 97
        RCProduct = 98
        Voltage = 99
        PowerDensity = 100
        RelativeVelocity = 101
        WaterCumulation = 102
        TurbulentSpecificDissipation = 103
        RadiativeHeatFlux = 104
        CollimatedHeatFlux = 105
        DiffuseHeatFlux = 106
        InfraredHeatFlux = 107
        ViewFactor = 108
        Unknown = 109
        MappedTemperature = 110
        MappedTemperatureGradient = 111
        RadiativeAbsorbedHeatFlux = 112
        RadiativeIncidentHeatFlux = 113
        RadiativeReflectedHeatFlux = 114
        RadiativeTransmittedHeatFlux = 115
        CollimatedAbsorbedHeatFlux = 116
        CollimatedIncidentHeatFlux = 117
        CollimatedReflectedHeatFlux = 118
        CollimatedTransmittedHeatFlux = 119
        DiffuseAbsorbedHeatFlux = 120
        DiffuseIncidentHeatFlux = 121
        DiffuseReflectedHeatFlux = 122
        DiffuseTransmittedHeatFlux = 123
        InfraredAbsorbedHeatFlux = 124
        InfraredIncidentHeatFlux = 125
        InfraredReflectedHeatFlux = 126
        InfraredTransmittedHeatFlux = 127
        AlbedoViewFactor = 128
        EarthViewFactor = 129
        SolarViewFactor = 130
        SpaceViewFactor = 131
        Quality = 132
        RadiationPatch = 133
        AbsorbedRadiation = 134
        IncidentRadiation = 135
        ReflectedRadiation = 136
        TransmittedRadiation = 137
        RefractiveIndex = 138
        RefractiveIndexGradient = 139
        OpticalPathLength = 140
        LaserPower = 141
        PumpingPower = 142
        RadiativeFluxinSolid = 143
        FluidScalar = 144
        WallDistance = 145
        RelativeHumidity = 146
        SpecificHumidity = 147
        MachNumber = 148
        PredictedPercentDissatisfied = 149
        PercentMeanVote = 150
        Vorticity = 151
        RelativePressure = 152
        AbsolutePressure = 153
        ElementAspectRatio = 154
        ElementDistortion = 155
        ElementTaper = 156
        ElementSize = 157
        ElementJacobian = 158
        ElementSkew = 159
        ElementStretch = 160
        ElementTwist = 161
        ElementWarp = 162
        FluidMesh = 163
        NetRadiativeLoad = 164
        NetRadiativeFlux = 165
        RadiosityLoad = 166
        RadiosityFlux = 167
        IrradianceLoad = 168
        IrradianceFlux = 169
        ParticleDensity = 170
        ParticleMassDensity = 171
        AcousticPowerDensity = 172
        ReynoldsNumber = 173
        BondStrengthRatio = 174
        PlyStrengthRatio = 175
        FailureIndex = 176
        ContactInitialSeparation = 177
        ContactFinalSeparation = 178
        GasketPressue = 179
        GasketClosure = 180
        GasketPlasticClosure = 181
        GasketStressYield = 182
        GasketStatus = 183
        ContactPenetration = 184
        ContactStatus = 185
        ContactGapDistance = 186
        StressLevelCrossingRate = 187
        VonMisesStressLevelCrossingRate = 188
        VonMisesStrainLevelCrossingRate = 189
        DisplacementLevelCrossingRate = 190
        RotationLevelCrossingRate = 191
        VelocityLevelCrossingRate = 192
        AngularVelocityLevelCrossingRate = 193
        AccelerationLevelCrossingRate = 194
        AngularAccelerationLevelCrossingRate = 195
        ElementForceLevelCrossingRate = 196
        ElementMomentLevelCrossingRate = 197
        ElementResultantsLevelCrossingRate = 198
        ShellResultantsLevelCrossingRate = 199
        BeamResultantsLevelCrossingRate = 200
        SpringDashpotResultantsLevelCrossingRate = 201
        ElementStrainResultantsLevelCrossingRate = 202
        ShellStrainResultantsLevelCrossingRate = 203
        BeamStrainResultantsLevelCrossingRate = 204
        SpringDashpotStrainResultantsLevelCrossingRate = 205
        XDisplacement = 206
        YDisplacement = 207
        ZDisplacement = 208
        LevelCrossingRateXDisplacement = 209
        LevelCrossingRateYDisplacement = 210
        LevelCrossingRateZDisplacement = 211
        XRotation = 212
        YRotation = 213
        ZRotation = 214
        LevelCrossingRateXRotation = 215
        LevelCrossingRateYRotation = 216
        LevelCrossingRateZRotation = 217
        XAcceleration = 218
        YAcceleration = 219
        ZAcceleration = 220
        LevelCrossingRateXAcceleration = 221
        LevelCrossingRateYAcceleration = 222
        LevelCrossingRateZAcceleration = 223
        XAngularAcceleration = 224
        YAngularAcceleration = 225
        ZAngularAcceleration = 226
        LevelCrossingRateXAngularAcceleration = 227
        LevelCrossingRateYAngularAcceleration = 228
        LevelCrossingRateZAngularAcceleration = 229
        XXStress = 230
        YYStress = 231
        ZZStress = 232
        XYStress = 233
        YZStress = 234
        ZXStress = 235
        LevelCrossingRateXXStress = 236
        LevelCrossingRateYYStress = 237
        LevelCrossingRateZZStress = 238
        LevelCrossingRateXYStress = 239
        LevelCrossingRateYZStress = 240
        LevelCrossingRateZXStress = 241
        XElementForce = 242
        YElementForce = 243
        ZElementForce = 244
        RXElementForce = 245
        RYElementForce = 246
        RZElementForce = 247
        LevelCrossingRateXElementForce = 248
        LevelCrossingRateYElementForce = 249
        LevelCrossingRateZElementForce = 250
        LevelCrossingRateRXElementForce = 251
        LevelCrossingRateRYElementForce = 252
        LevelCrossingRateRZElementForce = 253
        NXXShellResultant = 254
        NYYShellResultant = 255
        NXYShellResultant = 256
        MXXShellResultant = 257
        MYYShellResultant = 258
        MXYShellResultant = 259
        QXZShellResultant = 260
        QYZShellResultant = 261
        LevelCrossingRateNXXShellResultant = 262
        LevelCrossingRateNYYShellResultant = 263
        LevelCrossingRateNXYShellResultant = 264
        LevelCrossingRateMXXShellResultant = 265
        LevelCrossingRateMYYShellResultant = 266
        LevelCrossingRateMXYShellResultant = 267
        LevelCrossingRateQXZShellResultant = 268
        LevelCrossingRateQYZShellResultant = 269
        YPlus = 270
        ThermalConductivity = 271
        ThermalStrain = 272
        GapThickness = 273
        TotalForce = 274
        TotalMoment = 275
        TotalResidualForce = 276
        TotalResidualMoment = 277
        GridPointReactionForce = 278
        GridPointReactionMoment = 279
        GridPointAppliedForce = 280
        GridPointAppliedMoment = 281
        GlueForce = 282
        GluePressure = 283
        GlueTraction = 284
        Enthalpy = 285
        EnthalpyRate = 286
        NonlinearStress = 287
        NonlinearStrain = 288
        BondStress = 289
        BondStrain = 290
        SolidLaminateFailureIndex = 291
        SolidInterLaminarFailureIndex = 292
        ExternalAppliedHeatFlow = 293
        OptimizationDisplacement = 294
        DisplacementMagnitude = 295
        FractionVolume = 296
        FilmThickness = 297
        Time = 298
        SurfaceEmissivity = 299
        RootMeanSquareDisplacement = 300
        RootMeanSquareAcceleration = 301
        RootMeanSquareStress = 302
        ZeroCrossingsDisplacement = 303
        ZeroCrossingsAcceleration = 304
        ZeroCrossingsStress = 305
        SoundPressure = 306
        RootMeanSquareRotation = 307
        RootMeanSquareVelocity = 308
        RootMeanSquareAngularVelocity = 309
        RootMeanSquareAngularAcceleration = 310
        RootMeanSquareAppliedForce = 311
        RootMeanSquareAppliedMoment = 312
        RootMeanSquareVonMisesStress = 313
        ZeroCrossingseRotation = 314
        ZeroCrossingsVelocity = 315
        ZeroCrossingseAngularVelocity = 316
        ZeroCrossingseAngularAcceleration = 317
        ZeroCrossingseAppliedForce = 318
        ZeroCrossingseAppliedMoment = 319
        RootMeanSquareStrain = 320
        ZeroCrossingsStrain = 321
        PlasticStrain = 322
        LogarithmicStrain = 323
        TensionSafetyFactor = 324
        CompressionSafetyFactor = 325
        RootMeanSquareElementResultant = 326
        ZeroCrossingsElementResultant = 327
        RootMeanSquareShellResultants = 328
        RootMeanSquareBeamResultants = 329
        RootMeanSquareSpringDashpotResultant = 330
        ZeroCrossingsShellResultants = 331
        ZeroCrossingsBeamResultants = 332
        ZeroCrossingsSpringDashpotResultant = 333
        XReactionForce = 334
        YReactionForce = 335
        ZReactionForce = 336
        XReactionMoment = 337
        YReactionMoment = 338
        ZReactionMoment = 339
        LumpedMass = 340
        DistributedMassPerLength = 341
        DistributedMassPerArea = 342
        TemperatureLoad = 343
        TorsionStrain = 344
        AxialStress = 345
        AxialStrain = 346
        Length = 347
        SurfaceAbsoptivity = 348
        TurbulentIntensity = 349
        VaporToDryAirMassRatio = 350
        TracerFluidMassFraction = 351
        TotalMixtureMassFractions = 352
        Mass = 353
        SurfaceDensity = 354
        EmissivityValue = 355
        EffectiveEmissivity = 356
        VolumeFlow = 357
        CoefficientPerLength = 358
        Permeability = 359
        ThermalConductance = 360
        ThermalResistance = 361
        ConductancePerLength = 362
        SeebeckCoefficient = 363
        ElectricalResistivity = 364
        ElectricalResistance = 365
        Current = 366
        Power = 367
        HeatCapacity = 368
        TemperatureDifference = 369
        MassDensity = 370
        PrincipalStress = 371
        RootMeanSquareTorsionStress = 372
        ZeroCrossingsTorsionStress = 373
        RootMeanSquareTorsionStrain = 374
        ZeroCrossingsTorsionStrain = 375
        RootMeanSquareAxialStress = 376
        ZeroCrossingsAxialStress = 377
        RootMeanSquareAxialStrain = 378
        ZeroCrossingsAxialStrain = 379
        RootMeanSquareReactionForceMPC = 380
        ZeroCrossingsReactionForceMPC = 381
        MolecularDiffusionCoefficient = 382
        Angle = 383
        PressureDropToVelocityRatio = 384
        CauchyStress = 385
        EquivalentStress = 386
        PiolaKirchoffStress = 387
        GreenStrain = 388
        NormalContactForce = 389
        ShearContactForce = 390
        BiotStress = 391
        BiotStrain = 392
        NaturalStrain = 393
        Volume = 394
        PlyThermalStrain = 395
        PlyElasticStrain = 396
        CyclicReactionForce = 397
        CyclicReactionMoment = 398
        CurrentDensity = 399
        TrubulentStructures = 400
        TotalGlueSlipDistance = 401
        IncrementalGlueSlipDistance = 402
        ChockingGap = 403
        ChockingGapAtElementIntegrationPoint = 404
        InitialStrain = 405
        InitialStrainAtElementIntegrationPoint = 406
        LowersurfTemperature = 407
        MidsurfTemperature = 408
        UppersurfTemperature = 409
        TemperatureVarRate = 410
        GlasstransTemperature = 411
        ElectricPotential = 412
        Porosity = 413
        StrainEq = 414
        Damage = 415
        DamageEq = 416
        SpecificCapacitiveEnergy = 417
        GasMassFlux = 418
        RelativeDisplacement = 419
        HeatFluxApplied = 420
        HeatFluxEnthalpy = 421
        HeatFluxRadiativeEmitted = 422
        HeatFluxRadiativeFlame = 423
        HeatFluxRadiativeFlameEmitted = 424
        HeatFluxRadiativeFlameAbsorbed = 425
        TotalHeatFluxApplied = 426
        DissipatedEnergyDensity = 427
        DissipatedPowerDensity = 428
        DegreeConversion = 429
        AcousticPressure = 430
        AcousticIntensity = 431
        AcousticPower = 432
        MultiPointConstraintForce = 433
        MultiPointConstraintMoment = 434
        FluidAcousticCouplingQuality = 435
        FluidUncoupledAcousticCouplingQuality = 436
        StructuralAcousticCouplingQuality = 437
        StructuralUncoupledAcousticCouplingQuality = 438
        PressureCohesive = 439
        TactionCoheasive = 440
        PlyDamage = 441
        PlyPlasticDamage = 442
        EnergyDamage = 443
        StatusDamage = 444
        CohesiveNormalSeparation = 445
        CohesiveSlipDisplacement = 446
        CohesiveDamage = 447
        Sdv = 448
        SdvElementIntegrationPoint = 449
        BoltPreload2D = 450
        BoltPreload3D = 451
        MaxFrequency = 452
        FreeEdges = 453
        JunctionEdges = 454
        CoupledAcousticalNodes = 455
        StrainMech = 456
        StructuralAcousticCouplingDistance = 457
        NormalAcousticVelocity = 458
        NormalAcousticIntensity = 459
        SpecificCapacitivePower = 460
        TransportHeatFlux = 461
        VolumeHeatFlux = 462
        AcousticVelocity = 463
        CurrentDensityArea = 464
        ForceDensity = 465
        ForceDensityArea = 466
        ElectricFieldStrength = 467
        ElectricFluxDensity = 468
        PlyPlasticStrain = 469
        PlyStrainPlasticEq = 470
        PlyGreenStrain = 471
        PlyBiotStrain = 472
        PlyNaturalStrain = 473
        CyclicWorstPrincipalStrain = 474
        CyclicWorstPrincipalStress = 475
        CyclicWorstPrincipalStrainAngle = 476
        CyclicWorstPrincipalStressAngle = 477
        AxisymmetricWorstPrincipalStress = 478
        AxisymmetricWorstPrincipalStrain = 479
        XXStrain = 480
        YYStrain = 481
        ZZStrain = 482
        XYStrain = 483
        YZStrain = 484
        ZXStrain = 485
        LevelCrossingRateStrain = 486
        LevelCrossingRateXXStrain = 487
        LevelCrossingRateYYStrain = 488
        LevelCrossingRateZZStrain = 489
        LevelCrossingRateXYStrain = 490
        LevelCrossingRateYZStrain = 491
        LevelCrossingRateZXStrain = 492
        InitialImperfection = 493
        OffsetStrain = 494
        PlyStressEquivalent = 495
        PlyStressNonlinear = 496
        PressureGradient = 497
        NormalizedMassDensity = 498
        PSDDisplacement = 499
        PSDRMSDisplacement = 500
        PSDVelocity = 501
        PSDRMSVelocity = 502
        PSDAcceleration = 503
        PSDRMSAcceleration = 504
        PSDStress = 505
        PSDPerPlyStress = 506
        PSDRMSStress = 507
        PSDStrain = 508
        PSDPerPlyStressPerStrain = 509
        PSDRMSStressPerStrain = 510
        PSDSPCForce = 511
        PSDRMSSPCForce = 512
        PSDElementForce = 513
        PSDRMSElementForce = 514
        PSDPressure = 515
        PSDRMSPressure = 516
        ElementResultantPlasticStrain = 517
        ElementResultantElasticStrain = 518
        ElementResultantThermalStrain = 519
        ElementResultantCreepStrain = 520
        ElasticStrainVonMises = 521
        PlasticStrainVonMises = 522
        ThermalStrainVonMises = 523
        StrainVonMisesCreep = 524
        PlasticElemResultantStrainShell = 525
        PlasticElemResultantStrainBeam = 526
        PlasticElemResultantStrainSpringDashpot = 527
        ElasticElemResultantStrainShell = 528
        ElasticElemResultantStrainBeam = 529
        ElasticElemResultantStrainSpringDashpot = 530
        ThermalElemResultantStrainShell = 531
        ThermalElemResultantStrainBeam = 532
        ThermalElemResultantStrainSpringDashpot = 533
        ElemResultantStrainCreepShell = 534
        ElemResultantStrainCreepBeam = 535
        ElemResultantStrainCreepSpringDashpot = 536
        PlyStrainCreep = 537
        PowerSpectralDensityPressure = 538
        ZeroCrossingsPressure = 539
        RootMeanSquarePressure = 540
        AutoCorrelationPressure = 541
        CRMSPressure = 542
        PressureAbsoluteModal = 543
        DisplacementAbsoluteModal = 544
        AccelerationAbsoluteModal = 545
        VelocityAbsoluteModal = 546
        NormalDistance = 547
        EnergyDensity = 548
        Id = 549
        ElemResultantCreep = 550
        ElemResultantCreepShell = 551
        ElemResultantCreepBeam = 552
        ElemResultantCreepSpringDashpot = 553
        StrainEnergyPercent = 554
        PsdRotation = 555
        PsdAngularVelocity = 556
        PsdAngularAcceleration = 557
        PsdForceMpc = 558
        PsdPlyStrain = 559
        RMSStress = 560
        RMSPlyStress = 561
        RMSStressVonMises = 562
        RMSPlyStressVonMises = 563
        CRMSStress = 564
        CRMSPlyStress = 565
        EnergyStrain = 566
        RMSStrain = 567
        RMSPlyStrain = 568
        CRMSStrain = 569
        CRMSPlyStrain = 570
        EnergyDamping = 571
        PressureOverVolumeVelocity = 572
        SPForce = 573
        CumulativeRootMeanSquareDisplacement = 574
        CumulativeRootMeanSquareRotation = 575
        PSDReactionForce = 576
        RootMeanSquareReactionMomentMPC = 577
        ZeroCrossingsReactionMomentMPC = 578
        RootMeanSquareReactionForce = 579
        ZeroCrossingsReactionForce = 580
        RootMeanSquareReactionMoment = 581
        ZeroCrossingsReactionMoment = 582
        RootMeanSquareElementResultantStrain = 583
        ZeroCrossingsElementResultantStrain = 584
        RootMeanSquareShellStrainResultant = 585
        ZeroCrossingsShellStrainResultant = 586
        RootMeanSquareBeamStrainResultant = 587
        ZeroCrossingsBeamStrainResultant = 588
        RootMeanSquareSpringDashpotStrainResultant = 589
        ZeroCrossingsSpringDashpotStrainResultant = 590
        ElasticStrain = 591
        AdaptiveElementStressError = 592
        AdaptiveNodalMeshRefinementLevel = 593
        NormErrorStrainEnergy = 594
        NormErrorMaximumStrainEnergy = 595
        NormMaximumStrainEnergy = 596
        NormErrorMaximumStress = 597
        NormErrorStress = 598
        NormMaximumStress = 599
        NormStress = 600
        DynamicViscosity = 601
        NormStrainEnergy = 602
        ElementIntegrationPointStress = 603
        ElementIntegrationPointStrain = 604
        ElasticStrainAtElementIntegrationPoint = 605
        ThermalStrainAtElementIntegrationPoint = 606
        CreepStrain = 607
        CreepStrainAtElementIntegrationPoint = 608
        PlasticStrainAtElementIntegrationPoint = 609
        ContactSlipIncrementalDisplacement = 610
        ContactSliptotalDisplacement = 611
        GridPointReactionForceMPC = 612
        GridPointReactionMomentMPC = 613
        MagneticFluxDensity = 614
        MagneticField = 615
        TemperatureError = 616
        MaximumTemperatureError = 617
        XAngularVelocity = 618
        YAngularVelocity = 619
        ZAngularVelocity = 620
        RelativeRotation = 621
        GlueMoment = 622
        ContactMoment = 623
        NonLinearSpringDashpotResultant = 624
        DiffusionResistance = 625
        Aerea = 626
        FatigueStrengthCoeff = 627
        ThermalExpansionCoeff = 628
        MassMomentInertia = 629
        Frequency = 630
        MomentOfInertiaArea = 631
        ViscousDamping = 632
        Energy = 633
        Momentum = 634
        TransmissionLoss = 635
        SpecificHeat = 636
        Probability = 637
        DirCos = 638
        TotalDamage = 639
        ElementDisplacement = 640
        ConvectiveAreaFactor = 641
        ConvectiveThickness = 642
        MaxPrincipalPeakStress = 643
        MinPrincipalPeakStress = 644
        MaxPrincipalPeakStrain = 645
        MinPrincipalPeakStrain = 646
        Userdefined = 647
        Expression = 648
        SpecificEnthalpy = 649
        XVelocity = 650
        YVelocity = 651
        ZVelocity = 652
        LevelCrossingRateXVelocity = 653
        LevelCrossingRateYVelocity = 654
        LevelCrossingRateZVelocity = 655
        LevelCrossingRateXAngularVelocity = 656
        LevelCrossingRateYAngularVelocity = 657
        LevelCrossingRateZAngularVelocity = 658
        HomogYoungModulus = 659
        HomogPoissonRatio = 660
        HomogShearModulus = 661
        HomogTexpCoef = 662
        HomogChemShrinkage = 663
        FractionFiberVolume = 664
        PressureCoefficient = 665
        Force = 666
        Moment = 667
        TotalStrain = 668
        SolarPressure = 669
        SPCMoment = 670
        EquivalentElasticStrain = 671
        Fraction = 672
        VolumeAcceleration = 673
        NodeProximityToCad = 674
        Torue = 675
        MagneticFluxFunction = 676
        VolumeForceDensity = 677
        VolumeLossDensity = 678
        VolumeTorqueDensity = 679
        NodalTroqueDensityLength = 680
        NodalTorque = 681
        ElectricalConductivity = 682
        PermeanceCoefficient = 683
        RelativePermeability = 684
        RelativeReluctivity = 685
        SkinDepth = 686
        Demagnetization = 687
        DemagnetizationPrediction = 688
        ContactSlidingDistance = 689
    

    class PlyLocation(enum.Enum):
        Middle = 1
        Top = 2
        Bottom = 4
    

    class Location(enum.Enum):
        Nodal = 0
        Element = 1
        ElementNodal = 2
        ElementFace = 3
        ElementEdge = 4
        ElementFaceNode = 5
        ElementEdgeNode = 6
    

    class LoadcaseValueType(enum.Enum):
        Unknown = -1
        Frequency = 0
        LoadFactor = 1
        NodeDOF = 2
        LoadCase = 3
        Time = 4
    

    class InitialDeformationSelection(enum.Enum):
        None = 0
        Default = 1
        UserDefined = 2
    

    class GroupContainer(enum.Enum):
        ZeroDimensional = 0
        OneDimensional = 1
        TwoDimensional = 2
        ThreeDimensional = 3
        Connector = 4
        Other = 5
    

    class Filetype(enum.Enum):
        Nastran = 0
        Ideas = 1
        Bud = 2
        Vki = 3
        Abaqus = 4
        Ansys = 5
        Mapped = 6
        Afu = 7
        Rs2 = 8
        AbaqusOdb = 9
        LsdynaState = 10
        PermasPost = 11
        SamcefDes = 12
        NastranXdb = 13
        SysnoiseDb = 14
        LmsMotionFlexible = 15
        ScH5 = 16
        Scd5 = 17
        MappedOnModel = 18
    

    class ElementValueCriterion(enum.Enum):
        Average = 0
        Centroid = 1
        Maximum = 2
        Minimum = 3
        AbsoluteMaximum = 4
        AbsoluteMinimum = 5
        SignedAbsoluteMaximum = 6
        SignedAbsoluteMinimum = 7
    

    class ResultElementValue():
        DoElementValue: bool
        Criterion: CAE.Result.ElementValueCriterion
        def ToString(self) -> str:
            ...
        def __init__(self, DoElementValue: bool, Criterion: CAE.Result.ElementValueCriterion) -> None: ...
    

    class DiscontinuityMethod(enum.Enum):
        Relative = 0
        Weighted = 1
        Local = 2
        LocallyBalanced = 3
    

    class DeformationScale(enum.Enum):
        Model = 0
        Absolute = 1
    

    class ResultDeformationParameters():
        LoadCaseIndex: int
        IterationIndex: int
        Type: CAE.Result.Type
        Complex: CAE.Result.Complex
        PhaseAngle: float
        DeformationScale: CAE.Result.DeformationScale
        AbsoluteScaleValue: float
        ModelPercentScaleValue: float
        def ToString(self) -> str:
            ...
    

    class DbScale(enum.Enum):
        Db10 = 0
        Db20 = 1
    

    class DataType(enum.Enum):
        Scalar = 0
        Vector = 1
        SixVector = 2
        Tensor = 3
        ElementResultantShell = 4
        ElementResultantBeam = 5
        ElementResultantSpringDashpot = 6
        SixScalars = 7
        ThreeScalars = 8
        MultiScalar = 9
    

    class CoordinateSystemSource(enum.Enum):
        None = 0
        Model = 1
        Result = 2
    

    class CoordinateSystem(enum.Enum):
        AbsoluteRectangular = 0
        AbsoluteCylindrical = 1
        AbsoluteSpherical = 2
        WorkRectangular = 3
        WorkCylindrical = 4
        WorkSpherical = 5
        Local = 6
        Material = 7
        SelectRectangular = 8
        SelectCylindrical = 9
        SelectSpherical = 10
    

    class ComputationType(enum.Enum):
        None = 0
        Average = 1
        Sum = 2
        Minimum = 3
        Maximum = 4
        AbsoluteMinimum = 5
        AbsoluteMaximum = 6
        ArithmaticMean = 7
        Discontinuity = 8
        SignedAbsoluteMinimum = 9
        SignedAbsoluteMaximum = 10
    

    class Component(enum.Enum):
        Scalar = 0
        X = 1
        Y = 2
        Z = 3
        Magnitude = 4
        Xx = 5
        Yy = 6
        Zz = 7
        Xy = 8
        Yz = 9
        Zx = 10
        Determinant = 11
        Mean = 12
        MaximumShear = 13
        MinimumPrincipal = 14
        MiddlePrincipal = 15
        MaximumPrincipal = 16
        Octahedral = 17
        VonMises = 18
        MembraneXX = 19
        MembraneYY = 20
        MembraneXY = 21
        BendingXX = 22
        BendingYY = 23
        BendingXY = 24
        ShearXZ = 25
        ShearYZ = 26
        Axial = 27
        BendingS = 28
        BendingT = 29
        Torsion = 30
        ShearS = 31
        ShearT = 32
        SpringDashpotForce = 33
        SpringDashpotForceX = 34
        SpringDashpotForceY = 35
        SpringDashpotForceZ = 36
        SpringDashpotMomentX = 37
        SpringDashpotMomentY = 38
        SpringDashpotMomentZ = 39
        Scalar1 = 40
        Scalar2 = 41
        Scalar3 = 42
        Scalar4 = 43
        Scalar5 = 44
        Scalar6 = 45
        Scalar7 = 46
        Scalar8 = 47
        Scalar9 = 48
        Scalar10 = 49
        Scalar11 = 50
        Scalar12 = 51
        WorstPrincipal = 52
    

    class Complex(enum.Enum):
        Real = 0
        Imaginary = 1
        Amplitude = 2
        SignedAmplitude = 3
        PhaseAngle = 4
    

    class BeamSection(enum.Enum):
        NotApplicable = 0
        StressRecoveryPointC = 1
        StressRecoveryPointD = 2
        StressRecoveryPointE = 3
        StressRecoveryPointF = 4
        Minimum = 5
        Maximum = 6
    

    class BeamEnd(enum.Enum):
        None = -1
        Fore = 0
        Aft = 1
    

    class ResultAveraging():
        DoAveraging: bool
        AverageAcrossPropertyIds: bool
        AverageAcrossMaterialIds: bool
        AverageAcrossElementTypes: bool
        AverageAcrossFeatangle: bool
        AverageAcrossAnglevalue: float
        IncludeInternalElementContributions: bool
        def ToString(self) -> str:
            ...
    

    class Result_ResultParameters():
        load_case_index: int
        iteration_index: int
        type: CAE.Result.Type
        component: CAE.Result.Component
        res_section: CAE.Result.ResultSection
        section: int
        plynumber: int
        layer: int
        averaging: CAE.Result.Averaging
        include_midnode: bool
        coordinate_system: CAE.Result.CoordinateSystem
        display_beam_result_in_local_csys: bool
        element_value: CAE.Result.ElementValue
        complex: CAE.Result.Complex
        phase_angle: float
        absolute_value: bool
        scale_value: float
        unit: Tag
        calculate_beam_str_results: bool
        add_beam_str_fillets: bool
        beam_fillet_radius: float
    

    class Result_ResultBasicUnit():
        mass_unit: Tag
        length_unit: Tag
        time_unit: Tag
        temperature_unit: Tag
        angle_unit: Tag
        thermalenergy_unit: Tag
    

class RemoveRibsBuilder(Builder):
    def __init__(self) -> None: ...
    def DetectRibs(self) -> int:
        ...
    def GetRibElements(self, ribId: int) -> typing.List[CAE.FEElement]:
        ...
    def DeleteRibs(self, ribIds: int) -> None:
        ...
    CreateGroups: bool
    RibMaxArea: float
    RibMaxElem: int
    RibMinBoundaryNodeRatio: int
    SelectedElements: CAE.SelectElementsBuilder
    UseMidNodes: bool
    UseRibMaxArea: bool
    UseRibMaxElem: bool
    UseRibMinBoundaryNodeRatio: bool


class RemesherBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable
    SelectMesh: SelectTaggedObjectList


class RelatedVertexMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetVertices(self) -> typing.List[CAE.CAEVertex]:
        ...


class RelatedNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class RelatedFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class RelatedElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class RelatedElemFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementFaces(self) -> typing.List[CAE.SetObject]:
        """[Obsolete("Deprecated in NX11.0.2.  Use NXOpen.CAE.RelatedElemFaceMethod.GetFeElemFaces.")"""
        ...
    def GetFeElemFaces(self) -> typing.List[CAE.FEElemFace]:
        ...


class RelatedElemEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementEdges(self) -> typing.List[CAE.SetObject]:
        """[Obsolete("Deprecated in NX11.0.2.  Use NXOpen.CAE.RelatedElemEdgeMethod.GetFeElemEdges.")"""
        ...
    def GetFeElemEdges(self) -> typing.List[CAE.FEElemEdge]:
        ...


class RelatedEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEdges(self) -> typing.List[CAE.CAEEdge]:
        ...


class RelatedCurveMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetCurves(self) -> typing.List[Curve]:
        ...


class RelatedBodyMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetBodies(self) -> typing.List[CAE.CAEBody]:
        ...


class RecipeSurfaceWrap(CAE.Mesh):
    def __init__(self) -> None: ...


class RecipeOpenDuctMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class RecipeConvexMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class RecipeAcousticMeshAutomation(CAE.Mesh):
    def __init__(self) -> None: ...


class RecipeAcousticChamberMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class ReassignElementsBuilder(Builder):
    def __init__(self) -> None: ...
    EccName: str
    ElemSel: CAE.SelectElementsBuilder
    ElementDimOpt: CAE.ReassignElementsBuilder.ElementDimensionOption
    ElementTypeOpt: CAE.ReassignElementsBuilder.ElementTypeOption


    class ElementTypeOption(enum.Enum):
        FirstValue = 0
    

    class ElementDimensionOption(enum.Enum):
        Point = 0
        Beam = 1
        Shell = 2
        Solid = 3
    

class RadiusType(enum.Enum):
    AllTypes = 0
    Inside = 1
    Outside = 2


class QueryCurveUsageOptions(TaggedObject):
    def __init__(self) -> None: ...
    CurveUsage: CAE.QueryCurveUsageOptions.CurveUsageType
    DistanceTolerance: float
    ProjectDirection: Vector3d
    QueryCurve: CAE.QueryCurve
    ResultantCurveLocator: CAE.QueryCurveUsageOptions.ResultantCurveLocatorType
    ResultantLocationTolerance: float
    ReverseDirection: bool


    class ResultantCurveLocatorType(enum.Enum):
        UseAsIs = 0
        SnapToClosestNode = 1
        UseIntersectedElements = 2
    

    class CurveUsageType(enum.Enum):
        UseVertices = 0
        UseIntersectionLocation = 1
        ProjectToElementFaces = 2
    

class QueryCurvePost(CAE.QueryCurve):
    def __init__(self) -> None: ...


    class EntityType(enum.Enum):
        Node = 0
        Elem = 1
        Point = 2
    

    class QueryCurvePostEntity():
        Type: CAE.QueryCurvePost.EntityType
        Label: int
        Point: Point3d
        def ToString(self) -> str:
            ...
        def __init__(self, Type: CAE.QueryCurvePost.EntityType, Label: int, Point: Point3d) -> None: ...
    

class QueryCurveManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateQueryCurveBuilder(self) -> CAE.QueryCurveBuilder:
        ...
    def CreateQueryCurveBuilder(self, querycurve: CAE.QueryCurve) -> CAE.QueryCurveBuilder:
        ...
    def Tag(self) -> Tag: ...



class QueryCurveBuilder(Builder):
    def __init__(self) -> None: ...
    CurveName: str
    Selection: CAE.OrderedSelection


class QueryCurve(NXObject):
    def __init__(self) -> None: ...


class PropertyTable(BasePropertyTable):
    def __init__(self) -> None: ...
    def GetPropertyType(self, propertyName: str) -> CAE.PropertyTable.PropertyType:
        ...
    def GetTextPropertyValue(self, propertyName: str) -> str:
        ...
    def SetTextPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    def GetScalarWithDataPropertyValue(self, propertyName: str, propertyValue: float, unitType: Unit) -> None:
        ...
    def SetScalarWithDataPropertyValue(self, propertyName: str, propertyValue: float, unitType: Unit) -> None:
        ...
    def SetScalarWithDataPropertyValue(self, propertyName: str, propertyValue: str, unitType: Unit) -> None:
        ...
    def GetScalarFieldPropertyValue(self, propertyName: str) -> Fields.FieldExpression:
        ...
    def SetScalarFieldPropertyValue(self, propertyName: str, propertyValue: Fields.FieldExpression) -> None:
        ...
    def GetVectorPropertyValue(self, propertyName: str) -> Direction:
        ...
    def SetVectorPropertyValue(self, propertyName: str, propertyValue: Direction) -> None:
        ...
    def GetReferencePropertyValue(self, propertyName: str) -> NXObject:
        ...
    def SetReferencePropertyValue(self, propertyName: str, propertyValue: NXObject) -> None:
        ...
    def GetReferencePropertyValueArray(self, propertyName: str, propertyValues: typing.List[NXObject]) -> None:
        ...
    def SetReferencePropertyValueArray(self, propertyName: str, propertyValues: typing.List[NXObject]) -> None:
        ...
    def GetPointPropertyValue(self, propertyName: str) -> Point:
        ...
    def SetPointPropertyValue(self, propertyName: str, propertyValue: Point) -> None:
        ...
    def GetDateTimePropertyValue(self, propertyName: str, propertyYear: int, propertyMonth: int, propertyDay: int, propertyHour: int, propertyMin: int, propertySecond: int, propertyMsec: int) -> None:
        ...
    def SetDateTimePropertyValue(self, propertyName: str, propertyYear: int, propertyMonth: int, propertyDay: int, propertyHour: int, propertyMin: int, propertySecond: int, propertyMsec: int) -> None:
        ...
    def GetNamedPropertyTableArrayPropertyValue(self, propertyName: str) -> typing.List[CAE.NamedPropertyTable]:
        ...
    def SetNamedPropertyTableArrayPropertyValue(self, propertyName: str, propertyValue: typing.List[CAE.NamedPropertyTable]) -> None:
        ...
    def AddElementsToNamedPropertyTableArrayPropertyValue(self, propertyName: str, propertyValue: typing.List[CAE.NamedPropertyTable]) -> None:
        ...
    def RemoveElementsFromNamedPropertyTableArrayPropertyValue(self, propertyName: str, propertyValue: typing.List[CAE.NamedPropertyTable]) -> None:
        ...
    def GetSetManagerPropertyValue(self, propertyName: str) -> CAE.SetManager:
        ...
    def GetNamedPropertyTablePropertyValue(self, propertyName: str) -> CAE.NamedPropertyTable:
        ...
    def SetNamedPropertyTablePropertyValue(self, propertyName: str, namedPropertyTable: CAE.NamedPropertyTable) -> None:
        ...
    def GetAxisPropertyValue(self, propertyName: str) -> Axis:
        ...
    def SetAxisPropertyValue(self, propertyName: str, propertyValue: Axis) -> None:
        ...
    def GetPhysicalMaterialPropertyValue(self, propertyName: str) -> CAE.MaterialOptions:
        ...
    def SetPhysicalMaterialPropertyValue(self, propertyName: str, materialOptions: CAE.MaterialOptions) -> None:
        ...
    def GetCaeSectionPropertyValue(self, propertyName: str) -> CAE.BeamSectionOptions:
        ...
    def SetCaeSectionPropertyValue(self, propertyName: str, beamSectionOptions: CAE.BeamSectionOptions) -> None:
        ...
    def GetVectorFieldWrapperPropertyValue(self, propertyName: str) -> Fields.VectorFieldWrapper:
        ...
    def SetVectorFieldWrapperPropertyValue(self, propertyName: str, propertyValue: Fields.VectorFieldWrapper) -> None:
        ...
    def GetSectionOrientationPropertyValue(self, propertyName: str) -> CAE.BeamSectionOrientationOptions:
        ...
    def SetSectionOrientationPropertyValue(self, propertyName: str, beamSectionOptions: CAE.BeamSectionOrientationOptions) -> None:
        ...
    def GetSectionOffsetPropertyValue(self, propertyName: str) -> CAE.BeamSectionOffsetOptions:
        ...
    def SetSectionOffsetPropertyValue(self, propertyName: str, beamSectionOptions: CAE.BeamSectionOffsetOptions) -> None:
        ...
    def GetExtMenuPropertyValue(self, propertyName: str) -> str:
        ...
    def SetExtMenuPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    def GetStringArrayPropertyValue(self, propertyName: str) -> str:
        ...
    def SetStringArrayPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    def GetStringArrayPropertyValueChoices(self, propertyName: str) -> str:
        ...
    def GetPropertyDescriptorName(self, propertyName: str) -> str:
        ...


    class PropertyType(enum.Enum):
        Unknown = 0
        String = 1
        Boolean = 2
        Integer = 3
        Double = 4
        FieldWrapper = 5
        ScalarFieldWrapper = 6
        CoordinateSystem = 7
        DoubleArray = 8
        IntegerArray = 9
        PhysicalMaterial = 10
        Matrix = 11
        ScalarTable = 12
        Text = -1
        FieldExpression = -2
        VectorFieldWrapper = -3
        Vector = -4
        Reference = -5
        Point = -6
        DateTime = -7
        NamedPropertyTableArray = -8
        SetManager = -9
        NamedPropertyTable = -10
        Axis = -11
        CaeSection = -12
        SectionOrientation = -13
        SectionOffset = -14
        ReferenceArray = -15
        StringArray = -16
    

class ProjectNodesToCadGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    def IdentifyProximityNodes(self) -> None:
        ...
    def IdentifyCadGeometry(self) -> None:
        ...
    def GetNodes(self, nodes: typing.List[CAE.FENode], cadGeometries: typing.List[NXObject]) -> typing.List[Point3d]:
        ...
    def GetProximityNodes(self, proximityNodes: typing.List[CAE.FENode]) -> typing.List[Point3d]:
        ...
    def AdjustProximityNodes(self) -> None:
        ...
    def CreatePlotObject(self) -> CAE.NodeProximityPlotContours:
        ...
    AdjustedNodeLocationColor: NXColor
    CheckedObjectsList: SelectDisplayableObjectList
    IncludeMidnodes: bool
    ListingOptionState: CAE.ProjectNodesToCadGeometryBuilder.ListingOption
    OperationState: CAE.ProjectNodesToCadGeometryBuilder.Operation
    OriginalNodeLocationColor: NXColor
    ProximityTolerance: float
    SelectionList: CAE.SelectMeshList
    ShowNodeLabels: bool
    ShowNodeLocations: bool
    Tolerance: Expression


    class Operation(enum.Enum):
        Show = 0
        Adjust = 1
    

    class ListingOption(enum.Enum):
        None = -1
        SummaryOnly = 0
        All = 1
    

class ProbeOutputRecipe(NXObject):
    def __init__(self) -> None: ...
    def GetOutputRecipeType(self) -> CAE.ProbeOutputRecipe.Type:
        ...


    class Type(enum.Enum):
        Invalid = 0
        Graph = 1
        Field = 2
        PostView = 3
    

class ProbeAwarePostScenarioAction(CAE.PostScenarioAction):
    def __init__(self, ptr: int) -> None: ...
    def AddXProbeInfo(self, graphIndex: int, values: float, units: typing.List[Unit]) -> None:
        ...
    def AddZProbeInfo(self, graphIndex: int, values: float, units: typing.List[Unit]) -> None:
        ...
    def AddOrderProbeInfo(self, graphIndex: int, value: float) -> None:
        ...
    def AddAngleProbeInfo(self, graphIndex: int, value: float, unit: Unit) -> None:
        ...
    def GetAvailableXAxisMeasures(self, graphIndex: int) -> str:
        ...
    def GetAvailableZAxisMeasures(self, graphIndex: int) -> str:
        ...
    def IsOrderProbeSupported(self, graphIndex: int) -> bool:
        ...
    def IsAngleProbeSupported(self, graphIndex: int) -> bool:
        ...


class PrimitiveRecipeMeshBuilder(Builder):
    def __init__(self) -> None: ...
    ElementType: CAE.ElementTypeBuilder
    MeshName: str
    PropertyTable: CAE.PropertyTable


    class Type(enum.Enum):
        Sphere = 0
        Plane = 1
        PointSet = 2
        IsoPower = 3
        BoxSurface = 4
        BoxSolid = 5
        Circle = 6
        Line = 7
        AeroPanel = 8
        Cylinder = 9
        Hemisphere = 10
        AeroBody = 11
    

class PrimitiveRecipeMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class PrimitiveMeshBuilder(Builder):
    def __init__(self) -> None: ...
    ElementType: CAE.ElementTypeBuilder
    Name: str
    PropertyTable: CAE.PropertyTable


class PrimitiveMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class PreTestSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PreTestSolution]:
        ...
    def __init__(self, owner: CAE.CorrelManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.PreTestSolution:
        ...
    def ClonePretest(self, source: CAE.PreTestSolution) -> CAE.PreTestSolution:
        ...
    def DeletePretest(self, pretest: CAE.PreTestSolution) -> None:
        ...
    def CreatePretestBuilder(self, pretest: CAE.PreTestSolution) -> CAE.PreTestSolutionBuilder:
        ...
    def CreateSensorConfigBuilder(self, sensorConfig: CAE.PreTestSensorConfig) -> CAE.PreTestSensorConfigBuilder:
        ...
    def CreateExciterConfigBuilder(self, exciterConfig: CAE.PreTestExciterConfig) -> CAE.PreTestExciterConfigBuilder:
        ...
    def CreatePretestDofsetBuilder(self, dofset: CAE.PreTestDofSet) -> CAE.PreTestDofSetBuilder:
        ...
    def CreateAutoMacViewerBuilder(self, macInput: TaggedObject) -> CAE.AutoMacViewerBuilder:
        """[Obsolete("Deprecated in NX1847.0.0.  This function is no longer required.")"""
        ...
    def Tag(self) -> Tag: ...

    ActivePretest: CAE.PreTestSolution


class PreTestSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    HighFrequencyCutoff: float
    HighFrequencyFilteringMode: bool
    LowFrequencyCutoff: float
    LowFrequencyFilteringMode: bool
    Name: str
    Solution: CAE.SimSolution
    WorkSubcase: int


    class ModeConversionType(enum.Enum):
        SignedAmplitude = 0
        ComplexTransform = 1
    

class PreTestSolution(NXObject):
    def __init__(self) -> None: ...
    def SetActiveWorkMode(self, workModeNumber: int, active: bool) -> None:
        ...
    def SetWorkModeWeight(self, workModeNumber: int, weight: float) -> None:
        ...
    def ExportShapeMetricsCsvFile(self, metricCode: CAE.CorrelShapemetrictype, filename: str) -> None:
        ...
    def SolveSensorConfig(self, tSensorConfig: CAE.PreTestSensorConfig) -> None:
        ...
    def UpdateResultsForSolution(self, tSolution: CAE.SimSolution, ignoreReload: bool) -> None:
        ...
    def CreateExportUnvBuilder(self) -> CAE.PreTestExportUnvBuilder:
        ...
    def SolveExciterConfig(self, tExciterConfig: CAE.PreTestExciterConfig) -> None:
        ...
    def SensorConfigsInformation(self) -> None:
        ...
    def ExciterConfigsInformation(self) -> None:
        ...
    def IdentifyHighDisplacementNodes(self, nodes: typing.List[TaggedObject], threshold: float) -> None:
        ...
    SensorSelectionControl: CAE.PreTestSensorSelectionControl
    ExciterSelectionControl: CAE.PreTestExciterSelectionControl
    Name: str


class PreTestSensorSelectionDofSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PreTestDofSet]:
        ...
    def __init__(self, owner: CAE.PreTestSensorSelectionControl) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.PreTestDofSet:
        ...
    def Tag(self) -> Tag: ...



class PreTestSensorSelectionControl(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PreTestSolution) -> None: ...
    def Tag(self) -> Tag: ...

    SensorSelectionConfigs: CAE.PreTestSensorConfigCollection
    DofSets: CAE.PreTestSensorSelectionDofSetCollection


class PreTestSensorConfigCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PreTestSensorConfig]:
        ...
    def __init__(self, owner: CAE.PreTestSensorSelectionControl) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.PreTestSensorConfig:
        ...
    def CloneSensorConfig(self, source: CAE.PreTestSensorConfig) -> CAE.PreTestSensorConfig:
        ...
    def RemoveSensorConfig(self, toRemove: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveSensorConfig: int


class PreTestSensorConfigBuilder(Builder):
    def __init__(self) -> None: ...
    AlgorithmChoice: CAE.PreTestSensorConfigBuilder.AlgorithmChoiceType
    MacLimit: float
    MaxDofs: int
    Name: str
    NumTriaxialSensors: int
    NumUniaxialSensors: int
    SensorChoice: CAE.PreTestSensorConfigBuilder.SensorChoiceType


    class SensorChoiceType(enum.Enum):
        Uniaxial = 0
        Triaxial = 1
    

    class AlgorithmChoiceType(enum.Enum):
        MinMac = 0
        ModMac = 1
    

class PreTestSensorConfig(NXObject):
    def __init__(self) -> None: ...
    def ExportCsvFile(self, mSol: CAE.PreTestSolution, filename: str) -> None:
        ...
    def ExportShapeMetricsCsvFile(self, metricCode: CAE.CorrelShapemetrictype, filename: str) -> None:
        ...
    def GenerateMatchingDofset(self) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Behaves like new function with no change in disp csys.")"""
        ...
    def GenerateMatchingDofset(self, changeDispCSys: bool) -> None:
        ...
    def Information(self, mSol: CAE.PreTestSolution) -> None:
        ...
    def ShapeMetricInformation(self, metricCode: CAE.CorrelShapemetrictype) -> None:
        ...
    Name: str


class PreTestSensor(DisplayableObject):
    def __init__(self) -> None: ...


class PreTestExportUnvBuilder(Builder):
    def __init__(self) -> None: ...
    ElementsSelection: CAE.SelectElementsBuilder
    GroupsSelection: CAE.SelectGroupsBuilder
    NativeFileBrowser: str
    NativeFileUnits: CAE.PreTestExportUnvBuilder.FileUnitsOption


    class FileUnitsOption(enum.Enum):
        Si = 0
        Bg = 1
        Mg = 2
        Ba = 3
        Mm = 4
        Cm = 5
        In = 6
        Gm = 7
        Mn = 8
    

class PreTestExciterSelectionDofSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PreTestDofSet]:
        ...
    def __init__(self, owner: CAE.PreTestExciterSelectionControl) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.PreTestDofSet:
        ...
    def Tag(self) -> Tag: ...



class PreTestExciterSelectionControl(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PreTestSolution) -> None: ...
    def Tag(self) -> Tag: ...

    ExciterSelectionConfigs: CAE.PreTestExciterConfigCollection
    DofSets: CAE.PreTestExciterSelectionDofSetCollection


class PreTestExciterConfigCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PreTestExciterConfig]:
        ...
    def __init__(self, owner: CAE.PreTestExciterSelectionControl) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.PreTestExciterConfig:
        ...
    def CloneExciterConfig(self, source: CAE.PreTestExciterConfig) -> CAE.PreTestExciterConfig:
        ...
    def RemoveExciterConfig(self, toRemove: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveExciterConfig: int


class PreTestExciterConfigBuilder(Builder):
    def __init__(self) -> None: ...
    DampingRatio: float
    MethodChoice: CAE.PreTestExciterConfigBuilder.MethodChoiceType
    Name: str
    NmifThreshold: float
    OffAxisAngleChoice: CAE.PreTestExciterConfigBuilder.OffAxisAngleChoiceType


    class OffAxisAngleChoiceType(enum.Enum):
        None = 0
        Angle45 = 1
        Angle30 = 2
    

    class MethodChoiceType(enum.Enum):
        AutomaticNmif = 0
        Manual = 1
    

class PreTestExciterConfig(NXObject):
    def __init__(self) -> None: ...
    def ExportCsvFile(self, filename: str) -> None:
        ...
    def ExportShapeMetricsCsvFile(self, metricCode: CAE.CorrelShapemetrictype, filename: str) -> None:
        ...
    def GenerateMatchingDofset(self, changeDispCSys: bool) -> None:
        ...
    def Information(self, mSol: CAE.PreTestSolution) -> None:
        ...
    ConfigName: str
    Name: str


class PreTestExciter(DisplayableObject):
    def __init__(self) -> None: ...


class PreTestDofSetBuilder(Builder):
    def __init__(self) -> None: ...
    def GetUseNormalDofs(self, nodes: typing.List[CAE.FENode], useNormalDofs: bool) -> None:
        ...
    def SetUseNormalDofs(self, nodes: typing.List[CAE.FENode], useNormalDofs: bool) -> None:
        ...
    def GetDofValues(self, nodes: typing.List[CAE.FENode], dofValues: int) -> None:
        ...
    def SetDofValues(self, nodes: typing.List[CAE.FENode], dofValues: int) -> None:
        ...
    ConflictResolutionRule: CAE.PreTestDofSetBuilder.ConflictResolution
    DofSetSelect: CAE.CaeDOFSet
    Nodes: CAE.SelectFENodeList
    NodesEnabled: bool
    UseNormalDof: bool


    class ConflictResolution(enum.Enum):
        ApplyFromDofSet = 0
        ApplyFromSelectedNodes = 1
    

class PreTestDofSet(NXObject):
    def __init__(self) -> None: ...
    def SetDofSet(self, dofsetref: CAE.CaeDOFSet) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Please use the builder NXOpen.CAE.PreTestDofSetBuilder to set DOFSet.")"""
        ...
    def SetDofs(self, nodes: typing.List[CAE.FENode], dofs: bool) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Please use the builder NXOpen.CAE.PreTestDofSetBuilder to set dofs.")"""
        ...
    def ExportShapeMetricsCsvFile(self, metricCode: CAE.CorrelShapemetrictype, filename: str) -> None:
        ...
    def ClearDofSet(self) -> None:
        ...
    def Information(self) -> None:
        ...
    def InitializeFrom(self, extDofSet: CAE.PreTestDofSet) -> None:
        ...
    def InitializeFrom(self, sensorConfig: CAE.PreTestSensorConfig) -> None:
        ...
    def InitializeFrom(self, exciterConfig: CAE.PreTestExciterConfig) -> None:
        ...
    def RemoveDof(self, removeINode: CAE.FENode, removeDofType: CAE.PreTestDofSet.DofType, createAndAssignNewDofset: bool) -> None:
        ...


    class InitializationType(enum.Enum):
        Dof = 0
        Config = 1
    

    class DofType(enum.Enum):
        Normal = -1
        X = 1
        Y = 2
        Z = 4
    

class PreparedMesh1dBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    def GetBeamSectionsFromSelectionList(self) -> typing.List[CADCAEPrep.IBeamSection]:
        ...
    AutoChainOption: bool
    ElementType: CAE.ElementTypeBuilder
    FlipDirectionOption: bool
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList


class PreparedMesh1d(CAE.Mesh):
    def __init__(self) -> None: ...


class PostViewportPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    HighlightSelectedViewport: bool
    MasterViewportHighlightColor: NXColor
    OtherViewportHighlightColor: NXColor


class PostSmartSelectionManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Post) -> None: ...
    def CreateRelatedElementsMethodBySeedEntity(self, seedEntity: CAE.PostSelectionEntity, pvid: int) -> CAE.PostRelatedElementsMethod:
        ...
    def CreateRelatedElementsMethodBySeedGeometry(self, seedGeom: TaggedObject, pvid: int) -> CAE.PostRelatedElementsMethod:
        ...
    def CreateRelatedNodesMethodBySeedEntity(self, seedEntity: CAE.PostSelectionEntity, pvid: int) -> CAE.PostRelatedNodesMethod:
        ...
    def CreateRelatedNodesMethodBySeedGeometry(self, seedGeom: TaggedObject, pvid: int) -> CAE.PostRelatedNodesMethod:
        ...
    def CreateNMaxResultsMethod(self, pMethodParameters: CAE.PostSmartSelectionManager.NMaxMinParameters) -> CAE.PostNMaxMinMethod:
        ...
    def CreateNMinResultsMethod(self, pMethodParameters: CAE.PostSmartSelectionManager.NMaxMinParameters) -> CAE.PostNMaxMinMethod:
        ...
    def CreateResultRangeMethod(self, pMethodParameters: CAE.PostSmartSelectionManager.ResultRangeParameters) -> CAE.PostResultRangeMethod:
        ...
    def Tag(self) -> Tag: ...



    class PostSmartSelectionManagerResultRangeParameters():
        Pvid: int
        IsBelowValueSpecified: bool
        BelowValue: float
        IsAboveValueSpecified: bool
        AboveValue: float
        EntityType: CAE.PostSmartSelectionManager.EntityType
        IncludeVisibleEntitiesOnly: bool
        def ToString(self) -> str:
            ...
    

    class PostSmartSelectionManagerNMaxMinParameters():
        EntityType: CAE.PostSmartSelectionManager.EntityType
        NResults: int
        Pvid: int
        IncludeVisibleEntitiesOnly: bool
        def ToString(self) -> str:
            ...
    

    class EntityType(enum.Enum):
        None = -1
        Node = 0
        Elem = 1
    

class PostShowhideBuilder(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def CommitShowhide(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    def SetSelectedEntities(self, selent: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    def GetSelectedEntities(self, selent: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    def GetVisibility(self) -> CAE.PostShowhideBuilder.Vis:
        ...
    def SetVisibility(self, doshow: CAE.PostShowhideBuilder.Vis) -> None:
        ...
    def GetPvid(self) -> int:
        ...
    def SetPvid(self, pvid: int) -> None:
        ...
    def SetMeshes(self, meshes: typing.List[CAE.PostMesh]) -> None:
        ...


    class Vis(enum.Enum):
        Showonly = 0
        Show = 1
        Hide = 2
    

class PostSelectionEntityList(TaggedObject):
    def __init__(self) -> None: ...
    def AddEntity(self, selEntity: CAE.PostSelectionEntity) -> None:
        ...
    def AddMethod(self, pSmartMethod: CAE.PostISmartSelectorMethod) -> None:
        ...
    def RemoveMethod(self, pSmartMethod: CAE.PostISmartSelectorMethod) -> None:
        ...
    def GetEntity(self, index: int) -> CAE.PostSelectionEntity:
        ...
    def RemoveEntities(self, indices: int) -> None:
        ...
    def Clear(self) -> None:
        ...
    def GetEntityCount(self) -> int:
        ...
    def AskMatchingEntitiesByElementIds(self, elementIds: int, indices: int) -> None:
        ...
    def AskMatchingEntitiesByNodeIds(self, nodeIds: int, indices: int) -> None:
        ...


class PostSelectionEntity(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def HasNode(self) -> bool:
        ...
    def HasElem(self) -> bool:
        ...
    def HasEdge(self) -> bool:
        ...
    def HasFace(self) -> bool:
        ...
    def HasSE(self) -> bool:
        ...
    def HasSector(self) -> bool:
        ...
    def HasRotationAngle(self) -> bool:
        ...
    def HasPoint(self) -> bool:
        ...
    def GetFeatedge(self, edgeElemId: int, edgeIdx: int) -> None:
        ...
    def SetFeatedge(self, edgeElemId: int, edgeIdx: int) -> None:
        ...
    def HasFeatedge(self) -> bool:
        ...
    def HasFeatface(self) -> bool:
        ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    EdgeId: int
    ElemId: int
    FaceId: int
    Featface: int
    NodeId: int
    Point: Point3d
    RotationAngle: float
    SEId: int
    SectorId: int


class PostScenarioXyPlotHandle(CAE.PostScenarioPlotHandle):
    def __init__(self) -> None: ...
    def CreateResultAccessor(self) -> CAE.Xyplot.ResultAccessor:
        ...
    CanvasIndex: int
    XyPlot: CAE.Xyplot.Plot


class PostScenarioWeightingType(enum.Enum):
    Unknown = 0
    NoWeighting = 1
    A = 2
    B = 3
    C = 4
    D = 5
    Ab = 6
    Bc = 7


class PostScenarioVisualizationDefinition(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


class PostScenarioVisualizationCustomizationCollection(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSubviewportIds(self) -> int:
        ...
    def GetVisualizationNames(self) -> str:
        ...
    def GetVisualizationCustomization(self, subviewPortId: int) -> CAE.IPostScenarioVisualizationCustomization:
        ...
    def GetVisualizationCustomization(self, visualizationName: str) -> CAE.IPostScenarioVisualizationCustomization:
        ...


class PostScenarioVisualizationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioVisualizationDefinition]:
        ...
    def __init__(self, owner: CAE.PostScenarioInputDefinition) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioVisualizationDefinition:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioVariantType(enum.Enum):
    Unary = 0
    Boolean = 1
    Integer = 2
    Double = 3
    Complex = 4
    String = 5
    UnicodeString = 6
    Vector3d = 7
    Component = 8
    ModeDescription = 9
    Wildcard = 10
    CoordinateSystem = 11
    DoubleDataOnNodesOfElements = 12
    ComplexDataOnNodesOfElements = 13


class PostScenarioVariantList(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetValueAsBoolean(self) -> bool:
        ...
    def GetValueAsInteger(self) -> int:
        ...
    def GetValueAsDouble(self) -> float:
        ...
    def GetValueAsComplex(self) -> typing.List[CAE.Complex]:
        ...
    def GetValueAsString(self) -> str:
        ...
    def GetValueAsUnicodeString(self) -> str:
        ...
    def GetValueAsVector3d(self) -> typing.List[Vector3d]:
        ...
    def GetValueAsModeDescription(self) -> typing.List[CAE.PostScenarioModeDescription]:
        ...
    def GetValueAsCoordinateSystem(self) -> typing.List[CAE.PostScenarioCoordinateSystem]:
        ...
    def GetValueAsDoubleDataOnNodesOfElements(self) -> typing.List[CAE.PostScenarioDoubleDataOnNodesOfElements]:
        ...
    def GetValueAsComplexDataOnNodesOfElements(self) -> typing.List[CAE.PostScenarioComplexDataOnNodesOfElements]:
        ...
    def GetDataType(self) -> CAE.PostScenarioVariantType:
        ...
    def FreeResource(self) -> None:
        ...
    def SetValueAsBoolean(self, value: bool) -> None:
        ...
    def SetValueAsInteger(self, value: int) -> None:
        ...
    def SetValueAsDouble(self, value: float) -> None:
        ...
    def SetValueAsComplex(self, value: typing.List[CAE.Complex]) -> None:
        ...
    def SetValueAsString(self, value: str) -> None:
        ...
    def SetValueAsUnicodeString(self, value: str) -> None:
        ...
    def SetValueAsUnary(self, nValues: int) -> None:
        ...
    def SetValueAsVector3d(self, value: typing.List[Vector3d]) -> None:
        ...
    def SetValueAsModeDescription(self, value: typing.List[CAE.PostScenarioModeDescription]) -> None:
        ...
    def SetValueAsCoordinateSystem(self, value: typing.List[CAE.PostScenarioCoordinateSystem]) -> None:
        ...
    def SetValueAsDoubleDataOnNodesOfElements(self, value: typing.List[CAE.PostScenarioDoubleDataOnNodesOfElements]) -> None:
        ...
    def SetValueAsComplexDataOnNodesOfElements(self, value: typing.List[CAE.PostScenarioComplexDataOnNodesOfElements]) -> None:
        ...
    def NewPostScenarioCoordinateSystem(self, type: CAE.PostScenarioCoordinateSystemType, origin: Vector3d, matrix: Matrix3x3) -> CAE.PostScenarioCoordinateSystem:
        ...


class PostScenarioVariantComponent(enum.Enum):
    Scalar = 0
    X = 1
    Y = 2
    Z = 3
    Magnitude = 4
    Xx = 5
    Yy = 6
    Zz = 7
    Xy = 8
    Xz = 9
    Yx = 10
    Yz = 11
    Zx = 12
    Zy = 13
    Determinant = 14
    Mean = 15
    MaxShear = 16
    MinPrincipal = 17
    MidPrincipal = 18
    MaxPrincipal = 19
    WorstPrincipal = 20
    Octahedral = 21
    VonMises = 22
    Axial = 23
    Torque = 24
    AxialXx = 25
    ShearXy = 26
    ShearXz = 27
    BendingYy = 28
    BendingZz = 29
    TorsionXx = 30


class PostScenarioVariant(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def ToStringRepr(self) -> str:
        ...
    def GetValueAsBoolean(self) -> bool:
        ...
    def GetValueAsInteger(self) -> int:
        ...
    def GetValueAsDouble(self) -> float:
        ...
    def GetValueAsComplex(self) -> CAE.Complex:
        ...
    def GetValueAsString(self) -> str:
        ...
    def GetValueAsUnicodeString(self) -> str:
        ...
    def GetValueAsVector3d(self) -> Vector3d:
        ...
    def GetValueAsComponent(self) -> CAE.PostScenarioVariantComponent:
        ...
    def GetValueAsModeDescription(self) -> CAE.PostScenarioModeDescription:
        ...
    def GetValueAsCoordinateSystem(self) -> CAE.PostScenarioCoordinateSystem:
        ...
    def GetDataType(self) -> CAE.PostScenarioVariantType:
        ...
    def FreeResource(self) -> None:
        ...
    def SetValueAsBoolean(self, value: bool) -> None:
        ...
    def SetValueAsInteger(self, value: int) -> None:
        ...
    def SetValueAsDouble(self, value: float) -> None:
        ...
    def SetValueAsComplex(self, value: CAE.Complex) -> None:
        ...
    def SetValueAsString(self, value: str) -> None:
        ...
    def SetValueAsUnicodeString(self, value: str) -> None:
        ...
    def SetValueAsUnary(self) -> None:
        ...
    def SetValueAsWildcard(self) -> None:
        ...
    def SetValueAsVector3d(self, value: Vector3d) -> None:
        ...
    def SetValueAsComponent(self, value: CAE.PostScenarioVariantComponent) -> None:
        ...
    def SetValueAsModeDescription(self, value: CAE.PostScenarioModeDescription) -> None:
        ...
    def SetValueAsCoordinateSystem(self, value: CAE.PostScenarioCoordinateSystem) -> None:
        ...
    def NewPostScenarioCoordinateSystem(self, type: CAE.PostScenarioCoordinateSystemType, origin: Vector3d, matrix: Matrix3x3) -> CAE.PostScenarioCoordinateSystem:
        ...


class PostScenarioVariableDomain(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetAllBaseDomains(self) -> str:
        ...
    def GetAllSubdomains(self, baseDomain: str) -> str:
        ...
    def AddComponent(self, baseDomain: str, subdomains: str) -> None:
        ...
    def GetMeasure(self) -> str:
        ...
    def GetUnit(self) -> Unit:
        ...
    def GetNumberOfComponents(self) -> int:
        ...
    def GetNthComponent(self, n: int, baseDomain: str, subdomains: str) -> None:
        ...


class PostScenarioVariableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioVariable]:
        ...
    def __init__(self, owner: CAE.PostScenarioSelectionParameters) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioVariable:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioVariable(TaggedObject):
    def __init__(self) -> None: ...
    def AssignBooleanValues(self, values: bool) -> None:
        ...
    def AssignIntegerValues(self, values: int) -> None:
        ...
    def AssignDoubleValues(self, values: float) -> None:
        ...
    def AssignComplexValues(self, values: typing.List[CAE.Complex]) -> None:
        ...
    def AssignStringValues(self, values: str) -> None:
        ...
    def AssignUnicodeStringValues(self, values: str) -> None:
        ...
    def AssignValues(self, values: typing.List[CAE.PostScenarioVariant]) -> None:
        ...
    def AssignDefaults(self) -> None:
        ...
    def GetValues(self) -> typing.List[CAE.PostScenarioVariant]:
        ...
    def GetAssignedValues(self) -> typing.List[CAE.PostScenarioVariant]:
        ...
    def SetIterationValues(self, behavior: CAE.PostScenarioVariable.IterationOption) -> None:
        ...
    def SetIterationValues(self, values: typing.List[CAE.PostScenarioVariant]) -> None:
        ...
    DisplayName: str
    Name: str


    class IterationOption(enum.Enum):
        All = 0
        None = 1
    

class PostScenarioValueCollector(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AddString(self, theValue: str) -> None:
        ...
    def AddValue(self, theValue: CAE.PostScenarioVariant) -> None:
        ...
    def GetValues(self) -> typing.List[CAE.PostScenarioVariant]:
        ...
    def FreeResource(self) -> None:
        ...


class PostScenarioSpectrumMode(enum.Enum):
    Unknown = 0
    Peak = 1
    Rms = 2


class PostScenarioSpectrumFormat(enum.Enum):
    Unknown = 0
    Linear = 1
    Power = 2


class PostScenarioSelectionParameters(TaggedObject):
    def __init__(self) -> None: ...
    def NewVariant(self) -> CAE.PostScenarioVariant:
        ...
    def Destroy(self) -> None:
        ...
    def SetIterationVariable(self, variable: CAE.PostScenarioVariable) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.PostScenarioVariable.SetIterationValues")"""
        ...
    Variables: CAE.PostScenarioVariableCollection
    ConfigurationVariables: CAE.PostScenarioConfigurationVariableCollection


class PostScenarioSelectionCallbackContext(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetCurrentSelection(self, variable: str) -> typing.List[CAE.PostScenarioVariant]:
        ...
    def GetDataSourceDefaultValue(self, variable: str) -> CAE.PostScenarioVariant:
        ...
    def GetSelectedMeshes(self) -> typing.List[CAE.PostScenarioMesh]:
        ...
    def GetMeshNodes(self) -> typing.List[CAE.PostScenarioMeshNode]:
        ...
    CurrentVariable: CAE.PostScenarioResultGroupVariable
    CurrentVariableName: str
    MessageCollector: CAE.PostScenarioMessageCollector


class PostScenarioResultGroupVariable(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    ComponentType: CAE.PostScenarioComponentType
    DataType: CAE.PostScenarioVariantType
    Domain: CAE.PostScenarioVariableDomain
    Name: str


class PostScenarioResultGroupBuilder(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddSelectionVariable(self, name: str, dataType: CAE.PostScenarioVariantType, domain: CAE.PostScenarioVariableDomain) -> None:
        ...
    def AddIndependentVariable(self, name: str, dataType: CAE.PostScenarioVariantType, domain: CAE.PostScenarioVariableDomain) -> None:
        ...
    def AddDependentVariable(self, name: str, dataType: CAE.PostScenarioVariantType, compType: CAE.PostScenarioComponentType, domain: CAE.PostScenarioVariableDomain) -> None:
        ...
    def Commit(self) -> None:
        ...


class PostScenarioResultGroup(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSelectionVariables(self) -> typing.List[CAE.PostScenarioResultGroupVariable]:
        ...
    def GetIndependentVariables(self) -> typing.List[CAE.PostScenarioResultGroupVariable]:
        ...
    def GetDependentVariables(self) -> typing.List[CAE.PostScenarioResultGroupVariable]:
        ...
    def GetPlots(self) -> typing.List[CAE.PostScenarioPlotData]:
        ...
    Name: str


class PostScenarioRayModelViewPlotHandle(CAE.PostScenarioPlotHandle):
    def __init__(self) -> None: ...
    Rays: CAE.PostScenarioRayCollection


class PostScenarioRayCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioRay]:
        ...
    def __init__(self, owner: CAE.PostScenarioRayModelViewPlotHandle) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, plotName: str) -> CAE.PostScenarioRay:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioRay(TaggedObject):
    def __init__(self) -> None: ...
    def GetPoints(self) -> typing.List[Point3d]:
        ...
    Number: int


class PostScenarioQueryResults(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def NewResultGroupBuilder(self, name: str) -> CAE.PostScenarioResultGroupBuilder:
        ...
    def NewConfigurationGroupBuilder(self, name: str) -> CAE.PostScenarioConfigurationGroupBuilder:
        ...
    def NewPlotBuilder(self, name: str, resultGroup: str, namedSelection: str) -> CAE.PostScenarioPlotBuilder:
        ...
    def GetResultGroups(self) -> typing.List[CAE.PostScenarioResultGroup]:
        ...
    def GetConfigurationGroups(self) -> typing.List[CAE.PostScenarioConfigurationGroup]:
        ...
    def NewMetadata(self) -> CAE.PostScenarioMetadata:
        ...
    Name: str


class PostScenarioQueryContext(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetMeshNodes(self) -> typing.List[CAE.PostScenarioMeshNode]:
        ...
    def GetSelectedMeshes(self) -> typing.List[CAE.PostScenarioMesh]:
        ...
    MessageCollector: CAE.PostScenarioMessageCollector
    ResultCoordinateSystems: CAE.PostScenarioQueryResults


class PostScenarioPostViewHandle(CAE.PostScenarioPlotHandle):
    def __init__(self) -> None: ...
    def CreateResultAccess(self) -> CAE.ResultAccess:
        ...
    def DeleteResultAccess(self, raccess: CAE.ResultAccess) -> None:
        ...
    PostViewId: int
    ResultId: int


class PostScenarioPlotTypes(enum.Enum):
    Replace = 0
    UpdateScenario = 1
    Overlay = 2


class PostScenarioPlotHandleCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioPlotHandle]:
        ...
    def __init__(self, owner: CAE.PostScenario) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, plotName: str) -> CAE.PostScenarioPlotHandle:
        ...
    def FindObjectByViewport(self, viewportIndex: int) -> CAE.PostScenarioPlotHandle:
        ...
    def FindObjectByDescriptiveName(self, visualizationDefinitionName: str) -> CAE.PostScenarioPlotHandle:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioPlotHandle(TaggedObject):
    def __init__(self) -> None: ...
    def GetDescriptiveName(self) -> str:
        ...
    def GetPlotData(self) -> typing.List[CAE.PostScenarioPlotData]:
        ...
    ViewportIndex: int


class PostScenarioPlotEntryBuilder(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetHighOrderIndependent(self, variableName: str, values: CAE.PostScenarioVariant) -> None:
        ...
    def SetIndependent(self, variableName: str, values: CAE.PostScenarioVariantList) -> None:
        ...
    def AssignDependent(self, variableName: str, comp: CAE.PostScenarioVariantComponent, values: CAE.PostScenarioVariantList) -> None:
        ...
    def Commit(self) -> None:
        ...


class PostScenarioPlotDataEntry(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetHighOrderIndependentVariableValue(self, name: str) -> CAE.PostScenarioVariant:
        ...
    def GetIndependentValues(self) -> CAE.PostScenarioVariantList:
        ...
    def GetAvailableComponents(self, name: str) -> typing.List[CAE.PostScenarioVariantComponent]:
        ...
    def GetDependentValues(self, name: str, component: CAE.PostScenarioVariantComponent) -> CAE.PostScenarioVariantList:
        ...


class PostScenarioPlotData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSelectionVariableValue(self, name: str) -> CAE.PostScenarioVariant:
        ...
    def GetSelectionVariableMetadata(self, name: str) -> CAE.PostScenarioMetadata:
        ...
    def GetEntries(self) -> typing.List[CAE.PostScenarioPlotDataEntry]:
        ...
    ConfigurationGroupName: str
    Metadata: CAE.PostScenarioMetadata
    Name: str
    ResultGroupName: str


class PostScenarioPlotBuilder(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetSelectionValue(self, variableName: str, values: CAE.PostScenarioVariant) -> None:
        ...
    def SetSelectionValue(self, variableName: str, values: CAE.PostScenarioVariant, metadata: CAE.PostScenarioMetadata) -> None:
        ...
    def NewPlotEntryBuilder(self) -> CAE.PostScenarioPlotEntryBuilder:
        ...
    def Commit(self) -> None:
        ...
    def SetMetadata(self, metadata: CAE.PostScenarioMetadata) -> None:
        ...
    def GeneratePlotName(self, dof: CAE.PostScenarioVariantComponent) -> str:
        ...
    def GetPlotNameComponent(self) -> CAE.PostScenarioVariantComponent:
        ...
    Name: str


class PostScenarioParameters(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetPreferredDataSources(self, dataSources: typing.List[CAE.DataSource]) -> None:
        ...
    DataSource: CAE.IPostScenarioDataSource
    ScenarioDescriptor: CAE.PostScenarioDescriptor
    ViewPortIndex: int


class PostScenarioModeDescription():
    Number: int
    Frequency: float
    def ToString(self) -> str:
        ...
    def __init__(self, Number: int, Frequency: float) -> None: ...


class PostScenarioMetadata(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetKeys(self) -> str:
        ...
    def GetValue(self, key: str) -> CAE.PostScenarioVariant:
        ...
    def SetKeyValue(self, key: str, values: CAE.PostScenarioVariant) -> None:
        ...
    def GetComplexOption(self) -> typing.List[CAE.PostScenarioComplexOption]:
        ...
    def SetComplexOption(self, complexOptions: typing.List[CAE.PostScenarioComplexOption]) -> None:
        ...
    def GetOrigin(self, username: str, displayName: str) -> None:
        ...
    def SetOrigin(self, username: str, displayName: str) -> None:
        ...
    def GetAdditionalLegendColumns(self, headers: str, values: str) -> None:
        ...
    def SetAdditionalLegendColumns(self, headers: str, values: str) -> None:
        ...
    def GetComponentFilter(self, dependentVariableID: str) -> typing.List[CAE.PostScenarioVariantComponent]:
        ...
    Alias: str
    AmplitudeCorrectionFactor: float
    AxisScale: CAE.PostScenarioAxisScale
    CorrectionMode: CAE.PostScenarioCorrectionMode
    CustomizedDependentColumnName: str
    CustomizedFirstIndependentColumnName: str
    CustomizedSecondIndependentColumnName: str
    DisplayName: str
    Duplicate: bool
    EnergyCorrectionFactor: float
    FunctionClass: CAE.PostScenarioFunctionClass
    HighlightedDisplay: bool
    RecordNameHidden: bool
    SelectedComponent: CAE.PostScenarioVariantComponent
    SpectrumFormat: CAE.PostScenarioSpectrumFormat
    SpectrumMode: CAE.PostScenarioSpectrumMode
    VisualizationCorrectionMode: CAE.PostScenarioCorrectionMode
    VisualizationSpectrumMode: CAE.PostScenarioSpectrumMode
    VisualizationTemplate: str
    WeightingType: CAE.PostScenarioWeightingType


class PostScenarioMessageCollectorTable(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddTableRow(self, headerCells: str, cells: str) -> None:
        ...


class PostScenarioMessageCollector(TaggedObject):
    def __init__(self) -> None: ...
    def AddInformationLine(self, text: str) -> None:
        ...
    def AddHeading(self, text: str) -> None:
        ...
    def AddParagraph(self, text: str) -> None:
        ...
    def AddList(self, title: str, entries: str) -> None:
        ...
    def AddTableWithHeaderRow(self, title: str, headerColTitles: str, colTitles: str) -> CAE.PostScenarioMessageCollectorTable:
        ...
    def AddTable(self, title: str, numHeaderCols: int, numCols: int) -> CAE.PostScenarioMessageCollectorTable:
        ...
    def Warning(self, title: str, message: str) -> None:
        ...


class PostScenarioMeshNode(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Coordinates: Point3d
    Label: int


class PostScenarioMeshElement(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodeIndices(self) -> int:
        ...
    ElementType: CAE.ElementType
    Label: int


class PostScenarioMeshDefinitionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioMeshDefinition]:
        ...
    def __init__(self, owner: CAE.PostScenarioInputDefinition) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioMeshDefinition:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioMeshDefinition(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


class PostScenarioMesh(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.PostScenarioMeshElement]:
        ...


class PostScenarioManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def NewVariant(self) -> CAE.PostScenarioVariant:
        ...
    def NewVariantList(self) -> CAE.PostScenarioVariantList:
        ...
    def NewDoubleDataOnNodesOfElements(self) -> CAE.PostScenarioDoubleDataOnNodesOfElements:
        ...
    def NewComplexDataOnNodesOfElements(self) -> CAE.PostScenarioComplexDataOnNodesOfElements:
        ...
    def NewVariableDomain(self) -> CAE.PostScenarioVariableDomain:
        ...
    def NewPostScenarioParameters(self) -> CAE.PostScenarioParameters:
        ...
    def CheckValidDataSource(self, scenarioParameters: CAE.PostScenarioParameters) -> bool:
        """[Obsolete("Deprecated in NX1980.0.0.  No alternative provided for this method.")"""
        ...
    def CreatePostScenarioBuilderFromParameters(self, scenarioParameters: CAE.PostScenarioParameters) -> CAE.PostScenarioBuilder:
        ...
    def CreatePostScenarioBuilderFromViewport(self, viewportIndex: int) -> CAE.PostScenarioBuilder:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.PostScenarioManager.CreatePostScenarioBuilderFromScenario instead. Scenarios can be retrieved via NXOpen.CAE.PostScenarioManager.GetScenariosInViewport.")"""
        ...
    def CreatePostScenarioBuilderFromScenario(self, scenario: CAE.PostScenario) -> CAE.PostScenarioBuilder:
        ...
    def GetScenariosInViewport(self, viewportIndex: int) -> typing.List[CAE.PostScenario]:
        ...
    def CreateViewportSynchronizationOptions(self) -> CAE.ViewportSynchronizationOptions:
        ...
    def SetViewportSynchronizationOptions(self, options: CAE.ViewportSynchronizationOptions) -> None:
        ...
    def RemoveScenario(self, scenario: CAE.PostScenario) -> None:
        ...
    def CreateDemoScenarioDescriptors(self) -> None:
        ...
    def GetVisualizationCustomizationCollection(self, viewPortId: int) -> CAE.PostScenarioVisualizationCustomizationCollection:
        ...
    def Tag(self) -> Tag: ...

    PostScenarioDescriptors: CAE.PostScenarioDescriptorCollection
    AvailablePostScenarioDescriptors: CAE.PostScenarioAvailableDescriptorCollection
    DataSources: CAE.DataSourceCollection


class PostScenarioInputDefinitionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioInputDefinition]:
        ...
    def __init__(self, owner: CAE.PostScenarioDescriptor) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioInputDefinition:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioInputDefinition(TaggedObject):
    def __init__(self) -> None: ...
    Visualizations: CAE.PostScenarioVisualizationCollection
    MeshDefinitions: CAE.PostScenarioMeshDefinitionCollection
    Name: str


class PostScenarioFunctionClass(enum.Enum):
    Unknown = 0
    Spectrum = 1
    Time = 2
    FrequencyResponseFunctions = 3
    AutoPower = 4
    CrossPower = 5
    PowerSpectralDensity = 6


class PostScenarioDoubleDataOnNodesOfElements(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetValues(self) -> float:
        ...
    def SetValues(self, values: float) -> None:
        ...


class PostScenarioDescriptorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioDescriptor]:
        ...
    def __init__(self, owner: CAE.PostScenarioManager) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioDescriptor:
        ...
    def NewPostScenarioDescriptorBuilder(self) -> CAE.PostScenarioDescriptorBuilder:
        ...
    def DeleteUserScenario(self, descriptor: CAE.PostScenarioDescriptor) -> None:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioDescriptorBuilder(Builder):
    def __init__(self) -> None: ...
    def AddDescriptionCallback(self, cb: CAE.PostScenarioDescriptorBuilder.DescriptionCallback) -> None:
        ...
    def AddTransformationCallback(self, cb: CAE.PostScenarioDescriptorBuilder.TransformationCallback) -> None:
        ...
    def AddDeformationTransformationCallback(self, cb: CAE.PostScenarioDescriptorBuilder.DeformationTransformationCallback) -> None:
        ...
    def AddOrientationTransformationCallback(self, cb: CAE.PostScenarioDescriptorBuilder.OrientationTransformationCallback) -> None:
        ...
    def AddChoiceProviderCallback(self, name: str, cb: CAE.PostScenarioDescriptorBuilder.ChoiceProviderCallback) -> None:
        ...
    def AddSensitivityCallback(self, name: str, cb: CAE.PostScenarioDescriptorBuilder.SensitivityCallback) -> None:
        ...
    def AddDefaultMatchOverrideCallback(self, cb: CAE.PostScenarioDescriptorBuilder.OverrideMatchCallback) -> None:
        ...
    def AddDataDefinitionChangedOverrideCallback(self, cb: CAE.PostScenarioDescriptorBuilder.OverrideMatchCallback) -> None:
        ...
    def AddAggregationCallback(self, name: str, cb: CAE.PostScenarioDescriptorBuilder.AggregationCallback) -> None:
        ...
    def AddOverrideDefaultSelectionCallback(self, name: str, cb: CAE.PostScenarioDescriptorBuilder.OverrideDefaultSelectionCallback) -> None:
        ...
    XmlPath: str
    XmlText: str


    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

class PostScenarioDescriptor(TaggedObject):
    def __init__(self) -> None: ...
    def GetLicenseRequierments(self) -> str:
        ...
    InputDefinitions: CAE.PostScenarioInputDefinitionCollection
    Description: str
    Name: str
    UserDefined: bool


class PostScenarioDemoExportToUNV(CAE.PostScenarioAction):
    def __init__(self, ptr: int) -> None: ...
    File: str


class PostScenarioDefinition(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def PrintInformation(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    Name: str


class PostScenarioDataMatchOutput(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSlotDataSourceName(self, slotName: str) -> str:
        ...
    def GetSlotDataDefinitionName(self, slotName: str) -> str:
        ...
    def SetSlotDataSourceName(self, slotName: str, dataSourceName: str, dataDefinitionName: str) -> None:
        ...


class PostScenarioDataMatchesInput(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNamesOfPreferredDataSources(self) -> str:
        ...
    def GetSlotDataMatches(self, slotName: str) -> typing.List[CAE.PostScenarioDataMatch]:
        ...
    SelectedInputDefinitionName: str


class PostScenarioDataMatch(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetMatchedDependentVariables(self) -> typing.List[CAE.PostScenarioResultGroupVariable]:
        ...
    def GetMatchedIndependentVariables(self) -> typing.List[CAE.PostScenarioResultGroupVariable]:
        ...
    def GetMatchedSelectionVariables(self) -> typing.List[CAE.PostScenarioResultGroupVariable]:
        ...
    def GetVariableValues(self, variableName: str, defaultValue: CAE.PostScenarioVariant, values: typing.List[CAE.PostScenarioVariant]) -> None:
        ...
    DataDefinitionName: str
    DataSourceName: str


class PostScenarioDataDefinition(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


class PostScenarioCorrectionMode(enum.Enum):
    Unknown = 0
    Energy = 1
    Amplitude = 2


class PostScenarioCoordinateSystemType(enum.Enum):
    Rectangular = 0
    Cylindrical = 1
    Spherical = 2


class PostScenarioCoordinateSystem(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetCsysType(self) -> CAE.PostScenarioCoordinateSystemType:
        ...
    def SetCsysType(self, type: CAE.PostScenarioCoordinateSystemType) -> None:
        ...
    def GetOrigin(self) -> Vector3d:
        ...
    def SetOrigin(self, origin: Vector3d) -> None:
        ...
    def GetMatrix(self) -> Matrix3x3:
        ...
    def SetMatrix(self, matrix: Matrix3x3) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class PostScenarioConfigurationVariableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioConfigurationVariable]:
        ...
    def __init__(self, owner: CAE.PostScenarioSelectionParameters) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioConfigurationVariable:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioConfigurationVariableCallbackContext(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSlotDataMatch(self, slotName: str) -> CAE.PostScenarioDataMatch:
        ...
    InputDefinition: CAE.PostScenarioInputDefinition


class PostScenarioConfigurationVariable(TaggedObject):
    def __init__(self) -> None: ...
    def AssignBooleanValues(self, values: bool) -> None:
        ...
    def AssignIntegerValues(self, values: int) -> None:
        ...
    def AssignDoubleValues(self, values: float) -> None:
        ...
    def AssignComplexValues(self, values: typing.List[CAE.Complex]) -> None:
        ...
    def AssignStringValues(self, values: str) -> None:
        ...
    def AssignUnicodeStringValues(self, values: str) -> None:
        ...
    def AssignValues(self, values: typing.List[CAE.PostScenarioVariant]) -> None:
        ...
    def GetValues(self, values: typing.List[CAE.PostScenarioVariant]) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use CAE.PostScenarioConfigurationVariable.GetValues2 with a corrected signature instead.")"""
        ...
    def GetValues2(self) -> typing.List[CAE.PostScenarioVariant]:
        ...
    def GetAssignedValues(self) -> typing.List[CAE.PostScenarioVariant]:
        ...
    Name: str


class PostScenarioConfigurationGroupBuilder(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddMetadata(self, name: str, values: typing.List[CAE.PostScenarioVariant]) -> None:
        ...
    def Commit(self) -> None:
        ...


class PostScenarioConfigurationGroup(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetKeys(self) -> str:
        ...
    def GetValues(self, key: str) -> typing.List[CAE.PostScenarioVariant]:
        ...
    Name: str


class PostScenarioComponentType(enum.Enum):
    Scalar = 0
    Vector = 1
    SymmetricTensor = 2
    Symmetric2dTensor = 3
    PlyTensor = 4
    BeamForce = 5
    BeamMoment = 6
    RodForce = 7
    RodMoment = 8
    BarForce = 9
    BarMoment = 10
    ScalarSprinT = 11
    VectorSpring = 12
    Scalar3Components = 13
    Scalar6Components = 14


class PostScenarioComplexOption(enum.Enum):
    None = 0
    Real = 1
    Imaginary = 2
    Magnitude = 3
    Phase = 4
    SignedMagnitude = 5


class PostScenarioComplexDataOnNodesOfElements(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetValues(self) -> typing.List[CAE.Complex]:
        ...
    def SetValues(self, values: typing.List[CAE.Complex]) -> None:
        ...


class PostScenarioColorBarsCustomization(TaggedObject):
    def __init__(self) -> None: ...
    def GetRecordNameFields(self) -> str:
        ...
    def EnableRecordNameField(self, field: str) -> None:
        ...
    def DisableRecordNameField(self, field: str) -> None:
        ...
    def ResetRecordNamesToDefault(self) -> None:
        ...
    def GetNumberOfRecords(self) -> int:
        ...
    def GetFreeTexts(self) -> str:
        ...
    def SetFreeText(self, recordIndex: int, text: str) -> None:
        ...
    def EnableFreeText(self) -> None:
        ...
    def DisableFreeText(self) -> None:
        ...
    def GetSubviewportIndex(self) -> int:
        ...
    def GetName(self) -> str:
        ...
    def Update(self) -> None:
        ...


class PostScenarioBuilderSlotCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioDescriptor]:
        ...
    def __init__(self, owner: CAE.PostScenarioBuilder) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioBuilderSlot:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioBuilderSlot(Builder):
    def __init__(self) -> None: ...
    def GetDefinitions(self) -> typing.List[CAE.PostScenarioDefinition]:
        ...
    def GetAvailableDataSources(self) -> typing.List[CAE.DataSource]:
        ...
    def GetAvailableDefinitionsForDataSource(self, dataSource: CAE.DataSource) -> typing.List[CAE.PostScenarioDefinition]:
        ...
    def SetDataSource(self, dataSource: CAE.DataSource, dataDefinition: CAE.PostScenarioDefinition) -> None:
        ...
    def SetDataSource(self, dataSource: CAE.DataSource, dataDefinitions: typing.List[CAE.PostScenarioDefinition]) -> None:
        ...
    DataSource: CAE.DataSource
    Name: str


class PostScenarioBuilderDataDefinitionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioDataDefinition]:
        ...
    def __init__(self, owner: CAE.PostScenarioBuilder) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioDataDefinition:
        """[Obsolete("Deprecated in NX12.0.0.  Use CAE.PostScenarioDefinition instead.")"""
        ...
    def Tag(self) -> Tag: ...



class PostScenarioBuilder(Builder):
    def __init__(self) -> None: ...
    def NewPostScenarioSelectionParameters(self) -> CAE.PostScenarioSelectionParameters:
        ...
    def CheckSelectionParameters(self, parameters: CAE.PostScenarioSelectionParameters) -> bool:
        ...
    def SetSelectionParameters(self, parameters: CAE.PostScenarioSelectionParameters) -> None:
        ...
    def GetAvailableInputDefinitions(self) -> typing.List[CAE.PostScenarioInputDefinition]:
        ...
    def GetAvailableDataDefinitions(self) -> typing.List[CAE.PostScenarioDataDefinition]:
        """[Obsolete("Deprecated in NX12.0.0.  Use CAE.PostScenarioBuilderSlot.GetAvailableDefinitionsForDataSource instead.")"""
        ...
    def GetAvailableVisualizationDefinitions(self) -> typing.List[CAE.PostScenarioVisualizationDefinition]:
        ...
    def SetViewportIndex(self, viewportIndex: int) -> None:
        ...
    DataDefinitions: CAE.PostScenarioBuilderDataDefinitionCollection
    Slots: CAE.PostScenarioBuilderSlotCollection
    DataDefinition: CAE.PostScenarioDataDefinition
    InputDefinition: CAE.PostScenarioInputDefinition
    PlotType: CAE.PostScenarioPlotTypes
    Visualization: CAE.PostScenarioVisualizationDefinition


class PostScenarioAxisScale(enum.Enum):
    Default = 0
    Linear = 1
    Db = 2
    Log = 3


class PostScenarioAvailableDescriptorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioDescriptor]:
        ...
    def __init__(self, owner: CAE.PostScenarioManager) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioDescriptor:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioAggregationOutput(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def CreateAggregatedVariable(self, variableName: str, dataType: CAE.PostScenarioVariantType, domain: CAE.PostScenarioVariableDomain) -> None:
        ...
    def NewAggregateValue(self, aggregateValue: CAE.PostScenarioVariant) -> CAE.PostScenarioAggregateValueBuilder:
        ...
    def SetDefaultValue(self, defaultValue: CAE.PostScenarioVariant) -> None:
        ...


class PostScenarioAggregationInput(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetDependentVariables(self, slotVariableName: str) -> typing.List[CAE.PostScenarioResultGroupVariable]:
        ...
    def GetDataSourceVariable(self, slotVariableName: str) -> CAE.PostScenarioResultGroupVariable:
        ...
    def GetVariableValues(self, slotVariableName: str, defaultValue: CAE.PostScenarioVariant) -> typing.List[CAE.PostScenarioVariant]:
        ...
    def GetVariableValueAnnotations(self, slotVariableName: str) -> str:
        ...


class PostScenarioAggregateValueBuilder(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetDeaggregates(self, slotVariable: str, deaggregateValues: typing.List[CAE.PostScenarioVariant]) -> None:
        ...
    def Commit(self) -> None:
        ...


class PostScenarioAction(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Invoke(self) -> None:
        ...
    DisplayName: str
    Name: str
    Subvisualization: str


class PostScenario(NXObject):
    def __init__(self) -> None: ...
    def GetAvailableActions(self) -> typing.List[CAE.PostScenarioAction]:
        ...
    def GetActionByName(self, subvisualization: str, name: str) -> CAE.PostScenarioAction:
        ...
    def GetScenarioData(self) -> CAE.PostScenarioQueryResults:
        ...
    Plots: CAE.PostScenarioPlotHandleCollection
    Viewport: int
    Window: int


class PostResultRangeMethod(CAE.PostISmartSelectorMethod):
    def __init__(self, ptr: int) -> None: ...
    def GetEntities(self, resultEntities: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    IncludeVisibleEntitiesOnly: bool


class PostResultPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    AddCompanionNameToLoadCase: bool
    ImportUserGroups: bool
    ReadOneModeOrthogonalPair: bool


class PostResultNavigatorPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    Format: CAE.Post.Format
    SignificantPlaces: int


class PostRelatedNodesMethod(CAE.PostISmartSelectorMethod):
    def __init__(self, ptr: int) -> None: ...
    def GetEntities(self, resultEntities: typing.List[CAE.PostSelectionEntity]) -> None:
        ...


class PostRelatedElementsMethod(CAE.PostISmartSelectorMethod):
    def __init__(self, ptr: int) -> None: ...
    def GetEntities(self, resultEntities: typing.List[CAE.PostSelectionEntity]) -> None:
        ...


class PostProcessingSessionApplicator(Builder):
    def __init__(self) -> None: ...
    def SetFile(self, filePath: str) -> None:
        ...
    def SetApplyActiveLayoutState(self, apply: bool) -> None:
        ...
    def GetApplyActiveLayoutState(self) -> bool:
        ...
    def SetNthDataSourcePath(self, dataSourceIndex: int, sourcePath: str) -> None:
        ...
    def GetNthDataSourcePath(self, dataSourceIndex: int) -> str:
        ...
    def GetNumDataSources(self) -> int:
        ...
    def GetNthDataSourceName(self, dataSourceIndex: int) -> str:
        ...
    def SetCleanUpDataSources(self, doCleanDataSources: bool) -> None:
        ...
    def GetCleanUpDataSources(self) -> bool:
        ...
    def SetNthLoadingActions(self, dataSourceIndex: int, action: CAE.CaePostProcessingSessionApplicatorLoadAction) -> None:
        ...
    def GetNthLoadingActions(self, dataSourceIndex: int) -> CAE.CaePostProcessingSessionApplicatorLoadAction:
        ...


class PostProcessingSession(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Post) -> None: ...
    def CreateBuilder(self, part: BasePart) -> CAE.PostProcessingSessionApplicator:
        ...
    def ExportToFile(self, part: BasePart, filePath: str) -> None:
        ...
    def ExportToFileForValidation(self, part: BasePart, filePath: str) -> None:
        ...
    def ExportLayoutStatesListToSessionFile(self, file: str, layoutStatesToExport: typing.List[CAE.LayoutState]) -> None:
        ...
    def ExportLayoutStatesListForValidation(self, file: str, layoutStatesToExport: typing.List[CAE.LayoutState]) -> None:
        ...
    def GetExportedFilePath(self, part: BasePart) -> str:
        ...
    def GetActiveLayoutState(self, part: BasePart) -> CAE.LayoutState:
        ...
    def Tag(self) -> Tag: ...



class PostPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Post) -> None: ...
    def ApplyPreference(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    PostResultNavigatorPreference: CAE.PostResultNavigatorPreference
    PostIdentifyPreference: CAE.PostIdentifyPreference
    PostAnnotationPreference: CAE.PostAnnotationPreference
    PostLegendPreference: CAE.PostLegendPreference
    PostGraphPreference: CAE.PostGraphPreference
    PostResultPreference: CAE.PostResultPreference
    PostGeneralPreference: CAE.PostGeneralPreference
    PostViewportPreference: CAE.PostViewportPreference


class PostNMaxMinMethod(CAE.PostISmartSelectorMethod):
    def __init__(self, ptr: int) -> None: ...
    def GetEntities(self, resultEntities: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    IncludeVisibleEntitiesOnly: bool


class PostMeshCollector(TaggedObject):
    def __init__(self) -> None: ...
    def GetName(self) -> str:
        ...
    def GetPostMeshes(self) -> typing.List[CAE.PostMesh]:
        ...
    def GetPostMeshCollectors(self) -> typing.List[CAE.PostMeshCollector]:
        ...
    def GetCollectorType(self) -> CAE.PostMeshCollector.CollectorType:
        ...


    class CollectorType(enum.Enum):
        ElementFamilyZeroDimension = 0
        ElementFamilyOneDimension = 1
        ElementFamilyTwoDimension = 2
        ElementFamilyThreeDimension = 3
        AllElementFamilyOfFem = 4
        AllElementFamilyOfAfem = 5
        MeshCollector = 6
    

class PostMesh(TaggedObject):
    def __init__(self) -> None: ...
    CollectorId: int
    MaterialDescription: str
    MaterialId: int
    MaterialIdColor: int
    MeshColor: int
    MeshDimension: CAE.Result.GroupContainer
    Name: str
    NumElements: int
    Numelem: int
    PartId: int
    PropertyDescription: str
    PropertyId: int
    PropertyIdColor: int
    SuperelementId: int
    Type: int
    TypeDescription: str


class PostLegendPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    Format: CAE.Post.Format
    LegendCustomHeaderLines: CAE.PostCustomHeaderLines
    LegendHeaderDisplayStyle: CAE.PostHeader.DisplayStyle
    LegendMultipleOverlaysState: bool
    Position: CAE.Post.Position
    SignificantPlaces: int


class PostLegend(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetColorbarVisibility(self) -> bool:
        ...
    def SetColorbarVisibility(self, status: bool) -> None:
        ...
    def GetHeaderVisibility(self) -> bool:
        ...
    def SetHeaderVisibility(self, status: bool) -> None:
        ...
    def GetColorbar(self) -> CAE.PostColorbar:
        ...
    def SetColorbar(self, colorbar: CAE.PostColorbar) -> None:
        ...
    def GetHeader(self) -> CAE.PostHeader:
        ...
    def SetHeader(self, header: CAE.PostHeader) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class PostJtExportBuilder(Builder):
    def __init__(self) -> None: ...
    Component: CAE.Result.Component
    Jtdatasetname: str
    Jtfilename: str
    Layer: int
    Ply: int
    Result: CAE.Result
    ResultType: CAE.BaseResultType


class PostISmartSelectorMethod(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class PostIdentifyPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    Format: CAE.Post.Format
    SignificantPlaces: int


class PostHeader(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetCustomHeaderLines(self) -> CAE.PostCustomHeaderLines:
        ...
    def SetCustomHeaderLines(self, customheaderlines: CAE.PostCustomHeaderLines) -> None:
        ...
    def FreeResource(self) -> None:
        ...


    class DisplayStyle(enum.Enum):
        None = 0
        Default = 1
        Customized = 2
    

class PostGroupBuilder(Builder):
    def __init__(self) -> None: ...
    Label: int
    Name: str
    NeedCreateGroupInCurrentWorkPart: bool
    SelectionEntityList: CAE.PostSelectionEntityList


class PostGraphPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    GraphAutoSave: bool


class PostGraphOrbitBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEntityIds(self, entityIds: int) -> None:
        ...
    def SetFreePoints(self, freePoints: typing.List[Point3d]) -> None:
        ...
    def SetSelectionEntityObjects(self, selectionEntities: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    GraphTitle: str
    XresultComponent: CAE.Result.Component
    YresultComponent: CAE.Result.Component


class PostGraphBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEntityIds(self, isnodal: bool, entityIds: int) -> None:
        ...
    def SetFreePoints(self, freePoints: typing.List[Point3d]) -> None:
        ...
    def SetEntityObjects(self, entityObjs: typing.List[TaggedObject]) -> None:
        ...
    def SetSelectionEntityObjects(self, selectionEntities: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    def GetFieldTable(self) -> Fields.FieldTable:
        ...
    ComplexGraphTypes: CAE.Xyplot.ComplexOption2D
    CreateFieldOption: bool
    EdgeIntegralOptionValue: CAE.PostGraphBuilder.EdgeIntegralOption
    EvalutionErrorsOption: CAE.PostGraphBuilder.EvalutionErrors
    FaceIntegralOptionValue: CAE.PostGraphBuilder.FaceIntegralOption
    GeometryCombinationValue: CAE.PostGraphBuilder.GeometryValue
    GraphTitle: str
    IncompatibleResultOption: CAE.PostGraphBuilder.IncompatibleResult
    NoDataOption: CAE.PostGraphBuilder.DataErrorHandling
    NodalCombinationValue: CAE.PostGraphBuilder.NodalCombination
    SaveAfuOption: bool
    SelectedEntityType: CAE.PostGraphBuilder.EntityType
    UserData: float


    class NodalCombination(enum.Enum):
        Average = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
        None = 4
    

    class IncompatibleResult(enum.Enum):
        Skip = 0
        Abort = 1
    

    class GeometryValue(enum.Enum):
        Average = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
        WeightedAverage = 4
        Integral = 5
    

    class FaceIntegralOption(enum.Enum):
        Area = 0
        Volume = 1
    

    class EvalutionErrors(enum.Enum):
        Skip = 0
        UserValue = 1
        Abort = 2
    

    class EntityType(enum.Enum):
        Node = 0
        Element = 1
        Point = 2
        Edge = 3
        Face = 4
        Body = 5
        Group = 6
        SelectionRecipe = 7
    

    class EdgeIntegralOption(enum.Enum):
        Length = 0
        Area = 1
    

    class DataErrorHandling(enum.Enum):
        Skip = 0
        UserValue = 1
    

class PostGraphAlongPathBuilder(CAE.PostGraphBuilder):
    def __init__(self) -> None: ...
    def SetVector(self, unitvector: Point3d) -> None:
        ...
    def SetCsys(self, csys: Matrix3x3) -> None:
        ...
    def SetOrigin(self, origin: Point3d) -> None:
        ...
    def SetCsysType(self, csystype: CAE.PostGraphAlongPathBuilder.CsysType) -> None:
        ...
    CsysAxis: CAE.PostGraphAlongPathBuilder.CoordinateSysAxis
    DefineByPathOption: bool
    IncludeItersectionsOption: bool
    PathId: int
    QueryCurveUsageOptions: CAE.QueryCurveUsageOptions
    XaxisOption: CAE.PostGraphAlongPathBuilder.Xaxis


    class Xaxis(enum.Enum):
        IDs = 0
        PathLength = 1
        LengthAlongDirection = 2
        CoordinateValueOfCoordinateSystemAxis = 3
    

    class CsysType(enum.Enum):
        Cartesian = 0
        Cylindrical = 1
        Spherical = 2
    

    class CoordinateSysAxis(enum.Enum):
        FirstAxis = 0
        SecondAxis = 1
        ThirdAxis = 2
    

class PostGraphAcrossIterationsBuilder(CAE.PostGraphBuilder):
    def __init__(self) -> None: ...
    def SetStartIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    def SetEndIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    CombineAcrossEntities: bool
    CombineValueFromEntitiesOption: CAE.PostGraphAcrossIterationsBuilder.CombinationMethod
    CreateEntityLabelToggleValue: bool
    IterationStepSpacing: int
    IterationValueFilter: CAE.BaseIteration.IterationValueType
    IterationValueOption: CAE.PostGraphAcrossIterationsBuilder.IterationLabelingOption


    class IterationLabelingOption(enum.Enum):
        Value = 0
        Id = 1
    

    class CombinationMethod(enum.Enum):
        Average = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
        Difference = 4
        WeightedAverage = 5
        Integral = 6
        AbsoluteMinimum = 7
        AbsoluteMaximum = 8
        SignedAbsoluteMinimum = 9
        SignedAbsoluteMaximum = 10
        Rms = 11
        Rss = 12
        WeightedRMS = 13
        WeightedRSS = 14
    

class PostGraph(NXObject):
    def __init__(self) -> None: ...
    def Plot(self, windowIndex: int, viewIndex: int, overlay: bool) -> CAE.Xyplot.Plot:
        ...
    def Listgraphxydata(self) -> None:
        ...
    def Copyrecords(self, filename: str) -> None:
        ...
    def Editgraph(self) -> None:
        ...
    def Infoofgraph(self) -> None:
        ...
    def CreateTableField(self, tables: typing.List[NXObject]) -> None:
        ...


class PostGeneralPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    DistToMeshTolerance: float


class PostEnvironmentsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def GetPostEnvironmentOfType(self, postEnvironmentType: CAE.PostEnvironmentsManager.PostEnvironment) -> TaggedObject:
        ...
    def GetActivePostEnvironmentType(self) -> CAE.PostEnvironmentsManager.PostEnvironment:
        ...
    def Tag(self) -> Tag: ...

    Definition: CAE.PostEnvironmentsManager.DefinitionType
    PostEnvironmentType: CAE.PostEnvironmentsManager.PostEnvironment


    class PostEnvironment(enum.Enum):
        Standard = 0
        Acoustic = 1
    

    class DefinitionType(enum.Enum):
        Infer = 0
        UserDefined = 1
    

class PostEntitiesSelection(TaggedObject):
    def __init__(self) -> None: ...
    def GetSelectedEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    def SetSelectedEntities(self, entities: typing.List[TaggedObject]) -> None:
        ...
    FullResultModelType: CAE.PostEntitiesSelection.ResultModelType
    SelectionEntityType: CAE.PostEntitiesSelection.Type


    class Type(enum.Enum):
        FullResultModel = 0
        Nodes = 1
        Elements = 2
        Groups = 3
        SelectionRecipes = 4
    

    class ResultModelType(enum.Enum):
        FirstResult = 0
    

class PostDisplayManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Post) -> None: ...
    def SetVisibility(self, type: CAE.PostDisplayManager.ShowHideType, viewportID: int, isVisible: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



    class ShowHideType(enum.Enum):
        All = 0
        Legend = 1
        Annotations = 2
        MinAnnotations = 3
        MaxAnnotations = 4
        UserDefinedAnnotations = 5
        CoordinateSystem = 6
        Meshes = 7
        ZeroDimensionalMeshes = 8
        OneDimensionalMeshes = 9
        TwoDimensionalMeshes = 10
        ThreeDimensionalMeshes = 11
        SolidElement = 12
        Solid2DElement = 13
        Solid3DElement = 14
        ShellElement = 15
        Shell1DElement = 16
        Shell2DElement = 17
        MembraneElement = 18
        BeamElement = 19
        TrussElement = 20
        InfiniteElement = 21
        GapElement = 22
        JointElement = 23
        SpringDashPotElement = 24
        SpringDashPot0DElement = 25
        SpringDashPot1DElement = 26
        RigidElement = 27
        ConstraintElement = 28
        PlotElement = 29
        Plot1DElement = 30
        Plot2DElement = 31
        Plot3DElement = 32
        MassElement = 33
        InterElement = 34
        SuperElement = 35
        Number = 36
    

class PostCustomHeaderLines(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def InsertNthLine(self, index: int, line: typing.List[CAE.PostCustomHeaderLines.HeaderToken]) -> None:
        ...
    def GetNumLines(self) -> int:
        ...
    def GetNthLine(self, index: int) -> typing.List[CAE.PostCustomHeaderLines.HeaderToken]:
        ...
    def DeleteNthLine(self, index: int) -> None:
        ...
    def ClearLines(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...


    class Token(enum.Enum):
        AbsoluteValue = 0
        BeamCsys = 1
        BeamSection = 2
        Combination = 3
        Complex = 4
        Component = 5
        CrossSectionViewBeamInfo = 6
        Csys = 7
        Deformation = 8
        DisplayedMinMax = 9
        Formula = 10
        Iteration = 11
        Loadcase = 12
        ModelSummary = 13
        PlyIdAndLayer = 14
        Result = 15
        ResultEnvironment = 16
        ResultMinMax = 17
        Scale = 18
        ShellSection = 19
        Solution = 20
        Subcase = 21
        StreamlineData = 22
        Unit = 23
        Usertext = 24
    

    class PostCustomHeaderLinesHeaderToken():
        EnumToken: CAE.PostCustomHeaderLines.Token
        UserText: str
        def ToString(self) -> str:
            ...
        def __init__(self, EnumToken: CAE.PostCustomHeaderLines.Token, UserText: str) -> None: ...
    

    class PostCustomHeaderLines_HeaderToken():
        enumToken: CAE.PostCustomHeaderLines.Token
        userText: int
    

class PostCoordinateSystem(TaggedObject):
    def __init__(self) -> None: ...
    def GetCoordinateSystemType(self) -> CAE.PostCoordinateSystem.CoordinateSystemType:
        ...
    def SetCoordinateSystemType(self, coordinateSystemType: CAE.PostCoordinateSystem.CoordinateSystemType) -> None:
        ...
    def GetCsysOrientation(self) -> Matrix3x3:
        ...
    def SetCsysOrientation(self, val: Matrix3x3) -> None:
        ...
    def GetCsysOrigin(self) -> Point3d:
        ...
    def SetCsysOrigin(self, val: Point3d) -> None:
        ...


    class CoordinateSystemType(enum.Enum):
        Cartesian = 0
        Cylindrical = 1
        Spherical = 2
    

class PostColorbarValueParameters(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetSpacing(self) -> CAE.PostColorbarValueParameters.Spacing:
        ...
    def SetSpacing(self, spacing: CAE.PostColorbarValueParameters.Spacing) -> None:
        ...
    def GetExtreme(self) -> CAE.PostColorbarValueParameters.Extreme:
        ...
    def SetExtreme(self, extreme: CAE.PostColorbarValueParameters.Extreme) -> None:
        ...
    def GetExtremeMinimum(self) -> float:
        ...
    def SetExtremeMinimum(self, minimum: float) -> None:
        ...
    def GetExtremeMaximum(self) -> float:
        ...
    def SetExtremeMaximum(self, maximum: float) -> None:
        ...
    def GetScale(self) -> CAE.PostColorbarValueParameters.Scale:
        ...
    def SetScale(self, scale: CAE.PostColorbarValueParameters.Scale) -> None:
        ...
    def GetNumLevels(self) -> int:
        ...
    def SetNumLevels(self, numlevels: int) -> None:
        ...
    def GetIncrementPerLevel(self) -> float:
        ...
    def SetIncrementPerLevel(self, incrementperlevel: float) -> None:
        ...
    def GetCustomOverwriteValue(self) -> bool:
        ...
    def SetCustomOverwriteValue(self, customoverwritevalue: bool) -> None:
        ...
    def GetValueRange(self) -> float:
        ...
    def SetValueRange(self, valuerange: float) -> None:
        ...
    def FreeResource(self) -> None:
        ...


    class Spacing(enum.Enum):
        EquallySpaced = 0
        RoundOff = 1
        LevelIncrement = 2
    

    class Scale(enum.Enum):
        Automatic = 0
        Linear = 1
        Logarithmic = 2
    

    class Extreme(enum.Enum):
        Result = 0
        Displayed = 1
        Specified = 2
        ViewportResult = 3
        ViewportDisplayed = 4
    

class PostColorbarUnderFlowOverFlowParameters(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetOverflowAboveColor(self) -> NXColor:
        ...
    def SetOverflowAboveColor(self, colorId: NXColor) -> None:
        ...
    def GetUnderflowBelowColor(self) -> NXColor:
        ...
    def SetUnderflowBelowColor(self, colorId: NXColor) -> None:
        ...
    def GetOverflowDisplayStyle(self) -> CAE.PostColorbarUnderFlowOverFlowParameters.LimitDisplay:
        ...
    def SetOverflowDisplayStyle(self, overflow: CAE.PostColorbarUnderFlowOverFlowParameters.LimitDisplay) -> None:
        ...
    def GetUnderflowDisplayStyle(self) -> CAE.PostColorbarUnderFlowOverFlowParameters.LimitDisplay:
        ...
    def SetUnderflowDisplayStyle(self, underflow: CAE.PostColorbarUnderFlowOverFlowParameters.LimitDisplay) -> None:
        ...
    def GetOverflowAboveVisibility(self) -> bool:
        ...
    def SetOverflowAboveVisibility(self, showoverflowabove: bool) -> None:
        ...
    def GetUnderflowBelowVisibility(self) -> bool:
        ...
    def SetUnderflowBelowVisibility(self, showunderflowbelow: bool) -> None:
        ...
    def FreeResource(self) -> None:
        ...


    class LimitDisplay(enum.Enum):
        None = 0
        Shaded = 1
        Translucent = 2
        Clipped = 3
    

class PostColorbarColorParameters(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetSpectrum(self) -> CAE.PostColorbarColorParameters.Spectrum:
        ...
    def SetSpectrum(self, spectrum: CAE.PostColorbarColorParameters.Spectrum) -> None:
        ...
    def GetInvertSpectrum(self) -> bool:
        ...
    def SetInvertSpectrum(self, invertspectrum: bool) -> None:
        ...
    def GetCustomOverwriteColor(self) -> bool:
        ...
    def SetCustomOverwriteColor(self, customoverwritecolor: bool) -> None:
        ...
    def GetColorRange(self) -> int:
        ...
    def SetColorRange(self, colorrange: int) -> None:
        ...
    def FreeResource(self) -> None:
        ...


    class Spectrum(enum.Enum):
        Structural = 0
        Thermal = 1
        GrayScale = 2
        StopLight = 3
    

class PostColorbar(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetColorParameters(self) -> CAE.PostColorbarColorParameters:
        ...
    def SetColorParameters(self, params: CAE.PostColorbarColorParameters) -> None:
        ...
    def GetValueParameters(self) -> CAE.PostColorbarValueParameters:
        ...
    def SetValueParameters(self, params: CAE.PostColorbarValueParameters) -> None:
        ...
    def GetUnderFlowOverFlowParameters(self) -> CAE.PostColorbarUnderFlowOverFlowParameters:
        ...
    def SetUnderFlowOverFlowParameters(self, params: CAE.PostColorbarUnderFlowOverFlowParameters) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class PostAnnotationPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    FontScaling: bool
    Format: CAE.Post.Format
    ScaleFactor: float
    SignificantPlaces: int


class PostAnnotationBuilder(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetAnnotationType(self, type: CAE.PostAnnotationBuilder.Type) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    def SetElements(self, elementIds: int) -> None:
        ...
    def SetNodes(self, nodeIds: int) -> None:
        ...
    def SetEdgeFace(self, subIds: int) -> None:
        ...
    def SetResults(self, results: typing.List[CAE.Result]) -> None:
        ...
    def SetSectors(self, sectorIds: int) -> None:
        ...
    def SetSectionAngles(self, sectionAngles: float) -> None:
        ...
    def SetNumMinMax(self, numMinMax: int) -> None:
        ...
    def SetUpdateEntityOnResultChange(self, update: bool) -> None:
        ...
    def SetCoordinate(self, xcord: float, ycord: float) -> None:
        ...
    def SetUsertext(self, usertext: str) -> None:
        ...
    def CommitAnnotation(self) -> CAE.PostAnnotation:
        ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    def SetGroupRefrenceName(self, refGroupName: str) -> None:
        ...
    def GetCombineOption(self) -> CAE.PostAnnotation.CombineOption:
        ...
    def SetCombineOption(self, combineOption: CAE.PostAnnotation.CombineOption) -> None:
        ...


    class Type(enum.Enum):
        Entity = 0
        Min = 1
        Max = 2
        Userloc = 3
    

class PostAnnotation(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    def Draw(self) -> None:
        ...
    def Show(self, show: bool) -> None:
        ...
    def SetUserText(self, usertext: str) -> None:
        ...
    def GetUserText(self, usertext: str) -> None:
        ...
    def UpdateAnnotation(self) -> None:
        ...
    def SetReferenceGroup(self, newRefgroupName: str) -> None:
        ...
    BoxColor: NXColor
    BoxFill: bool
    BoxTextAlignment: CAE.PostAnnotation.TextAlignment
    BoxTranluceny: bool
    BoxTranslucency: bool
    DisplayStyle: CAE.PostAnnotation.Style
    DisplayUnit: bool
    DisplayValueType: CAE.PostAnnotation.ValueType
    DrawBox: bool
    Name: str
    TextColor: NXColor


    class ValueType(enum.Enum):
        None = 0
        ResultAndEntity = 1
        Result = 2
        Entity = 3
    

    class TextAlignment(enum.Enum):
        Left = 0
        Right = 1
        Center = 2
    

    class Style(enum.Enum):
        Box = 0
        BoxWithLeader = 1
        BoxAtModelLocation = 2
    

    class CombineOption(enum.Enum):
        None = 0
        ArithmeticMean = 1
        Sum = 2
    

class Post3DGraphBuilder(CAE.PostGraphBuilder):
    def __init__(self) -> None: ...
    def SetStartIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    def SetEndIteration(self, iteration: CAE.BaseIteration) -> None:
        ...


class Post(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetPostviewIds(self) -> int:
        ...
    def LoadImportedResult(self, resultName: str, fileName: str, units: typing.List[Unit]) -> int:
        ...
    def LoadSolutionResult(self, solution: CAE.SimSolution) -> int:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.ResultManager.CreateSolutionResult instead.")"""
        ...
    def LoadRaEventResult(self, raEvent: CAE.ResponseSimulation.RSEvent) -> int:
        ...
    def UnloadResultFile(self, fileName: str) -> None:
        ...
    def UnloadResult(self, resultId: int) -> None:
        ...
    def UpdateUserGroupsFromSimPart(self, simpart: CAE.SimPart) -> None:
        ...
    def CreatePostview(self, viewIndex: int, resultId: int, overlay: bool) -> int:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.Post.CreatePostview instead.")"""
        ...
    def CreateNewPostview(self, viewIndex: int, resultId: int, overlay: bool, colorscheme: CAE.Post.DisplayColorSchemeType) -> int:
        ...
    def CreatePostviewForResult(self, viewIndex: int, resultId: int, overlay: bool, result: CAE.Result.ResultParameters) -> int:
        """[Obsolete("Deprecated in NX7.5.1.  Use NXOpen.CAE.Post.CreatePostviewForResult instead.")"""
        ...
    def CreateNewPostviewForResult(self, viewIndex: int, resultId: int, overlay: bool, result: CAE.Result.ResultParameters, colorscheme: CAE.Post.DisplayColorSchemeType) -> int:
        ...
    def CreateCrossSectionViewForResult(self, viewIndex: int, resultId: int, result: CAE.CrossSectionParameters) -> int:
        ...
    def DeleteViewport(self, viewIndex: int) -> None:
        ...
    def PostviewRename(self, postviewId: int, newName: str) -> None:
        ...
    def PostviewDelete(self, postviewId: int) -> None:
        ...
    def PostviewSetCurrentInOverlay(self, postviewId: int) -> None:
        ...
    def PostviewAnimationPlay(self, postviewId: int, animation: CAE.Post.Animation) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.Post.PostviewAnimationPlay instead.")"""
        ...
    def PostviewAnimationControl(self, postviewId: int, control: CAE.Post.AnimationControl, frame: int, fullCycle: bool, delay: int) -> None:
        ...
    def PostviewAnimationControlStreamline(self, postviewId: int, control: CAE.Post.AnimationStreamline) -> None:
        ...
    def PostviewAnimationVectorDisplaySizeControl(self, postviewId: int, vectorDisplaySizeControl: bool) -> None:
        ...
    def PostviewMarkerOnOff(self, postviewId: int, showMarker: bool) -> None:
        ...
    def PostviewApplyTemplate(self, postviewId: int, templateId: int) -> None:
        ...
    def PostviewApplyTemplateFile(self, postviewId: int, xmlFileName: str) -> None:
        ...
    def PostviewApplyShowAll(self, postviewId: int) -> None:
        ...
    def PostviewApplyGroupContainerVisibility(self, postviewId: int, container: CAE.Result.GroupContainer, visibility: bool) -> None:
        ...
    def PostviewApplySEVisibility(self, postviewId: int, superelementId: int, visibility: bool) -> None:
        ...
    def PostviewApplySERepresentation(self, postviewId: int, superelementId: int, representation: CAE.Result.SuperElementRep) -> None:
        ...
    def PostviewApplySERepresentation(self, postviewId: int, superelementIds: int, representation: CAE.Result.SuperElementRep) -> None:
        ...
    def PostviewApplyAllSEVis(self, pvid: int, visibility: bool) -> None:
        ...
    def PostviewAskSERepresentations(self, postviewId: int, superelementId: int, representation: typing.List[CAE.Result.SuperElementRep]) -> None:
        ...
    def PostviewApplyGroupContainerVisibility(self, postviewId: int, result: CAE.Result, container: CAE.Result.GroupContainer, visibility: bool) -> None:
        ...
    def PostviewApplyGroupContainerVisibility(self, postviewId: int, container: typing.List[CAE.Result.GroupContainer], visibility: bool) -> None:
        ...
    def PostviewApplyGroupContainerVisibility(self, postviewId: int, result: CAE.Result, container: typing.List[CAE.Result.GroupContainer], visibility: bool) -> None:
        ...
    def PostviewApplyGroupVisibility(self, postviewId: int, container: CAE.Result.GroupContainer, group: int, visibility: bool) -> None:
        ...
    def PostviewApplyGroupVisibility(self, postviewId: int, resultId: int, container: CAE.Result.GroupContainer, group: int, visibility: bool) -> None:
        ...
    def PostviewApplyGroupVisibility(self, postviewId: int, container: typing.List[CAE.Result.GroupContainer], group: int, visibility: bool) -> None:
        ...
    def PostviewApplyGroupVisibility(self, postviewId: int, resultId: int, container: typing.List[CAE.Result.GroupContainer], group: int, visibility: bool) -> None:
        ...
    def PostviewApplyCsysContainerVisibility(self, postviewId: int, visibility: bool) -> None:
        ...
    def PostviewApplyCsysVisibility(self, postviewId: int, id: int, visibility: bool) -> None:
        ...
    def PostviewApplyUserGroupVisibility(self, postviewId: int, usergroupIds: int, visibility: CAE.Post.GroupVisibility) -> None:
        ...
    def PostviewApplyUserGroupVisibility(self, postviewId: int, result: CAE.Result, usergroupIds: int, visibility: CAE.Post.GroupVisibility) -> None:
        ...
    def PostviewApplyUserGroupVisibility(self, postviewId: int, results: typing.List[CAE.Result], usergroupIds: int, visibility: CAE.Post.GroupVisibility) -> None:
        ...
    def PostviewGetUserGroupGids(self, postviewId: int, usergroupNames: str, usergroupsGids: int) -> None:
        ...
    def PostviewSetStyle(self, postviewId: int, showStyle: int, style: CAE.Post.Style) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.Post.PostviewSetStyle instead.")"""
        ...
    def PostviewSetStyle(self, postviewId: int, showStyle: int, style: CAE.Post.PlotStyle) -> None:
        ...
    def PostviewSetColorbarStyle(self, postviewId: int, colorbarStyle: CAE.Post.ColorbarStyle) -> None:
        ...
    def PostViewSetColorScheme(self, postviewId: int, colorScheme: CAE.Post.DisplayColorSchemeType) -> None:
        ...
    def PostviewSetTarget(self, postviewId: int, target: CAE.Post.Target) -> None:
        ...
    def PostviewSetResult(self, postviewId: int, result: CAE.Result.ResultParameters) -> None:
        """[Obsolete("Deprecated in NX7.5.1.  Use NXOpen.CAE.Post.PostviewSetResult instead.")"""
        ...
    def PostviewSetBandStyle(self, postviewId: int, bandstyle: CAE.Post.BandStyle) -> None:
        ...
    def CrossSectionViewSetResult(self, postviewId: int, result: CAE.CrossSectionParameters) -> None:
        ...
    def PostviewSetDeformation(self, postviewId: int, deformation: CAE.Result.DeformationParameters) -> None:
        """[Obsolete("Deprecated in NX7.5.1.  Use NXOpen.CAE.Post.PostviewSetDeformation instead.")"""
        ...
    def PostviewSetStreamlineVelocity(self, postviewId: int, velocity: CAE.Result.VelocityParameters) -> None:
        """[Obsolete("Deprecated in NX7.5.1.  Use NXOpen.CAE.Post.PostviewSetStreamlineVelocity instead.")"""
        ...
    def PostviewSetStreamlineSeedSet(self, postviewId: int, seedsetId: int) -> None:
        ...
    def PostviewSetMark(self, postviewId: int, mark: CAE.Post.Mark) -> None:
        ...
    def PostviewSetStreamline(self, postviewId: int, streamline: CAE.Post.Streamline) -> None:
        ...
    def PostviewSetDeformed(self, postviewId: int, deformed: bool) -> None:
        ...
    def PostviewSetUndeformed(self, postviewId: int, undeformed: bool) -> None:
        ...
    def PostviewSetColorDisplayDeformationSynchronization(self, postviewId: int, synchronization: bool) -> None:
        ...
    def PostviewSetDeformedUndeformedSynchronization(self, postviewId: int, showDeformedPrimaryDisplay: bool, showUndeformedModel: bool, synchronizeLoadCaseAndIteration: bool) -> None:
        ...
    def PostviewSetColorbar(self, postviewId: int, colorbar: CAE.Post.Colorbar) -> None:
        ...
    def PostviewSetColorbar(self, postviewId: int, colorbar: CAE.Post.Colorbar, customOverwrite: bool, rangeValue: float, rangeColors: typing.List[NXColor.Rgb]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.Post.PostviewSetColorbar and NXOpen.CAE.Post.PostviewSetColorbar instead.")"""
        ...
    def PostviewSetColorbar(self, postviewId: int, colorbar: CAE.Post.Colorbar, customOverwriteValue: bool, customOverwriteColor: bool, rangeValue: float, rangeColors: typing.List[NXColor.Rgb]) -> None:
        ...
    def PostviewGetColorbar(self, postviewId: int, customOverwrite: int) -> CAE.Post.Colorbar:
        ...
    def PostviewGetColorbarWithCustomOptions(self, postviewId: int, customOverwriteValue: bool, customOverwriteColor: bool) -> CAE.Post.Colorbar:
        ...
    def PostviewSetShowHeader(self, postviewId: int, showHeader: CAE.Post.ShowHeader) -> None:
        ...
    def PostviewSetHeaderlines(self, postviewId: int, headerlines: typing.List[CAE.Post.Headerlines]) -> None:
        ...
    def PostviewGetShowHeader(self, postviewId: int) -> CAE.Post.ShowHeader:
        ...
    def PostviewSetLegend(self, postviewId: int, showLegend: bool, legend: CAE.Post.Legend) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.CAE.Post.PostviewSetShowHeader and NXOpen.CAE.Post.PostviewSetColorbar instead.")"""
        ...
    def PostviewSetEdgeFace(self, postviewId: int, primaryEdgeface: CAE.Post.EdgeFace, undeformedEdgeface: CAE.Post.EdgeFace) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.Post.PostviewSetEdgeFace instead.")"""
        ...
    def PostviewSetEdgeFace(self, postviewId: int, edgeface: CAE.Post.EdgeFace) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.Post.PostviewSetEdgeFace instead.")"""
        ...
    def CrossSectionViewSetLockRotation(self, postviewId: int, lockRotation: bool) -> None:
        ...
    def PostviewSetText(self, postviewId: int, text: CAE.Post.Text) -> None:
        ...
    def PostviewGetText(self, postviewId: int) -> CAE.Post.Text:
        ...
    def PostviewSetFormat(self, postviewId: int, format: CAE.Post.Format, numdecimal: int) -> None:
        ...
    def PostviewGetFormat(self, postviewId: int, format: CAE.Post.Format, numdecimal: int) -> None:
        ...
    def PostviewSetPosition(self, postviewId: int, position: CAE.Post.Position) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Set NXOpen.CAE.PostPreference Position set through post preferences instead.")"""
        ...
    def PostviewSetMarker(self, postviewId: int, showMarker: bool, marker: CAE.Post.Marker) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Set NXOpen.CAE.PostAnnotation show hide instead.")"""
        ...
    def PostviewSetAnnotationBox(self, postviewId: int, annotationBox: CAE.Post.AnnotationBox) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Set NXOpen.CAE.PostAnnotation Display Attribute directly instead.")"""
        ...
    def PostviewSetFontSize(self, postviewId: int, autoFontSize: bool, fontScale: float) -> None:
        ...
    def PostviewGetFontSize(self, postviewId: int, autoFontSize: int, fontScale: float) -> None:
        ...
    def PostviewSetAxisymmetric(self, postviewId: int, axisymmetric: CAE.Post.Axisymmetric) -> None:
        ...
    def PostviewSetClipping(self, postviewId: int, clipping: CAE.Post.Clipping) -> None:
        """[Obsolete("Deprecated in NX7.5.1.  Use NXOpen.CAE.Post.PostviewSetClipping instead.")"""
        ...
    def PostviewSetLighting(self, postviewId: int, lighted: bool) -> None:
        ...
    def PostviewSetCompression(self, postviewId: int, compress: bool, featureangle: float, banddifference: float) -> None:
        ...
    def PostviewSetClipping(self, postviewId: int, clipping: CAE.ClippingParameters) -> None:
        ...
    def PostviewSetGroupContainerVisibility(self, postviewId: int, container: CAE.Result.GroupContainer, visibility: bool) -> None:
        ...
    def PostviewSetGroupVisibility(self, postviewId: int, container: CAE.Result.GroupContainer, group: int, visibility: bool) -> None:
        ...
    def PostviewUpdate(self, postviewId: int) -> None:
        ...
    def PostviewCaptureAnimatedGif(self, postviewId: int, fileName: str, includeOverlayedPostviews: bool, whiteBackground: bool) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  use NXOpen.CAE.Post.PostviewCaptureAllViewportsToGif for multiple animations.")"""
        ...
    def PostviewExportDisplay(self, postviewId: int, fileName: str, format: CAE.Post.Export, ignoreClipping: bool, ignoreVisibility: bool) -> None:
        ...
    def PostviewSaveTemplate(self, postviewId: int) -> int:
        ...
    def PostviewExportTemplate(self, postviewId: int, xmlFileName: str) -> None:
        ...
    def PostviewSetCriticalPlyIdDisplay(self, postviewId: int, displayCriticalPlies: bool) -> None:
        ...
    def PostviewSetCriticalLayerIdDisplay(self, postviewId: int, displayCriticalLayers: bool) -> None:
        ...
    def PostviewSetCriticalLoadIdDisplay(self, postviewId: int, displayCriticalLoads: bool) -> None:
        ...
    def CreateUserGroupFromEntityLabels(self, postviewId: int, entityType: CAE.CaeGroupCollection.EntityType, labels: int) -> int:
        ...
    def CreateUserGroupFromEntityLabels(self, postviewId: int, result: CAE.Result, entityType: CAE.CaeGroupCollection.EntityType, labels: int) -> int:
        ...
    def UserGroupRename(self, usergroupId: int, newName: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  use NXOpen.CAE.Post.UserGroupRename with resulttag.")"""
        ...
    def UserGroupDelete(self, usergroupId: int) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  use NXOpen.CAE.Post.UserGroupDelete with resulttag.")"""
        ...
    def CreateStreamlineSeedSet(self, postviewId: int, name: str, seeds: typing.List[CAE.Post.StreamlineSeed]) -> int:
        ...
    def StreamlineSeedSetDelete(self, seedsetId: int) -> None:
        ...
    def CreatePathFromNodeIds(self, postviewId: int, name: str, nodeIds: int) -> int:
        """[Obsolete("Deprecated in NX11.0.0.  use NXOpen.CAE.ResultManager.CreateQueryCurvePost with nodes, elements or free points.")"""
        ...
    def CreatePathFromElemIds(self, postviewId: int, name: str, elemIds: int) -> int:
        """[Obsolete("Deprecated in NX11.0.0.  use NXOpen.CAE.ResultManager.CreateQueryCurvePost with nodes, elements or free points.")"""
        ...
    def CreatePathFromPoints(self, postviewId: int, name: str, points: float, numberOfInsertPointsPerSegment: int) -> int:
        """[Obsolete("Deprecated in NX11.0.0.  use NXOpen.CAE.ResultManager.CreateQueryCurvePost with nodes, elements or free points.")"""
        ...
    def PathDelete(self, pathId: int) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  use NXOpen.CAE.ResultManager.DeleteQueryCurve to delete the query curves")"""
        ...
    def CreateSpatialGraph(self, postviewId: int, name: str, graph: CAE.Post.GraphParameters, pathId: int) -> CAE.Post.GraphIds:
        ...
    def CreateHistoryGraph(self, postviewId: int, name: str, graph: CAE.Post.GraphParameters, startIteration: int, endIteration: int, iterationIncrement: int, nodeLabel: int, point: float) -> CAE.Post.GraphIds:
        ...
    def PlotGraph(self, viewIndex: int, graphIds: CAE.Post.GraphIds, overlay: bool) -> None:
        ...
    def GraphDelete(self, graphIds: CAE.Post.GraphIds) -> None:
        ...
    def TemplateDelete(self, templateId: int) -> None:
        ...
    def TemplateRename(self, templateId: int, newName: str) -> None:
        ...
    def TemplateSearch(self, name: str) -> int:
        ...
    def TemplateSetAsDefault(self, templateId: int) -> None:
        ...
    def DeleteAllTemplates(self) -> None:
        ...
    def LoadTemplate(self, filename: str, name: str, templateId: int) -> str:
        ...
    def ReloadTemplates(self) -> None:
        ...
    def SetFactoryDefaultTemplate(self) -> None:
        ...
    def CompareDisplayFiles(self, benchmarkFileName: str, testFileName: str, tolerances: CAE.Post.ASCIIDiffTolerances) -> str:
        ...
    def CreatePostview(self, viewIndex: int, result: CAE.Result, overlay: bool) -> int:
        ...
    def CreateNewPostview(self, viewIndex: int, result: CAE.Result, overlay: bool, colorscheme: CAE.Post.DisplayColorSchemeType) -> int:
        ...
    def CreatePostviewForResult(self, viewIndex: int, result: CAE.Result, overlay: bool, resultParamter: CAE.ResultParameters) -> int:
        ...
    def CreateNewPostviewForResult(self, viewIndex: int, result: CAE.Result, overlay: bool, resultParamter: CAE.ResultParameters, colorscheme: CAE.Post.DisplayColorSchemeType) -> int:
        ...
    def GetResultForPostview(self, postviewId: int, result: CAE.Result, resultParamter: CAE.ResultParameters) -> None:
        ...
    def CreatePostviewsForResultAndSE(self, viewIndex: int, result: CAE.Result, resultParamter: CAE.ResultParameters, postviewIds: int) -> None:
        ...
    def PostviewSetResult(self, postviewId: int, resultParamter: CAE.ResultParameters) -> None:
        ...
    def PostviewSetDeformation(self, postviewId: int, deformation: CAE.DeformationParameters) -> None:
        ...
    def PostviewSetStreamlineVelocity(self, postviewId: int, velocity: CAE.BaseResultType) -> None:
        ...
    def CreateAnnotation(self, postviewId: int, name: str, num: int, max: bool, usertext: str) -> CAE.PostAnnotation:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.PostAnnotationBuilder instead.")"""
        ...
    def CreateAnnotation(self, postviewId: int, name: str, entities: int, subEntities: int, usertext: str) -> CAE.PostAnnotation:
        """[Obsolete("Deprecated in NX9.0.0.  use NXOpen.CAE.Post.CreateAnnotation with extra face parameter.")"""
        ...
    def CreateAnnotation(self, postviewId: int, name: str, elements: int, nodes: int, elmedgeface: int, usertext: str) -> CAE.PostAnnotation:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.PostAnnotationBuilder instead.")"""
        ...
    def CreateAnnotation(self, postviewId: int, name: str, xcoord: float, ycoord: float, usertext: str) -> CAE.PostAnnotation:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.PostAnnotationBuilder instead.")"""
        ...
    def GetAnnotations(self, postviewId: int, annotation: typing.List[CAE.PostAnnotation]) -> None:
        ...
    def Plotgraphs(self, windowIndex: int, viewIndex: int, graphs: typing.List[CAE.PostGraph], overlay: bool) -> CAE.Xyplot.Plot:
        ...
    def Deletegraphs(self, graphs: typing.List[CAE.PostGraph]) -> None:
        ...
    def CreatePostview(self, viewIndex: int, probeparams: CAE.ResultParametersWithProbe, overlay: bool) -> int:
        ...
    def PostviewSetResultWithProbe(self, postviewId: int, probeparams: CAE.ResultParametersWithProbe) -> None:
        ...
    def PostviewCreateClone(self, postviewId: int, viewIndex: int) -> int:
        ...
    def PostviewAnimationPlay(self, postviewId: int, animation: CAE.Post.AnimationParameters) -> None:
        ...
    def UserGroupRename(self, result: CAE.Result, usergroupId: int, newName: str) -> None:
        ...
    def UserGroupDelete(self, result: CAE.Result, usergroupId: int) -> None:
        ...
    def CreateAnnotationBuilder(self, pvid: int) -> CAE.PostAnnotationBuilder:
        ...
    def GetElemsVisibility(self, pvid: int, includeOrExculdes: bool) -> int:
        ...
    def GetClipLocations(self, pvid: int, cutinfos: typing.List[CAE.PostSelectionEntity]) -> None:
        ...
    def CreatePostShowhideBuilder(self, pvid: int) -> CAE.PostShowhideBuilder:
        ...
    def PostviewSetMeshTransparency(self, pvid: int, meshes: typing.List[CAE.PostMesh], isTransparent: bool) -> None:
        ...
    def PostviewSetGlobalTranslucency(self, pvid: int, isTranslucent: bool) -> None:
        ...
    def CreatePostview(self, viewIndex: int, nodalforcereportparams: CAE.ResultParametersWithNodalForceReport) -> int:
        """[Obsolete("Deprecated in NX1953.0.0.  use NXOpen.CAE.Post.JA_SPP_CreatePostviewFromNodalForceReportParameters instead.")"""
        ...
    def PostviewSetResultWithNodalForceReport(self, postviewId: int, nodalforcereportparams: CAE.ResultParametersWithNodalForceReport) -> None:
        ...
    def PostviewSetEdgeFace(self, postviewId: int, primaryEdgeface: CAE.Post.PrimaryEdgeFace, undeformedEdgeface: CAE.Post.EdgeFace) -> None:
        ...
    def PostviewSetEdgeFace(self, postviewId: int, primaryEdgeface: CAE.Post.PrimaryEdgeFace) -> None:
        ...
    def PostviewCalculateDistanceBetweenEntities(self, pvid: int, postSel1: CAE.PostSelectionEntity, defstate1: bool, postSel2: CAE.PostSelectionEntity, defstate2: bool) -> float:
        ...
    def PostviewGetLegend(self, postviewId: int) -> CAE.PostLegend:
        ...
    def PostviewSetLegend(self, postviewId: int, legend: CAE.PostLegend) -> None:
        ...
    def PostviewSetMass(self, postviewId: int, mass: CAE.Post.Mass) -> None:
        ...
    def PostviewShowBeamContour(self, posviewId: int, showBeamContour: bool) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  Instead use NXOpen.CAE.Post.PostviewSetBeamDisplay with Style as LineAndDiagram.")"""
        ...
    def PostviewSetBeamContourScaleMethod(self, posviewId: int, method: CAE.Post.BeamContourScaleMethod) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  Instead use NXOpen.CAE.Post.PostviewSetBeamDisplay with Style as LineAndDiagram.")"""
        ...
    def PostviewSetBeamContourScaleFactor(self, posviewId: int, factor: float) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  Instead use NXOpen.CAE.Post.PostviewSetBeamDisplay with Style as LineAndDiagram.")"""
        ...
    def PostviewAskHotspotRecipes(self, posviewId: int) -> typing.List[TaggedObject]:
        ...
    def PostviewAskHotspotsOfRecipe(self, posviewId: int, recipe: CAE.HotspotRecipe, listhotspot: typing.List[CAE.Hotspot]) -> None:
        ...
    def PostviewSetSpring(self, postviewId: int, spring: CAE.Post.Spring) -> None:
        ...
    def PostviewSetDrawForLegendBox(self, postviewId: int, draw: bool) -> None:
        ...
    def PostviewAskDrawForLegendBox(self, postviewId: int) -> bool:
        ...
    def PostviewSetFillForLegendBox(self, postviewId: int, fill: bool) -> None:
        ...
    def PostviewAskFillForLegendBox(self, postviewId: int) -> bool:
        ...
    def PostviewSetFillColorForLegendBox(self, postviewId: int, fillColor: int) -> None:
        ...
    def PostviewAskFillColorForLegendBox(self, postviewId: int) -> int:
        ...
    def PostviewSetFillTranslucentForLegendBox(self, postviewId: int, translucent: bool) -> None:
        ...
    def PostviewAskFillTranslucentForLegendBox(self, postviewId: int) -> bool:
        ...
    def PostviewCaptureAllViewportsToGif(self, fileName: str, includeOverlayedPostviews: bool, whiteBackground: bool) -> None:
        ...
    def CreatePostviewFromNodalForceReportParameters(self, viewIndex: int, nodalforcereportparams: CAE.ResultParametersWithNodalForceReport, overlay: bool) -> int:
        ...
    def PostviewGetBeamDisplay(self, postviewId: int) -> CAE.BeamDisplayParameters:
        ...
    def PostviewSetBeamDisplay(self, postviewId: int, param: CAE.BeamDisplayParameters) -> None:
        ...
    def AskResultParametersWithNodalForceReport(self, pvid: int) -> CAE.ResultParametersWithNodalForceReport:
        ...
    def SetResultParametersWithNodalForceReport(self, pvid: int, resultParameter: CAE.ResultParametersWithNodalForceReport) -> None:
        ...
    def PostviewInvertDisplay(self, pvid: int) -> None:
        ...
    def ExportDisplayInAscii(self, postviewId: int, fileName: str, ignoreClipping: bool, ignoreVisibility: bool, useDirectModelDisplay: bool) -> None:
        ...
    def UpdateAllAnnotations(self, pvid: int) -> None:
        ...
    def CreatePostGroupBuilder(self, postViewId: int) -> CAE.PostGroupBuilder:
        ...
    def Tag(self) -> Tag: ...

    Preference: CAE.PostPreference
    PostProcessingSession: CAE.PostProcessingSession
    DisplayManager: CAE.PostDisplayManager
    SmartSelectionManager: CAE.PostSmartSelectionManager


    class ValueSharingCriterion(enum.Enum):
        Average = 0
        Minimum = 1
        Maximum = 2
    

    class Threshold(enum.Enum):
        Result = 0
        Displayed = 1
        Specified = 2
        ViewportResult = 3
        ViewportDisplayed = 4
    

    class PostText():
        Font: int
        Size: int
        Color: NXColor
        Bold: int
        def ToString(self) -> str:
            ...
    

    class Target(enum.Enum):
        FreeFacees = 0
        Volume = 1
        CuttingPlane = 2
        AxisSymmetry3D = 3
    

    class Style(enum.Enum):
        SmoothContours = 0
        BandedContours = 1
        Elements = 2
        IsoLines = 3
        IsoSurfaces = 4
        Cubes = 5
        Spheres = 6
        Arrows = 7
        Tensors = 8
        Streamlines = 9
    

    class StreamlineSynchronization(enum.Enum):
        Upstream = 0
        Downstream = 1
        SeedPoint = 2
    

    class StreamlineStyle(enum.Enum):
        Line = 0
        Ribbon = 1
        Tube = 2
        Bubble = 3
    

    class StreamlineSize(enum.Enum):
        PercentageOfModel = 0
        SpecifiedLength = 1
    

    class PostStreamlineSeed():
        Extraction: CAE.Post.StreamlineExtraction
        Coordinates: Point3d
        ElementId: int
        def ToString(self) -> str:
            ...
        def __init__(self, Extraction: CAE.Post.StreamlineExtraction, Coordinates: Point3d, ElementId: int) -> None: ...
    

    class StreamlineLineWeight(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
    

    class PostStreamlineExtraction():
        Direction: CAE.Post.StreamlineDirection
        MaximumTimeElapsed: float
        MaxIntegrationSteps: int
        LimitStepSize: bool
        MaximumStepSize: float
        IntegrationScheme: CAE.Post.IntegrationScheme
        DisjointRestart: bool
        def ToString(self) -> str:
            ...
    

    class StreamlineDirection(enum.Enum):
        Upstream = 0
        Downstream = 1
        Both = 2
    

    class PostStreamlineData():
        ValueShareingCriterion: CAE.Post.ValueSharingCriterion
        NoDataTreatment: CAE.Post.NoDataTreatment
        NoDataValue: float
        def ToString(self) -> str:
            ...
        def __init__(self, ValueShareingCriterion: CAE.Post.ValueSharingCriterion, NoDataTreatment: CAE.Post.NoDataTreatment, NoDataValue: float) -> None: ...
    

    class StreamlineColor(enum.Enum):
        ResultValue = 0
        Specified = 1
        Textcolor = 2
    

    class PostStreamline():
        DataParams: CAE.Post.StreamlineData
        StreamStyle: CAE.Post.StreamlineStyle
        StreamColor: CAE.Post.StreamlineColor
        SpecifiedColor: NXColor
        StreamSize: CAE.Post.StreamlineSize
        ModelPrecentValue: float
        SpecifiedLengthValue: float
        Lineweight: CAE.Post.StreamlineLineWeight
        StreamSync: CAE.Post.StreamlineSynchronization
        BubbleTimestep: float
        def ToString(self) -> str:
            ...
    

    class SpringSizeOption(enum.Enum):
        PercentageOfModel = 0
        SpecifiedLength = 1
    

    class PostSpring():
        SpringSizeOption: CAE.Post.SpringSizeOption
        ModelPrecentValue: float
        SpecifiedLengthValue: float
        def ToString(self) -> str:
            ...
        def __init__(self, SpringSizeOption: CAE.Post.SpringSizeOption, ModelPrecentValue: float, SpecifiedLengthValue: float) -> None: ...
    

    class Spectrum(enum.Enum):
        Structural = 0
        Thermal = 1
        GrayScale = 2
        StopLight = 3
    

    class Spacing(enum.Enum):
        EquallySpaced = 0
        RoundOff = 1
        LevelIncrement = 2
    

    class ShowHeader(enum.Enum):
        None = 0
        Automatic = 1
        Customized = 2
        Compact = 3
    

    class Scale(enum.Enum):
        Automatic = 0
        Linear = 1
        Logarithmic = 2
    

    class PostPrimaryEdgeFace():
        EdgeStyle: CAE.Post.EdgeStyle
        EdgeColor: NXColor
        FaceStyle: CAE.Post.FaceFillStyle
        FaceColor: NXColor
        def ToString(self) -> str:
            ...
    

    class Position(enum.Enum):
        Left = 0
        Right = 1
        None = 2
    

    class PlotStyle(enum.Enum):
        Contours = 0
        IsoLines = 1
        IsoSurfaces = 2
        Cubes = 3
        Spheres = 4
        Arrows = 5
        Tensors = 6
        Streamlines = 7
    

    class NodeValueSharingCriterion(enum.Enum):
        Average = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
    

    class NoDataTreatment(enum.Enum):
        Ignore = 0
        SpecifiedValue = 1
    

    class MassSizeOption(enum.Enum):
        PercentageOfModel = 0
        SpecifiedLength = 1
    

    class PostMass():
        MassSizeOption: CAE.Post.MassSizeOption
        ModelPrecentValue: float
        SpecifiedLengthValue: float
        def ToString(self) -> str:
            ...
        def __init__(self, MassSizeOption: CAE.Post.MassSizeOption, ModelPrecentValue: float, SpecifiedLengthValue: float) -> None: ...
    

    class MarkTensorStyle(enum.Enum):
        BoxAndArrows = 0
        OnlyArrows = 1
        OnlyBox = 2
        OnlyLine = 3
    

    class MarkSize(enum.Enum):
        ResultValue = 0
        Specified = 1
    

    class MarkResultantCompCombinationType(enum.Enum):
        None = 0
        Xy = 1
        Yz = 2
        Zx = 3
    

    class MarkRenderStyle(enum.Enum):
        Line = 0
        Solid = 1
    

    class MarkMaximumSize(enum.Enum):
        PercentageOfModel = 0
        SpecifiedLength = 1
    

    class MarkLocation(enum.Enum):
        Nodes = 0
        Elements = 1
    

    class MarkHide(enum.Enum):
        ResultPercent = 0
        AbsoluteResultPercent = 1
        ResultValue = 2
    

    class Marker(enum.Enum):
        MinimumAndMaximum = 0
        MinimumOnly = 1
        MaximumOnly = 2
    

    class MarkComponentCombinationType(enum.Enum):
        Normal = 0
        Principal = 1
        Shear = 2
        Force = 3
        Moment = 4
    

    class MarkColor(enum.Enum):
        ResultValue = 0
        Specified = 1
        Textcolor = 2
    

    class PostMark():
        ShowArrowXComponent: bool
        ShowArrowYComponent: bool
        ShowArrowZComponent: bool
        ShowArrowMagnitude: bool
        MarkRenderStyle: CAE.Post.MarkRenderStyle
        MarkTensorStyle: CAE.Post.MarkTensorStyle
        MarkColor: CAE.Post.MarkColor
        SpecifiedColor: NXColor
        MarkSize: CAE.Post.MarkSize
        MarkMaximumSize: CAE.Post.MarkMaximumSize
        ModelPrecentValue: float
        SpecifiedLengthValue: float
        MarkLocation: CAE.Post.MarkLocation
        HideMarksBelow: bool
        BelowMarkHideType: CAE.Post.MarkHide
        BelowResultPercent: float
        BelowResultValue: float
        DisplayNumericalValueWithArrow: bool
        DoubleSided: bool
        MarkComponentCombinationType: CAE.Post.MarkComponentCombinationType
        ShowTensorComponent1: bool
        ShowTensorComponent2: bool
        ShowTensorComponent3: bool
        ShowTensorComponent4: bool
        DisplayComponentLabelWithArrow: bool
        ShowArrowResultant: bool
        MarkResultantCompCombinationType: CAE.Post.MarkResultantCompCombinationType
        def ToString(self) -> str:
            ...
    

    class LimitDisplay(enum.Enum):
        None = 0
        Shaded = 1
        Translucent = 2
        Clipped = 3
    

    class Legend(enum.Enum):
        Detailed = 0
        ColorbarOnly = 1
        HeaderOnly = 2
    

    class IntegrationScheme(enum.Enum):
        Euler = 0
        Rk2 = 1
        Rk4 = 2
    

    class PostHeaderlines():
        Show: bool
        Line: str
        def ToString(self) -> str:
            ...
        def __init__(self, Show: bool, Line: str) -> None: ...
    

    class GroupVisibility(enum.Enum):
        ShowOnly = 0
        Show = 1
        Hide = 2
    

    class PostGraphParameters():
        UseDeformedConfiguration: bool
        IncludeIntersections: bool
        ValueShareingCriterion: CAE.Post.NodeValueSharingCriterion
        NoDataTreatment: CAE.Post.NoDataTreatment
        NoDataValue: float
        Abcissa: CAE.Post.Abcissa
        def ToString(self) -> str:
            ...
    

    class PostGraphIds():
        GraphFileId: int
        GraphSetId: int
        def ToString(self) -> str:
            ...
        def __init__(self, GraphFileId: int, GraphSetId: int) -> None: ...
    

    class Format(enum.Enum):
        Auto = 0
        FixedPoint = 1
        Scientific = 2
    

    class FaceStyle(enum.Enum):
        Opaque = 0
        Translucent = 1
        None = 2
    

    class FaceFillStyle(enum.Enum):
        Fill = 0
        NoFill = 1
    

    class Export(enum.Enum):
        Ascii = 0
        Jt = 1
        Vrml = 2
    

    class EdgeStyle(enum.Enum):
        External = 0
        Feature = 1
        Wireframe = 2
        None = 3
        Polygonedge = 4
    

    class PostEdgeFace():
        EdgeStyle: CAE.Post.EdgeStyle
        EdgeColor: NXColor
        FaceStyle: CAE.Post.FaceStyle
        FaceColor: NXColor
        def ToString(self) -> str:
            ...
    

    class DisplayColorSchemeType(enum.Enum):
        Fringe = 0
        Mid = 1
        Pid = 2
        Mesh = 3
    

    class ColorbarStyle(enum.Enum):
        Smooth = 0
        Banded = 1
    

    class PostColorbar():
        Spectrum: CAE.Post.Spectrum
        InvertSpectrum: bool
        Scale: CAE.Post.Scale
        AutomaticLevel: bool
        NumberOfLevels: int
        Threshold: CAE.Post.Threshold
        ThresholdMinimum: float
        ThresholdMaximum: float
        ShowOverflowAbove: bool
        ShowOverflowBelow: bool
        OverflowAboveColor: NXColor
        OverflowBelowColor: NXColor
        Position: CAE.Post.Position
        Overflow: CAE.Post.LimitDisplay
        Underflow: CAE.Post.LimitDisplay
        Spacing: CAE.Post.Spacing
        IncrementPerLevel: float
        def ToString(self) -> str:
            ...
    

    class ClipSide(enum.Enum):
        Positive = 0
        Negative = 1
        Both = 2
    

    class ClipPlane(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class PostClipping():
        ShowOutline: bool
        ShowClippedGhost: bool
        ClipValue: float
        Side: CAE.Post.ClipSide
        Plane: CAE.Post.ClipPlane
        PlaneCoordinateSystem: CAE.Result.CoordinateSystem
        def ToString(self) -> str:
            ...
    

    class BeamContourScaleMethod(enum.Enum):
        PercentModel = 0
        Absolute = 1
    

    class BandStyle(enum.Enum):
        Default = 0
        Line = 1
        ValInline = 2
    

    class PostAxisymmetric():
        NumberOfSection: int
        RevolveAngle: float
        AxisymAxis: CAE.Post.AxisymetricAxis
        def ToString(self) -> str:
            ...
        def __init__(self, NumberOfSection: int, RevolveAngle: float, AxisymAxis: CAE.Post.AxisymetricAxis) -> None: ...
    

    class AxisymetricAxis(enum.Enum):
        None = -1
        X = 0
        Y = 1
        Z = 2
    

    class PostASCIIDiffTolerances():
        Coorderr: float
        Dataerr: float
        Rgbtol: float
        Coordtol: float
        Datatol: float
        Zerotol: float
        def ToString(self) -> str:
            ...
    

    class PostAnnotationBox():
        LineColor: NXColor
        AreaColor: NXColor
        ShowBorder: bool
        FillArea: bool
        AreaTranslucency: bool
        def ToString(self) -> str:
            ...
    

    class AnimationType(enum.Enum):
        Result = 0
        Iterations = 1
        Streamline = 2
    

    class AnimationStyle(enum.Enum):
        Linear = 0
        Modal = 1
        Forwardwave = 2
        Backwardwave = 3
    

    class PostAnimationStreamline():
        ShowGuides: bool
        StreamSync: CAE.Post.StreamlineSynchronization
        ActiveRegionStartFactor: float
        ActiveRegionEndFactor: float
        NumberOfIncrements: int
        ContinuousPulse: bool
        NumberOfTimePeriods: int
        FramesPerPulse: float
        PulseDutycycle: float
        def ToString(self) -> str:
            ...
    

    class PostAnimationParameters():
        AnimationType: CAE.Post.AnimationType
        AnimationStyle: CAE.Post.AnimationStyle
        NumberOfFrames: int
        AnimStartIteration: CAE.Iteration
        AnimEndIteration: CAE.Iteration
        IterationIncrement: int
        FullCycle: bool
        Delay: int
        AnimationStreamline: CAE.Post.AnimationStreamline
        IterationType: CAE.Post.AnimationIterationTypes
        IterValueType: CAE.BaseIteration.IterationValueType
        Color: bool
        Deformation: bool
        SaveFramesInMemory: bool
        def ToString(self) -> str:
            ...
    

    class AnimationIterationTypes(enum.Enum):
        Value = 0
        None = 1
    

    class AnimationControl(enum.Enum):
        Back = 0
        Next = 1
        Play = 2
        Pause = 3
        Stop = 4
        SetFrame = 5
        FullCycle = 6
        Delay = 7
        Streamline = 8
    

    class PostAnimation():
        AnimationType: CAE.Post.AnimationType
        AnimationStyle: CAE.Post.AnimationStyle
        NumberOfFrames: int
        StartLoadcase: int
        StartIteration: int
        EndLoadcase: int
        EndIteration: int
        IterationIncrement: int
        FullCycle: bool
        Delay: int
        AnimationStreamline: CAE.Post.AnimationStreamline
        IterationType: CAE.Post.AnimationIterationTypes
        IterValueType: CAE.BaseIteration.IterationValueType
        Color: bool
        Deformation: bool
        SaveFramesInMemory: bool
        def ToString(self) -> str:
            ...
    

    class Abcissa(enum.Enum):
        Uneven = 0
        Even = 1
        Sequenced = 2
    

    class Post_Text():
        font: int
        size: int
        color: int
        bold: int
    

    class Post_Streamline():
        data_params: CAE.Post.StreamlineData
        stream_style: CAE.Post.StreamlineStyle
        stream_color: CAE.Post.StreamlineColor
        specified_color: int
        stream_size: CAE.Post.StreamlineSize
        model_precent_value: float
        specified_length_value: float
        lineweight: CAE.Post.StreamlineLineWeight
        stream_sync: CAE.Post.StreamlineSynchronization
        bubble_timestep: float
    

    class Post_PrimaryEdgeFace():
        edge_style: CAE.Post.EdgeStyle
        edge_color: int
        face_style: CAE.Post.FaceFillStyle
        face_color: int
    

    class Post_Mark():
        show_arrow_x_component: bool
        show_arrow_y_component: bool
        show_arrow_z_component: bool
        show_arrow_magnitude: bool
        mark_render_style: CAE.Post.MarkRenderStyle
        mark_tensor_style: CAE.Post.MarkTensorStyle
        mark_color: CAE.Post.MarkColor
        specified_color: int
        mark_size: CAE.Post.MarkSize
        mark_maximum_size: CAE.Post.MarkMaximumSize
        model_precent_value: float
        specified_length_value: float
        mark_location: CAE.Post.MarkLocation
        hide_marks_below: bool
        below_mark_hide_type: CAE.Post.MarkHide
        below_result_percent: float
        below_result_value: float
        display_numerical_value_with_arrow: bool
        doubleSided: bool
        mark_component_combination_type: CAE.Post.MarkComponentCombinationType
        show_tensor_component1: bool
        show_tensor_component2: bool
        show_tensor_component3: bool
        show_tensor_component4: bool
        display_component_label_with_arrow: bool
        show_arrow_resultant: bool
        mark_resultant_comp_combination_type: CAE.Post.MarkResultantCompCombinationType
    

    class Post_Headerlines():
        show: bool
        line: int
    

    class Post_EdgeFace():
        edge_style: CAE.Post.EdgeStyle
        edge_color: int
        face_style: CAE.Post.FaceStyle
        face_color: int
    

    class Post_Colorbar():
        spectrum: CAE.Post.Spectrum
        invert_spectrum: bool
        scale: CAE.Post.Scale
        automatic_level: bool
        number_of_levels: int
        threshold: CAE.Post.Threshold
        threshold_minimum: float
        threshold_maximum: float
        show_overflow_above: bool
        show_overflow_below: bool
        overflow_above_color: int
        overflow_below_color: int
        position: CAE.Post.Position
        overflow: CAE.Post.LimitDisplay
        underflow: CAE.Post.LimitDisplay
        spacing: CAE.Post.Spacing
        increment_per_level: float
    

    class Post_AnnotationBox():
        line_color: int
        area_color: int
        show_border: bool
        fill_area: bool
        area_translucency: bool
    

    class Post_AnimationParameters():
        animation_type: CAE.Post.AnimationType
        animation_style: CAE.Post.AnimationStyle
        number_of_frames: int
        anim_start_iteration: Tag
        anim_end_iteration: Tag
        iteration_increment: int
        full_cycle: bool
        delay: int
        animation_streamline: CAE.Post.AnimationStreamline
        iteration_type: CAE.Post.AnimationIterationTypes
        iter_value_type: CAE.BaseIteration.IterationValueType
        color: bool
        deformation: bool
        save_frames_in_memory: bool
    

class PolygonGeometryManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.FemPart) -> None: ...
    def SetPolygonBodyResolutionOnFemBodies(self, resType: CAE.PolygonGeometryManager.PolygonBodyResolutionType) -> None:
        ...
    def GetPolygonBodyResolutionOnFemBodies(self) -> CAE.PolygonGeometryManager.PolygonBodyResolutionType:
        ...
    def SetPolygonBodyResolutionWithRecreate(self, resolutionType: CAE.PolygonGeometryManager.PolygonBodyResolutionType, inPolygonBodies: typing.List[CAE.CAEBody]) -> typing.List[CAE.CAEBody]:
        ...
    def SetPolygonBodyResolutionWithRecreateAndUpdate(self, resolutionType: CAE.PolygonGeometryManager.PolygonBodyResolutionType, inPolygonBodies: typing.List[CAE.CAEBody]) -> typing.List[CAE.CAEBody]:
        ...
    def SetPolygonBodyResolutionCustomDistanceOnFemBodies(self, customDistance: Expression) -> None:
        ...
    def GetPolygonBodyResolutionCustomDistanceOnFemBodies(self) -> Expression:
        ...
    def SetPolygonBodyResolutionCustomAngleOnFemBodies(self, customAngle: Expression) -> None:
        ...
    def GetPolygonBodyResolutionCustomAngleOnFemBodies(self) -> Expression:
        ...
    def SetPolygonBodyResolutionCustomDistance(self, customDistance: Expression, inPolygonBodies: typing.List[CAE.CAEBody]) -> None:
        ...
    def GetPolygonBodyResolutionCustomDistance(self, polygonBody: CAE.CAEBody) -> Expression:
        ...
    def SetPolygonBodyResolutionCustomAngle(self, customAngle: Expression, inPolygonBodies: typing.List[CAE.CAEBody]) -> None:
        ...
    def GetPolygonBodyResolutionCustomAngle(self, polygonBody: CAE.CAEBody) -> Expression:
        ...
    def AutomaticCustomDistance(self, inSolidBodies: typing.List[Body]) -> Expression:
        ...
    def AutomaticCustomDistanceFromPolygonBodies(self, inSolidBodies: typing.List[CAE.CAEBody]) -> Expression:
        ...
    def FindPolygonBodyFromSolidBody(self, body: Body) -> CAE.CAEBody:
        ...
    def Tag(self) -> Tag: ...

    CaeGeometryRecipes: CAE.GeometryRecipeCollection


    class PolygonBodyResolutionType(enum.Enum):
        Standard = 0
        Medium = 1
        High = 2
        Custom = 3
    

class PolygonFaceOnMeshBuilder(Builder):
    def __init__(self) -> None: ...
    AllowInconsistentElementNormalsOption: bool
    BoundaryMerging: Expression
    DuplicateNodesAttachedToSolidsOption: bool
    ElementEdgeFeatureAngle: Expression
    ElementEdgeSelection: CAE.SelectElementsBuilder
    ElementFaceFeatureAngle: Expression
    ElementSelection: CAE.SelectElementsBuilder
    FaceSmoothing: Expression
    KeepInternalEdgesOption: bool
    SelectBody: SelectTaggedObjectList
    SelectBodyOption: CAE.PolygonFaceOnMeshBuilder.SelectBodyMethod
    SelectMesh: SelectTaggedObjectList
    Type: CAE.PolygonFaceOnMeshBuilder.PolygonFaceOnMeshType


    class SelectBodyMethod(enum.Enum):
        CreateNew = 0
        AddToExisting = 1
    

    class PolygonFaceOnMeshType(enum.Enum):
        TwoDimensionElement = 0
        ElementFreeFace = 1
        Mesh = 2
    

class PointSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    def SetPointAndTolerance(self, point: Point, tolerance: float) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipePointStrategy.SetPointAndTolerance instead.")"""
        ...
    def SetHighLabelPreference(self, useHighLabel: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipePointStrategy.SetResolvePreference instead.")"""
        ...
    HighLabelPreference: bool
    Point: Point
    Tolerance: float


class PointInterpolationData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    def AskElementIndex(self) -> int:
        ...
    def AskPoint(self) -> Point3d:
        ...


class PlotFrfOptionsBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    AveragingOptions: CAE.PlotFrfOptionsBuilder.AveragingFrfOptions
    FreqRangeLowerLimit: Expression
    FreqRangeUpperLimit: Expression
    FrequencyFracRange: CAE.PlotFrfOptionsBuilder.FracFrequencyRange
    FrequencyRange: CAE.PlotFrfOptionsBuilder.FrequencyFrfRange
    InputWorkFrfDofX: bool
    InputWorkFrfDofY: bool
    InputWorkFrfDofZ: bool
    StretchFactor: float
    StretchFactorIncrement: float
    StretchFactorLowerLimit: float
    StretchFactorUpperLimit: float
    WorkFrfDofX: bool
    WorkFrfDofY: bool
    WorkFrfDofZ: bool


    class FrequencyFrfRange(enum.Enum):
        Inferred = 0
        Reference = 1
        Work = 2
        UserDefined = 3
    

    class FracFrequencyRange(enum.Enum):
        Inferred = 0
        UserDefined = 1
    

    class AveragingFrfOptions(enum.Enum):
        None = 0
        RMSAverage = 1
        RSSSum = 2
    

class PlotFrfOptions(NXObject):
    def __init__(self) -> None: ...


class PlotContoursBuilder(Builder):
    def __init__(self) -> None: ...
    def SetMeshesToPlot(self, pMeshTags: typing.List[CAE.Mesh]) -> None:
        ...
    def SetElementsToPlot(self, pElementTags: typing.List[CAE.FEElement]) -> None:
        ...
    def CreatePlotObject(self) -> CAE.ExpressionPlotContours:
        ...
    ScalarFieldWrapper: Fields.ScalarFieldWrapper


class Plane(enum.Enum):
    XyOfWcs = 1
    ModelView = 2
    XzOfWcs = 3
    YzOfWcs = 4


class PlanarParallelMeshSlicing(CAE.MeshSlicingData):
    def __init__(self) -> None: ...
    def GetSlicingDirection(self, coordinates: float) -> None:
        ...
    def SetSlicingDirection(self, coordinates: float) -> None:
        ...
    def GetReferencePoint(self, pointCoords: float) -> None:
        ...
    def SetReferencePoint(self, pointCoords: float) -> None:
        ...
    def GetDistancesFromReferencePoint(self, distances: float) -> None:
        ...
    def SetDistancesFromReferencePoint(self, distances: float) -> None:
        ...


class PhysicalPropertyTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PhysicalPropertyTable]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreatePhysicalPropertyTable(self, descriptorType: str, languageName: str, solverName: str, name: str, label: int) -> CAE.PhysicalPropertyTable:
        ...
    def CopyPhysicalPropertyTable(self, sourcePhysicalPropertyTable: CAE.PhysicalPropertyTable) -> CAE.PhysicalPropertyTable:
        ...
    def CopyLaminatePropertyTableAs2d3d(self, sourceLaminate: CAE.Laminate) -> CAE.Laminate:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.PhysicalPropertyTable:
        ...
    def Tag(self) -> Tag: ...



class PhysicalPropertyTable(CAE.NamedPropertyTable):
    def __init__(self) -> None: ...
    def GetSolverCardSyntax(self) -> str:
        ...


class PathType(enum.Enum):
    ShortestPath = 0
    MostTangentPath = 1


class PathEnclosedElemFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementFaces(self) -> typing.List[CAE.FEElemFace]:
        ...


class OverrideCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Override]:
        ...
    def __init__(self, owner: CAE.FEModelOccurrence) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> CAE.Override:
        ...
    def Delete(self, ovrride: CAE.Override) -> None:
        ...
    def Delete(self, ovrrides: typing.List[CAE.Override]) -> None:
        ...
    def Tag(self) -> Tag: ...



class Override(TaggedObject):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...


class OrderedSelection(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, entity: CAE.MeshPoint) -> None:
        ...
    def Add(self, entity: Point) -> None:
        ...
    def Add(self, entity: CAE.FENode) -> None:
        ...
    def Add(self, entity: CAE.FEElement) -> None:
        ...
    def Add(self, entity: CAE.CAEEdge, flipDirection: bool) -> None:
        ...
    def Add(self, entity: Line, flipDirection: bool) -> None:
        ...
    def Add(self, entity: Arc, flipDirection: bool) -> None:
        ...
    def Add(self, entity: Conic, flipDirection: bool) -> None:
        ...
    def Add(self, entity: Spline, flipDirection: bool) -> None:
        ...
    def Add(self, selectionMethod: SelectionMethod) -> None:
        ...
    def Remove(self, entity: TaggedObject) -> None:
        ...
    def Remove(self, selectionMethod: SelectionMethod) -> None:
        ...
    def Clear(self) -> None:
        ...


class OrderedFeatureEdgeNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class OrderedFeatureEdgeElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class OrderedEdgeNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class OrderedEdgeElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class OptimizeLatticeBuilder(Builder):
    def __init__(self) -> None: ...
    MaxLatticeDiameter: Expression
    MinLatticeDiameter: Expression


class OpenDuctMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def AutomaticElementSize(self) -> None:
        ...
    ElementEdge: CAE.SelectElementsBuilder
    ElementType: CAE.ElementTypeBuilder
    PropertyTable: CAE.PropertyTable


class OneDimensionalElementSplitBuilder(Builder):
    def __init__(self) -> None: ...
    Elements: CAE.SelectElementsBuilder
    LengthOfSubElements: Expression
    NumberOfSubElements: int
    SplitMethod: CAE.OneDimensionalElementSplitBuilder.SplitMethodType


    class SplitMethodType(enum.Enum):
        NumberElement = 0
        LengthElement = 1
    

class NxBcPlotContours(TaggedObject):
    def __init__(self) -> None: ...
    def PlotContour(self, viewIndex: int) -> None:
        ...


class NumberFormat(TaggedObject):
    def __init__(self) -> None: ...
    DecimalPlaces: int
    Format: CAE.NumberFormat.FormatOption


    class FormatOption(enum.Enum):
        Automatic = 0
        Fixed = 1
        Scientific = 2
    

class NotePreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    BackgroundColor: int
    EnableBackground: bool
    FontGapFactor: float
    LetteringAngle: float
    LineGapFactor: float
    LockSizeAndPosition: bool
    ParallelToScreen: bool
    TextAspectRatio: float
    TextColor: int
    TextFont: int
    TextHeight: float
    TextJustification: int
    TextWidth: float


class NoteManager(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.NoteFolder]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateCaeNoteBuilder(self, annotation: Annotations.SimpleDraftingAid) -> CAE.CaeNoteBuilder:
        ...
    def CreateNoteFolder(self, folderName: str) -> CAE.NoteFolder:
        ...
    def GetFolderOfAnnotation(self, annotation: Annotations.NoteBase) -> TaggedObject:
        ...
    def MoveNotesToFolder(self, folder: CAE.NoteFolder, annotation: typing.List[Annotations.NoteBase]) -> None:
        ...
    def DeleteFolder(self, folder: CAE.NoteFolder) -> None:
        ...
    def RenameFolder(self, folder: CAE.NoteFolder, folderName: str) -> None:
        ...
    def GetAllNotes(self, noteArray: typing.List[TaggedObject]) -> None:
        ...
    def GetAllNotesOfFolder(self, folderName: str, noteArray: typing.List[TaggedObject]) -> None:
        ...
    def AttachObjectsWithNote(self, note: TaggedObject, objectArray: typing.List[TaggedObject]) -> None:
        ...
    def DetachObjectsWithNote(self, note: TaggedObject) -> None:
        ...
    def ShowNotes(self, noteArray: typing.List[TaggedObject]) -> None:
        ...
    def HideNotes(self, noteArray: typing.List[TaggedObject]) -> None:
        ...
    def GetDisplayStatus(self, notes: TaggedObject) -> bool:
        ...
    def FindNotesWithText(self, findStr: str, noteArray: typing.List[TaggedObject]) -> None:
        ...
    def FindNotesWithSubtext(self, findStr: str, noteArray: typing.List[TaggedObject]) -> None:
        ...
    def CreateNote(self, lines: str, origin: Point3d, font: int, fontColor: int, fontSize: int, planeType: CAE.Plane, folderName: str) -> CAE.CaeNote:
        ...
    def SetText(self, note: TaggedObject, lines: str) -> None:
        ...
    def SetOrigin(self, note: TaggedObject, origin: Point3d) -> None:
        ...
    def SetParallelToScreen(self, parallelToScreen: bool, annotations: typing.List[CAE.CaeNote]) -> None:
        ...
    def CreateNotePreferencesBuilder(self) -> CAE.NotePreferencesBuilder:
        ...
    def SetAnnotContextToAnnotCaeContext(self, note: TaggedObject) -> None:
        ...
    def Tag(self) -> Tag: ...



class NoteFolder(NXObject):
    def __init__(self) -> None: ...


    class FolderType(enum.Enum):
        New = 0
        Existing = 1
    

class NoteCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Annotations.BaseNote]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def NewNoteData(self) -> Annotations.NoteData:
        ...
    def CreateNote(self, noteData: Annotations.NoteData) -> CAE.CaeNote:
        ...
    def NewLabelData(self) -> Annotations.LabelData:
        ...
    def CreateLabel(self, labelData: Annotations.LabelData) -> CAE.CaeLabel:
        ...
    def RemoveNote(self, note: TaggedObject) -> None:
        ...
    def RemoveAnnotationWithoutPlane(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class NodeTranslateBuilder(Builder):
    def __init__(self) -> None: ...
    CopyOption: CAE.NodeTranslateBuilder.CopyType
    Csys: CoordinateSystem
    DistanceOption: CAE.NodeTranslateBuilder.DistanceType
    Field: Fields.FieldWrapper
    Increment: int
    Label: int
    LabelOption: CAE.NodeTranslateBuilder.LabelType
    MethodOption: CAE.NodeTranslateBuilder.MethodType
    Node: CAE.SelectFENodeList
    NumCopy: int
    Offset: int
    PAngle: Expression
    PointSource: Point
    PointTarget: Point
    ScaleFactor: float
    TAngle: Expression
    Vector: Direction
    VectorSource: Direction
    VectorTarget: Direction
    XDistance: Expression
    XScaleFactor: float
    YDistance: Expression
    YScaleFactor: float
    ZDistance: Expression
    ZScaleFactor: float


    class MethodType(enum.Enum):
        ByComponents = 0
        AlongDirection = 1
        AlignVectors = 2
        PointToPoint = 3
        ScaleModel = 4
        ByField = 5
    

    class LabelType(enum.Enum):
        LabelIncrement = 0
        ByOffset = 1
    

    class DistanceType(enum.Enum):
        PerCopy = 0
        Total = 1
    

    class CopyType(enum.Enum):
        TranslateOnly = 0
        CopyTranslate = 1
    

class NodesRepositionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetNodePosition(self, fenode: CAE.FENode, position: Point3d) -> None:
        ...
    def SetNodePositions(self, fenodes: typing.List[CAE.FENode], positions: typing.List[Point3d]) -> None:
        ...


class NodesOnCurveBuilder(Builder):
    def __init__(self) -> None: ...
    Distance: Expression
    Edge: CAE.SelectCAEEdge
    Geom: SelectDisplayableObject
    Increment: int
    IsClosedCurve: bool
    Label: int
    Length: float
    NumNodes: int
    PlacementOption: CAE.NodesOnCurveBuilder.PlacementType


    class PlacementType(enum.Enum):
        ByNumber = 0
        ByDistance = 1
    

class NodesBetweenNodesBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCommittedNodes(self) -> typing.List[CAE.FENode]:
        ...
    Increment: int
    Label: int
    Node: CAE.SelectFENodeList
    NumNodes: int
    Type: CAE.NodesBetweenNodesBuilder.TypeEnum


    class TypeEnum(enum.Enum):
        NodesBetweenTwoNodes = 0
        NodeAtCenterOfThreeNodes = 1
    

class NodeRotateBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: Expression
    Axis: Axis
    CopyOption: CAE.NodeRotateBuilder.CopyType
    DistanceOption: CAE.NodeRotateBuilder.DistanceType
    Increment: int
    Label: int
    LabelOption: CAE.NodeRotateBuilder.LabelType
    Node: CAE.SelectFENodeList
    NumCopy: int
    Offset: int


    class LabelType(enum.Enum):
        LabelIncrement = 0
        ByOffset = 1
    

    class DistanceType(enum.Enum):
        PerCopy = 0
        Total = 1
    

    class CopyType(enum.Enum):
        RotateOnly = 0
        CopyRotate = 1
    

class NodeRelationshipType(enum.Enum):
    AnyNode = 0
    AllNodes = 1


class NodeReflectBuilder(Builder):
    def __init__(self) -> None: ...
    CopyOption: CAE.NodeReflectBuilder.CopyType
    Increment: int
    Label: int
    LabelOption: CAE.NodeReflectBuilder.LabelType
    Node: CAE.SelectFENodeList
    Offset: int
    Plane: Plane


    class LabelType(enum.Enum):
        LabelIncrement = 0
        ByOffset = 1
    

    class CopyType(enum.Enum):
        ReflectOnly = 0
        CopyReflect = 1
    

class NodeProximityPlotContours(TaggedObject):
    def __init__(self) -> None: ...
    def PlotContour(self, viewIndex: int) -> None:
        ...


class NodeProjectBuilder(Builder):
    def __init__(self) -> None: ...
    CopyOption: CAE.NodeProjectBuilder.NodeProjectTypes
    Geometry: SelectTaggedObject
    Increment: int
    Label: int
    LabelOption: CAE.NodeProjectBuilder.LabelType
    MethodOption: CAE.NodeProjectBuilder.ProjectionMethodType
    Nodes: CAE.SelectFENodeList
    Offset: int
    PercentOffset: float
    Tolerance: float
    Vector: Direction


    class ProjectionMethodType(enum.Enum):
        ByDirection = 0
        ShotestDistance = 1
    

    class NodeProjectTypes(enum.Enum):
        ProjectOnly = 0
        CopyAndProject = 1
    

    class LabelType(enum.Enum):
        Label = 0
        Offset = 1
    

class NodeModifyLocationBuilder(Builder):
    def __init__(self) -> None: ...
    Csys: CoordinateSystem
    Node: CAE.SelectFENodeList
    Phi: Expression
    Theta: Expression
    X: Expression
    XOption: bool
    Y: Expression
    YOption: bool
    Z: Expression
    ZOption: bool


class NodeModifyLabelBuilder(Builder):
    def __init__(self) -> None: ...
    DispCsys: CoordinateSystem
    Increment: int
    Label: int
    LabelOption: CAE.NodeModifyLabelBuilder.LabelType
    Node: CAE.SelectFENodeList
    Offset: int
    RefCsys: CoordinateSystem


    class LabelType(enum.Enum):
        LabelIncrement = 0
        ByOffset = 1
    

class NodeLabelMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class NodeInfoUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.NodeElementManager) -> None: ...
    def AskNodeCoordinates(self, nodes: typing.List[CAE.FENode], coordinateSystem: CoordinateSystem) -> typing.List[Point3d]:
        ...
    def Tag(self) -> Tag: ...



class NodeElementManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def CreateNodesOnCurveBuilder(self) -> CAE.NodesOnCurveBuilder:
        ...
    def CreateNodeRotateBuilder(self) -> CAE.NodeRotateBuilder:
        ...
    def CreateNodeTranslateBuilder(self) -> CAE.NodeTranslateBuilder:
        ...
    def CreateNodeAlignBuilder(self) -> CAE.NodeAlignBuilder:
        ...
    def CreateNodeModifyLabelBuilder(self) -> CAE.NodeModifyLabelBuilder:
        ...
    def CreateElementModifyLabelBuilder(self) -> CAE.ElementModifyLabelBuilder:
        ...
    def CreateNodesBetweenNodesBuilder(self) -> CAE.NodesBetweenNodesBuilder:
        ...
    def CreateNodeDeleteBuilder(self) -> CAE.NodeDeleteBuilder:
        ...
    def CreateElementCreateBuilder(self) -> CAE.ElementCreateBuilder:
        ...
    def CreateMultipleElementCreateBuilder(self, estimatedNumberOfElements: int) -> CAE.MultipleElementCreateBuilder:
        ...
    def CreateElementExtrudeBuilder(self) -> CAE.ElementExtrudeBuilder:
        ...
    def CreateElementRevolveBuilder(self) -> CAE.ElementRevolveBuilder:
        ...
    def CreateElementSplitBuilder(self) -> CAE.ElementSplitBuilder:
        ...
    def CreateOneDimensionalElementSplitBuilder(self) -> CAE.OneDimensionalElementSplitBuilder:
        ...
    def CreateNodeCreateBuilder(self) -> CAE.NodeCreateBuilder:
        ...
    def CreateMultipleNodeCreateBuilder(self, estimatedNumberOfNodes: int) -> CAE.MultipleNodeCreateBuilder:
        ...
    def CreateNodeModifyLocationBuilder(self) -> CAE.NodeModifyLocationBuilder:
        ...
    def CreateNodesRepositionBuilder(self) -> CAE.NodesRepositionBuilder:
        ...
    def CreateElementProjectBuilder(self) -> CAE.ElementProjectBuilder:
        ...
    def CreateDeleteElementBuilder(self) -> CAE.ElementDeleteBuilder:
        ...
    def CreateElementTranslateBuilder(self) -> CAE.ElementTranslateBuilder:
        ...
    def CreateNodeReflectBuilder(self) -> CAE.NodeReflectBuilder:
        ...
    def CreateElementReflectBuilder(self) -> CAE.ElementReflectBuilder:
        ...
    def CreateElementCopyAndReflectBuilder(self, tRecipeReflect: CAE.MeshManual) -> CAE.ElementReflectBuilder:
        ...
    def CreateElementConnectivityBuilder(self) -> CAE.ElementConnectivityBuilder:
        ...
    def CreateSpiderElementBuilder(self) -> CAE.SpiderElementBuilder:
        ...
    def CreateElementTypeBuilder(self) -> CAE.ElementTypeBuilder:
        ...
    def CreateDestinationCollectorBuilder(self, isInEdit: bool, elementTypeBuilder: CAE.ElementTypeBuilder) -> CAE.DestinationCollectorBuilder:
        ...
    def CreateLumpedMassEadBuilder(self) -> CAE.LumpedMassEADBuilder:
        ...
    def CreateLumpedMassEadBuilder(self, element: CAE.FEElement) -> CAE.LumpedMassEADBuilder:
        ...
    def CreateSpringEadBuilder(self) -> CAE.SpringEADBuilder:
        ...
    def CreateSpringEadBuilder(self, element: CAE.FEElement) -> CAE.SpringEADBuilder:
        ...
    def CreateBeamEadBuilder(self) -> CAE.BeamEADBuilder:
        ...
    def CreateBeamEadBuilder(self, element: CAE.FEElement) -> CAE.BeamEADBuilder:
        ...
    def CreateShellEadBuilder(self) -> CAE.ShellEADBuilder:
        ...
    def CreateShellEadBuilder(self, element: CAE.FEElement) -> CAE.ShellEADBuilder:
        ...
    def CreateBushingEadBuilder(self) -> CAE.BushingEADBuilder:
        ...
    def CreateBushingEadBuilder(self, element: CAE.FEElement) -> CAE.BushingEADBuilder:
        ...
    def CreateGapEadBuilder(self) -> CAE.GapEADBuilder:
        ...
    def CreateGapEadBuilder(self, element: CAE.FEElement) -> CAE.GapEADBuilder:
        ...
    def CreateInterpolationEadBuilder(self, element: CAE.FEElement) -> CAE.InterpolationEADBuilder:
        ...
    def CreateDamperEadBuilder(self) -> CAE.DamperEADBuilder:
        ...
    def CreateDamperEadBuilder(self, element: CAE.FEElement) -> CAE.DamperEADBuilder:
        ...
    def CreateRigidEadBuilder(self) -> CAE.RigidEADBuilder:
        ...
    def CreateRigidEadBuilder(self, element: CAE.FEElement) -> CAE.RigidEADBuilder:
        ...
    def CreateSolidEadBuilder(self) -> CAE.SolidEADBuilder:
        ...
    def CreateSolidEadBuilder(self, element: CAE.FEElement) -> CAE.SolidEADBuilder:
        ...
    def CreateElementModifyOrderBuilder(self) -> CAE.ElementModifyOrderBuilder:
        ...
    def CreateSurfaceCoatBuilder(self) -> CAE.SurfaceCoatBuilder:
        ...
    def CreateCombineTrisBuilder(self) -> CAE.CombineTrisBuilder:
        ...
    def CreateElementExtractBuilder(self) -> CAE.ElementExtractBuilder:
        ...
    def CreateSweepBetweenMeshBuilder(self) -> CAE.SweepBetweenMeshBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use CAE.Mesh3dHexBuilder.")"""
        ...
    def CreateMeshFromBoundaryBuilder(self) -> CAE.MeshFromBoundaryBuilder:
        ...
    def CreateElementModifyTypeBuilder(self) -> CAE.ElementModifyTypeBuilder:
        ...
    def CreateNodeProjectBuilder(self) -> CAE.NodeProjectBuilder:
        ...
    def CreateAutomaticMorphBuilder(self) -> CAE.AutomaticMorphBuilder:
        ...
    def CreateManualMorphBuilder(self) -> CAE.ManualMorphBuilder:
        ...
    def CreateNodeAssociationBuilder(self) -> CAE.NodeAssociationBuilder:
        ...
    def CreateNodeDissociationBuilder(self) -> CAE.NodeDissociationBuilder:
        ...
    def CreateManualNodeAssociationBuilder(self) -> CAE.ManualNodeAssociationBuilder:
        ...
    def CreateMorphRevolvedMeshBuilder(self) -> CAE.MorphRevolvedMeshBuilder:
        ...
    def CreateElementDetachBuilder(self) -> CAE.ElementDetachBuilder:
        ...
    def CreateConvexMeshBuilder(self, mesh: CAE.RecipeConvexMesh) -> CAE.ConvexMeshBuilder:
        ...
    def CreateThickenMeshBuilder(self) -> CAE.ThickenMeshBuilder:
        ...
    def CreateAttachElementsBuilder(self) -> CAE.AttachElementsBuilder:
        ...
    def CreateRemoveRibsBuilder(self) -> CAE.RemoveRibsBuilder:
        ...
    def CreateMoveNodeBuilder(self) -> CAE.MoveNodeBuilder:
        ...
    def CreateSwapDiagonalBuilder(self) -> CAE.MoveNodeBuilder:
        ...
    def CreateRemesherBuilder(self) -> CAE.RemesherBuilder:
        ...
    def CreateElementRotateBuilder(self) -> CAE.ElementRotateBuilder:
        ...
    def CreateOpenDuctMeshBuilder(self, mesh: CAE.RecipeOpenDuctMesh) -> CAE.OpenDuctMeshBuilder:
        ...
    def CreateAcousticChamberMeshBuilder(self, mesh: CAE.RecipeAcousticChamberMesh) -> CAE.AcousticChamberMeshBuilder:
        ...
    def CreateMeshFromPointCloudBuilder(self) -> CAE.MeshFromPointCloudBuilder:
        ...
    def CreateAmSupportsMeshBuilder(self) -> CAE.AMSupportsMeshBuilder:
        ...
    def CreateGlobalAeroCsysBuilder(self) -> CAE.GlobalAeroCsysBuilder:
        ...
    def CreateWireframeFromDofsetBuilder(self) -> CAE.WireframeFromDOFSetBuilder:
        ...
    def CreateMeshSlicerBuilder(self) -> CAE.MeshSlicerBuilder:
        ...
    def CreateWireframeElementsBuilder(self) -> CAE.WireframeElementsBuilder:
        ...
    def CreateBendPipeEadBuilder(self) -> CAE.BendPipeEADBuilder:
        ...
    def Tag(self) -> Tag: ...

    ElemInfoUtils: CAE.ElementInfoUtils
    NodeInfoUtils: CAE.NodeInfoUtils
    ElemAssociatedDataUtils: CAE.ElementAssociatedDataUtils


class NodeElementInfoManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateNodeElementInfoBuilder(self) -> CAE.NodeElementInfoBuilder:
        ...
    def CreateThicknessBuilder(self, meshContext: CAE.Mesh) -> CAE.ThicknessBuilder:
        ...
    def CreateAssignNodalCsBuilder(self) -> CAE.AssignNodalCSBuilder:
        ...
    def CreateThicknessPlotContoursBuilder(self) -> CAE.ThicknessPlotContoursBuilder:
        ...
    def CreatePlotContoursBuilder(self) -> CAE.PlotContoursBuilder:
        ...
    def CreateDisplayNodalCsysBuilder(self) -> CAE.DisplayNodalCsysBuilder:
        ...
    def CreateShowElemNodeLabelsBuilder(self) -> CAE.ShowElemNodeLabelsBuilder:
        ...
    def Tag(self) -> Tag: ...



class NodeElementInfoBuilder(Builder):
    def __init__(self) -> None: ...
    Coordinates: bool
    Csys: bool
    Element: CAE.SelectElementsBuilder
    ElementConnectivity: bool
    ElementQuality: bool
    ElementType: bool
    EntityOption: CAE.NodeElementInfoBuilder.EntityType
    FormatOption: CAE.NodeElementInfoBuilder.FormatType
    Mesh: bool
    MeshCollector: bool
    Node: CAE.SelectFENodeList
    NodeConnectivity: bool
    PropertyOption: CAE.NodeElementInfoBuilder.PropertyType


    class PropertyType(enum.Enum):
        Brief = 0
        Detailed = 1
    

    class FormatType(enum.Enum):
        Tabular = 0
        General = 1
    

    class EntityType(enum.Enum):
        Node = 0
        Element = 1
    

class NodeDissociationBuilder(Builder):
    def __init__(self) -> None: ...
    Node: CAE.SelectFENodeList


class NodeDeleteBuilder(Builder):
    def __init__(self) -> None: ...
    Node: CAE.SelectFENodeList


class NodeCreateBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitNode(self) -> CAE.FENode:
        ...
    Csys: CoordinateSystem
    DispCsys: CoordinateSystem
    Increment: int
    Label: int
    PAngle: Expression
    Point: Point
    SingleOption: bool
    TAngle: Expression
    X: Expression
    Y: Expression
    Z: Expression


class NodeAssociationBuilder(Builder):
    def __init__(self) -> None: ...
    AssoAngle: Expression
    AssoDistance: Expression
    BodySelection: SelectTaggedObjectList
    MeshSelection: SelectTaggedObjectList


class NodeAlignBuilder(Builder):
    def __init__(self) -> None: ...
    MidNodeMove: bool
    Node: CAE.SelectFENodeList
    Point1: CAE.SelectFENode
    Point2: CAE.SelectFENode


class NodalForceReportBuilder(Builder):
    def __init__(self) -> None: ...
    AddAllForcesAndMoments: bool
    AllElems: bool
    AllNodes: bool
    CSysType: CAE.NodalForceReportBuilder.CSType
    CalculateMomentAboutPoint: bool
    Csys: CoordinateSystem
    Deformation: bool
    ElemRefs: CAE.SelectElementsBuilder
    ElemSelectEntities: CAE.TargetEntitiesBuilder
    ForceType: CAE.NodalForceReportBuilder.Force
    GridPointAppliedForce: bool
    GridPointAppliedForceElementNodal: bool
    GridPointForce: bool
    GridPointReactionForce: bool
    GridPointReactionForceMPC: bool
    LoadCaseIndex: int
    LoadCaseType: CAE.NodalForceReportBuilder.LoadcaseSelection
    NfrName: str
    NodeRefs: CAE.SelectFENodeList
    NodeSelectEntities: CAE.TargetEntitiesBuilder
    RefPoint: Point


    class LoadcaseSelection(enum.Enum):
        First = 0
        Last = 1
        SpecifyIndex = 2
        All = 3
    

    class Force(enum.Enum):
        GridPoint = 0
        Reaction = 1
        Mpc = 2
        Applied = 3
        Glue = 4
        Contact = 5
    

    class CSType(enum.Enum):
        Global = 0
        Cartesian = 1
        Cylindrical = 2
        Spherical = 3
    

class NodalForceReport(NXObject):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def CreateGraphAcrossIterations(self, forceTogglevalue: bool, momentToggleValue: bool, graphNamePrefix: str) -> None:
        ...


    class SubcaseOption(enum.Enum):
        UseSingle = 0
        UseAll = 1
    

    class ForceComponent(enum.Enum):
        GridPointForce = 0
        GridPointReactionForce = 1
        GridPointAppliedForce = 2
        GridPointReactionForceMPC = 3
        Reaction = 4
        Mpc = 5
        Applied = 6
        Glue = 7
        Contact = 8
        GridPointAppliedForceElementNodal = 9
    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class NamedPropTableWithTargetSet(CAE.NamedPropertyTable):
    def __init__(self) -> None: ...
    TargetSetManager: CAE.SetManager


class NamedPropertyTable(NXObject):
    def __init__(self) -> None: ...
    DescriptorType: str
    Label: int
    LanguageName: str
    PropertyTable: CAE.PropertyTable
    SolverName: str


class MultiTargetsetCopyBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSourceBc(self, bc: CAE.SimBC) -> None:
        ...
    def SetTargetBcs(self, bcs: typing.List[CAE.SimBC]) -> None:
        ...


class MultipleNodeCreateBuilder(Builder):
    def __init__(self) -> None: ...
    def AddNodes(self, positions: typing.List[Point3d]) -> None:
        ...
    def AddNodes(self, positions: typing.List[Point3d], labels: int) -> None:
        ...
    def CommitNodes(self) -> typing.List[CAE.FENode]:
        ...
    LabelIncrement: int
    StartLabel: int


class MultipleElementCreateBuilder(Builder):
    def __init__(self) -> None: ...
    def AddElement(self, nodes: typing.List[CAE.FENode]) -> None:
        ...
    def AddElement(self, nodes: typing.List[CAE.FENode], label: int) -> None:
        ...
    def CommitElements(self) -> typing.List[CAE.FEElement]:
        ...
    ElementType: CAE.ElementTypeBuilder
    LabelIncrement: int
    MeshName: str
    NewMeshOption: CAE.MultipleElementCreateBuilder.NewMeshType
    StartLabel: int


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

class MultipleCompanionResultBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitResult(self) -> typing.List[CAE.CompanionResult]:
        ...
    def SetCompanionResultFiles(self, filenames: str) -> None:
        ...
    def GetCompanionResultFiles(self) -> str:
        ...
    AppendMethod: CAE.CompanionResultBuilder.ResultAppendMethod
    Disposition: CAE.CompanionResultBuilder.CompanionResultDisposition


class MoveNodeBuilder(Builder):
    def __init__(self) -> None: ...
    SourceNode: CAE.SelectFENodeList
    TargetNode: CAE.SelectFENodeList


class MorphRevolvedMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def GetNodeMappedPoint(self, node: CAE.FENode) -> Point:
        ...
    def AddOrModifyNodeMap(self, node: CAE.FENode, point: Point) -> None:
        ...
    def RemoveNodeMap(self, node: CAE.FENode) -> None:
        ...
    def ReplaceNodeMap(self, oldNode: CAE.FENode, newNode: CAE.FENode, newPoint: Point) -> None:
        ...
    Axis: Axis
    Elements: CAE.SelectElementsBuilder
    FixedNodes: CAE.SelectFENodeList
    SourceNodes: CAE.SelectFENodeList
    TargetCurveType: CAE.MorphRevolvedMeshBuilder.CurveType
    TargetCurves: SelectDisplayableObjectList
    TargetLineEnd: Point
    TargetLineStart: Point


    class CurveType(enum.Enum):
        EdgeCurve = 0
        Line = 1
    

class ModifiableFEModelOccAttribute(CAE.FEModelOccAttribute):
    def __init__(self) -> None: ...
    def SetRepToBaseFem(self) -> None:
        ...
    def SetAltRepType(self, pcAltRepDescNeutralName: str, lengthUnits: CAE.FEModelOccAttribute.AltRepLengthUnitType, massUnits: CAE.FEModelOccAttribute.AltRepMassUnitType, femdataset: CAE.AlternateFemRepresentationSource, pcFileName: str) -> None:
        ...
    def ReloadSuperElementFile(self) -> None:
        ...


class ModeSetDataSourceBuilder(CAE.AlternateFemRepresentationDataSourceBuilder):
    def __init__(self) -> None: ...
    def GetAvailableModesets(self) -> str:
        ...
    def SelectModeset(self, modeSetName: str) -> None:
        ...
    def SetModesCanBeRenumbered(self, allowRenumbering: bool) -> None:
        ...


class ModeSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModeSet]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self, pModeSet: CAE.ModeSet) -> CAE.ModeSetBuilder:
        ...
    def Find(self, name: str) -> CAE.ModeSet:
        ...
    def Delete(self, modeSetTag: CAE.ModeSet) -> None:
        ...
    def CreateModalDampingIdentificationBuilder(self) -> CAE.ModalDampingIdentificationBuilder:
        ...
    def Tag(self) -> Tag: ...



class ModeSetBuilder(CAE.AlternateFemRepresentationSourceBuilder):
    def __init__(self) -> None: ...
    def GetAvailableModesets(self) -> str:
        ...
    def SelectModeset(self, modeSetName: str) -> None:
        ...
    def SetModesCanBeRenumbered(self, allowRenumbering: bool) -> None:
        ...


class ModeSet(CAE.AlternateFemRepresentationSource):
    def __init__(self) -> None: ...
    def GetNumberOfModes(self) -> int:
        ...
    def GetModeByIndex(self, index: int, label: int, status: bool, undampedFrequency: float, dampingRatio: float, modalMassReal: float, modalMassImg: float, annotation: str) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use GetModeInfoByIndex instead.")"""
        ...
    def GetModeInfoByIndex(self, index: int) -> CAE.ModeSet.ModeInfo:
        ...
    def GetAllModesInfos(self, modesInfos: typing.List[CAE.ModeSet.ModeInfo]) -> None:
        ...
    def SetModeStatus(self, label: int, status: bool) -> None:
        ...
    def SetModeStatus(self, dataSourceName: str, label: int, status: bool) -> None:
        ...
    def SetModeUndampedFrequency(self, label: int, undampedFrequency: float) -> None:
        ...
    def SetModeUndampedFrequency(self, dataSourceName: str, label: int, undampedFrequency: float) -> None:
        ...
    def SetModeDampingRatio(self, label: int, dampingRatio: float) -> None:
        ...
    def SetModeDampingRatio(self, dataSourceName: str, label: int, dampingRatio: float) -> None:
        ...
    def SetModeModalMass(self, label: int, modalMassReal: float, modalMassImg: float) -> None:
        ...
    def SetModeModalMass(self, dataSourceName: str, label: int, modalMassReal: float, modalMassImg: float) -> None:
        ...
    def SetModeAnnotation(self, label: int, annotation: str) -> None:
        ...
    def SetModeAnnotation(self, dataSourceName: str, label: int, annotation: str) -> None:
        ...
    def SetModeStructuralDampingFactor(self, label: int, structuralDampingFactor: float) -> None:
        ...
    def SetModeStructuralDampingFactor(self, dataSourceName: str, label: int, structuralDampingFactor: float) -> None:
        ...
    def SetModeViscousDampingFactor(self, label: int, viscousDampingFactor: float) -> None:
        ...
    def SetModeViscousDampingFactor(self, dataSourceName: str, label: int, viscousDampingFactor: float) -> None:
        ...


    class ModeSetModeInfo():
        Label: int
        ExportedIndex: int
        Status: bool
        UndampedFrequency: float
        DampingRatio: float
        ModalMassReal: float
        ModalMassImg: float
        StructuralDamping: float
        StructuralDampingFactor: float
        HasStructuralDamping: bool
        ViscousDamping: float
        ViscousDampingFactor: float
        HasViscousDamping: bool
        DataSourceName: str
        Annotation: str
        def ToString(self) -> str:
            ...
    

    class ModeSet_ModeInfo():
        label: int
        exported_index: int
        status: bool
        undamped_frequency: float
        damping_ratio: float
        modalMassReal: float
        modalMassImg: float
        structuralDamping: float
        structuralDampingFactor: float
        hasStructuralDamping: bool
        viscousDamping: float
        viscousDampingFactor: float
        hasViscousDamping: bool
        data_source_name: int
        annotation: int
    

class ModelUpdateSolutionSetDesignVariableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelUpdateDesignVariable]:
        ...
    def __init__(self, owner: CAE.ModelUpdateSolutionSet) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.ModelUpdateDesignVariable:
        ...
    def ResetDesignVariables(self) -> None:
        ...
    def SetDesignVariablesInitialValue(self, initialValue: float) -> None:
        ...
    def DesignVars(self, fileName: str) -> None:
        ...
    def DesignVars(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class ModelUpdateSolutionSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelUpdateSolutionSet]:
        ...
    def __init__(self, owner: CAE.CorrelManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSolutionSet(self, muSolsTags: typing.List[CAE.ModelUpdateSolution], name: str, modePairingMethod: CAE.CorrelModePairingBuilder.Auto, shapeCorrelationMethod: CAE.CorrelModePairingBuilder.ShapeCorrelation) -> CAE.ModelUpdateSolutionSet:
        ...
    def CreateSolutionSet(self, masterMUSol: CAE.ModelUpdateSolution, muSolsTags: typing.List[CAE.ModelUpdateSolution], name: str) -> CAE.ModelUpdateSolutionSet:
        ...
    def FindObject(self, solutionSetName: str) -> CAE.ModelUpdateSolutionSet:
        ...
    def DeleteSolutionSet(self, solnSetTag: CAE.ModelUpdateSolutionSet) -> None:
        ...
    def UpdateFiniteElementModel(self, solnSetTag: CAE.ModelUpdateSolutionSet) -> None:
        ...
    def CloneSolutionset(self, sourceSolnSetTag: CAE.ModelUpdateSolutionSet) -> CAE.ModelUpdateSolutionSet:
        ...
    def Tag(self) -> Tag: ...

    ActiveSolutionSet: CAE.ModelUpdateSolutionSet


class ModelUpdateSolutionSet(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...
    def SetMaster(self, muSol: CAE.ModelUpdateSolution) -> None:
        ...
    def ClearMaster(self) -> None:
        ...
    def SetFreqTargetActive(self, solutionIndex: int, targetIndex: int, active: bool) -> None:
        ...
    def SetModeShapeTargetActive(self, solutionIndex: int, targetIndex: int, active: bool) -> None:
        ...
    def UpdateDesignVariables(self) -> None:
        ...
    def Information(self) -> None:
        ...
    def Error(self) -> None:
        ...
    def Error(self, fileName: str) -> None:
        ...
    def CalculateErrors(self) -> None:
        ...
    def CreateOptionsBuilder(self) -> CAE.ModelUpdateOptionsBuilder:
        ...
    def CreateOptimOptionsBuilder(self) -> CAE.ModelUpdateOptimOptionsBuilder:
        ...
    def TargetsInformation(self, setTargetIndex: int, targetsType: CAE.ModelUpdateSolution.TargetType) -> None:
        ...
    def TargetsReset(self) -> None:
        ...
    def TargetsCsvExport(self, setTargetIndex: int, targetsType: CAE.ModelUpdateSolution.TargetType, fileName: str) -> None:
        ...
    def SetFreqTargetWeight(self, solutionIndex: int, targetIndex: int, newWeight: float) -> None:
        ...
    def SetModeShapeTargetWeight(self, solutionIndex: int, targetIndex: int, newWeight: float) -> None:
        ...
    def ErrorsInformation(self, solutionIndex: int, targetsType: CAE.ModelUpdateSolution.TargetType) -> None:
        ...
    def ExportErrorsCsvFile(self, solutionIndex: int, targetType: CAE.ModelUpdateSolution.TargetType, fileName: str) -> None:
        ...
    DesignVariables: CAE.ModelUpdateSolutionSetDesignVariableCollection
    ModePairingMethod: CAE.CorrelModePairingBuilder.Auto
    ShapeCorrelationMethod: CAE.CorrelModePairingBuilder.ShapeCorrelation


class ModelUpdateSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelUpdateSolution]:
        ...
    def __init__(self, owner: CAE.CorrelManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSolutionBuilder(self, solution: CAE.ModelUpdateSolution) -> CAE.ModelUpdateSolutionBuilder:
        ...
    def FindObject(self, solutionName: str) -> CAE.ModelUpdateSolution:
        ...
    def CreateSensitivityViewerBuilder(self, solution: CAE.ModelUpdateSolution) -> CAE.ModelUpdateSensitivityViewerBuilder:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ModelUpdateSolution.PlotSensitivities instead.")"""
        ...
    def Tag(self) -> Tag: ...

    ActiveSolution: CAE.ModelUpdateSolution


class ModelUpdateSolutionBuilder(CAE.CorrelSolutionBuilder):
    def __init__(self) -> None: ...


class ModelUpdateSolution(CAE.CorrelSolution):
    def __init__(self) -> None: ...
    def CreateOptionsBuilder(self) -> CAE.ModelUpdateOptionsBuilder:
        ...
    def CreateOptimOptionsBuilder(self) -> CAE.ModelUpdateOptimOptionsBuilder:
        ...
    def GetDesignVarNumber(self) -> int:
        ...
    def SetDesignVarActive(self, designVarIndex: int, active: bool) -> None:
        ...
    def SetDesignVarValue(self, designVarIndex: int, value: float) -> None:
        ...
    def SetDesignVarLowerBound(self, designVarIndex: int, lowerBound: float) -> None:
        ...
    def SetDesignVarUpperBound(self, designVarIndex: int, upperBound: float) -> None:
        ...
    def SetDesignVarWeight(self, designVarIndex: int, weight: float) -> None:
        ...
    def CalculateErrors(self) -> None:
        ...
    def ResetDesignVariables(self) -> None:
        ...
    def SetDesignVariablesInitialValue(self, initialValue: float) -> None:
        ...
    def ResetTargets(self) -> None:
        ...
    def SetFreqTargetActive(self, freqTargetIndex: int, active: bool) -> None:
        ...
    def SetModeShapeTargetActive(self, modeShapeTargetIndex: int, active: bool) -> None:
        ...
    def SetFreqTargetWeight(self, freqTargetIndex: int, weight: float) -> None:
        ...
    def SetModeShapeTargetWeight(self, modeShapeTargetIndex: int, modeShapeWeight: float) -> None:
        ...
    def CreateOverallWeightsBuilder(self) -> CAE.ModelUpdateOverallWeightsBuilder:
        ...
    def CreateCorrelMethodBuilder(self) -> CAE.ModelUpdateCorrelMethodBuilder:
        """[Obsolete("Deprecated in NX1926.0.0.  Please use the builder NXOpen.CAE.CorrelModePairingBuilder to set correlation method.")"""
        ...
    def UpdateDesignVariables(self) -> None:
        ...
    def UpdateFiniteElementModel(self) -> None:
        ...
    def ExportDesignVariablesCsvFile(self, fileName: str) -> None:
        ...
    def ExportSensitivitiesCsvFile(self, fileName: str) -> None:
        ...
    def ExportErrorsCsvFile(self, targetType: CAE.ModelUpdateSolution.TargetType, fileName: str) -> None:
        ...
    def ExportTargetsCsvFile(self, tagetType: CAE.ModelUpdateSolution.TargetType, fileName: str) -> None:
        ...
    def CloneModelupdate(self) -> CAE.ModelUpdateSolution:
        ...
    def GetDesignVariables(self) -> typing.List[CAE.ModelUpdateDesignVariable]:
        ...
    def PlotSensitivities(self, device: int, viewIndex: int) -> None:
        ...
    def TargetsInformation(self, targetsType: CAE.ModelUpdateSolution.TargetType) -> None:
        ...
    def ErrorsInformation(self, targetsType: CAE.ModelUpdateSolution.TargetType) -> None:
        ...
    DesignVariables: CAE.ModelUpdateDesignVariablesCollection


    class TargetType(enum.Enum):
        All = 0
        Frequencies = 1
        ModeShapes = 2
    

class ModelUpdateSensitivityViewerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTargetIds(self, targetIds: int) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ModelUpdateSolution.PlotSensitivities instead.")"""
        ...
    def SetTargetIds(self, targetIds: int) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ModelUpdateSolution.PlotSensitivities instead.")"""
        ...
    def GetDesignVariableLabels(self) -> str:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ModelUpdateSolution.PlotSensitivities instead.")"""
        ...
    def SetDesignVariableLabels(self, designVaraibleLabels: str) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ModelUpdateSolution.PlotSensitivities instead.")"""
        ...
    def GetSensitivityValues(self) -> float:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ModelUpdateSolution.PlotSensitivities instead.")"""
        ...
    def SetSensitivityValues(self, sensitivityValues: float) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ModelUpdateSolution.PlotSensitivities instead.")"""
        ...


class ModelUpdateOverallWeightsBuilder(Builder):
    def __init__(self) -> None: ...
    Frequencies: float
    ModeShapes: float


class ModelUpdateOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    RigidBodyTolerance: float
    UpperBoundMultiplier: float


class ModelUpdateOptimOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    def Optimize(self) -> None:
        ...
    DesignVarLinearRange: float
    DesignVarWeight: float
    GaOptNumGenerations: int
    GaOptNumGenes: int
    GaOptNumIndividuals: int
    LeastSqrAutoFilter: bool
    MaxIterations: int
    Method: CAE.ModelUpdateOptimOptionsBuilder.MethodChoice
    MinImprovement: float
    SteepestDescDVarStep: float
    SteepestDescMaxInnerIter: int
    SteepestDescMethod: CAE.ModelUpdateOptimOptionsBuilder.SteepestDescMethodChoice


    class SteepestDescMethodChoice(enum.Enum):
        Linear = 0
        Fractional = 1
    

    class MethodChoice(enum.Enum):
        LeastSquares = 0
        SteepestDescent = 1
        GeneticAlgorithm = 2
    

class ModelUpdateDesignVariablesRapidCreateBuilder(Builder):
    def __init__(self) -> None: ...
    def SelectEntity(self, entityName: str) -> None:
        ...
    def SelectAllEntities(self) -> None:
        ...
    def DeselectAllEntities(self) -> None:
        ...
    def SelectField(self, field: str) -> None:
        ...
    def SelectAllFields(self) -> None:
        ...
    def DeselectAllFields(self) -> None:
        ...
    CardName: str
    DesignVariableType: CAE.ModelUpdateDesignVariablesRapidCreateBuilder.DesignVariableTypeEnum
    HasInitialValue: bool
    HasLowerBound: bool
    HasUpperBound: bool
    InitialValue: float
    LowerBound: float
    MaterialTypes: CAE.ModelUpdateDesignVariablesRapidCreateBuilder.MaterialTypesEnum
    NameSeed: str
    PhysicalTypes: CAE.ModelUpdateDesignVariablesRapidCreateBuilder.PhysicalTypesEnum
    UpperBound: float


    class PhysicalTypesEnum(enum.Enum):
        Pbar = 0
        Pbarl = 1
        Pbeam = 2
        Pbeaml = 3
        Pbush = 4
        Pdamp = 5
        Pelas = 6
        Pgap = 7
        Pmass = 8
        Prod = 9
        Pshear = 10
        Pshell = 11
        Ptube = 12
        Pvisc = 13
    

    class MaterialTypesEnum(enum.Enum):
        Mat1 = 0
        Mat2 = 1
        Mat3 = 2
        Mat8 = 3
        Mat9 = 4
    

    class DesignVariableTypeEnum(enum.Enum):
        Material = 0
        Physical = 1
    

class ModelUpdateDesignVariablesCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelUpdateDesignVariable]:
        ...
    def __init__(self, owner: CAE.ModelUpdateSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.ModelUpdateDesignVariable:
        ...
    def Tag(self) -> Tag: ...



class ModelUpdateDesignVariable(NXObject):
    def __init__(self) -> None: ...
    def GetDesignVariableModelingObject(self) -> CAE.ModelingObjectPropertyTable:
        ...
    def GetActivityStatus(self) -> bool:
        ...
    def SetActivityStatus(self, active: bool) -> None:
        ...
    def GetWeight(self) -> float:
        ...
    def SetWeight(self, weight: float) -> None:
        ...
    def GetLowerBound(self) -> float:
        ...
    def SetLowerBound(self, lowerBound: float) -> None:
        ...
    def GetUpperBound(self) -> float:
        ...
    def SetUpperBound(self, upperBound: float) -> None:
        ...
    def GetValue(self) -> float:
        ...
    def SetValue(self, value: float) -> None:
        ...


class ModelUpdateCorrelMethodBuilder(Builder):
    def __init__(self) -> None: ...
    CorrelMethod: CAE.ModelUpdateCorrelMethodBuilder.Method


    class Method(enum.Enum):
        Mac = 0
        XOrtho = 1
    

class ModelingObjectPropertyTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelingObjectPropertyTable]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateModelingObjectPropertyTable(self, descriptorType: str, languageName: str, solverName: str, name: str, label: int) -> CAE.ModelingObjectPropertyTable:
        ...
    def CopyModelingObjectPropertyTable(self, sourceModelingObjectPropertyTable: CAE.ModelingObjectPropertyTable) -> CAE.ModelingObjectPropertyTable:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.ModelingObjectPropertyTable:
        ...
    def Filter(self, filterByType: bool, filterType: int, filterByName: bool, filterName: str, filterByLowerLabelBound: bool, lowerLabelBound: int, filterByUpperLabelBound: bool, upperLabelBound: int, found: typing.List[CAE.ModelingObjectPropertyTable]) -> None:
        ...
    def Tag(self) -> Tag: ...



class ModelingObjectPropertyTable(CAE.NamedPropertyTable):
    def __init__(self) -> None: ...
    def GetSolverCardSyntax(self) -> str:
        ...


class ModelDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    def SetColorsOnMeshes(self) -> None:
        ...
    def SetDisplayParametersByConnectionType(self, connectionType: CAE.Connections.ConnectionType, parameters: CAE.ModelDisplayBuilder.ConnectionDisplayParameters) -> None:
        ...
    def GetDisplayParametersByConnectionType(self, connectionType: CAE.Connections.ConnectionType) -> CAE.ModelDisplayBuilder.ConnectionDisplayParameters:
        ...
    def SetDisplayParametersByFlangeCount(self, flangeCount: CAE.ModelDisplayBuilder.ConnectionFlangeCount, parameters: CAE.ModelDisplayBuilder.ConnectionDisplayParameters) -> None:
        ...
    def GetDisplayParametersByFlangeCount(self, flangeCount: CAE.ModelDisplayBuilder.ConnectionFlangeCount) -> CAE.ModelDisplayBuilder.ConnectionDisplayParameters:
        ...
    def SetDisplayParametersByStatus(self, status: CAE.ModelDisplayBuilder.ConnectionStatus, parameters: CAE.ModelDisplayBuilder.ConnectionDisplayParameters) -> None:
        ...
    def GetDisplayParametersByStatus(self, status: CAE.ModelDisplayBuilder.ConnectionStatus) -> CAE.ModelDisplayBuilder.ConnectionDisplayParameters:
        ...
    def AddDisplayParametersByDiameter(self, minimum: Expression, maximum: Expression, parameters: CAE.ModelDisplayBuilder.ConnectionDisplayParameters) -> None:
        ...
    def GetParametersByDiameterRangeIndex(self, index: int, minimum: Expression, maximum: Expression) -> CAE.ModelDisplayBuilder.ConnectionDisplayParameters:
        ...
    def UpdateParametersByDiameterRangeIndex(self, index: int, parameters: CAE.ModelDisplayBuilder.ConnectionDisplayParameters) -> None:
        ...
    def RemoveDiameterRange(self, index: int) -> None:
        ...
    ColorPolygonBodies: bool
    DisplayColorBar: bool
    ElemMaterialDisplayLaminateColor: NXColor
    ElemMaterialDisplayNoMaterialColor: NXColor
    ElemQualFailColor: NXColor
    ElemQualFailShadedBorderColor: NXColor
    ElemQualPassColor: NXColor
    ElemQualPassTranslucency: int
    ElemQualPassType: CAE.ModelDisplayBuilder.ElemQualPass
    ElementColorCycler: CAE.ModelDisplayBuilder.ElmClrBasis
    ElementDisplayQuality: CAE.ModelDisplayBuilder.ElmDispQuality
    ElementSelectInternal: bool
    GeomDisplayFreeEdges: bool
    GeomDisplayStitchedEdges: bool
    GeomFaceResolveDisplayContention: bool
    GeomFreeEdgeColor: NXColor
    GeomFreeEdgeEndMarker: CAE.ModelDisplayBuilder.FreeEdgeMarker
    GeomFreeEdgeFont: CAE.ModelDisplayBuilder.FreeEdgeFont
    GeomFreeEdgeLineWidth: CAE.ModelDisplayBuilder.FreeEdgeWidth
    GeomStitchedEdgeColor: NXColor
    GeomStitchedEdgeEndMarker: CAE.ModelDisplayBuilder.StitchedEdgeMarker
    GeomStitchedEdgeFont: CAE.ModelDisplayBuilder.StitchedEdgeFont
    GeomStitchedEdgeLineWidth: CAE.ModelDisplayBuilder.StitchedEdgeWidth
    GroupElemFaceMultiGroupColor: NXColor
    GroupElemFaceNoGroupColor: NXColor
    GroupElemMultiGroupColor: NXColor
    GroupElemNoGroupColor: NXColor
    GroupSelRecipeOpts: CAE.ModelDisplayBuilder.GroupPreference
    Include2dElements: bool
    LamZoneElemNoColor: NXColor
    NodeColor: NXColor
    NodeDisplayMode: CAE.ModelDisplayBuilder.NodeDisplayModeType
    NodeMarker: CAE.ModelDisplayBuilder.NodeMarkerType
    NodeMeshShowHideOption: CAE.ModelDisplayBuilder.NodeMeshShowHideOptionType
    NodeSelectInternal: bool
    NodeUnattachedMarker: CAE.ModelDisplayBuilder.NodeUnattachedMarkerType
    NumberOfDiameterRanges: int
    RotationAxisColor: NXColor
    RotationAxisDisplaySwitch: bool
    RotationAxisFont: CAE.ModelDisplayBuilder.RotationAxisLineFont
    RotationAxisLineWidth: CAE.ModelDisplayBuilder.RotationAxisWidth
    SolverDisplayMode: str
    UnattachedNodesInBoundingBoxRatio: float
    UniversalConnectionVisualizationType: CAE.ModelDisplayBuilder.UniversalConnectionVisualizationSettingsType


    class UniversalConnectionVisualizationSettingsType(enum.Enum):
        None = 0
        ByType = 1
        ByDiameter = 2
        ByFlangeCount = 3
        ByStatus = 4
    

    class StitchedEdgeWidth(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class StitchedEdgeMarker(enum.Enum):
        None = 0
        Plus = 1
        Dot = 2
        Asterisk = 3
        Circle = 4
        Poundsign = 5
        Cross = 6
        Square = 7
        Triangle = 8
        Diamond = 9
        CenterLine = 10
    

    class StitchedEdgeFont(enum.Enum):
        Solid = 0
        Dashed = 1
        Phantom = 2
        Centerline = 3
        Dotted = 4
        LongDashed = 5
        DottedDashed = 6
        Eight = 7
        Nine = 8
        Ten = 9
        Eleven = 10
    

    class RotationAxisWidth(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class RotationAxisLineFont(enum.Enum):
        Solid = 0
        Dashed = 1
        Phantom = 2
        Centerline = 3
        Dotted = 4
        LongDashed = 5
        DottedDashed = 6
        Eight = 7
        Nine = 8
        Ten = 9
        Eleven = 10
    

    class NodeUnattachedMarkerType(enum.Enum):
        None = 0
        Dot = 1
        Asterisk = 2
        FilledCircle = 3
        BigAsterisk = 4
    

    class NodeMeshShowHideOptionType(enum.Enum):
        Exterior = 0
        All = 1
        None = 2
    

    class NodeMarkerType(enum.Enum):
        None = 0
        Dot = 1
        Asterisk = 2
        FilledCircle = 3
        BigAsterisk = 4
    

    class NodeDisplayModeType(enum.Enum):
        Implicit = 0
        Explicit = 1
    

    class GroupPreference(enum.Enum):
        GroupOnly = 0
        SelRecipeOnly = 1
        Both = 2
    

    class FreeEdgeWidth(enum.Enum):
        Thin = 0
        Normal = 1
        Thick = 2
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class FreeEdgeMarker(enum.Enum):
        None = 0
        Plus = 1
        Dot = 2
        Asterisk = 3
        Circle = 4
        Poundsign = 5
        Cross = 6
        Square = 7
        Triangle = 8
        Diamond = 9
        CenterLine = 10
    

    class FreeEdgeFont(enum.Enum):
        Solid = 0
        Dashed = 1
        Phantom = 2
        Centerline = 3
        Dotted = 4
        LongDashed = 5
        DottedDashed = 6
        Eight = 7
        Nine = 8
        Ten = 9
        Eleven = 10
    

    class ElmDispQuality(enum.Enum):
        Coarse = 0
        Medium = 1
        Fine = 2
    

    class ElmClrBasis(enum.Enum):
        Default = 0
        PhysicalPropertyTable = 1
        MaterialPropertyTable = 2
        ElemCollContainer = 3
        ElemColl = 4
        ElemQualityCheck = 5
        GroupElem = 6
        GroupElemFace = 7
        ProtoElemColl = 8
        LamZoneElem = 9
        SolverSpecific = 10
    

    class ElemQualPass(enum.Enum):
        Shaded = 0
        Wireframe = 1
    

    class ConnectionStatus(enum.Enum):
        Realized = 1
        NotRealized = 2
        Invalid = 3
    

    class ConnectionFlangeCount(enum.Enum):
        TwoFlanges = 2
        ThreeFlanges = 3
        FourFlanges = 4
        Other = 5
    

    class ModelDisplayBuilderConnectionDisplayParameters():
        Color: NXColor
        LineFont: DisplayableObject.ObjectFont
        LineWidth: DisplayableObject.ObjectWidth
        def ToString(self) -> str:
            ...
        def __init__(self, Color: NXColor, LineFont: DisplayableObject.ObjectFont, LineWidth: DisplayableObject.ObjectWidth) -> None: ...
    

    class ModelDisplayBuilder_ConnectionDisplayParameters():
        color: int
        lineFont: DisplayableObject.ObjectFont
        lineWidth: DisplayableObject.ObjectWidth
    

class ModelCheckManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateMechanicalLoadSumBuilder(self) -> CAE.MechanicalLoadSumBuilder:
        ...
    def CreateSolidPropertyCheckBuilder(self) -> CAE.SolidPropertyCheckBuilder:
        ...
    def CreateElementEdgeCheckBuilder(self) -> CAE.ModelCheck.ElementEdgeCheckBuilder:
        ...
    def CreateReverseShellElementNormalBuilder(self) -> CAE.ModelCheck.ReverseShellElementNormalBuilder:
        ...
    def CreateAlignShellElementNormalBuilder(self) -> CAE.ModelCheck.AlignShellElementNormalBuilder:
        ...
    def CreateSolidElementFaceNormalBuilder(self) -> CAE.ModelCheck.SolidElementFaceNormalBuilder:
        ...
    def CreateDuplicateNodesCheckBuilder(self) -> CAE.ModelCheck.DuplicateNodesCheckBuilder:
        ...
    def CreateDuplicateElementsCheckBuilder(self) -> CAE.ModelCheck.DuplicateElementsCheckBuilder:
        ...
    def CreateFaceClearanceCheckBuilder(self) -> CAE.ModelCheck.FaceClearanceCheckBuilder:
        ...
    def CreateElementMaterialOrientationCheckBuilder(self) -> CAE.ModelCheck.ElementMaterialOrientationCheckBuilder:
        ...
    def CreateElementQualityCheckBuilder(self) -> CAE.ModelCheck.ElementQualityCheckBuilder:
        ...
    def CreateModelSetupCheckBuilder(self) -> CAE.ModelCheck.ModelSetupCheckBuilder:
        ...
    def CheckModelConsistency(self, logFileName: str, caeBodySet: CAE.CaeGroup) -> bool:
        ...
    def CreateAlignShellElementFirstEdgeBuilder(self) -> CAE.ModelCheck.AlignShellElementFirstEdgeBuilder:
        ...
    def CreateReverseBeamElementDirectionBuilder(self) -> CAE.ModelCheck.ReverseBeamElementDirectionBuilder:
        ...
    def CreateAlignBeamElementDirectionBuilder(self) -> CAE.ModelCheck.AlignBeamElementDirectionBuilder:
        ...
    def CreateAeroMeshCheckBuilder(self) -> CAE.AeroMeshCheckBuilder:
        ...
    def CreateSolverElementQualityChecker(self, solverName: str) -> CAE.ModelCheck.IElementQualityChecker:
        ...
    def CreateCorrectBeamElementsBuilder(self) -> CAE.ModelCheck.CorrectBeamElementsBuilder:
        ...
    def Tag(self) -> Tag: ...



class ModelAndLoadPreProcessWaterfallToOrderCutBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    FrequencyBandwidth: Expression
    Method: int
    NumberOfFrequencies: int
    OrderBandwidth: float
    OrderEnd: float
    OrderStart: float
    OrderStep: float
    PercentageOrder: float


class ModelAndLoadPreProcessWaterfallToOrderCut(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessVibrationConversionBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    TargetVibration: CAE.ModelAndLoadPreProcessVibrationConversionBuilder.VibrationType


    class VibrationType(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
    

class ModelAndLoadPreProcessVibrationConversion(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessTimeToWaterfallBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    def SetRpmFunction(self, functionSelectionTypes: typing.List[CAE.ModelAndLoadPreProcessTimeToWaterfallBuilder.FunctionVariableEnum], functionSelectionValues: str) -> None:
        ...
    FrameSizeSamples: int
    FrameSizeTime: Expression
    FrameSizeType: CAE.ModelAndLoadPreProcessTimeToWaterfallBuilder.FrameSizeTypeEnum
    RpmEnd: Expression
    RpmFunctionDefinitionType: CAE.ModelAndLoadPreProcessTimeToWaterfallBuilder.RpmFunctionDefinitionTypeEnum
    RpmFunctionField: Fields.ScalarFieldWrapper
    RpmStart: Expression
    RpmStep: Expression
    RpmTolerance: float
    TimeStepTolerance: float


    class RpmFunctionDefinitionTypeEnum(enum.Enum):
        FromFile = 0
        FromField = 1
    

    class FunctionVariableEnum(enum.Enum):
        ElementName = 0
        VariableName = 1
        FirstMarkerPosition = 2
        SecondMarkerPosition = 3
        Node = 4
        Subcase = 5
    

    class FrameSizeTypeEnum(enum.Enum):
        Time = 0
        Samples = 1
    

class ModelAndLoadPreProcessTimeToWaterfall(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessTimeSignalBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    AveragingType: CAE.ModelAndLoadPreProcessTimeSignalBuilder.AveragingTypeEnum
    BlockSize: int
    CorrectionMode: CAE.ModelAndLoadPreProcessTimeSignalBuilder.CorrectionModeEnum
    Enable0Padding: bool
    EnableAveraging: bool
    EnableFFT: bool
    EnableLowerFrequencyLimit: bool
    EnablePrePadding: bool
    EnableSignalRepetition: bool
    EnableTimeSegmentation: bool
    EnableUpperFrequencyLimit: bool
    FrequencyResolution: Expression
    LowerFrequencyLimit: Expression
    LowerLimitType: CAE.ModelAndLoadPreProcessTimeSignalBuilder.TimeLimitEnum
    LowerSampleLimit: int
    LowerTimeLimit: Expression
    NumberOfRepetitions: int
    Overlap: float
    TimeStepTolerance: float
    UpperFrequencyLimit: Expression
    UpperLimitType: CAE.ModelAndLoadPreProcessTimeSignalBuilder.TimeLimitEnum
    UpperSampleLimit: int
    UpperTimeLimit: Expression
    WindowType: CAE.ModelAndLoadPreProcessTimeSignalBuilder.WindowTypeEnum


    class WindowTypeEnum(enum.Enum):
        Rectangular = 0
        Hanning = 1
        Hamming = 2
        KaiserBessel = 3
        Blackman = 4
        FlatTop = 5
    

    class TimeLimitEnum(enum.Enum):
        None = 0
        Time = 1
        Samples = 2
    

    class CorrectionModeEnum(enum.Enum):
        Amplitude = 0
    

    class AveragingTypeEnum(enum.Enum):
        AmplitudePhaseLinear = 0
        MaximumPeakHold = 1
        RMSEnergy = 2
        RealImaginaryLinear = 3
    

class ModelAndLoadPreProcessTimeSignal(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessTblBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    def GetUserParameters(self, userParamNames: str, userParameters: typing.List[Expression]) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use the accessors in the contained AcousticsAndVibrationTblModelParametersAccessor instead.")"""
        ...
    AutoSpectrumField: Fields.FieldWrapper
    AutoSpectrumType: CAE.ModelAndLoadPreProcessTblBuilder.AsType
    BoundaryLayerThicknessParam: Expression
    ConvectiveVelocityXParam: Expression
    ConvectiveVelocityYParam: Expression
    ConvectiveVelocityZParam: Expression
    CorrelationDecayRateAlphaParam: Expression
    CorrelationDecayRateBetaParam: Expression
    CorrelationSpectrumType: CAE.ModelAndLoadPreProcessTblBuilder.CsType
    CorrelationSpectrumUserDLL: str
    DeltaKx: Expression
    DeltaKy: Expression
    DisplacementThicknessParam: Expression
    EnableRandomSampling: bool
    FluidDensityParam: Expression
    FluidOuterVelocityParam: Expression
    FluidViscosityParam: Expression
    FormulationType: CAE.ModelAndLoadPreProcessTblBuilder.Formulation
    FrequencyOptions: CAE.ModelAndLoadPreProcessFrequencyOptions
    MaxKx: Expression
    MaxKy: Expression
    MinKx: Expression
    MinKy: Expression
    MomentumThicknessParam: Expression
    NumRandomSamples: int
    RegionSelector: SelectTaggedObjectList
    ScaleLoads: bool
    SoundSpeedParam: Expression
    TblModel: CAE.AcousticsAndVibrationTblModelParametersAccessor
    WallFrictionVelocityParam: Expression
    WallShearStressParam: Expression


    class Formulation(enum.Enum):
        WaveNumberDomain = 0
        SpatialCholesky = 1
    

    class CsType(enum.Enum):
        Corcos = 0
        Efimtsov = 1
        Chase = 2
        UserDefined = 3
    

    class AsType(enum.Enum):
        RobertCorcos = 0
        Efimtsov = 1
        Goody = 2
        Smolyakov = 3
        CockburnRobertson = 4
        SmolyakovTkachenko = 5
        ChaseHowe = 6
        UserDefined = 7
    

class ModelAndLoadPreProcessTbl(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessPressureToForceBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessPressureToForce(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessor(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelAndLoadPreProcess]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.ModelAndLoadPreProcess:
        ...
    def Create(self) -> CAE.ModelAndLoadPreProcess:
        ...
    def CreateBuilder(self, metasolution: CAE.ModelAndLoadPreProcess) -> CAE.ModelAndLoadPreProcessBuilder:
        ...
    def DeleteModelAndLoadPreProcess(self, metasolution: CAE.ModelAndLoadPreProcess) -> None:
        ...
    def CloneMetasolution(self, source: CAE.ModelAndLoadPreProcess) -> CAE.ModelAndLoadPreProcess:
        ...
    def Tag(self) -> Tag: ...



class ModelAndLoadPreProcessOperations(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelAndLoadPreProcessOperation]:
        ...
    def __init__(self, owner: CAE.ModelAndLoadPreProcess) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.ModelAndLoadPreProcessOperation:
        ...
    def DeleteOperation(self, blockTag: CAE.ModelAndLoadPreProcessOperation) -> None:
        ...
    def CreateBuilder(self, operationTypeString: str) -> CAE.ModelAndLoadPreProcessOperationBuilder:
        ...
    def EditBuilder(self, baseOp: CAE.ModelAndLoadPreProcessOperation) -> CAE.ModelAndLoadPreProcessOperationBuilder:
        ...
    def Tag(self) -> Tag: ...



class ModelAndLoadPreProcessOperationBuilder(Builder):
    def __init__(self) -> None: ...
    OperationName: str


class ModelAndLoadPreProcessOperation(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...


class ModelAndLoadPreProcessMeshMappingDatas(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ModelAndLoadPreProcessMeshMappingData]:
        ...
    def __init__(self, owner: CAE.ModelAndLoadPreProcessMeshMapping) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.ModelAndLoadPreProcessMeshMappingData:
        ...
    def DeleteMappingdata(self, blockTag: CAE.ModelAndLoadPreProcessMeshMappingData) -> None:
        ...
    def CreateBuilder(self) -> CAE.ModelAndLoadPreProcessMeshMappingDataBuilder:
        ...
    def EditBuilder(self, baseOp: CAE.ModelAndLoadPreProcessMeshMappingData) -> CAE.ModelAndLoadPreProcessMeshMappingDataBuilder:
        ...
    def Tag(self) -> Tag: ...



class ModelAndLoadPreProcessMeshMappingDataBuilder(Builder):
    def __init__(self) -> None: ...
    def SetIntermediateEntities(self, slot: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.IntermediateSlot, entityType: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.IntermediateEntity, intermediateEntities: int) -> None:
        ...
    def SetIntermediateMeshGroups(self, slot: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.IntermediateSlot, meshGroupNames: str) -> None:
        ...
    MatrixFilePath: str
    MaximumDistance: Expression
    Method: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.MappingMethod
    ModelSelection: SelectTaggedObjectList
    Name: str
    NumInflNodes: int
    SourceModelSelection: SelectTaggedObjectList
    SourceSelectionType: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.SourceSelectionTypeEnum
    TargetCriterion: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.SelectionCriterion
    TargetDataCsysType: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.TargetDataCsysTypeEnum
    TargetModelSelection: SelectTaggedObjectList
    TargetSelectionType: CAE.ModelAndLoadPreProcessMeshMappingDataBuilder.TargetSelectionTypeEnum


    class TargetSelectionTypeEnum(enum.Enum):
        ModelMeshSelection = 0
        IntermediaryMeshSelection = 1
        SourceMeshSelection = 2
    

    class TargetDataCsysTypeEnum(enum.Enum):
        Absolute = 0
        Native = 1
    

    class SourceSelectionTypeEnum(enum.Enum):
        IntermediaryMeshSelection = 0
        AllMesh = 1
        ModelMeshSelection = 2
    

    class SelectionCriterion(enum.Enum):
        ModelEntities = 0
        IntermediaryEntities = 1
    

    class MappingMethod(enum.Enum):
        MaximumDistance = 0
        ConservativeMaximumDistance = 1
        NearestNeighbour = 2
        Matrix = 3
    

    class IntermediateSlot(enum.Enum):
        Source = 0
        Target = 1
    

    class IntermediateEntity(enum.Enum):
        None = 0
        Node = 1
        Element = 2
        ElementFace = 3
    

class ModelAndLoadPreProcessMeshMappingData(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...


class ModelAndLoadPreProcessMeshMappingBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    DoDataTransfer: bool
    ExportMappingGroups: bool
    ExportMeshMappingMatrix: bool
    ExportMeshMappingMatrixBinary: bool
    GroupsFile: str
    GroupsToExport: CAE.ModelAndLoadPreProcessMeshMappingBuilder.ExportGroups
    MeshMappingMatrixFile: str
    SourceGroupFile: str
    SourceMeshDynamicType: CAE.ModelAndLoadPreProcessMeshMappingBuilder.SourceMeshDynamicTypeEnum
    SourceMeshRotationAxis: Axis
    SourceMeshRotationDataInRelativeCsys: bool
    SourceMeshRotationRemoveRigidBodyDisplacement: bool
    SourceMeshRotationRpm: Fields.ScalarFieldWrapper
    TargetGroupFile: str


    class SourceMeshDynamicTypeEnum(enum.Enum):
        Stationary = 0
        Rotating = 1
    

    class ExportGroups(enum.Enum):
        Source = 0
        Target = 1
        BothInOneFile = 2
        BothInTwoFiles = 3
    

class ModelAndLoadPreProcessMeshMapping(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...
    Datas: CAE.ModelAndLoadPreProcessMeshMappingDatas


class ModelAndLoadPreProcessLoadExtrusionBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    def SetRegionSelection(self, intermediateEntities: int) -> None:
        ...
    Distance: Expression
    DistanceCriterion: CAE.ModelAndLoadPreProcessLoadExtrusionBuilder.DistanceCriterionEnum
    NumCopies: int


    class DistanceCriterionEnum(enum.Enum):
        PerCopy = 0
        Total = 1
    

class ModelAndLoadPreProcessLoadExtrusion(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessInverseFftBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    EnableLowerTimeLimit: bool
    EnableUpperTimeLimit: bool
    FrequencyLowerLimitType: CAE.ModelAndLoadPreProcessInverseFftBuilder.FrequencyLimitEnum
    FrequencyLowerSampleLimit: int
    FrequencyLowerValueLimit: Expression
    FrequencyUpperLimitType: CAE.ModelAndLoadPreProcessInverseFftBuilder.FrequencyLimitEnum
    FrequencyUpperSampleLimit: int
    FrequencyUpperValueLimit: Expression
    LowerTimeLimit: Expression
    Tolerance: float
    UpperTimeLimit: Expression


    class FrequencyLimitEnum(enum.Enum):
        None = 0
        Value = 1
        Samples = 2
    

class ModelAndLoadPreProcessInverseFft(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessInputFileBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    def RefreshDataSets(self) -> None:
        ...
    def SetQuerySelected(self, quantity: CAE.ModelAndLoadPreProcessInputFileBuilder.Quantity, location: CAE.ModelAndLoadPreProcessInputFileBuilder.Location, sorting: CAE.ModelAndLoadPreProcessInputFileBuilder.Sorting, name: str, selected: bool) -> None:
        ...
    def SetQueryTargetStorageName(self, quantity: CAE.ModelAndLoadPreProcessInputFileBuilder.Quantity, location: CAE.ModelAndLoadPreProcessInputFileBuilder.Location, sorting: CAE.ModelAndLoadPreProcessInputFileBuilder.Sorting, name: str, targetStorageName: str) -> None:
        ...
    def SetSubcaseSelected(self, subcaseName: str, selected: bool) -> None:
        ...
    def SetComponentNameSelected(self, componentName: str, selected: bool) -> None:
        ...
    def SetRpmSelected(self, rpmValue: float, selected: bool) -> None:
        ...
    def SetOrderCutSelected(self, orderCutValue: float, selected: bool) -> None:
        ...
    DatabaseOptions: CAE.DataReaderDatabaseOptions
    FilePath: str
    ManualMpfOffset: int
    MeshDatabaseOptions: CAE.DataReaderDatabaseOptions
    MeshFilePath: str
    MeshSourceType: CAE.ModelAndLoadPreProcessInputFileBuilder.MeshSource
    MpfOffsetStrategyType: CAE.ModelAndLoadPreProcessInputFileBuilder.MpfOffsetStrategy


    class Sorting(enum.Enum):
        Vectors = 0
        Functions = 1
    

    class Quantity(enum.Enum):
        Pressure = 0
        Displacement = 1
        Velocity = 2
        Acceleration = 3
        MassDensity = 4
        SpeedOfSound = 5
        Force = 6
        Temperature = 7
        Rotation = 8
        AngularVelocity = 9
        AngularAcceleration = 10
        Moment = 11
        MPFDisplacement = 12
        MPFVelocity = 13
        MPFAcceleration = 14
        ModeDisplacement = 15
        ModeRotation = 16
    

    class MpfOffsetStrategy(enum.Enum):
        NoOffset = 0
        AutomaticOffset = 1
        ManualOffset = 2
    

    class MeshSource(enum.Enum):
        DataSource = 0
        File = 1
    

    class Location(enum.Enum):
        Node = 0
        Element = 1
        MotionElement = 2
        Mode = 3
    

class ModelAndLoadPreProcessInputFile(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...
    def ProcessMesh(self, loadUnload: bool) -> None:
        ...
    def CreateSelectionRecipes(self, filter: TaggedObject, filterType: CAE.SelRecipeBuilder.InputFilterType, tolerance: float) -> None:
        ...
    DataSource: CAE.ModelAndLoadPreProcessDatabaseSource
    MeshSource: CAE.ModelAndLoadPreProcessDatabaseSource


class ModelAndLoadPreProcessFrequencyOptions(NXObject):
    def __init__(self) -> None: ...
    def GetIndividualFrequencies(self) -> str:
        ...
    def SetIndividualFrequencies(self, individualFrequencies: str) -> None:
        ...
    DefinitionType: CAE.ModelAndLoadPreProcessFrequencyOptions.Frequencyrangedefinitiontype
    EndFrequencyLinear: Expression
    EndFrequencyLogarithmic: Expression
    LowerCenterFrequencyOctave: Expression
    NumLogarithmicIntervals: int
    StartFrequencyLinear: Expression
    StartFrequencyLogarithmic: Expression
    StepValueLinear: Expression
    UpperCenterFrequencyOctave: Expression


    class Frequencyrangedefinitiontype(enum.Enum):
        IndividualFrequencies = 0
        LinearSweep = 1
        LogarithmicSweep = 2
        Octave = 3
        Octave3 = 4
        Octave12 = 5
        UserFrequenciesFromInput = 6
    

class ModelAndLoadPreProcessFanNoiseSegmentationBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...
    FanRotationAxis: CoordinateSystem
    MaxComputationFreq: Expression
    SoundSpeed: Expression


class ModelAndLoadPreProcessFanNoiseSegmentation(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessExportToBinaryBuilder(CAE.ModelAndLoadPreProcessOperationBuilder):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessExportToBinary(CAE.ModelAndLoadPreProcessOperation):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessDatabaseSource(NXObject):
    def __init__(self) -> None: ...


class ModelAndLoadPreProcessBuilder(Builder):
    def __init__(self) -> None: ...
    Memory: float
    MetaSolutionName: str
    NumThreads: int
    RunInForeground: bool
    SolverParameters: CAE.AcousticsAndVibrationSolverParametersComponentAccessor
    SolverPath: str
    TempDir: str
    UseEnvVar: bool
    UseModelDirForSolverTempFiles: bool


class ModelAndLoadPreProcess(NXObject):
    def __init__(self) -> None: ...
    def Validate(self) -> None:
        ...
    def WriteSolverInputFile(self) -> None:
        ...
    def Solve(self) -> None:
        ...
    def Rename(self, name: str) -> None:
        ...
    def CreateLoadRecipeFromResults(self) -> CAE.SimLoadRecipe:
        ...
    def CreateSourceNodesGroup(self) -> CAE.CaeGroup:
        ...
    def CreateTargetNodesGroup(self) -> CAE.CaeGroup:
        ...
    Operations: CAE.ModelAndLoadPreProcessOperations


class ModalDampingIdentificationBuilder(Builder):
    def __init__(self) -> None: ...
    def SetModeset(self, pModeSet: CAE.ModeSet) -> None:
        ...
    def SetRigidbodyThresholdFrequency(self, undampedFrequency: float) -> None:
        ...


class MMCCreateBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMmcs(self) -> typing.List[CAE.MeshMate]:
        ...
    def CommitMmcsAndReturnStatus(self, noSkippedFacePairs: bool) -> typing.List[CAE.MeshMate]:
        ...
    def PrintLogOnInfoWindow(self, fValue: bool) -> None:
        ...
    AutoSelection: SelectDisplayableObjectList
    DistTolerance: Expression
    FaceSearchOption: CAE.MMCCreateBuilder.FaceSearchType
    MeshMatingOption: CAE.MMCCreateBuilder.MeshMatingType
    Mmc: CAE.MeshMate
    ReverseDirection: bool
    SnapTolerance: Expression
    SourceFace: SelectIParameterizedSurface
    TargetFace: SelectIParameterizedSurface
    Type: CAE.MMCCreateBuilder.Types


    class Types(enum.Enum):
        AutoCreate = 0
        Manual = 1
    

    class MeshMatingType(enum.Enum):
        GlueCoincident = 0
        GlueNonCoincident = 1
        FreeCoincident = 2
    

    class FaceSearchType(enum.Enum):
        AllPairs = 0
        IdenticalPairsOnly = 1
    

class MeshSlicingData(TaggedObject):
    def __init__(self) -> None: ...
    def GetSlicingType(self) -> CAE.MeshSlicingData.Type:
        ...


    class Type(enum.Enum):
        Horizontal = 0
        PlanarParallel = 1
        Freeform = 2
    

class MeshSlicerBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateMeshSlicingDataObject(self, slicingType: CAE.MeshSlicingData.Type) -> CAE.MeshSlicingData:
        ...
    def ProcessMeshSlicer(self, meshSlicingDataObj: CAE.MeshSlicingData, meshes: typing.List[CAE.Mesh], nbSlicesPerMesh: int, sliceLayers: int, sliceElements: typing.List[CAE.CaeGroup], sliceTopFaces: typing.List[CAE.CaeGroup], sliceBotFaces: typing.List[CAE.CaeGroup]) -> None:
        ...
    PropertyTable: CAE.PropertyTable


class MeshShellFromSolid(CAE.MeshFollower):
    def __init__(self) -> None: ...


class MeshRefinementBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable
    SelectMesh: SelectTaggedObjectList


class MeshPointProjectBuilder(CAE.MeshPointBaseBuilder):
    def __init__(self) -> None: ...
    Direction: Direction
    Point: Point
    Points: SelectDisplayableObjectList
    PointsList: SelectTaggedObjectList
    ProjectSearchDistanceOption: bool
    ProjectToNearestGeometry: bool
    ProjectionOption: CAE.MeshPointProjectBuilder.ProjectionMethod
    ProjectionTolerance: float
    SearchDistance: Expression
    Target: SelectDisplayableObjectList


    class ProjectionMethod(enum.Enum):
        TypeNearestPoint = 0
        TypeAlongVector = 1
    

class MeshPointOnFaceBuilder(CAE.MeshPointBaseBuilder):
    def __init__(self) -> None: ...
    Face: SelectIParameterizedSurfaceList
    UParameter: Expression
    VParameter: Expression


class MeshPointOnCurveBuilder(CAE.MeshPointBaseBuilder):
    def __init__(self) -> None: ...
    Curve: SelectIBaseCurveList
    TParameter: Expression


class MeshPointMultipleOnCurveBuilder(CAE.MeshPointBaseBuilder):
    def __init__(self) -> None: ...
    CreateOption: bool
    Distance: Expression
    Edge: SelectIBaseCurveList
    NumMeshpoints: int
    PlacementOption: CAE.MeshPointMultipleOnCurveBuilder.PlacementType


    class PlacementType(enum.Enum):
        ByNumber = 0
        ByDistance = 1
    

class MeshPointInsideVolumeBuilder(CAE.MeshPointBaseBuilder):
    def __init__(self) -> None: ...
    Point: Point
    Volume: SelectIBody


class MeshPointExistingPointBuilder(CAE.MeshPointBaseBuilder):
    def __init__(self) -> None: ...
    ExistingPoint: SelectPointList


class MeshPointConicCenterBuilder(CAE.MeshPointBaseBuilder):
    def __init__(self) -> None: ...
    Conic: SelectIBaseCurveList


class MeshPointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.MeshPoint]:
        ...
    def __init__(self, owner: CAE.FemPart) -> None: ...
    def __init__(self) -> None: ...
    def CreateMeshpointOnCurveBuilder(self) -> CAE.MeshPointOnCurveBuilder:
        ...
    def CreateMeshpointMultipleOnCurveBuilder(self) -> CAE.MeshPointMultipleOnCurveBuilder:
        ...
    def CreateMeshpointOnFaceBuilder(self) -> CAE.MeshPointOnFaceBuilder:
        ...
    def CreateMeshpointExistingPointBuilder(self) -> CAE.MeshPointExistingPointBuilder:
        ...
    def CreateMeshpointConicCenterBuilder(self) -> CAE.MeshPointConicCenterBuilder:
        ...
    def CreateMeshpointProjectBuilder(self) -> CAE.MeshPointProjectBuilder:
        ...
    def CreateMeshpointInsideVolumeBuilder(self) -> CAE.MeshPointInsideVolumeBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.MeshPoint:
        ...
    def Tag(self) -> Tag: ...



class MeshPointBaseBuilder(Builder):
    def __init__(self) -> None: ...
    MeshPointToEdit: CAE.MeshPoint
    NodeLabel: int


class MeshPoint(SmartObject):
    def __init__(self) -> None: ...
    def SetCoordinates(self, coordinates: Point3d) -> None:
        ...
    Coordinates: Point3d
    Geometry: NXObject


class MeshMate(CAE.MeshControl):
    def __init__(self) -> None: ...


class MeshManualSweepBetweenListItemSelectionList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAE.MeshManualSweepBetweenListItemSelection]) -> None:
        ...
    def Append(self, object: CAE.MeshManualSweepBetweenListItemSelection) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAE.MeshManualSweepBetweenListItemSelection) -> int:
        ...
    def FindItem(self, index: int) -> CAE.MeshManualSweepBetweenListItemSelection:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAE.MeshManualSweepBetweenListItemSelection) -> None:
        ...
    def Erase(self, obj: CAE.MeshManualSweepBetweenListItemSelection, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAE.MeshManualSweepBetweenListItemSelection]:
        ...
    def SetContents(self, objects: typing.List[CAE.MeshManualSweepBetweenListItemSelection]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAE.MeshManualSweepBetweenListItemSelection, object2: CAE.MeshManualSweepBetweenListItemSelection) -> None:
        ...
    def Insert(self, location: int, object: CAE.MeshManualSweepBetweenListItemSelection) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class MeshManualSweepBetweenListItemSelection(NXObject):
    def __init__(self) -> None: ...
    FlipDirection: bool
    MasterEdge: CAE.SelectCAEEdge
    TargetEdge: CAE.SelectCAEEdge


class MeshManual(CAE.Mesh):
    def __init__(self) -> None: ...
    ReflectSourceMesh: CAE.Mesh


class MeshManagerOccurrence(CAE.IMeshManager):
    def __init__(self) -> None: ...
    def CreateOccurrenceBuilder(self, meshCollector: CAE.MeshCollectorOccurrence) -> CAE.MeshCollectorOccurrenceBuilder:
        ...


class MeshManager(CAE.IMeshManager):
    def __init__(self) -> None: ...
    def CreateMappedMeshBuilder(self, mappedMesh: CAE.MappedMesh) -> CAE.MappedMeshBuilder:
        ...
    def CreateDependentMeshBuilder(self, dependentMesh: CAE.DependentMesh) -> CAE.DependentMeshBuilder:
        ...
    def CreateMesh0dBuilder(self, mesh: CAE.Mesh0d) -> CAE.Mesh0dBuilder:
        ...
    def CreateMesh1dBuilder(self, mesh: CAE.Mesh1d) -> CAE.Mesh1dBuilder:
        ...
    def CreateMesh2dBuilder(self, mesh: CAE.Mesh2d) -> CAE.Mesh2dBuilder:
        ...
    def CreateShipMeshAutomationBuilder(self, mesh: CAE.ShipMeshAutomation) -> CAE.ShipMeshAutomationBuilder:
        ...
    def CreateMesh3dTetBuilder(self, mesh: CAE.Mesh3d) -> CAE.Mesh3dTetBuilder:
        ...
    def CreateMesh3dHexBuilder(self, mesh: CAE.SweptMesh) -> CAE.Mesh3dHexBuilder:
        ...
    def CreateMesh3dHybridBuilder(self, mesh: CAE.Mesh) -> CAE.Mesh3dHybridBuilder:
        ...
    def CreateImmersedBoundaryMeshBuilder(self, mesh: CAE.Mesh) -> CAE.ImmersedBoundaryMeshBuilder:
        ...
    def CreateShell2solidBuilder(self, mesh: CAE.Mesh3d) -> CAE.Shell2SolidBuilder:
        ...
    def CreateShellto3dhybridBuilder(self, mesh: CAE.Mesh3d) -> CAE.ShellTo3dHybridBuilder:
        ...
    def CreateSurfaceCoatBuilder(self, mesh: CAE.MeshShellFromSolid) -> CAE.SurfaceCoatBuilder:
        ...
    def CreateLocalRemeshBuilder(self) -> CAE.LocalRemeshBuilder:
        ...
    def CreatePrimitiveMeshBuilder(self, mesh: CAE.Mesh) -> CAE.PrimitiveMeshBuilder:
        ...
    def CreatePrimitiveMeshBuilder(self, meshType: str) -> CAE.PrimitiveMeshBuilder:
        ...
    def CreateCollectorBuilder(self, meshCollector: CAE.MeshCollector, pElementCollectorContainerName: str) -> CAE.MeshCollectorBuilder:
        ...
    def CreateReassignElementsBuilder(self) -> CAE.ReassignElementsBuilder:
        ...
    def SetMeshCollectorName(self, meshCollector: CAE.MeshCollector, collectorName: str) -> None:
        ...
    def DragNDropMesh(self, mesh: CAE.Mesh, sourceMeshCollector: CAE.MeshCollector, targetMeshCollector: CAE.MeshCollector) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.MeshManager.MoveMeshToNewCollector instead.")"""
        ...
    def MoveMeshToNewCollector(self, mesh: CAE.Mesh, keepMeshDisplaySettings: bool, sourceMeshCollector: CAE.MeshCollector, targetMeshCollector: CAE.MeshCollector) -> None:
        ...
    def CreateProjectNodesToCadGeometryBuilder(self) -> CAE.ProjectNodesToCadGeometryBuilder:
        ...
    def MergeMeshes(self, selectedMeshes: typing.List[CAE.Mesh]) -> CAE.Mesh:
        ...
    def CreateWeldBuilder(self, mesh: CAE.Mesh) -> CAE.WeldBuilder:
        ...
    def CreateContactMeshBuilder(self, contactMesh: CAE.Mesh1d) -> CAE.ContactMeshBuilder:
        ...
    def CreateMeshRefinementBuilder(self) -> CAE.MeshRefinementBuilder:
        ...
    def CreatePrimitiveRecipeMeshBuilder(self, mesh: CAE.PrimitiveRecipeMesh) -> CAE.PrimitiveRecipeMeshBuilder:
        ...
    def CreatePrimitiveRecipeMeshBuilder(self, primitiveType: CAE.PrimitiveRecipeMeshBuilder.Type) -> CAE.PrimitiveRecipeMeshBuilder:
        ...
    def CreateMesh2dFromFacetsBuilder(self, mesh: CAE.Mesh2dFromFacets) -> CAE.Mesh2dFromFacetsBuilder:
        ...
    def MeshCollectorClone(self, sourceColl: CAE.IMeshCollector) -> CAE.MeshCollector:
        ...
    def GetAutoElementSize(self, bodies: typing.List[CAE.CAEBody]) -> float:
        ...
    def GetAutoElementSize(self, faces: typing.List[CAE.CAEFace]) -> float:
        ...
    def GetAutoElementSize(self, faces: typing.List[Body]) -> float:
        ...
    def GetAutoElementSize(self, faces: typing.List[Face]) -> float:
        ...
    def CreatePreparedMesh1dBuilder(self, mesh: CAE.PreparedMesh1d) -> CAE.PreparedMesh1dBuilder:
        ...
    def CreateAcousticMeshAutomationBuilder(self, mesh: CAE.RecipeAcousticMeshAutomation) -> CAE.AcousticMeshAutomationBuilder:
        ...


class MeshingPreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    AppType: CAE.MeshingPreferencesBuilder.AppTypeName
    MaxNumElem: int
    MaxNumElemOptn: bool
    MeshUpdateOrderType: CAE.MeshingPreferencesBuilder.MeshUpdateOrder
    MinNumElem: int
    MinNumElemOptn: bool
    ProjectNodesToCADOptn: bool
    ProjectNodesToCADTol: float
    TinyEdgeColor: NXColor
    TinyEdgeTol: float


    class MeshUpdateOrder(enum.Enum):
        TimeStamp = 0
        ElementSize = 1
    

    class AppTypeName(enum.Enum):
        General = 0
        CrashAnalysis = 1
    

class MeshFromPointCloudBuilder(Builder):
    def __init__(self) -> None: ...
    BeamMeshToggle: bool
    FeatureAngle: Expression
    MaxDistance: Expression
    MeshName: str
    Points: SelectTaggedObjectList
    ShellElementType: CAE.ElementTypeBuilder
    WireframeElementType: CAE.ElementTypeBuilder


class MeshFromBoundaryBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSourceElementEdgePathMethod(self, sourceElementEdgePathMethod: CAE.ElemEdgePathMethod) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  There is no replacement for this function.")"""
        ...
    def SetTargetElementEdgePathMethod(self, targetElementEdgePathMethod: CAE.ElemEdgePathMethod) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  There is no replacement for this function.")"""
        ...
    ClosedLoopMethodType: CAE.MeshFromBoundaryBuilder.ClosedLoopMethod
    ClosedLoopSelection: SelectTaggedObjectList
    ClosedLoopSelectionMesh: SelectTaggedObjectList
    CollectorName: str
    ElementType: CAE.ElementTypeBuilder
    Layers: int
    LoopType: CAE.MeshFromBoundaryBuilder.LoopOption
    NumElementsOnRail1: int
    NumElementsOnRail2: int
    Rail1Selection: SelectTaggedObjectList
    Rail2Selection: SelectTaggedObjectList
    RailType: CAE.MeshFromBoundaryBuilder.RailOption
    SourceSelection: SelectTaggedObjectList
    TargetSelection: SelectTaggedObjectList
    Type: CAE.MeshFromBoundaryBuilder.LoopOption


    class RailOption(enum.Enum):
        Uniform = 0
        Transition = 1
        Automatic = 2
    

    class LoopOption(enum.Enum):
        SourceTarget = 0
        ClosedLoop = 1
    

    class ClosedLoopMethod(enum.Enum):
        Edge = 0
        Group = 1
        Mesh = 2
    

class MeshFollower(CAE.Mesh):
    def __init__(self) -> None: ...


class MeshDisplaySettings3d(CAE.MeshDisplaySettings):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DisplayInternalEdges: bool
    DisplayShadedEdges: bool
    ElementShrinkPercent: int
    LineWidth: DisplayableObject.ObjectWidth
    ShadedEdgeColor: NXColor


class MeshDisplaySettings2d(CAE.MeshDisplaySettings):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    BoltHoleCenterlineColor: NXColor
    DisplayBoltHoleCenterline: bool
    DisplayShadedEdges: bool
    DisplayThickShell: bool
    ElementNormals: CAE.ElementNormalsType
    ElementShrinkPercent: int
    LineWidth: DisplayableObject.ObjectWidth
    NormalsColor: NXColor
    ShadedEdgeColor: NXColor


class MeshDisplaySettings1d(CAE.MeshDisplaySettings):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DisplaySection: CAE.DisplaySectionType
    DisplaySectionEndRelease: bool
    DisplaySectionOrientation: bool
    DisplaySectionOrientationVector: bool
    DisplayText: bool
    ElementShrinkPercent: int
    LineWidth: DisplayableObject.ObjectWidth


class MeshDisplaySettings0d(CAE.MeshDisplaySettings):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DisplayText: bool
    ElementMarker: CAE.MarkerType0d


class MeshDisplaySettings(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def UseMeshCollectorDisplaySettings(self) -> None:
        ...
    def UseCustomerDefaultsDisplaySettings(self) -> None:
        ...
    Color: NXColor


class MeshControlDisplayOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryLayerSize: int
    BoundingVolumeDensitySize: int
    CrackFaceConditionSize: int
    CylinderDensitySize: int
    DependentEdgeDensitySize: int
    EdgeDensitySize: int
    EdgeSeparationConditionSize: int
    FaceDensitySize: int
    FilletDensitySize: int
    MappedHoleSize: int
    MeshMateSize: int
    PointDensitySize: int
    ShadeSymbols: bool
    ShowThroughDisplay: bool
    TextDisplay: bool
    WeldRowSize: int


class MeshControlDisplayManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def CreateBuilder(self) -> CAE.MeshControlDisplayOptionsBuilder:
        ...
    def Tag(self) -> Tag: ...



class MeshControlCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.MeshControl]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.MeshControl:
        ...
    def CreateBuilder(self, meshControl: CAE.MeshControl) -> CAE.MeshControlBuilder:
        ...
    def CreateMmcCreateBuilder(self, mmcCreate: CAE.MeshMate) -> CAE.MMCCreateBuilder:
        ...
    def CreateCrackFaceConditionBuilder(self) -> CAE.CrackFaceConditionBuilder:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.MeshControlCollection.CreateCrackFaceBuilder and pass in a null reference (Nothing in Visual Basic) for mesh control parameter")"""
        ...
    def CreateCrackFaceBuilder(self, meshControl: CAE.MeshControl) -> CAE.CrackFaceConditionBuilder:
        ...
    def Tag(self) -> Tag: ...



class MeshControlBuilder(Builder):
    def __init__(self) -> None: ...
    def AutoSize(self) -> None:
        ...
    def LoadMeshControlData(self, tMeshControl: CAE.MeshControl) -> None:
        ...
    def AddWeldFaceDefinition(self) -> int:
        ...
    def DeleteWeldFaceDefinitions(self, piFaceDefinitions: int) -> None:
        ...
    def AutoCreateWeldFaceDefinitions(self) -> int:
        ...
    def GetWeldFaceDefinitions(self) -> int:
        ...
    def SetWeldFaceDefinition(self, iFaceDefinition: int) -> None:
        ...
    def ResolveConflicts(self, fDoNotOverwriteExisting: bool) -> None:
        ...
    def CommitDensities(self) -> typing.List[CAE.MeshControl]:
        ...
    def SetCurrentPointLayerThicknessDefinition(self, iLayerId: int) -> None:
        ...
    AspectRatio: Expression
    BlBodySelection: SelectNXObjectList
    BlBodySelectionToggle: bool
    BlDimension: int
    BlTargetSelection: SelectNXObjectList
    BoundingVolumeApplyToSurfacesOnly: bool
    BoundingVolumeBodySelection: SelectNXObjectList
    BoundingVolumeDensityElementSize: Expression
    ChordalTolerance: Expression
    CylinderAxialElementSize: Expression
    CylinderAxialElementSizeOption: CAE.MeshControlBuilder.CylinderAxialElementSizeType
    CylinderAxialNumElements: int
    CylinderAxialNumElementsExp: Expression
    CylinderCircularNumElements: int
    CylinderCircularNumElementsExp: Expression
    CylinderCircularNumPerQuarter: int
    CylinderCircularNumPerQuarterExp: Expression
    CylinderCircularSizeOption: CAE.MeshControlBuilder.CylinderCircularSizeType
    CylinderFreezeGeometryOption: bool
    CylinderMaxAngle: Expression
    CylinderMaxRadius: Expression
    CylinderMinAngle: Expression
    CylinderMinRadius: Expression
    DistributeOnChainOption: bool
    EdgeFraction: Expression
    EndSize: Expression
    FilletAxialElementSizeOption: CAE.MeshControlBuilder.FilletAxialElementSizeType
    FilletCircumMinElementSize: Expression
    FilletCircumNumberElements: int
    FilletCircumNumberElementsExp: Expression
    FilletCircumSizeOption: CAE.MeshControlBuilder.FilletCircumferenceSizeType
    FilletCircumTargetElemSize: Expression
    FilletElementSize: Expression
    FilletMaxAngle: Expression
    FilletMaxRadius: Expression
    FilletMethod: CAE.MeshControlBuilder.FilletType
    FilletMinAngle: Expression
    FilletMinRadius: Expression
    FirstLayerThickness: Expression
    GeometricRatio: Expression
    GrowthRate: float
    HeightDefinedBy: CAE.MeshControlBuilder.HeightDefinedByOption
    HoleAllowNonCircularHolesToggle: bool
    HoleFreeEdgesToggle: bool
    HoleMaxRadius: Expression
    HoleMinRadius: Expression
    MainType: CAE.MeshControlBuilder.Types
    MappedAdjustDepth: bool
    MappedApplyShapeImprints: bool
    MappedNumberOfLayers: int
    MappedNumberOfLayersExp: Expression
    MappedOffset: Expression
    MinimumElementSize: Expression
    MinimumElementSizeOption: bool
    NumOfElements: int
    NumOfElementsExp: Expression
    NumberOfLayers: int
    NumberOfLayersExp: Expression
    OverallSize: Expression
    PointElementSize: Expression
    PointIndividualLayerThickness: Expression
    PointLayerThicknessOption: bool
    PointNumberOfElements: Expression
    PointNumberOfLayers: Expression
    PointRadiusOfInfluence: Expression
    PointSpotWeldStatus: bool
    ProgressionSubtype: CAE.MeshControlBuilder.ProgressionTypes
    SelectWeldFace: SelectNXObjectList
    Selection: SelectNXObjectList
    SelectionFilterToggle: bool
    SizeSubtype: CAE.MeshControlBuilder.SizeTypes
    SizingOption: CAE.MeshControlBuilder.SizingType
    SpacingElementSize: Expression
    SpacingNumberOfElements: int
    SpacingNumberOfElementsExp: Expression
    StartSize: Expression
    TotalThickness: Expression
    WeldDirection: CAE.MeshControlBuilder.WeldSide
    WeldDirectionScarEdge: NXObject
    WeldNumberOfLayers: int
    WeldNumberOfLayersExp: Expression
    WeldOffset: Expression


    class WeldSide(enum.Enum):
        Both = 0
        Side1 = 1
        Side2 = 2
    

    class Types(enum.Enum):
        EdgeDensityNumber = 0
        EdgeDensitySize = 1
        EdgeDensityChordal = 2
        EdgeDensityProgression = 3
        FaceDensitySize = 4
        WeldRow = 5
        MappedHoles = 6
        FilletDensity = 7
        CylinderDensity = 8
        BoundaryLayers = 9
        PointDensity = 10
        BoundingVolumeDensity = 11
        TypesLastValue = 12
    

    class SizingType(enum.Enum):
        None = 0
        ByNumber = 1
        BySize = 2
    

    class SizeTypes(enum.Enum):
        All = 0
        Start = 1
        End = 2
        StartAndEnd = 3
        LastValue = 4
    

    class ProgressionTypes(enum.Enum):
        Start = 0
        End = 1
        Center = 2
        LastValue = 3
    

    class HeightDefinedByOption(enum.Enum):
        TotalThickness = 0
        GrowthRate = 1
    

    class FilletType(enum.Enum):
        AllTypes = 0
        InsideRadius = 1
        OutsideRadius = 2
    

    class FilletCircumferenceSizeType(enum.Enum):
        None = 0
        Angle = 1
        Size = 2
    

    class FilletAxialElementSizeType(enum.Enum):
        None = 0
        Size = 1
    

    class CylinderCircularSizeType(enum.Enum):
        None = 0
        ByAngle = 1
        Number = 2
    

    class CylinderAxialElementSizeType(enum.Enum):
        None = 0
        Number = 1
        Size = 2
    

    class BLType(enum.Enum):
        Face = 0
        Edge = 1
    

class MeshControl(DisplayableObject):
    def __init__(self) -> None: ...


class MeshCollectorOccurrenceBuilder(Builder):
    def __init__(self) -> None: ...
    def SetOverrideProperty(self, overrideProperty: str, updateThisOverride: bool) -> None:
        ...
    PropertyTable: CAE.PropertyTable


class MeshCollectorOccurrence(CAE.IMeshCollector):
    def __init__(self) -> None: ...


class MeshCollectorDisplayDefaults3d(CAE.MeshCollectorDisplayDefaults):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DisplayInternalEdges: bool
    DisplayShadedEdges: bool
    ElementShrinkPercent: int
    LineWidth: DisplayableObject.ObjectWidth
    ShadedEdgeColor: NXColor


class MeshCollectorDisplayDefaults2d(CAE.MeshCollectorDisplayDefaults):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    BoltHoleCenterlineColor: NXColor
    DisplayBoltHoleCenterline: bool
    DisplayShadedEdges: bool
    DisplayThickShell: bool
    ElementNormals: CAE.ElementNormalsType
    ElementShrinkPercent: int
    LineWidth: DisplayableObject.ObjectWidth
    NormalsColor: NXColor
    ShadedEdgeColor: NXColor


class MeshCollectorDisplayDefaults1d(CAE.MeshCollectorDisplayDefaults):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DisplaySection: CAE.DisplaySectionType
    DisplaySectionEndRelease: bool
    DisplaySectionOrientation: bool
    DisplaySectionOrientationVector: bool
    DisplayText: bool
    ElementShrinkPercent: int
    LineWidth: DisplayableObject.ObjectWidth


class MeshCollectorDisplayDefaults0d(CAE.MeshCollectorDisplayDefaults):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DisplayText: bool
    ElementMarker: CAE.MarkerType0d


class MeshCollectorDisplayDefaults(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def UseCustomerDefaultsDisplaySettings(self) -> None:
        ...
    Color: NXColor


class MeshCollectorBuilder(Builder):
    def __init__(self) -> None: ...
    CollectorName: str
    PropertyTable: CAE.PropertyTable


    class ElementDimensionOption(enum.Enum):
        Point = 0
        Beam = 1
        Shell = 2
        Solid = 3
        ContactEdge = 4
        ContactFace = 5
    

class MeshCollector(CAE.IMeshCollector):
    def __init__(self) -> None: ...


class Mesh3dTetBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    def CommitWithPartialMesh(self) -> typing.List[CAE.Mesh]:
        ...
    AutoResetOption: bool
    AutoSizeOption: bool
    CheckElementSizeOption: bool
    ElementType: CAE.ElementTypeBuilder
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionFillet: CAE.SelectCAEFaceList
    SelectionList: SelectDisplayableObjectList


class Mesh3dHybridBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    def CommitWithPartialMesh(self) -> typing.List[CAE.Mesh]:
        ...
    AutoResetOption: bool
    ElementType: CAE.ElementTypeBuilder
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList


class Mesh3dHexBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateNewListItem(self, tMasterEdge: CAE.CAEEdge, tTargetEdge: CAE.CAEEdge, fFlipDirection: bool) -> CAE.MeshManualSweepBetweenListItemSelection:
        ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    CreationType: CAE.Mesh3dHexBuilder.Type
    ElementType: CAE.ElementTypeBuilder
    LoopList: CAE.MeshManualSweepBetweenListItemSelectionList
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList
    SourceFace: SelectDisplayableObject
    SourceFaceList: SelectDisplayableObjectList
    TargetFace: SelectDisplayableObject
    TargetFaceList: SelectDisplayableObjectList
    WallFaceList: SelectDisplayableObjectList


    class Type(enum.Enum):
        AutomaticMultipleBody = 0
        Automatic = 1
        Manual = 2
        BetweenAutomatic = 3
        BetweenManual = 4
    

class Mesh3d(CAE.Mesh):
    def __init__(self) -> None: ...


class Mesh2dFromFacetsBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    ElementType: CAE.ElementTypeBuilder
    ExportMesh: bool
    MeshName: str
    MeshingMethod: CAE.Mesh2dFromFacetsBuilder.MeshingMethodType
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList


    class MeshingMethodType(enum.Enum):
        Create = 0
        Extract = 1
    

class Mesh2dFromFacets(CAE.Mesh):
    def __init__(self) -> None: ...


class Mesh2dFree(CAE.Mesh2d):
    def __init__(self) -> None: ...


class Mesh2dBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    AutoResetOption: bool
    ElementType: CAE.ElementTypeBuilder
    ExportMesh: bool
    GeometryUsageType: CAE.Mesh2dBuilder.GeometryType
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList


    class GeometryType(enum.Enum):
        Main = 0
        Fillet = 1
        Cylinder = 2
    

class Mesh2d(CAE.Mesh):
    def __init__(self) -> None: ...


class Mesh1dBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    AutoChainOption: bool
    ElementType: CAE.ElementTypeBuilder
    FlipDirectionOption: bool
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList


class Mesh1d(CAE.Mesh):
    def __init__(self) -> None: ...


class Mesh0dBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    CombineBody: bool
    Csys: CoordinateSystem
    CsysOption: int
    ElementType: CAE.ElementTypeBuilder
    ExpressionMass: Expression
    LmEntitySelList: SelectDisplayableObjectList
    LmPointSelection: SelectDisplayableObjectList
    MeshCreateOption: CAE.Mesh0dBuilder.MeshCreationType
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList
    TotalMass: bool
    XOffset: Expression
    YOffset: Expression
    ZOffset: Expression


    class MeshCreationType(enum.Enum):
        Mesh0d = 0
        LumpedMass = 1
    

class Mesh0d(CAE.Mesh):
    def __init__(self) -> None: ...


class Mesh(DisplayableObject):
    def __init__(self) -> None: ...
    def GetMeshDisplaySettings(self) -> CAE.MeshDisplaySettings:
        ...
    def IsValid(self) -> bool:
        ...
    def GetUpdatePendingStatus(self) -> bool:
        ...
    def GetLatticeBody(self) -> Body:
        ...
    def GetPrintMeshWithTolerance(self) -> bool:
        ...
    def SetPrintMeshWithTolerance(self, printTolerance: bool) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    ElementPropertyTable: CAE.PropertyTable
    ExportMeshProperty: bool
    LockStatus: bool
    MeshCollector: CAE.IMeshCollector


class MergeFaceBuilder(Builder):
    def __init__(self) -> None: ...
    AutoRemoveToggle: bool
    EdgeAngle: Expression
    SelectEdgeFaceBodyBlock: SelectDisplayableObjectList
    VertexAngle: Expression


class MechanicalLoadSumBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSolution(self) -> CAE.SimSolution:
        ...
    def SetSolution(self, solution: CAE.SimSolution) -> None:
        ...
    def GetSubcase(self) -> CAE.SimSolutionStep:
        ...
    def SetSubcase(self, subcase: CAE.SimSolutionStep) -> None:
        ...
    def GetLoads(self) -> typing.List[CAE.SimLoad]:
        ...
    def SetLoads(self, loads: typing.List[CAE.SimLoad]) -> None:
        ...
    EvaluationFrequency: Expression
    EvaluationTime: Expression
    ReferenceCsys: CoordinateSystem
    UserSpecifiedUnit: CAE.MechanicalLoadSumBuilder.UserUnit


    class UserUnit(enum.Enum):
        DeckUnit = 0
        MilliNewton = 1
        MilliMillinewton = 2
        MeterNewton = 3
        FtPoundForce = 4
        InPoundForce = 5
    

class MaterialOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Material: PhysicalMaterial
    MaterialInherited: bool


class MarkerType0d(enum.Enum):
    None = 0
    Plus = 1
    Dot = 2
    Asterisk = 3
    Circle = 4
    Poundsign = 5
    Cross = 6
    Square = 7
    Triangle = 8
    Diamond = 9
    CenterLine = 10
    FilledCircle = 11
    FilledSquare = 12
    FilledSquareWithOneRing = 13
    FilledSquareWithTwoRings = 14
    TriangleInTriangle = 15
    FilledDiamond = 16
    CircleInCircle = 17
    CircleInSquare = 18
    LargeFilledSquare = 19
    SquareInSquare = 20
    ThickCircle = 21
    LargeBox = 22


class MappedResult(CAE.Result):
    def __init__(self) -> None: ...
    def GetFiletype(self) -> CAE.Result.Filetype:
        ...
    def GetFilename(self) -> str:
        ...


class MappedMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCornerData(self, face: NXObject) -> typing.List[NXObject]:
        ...
    def SetCornerData(self, face: NXObject, vertexList: typing.List[NXObject]) -> None:
        ...
    def SetCornerDataWithEdges(self, face: NXObject, start: int, edge: typing.List[NXObject]) -> None:
        ...
    def ChangeEdgeDensity(self, edge: NXObject, numberElements: int) -> None:
        ...
    def AutoSize(self) -> float:
        ...
    def PreviewMesh(self) -> None:
        ...
    def ChangeEdgeDensityObject(self, pEdgeTags: typing.List[NXObject], numberElements: int) -> None:
        ...
    AllTriBoundaryLayer: bool
    AttemptMultiblockDecompositionOption: bool
    ControlSlender: bool
    EccAuto: bool
    EccName: str
    EdgeMatchOption: bool
    EdgeMatchTolerance: float
    EdgeMergeAngle: float
    ElementSize: float
    ElementSizeExpression: Expression
    ElementType: str
    FlipDiagonals: bool
    FormatMesh: bool
    GradationRate: float
    InsertBlendElement: bool
    Jacobian: float
    KeepFreeMeshes: bool
    MergeEdges: bool
    MidNodeOption: CAE.MappedMeshBuilder.MidNodeType
    MinAspectRatio: float
    ProjectVertices: bool
    QuadOnlyMesh: bool
    SelectionFace: SelectDisplayableObjectList
    SmoothingDistanceFactor: float
    SweepAngle: float


    class MidNodeType(enum.Enum):
        Mixed = 0
        Curved = 1
        Straight = 2
    

class MappedMesh(CAE.Mesh2d):
    def __init__(self) -> None: ...


class MappedHole(CAE.MeshControl):
    def __init__(self) -> None: ...


class ManualSweepBetweenSelection(Builder):
    def __init__(self) -> None: ...
    def CreateNewListItem(self, tMasterEdge: CAE.CAEEdge, tTargetEdge: CAE.CAEEdge, fFlipDirection: bool) -> CAE.ManualSweepBetweenListItemSelection:
        """[Obsolete("Deprecated in NX10.0.0.  Use CAE.Mesh3dHexBuilder.")"""
        ...
    LoopList: CAE.ManualSweepBetweenListItemSelectionList
    MasterFace: CAE.SelectCAEFace
    TargetFace: CAE.SelectCAEFace
    WallFaceSelection: CAE.SelectCAEFaceList


class ManualSweepBetweenListItemSelectionList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAE.ManualSweepBetweenListItemSelection]) -> None:
        ...
    def Append(self, object: CAE.ManualSweepBetweenListItemSelection) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAE.ManualSweepBetweenListItemSelection) -> int:
        ...
    def FindItem(self, index: int) -> CAE.ManualSweepBetweenListItemSelection:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAE.ManualSweepBetweenListItemSelection) -> None:
        ...
    def Erase(self, obj: CAE.ManualSweepBetweenListItemSelection, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAE.ManualSweepBetweenListItemSelection]:
        ...
    def SetContents(self, objects: typing.List[CAE.ManualSweepBetweenListItemSelection]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAE.ManualSweepBetweenListItemSelection, object2: CAE.ManualSweepBetweenListItemSelection) -> None:
        ...
    def Insert(self, location: int, object: CAE.ManualSweepBetweenListItemSelection) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ManualSweepBetweenListItemSelection(NXObject):
    def __init__(self) -> None: ...
    FlipDirection: bool
    MasterEdge: CAE.SelectCAEEdge
    TargetEdge: CAE.SelectCAEEdge


class ManualNodeAssociationBuilder(Builder):
    def __init__(self) -> None: ...
    ChildrenGeomAssociation: bool
    GeomSelection: SelectTaggedObjectList
    NodeSelection: CAE.SelectFENodeList


class ManualMorphBuilder(Builder):
    def __init__(self) -> None: ...
    def GetManualMapList(self) -> typing.List[TaggedObject]:
        ...
    def SetMapData(self, mapTag: TaggedObject) -> None:
        ...
    def RemoveMapData(self, mapTag: TaggedObject) -> None:
        ...
    def EmptyMapList(self) -> None:
        ...
    def CreateMapData(self) -> TaggedObject:
        ...
    def SetMapName(self, mapDataTag: TaggedObject, mapName: str) -> None:
        ...
    def GetMapByName(self, pMapTags: typing.List[TaggedObject], mapName: str) -> TaggedObject:
        ...
    def SetMapType(self, mapDataTag: TaggedObject, mapType: CAE.ManualMorphBuilder.MapType) -> None:
        ...
    def SetMapMethod(self, mapDataTag: TaggedObject, mapMethod: CAE.ManualMorphBuilder.MapMethod) -> None:
        ...
    def SetNodeSelection(self, mapDataTag: TaggedObject, pNodeTags: typing.List[CAE.FENode]) -> None:
        ...
    def SetGeometrySelection(self, mapDataTag: TaggedObject, pGeomTags: typing.List[TaggedObject]) -> None:
        ...
    def SetMapDirection(self, mapDataTag: TaggedObject, direction: float) -> None:
        ...
    def SetMapDirectionPoint(self, mapDataTag: TaggedObject, pointCoords: float) -> None:
        ...
    def SetMapDirectionMethod(self, mapDataTag: TaggedObject, vecMethod: int) -> None:
        ...
    def SetVertexNode(self, mapDataTag: TaggedObject, isVertexNode: bool) -> None:
        ...
    def SetNodeToVertexMap(self, mapDataTag: TaggedObject, pVertexNodeTags: typing.List[CAE.FENode]) -> None:
        ...
    def SetNodeToCurveEndPointMap(self, mapDataTag: TaggedObject, pVertexNodeTags: typing.List[CAE.FENode]) -> None:
        ...
    def ClearNodesOfMap(self, mapDataTag: TaggedObject) -> None:
        ...
    def ClearGeometryOfMap(self, mapDataTag: TaggedObject) -> None:
        ...
    def CheckNodesForContinuity(self, pNodeTags: typing.List[CAE.FENode], pVertexNodeTags: typing.List[CAE.FENode]) -> None:
        ...
    def CheckNodeToPointMapForPlanarAnalysis(self, pointTag: TaggedObject, nodeTag: TaggedObject) -> bool:
        ...
    def CheckNodeToFaceMapForPlanarAnalysis(self, faceTag: TaggedObject, pNodeTags: typing.List[CAE.FENode]) -> bool:
        ...
    def CheckNodeToEdgeMapForPlanarAnalysis(self, pEdgeTags: typing.List[TaggedObject], pNodeTags: typing.List[CAE.FENode]) -> bool:
        ...
    ElementSelection: CAE.SelectElementsBuilder
    MapSequence: bool


    class MapType(enum.Enum):
        Stationary = 0
        NodeToPoint = 1
        NodeToEdge = 2
        NodeToFace = 3
    

    class MapMethod(enum.Enum):
        NearestPoint = 0
        AlongVector = 1
        UniformAcrossEdge = 2
        KeepSourceBias = 3
        BasedOnEdgeNodeMovement = 4
        AlongElementNormal = 5
    

class LumpedMassEADBuilder(Builder):
    def __init__(self) -> None: ...
    Elements: CAE.SelectElementsBuilder
    ExpressionMass: Expression
    MassState: CAE.LumpedMassEADBuilder.State


    class State(enum.Enum):
        Apply = 0
        Clear = 1
    

class LocalRemeshBuilder(Builder):
    def __init__(self) -> None: ...
    ControlOption: CAE.LocalRemeshBuilder.MeshControlOption
    ElementList: CAE.SelectElementsBuilder
    FactorValue: Expression
    LayerThickness: Expression
    LayerThicknessOption: bool
    NumberOfElements: Expression
    NumberOfElementsOption: bool
    NumberOfLayers: Expression
    NumberOfLayersOption: bool
    SelectionElementEdges: SelectTaggedObjectList
    SizeOption: CAE.LocalRemeshBuilder.Option
    SizeValue: Expression
    Transition: int


    class Option(enum.Enum):
        Factor = 0
        Size = 1
    

    class MeshControlOption(enum.Enum):
        MappedHole = 0
        None = 1
    

class LoadMappingBuilder(Builder):
    def __init__(self) -> None: ...
    def SetForces(self, forces: typing.List[CAE.SimLoad]) -> None:
        ...
    def SetFolder(self, folder: Fields.FieldFolder) -> None:
        ...


class LoadcaseCombinationBuilder(Builder):
    def __init__(self) -> None: ...
    def AddCombinedLoadcase(self, name: str) -> None:
        ...
    def RenameCombinedLoadcase(self, oldName: str, newName: str) -> None:
        ...
    def DeleteCombinedLoadcase(self, name: str) -> None:
        ...
    def AddComponent(self, name: str, loadcaseName: str, mult: float) -> None:
        ...
    def EditComponentScaleFactor(self, name: str, loadcaseName: str, mult: float) -> None:
        ...
    def EditComponent(self, name: str, oldLoadcaseName: str, newLoadcaseName: str) -> None:
        ...
    def RemoveComponent(self, name: str, loadcaseName: str) -> None:
        ...
    def ExportToCSV(self, fileName: str) -> None:
        ...
    def ImportFromCSV(self, fileName: str) -> None:
        ...


class Loadcase(CAE.BaseLoadcase):
    def __init__(self) -> None: ...
    Label: int


class LbcAssociationMgr(Builder):
    def __init__(self) -> None: ...
    def ExportToCsv(self, csvFileName: str) -> None:
        ...
    def ImportFromCsv(self, csvFileName: str) -> None:
        ...
    Orientation: bool
    TypeOption: CAE.LbcAssociationMgr.BcType


    class BcType(enum.Enum):
        Load = 0
        Constraint = 1
        SimulationObject = 2
        None = 3
    

class LayoutStatePreferences(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def DisposeRetainingPreferencesPropertyTable(self) -> None:
        ...
    def DisposeRestoringPreferencesPropertyTable(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    RestoringPreferencesPropertyTable: BasePropertyTable
    RetainingPreferencesPropertyTable: BasePropertyTable
    WorkRestoringPreferencesPropertyTable: BasePropertyTable
    WorkRetainingPreferencesPropertyTable: BasePropertyTable


class LayoutStateDataReferenceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LayoutStateDataReference]:
        ...
    def __init__(self, owner: CAE.LayoutStateApplicator) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, referenceName: str) -> CAE.LayoutStateDataReference:
        ...
    def Tag(self) -> Tag: ...



class LayoutStateDataReference(TaggedObject):
    def __init__(self) -> None: ...
    def OverrideContent(self, referenceString: str) -> None:
        ...
    def OverrideContentWithVersion(self, version: int, referenceString: str) -> None:
        ...


class LayoutStateCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LayoutState]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.LayoutState:
        ...
    def CreateLayoutStateBuilder(self, layoutState: CAE.LayoutState) -> CAE.LayoutStateBuilder:
        ...
    def DeleteLayoutState(self, layoutState: CAE.LayoutState) -> None:
        ...
    def CloneLayoutState(self, fromLayoutState: CAE.LayoutState, newName: str) -> CAE.LayoutState:
        ...
    def CreateEmptyLayoutState(self, layoutStateName: str) -> CAE.LayoutState:
        ...
    def CreateLayoutStateApplicator(self) -> CAE.LayoutStateApplicator:
        ...
    def CopyLayoutStateToArchived(self, fromLayoutState: CAE.LayoutState, newName: str) -> CAE.LayoutState:
        ...
    def Tag(self) -> Tag: ...



class LayoutStateBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitLayoutState(self) -> CAE.LayoutState:
        ...
    def SetName(self, name: str) -> None:
        ...
    def SetAutoSave(self, isAutoSave: bool) -> None:
        ...
    def GetAutoSave(self) -> bool:
        ...


class LayoutStateApplicator(Builder):
    def __init__(self) -> None: ...
    def SetLayoutState(self, layoutState: CAE.LayoutState) -> None:
        ...
    def SetFile(self, filePath: str) -> None:
        ...
    def SetUpdateLayoutState(self, update: bool) -> None:
        ...
    def GetUpdateLayoutState(self) -> bool:
        ...
    DataReferences: CAE.LayoutStateDataReferenceCollection


class LayoutState(TaggedObject):
    def __init__(self) -> None: ...
    def Export(self, filePath: str) -> None:
        ...
    def ExportForValidation(self, filePath: str) -> None:
        ...
    def CustomExportForValidation(self, filePath: str, filters: str) -> None:
        ...
    def Rename(self, name: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.LayoutState.Name instead.")"""
        ...
    def GetViewportContents(self) -> typing.List[CAE.LayoutState.ViewportContent]:
        ...
    def GetViewportDescription(self, viewport: int) -> str:
        ...
    def GetViewportDescription(self, viewportContent: CAE.LayoutState.ViewportContent) -> str:
        ...
    def SetViewportDescription(self, viewport: int, xmloutput: str) -> None:
        ...
    def SetViewportDescriptionWithOption(self, viewport: int, pasteOption: str, xmloutput: str) -> None:
        ...
    def GetViewportName(self, viewport: int) -> str:
        ...
    def SetViewportName(self, viewport: int, name: str) -> None:
        ...
    def GetViewportAvailablePasteOptions(self, viewport: int, cliboardInformation: str) -> typing.List[CAE.LayoutState.PasteOption]:
        ...
    Name: str


    class ViewportContentType(enum.Enum):
        Viewport = 0
        Page = 1
        CurveOperation = 2
    

    class LayoutStateViewportContent():
        Name: str
        Type: CAE.LayoutState.ViewportContentType
        Path: str
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, Type: CAE.LayoutState.ViewportContentType, Path: str) -> None: ...
    

    class LayoutStatePasteOption():
        Key: str
        LocalizedValue: str
        IconName: str
        Category: int
        ParentCommandKey: str
        Tooltip: str
        def ToString(self) -> str:
            ...
    

    class LayoutState_ViewportContent():
        name: int
        type: CAE.LayoutState.ViewportContentType
        path: int
    

    class LayoutState_PasteOption():
        key: int
        localizedValue: int
        iconName: int
        category: int
        parentCommandKey: int
        tooltip: int
    

class LaminateViewDrapingResultsBuilder(Builder):
    def __init__(self) -> None: ...


    class OuputChoice(enum.Enum):
        Spreadsheet = 0
        Csv = 1
    

class LaminateSpreadsheetReportCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateSpreadsheetReport]:
        ...
    def __init__(self, owner: CAE.LaminatePostReport) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminateSpreadsheetReport:
        ...
    def DeleteReport(self, spreadsheetReport: CAE.LaminateSpreadsheetReport) -> None:
        ...
    def CloneReport(self, spreadsheetReport: CAE.LaminateSpreadsheetReport) -> None:
        ...
    def Tag(self) -> Tag: ...



class LaminateSpreadsheetReportBuilder(Builder):
    def __init__(self) -> None: ...
    AbsValueFilter: bool
    AbsValueSort: bool
    DetailedOutput: bool
    ElemNodalOption: CAE.LaminateSpreadsheetReportBuilder.ElemNodalOptionType
    ElementFilter: CAE.LaminateElementFilterBuilder
    FailureIndex: bool
    FailureIndexRule: CAE.LaminateSpreadsheetReportBuilder.EnvelopeRule
    FailureMode: CAE.LaminateSpreadsheetReportBuilder.FailureModeType
    FilterType: CAE.LaminateSpreadsheetReportBuilder.FilteringType
    InterLamFTOverride1: CAE.LaminatePly.InterLaminarFailureTheoryType
    InterLamFTOverride1State: bool
    InterLamFTOverride2: CAE.LaminatePly.InterLaminarFailureTheoryType
    InterLamFTOverride2State: bool
    Name: str
    PlyBottom: bool
    PlyFTOverride1: CAE.LaminatePly.PlyFailureTheoryType
    PlyFTOverride1State: bool
    PlyFTOverride2: CAE.LaminatePly.PlyFailureTheoryType
    PlyFTOverride2State: bool
    PlyFilter: CAE.LaminatePlyFilterBuilder
    PlyMiddle: bool
    PlyStrainOutput: bool
    PlyStrainRule: CAE.LaminateSpreadsheetReportBuilder.EnvelopeRule
    PlyStressCoordSys: CAE.LaminateSpreadsheetReportBuilder.CoordinateSystemType
    PlyStressMaxP: bool
    PlyStressMaxS: bool
    PlyStressMinP: bool
    PlyStressOutput: bool
    PlyStressRule: CAE.LaminateSpreadsheetReportBuilder.EnvelopeRule
    PlyStressXX: bool
    PlyStressXY: bool
    PlyStressYY: bool
    PlyStressYZ: bool
    PlyStressZX: bool
    PlyStressZZ: bool
    PlyTop: bool
    PlyVonMises: bool
    ReportObject: CAE.LaminateReportObject
    SafetyFactor: float
    SafetyMargin: bool
    SafetyMarginRule: CAE.LaminateSpreadsheetReportBuilder.EnvelopeRule
    ShellResultantFx: bool
    ShellResultantFxy: bool
    ShellResultantFy: bool
    ShellResultantMx: bool
    ShellResultantMxy: bool
    ShellResultantMy: bool
    ShellResultantQx: bool
    ShellResultantQy: bool
    SolverInput: CAE.LaminateSpreadsheetReportBuilder.SolverInputType
    SolverPlyStress: bool
    SolverShellResultant: bool
    SortOrder: CAE.LaminateSpreadsheetReportBuilder.SortOrderType
    SortType: CAE.LaminateSpreadsheetReportBuilder.SortingType
    StrengthRatio: bool
    StrengthRatioRule: CAE.LaminateSpreadsheetReportBuilder.EnvelopeRule
    ThresholdType: CAE.LaminateSpreadsheetReportBuilder.ThreshType
    ThresholdValue: float
    UserDefinedInterLamFTOverride1: str
    UserDefinedInterLamFTOverride2: str
    UserDefinedPlyFTOverride1: str
    UserDefinedPlyFTOverride2: str


    class ThreshType(enum.Enum):
        AboveTreshold = 0
        BelowTreshold = 1
    

    class SortOrderType(enum.Enum):
        Ascending = 0
        Descending = 1
    

    class SortingType(enum.Enum):
        ElementId = 0
        PlyId = 1
        StressXX = 2
        StressYY = 3
        StressZZ = 4
        StressXY = 5
        StressZX = 6
        StressYZ = 7
        StressMaxP = 8
        StressMinP = 9
        StressMaxS = 10
        StressVonMises = 11
        StrainXX = 12
        StrainYY = 13
        StrainZZ = 14
        StrainXY = 15
        StrainZX = 16
        StrainYZ = 17
        StrainMaxP = 18
        StrainMinP = 19
        StrainMaxS = 20
        StrainVonMises = 21
        PlyFailureIndex = 22
        PlyStrengthRatio = 23
        PlyMarginofSafety = 24
        BondFailureIndex = 25
        BondStrengthRatio = 26
        BondMarginofSafety = 27
    

    class SolverInputType(enum.Enum):
        ShellStress = 0
        PlyStress = 1
    

    class FilteringType(enum.Enum):
        None = 0
        StressXX = 1
        StressYY = 2
        StressZZ = 3
        StressXY = 4
        StressZX = 5
        StressYZ = 6
        StressMaxP = 7
        StressMinP = 8
        StressMaxS = 9
        StressVonMises = 10
        StrainXX = 11
        StrainYY = 12
        StrainZZ = 13
        StrainXY = 14
        StrainZX = 15
        StrainYZ = 16
        StrainMaxP = 17
        StrainMinP = 18
        StrainMaxS = 19
        StrainVonMises = 20
        PlyFailureIndex = 21
        PlyStrengthRatio = 22
        PlyMarginofSafety = 23
        BondFailureIndex = 24
        BondStrengthRatio = 25
        BondMarginofSafety = 26
    

    class FailureModeType(enum.Enum):
        InPlanePly = 0
        Interlaminar = 1
        Both = 2
    

    class EnvelopeRule(enum.Enum):
        MaxMin = 0
        Min = 1
        Max = 2
        AbsMax = 3
        AbsMin = 4
    

    class ElemNodalOptionType(enum.Enum):
        Elemental = 0
        Nodal = 1
    

    class CoordinateSystemType(enum.Enum):
        Ply = 0
        Laminate = 1
    

class LaminateSpreadsheetReport(NXObject):
    def __init__(self) -> None: ...
    def ExportCsvFile(self, filename: str) -> None:
        ...


class LaminateSineEventBuilder(CAE.LaminateDynamicEventBuilder):
    def __init__(self) -> None: ...
    def SelectModes(self, selectedModes: typing.List[CAE.LaminateModeProperty]) -> None:
        ...
    def SetAdditionalFrequencies(self, additionalFrequencies: float) -> None:
        ...
    AdditionalFrequenciesBreakPoints: bool
    AdditionalFrequenciesUnits: CAE.LaminateSineEventBuilder.AdditionalFrequeciesUnitsEnum
    IntermediateFrequenciesBetweenOption: CAE.LaminateSineEventBuilder.IntermediateFrequeciesBetweenEnum
    IntermediateFrequenciesCluster: float
    IntermediateFrequenciesEnable: bool
    IntermediateFrequenciesIncludeNatFreq: bool
    IntermediateFrequenciesNumExcitations: int
    IntermediateFrequenciesNumIncrements: int
    IntermediateFrequenciesOption: CAE.LaminateSineEventBuilder.IntermediateFrequeciesEnum
    NaturalFrequenciesChoice: CAE.LaminateSineEventBuilder.NaturalFrequeciesEnum
    NaturalFrequenciesEnable: bool


    class NaturalFrequeciesEnum(enum.Enum):
        All = 0
        Select = 1
    

    class IntermediateFrequeciesEnum(enum.Enum):
        IncrementLinear = 0
        IncrementLogarithmic = 1
        BetweenFrequencies = 2
    

    class IntermediateFrequeciesBetweenEnum(enum.Enum):
        Linear = 0
        Logarithmic = 1
    

    class AdditionalFrequeciesUnitsEnum(enum.Enum):
        Hz = 0
        KHz = 1
        MHz = 2
        GHz = 3
    

class LaminateSineEvent(CAE.LaminateDynamicEvent):
    def __init__(self) -> None: ...


class LaminateSelectEntitiesBuilder(Builder):
    def __init__(self) -> None: ...
    def Clear(self) -> None:
        ...
    def AddEntities(self, objects: typing.List[CAE.SetObject]) -> None:
        ...
    SelectionList: SelectTaggedObjectList


class LaminateReportObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateReportObject]:
        ...
    def __init__(self, owner: CAE.LaminateManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminateReportObject:
        ...
    def DeleteReportObject(self, reportObj: CAE.LaminateReportObject) -> None:
        ...
    def CloneReportObject(self, reportObj: CAE.LaminateReportObject) -> None:
        ...
    def CreateReportObjectBuilder(self, laminateReportObjTag: CAE.LaminateReportObject) -> CAE.LaminateReportObjectBuilder:
        ...
    def Tag(self) -> Tag: ...



class LaminateReportObjectBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSelectedGroups(self, selectedGroups: typing.List[NXObject]) -> None:
        ...
    def GetSelectedPlyNames(self, selectedPlyNames: str) -> None:
        ...
    def SetSelectedPlyNames(self, selectedPlies: str) -> None:
        ...
    GroupReference: bool
    ReportObjLabel: int
    ReportObjName: str
    SelectAllElements: bool
    SelectAllPlies: bool
    SelectElements: CAE.SelectElementsBuilder


class LaminateReportObject(NXObject):
    def __init__(self) -> None: ...


class LaminateRelabelPliesBuilder(Builder):
    def __init__(self) -> None: ...
    def AddGlobalLayup(self, layup: CAE.LaminateGlobalLayup) -> None:
        ...
    Increment: int
    MinLabel: int
    Offset: int
    RelabelOption: CAE.LaminateRelabelPliesBuilder.RelabelOptionEnum


    class RelabelOptionEnum(enum.Enum):
        LabelAndIncrement = 0
        Offset = 1
    

class LaminateRandomEventBuilder(CAE.LaminateDynamicEventBuilder):
    def __init__(self) -> None: ...
    def GetOutputRequest(self) -> CAE.ModelingObjectPropertyTable:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.LaminateDynamicEventBuilder.GetOutputRequestObject instead.")"""
        ...
    def SetOutputRequest(self, ssmo: CAE.ModelingObjectPropertyTable) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.LaminateDynamicEventBuilder.SetOutputRequestObject instead.")"""
        ...
    ConfidenceLevel: float
    ConfidenceLevelOption: CAE.LaminateRandomEventBuilder.ConfidenceLevelOptionEnum
    EventName: str
    ExcitationAxis: CAE.LaminateRandomEventBuilder.ExcitationAxisEnum
    ExcitationCoordinateSystem: CoordinateSystem
    Function: TaggedObject
    LowerBoundFreq: float
    NastranBasic: bool
    Reference: CAE.LaminateRandomEventBuilder.ReferenceEnum
    StandardDeviation: float
    UpperBoundFreq: float


    class ReferenceEnum(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class ExcitationAxisEnum(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class ConfidenceLevelOptionEnum(enum.Enum):
        UserDef = 0
        StandardDev = 1
    

class LaminateRandomEvent(CAE.LaminateDynamicEvent):
    def __init__(self) -> None: ...


class LaminateQuickReportCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateQuickReport]:
        ...
    def __init__(self, owner: CAE.LaminatePostReport) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminateQuickReport:
        ...
    def DeleteReport(self, quickReport: CAE.LaminateQuickReport) -> None:
        ...
    def CloneReport(self, quickReport: CAE.LaminateQuickReport) -> None:
        ...
    def Tag(self) -> Tag: ...



class LaminateQuickReportBuilder(Builder):
    def __init__(self) -> None: ...
    ElemNodalOption: CAE.LaminateQuickReportBuilder.ElemNodalOptionType
    FailureIndex: bool
    FailureIndexRule: CAE.LaminateQuickReportBuilder.EnvelopeRule
    Name: str
    PlyStrain: bool
    PlyStrainRule: CAE.LaminateQuickReportBuilder.EnvelopeRule
    PlyStress: bool
    PlyStressRule: CAE.LaminateQuickReportBuilder.EnvelopeRule
    ShellStress: bool
    ShellStressRule: CAE.LaminateQuickReportBuilder.EnvelopeRule
    StrengthRatio: bool
    StrengthRatioRule: CAE.LaminateQuickReportBuilder.EnvelopeRule


    class EnvelopeRule(enum.Enum):
        MaxMin = 0
        Min = 1
        Max = 2
        AbsMax = 3
        AbsMin = 4
    

    class ElemNodalOptionType(enum.Enum):
        Elemental = 0
        Nodal = 1
    

class LaminateQuickReport(NXObject):
    def __init__(self) -> None: ...
    def ExportCsvFile(self, filename: str) -> None:
        ...


class LaminatePostReportCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminatePostReport]:
        ...
    def __init__(self, owner: CAE.LaminateManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminatePostReport:
        ...
    def DeletePostReport(self, postReport: CAE.LaminatePostReport) -> None:
        ...
    def ClonePostReport(self, postReport: CAE.LaminatePostReport) -> None:
        ...
    def CreateLaminatePostReportBuilder(self, postReport: CAE.LaminatePostReport) -> CAE.LaminatePostReportBuilder:
        ...
    def CreateLaminateSpreadsheetReportBuilder(self, spreadsheetReport: CAE.LaminateSpreadsheetReport) -> CAE.LaminateSpreadsheetReportBuilder:
        ...
    def CreateLaminateGraphicalReportBuilder(self, graphicalReport: CAE.LaminateGraphicalReport) -> CAE.LaminateGraphicalReportBuilder:
        ...
    def CreateLaminateQuickReportBuilder(self, quickReport: CAE.LaminateQuickReport) -> CAE.LaminateQuickReportBuilder:
        ...
    def Tag(self) -> Tag: ...

    ActivePostReport: CAE.LaminatePostReport


class LaminatePostReportBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSelectedResults(self, resultNames: str, loadcaseNames: str, iterationNames: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.LaminatePostReport.GetSelectedSolutions instead.")"""
        ...
    def SetSelectedResults(self, resultNames: str, loadcaseNames: str, iterationNames: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.LaminatePostReport.SetSelectedSolutions instead.")"""
        ...
    def GetSelectedSolutions(self, solutionNames: str, selectAllSubcases: bool, loadcaseNames: str, iterationNames: str) -> None:
        ...
    def SetSelectedSolutions(self, solutionNames: str, selectAllSubcases: bool, loadcaseNames: str, iterationNames: str) -> None:
        ...
    Name: str


class LaminatePostReport(NXObject):
    def __init__(self) -> None: ...
    LaminateSpreadsheetReports: CAE.LaminateSpreadsheetReportCollection
    LaminateGraphicalReports: CAE.LaminateGraphicalReportCollection
    LaminateQuickReports: CAE.LaminateQuickReportCollection
    Name: str


class LaminatePlySectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminatePlySection]:
        ...
    def __init__(self, owner: CAE.LaminateGlobalLayupMgr) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.LaminatePlySection:
        ...
    def Tag(self) -> Tag: ...



class LaminatePlySectionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSelectedLaminates(self, laminates: typing.List[CAE.Laminate]) -> None:
        ...
    def SetSelectedLaminates(self, laminates: typing.List[CAE.Laminate]) -> None:
        ...
    CoreOffsetScale: float
    PlyColor: int
    PlyOffsetScale: float
    SectionName: str
    SectionPlane: Plane
    SelectAllLaminates: bool


class LaminatePlySection(NXObject):
    def __init__(self) -> None: ...
    def RemovePlySection(self) -> None:
        ...
    def CopyPlySection(self, name: str) -> None:
        ...
    def ComputeSectionCurves(self) -> None:
        ...
    def Information(self) -> None:
        ...
    ActiveStatus: bool
    Name: str


class LaminatePlyMaxThicknessVarBuilder(Builder):
    def __init__(self) -> None: ...
    ThicknessOverride: bool
    ThicknessVariationDownLimit: float
    ThicknessVariationUpLimit: float


class LaminatePlyGroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminatePlyGroup]:
        ...
    def __init__(self, owner: CAE.Laminate) -> None: ...
    def __init__(self) -> None: ...
    def InsertSinglePly(self, insertionIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def InsertPlyGroup(self, name: str, insertionIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def InsertLinkedPlyGroup(self, name: str, linkType: CAE.LaminatePlyGroup.Link, parentName: str, insertionIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def DeletePlyGroup(self, groupIndex: int) -> None:
        ...
    def GetPlyGroup(self, groupIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def Tag(self) -> Tag: ...



class LaminatePlyGroup(NXObject):
    def __init__(self) -> None: ...
    Plies: CAE.LaminatePlyCollection
    LinkType: CAE.LaminatePlyGroup.Link
    Name: str


    class Link(enum.Enum):
        None = 0
        Repeat = 1
        Symm = 2
        Anti = 3
        Rev = 4
    

class LaminatePlyFilterBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSelectedPlyNames(self, selectedPlyNames: str) -> None:
        ...
    def SetSelectedPlyNames(self, selectedPlies: str) -> None:
        ...
    SelectAllPlies: bool


class LaminatePlyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminatePly]:
        ...
    def __init__(self, owner: CAE.LaminatePlyGroup) -> None: ...
    def __init__(self) -> None: ...
    def InsertPly(self, insertionIndex: int, thickness: float, orientation: float, color: int) -> CAE.LaminatePly:
        ...
    def InsertCohesiveLayer(self, insertionIndex: int, orientation: float, color: int) -> CAE.LaminatePly:
        ...
    def DeletePly(self, index: int) -> None:
        ...
    def GetPly(self, plyIndex: int) -> CAE.LaminatePly:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.LaminatePly:
        ...
    def Tag(self) -> Tag: ...



class LaminatePly(NXObject):
    def __init__(self) -> None: ...
    def CreateDrapingDataBuilder(self) -> CAE.LaminateDrapingDataBuilder:
        ...
    def CreateDrapingExtensionBuilder(self) -> CAE.LaminateDrapingExtensionBuilder:
        ...
    def CreateLaminatePlyMaxThicknessVarBuilder(self) -> CAE.LaminatePlyMaxThicknessVarBuilder:
        ...
    def AssignThicknessExpression(self, thickExp: str) -> None:
        ...
    def AssignAngleExpression(self, angleExp: str) -> None:
        ...
    def CopyDrapingResults(self, drapingResults: CAE.LaminateDrapingOrientation) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.LaminatePly.CopyDrapingResultsInstance instead.")"""
        ...
    def CopyDrapingResultsInstance(self, drapingResults: CAE.LaminateIDrapingOrientation) -> None:
        ...
    def SetMaterialByName(self, name: str) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.LaminatePly.SetMaterial instead.")"""
        ...
    def SetPlyMaterialByName(self, name: str) -> None:
        ...
    def GetMaterialName(self) -> str:
        ...
    def Information(self, detailed: bool) -> None:
        ...
    def ComputeDraping(self) -> None:
        ...
    def ExportDrapingResults(self, csvFilename: str, showShearAngle: bool, showYarnAngle: bool, showPrimaryDirection: bool, showSecondaryDirection: bool, showNormalDirection: bool) -> None:
        ...
    def ExportDrapingDomainAsGroup(self) -> None:
        ...
    def ResetExtensionTarget(self, targetPly: CAE.LaminatePly) -> None:
        ...
    def SetMaterial(self, tMat: TaggedObject) -> None:
        ...
    AngleExpression: Expression
    Color: int
    Description: str
    DrapingExtension: CAE.LaminateDrapingExtension
    DrapingInput: CAE.LaminateDrapingData
    GlobalId: int
    InterLaminarFailureTheory: CAE.LaminatePly.InterLaminarFailureTheoryType
    Orientation: float
    PlyFailureTheory: CAE.LaminatePly.PlyFailureTheoryType
    SolidProperty: CAE.LaminatePly.SolidPropertyType
    StressStrainRequest: bool
    Thickness: float
    ThicknessExpression: Expression
    UserDefinedInterLaminarFailureTheory: str
    UserDefinedPlyFailureTheory: str


    class SolidPropertyType(enum.Enum):
        Layered = 0
        Homogeneous = 1
    

    class PlyFailureTheoryType(enum.Enum):
        None = 0
        Hill = 1
        Hoffman = 2
        TsaiWu = 3
        MaxStrain = 4
        MaxStress = 5
        MaxTransverseShear = 6
        VonMisesYield = 7
        VonMisesUltimate = 8
        ProgressiveFailure = 9
        UserDefined = 10
        InheritedFromMaterial = 11
    

    class InterLaminarFailureTheoryType(enum.Enum):
        None = 0
        TransverseShearStress = 1
        NormalStress = 2
        UserDefined = 3
        InheritedFromMaterial = 4
    

class LaminateModePropertyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateModeProperty]:
        ...
    def __init__(self, owner: CAE.LaminateDynamicSim) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminateModeProperty:
        ...
    def Tag(self) -> Tag: ...



class LaminateModeProperty(NXObject):
    def __init__(self) -> None: ...
    def SetActiveStatus(self, activeStatus: bool) -> None:
        ...
    def SetViscousDampingFactor(self, dampingFactor: float) -> None:
        ...


class LaminateMatOrientationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateMatOrientation]:
        ...
    def __init__(self, owner: CAE.LaminateGlobalLayupMgr) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.LaminateMatOrientation:
        ...
    def Tag(self) -> Tag: ...



class LaminateMatOrientationBuilder(Builder):
    def __init__(self) -> None: ...
    RefPlyId: int
    Selection: CAE.LaminateSelectEntitiesBuilder


class LaminateMatOrientation(NXObject):
    def __init__(self) -> None: ...
    Name: str


class LaminateManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def Tag(self) -> Tag: ...

    PostReports: CAE.LaminatePostReportCollection
    DynamicSims: CAE.LaminateDynamicSimCollection
    ReportObjects: CAE.LaminateReportObjectCollection


class LaminateLockAngleBuilder(Builder):
    def __init__(self) -> None: ...
    LockAngle: float


class LaminateLayupOffsetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateLayupOffset]:
        ...
    def __init__(self, owner: CAE.LaminateGlobalLayupMgr) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.LaminateLayupOffset:
        ...
    def Tag(self) -> Tag: ...



class LaminateLayupOffsetBuilder(Builder):
    def __init__(self) -> None: ...
    FiberDistance: float
    RefPlanePosition: Expression
    Selection: CAE.LaminateSelectEntitiesBuilder


class LaminateLayupOffset(NXObject):
    def __init__(self) -> None: ...
    Name: str


class LaminateImportZonesBuilder(Builder):
    def __init__(self) -> None: ...
    Filename: str
    ImportBoundaries: bool
    ImportMaterials: bool
    OverwriteCollectors: bool
    OverwriteLamProps: bool
    OverwriteMaterials: bool
    SearchDistance: Expression
    Selection: CAE.LaminateSelectEntitiesBuilder


class LaminateImportedPlyBuilder(Builder):
    def __init__(self) -> None: ...
    FillPartiallyMappedFaces: bool
    FillUnmappedFaceThreshold: float
    OmitPartiallyMapped: bool
    UnmappedFaceThreshold: float


class LaminateImportedLayupBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateApiLaminateList(self) -> None:
        ...
    def SelectLaminate(self, laminate: str) -> None:
        ...
    ApiType: CAE.LaminateImportedLayupBuilder.ApiTypeEnum
    ElementalElemSelection: CAE.SelectElementsBuilder
    ElementalMapping: int
    ElementalNodalMapping: int
    FileName: str
    FileType: CAE.LaminateImportedLayupBuilder.FileEnum
    FillPartiallyMappedFaces: bool
    FillUnmappedFaceThreshold: float
    ImportDescriptionFromName: bool
    ImportMaterials: bool
    ImportMethod: CAE.LaminateImportedLayupBuilder.ImportMethodEnum
    LayupName: str
    MaxDeviationAngle: Expression
    MeshSizeFactor: float
    NameOverride: bool
    NodalMapping: int
    NumDiscretizationPoints: int
    OmitPartiallyMapped: bool
    OverridePlyMappingOptions: bool
    OverwriteMaterials: bool
    Selection: CAE.LaminateSelectEntitiesBuilder
    Tolerance: Expression
    UnmappedFaceThreshold: float


    class ImportMethodEnum(enum.Enum):
        ExternalFile = 0
        ExternalApi = 1
    

    class FileEnum(enum.Enum):
        FiberSimXml = 0
        FiberSimH5 = 1
        SimulaytLayup = 2
        FiberSimPart = 3
        CatiaPlyGroups = 4
    

    class ApiTypeEnum(enum.Enum):
        FiberSim = 0
    

class LaminateIDrapingOrientation(NXObject):
    def __init__(self) -> None: ...


class LaminateGraphicalReportCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateGraphicalReport]:
        ...
    def __init__(self, owner: CAE.LaminatePostReport) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminateGraphicalReport:
        ...
    def DeleteReport(self, graphicalReport: CAE.LaminateGraphicalReport) -> None:
        ...
    def CloneReport(self, graphicalReport: CAE.LaminateGraphicalReport) -> None:
        ...
    def Tag(self) -> Tag: ...



class LaminateGraphicalReportBuilder(Builder):
    def __init__(self) -> None: ...
    CoordinateSystem: CAE.LaminateGraphicalReportBuilder.CoordinateSystemType
    ElemNodalOption: CAE.LaminateGraphicalReportBuilder.ElemNodalOptionType
    ElementFilter: CAE.LaminateElementFilterBuilder
    FailureIndex: bool
    FailureIndexRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    FailureMode: CAE.LaminateGraphicalReportBuilder.FailureModeType
    InterLamFTOverride1: CAE.LaminatePly.InterLaminarFailureTheoryType
    InterLamFTOverride1State: bool
    InterLamFTOverride2: CAE.LaminatePly.InterLaminarFailureTheoryType
    InterLamFTOverride2State: bool
    Name: str
    OverallOnly: bool
    PlyBottom: bool
    PlyExportOption: CAE.LaminateGraphicalReportBuilder.PlyExportOptionType
    PlyFTOverride1: CAE.LaminatePly.PlyFailureTheoryType
    PlyFTOverride1State: bool
    PlyFTOverride2: CAE.LaminatePly.PlyFailureTheoryType
    PlyFTOverride2State: bool
    PlyFilter: CAE.LaminatePlyFilterBuilder
    PlyMiddle: bool
    PlyStrain: bool
    PlyStrainRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    PlyStress: bool
    PlyStressRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    PlyTop: bool
    ReportObject: CAE.LaminateReportObject
    SafetyFactor: float
    SafetyMargin: bool
    SafetyMarginRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    ShowLoadCases: bool
    ShowPlyResults: bool
    SolverInput: CAE.LaminateGraphicalReportBuilder.SolverInputType
    StrengthRatio: bool
    StrengthRatioRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    UserDefinedInterLamFTOverride1: str
    UserDefinedInterLamFTOverride2: str
    UserDefinedPlyFTOverride1: str
    UserDefinedPlyFTOverride2: str


    class SolverInputType(enum.Enum):
        SolverShellStressResultant = 0
        SolverPlyStressesAndStrains = 1
    

    class PlyExportOptionType(enum.Enum):
        GlobalPlyId = 0
        Layer = 1
    

    class FailureModeType(enum.Enum):
        InPlanePly = 0
        Interlaminar = 1
        Both = 2
    

    class EnvelopeRule(enum.Enum):
        MaxMin = 0
        Min = 1
        Max = 2
        AbsMax = 3
        AbsMin = 4
    

    class ElemNodalOptionType(enum.Enum):
        Elemental = 0
        Nodal = 1
    

    class CoordinateSystemType(enum.Enum):
        Ply = 0
        Laminate = 1
    

class LaminateGraphicalReport(NXObject):
    def __init__(self) -> None: ...
    def GenerateResults(self) -> None:
        ...


class LaminateGlobalLayupPlyGroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminatePlyGroup]:
        ...
    def __init__(self, owner: CAE.LaminateGlobalLayup) -> None: ...
    def __init__(self) -> None: ...
    def InsertSinglePly(self, insertionIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def InsertCohesiveLayer(self, insertionIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def InsertPlyGroup(self, name: str, insertionIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def InsertLinkedPlyGroup(self, name: str, linkType: CAE.LaminatePlyGroup.Link, parentName: str, insertionIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def InsertPlyExtension(self, plyGroup: CAE.LaminatePlyGroup, insertionIndex: int, targetPly: CAE.LaminatePly) -> CAE.LaminatePly:
        ...
    def DeletePlyGroup(self, groupIndex: int) -> None:
        ...
    def GetPlyGroup(self, groupIndex: int) -> CAE.LaminatePlyGroup:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.LaminatePlyGroup:
        ...
    def InsertPlyGroupLayupLink(self, name: str, insertionIndex: int, laminateGlobalLayupSource: CAE.LaminateGlobalLayup) -> CAE.LaminatePlyGroup:
        ...
    def Tag(self) -> Tag: ...



class LaminateGlobalLayupMgr(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def CreateGlobalLayupImportFromPptBuilder(self) -> CAE.GlobalLayupImportFromPptBuilder:
        ...
    def CreateLayupOffsetBuilder(self, layupoffset: CAE.LaminateLayupOffset) -> CAE.LaminateLayupOffsetBuilder:
        ...
    def CreateLaminateMatOrientationBuilder(self, matOrientation: CAE.LaminateMatOrientation) -> CAE.LaminateMatOrientationBuilder:
        ...
    def CreateViewLaminateBuilder(self, laminate: CAE.Laminate, zoneIndex: int) -> CAE.ViewLaminateBuilder:
        ...
    def CreateFlatPatternsBuilder(self) -> CAE.FlatPatternsBuilder:
        ...
    def CreateViewDrapingResultsBuilder(self, globalLayup: CAE.LaminateGlobalLayup, ply: CAE.LaminatePly) -> CAE.LaminateViewDrapingResultsBuilder:
        ...
    def RemoveMaterialOrientation(self, matOrientation: int) -> None:
        ...
    def RemoveLayupOffset(self, layupOffset: int) -> None:
        ...
    def CreateLaminateExtrudeSetupBuilder(self, extrudeSetup: CAE.LaminateExtrudeSetup) -> CAE.LaminateExtrudeSetupBuilder:
        ...
    def CreateLaminateFillSetupBuilder(self, extrudeSetup: CAE.LaminateExtrudeSetup) -> CAE.LaminateFillSetupBuilder:
        ...
    def CreateLaminateImportedLayupBuilder(self, globalLayup: CAE.LaminateGlobalLayup) -> CAE.LaminateImportedLayupBuilder:
        ...
    def UpdateDraping(self) -> None:
        ...
    def UpdatePlyDraping(self, plies: typing.List[CAE.LaminatePly]) -> None:
        ...
    def Information(self) -> None:
        ...
    def ComputeZones(self) -> None:
        ...
    def ExportZoneInformation(self, csvFilename: str) -> None:
        ...
    def CreateLaminateSelectEntitiesBuilder(self) -> CAE.LaminateSelectEntitiesBuilder:
        ...
    def ExportZonesAsGroups(self) -> None:
        ...
    def ExportZonesAsLaminates(self) -> None:
        ...
    def ExportDrapingDomainAsGroups(self) -> None:
        ...
    def AutogroupByMaterials(self) -> None:
        ...
    def AutogroupLayupsByMaterials(self, layups: typing.List[CAE.LaminateGlobalLayup]) -> None:
        ...
    def CreateLaminateImportZonesBuilder(self) -> CAE.LaminateImportZonesBuilder:
        ...
    def CreateRelabelPliesBuilder(self) -> CAE.LaminateRelabelPliesBuilder:
        ...
    def RelinkAllGlobalLayups(self) -> None:
        ...
    def CreateLaminatePlyMaxThicknessVarBuilder(self, listOfSelectedPlies: typing.List[CAE.LaminatePly]) -> CAE.LaminatePlyMaxThicknessVarBuilder:
        ...
    def CreatePlySectionBuilder(self, plySection: CAE.LaminatePlySection) -> CAE.LaminatePlySectionBuilder:
        ...
    def Display2dFiberOrientations(self, plyNames: str, xform: Matrix4x4) -> None:
        ...
    def Display2dFiberOrientations(self, plyNames: str, displayOptions: bool, colors: int, xform: Matrix4x4) -> None:
        ...
    def Display3dFiberOrientations(self, plyNames: str, displayOptions: bool, colors: int, xform: Matrix4x4) -> None:
        ...
    def EraseFiberOrientations(self) -> None:
        ...
    def CreateMultipleDrapingDataBuilder(self, plies: typing.List[CAE.LaminatePly]) -> CAE.LaminateDrapingDataBuilder:
        ...
    def SetButtjointCompareOption(self, buttJointOption: CAE.LaminateGlobalLayupMgr.ButtjointOption) -> None:
        ...
    def CreateLaminateImportedPlyBuilder(self, plies: typing.List[CAE.LaminatePly]) -> CAE.LaminateImportedPlyBuilder:
        ...
    def ReimportPlies(self, plies: typing.List[CAE.LaminatePly]) -> None:
        ...
    def CreateAnnotationBuilder(self) -> CAE.LaminateAnnotationBuilder:
        ...
    def Tag(self) -> Tag: ...

    GlobalLayups: CAE.LaminateGlobalLayupCollection
    LayupOffsets: CAE.LaminateLayupOffsetCollection
    MatOrientations: CAE.LaminateMatOrientationCollection
    ExtrudeSetups: CAE.LaminateExtrudeSetupCollection
    PlySections: CAE.LaminatePlySectionCollection
    DefaultLayupOffset: CAE.LaminateLayupOffset
    DefaultMaterialOrientation: int


    class ButtjointOption(enum.Enum):
        None = 0
        Int = 1
        String = 2
    

class LaminateGlobalLayupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateGlobalLayup]:
        ...
    def __init__(self, owner: CAE.LaminateGlobalLayupMgr) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.LaminateGlobalLayup:
        ...
    def CreateGlobalLayup(self) -> CAE.LaminateGlobalLayup:
        ...
    def DeleteGlobalLayup(self, layupToRemove: CAE.LaminateGlobalLayup) -> None:
        ...
    def Tag(self) -> Tag: ...



class LaminateGlobalLayup(NXObject):
    def __init__(self) -> None: ...
    def CreateFiberOrientationOptionsBuilder(self) -> CAE.LaminateFiberOrientationOptionsBuilder:
        ...
    def CreateLockAngleBuilder(self) -> CAE.LaminateLockAngleBuilder:
        ...
    def ClearLayup(self) -> None:
        ...
    def RefreshLinkedGroups(self) -> None:
        ...
    def Information(self, detailed: bool) -> None:
        ...
    def UpdateDraping(self) -> None:
        ...
    def ExportDrapingResults(self, csvFilename: str, showShearAngle: bool, showYarnAngle: bool, showPrimaryDirection: bool, showSecondaryDirection: bool, showNormalDirection: bool) -> None:
        ...
    def ExportDrapingDomainAsGroups(self, individualPlyGroups: bool) -> None:
        ...
    def ExportLayup(self, csvFilename: str) -> None:
        ...
    def DefineSymPlyidRange(self, minId: int, maxId: int) -> None:
        ...
    def ExportPliesToFibersim(self, filename: str) -> None:
        ...
    def AutogroupByMaterials(self) -> None:
        ...
    PlyGroups: CAE.LaminateGlobalLayupPlyGroupCollection
    ActiveStatus: bool
    FiberOrientationOptions: CAE.LaminateFiberOrientationOptions
    Label: int
    Name: str
    StackingRecipe: CAE.LaminateGlobalLayup.StackingRecipeType


    class StackingRecipeType(enum.Enum):
        Normal = 0
        Symmetric = 1
        SymmetricWithCore = 2
        Repeated = 3
        RepeatedWithCore = 4
    

class LaminateFillSetupBuilder(Builder):
    def __init__(self) -> None: ...
    FillName: str
    HomogeneousPlies: bool
    LimitThicknessVariation: bool
    SamcefElementType: CAE.LaminateFillSetupBuilder.SamcefElementTypeEnum
    SamcefSolidShells: bool
    Selection: CAE.LaminateSelectEntitiesBuilder
    SinglePlyPerLayer: bool
    ThicknessVariationDownLimit: float
    ThicknessVariationUpLimit: float


    class SamcefElementTypeEnum(enum.Enum):
        Solid = 0
        SolidShell = 1
        SolidPly = 2
    

class LaminateFiberOrientationOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    Spectrum: int
    YellowPoint: float


class LaminateFiberOrientationOptions(NXObject):
    def __init__(self) -> None: ...


class LaminateExtrudeSetupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateExtrudeSetup]:
        ...
    def __init__(self, owner: CAE.LaminateGlobalLayupMgr) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.LaminateExtrudeSetup:
        ...
    def RemoveExtrudeSetup(self, setup: CAE.LaminateExtrudeSetup) -> None:
        ...
    def Tag(self) -> Tag: ...



class LaminateExtrudeSetupBuilder(Builder):
    def __init__(self) -> None: ...
    def AddSandwichCorePly(self, ply: CAE.LaminatePly) -> bool:
        ...
    def ClearSandwichCorePly(self, clear: bool) -> None:
        ...
    CutFaceDrops: bool
    CutFaceSelect: CAE.SelectCAEFaceList
    Cuts: bool
    ExtrudeName: str
    FlipNormals: bool
    HomogeneousPlies: bool
    KeepInvalidElems: bool
    MinElemThickness: float
    NumSmoothIterations: int
    ReferencePlaneLocation: bool
    SamcefElementType: CAE.LaminateExtrudeSetupBuilder.SamcefElementTypeEnum
    SamcefSolidShells: bool
    SandwichBottomSkinMeshOption: int
    SandwichInflation: bool
    SandwichNumCoreElementLayers: int
    SandwichTopSkinMeshOption: int
    Selection: CAE.LaminateSelectEntitiesBuilder
    SinglePlyPerLayer: bool
    SmoothNormals: bool
    SmoothRatio: float
    SnapToCutFaceTolerance: Expression


    class SamcefElementTypeEnum(enum.Enum):
        Solid = 0
        SolidShell = 1
        SolidPly = 2
    

class LaminateExtrudeSetup(NXObject):
    def __init__(self) -> None: ...
    def CreateGroups(self) -> None:
        ...


class LaminateElementFilterBuilder(Builder):
    def __init__(self) -> None: ...
    SelectAllElements: bool
    SelectElements: CAE.SelectElementsBuilder


class LaminateDynamicSimCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateDynamicSim]:
        ...
    def __init__(self, owner: CAE.LaminateManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminateDynamicSim:
        ...
    def Delete(self, dynamicSim: CAE.LaminateDynamicSim) -> None:
        ...
    def CloneDynamicSim(self, dynamicSim: CAE.LaminateDynamicSim) -> None:
        ...
    def CreateDynamicSimBuilder(self, laminateDynamicSimTag: CAE.LaminateDynamicSim) -> CAE.LaminateDynamicSimBuilder:
        ...
    def CreateDampingFactorBuilder(self, contextObjectTag: TaggedObject) -> CAE.LaminateDampingFactorBuilder:
        ...
    def Tag(self) -> Tag: ...

    Active: CAE.LaminateDynamicSim


class LaminateDynamicSimBuilder(Builder):
    def __init__(self) -> None: ...
    Name: str
    Solution: CAE.SimSolution


class LaminateDynamicSim(NXObject):
    def __init__(self) -> None: ...
    def RefreshModes(self) -> None:
        ...
    DynamicEvents: CAE.LaminateDynamicEventCollection
    ModeProperties: CAE.LaminateModePropertyCollection


class LaminateDynamicEventCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LaminateDynamicEvent]:
        ...
    def __init__(self, owner: CAE.LaminateDynamicSim) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.LaminateDynamicEvent:
        ...
    def Delete(self, dynamicEvent: CAE.LaminateDynamicEvent) -> None:
        ...
    def CloneDynamicEvent(self, dynamicEvent: CAE.LaminateDynamicEvent) -> None:
        ...
    def CreateRandomEventBuilder(self, laminateRandomEventTag: CAE.LaminateRandomEvent) -> CAE.LaminateRandomEventBuilder:
        ...
    def CreateSineEventBuilder(self, laminateSineEventTag: CAE.LaminateSineEvent) -> CAE.LaminateSineEventBuilder:
        ...
    def Tag(self) -> Tag: ...



class LaminateDynamicEventBuilder(Builder):
    def __init__(self) -> None: ...
    def GetOutputRequestObject(self) -> CAE.ModelingObjectPropertyTable:
        ...
    def SetOutputRequestObject(self, ssmo: CAE.ModelingObjectPropertyTable) -> None:
        ...
    DynamicEventName: str
    ExcitationCsys: CoordinateSystem
    ExcitationSelectedAxis: CAE.LaminateDynamicEventBuilder.ExcitationSelectedAxisEnum
    LowerBoundFrequency: float
    NastranBasicCsys: bool
    ReferenceType: CAE.LaminateDynamicEventBuilder.ReferenceTypeEnum
    UpperBoundFrequency: float
    UserFunction: TaggedObject


    class ReferenceTypeEnum(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class ExcitationSelectedAxisEnum(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

class LaminateDynamicEvent(NXObject):
    def __init__(self) -> None: ...
    def Solve(self, runInBackground: bool) -> int:
        ...
    def WriteInputFile(self) -> None:
        ...


class LaminateDrapingOrientation(NXObject):
    def __init__(self) -> None: ...


class LaminateDrapingExtensionBuilder(Builder):
    def __init__(self) -> None: ...
    Selection: CAE.LaminateSelectEntitiesBuilder


class LaminateDrapingExtension(NXObject):
    def __init__(self) -> None: ...


class LaminateDrapingDataBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitPlies(self) -> typing.List[CAE.LaminatePly]:
        ...
    CutSelection: CAE.LaminateSelectEntitiesBuilder
    DirectionCsys: CoordinateSystem
    DirectionOption: CAE.LaminateDrapingDataBuilder.DrapingDirectionType
    DrapingAbsMeshSize: Expression
    DrapingMeshRatio: float
    DrapingPath: CAE.LaminateDrapingDataBuilder.DrapingPathType
    FaceSelection: CAE.LaminateSelectEntitiesBuilder
    LockingAngle: Expression
    PrimaryVector: Direction
    ProjectionDirectionOption: CAE.LaminateDrapingDataBuilder.ProjectionDrapingDirectionType
    SecondaryVector: Direction
    SecondaryVectorChoice: CAE.LaminateDrapingDataBuilder.SecondaryVectorType
    SeedSelection: CAE.LaminateSelectEntitiesBuilder
    Solver: CAE.LaminateDrapingDataBuilder.SolverType
    StartPoint: Point
    UsingDrapingMeshSize: bool


    class SolverType(enum.Enum):
        None = 0
        Unidirectional = 1
        Woven = 2
        Imported = 3
        InheritedFromMaterial = 4
    

    class SecondaryVectorType(enum.Enum):
        Default = 0
        Specify = 1
    

    class ProjectionDrapingDirectionType(enum.Enum):
        Mov = 0
        Csys = 1
    

    class DrapingPathType(enum.Enum):
        Geodesic = 0
        SeedCurve = 1
    

    class DrapingDirectionType(enum.Enum):
        Vectors = 0
        Csys = 1
    

class LaminateDrapingData(NXObject):
    def __init__(self) -> None: ...


class LaminateDampingFactorBuilder(Builder):
    def __init__(self) -> None: ...
    DampingFactor: float


class LaminateAnnotationBuilder(Builder):
    def __init__(self) -> None: ...
    Composition: bool
    Description: bool
    GlobalPlyId: bool
    PlyOrder: CAE.LaminateAnnotationBuilder.PlyOrderEnum
    PrimaryAngle: bool
    SelectElements: SelectTaggedObjectList
    Thickness: bool
    YarnAngle: bool


    class PlyOrderEnum(enum.Enum):
        Up = 0
        Down = 1
    

    class ZoneType(enum.Enum):
        OrphanElems = 0
        OverlapElems = 1
        Regular = 2
        All = 3
    

class Laminate(CAE.PhysicalPropertyTable):
    def __init__(self) -> None: ...
    def StrengthAnalysis(self, csvFilename: str) -> None:
        ...
    def ClearLayup(self) -> None:
        ...
    def RefreshLinkedGroups(self) -> None:
        ...
    def Information(self, detailed: bool) -> None:
        ...
    def ExportInformation(self, csvFilename: str) -> None:
        ...
    def ExportLayup(self, csvFilename: str) -> None:
        ...
    def ComputeZones(self) -> None:
        ...
    def ExportZoneInformation(self, csvFilename: str) -> None:
        ...
    def ExportZonesAsGroups(self, zoneType: CAE.Laminate.ZoneType, zoneIndex: int) -> None:
        ...
    def ExportZonesAsLaminates(self, zoneType: CAE.Laminate.ZoneType, zoneIndex: int) -> None:
        ...
    def Optimize(self) -> None:
        ...
    def DefineSymPlyidRange(self, minId: int, maxId: int) -> None:
        ...
    def StiffnessMatrices(self, detailed: bool) -> None:
        ...
    def ComplianceMatrices(self, detailed: bool) -> None:
        ...
    def EquivalentProperties(self, detailed: bool) -> None:
        ...
    PlyGroups: CAE.LaminatePlyGroupCollection
    Parameters: CAE.PropertyTable
    StrengthLoadcase: CAE.PropertyTable
    UserDefinedInterLaminarFailureTheory: str
    UserDefinedPlyFailureTheory: str


class LabelRangeSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    def GetLabelRanges(self, singleLabels: int, startLabels: int, endLabels: int, increments: int) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeLabelRangeStrategy.GetLabelRanges instead.")"""
        ...
    def SetLabelRanges(self, singleLabels: int, startLabels: int, endLabels: int, increments: int) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeLabelRangeStrategy.SetLabelRanges instead.")"""
        ...


class Iteration(CAE.BaseIteration):
    def __init__(self) -> None: ...
    Label: int


class ISensorSet(NXObject):
    def __init__(self) -> None: ...
    def GetNumberOfSensors(self) -> int:
        ...
    def GetSensor(self, sensorIndex: int) -> CAE.CaeSensor:
        ...
    def DisplaySensorSet(self, show: bool) -> None:
        ...


class IPostScenarioVisualizationCustomization():
    def GetSubviewportIndex(self) -> int:
        ...
    def GetName(self) -> str:
        ...
    def Update(self) -> None:
        ...




class InterpolationEADBuilder(Builder):
    def __init__(self) -> None: ...
    def SetDof1Weights(self, dofWeights: float) -> None:
        ...
    def GetDof1Weights(self) -> float:
        ...
    def SetDof2Weights(self, dofWeights: float) -> None:
        ...
    def GetDof2Weights(self) -> float:
        ...
    def SetDof3Weights(self, dofWeights: float) -> None:
        ...
    def GetDof3Weights(self) -> float:
        ...
    def SetDof4Weights(self, dofWeights: float) -> None:
        ...
    def GetDof4Weights(self) -> float:
        ...
    def SetDof5Weights(self, dofWeights: float) -> None:
        ...
    def GetDof5Weights(self) -> float:
        ...
    def SetDof6Weights(self, dofWeights: float) -> None:
        ...
    def GetDof6Weights(self) -> float:
        ...
    def SetUmData(self, umData: int) -> None:
        ...
    def GetUmData(self) -> int:
        ...
    Elements: CAE.SelectElementsBuilder


class ImprintBuilder(Builder):
    def __init__(self) -> None: ...
    ClosestImprintOption: bool
    GeomSelection: SelectDisplayableObjectList
    ImprintType: CAE.ImprintBuilder.ImprintTypes
    ProjectionDirectionMethod: CAE.ImprintBuilder.ProjectionDirectionType
    ProjectionVector: Direction
    SearchDistance: float
    SnapDistance: Expression
    SnapToggle: bool
    SnapTolerance: float
    StitchToggle: bool
    TargetFace: SelectDisplayableObjectList


    class ProjectionDirectionType(enum.Enum):
        NaturalExtension = 0
        AlongVector = 1
        NormalToFace = 2
    

    class ImprintTypes(enum.Enum):
        FaceFaceImprint = 0
        EdgeFaceImprint = 1
    

class ImportSimulationBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSourceSimPart(self, tPart: CAE.SimPart) -> None:
        ...
    def SetPrependString(self, prependString: str) -> None:
        ...
    def SetIdOffset(self, idOffset: int) -> None:
        ...
    def SetImportAll(self, importAll: bool) -> None:
        ...
    def SetLoads(self, loads: typing.List[CAE.SimLoad]) -> None:
        ...
    def SetConstraints(self, constraints: typing.List[CAE.SimConstraint]) -> None:
        ...
    def SetSimulationObjects(self, simobjects: typing.List[CAE.SimSimulationObject]) -> None:
        ...
    def SetMaterials(self, materials: typing.List[PhysicalMaterial]) -> None:
        ...
    def SetFields(self, fields: typing.List[Fields.Field]) -> None:
        ...
    def SetModelingObjects(self, modelingobjects: typing.List[CAE.ModelingObjectPropertyTable]) -> None:
        ...
    def SetPhysicalPropertyTables(self, propertytables: typing.List[CAE.PhysicalPropertyTable]) -> None:
        ...
    def SetGroups(self, groups: typing.List[CAE.CaeGroup]) -> None:
        ...
    def SetRegions(self, regions: typing.List[CAE.CaeRegion]) -> None:
        ...
    def SetSolutions(self, solutions: typing.List[CAE.SimSolution]) -> None:
        ...
    def SetDofSets(self, dofsets: typing.List[CAE.CaeDOFSet]) -> None:
        ...
    def SetTargetFemoccs(self, selectedFemoccs: typing.List[CAE.FEModelOccurrence]) -> None:
        ...
    def SetConditionSequences(self, sequences: typing.List[CAE.SimConditionSequence]) -> None:
        ...
    def SetLayoutStates(self, layoutStates: typing.List[CAE.LayoutState]) -> None:
        ...
    def SetSelectionRecipes(self, selectionRecipes: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    def SetResultProbes(self, resProbes: typing.List[CAE.ResultProbe]) -> None:
        ...
    def SetLoadSets(self, loadSets: typing.List[CAE.SimLoadSet]) -> None:
        ...
    def SetConstraintSets(self, constraintSets: typing.List[CAE.SimConstraintSet]) -> None:
        ...
    def SetTargetSolution(self, targetSolTag: CAE.SimSolution) -> None:
        ...
    def SetSuffixString(self, suffixString: str) -> None:
        ...
    def SetExpressionConflictOption(self, option: CAE.ImportSimulationBuilder.ExpressionConflictOption) -> None:
        ...


    class ExpressionConflictOption(enum.Enum):
        KeepExisting = 0
        KeepImported = 1
        KeepBoth = 2
    

class ImportResultParameters(TaggedObject):
    def __init__(self) -> None: ...
    def GetResultFiles(self, resultFileNames: str) -> None:
        ...
    def SetResultFiles(self, resultFileNames: str) -> None:
        ...
    InferResultUnit: bool
    Parent: CAE.CaePart
    ResultName: str
    SyncWithParent: bool
    UnitSystem: CAE.ResultUnitSystem
    UpdateNavigator: bool


class ImportedSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSolutionName(self, solutionname: str) -> None:
        ...
    def SetResultFile(self, resultfile: str) -> None:
        ...
    def SetUnitsSystem(self, unitsSystem: CAE.Result.ResultBasicUnit) -> None:
        ...
    def SetPreGroup(self, pregroup: bool) -> None:
        ...


class ImportedSimInterfaceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.ImportedSimInterface]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateImportedSimulationInterface(self, simif: CAE.SimulationInterface, expconfop: CAE.ImportedSimInterfaceCollection.ExpressionConflictOption) -> CAE.ImportedSimInterface:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.ImportedSimInterface:
        ...
    def DeleteSimInterface(self, importedSimIF: CAE.ImportedSimInterface) -> None:
        ...
    def LoadSourceSim(self, importedSimIF: CAE.ImportedSimInterface) -> None:
        ...
    def Tag(self) -> Tag: ...



    class ExpressionConflictOption(enum.Enum):
        KeepExisting = 0
        KeepImported = 1
        KeepBoth = 2
    

class ImportedSimInterface(NXObject):
    def __init__(self) -> None: ...
    def AttachFemComponents(self, femOccs: typing.List[CAE.FEModelOccurrence]) -> None:
        ...
    def GetSimif(self) -> CAE.SimulationInterface:
        ...
    def GetExpconfop(self) -> CAE.ImportedSimInterfaceCollection.ExpressionConflictOption:
        ...
    def GetFemoccs(self) -> typing.List[CAE.FEModelOccurrence]:
        ...
    def SetFemoccs(self, femoccs: typing.List[CAE.FEModelOccurrence]) -> None:
        ...
    def GetUpdatepending(self) -> bool:
        ...
    def UpdateSimInterface(self) -> None:
        ...


class ImportedResult(CAE.Result):
    def __init__(self) -> None: ...
    def GetFiletype(self) -> CAE.Result.Filetype:
        ...
    def GetFilename(self) -> str:
        ...


class ImmersedBoundaryMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    AutoResetOption: bool
    ElementType: CAE.ElementTypeBuilder
    FeatureSelectionList: SelectDisplayableObjectList
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList


    class JaImmersedBoundaryMeshBuilderSubdivisionType(enum.Enum):
        One = 0
        Two = 1
        Three = 2
        Four = 3
        Five = 4
        Six = 5
        Seven = 6
        Eight = 7
    

class IMeshManager(TaggedObject):
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> TaggedObject:
        ...
    def GetMeshCollectors(self) -> typing.List[CAE.IMeshCollector]:
        ...
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...
    def GetNodeStatus(self) -> CAE.IMeshManager.StatusInfo:
        ...
    def GetElementStatus(self) -> CAE.IMeshManager.StatusInfo:
        ...


    class IMeshManagerStatusInfo():
        TotalNum: int
        LowLabel: int
        HighLabel: int
        def ToString(self) -> str:
            ...
        def __init__(self, TotalNum: int, LowLabel: int, HighLabel: int) -> None: ...
    

class IMeshCollector(NXObject):
    def __init__(self) -> None: ...
    def GetMeshes(self) -> typing.List[CAE.Mesh]:
        ...
    def GetMeshDisplayDefaults(self) -> CAE.MeshCollectorDisplayDefaults:
        ...
    CollectorNeutralType: str
    CollectorType: str
    ElementPropertyTable: CAE.PropertyTable


class IHierarchicalFEModel():
    def GetChildren(self) -> typing.List[CAE.FEModelOccurrence]:
        ...
    Parent: CAE.IFEModel


class IFormatHandler():
    DisplayName: str
    Name: str


class IFolder():
    def GetParent(self) -> CAE.IFolder:
        ...
    def GetChildren(self) -> typing.List[CAE.IFolder]:
        ...
    def GetMembers(self) -> typing.List[NXObject]:
        ...


class IFEModel(NXObject):
    def __init__(self) -> None: ...
    ConnectionsContainer: CAE.Connections.Folder
    FeelementLabelMap: CAE.FEElementLabelMap
    FenodeLabelMap: CAE.FENodeLabelMap
    MeshManager: CAE.IMeshManager


class IExportableFEEntity():
    def GetSolverCardSyntax(self) -> str:
        ...


class IBeamSectionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetUserDefinedStressRecoveryPoints(self, points: typing.List[Point2d]) -> None:
        ...
    def GetUserDefinedStressRecoveryPoints(self, points: typing.List[Point2d]) -> None:
        ...
    PropertyTable: CAE.PropertyTable
    SectionName: str


class IApplicationObjectManager(NXObject):
    def __init__(self) -> None: ...


class IAncillaryDisplayableEntity():
    def AncillaryDisplay(self) -> None:
        ...


class HybridMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class HotspotRecipePost(CAE.HotspotRecipe):
    def __init__(self) -> None: ...


class HotspotRecipeManager(NXObject):
    def __init__(self) -> None: ...
    def GetHotspotRecipes(self, pHotspotRecipes: typing.List[CAE.HotspotRecipe]) -> None:
        ...


class HotspotRecipeBuilder(Builder):
    def __init__(self) -> None: ...
    def GetResultQuantity(self) -> str:
        ...
    def SetResultQuantity(self, resultQuantity: str) -> None:
        ...
    def GetOffsetForMinMax(self) -> float:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.HotspotRecipeBuilder.GetOffsetValueForMinMax instead.")"""
        ...
    def SetOffsetForMinMax(self, offsetByValue: float) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.HotspotRecipeBuilder.SetOffsetValueForMinMax instead.")"""
        ...
    def GetEntityObjects(self) -> typing.List[TaggedObject]:
        ...
    def SetEntityObjects(self, entityObjs: typing.List[TaggedObject]) -> None:
        ...
    def InitFromRecipe(self, recipe: CAE.HotspotRecipe) -> None:
        ...
    def GetResultQuantityType(self) -> CAE.Result.Quantity:
        ...
    def SetResultQuantityType(self, resQuan: CAE.Result.Quantity) -> None:
        ...
    def GetThresholdValue(self) -> CAE.HotspotRecipeBuilder.UnitValue:
        ...
    def SetThresholdValue(self, seedValue: CAE.HotspotRecipeBuilder.UnitValue) -> None:
        ...
    def GetNeighbourOffset(self) -> CAE.HotspotRecipeBuilder.UnitValue:
        ...
    def SetNeighbourOffset(self, neighbourvalue: CAE.HotspotRecipeBuilder.UnitValue) -> None:
        ...
    def GetSortBelowParamVal(self) -> CAE.HotspotRecipeBuilder.UnitValue:
        ...
    def SetSortBelowParamVal(self, belowValue: CAE.HotspotRecipeBuilder.UnitValue) -> None:
        ...
    def GetSortAboveParamVal(self) -> CAE.HotspotRecipeBuilder.UnitValue:
        ...
    def SetSortAboveParamVal(self, aboveValue: CAE.HotspotRecipeBuilder.UnitValue) -> None:
        ...
    def GetOffsetValueForMinMax(self) -> CAE.HotspotRecipeBuilder.UnitValue:
        ...
    def SetOffsetValueForMinMax(self, offsetValue: CAE.HotspotRecipeBuilder.UnitValue) -> None:
        ...
    DataTypeFilter: CAE.Result.DataType
    IsSortRangeAboveRes: bool
    IsSortRangeBelowRes: bool
    IsSortSelectedEntities: bool
    MaxNumRegions: int
    MinSpanOfRegion: int
    NeighborOffset: float
    OffsetTypeMinMax: CAE.HotspotRecipeBuilder.EnumOffsetTypeMinMax
    RecipeName: str
    ResultComponent: CAE.Result.Component
    ResultLocation: CAE.Result.Location
    SortAboveParamVal: float
    SortBelowParamVal: float
    SortMethod: CAE.HotspotRecipeBuilder.EnumSortingMethod
    SpanOfRegion: int
    ThresholdType: CAE.HotspotRecipeBuilder.EnumThresholdType
    ThresholdValue: float


    class HotspotRecipeBuilderUnitValue():
        Value: float
        Unit: Unit
        def ToString(self) -> str:
            ...
        def __init__(self, Value: float, Unit: Unit) -> None: ...
    

    class EnumThresholdType(enum.Enum):
        MaxOffset = 0
        MinOffset = 1
        MaxFactor = 2
        MinFactor = 3
    

    class EnumSortingMethod(enum.Enum):
        Threshold = 0
        Range = 1
        MinimumResult = 2
        MaximumResults = 3
    

    class EnumOffsetTypeMinMax(enum.Enum):
        ByValueOffset = 0
        ByPercentageOffset = 1
        ByNumberofEntities = 2
    

    class HotspotRecipeBuilder_UnitValue():
        value: float
        unit: Tag
    

class HotspotRecipe(NXObject):
    def __init__(self) -> None: ...
    def ResolveHotspotRecipe(self, pvid: int) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.HotspotRecipe.ResolveHotspotRecipeNew instead.")"""
        ...
    def CreateGroup(self, pvid: int) -> None:
        ...
    def Show(self, pvid: int) -> None:
        ...
    def ShowOnly(self, pvid: int) -> None:
        ...
    def Hide(self, pvid: int) -> None:
        ...
    def CreateGroupOfSeed(self, pvid: int) -> None:
        ...
    def PrintInformation(self, pvid: int) -> None:
        ...
    def ResolveHotspotRecipeNew(self, pvid: int, pHotspots: typing.List[CAE.Hotspot]) -> None:
        ...


class Hotspot(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def Show(self, postViewId: int) -> None:
        ...
    def ShowOnly(self, postViewId: int) -> None:
        ...
    def Hide(self, postViewId: int) -> None:
        ...
    def CreateGroup(self, postViewId: int) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.Hotspot.CreateGroup1 instead.")"""
        ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    def CreateGroupOfSeed(self, postViewId: int) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.Hotspot.CreateGroupOfSeed1 instead.")"""
        ...
    def PrintInformation(self, recipe: CAE.HotspotRecipe) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.Hotspot.PunchInformation instead.")"""
        ...
    def CreateGroup1(self, postViewId: int, recipe: CAE.HotspotRecipe) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.Hotspot.CreateFEGroup instead.")"""
        ...
    def CreateGroupOfSeed1(self, postViewId: int, recipe: CAE.HotspotRecipe) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.Hotspot.CreateFEGroupOfSeed instead.")"""
        ...
    def PunchInformation(self) -> None:
        ...
    def CreateFEGroup(self) -> None:
        ...
    def CreateFEGroupOfSeed(self) -> None:
        ...
    def AddToDisplay(self) -> None:
        ...
    def DisplayOnly(self) -> None:
        ...
    def HideFromDisplay(self) -> None:
        ...


class HorizontalMeshSlicing(CAE.MeshSlicingData):
    def __init__(self) -> None: ...
    def GetAltitudes(self, altitudes: float) -> None:
        ...
    def SetAltitudes(self, altitudes: float) -> None:
        ...


class HoleElementEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementEdges(self) -> typing.List[CAE.SetObject]:
        """[Obsolete("Deprecated in NX11.0.2.  Use NXOpen.CAE.HoleElementEdgeMethod.GetFeElemEdges.")"""
        ...
    def GetFeElemEdges(self) -> typing.List[CAE.FEElemEdge]:
        ...


class GroupNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class GroupMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEntities(self) -> typing.List[TaggedObject]:
        ...


class GroupFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class GroupElemMethodElemOption(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class ElemOption(enum.Enum):
        ElemAll = 0
        Elem0d = 1
        Elem1d = 2
        Elem2d = 3
        Elem3d = 4
        Elemface2d = 5
        Elemedge1d = 6
    

class GroupElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class GroupElemFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementFaces(self) -> typing.List[CAE.FEElemFace]:
        ...


class GroupElemEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementEdges(self) -> typing.List[CAE.FEElemEdge]:
        ...


class GroupEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEdges(self) -> typing.List[CAE.CAEEdge]:
        ...


class GroupByBoundaryBuilder(Builder):
    def __init__(self) -> None: ...
    def FindVolume(self) -> None:
        ...
    ClosedVolumeToggle: bool
    CreateTwoGroups: bool
    NormalDirectionFlipped: bool
    SeedElement: CAE.FEElement
    SelectElementsGroupOne: CAE.SelectElementsBuilder
    SelectElementsGroupTwo: CAE.SelectElementsBuilder
    SelectRemovedGroup: CAE.SelectElementsBuilder


class GRMSearch(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def FindReferencers(self, fileSpec: str, useCache: bool, referencerNames: str) -> None:
        ...
    def FindCachedReferencers(self, fileSpec: str, referencerNames: str) -> None:
        ...
    def ClearCache(self) -> None:
        ...


class GraphRecipe(CAE.ProbeOutputRecipe):
    def __init__(self) -> None: ...
    def GetXaxisoption(self) -> CAE.GraphRecipe.XAxisoption:
        ...
    def SetXaxisoption(self, xaxis: CAE.GraphRecipe.XAxisoption) -> None:
        ...
    def GetDirection(self) -> Direction:
        ...
    def SetDirection(self, direction: Direction) -> None:
        ...
    def GetCsystype(self) -> CAE.GraphRecipe.CsysType:
        ...
    def SetCsystype(self, csystype: CAE.GraphRecipe.CsysType) -> None:
        ...
    def GetCsys(self) -> CoordinateSystem:
        ...
    def SetCsys(self, csys: CoordinateSystem) -> None:
        ...
    def GetCsysaxis(self) -> CAE.GraphRecipe.CsysAxis:
        ...
    def SetCsysaxis(self, axis: CAE.GraphRecipe.CsysAxis) -> None:
        ...
    def GetFormula(self) -> str:
        ...
    def SetFormula(self, formula: str) -> None:
        ...
    def GetUnit(self) -> Unit:
        ...
    def SetUnit(self, unit: Unit) -> None:
        ...


    class XAxisoption(enum.Enum):
        Pathlength = 0
        Lengthalongdirection = 1
        Csysaxis = 2
        Iteration = 3
        Formula = 4
        Rpm = 5
    

    class CsysType(enum.Enum):
        GlobalCyclicAnalysis = 0
        Global = 1
        Cartesian = 2
        Cylindrical = 3
        Spherical = 4
    

    class CsysAxis(enum.Enum):
        First = 0
        Second = 1
        Third = 2
    

class GraphFromResultProbeBuilder(Builder):
    def __init__(self) -> None: ...
    def SetWindowIndex(self, windowIndex: int) -> None:
        ...
    def SetViewIndex(self, viewIndex: int) -> None:
        ...
    def SetPlotType(self, plotType: CAE.GraphFromResultProbeBuilder.PlotType) -> None:
        ...
    def SetResultProbes(self, resultProbes: typing.List[CAE.ResultProbe]) -> None:
        ...
    def GetGraphs(self) -> typing.List[CAE.PostGraph]:
        ...


    class PlotType(enum.Enum):
        Xy = 0
        XYInStack = 1
        Xyz = 2
    

class GlobalLayupImportFromPptBuilder(Builder):
    def __init__(self) -> None: ...
    LamPptSelect: int


class GlobalAeroCsysBuilder(Builder):
    def __init__(self) -> None: ...
    Csys: CoordinateSystem


class GeometryRecipeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.GeometryRecipe]:
        ...
    def __init__(self, owner: CAE.PolygonGeometryManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFreezeGeometryBuilder(self, recipe: CAE.FreezeGeometryRecipe) -> CAE.FreezeGeometryBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.GeometryRecipe:
        ...
    def Tag(self) -> Tag: ...



class GeometryRecipe(NXObject):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...


class GeometryQueryHelper(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...


class GeneralGeometryIdealizedBeamSectionBuilder(CAE.StandardBeamSectionBuilder):
    def __init__(self) -> None: ...


class GeneralGeometryBeamSectionBuilder(CAE.IBeamSectionBuilder):
    def __init__(self) -> None: ...
    DescriptorName: str
    Sketch: CAE.SketchCurves


class GeneralGeometryBeamSection(CAE.BeamSection):
    def __init__(self) -> None: ...


class GapEADBuilder(Builder):
    def __init__(self) -> None: ...
    Elements: CAE.SelectElementsBuilder
    OriCsystem: CoordinateSystem
    OriDirr: Direction
    OriMethod: CAE.GapEADBuilder.OrientationMethod
    OriNode: CAE.SelectFENodeList
    OrientationState: CAE.GapEADBuilder.State
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.GapEADBuilder.State


    class State(enum.Enum):
        Apply = 0
        Clear = 1
        Ignore = 2
    

    class OrientationMethod(enum.Enum):
        Vector = 0
        Csystem = 1
        Node = 2
    

class FunctionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Function]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateFunctionBuilder(self, function: CAE.Function) -> CAE.FunctionBuilder:
        ...
    def Copy(self, sourceFunction: CAE.Function, destinationFunctionName: str) -> CAE.Function:
        ...
    def Delete(self, deleteFunction: CAE.Function) -> None:
        ...
    def FindObject(self, name: str) -> CAE.Function:
        ...
    def Tag(self) -> Tag: ...



class FunctionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTypes(self, functionType: CAE.Function.Type, macroType: CAE.XyFunctionMacroType, generalType: CAE.XyFunctionGeneralType) -> None:
        ...
    def GetTypes(self, functionType: CAE.Function.Type, macroType: CAE.XyFunctionMacroType, generalType: CAE.XyFunctionGeneralType) -> None:
        ...
    def SetUnits(self, xUnit: CAE.XyFunctionUnit, yUnit: CAE.XyFunctionUnit, frfUnit: CAE.XyFunctionUnit) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use CAE.FunctionBuilder.AbscissaUnit, CAE.FunctionBuilder.OrdinateUnit, CAE.FunctionBuilder.OrdinateSecondNumeratorUnit and CAE.FunctionBuilder.OrdinateDenominatorUnit instead.")"""
        ...
    def GetUnits(self, xUnit: CAE.XyFunctionUnit, yUnit: CAE.XyFunctionUnit, frfUnit: CAE.XyFunctionUnit) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use CAE.FunctionBuilder.AbscissaUnit, CAE.FunctionBuilder.OrdinateUnit, CAE.FunctionBuilder.OrdinateSecondNumeratorUnit and CAE.FunctionBuilder.OrdinateDenominatorUnit instead.")"""
        ...
    def SetDefinitions(self, definitions: str) -> None:
        ...
    def GetDefinitions(self) -> str:
        ...
    def SetReferencedObjects(self, objects: typing.List[CAE.Function]) -> None:
        ...
    def GetReferencedObjects(self) -> typing.List[CAE.Function]:
        ...
    def SetMathPlotData(self, dataCount: int, xMinimum: float, xIncrement: float) -> None:
        ...
    def GetMathPlotData(self, dataCount: int, xMinimum: float, xIncrement: float) -> None:
        ...
    def SetTableData(self, recordIndex: int, recordName: str, recordTimestamp: str, interpolateMethod: CAE.Function.InterpolationMethod) -> None:
        ...
    def GetTableData(self, recordIndex: int, recordName: str, recordTimestamp: str, interpolateMethod: CAE.Function.InterpolationMethod) -> None:
        ...
    AbscissaUnit: CAE.XyFunctionUnit
    InitialEstimateValue: float
    Name: str
    OrdinateDenominatorUnit: CAE.XyFunctionUnit
    OrdinateSecondNumeratorUnit: CAE.XyFunctionUnit
    OrdinateUnit: CAE.XyFunctionUnit


class Function(NXObject):
    def __init__(self) -> None: ...


    class Type(enum.Enum):
        Math = 0
        Table = 1
    

    class InterpolationMethod(enum.Enum):
        Cubic = 0
        Akima = 1
        Linear = 2
    

class FrfSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.FrfSet]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self, pFrfSet: CAE.FrfSet) -> CAE.FrfSetBuilder:
        ...
    def Find(self, name: str) -> CAE.FrfSet:
        ...
    def Delete(self, frfSetTag: CAE.FrfSet) -> None:
        ...
    def Tag(self) -> Tag: ...



class FrfSetBuilder(CAE.AlternateFemRepresentationSourceBuilder):
    def __init__(self) -> None: ...
    def GetAvailableFrfsubsets(self) -> str:
        ...
    def DeselectFrfsubsets(self, frfSubSetNames: str) -> None:
        ...


class FrfSet(CAE.AlternateFemRepresentationSource):
    def __init__(self) -> None: ...
    def GetNumberOfFrfs(self) -> int:
        ...
    def GetFrfStatus(self, inputNode: int, inputComponent: CAE.FrfSet.NodeComponent, outputNode: int, outputComponent: CAE.FrfSet.NodeComponent, excitation: CAE.FrfSet.Measure, response: CAE.FrfSet.Measure) -> bool:
        ...
    def SetFrfStatus(self, inputNode: int, inputComponent: CAE.FrfSet.NodeComponent, outputNode: int, outputComponent: CAE.FrfSet.NodeComponent, excitation: CAE.FrfSet.Measure, response: CAE.FrfSet.Measure, status: bool) -> None:
        ...


    class NodeComponent(enum.Enum):
        S = 0
        X = 1
        Y = 2
        Z = 3
        Rx = 4
        Ry = 5
        Rz = 6
    

    class Measure(enum.Enum):
        Force = 0
        Moment = 1
        Displacement = 2
        Rotation = 3
        Velocity = 4
        Angularvelocity = 5
        Acceleration = 6
        Angularacceleration = 7
        Pressure = 8
        Volumeacceleration = 9
        Volumevelocity = 10
        Volumedisplacement = 11
        Acupoleamplitude = 12
        Power = 13
    

class FrfPairingFilterBuilder(Builder):
    def __init__(self) -> None: ...
    FilterName: str
    FilterOperator: CAE.FrfPairingFilterBuilder.FilterOperatorType
    FilterString: str
    FilterType: CAE.FrfPairingFilterBuilder.NodeType
    NodeLabelLookupSource: CAE.FrfPairingFilterBuilder.LookupSource
    ToggleS: bool
    ToggleX: bool
    ToggleY: bool
    ToggleZ: bool


    class NodeType(enum.Enum):
        Output = 0
        Input = 1
    

    class LookupSource(enum.Enum):
        Ref = 0
        Work = 1
    

    class FilterOperatorType(enum.Enum):
        Equal = 0
        Contains = 1
        LessOrEqualThan = 2
        GreaterOrEqualThan = 3
    

class FrfPairingFilter(NXObject):
    def __init__(self) -> None: ...
    def SetActive(self, active: bool) -> None:
        ...


class FreezeGeometryRecipe(CAE.GeometryRecipe):
    def __init__(self) -> None: ...


class FreezeGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    FaceSelect: SelectTaggedObjectList


class FreeFormMeshSlicing(CAE.MeshSlicingData):
    def __init__(self) -> None: ...
    def GetSurfaces(self, sufaces: typing.List[Facet.FacetedBody]) -> None:
        ...
    def SetSurfaces(self, surfaces: typing.List[Facet.FacetedBody]) -> None:
        ...
    def GetMaximumDistanceToMeshBoundaries(self) -> float:
        ...
    def SetMaximumDistanceToMeshBoundaries(self, maximumDistanceToMeshBoundaries: float) -> None:
        ...


class FreeElemFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFeElemFaces(self) -> typing.List[CAE.FEElemFace]:
        ...


class FreeElemEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFeElemEdges(self) -> typing.List[CAE.FEElemEdge]:
        ...


class FreeBodyResultsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetIteration(self) -> CAE.BaseIteration:
        ...
    def SetIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    def GetPostview(self) -> int:
        ...
    def SetPostview(self, postviewId: int) -> None:
        ...
    def GetElements(self) -> int:
        ...
    def SetElements(self, elements: int) -> None:
        ...
    def GetNodes(self) -> int:
        ...
    def SetNodes(self, nodes: int) -> None:
        ...
    def GetLocationMethod(self) -> CAE.FreeBodyResultsBuilder.LocationMethod:
        ...
    def SetLocationMethod(self, method: CAE.FreeBodyResultsBuilder.LocationMethod) -> None:
        ...
    def GetLocationId(self) -> int:
        ...
    def SetLocationId(self, nodeId: int) -> None:
        ...
    def GetLocationCoords(self) -> Point3d:
        ...
    def SetLocationCoords(self, coordinates: Point3d) -> None:
        ...
    def GetLocationCsys(self) -> int:
        ...
    def SetLocationCsys(self, id: int) -> None:
        ...
    def GetLocationCsysSource(self) -> CAE.Result.CoordinateSystemSource:
        ...
    def SetLocationCsysSource(self, source: CAE.Result.CoordinateSystemSource) -> None:
        ...
    def GetReferenceCsys(self) -> CAE.Result.CoordinateSystem:
        ...
    def SetReferenceCsys(self, csys: CAE.Result.CoordinateSystem) -> None:
        ...
    def GetSelectedReferenceCsys(self) -> int:
        ...
    def SetSelectedReferenceCsys(self, id: int) -> None:
        ...
    def GetSelectedReferenceCsysSource(self) -> CAE.Result.CoordinateSystemSource:
        ...
    def SetSelectedReferenceCsysSource(self, source: CAE.Result.CoordinateSystemSource) -> None:
        ...
    def GetPrintOutput(self) -> bool:
        ...
    def SetPrintOutput(self, print: bool) -> None:
        ...
    def GetDisplayForce(self) -> bool:
        ...
    def SetDisplayForce(self, display: bool) -> None:
        ...
    def GetDisplayMoment(self) -> bool:
        ...
    def SetDisplayMoment(self, display: bool) -> None:
        ...
    def GetForceVectorDisplay(self) -> CAE.FreeBodyResultsBuilder.VectorDisplay:
        ...
    def SetForceVectorDisplay(self, vectorDisplay: CAE.FreeBodyResultsBuilder.VectorDisplay) -> None:
        ...
    def GetMomentVectorDisplay(self) -> CAE.FreeBodyResultsBuilder.VectorDisplay:
        ...
    def SetMomentVectorDisplay(self, vectorDisplay: CAE.FreeBodyResultsBuilder.VectorDisplay) -> None:
        ...
    def GetForceColor(self) -> NXColor:
        ...
    def SetForceColor(self, display: NXColor) -> None:
        ...
    def GetMomentColor(self) -> NXColor:
        ...
    def SetMomentColor(self, color: NXColor) -> None:
        ...
    def GetOutputUnits(self) -> CAE.FreeBodyResultsBuilder.OutputUnits:
        ...
    def SetOutputUnits(self, units: CAE.FreeBodyResultsBuilder.OutputUnits) -> None:
        ...


    class VectorDisplay(enum.Enum):
        Magnitude = 0
        Components = 1
    

    class OutputUnits(enum.Enum):
        Default = 0
        MilliNewton = 1
        MilliMillinewton = 2
        MeterNewton = 3
        FtPoundForce = 4
        InPoundForce = 5
    

    class LocationMethod(enum.Enum):
        Id = 0
        Coords = 1
        Csysorigin = 2
    

class FormatHandlerCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.IFormatHandler]:
        ...
    def __init__(self, owner: CAE.DataSourceBuilder) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.IFormatHandler:
        ...
    def Tag(self) -> Tag: ...



class FolderType(enum.Enum):
    New = 0
    Existing = 1


class FluidDomainRecipe(NXObject):
    def __init__(self) -> None: ...
    def SetName(self, name: str) -> None:
        ...
    def GetName(self) -> str:
        ...
    def AddLocalResolutionConstraint(self, localResolutionConstraint: CAE.CfdLocalResolutionConstraint) -> None:
        ...
    def RemoveLocalResolutionConstraint(self, localResolutionConstraint: CAE.CfdLocalResolutionConstraint) -> None:
        ...
    def AddContactPreventionConstraint(self, contactPreventionConstraint: CAE.CfdContactPreventionConstraint) -> None:
        ...
    def RemoveContactPreventionConstraint(self, contactPreventionConstraint: CAE.CfdContactPreventionConstraint) -> None:
        ...
    def AddAutoRefinementConstraint(self, autoRefinementConstraint: CAE.CfdAutoRefinementConstraint) -> None:
        ...
    def RemoveAutoRefinementConstraint(self, autoRefinementConstraint: CAE.CfdAutoRefinementConstraint) -> None:
        ...
    def GetFluidBody(self) -> CAE.CAEBody:
        ...
    def GetFluidBodies(self, fluidBodies: typing.List[CAE.CAEBody]) -> None:
        ...
    def SyncFaceNamesAndAttributes(self) -> None:
        ...


class FluidDomainCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.FluidDomainRecipe]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.FluidDomainRecipe:
        ...
    def Find(self, journalIdentifier: str) -> CAE.FluidDomainRecipe:
        ...
    def CreateBuilder(self, recipe: CAE.FluidDomainRecipe) -> CAE.FluidDomainBuilder:
        ...
    def UpdateRecipe(self, recipe: CAE.FluidDomainRecipe) -> None:
        ...
    def UpdateAll(self) -> None:
        ...
    def DeleteRecipe(self, recipe: CAE.FluidDomainRecipe) -> None:
        ...
    def FindRecipeFromFluidBody(self, fluidBody: CAE.CAEBody) -> CAE.FluidDomainRecipe:
        ...
    def Tag(self) -> Tag: ...



class FluidDomainBuilder(Builder):
    def __init__(self) -> None: ...
    def SetCavityPoint(self, points: Point3d) -> None:
        ...
    def SetCavityPoints(self, points: typing.List[Point3d]) -> None:
        ...
    def AutoSizeButton(self) -> None:
        ...
    def CommitFluidDomain(self) -> CAE.CAEBody:
        ...
    AcousticWrapEnabled: bool
    AttemptQuadOnly: bool
    ClosingSize: Expression
    ColinearThreshold: float
    CollectorName: str
    CoplanarThreshold: float
    CurvatureBasedElementSizeLevel: float
    DetectFeatureEdges: bool
    DoCoplanarDecimation: bool
    DoExportMeshToSolver: bool
    DoSharpFeatureEdge: bool
    DoSharpFeaturePlaneIntersection: bool
    ElementSize: Expression
    ElementType: CAE.ElementTypeBuilder
    FaceNormal: Direction
    FaceSelection: CAE.SelectCAEFace
    FeatureAngle: Expression
    GeometrySelection: SelectTaggedObjectList
    InteriorExteriorType: CAE.FluidDomainBuilder.IntExtType
    InteriorPoint: Point
    MaxSubdivisionType: CAE.FluidDomainBuilder.SubdivisionType
    OutputType: CAE.FluidDomainBuilder.OutputOptionsType
    Resolution: Expression
    SmoothingLevel: float
    SnapToSourceBoundaries: bool
    SpecifyElementSize: bool
    UseAutomaticRefinement: bool


    class SubdivisionType(enum.Enum):
        One = 0
        Two = 1
        Three = 2
        Four = 3
        Five = 4
        Six = 5
        Seven = 6
        Eight = 7
    

    class OutputOptionsType(enum.Enum):
        BodyOnly = 0
        BodyandMesh = 1
        MeshOnly = 2
    

    class IntExtType(enum.Enum):
        FaceAndNormalVector = 0
        Point = 1
        CavityPoints = 2
        FromExterior = 3
    

class FlatPatternsBuilder(Builder):
    def __init__(self) -> None: ...
    def ExportButton(self) -> None:
        ...
    Filename: str
    IndividualExport: bool
    PlySelect: int


class FilterNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class FilterFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class FilterElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElems(self) -> typing.List[CAE.FEElement]:
        ...


class FilterEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEdges(self) -> typing.List[CAE.CAEEdge]:
        ...


class FilterBodyMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetBodies(self) -> typing.List[CAE.CAEBody]:
        ...


class FilletFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class FieldRecipe(CAE.ProbeOutputRecipe):
    def __init__(self) -> None: ...
    def GetIndependentVars(self) -> typing.List[Fields.FieldVariable]:
        ...
    def SetIndependentVars(self, inputVars: typing.List[Fields.FieldVariable]) -> None:
        ...
    def GetDependentVar(self) -> Fields.FieldVariable:
        ...
    def SetDependentVar(self, inputVar: Fields.FieldVariable) -> None:
        ...
    def GetSpatialMap(self) -> Fields.SpatialMap:
        ...
    def SetSpatialMap(self, spatialMap: Fields.SpatialMap) -> None:
        ...
    def GetDuplicateValueOption(self) -> Fields.FieldTable.DuplicateValueOption:
        ...
    def SetDuplicateValueOption(self, duplicate: Fields.FieldTable.DuplicateValueOption) -> None:
        ...
    def GetLengthDirection(self) -> Direction:
        ...
    def SetLengthDirection(self, direction: Direction) -> None:
        ...


class FENodeLabelMap(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetNode(self, nodelabel: int) -> CAE.FENode:
        ...
    def AskNextNodeLabel(self, nodelabel: int) -> int:
        ...
    def AskNodeLabelUsed(self, nodelabel: int) -> bool:
        ...
    def FreeResource(self) -> None:
        ...
    NumNodes: int


class FENode(TaggedObject):
    def __init__(self) -> None: ...
    def IsScalarPoint(self) -> bool:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    Coordinates: Point3d
    DisplacementCsys: CoordinateSystem
    Label: int
    ReferenceCsys: CoordinateSystem
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


class FemSynchronizeOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetAllSynchronizeFlags(self, synchronizeOption: bool) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    SynchronizeArcsFlag: bool
    SynchronizeConicsFlag: bool
    SynchronizeCoordinateSystemFlag: bool
    SynchronizeCreateMeshPointsFlag: bool
    SynchronizeDplaneFlag: bool
    SynchronizeLinesFlag: bool
    SynchronizePointsFlag: bool
    SynchronizeSketchCurvesFlag: bool
    SynchronizeSplinesFlag: bool


class FemSignalProcessingSignalAttributes(NXObject):
    def __init__(self) -> None: ...
    def GetApplication(self) -> Fields.IApplication:
        ...
    def DeleteApplicationData(self) -> None:
        ...
    def CopyToField(self, field: Fields.Field) -> None:
        ...
    AcousticalWeighting: CAE.FemSignalProcessingSignalAttributes.AcousticalWeightings
    AmplitudeCorrectionFactor: float
    CorrectionMode: CAE.FemSignalProcessingSignalAttributes.CorrectionModes
    EnergyCorrectionFactor: float
    SpectrumScaling: CAE.FemSignalProcessingSignalAttributes.SpectrumScalings


    class SpectrumScalings(enum.Enum):
        Unknown = 0
        Peak = 1
        Rms = 2
    

    class CorrectionModes(enum.Enum):
        Unknown = 0
        Energy = 1
        Amplitude = 2
    

    class AcousticalWeightings(enum.Enum):
        Unknown = 0
        None = 1
        A = 2
        B = 3
        C = 4
        D = 5
        Ab = 6
        Bc = 7
    

class FemSignalProcessingApplication(Fields.IApplication):
    def __init__(self) -> None: ...
    def CreateSignalAttributes(self, defaultVisualizationSpectrumScaling: CAE.FemSignalProcessingSignalAttributes.SpectrumScalings, defaultVisualizationCorrectionMode: CAE.FemSignalProcessingSignalAttributes.CorrectionModes, amplitudeCorrectionFactor: float, energyCorrectionFactor: float, acousticalWeighting: CAE.FemSignalProcessingSignalAttributes.AcousticalWeightings) -> CAE.FemSignalProcessingSignalAttributes:
        ...


class FemPart(CAE.BaseFemPart):
    def __init__(self) -> None: ...
    def FinalizeCreation(self, creationOptions: CAE.FemCreationOptions) -> None:
        ...
    def NewFemCreationOptions(self) -> CAE.FemCreationOptions:
        ...
    def CreateEdgeSticherBuilder(self) -> CAE.EdgeSticherBuilder:
        ...
    def CreateUnStitchEdgeBuilder(self) -> CAE.UnStitchEdgeBuilder:
        ...
    def NewFemSynchronizeOptions(self) -> CAE.FemSynchronizeOptions:
        ...
    def GetGeometryData(self, useBodiesOption: CAE.FemPart.UseBodiesOption, listOfBodies: typing.List[Body], psyncData: CAE.FemSynchronizeOptions) -> None:
        ...
    def SetGeometryData(self, useBodiesOption: CAE.FemPart.UseBodiesOption, listOfBodies: typing.List[Body], psyncData: CAE.FemSynchronizeOptions) -> None:
        ...
    def SetMeshPreferences(self, tinyEdgeColor: NXColor, snapTolerance: float, projectNodesToCadOption: int, projectionTolerance: float, refineTessellation: int, maxNumOfElemOption: int, maxNumOfElem: int, minNumOfElemOption: int, minNumOfElem: int) -> None:
        ...
    def GetMeshPreferences(self, tinyEdgeColor: NXColor, snapTolerance: float, projectNodesToCadOption: int, projectionTolerance: float, refineTessellation: int, maxNumOfElemOption: int, maxNumOfElem: int, minNumOfElemOption: int, minNumOfElem: int) -> None:
        ...
    def BodyRecreateNew(self, body: Body) -> None:
        ...
    def BodiesRecreateNew(self, listOfBodies: typing.List[Body]) -> None:
        ...
    def PolygonBodyDelete(self, body: CAE.CAEBody) -> None:
        ...
    def BodyRecreateUpdate(self, body: Body) -> None:
        ...
    def BodiesRecreateUpdate(self, listOfBodies: typing.List[Body]) -> None:
        ...
    def CreatePolygonBody(self, body: Body) -> None:
        ...
    def SetAssociatedCadAsWork(self, cadPart: Part) -> None:
        ...
    def SetFemAsWork(self) -> None:
        ...
    def MeshDebugOption(self, printFlag: bool) -> None:
        ...
    def CreateMeshingPreferencesBuilder(self) -> CAE.MeshingPreferencesBuilder:
        ...
    CadModeling: CAE.CADModeling
    MeshPoints: CAE.MeshPointCollection
    PolygonGeometryMgr: CAE.PolygonGeometryManager
    AssociatedCadPart: Part
    IdealizedPart: Part
    MasterCadPart: Part


    class UseBodiesOption(enum.Enum):
        SelectedBodies = 0
        VisibleBodies = 1
        AllBodies = 2
    

class FEModelOccurrence(CAE.IFEModel):
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def GetComponent(self) -> Assemblies.Component:
        ...
    def GetCaeOccEntityLabelOffsets(self, nodeOffset: int, elemOffset: int, csysOffset: int, physOffset: int, groupOffset: int, plyOffset: int, ssmoOffset: int) -> None:
        ...
    def SetCaeOccEntityLabelOffsets(self, nodeOffset: int, elemOffset: int, csysOffset: int, physOffset: int, groupOffset: int, plyOffset: int, ssmoOffset: int) -> None:
        ...
    def GetAttributes(self) -> CAE.FEModelOccAttribute:
        ...
    def GetChildren(self) -> typing.List[CAE.FEModelOccurrence]:
        ...
    Overrides: CAE.OverrideCollection
    Parent: CAE.IFEModel


class FEModelOccAttribute(NXObject):
    def __init__(self) -> None: ...
    def GetRepType(self) -> CAE.FEModelOccAttribute.RepType:
        ...
    def GetLabel(self) -> int:
        ...
    def GetSuperElementFile(self) -> str:
        ...
    def GetAltRepDisplayStyle(self) -> CAE.FEModelOccAttribute.AltRepDisplayStyle:
        ...
    def SetAltRepDisplayStyle(self, dispStyle: CAE.FEModelOccAttribute.AltRepDisplayStyle) -> None:
        ...
    def GetAltRepDisplayColor(self) -> NXColor:
        ...
    def SetAltRepDisplayColor(self, color: NXColor) -> None:
        ...
    def GetAltRepDisplayFont(self) -> DisplayableObject.ObjectFont:
        ...
    def SetAltRepDisplayFont(self, lineFont: DisplayableObject.ObjectFont) -> None:
        ...
    def GetAltRepDisplayWidth(self) -> DisplayableObject.ObjectWidth:
        ...
    def SetAltRepDisplayWidth(self, width: DisplayableObject.ObjectWidth) -> None:
        ...
    def GetAltRepDisplayTranslucency(self) -> int:
        ...
    def SetAltRepDisplayTranslucency(self, translucency: int) -> None:
        ...
    AltRepPropertyTable: CAE.PropertyTable


    class RepType(enum.Enum):
        BaseFem = 0
        SuperElement = 1
    

    class AltRepMassUnitType(enum.Enum):
        G = 1
        Kg = 2
        Mg = 3
        T = 4
        Lbm = 5
        Slug = 6
        Inchlbfsec2In = 7
        Mmkgfsec2M = 8
        Kgfsec2Cm = 9
        Kgfsec2Mm = 10
    

    class AltRepLengthUnitType(enum.Enum):
        Km = 1
        M = 2
        Cm = 3
        Mm = 4
        Micron = 5
        Nm = 6
        An = 7
        Mi = 8
        Ft = 9
        Inch = 10
    

    class AltRepDisplayStyle(enum.Enum):
        None = 0
        Approx = 1
        Symbol = 2
        Simplified = 3
    

class FEModel(CAE.BaseFEModel):
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def AppendFemodel(self, sourceFem: CAE.FEModel, idSpec: CAE.FEModel.IdSpecificationObject) -> None:
        ...
    AbstractionMgr: CAE.AbstractionManager


    class FEModelIdSpecificationObject():
        FemObjectPrependName: str
        NodeStartId: int
        NodeIdOffset: bool
        ElementStartId: int
        ElementIdOffset: bool
        PhysicalPropertyTableStartId: int
        PhysicalPropertyTableIdOffset: bool
        def ToString(self) -> str:
            ...
    

    class FEModel_IdSpecificationObject():
        fem_object_prepend_name: int
        node_start_id: int
        node_id_offset: bool
        element_start_id: int
        element_id_offset: bool
        physical_property_table_start_id: int
        physical_property_table_id_offset: bool
    

class FemCreationOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetCadData(self, cadPart: Part, idealizedPartName: str) -> None:
        ...
    def SetAutoGenIdeal(self, autoGenIdeal: bool) -> None:
        ...
    def SetGeometryOptions(self, useBodiesOption: CAE.FemCreationOptions.UseBodiesOption, bodies: typing.List[Body], geometrySyncOptions: CAE.FemSynchronizeOptions) -> None:
        ...
    def SetLayerVisibilityOptions(self, layerVisibilityOption: CAE.FemCreationOptions.LayerVisibilityOption) -> None:
        ...
    def SetSolverOptions(self, solverName: str, analysisType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType) -> None:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def SetMorphingFlag(self, isMorphEnabled: bool) -> None:
        ...
    def SetCyclicSymmetryData(self, useCyclicSymmetryCsys: bool, cyclicSymmetryCsys: CoordinateSystem) -> None:
        ...
    def SetAxiPlaneCheckState(self, axiPlaneCheckState: bool) -> None:
        ...


    class UseBodiesOption(enum.Enum):
        SelectedBodies = 0
        VisibleBodies = 1
        AllBodies = 2
    

    class LayerVisibilityOption(enum.Enum):
        Part = 0
        FemTemplate = 1
        All = 2
    

class FEElemFace(TaggedObject):
    def __init__(self) -> None: ...
    def GetElementsAndFaceIds(self, faceIds: int) -> typing.List[CAE.FEElement]:
        ...


class FEElementLabelMap(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetElement(self, elementlabel: int) -> CAE.FEElement:
        ...
    def AskNextElementLabel(self, elementlabel: int) -> int:
        ...
    def AskElementLabelUsed(self, elementlabel: int) -> bool:
        ...
    def FreeResource(self) -> None:
        ...
    NumElements: int


class FEElement(TaggedObject):
    def __init__(self) -> None: ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...
    def GetElemFace(self, faceIndex: int) -> CAE.FEElemFace:
        ...
    def GetElemEdge(self, edgeIndex: int) -> CAE.FEElemEdge:
        ...
    def GetNumberOfCornerNodesOnFace(self, faceIndex: int) -> int:
        ...
    def GetNumberOfCornerNodesOnEdge(self, edgeIndex: int) -> int:
        ...
    def GetCornerNodesOnFace(self, faceIndex: int) -> typing.List[CAE.FENode]:
        ...
    def GetMidNodesOnFace(self, faceIndex: int) -> typing.List[CAE.FENode]:
        ...
    def GetFaceNormal(self, faceIndex: int) -> Vector3d:
        ...
    def GetCornerNodesOnEdge(self, edgeIndex: int) -> typing.List[CAE.FENode]:
        ...
    def GetMidNodeOnEdge(self, edgeIndex: int) -> CAE.FENode:
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    Label: int
    Mesh: CAE.Mesh
    NumberOfCornerNodes: int
    Order: CAE.ElementTypes.Order
    Shape: CAE.ElementTypes.Shape
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


class FEElemEdge(TaggedObject):
    def __init__(self) -> None: ...
    def GetElementsAndEdgeIds(self, edgeIds: int) -> typing.List[CAE.FEElement]:
        ...


class FeatureShellElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class FeatureNodeMethodOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetDoEntityVisibilityCheck(self, doEntityVisibilityCheck: bool) -> None:
        ...
    def SetComputeFreesOnVisibleModel(self, computeFreesOnVisibleModel: bool) -> None:
        ...
    def SetStopAtNonmanifoldJunctions(self, stopAtNonManifoldJunctions: bool) -> None:
        ...
    def SetFeatureAngle(self, featureAngle: float) -> None:
        ...
    def SetOnlyCornerNodes(self, onlyCornerNodes: bool) -> None:
        ...


class FeatureNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class FeatureElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class FeatureElemFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementFaces(self) -> typing.List[CAE.SetObject]:
        """[Obsolete("Deprecated in NX11.0.2.  Use NXOpen.CAE.FeatureElemFaceMethod.GetFeElemFaces.")"""
        ...
    def GetFeElemFaces(self) -> typing.List[CAE.FEElemFace]:
        ...


class FeatureElemEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElementEdges(self) -> typing.List[CAE.SetObject]:
        """[Obsolete("Deprecated in NX11.0.2.  Use NXOpen.CAE.FeatureElemEdgeMethod.GetFeElemEdges.")"""
        ...
    def GetFeElemEdges(self) -> typing.List[CAE.FEElemEdge]:
        ...


class FeatureEdgeNodeMethodOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetDoEntityVisibilityCheck(self, doEntityVisibilityCheck: bool) -> None:
        ...
    def SetComputeFreeEdgesOnVisibleModel(self, computeFreeEdgesOnVisibleModel: bool) -> None:
        ...
    def SetStopAtNonmanifoldJunctions(self, stopAtNonManifoldJunctions: bool) -> None:
        ...
    def SetComputeElementEdgeType(self, edgeType: CAE.Type) -> None:
        ...
    def SetFeatureAngle(self, featureAngle: float) -> None:
        ...
    def SetOnlyCornerNodes(self, onlyCornerNodes: bool) -> None:
        ...


class FeatureEdgeNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class FacePref(enum.Enum):
    First2dElse3d = 0
    First3dElse2d = 1
    Only2d = 2
    Only3d = 3
    FreeOnly = 4


class FaceFromBoundaryBuilder(Builder):
    def __init__(self) -> None: ...
    def AddSelectedPointPairs(self) -> None:
        ...
    EdgeSelection: CAE.SelectCAEEdgeList
    FirstPtSelect: Point
    PolygonBodySelection: CAE.SelectCAEBody
    SecondPtSelect: Point


class FaceFaceIntersectionBuilder(Builder):
    def __init__(self) -> None: ...
    GeomSelection: SelectDisplayableObjectList
    SnapDistance: Expression
    StitchToggle: bool


class FaceFaceImprintBuilder(Builder):
    def __init__(self) -> None: ...
    GeomSelection: SelectDisplayableObjectList
    StitchOption: bool
    ToleranceDistance: float


class FaceDensity(CAE.MeshControl):
    def __init__(self) -> None: ...


class ExtractingResultsToScd5OutputSettings(TaggedObject):
    def __init__(self) -> None: ...
    ErrorHandling: CAE.ResultsManipulationErrorHandling
    FileName: str
    UnitsSystem: CAE.ResultsManipulationUnitsSystem


class ExtractingResultsToScd5Builder(Builder):
    def __init__(self) -> None: ...
    InputSettings: CAE.ResultsManipulationInputSettings
    OutputSettings: CAE.ExtractingResultsToScd5OutputSettings


class ExtractingResultsToCsvOutputSettings(TaggedObject):
    def __init__(self) -> None: ...
    def GetRowColumnFormat(self, entityFormat: CAE.ExtractingResultsToCsvOutputSettings.VariableFormat, loadcaseFormat: CAE.ExtractingResultsToCsvOutputSettings.VariableFormat, resulttypeFormat: CAE.ExtractingResultsToCsvOutputSettings.VariableFormat) -> None:
        ...
    def SetRowColumnFormat(self, entityFormat: CAE.ExtractingResultsToCsvOutputSettings.VariableFormat, loadcaseFormat: CAE.ExtractingResultsToCsvOutputSettings.VariableFormat, resulttypeFormat: CAE.ExtractingResultsToCsvOutputSettings.VariableFormat) -> None:
        ...
    ErrorHandling: CAE.ResultsManipulationErrorHandling
    FileName: str
    NumberFormat: CAE.NumberFormat
    UnitsSystem: CAE.ResultsManipulationUnitsSystem


    class VariableFormat(enum.Enum):
        InRow = 0
        InColumn = 1
    

class ExtractingResultsToCsvBuilder(Builder):
    def __init__(self) -> None: ...
    InputSettings: CAE.ResultsManipulationInputSettings
    OutputSettings: CAE.ExtractingResultsToCsvOutputSettings


class ExpressionPlotContours(TaggedObject):
    def __init__(self) -> None: ...
    def PlotContour(self, viewIndex: int) -> None:
        ...


class ExportLatticeDiameterFieldBuilder(Builder):
    def __init__(self) -> None: ...
    FieldFile: str


class EnergyDistributionTableResultPIDData(TaggedObject):
    def __init__(self) -> None: ...
    Elements: int
    Energy: float
    Name: str
    RelativeEnergyPercentage: float


class EnergyDistributionTableResultGroupData(TaggedObject):
    def __init__(self) -> None: ...
    def GetResultPIDDatas(self) -> typing.List[CAE.EnergyDistributionTableResultPIDData]:
        ...
    Elements: int
    Energy: float
    Name: str
    RelativeEnergyPercentage: float


class EnergyDistributionTableBuilder(Builder):
    def __init__(self) -> None: ...
    def GetGroups(self) -> typing.List[CAE.CaeGroup]:
        ...
    def SetGroups(self, objects: typing.List[CAE.CaeGroup]) -> None:
        ...
    def Export(self, iAbsoluteFilePath: str) -> None:
        ...
    def GetResults(self) -> typing.List[CAE.EnergyDistributionTableResultGroupData]:
        ...
    Iteration: CAE.BaseIteration
    LoadCase: CAE.BaseLoadcase
    Result: CAE.Result
    ResultType: CAE.BaseResultType


class ElemLabelMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElems(self) -> typing.List[CAE.FEElement]:
        ...


class ElementTypes(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class Shape(enum.Enum):
        Undefined = -1
        Point = 0
        Line = 1
        Tri = 2
        Quad = 3
        Tet = 4
        Pyr = 5
        Wed = 6
        Hex = 7
        Spider = 8
        Matrix = 9
        Rspline = 10
    

    class Order(enum.Enum):
        Undefined = 0
        Linear = 1
        Parabolic = 2
        Mixed = 3
    

    class NeutralType(enum.Enum):
        Undefined = 0
        ConcentratedMass = 1
        Bar = 2
        Beam = 3
        Rod = 4
        RigidLink = 5
        Spring = 6
        Mass = 7
        HeatBody = 8
        Quad4 = 9
        Tri3 = 10
        Quad8 = 11
        Tri6 = 12
        Tet4 = 13
        Tet10 = 14
        Contact1d = 15
        Hex8 = 16
        Hex20 = 17
        Wed6 = 18
        Wed15 = 19
        Contact2d = 20
        Weld = 21
        EdgeFaceContact = 22
        MeshMatingFree = 23
        MeshMatingGlue = 24
        RigidBody3 = 25
        Pyramid5 = 26
        Pyramid9 = 27
        Pyramid13 = 28
        NodeGround1d = 29
        PlotElement1d = 30
        Mass1d = 31
        PyramidMixedOrder = 32
        TETMixedOrder = 33
        Bearing1d = 34
        HEXCohesive8 = 35
        HEXCohesive20 = 36
        WEDCohesive6 = 37
        WEDCohesive15 = 38
        MultipointConstraint = 39
        Matrix = 40
        Joint1d = 41
        Rspline = 42
        Bearing21d = 43
        Fou31d = 44
        Bushing21d = 45
        CLink1d = 46
        BendPipe = 47
        CGear1d = 48
    

    class Dimension(enum.Enum):
        Undefined = -1
        Point = 0
        Beam = 1
        Shell = 2
        Solid = 3
        Matrix = 4
        All = 5
    

class ElementTypeBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetElementTypeNames(self) -> str:
        ...
    DestinationCollector: CAE.DestinationCollectorBuilder
    ElementDimension: CAE.ElementTypeBuilder.ElementType
    ElementOrder: CAE.ElementTypeBuilder.ElementOrderType
    ElementTypeName: str
    PropertyTable: CAE.PropertyTable
    RetainElementType: bool


    class ElementType(enum.Enum):
        Point = 0
        Beam = 1
        Shell = 2
        FreeSolid = 3
        SweepSolid = 4
        SweepSolidWedge = 5
        Spider = 6
        Connection = 7
        AnySolid = 8
        TriaShell = 9
        QuadShell = 10
        Weld = 11
        Contact = 12
        Pyramid = 13
        Matrix = 14
    

    class ElementOrderType(enum.Enum):
        Any = 0
        Linear = 1
        Parabolic = 2
    

class ElementType(enum.Enum):
    Node1 = 0
    Line2 = 1
    Line3 = 2
    Spid = 3
    Spli = 4
    Tria3 = 5
    Tria6 = 6
    Quad4 = 7
    Quad8 = 8
    Tetr4 = 9
    Tetr10 = 10
    Wedg6 = 11
    Wedg15 = 12
    Pyra5 = 13
    Pyra13 = 14
    Hexa8 = 15
    Hexa20 = 16


class ElementTranslateBuilder(Builder):
    def __init__(self) -> None: ...
    CopyOption: CAE.ElementTranslateBuilder.CopyType
    Csys: CoordinateSystem
    Distance: Expression
    DistanceOption: CAE.ElementTranslateBuilder.DistanceType
    ElementDimension: CAE.ElementTranslateBuilder.ElemDimensionType
    ElementSelection: CAE.SelectElementsBuilder
    ElementType: CAE.ElementTypeBuilder
    ExportMesh: bool
    FlipState: int
    Increment: int
    Label: int
    LabelOption: CAE.ElementTranslateBuilder.LabelType
    MeshCollectorName: str
    MeshName: str
    Method: CAE.ElementTranslateBuilder.MethodType
    NeutralName: str
    NewMeshOption: CAE.ElementTranslateBuilder.NewMeshType
    NodeIncrement: int
    NodeLabel: int
    NodeLabelOption: CAE.ElementTranslateBuilder.LabelType
    NodeOffset: int
    NumCopy: int
    Offset: int
    PAngle: Expression
    RDistance: Expression
    SourcePoint: Point
    TAngle: Expression
    TargetPoint: Point
    Vector: Direction
    XDistance: Expression
    YDistance: Expression
    ZDistance: Expression


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

    class MethodType(enum.Enum):
        Component = 0
        Direction = 1
        ElemNormal = 2
        PointToPoint = 3
    

    class LabelType(enum.Enum):
        Label = 0
        Offset = 1
    

    class ElemDimensionType(enum.Enum):
        Any = 0
        Beam = 1
        Shell = 2
        Solid = 3
    

    class DistanceType(enum.Enum):
        PerCopy = 0
        Total = 1
    

    class CopyType(enum.Enum):
        TranslateOnly = 0
        CopyTranslate = 1
        ElementCoat = 2
    

class ElementSplitBuilder(Builder):
    def __init__(self) -> None: ...
    def Flip(self) -> None:
        ...
    Elementsss: CAE.SelectElementsBuilder
    FirstElementSplitType: int
    JacobianToggle: bool
    JacobianValue: float
    MValue: int
    MaxAngleToggle: bool
    MaxAngleValue: float
    MergeDupNode: bool
    MinAngleToggle: bool
    MinAngleValue: float
    NValue: int
    Point1: Point
    Point2: Point
    SplitMethod: CAE.ElementSplitBuilder.SplitMethodType
    Type: CAE.ElementSplitBuilder.Types
    WarpToggle: bool
    WarpValue: float


    class Types(enum.Enum):
        QuadTo2Tria = 0
        QuadTo2Quad = 1
        QuadTo4Quad = 2
        QuadToMxN = 3
        QuadTo3Quad = 4
        QuadTo3Tria = 5
        TriaTo4Tria = 6
        SplitByLine = 7
        TriaTo2Tria = 8
    

    class SplitMethodType(enum.Enum):
        SeedElement = 0
        ExistingConnectivity = 1
        InteractiveMouseLocation = 2
        ElementShape = 3
        ShortestDiagonal = 4
    

class ElementRotateBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: Expression
    Axis: Axis
    CopyOption: CAE.ElementRotateBuilder.CopyType
    DistanceCopyOption: CAE.ElementRotateBuilder.DistanceType
    ElementDimension: CAE.ElementRotateBuilder.ElemDimensionType
    ElementSelection: CAE.SelectElementsBuilder
    ElementType: CAE.ElementTypeBuilder
    Increment: int
    Label: int
    LabelOption: CAE.ElementRotateBuilder.LabelType
    MeshCollectorName: str
    MeshName: str
    NeutralName: str
    NewMeshOption: CAE.ElementRotateBuilder.NewMeshType
    NumCopy: int
    Offset: int


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

    class MethodType(enum.Enum):
        Component = 0
        Direction = 1
        ElemNormal = 2
        PointToPoint = 3
    

    class LabelType(enum.Enum):
        Label = 0
        Offset = 1
    

    class ElemDimensionType(enum.Enum):
        Any = 0
        Beam = 1
        Shell = 2
        Solid = 3
    

    class DistanceType(enum.Enum):
        PerCopy = 0
        Total = 1
    

    class CopyType(enum.Enum):
        RotateOnly = 0
        CopyRotate = 1
    

class ElementRevolveBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: Expression
    AngleOption: CAE.ElementRevolveBuilder.AngleType
    Axis: Axis
    CollectorName: str
    ElementDimensionOption: CAE.ElementRevolveBuilder.ElemDimType
    ElementType: CAE.ElementTypeBuilder
    Elements: CAE.SelectElementsBuilder
    ExportMesh: bool
    Increment: int
    Label: int
    MeshName: str
    NeutralName: str
    NewMeshOption: CAE.ElementRevolveBuilder.NewMeshType
    NumberOfCopy: int
    RetainCollector: bool


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

    class ElemDimType(enum.Enum):
        Beam = 0
        Shell = 1
    

    class AngleType(enum.Enum):
        PerCopy = 0
        Total = 1
    

class ElementReflectBuilder(Builder):
    def __init__(self) -> None: ...
    AssociativeSelection: SelectTaggedObjectList
    CollectorName: str
    ElementDimensionOption: CAE.ElementReflectBuilder.ElemDimType
    ElementType: CAE.ElementTypeBuilder
    Elements: CAE.SelectElementsBuilder
    ExportMesh: bool
    Increment: int
    Label: int
    LabelOption: CAE.ElementReflectBuilder.LabelType
    MergeNodes: bool
    MeshName: str
    MovToggle: bool
    NeutralName: str
    NewMeshOption: CAE.ElementReflectBuilder.NewMeshType
    Offset: int
    Plane: Plane
    ReflectType: CAE.ElementReflectBuilder.Type
    SolidElmOption: CAE.ElementReflectBuilder.SolidElemMovDirType


    class Type(enum.Enum):
        Associative = 0
        NonAssociative = 1
    

    class SolidElemMovDirType(enum.Enum):
        FirstAndSecond = 0
        FirstAndThird = 1
        SecondAndThird = 2
    

    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

    class LabelType(enum.Enum):
        Label = 0
        Offset = 1
    

    class ElemDimType(enum.Enum):
        Any = 0
        Beam = 1
        Shell = 2
        Solid = 3
    

class ElementProjectBuilder(Builder):
    def __init__(self) -> None: ...
    CollectorName: str
    ElementDimensionOption: CAE.ElementProjectBuilder.ElementDimensionType
    ElementType: CAE.ElementTypeBuilder
    Elements: CAE.SelectElementsBuilder
    ExportMesh: bool
    Face: CAE.SelectCAEFaceList
    FlipState: int
    Increment: int
    Label: int
    LabelOption: CAE.ElementProjectBuilder.LabelType
    MeshName: str
    MethodOption: CAE.ElementProjectBuilder.MethodType
    NeutralName: str
    NewMeshOption: CAE.ElementProjectBuilder.NewMeshType
    Offset: int
    PercentOffset: float
    Vector: Direction


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

    class MethodType(enum.Enum):
        Vector = 0
        ElemNormal = 1
    

    class LabelType(enum.Enum):
        Label = 0
        Offset = 1
    

    class ElementDimensionType(enum.Enum):
        Any = 0
        Beam = 1
        Shell = 2
    

class ElementNormalsType(enum.Enum):
    None = 0
    Tails = 1
    Vectors = 2


class ElementModifyTypeBuilder(Builder):
    def __init__(self) -> None: ...
    ElementType: CAE.ElementTypeBuilder
    MeshCollectorName: str
    MeshSelection: SelectTaggedObjectList
    RetainSourceCollectorName: bool
    UseSourceMeshCollector: bool


class ElementModifyOrderBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> typing.List[CAE.Mesh]:
        ...
    ElementType: CAE.ElementTypeBuilder
    Jacobian: Expression
    MeshSelection: SelectTaggedObjectList
    MidnodeType: CAE.ElementModifyOrderBuilder.Midnode
    OperationType: CAE.ElementModifyOrderBuilder.Operation


    class Operation(enum.Enum):
        Order = 0
        Midnode = 1
    

    class Midnode(enum.Enum):
        Mixed = 0
        Curved = 1
        Linear = 2
    

class ElementModifyLabelBuilder(Builder):
    def __init__(self) -> None: ...
    Elements: CAE.SelectElementsBuilder
    Increment: int
    Label: int
    LabelOption: CAE.ElementModifyLabelBuilder.LabelType
    Offset: int


    class LabelType(enum.Enum):
        LabelIncrement = 0
        ByOffset = 1
    

class ElementInfoUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.NodeElementManager) -> None: ...
    def Ask2d3dElementCentroids(self, elements: typing.List[CAE.FEElement], coordinateSystem: CoordinateSystem) -> typing.List[Point3d]:
        ...
    def Ask2dElementAreas(self, elements: typing.List[CAE.FEElement]) -> float:
        ...
    def Ask2dElementNormals(self, elements: typing.List[CAE.FEElement]) -> typing.List[Vector3d]:
        ...
    def Ask3dElementVolumes(self, elements: typing.List[CAE.FEElement]) -> float:
        ...
    def CreateBeamElementInfoHandler(self) -> CAE.BeamElementInfoHandler:
        ...
    def Tag(self) -> Tag: ...



class ElementExtrudeBuilder(Builder):
    def __init__(self) -> None: ...
    def Flip(self) -> None:
        ...
    Axis: Axis
    CollectorName: str
    Distance: Expression
    DistanceOption: CAE.ElementExtrudeBuilder.DistanceType
    Edge: CAE.SelectCAEEdge
    ElementDimensionOption: CAE.ElementExtrudeBuilder.ElemDimType
    ElementType: CAE.ElementTypeBuilder
    Elements: CAE.SelectElementsBuilder
    ExportMesh: bool
    Face: CAE.SelectCAEFaceList
    FlipState: int
    Increment: int
    Label: int
    MeshName: str
    MethodOption: CAE.ElementExtrudeBuilder.MethodType
    NeutralName: str
    NewMeshOption: CAE.ElementExtrudeBuilder.NewMeshType
    NumberOfCopy: int
    PercentOffset: float
    RetainCollector: bool
    TwistAngle: Expression
    TwistOrigin: Point
    Vector: Direction


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

    class MethodType(enum.Enum):
        Vector = 0
        Path = 1
        ProjSurface = 2
        ElemNormal = 3
        Radial = 4
    

    class ElemDimType(enum.Enum):
        Beam = 0
        Shell = 1
    

    class DistanceType(enum.Enum):
        PerCopy = 0
        Total = 1
    

class ElementExtractBuilder(Builder):
    def __init__(self) -> None: ...
    ElemSel: CAE.SelectElementsBuilder


class ElementDetachBuilder(Builder):
    def __init__(self) -> None: ...
    DetachNodeOption: bool
    DetachmentNodes: CAE.SelectFENodeList
    ElementSelection: CAE.SelectElementsBuilder
    NewMeshOption: bool


class ElementDeleteBuilder(Builder):
    def __init__(self) -> None: ...
    DeleteDangling: bool
    Element: CAE.SelectElementsBuilder


class ElementCreateBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateCollector(self) -> None:
        ...
    CollectorName: str
    ElementDimensionOption: CAE.ElementCreateBuilder.ElemDimType
    ElementType: CAE.ElementTypeBuilder
    ExportMesh: bool
    Increment: int
    Label: int
    MeshName: str
    NeutralName: str
    NewMeshOption: CAE.ElementCreateBuilder.NewMeshType
    Node: CAE.SelectFENodeList
    Point: SelectTaggedObjectList


    class NewMeshType(enum.Enum):
        Create = 0
        Existing = 1
    

    class ElemDimType(enum.Enum):
        Point = 0
        Beam = 1
        Shell = 2
        Solid = 3
        AnySolid = 4
    

class ElementConnectivityBuilder(Builder):
    def __init__(self) -> None: ...
    DeleteOrphan: bool
    Element: CAE.SelectElementsBuilder
    InNode: CAE.SelectFENode
    Method: CAE.ElementConnectivityBuilder.Methods
    OutNode: CAE.SelectFENode
    SpiderLegNodes: CAE.SelectFENodeList
    Type: CAE.ElementConnectivityBuilder.Types


    class Types(enum.Enum):
        SingleElement = 0
        AllElementsAttachedToNode = 1
    

    class Methods(enum.Enum):
        ReplaceNode = 0
        SwapEnds = 1
        ModifyLegs = 2
    

class ElementAssociatedDataUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.NodeElementManager) -> None: ...
    def AskConstraintEquationData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, terms: typing.List[CAE.DofTerm], constantTerm: float) -> None:
        ...
    def SetConstraintEquationData(self, element: CAE.FEElement, terms: typing.List[CAE.DofTerm], constantTerm: float) -> None:
        ...
    def AskShellData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, cornerNodeThicknesses: float, cornerNodeGapValues: float, zOffset: float, physicalPropertyTable: CAE.PhysicalPropertyTable, matOriMethod: CAE.CaeElementAssociatedDataUtilsMatOrientationMethod, coordinateSystem: CoordinateSystem, matOriAngle: float, csysDataType: CAE.CaeElementAssociatedDataUtilsCsysDataType, originPoint: Point3d, zAxisPoint: Point3d, planePoint: Point3d, preferredLabel: int) -> None:
        ...
    def SetShellData(self, element: CAE.FEElement, cornerNodeThicknesses: float, cornerNodeGapValues: float, zOffset: float, physicalPropertyTable: CAE.PhysicalPropertyTable, matOriMethod: CAE.CaeElementAssociatedDataUtilsMatOrientationMethod, coordinateSystem: CoordinateSystem, matOriAngle: float, csysDataType: CAE.CaeElementAssociatedDataUtilsCsysDataType, originPoint: Point3d, zAxisPoint: Point3d, planePoint: Point3d, preferredLabel: int) -> None:
        ...
    def AskBeamData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, vectorType: CAE.CaeElementAssociatedDataUtilsVectorChoiceType, direction: Direction, orientationNode: CAE.FENode, endAState: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndADOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, endBState: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndBDOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, xOffsetEndA: float, yOffsetEndA: float, zOffsetEndA: float, xOffsetEndB: float, yOffsetEndB: float, zOffsetEndB: float) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ElementAssociatedDataUtils.AskBeamData2 instead.")"""
        ...
    def AskBeamData2(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, orientationCsysType: CAE.CaeElementAssociatedDataUtilsOrientationCsys, vectorType: CAE.CaeElementAssociatedDataUtilsVectorChoiceType, direction: Direction, orientationNode: CAE.FENode, endAState: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndADOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, endBState: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndBDOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, offsetCSYSEndA: CAE.CaeElementAssociatedDataUtilsOffsetCsysChoice, xOffsetEndA: float, yOffsetEndA: float, zOffsetEndA: float, offsetCSYSEndB: CAE.CaeElementAssociatedDataUtilsOffsetCsysChoice, xOffsetEndB: float, yOffsetEndB: float, zOffsetEndB: float) -> None:
        ...
    def SetBeamData(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, vectorType: CAE.CaeElementAssociatedDataUtilsVectorChoiceType, direction: Direction, orientationNode: CAE.FENode, endReleaseA: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndADOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, endReleaseB: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndBDOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, xOffsetEndA: float, yOffsetEndA: float, zOffsetEndA: float, xOffsetEndB: float, yOffsetEndB: float, zOffsetEndB: float) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use NXOpen.CAE.ElementAssociatedDataUtils.SetBeamData2 which has 32 parameters instead.")"""
        ...
    def SetBeamData2(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, orientationCsysType: CAE.CaeElementAssociatedDataUtilsOrientationCsys, vectorType: CAE.CaeElementAssociatedDataUtilsVectorChoiceType, direction: Direction, orientationNode: CAE.FENode, endReleaseA: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndADOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, endReleaseB: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndBDOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, offsetCSYSEndA: CAE.CaeElementAssociatedDataUtilsOffsetCsysChoice, xOffsetEndA: float, yOffsetEndA: float, zOffsetEndA: float, offsetCSYSEndB: CAE.CaeElementAssociatedDataUtilsOffsetCsysChoice, xOffsetEndB: float, yOffsetEndB: float, zOffsetEndB: float) -> None:
        ...
    def AskInterpolationData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, dofDataTerms: typing.List[CAE.DofTerm]) -> int:
        ...
    def SetInterpolationData(self, element: CAE.FEElement, dofDataTerms: typing.List[CAE.DofTerm], umData: int) -> None:
        ...
    def AskBushingData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, oriDirr: Direction, coordinateSystem: CoordinateSystem, oriNode: CAE.FENode, csysDataType: CAE.CaeElementAssociatedDataUtilsCsysDataType, originPoint: Point3d, zAxisPoint: Point3d, planePoint: Point3d, preferredLabel: int) -> None:
        ...
    def SetBushingData(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, oriDirr: Direction, coordinateSystem: CoordinateSystem, oriNode: CAE.FENode, csysDataType: CAE.CaeElementAssociatedDataUtilsCsysDataType, originPoint: Point3d, zAxisPoint: Point3d, planePoint: Point3d, preferredLabel: int) -> None:
        ...
    def AskGapData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, oriDirr: Direction, coordinateSystem: CoordinateSystem, oriNode: CAE.FENode) -> None:
        ...
    def SetGapData(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, oriDirr: Direction, coordinateSystem: CoordinateSystem, oriNode: CAE.FENode) -> None:
        ...
    def AskSpringData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable, stiffness: float, componentEndA: CAE.CaeElementAssociatedDataUtilsComponentEnd, componentEndB: CAE.CaeElementAssociatedDataUtilsComponentEnd) -> None:
        ...
    def SetSpringData(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, stiffness: float, componentEndA: CAE.CaeElementAssociatedDataUtilsComponentEnd, componentEndB: CAE.CaeElementAssociatedDataUtilsComponentEnd) -> None:
        ...
    def AskLumpedMassData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, mass: float) -> None:
        ...
    def SetLumpedMassData(self, element: CAE.FEElement, mass: float) -> None:
        ...
    def AskRigidData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, dofs: typing.List[CAE.CaeElementAssociatedDataUtilsDof]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  NXOpen.CAE.ElementAssociatedDataUtils.AskRigidData2 instead.")"""
        ...
    def AskRigidData2(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable, dofs: typing.List[CAE.CaeElementAssociatedDataUtilsDof]) -> None:
        ...
    def SetRigidData(self, element: CAE.FEElement, dofs: typing.List[CAE.CaeElementAssociatedDataUtilsDof]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  NXOpen.CAE.ElementAssociatedDataUtils.SetRigidData2 instead.")"""
        ...
    def SetRigidData2(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, dofs: typing.List[CAE.CaeElementAssociatedDataUtilsDof]) -> None:
        ...
    def AskDamperData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, viscousDamping: float, physicalPropertyTable: CAE.PhysicalPropertyTable, componentEndA: CAE.CaeElementAssociatedDataUtilsComponentEnd, componentEndB: CAE.CaeElementAssociatedDataUtilsComponentEnd) -> None:
        ...
    def SetDamperData(self, element: CAE.FEElement, viscousDamping: float, physicalPropertyTable: CAE.PhysicalPropertyTable, componentEndA: CAE.CaeElementAssociatedDataUtilsComponentEnd, componentEndB: CAE.CaeElementAssociatedDataUtilsComponentEnd) -> None:
        ...
    def AskSolidData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable) -> None:
        ...
    def SetSolidData(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable) -> None:
        ...
    def AskRsplineData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, dofDataTerms: typing.List[CAE.ComponentDofsTerm]) -> None:
        ...
    def SetRsplineData(self, element: CAE.FEElement, dofDataTerms: typing.List[CAE.ComponentDofsTerm]) -> None:
        ...
    def AskBendPipeData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, oriDirr: Direction, oriNode: CAE.FENode) -> None:
        ...
    def SetBendPipeData(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, oriDirr: Direction, oriNode: CAE.FENode) -> None:
        ...
    def Tag(self) -> Tag: ...



class ElemEdgePathMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def AddSeedEdge(self, seedStartNode: CAE.FENode, seedElemEdge: CAE.FEElemEdge, preferFreeEdges: bool, preferGeometryAssociatedEdges: bool, preferFeatureElementEdge: bool, featureAngleTolerance: float, allowGapJumping: bool, gapJumpingTolerance: float, pathMethodType: CAE.PathType, dTangentAngleTolerance: float) -> None:
        ...
    def RemoveSeedEdge(self, seedElemEdge: CAE.FEElemEdge) -> None:
        ...
    def FlipPath(self) -> None:
        ...
    def GetSeeds(self, seedStartNodes: typing.List[CAE.FENode], seedElemEdges: typing.List[CAE.FEElemEdge], preferFreeEdges: bool, preferGeometryAssociatedEdges: bool, preferFeatureElementEdge: bool, featureAngleTolerance: float, allowGapJumping: bool, gapJumpingTolerance: float) -> None:
        ...
    def GetPathEdges(self, pathStartNodes: typing.List[CAE.FENode], pathElemEdges: typing.List[CAE.FEElemEdge]) -> None:
        ...


class ElemEdgefaceObject():
    Obj: CAE.FEElement
    SubType: CAE.CaeGroupElementSubType
    SubId: int
    def ToString(self) -> str:
        ...
    def __init__(self, Obj: CAE.FEElement, SubType: CAE.CaeGroupElementSubType, SubId: int) -> None: ...


class EdgeSticherBuilder(Builder):
    def __init__(self) -> None: ...
    BodySelection: CAE.SelectCAEBodyList
    ExclusionEdgeSelection: CAE.SelectCAEEdgeList
    SearchDistance: Expression
    SnapEnds: Expression
    SourceEdgeSelection: CAE.SelectCAEEdgeList
    StitchMethod: CAE.EdgeSticherBuilder.StitchMethods
    StitchOption: CAE.EdgeSticherBuilder.StitchOptions
    TargetEdgeSelection: CAE.SelectCAEEdgeList
    TargetFaceSelection: CAE.SelectCAEFaceList
    Type: CAE.EdgeSticherBuilder.Types


    class Types(enum.Enum):
        AutomaticFreeEdgeToAllEdges = 0
        ManualEdgeToEdge = 1
        ManualEdgeToFace = 2
    

    class StitchOptions(enum.Enum):
        EdgeToEdges = 0
        EdgeToFaces = 1
        Both = 2
    

    class StitchMethods(enum.Enum):
        Automatic = 0
        Manual = 1
    

class EdgeSeparationConditionBuilder(Builder):
    def __init__(self) -> None: ...
    EdgeSelection: CAE.SelectCAEEdgeList


class EdgeSeparation(CAE.MeshControl):
    def __init__(self) -> None: ...


class EdgePathMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def AddSeedEdge(self, seedStartVertex: CAE.CAEVertex, seedEdge: CAE.CAEEdge, preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float, pathMethodType: CAE.PathType, dTangentAngleTolerance: float) -> None:
        ...
    def AddClosedSeedEdge(self, seedEdgeTag: CAE.CAEEdge, flipEdge: bool) -> None:
        ...
    def RemoveSeedEdge(self, seedEdge: CAE.CAEEdge) -> None:
        ...
    def FlipPath(self) -> None:
        ...
    def GetSeeds(self, seedStartVertices: typing.List[CAE.CAEVertex], seedEdges: typing.List[CAE.CAEEdge], preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float) -> None:
        ...
    def GetPathEdges(self, pathStartVertices: typing.List[CAE.CAEVertex], pathEdges: typing.List[CAE.CAEEdge]) -> None:
        ...
    def GetClosedPathEdge(self, seedEdgeTag: CAE.CAEEdge, flipEdge: bool) -> None:
        ...


class EdgeFaceImprintBuilder(Builder):
    def __init__(self) -> None: ...
    EdgeCurveSelection: SelectDisplayableObjectList
    ExtendEdgeToBoundaryToggle: bool
    ProjectionDirectionMethod: CAE.EdgeFaceImprintBuilder.ProjectionDirectionType
    ProjectionVector: Direction
    StitchToggle: bool
    TargetFace: SelectDisplayableObjectList


    class ProjectionDirectionType(enum.Enum):
        AlongNormal = 0
        ClosetToTarget = 1
        AlongVector = 2
    

class EdgeDensity(CAE.MeshControl):
    def __init__(self) -> None: ...


class DurspStrainGageType(enum.Enum):
    UniAxial = 0
    BiAxial = 1
    Rosette45DegreeIncrement = 2
    Rosette60DegreeIncrement = 3


class DurspStrainGageShellElementFaceType(enum.Enum):
    Top = 0
    Botton = 1


class DurspStrainGagePlacementType(enum.Enum):
    Node = 0
    ElementFaceCenter = 1


class DurspStrainGageOrientationPlane(enum.Enum):
    FacePlane = 0
    Csys = 1


class DurSpecialistVibrationInputDefinitionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistVibrationInputDefinition]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDurSpecialistVibrationInputDefinitionBuilder(self, inputDef: CAE.DurSpecialistVibrationInputDefinition) -> CAE.DurSpecialistVibrationInputDefinitionBuilder:
        ...
    def FindObject(self, name: str) -> CAE.DurSpecialistVibrationInputDefinition:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistVibrationInputDefinitionBuilder(Builder):
    def __init__(self) -> None: ...
    BCTypeRX: CAE.DurSpecialistVibrationInputDefinitionBuilder.BcType
    BCTypeRY: CAE.DurSpecialistVibrationInputDefinitionBuilder.BcType
    BCTypeRZ: CAE.DurSpecialistVibrationInputDefinitionBuilder.BcType
    BCTypeX: CAE.DurSpecialistVibrationInputDefinitionBuilder.BcType
    BCTypeY: CAE.DurSpecialistVibrationInputDefinitionBuilder.BcType
    BCTypeZ: CAE.DurSpecialistVibrationInputDefinitionBuilder.BcType
    CoordSys: CoordinateSystem
    DataSourceBuilder: CAE.DurSpecialistVibrationDataSourceBuilder
    Description: str
    EnumCSYS: CAE.DurSpecialistVibrationInputDefinitionBuilder.Csys
    FuncRX: CAE.Function
    FuncRY: CAE.Function
    FuncRZ: CAE.Function
    FuncX: CAE.Function
    FuncY: CAE.Function
    FuncZ: CAE.Function
    HarmonicDataSourceBuilder: CAE.DurSpecialistHarmonicDataSourceBuilder
    MPFSubcaseRX: CAE.DurSpecialistMpfSubcaseLink
    MPFSubcaseRY: CAE.DurSpecialistMpfSubcaseLink
    MPFSubcaseRZ: CAE.DurSpecialistMpfSubcaseLink
    MPFSubcaseX: CAE.DurSpecialistMpfSubcaseLink
    MPFSubcaseY: CAE.DurSpecialistMpfSubcaseLink
    MPFSubcaseZ: CAE.DurSpecialistMpfSubcaseLink
    Name: str
    ScaleFactorMPFRX: Expression
    ScaleFactorMPFRY: Expression
    ScaleFactorMPFRZ: Expression
    ScaleFactorMPFX: Expression
    ScaleFactorMPFY: Expression
    ScaleFactorMPFZ: Expression
    SelectNodes: CAE.SelectFENodeList
    UnitLoadMeasureMPFRX: CAE.DurSpecialistVibrationInputDefinitionBuilder.MpfUnitLoadMeasureType
    UnitLoadMeasureMPFRY: CAE.DurSpecialistVibrationInputDefinitionBuilder.MpfUnitLoadMeasureType
    UnitLoadMeasureMPFRZ: CAE.DurSpecialistVibrationInputDefinitionBuilder.MpfUnitLoadMeasureType
    UnitLoadMeasureMPFX: CAE.DurSpecialistVibrationInputDefinitionBuilder.MpfUnitLoadMeasureType
    UnitLoadMeasureMPFY: CAE.DurSpecialistVibrationInputDefinitionBuilder.MpfUnitLoadMeasureType
    UnitLoadMeasureMPFZ: CAE.DurSpecialistVibrationInputDefinitionBuilder.MpfUnitLoadMeasureType


    class MpfUnitLoadMeasureType(enum.Enum):
        None = 0
        Force = 1
        Moment = 2
        Displacement = 3
        Velocity = 4
        Acceleration = 5
        AngularDisplacement = 6
        AngularVelocity = 7
        AngularAcceleration = 8
    

    class Csys(enum.Enum):
        Existing = 0
        Global = 1
        Cartesian = 2
        Cylindrical = 3
        Spherical = 4
    

    class BcType(enum.Enum):
        Free = 0
        Fixed = 1
        EnforcedMotion = 2
        NodalForce = 3
        NodalMoment = 4
    

class DurSpecialistVibrationInputDefinition(NXObject):
    def __init__(self) -> None: ...
    def InformationWindow(self) -> None:
        ...


class DurSpecialistVibrationDataSourceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistVibrationDataSource]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateVibrationDataSourceBuilder(self, dataSource: CAE.DurSpecialistVibrationDataSource) -> CAE.DurSpecialistVibrationDataSourceBuilder:
        ...
    def InformationWindow(self) -> None:
        ...
    def CloneVibrationDataSource(self, sourceVibrationDataSource: CAE.DurSpecialistVibrationDataSource) -> CAE.DurSpecialistVibrationDataSource:
        ...
    def DeleteVibrationDataSource(self, theVibrationDataSource: CAE.DurSpecialistVibrationDataSource) -> None:
        ...
    def Rename(self, theVibrationDataSource: CAE.DurSpecialistVibrationDataSource, name: str) -> None:
        ...
    def VibrationDataSourceInformationWindow(self, theVibrationDataSource: CAE.DurSpecialistVibrationDataSource) -> None:
        ...
    def FindObject(self, name: str) -> CAE.DurSpecialistVibrationDataSource:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistVibrationDataSourceBuilder(Builder):
    def __init__(self) -> None: ...
    def AddVibrationInputDefinition(self, vid: CAE.DurSpecialistVibrationInputDefinition) -> None:
        ...
    def AddCorrelationInputDefinition(self, cid: CAE.DurSpecialistCorrelationInputDefinition) -> None:
        ...
    def GetNumberMPFSubcases(self) -> int:
        ...
    def GetNthMPFSubcaseIndex(self, nth: int) -> int:
        ...
    def GetNthMPFSubcase(self, nth: int) -> CAE.DurSpecialistMpfSubcaseLink:
        ...
    def GetNthMPFSubcaseName(self, nth: int) -> str:
        ...
    def GetFileName(self) -> str:
        ...
    def SetFile(self, fileName: str, type: CAE.DurSpecialistDataSources.FileFormat) -> None:
        ...
    def SetSolution(self, sol: CAE.SimSolution) -> None:
        ...
    def SetUnitSystem(self, unitSystem: CAE.DurSpecialistDataSources.UnitSystem) -> None:
        ...
    def SetStaticLoad(self, modeIndex: int, scaleFactor: float) -> None:
        ...
    def UpdateMpfVibrationInputDefinitionByFile(self, mpfFilePath: str) -> None:
        ...
    def UpdateMpfVibrationInputDefinitionByModeSet(self, modeSet: CAE.ModeSet) -> None:
        ...
    def AdjustMpfVibrationInputDefinitionBCTypes(self) -> int:
        ...
    DataSourceType: CAE.DurSpecialistDataSources.FileFormat
    Description: str
    FilePath: str
    Mode: CAE.DurSpecialistVibrationDataSourceBuilder.ModeType
    ModeSelection: CAE.DurSpecialistEvent.UpdateCriterionType
    ModeSet: CAE.ModeSet
    MpfSource: CAE.DurSpecialistVibrationDataSourceBuilder.Source
    Name: str
    NumStaticLoadScales: int
    ReadMpf: bool
    StaticLoadSourceType: CAE.DurSpecialistVibrationDataSourceBuilder.StaticLoadSource
    Step: Expression


    class StaticLoadSource(enum.Enum):
        File = 0
        Solution = 1
    

    class Source(enum.Enum):
        File = 0
        ModeSet = 1
    

    class ModeType(enum.Enum):
        Free = 0
        Fixed = 1
        ReadMpf = 2
    

class DurSpecialistVibrationDataSource(NXObject):
    def __init__(self) -> None: ...
    def RemoveVibrationInputDefinition(self, vid: CAE.DurSpecialistVibrationInputDefinition) -> None:
        ...
    def VibrationInputsInformation(self) -> None:
        ...
    def RemoveCorrelationInputDefinition(self, cid: CAE.DurSpecialistCorrelationInputDefinition) -> None:
        ...
    def ClearVibrationInputDefinitions(self) -> None:
        ...
    def ClearCorrelationInputDefinitions(self) -> None:
        ...
    def CorrelationInputsInformation(self) -> None:
        ...
    def RenameVibrationInputDefinition(self, vid: CAE.DurSpecialistVibrationInputDefinition, name: str) -> None:
        ...
    def RenameCorrelationInputDefinition(self, cid: CAE.DurSpecialistCorrelationInputDefinition, name: str) -> None:
        ...


class DurSpecialistTransientEventBuilder(Builder):
    def __init__(self) -> None: ...
    def TagOutputTransientIncrements(self) -> None:
        ...
    def MoveSelectedTransientSubcases(self, subcaseToMoveIndices: int, operation: CAE.DurSpecialistTransientEventBuilder.MoveOperation) -> None:
        ...
    def EditSelectedTransientIncrements(self, incrementToEditIndices: int, parentSubcaseIndices: int, operation: CAE.DurSpecialistTransientEventBuilder.EditOperation, value: bool) -> None:
        ...
    def EditSelectedTransientIncrementsScale(self, incrementToEditIndices: int, parentSubcaseIndices: int, scales: float) -> None:
        ...
    def GetNumTransientIncrements(self) -> int:
        ...
    def EditSelectedSubcaseLinks(self, subcaseLinksToEditIndices: int, operation: CAE.DurSpecialistTransientEventBuilder.SubcaseLinkOperation, scale: float) -> bool:
        ...
    Description: str
    FeResults: CAE.DurSpecialistDataSources
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    MatchBy: CAE.DurSpecialistTransientEventBuilder.MatchByType
    Name: str
    TemperatureSource: CAE.DurSpecialistTemperatureSource
    TemperatureSourceInherited: bool
    TemperatureSourceOverlapResolution: CAE.DurSpecialistTransientEventBuilder.OverlapResolution
    TimeIncrement: int


    class SubcaseLinkOperation(enum.Enum):
        MoveUp = 0
        MoveDown = 1
        Activate = 2
        Deactivate = 3
        Scale = 4
        ReverseOrder = 5
        OriginalOrder = 6
        Duplicate = 7
        Remove = 8
    

    class OverlapResolution(enum.Enum):
        Maximum = 0
        Minimum = 1
        Average = 2
    

    class MoveOperation(enum.Enum):
        ReverseOrder = 0
        MoveUp = 1
        MoveDown = 2
    

    class MatchByType(enum.Enum):
        Name = 0
        Index = 1
    

    class EditOperation(enum.Enum):
        Active = 0
        Visible = 1
        Output = 2
    

class DurSpecialistTransientEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistTemperatureTimeHistoryDataSource(CAE.DurSpecialistFunctionDataSource):
    def __init__(self) -> None: ...


class DurSpecialistTemperatureSourceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistTemperatureSource]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateTemperatureSourceBuilder(self, temperatureSource: CAE.DurSpecialistTemperatureSource) -> CAE.DurSpecialistTemperatureSourceBuilder:
        ...
    def CreateTemperatureLoadBuilder(self, temperatureLoad: CAE.DurSpecialistTemperatureLoad) -> CAE.DurSpecialistTemperatureLoadBuilder:
        ...
    def InformationWindow(self) -> None:
        ...
    def CloneTemperatureSource(self, sourceTemperatureSource: CAE.DurSpecialistTemperatureSource) -> CAE.DurSpecialistTemperatureSource:
        ...
    def DeleteTemperatureSource(self, theTemperatureSource: CAE.DurSpecialistTemperatureSource) -> None:
        ...
    def Rename(self, theTemperatureSource: CAE.DurSpecialistTemperatureSource, name: str) -> None:
        ...
    def TemperatureSourceInformationWindow(self, theTemperatureSource: CAE.DurSpecialistTemperatureSource) -> None:
        ...
    def FindObject(self, name: str) -> CAE.DurSpecialistTemperatureSource:
        ...
    def CreateTemperatureLoadListBuilder(self) -> CAE.DurSpecialistTemperatureLoadListBuilder:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistTemperatureSourceBuilder(Builder):
    def __init__(self) -> None: ...
    def GetFileName(self) -> str:
        ...
    def SetFile(self, fileName: str, type: CAE.DurSpecialistDataSources.FileFormat) -> None:
        ...
    def SetSolution(self, sol: CAE.SimSolution) -> None:
        ...
    def GetDataSourceType(self) -> CAE.DurSpecialistDataSources.FileFormat:
        ...
    def GetTemperatureUnitSystem(self) -> CAE.DurSpecialistDataSources.TemperatureUnitSystem:
        ...
    def SetTemperatureUnitSystem(self, temperatureUnitSystem: CAE.DurSpecialistDataSources.TemperatureUnitSystem) -> None:
        ...
    def MoveSelectedTransientSubcases(self, subcaseToMoveIndices: int, operation: CAE.DurSpecialistTemperatureSourceBuilder.MoveOperation) -> None:
        ...
    def EditSelectedTransientIncrements(self, incrementToEditIndices: int, parentSubcaseIndices: int, operation: CAE.DurSpecialistTemperatureSourceBuilder.EditOperation, value: bool) -> None:
        ...
    def EditSelectedTransientIncrementsScale(self, incrementToEditIndices: int, parentSubcaseIndices: int, scales: float) -> None:
        ...
    def TagOutputTransientIncrements(self) -> None:
        ...
    def GetNumTransientIncrements(self) -> int:
        ...
    def AddTemperatureLoad(self, newLoadTag: CAE.DurSpecialistTemperatureLoad) -> None:
        ...
    def RemoveTemperatureLoad(self, indexes: int) -> None:
        ...
    def EditSelectedSubcaseLinks(self, subcaseLinksToEditIndices: int, operation: CAE.DurSpecialistTemperatureSourceBuilder.SubcaseLinkOperation, scale: float) -> bool:
        ...
    def GetRemainingStructureFileName(self) -> str:
        ...
    def SetFileForRemainingStructure(self, fileName: str, type: CAE.DurSpecialistDataSources.FileFormat) -> None:
        ...
    def PlotChannelDataCurveForRemainingStructure(self, deviceIndex: int, viewIndex: int) -> None:
        ...
    def GetEntireModelFileName(self) -> str:
        ...
    def SetFileForEntireModel(self, fileName: str, type: CAE.DurSpecialistDataSources.FileFormat) -> None:
        ...
    def PlotChannelDataCurveForEntireModel(self, deviceIndex: int, viewIndex: int) -> None:
        ...
    Description: str
    EntireModelSubcase: int
    EnumLoadSource: CAE.DurSpecialistTemperatureLoadBuilder.LoadSource
    EnumOverlapResolution: CAE.DurSpecialistTemperatureSourceBuilder.OverlapResolution
    EnumRemainingStructureLoadSource: CAE.DurSpecialistTemperatureLoadBuilder.LoadSource
    EnumRemainingStructureTemperatureLoadType: CAE.DurSpecialistTemperatureLoadBuilder.LoadType
    EnumResultSource: CAE.DurSpecialistTemperatureSourceBuilder.ResultSource
    EnumSourceType: CAE.DurSpecialistTemperatureSourceBuilder.SourceType
    EnumTemperatureDistribution: CAE.DurSpecialistTemperatureSourceBuilder.TemperatureDistribution
    FeResults: CAE.DurSpecialistDataSources
    MatchBy: CAE.DurSpecialistTemperatureSourceBuilder.MatchByType
    Name: str
    PropertyTable: CAE.PropertyTable
    RemainingStructureSubcase: int
    Subcase: int
    ToggleTemperatureRemainingStructure: bool
    TransientLoadTimeControl: CAE.DurSpecialistTemperatureSourceBuilder.TimeStepControl
    TransientLoadTimeIncrement: int


    class TimeStepControl(enum.Enum):
        DefineIncrement = 0
        StartandEnd = 1
    

    class TemperatureDistribution(enum.Enum):
        EntireModel = 0
        Groups = 1
    

    class SubcaseLinkOperation(enum.Enum):
        MoveUp = 0
        MoveDown = 1
        Activate = 2
        Deactivate = 3
        Scale = 4
        ReverseOrder = 5
        OriginalOrder = 6
        Duplicate = 7
        Remove = 8
    

    class SourceType(enum.Enum):
        Constant = 0
        TimeHistory = 1
        DataSource = 2
        TransientDataSource = 3
    

    class ResultSource(enum.Enum):
        File = 0
        SolutionResult = 1
    

    class OverlapResolution(enum.Enum):
        Maximum = 0
        Minimum = 1
        Average = 2
    

    class MoveOperation(enum.Enum):
        ReverseOrder = 0
        MoveUp = 1
        MoveDown = 2
    

    class MatchByType(enum.Enum):
        Name = 0
        Index = 1
    

    class EditOperation(enum.Enum):
        Active = 0
        Visible = 1
        Output = 2
    

class DurSpecialistTemperatureSource(NXObject):
    def __init__(self) -> None: ...


class DurSpecialistTemperatureLoadListBuilder(Builder):
    def __init__(self) -> None: ...
    def SetLoadTags(self, loadTags: typing.List[TaggedObject]) -> None:
        ...


class DurSpecialistTemperatureLoadBuilder(Builder):
    def __init__(self) -> None: ...
    def ClearSelectedGroups(self) -> None:
        ...
    def SetSelectedGroups(self, selectedGroups: typing.List[NXObject]) -> None:
        ...
    def SetSelectedSelectionRecipes(self, selectedSelRecipes: typing.List[NXObject]) -> None:
        ...
    def GetFileName(self) -> str:
        ...
    def SetFile(self, fileName: str, type: CAE.DurSpecialistDataSources.FileFormat) -> None:
        ...
    def PlotChannelDataCurve(self, deviceIndex: int, viewIndex: int) -> None:
        ...
    EnumLoadSource: CAE.DurSpecialistTemperatureLoadBuilder.LoadSource
    EnumLoadType: CAE.DurSpecialistTemperatureLoadBuilder.LoadType
    PropertyTable: CAE.PropertyTable
    Subcase: int


    class LoadType(enum.Enum):
        Constant = 0
        TimeHistory = 1
    

    class LoadSource(enum.Enum):
        Field = 0
        File = 1
    

class DurSpecialistTemperatureLoad(NXObject):
    def __init__(self) -> None: ...


class DurSpecialistSuperpositionEventBuilder(Builder):
    def __init__(self) -> None: ...
    def GetStaticLoad(self, modeIndex: int, scaleFactor: float) -> None:
        ...
    def SetStaticLoad(self, modeIndex: int, scaleFactor: float) -> None:
        ...
    def AddConnection(self, loadIndex: int, modeIndex: int, active: bool, scaleFactor: float) -> int:
        ...
    def DeleteConnection(self, connectionIndex: int) -> None:
        ...
    def UpdateConnection(self, connectionIndex: int, active: bool, scaleFactor: float) -> None:
        ...
    def UpdateUnitLoad(self, connectionIndex: int, unitLoad: str) -> None:
        ...
    Acceleration: Expression
    Angle: Expression
    AngularAcceleration: Expression
    AngularVelocity: Expression
    CaseSensitive: bool
    Description: str
    FeResults: CAE.DurSpecialistDataSources
    FieldFind: int
    FieldFindUsing: str
    FieldMatchUsing: str
    FieldMatchWith: int
    Find: str
    FindIn: CAE.DurSpecialistSuperpositionEventBuilder.FindInType
    Force: Expression
    HistoryEndTreatment: CAE.DurSpecialistSuperpositionEventBuilder.HistoryEndTreatmentType
    IgnoreSpecialCharacters: bool
    Length: Expression
    LoadHistories: CAE.DurSpecialistDataSources
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    ManualMatchBy: CAE.DurSpecialistSuperpositionEventBuilder.ManualMatchByType
    MatchBy: CAE.DurSpecialistSuperpositionEventBuilder.MatchByType
    MatchUsing: CAE.DurSpecialistSuperpositionEventBuilder.MatchUsingType
    MatchWith: str
    Matching: CAE.DurSpecialistSuperpositionEventBuilder.MatchingType
    MatchingUpdate: CAE.DurSpecialistEvent.UpdateCriterionType
    MaxLength: int
    MinLength: int
    Moment: Expression
    Name: str
    NumStaticLoadScales: int
    PreStressCase: int
    PreStressIncluded: bool
    PreStressScale: Expression
    PreStressUpdate: CAE.DurSpecialistEvent.UpdateCriterionType
    Pressure: Expression
    Range: CAE.DurSpecialistSuperpositionEventBuilder.RangeType
    RangeEnd: Expression
    RangeStart: Expression
    StaticLoadUpdate: CAE.DurSpecialistEvent.UpdateCriterionType
    TemperatureSource: CAE.DurSpecialistTemperatureSource
    UseMaxLength: bool
    UseMinLength: bool
    Velocity: Expression


    class RangeType(enum.Enum):
        FullHistory = 0
        SubRange = 1
    

    class MatchUsingType(enum.Enum):
        CompleteSubstring = 0
        Field = 1
        Pattern = 2
        SubstringOfSpecifiedLength = 3
    

    class MatchingType(enum.Enum):
        Automatic = 0
        Manual = 1
    

    class MatchByType(enum.Enum):
        Name = 0
        Index = 1
    

    class ManualMatchByType(enum.Enum):
        Name = 0
        Order = 1
    

    class HistoryEndTreatmentType(enum.Enum):
        Truncate = 0
        FillWithLastValue = 1
        Repeat = 2
    

    class FindInType(enum.Enum):
        LoadHistories = 0
        Subcases = 1
    

class DurSpecialistSuperpositionEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistStrainGageDispAttr(NXObject):
    def __init__(self) -> None: ...
    DisplayName: bool
    Scale: Expression


class DurSpecialistStrainGageCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistStrainGage]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateStrainGageBuilder(self, eventObject: CAE.DurSpecialistStrainGage) -> CAE.DurSpecialistStrainGageBuilder:
        ...
    def StrainGageInformationWindow(self, gage: CAE.DurSpecialistStrainGage) -> None:
        ...
    def InformationWindow(self) -> None:
        ...
    def FindObject(self, name: str) -> CAE.DurSpecialistStrainGage:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistStrainGageBuilder(Builder):
    def __init__(self) -> None: ...
    Csys: SmartObject
    Description: str
    GageType: CAE.DurspStrainGageType
    Name: str
    Placement: CAE.DurspStrainGagePlacementType
    Plane: CAE.DurspStrainGageOrientationPlane
    RotationAngle: Expression
    SelectedElementFaces: CAE.SelectFEElemFaceList
    SelectedNode: CAE.SelectFENodeList
    ShellElementFace: CAE.DurspStrainGageShellElementFaceType


class DurSpecialistStrainGage(DisplayableObject):
    def __init__(self) -> None: ...
    def GetDisplayAttribute(self) -> CAE.DurSpecialistStrainGageDispAttr:
        ...
    def Rename(self, title: str) -> None:
        ...


class DurSpecialistSolverProfileCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistSolverProfile]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, neutralName: str) -> CAE.DurSpecialistSolverProfile:
        ...
    def CreateSolverProfileBuilder(self, paramType: int) -> CAE.DurSpecialistSolverProfileBuilder:
        ...
    def CreateSolverProfileEditBuilder(self, solverProfile: CAE.DurSpecialistSolverProfile) -> CAE.DurSpecialistSolverProfileBuilder:
        ...
    def CreateSolverProfileInspectBuilder(self, solverProfile: CAE.DurSpecialistSolverProfile) -> CAE.DurSpecialistSolverProfileBuilder:
        ...
    def FindOrCreateObject(self, parameterTag: ParamLibParameter) -> CAE.DurSpecialistSolverProfile:
        ...
    def GetUsage(self, solverProfile: CAE.DurSpecialistSolverProfile, objectTags: typing.List[NXObject]) -> None:
        ...
    def Information(self, solverProfile: CAE.DurSpecialistSolverProfile) -> None:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistSolverProfileBuilder(ParamLibParameterBuilder):
    def __init__(self) -> None: ...
    ParameterTable: CAE.DurSpecialistSolverParameterTable


class DurSpecialistSolverProfile(NXObject):
    def __init__(self) -> None: ...
    def Synchronize(self) -> None:
        ...
    Parameter: ParamLibParameter


class DurSpecialistSolverParameterTable(NXObject):
    def __init__(self) -> None: ...
    def AddObject(self, parameterObject: CAE.DurSpecialistParameterObject) -> int:
        ...
    def RemoveObject(self, parameterObject: CAE.DurSpecialistParameterObject) -> int:
        ...
    def MoveUp(self, parameterObject: CAE.DurSpecialistParameterObject, numberObjects: int) -> int:
        ...
    def MoveDown(self, parameterObject: CAE.DurSpecialistParameterObject, numberObjects: int) -> int:
        ...
    def InformationWindow(self) -> None:
        ...
    def Include(self, parameterObject: CAE.DurSpecialistParameterObject) -> bool:
        ...
    def Find(self, journalIdentifier: str) -> CAE.DurSpecialistSolverParameter:
        ...


class DurSpecialistSolverParameter(TaggedObject):
    def __init__(self) -> None: ...
    def GetObjectType(self) -> str:
        ...
    def InformationWindow(self) -> None:
        ...
    ParameterObject: CAE.DurSpecialistParameterObject


class DurSpecialistSolveBuilder(Builder):
    def __init__(self) -> None: ...
    def GetCommitNoSolve(self) -> bool:
        ...
    def SetCommitNoSolve(self, flag: bool) -> None:
        ...
    FunctionResultsOnly: bool
    ModelCheck: bool
    SolverParameters: CAE.DurSpecialistSolverParameterTable
    SolverProfile: CAE.DurSpecialistSolverProfile
    SubmitOptions: CAE.DurSpecialistSolveBuilder.SubmitOptionsEnum


    class SubmitOptionsEnum(enum.Enum):
        Solve = 0
        WriteSolverInputFile = 1
        SolveInputFile = 2
    

class DurSpecialistSolutionSelectorBuilder(Builder):
    def __init__(self) -> None: ...
    Solution: CAE.SimSolution


class DurSpecialistSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistSolution]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurSpecialistSolution:
        ...
    def CreateSpecialistSolutionBuilder(self, solution: CAE.DurSpecialistSolution) -> CAE.DurSpecialistSolutionBuilder:
        ...
    def CreateResultToggles(self) -> CAE.DurSpecialistResultTableToggles:
        ...
    def CreateResultSetup(self) -> CAE.DurSpecialistResultTableSetup:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def Reset(self) -> None:
        ...
    def PlotMaterialCurve(self, type: CAE.DurSpecialistSolutionBuilder.PlotCurve, deviceIndex: int, viewIndex: int) -> int:
        """[Obsolete("Deprecated in NX1984.0.0.  Use CAE.DurSpecialistSolutionBuilder.PlotMaterial instead.")"""
        ...
    def PlotMaterial(self, type: CAE.DurSpecialistSolutionBuilder.PlotMaterialType, deviceIndex: int, viewIndex: int) -> int:
        ...
    AnalysisType: CAE.DurSpecialistAnalysisType
    Event: NXObject
    MaterialSource: CAE.DurSpecialistSolutionBuilder.MaterialSourceType
    Name: str
    SelectedMaterial: PhysicalMaterial
    SimulationObjects: CAE.DurSpecialistSimulationObjectTable


    class PlotMaterialType(enum.Enum):
        StressLifeSNCurve = 0
        StrainLifePlots = 1
        StressStrainCurve = 2
        StrainLifeENCurve = 3
    

    class PlotCurve(enum.Enum):
        StressLife = 0
        StrainLife = 1
        RambergOsgood = 2
        MansonCoffinMorrow = 3
    

    class MaterialSourceType(enum.Enum):
        InheritFromSimulation = 0
        MaterialLibrary = 1
    

class DurSpecialistSolution(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, title: str) -> None:
        ...
    def CloneSolution(self) -> CAE.DurSpecialistSolution:
        ...
    def Activate(self, activityStatus: bool) -> None:
        ...
    def Solve(self, solveOption: CAE.DurSpecialistSolution.SolveOption, check: bool) -> None:
        ...
    def Check(self) -> None:
        ...
    def InformationWindow(self) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def ExportResultsCsv(self, resultFileName: str, exportFileName: str, setup: CAE.DurSpecialistResultTableSetup) -> None:
        ...
    def ExportCsv(self, resultFileName: str, exportFileName: str, toggles: CAE.DurSpecialistResultTableToggles) -> None:
        ...
    def SetEvent(self, eventObject: CAE.DurSpecialistEvent) -> None:
        ...
    def ResultDataSource(self, newObject: bool) -> CAE.DurSpecialistResultDataSource:
        ...
    def CleanOutOfDateResultDataSources(self) -> None:
        ...
    def SetResult(self, dataSource: CAE.DataSource) -> None:
        ...
    LocalDefinitions: CAE.DurSpecialistLocalDefinitionCollection
    FunctionDefinitions: CAE.DurSpecialistFunctionDefinitionCollection
    SimulationObjects: CAE.DurSpecialistSimulationObjectTable
    SolverParameters: str


    class SolveOption(enum.Enum):
        Solve = 0
        WriteSolverInputFile = 1
        SolveInputFile = 2
    

class DurSpecialistSimulationObjectTable(NXObject):
    def __init__(self) -> None: ...
    def RemoveObjectType(self, neutralName: str) -> int:
        ...
    def AddObjectType(self, neutralName: str) -> int:
        ...
    def AddObject(self, parameterObject: CAE.DurSpecialistParameterObject) -> int:
        ...
    def GetNumSimulationObjects(self) -> int:
        ...
    def GetSimulationObject(self, index: int) -> CAE.DurSpecialistSimulationObject:
        ...
    def Find(self, neutralName: str) -> CAE.DurSpecialistSimulationObject:
        ...
    def InformationWindow(self) -> None:
        ...
    MaterialNeeded: bool


class DurSpecialistSimulationObject(TaggedObject):
    def __init__(self) -> None: ...
    def GetObjectType(self) -> str:
        ...
    def SetObjectType(self, type: str) -> None:
        ...
    def InformationWindow(self) -> None:
        ...
    IsInherited: bool
    ParameterObject: CAE.DurSpecialistParameterObject


class DurSpecialistResultTableToggles(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    ToggleAccumulatedEventResults: bool
    ToggleCyclicFatigueDamage: bool
    ToggleDesignLoadFactor: bool
    ToggleEvent: bool
    ToggleFatigueLife: bool
    ToggleFatigueLifetime: bool
    ToggleLocalDefinition: bool
    ToggleMaxStressAmplitude: bool
    ToggleMeanStress: bool
    ToggleMinSafetyFactor: bool
    ToggleRepeatedEventResults: bool
    ToggleResultStep: bool
    ToggleSingleEventResults: bool


class DurSpecialistResultTableSetup(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def ApplyResultTypes(self, resultTypes: typing.List[CAE.DurSpecialistResultTableSetup.ResultType]) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    ToggleAccumulatedEventResults: bool
    ToggleEvent: bool
    ToggleLocalDefinition: bool
    ToggleRepeatedEventResults: bool
    ToggleResultStep: bool
    ToggleSingleEventResults: bool


    class ResultType(enum.Enum):
        CyclicFatigueDamage = 0
        FatigueLife = 1
        FatigueLifetime = 2
        Mileage = 3
        MaxStressAmplitude = 4
        MaxStress = 5
        MinStress = 6
        MeanStress = 7
        StaticSafetyFactor = 8
        DesignLifeFactor = 9
        DesignLoadFactor = 10
        DurabilityFailureType = 11
        MinEnergyReleaseRate = 12
        MaxEnergyReleaseRate = 13
        MeanEnergyReleaseRate = 14
        MaxEnergyReleaseRateAmplitude = 15
        EquivalentEnergyReleaseRate = 16
        DegradationFactor = 17
        EquivalentLife = 18
        StressReductionFactor = 19
        StiffnessReduction2D = 20
        StiffnessReduction3D = 21
        AccumulatedDamage = 22
        DurabilitySafetyFactor = 23
        CombinedSafetyFactor = 24
        CombinedSafetyFactorCalculated = 25
        MaxTemperature = 26
        MinTemperature = 27
    

class DurSpecialistResultDataSource(TaggedObject):
    def __init__(self) -> None: ...


class DurSpecialistRandomEventBuilder(Builder):
    def __init__(self) -> None: ...
    DataSource: NXObject
    Description: str
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    Name: str
    Option: CAE.DurSpecialistRandomEventBuilder.OptionType
    Scaling: Expression
    TemperatureSource: CAE.DurSpecialistTemperatureSource


    class OptionType(enum.Enum):
        Dirlik = 0
        Narrow = 1
        Equivalent = 2
    

class DurSpecialistRandomEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistPlotMaterialBuilder(Builder):
    def __init__(self) -> None: ...
    def SetTemperatureFilter(self, filters: float) -> None:
        ...
    def PlotMaterialCurve(self, deviceIndex: int, viewIndex: int, isOverlay: bool) -> int:
        ...
    MansonCoffinMorrow: bool
    PlotTypeEnum: CAE.DurSpecialistPlotMaterialBuilder.PlotType
    RambergOsgood: bool
    SelectedMaterial: PhysicalMaterial
    StrainLifeCurve: bool
    StressStrainCurve: bool


    class PlotType(enum.Enum):
        StressLife = 0
        StrainLife = 1
    

class DurSpecialistParameterObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistParameterObject]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, neutralName: str) -> CAE.DurSpecialistParameterObject:
        ...
    def GetUsage(self, parameterObject: CAE.DurSpecialistParameterObject, objectTags: typing.List[NXObject]) -> None:
        ...
    def RemoveUsages(self, parameterObject: CAE.DurSpecialistParameterObject) -> None:
        ...
    def FindOrCreate(self, paramTag: ParamLibParameter) -> CAE.DurSpecialistParameterObject:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistParameterObject(TaggedObject):
    def __init__(self) -> None: ...
    Parameter: ParamLibParameter


class DurSpecialistMpfSubcaseLink(TaggedObject):
    def __init__(self) -> None: ...


class DurSpecialistMpfDataSource(CAE.DurSpecialistDataSource):
    def __init__(self) -> None: ...


class DurSpecialistMaterialToolBuilder(Builder):
    def __init__(self) -> None: ...
    def IsUltimateTensileStrengthDefined(self, materialTag: PhysicalMaterial) -> bool:
        ...
    def IsYoungsModulusDefined(self, materialTag: PhysicalMaterial) -> bool:
        ...
    CreateMaterialInFem: bool
    CreatedMaterial: PhysicalMaterial
    EnumDefinitionType: CAE.DurSpecialistMaterialToolBuilder.DefinitionType
    EnumULawMaterialType: CAE.DurSpecialistMaterialToolBuilder.ULawMaterialType
    EnumULawTensileStrength: CAE.DurSpecialistMaterialToolBuilder.ULawTensileStrength
    EnumULawYoungsModulus: CAE.DurSpecialistMaterialToolBuilder.ULawYoungsModulus
    EnumUSlopeMaterialType: CAE.DurSpecialistMaterialToolBuilder.USlopeMaterialType
    EnumUSlopeTensileStrength: CAE.DurSpecialistMaterialToolBuilder.USlopeTensileStrength
    ExpressionULawTensileStrength: Expression
    ExpressionULawYoungsModulus: Expression
    ExpressionUSlopeTensileStrength: Expression
    LoadNotchStrainRelation: CAE.DurSpecialistSimulationObjectTable
    Name: str
    SourceMaterial: PhysicalMaterial
    StrainLifeDamage: CAE.DurSpecialistSimulationObjectTable


    class USlopeTensileStrength(enum.Enum):
        InheritFromMaterial = 0
        Specify = 1
    

    class USlopeMaterialType(enum.Enum):
        Steel = 0
        SteelFKMConservative = 1
        IronCasts = 2
        IronCastsFKMConservative = 3
        Aluminum = 4
        Magnesium = 5
        AluminumMagnesiumFKMConservative = 6
        Titanium = 7
        CopperNickel = 8
    

    class ULawYoungsModulus(enum.Enum):
        InheritFromMaterial = 0
        Specify = 1
    

    class ULawTensileStrength(enum.Enum):
        InheritFromMaterial = 0
        Specify = 1
    

    class ULawMaterialType(enum.Enum):
        Steel = 0
        Aluminum = 1
        GrayCast = 2
    

    class DefinitionType(enum.Enum):
        UniversalSlope = 0
        UniversalMaterialLaw = 1
        SyntheticSNCurveFromStrainLife = 2
    

class DurSpecialistManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def CreateSolveBuilder(self, durSpecialistSolTag: CAE.DurSpecialistSolution) -> CAE.DurSpecialistSolveBuilder:
        ...
    def CreateEvaluateBuilder(self, durFuncDefTag: CAE.DurSpecialistFunctionDefinition) -> CAE.DurSpecialistSolveBuilder:
        ...
    def CreateMaterialToolBuilder(self, sourceMaterialTag: PhysicalMaterial) -> CAE.DurSpecialistMaterialToolBuilder:
        ...
    def CreatePlotMaterialBuilder(self) -> CAE.DurSpecialistPlotMaterialBuilder:
        ...
    def Tag(self) -> Tag: ...

    Solutions: CAE.DurSpecialistSolutionCollection
    AnalysisTypes: CAE.DurSpecialistAnalysisTypeCollection
    ParameterObjects: CAE.DurSpecialistParameterObjectCollection
    Events: CAE.DurSpecialistEventCollection
    DurWelds: CAE.DurSpecialistDurWeldCollection
    SolverProfiles: CAE.DurSpecialistSolverProfileCollection
    StrainGages: CAE.DurSpecialistStrainGageCollection
    VibrationDataSources: CAE.DurSpecialistVibrationDataSourceCollection
    VibrationInputDefinitions: CAE.DurSpecialistVibrationInputDefinitionCollection
    CorrelationInputDefinitions: CAE.DurSpecialistCorrelationInputDefinitionCollection
    HarmonicDataSources: CAE.DurSpecialistHarmonicDataSourceCollection
    TemperatureSources: CAE.DurSpecialistTemperatureSourceCollection


class DurSpecialistLocalDefinitionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistLocalDefinition]:
        ...
    def __init__(self, owner: CAE.DurSpecialistSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurSpecialistLocalDefinition:
        ...
    def CreateLocalDefinitionBuilder(self, localDefinition: CAE.DurSpecialistLocalDefinition) -> CAE.DurSpecialistLocalDefinitionBuilder:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistLocalDefinitionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def ClearSelectedGroups(self) -> None:
        ...
    def SetSelectedGroups(self, selectedGroups: typing.List[NXObject]) -> None:
        ...
    def ClearSelectedSelectionRecipes(self) -> None:
        ...
    def SetSelectedSelectionRecipes(self, selectedSelRecipes: typing.List[NXObject]) -> None:
        ...
    def SetSelectedSeamWeldSets(self, selectedSets: typing.List[NXObject]) -> None:
        ...
    def SetSelectedSpotWeldSets(self, selectedSets: typing.List[NXObject]) -> None:
        ...
    def Reset(self) -> None:
        ...
    def GetActiveAnalysisType(self) -> CAE.DurSpecialistAnalysisType:
        ...
    def PlotMaterialCurve(self, type: CAE.DurSpecialistLocalDefinitionBuilder.PlotCurve, deviceIndex: int, viewIndex: int) -> int:
        """[Obsolete("Deprecated in NX1984.0.0.  Use CAE.DurSpecialistLocalDefinitionBuilder.PlotMaterial instead.")"""
        ...
    def PlotMaterial(self, type: CAE.DurSpecialistLocalDefinitionBuilder.PlotMaterialType, deviceIndex: int, viewIndex: int) -> int:
        ...
    AnalysisType: CAE.DurSpecialistAnalysisType
    IsAnalysisTypeInherited: bool
    IsMaterialInherited: bool
    Location: CAE.DurSpecialistLocalDefinitionBuilder.LocationType
    MaterialSource: CAE.DurSpecialistSolutionBuilder.MaterialSourceType
    Name: str
    SelectElements: CAE.SelectElementsBuilder
    SelectedMaterial: PhysicalMaterial
    SelectionType: int
    SimulationObjects: CAE.DurSpecialistSimulationObjectTable


    class PlotMaterialType(enum.Enum):
        StressLifeSNCurve = 0
        StrainLifePlots = 1
        StressStrainCurve = 2
        StrainLifeENCurve = 3
    

    class PlotCurve(enum.Enum):
        StressLife = 0
        StrainLife = 1
        RambergOsgood = 2
        MansonCoffinMorrow = 3
    

    class LocationType(enum.Enum):
        Elements = 0
        Groups = 1
        SeamWelds = 2
        SpotWelds = 3
        RemainingStructure = 4
        AllModel = 5
        None = 6
    

class DurSpecialistLocalDefinition(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, title: str) -> None:
        ...
    def CloneLocalDefinition(self) -> CAE.DurSpecialistLocalDefinition:
        ...
    def Activate(self, activity: bool) -> None:
        ...
    def InformationWindow(self) -> None:
        ...
    SimulationObjects: CAE.DurSpecialistSimulationObjectTable


class DurSpecialistLoadLengthBuilder(Builder):
    def __init__(self) -> None: ...
    Distance: Expression
    DistanceType: CAE.DurSpecialistLoadLengthBuilder.Definition
    Duration: Expression
    DurationType: CAE.DurSpecialistLoadLengthBuilder.Definition


    class Definition(enum.Enum):
        Implicit = 0
        Imposed = 1
        NotAvailable = 2
    

class DurSpecialistLoadLength(TaggedObject):
    def __init__(self) -> None: ...


class DurSpecialistLoadEventListBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEventTags(self, eventTags: typing.List[TaggedObject]) -> None:
        ...


class DurSpecialistHarmonicEventBuilder(Builder):
    def __init__(self) -> None: ...
    DataSource: NXObject
    Description: str
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    Name: str
    Scaling: Expression
    TemperatureSource: CAE.DurSpecialistTemperatureSource


class DurSpecialistHarmonicEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistHarmonicDataSourceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistHarmonicDataSource]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateHarmonicDataSourceBuilder(self, dataSource: CAE.DurSpecialistHarmonicDataSource) -> CAE.DurSpecialistHarmonicDataSourceBuilder:
        ...
    def InformationWindow(self) -> None:
        ...
    def CloneHarmonicDataSource(self, sourceHarmonicDataSource: CAE.DurSpecialistHarmonicDataSource) -> CAE.DurSpecialistHarmonicDataSource:
        ...
    def DeleteHarmonicDataSource(self, theHarmonicDataSource: CAE.DurSpecialistHarmonicDataSource) -> None:
        ...
    def Rename(self, theHarmonicDataSource: CAE.DurSpecialistHarmonicDataSource, name: str) -> None:
        ...
    def HarmonicDataSourceInformationWindow(self, theHarmonicDataSource: CAE.DurSpecialistHarmonicDataSource) -> None:
        ...
    def FindObject(self, name: str) -> CAE.DurSpecialistHarmonicDataSource:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistHarmonicDataSourceBuilder(Builder):
    def __init__(self) -> None: ...
    def AddVibrationInputDefinition(self, vid: CAE.DurSpecialistVibrationInputDefinition) -> None:
        ...
    def GetNumberMPFSubcases(self) -> int:
        ...
    def GetNthMPFSubcaseIndex(self, nth: int) -> int:
        ...
    def GetNthMPFSubcase(self, nth: int) -> CAE.DurSpecialistMpfSubcaseLink:
        ...
    def GetNthMPFSubcaseName(self, nth: int) -> str:
        ...
    def UpdateMpfVibrationInputDefinitionByFile(self, mpfFilePath: str) -> None:
        ...
    def UpdateMpfVibrationInputDefinitionByModeSet(self, modeSet: CAE.ModeSet) -> None:
        ...
    def AdjustMpfVibrationInputDefinitionBCTypes(self) -> int:
        ...
    def CreateNewMultipleExpressions(self) -> None:
        ...
    def UpdateNthFrequency(self, nth: int) -> None:
        ...
    def UpdateFrequencyFromSelection(self, nth: int) -> None:
        ...
    def AddFrequency(self) -> None:
        ...
    def RemoveFrequencies(self, indexes: int) -> None:
        ...
    Description: str
    Duration: Expression
    DurationMultiple: Expression
    EndFrequency: Expression
    EndFrequencyMultiple: Expression
    FFLoadType: CAE.DurSpecialistHarmonicDataSourceBuilder.LoadType
    FFSineSweepType: CAE.DurSpecialistHarmonicDataSourceBuilder.SineSweepType
    FilePath: str
    Frequency: Expression
    FrequencyMultiple: Expression
    FrequencyOpt: CAE.DurSpecialistHarmonicDataSourceBuilder.FrequencyOption
    ModeSet: CAE.ModeSet
    ModeType: CAE.DurSpecialistVibrationDataSourceBuilder.ModeType
    MpfSource: CAE.DurSpecialistHarmonicDataSourceBuilder.Source
    Name: str
    StartFrequency: Expression
    StartFrequencyMultiple: Expression
    Step: Expression


    class Source(enum.Enum):
        File = 0
        ModeSet = 1
    

    class SineSweepType(enum.Enum):
        Linear = 0
        Logarithmic = 1
    

    class LoadType(enum.Enum):
        SineSweep = 0
        SineDwell = 1
    

    class FrequencyOption(enum.Enum):
        Single = 0
        Multiple = 1
    

class DurSpecialistHarmonicDataSource(NXObject):
    def __init__(self) -> None: ...
    def RemoveVibrationInputDefinition(self, vid: CAE.DurSpecialistVibrationInputDefinition) -> None:
        ...
    def HarmonicInputsInformation(self) -> None:
        ...
    def ClearVibrationInputDefinitions(self) -> None:
        ...
    def RenameVibrationInputDefinition(self, vid: CAE.DurSpecialistVibrationInputDefinition, name: str) -> None:
        ...


class DurSpecialistFunctionDefinitionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistFunctionDefinition]:
        ...
    def __init__(self, owner: CAE.DurSpecialistSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurSpecialistFunctionDefinition:
        ...
    def CreateFunctionDefinitionBuilderFromSolution(self, functionDefinition: CAE.DurSpecialistFunctionDefinition) -> CAE.DurSpecialistFunctionDefinitionBuilder:
        ...
    def CreateFunctionDefinitionBuilderFromLocalDefinition(self, localDefTag: CAE.DurSpecialistLocalDefinition, functionDefinition: CAE.DurSpecialistFunctionDefinition) -> CAE.DurSpecialistFunctionDefinitionBuilder:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistFunctionDefinitionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetName(self) -> str:
        ...
    def SetName(self, title: str) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def GetLocationType(self) -> CAE.DurSpecialistFunctionDefinitionBuilder.LocationType:
        ...
    def SetLocationType(self, type: CAE.DurSpecialistFunctionDefinitionBuilder.LocationType) -> None:
        ...
    def GetSimulationObjects(self) -> CAE.DurSpecialistSimulationObjectTable:
        ...
    def ClearSelectedElements(self) -> None:
        ...
    def SetSelectedElements(self, elements: typing.List[CAE.FEElement], selectionRecipes: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    def ClearSelectedElementGroups(self) -> None:
        ...
    def SetSelectedElementGroups(self, selectedGroups: typing.List[NXObject]) -> None:
        ...
    def ClearSelectedElementSelectionRecipes(self) -> None:
        ...
    def SetSelectedElementSelectionRecipes(self, selectedElemSelRecipes: typing.List[NXObject]) -> None:
        ...
    def ClearSelectedNodes(self) -> None:
        ...
    def SetSelectedNodes(self, elements: typing.List[CAE.FENode], selectionRecipes: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    def ClearSelectedNodeGroups(self) -> None:
        ...
    def SetSelectedNodeGroups(self, selectedGroups: typing.List[NXObject]) -> None:
        ...
    def ClearSelectedNodeSelectionRecipes(self) -> None:
        ...
    def SetSelectedNodeSelectionRecipes(self, selectedNodeSelRecipes: typing.List[NXObject]) -> None:
        ...
    def ClearSelectedStrainGages(self) -> None:
        ...
    def SetSelectedStrainGages(self, selectedStrainGages: typing.List[NXObject]) -> None:
        ...
    def Reset(self) -> None:
        ...
    def RemoveObject(self, selObj: str) -> None:
        ...


    class LocationType(enum.Enum):
        Elements = 0
        ElementGroups = 1
        Nodes = 2
        NodeGroups = 3
        StrainGages = 4
    

class DurSpecialistFunctionDefinition(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, title: str) -> None:
        ...
    def CloneFunctionDefinition(self) -> CAE.DurSpecialistFunctionDefinition:
        ...
    def FunctionDefinition(self) -> None:
        ...
    def InformationWindow(self) -> None:
        ...
    def ResultDataSource(self, newObject: bool) -> CAE.DurSpecialistResultDataSource:
        ...
    def CleanOutOfDateResultDataSources(self) -> None:
        ...
    def SetResult(self, dataSource: CAE.DataSource) -> None:
        ...
    ResultReader: CAE.DurSpecialistDataSource
    SimulationObjects: CAE.DurSpecialistSimulationObjectTable


class DurSpecialistFunctionDataSource(CAE.DurSpecialistDataSource):
    def __init__(self) -> None: ...


class DurSpecialistFlexBodyEventBuilder(Builder):
    def __init__(self) -> None: ...
    def GetMotionFileName(self) -> str:
        ...
    def SetMotionFileName(self, fileName: str) -> None:
        ...
    def GetSolutions(self) -> typing.List[Motion.MotionSolution]:
        ...
    def GetFlexBodies(self) -> typing.List[Motion.FlexBody]:
        ...
    Description: str
    FlexBody: Motion.FlexBody
    IntervalEnd: Expression
    IntervalStart: Expression
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    Name: str
    Range: CAE.DurSpecialistFlexBodyEventBuilder.RangeType
    Solution: Motion.MotionSolution
    TemperatureSource: CAE.DurSpecialistTemperatureSource


    class RangeType(enum.Enum):
        FullHistory = 0
        SubRange = 1
    

class DurSpecialistFlexBodyEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistEventCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistEvent]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurSpecialistEvent:
        ...
    def CreateLoadEventListBuilder(self) -> CAE.DurSpecialistLoadEventListBuilder:
        ...
    def CreateBlockLoadEventBuilder(self, eventObject: CAE.DurSpecialistBlockLoadEvent) -> CAE.DurSpecialistBlockLoadEventBuilder:
        ...
    def CreateSuperpositionEventBuilder(self, eventObject: CAE.DurSpecialistSuperpositionEvent) -> CAE.DurSpecialistSuperpositionEventBuilder:
        ...
    def CreateTransientEventBuilder(self, eventObject: CAE.DurSpecialistTransientEvent) -> CAE.DurSpecialistTransientEventBuilder:
        ...
    def CreateDutyCycleEventBuilder(self, eventObject: CAE.DurSpecialistDutyCycleEvent) -> CAE.DurSpecialistDutyCycleEventBuilder:
        ...
    def CreateFlexBodyEventBuilder(self, eventObject: CAE.DurSpecialistFlexBodyEvent) -> CAE.DurSpecialistFlexBodyEventBuilder:
        ...
    def CreateSolutionSelectorBuilder(self, solutionObject: CAE.SimSolution, eventType: CAE.DurSpecialistEvent.EventType) -> CAE.DurSpecialistSolutionSelectorBuilder:
        ...
    def CreateRandomEventBuilder(self, eventObject: CAE.DurSpecialistRandomEvent) -> CAE.DurSpecialistRandomEventBuilder:
        ...
    def InformationWindow(self) -> None:
        ...
    def CloneEvent(self, sourceEvent: CAE.DurSpecialistEvent) -> CAE.DurSpecialistEvent:
        ...
    def DeleteEvent(self, theEvent: CAE.DurSpecialistEvent) -> None:
        ...
    def Rename(self, theEvent: CAE.DurSpecialistEvent, name: str) -> None:
        ...
    def GetEventDescription(self, theEvent: CAE.DurSpecialistEvent) -> str:
        ...
    def SetEventDescription(self, theEvent: CAE.DurSpecialistEvent, description: str) -> None:
        ...
    def EventInformationWindow(self, theEvent: CAE.DurSpecialistEvent) -> None:
        ...
    def CreateAutoDutyCycleBuilder(self) -> CAE.DurSpecialistAutoDutyCycleBuilder:
        ...
    def CreateHarmonicEventBuilder(self, eventObject: CAE.DurSpecialistHarmonicEvent) -> CAE.DurSpecialistHarmonicEventBuilder:
        ...
    def SuperpositionEventFromFlexibleBodyEvent(self, sourceEvent: CAE.DurSpecialistFlexBodyEvent) -> CAE.DurSpecialistSuperpositionEvent:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistEvent(NXObject):
    def __init__(self) -> None: ...


    class UpdateCriterionType(enum.Enum):
        ByName = 0
        ByIndex = 1
    

    class SelectionCriterionType(enum.Enum):
        Dummy = 0
    

    class EventType(enum.Enum):
        Superposition = 0
        BlockLoad = 1
        FlexBody = 2
        Transient = 3
        DutyCycle = 4
        Random = 5
        Harmonic = 6
    

class DurSpecialistDutyCycleEventBuilder(Builder):
    def __init__(self) -> None: ...
    def AddEventData(self, newEvent: CAE.DurSpecialistEvent) -> None:
        ...
    def EditEventData(self, indexes: int, operation: CAE.DurSpecialistDutyCycleEventBuilder.Operation, repetitions: Expression) -> None:
        ...
    def SetUseOrder(self, useOrder: bool) -> None:
        ...
    Description: str
    Name: str
    Repetitions: Expression


    class OperationError(enum.Enum):
        None = 0
        Circular = 1
        InvalidRepetitions = 2
    

    class Operation(enum.Enum):
        Remove = 0
        MoveUp = 1
        MoveDown = 2
        Activate = 3
        Deactivate = 4
        Repetitions = 5
    

class DurSpecialistDutyCycleEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistDurWeldSetBuilder(Builder):
    def __init__(self) -> None: ...
    def GetSelectedWeldConnections(self) -> typing.List[CAE.Connections.IConnection]:
        ...
    def SetSelectedWeldConnections(self, selectedWeldConnections: typing.List[CAE.Connections.IConnection]) -> None:
        ...
    def GetDurWelds(self) -> typing.List[CAE.DurSpecialistDurWeld]:
        ...
    def SetDurWelds(self, durWelds: typing.List[CAE.DurSpecialistDurWeld]) -> None:
        ...
    AllowOverride: bool
    DescriptionString: str
    DurWeldSetType: CAE.DurSpecialistDurWeldSetBuilder.Type
    NameString: str
    RecoverySimulationObject: CAE.DurSpecialistSimulationObjectTable


    class Type(enum.Enum):
        SeamWeld = 0
        SpotWeld = 1
    

class DurSpecialistDurWeldSet(NXObject):
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> INXObject:
        ...
    def MoveDurWeld(self, durWelds: typing.List[CAE.DurSpecialistDurWeld], durWeldToSet: CAE.DurSpecialistDurWeldSet) -> None:
        ...
    def RemoveDurWelds(self, durWelds: typing.List[CAE.DurSpecialistDurWeld]) -> None:
        ...


class DurSpecialistDurWeldCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistDurWeldSet]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurSpecialistDurWeldSet:
        ...
    def CreateSeamWeldBuilder(self, durWeld: CAE.DurSpecialistDurWeld) -> CAE.DurSpecialistDurSeamWeldBuilder:
        ...
    def CreateSpotWeldBuilder(self, durWeld: CAE.DurSpecialistDurWeld) -> CAE.DurSpecialistDurSpotWeldBuilder:
        ...
    def CreateSeamWeldSetBuilder(self, durWeldSet: CAE.DurSpecialistDurWeldSet) -> CAE.DurSpecialistDurSeamWeldSetBuilder:
        ...
    def CreateSpotWeldSetBuilder(self, durWeldSet: CAE.DurSpecialistDurWeldSet) -> CAE.DurSpecialistDurSpotWeldSetBuilder:
        ...
    def FindOrCreateSet(self, neutralName: str, isOrphanSet: bool, type: CAE.DurSpecialistDurWeldSetBuilder.Type) -> CAE.DurSpecialistDurWeldSet:
        ...
    def CloneSet(self, tOldSet: CAE.DurSpecialistDurWeldSet, suggestedName: str) -> CAE.DurSpecialistDurWeldSet:
        ...
    def ExtractOrphanSet(self, tSet: CAE.DurSpecialistDurWeldSet, suggestedName: str) -> CAE.DurSpecialistDurWeldSet:
        ...
    def DeleteSet(self, tSet: CAE.DurSpecialistDurWeldSet) -> None:
        ...
    def ImportWeldFromXMcf(self, propertyList: CAE.CaeDataContainer) -> typing.List[CAE.Connections.IConnection]:
        ...
    def ExportWeldToXMcf(self, connections: typing.List[CAE.Connections.IConnection], propertyList: CAE.CaeDataContainer) -> None:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistDurWeldBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescriptionMultiString(self) -> str:
        ...
    def SetDescriptionMultiString(self, descriptionMultiString: str) -> None:
        ...
    CustomSimulationObject: CAE.DurSpecialistSimulationObjectTable
    DurWeldSet: CAE.DurSpecialistDurWeldSet
    NameString: str
    RecoverySimulationObject: CAE.DurSpecialistSimulationObjectTable
    WeldConnection: CAE.Connections.IConnection


class DurSpecialistDurWeld(NXObject):
    def __init__(self) -> None: ...
    Active: bool


class DurSpecialistDurSpotWeldSetBuilder(CAE.DurSpecialistDurWeldSetBuilder):
    def __init__(self) -> None: ...


class DurSpecialistDurSpotWeldSet(CAE.DurSpecialistDurWeldSet):
    def __init__(self) -> None: ...


class DurSpecialistDurSpotWeldBuilder(CAE.DurSpecialistDurWeldBuilder):
    def __init__(self) -> None: ...


class DurSpecialistDurSpotWeld(CAE.DurSpecialistDurWeld):
    def __init__(self) -> None: ...


class DurSpecialistDurSeamWeldSetBuilder(CAE.DurSpecialistDurWeldSetBuilder):
    def __init__(self) -> None: ...


class DurSpecialistDurSeamWeldSet(CAE.DurSpecialistDurWeldSet):
    def __init__(self) -> None: ...


class DurSpecialistDurSeamWeldBuilder(CAE.DurSpecialistDurWeldBuilder):
    def __init__(self) -> None: ...


class DurSpecialistDurSeamWeld(CAE.DurSpecialistDurWeld):
    def __init__(self) -> None: ...


class DurSpecialistDataSources(TaggedObject):
    def __init__(self) -> None: ...
    def AddDataSource(self, fileName: str, driver: CAE.DurSpecialistDataSources.FileFormat) -> int:
        ...
    def AddSolution(self, sol: CAE.SimSolution) -> int:
        ...
    def ReplaceDataSourceWithSolution(self, fileIndex: int, sol: CAE.SimSolution) -> None:
        ...
    def RemoveDataSource(self, fileIndex: int) -> None:
        ...
    def GetDataSourceUnitSystem(self, fileIndex: int) -> CAE.DurSpecialistDataSources.UnitSystem:
        ...
    def SetDataSourceUnitSystem(self, fileIndex: int, unitSystem: CAE.DurSpecialistDataSources.UnitSystem) -> None:
        ...
    def InformationWindow(self, fileIndex: int) -> None:
        ...
    def PlotLoadHistories(self, fileIndex: int, loadHistoriesIndexes: int, deviceIndex: int, viewIndex: int, plotType: CAE.DurSpecialistDataSources.XyPlotType) -> None:
        ...
    def SwapDataSource(self, dataSource1: CAE.DurSpecialistDataSource, dataSource2: CAE.DurSpecialistDataSource) -> None:
        ...
    def SetChannelsActivity(self, fileIndex: int, loadHistoryIndices: int, activity: bool) -> None:
        ...
    def CopyTransientLoadStatus(self, dataSourceSrc: CAE.DurSpecialistDataSource, dataSourceDes: CAE.DurSpecialistDataSource) -> None:
        ...
    def GetNthDataSource(self, index: int) -> CAE.DurSpecialistDataSource:
        ...
    def GetDataSourceTemperatureUnitSystem(self, fileIndex: int) -> CAE.DurSpecialistDataSources.TemperatureUnitSystem:
        ...
    def SetDataSourceTemperatureUnitSystem(self, fileIndex: int, unitSystem: CAE.DurSpecialistDataSources.TemperatureUnitSystem) -> None:
        ...


    class XyPlotType(enum.Enum):
        Plot2D = 0
        Plot2DInStack = 1
        Plot2DOverlay = 2
    

    class UnitSystem(enum.Enum):
        Implicit = 0
        MillinewtonMillimeter = 1
        NewtonMeter = 2
        NewtonMillimeter = 3
        CentinewtonCentimeter = 4
        KgfMeter = 5
        KgfMillimeter = 6
        LbfFoot = 7
        LbfInch = 8
        PoundalFoot = 9
    

    class TemperatureUnitSystem(enum.Enum):
        Implicit = 0
        Celsius = 1
        Fahrenheit = 2
        Kelvin = 3
        Rankine = 4
    

    class FileFormat(enum.Enum):
        NastranResult = 0
        TestLab = 1
        UniversalFile = 2
        MotionResult = 3
        SamcefResult = 4
        AbaqusResult = 5
        Tecware = 6
        AnsysResult = 7
        SCHDF5File = 8
        SCD5File = 9
    

class DurSpecialistDataSource(TaggedObject):
    def __init__(self) -> None: ...


class DurSpecialistCorrelationInputDefinitionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistCorrelationInputDefinition]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateDurSpecialistCorrelationInputDefinitionBuilder(self, inputDef: CAE.DurSpecialistCorrelationInputDefinition) -> CAE.DurSpecialistCorrelationInputDefinitionBuilder:
        ...
    def FindObject(self, name: str) -> CAE.DurSpecialistCorrelationInputDefinition:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistCorrelationInputDefinitionBuilder(Builder):
    def __init__(self) -> None: ...
    DataSourceBuilder: CAE.DurSpecialistVibrationDataSourceBuilder
    Description: str
    FromDOF: CAE.DurSpecialistCorrelationInputDefinitionBuilder.Dof
    FromNode: CAE.FENode
    FromVibrationInputDefinition: CAE.DurSpecialistVibrationInputDefinition
    Function: CAE.Function
    Name: str
    ToDOF: CAE.DurSpecialistCorrelationInputDefinitionBuilder.Dof
    ToNode: CAE.FENode
    ToVibrationInputDefinition: CAE.DurSpecialistVibrationInputDefinition


    class Dof(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        Rx = 3
        Ry = 4
        Rz = 5
    

class DurSpecialistCorrelationInputDefinition(NXObject):
    def __init__(self) -> None: ...
    def InformationWindow(self) -> None:
        ...


class DurSpecialistBlockLoadEventBuilder(Builder):
    def __init__(self) -> None: ...
    def GetUnitSystem(self) -> CAE.DurSpecialistDataSources.UnitSystem:
        ...
    def SetUnitSystem(self, unitSystem: CAE.DurSpecialistDataSources.UnitSystem) -> None:
        ...
    def GetFileName(self) -> str:
        ...
    def SetFile(self, fileName: str, type: CAE.DurSpecialistDataSources.FileFormat) -> None:
        ...
    def SetSolution(self, sol: CAE.SimSolution) -> None:
        ...
    DataSourceType: CAE.DurSpecialistDataSources.FileFormat
    Description: str
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    LowerValue: Expression
    ModeSelection: CAE.DurSpecialistEvent.UpdateCriterionType
    Name: str
    Pattern: CAE.DurSpecialistBlockLoadEventBuilder.PatternType
    Source: CAE.DurSpecialistBlockLoadEventBuilder.ResultSource
    StartWithLower: bool
    Subcase: int
    TemperatureSource: CAE.DurSpecialistTemperatureSource
    UpperValue: Expression


    class ResultSource(enum.Enum):
        Solution = 0
        File = 1
    

    class PatternType(enum.Enum):
        Swelling = 0
        Alternating = 1
        Free = 2
    

class DurSpecialistBlockLoadEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistAutoDutyCycleBuilder(Builder):
    def __init__(self) -> None: ...
    Description: str
    Event: NXObject
    Filename: str
    Folder: str
    Name: str
    OrderOption: int


class DurSpecialistAnalysisTypeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistAnalysisType]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, neutralName: str) -> CAE.DurSpecialistAnalysisType:
        ...
    def CreateAnalysisTypeBuilder(self, paramType: int) -> CAE.DurSpecialistAnalysisTypeBuilder:
        ...
    def CreateAnalysisTypeEditBuilder(self, analysisType: CAE.DurSpecialistAnalysisType) -> CAE.DurSpecialistAnalysisTypeBuilder:
        ...
    def CreateAnalysisTypeInspectBuilder(self, analysisType: CAE.DurSpecialistAnalysisType) -> CAE.DurSpecialistAnalysisTypeBuilder:
        ...
    def FindOrCreateObject(self, parameterTag: ParamLibParameter) -> CAE.DurSpecialistAnalysisType:
        ...
    def GetUsage(self, analysisType: CAE.DurSpecialistAnalysisType, objectTags: typing.List[NXObject]) -> None:
        ...
    def Information(self, analysisType: CAE.DurSpecialistAnalysisType) -> None:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistAnalysisTypeBuilder(ParamLibParameterBuilder):
    def __init__(self) -> None: ...
    Implicit: CAE.DurSpecialistSimulationObjectTable
    Optional: CAE.DurSpecialistSimulationObjectTable
    Required: CAE.DurSpecialistSimulationObjectTable


class DurSpecialistAnalysisType(NXObject):
    def __init__(self) -> None: ...
    def IsTypeRequired(self, type: str) -> bool:
        ...
    def IsTypeOptional(self, type: str) -> bool:
        ...
    def IsTypeImplicit(self, type: str) -> bool:
        ...
    def GetSimulationObject(self, type: str) -> CAE.DurSpecialistSimulationObject:
        ...
    def Synchronize(self) -> None:
        ...
    Parameter: ParamLibParameter


class DurabilityTransientEventBuilder(CAE.DurabilityEventBuilder):
    def __init__(self) -> None: ...
    def GetNthSubcase(self, index: int) -> int:
        ...
    def SetNthSubcase(self, index: int, nthSubcase: int) -> None:
        ...
    DataControl: CAE.DurabilityDataControlBuilder
    MdfFileName: str
    Sort2Access: bool
    StaticOffset: NXObject
    Subcase: int


class DurabilityTransientEvent(CAE.DurabilityEvent):
    def __init__(self) -> None: ...


class DurabilityStressAxesBuilder(Builder):
    def __init__(self) -> None: ...
    BeamStress: CAE.DurabilityStressAxesBuilder.BeamStressEnum
    ElementFaceStressAxis: CAE.DurabilityStressAxesBuilder.ElementFaceStressAxisEnum
    Name: str
    NodeElementOption: CAE.DurabilityStressAxesBuilder.NodeElementOptionEnum
    SearchResolution: Expression
    ShellRegion: CAE.DurabilityStressAxesBuilder.ShellRegionEnum
    StressAxisDirectionSearchMethod: CAE.DurabilityStressAxesBuilder.StressAxisDirectionSearchMethodEnum
    StressAxisMethod: CAE.DurabilityStressAxesBuilder.StressAxisMethodEnum
    StressDirection: Direction


    class StressAxisMethodEnum(enum.Enum):
        ElementFace = 0
        NodalUniAxial = 1
    

    class StressAxisDirectionSearchMethodEnum(enum.Enum):
        CriticalPlane = 0
        MaximumDamage = 1
        PrincipalAxis = 2
    

    class ShellRegionEnum(enum.Enum):
        Bottom = 0
        Middle = 1
        Top = 2
    

    class NodeElementOptionEnum(enum.Enum):
        Solids = 0
        Shells = 1
    

    class ElementFaceStressAxisEnum(enum.Enum):
        BiAxial = 0
        UniAxial = 1
    

    class BeamStressEnum(enum.Enum):
        Axial = 0
        Torsional = 1
        None = 2
    

class DurabilityStrengthCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilityStrength]:
        ...
    def __init__(self, owner: CAE.DurabilityManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilityStrength:
        ...
    def CreateEventstrengthsettingsBuilder(self, eventstrengthsettings: CAE.DurabilityStrength) -> CAE.DurabilityEventStrengthSettingsBuilder:
        ...
    def DeleteStrength(self, eventstrengthsettings: CAE.DurabilityStrength) -> None:
        ...
    def CloneStrength(self, source: CAE.DurabilityStrength) -> CAE.DurabilityStrength:
        ...
    def Tag(self) -> Tag: ...



class DurabilityStrength(NXObject):
    def __init__(self) -> None: ...


class DurabilityStrainGageAnalyzerBuilder(Builder):
    def __init__(self) -> None: ...
    def UseStrainGageData(self, prefixName: str, name: str, afuName: str, numRecords: int, index1: int, index2: int, index3: int) -> None:
        ...
    AbsoluteMaximumPrincipalAngle: bool
    AbsoluteMaximumPrincipalStrain: bool
    AbsoluteMaximumPrincipalStress: bool
    AbsoluteMaximumShearStrain: bool
    AbsoluteMaximumShearStress: bool
    AxisDirectionSearchMethod: CAE.DurabilityStrainGageAnalyzerBuilder.AxisDirectionSearchMethodEnum
    BiaxialityRatioHistory: bool
    CriticalPlaneOption: CAE.DurabilityStrainGageAnalyzerBuilder.CriticalPlaneOptionEnum
    EffectiveStrain: bool
    EffectiveStress: bool
    GageConstruction: CAE.DurabilityStrainGageAnalyzerBuilder.GageConstructionEnum
    GagePoissonRatio: float
    GageSource: CAE.DurabilityStrainGageAnalyzerBuilder.GageSourceEnum
    GageType: CAE.DurabilityStrainGageAnalyzerBuilder.GageTypeEnum
    Kt1: float
    Kt2: float
    Kt3: float
    MaterialTag: PhysicalMaterial
    MaximumPrincipalAngle: bool
    MaximumPrincipalStrain: bool
    MaximumPrincipalStress: bool
    MaximumShearStrain: bool
    MaximumShearStress: bool
    SearchResolution: Expression
    SignedVonMisesStress: bool
    TargetFileName: str
    UseEffectiveBiaxialityRatio: bool
    VonMisesStress: bool


    class GageTypeEnum(enum.Enum):
        Rectangular = 0
        Delta = 1
        Tee = 2
    

    class GageSourceEnum(enum.Enum):
        Response = 0
        Afu = 1
    

    class GageConstructionEnum(enum.Enum):
        Stacked = 0
        Planar = 1
        User = 2
    

    class CriticalPlaneOptionEnum(enum.Enum):
        MaximumShear = 0
        MaximumPrincipal = 1
    

    class AxisDirectionSearchMethodEnum(enum.Enum):
        CriticalPlane = 0
        PrincipalAxis = 1
    

class DurabilityStaticEventBuilder(CAE.DurabilityEventBuilder):
    def __init__(self) -> None: ...
    ExcitationType: CAE.DurabilityStaticEventBuilder.ExcitationTypeEnum


    class ExcitationTypeEnum(enum.Enum):
        Pattern = 0
        ResultPath = 1
        Function = 2
    

class DurabilityStaticEvent(CAE.DurabilityEvent):
    def __init__(self) -> None: ...
    Excitations: CAE.DurabilityExcitationCollection


class DurabilitySolverBuilder(Builder):
    def __init__(self) -> None: ...
    ActiveEventSolveOptions: CAE.DurabilitySolverBuilder.ActiveEventSolveOptionsEnum
    CreateDiagnosticGroups: bool
    ModelCheck: bool
    SaveGeometry: bool
    SubmitOptions: CAE.DurabilitySolverBuilder.SubmitOptionsEnum


    class SubmitOptionsEnum(enum.Enum):
        Solve = 0
    

    class ActiveEventSolveOptionsEnum(enum.Enum):
        Unsolved = 0
        All = 1
    

class DurabilitySolveOptionsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilitySolveOptions]:
        ...
    def __init__(self, owner: CAE.DurabilityManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilitySolveOptions:
        ...
    def CreateEventoverridesBuilder(self, eventoverrides: CAE.DurabilitySolveOptions) -> CAE.DurabilityEventOverridesBuilder:
        ...
    def DeleteSolveoptions(self, eventoverrides: CAE.DurabilitySolveOptions) -> None:
        ...
    def CloneSolveoptions(self, source: CAE.DurabilitySolveOptions) -> CAE.DurabilitySolveOptions:
        ...
    def Tag(self) -> Tag: ...



class DurabilitySolveOptions(NXObject):
    def __init__(self) -> None: ...


class DurabilityResultsReportBuilder(Builder):
    def __init__(self) -> None: ...
    def ExportResultsToCsv(self, csvFilename: str) -> None:
        ...
    EventDamage: bool
    EventLife: bool
    FailureIndex: bool
    FatigueSafetyFactor: bool
    FreeFaceIndicator: bool
    LoadProportionality: bool
    MarginSafety: bool
    PrincipalAxisStability: bool
    StrengthSafetyFactor: bool
    UseEvents: CAE.DurabilityResultsReportBuilder.UseEventsEnum
    UseHighlight: bool


    class UseEventsEnum(enum.Enum):
        Active = 0
        All = 1
    

class DurabilityResultPathBuilder(CAE.DurabilityExcitationBuilder):
    def __init__(self) -> None: ...
    def AddLoadcase(self, loadcase: int) -> None:
        ...
    def AddIteration(self, iteration: int) -> None:
        ...
    def SetScale(self, index: int, scale: float) -> None:
        ...
    def MoveLoadcaseUp(self, index: int) -> None:
        ...
    def MoveLoadcaseDown(self, index: int) -> None:
        ...
    def RemoveLoadcase(self, index: int) -> None:
        ...


class DurabilityResultPath(CAE.DurabilityExcitation):
    def __init__(self) -> None: ...


class DurabilityRandomFatigueCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilityRandomFatigue]:
        ...
    def __init__(self, owner: CAE.DurabilityManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilityRandomFatigue:
        ...
    def CreateRandomfatigueBuilder(self, randomFatigue: CAE.DurabilityRandomFatigue) -> CAE.DurabilityRandomFatigueBuilder:
        ...
    def DeleteRandomFatigue(self, randomFatigue: CAE.DurabilityRandomFatigue) -> None:
        ...
    def CloneRandomFatigue(self, source: CAE.DurabilityRandomFatigue) -> CAE.DurabilityRandomFatigue:
        ...
    def Tag(self) -> Tag: ...



class DurabilityRandomFatigueBuilder(Builder):
    def __init__(self) -> None: ...
    EventDamage: bool
    EventLife: bool
    Name: str
    RandomEventDuration: Expression
    RandomFatigueMethod: CAE.DurabilityRandomFatigueBuilder.RandomFatigueMethodEnum


    class RandomFatigueMethodEnum(enum.Enum):
        NarrowBandMiles = 0
        WideBandDirlik = 1
    

class DurabilityRandomFatigue(NXObject):
    def __init__(self) -> None: ...


class DurabilityRandomEventBuilder(CAE.DurabilityEventBuilder):
    def __init__(self) -> None: ...
    def SetRandomfatigue(self, randomFatigue: CAE.DurabilityRandomFatigue) -> None:
        ...
    Subcase: int


class DurabilityRandomEvent(CAE.DurabilityEvent):
    def __init__(self) -> None: ...


class DurabilityMetaSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilityMetaSolution]:
        ...
    def __init__(self, owner: CAE.DurabilityManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilityMetaSolution:
        ...
    def CreateMetasolutionBuilder(self, metasolution: CAE.DurabilityMetaSolution) -> CAE.DurabilityMetaSolutionBuilder:
        ...
    def DeleteMetasolution(self, metasolution: CAE.DurabilityMetaSolution) -> None:
        ...
    def CloneMetasolution(self, source: CAE.DurabilityMetaSolution) -> CAE.DurabilityMetaSolution:
        ...
    def SetActiveMetasolution(self, source: CAE.DurabilityMetaSolution) -> None:
        ...
    def Tag(self) -> Tag: ...



class DurabilityMetaSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    MetaSolutionName: str


class DurabilityMetaSolution(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...
    def Check(self) -> None:
        ...
    Events: CAE.DurabilityEventCollection


class DurabilityManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def CreateSolverBuilder(self, durabilityTag: CAE.DurabilityMetaSolution) -> CAE.DurabilitySolverBuilder:
        ...
    def CreateEventSolverBuilder(self, eventTag: CAE.DurabilityEvent) -> CAE.DurabilityEventSolverBuilder:
        ...
    def CreateDamageEvaluationBuilder(self) -> CAE.DurabilityDamageEvaluationBuilder:
        ...
    def CreateStrainGageAnalyzerBuilder(self) -> CAE.DurabilityStrainGageAnalyzerBuilder:
        ...
    def CreateDurabilityEvaluateFatigueHistoryBuilder(self, eventTag: CAE.DurabilityEvent) -> CAE.DurabilityEvaluateFatigueHistoryBuilder:
        ...
    def CreateDurabilityResultsReportBuilder(self, durabilityTag: CAE.DurabilityMetaSolution) -> CAE.DurabilityResultsReportBuilder:
        ...
    def Tag(self) -> Tag: ...

    MetaSolutions: CAE.DurabilityMetaSolutionCollection
    StrengthCollection: CAE.DurabilityStrengthCollection
    FatigueCollection: CAE.DurabilityFatigueCollection
    RandomFatigueCollection: CAE.DurabilityRandomFatigueCollection
    AxisSearchCollection: CAE.DurabilityAxisSearchCollection
    SolveOptionsCollection: CAE.DurabilitySolveOptionsCollection


class DurabilityLoadPatternBuilder(CAE.DurabilityExcitationBuilder):
    def __init__(self) -> None: ...
    Iteration: int
    Loadcase: int
    Offset: float
    PatternType: CAE.DurabilityLoadPatternBuilder.PatternTypeEnum
    Scale: float


    class PatternTypeEnum(enum.Enum):
        HalfSineWave = 0
        FullSineWave = 1
    

class DurabilityLoadPattern(CAE.DurabilityExcitation):
    def __init__(self) -> None: ...


class DurabilityFunctionExcitationBuilder(CAE.DurabilityExcitationBuilder):
    def __init__(self) -> None: ...
    Function: TaggedObject
    Iteration: int
    Loadcase: int
    Offset: float
    Scale: float


class DurabilityFunctionExcitation(CAE.DurabilityExcitation):
    def __init__(self) -> None: ...


class DurabilityFatigueCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilityFatigue]:
        ...
    def __init__(self, owner: CAE.DurabilityManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilityFatigue:
        ...
    def CreateEventfatiguesettingsBuilder(self, eventfatiguesettings: CAE.DurabilityFatigue) -> CAE.DurabilityEventFatigueSettingsBuilder:
        ...
    def DeleteFatigue(self, eventfatiguesettings: CAE.DurabilityFatigue) -> None:
        ...
    def CloneFatigue(self, source: CAE.DurabilityFatigue) -> CAE.DurabilityFatigue:
        ...
    def Tag(self) -> Tag: ...



class DurabilityFatigue(NXObject):
    def __init__(self) -> None: ...


class DurabilityExcitationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilityExcitation]:
        ...
    def __init__(self, owner: CAE.DurabilityStaticEvent) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilityExcitation:
        ...
    def DeleteExcitation(self, excitationTag: CAE.DurabilityExcitation) -> None:
        ...
    def CloneExcitation(self, source: CAE.DurabilityExcitation) -> CAE.DurabilityExcitation:
        ...
    def CreateLoadPatternBuilder(self, loadPattern: CAE.DurabilityLoadPattern) -> CAE.DurabilityLoadPatternBuilder:
        ...
    def CreateResultPathBuilder(self, resultPath: CAE.DurabilityResultPath) -> CAE.DurabilityResultPathBuilder:
        ...
    def CreateFunctionExcitationBuilder(self, resultPath: CAE.DurabilityFunctionExcitation) -> CAE.DurabilityFunctionExcitationBuilder:
        ...
    def Tag(self) -> Tag: ...



class DurabilityExcitationBuilder(Builder):
    def __init__(self) -> None: ...
    ExcitationName: str


class DurabilityExcitation(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...


class DurabilityEventStrengthSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    FactorOfSafety: float
    MarginOfSafety: bool
    Name: str
    OrthotropicFailureCriterion: CAE.DurabilityEventStrengthSettingsBuilder.OrthotropicFailureCriterionEnum
    PerformOrthotropicAnalysis: bool
    StrengthSafetyFactor: bool
    StressCriterion: CAE.DurabilityEventStrengthSettingsBuilder.StressCriterionEnum
    StressType: CAE.DurabilityEventStrengthSettingsBuilder.StressTypeEnum


    class StressTypeEnum(enum.Enum):
        VonMises = 0
        Tresca = 1
        MaximumPrincipal = 2
        MinimumPrincipal = 3
    

    class StressCriterionEnum(enum.Enum):
        UltimateStress = 0
        YieldStress = 1
    

    class OrthotropicFailureCriterionEnum(enum.Enum):
        Hill = 0
        Hoffman = 1
        TsaiWu = 2
        MaximumStress = 3
    

class DurabilityEventSolverBuilder(Builder):
    def __init__(self) -> None: ...
    CreateDiagnosticGroups: bool
    ModelCheck: bool
    SaveGeometry: bool
    SubmitOptions: CAE.DurabilityEventSolverBuilder.SubmitOptionsEnum


    class SubmitOptionsEnum(enum.Enum):
        Solve = 0
    

class DurabilityEventOverridesBuilder(Builder):
    def __init__(self) -> None: ...
    DefaultMaterialTemperature: Expression
    Elements: CAE.SelectElementsBuilder
    MaterialTag: PhysicalMaterial
    Name: str
    OverrideMaterial: bool
    UseElements: CAE.DurabilityEventOverridesBuilder.UseElementsEnum
    UseNonLinear: bool


    class UseElementsEnum(enum.Enum):
        All = 0
        Select = 1
    

class DurabilityEventFatigueSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    BwiWeldClass: CAE.DurabilityEventFatigueSettingsBuilder.BwiWeldClassEnum
    CyclesToFailure: float
    CyclicStressStrainModel: CAE.DurabilityEventFatigueSettingsBuilder.CyclicStressStrainModelEnum
    EquivalentStressMethod: CAE.DurabilityEventFatigueSettingsBuilder.EquivalentStressMethodEnum
    EventDamage: bool
    EventDamageDirection: bool
    EventLife: bool
    FailureIndex: bool
    FatigueLifeCriterion: CAE.DurabilityEventFatigueSettingsBuilder.FatigueLifeCriterionEnum
    FatigueSafetyFactorKeyin: float
    FatigueSafetyFactorMethod: CAE.DurabilityEventFatigueSettingsBuilder.FatigueSafetyFactorMethodEnum
    FatigueSafetyFactorOutput: CAE.DurabilityEventFatigueSettingsBuilder.FatigueSafetyFactorOutputEnum
    FatigueSafetyFactorToggle: bool
    FreeFaceIndicator: bool
    IncludeMeanStressEffects: bool
    LoadProportionality: bool
    MaximumAlternatingStress: CAE.DurabilityEventFatigueSettingsBuilder.MaximumAlternatingStressEnum
    MaximumAlternatingStressKeyin: Expression
    Name: str
    NotchFactor: float
    NumberOfElementsInHysterisisLoop: int
    NumberOfOccurrences: int
    NumberOfStandardDeviations: float
    OrthotropicFatigueCriterion: CAE.DurabilityEventFatigueSettingsBuilder.OrthotropicFatigueCriterionEnum
    OrthotropicMeanStress: CAE.DurabilityEventFatigueSettingsBuilder.OrthotropicMeanStressEnum
    PerformOrthotropicAnalysis: bool
    PlateThicknessExponent: float
    PlateThicknessRatio: float
    PrincipalAxisStability: bool
    ProbabilityOfFailure: float
    ProbabilityOption: CAE.DurabilityEventFatigueSettingsBuilder.ProbabilityOptionEnum
    TwiHighCycleCutoff: float
    TwiHighCycleSlopeChange: float
    TwiLowCycleStressCutoff: float
    TwiLowCycleStressExtension: float
    UseNotchFactor: bool
    UsePlateThicknessCorrection: bool


    class ProbabilityOptionEnum(enum.Enum):
        NumberOfStandardDeviations = 0
        ProbabilityOfFailure = 1
    

    class OrthotropicMeanStressEnum(enum.Enum):
        None = 0
        Goodman = 1
        Gerber = 2
        Morrow = 3
    

    class OrthotropicFatigueCriterionEnum(enum.Enum):
        Hill = 0
        TsaiWu = 1
        MaximumStress = 2
    

    class MaximumAlternatingStressEnum(enum.Enum):
        Calculate = 0
        Keyin = 1
    

    class FatigueSafetyFactorOutputEnum(enum.Enum):
        Goodman = 0
        Gerber = 1
        DangVan = 2
    

    class FatigueSafetyFactorMethodEnum(enum.Enum):
        AmplitudeandMean = 0
        Amplitude = 1
        Mean = 2
    

    class FatigueLifeCriterionEnum(enum.Enum):
        SmithWatsonTopper = 0
        StrainLifeMaximumPrincipal = 1
        StrainLifeMaximumShear = 2
        StressLife = 3
        Bwi = 4
        Twi = 5
    

    class EquivalentStressMethodEnum(enum.Enum):
        None = 0
        Goodman = 1
        Soderberg = 2
        Gerber = 3
        Morrow = 4
    

    class CyclicStressStrainModelEnum(enum.Enum):
        Linear = 0
        PowerHardening = 1
        RambergOsgood = 2
    

    class BwiWeldClassEnum(enum.Enum):
        B = 0
        C = 1
        D = 2
        E = 3
        F = 4
        F2 = 5
        G = 6
        W = 7
    

class DurabilityEventCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilityEvent]:
        ...
    def __init__(self, owner: CAE.DurabilityMetaSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilityEvent:
        ...
    def DeleteEvent(self, eventTag: CAE.DurabilityEvent) -> None:
        ...
    def CloneEvent(self, source: CAE.DurabilityEvent) -> CAE.DurabilityEvent:
        ...
    def CreateStaticEventBuilder(self, eventTag: CAE.DurabilityStaticEvent) -> CAE.DurabilityStaticEventBuilder:
        ...
    def CreateRandomEventBuilder(self, eventTag: CAE.DurabilityRandomEvent) -> CAE.DurabilityRandomEventBuilder:
        ...
    def CreateTransientEventBuilder(self, eventTag: CAE.DurabilityTransientEvent) -> CAE.DurabilityTransientEventBuilder:
        ...
    def Tag(self) -> Tag: ...



class DurabilityEventBuilder(Builder):
    def __init__(self) -> None: ...
    def SetStrength(self, strength: CAE.DurabilityStrength) -> None:
        ...
    def SetFatigue(self, fatigue: CAE.DurabilityFatigue) -> None:
        ...
    def SetAxissearch(self, axisSearch: CAE.DurabilityAxisSearch) -> None:
        ...
    def SetSolveoptions(self, solveOption: CAE.DurabilitySolveOptions) -> None:
        ...
    EventName: str
    ResultSourceTag: NXObject


class DurabilityEvent(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...
    ActivityStatus: bool


class DurabilityEvaluateFatigueHistoryBuilder(Builder):
    def __init__(self) -> None: ...
    def EditEvent(self) -> None:
        ...
    def AfuFunction(self) -> None:
        ...
    def ExportFatigueHistoryToCsv(self, csvFilename: str) -> None:
        ...
    FatigueHistoryDataType: CAE.DurabilityEvaluateFatigueHistoryBuilder.FatigueHistoryDataTypeEnum
    OutputAfuFileName: str


    class FatigueHistoryDataTypeEnum(enum.Enum):
        AsPerEvent = 0
        Stress = 1
        Strain = 2
    

class DurabilityDataControlBuilder(TaggedObject):
    def __init__(self) -> None: ...
    DecimationOrder: int
    OutputEndTime: Expression
    OutputStartTime: Expression
    PeakValleyTolerance: float
    TimeExtents: CAE.DurabilityDataControlBuilder.TimeExtentsEnum


    class TimeExtentsEnum(enum.Enum):
        FromParentResult = 0
        Specify = 1
    

class DurabilityDamageEvaluationBuilder(Builder):
    def __init__(self) -> None: ...
    def GetNthNominalRangeBin(self, index: int) -> float:
        ...
    def SetNthNominalRangeBin(self, index: int, nthNominalRangeBin: float) -> None:
        ...
    def GetNthMeanBin(self, index: int) -> float:
        ...
    def SetNthMeanBin(self, index: int, nthMeanBin: float) -> None:
        ...
    def ExportResultsToCsv(self, csvFilename: str) -> None:
        ...
    def SetFunctionData(self, functionTag: TaggedObject, numberOfOccurrences: int, lateralLoadingFactor: float, scaleFactor: float) -> None:
        ...
    def RemoveFunction(self, rowIndex: int) -> None:
        ...
    def SetLlr(self, rowIndex: int, lateralLoadingFactor: float) -> None:
        ...
    def SetScale(self, rowIndex: int, scale: float) -> None:
        ...
    def SetOccurrence(self, rowIndex: int, occurrence: int) -> None:
        ...
    def SetFatigue(self, fatigue: CAE.DurabilityFatigue) -> None:
        ...
    EnableDetailedOutput: bool
    HighlightDamageValues: bool
    MaterialTag: PhysicalMaterial
    MaxMeanRange: float
    MaxNominalRange: float
    MinMeanRange: float
    NumberOfMaxBins: int
    NumberOfMeanBins: int
    PeakValleyTolerance: float


    class ProbabilityOptionEnum(enum.Enum):
        NumberOfStandardDeviations = 0
        ProbabilityOfFailure = 1
    

    class FatigueLifeCriterionEnum(enum.Enum):
        SmithWatsonTopper = 0
        StrainLifeMaximumPrincipal = 1
        StrainLifeMaximumShear = 2
        StressLife = 3
        Bwi = 4
        Twi = 5
    

    class EquivalentStressMethodEnum(enum.Enum):
        None = 0
        Goodman = 1
        Soderberg = 2
        Gerberg = 3
        Morrow = 4
    

    class CyclicStressStrainModelEnum(enum.Enum):
        Linear = 0
        PowerHardening = 1
        RambergOsgood = 2
    

    class BwiWeldClassEnum(enum.Enum):
        B = 0
        C = 1
        D = 2
        E = 3
        F = 4
        F2 = 5
        G = 6
        W = 7
    

class DurabilityAxisSearchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurabilityAxisSearch]:
        ...
    def __init__(self, owner: CAE.DurabilityManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurabilityAxisSearch:
        ...
    def CreateStressaxesBuilder(self, stressaxes: CAE.DurabilityAxisSearch) -> CAE.DurabilityStressAxesBuilder:
        ...
    def DeleteAxissearch(self, stressaxes: CAE.DurabilityAxisSearch) -> None:
        ...
    def CloneAxissearch(self, source: CAE.DurabilityAxisSearch) -> CAE.DurabilityAxisSearch:
        ...
    def Tag(self) -> Tag: ...



class DurabilityAxisSearch(NXObject):
    def __init__(self) -> None: ...


class DprExciterConfig(CAE.PreTestExciterConfig):
    def __init__(self) -> None: ...
    DprNumDrivingPoints: int
    DprSortingMode: CAE.DprExciterConfig.SortingMethod


    class SortingMethod(enum.Enum):
        WeightedAverage = 0
        Average = 1
        Maximum = 2
        Minimum = 3
    

class DofTerm():
    NodeIndex: int
    DofComponent: int
    Coefficient: float
    def ToString(self) -> str:
        ...
    def __init__(self, NodeIndex: int, DofComponent: int, Coefficient: float) -> None: ...


class DisplaySectionType(enum.Enum):
    None = 0
    Curves = 1
    Solid = 2


class DisplayNodalCsysBuilder(Builder):
    def __init__(self) -> None: ...
    def GetColorXAxis(self) -> NXColor:
        ...
    def SetColorXAxis(self, xAxisColor: NXColor) -> None:
        ...
    def GetColorYAxis(self) -> NXColor:
        ...
    def SetColorYAxis(self, yAxisColor: NXColor) -> None:
        ...
    def GetColorZAxis(self) -> NXColor:
        ...
    def SetColorZAxis(self, zAxisColor: NXColor) -> None:
        ...
    CsysTypeEnum: CAE.DisplayNodalCsysBuilder.DisplayNodalCsysType
    NodeSelector: CAE.SelectFENodeList
    SelectionTypeEnum: CAE.DisplayNodalCsysBuilder.NodesToDisplayType


    class NodesToDisplayType(enum.Enum):
        EntireModel = 0
        SelectedNodes = 1
    

    class DisplayNodalCsysType(enum.Enum):
        Displacement = 0
        Reference = 1
    

class DirectionalityFieldBuilder(Builder):
    def __init__(self) -> None: ...
    Entities: SelectTaggedObjectList
    EntitiesSelectionType: CAE.DirectionalityFieldBuilder.SelectionType
    Solution: CAE.SimSolution
    SpatialMappingAxis: CoordinateSystem
    SpatialMappingType: CAE.DirectionalityFieldBuilder.SpatialMapType
    SubcaseIndex: int
    SubcaseSelection: CAE.DirectionalityFieldBuilder.SubcaseSelectionType


    class SubcaseSelectionType(enum.Enum):
        First = 0
        Last = 1
        Index = 2
    

    class SpatialMapType(enum.Enum):
        Global = 0
        Local = 1
    

    class SelectionType(enum.Enum):
        Nodes = 0
        SelectionRecipe = 1
    

class DestinationCollectorBuilder(TaggedObject):
    def __init__(self) -> None: ...
    AutomaticMode: bool
    ElementContainer: CAE.MeshCollector


class DependentMeshListItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[CAE.DependentMeshListItemBuilder]) -> None:
        ...
    def Append(self, object: CAE.DependentMeshListItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: CAE.DependentMeshListItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> CAE.DependentMeshListItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: CAE.DependentMeshListItemBuilder) -> None:
        ...
    def Erase(self, obj: CAE.DependentMeshListItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[CAE.DependentMeshListItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[CAE.DependentMeshListItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: CAE.DependentMeshListItemBuilder, object2: CAE.DependentMeshListItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: CAE.DependentMeshListItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DependentMeshListItemBuilder(NXObject):
    def __init__(self) -> None: ...
    FlipDirection: bool
    MasterEdge: SelectObject
    TargetEdge: SelectObject


class DependentMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def MatchCylinderSeams(self) -> None:
        ...
    def CheckForTinyEdges(self) -> bool:
        ...
    def CheckForSymmetry(self) -> bool:
        ...
    def CreateNewListItem(self, tMasterEdge: CAE.CAEEdge, tTargetEdge: CAE.CAEEdge, fFlipDirection: bool) -> CAE.DependentMeshListItemBuilder:
        ...
    def GetMeshType(self) -> CAE.DependentMeshBuilder.MeshType:
        ...
    def SetMeshType(self, type: CAE.DependentMeshBuilder.MeshType) -> None:
        ...
    def GetCsys(self) -> NXObject:
        ...
    def SetCsys(self, tCsys: NXObject) -> None:
        ...
    def CommitDependentMesh(self) -> CAE.Mesh2d:
        ...
    LoopList: CAE.DependentMeshListItemBuilderList
    MasterFace: CAE.SelectCAEFace
    TargetFace: CAE.SelectCAEFace


    class MeshType(enum.Enum):
        Free = 0
        Map = 1
    

class DependentMesh(CAE.Mesh2d):
    def __init__(self) -> None: ...


class DeleteUnreferencedEntitiesBuilder(Builder):
    def __init__(self) -> None: ...
    def GenerateAndQueryNumberOfDeletionCandidates(self) -> int:
        ...
    def QueryDeletionCandidateWithIndex(self, index: int) -> NXObject:
        ...
    def SetDeleteCandidateExceptions(self, deletionExceptions: typing.List[NXObject]) -> None:
        ...
    AllOptionsToggle: bool
    ConditionSequenceParametersToggle: bool
    ConstraintFoldersToggle: bool
    ConstraintsToggle: bool
    CsysToggle: bool
    FieldsToggle: bool
    FileScopeEnum: CAE.DeleteUnreferencedEntitiesBuilder.FileScopeType
    GroupsToggle: bool
    LoadFoldersToggle: bool
    LoadsToggle: bool
    MaterialsToggle: bool
    ModelingObjectsToggle: bool
    PhysicalPropertiesToggle: bool
    RegionsToggle: bool
    SelectionRecipesToggle: bool
    SimulationObjectFoldersToggle: bool
    SimulationObjectsToggle: bool
    SolutionSearchFilterEnum: CAE.DeleteUnreferencedEntitiesBuilder.SolutionSearchFilterType
    SolverSetsToggle: bool
    UserDefinedExpressionsToggle: bool


    class SolutionSearchFilterType(enum.Enum):
        UnusedbyActive = 0
        UnusedbyAll = 1
    

    class FileScopeType(enum.Enum):
        SimOnly = 0
        SimandRelatedFEMsandAFEMs = 1
    

class DeletePolygonFaceBuilder(Builder):
    def __init__(self) -> None: ...
    PolygonFaceSelect: CAE.SelectCAEFaceList


class DeformationParameters(TaggedObject):
    def __init__(self) -> None: ...
    ComplexCriterion: CAE.Result.Complex
    Component: CAE.Result.Component
    DeformationType: CAE.Result.DeformationScale
    GenericType: CAE.BaseResultType
    InitialDeformationScale: float
    InitialDeformationScaleType: CAE.Result.DeformationScale
    InitialDeformationUserDefinedResultType: CAE.BaseResultType
    InitialDeformationUserselectionType: CAE.Result.InitialDeformationSelection
    IsReferenceNode: bool
    PhaseAngle: float
    ReferenceNode: CAE.PostSelectionEntity
    ReferenceNodeLabel: int
    Scale: float
    UseShellNormalComponent: bool


class DefaultFormatHandler(TaggedObject):
    def __init__(self) -> None: ...
    DisplayName: str
    Name: str


class DataSourceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DataSource]:
        ...
    def __init__(self, owner: CAE.PostScenarioManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DataSource:
        ...
    def CreateDataSourceBuilder(self) -> CAE.DataSourceBuilder:
        ...
    def EditDataSourceBuilder(self, source: CAE.DataSource) -> CAE.DataSourceBuilder:
        ...
    def DeleteDataSource(self, source: CAE.DataSource) -> None:
        ...
    def Refresh(self) -> None:
        ...
    def CreateDemoDataSource(self, dataDefinitions: str) -> CAE.DataSource:
        ...
    def CreateMisbehavingDataSource(self, flags: int) -> CAE.DataSource:
        ...
    def Tag(self) -> Tag: ...



class DataSourceBuilder(Builder):
    def __init__(self) -> None: ...
    AvailableFormats: CAE.FormatHandlerCollection
    FormatHandler: CAE.IFormatHandler
    SourceFile: str
    SourceName: str
    SourceObject: CAE.IPostScenarioDataSource
    SourceTaggedObject: TaggedObject
    UsePreProcessingEntities: bool


class DataSource(NXObject):
    def __init__(self) -> None: ...
    def GetDefinitions(self) -> typing.List[CAE.PostScenarioDefinition]:
        ...
    def GetDefinitionByName(self, name: str) -> CAE.PostScenarioDefinition:
        ...
    def PrintInformation(self) -> None:
        ...
    def Refresh(self) -> None:
        ...
    Name: str


class DataReaderUnitCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Unit]:
        ...
    def __init__(self, owner: CAE.DataReaderOptionUnit) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> Unit:
        ...
    def Tag(self) -> Tag: ...



class DataReaderOptionUnit(CAE.DataReaderOptionBase):
    def __init__(self) -> None: ...
    def SetUnit(self, unit: Unit) -> None:
        ...
    SuggestedUnits: CAE.DataReaderUnitCollection


class DataReaderOptionString(CAE.DataReaderOptionBase):
    def __init__(self) -> None: ...
    DefaultValue: str
    Value: str


class DataReaderOptionInt(CAE.DataReaderOptionBase):
    def __init__(self) -> None: ...
    DefaultValue: int
    Value: int


class DataReaderOptionEnum(CAE.DataReaderOptionBase):
    def __init__(self) -> None: ...
    def GetChoiceByIndex(self, choiceIndex: int) -> str:
        ...
    DefaultValue: str
    NumChoices: int
    Value: str


class DataReaderOptionDouble(CAE.DataReaderOptionBase):
    def __init__(self) -> None: ...
    DefaultValue: float
    Value: float


class DataReaderOptionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DataReaderOptionBase]:
        ...
    def __init__(self, owner: CAE.DataReaderDatabaseOptions) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> CAE.DataReaderOptionBase:
        ...
    def Tag(self) -> Tag: ...



class DataReaderOptionBase(TaggedObject):
    def __init__(self) -> None: ...
    Description: str
    Name: str
    Type: CAE.DataReaderDatabaseOptions.OptionType


class DataReaderDatabaseOptions(TaggedObject):
    def __init__(self) -> None: ...
    OptionCollection: CAE.DataReaderOptionCollection


    class OptionType(enum.Enum):
        Int = 0
        Double = 1
        String = 2
        Enum = 3
        Unit = 4
        Unknown = 5
    

class DataProcessingCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DataProcessing]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DataProcessing:
        ...
    def Create(self, dataSource: CAE.DataSource) -> CAE.DataProcessing:
        ...
    def CreateBuilder(self, metasolution: CAE.DataProcessing) -> CAE.DataProcessingBuilder:
        ...
    def DeleteDataProcessing(self, metasolution: CAE.DataProcessing) -> None:
        ...
    def Tag(self) -> Tag: ...



class DataProcessingBuilder(Builder):
    def __init__(self) -> None: ...


class DataProcessingBlockCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DataProcessingBlock]:
        ...
    def __init__(self, owner: CAE.DataProcessing) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DataProcessingBlock:
        ...
    def DeleteBlock(self, blockTag: CAE.DataProcessingBlock) -> None:
        ...
    def CreateBuilder(self, propertyName: str, dataTag: NXObject) -> CAE.DataProcessingBlockBuilder:
        ...
    def Tag(self) -> Tag: ...



class DataProcessingBlockBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable


class DataProcessingBlock(NXObject):
    def __init__(self) -> None: ...
    def Process(self) -> None:
        ...


class DataProcessing(NXObject):
    def __init__(self) -> None: ...
    def Process(self) -> None:
        ...
    Blocks: CAE.DataProcessingBlockCollection


class DataMatchOverrideResult(enum.Enum):
    Override = 0
    UseDefault = 1


class DamperEADBuilder(Builder):
    def __init__(self) -> None: ...
    ComponentEndAState: CAE.DamperEADBuilder.State
    ComponentEndBState: CAE.DamperEADBuilder.State
    Elements: CAE.SelectElementsBuilder
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.DamperEADBuilder.State
    RotationalComponentEndA: CAE.DamperEADBuilder.RotationalComponentEnd
    RotationalComponentEndB: CAE.DamperEADBuilder.RotationalComponentEnd
    RotationalViscousDamping: Expression
    TranslationalComponentEndA: CAE.DamperEADBuilder.TranslationalComponentEnd
    TranslationalComponentEndB: CAE.DamperEADBuilder.TranslationalComponentEnd
    TranslationalViscousDamping: Expression
    ViscousDampingState: CAE.DamperEADBuilder.State


    class TranslationalComponentEnd(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class State(enum.Enum):
        Apply = 0
        Clear = 1
        Ignore = 2
    

    class RotationalComponentEnd(enum.Enum):
        Rx = 0
        Ry = 1
        Rz = 2
    

class CylinderFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class CylinderBoundingVolume(CAE.BoundingVolumePrimitive):
    def __init__(self) -> None: ...
    def GetCsysDiameterHeight(self, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression) -> None:
        ...
    def SetCsysDiameterHeight(self, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression) -> None:
        ...
    def GetCsysDiametersHeight(self, centerCsys: CoordinateSystem, innerDiaOption: CAE.CylinderBoundingVolume.InnerDiameter, outerDiaOption: CAE.CylinderBoundingVolume.OuterDiameter, innerDiameter: Expression, outerDiameter: Expression, cylinderHeight: Expression) -> None:
        ...
    def SetCsysDiametersHeight(self, centerCsys: CoordinateSystem, innerDiaOption: CAE.CylinderBoundingVolume.InnerDiameter, outerDiaOption: CAE.CylinderBoundingVolume.OuterDiameter, innerDiameter: Expression, outerDiameter: Expression, cylinderHeight: Expression) -> None:
        ...
    def GetCsysDiameterHeightAngles(self, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression, isStartActive: bool, startAngle: Expression, isEndActive: bool, endAngle: Expression) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CylinderBoundingVolume.GetCsysDiametersHeightsAngles which uses inner dimensions as arguments.")"""
        ...
    def SetCsysDiameterHeightAngles(self, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression, isStartActive: bool, startAngle: Expression, isEndActive: bool, endAngle: Expression) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CylinderBoundingVolume.SetCsysDiametersHeightsAngles which uses inner dimensions as arguments.")"""
        ...
    def GetCsysDiametersHeightsAngles(self, centerCsys: CoordinateSystem, innerDiameter: Expression, outerDiameter: Expression, startHeight: Expression, endHeight: Expression, startAngle: Expression, endAngle: Expression, innerDiaOption: CAE.CylinderBoundingVolume.InnerDiameter, outerDiaOption: CAE.CylinderBoundingVolume.OuterDiameter, startHeightOption: CAE.CylinderBoundingVolume.StartHeight, endHeightOption: CAE.CylinderBoundingVolume.EndHeight, startAngleOption: CAE.CylinderBoundingVolume.StartAngle, endAngleOption: CAE.CylinderBoundingVolume.EndAngle) -> None:
        ...
    def SetCsysDiametersHeightsAngles(self, centerCsys: CoordinateSystem, innerDiameter: Expression, outerDiameter: Expression, startHeight: Expression, endHeight: Expression, startAngle: Expression, endAngle: Expression, innerDiaOption: CAE.CylinderBoundingVolume.InnerDiameter, outerDiaOption: CAE.CylinderBoundingVolume.OuterDiameter, startHeightOption: CAE.CylinderBoundingVolume.StartHeight, endHeightOption: CAE.CylinderBoundingVolume.EndHeight, startAngleOption: CAE.CylinderBoundingVolume.StartAngle, endAngleOption: CAE.CylinderBoundingVolume.EndAngle) -> None:
        ...
    def GetEndpointsDiameter(self, baseCenter: Point, topCenter: Point, diameter: Expression) -> None:
        ...
    def SetEndpointsDiameter(self, baseCenter: Point, topCenter: Point, diameter: Expression) -> None:
        ...
    def GetEndpointsDiameters(self, baseCenter: Point, topCenter: Point, innerDiaOption: CAE.CylinderBoundingVolume.InnerDiameter, outerDiaOption: CAE.CylinderBoundingVolume.OuterDiameter, innerDiameter: Expression, outerDiameter: Expression) -> None:
        ...
    def SetEndpointsDiameters(self, baseCenter: Point, topCenter: Point, innerDiaOption: CAE.CylinderBoundingVolume.InnerDiameter, outerDiaOption: CAE.CylinderBoundingVolume.OuterDiameter, innerDiameter: Expression, outerDiameter: Expression) -> None:
        ...


    class StartHeight(enum.Enum):
        NotDefined = 0
        Value = 1
        PositiveInfinity = 2
        NegativeInfinity = 3
    

    class StartAngle(enum.Enum):
        NotDefined = 0
        Value = 1
    

    class OuterDiameter(enum.Enum):
        Value = 0
        Infinity = 1
    

    class InnerDiameter(enum.Enum):
        NotDefined = 0
        Value = 1
    

    class EndHeight(enum.Enum):
        Value = 0
        PositiveInfinity = 1
        NegativeInfinity = 2
    

    class EndAngle(enum.Enum):
        NotDefined = 0
        Value = 1
    

class CyclicSymmetricStageProperties(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self, elems: int) -> None:
        ...
    Axis: Point3d
    NumSectors: int
    Origin: Point3d


class CyclicSymmetricParameters(TaggedObject):
    def __init__(self) -> None: ...
    def GetSectorIndices(self, sectors: int) -> None:
        ...
    def SetSectorIndices(self, sectors: int) -> None:
        ...
    EnvValue: CAE.CyclicSymmetricParameters.EnvelopeValue
    OriginalResultOption: CAE.CyclicSymmetricParameters.OriginalResult
    ResultOption: CAE.CyclicSymmetricParameters.GetResult
    SectCriteria: CAE.CyclicSymmetricParameters.SectorCriteria
    SectorIndex: int
    SectorValue: CAE.CyclicSymmetricParameters.Value


    class Value(enum.Enum):
        Maximum = 0
        Minimum = 1
        AbsoluteMaximum = 2
        AbsoluteMinimum = 3
    

    class SectorCriteria(enum.Enum):
        Index = 0
        Value = 1
    

    class OriginalResult(enum.Enum):
        BySector = 0
        EnvelopeAcrossSectors = 1
    

    class GetResult(enum.Enum):
        OnOriginalModel = 0
        RevolvedAll = 1
        RevolvedSelectedSectors = 2
    

    class EnvelopeValue(enum.Enum):
        Maximum = 0
        Minimum = 1
        AbsoluteMaximum = 2
        AbsoluteMinimum = 3
        Average = 4
        Sum = 5
    

class CurveOperationExpressionRecordCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CurveOperationExpressionRecord]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, name: str, dataType: CAE.XyFunctionDataComplexType, formulaStrings: str) -> CAE.CurveOperationExpressionRecord:
        ...
    def Export(self, pRecords: typing.List[CAE.CurveOperationExpressionRecord], exportFilesParam: CAE.FTK.ExportFilesParameter) -> None:
        ...
    def FindObject(self, name: str) -> CAE.CurveOperationExpressionRecord:
        ...
    def Tag(self) -> Tag: ...



class CurveOperationExpressionRecord(NXObject):
    def __init__(self) -> None: ...
    def GetFormulas(self, formulaStrings: str) -> CAE.XyFunctionDataComplexType:
        ...
    def SetFormulas(self, dataType: CAE.XyFunctionDataComplexType, formulaStrings: str) -> None:
        ...
    def Evaluate(self) -> CAE.FTK.ArrayRecord2D:
        ...
    def Copy(self, name: str) -> CAE.CurveOperationExpressionRecord:
        ...
    Description: str
    Name: str


class CurveOperationDataSource(NXObject):
    def __init__(self) -> None: ...
    Description: str
    Identifier: str


class CurveOperation(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def EvaluateCurveExpressionStrings(self, recordName: str, dataType: CAE.XyFunctionDataComplexType, curveExpressionStrings: str) -> CAE.FTK.ArrayRecord2D:
        ...
    def ValidateCurveExpressionString(self, curveExpressionString: str, isNeedToPrintErrorMessages: bool) -> None:
        ...
    def CreatePlot(self, deviceIndex: int, viewIndex: int, arrayRecord: CAE.FTK.ArrayRecord2D) -> CAE.Xyplot.Plot:
        ...
    def AskDataSource(self, context: NXObject, identifier: str) -> CAE.CurveOperationDataSource:
        ...
    def AskAllDataSources(self, context: NXObject, dataSources: typing.List[CAE.CurveOperationDataSource]) -> None:
        ...
    def NewExportFilesParameters(self) -> CAE.FTK.ExportFilesParameter:
        ...
    def Tag(self) -> Tag: ...



class CrossSectionParameters(TaggedObject):
    def __init__(self) -> None: ...
    def GetGenericResultType(self) -> CAE.BaseResultType:
        ...
    def SetGenericResultType(self, type: CAE.BaseResultType) -> None:
        ...
    def SetResultComponent(self, component: CAE.Result.Component) -> None:
        ...
    def GetResultComponent(self) -> CAE.Result.Component:
        ...
    def MakeElementResult(self, elementResult: bool) -> None:
        ...
    def GetElementResult(self) -> bool:
        ...
    def SetElementValueCriterion(self, criteria: CAE.Result.ElementValueCriterion) -> None:
        ...
    def GetElementValueCriterion(self) -> CAE.Result.ElementValueCriterion:
        ...
    def SetComplexCriterion(self, complex: CAE.Result.Complex) -> None:
        ...
    def GetComplexCriterion(self) -> CAE.Result.Complex:
        ...
    def SetPhaseAngle(self, angle: float) -> None:
        ...
    def GetPhaseAngle(self) -> float:
        ...
    def SetScale(self, scale: float) -> None:
        ...
    def GetScale(self) -> float:
        ...
    def SetUnit(self, unit: Unit) -> None:
        ...
    def GetUnit(self) -> Unit:
        ...
    def SetAbsoluteValue(self, absolute: bool) -> None:
        ...
    def GetAbsoluteValue(self) -> bool:
        ...
    def SetFillets(self, fillets: bool) -> None:
        ...
    def GetFillets(self) -> bool:
        ...
    def SetFilletRadius(self, filletRadius: float) -> None:
        ...
    def GetFilletRadius(self) -> float:
        ...
    def SetBeamElement(self, beamEid: int) -> None:
        ...
    def GetBeamElement(self) -> int:
        ...
    def SetBeamEnd(self, beamEnd: CAE.Result.BeamEnd) -> None:
        ...
    def GetBeamEnd(self) -> CAE.Result.BeamEnd:
        ...
    def GetModelRangeParameters(self) -> CAE.ResultParameters:
        ...
    def SetTensorComponentAbsoluteValue(self, absolute: CAE.Result.TensorDerivedAbsolute) -> None:
        ...
    def GetTensorComponentAbsoluteValue(self) -> CAE.Result.TensorDerivedAbsolute:
        ...


class Criteria(enum.Enum):
    None = -1
    Range = 0
    DiscreteValues = 1


class CreateJtBuilder(Builder):
    def __init__(self) -> None: ...
    def SetResult(self, result: CAE.Result) -> None:
        ...
    def SetExportData(self, parameters: typing.List[CAE.ResultParameters], templateIds: int, componentToExport: typing.List[CAE.CreateJtBuilder.Component]) -> None:
        ...
    def SetOutputFile(self, outputFile: str) -> None:
        ...


    class Component(enum.Enum):
        Unknown = -1
        Current = 0
        Primary = 1
    

class CrackFaceConditionBuilder(Builder):
    def __init__(self) -> None: ...
    CrackFrontEdgeSelection: CAE.SelectCAEEdgeList
    CreateCoincidentNodeToggle: bool
    FaceSelection: CAE.SelectCAEFaceList


class CorrelTestNodeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CorrelTestNode]:
        ...
    def __init__(self, owner: CAE.TestModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.CorrelTestNode:
        ...
    def Tag(self) -> Tag: ...



class CorrelTestNode(NXObject):
    def __init__(self) -> None: ...


class CorrelTestAnalysisSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    def ClearExciterConfig(self) -> None:
        ...
    AddUnattachedVisualizationNodes: bool
    Config: CAE.PreTestSensorConfig
    ConflictResolutionUsingExciterInfo: bool
    DetectActiveModeSensors: bool
    DofSet: CAE.CaeDOFSet
    ExciterConfig: CAE.PreTestExciterConfig
    GroupsSelection: CAE.SelectGroupsBuilder
    MaxDistanceRatio: float
    MaxNumOfWiresPerNode: int
    Method: CAE.CorrelTestAnalysisSolutionBuilder.MethodType
    MinAngleBetweenWires: Expression
    Name: str
    PreTestSolution: CAE.PreTestSolution
    Solution: CAE.SimSolution
    Source: CAE.CorrelTestAnalysisSolutionBuilder.SourceType
    SubcaseIndex: int


    class SourceType(enum.Enum):
        Solution = 0
        PreTestSolution = 1
    

    class MethodType(enum.Enum):
        Automatic = 0
        Manual = 1
    

class CorrelSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CorrelBaseSolution]:
        ...
    def __init__(self, owner: CAE.CorrelManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSolutionBuilder(self, solution: CAE.CorrelSolution) -> CAE.CorrelSolutionBuilder:
        ...
    def CreateFrfSolutionBuilder(self, frfSolution: CAE.CorrelFrfSolution) -> CAE.CorrelSolutionBuilder:
        ...
    def CreateFrfSynthesisSolutionBuilder(self, frfSolution: CAE.CorrelFrfSolution) -> CAE.CorrelSolutionBuilder:
        ...
    def CreateShapeMetricViewerBuilder(self, solution: CAE.CorrelSolution) -> CAE.ShapeMetricViewerBuilder:
        """[Obsolete("Deprecated in NX1847.0.0.  This function is no longer required.")"""
        ...
    def CreateComacViewerBuilder(self) -> CAE.ComacViewerBuilder:
        """[Obsolete("Deprecated in NX1847.0.0.  This function is no longer required.")"""
        ...
    def CreateCorrelTestAnalysisSolutionBuilder(self) -> CAE.CorrelTestAnalysisSolutionBuilder:
        ...
    def GetValidSolutionName(self) -> str:
        ...
    def CloneSolution(self, oldSolution: CAE.CorrelBaseSolution, suggestedName: str) -> CAE.CorrelBaseSolution:
        ...
    def FindObject(self, solutionName: str) -> CAE.CorrelBaseSolution:
        ...
    def Tag(self) -> Tag: ...

    ActiveSolution: CAE.CorrelBaseSolution


class CorrelSolutionBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    def GetSubcase(self) -> str:
        """[Obsolete("Deprecated in NX1872.0.0.  This functionality is no longer supported.")"""
        ...
    def SetSubcase(self, subcase: str) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  This functionality is no longer supported.")"""
        ...
    def CreateMethodBuilder(self) -> CAE.CorrelNodeMapMethodBuilder:
        ...
    def CreateFilterBuilder(self) -> CAE.CorrelNodeMapFilterBuilder:
        ...
    ComputeNodeMap: bool
    FrfDampingSource: CAE.CorrelSolutionBuilder.EnumDampingFrftype
    HighFrequencyCutoff: float
    HighFrequencyFilteringMode: bool
    LowFrequencyCutoff: float
    LowFrequencyFilteringMode: bool
    ModalMeasurementType: CAE.CorrelSolutionBuilder.ModalMeasurement
    NodeMapFilter: CAE.CorrelSolutionBuilder.EnumNodeMapFilter
    NodeMapMethod: CAE.CorrelSolutionBuilder.EnumNodeMapMethod
    NodeMapSizeLimit: int
    NodeMapSizeLimitActive: bool
    NodeMatchingDistance: float
    PrefFrfExcitationMeasure: CAE.CorrelSolutionBuilder.PrefFrfMeasure
    PrefFrfResponseExcitationMeasure: CAE.CorrelSolutionBuilder.PrefFrfRem
    PrefFrfResponseMeasure: CAE.CorrelSolutionBuilder.PrefFrfMeasure
    RefSubcase: int
    ReferenceSolution: CAE.SimSolution
    Title: str
    WorkSolution: CAE.SimSolution
    WorkSubcase: int


    class PrefFrfRem(enum.Enum):
        AccelerationForce = 0
        VelocityForce = 1
        DisplacementForce = 2
    

    class PrefFrfMeasure(enum.Enum):
        Force = 0
        Acceleration = 1
        Velocity = 2
        Displacement = 3
        Pressure = 4
        VolumeAcceleration = 5
        VolumeVelocity = 6
        VolumeDisplacement = 7
    

    class ModalMeasurement(enum.Enum):
        Auto = 0
        Displacement = 1
        Acceleration = 2
        Velocity = 3
        Pressure = 4
    

    class EnumNodeMapMethod(enum.Enum):
        None = 0
        Proximity = 1
        Identifier = 2
    

    class EnumNodeMapFilter(enum.Enum):
        None = 0
        SpatialReduction = 1
        Reduction = 2
        ExcludeNodesWithNoResults = 3
    

    class EnumDampingFrftype(enum.Enum):
        FromWorkModel = 0
        SpecifyDamping = 1
    

class CorrelSolution(CAE.CorrelBaseSolution):
    def __init__(self) -> None: ...
    def CreateModePairingBuilder(self) -> CAE.CorrelModePairingBuilder:
        ...
    def CreateModeClusteringBuilder(self) -> CAE.CorrelModeClusteringBuilder:
        ...
    def GetSolutionName(self) -> str:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.GetName instead.")"""
        ...
    def SetSolutionName(self, solutionName: str, renameResultFile: bool) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.SetName instead.")"""
        ...
    def Destroy(self, deleteResultFile: bool) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.Delete instead.")"""
        ...
    def ComputeMacs(self, referenceModeFrequencies: float, referenceModeNumbers: int, workModeFrequencies: float, workModeNumbers: int) -> float:
        ...
    def CalculateComacs(self, referenceModeNumbers: int, workModeNumbers: int, referenceModeFrequencies: float, workModeFrequencies: float, refNodesHaveSensors: int, refNodeIndex: int, refDofIndex: int) -> float:
        ...
    def SetActiveRefMode(self, refModeNumber: int, active: bool) -> None:
        ...
    def SetActiveWorkMode(self, workModeNumber: int, active: bool) -> None:
        ...
    def SetActiveModePair(self, referenceModeNumber: int, workModeNumber: int, active: bool) -> None:
        ...
    def SetActiveSensor(self, sensorNumber: int, active: bool) -> None:
        ...
    def SetActiveSensorDof(self, sensorNumber: int, dofNumber: int, active: bool) -> None:
        ...
    def SetActiveSensorDofOrientation(self, sensorNumber: int, dofNumber: int, orientation: bool) -> None:
        ...
    def ExportModePairCsvFile(self, filename: str) -> None:
        ...
    def ExportShapeMetricsCsvFile(self, metricCode: CAE.CorrelShapemetrictype, filename: str) -> None:
        ...
    def UpdateNodeMatchings(self) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.UpdateNodeMap instead.")"""
        ...
    def ComputeModePairsForSol(self) -> None:
        ...
    def CloneCorrelation(self) -> CAE.CorrelSolution:
        ...
    def UpdateResultsForSolution(self, tSolution: CAE.SimSolution, ignoreReload: bool) -> None:
        ...
    def GenerateMatchingDofset(self) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.GenerateDofSet instead.")"""
        ...
    def GenerateComacResults(self) -> None:
        ...
    def ImportNodeMapCsvFile(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.ImportNodeMapFromCsvFile instead.")"""
        ...
    def ExportNodeMapCsvFile(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.ExportNodeMapToCsvFile instead.")"""
        ...
    def LockNodeMap(self) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.NodeMapLock instead.")"""
        ...
    def UnlockNodeMap(self) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.NodeMapUnlock instead.")"""
        ...
    def ShowInformation(self) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.ShowInfo instead.")"""
        ...
    def ShowModePairingInformation(self) -> None:
        ...
    def ShowModeClustersInformation(self) -> None:
        ...
    def ShowModePairsInformation(self) -> None:
        ...
    def ShowNodeMapInformation(self) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.ShowNodeMapInfo instead.")"""
        ...
    def CreateDofSetFromSensorSet(self, pSensorSet: CAE.ISensorSet, modifyNodeDisplacementCsys: bool) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.CreateDofSet instead.")"""
        ...
    def GetSensorSetMgr(self, sensorSetType: CAE.CorrelSensorsettype) -> CAE.SensorSetMgr:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.CorrelBaseSolution.GetSensorSetMgr instead.")"""
        ...
    def CreateMacContributionsDlgBuilder(self) -> CAE.CorrelMacContributionsDlgBuilder:
        ...


class CorrelShapemetrictype(enum.Enum):
    Mac = 0
    Comac = 1
    Msf = 2
    Xortho = 3
    Nco = 4
    Sco = 5
    ModmacEvolution = 6
    Last = 7


class CorrelSensorsettype(enum.Enum):
    Mode = 0
    Frf = 1


class CorrelNodeMapMethodCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CorrelNodeMapMethod]:
        ...
    def __init__(self, owner: CAE.CorrelNodeMap) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.CorrelNodeMapMethod:
        ...
    def DeleteMethod(self, methodTag: CAE.CorrelNodeMapMethod) -> None:
        ...
    def Tag(self) -> Tag: ...



class CorrelNodeMapMethodBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def GetSearchDistance(self) -> float:
        ...
    def SetSearchDistance(self, distance: float) -> None:
        ...
    def GetCoincidenceTolerance(self) -> float:
        ...
    def SetCoincidenceTolerance(self, tolerance: float) -> None:
        ...
    def GetManualPairs(self, refLabels: int, workLabels: int) -> None:
        ...
    def SetManualPairs(self, refLabels: int, workLabels: int) -> None:
        ...
    CheckForCoincidentWorkNodes: bool
    IgnoreSpecialChars: bool
    MapSequentially: bool
    MatchBy: CAE.CorrelNodeMapMethodBuilder.MatchingBy
    MatchCase: bool
    MethodType: CAE.CorrelNodeMapMethodBuilder.Type
    Name: str
    Offset: int


    class Type(enum.Enum):
        Proximity = 0
        Identifier = 1
        Manual = 2
    

    class MatchingBy(enum.Enum):
        Label = 0
        Name = 1
    

class CorrelNodeMapMethod(NXObject):
    def __init__(self) -> None: ...
    def CreateFilterBuilder(self, filterTag: CAE.CorrelNodeMapFilter) -> CAE.CorrelNodeMapFilterBuilder:
        ...
    def Information(self) -> None:
        ...
    def IsActive(self) -> bool:
        ...
    def SetActive(self, active: bool) -> None:
        ...
    def GetName(self) -> str:
        ...
    def SetName(self, methodName: str) -> None:
        ...
    Filters: CAE.CorrelNodeMapFilterCollection


class CorrelNodeMapFilterCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CorrelNodeMapFilter]:
        ...
    def __init__(self, owner: CAE.CorrelNodeMapMethod) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.CorrelNodeMapFilter:
        ...
    def DeleteFilter(self, filterTag: CAE.CorrelNodeMapFilter) -> None:
        ...
    def Tag(self) -> Tag: ...



class CorrelNodeMapFilterBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def SetTestModelNodes(self, testModelNodes: typing.List[CAE.CorrelTestNode]) -> None:
        ...
    def SetGroups(self, groups: typing.List[TaggedObject]) -> None:
        ...
    def SetImportedNodes(self, baseSol: CAE.CorrelBaseSolution, importNodeLabels: int) -> None:
        ...
    DofSet: CAE.CaeDOFSet
    ExcludeMethodType: CAE.CorrelNodeMapFilterBuilder.ExcludeMethod
    FilterType: CAE.CorrelNodeMapFilterBuilder.Type
    GroupsSelection: CAE.SelectGroupsBuilder
    Name: str
    NodeMapSizeLimit: int
    NodeSourceType: CAE.CorrelNodeMapFilterBuilder.NodeSource
    Nodes: CAE.SelectFENodeList


    class Type(enum.Enum):
        Exclude = 0
        Include = 1
        Reduction = 2
        SpatialReduction = 3
    

    class NodeSource(enum.Enum):
        Reference = 0
        Work = 1
        Both = 2
    

    class ExcludeMethod(enum.Enum):
        Manual = 0
        NodesWithNoResults = 1
    

class CorrelNodeMapFilter(NXObject):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def IsActive(self) -> bool:
        ...
    def SetActive(self, active: bool) -> None:
        ...
    def GetName(self) -> str:
        ...
    def SetName(self, filterName: str) -> None:
        ...


class CorrelNodeMap(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CorrelBaseSolution) -> None: ...
    def CreateMethodBuilder(self, method: CAE.CorrelNodeMapMethod) -> CAE.CorrelNodeMapMethodBuilder:
        ...
    def Update(self) -> None:
        ...
    def ShowInfo(self) -> None:
        ...
    def ExportToCsvFile(self, filename: str) -> None:
        ...
    def Lock(self) -> None:
        ...
    def Unlock(self) -> None:
        ...
    def ClearNodes(self, removeWorkNodes: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    Methods: CAE.CorrelNodeMapMethodCollection


class CorrelModePairingBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    def AddManualPair(self, refModeId: int, workModeId: int) -> None:
        ...
    def RemoveManualPair(self, refModeId: int, workModeId: int) -> None:
        ...
    def ClearAllManualPairs(self) -> None:
        ...
    AutomaticRule: CAE.CorrelModePairingBuilder.Auto
    DefineModeClusters: bool
    FrequencyMode: CAE.CorrelModePairingBuilder.Frequency
    FrequencyTolerance: float
    FrequencyTolerancePct: float
    MacLowerBound: float
    ModePairsOnly: bool
    ShapeCorrelationMethod: CAE.CorrelModePairingBuilder.ShapeCorrelation
    TrackingMaster: bool
    XorthoLowerBound: float


    class ShapeCorrelation(enum.Enum):
        Mac = 0
        Xortho = 1
        None = 2
    

    class Frequency(enum.Enum):
        Delta = 0
        Pct = 1
    

    class Auto(enum.Enum):
        None = 0
        Sequential = 1
        Frequency = 2
        Mac = 3
        Xortho = 4
    

class CorrelModeClusteringBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    def AddCluster(self, refModes: int, workModes: int) -> None:
        ...
    def ModifyCluster(self, clusterIndex: int, refModes: int, workModes: int) -> None:
        ...
    def RemoveCluster(self, clusterIndex: int) -> None:
        ...


class CorrelManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def CreateModelUpdateDesignVariablesRapidCreateBuilderBuilder(self) -> CAE.ModelUpdateDesignVariablesRapidCreateBuilder:
        ...
    def CreateCorrelApplyAlignmentFromBuilder(self, solution: CAE.SimSolution) -> CAE.CorrelApplyAlignmentFromBuilder:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.TestModel instead.")"""
        ...
    def CreateCorrelFineTuneAlignmentBuilder(self, solution: CAE.SimSolution) -> CAE.CorrelFineTuneAlignmentBuilder:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.TestModel instead.")"""
        ...
    def ShowTestReferenceSolutionInformation(self, solution: CAE.SimSolution) -> None:
        ...
    def ExportTestAnalysisReferenceSolution(self, solution: CAE.SimSolution, format: CAE.CorrelManager.FormatType, filename: str, units: CAE.CorrelManager.UnitType, componentName: str) -> None:
        ...
    def CreateNewMaxSpreadGroup(self, inputNodes: typing.List[TaggedObject], groupName: str, groupLabel: int, maxNodes: int, minDistance: float) -> None:
        ...
    def Tag(self) -> Tag: ...

    Solutions: CAE.CorrelSolutionCollection
    PreTests: CAE.PreTestSolutionCollection
    ModelUpdates: CAE.ModelUpdateSolutionCollection
    ModelUpdateSolutionSets: CAE.ModelUpdateSolutionSetCollection


    class UnitType(enum.Enum):
        MeterNewton = 0
        FootPoundForce = 1
        MeterKilogramForce = 2
        FootPoundal = 3
        MmMilliNewton = 4
        CmCentiNewton = 5
        InchPoundForce = 6
        MmKilogramForce = 7
        MmNewton = 8
    

    class FormatType(enum.Enum):
        Unv = 0
        Sc2tl = 1
        Vl2tl = 2
    

class CorrelMacContributionsDlgBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    DeactivateToggle: bool
    RefModeIndex: int
    TargetMacValue: float
    TempSensorSet: CAE.ISensorSet
    WorkModeIndex: int


class CorrelFrfSynthSolution(CAE.CorrelFrfSolution):
    def __init__(self) -> None: ...
    def ShowModeInformation(self) -> None:
        ...
    def SetActiveWorkMode(self, index: int, isActive: bool) -> None:
        ...
    def SetActiveWorkModes(self, indices: int, isActive: bool) -> None:
        ...
    def SetDampingValue(self, index: int, value: float) -> None:
        ...
    def SetDampingValues(self, indices: int, values: float) -> None:
        ...


class CorrelFrfSolution(CAE.CorrelBaseSolution):
    def __init__(self) -> None: ...
    def ShowFrfPairsInformation(self) -> None:
        ...
    def ShowFrfPairingFilterInformation(self, filter: CAE.FrfPairingFilter) -> None:
        ...
    def FrfPlotSetupPlotting(self, cmd: CAE.CorrelFrfSolution.OptionsSelectedCommand) -> None:
        ...
    def FrfPlotAddPair(self, frfWorkExcitationNode: int, frfWorkResponseNode: int, frfRefExcitationNode: int, frfRefResponseNode: int, frfRefResponseDof: int, frfRefExcitationDof: int) -> None:
        ...
    def FrfPlotSetViewportDeviceAndIndex(self, device: int, viewIndex: int) -> None:
        ...
    def FrfPlotDoPlot(self) -> None:
        ...
    def SelectAllFrfPairs(self) -> None:
        ...
    def CreatePlotFrfOptionsBuilder(self, plotFrfOptions: CAE.PlotFrfOptions) -> CAE.PlotFrfOptionsBuilder:
        ...
    def ShowFrfInformation(self, reference: bool) -> None:
        ...
    def FrfPairingRemoveAllFilters(self) -> None:
        ...
    def FrfPairingRemoveFilter(self, name: str) -> None:
        ...
    def CreateFrfPairingFilterBuilder(self) -> CAE.FrfPairingFilterBuilder:
        ...
    def CloneFrfCorrelation(self) -> CAE.CorrelFrfSolution:
        ...
    def ExportFrfPairsToCsvFile(self, filename: str) -> None:
        ...


    class OptionsSelectedCommand(enum.Enum):
        Ref = 0
        Work = 1
        Overlay = 2
        Frac = 3
        FRACColorBar = 4
        FRACComparision = 5
    

class CorrelFineTuneAlignmentBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    def MoveButton(self) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.TestModel instead.")"""
        ...
    def RotateButton(self) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.TestModel instead.")"""
        ...
    AngleEnum: CAE.CorrelFineTuneAlignmentBuilder.AngleVector
    AngularExp: Expression
    DistanceEnum: CAE.CorrelFineTuneAlignmentBuilder.DistanceVector
    DistanceExp: Expression


    class DistanceVector(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
        NegXc = 3
        NegYc = 4
        NegZc = 5
    

    class AngleVector(enum.Enum):
        Xc = 0
        Yc = 1
        Zc = 2
        NegXc = 3
        NegYc = 4
        NegZc = 5
    

class CorrelBaseSolution(NXObject):
    def __init__(self) -> None: ...
    def GetName(self) -> str:
        ...
    def SetName(self, solutionName: str, renameResultFile: bool) -> None:
        ...
    def Delete(self, deleteResultFile: bool) -> None:
        ...
    def GenerateDofSet(self) -> None:
        ...
    def CreateDofSet(self, sensorSet: CAE.ISensorSet, modifyNodeDisplacementCsys: bool) -> None:
        ...
    def UpdateNodeMap(self) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CorrelNodeMap.Update instead.")"""
        ...
    def UpdateResultsForSol(self, sol: CAE.SimSolution, ignoreReload: bool) -> None:
        ...
    def ShowNodeMapInfo(self) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CorrelNodeMap.ShowInfo instead.")"""
        ...
    def ImportNodeMapFromCsvFile(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  This function is no longer required.")"""
        ...
    def ExportNodeMapToCsvFile(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CorrelNodeMap.ExportToCsvFile instead.")"""
        ...
    def NodeMapLock(self) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CorrelNodeMap.Lock instead.")"""
        ...
    def NodeMapUnlock(self) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CorrelNodeMap.Unlock instead.")"""
        ...
    def ShowInfo(self) -> None:
        ...
    def GetSensorSetMgr(self) -> CAE.SensorSetMgr:
        ...
    def CreateGroupFromSensorSet(self, sensorSet: CAE.ISensorSet) -> None:
        ...
    def ClearNodeMapNodes(self, removeWorkNodes: int) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.CAE.CorrelNodeMap.ClearNodes instead.")"""
        ...
    def ShowEffectiveDofs(self) -> None:
        ...
    NodeMap: CAE.CorrelNodeMap


class CorrelBaseBuilder(Builder):
    def __init__(self) -> None: ...


class CorrelApplyAlignmentFromBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    NativeFileBrowser: str


class CoordinateSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    def SetCoordinatesAndTolerance(self, coordinates: Point3d, tolerance: float) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeCoordinateStrategy.SetCoordinatesAndTolerance instead.")"""
        ...
    def SetHighLabelPreference(self, useHighLabel: bool) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeCoordinateStrategy.SetResolvePreference instead.")"""
        ...
    Coordinates: Point3d
    HighLabelPreference: bool
    Tolerance: float


class ConvexMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def AutomaticElementSize(self) -> None:
        ...
    def GetInfinitePlanes(self, infinitePlanes: typing.List[Plane]) -> None:
        ...
    def SetInfinitePlanes(self, pPlaneTags: typing.List[Plane]) -> None:
        ...
    ElementSize: Expression
    ElementType: CAE.ElementTypeBuilder
    InfinitePlane: Plane
    InfinitePlaneState: bool
    OffsetDistance: Expression
    OffsetMethod: CAE.ConvexMeshBuilder.OffsetMethodOption
    PropertyTable: CAE.PropertyTable
    ScaleFactor: Expression
    SelectMesh: SelectTaggedObjectList


    class OffsetMethodOption(enum.Enum):
        DistanceAlongNormal = 0
        ScaleFactor = 1
        None = 2
    

class ConvertToConvergentBodyBuilder(Builder):
    def __init__(self) -> None: ...
    Associate: bool
    BodySelection: CAE.SelectCAEBodyList
    ExistingFile: str
    NewFile: str
    TargetOption: CAE.ConvertToConvergentBodyBuilder.Option


    class Option(enum.Enum):
        ParentOfFEM = 0
        ComponentOfCADBody = 1
        NewPart = 2
        ExistingPart = 3
    

class ContactMeshBuilder(Builder):
    def __init__(self) -> None: ...
    AlignTargetEdgeNodes: bool
    AlignmentMethod: CAE.ContactMeshBuilder.AlignmentType
    ContactEdge: CAE.SelectCAEEdge
    ContactEdgeEndPoint: Point
    ContactEdgeStartPoint: Point
    ElementType: CAE.ElementTypeBuilder
    EnableGapTolerance: bool
    GapTolerance: float
    NumElements: int
    TargetEdge: CAE.SelectCAEEdge
    TargetEdgeEndPoint: Point
    TargetEdgeStartPoint: Point


    class AlignmentType(enum.Enum):
        Minimumdistance = 0
        Normaltocontactedge = 1
    

class ConflictResolutionBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable
    ResolveRule: CAE.ConflictResolutionBuilder.Rule


    class Rule(enum.Enum):
        ApplyFirstBc = 0
        ApplySecondBc = 1
        AverageDofValues = 2
        AddDofValues = 3
        SpecifyDofValues = 4
        IgnoreConflict = 5
        ApplyOverride = 6
    

class ComponentDofsTerm():
    NodeIndex: int
    ComponentDofs: int
    def ToString(self) -> str:
        ...
    def __init__(self, NodeIndex: int, ComponentDofs: int) -> None: ...


class Complex():
    Real: float
    Imag: float
    def ToString(self) -> str:
        ...
    def __init__(self, Real: float, Imag: float) -> None: ...


class CompanionResultCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CompanionResult]:
        ...
    def __init__(self, owner: CAE.SimResultReference) -> None: ...
    def __init__(self) -> None: ...
    def CreateCompanionResultBuilder(self, companionresult: CAE.CompanionResult) -> CAE.CompanionResultBuilder:
        ...
    def Delete(self, companionresult: CAE.CompanionResult) -> None:
        ...
    def CreateMultipleCompanionResultBuilder(self) -> CAE.MultipleCompanionResultBuilder:
        ...
    def Tag(self) -> Tag: ...



class CompanionResultBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitResult(self) -> CAE.CompanionResult:
        ...
    AppendMethod: CAE.CompanionResultBuilder.ResultAppendMethod
    CompanionResultsFile: str
    Disposition: CAE.CompanionResultBuilder.CompanionResultDisposition
    Name: str


    class ResultAppendMethod(enum.Enum):
        CreateNewLoadCases = 0
        MergeWithPrimaryResultsData = 1
    

    class CompanionResultDisposition(enum.Enum):
        Delete = 0
        Keep = 1
    

class CompanionResult(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


class CombineTrisBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMesh(self) -> CAE.Mesh:
        ...
    SelectFirstTri: SelectTaggedObjectList
    SelectSecondTri: SelectTaggedObjectList


class ComacViewerBuilder(Builder):
    def __init__(self) -> None: ...
    def Init(self, solution: CAE.CorrelSolution, comacsValues: float, nodeIndex: int, dofIndex: int) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  This function is no longer required.")"""
        ...


class CloneSelRecipeBuilder(CAE.SelRecipeBuilder):
    def __init__(self) -> None: ...
    DeleteSourceRecipe: bool
    SourceSelRecipe: CAE.SelectionRecipe


class ClippingParameters(TaggedObject):
    def __init__(self) -> None: ...
    def GetShowOutline(self) -> bool:
        ...
    def SetShowOutline(self, showOutline: bool) -> None:
        ...
    def GetShowClippedGhost(self) -> bool:
        ...
    def SetShowClippedGhost(self, showClippedGhost: bool) -> None:
        ...
    def GetClipValue(self) -> float:
        ...
    def SetClipValue(self, clipValue: float) -> None:
        ...
    def GetSide(self) -> CAE.Post.ClipSide:
        ...
    def SetSide(self, side: CAE.Post.ClipSide) -> None:
        ...
    def GetPlane(self) -> CAE.Post.ClipPlane:
        ...
    def SetPlane(self, plane: CAE.Post.ClipPlane) -> None:
        ...
    def GetCoordinateSystem(self) -> CAE.Result.CoordinateSystem:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ClippingParameters.GetPostCoordinateSystem instead.")"""
        ...
    def SetCoordinateSystem(self, coordinateSystem: CAE.Result.CoordinateSystem) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ClippingParameters.SetPostCoordinateSystem instead.")"""
        ...
    def GetSelectedCoordinateSystem(self, source: CAE.Result.CoordinateSystemSource, id: int) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ClippingParameters.GetPostCoordinateSystem instead.")"""
        ...
    def SetSelectedCoordinateSystem(self, source: CAE.Result.CoordinateSystemSource, id: int) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.ClippingParameters.SetPostCoordinateSystem instead.")"""
        ...
    def GetRefNode(self) -> CAE.PostSelectionEntity:
        ...
    def SetRefNode(self, val: CAE.PostSelectionEntity) -> None:
        ...
    def GetPostCoordinateSystem(self) -> CAE.PostCoordinateSystem:
        ...
    def SetPostCoordinateSystem(self, val: CAE.PostCoordinateSystem) -> None:
        ...


class CircularImprintBuilder(Builder):
    def __init__(self) -> None: ...
    AbsoluteDiaAroundEdge: Expression
    AbsoluteDiaAroundPoint: Expression
    AroundEdgeDiaOption: CAE.CircularImprintBuilder.AroundEdgeDiaType
    DiaScaleFactor: float
    EdgeSelection: SelectTaggedObjectList
    SurfaceSelection: SelectTaggedObjectList


    class AroundEdgeDiaType(enum.Enum):
        Absolute = 0
        Relative = 1
    

class CircularEdgeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEdges(self) -> typing.List[CAE.CAEEdge]:
        ...


class CfdLocalResolutionConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CfdLocalResolutionConstraint]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.CfdLocalResolutionConstraint:
        ...
    def Find(self, journalIdentifier: str) -> CAE.CfdLocalResolutionConstraint:
        ...
    def CreateBuilder(self, recipe: TaggedObject) -> CAE.CfdLocalResolutionConstraintBuilder:
        ...
    def DeleteConstraint(self, constraint: CAE.CfdLocalResolutionConstraint) -> None:
        ...
    def CloneConstraint(self, source: CAE.CfdLocalResolutionConstraint) -> CAE.CfdLocalResolutionConstraint:
        ...
    def Tag(self) -> Tag: ...



class CfdLocalResolutionConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    BboxPoint: Point
    BsphereRadius: Expression
    LocalResolution: Expression
    LocalSubdivision: CAE.CfdLocalResolutionConstraintBuilder.LocalSubdivisions
    NameString: str
    PointSelection: Point
    PriorityLevel: CAE.CfdLocalResolutionConstraintBuilder.Priority
    ResolutionDensityType: CAE.CfdLocalResolutionConstraintBuilder.ResolutionDensity
    SelectElement: SelectTaggedObjectList
    SelectObject: SelectDisplayableObjectList
    SizingOption: CAE.CfdLocalResolutionConstraintBuilder.Sizing


    class Sizing(enum.Enum):
        RelativeRefinement = 0
        RelativeCoarsening = 1
        Absolute = 2
    

    class ResolutionDensity(enum.Enum):
        SizeonObjects = 0
        SizeonElements = 1
        SizeinBoundingBox = 2
        SizeinBoundingSphere = 3
    

    class Priority(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
    

    class LocalSubdivisions(enum.Enum):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
    

class CfdLocalResolutionConstraint(NXObject):
    def __init__(self) -> None: ...
    def SetName(self, name: str) -> None:
        ...
    def GetName(self) -> str:
        ...


class CfdContactPreventionConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CfdContactPreventionConstraint]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.CfdContactPreventionConstraint:
        ...
    def Find(self, journalIdentifier: str) -> CAE.CfdContactPreventionConstraint:
        ...
    def CreateBuilder(self, recipe: TaggedObject) -> CAE.CfdContactPreventionConstraintBuilder:
        ...
    def DeleteConstraint(self, constraint: CAE.CfdContactPreventionConstraint) -> None:
        ...
    def CloneConstraint(self, source: CAE.CfdContactPreventionConstraint) -> CAE.CfdContactPreventionConstraint:
        ...
    def Tag(self) -> Tag: ...



class CfdContactPreventionConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    ContactType: CAE.CfdContactPreventionConstraintBuilder.Contact
    FirstSelectElement: SelectTaggedObjectList
    FirstSelection: SelectDisplayableObject
    LocalResolution: Expression
    LocalSubdivision: CAE.CfdContactPreventionConstraintBuilder.LocalSubdivisions
    NameString: str
    PriorityLevel: CAE.CfdContactPreventionConstraintBuilder.Priority
    SecondSelectElement: SelectTaggedObjectList
    SecondSelection: SelectDisplayableObject
    SizingOption: CAE.CfdContactPreventionConstraintBuilder.Sizing


    class Sizing(enum.Enum):
        RelativeRefinement = 0
        RelativeCoarsening = 1
        Absolute = 2
    

    class Priority(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
    

    class LocalSubdivisions(enum.Enum):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
    

    class Contact(enum.Enum):
        ContactbetweenObjects = 0
        ContactbetweenElements = 1
    

class CfdContactPreventionConstraint(NXObject):
    def __init__(self) -> None: ...
    def SetName(self, name: str) -> None:
        ...
    def GetName(self) -> str:
        ...


class CfdAutoRefinementConstraintCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CfdAutoRefinementConstraint]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.CfdAutoRefinementConstraint:
        ...
    def Find(self, journalIdentifier: str) -> CAE.CfdAutoRefinementConstraint:
        ...
    def CreateBuilder(self, recipe: TaggedObject) -> CAE.CfdAutoRefinementConstraintBuilder:
        ...
    def DeleteConstraint(self, constraint: CAE.CfdAutoRefinementConstraint) -> None:
        ...
    def CloneConstraint(self, source: CAE.CfdAutoRefinementConstraint) -> CAE.CfdAutoRefinementConstraint:
        ...
    def Tag(self) -> Tag: ...



class CfdAutoRefinementConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    LocalResolution: Expression
    LocalSubdivision: CAE.CfdAutoRefinementConstraintBuilder.LocalSubdivisions
    NameString: str
    PriorityLevel: CAE.CfdAutoRefinementConstraintBuilder.Priority
    SelectObject: SelectDisplayableObjectList
    SizingOption: CAE.CfdAutoRefinementConstraintBuilder.Sizing


    class Sizing(enum.Enum):
        RelativeRefinement = 0
        RelativeCoarsening = 1
        Absolute = 2
    

    class Priority(enum.Enum):
        Low = 0
        Medium = 1
        High = 2
    

    class LocalSubdivisions(enum.Enum):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
    

class CfdAutoRefinementConstraint(NXObject):
    def __init__(self) -> None: ...
    def SetName(self, name: str) -> None:
        ...
    def GetName(self) -> str:
        ...


class CAEWeldConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitWeldconnection(self) -> CAE.CAEWeldConnection:
        """[Obsolete("Deprecated in NX7.5.1.  Use Builder.Commit instead.")"""
        ...
    BottomFaceSelection: SelectTaggedObjectList
    ElementType: CAE.ElementTypeBuilder
    HardObjSelection: SelectTaggedObjectList
    MergeNodeTol: Expression
    MeshDensityType: CAE.CAEWeldConnectionBuilder.MeshDensityTypeEnum
    MeshDensityValue: Expression
    TopFaceSelection: SelectTaggedObjectList
    WeldType: CAE.CAEWeldConnectionBuilder.WeldTypeEnum


    class WeldTypeEnum(enum.Enum):
        PointToPointDirect = 0
        PointToPointIndirect = 1
        PointToPoint3dWeld = 2
    

    class MeshDensityTypeEnum(enum.Enum):
        Size = 0
        Number = 1
    

class CAEWeldConnection(CAE.CAEConnection):
    def __init__(self) -> None: ...


class CAEVertex(DisplayableObject):
    def __init__(self) -> None: ...
    Coordinates: Point3d


class CaeSetObjectSubType(enum.Enum):
    None = 0
    ElementFace = 1
    ElementEdge = 2
    Part = 3
    SelRecipe = 4


class CaeSetGroupFilterType(enum.Enum):
    Node = 0
    Element = 1
    GeomFace = 2
    GeomBody = 3
    GeomCurve = 4
    GeomPoint = 5
    PointElement = 6
    BeamElement = 7
    ShellElement = 8
    SolidElement = 9
    GeomPlanarFace = 10
    GeomCylFace = 11
    BeamElementTypeBar = 12
    BeamElementTypeBeam = 13
    BeamElementTypeRod = 14
    BeamElementTypeBearing = 15
    NodeAndElement = 16
    CaeGeometry = 17
    CaeMesh = 18
    BoundingVolume = 19
    ElementFace = 20
    ElementEdge = 21
    GeomEdge = 22
    GeomCircularedge = 23
    BeamElementTypeMpc = 24
    CaePointMesh = 25
    CaeBeamMesh = 26
    CaeShellMesh = 27
    CaeSolidMesh = 28
    BeamMeshTypeBar = 29
    BeamMeshTypeBeam = 30
    BeamMeshTypeRod = 31
    BeamMeshTypeBearing = 32
    BeamMeshTypeMpc = 33
    GeomVertex = 34
    FeEntity = 35
    BeamElementTypeJoint = 36
    BeamMeshTypeJoint = 37
    BeamElementTypeBearing2 = 38
    BeamMeshTypeBearing2 = 39
    BeamElementTypeFou3 = 40
    BeamMeshTypeFou3 = 41
    BeamElementTypeBush2 = 42
    BeamMeshTypeBush2 = 43
    BeamElementTypeClink = 44
    BeamMeshTypeClink = 45
    BeamElementTypeCgear = 46
    BeamMeshTypeCgear = 47


class CAESet(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetMembers(self, members: typing.List[CAE.SetObject]) -> None:
        ...
    def GetMembers(self, members: typing.List[CAE.SetObject]) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class CaeSession(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetDataContainer(self) -> CAE.CaeDataContainer:
        ...
    def ImportSimulation(self, solverName: str, propertyList: CAE.CaeDataContainer) -> CAE.CaePart:
        ...
    def SetFileNewContext(self, contextPart: NXObject) -> None:
        ...
    def NewCaeCoreService(self) -> CAE.CAECoreService:
        ...
    def AddPartCreatedHandler(self, handler: CAE.CaeSession.PartCreatedHandler) -> int:
        ...
    def RemovePartCreatedHandler(self, id: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    MaterialUtils: MaterialUtilities
    AssociationUtils: CAE.AssociationUtilities
    QualityAuditManager: CAE.QualityAudit.Manager
    UniversalConnectionUtilities: CAE.Connections.Utils
    MeshMappingUtils: CAE.MeshMapping.Utils
    PenetrationCheckManager: CAE.PenetrationCheck.Manager
    ModelDependencyCheckManager: CAE.ModelDependencyCheck.Manager
    ContactPreviewObjectCollection: CAE.ContactPreview.ContactObjectCollection


    

    

    

class CaeSensor(NXObject):
    def __init__(self) -> None: ...
    def GetLabel(self) -> int:
        ...
    def GetSensorActive(self) -> bool:
        ...
    def SetSensorActive(self, active: bool) -> None:
        ...
    def GetSensorDofs(self, dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> None:
        ...
    def SetSensorDofs(self, dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> None:
        ...
    def SetSensorDofsNegative(self, negative1: bool, negative2: bool, negative3: bool, negative4: bool, negative5: bool, negative6: bool) -> None:
        ...


class CaeRegionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CaeRegion]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateCaeRegion(self, descriptorName: str, name: str, label: int) -> CAE.CaeRegion:
        ...
    def Copy(self, tSourceRegion: CAE.CaeRegion) -> CAE.CaeRegion:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.CaeRegion:
        ...
    def Tag(self) -> Tag: ...



class CaeRegionBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable
    TargetSetManager: CAE.SetManager


class CaeRegion(CAE.NamedPropTableWithTargetSet):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    DescriptorName: str


class CaePostProcessingSessionApplicatorLoadAction(enum.Enum):
    DoNothing = 0
    LoadFromFile = 1
    KeepBoth = 2


class CaePart(BasePart):
    def __init__(self) -> None: ...
    def NewMaterialOptions(self) -> CAE.MaterialOptions:
        ...
    def CreateConvertToConvergentBodyBuilder(self) -> CAE.ConvertToConvergentBodyBuilder:
        ...
    def ExportJt(self, fileName: str) -> None:
        ...
    def ExportSimulation(self, solverName: str, propertyList: CAE.CaeDataContainer) -> None:
        ...
    def NewBeamSectionOptions(self) -> CAE.BeamSectionOptions:
        ...
    def CreateModelDisplayBuilder(self) -> CAE.ModelDisplayBuilder:
        ...
    def NewThermoOpticalPropMgr(self) -> CAE.ThermoOpticalPropMgr:
        ...
    def GetDescription(self, description: str) -> None:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def NewBeamSectionOrientationOptions(self) -> CAE.BeamSectionOrientationOptions:
        ...
    def NewBeamSectionOffsetOptions(self) -> CAE.BeamSectionOffsetOptions:
        ...
    def ImportExistingSimulation(self, solverName: str, propertyList: CAE.CaeDataContainer) -> None:
        ...
    def CreateSolverAppendOption(self) -> CAE.SolverAppendOption:
        ...
    def DeleteSolverAppendOption(self, appendOption: CAE.SolverAppendOption) -> None:
        ...
    def GetCsysFlattenedLabel(self, csys: CoordinateSystem) -> int:
        ...
    def GetApplication(self, applicationType: CAE.CaePart.FieldApplicationType) -> Fields.IApplication:
        ...
    def CreatePenetrationCheckAddSetBuilder(self, penetrationAddSet: NXObject) -> CAE.PenetrationCheck.AddSetBuilder:
        ...
    def CreatePenetrationCheckAutomaticResolveBuilder(self, penetrationCheck: NXObject) -> CAE.PenetrationCheck.AutomaticResolveBuilder:
        ...
    def CreatePenetrationCheckTranslateNodesBuilder(self) -> CAE.PenetrationCheck.TranslateNodesBuilder:
        ...
    def CreateStlImportBuilder(self) -> CAE.StlImportBuilder:
        ...
    def CreateContactPreviewSettingsBuilder(self) -> CAE.ContactPreview.SettingsBuilder:
        ...
    AtvSets: CAE.AtvSetCollection
    FrfSets: CAE.FrfSetCollection
    ModeSets: CAE.ModeSetCollection
    VatvSets: CAE.VatvSetCollection
    PhysicalPropertyTables: CAE.PhysicalPropertyTableCollection
    ModelingObjectPropertyTables: CAE.ModelingObjectPropertyTableCollection
    CaeGroups: CAE.CaeGroupCollection
    SmartSelectionMgr: CAE.SmartSelectionManager
    NodeElementInfoMgr: CAE.NodeElementInfoManager
    SelectElementMgr: CAE.SelectElementsManager
    MeshControlDisplayMgr: CAE.MeshControlDisplayManager
    ModelCheckMgr: CAE.ModelCheckManager
    ShowHideMgr: CAE.ShowHideManager
    ElementQualitySettings: CAE.ModelCheck.ElementQualitySettingCollection
    CaeQueryCurves: CAE.QueryCurveManager
    BeamSections: CAE.BeamSectionsCollection
    SelectionRecipes: CAE.SelectionRecipeCollection
    Notes: CAE.NoteManager
    CaeNoteCollection: CAE.NoteCollection
    MarginAnnotationCollection: CAE.AeroStructures.MarginAnnotCollection
    PostEnvironmentsMgr: CAE.PostEnvironmentsManager
    SelectGroupsMgr: CAE.SelectGroupsManager


    class FieldApplicationType(enum.Enum):
        SignalProcessing = 0
        Abaqus = 1
        Dyna = 2
    

class CaeNoteBuilder(Annotations.DraftingNoteBuilder):
    def __init__(self) -> None: ...
    def SetFolderName(self, folderName: str) -> None:
        ...
    def ConvertLabelToNote(self, annotation: Annotations.NoteBase) -> None:
        ...
    def ConvertNoteToLabel(self, annotation: Annotations.NoteBase) -> None:
        ...
    AssociatedObjects: SelectTaggedObjectList


class CaeNote(Annotations.NoteBase):
    def __init__(self) -> None: ...
    def SetAssociatedObjects(self, objectArray: typing.List[TaggedObject]) -> None:
        ...
    def GetAssociatedObjects(self) -> typing.List[TaggedObject]:
        ...
    def RemoveAssociatedObjects(self) -> None:
        ...
    def GetAssocOrigin(self, origin: Point3d) -> Annotations.Annotation.AssociativeOriginData:
        ...


class CaeLabel(Annotations.NoteBase):
    def __init__(self) -> None: ...
    def SetAssociatedObjects(self, objectArray: typing.List[TaggedObject]) -> None:
        ...
    def GetAssociatedObjects(self) -> typing.List[TaggedObject]:
        ...
    def RemoveAssociatedObjects(self) -> None:
        ...


class CaeGroupElementSubType(enum.Enum):
    Face = 0
    Edge = 1


class CaeGroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CaeGroup]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateGroup(self, setName: str, objects: typing.List[TaggedObject]) -> CAE.CaeGroup:
        ...
    def CreateGroup(self, setName: str, label: int, objects: typing.List[TaggedObject]) -> CAE.CaeGroup:
        ...
    def CreateUnionGroup(self, setName: str, objects: typing.List[CAE.CaeGroup]) -> CAE.CaeGroup:
        ...
    def CreateIntersectionGroup(self, setName: str, objects: typing.List[CAE.CaeGroup]) -> CAE.CaeGroup:
        ...
    def CreateExclusiveOrGroup(self, setName: str, objects: typing.List[CAE.CaeGroup]) -> CAE.CaeGroup:
        ...
    def CreateSubtractGroup(self, setName: str, fromGroup: CAE.CaeGroup, excludedGroup: CAE.CaeGroup) -> CAE.CaeGroup:
        ...
    def CopyGroup(self, setName: str, sourceGroup: CAE.CaeGroup) -> CAE.CaeGroup:
        ...
    def CopyToClipboard(self, sourceGroups: typing.List[CAE.CaeGroup]) -> None:
        ...
    def PasteFromClipboard(self, pasteOptions: CAE.CaeGroupCollection.PasteOptions) -> None:
        ...
    def CreateOutputGroup(self, objects: typing.List[TaggedObject]) -> CAE.CaeGroup:
        ...
    def CreateGroupFromEntityIds(self, setName: str, entityType: CAE.CaeGroupCollection.EntityType, entityID: int) -> CAE.CaeGroup:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.CaeGroup:
        ...
    def QueryGroupList(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def CreateGroupByBoundaryBuilder(self) -> CAE.GroupByBoundaryBuilder:
        ...
    def CreateAutoGroups(self, autoGroupTypes: CAE.CaeGroupCollection.AutoGroupTypes, autoGroupSeeds: CAE.CaeGroupCollection.AutoGroupSeedNames, autoGroups: typing.List[CAE.CaeGroup]) -> CAE.CaeGroupCollection.AutoGroupErrorCodes:
        ...
    def CreateAutoGroups(self, ptMeshes: typing.List[CAE.Mesh], autoGroupTypes: CAE.CaeGroupCollection.AutoGroupTypes, autoGroupSeeds: CAE.CaeGroupCollection.AutoGroupSeedNames, autoGroups: typing.List[CAE.CaeGroup]) -> CAE.CaeGroupCollection.AutoGroupErrorCodes:
        ...
    def CreateGroupHidden(self, objects: typing.List[TaggedObject]) -> CAE.CaeGroup:
        ...
    def CreateGroupBuilder(self, group: CAE.CaeGroup) -> CAE.CaeGroupBuilder:
        ...
    def Tag(self) -> Tag: ...



    class CaeGroupCollectionPasteOptions():
        Prefix: str
        Label: int
        def ToString(self) -> str:
            ...
        def __init__(self, Prefix: str, Label: int) -> None: ...
    

    class EntityType(enum.Enum):
        Node = 0
        Element = 1
    

    class CaeGroupCollectionAutoGroupTypes():
        ByMaterial: bool
        ByPpt: bool
        ByColor: bool
        BySection: bool
        ByLaminate: bool
        ByDimension: bool
        ByMeshcolltype: bool
        ByMeshsubtype: bool
        ConnectedcompNodes: bool
        def ToString(self) -> str:
            ...
    

    class CaeGroupCollectionAutoGroupSeedNames():
        MaterialSeed: str
        PptSeed: str
        ColorSeed: str
        SectionSeed: str
        LaminateSeed: str
        DimensionSeed: str
        MeshcolltypeSeed: str
        ConnectedcompSeed: str
        def ToString(self) -> str:
            ...
    

    class CaeGroupCollectionAutoGroupErrorCodes():
        ByMaterial: int
        ByPpt: int
        ByColor: int
        BySection: int
        ByLaminate: int
        ByDimension: int
        ByMeshcolltype: int
        ByMeshsubtype: int
        ConnectedcompNodes: int
        def ToString(self) -> str:
            ...
    

    class CaeGroupCollection_PasteOptions():
        prefix: int
        label: int
    

    class CaeGroupCollection_AutoGroupSeedNames():
        material_seed: int
        ppt_seed: int
        color_seed: int
        section_seed: int
        laminate_seed: int
        dimension_seed: int
        meshcolltype_seed: int
        connectedcomp_seed: int
    

class CaeGroupBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, desc: str) -> None:
        ...
    def ClearDescription(self) -> None:
        ...
    Label: int
    Name: str
    Selection: SelectTaggedObjectList


class CaeGroup(NXObject):
    def __init__(self) -> None: ...
    def SetName(self, name: str) -> None:
        ...
    def GetName(self) -> str:
        ...
    def SetEntities(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def GetEntities(self) -> typing.List[TaggedObject]:
        ...
    def SetEntitiesFromNodesId(self, nodesId: int) -> None:
        ...
    def SetEntitiesFromElementsId(self, elementsId: int) -> None:
        ...
    def GetElementEdges(self, objects: typing.List[CAE.ElemEdgefaceObject]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.CaeGroup.GetFeElemEdges instead.")"""
        ...
    def GetElementFaces(self, objects: typing.List[CAE.ElemEdgefaceObject]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use NXOpen.CAE.CaeGroup.GetFeElemFaces instead.")"""
        ...
    def GetFeElemEdges(self) -> typing.List[CAE.FEElemEdge]:
        ...
    def GetFeElemFaces(self) -> typing.List[CAE.FEElemFace]:
        ...
    def AddEntities(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def RemoveEntities(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def ShowOnlyGroup(self) -> None:
        ...
    def ShowGroup(self) -> None:
        ...
    def HideGroup(self) -> None:
        ...
    def GroupInformation(self) -> None:
        ...
    def HasNonDisplayableEntities(self) -> bool:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    Label: int


class CAEFace(DisplayableObject):
    def __init__(self) -> None: ...
    def GetUgfaces(self) -> typing.List[Face]:
        ...
    def SynchronizeCadProperties(self) -> None:
        ...
    def GetBodies(self) -> typing.List[CAE.CAEBody]:
        ...


class CaeElementAssociatedDataUtilsVectorChoiceType(enum.Enum):
    Horizontal = 0
    Vertical = 1


class CaeElementAssociatedDataUtilsOrientationMethod(enum.Enum):
    None = 0
    Vector = 1
    Csystem = 2
    Node = 3
    CsystemData = 4


class CaeElementAssociatedDataUtilsOrientationCsys(enum.Enum):
    Absolute = 0
    Nodal = 1


class CaeElementAssociatedDataUtilsOffsetCsysChoice(enum.Enum):
    Nodal = 0
    Elemental = 1


class CaeElementAssociatedDataUtilsMatOrientationMethod(enum.Enum):
    None = 0
    OriAngle = 1
    CoordinateSystem = 2
    CsysData = 3


class CaeElementAssociatedDataUtilsEndReleaseState(enum.Enum):
    Set = 0
    Clear = 1


class CaeElementAssociatedDataUtilsEndReleaseSetting(enum.Enum):
    Off = 0
    On = 1


class CaeElementAssociatedDataUtilsDof(enum.Enum):
    Off = 0
    On = 1


class CaeElementAssociatedDataUtilsCsysDataType(enum.Enum):
    Cartesian = 0
    Cylindrical = 1
    Spherical = 2


class CaeElementAssociatedDataUtilsComponentEnd(enum.Enum):
    None = 0
    X = 1
    Y = 2
    Z = 3
    Rx = 4
    Ry = 5
    Rz = 6


class CAEEdge(DisplayableObject):
    def __init__(self) -> None: ...
    def SynchronizeCadProperties(self) -> None:
        ...
    def GetLength(self) -> float:
        ...
    def GetLocations(self) -> typing.List[GeometricUtilities.CurveLocation]:
        ...
    IsReference: bool


class CaeDOFSetDisplay(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateDisplay(self) -> None:
        ...
    GraphicSymbolDisplayFlag: bool
    NameDisplayFlag: bool
    NodeIdDisplayFlag: bool
    Scale: int
    ShadeGraphicSymbol: bool


class CaeDOFSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CaeDOFSet]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def CreateDofset(self, dofsetName: str, nodes: typing.List[CAE.FENode], dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> CAE.CaeDOFSet:
        ...
    def CreateDofsetFromSelectionRecipes(self, dofsetName: str, selectionRecipes: typing.List[CAE.SelectionRecipe], dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> CAE.CaeDOFSet:
        ...
    def CreateDofsetFromNodesAndSelectionRecipes(self, dofsetName: str, nodes: typing.List[CAE.FENode], nodeDof1: bool, nodeDof2: bool, nodeDof3: bool, nodeDof4: bool, nodeDof5: bool, nodeDof6: bool, selectionRecipes: typing.List[CAE.SelectionRecipe], selRepDof1: bool, selRepDof2: bool, selRepDof3: bool, selRepDof4: bool, selRepDof5: bool, selRepDof6: bool) -> CAE.CaeDOFSet:
        ...
    def CreateUnionDofset(self, dofsetName: str, objects: typing.List[CAE.CaeDOFSet]) -> CAE.CaeDOFSet:
        ...
    def CreateIntersectionDofset(self, dofsetName: str, objects: typing.List[CAE.CaeDOFSet]) -> CAE.CaeDOFSet:
        ...
    def CreateExclusiveOrDofset(self, dofsetName: str, objects: typing.List[CAE.CaeDOFSet]) -> CAE.CaeDOFSet:
        ...
    def CopyDofset(self, dofsetName: str, sourceDofset: CAE.CaeDOFSet) -> CAE.CaeDOFSet:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.CaeDOFSet:
        ...
    def QueryDofsetList(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def Tag(self) -> Tag: ...



class CaeDOFSet(DisplayableObject):
    def __init__(self) -> None: ...
    def SetLabel(self, label: int) -> None:
        ...
    def GetLabel(self) -> int:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...
    def GetNodesWithDof(self, dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> typing.List[CAE.FENode]:
        ...
    def AddNodes(self, nodes: typing.List[CAE.FENode], dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> None:
        ...
    def AddSelectionRecipes(self, recipes: typing.List[CAE.SelectionRecipe], dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> None:
        ...
    def AddNodesAndSelectionRecipes(self, nodes: typing.List[CAE.FENode], ndof1: bool, ndof2: bool, ndof3: bool, ndof4: bool, ndof5: bool, ndof6: bool, recipes: typing.List[CAE.SelectionRecipe], rdof1: bool, rdof2: bool, rdof3: bool, rdof4: bool, rdof5: bool, rdof6: bool) -> None:
        ...
    def RemoveNodes(self, nodes: typing.List[CAE.FENode]) -> None:
        ...
    def RemoveSelectionRecipes(self, recipes: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    def ModifyNodeDofs(self, nodes: typing.List[CAE.FENode], dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> None:
        ...
    def ModifySelectionRecipeDofs(self, recipes: typing.List[CAE.SelectionRecipe], dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> None:
        ...
    def RemoveAllNodes(self) -> None:
        ...
    def RemoveAllSelectionRecipes(self) -> None:
        ...
    def Information(self) -> None:
        ...
    def GetDisplay(self) -> CAE.CaeDOFSetDisplay:
        ...
    def GetSelectionRecipes(self) -> typing.List[CAE.SelectionRecipe]:
        ...
    def GetSelectionRecipesWithDof(self, dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> typing.List[CAE.SelectionRecipe]:
        ...


class CaeDataContainer(DataContainer):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class CAECoreService(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def ExecuteStructureDataMap(self, part: BasePart, smSpec: str, domain: str) -> str:
        ...


class CAEConnectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CAEConnection]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.CAEConnection:
        ...
    def CreateConnectionBuilder(self, connection: CAE.CAEConnection) -> CAE.CAEConnectionBuilder:
        ...
    def CreateWeldConnectionBuilder(self, weldconnection: CAE.CAEWeldConnection) -> CAE.CAEWeldConnectionBuilder:
        ...
    def CreateEdgeSeparationConditionBuilder(self) -> CAE.EdgeSeparationConditionBuilder:
        ...
    def Tag(self) -> Tag: ...



class CAEConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    def MeshDensity(self) -> None:
        ...
    ApplyWeightsRbe3: bool
    EdgeToEdgeConnectionMethodType: CAE.CAEConnectionBuilder.EdgeToEdgeConnectionMethodTypeEnum
    EdgeTolerance: float
    EditableNodeToNodeConnection: bool
    ElementEdge: CAE.SelectElementsBuilder
    ElementFace: CAE.SelectElementsBuilder
    ElementType: CAE.ElementTypeBuilder
    ElementTypeRbe3: CAE.ElementTypeBuilder
    Isedgeprojectableonface: int
    Ismeshtofaceconnectionpossible: int
    Label: int
    LimitConnectionToggle: bool
    Mesh: CAE.Mesh
    MethodType: CAE.CAEConnectionBuilder.MethodTypeEnum
    MidNode: bool
    NodeFaceProximity: float
    PointToEdgeConnectionMethodType: CAE.CAEConnectionBuilder.PointToEdgeConnectionMethodTypeEnum
    SearchDistance: float
    SourceGroup: CAE.CaeGroup
    SourceGroupFilterType: int
    SourceGroupReferenceState: bool
    SourceNodes: CAE.SelectFENodeList
    SourceNodesSelection: SelectTaggedObjectList
    SourceSelection: SelectTaggedObjectList
    SourceTargetDistance: float
    SpiderConnectionMethodType: CAE.CAEConnectionBuilder.SpiderConnectionMethodTypeEnum
    SpiderMesh: CAE.Mesh
    TargetGroup: CAE.CaeGroup
    TargetGroupFilterType: int
    TargetGroupReferenceState: bool
    TargetNodes: CAE.SelectFENodeList
    TargetNodesSelection: SelectTaggedObjectList
    TargetSelection: SelectTaggedObjectList
    Type: CAE.CAEConnectionBuilder.ConnectionTypeEnum


    class SpiderConnectionMethodTypeEnum(enum.Enum):
        SearchRadius = 0
        AverageNode = 1
    

    class PointToEdgeConnectionMethodTypeEnum(enum.Enum):
        PointToEdge = 0
        ArcToCenter = 1
    

    class MethodTypeEnum(enum.Enum):
        Proximity = 0
        OrderOfSelection = 1
        MeanVector = 2
        SortXcoord = 3
        SortYcoord = 4
        SortZcoord = 5
        SpiderConnection = 6
        Rbe3ToTargetFace = 7
    

    class EdgeToEdgeConnectionMethodTypeEnum(enum.Enum):
        NodeToNode = 0
        Rbe2Rbe3ToElementEdge = 1
        Rbe2Rbe3ToElementFace = 2
    

    class ConnectionTypeEnum(enum.Enum):
        NodeToNode = 0
        ElemedgeToElemface = 1
        PointToPoint = 2
        PointToEdge = 3
        PointToFace = 4
        EdgeToEdge = 5
        EdgeToFace = 6
        FaceToFace = 7
        Mesh1dToFace = 8
    

class CAEConnection(DisplayableObject):
    def __init__(self) -> None: ...
    Mesh: CAE.Mesh
    SpiderMesh: CAE.Mesh


class CaeBoundingVolumePrimitiveType(enum.Enum):
    BoxCsysAndEdgeLengths = 0
    BoxTwoDiagonalPoints = 1
    CylinderCsysDiameterAndHeight = 2
    CylinderTwoPointsAndDiameter = 3
    SphereOriginAndDiameter = 4
    ArbitraryVolume = 5


class CaeBoundingVolumePrimitiveContainment(enum.Enum):
    Inside = 0
    InsideCrossing = 1
    Outside = 2
    OutsideCrossing = 3


class CAEBody(DisplayableObject):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> float:
        ...
    def SynchronizeCadProperties(self) -> None:
        ...
    CadBody: NXObject
    IsSheetBody: bool


class CADModeling(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.FemPart) -> None: ...
    def CreateSurfaceFromPolygonFace(self, cadPart: Part, polygonFace: CAE.CAEFace) -> Features.Feature:
        ...
    def CreateCurvesFromPolygonFace(self, cadPart: Part, polygonFace: CAE.CAEFace, lines: typing.List[TaggedObject]) -> None:
        ...
    def Tag(self) -> Tag: ...



class CacheResultRecipeManager(NXObject):
    def __init__(self) -> None: ...
    def AddCacheResultRecipes(self, resTypes: typing.List[CAE.CacheResultRecipe]) -> None:
        ...
    def DeleteCacheResultRecipes(self, resTypes: typing.List[CAE.CacheResultRecipe]) -> None:
        ...
    def LoadCacheResultRecipe(self, resTypes: typing.List[CAE.CacheResultRecipe]) -> None:
        ...
    def UnloadCacheResultRecipe(self, resTypes: typing.List[CAE.CacheResultRecipe]) -> None:
        ...


class CacheResultRecipeBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEquivalentResultType(self, restype: CAE.BaseResultType) -> None:
        ...
    def SetStartIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    def SetEndIteration(self, iteration: CAE.BaseIteration) -> None:
        ...
    IterationStepSpacing: int
    IterationValueTypeFilter: CAE.BaseIteration.IterationValueType


class CacheResultRecipe(NXObject):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def GetResultTypes(self, types: typing.List[CAE.BaseResultType]) -> None:
        ...


class BushingEADBuilder(Builder):
    def __init__(self) -> None: ...
    CsysDataType: CAE.BushingEADBuilder.CoordinateSystemDataType
    Elements: CAE.SelectElementsBuilder
    OriCsystem: CoordinateSystem
    OriDirr: Direction
    OriMethod: CAE.BushingEADBuilder.OrientationMethod
    OriNode: CAE.SelectFENodeList
    OrientationState: CAE.BushingEADBuilder.State
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.BushingEADBuilder.State
    PointInPlane: Point
    PointOnZaxis: Point
    PointOrigin: Point
    PreferredLabel: int


    class State(enum.Enum):
        Apply = 0
        Clear = 1
        Ignore = 2
    

    class OrientationMethod(enum.Enum):
        Vector = 0
        Csystem = 1
        Node = 2
        CsystemData = 3
    

    class CoordinateSystemDataType(enum.Enum):
        Cartesian = 0
        Cylindrical = 1
        Spherical = 2
    

class BoxBoundingVolume(CAE.BoundingVolumePrimitive):
    def __init__(self) -> None: ...
    def GetCsysEdgelengths(self, centerCsys: CoordinateSystem, length: Expression, width: Expression, height: Expression) -> None:
        ...
    def SetCsysEdgelengths(self, centerCsys: CoordinateSystem, length: Expression, width: Expression, height: Expression) -> None:
        ...
    def GetDiagonalPoints(self, firstPoint: Point, secondPoint: Point) -> None:
        ...
    def SetDiagonalPoints(self, firstPoint: Point, secondPoint: Point) -> None:
        ...


class BoundingVolumeSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    BoundingVolume: CAE.BoundingVolumePrimitive


class BoundingVolumePrimitive(TaggedObject):
    def __init__(self) -> None: ...
    def GetCreationMethod(self) -> CAE.CaeBoundingVolumePrimitiveType:
        ...
    Containment: CAE.CaeBoundingVolumePrimitiveContainment


class BoltCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.Bolt]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.Bolt:
        ...
    def CreateBoltBuilder(self, bolt: CAE.Bolt) -> CAE.BoltBuilder:
        ...
    def Tag(self) -> Tag: ...



class BoltBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitBolt(self) -> CAE.Bolt:
        ...
    ApplyWeightsRbe3: bool
    BoltLength: Expression
    CollinearTolerance: float
    HeadEdge: SelectTaggedObjectList
    HeadPoint: SelectTaggedObjectList
    HeadSelectionType: CAE.BoltBuilder.Selection
    HeadSpiderDiameter: Expression
    HeadSpiderScale: float
    HeadSpiderType: CAE.BoltBuilder.SpiderDiameter
    HeadSurface: SelectTaggedObjectList
    Junction: bool
    Junction1Edge: SelectTaggedObjectList
    Junction1Point: SelectTaggedObjectList
    Junction1SelectionType: CAE.BoltBuilder.Selection
    Junction1SpiderDiameter: Expression
    Junction1SpiderScale: float
    Junction1SpiderType: CAE.BoltBuilder.SpiderDiameter
    Junction1Surface: SelectTaggedObjectList
    Junction2Edge: SelectTaggedObjectList
    Junction2Point: SelectTaggedObjectList
    Junction2SelectionType: CAE.BoltBuilder.Selection
    Junction2SpiderDiameter: Expression
    Junction2SpiderScale: float
    Junction2SpiderType: CAE.BoltBuilder.SpiderDiameter
    Junction2Surface: SelectTaggedObjectList
    JunctionEdge: SelectTaggedObjectList
    JunctionPoint: SelectTaggedObjectList
    JunctionSelectionType: CAE.BoltBuilder.Selection
    JunctionSpiderDiameter: Expression
    JunctionSpiderScale: float
    JunctionSpiderType: CAE.BoltBuilder.SpiderDiameter
    JunctionSurface: SelectTaggedObjectList
    JunctionTolerance: float
    Midnode: bool
    NodeTolerance: float
    NutEdge: SelectTaggedObjectList
    NutPoint: SelectTaggedObjectList
    NutSelectionType: CAE.BoltBuilder.Selection
    NutSpiderDiameter: Expression
    NutSpiderScale: float
    NutSpiderType: CAE.BoltBuilder.SpiderDiameter
    NutSurface: SelectTaggedObjectList
    OperationType: CAE.BoltBuilder.BoltOperation
    ShankElementType: CAE.ElementTypeBuilder
    SpiderElementType: CAE.ElementTypeBuilder
    Spring: bool
    TapSurface: SelectTaggedObjectList
    ThreadLength: Expression


    class SpiderDiameter(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class Selection(enum.Enum):
        Edge = 0
        Point = 1
    

    class BoltOperation(enum.Enum):
        BoltNut = 0
        BoltTap = 1
        SpiderJunction = 2
    

class Bolt(NXObject):
    def __init__(self) -> None: ...


class BodyType(enum.Enum):
    All = -1
    Solid = 0
    Sheet = 1


class BodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CAEBody]:
        ...
    def __init__(self, owner: CAE.BaseFemPart) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class BendPipeEADBuilder(Builder):
    def __init__(self) -> None: ...
    Elements: CAE.SelectElementsBuilder
    OriDirr: Direction
    OriMethod: CAE.BendPipeEADBuilder.OrientationMethod
    OriNode: CAE.SelectFENodeList
    OrientationState: CAE.BendPipeEADBuilder.State
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.BendPipeEADBuilder.State


    class State(enum.Enum):
        Apply = 0
        Clear = 1
        Ignore = 2
    

    class OrientationMethod(enum.Enum):
        Vector = 0
        Node = 1
    

class BeamSectionsCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.BeamSection]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CAE.BeamSection:
        ...
    def CreateStandardBeamSectionBuilder(self, section: CAE.StandardBeamSection) -> CAE.StandardBeamSectionBuilder:
        ...
    def CreateUserDefinedSolidBeamSectionBuilder(self, section: CAE.UserDefinedSolidBeamSection) -> CAE.UserDefinedSolidBeamSectionBuilder:
        ...
    def CreateGeneralGeometryBeamSectionBuilder(self, section: CAE.GeneralGeometryBeamSection) -> CAE.GeneralGeometryBeamSectionBuilder:
        ...
    def CopyAsGeneralGeometrySection(self, sourceSection: CAE.BeamSection) -> CAE.GeneralGeometryBeamSection:
        ...
    def CloneSection(self, sourceSection: CAE.BeamSection) -> CAE.BeamSection:
        ...
    def CreateStandardIdealizedBeamSectionBuilder(self, iBeamSection: CADCAEPrep.IBeamSection) -> CAE.StandardIdealizedBeamSectionBuilder:
        ...
    def CreateGeneralGeometryIdealizedBeamSectionBuilder(self, iBeamSection: CADCAEPrep.IBeamSection) -> CAE.GeneralGeometryIdealizedBeamSectionBuilder:
        ...
    def Tag(self) -> Tag: ...



class BeamSectionOrientationOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DirectionType: CAE.BeamSection.DirectionOption
    MethodType: CAE.BeamSectionOrientationOptions.Method
    Node: CAE.FENode
    OrientedElement: CAE.FEElement
    Vector: Direction


    class Method(enum.Enum):
        ByVector = 0
        ByNode = 1
    

class BeamSectionOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    BeamAftSection: CAE.BeamSection
    BeamForeSection: CAE.BeamSection
    BeamSectionTapered: bool
    BeamSectionTaperedChaining: bool


class BeamSectionOffsetOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AftOffset: CAE.BeamSectionOffsetOptions.Offset
    ForeOffset: CAE.BeamSectionOffsetOptions.Offset
    IsOffsetSpecified: bool
    OffsetMethodType: CAE.BeamSectionOffsetOptions.Method
    SameEndOffsets: bool


    class BeamSectionOffsetOptionsOffset():
        YEccentric: float
        ZEccentric: float
        OffsetX: Expression
        OffsetY: Expression
        OffsetZ: Expression
        def ToString(self) -> str:
            ...
    

    class Method(enum.Enum):
        Neutral = 0
        LanguageSpecific = 1
    

    class BeamSectionOffsetOptions_Offset():
        y_eccentric: float
        z_eccentric: float
        offset_x: Tag
        offset_y: Tag
        offset_z: Tag
    

class BeamSectionOccurrence(CAE.BeamSection):
    def __init__(self) -> None: ...
    PrototypeSection: CAE.BeamSection


class BeamSection(NXObject):
    def __init__(self) -> None: ...
    def GetDescriptorName(self) -> str:
        ...
    def GetStressRecoveryPoints(self, points: typing.List[Point2d]) -> None:
        ...
    PropertyTable: CAE.PropertyTable
    SectionProperties: CAE.BeamSection.Properties


    class BeamSectionProperties():
        Area: float
        PrincipalAngle: float
        MomentInertiaYY: float
        MomentInertiaZZ: float
        MomentInertiaYZ: float
        TorsionCoefficient: float
        WarpingCoefficient: float
        YEccentricity: float
        ZEccentricity: float
        PrincipalMomentInertiaYY: float
        PrincipalMomentInertiaZZ: float
        def ToString(self) -> str:
            ...
    

    class DirectionOption(enum.Enum):
        Horizontal = 0
        Vertical = 1
    

class BeamElementInfoHandler(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AskElementInfo(self, tBeamElem: CAE.FEElement) -> CAE.BeamElementInfo:
        ...


class BeamElementInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetEndReleasesAtForeEnd(self, endReleases: int) -> None:
        ...
    def GetEndReleasesAtAftEnd(self, endReleases: int) -> None:
        ...
    HasSectionAssignedAtAftEnd: bool
    HasSectionAssignedAtForeEnd: bool
    IsTapered: bool
    LanguageOffsetAtAftEnd: Vector3d
    LanguageOffsetAtForeEnd: Vector3d
    NeutralOffsetAtAftEnd: Vector3d
    NeutralOffsetAtForeEnd: Vector3d
    OffsetSectionCentroidAtAftEnd: Point3d
    OffsetSectionCentroidAtForeEnd: Point3d
    OffsetSectionShearCenterAtAftEnd: Point3d
    OffsetSectionShearCenterAtForeEnd: Point3d
    OrientationCoordinateSystem: Matrix3x3
    OrientationDirection: CAE.BeamSection.DirectionOption
    OrientationNode: CAE.FENode
    OrientationVector: Vector3d
    SectionAtAftEnd: CAE.BeamSection
    SectionAtForeEnd: CAE.BeamSection
    SectionPropertiesAtAftEnd: CAE.BeamSection.Properties
    SectionPropertiesAtForeEnd: CAE.BeamSection.Properties


class BeamEADBuilder(Builder):
    def __init__(self) -> None: ...
    Elements: CAE.SelectElementsBuilder
    EndAOffsetCSYS: CAE.BeamEADBuilder.OffsetCsysChoice
    EndBOffsetCSYS: CAE.BeamEADBuilder.OffsetCsysChoice
    EndOffsetA1: Expression
    EndOffsetA2: Expression
    EndOffsetA3: Expression
    EndOffsetAState: CAE.BeamEADBuilder.State
    EndOffsetB1: Expression
    EndOffsetB2: Expression
    EndOffsetB3: Expression
    EndOffsetBState: CAE.BeamEADBuilder.State
    EndReleaseA1: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseA2: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseA3: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseA4: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseA5: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseA6: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseAState: CAE.BeamEADBuilder.State
    EndReleaseB1: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseB2: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseB3: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseB4: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseB5: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseB6: CAE.BeamEADBuilder.EndReleaseSetting
    EndReleaseBState: CAE.BeamEADBuilder.State
    Node: CAE.SelectFENodeList
    OriMethod: CAE.BeamEADBuilder.OrientationMethod
    OrientationCsysType: CAE.BeamEADBuilder.OrientationCsys
    OrientationNodalDisplacementVector: Vector3d
    OrientationState: CAE.BeamEADBuilder.State
    PhysicalPropertyTable: CAE.PhysicalPropertyTable
    PhysicalPropertyTableState: CAE.BeamEADBuilder.State
    SelectSectionOri: Direction
    VectorChoice: CAE.BeamEADBuilder.VectorChoiceType


    class VectorChoiceType(enum.Enum):
        Horizontal = 0
        Vertical = 1
    

    class State(enum.Enum):
        Ignore = 0
        Apply = 1
        Clear = 2
    

    class OrientationMethod(enum.Enum):
        Vector = 0
        Node = 1
    

    class OrientationCsys(enum.Enum):
        Absolute = 0
        Nodal = 1
    

    class OffsetCsysChoice(enum.Enum):
        NodalDisplacement = 0
        Elemental = 1
    

    class EndReleaseSetting(enum.Enum):
        Off = 0
        On = 1
    

class BeamDisplayParameters(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    BeamDiagramScaleFactor: float
    BeamDiagramScaleMethod: CAE.BeamDisplayParameters.Method
    BeamDisplyStyle: CAE.BeamDisplayParameters.Style


    class Style(enum.Enum):
        Line = 0
        LineAndDiagram = 1
        Solid = 2
    

    class Method(enum.Enum):
        PercentModel = 0
        Absolute = 1
    

class BCSelectionDisplayBuilder(Builder):
    def __init__(self) -> None: ...
    def AskFamilyNamesByFilter(self, loadFilter: bool, constraintFilter: bool, simObjFilter: bool) -> str:
        ...
    def AskBCsByFilter(self, loadFilter: bool, constraintFilter: bool, simObjFilter: bool, familyFilterNames: str, bcs: typing.List[CAE.SimBC]) -> None:
        ...
    def AddToSelectedBCsList(self, bcs: typing.List[CAE.SimBC]) -> None:
        ...
    def RemoveFromSelectedBCsList(self, bcs: typing.List[CAE.SimBC]) -> None:
        ...
    def AskSelectedBCsList(self, bcs: typing.List[CAE.SimBC]) -> None:
        ...
    def AskOverlappingBCs(self, bcs: typing.List[CAE.SimBC], overlappingBCs: typing.List[CAE.SimBC]) -> None:
        ...
    ExcludesColor: NXColor
    OverlappingColor: NXColor
    ShowExcludes: bool
    UnspecifiedColor: NXColor
    UseUnspecified: bool


class BcLabelManagerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetBcTags(self, bcTags: typing.List[CAE.SimBC]) -> None:
        ...
    def SetBcTags(self, bcTags: typing.List[CAE.SimBC]) -> None:
        ...
    NumOfBc: int
    RenumberMethod: CAE.BcLabelManagerBuilder.RenumberType
    RenumberStartValue: int


    class RenumberType(enum.Enum):
        Renumber = 0
        Offset = 1
    

class BaseResultType(TaggedObject):
    def __init__(self) -> None: ...
    def GetSectionDefined(self) -> typing.List[CAE.Result.Section]:
        ...
    def AskComponents(self, components: typing.List[CAE.Result.Component]) -> str:
        ...
    def AskDefaultUnitForComponent(self, component: CAE.Result.Component) -> Unit:
        ...
    def AskPlies(self, plyIDs: int) -> None:
        ...
    def AskPlyLocations(self, plyID: int, locations: typing.List[CAE.Result.PlyLocation]) -> None:
        ...
    def AskShellLocations(self, shellLocations: typing.List[CAE.Result.ShellSection]) -> None:
        ...
    def AskBeamLocations(self, beamLocations: typing.List[CAE.Result.BeamSection]) -> None:
        ...
    Complex: bool
    Datatype: CAE.Result.DataType
    Location: CAE.Result.Location
    Name: str
    Quantity: CAE.Result.Quantity
    UserName: str


class BaseLoadcase(TaggedObject):
    def __init__(self) -> None: ...
    def GetIterations(self) -> typing.List[CAE.BaseIteration]:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    Name: str


class BaseIteration(TaggedObject):
    def __init__(self) -> None: ...
    def GetSubIterations(self) -> typing.List[CAE.BaseIteration]:
        ...
    def GetResultTypes(self) -> typing.List[CAE.BaseResultType]:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def HasModalMass(self) -> bool:
        ...
    def GetValueOfType(self, valueType: CAE.BaseIteration.IterationValueType) -> float:
        ...
    def GetValueTypes(self, valueType: typing.List[CAE.BaseIteration.IterationValueType]) -> None:
        ...
    def GetUnitOfType(self, valueType: CAE.BaseIteration.IterationValueType) -> Unit:
        ...
    ModalMass: float
    Name: str
    Type: CAE.BaseIteration.IterationType
    Unit: Unit
    Value: float
    ValueType: CAE.BaseIteration.IterationValueType


    class IterationValueType(enum.Enum):
        Unknown = -1
        Time = 0
        Frequency = 1
        LoadFactor = 2
        Eigenvalue = 3
        Harmonic = 4
        RotationSpeed = 5
        DesignCycle = 6
        Acoustic = 7
        BoltSequence = 8
        AeroMode = 9
    

    class IterationType(enum.Enum):
        Unknown = -1
        Static = 0
        Mode = 1
        ConstraintMode = 2
        Transient = 3
        Buckling = 4
        Nonlinear = 5
        FrequencyResponse = 6
    

class BaseFemPart(CAE.CaePart):
    def __init__(self) -> None: ...
    def GetSolverAndAnalysisType(self, solverTypeName: str, analysisTypeName: str) -> None:
        ...
    def SetSolverAndAnalysisTypeAndAbstraction(self, solverTypeName: str, analysisTypeName: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType) -> None:
        ...
    def GetAbstractionType(self) -> CAE.BaseFemPart.AxisymAbstractionType:
        ...
    def GetEnableMeshMorph(self) -> bool:
        ...
    def SetEnableMeshMorph(self, isMorphingEnabled: bool) -> None:
        ...
    def SetUseCyclicSymmetryCsys(self, useCyclicSymmetryCsys: bool) -> None:
        ...
    def GetCyclicSymmetryCsys(self) -> CoordinateSystem:
        ...
    def SetCyclicSymmetryCsys(self, cyclicSymmetryCsys: CoordinateSystem) -> None:
        ...
    def SetAxiPlaneCheckState(self, axiPlaneCheckState: bool) -> None:
        ...
    Bodies: CAE.BodyCollection
    SketchCurves: CAE.SketchCurvesCollection
    BaseFEModel: CAE.BaseFEModel
    FullPathForAssociatedCadPart: str
    UseCyclicSymmetryCsys: bool


    class AxisymAbstractionType(enum.Enum):
        None = 0
        ZxPlane = 1
        XyPlane = 2
        XxyPlane = 3
    

class BaseFEModel(CAE.IFEModel):
    def __init__(self) -> None: ...
    def UpdateFemodel(self) -> None:
        ...
    def EnableFemUpdate(self) -> None:
        ...
    def AskUpdatePending(self) -> bool:
        ...
    NodeElementMgr: CAE.NodeElementManager
    CaeConnections: CAE.CAEConnectionCollection
    MeshControls: CAE.MeshControlCollection
    Bolts: CAE.BoltCollection
    FluidDomains: CAE.FluidDomainCollection
    CfdLocalResolutionConstraints: CAE.CfdLocalResolutionConstraintCollection
    CfdContactPreventionConstraints: CAE.CfdContactPreventionConstraintCollection
    CfdAutoRefinementConstraints: CAE.CfdAutoRefinementConstraintCollection
    CaeReuseLibrary: Tooling.CaeReuseLibrary
    ConnectionElementCollection: CAE.Connections.ElementCollection
    GlobalLayupMgr: CAE.LaminateGlobalLayupMgr


class AxiSymmetricParameters(TaggedObject):
    def __init__(self) -> None: ...
    AxiOptions: CAE.AxiSymmetricParameters.Options
    EndRevolveAngle: float
    EnvelopeVal: CAE.AxiSymmetricParameters.EnvVal
    NumberOfSections: int
    ResultOption: CAE.AxiSymmetricParameters.GetResult
    RevolveAngle: float
    RotationAxis: CAE.AxiSymmetricParameters.AxisOfRotation
    StartRevolveAngle: float


    class Options(enum.Enum):
        AtRevolveAngle = 0
        EnvelopeAcrossCircumference = 1
    

    class GetResult(enum.Enum):
        OnOriginalModel = 0
        RevolvedModel = 1
    

    class EnvVal(enum.Enum):
        Maximum = 0
        Minimum = 1
        AbsoluteMaximum = 2
        AbsoluteMinimum = 3
        Average = 4
        Sum = 5
    

    class AxisOfRotation(enum.Enum):
        XAxis = 0
        YAxis = 1
        ZAxis = 2
    

class AutoPairsBuilder(Builder):
    def __init__(self) -> None: ...
    def PreviewButton(self) -> None:
        ...
    DisplayableobjectSelection: SelectDisplayableObjectList
    PropertyTable: CAE.PropertyTable


class AutoPairs(NXObject):
    def __init__(self) -> None: ...
    def SetFaces(self, faces: typing.List[CAE.CAEFace]) -> None:
        ...
    def GetFaces(self, faces: typing.List[CAE.CAEFace]) -> None:
        ...
    def SetBodies(self, faces: typing.List[CAE.CAEBody]) -> None:
        ...
    def GetBodies(self, bodies: typing.List[CAE.CAEBody]) -> None:
        ...
    def CreateFacePairs(self, side1Faces: typing.List[CAE.CAEFace], side2Faces: typing.List[CAE.CAEFace]) -> None:
        ...
    PropertyTable: CAE.PropertyTable


class AutomaticSweepBetweenSelection(Builder):
    def __init__(self) -> None: ...
    MasterFaceSelection: CAE.SelectCAEFaceList
    TargetFaceSelection: CAE.SelectCAEFaceList
    WallFaceSelection: CAE.SelectCAEFaceList


class AutomaticMorphBuilder(Builder):
    def __init__(self) -> None: ...
    AssociationTolerance: Expression
    OrphanNodeMovementOption: int
    SelectMesh: SelectTaggedObjectList


    class OrphanNodeMovementType(enum.Enum):
        BasedOnNbrMovement = 0
        Stationary = 1
    

class AutoMacViewerBuilder(Builder):
    def __init__(self) -> None: ...


class AutoHealGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    def SmallFeatureAutoSize(self) -> None:
        ...
    def TargetElementAutoSize(self) -> None:
        ...
    CurvatureAbstractionSetting: bool
    HoleDiameter: Expression
    MergeEdgeSetting: bool
    MinimumElementLengthOption: bool
    MinimumElementLengthValue: Expression
    MoveNodesOffGeometryOption: bool
    PointCreation: int
    Selection: SelectDisplayableObjectList
    SuppressHoleSetting: bool
    TargetElementSize: Expression
    Tolerance: Expression
    VertexAngle: Expression


class AutoEdgePairsBuilder(Builder):
    def __init__(self) -> None: ...
    EdgeObjectSelection: SelectDisplayableObjectList
    PropertyTable: CAE.PropertyTable


class AutoEdgePairs(NXObject):
    def __init__(self) -> None: ...


class AutoEdgeBCBuilder(Builder):
    def __init__(self) -> None: ...
    Autopairs: CAE.AutoEdgePairs
    BcBaseName: str
    DestinationFolder: CAE.SimLbcFolder
    Label: int
    PropertyTable: CAE.PropertyTable


class AutoCyclicSymmetryPairsBuilder(Builder):
    def __init__(self) -> None: ...
    def PreviewButton(self) -> None:
        ...
    GeometrySelection: CAE.SelectCAEFaceList
    PropertyTable: CAE.PropertyTable


class AutoBCBuilder(Builder):
    def __init__(self) -> None: ...
    Autopairs: CAE.AutoPairs
    BcBaseName: str
    DestinationFolder: CAE.SimLbcFolder
    Label: int
    PropertyTable: CAE.PropertyTable
    Recipe: CAE.SimAutoBcRecipe
    RetainRecipeFlag: bool


class AtvSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AtvSet]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateBuilder(self, pAtvSet: CAE.AtvSet) -> CAE.AtvSetBuilder:
        ...
    def Find(self, name: str) -> CAE.AtvSet:
        ...
    def Delete(self, atvSetTag: CAE.AtvSet) -> None:
        ...
    def Tag(self) -> Tag: ...



class AtvSetBuilder(CAE.AlternateFemRepresentationSourceBuilder):
    def __init__(self) -> None: ...


class AtvSet(CAE.AlternateFemRepresentationSource):
    def __init__(self) -> None: ...


class AttributeSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    def SetNameAttribute(self, name: str) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.SetNameAttribute instead.")"""
        ...
    def RemoveNameAttribute(self) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.RemoveNameAttribute instead.")"""
        ...
    def SetColorAttribute(self, color: int) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.SetColorAttribute instead.")"""
        ...
    def RemoveColorAttribute(self) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.RemoveColorAttribute instead.")"""
        ...
    def GetUserAttributeNames(self, userAttributeNames: str) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.GetUserAttributeNames instead.")"""
        ...
    def GetHasUserAttributes(self, attributeName: str) -> bool:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.GetHasUserAttributes instead.")"""
        ...
    def GetUserAttributes(self, attributeName: str, lowValueAttribute: NXObject.AttributeInformation, highValueAttribute: NXObject.AttributeInformation) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.GetUserAttributes instead.")"""
        ...
    def SetUserAttributes(self, attributeName: str, lowValueAttribute: NXObject.AttributeInformation, highValueAttribute: NXObject.AttributeInformation) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.SetUserAttributes instead.")"""
        ...
    def RemoveUserAttributes(self, attributeName: str) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.RemoveUserAttributes instead.")"""
        ...
    def ClearAllAttributes(self) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.ClearAllAttributes instead.")"""
        ...
    def SetUserAttributes(self, setNameAttribute: bool, nameAttribute: str, setColorAttribute: bool, colorAttribute: int, userAttributeNames: str, lowValueAttributes: typing.List[NXObject.AttributeInformation], highValueAttributes: typing.List[NXObject.AttributeInformation]) -> None:
        """[Obsolete("Deprecated in NX1847.0.0.  Use CAE.SelRecipeAttributeStrategy.SetUserAttributes instead.")"""
        ...
    ColorAttribute: int
    HasColorAttribute: bool
    HasNameAttribute: bool
    NameAttribute: str


class AttachElementsBuilder(Builder):
    def __init__(self) -> None: ...
    AttachType: CAE.AttachElementsBuilder.AttachOption
    EdgeCurve: SelectDisplayableObjectList
    ElementEdges: CAE.SelectElementsBuilder
    MeshSelection: SelectTaggedObjectList
    PointEnd: Point
    PointStart: Point
    SplitLineType: CAE.AttachElementsBuilder.SplitLineOption
    SplitSize: Expression


    class SplitLineOption(enum.Enum):
        ElementEdge = 0
        TwoPoints = 1
        Edge = 2
    

    class AttachOption(enum.Enum):
        SplitAndAttach = 0
        SplitOnly = 1
    

class AttachedElemMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetElements(self) -> typing.List[CAE.FEElement]:
        ...


class AttachedByOption(enum.Enum):
    Node = 0
    Edge = 1
    Face = 2


class AssyFemPart(CAE.BaseFemPart):
    def __init__(self) -> None: ...
    def FinalizeCreation(self, cadPart: Part, solverTypeName: str, analysisTypeType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType, description: str, useCyclicSymmetryCSYS: bool, cyclicSymmetryCsys: CoordinateSystem) -> None:
        ...
    MasterCadPart: Part


class AssyFEModel(CAE.BaseFEModel):
    def __init__(self) -> None: ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def MapFemToAssemblyComponent(self, femPart: CAE.BaseFemPart, cadPartOcc: Assemblies.Component, workLayer: bool) -> CAE.FEModelOccurrence:
        ...
    def MapFemToMultiAssemblyComponents(self, femPart: CAE.BaseFemPart, pCadPartOccs: typing.List[Assemblies.Component], workLayer: bool) -> typing.List[CAE.FEModelOccurrence]:
        ...
    def GetMappedFemOccForAssemblyComponent(self, cadPartOcc: Assemblies.Component) -> CAE.FEModelOccurrence:
        ...
    def GetAssemblyComponentForMappedFemOcc(self, femOcc: CAE.FEModelOccurrence) -> Assemblies.Component:
        ...
    def UnmapFemFromAssemblyComponent(self, cadPartOcc: Assemblies.Component) -> None:
        ...
    def RemoveFemMappedToAssemblyComponent(self, cadPartOcc: Assemblies.Component) -> None:
        ...
    def UnmapAndPreserveFemFromAssemblyComponent(self, femOcc: CAE.FEModelOccurrence) -> None:
        ...
    def GetRepositionOption(self) -> CAE.AssyFEModel.RepositionType:
        ...
    def SetRepositionOption(self, reposOption: CAE.AssyFEModel.RepositionType) -> None:
        ...
    def GetMappedComponentRemovalOption(self) -> CAE.AssyFEModel.MappedComponentRemovalType:
        ...
    def SetMappedComponentRemovalOption(self, remOption: CAE.AssyFEModel.MappedComponentRemovalType) -> None:
        ...
    def GetFreezeOption(self) -> bool:
        ...
    def SetFreezeOption(self, freezeOption: bool) -> None:
        ...
    def DeleteModelEdits(self) -> None:
        ...
    def PositionComponentByCoordinateSystem(self, femOcc: CAE.FEModelOccurrence, csys: CartesianCoordinateSystem) -> None:
        ...
    def RemovePositioningOfComponentByCoordinateSystem(self, femOcc: CAE.FEModelOccurrence) -> None:
        ...
    def LocateCoordinateSystemThatControlsComponentPositioning(self, femOcc: CAE.FEModelOccurrence) -> CartesianCoordinateSystem:
        ...
    def PositionAllComponentsByCoordinateSystems(self, startLabel: int) -> None:
        ...
    def PositionComponentsByCoordinateSystems(self, femOccs: typing.List[CAE.FEModelOccurrence], startLabel: int) -> None:
        ...
    def RemovePositioningOfComponentsByCoordinateSystem(self) -> None:
        ...
    def GetChildren(self) -> typing.List[CAE.FEModelOccurrence]:
        ...
    Parent: CAE.IFEModel


    class RepositionType(enum.Enum):
        AlwaysReposition = 0
        NeverReposition = 1
        Prompt = 2
    

    class MappedComponentRemovalType(enum.Enum):
        KeepAsUnmapped = 0
        Remove = 1
    

class AssociationUtilities(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaeSession) -> None: ...
    def ReportAssociation(self, fem: CAE.IFEModel, uiOrFile: CAE.AssociationUtilities.PrintInfoType, fileName: str) -> None:
        ...
    def Tag(self) -> Tag: ...



    class PrintInfoType(enum.Enum):
        Internal = 0
        External = 1
        All = 2
    

class AssignNodalCSBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryOptions: CAE.AssignNodalCSBuilder.GeometryOption
    CsOption: CAE.AssignNodalCSBuilder.Cs
    DispCS: CoordinateSystem
    DispCSType: CAE.AssignNodalCSBuilder.CSType
    Objects: SelectTaggedObjectList
    RefCS: CoordinateSystem
    RefCSType: CAE.AssignNodalCSBuilder.CSType
    SingleOption: bool


    class GeometryOption(enum.Enum):
        InteriorNodesOnly = 0
        BoundaryNodesOnly = 1
        InteriorandBoundaryNodes = 2
    

    class CSType(enum.Enum):
        Global = 0
        Cartesian = 1
        Cylindrical = 2
        Spherical = 3
        GlobalCyclic = 4
    

    class Cs(enum.Enum):
        DisplacementCS = 0
        ReferenceCS = 1
        Both = 2
    

class ArbitraryPolygonBodyBoundingVolume(CAE.BoundingVolumePrimitive):
    def __init__(self) -> None: ...
    def GetPolygonBody(self) -> CAE.CAEBody:
        ...
    def SetPolygonBody(self, body: CAE.CAEBody) -> None:
        ...


class ArbitraryMeshBoundingVolume(CAE.BoundingVolumePrimitive):
    def __init__(self) -> None: ...
    def GetMesh(self) -> CAE.Mesh:
        ...
    def SetMesh(self, mesh: CAE.Mesh) -> None:
        ...


class AMSupportsMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPrintedBodyMeshes(self, pptPrintedBodyMeshes: typing.List[CAE.Mesh]) -> None:
        ...
    def CreateAmSupportObject(self, tFacetBodyOfSupport: Facet.FacetedBody, supportType: CAE.AMSupportObject.SupportType, meshName: str) -> CAE.AMSupportObject:
        ...
    def GetSupportObjects(self, pptSupportObjects: typing.List[CAE.AMSupportObject]) -> None:
        ...
    def GetSupportMeshes(self, pptSupportMeshes: typing.List[CAE.Mesh]) -> None:
        ...
    def GetPowderMeshes(self, pptPowderMeshes: typing.List[CAE.Mesh]) -> None:
        ...
    def AddPrintedBody(self, printedBody: CAE.CAEBody, elemSize: float) -> None:
        ...
    BuildVolumeBody: CAE.SelectCAEBodyList
    PrintedBodySelection: CAE.SelectCAEBodyList
    PropertyTable: CAE.PropertyTable


class AMSupportObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetSupport(self, support: TaggedObject) -> None:
        ...
    def GetFacetBody(self) -> Facet.FacetedBody:
        ...
    def GetSupportType(self) -> CAE.AMSupportObject.SupportType:
        ...
    def SetSupportType(self, supportType: CAE.AMSupportObject.SupportType) -> None:
        ...
    def ComputeResolution(self) -> float:
        ...
    def ComputeCharacteristicLength(self) -> float:
        ...
    def ComputeGluingDistanceToSpecimen(self) -> float:
        ...
    def GetMeshName(self) -> str:
        ...
    def SetMeshName(self, meshName: str) -> None:
        ...
    CreationInterface: SelectDisplayableObjectList
    PropertyTable: CAE.PropertyTable


    class SupportType(enum.Enum):
        Undefined = 0
        Volume = 1
        Block = 2
        Contour = 3
        Web = 4
        Cone = 5
        Tree = 6
        Line = 7
        Point = 8
        User = 9
        Gusset = 10
        Combined = 11
    

class AlternateFemRepSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    NodeLabel: int


class AlternateFemRepresentationSourceBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitAlternateFemRepresentationSource(self) -> CAE.AlternateFemRepresentationSource:
        ...
    def SetName(self, name: str) -> None:
        ...
    def SetFilePath(self, filepath: str) -> None:
        ...
    def SetResultReference(self, pResultRef: CAE.SimResultReference) -> None:
        ...
    def GetDatabaseOptions(self) -> CAE.DataReaderDatabaseOptions:
        ...
    def SetLengthUnit(self, lengthUnit: Unit) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.AlternateFemRepresentationSourceBuilder.GetDatabaseOptionsinstead.")"""
        ...
    def SetMassUnit(self, massUnit: Unit) -> None:
        """[Obsolete("Deprecated in NX1872.0.0.  Use NXOpen.CAE.AlternateFemRepresentationSourceBuilder.GetDatabaseOptionsinstead.")"""
        ...
    def SetMeshCreationMode(self, creationMode: CAE.AlternateFemRepresentationSource.CreateMeshMode) -> None:
        ...
    def GetMeshDatabaseOptions(self) -> CAE.DataReaderDatabaseOptions:
        ...
    def SetMeshFileSpec(self, filepath: str) -> None:
        ...
    def SetMeshResultReference(self, pResultRef: CAE.SimResultReference) -> None:
        ...
    def SetMeshFeModel(self, feModel: CAE.IFEModel) -> None:
        ...
    def SetMainDataSourceAsMeshSource(self) -> None:
        ...
    def GetDataSourceNames(self) -> str:
        ...
    def GetNewDataSourceBuilder(self) -> CAE.AlternateFemRepresentationDataSourceBuilder:
        ...
    def RemoveDataSourceBuilder(self, sourceBuilder: CAE.AlternateFemRepresentationDataSourceBuilder) -> None:
        ...
    def GetMainDataSourceBuilder(self) -> CAE.AlternateFemRepresentationDataSourceBuilder:
        ...
    def GetDataSourceBuilder(self, dataSourceName: str) -> CAE.AlternateFemRepresentationDataSourceBuilder:
        ...
    PropertyTable: BasePropertyTable


class AlternateFemRepresentationSource(TaggedObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...
    def ForceUpdate(self) -> None:
        ...
    def HasNodeIdMappings(self) -> bool:
        ...
    def GetNodeIdMappings(self) -> typing.List[CAE.AlternateFemRepresentationSource.NameLabelPair]:
        ...
    def InsertNamedNodeWithLabel(self, recipeNameString: str, nodeLabel: int) -> None:
        ...
    def InsertNamedNodeWithNodeId(self, recipeNameString: str, nodeIDString: str) -> None:
        ...
    def ClearNamedNodes(self) -> None:
        ...
    def GetReplacedFeModelOccs(self) -> typing.List[CAE.FEModelOccurrence]:
        ...
    def InsertSelectionRecipeMappingWithNodeId(self, feModelOccTag: CAE.FEModelOccurrence, pSelectionRecipe: CAE.SelectionRecipe, nodeIDString: str) -> None:
        ...
    def InsertSelectionRecipeMappingWithLabel(self, feModelOccTag: CAE.FEModelOccurrence, pSelectionRecipe: CAE.SelectionRecipe, nodeLabel: int) -> None:
        ...
    def RemoveSelectionRecipeMapping(self, feModelOccTag: CAE.FEModelOccurrence, pSelectionRecipe: CAE.SelectionRecipe) -> None:
        ...
    def GetMappedSelectionRecipes(self, feModelOccTag: CAE.FEModelOccurrence) -> typing.List[CAE.SelectionRecipe]:
        ...
    def GetAltRepSelectionRecipes(self, pptFeModelOccTags: typing.List[CAE.FEModelOccurrence], pppSelectionRecipe: typing.List[CAE.SelectionRecipe]) -> None:
        ...
    def GetNamedNodesWithNodeId(self) -> typing.List[CAE.AlternateFemRepresentationSource.NameIdentifierPair]:
        ...
    def GetNamedNodesWithLabel(self) -> typing.List[CAE.AlternateFemRepresentationSource.NameLabelPair]:
        ...
    def Information(self, showWarnings: bool) -> None:
        ...
    def CreateSingleLabelSelectionRecipes(self, updateExistingRecipes: bool, componentTag: TaggedObject) -> None:
        ...
    def CreateCoordinateSelectionRecipes(self, updateExistingRecipes: bool, componentTag: TaggedObject, tolerance: float, resolvePreference: CAE.SelRecipeCoordinateStrategy.Pref) -> None:
        ...
    PropertyTable: BasePropertyTable


    class AlternateFemRepresentationSourceNameLabelPair():
        Name: str
        Label: int
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, Label: int) -> None: ...
    

    class AlternateFemRepresentationSourceNameIdentifierPair():
        Name: str
        Identifier: str
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, Identifier: str) -> None: ...
    

    class CreateMeshMode(enum.Enum):
        AllElements = 0
        DataElements = 1
        VisualizationElements = 2
    

    class AlternateFemRepresentationSource_NameLabelPair():
        name: int
        label: int
    

    class AlternateFemRepresentationSource_NameIdentifierPair():
        name: int
        identifier: int
    

class AlternateFemRepresentationDataSourceBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetFilePath(self, filepath: str) -> None:
        ...
    def SetResultReference(self, pResultRef: CAE.SimResultReference) -> None:
        ...
    def GetDatabaseOptions(self) -> CAE.DataReaderDatabaseOptions:
        ...


class AfuZHeaderInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    GeneralValue: float
    OrderValue: float
    RpmValue: float
    TimeValue: float
    Unit: CAE.XyFunctionUnit


class AfuOrdinateHeaderInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AxisLabel: str
    Damping: float
    DataFormat: int
    ImaginaryOffset: float
    ImaginaryScale: float
    RealOffset: float
    RealScale: float
    UnitLabel: str


class AfuMathOperation(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.AfuManager) -> None: ...
    def CalculateSingleMathScaleByReal(self, scaleValue: float, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathScaleByComplex(self, scaleRealValue: float, scaleImaginaryValue: float, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathOffsetByReal(self, offsetValue: float, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathOffsetByComplex(self, offsetRealValue: float, offsetImaginaryValue: float, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathShiftAbscissa(self, shiftValue: float, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathSignValue(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathAbsoluteValue(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathComplexConjugate(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathFourierTransform(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathLinearInterpolation(self, outerInterpolation: CAE.AfuMathOperation.OuterInterpolation, newXIncrement: float, newXMinimum: float, newXMaximum: float, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathLagrangianInterpolation(self, polynomialOrder: int, outerInterpolation: CAE.AfuMathOperation.OuterInterpolation, newXIncrement: float, newXMinimum: float, newXMaximum: float, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathSquareRoot(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathSquareMagnitude(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathMovingAverage(self, movingAverageNumber: int, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathInverse(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathIndependentIntegration(self, gUnitInchFormat: bool, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathIndependentIntegration(self, gUnitInchFormat: bool, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, correctionType: CAE.AfuMathOperation.RigidCorrectionType) -> None:
        ...
    def CalculateSingleMathIndependentDifferentiation(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathFrequencyIntegration(self, gUnitInchFormat: bool, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathIntegration(self, gUnitInchFormat: bool, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, correctionType: CAE.AfuMathOperation.RigidCorrectionType, doDoubleIntegration: bool) -> None:
        ...
    def CalculateSingleMathFrequencyDifferentiation(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathDifferentiation(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, doDoubledifferentiation: bool) -> None:
        ...
    def NewFastRmsInfo(self) -> CAE.AfuMathFastRMSInfo:
        ...
    def NewFastRmsOutput(self) -> CAE.AfuMathFastRMSOutput:
        ...
    def CalculateAndStoreFastRmsPsdFit(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, fastRmsInfo: CAE.AfuMathFastRMSInfo) -> CAE.AfuMathFastRMSOutput:
        ...
    def CalculateMultiMathRecords(self, multiMathType: CAE.AfuMathOperation.MultiType, sourceAfuFileName1: str, sourceRecordIndex1: int, sourceAfuFileName2: str, sourceRecordIndex2: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateOverallMathRecords(self, overallType: CAE.AfuMathOperation.Overall, sourceAfuFileNames: str, sourceRecordIndexes: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def SynchronizeRecords(self, newIncrement: float, interpolationMode: CAE.AfuMathOperation.InterpolationMode, shiftToStartPoint: bool, sourceAfuFileNames: str, sourceRecordIndexes: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def SrsToTime(self, inputAfuFileName: str, inputRecordId: int, conversionOption: CAE.AfuMathOperation.SrsToTimeOption, dampingRatio: float, numTimePoints: int, iterations: int, octave: CAE.AfuMathOperation.SrsToTimeOctave, numTrials: int, strategy: CAE.AfuMathOperation.SrsToTimeStrategy, saveSrsResults: bool, outputAfuFileName: str, outputRecordName: str) -> None:
        ...
    def SrsToTime(self, inputAfuFileName: str, inputRecordId: int, conversionOption: CAE.AfuMathOperation.SrsToTimeOption, dampingRatio: float, numTimePoints: int, iterations: int, octave: CAE.AfuMathOperation.SrsToTimeOctave, numTrials: int, strategy: CAE.AfuMathOperation.SrsToTimeStrategy, saveSrsResults: bool, outputAfuFileName: str, outputRecordName: str, outputType: CAE.AfuMathOperation.OutputType) -> None:
        ...
    def TimeToSrs(self, inputAfuFileName: str, inputRecordId: int, dampingRatio: float, freqAxisType: CAE.AfuMathOperation.TimeToSrsAxisType, frequencyMin: float, frequencyMax: float, frequenceIncrement: float, pointsPerDecades: int, responseType: CAE.AfuMathOperation.TimeToSrsResponseType, outputAfuFileName: str, outputRecordName: str) -> None:
        ...
    def TimeToSrs(self, inputAfuFileName: str, inputRecordId: int, dampingRatio: float, freqAxisType: CAE.AfuMathOperation.TimeToSrsAxisType, frequencyMin: float, frequencyMax: float, frequenceIncrement: float, pointsPerDecades: int, responseType: CAE.AfuMathOperation.TimeToSrsResponseType, fSetEndZeros: bool, outputAfuFileName: str, outputRecordName: str) -> None:
        ...
    def TimeToSrs(self, inputAfuFileName: str, inputRecordId: int, dampingRatio: float, freqAxisType: CAE.AfuMathOperation.TimeToSrsAxisType, frequencyMin: float, frequencyMax: float, frequenceIncrement: float, pointsPerDecades: int, responseType: CAE.AfuMathOperation.TimeToSrsResponseType, fSetEndZeros: bool, outputAfuFileName: str, outputRecordName: str, outputType: CAE.AfuMathOperation.OutputType) -> None:
        ...
    def TimeToPsd(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def PsdToTime(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, newXIncrement: float, numTimePoints: int, seed: int, interpolationMode: CAE.AfuMathOperation.InterpolationMode) -> None:
        ...
    def FftAveraging(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, averagingMethod: CAE.AfuMathOperation.FttAveragingMethod, exponentialValue: int, firstStartPoint: int, frameSize: int, overlapPercentage: float, framesPerAverage: int) -> None:
        ...
    def EnvelopeLine(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, envelopeType: CAE.AfuMathOperation.EnvelopeType, dataFormat: CAE.AfuMathOperation.DataFormat) -> None:
        ...
    def InterpolateData(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str, numberOfPoints: int, interpolationMode: CAE.AfuMathOperation.InterpolationMode) -> None:
        ...
    def Tag(self) -> Tag: ...



    class TimeToSrsResponseType(enum.Enum):
        PositiveMax = 1
        NegativeMax = 2
        AbsoluteMax = 3
    

    class TimeToSrsAxisType(enum.Enum):
        Linear = 1
        Log = 2
        Octave = 3
        OneThirdOctave = 4
        Decade = 5
    

    class SrsToTimeStrategy(enum.Enum):
        Random = 1
        ReverseSineSweep = 2
        Combination = 3
    

    class SrsToTimeOption(enum.Enum):
        DampedSinusoid = 1
        Wavelet = 2
    

    class SrsToTimeOctave(enum.Enum):
        OneThird = 1
        OneSixth = 2
        OneTwelfth = 3
    

    class RigidCorrectionType(enum.Enum):
        None = 0
        ZeroMean = 1
    

    class Overall(enum.Enum):
        MinimumValue = 0
        MaximumValue = 1
        MinimumMagnitude = 2
        MaximumMagnitude = 3
        MeanMagnitude = 4
        SumMagnitude = 5
        SumComplex = 6
    

    class OutputType(enum.Enum):
        Append = 0
        Overwrite = 1
        OtherFile = 2
    

    class OuterInterpolation(enum.Enum):
        Zero = 0
        Curve = 1
    

    class MultiType(enum.Enum):
        Add = 0
        Subtract = 1
        Multiple = 2
        Conjugate = 3
        Divide = 4
    

    class InterpolationMode(enum.Enum):
        LinearLinear = 0
        LogLog = 1
        LogLinear = 2
        LinearLog = 3
    

    class FttAveragingMethod(enum.Enum):
        Linear = 0
        Exponential = 1
        PeakHold = 2
    

    class EnvelopeType(enum.Enum):
        Upward = 0
        Downward = 1
    

    class DataFormat(enum.Enum):
        Magnitude = 0
        Real = 1
        Imaginary = 2
    

class AfuMathFastRMSOutput(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetRmsError(self) -> float:
        ...
    def SetRmsError(self, rmsError: float) -> None:
        ...
    def SetPsdfitOriginalData(self, psdfitOriginalX: float, psdfitOriginalY: float) -> None:
        ...
    def GetPsdfitOriginalData(self, psdfitOriginalX: float) -> float:
        ...
    def SetPsdfitFittedData(self, psdfitFittedX: float, psdfitFittedY: float, abcd: float, psdfitFreqValue1: float, psdfitFreqValue2: float) -> None:
        ...
    def GetPsdfitFittedData(self, psdfitFittedX: float, psdfitFittedY: float, abcd: float, psdfitFreqValue1: float) -> float:
        ...


class AfuMathFastRMSInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetData(self, numberOfPoints: int, order: int, relativeOrder: int, useHighpassFilter: int, cutoffFraction: float, addSidelobes: int, slope: float, interpolationMethod: int) -> None:
        ...
    def GetData(self, numberOfPoints: int, order: int, relativeOrder: int, useHighpassFilter: int, cutoffFraction: float, addSidelobes: int, slope: float) -> int:
        ...


class AfuManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateRecord(self, macroType: CAE.XyFunctionMacroType, dataType: CAE.XyFunctionGeneralType, afuData: CAE.AfuData) -> str:
        ...
    def CreateRecordsFromPunchFile(self, sourcePchFileNames: str, destinationAfuFileName: str, requestedFunctions: typing.List[CAE.AfuManager.RequestedMeasureType]) -> None:
        ...
    def EditRecord(self, macroType: CAE.XyFunctionMacroType, dataType: CAE.XyFunctionGeneralType, afuRecordIndex: int, afuData: CAE.AfuData) -> str:
        ...
    def CopyRecords(self, sourceAfuFileNames: str, recordIndexes: int, destinationAfuFileName: str) -> None:
        ...
    def DeleteRecords(self, afuFileName: str, afuRecordIndexes: int) -> None:
        ...
    def GetAfuData(self, afuFileName: str, recordIndex: int, afuData: CAE.AfuData) -> str:
        ...
    def CreateAfuData(self, abscissaType: CAE.AfuData.AbscissaType) -> CAE.AfuData:
        ...
    def CreateNewAfuFile(self, afuFileName: str) -> None:
        ...
    def DeleteAfuFile(self, afuFileName: str) -> None:
        ...
    def ImportAfu(self, importFileName: str, afuFileName: str) -> None:
        ...
    def ExportAfu(self, afuFileName: str, recordIndex: int, exportFileName: str) -> None:
        ...
    def RenameRecord(self, afuFileName: str, recordIndex: int, newRecordName: str) -> None:
        ...
    def GetRecordIndexes(self, afuFileName: str) -> int:
        ...
    def ListRecordInformation(self, afuFileName: str, recordIndex: int, listPointData: bool, outputFileName: str, mode: CAE.AfuManager.WritingFileMode) -> None:
        ...
    def ListFileInformation(self, afuFileName: str, listPointData: bool, outputFileName: str, mode: CAE.AfuManager.WritingFileMode) -> None:
        ...
    def ExportAfuFile(self, afuFileName: str, exportFileName: str) -> None:
        ...
    def CreateRecord(self, afuData: CAE.AfuData) -> None:
        ...
    def EditRecord(self, afuRecordIndex: int, afuData: CAE.AfuData) -> None:
        ...
    def CreateAfuHeaderId(self) -> CAE.AfuHeaderId:
        ...
    def GetAfuUnitTypeText(self, unit: CAE.XyFunctionUnit) -> str:
        ...
    def GetAfuUnitText(self, unit: CAE.XyFunctionUnit) -> str:
        ...
    def CreateAfuAbscissaHeaderInfo(self) -> CAE.AfuAbscissaHeaderInfo:
        ...
    def CreateAfuOrdinateHeaderInfo(self) -> CAE.AfuOrdinateHeaderInfo:
        ...
    def CreateAfuZHeaderInfo(self) -> CAE.AfuZHeaderInfo:
        ...
    def Tag(self) -> Tag: ...

    AfuDataConvertor: CAE.AfuDataConvertor
    AfuDataCreator: CAE.AfuDataCreator
    AfuMathOperation: CAE.AfuMathOperation


    class WritingFileMode(enum.Enum):
        Override = 0
        Append = 1
    

    class RequestedMeasureType(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
        Pressure = 3
    

class AfuHeaderId(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Coordinate: int
    IdLine1: str
    IdLine2: str
    IdLine3: str
    IdLine4: str
    LoadCase: int
    Owner: str
    Reference: str
    ReferenceId: int
    Response: str
    ResponseId: int
    Version: int


class AfuDataCreator(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.AfuManager) -> None: ...
    def GetHalfSineData(self, afuFileName: str, recordName: str, amplitude: float, timePeriod: float, numberOfCycles: int, numberOfIntervals: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetFullSineData(self, afuFileName: str, recordName: str, amplitude: float, timePeriod: float, fullCycle: bool, numberOfCycles: int, numberOfIntervals: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetHaversineData(self, afuFileName: str, recordName: str, amplitude: float, timePeriod: float, numberOfCycles: int, numberOfIntervals: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetFullHaversineData(self, afuFileName: str, recordName: str, amplitude: float, timePeriod: float, fullCycle: bool, numberOfCycles: int, numberOfIntervals: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetTriangleData(self, afuFileName: str, recordName: str, amplitude: float, timePeriod: float, numberOfCycles: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetSquareData(self, afuFileName: str, recordName: str, amplitude: float, width: float, timePeriod: float, numberOfCycles: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetRampData(self, afuFileName: str, recordName: str, amplitude: float, width: float, timePeriod: float, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetRandomSignalData(self, afuFileName: str, recordName: str, minimumTime: float, maximumTime: float, timeIncrement: float, amplitude: float, mean: float, stamdardDeviation: float, seed: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetUnbalancedForceData(self, afuFileName: str, recordName: str, width: float, frequencyIncrement: float, mass: float, eccentricity: float, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetRectangleData(self, afuFileName: str, recordName: str, amplitude: float, initialWidth: float, signalWidth: float, finalWidth: float, numberOfCycles: int, ordinateUnitType: CAE.XyFunctionUnit, abscissaUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def GetPsdExcitationData(self, afuFileName: str, recordName: str, amplitude: float, positiveSlope: float, negativeSlope: float, firstFrequencyPoint: float, secondFrequencyPoint: float, thirdFrequencyPoint: float, fourthFrequencyPoint: float, ordinateUnitType: CAE.XyFunctionUnit) -> CAE.AfuData:
        ...
    def Tag(self) -> Tag: ...



class AfuDataConvertor(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.AfuManager) -> None: ...
    def GetFftComplexType(self, fftType: CAE.AfuDataConvertor.Fft, inComplexType: CAE.AfuData.OrdinateType) -> CAE.AfuData.OrdinateType:
        ...
    def GetFftFrequencyData(self, inXValues: float, inYValues: float, xValues: float, yValues: float) -> float:
        ...
    def GetFftTimeData(self, inXValues: float, inYValues: float, inZValues: float, xValues: float) -> float:
        ...
    def Tag(self) -> Tag: ...



    class Fft(enum.Enum):
        Forward = 1
        Inverse = 2
    

class AfuData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetAbscissaAndOrdinateAxisDefinition(self, xUnit: CAE.XyFunctionUnit, ordinateType: CAE.AfuData.OrdinateType, yUnit: CAE.XyFunctionUnit, yDenominatorUnit: CAE.XyFunctionUnit) -> None:
        ...
    def GetAbscissaAndOrdinateAxisDefinition(self, abscissaType: CAE.AfuData.AbscissaType, xUnit: CAE.XyFunctionUnit, ordinateType: CAE.AfuData.OrdinateType, yUnit: CAE.XyFunctionUnit, yDenominatorUnit: CAE.XyFunctionUnit) -> None:
        ...
    def GetEvenData(self, xMinimum: float, xIncrement: float, numberOfPoints: int) -> None:
        ...
    def SetRealData(self, xValues: float, yValues: float) -> None:
        ...
    def SetRealData(self, xMinimum: float, xIncrement: float, yValues: float) -> None:
        ...
    def GetRealData(self, xValues: float) -> float:
        ...
    def SetComplexData(self, xValues: float, yValues: float, zValues: float) -> None:
        ...
    def SetComplexData(self, xMinimum: float, xIncrement: float, yValues: float, zValues: float) -> None:
        ...
    def GetComplexData(self, xValues: float, yValues: float) -> float:
        ...
    AbscissaSpacingType: CAE.AfuData.AbscissaType
    AbscissaUnit: CAE.XyFunctionUnit
    AfuAbscissaHeaderInfo: CAE.AfuAbscissaHeaderInfo
    AfuHeaderId: CAE.AfuHeaderId
    AfuOrdinateHeaderInfo: CAE.AfuOrdinateHeaderInfo
    AfuZHeaderInfo: CAE.AfuZHeaderInfo
    Extrapolation: CAE.AfuData.ExtrapolationType
    FileName: str
    FunctionDataType: CAE.XyFunctionDataType
    Interpolation: CAE.AfuData.InterpolationType
    OrdinateDataType: CAE.AfuData.OrdinateType
    OrdinateDenominatorUnit: CAE.XyFunctionUnit
    OrdinateSecondNumeratorUnit: CAE.XyFunctionUnit
    OrdinateUnit: CAE.XyFunctionUnit
    RecordName: str


    class OrdinateType(enum.Enum):
        Real = 0
        RealImaginary = 1
        MagnitudePhase = 2
    

    class InterpolationType(enum.Enum):
        Cubic = 0
        Akima = 1
        Akima72 = 2
        Linear = 3
    

    class ExtrapolationType(enum.Enum):
        Linear = 0
        Parabolic = 1
    

    class AbscissaType(enum.Enum):
        Even = 0
        Uneven = 1
    

class AfuAbscissaHeaderInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AxisLabel: str
    RealOffset: float
    RealScale: float
    Spacing: int
    UnitLabel: str


class AeroStructManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def Tag(self) -> Tag: ...

    MarginSolutionCollection: CAE.AeroStructures.MarginSolutionCollection
    LoadFilteringSolutionCollection: CAE.AeroStructures.LoadFilteringSolutionCollection


class AeroMeshCheckBuilder(Builder):
    def __init__(self) -> None: ...
    CheckScope: CAE.AeroMeshCheckBuilder.Scope
    DisplaySettingsData: CAE.AeroMeshCheckBuilder.DisplaySettings
    MeshSelection: SelectTaggedObjectList


    class Scope(enum.Enum):
        Displayed = 0
        Selected = 1
    

    class AeroMeshCheckBuilderDisplaySettings():
        ShowIncorrectMeshes: bool
        MeshColor: NXColor
        MeshWidth: DisplayableObject.ObjectWidth
        def ToString(self) -> str:
            ...
        def __init__(self, ShowIncorrectMeshes: bool, MeshColor: NXColor, MeshWidth: DisplayableObject.ObjectWidth) -> None: ...
    

    class AeroMeshCheckBuilder_DisplaySettings():
        showIncorrectMeshes: bool
        meshColor: int
        meshWidth: DisplayableObject.ObjectWidth
    

class AdjacentFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
        ...


class AdaptivityMetaSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AdaptivityMetaSolution]:
        ...
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.AdaptivityMetaSolution:
        ...
    def CreateBuilder(self, metasolution: CAE.AdaptivityMetaSolution) -> CAE.AdaptivityMetaSolutionBuilder:
        ...
    def Tag(self) -> Tag: ...



class AdaptivityMetaSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable


class AdaptivityMetaSolution(NXObject):
    def __init__(self) -> None: ...
    def Solve(self) -> None:
        ...
    AdaptivityExclusionZones: CAE.AdaptivityExclusionZoneCollection


class AdaptivityExclusionZoneCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AdaptivityExclusionZone]:
        ...
    def __init__(self, owner: CAE.AdaptivityMetaSolution) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.AdaptivityExclusionZone:
        ...
    def CreateExclusionZoneBuilder(self, exclusionZone: CAE.AdaptivityExclusionZone) -> CAE.AdaptivityExclusionZoneBuilder:
        ...
    def Tag(self) -> Tag: ...



class AdaptivityExclusionZoneBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable


class AdaptivityExclusionZone(NXObject):
    def __init__(self) -> None: ...


class AcousticsPanelGenerator(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Acoustics) -> None: ...
    def GenerateFromAllGroups(self) -> None:
        ...
    def Generate(self, pGroups: typing.List[CAE.CaeGroup]) -> None:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationVibrationDataComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    def GetQuantityAndSorting(self, quantity: CAE.AcousticsAndVibrationVibrationDataComponentAccessor.QuantityEnum, sorting: CAE.AcousticsAndVibrationVibrationDataComponentAccessor.SortingEnum) -> None:
        ...
    def SetQuantityAndSorting(self, quantity: CAE.AcousticsAndVibrationVibrationDataComponentAccessor.QuantityEnum, sorting: CAE.AcousticsAndVibrationVibrationDataComponentAccessor.SortingEnum) -> None:
        ...
    def GetSubcases(self, subcaseNames: str) -> None:
        ...
    def SetSubcases(self, subcaseNames: str) -> None:
        ...
    Abscissa: CAE.AcousticsAndVibrationVibrationDataComponentAccessor.AbscissaEnum
    DatabaseOptions: CAE.DataReaderDatabaseOptions
    FilePath: str


    class SortingEnum(enum.Enum):
        Vectors = 0
        Functions = 1
    

    class QuantityEnum(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
    

    class AbscissaEnum(enum.Enum):
        Frequency = 0
        AngularVelocity = 1
    

class AcousticsAndVibrationVibrationDataComponent(NXObject):
    def __init__(self) -> None: ...
    def CreateSelectionRecipes(self) -> None:
        ...


class AcousticsAndVibrationVatvSelectionComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    FilePath: str
    SelectionChoice: CAE.AcousticsAndVibrationVatvSelectionComponentAccessor.SelectionChoiceEnum
    SourceObject: TaggedObject


    class SelectionChoiceEnum(enum.Enum):
        Resultnode = 0
        Datafile = 1
    

class AcousticsAndVibrationVatvSelectionComponent(NXObject):
    def __init__(self) -> None: ...
    def LoadMesh(self) -> None:
        ...
    def UnloadMesh(self) -> None:
        ...


class AcousticsAndVibrationTransientMeshSelectionAccessor(NXObject):
    def __init__(self) -> None: ...
    def SetSelectedEntities(self, entityType: CAE.AcousticsAndVibrationTransientMeshSelectionAccessor.IntermediateEntity, intermidiateFaces: int) -> None:
        ...
    UseCustomSelection: bool


    class IntermediateEntity(enum.Enum):
        ElementFace = 0
        Element = 1
    

class AcousticsAndVibrationTblModelParametersAccessor(NXObject):
    def __init__(self) -> None: ...
    def GetNumUserDefinedExpressions(self) -> int:
        ...
    def GetNthUserDefinedExpression(self, expressionIndex: int, expressionName: str, userExpression: Expression) -> None:
        ...
    def LoadUserDefinedDll(self) -> None:
        ...
    AutoSpectrumField: Fields.FieldWrapper
    AutoSpectrumType: CAE.AcousticsAndVibrationTblModelParametersAccessor.AsType
    BoundaryLayerThicknessParam: Expression
    ConvectiveVelocityXParam: Expression
    ConvectiveVelocityYParam: Expression
    ConvectiveVelocityZParam: Expression
    CorrelationDecayRateAlphaParam: Expression
    CorrelationDecayRateBetaParam: Expression
    CorrelationSpectrumType: CAE.AcousticsAndVibrationTblModelParametersAccessor.CsType
    CorrelationSpectrumUserDLL: str
    DisplacementThicknessParam: Expression
    FluidDensityParam: Expression
    FluidOuterVelocityParam: Expression
    FluidViscosityParam: Expression
    MomentumThicknessParam: Expression
    SoundSpeedParam: Expression
    WallFrictionVelocityParam: Expression
    WallShearStressParam: Expression


    class CsType(enum.Enum):
        Corcos = 0
        Efimtsov = 1
        Chase = 2
        UserDefined = 3
    

    class AsType(enum.Enum):
        RobertCorcos = 0
        Efimtsov = 1
        Goody = 2
        Smolyakov = 3
        CockburnRobertson = 4
        SmolyakovTkachenko = 5
        ChaseHowe = 6
        UserDefined = 7
    

class AcousticsAndVibrationSolverParametersComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    Memory: float
    NumThreads: int
    PresolverPath: str
    SolverPath: str
    SolverTemperatureUnitType: CAE.AcousticsAndVibrationSolverParametersComponentAccessor.TuType
    SolverUnitSystemType: CAE.AcousticsAndVibrationSolverParametersComponentAccessor.UsType
    SpecifyTemperatureUnit: bool
    SysnoisePath: str
    TargetOperatingSystemFamily: CAE.AcousticsAndVibrationSolverParametersComponentAccessor.TargetOsFamily
    TempDir: str
    UseEnvVar: bool
    UseModelDirForSolverTempFiles: bool
    UsePresolverEnvVar: bool
    UseRunInForeground: bool
    UseSysnoiseEnvVar: bool


    class UsType(enum.Enum):
        FromInputFile = 0
        SiMeterNewton = 1
        BgFootPoundForce = 2
        MgMeterKilogramForce = 3
        BaFootPoundal = 4
        MmMillimeterMilliNewton = 5
        CmCentimeterCentiNewton = 6
        InInchPoundForce = 7
        GmMillimeterKilogramForce = 8
        MnMillimeterMilliNewton = 9
    

    class TuType(enum.Enum):
        Celsius = 0
        Fahrenheit = 1
        Kelvin = 2
        Rankine = 3
    

    class TargetOsFamily(enum.Enum):
        Windows = 0
        Unix = 1
        Autodetect = 2
    

class AcousticsAndVibrationSolutionOptionsComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    CsysType: CAE.AcousticsAndVibrationSolutionOptionsComponentAccessor.CsysTypeEnum
    MaxNumOfExposedFunctions: int


    class CsysTypeEnum(enum.Enum):
        Native = 0
        Absolute = 1
    

class AcousticsAndVibrationRandomVatvResponseSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AcousticsAndVibrationRandomVatvResponseSolution]:
        ...
    def __init__(self, owner: CAE.AcousticsAndVibrationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.AcousticsAndVibrationRandomVatvResponseSolution:
        ...
    def Create(self) -> CAE.AcousticsAndVibrationRandomVatvResponseSolution:
        ...
    def Delete(self, solution: CAE.AcousticsAndVibrationRandomVatvResponseSolution) -> None:
        ...
    def CloneSolution(self, solution: CAE.AcousticsAndVibrationRandomVatvResponseSolution) -> CAE.AcousticsAndVibrationRandomVatvResponseSolution:
        ...
    def CreateBuilder(self, solution: CAE.AcousticsAndVibrationRandomVatvResponseSolution) -> CAE.AcousticsAndVibrationRandomVatvResponseSolutionBuilder:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationRandomVatvResponseSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    RandomOutputRequests: CAE.AcousticsAndVibrationRandomOutputRequestsComponentAccessor
    SolutionName: str
    SolverParameters: CAE.AcousticsAndVibrationSolverParametersComponentAccessor
    TblModel: CAE.AcousticsAndVibrationTblModelParametersAccessor
    TblTransientMeshSelector: CAE.AcousticsAndVibrationTransientMeshSelectionAccessor
    VatvSelection: CAE.AcousticsAndVibrationVatvSelectionComponentAccessor


class AcousticsAndVibrationRandomVatvResponseSolution(NXObject):
    def __init__(self) -> None: ...
    def Solve(self) -> None:
        ...
    def WriteSolverInputFile(self) -> None:
        ...
    def Rename(self, name: str, renameResultFile: bool) -> None:
        ...
    def DeleteResultFile(self) -> None:
        ...
    VATVSelectionComponent: CAE.AcousticsAndVibrationVatvSelectionComponent


class AcousticsAndVibrationRandomOutputRequestsComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    def SetFirstResponseSelectedEntities(self, entityType: CAE.AcousticsAndVibrationRandomOutputRequestsComponentAccessor.IntermediateEntity, intermediateNodes: int) -> None:
        ...
    def SetSecondResponseSelectedEntities(self, entityType: CAE.AcousticsAndVibrationRandomOutputRequestsComponentAccessor.IntermediateEntity, intermediateNodes: int) -> None:
        ...
    Csd: bool
    NodeSelectionType: CAE.AcousticsAndVibrationRandomOutputRequestsComponentAccessor.NsType
    Psd: bool


    class NsType(enum.Enum):
        AllNodes = 0
        SubsetOfNodes = 1
    

    class IntermediateEntity(enum.Enum):
        Node = 0
    

class AcousticsAndVibrationPotentialFlowSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AcousticsAndVibrationPotentialFlowSolution]:
        ...
    def __init__(self, owner: CAE.AcousticsAndVibrationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.AcousticsAndVibrationPotentialFlowSolution:
        ...
    def Create(self) -> CAE.AcousticsAndVibrationPotentialFlowSolution:
        ...
    def Delete(self, solution: CAE.AcousticsAndVibrationPotentialFlowSolution) -> None:
        ...
    def CloneSolution(self, solution: CAE.AcousticsAndVibrationPotentialFlowSolution) -> CAE.AcousticsAndVibrationPotentialFlowSolution:
        ...
    def CreateBuilder(self, solution: CAE.AcousticsAndVibrationPotentialFlowSolution) -> CAE.AcousticsAndVibrationPotentialFlowSolutionBuilder:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationPotentialFlowSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    Potentials: CAE.AcousticsAndVibrationBcGroupComponentAccessor
    SolutionName: str
    SolverParameters: CAE.AcousticsAndVibrationSolverParametersComponentAccessor
    Velocities: CAE.AcousticsAndVibrationBcGroupComponentAccessor


class AcousticsAndVibrationPotentialFlowSolution(NXObject):
    def __init__(self) -> None: ...
    def Solve(self) -> None:
        ...
    def WriteSolverInputFile(self) -> None:
        ...
    def Rename(self, name: str, renameResultFile: bool) -> None:
        ...
    def DeleteResultFile(self) -> None:
        ...


class AcousticsAndVibrationPcaSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AcousticsAndVibrationPcaSolution]:
        ...
    def __init__(self, owner: CAE.AcousticsAndVibrationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.AcousticsAndVibrationPcaSolution:
        ...
    def Create(self) -> CAE.AcousticsAndVibrationPcaSolution:
        ...
    def Delete(self, solution: CAE.AcousticsAndVibrationPcaSolution) -> None:
        ...
    def CloneSolution(self, solution: CAE.AcousticsAndVibrationPcaSolution) -> CAE.AcousticsAndVibrationPcaSolution:
        ...
    def CreateBuilder(self, solution: CAE.AcousticsAndVibrationPcaSolution) -> CAE.AcousticsAndVibrationPcaSolutionBuilder:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationPcaSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    CrossPowerData: CAE.AcousticsAndVibrationCrossPowerDataComponentAccessor
    SolutionName: str
    SolverParameters: CAE.AcousticsAndVibrationSolverParametersComponentAccessor


class AcousticsAndVibrationPcaSolution(NXObject):
    def __init__(self) -> None: ...
    def Solve(self) -> None:
        ...
    def WriteSolverInputFile(self) -> None:
        ...
    def Rename(self, name: str, renameResultFile: bool) -> None:
        ...
    def DeleteResultFile(self) -> None:
        ...
    CrossPowerDataComponent: CAE.AcousticsAndVibrationCrossPowerDataComponent


class AcousticsAndVibrationMeshSelectionComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    RegionSelector: SelectTaggedObjectList


class AcousticsAndVibrationMappingDataComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    def CreateAutomaticMapping(self) -> None:
        ...
    def CreateMapping(self, excitationNodeValues: int, responseNodeValues: int, inputNodeValues: int, outputNodeValues: int) -> None:
        ...
    def CreateIndirectMapping(self, responseNodeValues: int, vibrationNodeValues: int) -> None:
        ...


class AcousticsAndVibrationManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def Tag(self) -> Tag: ...

    RandomVatvResponseSolutions: CAE.AcousticsAndVibrationRandomVatvResponseSolutionCollection
    LoadIdentificationSolutions: CAE.AcousticsAndVibrationLoadIdentificationSolutionCollection
    PotentialFlowSolutions: CAE.AcousticsAndVibrationPotentialFlowSolutionCollection
    PcaSolutions: CAE.AcousticsAndVibrationPcaSolutionCollection
    AcousticFieldResponseSolutions: CAE.AcousticsAndVibrationAcousticFieldResponseSolutionCollection


class AcousticsAndVibrationLoadIdentificationSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AcousticsAndVibrationLoadIdentificationSolution]:
        ...
    def __init__(self, owner: CAE.AcousticsAndVibrationManager) -> None: ...
    def __init__(self) -> None: ...
    def Create(self) -> CAE.AcousticsAndVibrationLoadIdentificationSolution:
        ...
    def FindObject(self, name: str) -> CAE.AcousticsAndVibrationLoadIdentificationSolution:
        ...
    def Delete(self, solution: CAE.AcousticsAndVibrationLoadIdentificationSolution) -> None:
        ...
    def CloneSolution(self, solution: CAE.AcousticsAndVibrationLoadIdentificationSolution) -> CAE.AcousticsAndVibrationLoadIdentificationSolution:
        ...
    def CreateBuilder(self, solution: CAE.AcousticsAndVibrationLoadIdentificationSolution) -> CAE.AcousticsAndVibrationLoadIdentificationSolutionBuilder:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationLoadIdentificationSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    FrfData: CAE.AcousticsAndVibrationFrfDataComponentAccessor
    MappingData: CAE.AcousticsAndVibrationMappingDataComponentAccessor
    SolutionName: str
    SolutionOptions: CAE.AcousticsAndVibrationSolutionOptionsComponentAccessor
    SolverParameters: CAE.AcousticsAndVibrationSolverParametersComponentAccessor
    VibrationData: CAE.AcousticsAndVibrationVibrationDataComponentAccessor


class AcousticsAndVibrationLoadIdentificationSolution(NXObject):
    def __init__(self) -> None: ...
    def Solve(self) -> None:
        ...
    def WriteSolverInputFile(self) -> None:
        ...
    def Rename(self, name: str, renameResultFile: bool) -> None:
        ...
    def DeleteResultFile(self) -> None:
        ...
    Frfs: CAE.AcousticsAndVibrationFrfDataComponent
    Vibrations: CAE.AcousticsAndVibrationVibrationDataComponent


class AcousticsAndVibrationFrfDataComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    def GetDatabaseOptions(self) -> CAE.DataReaderDatabaseOptions:
        ...
    def GetSubcases(self, subcaseNames: str) -> None:
        ...
    def SetSubcases(self, subcaseNames: str) -> None:
        ...
    FilePath: str
    FrfType: CAE.AcousticsAndVibrationFrfDataComponentAccessor.FrfTypeEnum
    Quantity: CAE.AcousticsAndVibrationFrfDataComponentAccessor.QuantityEnum
    ScalingFactorImaginary: float
    ScalingFactorReal: float
    SvdFilterType: CAE.AcousticsAndVibrationFrfDataComponentAccessor.SvdFilterTypeEnum
    SvdNumSingularValues: int
    SvdRelativeTolerance: float


    class SvdFilterTypeEnum(enum.Enum):
        RelativeThreshold = 0
        NumberOfSingularValues = 1
    

    class QuantityEnum(enum.Enum):
        Displacement = 0
        Velocity = 1
        Acceleration = 2
    

    class FrfTypeEnum(enum.Enum):
        DirectStiffness = 0
        InverseStiffness = 1
    

class AcousticsAndVibrationFrfDataComponent(NXObject):
    def __init__(self) -> None: ...
    def CreateSelectionRecipes(self) -> None:
        ...


class AcousticsAndVibrationDatabaseSourceAccessor(NXObject):
    def __init__(self) -> None: ...
    FileName: str


class AcousticsAndVibrationCrossPowerDataComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    def ReadFile(self) -> None:
        ...
    def SetReferenceNodes(self, nodeIds: int) -> None:
        ...
    def SetResponseNodes(self, nodeIds: int) -> None:
        ...
    AutomaticNodeSelection: bool
    DatabaseOptions: CAE.DataReaderDatabaseOptions
    FilePath: str
    SelectedAutoPowerSubcase: str
    SelectedCrossPowerSubcase: str
    SvdFilterType: CAE.AcousticsAndVibrationCrossPowerDataComponentAccessor.SvdFilterTypeEnum
    SvdNumSingularValues: int
    SvdRelativeTolerance: float


    class SvdFilterTypeEnum(enum.Enum):
        RelativeThreshold = 0
        NumberOfSingularValues = 1
    

class AcousticsAndVibrationCrossPowerDataComponent(NXObject):
    def __init__(self) -> None: ...


class AcousticsAndVibrationBcGroupComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    BcCollection: CAE.AcousticsAndVibrationBcCollection


class AcousticsAndVibrationBcComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    MeshSelection: CAE.AcousticsAndVibrationMeshSelectionComponentAccessor
    Name: str
    Value: Expression


class AcousticsAndVibrationBcCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AcousticsAndVibrationBcComponentAccessor]:
        ...
    def __init__(self, owner: CAE.AcousticsAndVibrationBcGroupComponentAccessor) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.AcousticsAndVibrationBcComponentAccessor:
        ...
    def AddNew(self) -> CAE.AcousticsAndVibrationBcComponentAccessor:
        ...
    def Delete(self, bc: CAE.AcousticsAndVibrationBcComponentAccessor) -> None:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationAcousticRadiatingSurfaceGroupComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    Loads: CAE.AcousticsAndVibrationAcousticRadiatingSurfaceCollection


class AcousticsAndVibrationAcousticRadiatingSurfaceComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    DatabaseSource: CAE.AcousticsAndVibrationDatabaseSourceAccessor
    DensityDataSetName: str
    Name: str
    PressureDataSetName: str
    Type: CAE.AcousticsAndVibrationAcousticRadiatingSurfaceComponentAccessor.Loadtype
    VelocityDataSetName: str


    class Loadtype(enum.Enum):
        KirchhoffPotentials = 0
        KirchhoffPressureVelocity = 1
        Fwh = 2
    

class AcousticsAndVibrationAcousticRadiatingSurfaceCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AcousticsAndVibrationAcousticRadiatingSurfaceComponentAccessor]:
        ...
    def __init__(self, owner: CAE.AcousticsAndVibrationAcousticRadiatingSurfaceGroupComponentAccessor) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, loadName: str) -> CAE.AcousticsAndVibrationAcousticRadiatingSurfaceComponentAccessor:
        ...
    def CreateNew(self) -> CAE.AcousticsAndVibrationAcousticRadiatingSurfaceComponentAccessor:
        ...
    def Remove(self, loadAccessor: CAE.AcousticsAndVibrationAcousticRadiatingSurfaceComponentAccessor) -> None:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationAcousticFieldResponseSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.AcousticsAndVibrationAcousticFieldResponseSolution]:
        ...
    def __init__(self, owner: CAE.AcousticsAndVibrationManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.AcousticsAndVibrationAcousticFieldResponseSolution:
        ...
    def Create(self) -> CAE.AcousticsAndVibrationAcousticFieldResponseSolution:
        ...
    def Delete(self, solution: CAE.AcousticsAndVibrationAcousticFieldResponseSolution) -> None:
        ...
    def CloneSolution(self, solution: CAE.AcousticsAndVibrationAcousticFieldResponseSolution) -> CAE.AcousticsAndVibrationAcousticFieldResponseSolution:
        ...
    def CreateBuilder(self, solution: CAE.AcousticsAndVibrationAcousticFieldResponseSolution) -> CAE.AcousticsAndVibrationAcousticFieldResponseSolutionBuilder:
        ...
    def Tag(self) -> Tag: ...



class AcousticsAndVibrationAcousticFieldResponseSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    FrequencyOptions: CAE.ModelAndLoadPreProcessFrequencyOptions
    LoadsGroup: CAE.AcousticsAndVibrationAcousticRadiatingSurfaceGroupComponentAccessor
    OutputRequest: CAE.AcousticsAndVibrationAcousticFieldResponseOutputRequestComponentAccessor
    SolutionName: str
    SolverParameters: CAE.AcousticsAndVibrationSolverParametersComponentAccessor


class AcousticsAndVibrationAcousticFieldResponseSolution(NXObject):
    def __init__(self) -> None: ...
    def Solve(self) -> None:
        ...
    def WriteSolverInputFile(self) -> None:
        ...
    def Rename(self, name: str, renameResultFile: bool) -> None:
        ...
    def DeleteResultFile(self) -> None:
        ...


class AcousticsAndVibrationAcousticFieldResponseOutputRequestComponentAccessor(NXObject):
    def __init__(self) -> None: ...
    EnableFunctionsOutput: bool
    EnableVectorsOutput: bool


class Acoustics(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def ImportSpecificDuctModes(self, ductInletRegion: CAE.CaeRegion, csvFileName: str) -> None:
        ...
    def ComputeLoudness(self, frequencyValues: float, pressureValues: float) -> float:
        ...
    def Tag(self) -> Tag: ...

    PanelGenerator: CAE.AcousticsPanelGenerator


class AcousticPostEnvironment(TaggedObject):
    def __init__(self) -> None: ...
    def GetPostEnvironmentType(self) -> CAE.PostEnvironmentsManager.PostEnvironment:
        ...
    SpectrumScaling: CAE.SignalProcessingPlotData.ScalingType
    Weighting: CAE.SignalProcessingPlotData.AcousticalWeighting


class AcousticMeshAutomationBuilder(Builder):
    def __init__(self) -> None: ...
    def AutomaticElementSize(self) -> None:
        ...
    def SetInfinitePlanes(self, pPlaneTags: typing.List[Plane]) -> None:
        ...
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList
    Shell2SolidElementType: CAE.ElementTypeBuilder
    SurfaceWrapElementType: CAE.ElementTypeBuilder


class AcousticChamberMeshBuilder(Builder):
    def __init__(self) -> None: ...
    def AutomaticElementSize(self) -> None:
        ...
    def AutomaticRemeshElementSize(self) -> None:
        ...
    def AutomaticInferPlane(self) -> None:
        ...
    def AutomaticOffsetDistance(self) -> None:
        ...
    ElementType: CAE.ElementTypeBuilder
    InfinitePlane: Plane
    MeshName: str
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectTaggedObjectList


class AbstractionManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.FEModel) -> None: ...
    def CreateCircularImprintBuilder(self) -> CAE.CircularImprintBuilder:
        ...
    def CreatePolygonFaceOnMeshBuilder(self) -> CAE.PolygonFaceOnMeshBuilder:
        ...
    def CreateSuppressHoleBuilder(self) -> CAE.SuppressHoleBuilder:
        ...
    def CreateDeletePolygonFaceBuilder(self) -> CAE.DeletePolygonFaceBuilder:
        ...
    def CreateFaceFaceImprintBuilder(self) -> CAE.FaceFaceImprintBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use CAE.ImprintBuilder.")"""
        ...
    def CreateFaceFromBoundaryBuilder(self) -> CAE.FaceFromBoundaryBuilder:
        ...
    def CreateMergeFaceBuilder(self) -> CAE.MergeFaceBuilder:
        ...
    def CreateEdgeFaceImprintBuilder(self) -> CAE.EdgeFaceImprintBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use CAE.ImprintBuilder.")"""
        ...
    def CreateImprintBuilder(self) -> CAE.ImprintBuilder:
        ...
    def CreateAutoHealGeometryBuilder(self) -> CAE.AutoHealGeometryBuilder:
        ...
    def EdgeMerge(self, ptVertex: typing.List[CAE.CAEVertex], vertexAngle: float, vertexAngleToggle: bool) -> None:
        ...
    def CreateFaceFaceIntersectionBuilder(self) -> CAE.FaceFaceIntersectionBuilder:
        ...
    def Tag(self) -> Tag: ...



class _SetObject():
    obj: Tag
    sub_type: CAE.CaeSetObjectSubType
    sub_id: int


class _ElemEdgefaceObject():
    obj: Tag
    sub_type: CAE.CaeGroupElementSubType
    sub_id: int


