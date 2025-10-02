from ...NXOpen import *
from ..Fields import *

import typing
import enum

class VectorFieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def GetExpressionByIndex(self, index: int) -> Expression:
        ...
    def SetExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    def SetField(self, field: Fields.Field, scaleFactors: float) -> None:
        ...
    def GetField(self) -> Fields.Field:
        ...


class TimeSeriesProfileBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetMeasureFixed(self, isMeasureFixed: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    def GetExternalFileReferenceAdapter(self, referenceObjectId: int) -> ExternalFileReferenceAdapter:
        ...
    def SetExternalFileReferenceAdapter(self, referenceObjectId: int, adapter: ExternalFileReferenceAdapter) -> None:
        ...
    def GetExternalFileDefinitionKey(self, adapter: ExternalFileReferenceAdapter) -> str:
        ...
    def EstablishReference(self, referenceObjectId: int, referenceType: ExternalFileReferenceAdapter.Type, externalFileSpec: str) -> ExternalFileReferenceAdapter:
        ...
    ChannelHasMeasureUnknown: bool
    ChannelName: str
    ExternalFile: str
    Interpolation: Fields.TimeSeriesProfileBuilder.InterpolationEnum
    Offset: Expression
    ScaleFactor: Expression
    TimeDelta: Expression
    UserDefinedUnitType: Unit


    class InterpolationEnum(enum.Enum):
        Linear = 0
        Akima = 1
        Akima72 = 2
        Cubic = 3
    

class SpatialMapBuilder(Builder):
    def __init__(self) -> None: ...
    def AutoTolerance(self) -> None:
        ...
    def CreateLatticeMap(self, numOfLatticeColumn: int, numOfColumns: int, indepVarArray: typing.List[Fields.FieldVariable], datapoint: float, parameterizedDatapoints: float) -> Fields.SpatialMap:
        ...
    def ResetMap(self, spatialMap: Fields.SpatialMap) -> None:
        ...
    def CreateSurfaceThroughPoints(self, locations: typing.List[Point3d], points: typing.List[Point], pointGroup: Group, feature: Features.FitSurface) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  This method will throw an error and should be replaced.  Use JA_SPATIAL_MAP_BUILDER_set_map_subtype to set subtype to JA_SPATIAL_MAP_subtype_enum_fit_surface.")"""
        ...
    def SetFitSurfaceOrientation(self, origin: Point3d, mtx: Matrix3x3) -> None:
        ...
    def GetBoundingBox(self) -> float:
        ...
    def SetBoundingBox(self, boundingbox: float) -> None:
        ...
    BoundedObjects: SelectNXObjectList
    BoundingBoxMap: Fields.SpatialMap.BoundingBoxMapEnum
    ConstUObjects: Fields.PathObjectsList
    ConstVObjects: Fields.PathObjectsList
    CoordSystem: CoordinateSystem
    EvaluationTolerance: Expression
    FaceTolerance: Expression
    FitSurfaceCoordinateSystem: CoordinateSystem
    FitSurfaceDirectionOption: Fields.SpatialMapBuilder.FitSurfaceDirectionType
    FitSurfaceUDegree: int
    FitSurfaceUPatches: int
    FitSurfaceVDegree: int
    FitSurfaceVPatches: int
    FitSurfaceVector: Direction
    LatticePath: Fields.PathObjects
    MapSubtype: Fields.SpatialMap.SubtypeEnum
    MapSubtypeMapping: Fields.SpatialMap.SubtypeMappingEnum
    MapType: Fields.SpatialMap.TypeEnum
    MappingFaces: SelectNXObjectList
    OppositeCorner: Point
    Origin: Point
    ParametricPlaneMap: Fields.SpatialMap.ParametricPlaneMapEnum


    class FitSurfaceDirectionType(enum.Enum):
        BestFit = 0
        Vector = 1
        Orientation = 2
        Csys = 3
    

class SpatialMap(NXObject):
    def __init__(self) -> None: ...


    class TypeEnum(enum.Enum):
        None = 0
        Global = 1
        Cartesian = 2
        Cylindrical = 3
        Spherical = 4
        ParametricSpace = 5
        ParametricPlane = 6
        ParametricLine = 7
        ImportedParametricLine = 8
    

    class SubtypeMappingEnum(enum.Enum):
        Faces = 0
        IsoSections = 1
        IsoLines = 2
    

    class SubtypeEnum(enum.Enum):
        None = 0
        Surface = 1
        FitSurface = 2
    

    class ParametricPlaneMapEnum(enum.Enum):
        IsoSections = 0
        IsoLines = 1
        ImportedIsoLines = 2
    

    class BoundingBoxMapEnum(enum.Enum):
        OppositeCorner = 0
        Objects = 1
    

class SketchProfileBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    ChordalTolerance: Expression
    DiscretePointType: Fields.FieldProfileTable.SamplingPointOption
    Interpolation: Fields.SketchProfileBuilder.InterpolationType
    NumberPoints: int
    Offset: Expression
    PointSamplingType: Fields.SketchProfileBuilder.SamplingPointType
    Points: PointList
    Scale: Expression
    Sketch: SelectSketch
    UnitType: Unit


    class SamplingPointType(enum.Enum):
        ChordalTolerance = 0
        EqualArcLength = 1
    

    class InterpolationType(enum.Enum):
        Linear = 0
        Akima = 1
        Akima72 = 2
        Cubic = 3
    

class ScalarFieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def SetExpression(self, expression: Expression) -> None:
        ...
    def GetExpression(self) -> Expression:
        ...
    def GetField(self) -> Fields.Field:
        ...
    def SetField(self, field: Fields.Field, scaleFactor: float) -> None:
        ...
    def GetFieldScaleFactor(self) -> float:
        ...


class ProfileSolverOptionsBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Cyclic: Fields.ProfileSolverOptionsBuilder.CyclicType
    SlopeLeft: Expression
    SlopeRight: Expression
    XExtrapolation: Fields.ProfileSolverOptionsBuilder.Extrapolation
    XInterpolation: Fields.ProfileSolverOptionsBuilder.Interpolation
    YExtrapolation: Fields.ProfileSolverOptionsBuilder.Extrapolation
    YInterpolation: Fields.ProfileSolverOptionsBuilder.Interpolation


    class Interpolation(enum.Enum):
        Linear = 0
        Akima = 1
        Akima72 = 2
        Cubic = 3
    

    class Extrapolation(enum.Enum):
        Linear = 0
        Parabolic = 1
        Cubic = 2
    

    class CyclicType(enum.Enum):
        None = 0
        XOnly = 1
        YOnly = 2
        Both = 3
    

class PathObjectsList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Fields.PathObjects]) -> None:
        ...
    def Append(self, object: Fields.PathObjects) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Fields.PathObjects) -> int:
        ...
    def FindItem(self, index: int) -> Fields.PathObjects:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Fields.PathObjects) -> None:
        ...
    def Erase(self, obj: Fields.PathObjects, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Fields.PathObjects]:
        ...
    def SetContents(self, objects: typing.List[Fields.PathObjects]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Fields.PathObjects, object2: Fields.PathObjects) -> None:
        ...
    def Insert(self, location: int, object: Fields.PathObjects) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PathObjects(SelectObjectList):
    def __init__(self) -> None: ...
    def ReverseDirection(self) -> None:
        ...
    def HandleLatestSelDirection(self) -> None:
        ...
    def ReverseSectionDirection(self, index: int) -> None:
        ...


