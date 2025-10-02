from ...NXOpen import *
from ..Fields import *

import typing
import enum

class VectorFieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def SetExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    def GetExpressionByIndex(self, index: int) -> Expression:
        ...
    def SetField(self, field: Fields.Field, scaleFactors: float) -> None:
        ...
    def GetField(self) -> Fields.Field:
        ...


class SpatialMapBuilder(Builder):
    def __init__(self) -> None: ...
    def AutoTolerance(self) -> None:
        ...
    def CreateLatticeMap(self, numOfLatticeColumn: int, numOfColumns: int, indepVarArray: typing.List[Fields.FieldVariable], datapoint: float, parameterizedDatapoints: float) -> Fields.SpatialMap:
        ...
    BoundedObjects: SelectNXObjectList
    BoundingBoxMap: Fields.SpatialMap.BoundingBoxMapEnum
    ConstUObjects: Fields.PathObjectsList
    ConstVObjects: Fields.PathObjectsList
    ConstantUObjects: SelectNXObjectList
    ConstantVObjects: SelectNXObjectList
    CoordSystem: CoordinateSystem
    FaceTolerance: Expression
    LatticePath: Fields.PathObjects
    MapSubtype: Fields.SpatialMap.SubtypeEnum
    MapSubtypeMapping: Fields.SpatialMap.SubtypeMappingEnum
    MapType: Fields.SpatialMap.TypeEnum
    MappingFaces: SelectNXObjectList
    OppositeCorner: Point
    Origin: Point
    ParametricPlaneMap: Fields.SpatialMap.ParametricPlaneMapEnum


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
    

    class ParametricPlaneMapEnum(enum.Enum):
        IsoSections = 0
        IsoLines = 1
        ImportedIsoLines = 2
    

    class BoundingBoxMapEnum(enum.Enum):
        OppositeCorner = 0
        Objects = 1
    

class ScalarFieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def SetExpression(self, expression: Expression) -> None:
        ...
    def GetExpression(self) -> Expression:
        ...
    def SetField(self, field: Fields.Field, scaleFactor: float) -> None:
        ...
    def GetField(self) -> Fields.Field:
        ...
    def GetFieldScaleFactor(self) -> float:
        ...


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
    def ReverseSectionDirection(self, index: int) -> None:
        ...
    def HandleLatestSelDirection(self) -> None:
        ...


class NameVariable(NXObject):
    def __init__(self) -> None: ...
    Measure: str
    Name: str


class ImportData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetFileName(self, fileName: str) -> None:
        ...
    def GetFileName(self) -> str:
        ...
    def GetFields(self, fields: typing.List[Fields.Field]) -> None:
        ...
    def GetMessages(self, messages: str) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class IApplicationData():
    def GetApplication(self) -> Fields.IApplication:
        ...


class IApplication(TaggedObject):
    def __init__(self) -> None: ...
    Name: str


class FieldWrapper(NXObject):
    def __init__(self) -> None: ...
    def SetField(self, field: Fields.Field) -> None:
        ...
    def GetField(self) -> Fields.Field:
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
    def SetInterpolation(self, interpolationMethod: int) -> None:
        """[Obsolete("Deprecated in NX7.5.2.  Use NXOpen.Fields.FieldTable.InterpolationMethod instead.")"""
        ...
    def GetIdwOptions(self, nearestOption: Fields.FieldEvaluator.InverseDistanceWeightingEnum, nearestFraction: float) -> None:
        ...
    def SetIdwOptions(self, nearestOption: Fields.FieldEvaluator.InverseDistanceWeightingEnum, nearestFraction: float) -> None:
        ...
    def LoadFromFile(self, filename: str, loadFileOption: Fields.FieldTable.LoadFileOption) -> None:
        ...
    def GetData(self, variable: Fields.FieldVariable) -> float:
        ...
    def EditTableVariables(self, indepVarArray: typing.List[Fields.FieldVariable], depExpArray: typing.List[Fields.FieldVariable]) -> None:
        ...
    AnnTolerance: float
    Discontinuities: bool
    IndependentValueDivisor: float
    IndependentValueDivisorOption: bool
    IndependentValueShift: float
    IndependentValueShiftOption: bool
    InterpolationMethod: Fields.FieldEvaluator.InterpolationEnum
    LatticeDataOption: bool
    LinearLogOption: Fields.FieldEvaluator.LinearLogOptionEnum
    NumLatticeDataColumn: int
    PersistentInterpolator: bool
    ValuesOutsideTableInterpolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum


    class LoadFileOption(enum.Enum):
        Append = 0
        Replace = 1
    

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
    

