from ...NXOpen import *
from ..Optimization import *

import typing
import enum

class OptimizationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Optimization.OptimizationBuilder]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateOptimizationBuilder(self) -> Optimization.OptimizationBuilder:
        ...
    def CreateOptimizationAttributeBuilder(self) -> Optimization.OptimizationAttributeBuilder:
        ...
    def CreateMapleExpBuilder(self) -> Optimization.MapleExpBuilder:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.Optimization.OptimizationCollection.CreateMathIntegrationExpBuilder instead.")"""
        ...
    def CreateMathIntegrationExpBuilder(self) -> Optimization.MathIntegrationExpBuilder:
        ...
    def Tag(self) -> Tag: ...



class OptimizationBuilder(Builder):
    def __init__(self) -> None: ...
    def RunOptimization(self) -> None:
        ...
    def GetOptimizationObjectives(self) -> typing.List[Optimization.OptimizationBuilder.OptimizationObjective]:
        ...
    def SetOptimizationObjectives(self, attributeNames: str, attributeObjects: typing.List[NXObject], objectiveTypes: typing.List[Optimization.OptimizationBuilder.OptimizationAttributeType], objectiveTargetValues: float) -> None:
        ...
    def GetOptimizationVariables(self) -> typing.List[Optimization.OptimizationBuilder.OptimizationVariable]:
        ...
    def SetOptimizationVariables(self, attributeNames: str, attributeObjects: typing.List[NXObject], variableTypes: typing.List[Optimization.OptimizationBuilder.OptimizationAttributeType], variableLowerLimitValue: float, variableUpperLimitValue: float) -> None:
        ...
    def GetOptimizationConstraints(self) -> typing.List[Optimization.OptimizationBuilder.OptimizationConstraint]:
        ...
    def SetOptimizationConstraints(self, attributeNames: str, attributeObjects: typing.List[NXObject], constraintTypes: typing.List[Optimization.OptimizationBuilder.OptimizationAttributeType], constraintLowerLimitValue: float, constraintUpperLimitValue: float, constraintLimitType: typing.List[Optimization.OptimizationBuilder.OptimizationConstraintLimitType]) -> None:
        ...
    def BuildAllObjectives(self) -> None:
        ...
    def RemoveAllObjectives(self) -> None:
        ...
    def BuildAllVariables(self) -> None:
        ...
    def RemoveAllVariables(self) -> None:
        ...
    def BuildAllConstraints(self) -> None:
        ...
    def RemoveAllConstraints(self) -> None:
        ...
    AbsoluteConvergenceCriteria: float
    AlgorithmType: Optimization.OptimizationBuilder.OptimizationAlgorithmType
    ConvergenceSpeedType: Optimization.OptimizationBuilder.OptimizationConvergenceSpeedType
    IsShowGraph: bool
    IsUpdateDisp: bool
    MaxNumberIteration: int
    MaxTime: int
    OptimizationType: Optimization.OptimizationBuilder.OptimizationTargetType
    RelativeConvergenceCriteria: float
    StudyName: str


    class OptimizationBuilderOptimizationVariable():
        AttributeName: str
        AttributeObject: NXObject
        VariableType: Optimization.OptimizationBuilder.OptimizationAttributeType
        VariableLowerLimitValue: float
        VariableUpperLimitValue: float
        def ToString(self) -> str:
            ...
    

    class OptimizationTargetType(enum.Enum):
        Minimum = 0
        Maximum = 1
        Target = 2
    

    class OptimizationBuilderOptimizationObjective():
        AttributeName: str
        AttributeObject: NXObject
        ObjectiveType: Optimization.OptimizationBuilder.OptimizationAttributeType
        ObjectiveTargetValue: float
        def ToString(self) -> str:
            ...
    

    class OptimizationConvergenceSpeedType(enum.Enum):
        Slow = 0
        Medium = 1
        Fast = 2
        Infinite = 3
    

    class OptimizationConstraintLimitType(enum.Enum):
        Upper = 0
        Lower = 1
    

    class OptimizationBuilderOptimizationConstraint():
        AttributeName: str
        AttributeObject: NXObject
        ConstraintType: Optimization.OptimizationBuilder.OptimizationAttributeType
        ConstraintLowerLimitValue: float
        ConstraintUpperLimitValue: float
        ConstraintLimitType: Optimization.OptimizationBuilder.OptimizationConstraintLimitType
        def ToString(self) -> str:
            ...
    

    class OptimizationAttributeType(enum.Enum):
        Expression = 0
        KFAttribute = 1
        GeometryParameter = 2
    

    class OptimizationAlgorithmType(enum.Enum):
        SimulatedAnnealing = 0
        GlobalSimplex = 1
        Powell = 2
        ConjugateGradient = 3
        Lexicographic = 4
        PatternSwarm = 5
    

    class OptimizationBuilder_OptimizationVariable():
        attributeName: int
        attributeObject: Tag
        variableType: Optimization.OptimizationBuilder.OptimizationAttributeType
        variableLowerLimitValue: float
        variableUpperLimitValue: float
    

    class OptimizationBuilder_OptimizationObjective():
        attributeName: int
        attributeObject: Tag
        objectiveType: Optimization.OptimizationBuilder.OptimizationAttributeType
        objectiveTargetValue: float
    

    class OptimizationBuilder_OptimizationConstraint():
        attributeName: int
        attributeObject: Tag
        constraintType: Optimization.OptimizationBuilder.OptimizationAttributeType
        constraintLowerLimitValue: float
        constraintUpperLimitValue: float
        constraintLimitType: Optimization.OptimizationBuilder.OptimizationConstraintLimitType
    