class NameVariable(NXObject):
    def __init__(self) -> None: ...
    Measure: str
    Name: str


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class ManualInputProfileBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def SetDataPointValues(self, dataPoints: float) -> None:
        ...
    def SetDataPointExpressions(self, dataPointCellIds: int, dataPointExpressions: str) -> None:
        ...
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        ...
    def Validate(self) -> bool:
        ...
    Cyclic: Fields.ManualInputProfileBuilder.CyclicType
    OrdinateOffset: Expression
    OrdinateScale: Expression
    OrdinateUnitType: Unit
    SlopeLeft: Expression
    SlopeRight: Expression
    SolverOptions: Fields.ProfileSolverOptionsBuilder
    XExtrapolation: Fields.ManualInputProfileBuilder.Extrapolation
    XInterpolation: Fields.ManualInputProfileBuilder.Interpolation
    XOffset: Expression
    XScale: Expression
    XUnitType: Unit


    class Interpolation(enum.Enum):
        Linear = 0
        Akima = 1
        Akima72 = 2
        Cubic = 3
    

    class Extrapolation(enum.Enum):
        Linear = 0
        Parabolic = 1
    

    class CyclicType(enum.Enum):
        None = 0
        XOnly = 1
    

class ManualInputProfile(Fields.FieldTable):
    def __init__(self) -> None: ...


class ImportTableDataBuilder(Builder):
    def __init__(self) -> None: ...
    def RescanImportFile(self) -> None:
        ...
    def SetClearTableOnImport(self) -> None:
        ...
    CreateSpatialMap: bool
    DuplicateValues: Fields.FieldTable.DuplicateValueOption
    ImportFile: str
    IsStructDataFormat: bool
    NumStructDataColumns: int
    NumStructDataPlanes: int
    NumStructDataRows: int


class ImportData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetFileName(self, fileName: str) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Fields.ImportBuilder.  See documentation for equivalent methods.")"""
        ...
    def GetFileName(self) -> str:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Fields.ImportBuilder.  See documentation for equivalent methods.")"""
        ...
    def GetFields(self, fields: typing.List[Fields.Field]) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Fields.ImportBuilder.  See documentation for equivalent methods.")"""
        ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  No replacement.")"""
        ...
    def GetMessages(self, messages: str) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  No replacement.")"""
        ...


class ImportBuilder(Builder):
    def __init__(self) -> None: ...
    def SetImportAction(self, nthField: int, action: int) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Fields.ImportBuilder.SetNthImportAction instead.")"""
        ...
    def GetImportAction(self, nthField: int) -> int:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Fields.ImportBuilder.GetNthImportAction instead.")"""
        ...
    def GetNumFields(self) -> int:
        ...
    def SetNthImportAction(self, nthField: int, action: Fields.ImportBuilder.ActionType) -> None:
        ...
    def GetNthImportAction(self, nthField: int) -> Fields.ImportBuilder.ActionType:
        ...
    def GetNthFieldName(self, nthField: int) -> str:
        ...
    def GetNthConflictType(self, nthField: int) -> Fields.ImportBuilder.ConflictType:
        ...
    ConflictResolutionStrategy: Fields.ImportBuilder.ImportConflictStrategy
    FilterOptions: Fields.ImportBuilder.ImportFilter
    FilterString: str
    ImportField: Fields.Field
    ImportFile: str
    ImportFolders: bool
    PrependString: str


    class ImportFilter(enum.Enum):
        All = 0
        Formula = 1
        Table = 2
        LinkedField = 3
        TableofFields = 4
        FilterbyName = 5
        FilterbyDomain = 6
        FilterbyDependentVariableName = 7
        FilterbyIndependentVariableName = 8
    

    class ImportFieldStrategy(enum.Enum):
        Skip = 0
        RenameExisting = 1
        RenameImported = 2
        Replace = 3
        BackupReplace = 4
    

    class ImportConflictStrategy(enum.Enum):
        AppendtoImportedFieldName = 0
        PrependStringtoImportedFieldName = 1
        UserSpecifiedReplaceandorRename = 2
    

    class ConflictType(enum.Enum):
        NoConflict = 0
        NameOnlyConflict = 1
        NameOnlyConflictInUse = 2
        CompatibleVariableConflict = 3
        CompatibleVariableConflictInUse = 4
        IncompatibleVariableConflict = 5
        IncompatibleVariableConflictInUse = 6
    

    class ActionType(enum.Enum):
        Import = 0
        DontImport = 1
        ImportAppend = 2
        Replace = 3
        BackupAndReplace = 4
        ImportPrepend = 5
    

