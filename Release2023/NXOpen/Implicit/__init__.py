from ...NXOpen import *
from ..Implicit import *

import typing
import enum

class UniteBuilder(Implicit.BooleanBuilder):
    def __init__(self) -> None: ...


class Unite(Implicit.Boolean):
    def __init__(self) -> None: ...


class TorusBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    CenterAndOrientation: CartesianCoordinateSystem
    InnerDimension: Expression
    OuterDimension: Expression


class Torus(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class ThickenBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    FacesToThicken: ScCollector
    Thickness: Expression
    ThicknessMethod: Implicit.ThickenBuilder.ThicknessMethodType
    VariableThicknessList: ModlUtils.SelectObjectDimList


    class ThicknessMethodType(enum.Enum):
        Constant = 0
        Variable = 1
    

class Thicken(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class SubtractBuilder(Implicit.BooleanBuilder):
    def __init__(self) -> None: ...


class Subtract(Implicit.Boolean):
    def __init__(self) -> None: ...


class SplitP(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class SphereBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    AssociativeOrigin: bool
    CenterPoint: Point
    Diameter: Expression


class Sphere(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class ShellBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    AlternateThicknessList: ExpressionCollectorSetList
    BodyToOffset: ScCollector
    DefaultThicknessDirectionReversed: bool
    FacesToOpen: ScCollector
    Thickness: Expression
    TypeOfShell: Implicit.ShellBuilder.Type


    class Type(enum.Enum):
        Closed = 0
        Open = 1
    

class Shell(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class Schwarz(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class Schoen(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class Scherk(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class OperationBuilder(Builder):
    def __init__(self) -> None: ...
    DisplayVoxel: bool
    UpdateDefaultVoxelSizeBasedOnFirstOperation: bool
    VoxelSizePercent: Expression


class OffsetBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    BodyToOffset: ScCollector
    DefaultThicknessDirectionReversed: bool
    Thickness: Expression


class Offset(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class Neovius(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class Lidinoid(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class IntersectBuilder(Implicit.BooleanBuilder):
    def __init__(self) -> None: ...


class Intersect(Implicit.Boolean):
    def __init__(self) -> None: ...


class ImportSolidBodyBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    BodiesOrFacesToImport: ScCollector
    BodiesToImport: ScCollector
    HideInputBody: bool


class ImportSolidBody(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class ImplicitOperationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Implicit.ImplicitOperation]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateImplicitModelingPreferencesBuilder(self, implicitFeature: Features.Feature) -> Implicit.ImplicitModelingPreferencesBuilder:
        ...
    def CreateEquationOperationBuilder(self, implicitOperation: Implicit.EquationOperation) -> Implicit.EquationOperationBuilder:
        ...
    def CreateImportSoildBodyBuilder(self, implicitOperation: Implicit.ImportSolidBody) -> Implicit.ImportSolidBodyBuilder:
        ...
    def CreateBlockBuilder(self, implicitOperation: Implicit.Block) -> Implicit.BlockBuilder:
        ...
    def CreateSphereBuilder(self, implicitOperation: Implicit.Sphere) -> Implicit.SphereBuilder:
        ...
    def CreateTorusBuilder(self, implicitOperation: Implicit.Torus) -> Implicit.TorusBuilder:
        ...
    def CreateEllipsoidBuilder(self, implicitOperation: Implicit.Ellipsoid) -> Implicit.EllipsoidBuilder:
        ...
    def CreateGeneralEquationOperationBuilder(self, implicitOperation: Implicit.GeneralEquationOperation) -> Implicit.GeneralEquationOperationBuilder:
        ...
    def CreateCylinderBuilder(self, implicitOperation: Implicit.Cylinder) -> Implicit.CylinderBuilder:
        ...
    def CreateConeBuilder(self, implicitOperation: Implicit.Cone) -> Implicit.ConeBuilder:
        ...
    def CreateShellBuilder(self, implicitOperation: Implicit.Shell) -> Implicit.ShellBuilder:
        ...
    def CreateIntersectBuilder(self, implicitOperation: Implicit.Intersect) -> Implicit.IntersectBuilder:
        ...
    def CreateSubtractBuilder(self, implicitOperation: Implicit.Subtract) -> Implicit.SubtractBuilder:
        ...
    def CreateUniteBuilder(self, implicitOperation: Implicit.Unite) -> Implicit.UniteBuilder:
        ...
    def CreateThickenBuilder(self, implicitOperation: Implicit.Thicken) -> Implicit.ThickenBuilder:
        ...
    def CreateCartesianPatternBuilder(self, implicitOperation: Implicit.CartesianPattern) -> Implicit.CartesianPatternBuilder:
        ...
    def CreateCylindricalPatternBuilder(self, implicitOperation: Implicit.CylindricalPattern) -> Implicit.CylindricalPatternBuilder:
        ...
    def Tag(self) -> Tag: ...



class ImplicitOperation(NXObject):
    def __init__(self) -> None: ...
    def GetParents(self) -> typing.List[Implicit.ImplicitOperation]:
        ...
    def GetExpressions(self) -> typing.List[Expression]:
        ...
    Timestamp: int


class ImplicitModelingPreferencesBuilder(Builder):
    def __init__(self) -> None: ...
    ChordalTolerance: float
    MaxFacetSize: Expression
    RemeshFlag: bool
    VoxelSize: Expression


class Gyroid(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class GeneralEquationOperationBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    BoundaryBody: ScCollector
    BoundaryOption: Implicit.GeneralEquationOperationBuilder.BoundaryOptionsEnum
    LocationAndOrientation: CoordinateSystem
    SizeX: Expression
    SizeY: Expression
    SizeZ: Expression
    Thickness: Expression
    ThicknessFactor: Expression
    ThicknessMethod: Implicit.GeneralEquationOperationBuilder.ThicknessMethodType
    UniformRange: bool
    UniformSize: Expression
    UserExpression: ModlUtils.EquationEditorBuilder


    class ThicknessMethodType(enum.Enum):
        Absolute = 0
        Relative = 1
    

    class BoundaryOptionsEnum(enum.Enum):
        CartesianRange = 0
        BoundaryBody = 1
    

class GeneralEquationOperation(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class EquationOperationBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    BlendFactor: int
    BoundaryBody: ScCollector
    BoundaryConditionOption: Implicit.EquationOperationBuilder.BoundaryConditionOptionType
    EdgeLength: Expression
    KFactor: float
    LocationAndOrientation: CoordinateSystem
    SizeX: Expression
    SizeY: Expression
    SizeZ: Expression
    Thickness: Expression
    ThicknessFactor: Expression
    ThicknessField: Fields.ScalarFieldWrapper
    ThicknessMethod: Implicit.EquationOperationBuilder.ThicknessMethodType
    TypeOfEquation: Implicit.EquationOperationBuilder.EquationType
    UniformCubeFlag: bool
    VariableThicknessList: ModlUtils.SelectObjectDimList


    class ThicknessMethodType(enum.Enum):
        Absolute = 0
        AbsoluteVariable = 1
        Relative = 2
    

    class EquationType(enum.Enum):
        Gyroid = 0
        Schwarz = 1
        Diamond = 2
        Neovius = 3
        Schoen = 4
        Scherk = 5
        Lidinoid = 6
        SplitP = 7
    

    class BoundaryConditionOptionType(enum.Enum):
        SolidVolume = 0
        VoidVolume = 1
        VoidVolumeAndUnite = 2
    

class EquationOperation(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class EllipsoidBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    CenterAndOrientation: CartesianCoordinateSystem
    Height: Expression
    Length: Expression
    Width: Expression


class Ellipsoid(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class Diamond(Implicit.EquationOperation):
    def __init__(self) -> None: ...


class CylindricalPatternBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    CenterAndOrientation: CartesianCoordinateSystem
    Diameter: Expression
    Height: Expression
    NumberOfCellsAroundCircumference: int
    NumberOfRadialLayers: int
    UnitCellBody: ScCollector


class CylindricalPattern(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class CylinderBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    CenterAndOrientation: CartesianCoordinateSystem
    Diameter: Expression
    Height: Expression


class Cylinder(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class ConeBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    BaseDiameter: Expression
    CenterAndOrientation: CartesianCoordinateSystem
    Height: Expression
    TopDiameter: Expression


class Cone(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class CartesianPatternBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    BlendFactor: int
    BoundaryBody: ScCollector
    BoundaryConditionOption: Implicit.CartesianPatternBuilder.BoundaryConditionOptionType
    EdgeLength: Expression
    LocationAndOrientation: CoordinateSystem
    SizeX: Expression
    SizeY: Expression
    SizeZ: Expression
    UniformCubeFlag: bool
    UnitCellBody: ScCollector


    class BoundaryConditionOptionType(enum.Enum):
        SolidVolume = 0
        VoidVolume = 1
        VoidVolumeAndUnite = 2
    

class CartesianPattern(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class BooleanBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    BlendFactor: int
    CreateBlends: bool
    KeepTarget: bool
    KeepTool: bool
    TargetBody: ScCollector
    ToolBody: ScCollector


class Boolean(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


class BlockBuilder(Implicit.OperationBuilder):
    def __init__(self) -> None: ...
    Associative: bool
    Height: Expression
    Length: Expression
    OriginAndOrientation: CartesianCoordinateSystem
    Width: Expression


class Block(Implicit.ImplicitOperation):
    def __init__(self) -> None: ...