class FieldReference(Fields.Field):
    def __init__(self) -> None: ...
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolationMethod: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
        ...
    def GetSecondaryValuesOutsideTableInterpolation(self) -> Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        ...
    ValuesOutsideTableInterpolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum


class FieldProfileTable(Fields.FieldTable):
    def __init__(self) -> None: ...
    def SetUnitType(self, unitType: Unit) -> None:
        ...
    ChordalTolerance: Expression
    NumberPoints: int
    Offset: Expression
    SamplingPointType: Fields.FieldProfileTable.SamplingPointOption
    Scale: Expression
    Sketch: Sketch


    class SamplingPointOption(enum.Enum):
        ChordalTolerance = 0
        EqualArcLength = 1
    

class FieldManager(NXObject):
    def __init__(self) -> None: ...
    def CreateFieldExpression(self, fieldExpString: str, unitType: Unit) -> Fields.FieldExpression:
        ...
    def CreateFieldExpression(self, fieldExpString: str, unitType: Unit, indepVarArray: typing.List[Fields.FieldVariable]) -> Fields.FieldExpression:
        """[Obsolete("Deprecated in NX10.0.0.  Field expressions are owned by other objects.  They are managed by the creation and editing of the owning object and should not be created independently.")"""
        ...
    def CreateSubFieldExpression(self, depVar: Fields.FieldVariable) -> Fields.FieldExpression:
        ...
    def CreateFieldFormula(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depExpArray: typing.List[Fields.FieldExpression]) -> Fields.FieldFormula:
        ...
    def CreateFieldTable(self, fieldName: str, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float) -> Fields.FieldTable:
        ...
    def CreateFieldTableFromData(self, fieldNamePrefix: str, ivarUnit: Unit, dvarUnit: Unit, dvarType: Fields.FieldVariable.ValueType, datapoints: float) -> Fields.FieldTable:
        ...
    def CreateFieldLink(self, fieldName: str, fieldToLink: Fields.Field) -> Fields.FieldLink:
        ...
    def DeleteField(self, field: Fields.Field) -> Fields.Field:
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
    def CreateSpatialMapBuilder(self, spatialmap: Fields.SpatialMap) -> Fields.SpatialMapBuilder:
        ...
    def CreateExportData(self) -> Fields.ExportData:
        ...
    def ExportFields(self, exportData: Fields.ExportData) -> None:
        ...
    def CreateImportData(self) -> Fields.ImportData:
        ...
    def ImportFields(self, importData: Fields.ImportData) -> None:
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
    def CreateProfileField(self, fieldName: str, dependentUnit: Unit, sketch: Sketch, discreteType: int, numPoints: int, chordalTolerance: Expression, offset: Expression, scale: Expression, interpolationType: int) -> Fields.FieldProfileTable:
        ...
    def CreateProfileExternalTable(self, fieldName: str, filePath: str, nbAbscisae: int, xColumn: int, yColumn: int, ordinateColumn: int, xOffset: Expression, yOffset: Expression, ordinateOffset: Expression, xScale: Expression, yScale: Expression, ordinateScale: Expression, xCyclic: bool, yCyclic: bool, interpolation: Fields.FieldEvaluator.InterpolationEnum, xExtrapolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum, yExtrapolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum, slopeLeft: Expression, slopeRight: Expression) -> Fields.FieldReference:
        ...
    def EditProfileExternalTable(self, externalFileRefField: Fields.FieldReference, fieldName: str, filePath: str, nbAbscisae: int, xColumn: int, yColumn: int, ordinateColumn: int, xOffset: Expression, yOffset: Expression, ordinateOffset: Expression, xScale: Expression, yScale: Expression, ordinateScale: Expression, xCyclic: bool, yCyclic: bool, interpolation: Fields.FieldEvaluator.InterpolationEnum, xExtrapolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum, yExtrapolation: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum, slopeLeft: Expression, slopeRight: Expression) -> None:
        ...
    Domains: Fields.FieldDomainCollection
    Fields: Fields.FieldCollection


class FieldLinksTable(Fields.Field):
    def __init__(self) -> None: ...
    def EditFieldLinksTable(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field]) -> None:
        ...
    def EditFieldLinksTable(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable], datapoints: float, linkFieldsArray: typing.List[Fields.Field], managedFieldsArray: bool) -> None:
        ...
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolationMethod: Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
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
    def GetDependentExpressions(self) -> typing.List[Fields.FieldExpression]:
        ...
    def EditFieldFormulaVariables(self, indepVarArray: typing.List[Fields.FieldVariable], depVarArray: typing.List[Fields.FieldVariable]) -> None:
        ...


