from ...NXOpen import *
from ..AutomatedTesting import *

import typing
import enum

class TestingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def RunCheckers(self, needCompare: bool) -> None:
        ...
    def AppendCheckerNode(self, className: str) -> Validate.CheckerNode:
        ...
    def AppendCheckerNodes(self, classNames: str, checkerNode: typing.List[Validate.CheckerNode]) -> None:
        """[Obsolete("Deprecated in NX1926.0.0.  Use AutomatedTesting.TestingManager.AddCheckerNodes with CheckerNode as result instead.")"""
        ...
    def AddCheckerNodes(self, classNames: str) -> typing.List[Validate.CheckerNode]:
        ...
    def RemoveCheckerNode(self, checkerNode: Validate.CheckerNode) -> None:
        ...
    def ClearCheckerNodes(self) -> None:
        ...
    def GetLogger(self) -> Validate.Logger:
        ...
    def ModifyOriginalPath(self, originalFileSpecification: str) -> str:
        ...
    def ExecuteMacro(self, macroFile: str) -> None:
        ...
    def RunDialogLaunchPerformanceTest(self, fileName: str, runCount: int) -> None:
        ...
    def Tag(self) -> Tag: ...

    TestCaseManager: AutomatedTesting.TestCaseManager


class TestCaseManager(Utilities.NXRemotableObject):
    def __init__(self, owner: AutomatedTesting.TestingManager) -> None: ...
    def CreateTestDefinition(self, caseParams: str, resourceFiles: str, subTestIds: str, interactive: bool, setUp: AutomatedTesting.TestCaseManager.SetupHandler, runTest: AutomatedTesting.TestCaseManager.RunTestHandler, tearDown: AutomatedTesting.TestCaseManager.TeardownHandler) -> None:
        ...
    def Tag(self) -> Tag: ...



    

    

    

    

    

    

    

    

    

class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


