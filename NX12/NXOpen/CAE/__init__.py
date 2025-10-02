from . import Xyplot
from . import ResponseSimulation
from . import FTK
from . import Optimization
from . import QualityAudit
from . import ModelCheck
from . import AeroStructures
from . import Connections
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
    ForceN = 5
    ForceMn = 6
    ForceBf = 7
    TemperatureC = 8
    TemperatureF = 9
    TemperatureK = 10
    TimeSec = 11
    TimeMin = 12
    TimeHour = 13
    FrequencyHz = 14
    MassKg = 15
    MassG = 16
    MassBm = 17
    MassTon = 18
    MassLbfIn = 19
    VelocityM = 20
    VelocityMm = 21
    VelocityIn = 22
    VelocityFt = 23
    AccelerationM = 24
    AccelerationMm = 25
    AccelerationIn = 26
    AccelerationFt = 27
    AccelerationGs = 28
    AngularDisplacementRadian = 29
    AngularDisplacementDegree = 30
    AngularVelocityRadian = 31
    AngularVelocityDegree = 32
    AngularAccelerationRadian = 33
    AngularAccelerationDegree = 34
    MomentMnMm = 35
    MomentNMm = 36
    MomentNM = 37
    MomentBfIn = 38
    MomentBfFt = 39
    PressureKpa = 40
    PressureMpa = 41
    PressurePa = 42
    PressurePsi = 43
    PressureLbfFt = 44
    PressureBar = 45
    PressureAt = 46
    StressKpa = 47
    StressMpa = 48
    StressPa = 49
    StressPsi = 50
    StrainMm = 51
    StrainIn = 52
    RpmRpm = 53
    OrderOrder = 54
    CyclesDuty = 55
    TorqueMnMm = 56
    TorqueNMm = 57
    TorqueNM = 58
    TorqueBfIn = 59
    TorqueBfFt = 60
    GravitationalAccelerationM = 61
    GravitationalAccelerationMm = 62
    GravitationalAccelerationIn = 63
    GravitationalAccelerationFt = 64
    GravitationalAccelerationGs = 65
    Curv1M = 66
    Curv1Mm = 67
    Curv1In = 68
    Curv1Ft = 69
    ElementForceMnMm = 70
    ElementForceNMm = 71
    ElementForceNM = 72
    ElementForceBfIn = 73
    ElementForceBfFt = 74
    ElementMomentMnMm = 75
    ElementMomentNMm = 76
    ElementMomentNM = 77
    ElementMomentBfIn = 78
    ElementMomentBfFt = 79
    VoltageV = 80
    VoltageMv = 81
    ElectricCurrentA = 82
    ElectricCurrentMa = 83
    LoadfactorNone = 84
    MotorSignalNone = 85
    UnitlessScalarNone = 86
    UnitlessRealNone = 87
    UnitlessIntegerNone = 88
    MassSlug = 89
    StressLbfFt = 90
    ForcePoundal = 91
    DampingMnMm = 92
    DampingNMm = 93
    DampingNM = 94
    DampingBfIn = 95
    PowerLbmft2sp3 = 96
    PowerLbfinps = 97
    PowerMuw = 98
    PowerW = 99
    PowerKw = 100
    PowerMw = 101
    PowerBtuph = 102
    PowerBtupm = 103
    PowerBtups = 104
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
    AreaM2 = 122
    AreaMm2 = 123
    AreaIn2 = 124
    AreaFt2 = 125
    DisplacementCm = 126
    ForceCn = 127
    ForceKgf = 128
    MassKgfM = 129
    MassKgfMm = 130
    MassKgfCm = 131
    VelocityCm = 132
    AccelerationCm = 133
    MomentCnCm = 134
    MomentKgfM = 135
    MomentKgfMm = 136
    MomentKgfCm = 137
    PressureCnCm2 = 138
    PressureKgfCm2 = 139
    PressureKgfM2 = 140
    PressureKgfMm2 = 141
    StressCnCm2 = 142
    StressKgfM2 = 143
    StressKgfMm2 = 144
    StressKgfCm2 = 145
    StrainM = 146
    StrainCm = 147
    TorqueCnCm = 148
    TorqueKgfM = 149
    TorqueKgfMm = 150
    TorqueKgfCm = 151
    ElementForceCnCm = 152
    ElementForceKgfM = 153
    ElementForceKgfMm = 154
    ElementForceKgfCm = 155
    ElementMomentCnCm = 156
    ElementMomentKgfM = 157
    ElementMomentKgfMm = 158
    ElementMomentKgfCm = 159
    AreaCm2 = 160
    GravitationalAccelerationCm = 161
    DampingCnCm = 162
    DampingKgfM = 163
    DampingKgfMm = 164
    DampingKgfCm = 165
    Curv1Cm = 166
    AngularDisplacementRev = 167
    AngularVelocityRevSec = 168
    AngularVelocityRevMin = 169
    AngularAccelerationRevSec2 = 170
    AngularAccelerationRevMin2 = 171
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
    DisplacementKm = 250
    DisplacementMi = 251
    DisplacementMicron = 252
    DisplacementNm = 253
    DisplacementAngstrom = 254
    VelocityKmHr = 255
    VelocityMiHr = 256
    VelocityFtMin = 257
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
    TemperatureR = 283
    FrequencyKhz = 284
    FrequencyMhz = 285
    FrequencyGhz = 286
    MassMg = 287
    AngularDisplacementPiRad = 288
    PressureNCm2 = 289
    PressureMmH2o = 290
    PressureMmHg = 291
    PressureInH2o = 292
    PressureInHg = 293
    StressNCm2 = 294
    ElementForceJM2 = 295
    VoltageMicrov = 296
    VoltageLbfInAS = 297
    ElectricCurrentMicroa = 298
    DampingLbmSec = 299
    DampingKgSec = 300
    EnergyMj = 301
    ConvectionCoefficientWM2Degk = 302
    Number = 303


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
    Number = 46


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


class WeldRow(CAE.MeshControl):
    def __init__(self) -> None: ...


class WeldBuilder(Builder):
    def __init__(self) -> None: ...
    DistanceBetween: Expression
    EdgeSelection: SelectTaggedObjectList
    ElementType: CAE.ElementTypeBuilder
    EndOffset: Expression
    FlipState: int
    InputFile: str
    Location: CAE.WeldBuilder.WeldLocation
    NodeSelection: CAE.SelectFENodeList
    NumberOfPointsOnEdge: int
    NumberOfPointsOption: CAE.WeldBuilder.NumberOfPointsOnEdgeType
    OffsetDistance: Expression
    OffsetVector: Direction
    Pattern: str
    PointOnEdgeOption: CAE.WeldBuilder.PointOnEdgeType
    PointsSelection: SelectTaggedObjectList
    SearchDistance: Expression
    SpecifiedNumberOfPoints: int
    StartOffset: Expression
    SupportAllPids: bool


    class WeldLocation(enum.Enum):
        Point = 0
        File = 1
        Edge = 2
        Node = 3
    

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


class ViewLayoutManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def SetArrangement(self, arrangementType: CAE.ViewLayoutManager.ArrangementType) -> None:
        ...
    def GetViewXY(self, viewXY: typing.List[CAE.ViewLayoutManager.ViewXY]) -> None:
        ...
    def SetViewXY(self, viewIndex: int, viewXY: CAE.ViewLayoutManager.ViewXY) -> None:
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
    