class FieldExpression(Fields.Field):
    def __init__(self) -> None: ...
    def EditFieldExpression(self, fieldExpString: str, unitType: Unit, indepVarArray: typing.List[Fields.FieldVariable], updateFlag: bool) -> None:
        ...
    def SetFieldExpressionString(self, fieldExpString: str, updateFlag: bool) -> None:
        ...
    def GetFieldExpressionString(self) -> str:
        ...


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
    

    class LinearLogOptionEnum(enum.Enum):
        LinearLinear = 0
        LogLinear = 1
        LinearLog = 2
        LogLog = 3
    

    class InverseDistanceWeightingEnum(enum.Enum):
        All = 0
        Radius = 1
        NearestPoints = 2
    

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
    

class FieldDrawHelper(TaggedObject):
    def __init__(self) -> None: ...
    def GetReloadResult(self) -> bool:
        ...
    def GetDrawSymbolsResult(self) -> bool:
        ...
    def GetDrawTableSymbolsResult(self) -> bool:
        ...
    def GetDrawContoursResult(self) -> bool:
        ...
    def GetDrawContoursWithEdgesResult(self) -> bool:
        ...
    def GetDrawAxesResult(self) -> bool:
        ...
    def GetDrawUserDefinedResolutionResult(self) -> bool:
        ...
    def GetDrawLegendResult(self) -> bool:
        ...
    def GetLegendTearDownResult(self) -> bool:
        ...
    def GetDrawAxesLabelsResult(self) -> bool:
        ...
    def GetDrawIndepDomainResult(self) -> bool:
        ...
    def GetDrawDefaultValueLabelsResult(self) -> bool:
        ...
    def GetDrawDescriptionResult(self) -> bool:
        ...
    def GetDrawNameResult(self) -> bool:
        ...
    def GetDrawValueLabelsResult(self) -> bool:
        ...
    def GetDrawTableValueLabelsResult(self) -> bool:
        ...
    def GetDrawUndefineSymbolValuesResult(self) -> bool:
        ...
    def GetDrawOverflowSymbolValuesResult(self) -> bool:
        ...
    def GetDrawUnderflowSymbolValuesResult(self) -> bool:
        ...
    def GetDrawUndefineContourValuesResult(self) -> bool:
        ...
    def GetDrawOverflowContourValuesResult(self) -> bool:
        ...
    def GetDrawUnderflowContourValuesResult(self) -> bool:
        ...


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
    def GetFieldDrawhelper(self) -> Fields.FieldDrawHelper:
        ...
    def SetPartContext(self) -> None:
        ...
    def CreateDrawHelper(self) -> Fields.FieldDrawHelper:
        ...
    def CopyToPart(self, targetPart: BasePart) -> None:
        """[Obsolete("Deprecated in NX6.0.1.  Use NXOpen.Fields.Field.CreateCopyInPart instead.")"""
        ...
    def CreateCopyInPart(self, targetPart: BasePart) -> Fields.Field:
        ...
    def CopyAsTableToPart(self, targetPart: BasePart) -> None:
        """[Obsolete("Deprecated in NX6.0.1.  Use NXOpen.Fields.Field.CreateTableInPart instead.")"""
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
    def GetApplicationData(self, applicationName: str) -> Fields.IApplicationData:
        ...
    def AddApplicationData(self, applicationData: Fields.IApplicationData) -> None:
        ...
    IsLocked: bool
    IsUserField: bool


class ExportData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def AddField(self, field: Fields.Field) -> None:
        ...
    def AddFields(self, fields: typing.List[Fields.Field]) -> None:
        ...
    def SetFileName(self, fileName: str) -> None:
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
    ShowUndefinedValues: Fields.DisplayPropertiesBuilder.ValuesEnum
    ShowUnderflowValues: bool
    SpectrumLevels: int
    SurfaceOffset: float
    TblDepColor: NXColor
    TblDepDomColor: Fields.DisplayPropertiesBuilder.DepDomColorEnum
    TblDepLabelValues: Fields.DisplayPropertiesBuilder.DepLabelValueEnum
    TblDepPtType: Fields.DisplayPropertiesBuilder.TblPointTypeEnum
    TblDepSymbolSize: float
    TblIndepColor: NXColor
    TblIndepPtType: Fields.DisplayPropertiesBuilder.ValuesEnum
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
    def SetExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    def GetExpressionByIndex(self, index: int) -> Expression:
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
    def SetField(self, field: Fields.Field) -> None:
        ...
    def GetField(self) -> Fields.Field:
        ...
    def SetFieldWithScaleFactor(self, field: Fields.Field, scaleFactor: float) -> None:
        ...


