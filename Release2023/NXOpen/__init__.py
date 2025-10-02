from . import StructureDesign
from . import BodyDes
from . import BlockStyler
from . import OpenXml
from . import CLDKin
from . import Drafting
from . import PartFamily
from . import MendixReporting
from . import Optimization
from . import ToolDesigner
from . import UserDefinedTemplate
from . import Layout2d
from . import Die
from . import Features
from . import Validate
from . import PDM
from . import ElectricalRouting
from . import Weld
from . import Fields
from . import Report
from . import RoutingCommon
from . import Display
from . import UIStyler
from . import Options
from . import PhysMat
from . import Formboard
from . import Join
from . import LineDesigner
from . import Placement
from . import ALP
from . import UserDefinedObjects
from . import Select
from . import Markup
from . import PID
from . import DSEPlatform
from . import Routing
from . import Assemblies
from . import ShapeSearch
from . import ShipDesign
from . import Issue
from . import Motion
from . import TDP
from . import Gateway
from . import UF
from . import Implicit
from . import CAE
from . import DSEDesignWorkflow
from . import Drawings
from . import CollaborationApplication
from . import DiagrammingLibraryAuthor
from . import MenuBar
from . import PressLineSimulation
from . import CableRouter
from . import ModlDirect
from . import PcbExchange
from . import MechanicalRouting
from . import CloudDM
from . import Diagramming
from . import SIM
from . import Annotations
from . import StageModel
from . import Positioning
from . import CADCAEPrep
from . import ModlUtils
from . import GeometricUtilities
from . import VisualReporting
from . import VectorArithmetic
from . import CAM
from . import RegionRecognition
from . import Layer
from . import MfgModel
from . import DMU
from . import Facet
from . import MoldCooling
from . import AnimationDesigner
from . import GeometricAnalysis
from . import MFGViewMaker
from . import Appearance
from . import Preferences
from . import Tooling
from . import Utilities
from . import AutomatedTesting
from . import Mechatronics
from . import Vsa
from . import DSE
from . import Mfg
from . import PLAS
from . import Schematic
from . import SheetMetal
from ..NXOpen import *

import typing
import enum

class XYZAxis(enum.Enum):
    XAxis = 0
    YAxis = 1
    ZAxis = 2


class XformCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Xform]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateXform(self, origin: Point3d, xDirection: Vector3d, yDirection: Vector3d, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, origin: Point3d, orientation: Matrix3x3, update: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, point1: Point, point2: Point, point3: Point, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, plane1: IPlaneForXformByThreePlanes, plane2: IPlaneForXformByThreePlanes, plane3: IPlaneForXformByThreePlanes, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, csys: CoordinateSystem, point0: Point, point1: Point, rotationScalarX: Scalar, rotationScalarY: Scalar, rotationScalarZ: Scalar, rotationOption: int, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXformWithView(self, view: View, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXform(self, csys: CoordinateSystem, point0: Offset, point1: Offset, rotationScalarX: Scalar, rotationScalarY: Scalar, rotationScalarZ: Scalar, rotationOption: int, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXformByDynamicOffset(self, csys: CoordinateSystem, originOffset: Vector3d, trasformMatrix: Matrix3x3, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, origin: Point, xDirection: Direction, yDirection: Direction, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXformByPointXDirZDir(self, origin: Point, xDirection: Direction, zDirection: Direction, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXformByPointYDirZDir(self, origin: Point, yDirection: Direction, zDirection: Direction, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, xDirection: Direction, yDirection: Direction, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, plane: DisplayableObject, axis: Direction, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, xPoint: Point, zAxis: Axis, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXform(self, point: Point, helperPoint: Point, curve: ICurve, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXform(self, workOcc: Assemblies.Component, contextObject: Assemblies.Component, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformFromCurrentView(self, updateOption: SmartObject.UpdateOption, scale: float) -> Xform:
        ...
    def CreateXform(self, object: NXObject, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXform(self, object: NXObject, explosion: Assemblies.Explosion, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateExtractXform(self, object: NXObject, updateOption: SmartObject.UpdateOption, forceXformCreation: bool, proto: NXObject) -> Xform:
        ...
    def CreateXform(self, explosion: Assemblies.Explosion, sourceComponent: Assemblies.Component, destComponent: Assemblies.Component, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXform(self, origin: Point, axis: XYZAxis, direction: Direction, scale: Scalar, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformWithReverseNormal(self, xform: Xform, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformDistanceDirection(self, direction: Direction, distance: Expression, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformDistanceBetweenPoints(self, origin: Point, measure: Point, vector: Direction, distance: Expression, originDistance: Expression, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformDistanceRadial(self, axis: Axis, point: Point, distance: Expression, originDistance: Expression, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformAngleAxis(self, axis: Axis, angle: Expression, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformTwoPoints(self, from: Point, to: Point, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformRotateThreePoints(self, vector: Axis, start: Point, end: Point, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformAxisVector(self, axis: Axis, vector: Direction, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformCsysToCsys(self, from: CoordinateSystem, to: CoordinateSystem, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformDistanceAngle(self, distance: Expression, angle: Expression, dirr: Axis, angulardirr: Direction, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformDynamic(self, org: typing.List[Scalar], mtx: typing.List[Scalar], updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformDeltaXyz(self, delta: typing.List[Scalar], updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def CreateXformByPlaneXDirPoint(self, plane: DisplayableObject, xDirection: Direction, point: Point, updateOption: SmartObject.UpdateOption, scale: float, flipXDirection: bool, flipZDirection: bool) -> Xform:
        ...
    def CreateXformByPlaneYDirPoint(self, plane: DisplayableObject, yDirection: Direction, point: Point, updateOption: SmartObject.UpdateOption, scale: float, flipYDirection: bool, flipZDirection: bool) -> Xform:
        ...
    def CreateXformExtract(self, updateOption: SmartObject.UpdateOption, xform1: Xform, xform2: Xform) -> Xform:
        ...
    def CreateXformPqr(self, updateOption: SmartObject.UpdateOption, origin: Point, pPoint: Point, qPoint: Point, scale: float, axisAndPlaneType: XformCollection.AxisAndPlaneType) -> Xform:
        ...
    def CreateXformEulerTaitBryanAngles(self, csys: CoordinateSystem, originPoint: Point, sequence: XformCollection.RotationSequence, rotationScalarX: Scalar, rotationScalarY: Scalar, rotationScalarZ: Scalar, scale: float, updateOption: SmartObject.UpdateOption) -> Xform:
        ...
    def Tag(self) -> Tag: ...



    class RotationSequence(enum.Enum):
        ZXZ = 0
        XYX = 1
        YZY = 2
        ZYZ = 3
        XZX = 4
        YXY = 5
        XYZ = 6
        YZX = 7
        ZXY = 8
        XZY = 9
        ZYX = 10
        YXZ = 11
    

    class AxisAndPlaneType(enum.Enum):
        XaxisXyPlane = 0
        XaxisXzPlane = 1
        YaxisXyPlane = 2
        YaxisYzPlane = 3
        ZaxisXzPlane = 4
        ZaxisYzPlane = 5
    

class Xform(SmartObject):
    def __init__(self) -> None: ...
    def SetOrigin(self, origin: Point3d) -> None:
        ...
    def SetOrientation(self, orientation: Matrix3x3) -> None:
        ...
    def SetScale(self, scale: float) -> None:
        ...
    Orientation: Matrix3x3
    Origin: Point3d
    Scale: float


class WithinCurvesRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> IFacet:
        ...


class WidthDefinition(TaggedObject):
    def __init__(self) -> None: ...
    def GetCustomWidths(self) -> typing.List[CustomWidth]:
        ...
    def GetColorWidths(self) -> typing.List[ColorWidth]:
        ...
    Single: int
    SingleSource: int
    SingleWidth: float
    Units: int
    Use: int


class WCS(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def Save(self) -> CartesianCoordinateSystem:
        ...
    def SetOriginAndMatrix(self, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def Rotate(self, rotationAxis: WCS.Axis, angle: float) -> None:
        ...
    def SetCoordinateSystem(self, newCs: CartesianCoordinateSystem) -> CartesianCoordinateSystem:
        ...
    def SetCoordinateSystemCartesianAtCsys(self, newCs: CartesianCoordinateSystem) -> CartesianCoordinateSystem:
        ...
    def Tag(self) -> Tag: ...

    CoordinateSystem: CartesianCoordinateSystem
    Origin: Point3d
    Visibility: bool


    class Axis(enum.Enum):
        XAxis = 1
        YAxis = 2
        ZAxis = 3
    

class WavefrontObjImporter(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    CanCreateSingleFeature: bool
    Cleanup: bool
    FileOpenFlag: bool
    ImportAs: WavefrontObjImporter.ImportAsOption
    ImportGroups: WavefrontObjImporter.GroupsEnum
    ImportTo: WavefrontObjImporter.ImportToOption
    ImportToTeamcenter: bool
    ImportUnits: WavefrontObjImporter.UnitsEnum
    Messages: WavefrontObjImporter.MessageEnum
    ReverseNames: bool
    SettingsFile: str
    ShowInformationWindowFlag: bool


    class UnitsEnum(enum.Enum):
        Millimeters = 0
        Inches = 1
        Meters = 2
        Centimeters = 3
        Feet = 4
        Microns = 5
    

    class MessageEnum(enum.Enum):
        None = 0
        Informational = 1
        Warning = 2
        Error = 3
        Debug = 4
        All = 5
    

    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

    class ImportAsOption(enum.Enum):
        ConvergentGeometry = 0
        SubdivisionGeometry = 1
    

    class GroupsEnum(enum.Enum):
        NodeNames = 0
        Assembly = 1
        Off = 2
    

class WavefrontObjCreator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    AngularTolerance: float
    ChordalTolerance: float
    ExportAs: WavefrontObjCreator.ExportAsOption
    ExportFrom: WavefrontObjCreator.ExportFromOption
    ExportSelectionBlock: ObjectSelector
    ExportUnits: WavefrontObjCreator.UnitsEnum
    FeatureSelector: Features.SelectFeatureList
    FileSaveFlag: bool
    FlattenAssemblyStructure: bool
    InputFile: str
    SettingsFile: str


    class UnitsEnum(enum.Enum):
        Millimeters = 0
        Inches = 1
        Meters = 2
        Centimeters = 3
        Feet = 4
        Microns = 5
    

    class ExportFromOption(enum.Enum):
        DisplayPart = 0
        ExistingPart = 1
    

    class ExportAsOption(enum.Enum):
        FacetGeometry = 0
        SubdivisionGeometry = 1
    

class VRMLImporter(Importer):
    def __init__(self) -> None: ...
    AllLevelsOfDetail: bool
    AngularTolerance: VRMLImporter.AngularToleranceType
    FileUnits: VRMLImporter.FileUnitsType
    GenerateOneModel: bool
    HideSmoothEdges: bool
    MoreSummaryDetails: bool
    SuppressWarningMessages: bool


    class FileUnitsType(enum.Enum):
        Meters = 0
        Millimeters = 1
        Inches = 2
    

    class AngularToleranceType(enum.Enum):
        Coarse = 0
        Medium = 1
        Fine = 2
    

class VirtuallabImporter(Builder):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    ApplyUnits: bool
    OutputDirectory: str
    SettingsFile: str
    SkipTranslatedParts: bool
    UseEnglishForPartUnits: bool
    UseFileDirectory: bool


class VirtualAxis(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Direction: VectorArithmetic.Vector3
    Position: float
    Speed: float
    Active: bool


    class VirtualAxis.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class ViewUIManager(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def CreatePreview(self, viewTag: View, fit: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class ViewSetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[ViewSet]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateViewSet(self, viewSetName: str, baseView: ModelingView, baseViewOrientation: ViewSet.ViewOrientation, viewOrientations: typing.List[ViewSet.ViewOrientation]) -> ViewSet:
        ...
    def FindObject(self, journalingId: str) -> ViewSet:
        ...
    def Tag(self) -> Tag: ...



class ViewSet(NXObject):
    def __init__(self) -> None: ...
    def AddView(self, orientation: ViewSet.ViewOrientation) -> None:
        ...
    def GetBaseView(self) -> ModelingView:
        ...
    def SetBaseView(self, orientation: ViewSet.ViewOrientation) -> None:
        ...
    def GetViews(self, views: typing.List[ModelingView]) -> None:
        ...


    class ViewOrientation(enum.Enum):
        Top = 0
        Front = 1
        Right = 2
        Back = 3
        Bottom = 4
        Left = 5
        Isometric = 6
        Trimetric = 7
        Dimetric = 8
    

class ViewDependentDisplayManager(Utilities.NXRemotableObject):
    def __init__(self, owner: View) -> None: ...
    def ApplyShadeEdit(self, shadeColor: NXColor, partialShading: ViewDependentDisplayManager.PartialShading, translucencyOption: ViewDependentDisplayManager.Translucency, translucencyScale: int, objects: typing.List[DisplayableObject]) -> None:
        ...
    def ApplyShadeEdit(self, partialShading: ViewDependentDisplayManager.PartialShading, translucencyOption: ViewDependentDisplayManager.Translucency, translucencyScale: int, objects: typing.List[DisplayableObject]) -> None:
        ...
    def ApplyWireframeEdit(self, color: NXColor, font: ViewDependentDisplayManager.Font, width: ViewDependentDisplayManager.Width, objects: typing.List[DisplayableObject]) -> None:
        ...
    def ApplyWireframeEdit(self, font: ViewDependentDisplayManager.Font, width: ViewDependentDisplayManager.Width, objects: typing.List[DisplayableObject]) -> None:
        ...
    def ApplySegmentEdit(self, object: DisplayableObject, color: NXColor, font: ViewDependentDisplayManager.Font, width: ViewDependentDisplayManager.Width, segmentStart: float, segmentEnd: float) -> None:
        ...
    def ApplySegmentEdit(self, object: DisplayableObject, font: ViewDependentDisplayManager.Font, width: ViewDependentDisplayManager.Width, segmentStart: float, segmentEnd: float) -> None:
        ...
    def Erase(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def RemoveErasure(self, objects: typing.List[DisplayableObject]) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.ViewDependentDisplayManager.RemoveErasureOnObjectAndSubobjects instead.")"""
        ...
    def RemoveErasureOnObjectAndSubobjects(self, objects: typing.List[DisplayableObject], removeFromSubObjects: bool) -> None:
        ...
    def RemoveEdit(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def RemoveAllEdits(self) -> None:
        ...
    def MoveToModel(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def MoveToView(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def SetBackground(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def Tag(self) -> Tag: ...



    class Width(enum.Enum):
        Normal = 0
        Thick = 1
        Thin = 2
        Object = 3
        One = 5
        Two = 6
        Three = 7
        Four = 8
        Five = 9
        Six = 10
        Seven = 11
        Eight = 12
        Nine = 13
    

    class Translucency(enum.Enum):
        NoChange = 0
        Original = 1
        Yes = 2
    

    class PartialShading(enum.Enum):
        NoChange = 0
        Original = 1
        No = 2
        Yes = 3
    

    class Font(enum.Enum):
        Invisible = 0
        Solid = 1
        Dashed = 2
        Phantom = 3
        Centerline = 4
        Dotted = 5
        LongDashed = 6
        DottedDashed = 7
        Object = 8
        Eight = 11
        Nine = 12
        Ten = 13
        Eleven = 14
    

class ViewCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[View]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Refresh(self) -> None:
        ...
    def GetActiveViews(self) -> typing.List[View]:
        ...
    def GetCustomViews(self) -> str:
        ...
    def IsWorkViewExpanded(self) -> bool:
        ...
    def SaveAs(self, selectedView: View, newViewName: str, copyViewModifications: bool, moveViewDependencies: bool) -> View:
        ...
    def Save(self) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> View:
        ...
    def UnexpandWork(self) -> None:
        ...
    def FitAll(self) -> None:
        ...
    def Regenerate(self) -> None:
        ...
    def UpdateDisplay(self) -> None:
        ...
    def CreateScene(self, view: View, makeReferencedObjects: bool) -> Display.Scene:
        ...
    def CreateBackground(self, view: View, makeReferencedObjects: bool) -> Display.Background:
        ...
    def CreateShadows(self, view: View) -> Display.Shadows:
        ...
    def CreateImage(self, view: View) -> Display.Image:
        ...
    def CreateStage(self, view: View, makeReferencedObjects: bool) -> Display.Stage:
        ...
    def CreateWall(self, view: View, wallType: Display.Stage.WallType) -> Display.Wall:
        ...
    def CreateReflection(self, view: View, makeReferencedObjects: bool) -> Display.Reflection:
        ...
    def CreateLighting(self, view: View) -> Display.Lighting:
        ...
    def CreateLightBuilder(self, light: Light) -> Display.LightBuilder:
        ...
    def CreateImageBasedLighting(self, view: View, makeReferencedObjects: bool) -> Display.ImageBasedLighting:
        ...
    def CreateExtractScene(self, view: View) -> Display.ExtractScene:
        ...
    def CreateNonProportionalZoom(self) -> Display.NonProportionalZoom:
        ...
    def CreateStudioImageCaptureBuilder(self) -> Display.StudioImageCaptureBuilder:
        ...
    def SaveAsPreservingCase(self, selectedView: View, newViewName: str, copyViewModifications: bool, moveViewDependencies: bool) -> View:
        ...
    def CreateRayTracedStudioBuilder(self) -> Display.RayTracedStudioBuilder:
        ...
    def CreateSaveImageFileBrowserBuilder(self) -> Display.SaveImageFileBrowserBuilder:
        ...
    def CreateGlobalIlluminationBuilder(self) -> Display.GlobalIlluminationBuilder:
        ...
    def CreateRayTracedStudioPreferencesBuilder(self) -> Display.RayTracedStudioPreferencesBuilder:
        ...
    def CreateRayTracedStudioEditorBuilder(self) -> Display.RayTracedStudioEditorBuilder:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Display.RayTracedStudioPreferencesBuilder instead.")"""
        ...
    def CreateIrayPlusStudioEditorBuilder(self) -> Display.IRayPlusStudioEditorBuilder:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.Display.IRayPlusStudioPreferencesBuilder instead.")"""
        ...
    def CreateEnvironmentBuilder(self, view: View, makeReferencedObjects: bool) -> Display.EnvironmentBuilder:
        ...
    def CreateIrayPlusStudioPreferencesBuilder(self) -> Display.IRayPlusStudioPreferencesBuilder:
        ...
    def CreateDownloadOfflineRenderingBuilder(self) -> Display.DownloadOfflineRenderingBuilder:
        ...
    def CreateIrayPlusStudioAnimationBuilder(self) -> Display.IrayPlusStudioAnimationBuilder:
        ...
    def CreateIrayPlusSimpleMaterialEditorBuilder(self) -> Display.IrayPlusSimpleMaterialEditorBuilder:
        ...
    def CreateIrayPlusMaterialEditorBuilder(self, materialName: str) -> Display.IrayPlusMaterialEditorBuilder:
        ...
    def GetDisclosedModelViews(self) -> typing.List[View]:
        ...
    def GetDisclosedModelViewsAndPurposes(self, disclosurePurposes: str) -> typing.List[View]:
        ...
    def CreateHighEndRenderImage(self, fileLocation: str) -> ViewCollection.HighEndRenderImageResults:
        ...
    def DestroyHighEndRenderSession(self) -> None:
        ...
    def CreateImageExportBuilder(self) -> Gateway.ImageExportBuilder:
        ...
    def Tag(self) -> Tag: ...

    WorkView: View


    class ViewCollectionHighEndRenderImageResults():
        Iterations: int
        Seconds: float
        def ToString(self) -> str:
            ...
        def __init__(self, Iterations: int, Seconds: float) -> None: ...
    

class View(NXObject):
    def __init__(self) -> None: ...
    def Concatenate(self, translation: Point3d) -> None:
        ...
    def Concatenate(self, scale: float) -> None:
        ...
    def Concatenate(self, translation: Point3d, scale: float) -> None:
        ...
    def Concatenate(self, centerOfRotation: Point3d, rotationAxis: Vector3d, angle: float) -> None:
        ...
    def Concatenate(self, translation: Point3d, centerOfRotation: Point3d, rotationAxis: Vector3d, angle: float) -> None:
        ...
    def Concatenate(self, scale: float, centerOfRotation: Point3d, rotationAxis: Vector3d, angle: float) -> None:
        ...
    def Concatenate(self, translation: Point3d, scale: float, centerOfRotation: Point3d, rotationAxis: Vector3d, angle: float) -> None:
        ...
    def Expand(self) -> None:
        ...
    def Fit(self) -> None:
        ...
    def FitAfterShowOrHide(self, type: View.ShowOrHideType) -> None:
        ...
    def FitToObjects(self, objects: typing.List[IFitTo]) -> None:
        ...
    def PanToObjects(self, objects: typing.List[INXObject]) -> None:
        ...
    def FlyToObjects(self, objects: typing.List[INXObject]) -> None:
        ...
    def GetExpandedScale(self) -> float:
        ...
    def GetAxis(self, xYZAxis: XYZAxis) -> Vector3d:
        ...
    def MakeWork(self) -> None:
        ...
    def Orient(self, matrix: Matrix3x3) -> None:
        ...
    def Orient(self, viewName: View.Canned, viewScale: View.ScaleAdjustment) -> None:
        ...
    def Orient(self, viewName: str, viewScale: View.ScaleAdjustment) -> None:
        ...
    def Regenerate(self) -> None:
        ...
    def Restore(self) -> bool:
        ...
    def Rotate(self, matrix: Matrix3x3) -> None:
        ...
    def Rotate(self, origin: Point3d, vector: Vector3d, angle: float) -> None:
        ...
    def SetOrigin(self, origin: Point3d) -> None:
        ...
    def SetScale(self, scale: float) -> None:
        ...
    def SetRotationTranslationScale(self, rotMatrix: Matrix3x3, translation: Point3d, scale: float) -> None:
        ...
    def SnapToClosestCannedOrientation(self) -> None:
        ...
    def SnapToVariantCannedOrientation(self) -> None:
        ...
    def UpdateDisplay(self) -> None:
        ...
    def Zoom(self, scaleFactor: View.ScaleFactor) -> None:
        ...
    def ZoomAboutPoint(self, relativeScale: float, scaleAboutPoint: Point3d, viewCenter: Point3d) -> None:
        ...
    def ZoomByRectangle(self, corner1: Point3d, corner2: Point3d) -> None:
        ...
    def ChangePerspective(self, changeViewToPerspective: bool) -> None:
        ...
    def AskVisibleObjects(self) -> typing.List[DisplayableObject]:
        ...
    def UpdateCustomSymbols(self) -> None:
        ...
    def HasPreview(self) -> bool:
        ...
    def EnableNavigationFlyThrough(self, isEnable: bool) -> None:
        ...
    def IsNavigationFlyThroughEnabled(self) -> bool:
        ...
    def SaveNavigationHomeView(self) -> None:
        ...
    def RestoreNavigationHomeView(self) -> None:
        ...
    def NavigationFlyThrough(self, startPoint: Point3d, startEnd: Point3d) -> None:
        ...
    def NavigationFlyThroughWithScale(self, relativeScale: float) -> None:
        ...
    VisualizationVisualPreferences: Preferences.ViewVisualizationVisual
    VisualizationSpecialEffectsPreferences: Preferences.ViewVisualizationSpecialEffects
    DependentDisplay: ViewDependentDisplayManager
    AbsoluteOrigin: Point3d
    DisclosurePurpose: str
    IsDisclosed: bool
    LockRotations: bool
    Matrix: Matrix3x3
    Origin: Point3d
    RenderingStyle: View.RenderingStyleType
    Scale: float
    SyncViews: bool
    TriadVisibility: bool
    WcsVisibility: bool


    class ShowOrHideType(enum.Enum):
        ShowOnly = 0
        HideOnly = 1
        BothShowAndHide = 2
        InvertShownAndHidden = 3
    

    class ScaleFactor(enum.Enum):
        HalfScale = 0
        DoubleScale = 1
        ReduceScale = 2
        IncreaseScale = 3
    

    class ScaleAdjustment(enum.Enum):
        Fit = 0
        Current = 1
        Saved = 2
    

    class RenderingStyleType(enum.Enum):
        ShadedWithEdges = 0
        ShadedWithBodyColorEdges = 1
        Shaded = 2
        WireframeWithDimEdges = 3
        WireframeWithHiddenEdges = 4
        WireframeWithDashedEdges = 5
        Studio = 6
        FaceAnalysis = 7
        PartiallyShaded = 8
        StaticWireframe = 9
    

    class Canned(enum.Enum):
        Top = 0
        Front = 1
        Right = 2
        Back = 3
        Bottom = 4
        Left = 5
        Isometric = 6
        Trimetric = 7
    

class VelocitySensor(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Signal: float
    Active: bool


    class VelocitySensor.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Vector3d():
    X: float
    Y: float
    Z: float
    def ToString(self) -> str:
        ...
    def __init__(self, X: float, Y: float, Z: float) -> None: ...


class Validator(DexBuilder):
    def __init__(self) -> None: ...
    LogFile: str
    OutputFile: str
    ProductName: str


class ValidationCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Validation]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, source: str, type: Validation.InputType) -> Validation:
        ...
    def GetRevisionRule(self) -> str:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Validate.RequirementCollection.RevisionRule instead.")"""
        ...
    def SetRevisionRule(self, rule: str) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.Validate.RequirementCollection.RevisionRule instead.")"""
        ...
    def Tag(self) -> Tag: ...



class Validation(NXObject):
    def __init__(self) -> None: ...
    def SetUpdateControl(self, updateTime: Validation.UpdateTime) -> None:
        ...
    def Add(self, key: str, objs: typing.List[NXObject]) -> None:
        ...
    def Replace(self, key: str, objs: typing.List[NXObject]) -> None:
        ...
    def Add(self, key: str, text: str) -> None:
        ...
    def Add(self, key: str, number: float) -> None:
        ...
    def Add(self, key: str, number: int) -> None:
        ...
    def Add(self, key: str, day: int, time: int) -> None:
        ...
    def Evaluate(self) -> Validation.Result:
        ...
    def GetCheckResult(self) -> Validation.Result:
        ...
    def SetCheckResult(self, result: Validation.Result) -> None:
        ...
    def GetKeys(self) -> str:
        ...
    def GetKeyType(self, key: str) -> Validation.MapType:
        ...
    def SetUserClassName(self, name: str) -> None:
        ...
    def Lookup(self, key: str) -> typing.List[NXObject]:
        ...
    def LookupNumber(self, key: str, number: float, found: bool) -> None:
        ...
    def LookupText(self, key: str, text: str, found: bool) -> None:
        ...
    def LookupInteger(self, key: str, number: int, found: bool) -> None:
        ...
    def LookupTime(self, key: str, day: int, time: int, found: bool) -> None:
        ...
    def Remove(self, key: str) -> None:
        ...
    def GetSuppressed(self) -> bool:
        ...
    def SetSuppressed(self, suppress: bool) -> None:
        ...
    def GetInitialResult(self) -> Validation.Result:
        ...
    def Delete(self) -> None:
        ...
    def Information(self) -> None:
        ...
    def GetAssociatedObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def SetAssociatedObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    Requirement: str


    class UpdateTime(enum.Enum):
        EveryChange = 0
        Save = 1
    

    class Result(enum.Enum):
        Pass = 0
        Information = 1
        Warning = 2
        Failed = 3
        Unknown = 4
        Skipped = 5
    

    class MapType(enum.Enum):
        Text = 0
        Real = 1
        Int = 2
        Time = 3
        Tag = 4
        None = 5
    

    class InputType(enum.Enum):
        KfClass = 0
        Spreadsheet = 1
        TextFile = 2
        Xml = 3
        Tcr = 4
        Application = 5
        Num = 6
    

class VacuumGripper(Gripper):
    def __init__(self, pItem: int) -> None: ...
    Grip: bool
    Release: bool
    Duration: float
    GrippedObject: RigidBody
    HasGrippedObject: bool
    Active: bool


    class VacuumGripper.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Update(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def AddToDeleteList(self, objects: typing.List[NXObject]) -> int:
        """[Obsolete("Deprecated in NX12.0.0.  Use Update.AddObjectsToDeleteList instead.")"""
        ...
    def AddToDeleteList(self, object: TaggedObject) -> int:
        ...
    def RemoveFromDeleteList(self, objects: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use Update.RemoveObjectsFromDeleteList instead.")"""
        ...
    def GetDeleteList(self) -> typing.List[NXObject]:
        """[Obsolete("Deprecated in NX12.0.0.  Use Update.GetObjectsOnDeleteList instead.")"""
        ...
    def ClearDeleteList(self) -> None:
        ...
    def DoUpdate(self, undoMark: Session.UndoMarkId) -> int:
        ...
    def ClearErrorList(self) -> None:
        ...
    def DoInterpartUpdate(self, undoMark: Session.UndoMarkId) -> None:
        ...
    def SetDefaultUpdateFailureAction(self, failureAction: Update.FailureOption) -> None:
        ...
    def GetDefaultUpdateFailureAction(self) -> Update.FailureOption:
        ...
    def SetUpdateFailureAction(self, object: TaggedObject, failureAction: Update.FailureOption) -> None:
        ...
    def RemoveUpdateFailureAction(self, object: TaggedObject) -> None:
        ...
    def DoAssemblyConstraintsUpdateInPart(self, partTag: Part, undoMarkId: Session.UndoMarkId) -> None:
        ...
    def DoAssemblyConstraintsUpdate(self, undoMarkId: Session.UndoMarkId) -> None:
        ...
    def StartLocalUpdate(self) -> None:
        ...
    def EndLocalUpdate(self) -> None:
        ...
    def UndelayObjectUpdate(self, objectToUpdate: TaggedObject) -> None:
        ...
    def LogForUpdate(self, objectToUpdate: TaggedObject) -> None:
        ...
    def SetUpdateLock(self, lock: bool) -> None:
        ...
    def GetUpdateLock(self) -> bool:
        ...
    def UpdateAllIntrapartPartModulesInPart(self, partTag: Part, undoMarkId: Session.UndoMarkId) -> None:
        """[Obsolete("Deprecated in NX1899.0.0.  Use Update.UpdateModelinstead.")"""
        ...
    def MakeUpToDate(self, objects: typing.List[NXObject], undoMarkId: Session.UndoMarkId) -> None:
        ...
    def UpdateAllLinkedPartModulesInPart(self, partTag: Part, undoMarkId: Session.UndoMarkId) -> None:
        ...
    def AddObjectsToDeleteList(self, objects: typing.List[TaggedObject]) -> int:
        ...
    def RemoveObjectsFromDeleteList(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def GetObjectsOnDeleteList(self) -> typing.List[TaggedObject]:
        ...
    def UpdateAllProductInterfaceInPart(self, partTag: Part, undoMarkId: Session.UndoMarkId) -> None:
        ...
    def UpdateModel(self, partTag: Part, undoMarkId: Session.UndoMarkId) -> None:
        ...
    def SetPropagateDelete(self, propagateToDelete: bool) -> None:
        ...
    def LogObjectsToMakeUpToDate(self, objectTag: TaggedObject) -> None:
        ...
    def Tag(self) -> Tag: ...

    AssemblyConstraintsDelay: bool
    ErrorList: ErrorList
    InterpartDelay: bool
    IntrapartPartModuleDelay: bool
    ModelUpdateDelay: bool
    ProductInterfaceDelay: bool


    class Option(enum.Enum):
        Now = 0
        Later = 1
    

    class FailureOption(enum.Enum):
        NoOption = 0
        Undo = 1
        Suppress = 2
        SuppressAll = 3
        Accept = 4
        AcceptAll = 5
        Delete = 6
        DeleteDependents = 7
        Interrupt = 8
    

class UnitCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Unit]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def SetDefaultDataEntryUnits(self, defaults: UnitCollection.UnitDefaults) -> None:
        ...
    def GetDefaultDataEntryUnits(self) -> UnitCollection.UnitDefaults:
        ...
    def SetDefaultObjectInformationUnits(self, defaults: UnitCollection.UnitDefaults) -> None:
        ...
    def GetDefaultObjectInformationUnits(self) -> UnitCollection.UnitDefaults:
        ...
    def FindObject(self, name: str) -> Unit:
        ...
    def GetMeasures(self) -> str:
        ...
    def GetMeasureTypes(self, measureName: str) -> typing.List[Unit]:
        ...
    def GetBase(self, measureName: str) -> Unit:
        ...
    def Convert(self, initialUnitType: Unit, targetUnitType: Unit, initialValue: float) -> float:
        ...
    def GetDataEntryUnit(self, measureName: str) -> Unit:
        ...
    def GetObjectInformationUnit(self, measureName: str) -> Unit:
        ...
    def Tag(self) -> Tag: ...



    class UnitDefaults(enum.Enum):
        LbmInLbfDegF = 0
        LbmFtLbfDegF = 1
        GMmNDegC = 2
        GCmNDegC = 3
        KgMNRadK = 4
        KgMmNDegC = 5
    

class Unit(NXObject):
    def __init__(self) -> None: ...
    def MakeDefault(self) -> None:
        ...
    def MakeInfoUnit(self) -> None:
        ...
    Abbreviation: str
    IsBaseUnit: bool
    IsDefaultUnit: bool
    IsInfoUnit: bool
    Measure: str
    Name: str
    Symbol: str
    TypeName: str


class UnderlineStyleT(enum.Enum):
    None = 0
    Single = 1
    SingleAccounting = 2
    Double = 3
    DoubleAccounting = 4


class UI(TaggedObject):
    def __init__(self) -> None: ...
    def GetUI(self) -> UI:
        ...
    def LockAccess(self) -> None:
        ...
    def UnlockAccess(self) -> None:
        ...
    def JournalPause(self) -> None:
        ...
    def AskLockStatus(self) -> UI.Status:
        ...
    def CreateDialog(self, dialogName: str) -> BlockStyler.BlockDialog:
        ...
    def AddUtilityFunctionVisibilityHandler(self, utilityFunctionVisibilityHandler: UI.UtilityFunctionVisibilityHandler) -> int:
        ...
    def RemoveUtilityFunctionVisibilityHandler(self, id: int) -> None:
        ...
    def CreateCustomPopupMenuHandler(self) -> CustomPopupMenuHandler:
        ...
    def CreateSnapDialog(self, dialogName: str) -> BlockStyler.SnapBlockDialog:
        ...
    def CreateImageExportBuilder(self) -> Gateway.ImageExportBuilder:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.ViewCollection.CreateImageExportBuilder  instead.")"""
        ...
    def CanOpenPart(self) -> bool:
        ...
    def DisplayNotification(self, title: str, description: str, extraText: str, icon: str) -> int:
        ...
    def RemoveNotification(self, id: int) -> None:
        ...
    NXMessageBox: NXMessageBox
    Styler: UIStyler.Styler
    SelectionManager: Selection
    ObjectPreferences: Preferences.ObjectPreferences
    UserInterfacePreferences: Preferences.SessionUserInterfaceUI
    VisualizationVisualPreferences: Preferences.SessionVisualizationVisual
    VisualizationLinePreferences: Preferences.VisualizationLine
    VisualizationShadingPreferences: Preferences.SessionVisualizationShade
    MenuBarManager: MenuBar.MenuBarManager
    MovieManager: MovieManager
    ViewUIManager: ViewUIManager
    ProductDemo: ProductDemo


    

    class Status(enum.Enum):
        Lock = 0
        Unlock = 1
    

    

    

class TreeListNode(TaggedObject):
    def __init__(self) -> None: ...


class TransportSurface(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    ParallelSpeed: float
    PerpendicularSpeed: float
    Surface: CollisionMaterial
    Active: bool


    class TransportSurface.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class TransmitterExit(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Position: VectorArithmetic.Vector3
    Orientation: VectorArithmetic.Matrix3
    Body: RigidBody
    Port: int
    Active: bool


    class TransmitterExit.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class TransmitterEntry(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Port: int
    Active: bool
    ExecuteOnce: bool


    class TransmitterEntry.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class TransientObject(Utilities.NXRemotableObject):
    def __init__(self, ptr: int) -> None: ...
    def __init__(self) -> None: ...
    def Dispose(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    def Finalize(self) -> None:
        ...
    def ToString(self) -> str:
        ...
    def PrintTestData(self, variableName: str) -> None:
        ...
    def PrintTestData(self, variableName: str, lineNumber: int) -> None:
        ...
    Handle: int


class Transformer(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Body: RigidBody
    Active: bool
    ExecuteOnce: bool


    class Transformer.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Tracer(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Active: bool


    class Tracer.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class TracelineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Traceline]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateAutomaticTraceline(self, explosion: Assemblies.Explosion, startPoint: Point, startDirection: Direction, endPoint: Point, endDirection: Direction, orientation: Matrix3x3, mode: AutomaticTraceline.ModeOption, solution: int, startOffset: float, endOffset: float, segmentIndices: int, segmentLengths: float) -> AutomaticTraceline:
        ...
    def Tag(self) -> Tag: ...



class Traceline(DisplayableObject):
    def __init__(self) -> None: ...
    def AskShape(self) -> Curve:
        ...
    def AskExplosion(self) -> Assemblies.Explosion:
        ...


class TopologyOptimizationTaskEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Enter(self) -> None:
        ...
    def Exit(self) -> None:
        ...
    def SetFeatureToEdit(self, feature: Features.TopologyOptimizationFeature) -> None:
        ...
    def SetCancelled(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveFeature: Features.TopologyOptimizationFeature


class TextureModelingTaskEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Enter(self) -> None:
        ...
    def Exit(self) -> None:
        ...
    def SetFeatureToEdit(self, feature: Features.Texture) -> None:
        ...
    def SetCancelled(self) -> None:
        ...
    def DelayTextureUpdate(self) -> None:
        ...
    def UndelayTextureUpdate(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveFeature: Features.Texture


class TextColorFontWidthBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    TextColor: NXColor
    TextFont: str
    TextStyle: str
    TextWidth: str


class TextAlignmentModeT(enum.Enum):
    VertTop = 0
    VertMiddle = 1
    VertBottom = 2
    VertJustify = 3
    VertDistributed = 4
    HorGeneral = 5
    HorLeft = 6
    HorCenter = 7
    HorRight = 8
    HorFill = 9
    HorJustify = 10
    HorCenterAcrossSelection = 11
    HorDistributed = 12


class TangentFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, tangencyTolerance: float) -> IFacet:
        ...
    def UpdateTangencyTolerance(self, tangencyTolerance: float) -> None:
        ...


class TaggedObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def Append(self, object: TaggedObject) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: TaggedObject) -> int:
        ...
    def FindItem(self, index: int) -> TaggedObject:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: TaggedObject) -> None:
        ...
    def Erase(self, obj: TaggedObject, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[TaggedObject]:
        ...
    def SetContents(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: TaggedObject, object2: TaggedObject) -> None:
        ...
    def Insert(self, location: int, object: TaggedObject) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class TaggedObjectCollection(Utilities.NXRemotableObject):
    def GetEnumerator(self) -> None:
        ...
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def initialize(self) -> None:
        ...
    def __init__(self) -> None: ...


    class TaggedObjectCollection.Enumerator(System.Object):
        def MoveNext(self) -> bool:
            ...
        def Reset(self) -> None:
            ...
        Current: any
    

class TaggedObject(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...
    def initialize(self) -> None:
        ...
    def ToString(self) -> str:
        ...
    def PrintTestData(self, variableName: str) -> None:
        ...
    def PrintTestData(self, variableName: str, lineNumber: int) -> None:
        ...
    def Tag(self) -> Tag: ...



class TagForm(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetNumParameters(self) -> int:
        ...
    def GetParameter(self, nProp: int) -> Parameter:
        ...


    class TagForm.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Tag(enum.Enum):
    Null = 0


class TableEditorDefaultDataProvider(TaggedObject):
    def __init__(self) -> None: ...
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def GetString(self, row: int, column: int) -> str:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def GetInteger(self, row: int, column: int, isUnassigned: bool) -> int:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def GetDouble(self, row: int, column: int, isUnassigned: bool) -> float:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def GetBoolean(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, rows: int, column: int) -> bool:
        ...
    def Destroy(self) -> None:
        ...
    ColumnCount: int
    RowCount: int


class TableBase(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...


    class TableBase.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class SymbolFont(NXObject):
    def __init__(self) -> None: ...


class SurfaceUVDirectionBuilder(Builder):
    def __init__(self) -> None: ...
    ReverseU: bool
    ReverseV: bool
    SwapUandV: bool
    TargetFace: SelectFaceList


class SurfaceRebuildData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetTolerances(self, tolerances: float) -> None:
        ...
    def GetTolerances(self, numTolerances: int) -> float:
        ...
    CrossDegree: int
    CrossMaxDegree: int
    CrossMaxSegments: int
    CrossRebuildType: SurfaceRebuildData.Type
    PrimaryDegree: int
    PrimaryMaxDegree: int
    PrimaryMaxSegments: int
    PrimaryRebuildType: SurfaceRebuildData.Type


    class Type(enum.Enum):
        None = 0
        Manual = 1
        Auto = 2
    

class SuppressByExpressionBuilder(Builder):
    def __init__(self) -> None: ...
    FeatureList: Features.SelectFeatureList
    SuppressAction: SuppressByExpressionBuilder.ExpressionAction


    class ExpressionAction(enum.Enum):
        CreateEach = 0
        CreateShared = 1
        DeleteEach = 2
        DeleteShared = 3
    

class SubdivisionTaskEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Enter(self) -> None:
        ...
    def Exit(self) -> None:
        ...
    def SetFeatureToEdit(self, subdivisionBodyFeature: Features.Subdivision.SubdivisionBody) -> None:
        ...
    def SetCancelled(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveSubdivisionBodyFeature: Features.Subdivision.SubdivisionBody


class SubdivisionMeshVertex(DisplayableObject):
    def __init__(self) -> None: ...
    def GetBody(self) -> SubdivisionMeshBody:
        ...
    def GetFaces(self) -> typing.List[SubdivisionMeshFace]:
        ...
    def GetEdges(self) -> typing.List[SubdivisionMeshEdge]:
        ...
    Coordinates: Point3d


class SubdivisionMeshFace(DisplayableObject):
    def __init__(self) -> None: ...
    def GetBody(self) -> SubdivisionMeshBody:
        ...
    def GetEdges(self) -> typing.List[SubdivisionMeshEdge]:
        ...
    def GetVertices(self) -> typing.List[SubdivisionMeshVertex]:
        ...


class SubdivisionMeshEdge(DisplayableObject):
    def __init__(self) -> None: ...
    def GetBody(self) -> SubdivisionMeshBody:
        ...
    def GetFaces(self) -> typing.List[SubdivisionMeshFace]:
        ...
    def GetVertices(self, vertex1: SubdivisionMeshVertex, vertex2: SubdivisionMeshVertex) -> None:
        ...


class SubdivisionMeshBody(DisplayableObject):
    def __init__(self) -> None: ...
    def GetFaces(self) -> typing.List[SubdivisionMeshFace]:
        ...
    def GetEdges(self) -> typing.List[SubdivisionMeshEdge]:
        ...
    def GetVertices(self) -> typing.List[SubdivisionMeshVertex]:
        ...


class StudioMaterialManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def ImportMaterial(self, materialFilename: str, materialNames: str) -> None:
        ...
    def Tag(self) -> Tag: ...



class StrokeCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Stroke]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Stroke:
        ...
    def Tag(self) -> Tag: ...



class Stroke(Polyline):
    def __init__(self) -> None: ...
    def GetSpeeds(self) -> float:
        ...


class STLImporter(Importer):
    def __init__(self) -> None: ...
    AngularTolerance: STLImporter.AngularToleranceType
    DisplayInformation: bool
    FileFormat: STLImporter.FileFormatType
    FileUnits: STLImporter.FileUnitsType
    HideSmoothEdges: bool


    class FileUnitsType(enum.Enum):
        Meters = 0
        Millimeters = 1
        Inches = 2
    

    class FileFormatType(enum.Enum):
        Ascii = 0
        Binary = 1
    

    class AngularToleranceType(enum.Enum):
        Coarse = 0
        Medium = 1
        Fine = 2
    

class STLCreator(BaseCreator):
    def __init__(self) -> None: ...
    AdjacencyTol: float
    AngularTol: float
    AutoNormalGen: bool
    ChordalTol: float
    ErrorMessageDisplay: bool
    ExportSelectionBlock: SelectNXObjectList
    HeaderInfo: str
    NormalDirectionIndicator: int
    NormalDisplay: bool
    OutputType: STLCreator.OutputTypeEnum
    ReferenceSurfaceSelectionBlock: SelectNXObjectList
    ReverseNormalDirection: bool
    SheetBodyExportOption: STLCreator.SheetBodyExportOptionEnum
    TriangleDisplay: bool


    class SheetBodyExportOptionEnum(enum.Enum):
        IndividualSheets = 0
        JoinSheets = 1
    

    class OutputTypeEnum(enum.Enum):
        Binary = 0
        Text = 1
    

class StepCreator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    AssemblyValidationProperties: bool
    Author: str
    Authorization: str
    BsplineTol: float
    CloudOfPointsProperties: bool
    ColorAndLayers: bool
    Company: str
    Description: str
    EntityNames: StepCreator.EntityNameOption
    ExportAs: StepCreator.ExportAsOption
    ExportConvergentAs: StepCreator.ExportConvergentAsOption
    ExportExtRef: bool
    ExportExtRefStructureAs: StepCreator.ExternalReferenceStructureOption
    ExportFrom: StepCreator.ExportFromOption
    ExportSelectionBlock: ObjectSelector
    ExportSolidsAndSurfacesAs: StepCreator.ExportSolidsAndSurfacesAsOption
    FileSaveFlag: bool
    GeometricValidationProperties: bool
    InputFile: str
    KinematicApp: str
    LayerMask: str
    ObjectTypes: ObjectTypeSelector
    PMIValidationProperties: bool
    SettingsFile: str
    SystemAttributes: bool
    UserDefinedAttributes: bool
    ValidationProperties: bool


    class ExternalReferenceStructureOption(enum.Enum):
        Basic = 0
        Nested = 1
    

    class ExportSolidsAndSurfacesAsOption(enum.Enum):
        Precise = 0
        Tessellated = 1
    

    class ExportFromOption(enum.Enum):
        DisplayPart = 0
        ExistingPart = 1
    

    class ExportConvergentAsOption(enum.Enum):
        SplitPreciseAndTessellated = 0
        Tessellated = 1
    

    class ExportAsOption(enum.Enum):
        Ap203 = 0
        Ap214 = 1
        Ap242 = 2
        Ap242ED2 = 3
    

    class EntityNameOption(enum.Enum):
        LongName = 0
        ShortName = 1
    

class Step242Importer(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    FileOpenFlag: bool
    FlattenAssembly: bool
    ImportTo: Step242Importer.ImportToOption
    ImportToTeamcenter: bool
    Messages: Step242Importer.MessageEnum
    ObjectTypes: ObjectTypeSelector
    Optimize: bool
    SettingsFile: str
    SewSurfaces: bool
    SimplifyGeometry: bool
    SmoothBSurfaces: bool


    class MessageEnum(enum.Enum):
        None = 0
        Informational = 1
        Warning = 2
        Error = 3
        Debug = 4
        All = 5
    

    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

class Step214Importer(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    FileOpenFlag: bool
    FlattenAssembly: bool
    ImportTo: Step214Importer.ImportToOption
    ImportToTeamcenter: bool
    LayerDefault: int
    ObjectTypes: ObjectTypeSelector
    Optimize: bool
    SettingsFile: str
    SewSurfaces: bool
    SimplifyGeometry: bool
    SmoothBSurfaces: bool


    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

class Step203Importer(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    FileOpenFlag: bool
    FlattenAssembly: bool
    ImportTo: Step203Importer.ImportToOption
    ImportToTeamcenter: bool
    LayerDefault: int
    ObjectTypes: ObjectTypeSelector
    Optimize: bool
    SettingsFile: str
    SewSurfaces: bool
    SimplifyGeometry: bool
    SmoothBSurfaces: bool


    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

class SpringJoint(Joint):
    def __init__(self, pItem: int) -> None: ...
    AttachVector: VectorArithmetic.Vector3
    BaseVector: VectorArithmetic.Vector3
    SpringConstant: float
    Damping: float
    RelaxedPosition: float


class SpringDamper(AxisConstraint):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Axis: AxisJoint
    SpringConstant: float
    Damping: float
    RelaxedPosition: float


    class SpringDamper.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class SpreadsheetManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def ReadCell(self, filename: str, cell: str) -> SpreadsheetCellData:
        ...
    def ReadAny(self, filename: str, cell: str) -> SpreadsheetCellData:
        ...
    def HorizontalLookup(self, file: str, target: str, range: str, offset: int, mode: SpreadsheetManager.LookupMode) -> SpreadsheetCellData:
        ...
    def VerticalLookup(self, file: str, target: str, range: str, offset: int, mode: SpreadsheetManager.LookupMode) -> SpreadsheetCellData:
        ...
    def OpenFile(self, sheet: str, mode: SpreadsheetManager.OpenMode) -> SpreadsheetExternal:
        ...
    def ExportFile(self, partnum: str) -> str:
        ...
    def Open(self, sheettype: SpreadsheetManager.Sheettype, partfile: str) -> Spreadsheet:
        ...
    def CreateCellData(self) -> SpreadsheetCellData:
        ...
    def Tag(self) -> Tag: ...



    class Sheettype(enum.Enum):
        Gateway = 0
        Modeling = 1
        Partfamily = 2
    

    class OpenMode(enum.Enum):
        Read = 0
        Write = 1
    

    class LookupMode(enum.Enum):
        Exact = 0
        Higher = 1
        Lower = 2
        Closest = 3
    

class SpreadsheetExternal(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def CloseFile(self, save: bool) -> None:
        ...
    def GetWorksheetIndex(self, sheetname: str) -> int:
        ...
    def ReadNamedRange(self, worksheet: int, rangename: str, v2: typing.List[SpreadsheetCellData]) -> None:
        ...
    def ReadRange(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, v2: typing.List[SpreadsheetCellData]) -> None:
        ...
    def AppendRow(self, worksheet: int, data: typing.List[SpreadsheetCellData]) -> None:
        ...
    def WriteRange(self, data: typing.List[SpreadsheetCellData]) -> None:
        ...
    def SetRangeBackgroundColor(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, cellBackgroundColor: float) -> None:
        ...
    def SetSheetTabBackgroundColor(self, worksheet: int, tabBackgroundColor: float) -> None:
        ...
    def MergeCellRange(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int) -> None:
        ...
    def SetWorksheetName(self, worksheet: int, sheetname: str) -> None:
        ...
    def AddWorksheet(self, sheetname: str) -> int:
        ...
    def SetRangeAlignment(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, alignStyle: AlignmentStyleT, alignMode: TextAlignmentModeT) -> None:
        ...
    def SetRangeBordersProperty(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, cellBorderColor: float, borderLineStyle: BorderLineStyleT) -> None:
        ...
    def SetRangeFontProperty(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, fontName: str, fontSize: int, cellFontColor: float, bold: bool, italic: bool, underline: UnderlineStyleT, strikethrough: bool, superscript: bool, subscript: bool) -> None:
        ...
    def SaveAs(self, worksheet: int, fileName: str, fileFormat: ExcelFileFormatT) -> None:
        ...
    def InsertImage(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, imagepath: str) -> None:
        ...
    def AutofitColumns(self, worksheet: int, colstart: int, colend: int) -> None:
        ...
    def GetNumberofsheets(self) -> int:
        ...
    def DeleteRow(self, worksheet: int, rownumber: int) -> None:
        ...
    def DeleteColumn(self, worksheet: int, columnnumber: int) -> None:
        ...
    def DeleteRange(self, worksheet: int, columnstart: int, columnend: int, rowstart: int, rowend: int) -> None:
        ...
    def ReadSpreadsheetRange(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, v2: typing.List[SpreadsheetCellData]) -> None:
        ...
    def WriteSpreadsheetRange(self, worksheet: int, rowstart: int, colstart: int, rowend: int, colend: int, data: typing.List[SpreadsheetCellData]) -> None:
        ...
    def GetWorksheetNames(self, sheetnames: str) -> None:
        ...


class SpreadsheetCellData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    DoubleValue: float
    FormulaValue: str
    IntValue: int
    LogicalValue: bool
    StringValue: str
    Type: SpreadsheetCellData.Types


    class Types(enum.Enum):
        Int = 0
        Double = 1
        String = 2
        Logical = 3
        Formula = 4
    

class Spreadsheet(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNumber(self, row: int, col: int, sheet: int) -> SpreadsheetCellData:
        ...
    def GetFormula(self, row: int, col: int, sheet: int) -> SpreadsheetCellData:
        ...
    def GetNumberOfSheets(self) -> int:
        ...
    def GetSheetNumber(self) -> int:
        ...
    def GetSheetNumberOfName(self, sheetname: str) -> int:
        ...
    def GetString(self, row: int, col: int, sheet: int) -> SpreadsheetCellData:
        ...
    def GetValue(self, row: int, col: int, sheet: int) -> SpreadsheetCellData:
        ...
    def SetFormula(self, row: int, col: int, cellvalue: SpreadsheetCellData, sheet: int) -> None:
        ...
    def SetNumber(self, row: int, col: int, cellvalue: SpreadsheetCellData, sheet: int) -> None:
        ...
    def SetSheetNumber(self, sheet: int) -> None:
        ...
    def SetString(self, row: int, col: int, cellvalue: SpreadsheetCellData, sheet: int) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Delete(self, start1: int, end1: int, sheet: int, operation: int) -> None:
        ...
    def DeleteSheets(self, sheet: int, count: int) -> None:
        ...
    def EraseRange(self, row0: int, col0: int, row1: int, col1: int, sheet0: int, sheet1: int) -> None:
        ...
    def EvaluateCell(self, row: int, col: int, sheet: int) -> SpreadsheetCellData:
        ...
    def InsertSheets(self, sheet: int, count: int) -> None:
        ...
    def Terminate(self) -> None:
        ...
    def Save(self) -> None:
        ...
    def Recalculate(self) -> None:
        ...
    def GetSheetNames(self, sheetnames: str) -> None:
        ...
    def GetNamedRange(self, rangename: str, namedrange: int) -> None:
        ...
    def SetNamedRange(self, rangename: str, row0: int, col0: int, row1: int, col1: int, sheet: int) -> None:
        ...


class SplineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Spline]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Spline:
        ...
    def Tag(self) -> Tag: ...



class Spline(Curve):
    def __init__(self) -> None: ...
    def GetKnots(self) -> float:
        ...
    def GetPoles(self) -> typing.List[Point4d]:
        ...
    def Get3DPoles(self) -> typing.List[Point3d]:
        ...
    Order: int
    Periodic: bool
    PoleCount: int
    Rational: bool


class SphericalCoordinateSystem(CoordinateSystem):
    def __init__(self) -> None: ...


class SpeedControl(ControlBase):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Axis: AxisJoint
    Surface: TransportSurface
    VirtualJoint: VirtualAxis
    Speed: float
    Position: float
    LimitAcceleration: bool
    Acceleration: float
    LimitJerk: bool
    Jerk: float
    LimitForceTorque: bool
    LimitForceTorqueForward: float
    LimitForceTorqueReverse: float


    class SpeedControl.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class SpeechRecognitionMock(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetSpeechRecognitionMock(self, owner: Session) -> SpeechRecognitionMock:
        ...
    def InvokeMockSpeechRecognition(self, isSpecialKeyword: bool) -> None:
        ...
    def SetMockTranscribedText(self, mockTranscribedText: str) -> None:
        ...
    def GetLaunchedCommandTitle(self) -> str:
        ...
    def Tag(self) -> Tag: ...



class SourceBehavior(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Active: bool


    class SourceBehavior.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class SmartObject(DisplayableObject):
    def __init__(self) -> None: ...
    def RemoveParameters(self) -> None:
        ...
    def ReplaceParameters(self, otherSo: SmartObject) -> None:
        ...
    def Evaluate(self) -> None:
        ...
    def SetVisibility(self, visibility: SmartObject.VisibilityOption) -> None:
        ...
    def ProtectFromDelete(self) -> None:
        ...
    def ReleaseDeleteProtection(self) -> None:
        ...
    Update: SmartObject.UpdateOption
    Visibility: SmartObject.VisibilityOption


    class VisibilityOption(enum.Enum):
        Invisible = 0
        Visible = 1
        VisibleIfParentInvisible = 2
    

    class UpdateOption(enum.Enum):
        DontUpdate = 0
        WithinModeling = 1
        AfterModeling = 2
        AfterParentBody = 3
        Mixed = 4
    

class SlidingJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    def GetVelocity(self) -> float:
        ...
    Attach: RigidBody
    Base: RigidBody
    Axis: VectorArithmetic.Vector3
    Position: float
    Active: bool


    class SlidingJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class SketchWorkRegionBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryObjects: SelectTaggedObjectList
    Scope: SketchWorkRegionBuilder.ScopeType
    WorkRegionObjects: SelectTaggedObjectList


    class ScopeType(enum.Enum):
        SelectedObjects = 0
        EntireSketch = 1
    

class SketchVirtualPoint(Point):
    def __init__(self) -> None: ...
    def GetParentCurves(self) -> typing.List[Curve]:
        ...
    def RemoveParentCurve(self, parentCurve: Curve) -> None:
        ...
    def ConvertToRegularPoint(self) -> None:
        ...
    def UpdatePosition(self, position: Point3d) -> None:
        ...


class SketchTangentToStringConstraint(SketchHelpedGeometricConstraint):
    def __init__(self) -> None: ...
    def UseAlternateSolution(self) -> None:
        ...


class SketchTangentConstraint(SketchHelpedGeometricConstraint):
    def __init__(self) -> None: ...
    def UseAlternateSolution(self) -> None:
        ...


class SketchSymmetricBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...
    CenterLine: SelectNXObject
    ConvertCenterlineToReference: bool


class SketchRelation(DisplayableObject):
    def __init__(self) -> None: ...


class SketchRapidDimensionBuilder(Annotations.BaseRapidDimensionBuilder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder


class SketchRadialDimensionBuilder(Annotations.BaseRadialDimensionBuilder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder


class SketchQuickTrimBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryCurves: SelectCurveList
    BoundaryObjects: SelectNXObjectList
    ExtendBound: bool
    TrimmedCurves: SelectCurveList


class SketchQuickExtendBuilder(Builder):
    def __init__(self) -> None: ...
    BoundaryCurves: SelectCurveList
    BoundaryObjects: SelectNXObjectList
    ExtendBound: bool
    ExtendedCurves: SelectCurveList


class SketchProjectBuilder(Features.EmbeddedOperationBuilder):
    def __init__(self) -> None: ...
    Associativity: bool
    CurveList: SelectNXObjectList
    CurveType: SketchProjectBuilder.OutputCurve
    ProjectAsDumbFixedCurves: bool
    Section: Section
    Tolerance: float


    class OutputCurve(enum.Enum):
        Original = 0
        SplineSegment = 1
        SingleSpline = 2
    

class SketchPolygonBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateLengthDimension(self, createDim: bool) -> None:
        ...
    def CreateRadiusDimension(self, createDim: bool) -> None:
        ...
    def CreateAngleDimension(self, createDim: bool) -> None:
        ...
    CenterPoint: Point
    CreateConstraint: bool
    LengthDimension: Expression
    NumberOfSides: int
    RadiusDimension: Expression
    RotationDimension: Expression
    Size: SketchPolygonBuilder.SizeType
    SizePoint: Point


    class SizeType(enum.Enum):
        InscribedRadius = 0
        CircumscribedRadius = 1
        SideLength = 2
    

class SketchPolygon(SketchGeometricConstraint):
    def __init__(self) -> None: ...


class SketchPatternBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEndConstraint(self, parent: NXObject, inx: int, isStart: bool, constraint: bool) -> None:
        ...
    def UpdateCopies(self) -> None:
        ...
    def UpdateInputSection(self) -> None:
        ...
    def UpdateLinearDirectionObject(self) -> None:
        ...
    def UpdateCenterPoint(self) -> None:
        ...
    def UpdateRectangularDirectionObjects(self) -> None:
        ...
    def UpdateFromPoint(self) -> None:
        ...
    def EvaluatePattern(self) -> None:
        ...
    def UpdateData(self) -> None:
        ...
    def HandleFlip(self) -> None:
        ...
    CreateConstraint: bool
    CreateSpacingExp: bool
    LockOrientation: bool
    PatternService: GeometricUtilities.PatternDefinition
    Section: Section


class SketchPattern(SketchGeometricConstraint):
    def __init__(self) -> None: ...
    PatternType: SketchPattern.Type


    class Type(enum.Enum):
        Linear = 0
        Circular = 1
        Mirror = 2
        Rectangular = 3
        General = 4
    

    class InstanceControl(enum.Enum):
        FullCircle = 0
        NumberOffset = 1
    

class SketchPasteBuilder(Builder):
    def __init__(self) -> None: ...
    def ResetInitialPasteLocation(self) -> None:
        ...
    InitialPasteLocation: Point3d
    MoveObject: Features.MoveObjectBuilder


class SketchOperationData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetConfigurationData(self, configurationDataSize: int) -> str:
        ...
    def GetGeometryData(self, geometryData: typing.List[SketchOperationData.GeometryData]) -> None:
        ...


    class SketchOperationDataGeometryData():
        GeometryTag: NXObject
        GeometryString: str
        def ToString(self) -> str:
            ...
        def __init__(self, GeometryTag: NXObject, GeometryString: str) -> None: ...
    

    class SketchOperationData_GeometryData():
        geometryTag: Tag
        geometryString: int
    

class SketchOperationBuilder(Builder):
    def __init__(self) -> None: ...
    def FindRelations(self) -> typing.List[SketchFoundRelation]:
        ...
    def SetRelationRelaxState(self, relation: SketchRelation, relax: bool) -> None:
        ...
    def RestoreOperation(self) -> None:
        ...
    def ExportSolverConfiguration(self, numStringSize: int) -> str:
        """[Obsolete("Deprecated in NX2007.0.0.  Use NXOpen.SketchOperationBuilder.ExportOperationData instead.")"""
        ...
    def ExportOperationData(self) -> SketchOperationData:
        ...


class SketchOffsetBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateSection(self) -> Section:
        ...
    def RemoveSection(self, section: Section) -> None:
        ...
    def ReverseOffsetDirectionOfChain(self, objectInChain: NXObject) -> None:
        ...
    def ReverseOffsetDirection(self) -> None:
        ...
    def BreakChain(self, object1: NXObject, object2: NXObject, helpPt: Point3d) -> None:
        ...
    def MergeChains(self, object1: NXObject, object2: NXObject, helpPt: Point3d) -> None:
        ...
    def SetEndConstraint(self, objectInChain: NXObject, inx: int, isStartEnd: bool, constraint: bool) -> None:
        ...
    def GetOutputCurvesOfOffset(self) -> typing.List[NXObject]:
        ...
    def GetSections(self) -> typing.List[Section]:
        ...
    def UpdateLoopsAndCopies(self) -> None:
        ...
    def EvaluateOffset(self) -> None:
        ...
    def UpdateSolverDistance(self) -> None:
        ...
    def UpdateSymmetry(self) -> None:
        ...
    CapType: SketchOffset.CapType
    ConvertToReference: bool
    CreateConstraint: bool
    CreateDimension: bool
    Degree: int
    Distance: Expression
    IsSymmetric: bool
    NumberOfCopies: int
    Tolerance: float


class SketchOffset(SketchGeometricConstraint):
    def __init__(self) -> None: ...
    def UpdateDistance(self, dist: float) -> None:
        ...


    class CapType(enum.Enum):
        Extension = 0
        Arc = 1
    

class SketchMirrorPatternBuilder(Builder):
    def __init__(self) -> None: ...
    def SetEndConstraint(self, parent: NXObject, isStart: bool, constraint: bool) -> None:
        ...
    def UpdateDirectionObject(self) -> None:
        ...
    def UpdateInputSection(self) -> None:
        ...
    ConvertToReference: bool
    CreateConstraint: bool
    DirectionObject: SelectNXObject
    Section: Section


class SketchManageSymmetryLinesBuilder(Builder):
    def __init__(self) -> None: ...
    def ChangeSymmetryLineStatus(self, symmetryLine: NXObject, isActivated: bool) -> None:
        ...
    ObjectSelected: SelectNXObject


class SketchMakeVerticalBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeUniformScaleBuilder(Builder):
    def __init__(self) -> None: ...
    SplinesToConstrain: SelectSketchMakeUniformScaleBuilderList


class SketchMakeTangentToStringBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeTangentBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeSymmetricBuilder(Builder):
    def __init__(self) -> None: ...
    CenterLine: SelectNXObject
    ConvertToReference: bool
    PrimaryObject: SelectNXObject
    SecondaryObject: SelectNXObject


class SketchMakeRelationBuilder(SketchOperationBuilder):
    def __init__(self) -> None: ...
    def SetCreateConstraints(self, createConstaints: bool) -> None:
        ...
    def ClearCurrentOperation(self) -> None:
        ...
    LockObjects: SelectNXObjectList
    LockPoints: SelectNXObjectList
    MotionObjects: SelectNXObjectList
    MotionPoints: SelectNXObjectList
    StationaryObject: SelectNXObject


    class RelationTypes(enum.Enum):
        Coincident = 0
        Collinear = 1
        Horizontal = 2
        Vertical = 3
        Parallel = 4
        Perpendicular = 5
        EqualLength = 6
        EqualRadius = 7
        Symmetric = 8
        Tangent = 9
        MidpointAligned = 10
        PointOnString = 11
        TangentToString = 12
        PerpendicularToString = 13
    

class SketchMakePointOnStringBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakePerpendicularToStringBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakePerpendicularBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeParallelBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeMidpointAlignedBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeHorizontalBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeEqualBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...
    EqualType: SketchMakeEqualBuilder.EqualTypes


    class EqualTypes(enum.Enum):
        Radius = 0
        Length = 1
    

class SketchMakeCollinearBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchMakeCoincidentBuilder(SketchMakeRelationBuilder):
    def __init__(self) -> None: ...


class SketchLineBuilder(Builder):
    def __init__(self) -> None: ...
    def GetPreviewGeometry(self) -> Line:
        ...
    def SetStartPoint(self, startPoint: Point3d) -> None:
        ...
    def SetSnapTarget(self, snapTarget: NXObject) -> None:
        ...
    def SetSnapPointTarget(self, snapTarget: NXObject, snapHelpPoint: Point3d) -> None:
        ...
    def SetEndPoint(self, endPoint: Point3d) -> None:
        ...
    def LockDirectionalSnapRelations(self) -> None:
        ...
    def UnlockDirectionalSnapRelations(self) -> None:
        ...
    SnapEnabled: bool
    SnapRadius: float


class SketchLinearDimensionBuilder(Annotations.BaseLinearDimensionBuilder):
    def __init__(self) -> None: ...
    def ConvertToHalfDiameter(self, updateStyle: bool) -> None:
        ...
    def ConvertFromHalfDiameter(self, updateStyle: bool) -> None:
        ...
    Driving: Annotations.DrivingValueBuilder


class SketchIntersectionPointBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def UpdateData(self) -> None:
        ...
    def Cycle(self) -> None:
        ...
    Associative: bool
    Rail: Section


class SketchIntersectionPoint(Features.Feature):
    def __init__(self) -> None: ...


class SketchIntersectionCurveBuilder(Features.FeatureBuilder):
    def __init__(self) -> None: ...
    def CollectorUpdated(self) -> None:
        ...
    def AlternateSolution(self, solutionIndex: int) -> None:
        ...
    def CurveFitMethodUpdated(self) -> None:
        ...
    def GetOldAndNewOutputCurves(self, oldOutputCurves: typing.List[NXObject], newOutputCurves: typing.List[NXObject]) -> None:
        ...
    def MapOutputCurve(self, oldOutputCurve: NXObject, newOutputCurve: NXObject) -> None:
        ...
    AngleTolerance: float
    Associative: bool
    CurveFitMethod: GeometricUtilities.CurveFitOptions
    DistanceTolerance: float
    FaceCollector: ScCollector
    IgnoreHoles: bool
    JoinCurves: bool


class SketchIntersectionCurve(Features.Feature):
    def __init__(self) -> None: ...


class SketchInPlaceBuilder(Builder):
    def __init__(self) -> None: ...
    Axis: SelectIReferenceAxis
    AxisOrientation: AxisOrientation
    AxisOrientationInfer: AxisOrientation
    AxisReference: Direction
    CreateIntermediateDatumCsys: bool
    Csystem: CartesianCoordinateSystem
    MakeOriginAssociative: bool
    OriginOption: OriginMethod
    OriginOptionInfer: OriginMethod
    Plane: Plane
    PlaneOption: Sketch.PlaneOption
    PlaneOrFace: SelectISurface
    PlaneReference: Plane
    ProjectWorkPartOrigin: bool
    ReverseAxis: bool
    ReversePlaneNormal: bool
    SketchOrigin: Point


class SketchInDraftingBuilder(Builder):
    def __init__(self) -> None: ...
    View: SelectView


class SketchIncludeGeometryBuilder(Builder):
    def __init__(self) -> None: ...
    ObjectsToInclude: SelectNXObjectList


class SketchIgnoreRelationBuilder(SketchOperationBuilder):
    def __init__(self) -> None: ...
    GeometryOrDimension: SelectNXObject
    RelationsToIgnore: SelectNXObjectList


class SketchHelpedGeometricConstraint(SketchGeometricConstraint):
    def __init__(self) -> None: ...
    def GetHelpData(self, hasHelpPoint1: bool, hasHelpPoint2: bool, hasHelpParameter1: bool, hasHelpParameter2: bool, helpPoint1: Point3d, helpPoint2: Point3d, helpParameter1: float, helpParameter2: float) -> None:
        ...
    def SetHelpPoints(self, hasHelp1: bool, hasHelp2: bool, helpPoint1: Point3d, helpPoint2: Point3d) -> None:
        ...
    def SetHelpParameters(self, hasHelp1: bool, hasHelp2: bool, helpParameter1: float, helpParameter2: float) -> None:
        ...


class SketchHelpedDimensionalConstraint(SketchDimensionalConstraint):
    def __init__(self) -> None: ...
    def GetHelpData(self, hasHelpPoint1: bool, hasHelpPoint2: bool, hasHelpParameter1: bool, hasHelpParameter2: bool, helpPoint1: Point3d, helpPoint2: Point3d, helpParameter1: float, helpParameter2: float) -> None:
        ...
    def SetHelpPoints(self, hasHelp1: bool, hasHelp2: bool, helpPoint1: Point3d, helpPoint2: Point3d) -> None:
        ...
    def SetHelpParameters(self, hasHelp1: bool, hasHelp2: bool, helpParameter1: float, helpParameter2: float) -> None:
        ...


class SketchGeometricConstraint(SketchConstraint):
    def __init__(self) -> None: ...
    def GetGeometry(self) -> typing.List[Sketch.ConstraintGeometry]:
        ...
    IsInferred: bool


class SketchG2Constraint(SketchGeometricConstraint):
    def __init__(self) -> None: ...
    CurvatureGeometry: Curve
    IsFixedMagnitude: bool
    Spline: Spline


class SketchG1Constraint(SketchGeometricConstraint):
    def __init__(self) -> None: ...
    ConstraintSlopeType: SketchG1Constraint.SlopeType
    IsFixedMagnitude: bool
    Spline: Spline
    TangentGeometry: Curve


    class SlopeType(enum.Enum):
        Tangent = 0
        Normal = 1
    

class SketchFoundRelation(SketchRelation):
    def __init__(self) -> None: ...
    def GetGeometry(self) -> typing.List[Sketch.ConstraintGeometry]:
        ...
    def GetHelpData(self, helpPoint1: Point3d, helpPoint2: Point3d, helpParameter1: float, helpParameter2: float) -> None:
        ...
    def MakeIgnored(self) -> None:
        ...
    IsIgnored: bool
    Type: Sketch.ConstraintType


class SketchFixObjectsBuilder(Builder):
    def __init__(self) -> None: ...
    def AddObject(self, fixObject: Sketch.ConstraintGeometry) -> None:
        ...
    def RemoveObject(self, fixObject: Sketch.ConstraintGeometry) -> None:
        ...
    def GetObjects(self) -> typing.List[Sketch.ConstraintGeometry]:
        ...
    FixObjects: SelectTaggedObjectList


class SketchFindMovableObjectsBuilder(Builder):
    def __init__(self) -> None: ...


class SketchExpressionModifierBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Exp1: Expression
    Exp10: Expression
    Exp11: Expression
    Exp12: Expression
    Exp2: Expression
    Exp3: Expression
    Exp4: Expression
    Exp5: Expression
    Exp6: Expression
    Exp7: Expression
    Exp8: Expression
    Exp9: Expression
    Sketch: Sketch
    Sketches: SketchExpressionModifierBuilder.EndCuts


    class EndCuts(enum.Enum):
        EndCut1 = 0
        EndCut2 = 1
    

class SketchEvaluatorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[SketchEvaluator]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, varsweep: Features.Feature) -> SketchEvaluator:
        ...
    def Tag(self) -> Tag: ...



class SketchEvaluator(TaggedObject):
    def __init__(self) -> None: ...
    def EvaluateOneSketch(self, pathLocation: float) -> typing.List[Curve]:
        ...
    def Destroy(self) -> None:
        ...
    AngularTolerance: float
    CreateCurveOption: bool
    DistanceTolerance: float
    Section: Section
    SimplifyCurveOption: bool


class SketchEllipseBuilder(Builder):
    def __init__(self) -> None: ...
    def HandleComplement(self) -> None:
        ...
    CenterPoint: Point
    Closed: bool
    EndAngle: Expression
    MajorPoint: Point
    MajorRadius: Expression
    MinorPoint: Point
    MinorRadius: Expression
    RotationAngle: Expression
    StartAngle: Expression


class SketchEditParametersBuilder(SketchOperationBuilder):
    def __init__(self) -> None: ...
    def Evaluate(self, dimensionTag: Annotations.Dimension, newValue: float) -> None:
        ...


class SketchEditDimensionValueBuilder(SketchOperationBuilder):
    def __init__(self) -> None: ...
    def LoadExtraGeometry(self) -> None:
        ...
    DimValue: float
    Expression: Expression
    ExtraGeometries: SelectNXObjectList


class SketchEditDefiningSectionBuilder(Builder):
    def __init__(self) -> None: ...
    AllSectionList: SectionList


class SketchDragGeometryBuilder(SketchOperationBuilder):
    def __init__(self) -> None: ...
    def GetDragGeometry(self, dragObjects: typing.List[Sketch.SketchGeometry]) -> None:
        ...
    def SetDragGeometry(self, dragObjects: typing.List[Sketch.SketchGeometry]) -> None:
        ...
    def InitializeDrag(self, initialPosition: Point3d) -> None:
        ...
    def SetSnapTarget(self, snapTarget: NXObject) -> None:
        ...
    def SetSnapPointTarget(self, snapTarget: NXObject, snapHelpPoint: Point3d) -> None:
        ...
    def DragToPoint(self, newPosition: Point3d) -> None:
        ...
    def DetachGeometry(self) -> None:
        ...
    SnapEnabled: bool
    SnapGeometry: Sketch.SketchGeometry
    SnapRadius: float
    SnapToGridOffset: Vector3d
    SplineLinearScale: bool


class SketchDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    ExpressionOption: SketchDimensionBuilder.ExpOption
    FirstGeometry: SelectNXObject
    SecondGeometry: SelectNXObject
    SnapRadius: float


    class ExpOption(enum.Enum):
        KeepExpression = 0
        MeasureGeometry = 1
    

class SketchDimensionalConstraint(SketchConstraint):
    def __init__(self) -> None: ...
    def GetDimensionGeometry(self) -> typing.List[Sketch.DimensionGeometry]:
        ...
    def UseAlternateSolution(self) -> None:
        ...
    def SetAsDriving(self) -> None:
        ...
    def RemoveDrivingExpression(self) -> None:
        ...
    def EditDimensionValue(self, newDimValue: float) -> None:
        ...
    def SetEndBehaviorPreference(self, preference: SketchDimensionalConstraint.EndBehaviorPreference) -> None:
        ...
    def AlternateAngle(self) -> None:
        ...
    AssociatedDimension: Annotations.Dimension
    AssociatedExpression: Expression
    DimensionState: SketchDimensionalConstraint.DimensionStateType


    class EndBehaviorPreference(enum.Enum):
        Any = 0
        Geometry1Moves = 1
        Geometry2Moves = 2
    

    class DimensionStateType(enum.Enum):
        Driving = 0
        Reference = 1
        Automatic = 2
        Constant = 3
    

class SketchDefineWorkRegionBuilder(Builder):
    def __init__(self) -> None: ...
    Scope: SketchDefineWorkRegionBuilder.ScopeType
    WorkRegionObjects: ScCollector


    class ScopeType(enum.Enum):
        SelectedObjects = 0
        EntireSketch = 1
    

class SketchCornerBuilder(Builder):
    def __init__(self) -> None: ...
    Curves: SelectCurveList


class SketchConstraintBuilder(Builder):
    def __init__(self) -> None: ...
    Centerline: SelectNXObject
    ConstraintType: SketchConstraintBuilder.Constraint
    GeometryToConstrain: SelectNXObjectList
    GeometryToConstrainTo: SelectNXObject
    MakeReference: bool
    UpdateSketchAtCommit: bool


    class Constraint(enum.Enum):
        Coincident = 0
        PointOnCurve = 1
        Tangent = 2
        Parallel = 3
        Perpendicular = 4
        Horizontal = 5
        Vertical = 6
        HorizontalAlignment = 7
        VerticalAlignment = 8
        Midpoint = 9
        Collinear = 10
        Concentric = 11
        EqualLength = 12
        EqualRadius = 13
        Symmetric = 14
        Fixed = 15
        FullyFixed = 16
        ConstantAngle = 17
        ConstantLength = 18
        PointOnString = 19
        TangentToString = 20
        PerpendicularToString = 21
        NonUniformScale = 22
        UniformScale = 23
        SlopeOfCurve = 24
    

class SketchConstraint(SketchRelation):
    def __init__(self) -> None: ...
    def RefreshDimension(self) -> None:
        ...
    def Refresh(self) -> None:
        ...
    ConstraintType: Sketch.ConstraintType


class SketchConicBuilder(Builder):
    def __init__(self) -> None: ...
    ControlPoint: Point
    EndPoint: Point
    Rho: float
    StartPoint: Point


class SketchCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Sketch]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> Sketch:
        ...
    def GetOwningSketch(self, geometry: SmartObject) -> Sketch:
        ...
    def CreateIntersectionCurveBuilder(self, operation: SketchIntersectionCurve) -> SketchIntersectionCurveBuilder:
        ...
    def CreateIntersectionPointBuilder(self, operation: SketchIntersectionPoint) -> SketchIntersectionPointBuilder:
        ...
    def CreateProjectBuilder(self, operation: Features.Feature) -> SketchProjectBuilder:
        ...
    def CreateCornerBuilder(self) -> SketchCornerBuilder:
        ...
    def CreateAutoConstrainBuilder(self) -> SketchAutoConstrainBuilder:
        ...
    def CreateSketchOffsetBuilder(self, offCon: SketchOffset) -> SketchOffsetBuilder:
        ...
    def CreateSketchAssociativeTrimBuilder(self, trimCon: SketchAssociativeTrim) -> SketchAssociativeTrimBuilder:
        ...
    def CreateConvertToFromReferenceBuilder(self) -> ConvertToFromReferenceBuilder:
        ...
    def CreateInferredConstraintsBuilder(self) -> InferredConstraintsBuilder:
        ...
    def CreateDimensionBuilder(self, constraint: SketchDimensionalConstraint) -> SketchDimensionBuilder:
        ...
    def CreateQuickExtendBuilder(self) -> SketchQuickExtendBuilder:
        ...
    def CreateQuickTrimBuilder(self) -> SketchQuickTrimBuilder:
        ...
    def CreateNewSketchInPlaceBuilder(self, operation: Sketch) -> SketchInPlaceBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.SketchCollection.CreateSketchInPlaceBuilder2 instead.")"""
        ...
    def CreateSketchInPlaceBuilder2(self, operation: Sketch) -> SketchInPlaceBuilder:
        ...
    def CreateSimpleSketchInPlaceBuilder(self) -> SimpleSketchInPlaceBuilder:
        ...
    def CreateSketchAlongPathBuilder(self, operation: Sketch) -> SketchAlongPathBuilder:
        ...
    def CreateSketchInDraftingBuilder(self) -> SketchInDraftingBuilder:
        ...
    def CreateSketchEllipseBuilder(self, ellipse: NXObject) -> SketchEllipseBuilder:
        ...
    def CreateSketchConicBuilder(self, conic: NXObject) -> SketchConicBuilder:
        ...
    def CreateSketchChamferBuilder(self) -> SketchChamferBuilder:
        ...
    def CreateAutoDimensionBuilder(self) -> SketchAutoDimensionBuilder:
        ...
    def CreateSketchPatternBuilder(self, con: SketchPattern) -> SketchPatternBuilder:
        ...
    def CreateSketchMirrorPatternBuilder(self, con: SketchPattern) -> SketchMirrorPatternBuilder:
        ...
    def CreateMakeSymmetricBuilder(self) -> SketchMakeSymmetricBuilder:
        ...
    def CreateSketchPolygonBuilder(self, polygonconstraint: SketchPolygon) -> SketchPolygonBuilder:
        ...
    def CreateSketchPasteBuilder(self, sketches: typing.List[Sketch]) -> SketchPasteBuilder:
        ...
    def CreateEditDefiningSectionBuilder(self) -> SketchEditDefiningSectionBuilder:
        ...
    def CreateConstraintBuilder(self) -> SketchConstraintBuilder:
        ...
    def CreateAngularDimensionBuilder(self, angularDimension: Annotations.AngularDimension) -> SketchAngularDimensionBuilder:
        ...
    def CreateLinearDimensionBuilder(self, linearDimension: Annotations.Dimension) -> SketchLinearDimensionBuilder:
        ...
    def CreateRapidDimensionBuilder(self) -> SketchRapidDimensionBuilder:
        ...
    def CreateRadialDimensionBuilder(self, radialDimension: Annotations.Dimension) -> SketchRadialDimensionBuilder:
        ...
    def CreateCurveSnapOptionsBuilder(self) -> CurveSnapOptionsBuilder:
        ...
    def CreateRelationFinderSettingsBuilder(self) -> RelationFinderSettingsBuilder:
        ...
    def CreateSketchMakeCoincidentBuilder(self) -> SketchMakeCoincidentBuilder:
        ...
    def CreateSketchMakeCollinearBuilder(self) -> SketchMakeCollinearBuilder:
        ...
    def CreateSketchMakeEqualBuilder(self) -> SketchMakeEqualBuilder:
        ...
    def CreateSketchMakeHorizontalBuilder(self) -> SketchMakeHorizontalBuilder:
        ...
    def CreateSketchMakeMidpointAlignedBuilder(self) -> SketchMakeMidpointAlignedBuilder:
        ...
    def CreateSketchMakeParallelBuilder(self) -> SketchMakeParallelBuilder:
        ...
    def CreateSketchMakePerpendicularBuilder(self) -> SketchMakePerpendicularBuilder:
        ...
    def CreateSketchMakePerpendicularToStringBuilder(self) -> SketchMakePerpendicularToStringBuilder:
        ...
    def CreateSketchMakePointOnStringBuilder(self) -> SketchMakePointOnStringBuilder:
        ...
    def CreateSketchMakeTangentBuilder(self) -> SketchMakeTangentBuilder:
        ...
    def CreateSketchMakeTangentToStringBuilder(self) -> SketchMakeTangentToStringBuilder:
        ...
    def CreateSketchMakeVerticalBuilder(self) -> SketchMakeVerticalBuilder:
        ...
    def CreateSketchSymmetricBuilder(self) -> SketchSymmetricBuilder:
        ...
    def CreateEditDimensionValueBuilder(self, dimension: Annotations.Dimension) -> SketchEditDimensionValueBuilder:
        ...
    def CreateSketchIncludeGeometryBuilder(self, includedObject: SmartObject) -> SketchIncludeGeometryBuilder:
        ...
    def CreateSketchManageSymmetryLinesBuilder(self) -> SketchManageSymmetryLinesBuilder:
        ...
    def CreateDefineWorkRegionBuilder(self) -> SketchDefineWorkRegionBuilder:
        """[Obsolete("Deprecated in NX1980.0.0.  Use NXOpen.SketchWorkRegionBuilder instead.")"""
        ...
    def CreateWorkRegionBuilder(self) -> SketchWorkRegionBuilder:
        ...
    def CreateSketchFixObjectsBuilder(self) -> SketchFixObjectsBuilder:
        ...
    def CreateFindMovableObjectsBuilder(self) -> SketchFindMovableObjectsBuilder:
        ...
    def CreateIgnoreRelationBuilder(self) -> SketchIgnoreRelationBuilder:
        ...
    def CreateSketchMakeUniformScaleBuilder(self) -> SketchMakeUniformScaleBuilder:
        ...
    def CreateEditParametersBuilder(self, operation: Sketch) -> SketchEditParametersBuilder:
        ...
    def CreateDragGeometryBuilder(self) -> SketchDragGeometryBuilder:
        ...
    def CreateLineBuilder(self) -> SketchLineBuilder:
        ...
    def Tag(self) -> Tag: ...



class SketchChamferBuilder(Builder):
    def __init__(self) -> None: ...
    Angle: Expression
    ChamferOption: SketchChamferBuilder.ChamferOptions
    CreateAngleDimension: bool
    CreateDistance1Dimension: bool
    CreateDistance2Dimension: bool
    CurvesToChamfer: SelectDisplayableObjectList
    Distance1: Expression
    Distance2: Expression
    HelpPoint: Point
    TrimInputCurves: bool


    class ChamferOptions(enum.Enum):
        Symmetric = 0
        Asymmetric = 1
        OffsetandAngle = 2
    

class SketchAutoDimensionBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRules(self) -> typing.List[Sketch.AutoDimensioningRule]:
        ...
    def SetRules(self, rules: typing.List[Sketch.AutoDimensioningRule]) -> None:
        ...
    DimensionType: SketchAutoDimensionBuilder.DimType
    SelectionObject: SelectNXObjectList


    class DimType(enum.Enum):
        Driving = 0
        Automatic = 1
    

class SketchAutoConstrainBuilder(Builder):
    def __init__(self) -> None: ...
    def SetAllConstraints(self) -> None:
        ...
    def ClearAllConstraints(self) -> None:
        ...
    AngleTolerance: float
    ApplyRemoteConstraints: bool
    Coincident: bool
    Collinear: bool
    Concentric: bool
    CurveList: SelectObjectList
    DistanceTolerance: float
    EqualLength: bool
    EqualRadius: bool
    Horizontal: bool
    Parallel: bool
    Perpendicular: bool
    PointOnCurve: bool
    Tangent: bool
    Vertical: bool


class SketchAssociativeTrimBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateSection(self) -> Section:
        ...
    def RemoveSection(self, section: Section) -> None:
        ...
    def GetSections(self) -> typing.List[Section]:
        ...
    def SelectRegion(self, helpPoint: Point3d) -> None:
        ...
    def DeselectRegion(self, helpPoint: Point3d) -> None:
        ...
    def UpdateRegions(self) -> None:
        ...
    def ResetRegions(self) -> None:
        ...
    RecipeCurves: SelectNXObjectList
    TrimType: SketchAssociativeTrimBuilder.TrimOption


    class TrimOption(enum.Enum):
        Keep = 0
        Discard = 1
    

class SketchAssociativeTrim(SketchGeometricConstraint):
    def __init__(self) -> None: ...


class SketchAngularDimensionBuilder(Annotations.BaseAngularDimensionBuilder):
    def __init__(self) -> None: ...
    Driving: Annotations.DrivingValueBuilder


class SketchAlongPathBuilder(Builder):
    def __init__(self) -> None: ...
    Axis: SelectIReferenceAxis
    NextThroughPointSolution: float
    OrientingFace: ScCollector
    PlaneLocation: GeometricUtilities.OnPathDimensionBuilder
    PlaneOrientation: SketchAlongPathBuilder.PlaneOrientationType
    PlaneOrientationAxis: Direction
    ReverseAxis: bool
    ReversePlaneNormal: bool
    Section: Section
    ShowAllDatumAxes: bool
    SketchOrient: SketchAlongPathBuilder.SketchOrientationType


    class SketchOrientationType(enum.Enum):
        Automatic = 0
        RelativeToFace = 1
        UseCurveParameters = 2
    

    class PlaneOrientationType(enum.Enum):
        NormalToPath = 0
        NormalToVector = 1
        ParallelToVector = 2
        ThroughAxis = 3
    

class SketchAlignmentConstraint(SketchGeometricConstraint):
    def __init__(self) -> None: ...
    AlignmentType: SketchAlignmentConstraint.Type


    class Type(enum.Enum):
        Horizontal = 0
        Vertical = 1
    

class Sketch(DisplayableObject):
    def __init__(self) -> None: ...
    def DeleteObjects(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def Reattach(self, attachmentPlane: ISurface, referenceAxis: IReferenceAxis, referenceDirection: Vector3d, referenceAxisOrientation: AxisOrientation, referenceAxisSense: Sense, normalOrientation: PlaneNormalOrientation, localCoordinateSystemOrigin: Point3d) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.SketchInPlaceBuilder instead.")"""
        ...
    def Activate(self, orientView: Sketch.ViewReorient) -> None:
        ...
    def Deactivate(self, orientView: Sketch.ViewReorient, updateLevel: Sketch.UpdateLevel) -> None:
        ...
    def SetReferenceDirection(self, referenceAxis: IReferenceAxis, referenceDirection: Vector3d, referenceAxisOrientation: AxisOrientation, referenceAxisSense: Sense) -> None:
        ...
    def FlipReferenceDirection(self) -> None:
        ...
    def FlipNormal(self) -> None:
        ...
    def GetReferenceDirection(self, referenceAxis: IReferenceAxis, referenceAxisOrientation: AxisOrientation, referenceAxisSense: Sense) -> Vector3d:
        ...
    def RunAutoDimension(self) -> None:
        ...
    def CreateCoincidentConstraint(self, geom1: Sketch.ConstraintGeometry, geom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateFixedConstraint(self, geom: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateFullyFixedConstraints(self, geom: Sketch.ConstraintGeometry) -> typing.List[SketchGeometricConstraint]:
        ...
    def CreateHorizontalConstraint(self, geom: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateVerticalConstraint(self, geom: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateTangentConstraint(self, geom1: Sketch.ConstraintGeometry, geom1Help: Sketch.ConstraintGeometryHelp, geom2: Sketch.ConstraintGeometry, geom2Help: Sketch.ConstraintGeometryHelp) -> SketchTangentConstraint:
        ...
    def CreateConstantLengthConstraint(self, conGeom: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateConstantAngleConstraint(self, conGeom: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateUniformScaledConstraint(self, conGeom: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateNonUniformScaledConstraint(self, conGeom: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateParallelConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreatePerpendicularConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateNormalConstraint(self, conGeom1: Sketch.ConstraintGeometry, geom1Help: Sketch.ConstraintGeometryHelp, conGeom2: Sketch.ConstraintGeometry, geom2Help: Sketch.ConstraintGeometryHelp) -> SketchGeometricConstraint:
        ...
    def CreateCollinearConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateEqualLengthConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateEqualRadiusConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateConcentricConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateMidpointConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreateSlopeConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry) -> SketchGeometricConstraint:
        ...
    def CreatePointOnCurveConstraint(self, conGeom1: Sketch.ConstraintGeometry, conGeom2: Sketch.ConstraintGeometry, help: Sketch.ConstraintGeometryHelp) -> SketchHelpedGeometricConstraint:
        ...
    def CreatePointOnStringConstraint(self, conGeom1: Sketch.ConstraintGeometry, curvesInString: typing.List[Curve], helpData: Sketch.ConstraintGeometryHelp, curveWhichHelpParamAppliesTo: int) -> SketchHelpedGeometricConstraint:
        ...
    def CreatePointOnStringConstraint(self, conGeom1: Sketch.ConstraintGeometry, curveInString: Curve, helpData: Sketch.ConstraintGeometryHelp) -> SketchHelpedGeometricConstraint:
        ...
    def CreateDimension(self, dimType: Sketch.ConstraintType, dimObject1: Sketch.DimensionGeometry, dimObject2: Sketch.DimensionGeometry, dimOrigin: Point3d, expression: Expression) -> SketchDimensionalConstraint:
        ...
    def CreateDimension(self, dimType: Sketch.ConstraintType, dimObject1: Sketch.DimensionGeometry, dimObject2: Sketch.DimensionGeometry, dimOrigin: Point3d, expression: Expression, refDim: Sketch.DimensionOption) -> SketchDimensionalConstraint:
        ...
    def CreateRadialDimension(self, dimObject1: Sketch.DimensionGeometry, dimOrigin: Point3d, expression: Expression) -> SketchDimensionalConstraint:
        ...
    def CreateRadialDimension(self, dimObject1: Sketch.DimensionGeometry, dimOrigin: Point3d, expression: Expression, refDim: Sketch.DimensionOption) -> SketchDimensionalConstraint:
        ...
    def CreateDiameterDimension(self, dimObject1: Sketch.DimensionGeometry, dimOrigin: Point3d, expression: Expression) -> SketchDimensionalConstraint:
        ...
    def CreateDiameterDimension(self, dimObject1: Sketch.DimensionGeometry, dimOrigin: Point3d, expression: Expression, refDim: Sketch.DimensionOption) -> SketchDimensionalConstraint:
        ...
    def CreatePerimeterDimension(self, curves: typing.List[Curve], dimOrigin: Point3d, expression: Expression) -> SketchDimensionalConstraint:
        ...
    def LocalUpdate(self) -> None:
        ...
    def Update(self) -> None:
        ...
    def Update(self, geoms: typing.List[NXObject]) -> None:
        ...
    def UpdateGeometryDisplay(self) -> None:
        ...
    def UpdateGeometryDisplay(self, geoms: typing.List[SmartObject]) -> None:
        ...
    def UpdateDimensionDisplay(self) -> None:
        ...
    def UpdateDimensionDisplay(self, geoms: typing.List[SmartObject]) -> None:
        ...
    def UpdateDimensionDisplay(self, dims: typing.List[NXObject]) -> None:
        ...
    def UpdateConstraintDisplay(self) -> None:
        ...
    def UpdateConstraintDisplay(self, geoms: typing.List[SmartObject]) -> None:
        ...
    def AddGeometry(self, crv: DisplayableObject, inferCoincidentConstraints: Sketch.InferConstraintsOption) -> None:
        ...
    def AddGeometry(self, crv: DisplayableObject) -> None:
        ...
    def AddGeometry(self, crv: Curve, inferCoincidentConstraints: Sketch.InferConstraintsOption, ellipseOption: Sketch.AddEllipseOption) -> None:
        ...
    def AddGeometry(self, inferCoincidentConstraints: Sketch.InferConstraintsOption, ellipseOption: Sketch.AddEllipseOption, curvesOrPoints: typing.List[SmartObject]) -> None:
        ...
    def GetStatus(self, dofNeeded: int) -> Sketch.Status:
        ...
    def CalculateStatus(self) -> None:
        ...
    def GetAllConstraintsOfType(self, conClass: Sketch.ConstraintClass, conType: Sketch.ConstraintType) -> typing.List[SketchConstraint]:
        ...
    def GetConstraintsForGeometry(self, geometry: SmartObject, conClass: Sketch.ConstraintClass) -> typing.List[SketchConstraint]:
        ...
    def GetAllExpressions(self) -> typing.List[Expression]:
        ...
    def GetAllGeometry(self) -> typing.List[NXObject]:
        ...
    def IsSketchGeometry(self, geometry: SmartObject) -> bool:
        ...
    def Fillet(self, curve1: Curve, curve2: Curve, helpPoint1: Point3d, helpPoint2: Point3d, radius: float, doTrim: Sketch.TrimInputOption, createRadiusDim: Sketch.CreateDimensionOption, alternateSolution: Sketch.AlternateSolutionOption, constraints: typing.List[SketchConstraint]) -> typing.List[Arc]:
        ...
    def Fillet(self, curve1: Curve, curve2: Curve, helpPoint1: Point3d, helpPoint2: Point3d, pointOnArc: Point3d, radius: float, doTrim: Sketch.TrimInputOption, createRadiusDim: Sketch.CreateDimensionOption, alternateSolution: Sketch.AlternateSolutionOption, constraints: typing.List[SketchConstraint]) -> typing.List[Arc]:
        ...
    def Fillet(self, curve1: Curve, curve2: Curve, curve3: Curve, helpPoint1: Point3d, helpPoint2: Point3d, helpPoint3: Point3d, radius: float, doTrim: Sketch.TrimInputOption, doDelete: Sketch.DeleteThirdCurveOption, createRadiusDim: Sketch.CreateDimensionOption, alternateSolution: Sketch.AlternateSolutionOption, constraints: typing.List[SketchConstraint]) -> typing.List[Arc]:
        ...
    def Fillet(self, curve1: Curve, curve2: Curve, curve3: Curve, helpPoint1: Point3d, helpPoint2: Point3d, helpPoint3: Point3d, pointOnArc: Point3d, radius: float, doTrim: Sketch.TrimInputOption, doDelete: Sketch.DeleteThirdCurveOption, createRadiusDim: Sketch.CreateDimensionOption, alternateSolution: Sketch.AlternateSolutionOption, constraints: typing.List[SketchConstraint]) -> typing.List[Arc]:
        ...
    def DeleteConstraintsOnGeometries(self, objects: typing.List[NXObject]) -> None:
        ...
    def DeleteConstraintsOnGeometries(self, objects: typing.List[Sketch.ConstraintGeometry]) -> None:
        ...
    def DeleteConstraintsOnGeometries(self, conClass: Sketch.ConstraintClass, objects: typing.List[Sketch.ConstraintGeometry]) -> None:
        ...
    def CopyObjects(self, inputObjects: typing.List[NXObject]) -> typing.List[NXObject]:
        ...
    def CopyObjectsWithDimensionOutput(self, inputObjects: typing.List[NXObject], outputObjects: typing.List[NXObject], outputDims: typing.List[NXObject]) -> None:
        ...
    def ShowDimensions(self, inputObjects: typing.List[DisplayableObject]) -> None:
        ...
    def HideDimensions(self, inputObjects: typing.List[DisplayableObject]) -> None:
        ...
    def ShowDimensions(self) -> None:
        ...
    def ShowDimensions(self, objects: typing.List[Sketch.ConstraintGeometry]) -> None:
        ...
    def HideDimensions(self) -> None:
        ...
    def HideDimensions(self, objects: typing.List[Sketch.ConstraintGeometry]) -> None:
        ...
    def AutoConstrain(self, linearTolerance: float, angularTolerance: float, allowRemoteConstraints: bool, geometries: typing.List[SmartObject], autoconstraintTypes: typing.List[Sketch.ConstraintType]) -> typing.List[SketchConstraint]:
        ...
    def MakeDatumsInternal(self) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  None.")"""
        ...
    def MakeDatumsExternal(self) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Please use NXOpen.Sketch.MakeDatumsExternal2 instead.")"""
        ...
    def MakeDatumsExternal2(self) -> None:
        ...
    def CopyObjectsWithTracking(self, inputObjects: typing.List[DisplayableObject]) -> typing.List[Sketch.CopyObjectData]:
        ...
    def EditSplinePoles(self, spline: Spline, poles: float) -> None:
        ...
    def EditSplineDefiningPoints(self, spline: Spline, points: float) -> None:
        ...
    def ConvertToNx10Spline(self, spline: Spline) -> None:
        ...
    def RemoveRedundantVertices(self, geoms: typing.List[NXObject]) -> None:
        ...
    def ManageConstraintsAfterEdit(self, sketchGeoms: typing.List[NXObject], preserveComplexConstraints: bool) -> None:
        ...
    def BreakAssociativity(self, sketchGeoms: typing.List[NXObject]) -> None:
        ...
    def Scale(self, scaleFactor: float) -> None:
        ...
    def SetTextHeight(self, textHeight: float) -> None:
        ...
    def ConvertRadialDimension(self, dimensions: typing.List[DisplayableObject]) -> None:
        ...
    def GetVirtualPoints(self) -> typing.List[SketchVirtualPoint]:
        ...
    def GetIgnoredRelationsOfGeometry(self, geometry: Sketch.ConstraintGeometry) -> typing.List[SketchRelation]:
        ...
    def SetRotationOrigin(self, center: Point3d) -> None:
        ...
    Preferences: Preferences.SketchPreferences
    AttachPlane: ISurface
    CreateInferConstraintsSetting: Sketch.CreateInferConstraintSetting
    DOFDisplay: bool
    Feature: Features.Feature
    IsActive: bool
    IsDraftingSketch: bool
    IsInternal: bool
    Orientation: NXMatrix
    Origin: Point3d
    RotateDragMode: bool
    UpdateScope: Sketch.UpdateLevel
    UpgradeUponActivation: bool
    UsesLegacySolver: bool
    View: View


    class ViewReorient(enum.Enum):
        False = 0
        True = 1
    

    class UpdateLevel(enum.Enum):
        SketchOnly = 0
        Model = 1
    

    class TrimInputOption(enum.Enum):
        False = 0
        True = 1
    

    class Status(enum.Enum):
        Unknown = 0
        NotEvaluated = 1
        UnderConstrained = 2
        WellConstrained = 3
        OverConstrained = 4
        InconsistentlyConstrained = 5
    

    class SketchSketchGeometry():
        Geometry: NXObject
        PointType: Sketch.PointType
        PointIndex: int
        def ToString(self) -> str:
            ...
        def __init__(self, Geometry: NXObject, PointType: Sketch.PointType, PointIndex: int) -> None: ...
    

    class PointType(enum.Enum):
        None = 0
        StartPoint = 1
        EndPoint = 2
        Center = 3
        SplineDefiningPoint = 4
        Anchor = 5
        SplinePole = 6
        MidPoint = 7
        Quadrant = 8
    

    class PlaneOption(enum.Enum):
        Inferred = 0
        ExistingPlane = 1
        NewPlane = 2
        NewCsys = 3
    

    class InferConstraintsOption(enum.Enum):
        InferNoConstraints = 0
        InferCoincidentConstraints = 1
    

    class DimensionOption(enum.Enum):
        CreateAsDriving = 0
        CreateAsReference = 1
        CreateAsAutomatic = 2
        CreateAsConstant = 3
    

    class SketchDimensionGeometry():
        Geometry: NXObject
        AssocType: Sketch.AssocType
        AssocValue: int
        HelpPoint: Point3d
        View: NXObject
        def ToString(self) -> str:
            ...
    

    class DeleteThirdCurveOption(enum.Enum):
        False = 0
        True = 1
    

    class CreateInferConstraintSetting(enum.Enum):
        On = 0
        Off = 1
    

    class CreateDimensionOption(enum.Enum):
        False = 0
        True = 1
    

    class SketchCopyObjectData():
        OrigObject: NXObject
        CopiedObject: NXObject
        def ToString(self) -> str:
            ...
        def __init__(self, OrigObject: NXObject, CopiedObject: NXObject) -> None: ...
    

    class ConstraintType(enum.Enum):
        NoCon = 0
        Fixed = 1
        Horizontal = 2
        Vertical = 3
        Parallel = 4
        Perpendicular = 5
        Collinear = 6
        EqualLength = 7
        EqualRadius = 8
        ConstantLength = 9
        ConstantAngle = 10
        Coincident = 11
        Concentric = 12
        Mirror = 13
        PointOnCurve = 14
        Midpoint = 15
        Tangent = 16
        RadiusDim = 17
        DiameterDim = 18
        HorizontalDim = 19
        VerticalDim = 20
        ParallelDim = 21
        PerpendicularDim = 22
        AngularDim = 23
        ReservedCon1 = 24
        ReservedCon2 = 25
        ReservedCon3 = 26
        ReservedCon4 = 27
        ReservedCon5 = 28
        ReservedCon6 = 29
        PointOnString = 30
        Slope = 31
        UniformScaled = 32
        NonUniformScaled = 33
        AssocTrim = 34
        AssocOffset = 35
        PerimeterDim = 36
        Offset = 37
        Normal = 38
        PointOnLoop = 39
        RecipeTrim = 40
        Pattern = 41
        MinorAngularDim = 42
        MajorAngularDim = 43
        LastConType = 44
    

    class ConstraintPointType(enum.Enum):
        None = 0
        StartVertex = 1
        EndVertex = 2
        ArcCenter = 3
        SplineDefiningPoint = 4
        Anchor = 5
        SplinePole = 6
        MidVertex = 7
    

    class ConstraintGeometryHelpType(enum.Enum):
        Point = 0
        Parameter = 1
    

    class SketchConstraintGeometryHelp():
        Type: Sketch.ConstraintGeometryHelpType
        Point: Point3d
        Parameter: float
        def ToString(self) -> str:
            ...
        def __init__(self, Type: Sketch.ConstraintGeometryHelpType, Point: Point3d, Parameter: float) -> None: ...
    

    class SketchConstraintGeometry():
        Geometry: NXObject
        PointType: Sketch.ConstraintPointType
        SplineDefiningPointIndex: int
        def ToString(self) -> str:
            ...
        def __init__(self, Geometry: NXObject, PointType: Sketch.ConstraintPointType, SplineDefiningPointIndex: int) -> None: ...
    

    class ConstraintClass(enum.Enum):
        NotConstraint = 0
        Any = 1
        Geometric = 2
        Dimension = 3
    

    class AutoDimensioningRule(enum.Enum):
        Symmetric = 1
        AdjacentAngle = 2
        Length = 3
        HorizontalVertical = 4
        ReferenceAxes = 5
    

    class AssocType(enum.Enum):
        None = 0
        StartPoint = 1
        EndPoint = 2
        ArcCenter = 3
        Tangency = 4
        CurvePoint = 5
        AnchorPoint = 6
        Midpoint = 7
    

    class AlternateSolutionOption(enum.Enum):
        False = 0
        True = 1
    

    class AddEllipseOption(enum.Enum):
        TreatAsEllipse = 0
        TreatAsConic = 1
    

    class Sketch_SketchGeometry():
        geometry: Tag
        pointType: Sketch.PointType
        pointIndex: int
    

    class Sketch_DimensionGeometry():
        geometry: Tag
        assoc_type: Sketch.AssocType
        assoc_value: int
        help_point: Point3d
        view: Tag
    

    class Sketch_CopyObjectData():
        orig_object: Tag
        copied_object: Tag
    

    class Sketch_ConstraintGeometry():
        geometry: Tag
        point_type: Sketch.ConstraintPointType
        spline_defining_point_index: int
    

class SinkBehavior(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Active: bool


    class SinkBehavior.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class SingleMeasure(GenericMeasure):
    def __init__(self, ptr: int) -> None: ...
    Value: float


class SingleFacetRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, facets: typing.List[IFacet]) -> None:
        ...


class SimulationAction(enum.Enum):
    Restart = 1
    Pause = 2
    Resume = 3
    Stop = 4


class SimpleSketchInPlaceBuilder(Builder):
    def __init__(self) -> None: ...
    def FlipSketchPlaneNormal(self) -> None:
        ...
    def FlipHorizontalReference(self) -> None:
        ...
    CoordinateSystem: CartesianCoordinateSystem
    HorizontalReference: SelectNXObject
    SketchOrigin: Point
    UseWorkPartOrigin: bool


class SignalAdapter(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Signals: typing.List[Signal]
    Active: bool


    class SignalAdapter.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Signal(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Type: int
    IntValue: int
    FloatValue: float
    BoolValue: bool
    StringValue: str
    BoolValues: bool
    IntValues: int
    FloatValues: float
    StringValues: str
    Adapter: SignalAdapter
    Active: bool


    class Signal.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class ShapeBody(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetOwner(self) -> RigidBody:
        ...


class Session(Utilities.BaseSession):
    def __init__(self) -> None: ...
    def GetSession() -> Session:
        ...
    def SetUndoMark(self, markVisibility: Session.MarkVisibility, name: str) -> Session.UndoMarkId:
        ...
    def UndoToLastVisibleMark(self) -> None:
        ...
    def UndoLastNVisibleMarks(self, n: int, marksRecycled: bool, undoUnavailable: bool) -> None:
        ...
    def Redo(self) -> None:
        ...
    def UndoToMark(self, markId: Session.UndoMarkId, markName: str) -> None:
        ...
    def UndoToMarkWithStatus(self, markId: Session.UndoMarkId, markName: str) -> None:
        ...
    def DeleteUndoMark(self, markId: Session.UndoMarkId, markName: str) -> None:
        ...
    def DeleteUndoMarksUpToMark(self, markId: Session.UndoMarkId, markName: str, deleteAllIfNotFound: bool) -> None:
        ...
    def DeleteAllUndoMarks(self) -> None:
        ...
    def SetUndoMarkVisibility(self, markId: Session.UndoMarkId, markName: str, visibility: Session.MarkVisibility) -> None:
        ...
    def GetUndoMarkVisibility(self, markId: Session.UndoMarkId, markName: str) -> Session.MarkVisibility:
        ...
    def GetUndoMarkName(self, markId: Session.UndoMarkId) -> str:
        ...
    def SetUndoMarkName(self, markId: Session.UndoMarkId, markName: str) -> None:
        ...
    def DoesUndoMarkExist(self, markId: Session.UndoMarkId, markName: str) -> bool:
        ...
    def GetAllUndoMarks(self, visibility: Session.MarkVisibility) -> typing.List[Session.UndoMarkData]:
        ...
    def GetNewestUndoMark(self, visibility: Session.MarkVisibility) -> Session.UndoMarkId:
        ...
    def BeginTaskEnvironment(self) -> None:
        ...
    def DeleteUndoMarksSetInTaskEnvironment(self) -> None:
        ...
    def EndTaskEnvironment(self) -> None:
        ...
    def NewPartCleanup(self) -> PartCleanup:
        ...
    def NewErrorList(self) -> ErrorList:
        ...
    def NewDatabaseSessionOptions(self) -> PDM.SessionSettings:
        ...
    def NewDatabasePersistentOptions(self) -> PDM.PersistentSettings:
        ...
    def NewCaeGrmsearch(self) -> CAE.GRMSearch:
        ...
    def ExecuteGrip(self, gripExecutable: str, inputArgs: any) -> any:
        ...
    def Execute(self, libName: str, className: str, methodName: str, inputArgs: any) -> any:
        ...
    def CreateCamSession(self) -> None:
        ...
    def IsCamSessionInitialized(self) -> bool:
        ...
    def CreateInspectionSession(self) -> None:
        ...
    def IsInspectionSessionInitialized(self) -> bool:
        ...
    def GetProperty(self, object: TaggedObject, propertyName: str) -> str:
        ...
    def SetProperty(self, object: TaggedObject, propertyName: str, value: str) -> None:
        ...
    def GetNamedProperties(self, object: TaggedObject) -> str:
        ...
    def GetClasses(self) -> str:
        ...
    def GetNamedProperties(self, className: str, properties: str, propertyTypes: str) -> None:
        ...
    def CleanUpFacetedFacesAndEdges(self) -> None:
        ...
    def AssignRemoveProjects(self, cliNames: str, objectTypes: typing.List[Session.ProjectAssignmentObjectType], projectNames: str, assignmentStates: typing.List[Session.ProjectAssignmentState]) -> None:
        ...
    def GetEnvironmentVariableValue(self, envVaribable: str) -> str:
        ...
    def SetEnvironmentVariableValue(self, envVaribable: str, envValue: str) -> None:
        ...
    def EnableRedo(self, enableRedo: bool) -> bool:
        ...
    def NewTransientText(self) -> Display.TransientText:
        ...
    def AssignRemoveProjectsBasedOnPartOccs(self, partOccs: typing.List[TaggedObject], objectTypes: typing.List[Session.ProjectAssignmentObjectType], projectNames: str, assignmentStates: typing.List[Session.ProjectAssignmentState]) -> None:
        ...
    def ApplicationSwitchOnActiveDisplayedPart(self) -> None:
        ...
    def ApplicationSwitchImmediate(self, applicationName: str) -> None:
        ...
    def CreateTableEditorDefaultDataProvider(self, part: BasePart) -> TableEditorDefaultDataProvider:
        ...
    def DeleteTransientDynamicSectionCutData(self) -> bool:
        ...
    def ExitPartNavigator(self) -> None:
        ...
    def OpenPartNavigator(self) -> None:
        ...
    def IsPartNavigatorOpen(self) -> bool:
        ...
    def IsPartNavigatorFrozen(self) -> bool:
        ...
    def FreezePartNavigator(self) -> None:
        ...
    def UnfreezePartNavigator(self) -> None:
        ...
    def GetMinimallyLoadedParts(self, minimallyLoadedParts: typing.List[BasePart]) -> None:
        ...
    def GetTranslatedString(self, fileName: str, uniqueID: str, string: str, context: str) -> str:
        ...
    def CreateRoutingSession(self) -> None:
        ...
    AfuManager: CAE.AfuManager
    DexManager: DexManager
    PvtransManager: PvtransManager
    FTKManager: CAE.FTK.FTKManager
    Post: CAE.Post
    ResultManager: CAE.ResultManager
    CaeSession: CAE.CaeSession
    UpdateManager: Update
    Parts: PartCollection
    WeldCustomManager: Weld.CustomManager
    ValidationManager: Validate.ValidationManager
    CheckerDataStatus: MendixReporting.CheckerDataStatus
    AutomatedTestingManager: AutomatedTesting.TestingManager
    ListingWindow: ListingWindow
    SpreadsheetManager: SpreadsheetManager
    DisplayManager: DisplayManager
    MathUtils: MathUtils
    EngineeringFunction: EngineeringFunction
    Measurement: Measurement
    Information: Information
    Preferences: Preferences.SessionPreferences
    LogFile: LogFile
    CAMSession: CAM.CAMSession
    DesignRuleManager: Routing.DesignRuleManager
    RouteCustomManager: Routing.CustomManager
    RoutingCustomManager: RoutingCommon.CustomManager
    OptionsManager: Options.OptionsManager
    LicenseManager: LicenseManager
    UserDefinedClassManager: UserDefinedObjects.UserDefinedClassManager
    AssembliesUtils: AssembliesUtils
    DrawingUtils: DrawingUtils
    RequirementUtils: PDM.RequirementUtils
    MotionSession: Motion.MotionSession
    MotionSimulation: Motion.MotionSimulation
    PdmSearchManager: PDM.PdmSearchManager
    XmlComparator: Validate.XmlComparator
    DataManager: CAE.FTK.DataManager
    VisualReportManager: VisualReporting.VisualReportManager
    XYPlotManager: CAE.Xyplot.XYPlotManager
    PdmSession: PDM.PdmSession
    ToolingSession: Tooling.ToolingSession
    UserDefinedFeatureClassManager: Features.UserDefinedFeatureClassManager
    IssueManager: Issue.IssueManager
    AttributeManager: AttributeManager
    LinkedPartManager: LinkedPartManager
    CollaborativeContentManager: CollaborativeContentManager
    MechatronicsSession: Mechatronics.MechatronicsSession
    ConfigurationManager: PDM.ConfigurationManager
    BookmarkFile: Gateway.BookmarkFile
    SubdivisionTaskEnvironment: SubdivisionTaskEnvironment
    WeldCpdUtils: Weld.WeldCpdUtils
    CustomFeatureClassManager: Features.CustomFeatureClassManager
    PostConfiguratorManager: SIM.PostConfigurator.PostConfiguratorManager
    JournalManager: JournalManager
    WebAppSession: PDM.WebAppSession
    ReportManager: Report.ReportManager
    ShipSession: ShipDesign.ShipSession
    SheetManager: Diagramming.SheetManager
    PolygonModelingTaskEnvironment: PolygonModelingTaskEnvironment
    CurveOperation: CAE.CurveOperation
    StudioMaterialManager: StudioMaterialManager
    TextureModelingTaskEnvironment: TextureModelingTaskEnvironment
    MorphMeshTaskEnvironment: MorphMeshTaskEnvironment
    StructureDesignSession: StructureDesign.StructureDesignSession
    TopologyOptimizationTaskEnvironment: TopologyOptimizationTaskEnvironment
    FrameTaskEnvironment: StructureDesign.FrameTaskEnvironment
    SessionManager: CollaborationApplication.SessionManager
    DMUSessionCollection: DMUSessionCollection
    DrawShapeTaskEnvironment: DrawShapeTaskEnvironment
    AppearanceUtils: Appearance.AppearanceUtils
    FeatureColorManager: Features.FeatureColorManager
    ImplicitModelingTaskEnvironment: ImplicitModelingTaskEnvironment
    ActiveSketch: Sketch
    ApplicationName: str
    BuildNumber: int
    CompatibleBaseRelease: int
    ExecutingJournal: str
    GroupBuild: str
    IsBatch: bool
    IsInTaskEnvironment: bool
    NewestVisibleUndoMark: Session.UndoMarkId
    ReleaseName: str
    ReleaseNumber: int
    TransientPartPersistencePolicy: Session.TransientPartPolicy


    

    class SessionUndoMarkData():
        Id: Session.UndoMarkId
        Visibility: Session.MarkVisibility
        def ToString(self) -> str:
            ...
        def __init__(self, Id: Session.UndoMarkId, Visibility: Session.MarkVisibility) -> None: ...
    

    class TransientPartPolicy(enum.Enum):
        RetainTransience = 0
        RemoveTransience = 1
    

    class ProjectAssignmentState(enum.Enum):
        None = 10
        Partial = 11
        Full = 12
    

    class ProjectAssignmentObjectType(enum.Enum):
        Part = 0
        Partrev = 1
        Appdata = 2
        CollaborativeProductDevelopmentDe = 3
    

    class MarkVisibility(enum.Enum):
        Visible = 0
        Invisible = 1
        AnyVisibility = 2
    

    class LibraryUnloadOption(enum.Enum):
        Immediately = 1
        Explicitly = 2
        AtTermination = 3
    

class Sense(enum.Enum):
    Forward = 0
    Reverse = 1


class SelectViewList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: View) -> bool:
        ...
    def Add(self, objects: typing.List[View]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: View, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: View) -> bool:
        ...
    def Remove(self, object: View, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: View, view1: View, point1: Point3d, selection2: View, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[View]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: View) -> bool:
        ...
    def SetArray(self, objects: typing.List[View]) -> None:
        ...
    def GetArray(self) -> typing.List[View]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: View, view1: View, point1: Point3d, selection2: View, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: View, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectView(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: View, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: View, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: View, view1: View, point1: Point3d, selection2: View, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: View, view1: View, point1: Point3d, selection2: View, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: View, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> View:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: View


class SelectTaggedObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: TaggedObject) -> bool:
        ...
    def Add(self, objects: typing.List[TaggedObject]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: TaggedObject, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: TaggedObject) -> bool:
        ...
    def Remove(self, object: TaggedObject, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[TaggedObject]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: TaggedObject) -> bool:
        ...
    def SetArray(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def GetArray(self) -> typing.List[TaggedObject]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: TaggedObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectTaggedObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: TaggedObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: TaggedObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: TaggedObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> TaggedObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: TaggedObject


class SelectSplineList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Spline) -> bool:
        ...
    def Add(self, objects: typing.List[Spline]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Spline, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Spline) -> bool:
        ...
    def Remove(self, object: Spline, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Spline, view1: View, point1: Point3d, selection2: Spline, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Spline]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Spline) -> bool:
        ...
    def SetArray(self, objects: typing.List[Spline]) -> None:
        ...
    def GetArray(self) -> typing.List[Spline]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Spline, view1: View, point1: Point3d, selection2: Spline, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Spline, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectSpline(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Spline, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Spline, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Spline, view1: View, point1: Point3d, selection2: Spline, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Spline, view1: View, point1: Point3d, selection2: Spline, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Spline, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Spline:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Spline


class SelectSmartObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: SmartObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: SmartObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: SmartObject, view1: View, point1: Point3d, selection2: SmartObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: SmartObject, view1: View, point1: Point3d, selection2: SmartObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: SmartObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> SmartObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: SmartObject


class SelectSketchMakeUniformScaleBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: SketchMakeUniformScaleBuilder) -> bool:
        ...
    def Add(self, objects: typing.List[SketchMakeUniformScaleBuilder]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: SketchMakeUniformScaleBuilder, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: SketchMakeUniformScaleBuilder) -> bool:
        ...
    def Remove(self, object: SketchMakeUniformScaleBuilder, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: SketchMakeUniformScaleBuilder, view1: View, point1: Point3d, selection2: SketchMakeUniformScaleBuilder, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[SketchMakeUniformScaleBuilder]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: SketchMakeUniformScaleBuilder) -> bool:
        ...
    def SetArray(self, objects: typing.List[SketchMakeUniformScaleBuilder]) -> None:
        ...
    def GetArray(self) -> typing.List[SketchMakeUniformScaleBuilder]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: SketchMakeUniformScaleBuilder, view1: View, point1: Point3d, selection2: SketchMakeUniformScaleBuilder, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: SketchMakeUniformScaleBuilder, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectSketchList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Sketch) -> bool:
        ...
    def Add(self, objects: typing.List[Sketch]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Sketch, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Sketch) -> bool:
        ...
    def Remove(self, object: Sketch, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Sketch, view1: View, point1: Point3d, selection2: Sketch, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Sketch]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Sketch) -> bool:
        ...
    def SetArray(self, objects: typing.List[Sketch]) -> None:
        ...
    def GetArray(self) -> typing.List[Sketch]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Sketch, view1: View, point1: Point3d, selection2: Sketch, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Sketch, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectSketch(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Sketch, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Sketch, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Sketch, view1: View, point1: Point3d, selection2: Sketch, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Sketch, view1: View, point1: Point3d, selection2: Sketch, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Sketch, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Sketch:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Sketch


class SelectSelectObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: SelectObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: SelectObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: SelectObject, view1: View, point1: Point3d, selection2: SelectObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: SelectObject, view1: View, point1: Point3d, selection2: SelectObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: SelectObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> SelectObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: SelectObject


class SelectPointList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Point) -> bool:
        ...
    def Add(self, objects: typing.List[Point]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Point, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Point) -> bool:
        ...
    def Remove(self, object: Point, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Point, view1: View, point1: Point3d, selection2: Point, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Point]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Point) -> bool:
        ...
    def SetArray(self, objects: typing.List[Point]) -> None:
        ...
    def GetArray(self) -> typing.List[Point]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Point, view1: View, point1: Point3d, selection2: Point, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Point, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectPoint(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Point, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Point, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Point, view1: View, point1: Point3d, selection2: Point, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Point, view1: View, point1: Point3d, selection2: Point, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Point, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Point:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Point


class SelectPartList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Part) -> bool:
        ...
    def Add(self, objects: typing.List[Part]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Part, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Part) -> bool:
        ...
    def Remove(self, object: Part, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Part, view1: View, point1: Point3d, selection2: Part, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Part]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Part) -> bool:
        ...
    def SetArray(self, objects: typing.List[Part]) -> None:
        ...
    def GetArray(self) -> typing.List[Part]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Part, view1: View, point1: Point3d, selection2: Part, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Part, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectPart(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Part, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Part, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Part, view1: View, point1: Point3d, selection2: Part, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Part, view1: View, point1: Point3d, selection2: Part, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Part, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Part:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Part


class SelectObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: TaggedObject) -> bool:
        ...
    def Add(self, objects: typing.List[TaggedObject]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: TaggedObject, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: TaggedObject) -> bool:
        ...
    def Remove(self, object: TaggedObject, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[TaggedObject]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: TaggedObject) -> bool:
        ...
    def SetArray(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def GetArray(self) -> typing.List[TaggedObject]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: TaggedObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: TaggedObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: TaggedObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: TaggedObject, view1: View, point1: Point3d, selection2: TaggedObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: TaggedObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> TaggedObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: TaggedObject


class SelectNXObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: NXObject) -> bool:
        ...
    def Add(self, objects: typing.List[NXObject]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: NXObject, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: NXObject) -> bool:
        ...
    def Remove(self, object: NXObject, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: NXObject, view1: View, point1: Point3d, selection2: NXObject, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[NXObject]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: NXObject) -> bool:
        ...
    def SetArray(self, objects: typing.List[NXObject]) -> None:
        ...
    def GetArray(self) -> typing.List[NXObject]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: NXObject, view1: View, point1: Point3d, selection2: NXObject, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: NXObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectNXObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: NXObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: NXObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: NXObject, view1: View, point1: Point3d, selection2: NXObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: NXObject, view1: View, point1: Point3d, selection2: NXObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: NXObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> NXObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: NXObject


class SelectModelingViewList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: ModelingView) -> bool:
        ...
    def Add(self, objects: typing.List[ModelingView]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: ModelingView, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: ModelingView) -> bool:
        ...
    def Remove(self, object: ModelingView, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: ModelingView, view1: View, point1: Point3d, selection2: ModelingView, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[ModelingView]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: ModelingView) -> bool:
        ...
    def SetArray(self, objects: typing.List[ModelingView]) -> None:
        ...
    def GetArray(self) -> typing.List[ModelingView]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: ModelingView, view1: View, point1: Point3d, selection2: ModelingView, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: ModelingView, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectLine(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Line, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Line, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Line, view1: View, point1: Point3d, selection2: Line, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Line, view1: View, point1: Point3d, selection2: Line, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Line, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Line:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Line


class SelectISurface(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: ISurface, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: ISurface, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: ISurface, view1: View, point1: Point3d, selection2: ISurface, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: ISurface, view1: View, point1: Point3d, selection2: ISurface, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: ISurface, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> ISurface:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: ISurface


class SelectIReferenceAxis(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: IReferenceAxis, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: IReferenceAxis, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: IReferenceAxis, view1: View, point1: Point3d, selection2: IReferenceAxis, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: IReferenceAxis, view1: View, point1: Point3d, selection2: IReferenceAxis, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: IReferenceAxis, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> IReferenceAxis:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: IReferenceAxis


class SelectIParameterizedSurfaceList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: IParameterizedSurface) -> bool:
        ...
    def Add(self, objects: typing.List[IParameterizedSurface]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: IParameterizedSurface, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: IParameterizedSurface) -> bool:
        ...
    def Remove(self, object: IParameterizedSurface, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: IParameterizedSurface, view1: View, point1: Point3d, selection2: IParameterizedSurface, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[IParameterizedSurface]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: IParameterizedSurface) -> bool:
        ...
    def SetArray(self, objects: typing.List[IParameterizedSurface]) -> None:
        ...
    def GetArray(self) -> typing.List[IParameterizedSurface]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: IParameterizedSurface, view1: View, point1: Point3d, selection2: IParameterizedSurface, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: IParameterizedSurface, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectIParameterizedSurface(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: IParameterizedSurface, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: IParameterizedSurface, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: IParameterizedSurface, view1: View, point1: Point3d, selection2: IParameterizedSurface, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: IParameterizedSurface, view1: View, point1: Point3d, selection2: IParameterizedSurface, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: IParameterizedSurface, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> IParameterizedSurface:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: IParameterizedSurface


class SelectionSubscriber(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def Activate(self) -> None:
        ...
    def Deactivate(self) -> None:
        ...
    def IsActive(self) -> bool:
        ...
    def RegisterOnSelectionChangeCallback(self, callbackToRegister: SelectionSubscriber.OnSelectionChangeCallback) -> None:
        ...
    def FreeResource(self) -> None:
        ...


    

    

    

class SelectionMethod(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetSelectedObjects(self) -> typing.List[TaggedObject]:
        ...
    def FreeResource(self) -> None:
        ...


class SelectionIntentRuleOptions(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def SetSelectedFromInactive(self, selectionFromInactiveWindow: bool) -> None:
        ...


class SelectionIntentRule(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Type: SelectionIntentRule.RuleType


    class RuleType(enum.Enum):
        EdgeDumb = 0
        EdgeChain = 1
        EdgeTangent = 2
        EdgeFace = 3
        EdgeBody = 4
        EdgeFeature = 5
        EdgeSheetBoundary = 6
        EdgeBoundary = 7
        EdgeIntersect = 8
        EdgeMultipleSeedTangent = 9
        EdgeVertex = 10
        EdgeVertexTangent = 11
        CurveDumb = 12
        CurveFeature = 13
        CurveFeatureChain = 14
        CurveFeatureTangent = 15
        FollowFillet = 16
        FeaturePoints = 17
        RegionBoundary = 18
        FaceDumb = 19
        FaceTangent = 20
        FaceAdjacent = 21
        FaceBody = 22
        FaceRegion = 23
        FaceFeature = 24
        FaceConnectedBlend = 25
        FaceAllBlend = 26
        FaceRib = 27
        FaceMergedRib = 28
        FaceSlot = 29
        FaceBossPocket = 30
        FaceRegionBoundary = 31
        FaceAndAdjacentFaces = 32
        CurveGroup = 33
        BodyDumb = 34
        BodyFeature = 35
        BodyGroup = 36
        ApparentChaining = 37
        OuterFaceEdges = 38
        RibTopFaceEdges = 39
        FeatureIntersectionEdges = 40
        FaceHole = 41
        InvalidType = 42
    

class SelectionHandle(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class Selection(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def SelectTaggedObjects(self, message: str, title: str, scope: Selection.SelectionScope, includeFeatures: bool, keepHighlighted: bool, objectArray: typing.List[TaggedObject]) -> Selection.Response:
        ...
    def SelectTaggedObject(self, message: str, title: str, scope: Selection.SelectionScope, includeFeatures: bool, keepHighlighted: bool, object: TaggedObject, cursor: Point3d) -> Selection.Response:
        ...
    def SelectTaggedObjectsWithFilterMembers(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, filterMembers: typing.List[Select.FilterMember], objectArray: typing.List[TaggedObject]) -> Selection.Response:
        ...
    def SelectTaggedObjectsWithFilterCallback(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, filterMembers: typing.List[Select.FilterMember], filterCallback: Selection.FilterTaggedObject, objectArray: typing.List[TaggedObject]) -> Selection.Response:
        ...
    def SelectTaggedObjectsWithFullFiltering(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, supportedFilterMembers: typing.List[Select.FilterMember], initialFilterMembers: typing.List[Select.FilterMember], filterCallback: Selection.FilterTaggedObject, objectArray: typing.List[TaggedObject]) -> Selection.Response:
        ...
    def SelectTaggedObjectWithFilterMembers(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, filterMembers: typing.List[Select.FilterMember], object: TaggedObject, cursor: Point3d) -> Selection.Response:
        ...
    def SelectTaggedObjectWithFilterCallback(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, filterMembers: typing.List[Select.FilterMember], filterCallback: Selection.FilterTaggedObject, object: TaggedObject, cursor: Point3d) -> Selection.Response:
        ...
    def SelectTaggedObjectWithFullFiltering(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, supportedFilterMembers: typing.List[Select.FilterMember], initialFilterMembers: typing.List[Select.FilterMember], filterCallback: Selection.FilterTaggedObject, object: TaggedObject, cursor: Point3d) -> Selection.Response:
        ...
    def SelectObjects(self, message: str, title: str, scope: Selection.SelectionScope, includeFeatures: bool, keepHighlighted: bool, objectArray: typing.List[NXObject]) -> Selection.Response:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.SelectTaggedObjects instead")"""
        ...
    def SelectObjects(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, includeFeatures: bool, keepHighlighted: bool, maskArray: typing.List[Selection.MaskTriple], objectArray: typing.List[NXObject]) -> Selection.Response:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.SelectTaggedObject instead")"""
        ...
    def SelectTaggedObjects(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, includeFeatures: bool, keepHighlighted: bool, maskArray: typing.List[Selection.MaskTriple], objectArray: typing.List[TaggedObject]) -> Selection.Response:
        ...
    def SelectObjects(self, message: str, title: str, scope: Selection.SelectionScope, keepHighlighted: bool, typeArray: typing.List[Selection.SelectionType], objectArray: typing.List[NXObject]) -> Selection.Response:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.SelectTaggedObject instead")"""
        ...
    def SelectTaggedObjects(self, message: str, title: str, scope: Selection.SelectionScope, keepHighlighted: bool, typeArray: typing.List[Selection.SelectionType], objectArray: typing.List[TaggedObject]) -> Selection.Response:
        ...
    def SelectObject(self, message: str, title: str, scope: Selection.SelectionScope, includeFeatures: bool, keepHighlighted: bool, object: NXObject, cursor: Point3d) -> Selection.Response:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.SelectTaggedObject instead")"""
        ...
    def SelectObject(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, includeFeatures: bool, keepHighlighted: bool, maskArray: typing.List[Selection.MaskTriple], object: NXObject, cursor: Point3d) -> Selection.Response:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.SelectTaggedObject instead")"""
        ...
    def SelectTaggedObject(self, message: str, title: str, scope: Selection.SelectionScope, action: Selection.SelectionAction, includeFeatures: bool, keepHighlighted: bool, maskArray: typing.List[Selection.MaskTriple], object: TaggedObject, cursor: Point3d) -> Selection.Response:
        ...
    def SelectObject(self, message: str, title: str, scope: Selection.SelectionScope, keepHighlighted: bool, typeArray: typing.List[Selection.SelectionType], object: NXObject, cursor: Point3d) -> Selection.Response:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.SelectTaggedObject instead")"""
        ...
    def SelectTaggedObject(self, message: str, title: str, scope: Selection.SelectionScope, keepHighlighted: bool, typeArray: typing.List[Selection.SelectionType], object: TaggedObject, cursor: Point3d) -> Selection.Response:
        ...
    def SelectFeatures(self, message: str, featType: Selection.SelectionFeatureType, featureArray: typing.List[Features.Feature]) -> Selection.Response:
        ...
    def SelectScreenPosition(self, message: str, object: View, screenPosition: Point3d) -> Selection.DialogResponse:
        ...
    def GetNumSelectedObjects(self) -> int:
        ...
    def GetSelectedObject(self, index: int) -> NXObject:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.GetSelectedTaggedObject instead")"""
        ...
    def GetSelectedTaggedObject(self, index: int) -> TaggedObject:
        ...
    def IsGlobalSelectionActive(self) -> bool:
        ...
    def ClearGlobalSelectionList(self) -> None:
        ...
    def SetEnabledGlobalFilterMember(self, filterMember: Select.FilterMember) -> None:
        ...
    def SetEnabledGlobalFilterMembers(self, filterMembers: typing.List[Select.FilterMember]) -> None:
        ...
    def ResetEnabledGlobalFilterMembers(self) -> None:
        ...
    def RequestSelections(self, selectList: typing.List[TaggedObject]) -> None:
        ...
    def RequestDeselections(self, deselectList: typing.List[TaggedObject]) -> None:
        ...
    def SetSelectionMask(self, select: SelectionHandle, action: Selection.SelectionAction, maskArray: typing.List[Selection.MaskTriple]) -> None:
        ...
    def SetSelectType(self, select: SelectionHandle, type: Selection.UistylerSelectionType) -> None:
        ...
    def SetSelectionCallbacks(self, select: SelectionHandle, filterproc: Selection.FilterCallback, selcb: Selection.SelectionCallback) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use NXOpen.Selection.SetTaggedObjectSelectionCallbacks instead")"""
        ...
    def SetTaggedObjectSelectionCallbacks(self, select: SelectionHandle, filterproc: Selection.FilterTaggedObjectCallback, selcb: Selection.TaggedObjectSelectionCallback) -> None:
        ...
    def GetSelectionStatusOfUserDefinedClass(self, udoClass: UserDefinedObjects.UserDefinedClass) -> bool:
        ...
    def SetSelectionStatusOfUserDefinedClass(self, udoClass: UserDefinedObjects.UserDefinedClass, selectionStatus: bool) -> None:
        ...
    def RemoveFromSelectionList(self, select: SelectionHandle, objs: typing.List[NXObject], unhighlight: bool) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.RemoveTaggedObjectsFromSelectionList instead")"""
        ...
    def RemoveTaggedObjectsFromSelectionList(self, select: SelectionHandle, objs: typing.List[TaggedObject], unhighlight: bool) -> None:
        ...
    def RemoveAllFromSelectionList(self, select: SelectionHandle, unhighlight: bool) -> None:
        ...
    def IsObjectInSelectionList(self, select: SelectionHandle, object: TaggedObject) -> bool:
        ...
    def AskSelectionListCount(self, select: SelectionHandle) -> int:
        ...
    def AskSelectionObjectList(self, select: SelectionHandle, objects: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.AskSelectionTaggedObjectList instead")"""
        ...
    def AskSelectionTaggedObjectList(self, select: SelectionHandle, objects: typing.List[TaggedObject]) -> None:
        ...
    def AddToSelectionList(self, select: SelectionHandle, objs: typing.List[NXObject], highlightFlag: bool) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use Selection.AddToTaggedObjectsSelectionList instead")"""
        ...
    def AddToTaggedObjectsSelectionList(self, select: SelectionHandle, objs: typing.List[TaggedObject], highlightFlag: bool) -> None:
        ...
    def AskSelectionDescriptor(self, select: SelectionHandle) -> Selection.SelectionDescriptor:
        ...
    def AskSelectionCursorPosition(self, select: SelectionHandle, view: View) -> Point3d:
        ...
    def AskSelectionRectanglePosition(self, select: SelectionHandle, position1: Point3d, position2: Point3d, position3: Point3d, position4: Point3d) -> View:
        ...
    def CreateSelectionSubscriber(self) -> SelectionSubscriber:
        ...
    def Tag(self) -> Tag: ...



    class UistylerSelectionType(enum.Enum):
        InactiveSelection = 0
        SingleSelection = 1
        SingleDeselection = 2
        RobustSelection = 3
        SinglePosition = 4
        RectanglePosition = 5
    

    

    class SelectionType(enum.Enum):
        All = 0
        Features = 1
        Curves = 2
        Faces = 3
        Edges = 4
        CurvesAndEdges = 5
    

    class SelectionScope(enum.Enum):
        UseDefault = 0
        WorkPart = 1
        AnyInAssembly = 3
        WorkPartAndOccurrence = 4
        WorkPartAndWorkPartOccurrence = 5
    

    class SelectionFeatureType(enum.Enum):
        Browsable = 0
        NoBooleanUdf = 1
    

    class SelectionSelectionDescriptor():
        Selection: bool
        Deselection: bool
        Reselection: bool
        SingleSelection: bool
        MultipleSelection: bool
        SinglePosition: bool
        RectanglePosition: bool
        NameSelection: bool
        Rectangle: bool
        def ToString(self) -> str:
            ...
    

    

    class SelectionAction(enum.Enum):
        EnableAll = 0
        EnableSpecific = 1
        DisableSpecific = 2
        ClearAndEnableSpecific = 3
        AllAndDisableSpecific = 4
    

    class Response(enum.Enum):
        Back = 1
        Cancel = 2
        Ok = 3
        ObjectSelectedByName = 4
        ObjectSelected = 5
    

    class SelectionMaskTriple():
        Type: int
        Subtype: int
        SolidBodySubtype: int
        def ToString(self) -> str:
            ...
        def __init__(self, Type: int, Subtype: int, SolidBodySubtype: int) -> None: ...
    

    

    

    

    class DialogResponse(enum.Enum):
        None = 0
        Pick = 1
        Ok = 2
        Cancel = 3
        Back = 4
        Apply = 5
        Help = 6
    

    

    

    

    

    

    

    

    

    

    

class SelectINXObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: INXObject) -> bool:
        ...
    def Add(self, objects: typing.List[INXObject]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: INXObject, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: INXObject) -> bool:
        ...
    def Remove(self, object: INXObject, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: INXObject, view1: View, point1: Point3d, selection2: INXObject, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[INXObject]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: INXObject) -> bool:
        ...
    def SetArray(self, objects: typing.List[INXObject]) -> None:
        ...
    def GetArray(self) -> typing.List[INXObject]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: INXObject, view1: View, point1: Point3d, selection2: INXObject, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: INXObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectICurveList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: ICurve) -> bool:
        ...
    def Add(self, objects: typing.List[ICurve]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: ICurve, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: ICurve) -> bool:
        ...
    def Remove(self, object: ICurve, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: ICurve, view1: View, point1: Point3d, selection2: ICurve, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[ICurve]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: ICurve) -> bool:
        ...
    def SetArray(self, objects: typing.List[ICurve]) -> None:
        ...
    def GetArray(self) -> typing.List[ICurve]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: ICurve, view1: View, point1: Point3d, selection2: ICurve, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: ICurve, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectICurve(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: ICurve, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: ICurve, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: ICurve, view1: View, point1: Point3d, selection2: ICurve, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: ICurve, view1: View, point1: Point3d, selection2: ICurve, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: ICurve, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> ICurve:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: ICurve


class SelectIBody(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: IBody, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: IBody, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: IBody, view1: View, point1: Point3d, selection2: IBody, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: IBody, view1: View, point1: Point3d, selection2: IBody, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: IBody, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> IBody:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: IBody


class SelectIBasePlaneList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: IBasePlane) -> bool:
        ...
    def Add(self, objects: typing.List[IBasePlane]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: IBasePlane, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: IBasePlane) -> bool:
        ...
    def Remove(self, object: IBasePlane, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: IBasePlane, view1: View, point1: Point3d, selection2: IBasePlane, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[IBasePlane]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: IBasePlane) -> bool:
        ...
    def SetArray(self, objects: typing.List[IBasePlane]) -> None:
        ...
    def GetArray(self) -> typing.List[IBasePlane]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: IBasePlane, view1: View, point1: Point3d, selection2: IBasePlane, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: IBasePlane, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectIBaseCurveList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: IBaseCurve) -> bool:
        ...
    def Add(self, objects: typing.List[IBaseCurve]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: IBaseCurve, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: IBaseCurve) -> bool:
        ...
    def Remove(self, object: IBaseCurve, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: IBaseCurve, view1: View, point1: Point3d, selection2: IBaseCurve, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[IBaseCurve]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: IBaseCurve) -> bool:
        ...
    def SetArray(self, objects: typing.List[IBaseCurve]) -> None:
        ...
    def GetArray(self) -> typing.List[IBaseCurve]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: IBaseCurve, view1: View, point1: Point3d, selection2: IBaseCurve, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: IBaseCurve, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectIBaseCurve(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: IBaseCurve, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: IBaseCurve, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: IBaseCurve, view1: View, point1: Point3d, selection2: IBaseCurve, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: IBaseCurve, view1: View, point1: Point3d, selection2: IBaseCurve, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: IBaseCurve, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> IBaseCurve:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: IBaseCurve


class SelectGroupList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Group) -> bool:
        ...
    def Add(self, objects: typing.List[Group]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Group, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Group) -> bool:
        ...
    def Remove(self, object: Group, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Group, view1: View, point1: Point3d, selection2: Group, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Group]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Group) -> bool:
        ...
    def SetArray(self, objects: typing.List[Group]) -> None:
        ...
    def GetArray(self) -> typing.List[Group]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Group, view1: View, point1: Point3d, selection2: Group, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Group, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectGroup(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Group, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Group, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Group, view1: View, point1: Point3d, selection2: Group, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Group, view1: View, point1: Point3d, selection2: Group, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Group, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Group:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Group


class SelectFaceList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Face) -> bool:
        ...
    def Add(self, objects: typing.List[Face]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Face, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Face) -> bool:
        ...
    def Remove(self, object: Face, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Face, view1: View, point1: Point3d, selection2: Face, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Face]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Face) -> bool:
        ...
    def SetArray(self, objects: typing.List[Face]) -> None:
        ...
    def GetArray(self) -> typing.List[Face]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Face, view1: View, point1: Point3d, selection2: Face, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Face, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectFace(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Face, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Face, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Face, view1: View, point1: Point3d, selection2: Face, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Face, view1: View, point1: Point3d, selection2: Face, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Face, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Face:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Face


class SelectExpressionList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Expression) -> bool:
        ...
    def Add(self, objects: typing.List[Expression]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Expression, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Expression) -> bool:
        ...
    def Remove(self, object: Expression, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Expression, view1: View, point1: Point3d, selection2: Expression, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Expression]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Expression) -> bool:
        ...
    def SetArray(self, objects: typing.List[Expression]) -> None:
        ...
    def GetArray(self) -> typing.List[Expression]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Expression, view1: View, point1: Point3d, selection2: Expression, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Expression, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectEdgeList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Edge) -> bool:
        ...
    def Add(self, objects: typing.List[Edge]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Edge, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Edge) -> bool:
        ...
    def Remove(self, object: Edge, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Edge, view1: View, point1: Point3d, selection2: Edge, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Edge]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Edge) -> bool:
        ...
    def SetArray(self, objects: typing.List[Edge]) -> None:
        ...
    def GetArray(self) -> typing.List[Edge]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Edge, view1: View, point1: Point3d, selection2: Edge, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Edge, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectEdge(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Edge, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Edge, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Edge, view1: View, point1: Point3d, selection2: Edge, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Edge, view1: View, point1: Point3d, selection2: Edge, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Edge, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Edge:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Edge


class SelectDisplayableObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: DisplayableObject) -> bool:
        ...
    def Add(self, objects: typing.List[DisplayableObject]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: DisplayableObject, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: DisplayableObject) -> bool:
        ...
    def Remove(self, object: DisplayableObject, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: DisplayableObject, view1: View, point1: Point3d, selection2: DisplayableObject, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[DisplayableObject]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: DisplayableObject) -> bool:
        ...
    def SetArray(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def GetArray(self) -> typing.List[DisplayableObject]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: DisplayableObject, view1: View, point1: Point3d, selection2: DisplayableObject, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: DisplayableObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectDisplayableObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: DisplayableObject, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: DisplayableObject, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: DisplayableObject, view1: View, point1: Point3d, selection2: DisplayableObject, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: DisplayableObject, view1: View, point1: Point3d, selection2: DisplayableObject, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: DisplayableObject, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> DisplayableObject:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: DisplayableObject


class SelectDatumPlaneList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: DatumPlane) -> bool:
        ...
    def Add(self, objects: typing.List[DatumPlane]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: DatumPlane, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: DatumPlane) -> bool:
        ...
    def Remove(self, object: DatumPlane, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: DatumPlane, view1: View, point1: Point3d, selection2: DatumPlane, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[DatumPlane]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: DatumPlane) -> bool:
        ...
    def SetArray(self, objects: typing.List[DatumPlane]) -> None:
        ...
    def GetArray(self) -> typing.List[DatumPlane]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: DatumPlane, view1: View, point1: Point3d, selection2: DatumPlane, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: DatumPlane, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectDatumPlane(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: DatumPlane, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: DatumPlane, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: DatumPlane, view1: View, point1: Point3d, selection2: DatumPlane, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: DatumPlane, view1: View, point1: Point3d, selection2: DatumPlane, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: DatumPlane, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> DatumPlane:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: DatumPlane


class SelectCurveList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Curve) -> bool:
        ...
    def Add(self, objects: typing.List[Curve]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Curve, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Curve) -> bool:
        ...
    def Remove(self, object: Curve, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Curve, view1: View, point1: Point3d, selection2: Curve, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Curve]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Curve) -> bool:
        ...
    def SetArray(self, objects: typing.List[Curve]) -> None:
        ...
    def GetArray(self) -> typing.List[Curve]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Curve, view1: View, point1: Point3d, selection2: Curve, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Curve, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCurve(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Curve, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Curve, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Curve, view1: View, point1: Point3d, selection2: Curve, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Curve, view1: View, point1: Point3d, selection2: Curve, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Curve, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Curve:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Curve


class SelectCoordinateSystemList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: CoordinateSystem) -> bool:
        ...
    def Add(self, objects: typing.List[CoordinateSystem]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: CoordinateSystem, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: CoordinateSystem) -> bool:
        ...
    def Remove(self, object: CoordinateSystem, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: CoordinateSystem, view1: View, point1: Point3d, selection2: CoordinateSystem, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[CoordinateSystem]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: CoordinateSystem) -> bool:
        ...
    def SetArray(self, objects: typing.List[CoordinateSystem]) -> None:
        ...
    def GetArray(self) -> typing.List[CoordinateSystem]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: CoordinateSystem, view1: View, point1: Point3d, selection2: CoordinateSystem, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: CoordinateSystem, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectCoordinateSystem(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: CoordinateSystem, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: CoordinateSystem, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: CoordinateSystem, view1: View, point1: Point3d, selection2: CoordinateSystem, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: CoordinateSystem, view1: View, point1: Point3d, selection2: CoordinateSystem, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: CoordinateSystem, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> CoordinateSystem:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: CoordinateSystem


class SelectCartesianCoordinateSystem(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: CartesianCoordinateSystem, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: CartesianCoordinateSystem, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: CartesianCoordinateSystem, view1: View, point1: Point3d, selection2: CartesianCoordinateSystem, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: CartesianCoordinateSystem, view1: View, point1: Point3d, selection2: CartesianCoordinateSystem, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: CartesianCoordinateSystem, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> CartesianCoordinateSystem:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: CartesianCoordinateSystem


class SelectBodyList(TaggedObject):
    def __init__(self) -> None: ...
    def Add(self, object: Body) -> bool:
        ...
    def Add(self, objects: typing.List[Body]) -> bool:
        ...
    def Add(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Add(self, selection: Body, view: View, point: Point3d) -> bool:
        ...
    def Remove(self, object: Body) -> bool:
        ...
    def Remove(self, object: Body, view: View) -> bool:
        ...
    def Remove(self, snapType: InferSnapType.SnapType, selection1: Body, view1: View, point1: Point3d, selection2: Body, view2: View, point2: Point3d) -> bool:
        ...
    def RemoveArray(self, objects: typing.List[Body]) -> bool:
        ...
    def Remove(self, inputSelectionMethod: SelectionMethod) -> bool:
        ...
    def Clear(self) -> None:
        ...
    def Contains(self, object: Body) -> bool:
        ...
    def SetArray(self, objects: typing.List[Body]) -> None:
        ...
    def GetArray(self) -> typing.List[Body]:
        ...
    def GetSelectObjectArray(self) -> typing.List[SelectObject]:
        ...
    def Add(self, snapType: InferSnapType.SnapType, selection1: Body, view1: View, point1: Point3d, selection2: Body, view2: View, point2: Point3d) -> bool:
        ...
    def Add(self, selection: Body, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObjectList.Add.")"""
        ...
    def Validate(self) -> bool:
        ...
    DuplicatesAllowed: bool
    Size: int


class SelectBody(TaggedObject):
    def __init__(self) -> None: ...
    def SetValue(self, selection: Body, view: View, point: Point3d) -> None:
        ...
    def GetValue(self, selection: Body, view: View, point: Point3d) -> None:
        ...
    def SetValue(self, snapType: InferSnapType.SnapType, selection1: Body, view1: View, point1: Point3d, selection2: Body, view2: View, point2: Point3d) -> None:
        ...
    def GetValue(self, snapType: InferSnapType.SnapType, selection1: Body, view1: View, point1: Point3d, selection2: Body, view2: View, point2: Point3d) -> None:
        ...
    def SetValue(self, selection: Body, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.SetValue.")"""
        ...
    def GetValue(self, caeSubType: CaeObjectType.CaeSubType, caeSubId: int) -> Body:
        """[Obsolete("Deprecated in NX10.0.0.  Use other versions of NXOpen.SelectObject.GetValue.")"""
        ...
    def Validate(self) -> bool:
        ...
    Value: Body


class SectionList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Section]) -> None:
        ...
    def Append(self, object: Section) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Section) -> int:
        ...
    def FindItem(self, index: int) -> Section:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Section) -> None:
        ...
    def Erase(self, obj: Section, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Section]:
        ...
    def SetContents(self, objects: typing.List[Section]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Section, object2: Section) -> None:
        ...
    def Insert(self, location: int, object: Section) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class SectionElementData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetSectionElementData(self, sectionElement: ICurve, startConnector: ICurve, startPoint: Point3d, endConnector: ICurve, endPoint: Point3d) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SectionElementData.GetSectionElementData1 instead.")"""
        ...
    def GetSectionElementData1(self, sectionElement: DisplayableObject, startConnector: DisplayableObject, startPoint: Point3d, endConnector: DisplayableObject, endPoint: Point3d) -> None:
        ...


class SectionData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetStartConnector(self) -> NXObject:
        ...
    def GetEndConnector(self) -> NXObject:
        ...
    def GetRules(self, rules: typing.List[SelectionIntentRule]) -> None:
        ...
    def GetSectionElementsData(self, sectionElementsData: typing.List[SectionElementData]) -> None:
        ...


class SectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Section]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateSection(self, chainingTolerance: float, distanceTolerance: float, angleTolerance: float) -> Section:
        ...
    def CreateSection(self) -> Section:
        ...
    def CreateSectionsUsingCurves(self, curves: typing.List[NXObject], loopOption: SectionCollection.LoopOption, chainingTolerance: float, distanceTolerance: float, angleTolerance: float, section: typing.List[Section]) -> None:
        ...
    def CreateSection(self, curve: NXObject) -> Section:
        ...
    def Tag(self) -> Tag: ...



    class LoopOption(enum.Enum):
        Separate = 0
        SeparateOuter = 1
    

class Section(DisplayableObject):
    def __init__(self) -> None: ...
    def AddToSection(self, rules: typing.List[SelectionIntentRule], seed: NXObject, startConnector: NXObject, endConnector: NXObject, helpPoint: Point3d, featureMode: Section.Mode) -> None:
        ...
    def AddToSection(self, rules: typing.List[SelectionIntentRule], seed: NXObject, startConnector: NXObject, endConnector: NXObject, helpPoint: Point3d, featureMode: Section.Mode, chainWithinFeature: bool) -> None:
        ...
    def RemoveRules(self, rules: typing.List[SelectionIntentRule], startConnector: NXObject, endConnector: NXObject, featureMode: Section.Mode) -> None:
        ...
    def RemoveSingleSectionElement(self, sectionElement: ICurve, startConnector: NXObject, endConnector: NXObject, featureMode: Section.Mode) -> None:
        ...
    def RemoveSingleSectionElement(self, sectionElement: Point, featureMode: Section.Mode) -> None:
        ...
    def RemoveRules(self, sectionElement: ICurve, startConnector: NXObject, endConnector: NXObject, featureMode: Section.Mode) -> None:
        ...
    def RemoveUnderlyingChain(self, pointSpecifyingChain: Point3d, tolerance: float, featureMode: Section.Mode) -> None:
        ...
    def SetStartAndDirection(self, startElement: ICurve, startPoint: Point3d, direction: Vector3d) -> None:
        ...
    def GetStartAndDirection(self, startElement: ICurve, startPoint: Point3d, direction: Vector3d) -> None:
        ...
    def GetStartAndDirectionOfLoop(self, index: int, startPoint: Point3d, direction: Vector3d) -> None:
        ...
    def GetSectionData(self, sectionData: typing.List[SectionData]) -> None:
        ...
    def Destroy(self) -> None:
        ...
    def ReverseDirection(self) -> None:
        ...
    def ReverseDirectionOfLoop(self, index: int) -> None:
        ...
    def SetStartCurveOfClosedLoop(self, index: int, pointOnStartCurve: Point3d) -> None:
        ...
    def ReverseDirectionOfClosedLoop(self, index: int) -> None:
        ...
    def AddSmartPoint(self, smartPt: Point, tol: float) -> None:
        """[Obsolete("Deprecated in NX7.5.0.  Please use ScRuleFactory.CreateRuleCurveDumb followed by Section.AddToSection instead.")"""
        ...
    def AllowSelfIntersection(self, allowSelfIntersection: bool) -> None:
        ...
    def AllowDegenerateCurves(self, allowDegenerateCurves: bool) -> None:
        ...
    def Clear(self) -> None:
        ...
    def GetLoopIndex(self, sectionElement: NXObject) -> int:
        ...
    def GetLoopIndex(self, pointSpecifyingLoop: Point3d, tolerance: float) -> int:
        ...
    def AlignDirectionOfLoop(self, point: Point3d, direction: Vector3d) -> None:
        ...
    def SetInterpart(self, interpart: bool) -> None:
        ...
    def RemoveMultipleCurves(self, wfs: typing.List[ICurve], startConnector: typing.List[NXObject], endConnector: typing.List[NXObject], featureMode: Section.Mode) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Please use Section.RemoveMultipleElements instead.")"""
        ...
    def RemoveMultiplePoints(self, points: typing.List[Point], featureMode: Section.Mode) -> None:
        """[Obsolete("Deprecated in NX8.5.0.  Please use Section.RemoveMultipleElements instead.")"""
        ...
    def RemoveUnderlyingCurve(self, pointSpecifyingCurve: Point3d, tolerance: float, featureMode: Section.Mode) -> None:
        ...
    def RemoveMultipleElements(self, wfs: typing.List[ICurve], startConnectors: typing.List[NXObject], endConnectors: typing.List[NXObject], isCombinationsResultIntoOnlyOneCurvePerCombination: bool, pointsOnCurvesToBeRemoved: typing.List[Point3d], points: typing.List[Point], featureMode: Section.Mode) -> None:
        ...
    def CloneSection(self) -> Section:
        ...
    def PrepareMappingData(self) -> None:
        ...
    def CleanMappingData(self) -> None:
        ...
    def GetAllowedEntityTypes(self) -> Section.AllowTypes:
        ...
    def SetAllowedEntityTypes(self, allowedEntityTypes: Section.AllowTypes) -> None:
        ...
    def MapSectionElements(self, oldWf: NXObject, newWf: NXObject) -> None:
        ...
    def GetOutputCurves(self, outputs: typing.List[NXObject]) -> None:
        ...
    def GetOldOutputCurves(self, oldOutputs: typing.List[NXObject]) -> None:
        ...
    def DeselectPortion(self, seedPoint: Point3d, startLimit: NXObject, endLimit: NXObject, deselectionType: Section.DeselectOption) -> None:
        ...
    def AddChainBetweenIntersectionPoints(self, rules: typing.List[SelectionIntentRule], startConnector: NXObject, startIntersectionPoint: Point3d, endConnector: NXObject, endIntersectionPoint: Point3d, seed: NXObject, helpPoint: Point3d, featureMode: Section.Mode, chainWithinFeature: bool) -> None:
        ...
    def SkipSorting(self, skipSorting: bool) -> None:
        ...
    def EvaluateAndAskOutputEntities(self, refs: typing.List[NXObject]) -> None:
        ...
    def GetMultiComponent(self) -> bool:
        ...
    def SetMultiComponent(self) -> None:
        ...
    def GetNonFeatureMode(self) -> bool:
        ...
    def SetNonFeatureMode(self) -> None:
        ...
    def SetAllowRefCrvs(self, allowRefCrvs: bool) -> None:
        ...
    def GetSectionData(self, withOccurrenceInfo: bool, sectionData: typing.List[SectionData]) -> None:
        ...
    AngleTolerance: float
    ChainingTolerance: float
    DistanceTolerance: float


    class Mode(enum.Enum):
        Create = 0
        Edit = 1
    

    class DeselectOption(enum.Enum):
        SectionBetweenIntersection = 0
        CurveBetweenIntersection = 1
    

    class AllowTypes(enum.Enum):
        Uninitialized = 0
        OnlyCurves = 1
        OnlyPoints = 2
        CurvesAndPoints = 3
    

class ScRuleFactory(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateRuleOptions(self) -> SelectionIntentRuleOptions:
        ...
    def CreateRuleEdgeDumb(self, edges: typing.List[Edge]) -> EdgeDumbRule:
        ...
    def CreateRuleEdgeDumb(self, edges: typing.List[Edge], options: SelectionIntentRuleOptions) -> EdgeDumbRule:
        ...
    def CreateRuleEdgeChain(self, startEdge: Edge, endEdge: Edge, isFromStart: bool) -> EdgeChainRule:
        ...
    def CreateRuleEdgeMultipleSeedTangent(self, seedEdges: typing.List[Edge], angleTolerance: float, hasSameConvexity: bool) -> EdgeMultipleSeedTangentRule:
        ...
    def CreateRuleEdgeMultipleSeedTangent(self, seedEdges: typing.List[Edge], angleTolerance: float, hasSameConvexity: bool, options: SelectionIntentRuleOptions) -> EdgeMultipleSeedTangentRule:
        ...
    def CreateRuleEdgeTangent(self, startEdge: Edge, endEdge: Edge, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool) -> EdgeTangentRule:
        ...
    def CreateRuleEdgeFace(self, faces: typing.List[Face]) -> EdgeFaceRule:
        ...
    def CreateRuleEdgeFace(self, faces: typing.List[Face], options: SelectionIntentRuleOptions) -> EdgeFaceRule:
        ...
    def CreateRuleEdgeBody(self, body: Body) -> EdgeBodyRule:
        ...
    def CreateRuleEdgeBody(self, body: Body, options: SelectionIntentRuleOptions) -> EdgeBodyRule:
        ...
    def CreateRuleEdgeFeature(self, features: typing.List[Features.Feature]) -> EdgeFeatureRule:
        ...
    def CreateRuleEdgeFeature(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject) -> EdgeFeatureRule:
        ...
    def CreateRuleEdgeFeature(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject, options: SelectionIntentRuleOptions) -> EdgeFeatureRule:
        ...
    def CreateRuleEdgeSheetBoundary(self, sheet: Body) -> EdgeSheetBoundaryRule:
        ...
    def CreateRuleEdgeSheetBoundary(self, sheet: Body, options: SelectionIntentRuleOptions) -> EdgeSheetBoundaryRule:
        ...
    def CreateRuleEdgeBoundary(self, facesOfFeatures: typing.List[Face]) -> EdgeBoundaryRule:
        ...
    def CreateRuleEdgeBoundary(self, facesOfFeatures: typing.List[Face], options: SelectionIntentRuleOptions) -> EdgeBoundaryRule:
        ...
    def CreateRuleEdgeIntersect(self, facesOfFeatures1: typing.List[Face], facesOfFeatures2: typing.List[Face]) -> EdgeIntersectRule:
        ...
    def CreateRuleEdgeIntersect(self, facesOfFeatures1: typing.List[Face], facesOfFeatures2: typing.List[Face], options: SelectionIntentRuleOptions) -> EdgeIntersectRule:
        ...
    def CreateRuleEdgeVertex(self, startEdge: Edge, isFromStart: bool) -> EdgeVertexRule:
        ...
    def CreateRuleEdgeVertex(self, startEdge: Edge, isFromStart: bool, options: SelectionIntentRuleOptions) -> EdgeVertexRule:
        ...
    def CreateRuleEdgeVertexTangent(self, startEdge: Edge, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool) -> EdgeVertexTangentRule:
        ...
    def CreateRuleEdgeVertexTangent(self, startEdge: Edge, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool, options: SelectionIntentRuleOptions) -> EdgeVertexTangentRule:
        ...
    def CreateRuleCurveDumb(self, curves: typing.List[Curve]) -> CurveDumbRule:
        ...
    def CreateRuleCurveDumb(self, curves: typing.List[Curve], options: SelectionIntentRuleOptions) -> CurveDumbRule:
        ...
    def CreateRuleBaseCurveDumb(self, curves: typing.List[IBaseCurve]) -> CurveDumbRule:
        ...
    def CreateRuleBaseCurveDumb(self, curves: typing.List[IBaseCurve], options: SelectionIntentRuleOptions) -> CurveDumbRule:
        ...
    def CreateRuleCurveDumbFromPoints(self, points: typing.List[Point]) -> CurveDumbRule:
        ...
    def CreateRuleCurveDumbFromPoints(self, points: typing.List[Point], options: SelectionIntentRuleOptions) -> CurveDumbRule:
        ...
    def CreateRuleCurveFeature(self, features: typing.List[Features.Feature]) -> CurveFeatureRule:
        ...
    def CreateRuleCurveFeature(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject) -> CurveFeatureRule:
        ...
    def CreateRuleCurveFeature(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject, options: SelectionIntentRuleOptions) -> CurveFeatureRule:
        ...
    def CreateRuleCurveFeatureChain(self, features: typing.List[Features.Feature], seedCurve: Curve, endCurve: Curve, isFromSeedStart: bool, gapTolerance: float) -> CurveFeatureChainRule:
        ...
    def CreateRuleCurveFeatureChain(self, features: typing.List[Features.Feature], seedCurve: Curve, endCurve: Curve, isFromSeedStart: bool, gapTolerance: float, options: SelectionIntentRuleOptions) -> CurveFeatureChainRule:
        ...
    def CreateRuleCurveFeatureTangent(self, features: typing.List[Features.Feature], seedCurve: Curve, endCurve: Curve, isFromSeedStart: bool, angleTolerance: float, gapTolerance: float) -> CurveFeatureTangentRule:
        ...
    def CreateRuleCurveFeatureTangent(self, features: typing.List[Features.Feature], seedCurve: Curve, endCurve: Curve, isFromSeedStart: bool, angleTolerance: float, gapTolerance: float, options: SelectionIntentRuleOptions) -> CurveFeatureTangentRule:
        ...
    def CreateRuleFollowFillet(self, features: typing.List[Features.Feature], bodies: typing.List[Body], basicCurves: typing.List[ICurve], seedWireframe: ICurve, endWireframe: ICurve, isFromSeedStart: bool, seedPoint: Point3d, gapTolerance: float, angleTolerance: float, method: FollowFilletRuleType) -> FollowFilletRule:
        ...
    def CreateRuleFeaturePoints(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject) -> FeaturePointsRule:
        ...
    def CreateRuleFeaturePoints(self, features: typing.List[Features.Feature]) -> FeaturePointsRule:
        ...
    def CreateRuleFeaturePoints(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject, options: SelectionIntentRuleOptions) -> FeaturePointsRule:
        ...
    def CreateRuleRegionBoundary(self, seedObj: DisplayableObject, curves: typing.List[ICurve], seedPoint: Point3d, distanceTolerance: float) -> RegionBoundaryRule:
        ...
    def CreateRuleRegionBoundary(self, seedObj: DisplayableObject, curves: typing.List[ICurve], seedPoint: Point3d, distanceTolerance: float, options: SelectionIntentRuleOptions) -> RegionBoundaryRule:
        ...
    def CreateRuleFaceDumb(self, faces: typing.List[Face]) -> FaceDumbRule:
        ...
    def CreateRuleFaceDumb(self, faces: typing.List[Face], options: SelectionIntentRuleOptions) -> FaceDumbRule:
        ...
    def CreateRuleFaceDatum(self, faces: typing.List[DatumPlane]) -> FaceDumbRule:
        ...
    def CreateRuleFaceDatum(self, faces: typing.List[DatumPlane], options: SelectionIntentRuleOptions) -> FaceDumbRule:
        ...
    def CreateRuleFaceTangent(self, seedFace: Face, boundaryFaces: typing.List[Face]) -> FaceTangentRule:
        ...
    def CreateRuleFaceTangent(self, seedFace: Face, boundaryFaces: typing.List[Face], angleTolerance: float) -> FaceTangentRule:
        ...
    def CreateRuleFaceTangent(self, seedFace: Face, boundaryFaces: typing.List[Face], angleTolerance: float, options: SelectionIntentRuleOptions) -> FaceTangentRule:
        ...
    def CreateRuleFaceBody(self, body: Body) -> FaceBodyRule:
        ...
    def CreateRuleFaceBody(self, body: Body, options: SelectionIntentRuleOptions) -> FaceBodyRule:
        ...
    def CreateRuleFaceRegion(self, seedFace: Face, boundaryFaces: typing.List[Face]) -> FaceRegionRule:
        ...
    def CreateRuleFaceRegion(self, seedFace: Face, boundaryFaces: typing.List[Face], options: SelectionIntentRuleOptions) -> FaceRegionRule:
        ...
    def CreateRuleFaceFeature(self, features: typing.List[Features.Feature]) -> FaceFeatureRule:
        ...
    def CreateRuleFaceFeature(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject) -> FaceFeatureRule:
        ...
    def CreateRuleFaceFeature(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject, options: SelectionIntentRuleOptions) -> FaceFeatureRule:
        ...
    def CreateRuleFaceAdjacent(self, seedFace: Face) -> FaceAdjacentRule:
        ...
    def CreateRuleFaceAdjacent(self, seedFace: Face, options: SelectionIntentRuleOptions) -> FaceAdjacentRule:
        ...
    def CreateRuleFaceConnectedBlend(self, seedFace: Face) -> FaceConnectedBlendRule:
        ...
    def CreateRuleFaceConnectedBlend(self, seedFace: Face, includeBlendLike: bool, feature: Features.Feature) -> FaceConnectedBlendRule:
        ...
    def CreateRuleFaceConnectedBlend(self, seedFace: Face, includeBlendLike: bool, includeUnlabeledBlend: bool, feature: Features.Feature) -> FaceConnectedBlendRule:
        ...
    def CreateRuleFaceConnectedBlend(self, seedFace: Face, includeBlendLike: bool, includeUnlabeledBlend: bool, feature: Features.Feature, options: SelectionIntentRuleOptions) -> FaceConnectedBlendRule:
        ...
    def CreateRuleFaceAllBlend(self, body: Body) -> FaceAllBlendRule:
        ...
    def CreateRuleFaceAllBlend(self, body: Body, feature: Features.Feature) -> FaceAllBlendRule:
        ...
    def CreateRuleFaceAllBlend(self, body: Body, feature: Features.Feature, options: SelectionIntentRuleOptions) -> FaceAllBlendRule:
        ...
    def CreateRuleFaceRib(self, seed: Face) -> FaceRibFacesRule:
        ...
    def CreateRuleFaceRib(self, seed: Face, includeBoundaryBlends: bool, traverseInteriorLoops: bool) -> FaceRibFacesRule:
        ...
    def CreateRuleFaceRib(self, seed: Face, includeBoundaryBlends: bool, traverseInteriorLoops: bool, options: SelectionIntentRuleOptions) -> FaceRibFacesRule:
        ...
    def CreateRuleFaceMergedRib(self, seed: Face, edge: Edge) -> FaceMergedRibFacesRule:
        ...
    def CreateRuleFaceMergedRib(self, seed: Face, edge: Edge, includeBoundaryBlends: bool) -> FaceMergedRibFacesRule:
        ...
    def CreateRuleFaceMergedRib(self, seed: Face, includeBoundaryBlends: bool, seedPoint: Point3d) -> FaceMergedRibFacesRule:
        ...
    def CreateRuleFaceMergedRib(self, seed: Face, includeBoundaryBlends: bool, seedPoint: Point3d, options: SelectionIntentRuleOptions) -> FaceMergedRibFacesRule:
        ...
    def CreateRuleFaceSlot(self, seed: Face) -> FaceSlotFacesRule:
        ...
    def CreateRuleFaceSlot(self, seed: Face, includeBoundaryBlends: bool, traverseInteriorLoops: bool) -> FaceSlotFacesRule:
        ...
    def CreateRuleFaceSlot(self, seed: Face, includeBoundaryBlends: bool, traverseInteriorLoops: bool, options: SelectionIntentRuleOptions) -> FaceSlotFacesRule:
        ...
    def CreateRuleFaceBossPocket(self, seed: Face) -> FaceBossPocketFacesRule:
        ...
    def CreateRuleFaceBossPocket(self, seed: Face, includeBoundaryBlends: bool) -> FaceBossPocketFacesRule:
        ...
    def CreateRuleFaceBossPocket(self, seed: Face, includeBoundaryBlends: bool, options: SelectionIntentRuleOptions) -> FaceBossPocketFacesRule:
        ...
    def CreateRuleFaceTangentWithSmartBoundaries(self, seedFace: Face, boundaryFaceRules: typing.List[SelectionIntentRule]) -> FaceTangentRule:
        ...
    def CreateRuleFaceTangentWithSmartBoundaries(self, seedFace: Face, boundaryFaceRules: typing.List[SelectionIntentRule], options: SelectionIntentRuleOptions) -> FaceTangentRule:
        ...
    def CreateRuleFaceRegionWithSmartBoundaries(self, seedFace: Face, boundaryFaceRules: typing.List[SelectionIntentRule]) -> FaceRegionRule:
        ...
    def CreateRuleFaceRegionWithSmartBoundaries(self, seedFace: Face, boundaryFaceRules: typing.List[SelectionIntentRule], options: SelectionIntentRuleOptions) -> FaceRegionRule:
        ...
    def CreateRuleFaceRegionBoundary(self, seedObj: Face, curves: typing.List[ICurve], seedPoint: Point3d, distanceTolerance: float) -> FaceRegionBoundaryRule:
        ...
    def CreateRuleFaceRegionBoundary(self, seedObj: Face, curves: typing.List[ICurve], seedPoint: Point3d, distanceTolerance: float, options: SelectionIntentRuleOptions) -> FaceRegionBoundaryRule:
        ...
    def CreateRuleFaceAndAdjacentFaces(self, seedFace: Face) -> FaceAndAdjacentFacesRule:
        ...
    def CreateRuleFaceAndAdjacentFaces(self, seedFace: Face, options: SelectionIntentRuleOptions) -> FaceAndAdjacentFacesRule:
        ...
    def CreateRuleCurveGroup(self, groups: typing.List[Group]) -> CurveGroupRule:
        ...
    def CreateRuleCurveGroup(self, groups: typing.List[Group], options: SelectionIntentRuleOptions) -> CurveGroupRule:
        ...
    def CreateRuleBodyDumb(self, bodies: typing.List[Body]) -> BodyDumbRule:
        ...
    def CreateRuleBodyDumb(self, bodies: typing.List[Body], includeSheetBodies: bool) -> BodyDumbRule:
        ...
    def CreateRuleBodyDumb(self, bodies: typing.List[Body], includeSheetBodies: bool, options: SelectionIntentRuleOptions) -> BodyDumbRule:
        ...
    def CreateRuleBodyFeature(self, features: typing.List[Features.Feature]) -> BodyFeatureRule:
        ...
    def CreateRuleBodyFeature(self, features: typing.List[Features.Feature], includeSheetBodies: bool) -> BodyFeatureRule:
        ...
    def CreateRuleBodyFeature(self, features: typing.List[Features.Feature], partOccurrence: DisplayableObject) -> BodyFeatureRule:
        ...
    def CreateRuleBodyFeature(self, features: typing.List[Features.Feature], includeSheetBodies: bool, partOccurrence: DisplayableObject) -> BodyFeatureRule:
        ...
    def CreateRuleBodyFeature(self, features: typing.List[Features.Feature], includeSheetBodies: bool, partOccurrence: DisplayableObject, options: SelectionIntentRuleOptions) -> BodyFeatureRule:
        ...
    def CreateRuleBodyGroup(self, groups: typing.List[Group]) -> BodyGroupRule:
        ...
    def CreateRuleBodyGroup(self, groups: typing.List[Group], includeSheetBodies: bool) -> BodyGroupRule:
        ...
    def CreateRuleBodyGroup(self, groups: typing.List[Group], includeSheetBodies: bool, options: SelectionIntentRuleOptions) -> BodyGroupRule:
        ...
    def CreateRuleFollowFillet(self, features: typing.List[Features.Feature], bodies: typing.List[Body], basicCurves: typing.List[ICurve], seedWireframe: ICurve, seedPoint: Point3d, gapTolerance: float, angleTolerance: float, method: FollowFilletRuleType) -> FollowFilletRule:
        ...
    def CreateRuleFollowFillet(self, features: typing.List[Features.Feature], bodies: typing.List[Body], basicCurves: typing.List[ICurve], seedWireframe: ICurve, seedPoint: Point3d, gapTolerance: float, angleTolerance: float, method: FollowFilletRuleType, options: SelectionIntentRuleOptions) -> FollowFilletRule:
        ...
    def CreateRuleFollowFillet(self, features: typing.List[Features.Feature], bodies: typing.List[Body], basicCurves: typing.List[ICurve], seedWireframe: ICurve, endWireframe: ICurve, isFromSeedStart: bool, seedPoint: Point3d, gapTolerance: float, angleTolerance: float, method: FollowFilletRuleType, options: SelectionIntentRuleOptions) -> FollowFilletRule:
        ...
    def CreateRuleEdgeChain(self, startEdge: Edge, endEdge: Edge, isFromStart: bool, commonFace: Face, allowLaminarEdge: bool) -> EdgeChainRule:
        ...
    def CreateRuleEdgeChain(self, startEdge: Edge, endEdge: Edge, isFromStart: bool, commonFace: Face, allowLaminarEdge: bool, options: SelectionIntentRuleOptions) -> EdgeChainRule:
        ...
    def CreateRuleEdgeTangent(self, startEdge: Edge, endEdge: Edge, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool, allowLaminarEdge: bool) -> EdgeTangentRule:
        ...
    def CreateRuleEdgeTangent(self, startEdge: Edge, endEdge: Edge, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool, allowLaminarEdge: bool, options: SelectionIntentRuleOptions) -> EdgeTangentRule:
        ...
    def CreateRuleApparentChaining(self, seedCurve: ICurve, view: View, chainingMethod: ApparentChainingRuleType, selectionMask: ApparentChainingRuleSelection, chainingTolerance: float, angleTolerance: float) -> ApparentChainingRule:
        ...
    def CreateRuleApparentChaining(self, seedCurve: ICurve, view: View, chainingMethod: ApparentChainingRuleType, selectionMask: ApparentChainingRuleSelection, chainingTolerance: float, angleTolerance: float, options: SelectionIntentRuleOptions) -> ApparentChainingRule:
        ...
    def CreateRuleOuterEdgesOfFaces(self, facesOfFeatures: typing.List[NXObject]) -> OuterEdgesOfFacesRule:
        ...
    def CreateRuleOuterEdgesOfFaces(self, facesOfFeatures: typing.List[NXObject], options: SelectionIntentRuleOptions) -> OuterEdgesOfFacesRule:
        ...
    def CreateRuleRibTopFaceEdges(self, facesOfFeatures: typing.List[NXObject]) -> RibTopFaceEdgesRule:
        ...
    def CreateRuleRibTopFaceEdges(self, facesOfFeatures: typing.List[NXObject], options: SelectionIntentRuleOptions) -> RibTopFaceEdgesRule:
        ...
    def CreateRuleCurveChain(self, seedCurve: ICurve, endCurve: ICurve, isFromSeedStart: bool, gapTolerance: float) -> CurveChainRule:
        ...
    def CreateRuleCurveChain(self, seedCurve: ICurve, endCurve: ICurve, isFromSeedStart: bool, gapTolerance: float, options: SelectionIntentRuleOptions) -> CurveChainRule:
        ...
    def CreateRuleCurveTangent(self, seedCurve: ICurve, endCurve: ICurve, isFromSeedStart: bool, angleTolerance: float, gapTolerance: float) -> CurveTangentRule:
        ...
    def CreateRuleCurveTangent(self, seedCurve: ICurve, endCurve: ICurve, isFromSeedStart: bool, angleTolerance: float, gapTolerance: float, options: SelectionIntentRuleOptions) -> CurveTangentRule:
        ...
    def CreateRuleFeatureIntersectionEdges(self, features: typing.List[NXObject]) -> FeatureIntersectionEdgesRule:
        ...
    def CreateRuleFeatureIntersectionEdges(self, features: typing.List[NXObject], partOccurrence: DisplayableObject) -> FeatureIntersectionEdgesRule:
        ...
    def CreateRuleFeatureIntersectionEdges(self, features: typing.List[NXObject], partOccurrence: DisplayableObject, options: SelectionIntentRuleOptions) -> FeatureIntersectionEdgesRule:
        ...
    def CreateRuleFaceHole(self, seed: Face, options: SelectionIntentRuleOptions) -> FaceHoleFacesRule:
        ...
    def Tag(self) -> Tag: ...



class ScrewJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    Anchor: VectorArithmetic.Vector3
    Axis: VectorArithmetic.Vector3
    LinearPosition: float
    AngularPosition: float
    Active: bool
    Ratio: float


    class ScrewJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class ScEvaluationFiltertype(enum.Enum):
    SleepyEntity = 1
    LaminarEdge = 2
    MinimumBody = 3
    SheetBody = 4
    FacetEntity = 5


class ScCollectorList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[ScCollector]) -> None:
        ...
    def Append(self, object: ScCollector) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: ScCollector) -> int:
        ...
    def FindItem(self, index: int) -> ScCollector:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: ScCollector) -> None:
        ...
    def Erase(self, obj: ScCollector, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[ScCollector]:
        ...
    def SetContents(self, objects: typing.List[ScCollector]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: ScCollector, object2: ScCollector) -> None:
        ...
    def Insert(self, location: int, object: ScCollector) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ScCollectorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[ScCollector]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateCollector(self) -> ScCollector:
        ...
    def Tag(self) -> Tag: ...



class ScCollectorAllowTypes(enum.Enum):
    Uninitialized = 0
    OnlyCurves = 1
    OnlyPoints = 2
    CurvesAndPoints = 3


class ScCollector(DisplayableObject):
    def __init__(self) -> None: ...
    def ReplaceRules(self, rules: typing.List[SelectionIntentRule], createRulesWoUpdate: bool) -> None:
        ...
    def ReplaceRules(self, rules: typing.List[SelectionIntentRule], negatedEntities: typing.List[DisplayableObject], createRulesWoUpdate: bool) -> None:
        ...
    def Destroy(self) -> None:
        ...
    def GetObjects(self) -> typing.List[TaggedObject]:
        ...
    def GetRules(self, rules: typing.List[SelectionIntentRule]) -> None:
        ...
    def SetInterpart(self, interpart: bool) -> None:
        ...
    def RemoveRule(self, ruleIndex: int) -> None:
        ...
    def RemoveRules(self, rules: typing.List[SelectionIntentRule]) -> None:
        ...
    def CopyCollector(self) -> ScCollector:
        ...
    def GetMultiComponent(self) -> bool:
        ...
    def SetMultiComponent(self) -> None:
        ...
    def GetNonFeatureMode(self) -> bool:
        ...
    def SetNonFeatureMode(self) -> None:
        ...
    def GetObjectsSortedById(self) -> typing.List[TaggedObject]:
        ...
    def AddEvaluationFilter(self, filterType: ScEvaluationFiltertype) -> None:
        ...
    def RemoveEvaluationFilter(self, filterType: ScEvaluationFiltertype) -> None:
        ...
    def IsEvaluationFilterEnabled(self, filterType: ScEvaluationFiltertype) -> bool:
        ...
    def SetAllowRefCurves(self, allowRefCurves: bool) -> None:
        ...
    def GetAllowedWireframeType(self) -> ScCollectorAllowTypes:
        ...
    def SetAllowedWireframeType(self, allowedEntityTypes: ScCollectorAllowTypes) -> None:
        ...
    def RemoveMissingParents(self) -> None:
        ...
    def GetCustomRule(self) -> Features.CustomRule:
        ...


class ScalarTableValue(GeneralScalarTable):
    def __init__(self, ptr: int) -> None: ...


class ScalarMatrixValue(GeneralScalarTable):
    def __init__(self, ptr: int) -> None: ...
    Units: Unit


class ScalarCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Scalar]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateScalar(self, value: float, dimensionality: Scalar.DimensionalityType, update: SmartObject.UpdateOption) -> Scalar:
        ...
    def CreateScalar(self, scalarExtract: Scalar, scalarOptional: Scalar, dimensionality: Scalar.DimensionalityType, update: SmartObject.UpdateOption) -> Scalar:
        ...
    def CreateScalarExpression(self, expression: Expression, dimensionality: Scalar.DimensionalityType, update: SmartObject.UpdateOption) -> Scalar:
        ...
    def CreateScalarReciprocalValue(self, scalar: Scalar, dimensionality: Scalar.DimensionalityType, update: SmartObject.UpdateOption) -> Scalar:
        ...
    def Tag(self) -> Tag: ...



class Scalar(SmartObject):
    def __init__(self) -> None: ...
    Dimensionality: Scalar.DimensionalityType
    MeasurementName: str
    Value: float


    class DimensionalityType(enum.Enum):
        None = 0
        Length = 1
        Area = 2
        Volume = 3
        Mass = 4
        Angle = 5
        Force = 6
    

class SaveOptions(Utilities.NXRemotableObject):
    def __init__(self, owner: PartCollection) -> None: ...
    def Tag(self) -> Tag: ...

    FamilyDefaultDirectory: str
    TrueShapeData: bool
    VisualizationData: bool


class RuntimeParameters(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetNumParameters(self) -> int:
        ...
    def GetParameter(self, nProp: int) -> Parameter:
        ...
    def SetParameter(self, nProp: int, value: Parameter) -> None:
        ...


    class RuntimeParameters.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class RuntimeObject(System.Object):

    def __init__(self, pItem: int) -> None: ...
    def Finalize(self) -> None:
        ...
    def Dispose(self) -> None:
        ...
    def AskAssembly(self) -> ComponentPart:
        ...
    def GetPhysicsObject(self) -> Tag:
        ...
    Active: bool


class RuntimeNC(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    IsRun: bool
    IsPause: bool
    IsFinished: bool
    IsToolChanged: bool


    class RuntimeNC.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class RuntimeButton(ShapeBody):
    def __init__(self, pItem: int) -> None: ...
    Triggered: bool
    Active: bool


    class RuntimeButton.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class RuleManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def Initialize(self, licenseToTake: RuleManager.LicenseType, intentStatus: int) -> RuleManager.InitializationStatusType:
        ...
    def CreateDynamicRule(self, referenceChain: str, ruleName: str, ruleType: RuleManager.RuleType, ruleText: str) -> None:
        ...
    def CreateDynamicRule(self, referenceChain: str, ruleName: str, behaviors: str, ruleUnits: str, ruleText: str, leadingComment: str) -> None:
        ...
    def CreateDynamicRule(self, referenceChain: str, ruleName: str, behaviors: str, ruleText: str, leadingComment: str) -> None:
        ...
    def DoKfUpdate(self, undoMark: Session.UndoMarkId) -> int:
        ...
    def DeleteDynamicRule(self, referenceChain: str, ruleName: str) -> None:
        ...
    def CreateChildRule(self, ruleName: str, className: str, parameters: typing.List[RuleManager.ParameterRule]) -> None:
        ...
    def DeleteChildRule(self, ruleName: str) -> None:
        ...
    def RemoveRuleOnly(self, referenceChain: str) -> None:
        ...
    def IsUserClass(self, className: str) -> bool:
        ...
    def GetRulesOfClass(self, className: str) -> str:
        ...
    def GetDynamicRules(self, childRuleName: str) -> str:
        ...
    def GetSpecifiedParameters(self, referenceChain: str) -> str:
        ...
    def GetParameterFormula(self, referenceChain: str, parameterName: str) -> str:
        ...
    def Rename(self, referenceChain: str, newName: str) -> None:
        ...
    def Copy(self, oldNameChain: str, oldLeafName: str, newNameChain: str, newLeafName: str) -> None:
        ...
    def GetClass(self, referenceChain: str) -> str:
        ...
    def GetClassesOfChildList(self, referenceChain: str) -> str:
        ...
    def GetDependents(self, referenceChain: str) -> str:
        ...
    def GetDependencies(self, referenceChain: str) -> str:
        ...
    def GetRuleType(self, className: str, ruleName: str) -> RuleManager.RuleType:
        ...
    def GetRuleType(self, referenceChain: str) -> RuleManager.RuleType:
        ...
    def GetParameterType(self, referenceChain: str) -> RuleManager.RuleType:
        ...
    def IsChildRule(self, className: str, ruleName: str) -> bool:
        ...
    def IsChildRule(self, referenceChain: str) -> bool:
        ...
    def IsChildList(self, className: str, ruleName: str) -> bool:
        ...
    def IsChildList(self, referenceChain: str) -> bool:
        ...
    def IsUncached(self, className: str, ruleName: str) -> bool:
        ...
    def IsUncached(self, referenceChain: str) -> bool:
        ...
    def IsHidden(self, className: str, ruleName: str) -> bool:
        ...
    def IsHidden(self, referenceChain: str) -> bool:
        ...
    def IsLocal(self, className: str, ruleName: str) -> bool:
        ...
    def IsParameter(self, className: str, ruleName: str) -> bool:
        ...
    def IsCanonical(self, className: str, ruleName: str) -> bool:
        ...
    def IsModifiable(self, className: str, ruleName: str) -> bool:
        ...
    def IsModifiable(self, referenceChain: str) -> bool:
        ...
    def IsMethod(self, className: str, ruleName: str) -> bool:
        ...
    def IsMethod(self, referenceChain: str) -> bool:
        ...
    def IsComputed(self, referenceChain: str) -> bool:
        ...
    def RebuildTrees(self) -> None:
        ...
    def IsRuleInClass(self, className: str, ruleName: str) -> bool:
        ...
    def GetDefaultFormula(self, className: str, ruleName: str) -> str:
        ...
    def Evaluate(self, referenceChain: str) -> any:
        ...
    def EvaluateAsString(self, referenceChain: str) -> str:
        ...
    def EvaluateAnyAsString(self, referenceChain: str) -> str:
        ...
    def GetNameChain(self, ugObject: NXObject) -> str:
        ...
    def RegenerateAll(self) -> None:
        ...
    def SyntaxCheck(self, fileName: str) -> None:
        ...
    def GetAncestorClasses(self, className: str) -> str:
        ...
    def Reload(self, refreshUserClassDir: bool) -> None:
        ...
    def ReloadSingleClass(self, className: str) -> None:
        ...
    def ReloadClassesAndFunctions(self, classes: str, functions: str) -> None:
        ...
    def GetRuleTypes(self) -> str:
        ...
    def GetClasses(self, filter: RuleManager.Filter) -> str:
        ...
    def GetFunctions(self, filter: RuleManager.Filter, doSort: bool) -> str:
        ...
    def RemoveAllRules(self) -> None:
        ...
    def ReadDfaFile(self, fileName: str) -> str:
        ...
    def WriteDfaFile(self, fileName: str, fileString: str, replace: bool) -> None:
        ...
    def GetClassDfaFile(self, className: str) -> str:
        ...
    def GetLastError(self) -> str:
        ...
    def GetReferenceText(self, ugObject: NXObject) -> str:
        ...
    def GetObjectText(self, ugObject: NXObject) -> str:
        ...
    def AdoptObjects(self, ugObjects: typing.List[NXObject]) -> bool:
        ...
    def GetAdoptableTypes(self) -> typing.List[RuleManager.AdoptableTypes]:
        ...
    def GetRulesForObjects(self, ugObjects: typing.List[NXObject]) -> str:
        ...
    def GetFunctionInformation(self, functionName: str, instanceOrClassName: str, isInstance: bool, briefOnly: bool) -> RuleManager.FunctionInformation:
        ...
    def GetFunctionArgumentsInformation(self, functionName: str, instanceOrClassName: str, isInstance: bool, briefOnly: bool) -> typing.List[RuleManager.FunctionArgumentsInformation]:
        ...
    def GetFunctionFile(self, functionName: str) -> str:
        ...
    def IsUserFunction(self, functionName: str) -> bool:
        ...
    def IsExpressionRule(self, ruleName: str) -> bool:
        ...
    def GetDynamicRuleText(self, referenceChain: str) -> str:
        ...
    def GetDebugInstances(self, instances: typing.List[RuleManager.DebugInstance], rules: typing.List[RuleManager.DebugRule]) -> None:
        ...
    def GetErrorStart(self) -> int:
        ...
    def GetErrorEnd(self) -> int:
        ...
    def GetObjectOfInstance(self, nameChain: str) -> NXObject:
        ...
    def Tag(self) -> Tag: ...

    CreateMode: bool
    DebugFlag: bool


    class RuleType(enum.Enum):
        Boolean = 0
        Frame = 1
        Integer = 2
        List = 3
        Name = 4
        Number = 5
        Point = 6
        String = 7
        Vector = 8
        Instance = 9
        Any = 10
        HostPointer = 11
    

    class RuleManagerParameterRule():
        Name: str
        Rule: str
        def ToString(self) -> str:
            ...
        def __init__(self, Name: str, Rule: str) -> None: ...
    

    class LicenseType(enum.Enum):
        NoLicense = 0
        Author = 1
        Execute = 2
        Pipeline = 3
        KfFeature = 4
        KfInterop = 5
        KfNewGeom = 6
        KfChecking = 7
    

    class InitializationStatusType(enum.Enum):
        Success = 0
        Failure = 1
        Unavailable = 2
        UnableToObtainLicense = 3
        CloseFailure = 4
    

    class RuleManagerFunctionInformation():
        ReturnType: str
        NumArguments: int
        BriefDescription: str
        FullDescription: str
        ReturnDescription: str
        IsDynamic: bool
        DesignLogic: bool
        SeeAlso: str
        def ToString(self) -> str:
            ...
    

    class RuleManagerFunctionArgumentsInformation():
        ArgumentName: str
        ArgumentType: str
        ArgumentStyle: str
        ArgumentDefault: str
        ArgumentDimensionality: str
        ArgumentDescription: str
        ArgumentSelectionTypes: str
        def ToString(self) -> str:
            ...
    

    class Filter(enum.Enum):
        User = 0
        System = 1
        Both = 2
        UserPlus = 3
        UserLoaded = 4
        SystemLoaded = 5
        BothLoaded = 6
        UserPlusLoaded = 7
    

    class RuleManagerDebugRule():
        Unit: str
        Name: str
        Formula: str
        Type: str
        Value: str
        def ToString(self) -> str:
            ...
    

    class RuleManagerDebugInstance():
        PartName: str
        RefChain: str
        NhaChain: str
        NRules: int
        Rules0: int
        def ToString(self) -> str:
            ...
    

    class RuleManagerAdoptableTypes():
        ObjectType: int
        ObjectSubtype: int
        FeatureType: int
        def ToString(self) -> str:
            ...
        def __init__(self, ObjectType: int, ObjectSubtype: int, FeatureType: int) -> None: ...
    

    class RuleManager_ParameterRule():
        name: int
        rule: int
    

    class RuleManager_FunctionInformation():
        return_type: int
        num_arguments: int
        brief_description: int
        full_description: int
        return_description: int
        is_dynamic: bool
        design_logic: bool
        see_also: int
    

    class RuleManager_FunctionArgumentsInformation():
        argument_name: int
        argument_type: int
        argument_style: int
        argument_default: int
        argument_dimensionality: int
        argument_description: int
        argument_selection_types: int
    

    class RuleManager_DebugRule():
        unit: int
        name: int
        formula: int
        type: int
        value: int
    

    class RuleManager_DebugInstance():
        part_name: int
        ref_chain: int
        nha_chain: int
        n_rules: int
        rules0: int
    

class RoughBrushFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, roughBrushToolStartPoint: Point3d, roughBrushToolDirection: Vector3d, roughBrushToolRadius: float, seedFacet: IFacet) -> None:
        ...


class RotationDirection(enum.Enum):
    RightHand = 0
    LeftHand = 1


class RigidBody(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def Copy(self) -> RigidBody:
        ...
    def ActivateAll(self, bActive: bool) -> None:
        ...
    def ApplyForce(self, force: VectorArithmetic.Vector3) -> None:
        ...
    def ApplyTorque(self, torque: VectorArithmetic.Vector3) -> None:
        ...
    Parts: typing.List[ShapeBody]
    Active: bool
    Position: VectorArithmetic.Vector3
    Orientation: VectorArithmetic.Matrix3
    LinearVelocity: VectorArithmetic.Vector3
    AngularVelocity: VectorArithmetic.Vector3
    Mass: float
    Inertia: VectorArithmetic.Vector3


    class RigidBody.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class RibTopFaceEdgesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, facesOfFeatures: typing.List[NXObject]) -> None:
        ...


class ReplaceExpressionsBuilder(Builder):
    def __init__(self) -> None: ...
    def SetSelectedExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    CurrentString: str
    FilterMatchCase: bool
    FilterWholeWord: bool
    ReplaceString: str
    ReplaceType: ReplaceExpressionsBuilder.ReplacementTypes
    SearchString: str
    UpdateString: str


    class ReplacementTypes(enum.Enum):
        ExpressionName = 0
        GenericString = 1
    

class RemoteUtilities(TaggedObject):
    def __init__(self) -> None: ...
    def GetRemoteUtilities(self) -> RemoteUtilities:
        ...
    def RenameFile(self, oldFilename: str, newFilename: str) -> None:
        ...
    def CopyFile(self, originalFilename: str, newFilename: str) -> None:
        ...
    def FileExists(self, testFilename: str) -> bool:
        ...
    def DeleteFile(self, filename: str) -> None:
        ...
    def IsFileWritable(self, filename: str) -> bool:
        ...
    def SetFileWritable(self, filename: str, writable: bool) -> None:
        ...
    def CreateDirectory(self, dirname: str) -> None:
        ...
    def RemoveDirectory(self, dirname: str) -> None:
        ...


class Relay(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Signal: bool
    Active: bool


    class Relay.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class RelationFinderSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    FindChamfer: bool
    FindCollinear: bool
    FindConcentric: bool
    FindEqualRadius: bool
    FindOffset: bool
    FindOrthogonal: bool
    FindParallel: bool
    FindPerpendicular: bool
    FindSymmetric: bool
    FindTangent: bool


class RegionPointList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[RegionPoint]) -> None:
        ...
    def Append(self, object: RegionPoint) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: RegionPoint) -> int:
        ...
    def FindItem(self, index: int) -> RegionPoint:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: RegionPoint) -> None:
        ...
    def Erase(self, obj: RegionPoint, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[RegionPoint]:
        ...
    def SetContents(self, objects: typing.List[RegionPoint]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: RegionPoint, object2: RegionPoint) -> None:
        ...
    def Insert(self, location: int, object: RegionPoint) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class RegionPoint(NXObject):
    def __init__(self) -> None: ...
    Body: Body
    Point: Point


class RegionBoundaryRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seedObj: DisplayableObject, curves: typing.List[Curve], seedPoint: Point3d, distanceTolerance: float) -> None:
        ...


class ReferenceSet(DisplayableObject):
    def __init__(self) -> None: ...
    def AddObjectsToReferenceSet(self, components: typing.List[NXObject]) -> None:
        ...
    def RemoveObjectsFromReferenceSet(self, components: typing.List[NXObject]) -> None:
        ...
    def AskMembersInReferenceSet(self) -> typing.List[NXObject]:
        ...
    def AskAllDirectMembers(self) -> typing.List[NXObject]:
        ...
    def SetAddComponentsAutomatically(self, newValue: bool, addExistingComponents: bool) -> None:
        ...
    def GetAddComponentsAutomatically(self) -> bool:
        ...


class ReadWriteDeviceObject(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    DeviceType: int
    ExecuteMode: int
    Active: bool


    class ReadWriteDeviceObject.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class RackPinion(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    MasterAxis: AxisJoint
    SlaveAxis: AxisJoint
    AllowSlip: bool
    Active: bool


    class RackPinion.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PvtransManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateJtCreator(self) -> JtCreator:
        ...
    def Tag(self) -> Tag: ...



class PulleysBeltChain(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetNumPulleys(self) -> int:
        ...
    def GetMasterFlag(self, pulleyIndex: int) -> bool:
        ...
    def GetRotaryAxis(self, pulleyIndex: int) -> AxisJoint:
        ...
    def SetRotaryAxis(self, pulleyIndex: int, pValue: AxisJoint) -> None:
        ...
    def GetTransmisionRatio(self, pulleyIndex: int) -> float:
        ...
    def GetPulleyForce(self, pulleyIndex: int) -> VectorArithmetic.Vector3:
        ...
    def GetPulleyTorque(self, pulleyIndex: int) -> VectorArithmetic.Vector3:
        ...
    Active: bool


    class PulleysBeltChain.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class ProxyObject(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetNumParameters(self) -> int:
        ...
    def GetParameter(self, nProp: int) -> Parameter:
        ...
    def SetParameter(self, nProp: int, value: Parameter) -> None:
        ...


    class ProxyObject.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PropertyContainer(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetPropertyNames(self) -> str:
        ...
    def GetPropertyType(self, propertyName: str) -> PropertyContainer.PropertyType:
        ...
    def GetPropertyType(self, propertyIndex: int) -> PropertyContainer.PropertyType:
        ...
    def SetInteger(self, propertyName: str, value: int) -> None:
        ...
    def GetInteger(self, propertyName: str) -> int:
        ...
    def GetInteger(self, propertyIndex: int) -> int:
        ...
    def SetLogical(self, propertyName: str, value: bool) -> None:
        ...
    def GetLogical(self, propertyName: str) -> bool:
        ...
    def GetLogical(self, propertyIndex: int) -> bool:
        ...
    def SetDouble(self, propertyName: str, value: float) -> None:
        ...
    def GetDouble(self, propertyName: str) -> float:
        ...
    def GetDouble(self, propertyIndex: int) -> float:
        ...
    def SetString(self, propertyName: str, value: str) -> None:
        ...
    def GetString(self, propertyName: str) -> str:
        ...
    def GetString(self, propertyIndex: int) -> str:
        ...
    def SetEnumAsString(self, propertyName: str, value: str) -> None:
        ...
    def GetEnumAsString(self, propertyName: str) -> str:
        ...
    def GetEnumAsString(self, propertyIndex: int) -> str:
        ...
    def SetEnum(self, propertyName: str, value: int) -> None:
        ...
    def GetEnum(self, propertyName: str) -> int:
        ...
    def GetEnum(self, propertyIndex: int) -> int:
        ...
    def SetEnumMembers(self, propertyName: str, stringArray: str) -> None:
        ...
    def GetEnumMembers(self, propertyName: str) -> str:
        ...
    def GetEnumMembers(self, propertyIndex: int) -> str:
        ...
    def SetStrings(self, propertyName: str, stringArray: str) -> None:
        ...
    def GetStrings(self, propertyName: str) -> str:
        ...
    def GetStrings(self, propertyIndex: int) -> str:
        ...
    def SetPoint(self, propertyName: str, pointSc: Point3d) -> None:
        ...
    def GetPoint(self, propertyName: str) -> Point3d:
        ...
    def GetPoint(self, propertyIndex: int) -> Point3d:
        ...
    def SetVector(self, propertyName: str, vector: Vector3d) -> None:
        ...
    def GetVector(self, propertyName: str) -> Vector3d:
        ...
    def GetVector(self, propertyIndex: int) -> Vector3d:
        ...
    def SetBits(self, propertyName: str, bitsSc: int) -> None:
        ...
    def GetBits(self, propertyName: str) -> int:
        ...
    def GetBits(self, propertyIndex: int) -> int:
        ...
    def SetTaggedObject(self, propertyName: str, taggedSc: TaggedObject) -> None:
        ...
    def GetTaggedObject(self, propertyName: str) -> TaggedObject:
        ...
    def GetTaggedObject(self, propertyIndex: int) -> TaggedObject:
        ...
    def GetIntegerVector(self, propertyName: str) -> int:
        ...
    def SetIntegerVector(self, propertyName: str, intVector: int) -> None:
        ...
    def GetIntegerVector(self, propertyIndex: int) -> int:
        ...
    def GetDoubleVector(self, propertyName: str) -> float:
        ...
    def SetDoubleVector(self, propertyName: str, doubleVector: float) -> None:
        ...
    def GetDoubleVector(self, propertyIndex: int) -> float:
        ...
    def GetTaggedObjectVector(self, propertyName: str) -> typing.List[TaggedObject]:
        ...
    def SetTaggedObjectVector(self, propertyName: str, tagVector: typing.List[TaggedObject]) -> None:
        ...
    def GetTaggedObjectVector(self, propertyIndex: int) -> typing.List[TaggedObject]:
        ...
    def GetIntegerMatrix(self, propertyName: str, nRows: int, nColumns: int) -> int:
        ...
    def SetIntegerMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: int) -> None:
        ...
    def GetIntegerMatrix(self, propertyIndex: int, nRows: int, nColumns: int) -> int:
        ...
    def GetDoubleMatrix(self, propertyName: str, nRows: int, nColumns: int) -> float:
        ...
    def SetDoubleMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: float) -> None:
        ...
    def GetDoubleMatrix(self, propertyIndex: int, nRows: int, nColumns: int) -> float:
        ...
    def GetFile(self, propertyName: str) -> str:
        ...
    def SetFile(self, propertyName: str, value: str) -> None:
        ...
    def GetFile(self, propertyIndex: int) -> str:
        ...
    def GetArray(self, propertyName: str) -> PropertyContainer:
        ...
    def GetArray(self, propertyIndex: int) -> PropertyContainer:
        ...
    Length: int
    Mode: PropertyContainer.ListMode


    class PropertyType(enum.Enum):
        String = 0
        Double = 1
        Logical = 2
        Integer = 3
        Enum = 4
        Strings = 5
        UIBlock = 6
        Point = 7
        Vector = 8
        Bits = 9
        TaggedObject = 10
        Array = 11
        IntegerMatrix2d = 12
        DoubleMatrix2d = 13
        TaggedObjectMatrix2d = 14
        IntegerVector = 15
        DoubleVector = 16
        TaggedObjectVector = 17
        File = 18
        SelectionFilter = 19
        Undefined = 20
    

    class ListMode(enum.Enum):
        Indexed = 0
        Named = 1
    

class PropertiesManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreateAttributePropertiesBuilder(self, objects: typing.List[NXObject]) -> AttributePropertiesBuilder:
        """[Obsolete("Deprecated in NX8.5.0.  Use NXOpen.AttributeManager.CreateAttributePropertiesBuilder instead.")"""
        ...
    def CreateMassPropertiesBuilder(self, objects: typing.List[NXObject]) -> MassPropertiesBuilder:
        ...
    def CreatePreviewPropertiesBuilder(self, objects: typing.List[NXObject]) -> PreviewPropertiesBuilder:
        ...
    def CreateGeneralCAMPropertiesBuilder(self, objects: typing.List[NXObject]) -> CAM.GeneralPropertiesBuilder:
        ...
    def CreateAssembliesParameterPropertiesBuilder(self, objects: typing.List[NXObject]) -> Assemblies.AssembliesParameterPropertiesBuilder:
        ...
    def CreateFeatureGeneralPropertiesBuilder(self, objects: typing.List[NXObject]) -> FeatureGeneralPropertiesBuilder:
        ...
    def CreateObjectGeneralPropertiesBuilder(self, objects: typing.List[NXObject]) -> ObjectGeneralPropertiesBuilder:
        ...
    def CreateAssembliesGeneralPropertiesBuilder(self, objects: typing.List[NXObject]) -> Assemblies.AssembliesGeneralPropertiesBuilder:
        ...
    def CreateAttributeTemplatesBuilder(self) -> AttributeTemplatesBuilder:
        ...
    def Tag(self) -> Tag: ...

    MassCollection: Gateway.MassCollection


class ProeImporter(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.CreoImporter instead.")"""
        ...
    HealBodies: bool
    ImportTo: ProeImporter.ImportToOption
    ImportToTeamcenter: bool
    IncludeNonManifoldObj: bool
    Optimize: bool
    SettingsFile: str
    SimplifyGeometry: bool


    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

class ProductDemo(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def SetDemoLink(self, applicationName: str, demoURLLink: str) -> None:
        ...
    def GetDemoLink(self, applicationName: str) -> str:
        ...
    def Show(self, applicationName: str, additionalInformation: str) -> ProductDemo.Message:
        ...
    def Show(self, applicationName: str) -> ProductDemo.Message:
        ...
    def Tag(self) -> Tag: ...



    class Message(enum.Enum):
        Shown = 0
        NotShownInvalidUrl = 1
    

class PrintSVGBuilder(Builder):
    def __init__(self) -> None: ...
    SourceBuilder: PlotSourceBuilder


class PrintPDFBuilder(Builder):
    def __init__(self) -> None: ...
    def Assign(self) -> None:
        ...
    def DefinePalette(self) -> None:
        ...
    def DefineWidths(self) -> None:
        ...
    def CreateCdf(self) -> CDF:
        ...
    def GetCdf(self) -> CDF:
        ...
    def CreateWidthDefinition(self) -> WidthDefinition:
        ...
    def GetWidthDefinition(self) -> WidthDefinition:
        ...
    Action: PrintPDFBuilder.ActionOption
    AddWatermark: bool
    Append: bool
    Colors: PrintPDFBuilder.Color
    CustomSymbolsInForeground: bool
    DatasetName: str
    DatasetType: str
    DeleteDatasets: bool
    Filename: str
    ImageResolution: PrintPDFBuilder.ImageResolutionOption
    NamedReferenceType: str
    OutputText: PrintPDFBuilder.OutputTextOption
    RasterImages: bool
    Relation: PrintPDFBuilder.RelationOption
    Scale: float
    ShadedGeometry: bool
    Size: PrintPDFBuilder.SizeOption
    SourceBuilder: PlotSourceBuilder
    Units: PrintPDFBuilder.UnitsOption
    Watermark: str
    Widths: PrintPDFBuilder.Width
    XDimension: float
    YDimension: float


    class Width(enum.Enum):
        StandardWidths = 0
        SingleWidth = 1
        CustomThreeWidths = 2
        CustomPalette = 3
    

    class UnitsOption(enum.Enum):
        Metric = 0
        English = 1
    

    class SizeOption(enum.Enum):
        FullScale = 0
        ScaleFactor = 1
        Dimension = 2
    

    class RelationOption(enum.Enum):
        Specification = 0
        Manifestation = 1
        Undefined = 2
    

    class OutputTextOption(enum.Enum):
        Text = 0
        Polylines = 1
    

    class ImageResolutionOption(enum.Enum):
        Draft = 0
        Low = 1
        Medium = 2
        High = 3
    

    class Color(enum.Enum):
        AsDisplayed = 0
        PartColors = 1
        CustomPalette = 2
        BlackOnWhite = 3
        LegacyColors = 4
        ColorsByWidth = 5
    

    class ActionOption(enum.Enum):
        New = 0
        Overwrite = 1
        Append = 2
        Native = 3
    

class PrintBuilder(Builder):
    def __init__(self) -> None: ...
    Copies: int
    CustomPaper: int
    CustomSymbolsInForeground: bool
    ImageResolution: PrintBuilder.ImageResolutionOption
    NormalWidth: float
    Orientation: PrintBuilder.OrientationOption
    Output: PrintBuilder.OutputOption
    Paper: PrintBuilder.PaperSize
    PrinterText: str
    RasterImages: bool
    ShadedGeometry: bool
    SourceBuilder: PlotSourceBuilder
    ThickWidth: float
    ThinWidth: float
    WhiteBackground: bool
    Width1ScaleFactor: float
    Width2ScaleFactor: float
    Width3ScaleFactor: float
    Width4ScaleFactor: float
    Width5ScaleFactor: float
    Width6ScaleFactor: float
    Width7ScaleFactor: float
    Width8ScaleFactor: float
    Width9ScaleFactor: float


    class PaperSize(enum.Enum):
        Letter = 0
        Legal = 1
        Inch9x11 = 2
        Inch10x11 = 3
        Inch10x14 = 4
        Inch15x11 = 5
        Inch11x17 = 6
        Inch12x11 = 7
        A2 = 8
        A3 = 9
        A3Extra = 10
        A3ExtraTransverse = 11
        A3Rotated = 12
        A3Transverse = 13
        A4 = 14
        A4Extra = 15
        A4Plus = 16
        A4Rotated = 17
        A4Small = 18
        A4Transverse = 19
        A5 = 20
        A5Extra = 21
        A5Rotated = 22
        A5Transverse = 23
        A6 = 24
        A6Rotated = 25
        APlus = 26
        B4 = 27
        B4JisRotated = 28
        B5 = 29
        B5Extra = 30
        B5JisRotated = 31
        B6Jis = 32
        B6JisRotated = 33
        BPlus = 34
        CSheet = 35
        DoubleJapanesePostcard = 36
        DoubleJapanesePostcardRotated = 37
        DSheet = 38
        Envelope9 = 39
        Envelope10 = 40
        Envelope11 = 41
        Envelope12 = 42
        Envelope14 = 43
        EnvelopeC5 = 44
        EnvelopeC3 = 45
        EnvelopeC4 = 46
        EnvelopeC6 = 47
        EnvelopeC65 = 48
        EnvelopeB4 = 49
        EnvelopeB5 = 50
        EnvelopeB6 = 51
        EnvelopeDl = 52
        EnvelopeInvite = 53
        EnvelopeItaly = 54
        EnvelopeMonarch = 55
        EnvelopePersonal = 56
        ESheet = 57
        Executive = 58
        FanfoldUs = 59
        FanfoldStandardGerman = 60
        FanfoldLegalGerman = 61
        Folio = 62
        IsoB4 = 63
        JapanesePostcard = 64
        JapanesePostcardRotated = 65
        JapaneseEnvelopeChou3 = 66
        JapaneseEnvelopeChou3Rotated = 67
        JapaneseEnvelopeChou4 = 68
        JapaneseEnvelopeChou4Rotated = 69
        JapaneseEnvelopeKaku2 = 70
        JapaneseEnvelopeKaku2Rotated = 71
        JapaneseEnvelopeKaku3 = 72
        JapaneseEnvelopeKaku3Rotated = 73
        JapaneseEnvelopeYou4 = 74
        JapaneseEnvelopeYou4Rotated = 75
        Ledger = 76
        LegalExtra = 77
        LetterExtra = 78
        LetterExtraTransverse = 79
        LetterRotated = 80
        LetterSmall = 81
        LetterTransverse = 82
        Note = 83
        Prc16k = 84
        Prc16kRotated = 85
        Prc32k = 86
        Prc32kRotated = 87
        Prc32kBig = 88
        Prc32kBigRotated = 89
        PrcEnvelope1 = 90
        PrcEnvelope1Rotated = 91
        PrcEnvelope2 = 92
        PrcEnvelope2Rotated = 93
        PrcEnvelope3 = 94
        PrcEnvelope3Rotated = 95
        PrcEnvelope4 = 96
        PrcEnvelope4Rotated = 97
        PrcEnvelope5 = 98
        PrcEnvelope5Rotated = 99
        PrcEnvelope6 = 100
        PrcEnvelope6Rotated = 101
        PrcEnvelope7 = 102
        PrcEnvelope7Rotated = 103
        PrcEnvelope8 = 104
        PrcEnvelope8Rotated = 105
        PrcEnvelope9 = 106
        PrcEnvelope9Rotated = 107
        PrcEnvelope10 = 108
        PrcEnvelope10Rotated = 109
        Quarto = 110
        Statement = 111
        Tabloid = 112
        TabloidExtra = 113
        Custom = 114
    

    class OutputOption(enum.Enum):
        Wireframe = 0
        WireframeBlackWhite = 1
        Shaded = 2
    

    class OrientationOption(enum.Enum):
        Landscape = 0
        Portrait = 1
    

    class ImageResolutionOption(enum.Enum):
        Draft = 0
        Low = 1
        Medium = 2
        High = 3
    

class Print3dBuilder(Builder):
    def __init__(self) -> None: ...
    AddRaft: bool
    AddSupport: bool
    Bodies: SelectBodyList
    InFillPrint: Print3dBuilder.PrintInfillEnum
    LocationCoordinateSystem: CoordinateSystem
    PrinterText: str
    QualityPrint: Print3dBuilder.PrintQualityEnum


    class PrintQualityEnum(enum.Enum):
        High = 0
        Medium = 1
        Draft = 2
    

    class PrintInfillEnum(enum.Enum):
        Hollow = 0
        Low = 1
        Medium = 2
        High = 3
        Solid = 4
    

class PrimitiveFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seedFacet: IFacet, primitiveShapeToleranceFactor: float) -> None:
        ...
    def UpdateToleranceFactor(self, primitiveShapeToleranceFactor: float) -> None:
        ...


class PreviewPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    ModelViewCreation: PreviewPropertiesBuilder.ModelViewCreationOptions
    PartCreation: PreviewPropertiesBuilder.PartCreationOptions
    SelectedObjects: SelectNXObjectList
    StoreModelViewPreview: bool
    StorePartPreview: bool


    class PartCreationOptions(enum.Enum):
        OnSave = 0
        OnDemand = 1
    

    class ModelViewCreationOptions(enum.Enum):
        OnPartSave = 0
        OnViewSave = 1
        OnDemand = 2
    

class PreviewBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def DeletePreview(self) -> None:
        ...
    def Preview(self) -> None:
        ...
    def GetTrimmedExtendedEntities(self) -> typing.List[NXObject]:
        ...
    def GetTransformedEntities(self) -> typing.List[NXObject]:
        ...


class PreventCollision(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Body1: RuntimeObject
    Body2: RuntimeObject
    Active: bool


    class PreventCollision.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PositionSensor(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Signal: float
    Active: bool


    class PositionSensor.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PositioningDimension(NXObject):
    def __init__(self) -> None: ...
    def GetSubtype(self) -> PositioningDimension.Subtype:
        ...
    Expression: Expression
    Target: NXObject
    Tool: NXObject


    class Subtype(enum.Enum):
        Horizontal = 0
        Vertical = 1
        Parallel = 2
        Perpendicular = 3
        ParallelDistance = 4
        Angular = 5
        PointOntoPoint = 6
        PointOntoLine = 7
        LineOntoLine = 8
    

class PositionControl(ControlBase):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Axis: AxisJoint
    Surface: TransportSurface
    VirtualJoint: VirtualAxis
    Speed: float
    Position: float
    LimitAcceleration: bool
    Acceleration: float
    Deceleration: float
    LimitJerk: bool
    Jerk: float
    LimitForceTorque: bool
    LimitForceTorqueForward: float
    LimitForceTorqueReverse: float


    class PositionControl.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PolylineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Polyline]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Polyline:
        ...
    def CreateThroughPoints(self, updateOption: SmartObject.UpdateOption, points: typing.List[Point], isClosed: bool) -> Polyline:
        ...
    def Tag(self) -> Tag: ...



class Polyline(Spline):
    def __init__(self) -> None: ...
    def GetPoints(self) -> typing.List[Point3d]:
        ...
    Closed: bool


class PolygonModelingTaskEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Enter(self) -> None:
        ...
    def Exit(self) -> None:
        ...
    def SetCancelled(self) -> None:
        ...
    def Tag(self) -> Tag: ...



class PointOnCurveJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Point: VectorArithmetic.Vector3
    Axis: VectorArithmetic.Vector3
    Position: float
    Active: bool


    class PointOnCurveJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PointList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Point]) -> None:
        ...
    def Append(self, object: Point) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Point) -> int:
        ...
    def FindItem(self, index: int) -> Point:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Point) -> None:
        ...
    def Erase(self, obj: Point, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Point]:
        ...
    def SetContents(self, objects: typing.List[Point]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Point, object2: Point) -> None:
        ...
    def Insert(self, location: int, object: Point) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PointCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Point]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreatePoint(self, coordinates: Point3d) -> Point:
        ...
    def CreatePoint(self, offset: Offset, offsetPoint: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, face: IParameterizedSurface, scalarU: Scalar, scalarV: Scalar, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, view: View, edgeCurve1: IBaseCurve, edgeCurve2: IBaseCurve, helpPt: Point3d, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, edgeCurve: IBaseCurve, scalarT: Scalar, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, edgeCurve: IBaseCurve, scalarT: Scalar, locationOption: PointCollection.PointOnCurveLocationOption, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, edgeCurve: IBaseCurve, scalarT: Scalar, updateOption: SmartObject.UpdateOption, useReverseParameter: bool) -> Point:
        ...
    def CreatePoint(self, edgeCurve: IBaseCurve, pointOffset: Point, distancePercent: Scalar, option: PointCollection.AlongCurveOption, sense: Sense, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, scalarX: Scalar, scalarY: Scalar, scalarZ: Scalar, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, pointExtract: Point, xform: Xform, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, edgeCurve: IBaseCurve, angle: Scalar, xform: Xform, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, edgeCurve: IBaseCurve, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, curve1: IBaseCurve, curve2: IBaseCurve, helpPt1: Point, helpPt2: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, curve1: IBaseCurve, curve2: IBaseCurve, startPoint: Point3d, view: View, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, face: IParameterizedSurface, curve: IBaseCurve, helpPt1: Point, helpPt2: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, plane: IBasePlane, curve: IBaseCurve, helpPt1: Point, helpPt2: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, sphericalFace: IParameterizedSurface, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, routePosition: Routing.IRoutePosition, xform: Xform, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def FindObject(self, journalIdentifier: str) -> Point:
        ...
    def CreatePoint(self, csys: CartesianCoordinateSystem, scalarX: Scalar, scalarY: Scalar, scalarZ: Scalar, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, point1: Point, point2: Point, distancePercentage: Scalar, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreateVirtualIntersectionPoint(self, curve1: IBaseCurve, curve2: IBaseCurve, helpPt1: Point, helpPt2: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, exp: Expression, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreateStockOffsetPoint(self, basePoint: Point, offsetDirr: Direction, offsetExpression: str, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def EditStockOffsetPoint(self, basePoint: Point, offsetDirr: Direction, offsetExpression: str, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePointOnPortExtractAlign(self, updateOption: SmartObject.UpdateOption, port: Routing.Port, distance: Scalar) -> Point:
        ...
    def CreatePointOnSurfaceAxis(self, face: TaggedObject, parameter: Scalar, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, face: CAE.CAEFace, projectedPoint: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreateQuadrantPoint(self, curveOrEdge: IBaseCurve, quadrant: int, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePointOnSectionCG(self, updateOption: SmartObject.UpdateOption, face: TaggedObject) -> Point:
        ...
    def DeletePoint(self, point: Point) -> None:
        ...
    def RemoveParameters(self, point: Point) -> None:
        ...
    def CreatePoint(self, faces: ScCollector, curve: IBaseCurve, helpPt1: Point, helpPt2: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, updateOption: SmartObject.UpdateOption, annotation: Annotations.Annotation, t: Scalar, side: int, block: int, attachFcfToDim: bool) -> Point:
        ...
    def CreatePoint(self, splarc: IBaseCurve, view: View) -> Point:
        ...
    def CreatePointSplinePole(self, splineCurve: IBaseCurve, poleIndex: int, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePointSplarc(self, splarc: IBaseCurve, view: View) -> Point:
        ...
    def CreatePointSplineDefiningPoint(self, splineCurve: IBaseCurve, definingPointIndex: int, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePoint(self, edgeCurve: IBaseCurve, scalarT: Scalar, locationOption: PointCollection.PointOnCurveLocationOption, specifiedPoint: Point, updateOption: SmartObject.UpdateOption) -> Point:
        ...
    def CreatePointAtCoordinateSystemOrigin(self, updateOption: SmartObject.UpdateOption, smartCsys: CoordinateSystem) -> Point:
        ...
    def Tag(self) -> Tag: ...



    class PointOnCurveLocationOption(enum.Enum):
        Parameter = 0
        PercentParameter = 1
        ArcLength = 2
        PercentArcLength = 3
    

    class AlongCurveOption(enum.Enum):
        Distance = 0
        Percent = 1
    

class Point4d():
    X: float
    Y: float
    Z: float
    W: float
    def ToString(self) -> str:
        ...


class Point3d():
    X: float
    Y: float
    Z: float
    def ToString(self) -> str:
        ...
    def __init__(self, X: float, Y: float, Z: float) -> None: ...


class Point2d():
    X: float
    Y: float
    def ToString(self) -> str:
        ...
    def __init__(self, X: float, Y: float) -> None: ...


class Point(SmartObject):
    def __init__(self) -> None: ...
    def SetCoordinates(self, coordinates: Point3d) -> None:
        ...
    def SetPointOnCurveTParameterFixed(self, isFixed: bool) -> None:
        ...
    Coordinates: Point3d
    IsReference: bool


class PneumaticValve(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    SupplyPressure: float
    ExhaustPressure: float
    ControlIn: float
    Active: bool


    class PneumaticValve.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PneumaticCylinder(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Axis: AxisJoint
    PressureA: float
    PressureB: float
    Active: bool


    class PneumaticCylinder.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PlotSourceBuilder(NXObject):
    def __init__(self) -> None: ...
    def GetSheets(self) -> typing.List[NXObject]:
        ...
    def SetSheets(self, sheets: typing.List[NXObject]) -> None:
        ...
    SelectedSheets: int


class PlotManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def CreatePrintBuilder(self) -> PrintBuilder:
        ...
    def CreatePrintPdfbuilder(self) -> PrintPDFBuilder:
        ...
    def CreatePlotBuilder(self) -> PlotBuilder:
        ...
    def CreateCgmBuilder(self) -> CGMBuilder:
        ...
    def CreatePrint3dBuilder(self) -> Print3dBuilder:
        ...
    def CreatePrintSvgbuilder(self) -> PrintSVGBuilder:
        ...
    def Tag(self) -> Tag: ...



class PlotColorsWidthsBuilder(NXObject):
    def __init__(self) -> None: ...
    def DefinePalette(self) -> None:
        ...
    def DefineWidths(self) -> None:
        ...
    def RetrieveColors(self) -> None:
        ...
    def SaveColors(self) -> None:
        ...
    def EditColors(self) -> None:
        ...
    def DeleteColors(self) -> None:
        ...
    def ResetColors(self) -> None:
        ...
    def RetrieveWidths(self) -> None:
        ...
    def SaveWidths(self) -> None:
        ...
    def EditWidths(self) -> None:
        ...
    def DeleteWidths(self) -> None:
        ...
    def ResetWidths(self) -> None:
        ...
    def CreateCdf(self) -> CDF:
        ...
    def GetCdf(self) -> CDF:
        ...
    def CreateWidthDefinition(self) -> WidthDefinition:
        ...
    def GetWidthDefinition(self) -> WidthDefinition:
        ...
    Colors: PlotColorsWidthsBuilder.Color
    UseDrawingSheetColors: bool
    UseDrawingSheetWidths: bool
    Widths: PlotColorsWidthsBuilder.Width


    class Width(enum.Enum):
        StandardWidths = 0
        SingleWidth = 1
        CustomThreeWidths = 2
        CustomPalette = 3
    

    class Color(enum.Enum):
        AsDisplayed = 0
        PartColors = 1
        CustomPalette = 2
        BlackOnWhite = 3
        LegacyColors = 4
        ColorsByWidth = 5
    

class PlotBuilder(Builder):
    def __init__(self) -> None: ...
    def AddToPlotLayout(self) -> None:
        ...
    def ClearPlotLayout(self) -> None:
        ...
    def SaveCgm(self) -> None:
        ...
    def AdvancedPlot(self) -> None:
        ...
    def GetFilenames(self) -> str:
        ...
    def SetFilenames(self, filenames: str) -> None:
        ...
    def GetGraphicFilenames(self) -> str:
        ...
    def SetGraphicFilenames(self, filenames: str) -> None:
        ...
    BannerMessage: str
    CharacterSize: float
    ClsfData: bool
    ColorsWidthsBuilder: PlotColorsWidthsBuilder
    Copies: int
    CustomSymbolsInForeground: bool
    DisplayBanner: bool
    ImageResolution: PlotBuilder.ImageResolutionOption
    JobName: str
    Justification: PlotBuilder.JustificationOption
    PlotType: PlotBuilder.PlotTypes
    PlotterText: str
    PrinterGroupText: str
    ProfileText: str
    RasterImages: bool
    Rotation: PlotBuilder.RotationOption
    ShadedGeometry: bool
    SourceBuilder: PlotSourceBuilder
    Tolerance: float
    Units: PlotBuilder.UnitsOption
    XDisplay: PlotBuilder.XdisplayOption
    XOffset: float
    YDisplay: PlotBuilder.YdisplayOption
    YOffset: float


    class YdisplayOption(enum.Enum):
        Bottom = 0
        Center = 1
        Top = 2
    

    class XdisplayOption(enum.Enum):
        Left = 0
        Center = 1
        Right = 2
    

    class UnitsOption(enum.Enum):
        Metric = 0
        English = 1
    

    class RotationOption(enum.Enum):
        Degree0 = 0
        Degree90 = 1
        Degree180 = 2
        Degree270 = 3
    

    class PlotTypes(enum.Enum):
        Standard = 0
        UsingLayout = 1
    

    class JustificationOption(enum.Enum):
        Left = 0
        Center = 1
        Right = 2
    

    class ImageResolutionOption(enum.Enum):
        Draft = 0
        Low = 1
        Medium = 2
        High = 3
    

class PlaneTypes(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class MethodType(enum.Enum):
        Undefined = 0
        Inferred = 1
        Coincident = 2
        CoincidentFaceAxis = 3
        CoincidentPerpLinear = 4
        Parallel = 5
        ParallelPoint = 6
        Perpendicular = 7
        PerpendicularPoint = 8
        PerpendicularLinear = 9
        Center = 10
        Tangent = 11
        TangentFace = 12
        TangentPoint = 13
        TangentLinear = 14
        TangentParPlane = 15
        TangentPerpPlane = 16
        TangentTwoFaces = 17
        TangentAnglePlane = 18
        Distance = 19
        Angle = 20
        Frenet = 21
        PointDir = 22
        Point = 23
        TwoPoints = 24
        ThreePoints = 25
        Line = 26
        TwoLines = 27
        CurvePoint = 28
        FixedX = 29
        FixedY = 30
        FixedZ = 31
        FixedXyCsys = 32
        Coefficients = 33
        InferredTop = 34
        TangentInfer = 35
        PointInfer = 36
        FaceAxisPoint = 37
        Fixed = 38
        FixedView = 39
        Constructed = 40
    

    class FrenetSubtype(enum.Enum):
        NotSpecified = 0
        Tangent = 1
        Normal = 2
        Binormal = 3
        Project = 7
        ThruPoint = 9
        NormalToVector = 10
        ParallelToVector = 11
        ThruAxis = 12
        ThruPointNormalToVector = 13
        ThruPointParallelToVector = 14
        ThruPointThruAxis = 15
        ThruPointNormal = 16
        ThruPointBinormal = 17
        ThruPointProject = 18
    

    class AlternateType(enum.Enum):
        One = 0
        Two = 1
        Three = 2
        Four = 3
        Five = 4
        Six = 5
    

class PlaneNormalOrientation(enum.Enum):
    Inward = 0
    Outward = 1


class PlaneList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Plane]) -> None:
        ...
    def Append(self, object: Plane) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Plane) -> int:
        ...
    def FindItem(self, index: int) -> Plane:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Plane) -> None:
        ...
    def Erase(self, obj: Plane, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Plane]:
        ...
    def SetContents(self, objects: typing.List[Plane]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Plane, object2: Plane) -> None:
        ...
    def Insert(self, location: int, object: Plane) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class PlaneCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Plane]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreatePlane(self, origin: Point3d, normal: Vector3d, updateOption: SmartObject.UpdateOption) -> Plane:
        ...
    def CreatePlane(self, datum: Features.Feature) -> Plane:
        ...
    def CreatePlane(self, method: PlaneTypes.MethodType, alternate: PlaneTypes.AlternateType, origin: Point3d, normal: Vector3d, expression: str, flip: bool, percent: bool, geometry: typing.List[NXObject]) -> Plane:
        ...
    def CreateFixedPlane(self, origin: Point3d, matrix: Matrix3x3) -> Plane:
        ...
    def CreateFixedPlane(self, origin: Point3d, matrix: Matrix3x3, show: bool) -> Plane:
        ...
    def CreateFixedTypePlane(self, origin: Point3d, matrix: Matrix3x3, updateOption: SmartObject.UpdateOption) -> Plane:
        ...
    def Tag(self) -> Tag: ...



class Plane(SmartObject):
    def __init__(self) -> None: ...
    def CopySoPlane(self) -> Plane:
        """[Obsolete("Deprecated in NX11.0.1.  NXOpen.Plane.CopyPlane")"""
        ...
    def CopyPlane(self) -> Plane:
        ...
    def DestroyPlane(self) -> None:
        ...
    def ConvertToSmartPlane(self) -> None:
        ...
    def EditFixedPlane(self, origin: Point3d, matrix: Matrix3x3) -> None:
        ...
    def SynchronizeToPlane(self, sourcePlane: Plane) -> None:
        ...
    def SetMethod(self, type: PlaneTypes.MethodType) -> None:
        ...
    def SetExpression(self, valueExpression: str) -> None:
        ...
    def SetFlip(self, flip: bool) -> None:
        ...
    def SetPercent(self, percent: bool) -> None:
        ...
    def SetGeometry(self, geom: typing.List[NXObject]) -> None:
        ...
    def GetGeometry(self) -> typing.List[NXObject]:
        ...
    def Evaluate(self) -> None:
        ...
    def SetAlternate(self, type: PlaneTypes.AlternateType) -> None:
        ...
    def GetAlternate(self) -> PlaneTypes.AlternateType:
        ...
    def GetNumberOfAlternate(self) -> int:
        ...
    def SetReverseSection(self, reverseSection: bool) -> None:
        ...
    def GetReverseSection(self) -> bool:
        ...
    def SetFrenetSubtype(self, subtype: PlaneTypes.FrenetSubtype) -> None:
        ...
    def SetReverseSide(self, reverseSide: bool) -> None:
        ...
    def GetReverseSide(self) -> bool:
        ...
    def SetUpdateOption(self, update: SmartObject.UpdateOption) -> None:
        ...
    def SetOffsetExpression(self, valueExpression: str) -> None:
        ...
    def SetOffsetFlip(self, flip: bool) -> None:
        ...
    def RemoveOffsetData(self) -> None:
        ...
    def ReplaceExpression(self, expTag: Expression) -> None:
        ...
    def ResetExpressionValue(self) -> None:
        ...
    Expression: Expression
    Flip: bool
    FrenetSubtype: PlaneTypes.FrenetSubtype
    Matrix: Matrix3x3
    Method: PlaneTypes.MethodType
    Normal: Vector3d
    OffsetExpression: Expression
    OffsetFlip: bool
    Origin: Point3d
    Percent: bool


class PlanarJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    Axis: VectorArithmetic.Vector3
    Active: bool


    class PlanarJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PidDebugSession(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetPidDebugSession(self, owner: Session) -> PidDebugSession:
        ...
    def PrintSheetInformation(self, sheet: Diagramming.Sheet) -> None:
        ...
    def PrintPreferenceInformation(self, sheet: Diagramming.Sheet) -> None:
        ...
    def PrintTemplateInformation(self, sheet: Diagramming.Sheet) -> None:
        ...
    def PrintTCINInformation(self, sheet: Diagramming.Sheet) -> None:
        ...
    def PrintAllSheetTCINInformation(self) -> None:
        ...
    def StartDeltaObserver(self) -> None:
        ...
    def EndAndPrintDelta(self) -> None:
        ...
    def EndAndPrintAllSheetsDelta(self) -> None:
        ...
    def SetIsTagPrinted(self, isTagPrinted: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class PhysicalMaterialCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Material]:
        ...
    def __init__(self, owner: MaterialManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Material:
        ...
    def CreateListBlockBuilder(self) -> PhysMat.PhysicalMaterialListBuilder:
        ...
    def CreateMaterialAssignBuilder(self) -> PhysMat.PhysicalMaterialAssignBuilder:
        ...
    def CreatePhysicalMaterialEditBuilder(self, physicalMaterial: PhysicalMaterial) -> PhysicalMaterialBuilder:
        ...
    def CreatePhysicalMaterialInspectBuilder(self, physicalMaterial: PhysicalMaterial) -> PhysicalMaterialBuilder:
        ...
    def CreatePhysicalMaterialBuilder(self, materialType: PhysicalMaterial.Type) -> PhysicalMaterialBuilder:
        ...
    def CreateMaterialLibmgrBuilder(self) -> PhysMat.PhysicalMaterialLibMgrBuilder:
        ...
    def LoadFromNxlibrary(self, libraryReference: str) -> PhysicalMaterial:
        ...
    def LoadFromMatmlLibrary(self, libraryName: str, materialName: str) -> PhysicalMaterial:
        ...
    def LoadFromLegacynxlibrary(self, libraryReference: str) -> PhysicalMaterial:
        ...
    def LoadFromNxmatmllibrary(self, materialName: str) -> PhysicalMaterial:
        ...
    def LoadFromLibrary(self, pcLibName: str, pcMatlName: str) -> PhysicalMaterial:
        ...
    def LoadMaterialItemRevision(self, pcMatlItem: str, pcRevisionID: str) -> PhysicalMaterial:
        """[Obsolete("Deprecated in NX12.0.0.  Teamcenter material item revision is no longer supported.")"""
        ...
    def GetLoadedMaterialItemRevision(self, pcMatlItem: str, pcRevisionID: str) -> PhysicalMaterial:
        """[Obsolete("Deprecated in NX12.0.0.  Teamcenter material item revision is no longer supported.")"""
        ...
    def GetLoadedLibraryMaterial(self, pcLibName: str, pcMatlName: str) -> PhysicalMaterial:
        ...
    def CopyMaterialFromLibrary(self, libraryName: str, libraryReference: str) -> PhysicalMaterial:
        ...
    def CopyMaterialFromLibrary(self, libraryName: str, libraryReference: str, retainParentPedigree: bool) -> PhysicalMaterial:
        ...
    def CopyMaterialItemRevision(self, pcMatlItem: str, pcRevisionID: str) -> PhysicalMaterial:
        """[Obsolete("Deprecated in NX12.0.0.  Teamcenter material item revision is no longer supported.")"""
        ...
    def OutputMaterialsToLibrary(self, pcMatlNames: str, pcLibNames: str, pcExportedLibName: str) -> None:
        ...
    def ExportMaterialsToLibrary(self, pcMatlNames: str, pcLibNames: str, pcExportedLibName: str, bUpdateLibraryReference: bool) -> None:
        ...
    def ExportMaterialsToLibrary(self, pcMatlNames: str, pcLibNames: str, pcExportedLibName: str, bUpdateLibraryReference: bool) -> None:
        ...
    def UpdateMaterialsInLibrary(self, tEditedMatl: typing.List[PhysicalMaterial], pMatlNames: str, pcLibName: str) -> None:
        ...
    def DeleteMaterialsFromLibrary(self, pMatlNames: str, pcLibName: str) -> None:
        ...
    def FindBodiesWithoutMaterial(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def AnyBodiesWithoutMaterial(self) -> bool:
        ...
    def FindBodiesWithoutPreferredMaterial(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def AnyBodiesWithoutPreferredMaterial(self) -> bool:
        ...
    def AskMaterialOfObject(self, obj: TaggedObject) -> PhysicalMaterial:
        ...
    def InfoLibraryMaterial(self, pcLibAr: str, pcMatlNameAr: str) -> None:
        ...
    def InfoLibraryMaterialToFile(self, pcLibAr: str, pcMatlNameAr: str, bOverride: bool, pcFileName: str) -> None:
        ...
    def InfoItemRevision(self, pcMaterialItem: str, pcRevision: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Teamcenter material item revision is no longer supported.")"""
        ...
    def InfoItemRevisionToFile(self, pcMaterialItem: str, pcRevision: str, bOverride: bool, pcFileName: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Teamcenter material item revision is no longer supported.")"""
        ...
    def GetUsedMaterials(self) -> typing.List[PhysicalMaterial]:
        ...
    def GetMaterialsFromLibrary(self, pcLibName: str) -> str:
        ...
    def GetMaterialPropertyNeutralNames(self, materialName: str) -> str:
        """[Obsolete("Deprecated in NX1953.0.0.  Please use PhysicalMaterialCollection::GetMaterialSpecifiedPropertyNeutralNames instead.")"""
        ...
    def GetMaterialPropertyValue(self, materialName: str, propNeutralName: str) -> str:
        """[Obsolete("Deprecated in NX1953.0.0.  Please use PhysicalMaterialCollection::GetMaterialPropertyValueAndDisplayName instead.")"""
        ...
    def GetMaterialSpecifiedPropertyNeutralNames(self, pcLibName: str, materialName: str) -> str:
        ...
    def GetMaterialPropertyValueAndDisplayName(self, pcLibName: str, materialName: str, propNeutralName: str, propDisplayName: str) -> str:
        ...
    def GetDynaApplication(self) -> Fields.IApplication:
        ...
    def Tag(self) -> Tag: ...



class PhysicalMaterialBuilder(ItemCacheMappedEntityBuilder):
    def __init__(self) -> None: ...
    AddToMaterialLibraryToggle: bool
    Description: str
    Id: int
    MaterialLibrary: str
    Name: str
    PropertyTable: CAE.PropertyTable


class PhysicalMaterial(Material):
    def __init__(self) -> None: ...
    def GetMaterialType(self) -> PhysicalMaterial.Type:
        ...
    def GetId(self) -> int:
        ...
    def SetId(self, materialId: int) -> None:
        ...
    def GetCategory(self) -> str:
        ...
    def SetCategory(self, materialCategory: str) -> None:
        ...
    def SetMaterialCategory(self, materialCategory: str) -> None:
        ...
    def GetMaterialCategory(self) -> str:
        ...
    def GetSubcategory(self) -> str:
        ...
    def SetSubcategory(self, materialSubcategory: str) -> None:
        ...
    def GetAlternatename(self) -> str:
        ...
    def SetAlternatename(self, materialAlternatename: str) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, materialDescription: str) -> None:
        ...
    def IsNonlibraryMaterial(self) -> bool:
        ...
    def IsLoadedLibraryMaterial(self) -> bool:
        ...
    def IsLoadedTeamcenterMaterialItem(self) -> bool:
        ...
    def GetLibraryName(self) -> str:
        ...
    def GetTeamcenterMaterialItem(self) -> str:
        ...
    def GetVersion(self) -> str:
        ...
    def HasParentmaterial(self) -> bool:
        ...
    def GetParentmaterial(self) -> PhysicalMaterial:
        ...
    def HasParentlibrarymaterial(self) -> bool:
        ...
    def GetParentlibrarymaterial(self, parentName: str, parentLibraryName: str) -> None:
        ...
    def GetMaterialEditable(self) -> bool:
        ...
    def SetMaterialEditable(self, isEditable: bool) -> None:
        ...
    def AssignObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def AssignToAllBodies(self) -> None:
        ...
    def AssignToBodiesWithoutMaterials(self) -> PhysicalMaterial.AssignWarning:
        ...
    def AssignToBodiesNotUsingPreferredMaterial(self) -> PhysicalMaterial.AssignWarning:
        ...
    def UnassignAllObjects(self) -> None:
        ...
    def GetUsage(self, objects: typing.List[NXObject]) -> None:
        ...
    def ReplaceMaterialAssignment(self, newMatl: PhysicalMaterial) -> None:
        ...
    def Copy(self, partObject: NXObject) -> PhysicalMaterial:
        ...
    def CopyLibMatlToPart(self, partObject: NXObject) -> PhysicalMaterial:
        ...
    def CopyLibMatlToPart(self, partObject: NXObject, editable: bool) -> PhysicalMaterial:
        ...
    def Delete(self) -> None:
        ...
    def DeleteUserMaterialModels(self) -> None:
        ...
    def DeleteOrphanedUserMaterialModels(self) -> None:
        ...
    def ResyncWithLibraryDefinition(self) -> None:
        ...
    def UpdateMaterialProperties(self) -> None:
        ...
    def InfoMaterial(self) -> None:
        ...
    def InfoMaterialToFile(self, bOverride: bool, pcFileName: str) -> None:
        ...
    def GetPropTable(self) -> BasePropertyTable:
        ...
    def IsPropertyOverridden(self, propNeutralName: str) -> bool:
        ...
    def GetPropertyInheritedValue(self, propNeutralName: str) -> str:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...


    class Type(enum.Enum):
        Unknown = -1
        Isotropic = 0
        Orthotropic = 1
        Anisotropic = 2
        Fluid = 4
        GeneralHyperelastic = 5
        Mooneyrivlin = 6
        Mooneyrivlintestdata = 7
        Polynomial = 8
        Reducedpolynomial = 9
        Ogden = 10
        Ogdentestdata = 11
        Foam = 12
        Foamtestdata = 13
        Blatz = 14
        Arrudaboyce = 15
        Arrudaboycetestdata = 16
        Neohooke = 17
        Neohooketestdata = 18
        Marlow = 19
        Vanderwaals = 20
        Yeoh = 21
        Yeohtestdata = 22
        Gent = 23
        Gasket = 24
        Gasketbehavior = 25
        Shapememoryalloy = 26
        Sussmanbathe = 27
        Gasketdisplacement = 28
        Damageinterface = 29
        Multiplefluid = 30
        Hartsmith = 31
        Alexander = 32
        Curing = 33
        Porous = 35
        Compoundisotropic = 36
        Lowdensityfoam = 37
        Fabric = 38
        Crushablefoam = 39
        Ratesensitivefoam = 40
        Multimechmicrostructure = 41
        Honeycomb = 42
        Composite = 43
    

    class Category(enum.Enum):
        Metals = 0
        Plastics = 1
        Polymers = 2
        Ceramics = 3
        Other = 4
    

    class AssignWarning(enum.Enum):
        None = 0
        InvalidObj = 1
    

class Persistence(enum.Enum):
    Temporary = 0
    Permanent = 1


class PathConstraintJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Point: VectorArithmetic.Vector3
    Position: float
    Parameter: float
    Active: bool


    class PathConstraintJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class PasteSpecialBuilder(Builder):
    def __init__(self) -> None: ...
    Csys: CoordinateSystem
    DestinationOpt: PasteSpecialBuilder.DestinationOption
    LayerNumber: int
    LayerOpt: PasteSpecialBuilder.LayerOption


    class LayerOption(enum.Enum):
        Work = 0
        Original = 1
        Specified = 2
    

    class DestinationOption(enum.Enum):
        Wcs = 0
        Csys = 1
    

class PartSaveStatus(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetPart(self, i: int) -> BasePart:
        ...
    def GetStatus(self, i: int) -> int:
        ...
    def GetObjectStatus(self, i: int) -> int:
        ...
    NumberUnsavedObjects: int
    NumberUnsavedParts: int


class PartSaveOptions(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def Tag(self) -> Tag: ...

    Annotation3dData: bool
    CompressPart: bool
    DrawingCgmData: bool
    GenerateWeightData: bool
    PatternDataToSave: PartSaveOptions.PatternData


    class PatternData(enum.Enum):
        SaveNoShadedOrPattern = 0
        SavePatternOnly = 1
        SavePatternAndShaded = 2
    

class PartReopenStatus(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AfterName: str
    BeforeName: str
    CouldNotClose: bool
    LoadStatus: int
    LoadStatusDescription: str
    ModifiedInSession: bool
    ModifiedOnDisk: bool


class PartReopenReport(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetStatuses(self) -> typing.List[PartReopenStatus]:
        ...
    CouldNotResetWorkPart: bool
    NumberReopenParts: int
    WasDisplayPartReopened: bool


class PartLoadStatus(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetPartName(self, i: int) -> str:
        ...
    def GetStatus(self, i: int) -> int:
        ...
    def GetStatusDescription(self, i: int) -> str:
        ...
    NumberUnloadedParts: int


class PartLoadState(enum.Enum):
    NotLoaded = 0
    FullyLoaded = 1
    PartiallyLoaded = 2
    MinimallyLoaded = 3


class PartImporter(Importer):
    def __init__(self) -> None: ...
    def SetSpecifiedCoordinateSystem(self, specifiedCoordinateSystem: CoordinateSystem) -> None:
        ...
    def SetSpecifiedCoordinateSystem(self, specifiedCoordinateSystem: CoordinateSystem, deleteSpecifiedCoordinateSystem: bool) -> None:
        ...
    CreateNamedGroup: bool
    DestinationCoordinateSystem: NXMatrix
    DestinationCoordinateSystemSpecification: PartImporter.DestinationCoordinateSystemSpecificationType
    DestinationPoint: Point3d
    ImportCamObjects: bool
    ImportViews: bool
    LayerOption: PartImporter.LayerOptionType
    Scale: float


    class LayerOptionType(enum.Enum):
        Work = 0
        Original = 1
    

    class DestinationCoordinateSystemSpecificationType(enum.Enum):
        Work = 0
        Specified = 1
    

class PartFamilyMemberValues(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  PartFamilyMemberValues object is deprecated, so dispose of this object is not needed")"""
        ...
    def SetMemberValues(self, memberValues: str) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.InstanceDefinition.SetValueOfAttribute and NXOpen.PartFamily.TemplateManager.GetPartFamilyAttribute instead.")"""
        ...


class PartFamilyMemberData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  PartFamilyMemberData object is deprecated, so dispose of this object is not needed")"""
        ...
    def SetMemberData(self, memberData: typing.List[PartFamilyMemberValues]) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.TemplateManager.AddInstanceDefinition and NXOpen.PartFamily.InstanceDefinition.SetValueOfAttribute instead")"""
        ...


class PartFamilyManager(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  PartFamilyManager object is deprecated, so dispose of this object is not needed")"""
        ...
    def GetMemberCount(self) -> int:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.Template.GetMembers instead")"""
        ...
    def CreateMember(self, memberIndex: int) -> Part:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.TemplateManager.SaveFamilyAndCreateMembers instead")"""
        ...
    def AddMember(self, memberData: PartFamilyMemberValues) -> int:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.TemplateManager.AddInstanceDefinition instead")"""
        ...
    def EditMember(self, memberIndex: int, newMemberData: PartFamilyMemberValues) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.TemplateManager.GetInstanceDefinition and NXOpen.PartFamily.InstanceDefinition.SetValueOfAttribute instead")"""
        ...
    def DeleteMember(self, memberIndex: int) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.TemplateManager.DeleteInstanceDefinition instead")"""
        ...
    def AskIndexOfMemberName(self, memberName: str) -> int:
        """[Obsolete("Deprecated in NX9.0.0.  Use query methods on the NXOpen.PartFamily.TemplateManager instead")"""
        ...
    def PrintFamilyTable(self) -> None:
        """[Obsolete("Deprecated in NX9.0.0.  Use methods on the NXOpen.PartFamily.TemplateManager to query and print part family information")"""
        ...
    def EstablishMember(self, memberIndex: int) -> str:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.TemplateManager.EstablishFamilyInstance")"""
        ...


class PartDisplayPartWorkPartOption(enum.Enum):
    SameAsDisplay = 0
    UseLast = 1


class PartDelayedUpdateStatus(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetPartName(self, i: int) -> str:
        ...
    def GetDelayedStatus(self, i: int) -> PartDelayedUpdateStatus.DelayStatusInfo:
        ...
    NumberDelayedParts: int


    class PartDelayedUpdateStatusDelayStatusInfo():
        SessionDelayed: bool
        ExplicitDelayed: bool
        FrozenDelayed: bool
        NotDisplayedDelayed: bool
        DeferredDelayed: bool
        InternalDelayed: bool
        ConstraintDelayed: bool
        def ToString(self) -> str:
            ...
    

class PartCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[BasePart]:
        ...
    def __init__(self, owner: Session) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, name: str) -> BasePart:
        ...
    def GetConfiguredParts(self, part: BasePart) -> typing.List[ConfiguredPart]:
        ...
    def GetPrimaryConfiguredPart(self, part: BasePart) -> ConfiguredPart:
        ...
    def NewDisplay(self, name: str, units: Part.Units) -> Part:
        ...
    def NewBaseDisplay(self, name: str, units: BasePart.Units) -> BasePart:
        ...
    def NewBase(self, name: str, units: BasePart.Units) -> BasePart:
        ...
    def Open(self, filename: str, loadStatus: PartLoadStatus) -> Part:
        ...
    def OpenBase(self, filename: str, loadStatus: PartLoadStatus) -> BasePart:
        ...
    def OpenDisplay(self, filename: str, loadStatus: PartLoadStatus) -> Part:
        ...
    def OpenActiveDisplay(self, filename: str, displayPartOption: DisplayPartOption, loadStatus: PartLoadStatus) -> BasePart:
        ...
    def OpenBaseDisplay(self, filename: str, loadStatus: PartLoadStatus) -> BasePart:
        ...
    def SaveAll(self, anyPartsModified: bool, saveStatus: PartSaveStatus) -> None:
        ...
    def CloseAll(self, closeModified: BasePart.CloseModified, responses: PartCloseResponses) -> None:
        ...
    def ReopenAll(self, closeModified: BasePart.CloseModified, responses: PartCloseResponses) -> PartReopenReport:
        ...
    def GetDisplayedParts(self) -> typing.List[BasePart]:
        ...
    def SetWork(self, part: BasePart) -> None:
        ...
    def SetWorkComponent(self, workComponent: Assemblies.Component, loadStatus: PartLoadStatus) -> None:
        ...
    def SetWorkComponent(self, workComponent: Assemblies.Component, refsetOption: PartCollection.RefsetOption, visibility: PartCollection.WorkComponentOption, loadStatus: PartLoadStatus) -> None:
        ...
    def SetWorkComponentOverride(self, workComponent: Assemblies.Component) -> PartLoadStatus:
        ...
    def SetDisplay(self, part: BasePart, maintainWorkPart: bool, setEntirePart: bool, loadStatus: PartLoadStatus) -> PartCollection.SdpsStatus:
        ...
    def SetActiveDisplay(self, part: BasePart, displayPartOption: DisplayPartOption, workPartOption: PartDisplayPartWorkPartOption, loadStatus: PartLoadStatus) -> PartCollection.SdpsStatus:
        ...
    def SetActiveDisplayRetainUndoMarks(self, part: BasePart, displayPartOption: DisplayPartOption, workPartOption: PartDisplayPartWorkPartOption, loadStatus: PartLoadStatus) -> PartCollection.SdpsStatus:
        ...
    def NewPartCloseResponses(self) -> PartCloseResponses:
        ...
    def FileNew(self) -> FileNew:
        ...
    def AddPartCreatedHandler(self, handler: PartCollection.PartCreatedHandler) -> int:
        ...
    def RemovePartCreatedHandler(self, id: int) -> None:
        ...
    def AddPartOpenedHandler(self, handler: PartCollection.PartOpenedHandler) -> int:
        ...
    def RemovePartOpenedHandler(self, id: int) -> None:
        ...
    def AddPartSavedHandler(self, handler: PartCollection.PartSavedHandler) -> int:
        ...
    def RemovePartSavedHandler(self, id: int) -> None:
        ...
    def AddPartSavedAsHandler(self, handler: PartCollection.PartSavedAsHandler) -> int:
        ...
    def RemovePartSavedAsHandler(self, id: int) -> None:
        ...
    def AddPartClosedHandler(self, handler: PartCollection.PartClosedHandler) -> int:
        ...
    def RemovePartClosedHandler(self, id: int) -> None:
        ...
    def AddPartModifiedHandler(self, handler: PartCollection.PartModifiedHandler) -> int:
        ...
    def RemovePartModifiedHandler(self, id: int) -> None:
        ...
    def AddPartRenamedHandler(self, handler: PartCollection.PartRenamedHandler) -> int:
        ...
    def RemovePartRenamedHandler(self, id: int) -> None:
        ...
    def AddWorkPartChangedHandler(self, handler: PartCollection.WorkPartChangedHandler) -> int:
        ...
    def RemoveWorkPartChangedHandler(self, id: int) -> None:
        ...
    def ForceSaveAll(self) -> PartSaveStatus:
        ...
    def SetSeedPartTemplateData(self, filename: str, templateName: str, addMaster: bool) -> None:
        ...
    def OpenSeedPartBlankTemplate(self, filename: str, addMaster: bool) -> None:
        ...
    def SetNonmasterSeedPartData(self, filename: str) -> None:
        ...
    def CreateLinkedMirrorPartBuilder(self, part: Part) -> LinkedMirrorPartBuilder:
        ...
    def IsMirroredPart(self, part: Part) -> bool:
        ...
    def IsExactMirroredPart(self, part: Part) -> bool:
        ...
    def SetMirrorPartType(self, part: Part, mirrorOption: LinkedMirrorPartBuilder.MirrorPartTypeOption) -> None:
        ...
    def GetMirrorPartType(self, part: Part) -> LinkedMirrorPartBuilder.MirrorPartTypeOption:
        ...
    def GetSourcePartNameOfMirrorPart(self, mirrorPart: Part) -> str:
        ...
    def SetPassword(self, part: Part, uAdminPassword: str, uReadPassword: str, uWritePassword: str, uFullControlPassword: str) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded SetPassword instead.")"""
        ...
    def RemovePassword(self, part: Part) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use overloaded RemovePassword instead.")"""
        ...
    def SetOpenPassword(self, fileName: str, password: str) -> None:
        ...
    def ImportToolDesignPackage(self, filename: str, outputDirectory: str, loadStatus: PartLoadStatus, saveStatus: PartSaveStatus) -> Part:
        ...
    def GetMirrorCsysOptionOfMirrorPart(self, part: Part) -> LinkedMirrorPartBuilder.MirrorCsysOption:
        ...
    def GetMirrorPlaneDataOfMirrorPart(self, part: Part, mirrorPlaneOrigin: Point3d, mirrorPlaneDirection: Vector3d) -> None:
        ...
    def SolveAllPostponedConstraints(self) -> None:
        ...
    def RefreshPartNavigator(self) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  A direct call to refresh the part navigator should not be needed.")"""
        ...
    def CreateGenericFileNewBuilder(self) -> Gateway.GenericFileNewBuilder:
        ...
    def OpenPasswordSafe(self, fileName: str, password: str) -> None:
        ...
    def ClosePasswordSafe(self) -> None:
        ...
    def SetPassword(self, part: Part, adminPassword: str, readPassword: str, writePassword: str, fullControlPassword: str, partoption: PartCollection.SetProtectionOn) -> None:
        ...
    def RemovePassword(self, part: Part, partoption: PartCollection.SetProtectionOn) -> None:
        ...
    def SetAllowMultipleDisplayedParts(self, additionalPartsDisplayed: bool) -> None:
        ...
    def EnsurePartsLoadedPartially(self, parts: typing.List[BasePart], includeChildren: bool) -> PartLoadStatus:
        ...
    def EnsurePartsLoadedFully(self, parts: typing.List[BasePart], includeChildren: bool) -> PartLoadStatus:
        ...
    def GetPartLoadStateOfFileName(self, fileName: str) -> PartLoadState:
        ...
    def CreateCloudDMNewPartBuilder(self) -> CloudDM.NewPartBuilder:
        ...
    def Tag(self) -> Tag: ...

    LoadOptions: LoadOptions
    SaveOptions: SaveOptions
    PDMPartManager: PDM.PartManager
    ShapeSearchManager: ShapeSearch.SearchManager
    AllowMultipleDisplayedParts: PartCollection.MultipleDisplayedPartStatus
    BaseDisplay: BasePart
    BaseWork: BasePart
    Display: Part
    Work: Part
    WorkComponent: Assemblies.Component


    

    class WorkComponentOption(enum.Enum):
        Visible = 0
        Given = 1
    

    class SetProtectionOn(enum.Enum):
        DisplayedPart = 0
        DisplayedPartandComponents = 1
        AllParts = 2
    

    class SdpsStatus(enum.Enum):
        Ok = 0
        OutsideModelling = 1
        DrawingDisplayed = 2
        InPartsList = 3
        Gdt = 4
        UnitsMismatch = 5
    

    class RefsetOption(enum.Enum):
        Entire = 0
        Current = 1
        PreserveRefset = 2
    

    

    

    

    

    

    

    

    class MultipleDisplayedPartStatus(enum.Enum):
        Enabled = 0
        DisabledByCustomer = 1
        Disabled = 2
    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

class PartCloseStatus(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetPart(self, i: int) -> BasePart:
        ...
    def GetStatus(self, i: int) -> int:
        ...
    NumberUnclosedParts: int


class PartCloseResponses(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddResponse(self, partName: str, response: bool) -> None:
        ...


class PartCleanup(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def DoCleanup(self) -> None:
        ...
    def Reset(self) -> None:
        ...
    CleanupAssemblyConstraints: bool
    CleanupCAMObjects: bool
    CleanupDraftingObjects: bool
    CleanupFeatureData: bool
    CleanupMatingData: bool
    CleanupMotionData: bool
    CleanupPartFamilyData: bool
    CleanupRoutingData: bool
    DeleteBrokenInterpartLinks: bool
    DeleteDuplicateLights: bool
    DeleteInvalidAttributes: bool
    DeleteMaterials: bool
    DeleteSpreadSheetData: bool
    DeleteUnusedExpressions: bool
    DeleteUnusedExtractReferences: bool
    DeleteUnusedFonts: bool
    DeleteUnusedObjects: bool
    DeleteUnusedUnits: bool
    DeleteVisualEditorData: bool
    FixOffplaneSketchCurves: bool
    GroupsToDelete: PartCleanup.DeleteGroups
    PartsToCleanup: PartCleanup.CleanupParts
    ResetComponentDisplay: PartCleanup.ResetComponentDisplayAction
    TurnOffHighlighting: bool


    class ResetComponentDisplayAction(enum.Enum):
        No = 0
        RemoveRedundantChanges = 1
        RemoveAllChanges = 2
    

    class DeleteGroups(enum.Enum):
        None = 0
        Unnamed = 1
        All = 2
    

    class CleanupParts(enum.Enum):
        Work = 0
        Components = 1
        All = 2
    

class Part(BasePart):
    def __init__(self) -> None: ...
    def GetInterpartChildren(self) -> typing.List[Part]:
        ...
    def GetInterpartParents(self) -> typing.List[Part]:
        ...
    def GetUpdateStatusReport(self, numFailed: int) -> typing.List[Part.FeatureUpdateStatus]:
        ...
    def ResetTimestampToLatestFeature(self) -> None:
        ...
    def DeleteRetainedDraftingObjectsInCurrentLayout(self) -> None:
        ...
    def CreateObjectList(self) -> ObjectList:
        ...
    def CreateExpressionSectionSet(self, section: Section, value: str, unitsType: str, index: int) -> ExpressionSectionSet:
        ...
    def CreateTwoExpressionsSectionSet(self, section: Section, value: str, valueTwo: str, unitsType: str, index: int) -> GeometricUtilities.TwoExpressionsSectionSet:
        ...
    def CreateEmptyExpressionSectionSet(self) -> ExpressionSectionSet:
        ...
    def CreateEmptyTwoExpressionsSectionSet(self) -> GeometricUtilities.TwoExpressionsSectionSet:
        ...
    def CreateExpressionCollectorSet(self, collector: ScCollector, value: str, unitsType: str, index: int) -> ExpressionCollectorSet:
        ...
    def CreateTwoExpressionsCollectorSet(self, collector: ScCollector, value: str, valueTwo: str, unitsType: str, index: int) -> GeometricUtilities.TwoExpressionsCollectorSet:
        ...
    def CreateEmptyExpressionCollectorSet(self) -> ExpressionCollectorSet:
        ...
    def CreateEmptyTwoExpressionsCollectorSet(self) -> GeometricUtilities.TwoExpressionsCollectorSet:
        ...
    def CreateCamSetup(self, templateName: str) -> CAM.CAMSetup:
        ...
    def DeleteCamSetup(self) -> None:
        ...
    def CreateInspectionSetup(self, templateName: str) -> CAM.InspectionSetup:
        ...
    def DeleteInspectionSetup(self) -> None:
        ...
    def CreateRegionPoint(self, point: Point, body: Body) -> RegionPoint:
        ...
    def CreateEmptyRegionPoint(self) -> RegionPoint:
        ...
    def CreatePartFamily(self, attributeData: typing.List[Part.PartFamilyAttributeData], memberData: PartFamilyMemberData) -> PartFamilyManager:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.TemplateManager.CreatePartFamily instead")"""
        ...
    def GetPartFamilyManager(self) -> PartFamilyManager:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.Part.NewPartFamilyTemplateManager instead")"""
        ...
    def NewPartFamilyMemberData(self) -> PartFamilyMemberData:
        """[Obsolete("Deprecated in NX9.0.0.  Create and use NXOpen.PartFamily.InstanceDefinition objects using NXOpen.PartFamily.TemplateManager.AddInstanceDefinition")"""
        ...
    def NewPartFamilyMemberValues(self) -> PartFamilyMemberValues:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.PartFamily.InstanceDefinition and NXOpen.PartFamily.InstanceDefinition.SetValueOfAttribute")"""
        ...
    def CreateWavelinkRepository(self) -> GeometricUtilities.WaveLinkRepository:
        ...
    def CreateEmptyBoundaryDefinitionBuilder(self) -> GeometricUtilities.BoundaryDefinitionBuilder:
        ...
    def CreatePointSetAlignmentBuilder(self) -> GeometricUtilities.PointSetAlignmentBuilder:
        ...
    def CreateKinematicConfigurator(self) -> SIM.KinematicConfigurator:
        ...
    def CreateBoundingObjectBuilder(self) -> GeometricUtilities.BoundingObjectBuilder:
        ...
    def MakeAllFeaturesInactive(self) -> None:
        ...
    def MakeNoPartModuleActive(self) -> None:
        ...
    def CreateSelectionList(self) -> GeometricUtilities.SelectionList:
        ...
    def CreateEmptySelectionList(self) -> GeometricUtilities.SelectionList:
        ...
    def CreatePointsFromFileBuilder(self) -> GeometricUtilities.PointsFromFileBuilder:
        ...
    def ConvertPreNX9CompoundWelds(self) -> None:
        ...
    def RemoveMissingParentsFromEdgeBlend(self, removedEdgeCounts: int) -> typing.List[Features.EdgeBlend]:
        ...
    def NewPartFamilyTemplateManager(self) -> PartFamily.TemplateManager:
        ...
    def GetFamilyInstance(self) -> PartFamily.Instance:
        ...
    def CreateEmptyBlendSetbackBuilder(self) -> GeometricUtilities.BlendSetbackBuilder:
        ...
    def CreateEmptyTransitionCurveBuilder(self) -> GeometricUtilities.TransitionCurveBuilder:
        ...
    def CreateEmptySpinePlaneBuilder(self) -> GeometricUtilities.SpinePlaneBuilder:
        ...
    def LoadWaveLinkFeatureParents(self) -> PartLoadStatus:
        ...
    Bodies: BodyCollection
    CutViews: CutViewCollection
    Dimensions: Annotations.DimensionCollection
    DraftingViews: Drawings.DraftingViewCollection
    DrawingSheets: Drawings.DrawingSheetCollection
    DraftingDrawingSheets: Drawings.DraftingDrawingSheetCollection
    Notes: Annotations.NoteCollection
    Labels: Annotations.LabelCollection
    Gdts: Annotations.GdtCollection
    Markers: Motion.MarkerCollection
    RouteManager: Routing.RouteManager
    SegmentManager: Routing.SegmentManager
    MechanicalRoutingCollectionsManager: MechanicalRouting.CollectionsManager
    Sketches: SketchCollection
    Tracelines: TracelineCollection
    FaceSetOffsets: GeometricUtilities.FaceSetOffsetCollection
    PackagingCollection: Motion.PackagingCollection
    MotionManager: Motion.MotionManager
    PhysicsManager: Mechatronics.PhysicsManager
    PenetrationManager: Features.ShipDesign.PenetrationManager
    DraftPointData: DraftPointDataCollection
    Relinkers: Assemblies.RelinkerCollection
    OnestepUnforms: BodyDes.OnestepUnformCollection
    ReusableParts: Tooling.AddReusablePartCollection
    ToolingManager: Tooling.ToolingManager
    SketchEvaluators: SketchEvaluatorCollection
    Drafting: DraftingManager
    DraftingManager: Drafting.DraftingApplicationManager
    ComponentGroups: Assemblies.ComponentGroupCollection
    ImportManager: ImportManager
    FacetedBodies: Facet.FacetedBodyCollection
    ProductInterface: Assemblies.ProductInterface.Collection
    ClipboardOperationsManager: ClipboardOperationsManager
    ViewPreferences: Preferences.ViewPreferences
    SpinePointData: GeometricUtilities.SpinePointDataCollection
    PmiManager: Annotations.PmiManager
    BlendStopshortBuilder: GeometricUtilities.BlendStopshortBuilderCollection
    CAMDataPrepManager: GeometricUtilities.CAMDataPrepManager
    FaceSetData: GeometricUtilities.FaceSetDataCollection
    GeometryLocationData: GeometricUtilities.GeometryLocationDataCollection
    DieSimData: Die.DieSimCollection
    FacePlaneSelectionBuilderData: GeometricUtilities.FacePlaneSelectionBuilderCollection
    DrawingCompare: DrawingCompareManager
    MechatronicsManager: Mechatronics.MechatronicsManager
    GanttCollection: Mechatronics.GanttCollection
    GanttLinkerCollection: Mechatronics.GanttLinkerCollection
    ProxyObjectCollection: Mechatronics.ProxyObjectCollection
    ProxyOverrideObjectCollection: Mechatronics.ProxyOverrideObjectCollection
    SettingsManager: Drafting.SettingsManager
    PmiSettingsManager: Annotations.PmiSettingsManager
    DisplayedConstraints: Positioning.DisplayedConstraintCollection
    ViewAlignments: Drawings.ViewAlignmentCollection
    CAMDataManager: Tooling.CAMDataManager
    SubdivisionBodies: Features.Subdivision.SubdivisionBodyCollection
    Component2dCollection: Layout2d.ComponentCollection
    ComponentDefinitions: Layout2d.ComponentDefinitionCollection
    LocalDefinitionFolders: Layout2d.LocalDefinitionFolderCollection
    LayoutDrawingSheets: Layout2d.LayoutDrawingSheetCollection
    ShipDimensions: Annotations.ShipDimensionCollection
    DiagrammingManager: Diagramming.DiagrammingManager
    SmartDiagrammingManager: Diagramming.SmartDiagrammingManager
    AppearanceManager: Appearance.AppearanceManager
    PlasManager: PLAS.PlasManager
    UserDefinedTemplates: UserDefinedTemplate.Collection
    ConfigurationManager: UserDefinedTemplate.ConfigurationManager
    DBEntityProxies: PDM.DBEntityProxyCollection
    FacetSelectionRuleFactory: FacetSelectionRuleFactory
    FacetCollectorCollection: FacetCollectorCollection
    UVMappingCollection: GeometricUtilities.UVMapping.UVMappingCollection
    IdealizedBeamManager: CADCAEPrep.IdealizedBeamManager
    SchematicManager: Schematic.SchematicManager
    RunCollection: Schematic.Mechanical.RunCollection
    LocalUntrimManager: GeometricUtilities.LocalUntrimManager
    OmnicadManager: GeometricUtilities.OmnicadManager
    CAMSetup: CAM.CAMSetup
    CurrentFeature: Features.Feature
    HasReuseTemplate: bool
    InspectionSetup: CAM.InspectionSetup
    IsBookletPart: bool
    KinematicConfigurator: SIM.KinematicConfigurator


    class Units(enum.Enum):
        Inches = 0
        Millimeters = 1
        Mix = 2
    

    class Relations(enum.Enum):
        Standalone = 0
        ReferenceExisting = 1
        Mix = 2
    

    class PartFamilyAttrType(enum.Enum):
        TextType = 1
        NumericType = 2
        IntegerType = 3
        DoubleType = 4
        StringType = 5
        PartType = 6
        NameType = 7
        InstanceType = 8
        ExpressionType = 9
        MirrorType = 10
        DensityType = 11
        FeatureType = 12
    

    class PartPartFamilyAttributeData():
        AttributeType: Part.PartFamilyAttrType
        AttributeName: str
        def ToString(self) -> str:
            ...
        def __init__(self, AttributeType: Part.PartFamilyAttrType, AttributeName: str) -> None: ...
    

    class PartFeatureUpdateStatus():
        Feature: Features.Feature
        Status: str
        ErrorMessage: str
        def ToString(self) -> str:
            ...
        def __init__(self, Feature: Features.Feature, Status: str, ErrorMessage: str) -> None: ...
    

    class Part_PartFamilyAttributeData():
        attribute_type: Part.PartFamilyAttrType
        attribute_name: int
    

    class Part_FeatureUpdateStatus():
        feature: Tag
        status: int
        error_message: int
    

class ParasolidImporter(BaseImporter):
    def __init__(self) -> None: ...
    FlattenAssembly: bool
    ObjectTypes: ObjectTypeSelector
    TargetLayer: int
    UseActiveLayer: bool


class ParasolidExporter(BaseCreator):
    def __init__(self) -> None: ...
    ExportFrom: ParasolidExporter.ExportFromOption
    ExportSelectionBlock: ObjectSelector
    FlattenAssembly: bool
    HeaderInformation: bool
    InputFile: str
    ObjectTypes: ObjectTypeSelector
    ParasolidVersion: ParasolidExporter.ParasolidVersionOption


    class ParasolidVersionOption(enum.Enum):
        Current = 0
        Ps340Nx2007 = 340
        Ps331Nx1980 = 331
        Ps330Nx1953 = 330
        Ps320Nx1899 = 320
        Ps310Nx1847 = 310
        Ps300Nx120 = 300
        Ps280Nx110 = 280
        Ps270Nx100 = 270
        Ps260Nx90 = 260
        Ps250Nx85 = 250
        Ps240Nx80 = 240
        Ps221Nx75 = 221
        Ps220Nx70 = 220
        Ps190Nx60 = 190
        Ps180Nx50 = 180
        Ps170Nx40 = 170
        Ps160Nx30 = 160
        Ps150Nx20 = 150
        Ps140Nx10 = 140
        Ps130Ug180 = 130
        Ps120Ug170 = 120
        Ps110Ug160 = 110
        Ps100Ug150 = 100
        Ps91Ug140 = 91
        Ps90Ug130 = 90
        Ps80Ug120 = 80
        Ps71Ug111 = 71
        Ps70Ug110 = 70
    

    class ExportFromOption(enum.Enum):
        DisplayedPart = 0
        ExistingPart = 1
    

class ParamLibParameterListBuilder(Builder):
    def __init__(self) -> None: ...


class ParamLibParameterLibraryManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def Tag(self) -> Tag: ...

    Parameters: ParamLibParameterCollection


class ParamLibParameterCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[ParamLibParameter]:
        ...
    def __init__(self, owner: ParamLibParameterLibraryManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> ParamLibParameter:
        ...
    def CreateListBlockBuilder(self) -> ParamLibParameterListBuilder:
        ...
    def CreateListBlockBuilder1(self, pcLibTypeNeuNames: str) -> ParamLibParameterListBuilder:
        ...
    def CreateParameterEditBuilder(self, parameterTag: ParamLibParameter) -> ParamLibParameterBuilder:
        ...
    def CreateParameterInspectBuilder(self, parameterTag: ParamLibParameter) -> ParamLibParameterBuilder:
        ...
    def CreateParameterBuilder(self, libTypeNeutralName: str, parameterType: int) -> ParamLibParameterBuilder:
        ...
    def CreateParameterLibmgrBuilder(self, pcLibTypeNeuNames: str) -> ParamLibLibraryManagerBuilder:
        ...
    def LoadFromParamplLibrary(self, libraryName: str, parameterName: str) -> ParamLibParameter:
        ...
    def LoadFromNxparampllibrary(self, parameterName: str) -> ParamLibParameter:
        ...
    def GetLoadedLibraryParameter(self, pcLibName: str, pcParamName: str) -> ParamLibParameter:
        ...
    def CopyParameterFromLibrary(self, libraryName: str, libraryReference: str) -> ParamLibParameter:
        ...
    def CopyParameterFromLibrary(self, libraryName: str, libraryReference: str, retainParentPedigree: bool) -> ParamLibParameter:
        ...
    def OutputParametersToLibrary(self, pcParamNames: str, pcLibNames: str, pcExportedLibName: str) -> None:
        ...
    def ExportParametersToLibrary(self, pcParamNames: str, pcLibNames: str, pcExportedLibName: str, bUpdateLibraryReference: bool) -> None:
        ...
    def ExportParametersToLibrary(self, pcParamNames: str, pcLibNames: str, pcExportedLibName: str, bUpdateLibraryReference: bool) -> None:
        ...
    def UpdateParametersInLibrary(self, tEditedParam: typing.List[ParamLibParameter], pParamNames: str, pcLibName: str) -> None:
        ...
    def DeleteParametersFromLibrary(self, pParamNames: str, pcLibName: str) -> None:
        ...
    def InfoLibraryParameter(self, pcLibAr: str, pcParamNameAr: str) -> None:
        ...
    def InfoLibraryParameterToFile(self, pcLibAr: str, pcParamNameAr: str, bOverride: bool, pcFileName: str) -> None:
        ...
    def GetUsedParameters(self) -> typing.List[ParamLibParameter]:
        ...
    def Tag(self) -> Tag: ...



class ParamLibParameterBuilder(ItemCacheMappedEntityBuilder):
    def __init__(self) -> None: ...
    Description: str
    Id: int
    Name: str
    PropertyTable: CAE.PropertyTable


class ParamLibParameter(NXObject):
    def __init__(self) -> None: ...
    def GetLibraryType(self) -> str:
        ...
    def GetParameterType(self) -> int:
        ...
    def GetId(self) -> int:
        ...
    def SetId(self, parameterId: int) -> None:
        ...
    def GetCategory(self) -> str:
        ...
    def SetCategory(self, parameterCategory: str) -> None:
        ...
    def SetParameterCategory(self, parameterCategory: str) -> None:
        ...
    def GetParameterCategory(self) -> str:
        ...
    def GetSubcategory(self) -> str:
        ...
    def SetSubcategory(self, parameterSubcategory: str) -> None:
        ...
    def GetAlternatename(self) -> str:
        ...
    def SetAlternatename(self, parameterAlternatename: str) -> None:
        ...
    def GetDescription(self) -> str:
        ...
    def SetDescription(self, parameterDescription: str) -> None:
        ...
    def IsNonlibraryParameter(self) -> bool:
        ...
    def IsLoadedLibraryParameter(self) -> bool:
        ...
    def IsLoadedTeamcenterParameterItem(self) -> bool:
        ...
    def GetLibraryName(self) -> str:
        ...
    def GetTeamcenterParameterItem(self) -> str:
        ...
    def GetVersion(self) -> str:
        ...
    def HasParentparameter(self) -> bool:
        ...
    def GetParentparameter(self) -> ParamLibParameter:
        ...
    def HasParentlibraryparameter(self) -> bool:
        ...
    def GetParentlibraryparameter(self, parentName: str, parentLibraryName: str) -> None:
        ...
    def GetParameterEditable(self) -> bool:
        ...
    def SetParameterEditable(self, isEditable: bool) -> None:
        ...
    def UnassignAllObjects(self) -> None:
        ...
    def GetUsage(self, objects: typing.List[NXObject]) -> None:
        ...
    def Copy(self, partObject: NXObject) -> ParamLibParameter:
        ...
    def CopyLibParamToPart(self, partObject: NXObject) -> ParamLibParameter:
        ...
    def CopyLibParamToPart(self, partObject: NXObject, editable: bool) -> ParamLibParameter:
        ...
    def Delete(self) -> None:
        ...
    def DeleteUserParameterModels(self) -> None:
        ...
    def DeleteOrphanedUserParameterModels(self) -> None:
        ...
    def ResyncWithLibraryDefinition(self) -> None:
        ...
    def UpdateParameterProperties(self) -> None:
        ...
    def InfoParameter(self) -> None:
        ...
    def InfoParameterToFile(self, bOverride: bool, pcFileName: str) -> None:
        ...
    def GetPropTable(self) -> BasePropertyTable:
        ...


class ParamLibLibraryManagerBuilder(Builder):
    def __init__(self) -> None: ...


class ParameterTableCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[ParameterTable]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, tableName: str) -> ParameterTable:
        ...
    def ImportFile(self, fileName: str, remember: bool) -> ParameterTable:
        ...
    def ImportFileWithErrorInfo(self, fileName: str, remember: bool, expName: str) -> ParameterTable:
        ...
    def FindObject(self, journalIdentifier: str) -> ParameterTable:
        ...
    def Tag(self) -> Tag: ...



class ParameterTable(NXObject):
    def __init__(self) -> None: ...
    def RenameTable(self, tableName: str) -> None:
        ...
    def RemoveTable(self) -> None:
        ...
    def DeactivateTable(self) -> None:
        ...
    def GetNumberOfConfigurations(self) -> int:
        ...
    def AddConfiguration(self, configurationName: str) -> int:
        ...
    def RemoveConfiguration(self, configurationName: str) -> None:
        ...
    def SetConfigurationName(self, configIndex: int, configurationName: str) -> None:
        ...
    def RenameConfiguration(self, oldConfigurationName: str, configurationName: str) -> None:
        ...
    def GetNumberOfExpressions(self) -> int:
        ...
    def GetExpressionName(self, index: int) -> str:
        ...
    def GetExpressionLabel(self, index: int) -> str:
        ...
    def AddExpression(self, expressionName: str) -> None:
        ...
    def RemoveExpression(self, expressionName: str) -> None:
        ...
    def ReplaceExpression(self, oldExpressionName: str, expressionName: str) -> None:
        ...
    def ReplaceExpressionLabel(self, expressionName: str, labelName: str) -> None:
        ...
    def IsExpressionUsedByTable(self, expressionName: str) -> bool:
        ...
    def GetConfigurationValue(self, configurationName: str, expressionName: str) -> str:
        ...
    def SetConfigurationValue(self, configIndex: int, expressionName: str, value: str) -> None:
        ...
    def GetConfigurationName(self, index: int) -> str:
        ...
    def ActivateConfiguration(self, configIndex: int, activate: bool) -> None:
        ...
    def ActivateConfiguration(self, configurationName: str, activate: bool) -> None:
        ...
    def ConfigurationIsActive(self, configIndex: int) -> bool:
        ...
    def ConfigurationIsActive(self, configurationName: str) -> bool:
        ...
    def GetActiveConfigurationIndex(self) -> int:
        ...
    def RemoveReference(self) -> None:
        ...
    def UpdateFromFile(self) -> None:
        ...
    def UpdateModel(self) -> None:
        ...
    TableName: str


class Parameter(System.Object):










    def __init__(self) -> None: ...
    def __init__(self, nValue: int) -> None: ...
    def __init__(self, fValue: float) -> None: ...
    def __init__(self, bValue: bool) -> None: ...
    def __init__(self, strValue: str) -> None: ...
    def __init__(self, pValues: int, size: int, type: int) -> None: ...
    def SetValue(self, nValue: int) -> None:
        ...
    def SetValue(self, fValue: float) -> None:
        ...
    def SetValue(self, bValue: bool) -> None:
        ...
    def SetValue(self, strValue: str) -> None:
        ...
    def SetValue(self, pValues: int, size: int, type: int) -> None:
        ...


class ParabolaCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Parabola]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class Parabola(Conic):
    def __init__(self) -> None: ...
    FocalLength: float
    MaximumDY: float
    MinimumDY: float


class OuterEdgesOfFacesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, facesOfFeatures: typing.List[NXObject]) -> None:
        ...


class OriginMethod(enum.Enum):
    SpecifyPoint = 0
    WorkPartOrigin = 1


class Operation(System.Object):
    def __init__(self, pItem: int) -> None: ...
    def FetchOperation(self, pItem: int) -> Operation:
        ...
    IsActive: bool
    Duration: float


    class Operation.Factory(System.Object):
        def Create(self, pItem: int) -> Operation:
            ...
        def __init__(self) -> None: ...
    

class OffsetCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Offset]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateOffset(self, origin: Point3d, vector: Vector3d, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateOffsetRectangular(self, deltaX: Scalar, deltaY: Scalar, deltaZ: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateOffsetCylindrical(self, radius: Scalar, angle: Scalar, deltaZ: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateOffsetSpherical(self, radius: Scalar, angle1: Scalar, angle2: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateOffset(self, direction: Direction, distance: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvature(self, icurve: ICurve, t: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvature(self, atPoint: Point, icurve: ICurve, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvatureDerivative(self, icurve: ICurve, t: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvatureDerivative(self, atPoint: Point, icurve: ICurve, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvature(self, face: Face, u: Scalar, v: Scalar, absoluteUv: bool, option: Offset.OnFaceOption, sectionDirection: Direction, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvatureDerivative(self, face: Face, u: Scalar, v: Scalar, absoluteUv: bool, option: Offset.OnFaceOption, sectionDirection: Direction, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvature(self, atPoint: Point, face: Face, option: Offset.OnFaceOption, sectionDirection: SmartObject, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvatureDerivative(self, atPoint: Point, face: Face, option: Offset.OnFaceOption, sectionDirection: SmartObject, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvature(self, face: Face, u: Scalar, v: Scalar, absoluteUv: bool, sectionAngle: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateCurvatureDerivative(self, face: Face, u: Scalar, v: Scalar, absoluteUv: bool, sectionAngle: Scalar, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def CreateOffset(self, offsetIn: Offset, xform: Xform, updateOption: SmartObject.UpdateOption) -> Offset:
        ...
    def Tag(self) -> Tag: ...



class Offset(SmartObject):
    def __init__(self) -> None: ...
    def ReverseDirection(self) -> bool:
        ...
    Vector: Vector3d


    class OnFaceOption(enum.Enum):
        U = 0
        V = 1
        Section = 2
    

class ObjectTypeSelector(Builder):
    def __init__(self) -> None: ...
    Annotations: bool
    Attributes: bool
    ConvergentBodies: bool
    Csys: bool
    Curves: bool
    FacetBodies: bool
    Kinematic: bool
    PmiData: bool
    ProductData: bool
    Solids: bool
    Structures: bool
    Surfaces: bool
    Tessellation: bool


class ObjectSelector(Builder):
    def __init__(self) -> None: ...
    SelectionComp: SelectNXObjectList
    SelectionScope: ObjectSelector.Scope


    class Scope(enum.Enum):
        EntirePart = 0
        SelectedObjects = 1
    

class ObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def Append(self, object: TaggedObject) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: TaggedObject) -> int:
        ...
    def FindItem(self, index: int) -> TaggedObject:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: TaggedObject) -> None:
        ...
    def Erase(self, obj: TaggedObject, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[TaggedObject]:
        ...
    def SetContents(self, objects: typing.List[TaggedObject]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: TaggedObject, object2: TaggedObject) -> None:
        ...
    def Insert(self, location: int, object: TaggedObject) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


    class DeleteOption(enum.Enum):
        Delete = 0
        NoDelete = 1
    

class ObjectGeneralPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    def Delete(self) -> None:
        ...
    def GetNameLocation(self) -> Point3d:
        ...
    def SetNameLocation(self, nameLocation: Point3d) -> None:
        ...
    def ApplyToAllOccurrences(self) -> None:
        ...
    Active: bool
    AddComponents: bool
    AddIndex: bool
    ApplyToComponent: bool
    GroupDisplayProperties: bool
    Index: int
    Name: str
    NameLocationSpecified: bool
    SelectedObjects: SelectNXObjectList
    TopLevel: bool
    UniqueMembership: bool


class NXTo2dCreator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveNxto2dSettings(self, filename: str) -> None:
        ...
    def SaveIgesSettings(self, filename: str) -> None:
        ...
    def SetDrawingArray(self, objects: typing.List[TaggedObject]) -> None:
        ...
    DrawingName: str
    ExportData: NXTo2dCreator.ExportDataOption
    ExportFrom: NXTo2dCreator.ExportFromOption
    ExportSelectionBlock: ObjectSelector
    FacetBodies: bool
    IgesSettingsFile: str
    InputFile: str
    Jama: bool
    MaxLineThickness: float
    MaxSystem3DModelSpace: bool
    MaxSystemPointRes: bool
    MaxUser3DModelSpace: float
    MaxUserPointRes: float
    Nxto2dSettingsFile: str
    OutputFileType: NXTo2dCreator.OutputAsOption
    OutputTo: NXTo2dCreator.OutputToOption
    OverlappingEntities: bool
    SpCurveTolerance: float
    ViewName: str


    class OutputToOption(enum.Enum):
        Modeling = 0
        Drafting = 1
    

    class OutputAsOption(enum.Enum):
        NXPartFile = 0
        IGESFile = 1
    

    class ExportFromOption(enum.Enum):
        DisplayPart = 0
        ExistingPart = 1
    

    class ExportDataOption(enum.Enum):
        ModelData = 0
        Drawing = 1
    

class NXObjectList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[NXObject]) -> None:
        ...
    def Append(self, object: NXObject) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: NXObject) -> int:
        ...
    def FindItem(self, index: int) -> NXObject:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: NXObject) -> None:
        ...
    def Erase(self, obj: NXObject, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[NXObject]:
        ...
    def SetContents(self, objects: typing.List[NXObject]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: NXObject, object2: NXObject) -> None:
        ...
    def Insert(self, location: int, object: NXObject) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class NXObject(TaggedObject):
    def __init__(self) -> None: ...
    def SetUserAttribute(self, info: NXObject.AttributeInformation, option: Update.Option) -> None:
        ...
    def SetUserAttribute(self, title: str, index: int, value: int, option: Update.Option) -> None:
        ...
    def SetUserAttribute(self, title: str, index: int, value: float, option: Update.Option) -> None:
        ...
    def SetUserAttribute(self, title: str, index: int, value: str, option: Update.Option) -> None:
        ...
    def SetUserAttribute(self, title: str, index: int, option: Update.Option) -> None:
        ...
    def SetTimeUserAttribute(self, title: str, index: int, value: str, option: Update.Option) -> None:
        ...
    def SetTimeUserAttribute(self, title: str, index: int, value: NXObject.ComputationalTime, option: Update.Option) -> None:
        ...
    def SetBooleanUserAttribute(self, title: str, index: int, value: bool, option: Update.Option) -> None:
        ...
    def CreateAttributeIterator(self) -> AttributeIterator:
        ...
    def HasUserAttribute(self, iterator: AttributeIterator) -> bool:
        ...
    def HasUserAttribute(self, title: str, type: NXObject.AttributeType, index: int) -> bool:
        ...
    def GetUserAttributeCount(self, iterator: AttributeIterator) -> int:
        ...
    def GetUserAttributeCount(self, iterator: AttributeIterator, countArrayAsOneAttribute: bool) -> int:
        ...
    def GetUserAttributeCount(self, type: NXObject.AttributeType) -> int:
        ...
    def GetUserAttributeCount(self, type: NXObject.AttributeType, includeUnset: bool, countArrayAsOneAttribute: bool) -> int:
        ...
    def GetUserAttributeSize(self, title: str, type: NXObject.AttributeType) -> int:
        ...
    def GetNextUserAttribute(self, iterator: AttributeIterator, info: NXObject.AttributeInformation) -> bool:
        ...
    def GetUserAttribute(self, title: str, type: NXObject.AttributeType, index: int) -> NXObject.AttributeInformation:
        ...
    def GetBooleanUserAttribute(self, title: str, index: int) -> bool:
        ...
    def GetIntegerUserAttribute(self, title: str, index: int) -> int:
        ...
    def GetRealUserAttribute(self, title: str, index: int) -> float:
        ...
    def GetStringUserAttribute(self, title: str, index: int) -> str:
        ...
    def GetTimeUserAttribute(self, title: str, index: int) -> str:
        ...
    def GetComputationalTimeUserAttribute(self, title: str, index: int) -> NXObject.ComputationalTime:
        ...
    def GetUserAttributes(self, iterator: AttributeIterator) -> typing.List[NXObject.AttributeInformation]:
        ...
    def GetUserAttributes(self) -> typing.List[NXObject.AttributeInformation]:
        ...
    def GetUserAttributes(self, includeUnset: bool) -> typing.List[NXObject.AttributeInformation]:
        ...
    def GetUserAttributeAsString(self, title: str, type: NXObject.AttributeType, index: int) -> str:
        ...
    def DeleteUserAttributes(self, iterator: AttributeIterator, option: Update.Option) -> None:
        ...
    def DeleteUserAttribute(self, type: NXObject.AttributeType, title: str, deleteEntireArray: bool, option: Update.Option) -> None:
        ...
    def DeleteUserAttributes(self, type: NXObject.AttributeType, option: Update.Option) -> None:
        ...
    def SetUserAttributeLock(self, title: str, type: NXObject.AttributeType, lock: bool) -> None:
        ...
    def GetUserAttributeLock(self, title: str, type: NXObject.AttributeType) -> bool:
        ...
    def GetUserAttributeSourceObjects(self) -> typing.List[NXObject]:
        ...
    def SetPdmReferenceAttribute(self, attributeTitle: str, attributeValue: str) -> None:
        ...
    def GetPdmReferenceAttributeValue(self, attributeTitle: str) -> str:
        ...
    def GetUserAttribute(self, title: str, includeUnset: bool, addStringValues: bool, type: NXObject.AttributeType) -> typing.List[NXObject.AttributeInformation]:
        """[Obsolete("Deprecated in NX11.0.0.  Use GetUserAttribute instead.")"""
        ...
    def GetUserAttributes(self, includeUnset: bool, addStringValues: bool) -> typing.List[NXObject.AttributeInformation]:
        """[Obsolete("Deprecated in NX11.0.0.  Use GetUserAttributes instead.")"""
        ...
    def DeleteAllAttributesByType(self, type: NXObject.AttributeType) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use DeleteUserAttributes instead.")"""
        ...
    def DeleteAllAttributesByType(self, type: NXObject.AttributeType, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use DeleteUserAttributes instead.")"""
        ...
    def SetAttribute(self, title: str, value: int) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetAttribute(self, title: str, value: int, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetAttribute(self, title: str, value: float) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetAttribute(self, title: str, value: float, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetAttribute(self, title: str, value: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetAttribute(self, title: str, value: str, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetAttribute(self, title: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetAttribute(self, title: str, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetTimeAttribute(self, title: str, value: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetTimeAttribute(self, title: str, value: str, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def GetIntegerAttribute(self, title: str) -> int:
        """[Obsolete("Deprecated in NX8.0.0.  Use GetUserAttribute instead.")"""
        ...
    def GetRealAttribute(self, title: str) -> float:
        """[Obsolete("Deprecated in NX8.0.0.  Use GetUserAttribute instead.")"""
        ...
    def GetStringAttribute(self, title: str) -> str:
        """[Obsolete("Deprecated in NX8.0.0.  Use GetUserAttribute instead.")"""
        ...
    def GetTimeAttribute(self, format: NXObject.DateAndTimeFormat, title: str) -> str:
        """[Obsolete("Deprecated in NX8.0.0.  Use GetUserAttribute instead.")"""
        ...
    def GetReferenceAttribute(self, title: str) -> str:
        """[Obsolete("Deprecated in NX8.0.0.  Use GetUserAttribute instead.")"""
        ...
    def DeleteAttributeByTypeAndTitle(self, type: NXObject.AttributeType, title: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use DeleteUserAttribute instead.")"""
        ...
    def DeleteAttributeByTypeAndTitle(self, type: NXObject.AttributeType, title: str, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use DeleteUserAttribute instead.")"""
        ...
    def SetReferenceAttribute(self, title: str, value: str) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def SetReferenceAttribute(self, title: str, value: str, option: Update.Option) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  Use SetUserAttribute instead.")"""
        ...
    def GetAttributeTitlesByType(self, type: NXObject.AttributeType) -> typing.List[NXObject.AttributeInformation]:
        """[Obsolete("Deprecated in NX8.0.0.  Use GetUserAttributes instead.")"""
        ...
    def GetUserAttributesAsStrings(self) -> str:
        """[Obsolete("Deprecated in NX8.5.0.  Use GetUserAttributes instead.")"""
        ...
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


    class DateAndTimeFormat(enum.Enum):
        Numeric = 0
        Textual = 1
    

    class NXObjectComputationalTime():
        Day: int
        Minute: int
        def ToString(self) -> str:
            ...
        def __init__(self, Day: int, Minute: int) -> None: ...
    

    class AttributeType(enum.Enum):
        Invalid = 0
        Null = 1
        Boolean = 2
        Integer = 3
        Real = 4
        String = 5
        Time = 6
        Reference = 7
        Any = 100
    

    class NXObjectAttributeInformation():
        Type: NXObject.AttributeType
        Category: str
        Title: str
        TitleAlias: str
        BooleanValue: bool
        IntegerValue: int
        RealValue: float
        StringValue: str
        TimeValue: str
        CompTimeValue: NXObject.ComputationalTime
        ReferenceValue: str
        Inherited: bool
        IsOverride: bool
        Locked: bool
        OwnedBySystem: bool
        Required: bool
        Unset: bool
        Array: bool
        PdmBased: bool
        NotSaved: bool
        ArrayElementIndex: int
        Unit: Unit
        Expression: Expression
        def ToString(self) -> str:
            ...
    

    class NXObject_AttributeInformation():
        type: NXObject.AttributeType
        category: int
        title: int
        titleAlias: int
        booleanValue: bool
        integerValue: int
        realValue: float
        stringValue: int
        timeValue: int
        compTimeValue: NXObject.ComputationalTime
        referenceValue: int
        inherited: bool
        isOverride: bool
        locked: bool
        ownedBySystem: bool
        required: bool
        unset: bool
        array: bool
        pdmBased: bool
        notSaved: bool
        arrayElementIndex: int
        unit: Tag
        expression: Tag
    

class NXMessageBox(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def Show(self, title: str, msgboxType: NXMessageBox.DialogType, message: str) -> int:
        ...
    def Show(self, title: str, msgboxType: NXMessageBox.DialogType, messages: str) -> int:
        ...
    def Tag(self) -> Tag: ...



    class DialogType(enum.Enum):
        Error = 0
        Warning = 1
        Information = 2
        Question = 3
    

class NXMatrixCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[NXMatrix]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, element: Matrix3x3) -> NXMatrix:
        ...
    def FindObject(self, sid: str) -> NXMatrix:
        ...
    def Tag(self) -> Tag: ...



class NXMatrix(NXObject):
    def __init__(self) -> None: ...
    Element: Matrix3x3


class NxFacet(IFacet):
    def __init__(self) -> None: ...
    OwningFacetedBody: Facet.FacetedBody


class NXException(System.ApplicationException):
    def Create(self, status: int) -> NXException:
        ...
    def Create(self, message: str) -> NXException:
        ...
    def Create(self, status: int, message: str) -> NXException:
        ...
    def CreateWithoutUndoMark(self, status: int) -> NXException:
        ...
    def AssertErrorCode(self, status: int) -> None:
        ...
    def ThrowUnexpectedSuccess(self) -> None:
        ...
    def GetObjectData(self) -> None:
        ...
    ErrorCode: int
    Message: str
    UndoMark: int


class NXColor(Utilities.NXRemotableObject):
    def GetRgb(self) -> NXColor.Rgb:
        ...
    Handle: int
    Id: int
    Label: str


    class NXColorRgb():
        R: float
        G: float
        B: float
        def ToString(self) -> str:
            ...
        def __init__(self, R: float, G: float, B: float) -> None: ...
    

    class NXColor.Factory(System.Object):
        def _Get(self, handle: int) -> NXColor:
            ...
        def __init__(self) -> None: ...
    

class NestingStock(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Length: float
    Name: str
    Priority: NestingStock.Priorities
    Quantity: int
    Thickness: float
    Width: float


    class Priorities(enum.Enum):
        Lowest = 0
        Low = 1
        Normal = 2
        High = 3
        Highest = 4
    

class NestingSettings(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddLayerToCutLayers(self, layer: int) -> None:
        ...
    def GetCutLayers(self) -> int:
        ...
    def ClearCutLayers(self) -> None:
        ...
    def AddLayerToAttachLayers(self, layer: int) -> None:
        ...
    def GetAttachLayers(self) -> int:
        ...
    def ClearAttachLayers(self) -> None:
        ...
    BatchQuantity: int
    EdgeToPartDistance: float
    NestDirection: NestingSettings.NestDirections
    NestTime: float
    OutputFilePath: str
    PartToPartDistance: float
    StandardStockFilePath: str


    class NestDirections(enum.Enum):
        BottomLeft = 0
        BottomRight = 1
        TopLeft = 2
        TopRight = 3
    

class NestingPart(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AllowMirror: bool
    Format: NestingPart.Formats
    Include: bool
    IsValid: bool
    Material: str
    Name: str
    Priority: NestingPart.Priorities
    Quantity: int
    Rotation: NestingPart.Rotations
    RotationTolerance: float
    Thickness: float


    class Rotations(enum.Enum):
        Free = 0
        None = 1
        Degrees90 = 2
        Degrees180 = 3
    

    class Priorities(enum.Enum):
        Lowest = 0
        Low = 1
        Normal = 2
        High = 3
        Highest = 4
    

    class Formats(enum.Enum):
        Prt = 0
        Dxf = 1
    

class NestedSolution(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    CutLength: float
    Identifier: int
    NumberOfPartsNested: int
    NumberOfSheetsUsed: int
    NumberOfUnplacedParts: int
    Utilization: float


class NavigatorFilter(TaggedObject):
    def __init__(self) -> None: ...
    Clause: str
    Name: str


class NamespaceDoc(System.Object):
    def __init__(self) -> None: ...


class MWUpdate(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def UpdateLock(self) -> None:
        ...
    def SetLockState(self) -> None:
        ...


class MovieSettingsBuilder(Builder):
    def __init__(self) -> None: ...
    CaptureArea: MovieSettingsBuilder.CaptureAreaChoices
    CodecFourcc: str
    FramesPerSecond: int
    PlaybackSpeed: MovieSettingsBuilder.PlaybackSpeedChoices


    class PlaybackSpeedChoices(enum.Enum):
        VerySlow = 0
        Slow = 1
        AsRecorded = 2
        Fast = 3
        VeryFast = 4
    

    class CaptureAreaChoices(enum.Enum):
        Graphics = 0
        NxWindow = 1
        Desktop = 2
    

class MovieManager(Utilities.NXRemotableObject):
    def __init__(self, owner: UI) -> None: ...
    def CreateMovieSettingsBuilder(self) -> MovieSettingsBuilder:
        ...
    def Start(self, filename: str, userFrames: bool) -> None:
        ...
    def Pause(self) -> None:
        ...
    def Resume(self) -> None:
        ...
    def End(self) -> None:
        ...
    def CaptureFrame(self) -> None:
        ...
    def SetPlaybackSpeed(self, fps: int) -> None:
        ...
    def Tag(self) -> Tag: ...



class MorphMeshTaskEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Enter(self) -> None:
        ...
    def Exit(self) -> None:
        ...
    def SetFeatureToEdit(self, feature: Features.MorphMesh) -> None:
        ...
    def SetCancelled(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveMorphMeshFeature: Features.MorphMesh


class ModlConstraint(DisplayableObject):
    def __init__(self) -> None: ...
    def GetConstraintType(self) -> ModlConstraint.RelationType:
        ...
    def GetConstraintGeometryArray(self) -> typing.List[NXObject]:
        ...


    class RelationType(enum.Enum):
        Coplanar = 0
        Coplaxis = 1
        EqualRadius = 2
        Offset = 3
        Parallel = 4
        Perpendicular = 5
        Symmetric = 6
        Tangent = 7
        Coaxial = 8
    

class ModelingViewList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[ModelingView]) -> None:
        ...
    def Append(self, object: ModelingView) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: ModelingView) -> int:
        ...
    def FindItem(self, index: int) -> ModelingView:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: ModelingView) -> None:
        ...
    def Erase(self, obj: ModelingView, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[ModelingView]:
        ...
    def SetContents(self, objects: typing.List[ModelingView]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: ModelingView, object2: ModelingView) -> None:
        ...
    def Insert(self, location: int, object: ModelingView) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ModelingViewHighQualityImage(Utilities.NXRemotableObject):
    def __init__(self, owner: ModelingView) -> None: ...
    def Generate(self) -> None:
        ...
    def Save(self, imageFileName: str, compressImage: bool) -> None:
        ...
    def Erase(self) -> None:
        ...
    def Plot(self, resolution: Preferences.SessionVisualizationHighQualityImage.ResolutionType, dotsPerInch: int, plotQuality: Preferences.SessionVisualizationHighQualityImage.PlotQualityType, plotFileName: str) -> None:
        ...
    def ShowImageInformation(self) -> None:
        ...
    def GetImageCounts(self, numberBodiesRendered: int, numberFacesRendered: int, numberPolygonsGenerated: int, polygonGenerationSeconds: float, shadowGenerationSeconds: float, imageGenerationSeconds: float) -> None:
        ...
    def Tag(self) -> Tag: ...

    DisplayTechnique: ModelingViewHighQualityImage.DisplayTechniqueType
    FacetsQuality: float
    Format: ModelingViewHighQualityImage.FormatType
    Method: ModelingViewHighQualityImage.ShadeMethod
    Shadows: bool
    UseIbl: bool


    class ShadeMethod(enum.Enum):
        Flat = 0
        Gouraud = 1
        Phong = 2
        Improved = 3
        Preview = 4
        PhotoRealistic = 5
        RayTraced = 6
        RayTracedFfa = 7
        Radiosity = 8
        HybridRadiosity = 9
    

    class FormatType(enum.Enum):
        RasterImage = 0
        QtvrPanorama = 1
        QtvrObjectLow = 2
        QtvrObjectHigh = 3
    

    class DisplayTechniqueType(enum.Enum):
        RgbPlusNoise = 0
        FsRgb = 1
        FsRgbPlusNoise = 2
        Monochrome = 3
        GrayScale = 4
        NearestRgb = 5
        OrderedDither = 6
        TcPlusNoise = 7
    

class ModelingViewCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[ModelingView]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> ModelingView:
        ...
    def ExpandCollapseModelViewNode(self, expand: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    WorkView: ModelingView


class ModelingView(View):
    def __init__(self) -> None: ...
    def UseDefaultLights(self) -> None:
        ...
    def UseSceneLights(self) -> None:
        ...
    def IsDynamicSectionVisible(self, dynamicSection: Display.DynamicSection) -> bool:
        ...
    def SetDynamicSectionVisible(self, dynamicSection: Display.DynamicSection, visible: bool) -> None:
        ...
    def ExpandCollapseNode(self, expand: bool) -> None:
        ...
    HiqhQualityImage: ModelingViewHighQualityImage
    ActiveDynamicSection: Display.DynamicSection
    DisplaySectioningToggle: bool
    IsMirrored: bool


class MeshProfileString(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


    class Type(enum.Enum):
        Profile = 1
        Guide = 2
        Orient = 3
        Scale = 4
        Spine = 5
    

    class SelectedPoint(enum.Enum):
        None = 0
        First = 1
        Last = 2
        Both = 3
    

    class InsertOrder(enum.Enum):
        After = 0
        Before = 1
    

class MeshParameterData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    AlignmentType: MeshParameterData.Type
    Emphasize: MeshParameterData.Type
    FitMethod: MeshParameterData.Type
    Patch: MeshParameterData.Type
    UseSplinePoint: bool
    Vclose: MeshParameterData.Type
    Vdegree: int


    class Type(enum.Enum):
        Unused = 0
        AlignedByParameter = 1
        AlignedByArclength = 2
        AlignedByDistance = 3
        AlignedByAngle = 4
        AlignedBySpine = 5
        AlignedByPoint = 6
        AlignedBySplinePt = 7
        AlignedBySegment = 8
        PatchBezier = 9
        PatchBspline = 10
        PatchClosedBspline = 11
        PatchMatchString = 12
        EmphasizePrimary = 13
        EmphasizeCross = 14
        EmphasizeBoth = 15
        FitExact = 16
        FitApproximate = 17
        VclosedOpen = 18
        VclosedClose = 19
    

    class FeatureType(enum.Enum):
        CurveMesh = 2
        ThroughCurves = 3
        Ruled = 4
    

class MeasureRectangularExtreme(GenericMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    Point: Point3d


class MeasurePolarRadius(SingleMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbeddedObject(self, name: str) -> Scalar:
        ...


class MeasurePolarArea(SingleMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbeddedObject(self, name: str) -> Scalar:
        ...


class MeasurePolarAngle(SingleMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbeddedObject(self, name: str) -> Scalar:
        ...


class MeasurePoint(GenericMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...


class Measurement(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def DisplayArcLength(self, selectedObjects: typing.List[DisplayableObject]) -> None:
        ...
    def GetArcLength(self, selectedObjects: typing.List[DisplayableObject]) -> float:
        ...
    def DisplayMinimumDistance(self, object1: DisplayableObject, object2: DisplayableObject, closePoint1: Point3d, closePoint2: Point3d) -> None:
        ...
    def DisplayMinimumDistance(self, object1: NXObject, startPointForObject1: Point3d, object2: NXObject, startPointForObject2: Point3d, closePoint1: Point3d, closePoint2: Point3d) -> None:
        ...
    def DisplayMinimumDistance(self, object1: NXObject, startPointForObject1: Point3d, object2: NXObject, closePoint1: Point3d, closePoint2: Point3d) -> None:
        ...
    def DisplayMinimumDistance(self, object1: NXObject, object2: NXObject, startPointForObject2: Point3d, closePoint1: Point3d, closePoint2: Point3d) -> None:
        ...
    def GetMinimumDistance(self, object1: NXObject, object2: NXObject, closePoint1: Point3d, closePoint2: Point3d, accuracy: float) -> float:
        ...
    def GetMinimumDistance(self, object1: NXObject, startPointForObject1: Point3d, object2: NXObject, startPointForObject2: Point3d, closePoint1: Point3d, closePoint2: Point3d, accuracy: float) -> float:
        ...
    def GetMinimumDistance(self, object1: NXObject, startPointForObject1: Point3d, object2: NXObject, closePoint1: Point3d, closePoint2: Point3d, accuracy: float) -> float:
        ...
    def GetMinimumDistance(self, object1: NXObject, object2: NXObject, startPointForObject2: Point3d, closePoint1: Point3d, closePoint2: Point3d, accuracy: float) -> float:
        ...
    def DisplayAngle(self, object1: NXObject, position1: Point3d, object2: NXObject, position2: Point3d) -> None:
        ...
    def GetAngle(self, object1: NXObject, position1: Point3d, object2: NXObject, position2: Point3d) -> float:
        ...
    def DisplayDeviationChecking(self, curve1: ICurve, curve2: ICurve, numOfCheckPoints: int, distanceTolerance: float, angularTolerance: float, reportType: Measurement.DeviationReportType) -> None:
        ...
    def DisplayDeviationChecking(self, curve1: Curve, face2: Face, numOfCheckPoints: int, distanceTolerance: float, angularTolerance: float, reportType: Measurement.DeviationReportType) -> None:
        ...
    def DisplayDeviationChecking(self, face1: Face, edge1: Edge, face2: Face, numOfCheckPoints: int, distanceTolerance: float, angularTolerance: float, reportType: Measurement.DeviationReportType) -> None:
        ...
    def DisplayDeviationChecking(self, face1: Face, face2: Face, numOfCheckPointsU: int, numOfCheckPointsV: int, distanceTolerance: float, angularTolerance: float, reportType: Measurement.DeviationReportType) -> None:
        ...
    def DisplayDeviationChecking(self, face1: Face, edge1: Edge, face2: Face, edge2: Edge, numOfCheckPoints: int, distanceTolerance: float, angularTolerance: float, reportType: Measurement.DeviationReportType) -> None:
        ...
    def DisplayArcLengthBetweenPoints(self, point1: Point, point2: Point) -> None:
        ...
    def GetArcLengthBetweenPoints(self, point1: Point, point2: Point, length: float, curves: typing.List[Curve]) -> None:
        ...
    def DisplayRoutingPathLength(self, selectedObjects: typing.List[Routing.ISegment], usedObjects: typing.List[Routing.ISegment]) -> None:
        ...
    def GetRoutingPathLength(self, selectedObjects: typing.List[NXObject], usedObjects: typing.List[NXObject], individualLengths: float) -> float:
        ...
    def GetMinimumOrthogonalDistance(self, object1: DisplayableObject, object2: DisplayableObject, closestOrthogonalPoint: Point3d) -> float:
        ...
    def GetAngleQualifier(self, proto: DisplayableObject, requireExact: bool, seed: float, flip: bool) -> None:
        ...
    def GetAngle(self, alternateSolution: Measurement.AlternateAngle, requireExact: bool, object1: DisplayableObject, object2: DisplayableObject, pt1: Point3d, pt2: Point3d, pt3: Point3d, isApproximate: bool) -> float:
        ...
    def GetDistance(self, alternateSolution: Measurement.AlternateDistance, requireExact: bool, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject], pt1: Point3d, pt2: Point3d, isApproximate: bool) -> float:
        ...
    def GetFaceProperties(self, faces: typing.List[Face], accuracy: float, alternateSolution: Measurement.AlternateFace, requireExact: bool, area: float, perimeter: float, radiusDiameter: float, cog: Point3d, minRadiusOfCurvature: float, areaErrorEstimate: float, anchorPoint: Point3d, isApproximate: bool) -> None:
        ...
    def GetBodyProperties(self, bodys: typing.List[Body], accuracy: float, useWCS: bool, massProps: float, weight: float, centroid: Point3d, centroidUnit: float, density: float, axis: float) -> None:
        ...
    def GetProjectedDistanceProperties(self, selList1: typing.List[NXObject], selList2: typing.List[NXObject], vectorTag: NXObject, targetUnit: NXObject, requireExact: bool, alternateSolution: int, distance: float, points: typing.List[Point3d], isApproximate: bool) -> None:
        ...
    def GetEulerAnglesProperties(self, csys1Tag: NXObject, csys2Tag: NXObject, alternateSolution: int, targetUnit: NXObject, theta1: float, theta2: float, theta3: float) -> None:
        ...
    def GetArcAndCurveProperties(self, selList: typing.List[NXObject], targetUnit: NXObject, requireExact: bool, isApproximate: bool, arcLength: float, radius: float, diameter: float, minRadiusOfCurvature: float, startPoint: Point3d, endPoint: Point3d, arcCenter: Point3d) -> None:
        ...
    def GetPolarAngleProperties(self, collector: ScCollector, center: Point, vector: IReferenceAxis, minAngle: bool, targetUnit: NXObject, angle: float, p1: Point3d, p2: Point3d, p3: Point3d, axis: Point3d) -> None:
        ...
    def GetPolarAreaProperties(self, collector: ScCollector, targetUnit: NXObject, p1: Point3d, p2: Point3d, axis: Point3d) -> float:
        ...
    def GetPolarRadiusProperties(self, collector: ScCollector, center: Point, minDist: bool, targetUnit: NXObject, radius: float, p1: Point3d, p2: Point3d, axis: float) -> None:
        ...
    def GetExtremePointProperties(self, collector: ScCollector, vectors: typing.List[Direction]) -> Point3d:
        ...
    def GetPointProperties(self, point: Point, csys: NXObject, coords: typing.List[Point3d]) -> None:
        ...
    def GetCenterlineProperties(self, selList: typing.List[NXObject], targetUnit: NXObject, pvUGCurves: typing.List[NXObject], startPoint: Point3d, endPoint: Point3d) -> float:
        ...
    def GetBoundingBoxProperties(self, selList: typing.List[NXObject], nAltSolution: int, ptAnchor: Point3d, allowCache: bool, boxPoints: typing.List[Point3d], dir: typing.List[Point3d], edgeLength: float, ptOrigin: Point3d, ptExtreme: Point3d, pdVolume: float) -> None:
        ...
    def Tag(self) -> Tag: ...



    class QuickMeasureValueType(enum.Enum):
        Length = 0
        Distance = 1
        Area = 2
        Volume = 3
        Mass = 4
        InnerAngle = 5
        OuterAngle = 6
        Radius = 7
        Diameter = 8
        Undefined = 9
    

    class QuickMeasureType(enum.Enum):
        Distance = 0
        Curve = 1
        Face = 2
        ProjectedDistance = 3
        AngleThreePoints = 4
        CombinedFace = 5
        CombinedLength = 6
        CombinedBody = 7
        Angle = 8
        Body = 9
        Point = 10
        ArcLengthTwoPoints = 11
        EulerAngle = 12
        BoundingBox = 13
        SurfaceCenterLine = 14
        PolarAngle = 15
        PolarArea = 16
        PolarRadius = 17
        ExtremePoint = 18
        Last = 19
    

    class DeviationReportType(enum.Enum):
        NoDeviation = 0
        AllDeviation = 1
        MaximumDistance = 2
        MinimumDistance = 3
        MaximumAngle = 4
        MinimumAngle = 5
    

    class AlternateFace(enum.Enum):
        Radius = 0
        Diameter = 1
    

    class AlternateDistance(enum.Enum):
        Minimum = 0
        Maximum = 1
        MaximumCenterToEdge = 2
        MaximumEdgeToCenter = 3
        CenterToCenter = 4
        Thickness = 5
    

    class AlternateAngle(enum.Enum):
        Inner = 0
        Outer = 1
        Supplimental = 2
    

class MeasureMasterBuilder(Builder):
    def __init__(self) -> None: ...


class MeasureMaster(Features.Feature):
    def __init__(self) -> None: ...
    def SetNameSuffix(self, name: str) -> None:
        ...
    def GetMeasureElement(self, elementIndex: int) -> MeasureElement:
        ...
    def FixupModelingParents(self) -> None:
        ...
    def GetElementCount(self) -> int:
        ...
    SequenceType: MeasureMaster.Sequence
    UpdateAtTimestamp: bool


    class Sequence(enum.Enum):
        Free = 0
        Pair = 1
        Chain = 2
        Reference = 3
        Reference2 = 4
        Reference3 = 5
    

class MeasureManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def NewPoint(self, point: Point, csys: CartesianCoordinateSystem, createExpressions: bool) -> MeasurePoint:
        ...
    def EditPoint(self, feature: Measure, object1: Point, object2: CartesianCoordinateSystem) -> None:
        ...
    def InitializePoint(self, feature: Measure) -> MeasurePoint:
        ...
    def NewDistance(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, object1: DisplayableObject, object2: DisplayableObject) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, createGeometry: bool, object1: DisplayableObject, object2: DisplayableObject) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, object1: DisplayableObject) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, object1: DisplayableObject, mType: MeasureManager.RadialMeasureType) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, object1: NXObject, object2: NXObject) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, createGeometry: bool, object1: NXObject, object2: NXObject) -> MeasureDistance:
        ...
    def NewScDistance(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, collection1: ScCollector, collection2: ScCollector) -> MeasureDistance:
        ...
    def NewScDistance(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, createGeometry: bool, collection1: ScCollector, collection2: ScCollector) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, object1: DisplayableObject, startPointForObject1: Point3d, object2: DisplayableObject, startPointForObject2: Point3d) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, createGeometry: bool, object1: DisplayableObject, startPointForObject1: Point3d, object2: DisplayableObject, startPointForObject2: Point3d) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, object1: DisplayableObject, object2: DisplayableObject, direction: Direction) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, object1: DisplayableObject, object2: DisplayableObject, direction: Direction, projType: MeasureManager.ProjectionType) -> MeasureDistance:
        ...
    def NewDistance(self, units: Unit, object1: DisplayableObject, object2: DisplayableObject, direction: Direction, projType: MeasureManager.ProjectionType, createGeometry: bool) -> MeasureDistance:
        ...
    def NewScDistance(self, units: Unit, collection1: ScCollector, collection2: ScCollector, direction: Direction, projType: MeasureManager.ProjectionType) -> MeasureDistance:
        ...
    def NewScDistance(self, units: Unit, collection1: ScCollector, collection2: ScCollector, direction: Direction, projType: MeasureManager.ProjectionType, createGeometry: bool) -> MeasureDistance:
        ...
    def EditDistance(self, feature: Measure, object1: NXObject, object2: NXObject) -> None:
        ...
    def EditScDistance(self, feature: Measure, object1: ScCollector, object2: ScCollector, measurementType: MeasureManager.MeasureType) -> None:
        ...
    def EditDistance(self, feature: Measure, object1: DisplayableObject, startPointForObject1: Point3d, object2: DisplayableObject, startPointForObject2: Point3d) -> None:
        ...
    def EditDistance(self, feature: Measure, object1: DisplayableObject, object2: DisplayableObject, direction: Direction) -> None:
        ...
    def EditDistance(self, feature: Measure, object1: DisplayableObject, object2: DisplayableObject, direction: Direction, projType: MeasureManager.ProjectionType) -> None:
        ...
    def EditDistance(self, feature: Measure, object1: DisplayableObject) -> None:
        ...
    def EditDistance(self, name: str, object1: DisplayableObject, object2: DisplayableObject) -> None:
        ...
    def EditDistance(self, name: str, object1: DisplayableObject, startPointForObject1: Point3d, object2: DisplayableObject, startPointForObject2: Point3d) -> None:
        ...
    def EditDistance(self, name: str, object1: DisplayableObject, object2: DisplayableObject, direction: Direction) -> None:
        ...
    def EditDistance(self, name: str, object1: DisplayableObject, object2: DisplayableObject, direction: Direction, projType: MeasureManager.ProjectionType) -> None:
        ...
    def EditDistance(self, name: str, object1: DisplayableObject) -> None:
        ...
    def InitializeDistance(self, feature: Measure) -> MeasureDistance:
        ...
    def NewLength(self, units: Unit, objects: ScCollector) -> MeasureLength:
        ...
    def NewLength(self, units: Unit, objects: typing.List[DisplayableObject]) -> MeasureLength:
        ...
    def EditLength(self, feature: Measure, objects: ScCollector) -> None:
        ...
    def EditLength(self, feature: Measure, objects: typing.List[DisplayableObject]) -> None:
        ...
    def EditLength(self, name: str, objects: ScCollector) -> None:
        ...
    def EditLength(self, name: str, objects: typing.List[DisplayableObject]) -> None:
        ...
    def InitializeLength(self, feature: Measure) -> MeasureLength:
        ...
    def NewAngle(self, units: Unit, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType, minorAngle: bool) -> MeasureAngle:
        ...
    def NewAngle(self, units: Unit, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType, minorAngle: bool, trueAngle: bool) -> MeasureAngle:
        ...
    def NewAngle(self, units: Unit, basePoint: Point, endPoint1: Point, endPoint2: Point, minorAngle: bool) -> MeasureAngle:
        ...
    def NewAngle(self, units: Unit, createGeometry: bool, basePoint: Point, endPoint1: Point, endPoint2: Point, minorAngle: bool) -> MeasureAngle:
        ...
    def EditAngle(self, feature: Measure, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType, minorAngle: bool) -> None:
        ...
    def EditAngle(self, feature: Measure, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType, minorAngle: bool, trueAngle: bool) -> None:
        ...
    def EditAngle(self, feature: Measure, basePoint: Point, endPoint1: Point, endPoint2: Point, minorAngle: bool) -> None:
        ...
    def EditAngle(self, name: str, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType, minorAngle: bool) -> None:
        ...
    def EditAngle(self, name: str, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType, minorAngle: bool, trueAngle: bool) -> None:
        ...
    def EditAngle(self, name: str, basePoint: Point, endPoint1: Point, endPoint2: Point, minorAngle: bool) -> None:
        ...
    def InitializeAngle(self, feature: Measure) -> MeasureAngle:
        ...
    def NewFaceProperties(self, areaUnit: Unit, lengthUnit: Unit, accuracy: float, objects: ScCollector) -> MeasureFaces:
        ...
    def NewFaceProperties(self, areaUnit: Unit, lengthUnit: Unit, accuracy: float, objects: typing.List[IParameterizedSurface]) -> MeasureFaces:
        ...
    def EditFaceProperties(self, feature: Measure, objects: ScCollector) -> None:
        ...
    def EditFaceProperties(self, feature: Measure, objects: typing.List[IParameterizedSurface]) -> None:
        ...
    def EditFaceProperties(self, name: str, objects: ScCollector) -> None:
        ...
    def EditFaceProperties(self, name: str, objects: typing.List[IParameterizedSurface]) -> None:
        ...
    def InitializeFaceProperties(self, feature: Measure) -> MeasureFaces:
        ...
    def NewMassProperties(self, massUnits: typing.List[Unit], accuracy: float, objects: ScCollector) -> MeasureBodies:
        ...
    def NewMassProperties(self, massUnits: typing.List[Unit], accuracy: float, createGeometry: bool, objects: ScCollector) -> MeasureBodies:
        ...
    def NewMassProperties(self, massUnits: typing.List[Unit], accuracy: float, objects: typing.List[IBody]) -> MeasureBodies:
        ...
    def NewMassProperties(self, massUnits: typing.List[Unit], tolerances: float, objects: ScCollector) -> MeasureBodies:
        ...
    def NewMassProperties(self, massUnits: typing.List[Unit], tolerances: float, createGeometry: bool, objects: ScCollector) -> MeasureBodies:
        ...
    def NewMassProperties(self, massUnits: typing.List[Unit], tolerances: float, objects: typing.List[IBody]) -> MeasureBodies:
        ...
    def EditMassProperties(self, feature: Measure, objects: ScCollector) -> None:
        ...
    def EditMassProperties(self, feature: Measure, objects: typing.List[IBody]) -> None:
        ...
    def EditMassProperties(self, name: str, objects: ScCollector) -> None:
        ...
    def EditMassProperties(self, name: str, objects: typing.List[IBody]) -> None:
        ...
    def InitializeMassProperties(self, feature: Measure) -> MeasureBodies:
        ...
    def CreateMeasureDistanceBuilder(self, feature: NXObject) -> MeasureDistanceBuilder:
        ...
    def CreateMeasureAngleBuilder(self, feature: NXObject) -> MeasureAngleBuilder:
        ...
    def CreateMeasureFaceBuilder(self, feature: NXObject) -> MeasureFaceBuilder:
        ...
    def CreateMeasureBodyBuilder(self, feature: NXObject) -> MeasureBodyBuilder:
        ...
    def NewPointsOnCurvesLength(self, units: Unit, objects: typing.List[Point]) -> MeasureLength:
        ...
    def CreateRoutingMeasureDistanceBuilder(self, feature: NXObject) -> Routing.RoutingMeasureDistanceBuilder:
        ...
    def NewRoutingPathLength(self, units: Unit, objects: typing.List[NXObject]) -> MeasureLength:
        ...
    def CreateRoutingMeasureDistanceBuilder(self, feature: NXObject, measureDistanceBuilder: MeasureDistanceBuilder) -> Routing.RoutingMeasureDistanceBuilder:
        ...
    def NewPolarRadius(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, point: Point, objects: ScCollector) -> MeasurePolarRadius:
        ...
    def NewPolarRadius(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, point: Point, objects: ScCollector, createGeometry: bool) -> MeasurePolarRadius:
        ...
    def EditPolarRadius(self, feature: Measure, minMaxFlag: MeasureManager.MeasureType, point: Point, objects: ScCollector) -> None:
        ...
    def InitializePolarRadius(self, feature: Measure) -> MeasurePolarRadius:
        ...
    def NewPolarAngle(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, point: Point, vector: Direction, objects: ScCollector) -> MeasurePolarAngle:
        ...
    def NewPolarAngle(self, units: Unit, minMaxFlag: MeasureManager.MeasureType, point: Point, vector: Direction, objects: ScCollector, createGeometry: bool) -> MeasurePolarAngle:
        ...
    def EditPolarAngle(self, feature: Measure, minMaxFlag: MeasureManager.MeasureType, point: Point, vector: Direction, objects: ScCollector) -> None:
        ...
    def InitializePolarAngle(self, feature: Measure) -> MeasurePolarAngle:
        ...
    def NewPolarArea(self, units: Unit, objects: ScCollector, createExpressions: bool) -> MeasurePolarArea:
        ...
    def NewPolarArea(self, units: Unit, objects: ScCollector, createExpressions: bool, createGeometry: bool) -> MeasurePolarArea:
        ...
    def EditPolarArea(self, feature: Measure, objects: ScCollector) -> None:
        ...
    def InitializePolarArea(self, feature: Measure) -> MeasurePolarArea:
        ...
    def ExtremePoint(self, units: Unit, vector1: Direction, vector2: Direction, vector3: Direction, objects: ScCollector, createExpressions: bool) -> MeasureExtremePoint:
        ...
    def ExtremePoint(self, units: Unit, vector1: Direction, vector2: Direction, vector3: Direction, objects: ScCollector, createExpressions: bool, createGeometry: bool) -> MeasureExtremePoint:
        ...
    def EditExtremePoint(self, feature: Measure, vector1: Direction, vector2: Direction, vector3: Direction, objects: ScCollector) -> None:
        ...
    def InitializeExtremePoint(self, feature: Measure) -> MeasureExtremePoint:
        ...
    def NewRectangularExtreme(self, units: Unit, vector1: Direction, vector2: Direction, vector3: Direction, objects: ScCollector, createExpressions: bool) -> MeasureRectangularExtreme:
        ...
    def NewRectangularExtreme(self, units: Unit, vector1: Direction, vector2: Direction, vector3: Direction, objects: ScCollector, createExpressions: bool, createGeometry: bool) -> MeasureRectangularExtreme:
        ...
    def EditRectangularExtreme(self, feature: Measure, vector1: Direction, vector2: Direction, vector3: Direction, objects: ScCollector) -> None:
        ...
    def InitializeRectangularExtreme(self, feature: Measure) -> MeasureRectangularExtreme:
        ...
    def CreateMeasureMasterBuilder(self, feature: NXObject) -> MeasureMasterBuilder:
        ...
    def MasterMeasurement(self) -> MeasureMaster:
        ...
    def ShowMeasureAnnotation(self, feature: MeasureMaster) -> None:
        ...
    def DistanceElement(self, masterMeasurement: MeasureMaster, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject]) -> MeasureElement:
        ...
    def EmbeddedDistance(self, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject], name: str) -> Scalar:
        ...
    def EditDistanceElement(self, data: MeasureElement, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject]) -> None:
        ...
    def EditEmbeddedDistance(self, measurement: Scalar, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject]) -> None:
        ...
    def FacePropertiesElement(self, masterMeasurement: MeasureMaster, faceUnits: typing.List[Unit], alternateSolution: int, requireExact: bool, accuracy: float, objects: ScCollector) -> MeasureElement:
        ...
    def EmbeddedFaceProperties(self, outputField: int, faceUnits: typing.List[Unit], alternateSolution: int, requireExact: bool, accuracy: float, objects: ScCollector, name: str) -> Scalar:
        ...
    def EditFacePropertiesElement(self, data: MeasureElement, faceUnits: typing.List[Unit], alternateSolution: int, requireExact: bool, accuracy: float, objects: ScCollector) -> None:
        ...
    def EditEmbeddedFaceProperties(self, measurement: Scalar, outputField: int, faceUnits: typing.List[Unit], alternateSolution: int, requireExact: bool, accuracy: float, objects: ScCollector) -> None:
        ...
    def CurvePropertiesElement(self, masterMeasurement: MeasureMaster, lengthUnit: Unit, alternateSolution: int, requireExact: bool, curves: ScCollector, extraObjects: typing.List[DisplayableObject]) -> MeasureElement:
        ...
    def EmbeddedCurveProperties(self, outputField: int, lengthUnit: Unit, alternateSolution: int, requireExact: bool, curves: ScCollector, name: str) -> Scalar:
        ...
    def EditCurvePropertiesElement(self, data: MeasureElement, lengthUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, extraObjects: typing.List[DisplayableObject]) -> None:
        ...
    def EditEmbeddedCurveProperties(self, measurement: Scalar, outputField: int, lengthUnit: Unit, alternateSolution: int, requireExact: bool, curves: ScCollector) -> None:
        ...
    def AngleElement(self, masterMeasurement: MeasureMaster, angleUnit: Unit, alternateSolution: int, requireExact: bool, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType) -> MeasureElement:
        ...
    def EmbeddedAngle(self, angleUnit: Unit, alternateSolution: int, requireExact: bool, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType, name: str) -> Scalar:
        ...
    def EditAngleElement(self, data: MeasureElement, angleUnit: Unit, alternateSolution: int, requireExact: bool, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType) -> None:
        ...
    def EditEmbeddedAngle(self, measurement: Scalar, angleUnit: Unit, alternateSolution: int, requireExact: bool, object1: DisplayableObject, qualifier1: MeasureManager.EndpointType, object2: DisplayableObject, qualifier2: MeasureManager.EndpointType) -> None:
        ...
    def Angle3ptElement(self, masterMeasurement: MeasureMaster, angleUnit: Unit, alternateSolution: int, requireExact: bool, basePoint: Point, endPoint1: Point, endPoint2: Point) -> MeasureElement:
        ...
    def EmbeddedAngle3pt(self, angleUnit: Unit, alternateSolution: int, requireExact: bool, basePoint: Point, endPoint1: Point, endPoint2: Point, name: str) -> Scalar:
        ...
    def EditAngle3ptElement(self, data: MeasureElement, angleUnit: Unit, alternateSolution: int, requireExact: bool, basePoint: Point, endPoint1: Point, endPoint2: Point) -> None:
        ...
    def EditEmbeddedAngle3pt(self, measurement: Scalar, angleUnit: Unit, alternateSolution: int, requireExact: bool, basePoint: Point, endPoint1: Point, endPoint2: Point) -> None:
        ...
    def ProjectedDistanceElement(self, masterMeasurement: MeasureMaster, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject], direction: IReferenceAxis) -> MeasureElement:
        ...
    def EmbeddedProjectedDistance(self, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject], direction: IReferenceAxis, name: str) -> Scalar:
        ...
    def EditProjectedDistanceElement(self, data: MeasureElement, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject], direction: IReferenceAxis) -> None:
        ...
    def EditEmbeddedProjectedDistance(self, measurement: Scalar, lengthUnit: Unit, alternateSolution: int, requireExact: bool, collection1: ScCollector, collection2: ScCollector, objects1: typing.List[DisplayableObject], objects2: typing.List[DisplayableObject], direction: IReferenceAxis) -> None:
        ...
    def BodyElement(self, masterMeasurement: MeasureMaster, massUnits: typing.List[Unit], accuracy: float, objects: ScCollector) -> MeasureElement:
        ...
    def EditBodyElement(self, data: MeasureElement, massUnits: typing.List[Unit], accuracy: float, objects: ScCollector) -> None:
        ...
    def PointElement(self, masterMeasurement: MeasureMaster, point: Point, csys: CartesianCoordinateSystem) -> MeasureElement:
        ...
    def EmbeddedPoint(self, point: Point, csys: CartesianCoordinateSystem, name: str) -> Scalar:
        ...
    def EditPointElement(self, data: MeasureElement, point: Point, csys: CartesianCoordinateSystem) -> None:
        ...
    def EditEmbeddedPoint(self, measurement: Scalar, point: Point, csys: CartesianCoordinateSystem) -> None:
        ...
    def EulerAnglesElement(self, masterMeasurement: MeasureMaster, angleUnit: Unit, alternateSolution: int, csys1: CartesianCoordinateSystem, csys2: CartesianCoordinateSystem) -> MeasureElement:
        ...
    def EditEulerAnglesElement(self, data: MeasureElement, angleUnit: Unit, alternateSolution: int, csys1: CartesianCoordinateSystem, csys2: CartesianCoordinateSystem) -> None:
        ...
    def CleanupAssociativeGeometry(self) -> None:
        ...
    def CreateDimensionAnnotation(self, startPoint: Point3d, endPoint: Point3d, annotationText: str) -> Annotations.Annotation:
        ...
    def CreateDimensionAnnotationOnPosition(self, startPoint: Point3d, endPoint: Point3d, position: Point3d, annotationText: str) -> Annotations.Annotation:
        ...
    def CreateNoteAnnotation(self, anchorPoint: Point3d, annotationText: str) -> Annotations.Annotation:
        ...
    def CreateNoteAnnotationOnPosition(self, anchorPoint: Point3d, position: Point3d, annotationText: str) -> Annotations.Annotation:
        ...
    def CreateAngleAnnotation(self, basePoint: Point3d, endPoint1: Point3d, endPoint2: Point3d, alternateSolution: int, annotationText: str) -> Annotations.Annotation:
        ...
    def CreateAngleAnnotationOnPosition(self, basePoint: Point3d, endPoint1: Point3d, endPoint2: Point3d, position: Point3d, alternateSolution: int, annotationText: str) -> Annotations.Annotation:
        ...
    def CenterlinePropertiesElement(self, masterMeasurement: MeasureMaster, centerlineUnits: typing.List[Unit], objects: ScCollector) -> MeasureElement:
        ...
    def EmbeddedCenterlineProperties(self, outputField: int, centerlineUnits: typing.List[Unit], objects: ScCollector, name: str) -> Scalar:
        ...
    def EditCenterlinePropertiesElement(self, data: MeasureElement, centerlineUnits: typing.List[Unit], objects: ScCollector) -> None:
        ...
    def EditEmbeddedCenterlineProperties(self, measurement: Scalar, outputField: int, centerlineUnits: typing.List[Unit], objects: ScCollector) -> None:
        ...
    def BboxPropertiesElement(self, masterMeasurement: MeasureMaster, centerlineUnits: typing.List[Unit], objects: ScCollector, altSolution: int) -> MeasureElement:
        ...
    def EmbeddedBboxProperties(self, outputField: int, centerlineUnits: typing.List[Unit], objects: ScCollector, name: str, altSolution: int) -> Scalar:
        ...
    def EditBboxPropertiesElement(self, data: MeasureElement, bboxUnits: typing.List[Unit], altSolution: int, objects: ScCollector) -> None:
        ...
    def EditEmbeddedBboxProperties(self, measurement: Scalar, outputField: int, bboxUnits: typing.List[Unit], altSolution: int, objects: ScCollector) -> None:
        ...
    def PolarAngleElement(self, masterMeasurement: MeasureMaster, angleUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originPoint: Point, direction: IReferenceAxis) -> MeasureElement:
        ...
    def EditPolarAngleElement(self, data: MeasureElement, angleUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originPoint: Point, direction: IReferenceAxis) -> None:
        ...
    def EmbeddedPolarAngle(self, angleUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originPoint: Point, direction: IReferenceAxis) -> Scalar:
        ...
    def EditEmbeddedPolarAngle(self, measurement: Scalar, angleUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originTag: Point, direction: IReferenceAxis) -> None:
        ...
    def PolarRadiusElement(self, masterMeasurement: MeasureMaster, radiusUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originPoint: Point) -> MeasureElement:
        ...
    def EditPolarRadiusElement(self, data: MeasureElement, radiusUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originPoint: Point) -> None:
        ...
    def EmbeddedPolarRadius(self, radiusUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originPoint: Point) -> Scalar:
        ...
    def EditEmbeddedPolarRadius(self, measurement: Scalar, radiusUnit: Unit, alternateSolution: int, requireExact: bool, objects: ScCollector, originTag: Point) -> None:
        ...
    def PolarAreaElement(self, masterMeasurement: MeasureMaster, radiusUnit: Unit, requireExact: bool, objects: ScCollector) -> MeasureElement:
        ...
    def EditPolarAreaElement(self, data: MeasureElement, radiusUnit: Unit, requireExact: bool, objects: ScCollector) -> None:
        ...
    def EmbeddedPolarArea(self, areaUnit: Unit, requireExact: bool, objects: ScCollector) -> Scalar:
        ...
    def EditEmbeddedPolarArea(self, measurement: Scalar, areaUnit: Unit, requireExact: bool, objects: ScCollector) -> None:
        ...
    def ExtremePointElement(self, masterMeasurement: MeasureMaster, units: Unit, requireExact: bool, objects: ScCollector, vector1: Direction, vector2: Direction, vector3: Direction) -> MeasureElement:
        ...
    def EditExtremePointElement(self, data: MeasureElement, unit: Unit, requireExact: bool, objects: ScCollector, vector1: Direction, vector2: Direction, vector3: Direction) -> None:
        ...
    def EmbeddedExtremePoint(self, units: Unit, requireExact: bool, objects: ScCollector, vector1: Direction, vector2: Direction, vector3: Direction) -> Scalar:
        ...
    def EditEmbeddedExtremePoint(self, measurement: Scalar, areaUnit: Unit, requireExact: bool, objects: ScCollector, vector1: Direction, vector2: Direction, vector3: Direction) -> None:
        ...
    def GetIsMeasureAnnotation(self, annotation: NXObject) -> bool:
        ...
    def SetPartTransientModification(self) -> None:
        ...
    def ClearPartTransientModification(self) -> None:
        ...
    def SetSelectionIntent(self, measurement: Scalar, selectionIntent1: int, selectionIntent2: int) -> None:
        ...
    def GetSelectionIntent(self, measurement: Scalar, selectionIntent1: int, selectionIntent2: int) -> None:
        ...
    def Tag(self) -> Tag: ...



    class RadialMeasureType(enum.Enum):
        Radius = 0
        Diameter = 1
    

    class ProjectionType(enum.Enum):
        Minimum = 0
        MinClearance = 1
        MaxClearance = 2
        Maximum = 3
    

    class MeasureType(enum.Enum):
        Minimum = 0
        Maximum = 1
    

    class ExtremeType(enum.Enum):
        Rectangular = 0
        PolarRadius = 1
        PolarAngle = 2
        PolarArea = 3
        ExtremePoint = 4
    

    class EndpointType(enum.Enum):
        None = 0
        StartPoint = 1
        EndPoint = 2
    

class MeasureLength(SingleMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbedded(self) -> str:
        """[Obsolete("Deprecated in NX5.0.1.  Use MeasureLength.CreateEmbeddedObject instead.")"""
        ...
    def CreateEmbeddedObject(self, name: str) -> Scalar:
        ...


class MeasureFaces(GenericMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbedded(self, measurementType: MeasureFaces.ActiveValue) -> str:
        """[Obsolete("Deprecated in NX5.0.1.  Use MeasureFaces.CreateEmbeddedObject instead.")"""
        ...
    def CreateEmbeddedObject(self, measurementType: MeasureFaces.ActiveValue, name: str) -> Scalar:
        ...
    Accuracy: float
    Area: float
    Perimeter: float


    class ActiveValue(enum.Enum):
        Area = 0
        Perimeter = 1
    

class MeasureFaceBuilder(MeasureBuilder):
    def __init__(self) -> None: ...
    FaceCollector: ScCollector
    FaceObjects: SelectDisplayableObjectList


class MeasureExtremePoint(SingleMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    Point: Point3d


class MeasureElement(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetExpressionState(self, outputIndex: int) -> bool:
        ...
    def SetExpressionState(self, outputIndex: int, state: bool) -> None:
        ...
    def GetGeometryState(self, outputIndex: int) -> bool:
        ...
    def SetGeometryState(self, outputIndex: int, state: bool) -> None:
        ...
    def GetAnnotationState(self, outputIndex: int) -> bool:
        ...
    def SetAnnotationState(self, outputIndex: int, state: bool) -> None:
        ...
    def GetApproximateState(self, outputIndex: int) -> bool:
        ...
    def SetApproximateState(self, outputIndex: int, state: bool) -> None:
        ...
    def CreateAnnotation(self) -> Annotations.Annotation:
        ...
    def EditAnnotation(self) -> None:
        ...
    def CreateGeometry(self) -> None:
        ...
    def UpdateRequirements(self, requirementCheck: Validate.RequirementCheck, outputIndex: int) -> None:
        ...
    def ShowAnnotation(self) -> Annotations.Annotation:
        ...
    def FreeResource(self) -> None:
        ...
    def HideAnnotation(self) -> None:
        ...
    def ShowGeometry(self) -> None:
        ...
    def HideGeometry(self) -> None:
        ...
    def SetAnnotationPosition(self, position: Point3d) -> None:
        ...
    def SetGwifPosition(self, position: Point3d) -> None:
        ...
    def GetMeasureElementExpressions(self, expsTag: typing.List[Expression]) -> None:
        ...
    def GetMeasureElementExpressionsType(self, expsType: str) -> None:
        ...
    def GetMeasureElementCollector1(self) -> ScCollector:
        ...
    def GetMeasureElementCollector2(self) -> ScCollector:
        ...
    def GetExtraObjects1(self, extraObjects1: typing.List[NXObject]) -> None:
        ...
    def GetExtraObjects2(self, extraObjects2: typing.List[NXObject]) -> None:
        ...
    def SetMeasureElementAccuracy(self, accuracy: float) -> None:
        ...
    def GetMeasureElementAccuracy(self) -> float:
        ...
    AlternateSolution: int
    MeasureObject1: MeasureElement.Measure
    MeasureObject2: MeasureElement.Measure
    SelectionIntent1: int
    SelectionIntent2: int
    SingleSelect1: bool
    SingleSelect2: bool


    class Measure(enum.Enum):
        Object = 0
        Point = 1
        Vector = 2
        Csys = 3
    

class MeasureDistanceBuilder(MeasureBuilder):
    def __init__(self) -> None: ...
    DiameterObjects: SelectDisplayableObject
    DistanceCollector1: ScCollector
    DistanceCollector2: ScCollector
    IsExact: bool
    LengthCollector: ScCollector
    LengthObjects: SelectDisplayableObjectList
    Mtype: MeasureDistanceBuilder.MeasureType
    Object1: SelectDisplayableObject
    Object2: SelectDisplayableObject
    ProjectionVector: Direction
    RadiusObjects: SelectDisplayableObject
    Set1: SelectDisplayableObjectList
    Set2: SelectDisplayableObjectList


    class MeasureType(enum.Enum):
        ToAPoint = 0
        Minimum = 1
        LocalMinimum = 2
        Maximum = 3
        MinClearance = 4
        MaxClearance = 5
    

    class DistanceType(enum.Enum):
        Distance = 0
        SmartDistance = 1
        ProjectedDistance = 2
        SmartProjectedDistance = 3
        ScreenDistance = 4
        Length = 5
        Radius = 6
        Diameter = 7
        PointsOnCurves = 8
        RoutingPathLength = 9
        BetweenSets = 10
    

class MeasureDistance(SingleMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbedded(self) -> str:
        """[Obsolete("Deprecated in NX5.0.1.  Use NXOpen.MeasureDistance.CreateEmbeddedObject instead.")"""
        ...
    def CreateEmbeddedObject(self, name: str) -> Scalar:
        ...


class MeasureBuilder(Builder):
    def __init__(self) -> None: ...
    AnnotationMode: MeasureBuilder.AnnotationType
    InfoWindow: bool
    RequirementMode: MeasureBuilder.RequirementType


    class RequirementType(enum.Enum):
        None = 0
        New = 1
        Existing = 2
    

    class AnnotationType(enum.Enum):
        None = 0
        ShowDimension = 1
        CreateLine = 2
        CreateCsys = 3
    

class MeasureBodyBuilder(MeasureBuilder):
    def __init__(self) -> None: ...
    BodyCollector: ScCollector
    BodyObjects: SelectDisplayableObjectList


class MeasureBodies(GenericMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbedded(self, measurementType: MeasureBodies.ActiveValue) -> str:
        """[Obsolete("Deprecated in NX5.0.1.  Use NXOpen.MeasureBodies.CreateEmbeddedObject instead.")"""
        ...
    def CreateEmbeddedObject(self, measurementType: MeasureBodies.ActiveValue, name: str) -> Scalar:
        ...
    Area: float
    Centroid: Point3d
    InformationUnit: MeasureBodies.AnalysisUnit
    Mass: float
    RadiusOfGyration: float
    Volume: float
    Weight: float


    class AnalysisUnit(enum.Enum):
        PoundInch = 0
        PoundFoot = 1
        GramMillimeter = 2
        GramCentimeter = 3
        KilogramMeter = 4
        KilogramMillimeter = 5
        CustomUnit = 6
    

    class ActiveValue(enum.Enum):
        Volume = 0
        Area = 1
        Mass = 2
        RadiusOfGyration = 3
        Weight = 4
        Centroid = 5
    

class MeasureAngleBuilder(MeasureBuilder):
    def __init__(self) -> None: ...
    BaseEnd: Point
    BasePoint: Point
    Feature1: SelectDisplayableObject
    Feature2: SelectDisplayableObject
    IsExact: bool
    Object1: SelectDisplayableObject
    Object2: SelectDisplayableObject
    Objtype1: MeasureAngleBuilder.ObjectType
    Objtype2: MeasureAngleBuilder.ObjectType
    Orientation: MeasureAngleBuilder.OrientationType
    ProtractorEnd: Point
    Ptype: MeasureAngleBuilder.ProjectionType
    Vector1: Direction
    Vector2: Direction


    class ProjectionType(enum.Enum):
        Angle3d = 0
        AngleXy = 1
        TrueAngle = 2
    

    class OrientationType(enum.Enum):
        InnerAngle = 0
        OuterAngle = 1
    

    class ObjectType(enum.Enum):
        Object = 0
        Feature = 1
        Vector = 2
    

    class AngleType(enum.Enum):
        ThreePoints = 0
        TwoObjects = 1
        ScreenPoints = 2
    

class MeasureAngle(SingleMeasure):
    def __init__(self, ptr: int) -> None: ...
    def CreateFeature(self) -> Measure:
        ...
    def CreateEmbedded(self) -> str:
        """[Obsolete("Deprecated in NX5.0.1.  Use NXOpen.MeasureAngle.CreateEmbeddedObject instead.")"""
        ...
    def CreateEmbeddedObject(self, name: str) -> Scalar:
        ...


class Measure(Features.Feature):
    def __init__(self) -> None: ...


class MCDSignal(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Type: int
    IntValue: int
    FloatValue: float
    BoolValue: bool
    StringValue: str
    BoolValues: bool
    IntValues: int
    FloatValues: float
    StringValues: str
    Active: bool


    class MCDSignal.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Matrix4x4():
    Rxx: float
    Rxy: float
    Rxz: float
    Xt: float
    Ryx: float
    Ryy: float
    Ryz: float
    Yt: float
    Rzx: float
    Rzy: float
    Rzz: float
    Zt: float
    Sx: float
    Sy: float
    Sz: float
    Ss: float
    def ToString(self) -> str:
        ...


class Matrix3x3():
    Xx: float
    Xy: float
    Xz: float
    Yx: float
    Yy: float
    Yz: float
    Zx: float
    Zy: float
    Zz: float
    def ToString(self) -> str:
        ...


class MathUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Orthonormalize(self, original: Matrix3x3) -> Matrix3x3:
        ...
    def Multiply(self, matrix: Matrix3x3, originalVector: Vector3d) -> Vector3d:
        ...
    def Multiply(self, matrix: Matrix3x3, originalPoint: Point3d) -> Point3d:
        ...
    def Tag(self) -> Tag: ...



class MaterialUtilities(Utilities.NXRemotableObject):
    def __init__(self, owner: CAE.CaeSession) -> None: ...
    def ConvertStressStrainData(self, strainData: float, stressData: float, youngsModulus: float, poissionRatio: float, inputDataType: MaterialUtilities.StressStrainData, outputDataType: MaterialUtilities.StressStrainData, convertedStrainData: float, convertedStressData: float) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.MaterialUtilities.ConvertStressStrainYoungsModulusData instead.")"""
        ...
    def ConvertStressStrainYoungsModulusData(self, strainData: float, stressData: float, youngsModulus: float, poissionRatio: float, inputDataType: MaterialUtilities.StressStrainData, outputDataType: MaterialUtilities.StressStrainData, convertedStrainData: float, convertedStressData: float, convertedYoungsModulus: float) -> None:
        ...
    def ConvertIacspercentToElectricalConductivity(self, iacsData: float, electricalConductivityData: float) -> None:
        ...
    def ConvertElectricalConductivityToIacspercent(self, electricalConductivityData: float, iacsData: float) -> None:
        ...
    def Tag(self) -> Tag: ...



    class StressStrainData(enum.Enum):
        EngineeringStressEngineeringStrain = 0
        EngineeringStressEngineeringPlasticStrain = 1
        TrueStressLogStrain = 2
        TrueStressLogPlasticStrain = 3
        Undefined = 4
    

class MaterialManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def Tag(self) -> Tag: ...

    PhysicalMaterials: PhysicalMaterialCollection


class Material(NXObject):
    def __init__(self) -> None: ...


class MassPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateNow(self) -> None:
        ...
    Accuracy: float
    LoadPartialComponents: bool
    SelectedObjects: SelectNXObjectList
    UpdateOnSave: MassPropertiesBuilder.UpdateOptions


    class UpdateOptions(enum.Enum):
        No = 0
        Yes = 1
        Mixed = 2
    

class LogFile(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Write(self, s: str) -> None:
        ...
    def WriteLine(self, s: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    FileName: str


class LoadOptions(Utilities.NXRemotableObject):
    def __init__(self, owner: PartCollection) -> None: ...
    def SetInterpartData(self, interpartOption: bool, parentOption: LoadOptions.Parent) -> None:
        ...
    def GetInterpartData(self, interpartOption: bool, parentOption: LoadOptions.Parent) -> None:
        ...
    def SetBookmarkComponentsToLoad(self, restoreAnt: bool, restoreFullyLoadedStatus: bool, componentsLoadOption: LoadOptions.BookmarkComponents) -> None:
        ...
    def GetBookmarkComponentsToLoad(self, restoreAnt: bool, componentsLoadOption: LoadOptions.BookmarkComponents) -> None:
        ...
    def SetSearchDirectories(self, searchDirectories: str, searchSubDirs: bool) -> None:
        ...
    def GetSearchDirectories(self, searchDirectories: str, searchSubDirs: bool) -> None:
        ...
    def SetDefaultReferenceSets(self, referenceSets: str) -> None:
        ...
    def GetDefaultReferenceSets(self) -> str:
        ...
    def Save(self, optionsFile: str) -> None:
        ...
    def Restore(self, optionsFile: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    AbortOnFailure: bool
    AllowSubstitution: bool
    BookmarkRefsetLoadBehavior: LoadOptions.BookmarkRefsets
    ComponentLoadMethod: LoadOptions.LoadMethod
    ComponentsToLoad: LoadOptions.LoadComponents
    GenerateMissingPartFamilyMembers: bool
    LoadLatest: bool
    ManagedModeComponentLoadMethod: LoadOptions.ManagedModeLoadMethod
    OptionUpdateSubsetOnLoad: LoadOptions.UpdateSubsetOnLoad
    PartLoadOption: LoadOptions.LoadOption
    ReferenceSetOverride: bool
    UseLightweightRepresentations: bool
    UsePartialLoading: bool


    class UpdateSubsetOnLoad(enum.Enum):
        None = 0
        ReplayRecipe = 1
    

    class Parent(enum.Enum):
        Partial = 0
        Immediate = 1
        All = 2
    

    class ManagedModeLoadMethod(enum.Enum):
        ByRevisionRule = 1
        AsSaved = 2
    

    class LoadOption(enum.Enum):
        FullyLoad = 0
        PartiallyLoad = 1
        FullyLoadLightweightDisplay = 2
        PartiallyLoadLightweightDisplay = 3
        MinimallyLoadLightweightDisplay = 4
    

    class LoadMethod(enum.Enum):
        AsSaved = 0
        FromDirectory = 1
        SearchDirectories = 2
    

    class LoadComponents(enum.Enum):
        All = 0
        None = 1
        LastSet = 2
        LastFilter = 3
        SpecifyFilter = 4
    

    class BookmarkRefsets(enum.Enum):
        ImportData = 0
        ImportAndOptimizeLoad = 1
        DontImport = 2
    

    class BookmarkComponents(enum.Enum):
        NoChange = 0
        LoadVisible = 1
        LoadLoaded = 2
        LoadLoadedAndNonDisplayed = 3
    

class ListingWindow(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Open(self) -> None:
        ...
    def Close(self) -> None:
        ...
    def CloseWindow(self) -> None:
        ...
    def WriteLine(self, msg: str) -> None:
        ...
    def WriteFullline(self, msg: str) -> None:
        ...
    def SelectDevice(self, deviceType: ListingWindow.DeviceType, fileName: str) -> None:
        ...
    def Tag(self) -> Tag: ...

    Device: ListingWindow.DeviceType
    IsOpen: bool


    class DeviceType(enum.Enum):
        Window = 0
        File = 1
        FileAndWindow = 2
        None = 3
    

class ListCreatorList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[ListCreator]) -> None:
        ...
    def Append(self, object: ListCreator) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: ListCreator) -> int:
        ...
    def FindItem(self, index: int) -> ListCreator:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: ListCreator) -> None:
        ...
    def Erase(self, obj: ListCreator, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[ListCreator]:
        ...
    def SetContents(self, objects: typing.List[ListCreator]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: ListCreator, object2: ListCreator) -> None:
        ...
    def Insert(self, location: int, object: ListCreator) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ListCreator(Builder):
    def __init__(self) -> None: ...
    AdvCompression: float
    Angular: float
    Chordal: float
    FeatureSuppression: float
    Label: str
    Length: float
    NxLabel: str
    Resolution: ListCreator.ResolutionType
    Simplify: float
    TessOption: ListCreator.TessellationOption


    class TessellationOption(enum.Enum):
        Lw = 0
        Nx = 1
        Defined = 2
    

    class ResolutionType(enum.Enum):
        Coarse = 0
        Standard = 1
        Fine = 2
        ExtraFine = 3
        SuperFine = 4
        UltraFine = 5
        UserDefined = 6
    

class LinkedPartManager(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[LinkedMirrorPartEntityMapEvent]:
        ...
    def __init__(self, owner: Session) -> None: ...
    def __init__(self) -> None: ...
    def AddMapEntityHandler(self, handler: LinkedPartManager.MapEntityHandler) -> int:
        ...
    def RemoveMapEntityHandler(self, id: int) -> None:
        ...
    def AddAttributeEditHandler(self, handler: LinkedPartManager.AttributeEditHandler) -> int:
        ...
    def RemoveAttributeEditHandler(self, id: int) -> None:
        ...
    def Tag(self) -> Tag: ...



    

    

    

    

    

    

class LinkedMirrorPartEntityMapEvent(TaggedObject):
    def __init__(self) -> None: ...
    MapData: LinkedMirrorPartEntityMapData


class LinkedMirrorPartEntityMapData(TaggedObject):
    def __init__(self) -> None: ...
    def GetSourcePartEntitiesToMap(self) -> typing.List[TaggedObject]:
        ...
    def GetMirrorPartEntitiesToMap(self) -> typing.List[TaggedObject]:
        ...
    def GetMappedSourcePartEntities(self) -> typing.List[TaggedObject]:
        ...
    def GetMappedMirrorPartEntities(self) -> typing.List[TaggedObject]:
        ...
    def AddToMap(self, sourceEntity: TaggedObject, mirrorEntity: TaggedObject) -> None:
        ...


class LinkedMirrorPartBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRefSetNames(self) -> str:
        ...
    def SetRefSetNames(self, refSetNames: str) -> None:
        ...
    MirrorCsysMethod: LinkedMirrorPartBuilder.MirrorCsysOption
    MirrorPartName: str
    MirrorPartType: LinkedMirrorPartBuilder.MirrorPartTypeOption
    MirrorPlane: Plane
    MirrorPlaneNormal: Vector3d
    MirrorPlaneOrigin: Point3d
    MirrorPmiFlag: bool
    NewPart: Part
    ParentPart: Part


    class MirrorPartTypeOption(enum.Enum):
        ExactMirror = 0
        NonExactMirrorKeepBrokenLinks = 1
        NonExactMirrorDeleteBrokenLinks = 2
    

    class MirrorCsysOption(enum.Enum):
        MirrorXYAndDeriveZ = 0
        MirrorYZAndDeriveX = 1
        MirrorXZAndDeriveY = 2
    

class LinkedMirrorPartAttributeEditEvent(TaggedObject):
    def __init__(self) -> None: ...
    MapData: LinkedMirrorPartAttributeEditData


class LinkedMirrorPartAttributeEditData(TaggedObject):
    def __init__(self) -> None: ...
    MirrorPart: Part
    SourcePart: Part


class LineWidthOption(enum.Enum):
    Assigned = 0
    Default = 1
    NoChange = 2


class LineWidthBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def IsValidOption(self, widthOption: LineWidthOption) -> bool:
        ...
    def Validate(self) -> bool:
        ...
    Width: DisplayableObject.ObjectWidth
    WidthOption: LineWidthOption


class LineFontOption(enum.Enum):
    Assigned = 0
    Default = 1
    NoChange = 2


class LineFontBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    LineFont: LineFontBuilder.LineFontType


    class LineFontType(enum.Enum):
        NoChange = 0
        Original = 1
        Invisible = 2
        Solid = 3
        Dashed = 4
        Phantom = 5
        Centerline = 6
        Dotted = 7
        LongDashed = 8
        DottedDashed = 9
        Eight = 10
        Nine = 11
        Ten = 12
        Eleven = 13
    

    class LineFontOption(enum.Enum):
        Assigned = 0
        Default = 1
        NoChange = 2
        Invisible = 3
    

class LineColorFontWidthBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    LineColor: NXColor
    LineFont: LineFontBuilder
    LineWidth: DisplayableObject.ObjectWidth


class LineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Line]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Line:
        ...
    def CreateFaceAxis(self, face: IParameterizedSurface, updateOption: SmartObject.UpdateOption) -> Line:
        ...
    def CreateFaceAxisNoParentLoadRequired(self, face: IParameterizedSurface, updateOption: SmartObject.UpdateOption) -> Line:
        ...
    def CreateFaceAxisNoExtension(self, face: IParameterizedSurface, updateOption: SmartObject.UpdateOption) -> Line:
        ...
    def Tag(self) -> Tag: ...



class LinearSpring(SpringJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    AttachVector: VectorArithmetic.Vector3
    BaseVector: VectorArithmetic.Vector3
    SpringConstant: float
    Damping: float
    RelaxedPosition: float
    Active: bool


    class LinearSpring.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class LinearLimit(LimitJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    AttachVector: VectorArithmetic.Vector3
    BaseVector: VectorArithmetic.Vector3
    Minimum: float
    Maximum: float
    Active: bool


    class LinearLimit.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class LinearGripper(Gripper):
    def __init__(self, pItem: int) -> None: ...
    Grip: bool
    Release: bool
    IsOpened: bool
    IsClosed: bool
    StopGrippingAction: bool
    GrippedObject: RigidBody
    HasGrippedObject: bool
    FingerPosition: float
    Speed: float
    MaxPosition: float
    Active: bool


    class LinearGripper.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Line(Curve):
    def __init__(self) -> None: ...
    def SetStartPoint(self, startPoint: Point3d) -> None:
        ...
    def SetEndPoint(self, endPoint: Point3d) -> None:
        ...
    def SetEndpoints(self, startPoint: Point3d, endPoint: Point3d) -> None:
        ...
    EndPoint: Point3d
    StartPoint: Point3d


class LimitSwitch(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Signal: bool
    Active: bool


    class LimitSwitch.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class LimitJoint(Joint):
    def __init__(self, pItem: int) -> None: ...
    AttachVector: VectorArithmetic.Vector3
    BaseVector: VectorArithmetic.Vector3
    Minimum: float
    Maximum: float


class LightType(enum.Enum):
    Ambient = 0
    Distant = 1
    Eye = 2
    Point = 3
    Spot = 4
    Scene = 6


class LightCurtain(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Triggered: bool
    DistanceString: str
    NumBeams: int
    Distances: bool
    Angles: float


    class LightCurtain.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class LightCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Light]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Light:
        ...
    def SetLightIntensities(self, lights: typing.List[Light], intensities: float) -> None:
        ...
    def Tag(self) -> Tag: ...



class Light(NXObject):
    def __init__(self) -> None: ...
    def GetEnabledInView(self, view: View) -> bool:
        ...
    def SetEnabledInView(self, view: View, onOrOff: bool) -> None:
        ...
    def GetLightType(self, lightType: LightType, sceneLightType: Light.SceneType) -> None:
        ...
    Intensity: float


    class SceneType(enum.Enum):
        NotASceneLight = -1
        Ambient = 0
        LeftTop = 1
        Top = 2
        RightTop = 3
        Front = 4
        LeftBottom = 5
        Bottom = 6
        RightBottom = 7
    

class LicenseManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Reserve(self, license: str, contextName: str) -> None:
        ...
    def Release(self, license: str, contextName: str) -> None:
        ...
    def ReleaseAll(self, contextName: str) -> None:
        ...
    def GetReservedLicenses(self, contextName: str) -> str:
        ...
    def GetBundlesSelected(self) -> typing.List[LicenseManager.LicenseBundle]:
        ...
    def SetBundlesForUse(self, bundles: str) -> None:
        ...
    def GetBundlesUsed(self) -> str:
        ...
    def GetActiveLicensesInABundle(self, bundleName: str) -> str:
        ...
    def CheckPresence(self, licenseName: str) -> bool:
        ...
    def IsCheckedOut(self, license: str) -> bool:
        ...
    def Tag(self) -> Tag: ...



    class LicenseManagerLicenseBundle():
        NumUsing: int
        BundleName: str
        def ToString(self) -> str:
            ...
        def __init__(self, NumUsing: int, BundleName: str) -> None: ...
    

    class LicenseManager_LicenseBundle():
        numUsing: int
        bundle_name: int
    

class LayoutDefinition(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetView(self, row: int, column: int, view: View) -> None:
        ...
    def SetView(self, row: int, column: int, view: ModelingView) -> None:
        ...
    Arrangement: LayoutDefinition.ArrangementType


    class ArrangementType(enum.Enum):
        L1 = 0
        L2 = 1
        L3 = 2
        L4 = 3
        L6 = 4
        L9 = 5
        NonStandard = 6
    

class LayoutCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Layout]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, name: str, layoutArrangement: LayoutDefinition, fitAllViews: bool) -> Layout:
        ...
    def NewLayoutDefinition(self, arrangement: LayoutDefinition.ArrangementType, layoutArrangement: LayoutDefinition) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> Layout:
        ...
    def CreateSplitScreenLayoutAndNamedViews(self, leftViewName: str, rightViewname: str, layout: Layout, leftView: View, rightView: View) -> None:
        ...
    def DestroySplitScreenLayoutAndNamedViews(self, layout: Layout) -> None:
        ...
    def ChangeLayout(self, layout: Layout) -> None:
        ...
    def RenameViewsInSplitScreenLayout(self, layout: Layout, leftViewName: str, rightViewName: str) -> None:
        ...
    def ChangeLayoutWithOptions(self, layout: Layout, removeOldLayoutCache: bool, ignoreNewLayoutCache: bool) -> None:
        ...
    def Tag(self) -> Tag: ...

    Current: Layout


class Layout(NXObject):
    def __init__(self) -> None: ...
    def ReplaceView(self, view: ModelingView, row: int, column: int, performFitView: bool) -> None:
        ...
    def ReplaceView(self, oldView: ModelingView, newView: ModelingView, performFitView: bool) -> None:
        ...
    def GetViews(self) -> typing.List[View]:
        ...
    def Open(self) -> None:
        ...
    def Save(self) -> None:
        ...
    def SaveAs(self, layoutName: str) -> Layout:
        ...
    Definition: LayoutDefinition
    DisplayStatus: bool
    WorkView: View


class LaserScanner(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Triggered: bool
    DistanceString: str
    NumBeams: int
    Distances: float
    Angles: float


    class LaserScanner.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class KFObject(TaggedObject):
    def __init__(self) -> None: ...


class JtCreator(Builder):
    def __init__(self) -> None: ...
    def NewLevel(self) -> ListCreator:
        ...
    def LoadConfigSettings(self) -> None:
        ...
    AdvancedMaterial: JtCreator.AdvancedMaterials
    AppendRefset: bool
    ApplyPmi: bool
    AsmStructure: bool
    AutolowLod: bool
    ChordalOption: JtCreator.ChordalValue
    ConfigFile: str
    IncludePmi: JtCreator.PmiOption
    JtParts: bool
    JtWrite: JtCreator.FileWrite
    JtfileStructure: JtCreator.FileStructure
    Kinematics: bool
    LightTextureMaterial: bool
    LighweightLabel: str
    LodList: ListCreatorList
    MergeSheets: bool
    MergeSolids: bool
    OutputJtFile: str
    PreciseGeom: bool
    SmartLod: bool
    TessOption: JtCreator.TessellationOption
    UseRefset: JtCreator.RefsetOption
    WireFrame: bool


    class TessellationOption(enum.Enum):
        Lw = 0
        Nx = 1
        Defined = 2
    

    class RefsetOption(enum.Enum):
        Default = 0
        All = 1
        AllNamed = 2
        AsSpecified = 3
    

    class PmiOption(enum.Enum):
        None = 0
        PartOnly = 1
        AsmOnly = 2
        PartAndAsm = 3
        ThisLevelOnly = 4
    

    class FileWrite(enum.Enum):
        All = 0
        PartsOnly = 1
        AssemblyOnly = 2
    

    class FileStructure(enum.Enum):
        PerPart = 0
        Monolithic = 1
        FullShatter = 2
        Mimic = 3
        Plmxml = 4
        Ap242xml = 5
    

    class ChordalValue(enum.Enum):
        Relative = 0
        Absolute = 1
    

    class AdvancedMaterials(enum.Enum):
        None = 0
        Low = 1
        High = 2
    

class JournalManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def InsertUserDefinedCode(self, userDefinedCode: str) -> None:
        ...
    def InsertComment(self, comment: str) -> None:
        ...
    def PlayDotNetJournal(self, filename: str, arguments: str) -> JournalManager.PlayDotNetJournalInformation:
        ...
    def RecordJournal(self, filename: str) -> None:
        ...
    def StopRecordingJournal(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    IsJournalRecording: bool
    IsJournalRunning: bool
    JournalLanguage: Preferences.SessionUserInterface.JournalLanguageType
    PauseJournal: bool
    PauseJournalingOfBlockStylerCalls: bool


    class JournalManagerPlayDotNetJournalInformation():
        ErrorMessage: str
        WarningMessage: str
        def ToString(self) -> str:
            ...
        def __init__(self, ErrorMessage: str, WarningMessage: str) -> None: ...
    

    class JournalManager_PlayDotNetJournalInformation():
        errorMessage: int
        warningMessage: int
    

class Joint(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetForce(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetForce(self) -> VectorArithmetic.Vector3:
        ...
    def GetTorque(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetTorque(self) -> VectorArithmetic.Vector3:
        ...
    Attach: RigidBody
    Base: RigidBody


class ItemCacheMappedEntityBuilder(Builder):
    def __init__(self) -> None: ...
    ItemDescription: str
    ItemId: int
    ItemName: str
    ItemPropertyTable: CAE.PropertyTable


class ITableEditorDataProvider():
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def SetString(self, rows: int, column: int, stringData: str) -> bool:
        ...
    def GetString(self, row: int, column: int) -> str:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def SetInteger(self, rows: int, column: int, integerData: int) -> bool:
        ...
    def GetInteger(self, row: int, column: int, isUnassigned: bool) -> int:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def SetDouble(self, rows: int, column: int, doubleData: float) -> bool:
        ...
    def GetDouble(self, row: int, column: int, isUnassigned: bool) -> float:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def SetBoolean(self, rows: int, column: int, booleanData: bool) -> bool:
        ...
    def GetBoolean(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, row: int, column: int) -> bool:
        ...
    def UnsetValue(self, rows: int, column: int) -> bool:
        ...
    def Destroy(self) -> None:
        ...
    ColumnCount: int
    RowCount: int




class ISketchHelpedConstraint():
    def GetHelpData(self, hasHelpPoint1: bool, hasHelpPoint2: bool, hasHelpParameter1: bool, hasHelpParameter2: bool, helpPoint1: Point3d, helpPoint2: Point3d, helpParameter1: float, helpParameter2: float) -> None:
        ...
    def SetHelpPoints(self, hasHelp1: bool, hasHelp2: bool, helpPoint1: Point3d, helpPoint2: Point3d) -> None:
        ...
    def SetHelpParameters(self, hasHelp1: bool, hasHelp2: bool, helpParameter1: float, helpParameter2: float) -> None:
        ...


class IRuntimeContext():
    def AskRoot(self) -> ComponentPart:
        ...
    def Error(self, severity: bool, strMessage: str) -> None:
        ...
    def ForcePause(self) -> None:
        ...
    def SetPerformSimulation(self, action: SimulationAction) -> None:
        ...
    def GetRuntimeObject(self, physTag: Tag) -> RuntimeObject:
        ...
    def GetRuntimeObjects(self, physTag: Tag, numOfObjects: int, runtimeObjects: typing.List[RuntimeObject]) -> None:
        ...
    def ProceedSimulation(self, slice: float) -> None:
        ...








class IPlane():
    def SetMethod(self, type: PlaneTypes.MethodType) -> None:
        ...
    def SetExpression(self, valueExpression: str) -> None:
        ...
    def SetFlip(self, flip: bool) -> None:
        ...
    def SetPercent(self, percent: bool) -> None:
        ...
    def SetGeometry(self, geom: typing.List[NXObject]) -> None:
        ...
    def GetGeometry(self) -> typing.List[NXObject]:
        ...
    def Evaluate(self) -> None:
        ...
    def SetAlternate(self, type: PlaneTypes.AlternateType) -> None:
        ...
    def GetAlternate(self) -> PlaneTypes.AlternateType:
        ...
    def GetNumberOfAlternate(self) -> int:
        ...
    def SetReverseSection(self, reverseSection: bool) -> None:
        ...
    def GetReverseSection(self) -> bool:
        ...
    def SetFrenetSubtype(self, subtype: PlaneTypes.FrenetSubtype) -> None:
        ...
    def SetReverseSide(self, reverseSide: bool) -> None:
        ...
    def GetReverseSide(self) -> bool:
        ...
    def SetUpdateOption(self, update: SmartObject.UpdateOption) -> None:
        ...
    def SetOffsetExpression(self, valueExpression: str) -> None:
        ...
    def SetOffsetFlip(self, flip: bool) -> None:
        ...
    def RemoveOffsetData(self) -> None:
        ...
    def ReplaceExpression(self, expTag: Expression) -> None:
        ...
    def ResetExpressionValue(self) -> None:
        ...
    Expression: Expression
    Flip: bool
    FrenetSubtype: PlaneTypes.FrenetSubtype
    Matrix: Matrix3x3
    Method: PlaneTypes.MethodType
    Normal: Vector3d
    OffsetExpression: Expression
    OffsetFlip: bool
    Origin: Point3d
    Percent: bool






class INXObject():
    def FindObject(self, journalIdentifier: str) -> INXObject:
        ...
    def Print(self) -> None:
        ...
    def SetName(self, name: str) -> None:
        ...
    IsOccurrence: bool
    JournalIdentifier: str
    Name: str
    OwningComponent: Assemblies.Component
    OwningPart: BasePart
    Prototype: INXObject


class InverseKinematics(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Effector: RigidBody
    Position: VectorArithmetic.Vector3
    Orientation: VectorArithmetic.Vector3
    Active: bool


    class InverseKinematics.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class InterpartExpressionsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetExpressions(self, sourceExpressions: typing.List[Expression], destinationNames: str) -> None:
        ...
    def SetExpressions(self, sourceExpressions: typing.List[Expression], destinationNames: str) -> None:
        ...
    def SetExpressionsFor4gd(self, targetPartOcc: Assemblies.Component, sourcePartOcc: Assemblies.Component, sourceExpressions: typing.List[Expression], destinationNames: str) -> None:
        ...
    BaseString: str
    NamingRule: InterpartExpressionsBuilder.NamingRules
    ReplaceString: str


    class NamingRules(enum.Enum):
        AddPrefix = 0
        AddSuffix = 1
        Replace = 2
        RenameWithIndex = 3
    

class Information(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def DisplayPartHistory(self, part: BasePart) -> None:
        ...
    def DisplayPointDetails(self, point: Point) -> None:
        ...
    def DisplayPointDetails(self, absolutePointCoordinates: Point3d) -> None:
        ...
    def DisplayObjectsDetails(self, selectedObjects: typing.List[NXObject]) -> None:
        ...
    def DisplayFeatureDetails(self, feature: Features.Feature, type: Information.DisplayFeatureType) -> None:
        ...
    def DisplayInterpartChildren(self, part: Part) -> None:
        ...
    def DisplayInterpartParents(self, part: Part) -> None:
        ...
    def DisplayUpdateStatusReport(self, part: Part) -> None:
        ...
    def DisplayCamObjectsDetails(self, selectedObjects: typing.List[NXObject]) -> None:
        ...
    def DisplayProdIntObjectsDetails(self, selectedObjects: typing.List[NXObject], startCounter: int) -> None:
        ...
    def Tag(self) -> Tag: ...



    class DisplayFeatureType(enum.Enum):
        All = 0
        Expressions = 1
        Parameters = 2
        Dependencies = 3
        FeaturesInBody = 4
        RelatedObject = 5
    

class InfiniteLineCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[InfiniteLine]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> InfiniteLine:
        ...
    def Tag(self) -> Tag: ...



class InfiniteLine(Line):
    def __init__(self) -> None: ...


class InferSnapType(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class SnapType(enum.Enum):
        None = 0
        Start = 1
        End = 2
        Mid = 3
        Knot = 4
        Center = 5
        Exist = 6
        Quadrant = 7
        Intersection = 8
        Curve = 9
        Surf = 10
        Origin = 11
        DrfAid = 12
        DrfTangent = 13
        Pole = 14
        Defining = 15
        ConicAnchor = 16
        BoundedGrid = 17
        FacetVertex = 18
    

class InferredConstraintsBuilder(Builder):
    def __init__(self) -> None: ...
    def GetRules(self) -> typing.List[Sketch.AutoDimensioningRule]:
        ...
    def SetRules(self, rules: typing.List[Sketch.AutoDimensioningRule]) -> None:
        ...
    Coincident: bool
    Collinear: bool
    Concentric: bool
    DimensionalConstraint: bool
    EqualLength: bool
    EqualRadius: bool
    Horizontal: bool
    HorizontalAlignment: bool
    Midpoint: bool
    Parallel: bool
    Perpendicular: bool
    PointOnCurve: bool
    PointOnString: bool
    PreferStringConstraints: bool
    Tangent: bool
    Vertical: bool
    VerticalAlignment: bool


class Inclinometer(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Angle: VectorArithmetic.Vector3
    Active: bool


    class Inclinometer.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class ImportManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreatePartImporter(self) -> PartImporter:
        ...
    def CreateParasolidImporter(self) -> Importer:
        ...
    def CreateCgmImporter(self) -> Importer:
        ...
    def CreateSolidEdgeImporter(self) -> Importer:
        ...
    def CreateVrmlImporter(self) -> VRMLImporter:
        ...
    def CreateStlImporter(self) -> STLImporter:
        ...
    def CreateSteinbichlerImporter(self) -> Importer:
        ...
    def Tag(self) -> Tag: ...



class Importer3MF(DexBuilder):
    def __init__(self) -> None: ...
    Cleanup: bool
    CreateClipLatticeFeature: bool
    FacetBodyType: Importer3MF.FacetBodyTypes
    InputFile: str
    MinimumAngleFoldedFacets: float
    MinimumFacetNumber: int
    ShowInformationWindow: bool
    TessellationFactor: float


    class FacetBodyTypes(enum.Enum):
        Psm = 0
        Nx = 1
    

class Importer(Builder):
    def __init__(self) -> None: ...
    FileName: str


class ImplicitModelingTaskEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Enter(self) -> None:
        ...
    def SetImplicitModelToEdit(self, implicitModel: Features.Feature) -> None:
        ...
    def GetActiveImplicitModel(self) -> Features.Feature:
        ...
    def Exit(self) -> None:
        ...
    def SetCancelled(self) -> None:
        ...
    def Tag(self) -> Tag: ...





class IgesImporter(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    CopiousData: IgesImporter.CopiousDataEnum
    FileOpenFlag: bool
    FlattenAssembly: bool
    GeomFixupTol: float
    ImportTo: IgesImporter.ImportToEnum
    ImportToTeamcenter: bool
    LayerDefault: int
    LayerMask: str
    MapViewDep: bool
    ObjectTypes: ObjectTypeSelector
    Optimize: bool
    SettingsFile: str
    SewSurfaces: bool
    SimplifyGeometry: bool
    SmoothBSurf: bool
    SurfTrimTol: float


    class ImportToEnum(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

    class CopiousDataEnum(enum.Enum):
        CubicNURBBestfitSpline = 0
        LinearNURBSpline = 1
        GroupofLines = 2
    

class IgesCreator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    def SetDrawingArray(self, objects: typing.List[TaggedObject]) -> None:
        ...
    Author: str
    BcurveTol: float
    Company: str
    Csys: CoordinateSystem
    DrawingList: str
    ExportDrawings: bool
    ExportFrom: IgesCreator.ExportFromOption
    ExportModelData: bool
    ExportSelectionBlock: ObjectSelector
    FileSaveFlag: bool
    FlattenAssembly: bool
    IdenticalPointResolution: float
    InputFile: str
    Jama: bool
    LayerMask: str
    MapCrossHatchTo: IgesCreator.CrossHatchMapEnum
    MapRevolvedFacesTo: IgesCreator.MapRevolvedFacesOption
    MapTabCylToBSurf: bool
    MaxLineThickness: float
    MaxThreeDMdlSpace: float
    ObjectTypes: ObjectTypeSelector
    ReceiverID: str
    ReferenceType: IgesCreator.CsysrefEnum
    SettingsFile: str
    StartSectionFile: str
    SysDefidenticalPointResolution: bool
    SysDefmaxThreeDMdlSpace: bool
    UseStartSectionFile: bool
    ViewList: str


    class MapRevolvedFacesOption(enum.Enum):
        BSurfaces = 0
        SurfaceOfRevolution = 1
    

    class ExportFromOption(enum.Enum):
        DisplayPart = 0
        ExistingPart = 1
    

    class CsysrefEnum(enum.Enum):
        Absolute = 0
        Wcs = 1
        SpecifiedCsys = 2
    

    class CrossHatchMapEnum(enum.Enum):
        SectionArea = 0
        CopiousData = 1
    



class IfcImporter(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    BuildingControls: bool
    CollapsePRVsList: str
    Deltax: float
    Deltay: float
    Deltaz: float
    Electrical: bool
    ExcludeElementClassifications: str
    ExcludePRVsList: str
    FileOpenFlag: bool
    FlattenAssembly: bool
    Hvac: bool
    ImportFacetsAsConvergentGeometryList: str
    ImportFacetsAsPreciseGeometryList: str
    ImportFacetsAsXTBrepOrConvergent: IfcImporter.ImportFacetsAsXTBrepOrConvergentEnum
    ImportTo: IfcImporter.ImportToOption
    ImportToTeamcenter: bool
    ImportTooFarHandlingMethod: IfcImporter.ImportTooFarHandlingMethodEnum
    Messages: IfcImporter.MessageEnum
    MoveModelData: IfcImporter.MoveDataEnum
    Optimize: bool
    PlumbingFireProtection: bool
    ProductExtension: bool
    RotateAroundZByDegrees: float
    SettingsFile: str
    SharedBldgServicesElements: bool
    SharedBuildingElements: bool
    SharedComponentElements: bool
    SharedFacilitiesElements: bool
    ShowInformationWindowFlag: bool
    StructuralAnalysis: bool
    StructuralElements: bool


    class MoveDataEnum(enum.Enum):
        ByDeltamm = 0
        To000 = 1
    

    class MessageEnum(enum.Enum):
        None = 0
        Informational = 1
        Warning = 2
        Error = 3
        Debug = 4
        All = 5
    

    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

    class ImportTooFarHandlingMethodEnum(enum.Enum):
        Insertnode = 0
        None = 1
    

    class ImportFacetsAsXTBrepOrConvergentEnum(enum.Enum):
        XTBrep = 0
        ConvergentBodies = 1
    

class IfcCreator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    AngularTolerance: float
    AttributeCategories: str
    Attributes: str
    ChordalTolerance: float
    ChordalToleranceMethodOption: IfcCreator.ChordalToleranceMethodOptionEnum
    ExportFrom: IfcCreator.ExportFromOption
    ExportSelectionBlock: ObjectSelector
    ExportUnits: IfcCreator.UnitsEnum
    ExportUserDefinedAttributes: bool
    FileSaveFlag: bool
    IfcFileFormat: IfcCreator.IfcFormatEnum
    IncludeOrExcludeAttributeCategories: IfcCreator.IncludeOrExcludeAttributeCategoriesEnum
    IncludeOrExcludeAttributes: IfcCreator.IncludeOrExcludeAttributesEnum
    InputFile: str
    RelativeChordalTolerance: float
    SettingsFile: str
    TessellationMethodOption: IfcCreator.TessellationMethodOptionEnum


    class UnitsEnum(enum.Enum):
        Millimeters = 0
        Inches = 1
    

    class TessellationMethodOptionEnum(enum.Enum):
        LightWeightRepresentation = 0
        SpecifyTolerances = 1
    

    class IncludeOrExcludeAttributesEnum(enum.Enum):
        Include = 0
        Exclude = 1
    

    class IncludeOrExcludeAttributeCategoriesEnum(enum.Enum):
        Include = 0
        Exclude = 1
    

    class IfcFormatEnum(enum.Enum):
        IFC2x3 = 0
        Ifc4 = 1
    

    class ExportFromOption(enum.Enum):
        DisplayPart = 0
        ExistingPart = 1
    

    class ChordalToleranceMethodOptionEnum(enum.Enum):
        Relative = 0
        Absolute = 1
    

class IFacet(NXObject):
    def __init__(self) -> None: ...
    def GetIsVisible(self, viewDir: Vector3d) -> bool:
        ...
    FacetIdentifier: int


class IExternalFileReferencer():
    def GetExternalFileReferenceAdapter(self, referenceObjectId: int) -> ExternalFileReferenceAdapter:
        ...
    def SetExternalFileReferenceAdapter(self, referenceObjectId: int, adapter: ExternalFileReferenceAdapter) -> None:
        ...
    def GetExternalFileDefinitionKey(self, adapter: ExternalFileReferenceAdapter) -> str:
        ...
    def EstablishReference(self, referenceObjectId: int, referenceType: ExternalFileReferenceAdapter.Type, externalFileSpec: str) -> ExternalFileReferenceAdapter:
        ...


class IDefinitionContext():
    def Connect(self, strName: str, item: RuntimeObject) -> None:
        ...
    def Connect(self, strName: str, item: ComponentPart) -> None:
        ...
    def Connect(self, strName: str, item: RigidBody) -> None:
        ...
    def Connect(self, strName: str, item: CollisionBody) -> None:
        ...
    def Connect(self, strName: str, item: CollisionSensor) -> None:
        ...
    def Connect(self, strName: str, item: TransportSurface) -> None:
        ...
    def Connect(self, strName: str, item: CollisionMaterial) -> None:
        ...
    def Connect(self, strName: str, item: Joint) -> None:
        ...
    def Connect(self, strName: str, item: AxisJoint) -> None:
        ...
    def Connect(self, strName: str, item: HingeJoint) -> None:
        ...
    def Connect(self, strName: str, item: SlidingJoint) -> None:
        ...
    def Connect(self, strName: str, item: CylindricalJoint) -> None:
        ...
    def Connect(self, strName: str, item: PointOnCurveJoint) -> None:
        ...
    def Connect(self, strName: str, item: CurveOnCurveJoint) -> None:
        ...
    def Connect(self, strName: str, item: FixedJoint) -> None:
        ...
    def Connect(self, strName: str, item: BallJoint) -> None:
        ...
    def Connect(self, strName: str, item: LimitJoint) -> None:
        ...
    def Connect(self, strName: str, item: AngularLimit) -> None:
        ...
    def Connect(self, strName: str, item: LinearLimit) -> None:
        ...
    def Connect(self, strName: str, item: SpringJoint) -> None:
        ...
    def Connect(self, strName: str, item: AngularSpring) -> None:
        ...
    def Connect(self, strName: str, item: LinearSpring) -> None:
        ...
    def Connect(self, strName: str, item: SpeedControl) -> None:
        ...
    def Connect(self, strName: str, item: PositionControl) -> None:
        ...
    def Connect(self, strName: str, item: ForceTorqueControl) -> None:
        ...
    def Connect(self, strName: str, item: AxisConstraint) -> None:
        ...
    def Connect(self, strName: str, item: SpringDamper) -> None:
        ...
    def Connect(self, strName: str, item: BreakingConstraint) -> None:
        ...
    def Connect(self, strName: str, item: GearCoupling) -> None:
        ...
    def Connect(self, strName: str, item: CamCoupling) -> None:
        ...
    def Connect(self, strName: str, item: ElecCamCoupling) -> None:
        ...
    def Connect(self, strName: str, item: PreventCollision) -> None:
        ...
    def Connect(self, strName: str, item: ChangeMaterial) -> None:
        ...
    def Connect(self, strName: str, item: SourceBehavior) -> None:
        ...
    def Connect(self, strName: str, item: SinkBehavior) -> None:
        ...
    def Connect(self, strName: str, item: Transformer) -> None:
        ...
    def Connect(self, strName: str, item: TransmitterEntry) -> None:
        ...
    def Connect(self, strName: str, item: TransmitterExit) -> None:
        ...
    def Connect(self, strName: str, item: GraphControl) -> None:
        ...
    def Connect(self, strName: str, item: ExternalConnection) -> None:
        ...
    def Connect(self, strName: str, item: SignalAdapter) -> None:
        ...
    def Connect(self, strName: str, item: Signal) -> None:
        ...
    def Connect(self, strName: str, item: MCDSignal) -> None:
        ...
    def Connect(self, strName: str, item: ProxyObject) -> None:
        ...
    def Connect(self, strName: str, item: RuntimeParameters) -> None:
        ...
    def Connect(self, strName: str, item: VirtualAxis) -> None:
        ...
    def Connect(self, strName: str, item: ReadWriteDeviceObject) -> None:
        ...
    def Connect(self, strName: str, item: DisplayChanger) -> None:
        ...
    def Connect(self, strName: str, item: Gripper) -> None:
        ...
    def Connect(self, strName: str, item: LinearGripper) -> None:
        ...
    def Connect(self, strName: str, item: AngularGripper) -> None:
        ...
    def Connect(self, strName: str, item: VacuumGripper) -> None:
        ...
    def Connect(self, strName: str, item: ExpressionBlock) -> None:
        ...
    def Connect(self, strName: str, item: PathConstraintJoint) -> None:
        ...
    def Connect(self, strName: str, item: TagForm) -> None:
        ...
    def Connect(self, strName: str, item: RuntimeNC) -> None:
        ...
    def Connect(self, strName: str, item: Operation) -> None:
        ...
    def Connect(self, strName: str, item: DistanceSensor) -> None:
        ...
    def Connect(self, strName: str, item: LaserScanner) -> None:
        ...
    def Connect(self, strName: str, item: LightCurtain) -> None:
        ...
    def Connect(self, strName: str, item: PositionSensor) -> None:
        ...
    def Connect(self, strName: str, item: VelocitySensor) -> None:
        ...
    def Connect(self, strName: str, item: GenericSensor) -> None:
        ...
    def Connect(self, strName: str, item: LimitSwitch) -> None:
        ...
    def Connect(self, strName: str, item: Relay) -> None:
        ...
    def Connect(self, strName: str, item: Inclinometer) -> None:
        ...
    def Connect(self, strName: str, item: Accelerometer) -> None:
        ...
    def Connect(self, strName: str, item: ScrewJoint) -> None:
        ...
    def Connect(self, strName: str, item: PlanarJoint) -> None:
        ...
    def Connect(self, strName: str, item: RackPinion) -> None:
        ...
    def Connect(self, strName: str, item: TableBase) -> None:
        ...
    def Connect(self, strName: str, item: PneumaticCylinder) -> None:
        ...
    def Connect(self, strName: str, item: PneumaticValve) -> None:
        ...
    def Connect(self, strName: str, item: HydraulicCylinder) -> None:
        ...
    def Connect(self, strName: str, item: HydraulicValve) -> None:
        ...
    def Connect(self, strName: str, item: InverseKinematics) -> None:
        ...
    def Connect(self, strName: str, item: BondZone) -> None:
        ...
    def Connect(self, strName: str, item: PulleysBeltChain) -> None:
        ...
    def Connect(self, strName: str, item: RuntimeButton) -> None:
        ...
    def Connect(self, strName: str, item: AlignBody) -> None:
        ...
    def Connect(self, strName: str, item: DynamicObjectInstantiation) -> None:
        ...
    def Connect(self, strName: str, item: Tracer) -> None:
        ...
    def Parameter(self, strName: str, value: int, item: int) -> None:
        ...
    def Parameter(self, strName: str, value: float, item: float) -> None:
        ...
    def Parameter(self, strName: str, value: bool, item: bool) -> None:
        ...


class ICurve():
    def GetDraftingCurveInfo(self) -> Drawings.DraftingCurveInfo:
        ...
    def IsDraftingCurve(self) -> bool:
        ...






class IBaseCurve():
    def GetLength(self) -> float:
        ...
    def GetLocations(self) -> typing.List[GeometricUtilities.CurveLocation]:
        ...
    IsReference: bool


class IAttributeSourceObjectBuilder():
    def AutoAssignAttributes(self, objects: typing.List[NXObject]) -> ErrorList:
        ...
    def AutoAssignAttributesWithNamingPattern(self, objects: typing.List[NXObject], properties: typing.List[NXObject]) -> ErrorList:
        ...
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: str, titlePatterns: str) -> NXObject:
        ...


class HyperbolaCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Hyperbola]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class Hyperbola(Conic):
    def __init__(self) -> None: ...
    MaximumDY: float
    MinimumDY: float
    SemiConjugateLength: float
    SemiTransverseLength: float


class HydraulicValve(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    SupplyPressure: float
    ExhaustPressure: float
    ControlIn: float
    Active: bool


    class HydraulicValve.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class HydraulicCylinder(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Axis: AxisJoint
    PressureA: float
    PressureB: float
    Active: bool


    class HydraulicCylinder.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class HumanReachZone(TaggedObject):
    def __init__(self) -> None: ...
    def SetData(self, zoneName: str, method: HumanReachZone.MethodType, waistFlexAngleData: float, waistFlexRangeLowerData: float, waistFlexRangeUpperData: float, waistLateralAngleData: float, waistLateralRangeLowerData: float, waistLateralRangeUpperData: float, traceSiteName: str, human: Features.Human, resolution: int, assocReachZone: bool) -> None:
        ...
    def GetData(self, zoneName: str, method: HumanReachZone.MethodType, waistFlexAngleData: float, waistFlexRangeLowerData: float, waistFlexRangeUpperData: float, waistLateralAngleData: float, waistLateralRangeLowerData: float, waistLateralRangeUpperData: float, traceSiteName: str, human: Features.Human, resolution: int, assocReachZone: bool) -> None:
        ...
    def ChangeName(self, reachZoneName: str) -> None:
        ...
    Geom: NXObject


    class MethodType(enum.Enum):
        ShoulderOnly = 0
        FlexWaist = 1
    

class HumanPosturePredictionBuilder(Builder):
    def __init__(self) -> None: ...
    def CreateCarCsys(self, carCsysOrigin: Point3d, carCsysMatrix: Matrix3x3) -> None:
        ...
    def GetSgrpPoint(self) -> Point:
        ...
    def SetSgrpPoint(self, sgrpPoint: Point) -> None:
        ...
    def GetSgrpCoordinates(self, pointX: str, pointY: str, pointZ: str) -> None:
        ...
    def SetSgrpCoordinates(self, pointX: str, pointY: str, pointZ: str) -> None:
        ...
    def GetAhpPoint(self) -> Point:
        ...
    def SetAhpPoint(self, ahpPoint: Point) -> None:
        ...
    def GetAhpCoordinates(self, pointX: str, pointY: str, pointZ: str) -> None:
        ...
    def SetAhpCoordinates(self, pointX: str, pointY: str, pointZ: str) -> None:
        ...
    def GetHandFootDataType(self, handFoot: HumanData.HandFootType, side: HumanData.SideType) -> HumanPosturePredictionBuilder.SteeringWheelPedalType:
        ...
    def SetHandFootDataType(self, handFoot: HumanData.HandFootType, side: HumanData.SideType, steeringWheelPedalType: HumanPosturePredictionBuilder.SteeringWheelPedalType) -> None:
        ...
    def GetHandFootDataSolids(self, handFoot: HumanData.HandFootType, side: HumanData.SideType) -> typing.List[Body]:
        ...
    def SetHandFootDataSolids(self, handFoot: HumanData.HandFootType, side: HumanData.SideType, solids: typing.List[Body]) -> None:
        ...
    def GetHandFootDataCurves(self, handFoot: HumanData.HandFootType, side: HumanData.SideType) -> typing.List[NXObject]:
        ...
    def SetHandFootDataCurves(self, handFoot: HumanData.HandFootType, side: HumanData.SideType, curves: typing.List[NXObject]) -> None:
        ...
    def GetHandDataSae(self, side: HumanData.SideType, l11: str, h17: str, w9: str, a18: str) -> None:
        ...
    def SetHandDataSae(self, side: HumanData.SideType, l11: str, h17: str, w9: str, a18: str) -> None:
        ...
    def GetFootDataSae(self, side: HumanData.SideType) -> str:
        ...
    def SetFootDataSae(self, side: HumanData.SideType, pedalAngle: str) -> None:
        ...
    def GetHandFootCsys(self, handFoot: HumanData.HandFootType, side: HumanData.SideType, position: Point3d, orientation: Matrix3x3) -> None:
        ...
    def SetHandFootCsys(self, handFoot: HumanData.HandFootType, side: HumanData.SideType, position: Point3d, orientation: Matrix3x3) -> None:
        ...
    def ComputeHandCsys(self, leftHandPosition: Point3d, leftHandOrientation: Matrix3x3, rightHandPosition: Point3d, rightHandOrientation: Matrix3x3) -> None:
        ...
    def ComputeFootCsys(self, side: HumanData.SideType, position: Point3d, orientation: Matrix3x3) -> None:
        ...
    def GetPassengerHfUseDefaults(self, leftHand: int, rightHand: int, leftFoot: int, rightFoot: int) -> None:
        ...
    def SetPassengerHfUseDefaults(self, leftHand: int, rightHand: int, leftFoot: int, rightFoot: int) -> None:
        ...
    def GetPassengerHfMirror(self, leftHand: int, rightHand: int, leftFoot: int, rightFoot: int, dummy: int) -> None:
        ...
    def SetPassengerHfMirror(self, leftHand: int, rightHand: int, leftFoot: int, rightFoot: int, dummy: int) -> None:
        ...
    Age: int
    BackAngleA40: str
    CarCsys: CoordinateSystem
    CushionAngleA27: str
    CushionFirmness: HumanPosturePredictionBuilder.CushionFirmnessType
    Garb: HumanPosturePredictionBuilder.GarbType
    Human: Features.Human
    LumbarProminenceL81: str
    Name: str
    Occupant: HumanPosturePredictionBuilder.OccupantType
    PassengerDirection: int
    PassengerDirectionAngle: str
    PredictionMethod: HumanPosturePredictionBuilder.PredictionMethodType
    Seat: HumanPosturePredictionBuilder.SeatType
    SeatTrackAngleA19: str
    ShowReport: bool
    TrackLowerLimitHeightTH1: str
    TrackLowerLimitLengthTL1: str
    TrackUpperLimitHeightTH2: str
    TrackUpperLimitLengthTL23: str
    Transmission: HumanPosturePredictionBuilder.TransmissionType
    UseStl: bool
    UseVehiclePackagingData: bool
    VdaOccupant: int
    VdaVehicle: int
    Vehicle: HumanPosturePredictionBuilder.VehicleType
    VehiclePackagingDataName: str


    class VehicleType(enum.Enum):
        ClassA = 0
        ClassB = 1
        ClassSeatedSoldier = 2
    

    class TransmissionType(enum.Enum):
        Automatic = 0
        Manual = 1
    

    class SteeringWheelPedalType(enum.Enum):
        Solid = 0
        Curve = 1
        Sae = 2
        Csys = 3
    

    class SeatType(enum.Enum):
        Fixed = 0
        Adjustable = 1
    

    class PredictionMethodType(enum.Enum):
        Aspect = 0
        PreAspect = 1
    

    class OccupantType(enum.Enum):
        Driver = 0
        FrontPassenger = 1
        RearPassenger = 2
    

    class GarbType(enum.Enum):
        AdvCombatUniform = 0
        PersonalProtectiveEquip = 1
        Encumbrance = 2
    

    class CushionFirmnessType(enum.Enum):
        Soft = 0
        Medium = 1
        Firm = 2
    

class HumanPosturePrediction(TaggedObject):
    def __init__(self) -> None: ...


class HumanHandShapeData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    HandType: HumanHandShapeData.HandOpt
    HandshapeName: str
    HandshapeValue: float


    class HandOpt(enum.Enum):
        Left = 0
        Right = 1
        Both = 2
    

class HumanHandsDialogBuilder(Builder):
    def __init__(self) -> None: ...
    def UpdateHandPropsButton(self) -> None:
        ...
    def JointDialogButton(self) -> None:
        ...
    def SetHumanFeatureBuilder(self, humanfeaturebuilder: Features.HumanBuilder) -> None:
        ...
    Aperture: float
    BreadthPercentile: HumanHandsDialogBuilder.BreadthType
    BreadthValue: float
    Database: HumanHandsDialogBuilder.DatabaseType
    Gender: HumanHandsDialogBuilder.GenderType
    GloveThickness: float
    IncludeForearm: bool
    LengthPercentile: HumanHandsDialogBuilder.LengthType
    LengthValue: float
    ShapeName: str
    Side: HumanHandsDialogBuilder.HandType
    Style: HumanHandsDialogBuilder.StyleType


    class StyleType(enum.Enum):
        Gloves = 0
        BareHands = 1
    

    class LengthType(enum.Enum):
        P5 = 0
        P25 = 1
        P50 = 2
        P75 = 3
        P95 = 4
    

    class HandType(enum.Enum):
        Right = 0
        Left = 1
    

    class GenderType(enum.Enum):
        Male = 0
        Female = 1
    

    class DatabaseType(enum.Enum):
        Ansur = 0
        Ansur2 = 1
        Nhanes = 2
        Nhanes2014 = 3
    

    class BreadthType(enum.Enum):
        P5 = 0
        P25 = 1
        P50 = 2
        P75 = 3
        P95 = 4
    

class HumanH10DialogBuilder(Builder):
    def __init__(self) -> None: ...
    def SetHumanFeatureBuilder(self, humanfeaturebuilder: Features.HumanBuilder) -> None:
        ...
    AgeInput: int
    AssociateCheck: bool
    AssociatePoint: Point
    ChestCircumference: float
    Database: HumanH10DialogBuilder.DatabaseType
    ElbowToWrist: float
    FootBreadth: float
    FootLength: float
    Gender: HumanH10DialogBuilder.GenderType
    HandBreadth: float
    HandDepth: float
    HandLength: float
    HeightPercentile: HumanH10DialogBuilder.HeightInputType
    HeightUnits: HumanH10DialogBuilder.HeightUnitsEnum
    HeightValue: float
    HipMeasure: HumanH10DialogBuilder.HipMeasureType
    HipValue: float
    KneeHeight: float
    Name: str
    RefPoint: HumanH10DialogBuilder.RefPointType
    ShoeSoleHeight: float
    ShoulderMeasureBlock: HumanH10DialogBuilder.ShoulderMeasureType
    ShoulderValue: float
    SittingHeight: float
    WaistCircumference: float
    WeightPercentile: HumanH10DialogBuilder.WeightInputType
    WeightUnits: HumanH10DialogBuilder.WeightUnitsEnum
    WeightValue: float


    class WeightUnitsEnum(enum.Enum):
        Kg = 0
        Lbs = 1
    

    class WeightInputType(enum.Enum):
        Custom = 0
        Predictfromheight = 1
    

    class ShoulderMeasureType(enum.Enum):
        BiacromialBreadth = 0
        BideltoidBreadth = 1
    

    class RefPointType(enum.Enum):
        Leftfoot = 0
        Rightfoot = 1
    

    class HipMeasureType(enum.Enum):
        HipBreadth = 0
        HipCircumference = 1
    

    class HeightUnitsEnum(enum.Enum):
        In = 0
    

    class HeightInputType(enum.Enum):
        Custom = 0
        Predictfromweight = 1
    

    class GenderType(enum.Enum):
        Male = 0
        Female = 1
    

    class DatabaseType(enum.Enum):
        Ansur = 0
        Ansur2 = 1
        Nhanes = 2
        Nhanes2014 = 3
    

class HumanData(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetXform(self, orientation: Matrix3x3, position: Point3d) -> None:
        ...
    AssocReferencePoint: bool
    FigureFile: str
    Gender: HumanData.GenderType
    Name: str
    ReferencePoint: NXObject
    ReferencePointLocationType: HumanData.ReferencePointType
    StatureOption: HumanData.StatureType
    StatureValue: float
    WeightOption: HumanData.WeightType
    WeightValue: float


    class WeightUnitType(enum.Enum):
        Lb = 0
        Kg = 1
    

    class WeightType(enum.Enum):
        Percentile99 = 0
        Percentile95 = 1
        Percentile50 = 2
        Percentile5 = 3
        Percentile1 = 4
        Custom = 5
        Regress = 6
    

    class StatureUnitType(enum.Enum):
        Inch = 0
        Mm = 1
        Cm = 2
        M = 3
    

    class StatureType(enum.Enum):
        Percentile99 = 0
        Percentile95 = 1
        Percentile50 = 2
        Percentile5 = 3
        Percentile1 = 4
        Custom = 5
        Regress = 6
    

    class SideType(enum.Enum):
        Left = 0
        Right = 1
        Center = 2
    

    class SegmentScalingType(enum.Enum):
        Head = 0
        Neck = 1
        Torso = 2
        UpperArm = 3
        LowerArm = 4
        Hand = 5
        LowerTorso = 6
        UpperLeg = 7
        LowerLeg = 8
        Foot = 9
    

    class ReferencePointType(enum.Enum):
        No = 0
        LeftEye = 1
        RightEye = 2
        HPoint = 3
        LeftToe = 4
        RightToe = 5
        NumberReferences = 6
    

    class JointType(enum.Enum):
        BaseOfNeck = 0
        LeftShoulder = 1
        RightShoulder = 2
        Torso = 3
        LeftElbow = 4
        RightElbow = 5
        LeftWrist = 6
        RightWrist = 7
        Lthumb0 = 8
        Lthumb1 = 9
        Lthumb2 = 10
        LeftFinger00 = 11
        Linfinger01 = 12
        Linfinger02 = 13
        LeftFinger10 = 14
        Lmidfinger11 = 15
        Lmidfinger12 = 16
        LeftFinger20 = 17
        Lringfinger21 = 18
        Lringfinger22 = 19
        LeftFinger30 = 20
        Lpinfinger31 = 21
        Lpinfinger32 = 22
        Rthumb0 = 23
        Rthumb1 = 24
        Rthumb2 = 25
        RightFinger00 = 26
        Rinfinger01 = 27
        Rinfinger02 = 28
        RightFinger10 = 29
        Rmidfinger11 = 30
        Rmidfinger12 = 31
        RightFinger20 = 32
        Rringfinger21 = 33
        Rringfinger22 = 34
        RightFinger30 = 35
        Rpinfinger31 = 36
        Rpinfinger32 = 37
        Waist = 38
        LeftHip = 39
        RightHip = 40
        LeftKnee = 41
        RightKnee = 42
        LeftAnkle = 43
        RightAnkle = 44
        LeftToes = 45
        RightToes = 46
    

    class InverseKinematicsType(enum.Enum):
        DynamicDrag = 0
        ActiveReach = 1
    

    class InverseKinematicsInitJoint(enum.Enum):
        Shoulder = 0
        Waist = 1
    

    class InverseKinematicsHeadEyeType(enum.Enum):
        FollowLastDefined = 0
        Fixate = 1
    

    class InverseKinematicsBodyParts(enum.Enum):
        Head = 0
        Eyes = 1
        LeftHand = 2
        RightHand = 3
        LeftElbow = 4
        RightElbow = 5
        LeftKnee = 6
        RightKnee = 7
        LeftFoot = 8
        RightFoot = 9
        CenterOfMass = 10
    

    class InverseKinematicsBalanceType(enum.Enum):
        AllowStep = 0
        NoStep = 1
        KeepSeated = 2
    

    class HandGoalType(enum.Enum):
        GoalPoint = 0
        GoalCsys = 1
        HandFigure = 2
    

    class HandFootType(enum.Enum):
        Hand = 0
        Foot = 1
    

    class GenderType(enum.Enum):
        Male = 0
        Female = 1
    

    class EditDisplayBodyParts(enum.Enum):
        LeftEyePoint = 0
        RightEyePoint = 1
        MidEyePoint = 2
        HipPoint = 3
        LeftToePoint = 4
        RightToePoint = 5
        LeftHeelPoint = 6
        RightHeelPoint = 7
        CenterOfMass = 8
        All = 9
    

    class DatabaseType(enum.Enum):
        None = 0
        ANSUR = 1
        NHANES = 2
    

    class AppearanceType(enum.Enum):
        Segmented = 0
        Base = 1
        Clothed = 2
    

    class AdvancedScalingType(enum.Enum):
        AbdominalDepth = 0
        AcromionHeight = 1
        AnkleHeight = 2
        ArmLength = 3
        BiacromialBreadth = 4
        BideltoidBreadth = 5
        ButtockKneeLength = 6
        ElbowFingertipLength = 7
        ElbowRestHeight = 8
        FootBreadth = 9
        FootLength = 10
        HandBreadth = 11
        HandLength = 12
        HeadBreadth = 13
        HeadHeight = 14
        HeadLength = 15
        HipBreadth = 16
        InterpupilDistance = 17
        ShoulderElbowLength = 18
        SittingAcromialHeight = 19
        SittingEyeHeight = 20
        SittingHeight = 21
        SittingKneeHeight = 22
        ThighClearance = 23
        ThumbtipReach = 24
    

class HingeJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    def GetVelocity(self) -> float:
        ...
    Attach: RigidBody
    Base: RigidBody
    Anchor: VectorArithmetic.Vector3
    Axis: VectorArithmetic.Vector3
    Angle: float
    Active: bool


    class HingeJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class GroupBuilder(Builder):
    def __init__(self) -> None: ...
    ActionType: int
    ActivegroupOption: bool
    AttributeHolder: TaggedObject
    GroupDisplayProperties: bool
    GroupInAction: SelectGroup
    GroupName: str
    ObjectsInGroup: SelectObjectList
    OwningObject: NXObject
    SketchGroupType: GroupBuilder.SketchType
    UngroupLevel: GroupBuilder.UngroupOption
    UniqueMembershipOption: bool


    class UngroupOption(enum.Enum):
        Top = 0
        Full = 1
    

    class SketchType(enum.Enum):
        Regular = 0
        Unique = 1
        Rigid = 2
        Scalable = 3
    

    class Action(enum.Enum):
        NewGroup = 0
        AddToGroup = 1
        RemoveFromGroup = 2
        Ungroup = 3
        EditGroup = 4
        NewSketchGroup = 5
    

class Group(DisplayableObject):
    def __init__(self) -> None: ...
    def SetGroupActive(self, active: bool) -> None:
        ...


class Gripper(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...


class GraphControl(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    AxisControl: ControlBase
    InitialTime: float
    ValueOffset: float
    MasterScale: float
    SlaveScale: float
    TableObj: TableBase


    class GraphControl.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class GenericSensor(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Signal: float
    Active: bool


    class GenericSensor.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class GenericMeasure(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def Information(self) -> None:
        ...
    MeasurementType: GenericMeasure.Type


    class Type(enum.Enum):
        MinimumDistance = 0
        LocalMinimumDistance = 1
        MaximumDistance = 2
        ProjectedDistance = 3
        RadialDistance = 4
        Length = 5
        TwoObjectAngle = 6
        ThreePointAngle = 7
        FaceProperties = 8
        MassProperties = 9
        PointsOnCurves = 10
        RoutingPathLength = 11
        DiameterDistance = 12
        PolarRadius = 13
        PolarAngle = 14
        RectangularExtreme = 15
        PolarArea = 16
        ExtremePoint = 17
        MinimumSmartDistance = 18
        MaximumSmartDistance = 19
        Point = 20
    

class GeneralScalarTable(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetTableSize(self, nRows: int, nCols: int, dDefaultValue: float) -> None:
        ...
    def SetNumberOfRows(self, nRows: int, dDefaultValue: float) -> None:
        ...
    def GetCellValue(self, iRow: int, iCol: int) -> float:
        ...
    def SetCellValue(self, iRow: int, iCol: int, cellValue: float) -> None:
        ...
    def SetCellValue(self, iRow: int, iCol: int, cellValue: int) -> None:
        ...
    def SetCellNoValue(self, iRow: int, iCol: int) -> None:
        ...
    def SetNthRow(self, iRow: int, rowValues: float) -> None:
        ...
    def GetNthRow(self, iRow: int) -> float:
        ...
    def SetNthColumn(self, iCol: int, columnValues: float) -> None:
        ...
    def GetNthColumn(self, iCol: int) -> float:
        ...
    def SetNthColumnUnits(self, iCol: int, unitType: Unit) -> None:
        ...
    def GetNthColumnUnits(self, iCol: int) -> Unit:
        ...
    def FreeResource(self) -> None:
        ...
    NumCols: int
    NumRows: int


class GearCoupling(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetMasterForce(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetMasterForce(self) -> VectorArithmetic.Vector3:
        ...
    def GetMasterTorque(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetMasterTorque(self) -> VectorArithmetic.Vector3:
        ...
    def GetSlaveForce(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetSlaveForce(self) -> VectorArithmetic.Vector3:
        ...
    def GetSlaveTorque(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetSlaveTorque(self) -> VectorArithmetic.Vector3:
        ...
    MasterAxis: AxisJoint
    SlaveAxis: AxisJoint
    MasterMultiple: float
    SlaveMultiple: float
    AllowSlip: bool
    Active: bool


    class GearCoupling.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class FourPointSurfaceBuilder(Builder):
    def __init__(self) -> None: ...
    Point1: Point
    Point2: Point
    Point3: Point
    Point4: Point


class ForceTorqueControl(ControlBase):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Axis: AxisJoint
    Speed: float
    Position: float
    Force: float


    class ForceTorqueControl.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class FontCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def AddFont(self, fontName: str) -> int:
        ...
    def GetFontName(self, fontIndex: int) -> str:
        ...
    def DoesFontExist(self, fontIndex: int) -> bool:
        ...
    def GetLength(self) -> int:
        ...
    def AddFont(self, fontName: str, type: FontCollection.Type) -> int:
        ...
    def ReplaceFont(self, fontIndex: int, type: FontCollection.Type, fontName: str) -> None:
        ...
    def GetFontType(self, fontIndex: int) -> FontCollection.Type:
        ...
    def Tag(self) -> Tag: ...



    class Type(enum.Enum):
        Nx = 0
        Standard = 1
        Empty = 10
    

class FollowFilletRuleType(enum.Enum):
    Connected = 0
    Tangent = 1


class FollowFilletRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature], bodies: typing.List[Body], basicCurves: typing.List[ICurve], seedWireframe: ICurve, endWireframe: ICurve, fromSeedStart: bool, gapTolerance: float, angleTolerance: float, method: FollowFilletRuleType) -> None:
        ...


class FloodFillFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seedFacet: IFacet, isDeselectionRule: bool) -> None:
        ...


class FixedJoint(Joint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    Active: bool


    class FixedJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class FineBrushFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, fineBrushToolStartPoint: Point3d, fineBrushToolDirection: Vector3d, fineBrushToolRadius: float, seedFacet: IFacet) -> None:
        ...


class FillBoundaryRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class FileNewTemplateType(enum.Enum):
    Workset = 0
    Item = 1
    DesignElement = 2
    DesignControlElement = 3
    DesignFeature = 4
    Generic = 5
    Sheet = 6
    DiagrammingSheetpart = 7
    DesignWorkset = 8
    Last = 9


class FileNewTemplate(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def IsBlank(self) -> bool:
        ...
    def GetName(self) -> str:
        ...
    def GetUnits(self) -> Part.Units:
        ...
    def FreeResource(self) -> None:
        ...


class FileNewApplication(enum.Enum):
    Drafting = 0
    Modeling = 1
    Studio = 2
    Assemblies = 3
    Gateway = 4
    RoutingElectrical = 5
    RoutingMechanical = 6
    RoutingLogical = 7
    Nxsheetmetal = 8
    SheetTemplate = 9
    CaeFem = 10
    CaeSim = 11
    AeroSheetmetal = 12
    FlexPcdSheetmetal = 13
    CaeAssyFem = 14
    Cam = 15
    Inspection = 16
    Mechatronics = 17
    ShipContainer = 18
    ShipDetail = 19
    ShipReference = 20
    ShipSystem = 21
    Welding = 22
    WeldingJoint = 23
    Nxle = 24
    ShipGaAssembly = 25
    ShipGaSystem = 26
    AecSystem = 27
    Last = 28


class FileNew(Builder):
    def __init__(self) -> None: ...
    def GetAvailableTemplates(self) -> str:
        ...
    def SetProjectsData(self, projectName: str, assignmentState: int) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.Session.AssignRemoveProjects to assign/remove projects.")"""
        ...
    def GetAddMasterFlag(self) -> bool:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.PDM.PartOperationCreateBuilder.GetAddMaster to get addMaster flag.")"""
        ...
    def SetAddMasterFlag(self, addMaster: bool) -> None:
        """[Obsolete("Deprecated in NX10.0.0.  Use NXOpen.PDM.PartOperationCreateBuilder.SetAddMaster to set addMaster flag.")"""
        ...
    def GetApplicationNames(self) -> str:
        ...
    def SetPartOperationCreateBuilder(self, partOperationBuilder: PDM.PartOperationBuilder) -> None:
        ...
    def SetCanCreateAltrep(self, createAltrep: bool) -> None:
        ...
    def GetCanCreateAltrep(self) -> bool:
        ...
    def GetTemplates(self) -> typing.List[FileNewTemplate]:
        ...
    def SetCloudDMNewPartBuilder(self, cloudDMNewPartBuilder: CloudDM.NewPartBuilder) -> None:
        ...
    def AllowTemplatePostPartCreationAction(self, allowTemplatePostPartCreationAction: bool) -> None:
        ...
    Application: FileNewApplication
    ApplicationName: str
    DesignElementState: str
    DesignElementType: str
    DisplayPartOption: DisplayPartOption
    ItemType: str
    MakeDisplayedPart: bool
    MasterFileName: str
    NewFileName: str
    RelationType: str
    Specialization: str
    TemplateFileName: str
    TemplatePresentationName: str
    TemplateType: FileNewTemplateType
    Units: Part.Units
    UseBlankTemplate: bool
    UsesMasterModel: str


class FeatureProcessBuilderStatus(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetResultStatus(self) -> FeatureProcessBuilderStatus.ResultStatus:
        ...
    def SetResultStatus(self, result: FeatureProcessBuilderStatus.ResultStatus) -> None:
        ...


    class ResultStatus(enum.Enum):
        NoError = 0
        OperationNotAllocated = 1
        NoOperationsCreated = 2
    

class FeaturePointsRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature]) -> None:
        ...


class FeatureIntersectionEdgesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[NXObject]) -> None:
        ...


class FeatureGeneralPropertiesBuilder(Builder):
    def __init__(self) -> None: ...
    def DeleteGeneralName(self) -> None:
        ...
    def DeleteFeatureName(self) -> None:
        ...
    def GetNameLocation(self) -> Point3d:
        ...
    def SetNameLocation(self, nameLocation: Point3d) -> None:
        ...
    ApplyToWorkPart: bool
    FeatureName: str
    FeatureObject: NXObject
    GeneralName: str
    GeneralObject: NXObject
    NameLocationSpecified: bool
    SelectedObjects: SelectNXObjectList


class FacetSelectionRuleFactory(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateRuleSingleFacet(self, facets: typing.List[IFacet]) -> SingleFacetRule:
        ...
    def CreateRuleFaceFacets(self, faces: typing.List[NXObject]) -> FaceFacetsRule:
        ...
    def CreateRuleFloodFillFacets(self, seedFacet: IFacet, isDeselectionRule: bool) -> FloodFillFacetsRule:
        ...
    def CreateRuleRoughBrushFacets(self, brushToolStartPoint: Point3d, brushToolDirection: Vector3d, brushToolRadius: float, allowHiddenFacetsSel: bool, seedFacet: IFacet) -> RoughBrushFacetsRule:
        ...
    def CreateRuleFineBrushFacets(self, brushToolStartPoint: Point3d, brushToolDirection: Vector3d, brushToolRadius: float, allowHiddenFacetsSel: bool, seedFacet: IFacet) -> FineBrushFacetsRule:
        ...
    def CreateRuleColorRegionFacets(self, seedFacet: IFacet) -> ColorRegionRule:
        ...
    def CreateRuleFillBoundary(self, boundaryFacets: typing.List[IFacet], seedFacet: IFacet, includeBoudaryFacets: bool) -> FillBoundaryRule:
        ...
    def CreateRuleFillBoundary(self, boundaryFacets: typing.List[IFacet], seedFacets: typing.List[IFacet], includeBoudaryFacets: bool) -> FillBoundaryRule:
        ...
    def CreateRuleBodyFacets(self, bodies: typing.List[NXObject]) -> BodyFacetsRule:
        ...
    def CreateRulePrimitiveFacets(self, seedFacet: IFacet, primitiveShapeToleranceFactor: float) -> PrimitiveFacetsRule:
        ...
    def CreateRuleTangentFacets(self, seedFacet: IFacet, tangencyTolerance: float) -> TangentFacetsRule:
        ...
    def CreateRuleWithinCurves(self, seedFacet: IFacet) -> WithinCurvesRule:
        ...
    def Tag(self) -> Tag: ...



class FacetSelectionRule(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class FacetCollectorCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[FacetCollector]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateCollector(self) -> FacetCollector:
        ...
    def Tag(self) -> Tag: ...



class FacetCollector(NXObject):
    def __init__(self) -> None: ...
    def AddRules(self, rules: typing.List[FacetSelectionRule]) -> None:
        ...
    def RemoveRules(self, rules: typing.List[FacetSelectionRule]) -> None:
        ...
    def Destroy(self) -> None:
        ...
    def RemoveAllFacets(self) -> None:
        ...
    def GetFacets(self) -> typing.List[IFacet]:
        ...


class FaceTangentRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, startFace: Face, endFace: Face, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  This functionality is no longer supported.")"""
        ...


class FaceSlotFacesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> Face:
        ...
    def GetDefiningData(self, includeBoundaryBlends: bool, traverseInteriorLoops: bool) -> Face:
        ...


class FaceRibFacesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> Face:
        ...
    def GetDefiningData(self, includeBoundaryBlends: bool, travserseInteriorLoops: bool) -> Face:
        ...


class FaceRegionRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, boundaryFaces: typing.List[Face]) -> None:
        """[Obsolete("Deprecated in NX8.0.0.  This functionality is no longer supported.")"""
        ...


class FaceRegionBoundaryRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seedObj: Face, curves: typing.List[Curve], seedPoint: Point3d, distanceTolerance: float) -> None:
        ...


class FaceMergedRibFacesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, face: Face, edge: Edge) -> None:
        ...
    def GetDefiningData(self, edge: Edge, includeBoundaryBlends: bool) -> Face:
        ...
    def GetSeedAndPointData(self, face: Face, seedPt: Point3d) -> None:
        ...


class FaceHoleFacesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> Face:
        ...


class FaceFeatureRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature]) -> None:
        ...


class FaceFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, faces: typing.List[NXObject]) -> None:
        ...


class FaceDumbRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, faces: typing.List[Face]) -> None:
        ...


class FaceConnectedBlendRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> Face:
        ...
    def GetDefiningData(self, seedFace: Face, includeBlendLike: bool, includeUnlabeledBlend: bool, feature: Features.Feature) -> None:
        ...


class FaceBossPocketFacesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> Face:
        ...
    def GetDefiningData(self, includeBoundaryBlends: bool) -> Face:
        ...


class FaceBodyRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetBodyData(self) -> Body:
        ...


class FaceAndAdjacentFacesRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, faces: typing.List[Face]) -> None:
        ...


class FaceAllBlendRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> Body:
        ...
    def GetDefiningData(self, body: Body, feature: Features.Feature) -> None:
        ...


class FaceAdjacentRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, faces: typing.List[Face]) -> None:
        ...


class Face(DisplayableObject):
    def __init__(self) -> None: ...
    def GetEdges(self) -> typing.List[Edge]:
        ...
    def GetUnsortedEdges(self) -> typing.List[Edge]:
        ...
    def GetBody(self) -> Body:
        ...
    def GetNumberOfFacets(self) -> int:
        ...
    def GetNumberOfVertices(self) -> int:
        ...
    def GetNextFacet(self, inputFacet: ConvergentFacet) -> ConvergentFacet:
        ...
    def GetFirstFacetOnFace(self) -> ConvergentFacet:
        ...
    def DestroyOwnedFacets(self) -> None:
        ...
    def GetChamferData(self, chamferType: Face.ChamferType, offsets: float) -> bool:
        ...
    def GetBlendData(self, radius: float, isBlendFace: bool) -> None:
        ...
    SolidFaceType: Face.FaceType


    class FaceType(enum.Enum):
        Rubber = 0
        Planar = 1
        Cylindrical = 2
        Conical = 3
        Spherical = 4
        SurfaceOfRevolution = 5
        Parametric = 6
        Blending = 7
        Offset = 8
        Swept = 9
        Convergent = 10
        Undefined = 11
    

    class ChamferType(enum.Enum):
        OffsetOffset = 0
        OffsetAngle = 1
        Vertex = 2
        Undefined = 3
    

class ExtrudeTaperDataTaperType(enum.Enum):
    None = 0
    SimpleFromStart = 1
    SimpleFromProfile = 2
    Symmetric = 3
    MatchedEnds = 4
    Asymmetric = 5


class ExtrudeOffsetDataOffsetType(enum.Enum):
    None = 0
    NormalOffset = 1
    SymmetricOffset = 2
    SingleOffset = 3


class ExtrudeLimitDataLimitType(enum.Enum):
    Distance = 0
    UntilNext = 1
    UntilSelected = 2
    UntilSelectedExtendFace = 3
    ThroughAll = 4


class ExternalFileReferenceManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def GetExternalFileReferences(self, extRefs: typing.List[ExternalFileReference]) -> None:
        ...
    def Tag(self) -> Tag: ...



class ExternalFileReferenceAdapter(TaggedObject):
    def __init__(self) -> None: ...
    def EstablishReference(self, referenceType: ExternalFileReferenceAdapter.Type, externalFileSpec: str) -> None:
        ...
    def GetFileSpec(self) -> str:
        ...
    def SetExternalFileDefinitionKey(self, externalFileDefkey: str) -> None:
        ...
    def SetCandidateForSave(self, doSave: bool) -> None:
        ...
    def SetAssociatedFileReference(self) -> None:
        ...


    class Type(enum.Enum):
        Native = 0
        Part = 1
        ImanFile = 2
        DatabaseObject = 3
    

class ExternalFileReference(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetExternalFileSpec(self) -> str:
        ...
    def GetExternalFileName(self) -> str:
        ...
    def GetReferencingApplicationObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    def GetTimeStampWithStatus(self, status: ExternalFileReference.Status) -> str:
        ...


    class Status(enum.Enum):
        Ok = 0
        FileMoved = 1
        FileOutOfDate = 2
        FileNotFound = 3
        Invalid = 4
    

class ExternalConnection(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Target: RuntimeObject


    class ExternalConnection.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class ExtendedRealityFileCreator(Builder):
    def __init__(self) -> None: ...
    BodiesToExport: SelectDisplayableObjectList
    CsysOfexportPosition: CoordinateSystem
    DataCompression: bool
    ExportAppearanceSchemes: bool
    ExportAssemblyArrangements: bool
    ExportAssemblyExplosions: bool
    ExportCameras: bool
    ExportEntity: ExtendedRealityFileCreator.ObjectToExport
    ExportMotionAnimation: bool
    ExportPositionType: ExtendedRealityFileCreator.ExportedPositionCSYS
    FileLocation: str
    Format: ExtendedRealityFileCreator.OutputFormat


    class OutputFormat(enum.Enum):
        Gltf = 0
        Glb = 1
        Usdz = 2
    

    class ObjectToExport(enum.Enum):
        EntirePart = 0
        SelectedObjects = 1
    

    class ExportedPositionCSYS(enum.Enum):
        Absolute = 0
        Wcs = 1
        UserDefined = 2
    

class ExpressionSectionSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[ExpressionSectionSet]) -> None:
        ...
    def Append(self, object: ExpressionSectionSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: ExpressionSectionSet) -> int:
        ...
    def FindItem(self, index: int) -> ExpressionSectionSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: ExpressionSectionSet) -> None:
        ...
    def Erase(self, obj: ExpressionSectionSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[ExpressionSectionSet]:
        ...
    def SetContents(self, objects: typing.List[ExpressionSectionSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: ExpressionSectionSet, object2: ExpressionSectionSet) -> None:
        ...
    def Insert(self, location: int, object: ExpressionSectionSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ExpressionSectionSet(NXObject):
    def __init__(self) -> None: ...
    ItemFlipFlag: bool
    ItemIndex: int
    ItemValue: Expression
    Section: Section


class ExpressionGroupCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[ExpressionGroup]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, name: str) -> ExpressionGroup:
        ...
    def Rename(self, expressionGroup: ExpressionGroup, newName: str) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> ExpressionGroup:
        ...
    def Delete(self, expressionGroup: typing.List[ExpressionGroup]) -> None:
        ...
    def GetGroupOfExpression(self, expression: Expression) -> ExpressionGroup:
        ...
    def SetAllGroupsVisible(self) -> None:
        ...
    def GetDefault(self) -> ExpressionGroup:
        ...
    def GetAllExpressionGroupsInPart(self) -> typing.List[ExpressionGroup]:
        ...
    def CheckName(self, name: str) -> bool:
        ...
    def ExportExpressionGroupsToFile(self, expressionGroups: typing.List[ExpressionGroup], fileName: str, sortType: ExpressionCollection.SortType) -> None:
        ...
    def Tag(self) -> Tag: ...

    Active: ExpressionGroup


class ExpressionGroup(NXObject):
    def __init__(self) -> None: ...
    def GetMemberGroups(self) -> typing.List[ExpressionGroup]:
        ...
    def GetExpressions(self) -> typing.List[Expression]:
        ...
    def SetExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    def RemoveExpressions(self, expressions: typing.List[Expression]) -> None:
        ...
    Parent: ExpressionGroup
    Visibility: bool


class ExpressionCollectorSetList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[ExpressionCollectorSet]) -> None:
        ...
    def Append(self, object: ExpressionCollectorSet) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: ExpressionCollectorSet) -> int:
        ...
    def FindItem(self, index: int) -> ExpressionCollectorSet:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: ExpressionCollectorSet) -> None:
        ...
    def Erase(self, obj: ExpressionCollectorSet, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[ExpressionCollectorSet]:
        ...
    def SetContents(self, objects: typing.List[ExpressionCollectorSet]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: ExpressionCollectorSet, object2: ExpressionCollectorSet) -> None:
        ...
    def Insert(self, location: int, object: ExpressionCollectorSet) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class ExpressionCollectorSet(NXObject):
    def __init__(self) -> None: ...
    Collector: ScCollector
    ItemFlipFlag: bool
    ItemIndex: int
    ItemValue: Expression


class ExpressionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Expression]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Create(self, expressionString: str) -> Expression:
        ...
    def CreateWithUnits(self, expressionString: str, unitType: Unit) -> Expression:
        ...
    def CreateNumberExpression(self, expressionString: str, unitType: Unit) -> Expression:
        ...
    def CreateSystemExpression(self, expressionString: str) -> Expression:
        ...
    def CreateSystemExpressionWithUnits(self, expressionString: str, unitType: Unit) -> Expression:
        ...
    def CreateSystemNumberExpression(self, expressionString: str, unitType: Unit) -> Expression:
        ...
    def CreateExpression(self, expressionType: str, expressionString: str) -> Expression:
        ...
    def CreateSystemExpression(self, expressionType: str, expressionString: str) -> Expression:
        ...
    def Edit(self, expression: Expression, newFormula: str) -> None:
        ...
    def EditWithUnits(self, expression: Expression, unitType: Unit, newFormula: str) -> None:
        ...
    def EditExpression(self, expression: Expression, newFormula: str) -> None:
        ...
    def EditExpressionWithUnits(self, expression: Expression, unitType: Unit, newFormula: str) -> None:
        ...
    def Delete(self, expression: Expression) -> None:
        ...
    def FindObject(self, journalIdentifier: str) -> Expression:
        ...
    def ImportFromFile(self, fileName: str, importMode: ExpressionCollection.ImportMode, expModified: bool, errorMessages: str) -> None:
        ...
    def ExportToFile(self, exportMode: ExpressionCollection.ExportMode, fileName: str, sortType: ExpressionCollection.SortType) -> None:
        ...
    def GetInterpartReferences(self) -> str:
        ...
    def GetInterpartReferencesWithDisplayNames(self, referencedPartNames: str, referencedDispNames: str) -> None:
        ...
    def GetInterpartReferencesFor4gd(self, referencedPartNames: str, referencedDispNames: str, referencedParts: typing.List[NXObject]) -> None:
        ...
    def RemoveInterpartReferences(self, partName: str) -> bool:
        ...
    def ChangeInterpartReferences(self, oldPartName: str, newPartName: str) -> None:
        ...
    def ChangeInterpartReferences(self, oldPartName: str, newPartName: str, doUpdate: bool, doChecking: bool) -> None:
        ...
    def ChangeInterpartReferencesFor4gd(self, targetPartOccTag: Assemblies.Component, oldSourcePartName: str, newSourcePartOccTag: Assemblies.Component, doUpdate: bool, doChecking: bool) -> None:
        ...
    def GetVisibleExpressions(self) -> typing.List[Expression]:
        ...
    def Rename(self, expression: Expression, newName: str) -> None:
        ...
    def SystemRename(self, expression: Expression, newName: str) -> None:
        ...
    def Replace(self, currentName: str, replaceName: str) -> None:
        ...
    def CreateSuppressByExpressionBuilder(self) -> SuppressByExpressionBuilder:
        ...
    def CreateSystemExpressionFromReferenceString(self, reference: str) -> Expression:
        ...
    def GetAttributeExpression(self, object: NXObject, title: str, type: NXObject.AttributeType, index: int) -> Expression:
        ...
    def ReplaceAttributeExpression(self, expression: Expression, object: NXObject, title: str, type: NXObject.AttributeType, index: int) -> None:
        ...
    def CreateInterpartExpressionsBuilder(self) -> InterpartExpressionsBuilder:
        ...
    def CreateReplaceExpressionsBuilder(self) -> ReplaceExpressionsBuilder:
        ...
    def AskInterpartRhsName(self, sourceExpression: Expression) -> str:
        ...
    def AskInterpartLhsName(self, sourceExpression: Expression) -> str:
        ...
    def ReplaceRhsInterpartExpression(self, oldRhsIpe: Expression, newRhsIpe: Expression) -> None:
        ...
    def GetExpressionsOfType(self, type: ExpressionCollection.Type, visibleOnly: bool) -> typing.List[Expression]:
        ...
    def GetWarningsOnExpression(self, expression: Expression, warningStrings: str) -> int:
        ...
    def UpdateForExternalChange(self) -> None:
        ...
    def Tag(self) -> Tag: ...



    class Type(enum.Enum):
        All = 0
        Attribute = 1
        Interpart = 2
        Measure = 3
        System = 4
        User = 5
        UserAndGeometry = 6
        UserExcludeSystem = 7
        UserSpecified = 8
    

    class SortType(enum.Enum):
        AlphaNum = 0
        TimeStamp = 1
        ReverseTimeStamp = 2
    

    class ImportMode(enum.Enum):
        Replace = 0
        DontReplace = 1
        DeleteImports = 2
    

    class ExportMode(enum.Enum):
        WorkPart = 0
        AllInAssyTree = 1
        AllParts = 2
    

class ExpressionBlock(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetNumSlots(self) -> int:
        ...
    def GetSlot(self, nProp: int) -> Parameter:
        ...
    def SetSlot(self, nProp: int, value: Parameter) -> None:
        ...


    class ExpressionBlock.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class Expression(NXObject):
    def __init__(self) -> None: ...
    def GetFormula(self) -> str:
        ...
    def SetFormula(self, rightHandSide: str) -> None:
        ...
    def SetNumberValueWithUnits(self, numberValue: float, units: Unit) -> None:
        ...
    def GetNumberValueWithUnits(self, unitsOption: Expression.UnitsOption, numberValue: float, unit: Unit) -> None:
        ...
    def GetPointValueWithUnits(self, unitsOption: Expression.UnitsOption) -> Point3d:
        ...
    def GetVectorValueWithUnits(self, unitsOption: Expression.UnitsOption) -> Vector3d:
        ...
    def GetListValue(self) -> any:
        ...
    def EditComment(self, newComment: str) -> None:
        ...
    def GetUsingFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetOwningFeature(self) -> Features.Feature:
        ...
    def GetOwningRpoFeature(self) -> Features.Feature:
        ...
    def GetDescriptor(self) -> str:
        ...
    def GetReferencingExpressions(self) -> typing.List[Expression]:
        ...
    def GetInterpartExpressionNames(self, partName: str, expName: str) -> None:
        ...
    def GetValueUsingUnits(self, unitsOption: Expression.UnitsOption) -> float:
        ...
    def MakeConstant(self) -> None:
        ...
    BooleanValue: bool
    Description: str
    Equation: str
    ExpressionString: str
    IntegerValue: int
    IsGeometricExpression: bool
    IsInterpartExpression: bool
    IsMassManagementExp: bool
    IsMeasurementExpression: bool
    IsNoEdit: bool
    IsNoUpdate: bool
    IsRightHandSideLockedFromEdit: bool
    IsUserLocked: bool
    IsUserSpecified: bool
    NumberValue: float
    PointValue: Point3d
    RightHandSide: str
    Status: Expression.StatusOption
    StringValue: str
    Type: str
    Units: Unit
    Value: float
    VectorValue: Vector3d


    class UnitsOption(enum.Enum):
        Base = 0
        Expression = 1
        DataEntry = 2
        Info = 3
    

    class StatusOption(enum.Enum):
        OutOfDate = 0
        UpToDate = 1
        Locked = 2
        Delayed = 3
        Broken = 4
        Unknown = 5
    

class ExcelFileFormatT(enum.Enum):
    WorkbookNormal = 0
    WorkbookDefault = 1


class ErrorList(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetErrorInfo(self, n: int) -> ErrorInfo:
        ...
    def Clear(self) -> None:
        ...
    Length: int


class ErrorInfo(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    Description: str
    ErrorCode: int
    ErrorObject: NXObject
    ErrorObjectDescription: str


class EngineeringFunction(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GravityAcceleration(self) -> float:
        ...
    def LinearMotionFinalVelocity1(self, v0: float, a: float, t: float) -> float:
        ...
    def LinearMotionFinalVelocity2(self, v0: float, x0: float, a: float, x: float) -> float:
        ...
    def LinearMotionDisplacement(self, x0: float, v0: float, a: float, t: float) -> float:
        ...
    def CircularMotionCentripetalAcceleration(self, v: float, r: float) -> float:
        ...
    def CentrifugalForce(self, m: float, v: float, r: float) -> float:
        ...
    def Period(self, f: float) -> float:
        ...
    def Frequency(self, t: float) -> float:
        ...
    def NewtonMotionSecondLaw(self, m: float, a: float) -> float:
        ...
    def PendulumPeriod(self, l: float, g: float) -> float:
        ...
    def PendulumFrequency(self, l: float, g: float) -> float:
        ...
    def SpringRestoringForce(self, k: float, x: float) -> float:
        ...
    def SpringPotentialEnergy(self, k: float, x: float) -> float:
        ...
    def SpringPeriod(self, k: float, m: float) -> float:
        ...
    def WorkDone(self, f: float, s: float, angle: float) -> float:
        ...
    def Power(self, f: float, v: float, angle: float) -> float:
        ...
    def AveragePower(self, w: float, tc: float) -> float:
        ...
    def LinearKineticEnergy(self, m: float, v: float) -> float:
        ...
    def GravitationalPotentialEnergy(self, m: float, h: float, g: float) -> float:
        ...
    def Momentum(self, m: float, v: float) -> float:
        ...
    def Torque(self, f: float, r: float, angle: float) -> float:
        ...
    def FrictionForce(self, n: float, u: float) -> float:
        ...
    def Impulse1(self, f: float, tc: float) -> float:
        ...
    def Impulse2(self, m: float, vc: float) -> float:
        ...
    def CircularAreaMomentOfInertia(self, r: float) -> float:
        ...
    def CenterLoadDisplacement(self, x: float, l: float, pp: float, e: float, i: float) -> float:
        ...
    def CenterLoadDisplacementMaximum(self, l: float, pp: float, e: float, i: float) -> float:
        ...
    def CenterLoadSlope(self, x: float, l: float, pp: float, e: float, i: float) -> float:
        ...
    def CenterLoadMoment(self, x: float, l: float, pp: float) -> float:
        ...
    def CenterLoadShearForce(self, x: float, l: float, pp: float) -> float:
        ...
    def IntermediateLoadDisplacement(self, x: float, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def IntermediateLoadSlope(self, x: float, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def IntermediateLoadMoment(self, x: float, l: float, pp: float, a: float) -> float:
        ...
    def IntermediateLoadShearForce(self, x: float, l: float, pp: float, a: float) -> float:
        ...
    def IntermediateLoadShearForceMaximum(self, l: float, pp: float, a: float) -> float:
        ...
    def IntermediateLoadBendingStressMaximum(self, l: float, pp: float, a: float, c: float, i: float) -> float:
        ...
    def IntermediateLoadMomentMaximum(self, l: float, pp: float, a: float) -> float:
        ...
    def IntermediateLoadSlopeMaximum(self, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def IntermediateLoadDisplacementMaximum(self, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def CenterLoadShearForceMaximum(self, l: float, pp: float) -> float:
        ...
    def CenterLoadMomentMaximum(self, l: float, pp: float) -> float:
        ...
    def CenterLoadBendingStressMaximum(self, l: float, pp: float, c: float, i: float) -> float:
        ...
    def CenterLoadSlopeMaximum(self, l: float, pp: float, e: float, i: float) -> float:
        ...
    def SymmetricLoadDisplacementMaximum(self, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def SymmetricLoadSlopeMaximum(self, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def SymmetricLoadMomentMaximum(self, l: float, pp: float, a: float) -> float:
        ...
    def SymmetricLoadBendingStressMaximum(self, pp: float, a: float, c: float, i: float) -> float:
        ...
    def SymmetricLoadShearForceMaximum(self, pp: float) -> float:
        ...
    def SymmetricLoadShearForce(self, x: float, l: float, pp: float, a: float) -> float:
        ...
    def SymmetricLoadMoment(self, x: float, l: float, pp: float, a: float) -> float:
        ...
    def SymmetricLoadSlope(self, x: float, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def SymmetricLoadDisplacement(self, x: float, l: float, pp: float, a: float, e: float, i: float) -> float:
        ...
    def UniformLoadDisplacement(self, x: float, l: float, pp: float, e: float, i: float) -> float:
        ...
    def UniformLoadSlope(self, x: float, l: float, pp: float, e: float, i: float) -> float:
        ...
    def UniformLoadMoment(self, x: float, l: float, pp: float) -> float:
        ...
    def UniformLoadShearForce(self, x: float, l: float, pp: float) -> float:
        ...
    def UniformLoadShearForceMaximum(self, l: float, pp: float) -> float:
        ...
    def UniformLoadMomentMaximum(self, l: float, pp: float) -> float:
        ...
    def UniformLoadSlopeMaximum(self, l: float, pp: float, e: float, i: float) -> float:
        ...
    def UniformLoadDisplacementMaximum(self, l: float, pp: float, e: float, i: float) -> float:
        ...
    def UniformLoadBendingStressMaximum(self, l: float, pp: float, c: float, i: float) -> float:
        ...
    def CompressionSpringForce(self, lf: float, ld: float, k: float) -> float:
        ...
    def CompressionSpringDeformedLength(self, lf: float, f: float, k: float) -> float:
        ...
    def CompressionSpringConstant(self, lf: float, ld: float, f: float) -> float:
        ...
    def CompressionSpringShearStressMaximum(self, f: float, d: float, dout: float) -> float:
        ...
    def CompressionSpringConstantFromParam(self, g: float, d2: float, d: float, tn: float) -> float:
        ...
    def VibrationNaturalCriticalDamping1(self, m: float, k: float) -> float:
        ...
    def VibrationNaturalCriticalDamping2(self, m: float, wn: float) -> float:
        ...
    def VibrationDampingRatio(self, cv: float, cc: float) -> float:
        ...
    def VibrationDampedAngularFrequency(self, dr: float, wn: float) -> float:
        ...
    def VibrationNaturalAngularFrequency(self, m: float, k: float) -> float:
        ...
    def VibrationNaturalFrequency(self, wn: float) -> float:
        ...
    def VibrationDampedFrequency(self, wd: float) -> float:
        ...
    def ORingRadialSectionMaximum(self, bd: float, btol: float, gd: float, gtol: float, cmax: float, cstol: float) -> float:
        ...
    def ORingRadialSectionMinimum(self, bd: float, btol: float, gd: float, gtol: float, cmin: float, cstol: float) -> float:
        ...
    def ORingRadialInnerDia(self, gd: float, gtol: float) -> float:
        ...
    def ORingRadialGrooveWidth(self, cs: float) -> float:
        ...
    def ORingRadialBoreDia(self, cs: float, id: float, cn: float, str: float) -> float:
        ...
    def ORingRadialGrooveDia(self, id: float, str: float) -> float:
        ...
    def ORingRadialGrooveDiaBore(self, bd: float, cs: float, cn: float) -> float:
        ...
    def ORingRadialStretch(self, id: float, gd: float) -> float:
        ...
    def GearRatio(self, orate: float, irate: float) -> float:
        ...
    def SpurGearPitchDiameter(self, m: float, n: float) -> float:
        ...
    def SpurGearCircularPitch1(self, m: float) -> float:
        ...
    def SpurGearCircularPitch2(self, d: float, n: float) -> float:
        ...
    def SpurGearModule(self, pd: float) -> float:
        ...
    def SpurGearNumberOfTeeth(self, m: float, d: float) -> float:
        ...
    def SpurGearAddendum(self, m: float) -> float:
        ...
    def SpurGearDedendum(self, m: float) -> float:
        ...
    def SpurGearOutsideDiameter1(self, m: float, d: float) -> float:
        ...
    def SpurGearOutsideDiameter2(self, m: float, n: float) -> float:
        ...
    def SpurGearRootDiameter(self, m: float, d: float) -> float:
        ...
    def SpurGearBaseCircleDiameter(self, d: float, pangle: float) -> float:
        ...
    def SpurGearBasePitch(self, m: float, pangle: float) -> float:
        ...
    def SpurGearToothThickness(self, m: float) -> float:
        ...
    def SpurGearCenterDistance(self, m: float, n1: float, n2: float) -> float:
        ...
    def SpurGearMinimumNumberNoUndercutting(self, pangle: float) -> float:
        ...
    def SpurGearContactRatio(self, m: float, r1o: float, r2o: float, r1b: float, r2b: float, c: float, pangle: float) -> float:
        ...
    def SpurGearLinearBacklash1(self, cc: float, pangle: float) -> float:
        ...
    def SpurGearLinearBacklash2(self, ct: float) -> float:
        ...
    def SpurGearLinearBacklash3(self, ct: float, pangle: float) -> float:
        ...
    def SpurGearAngularBacklash(self, ct: float, d: float) -> float:
        ...
    def NewCoordinateNormalStressX(self, xstress: float, ystress: float, sstress: float, rangle: float) -> float:
        ...
    def NewCoordinateNormalStressY(self, xstress: float, ystress: float, sstress: float, rangle: float) -> float:
        ...
    def NewCoordinateShearStressXy(self, xstress: float, ystress: float, sstress: float, rangle: float) -> float:
        ...
    def NewCoordinateNormalStrainX(self, xstrain: float, ystrain: float, sstrain: float, rangle: float) -> float:
        ...
    def NewCoordinateNormalStrainY(self, xstrain: float, ystrain: float, sstrain: float, rangle: float) -> float:
        ...
    def NewCoordinateShearStrainXy(self, xstrain: float, ystrain: float, sstrain: float, rangle: float) -> float:
        ...
    def PrincipalStressMaximum(self, xstress: float, ystress: float, sstress: float) -> float:
        ...
    def PrincipalStressMinimum(self, xstress: float, ystress: float, sstress: float) -> float:
        ...
    def PrincipalStressAngle(self, xstress: float, ystress: float, sstress: float) -> float:
        ...
    def ShearStressMaximum1(self, xstress: float, ystress: float, sstress: float) -> float:
        ...
    def ShearStressMaximum2(self, stress1: float, stress2: float) -> float:
        ...
    def ShearStressAngleMaximum(self, xstress: float, ystress: float, sstress: float) -> float:
        ...
    def PrincipalStrainMaximum(self, xstrain: float, ystrain: float, sstrain: float) -> float:
        ...
    def PrincipalStrainMinimum(self, xstrain: float, ystrain: float, sstrain: float) -> float:
        ...
    def PrincipalStrainAngle(self, xstrain: float, ystrain: float, sstrain: float) -> float:
        ...
    def ShearStrainMaximum1(self, xstrain: float, ystrain: float, sstrain: float) -> float:
        ...
    def ShearStrainMaximum2(self, strain1: float, strain2: float) -> float:
        ...
    def ShearStrainAngleMaximum(self, xstrain: float, ystrain: float, sstrain: float) -> float:
        ...
    def YoungsModulusFromPoissonShear(self, g: float, v: float) -> float:
        ...
    def YoungsModulusFromBulkPoisson(self, k: float, v: float) -> float:
        ...
    def YoungsModulusFromPoissonLame(self, l: float, v: float) -> float:
        ...
    def YoungsModulusFromBulkShear(self, k: float, g: float) -> float:
        ...
    def YoungsModulusFromShearLame(self, g: float, l: float) -> float:
        ...
    def YoungsModulusFromBulkLame(self, k: float, l: float) -> float:
        ...
    def PoissonRatioFromYoungsShear(self, e: float, g: float) -> float:
        ...
    def PoissonRatioFromYoungsBulk(self, e: float, k: float) -> float:
        ...
    def PoissonRatioFromYoungsLame(self, e: float, l: float) -> float:
        ...
    def PoissonRatioFromShearBulk(self, g: float, k: float) -> float:
        ...
    def PoissonRatioFromShearLame(self, g: float, l: float) -> float:
        ...
    def PoissonRatioFromBulkLame(self, k: float, l: float) -> float:
        ...
    def ShearModulusFromYoungsPoisson(self, e: float, v: float) -> float:
        ...
    def ShearModulusFromYoungsBulk(self, e: float, k: float) -> float:
        ...
    def ShearModulusFromYoungsLame(self, e: float, l: float) -> float:
        ...
    def ShearModulusFromBulkPoisson(self, k: float, v: float) -> float:
        ...
    def ShearModulusFromPoissonLame(self, v: float, l: float) -> float:
        ...
    def ShearModulusFromBulkLame(self, k: float, l: float) -> float:
        ...
    def BulkModulusFromYoungsPoisson(self, e: float, v: float) -> float:
        ...
    def BulkModulusFromYoungsShear(self, e: float, g: float) -> float:
        ...
    def BulkModulusFromYoungsLame(self, e: float, l: float) -> float:
        ...
    def BulkModulusFromShearPoisson(self, g: float, v: float) -> float:
        ...
    def BulkModulusFromPoissonLame(self, v: float, l: float) -> float:
        ...
    def BulkModulusFromShearLame(self, g: float, l: float) -> float:
        ...
    def FirstLameFromYoungsPoisson(self, e: float, v: float) -> float:
        ...
    def FirstLameFromYoungsShear(self, e: float, g: float) -> float:
        ...
    def FirstLameFromYoungsBulk(self, e: float, k: float) -> float:
        ...
    def FirstLameFromShearPoisson(self, g: float, v: float) -> float:
        ...
    def FirstLameFromBulkPoisson(self, k: float, v: float) -> float:
        ...
    def FirstLameFromBulkShear(self, k: float, g: float) -> float:
        ...
    def PipePressureLossOfLaminarFlow(self, pin: float, fv: float, fd: float, zz: float, l: float, d: float, u: float, g: float) -> float:
        ...
    def SquareTopBottomSupportedUniformLoadStress(self, pp: float, l: float, t: float) -> float:
        ...
    def SquareTopBottomSupportedUniformLoadDeflection(self, pp: float, l: float, t: float, e: float) -> float:
        ...
    def SquareBottomSupportedUniformLoadStress(self, pp: float, l: float, t: float) -> float:
        ...
    def SquareBottomSupportedUniformLoadDeflection(self, pp: float, l: float, t: float, e: float) -> float:
        ...
    def SquareEdgesSupportedCenterLoadStress(self, pp: float, l: float, r0: float, t: float) -> float:
        ...
    def SquareEdgesSupportedCenterLoadDeflection(self, pp: float, l: float, r0: float, t: float, e: float) -> float:
        ...
    def SquareEdgesFixedCenterLoadStress(self, pp: float, l: float, t: float) -> float:
        ...
    def SquareEdgesFixedCenterLoadDeflection(self, pp: float, l: float, t: float, e: float) -> float:
        ...
    def SquareEdgesFixedCircularCenterLoadStress(self, pp: float, l: float, r0: float, t: float) -> float:
        ...
    def SquareEdgesFixedCircularCenterLoadDeflection(self, pp: float, l: float, r0: float, t: float, e: float) -> float:
        ...
    def RectangularEdgesSupportedUniformLoadStress(self, pp: float, ll: float, ls: float, t: float) -> float:
        ...
    def RectangularEdgesSupportedUniformLoadDeflection(self, pp: float, ll: float, ls: float, t: float, e: float) -> float:
        ...
    def RectangularEdgesFixedUniformLoadStress(self, pp: float, ll: float, ls: float, t: float) -> float:
        ...
    def RectangularEdgesFixedUniformLoadDeflection(self, pp: float, ll: float, ls: float, t: float, e: float) -> float:
        ...
    def CircularEdgesSupportedUniformLoadStress(self, pp: float, r: float, t: float) -> float:
        ...
    def CircularEdgesSupportedUniformLoadDeflection(self, pp: float, r: float, t: float, e: float) -> float:
        ...
    def CircularEdgesSupportedCenterLoadStress(self, w: float, r: float, t: float) -> float:
        ...
    def CircularEdgesSupportedCenterLoadDeflection(self, w: float, r: float, t: float, e: float) -> float:
        ...
    def CircularEdgesFixedUniformLoadStress(self, pp: float, r: float, t: float) -> float:
        ...
    def CircularEdgesFixedUniformLoadDeflection(self, pp: float, r: float, t: float, e: float) -> float:
        ...
    def CircularEdgesFixedCenterLoadStress(self, w: float, r: float, t: float) -> float:
        ...
    def CircularEdgesFixedCenterLoadDeflection(self, w: float, r: float, t: float, e: float) -> float:
        ...
    def Tag(self) -> Tag: ...



class EndCutBlockBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Angle: Expression
    Offset: Expression
    SketchBlock: SketchExpressionModifierBuilder
    TaperType: EndCutBlockBuilder.TaperTypeOption


    class TaperTypeOption(enum.Enum):
        Trim = 0
        Extend = 1
        TrimAndExtend = 2
    

class EllipseCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Ellipse]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def Tag(self) -> Tag: ...



class Ellipse(Conic):
    def __init__(self) -> None: ...
    def GetParameters(self, majorRadius: float, minorRadius: float, startAngle: float, endAngle: float, rotationAngle: float, center: Point3d) -> None:
        ...
    def SetParameters(self, majorRadius: float, minorRadius: float, startAngle: float, endAngle: float, rotationAngle: float, center: Point3d) -> None:
        ...
    EndAngle: float
    MajorRadius: float
    MinorRadius: float
    StartAngle: float


class ElecCamCoupling(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    InitialTime: float
    ValueOffset: float
    SlaveControl: ControlBase
    MasterOffset: float
    SlaveOffset: float
    Active: bool
    MasterScale: float
    SlaveScale: float
    MasterAxis: AxisJoint
    MasterSignal: Signal
    MasterVirtualAxis: VirtualAxis
    TableObj: TableBase


    class ElecCamCoupling.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class EffectivityConditionBuilder(Builder):
    def __init__(self) -> None: ...
    def AddUnitEffectivity(self, fromUnit: int, toUnit: int) -> None:
        ...
    def AddUnitEffectivity(self, fromUnit: int, toUnitType: EffectivityConditionBuilder.ToUnitType) -> None:
        ...
    def RemoveUnitEffectivity(self, fromUnit: int, toUnit: int) -> None:
        ...
    def RemoveUnitEffectivity(self, fromUnit: int, toUnitType: EffectivityConditionBuilder.ToUnitType) -> None:
        ...
    def RegisterBasicEffectivityBuilder(self, beBuilder: BasicEffectivityBuilder) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.PDM.EffectivityTableBuilder instead.")"""
        ...
    EffectivityFormula: str
    EffectivityType: EffectivityConditionBuilder.EffectivityConditionType


    class ToUnitType(enum.Enum):
        StockOut = 0
        OpenEnd = 1
    

    class EffectivityConditionType(enum.Enum):
        Unit = 0
        UnitRange = 1
    

class EdgeVertexTangentRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, startEdge: Edge, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool) -> None:
        ...


class EdgeVertexRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, startEdge: Edge, isFromStart: bool) -> None:
        ...


class EdgeTangentRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, startEdge: Edge, endEdge: Edge, isFromStart: bool, angleTolerance: float, hasSameConvexity: bool) -> None:
        ...


class EdgeSheetBoundaryRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, sheet: Body) -> None:
        ...


class EdgeMultipleSeedTangentRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seedEdges: typing.List[Edge], angleTolerance: float, hasSameConvexity: bool) -> None:
        ...


class EdgeIntersectRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, facesOfFeatures1: typing.List[Face], facesOfFeatures2: typing.List[Face]) -> None:
        ...


class EdgeFeatureRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature]) -> None:
        ...


class EdgeFaceRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, faces: typing.List[Face]) -> None:
        ...


class EdgeDumbRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, edges: typing.List[Edge]) -> None:
        ...


class EdgeChainRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, startEdge: Edge, endEdge: Edge, isFromStart: bool) -> None:
        ...


class EdgeBoundaryRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, facesOfFeatures: typing.List[Face]) -> None:
        ...


class EdgeBodyRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, body: Body) -> None:
        ...


class Edge(DisplayableObject):
    def __init__(self) -> None: ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def GetUnsortedFaces(self) -> typing.List[Face]:
        ...
    def GetVertices(self, vertex1: Point3d, vertex2: Point3d) -> None:
        ...
    def GetBody(self) -> Body:
        ...
    def GetDraftingCurveInfo(self) -> Drawings.DraftingCurveInfo:
        ...
    def IsDraftingCurve(self) -> bool:
        ...
    def GetLength(self) -> float:
        ...
    def GetLocations(self) -> typing.List[GeometricUtilities.CurveLocation]:
        ...
    SolidEdgeType: Edge.EdgeType
    IsReference: bool


    class EdgeType(enum.Enum):
        Rubber = 0
        Linear = 1
        Circular = 2
        Elliptical = 3
        Intersection = 4
        Spline = 5
        SpCurve = 6
        Foreign = 7
        ConstantParameter = 8
        TrimmedCurve = 9
        Convergent = 10
        Undefined = 11
    

class DynamicObjectInstantiation(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    ToolToFind: str
    Find: bool
    FindFinished: bool
    ToolAtMagazine: int
    ToolAtPocket: int
    DetachToolFromMagazine: bool
    DetachToolFromMagazineFinished: bool
    DetachToolFromToolChanger: bool
    DetachToolFromToolChangerFinished: bool
    DetachToolFromSpindle: bool
    DetachToolFromSpindleFinished: bool
    Active: bool


    class DynamicObjectInstantiation.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class DxfdwgImporter(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    AcadLayoutsToImport: str
    AspectRatioOption: DxfdwgImporter.AspectRatioOptions
    AvoidUsedNXLayers: bool
    ConvLayoutData: bool
    ConvLayouts: DxfdwgImporter.ConvLayoutsAs
    ConvModelData: bool
    CrossHatchMappingFile: str
    DestForUnselectedLayer: int
    DrawingSheetNametoImportModelData: str
    FacetImport: DxfdwgImporter.FacetImportAs
    FileOpenFlag: bool
    HealBodies: bool
    ImportBlockType: DxfdwgImporter.ImportBlocksAs
    ImportCurvesType: DxfdwgImporter.ImportCurvesAs
    ImportDimensionType: DxfdwgImporter.ImportDimensionsAs
    ImportPolylineTo: DxfdwgImporter.ImportPolylinesAs
    ImportTo: DxfdwgImporter.ImportToEnum
    ImportToTeamcenter: bool
    LineFontMappingFile: str
    ModelScaleFactor: float
    Optimize: bool
    ProcessingOrder: DxfdwgImporter.ProcessingOrderAs
    ReadLayerNumFromPrefix: bool
    RotationAngle: float
    SendLayoutsTo: DxfdwgImporter.SendLayoutsAs
    SendModelDataTo: DxfdwgImporter.SendModelDataAs
    SettingsFile: str
    SimplifyGeometry: bool
    SkipEmptyLayer: bool
    TemplateFile: str
    TextFontMappingFile: str
    TranslateUnselectedLayer: bool
    TranslationX: float
    TranslationY: float
    TranslationZ: float
    UnSelectedLayers: str
    Units: DxfdwgImporter.UnitsEnum
    Workflow: DxfdwgImporter.WorkflowAs


    class WorkflowAs(enum.Enum):
        Drawing = 0
        ThreeD = 1
    

    class UnitsEnum(enum.Enum):
        SameAsTemplate = 0
        Metric = 1
        English = 2
    

    class SendModelDataAs(enum.Enum):
        Modeling = 0
        DrawingView = 1
        DrawingSheet = 2
        NewDrawingSheet = 3
        SelectedDrawingSheet = 4
    

    class SendLayoutsAs(enum.Enum):
        ImportedView = 0
        DrawingView = 1
    

    class ProcessingOrderAs(enum.Enum):
        Alphabetical = 0
        ObjectCount = 1
    

    class ImportToEnum(enum.Enum):
        Work = 0
        New = 1
    

    class ImportPolylinesAs(enum.Enum):
        Splines = 0
        ArcLines = 1
    

    class ImportDimensionsAs(enum.Enum):
        Real = 0
        Group = 1
    

    class ImportCurvesAs(enum.Enum):
        SketchCurves = 0
        Curves = 1
    

    class ImportBlocksAs(enum.Enum):
        Group = 0
        CustomSymbol = 1
        Part = 2
        NX2DComponent = 3
    

    class FacetImportAs(enum.Enum):
        Jt = 0
        Convergent = 1
    

    class ConvLayoutsAs(enum.Enum):
        All = 0
        SelectedInPreview = 1
    

    class AspectRatioOptions(enum.Enum):
        AutomaticCalculation = 0
        UseSameAsACADWidthFactor = 1
        UseValueSpecifiedInMappingFile = 2
        ScaleACADWidthFactorWithSpecifiedValue = 3
    

class DxfdwgCreator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    AutoCADRevision: DxfdwgCreator.AutoCADRevisionOptions
    CrossHatchMappingFile: str
    DrawingList: str
    ExportAs: DxfdwgCreator.ExportAsOption
    ExportData: DxfdwgCreator.ExportDataOption
    ExportFacesAs: DxfdwgCreator.ExportFacesAsOptions
    ExportFrom: DxfdwgCreator.ExportFromOption
    ExportScaleOption: DxfdwgCreator.ExportScaleOptions
    ExportScaleValue: float
    ExportSelectionBlock: ObjectSelector
    ExportSplinesAs: DxfdwgCreator.ExportSplinesAsOptions
    FileSaveFlag: bool
    FlattenAssembly: bool
    InputFile: str
    LayerMask: str
    LineFontMappingFile: str
    ObjectTypes: ObjectTypeSelector
    OutputFileType: DxfdwgCreator.OutputFileTypeOption
    OutputTo: DxfdwgCreator.OutputToOption
    OverlappingEntities: bool
    SettingsFile: str
    SurfaceDesignU: int
    SurfaceDesignV: int
    TextFontMappingFile: str
    ViewEditMode: bool
    ViewList: str
    WidthFactorMode: DxfdwgCreator.WidthfactorMethodOptions


    class WidthfactorMethodOptions(enum.Enum):
        AutomaticCalculation = 0
        UseSameAsNXAspectratio = 1
        UseValueSpecifiedInMappingFile = 2
        ScaleNXAspectratioWithSpecifiedValue = 3
    

    class OutputToOption(enum.Enum):
        Modeling = 0
        Drafting = 1
    

    class OutputFileTypeOption(enum.Enum):
        Dxf = 0
        Dwg = 1
    

    class ExportSplinesAsOptions(enum.Enum):
        Spline = 0
        Polyline2D = 1
        Polyline3D = 2
    

    class ExportScaleOptions(enum.Enum):
        Default = 0
        BaseView = 1
        UserSpecified = 2
    

    class ExportFromOption(enum.Enum):
        DisplayPart = 0
        ExistingPart = 1
    

    class ExportFacesAsOptions(enum.Enum):
        Facets = 0
        PolylineMesh = 1
    

    class ExportDataOption(enum.Enum):
        Modeling = 0
        Drawing = 1
    

    class ExportAsOption(enum.Enum):
        TwoD = 0
        ThreeD = 1
        Cgm = 2
    

    class AutoCADRevisionOptions(enum.Enum):
        R12 = 0
        R13 = 1
        R14 = 2
        R2000 = 3
        R2004 = 4
        R2005 = 5
        R2007 = 6
        R2010 = 7
        R2013 = 8
        R2018 = 9
    

class DrawShapeTaskEnvironment(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def Enter(self) -> None:
        ...
    def Exit(self) -> None:
        ...
    def SetFeatureToEdit(self, feature: Features.DrawShape) -> None:
        ...
    def SetCancelled(self) -> None:
        ...
    def Tag(self) -> Tag: ...

    ActiveFeature: Features.DrawShape


class DrawingUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def AddDrawingAutomationWizardHandler(self, handler: DrawingUtils.DrawingAutomationWizardHandler) -> int:
        ...
    def RemoveDrawingAutomationWizardHandler(self, id: int) -> None:
        ...
    def NewDrawingAutomationWizard(self) -> Drafting.DrawingAutomationWizard:
        ...
    def Tag(self) -> Tag: ...



    

    

    

class DrawingCompareManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreateSnapshot(self) -> None:
        ...
    def CreateTrackChanges(self) -> None:
        ...
    def DeleteTrackChanges(self) -> None:
        ...
    def DeleteSnapshot(self) -> None:
        ...
    def DeleteComparisonReport(self) -> None:
        ...
    def GetEntityObjectFromId(self, subfileID: int) -> NXObject:
        ...
    def CreateDrawingCompareSettingsBuilder(self) -> Drawings.DrawingCompareSettingsBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.Drawings.TrackDrawingChangesGeneralBuilder  for General Builder and NXOpen.Drawings.TrackDrawingChangesReportFilterBuilder for Report Filter Builder")"""
        ...
    def CreateCompareReportBuilder(self) -> Drawings.CompareReportBuilder:
        """[Obsolete("Deprecated in NX11.0.0.  Use DrawingCompareManager.CreateCompareReportBuilder instead.")"""
        ...
    def CreateCompareReportBuilder(self, partFileNameToCompare: str, reuseExistingSnapshot: bool) -> Drawings.CompareReportBuilder:
        ...
    def CreateOverlayData(self) -> None:
        ...
    def DeleteOverlayData(self) -> None:
        ...
    def PreserveChangeSymbol(self, idSymbols: typing.List[Annotations.IdSymbol]) -> None:
        ...
    def UnpreserveChangeSymbol(self, idSymbols: typing.List[Annotations.IdSymbol]) -> None:
        ...
    def SetRemoveUndoMarks(self, removeUndoMarks: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class DraftPointDataCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[GeometricUtilities.DraftPointData]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def CreateDraftPointData(self, point: Point, angle: str) -> GeometricUtilities.DraftPointData:
        ...
    def Tag(self) -> Tag: ...



class DraftingManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def VersionUpAllDraftingObjects(self) -> None:
        """[Obsolete("Deprecated in NX12.0.2.  No replacement method will be provided.")"""
        ...
    def VersionUpSelectedDraftingObjects(self, draftingObjects: typing.List[NXObject]) -> None:
        """[Obsolete("Deprecated in NX12.0.2.  No replacement method will be provided.")"""
        ...
    def CreateImportSymbolBuilder(self) -> Annotations.ImportSymbolBuilder:
        ...
    def CreateMarkAsTemplateBuilder(self) -> Drawings.MarkAsTemplateBuilder:
        ...
    def CreateSheetZoneReferenceBuilder(self) -> Drawings.SheetZoneReferenceBuilder:
        ...
    def CreateImportAutocadBlockBuilder(self) -> Annotations.ImportAutocadBlockBuilder:
        ...
    def GetTemplateInstantiationIsComplete(self) -> bool:
        ...
    def SetTemplateInstantiationIsComplete(self, templateInstantiationStatus: bool) -> None:
        ...
    def AddCutObject(self, object: DisplayableObject) -> None:
        ...
    def RestoreUnpastedObjects(self) -> None:
        ...
    def RestoreUnpastedObjectsOfPart(self, partOfUnpastedObject: Part) -> None:
        ...
    def IsCutObject(self, object: DisplayableObject) -> bool:
        ...
    def CreateDrawingsPropertiesBuilder(self, objects: typing.List[DisplayableObject]) -> Drawings.DrawingsPropertiesBuilder:
        ...
    def EnterDraftingApplication(self) -> None:
        ...
    def ExitDraftingApplication(self) -> None:
        ...
    def SetDrawingLayout(self, setToDrawingLayout: bool) -> None:
        ...
    def RenewObjects(self) -> int:
        ...
    def Tag(self) -> Tag: ...

    SectionLines: Drawings.SectionLineCollection
    AutomationManager: Drafting.AutomationManager
    BordersAndZonesObjects: Drawings.BordersAndZonesCollection


class DMUSessionCollection(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateDesignSession(self, referencePart: str) -> None:
        ...
    def OpenDesignSession(self, databaseObject: PDM.DatabaseObject) -> None:
        ...
    def DesignSessionIncludeComponentsInRecipe(self, dmusessionPartTag: Part, componentsToInclude: typing.List[Assemblies.Component]) -> None:
        ...
    def DesignSessionExcludeComponentsFromRecipe(self, dmusessionPartTag: Part, componentsToExclude: typing.List[Assemblies.Component]) -> None:
        ...
    def OpenDesignSessionWithSelectedComponents(self, databaseObject: PDM.DatabaseObject, componentReferenceCollector: ComponentReferenceCollector) -> None:
        ...
    def GetComponentReferenceCollector(self) -> ComponentReferenceCollector:
        ...
    def CreateDesignSessionBuilder(self) -> DesignSessionBuilder:
        ...
    def Tag(self) -> Tag: ...



class DistanceSensor(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Triggered: bool
    Signal: float
    Active: bool


    class DistanceSensor.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class DisplayPartOption(enum.Enum):
    ReplaceExisting = 0
    AllowAdditional = 1


class DisplayModification(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetNewGrid(self, uGrid: int, vGrid: int) -> None:
        ...
    def GetNewGrid(self, uGrid: int, vGrid: int) -> None:
        ...
    def Apply(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    ApplyToAllFaces: bool
    ApplyToOwningParts: bool
    FaceAnalysisMode: bool
    KnotDisplayState: bool
    NewColor: int
    NewFont: DisplayableObject.ObjectFont
    NewLayer: int
    NewTranslucency: int
    NewWidth: DisplayableObject.ObjectWidth
    PartiallyShaded: bool
    PointShowThrough: bool
    PointSymbol: int
    PoleDisplayState: bool
    ShowObjectName: bool


class DisplayManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def NewDisplayModification(self) -> DisplayModification:
        ...
    def BlankObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def UnblankObjects(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def ShowByType(self, type: DisplayManager.ShowHideType, scope: DisplayManager.ShowHideScope) -> int:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.DisplayManager.ShowByType that takes a string type instead. To find all registered ShowHideType strings use NXOpen.DisplayManager.GetShowableHideableTypes")"""
        ...
    def ShowByType(self, type: str, scope: DisplayManager.ShowHideScope) -> int:
        ...
    def HideByType(self, type: DisplayManager.ShowHideType, scope: DisplayManager.ShowHideScope) -> int:
        """[Obsolete("Deprecated in NX9.0.0.  Use NXOpen.DisplayManager.HideByType that takes a string type instead. To find all registered ShowHideType strings use NXOpen.DisplayManager.GetShowableHideableTypes")"""
        ...
    def HideByType(self, type: str, scope: DisplayManager.ShowHideScope) -> int:
        ...
    def ShowOnly(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def ShowAdjacent(self, objects: typing.List[DisplayableObject]) -> None:
        ...
    def ShowNodesRelatedToDisplayedElements(self, includeInteriorNodes: bool) -> None:
        ...
    def MakeUpToDate(self) -> None:
        ...
    def GetJ3dData(self) -> typing.List[DisplayManager.J3dData]:
        ...
    def GetJ3dGeometry(self, eid: DisplayableObject, tolerance: float, wireframe: bool, points: float, normals: float, pointsPerStrip: int) -> bool:
        ...
    def ShowObjects(self, objects: typing.List[DisplayableObject], layerSetting: DisplayManager.LayerSetting) -> None:
        ...
    def GetShowableHideableTypes(self) -> str:
        ...
    def Tag(self) -> Tag: ...

    FacetCacheMemoryLevel: DisplayManager.FacetCacheMemoryLevelType


    class ShowHideType(enum.Enum):
        All = 0
        Geometry = 1
        Bodies = 2
        Components = 3
        SolidBodies = 4
        SheetBodies = 5
        FacetedBodies = 6
        PolygonBodies = 7
        SheetPolygonBodies = 8
        SolidPolygonBodies = 9
        MidsurfacePolygonBodies = 10
        FromMeshPolygonBodies = 11
        FlowPolygonBodies = 12
        Datums = 13
        Points = 14
        DatumAxes = 15
        DatumPlanes = 16
        DatumPlaneGrids = 17
        EntitySelectionPlanes = 18
        Csys = 19
        Sketches = 20
        Curves = 21
        InfiniteLines = 22
        DraftingAnnotations = 23
        DraftingDimensions = 24
        DraftingNotes = 25
        DraftingSymbols = 26
        DraftingGdt = 27
        Pmi = 28
        PmiDimensions = 29
        PmiNotes = 30
        PmiSymbols = 31
        PmiGdt = 32
        AssemblyConstraints = 33
        PmiGeometry = 34
        CaeEntities = 35
        Meshes = 36
        Mesh0d = 37
        Mesh0dConcentratedMass = 38
        Mesh0dDistributedMass = 39
        Mesh0dHeatBody = 40
        Mesh0dNodeToGround = 41
        Mesh1d = 42
        Mesh1dBar = 43
        Mesh1dBeam = 44
        Mesh1dRod = 45
        Mesh1dBearing = 46
        Mesh1dBearing2 = 47
        Mesh1dRigidLink = 48
        Mesh1dInterpolation = 49
        Mesh1dSpring = 50
        Mesh1dEdgeContact = 51
        Mesh1dFaceContact = 52
        Mesh1dWeld = 53
        Mesh1dEdgeFaceConnection = 54
        Mesh1dPlotel = 55
        Mesh1dMass = 56
        Mesh1dMpc = 57
        Mesh1dJoint = 58
        Mesh1dFou3 = 59
        Mesh1dBush2 = 60
        Mesh2d = 61
        Mesh2dTri3 = 62
        Mesh2dTri6 = 63
        Mesh2dQuad4 = 64
        Mesh2dQuad8 = 65
        Mesh3d = 66
        Mesh3dTet4 = 67
        Mesh3dTet10 = 68
        Mesh3dTetMixed = 69
        Mesh3dHex8 = 70
        Mesh3dHex20 = 71
        Mesh3dHexcohes8 = 72
        Mesh3dHexcohes20 = 73
        Mesh3dWedge6 = 74
        Mesh3dWedge15 = 75
        Mesh3dWdgcohes6 = 76
        Mesh3dWdgcohes15 = 77
        Mesh3dPyramid5 = 78
        Mesh3dPyramid13 = 79
        Mesh3dPyramidMixed = 80
        DrawingObjects = 81
        DrawingDimensions = 82
        DrawingAnnotation = 83
        DrawingNotes = 84
        DrawingFeatureControlFrame = 85
        DrawingDatumFeatureSymbols = 86
        DrawingDatumTargets = 87
        DrawingBalloons = 88
        DrawingSurfaceFinishSymbols = 89
        DrawingWeldSymbols = 90
        DrawingTargetPointSymbols = 91
        DrawingIntersectionSymbols = 92
        DrawingCrosshatch = 93
        DrawingAreaFill = 94
        DrawingCenterlines = 95
        DrawingCustomSymbols = 96
        DrawingTables = 97
        DrawingTabularNotes = 98
        DrawingPartsLists = 99
        DrawingTitleBlocks = 100
        DrawingHoleTables = 101
        DrawingImages = 102
        PmiObject = 103
        PmiObjectDimensions = 104
        PmiAnnotations = 105
        PmiObjectNotes = 106
        PmiFeatureControlFrames = 107
        PmiDatumFeatureSymbols = 108
        PmiDatumTargets = 109
        PmiBalloons = 110
        PmiSurfaceFinishSymbols = 111
        PmiWeldSymbols = 112
        PmiCenterlines = 113
        PmiRegions = 114
        PmiTables = 115
        PmiCustomSymbols = 116
        Components2d = 117
        Images = 118
        RasterImage = 119
        AoAll = 120
        AoDeviationGauge = 121
        AoSectionAnalysis = 122
        AoGridAnalysis = 123
        AoHighlightLines = 124
        AoSurfaceContinuity = 125
        AoGapFlushness = 126
        AoCurveContinuity = 127
        AoCurveCurvature = 128
        AoSurfaceIntersection = 129
        AoDraftAnalysis = 130
        AoTrimAngleCheck = 131
        AoMoldFlow = 132
        AoLocalRadius = 133
        AoFaceCurvature = 134
        AoFaceAnalysis = 135
        AoWallThickness = 136
        AoSheetBoundary = 137
        MeshControls = 138
        MeshControlsEdgeDensity = 139
        MeshControlsMappedEdgeDensity = 140
        MeshControlsFaceDensity = 141
        MeshControlsMappedHoleDensity = 142
        MeshControlsWeldRowDensity = 143
        MeshControlsFilletDensity = 144
        MeshControlsCylinderDensity = 145
        MeshControlsBoundaryLayer = 146
        Mmc = 147
        MeshedPolygonBodies = 148
        UnmeshedPolygonBodies = 149
        MeshPoints = 150
        PmiSketchDimensions = 151
        CaeBoundingVolumes = 152
        MeshControlsPointDensity = 153
        MeshControlsBoundingVolumeDensity = 154
        EdgeSeparationCondition = 155
        SelectionRecipes = 156
        SelectionRecipesBoundingVolume = 157
        SelectionRecipesSingleNode = 158
        Lbc = 159
        LbcLoad = 160
        LbcConstraint = 161
        LbcSimulationObject = 162
        Mesh1dClink = 163
        Mesh1dBeam3 = 164
        Mesh1dBendPipe = 165
        Mesh1dRspline = 166
        CompositesAll = 167
        CompositesLaminates = 168
        CompositesPlies = 169
        CompositesRosettes = 170
        CompositesProducibilities = 171
        CompositesFlatPatterns = 172
    

    class ShowHideScope(enum.Enum):
        AnyInAssembly = 0
        WorkPartAndOccurrence = 1
    

    class LayerSetting(enum.Enum):
        MoveObjectsToWorkLayer = 0
        ChangeLayerToSelectable = 1
        Invalid = 2
    

    class DisplayManagerJ3dMaterial():
        Color: DisplayManager.J3dColor
        HighlightColor: DisplayManager.J3dColor
        Roughness: float
        SpecularFactor: float
        DiffuseFactor: float
        AmbientFactor: float
        Transparency: float
        def ToString(self) -> str:
            ...
    

    class DisplayManagerJ3dData():
        Eid: DisplayableObject
        HasTransform: bool
        Sheet: bool
        Name: str
        Material: DisplayManager.J3dMaterial
        def ToString(self) -> str:
            ...
    

    class DisplayManagerJ3dColor():
        Red: float
        Green: float
        Blue: float
        def ToString(self) -> str:
            ...
        def __init__(self, Red: float, Green: float, Blue: float) -> None: ...
    

    class FacetCacheMemoryLevelType(enum.Enum):
        None = 0
        One = 1
        Two = 2
        Three = 3
    

    class DisplayManager_J3dData():
        eid: Tag
        has_transform: bool
        sheet: bool
        name: int
        material: DisplayManager.J3dMaterial
    

class DisplayChanger(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    ExecuteMode: int
    Color: int
    Translucency: int
    Visibility: bool
    Active: bool


    class DisplayChanger.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class DisplayableObject(NXObject):
    def __init__(self) -> None: ...
    def Blank(self) -> None:
        ...
    def Unblank(self) -> None:
        ...
    def Highlight(self) -> None:
        ...
    def Unhighlight(self) -> None:
        ...
    def SetNameLocation(self, location: Point3d) -> None:
        ...
    def RedisplayObject(self) -> None:
        ...
    def RemoveViewDependency(self) -> None:
        ...
    Color: int
    IsBlanked: bool
    Layer: int
    LineFont: DisplayableObject.ObjectFont
    LineWidth: DisplayableObject.ObjectWidth
    NameLocation: Point3d


    class ObjectWidth(enum.Enum):
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
    

    class ObjectFont(enum.Enum):
        Solid = 1
        Dashed = 2
        Phantom = 3
        Centerline = 4
        Dotted = 5
        LongDashed = 6
        DottedDashed = 7
        Eight = 11
        Nine = 12
        Ten = 13
        Eleven = 14
    

class DirectionCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Direction]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateDirection(self, origin: Point3d, vector: Vector3d, update: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, line: Line, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, edge: IBaseCurve, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, datumAxis: DatumAxis, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, startPoint: Routing.ControlPoint, endPoint: Routing.ControlPoint, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, startPoint: Point, endPoint: Point, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, face: IParameterizedSurface, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, plane: IBasePlane, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, plane: Sketch, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, conic: Conic, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, icurve: IBaseCurve, t: Scalar, option: Direction.OnCurveOption, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, icurve: IBaseCurve, point: Point, option: Direction.OnCurveOption, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirectionOnPointParentCurve(self, atPoint: Point, curve: IBaseCurve, option: Direction.OnCurveOption, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, face: Face, u: Scalar, v: Scalar, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, face: Face, u: Scalar, v: Scalar, absoluteUv: bool, option: Direction.OnFaceOption, sectionDirection: Direction, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, face: Face, u: Scalar, v: Scalar, absoluteUv: bool, sectionAngle: Scalar, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, atPoint: Point, face: Face, option: Direction.OnFaceOption, sectionDirection: SmartObject, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, directionExtract: Direction, xform: Xform, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, point: Point, vector: Vector3d) -> Direction:
        ...
    def CreateDirection(self, geomObj: Face, point: Point, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, direction: Direction, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, port: Routing.Port, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, direction1: Direction, direction2: Direction, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, point: Point, exp: Expression, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, face: IParameterizedSurface, point: Point, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def CreateDirection(self, faces: ScCollector, point: Point, sense: Sense, updateOption: SmartObject.UpdateOption) -> Direction:
        ...
    def Tag(self) -> Tag: ...



class Direction(SmartObject):
    def __init__(self) -> None: ...
    def ReverseDirection(self) -> bool:
        ...
    Origin: Point3d
    Sense: Sense
    Vector: Vector3d


    class OnFaceOption(enum.Enum):
        IsoU = 0
        IsoV = 1
        Normal = 2
        Section = 3
    

    class OnCurveOption(enum.Enum):
        Tangent = 0
        Normal = 1
        Binormal = 2
    

class DexManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateCatiav4Importer(self) -> Catiav4Importer:
        ...
    def CreateStep214Importer(self) -> Step214Importer:
        ...
    def CreateStep242Importer(self) -> Step242Importer:
        ...
    def CreateCatiav5Importer(self) -> Catiav5Importer:
        ...
    def CreateIgesImporter(self) -> IgesImporter:
        ...
    def CreateStep203Importer(self) -> Step203Importer:
        ...
    def CreateDxfdwgImporter(self) -> DxfdwgImporter:
        ...
    def CreateIgesCreator(self) -> IgesCreator:
        ...
    def CreateStepCreator(self) -> StepCreator:
        ...
    def CreateCatiav4Creator(self) -> Catiav4Creator:
        ...
    def CreateCatiav5Creator(self) -> Catiav5Creator:
        ...
    def CreateDxfdwgCreator(self) -> DxfdwgCreator:
        ...
    def CreateNxto2dCreator(self) -> NXTo2dCreator:
        ...
    def CreateProeImporter(self) -> ProeImporter:
        """[Obsolete("Deprecated in NX1953.0.0.  Use NXOpen.DexManager.CreateCreoImporter instead.")"""
        ...
    def CreateCreoImporter(self) -> CreoImporter:
        ...
    def CreateAscImporter(self) -> ASCImporter:
        ...
    def CreateAcisImporter(self) -> AcisImporter:
        ...
    def CreateAcisExporter(self) -> AcisExporter:
        ...
    def CreateStlCreator(self) -> STLCreator:
        ...
    def CreateVirtuallabImporter(self) -> VirtuallabImporter:
        ...
    def CreateCreator3mf(self) -> Creator3MF:
        ...
    def CreateImporter3mf(self) -> Importer3MF:
        ...
    def CreateWavefrontObjImporter(self) -> WavefrontObjImporter:
        ...
    def CreateWavefrontObjCreator(self) -> WavefrontObjCreator:
        ...
    def CreateIfcImporter(self) -> IfcImporter:
        ...
    def CreateIfcCreator(self) -> IfcCreator:
        ...
    def CreateParasolidImporter(self) -> ParasolidImporter:
        ...
    def CreateParasolidExporter(self) -> ParasolidExporter:
        ...
    def CreateValidator(self) -> Validator:
        ...
    def CreateExtendedRealityFileCreator(self) -> ExtendedRealityFileCreator:
        ...
    def Tag(self) -> Tag: ...



class DexBuilder(Builder):
    def __init__(self) -> None: ...
    ProcessHoldFlag: bool


class DesignSessionBuilder(Builder):
    def __init__(self) -> None: ...
    def SetMasterFileName(self, masterFileName: str) -> None:
        ...
    def GetMasterFileName(self) -> str:
        ...
    def SetSessionName(self, sessionName: str) -> None:
        ...
    def GetSessionName(self) -> str:
        ...


class Decal(NXObject):
    def __init__(self) -> None: ...


class DatumPlane(DisplayableObject):
    def __init__(self) -> None: ...
    def SetCornerPoints(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> None:
        ...
    def GetCornerPoints(self, point1: Point3d, point2: Point3d, point3: Point3d, point4: Point3d) -> None:
        ...
    def SetReverseSection(self, reverseSection: bool) -> None:
        ...
    Feature: Features.Feature
    Normal: Vector3d
    Origin: Point3d
    ReverseSection: bool


class DatumConstraint(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetArcLength(self, length: str) -> None:
        ...
    def SetAlternateSolution(self, solution: DatumConstraint.Solution) -> None:
        ...
    def FreeResource(self) -> None:
        ...
    AlternateSolution: DatumConstraint.Solution
    ArcLength: Expression
    ArcLengthType: DatumConstraint.CurveOption
    ConstraintType: DatumConstraint.Type
    Geometry: DisplayableObject


    class Type(enum.Enum):
        Undefined = 0
        Coincident = 1
        Parallel = 2
        Perpendicular = 3
        Center = 4
        Tangent = 5
        Distance = 6
        Angle = 7
        Frenet = 8
    

    class Solution(enum.Enum):
        Undefined = 0
        Tangent = 1
        Normal = 2
        Binormal = 3
        OppositeTangent = 4
        OppositeNormal = 5
        OppositeBinormal = 6
        Project = 7
    

    class CurveOption(enum.Enum):
        Distance = 0
        Percent = 1
    

class DatumCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[DisplayableObject]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateFixedDatumPlane(self, origin: Point3d, orientation: Matrix3x3) -> DatumPlane:
        ...
    def CreateFixedDatumAxis(self, start: Point3d, end: Point3d) -> DatumAxis:
        ...
    def FindObject(self, journalIdentifier: str) -> DisplayableObject:
        ...
    def Tag(self) -> Tag: ...



class DatumAxis(DisplayableObject):
    def __init__(self) -> None: ...
    def SetEndPoints(self, start: Point3d, end: Point3d) -> None:
        ...
    def GetEndPoints(self, start: Point3d, end: Point3d) -> None:
        ...
    Direction: Vector3d
    Feature: Features.Feature
    Origin: Point3d


class DateItemBuilderList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[DateItemBuilder]) -> None:
        ...
    def Append(self, object: DateItemBuilder) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: DateItemBuilder) -> int:
        ...
    def FindItem(self, index: int) -> DateItemBuilder:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: DateItemBuilder) -> None:
        ...
    def Erase(self, obj: DateItemBuilder, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[DateItemBuilder]:
        ...
    def SetContents(self, objects: typing.List[DateItemBuilder]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: DateItemBuilder, object2: DateItemBuilder) -> None:
        ...
    def Insert(self, location: int, object: DateItemBuilder) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class DateItemBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def Validate(self) -> bool:
        ...
    Day: DateItemBuilder.DayOfMonth
    Month: DateItemBuilder.MonthOfYear
    Time: str
    Year: str


    class MonthOfYear(enum.Enum):
        Jan = 0
        Feb = 1
        Mar = 2
        Apr = 3
        May = 4
        Jun = 5
        Jul = 6
        Aug = 7
        Sep = 8
        Oct = 9
        Nov = 10
        Dec = 11
        Blank = 12
    

    class DayOfMonth(enum.Enum):
        Day01 = 0
        Day02 = 1
        Day03 = 2
        Day04 = 3
        Day05 = 4
        Day06 = 5
        Day07 = 6
        Day08 = 7
        Day09 = 8
        Day10 = 9
        Day11 = 10
        Day12 = 11
        Day13 = 12
        Day14 = 13
        Day15 = 14
        Day16 = 15
        Day17 = 16
        Day18 = 17
        Day19 = 18
        Day20 = 19
        Day21 = 20
        Day22 = 21
        Day23 = 22
        Day24 = 23
        Day25 = 24
        Day26 = 25
        Day27 = 26
        Day28 = 27
        Day29 = 28
        Day30 = 29
        Day31 = 30
        Blank = 31
    

class DateBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def CreateDateItemBuilder(self) -> DateItemBuilder:
        ...
    def Validate(self) -> bool:
        ...
    DateItem: DateItemBuilder
    DateItemList: DateItemBuilderList
    FromDateItem: DateItemBuilder
    ToDateItem: DateItemBuilder


class DataContainer(PropertyContainer):
    def __init__(self, ptr: int) -> None: ...
    def AddInteger(self, propertyName: str, value: int) -> None:
        ...
    def AddLogical(self, propertyName: str, value: bool) -> None:
        ...
    def AddDouble(self, propertyName: str, value: float) -> None:
        ...
    def AddString(self, propertyName: str, value: str) -> None:
        ...
    def AddEnum(self, propertyName: str, stringArray: str) -> None:
        ...
    def AddStrings(self, propertyName: str, stringArray: str) -> None:
        ...
    def AddPoint(self, propertyName: str, pointSc: Point3d) -> None:
        ...
    def AddVector(self, propertyName: str, vector: Vector3d) -> None:
        ...
    def AddBits(self, propertyName: str, bitsSc: int) -> None:
        ...
    def AddTaggedObject(self, propertyName: str, taggedSc: TaggedObject) -> None:
        ...
    def AddIntegerVector(self, propertyName: str, intVector: int) -> None:
        ...
    def AddDoubleVector(self, propertyName: str, doubleVector: float) -> None:
        ...
    def AddTaggedObjectVector(self, propertyName: str, tagVector: typing.List[TaggedObject]) -> None:
        ...
    def AddIntegerMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: int) -> None:
        ...
    def AddDoubleMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: float) -> None:
        ...
    def AddFile(self, propertyName: str, value: str) -> None:
        ...


class CylindricalJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    def GetAngularVelocity(self) -> float:
        ...
    def GetLinearVelocity(self) -> float:
        ...
    Attach: RigidBody
    Base: RigidBody
    Anchor: VectorArithmetic.Vector3
    Axis: VectorArithmetic.Vector3
    Angle: float
    Position: float
    Active: bool


    class CylindricalJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class CylindricalCoordinateSystem(CoordinateSystem):
    def __init__(self) -> None: ...


class CutViewCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CutView]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CutView:
        ...
    def UpdateCutView(self, view: CutView) -> None:
        ...
    def DeleteCutView(self, view: CutView) -> None:
        ...
    def CreateLinkedSectionView(self, view: CutView) -> ModelingView:
        ...
    def IsCutBody(self, body: Body) -> bool:
        ...
    def IsCutBodyOfView(self, body: Body, view: CutView, uncutBody: Body) -> bool:
        ...
    def IsUncutBodyOfView(self, body: Body, view: CutView, cutBody: Body) -> bool:
        ...
    def IsToolBody(self, body: Body) -> bool:
        ...
    def GetCutViewsOfObject(self, body: Body) -> typing.List[DisplayableObject]:
        ...
    def Tag(self) -> Tag: ...



class CutView(ModelingView):
    def __init__(self) -> None: ...
    def GetCutBodies(self) -> typing.List[DisplayableObject]:
        ...
    IsCutViewOutOfDate: bool
    IsModelingTypeCut: bool


class CustomWidth(TaggedObject):
    def __init__(self) -> None: ...
    Name: str
    Width: float


class CustomPopupMenuItem(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def GetId(self) -> int:
        ...
    def GetName(self) -> str:
        ...
    def SetDisabled(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class CustomPopupMenuHandler(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def RegisterAddCustomPopupMenuCallback(self, popupCb: CustomPopupMenuHandler.AddCustomPopupMenuCallback) -> None:
        ...
    def RegisterCustomPopupMenuInvokedCallback(self, popupCb: CustomPopupMenuHandler.CustomPopupMenuInvokedCallback) -> None:
        ...
    def GetSelectedNodes(self, selectedNodes: typing.List[TreeListNode]) -> None:
        ...
    def GetInvokedCommand(self) -> CustomPopupMenuItem:
        ...
    def FreeResource(self) -> None:
        ...
    def AddMenu(self, menuId: int, menuName: str) -> CustomPopupMenu:
        ...
    def AddMenuItem(self, menuItemId: int, menuItemName: str) -> CustomPopupMenuItem:
        ...
    def AddMenuSeparator(self) -> None:
        ...


    

    

    

    

    

    

class CustomPopupMenu(CustomPopupMenuItem):
    def __init__(self, ptr: int) -> None: ...
    def AddMenuItem(self, menuItemId: int, menuItemName: str) -> CustomPopupMenuItem:
        ...
    def AddMenu(self, menuId: int, menuName: str) -> CustomPopupMenu:
        ...
    def AddMenuSeparator(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class CurveTangentRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seedCurve: Curve, endCurve: Curve, isFromSeedStart: bool, angleTolerance: float, gapTolerance: float) -> None:
        ...


class CurveSnapOptionsBuilder(Builder):
    def __init__(self) -> None: ...
    Collinear: bool
    OrthogonalAlignment: bool
    OrthogonalDirection: bool
    Parallel: bool
    Perpendicular: bool
    Tangent: bool


class CurveParameterType(enum.Enum):
    ArcLength = 0
    PercentArcLength = 1
    ThroughPoint = 2


class CurveOnCurveJoint(AxisJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Point: VectorArithmetic.Vector3
    Axis: VectorArithmetic.Vector3
    Position: float
    Slip: bool
    Active: bool


    class CurveOnCurveJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class CurveGroupRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, groups: typing.List[Group]) -> None:
        ...


class CurveFeatureTangentRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature], seedCurve: Curve, endCurve: Curve, isFromSeedStart: bool, angleTolerance: float, gapTolerance: float) -> None:
        ...


class CurveFeatureRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature]) -> None:
        ...


class CurveFeatureChainRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature], seedCurve: Curve, endCurve: Curve, fromSeedStart: bool, gapTolerance: float) -> None:
        ...


class CurveDumbRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, curves: typing.List[Curve]) -> None:
        ...


class CurveCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Curve]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateLine(self, startPoint: Point3d, endPoint: Point3d) -> Line:
        ...
    def CreateLine(self, startPoint: Point, endPoint: Point) -> Line:
        ...
    def CreateInfiniteLine(self, startPoint: Point3d, endPoint: Point3d) -> InfiniteLine:
        ...
    def CreatePairedInfiniteLine(self, line: Line) -> InfiniteLine:
        ...
    def CreateArc(self, startPoint: Point3d, pointOn: Point3d, endPoint: Point3d, alternateSolution: bool, startAndEndGotFlipped: bool) -> Arc:
        ...
    def CreateArc(self, center: Point3d, matrix: NXMatrix, radius: float, startAngle: float, endAngle: float) -> Arc:
        ...
    def CreateArc(self, center: Point3d, xDirection: Vector3d, yDirection: Vector3d, radius: float, startAngle: float, endAngle: float) -> Arc:
        ...
    def CreateEllipse(self, center: Point3d, majorRadius: float, minorRadius: float, startAngle: float, endAngle: float, rotationAngle: float, matrix: NXMatrix) -> Ellipse:
        ...
    def CreateEllipse(self, center: Point3d, xDirection: Vector3d, yDirection: Vector3d, majorRadius: float, minorRadius: float, startAngle: float, endAngle: float) -> Ellipse:
        ...
    def CreateParabola(self, center: Point3d, focalLength: float, minimumDY: float, maximumDY: float, rotationAngle: float, matrix: NXMatrix) -> Parabola:
        ...
    def CreateParabola(self, center: Point3d, xDirection: Vector3d, yDirection: Vector3d, focalLength: float, minimumDY: float, maximumDY: float) -> Parabola:
        ...
    def CreateHyperbola(self, center: Point3d, semiTransverseLength: float, semiConjugateLength: float, minimumDY: float, maximumDY: float, rotationAngle: float, matrix: NXMatrix) -> Hyperbola:
        ...
    def CreateHyperbola(self, center: Point3d, xDirection: Vector3d, yDirection: Vector3d, semiTransverseLength: float, semiConjugateLength: float, minimumDY: float, maximumDY: float) -> Hyperbola:
        ...
    def CreateVirtualBlendCurve(self, updateOption: SmartObject.UpdateOption, blendFace: IParameterizedSurface, tolerance: float) -> Curve:
        ...
    def CreateVirtualCenterlineCurve(self, updateOption: SmartObject.UpdateOption, blendFace: IParameterizedSurface, tolerance: float) -> Curve:
        ...
    def CreateSmartCompositeCurve(self, section: Section, updateOption: SmartObject.UpdateOption, tolerance: float) -> Curve:
        ...
    def CreateSmartCompositeCurve(self, curve: Curve, updateOption: SmartObject.UpdateOption) -> Curve:
        ...
    def CreateExtractedCurve(self, curveToExtract: ICurve, type: int, subtype: int, xform: Xform, tolerance: float, updateOption: SmartObject.UpdateOption) -> ICurve:
        ...
    def Tag(self) -> Tag: ...



class CurveChainRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seedCurve: Curve, endCurve: Curve, fromSeedStart: bool, gapTolerance: float) -> None:
        ...


class Curve(SmartObject):
    def __init__(self) -> None: ...
    def GetDraftingCurveInfo(self) -> Drawings.DraftingCurveInfo:
        ...
    def IsDraftingCurve(self) -> bool:
        ...
    def GetLength(self) -> float:
        ...
    def GetLocations(self) -> typing.List[GeometricUtilities.CurveLocation]:
        ...
    IsReference: bool


class CreoImporter(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    HealBodies: bool
    ImportTo: CreoImporter.ImportToOption
    ImportToTeamcenter: bool
    IncludeNonManifoldObj: bool
    Optimize: bool
    SettingsFile: str
    SimplifyGeometry: bool


    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

class Creator3MF(Builder):
    def __init__(self) -> None: ...
    AngularTolerance: float
    ChordalTolerance: float
    LatticeItemList: GeometricUtilities.LatticeItemListBuilder
    OutputFile: str
    RetainAssemblyStructure: bool
    SelectBody: SelectNXObjectList
    ShowInformationWindow: bool


class CoordinateSystemCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CoordinateSystem]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateCoordinateSystem(self, origin: Point3d, orientation: Matrix3x3, isTemporary: bool) -> CartesianCoordinateSystem:
        ...
    def CreateCoordinateSystem(self, origin: Point3d, xDirection: Vector3d, yDirection: Vector3d) -> CartesianCoordinateSystem:
        ...
    def CreateCylindricalCoordinateSystem(self, origin: Point3d, xDirection: Vector3d, yDirection: Vector3d) -> CylindricalCoordinateSystem:
        ...
    def CreateSphericalCoordinateSystem(self, origin: Point3d, xDirection: Vector3d, yDirection: Vector3d) -> SphericalCoordinateSystem:
        ...
    def CreateCoordinateSystem(self, origin: Point3d, orientation: NXMatrix, isTemporary: bool) -> CartesianCoordinateSystem:
        ...
    def CreateCoordinateSystem(self, xform: Xform, update: SmartObject.UpdateOption) -> CartesianCoordinateSystem:
        ...
    def CreateCylindricalCoordinateSystem(self, origin: Point3d, orientation: NXMatrix, isTemporary: bool) -> CylindricalCoordinateSystem:
        ...
    def CreateCylindricalCoordinateSystem(self, xform: Xform, update: SmartObject.UpdateOption) -> CylindricalCoordinateSystem:
        ...
    def CreateSphericalCoordinateSystem(self, origin: Point3d, orientation: NXMatrix, isTemporary: bool) -> SphericalCoordinateSystem:
        ...
    def CreateSphericalCoordinateSystem(self, xform: Xform, update: SmartObject.UpdateOption) -> SphericalCoordinateSystem:
        ...
    def GetOriginAndDirections(self, csystem: CoordinateSystem, origin: Point, direction1: Direction, direction2: Direction) -> None:
        ...
    def Tag(self) -> Tag: ...



class CoordinateSystem(SmartObject):
    def __init__(self) -> None: ...
    def GetDirections(self, xDirection: Vector3d, yDirection: Vector3d) -> None:
        ...
    def SetDirections(self, xDirection: Vector3d, yDirection: Vector3d) -> None:
        ...
    def GetSolverCardSyntax(self) -> str:
        ...
    IsTemporary: bool
    Label: int
    Name: str
    Orientation: NXMatrix
    Origin: Point3d


class ConvertToFromReferenceBuilder(Builder):
    def __init__(self) -> None: ...
    def AddProjectFeatureCurves(self, entity: Curve) -> None:
        ...
    def RemoveProjectFeatureCurves(self, entity: Curve) -> None:
        ...
    InputObjects: SelectNXObjectList
    OutputState: ConvertToFromReferenceBuilder.OutputType
    SelectAllProjectFeatureCurves: bool


    class OutputType(enum.Enum):
        Reference = 0
        Active = 1
    

class ConvergentFacet(IFacet):
    def __init__(self) -> None: ...
    def GetVertices(self) -> typing.List[Point3d]:
        ...
    def GetAdjacentFacet(self, edgeIndex: int) -> ConvergentFacet:
        ...
    def GetVertexNormals(self) -> typing.List[Vector3d]:
        ...
    def GetUnitNormal(self) -> Vector3d:
        ...
    def SetVertices(self, points: typing.List[Point3d]) -> None:
        ...
    def GetPlaneEquation(self, planeNormal: Vector3d, dCoefficient: float) -> None:
        ...
    def Destroy(self) -> None:
        ...
    IsValid: bool
    OwningFace: Face
    Vertex0: Point3d
    Vertex1: Point3d
    Vertex2: Point3d


class ControlBase(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetForce(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetForce(self) -> VectorArithmetic.Vector3:
        ...
    def GetTorque(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetTorque(self) -> VectorArithmetic.Vector3:
        ...


class ContentDefinition(NXObject):
    def __init__(self) -> None: ...


    class Type(enum.Enum):
        Baseline = 0
        ChangeNotice = 1
    

class Conic(Curve):
    def __init__(self) -> None: ...
    def GetOrientation(self, center: Point3d, xDirection: Vector3d, yDirection: Vector3d) -> None:
        ...
    def SetOrientation(self, center: Point3d, xDirection: Vector3d, yDirection: Vector3d) -> None:
        ...
    def SetParameters(self, startPoint: Point3d, endPoint: Point3d, anchorPoint: Point3d, rho: float) -> None:
        ...
    CenterPoint: Point3d
    Matrix: NXMatrix
    RotationAngle: float


class ConfiguredPart(NXObject):
    def __init__(self) -> None: ...


class ComponentReferenceCollector(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def AddComponentWithCsidVector(self, componentReference: str) -> None:
        ...


class ComponentPart(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def Copy(self) -> ComponentPart:
        ...
    def ActivateAll(self, bActive: bool) -> None:
        ...
    NumParts: int
    Parts: typing.List[RuntimeObject]


    class ComponentPart.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class ColorWidth(TaggedObject):
    def __init__(self) -> None: ...
    Width: float
    WidthSource: int


class ColorRegionRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self) -> IFacet:
        ...


class ColorManager(Utilities.NXRemotableObject):
    def __init__(self, owner: BasePart) -> None: ...
    def Find(self, name: str) -> NXColor:
        ...
    def Find(self, id: int) -> NXColor:
        ...
    def Tag(self) -> Tag: ...



class ColorDefinitionRgb():
    Red: float
    Green: float
    Blue: float
    def ToString(self) -> str:
        ...
    def __init__(self, Red: float, Green: float, Blue: float) -> None: ...


class ColorDefinition(TaggedObject):
    def __init__(self) -> None: ...
    def GetColorValues(self) -> ColorDefinitionRgb:
        ...
    def SetColorValues(self, colorVals: ColorDefinitionRgb) -> None:
        ...
    ColorIndex: int
    ColorName: str
    FavoriteIndex: int


class CollisionSensor(ShapeBody):
    def __init__(self, pItem: int) -> None: ...
    def GetOwner(self) -> RigidBody:
        ...
    def IsMember(self, part: CollisionBody) -> bool:
        ...
    def IsMember(self, body: RigidBody) -> bool:
        ...
    NumIntersect: int
    Intersects: typing.List[CollisionBody]
    Triggered: bool
    Active: bool


    class CollisionSensor.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class CollisionMaterial(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def Copy(self) -> CollisionMaterial:
        ...
    StaticFriction: float
    DynamicFriction: float
    RollingFriction: float
    Restitution: float


    class CollisionMaterial.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class CollisionBody(ShapeBody):
    def __init__(self, pItem: int) -> None: ...
    def GetOwner(self) -> RigidBody:
        ...
    TransportSurfaces: typing.List[TransportSurface]
    Active: bool
    Sticky: bool
    Surface: CollisionMaterial


    class CollisionBody.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class CollaborativeDesignCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[CollaborativeDesign]:
        ...
    def __init__(self, owner: CollaborativeContentManager) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> CollaborativeDesign:
        ...
    def Find(self, journalIdentifier: str) -> TaggedObject:
        ...
    def Tag(self) -> Tag: ...

    CurrentSubsetBuilder: Assemblies.SubsetBuilder


class CollaborativeDesign(NXObject):
    def __init__(self) -> None: ...
    def GetAllPartitionSchemes(self, partitionSchemes: typing.List[Assemblies.PartitionScheme]) -> None:
        ...
    def GetEffectivityRangeFormula(self) -> str:
        ...
    def GetContentDefinition(self, definitionType: ContentDefinition.Type, journalId: str, journalRevisionId: str) -> ContentDefinition:
        ...
    AttributeGroups: PDM.AttributeGroupCollection


class CollaborativeContentManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateDesignElementBuilder(self, workset: Part, operation: Assemblies.DesignElementBuilder.OperationType) -> Assemblies.DesignElementBuilder:
        ...
    def CreateOverridePartBuilder(self, workSetPart: Part) -> Assemblies.CreateOverridePartBuilder:
        ...
    def DeleteOverridePartBuilder(self, workSetPart: Part) -> Assemblies.DeleteOverridePartBuilder:
        ...
    def CreatePositioningGroupBuilder(self, worksetPart: Part, positioningGroup: Assemblies.PositioningGroup) -> Assemblies.PositioningGroupBuilder:
        ...
    def CreateAbsolutePositionBuilder(self, workSetPart: Part) -> Assemblies.AbsolutePositionBuilder:
        ...
    def CreateUpdateDesignElementPositionBuilder(self, workSetPart: Part) -> Assemblies.UpdateDesignElementPositionBuilder:
        ...
    def CreateCopyDesignElementBuilder(self, part: Part) -> Assemblies.CopyDesignElementBuilder:
        ...
    def Tag(self) -> Tag: ...

    CollaborativeDesigns: CollaborativeDesignCollection


class ClipboardOperationsManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Part) -> None: ...
    def CreatePasteSpecialBuilder(self) -> PasteSpecialBuilder:
        ...
    def CreateCopyCutBuilder(self) -> Gateway.CopyCutBuilder:
        ...
    def CreatePasteBuilder(self) -> Gateway.PasteBuilder:
        ...
    def Tag(self) -> Tag: ...



class ChangeMaterial(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Body1: RuntimeObject
    Body2: RuntimeObject
    Material: CollisionMaterial
    Active: bool


    class ChangeMaterial.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class CGMImporter(Importer):
    def __init__(self) -> None: ...
    Crosshatching: bool
    UseExportSessionWidths: bool


class CGMBuilder(Builder):
    def __init__(self) -> None: ...
    def GetDatasetNames(self) -> str:
        ...
    def SetDatasetNames(self, datasetNames: str) -> None:
        ...
    def GetFilenames(self) -> str:
        ...
    def SetFilenames(self, filenames: str) -> None:
        ...
    def CreateCdf(self) -> CDF:
        ...
    def GetCdf(self) -> CDF:
        ...
    def CreateWidthDefinition(self) -> WidthDefinition:
        ...
    def GetWidthDefinition(self) -> WidthDefinition:
        ...
    Action: CGMBuilder.ActionOption
    Colors: CGMBuilder.Color
    CustomSymbolsInForeground: bool
    DatasetType: str
    DeleteDatasets: bool
    ImageResolution: CGMBuilder.ImageResolutionOption
    Multiple: CGMBuilder.MultipleOption
    NamedReferenceType: str
    OutputText: CGMBuilder.OutputTextOption
    RasterImages: bool
    Relation: CGMBuilder.RelationOption
    Scale: float
    ShadedGeometry: bool
    Size: CGMBuilder.SizeOption
    SourceBuilder: PlotSourceBuilder
    Units: CGMBuilder.UnitsOption
    VdcCoordinates: CGMBuilder.Vdc
    Widths: CGMBuilder.Width
    XDimension: float
    YDimension: float


    class Width(enum.Enum):
        StandardWidths = 0
        SingleWidth = 1
        CustomThreeWidths = 2
        CustomPalette = 3
    

    class Vdc(enum.Enum):
        Integer = 0
        Real = 1
    

    class UnitsOption(enum.Enum):
        Metric = 0
        English = 1
    

    class SizeOption(enum.Enum):
        FullScale = 0
        ScaleFactor = 1
        Dimension = 2
    

    class RelationOption(enum.Enum):
        Specification = 0
        Manifestation = 1
        Undefined = 2
    

    class OutputTextOption(enum.Enum):
        Text = 0
        Polylines = 1
        Bestfit = 2
    

    class MultipleOption(enum.Enum):
        Individual = 0
        Single = 1
    

    class ImageResolutionOption(enum.Enum):
        Draft = 0
        Low = 1
        Medium = 2
        High = 3
    

    class Color(enum.Enum):
        AsDisplayed = 0
        PartColors = 1
        CustomPalette = 2
        BlackOnWhite = 3
        LegacyColors = 4
        ColorsByWidth = 5
    

    class ActionOption(enum.Enum):
        CreateNew = 0
        OverwriteExisting = 1
        FileBrowser = 2
    

class CDF(TaggedObject):
    def __init__(self) -> None: ...
    def GetColorDefinitions(self) -> typing.List[ColorDefinition]:
        ...


class Catiav5Importer(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    EnableFeatureTree: bool
    FileOpenFlag: bool
    ImportTo: Catiav5Importer.ImportToOption
    ImportToTeamcenter: bool
    IncludeCSYS: bool
    IncludeIndWireFrame: bool
    IncludeNoShowEntity: bool
    IncludeRefGeom: bool
    Optimize: bool
    SearchDirectoryList: str
    SettingsFile: str
    SimplifyFacesandEdges: bool
    TotalSearchDirectories: int


    class ImportToOption(enum.Enum):
        WorkPart = 0
        NewPart = 1
    

class Catiav5Creator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    EnableHybridDesign: bool
    ExportFrom: Catiav5Creator.ExportFromOption
    ExportSelectionBlock: ObjectSelector
    FileSaveFlag: bool
    IncludeBlankedObj: bool
    IncludeCSYS: bool
    IncludeIndWireFrame: bool
    IncludeRefGeom: bool
    InputFile: str
    SettingsFile: str


    class ExportFromOption(enum.Enum):
        DisplayPart = 0
        ExistingPart = 1
    

class Catiav4Importer(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    FileOpenFlag: bool
    HealBodies: bool
    Optimize: bool
    SettingsFile: str
    SimplifyGeometry: bool


class Catiav4Creator(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    ExportSelectionBlock: ObjectSelector
    FileSaveFlag: bool
    SettingsFile: str
    WriteSolidAs: Catiav4Creator.SolidBodyOutputOption


    class SolidBodyOutputOption(enum.Enum):
        VOLUMEs = 0
        Solide = 1
    

class CartesianCoordinateSystem(CoordinateSystem):
    def __init__(self) -> None: ...


class CamCoupling(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetMasterForce(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetMasterForce(self) -> VectorArithmetic.Vector3:
        ...
    def GetMasterTorque(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetMasterTorque(self) -> VectorArithmetic.Vector3:
        ...
    def GetSlaveForce(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetSlaveForce(self) -> VectorArithmetic.Vector3:
        ...
    def GetSlaveTorque(self, stepSize: float) -> VectorArithmetic.Vector3:
        """[Obsolete("Deprecated in NX9.0.1.  Use the un-deprecated method with the same method name.")"""
        ...
    def GetSlaveTorque(self) -> VectorArithmetic.Vector3:
        ...
    MasterAxis: AxisJoint
    SlaveAxis: AxisJoint
    Position: float
    Correction: float
    AllowSlip: bool
    MasterScale: float
    SlaveScale: float
    Active: bool


    class CamCoupling.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class CaeObjectType(Utilities.NXRemotableObject):
    def __init__(self) -> None: ...


    class CaeSubType(enum.Enum):
        None = 0
        ElementFace = 1
        ElementEdge = 2
    

class BunchFacetsOnFaceRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...


class Builder(TaggedObject):
    def __init__(self) -> None: ...
    def Commit(self) -> NXObject:
        ...
    def Destroy(self) -> None:
        ...
    def GetCommittedObjects(self) -> typing.List[NXObject]:
        ...
    def GetObject(self) -> NXObject:
        ...
    def ShowResults(self) -> None:
        ...
    def Validate(self) -> bool:
        ...
    PreviewBuilder: PreviewBuilder


class BrushFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, brushToolStartPoint: Point3d, brushToolDirection: Vector3d, brushToolRadius: float, collectInsideFacetsOnly: bool, seedFacet: IFacet) -> None:
        ...


class BreakingConstraint(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    BreakingJoint: Joint
    Force: float
    Active: bool
    BreakableJoint: Joint
    Magnitude: float


    class BreakingConstraint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class BorderLineStyleT(enum.Enum):
    None = 0
    Continuous = 1
    Dash = 2
    DashDot = 3
    DashDotDot = 4
    Dot = 5
    Double = 6
    SlantDashDot = 7


class BondZone(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def UpdateBond(self) -> None:
        ...
    def UpdateBond(self, RigidBodies: typing.List[RigidBody]) -> int:
        ...
    Triggered: bool
    Bonding: bool
    ActionMode: BondZone.BondAction
    Active: bool


    class BondZone.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

    class BondAction(enum.Enum):
        Collision = 0
        UserDefined = 1
    

class BodyList(TaggedObject):
    def __init__(self) -> None: ...
    def Append(self, objects: typing.List[Body]) -> None:
        ...
    def Append(self, object: Body) -> None:
        ...
    def ClearIndex(self, deleteIdx: int) -> None:
        ...
    def FindIndex(self, obj: Body) -> int:
        ...
    def FindItem(self, index: int) -> Body:
        ...
    def Erase(self, index: int) -> None:
        ...
    def Erase(self, index: int, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Erase(self, obj: Body) -> None:
        ...
    def Erase(self, obj: Body, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Clear(self, deleteOption: ObjectList.DeleteOption) -> None:
        ...
    def GetContents(self) -> typing.List[Body]:
        ...
    def SetContents(self, objects: typing.List[Body]) -> None:
        ...
    def Swap(self, index1: int, index2: int) -> None:
        ...
    def Swap(self, object1: Body, object2: Body) -> None:
        ...
    def Insert(self, location: int, object: Body) -> None:
        ...
    def MoveToTop(self, index: int) -> None:
        ...
    def MoveToBottom(self, index: int) -> None:
        ...
    Length: int


class BodyGroupRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, groups: typing.List[Group]) -> None:
        ...


class BodyFeatureRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, features: typing.List[Features.Feature]) -> None:
        ...


class BodyFacetsRule(FacetSelectionRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, bodies: typing.List[NXObject]) -> None:
        ...


class BodyDumbRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, bodies: typing.List[Body]) -> None:
        ...


class BodyCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Body]:
        ...
    def __init__(self, owner: Part) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Body:
        ...
    def CreateFourPointSurfaceBuilder(self) -> FourPointSurfaceBuilder:
        ...
    def CreateSurfaceUvdirectionBuilder(self) -> SurfaceUVDirectionBuilder:
        ...
    def CollectionSweepabilityCheck(self, setColor: bool) -> None:
        ...
    def Tag(self) -> Tag: ...



class Body(DisplayableObject):
    def __init__(self) -> None: ...
    def GetFeatures(self) -> typing.List[Features.Feature]:
        ...
    def GetFaces(self) -> typing.List[Face]:
        ...
    def GetEdges(self) -> typing.List[Edge]:
        ...
    def RemoveMergedRibImprintedEdges(self, originalFace: Face, imprintedEdges: typing.List[Edge]) -> None:
        ...
    def GetFacetedBody(self, facetBody: Facet.FacetedBody, upToDate: bool) -> None:
        ...
    def SweepabilityCheck(self) -> int:
        ...
    def GetNumberOfFacets(self) -> int:
        ...
    def GetNumberOfVertices(self) -> int:
        ...
    def GetNextFacet(self, facet: ConvergentFacet) -> ConvergentFacet:
        ...
    def GetFirstFacetOnBody(self) -> ConvergentFacet:
        ...
    Density: float
    IsConvergentBody: bool
    IsSheetBody: bool
    IsSolidBody: bool


class BehaviorDef(System.Object):
    def Define(self, access: IDefinitionContext) -> None:
        ...
    def Start(self, context: IRuntimeContext) -> None:
        ...
    def Stop(self, context: IRuntimeContext) -> None:
        ...
    def Step(self, context: IRuntimeContext, dt: float) -> None:
        ...
    def Refresh(self, context: IRuntimeContext) -> None:
        ...
    def Repaint(self) -> None:
        ...
    def __init__(self) -> None: ...


class BasicEffectivityBuilder(TaggedObject):
    def __init__(self) -> None: ...
    def UpdateBuilderDetails(self, cd: CollaborativeDesign, effectivityFormulae: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.PDM.EffectivityTableBuilder instead.")"""
        ...
    def UpdateBuilderDetails(self, cd: CollaborativeDesign, validationBasisFormula: str, effectivityFormulae: str) -> None:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.PDM.EffectivityTableBuilder instead.")"""
        ...
    def Validate(self) -> bool:
        """[Obsolete("Deprecated in NX12.0.0.  Use NXOpen.PDM.EffectivityTableBuilder instead..")"""
        ...
    EffectivityFormula: str
    UnitEffectivityValue: int
    ValidationBasisEffectivityFormula: str


class BasePropertyTable(NXObject):
    def __init__(self) -> None: ...
    def CopyProperties(self, sourceTable: BasePropertyTable) -> None:
        ...
    def GetPropertyCount(self) -> int:
        ...
    def GetPropertyNameByIndex(self, index: int) -> str:
        ...
    def GetBasePropertyType(self, propertyName: str) -> BasePropertyTable.BasePropertyType:
        ...
    def GetStringPropertyValue(self, propertyName: str) -> str:
        ...
    def SetStringPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    def GetFileReferencePropertyValue(self, propertyName: str) -> str:
        ...
    def SetFileReferencePropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    def GetBooleanPropertyValue(self, propertyName: str) -> bool:
        ...
    def SetBooleanPropertyValue(self, propertyName: str, propertyValue: bool) -> None:
        ...
    def GetIntegerPropertyValue(self, propertyName: str) -> int:
        ...
    def SetIntegerPropertyValue(self, propertyName: str, propertyValue: int) -> None:
        ...
    def GetDoublePropertyValue(self, propertyName: str) -> float:
        ...
    def SetDoublePropertyValue(self, propertyName: str, propertyValue: float) -> None:
        ...
    def GetBaseScalarWithDataPropertyValue(self, propertyName: str, propertyValue: float, unitType: Unit) -> None:
        ...
    def SetBaseScalarWithDataPropertyValue(self, propertyName: str, propertyValue: float, unitType: Unit) -> None:
        ...
    def SetBaseScalarWithDataPropertyValue(self, propertyName: str, propertyValue: str, unitType: Unit) -> None:
        ...
    def GetScalarPropertyValue(self, propertyName: str) -> Expression:
        ...
    def SetScalarPropertyValue(self, propertyName: str, propertyValue: Expression) -> None:
        ...
    def GetBaseScalarFieldPropertyValue(self, propertyName: str) -> Fields.FieldExpression:
        ...
    def SetBaseScalarFieldPropertyValue(self, propertyName: str, propertyValue: Fields.FieldExpression) -> None:
        ...
    def GetCoordinateSystemPropertyValue(self, propertyName: str) -> CoordinateSystem:
        ...
    def SetCoordinateSystemPropertyValue(self, propertyName: str, propertyValue: CoordinateSystem) -> None:
        ...
    def GetScalarArrayWithUnitsPropertyValue(self, propertyName: str, propertyValue: float, unitType: Unit) -> None:
        ...
    def SetScalarArrayWithUnitsPropertyValue(self, propertyName: str, propertyValue: float, unitType: Unit) -> None:
        ...
    def GetScalarArrayPropertyValue(self, propertyName: str) -> float:
        ...
    def SetScalarArrayPropertyValue(self, propertyName: str, propertyValue: float) -> None:
        ...
    def GetIntegerArrayPropertyValue(self, propertyName: str) -> int:
        ...
    def SetIntegerArrayPropertyValue(self, propertyName: str, propertyValue: int) -> None:
        ...
    def GetMaterialPropertyValue(self, propertyName: str, materialInherited: bool, material: PhysicalMaterial) -> None:
        ...
    def SetMaterialPropertyValue(self, propertyName: str, materialInherited: bool, material: PhysicalMaterial) -> None:
        ...
    def GetFieldWrapperPropertyValue(self, propertyName: str) -> Fields.FieldWrapper:
        ...
    def SetFieldWrapperPropertyValue(self, propertyName: str, propertyValue: Fields.FieldWrapper) -> None:
        ...
    def GetScalarFieldWrapperPropertyValue(self, propertyName: str) -> Fields.ScalarFieldWrapper:
        ...
    def SetScalarFieldWrapperPropertyValue(self, propertyName: str, propertyValue: Fields.ScalarFieldWrapper) -> None:
        ...
    def GetComplexScalarFieldWrapperPropertyValue(self, propertyName: str) -> Fields.ComplexScalarFieldWrapper:
        ...
    def SetComplexScalarFieldWrapperPropertyValue(self, propertyName: str, propertyValue: Fields.ComplexScalarFieldWrapper) -> None:
        ...
    def AddRowScalarFieldTable(self, propertyName: str) -> None:
        ...
    def DeleteRowScalarFieldTable(self, propertyName: str) -> None:
        ...
    def GetScalarFieldWrapperByIndex(self, iRow: int, iCol: int, propertyName: str) -> Fields.ScalarFieldWrapper:
        ...
    def SetScalarFieldWrapperByIndex(self, iRow: int, iCol: int, propertyName: str, propertyValue: Fields.ScalarFieldWrapper) -> None:
        ...
    def GetScalarFieldTableRowCol(self, propertyName: str, nRows: int, nCols: int) -> None:
        ...
    def GetMatrixPropertyValue(self, propertyName: str) -> ScalarMatrixValue:
        ...
    def SetMatrixPropertyValue(self, propertyName: str, matrix: ScalarMatrixValue) -> None:
        ...
    def GetScalarTablePropertyValue(self, propertyName: str) -> ScalarTableValue:
        ...
    def SetScalarTablePropertyValue(self, propertyName: str, table: ScalarTableValue) -> None:
        ...
    def SetTablePropertyWithoutValue(self, propertyName: str) -> None:
        ...
    def SetTablePropertyOverride(self, propertyName: str) -> None:
        ...
    def ClearTablePropertyOverride(self, propertyName: str) -> None:
        ...
    def CopyProperty(self, propertyName: str, sourcePropertyTable: BasePropertyTable) -> None:
        ...
    def GetComplexVectorFieldWrapperPropertyValue(self, propertyName: str) -> Fields.ComplexVectorFieldWrapper:
        ...
    def SetComplexVectorFieldWrapperPropertyValue(self, propertyName: str, propertyValue: Fields.ComplexVectorFieldWrapper) -> None:
        ...
    def GetIntegerExpressionPropertyValue(self, propertyName: str) -> int:
        ...
    def SetIntegerExpressionPropertyValue(self, propertyName: str, propertyValue: int) -> None:
        ...
    def SetStringOnIntegerExpressionPropertyValue(self, propertyName: str, propertyValue: str) -> None:
        ...
    DescriptorNeutralName: str
    DescriptorSpecificName: str


    class BasePropertyType(enum.Enum):
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
        ScalarFieldTableWrapper = 13
        ComplexScalarFieldWrapper = 14
        ComplexVectorFieldWrapper = 15
        FileReference = 16
    

class BasePart(NXObject):
    def __init__(self) -> None: ...
    def Save(self, saveComponentParts: BasePart.SaveComponents, close: BasePart.CloseAfterSave) -> PartSaveStatus:
        ...
    def SaveAs(self, newFileName: str) -> PartSaveStatus:
        ...
    def AssignPermanentName(self, newFileName: str) -> None:
        ...
    def Reopen(self, wholeTree: BasePart.CloseWholeTree, closeModified: BasePart.CloseModified, responses: PartCloseResponses, reopenReport: PartReopenReport) -> BasePart:
        ...
    def ReopenAs(self, fileName: str, closeModified: BasePart.CloseModified, responses: PartCloseResponses, reopenReport: PartReopenReport) -> BasePart:
        ...
    def Close(self, wholeTree: BasePart.CloseWholeTree, closeModified: BasePart.CloseModified, responses: PartCloseResponses) -> None:
        ...
    def LoadFully(self) -> PartLoadStatus:
        ...
    def LoadThisPartFully(self) -> PartLoadStatus:
        ...
    def LoadThisPartPartially(self) -> PartLoadStatus:
        ...
    def LoadFeatureDataForSelection(self) -> PartLoadStatus:
        ...
    def ReverseBlankAll(self) -> None:
        ...
    def GetHistoryInformation(self) -> typing.List[BasePart.HistoryEventInformation]:
        ...
    def GetPreviewImage(self, width: int, height: int, pixels: int) -> None:
        ...
    def RemoveTransience(self) -> None:
        ...
    def ReinstateTransience(self) -> None:
        ...
    def GetTransientStatus(self) -> BasePart.TransientStatus:
        ...
    def GetIncompleteStatus(self) -> BasePart.IncompleteStatus:
        ...
    def CompleteStructure(self) -> None:
        ...
    def SaveBookmark(self, fileName: str, option: BasePart.BookmarkOption) -> None:
        ...
    def CreateDynamicSectionBuilder(self, loadFromView: bool) -> Display.DynamicSectionBuilder:
        """[Obsolete("Deprecated in NX6.0.0.  Use NXOpen.BasePart.DynamicSections instead.")"""
        ...
    def CreateGatewayGroupBuilder(self, group: Group) -> GroupBuilder:
        ...
    def CreatePerspectiveOptionsBuilder(self) -> Display.PerspectiveOptionsBuilder:
        ...
    def CreateFacetSettingsBuilder(self) -> Display.FacetSettingsBuilder:
        ...
    def RegenerateDisplayFacets(self, regenerateChildren: bool) -> None:
        """[Obsolete("Deprecated in NX11.0.0.  Use NXOpen.BasePart.RegenerateDisplayFacets overload instead.")"""
        ...
    def RegenerateDisplayFacets(self, deleteSavedDisplayFacets: bool, regenerateChildren: bool) -> None:
        ...
    def CreateReferenceSet(self) -> ReferenceSet:
        ...
    def DeleteReferenceSet(self, referenceSetObject: ReferenceSet) -> None:
        ...
    def GetAllReferenceSets(self) -> typing.List[ReferenceSet]:
        ...
    def GetMakeUniqueName(self) -> str:
        ...
    def SetMakeUniqueName(self, newUniqueName: str) -> None:
        ...
    def CreateEffectivityConditionBuilder(self, cd: CollaborativeDesign, effectivityFormula: str) -> EffectivityConditionBuilder:
        ...
    def CreateEffectivityConditionBuilder(self, cd: CollaborativeDesign, validationBasisFormula: str, effectivityFormula: str) -> EffectivityConditionBuilder:
        ...
    def GetCollaborativeContentType(self) -> BasePart.CollaborativeContentType:
        ...
    def CanBeDisplayPart(self) -> bool:
        ...
    def Undisplay(self) -> None:
        ...
    def GetArrangements(self, arrangements: typing.List[Assemblies.Arrangement]) -> None:
        ...
    def HasAnyMinimallyLoadedChildren(self) -> bool:
        ...
    def GetMinimallyLoadedParts(self, minimallyLoadedParts: typing.List[BasePart]) -> None:
        ...
    def DeleteDisplayFacets(self, deleteSavedDisplayFacets: bool, processChildren: bool) -> None:
        ...
    CgfxAttrs: Display.CgfxAttrCollection
    CgfxMattex: Display.CgfxMattexCollection
    WCS: WCS
    Arcs: ArcCollection
    Parabolas: ParabolaCollection
    AnalysisManager: GeometricAnalysis.AnalysisManager
    MeasureManager: MeasureManager
    Layers: Layer.LayerManager
    Xforms: XformCollection
    Offsets: OffsetCollection
    Planes: PlaneCollection
    Hyperbolas: HyperbolaCollection
    Curves: CurveCollection
    Points: PointCollection
    Ellipses: EllipseCollection
    Lines: LineCollection
    InfiniteLines: InfiniteLineCollection
    Splines: SplineCollection
    Polylines: PolylineCollection
    NXMatrices: NXMatrixCollection
    Scalars: ScalarCollection
    Fonts: FontCollection
    Datums: DatumCollection
    Views: ViewCollection
    ExpressionGroups: ExpressionGroupCollection
    Expressions: ExpressionCollection
    ParameterTables: ParameterTableCollection
    UnitCollection: UnitCollection
    Directions: DirectionCollection
    ModelingViews: ModelingViewCollection
    LayerCategories: Layer.CategoryCollection
    RuleManager: RuleManager
    Preferences: Preferences.PartPreferences
    Axes: AxisCollection
    Lights: LightCollection
    Sections: SectionCollection
    ScCollectors: ScCollectorCollection
    ScRuleFactory: ScRuleFactory
    CoordinateSystems: CoordinateSystemCollection
    Layouts: LayoutCollection
    PDMPart: PDM.PdmPart
    Cameras: Display.CameraCollection
    AnimationCameras: Display.AnimationCameraCollection
    DynamicSections: Display.DynamicSectionCollection
    Decals: Display.DecalCollection
    UserDefinedObjectManager: UserDefinedObjects.UserDefinedObjectManager
    Functions: CAE.FunctionCollection
    CaeViewLayoutManager: CAE.ViewLayoutManager
    PostScenarioMgr: CAE.PostScenarioManager
    SelPref: Display.SelPrefCollection
    PlotManager: PlotManager
    PropertiesManager: PropertiesManager
    BaseFeatures: Features.BaseFeatureCollection
    Features: Features.FeatureCollection
    Colors: ColorManager
    Optimization: Optimization.OptimizationCollection
    MaterialManager: MaterialManager
    DesignStudy: Optimization.DesignStudyCollection
    SaveOptions: PartSaveOptions
    Validations: ValidationCollection
    Assemblies: Assemblies.ProductOutlineManager
    AssemblyManager: Assemblies.AssemblyManager
    SHEDObjs: Display.TrueShadingCollection
    TrueStudioObjs: Display.TrueStudioCollection
    Grids: Display.GridCollection
    ImageCaptureManager: Gateway.ImageCaptureManager
    CAMFeatures: CAM.CAMFeatureCollection
    RequirementChecks: Validate.RequirementCheckCollection
    Requirements: Validate.RequirementCollection
    Images: Display.ImageCollection
    ImagesData: Display.ImageDataCollection
    ConvertToPMIBuilderManager: Drawings.ConvertToPMIBuilderManager
    PointClouds: Display.PointCloudCollection
    Annotations: Annotations.AnnotationManager
    ParameterLibraryManager: ParamLibParameterLibraryManager
    ExternalFileReferenceManager: ExternalFileReferenceManager
    AnalysisResults: Validate.AnalysisResultCollection
    PersistentResults: Validate.PersistentResultCollection
    Markups: Markup.MarkupCollection
    ViewSets: ViewSetCollection
    ImplictOperations: Implicit.ImplicitOperationCollection
    Strokes: StrokeCollection
    CheckerData: MendixReporting.CheckerData
    CadInfoManager: MendixReporting.CadInfoManager
    UVMaps: Display.UVMapCollection
    GeometricAnalysisAnalysisResultCollection: GeometricAnalysis.AnalysisResultCollection
    SelectionProgramCollections: Features.SelectionProgramCollection
    LayoutStates: CAE.LayoutStateCollection
    LayoutStatePreferences: CAE.LayoutStatePreferences
    CurveOperationExpRecords: CAE.CurveOperationExpressionRecordCollection
    ComponentAssembly: Assemblies.ComponentAssembly
    Displayed: bool
    FieldManager: Fields.FieldManager
    FullPath: str
    HasWriteAccess: bool
    IsDesignReviewPart: bool
    IsFullyLoaded: bool
    IsModified: bool
    IsReadOnly: bool
    Leaf: str
    PartLoadState: PartLoadState
    PartPreviewMode: BasePart.PartPreview
    PartUnits: BasePart.Units
    SaveDisplayFacets: bool
    UniqueIdentifier: str


    class Units(enum.Enum):
        Inches = 0
        Millimeters = 1
        Mix = 2
    

    class BasePartTransientStatus():
        Trans: bool
        InitiallyTransient: bool
        Locked: bool
        TransientChildren: bool
        def ToString(self) -> str:
            ...
    

    class SaveComponents(enum.Enum):
        False = 0
        True = 1
    

    class PartPreview(enum.Enum):
        None = 0
        OnSave = 1
        OnDemand = 2
    

    class BasePartIncompleteStatus():
        StructIncomplete: bool
        PendIncomplete: bool
        IncompleteChildren: bool
        def ToString(self) -> str:
            ...
        def __init__(self, StructIncomplete: bool, PendIncomplete: bool, IncompleteChildren: bool) -> None: ...
    

    class BasePartHistoryEventInformation():
        Program: str
        User: str
        Machine: str
        Time: str
        Version: int
        def ToString(self) -> str:
            ...
    

    class CollaborativeContentType(enum.Enum):
        Workset = 0
        Subset = 1
        ShapeDesignElement = 2
        OverridePart = 3
        NotAssigned = 4
    

    class CloseWholeTree(enum.Enum):
        False = 0
        True = 1
    

    class CloseModified(enum.Enum):
        UseResponses = 0
        CloseModified = 1
        DontCloseModified = 2
    

    class CloseAfterSave(enum.Enum):
        False = 0
        True = 1
    

    class BookmarkOption(enum.Enum):
        All = 0
        ComponentGroupsLoadOptions = 1
        ComponentGroupsOnly = 2
        AllPlusDisplay = 3
        ComponentGroupsLoadOptionsPlusDisplay = 4
        ComponentGroupsOnlyPlusDisplay = 5
        DisplayOnly = 6
        Empty = 7
    

    class BasePart_HistoryEventInformation():
        program: int
        user: int
        machine: int
        time: int
        version: int
    

class BaseImporter(DexBuilder):
    def __init__(self) -> None: ...
    def GetMode(self) -> BaseImporter.Mode:
        ...
    def SetMode(self, mode: BaseImporter.Mode) -> None:
        ...
    InputFile: str
    OutputFile: str


    class Mode(enum.Enum):
        NativeFileSystem = 0
        Teamcenter = 1
    

class BaseCreator(DexBuilder):
    def __init__(self) -> None: ...
    DatasetName: str
    ExportDestination: BaseCreator.ExportDestinationOption
    OutputFile: str
    OutputFileExtension: str


    class ExportDestinationOption(enum.Enum):
        NativeFileSystem = 0
        Teamcenter = 1
    

class BallJoint(Joint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    Anchor: VectorArithmetic.Vector3
    Active: bool


    class BallJoint.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class AxisOrientation(enum.Enum):
    Horizontal = 0
    Vertical = 1


class AxisJointLimit(ControlBase):
    def __init__(self, pItem: int) -> None: ...
    Active: bool
    Axis: AxisJoint
    UpperLimit: float
    LowerLimit: float


    class AxisJointLimit.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class AxisJoint(Joint):
    def __init__(self, pItem: int) -> None: ...
    def GetAngularAcceleration(self) -> float:
        ...
    def GetLinearAcceleration(self) -> float:
        ...
    Axis: VectorArithmetic.Vector3


class AxisConstraint(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    def GetForce(self) -> VectorArithmetic.Vector3:
        ...
    def GetTorque(self) -> VectorArithmetic.Vector3:
        ...


class AxisCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Axis]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def CreateAxis(self, point: Point, direction: Direction, update: SmartObject.UpdateOption) -> Axis:
        ...
    def CreateAxis(self, point: Point3d, direction: Vector3d, update: SmartObject.UpdateOption) -> Axis:
        ...
    def CreateAxis(self, axis: Axis, xform: Xform, update: SmartObject.UpdateOption) -> Axis:
        ...
    def Tag(self) -> Tag: ...



class Axis(SmartObject):
    def __init__(self) -> None: ...
    def SetOrigin(self, origin: Point3d) -> None:
        ...
    def SetDirectionVector(self, vector: Vector3d) -> None:
        ...
    Direction: Direction
    DirectionVector: Vector3d
    Origin: Point3d
    Point: Point
    Type: Axis.Types


    class Types(enum.Enum):
        NonAssociative = 0
        PointAndDirection = 1
        Other = 2
    

class AutomaticTraceline(Traceline):
    def __init__(self) -> None: ...
    def GetSegmentConstraints(self, segmentIndices: int, segmentLengths: float) -> None:
        ...
    def SetSegmentConstraints(self, segmentIndices: int, segmentLengths: float) -> None:
        ...
    def RemoveSegmentConstraint(self, segmentIndex: int) -> None:
        ...
    EndDirection: Direction
    EndOffset: float
    EndPoint: Point
    Mode: AutomaticTraceline.ModeOption
    Orientation: Matrix3x3
    Solution: int
    StartDirection: Direction
    StartOffset: float
    StartPoint: Point


    class ModeOption(enum.Enum):
        Evaluate = 0
        Orientation = 1
        Infer = 2
    

class AutoInstallTest(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def GetAutoInstallTest(self, owner: Session) -> AutoInstallTest:
        ...
    def SetAutoAuthenticationFlag(self, autoAuthenticate: bool) -> None:
        ...
    def SetVersionInfo(self, versionInfo: AutoInstallTest.CustomVersionInfo) -> AutoInstallTest.ReturnParams:
        ...
    def GetUpdateStatus(self, state: int, baseCompatibleVersion: int, releasenotesLink: str) -> AutoInstallTest.ReturnParams:
        ...
    def ValidateDownloadedUpdate(self, failOnCertError: bool, certError: str) -> AutoInstallTest.ReturnParams:
        ...
    def StartDownload(self, downloadLocation: str) -> AutoInstallTest.ReturnParams:
        ...
    def GetDownloadProgress(self, progress: int) -> AutoInstallTest.ReturnParams:
        ...
    def StartInstall(self) -> AutoInstallTest.ReturnParams:
        ...
    def GetNotifications(self, notifications: typing.List[AutoInstallTest.Notifications]) -> AutoInstallTest.ReturnParams:
        ...
    def AcknowledgeNotifications(self, notificationsToAcknowledege: typing.List[AutoInstallTest.Notifications]) -> typing.List[AutoInstallTest.ReturnParams]:
        ...
    def CompareResponse(self, responseString: str, pathOfFile: str) -> bool:
        ...
    def Tag(self) -> Tag: ...



    class AutoInstallTestReturnParams():
        ReturnCode: int
        ResponseString: str
        def ToString(self) -> str:
            ...
        def __init__(self, ReturnCode: int, ResponseString: str) -> None: ...
    

    class AutoInstallTestNotifications():
        Id: str
        CreationDate: str
        def ToString(self) -> str:
            ...
        def __init__(self, Id: str, CreationDate: str) -> None: ...
    

    class AutoInstallTestCustomVersionInfo():
        VersionNumber: int
        BuildNumber: int
        CustomerPatch: int
        CustomerId: int
        ProductName: str
        ChannelType: str
        def ToString(self) -> str:
            ...
    

    class AutoInstallTest_ReturnParams():
        returnCode: int
        responseString: int
    

    class AutoInstallTest_Notifications():
        id: int
        creationDate: int
    

    class AutoInstallTest_CustomVersionInfo():
        versionNumber: int
        buildNumber: int
        customerPatch: int
        customerId: int
        productName: int
        channelType: int
    

class AttributeTemplatesBuilder(Builder):
    def __init__(self) -> None: ...
    def GetIntegerList(self) -> str:
        ...
    def SetIntegerList(self, integerList: str) -> None:
        ...
    def GetNumberList(self) -> str:
        ...
    def SetNumberList(self, numberList: str) -> None:
        ...
    def GetStringList(self) -> str:
        ...
    def SetStringList(self, stringList: str) -> None:
        ...
    def GetNote(self) -> str:
        ...
    def SetNote(self, note: str) -> None:
        ...
    def ImportCatalog(self) -> None:
        ...
    def ExportCatalog(self) -> None:
        ...
    def UpdateTemplates(self) -> None:
        ...
    def Delete(self, title: str, type: AttributePropertiesBaseBuilder.DataTypeOptions) -> bool:
        ...
    def GetAccessKeys(self) -> typing.List[AttributeTemplatesBuilder.AccessKey]:
        ...
    def SetAccessKeys(self, accessKeys: typing.List[AttributeTemplatesBuilder.AccessKey]) -> None:
        ...
    def AddAccessKey(self, accessKey: AttributeTemplatesBuilder.AccessKey) -> None:
        ...
    def RemoveAccessKey(self, accessKey: AttributeTemplatesBuilder.AccessKey) -> None:
        ...
    Alias: str
    AllowMultipleValues: bool
    CatalogFilename: str
    Category: str
    Constraint: AttributeTemplatesBuilder.ConstraintOptions
    CopyAttributeOnObjectCopy: bool
    DataType: AttributePropertiesBaseBuilder.DataTypeOptions
    DateConstraint: DateBuilder
    DefaultBoolean: AttributeTemplatesBuilder.DefaultBooleanOptions
    DefaultDate: DateBuilder
    DefaultInteger: int
    DefaultNumber: float
    DefaultString: str
    EnforcedConstraints: bool
    LockOnSave: bool
    MaxInteger: int
    MaxNumber: float
    MaxString: str
    MinInteger: int
    MinNumber: float
    MinString: str
    Persistent: bool
    ProxyAttributeForLocking: str
    Templates: AttributeTemplatesBuilder.TemplatesOptions
    Title: str
    Units: str


    class TemplatesOptions(enum.Enum):
        Part = 0
        Catalog = 1
    

    class DefaultBooleanOptions(enum.Enum):
        True = 0
        False = 1
    

    class ConstraintOptions(enum.Enum):
        None = 0
        UpperLimit = 1
        LowerLimit = 2
        UpperAndLowerLimit = 3
        List = 4
    

    class AccessKey(enum.Enum):
        Part = 0
        ReferenceSet = 1
        ComponentInstance = 2
        ComponentOccurrence = 3
        Objects = 4
    

class AttributePropertiesBuilder(AttributePropertiesBaseBuilder):
    def __init__(self) -> None: ...


    class OperationType(enum.Enum):
        None = -1
        Create = 0
        Revise = 1
        SaveAs = 2
        Save = 3
        Delete = 4
    

class AttributePropertiesBaseBuilder(Builder):
    def __init__(self) -> None: ...
    def Delete(self, object: NXObject) -> None:
        ...
    def DeleteArray(self, object: NXObject) -> None:
        ...
    def CreateAttribute(self) -> bool:
        ...
    def ApplyUnits(self) -> bool:
        ...
    def SetAttributeObjects(self, objects: typing.List[NXObject]) -> None:
        ...
    ArrayIndex: int
    BooleanValue: AttributePropertiesBaseBuilder.BooleanValueOptions
    Category: str
    DataType: AttributePropertiesBaseBuilder.DataTypeOptions
    DateValue: DateBuilder
    Expression: Expression
    IntegerValue: int
    IsArray: bool
    IsReferenceType: bool
    LockOnSave: bool
    NumberValue: float
    ObjectPicker: AttributePropertiesBaseBuilder.ObjectOptions
    SelectedObjects: SelectNXObjectList
    StringValue: str
    Title: str
    Units: str
    ValueAlias: str


    class ObjectOptions(enum.Enum):
        Object = 0
        Feature = 1
        Occurrence = 2
        ComponentInstance = 3
        ReferenceSet = 4
        ObjectInComponentPart = 5
        ComponentAsPartAttribute = 6
        Empty = 7
    

    class DataTypeOptions(enum.Enum):
        Null = 0
        Boolean = 1
        Integer = 2
        Number = 3
        String = 4
        Date = 5
    

    class BooleanValueOptions(enum.Enum):
        False = 0
        True = 1
    

class AttributeManager(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def CreateAttributePropertiesBuilder(self, part: BasePart, objects: typing.List[NXObject], operationType: AttributePropertiesBuilder.OperationType) -> AttributePropertiesBuilder:
        ...
    def Tag(self) -> Tag: ...



class AttributeIterator(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def SetIncludeOnlyType(self, type: NXObject.AttributeType) -> None:
        ...
    def SetIncludeOnlyCategory(self, category: str) -> None:
        ...
    def SetIncludeAllCategories(self) -> None:
        ...
    def SetIncludeOnlyTitle(self, title: str) -> None:
        ...
    def SetIncludeAlsoUnset(self, includeAlsoUnset: bool) -> None:
        ...
    def SetIncludeOnlyUnset(self, includeOnlyUnset: bool) -> None:
        ...
    def SetIncludeOnlyArrays(self, includeOnlyArrays: bool) -> None:
        ...
    def Rewind(self) -> None:
        ...
    def Reset(self) -> None:
        ...
    def FreeResource(self) -> None:
        ...


class AssyCloneNamingFailures(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetNumberOfFailures(self) -> int:
        ...
    def GetInputPartName(self, partListIndex: int) -> str:
        ...
    def GetOutputPartName(self, partListIndex: int) -> str:
        ...
    def GetStatus(self, partListIndex: int) -> int:
        ...


class AssyCloneLogFileFailures(TransientObject):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetLineNumber(self) -> int:
        ...
    def GetInputPartName(self) -> str:
        ...
    def GetInvalidToken(self) -> str:
        ...


class AssembliesUtils(Utilities.NXRemotableObject):
    def __init__(self, owner: Session) -> None: ...
    def NewWaveQuery(self) -> Assemblies.WaveQuery:
        ...
    def Tag(self) -> Tag: ...



class ASCImporter(Builder):
    def __init__(self) -> None: ...
    InputFile: str
    OutputFile: str
    PartUnitsEnum: ASCImporter.Units
    SheetGeometryToSketch: bool
    ViewGeometryToSketch: bool


    class Units(enum.Enum):
        Millimeters = 0
        Inches = 1
    

class ArcCollection(TaggedObjectCollection):
    def EnumerateMoveNext(self, currentTag: Tag, state: bytes) -> int:
        ...
    def ToArray(self) -> typing.List[Arc]:
        ...
    def __init__(self, owner: BasePart) -> None: ...
    def __init__(self) -> None: ...
    def FindObject(self, journalIdentifier: str) -> Arc:
        ...
    def Tag(self) -> Tag: ...



class Arc(Conic):
    def __init__(self) -> None: ...
    def SetRadius(self, radius: float) -> None:
        ...
    def SetParameters(self, radius: float, center: Point3d, startAngle: float, endAngle: float, matrix: NXMatrix) -> None:
        ...
    def SetParameters(self, radius: float, center: Point3d, startAngle: float, endAngle: float) -> None:
        ...
    EndAngle: float
    Radius: float
    StartAngle: float


class ApparentChainingRuleType(enum.Enum):
    Connected = 0
    Tangent = 1
    Dumb = 2


class ApparentChainingRuleSelection(enum.Enum):
    AllowAllTypes = 0
    AllowCurve = 1
    AllowEdge = 2


class ApparentChainingRule(SelectionIntentRule):
    def __init__(self, ptr: int) -> None: ...
    def FreeResource(self) -> None:
        ...
    def GetData(self, seed: ICurve, view: View, chainingRule: ApparentChainingRuleType, selectionMask: ApparentChainingRuleSelection, chainingTolerance: float, angleTolerance: float) -> None:
        ...


class AngularSpring(SpringJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    AttachVector: VectorArithmetic.Vector3
    BaseVector: VectorArithmetic.Vector3
    SpringConstant: float
    Damping: float
    RelaxedPosition: float
    Active: bool


    class AngularSpring.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class AngularLimit(LimitJoint):
    def __init__(self, pItem: int) -> None: ...
    Attach: RigidBody
    Base: RigidBody
    AttachVector: VectorArithmetic.Vector3
    BaseVector: VectorArithmetic.Vector3
    Minimum: float
    Maximum: float
    Active: bool


    class AngularLimit.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class AngularGripper(Gripper):
    def __init__(self, pItem: int) -> None: ...
    Grip: bool
    Release: bool
    IsOpened: bool
    IsClosed: bool
    StopGrippingAction: bool
    GrippedObject: RigidBody
    HasGrippedObject: bool
    FingerPosition: float
    Speed: float
    MaxPosition: float
    Active: bool


    class AngularGripper.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class AlignmentStyleT(enum.Enum):
    None = 0
    Horizontal = 1
    Vertical = 2


class AlignBody(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    AssociatedBody: RigidBody
    Point: VectorArithmetic.Vector3
    Proximity: float
    Detection: AlignBody
    Detected: bool
    Role: str
    Category: int
    EnableBond: bool
    Bond: bool
    Active: bool


    class AlignBody.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

class AcisImporter(BaseImporter):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    FileOpenFlag: bool
    HealBodies: bool
    IncludeWires: bool
    Optimize: bool
    SettingsFile: str
    Sew: bool
    SimplifyGeometry: bool


class AcisExporter(BaseCreator):
    def __init__(self) -> None: ...
    def SaveSettings(self, filename: str) -> None:
        ...
    AcisVersion: AcisExporter.AcisVersionOption
    ExportSelectionBlock: ObjectSelector
    FileSaveFlag: bool
    SettingsFile: str


    class AcisVersionOption(enum.Enum):
        V2021 = 0
        V2020 = 1
        R29 = 2
        R28 = 3
        R27 = 4
        R26 = 5
        R25 = 6
        R24 = 7
        R23 = 8
        R22 = 9
        R21 = 10
        R20 = 11
        R19 = 12
        R18 = 13
    

class Accelerometer(RuntimeObject):
    def __init__(self, pItem: int) -> None: ...
    Linear_Accelerometer: VectorArithmetic.Vector3
    Angular_Accelerometer: VectorArithmetic.Vector3
    Active: bool


    class Accelerometer.Factory(System.Object):
        def Create(self, pItem: int) -> RuntimeObject:
            ...
        def __init__(self) -> None: ...
    