class IApplicationData():
    def GetApplication(self) -> Fields.IApplication:
        ...
    def DeleteApplicationData(self) -> None:
        ...
    def CopyToField(self, field: Fields.Field) -> None:
        ...


class IApplication(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


class FieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def GetField(self) -> Fields.Field:
        ...
    def SetField(self, field: Fields.Field) -> None:
        ...


class FieldVariable(NXObject):
    def __init__(self) -> None: ...
    DefaultValue: float
    Logarithmic: bool
    NameVariable: Fields.NameVariable
    NumPoints: int
    Units: Unit
    VariableBounds: Fields.FieldVariable.Bounds
    VariableType: Fields.FieldVariable.Type


    class ValueType(enum.Enum):
        Real = 0
        Imaginary = 1
        ComplexRealImaginary = 2
        ComplexMagnitudePhase = 3
        Complex = 4
        Integer = 5
    

    class Type(enum.Enum):
        Unknown = -1
        Independent = 0
        Dependent = 1
    

    class FieldVariableBounds():
        IsMinimumDefined: bool
        IsMinimumInclusive: bool
        MinimumValue: float
        IsMaximumDefined: bool
        IsMaximumInclusive: bool
        MaximumValue: float
        def ToString(self) -> str:
            ...
    

class FieldTable(Fields.Field):
    def __init__(self) -> None: ...
    def EditFieldTable(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float) -> None:
        ...
    def EditFieldTableComplexDisplay(self, indepVarArrayComplexDisplay: bool, depVarArrayComplexDisplay: bool) -> None:
        ...
    def EditFieldTableComplexUnits(self, depVarArrayComplexUnits: typing.List[Unit]) -> None:
        ...
    def GetIdwOptions(self, nearestOption: Fields.FieldEvaluator.InverseDistanceWeightingEnum, nearestFraction: float) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use the overloaded NXOpen.Fields.FieldTable.GetIdwOptions call")"""
        ...
    def GetIdwOptions(self, nearestOption: Fields.FieldEvaluator.InverseDistanceWeightingEnum, nearestFraction: float, maximumRadius: float, numberOfPoints: int, powerOfDistance: Fields.FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum) -> None:
        ...
    def SetIdwOptions(self, nearestOption: Fields.FieldEvaluator.InverseDistanceWeightingEnum, nearestFraction: float) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use the overloaded NXOpen.Fields.FieldTable.SetIdwOptions call")"""
        ...
    def SetIdwOptions(self, nearestOption: Fields.FieldEvaluator.InverseDistanceWeightingEnum, nearestFraction: float, maximumRadius: float, numberOfPoints: int, powerOfDistance: Fields.FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum) -> None:
        ...
    def LoadFromFile(self, filename: str, loadFileOption: Fields.FieldTable.LoadFileOption) -> None:
        ...
    def GetData(self, variable: Fields.FieldVariable) -> float:
        ...
    def EditTableVariables(self, indepVarArray: typing.List[Fields.FieldVariable], depExpArray: typing.List[Fields.FieldVariable]) -> None:
        ...
    def EditDbScaling(self, dbScaleFactor: float, dbRefValue: float, isDbScaling: bool) -> None:
        ...
    def CreateInterpolator(self) -> None:
        ...
    def ProcessPendingUpdate(self) -> None:
        ...
    def EditTableLatticeData(self, latticeType: Fields.FieldTable.StructDataTableType, numLatticeRows: int, numLatticeColumns: int, numLatticePlanes: int) -> None:
        ...
    def GetTablePoints(self, pointObjectRowIds: int, pointObjects: typing.List[Point]) -> None:
        ...
    def EditFieldTableWithPoints(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, pointObjectRowIds: int, pointObjects: typing.List[Point]) -> None:
        ...
    def EditFieldTableWithExpressions(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, expCellIds: int, valueStrings: str) -> None:
        ...
    def EditFieldTableWithExpressions(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, expCellIds: int, valueStrings: str, cellReadOnlys: bool) -> None:
        ...
    def XYGraph3DStructuredData(self, xAxisIndepVar: Fields.FieldVariable, zAxisIndepVar: Fields.FieldVariable, yAxisDepVar: Fields.FieldVariable, structuredDataPlaneIndex: int, windowDevice: int, viewIndex: int, overlay: bool, scaleFactor: float) -> CAE.Xyplot.Plot:
        ...
    def SetConservativeOptions(self, annTolerance: float, maximumRadius: float, numberOfPoints: int) -> None:
        ...
    def GetVariableScaleFactor(self, varType: Fields.FieldVariable.Type) -> Expression:
        ...
    def SetVariableScaleFactor(self, varType: Fields.FieldVariable.Type, scaleFactor: Expression) -> None:
        ...
    def GetVariableOffset(self, varType: Fields.FieldVariable.Type) -> Expression:
        ...
    def SetVariableOffset(self, varType: Fields.FieldVariable.Type, offset: Expression) -> None:
        ...
    AnnTolerance: float
    CreateInterpolatorOnCommit: bool
    DelaunayDeleteSlivers: bool
    DelaunayRatioTolerance: float
    DelaunaySliverDetectionMethod: Fields.FieldEvaluator.DelaunaySliverDetectionMethodEnum
    DelaunaySnapVertices: bool
    DelayedUpdate: bool
    Discontinuities: bool
    DuplicateValueProcessingOption: Fields.FieldTable.DuplicateValueOption
    FallbackToDefaultInterpolator: bool
    IndependentValueDivisor: float
    IndependentValueDivisorOption: bool
    IndependentValueShift: float
    IndependentValueShiftOption: bool
    InterpolationMethod: Fields.FieldEvaluator.InterpolationEnum
    LinearLogOption: Fields.FieldEvaluator.LinearLogOptionEnum
    ParameterizeIndependentDomain: bool
    PersistentInterpolator: bool
    ValuesOutsideHighTableUserdefinedValue: float
    ValuesOutsideTableInterpolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum
    ValuesOutsideTableUserdefinedValue: float


    class StructDataTableType(enum.Enum):
        Regular = 0
        Strict = 1
    

    class LoadFileOption(enum.Enum):
        Append = 0
        Replace = 1
    

    class DuplicateValueOption(enum.Enum):
        None = 0
        Average = 1
        Minimum = 2
        Maximum = 3
        First = 4
        Last = 5
        Skip = 6
    

    class DBFactor(enum.Enum):
        AcousticPowerDefault = 0
        AcousticPressureDefault = 1
    

class FieldReference(Fields.Field):
    def __init__(self) -> None: ...
    def GetSecondaryValuesOutsideTableInterpolation(self) -> Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        ...
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolMethod: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
        ...
    ValuesOutsideTableInterpolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum


class FieldProfileTable(Fields.FieldTable):
    def __init__(self) -> None: ...


    class SamplingPointOption(enum.Enum):
        ChordalTolerance = 0
        EqualArcLength = 1
    

class FieldManager(NXObject):
    def __init__(self) -> None: ...
    def CreateFieldExpression(self, fieldExpString: str, unitType: Unit) -> Fields.FieldExpression:
        ...
    def CreateSubFieldExpression(self, depVar: Fields.FieldVariable) -> Fields.FieldExpression:
        ...
    def CreateFieldFormula(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depExpArray: typing.List[Fields.FieldExpression]) -> Fields.FieldFormula:
        ...
    def CreateFieldTable(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float) -> Fields.FieldTable:
        ...
    def CreateFieldTable(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, duplicateValueProcessingOption: Fields.FieldTable.DuplicateValueOption) -> Fields.FieldTable:
        ...
    def CreateFieldTable(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, duplicateValueProcessingOption: Fields.FieldTable.DuplicateValueOption, structDataType: Fields.FieldTable.StructDataTableType, numStructDataRows: int, numStructDataColumns: int, numStructDataPlanes: int) -> Fields.FieldTable:
        ...
    def CreateFieldTableFromData(self, fieldNamePrefix: str, ivarUnit: Unit, dvarUnit: Unit, dvarType: Fields.FieldVariable.ValueType, datapoints: float) -> Fields.FieldTable:
        ...
    def CreateFieldLink(self, fieldName: str, fieldToLink: Fields.Field) -> Fields.FieldLink:
        ...
    def DeleteField(self, field: Fields.Field) -> Fields.Field:
        ...
    def DeleteFields(self, fields: typing.List[Fields.Field]) -> bool:
        ...
    def CreateIndependentVariable(self, ownerField: Fields.Field, nameVariable: Fields.NameVariable, unitType: Unit, minValueSet: bool, minValueInclusive: bool, minValue: float, maxValueSet: bool, maxValueInclusive: bool, maxValue: float, numPtsSet: bool, numPts: int, defaultValueSet: bool, defaultValue: float) -> Fields.FieldVariable:
        ...
    def CreateIndependentVariable(self, ownerField: Fields.Field, nameVariable: Fields.NameVariable, unitType: Unit, type: Fields.FieldVariable.ValueType, minValueSet: bool, minValueInclusive: bool, minValue: float, maxValueSet: bool, maxValueInclusive: bool, maxValue: float, numPtsSet: bool, numPts: int, defaultValueSet: bool, defaultValue: float) -> Fields.FieldVariable:
        ...
    def EditIndependentVariable(self, indepVar: Fields.FieldVariable, varName: str, unitType: Unit, minValueSet: bool, minValueInclusive: bool, minValue: float, maxValueSet: bool, maxValueInclusive: bool, maxValue: float, numPtsSet: bool, numPts: int, defaultValueSet: bool, defaultValue: float) -> None:
        ...
    def EditIndependentVariable(self, indepVar: Fields.FieldVariable, unitType: Unit) -> None:
        ...
    def CreateDependentVariable(self, ownerField: Fields.Field, nameVariable: Fields.NameVariable, unitType: Unit) -> Fields.FieldVariable:
        ...
    def CreateDependentVariable(self, ownerField: Fields.Field, nameVariable: Fields.NameVariable, unitType: Unit, type: Fields.FieldVariable.ValueType) -> Fields.FieldVariable:
        ...
    def EditDependentVariable(self, depVar: Fields.FieldVariable, varName: str, unitType: Unit) -> None:
        ...
    def EditDependentVariable(self, depVar: Fields.FieldVariable, unitType: Unit) -> None:
        ...
    def CreateFieldWrapper(self, field: Fields.Field) -> Fields.FieldWrapper:
        ...
    def CreateScalarFieldWrapperWithExpression(self, expression: Expression) -> Fields.ScalarFieldWrapper:
        ...
    def CreateScalarFieldWrapperWithField(self, field: Fields.Field, scaleFactor: float) -> Fields.ScalarFieldWrapper:
        ...
    def CreateVectorFieldWrapperWithExpressions(self, expressions: typing.List[Expression]) -> Fields.VectorFieldWrapper:
        ...
    def CreateVectorFieldWrapperWithField(self, field: Fields.Field, scaleFactors: float) -> Fields.VectorFieldWrapper:
        ...
    def CreateComplexScalarFieldWrapperWithExpressions(self, expressions: typing.List[Expression]) -> Fields.ComplexScalarFieldWrapper:
        ...
    def CreateComplexScalarFieldWrapperWithField(self, field: Fields.Field) -> Fields.ComplexScalarFieldWrapper:
        ...
    def CreateDisplayPropertiesBuilder(self, fieldArray: typing.List[Fields.Field]) -> Fields.DisplayPropertiesBuilder:
        ...
    def CreateGlobalSpatialMap(self) -> Fields.SpatialMap:
        ...
    def CreateSpatialMapBuilder(self, spatialmap: Fields.SpatialMap) -> Fields.SpatialMapBuilder:
        ...
    def CreateExportData(self) -> Fields.ExportData:
        ...
    def ExportFields(self, exportData: Fields.ExportData) -> None:
        ...
    def CreateImportData(self) -> Fields.ImportData:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Fields.ImportBuilder instead.")"""
        ...
    def CreateImportBuilder(self) -> Fields.ImportBuilder:
        ...
    def ImportFields(self, importData: Fields.ImportData) -> None:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Fields.ImportBuilder instead.")"""
        ...
    def CreatePathObjects(self) -> Fields.PathObjects:
        ...
    def GetNameVariable(self, variableName: str, measureName: str) -> Fields.NameVariable:
        ...
    def GetValidFieldId(self) -> int:
        ...
    def CreateFieldLinksTable(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field]) -> Fields.FieldLinksTable:
        ...
    def CreateFieldLinksTable(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field], managedFieldsArray: bool) -> Fields.FieldLinksTable:
        ...
    def CreateFieldLinksTableWithConstants(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field], managedFieldsArray: bool) -> Fields.FieldLinksTable:
        ...
    def CreateMeshSizeFieldData(self, elementSizeType: int, meshArray: typing.List[TaggedObject]) -> Fields.Field:
        ...
    def ConvertToLinksTable(self, table: Fields.FieldTable) -> Fields.FieldLinksTable:
        ...
    def CreateComplexScalarFieldWrapperWithFieldWithScaleFactor(self, field: Fields.Field, scaleFactor: float) -> Fields.ComplexScalarFieldWrapper:
        ...
    def CreateComplexVectorFieldWrapperWithExpressions(self, expressions: typing.List[Expression]) -> Fields.ComplexVectorFieldWrapper:
        ...
    def CreateComplexVectorFieldWrapperWithField(self, field: Fields.Field, scaleFactor: float) -> Fields.ComplexVectorFieldWrapper:
        ...
    def CreateImportTableDataBuilder(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable]) -> Fields.ImportTableDataBuilder:
        ...
    def SetUndefinedVariableValue(self, undefinedValue: float) -> None:
        ...
    def CreateImportTableDataBuilderFromTable(self, fieldTable: Fields.FieldTable) -> Fields.ImportTableDataBuilder:
        ...
    def CreateFieldTableWithPoints(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, duplicateValueProcessingOption: Fields.FieldTable.DuplicateValueOption, pointObjectRowIds: int, pointObjects: typing.List[Point]) -> Fields.FieldTable:
        ...
    def CreateFieldTableWithExpressions(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, dupValueProcessOption: Fields.FieldTable.DuplicateValueOption, expCellIds: int, valueStrings: str) -> Fields.FieldTable:
        ...
    def CreateFieldTableWithExpressions(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, dupValueProcessOption: Fields.FieldTable.DuplicateValueOption, expCellIds: int, valueStrings: str, cellReadOnlys: bool) -> Fields.FieldTable:
        ...
    def DeleteFolders(self, folders: typing.List[Fields.FieldFolder], survivingFields: typing.List[Fields.Field]) -> None:
        ...
    Domains: Fields.FieldDomainCollection
    Fields: Fields.FieldCollection
    FieldFolders: Fields.FieldFolderCollection