class SphereBoundingVolume(CAE.BoundingVolumePrimitive):
    def __init__(self) -> None: ...
    def GetCenterDiameter(self, centerPoint: Point, diameter: Expression) -> None:
        ...
    def SetCenterDiameter(self, centerPoint: Point, diameter: Expression) -> None:
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
    def CreateAdjacentFaceMethod(self, seed: CAE.CAEFace) -> CAE.AdjacentFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateAdjacentFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateAdjacentFaceMethod(self, seeds: typing.List[CAE.CAEFace]) -> CAE.AdjacentFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateAdjacentFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateAdjacentFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.AdjacentFaceMethod:
        ...
    def CreateAdjacentFaceMethod(self, seed: CAE.CAEEdge) -> CAE.AdjacentFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateAdjacentFaceMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateAdjacentFaceMethod(self, seeds: typing.List[CAE.CAEEdge]) -> CAE.AdjacentFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateAdjacentFaceMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateAdjacentFaceMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.AdjacentFaceMethod:
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCircularEdgeMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        ...
    def CreateCircularEdgeMethod(self, seed: CAE.CAEFace, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCircularEdgeMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEFace], dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCircularEdgeMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        ...
    def CreateCircularEdgeMethod(self, seed: CAE.CAEBody, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCircularEdgeMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEBody], dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCircularEdgeMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCircularEdgeMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, dMinRadius: float, dMaxRadius: float, onlyHoleEdges: bool) -> CAE.CircularEdgeMethod:
        ...
    def CreateCylinderFaceMethod(self, seed: CAE.CAEBody, dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCylinderFaceMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCylinderFaceMethod(self, seeds: typing.List[CAE.CAEBody], dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCylinderFaceMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCylinderFaceMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        ...
    def CreateCylinderFaceMethod(self, seeds: typing.List[CAE.CAEFace], dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateCylinderFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateCylinderFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dMinCylinderRadius: float, dMaxCylinderRadius: float, dMinCylinderAngle: float, dMaxCylinderAngle: float) -> CAE.CylinderFaceMethod:
        ...
    def CreateEdgePathMethod(self, seedEdgeTag: CAE.CAEEdge, seedStartVertexTag: CAE.CAEVertex) -> CAE.EdgePathMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateEdgePathMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateEdgePathMethod(self, seedEdgeTag: CAE.CAEEdge, seedStartVertexTag: CAE.CAEVertex, preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float) -> CAE.EdgePathMethod:
        ...
    def CreateElemEdgePathMethod(self, seedElemEdgeTag: CAE.FEElemEdge, seedStartNodeTag: CAE.FENode) -> CAE.ElemEdgePathMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateElemEdgePathMethod which takes as input an array of NXOpen.CAE.FEElemEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateElemEdgePathMethod(self, seedElemEdgeTag: CAE.FEElemEdge, seedStartNodeTag: CAE.FENode, preferFreeEdges: bool, preferGeometryAssociatedEdges: bool, preferFeatureElementEdge: bool, featureAngleTolerance: float, allowGapJumping: bool, gapJumpingTolerance: float) -> CAE.ElemEdgePathMethod:
        ...
    def CreateFeatureEdgeNodeMethod(self, seedElemTag: CAE.FEElement, seedElemEdgeId: int, dFeatureAngle: float) -> CAE.FeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureEdgeNodeMethod which takes an array of NXOpen.CAE.FEElement and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureEdgeNodeMethod(self, seedTags: typing.List[CAE.FEElement], seedElemEdgeIds: int, dFeatureAngle: float) -> CAE.FeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureEdgeNodeMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureEdgeNodeMethod(self, seedTags: typing.List[CAE.FEElemEdge], dFeatureAngle: float) -> CAE.FeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureEdgeNodeMethod which takes as input an array of NXOpen.CAE.FEElemEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureEdgeNodeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, dFeatureAngle: float) -> CAE.FeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureEdgeNodeMethod which takes as input an array of NXOpen.CAE.FEElemEdge or NXOpen.CAE.Mesh objects and the argument edgeType.")"""
        ...
    def CreateFeatureEdgeNodeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureEdgeNodeMethod:
        ...
    def CreateFeatureElemEdgeMethod(self, seedElemTag: CAE.FEElement, seedElemEdgeId: int, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemEdgeMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemEdgeMethod(self, seedTags: typing.List[CAE.FEElement], seedElemEdgeIds: int, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemEdgeMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemEdgeMethod(self, seedTags: typing.List[CAE.FEElemEdge], dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemEdgeMethod which takes as input an array of NXOpen.CAE.FEElemEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemEdgeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemEdgeMethod which takes as input an array of NXOpen.CAE.FEElemEdge or NXOpen.CAE.Mesh objects and the argument edgeType.")"""
        ...
    def CreateFeatureElemEdgeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        ...
    def CreateFeatureElemEdgeMethod(self, seedTags: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, edgeType: CAE.Type, dFeatureAngle: float) -> CAE.FeatureElemEdgeMethod:
        ...
    def CreateFeatureElemFaceMethod(self, seedElemTag: CAE.FEElement, seedElemFaceId: int, dFeatureAngle: float) -> CAE.FeatureElemFaceMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemFaceMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemFaceMethod(self, seedTags: typing.List[CAE.FEElement], seedElemFaceIds: int, dFeatureAngle: float) -> CAE.FeatureElemFaceMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemFaceMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemFaceMethod(self, seedTags: typing.List[CAE.FEElemFace], dFeatureAngle: float) -> CAE.FeatureElemFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemFaceMethod which takes as input an array of NXOpen.CAE.FEElemFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemFaceMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, dFeatureAngle: float) -> CAE.FeatureElemFaceMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemFaceMethod which takes as input argument stopAtNonManifoldJunctions.")"""
        ...
    def CreateFeatureElemFaceMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureElemFaceMethod:
        ...
    def CreateFeatureElemMethod(self, seedElemTag: CAE.FEElement, seedElemFaceId: int, dFeatureAngle: float) -> CAE.FeatureElemMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemMethod(self, seedTags: typing.List[CAE.FEElement], seedElemFaceIds: int, dFeatureAngle: float) -> CAE.FeatureElemMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemMethod(self, seedTags: typing.List[CAE.FEElemFace], dFeatureAngle: float) -> CAE.FeatureElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemMethod which takes as input an array of NXOpen.CAE.FEElemFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureElemMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, dFeatureAngle: float) -> CAE.FeatureElemMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureElemMethod which takes as input argument stopAtNonManifoldJunctions.")"""
        ...
    def CreateFeatureElemMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureElemMethod:
        ...
    def CreateFeatureShellElemMethod(self, seedElemTag: CAE.FEElement, dFeatureAngle: float) -> CAE.FeatureShellElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureShellElemMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureShellElemMethod(self, seedTags: typing.List[CAE.FEElement], dFeatureAngle: float) -> CAE.FeatureShellElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureShellElemMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureShellElemMethod(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, dFeatureAngle: float) -> CAE.FeatureShellElemMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureShellElemMethod which takes as input argument stopAtNonManifoldJunctions.")"""
        ...
    def CreateFeatureShellElemMethod(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureShellElemMethod:
        ...
    def CreateFeatureNodeMethod(self, seedElemTag: CAE.FEElement, seedElemFaceId: int, dFeatureAngle: float) -> CAE.FeatureNodeMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureNodeMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureNodeMethod(self, seedTags: typing.List[CAE.FEElement], seedElemFaceIds: int, dFeatureAngle: float) -> CAE.FeatureNodeMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureNodeMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureNodeMethod(self, seedTags: typing.List[CAE.FEElemFace], dFeatureAngle: float) -> CAE.FeatureNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureNodeMethod which takes as input an array of NXOpen.CAE.FEElemFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFeatureNodeMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, dFeatureAngle: float) -> CAE.FeatureNodeMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFeatureNodeMethod which takes as input argument stopAtNonManifoldJunctions.")"""
        ...
    def CreateFeatureNodeMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool, computeFreeFacesOnVisibleModel: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.FeatureNodeMethod:
        ...
    def CreateFilletFaceMethod(self, seed: CAE.CAEBody, radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFilletFaceMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFilletFaceMethod(self, seeds: typing.List[CAE.CAEBody], radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFilletFaceMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFilletFaceMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        ...
    def CreateFilletFaceMethod(self, seeds: typing.List[CAE.CAEFace], radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateFilletFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateFilletFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, radiusType: CAE.RadiusType, dMinFilletRadius: float, dMaxFilletRadius: float, dMinFilletAngle: float, dMaxFilletAngle: float) -> CAE.FilletFaceMethod:
        ...
    def CreateGroupMethod(self, seed: CAE.CaeGroup) -> CAE.GroupMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateGroupMethod which takes as input doEntityVisibilityCheck.")"""
        ...
    def CreateGroupMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupMethod:
        ...
    def CreateGroupElemMethod(self, seed: CAE.CaeGroup, elemOption: CAE.GroupElemMethodElemOption.ElemOption) -> CAE.GroupElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateGroupElemMethod which takes as input doEntityVisibilityCheck.")"""
        ...
    def CreateGroupElemMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool, elemOption: CAE.GroupElemMethodElemOption.ElemOption) -> CAE.GroupElemMethod:
        ...
    def CreateGroupElemEdgeMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupElemEdgeMethod:
        ...
    def CreateGroupElemFaceMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupElemFaceMethod:
        ...
    def CreateGroupEdgeMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupEdgeMethod:
        ...
    def CreateGroupFaceMethod(self, seed: CAE.CaeGroup) -> CAE.GroupFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateGroupFaceMethod which takes as input doEntityVisibilityCheck.")"""
        ...
    def CreateGroupFaceMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupFaceMethod:
        ...
    def CreateGroupNodeMethod(self, seed: CAE.CaeGroup) -> CAE.GroupNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateGroupNodeMethod which takes as input doEntityVisibilityCheck.")"""
        ...
    def CreateGroupNodeMethod(self, seed: CAE.CaeGroup, doEntityVisibilityCheck: bool) -> CAE.GroupNodeMethod:
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
    def CreateOrderedFeatureEdgeNodeMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, flipSeedStart: bool, dFeatureAngle: float) -> CAE.OrderedFeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateOrderedFeatureEdgeNodeMethod which takes as input argument stopAtNonManifoldJunctions.")"""
        ...
    def CreateOrderedFeatureEdgeNodeMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, flipSeedStart: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.OrderedFeatureEdgeNodeMethod:
        ...
    def CreateOrderedFeatureEdgeElemMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, flipSeedStart: bool, dFeatureAngle: float) -> CAE.OrderedFeatureEdgeNodeMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateOrderedFeatureEdgeElemMethod which takes as input argument stopAtNonManifoldJunctions.")"""
        ...
    def CreateOrderedFeatureEdgeElemMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, computeFreeEdgesOnVisibleModel: bool, flipSeedStart: bool, stopAtNonManifoldJunctions: bool, dFeatureAngle: float) -> CAE.OrderedFeatureEdgeNodeMethod:
        ...
    def CreateRelatedCurveMethod(self, seeds: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedCurveMethod:
        ...
    def CreateRelatedCurveMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedCurveMethod:
        ...
    def CreateRelatedCurveMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedCurveMethod:
        ...
    def CreateRelatedEdgeMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedEdgeMethod:
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
    def CreateRelatedElemEdgeMethod(self, seed: CAE.Mesh) -> CAE.RelatedElemEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemEdgeMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemEdgeMethod(self, seeds: typing.List[CAE.Mesh]) -> CAE.RelatedElemEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemEdgeMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemEdgeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seed: CAE.CAEEdge) -> CAE.RelatedElemEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemEdgeMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemEdgeMethod(self, seeds: typing.List[CAE.CAEEdge]) -> CAE.RelatedElemEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemEdgeMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemEdgeMethod(self, seed: CAE.CAEEdge, doEntityVisibilityCheck: bool) -> CAE.RelatedElemEdgeMethod:
        ...
    def CreateRelatedElemFaceMethod(self, seed: CAE.Mesh) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.Mesh]) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemFaceMethod(self, seed: CAE.CAEFace) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.CAEFace]) -> CAE.RelatedElemFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemFaceMethod(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemFaceMethod(self, seed: CAE.CAEFace, doEntityVisibilityCheck: bool) -> CAE.RelatedElemFaceMethod:
        ...
    def CreateRelatedElemMethod(self, seed: CAE.Mesh) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.Mesh]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seed: CAE.CAEBody) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEBody]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seed: CAE.CAEFace) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEFace]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seed: CAE.CAEEdge) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEEdge]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seed: CAE.FENode) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.FENode objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.FENode]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.CAE.FENode objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Line]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.Line objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Line], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Arc]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.Arc objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Arc], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Conic]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.Conic objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Conic], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Spline]) -> CAE.RelatedElemMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedElemMethod which takes as input an array of NXOpen.Spline objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedElemMethod(self, seedTags: typing.List[Spline], doEntityVisibilityCheck: bool) -> CAE.RelatedElemMethod:
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
    def CreateRelatedFaceMethod(self, seed: CAE.Mesh) -> CAE.RelatedFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedFaceMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.Mesh]) -> CAE.RelatedFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedFaceMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seed: CAE.FENode) -> CAE.RelatedFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedFaceMethod which takes as input an array of NXOpen.CAE.FENode objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.FENode]) -> CAE.RelatedFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedFaceMethod which takes as input an array of NXOpen.CAE.FENode objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.FENode], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedFaceMethod(self, seedElemTag: CAE.FEElement, seedElemFaceId: int) -> CAE.RelatedFaceMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedFaceMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedFaceMethod(self, seedTags: typing.List[CAE.FEElement], seedElemFaceIds: int) -> CAE.RelatedFaceMethod:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedFaceMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedFaceMethod(self, seedTags: typing.List[CAE.FEElemFace]) -> CAE.RelatedFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedFaceMethod which takes as input an array of NXOpen.CAE.FEElemFace objects and the argument doEntityVisibilityCheck.")"""
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
    def CreateRelatedFaceMethod(self, seeds: typing.List[CAE.MeshControl], doEntityVisibilityCheck: bool) -> CAE.RelatedFaceMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.Mesh) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.Mesh]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.Mesh objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEBody) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEBody]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEFace) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEFace]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEEdge) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEEdge]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.FEElement) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.FEElement]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.FEElement objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.FEElement], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.MeshPoint]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.CAE.MeshPoint objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.MeshPoint], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Point]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.Point objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Point], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Line]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.Line objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Line], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Arc]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.Arc objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Arc], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Conic]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.Conic objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Conic], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Spline]) -> CAE.RelatedNodeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateRelatedNodeMethod which takes as input an array of NXOpen.Spline objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[Spline], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.FEElemEdge], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTags: typing.List[CAE.FEElemFace], doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.Mesh, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEBody, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEFace, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.CAEEdge, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.FEElement, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: CAE.MeshPoint, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: Point, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: Line, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: Arc, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: Conic, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seed: Spline, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
        ...
    def CreateRelatedNodeMethod(self, seedTag: CAE.FEElemFace, doEntityVisibilityCheck: bool) -> CAE.RelatedNodeMethod:
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
    def CreateSliverFaceMethod(self, seed: CAE.CAEBody, dSliverTolerance: float) -> CAE.SliverFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateSliverFaceMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateSliverFaceMethod(self, seeds: typing.List[CAE.CAEBody], dSliverTolerance: float) -> CAE.SliverFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateSliverFaceMethod which takes as input an array of NXOpen.CAE.CAEBody objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateSliverFaceMethod(self, seeds: typing.List[CAE.CAEBody], doEntityVisibilityCheck: bool, dSliverTolerance: float) -> CAE.SliverFaceMethod:
        ...
    def CreateSliverFaceMethod(self, seeds: typing.List[CAE.CAEFace], dSliverTolerance: float) -> CAE.SliverFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateSliverFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateSliverFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dSliverTolerance: float) -> CAE.SliverFaceMethod:
        ...
    def CreateTangentFaceMethod(self, seed: CAE.CAEFace, dTangentTolerance: float) -> CAE.TangentFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateTangentFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateTangentFaceMethod(self, seeds: typing.List[CAE.CAEFace], dTangentTolerance: float) -> CAE.TangentFaceMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateTangentFaceMethod which takes as input an array of NXOpen.CAE.CAEFace objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateTangentFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, dTangentTolerance: float) -> CAE.TangentFaceMethod:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateTangentFaceMethod which takes as input argument stopAtNonManifoldJunctions.")"""
        ...
    def CreateTangentFaceMethod(self, seeds: typing.List[CAE.CAEFace], doEntityVisibilityCheck: bool, stopAtNonManifoldJunctions: bool, dTangentTolerance: float) -> CAE.TangentFaceMethod:
        ...
    def CreateTangentContinuousEdgeMethod(self, seed: CAE.CAEEdge, dFeatureAngle: float) -> CAE.TangentContinuousEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateTangentContinuousEdgeMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateTangentContinuousEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], dFeatureAngle: float) -> CAE.TangentContinuousEdgeMethod:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded NXOpen.CAE.SmartSelectionManager.CreateTangentContinuousEdgeMethod which takes as input an array of NXOpen.CAE.CAEEdge objects and the argument doEntityVisibilityCheck.")"""
        ...
    def CreateTangentContinuousEdgeMethod(self, seeds: typing.List[CAE.CAEEdge], doEntityVisibilityCheck: bool, dFeatureAngle: float) -> CAE.TangentContinuousEdgeMethod:
        ...
    def CreateHoleElementEdgeMethod(self, seeds: typing.List[CAE.Mesh], doEntityVisibilityCheck: bool, dMinElementEdgeHoleRadius: float, dMaxElementEdgeHoleRadius: float, allowNonCircularHoles: bool) -> CAE.HoleElementEdgeMethod:
        ...
    def CreateHoleElementEdgeMethod(self, seedElemEdgeTag: CAE.FEElemEdge, doEntityVisibilityCheck: bool, dMinElementEdgeHoleRadius: float, dMaxElementEdgeHoleRadius: float, allowNonCircularHoles: bool) -> CAE.HoleElementEdgeMethod:
        ...
    def CreateElemLabelMethod(self, doEntityVisibilityCheck: bool, startLabel: int, endLabel: int, labelIncrement: int) -> CAE.ElemLabelMethod:
        ...
    def CreateNodeLabelMethod(self, doEntityVisibilityCheck: bool, startLabel: int, endLabel: int, labelIncrement: int) -> CAE.NodeLabelMethod:
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
        ...
    Label: int


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
    def ResolveConstraintConflicts(self) -> None:
        ...
    def Solve(self, solveOption: CAE.SimSolution.SolveOption, setupCheckOption: CAE.SimSolution.SetupCheckOption) -> None:
        ...
    def CreateAlignmentBuilder(self) -> CAE.CorrelAlignmentBuilder:
        ...
    def GetConflictingConstraintPairByIndex(self, index: int, tConstraint1: CAE.SimConstraint, tConstraint2: CAE.SimConstraint, ignored: bool) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimSolution.GetConflictingBcPairByIndex instead.")"""
        ...
    def GetConflictingBcPairByIndex(self, index: int, tBc1: CAE.SimBC, tBc2: CAE.SimBC, ignored: bool) -> None:
        ...
    def CreateConstraintResolutionBuilder(self, tStep: CAE.SimGroupContainer, tConstraint1: CAE.SimConstraint, tConstraint2: CAE.SimConstraint) -> CAE.ConstraintResolutionBuilder:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimSolution.CreateConflictResolutionBuilder instead.")"""
        ...
    def CreateConflictResolutionBuilder(self, tStep: CAE.SimGroupContainer, tBc1: CAE.SimBC, tBc2: CAE.SimBC) -> CAE.ConflictResolutionBuilder:
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
    def GetResultReferenceByIndex(self, resultIndex: int) -> CAE.SimResultReference:
        ...
    def SetLocalResultFile(self, dirpath: str, filename: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:SetLocalResultFile instead.")"""
        ...
    def SetManagedResultFile(self, file: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:SetManagedResultFile instead.")"""
        ...
    def SetInferredResultFile(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:SetInferredResultFile instead.")"""
        ...
    def GetResultFile(self, resultfiledir: str, resfilename: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:GetResultFile instead.")"""
        ...
    def GetManagedResultFile(self) -> str:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:GetManagedResultFile instead.")"""
        ...
    def GetResultFileUnits(self, units: typing.List[Unit]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:GetResultFileUnits instead.")"""
        ...
    def SetResultFileUnits(self, units: typing.List[Unit]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:SetResultFileUnits instead.")"""
        ...
    def SetInferredResultFileUnits(self) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.SimResultReference:SetInferredResultFileUnits instead.")"""
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
    def CreateReport(self, templateFile: str, reportName: str, listError: bool) -> Report.Report:
        ...
    def GetReports(self, pReports: typing.List[Report.Report]) -> None:
        ...
    AbstractionType: CAE.SimSimulation.AxisymAbstractionType
    ActiveStep: CAE.SimSolutionStep
    AllowedStepTypeCount: int
    AnalysisType: str
    AttachedLoadRecipe: CAE.SimLoadRecipe
    ConflictingBcCount: int
    ConflictingConstraintsCount: int
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
    def AddBc(self, bc: CAE.SimBC, solution: CAE.SimSolution, solutionStep: CAE.SimSolutionStep) -> None:
        ...
    def CreateAutoPairsBuilder(self, pcBCDescName: str) -> CAE.AutoPairsBuilder:
        ...
    def CreateAutoCyclicSymmetryPairsBuilder(self, pcBCDescName: str) -> CAE.AutoCyclicSymmetryPairsBuilder:
        ...
    def CreateAutoBcBuilder(self, pcBCDescName: str, pcRecipeName: str) -> CAE.AutoBCBuilder:
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
    def CreateConstraintSetBuilder(self, pcConstraintSetDescName: str, tConstraintSet: CAE.SimConstraintSet) -> CAE.SimConstraintSetBuilder:
        ...
    def SmoothOptResultsCreateBuilder(self) -> CAE.SmoothOptResultsBuilder:
        ...
    def CreateBcLabelManagerBuilder(self) -> CAE.BcLabelManagerBuilder:
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
    def SetLocalResultFile(self, dirpath: str, filename: str) -> None:
        ...
    def SetManagedResultFile(self, file: str) -> None:
        ...
    def SetInferredResultFile(self) -> None:
        ...
    def GetResultFile(self, resultfiledir: str, resfilename: str) -> None:
        ...
    def GetManagedResultFile(self) -> str:
        ...
    def GetResultFileUnits(self, units: typing.List[Unit]) -> None:
        ...
    def SetResultFileUnits(self, units: typing.List[Unit]) -> None:
        ...
    def SetInferredResultFileUnits(self) -> None:
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
    def RelabelByOffsets(self, csysOffset: int, physOffset: int, groupOffset: int) -> None:
        ...
    def CompressLabels(self, compressCsysLabels: bool, compressPhysLabels: bool, compressGroupLabels: bool) -> None:
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
    

class SimLoadRecipeTypes(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


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


    class LbcHierarchyTypes(enum.Enum):
        Aggregated = 0
        Separated = 1
    

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
    def Create(self, name: str, description: str, dataType: CAE.SimLoadRecipeTypes.DataTypes) -> CAE.SimLoadRecipe:
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
    def DisableLoadCondition(self, loadCondition: str) -> None:
        ...
    def EnableLoadCondition(self, loadCondition: str) -> None:
        ...
    def DisableTrackingValue(self, trackingValue: str) -> None:
        ...
    def EnableTrackingValue(self, trackingValue: str) -> None:
        ...
    def NewLbcGeneratorFromLoadRecipe(self) -> CAE.SimLoadRecipeLbcGenerator:
        ...
    def ImportFromCSVFile(self, filePath: str, csvDelim: str, noParsedContent: bool, invalidLoadType: bool, invalidEntityType: bool, invalidNbrOfParameters: bool) -> None:
        ...
    def ExportToCSVFile(self, filePath: str) -> bool:
        ...
    def Autofill(self) -> None:
        ...
    def Autofill(self, feModelOcc: CAE.FEModelOccurrence) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.SimLoadRecipe.Autofill instead.")"""
        ...
    def Validation(self) -> None:
        ...
    def LoadLoadConditions(self) -> None:
        ...
    def LoadTrackingValues(self) -> None:
        ...
    def SetAutofillAssemblyComponent(self, feModelOcc: CAE.FEModelOccurrence) -> None:
        ...
    MappingCollection: CAE.SimLoadRecipeMappingCollection
    SourceCollection: CAE.SimLoadRecipeSourceCollection
    DataType: CAE.SimLoadRecipeTypes.DataTypes
    Description: str
    Name: str


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
    ConditionTimeStepCollection: CAE.SimConditionTimeStepCollection


    class OutOfRangeBehavior(enum.Enum):
        Clip = 0
        Extrapolate = 1
    

class SimConditionSeqMgr(TaggedObject):
    def __init__(self) -> None: ...
    def IsReferenced(self, condition: CAE.SimCondition) -> bool:
        ...
    def ImportFile(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat) -> None:
        ...
    def ExportFile(self, filename: str, format: CAE.SimConditionSeqMgr.FileFormat) -> None:
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
    def SetEvaluationPoints(self, values: float, units: typing.List[Unit]) -> None:
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
    DisplayMagnitudeProperty: str
    DisplayMode: CAE.SimBCDisplay.Mode
    DistValueDisplayFlag: bool
    DofDisplayFlag: bool
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
    TextSymbolDisplayFlag: bool
    Translucency: int
    ValueDisplayFlag: bool


    class Mode(enum.Enum):
        Collapse = 0
        Expand = 1
        Offset = 2
    

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
    def GetSolverCardSyntax(self) -> str:
        ...
    BcLabel: int
    DescriptorName: str
    PropertyTable: CAE.PropertyTable
    TargetSetManager: CAE.SetManager


class SimAutoBcRecipe(CAE.SimRecipe):
    def __init__(self) -> None: ...
    def GetBcList(self, bcList: typing.List[CAE.SimBC]) -> None:
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


class ShipMeshAutomationBuilder(Builder):
    def __init__(self) -> None: ...
    DefaultElementSize: bool
    ElementSize: Expression
    MethodType: CAE.ShipMeshAutomationBuilder.MeshingMethodType


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
    MeshSizeVariation: float
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
    def SetTargetSetEdgePath(self, setIndex: int, seedEdges: typing.List[CAE.CAEEdge], seedVertices: typing.List[CAE.CAEVertex]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded CAE.SetManager.SetTargetSetEdgePath with additional arguments instead.")"""
        ...
    def SetTargetSetEdgePath(self, setIndex: int, seedEdges: typing.List[CAE.CAEEdge], seedVertices: typing.List[CAE.CAEVertex], preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float) -> None:
        ...
    def SetTargetSetPlane(self, setIndex: int, planePosition: Point3d, planeNormal: Vector3d) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded CAE.SetManager.SetTargetSetPlaneWithOffset.")"""
        ...
    def GetTargetSetPlane(self, setIndex: int, planePosition: Point3d, planeNormal: Vector3d) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use overloaded CAE.SetManager.GetTargetSetPlaneWithOffset.")"""
        ...
    def SetTargetSetPlaneWithOffset(self, setIndex: int, planePosition: Point3d, planeNormal: Vector3d, offsetValue: Expression) -> None:
        ...
    def GetTargetSetPlaneWithOffset(self, setIndex: int, planePosition: Point3d, planeNormal: Vector3d, offsetValue: Expression) -> None:
        ...
    def SetTargetSetPointLocation(self, setIndex: int, position: Point3d) -> None:
        ...
    def GetTargetSetPointLocation(self, setIndex: int) -> Point3d:
        ...
    def SetTargetSetDistributedPlanes(self, setIndex: int, centerMethod: CAE.SetManager.DistributedPlanesPosition, centerPoint: Point, radiusMethod: CAE.SetManager.DistributedPlanesPosition, radiusFactor: Expression, radiusValue: Expression, bboxOption: CAE.SetManager.DistributedPlanesBboxType, bboxElems: typing.List[CAE.FEElement], spaceDefinition: CAE.SetManager.DistributedPlanesBoundingSphereType, sphereDirection: CAE.SetManager.DistributedPlanesBoundingSphereDirection, sphereDirectionVector: Direction, sphereDirectionPoint1: Point, sphereDirectionPoint2: Point, sphereDirectionPoint3: Point, flipNormal: bool, refinementLevel: int) -> None:
        ...
    def GetTargetSetDistributedPlanes(self, setIndex: int, centerMethod: CAE.SetManager.DistributedPlanesPosition, centerPoint: Point, radiusMethod: CAE.SetManager.DistributedPlanesPosition, radiusFactor: Expression, radiusValue: Expression, bboxOption: CAE.SetManager.DistributedPlanesBboxType, bboxElems: typing.List[CAE.FEElement], spaceDefinition: CAE.SetManager.DistributedPlanesBoundingSphereType, sphereDirection: CAE.SetManager.DistributedPlanesBoundingSphereDirection, sphereDirectionVector: Direction, sphereDirectionPoint1: Point, sphereDirectionPoint2: Point, sphereDirectionPoint3: Point, flipNormal: bool, refinementLevel: int) -> None:
        ...
    def SetTargetSetElemEdgePath(self, setIndex: int, seedEdges: typing.List[CAE.FEElemEdge], seedVertices: typing.List[CAE.FENode]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded CAE.SetManager.SetTargetSetElemEdgePath with additional arguments instead.")"""
        ...
    def SetTargetSetElemEdgePath(self, setIndex: int, seedEdges: typing.List[CAE.FEElemEdge], seedVertices: typing.List[CAE.FENode], preferFreeEdges: bool, preferGeometryAssociatedEdges: bool, preferFeatureElementEdges: bool, featureAngleTolerance: float, allowGapJumping: bool, gapJumpingTolerance: float) -> None:
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
        ...
    def CreateBoxBoundingVolumeRecipe(self, name: str, centerPoint: Point, targetPoint: Point, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        ...
    def CreateCylinderBoundingVolumeRecipe(self, name: str, centerCsys: CoordinateSystem, diameter: Expression, cylinderHeight: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        ...
    def CreateCylinderBoundingVolumeRecipe(self, name: str, diameter: Expression, baseCenter: Point, topCenter: Point, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        ...
    def CreateSphereBoundingVolumeRecipe(self, name: str, centerPoint: Point, diameter: Expression, entityTypes: typing.List[CAE.CaeSetGroupFilterType]) -> CAE.BoundingVolumeSelectionRecipe:
        ...
    def CreateSingleLabelRecipe(self, name: str, nodeLabel: int) -> CAE.SingleLabelSelectionRecipe:
        ...
    def CreateLabelRangeRecipe(self, name: str, singleLabels: int, startLabels: int, endLabels: int, increments: int, entityType: CAE.CaeSetGroupFilterType) -> CAE.LabelRangeSelectionRecipe:
        ...
    def CreateCoordinateRecipe(self, name: str, coordinates: Point3d, tolerance: float) -> CAE.CoordinateSelectionRecipe:
        ...
    def CreatePointRecipe(self, name: str, point: Point, tolerance: float) -> CAE.PointSelectionRecipe:
        ...
    def CreateAttributeRecipe(self, name: str, entityType: CAE.CaeSetGroupFilterType, resolveRelatedFeEntity: bool, relatedFeEntityType: CAE.CaeSetGroupFilterType) -> CAE.AttributeSelectionRecipe:
        ...
    def FindObject(self, journalIdentifier: str) -> CAE.SelectionRecipe:
        ...
    def Copy(self, recipeToCopy: CAE.SelectionRecipe, name: str) -> CAE.SelectionRecipe:
        ...
    def Delete(self, recipes: typing.List[CAE.SelectionRecipe]) -> None:
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
    Display: CAE.SelectionRecipeDisplay


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
    Addfillets: bool
    BeamSect: CAE.Result.Section
    Comp: CAE.Result.Component
    Complex: CAE.Result.Complex
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
    Quan: CAE.Result.Quantity
    Selectedcsys: CoordinateSystem
    ShellSect: CAE.Result.Section
    Usertypename: str


    class NodalCombination(enum.Enum):
        None = 0
        Nodal = 1
        Elemental = 2
    

class ResultType(CAE.BaseResultType):
    def __init__(self) -> None: ...
    Subtitle: str
    Title: str


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
        ...
    def SetDependentDomain(self, domain: Fields.FieldDomain) -> None:
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
    

class ResultsModelExportBuilder(CAE.ResultsManipulationBuilder):
    def __init__(self) -> None: ...
    def SetResult(self, result: CAE.Result) -> None:
        ...


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
    

class ResultsEnvelopeBuilder(CAE.ResultsManipulationBuilder):
    def __init__(self) -> None: ...
    def SetOutput(self, output: CAE.ResultsEnvelopeBuilder.Output) -> None:
        ...
    def SetResults(self, results: typing.List[CAE.Result], parameters: typing.List[CAE.ResultParameters]) -> None:
        ...
    def SetResults(self, ids: int, results: typing.List[CAE.Result], parameters: typing.List[CAE.ResultParameters]) -> None:
        ...
    def SetOperation(self, operation: CAE.ResultsEnvelopeBuilder.Operation) -> None:
        ...
    def SetIncompatibleResultsOption(self, incompatibleResultsOption: CAE.ResultsEnvelopeBuilder.IncompatibleResults) -> None:
        ...
    def SetNoDataOption(self, noDataOption: CAE.ResultsEnvelopeBuilder.NoData) -> None:
        ...
    def SetFieldName(self, fieldName: str) -> None:
        ...
    def SetIndependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsEnvelopeBuilder.SetIndependentDomain instead.")"""
        ...
    def SetDependentDomainName(self, domainName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ResultsEnvelopeBuilder.SetDependentDomain instead.")"""
        ...
    def SetElementValueAtNode(self, value: CAE.ResultsManipulationBuilder.ElementValueAtNode) -> None:
        ...
    def SetIndependentDomain(self, domain: Fields.FieldDomain) -> None:
        ...
    def SetDependentDomain(self, domain: Fields.FieldDomain) -> None:
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
        ...
    def SetDependentDomain(self, domain: Fields.FieldDomain) -> None:
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
    AcousticModeIndex: int
    CombineAcross: bool
    CombineAcrossIteration: bool
    CombineIterOption: CAE.ResultProbeBuilder.CombineAcrossIterations
    CombinedValue: CAE.ResultProbeBuilder.CombineAcrossEntities
    DesignCycleIndex: int
    EdgeIntegralOption: CAE.ResultProbeBuilder.EdgeIntegral
    EndIterIndex: int
    EndIterValue: float
    ErrorHndl: CAE.ResultProbeBuilder.ErrorHandling
    FaceIntegralOption: CAE.ResultProbeBuilder.FaceIntegral
    Formula: str
    GeometryAverageValue: CAE.ResultProbeBuilder.GeometryValue
    HarmonicIndex: int
    IterNearValue: float
    Iteration: CAE.ResultProbeBuilder.IterationSelection
    IterationIndex: int
    IterationTypeOption: CAE.ResultProbeBuilder.IterationType
    Loadcase: CAE.ResultProbeBuilder.LoadcaseSelection
    LoadcaseIndex: int
    ModelSelectionType: CAE.ResultProbeBuilder.SelectionType
    NodalAveraging: CAE.ResultProbeBuilder.NodalCombination
    PickSequentially: bool
    ProbeName: str
    QueryCurveUsageOptions: CAE.QueryCurveUsageOptions
    ResultReferenceType: CAE.SimResultReference.Type
    ResultType: CAE.Result.Quantity
    RotationSpeedValue: float
    SkipSteps: int
    StartIterIndex: int
    StartIterValue: float
    SuperIterationType: CAE.ResultProbeBuilder.SuperIterType
    Unit: Unit


    class SuperIterType(enum.Enum):
        None = 0
        Harmonic = 1
        RotationSpeed = 2
        DesignCycle = 3
        Acoustic = 4
    

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
    

    class GeometryValue(enum.Enum):
        ArithmeticMean = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
        WeightedAverage = 4
        Integral = 5
        None = 6
    

    class FaceIntegral(enum.Enum):
        Area = 0
        Volume = 1
    

    class ErrorHandling(enum.Enum):
        Fillzero = 0
        Skip = 1
    

    class EdgeIntegral(enum.Enum):
        Length = 0
        Area = 1
    

    class CombineAcrossIterations(enum.Enum):
        ArithmeticMean = 0
        AbsoluteMaximum = 1
        Maximum = 2
        AbsoluteMinimum = 3
        Minimum = 4
        Sum = 5
    

    class CombineAcrossEntities(enum.Enum):
        ArithmeticMean = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
        Difference = 4
        WeightedAverage = 5
        Integral = 6
    

class ResultProbe(Fields.Field):
    def __init__(self) -> None: ...
    def Information(self) -> None:
        ...
    def CopyToSolution(self, targetSolution: CAE.SimSolution) -> CAE.ResultProbe:
        ...
    def GetOutputOptions(self) -> typing.List[CAE.ResultProbe.OutputOption]:
        ...


    class OutputOption(enum.Enum):
        Information = 0
        Graph = 1
        Graph3D = 2
        Field = 3
        UnvFile = 4
        PostView = 5
    

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


class ResultParametersWithNodalForceReport(TaggedObject):
    def __init__(self) -> None: ...
    def GetNodalForceReport(self) -> CAE.NodalForceReport:
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


    class ResultType(enum.Enum):
        Force = 0
        Moment = 1
    

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
        ...
    def SetResultBeamSection(self, section: CAE.Result.Section) -> None:
        ...
    def GetResultShellSection(self) -> CAE.Result.Section:
        ...
    def SetResultShellSection(self, section: CAE.Result.Section) -> None:
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
        ...
    def GetCyclicSymmetricParameters(self) -> CAE.CyclicSymmetricParameters:
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
        ...
    def IsMidnodeValueDisplayed(self) -> bool:
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
        ...
    def SetReferenceNodeLabel(self, referenceNodeLabel: int) -> None:
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


class ResultMeasureResultSectionOptions(CAE.ResultMeasureResultOptions):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetBeamSection(self, eBeamSect: CAE.Result.Section) -> None:
        ...
    def SetShellSection(self, eShellSect: CAE.Result.Section) -> None:
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


class ResultMeasureResultDirectionSectionOptions(CAE.ResultMeasureResultOptions):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetCoordinateSystem(self, eCsys: CAE.Result.CoordinateSystem) -> None:
        ...
    def SetBeamSection(self, eBeamSect: CAE.Result.Section) -> None:
        ...
    def SetShellSection(self, eShellSect: CAE.Result.Section) -> None:
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
        ...
    def SetBeamSection(self, eBeamSect: CAE.Result.Section) -> None:
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
        ...
    def CreateImportedResult(self, filename: str, resultname: str, unitsystem: CAE.Result.ResultBasicUnit) -> CAE.ImportedResult:
        ...
    def CreateImportedResult(self, filename: str, resultname: str) -> CAE.ImportedResult:
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
        ...
    def CreateResultsReductionBuilder(self) -> CAE.ResultsReductionBuilder:
        ...
    def CreateTransientResultsReductionBuilder(self) -> CAE.TransientResultsReductionBuilder:
        ...
    def FindObject(self, journalIdentifier: str) -> TaggedObject:
        ...
    def CreateClippingParameters(self) -> CAE.ClippingParameters:
        ...
    def DeleteClippingParameters(self, result: CAE.ClippingParameters) -> None:
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
        ...
    def CreateTableOfFieldsForModel(self, fieldName: str, indepDomainType: int, depDomainType: int, nodevalshare: int, pvid: int, isdeform: bool, elem: int, node: int, includeOrExculde: bool, primValues: float, lcases: int, iters: int, subiters: int) -> Fields.FieldLinksTable:
        ...
    def GetIterationsWithLimits(self, resid: int, lcase: int, iteration: int, superiter: int, minLimit: int, maxLimit: int, primValues: float, lcases: int, iters: int, subiters: int) -> None:
        ...
    def Create4dResultAccessReferenceFieldWithLimits(self, fieldManager: Fields.FieldManager, result: CAE.Result, parameters: CAE.ResultParameters, indepDomainName: str, depDomainName: str, fieldName: str, minLimit: int, maxLimit: int) -> Fields.FieldReference:
        ...
    def CreateTableFieldFromNodalForceReport(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], nodalForceReport: CAE.NodalForceReport) -> Fields.Field:
        ...
    def CreateResultParametersWithNodalForceReport(self, nodalForceReport: CAE.NodalForceReport) -> CAE.ResultParametersWithNodalForceReport:
        ...
    def DeleteResultParametersWithNodalForceReport(self, result: CAE.ResultParametersWithNodalForceReport) -> None:
        ...
    def CreatePostSelectionEntity(self) -> CAE.PostSelectionEntity:
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
    

    class ElementValueCriterion(enum.Enum):
        Average = 0
        Centroid = 1
        Maximum = 2
        Minimum = 3
    

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


class RecipeSurfaceWrap(CAE.Mesh):
    def __init__(self) -> None: ...


class RecipeOpenDuctMesh(CAE.Mesh):
    def __init__(self) -> None: ...


class RecipeConvexMesh(CAE.Mesh):
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
    Name: str
    NumTriaxialSensors: int
    NumUniaxialSensors: int


    class AlgorithmChoiceType(enum.Enum):
        MinMac = 0
    

class PreTestSensorConfig(NXObject):
    def __init__(self) -> None: ...
    def ExportCsvFile(self, mSol: CAE.PreTestSolution, filename: str) -> None:
        ...
    def ExportShapeMetricsCsvFile(self, metricCode: CAE.CorrelShapemetrictype, filename: str) -> None:
        ...
    def GenerateMatchingDofset(self) -> None:
        ...
    Name: str


class PreTestExportUnvBuilder(Builder):
    def __init__(self) -> None: ...
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
    ConfigName: str
    Name: str


class PreTestDofSetBuilder(Builder):
    def __init__(self) -> None: ...
    DofSetSelect: CAE.CaeDOFSet
    Nodes: CAE.SelectFENodeList
    NodesEnabled: bool


class PreTestDofSet(NXObject):
    def __init__(self) -> None: ...
    def SetDofSet(self, dofsetref: CAE.CaeDOFSet) -> None:
        ...
    def SetDofs(self, nodes: typing.List[CAE.FENode], dofs: bool) -> None:
        ...
    def ExportShapeMetricsCsvFile(self, metricCode: CAE.CorrelShapemetrictype, filename: str) -> None:
        ...


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
    def FreeResource(self) -> None:
        ...
    def Delete(self) -> None:
        ...
    EdgeId: int
    ElemId: int
    FaceId: int
    NodeId: int
    Point: Point3d
    RotationAngle: float
    SEId: int
    SectorId: int


class PostScenarioVisualizationDefinition(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


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


class PostScenarioVariantComponent(enum.Enum):
    Magnitude = 0
    Scalar = 1
    X = 2
    Y = 3
    Z = 4
    Xx = 5
    Yy = 6
    Zz = 7
    Xy = 8
    Xz = 9
    Yx = 10
    Yz = 11
    Zx = 12
    Zy = 13


class PostScenarioVariant(TransientObject):
    def __init__(self, ptr: int) -> None: ...
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
    def SetValueAsVector3d(self, value: Vector3d) -> None:
        ...
    def SetValueAsComponent(self, value: CAE.PostScenarioVariantComponent) -> None:
        ...
    def SetValueAsModeDescription(self, value: CAE.PostScenarioModeDescription) -> None:
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
    def GetValues(self) -> typing.List[CAE.PostScenarioVariant]:
        ...
    DisplayName: str
    Name: str


class PostScenarioSelectionParameters(TaggedObject):
    def __init__(self) -> None: ...
    def NewVariant(self) -> CAE.PostScenarioVariant:
        ...
    def Destroy(self) -> None:
        ...
    def SetIterationVariable(self, variable: CAE.PostScenarioVariable) -> None:
        ...
    Variables: CAE.PostScenarioVariableCollection
    ConfigurationVariables: CAE.PostScenarioConfigurationVariableCollection


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


class PostScenarioManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaePart) -> None: ...
    def NewPostScenarioParameters(self) -> CAE.PostScenarioParameters:
        ...
    def CheckValidDataSource(self, scenarioParameters: CAE.PostScenarioParameters) -> bool:
        ...
    def CheckScenarioDataSourceCompatible(self, scenarioParameters: CAE.PostScenarioParameters) -> bool:
        """[Obsolete("Deprecated in NX12.0.0.  This function is no longer useful because the new API only lists compatible data sources per slot.")"""
        ...
    def CreatePostScenarioBuilderFromParameters(self, scenarioParameters: CAE.PostScenarioParameters) -> CAE.PostScenarioBuilder:
        ...
    def CreatePostScenarioBuilderFromViewport(self, viewportIndex: int) -> CAE.PostScenarioBuilder:
        ...
    def CreatePostScenarioBuilderFromScenario(self, scenario: CAE.PostScenario) -> CAE.PostScenarioBuilder:
        ...
    def CreateViewportSynchronizationOptions(self) -> CAE.ViewportSynchronizationOptions:
        ...
    def SetViewportSynchronizationOptions(self, options: CAE.ViewportSynchronizationOptions) -> None:
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


class PostScenarioDescriptorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.PostScenarioDescriptor]:
        ...
    def __init__(self, owner: CAE.PostScenarioManager) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, name: str) -> CAE.PostScenarioDescriptor:
        ...
    def Tag(self) -> Tag: ...



class PostScenarioDescriptor(TaggedObject):
    def __init__(self) -> None: ...
    InputDefinitions: CAE.PostScenarioInputDefinitionCollection
    Name: str


class PostScenarioDefinition(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def PrintInformation(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    Name: str


class PostScenarioDataDefinition(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


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
        ...
    Name: str


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
    Visualization: CAE.PostScenarioVisualizationDefinition


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



class PostScenario(NXObject):
    def __init__(self) -> None: ...


class PostResultPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    ReadOneModeOrthogonalPair: bool


class PostResultNavigatorPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    Format: CAE.Post.Format
    SignificantPlaces: int


class PostProcessingSessionApplicator(Builder):
    def __init__(self) -> None: ...
    def SetFile(self, filePath: str) -> None:
        ...


class PostProcessingSession(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.Post) -> None: ...
    def CreateBuilder(self, part: CAE.CaePart) -> CAE.PostProcessingSessionApplicator:
        ...
    def ExportToFile(self, part: CAE.CaePart, filePath: str) -> None:
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
    LegendMultipleOverlaysState: bool
    Position: CAE.Post.Position
    SignificantPlaces: int


class PostJtExportBuilder(Builder):
    def __init__(self) -> None: ...
    Component: CAE.Result.Component
    Jtdatasetname: str
    Jtfilename: str
    Layer: int
    Ply: int
    Result: CAE.Result
    ResultType: CAE.BaseResultType


class PostIdentifyPreference(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.PostPreference) -> None: ...
    def Tag(self) -> Tag: ...

    Format: CAE.Post.Format
    SignificantPlaces: int


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
    IterationStepSpacing: int
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
    BoxColor: NXColor
    BoxFill: bool
    BoxTextAlignment: CAE.PostAnnotation.TextAlignment
    BoxTranluceny: bool
    BoxTranslucency: bool
    DisplayStyle: CAE.PostAnnotation.Style
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
        ...
    def PostviewGetColorbar(self, postviewId: int, customOverwrite: int) -> CAE.Post.Colorbar:
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
        ...
    def PostviewSetResultWithNodalForceReport(self, postviewId: int, nodalforcereportparams: CAE.ResultParametersWithNodalForceReport) -> None:
        ...
    def PostviewSetEdgeFace(self, postviewId: int, primaryEdgeface: CAE.Post.PrimaryEdgeFace, undeformedEdgeface: CAE.Post.EdgeFace) -> None:
        ...
    def PostviewSetEdgeFace(self, postviewId: int, primaryEdgeface: CAE.Post.PrimaryEdgeFace) -> None:
        ...
    def Tag(self) -> Tag: ...

    Preference: CAE.PostPreference
    PostProcessingSession: CAE.PostProcessingSession


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
    

    class Spectrum(enum.Enum):
        Structural = 0
        Thermal = 1
        GrayScale = 2
        StopLight = 3
    

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
    

    class NodeValueSharingCriterion(enum.Enum):
        Average = 0
        Minimum = 1
        Maximum = 2
        Sum = 3
    

    class NoDataTreatment(enum.Enum):
        Ignore = 0
        SpecifiedValue = 1
    

    class MarkTensorStyle(enum.Enum):
        BoxAndArrows = 0
        OnlyArrows = 1
        OnlyBox = 2
    

    class MarkSize(enum.Enum):
        ResultValue = 0
        Specified = 1
    

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
        def ToString(self) -> str:
            ...
    

    class Abcissa(enum.Enum):
        Uneven = 0
        Even = 1
        Sequenced = 2
    

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
    def Tag(self) -> Tag: ...

    CaeGeometryRecipes: CAE.GeometryRecipeCollection


    class PolygonBodyResolutionType(enum.Enum):
        Standard = 0
        Medium = 1
        High = 2
    

class PolygonFaceOnMeshBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryMerging: Expression
    ElementEdgeFeatureAngle: Expression
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
        ...
    def SetHighLabelPreference(self, useHighLabel: bool) -> None:
        ...
    HighLabelPreference: bool
    Point: Point
    Tolerance: float


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
    def Tag(self) -> Tag: ...



    class FolderType(enum.Enum):
        New = 0
        Existing = 1
    

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
    def CreateElementModifyOrderBuilder(self) -> CAE.ElementModifyOrderBuilder:
        ...
    def CreateSurfaceCoatBuilder(self) -> CAE.SurfaceCoatBuilder:
        ...
    def CreateCombineTrisBuilder(self) -> CAE.CombineTrisBuilder:
        ...
    def CreateElementExtractBuilder(self) -> CAE.ElementExtractBuilder:
        ...
    def CreateSweepBetweenMeshBuilder(self) -> CAE.SweepBetweenMeshBuilder:
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
    def CreateConvexMeshBuilder(self) -> CAE.ConvexMeshBuilder:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.NodeElementManager instead.")"""
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
    def CreateElementRotateBuilder(self) -> CAE.ElementRotateBuilder:
        ...
    def CreateOpenDuctMeshBuilder(self, mesh: CAE.RecipeOpenDuctMesh) -> CAE.OpenDuctMeshBuilder:
        ...
    def Tag(self) -> Tag: ...

    ElemInfoUtils: CAE.ElementInfoUtils
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
    ForceType: CAE.NodalForceReportBuilder.Force
    GridPointAppliedForce: bool
    GridPointForce: bool
    GridPointReactionForce: bool
    GridPointReactionForceMPC: bool
    LoadCaseIndex: int
    LoadCaseType: CAE.NodalForceReportBuilder.LoadcaseSelection
    NfrName: str
    NodeRefs: CAE.SelectFENodeList
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
    

class NodalForceReport(Fields.Field):
    def __init__(self) -> None: ...
    def Information(self) -> None:
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
    StartLabel: int


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
    def SetRepToSuperElement(self, pcFileName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.ModifiableFEModelOccAttribute.SetAltRepType instead.")"""
        ...
    def SetAltRepType(self, pcAltRepDescNeutralName: str, lengthUnits: CAE.FEModelOccAttribute.AltRepLengthUnitType, massUnits: CAE.FEModelOccAttribute.AltRepMassUnitType, femdataset: CAE.AlternateFemRepresentationSource, pcFileName: str) -> None:
        ...
    def ReloadSuperElementFile(self) -> None:
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
        ...
    def SetModeStatus(self, index: int, status: bool) -> None:
        ...
    def SetModeUndampedFrequency(self, index: int, undampedFrequency: float) -> None:
        ...
    def SetModeDampingRatio(self, index: int, dampingRatio: float) -> None:
        ...
    def SetModeModalMass(self, index: int, modalMassReal: float, modalMassImg: float) -> None:
        ...
    def SetModeAnnotation(self, index: int, annotation: str) -> None:
        ...


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
    DesignVariables: CAE.ModelUpdateDesignVariablesCollection


    class TargetType(enum.Enum):
        All = 0
        Frequencies = 1
        ModeShapes = 2
    

class ModelUpdateSensitivityViewerBuilder(Builder):
    def __init__(self) -> None: ...
    def GetTargetIds(self, targetIds: int) -> None:
        ...
    def SetTargetIds(self, targetIds: int) -> None:
        ...
    def GetDesignVariableLabels(self) -> str:
        ...
    def SetDesignVariableLabels(self, designVaraibleLabels: str) -> None:
        ...
    def GetSensitivityValues(self) -> float:
        ...
    def SetSensitivityValues(self, sensitivityValues: float) -> None:
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
    NodeColor: NXColor
    NodeDisplayMode: CAE.ModelDisplayBuilder.NodeDisplayModeType
    NodeMarker: CAE.ModelDisplayBuilder.NodeMarkerType
    NodeMeshShowHideOption: CAE.ModelDisplayBuilder.NodeMeshShowHideOptionType
    NodeSelectInternal: bool
    NodeUnattachedMarker: CAE.ModelDisplayBuilder.NodeUnattachedMarkerType
    RotationAxisColor: NXColor
    RotationAxisDisplaySwitch: bool
    RotationAxisFont: CAE.ModelDisplayBuilder.RotationAxisLineFont
    RotationAxisLineWidth: CAE.ModelDisplayBuilder.RotationAxisWidth
    SolverDisplayMode: str
    UnattachedNodesInBoundingBoxRatio: float


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
        SolverSpecific = 9
    

    class ElemQualPass(enum.Enum):
        Shaded = 0
        Wireframe = 1
    

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
    def Tag(self) -> Tag: ...



class MMCCreateBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitMmcs(self) -> typing.List[CAE.MeshMate]:
        ...
    AutoSelection: SelectDisplayableObjectList
    DistTolerance: Expression
    FaceSearchOption: CAE.MMCCreateBuilder.FaceSearchType
    MeshMatingOption: CAE.MMCCreateBuilder.MeshMatingType
    Mmc: CAE.MeshMate
    ReverseDirection: bool
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
    ProjectToNearestGeometry: bool
    ProjectionOption: CAE.MeshPointProjectBuilder.ProjectionMethod
    ProjectionTolerance: float
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


class MeshFromBoundaryBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSourceElementEdgePathMethod(self, sourceElementEdgePathMethod: CAE.ElemEdgePathMethod) -> None:
        ...
    def SetTargetElementEdgePathMethod(self, targetElementEdgePathMethod: CAE.ElemEdgePathMethod) -> None:
        ...
    ClosedLoopSelection: SelectTaggedObjectList
    CollectorName: str
    ElementType: CAE.ElementTypeBuilder
    Layers: int
    LoopType: CAE.MeshFromBoundaryBuilder.LoopOption
    NumElementsOnRail1: int
    NumElementsOnRail2: int
    RailType: CAE.MeshFromBoundaryBuilder.RailOption


    class RailOption(enum.Enum):
        Uniform = 0
        Transition = 1
    

    class LoopOption(enum.Enum):
        SourceTarget = 0
        ClosedLoop = 1
    

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
    CylinderDensitySize: int
    DependentEdgeDensitySize: int
    EdgeDensitySize: int
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
    AspectRatio: Expression
    BlBodySelection: SelectNXObjectList
    BlBodySelectionToggle: bool
    BoundingVolumeBodySelection: SelectNXObjectList
    BoundingVolumeDensityElementSize: Expression
    ChordalTolerance: Expression
    CylinderAxialElementSize: Expression
    CylinderAxialElementSizeOption: CAE.MeshControlBuilder.CylinderAxialElementSizeType
    CylinderAxialNumElements: int
    CylinderCircularNumElements: int
    CylinderCircularNumPerQuarter: int
    CylinderCircularSizeOption: CAE.MeshControlBuilder.CylinderCircularSizeType
    CylinderFreezeGeometryOption: bool
    CylinderMaxAngle: Expression
    CylinderMaxRadius: Expression
    CylinderMinAngle: Expression
    CylinderMinRadius: Expression
    EdgeFraction: Expression
    EndSize: Expression
    FilletAxialElementSizeOption: CAE.MeshControlBuilder.FilletAxialElementSizeType
    FilletCircumMinElementSize: Expression
    FilletCircumNumberElements: int
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
    MappedNumberOfLayers: int
    MappedOffset: Expression
    MinimumElementSize: Expression
    MinimumElementSizeOption: bool
    NumOfElements: int
    NumberOfLayers: int
    OverallSize: Expression
    PointElementSize: Expression
    PointRadiusOfInfluence: Expression
    ProgressionSubtype: CAE.MeshControlBuilder.ProgressionTypes
    SelectWeldFace: SelectNXObjectList
    Selection: SelectNXObjectList
    SelectionFilterToggle: bool
    SizeSubtype: CAE.MeshControlBuilder.SizeTypes
    SizingOption: CAE.MeshControlBuilder.SizingType
    SpacingElementSize: Expression
    SpacingNumberOfElements: int
    StartSize: Expression
    TotalThickness: Expression
    WeldDirection: CAE.MeshControlBuilder.WeldSide
    WeldDirectionScarEdge: NXObject
    WeldNumberOfLayers: int
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
    PropertyTable: CAE.PropertyTable
    SelectionList: SelectDisplayableObjectList
    SourceFace: SelectDisplayableObject
    SourceFaceList: SelectDisplayableObjectList
    TargetFace: SelectDisplayableObject
    TargetFaceList: SelectDisplayableObjectList
    WallFaceList: SelectDisplayableObjectList


    class Type(enum.Enum):
        Automatic = 0
        Manual = 1
        BetweenAutomatic = 2
        BetweenManual = 3
    

class Mesh3d(CAE.Mesh):
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
    Jacobian: float
    KeepFreeMeshes: bool
    MergeEdges: bool
    MidNodeOption: CAE.MappedMeshBuilder.MidNodeType
    ProjectVertices: bool
    QuadOnlyMesh: bool
    SelectionFace: SelectDisplayableObjectList


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
        """[Obsolete("Deprecated in NX10.0.0.  Use CAE.Mesh3dHexBuilder..")"""
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
    ElementList: CAE.SelectElementsBuilder
    FactorValue: Expression
    SelectionElementEdges: SelectTaggedObjectList
    SizeOption: CAE.LocalRemeshBuilder.Option
    SizeValue: Expression
    Transition: int


    class Option(enum.Enum):
        Factor = 0
        Size = 1
    

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


class LayoutStateCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.LayoutState]:
        ...
    def __init__(self, owner: CAE.CaePart) -> None: ...
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
    def Tag(self) -> Tag: ...



class LayoutStateBuilder(Builder):
    def __init__(self) -> None: ...
    def CommitLayoutState(self) -> CAE.LayoutState:
        ...
    def SetName(self, name: str) -> None:
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
    def Rename(self, name: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.LayoutState.Name instead.")"""
        ...
    def GetViewportDescription(self, viewport: int) -> str:
        ...
    def SetViewportDescription(self, viewport: int, xmloutput: str) -> None:
        ...
    Name: str


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
    Name: str
    PlyBottom: bool
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
        StrainXX = 11
        StrainYY = 12
        StrainZZ = 13
        StrainXY = 14
        StrainZX = 15
        StrainYZ = 16
        StrainMaxP = 17
        StrainMinP = 18
        StrainMaxS = 19
        PlyFailureIndex = 20
        PlyStrengthRatio = 21
        PlyMarginofSafety = 22
        BondFailureIndex = 23
        BondStrengthRatio = 24
        BondMarginofSafety = 25
    

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
        StrainXX = 10
        StrainYY = 11
        StrainZZ = 12
        StrainXY = 13
        StrainZX = 14
        StrainYZ = 15
        StrainMaxP = 16
        StrainMinP = 17
        StrainMaxS = 18
        PlyFailureIndex = 19
        PlyStrengthRatio = 20
        PlyMarginofSafety = 21
        BondFailureIndex = 22
        BondStrengthRatio = 23
        BondMarginofSafety = 24
    

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
    

    class InterLaminarFailureTheoryType(enum.Enum):
        None = 0
        TransverseShearStress = 1
        NormalStress = 2
        UserDefined = 3
    

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
    ImportMaterials: bool
    ImportMethod: CAE.LaminateImportedLayupBuilder.ImportMethodEnum
    LayupName: str
    MaxDeviationAngle: Expression
    MeshSizeFactor: float
    NameOverride: bool
    NodalMapping: int
    NumDiscretizationPoints: int
    OmitPartiallyMapped: bool
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
    Name: str
    OverallOnly: bool
    PlyBottom: bool
    PlyExportOption: CAE.LaminateGraphicalReportBuilder.PlyExportOptionType
    PlyFilter: CAE.LaminatePlyFilterBuilder
    PlyMiddle: bool
    PlyStrain: bool
    PlyStrainRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    PlyStress: bool
    PlyStressRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    PlyTop: bool
    SafetyFactor: float
    SafetyMargin: bool
    SafetyMarginRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule
    ShowLoadCases: bool
    ShowPlyResults: bool
    SolverInput: CAE.LaminateGraphicalReportBuilder.SolverInputType
    StrengthRatio: bool
    StrengthRatioRule: CAE.LaminateGraphicalReportBuilder.EnvelopeRule


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
    def __init__(self, owner: CAE.FEModel) -> None: ...
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
    def Tag(self) -> Tag: ...

    GlobalLayups: CAE.LaminateGlobalLayupCollection
    LayupOffsets: CAE.LaminateLayupOffsetCollection
    MatOrientations: CAE.LaminateMatOrientationCollection
    ExtrudeSetups: CAE.LaminateExtrudeSetupCollection
    DefaultLayupOffset: CAE.LaminateLayupOffset
    DefaultMaterialOrientation: int


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
    PlyGroups: CAE.LaminatePlyGroupCollection
    Parameters: CAE.PropertyTable
    StrengthLoadcase: CAE.PropertyTable
    UserDefinedInterLaminarFailureTheory: str
    UserDefinedPlyFailureTheory: str


class LabelRangeSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    def GetLabelRanges(self, singleLabels: int, startLabels: int, endLabels: int, increments: int) -> None:
        ...
    def SetLabelRanges(self, singleLabels: int, startLabels: int, endLabels: int, increments: int) -> None:
        ...


class Iteration(CAE.BaseIteration):
    def __init__(self) -> None: ...
    Label: int




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
    SnapTolerance: float
    StitchToggle: bool
    TargetFace: SelectDisplayableObjectList


    class ProjectionDirectionType(enum.Enum):
        NaturalExtension = 0
        AlongVector = 1
    

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


class ImportedResult(CAE.Result):
    def __init__(self) -> None: ...
    def GetFiletype(self) -> CAE.Result.Filetype:
        ...
    def GetFilename(self) -> str:
        ...


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


class IAncillaryDisplayableEntity():
    def AncillaryDisplay(self) -> None:
        ...


class HybridMesh(CAE.Mesh):
    def __init__(self) -> None: ...


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
        ...
    def GetUnits(self, xUnit: CAE.XyFunctionUnit, yUnit: CAE.XyFunctionUnit, frfUnit: CAE.XyFunctionUnit) -> None:
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
    InitialEstimateValue: float
    Name: str


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
    

class FreezeGeometryRecipe(CAE.GeometryRecipe):
    def __init__(self) -> None: ...


class FreezeGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    FaceSelect: SelectTaggedObjectList


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
    ColinearThreshold: float
    CollectorName: str
    CoplanarThreshold: float
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


class FilletFaceMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetFaces(self) -> typing.List[CAE.CAEFace]:
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
    SynchronizeLinesFlag: bool
    SynchronizePointsFlag: bool
    SynchronizeSketchCurvesFlag: bool
    SynchronizeSplinesFlag: bool


class FemSignalProcessingSignalAttributes(NXObject):
    def __init__(self) -> None: ...
    def GetApplication(self) -> Fields.IApplication:
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
    def SetMeshPreferences(self, tinyEdgeColor: NXColor, snapTolerance: float, projectNodesToCadOption: int, projectionTolerance: float, refineTessellation: int) -> None:
        ...
    def GetMeshPreferences(self, tinyEdgeColor: NXColor, snapTolerance: float, projectNodesToCadOption: int, projectionTolerance: float, refineTessellation: int) -> None:
        ...
    def BodyRecreateNew(self, body: Body) -> None:
        ...
    def BodiesRecreateNew(self, listOfBodies: typing.List[Body]) -> None:
        ...
    def BodyDelete(self, body: Body) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.CAE.FemPart.PolygonBodyDelete instead.")"""
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
    def FinalizeCreation(self, cadPart: Part, idealizedPartName: str, useBodiesOption: CAE.FemPart.UseBodiesOption, bodies: typing.List[Body], geometrySyncOptions: CAE.FemSynchronizeOptions, solverTypeName: str, analysisTypeType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType, description: str) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.FemPart.FinalizeCreation that takes CAE.FemCreationOptions as an input argument.")"""
        ...
    def FinalizeCreation(self, cadPart: Part, idealizedPartName: str, useBodiesOption: CAE.FemPart.UseBodiesOption, bodies: typing.List[Body], geometrySyncOptions: CAE.FemSynchronizeOptions, solverTypeName: str, analysisTypeType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType, description: str, isMorphEnabled: bool) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.FemPart.FinalizeCreation that takes CAE.FemCreationOptions as an input argument.")"""
        ...
    def FinalizeCreationManaged(self, cadPart: Part, createIdealPart: bool, useBodiesOption: CAE.FemPart.UseBodiesOption, bodies: typing.List[Body], geometrySyncOptions: CAE.FemSynchronizeOptions, solverTypeName: str, analysisTypeType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType, description: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.FemPart.FinalizeCreation that takes CAE.FemCreationOptions as an input argument.")"""
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
    def GetLabelOffsets(self, nodeOffset: int, elemOffset: int, csysOffset: int) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.FEModelOccurrence.GetOccEntityLabelOffsetsinstead.")"""
        ...
    def GetOccEntityLabelOffsets(self, nodeOffset: int, elemOffset: int, csysOffset: int, physOffset: int, groupOffset: int, plyOffset: int) -> None:
        ...
    def SetLabelOffsets(self, nodeOffset: int, elemOffset: int, csysOffset: int) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.CAE.FEModelOccurrence.SetOccEntityLabelOffsetsinstead.")"""
        ...
    def SetOccEntityLabelOffsets(self, nodeOffset: int, elemOffset: int, csysOffset: int, physOffset: int, groupOffset: int, plyOffset: int) -> None:
        ...
    def GetAttributes(self) -> CAE.FEModelOccAttribute:
        ...
    def GetChildren(self) -> typing.List[CAE.FEModelOccurrence]:
        ...
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
    GlobalLayupMgr: CAE.LaminateGlobalLayupMgr
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
    def SetSolverOptions(self, solverName: str, analysisType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType) -> None:
        ...
    def SetDescription(self, description: str) -> None:
        ...
    def SetMorphingFlag(self, isMorphEnabled: bool) -> None:
        ...
    def SetCyclicSymmetryData(self, useCyclicSymmetryCsys: bool, cyclicSymmetryCsys: CoordinateSystem) -> None:
        ...


    class UseBodiesOption(enum.Enum):
        SelectedBodies = 0
        VisibleBodies = 1
        AllBodies = 2
    

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


class FeatureEdgeNodeMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNodes(self) -> typing.List[CAE.FENode]:
        ...


class FaceFromBoundaryBuilder(Builder):
    def __init__(self) -> None: ...
    def AddSelectedPointPairs(self) -> None:
        ...
    EdgeSelection: CAE.SelectCAEEdgeList
    FirstPtSelect: Point
    PolygonBodySelection: CAE.SelectCAEBody
    SecondPtSelect: Point


class FaceFaceImprintBuilder(Builder):
    def __init__(self) -> None: ...
    GeomSelection: SelectDisplayableObjectList
    StitchOption: bool
    ToleranceDistance: float


class FaceDensity(CAE.MeshControl):
    def __init__(self) -> None: ...


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
    

    class Order(enum.Enum):
        Undefined = 0
        Linear = 1
        Parabolic = 2
        Mixed = 3
    

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
    

    class ElementOrderType(enum.Enum):
        Any = 0
        Linear = 1
        Parabolic = 2
    

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
    CollectorName: str
    ElementDimensionOption: CAE.ElementReflectBuilder.ElemDimType
    ElementType: CAE.ElementTypeBuilder
    Elements: CAE.SelectElementsBuilder
    ExportMesh: bool
    Increment: int
    Label: int
    LabelOption: CAE.ElementReflectBuilder.LabelType
    MeshName: str
    MovToggle: bool
    NeutralName: str
    NewMeshOption: CAE.ElementReflectBuilder.NewMeshType
    Offset: int
    Plane: Plane
    SolidElmOption: CAE.ElementReflectBuilder.SolidElemMovDirType


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
        ...
    def SetBeamData(self, element: CAE.FEElement, physicalPropertyTable: CAE.PhysicalPropertyTable, oriMethod: CAE.CaeElementAssociatedDataUtilsOrientationMethod, vectorType: CAE.CaeElementAssociatedDataUtilsVectorChoiceType, direction: Direction, orientationNode: CAE.FENode, endReleaseA: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndADOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndADOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, endReleaseB: CAE.CaeElementAssociatedDataUtilsEndReleaseState, pinFlagEndBDOF1: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF2: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF3: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF4: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF5: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, pinFlagEndBDOF6: CAE.CaeElementAssociatedDataUtilsEndReleaseSetting, xOffsetEndA: float, yOffsetEndA: float, zOffsetEndA: float, xOffsetEndB: float, yOffsetEndB: float, zOffsetEndB: float) -> None:
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
        ...
    def SetRigidData(self, element: CAE.FEElement, dofs: typing.List[CAE.CaeElementAssociatedDataUtilsDof]) -> None:
        ...
    def AskDamperData(self, element: CAE.FEElement, hasAssociatedDataDefined: bool, viscousDamping: float, physicalPropertyTable: CAE.PhysicalPropertyTable, componentEndA: CAE.CaeElementAssociatedDataUtilsComponentEnd, componentEndB: CAE.CaeElementAssociatedDataUtilsComponentEnd) -> None:
        ...
    def SetDamperData(self, element: CAE.FEElement, viscousDamping: float, physicalPropertyTable: CAE.PhysicalPropertyTable, componentEndA: CAE.CaeElementAssociatedDataUtilsComponentEnd, componentEndB: CAE.CaeElementAssociatedDataUtilsComponentEnd) -> None:
        ...
    def Tag(self) -> Tag: ...



class ElemEdgePathMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def AddSeedEdge(self, seedStartNode: CAE.FENode, seedElemEdge: CAE.FEElemEdge) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.ElemEdgePathMethod.AddSeedEdge with additional arguments instead.")"""
        ...
    def AddSeedEdge(self, seedStartNode: CAE.FENode, seedElemEdge: CAE.FEElemEdge, preferFreeEdges: bool, preferGeometryAssociatedEdges: bool, preferFeatureElementEdge: bool, featureAngleTolerance: float, allowGapJumping: bool, gapJumpingTolerance: float) -> None:
        ...
    def RemoveSeedEdge(self, seedElemEdge: CAE.FEElemEdge) -> None:
        ...
    def FlipPath(self) -> None:
        ...
    def GetSeedEdges(self, seedStartNodes: typing.List[CAE.FENode], seedElemEdges: typing.List[CAE.FEElemEdge]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.ElemEdgePathMethod.GetSeeds instead.")"""
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
    

class EdgePathMethod(SelectionMethod):
    def __init__(self, ptr: int) -> None: ...
    def AddSeedEdge(self, seedStartVertex: CAE.CAEVertex, seedEdge: CAE.CAEEdge) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use overloaded NXOpen.CAE.EdgePathMethod.AddSeedEdge with additional arguments instead.")"""
        ...
    def AddSeedEdge(self, seedStartVertex: CAE.CAEVertex, seedEdge: CAE.CAEEdge, preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float) -> None:
        ...
    def RemoveSeedEdge(self, seedEdge: CAE.CAEEdge) -> None:
        ...
    def FlipPath(self) -> None:
        ...
    def GetSeedEdges(self, seedStartVertices: typing.List[CAE.CAEVertex], seedEdges: typing.List[CAE.CAEEdge]) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.CAE.EdgePathMethod.GetSeeds instead.")"""
        ...
    def GetSeeds(self, seedStartVertices: typing.List[CAE.CAEVertex], seedEdges: typing.List[CAE.CAEEdge], preferFreeEdges: bool, allowGapJumping: bool, gapJumpingTolerance: float) -> None:
        ...
    def GetPathEdges(self, pathStartVertices: typing.List[CAE.CAEVertex], pathEdges: typing.List[CAE.CAEEdge]) -> None:
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
    Acceleration: Expression
    Angle: Expression
    AngularAcceleration: Expression
    AngularVelocity: Expression
    CaseSensitive: bool
    FeResults: CAE.DurSpecialistDataSources
    FieldFind: int
    FieldFindUsing: str
    FieldMatchUsing: str
    FieldMatchWith: int
    Find: str
    FindIn: CAE.DurSpecialistSuperpositionEventBuilder.FindInType
    Force: Expression
    IgnoreSpecialCharacters: bool
    Length: Expression
    LoadHistories: CAE.DurSpecialistDataSources
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    MatchBy: CAE.DurSpecialistSuperpositionEventBuilder.MatchByType
    MatchUsing: CAE.DurSpecialistSuperpositionEventBuilder.MatchUsingType
    MatchWith: str
    Matching: CAE.DurSpecialistSuperpositionEventBuilder.MatchingType
    MatchingUpdate: CAE.DurSpecialistEvent.UpdateCriterionType
    MaxLength: int
    MinLength: int
    Moment: Expression
    PreStressCase: int
    PreStressIncluded: bool
    PreStressScale: Expression
    PreStressUpdate: CAE.DurSpecialistEvent.UpdateCriterionType
    Pressure: Expression
    Range: CAE.DurSpecialistSuperpositionEventBuilder.RangeType
    RangeEnd: Expression
    RangeStart: Expression
    StaticLoadUpdate: CAE.DurSpecialistEvent.UpdateCriterionType
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
    

    class FindInType(enum.Enum):
        LoadHistories = 0
        Subcases = 1
    

class DurSpecialistSuperpositionEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


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
    def Tag(self) -> Tag: ...



class DurSpecialistSolutionBuilder(Builder):
    def __init__(self) -> None: ...
    def Reset(self) -> None:
        ...
    AnalysisType: CAE.DurSpecialistAnalysisType
    LoadProvider: NXObject
    MaterialSource: CAE.DurSpecialistSolutionBuilder.MaterialSourceType
    Name: str
    SelectedMaterial: PhysicalMaterial
    SimulationObjects: CAE.DurSpecialistSimulationObjectTable


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
    def Solve(self) -> None:
        ...
    def InformationWindow(self) -> None:
        ...
    LocalDefinitions: CAE.DurSpecialistLocalDefinitionCollection


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
    def InformationWindow(self) -> None:
        ...
    IsInherited: bool
    ParameterObject: CAE.DurSpecialistParameterObject


class DurSpecialistParameterObjectCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistParameterObject]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def Find(self, neutralName: str) -> CAE.DurSpecialistParameterObject:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistParameterObject(TaggedObject):
    def __init__(self) -> None: ...


class DurSpecialistManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def Tag(self) -> Tag: ...

    Solutions: CAE.DurSpecialistSolutionCollection
    AnalysisTypes: CAE.DurSpecialistAnalysisTypeCollection
    ParameterObjects: CAE.DurSpecialistParameterObjectCollection
    LoadProviders: CAE.DurSpecialistLoadProviderCollection


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
    def CreateLocalDefinitionByGroupBuilder(self) -> CAE.DurSpecialistLocalDefinitionByGroupBuilder:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistLocalDefinitionByGroupBuilder(Builder):
    def __init__(self) -> None: ...
    def SetGroups(self, groups: typing.List[NXObject]) -> None:
        ...
    Type: CAE.DurSpecialistLocalDefinitionByGroupBuilder.LocalDefinitionType


    class LocalDefinitionType(enum.Enum):
        Joint = 0
        Separate = 1
    

class DurSpecialistLocalDefinitionBuilder(Builder):
    def __init__(self) -> None: ...
    AnalysisType: CAE.DurSpecialistAnalysisType
    IsAnalysisTypeInherited: bool
    IsMaterialInherited: bool
    Location: CAE.DurSpecialistLocalDefinitionBuilder.LocationType
    MaterialSource: CAE.DurSpecialistSolutionBuilder.MaterialSourceType
    Name: str
    SelectedMaterial: PhysicalMaterial
    SimulationObjects: CAE.DurSpecialistSimulationObjectTable
    TargetSet: CAE.SetManager


    class LocationType(enum.Enum):
        Specify = 0
        UseRemainingStructure = 1
    

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


class DurSpecialistLoadProviderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistLoadProvider]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> CAE.DurSpecialistLoadProvider:
        ...
    def CreateLoadProviderBuilder(self, loadProvider: CAE.DurSpecialistLoadProvider) -> CAE.DurSpecialistLoadProviderBuilder:
        ...
    def CreateBlockLoadEventBuilder(self, eventObject: CAE.DurSpecialistBlockLoadEvent) -> CAE.DurSpecialistBlockLoadEventBuilder:
        ...
    def CreateSuperpositionEventBuilder(self, eventObject: CAE.DurSpecialistSuperpositionEvent) -> CAE.DurSpecialistSuperpositionEventBuilder:
        ...
    def InformationWindow(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistLoadProviderBuilder(Builder):
    def __init__(self) -> None: ...
    Description: str
    Event: CAE.DurSpecialistEvent
    LoadDefinition: CAE.DurSpecialistEvent.EventType
    Name: str


class DurSpecialistLoadProvider(NXObject):
    def __init__(self) -> None: ...
    def Rename(self, title: str) -> None:
        ...
    def CloneLoadProvider(self) -> CAE.DurSpecialistLoadProvider:
        ...
    def InformationWindow(self) -> None:
        ...


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
    

class DurSpecialistDataSources(TaggedObject):
    def __init__(self) -> None: ...
    def AddDataSource(self, fileName: str, driver: int) -> int:
        ...
    def RemoveDataSource(self, fileIndex: int) -> None:
        ...
    def InformationWindow(self, fileIndex: int) -> None:
        ...


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
    

class DurSpecialistBlockLoadEventBuilder(Builder):
    def __init__(self) -> None: ...
    LoadLength: CAE.DurSpecialistLoadLengthBuilder
    LowerValue: Expression
    ModeSelection: CAE.DurSpecialistEvent.UpdateCriterionType
    Pattern: CAE.DurSpecialistBlockLoadEventBuilder.PatternType
    StartWithLower: bool
    UpperValue: Expression


    class PatternType(enum.Enum):
        Swelling = 0
        Alternating = 1
        Free = 2
    

class DurSpecialistBlockLoadEvent(CAE.DurSpecialistEvent):
    def __init__(self) -> None: ...


class DurSpecialistAnalysisTypeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.DurSpecialistAnalysisType]:
        ...
    def __init__(self, owner: CAE.DurSpecialistManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, neutralName: str) -> CAE.DurSpecialistAnalysisType:
        ...
    def CreateAnalysisTypeBuilder(self, analysisType: CAE.DurSpecialistAnalysisType) -> CAE.DurSpecialistAnalysisTypeBuilder:
        ...
    def Tag(self) -> Tag: ...



class DurSpecialistAnalysisTypeBuilder(Builder):
    def __init__(self) -> None: ...
    Implicit: CAE.DurSpecialistSimulationObjectTable
    Name: str
    Optional: CAE.DurSpecialistSimulationObjectTable
    Required: CAE.DurSpecialistSimulationObjectTable


class DurSpecialistAnalysisType(NXObject):
    def __init__(self) -> None: ...


class DurabilityTransientEventBuilder(CAE.DurabilityEventBuilder):
    def __init__(self) -> None: ...
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
    ReferenceNodeLabel: int
    Scale: float


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
    def Tag(self) -> Tag: ...



class DataSourceBuilder(Builder):
    def __init__(self) -> None: ...
    SourceFile: str
    SourceName: str
    SourceObject: CAE.IPostScenarioDataSource


class DataSource(NXObject):
    def __init__(self) -> None: ...
    def GetDefinitions(self) -> typing.List[CAE.PostScenarioDefinition]:
        ...
    def GetDefinitionByName(self, name: str) -> CAE.PostScenarioDefinition:
        ...
    def PrintInformation(self) -> None:
        ...
    Name: str


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
    def GetEndpointsDiameter(self, baseCenter: Point, topCenter: Point, diameter: Expression) -> None:
        ...
    def SetEndpointsDiameter(self, baseCenter: Point, topCenter: Point, diameter: Expression) -> None:
        ...


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
    

class CorrelSolutionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.CorrelSolution]:
        ...
    def __init__(self, owner: CAE.CorrelManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateSolutionBuilder(self, solution: CAE.CorrelSolution) -> CAE.CorrelSolutionBuilder:
        ...
    def CreateShapeMetricViewerBuilder(self, solution: CAE.CorrelSolution) -> CAE.ShapeMetricViewerBuilder:
        ...
    def CreateComacViewerBuilder(self) -> CAE.ComacViewerBuilder:
        ...
    def GetValidSolutionName(self) -> str:
        ...
    def CloneSolution(self, oldSolution: CAE.CorrelSolution, suggestedName: str) -> CAE.CorrelSolution:
        ...
    def FindObject(self, solutionName: str) -> CAE.CorrelSolution:
        ...
    def Tag(self) -> Tag: ...

    ActiveSolution: CAE.CorrelSolution


class CorrelSolutionBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    FrfDampingSource: CAE.CorrelSolutionBuilder.EnumDampingFrftype
    HighFrequencyCutoff: float
    HighFrequencyFilteringMode: bool
    LowFrequencyCutoff: float
    LowFrequencyFilteringMode: bool
    NodeMapSizeLimit: int
    NodeMapSizeLimitActive: bool
    NodeMatchingDistance: float
    ReferenceSolution: CAE.SimSolution
    Title: str
    WorkSolution: CAE.SimSolution


    class EnumDampingFrftype(enum.Enum):
        FromWorkModel = 0
        SpecifyDamping = 1
    

class CorrelSolution(NXObject):
    def __init__(self) -> None: ...
    def CreateModePairingBuilder(self) -> CAE.CorrelModePairingBuilder:
        ...
    def GetSolutionName(self) -> str:
        ...
    def SetSolutionName(self, solutionName: str, renameResultFile: bool) -> None:
        ...
    def Destroy(self, deleteResultFile: bool) -> None:
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
        ...
    def ComputeModePairsForSol(self) -> None:
        ...
    def CloneCorrelation(self) -> CAE.CorrelSolution:
        ...
    def UpdateResultsForSolution(self, tSolution: CAE.SimSolution, ignoreReload: bool) -> None:
        ...
    def GenerateMatchingDofset(self) -> None:
        ...
    def GenerateComacResults(self) -> None:
        ...
    def ImportNodeMapCsvFile(self, filename: str) -> None:
        ...
    def ExportNodeMapCsvFile(self, filename: str) -> None:
        ...
    def LockNodeMap(self) -> None:
        ...
    def UnlockNodeMap(self) -> None:
        ...


class CorrelShapemetrictype(enum.Enum):
    Mac = 0
    Comac = 1
    Msf = 2
    Xortho = 3
    Nco = 4
    Sco = 5


class CorrelModePairingBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    def AddManualPair(self, refModeId: int, workModeId: int) -> None:
        ...
    def RemoveManualPair(self, refModeId: int, workModeId: int) -> None:
        ...
    def ClearAllManualPairs(self) -> None:
        ...
    AutomaticRule: CAE.CorrelModePairingBuilder.Auto
    FrequencyTolerance: float
    MacLowerBound: float


    class Auto(enum.Enum):
        None = 0
        Sequential = 1
        Frequency = 2
        Mac = 3
        FreqMac = 4
    

class CorrelManager(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.SimSimulation) -> None: ...
    def CreateModelUpdateDesignVariablesRapidCreateBuilderBuilder(self) -> CAE.ModelUpdateDesignVariablesRapidCreateBuilder:
        ...
    def CreateCorrelApplyAlignmentFromBuilder(self, solution: CAE.SimSolution) -> CAE.CorrelApplyAlignmentFromBuilder:
        ...
    def CreateCorrelFineTuneAlignmentBuilder(self, solution: CAE.SimSolution) -> CAE.CorrelFineTuneAlignmentBuilder:
        ...
    def Tag(self) -> Tag: ...

    Solutions: CAE.CorrelSolutionCollection
    PreTests: CAE.PreTestSolutionCollection
    ModelUpdates: CAE.ModelUpdateSolutionCollection


class CorrelFineTuneAlignmentBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    def MoveButton(self) -> None:
        ...
    def RotateButton(self) -> None:
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
    

class CorrelBaseBuilder(Builder):
    def __init__(self) -> None: ...


class CorrelApplyAlignmentFromBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    NativeFileBrowser: str


class CorrelAlignmentBuilder(CAE.CorrelBaseBuilder):
    def __init__(self) -> None: ...
    def GetReferencePt1(self) -> CAE.CorrelAlignmentBuilder.ReferencePt:
        ...
    def SetReferencePt1(self, referencePt1: CAE.CorrelAlignmentBuilder.ReferencePt) -> None:
        ...
    def GetReferencePt2(self) -> CAE.CorrelAlignmentBuilder.ReferencePt:
        ...
    def SetReferencePt2(self, referencePt2: CAE.CorrelAlignmentBuilder.ReferencePt) -> None:
        ...
    def GetReferencePt3(self) -> CAE.CorrelAlignmentBuilder.ReferencePt:
        ...
    def SetReferencePt3(self, referencePt3: CAE.CorrelAlignmentBuilder.ReferencePt) -> None:
        ...
    SaveXmlTransform: bool
    ScalingType: CAE.CorrelAlignmentBuilder.ScalingChoice
    ScalingValue: float
    WrkPt1: Point
    WrkPt2: Point
    WrkPt3: Point


    class ScalingChoice(enum.Enum):
        FromSecondAxis = 0
        Specify = 1
    

    class CorrelAlignmentBuilderReferencePt():
        Defined: bool
        X: float
        Y: float
        Z: float
        def ToString(self) -> str:
            ...
    

class CoordinateSelectionRecipe(CAE.SelectionRecipe):
    def __init__(self) -> None: ...
    def SetCoordinatesAndTolerance(self, coordinates: Point3d, tolerance: float) -> None:
        ...
    def SetHighLabelPreference(self, useHighLabel: bool) -> None:
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
    

class ConstraintResolutionBuilder(Builder):
    def __init__(self) -> None: ...
    PropertyTable: CAE.PropertyTable
    ResolveRule: CAE.ConstraintResolutionBuilder.Rule


    class Rule(enum.Enum):
        ApplyFirstConstraint = 0
        ApplySecondConstraint = 1
        AverageDofValues = 2
        AddDofValues = 3
        SpecifyDofValues = 4
        IgnoreConflict = 5
    

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
        ...


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
        ...
    def SetCoordinateSystem(self, coordinateSystem: CAE.Result.CoordinateSystem) -> None:
        ...
    def GetSelectedCoordinateSystem(self, source: CAE.Result.CoordinateSystemSource, id: int) -> None:
        ...
    def SetSelectedCoordinateSystem(self, source: CAE.Result.CoordinateSystemSource, id: int) -> None:
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
    def Tag(self) -> Tag: ...

    MaterialUtils: MaterialUtilities
    AssociationUtils: CAE.AssociationUtilities
    QualityAuditManager: CAE.QualityAudit.Manager


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
    AtvSets: CAE.AtvSetCollection
    FrfSets: CAE.FrfSetCollection
    ModeSets: CAE.ModeSetCollection
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
    LayoutStates: CAE.LayoutStateCollection
    PostScenarioMgr: CAE.PostScenarioManager
    SelectionRecipes: CAE.SelectionRecipeCollection
    Notes: CAE.NoteManager
    CaeNoteCollection: CAE.NoteCollection
    MarginAnnotationCollection: CAE.AeroStructures.MarginAnnotCollection


    class FieldApplicationType(enum.Enum):
        SignalProcessing = 0
    

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
    def Tag(self) -> Tag: ...



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
    def GetElementEdges(self, objects: typing.List[CAE.ElemEdgefaceObject]) -> None:
        ...
    def GetElementFaces(self, objects: typing.List[CAE.ElemEdgefaceObject]) -> None:
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
    def GetSolverCardSyntax(self) -> str:
        ...
    Label: int


class CAEFace(DisplayableObject):
    def __init__(self) -> None: ...
    def GetUgfaces(self) -> typing.List[Face]:
        ...
    def SynchronizeCadProperties(self) -> None:
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
    def RemoveNodes(self, nodes: typing.List[CAE.FENode]) -> None:
        ...
    def ModifyNodeDofs(self, nodes: typing.List[CAE.FENode], dof1: bool, dof2: bool, dof3: bool, dof4: bool, dof5: bool, dof6: bool) -> None:
        ...
    def RemoveAllNodes(self) -> None:
        ...
    def Information(self) -> None:
        ...
    def GetDisplay(self) -> CAE.CaeDOFSetDisplay:
        ...


class CaeDataContainer(DataContainer):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
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
    def Tag(self) -> Tag: ...



class CAEConnectionBuilder(Builder):
    def __init__(self) -> None: ...
    def MeshDensity(self) -> None:
        ...
    EdgeToEdgeConnectionMethodType: CAE.CAEConnectionBuilder.EdgeToEdgeConnectionMethodTypeEnum
    EdgeTolerance: float
    ElementEdge: CAE.SelectElementsBuilder
    ElementFace: CAE.SelectElementsBuilder
    ElementType: CAE.ElementTypeBuilder
    ElementTypeRbe3: CAE.ElementTypeBuilder
    Isedgeprojectableonface: int
    Label: int
    MethodType: CAE.CAEConnectionBuilder.MethodTypeEnum
    MidNode: bool
    PointToEdgeConnectionMethodType: CAE.CAEConnectionBuilder.PointToEdgeConnectionMethodTypeEnum
    SourceGroup: CAE.CaeGroup
    SourceGroupFilterType: int
    SourceGroupReferenceState: bool
    SourceNodes: CAE.SelectFENodeList
    SourceSelection: SelectTaggedObjectList
    TargetGroup: CAE.CaeGroup
    TargetGroupFilterType: int
    TargetGroupReferenceState: bool
    TargetNodes: CAE.SelectFENodeList
    TargetSelection: SelectTaggedObjectList
    Type: CAE.CAEConnectionBuilder.ConnectionTypeEnum


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
        Rbe3ToEdgeNodes = 6
        Rbe3ToFaceNodes = 7
    

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


class CaeBoundingVolumePrimitiveContainment(enum.Enum):
    Inside = 0
    InsideCrossing = 1


class CAEBody(DisplayableObject):
    def __init__(self) -> None: ...
    def GetTolerance(self) -> float:
        ...
    def SynchronizeCadProperties(self) -> None:
        ...


class CADModeling(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.FemPart) -> None: ...
    def CreateSurfaceFromPolygonFace(self, cadPart: Part, polygonFace: CAE.CAEFace) -> Features.Feature:
        ...
    def CreateCurvesFromPolygonFace(self, cadPart: Part, polygonFace: CAE.CAEFace, lines: typing.List[TaggedObject]) -> None:
        ...
    def Tag(self) -> Tag: ...



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
    

class BeamSectionOccurrence(CAE.BeamSection):
    def __init__(self) -> None: ...
    PrototypeSection: CAE.BeamSection


class BeamSectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CAE.BeamSection]:
        ...
    def __init__(self, owner: CAE.BaseFEModel) -> None: ...
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
    def Tag(self) -> Tag: ...



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
    

    class EndReleaseSetting(enum.Enum):
        Off = 0
        On = 1
    

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
    def SetSolverAndAnalysisType(self, solverTypeName: str, analysisTypeName: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.CAE.BaseFemPart.SetSolverAndAnalysisTypeAndAbstraction instead.")"""
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
    BeamSections: CAE.BeamSectionCollection
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
    ConnectionsRootFolder: CAE.Connections.Folder


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
    GeometrySelection: CAE.SelectCAEFaceList
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
    CurvatureAbstractionSetting: bool
    MergeEdgeSetting: bool
    Selection: SelectDisplayableObjectList
    Tolerance: Expression
    VertexAngle: Expression


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
    def GetUserAttributes(self, attributeName: str, lowValueAttribute: NXObject.AttributeInformation, highValueAttribute: NXObject.AttributeInformation) -> None:
        ...
    def SetUserAttributes(self, attributeName: str, lowValueAttribute: NXObject.AttributeInformation, highValueAttribute: NXObject.AttributeInformation) -> None:
        ...
    def RemoveUserAttributes(self, attributeName: str) -> None:
        ...
    def ClearAllAttributes(self) -> None:
        ...
    def SetUserAttributes(self, setNameAttribute: bool, nameAttribute: str, setColorAttribute: bool, colorAttribute: int, userAttributeNames: str, lowValueAttributes: typing.List[NXObject.AttributeInformation], highValueAttributes: typing.List[NXObject.AttributeInformation]) -> None:
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
    

class AssyFemPart(CAE.BaseFemPart):
    def __init__(self) -> None: ...
    def FinalizeCreation(self, cadPart: Part, solverTypeName: str, analysisTypeType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType, description: str, useCyclicSymmetryCSYS: bool, cyclicSymmetryCsys: CoordinateSystem) -> None:
        ...
    def FinalizeCreation(self, cadPart: Part, solverTypeName: str, analysisTypeType: str, abstractionType: CAE.BaseFemPart.AxisymAbstractionType, description: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.CAE.AssyFemPart.FinalizeCreation that includes CyclicSymmetryCSYS instead.")"""
        ...
    def FinalizeCreation(self, cadPart: Part, solverTypeName: str, analysisTypeType: str, description: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.CAE.AssyFemPart.FinalizeCreation that includes abstraction type instead.")"""
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
    def SetLengthUnit(self, lengthUnit: Unit) -> None:
        ...
    def SetMassUnit(self, massUnit: Unit) -> None:
        ...
    def SetMeshCreationMode(self, creationMode: CAE.AlternateFemRepresentationSource.CreateMeshMode) -> None:
        ...


class AlternateFemRepresentationSource(TaggedObject):
    def __init__(self) -> None: ...
    def Rename(self, name: str) -> None:
        ...
    def ForceUpdate(self) -> None:
        ...


    class CreateMeshMode(enum.Enum):
        AllElements = 0
        DataElements = 1
        VisualizationElements = 2
    

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
    def CalculateSingleMathIndependentDifferentiation(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathFrequencyIntegration(self, gUnitInchFormat: bool, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
        ...
    def CalculateSingleMathFrequencyDifferentiation(self, sourceAfuFileName: str, sourceRecordIndex: int, outputType: CAE.AfuMathOperation.OutputType, destinationAfuFileName: str) -> None:
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
    def TimeToSrs(self, inputAfuFileName: str, inputRecordId: int, dampingRatio: float, freqAxisType: CAE.AfuMathOperation.TimeToSrsAxisType, frequencyMin: float, frequencyMax: float, frequenceIncrement: float, pointsPerDecades: int, responseType: CAE.AfuMathOperation.TimeToSrsResponseType, outputAfuFileName: str, outputRecordName: str) -> None:
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
    

    class SrsToTimeOption(enum.Enum):
        DampedSinusoid = 1
        Wavelet = 2
    

    class SrsToTimeOctave(enum.Enum):
        OneThird = 1
        OneSixth = 2
        OneTwelfth = 3
    

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
    AfuMathOperation: CAE.AfuMathOperation


    class WritingFileMode(enum.Enum):
        Override = 0
        Append = 1
    

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
    AfuAbscissaHeaderInfo: CAE.AfuAbscissaHeaderInfo
    AfuHeaderId: CAE.AfuHeaderId
    AfuOrdinateHeaderInfo: CAE.AfuOrdinateHeaderInfo
    AfuZHeaderInfo: CAE.AfuZHeaderInfo
    Extrapolation: CAE.AfuData.ExtrapolationType
    FileName: str
    FunctionDataType: CAE.XyFunctionDataType
    Interpolation: CAE.AfuData.InterpolationType
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
        Sequence = 2
    

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
    def Tag(self) -> Tag: ...