class OptimizationAttributeBuilder(Builder):
    def __init__(self) -> None: ...
    def AdoptObject(self, object: NXObject) -> None:
        ...


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MathIntegrationExpBuilder(Builder):
    def __init__(self) -> None: ...


class MapleExpBuilder(Builder):
    def __init__(self) -> None: ...


class DesignStudyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Optimization.DesignStudyBuilder]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateDesignStudyBuilder(self) -> Optimization.DesignStudyBuilder:
        ...
    def CreateDesignStudyAttributeBuilder(self) -> Optimization.DesignStudyAttributeBuilder:
        ...
    def Tag(self) -> Tag: ...



class DesignStudyBuilder(Builder):
    def __init__(self) -> None: ...
    def RunDesignStudy(self) -> None:
        ...
    def GetDesignStudyObjectives(self) -> typing.List[Optimization.DesignStudyBuilder.DesignStudyObjective]:
        ...
    def SetDesignStudyObjectives(self, attributeNames: str, attributeObjects: typing.List[NXObject], objectiveTypes: typing.List[Optimization.DesignStudyBuilder.DesignStudyAttributeType], warningLowerLimit: float, warningUpperLimit: float, failureLowerLimit: float, failureUpperLimit: float) -> None:
        ...
    def GetDesignStudyVariables(self) -> typing.List[Optimization.DesignStudyBuilder.DesignStudyVariable]:
        ...
    def SetDesignStudyVariables(self, attributeNames: str, attributeObjects: typing.List[NXObject], variableTypes: typing.List[Optimization.DesignStudyBuilder.DesignStudyAttributeType], variableLowerLimitValue: float, variableUpperLimitValue: float, distributeType: typing.List[Optimization.DesignStudyBuilder.DesignStudyDistributeType], locationParameter: float, scaleParameter: float, shapeParameter: float, valuesCount: int) -> None:
        ...
    def BuildAllObjectives(self) -> None:
        ...
    def RemoveAllObjectives(self) -> None:
        ...
    def BuildAllVariables(self) -> None:
        ...
    def RemoveAllVariables(self) -> None:
        ...
    IsShowGraph: bool
    IsUpdateDisp: bool
    StudyName: str


    class DesignStudyBuilderDesignStudyVariable():
        AttributeName: str
        AttributeObject: NXObject
        VariableType: Optimization.DesignStudyBuilder.DesignStudyAttributeType
        VariableLowerLimitValue: float
        VariableUpperLimitValue: float
        DistributeType: Optimization.DesignStudyBuilder.DesignStudyDistributeType
        LocationParameter: float
        ScaleParameter: float
        ShapeParameter: float
        ValuesCount: int
        def ToString(self) -> str:
            ...
    

    class DesignStudyBuilderDesignStudyObjective():
        AttributeName: str
        AttributeObject: NXObject
        ObjectiveType: Optimization.DesignStudyBuilder.DesignStudyAttributeType
        WarningLowerLimit: float
        WarningUpperLimit: float
        FailureLowerLimit: float
        FailureUpperLimit: float
        def ToString(self) -> str:
            ...
    

    class DesignStudyDistributeType(enum.Enum):
        Uniform = 0
        Normal = 1
        Gamma = 2
    

    class DesignStudyConstraintLimitType(enum.Enum):
        Upper = 0
        Lower = 1
    

    class DesignStudyAttributeType(enum.Enum):
        Expression = 0
        KFAttribute = 1
        GeometryParameter = 2
    

    class DesignStudyBuilder_DesignStudyVariable():
        attributeName: int
        attributeObject: Tag
        variableType: Optimization.DesignStudyBuilder.DesignStudyAttributeType
        variableLowerLimitValue: float
        variableUpperLimitValue: float
        distributeType: Optimization.DesignStudyBuilder.DesignStudyDistributeType
        locationParameter: float
        scaleParameter: float
        shapeParameter: float
        valuesCount: int
    

    class DesignStudyBuilder_DesignStudyObjective():
        attributeName: int
        attributeObject: Tag
        objectiveType: Optimization.DesignStudyBuilder.DesignStudyAttributeType
        warningLowerLimit: float
        warningUpperLimit: float
        failureLowerLimit: float
        failureUpperLimit: float
    

class DesignStudyAttributeBuilder(Builder):
    def __init__(self) -> None: ...
    def AdoptObject(self, object: NXObject) -> None:
        ...