class FieldLinksTable(Fields.Field):
    def __init__(self) -> None: ...
    def EditFieldLinksTable(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field]) -> None:
        ...
    def EditFieldLinksTable(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field], managedFieldsArray: bool) -> None:
        ...
    def EditFieldLinksTableWithConstants(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field], managedFieldsArray: bool) -> None:
        ...
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolationMethod: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
        ...
    def GetPrimaryIndependentVariableScaleFactor(self) -> Expression:
        ...
    def SetPrimaryIndependentVariableScaleFactor(self, scaleFactor: Expression) -> None:
        ...
    def GetPrimaryIndependentVariableOffset(self) -> Expression:
        ...
    def SetPrimaryIndependentVariableOffset(self, offset: Expression) -> None:
        ...
    Discontinuities: bool
    ValuesOutsideTableInterpolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum


class FieldLink(Fields.Field):
    def __init__(self) -> None: ...
    def EditFieldLink(self, fieldToLink: Fields.Field) -> None:
        ...


class FieldFormula(Fields.Field):
    def __init__(self) -> None: ...
    def EditFieldFormula(self, indepVarArray: typing.List[Fields.FieldVariable], depExpArray: typing.List[Fields.FieldExpression]) -> None:
        ...
    def EditFieldFormulaVariables(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable]) -> None:
        ...
    def GetDependentExpressions(self) -> typing.List[Fields.FieldExpression]:
        ...
    CombineTable: Fields.FieldExpression.CombineTableOption


class FieldFolderCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Fields.FieldFolder]:
        ...
    def __init__(self, owner: Fields.FieldManager) -> None: ...
    def __init__(self) -> None: ...
    def CreateFolder(self, name: str, parent: Fields.FieldFolder) -> Fields.FieldFolder:
        ...
    def FindObject(self, journalIdentifier: str) -> Fields.FieldFolder:
        ...
    def Tag(self) -> Tag: ...



class FieldFolder(NXObject):
    def __init__(self) -> None: ...
    def AddSubfolder(self, subfolder: Fields.FieldFolder) -> None:
        ...
    def RemoveSubfolder(self, subfolder: Fields.FieldFolder) -> None:
        ...
    def AddField(self, field: Fields.Field) -> None:
        ...
    def RemoveField(self, field: Fields.Field) -> None:
        ...
    def GetParent(self) -> CAE.IFolder:
        ...
    def GetChildren(self) -> typing.List[CAE.IFolder]:
        ...
    def GetMembers(self) -> typing.List[NXObject]:
        ...
    Parent: Fields.FieldFolder


class FieldExpression(Fields.Field):
    def __init__(self) -> None: ...
    def EditFieldExpression(self, fieldExpString: str, unitType: Unit, indepVarArray: typing.List[Fields.FieldVariable], updateFlag: bool) -> None:
        ...
    def GetFieldExpressionString(self) -> str:
        ...
    def SetFieldExpressionString(self, fieldExpString: str, updateFlag: bool) -> None:
        ...
    CombineTable: Fields.FieldExpression.CombineTableOption
    FieldExpressionUnits: Unit


    class CombineTableOption(enum.Enum):
        Intersection = 0
        Union = 1
    

class FieldEvaluator(TaggedObject):
    def __init__(self) -> None: ...
    def GetDependentVariables(self) -> typing.List[Fields.FieldVariable]:
        ...
    def GetIndependentVariables(self) -> typing.List[Fields.FieldVariable]:
        ...
    def SetIndependentVariableValues(self, independentVariable: Fields.FieldVariable, values: float) -> None:
        ...
    def Evaluate(self, dependentVariable: Fields.FieldVariable) -> float:
        ...
    def Delete(self) -> None:
        ...
    InterpolationMethod: Fields.FieldEvaluator.InterpolationEnum


    class ValuesOutsideTableInterpolationEnum(enum.Enum):
        Undefined = 0
        Extrapolate = 1
        Constant = 2
        Linear = 3
        Parabolic = 4
        Cubic = 5
        Userdefined = 6
    

    class LinearLogOptionEnum(enum.Enum):
        LinearLinear = 0
        LogLinear = 1
        LinearLog = 2
        LogLog = 3
        ScaleOffset = 4
    

    class InverseDistanceWeightingPowerOfDistanceEnum(enum.Enum):
        One = 1
        Two = 2
        Three = 3
    

    class InverseDistanceWeightingEnum(enum.Enum):
        All = 0
        Radius = 1
        NearestPoints = 2
        NumNearestPoints = 3
        MaximumRadiusAndPoints = 4
    

    class InterpolationEnum(enum.Enum):
        None = 0
        Linear1d = 1
        NearestNeighbor1d = 2
        InverseDistanceWeighting1d = 3
        Delaunay2dFast = 4
        Delaunay2dMedium = 5
        Delaunay2dAccurate = 6
        NearestNeighbor2d = 7
        RenkaShepard2d = 8
        InverseDistanceWeighting2d = 9
        Delaunay3dFast = 10
        Delaunay3dMedium = 11
        Delaunay3dAccurate = 12
        NearestNeighbor3d = 13
        RenkaShepard3d = 14
        InverseDistanceWeighting3d = 15
        NearestNeighborNd = 16
        RenkaShepardNd = 17
        InverseDistanceWeightingNd = 18
        ApproxNearestNeighbor2d = 19
        ApproxNearestNeighbor3d = 20
        ApproxNearestNeighborNd = 21
        Akima1d = 22
        Akima721d = 23
        Cubic1d = 24
        Bilinear2d = 25
        Biakima2d = 26
        Biakima722d = 27
        Bicubic2d = 28
        AkimaLinear2d = 29
        Akima72Linear2d = 30
        CubicLinear2d = 31
        Conservative3d = 32
    

    class DelaunaySliverDetectionMethodEnum(enum.Enum):
        Edgelengthratio = 0
        Aspectratio = 1
    

class FieldDomainCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Fields.FieldDomain]:
        ...
    def __init__(self, owner: Fields.FieldManager) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class FieldDomain(NXObject):
    def __init__(self) -> None: ...


class FieldCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Fields.Field]:
        ...
    def __init__(self, owner: Fields.FieldManager) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class Field(DisplayableObject):
    def __init__(self) -> None: ...
    def GetFieldEvaluator(self) -> Fields.FieldEvaluator:
        ...
    def SetPartContext(self) -> None:
        ...
    def CreateCopyInPart(self, targetPart: BasePart) -> Fields.Field:
        ...
    def CreateTableInPart(self, targetPart: BasePart) -> Fields.FieldTable:
        ...
    def Rename(self, newName: str) -> None:
        ...
    def SetSpatialMap(self, overrideMap: Fields.SpatialMap) -> None:
        ...
    def GetSpatialMap(self) -> Fields.SpatialMap:
        ...
    def Delete(self) -> None:
        ...
    def XYGraph(self, indepVar: Fields.FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float) -> None:
        ...
    def XYGraph(self, indepVar: Fields.FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float, viewIndex: int, overlay: bool) -> None:
        ...
    def XYGraph(self, indepVar: Fields.FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float, windowDevice: int, viewIndex: int, overlay: bool) -> None:
        ...
    def XYGraph(self, indepVar: Fields.FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float, windowDevice: int, viewIndex: int, overlay: bool, plots: typing.List[CAE.Xyplot.Plot]) -> None:
        ...
    def XYGraph(self, indepVar: Fields.FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float, windowDevice: int, viewIndex: int, overlay: bool, scaleFactor: float, plots: typing.List[CAE.Xyplot.Plot]) -> None:
        ...
    def XYGraphPlotData(self, indepVar: Fields.FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float, windowDevice: int, viewIndex: int, overlay: bool, scaleFactor: float, plotOption: Fields.Field.PlotOption, plots: typing.List[CAE.Xyplot.Plot]) -> None:
        ...
    def XYGraphArgand(self, indepVar: Fields.FieldVariable, abscissaMinimum: float, abscissaMaximum: float, abscissaPointCount: int, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float, windowDevice: int, viewIndex: int, plots: typing.List[CAE.Xyplot.Plot]) -> None:
        ...
    def SetDescription(self, lines: str) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def SetIdLabel(self, idLabel: int) -> None:
        ...
    def GetIdLabel(self) -> int:
        ...
    def GetDependentVariables(self) -> typing.List[Fields.FieldVariable]:
        ...
    def GetIndependentVariables(self) -> typing.List[Fields.FieldVariable]:
        ...
    def XYGraph3D(self, xAxisIndepVar: Fields.FieldVariable, xAxisBndsMinimum: float, xAxisBndsMaximum: float, xAxisBndsSampleSize: int, zAxisIndepVar: Fields.FieldVariable, zAxisBndsMinimum: float, zAxisBndsMaximum: float, zAxisBndsSampleSize: int, yAxisDepVar: Fields.FieldVariable, constantIndepVarArray: typing.List[Fields.FieldVariable], constantIndepVarValueArray: float, interpolateTableData: bool, windowDevice: int, viewIndex: int, overlay: bool, scaleFactor: float) -> CAE.Xyplot.Plot:
        ...
    def AddApplicationData(self, appData: Fields.IApplicationData) -> None:
        ...
    def GetApplicationData(self, applicationName: str) -> Fields.IApplicationData:
        ...
    def Reload(self) -> None:
        ...
    def SetLocked(self, locked: bool) -> None:
        ...
    def GetFolder(self) -> Fields.FieldFolder:
        ...
    IsLocked: bool
    IsUserField: bool


    class PlotOption(enum.Enum):
        InterpolatedValues = 0
        InterpolatedValuesWithBounds = 1
        RawTableValues = 2
    

class ExternalFileProfileBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def GetNumberOfColumns(self) -> int:
        ...
    def GetColumnTitle(self, columnNumber: int) -> str:
        ...
    def GetColumnUnit(self, columnNumber: int) -> Unit:
        ...
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        ...
    def GetColumnMeasureName(self, columnNumber: int) -> str:
        ...
    def Validate(self) -> bool:
        ...
    def GetExternalFileReferenceAdapter(self, referenceObjectId: int) -> ExternalFileReferenceAdapter:
        ...
    def SetExternalFileReferenceAdapter(self, referenceObjectId: int, adapter: ExternalFileReferenceAdapter) -> None:
        ...
    def GetExternalFileDefinitionKey(self, adapter: ExternalFileReferenceAdapter) -> str:
        ...
    def EstablishReference(self, referenceObjectId: int, referenceType: ExternalFileReferenceAdapter.Type, externalFileSpec: str) -> ExternalFileReferenceAdapter:
        ...
    Cyclic: Fields.ExternalFileProfileBuilder.CyclicType
    Dimension: Fields.ExternalFileProfileBuilder.DimensionChoice
    FormatControlOption: Fields.ExternalFileProfileBuilder.FormatOptions
    OrdinateColumn: int
    OrdinateOffset: Expression
    OrdinateScale: Expression
    SlopeLeft: Expression
    SlopeRight: Expression
    SolverOptions: Fields.ProfileSolverOptionsBuilder
    XColumn: int
    XExtrapolation: Fields.ExternalFileProfileBuilder.Extrapolation
    XInterpolation: Fields.ExternalFileProfileBuilder.Interpolation
    XOffset: Expression
    XScale: Expression
    YColumn: int
    YExtrapolation: Fields.ExternalFileProfileBuilder.Extrapolation
    YInterpolation: Fields.ExternalFileProfileBuilder.Interpolation
    YOffset: Expression
    YScale: Expression


    class Interpolation(enum.Enum):
        Linear = 0
        Akima = 1
        Akima72 = 2
        Cubic = 3
    

    class FormatOptions(enum.Enum):
        ComputerRegionalSettings = 0
        DotDecimalSeparator = 1
        CommaDecimalSeparator = 2
        DotDecimalSeparatorAndCommaValueDelimiter = 3
        CommaDecimalSeparatorAndSemicolonValueDelimiter = 4
    

    class Extrapolation(enum.Enum):
        Linear = 0
        Parabolic = 1
        Cubic = 2
    

    class DimensionChoice(enum.Enum):
        Curve = 0
        Surface = 1
        Any = 2
    

    class CyclicType(enum.Enum):
        None = 0
        XOnly = 1
        YOnly = 2
        Both = 3
    

class ExportData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AddField(self, field: Fields.Field) -> None:
        ...
    def SetFileName(self, fileName: str) -> None:
        ...
    def AddFields(self, fields: typing.List[Fields.Field]) -> None:
        ...
    def GetFields(self, fields: typing.List[Fields.Field]) -> None:
        ...
    def GetFileName(self) -> str:
        ...
    def FreeResource(self) -> None:
        ...


class DisplayPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    AxisColor: NXColor
    BasicColor: NXColor
    DepCalcSymblSize: float
    DepDispType: Fields.DisplayPropertiesBuilder.DepDispTypeEnum
    DepDomColor: Fields.DisplayPropertiesBuilder.DepDomColorEnum
    DepLabelValues: Fields.DisplayPropertiesBuilder.DepLabelValueEnum
    DepRangeMax: float
    DepRangeMin: float
    DepSelColor: NXColor
    DepSymbolSize: float
    DisplayResolution: Fields.DisplayPropertiesBuilder.DispResolutionEnum
    DummyScale: float
    FaceAnalysis: bool
    FieldQuantity: Fields.DisplayPropertiesBuilder.FieldQuantityType
    HeteroTblDispOption: Fields.DisplayPropertiesBuilder.HeteroTblDispOptionEnum
    IndepDispType: Fields.DisplayPropertiesBuilder.IndepDomDispType
    LabelColor: NXColor
    Layer: int
    LegendPosition: Fields.DisplayPropertiesBuilder.LegendPos
    LineFont: Fields.DisplayPropertiesBuilder.LineFontEnum
    LineWidth: Fields.DisplayPropertiesBuilder.LineWidthEnum
    OverflowColor: NXColor
    PartiallyShaded: bool
    PrimaryVar: Expression
    Range: Fields.DisplayPropertiesBuilder.ValueRange
    RangeMax: float
    RangeMin: float
    ShowAxis: bool
    ShowDefaultVal: bool
    ShowDescription: bool
    ShowLabels: bool
    ShowMapTopo: bool
    ShowName: bool
    ShowOverflowValues: bool
    ShowSrcTblVals: bool
    ShowUndefValues: bool
    ShowUnderflowValues: bool
    SpectrumLevels: int
    SurfaceOffset: float
    TblDepColor: NXColor
    TblDepDispType: Fields.DisplayPropertiesBuilder.DepDispTypeEnum
    TblDepDomColor: Fields.DisplayPropertiesBuilder.DepDomColorEnum
    TblDepLabelValues: Fields.DisplayPropertiesBuilder.DepLabelValueEnum
    TblDepPtType: Fields.DisplayPropertiesBuilder.TblPointTypeEnum
    TblDepSymbolSize: float
    TblHetPrimaryValue: float
    TblIndepColor: NXColor
    TblIndepPtType: Fields.DisplayPropertiesBuilder.ValuesEnum
    TblSurfaceOffset: float
    Translucency: int
    UndefValueColor: NXColor
    UnderflowColor: NXColor
    XMax: Expression
    XMin: Expression
    XNum: int
    YMax: Expression
    YMin: Expression
    YNum: int
    ZMax: Expression
    ZMin: Expression
    ZNum: int


    class VectorType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
        Mag = 3
    

    class ValuesEnum(enum.Enum):
        Hide = 0
        Point = 1
        PlusSign = 2
        Asterisk = 3
        Circle = 4
        PoundSign = 5
        Cross = 6
        Square = 7
        Triangle = 8
        Diamond = 9
        Centerline = 10
    

    class ValueRange(enum.Enum):
        Auto = 0
        Specified = 1
    

    class TensorType(enum.Enum):
        Xx = 0
        Yy = 1
        Zz = 2
        Xy = 3
        Yz = 4
        Zx = 5
        Mean = 6
        MidPrncpl = 7
        MinPrncpl = 8
        MaxPrncpl = 9
        Octahedral = 10
        VonMises = 11
    

    class TblPointTypeEnum(enum.Enum):
        Hide = 0
        Show = 1
    

    class ScalarType(enum.Enum):
        Hide = 0
        Mag = 1
    

    class LineWidthEnum(enum.Enum):
        Normal = 0
        Thick = 1
        Thin = 2
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class LineFontEnum(enum.Enum):
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
    

    class LegendPos(enum.Enum):
        Hide = 0
        Left = 1
        Right = 2
    

    class Legacy3DType(enum.Enum):
        X = 0
        Y = 1
        Z = 2
    

    class IndepDomDispType(enum.Enum):
        Normal = 0
        Point = 1
        PlusSign = 2
        Asterisk = 3
        Circle = 4
        PoundSign = 5
        Cross = 6
        Square = 7
        Triangle = 8
        Diamond = 9
        Centerline = 10
        Hide = 11
    

    class HeteroTblDispOptionEnum(enum.Enum):
        ShowAverageValue = 0
        PrimaryVarValues = 1
        Show1StValue = 2
        ShowLastValue = 3
        ShowMinimumValue = 4
        ShowMaximumValue = 5
        Hide = 6
    

    class FieldQuantityType(enum.Enum):
        Type0 = 0
        Type1 = 1
        Type2 = 2
        Type3 = 3
        Type4 = 4
        Type5 = 5
        Type6 = 6
        Type7 = 7
        Type8 = 8
        Type9 = 9
        Type10 = 10
        Type11 = 11
        Type12 = 12
        Type13 = 13
        Type14 = 14
        Type15 = 15
    

    class DispResolutionEnum(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        ExtraFine = 3
        SuperFine = 4
        UltraFine = 5
        UserSpecified = 6
    

    class DepLabelValueEnum(enum.Enum):
        None = 0
        MinimumMaximum = 1
        Maximum = 2
        Minimum = 3
        All = 4
    

    class DepDomColorEnum(enum.Enum):
        Inherit = 0
        Specified = 1
        Spectrum = 2
    

    class DepDispTypeEnum(enum.Enum):
        Symbol = 0
        Surface = 1
        SurfaceEdges = 2
        Hide = 3
    

    class ComplexVectorType(enum.Enum):
        XReal = 0
        YReal = 1
        ZReal = 2
        XImaginary = 3
        YImaginary = 4
        ZImaginary = 5
    

    class ComplexScalarType(enum.Enum):
        Mag = 0
        Real = 1
        Imaginary = 2
        Phase = 3
    

    class BalStrainType(enum.Enum):
        Xx = 0
        Yy = 1
        Zz = 2
        Xy = 3
        Yz = 4
        Zx = 5
        OffSetXX = 6
        OffSetYY = 7
        OffSetZZ = 8
        OffSetXY = 9
        OffSetYZ = 10
        OffSetZX = 11
    

class ComplexVectorFieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def GetExpressionByIndex(self, index: int) -> Expression:
        ...
    def SetExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    def SetImaginaryExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    def GetImaginaryExpressionByIndex(self, index: int) -> Expression:
        ...
    def SetField(self, field: Fields.Field, scaleFactor: float) -> None:
        ...
    def GetField(self) -> Fields.Field:
        ...


class ComplexScalarFieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def SetExpression(self, expression: Expression) -> None:
        ...
    def GetExpression(self) -> Expression:
        ...
    def SetImaginaryExpression(self, expression: Expression) -> None:
        ...
    def GetImaginaryExpression(self) -> Expression:
        ...
    def GetField(self) -> Fields.Field:
        ...
    def SetField(self, field: Fields.Field) -> None:
        ...
    def SetFieldWithScaleFactor(self, field: Fields.Field, scaleFactor: float) -> None:
        ...


