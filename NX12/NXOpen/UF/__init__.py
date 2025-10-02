from ...NXOpen import *
from ..UF import *

import typing
import enum

class XUdoViewInfo():
    view_tag: Tag
    view_name: str
    view_cntr: float
    view_borders: float
    view_scale: float
    udo_tag: Tag


class UnitMeasureType(enum.Enum):
    MeasureInvalid = -2
    MeasureUnitless = -1
    MeasureLength = 0
    MeasureArea = 1
    MeasureVolume = 2
    MeasureMass = 3
    MeasureMassDensity = 4
    MeasureFatigueStrengthCoeff = 5
    MeasureTime = 6
    MeasureAngle = 7
    MeasureVelocity = 8
    MeasureAcceleration = 9
    MeasureForce = 10
    MeasureForcePerLength = 11
    MeasureForcePerArea = 12
    MeasureMoment = 13
    MeasureStress = 14
    MeasureStrain = 15
    MeasureStrainEnergy = 16
    MeasureStrainEnergyDensity = 17
    MeasureTemperature = 18
    MeasureHeatFlux = 19
    MeasureConvectionCoeff = 20
    MeasureThermalConductivity = 21
    MeasureThermalExpansionCoeff = 22
    MeasureSpecificHeat = 23
    MeasureAngularVelocity = 24
    MeasureAngularAcceleration = 25
    MeasureFatigueLife = 26
    MeasureHeatFlow = 27
    MeasureThermalEnergy = 28
    MeasureMassMomentInertia = 29
    MeasureDynamicViscosity = 30
    MeasureHeatGeneration = 31
    MeasureConductance = 32
    MeasureLengthConductance = 33
    MeasureThermalResistance = 34
    MeasureMassFlow = 35
    MeasureVolumeFlow = 36
    MeasureTemperatureDifference = 37
    MeasureFrequency = 38
    MeasureCoefficientLength = 39
    MeasureMomentOfInertiaArea = 40
    MeasureViscousDamping = 41
    MeasureEnergy = 42
    MeasurePower = 43
    MeasureMomentum = 44
    MeasureTemperatureGradient = 45
    MeasureEnergyPerMass = 46
    MeasureDissipationRateOfEnergyPerMass = 47
    MeasureMassFlux = 48
    MeasureMassPerLength = 49
    MeasureMassPerArea = 50
    MeasureElectricCurrent = 51
    MeasureElectricalResistance = 52
    MeasureElectricalResistivity = 53
    MeasureElectricalConductance = 54
    MeasureVoltage = 55
    MeasureVoltagePerTemperature = 56
    MeasureDiffusivity = 57
    MeasureLatentHeatPerMass = 58
    MeasureThermalEnergyPerArea = 59
    MeasureThermalPidGain = 60
    MeasureThermalPidIntegral = 61
    MeasureThermalPidDerivative = 62
    MeasureHeadlossCoeff = 63
    MeasureTsaiWuCoeff = 64
    MeasureMassLength = 65
    MeasurePerVolume = 66
    MeasureWarpingConstant = 67
    MeasureStressCompliance = 68
    MeasureLengthPerPressure = 69
    MeasurePressurePerLength = 70
    MeasurePressurePerVelocity = 71
    MeasureMomentPerAngle = 72
    MeasureCoefficientPerTime = 73
    MeasureAngularMomentumPerAngle = 74
    MeasureThermalCapacitance = 75
    MeasureInductance = 76
    MeasureVoltagePerAngularVelocity = 77
    MeasurePerArea = 78
    MeasureTemperatureChangeRate = 79
    MeasureJerk = 80
    MeasureAngularJerk = 81
    MeasureMagneticFieldStrength = 82
    MeasureMagneticFluxDensity = 83
    MeasureAngularMomentum = 84
    MeasureVelocityPerPressure = 85
    MeasureCoefficientPerTimeSquared = 86
    MeasureCoefficientPerTimeCubed = 87
    MeasureFlowResistivity = 88
    MeasureCurrentDensity = 89
    MeasureForcePerAngle = 90
    MeasureLengthPerAngle = 91
    MeasureCurrentDensityArea = 92
    MeasureElectricFieldStrength = 93
    MeasureElectricFluxDensity = 94
    MeasureElectricCharge = 95
    MeasureLuminousIntensity = 96
    MeasureLuminousFlux = 97
    MeasureLuminance = 98
    MeasureIlluminance = 99
    MeasureAmountOfSubstance = 100
    MeasureMolality = 101
    MeasureMolarConcentration = 102
    MeasurePerFrequency = 103
    MeasureDiffusionResistance = 104
    MeasureTransmissionLoss = 105
    MeasureCount = 106
    MeasureCustom = 5000


class UiMessageDialogType(enum.Enum):
    UiMessageError = 0
    UiMessageWarning = 1
    UiMessageInformation = 2
    UiMessageQuestion = 3


class UiMenuType(enum.Enum):
    UiMenu = 1
    UiCascadeMenu = 2
    UiPush = 3
    UiToggle = 4
    UiButtonSeparator = 5
    UiEndCustomCascadeMenu = 6
    UiEndCustomMenu = 7


class UgmgrAttrInfo():
    create_descriptor: bool
    key_identifier: bool
    basic_info: UF.UFAttr.Info


class UFXs(Utilities.NXRemotableObject):
    def ExtractSpreadsheet(self, spreadsheet_name: str, file_name: str) -> None:
        ...
    def StoreSpreadsheet(self, spreadsheet_name: str, file_name: str) -> None:
        ...


class UFWeld(Utilities.NXRemotableObject):
    def AskBodyId(self, feature_set_tag: Tag, body_id: typing.List[Tag], num_objects: int) -> None:
        ...
    def AskGrooveOrEdgeGuide(self, weld_feat_tag: Tag, guide_crv_cnt: typing.List[Tag], guide_curves: typing.List[Tag]) -> None:
        ...
    def AskGuideCurves(self, weld_feat_tag: Tag, guide_crv_cnt: int, guide_curves: typing.List[Tag]) -> None:
        ...
    def AskLinkedFaceParent(self, face_tag: Tag, source_obj: Tag) -> None:
        ...
    def AskLinkedFeatSource(self, linked_feat_tag: Tag, source_obj: Tag) -> None:
        ...
    def AskNumberOfWelds(self, feature_set_tag: Tag, num_of_welds: int) -> None:
        ...
    def AskSeamWeldInfo(self, seam_feature_set: Tag, seam_count: int, seam_id: typing.List[Tag], num_sets: int, n_faces_in_each_set: int, set_of_faces: typing.List[Tag[]]) -> None:
        ...
    def AskSegmentLenOfWelds(self, feature_set_tag: Tag, seg_len: float) -> None:
        ...
    def AskSpacingOfWelds(self, feature_set_tag: Tag, spacing: float) -> None:
        ...
    def AskSpotFaceData(self, spot_feature_set: Tag, num_sets: int, spot_count: int, spot_info: typing.List[UF.UFWeld.SpotInfo]) -> None:
        ...
    def AskSpotFaceInfo(self, spot_feature_set: Tag, num_sets: int, spot_count: int, spot_info: typing.List[UF.UFWeld.SpotData]) -> None:
        ...
    def AskSpotWeldInfo(self, spot_feature_set: Tag, top_body: Tag, spot_count: int, spot_points: typing.List[Tag], num_sets: int, n_faces_in_each_set: int, set_of_faces: typing.List[Tag[]]) -> None:
        ...
    def IsObjectWeld(self, _object: Tag, is_weld: bool, feature_set_tag: Tag) -> None:
        ...
    def LocateWelds(self, work_part: Tag, weld_type: UF.UFWeld.Types, count: int, weld_array: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def PopulateAttrList(self, feature_set_tag: Tag, attribute_title: str, count: int) -> None:
        ...


    class Types(enum.Enum):
        FilletType = 1
        GrooveType = 2
        EdgeType = 4
        PlugType = 8
        SlotType = 16
        ArcSpotType = 32
        SpotType = 64
        SeamType = 128
        TapeType = 256
        BeadType = 512
        DollopType = 1024
        ClinchType = 2048
        FilletNaType = 4096
        GrooveNaType = 8192
        EdgeNaType = 16384
        PlugNaType = 32768
        SlotNaType = 65536
        ArcSpotNaType = 131072
        SpotNaType = 262144
        SeamNaType = 524288
        TapeNaType = 1048576
        BeadNaType = 2097152
        DollopNaType = 4194304
        ClinchNaType = 8388608
        UF_FILLET_WELD_TYPE = 16777216
        AllTypes = 33554431
    

    class UFWeldSpotInfo():
        spot_point: Tag
        face_loc: typing.List[UF.UFWeld.SpotFaceLocation]
    

    class UFWeldSpotFaceLocation():
        face_tag: Tag
        point: float
        face_normal: float
    

    class UFWeldSpotFaceLoc():
        face_tag: Tag
        point: float
        face_normal: float
        face_handle: str
    

    class UFWeldSpotData():
        spot_point: Tag
        face_loc: typing.List[UF.UFWeld.SpotFaceLoc]
    

class UFWeight(Utilities.NXRemotableObject):
    def AskPartCset(self, part: Tag, cset_name: str) -> None:
        ...
    def AskPartMaxWeight(self, part: Tag, units: UF.UFWeight.UnitsType, max_weight: float, is_set: bool) -> None:
        ...
    def AskPartMinWeight(self, part: Tag, units: UF.UFWeight.UnitsType, min_weight: float, is_set: bool) -> None:
        ...
    def AskPartRefSet(self, part: Tag, ref_set_name: str) -> None:
        ...
    def AskPartSaveOption(self, part: Tag, update_on_save: bool) -> None:
        ...
    def AskProps(self, _object: Tag, units: UF.UFWeight.UnitsType, properties: UF.UFWeight.Properties) -> None:
        ...
    def AssertCompProps(self, component: Tag, properties: UF.UFWeight.Properties) -> None:
        ...
    def AssertPartProps(self, part: Tag, properties: UF.UFWeight.Properties) -> None:
        ...
    def ConvertPropUnits(self, old_properties: UF.UFWeight.Properties, new_units: UF.UFWeight.UnitsType, new_properties: UF.UFWeight.Properties) -> None:
        ...
    def CopyProps(self, properties: UF.UFWeight.Properties, new_properties: UF.UFWeight.Properties) -> None:
        ...
    def DeleteCompAssertion(self, component: Tag) -> None:
        ...
    def DeletePartAssertion(self, part: Tag) -> None:
        ...
    def EstabCompProps(self, component: Tag, accuracy: float, recurse: bool, units: UF.UFWeight.UnitsType, properties: UF.UFWeight.Properties, exceptions: UF.UFWeight.Exceptions) -> None:
        ...
    def EstabCompProps1(self, component: Tag, accuracy: float, recurse: bool, units: UF.UFWeight.UnitsType, properties: UF.UFWeight.Properties, exceptions: typing.List[UF.UFWeight.Exceptions]) -> None:
        ...
    def EstabPartProps(self, part: Tag, accuracy: float, recurse: bool, units: UF.UFWeight.UnitsType, properties: UF.UFWeight.Properties, exceptions: UF.UFWeight.Exceptions) -> None:
        ...
    def EstabPartProps1(self, part: Tag, accuracy: float, recurse: bool, units: UF.UFWeight.UnitsType, properties: UF.UFWeight.Properties, exceptions: typing.List[UF.UFWeight.Exceptions]) -> None:
        ...
    def EstabSolidProps(self, solid: Tag, accuracy: float, units: UF.UFWeight.UnitsType, properties: UF.UFWeight.Properties) -> None:
        ...
    def FreeExceptions(self, exceptions: UF.UFWeight.Exceptions) -> None:
        ...
    def InitExceptions(self, exceptions: UF.UFWeight.Exceptions) -> None:
        ...
    def SetPartCset(self, part: Tag, cset_name: str) -> None:
        ...
    def SetPartMaxWeight(self, part: Tag, max_weight: float, units: UF.UFWeight.UnitsType) -> None:
        ...
    def SetPartMinWeight(self, part: Tag, min_weight: float, units: UF.UFWeight.UnitsType) -> None:
        ...
    def SetPartRefSet(self, part: Tag, ref_set_name: str) -> None:
        ...
    def SetPartSaveOption(self, part: Tag, update_on_save: bool) -> None:
        ...
    def SumProps(self, count: int, properties_array: typing.List[UF.UFWeight.Properties], total_properties: UF.UFWeight.Properties) -> None:
        ...
    def TransformProps(self, transform: float, properties: UF.UFWeight.Properties, transformed_properties: UF.UFWeight.Properties) -> None:
        ...
    def UnsetPartMaxWeight(self, part: Tag) -> None:
        ...
    def UnsetPartMinWeight(self, part: Tag) -> None:
        ...


    class UnitsType(enum.Enum):
        UnitsKm = 0
        UnitsLi = 1
        UnitsLf = 2
        UnitsGm = 3
        UnitsGc = 4
        UnitsCustom = 5
        UnitsKmm = 6
    

    class StateType(enum.Enum):
        NoCache = 0
        Cached = 1
        Asserted = 2
        Unknown = 3
        Inherited = 4
        Implied = 6
    

    class UFWeightProperties():
        units: UF.UFWeight.UnitsType
        cache_state: UF.UFWeight.StateType
        accuracy: float
        density: float
        density_state: UF.UFWeight.StateType
        volume: float
        volume_error: float
        volume_state: UF.UFWeight.StateType
        mass: float
        mass_error: float
        mass_state: UF.UFWeight.StateType
        area: float
        area_error: float
        area_state: UF.UFWeight.StateType
        center_of_mass: float
        cofm_error: float
        cofm_state: UF.UFWeight.StateType
        moments_of_inertia: float
        products_of_inertia: float
        mofi_error: float
        mofi_state: UF.UFWeight.StateType
    

    class UFWeightExceptions():
        n_exceptions: int
        reasons: typing.List[UF.UFWeight.ExceptionReason]
        part_names: str
        comp_names: str
        on_part: bool
        repeat_counts: int
    

    class ExceptionReason(enum.Enum):
        NotLoaded = 1
        InsufficientlyLoaded = 2
        RefSetAbsent = 3
        CompSetAbsent = 4
        UnderMinimumWeight = 8
        OverMaximumWeight = 9
        HasAssertion = 11
        InsufficientAccuracy = 12
        IncompletePart = 15
        CompGroupNotUptodate = 16
        CompGroupUpdatedSuccessfully = 17
        ReferenceOnlyComponent = 18
        ExcludedFromSpatialSearch = 19
        PromotionWithSourceSuppressed = 20
    

class UFWeb(Utilities.NXRemotableObject):
    def AuthorHtml(self, output_filename: str, template_filename: str, apply_to_each_component: int) -> None:
        ...
    def WriteToFile(self, output_string: str) -> None:
        ...


class UFWave(Utilities.NXRemotableObject):
    def AcceptLinkBroken(self, linked_feature: Tag) -> None:
        ...
    def AskBrokenLinkSourcePart(self, broken_link: Tag, part_name: str, source_object_handle: str) -> None:
        ...
    def AskDelayStatus(self, part: Tag, delay_status: UF.UFWave.DelayStatus) -> None:
        ...
    def AskLinkAcceptBroken(self, linked_feature: Tag, is_accepted: bool) -> None:
        ...
    def AskLinkMirrorData(self, linked_feature: Tag, allow_load: bool, source_body: Tag, body_xform: Tag, datum_plane: Tag, datum_xform: Tag) -> None:
        ...
    def AskLinkRegionSources(self, linked_feature: Tag, allow_load: bool, n_seed_faces: int, seed_faces: typing.List[Tag], n_boundary_faces: int, boundary_faces: typing.List[Tag], traverse_interior_edges: bool, delete_openings: bool) -> None:
        ...
    def AskLinkSource(self, linked_feature: Tag, allow_load: bool, source_entity: Tag) -> None:
        ...
    def AskLinkUpdateTime(self, linked_feature: Tag, allow_load: bool, timestamp_feature: Tag) -> None:
        ...
    def AskLinkXform(self, linked_feature: Tag, xform: Tag) -> None:
        ...
    def AskLinkedFeatureGeom(self, linked_feature: Tag, linked_geom: Tag) -> None:
        ...
    def AskLinkedFeatureInfo(self, linked_geom: Tag, name_store: UF.UFWave.LinkedFeatureInfo) -> None:
        ...
    def AskLinkedFeatureMap(self, linked_feature: Tag, allow_load: bool, n_map_items: int, source_geom: typing.List[Tag], linked_geom: typing.List[Tag]) -> None:
        ...
    def AskLinkedPtAngle(self, linked_feature: Tag, angle: Tag) -> None:
        ...
    def AskLinkedPtCurvePrm(self, linked_feature: Tag, prm: Tag) -> None:
        ...
    def AskOutOfDateObjects(self, part: Tag, n_objects: int, objects: typing.List[Tag]) -> None:
        ...
    def AskOutOfDateParts(self, n_parts: int, parts: typing.List[Tag]) -> None:
        ...
    def AskSessionDelay(self, delayed: bool) -> None:
        ...
    def ConvertLinksToUseProductInterface(self) -> None:
        ...
    def CopyComponentAs(self, source_part_occurrence: Tag, source_part_name: str, new_part_name: str, reference_set_name: str, instance_name: str, transform: float, new_instance: Tag, new_part: Tag) -> None:
        ...
    def CreateLinkedBody(self, body: Tag, xform: Tag, object_in_part: Tag, update_at_timestamp: bool, linked_feature: Tag) -> None:
        ...
    def CreateLinkedCurve(self, curve: Tag, xform: Tag, object_in_part: Tag, update_at_timestamp: bool, linked_feature: Tag) -> None:
        ...
    def CreateLinkedDatum(self, datum: Tag, xform: Tag, object_in_part: Tag, linked_feature: Tag) -> None:
        ...
    def CreateLinkedFace(self, face: Tag, xform: Tag, object_in_part: Tag, update_at_timestamp: bool, linked_feature: Tag) -> None:
        ...
    def CreateLinkedMirror(self, body: Tag, body_xform: Tag, datum_plane: Tag, datum_xform: Tag, object_in_part: Tag, update_at_timestamp: bool, linked_feature: Tag) -> None:
        ...
    def CreateLinkedPart(self, start_part: Tag, ref_set: Tag, linked_part_name: str, linked_part: Tag) -> None:
        ...
    def CreateLinkedPtAngle(self, arc: Tag, angle: Tag, xform: Tag, object_in_part: Tag, linked_feature: Tag) -> None:
        ...
    def CreateLinkedPtCenter(self, conic: Tag, xform: Tag, object_in_part: Tag, linked_feature: Tag) -> None:
        ...
    def CreateLinkedPtCurve(self, curve: Tag, prm: Tag, xform: Tag, object_in_part: Tag, linked_feature: Tag) -> None:
        ...
    def CreateLinkedPtPoint(self, point: Tag, xform: Tag, object_in_part: Tag, linked_feature: Tag) -> None:
        ...
    def CreateLinkedRegion(self, n_seed_faces: int, seed_faces: typing.List[Tag], n_boundary_faces: int, boundary_faces: typing.List[Tag], xform: Tag, object_in_part: Tag, update_at_timestamp: bool, traverse_interior_edges: bool, delete_openings: bool, linked_feature: Tag) -> None:
        ...
    def CreateLinkedRoutePort(self, port: Tag, xform: Tag, object_in_part: Tag, linked_port_feature: Tag) -> None:
        ...
    def CreateLinkedRouteSegment(self, segment: Tag, xform: Tag, object_in_part: Tag, linked_curve_feature: Tag, linked_segment: Tag) -> None:
        ...
    def CreateLinkedSketch(self, sketch: Tag, xform: Tag, object_in_part: Tag, linked_feature: Tag) -> None:
        ...
    def CreateLinkedString(self, _string: Tag, xform: Tag, object_in_part: Tag, linked_feature: Tag) -> None:
        ...
    def FreeLinkedFeatureInfo(self, name_store: UF.UFWave.LinkedFeatureInfo) -> None:
        ...
    def Freeze(self, n_parts: int, parts: typing.List[Tag]) -> None:
        ...
    def FreezePersistently(self, n_parts: int, parts: typing.List[Tag]) -> None:
        ...
    def InitLinkedFeatureInfo(self, name_store: UF.UFWave.LinkedFeatureInfo) -> None:
        ...
    def IsLinkBroken(self, linked_feature: Tag, is_broken: bool) -> None:
        ...
    def IsPiloXform(self, xform: Tag) -> bool:
        ...
    def LoadParents(self, part: Tag, parent_option: int, n_failures: int, failing_parts: str, failing_statuses: int) -> int:
        ...
    def MapLinkGeomToSource(self, linked_feature: Tag, linked_geom: Tag, allow_load: bool, source_geom: Tag) -> None:
        ...
    def MapSourceToLinkGeom(self, linked_feature: Tag, source_geom: Tag, linked_geom: Tag) -> None:
        ...
    def SetLinkData(self, linked_feature: Tag, source_entity: Tag, xform: Tag, update_at_timestamp: bool) -> None:
        ...
    def SetLinkMirrorData(self, linked_feature: Tag, source_body: Tag, body_xform: Tag, datum_plane: Tag, datum_xform: Tag, update_at_timestamp: bool) -> None:
        ...
    def SetLinkRegionData(self, linked_feature: Tag, n_seed_faces: int, seed_faces: typing.List[Tag], n_boundary_faces: int, boundary_faces: typing.List[Tag], xform: Tag, update_at_timestamp: bool, traverse_interior_edges: bool, delete_openings: bool) -> None:
        ...
    def SetLinkUpdateTime(self, linked_feature: Tag, timestamp_feature: Tag) -> None:
        ...
    def SetLinkedPtAngle(self, linked_feature: Tag, arc: Tag, angle: Tag, xform: Tag) -> None:
        ...
    def SetLinkedPtCenter(self, linked_feature: Tag, conic: Tag, xform: Tag) -> None:
        ...
    def SetLinkedPtCurve(self, linked_feature: Tag, curve: Tag, prm: Tag, xform: Tag) -> None:
        ...
    def SetLinkedPtPoint(self, linked_feature: Tag, point: Tag, xform: Tag) -> None:
        ...
    def SetSessionDelay(self, delayed: bool) -> None:
        ...
    def Unfreeze(self, n_parts: int, parts: typing.List[Tag]) -> None:
        ...
    def UpdateParts(self, n_parts: int, parts: typing.List[Tag]) -> None:
        ...
    def UpdateSession(self) -> None:
        ...


    class UFWaveLinkedFeatureInfo():
        feature_name: str
        owning_part_name: str
        source_part_name: str
    

    class DelayStatus(enum.Enum):
        NotDelayed = 0
        SessionDelayed = 1
        SessionFrozen = 2
        PersistentFrozen = 3
        NotInAssemblyDelayed = 4
        AssemblyConstraintsDelayed = 5
    

class UFView(Utilities.NXRemotableObject):
    def AddToViewSet(self, view_set_tag: Tag, type: UF.UFView.StandardOrientation) -> None:
        ...
    def AskBaseViewOfViewSet(self, view_set_tag: Tag, base_view_tag: Tag) -> None:
        ...
    def AskCenter(self, tag: Tag, center: float) -> None:
        ...
    def AskCurrentXyClip(self, view_tag: Tag, xy_clip_bounds: float) -> None:
        ...
    def AskFogOptions(self, view_tag: Tag, fog_options: UF.UFView.FogOptions) -> None:
        ...
    def AskPerspective(self, tag: Tag, type: int, distance: float) -> None:
        ...
    def AskRotation(self, tag: Tag, matrix: float) -> None:
        ...
    def AskShadedEdgeOptions(self, view_tag: Tag, shaded_edge_options: UF.UFView.ShadedEdgeOptions) -> None:
        ...
    def AskSurfaceDisplayOptions(self, view_tag: Tag, rendering_style: UF.UFView.RenderingStyle, edge_display_options: UF.UFView.EdgeDisplayOptions) -> None:
        ...
    def AskTagOfViewName(self, view_name: str, view_tag: Tag) -> None:
        ...
    def AskType(self, view_tag: Tag, type: UF.UFView.Type, subtype: UF.UFView.Subtype) -> None:
        ...
    def AskVdeData(self, _object: Tag, number_edits: int, vde_data: typing.List[UF.UFView.VdeData]) -> None:
        ...
    def AskVdeDataWithType(self, _object: Tag, number_edits: int, vde_data: typing.List[UF.UFView.VdeDataAndType]) -> None:
        ...
    def AskViewDependentStatus(self, np1: Tag, ir2: int, cr3: str) -> None:
        ...
    def AskViewLight(self, view: Tag, view_light: UF.UFView.Lighting) -> None:
        ...
    def AskViewSetByName(self, name: str, view_set: Tag) -> None:
        ...
    def AskViewsOfViewSet(self, view_set_tag: Tag, num_views: int, views_in_set: typing.List[Tag]) -> None:
        ...
    def AskVisibleObjects(self, view: Tag, n_visible: int, visible: typing.List[Tag], n_clipped: int, clipped: typing.List[Tag]) -> None:
        ...
    def AskVisualization(self, view: Tag, view_data: UF.UFView.Visualization) -> None:
        ...
    def AskWorkView(self, work_view: Tag) -> None:
        ...
    def AskXyClip(self, view_tag: Tag, xy_clip_bounds: float) -> None:
        ...
    def AskZClip(self, tag: Tag, status: int, distances: float) -> None:
        ...
    def AskZoomScale(self, view_tag: Tag, scale: float) -> None:
        ...
    def ConvertToModel(self, view_tag: Tag, object_tag: Tag) -> None:
        ...
    def ConvertToView(self, view_tag: Tag, object_tag: Tag) -> None:
        ...
    def CopyView(self, view_to_copy: Tag, name_of_new_view: str, new_view: Tag) -> None:
        ...
    def CreateViewSet(self, name: str, base_view_tag: Tag, base_view_type: UF.UFView.StandardOrientation, num_other_views: int, other_view_types: typing.List[UF.UFView.StandardOrientation], view_set_tag: Tag) -> None:
        ...
    def CycleObjects(self, view: Tag, type: UF.UFView.CycleObjectsEnum, _object: Tag) -> None:
        ...
    def Delete(self, view_obj_id: Tag) -> None:
        ...
    def DeleteViewSet(self, view_set_tag: Tag) -> None:
        ...
    def EditViewLight(self, light_name: str, light_attrs: UF.UFView.LightAttributes) -> None:
        ...
    def ExpandView(self, view_tag: Tag) -> None:
        ...
    def ExpandWorkView(self) -> None:
        ...
    def FitView(self, view_tag: Tag, fraction: float) -> None:
        ...
    def IsExpanded(self, expanded: bool) -> None:
        ...
    def MapDrawingToModel(self, member_view: Tag, drawing_pt: float, model_pt: float) -> None:
        ...
    def MapModelToDrawing(self, member_view: Tag, model_pt: float, map_pt: float) -> None:
        ...
    def PanView(self, view_tag: Tag, center: float) -> None:
        ...
    def ReadViewDrawingParameters(self, cp1: str, rr2: float, rr3: float) -> None:
        ...
    def RemoveFromViewSet(self, view_set_tag: Tag, type: UF.UFView.StandardOrientation) -> None:
        ...
    def Rename(self, view: Tag, name: str) -> None:
        ...
    def RestoreView(self, view_tag: Tag) -> None:
        ...
    def RotateView(self, view_tag: Tag, axis: float, delta_angle: float, count: int) -> None:
        ...
    def RotateViewAbsCsys(self, view_tag: Tag, center: float, axis: float, delta_angle: float, count: int) -> None:
        ...
    def Save(self, cp1: str, cp2: str, ip3: int, ip4: int) -> None:
        ...
    def SaveAllActiveViews(self) -> None:
        ...
    def SetBaseViewOfViewSet(self, view_set_tag: Tag, type: UF.UFView.StandardOrientation) -> None:
        ...
    def SetCenter(self, tag: Tag, center: float) -> None:
        ...
    def SetFogOptions(self, view_tag: Tag, fog_options: UF.UFView.FogOptions) -> None:
        ...
    def SetPerspective(self, tag: Tag, option: int, distance: float, eye: float) -> None:
        ...
    def SetRotation(self, tag: Tag, axes: float) -> None:
        ...
    def SetScale(self, tag: Tag, scale: float) -> None:
        ...
    def SetShadedEdgeOptions(self, view_tag: Tag, shaded_edge_options: UF.UFView.ShadedEdgeOptions) -> None:
        ...
    def SetSurfaceDisplayOptions(self, view_tag: Tag, rendering_style: UF.UFView.RenderingStyle, edge_display_options: UF.UFView.EdgeDisplayOptions) -> None:
        ...
    def SetViewLight(self, view_tag: Tag, view_light: UF.UFView.Lighting) -> None:
        ...
    def SetViewMatrix(self, cp1: str, ip2: int, np3: Tag, rp4: float) -> None:
        ...
    def SetVisualization(self, view: Tag, view_data: UF.UFView.Visualization) -> None:
        ...
    def SetXyClip(self, view_tag: Tag, xy_clip_bounds: float) -> None:
        ...
    def SetZClip(self, tag: Tag, status: int, distances: float) -> None:
        ...
    def UnexpandWorkView(self) -> None:
        ...
    def UpdateView(self, view_tag: Tag) -> None:
        ...
    def ZoomView(self, view_tag: Tag, scale: float) -> None:
        ...


    class UFViewVisualization():
        display_mode: int
        hidden_edge_mode: int
        silhouette_mode: int
        smooth_edges_mode: UF.UFView.SmoothEdges
        smooth_edge_color: int
        smooth_edge_font: int
        smooth_edge_width: int
        smooth_edge_angle_tolerance: float
        fog_mode: int
        fog_color: float
        fog_front: float
        fog_back: float
        fog_rate: float
    

    class VdeType(enum.Enum):
        VdeNonEdit = -1
        VdeAll = 0
        VdeUser = 1
        VdeSystem = 2
    

    class UFViewVdeDataAndType():
        view_tag: Tag
        start_parameter: float
        end_parameter: float
        color: int
        font: int
        width: int
        vde_type: UF.UFView.VdeType
    

    class UFViewVdeData():
        view_tag: Tag
        start_parameter: float
        end_parameter: float
        color: int
        font: int
        width: int
    

    class Type(enum.Enum):
        ModelType = 0
        DrawingMemberType = 1
        DrawingSheetType = 2
    

    class Subtype(enum.Enum):
        InvalidSubtype = -1
        SectionSubtype = 0
        ImportedSubtype = 1
        BaseMemberSubtype = 2
        OrthogonalSubtype = 3
        AuxiliarySubtype = 4
        DetailSubtype = 5
        BreakSubtype = 6
    

    class StandardOrientation(enum.Enum):
        StandardOrientationNone = -1
        StandardOrientationTop = 0
        StandardOrientationFront = 1
        StandardOrientationRight = 2
        StandardOrientationBack = 3
        StandardOrientationBottom = 4
        StandardOrientationLeft = 5
        StandardOrientationIsometric = 6
        StandardOrientationTrimetric = 7
        StandardOrientationDimetric = 8
        StandardOrientationNumTypes = 9
    

    class SmoothEdges(enum.Enum):
        SmoothEdgesOn = 1
        SmoothEdgesOff = 2
    

    class ShadedEdgeStyle(enum.Enum):
        ShadedEdgeStyleShadedEdgeColor = 0
        ShadedEdgeStyleBodyColor = 1
        ShadedEdgeStyleOff = 2
    

    class UFViewShadedEdgeOptions():
        shaded_edge_style: UF.UFView.ShadedEdgeStyle
        shaded_edge_color: int
        hidden_edge_style: UF.UFView.HiddenEdgeStyle
    

    class RenderingStyle(enum.Enum):
        ShadedStyle = 0
        WireframeStyle = 1
        StudioStyle = 2
        FaceAnalysisStyle = 3
        PartiallyShadedStyle = 4
        StaticWireframeStyle = 5
    

    class LightType(enum.Enum):
        AmbientLight = 0
        DistantLight = 1
        EyeLight = 2
        PointLight = 3
        SpotLight = 4
        NumLightTypes = 5
    

    class UFViewLights():
        light_name: str
        light_type: UF.UFView.LightType
        light_mode: UF.UFView.LightMode
        location: float
        to: float
    

    class LightMode(enum.Enum):
        FixedToObserver = 0
        FixedToThePart = 1
    

    class LightIntensityFactor(enum.Enum):
        IntensityFactorNone = 0
        IntensityFactor10x = 1
        IntensityFactor100x = 2
        IntensityFactor1000x = 3
        NumIntensityFactor = 4
    

    class UFViewLighting():
        two_sided_light: int
        shininess: float
        light_count: int
        lights: typing.List[UF.UFView.Lights]
    

    class LightFallOff(enum.Enum):
        FallOffConstant = 0
        FallOffInverseLinear = 1
        FallOffInverseSquare = 2
        FallOffConstantInverseLinear = 3
        FallOffConstantInverseSquare = 4
        NumFallOff = 5
    

    class LightEdge(enum.Enum):
        EdgeHard = 0
        EdgeSoft = 1
        EdgeExtraSoft = 2
        EdgeUltraSoft = 3
        NumEdge = 4
    

    class LightDetail(enum.Enum):
        DetailCoarse = 0
        DetailStandard = 1
        DetailFine = 2
        DetailExtraFine = 3
        DetailRayTraced = 4
        NumDetail = 5
    

    class LightBeamFallOff(enum.Enum):
        BeamFallOffNone = 0
        BeamFallOffGradual = 1
        BeamFallOffRapid = 2
        NumBeamFallOff = 3
    

    class UFViewLightAttributes():
        red: int
        green: int
        blue: int
        intensity: float
        intensity_factor: UF.UFView.LightIntensityFactor
        fall_off: UF.UFView.LightFallOff
        cone_angle: float
        delta_angle: float
        beam_fall_off: UF.UFView.LightBeamFallOff
        scattering: bool
        generate_shadows: bool
        detail: UF.UFView.LightDetail
        edge: UF.UFView.LightEdge
    

    class HiddenEdgeStyle(enum.Enum):
        HiddenEdgeStyleInvisible = 0
        HiddenEdgeStyleHiddenGeometryColor = 1
        HiddenEdgeStyleDashedInBodyColor = 2
    

    class UFViewFogOptions():
        fog_mode: int
        fog_color: float
        fog_front: float
        fog_back: float
        fog_rate: float
    

    class UFViewEdgeDisplayOptions():
        hidden_edge_mode: int
        silhouette_mode: int
        smooth_edges_mode: UF.UFView.SmoothEdges
        smooth_edge_color: int
        smooth_edge_font: int
        smooth_edge_width: int
        smooth_edge_angle_tolerance: float
    

    class CycleObjectsEnum(enum.Enum):
        VisibleObjects = 1
        DependentObjects = 2
        ErasedObjects = 3
        ModifiedObjects = 4
    

class UFVec4(Utilities.NXRemotableObject):
    def Copy(self, vec_src: float, vec_dst: float) -> None:
        ...
    def IsEqual(self, vec1: float, vec2: float, tolerance: float, is_equal: int) -> None:
        ...
    def IsZero(self, vec: float, tolerance: float, is_zero: int) -> None:
        ...
    def Scale(self, scale: float, vec: float, scaled_vec: float) -> None:
        ...
    def Vec3(self, vec_4D: float, vec_3D: float) -> None:
        ...
    def Vec3Homogen(self, vec_4D: float, vec_3D: float) -> None:
        ...


class UFVec3(Utilities.NXRemotableObject):
    def Add(self, vec1: float, vec2: float, vec_sum: float) -> None:
        ...
    def AffineComb(self, vec: float, scale: float, vec_to_scale: float, vec_comb: float) -> None:
        ...
    def AngleBetween(self, vec_from: float, vec_to: float, vec_ccw: float, angle: float) -> None:
        ...
    def AskPerpendicular(self, vec1: float, vec_perp: float) -> None:
        ...
    def ConvexComb(self, parameter: float, pnt1: float, pnt2: float, pnt_on_seg: float) -> None:
        ...
    def Copy(self, vec_src: float, vec_dst: float) -> None:
        ...
    def Cross(self, vec1: float, vec2: float, cross_product: float) -> None:
        ...
    def Distance(self, pnt1: float, pnt2: float, distance: float) -> None:
        ...
    def DistanceToPlane(self, pnt1: float, pnt_on_plane: float, plane_normal: float, tolerance: float, distance: float) -> None:
        ...
    def Dot(self, vec1: float, vec2: float, dot_product: float) -> None:
        ...
    def IsEqual(self, vec1: float, vec2: float, tolerance: float, is_equal: int) -> None:
        ...
    def IsParallel(self, vec1: float, vec2: float, tolerance: float, is_parallel: int) -> None:
        ...
    def IsPerpendicular(self, vec1: float, vec2: float, tolerance: float, is_perp: int) -> None:
        ...
    def IsZero(self, vec: float, tolerance: float, is_zero: int) -> None:
        ...
    def LinearComb(self, scale1: float, vec1: float, scale2: float, vec2: float, vec_comb: float) -> None:
        ...
    def Mag(self, vec: float, magnitude: float) -> None:
        ...
    def Midpt(self, pnt1: float, pnt2: float, mid_pnt: float) -> None:
        ...
    def Negate(self, vec: float, negated_vec: float) -> None:
        ...
    def Scale(self, scale: float, vec: float, scaled_vec: float) -> None:
        ...
    def Sub(self, vec1: float, vec2: float, vec_diff: float) -> None:
        ...
    def Triple(self, vec1: float, vec2: float, vec3: float, triple_product: float) -> None:
        ...
    def Unitize(self, vec: float, tolerance: float, magnitude: float, unit_vec: float) -> None:
        ...
    def Vec2(self, vec_3D: float, vec_2D: float) -> None:
        ...
    def Vec4(self, vec_3D: float, vec_4D: float) -> None:
        ...
    def Vec4Homogen(self, vec_3D: float, weight: float, vec_4D: float) -> None:
        ...


class UFVec2(Utilities.NXRemotableObject):
    def Add(self, vec1: float, vec2: float, vec_sum: float) -> None:
        ...
    def AffineComb(self, vec: float, scale: float, vec_to_scale: float, vec_comb: float) -> None:
        ...
    def AskPerpendicular(self, vec1: float, vec_perp: float) -> None:
        ...
    def Components(self, vec1: float, vec2: float, vec_comb: float, tolerance: float, scale1: float, scale2: float) -> None:
        ...
    def ConvexComb(self, parameter: float, pnt1: float, pnt2: float, pnt_on_seg: float) -> None:
        ...
    def Copy(self, vec_src: float, vec_dst: float) -> None:
        ...
    def Cross(self, vec1: float, vec2: float, cross_product: float) -> None:
        ...
    def Distance(self, pnt1: float, pnt2: float, distance: float) -> None:
        ...
    def Dot(self, vec1: float, vec2: float, dot_product: float) -> None:
        ...
    def IsEqual(self, vec1: float, vec2: float, tolerance: float, is_equal: int) -> None:
        ...
    def IsParallel(self, vec1: float, vec2: float, tolerance: float, is_parallel: int) -> None:
        ...
    def IsPerpendicular(self, vec1: float, vec2: float, tolerance: float, is_perp: int) -> None:
        ...
    def IsZero(self, vec: float, tolerance: float, is_zero: int) -> None:
        ...
    def LinearComb(self, scale1: float, vec1: float, scale2: float, vec2: float, vec_comb: float) -> None:
        ...
    def Mag(self, vec: float, magnitude: float) -> None:
        ...
    def Midpt(self, pnt1: float, pnt2: float, mid_pnt: float) -> None:
        ...
    def Negate(self, vec: float, negated_vec: float) -> None:
        ...
    def Rotate(self, vec: float, angle: float, rotated_vec: float) -> None:
        ...
    def Scale(self, scale: float, vec: float, scaled_vec: float) -> None:
        ...
    def Sub(self, vec1: float, vec2: float, vec_diff: float) -> None:
        ...
    def Unitize(self, vec: float, tolerance: float, magnitude: float, unit_vec: float) -> None:
        ...
    def Vec3(self, vec_2D: float, vec_3D: float) -> None:
        ...


class UFUnit(Utilities.NXRemotableObject):
    def AskMeasureTypeFromUnitTag(self, unit: Tag, measure_type: UF.UnitMeasureType) -> None:
        ...
    def AskSystemUnitTagFromMeasure(self, _object: Tag, unit_measure_type: UF.UnitMeasureType, unit: Tag) -> None:
        ...
    def AskUnitNameFromUnitTag(self, unit: Tag, name: str) -> None:
        ...
    def AskUnitTagFromUnitName(self, _object: Tag, unit_measure_type: UF.UnitMeasureType, name: str, unit: Tag) -> None:
        ...
    def ConvertValue(self, initial_value: float, initial_units: Tag, new_units: Tag, converted_value: float) -> None:
        ...


class UFUndo(Utilities.NXRemotableObject):
    def AskAnyMarkExist(self, visibility: UF.UFUndo.UserVisibility, any_exists: int) -> None:
        ...
    def AskMarkExist(self, mark_id: int, mark_name: str, exists: int) -> None:
        ...
    def AskMarkVisibility(self, mark_id: int, mark_name: str, visibility: UF.UFUndo.UserVisibility) -> None:
        ...
    def AskNextVisMark(self, mark_id: int) -> None:
        ...
    def AskNumberOfMarks(self, visibility: UF.UFUndo.UserVisibility, how_many: int) -> None:
        ...
    def DeleteAllMarks(self) -> None:
        ...
    def DeleteAllMiscCbs(self) -> None:
        ...
    def DeleteMark(self, mark_id: int, mark_name: str) -> None:
        ...
    def DeleteToMark(self, mark_id: int, mark_name: str) -> None:
        ...
    def DisableMiscCbs(self) -> None:
        ...
    def EnableMiscCbs(self) -> None:
        ...
    def RegisterMiscCb(self, cb_type: UF.UFUndo.MiscCb, mark_id: int, visibility: UF.UFUndo.UserVisibility, func: UF.UFUndo.MiscCbFT, closure: int, id: int) -> None:
        ...
    def SetMark(self, visibility: UF.UFUndo.UserVisibility, mark_name: str, mark_id: int) -> None:
        ...
    def SetMarkVisibility(self, mark_id: int, mark_name: str, visibility: UF.UFUndo.UserVisibility) -> None:
        ...
    def SetToMarkVisibility(self, to_mark: int, mark_name: str, visibility: UF.UFUndo.UserVisibility) -> None:
        ...
    def UndoToLastMark(self, visibility: UF.UFUndo.UserVisibility, mark_id: int) -> None:
        ...
    def UndoToMark(self, mark_id: int, mark_name: str) -> None:
        ...
    def UndoToNextVisMark(self) -> None:
        ...
    def UndoToPrevMark(self, visibility: UF.UFUndo.UserVisibility, previous_to: int, mark_id: int) -> None:
        ...
    def UnregisterMiscCb(self, cb_id: int) -> None:
        ...


    class UserVisibility(enum.Enum):
        Visible = 0
        Invisible = 1
        AnyVis = 2
        Visibility2Big = 3
    

    class MiscCbRet(enum.Enum):
        MiscCbContinue = 0
        MiscCbStop = 1
        MiscCb2Big = 2
    

    

    class MiscCb(enum.Enum):
        MiscCbSetPre = 0
        MiscCbSetPost = 1
        MiscCbUndoPre = 2
        MiscCbUndoPost = 3
        MiscCbChgVis = 4
        MiscCbType2Big = 5
    

class UFUiParam(Utilities.NXRemotableObject):
    def EditObject(self, obj_tag: Tag, dialog_response: int) -> None:
        ...


class UFUiOnt(Utilities.NXRemotableObject):
    def AskSelectedNodes(self, count: int, objects: typing.List[Tag]) -> None:
        ...
    def AskView(self, view: UF.UFUiOnt.TreeMode) -> None:
        ...
    def CollapseView(self) -> None:
        ...
    def ExpandView(self) -> None:
        ...
    def Refresh(self) -> None:
        ...
    def SwitchView(self, view: UF.UFUiOnt.TreeMode) -> None:
        ...


    class TreeMode(enum.Enum):
        Order = 0
        MachineMode = 1
        GeometryMode = 2
        MachineTool = 3
        NumTreeModes = 4
    

class UFUi(Utilities.NXRemotableObject):
    def AddToClassSel(self, class_id: int) -> None:
        ...
    def AddToSelList(self, select_: int, num: int, objs: typing.List[Tag], highlight_flag: bool) -> None:
        ...
    def AllowNonWorkPartFeatureSelection(self, select_: int, allow: bool) -> None:
        ...
    def AppendMenubarMenu(self, menu: UF.UFUi.MenubarItem, change_state: UF.UFUi.ChangeStateFnT, application_name: str) -> None:
        ...
    def AskCreatePartFilename(self, file_name: str, units: int, response: int) -> None:
        ...
    def AskCursorView(self, cursor_view: int) -> None:
        ...
    def AskDialogDirectory(self, dir_index: UF.UFUi.DialogDirId, dir_name: str) -> None:
        ...
    def AskDialogFilter(self, dir_index: UF.UFUi.DialogFilterId, fltr_name: str) -> None:
        ...
    def AskGlobalSelObjectList(self, num_objects: int, objects: typing.List[Tag]) -> None:
        ...
    def AskInfoUnits(self, units: int) -> None:
        ...
    def AskIwDecimalPlaces(self, mode: int, decimal_places: int) -> None:
        ...
    def AskLastPickedView(self, view_name: str) -> None:
        ...
    def AskLockStatus(self) -> int:
        ...
    def AskMinimalGraphicsWindow(self, is_set: bool) -> None:
        ...
    def AskOpenPartFilename(self, file_name: str, unused: bool, response: int) -> None:
        ...
    def AskRibbonVis(self, ribbon_id: int, show: int) -> None:
        ...
    def AskSelCursorPos(self, select_: int, view: Tag, abs_cursor_pos: float) -> None:
        ...
    def AskSelDescriptor(self, select_: int, descriptor: int) -> None:
        ...
    def AskSelListCount(self, select_: int, count: int) -> None:
        ...
    def AskSelObjectList(self, select_: int, count: int, objs: typing.List[Tag]) -> None:
        ...
    def AskSelRectanglePos(self, select_: int, view: Tag, pos1: float, pos2: float, pos3: float, pos4: float) -> None:
        ...
    def AskStringInput(self, cue: str, str: str, length: int) -> int:
        ...
    def AskToolbarVis(self, tool_id: int, show: int) -> None:
        ...
    def CancelUfDialog(self, from_where: int) -> None:
        ...
    def CloseListingWindow(self) -> None:
        ...
    def CreateFilebox(self, prompt_string: str, title_string: str, filter_string: str, default_name: str, filename: str, response: int) -> None:
        ...
    def CreateFileboxWithMultipleFilters(self, prompt_string: str, title_string: str, file_extensions: str, num_extensions: int, default_name: str, filename: str, response: int) -> None:
        ...
    def CreateRibbon(self, file_name: str, show: int, ribbon_id: int) -> None:
        ...
    def CreateToolbar(self, file_name: str, show: int, tool_id: int) -> None:
        ...
    def CreateUsertool(self, tool_num: int, filename: str, map_flag: bool, read_flag: bool) -> None:
        ...
    def DeleteFromClassSel(self, class_id: int) -> None:
        ...
    def DisableQuickAccess(self) -> None:
        ...
    def DismissDialogArea2(self) -> None:
        ...
    def DisplayMenu(self, title: str, default_item: int, items: str, num_items: int) -> int:
        ...
    def DisplayMessage(self, message: str, option: int) -> None:
        ...
    def DisplayMultiSelectMenu(self, cue: str, ip2: int, items: str, num_items: int, selected: int) -> int:
        ...
    def DisplayNonmodalMsg(self, title_string: str, message: str, pos_method: int) -> None:
        ...
    def DisplayUrl(self, url: str) -> int:
        ...
    def DisplayUrlAndActivate(self, url: str) -> int:
        ...
    def DisplayUsertool(self, tool_num: int, map_flag: bool) -> None:
        ...
    def EnableQuickAccess(self) -> None:
        ...
    def ExitListingWindow(self) -> None:
        ...
    def GetDa1Coords(self, x: int, y: int) -> None:
        ...
    def GetDa2Coords(self, x: int, y: int) -> None:
        ...
    def GetDefaultParent(self) -> int:
        ...
    def GetInputDoubles(self, cp1: str, cp2: str, ip3: int, ra4: float, ip5: int) -> int:
        ...
    def GetInputIntegers(self, cp1: str, cp2: str, ip3: int, ia4: int, ip5: int) -> int:
        ...
    def GetInputNumbers(self, cp1: str, cp2: str, ip3: int, ia4: int, ra5: float, ip6: int) -> int:
        ...
    def GetInputValues(self, cp1: str, cp2: str, ip3: int, ia4: int, ra5: float, ca6: str, ip7: int) -> int:
        ...
    def InitAttachments(self, attach: UF.UFUi.Attachment) -> None:
        ...
    def IsListingWindowOpen(self, response: bool) -> None:
        ...
    def IsObjectInSelList(self, select_: int, _object: Tag, in_list: bool) -> None:
        ...
    def LockUgAccess(self, from_where: int) -> int:
        ...
    def MessageDialog(self, title_string: str, dialog_type: UF.UiMessageDialogType, messages: str, num_messages: int, translate: bool, buttons: UF.UFUi.MessageButtons, response: int) -> None:
        ...
    def OpenListingWindow(self) -> None:
        ...
    def PickCsys(self, title: str, option: int, csys_matrix: float, origin: float) -> int:
        ...
    def PickPoint(self, cue: str, point: float) -> int:
        ...
    def PickView(self, title: str, view_name: str) -> int:
        ...
    def PointConstruct(self, cue: str, base_method: UF.UFUi.PointBaseMethod, point_tag: Tag, base_pt: float, response: int) -> None:
        ...
    def PointSubfunction(self, cue: str, mode: int, point_display_mode: int, point: float) -> int:
        ...
    def RegisterChangeStateFn(self, change_state: UF.UFUi.ChangeStateFnT, application_name: str) -> None:
        ...
    def RemoveAllFromSelList(self, select_: int, unhighlight: bool) -> None:
        ...
    def RemoveFromSelList(self, select_: int, num: int, objs: typing.List[Tag], unhighlight: bool) -> None:
        ...
    def RemoveRibbon(self, ribbon_id: int) -> None:
        ...
    def RemoveToolbar(self, tool_id: int) -> None:
        ...
    def ResumeCreateToolbar(self) -> None:
        ...
    def ResumeInitAppstate(self) -> None:
        ...
    def ResumeRemoveToolbar(self) -> None:
        ...
    def RouteInvokeCallback(self, call_back_name: str, num_objects: int, objects: Tag) -> None:
        ...
    def SaveListingWindow(self, filename: str) -> None:
        ...
    def SelectByClass(self, message: str, opts: UF.UFUi.SelectionOption, response: int, count: int, _object: typing.List[Tag]) -> None:
        ...
    def SelectConehead(self, message: str, num: int, origins: float, directions: float, labels: str, attributes: typing.List[UF.UFDisp.ConeheadAttrbSTag], selection_point: float, display_coneheads: int, selected_num: int, response: int) -> None:
        ...
    def SelectFeature(self, message: str, filter: int, count: int, feature_tags: typing.List[Tag], response: int) -> None:
        ...
    def SelectParameters(self, message: str, feature_tag: Tag, count: int, exp_tags: typing.List[Tag], response: int) -> None:
        ...
    def SelectPointCollection(self, message: str, coincident_points: bool, points: typing.List[UF.UFUi.ChainedPoints], count: int, response: int) -> None:
        ...
    def SelectRoutingObjects(self, title: str, message: str, types: int, method: int, scope: int, response: int, count: int, objects: typing.List[Tag]) -> None:
        ...
    def SelectRpoDimensions(self, message: str, feature_tag: Tag, count: int, exp_tags: typing.List[Tag], response: int) -> None:
        ...
    def SelectSingle(self, message: str, opts: UF.UFUi.SelectionOption, response: int, _object: Tag, cursor: float, view: Tag) -> None:
        ...
    def SelectSketch(self, message: str, mask: int, sketch_tag: Tag, response: int) -> None:
        ...
    def SelectSketchDimensions(self, message: str, sketch_tag: Tag, count: int, exp_tags: typing.List[Tag], response: int) -> None:
        ...
    def SelectTcResultFileToImport(self, file_extensions: str, num_extensions: int, filename: str, response: int) -> None:
        ...
    def SelectWithClassDialog(self, message: str, title: str, scope: int, sel_init_proc: UF.UFUi.SelInitFnT, user_data: int, response: int, count: int, _object: typing.List[Tag]) -> None:
        ...
    def SelectWithSingleDialog(self, message: str, title: str, scope: int, init_proc: UF.UFUi.SelInitFnT, user_data: int, response: int, _object: Tag, cursor: float, view: Tag) -> None:
        ...
    def SetCursorView(self, new_cursor_view: int) -> None:
        ...
    def SetDialogDirectory(self, id: UF.UFUi.DialogDirId, dir_name: str) -> None:
        ...
    def SetDialogFilter(self, id: UF.UFUi.DialogFilterId, fltr_name: str) -> None:
        ...
    def SetForceUnlockFlag(self) -> None:
        ...
    def SetMinimalGraphicsWindow(self, set: bool) -> None:
        ...
    def SetMinimalGraphicsWindowLocation(self, left: int, top: int, right: int, bottom: int) -> None:
        ...
    def SetPrompt(self, prompt_text: str) -> None:
        ...
    def SetRibbonVis(self, ribbonl_id: int, show: int) -> None:
        ...
    def SetSelMask(self, select_: int, action: UF.UFUi.SelMaskAction, num: int, mask_triples: typing.List[UF.UFUi.Mask]) -> None:
        ...
    def SetSelProcs(self, select_: int, filter_proc: UF.UFUi.SelFilterFnT, sel_cb: UF.UFUi.SelCbFnT, user_data: int) -> None:
        ...
    def SetSelType(self, select_: int, type: int) -> None:
        ...
    def SetSelectMask(self, action: int, num_items: int, items_to_mask: int) -> None:
        ...
    def SetStatus(self, status_text: str) -> None:
        ...
    def SetToolbarVis(self, tool_id: int, show: int) -> None:
        ...
    def SetUsertoolMenuEntry(self, option_number: int, label: str, filename: str) -> None:
        ...
    def SpecifyCsys(self, title: str, option: int, csys_matrix: float, origin: float, csys_tag: Tag) -> int:
        ...
    def SpecifyPlane(self, message: str, mode: int, display: int, response: int, orientation: float, origin: float, plane_eid: Tag) -> None:
        ...
    def SpecifyScreenPosition(self, message: str, motion_cb: UF.UFUi.MotionFnT, motion_cb_data: int, screen_pos: float, view_tag: Tag, response: int) -> None:
        ...
    def SpecifyVector(self, message: str, mode: int, display_conehead: int, direction: float, origin: float, response: int) -> None:
        ...
    def SuspendCreateToolbar(self) -> None:
        ...
    def SuspendInitAppstate(self) -> None:
        ...
    def SuspendRemoveToolbar(self) -> None:
        ...
    def ToggleStoplight(self, toggle_on_off: int) -> None:
        ...
    def UgmgrAskCreatePartFileName(self, filename: str, part_type: str, template_name: str, response: int) -> None:
        ...
    def UnlockUgAccess(self, from_where: int) -> int:
        ...
    def UpdateListingWindow(self) -> None:
        ...
    def WriteListingWindow(self, _string: str) -> None:
        ...


    class SelMaskAction(enum.Enum):
        SelMaskEnableAll = 0
        SelMaskEnableSpecific = 1
        SelMaskDisableSpecific = 2
        SelMaskClearAndEnableSpecific = 3
        SelMaskAllAndDisableSpecific = 4
        SelMaskCount = 5
    

    

    

    class UFUiSelectionOption():
        num_mask_triples: int
        mask_triples: typing.List[UF.UFUi.Mask]
        scope: int
        other_options: int
        reserved: int
    

    

    class PointBaseMethod(enum.Enum):
        PointInferred = 0
        PointCursorPos = 1
        PointExistingPt = 2
        PointEndPt = 3
        PointControlPt = 4
        PointIntersectPt = 5
        PointCenterPt = 6
        PointAnglePt = 7
        PointQuadrantPt = 8
        PointOnCurvePt = 9
        PointOnSurfacePt = 10
        PointOffsetCsysPt = 11
        PointDialog = 12
        PointNoMethod = 13
        PointApplicationMethod = 14
    

    

    

    class UFUiMotionCbData():
        view_tag: Tag
        start_position: float
        start_view_tag: Tag
    

    class UFUiMessageButtons():
        button1: bool
        button2: bool
        button3: bool
        label1: str
        label2: str
        label3: str
        response1: int
        response2: int
        response3: int
    

    class UFUiMenubarItem():
        type: UF.UiMenuType
        text: str
        name: str
        state: int
        CBproc: UF.UFUi.CbProc
        CBdata: int
    

    class UFUiMask():
        object_type: int
        object_subtype: int
        solid_type: int
    

    class UFUiErrData():
        size: int
        data: int
    

    class DialogFilterId(enum.Enum):
        ExportPartFltr = 0
        ExportParasolidFltr = 1
        ExportCgmFltr = 2
        ExportDiagramFltr = 3
        ExportRptFltr = 4
        ExportInvFltr = 5
        SymFltr = 6
        ImportPartFltr = 7
        ImportParasolidFltr = 8
        ImportCgmFltr = 9
        ImportMarkupFltr = 10
        ImportUdfFltr = 11
        PartNewFltr = 12
        PartOpenFltr = 13
        PartSaveasFltr = 14
        PartSaveasStudentFltr = 15
        FileGripFltr = 16
        FileUfunFltr = 17
        ImportSymbolFltr = 18
        ImportBlockFltr = 19
        ImageQsFltr = 20
        ImageDispFltr = 21
        ExportExpressionsFltr = 22
        ImportExpressionsFltr = 23
        MacroFltr = 24
        LayoutFltr = 25
        ExportComponentFltr = 26
        ImportComponentFltr = 27
        CamMdfFltr = 28
        CamGpmFltr = 29
        CamClsFltr = 30
        CamClFltr = 31
        CamClfFltr = 32
        CamBclFltr = 33
        CamIsoFltr = 34
        CamNcoutFltr = 35
        CamListoutFltr = 36
        CamAclFltr = 37
        CamSFltr = 38
        CamArcFltr = 39
        CamCycFileFltr = 40
        CamMtkFltr = 41
        TranPartFltr = 42
        TranIgsFltr = 43
        TranStpFltr = 44
        TranDxfFltr = 45
        TranIgesFltr = 46
        TranStep203Fltr = 47
        TranStep214Fltr = 48
        TranDxftougFltr = 49
        TranUgtodxfFltr = 50
        TranLogFltr = 51
        MbSyslogFltr = 52
        MiscDataFltr = 53
        CamToolibFltr = 54
        CamLiblistFltr = 55
        CamDispatFltr = 56
        CamVcutsFltr = 57
        CamVcuttFltr = 58
        CamTempsetFltr = 59
        ImportVrmlFltr = 60
        NleFltr = 61
        RlistHrnFltr = 62
        RlistCmpFltr = 63
        ImportSeFltr = 64
        ImportStlFltr = 65
        CamConfigFltr = 66
        CamSetupPrtFltr = 67
        VdacCeoFltr = 68
        VdacCfgFltr = 69
        TbrFltr = 70
        HatchFltr = 71
        BookmarkFltr = 72
        CamShopDocFltr = 73
        FmbdFileFltr = 74
        LoadOptFltr = 75
        TranDwgFltr = 76
        MenuDxfFltr = 77
        ImportAscFltr = 78
        TranCatiaFltr = 79
        TranCatmodFltr = 80
        CaeRptTemplatesFltr = 81
        CaeRptImgFltr = 82
        InteropFltr = 83
        DraftingImageFltr = 84
        Nx2dFltr = 85
        SprdFltr = 86
        SprdntFltr = 87
        SprshtFltr = 88
        XessFltr = 89
        CaeRstFltr = 90
        CaeRstOdbFltr = 91
        CaeOdbFltr = 92
        CaeSamcefFltr = 93
        CaeOp2Fltr = 94
        TranCatiav5Fltr = 95
        TranCatiav5CatpartFltr = 96
        ImportAcFltr = 97
        PrtPartOpenFltr = 98
        SfemPartOpenFltr = 99
        FemPartOpenFltr = 100
        FemPartNewFltr = 101
        BookmarkOpenFltr = 102
        BookmarkSaveFltr = 103
        CaeAfuFltr = 104
        XyplotDispTemplateFltr = 105
        FemSaveasFltr = 106
        SimSaveasFltr = 107
        MotionImpExpFltr = 108
        FtkNavTreeHistoryFltr = 109
        SimPartNewFltr = 110
        SimPartOpenFltr = 111
        FaceAnalysisReflectionFltr = 112
        BackgroundImageFltr = 113
        TextureImageFltr = 114
        IblImageFltr = 115
        CaeRpciiiFltr = 116
        CaeDacFltr = 117
        CaeCsvFltr = 118
        TranProeFltr = 119
        SePartAsmFltr = 120
        CaeEefFltr = 121
        CaeSefFltr = 122
        CaeRs2Fltr = 123
        CamFeaExportFltr = 124
        CaeMatFltr = 125
        MotionAdamsResFltr = 126
        MotionRecurdynRadFltr = 127
        PdfFltr = 128
        JpgFltr = 129
        TifFltr = 130
        EmfFltr = 131
        PngFltr = 132
        CaeUnv58Fltr = 133
        AssyFemPartOpenFltr = 134
        AssyFemPartNewFltr = 135
        AssyFemSaveasFltr = 136
        IfemPartOpenFltr = 137
        KfMisc1Fltr = 138
        KfMisc2Fltr = 139
        KfMisc3Fltr = 140
        KfMisc4Fltr = 141
        KfMisc5Fltr = 142
        SimulinkMdlFltr = 143
        SimulinkMFltr = 144
        MotionExportSdkRmdFltr = 145
        StandardFontsFltr = 146
        SwPartAsmFltr = 147
        IgesExportFltr = 148
        StepExportFltr = 149
        MotionFlexbodyRfiFltr = 150
        ImageFileFltr = 151
        AttrCatalogFltr = 152
        MwFltr = 153
        TrumpfGeoFltr = 154
        TireSpindleFltr = 155
        StudioImageFileFltr = 156
        MotionRecurdynRadRanFltr = 157
        MechdesRuntimeCodeFltr = 158
        CaeUnvFltr = 159
        PaxFltr = 160
        Hdf5Fltr = 161
        LayupFltr = 162
        CaeBrowseFltr = 163
        CaeMdfFltr = 164
        PartSaveasWithCatproductFltr = 165
        TranCatiav5CatproductFltr = 166
        JtConfigFltr = 167
        CaeCondseqFltr = 168
        JpegFltr = 169
        JpeFltr = 170
        TiffFltr = 171
        RasterImageFltr = 172
        MotionLmsMresFltr = 173
        ReportTemplateFltr = 174
        ReportImagesFltr = 175
        ReportZipFltr = 176
        TranAcisImportFltr = 177
        TranAcisExportFltr = 178
        TranAcisSatFltr = 179
        TranAcisSabFltr = 180
        PodFltr = 181
        IrayplusMaterialFltr = 182
        IrayplusMaterialSystemSaveFltr = 183
        PsfFltr = 184
        DgmlFltr = 185
        TranStpxFltr = 186
        TranStpzFltr = 187
        TranStpxzFltr = 188
        TranStp242Fltr = 189
        Tran3mfFltr = 190
        CaeLayoutstateFltr = 191
        MotionLmsLmsmotionresultsFltr = 192
        MotionLmsOffFltr = 193
        LightProfileFileFltr = 194
        CaeAppppDatasourceFltr = 195
        CaeResultsessionFltr = 196
        PartSaveasWithProtection = 197
        GifFltr = 198
        BmpFltr = 199
        XwdFltr = 200
        DialogFilterCount = 201
    

    class DialogDirId(enum.Enum):
        ExportDir = 0
        ImportDir = 1
        PartDir = 2
        GripDir = 3
        ImageDir = 4
        ImportSymbDir = 5
        ImportBlockDir = 6
        UfunDir = 7
        MacroDir = 8
        LayoutDir = 9
        CamMdfDir = 10
        CamGpmDir = 11
        CamClfDir = 12
        CamClDir = 13
        CamClsDir = 14
        CamBclDir = 15
        CamIsoDir = 16
        CamNcoutDir = 17
        CamListoutDir = 18
        CamAclDir = 19
        CamSDir = 20
        CamArcDir = 21
        CamCycDir = 22
        CamMtkDir = 23
        TranIgsDir = 24
        TranStpDir = 25
        TranDxfDir = 26
        TranIgesDir = 27
        TranStep203Dir = 28
        TranStep214Dir = 29
        TranDxftougDir = 30
        TranUgtodxfDir = 31
        TranLogDir = 32
        MbSyslogDir = 33
        MiscDataDir = 34
        CamToolibDir = 35
        CamLiblistDir = 36
        CamDispatDir = 37
        CamVcutsDir = 38
        CamVcuttDir = 39
        CamTempsetDir = 40
        NleDir = 41
        RlistHrnDir = 42
        RlistCmpDir = 43
        CamConfigDir = 44
        CamSetupPrtDir = 45
        VdacCeoDir = 46
        VdacCfgDir = 47
        TbrDir = 48
        HatchDir = 49
        BookmarkDir = 50
        CamShopDocDir = 51
        FmbdFileDir = 52
        TranDwgDir = 53
        MenuDxfDir = 54
        ImportAscDir = 55
        TranCatiaDir = 56
        TranCatmodDir = 57
        CaeRptTemplatesDir = 58
        CaeRptImgDir = 59
        InteropFileDir = 60
        DraftingImageDir = 61
        Nx2dFileDir = 62
        SprdFileDir = 63
        SprdntFileDir = 64
        SprshtFileDir = 65
        XessFileDir = 66
        CaeRstDir = 67
        CaeRstOdbDir = 68
        CaeOdbDir = 69
        CaeSamcefDir = 70
        TranCatiav5Dir = 71
        TranCatiav5CatpartDir = 72
        CaeAfuDir = 73
        XyplotDispTemplateDir = 74
        MotionImpExpDir = 75
        FtkNavTreeHistoryDir = 76
        FaceAnalysisReflectionDir = 77
        BackgroundImageDir = 78
        TextureImageDir = 79
        IblImageDir = 80
        CaeRpciiiDir = 81
        CaeDacDir = 82
        CaeCsvDir = 83
        TranProeDir = 84
        CaeEefDir = 85
        CaeSefDir = 86
        CaeRs2Dir = 87
        CaeMatDir = 88
        ReportTemplateDir = 89
        ReportImagesDir = 90
        ReportZipDir = 91
        MotionAdamsResDir = 92
        MotionRecurdynRadDir = 93
        PdfDir = 94
        JpgDir = 95
        TifDir = 96
        EmfDir = 97
        PngDir = 98
        SymDir = 99
        CaeUnv58Dir = 100
        KfMisc1Dir = 101
        KfMisc2Dir = 102
        KfMisc3Dir = 103
        KfMisc4Dir = 104
        KfMisc5Dir = 105
        SimulinkMdlDir = 106
        SimulinkMDir = 107
        MotionExportSdkRmdDir = 108
        StandardFontsDir = 109
        IgesExportDir = 110
        StepExportDir = 111
        MotionFlexbodyRfiDir = 112
        AttrCatalogDir = 113
        MwDir = 114
        TrumpfGeoDir = 115
        TireSpindleDir = 116
        MotionRecurdynRadRanDir = 117
        MechdesRuntimeCodeDir = 118
        CaeUnvDir = 119
        PaxDir = 120
        Hdf5Dir = 121
        LayupDir = 122
        CaeBrowseDir = 123
        CaeMdfDir = 124
        TranCatiav5CatproductDir = 125
        CaeCondseqDir = 126
        MotionLmsMresDir = 127
        CaeRstXdbDir = 128
        CaeRstXdbOdbDir = 129
        TranAcisDir = 130
        TranAcisSatDir = 131
        TranAcisSabDir = 132
        MotionFlexbodyOp2Dir = 133
        PodDir = 134
        DgmlDir = 135
        TranStpxDir = 136
        TranStpzDir = 137
        IrayplusMaterialDir = 138
        IrayplusMaterialSystemSaveDir = 139
        TranStpxzDir = 140
        TranStp242Dir = 141
        Tran3mfDir = 142
        CaeLayoutstateDir = 143
        MotionLmsLmsmotionresultsDir = 144
        CaeAppppDatasourceDir = 145
        LightProfileFileDir = 146
        CaeResultsessionDir = 147
        GifDir = 148
        BmpDir = 149
        XwdDir = 150
        DialogDirCount = 151
    

    

    

    class UFUiChainedPoints():
        pt: float
        _object: Tag
    

    

    class UFUiAttachment():
        center: int
        attach_type_top: int
        attach_type_left: int
        attach_type_right: int
        offset_top: int
        offset_left: int
        offset_right: int
        item_id_top: str
        item_id_left: str
        item_id_right: str
    

class UFUgmgrKf(Utilities.NXRemotableObject):
    def ExportDfaInPart(self, part_name: str) -> None:
        ...


class UFUgmgr(Utilities.NXRemotableObject):
    def AddProductAssemblyPart(self, product: str) -> None:
        ...
    def AddToFolder(self, object_to_add: Tag, folder: Tag) -> None:
        ...
    def AskAutolockStatus(self, current_value: bool) -> None:
        ...
    def AskConfigRule(self, current_rule: str) -> None:
        ...
    def AskConfiguredRev(self, database_part_tag: Tag, part_revision: Tag) -> None:
        ...
    def AskDependentFiles(self, encoded_name: str, file_count: int, file_names: str) -> None:
        ...
    def AskExportDirectory(self, part_tag: Tag, export_dir_name: str) -> None:
        ...
    def AskFamilyMemberHandles(self, family_tag: Tag, member_id: str, member_rev_id: str, member_part_handle: str, member_partrev_handle: str) -> None:
        ...
    def AskFileExportStatus(self, status: bool) -> None:
        ...
    def AskFolderName(self, folder: Tag, folder_name: str) -> None:
        ...
    def AskIdDisplayRule(self, id_display_rule: str) -> None:
        ...
    def AskNewAlternatePartNo(self, func: UF.UFUgmgr.NewAlternatePartNoFnT) -> None:
        ...
    def AskNewDatasetName(self, func: UF.UFUgmgr.NewDatasetNameFnT) -> None:
        ...
    def AskNewId(self, func: UF.UFUgmgr.NewIdFnT) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskNewPartNo(self, func: UF.UFUgmgr.NewPartNoFnT) -> None:
        ...
    def AskNewPartRev(self, func: UF.UFUgmgr.NewPartRevFnT) -> None:
        ...
    def AskObjectType(self, _object: Tag, object_type: UF.UFUgmgr.ObjectType) -> None:
        ...
    def AskPartNameDesc(self, database_part_tag: Tag, part_name: str, part_desc: str) -> None:
        ...
    def AskPartNumber(self, part: Tag, part_number: str) -> None:
        ...
    def AskPartRevisionId(self, part_revision: Tag, revision_id: str) -> None:
        ...
    def AskPartTag(self, part_number: str, database_part_tag: Tag) -> None:
        ...
    def AskPartrevPartTag(self, database_part_rev_tag: Tag, database_part_tag: Tag) -> None:
        ...
    def AskProductAssemblies(self, n_prod_assys: int, products: str) -> None:
        ...
    def AskRootFolder(self, folder_tag: Tag) -> None:
        ...
    def AskSaveasDatasetInfo(self, func: UF.UFUgmgr.SaveasDatasetInfoFnT) -> None:
        ...
    def AskSaveasDatasetName(self, func: UF.UFUgmgr.SaveasDatasetNameFnT) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskUserFolder(self, user_name: str, folder_tag: Tag) -> None:
        ...
    def AskUserRole(self, role: str) -> None:
        ...
    def AssignAlternatePartId(self, part_tag: Tag, context: str, id_type: str, alt_item_id: str, alt_rev_id: str, modifiable: bool) -> None:
        ...
    def AssignCopyDsetName(self, old_owner: str, old_owner_revision: str, dataset: str, app_type: str, rel_type: str, new_owner: str, new_owner_revision: str, model_name: str, modifiable: bool) -> None:
        ...
    def AssignNewDsetName(self, owner: str, owner_revision: str, app_type: str, rel_type: str, basis_string: str, model_name: str, modifiable: bool) -> None:
        ...
    def AssignPartNumber(self, basis_part_num: str, part_type: str, part_num: str, modifiable: bool) -> None:
        ...
    def AssignPartRev(self, part_num: str, part_type: str, part_rev: str, modifiable: bool) -> None:
        ...
    def AttachAlternate(self, part_tag: Tag, context: str, id_type: str, alt_item_id: str, alt_rev_id: str, alt_name: str, alt_desc: str, is_default: bool) -> None:
        ...
    def ConvertFileNameToCli(self, internal_name: str, cli_name: str) -> None:
        ...
    def ConvertNameFromCli(self, cli_name: str, internal_name: str) -> None:
        ...
    def ConvertNameToCli(self, internal_name: str, cli_name: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateComponentPart(self, parent_part: Tag, new_part_name: str, refset_name: str, instance_name: str, units: int, layer: int, origin: float, csys_matrix: float, n_objects: int, objects: typing.List[Tag], part_type: str, instance: Tag) -> None:
        ...
    def DecodePartFileName(self, encoded_name: str, part_number: str, part_revision: str, part_file_type: str, part_file_name: str) -> None:
        ...
    def DecodePartFilename_(self, encoded_name: str, part_number: str, part_revision: str, part_file_type: str, part_file_name: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def EncodePartFilename(self, part_number: str, part_revision: str, part_file_type: str, part_file_name: str, encoded_name: str) -> None:
        ...
    def FindConfiguredRev(self, parentrev_tag: Tag, childpart_tag: Tag, child_part_rev: Tag) -> None:
        ...
    def FindProductAssemblies(self, n_displayed_parts: int, displayed_parts: typing.List[Tag]) -> None:
        ...
    def GenerateBaseFileName(self, partSpec: str, baseFileName: str) -> None:
        ...
    def GetCreationParameters(self, part_type: str, num_info: int, info: typing.List[UF.UgmgrAttrInfo]) -> None:
        ...
    def Initialize(self, argc: int, argv: str) -> None:
        ...
    def InvokePdmServer(self, input_code: int, input_string: str, output_code: int, output_string: str) -> None:
        ...
    def ListConfigRules(self, count: int, config_rules: str) -> None:
        ...
    def ListContexts(self, part_type: str, count: int, contexts: str) -> None:
        ...
    def ListFolderContents(self, folder: Tag, count: int, folder_contents: typing.List[Tag]) -> None:
        ...
    def ListIdDisplayRules(self, count: int, id_display_rules: str) -> None:
        ...
    def ListIdTypes(self, part_type: str, context: str, count: int, id_types: str) -> None:
        ...
    def ListPartRevFiles(self, part_revision: Tag, file_count: int, file_types: str, file_names: str) -> None:
        ...
    def ListPartRevisions(self, part: Tag, revision_count: int, revisions: typing.List[Tag]) -> None:
        ...
    def ListPartsInFolder(self, folder: Tag, count: int, parts: typing.List[Tag]) -> None:
        ...
    def NewPartFromTemplate(self, encoded_part_name: str, part_type: str, encoded_template_name: str, part_tag: Tag) -> None:
        ...
    def PartrevWhereUsed(self, part_revision: Tag, parent_revisions_count: int, parent_revisions: typing.List[Tag]) -> None:
        ...
    def RefreshAssyPdiDate(self, part_tag: Tag, traverse: bool) -> None:
        ...
    def RegNewAlternatePartNo(self, func: UF.UFUgmgr.NewAlternatePartNoFnT) -> None:
        ...
    def RegNewDatasetName(self, new_dataset_name_fn: UF.UFUgmgr.NewDatasetNameFnT) -> None:
        ...
    def RegNewId(self, new_id_fn: UF.UFUgmgr.NewIdFnT) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RegNewPartNo(self, new_part_no_fn: UF.UFUgmgr.NewPartNoFnT) -> None:
        ...
    def RegNewPartRev(self, new_part_rev_fn: UF.UFUgmgr.NewPartRevFnT) -> None:
        ...
    def RegSaveasDatasetInfo(self, saveas_dataset_info_fn: UF.UFUgmgr.SaveasDatasetInfoFnT) -> None:
        ...
    def RegSaveasDatasetName(self, saveas_dataset_name_fn: UF.UFUgmgr.SaveasDatasetNameFnT) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RemoveProductAssemblyPart(self, product: str) -> None:
        ...
    def SavePreciseAssembly(self, work_part_tag: Tag, traverse_children: bool) -> None:
        ...
    def SetAutolockStatus(self, new_value: bool) -> None:
        ...
    def SetCloneAutoTrans(self, _X1: UF.UFUgmgr.CloneAutoTransFT) -> None:
        ...
    def SetConfigRule(self, config_rule: str) -> None:
        ...
    def SetDefaultFolder(self, folder: Tag) -> None:
        ...
    def SetDialogDisplay(self, display: bool) -> None:
        ...
    def SetFileExportStatus(self, status: bool) -> None:
        ...
    def SetIdDisplayRule(self, id_display_rule: str) -> None:
        ...
    def SetPartNameDesc(self, database_part_tag: Tag, part_name: str, part_desc: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetUserRole(self, role: str) -> None:
        ...
    def SetVariantConfigurationsForDisplay(self, available_displayed_part: Tag, n_variants: int, variants: typing.List[UF.UFUgmgr.VariantConfiguration], selected: bool) -> None:
        ...
    def SetVariantConfigurationsForLoad(self, n_variants: int, variants: typing.List[UF.UFUgmgr.VariantConfiguration], selected: bool) -> None:
        ...
    def Terminate(self) -> None:
        ...
    def ValidateAlternatePartId(self, part_tag: Tag, alt_item_id: str, alt_rev_id: str, context: str, id_type: str, modified_item_id: str, modified_rev_id: str, status: UF.UFUgmgr.AltIdStatus, reason: str) -> None:
        ...
    def ValidatePartRev(self, part_num: str, part_rev: str, part_type: str, modified_part_num: str, modified_part_rev: str, status: UF.UFUgmgr.PartnoStatus) -> None:
        ...
    def ValidateString(self, inputString: str, lengthLimit: int, hasInvalidCharacters: bool) -> None:
        ...


    class UFUgmgrVariantConfiguration():
        product: str
        variant: str
        desc: str
    

    

    class UFUgmgrValidateDatasetName():
        old_part_number: str
        old_rev_name: str
        new_part_number: str
        new_rev_name: str
        new_part_type: str
        new_dataset_name: str
        valid: bool
        ifail: int
    

    

    class UFUgmgrSaveasDatasetName():
        old_owner: str
        old_owner_revision: str
        old_dataset: str
        relation_type: str
        new_owner: str
        new_owner_revision: str
        dataset_name_modifiable: bool
        dataset_name: str
        ifail: int
    

    

    

    class RevConfigOptions(enum.Enum):
        ConfigureNone = 0
        ConfigureLatest = 1
        ConfigureByRevRule = 2
        ConfigureAllRevisions = 3
    

    class UFUgmgrPropertyInfo():
        property_name: str
        is_key_field: bool
        is_mandatory: bool
        is_create_descriptor: bool
        property_value: str
        is_modifiable: bool
    

    class PartnoStatus(enum.Enum):
        PartnoValid = 0
        PartnoInvalid = 1
        PartnoModified = 2
        PartnoOverride = 3
    

    class UFUgmgrPartFileObject():
        fullSpec: str
        cliSpec: str
        partID: str
        datasetName: str
        revisionID: str
        partNumber: str
        datasetType: str
        pdiModelType: str
        partTag: Tag
        iFail: int
    

    class UFUgmgrPartFileInfo():
        fileName: str
        partID: str
        revisionId: str
        modelType: str
        datasetName: str
        revisionRule: str
        revisionOption: UF.UFUgmgr.RevConfigOptions
    

    class ObjectType(enum.Enum):
        TypeUnknown = 0
        TypeFolder = 1
        TypePart = 2
        TypePartRevision = 3
    

    

    class UFUgmgrNewPartRev():
        item: str
        item_type: str
        part_revision_modifiable: bool
        new_revision: str
        ifail: int
    

    

    class UFUgmgrNewPartNo():
        old_item: str
        item_type: str
        part_number_modifiable: bool
        new_id: str
        part_name_modifiable: bool
        new_name: str
        part_description_modifiable: bool
        new_description: str
        ifail: int
    

    

    class UFUgmgrNewId():
        old_item: str
        item_type: str
        num_properties: int
        properties: typing.List[UF.UFUgmgr.PropertyInfo]
        part_name_modifiable: bool
        new_name: str
        part_description_modifiable: bool
        new_description: str
        ifail: int
    

    

    class UFUgmgrNewDatasetName():
        owner: str
        owner_revision: str
        dataset_type: str
        relation_type: str
        basis_name: str
        dataset_name_modifiable: bool
        dataset_name: str
        ifail: int
    

    

    class UFUgmgrNewAlternatePartNo():
        part_tag: Tag
        context: str
        id_type: str
        alt_item_id: str
        alt_rev_id: str
        alt_name: str
        alt_description: str
        modifiable: bool
    

    

    class AltIdStatus(enum.Enum):
        AltIdValid = 0
        AltIdInvalid = 1
        AltIdModified = 2
        AltIdOverride = 3
    

class UFUgfont(Utilities.NXRemotableObject):
    def AddFont(self, fte: Tag, index: int, font: str) -> None:
        ...
    def AddStandardFont(self, fte: Tag, index: int, font: str) -> None:
        ...
    def AskFontHeader(self, fte: Tag, font: int, header: UF.UFUgfont.FontHeader) -> None:
        ...
    def AskFontName(self, fte: Tag, index: int, font_name: bytes) -> None:
        ...
    def AskFontStyles(self, fte: Tag, index: int, num_styles: int, styles: str) -> None:
        ...
    def AskFontType(self, fte: Tag, index: int, type: UF.UFUgfont.Type) -> None:
        ...
    def AskNumberOfFonts(self, fte: Tag, num: int) -> None:
        ...
    def ReplaceFont(self, fte: Tag, index: int, font: str) -> None:
        ...
    def ReplaceFont1(self, fte: Tag, index: int, type: UF.UFUgfont.Type, font: str) -> None:
        ...


    class Type(enum.Enum):
        Nx = 0
        Standard = 1
        Empty = 10
    

    class UFUgfontFontHeader():
        version: int
        height: int
        width: int
        base_height: int
        waist_height: int
        width_type: int
        overlap_1: int
        overlap_2: int
        overlap_3: int
        line_spacing: float
        char_spacing: float
        grid_spacing: float
        number_of_chars: int
    

class UFUdop(Utilities.NXRemotableObject):
    def AskOper(self, udop_id: int, oper_id: int) -> None:
        ...
    def AskPurpose(self, udop_id: int, purpose: UF.UFUdop.Purpose) -> None:
        ...
    def AskUdop(self, exit_id: int, udop_id: int) -> None:
        ...


    class Purpose(enum.Enum):
        UserParams = 0
        Generate = 1
    



    class QueryClassId(enum.Enum):
        DontAllowQueryClassId = 1
        AllowQueryClassId = 2
    

    class OwnedObjectSelection(enum.Enum):
        DontAllowSelection = 1
        AllowSelection = 2
    

    class UFUdobjLink():
        link_type: int
        assoc_ug_tag: Tag
        object_status: int
    

    class UFUdobjAllData():
        class_id: int
        udo_status: int
        num_ints: int
        ints: int
        num_doubles: int
        doubles: float
        num_strings: int
        strings: str
        num_links: int
        link_defs: typing.List[UF.UFUdobj.Link]
        num_lengths: int
        lengths: float
        num_areas: int
        areas: float
        num_volumes: int
        volumes: float
    

class UFUde(Utilities.NXRemotableObject):
    def AskBoolean(self, ude_obj: int, param_name: str, value: bool) -> None:
        ...
    def AskDouble(self, ude_obj: int, param_name: str, value: float) -> None:
        ...
    def AskInteger(self, ude_obj: int, param_name: str, value: int) -> None:
        ...
    def AskName(self, ude_object: int, ude_name: str) -> None:
        ...
    def AskParamToggle(self, ude_obj: int, param_name: str, toggle: UF.UFUde.ParamToggle) -> None:
        ...
    def AskParamType(self, ude_obj: int, param_name: str, param_type: UF.UFUde.ParamType) -> None:
        ...
    def AskParams(self, ude_obj: int, number_of_params: int, param_names: str) -> None:
        ...
    def AskPoint(self, ude_obj: int, param_name: str, smart_point_tag: Tag) -> None:
        ...
    def AskString(self, ude_obj: int, param_name: str, value: str) -> None:
        ...
    def AskVector(self, ude__obj: int, param_name: str, smart_vector_tag: Tag) -> None:
        ...
    def IsParamOptional(self, ude_obj: int, param_name: str, response: bool) -> None:
        ...
    def SetBoolean(self, ude_obj: int, param_name: str, param_value: bool) -> None:
        ...
    def SetDouble(self, ude_obj: int, param_name: str, value: float) -> None:
        ...
    def SetInteger(self, ude_obj: int, param_name: str, value: int) -> None:
        ...
    def SetParamToggle(self, ude_obj: int, param_name: str, toggle: UF.UFUde.ParamToggle) -> None:
        ...
    def SetPoint(self, ude_obj: int, param_name: str, smart_point_tag: Tag) -> None:
        ...
    def SetString(self, ude_obj: int, param_name: str, value: str) -> None:
        ...
    def SetVector(self, ude_obj: int, param_name: str, smart_vector_tag: Tag) -> None:
        ...


    class ParamType(enum.Enum):
        ParamTypeInt = 0
        ParamTypeDouble = 1
        ParamTypeString = 2
        ParamTypeBoolean = 3
        ParamTypeOption = 4
        ParamTypePoint = 5
        ParamTypeVector = 6
    

    class ParamToggle(enum.Enum):
        ParamInactive = 0
        ParamActive = 1
    

class UFTurn(Utilities.NXRemotableObject):
    def AskCutRegionOfIndex(self, oper_tag: Tag, index_of_cut_region: int, area_of_cut_region: float, selection_point_for_cut_region: float, cut_region_exists: bool, message: str) -> None:
        ...
    def AskCutRegionsExist(self, oper_tag: Tag, number_of_cut_regions_found: int, total_area_of_cut_regions_found: float, cut_regions_location: UF.UFTurn.CutRegionsLocation, message: str) -> None:
        ...
    def CreateBlankFromBoundary(self, object_tag: Tag, count: int, curves: typing.List[Tag], boundary_data: UF.UFCambnd.BoundaryData, app_data: typing.List[UF.UFCambnd.AppData], stock_equi: float, stock_face: float, stock_radial: float) -> None:
        ...
    def CreateParametricBlank(self, object_tag: Tag, workpiece_type: UF.ParamTurnWorkpieceType, direction: UF.ParamTurnWorkpieceDirection, mounting_point: Tag, length: float, outer_diameter: float, inner_diameter: float) -> None:
        ...
    def IpwBox(self, oper_tag: Tag, length: float, diameter: float, bottom_left_in_plane: float, top_right_in_plane: float, bottom_left_pnt3: float, bottom_right_pnt3: float, top_left_pnt3: float, top_right_pnt3: float, message: str) -> None:
        ...
    def MapAngleFromWcs(self, oper_tag: Tag, wcs_angle: float) -> float:
        ...
    def MapAngleToWcs(self, oper_tag: Tag, scs_angle: float) -> float:
        ...
    def MapPnt2FromWcs(self, oper_tag: Tag, wcs_pnt2: float, scs_pnt2: float) -> None:
        ...
    def MapPnt2ToAcs(self, oper_tag: Tag, scs_pnt2: float, acs_pnt3: float) -> None:
        ...
    def MapPnt2ToWcs(self, oper_tag: Tag, scs_pnt2: float, wcs_pnt2: float) -> None:
        ...
    def MapPnt3FromAcs(self, oper_tag: Tag, acs_pnt3: float, scs_pnt2: float) -> None:
        ...
    def MapTooltrackingpointFromWcs(self, oper_tag: Tag, wcs_tooltrackingpoint: int) -> None:
        ...
    def MapTooltrackingpointToWcs(self, oper_tag: Tag, scs_tooltrackingpoint: int) -> None:
        ...
    def MapVec2FromWcs(self, oper_tag: Tag, wcs_vec2: float, scs_vec2: float) -> None:
        ...
    def MapVec2ToAcs(self, oper_tag: Tag, scs_vec2: float, acs_vec3: float) -> None:
        ...
    def MapVec2ToWcs(self, oper_tag: Tag, scs_vec2: float, wcs_vec2: float) -> None:
        ...
    def MapVec3FromAcs(self, oper_tag: Tag, acs_vec3: float, scs_vec2: float) -> None:
        ...
    def SaveSpinningIpwAsPart(self, oper_tag: Tag, filename: str, message: str) -> None:
        ...
    def TeachmodeCreateSubop(self, oper_tag: Tag, subop_type: UF.ParamTtmoprSubopType, subop_tag: Tag, message: str) -> None:
        ...


    class CutRegionsLocation(enum.Enum):
        CutRegionsLocatedUndefined = 0
        CutRegionsLocatedOnNearSideOfCenterline = 1
        CutRegionsLocatedOnFarSideOfCenterline = 2
        CutRegionsLocatedOnBothSidesOfCenterline = 3
    

class UFTrns(Utilities.NXRemotableObject):
    def CreateCsysMappingMatrix(self, ref_csys: float, dest_csys: float, matrix: float, status: int) -> None:
        ...
    def CreateReflectionMatrix(self, _object: Tag, matrix: float, status: int) -> None:
        ...
    def CreateRotationMatrix(self, origin: float, direction: float, degrees_rotation: float, matrix: float, status: int) -> None:
        ...
    def CreateScalingMatrix(self, type: int, scales: float, origin: float, matrix: float, status: int) -> None:
        ...
    def CreateTranslationMatrix(self, translation: float, matrix: float) -> None:
        ...
    def MapPosition(self, ra1: float, rp2: float) -> None:
        ...
    def MultiplyMatrices(self, matrix1: float, matrix2: float, product: float) -> None:
        ...
    def TransformObjects(self, rp1: float, objects: typing.List[Tag], n_objects: int, move_or_copy: int, dest_layer: int, trace_curves: int, copies: typing.List[Tag], trace_curve_group: Tag, status: int) -> None:
        ...


class UFText(Utilities.NXRemotableObject):
    def AskTextMode(self) -> UF.UFText.ModeS:
        ...
    def CopyNchars(self, input_buffer: str, output_buffer_length: int, nchars: int, output_buffer: str) -> None:
        ...
    def CountCharacters(self, string_to_check: str, num_characters: int) -> None:
        ...
    def InitNativeLangSupport(self) -> None:
        ...
    def LoadTranslationFile(self, file: str) -> None:
        ...
    def SetTextMode(self, mode: UF.UFText.ModeS) -> None:
        ...
    def TranslateString(self, source: str, size: int, xstring: str) -> None:
        ...
    def TranslateString2(self, source: str, xstring: str) -> None:
        ...
    def Truncate(self, string_to_truncate: str, num_bytes: int, num_characters: int, truncated: bool) -> None:
        ...


    class ModeS(enum.Enum):
        Locale = 0
        Utf8 = 1
        AllUtf8 = 2
    

class UFTag(Utilities.NXRemotableObject):
    def AskHandleFromTag(self, object_tag: Tag, handle: str) -> None:
        ...
    def AskHandleOfTag(self, object_tag: Tag) -> str:
        """[Obsolete("Deprecated")"""
        ...
    def AskNewTagOfEntity(self, v9_eid: Tag) -> Tag:
        ...
    def AskTagOfHandle(self, object_handle: str) -> Tag:
        ...
    def ComposeHandle(self, file_data: str, sub_file_id: int, version: int, handle: str) -> None:
        ...
    def DecomposeHandle(self, handle: str, file_data: str, sub_file_id: int, version: int) -> None:
        ...
    def RegisterEventCb(self, callback: UF.UFTag.EventFnT, closure: int, callback_id: int) -> None:
        ...
    def UnregisterEventCb(self, callback_id: int) -> None:
        ...


    

    class Event(enum.Enum):
        EventNormalCreate = 0
        EventUndoOverCreate = 1
        EventNormalDelete = 2
        EventUndoOverDelete = 3
        EventUndoDeleteExpired = 4
        EventUndoCreateExpired = 5
    

class UFTabnotF(Utilities.NXRemotableObject):
    def Indandfixoutofsynchspreadsheettabnotes(self, partTag: Tag, fixTabnotes: bool, numTabnotes: int, tabnotes: typing.List[Tag]) -> None:
        ...


    class ZeroDisplay(enum.Enum):
        ZeroDisplayZero = 0
        ZeroDisplayDash = 1
        ZeroDisplayEmpty = 2
    

class UFTabnot(Utilities.NXRemotableObject):
    def AddColumn(self, tabular_note: Tag, column: Tag, index: int) -> None:
        ...
    def AddHeaderRow(self, tabular_note: Tag, row: Tag, index: int) -> None:
        ...
    def AddRow(self, tabular_note: Tag, row: Tag, index: int) -> None:
        ...
    def AskCellAtRowCol(self, row: Tag, column: Tag, cell: Tag) -> None:
        ...
    def AskCellPrefs(self, cell: Tag, cell_prefs: UF.UFTabnot.CellPrefs) -> None:
        ...
    def AskCellText(self, cell: Tag, cell_text: str) -> None:
        ...
    def AskCellTextPosition(self, cell: Tag, text_position: float) -> None:
        ...
    def AskColumnHeadCfw(self, column: Tag, section: Tag, cfw: int) -> None:
        ...
    def AskColumnOfCell(self, cell: Tag, column: Tag) -> None:
        ...
    def AskColumnSortData(self, column: Tag, sort_data: UF.UFTabnot.SortData) -> None:
        ...
    def AskColumnWidth(self, column: Tag, width: float) -> None:
        ...
    def AskDefaultCellPrefs(self, cell_prefs: UF.UFTabnot.CellPrefs) -> None:
        ...
    def AskDefaultSectionPrefs(self, section_prefs: UF.UFTabnot.SectionPrefs) -> None:
        ...
    def AskEvaluatedCellText(self, cell: Tag, evaluated_text: str) -> None:
        ...
    def AskMergeInfo(self, cell: Tag, start_row: Tag, start_column: Tag, end_row: Tag, end_column: Tag) -> None:
        ...
    def AskNmColumns(self, tabnote: Tag, nm_columns: int) -> None:
        ...
    def AskNmHeaderRows(self, tabnote: Tag, nm_header_rows: int) -> None:
        ...
    def AskNmRows(self, tabnote: Tag, nm_rows: int) -> None:
        ...
    def AskNmRowsInSection(self, section: Tag, nm_rows: int) -> None:
        ...
    def AskNmSections(self, tabnote: Tag, nm_sections: int) -> None:
        ...
    def AskNthColumn(self, tabnote: Tag, index: int, column: Tag) -> None:
        ...
    def AskNthHeaderRow(self, tabnote: Tag, index: int, row: Tag) -> None:
        ...
    def AskNthRow(self, tabnote: Tag, index: int, row: Tag) -> None:
        ...
    def AskNthRowInSection(self, section: Tag, index: int, row: Tag) -> None:
        ...
    def AskNthSection(self, tabnote: Tag, index: int, section: Tag) -> None:
        ...
    def AskRelativeColumn(self, column: Tag, position: int, relative_column: Tag) -> None:
        ...
    def AskRelativeRow(self, row: Tag, position: int, relative_row: Tag) -> None:
        ...
    def AskRowHeadCfw(self, row: Tag, cfw: int) -> None:
        ...
    def AskRowHeight(self, row: Tag, height: float) -> None:
        ...
    def AskRowOfCell(self, cell: Tag, row: Tag) -> None:
        ...
    def AskSectionOfRow(self, row: Tag, section: Tag) -> None:
        ...
    def AskSectionPrefs(self, section: Tag, section_prefs: UF.UFTabnot.SectionPrefs) -> None:
        ...
    def AskTabularNoteOfColumn(self, column: Tag, tabular_note: Tag) -> None:
        ...
    def AskTabularNoteOfSection(self, section: Tag, tabular_note: Tag) -> None:
        ...
    def ConvertToNonSpreadsheetTabnote(self, tabular_note: Tag) -> None:
        ...
    def Create(self, prefs: UF.UFTabnot.SectionPrefs, origin: float, tabular_note: Tag) -> None:
        ...
    def CreateColumn(self, width: float, column: Tag) -> None:
        ...
    def CreateFromTemplate(self, template_name: str, origin: float, tabular_note: Tag) -> None:
        ...
    def CreateRow(self, height: float, row: Tag) -> None:
        ...
    def EnableAutomaticUpdate(self, allow_automatic_update: bool) -> None:
        ...
    def ImportSpreadsheetCell(self, spreadsheet: Tag, sheet_number: int, row_number: int, column_number: int, cell: Tag) -> None:
        ...
    def MergeCells(self, start_cell: Tag, end_cell: Tag) -> None:
        ...
    def RemoveColumn(self, column: Tag) -> None:
        ...
    def RemoveRow(self, row: Tag) -> None:
        ...
    def SetCellPrefs(self, cell: Tag, cell_prefs: UF.UFTabnot.CellPrefs) -> None:
        ...
    def SetCellText(self, cell: Tag, cell_text: str) -> None:
        ...
    def SetColumnHeadCfw(self, column: Tag, section: Tag, cfw: int) -> None:
        ...
    def SetColumnSortData(self, column: Tag, sort_data: UF.UFTabnot.SortData) -> None:
        ...
    def SetColumnWidth(self, column: Tag, width: float) -> None:
        ...
    def SetDefaultCellPrefs(self, cell_prefs: UF.UFTabnot.CellPrefs) -> None:
        ...
    def SetDefaultSectionPrefs(self, section_prefs: UF.UFTabnot.SectionPrefs) -> None:
        ...
    def SetRowHeadCfw(self, row: Tag, cfw: int) -> None:
        ...
    def SetRowHeight(self, row: Tag, height: float) -> None:
        ...
    def SetSectionPrefs(self, section: Tag, section_prefs: UF.UFTabnot.SectionPrefs) -> None:
        ...
    def Sort(self, tabnote_tag: Tag) -> None:
        ...
    def UnmergeCells(self, cell: Tag) -> None:
        ...
    def Update(self, tabular_note: Tag) -> None:
        ...


    class SortDirection(enum.Enum):
        SortDirDescending = 0
        SortDirAscending = 1
    

    class UFTabnotSortData():
        sort_index: int
        sort_direction: UF.UFTabnot.SortDirection
    

    class UFTabnotSectionPrefs():
        header_location: UF.UFTabnot.HeaderLocation
        max_height: float
        overflow_direction: UF.UFTabnot.OverflowDirection
        overflow_spacing: float
        attach_point: UF.UFTabnot.AttachPoint
        use_double_width_border: bool
        border_width: float
        display_continuation_note: UF.UFTabnot.DisplayContinuationNote
        continuation_note: str
    

    class OverflowDirection(enum.Enum):
        OverflowLeft = 1
        OverflowRight = 2
        OverflowNextSheet = 3
        OverflowUp = 4
        OverflowDown = 5
    

    class Just(enum.Enum):
        JustLeft = 0
        JustCenter = 1
        JustRight = 2
        JustTop = 0
        JustMiddle = 1
        JustBottom = 2
    

    class HeaderLocation(enum.Enum):
        HeaderLocationNone = 0
        HeaderLocationAbove = 1
        HeaderLocationBelow = 2
    

    class Format(enum.Enum):
        FormatText = 1
        FormatFloat = 2
        FormatFixed = 3
        FormatGeneral = 4
        FormatMonetary = 5
        FormatComma = 6
        FormatFractionHalfSize = 7
        FormatFractionThreeQuarterSize = 8
        FormatFractionFullSize = 9
        FormatPercent = 10
        FormatDegrees = 11
        FormatDegreesRadianUnits = 12
        FormatDegreesDegreeUnits = 13
        FormatHex = 14
        FormatLogic = 15
        FormatDateDmy = 16
        FormatDateDm = 17
        FormatDateMy = 18
        FormatDateMdy = 19
        FormatDateYmd = 20
        FormatDateY4md = 21
        FormatDateDmyDot = 22
        FormatTimeHm = 23
        FormatTimeHms = 24
        FormatHidden = 25
        FormatCustom = 26
    

    class FitMethod(enum.Enum):
        FitMethodNone = 0
        FitMethodOverwriteBorder = 1
        FitMethodAutoSizeText = 2
        FitMethodWrap = 3
        FitMethodAbbreviate = 4
        FitMethodRemoveSpaces = 5
        FitMethodAutoSizeRow = 6
        FitMethodAutoSizeCol = 7
        FitMethodTruncate = 8
    

    class DisplayContinuationNote(enum.Enum):
        DisplayContinuationNoteNone = 0
        DisplayContinuationNoteAbove = 1
        DisplayContinuationNoteBelow = 2
    

    class UFTabnotCellPrefs():
        format: UF.UFTabnot.Format
        precision: int
        is_a_formula: bool
        zero_display: UF.UFTabnot.ZeroDisplay
        text_font: int
        text_height: float
        text_aspect_ratio: float
        symbolAspectRatio: float
        horiz_just: UF.UFTabnot.Just
        vert_just: UF.UFTabnot.Just
        text_angle: float
        text_slant: float
        is_vertical: bool
        is_italic: bool
        strikethru: bool
        line_space_factor: float
        char_space_factor: float
        is_hidden: bool
        text_color: int
        text_density: int
        bottom_line_cfw: int
        right_line_cfw: int
        nm_fit_methods: int
        fit_methods: typing.List[UF.UFTabnot.FitMethod]
        referenced_spreadsheet: Tag
        ss_sheet: int
        ss_row: int
        ss_col: int
        prefix: str
        suffix: str
        formula_suffix: str
        url: str
        is_protected: bool
    

    class AttachPoint(enum.Enum):
        AttachPointTopLeft = 1
        AttachPointTopRight = 2
        AttachPointBottomLeft = 3
        AttachPointBottomRight = 4
    

class UFSurfReg(Utilities.NXRemotableObject):
    def AskType(self, surf_reg_tag: Tag, surf_reg_type: UF.UFSurfReg.Type) -> None:
        ...


    class Type(enum.Enum):
        Seed = 1
        AllFacesOfBody = 2
        ExplicitFaces = 3
        Steep = 4
    

class UFSubdiv(Utilities.NXRemotableObject):
    def AskParms(self, subdiv_tag: Tag, subdiv_type: UF.UFSubdiv.Type, subdiv_structure_pointer: UF.UFSubdiv.DataStructuresUnion) -> None:
        ...
    def AskType(self, subdiv_tag: Tag, subdiv_type: UF.UFSubdiv.Type) -> None:
        ...
    def Create(self, subdiv_type: UF.UFSubdiv.Type, subdiv_structure_pointer: UF.UFSubdiv.DataStructuresUnion, subdiv_tag: Tag) -> None:
        ...
    def Edit(self, subdiv_type: UF.UFSubdiv.Type, subdiv_structure_pointer: UF.UFSubdiv.DataStructuresUnion, subdiv_tag: Tag) -> None:
        ...
    def Free(self, subdiv_type: UF.UFSubdiv.Type, subdiv_structure_pointer: UF.UFSubdiv.DataStructuresUnion) -> None:
        ...


    class Type(enum.Enum):
        Isocline = 1
    

    class UFSubdivIsocline():
        body_tag: Tag
        excluded_faces: typing.List[Tag]
        face_count: int
        direction: Tag
        angle_str: str
        second_direction: Tag
    

    class UFSubdivDataStructuresUnion():
        subdiv_type1: typing.List[UF.UFSubdiv.Isocline]
    

class UFStyler(Utilities.NXRemotableObject):
    def AskSelectDialogId(self, selection_data: int, dialog_id: int) -> None:
        ...


class UFStudio(Utilities.NXRemotableObject):
    def CreateStyledBlend(self, styled_blend_data: UF.UFStudio.StybldData, styled_blend: Tag) -> None:
        ...
    def EditStyledBlend(self, styled_blend_data: UF.UFStudio.StybldData, styled_blend: Tag) -> None:
        ...
    def InitStyledBlend(self, styled_blend_data: typing.List[UF.UFStudio.StybldData]) -> None:
        ...


    class StybldVDegree(enum.Enum):
        StybldVDegreeCubic = 3
        StybldVDegreeQuintic = 5
    

    class StybldTrim(enum.Enum):
        StybldTrimAttachAll = 0
        StybldTrimNo = 1
        StybldTrimInputWalls = 2
        StybldTrimInputBlends = 3
    

    class StybldTrans(enum.Enum):
        StybldTransConstant = 0
        StybldTransLinear = 1
        StybldTransNonInflecting = 2
        StybldTransSShaped = 3
    

    class StybldStiff(enum.Enum):
        StybldStiffAuto = 0
        StybldStiffLow = 1
    

    class UFStudioStybldShapeTrans():
        trans_type: UF.UFStudio.StybldTrans
        start: float
        end: float
        peak: float
        slope: float
        position: float
    

    class StybldMinrad(enum.Enum):
        StybldMinradNone = 0
        StybldMinradBound = 1
        StybldMinradPeak = 2
    

    class StybldMethod(enum.Enum):
        StybldMethodCurves = 0
        StybldMethodLaw = 1
        StybldMethodProfile = 2
    

    class StybldDirect(enum.Enum):
        StybldDirectNoSpecific = 0
        StybldDirectPerpendicular = 1
        StybldDirectIsoU = 2
        StybldDirectIsoV = 3
    

    class UFStudioStybldData():
        method: UF.UFStudio.StybldMethod
        num_faces1: int
        faces1: typing.List[Tag]
        reverse_normal1: bool
        num_faces2: int
        faces2: typing.List[Tag]
        reverse_normal2: bool
        floating_mode: bool
        edge_1: Tag
        edge_2: Tag
        trim_1: float
        trim_2: float
        continuity_blend_1: UF.UFStudio.StybldCont
        continuity_blend_2: UF.UFStudio.StybldCont
        spine: typing.List[UF.StringList]
        profile_curve: typing.List[UF.StringList]
        depth: UF.UFStudio.StybldShapeTrans
        skew: UF.UFStudio.StybldShapeTrans
        distance_tol: float
        angle_tol: float
        reverse_direction1: bool
        reverse_direction2: bool
        continuity1: UF.UFStudio.StybldCont
        continuity2: UF.UFStudio.StybldCont
        direction1: UF.UFStudio.StybldDirect
        direction2: UF.UFStudio.StybldDirect
        stiffness: UF.UFStudio.StybldStiff
        trim: UF.UFStudio.StybldTrim
        curve1: typing.List[UF.StringList]
        curve2: typing.List[UF.StringList]
        curve_trans1: UF.UFStudio.StybldCurveTrans
        curve_trans2: UF.UFStudio.StybldCurveTrans
        center_curve: typing.List[UF.StringList]
        reverse_center_curve: bool
        center_as_spine: int
        start_extension: float
        end_extension: float
        min_radius_mode: UF.UFStudio.StybldMinrad
        min_radius: str
        v_degree: UF.UFStudio.StybldVDegree
    

    class UFStudioStybldCurveTrans():
        trans_type: UF.UFStudio.StybldTrans
        start: str
        end: str
        peak: str
        slope: float
        position: float
    

    class StybldCont(enum.Enum):
        StybldContTangent = 0
        StybldContCurvature = 1
        StybldContG3 = 2
        StybldContPosition = 3
    

class UFStd(Utilities.NXRemotableObject):
    def AskStlFileType(self, filename: str, file_type: int) -> None:
        ...
    def CloseStlFile(self, file_handle: int) -> None:
        ...
    def CreateActivewebFile(self, working_directory: str, base_name: str, geom_server: str, server_directory: str, geometry_directory: str, attribute_server: str, attribute_directory: str, local_server_directory: str, local_geom_directory: str, local_web_directory: str, tolerance: float, mode_flags: int) -> None:
        ...
    def CreateVrmlFile(self, file_name: str, tolerance: float, mode_flags: int) -> None:
        ...
    def ExportIcadGeometry(self, file_spec: str, objects: typing.List[Tag], count: int) -> None:
        ...
    def ImportIcadGeometry(self, file_spec: str, matrix: float, ug_tag: Tag) -> None:
        ...
    def ImportStlAsciiFile(self, filename: str, parameters: UF.UFStd.StlParams, parser_line: int, num_topologies: int, topologies: typing.List[Tag], facets_per_topol: int) -> None:
        ...
    def ImportStlBinaryFile(self, filename: str, parameters: UF.UFStd.StlParams, num_facets: int, topology: Tag) -> None:
        ...
    def ImportVrmlFile(self, filename: str, parameters: UF.UFStd.VrmlParams, num_errors: int, num_warnings: int, n_topologies: int, topologies: typing.List[Tag]) -> None:
        ...
    def OpenBinaryStlFile(self, file_name: str, append: bool, header: str, file_handle: int) -> None:
        ...
    def OpenTextStlFile(self, file_name: str, append: bool, file_handle: int) -> None:
        ...
    def PutSheetsInStlFile(self, file_handle: int, csys: Tag, num_sheets: int, sheets: typing.List[Tag], min_edge_len: float, max_edge_len: float, facet_toler: float, adj_toler: float, num_negated: int, negated: typing.List[Tag], num_errors: int, error_info: typing.List[UF.UFStd.StlError]) -> None:
        ...
    def PutSolidInStlFile(self, file_handle: int, csys: Tag, body: Tag, min_edge_len: float, max_edge_len: float, facet_toler: float, num_errors: int, error_info: typing.List[UF.UFStd.StlError]) -> None:
        ...
    def SetCgmSizeMode(self, size_mode: int, size_values: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetDefaultStlParams(self, _params: UF.UFStd.StlParams) -> None:
        ...
    def SetDefaultVrmlParams(self, _params: UF.UFStd.VrmlParams) -> None:
        ...


    class UFStdVrmlParams():
        angular_tolerance: float
        unit_size: int
        generate_all_lod: bool
        hide_smooth_edges: bool
        generate_one_model: bool
        more_details: bool
        use_cache: bool
        suppress_warnings: bool
    

    class UFStdStlParams():
        angular_tolerance: float
        unit_size: int
        hide_smooth_edges: bool
        display_info: bool
        to_jt_body: int
    

    class UFStdStlError():
        error_code: int
        _object: Tag
        related: int
        point1: float
        point2: float
    

class UFSo(Utilities.NXRemotableObject):
    def Ask3ScalarsOfPoint(self, so_point: Tag, scalars: typing.List[Tag]) -> None:
        ...
    def AskAssyCtxtPartOcc(self, assy_context_xform: Tag, to_part_occ: Tag, from_part_occ: Tag) -> None:
        ...
    def AskChildren(self, _object: Tag, options: int, n_children: int, children: typing.List[Tag]) -> None:
        ...
    def AskDirectionOfAxis(self, axis: Tag, direction: float) -> None:
        ...
    def AskDirectionOfDirr(self, direction: Tag, dir: float) -> None:
        ...
    def AskDirrOnSurf(self, direction: Tag, dirr_on_surf_data: UF.UFSo.DirrOnSurfData) -> None:
        ...
    def AskDisplayMarkerOfPoint(self, point: Tag, disp_marker: UF.UFDisp.PolyMarker) -> None:
        ...
    def AskDoubleOfScalar(self, scalar: Tag, dbl: float) -> None:
        ...
    def AskExpOfScalar(self, scalar: Tag, exp: Tag) -> None:
        ...
    def AskMatrixOfXform(self, xform: Tag, matrix: float) -> None:
        ...
    def AskOffsetCurveCvtr(self, curvature: Tag, offset_curve_cvtr_data: UF.UFSo.OffsetCurveCvtrData) -> None:
        ...
    def AskOffsetOfOffset(self, offset: Tag, offset_vec: float) -> None:
        ...
    def AskOffsetSurfCvtr(self, curvature: Tag, offset_surf_cvtr_data: UF.UFSo.OffsetSurfCvtrData) -> None:
        ...
    def AskParentStatus(self, so: Tag, parent_status: int) -> None:
        ...
    def AskParents(self, so: Tag, options: int, n_parents: int, parents: typing.List[Tag]) -> None:
        ...
    def AskPointOfAxis(self, axis: Tag, point: float) -> None:
        ...
    def AskPointOfXform(self, xform: Tag, point: float) -> None:
        ...
    def AskScaleOfXform(self, xform: Tag, scale: float) -> None:
        ...
    def AskSpline(self, spline: Tag, spline_data: UF.UFSo.SplineData) -> None:
        ...
    def AskUpdateErrorCode(self, so: Tag, update_error_code: int) -> None:
        ...
    def AskVisibilityOption(self, so: Tag, visibility_option: UF.UFSo.VisibilityOption) -> None:
        ...
    def AskXDirectionOfXform(self, xform: Tag, x_direction: float) -> None:
        ...
    def AskYDirectionOfXform(self, xform: Tag, y_direction: float) -> None:
        ...
    def AskZDirectionOfXform(self, xform: Tag, z_direction: float) -> None:
        ...
    def CreateArcCenter2Pnts(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, points: typing.List[Tag], arc: Tag) -> None:
        ...
    def CreateArcRadiusAngles(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, xform: Tag, radius: Tag, angles: typing.List[Tag], arc: Tag) -> None:
        ...
    def CreateArcThreePoints(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, points: typing.List[Tag], arc: Tag) -> None:
        ...
    def CreateArcXform2Points(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, xform: Tag, points: typing.List[Tag], arc: Tag) -> None:
        ...
    def CreateAxisDoubles(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: float, direction: float, axis: Tag) -> None:
        ...
    def CreateAxisExtract(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, axis: Tag, xform: Tag, axis2: Tag) -> None:
        ...
    def CreateAxisPointDir(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: Tag, direction: Tag, axis: Tag) -> None:
        ...
    def CreateBcurveThruPoints(self, update_option: UF.UFSo.UpdateOption, num_of_points: int, points: typing.List[Tag], point_parameters: float, degree: int, periodic: int, start_slope: Tag, end_slope: Tag, start_slope_type: int, end_slope_type: int, bcurve: Tag) -> None:
        ...
    def CreateCurveExtract(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, curve1: Tag, type: int, subtype: int, xform: Tag, curve2: Tag) -> None:
        ...
    def CreateDirrAxisOfConic(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, conic: Tag, flip: bool, direction: Tag) -> None:
        ...
    def CreateDirrDoubles(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, direction: float, dirr: Tag) -> None:
        ...
    def CreateDirrDoublesPnt(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: float, direction: float, dirr: Tag) -> None:
        ...
    def CreateDirrExtract(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, dir: Tag, xform: Tag, direction: Tag) -> None:
        ...
    def CreateDirrLine(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, line: Tag, flip: bool, direction: Tag) -> None:
        ...
    def CreateDirrNormalToSurfacePoint(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, face: Tag, point: Tag, flip: bool, direction: Tag) -> None:
        ...
    def CreateDirrOnCurve(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, curve: Tag, t: Tag, option: UF.UFSo.DirrOnCurveOption, flip: bool, direction: Tag) -> None:
        ...
    def CreateDirrOnSurf(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, dirr_on_surf_data: UF.UFSo.DirrOnSurfData, direction: Tag) -> None:
        ...
    def CreateDirrPlane(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, plane: Tag, flip: bool, direction: Tag) -> None:
        ...
    def CreateDirrSurfaceAxis(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, conic: Tag, flip: bool, direction: Tag) -> None:
        ...
    def CreateDirrTwoDirs(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, directions: typing.List[Tag], direction: Tag) -> None:
        ...
    def CreateDirrTwoPoints(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, points: typing.List[Tag], dirr: Tag) -> None:
        ...
    def CreateLineTwoPoints(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, points: typing.List[Tag], line: Tag) -> None:
        ...
    def CreateOffset3Scalars(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, xyz: typing.List[Tag], offset: Tag) -> None:
        ...
    def CreateOffsetCurveCvtr(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, offset_curve_cvtr_data: UF.UFSo.OffsetCurveCvtrData, curvature: Tag) -> None:
        ...
    def CreateOffsetCylindrical(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, radius: Tag, angle: Tag, zdelta: Tag, offset: Tag) -> None:
        ...
    def CreateOffsetDirDist(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, direction: Tag, distance: Tag, offset: Tag) -> None:
        ...
    def CreateOffsetDouble(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, offset1: float, offset2: Tag) -> None:
        ...
    def CreateOffsetDoublePnt(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: float, offset1: float, offset2: Tag) -> None:
        ...
    def CreateOffsetExtract(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, offset1: Tag, xform: Tag, offset2: Tag) -> None:
        ...
    def CreateOffsetSpherical(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, radius: Tag, angle1: Tag, angle2: Tag, offset: Tag) -> None:
        ...
    def CreateOffsetSurfCvtr(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, offset_surf_cvtr_data: UF.UFSo.OffsetSurfCvtrData, curvature: Tag) -> None:
        ...
    def CreatePoint3Scalars(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, xyz: typing.List[Tag], point: Tag) -> None:
        ...
    def CreatePoint3ScalarsCsys(self, object_in_part: Tag, csys_tag: Tag, xyz: typing.List[Tag], update_option: UF.UFSo.UpdateOption, point: Tag) -> None:
        ...
    def CreatePointAlongCurve(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, curve: Tag, point1: Tag, t: Tag, option: UF.UFSo.PointAlongCurveOption, flip: bool, point2: Tag) -> None:
        ...
    def CreatePointConicCenter(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, conic: Tag, point: Tag) -> None:
        ...
    def CreatePointExtract(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point1: Tag, xform: Tag, point2: Tag) -> None:
        ...
    def CreatePointExtractWithDispMarker(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point1: Tag, xform: Tag, disp_marker: UF.UFDisp.PolyMarker, point2: Tag) -> None:
        ...
    def CreatePointOffset(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, base_point: Tag, offset: Tag, point: Tag) -> None:
        ...
    def CreatePointOnArcAngle(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, arc: Tag, angle: Tag, xform: Tag, point: Tag) -> None:
        ...
    def CreatePointOnAxis(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, ref_point: Tag, axis: Tag, point_on_axis: Tag) -> None:
        ...
    def CreatePointOnCurve(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, curve: Tag, t: Tag, point: Tag) -> None:
        ...
    def CreatePointOnSurface(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, face: Tag, u: Tag, v: Tag, point: Tag) -> None:
        ...
    def CreatePointSurfaceCrv(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, face: Tag, curve: Tag, help_point1: Tag, help_point2: Tag, point: Tag) -> None:
        ...
    def CreatePointTwoCurves(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, curve1: Tag, curve2: Tag, help_point1: Tag, help_point2: Tag, point: Tag) -> None:
        ...
    def CreateScalarDist2Pnts(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, points: typing.List[Tag], scalar: Tag) -> None:
        ...
    def CreateScalarDouble(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, dbl: float, scalar: Tag) -> None:
        ...
    def CreateScalarDoubleDim(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, dbl: float, dim: UF.UFSo.ScalarDimOption, scalar: Tag) -> None:
        ...
    def CreateScalarExp(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, exp: Tag, scalar: Tag) -> None:
        ...
    def CreateScalarExpDim(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, exp: Tag, dim: UF.UFSo.ScalarDimOption, scalar: Tag) -> None:
        ...
    def CreateScalarExtract(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, scalar1: Tag, scale: Tag, scalar2: Tag) -> None:
        ...
    def CreateScalarExtractDim(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, scalar1: Tag, scale: Tag, dim: UF.UFSo.ScalarDimOption, scalar2: Tag) -> None:
        ...
    def CreateScalarLengthCrv(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, curve: Tag, scalar: Tag) -> None:
        ...
    def CreateSpline(self, update_option: UF.UFSo.UpdateOption, spline_data: UF.UFSo.SplineData, spline: Tag) -> None:
        ...
    def CreateXformAssyCtxt(self, object_in_part: Tag, from_part_occ: Tag, to_part_occ: Tag, xform: Tag) -> None:
        ...
    def CreateXformDoubles(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: float, x_direction: float, y_direction: float, scale: float, xform: Tag) -> None:
        ...
    def CreateXformExtract(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, xform1: Tag, xform2: Tag, xform: Tag) -> None:
        ...
    def CreateXformOffsetXform(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, csys: Tag, point0: Tag, point1: Tag, rot_scalar_tags: typing.List[Tag], scale: Tag, xform: Tag) -> None:
        ...
    def CreateXformPntXyDirs(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: Tag, x_direction: Tag, y_direction: Tag, scale: Tag, xform: Tag) -> None:
        ...
    def CreateXformPntXzDirs(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: Tag, x_direction: Tag, z_direction: Tag, scale: Tag, xform: Tag) -> None:
        ...
    def CreateXformPntYzDirs(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point: Tag, y_direction: Tag, z_direction: Tag, scale: Tag, xform: Tag) -> None:
        ...
    def CreateXformThreePlanes(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, plane0: Tag, plane1: Tag, plane2: Tag, scale: Tag, xform: Tag) -> None:
        ...
    def CreateXformThreePoints(self, object_in_part: Tag, update_option: UF.UFSo.UpdateOption, point0: Tag, point1: Tag, point2: Tag, scale: Tag, xform: Tag) -> None:
        ...
    def DeleteNonDeletables(self, part: Tag) -> None:
        ...
    def DeleteParms(self, so: Tag) -> None:
        ...
    def Display(self, so: Tag, view_option: int, color_option: int, color: int) -> None:
        ...
    def DisplayParents(self, so: Tag, view_option: int, color_option: int, color: int) -> None:
        ...
    def HasBecomeDumb(self, so: Tag, has_become_dumb: bool) -> None:
        ...
    def IsAssyCtxtXform(self, xform: Tag, is_assy_xform: bool) -> None:
        ...
    def IsOutOfDate(self, so: Tag, is_out_of_date: bool) -> None:
        ...
    def IsSo(self, candidate: Tag, is_so: bool) -> None:
        ...
    def IsSubclass(self, candidate: Tag, is_so: bool) -> None:
        ...
    def ReplaceParms(self, old_so: Tag, new_so: Tag) -> None:
        ...
    def SetDirectionOfAxis(self, axis: Tag, new_direction: float) -> None:
        ...
    def SetDirectionOfDirr(self, direction: Tag, dir: float) -> None:
        ...
    def SetDisplayMarkerOfPoint(self, point: Tag, disp_marker: UF.UFDisp.PolyMarker) -> None:
        ...
    def SetDoubleOfScalar(self, scalar: Tag, dbl: float) -> None:
        ...
    def SetOffsetOfOffset(self, offset: Tag, new_offset: float) -> None:
        ...
    def SetPointOfAxis(self, axis: Tag, new_point: float) -> None:
        ...
    def SetPointOfXform(self, xform: Tag, point: float) -> None:
        ...
    def SetScaleOfXform(self, xform: Tag, scale: float) -> None:
        ...
    def SetVisibilityOption(self, so: Tag, visibility_option: UF.UFSo.VisibilityOption) -> None:
        ...
    def SetXyDirectionOfXform(self, xform: Tag, x_direction: float, y_direction: float) -> None:
        ...


    class VisibilityOption(enum.Enum):
        Invisible = 0
        Visible = 1
        VisibleIfParentInvisible = 2
    

    class UpdateOption(enum.Enum):
        DontUpdate = 0
        UpdateWithinModeling = 1
        UpdateAfterModeling = 2
        UpdateAfterParentBody = 3
        UpdateMixed = 4
    

    class UFSoSplineData():
        method: int
        degree: int
        periodic: int
        nump: int
        itype: int
        position: typing.List[Tag]
        parameter: float
        direction: typing.List[Tag]
        magnitude: typing.List[Tag]
        curvature: typing.List[Tag]
        symmetric: int
    

    class ScalarDimOption(enum.Enum):
        ScalarDimensionalityNone = 0
        ScalarDimensionalityLength = 1
        ScalarDimensionalityArea = 2
        ScalarDimensionalityVolume = 3
    

    class PointAlongCurveOption(enum.Enum):
        PointAlongCurveDistance = 0
        PointAlongCurvePercent = 1
    

    class UFSoOffsetSurfCvtrData():
        face: Tag
        uv: typing.List[Tag]
        option: int
        secdir: Tag
    

    class UFSoOffsetCurveCvtrData():
        curve: Tag
        t: Tag
    

    class UFSoDirrOnSurfData():
        face: Tag
        uv: typing.List[Tag]
        option: int
        secdir: Tag
        flip: bool
    

    class DirrOnCurveOption(enum.Enum):
        DirrOnCurveTangent = 0
        DirrOnCurveNormal = 1
        DirrOnCurveBinormal = 2
    

class UFSmd(Utilities.NXRemotableObject):
    def AskBendLineData(self, bend_line: Tag, bend_formula: str, angle: float, inside_radius: float, thickness: float, bend_allowance: float, material_side: int) -> None:
        ...
    def AskBendLines(self, flat_pattern: Tag, num_bend_lines: int, bend_lines: typing.List[Tag]) -> None:
        ...
    def AskBendSeqRecData(self, form_table: Tag, record_index: int, seq_data: typing.List[UF.UFSmd.SeqOutput], count: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskBendSeqTblData(self, form_table: Tag, seq_data: typing.List[UF.UFSmd.SeqOutput], count: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskBendTanLines(self, flat_pattern: Tag, num_bend_tan_lines: int, bend_tan_lines: typing.List[Tag]) -> None:
        ...
    def AskChildPipNodes(self, parent: Tag, n_pip_nodes: int, pip_nodes: typing.List[Tag]) -> None:
        ...
    def AskContourLines(self, flat_pattern: Tag, num_contour_lines: int, contour_lines: typing.List[Tag]) -> None:
        ...
    def AskFlatPattern(self, body: Tag, flat_pattern: Tag) -> None:
        ...
    def AskFormTbl(self, body: Tag, form_table: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskFormTblCount(self, form_table: Tag, count: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskFormTblCurrentSeq(self, form_table: Tag, record_index: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskFormTblData(self, form_table: Tag, form_data: typing.List[UF.UFSmd.FormOutput], count: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskFormableFeats(self, body: Tag, feat_list: typing.List[Tag]) -> None:
        ...
    def AskFormblkLines(self, flat_pattern: Tag, num_formblk_lines: int, formblk_lines: typing.List[Tag]) -> None:
        ...
    def AskFpAddCurves(self, body: Tag, num_additional_curves: int, additional_curves: typing.List[Tag]) -> None:
        ...
    def AskFpChildren(self, flat_pattern: Tag, parent: Tag, num_children: int, children: typing.List[Tag]) -> None:
        ...
    def AskFpFaces(self, body: Tag, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def AskFpParent(self, child: Tag, parent: Tag) -> None:
        ...
    def AskFpPrefs(self, fp_options: typing.List[UF.UFSmd.FpPrefs]) -> None:
        ...
    def AskGeneralPrefs(self, general_prefs: typing.List[UF.UFSmd.GenPrefs]) -> None:
        ...
    def AskPipNodeData(self, node: Tag, node_data: UF.UFSmd.PipNodeData) -> None:
        ...
    def ChkEntirePartStds(self, results: typing.List[UF.UFSmd.ChkStdResults]) -> None:
        ...
    def ChkFeatureStds(self, features: typing.List[Tag], num_features: int, results: typing.List[UF.UFSmd.ChkStdResults]) -> None:
        ...
    def ClearFormTbl(self, form_table: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateFlatPattern(self, name: str, layer: int, start_face: Tag, flat_pattern: Tag) -> None:
        ...
    def CreateFormTbl(self, body: Tag, form_table: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreatePipNode(self, node_data: UF.UFSmd.PipNodeData, node_tag: Tag) -> None:
        ...
    def CreateRepresentation(self, feature: Tag, hint_flag: int, new_feature: Tag) -> None:
        ...
    def DeleteBendSequence(self, form_table: Tag, record_index: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DeleteFlatPattern(self, flat_pattern: Tag) -> None:
        ...
    def DeletePipNode(self, node: Tag) -> None:
        ...
    def DeleteRepresentation(self, feature: Tag, new_feature: Tag) -> None:
        ...
    def EditPipNode(self, node: Tag, node_data: UF.UFSmd.PipNodeData) -> None:
        ...
    def EvalTrimAngles(self, curves: typing.List[Tag], num_curves: int, faces: typing.List[Tag], num_faces: int, dir_vec: float, equal_arc_len: float, num_of_pts: int, pts: typing.List[Tag], assoc_curves: typing.List[Tag], assoc_faces: typing.List[Tag], trim_ang_array: float) -> None:
        ...
    def ExecFormed(self, body: Tag) -> None:
        ...
    def ExecSequence(self, form_table: Tag, record_index: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def ExecUnformed(self, body: Tag) -> None:
        ...
    def ExecutePipNode(self, node: Tag) -> None:
        ...
    def Initialize(self) -> None:
        ...
    def IsInitialized(self) -> int:
        ...
    def LoadStandards(self, fspec: str) -> None:
        ...
    def SetFpPrefs(self, fp_options: UF.UFSmd.FpPrefs) -> None:
        ...
    def SetGeneralPrefs(self, general_prefs: UF.UFSmd.GenPrefs) -> None:
        ...
    def Terminate(self) -> None:
        ...
    def UpdateFlatPattern(self, body: Tag, flat_pattern: Tag) -> None:
        ...


    class UFSmdSeqOutput():
        design_angle: float
        process_angle: float
        inside_radius: float
        bend_allowance: float
        feature: Tag
        feature_name: str
        process_name: str
        bend_direction: str
        description: str
        baf: str
    

    class UFSmdSeqInput():
        process_angle: float
        feature: Tag
        process_name: str
        process_type: str
        description: str
    

    class RadiusTypeE(enum.Enum):
        RadiusInvalidOption = -1
        RadiusInside = 0
        RadiusOutside = 1
        RadiusNumItems = 2
    

    class PipTypeEnumE(enum.Enum):
        InvalidPipNodeType = -1
        PipProcess = 0
        PipUnformGroup = 1
        PipGroup = 2
        PipFormGroup = 3
        PipStep = 4
        PipUnformProcess = 5
        PipFormProcess = 6
        NumNodeType = 7
    

    class PipSequentialE(enum.Enum):
        SequentialProcInvalidOption = -1
        NonSequentialProcess = 0
        SequentialProcess = 1
        SequentialProcNumItems = 2
    

    class UFSmdPipNodeData():
        node_type: UF.UFSmd.PipTypeEnumE
        parent: Tag
        name: str
        feature_tag: Tag
        state_index: int
        proc_ang: float
    

    class UFSmdGenPrefs():
        seq_labels: int
        use_feat_stds: int
        chk_stds: int
        default_baf: str
        material: str
        thickness: str
        line_color: int
        enforce_cre_state: int
        mat_margin: str
        use_bat: int
        use_global_thickness: bool
        thickness_type: int
        use_global_radius: bool
        global_radius: str
        radius_type: UF.UFSmd.RadiusTypeE
        use_global_angle: bool
        global_angle: str
        angle_type: UF.UFSmd.AngleTypeE
        baf_option: UF.UFSmd.BafOptionsE
        use_global_baf: bool
        forming_method: UF.UFSmd.FormingMethodE
        bat_radius_type: UF.UFSmd.BatRadiusTypeE
        bat_angle_type: UF.UFSmd.BatAngleTypeE
        pip_sequential: UF.UFSmd.PipSequentialE
    

    class UFSmdFpPrefs():
        angle_tol: float
        chord_tol: float
        grid_size: float
        layer: int
        distortion_constraint: int
        fp_orientation: int
        curve_set: int
        tangent_lines: bool
        center_lines: bool
        form_block_curves: bool
        contour_curves: bool
        multiple_fp: bool
        auto_update: bool
        use_baf: bool
        name: str
        fp_algorithm: int
    

    class UFSmdFormOutput():
        process_name: str
        process_type: str
        description: str
    

    class FormingMethodE(enum.Enum):
        FormingMethodInvalidOption = -1
        UseSelfFormingFeatures = 0
        UseFormingOperations = 1
        FormingMethodNumItems = 2
    

    class UFSmdChkStdResults():
        num_objects: int
        results: str
    

    class BatRadiusTypeE(enum.Enum):
        BatRadiusInvalidOption = -1
        BatRadiusInside = 0
        BatRadiusOutside = 1
        BatRadiusNumItems = 2
    

    class BatAngleTypeE(enum.Enum):
        BatAngleInvalidOption = -1
        BatAngleBend = 0
        BatAngleIncluded = 1
        BatAngleNumItems = 2
    

    class BafOptionsE(enum.Enum):
        BafInvalidOption = -1
        BafUseExpression = 0
        BafUseTcl = 1
        BafUseSprdsheet = 2
        BafNumItems = 3
    

    class AngleTypeE(enum.Enum):
        AngleInvalidOption = -1
        AngleBend = 0
        AngleIncluded = 1
        AngleNumItems = 2
    

class UFSket(Utilities.NXRemotableObject):
    def AddConics(self, sketch_tag: Tag, count: int, _object: typing.List[Tag]) -> None:
        ...
    def AddExtractedObjects(self, sketch_tag: Tag, count: int, objects: typing.List[Tag], output_mode: int, num_extracted_objs: int, extracted_objs: typing.List[Tag]) -> None:
        ...
    def AddObjects(self, sketch_tag: Tag, count: int, _object: typing.List[Tag]) -> None:
        ...
    def AskActiveSketch(self, sketch_tag: Tag) -> None:
        ...
    def AskConIsInferred(self, con_tag: Tag, inferred_con_fl: bool) -> None:
        ...
    def AskConstraintClass(self, con_tag: Tag, con_class: UF.UFSket.ConClass) -> None:
        ...
    def AskConstraintType(self, con_tag: Tag, con_type: UF.UFSket.ConType) -> None:
        ...
    def AskConstraintsOfGeometry(self, sketch_tag: Tag, geom_tag: Tag, con_class: UF.UFSket.ConClass, con_num: int, con_tags: typing.List[Tag]) -> None:
        ...
    def AskConstraintsOfSketch(self, sketch_tag: Tag, con_class: UF.UFSket.ConClass, num_cons: int, con_tags: typing.List[Tag]) -> None:
        ...
    def AskDimStatus(self, dim_tag: Tag, exp_tag: Tag, exp_string: str, value: float, status: int) -> None:
        ...
    def AskDimensionsOfSketch(self, sketch_tag: Tag, num_dims: int, dim_tags: typing.List[Tag]) -> None:
        ...
    def AskExpsOfSketch(self, sketch_tag: Tag, num_exps: int, expression_tags: typing.List[Tag]) -> None:
        ...
    def AskFaceSketches(self, _object: Tag, object_list: typing.List[Tag]) -> None:
        ...
    def AskFeatureSketches(self, feature: Tag, object_list: typing.List[Tag]) -> None:
        ...
    def AskGeoConsOfGeometry(self, sketch_tag: Tag, geom_tag: Tag, con_num: int, con_tags: typing.List[Tag]) -> None:
        ...
    def AskGeoConsOfSketch(self, sketch_tag: Tag, num_cons: int, con_tags: typing.List[Tag]) -> None:
        ...
    def AskGeomsOfSketch(self, sketch_tag: Tag, num_geoms: int, geom_tags: typing.List[Tag]) -> None:
        ...
    def AskInferredConsOfSketch(self, sketch_tag: Tag, num_cons: int, con_tags: typing.List[Tag]) -> None:
        ...
    def AskLegacyPreferences(self, snap_angle: float, cap_dist: float, pt_name: str, auto_flag: int, show_flag: int, char_size: float, dec_places: int, ext_lines: int, dim_label: int) -> None:
        ...
    def AskPreferences(self, sketch_tag: Tag, snap_angle: float, name_prefix: str, vertex_prefix: str, line_prefix: str, arc_prefix: str, conic_prefix: str, spline_prefix: str, char_size: float, dec_places: int, dim_label: int) -> None:
        ...
    def AskReferenceStatus(self, skt_tag: Tag, member: Tag, status: UF.UFSket.ReferenceStatus) -> None:
        ...
    def AskSketFrecEid(self, sket_eid: Tag, sket_frec_eid: Tag) -> None:
        ...
    def AskSketchFeatures(self, sketch_tag: Tag, object_list: typing.List[Tag]) -> None:
        ...
    def AskSketchInfo(self, sketch_tag: Tag, sket_info: UF.UFSket.Info) -> None:
        ...
    def AskSketchOfGeom(self, geom_tag: Tag, sketch_tag: Tag) -> None:
        ...
    def AskSketchStatus(self, sketch_tag: Tag, sket_status: UF.UFSket.Status, dof_needed: int) -> None:
        ...
    def AttachToFace(self, sketch_tag: Tag, face_tag: Tag, ref_tag: Tag, ref_info: int, plane_dir: int, sketch_feature_tag: Tag) -> None:
        ...
    def CreateDimension(self, sketch_tag: Tag, dim_type: UF.UFSket.ConType, dim_object1: UF.UFSket.DimObject, dim_object2: UF.UFSket.DimObject, dim_origin: float, dim_tag: Tag) -> None:
        ...
    def CreateDimensionalConstraint(self, sketch_tag: Tag, dim_type: UF.UFSket.ConType, num_dim_obj: int, dim_objs: typing.List[UF.UFSket.DimObject], dim_origin: float, con_tag: Tag) -> None:
        ...
    def CreateGeometricConstraint(self, sketch_tag: Tag, con_type: UF.UFSket.ConType, num_con_geoms: int, con_geoms: typing.List[UF.UFSket.ConGeom], con_tag: Tag) -> None:
        ...
    def CreateSketch(self, name: str, option: int, matrix: float, _object: typing.List[Tag], reference: int, plane_dir: int, sketch_id: Tag) -> None:
        ...
    def DeleteConstraints(self, num_cons: int, con_tags: typing.List[Tag]) -> None:
        ...
    def DeleteDimensions(self, num_dims: int, dim_tags: typing.List[Tag]) -> None:
        ...
    def DeleteLegacyConstraint(self, type: int, obj_list: typing.List[Tag], assoc_var_list: int, delete_all: int) -> None:
        ...
    def InitializeSketch(self, name: str, _object: Tag) -> None:
        ...
    def IsOutOfDate(self, sket_eid: Tag, out_of_date: bool) -> None:
        ...
    def MirrorObjects(self, sketch_tag: Tag, center_line_tag: Tag, num_objs: int, obj_tags: typing.List[Tag], num_new_objs: int, new_obj_tags: typing.List[Tag], con_tags: typing.List[Tag]) -> None:
        ...
    def ReadDimension(self, sketch_tag: Tag, dim_tag: Tag, dim_type: UF.UFSket.ConType, dim_object1: UF.UFSket.DimObject, dim_object2: UF.UFSket.DimObject, dim_origin: float, dim_exp: Tag) -> None:
        ...
    def ReadDimensionalConstraint(self, sketch_tag: Tag, con_tag: Tag, dim_type: UF.UFSket.ConType, num_dim_obj: int, dim_objs: typing.List[UF.UFSket.DimObject], dim_origin: float, dim_tag: Tag, exp_tag: Tag) -> None:
        ...
    def ReadGeometricConstraint(self, sketch_tag: Tag, con_tag: Tag, con_type: UF.UFSket.ConType, geom_count: int, con_geoms: typing.List[UF.UFSket.ConGeom]) -> None:
        ...
    def SetLegacyPreferences(self, values: int, snap_angle: float, cap_dist: float, pt_name: str, auto_flag: int, show_flag: int, char_size: float, dec_places: int, ext_lines: int, dim_label: int) -> None:
        ...
    def SetPreferences(self, sketch_tag: Tag, values: int, snap_angle: float, name_prefix: str, vertex_prefix: str, line_prefix: str, arc_prefix: str, conic_prefix: str, spline_prefix: str, char_size: float, dec_places: int, dim_label: int) -> None:
        ...
    def SetReferenceStatus(self, skt_tag: Tag, member: Tag, status: UF.UFSket.ReferenceStatus) -> None:
        ...
    def TerminateSketch(self) -> None:
        ...
    def UpdateSketch(self, sketch_tag: Tag) -> None:
        ...


    class Status(enum.Enum):
        UnknownStatus = 0
        NotEvaluated = 1
        UnderConstrained = 2
        WellConstrained = 3
        OverConstrained = 4
        InconsistentlyConstrained = 5
    

    class ReferenceStatus(enum.Enum):
        Reference = 0
        Active = 1
    

    class UFSketInfo():
        subtype: int
        name: str
        csys_tag: Tag
        csys: float
        view_name: str
        datum_tag: Tag
        datum: float
    

    class HelpType(enum.Enum):
        NoHelpData = 0
        UseHelpPt = 1
        UseHelpParam = 2
    

    class GeomVertex(enum.Enum):
        NoVertex = 0
        StartVertex = 1
        EndVertex = 2
        CenterVertex = 3
        SplineDefiningPoint = 4
        AnchorVertex = 5
        SplinePole = 6
        MidVertex = 7
    

    class UFSketDimObject():
        object_tag: Tag
        object_assoc_type: UF.UFSket.AssocType
        object_assoc_mod_value: int
    

    class ConType(enum.Enum):
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
        PgmOffset = 37
        Normal = 38
        PointOnLoop = 39
        RecipeTrim = 40
        Pattern = 41
        RigidSet = 42
        G1 = 43
        G2 = 44
        Align = 45
        TangentToString = 46
        PerpendicularToString = 47
        ScalableSet = 48
        LastConType = 49
    

    class UFSketConGeom():
        geom_tag: Tag
        vertex_type: UF.UFSket.GeomVertex
        vertex_index: int
        use_help: UF.UFSket.HelpType
        help_point: float
        help_parameter: float
    

    class ConClass(enum.Enum):
        NoCons = 0
        AllCons = 1
        GeoCons = 2
        DimCons = 3
    

    class AssocType(enum.Enum):
        AssocTypeNone = 0
        EndPoint = 1
        ArcCenter = 2
        Tangency = 3
        CurvePoint = 4
        AnchorPoint = 5
    

class UFSim(Utilities.NXRemotableObject):
    def ActivateTool(self, engine: int, tool_name: str) -> None:
        ...
    def AskAxisDofJunction(self, engine: int, axis: str, jct_name: str, direction: UF.SvKimDegofDirection) -> None:
        ...
    def AskAxisIsReversalAllowed(self, engine: int, axis_name: str, allow_reversal: bool) -> None:
        ...
    def AskAxisLimits(self, engine: int, axis: str, min: float, max: float) -> None:
        ...
    def AskAxisPosition(self, engine: int, axis: str, position: float) -> None:
        ...
    def AskAxisRotaryDirMode(self, engine: int, axis_name: str, rot_mode: UF.UFSim.AxisRotDirType) -> None:
        ...
    def AskCompFromDof(self, engine: int, degof_name: str, comp_name: str) -> None:
        ...
    def AskCordingTol(self, engine: int, cording_tol: float) -> None:
        ...
    def AskDegofData(self, engine: int, degof_name: str, degof_type: UF.SimKimDegofTypes, lower_limit: float, upper_limit: float) -> None:
        ...
    def AskIfDegofExists(self, engine: int, degof_name: str, degof_exists: bool) -> None:
        ...
    def AskImmediateUpdate(self, engine: int, immediate_update: bool) -> None:
        ...
    def AskInitJunctionXform(self, engine: int, jct_name: str, xval: float, yval: float, zval: float, matrix: float) -> None:
        ...
    def AskIsJunctionDependent(self, engine: int, jct_name: str, axis_name: str, dependent: str) -> None:
        ...
    def AskIsJunctionExist(self, engine: int, jct_name: str, jct_exists: bool) -> None:
        ...
    def AskJunctionXform(self, engine: int, jct_name: str, xval: float, yval: float, zval: float, matrix: float) -> None:
        ...
    def AskKimCompNameById(self, engine: int, system_class: int, comp_id: str, comp_name: str) -> None:
        ...
    def AskMtcsJunction(self, engine: int, jct_name: str) -> None:
        ...
    def AskMtdUnits(self, engine: int, units: UF.UFSim.UnitType) -> None:
        ...
    def AskNcAxesOfMtool(self, engine: int, no_of_axes: int, axis_name_list: str) -> None:
        ...
    def AskSimEngine(self, mom_id: int, engine_id: int) -> None:
        ...
    def AskStatusSendNcCommandMsg(self, engine: int, status: bool) -> None:
        ...
    def AskToolOffsets(self, engine: int, tool_name: str, xval: float, yval: float, zval: float) -> None:
        ...
    def ConvertNurbsToPositionData(self, engine: int, cntr_point_count: int, order: int, knot_count: int, knots: float, cntr_points: float, point_count: int, positions: float) -> None:
        ...
    def CreateJunction(self, engine: int, jct_name: str, destination_comp: str, origin: float, matrix: float) -> None:
        ...
    def DbgEnd(self, engine: int) -> None:
        ...
    def DbgSetOutput(self, engine: int, on_off: bool, token: str) -> None:
        ...
    def DbgStart(self, engine: int, title: str) -> None:
        ...
    def DbgWriteMessage(self, engine: int, msg: str) -> None:
        ...
    def Delay(self, engine: int, label: str, duration: float) -> None:
        ...
    def DeleteJunction(self, engine: int, jct_name: str) -> None:
        ...
    def DialogSetItem(self, engine: int, item_id: str, attributes: str) -> None:
        ...
    def EndOfSimulation(self, engine: int) -> None:
        ...
    def FeedbackMessage(self, engine: int, label: str, message: str) -> None:
        ...
    def FindCompByName(self, engine: int, start_comp: str, search_comp: str, is_found: bool) -> None:
        ...
    def MountKimComp(self, engine: int, source_comp: str, source_jct: str, destination_comp: str, destination_jct: str, duration: float) -> None:
        ...
    def MountTool(self, engine: int, tool_class: UF.UFSim.ToolClass, tool_id: str, destination_comp: str, destination_jct: str, duration: float, tool_name: str) -> None:
        ...
    def MoveLinearAxis(self, engine_id: int, axis: str, value: float, duration: float) -> None:
        ...
    def MoveRotaryAxis(self, engine_id: int, axis: str, value: float, duration: float) -> None:
        ...
    def MsgNcCommand(self, engine: int, action: str) -> None:
        ...
    def MsgProgramMark(self, engine: int, program_mark: str) -> None:
        ...
    def MsgUserFeedback(self, engine: int, proc: str) -> None:
        ...
    def MtdInit(self, engine: int) -> None:
        ...
    def MtdReset(self, engine: int) -> None:
        ...
    def SetAxisAllowReversal(self, engine: int, axis_name: str, allow_reversal: bool) -> None:
        ...
    def SetAxisRotaryDirMode(self, engine: int, axis_name: str, rot_mode: UF.UFSim.AxisRotDirType) -> None:
        ...
    def SetChannel(self, engine: int, channel_number: int) -> None:
        ...
    def SetCoolant(self, engine: int, value: int, duration: float) -> None:
        ...
    def SetCurrentZcsJunction(self, engine: int, junction_name: str) -> None:
        ...
    def SetCuttingMode(self, engine: int, mode: UF.UFSim.CuttingMode) -> None:
        ...
    def SetFeed(self, engine: int, value: float, unit: UF.UFSim.UnitType, duration: float) -> None:
        ...
    def SetImmediateUpdate(self, engine: int, immediate_update: bool) -> None:
        ...
    def SetMtdUnits(self, engine: int, units: UF.UFSim.UnitType) -> None:
        ...
    def SetParameter(self, engine: int, label: str, text: str, unit: UF.UFSim.UnitType, duration: float) -> None:
        ...
    def SetSpeed(self, engine: int, value: float, unit: UF.UFSim.UnitType, duration: float) -> None:
        ...
    def SetStatusSendNcCommandMsg(self, engine: int, status: bool) -> None:
        ...
    def StartOfSimulation(self, engine: int) -> None:
        ...
    def Step(self, engine: int, label: str) -> None:
        ...
    def TransformMatrixAcsToMtcs(self, engine: int, acs_matrix: float, matrix: float) -> None:
        ...
    def TransformOffsetAcsToMtcs(self, engine: int, acs_vector: float, xval: float, yval: float, zval: float) -> None:
        ...
    def UnmountKimComp(self, engine: int, component: str, duration: float) -> None:
        ...
    def UnmountTool(self, engine: int, tool_name: str, duration: float) -> None:
        ...
    def Update(self, engine: int, label: str) -> None:
        ...


    class UnitType(enum.Enum):
        UnitNone = 0
        UnitMm = 1
        UnitM = 2
        UnitInch = 3
        UnitFeet = 4
        UnitSec = 5
        UnitMin = 6
        UnitMmPerSec = 7
        UnitMmPerMin = 8
        UnitMPerMin = 9
        UnitInchPerSec = 10
        UnitInchPerMin = 11
        UnitFeetPerMin = 12
        UnitRevPerSec = 13
        UnitRevPerMin = 14
        UnitDegPerMin = 15
        UnitMmPerRev = 16
        UnitInchPerRev = 17
        UnitMmPer100rev = 18
        UnitMPerSecPow2 = 19
        UnitSfm = 20
        UnitSmm = 21
        UnitDegPerSec = 22
        UnitRadPerSec = 23
        UnitRadPerMin = 24
    

    class ToolClass(enum.Enum):
        ToolClassToolNumber = 0
        ToolClassLibraryRef = 1
        ToolClassCatalogNumber = 2
        ToolClassUgName = 3
        ToolClassCompName = 4
    

    class CuttingMode(enum.Enum):
        CuttingModeNone = 0
        CuttingModeCut = 1
        CuttingModeRapid = 2
    

    class AxisRotDirType(enum.Enum):
        AxisRotNone = 0
        AxisRotMagnitudeDeterminesDirection = 1
        AxisRotAlwaysShortest = 2
        AxisRotSignDeterminesDirection = 3
        AxisRotAlwaysClw = 4
        AxisRotAlwaysCclw = 5
    

class UFShopdoc(Utilities.NXRemotableObject):
    def GenerateDoc(self, doc_name: str, output_filename: str, output_units: UF.UFSetup.OutputUnits) -> None:
        ...


class UFSfPost(Utilities.NXRemotableObject):
    def AnimateCreateAnimation(self, model_num: int) -> None:
        ...
    def AnimateDeleteAnimation(self, model_num: int) -> None:
        ...
    def AnimateSetAnimCurFrame(self, model_num: int, cfrm: int) -> None:
        ...
    def AnimateSetAnimCurIter(self, model_num: int, citer: int) -> None:
        ...
    def AnimateSetAnimIter(self, model_num: int, iter_sw: bool) -> None:
        ...
    def AnimateSetAnimIters(self, model_num: int, siter: int, eiter: int) -> None:
        ...
    def AnimateSetAnimNumFrames(self, model_num: int, num_frm: int) -> None:
        ...
    def AnimateSetAnimType(self, model_num: int, ichoice: int) -> None:
        ...
    def AnimateStepAnimationFrame(self, model_num: int, truth: bool) -> None:
        ...


class UFSfLegend(Utilities.NXRemotableObject):
    def SetColors(self, color_attr_p: UF.SfColorAttr) -> None:
        ...


class UFSfl(Utilities.NXRemotableObject):
    def AskBcDescriptorNameNx(self, bc_desc_tag: Tag, name_pp: str) -> None:
        ...
    def AskBcDescriptorNx(self, language_tag: Tag, name: str, bc_descriptor_tag: Tag) -> None:
        ...
    def AskCurLanguageNx(self, language_tag: Tag) -> None:
        ...
    def AskElementDescriptorNameNx(self, elem_desc_tag: Tag, name_pp: str) -> None:
        ...
    def AskElementDescriptorNx(self, language_tag: Tag, name: str, elem_descriptor_tag: Tag) -> None:
        ...
    def AskLanguageNx(self, solver_desc_tag: Tag, lang_name: str, language_tag: Tag) -> None:
        ...
    def AskLoadDescriptorNameNx(self, load_desc_tag: Tag, name_pp: str) -> None:
        ...
    def AskLoadDescriptorNx(self, language_tag: Tag, name: str, load_descriptor_tag: Tag) -> None:
        ...
    def AskNthBcDescriptorNx(self, language_tag: Tag, index: int, bc_descriptor_tag: Tag) -> None:
        ...
    def AskNthElementDescriptorNx(self, language_tag: Tag, index: int, elem_descriptor_tag: Tag) -> None:
        ...
    def AskNthLanguageNx(self, solver_desc_tag: Tag, index: int, language_tag: Tag) -> None:
        ...
    def AskNthLoadDescriptorNx(self, language_tag: Tag, index: int, load_descriptor_tag: Tag) -> None:
        ...
    def AskNthSolutionDescriptorNx(self, language_tag: Tag, index: int, solution_descriptor_tag: Tag) -> None:
        ...
    def AskNthSolverNx(self, index: int, solver_desc_tag: Tag) -> None:
        ...
    def AskNumBcDescriptorsNx(self, language_tag: Tag, num_bc_descriptors: int) -> None:
        ...
    def AskNumElementDescriptorsNx(self, language_tag: Tag, num_elem_descriptors: int) -> None:
        ...
    def AskNumLanguagesNx(self, solver_desc_tag: Tag, num_languages: int) -> None:
        ...
    def AskNumLoadDescriptorsNx(self, language_tag: Tag, num_load_descriptors: int) -> None:
        ...
    def AskNumSolutionDescriptorsNx(self, language_tag: Tag, num_solution_descriptors: int) -> None:
        ...
    def AskNumSolversNx(self, num_solvers: int) -> None:
        ...
    def AskSolutionDescriptorNx(self, language_tag: Tag, name: str, solution_descriptor_tag: Tag) -> None:
        ...
    def AskSolverNx(self, solver_name: str, solver_desc_tag: Tag) -> None:
        ...
    def SetDefaultEnvNx(self, language_name: str) -> None:
        ...
    def SolutionAskLbcDescValidNx(self, sol_desc_tag: Tag, lbc_desc_tag: Tag, valid: bool) -> None:
        ...
    def SolutionAskNthAllowableStepDescriptorNx(self, sol_desc_tag: Tag, index: int, step_descriptor_tag: Tag) -> None:
        ...
    def SolutionAskNumAllowableStepDescriptorsNx(self, sol_desc_tag: Tag, num_allow_step_descs: int) -> None:
        ...
    def SolutionAskStepDescriptorNx(self, sol_desc_tag: Tag, step_desc_name: str, step_descriptor_tag: Tag) -> None:
        ...
    def SolutionDescriptorAskNameNx(self, sol_desc_tag: Tag, name_pp: str) -> None:
        ...
    def StepAskLbcDescValidNx(self, step_desc_tag: Tag, lbc_desc_tag: Tag, valid: bool) -> None:
        ...
    def StepDescriptorAskNameNx(self, step_desc_tag: Tag, name_pp: str) -> None:
        ...


class UFSfCurve(Utilities.NXRemotableObject):
    def CreateLineArc(self, line_arc_data: UF.UFCurve.LineArc, curve_id: Tag) -> None:
        ...


class UFSf(Utilities.NXRemotableObject):
    def AddToSolutionNx(self, num_of_lbc: int, lbc: Tag) -> None:
        ...
    def AddToStepNx(self, num_of_lbc: int, lbc: Tag) -> None:
        ...
    def AllocDefeatureParms(self, num_ret_faces: int, ret_faces_a: typing.List[Tag], num_rem_faces: int, rem_faces_a: typing.List[Tag], seed_face: Tag, num_bnd_faces: int, bnd_faces: typing.List[Tag], angle_exp: Tag, defeature_parms_p: typing.List[UF.UFSf.DefeatureParms]) -> None:
        ...
    def AllocIdealizeParms(self, parms_p: int) -> None:
        ...
    def AllocIdealizeRegion(self, seed_face: Tag, num_bnd_faces: int, bnd_faces: typing.List[Tag], angle_exp: Tag, region_p: int) -> None:
        ...
    def ApplyBeamEndMass(self, end_a_nsm_exp: str, end_b_nsm_exp: str, num_items: int, items_array: typing.List[Tag]) -> None:
        ...
    def AskActiveSolutionNx(self, active_solution: Tag) -> None:
        ...
    def AskActiveStepNx(self, active_step: Tag) -> None:
        ...
    def AskAllPolygonBodies(self, num_polygon_bodies: int, polygon_bodies: typing.List[Tag]) -> None:
        ...
    def AskBeamEndMass(self, object_tag: Tag, end_a_nsm: float, end_b_nsm: float) -> None:
        ...
    def AskClosestPoint(self, point: float, entity: Tag, closest_point: float, min_dist: float) -> None:
        ...
    def AskCombinedLoadCase(self, clc_tag: Tag, clc_name: str, num_comps: int, lbc_tags: typing.List[Tag], lbc_scales: float) -> None:
        ...
    def AskCombinedLoadCases(self, part_tag: Tag, num_clcs: int, clc_tags: typing.List[Tag]) -> None:
        ...
    def AskDomElmType(self, mesh_recipe: Tag, elm_type: UF.UFSf.ElementType) -> None:
        ...
    def AskDursolNx(self, dursol_tag: Tag, dursol_name: str, solution_tag: Tag, stress_criterion: UF.UFSf.DursolStressCriterion, stress_type: UF.UFSf.DursolStressType, design_life_criterion: UF.UFSf.DursolDesignLifeCriterion, fatigue_cycles: int, k_factor: float, fatigue_life_criterion: UF.UFSf.DursolFatigueLifeCriterion, design_cycles: int) -> None:
        ...
    def AskEdgeDensity(self, object_tag: Tag, edge_density_data_ptr: UF.UFSf.EdgeDensityData) -> None:
        ...
    def AskElement(self, elm_tag: Tag, elm_id: int, adaptivity: UF.UFSf.ElmAdaptivityType, dimension: UF.UFSf.ElmDimensionType, element_type: UF.UFSf.ElementType) -> None:
        ...
    def AskElementEdges(self, elem_tag: Tag, num_edges: int, start_nodes: typing.List[Tag], end_nodes: typing.List[Tag], mid_nodes: typing.List[Tag]) -> None:
        ...
    def AskElementTypeNames(self, element_type: UF.UFSf.ElementType, element_name_array: str) -> None:
        ...
    def AskGeomData(self, mesh_object: Tag, usage_type: UF.UFSf.MeshGeomUsage, num_geom_items: int, geom_items_p: typing.List[Tag]) -> None:
        ...
    def AskIdealizeParmExp(self, parms_p: int, parm_exp_t: UF.UFSf.IdealizeParmExp, exp_tag: Tag) -> None:
        ...
    def AskIdealizeParmFaces(self, parms_p: int, parm_face_t: UF.UFSf.IdealizeParmFace, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def AskIdealizeParms(self, feature_tag: Tag, is_region: bool, body_region: int, idealize_parms: int) -> None:
        ...
    def AskIdealizeRegion(self, region_p: int, seed_face: Tag, num_bnd_faces: int, bnd_faces: typing.List[Tag], angle_exp: Tag) -> None:
        ...
    def AskLanguage(self, language_tag: Tag, language_name: str, version: int, analysis_type: UF.SfLangAnalysisType, problem_abstraction: UF.SfLangProblemAbstract, linearity: UF.SfLangLinearity, time_dependency: UF.SfLangTimeDepend, solver_name: str) -> None:
        ...
    def AskLibraryMaterials(self, type_filter: str, category_filter: str, name_filter: str, material_count: int, material_librefs: str, material_names: str, material_types: str) -> None:
        ...
    def AskLvNx(self, lv_tag: Tag, lv_name: str, scaling_factor: float, count: int, function_type: UF.UFSf.LvFunctionMode, solution_step_tag: Tag) -> None:
        ...
    def AskMaterialType(self, material_tag: Tag, material_type: UF.UFSf.NeutralMaterialTypes) -> None:
        ...
    def AskMeshDimension(self, mesh_recipe: Tag, dimension: UF.UFSf.MeshDimension) -> None:
        ...
    def AskMeshMatingCondition(self, assembly_mesh_tag: Tag, assembling_geom: Tag, target_geom: Tag, assembly_name: str, seed_mesh: int, assembly_type: UF.UFSf.AssemblyType, merge_tolerance: float, match_tolerance: float) -> None:
        ...
    def AskMeshVisuals(self, mesh_tag: Tag, mesh_vis: UF.UFSf.MeshVisuals) -> None:
        ...
    def AskMidsrfFrecType(self, feature_tag: Tag, midsrf_type: int) -> None:
        ...
    def AskNode(self, node_tag: Tag, node_id: int, b_type: UF.UFSf.NodeBtype, e_type: UF.UFSf.MidNodeType, abspos: float) -> None:
        ...
    def AskNodePgeoms(self, node_tag: Tag, parent_cnt: int, parent_list: typing.List[Tag], geom_types: typing.List[UF.UFSf.MeshGeometryTypes]) -> None:
        ...
    def AskNthDursolNx(self, index: int, dursol_tag: Tag) -> None:
        ...
    def AskNthMeshRecipe(self, fem_tag: Tag, index: int, mesh_recipe_tag: Tag) -> None:
        ...
    def AskNthSolutionNx(self, solution: int, solution_tag: Tag) -> None:
        ...
    def AskNumDursolsNx(self, num_dursols: int) -> None:
        ...
    def AskNumMeshRecipes(self, fem_tag: Tag, num_mesh_recipes: int) -> None:
        ...
    def AskNumSolutionsNx(self, solution_count: int) -> None:
        ...
    def AskOffsetMidsrfThickness(self, midsrf_tag: Tag, thickness: float) -> None:
        ...
    def AskSolutionNx(self, lbc_tag: Tag, num_members: int, solution_pp: typing.List[Tag]) -> None:
        ...
    def AskStepNx(self, lbc_tag: Tag, num_members: int, step_pp: typing.List[Tag]) -> None:
        ...
    def AskUgs2dMeshParms(self, mesh_tag: Tag, mesh_parms: UF.UFSf.Ugs2dMeshParms) -> None:
        ...
    def AskUgsTetMeshParms(self, mesh_tag: Tag, mesh_parms: UF.UFSf.UgsTetMeshParms) -> None:
        ...
    def AutoCreateMeshMatingCondition(self, entity_num: int, entity_array: typing.List[Tag], merge_tolerance: float, make_mesh_coincident: int, coincident_face_only: int, mesh_mating_type: int, num_assembly_meshes: int, assembly_meshes: typing.List[Tag]) -> None:
        ...
    def AutoCreateSurfaceContactMesh(self, capture_distance: float, property: int, num_meshes: int, mesh_recipes: typing.List[Tag]) -> None:
        ...
    def BodyAskBoundingBox(self, cae_tag: Tag, pad_bounding_volume: float) -> None:
        ...
    def BodyAskEdges(self, cae_tag: Tag, num_edges: int, edges: typing.List[Tag]) -> None:
        ...
    def BodyAskFaces(self, cae_tag: Tag, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def BodyAskModlBody(self, cae_tag: Tag, modl_body_p: Tag) -> None:
        ...
    def BodyAskVolumeAndCentroid(self, cae_tag: Tag, pd_volume: float, centroid: float) -> None:
        ...
    def CaeInformation(self, info_type: UF.UFSf.ScenarioInfo, num_entities: int, entities_tags: typing.List[Tag], output_file_with_path: str) -> None:
        ...
    def CheckModelComprehensive(self, detailed_message: bool, ouput_file_with_path: str) -> None:
        ...
    def CheckModelDuplicateNodes(self, num_meshes: int, mesh_tags: Tag, merge_duplicates: bool, tolerance: float, num_duplicates: int) -> None:
        ...
    def CheckModelElementShapes(self, num_meshes: int, mesh_tags: typing.List[Tag], list_all_elems: bool, output_file_with_path: str, FILE: int) -> None:
        ...
    def CleanMshvldErrorContainer(self, container: UF.UFSf.MeshErrorContainer) -> None:
        ...
    def CloneScenario(self, master_part_tag: Tag, orig_scen: str, cloned_scen: str) -> None:
        ...
    def CloseScenario(self) -> None:
        ...
    def CountAllNodesOfValidElements(self, number_of_all_valid_nodes: int) -> None:
        ...
    def CountAllValidElements(self, number_of_all_valid_elements: int) -> None:
        ...
    def CountElements(self, mesh: Tag, number_of_elements: int) -> None:
        ...
    def CountNodes(self, mesh: Tag, number_of_nodes: int) -> None:
        ...
    def Create0dMesh(self, num_geom_objects: int, geom_array: typing.List[Tag], element_type: UF.UFSf._0D_element_type_, default_density: float, default_density_type: UF.UFSf._0D_density_type_, mass_value: float, mesh_tag: Tag) -> None:
        ...
    def Create0dMeshDistMass(self, num_geom_objects: int, geom_array: typing.List[Tag], element_type: UF.UFSf._0D_element_type_, default_density: float, default_density_type: UF.UFSf._0D_density_type_, mass_value: float, distribute_mass: int, mesh_tag: Tag) -> None:
        ...
    def Create1dConnectionMesh(self, mesh_data: UF.UFSf._1d_mesh_data_, orient_data: UF.UFSf.OrientationData, num_group1_objects: int, group1_array: typing.List[Tag], group1_direction_array: typing.List[UF.UFSf.MeshGeomMeshdir], num_group2_objects: int, group2_array: typing.List[Tag], group2_direction_array: typing.List[UF.UFSf.MeshGeomMeshdir], mesh_tag: Tag) -> None:
        ...
    def Create1dMesh(self, mesh_data: UF.UFSf._1d_mesh_data_, orient_data: UF.UFSf.OrientationData, num_group1_objects: int, group1_array: typing.List[Tag], num_group2_objects: int, group2_array: typing.List[Tag], mesh_tag: Tag) -> None:
        ...
    def CreateAutoFaceSubdiv(self, objects: typing.List[Tag], obj_count: int, distance_tolerance: float, subdivision_needed: int, face_search_option: int, resulting_pairs: typing.List[UF.UFSf.ResultingFacePairs], resulting_pairs_count: int) -> None:
        ...
    def CreateCombinedLoadCase(self, clc_name: str, num_comps: int, lbc_tags: typing.List[Tag], lbc_scales: float, clc_tag: Tag) -> None:
        ...
    def CreateContactMesh(self, mesh: Tag, mesh_data: UF.UFSf.ContactMeshData, orient_data: UF.UFSf.OrientationData) -> None:
        ...
    def CreateDefeatureBody(self, defeature_parms_p: UF.UFSf.DefeatureParms, feature_tag: Tag, n_failing_wound_edges: int, failing_wound_edges: typing.List[Tag]) -> None:
        ...
    def CreateDursolNx(self, name: str, solution_tag: Tag, dursol_tag: Tag) -> None:
        ...
    def CreateEdgeFaceConn(self, uf_ef_conn_info: UF.UFSf.EfConnInfo, mesh_tag: Tag) -> None:
        ...
    def CreateFem(self, fem_name: str, cad_part_tag: Tag, idealized_part_name: str, use_all_bodies_flag: bool, num_bodies: int, body_tags: typing.List[Tag], solver_name: str, analysis_type_name: str, num_desc_lines: int, description: str, new_fem_tag: Tag) -> None:
        ...
    def CreateFemWithGeomOpts(self, fem_name: str, cad_part_tag: Tag, idealized_part_name: str, use_all_bodies_flag: bool, num_bodies: int, body_tags: Tag, solver_name: str, analysis_type_name: str, num_desc_lines: int, description: str, geom_options: UF.UFSf.GeomOptions, new_fem_tag: Tag) -> None:
        ...
    def CreateHardpointOnGeom(self, geom_tag: Tag, ref_point: float, hardpoint_tag: Tag) -> None:
        ...
    def CreateIdealizeBody(self, body_tag: Tag, parms_p: int, feature_tag: Tag, n_failing_wound_edges: int, failing_wound_edges: typing.List[Tag]) -> None:
        ...
    def CreateIdealizeRegion(self, region_p: int, parms_p: int, feature_tag: Tag, n_failing_wound_edges: int, failing_wound_edges: typing.List[Tag]) -> None:
        ...
    def CreateLvNx(self, lv_name: str, scaling_factor: float, count: int, function_type: UF.UFSf.LvFunctionMode, solution_step_tag: Tag, dursol_tag: Tag, lv_tag: Tag) -> None:
        ...
    def CreateMeshMatingCondition(self, assembling_geom: Tag, target_geom: Tag, assembly_name: str, seed_mesh: int, assembly_type: UF.UFSf.AssemblyType, merge_tolerance: float, match_tolerance: float, assembly_mesh: Tag) -> None:
        ...
    def CreateOffsetMidsrf(self, seed_face: Tag, cliff_angle: float, percentage_dist: float, midsurface_tag: Tag) -> None:
        ...
    def CreateReport(self) -> None:
        ...
    def CreateScenarioNx(self, scenario_name: str, new_scenario_tag: Tag) -> None:
        ...
    def CreateSimulation(self, simulation_name: str, fem_tag: Tag, num_desc_lines: int, description: str, new_simulation_tag: Tag) -> None:
        ...
    def CreateSolutionNx(self, solution_desc: Tag, solver_desc: Tag, solution_name: str, solution_tag: Tag) -> None:
        ...
    def CreateStepNx(self, step_desc: Tag, step_name: str, solution_tag: Tag, step_tag: Tag) -> None:
        ...
    def CreateSurfaceContactMesh(self, source_face: Tag, target_face: Tag, property: int, mesh_recipe: Tag) -> None:
        ...
    def CreateSweptHexMesh(self, solid_body: Tag, source_face: Tag, midnodes: bool, elem_size: float, mesh_tag: Tag) -> None:
        ...
    def CreateUgs2dMesh(self, mesh_parms: UF.UFSf.Ugs2dMeshParms, num_geoms: int, geoms_p: typing.List[Tag], mesh_tag: Tag) -> None:
        ...
    def CreateUgs2dMeshWithHdpts(self, mesh_parms: UF.UFSf.Ugs2dMeshParms, num_geoms: int, geoms_p: typing.List[Tag], num_hardpoints: int, hardpoints_p: typing.List[Tag], mesh_tag: Tag) -> None:
        ...
    def CreateUgs2dMeshWtAbstractionControl(self, mesh_parms: UF.UFSf.Ugs2dMeshParms, abs_data_p: UF.UFSf.UgsMeshAbstractionParams, num_geoms: int, geoms_p: typing.List[Tag], mesh_tag: Tag) -> None:
        ...
    def CreateUgsTetMesh(self, mesh_parms: UF.UFSf.UgsTetMeshParms, num_bodies: int, bodies_p: typing.List[Tag], mesh_tag: Tag) -> None:
        ...
    def CreateUgsTetMeshWtAbstractionControl(self, mesh_parms: UF.UFSf.UgsTetMeshParms, abs_data_p: UF.UFSf.UgsMeshAbstractionParams, num_bodies: int, bodies_p: typing.List[Tag], f_partial_surf_mesh: int, mesh_tag: Tag) -> None:
        ...
    def CreateUserdefMidsrf(self, parms_p: UF.UFSf.MidsrfUserParms, feature_tag: Tag) -> None:
        ...
    def CreateWeldMesh(self, mesh_data: UF.UFSf._1d_mesh_data_, orient_data: UF.UFSf.OrientationData, num_objects: int, obj_array: typing.List[Tag], num_top_faces: int, top_face_array: typing.List[Tag], num_bot_faces: int, bot_face_array: Tag, mesh_tag: Tag) -> None:
        ...
    def DeleteDispResults(self, delete_legend_sw: int) -> None:
        ...
    def DeleteDursolNx(self, dursol_tag: Tag) -> None:
        ...
    def DeleteLvNx(self, dursol_tag: Tag, lv_tag: Tag) -> None:
        ...
    def DeleteMeshMatingCondition(self, num_mmc: int, mmc_array: typing.List[Tag]) -> None:
        ...
    def DeleteScenario(self, master_tag: Tag, scenario_name: str) -> None:
        ...
    def DeleteSolutionNx(self, solution: Tag) -> None:
        ...
    def DeleteStepNx(self, step: Tag) -> None:
        ...
    def DisplayMesh(self, mesh_tag: Tag) -> None:
        ...
    def DursolAddLoadNx(self, dursol_tag: Tag, lv_tag: Tag) -> None:
        ...
    def DursolAskLoadCountNx(self, dursol_tag: Tag, num_lv: int) -> None:
        ...
    def DursolAskLoadNx(self, dursol_tag: Tag, lv_index: int, lv_tag: Tag) -> None:
        ...
    def DursolLocateAllMembersNx(self, dursol_tag: Tag, num_lv: int, lv_pp: typing.List[Tag]) -> None:
        ...
    def DursolRemoveLoadNx(self, dursol_tag: Tag, lv_tag: Tag) -> None:
        ...
    def EdgeAskAdjacentEdges(self, cae_tag: Tag, num_edges: int, edges: typing.List[Tag]) -> None:
        ...
    def EdgeAskBody(self, cae_tag: Tag, body_p: Tag) -> None:
        ...
    def EdgeAskBoundingBox(self, cae_tag: Tag, pad_bounding_box: float) -> None:
        ...
    def EdgeAskEndPoints(self, cae_tag: Tag, start_pt: float, end_pt: float, start_tangent: float, end_tangent: float) -> None:
        ...
    def EdgeAskFaces(self, cae_tag: Tag, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def EdgeAskLength(self, cae_tag: Tag, pd_length: float) -> None:
        ...
    def EdgeEvaluateClosestPoint(self, cae_tag: Tag, ad_point: float, ad_out_point: float, pd_param: float) -> None:
        ...
    def EdgeEvaluateParamLocation(self, cae_tag: Tag, d_param: float, ad_out_point: float) -> None:
        ...
    def EditBeamOrientation(self, mesh_tag: Tag, orient_data: UF.UFSf.OrientationData) -> None:
        ...
    def EditDefeatureParms(self, feature_tag: Tag, defeature_parms_p: UF.UFSf.DefeatureParms, n_failing_wound_edges: int, failing_wound_edges: typing.List[Tag]) -> None:
        ...
    def EditDursolNx(self, dursol_tag: Tag, dursol_name: str, stress_criterion: UF.UFSf.DursolStressCriterion, stress_type: UF.UFSf.DursolStressType, design_life_criterion: UF.UFSf.DursolDesignLifeCriterion, fatigue_cycles: int, k_factor: float, fatigue_life_criterion: UF.UFSf.DursolFatigueLifeCriterion, design_cycles: int) -> None:
        ...
    def EditIdealizeParms(self, feature_tag: Tag, parms_p: int, n_failing_wound_edges: int, failing_wound_edges: typing.List[Tag]) -> None:
        ...
    def EditLvNx(self, lv_tag: Tag, lv_name: str, scaling_factor: float, count: int, function_type: UF.UFSf.LvFunctionMode) -> None:
        ...
    def EditMeshMatingCondition(self, num_mmc: int, mmc_array: typing.List[Tag], make_mesh_coincident: int, mesh_mating_type: int) -> None:
        ...
    def EditOffsetMidsrf(self, seed_face: Tag, cliff_angle: float, percentage_dist: float, midsurface_tag: Tag) -> None:
        ...
    def EditUserdefMidsrf(self, parms_p: UF.UFSf.MidsrfUserParms, feature_tag: Tag) -> None:
        ...
    def FaceAskAdjacentFaces(self, cae_tag: Tag, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def FaceAskArea(self, cae_tag: Tag, pd_area: float) -> None:
        ...
    def FaceAskBody(self, cae_tag: Tag, body_p: Tag) -> None:
        ...
    def FaceAskBoundingBox(self, cae_tag: Tag, pad_bounding_box: float) -> None:
        ...
    def FaceAskEdges(self, cae_tag: Tag, num_edges: int, edges: typing.List[Tag]) -> None:
        ...
    def FaceEvaluateClosestPoint(self, cae_tag: Tag, num_evaluations: int, xyz: float, xyz_cl: float, uv_cl: float, nrml: float, dist: float, in_out: int) -> None:
        ...
    def FaceEvaluateParamLocation(self, cae_tag: Tag, ad_param: float, ad_out_point: float) -> None:
        ...
    def FacepairAskMidsrfFrec(self, facepair_feature_tag: Tag, midsrf_feature_tag: Tag) -> None:
        ...
    def FemAskCadPart(self, fem_tag: Tag, is_idealized_part: bool) -> Tag:
        ...
    def FindMesh(self, object_tag: Tag, dimension: UF.UFSf.MeshDimension, num_of_meshes: int, mesh_items_p: typing.List[Tag]) -> None:
        ...
    def FindMinimumDistance(self, entity_1: Tag, entity_2: Tag, min_dist: float, point1: float, point2: float) -> None:
        ...
    def FreeDefeatureParms(self, def_parms_p: UF.UFSf.DefeatureParms) -> None:
        ...
    def FreeIdealizeParms(self, parms_p: int) -> None:
        ...
    def FreeIdealizeRegion(self, region_p: int) -> None:
        ...
    def FreeMidsrfUserParms(self, parms_p: UF.UFSf.MidsrfUserParms) -> None:
        ...
    def GetAutoElementSize(self, num_objects: int, objects_p: Tag, esize: float) -> None:
        ...
    def IdealizedPartAskMasterPart(self, idealized_part_tag: Tag) -> Tag:
        ...
    def InitMshvldErrorContainer(self, container: UF.UFSf.MeshErrorContainer) -> None:
        ...
    def IsFem(self, fem_tag: Tag) -> bool:
        ...
    def IsIdealizedPart(self, idealized_part_tag: Tag) -> bool:
        ...
    def IsMidsrf(self, sheet_body_tag: Tag, is_midsrf: bool, midsrf_type: int, feature_tag: Tag) -> None:
        ...
    def IsOffsetMidsrf(self, sheet_body_tag: Tag, is_midsrf: bool) -> None:
        ...
    def IsScenarioPart(self) -> None:
        ...
    def IsSimulation(self, simulation_tag: Tag) -> bool:
        ...
    def IsUserdefMidsrf(self, sheet_body_tag: Tag, is_midsrf: bool, feature_tag: Tag) -> None:
        ...
    def LinkMaterial(self, material_tag: Tag, object_tag: Tag) -> None:
        ...
    def LinkSection(self, section_tag: Tag, mesh_geom_tag: Tag) -> None:
        ...
    def LocateAllMeshes(self, mesh_tag: Tag, mesh_count: int, mesh_pointer: typing.List[Tag]) -> None:
        ...
    def LocateElement(self, mesh_tag: Tag, num_of_elements: int, element_tags_p: typing.List[Tag]) -> None:
        ...
    def LocateElementById(self, mesh_tag: Tag, num_of_ids: int, element_ids: int, num_of_elements: int, element_tags_p: typing.List[Tag]) -> None:
        ...
    def LocateHptMgParents(self, point_tag: Tag, parent_cnt: int, parent_list: typing.List[Tag]) -> None:
        ...
    def LocateMaterial(self, object_tag: Tag, material_tag: Tag) -> None:
        ...
    def LocateMeshMatingConditionByName(self, assembly_name: str, assembly_mesh: Tag) -> None:
        ...
    def LocateMeshMatingConditionList(self, assembly_mesh_cnt: int, assembly_mesh_tags: typing.List[Tag]) -> None:
        ...
    def LocateNamedDursolNx(self, dursol_name: str, dursol_tag: Tag) -> None:
        ...
    def LocateNamedMaterial(self, material_name: str, material_tag_ptr: Tag) -> None:
        ...
    def LocateNamedSection(self, section_name: str, section_tag_ptr: Tag) -> None:
        ...
    def LocateNamedSolutionNx(self, solution_name: str, solution_tag: Tag) -> None:
        ...
    def LocateNamedStepNx(self, solution_tag: Tag, step_name: str, step_tag: Tag) -> None:
        ...
    def LocateNodeById(self, mesh_tag: Tag, num_of_ids: int, node_ids: int, num_of_node: int, node_tags_p: typing.List[Tag]) -> None:
        ...
    def LocateNodesOnElement(self, element_tag: Tag, num_of_nodes: int, node_tags_p: typing.List[Tag]) -> None:
        ...
    def LocateNodesOnGeometry(self, geom_tag: Tag, type_sw: UF.UFSf.NodeSwitch, nodes_cnt: int, nodes_list: typing.List[Tag]) -> None:
        ...
    def LocateNodesOnMesh(self, mesh_tag: Tag, num_of_nodes: int, node_tags_p: typing.List[Tag]) -> None:
        ...
    def LocateScenarios(self, number_of_scenarios: int, scenario_names: str) -> None:
        ...
    def LocateSection(self, mesh_object: Tag, section_tag: Tag) -> None:
        ...
    def LocateSolutionBoundaryConditionsNx(self, solution: Tag, num_members: int, membs_pp: typing.List[Tag]) -> None:
        ...
    def LocateSolutionLoadsNx(self, solution: Tag, num_members: int, membs_pp: typing.List[Tag]) -> None:
        ...
    def LocateStepBoundaryConditionsNx(self, step: Tag, num_members: int, membs_pp: typing.List[Tag]) -> None:
        ...
    def LocateStepLoadsNx(self, step: Tag, num_members: int, membs_pp: typing.List[Tag]) -> None:
        ...
    def MapObjectToCurrentPart(self, object_tag: Tag) -> Tag:
        ...
    def Mc2dAngle(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, results_format: UF.UFSf.McResultFormat, min_threshold: float, max_threshold: float, min_angle: float, max_angle: float, min_status_ptr: UF.SfmcResult, max_status_ptr: UF.SfmcResult) -> None:
        ...
    def McAspectRatio(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, result_format: UF.UFSf.McResultFormat, threshold: float, aspect_ratio: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def McElementCheck(self, mesh_tag: Tag, failed_elm_count: int) -> None:
        ...
    def McJacobianRatio(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, results_format: UF.UFSf.McResultFormat, threshold: float, jacobian_ratio: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def McJacobianZero(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, results_format: UF.UFSf.McResultFormat, threshold: float, jacobian_zero: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def McSkew(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, result_format: UF.UFSf.McResultFormat, threshold: float, skew: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def McTaper(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, result_format: UF.UFSf.McResultFormat, threshold: float, taper: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def McTetCollapse(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, result_format: UF.UFSf.McResultFormat, threshold: float, tet_collapse: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def McTetraAngle(self, abspos: float, node_count: int, results_format: UF.UFSf.McResultFormat, min_threshold: float, max_threshold: float, min_angle: float, max_angle: float, min_status_ptr: UF.SfmcResult, max_status_ptr: UF.SfmcResult) -> None:
        ...
    def McTwist(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, result_format: UF.UFSf.McResultFormat, threshold: float, twist: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def McWarp(self, element_type: UF.UFSf.ElementType, abspos: float, node_count: int, result_format: UF.UFSf.McResultFormat, threshold: float, warp: float, status_ptr: UF.SfmcResult) -> None:
        ...
    def ModlBodyAskBody(self, modl_body: Tag, cae_body_p: Tag) -> None:
        ...
    def OpenScenario(self, scenario_name: str, master_part_tag: Tag) -> None:
        ...
    def PartitionBody(self, num_solid_bodies: int, solid_body_tags: typing.List[Tag], tool_body: Tag, num_partitioned_bodies: int, partitioned_bodies: typing.List[Tag]) -> None:
        ...
    def PartitionBodyNx5(self, associate: int, num_solid_bodies: int, solid_body_tags: typing.List[Tag], tool_body: Tag, num_partitioned_bodies: int, partitioned_bodies: typing.List[Tag]) -> None:
        ...
    def PolygonBodyAskType(self, polygon_body: Tag, body_type: int) -> None:
        ...
    def PropertyAskNameNx(self, property_tag: Tag, property_name_pp: str) -> None:
        ...
    def PropertyAskTypeNx(self, property_tag: Tag, property_type: UF.UFSf.FemValueType) -> None:
        ...
    def PropertyAskValueNx(self, property_tag: Tag, bool_value: bool, int_value: int, scalar_value: float, text_value: str, num_lines: int, multi_text_value: str) -> None:
        ...
    def PropertySetValueNx(self, property_tag: Tag, bool_value: bool, int_value: int, scalar_value: float, text_value: str, num_lines: int, multi_text_value: str) -> None:
        ...
    def RemoveFromSolutionNx(self, num_of_lbc: int, lbc: Tag) -> None:
        ...
    def RemoveFromStepNx(self, num_of_lbc: int, lbc: Tag) -> None:
        ...
    def RenameScenario(self, master_tag: Tag, old_scenario: str, new_scenario: str) -> None:
        ...
    def ResetElementIds(self, start_id: int) -> None:
        ...
    def ResetNodeIds(self, start_id: int) -> None:
        ...
    def RetrieveLibraryMaterial(self, libref: str, material_tag: Tag) -> None:
        ...
    def SaveScenario(self) -> None:
        ...
    def SetActiveSolutionAndStepNx(self, active_solution: Tag, active_step: Tag) -> None:
        ...
    def SetEdgeDensity(self, object_tag: Tag, edge_density_data: UF.UFSf.EdgeDensityData) -> None:
        ...
    def SetIdealizeParmExp(self, parms_p: int, parm_exp_t: UF.UFSf.IdealizeParmExp, exp_tag: Tag) -> None:
        ...
    def SetIdealizeParmFaces(self, parms_p: int, parm_face_t: UF.UFSf.IdealizeParmFace, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def SetMeshVisuals(self, mesh_tag: Tag, mesh_vis: UF.UFSf.MeshVisuals) -> None:
        ...
    def SetShellThickness(self, shell_thick_exp: str, num_items: int, items_array: typing.List[Tag]) -> None:
        ...
    def SimulationAskFem(self, simulation_tag: Tag) -> Tag:
        ...
    def SolutionAskDescriptorNx(self, solution: Tag, descriptor: Tag) -> None:
        ...
    def SolutionAskLanguageNx(self, solution: Tag, language: Tag) -> None:
        ...
    def SolutionAskNameNx(self, solution: Tag, solution_name: str) -> None:
        ...
    def SolutionAskNthStepNx(self, solution_tag: Tag, step: int, step_tag: Tag) -> None:
        ...
    def SolutionAskNumStepsNx(self, solution_tag: Tag, step_count: int) -> None:
        ...
    def SolutionAskPropertyByIndexNx(self, solution: Tag, property: int, property_tag: Tag) -> None:
        ...
    def SolutionAskPropertyCountNx(self, solution: Tag, num_props: int) -> None:
        ...
    def SolutionAskPropertyNx(self, solution: Tag, property_name: str, property_tag: Tag) -> None:
        ...
    def SolutionAskSolverPropertyByIndexNx(self, solution: Tag, property: int, property_tag: Tag) -> None:
        ...
    def SolutionAskSolverPropertyCountNx(self, solution: Tag, num_props: int) -> None:
        ...
    def SolutionAskSolverPropertyNx(self, solution: Tag, property_name: str, property_tag: Tag) -> None:
        ...
    def SolutionSetNameNx(self, solution: Tag, solution_name: str, rename_result_file: bool) -> None:
        ...
    def SolveActiveSolutionNx(self, format_choice: int) -> None:
        ...
    def StepAskNameNx(self, step: Tag, step_name: str) -> None:
        ...
    def StepAskPropertyByIndexNx(self, step: Tag, property: int, property_tag: Tag) -> None:
        ...
    def StepAskPropertyCountNx(self, step: Tag, num_props: int) -> None:
        ...
    def StepAskPropertyNx(self, step: Tag, property_name: str, property_tag: Tag) -> None:
        ...
    def StepSetNameNx(self, solution: Tag, step: Tag, step_name: str) -> None:
        ...
    def SwitchScenarios(self, scenario_1_name: str, scenario_2_name: str) -> None:
        ...
    def TempDispResults(self, color_att_p: UF.SfColorAttr, legend_attr_p: UF.SfLegendAttr) -> None:
        ...
    def TempDisplayElement(self, node_tag: Tag, color: int, height: float, display_edges: bool, display_id: bool, display_nodes: bool, node_marker: UF.UFDisp.PolyMarker, display_orientation: bool) -> None:
        ...
    def TempDisplayNode(self, node_tag: Tag, color: int, height: float, display_id: bool, object_symbol: str, node_marker: UF.UFDisp.PolyMarker) -> None:
        ...
    def TestGpe(self) -> None:
        ...
    def UnlinkMaterial(self, object_tag: Tag) -> None:
        ...
    def UnlinkSection(self, section_tag: Tag, mesh_geom_tag: Tag) -> None:
        ...
    def UpdateScenario(self) -> None:
        ...
    def WriteReport(self) -> None:
        ...


    class UFSfUgsTetMeshParms():
        element_type: UF.UFSf.ElementType
        midnodes: int
        element_size: float
        midnode_option: UF.UFSf.UgsMesherMidnodeOption
        geometry_tolerance_toggle: int
        geometry_tolerance_value: float
        maximum_midnode_jacobian: float
        minimum_face_angle: float
        surf_mesh_size_variation: int
        tet_mesh_size_variation: int
        multi_block_decomposition: int
        mesh_transition: int
        remesh_toggle: int
        create_pyramids: int
        small_feature: float
        attempt_mapped_meshing: int
        two_element_through_thickness_toggle: int
        auto_fix_failed_elements_toggle: int
        edge_merge_toggle: int
        edge_angle: float
        fillet_toggle: int
        fillet_type: UF.UFSf.UgsTetMeshFilletTypeOption
        fillet_num_elem: int
        fillet_min_rad: float
        fillet_max_rad: float
    

    class UgsTetMeshFilletTypeOption(enum.Enum):
        UgsTetMeshFilletAll = 0
        UgsTetMeshFilletInside = 1
        UgsTetMeshFilletOutside = 2
    

    class UgsMesherMidnodeOption(enum.Enum):
        UgsMesherStraightMidnodes = 2
        UgsMesherCurvedMidnodes = 1
        UgsMesherMixedMidnodes = 0
    

    class UFSfUgsMeshAbstractionParams():
        small_feature: float
        edge_merge_toggle: int
        edge_angle: float
        fillet_toggle: int
        fillet_type: UF.UFSf.UgsAbstractionFilletTypeOption
        fillet_num_elem: int
        fillet_min_rad: float
        fillet_max_rad: float
    

    class UgsAbstractionFilletTypeOption(enum.Enum):
        UgsAbstractionFilletAll = 0
        UgsAbstractionFilletInside = 1
        UgsAbstractionFilletOutside = 2
    

    class UFSfUgs2dMeshParms():
        element_type: UF.UFSf.Ugs2dMesherElemType
        element_size: float
        edge_match_toggle: int
        edge_match_tolerance: float
        suppress_hole_toggle: int
        suppress_hole_diameter_value: float
        suppress_hole_point_type: int
        target_minimum_element_edge_length: int
        format_mesh: int
        attempt_quad_mapping: int
        quad_only_option: int
        split_poor_quads: int
        maximum_quad_warp: float
        midnode_option: UF.UFSf.UgsMesherMidnodeOption
        geometry_tolerance_toggle: int
        geometry_tolerance_value: float
        maximum_midnode_jacobian: float
        minimum_face_angle: float
        surf_mesh_size_variation: int
        small_feature: float
        edge_merge_toggle: int
        edge_angle: float
        mesh_transition: int
        multi_block_decomposition: int
        mesh_individual_faces: int
        CAD_curvature_abstraction: int
        minimum_feature_length: float
        mesh_method: int
        fillet_toggle: int
        fillet_type: UF.UFSf.UgsAbstractionFilletTypeOption
        fillet_num_elem: int
        fillet_min_rad: float
        fillet_max_rad: float
        max_included_angle_quad_toggle: int
        min_included_angle_quad_toggle: int
        max_included_angle_tria_toggle: int
        min_included_angle_tria_toggle: int
        max_included_angle_quad_value: float
        min_included_angle_quad_value: float
        max_included_angle_tria_value: float
        min_included_angle_tria_value: float
        move_nodes_off_geometry: int
        max_warp_toggle: int
    

    class Ugs2dMesherElemType(enum.Enum):
        UgsMesherTri3 = 0
        UgsMesherTri6 = 1
        UgsMesherQuad4 = 2
        UgsMesherQuad8 = 3
    

    class ScenarioInfo(enum.Enum):
        MeshInfo = 0
        LoadInfo = 1
        SolutionInfo = 2
        StepInfo = 3
        BoundaryConditionInfo = 4
        MaterialInfo = 5
        SectionInfo = 6
        MeshMatingConditionInfo = 7
        FeaSummaryInfo = 8
        DurEventInfo = 9
        LoadCaseInfo = 10
        SimSummaryInfo = 11
    

    class UFSfResultingFacePairs():
        face1: Tag
        face2: Tag
        relative_status: UF.UFSf.FaceSubdivStatus
    

    class UFSfOrientationData():
        face_tag: Tag
        origin: float
        x_dir: float
        y_dir: float
    

    class NodeSwitch(enum.Enum):
        SwitchOnBoundary = 0
        SwitchInInterior = 1
        SwitchAll = 2
    

    class NodeBtype(enum.Enum):
        NodeBodyinterior = 0
        NodeEdge = 1
        NodeFaceinterior = 2
        NodeInterior = 3
        NodeNoGeometry = 4
        NodePoint = 5
    

    class NeutralMaterialTypes(enum.Enum):
        MaterialIsotropic = 0
        MaterialOrthotropic = 1
        MaterialAnisotropic = 2
        MaterialFormability = 3
        MaterialFluid = 4
        MaterialHyperelastic = 5
        MaterialMooneyrivlin = 6
        MaterialMooneyrivlintestdata = 7
        MaterialPolynomial = 8
        MaterialReducedpolynomial = 9
        MaterialOgden = 10
        MaterialOgdentestdata = 11
        MaterialFoam = 12
        MaterialFoamtestdata = 13
        MaterialBlatz = 14
        MaterialArrudaboyce = 15
        MaterialArrudaboycetestdata = 16
        MaterialNeohooke = 17
        MaterialNeohooketestdata = 18
        MaterialMarlow = 19
        MaterialVanderwaals = 20
        MaterialYeoh = 21
        MaterialYeohtestdata = 22
        MaterialGent = 23
        MaterialGasket = 24
        MaterialGasketbehavior = 25
        MaterialShapememoryalloy = 26
        MaterialSussmanbathe = 27
        MaterialGasketdisplacement = 28
        MaterialDamageinterface = 29
        MaterialMultiplefluid = 30
        MaterialHartsmith = 31
        MaterialAlexander = 32
        MaterialCuring = 33
        MaterialPorous = 35
    

    class UFSfMidsrfUserParms():
        solid_body: Tag
        num_sheet_bodies: int
        sheet_bodies_a: typing.List[Tag]
        thickness: float
        const_thickness: float
    

    class MidNodeType(enum.Enum):
        NodeCorner = 0
        NodeDisabled = 1
        NodeMid = 2
        NodeOrientation = 3
    

    class UFSfMeshVisuals():
        color: int
        shade_mode: int
        shade_edge_color: int
        shrink_factor: int
        normals: int
        normals_color: int
        edge_visibility_sw: int
        text_display_sw: int
        thick_shell_sw: int
        show_analysis: int
        show_deformed: int
        deformed_scale: float
    

    class MeshGeomUsage(enum.Enum):
        GeomAny = 0
        GeomHard = 1
        GeomConnectA = 2
        GeomConnectB = 3
    

    class MeshGeomMeshdir(enum.Enum):
        MgMeshdirUninitialized = 0
        MgMeshdirUndefined = 1
        MgMeshdirFromStart = 2
        MgMeshdirFromEnd = 3
        MgMeshdirReverse = 4
        MgMeshdirDontReverse = 5
    

    class MeshGeometryTypes(enum.Enum):
        GeomOther = 0
        GeomAssem = 1
        GeomCompon = 2
        GeomOcc = 3
        GeomBody = 4
        GeomFace = 5
        GeomEdge = 6
        GeomSurf = 7
        GeomCurve = 8
        GeomPoint = 9
        GeomVertex = 10
        GeomCompositeBody = 11
        GeomCompositeFace = 12
        GeomCompositeEdge = 13
    

    class MeshErrorType(enum.Enum):
        MshvldNotClassified = 0
        MshvldMeshNotAssociatedToMr = 1
        MshvldMeshWithNoElem = 2
        MshvldMeshWithDiffDimElem = 3
        MshvldInvalidElemOwner = 4
        MshvldInvalidElemNodeNum = 5
        MshvldOrphanNode = 6
        MshvldInvalidNodeOwner = 7
        MshvldInvalidCornerMidNodeOrder = 8
        MshvldNodeNotAssociatedToMg = 9
        MshvldCornerMidNodeOverlap = 10
        MshvldMidNodeNotProperlySet = 11
        MshvldInvalidNodeBtype = 12
        MshvldNodeAssociatedToChildFace = 13
        MshvldNodeAssociatedToInteriorEdge = 14
        MshvldNodeSharedByMultipleCollectors = 15
        MshvldDuplicateNodeLabel = 16
        MshvldMrWithNoMg = 17
        MshvldInvalid1dConnectElem = 18
        MshvldInvalid1dWeldElem = 19
        MshvldInvalid1dContactElem = 20
        MshvldInvalidEdgeLimit = 21
        MshvldHardPntNotHonored = 22
        MshvldInvalidMatchEdgeMesh = 23
        MshvldInvalidGlueMateEdgeMesh = 24
        MshvldInvalidFreeMateEdgeMesh = 25
        MshvldInvalidGlueMateFaceMesh = 26
        MshvldInvalidFreeMateFaceMesh = 27
        MshvldInvalidMatchMateEdgeMesh = 28
        MshvldInvalidEdgeMateForMmc = 29
        MshvldInvalidEndNodeAssociativity = 30
        MshvldNodeAssociatedToTinyEdge = 31
        MshvldEdgeDensityNotHonored = 32
        MshvldFaceDensityNotHonored = 33
        MshvldEdgeDensityNotHonoredForMatchMatePnrs = 34
        MshvldFaceDensityNotHonoredForMatePnrs = 35
        MshvldEdgeFaceDensityNotHonored = 36
        MshvldMeshWithPendingUpdate = 37
    

    class UFSfMeshErrorList():
        num_mesh_errors: int
        mesh_errors: typing.List[UF.UFSf.MeshError]
    

    class UFSfMeshErrorContainer():
        node_asso_error_list: UF.UFSf.MeshErrorList
        elem_asso_error_list: UF.UFSf.MeshErrorList
        mesh_asso_error_list: UF.UFSf.MeshErrorList
        mesh_recipe_error_list: UF.UFSf.MeshErrorList
        geom_constraint_error_list: UF.UFSf.MeshErrorList
        user_attribute_error_list: UF.UFSf.MeshErrorList
    

    class UFSfMeshError():
        err_object: Tag
        err_type: UF.UFSf.MeshErrorType
    

    class MeshDimension(enum.Enum):
        Dimension0d = 0
        Dimension1d = 1
        Dimension2d = 2
        Dimension3d = 3
        DimensionAny = 4
    

    class McResultFormat(enum.Enum):
        McDoNotNormalizeResult = 0
        McNormalizeResult = 1
    

    class LvFunctionMode(enum.Enum):
        HalfUnitCycle = 0
        FullUnitCycle = 1
    

    class LibraryMaterial(enum.Enum):
        MatlIsReadOnly = 0
        MatlIsEditable = 1
    

    class IdealizeParmFace(enum.Enum):
        IdealizeRetainedFaces = 0
        IdealizeRemovedFaces = 1
    

    class IdealizeParmExp(enum.Enum):
        IdealizeHoleDiameter = 0
        IdealizeBlendRadius = 1
        IdealizeTinyFaceArea = 2
        IdealizeThinFaceWidth = 3
        IdealizeFaceCollector = 4
        IdealizeScreenSelectedFace = 5
    

    class UFSfGeomOptions():
        fSyncPoints: bool
        fSyncCsys: bool
        fSyncLines: bool
        fSyncArcs: bool
        fSyncSplines: bool
        fSyncSketchCurves: bool
        fSyncConics: bool
    

    class FemValueType(enum.Enum):
        FemValueNil = 0
        FemValueInt = 1
        FemValueScalar = 2
        FemValueText = 3
        FemValueEnum = 4
        FemValueCoord = 5
        FemValueMaterial = 6
        FemValueSection = 7
        FemValueVector = 8
        FemValueTable = 9
        FemValueLoad = 10
        FemValueBndcond = 11
        FemValueBool = 12
        FemValueMultiString = 13
        FemValueMultiStringIti = 23
        FemValueFilenameValType = 14
        FemValueDirpathValType = 15
        FemValueSsmoValType = 16
        FemValuePptValType = 29
        FemValuePlymatValType = 32
        FemValueFieldValType = 17
        FemValueAxisValType = 18
        FemValueDofValType = 19
        FemValuePointValType = 20
        FemValueEdgesOnFace = 25
        FemValueScalarArray = 27
        FemValueAction = 28
        FemValueSsmoArray = 30
        FemValueTime = 31
        FemValueIntArray = 33
        FemValueExtMenu = 34
        FemValueCatalog = 35
        FemValueGeneralField = 36
        FemValueScalarField = 37
        FemValueVectorField = 38
        FemValueComplexScalarField = 54
        FemValueMatrix = 39
        FemValueRegion = 40
        FemValueGroupref = 41
        FemValueSelectref = 42
        FemValueSectionOrient = 43
        FemValueSectionOffset = 44
        FemValueTargetset = 45
        FemValueSectionRef = 46
        FemValueDofsetRef = 47
        FemValueLbcref = 49
        FemValuePptArray = 50
        FemValueSolutionref = 51
        FemValueGrouprefArray = 52
        FemValueScalarFieldTable = 53
        FemValueSolutionstepref = 55
        FemValuePointArrayValType = 56
        FemValueComponentref = 57
        FemValueComponentrefArray = 58
        FemValueSolverDrivenStringArray = 59
        FemValueImageValType = 60
        FemValueComplexVectorField = 61
        FemValueLbcrefArray = 62
    

    class FaceSubdivStatus(enum.Enum):
        IdenticalFacesEqEdges = 0
        IdenticalFacesUneqEdges = 1
        NotIdentical = 2
        OverlappingFaces = 3
        SeparateFaces = 4
    

    class ElmDimensionType(enum.Enum):
        ElementPoint = 0
        ElementBeam = 1
        ElementShell = 2
        ElementSolid = 3
        ElementAll = 4
    

    class ElmAdaptivityType(enum.Enum):
        ElementAdaptHelms = 0
        ElementAdaptPelms = 1
    

    class ElementType(enum.Enum):
        Undefined = 0
        Cmass = 1
        Bar = 2
        Beam = 3
        Rod = 4
        Rbe2 = 5
        Spring = 6
        Mass = 7
        Hbdy = 8
        Quad4 = 9
        Tria3 = 10
        Quad8 = 11
        Tria6 = 12
        Tet4 = 13
        Tet10 = 14
        _1D_CONTACT = 15
        Hex8 = 16
        Hex20 = 17
        Wdg6 = 18
        Wdg15 = 19
        _2D_CONTACT = 20
        Weld = 21
        EfConn = 22
        MmFree = 23
        MmGlue = 24
        Rbe3 = 25
        Pyr5 = 26
        Pyr9 = 27
        Pyr13 = 28
        _1D_NG = 29
        _1D_PLOTEL = 30
        _1D_MASS = 31
        PyrMixedOrder = 32
        TetMixedOrder = 33
        _1D_BEARING = 34
        Hexcohes8 = 35
        Hexcohes20 = 36
        Wdgcohes6 = 37
        Wdgcohes15 = 38
        Mpc = 39
        TotalCount = 40
    

    class UFSfEfConnInfo():
        element_des_tag: Tag
        density_type: UF.UFSf._1D_density_type_
        edge_density: float
        mesh_option: int
        num_edges: int
        edge_tags: typing.List[Tag]
        num_faces: int
        face_tags: typing.List[Tag]
    

    class EdgeDensityType(enum.Enum):
        EdgeDensitySize = 0
        EdgeDensityNumber = 1
        EdgeDensitySmart = 4
        NotEdgeDensityDefined = 5
    

    class UFSfEdgeDensityData():
        type: UF.UFSf.EdgeDensityType
        size: float
        number: int
    

    class DursolStressType(enum.Enum):
        VonMises = 0
        Tresca = 1
        MaximumPrinciple = 2
        MinimumPrinciple = 3
    

    class DursolStressCriterion(enum.Enum):
        UltimateStrength = 0
        YieldStrength = 1
    

    class DursolFatigueLifeCriterion(enum.Enum):
        SmithWatsonTopper = 0
        StrainLifeMaxPrinciple = 1
        StrainLifeMaxShear = 2
        StressLife = 3
    

    class DursolDesignLifeCriterion(enum.Enum):
        InfiniteLife = 0
        CyclesToFailure = 1
    

    class UFSfDefeatureParms():
        num_ret_faces: int
        retained_faces: typing.List[Tag]
        num_rem_faces: int
        removed_faces: typing.List[Tag]
        region_parms_p: int
    

    class UFSfContactMeshData():
        element_name: str
        element_descritor_tag: Tag
        align_target_edge_node: int
        target_edge_node_align_method: int
        number_of_elms: int
        gap_tol_option: int
        gap_tolerance: float
        contact_edge: Tag
        contact_edge_mesh_dir: UF.UFSf.MeshGeomMeshdir
        contact_edge_start_limit: float
        contact_edge_end_limit: float
        target_edge: Tag
        target_edge_mesh_dir: UF.UFSf.MeshGeomMeshdir
        target_edge_start_limit: float
        target_edge_end_limit: float
    

    class AssemblyType(enum.Enum):
        NotSupportAssemType = 0
        AssemByGlue = 1
        AssemBySlideContact = 2
        AssemByGapContact = 3
        AssemFree = 4
    

    class UFSf_1d_mesh_data_():
        element_type: UF.UFSf._1D_element_type_
        density_type: UF.UFSf._1D_density_type_
        edge_density: float
        merge_node_option: int
        node_unique_tol: float
    

    class _1D_element_type_(enum.Enum):
        _1D_SPRING_TYPE = 6
        _1D_BAR_TYPE = 2
        _1D_BEAM_TYPE = 3
        _1D_ROD_TYPE = 4
        _1D_RIGID_TYPE = 5
    

    class _1D_density_type_(enum.Enum):
        _1D_EDGE_DENSITY_SIZE = 0
        _1D_EDGE_DENSITY_NUMBER = 1
        _1D_EDGE_DENSITY_SMART = 4
    

    class _0D_element_type_(enum.Enum):
        _0D_CONMASS = 1
    

    class _0D_density_type_(enum.Enum):
        _0D_EDGE_DENSITY_SIZE = 0
        _0D_EDGE_DENSITY_NUMBER = 1
        _0D_EDGE_DENSITY_SMART = 4
    

class UFSetup(Utilities.NXRemotableObject):
    def AskGeomNull(self, setup_tag: Tag, geom_null: Tag) -> None:
        ...
    def AskGeomRoot(self, setup_tag: Tag, geom_group: Tag) -> None:
        ...
    def AskMctNull(self, setup_tag: Tag, mct_null: Tag) -> None:
        ...
    def AskMctRoot(self, setup_tag: Tag, mct_group: Tag) -> None:
        ...
    def AskMthdNull(self, setup_tag: Tag, mthd_null: Tag) -> None:
        ...
    def AskMthdRoot(self, setup_tag: Tag, mthd_group: Tag) -> None:
        ...
    def AskProgramNull(self, setup_tag: Tag, program_null: Tag) -> None:
        ...
    def AskProgramRoot(self, setup_tag: Tag, program_group: Tag) -> None:
        ...
    def AskSetup(self, setup_tag: Tag) -> None:
        ...
    def Create(self, part_tag: Tag, template_name: str) -> None:
        ...
    def DeleteSetup(self) -> None:
        ...
    def GenerateClsf(self, setup: Tag, group: Tag, clsf_name: str, output_filename: str, output_units: UF.UFSetup.OutputUnits) -> None:
        ...
    def GenerateProgram(self, setup: Tag, group: Tag, post_name: str, output_filename: str, output_units: UF.UFSetup.OutputUnits) -> None:
        ...


    class OutputUnits(enum.Enum):
        OutputUnitsInch = 0
        OutputUnitsMetric = 1
        OutputUnitsOutputDefined = 2
        OutputUnitsLast = 3
    

class UFSession(Utilities.BaseSession):
    def GetUFSession() -> UFSession:
        ...
    Udobj: UFUdobj
    UF: UF
    Cfi: UFCfi
    Drf: UFDrf
    Attr: UFAttr
    Modl: UFModl
    Disp: UFDisp
    Help: UFHelp
    Ugmgr: UFUgmgr
    Sf: UFSf
    Obj: UFObj
    Smd: UFSmd
    Msao: UFMsao
    Std: UFStd
    Draw: UFDraw
    Plist: UFPlist
    Part: UFPart
    Pd: UFPd
    Curve: UFCurve
    Clear: UFClear
    def Tag() -> Tag: ...

    Assem: UFAssem
    Route: UFRoute
    Misc: UFMisc
    Abort: UFAbort
    Bound: UFBound
    CurveLineArc: UFCurveLineArc
    Forgeo: UFForgeo
    Brep: UFBrep
    Cam: UFCam
    Ude: UFUde
    Param: UFParam
    CamPref: UFCamPref
    CamPrepro: UFCamPrepro
    Cambnd: UFCambnd
    CambndWedm: UFCambndWedm
    Camgeom: UFCamgeom
    Camtext: UFCamtext
    Cgm: UFCgm
    Clone: UFClone
    Clsf: UFClsf
    Csys: UFCsys
    CutLevels: UFCutLevels
    Cutter: UFCutter
    DbcMld: UFDbcMld
    Die: UFDie
    Dieeng: UFDieeng
    Dirpath: UFDirpath
    Path: UFPath
    Oper: UFOper
    Drpos: UFDrpos
    Dpud: UFDpud
    Eval: UFEval
    Evalsf: UFEvalsf
    Facet: UFFacet
    Fam: UFFam
    FbmGeom: UFFbmGeom
    Fltr: UFFltr
    Gdt: UFGdt
    Gexp: UFGexp
    Group: UFGroup
    Hmop: UFHmop
    Kf: UFKf
    KfUgmgr: UFKfUgmgr
    UgmgrKf: UFUgmgrKf
    Layer: UFLayer
    Lib: UFLib
    Mct: UFMct
    Ui: UFUi
    Styler: UFStyler
    Mb: UFMb
    Mfm: UFMfm
    ModlSweep: UFModlSweep
    ModlTrex: UFModlTrex
    Mom: UFMom
    Motion: UFMotion
    Mtx2: UFMtx2
    Mtx3: UFMtx3
    Mtx4: UFMtx4
    Ncgroup: UFNcgroup
    Ncprog: UFNcprog
    Ncgeom: UFNcgeom
    Ncmthd: UFNcmthd
    Nx2d: UFNx2d
    Oprbnd: UFOprbnd
    Patt: UFPatt
    Plot: UFPlot
    So: UFSo
    Point: UFPoint
    ProcessAid: UFProcessAid
    Ps: UFPs
    RouteRun: UFRouteRun
    Rule: UFRule
    Scop: UFScop
    Setup: UFSetup
    Shopdoc: UFShopdoc
    SfLegend: UFSfLegend
    Sfl: UFSfl
    SfCurve: UFSfCurve
    Mech: UFMech
    SfPost: UFSfPost
    Sim: UFSim
    Sket: UFSket
    Studio: UFStudio
    Subdiv: UFSubdiv
    SurfReg: UFSurfReg
    Tabnot: UFTabnot
    TabnotF: UFTabnotF
    Text: UFText
    Trns: UFTrns
    Turn: UFTurn
    Udop: UFUdop
    Ugfont: UFUgfont
    UiOnt: UFUiOnt
    UiParam: UFUiParam
    Undo: UFUndo
    Unit: UFUnit
    Vec2: UFVec2
    Vec3: UFVec3
    Vec4: UFVec4
    View: UFView
    Wave: UFWave
    Web: UFWeb
    Weight: UFWeight
    Weld: UFWeld
    Xs: UFXs


class UFScop(Utilities.NXRemotableObject):
    def AskRowColumnCount(self, object_tag: Tag, num_row: int, num_col: int) -> None:
        ...
    def AskTxIntpDataType(self, object_tag: Tag, tx_intp_data_type: UF.UFScop.TxIntpDataType) -> None:
        ...
    def AskTxIntpMethod(self, object_tag: Tag, tx_intp_method: UF.UFScop.TxIntpMethod) -> None:
        ...
    def AskTxIntpVectorData(self, object_tag: Tag, count: int, vector_data: typing.List[UF.UFScop.VectorData]) -> None:
        ...
    def DisplayUvDirs(self, object_tag: Tag) -> None:
        ...
    def EvalGrid(self, object_tag: Tag, uv: float, entity: Tag, srf_value: UF.ModlSrfValue) -> None:
        ...
    def GetNextDrivePoint(self, object_tag: Tag, drpos: int, point_count: int) -> None:
        ...
    def RewindDrivePoint(self, object_tag: Tag) -> None:
        ...
    def SetTxIntpDataType(self, object_tag: Tag, tx_intp_data_type: UF.UFScop.TxIntpDataType) -> None:
        ...
    def SetTxIntpMethod(self, object_tag: Tag, tx_intp_method: UF.UFScop.TxIntpMethod) -> None:
        ...
    def SetTxIntpVectorData(self, object_tag: Tag, count: int, vector_data: UF.UFScop.VectorData, all_on_surface: bool) -> None:
        ...


    class UFScopVectorData():
        xyz: float
        ijk: float
        lead_tilt: float
        is_corner_vector: bool
    

    class TxIntpMethod(enum.Enum):
        TxIntpLinearMethod = 0
        TxIntpCubicSplineMethod = 1
        TxIntpSmoothMethod = 2
    

    class TxIntpDataType(enum.Enum):
        TxIntpDatypeVector = 0
        TxIntpDatypeAnglePs = 1
        TxIntpDatypeAngleDs = 2
    



    

class UFRouteRun(Utilities.NXRemotableObject):
    def AskFromItems(self, run: Tag, n_from_items: int, from_items: typing.List[Tag]) -> None:
        ...
    def AskMemberItems(self, run: Tag, n_member_items: int, member_items: typing.List[Tag]) -> None:
        ...
    def AskRunIdAndType(self, run: Tag, run_id: str, run_type: str) -> None:
        ...
    def AskRunsInPart(self, part: Tag, n_runs: int, runs: typing.List[Tag]) -> None:
        ...
    def AskToItems(self, run: Tag, n_to_items: int, to_items: typing.List[Tag]) -> None:
        ...
    def EditRun(self, run: Tag, run_id: str, run_type: str, n_from_items: int, from_items: typing.List[Tag], n_to_items: int, to_items: typing.List[Tag], n_member_items: int, member_items: typing.List[Tag]) -> None:
        ...
    def SetRunId(self, run: Tag, run_id: str) -> None:
        ...
    def SetRunType(self, run: Tag, run_type: str) -> None:
        ...


class UFRoute(Utilities.NXRemotableObject):
    def AddSegmentToStock(self, stock: Tag, segment: Tag) -> None:
        ...
    def AddTerminalPorts(self, multi: Tag, num_terms: int, terms: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AddVirtualPorts(self, multi: Tag, num_terms: int, terms: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AlignStock(self, stock: Tag, rotate_vec: float) -> None:
        ...
    def ArePortsConnectable(self, port1: Tag, port2: Tag) -> bool:
        """[Obsolete("Deprecated")"""
        ...
    def AreSegmentsTangent(self, segment1: Tag, segment: Tag, rcp: Tag) -> bool:
        ...
    def AskAnchorPosition(self, anchor_tag: Tag, position: float) -> None:
        ...
    def AskAnchorStock(self, anchor_tag: Tag, num_stocks: int, stocks: typing.List[Tag]) -> None:
        ...
    def AskAnchorStockData(self, anchor_tag: Tag, num_stock_data: int, stock_datas: typing.List[Tag]) -> None:
        ...
    def AskAppViewCorners(self, app_view: int, curves: int) -> None:
        ...
    def AskAppViewCurves(self, app_view: int, curves: int) -> None:
        ...
    def AskAppViewDefStock(self, app_view: int, stock: str, anchor: str) -> None:
        ...
    def AskAppViewDefStyle(self, app_view: int, style: int) -> None:
        ...
    def AskAppViewDesc(self, app_view: int, description: str) -> None:
        ...
    def AskAppViewExtPlib(self, app_view: int, library: str, entry: str) -> None:
        ...
    def AskAppViewFabCharx(self, app_view: int, num_charx: int, entry: typing.List[UF.UFRoute.CharDesc]) -> None:
        ...
    def AskAppViewFilename(self, app_view: int, filename: str) -> None:
        ...
    def AskAppViewName(self, app_view: int, name: str) -> None:
        ...
    def AskAppViewOptCharx(self, app_view: int, num_charx: int, charx: typing.List[UF.UFRoute.CharDesc]) -> None:
        ...
    def AskAppViewPlibType(self, app_view: int, type: int) -> None:
        ...
    def AskAppViewReqCharx(self, app_view: int, num_charx: int, charx: typing.List[UF.UFRoute.CharDesc]) -> None:
        ...
    def AskBendRadius(self, bend_tag: Tag, radius: float) -> None:
        ...
    def AskBendRcp(self, bend_tag: Tag, rcp: Tag) -> None:
        ...
    def AskBendSegment(self, bend_obj: Tag, seg_id: Tag) -> None:
        ...
    def AskBuiltInPathObjs(self, bip: Tag, num_objs: int, objects: typing.List[Tag]) -> None:
        ...
    def AskBuiltInPaths(self, part: Tag, num_paths: int, paths: typing.List[Tag], bip_names: str) -> None:
        ...
    def AskCharxEnv(self, num_charx: int, charx: typing.List[UF.EplibCharx]) -> None:
        ...
    def AskConnectionPorts(self, conn_tag: Tag, ports: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskCrossCurves(self, cross_tag: Tag, num_curves: int, curves: typing.List[Tag]) -> None:
        ...
    def AskCrossOffsets(self, cross_tag: Tag, offsets: float) -> None:
        ...
    def AskCrossStockData(self, cross_tag: Tag, num_stock_data: int, stock_data_tags: typing.List[Tag]) -> None:
        ...
    def AskCrossStyle(self, cross_tag: Tag, style: int) -> None:
        ...
    def AskCurrentAppView(self) -> int:
        ...
    def AskHarnessComps(self, harness: Tag, num_comps: int, comps: typing.List[Tag]) -> None:
        ...
    def AskHarnessWires(self, harness: Tag, num_wires: int, wires: typing.List[Tag]) -> None:
        ...
    def AskLengthTolerance(self, tol: float) -> None:
        ...
    def AskLoadedBendTables(self, num_tables: int, tables: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskMultiportStrings(self, port_tag: Tag, num_strings: int, strings: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskMultiportTags(self, port_tag: Tag, num_tags: int, tags: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskMultiportTerminals(self, multi: Tag, num_terms: int, terms: typing.List[Tag], num_virts: int, virts: str) -> None:
        ...
    def AskMultiportTermname(self, port_tag: Tag, name: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskObjBendRadius(self, obj_id: Tag, radius: float) -> bool:
        ...
    def AskObjCornerInfo(self, obj_id: Tag, crn_typ: int, crn_rcp: Tag, crn_obj: Tag) -> bool:
        ...
    def AskObjectPort(self, _object: Tag, num_ports: int, ports: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskObjectStock(self, obj_id: Tag, stock: Tag) -> None:
        ...
    def AskPartDuplicateRcps(self, part: Tag, tolerance: float, found_duplicates: bool, num_part_dup_rcp_lists: int, part_dup_rcp_lists: typing.List[UF.UFRoute.TagList]) -> None:
        ...
    def AskPartDuplicateSegs(self, part: Tag, tolerance: float, found_duplicates: bool, num_part_dup_seg_lists: int, part_dup_seg_lists: typing.List[UF.UFRoute.TagList]) -> None:
        ...
    def AskPartNumRcps(self, part: Tag, num_part_rcps: int) -> None:
        ...
    def AskPartNumSegs(self, part: Tag, num_part_segs: int) -> None:
        ...
    def AskPartOccPorts(self, part_tag: Tag, num_ports: int, ports: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPartPartType(self, r_part: Tag, type: int) -> None:
        ...
    def AskPartRcps(self, part: Tag, num_part_rcps: int, part_rcps: typing.List[Tag]) -> None:
        ...
    def AskPartSearchPath(self, path: Tag) -> None:
        ...
    def AskPartSegs(self, part: Tag, num_part_segs: int, part_segs: typing.List[Tag]) -> None:
        ...
    def AskPlacesTransform(self, places: int, origin: float, csys_matrix: float) -> None:
        ...
    def AskPortAlignFlag(self, port_tag: Tag, flag: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortAlignVector(self, port_tag: Tag, vector: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortBackExtension(self, port: Tag, ext: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortBackExtensionObj(self, port: Tag, ext: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortCharx(self, charx_name: str, expected_type: int, port_tag: Tag, desired_charx: UF.EplibCharx) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortClockIncrement(self, port: Tag, increment: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortConnPort(self, curr_port: Tag, connected_port: Tag) -> bool:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortConnectedPort(self, curr_port: Tag, connected_port: Tag, connected: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortConnection(self, port_tag: Tag, connection: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortCutBackLength(self, port: Tag, cut_back_length: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortEngageObj(self, port_tag: Tag, engage_obj: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortEngagedPos(self, port: Tag, position: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortEngagement(self, port_tag: Tag, distance: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortExtension(self, port: Tag, ext: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortExtensionObj(self, port: Tag, ext: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortLockInfo(self, port_occ: Tag, is_locked: bool, is_rotation_locked: bool, is_from_port: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortMultiport(self, port: Tag, multi: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortOccOfPort(self, port_tag: Tag, port_occ: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortOnSegment(self, segment: Tag, segend: int, port: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortPartOcc(self, port_tag: Tag, part_occ: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortPosition(self, port_tag: Tag, position: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortRotateFlag(self, port_tag: Tag, flag: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortRotateVector(self, port_tag: Tag, vector: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortSegment(self, port_tag: Tag, segment: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortStock(self, port_tag: Tag, stock_tag: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPortTerminalPorts(self, port: Tag, num_terms: int, terms: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskRcpAtTermPort(self, port: Tag, rcp: Tag, at: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskRcpCorner(self, rcp_tag: Tag, corner: Tag) -> None:
        ...
    def AskRcpOnPort(self, port_tag: Tag, rcp_tag: Tag) -> None:
        ...
    def AskRcpPorts(self, rcp: Tag, num_ports: int, ports: typing.List[Tag]) -> None:
        ...
    def AskRcpPosition(self, rcp_id: Tag, rcp_pos: float) -> None:
        ...
    def AskRcpSegments(self, rcp_tag: Tag, num_segs: int, segments: typing.List[Tag]) -> None:
        ...
    def AskRcpSegs(self, rcp_id: Tag, num_segs: int, segments: typing.List[Tag]) -> None:
        ...
    def AskRouteEnd(self, route: Tag, end: Tag) -> None:
        ...
    def AskRouteObjs(self, route: Tag, num_objs: int, objs: typing.List[Tag]) -> None:
        ...
    def AskRouteStart(self, route: Tag, start: Tag) -> None:
        ...
    def AskSegCurve(self, segment: Tag, curve: Tag) -> None:
        ...
    def AskSegRcps(self, segment: Tag, rcp: typing.List[Tag]) -> None:
        ...
    def AskSegmentBendCrnr(self, segment: Tag, corner: Tag) -> None:
        ...
    def AskSegmentBranchAngle(self, segment: Tag, branch_angle: float) -> None:
        ...
    def AskSegmentBundleStock(self, segment: Tag, harness: Tag, stock: Tag) -> None:
        ...
    def AskSegmentEndIdx(self, segment: Tag, end_object: Tag, index: int) -> None:
        ...
    def AskSegmentEndPnts(self, segment: Tag, start: float, end: float) -> None:
        ...
    def AskSegmentEndProps(self, segment: Tag, end: int, parameter: float, norm_parameter: float, point: float, tangent: float) -> None:
        ...
    def AskSegmentIntPart(self, segment: Tag, part: Tag) -> None:
        ...
    def AskSegmentIntParts(self, segment: Tag, num_parts: int, parts: typing.List[Tag]) -> None:
        ...
    def AskSegmentLength(self, segment: Tag, length: float) -> None:
        ...
    def AskSegmentPaths(self, segment: Tag, number_of_paths: int, paths: typing.List[Tag]) -> None:
        ...
    def AskSegmentRoutes(self, segment: Tag, num_routes: int, routes: typing.List[Tag]) -> None:
        ...
    def AskSegmentStock(self, segment: Tag, num_stock: int, stock: typing.List[Tag]) -> None:
        ...
    def AskSegmentWires(self, segment: Tag, num_wires: int, wires: typing.List[Tag]) -> None:
        ...
    def AskSegmentsIsPath(self, number_of_segments: int, segments: typing.List[Tag], path: Tag, is_path: bool) -> None:
        ...
    def AskSegmentsPaths(self, num_segments: int, segments: typing.List[Tag], num_paths: int, paths: typing.List[Tag], share_path: bool) -> None:
        ...
    def AskStockAnchor(self, stock_tag: Tag, anchor: Tag) -> None:
        ...
    def AskStockBody(self, stock_tag: Tag, body: Tag) -> None:
        ...
    def AskStockCrossSect(self, stock_tag: Tag, cross_section: Tag) -> None:
        ...
    def AskStockDataAnchors(self, stock_data_tag: Tag, num_anchors: int, anchors: typing.List[Tag]) -> None:
        ...
    def AskStockDataCross(self, stock_data_tag: Tag, num_cross_sections: int, cross_sections: typing.List[Tag]) -> None:
        ...
    def AskStockDataStock(self, stock_data_tag: Tag, num_stock: int, stock: typing.List[Tag]) -> None:
        ...
    def AskStockDiameter(self, stock: Tag, diameter: float) -> None:
        ...
    def AskStockFeature(self, stock_tag: Tag, feature: Tag) -> None:
        ...
    def AskStockHarness(self, stock: Tag, num_harness: int, harness: typing.List[Tag]) -> None:
        ...
    def AskStockPartOcc(self, stock: Tag, stock_component: Tag) -> None:
        ...
    def AskStockPorts(self, stock: Tag, ports: typing.List[Tag]) -> None:
        ...
    def AskStockProfilePort(self, stock_tag: Tag, profile_port: int) -> None:
        ...
    def AskStockRotation(self, stock_tag: Tag, rotation: float) -> None:
        ...
    def AskStockSegments(self, stock: Tag, num_segments: int, segments: typing.List[Tag]) -> None:
        ...
    def AskStockStockData(self, stock: Tag, stock_data: Tag) -> None:
        ...
    def AskStockStyle(self, stock_tag: Tag, style: int) -> None:
        ...
    def AskStockUnits(self, stock_tag: Tag, units: int) -> None:
        ...
    def AskStockWires(self, stock: Tag, num_wires: int, wires: typing.List[Tag]) -> None:
        ...
    def AskTerminalMultiport(self, terminal: Tag, multi: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskTerminalPortUid(self, terminal: Tag, uid: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskWireHarness(self, wire: Tag, num_harness: int, harness: typing.List[Tag]) -> None:
        ...
    def AskWireSegments(self, wire: Tag, num_segments: int, segments: typing.List[Tag]) -> None:
        ...
    def AskWireStock(self, wire: Tag, num_stock: int, stock: typing.List[Tag]) -> None:
        ...
    def AssignStock(self, stock_data_tag: Tag, anchor_tag: Tag, cross_tag: Tag, seg_count: int, segments: typing.List[Tag]) -> None:
        ...
    def AssignStockStyle(self, new_style: int, num_stocks: int, stock_tags: typing.List[Tag]) -> None:
        ...
    def CalcAbsMinmaxBox(self, dwg_view: Tag, box: float) -> None:
        ...
    def ComputeStockLength(self, stock: Tag, total_path_length: float) -> None:
        ...
    def ConnectPort(self, port: Tag, connection: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def ConvertToStockAsComponents(self, part: Tag, convert_subcomponents: bool, permanent_stock: bool, reuse_stock: bool) -> None:
        ...
    def CreateAnchorFromPnt(self, object_in_part: Tag, ref_point: Tag, anchor: Tag) -> None:
        ...
    def CreateAnchorFromPos(self, object_in_part: Tag, point_pos: float, anchor: Tag) -> None:
        ...
    def CreateBendByRadius(self, obj_id: Tag, radius: float, corner: Tag, seg: Tag) -> None:
        ...
    def CreateBendByRatio(self, obj_id: Tag, ratio: float, corner: Tag, seg: Tag) -> None:
        ...
    def CreateBendByTable(self, obj_id: Tag, table: str, corner: Tag, seg: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateBuiltInPath(self, part: Tag, num_objs: int, objs: typing.List[Tag], name: str, bip_tag: Tag) -> None:
        ...
    def CreateCrossSection(self, object_in_part: Tag, style: int, exprs: typing.List[Tag], num_curves: int, curves: typing.List[Tag], cross: Tag) -> None:
        ...
    def CreateIsoDrawing(self, part_tag: Tag) -> None:
        ...
    def CreateMiterCorner(self, obj_id: Tag, corner: Tag) -> None:
        ...
    def CreateMultiportFromPosition(self, part: Tag, position: float, align_flag: bool, align_vector: float, fixture_port: bool, term_id: str, port_tag: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreatePortAtSegend(self, segment: Tag, segend: int, rotate_flag: bool, port: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreatePortLock(self, from_port_occ: Tag, lock_rotation: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateRcpArcCenter(self, arc: Tag, new_rcp: Tag) -> None:
        ...
    def CreateRcpAtPort(self, port: Tag, new_rcp: Tag, check_existing_rcp: bool, found_existing_rcp: bool) -> None:
        ...
    def CreateRcpByWcsOff(self, _object: Tag, offset: float, new_rcp: Tag, check_existing_rcp: bool, found_existing_rcp: bool) -> None:
        ...
    def CreateRcpByWorkPos(self, work_pos: float, new_rcp: Tag, check_existing_rcp: bool, found_existing_rcp: bool) -> None:
        ...
    def CreateRcpCurveParm(self, curve: Tag, parm: float, new_rcp: Tag) -> None:
        ...
    def CreateRcpOnRcp(self, occ_rcp: Tag, new_rcp: Tag, check_existing_rcp: bool, found_existing_rcp: bool) -> None:
        ...
    def CreateRcpPoint(self, point: Tag, new_rcp: Tag) -> None:
        ...
    def CreateRcpPosition(self, pos: float, new_rcp: Tag) -> None:
        ...
    def CreateRoundCrossSection(self, object_in_part: Tag, style: int, diameter: float, offsets: str, cross: Tag) -> None:
        ...
    def CreateSegOnCurve(self, curve: Tag, rcp1: Tag, rcp2: Tag, new_segment: Tag) -> None:
        ...
    def CreateSegThruRcps(self, rcp1: Tag, rcp2: Tag, new_segment: Tag) -> None:
        ...
    def DeleteCharacteristics(self, obj_id: Tag, charx_count: int, list: typing.List[UF.EplibCharx]) -> None:
        ...
    def DeletePortLock(self, from_occ: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DisconnectPort(self, port: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def EnterCustomApp(self) -> None:
        ...
    def ExitCustomApp(self) -> None:
        ...
    def FindPartInPath(self, part_name: str, path: str) -> None:
        ...
    def FindPath(self, begin: Tag, end: Tag, path_size: int, path_data: typing.List[Tag]) -> None:
        ...
    def FindPortCharx(self, charx_name: str, type: int, port: Tag, charx: UF.EplibCharx) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def FindTerminalCharx(self, charx_name: str, charx_type: int, terminal: Tag, charx: UF.EplibCharx) -> None:
        ...
    def FindTerminalPort(self, multi: Tag, id: str, tag: Tag) -> bool:
        """[Obsolete("Deprecated")"""
        ...
    def FindTitleInCharx(self, num_charx: int, charx: typing.List[UF.EplibCharx], title: str, index: int) -> None:
        ...
    def FreePlaces(self, num_places: int, places: int) -> None:
        ...
    def GetNextConnections(self, curr_conn: Tag, curr_obj: Tag, num_conns: int, next_conns: typing.List[Tag], next_objs: typing.List[Tag]) -> None:
        ...
    def InitCustomApp(self) -> None:
        ...
    def IsPartAnchor(self, _object: Tag, is_anchor: bool) -> None:
        ...
    def IsPartFabrication(self, fab_part: Tag, fab: bool) -> None:
        ...
    def IsPartOccRoutePart(self, obj_id: Tag) -> bool:
        ...
    def IsPortConnected(self, port_tag: Tag, is_connected: bool) -> None:
        ...
    def IsPortFixturePort(self, port: Tag, is_fixture: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def IsPortMulti(self, port: Tag) -> bool:
        """[Obsolete("Deprecated")"""
        ...
    def IsPortTerminal(self, port: Tag) -> bool:
        """[Obsolete("Deprecated")"""
        ...
    def IsRcpBendSegRcp(self, candidate: Tag, corner: Tag) -> bool:
        ...
    def IsRcpMiterCorner(self, rcp: Tag) -> bool:
        ...
    def IsSegment(self, _object: Tag, is_segment: bool) -> None:
        ...
    def IsSegmentInsidePart(self, segment: Tag, part_occ: Tag) -> bool:
        ...
    def IsStockEqual(self, stock1: Tag, stock2: Tag) -> bool:
        ...
    def IsStockInterior(self, stock: Tag, is_interior: bool) -> None:
        ...
    def IsTerminalSegment(self, segment: Tag, is_term: bool) -> None:
        ...
    def IsWireOnSegment(self, wire: Tag, segment: Tag, on_seg: bool) -> None:
        ...
    def LoadAppView(self, filename: str, app_view: int) -> None:
        ...
    def LoadAppViewList(self, num_app_views: int, app_views: typing.List[UF.UFRoute.AppViewDesc]) -> None:
        ...
    def LoadPartByCharx(self, num_charx: int, charx: typing.List[UF.EplibCharx], part: Tag) -> None:
        ...
    def LoadPartByName(self, part_name: str, member_name: str, part: Tag) -> None:
        ...
    def LoadStockByCharx(self, stock: UF.EplibPartLibPart, anchor_name: str, stock_style: int, stock_data_tag: Tag, anchor_tag: Tag, cross_tag: Tag) -> None:
        ...
    def LoadStockData(self, part_name: str, member_name: str, stock_style: int, stock_data_tag: Tag, anchor_tag: Tag, cross_tag: Tag) -> None:
        ...
    def MatchCharxInPlib(self, start: str, num_criteria: int, criteria: typing.List[UF.EplibCharx], num_matches: int, matches: typing.List[UF.EplibPartLibPart]) -> None:
        ...
    def MergeRcps(self, num_rcps: int, rcps: typing.List[Tag], preferred_rcp: Tag, num_remaining: int, remaining: typing.List[Tag]) -> None:
        ...
    def RegisterCustomApp(self, app_id: int) -> None:
        ...
    def RemoveCorner(self, corner: Tag) -> None:
        ...
    def RemoveSegFromStock(self, seg: Tag, num_stock: int, stock: typing.List[Tag]) -> None:
        ...
    def RemoveStock(self, num_segs: int, segments: typing.List[Tag]) -> None:
        ...
    def RemoveTerminalPorts(self, multi: Tag, num_terms: int, terms: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RemoveVirtualPorts(self, multi: Tag, num_terms: int, terms: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def ReuseStockPart(self, stock: Tag) -> None:
        ...
    def SetBuiltInPathObjs(self, bip: Tag, num_objs: int, objs: typing.List[Tag]) -> None:
        ...
    def SetCharacteristics(self, obj_id: Tag, charx_count: int, list: typing.List[UF.EplibCharx]) -> None:
        ...
    def SetCharxEnv(self, num_charx: int, charx: typing.List[UF.EplibCharx]) -> None:
        ...
    def SetCurrentAppView(self, app_view: int) -> None:
        ...
    def SetPartInStock(self, occ: Tag) -> None:
        ...
    def SetPartSearchPath(self, dirpath: Tag) -> None:
        ...
    def SetPortBackExtension(self, port: Tag, ext: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortBackExtensionObj(self, port: Tag, ext: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortClockIncrement(self, port: Tag, increment: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortEngagement(self, port: Tag, eng: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortEngagementObj(self, port: Tag, eng: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortExtension(self, port: Tag, ext: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortExtensionObj(self, port: Tag, ext: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortId(self, obj_id: Tag, port_id: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortLockRotationFlag(self, port_occ: Tag, rotation_locked: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPortRotByPoint(self, pnt_pos: float, port_tag: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetStockPartName(self, stock: Tag, part_name: str) -> None:
        ...
    def SetStockStyle(self, new_style: int, num_stocks: int, stock_tags: typing.List[Tag]) -> None:
        ...
    def SimplifyRcps(self, count: int, rcps: typing.List[Tag]) -> None:
        ...
    def SimplifySegments(self, count: int, segments: typing.List[Tag], num_new_segments: int, new_segments: typing.List[Tag]) -> None:
        ...
    def SolvePlaces(self, placer: Tag, part_occ: Tag, num_places: int, places: int) -> None:
        ...
    def StockAskName(self, stock: Tag, name: str) -> None:
        ...
    def TransformObjects(self, tags: typing.List[Tag], num_tags: int, transform: float, copy_operation: bool, copy_tags: typing.List[Tag]) -> None:
        ...
    def UnsetShadowForView(self, view: Tag) -> None:
        ...
    def UpdateCharxEnv(self, num_charx: int, charx: typing.List[UF.EplibCharx]) -> None:
        ...


    class UFRouteTagList():
        num_alloc: int
        num_used: int
        array: typing.List[Tag]
    

    class UFRouteCharDesc():
        name: str
        type: int
    

    class UFRouteBendReportYbc():
        num_bends: int
        y: float
        b: float
        c: float
        radii: float
        total_length: float
    

    class UFRouteBendReportXyz():
        num_bends: int
        xc: float
        yc: float
        zc: float
        radii: float
        total_length: float
    

    class UFRouteBendReportMil98():
        num_bends: int
        c: float
        f: float
        e: float
        g: float
        y: float
        total_length: float
    

    class UFRouteAppViewDesc():
        name: str
        filename: str
    

class UFPs(Utilities.NXRemotableObject):
    def AskCurrentHighestTag(self, highest_tag: Tag) -> None:
        ...
    def AskCurrentPartition(self, partition: Tag) -> None:
        ...
    def AskEntityPartition(self, entity: Tag, partition: Tag) -> None:
        ...
    def AskJournalData(self, journal_state: int, journal_name: str) -> None:
        ...
    def AskKernelVersion(self, version_data: UF.UFPs.KernelVersion) -> None:
        ...
    def AskObjectOfPsTag(self, ps_tag: Tag, obj_id: Tag) -> None:
        ...
    def AskPsTagOfObject(self, obj_id: Tag, ps_tag: Tag) -> None:
        ...
    def AskTagsRemaining(self, tags_remaining: int) -> None:
        ...
    def CreateObjFromPsTag(self, ps_tag: Tag, ug_tag: Tag) -> None:
        ...
    def CreatePartition(self, partition: Tag) -> None:
        ...
    def CreatePsTrimmedCurve(self, curve_or_edge: Tag, ps_curve: Tag) -> None:
        ...
    def ExportData(self, body_list: typing.List[Tag], file_name: str) -> None:
        ...
    def ExportLinkedData(self, tags: typing.List[Tag], n_tags: int, file_name: str, version: int, link_fnc: UF.UFPs.LinkFPT, n_unexported: int, unexported_tags: typing.List[UF.UFPs.Unexported]) -> None:
        ...
    def ImportData(self, file_name: str, body_list: typing.List[Tag]) -> None:
        ...
    def SetCurrentPartition(self, partition: Tag) -> None:
        ...
    def SetJournalState(self, journal_state: int) -> None:
        ...
    def WriteToJournal(self, journal_commt: str) -> None:
        ...


    class UFPsUnexported():
        ug_body_tag: Tag
        fail_code: int
    

    

    class UFPsKernelVersion():
        major_revision: int
        minor_revision: int
        build_number: int
        year: int
        month: int
        day: int
        hour: int
        minute: int
        second: int
    

class UFProcessAid(Utilities.NXRemotableObject):
    def AskChildrenFeatures(self, feature_set: Tag, num_children: int, children: typing.List[Tag]) -> None:
        ...
    def AskDatumObjects(self, feature_set: Tag, num_dat_points: int, datum_point: typing.List[Tag], num_dat_vectors: int, datum_vector: typing.List[Tag], num_sets: int, n_objects_in_each_set: int, objects: typing.List[Tag]) -> None:
        ...
    def AskDatumsInPart(self, part_tag: Tag, feat_type: UF.UFProcessAid.Types, feature_sets: typing.List[Tag]) -> None:
        ...
    def AskLinkObjects(self, _object: Tag, linked_objects: typing.List[Tag], linked_object_count: int) -> None:
        ...
    def AskParentFeature(self, feature_set: Tag, parent_datum: Tag) -> None:
        ...
    def AskSectionOfDatum(self, datum_feat: Tag, num_sections: int, sec_planes: typing.List[Tag]) -> None:
        ...
    def AskSourceObject(self, _object: Tag, is_recurse: bool, source_object: Tag, file_to_open: str) -> None:
        ...
    def IsDatumObject(self, _object: Tag, is_datum: bool, datum_type: UF.UFProcessAid.Types, feature_set_tag: Tag) -> None:
        ...
    def PopulateAttrList(self, feature_set: Tag, count: int, list: str) -> None:
        ...


    class Types(enum.Enum):
        DatumLocSurfType = 1
        DatumLocHoleType = 2
        DatumLocSlotType = 4
        DatumLocPinType = 8
        DatumLocSurfNaType = 16
        DatumLocHoleNaType = 32
        DatumLocSlotNaType = 64
        DatumLocPinNaType = 128
        DatumPtType = 256
        CertPtType = 512
        CertPtNaType = 1024
        MeaSurfVecType = 2048
        MeaHoleVecType = 4096
        MeaSlotVecType = 8192
        MeaStudVecType = 16384
        MeaTrimVecType = 32768
        MeaHemVecType = 65536
        MeaVecNaType = 131072
        MeaLocSurfType = 262144
        MeaLocHoleType = 524288
        MeaLocSlotType = 1048576
        MeaLocPinType = 2097152
        MeaLocSurfNaType = 4194304
        MeaLocHoleNaType = 8388608
        MeaLocSlotNaType = 16777216
        MeaLocPinNaType = 33554432
        MeaPtType = 67108864
        AllDatumTypes = 134217727
    

class UFPoint(Utilities.NXRemotableObject):
    def AskPointOutput(self, point_feature_id: Tag, point_id: Tag) -> None:
        ...
    def Create3Scalars(self, xyz: typing.List[Tag], point_feature_id: Tag) -> None:
        ...
    def CreateAlongCurve(self, curve: Tag, base_point: Tag, t: Tag, option: UF.UFSo.PointAlongCurveOption, flip: bool, point_feature_id: Tag) -> None:
        ...
    def CreateAtConicCenter(self, conic: Tag, point_feature_id: Tag) -> None:
        ...
    def CreateAtIntersectionOfTwoCurves(self, curve1: Tag, curve2: Tag, help_point1: Tag, help_point2: Tag, point_feature_id: Tag) -> None:
        ...
    def CreateOnArcAngle(self, arc: Tag, angle: Tag, xform: Tag, point_feature_id: Tag) -> None:
        ...
    def CreateOnCurve(self, curve: Tag, t: Tag, point_feature_id: Tag) -> None:
        ...
    def CreateOnSurface(self, surface: Tag, u: Tag, v: Tag, point_feature_id: Tag) -> None:
        ...
    def CreateSurfaceCurveIntersection(self, surface: Tag, curve: Tag, help_point1: Tag, help_point2: Tag, point_feature_id: Tag) -> None:
        ...
    def CreateWithOffset(self, base_point: Tag, offset: Tag, point_feature_id: Tag) -> None:
        ...


class UFPlot(Utilities.NXRemotableObject):
    def AddJobToPlotLayout(self, drawing_sheet: Tag, job_options: UF.UFPlot.JobOptions, job_name: str, units: UF.UFPlot.Units, origin: float, rotation: UF.UFPlot.Rotation, scale: float, extents: UF.UFPlot.Extents) -> None:
        ...
    def AskDefaultBannerOptions(self, banner_options: UF.UFPlot.BannerOptions) -> None:
        ...
    def AskDefaultCustomColors(self, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def AskDefaultCustomWidths(self, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def AskDefaultJobName(self, drawing_sheet: Tag, job_name: str) -> None:
        ...
    def AskDefaultJobOptions(self, job_options: UF.UFPlot.JobOptions) -> None:
        ...
    def AskDefaultPrinterAndProfile(self, printer: str, profile: str) -> None:
        ...
    def AskDrawingSheetColors(self, drawing_sheet: Tag, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def AskDrawingSheetWidths(self, drawing_sheet: Tag, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def AskPlotLayoutExtents(self, units: UF.UFPlot.Units, extents: UF.UFPlot.Extents) -> None:
        ...
    def AskPrinterGroups(self, num_printer_groups: int, printer_groups: typing.List[UF.UFPlot.PrinterGroup]) -> None:
        ...
    def AskPrinterNames(self, num_printers: int, printers: str) -> None:
        ...
    def AskProfileNames(self, printer: str, num_profiles: int, profiles: str) -> None:
        ...
    def AskSessionBannerOptions(self, banner_options: UF.UFPlot.BannerOptions) -> None:
        ...
    def AskSessionCustomColors(self, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def AskSessionCustomWidths(self, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def AskSessionJobOptions(self, job_options: UF.UFPlot.JobOptions) -> None:
        ...
    def ClearPlotLayout(self) -> None:
        ...
    def CompareUghpglFiles(self, first_plot: str, second_plot: str, compare_options: UF.UFPlot.UghpglCmpOptions, result_plot: str, comparison_result: UF.UFPlot.DiffCmpStatus) -> None:
        ...
    def ConvertCustomWidths(self, units: UF.UFPlot.Units, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def ConvertFile(self, cgm_or_tiff_file_name: str, output_format: UF.UFPlot.Format, output_file_name: str) -> None:
        ...
    def DeleteDrawingSheetColors(self, drawing_sheet: Tag) -> None:
        ...
    def DeleteDrawingSheetWidths(self, drawing_sheet: Tag) -> None:
        ...
    def HasDrawingSheetColors(self, drawing_sheet: Tag, drawing_sheet_has_colors: bool) -> None:
        ...
    def HasDrawingSheetWidths(self, drawing_sheet: Tag, drawing_sheet_has_widths: bool) -> None:
        ...
    def Print(self, drawing_sheet: Tag, job_options: UF.UFPlot.JobOptions, job_name: str, banner_options: UF.UFPlot.BannerOptions, printer: str, profile: str, num_copies: int) -> None:
        ...
    def PrintFile(self, filename: str, printer: str, profile: str, num_copies: int) -> None:
        ...
    def PrintPlotLayout(self, job_name: str, banner_options: UF.UFPlot.BannerOptions, printer: str, profile: str, num_copies: int) -> None:
        ...
    def ReadCustomColorsFromCdf(self, cdf_name: str, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def ReadCustomWidthsFromWdf(self, wdf_name: str, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def SaveCgm(self, drawing_sheet: Tag, job_options: UF.UFPlot.JobOptions, job_name: str, banner_options: UF.UFPlot.BannerOptions, cgm_file_name: str) -> None:
        ...
    def SaveCgmForPlotLayout(self, job_name: str, banner_options: UF.UFPlot.BannerOptions, cgm_file_name: str) -> None:
        ...
    def SetDrawingSheetColors(self, drawing_sheet: Tag, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def SetDrawingSheetWidths(self, drawing_sheet: Tag, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def SetPrinterGroup(self, group_dir: str, jobs_dir: str, home_dir: str) -> None:
        ...
    def SetSessionBannerOptions(self, banner_options: UF.UFPlot.BannerOptions) -> None:
        ...
    def SetSessionCustomColors(self, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def SetSessionCustomWidths(self, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def SetSessionJobOptions(self, job_options: UF.UFPlot.JobOptions) -> None:
        ...
    def SetUghpglSmallTol(self, small_tolerance: float, units: int) -> None:
        ...
    def SetUghpglTol(self, shift_tolerance: float, units: int) -> None:
        ...
    def WriteCustomColorsToCdf(self, cdf_name: str, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def WriteCustomWidthsToWdf(self, wdf_name: str, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...


    class Widths(enum.Enum):
        StandardWidths = 0
        SingleWidth = 1
        Custom3Widths = 2
        CustomPaletteWidths = 3
    

    class Units(enum.Enum):
        Millimeters = 1
        Inches = 2
    

    class UFPlotUghpglCmpOptions():
        color_width_option: UF.UFPlot.CmpColorWidth
        resulting_plot_option: UF.UFPlot.CreateCmpResultPlot
        plot_tolerance: float
    

    class Rotation(enum.Enum):
        Rotation0 = 0
        Rotation90 = 1
        Rotation180 = 2
        Rotation270 = 3
    

    class UFPlotPrinterGroup():
        group_dir: str
        jobs_dir: str
        home_dir: str
        label: str
    

    class UFPlotJobOptions():
        colors: UF.UFPlot.Colors
        use_drawing_sheet_colors: bool
        widths: UF.UFPlot.Widths
        use_drawing_sheet_widths: bool
        tolerance: float
    

    class Format(enum.Enum):
        CgmFormat = 0
        EmfFormat = 1
        TiffFormat = 2
        JpegFormat = 3
        PngFormat = 4
    

    class UFPlotExtents():
        left: float
        right: float
        bottom: float
        top: float
    

    class DiffCmpStatus(enum.Enum):
        CmpNoDiffFound = 0
        CmpDiffFound = 1
    

    class CreateCmpResultPlot(enum.Enum):
        CreateCmpPlot = 1
        CreateCmpPlotDiffOnly = 2
        CreateCmpNoPlot = 3
    

    class Colors(enum.Enum):
        AsDisplayedColors = 0
        PartColors = 1
        CustomPaletteColors = 2
        BlackOnWhite = 3
        LegacyColors = 4
        ColorByWidth = 5
    

    class CmpColorWidth(enum.Enum):
        CmpColorWidth = 1
        CmpNoColorWidth = 2
    

    class UFPlotBannerOptions():
        show_banner: bool
        message: str
    

class UFPlist(Utilities.NXRemotableObject):
    def AddEntities(self, obj_id: Tag, num_to_add: int, objects: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AddObject(self, parts_list: Tag, add_components_as_subassemblies: bool, _object: Tag) -> None:
        ...
    def AskAttachedRows(self, parent: Tag, nm_rows: int, children_rows: typing.List[Tag]) -> None:
        ...
    def AskColPrefs(self, col: Tag, col_prefs: UF.UFPlist.ColPrefs) -> None:
        ...
    def AskDefaultColPrefs(self, col_prefs: UF.UFPlist.ColPrefs) -> None:
        ...
    def AskDefaultPrefs(self, plist_prefs: UF.UFPlist.Prefs) -> None:
        ...
    def AskLdrMethod(self, row: Tag, ldr_method: int) -> None:
        ...
    def AskNestedAssyParentComp(self, column: Tag, component: Tag) -> None:
        ...
    def AskObjects(self, parts_list: Tag, nm_objects: int, objects: typing.List[Tag]) -> None:
        ...
    def AskPrefs(self, parts_list: Tag, prefs: UF.UFPlist.Prefs) -> None:
        ...
    def AskRowLock(self, row: Tag, lock_state: bool) -> None:
        ...
    def AskTag(self) -> Tag:
        """[Obsolete("Deprecated")"""
        ...
    def AskTagOfNote(self, obj_id: Tag) -> Tag:
        """[Obsolete("Deprecated")"""
        ...
    def AskTags(self, parts_list: typing.List[Tag], num: int) -> None:
        ...
    def AskTraversalSettings(self, parts_list: Tag, traversal_settings: UF.UFPlist.TraversalSettings) -> None:
        ...
    def AttachRows(self, parent_row: Tag, nm_rows: int, children_rows: typing.List[Tag]) -> None:
        ...
    def Create(self, prefs: UF.UFPlist.Prefs, origin: float, parts_list: Tag) -> None:
        ...
    def CreateColumn(self, width: float, col_prefs: UF.UFPlist.ColPrefs, column_type: UF.UFPlist.ColumnType, column: Tag) -> None:
        ...
    def CreateFromTemplate(self, template_name: str, origin: float, parts_list: Tag) -> None:
        ...
    def CreateManualRow(self, height: float, row: Tag) -> None:
        ...
    def CreateNote(self, obj_id: Tag, position: float, note_obj_id: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DefineField(self, obj_id: Tag, pos: int, line_1: str, line_2: str, attr_title: str, f_format: UF.UFPlist.FieldFormat, f_width: int, f_type: int, p_mask: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def List(self, obj_id: Tag) -> None:
        ...
    def ListToFile(self, obj_id: Tag, out_filename: str, new_file: int, plist_level: str) -> None:
        ...
    def RemoveEntity(self, obj_id: Tag, num_to_add: int, objects: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RemoveField(self, obj_id: Tag, field: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RemoveObject(self, parts_list: Tag, remove_components_as_subassemblies: bool, _object: Tag) -> None:
        ...
    def SetColPrefs(self, col: Tag, col_prefs: UF.UFPlist.ColPrefs) -> None:
        ...
    def SetColumnModes(self, obj_id: Tag, rowmax: int, rowpos: int, rowgap: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetDefaultPrefs(self, plist_prefs: UF.UFPlist.Prefs) -> None:
        ...
    def SetDisplayModes(self, obj_id: Tag, attr_title: str, sort_mode: int, header_mode: int, callout_mode: int, box_mode: int, report_mode: int, symbol_mode: int, line_space: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetFitCharSizes(self, obj_id: Tag, csize_option: int, dash_option: int, ccsize: float, dcsize: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetFitRules(self, obj_id: Tag, priorities: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetFrozenLevel(self, obj_id: Tag, value: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetNestedAssyParentComp(self, column: Tag, component: Tag) -> None:
        ...
    def SetPrefs(self, parts_list: Tag, prefs: UF.UFPlist.Prefs) -> None:
        ...
    def SetReportMode(self, obj_id: Tag, value: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetRowLock(self, row: Tag, lock_state: bool) -> None:
        ...
    def SetSecondSort(self, obj_id: Tag, attr_title: str, smode2: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetSkipLevel(self, obj_id: Tag, value: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetTraversalSettings(self, parts_list: Tag, traversal_settings: UF.UFPlist.TraversalSettings) -> None:
        ...
    def Update(self, parts_list: Tag) -> None:
        ...
    def UpdateAllPlists(self) -> None:
        ...


    class UFPlistTraversalSettings():
        master_model: bool
        top_level_only: bool
        leaves_only: bool
    

    class SymbolType(enum.Enum):
        SymbolTypeNone = 0
        SymbolTypeIdSymbolCircle = 1
        SymbolTypeIdSymbolDivCircle = 2
        SymbolTypeIdSymbolDownTriangle = 3
        SymbolTypeIdSymbolUpTriangle = 4
        SymbolTypeIdSymbolSquare = 5
        SymbolTypeIdSymbolDivSquare = 6
        SymbolTypeIdSymbolHexagon = 7
        SymbolTypeIdSymbolDivHexagon = 8
        SymbolTypeIdSymbolQuadCircle = 9
        SymbolTypeIdSymbolRoundedBox = 10
        SymbolTypeIdSymbolUnderline = 11
    

    class UFPlistPrefs():
        section_prefs: UF.UFTabnot.SectionPrefs
        grow_direction: UF.UFPlist.GrowDirection
        ldr_method: UF.UFPlist.LdrMethod
        create_new_rows_as_locked: bool
        initial_callout_field: str
        callout_increment: int
        symbol_type: UF.UFPlist.SymbolType
        main_symbol_text: str
        ref_symbol_text: str
        characters_to_skip: str
        auto_update: bool
        sort_on_update: bool
        highlight_manual_text: bool
        isProtected: bool
        allowManualRows: bool
    

    class LdrMethod(enum.Enum):
        LdrMethodStrikeThru = 1
        LdrMethodBlank = 2
        LdrMethodRemove = 3
        LdrMethodOrdinary = 4
    

    class GrowDirection(enum.Enum):
        GrowDirectionUp = 1
        GrowDirectionDown = 2
    

    class UFPlistFieldFormat():
        justification: int
        lead_str: str
        trailing_str: str
        format_type: int
        width: int
        precision: int
    

    class ColumnType(enum.Enum):
        ColumnTypeGeneral = 0
        ColumnTypeCallout = 1
        ColumnTypeQuantity = 2
    

    class UFPlistColPrefs():
        is_key_field: bool
        default_string: str
        cell_prefs: UF.UFTabnot.CellPrefs
        is_protected: bool
    

class UFPd(Utilities.NXRemotableObject):
    def AddBusinessProcessModifier(self, product_attribute: Tag, modifier_name: str) -> None:
        ...
    def AskBusinessProcessModifierData(self, business_process_modifier: Tag, business_modifier: UF.UFPd.BusinessModifier) -> None:
        ...
    def AskBusinessProcessModifierType(self, business_process_modifier: Tag, type: UF.PdBusModfrType) -> None:
        ...
    def AskBusinessProcessModifiers(self, product_attributes: Tag, modifiers: typing.List[Tag], num_modifiers: int) -> None:
        ...
    def AskDefinitionAllowableGeometry(self, definition: Tag, num_allowable_geometry: int, allowable_geom: str) -> None:
        ...
    def AskProductAttribueData(self, attribute: Tag, attribute_data: UF.UFPd.ProductAttribute) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskProductAttribueData2(self, attribute: Tag, attribute_data: UF.UFPd.ProductAttribute2) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskProductAttribueValueData(self, attribute_value: Tag, value_data: UF.UFPd.AttributeValue) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskProductAttribues(self, product_definition: Tag, product_attributess: typing.List[Tag], num_product_attributes: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskProductAttributeData(self, attribute: Tag, attribute_data: UF.UFPd.ProductAttribute) -> None:
        ...
    def AskProductAttributeData2(self, attribute: Tag, attribute_data: UF.UFPd.ProductAttribute2) -> None:
        ...
    def AskProductAttributeValueData(self, attribute_value: Tag, value_data: UF.UFPd.AttributeValue) -> None:
        ...
    def AskProductAttributes(self, product_definition: Tag, product_attributess: typing.List[Tag], num_product_attributes: int) -> None:
        ...
    def AskProductDefinitionData(self, product_definition: Tag, product_definitions: typing.List[UF.UFPd.ProductDefinition]) -> None:
        ...
    def AskProductDefinitionFromInstance(self, instance: Tag, product_definition: Tag) -> None:
        ...
    def AskProductDefinitions(self, context: Tag, product_definitions: typing.List[Tag], num_product_definitions: int) -> None:
        ...
    def AskProductDefinitionsInstances(self, product_definition: Tag, instances: typing.List[Tag], num_instances: int) -> None:
        ...
    def AskProductDefinitionsOfGeometry(self, geometry_references: typing.List[Tag], num_geometry_references: int, product_definitions: typing.List[Tag], num_product_definitions: int) -> None:
        ...
    def CreateProductDefinition(self, product_definition: UF.UFPd.ProductDefinition, product_definition_created: Tag) -> None:
        ...
    def FreeBusinessModifierData(self, business_modifier: UF.UFPd.BusinessModifier) -> None:
        ...
    def FreeProductAttributeData(self, attr: UF.UFPd.ProductAttribute) -> None:
        ...
    def FreeProductAttributeData2(self, attr: UF.UFPd.ProductAttribute2) -> None:
        ...
    def FreeProductAttributeValueData(self, value_data: UF.UFPd.AttributeValue) -> None:
        ...
    def InitAttribute(self, attribute_data: UF.UFPd.ProductAttribute) -> None:
        ...
    def InitAttributeValue(self, attribute_value_data: UF.UFPd.AttributeValue) -> None:
        ...
    def InitBusinessModifier(self, business_modifier: UF.UFPd.BusinessModifier) -> None:
        ...
    def InitProductDefinition(self, product_definition_data: UF.UFPd.ProductDefinition) -> None:
        ...
    def IsRetained(self, product_definition: Tag, retained: bool) -> None:
        ...
    def ModifyProductAttribute(self, attribute: Tag, data: UF.UFPd.ProductAttribute) -> None:
        ...
    def SetBusinessProcessModifierData(self, business_process_modifier: Tag, business_modifier: UF.UFPd.BusinessModifier) -> None:
        ...
    def SetProductDefinitionData(self, product_definition: Tag, product_definition_data: UF.UFPd.ProductDefinition) -> None:
        ...


    class UFPdProductDefinition():
        name: str
        geometry_references: typing.List[Tag]
        num_geometry_references: int
        retained: bool
        product_attributes: typing.List[UF.UFPd.ProductAttribute]
        num_product_attributes: int
    

    class UFPdProductAttribute2():
        attribute_type: UF.UFPd.AttributeType
        attribute_group: str
        attribute_type_name: str
        attribute_name: str
        symbolic_display: str
        kf_name: str
        number_busmods: int
        busmods: typing.List[UF.UFPd.BusinessModifier]
        values: typing.List[UF.UFPd.AttributeValue]
        num_attribute_values: int
        value_dats: typing.List[UF.UFPd.AttributeValueData2]
        num_attribute_value_dats: int
    

    class UFPdProductAttribute():
        attribute_type: UF.UFPd.AttributeType
        attribute_group: str
        attribute_type_name: str
        attribute_name: str
        symbolic_display: str
        kf_name: str
        number_busmods: int
        busmods: typing.List[UF.UFPd.BusinessModifier]
        values: typing.List[UF.UFPd.AttributeValue]
        num_attribute_values: int
        value_dats: typing.List[UF.UFPd.AttributeValueData]
        num_attribute_value_dats: int
    

    class UFPdBusinessModifier():
        title: str
        value: str
    

    class AttributeValueType(enum.Enum):
        IntegerValue = 0
        NumberValue = 1
        StringValue = 2
        ListValue = 3
        UrlValue = 4
    

    class UFPdAttributeValueString():
        num_strings: int
        strings: str
    

    class UFPdAttributeValueData2():
        title: str
        dat: typing.List[UF.UFPd.AttributeValueString]
    

    class UFPdAttributeValueData():
        title: str
        dat: UF.UFPd.AttributeValueString
    

    class UFPdAttributeValue():
        value_type: UF.UFPd.AttributeValueType
        value_title: str
        integer_value: int
        number_value: float
        string_value: str
    

    class AttributeType(enum.Enum):
        NullAttributeType = 0
        UgUserDefined = 1
        StringType = 2
        IntegerType = 3
        NumberType = 4
        EnterpriseIdentifierType = 5
        PartIdentifierType = 6
        MaterialSpecificationType = 7
        ProcessSpecificationType = 8
        SurfaceFinishType = 9
        GenericNoteType = 10
        SpecificNoteType = 11
        BalloonNoteType = 12
        LocatorDesignatorType = 13
        CoordinateNoteType = 14
        ExportControlType = 15
        GovernmentSecurityInfoType = 16
        CompanyProprietaryInfoType = 17
        GenericEmarkingType = 18
        SpurGearType = 19
        HelicalGearType = 20
        StraightSidedSplineType = 21
        InvoluteSplineType = 22
        NumAttributeTypes = 23
    

class UFPatt(Utilities.NXRemotableObject):
    def AskData(self, _object: Tag, name: str, file_name: str, view_dependent_status: int, layer: int, retrieval_status: int, transform_data: float) -> None:
        ...
    def AskParams(self, tag: Tag, origin_display: UF.UFPatt.Switch, max_min_display: UF.UFPatt.Switch, control_pt_display: UF.UFPatt.Switch) -> None:
        ...
    def CreatePoint(self, coordinates: float, tag: Tag) -> None:
        ...
    def CycleErrors(self, ia1: int, cr2: str) -> None:
        ...
    def Import(self, file_name: str, pattern_name: str, autoscale_option: int, transform_data: float, pattern: Tag) -> None:
        ...
    def IsArchivingOn(self, on: bool) -> None:
        ...
    def IsShadingOn(self, on: bool) -> None:
        ...
    def SetArchiving(self, setting: UF.UFPatt.Switch) -> None:
        ...
    def SetParams(self, tag: Tag, origin_status: UF.UFPatt.Switch, max_min_status: UF.UFPatt.Switch, control_pt_status: UF.UFPatt.Switch) -> None:
        ...
    def SetShading(self, setting: UF.UFPatt.Switch) -> None:
        ...


    class Switch(enum.Enum):
        Off = 0
        On = 1
    

class UFPath(Utilities.NXRemotableObject):
    def CreateAuxfun(self, path_id: int, auxfun_code: int, text: str) -> None:
        ...
    def CreateCircularMotion(self, path_id: int, circular_motion_data: UF.UFPath.CircularMotion) -> None:
        ...
    def CreateClamp(self, path_id: int, clamp_status: UF.UFPath.ClampStatus, axis_type: UF.UFPath.Axis, text: str) -> None:
        ...
    def CreateContactCircularMotion(self, path_id: int, motion_data: UF.UFPath.CircularMotion, contact_data: UF.UFPath.ContactData) -> None:
        ...
    def CreateContactLinearMotion(self, path_id: int, linear_motion_data: UF.UFPath.LinearMotion, contact_data: UF.UFPath.ContactData) -> None:
        ...
    def CreateCoolantOff(self, paht_id: int, text: str) -> None:
        ...
    def CreateCoolantOn(self, path_id: int, coolant_type: UF.UFPath.CoolantType, text: str) -> None:
        ...
    def CreateCutWire(self, path_id: int, text: str) -> None:
        ...
    def CreateCutcom(self, path_id: int, cutcom_data: UF.UFPath.Cutcom, text: str) -> None:
        ...
    def CreateDwell(self, path_id: int, dwell_value: float, dwell_unit: UF.UFPath.DwellUnit, text: str) -> None:
        ...
    def CreateFedrat(self, path_id: int, fedrat_value: float, text: str) -> None:
        ...
    def CreateFlush(self, path_id: int, flush_data: UF.UFPath.Flush, text: str) -> None:
        ...
    def CreateFlushTank(self, path_id: int, tank_type: UF.UFPath.TankType, text: str) -> None:
        ...
    def CreateHelicalMotion(self, path_id: int, helical_motion_data: UF.UFPath.HelicalMotion) -> None:
        ...
    def CreateLevelMarker(self, path_id: int, level_marker_data: UF.UFPath.LevelMarker) -> None:
        ...
    def CreateLinearMotion(self, path_id: int, linear_motion_data: UF.UFPath.LinearMotion) -> None:
        ...
    def CreateOpSkip(self, path_id: int, skip_option: UF.UFPath.OpSkip, text: str) -> None:
        ...
    def CreateOpStop(self, path_id: int, text: str) -> None:
        ...
    def CreateOpmessage(self, path_id: int, text: str) -> None:
        ...
    def CreateOrigin(self, path_id: int, origin_coordinates: float, text: str) -> None:
        ...
    def CreatePower(self, path_id: int, power_value: float, text: str) -> None:
        ...
    def CreatePprint(self, path_id: int, text: str) -> None:
        ...
    def CreatePrefun(self, path_id: int, prefun_code: int, text: str) -> None:
        ...
    def CreateRotate(self, path_id: int, rotate_data: UF.UFPath.Rotate, text: str) -> None:
        ...
    def CreateSelectHead(self, path_id: int, head_type: UF.UFPath.HeadType, text: str) -> None:
        ...
    def CreateSeqno(self, path_id: int, seq_type: UF.UFPath.Seqno, seq_number: int, seq_incr: int, seq_freq: int, text: str) -> None:
        ...
    def CreateSetMode(self, path_id: int, ouput_mode: UF.UFPath.OutputMode, feedrate_mode: UF.UFPath.FeedrateMode, arc_mode: UF.UFPath.ArcMode, parallel_mode: UF.UFPath.ParallelMode, machine_mode: UF.UFPath.MachineMode, text: str) -> None:
        ...
    def CreateSpindleOff(self, path_id: int, text: str) -> None:
        ...
    def CreateSpindleOn(self, path_id: int, spindle_on_data: UF.UFPath.SpindleOn, text: str) -> None:
        ...
    def CreateSpindleReverse(self, path_id: int, text: str) -> None:
        ...
    def CreateStop(self, path_id: int, text: str) -> None:
        ...
    def CreateText(self, path_id: int, text: str) -> None:
        ...
    def CreateThreadWire(self, path_id: int, text: str) -> None:
        ...
    def CreateToolChange(self, path_id: int, tool_change_data: UF.UFPath.ToolChange, text: str) -> None:
        ...
    def CreateToolLengthComp(self, path_id: int, tool_comp_register: int, text: str) -> None:
        ...
    def CreateToolPreselect(self, path_id: int, tool_number: int, text: str) -> None:
        ...
    def CreateTrackingPointChange(self, path_id: int, tool_change_data: UF.UFPath.TrackingPointChange) -> None:
        ...
    def CreateWireAngle(self, path_id: int, slope_value: float, angle_value: float, angle_flag: bool, text: str) -> None:
        ...
    def CreateWireCutcom(self, path_id: int, cutcom_mode: UF.UFPath.CutcomMode, adjust_register: int, cutcom_off_flag: bool, adjust_flag: bool, text: str) -> None:
        ...
    def CreateWireGuides(self, path_id: int, text: str) -> None:
        ...
    def EndToolPath(self, path_id: int) -> None:
        ...
    def InitToolPath(self, path_id: int) -> None:
        ...


    class UFPathTrackingPointChange():
        xoff: float
        yoff: float
        adjust_register: int
        cutcom_register: int
    

    class UFPathToolChange():
        xoffset_value: float
        yoffset_value: float
        zoffset_value: float
        tool_angle: float
        radius: float
        tool_number: int
        adjust_register: int
        head_type: UF.UFPath.HeadType
        adjust_flag: bool
        tool_offset_flag: bool
        tool_number_flag: bool
        tool_angle_radius_flag: bool
        manual_change_flag: bool
    

    class TankType(enum.Enum):
        TankIn = 0
        TankOut = 1
        TankTypeLastElement = 2
    

    class UFPathSpindleOn():
        speed: float
        maxrpm: float
        range: str
        mode: UF.UFPath.SpindleMode
        direction: UF.UFPath.Direction
        speed_flag: bool
        maxrpm_flag: bool
        range_flag: bool
    

    class SpindleMode(enum.Enum):
        SpindleModeRpm = 0
        SpindleModeSfm = 1
        SpindleModeSmm = 2
        SpindleModeLastElement = 3
    

    class Side(enum.Enum):
        SideUndefined = 0
        SideRight = 1
        SideOn = 2
        SideLeft = 3
        SideLastElement = 4
    

    class Shape(enum.Enum):
        ShapeLinear = 0
        ShapeCircularCw = 1
        ShapeCircularCcw = 2
        ShapeHelicalCw = 5
        ShapeHelicalCcw = 6
        ShapeLastElement = 7
    

    class Seqno(enum.Enum):
        SeqnoN = 0
        SeqnoOff = 1
        SeqnoOn = 2
        SeqnoAuto = 3
        SeqnoLastElement = 4
    

    class RotationType(enum.Enum):
        RotationNone = 0
        RotationAngle = 1
        RotationAbsolute = 2
        RotationIncremental = 3
        RotationTypeLastElement = 4
    

    class RotationObject(enum.Enum):
        RotationObjectTable = 0
        RotationObjectHead = 1
        RotationObjectAaxis = 2
        RotationObjectBaxis = 3
        RotationObjectCaxis = 4
        RotationObjectLastElement = 5
    

    class UFPathRotate():
        rotation_angle: float
        rotation_object: UF.UFPath.RotationObject
        rotation_type: UF.UFPath.RotationType
        rotation_direction: UF.UFPath.Direction
        angle_flag: bool
        rotref_flag: bool
    

    class Pressure(enum.Enum):
        PressureNone = 0
        PressureLow = 1
        PressureMedium = 2
        PressureHigh = 3
        PressureRegister = 4
        PressureLastElement = 5
    

    class PlaneType(enum.Enum):
        PlaneTypeNone = 0
        PlaneTypeXy = 1
        PlaneTypeXz = 2
        PlaneTypeYz = 3
        PlaneTypeLastElement = 4
    

    class ParallelMode(enum.Enum):
        ParallelZaxis = 0
        ParallelWaxis = 1
        ParallelVaxis = 2
        ParallelModeNone = 3
        ParallelModeLastElement = 4
    

    class OutputMode(enum.Enum):
        OutputModeAbsolute = 0
        OutputModeIncremental = 1
        OutputModeNone = 2
        OutputModeLastElement = 3
    

    class OpSkip(enum.Enum):
        OpSkipOn = 0
        OpSkipOff = 1
        OpSkipLastElement = 2
    

    class MotionType(enum.Enum):
        MotionTypeUndefined = 0
        MotionTypeRapid = 1
        MotionTypeEngage = 2
        MotionTypeCut = 3
        MotionTypeRetract = 4
        MotionTypeFirstCut = 5
        MotionTypeApproach = 6
        MotionTypeStepover = 7
        MotionTypeDeparture = 8
        MotionTypeReturn = 9
        MotionTypeTraversal = 10
        MotionTypeThreadTurn = 11
        MotionTypeFrom = 12
        MotionTypeGohome = 13
        MotionTypeCycle = 14
        MotionTypeLastElement = 15
    

    class MachineMode(enum.Enum):
        MachineMill = 0
        MachineTurn = 1
        MachinePunch = 2
        MachineLaser = 3
        MachineTorch = 4
        MachineWire = 5
        MachineModeNone = 6
        MachineModeLastElement = 7
    

    class UFPathLinearMotion():
        position: float
        tool_axis: float
        feed_value: float
        feed_unit: UF.UFPath.FeedUnit
        type: UF.UFPath.MotionType
    

    class UFPathLevelMarker():
        tool_axis: float
        depth: float
    

    class UFPathHelicalMotion():
        start: float
        start_tool_axis: float
        end: float
        end_tool_axis: float
        arc_axis: float
        arc_center: float
        arc_radius: float
        tolerance: float
        times: float
        feed_value: float
        feed_unit: UF.UFPath.FeedUnit
        type: UF.UFPath.MotionType
        material_side: UF.UFPath.Side
        shape: UF.UFPath.Shape
    

    class HeadType(enum.Enum):
        HeadtypeNone = 0
        HeadtypeFront = 1
        HeadtypeRear = 2
        HeadtypeRight = 3
        HeadtypeLeft = 4
        HeadtypeSide = 5
        HeadtypeSaddle = 6
        HeadtypeLastElement = 7
    

    class Guide(enum.Enum):
        GuideNone = 0
        GuideUpper = 1
        GuideLower = 2
        GuideAll = 3
        GuideLastElement = 4
    

    class FlushType(enum.Enum):
        FlushOn = 0
        FlushOff = 1
        FlushTypeLastElement = 2
    

    class UFPathFlush():
        flush_type: UF.UFPath.FlushType
        flushing_guide: UF.UFPath.Guide
        flushing_pressure: UF.UFPath.Pressure
        flush_register: bool
        guide_flag: bool
        pressure_flag: bool
    

    class FeedUnit(enum.Enum):
        FeedUnitNone = 0
        FeedUnitPerMinute = 1
        FeedUnitPerRevolution = 2
        FeedUnitLastElement = 3
    

    class FeedrateMode(enum.Enum):
        FeedrateOutputOff = 0
        FeedrateOutputIpm = 1
        FeedrateOutputMmpm = 2
        FeedrateOutputIpr = 3
        FeedrateOutputMmpr = 4
        FeedrateOutputInvers = 5
        FeedrateOutputModeNone = 6
        FeedrateModeLastElement = 7
    

    class DwellUnit(enum.Enum):
        DwellSeconds = 0
        DwellRevolutions = 1
        DwellUnitLastElement = 2
    

    class Direction(enum.Enum):
        DirectionNone = 0
        DirectionClockwise = 1
        DirectionCounterClw = 2
        DirectionLastElement = 3
    

    class CutcomOn(enum.Enum):
        CutcomOnBeforeEngage = 0
        CutcomOnAfterEngage = 1
        CutcomOnBeforeMotion = 2
        CutcomOnLastElement = 3
    

    class CutcomOff(enum.Enum):
        CutcomOffBeforeRetract = 0
        CutcomOffAfterRetract = 1
        CutcomOffAfterMotion = 2
        CutcomOffLastElement = 3
    

    class CutcomMode(enum.Enum):
        CutcomOff = 0
        CutcomOn = 1
        CutcomLeft = 2
        CutcomRight = 3
        CutcomModeLastElement = 4
    

    class UFPathCutcom():
        cutcom_mode: UF.UFPath.CutcomMode
        plane_type: UF.UFPath.PlaneType
        cutcom_on_status: UF.UFPath.CutcomOn
        cutcom_off_status: UF.UFPath.CutcomOff
        adjust_register: int
        full_cutcom_output: bool
        adjust_flag: bool
    

    class CoolantType(enum.Enum):
        CoolantTypeOn = 0
        CoolantTypeMist = 1
        CoolantTypeFlood = 2
        CoolantTypeTap = 3
        CoolantTypeLastElement = 4
    

    class UFPathContactData():
        contact_pt: float
        contact_axis: float
        contact_arc_axis: float
        contact_arc_center: float
        contact_arc_radius: float
        contact_shape: UF.UFPath.Shape
    

    class ClampStatus(enum.Enum):
        ClampOn = 0
        ClampOff = 1
        ClampAxisOn = 2
        ClampAxisOff = 3
        ClampStatusLastElement = 4
    

    class UFPathCircularMotion():
        start: float
        start_tool_axis: float
        end: float
        end_tool_axis: float
        arc_axis: float
        arc_center: float
        arc_radius: float
        tolerance: float
        feed_value: float
        feed_unit: UF.UFPath.FeedUnit
        type: UF.UFPath.MotionType
        material_side: UF.UFPath.Side
        shape: UF.UFPath.Shape
    

    class Axis(enum.Enum):
        Xaxis = 0
        Yaxis = 1
        Zaxis = 2
        Aaxis = 3
        Baxis = 4
        Caxis = 5
        AxisNone = 6
        AxisLastElement = 7
    

    class ArcMode(enum.Enum):
        ArcLinear = 0
        ArcCircular = 1
        ArcModeNone = 2
        ArcModeLastElement = 3
    

class UFPart(Utilities.NXRemotableObject):
    def AddToRecentFileList(self, part_tag: Tag) -> None:
        ...
    def ApplyFamilyInstance(self, family: Tag, member_index: int) -> None:
        ...
    def AskCompressionFlags(self, part: Tag, compress_mask: UF.UFPart.CompressFlags) -> None:
        ...
    def AskCustomerArea(self, part_tag: Tag, customer_area: str) -> None:
        ...
    def AskDescription(self, part_tag: Tag, description: str) -> None:
        ...
    def AskDisplayPart(self) -> Tag:
        ...
    def AskEnforcePiecePart(self, part_tag: Tag, status: bool) -> None:
        ...
    def AskFamInstSaveDir(self, part_directory: str) -> None:
        ...
    def AskFamilies(self, part: Tag, family_count: int, families: typing.List[Tag]) -> None:
        ...
    def AskFamilyInstance(self, part: Tag, instance: Tag) -> None:
        ...
    def AskFamilySaveDir(self, family: Tag, dir: str) -> None:
        ...
    def AskJtInfoOfPart(self, part_tag: Tag, from_jt_file: bool, jt_file_exists: bool, contains_breps: bool) -> None:
        ...
    def AskLastModifiedVersion(self, part: Tag, modified_version: int) -> None:
        ...
    def AskMinorVersion(self, part: Tag, minor_version: int) -> None:
        ...
    def AskNthHistory(self, history_list: int, index: int, program: str, user: str, machine: str, version: int, gmtime: int) -> None:
        ...
    def AskNthPart(self, part_num: int) -> Tag:
        ...
    def AskNumHistories(self, history_list: int, number: int) -> None:
        ...
    def AskNumParts(self) -> int:
        ...
    def AskPartHistory(self, part: Tag, history_list: int) -> None:
        ...
    def AskPartHistoryWithRenameInfo(self, part: Tag, history_list: int) -> None:
        ...
    def AskPartName(self, part: Tag, part_fspec: str) -> None:
        ...
    def AskPartTag(self, part_name: str) -> Tag:
        ...
    def AskStatus(self, part_tag: Tag, status: int) -> None:
        ...
    def AskTagOfDispName(self, display_name: str, part_tag: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskTemplateFilename(self, part: Tag, template_name: str) -> None:
        ...
    def AskUnits(self, part: Tag, part_units: int) -> None:
        ...
    def CheckPartWritable(self, part_name: str, writable: bool) -> None:
        ...
    def Cleanup(self, option_mask: int) -> None:
        ...
    def ClearHistoryList(self, historiy_list: int) -> None:
        ...
    def Close(self, part: Tag, scope: int, mode: int) -> None:
        ...
    def CloseAll(self) -> None:
        ...
    def CloseCset(self, cset: Tag) -> None:
        ...
    def CreateFamilyInstance(self, family: Tag, member_index: int, part: Tag, instance: Tag) -> None:
        ...
    def CreateHistoryList(self, history_list: int) -> None:
        ...
    def EvaluateWriteState(self, part_tag: Tag) -> None:
        ...
    def Export(self, part_name: str, num_objects: int, object_array: typing.List[Tag]) -> None:
        ...
    def ExportWithOptions(self, part_name: str, num_objects: int, object_array: typing.List[Tag], options: UF.UFPart.ExportOptions) -> None:
        ...
    def FileNameForDisplay(self, name_format: str, display_name: str) -> None:
        ...
    def FileNameForDisplayString(self, name_format: str, display_name: str) -> None:
        ...
    def FindFamilyInstance(self, family: Tag, member_index: int, load: bool, use_load_options: bool, part_name: str) -> None:
        ...
    def FindTagOfDisplayName(self, display_name: str, part_tag: Tag) -> None:
        ...
    def FreeLoadStatus(self, load_status: UF.UFPart.LoadStatus) -> None:
        ...
    def Import(self, file_name: str, modes: UF.ImportPartModes, dest_csys: float, dest_point: float, scale: float, group: Tag) -> None:
        ...
    def ImportXtHidden(self, xtFileName: str, numBodies: int, bodyTags: typing.List[Tag]) -> None:
        ...
    def InheritStatusOfTemplate(self, member_tag: Tag) -> None:
        ...
    def IsFamilyInstCurrent(self, part: Tag, is_inst_current: bool) -> None:
        ...
    def IsFamilyInstance(self, part: Tag, is_family_instance: bool) -> None:
        ...
    def IsFamilyTemplate(self, part: Tag, is_family_template: bool) -> None:
        ...
    def IsLoaded(self, part_name: str) -> int:
        ...
    def IsModified(self, part: Tag) -> bool:
        ...
    def NameForDisplay(self, name_format: str, display_name: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def New(self, part_name: str, units: int, part: Tag) -> None:
        ...
    def Open(self, part_name: str, part: Tag, error_status: UF.UFPart.LoadStatus) -> None:
        ...
    def OpenComponentAs(self, component: Tag, old_name: str, new_name: str, part: Tag, error_status: UF.UFPart.LoadStatus) -> None:
        ...
    def OpenCset(self, cset: Tag, load_status: UF.UFPart.LoadStatus) -> None:
        ...
    def OpenQuiet(self, part_name: str, part: Tag, error_status: UF.UFPart.LoadStatus) -> None:
        ...
    def OpenSingleComponentAs(self, component: Tag, new_part_name: str, part: Tag, error_status: UF.UFPart.LoadStatus) -> None:
        ...
    def Rename(self, part_tag: Tag, new_part_name: str) -> None:
        ...
    def Reopen(self, part: Tag, scope: int, mode: int, new_part: Tag) -> None:
        ...
    def Save(self) -> None:
        ...
    def SaveAll(self, count: int, part_list: typing.List[Tag], error_list: int) -> None:
        ...
    def SaveAs(self, new_part_name: str) -> None:
        ...
    def SaveWorkOnly(self) -> None:
        ...
    def SetCompressionFlags(self, part: Tag, compress_mask: UF.UFPart.CompressFlags) -> None:
        ...
    def SetCustomerArea(self, part_tag: Tag, customer_area: str) -> None:
        ...
    def SetDescription(self, part_tag: Tag, description: str) -> None:
        ...
    def SetDisplayPart(self, part: Tag) -> None:
        ...
    def SetEnforcePiecePart(self, part_tag: Tag, status: bool) -> None:
        ...
    def SetFamInstSaveDir(self, part_directory: str) -> None:
        ...
    def SetFamilySaveDir(self, family: Tag, dir: str) -> None:
        ...
    def SetStatus(self, part_tag: Tag, status: int) -> None:
        ...
    def UpdateFamilyInstance(self, family: Tag, member_index: int, force_update: bool, part: Tag, saved: bool, count: int, part_list: typing.List[Tag], error_list: int, info: str) -> None:
        ...
    def UpdateJtBrep(self, part_tag: Tag) -> None:
        ...
    def UpdateJtFacets(self, part_tag: Tag) -> None:
        ...


    class UFPartLoadStatus():
        failed: bool
        user_abort: bool
        n_parts: int
        file_names: str
        statuses: int
    

    class ExportParamsMode(enum.Enum):
        MaintainParams = 0
        RemoveParams = 1
        MaintainAllParams = 2
    

    class UFPartExportOptions():
        new_part: bool
        params_mode: UF.UFPart.ExportParamsMode
        expression_mode: UF.UFPart.ExportExpMode
    

    class ExportExpMode(enum.Enum):
        CopyExpDeeply = 0
        CopyExpShallowly = 1
    

    class UFPartCompressFlags():
        standard: bool
    

class UFParam(Utilities.NXRemotableObject):
    def AppendUde(self, param: Tag, ude_set_type: UF.UdeSetType, ude_name: str, ud_obj: int) -> None:
        ...
    def Ask2dValue(self, param_tag: Tag, param_index: int, value: float) -> None:
        ...
    def Ask3dValue(self, param_tag: Tag, param_index: int, value: float) -> None:
        ...
    def AskDoubleValue(self, param_tag: Tag, param_index: int, value: float) -> None:
        ...
    def AskDoubleVla(self, param_tag: Tag, param_index: int, count: int, dbl_array: float) -> None:
        ...
    def AskInheritedParams(self, param_tag: Tag, count: int, indices: int) -> None:
        ...
    def AskIntValue(self, param_tag: Tag, param_index: int, value: int) -> None:
        ...
    def AskIntVla(self, param_tag: Tag, param_index: int, count: int, int_array: int) -> None:
        ...
    def AskLogicalValue(self, param_tag: Tag, param_index: int, value: bool) -> None:
        ...
    def AskParamAttributes(self, param_index: int, attributes: UF.UFParam.IndexAttribute) -> None:
        ...
    def AskParamDefiner(self, param_tag: Tag, param_index: int, definer_tag: Tag) -> None:
        ...
    def AskParamStatus(self, param_tag: Tag, param_index: int, status: UF.UFParam.Status) -> None:
        ...
    def AskRequiredParams(self, param_tag: Tag, count: int, indices: int) -> None:
        ...
    def AskStrValue(self, param_tag: Tag, param_index: int, value: str) -> None:
        ...
    def AskSubobjPtrValue(self, param_tag: Tag, param_index: int, value: int) -> None:
        ...
    def AskTagValue(self, param_tag: Tag, param_index: int, value: Tag) -> None:
        ...
    def AskTagVla(self, param_tag: Tag, param_index: int, count: int, tag_array: typing.List[Tag]) -> None:
        ...
    def AskUdes(self, param: Tag, ude_set_type: UF.UdeSetType, num_of_udes: int, ude_objs: int) -> None:
        ...
    def CanAcceptUde(self, param: Tag, ude_set_type: UF.UdeSetType, ude_name: str, response: bool) -> None:
        ...
    def CanAcceptUdeSet(self, param: Tag, ude_set_type: UF.UdeSetType, response: bool) -> None:
        ...
    def Check(self, param: Tag, is_ok: bool) -> None:
        ...
    def DeleteAllUdes(self, param: Tag, ude_set_type: UF.UdeSetType) -> None:
        ...
    def DeleteUde(self, param: Tag, ude_set_type: UF.UdeSetType, ude_obj: int) -> None:
        ...
    def Duplicate(self, old_obj_tag: Tag, name: str, new_obj_tag: Tag) -> None:
        ...
    def Generate(self, param_tag: Tag, generated: bool) -> None:
        ...
    def InheritValue(self, param_tag: Tag, param_index: int) -> None:
        ...
    def IsInherited(self, param_tag: Tag, param_index: int, answer: bool) -> None:
        ...
    def IsLoadWithParent(self, param: Tag, response: bool) -> None:
        ...
    def IsSameClass(self, obj1_tag: Tag, obj2_tag: Tag, answer: bool) -> None:
        ...
    def IsTemplate(self, param: Tag, response: bool) -> None:
        ...
    def Reinit(self, param_to_reinit: Tag, param_to_reinit_from: Tag) -> None:
        ...
    def Rename(self, param_tag: Tag, new_name: str) -> None:
        ...
    def ReplayPath(self, param_tag: Tag) -> None:
        ...
    def Set2dValue(self, param_tag: Tag, param_index: int, value: float) -> None:
        ...
    def Set3dValue(self, param_tag: Tag, param_index: int, value: float) -> None:
        ...
    def SetDoubleValue(self, param_tag: Tag, param_index: int, value: float) -> None:
        ...
    def SetDoubleVla(self, param_tag: Tag, param_index: int, count: int, dbl_array: float) -> None:
        ...
    def SetIntValue(self, param_tag: Tag, param_index: int, value: int) -> None:
        ...
    def SetIntVla(self, param_tag: Tag, param_index: int, count: int, int_array: int) -> None:
        ...
    def SetLogicalValue(self, param_tag: Tag, param_index: int, value: bool) -> None:
        ...
    def SetStrValue(self, param_tag: Tag, param_index: int, value: str) -> None:
        ...
    def SetSubobjPtrValue(self, param_tag: Tag, param_index: int, value: int) -> None:
        ...
    def SetTagValue(self, param_tag: Tag, param_index: int, value: Tag) -> None:
        ...
    def SetTagVla(self, param_tag: Tag, param_index: int, count: int, tag_array: typing.List[Tag]) -> None:
        ...


    class Type(enum.Enum):
        TypeLogical = 0
        TypeChar = 1
        TypeShort = 2
        TypeInt = 3
        TypePointer = 4
        TypeFloat = 5
        TypeDouble = 6
        TypeByte = 7
        TypeDate = 8
        TypeTag = 9
        TypeString = 10
        Type2d = 11
        Type3d = 12
        TypeVlaReal = 13
        TypeVlaInt = 14
        TypeVlaTag = 15
        TypeDoubleLength = 16
        Type2dLength = 17
        Type3dLength = 18
        TypeVlaLength = 19
        TypeVlaString = 20
        TypeObject = 21
        TypeVlaLengthComposite = 22
        TypeLast = 23
    

    class Status(enum.Enum):
        Default = 0
        Inherited = 1
        Overridden = 2
        InvalidIndex = 3
    

    class Regen(enum.Enum):
        RegenNone = 0
        RegenPost = 1
        RegenPath = 2
        RegenAll = 3
    

    class UFParamIndexAttribute():
        key: int
        name: str
        type: UF.UFParam.Type
        int_default: int
        dbl_default: float
        regen_flag: UF.UFParam.Regen
    

    class FeedUnit(enum.Enum):
        FeedNone = 0
        FeedPerMinute = 1
        FeedPerRevolution = 2
    

    class UFParamFeedrate():
        unit: UF.UFParam.FeedUnit
        value: float
        color: int
    

    class UFParamDispTool():
        type: int
        frequency: int
    

    class UFParamDispPath():
        silh_percent: float
        normx: float
        normy: float
        normz: float
        arrow: int
        number: int
        speed: int
        type: int
        feed: int
        norm_flag: int
    

class UFOprbnd(Utilities.NXRemotableObject):
    def AppendItemUde(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, set_type: UF.OprbndUdeSetType, ude_name: str, ude: int, response: bool) -> None:
        ...
    def AskBoundaryAppData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, app_data: UF.UFOprbnd.AppData) -> None:
        ...
    def AskItemAppData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, app_data: UF.UFOprbnd.AppData) -> None:
        ...
    def AskItemUdes(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, set_type: UF.OprbndUdeSetType, num_udes: int, udes: int) -> None:
        ...
    def CanAcceptItemUde(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, set_type: UF.OprbndUdeSetType, ude_name: str, response: bool) -> None:
        ...
    def DeleteAllItemUdes(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, set_type: UF.OprbndUdeSetType) -> None:
        ...
    def DeleteItemUde(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, set_type: UF.OprbndUdeSetType, ude: int) -> None:
        ...
    def SetBoundaryAppData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, app_data: UF.UFOprbnd.AppData) -> None:
        ...
    def SetItemAppData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, app_data: UF.UFOprbnd.AppData) -> None:
        ...


    class UFOprbndAppData():
        has_stock: int
        stock: float
        has_feedrate: int
        feedrate_unit: UF.CamFeedrateUnit
        feedrate_value: float
        has_tool_position: int
        tool_position: UF.CamToolPosition
    

class UFOper(Utilities.NXRemotableObject):
    def AskCutterGroup(self, oper: Tag, group: Tag) -> None:
        ...
    def AskGeomGroup(self, oper: Tag, group: Tag) -> None:
        ...
    def AskMachiningMode(self, oper: Tag, mode: UF.UFOper.MachMode) -> None:
        ...
    def AskMethodGroup(self, oper: Tag, group: Tag) -> None:
        ...
    def AskName(self, oper_id: int, op_name: str) -> None:
        ...
    def AskNameFromTag(self, oper: Tag, name: str) -> None:
        ...
    def AskOper(self, exit_id: int, oper_id: int) -> None:
        ...
    def AskOperType(self, oper: Tag, type: int) -> None:
        ...
    def AskPath(self, oper_id: int, path_id: int) -> None:
        ...
    def AskProgramGroup(self, oper: Tag, group: Tag) -> None:
        ...
    def AskRefCutter(self, oper_tag: Tag, ref_cutter_tag: Tag) -> None:
        ...
    def AskSelectedPointData(self, object_tag: Tag, index: int, data: UF.UFCutter.TrackingPointData) -> None:
        ...
    def AskSelectedTrackingPointCount(self, object_tag: Tag, count: int) -> None:
        ...
    def AskSelectedTurnPointData(self, object_tag: Tag, index: int, data: UF.UFCutter.TurnTrackingPointData) -> None:
        ...
    def AskStatus(self, oper: Tag, status: UF.UFOper.Status) -> None:
        ...
    def AskStatus1(self, oper: Tag, status: UF.UFOper.Status1) -> None:
        ...
    def Create(self, type_name: str, subtype_name: str, new_object: Tag) -> None:
        ...
    def DeleteToolPath(self, oper: Tag) -> None:
        ...
    def DeselectTrackingPoint(self, object_tag: Tag, name: str) -> None:
        ...
    def HasSelfIpw(self, oper: Tag, result: bool) -> None:
        ...
    def IsPathGouged(self, oper: Tag, result: bool) -> None:
        ...
    def ResetFromTable(self, oper_tag: Tag) -> None:
        ...
    def SelectTrackingPoint(self, object_tag: Tag, name: str) -> None:
        ...
    def SetMachiningData(self, oper_tag: Tag) -> None:
        ...
    def SetRefCutter(self, oper_tag: Tag, ref_cutter_tag: Tag) -> None:
        ...
    def UnloadPath(self, oper_tag: Tag) -> None:
        ...


    class UFOperStatus1():
        is_edited: int
        toolpath_exists: int
        toolpath_edited: int
    

    class UFOperStatus():
        is_edited: int
        toolpath_exists: int
        toolpath_edited: int
        open: int
    

    class MachMode(enum.Enum):
        MachModeUndef = 0
        MachModeMill = 1
        MachModeLathe = 2
        MachModeDrill = 3
        MachModeWedm = 4
        MachModeTurn = 5
        MachModeLast = 6
    

class UFObj(Utilities.NXRemotableObject):
    def AskCreModVersions(self, _object: Tag, creation_version: int, lastmod_version: int) -> None:
        ...
    def AskCreSettings(self, type: int, subtype: int, property: int, settings: UF.UFObj.CreSettings) -> None:
        ...
    def AskDefCreSettings(self, settings: UF.UFObj.CreSettings) -> None:
        ...
    def AskDisplayProperties(self, object_id: Tag, disp_props: UF.UFObj.DispProps) -> None:
        ...
    def AskExtendedTypeAndSubtype(self, object_id: Tag, type: int, subtype: int) -> None:
        ...
    def AskFaceAnalysis(self, face: Tag, srfanl: bool) -> None:
        ...
    def AskName(self, object_id: Tag, name: str) -> None:
        ...
    def AskNameOrigin(self, object_id: Tag, origin: float) -> None:
        ...
    def AskOwningPart(self, object_in_part: Tag, part_tag: Tag) -> None:
        ...
    def AskPartiallyShaded(self, _object: Tag, shaded: bool) -> None:
        ...
    def AskStatus(self, _object: Tag) -> int:
        ...
    def AskTranslucency(self, _object: Tag, translucency: int) -> None:
        ...
    def AskTypeAndSubtype(self, object_id: Tag, type: int, subtype: int) -> None:
        ...
    def CanTypeHaveMatrix(self, object_type: int) -> bool:
        """[Obsolete("Deprecated")"""
        ...
    def CycleAll(self, part_tag: Tag, _object: Tag) -> Tag:
        ...
    def CycleByName(self, name: str, _object: Tag) -> None:
        ...
    def CycleByNameAndType(self, part_tag: Tag, name: str, type: int, use_occ: bool, _object: Tag) -> None:
        ...
    def CycleByNameAndTypeExtended(self, part_tag: Tag, name: str, type: int, use_occ: bool, _object: Tag) -> None:
        ...
    def CycleObjsInPart(self, part_tag: Tag, type: int, _object: Tag) -> None:
        ...
    def CycleObjsInPart1(self, part_tag: Tag, type: int, _object: Tag) -> None:
        ...
    def CycleTypedObjsInPart(self, part_tag: Tag, type: int, _object: Tag) -> None:
        ...
    def DeleteName(self, object_id: Tag) -> None:
        ...
    def DeleteObject(self, object_id: Tag) -> None:
        ...
    def IsDefCreColor(self, type: int, subtype: int, property: int, is_default: bool) -> None:
        ...
    def IsDefCreLineFont(self, type: int, subtype: int, property: int, is_default: bool) -> None:
        ...
    def IsDefCreWidth(self, type: int, subtype: int, property: int, is_default: bool) -> None:
        ...
    def IsDisplayable(self, object_id: Tag, is_displayable: bool) -> None:
        ...
    def IsObjectAPromotion(self, _object: Tag) -> bool:
        ...
    def IsTransferable(self, object_id: Tag, is_transferable: bool) -> None:
        ...
    def IsTypeDisplayable(self, object_type: int) -> bool:
        """[Obsolete("Deprecated")"""
        ...
    def IsTypeTransferable(self, object_type: int, is_transferable: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def ModifyDefaults(self, default_color: int, default_layer: int, default_width: int, default_font: int) -> None:
        ...
    def ReplaceObjectArrayData(self, num_objects: int, target_objects: typing.List[Tag], source_objects: typing.List[Tag]) -> None:
        ...
    def ReplaceObjectData(self, orig_obj: Tag, new_obj: Tag) -> None:
        ...
    def ResetDefaults(self, default_color: int, default_layer: int, default_width: int, default_font: int) -> None:
        ...
    def ReturnPrevDefaults(self) -> None:
        ...
    def ReverseBlankAll(self) -> None:
        ...
    def SetBlankStatus(self, object_id: Tag, blank_status: int) -> None:
        ...
    def SetColor(self, object_id: Tag, color: int) -> None:
        ...
    def SetCreColor(self, type: int, subtype: int, property: int, color: int) -> None:
        ...
    def SetCreColorToDef(self, type: int, subtype: int, property: int) -> None:
        ...
    def SetCreLineFont(self, type: int, subtype: int, property: int, line_font: int) -> None:
        ...
    def SetCreLineFontToDef(self, type: int, subtype: int, property: int) -> None:
        ...
    def SetCreWidth(self, type: int, subtype: int, property: int, width: int) -> None:
        ...
    def SetCreWidthToDef(self, type: int, subtype: int, property: int) -> None:
        ...
    def SetDefCreColor(self, color: int) -> None:
        ...
    def SetDefCreLineFont(self, line_font: int) -> None:
        ...
    def SetDefCreWidth(self, width: int) -> None:
        ...
    def SetFaceAnalysis(self, face: Tag, srfanl: bool) -> None:
        ...
    def SetFont(self, object_id: Tag, font: int) -> None:
        ...
    def SetLayer(self, object_id: Tag, layer: int) -> None:
        ...
    def SetLayerAllowHidden(self, object_id: Tag, layer: int) -> None:
        ...
    def SetLineWidth(self, object_id: Tag, line_width: int) -> None:
        ...
    def SetName(self, object_id: Tag, name: str) -> None:
        ...
    def SetNameOrigin(self, object_id: Tag, origin: float) -> None:
        ...
    def SetPartiallyShaded(self, _object: Tag, shaded: bool) -> None:
        ...
    def SetTranslucency(self, _object: Tag, translucency: int) -> None:
        ...


    class UFObjDispProps():
        layer: int
        color: int
        blank_status: int
        line_width: int
        font: int
        highlight_status: bool
    

    class UFObjCreSettings():
        color: int
        line_font: int
        width: int
    



class UFNcprog(Utilities.NXRemotableObject):
    def Create(self, type_name: str, subtype_name: str, new_object: Tag) -> None:
        ...


class UFNcmthd(Utilities.NXRemotableObject):
    def Create(self, type_name: str, subtype_name: str, new_object: Tag) -> None:
        ...


class UFNcgroup(Utilities.NXRemotableObject):
    def AcceptMember(self, parent: Tag, member: Tag) -> None:
        ...
    def AskMemberInList(self, parent: Tag, index: int, member: Tag) -> None:
        ...
    def AskMemberList(self, obj_tag: Tag, count: int, list: typing.List[Tag]) -> None:
        ...
    def AskObjectOfName(self, obj_tag: Tag, name: str, obj_with_name: Tag) -> None:
        ...
    def AskRootOfObject(self, obj_tag: Tag, root_tag: Tag) -> None:
        ...
    def CanAcceptMember(self, obj1: Tag, obj2: Tag, answer: bool, reason: str) -> None:
        ...
    def CycleMembers(self, group: Tag, cb: UF.UFNcgroup.CycleCbFT, data: int) -> None:
        ...
    def InsertMember(self, parent: Tag, member: Tag, sibling: Tag, where: UF.UFNcgroup.Position) -> None:
        ...
    def IsAMember(self, group: Tag, member: Tag, answer: bool, index: int) -> None:
        ...
    def IsGroup(self, obj_tag: Tag, answer: bool) -> None:
        ...


    class Position(enum.Enum):
        PositionBefore = 0
        PositionAfter = 1
    

    

class UFNcgeom(Utilities.NXRemotableObject):
    def Create(self, type_name: str, subtype_name: str, new_object: Tag) -> None:
        ...


class UFMtx4(Utilities.NXRemotableObject):
    def AskRotation(self, mtx_4D: float, mtx_3D: float) -> None:
        ...
    def AskScale(self, mtx: float, scale: float) -> None:
        ...
    def AskTranslation(self, mtx: float, translate_vec: float) -> None:
        ...
    def Copy(self, mtx_src: float, mtx_dst: float) -> None:
        ...
    def CsysToCsys(self, from_origin: float, from_x_axis: float, from_y_axis: float, to_origin: float, to_x_axis: float, to_y_axis: float, mtx: float) -> None:
        ...
    def EditRotation(self, mtx_4D: float, mtx_3D: float) -> None:
        ...
    def EditScale(self, mtx: float, scale: float) -> None:
        ...
    def EditTranslation(self, mtx: float, translate_vec: float) -> None:
        ...
    def Identity(self, identity_mtx: float) -> None:
        ...
    def Initialize(self, scale: float, translation_vec: float, mtx_3D: float, mtx_4D: float) -> None:
        ...
    def Invert(self, mtx_in: float, mtx_out: float) -> None:
        ...
    def Mirror(self, origin: float, normal: float, mtx: float) -> None:
        ...
    def Multiply(self, mtx1: float, mtx2: float, mtx_product: float) -> None:
        ...
    def MultiplyT(self, mtx1: float, mtx2: float, mtx_product: float) -> None:
        ...
    def OrthoNormalize(self, mtx: float) -> None:
        ...
    def Rotation(self, rotation_point: float, rotation_axis: float, angle: float, mtx: float) -> None:
        ...
    def Scaling(self, invariant_point: float, scale: float, mtx: float) -> None:
        ...
    def Transpose(self, mtx: float, transpose_mtx: float) -> None:
        ...
    def Vec3Multiply(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def Vec3MultiplyT(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def VecMultiply(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def VecMultiplyT(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def XVec(self, mtx: float, x_vec: float) -> None:
        ...
    def YVec(self, mtx: float, y_vec: float) -> None:
        ...
    def ZVec(self, mtx: float, z_vec: float) -> None:
        ...


class UFMtx3(Utilities.NXRemotableObject):
    def Copy(self, mtx_src: float, mtx_dst: float) -> None:
        ...
    def Determinant(self, mtx: float, determinant: float) -> None:
        ...
    def Identity(self, identity_mtx: float) -> None:
        ...
    def Initialize(self, x_vec: float, y_vec: float, mtx: float) -> None:
        ...
    def InitializeX(self, x_vec: float, mtx: float) -> None:
        ...
    def InitializeZ(self, z_vec: float, mtx: float) -> None:
        ...
    def Mtx4(self, mtx_3D: float, mtx_4D: float) -> None:
        ...
    def Multiply(self, mtx1: float, mtx2: float, mtx_product: float) -> None:
        ...
    def MultiplyT(self, mtx1: float, mtx2: float, mtx_product: float) -> None:
        ...
    def OrthoNormalize(self, mtx: float) -> None:
        ...
    def RotateAboutAxis(self, rotation_axis: float, rotation_angle: float, mtx: float) -> None:
        ...
    def Transpose(self, mtx: float, transpose_mtx: float) -> None:
        ...
    def VecMultiply(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def VecMultiplyT(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def XVec(self, mtx: float, x_vec: float) -> None:
        ...
    def YVec(self, mtx: float, y_vec: float) -> None:
        ...
    def ZVec(self, mtx: float, z_vec: float) -> None:
        ...


class UFMtx2(Utilities.NXRemotableObject):
    def Copy(self, mtx_src: float, mtx_dst: float) -> None:
        ...
    def Determinant(self, mtx: float, determinant: float) -> None:
        ...
    def Identity(self, identity_mtx: float) -> None:
        ...
    def Initialize(self, x_vec: float, y_vec: float, mtx: float) -> None:
        ...
    def Multiply(self, mtx1: float, mtx2: float, mtx_product: float) -> None:
        ...
    def MultiplyT(self, mtx1: float, mtx2: float, mtx_product: float) -> None:
        ...
    def Transpose(self, mtx: float, transpose_mtx: float) -> None:
        ...
    def VecMultiply(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def VecMultiplyT(self, vec: float, mtx: float, vec_product: float) -> None:
        ...
    def XVec(self, mtx: float, x_vec: float) -> None:
        ...
    def YVec(self, mtx: float, y_vec: float) -> None:
        ...


class UFMsao(Utilities.NXRemotableObject):
    def AskFace(self, msao: Tag, index: int, face: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...


class UFMotion(Utilities.NXRemotableObject):
    def AnimationRun(self) -> None:
        ...
    def ArticulationRun(self) -> None:
        ...
    def Ask2dContact(self, contact_tag: Tag, contact_struct: UF.UFMotion._2D_contact_) -> None:
        ...
    def Ask3dContact(self, contact_tag: Tag, contact_struct: UF.UFMotion._3D_contact_) -> None:
        ...
    def Ask3dContactMethod(self, contact_method: UF.UFMotion._3d_contact_method_, facet_contact_tolerance: int) -> None:
        ...
    def AskAccelerationResults(self, motion_object: Tag, type: UF.MotnMotionType, component: UF.UFMotion.VectorComponent, ref_frame: UF.UFMotion.ReferenceFrame, number_of_results: int, results: float) -> None:
        ...
    def AskActiveSolution(self, active_solution: Tag) -> None:
        ...
    def AskAngularUnits(self, angle_units: UF.UFMotion.AngularUnitsType) -> None:
        ...
    def AskArticStepSize(self, joint_tag: Tag, step_size: float) -> None:
        ...
    def AskArticulationStopTolerance(self, stop_tolerance: float) -> None:
        ...
    def AskAttachmentsOfType(self, entity_tag: Tag, type: int, subtype: int, num_attachments: int, attachments: typing.List[Tag]) -> None:
        ...
    def AskCrvCrvConstraint(self, crv_crv_tag: Tag, crv_crv_struct: UF.UFMotion.CurveCurveConstraint) -> None:
        ...
    def AskCylindricalBushing(self, bushing_tag: Tag, bushing_struct: UF.UFMotion.CylindricalBushing) -> None:
        ...
    def AskDamper(self, damper_tag: Tag, damper_struct: UF.UFMotion.SpringDamper) -> None:
        ...
    def AskForceResults(self, motion_object: Tag, component: UF.UFMotion.VectorComponent, ref_frame: UF.UFMotion.ReferenceFrame, number_of_results: int, results: float) -> None:
        ...
    def AskFunction(self, function_tag: Tag, function_struct: UF.UFMotion.Function) -> None:
        ...
    def AskFunctionTagFromName(self, function_name: str, function_tag: Tag) -> None:
        ...
    def AskGeneralBushing(self, bushing_tag: Tag, bushing_struct: UF.UFMotion.GeneralBushing) -> None:
        ...
    def AskGravitationalConstants(self, gravitational_constants: float) -> None:
        ...
    def AskGrueblerCount(self, gruebler_count: int) -> None:
        ...
    def AskIconScaleFactor(self, scale: float) -> None:
        ...
    def AskInterference(self, interfere_tag: Tag, interference_struct: UF.UFMotion.InterferenceStruct) -> None:
        ...
    def AskJoint(self, joint_tag: Tag, joint_struct: UF.UFMotion.Joint) -> None:
        ...
    def AskJointCoupler(self, joint_coupler_tag: Tag, coupler_struct: UF.UFMotion.JointCoupler) -> None:
        ...
    def AskJointLimits(self, joint_tag: Tag, joint_limits_struct: UF.UFMotion.JointLimits) -> None:
        ...
    def AskJointMotionInput(self, joint_tag: Tag, motion_input_struct: UF.UFMotion.JointMotionInput) -> None:
        ...
    def AskLink(self, link_tag: Tag, link_struct: UF.UFMotion.Link) -> None:
        ...
    def AskLinkInitialVelocity(self, link_tag: Tag, init_vel_struct: UF.UFMotion.LinkInitialVel) -> None:
        ...
    def AskLinkMassProperties(self, link_tag: Tag, mass_prop_struct: UF.UFMotion.LinkMassProperties) -> None:
        ...
    def AskLinkTransfromForGivenFrame(self, linkTag: Tag, frame: int, transformMatrix: float) -> None:
        ...
    def AskMarker(self, marker_tag: Tag, marker_struct: UF.UFMotion.Marker) -> None:
        ...
    def AskMeasurement(self, meas_tag: Tag, meas_struct: UF.UFMotion.Measurement) -> None:
        ...
    def AskNameDisplay(self, name_display: bool) -> None:
        ...
    def AskNumberOfAnimationFrames(self, numFrames: int) -> None:
        ...
    def AskPointOnSurfaceConstraint(self, point_on_surface_tag: Tag, pt_on_surf_data: UF.UFMotion.PointOnSurfaceData) -> None:
        ...
    def AskPtCrvConstraint(self, pt_crv_tag: Tag, pt_crv_struct: UF.UFMotion.PointCurveConstraint) -> None:
        ...
    def AskRotDisplacementResults(self, motion_object: Tag, component: UF.UFMotion.DispAngle, ref_frame: UF.UFMotion.ReferenceFrame, number_of_results: int, results: float) -> None:
        ...
    def AskScalarForce(self, force_tag: Tag, force_struct: UF.UFMotion.ScalarForceTorque) -> None:
        ...
    def AskScalarTorque(self, torque_tag: Tag, torque_struct: UF.UFMotion.ScalarForceTorque) -> None:
        ...
    def AskSolverDofCount(self, dof_count: int) -> None:
        ...
    def AskSolverParameters(self, solver_params_struct: UF.UFMotion.SolverParameters) -> None:
        ...
    def AskSpring(self, spring_tag: Tag, spring_struct: UF.UFMotion.SpringDamper) -> None:
        ...
    def AskTorqueResults(self, motion_object: Tag, component: UF.UFMotion.VectorComponent, ref_frame: UF.UFMotion.ReferenceFrame, number_of_results: int, results: float) -> None:
        ...
    def AskTrace(self, trace_tag: Tag, trace_struct: UF.UFMotion.TraceStruct) -> None:
        ...
    def AskTraceExplosionToMaster(self, to_master: bool) -> None:
        ...
    def AskTransDisplacementResults(self, motion_object: Tag, component: UF.UFMotion.VectorComponent, ref_frame: UF.UFMotion.ReferenceFrame, number_of_results: int, results: float) -> None:
        ...
    def AskVectorForceTorque(self, vobject_tag: Tag, vector_struct: UF.UFMotion.VectorForceTorque) -> None:
        ...
    def AskVelocityResults(self, motion_object: Tag, type: UF.MotnMotionType, component: UF.UFMotion.VectorComponent, ref_frame: UF.UFMotion.ReferenceFrame, number_of_results: int, results: float) -> None:
        ...
    def CalculateStaticEquilibrium(self, static_result_steps: int) -> None:
        ...
    def Create2dContact(self, contact_struct: UF.UFMotion._2D_contact_, contact_tag: Tag) -> None:
        ...
    def Create3dContact(self, contact_struct: UF.UFMotion._3D_contact_, contact_tag: Tag) -> None:
        ...
    def CreateCrvCrvConstraint(self, crv_crv_data: UF.UFMotion.CurveCurveConstraint, crv_crv_tag: Tag) -> None:
        ...
    def CreateCylindricalBushing(self, bushing_struct: UF.UFMotion.CylindricalBushing, bushing_tag: Tag) -> None:
        ...
    def CreateDamper(self, damper_struct: UF.UFMotion.SpringDamper, damper_tag: Tag) -> None:
        ...
    def CreateFunction(self, function_struct: UF.UFMotion.Function, function_tag: Tag) -> None:
        ...
    def CreateGeneralBushing(self, bushing_struct: UF.UFMotion.GeneralBushing, bushing_tag: Tag) -> None:
        ...
    def CreateInterference(self, interfere_struct: UF.UFMotion.InterferenceStruct, interference_tag: Tag) -> None:
        ...
    def CreateInterferenceBody(self, interference_tag: Tag, analysis_step_num: int, frame: UF.UFMotion.ReferenceFrame, num_interference_bodies: int, interference_body_tags: typing.List[Tag]) -> None:
        ...
    def CreateJoint(self, joint_struct: UF.UFMotion.Joint, joint_tag: Tag) -> None:
        ...
    def CreateJointCoupler(self, coupler_struct: UF.UFMotion.JointCoupler, joint_coupler_tag: Tag) -> None:
        ...
    def CreateLink(self, link_struct: UF.UFMotion.Link, link_tag: Tag) -> None:
        ...
    def CreateMarker(self, marker_struct: UF.UFMotion.Marker, marker_tag: Tag) -> None:
        ...
    def CreateMeasurement(self, meas_struct: UF.UFMotion.Measurement, meas_tag: Tag) -> None:
        ...
    def CreatePointOnSurfaceConstraint(self, pt_on_surf_data: UF.UFMotion.PointOnSurfaceData, point_on_surface_tag: Tag) -> None:
        ...
    def CreatePtCrvConstraint(self, pt_crv_data: UF.UFMotion.PointCurveConstraint, pt_crv_tag: Tag) -> None:
        ...
    def CreateScalarForce(self, force_struct: UF.UFMotion.ScalarForceTorque, force_tag: Tag) -> None:
        ...
    def CreateScalarTorque(self, torque_struct: UF.UFMotion.ScalarForceTorque, torque_tag: Tag) -> None:
        ...
    def CreateSpring(self, spring_struct: UF.UFMotion.SpringDamper, spring_tag: Tag) -> None:
        ...
    def CreateTrace(self, trace_struct: UF.UFMotion.TraceStruct, trace_tag: Tag) -> None:
        ...
    def CreateVectorForceTorque(self, vector_struct: UF.UFMotion.VectorForceTorque, vobject_tag: Tag) -> None:
        ...
    def DeleteFunction(self, function_tag: Tag) -> None:
        ...
    def DeleteInterference(self, interfere_tag: Tag) -> None:
        ...
    def DeleteMeasurement(self, meas_tag: Tag) -> None:
        ...
    def DeleteTrace(self, trace_tag: Tag) -> None:
        ...
    def EditArticStepSize(self, joint_tag: Tag, step_size: float) -> None:
        ...
    def EditInterference(self, interfere_tag: Tag, interfere_struct: UF.UFMotion.InterferenceStruct) -> None:
        ...
    def EditMeasurement(self, meas_tag: Tag, meas_struct: UF.UFMotion.Measurement) -> None:
        ...
    def EditSolverParameters(self, solver_params: UF.UFMotion.SolverParameters) -> None:
        ...
    def EditTrace(self, trace_tag: Tag, trace_struct: UF.UFMotion.TraceStruct) -> None:
        ...
    def ExportAdamsAnlFile(self, file_name: str, geometry_format: UF.UFMotion.AnlGeometryFormat, stl_params: UF.UFMotion.StlParameters) -> None:
        ...
    def ExportAdamsResFile(self, file_name: str) -> None:
        ...
    def ExportToProductVision(self, full_file_name: str, export_option: UF.MotionPvExportType) -> None:
        ...
    def FileSuppressWarnings(self, flag: bool) -> None:
        ...
    def FindAllFunctions(self, function_tags: typing.List[Tag], num_functions: int) -> None:
        ...
    def GetObjectDerivedFunction(self, motion_obj_tag: Tag, func_type: UF.UFMotion.FuncResultType, func_comp: UF.UFMotion.FuncComponentType, ref_frame: UF.UFMotion.FuncRefFrameType, derived_func_string: str) -> None:
        ...
    def Init2dContactStruct(self, contact_struct: UF.UFMotion._2D_contact_) -> None:
        ...
    def Init3dContactStruct(self, contact_struct: UF.UFMotion._3D_contact_) -> None:
        ...
    def InitArticulation(self) -> None:
        ...
    def InitCrvCrvStruct(self, crv_crv_struct: UF.UFMotion.CurveCurveConstraint) -> None:
        ...
    def InitCylindricalBushingStruct(self, bushing_struct: UF.UFMotion.CylindricalBushing) -> None:
        ...
    def InitFunctionStruct(self, function_struct: UF.UFMotion.Function) -> None:
        ...
    def InitGeneralBushingStruct(self, bushing_struct: UF.UFMotion.GeneralBushing) -> None:
        ...
    def InitInterferenceStruct(self, interference_struct: UF.UFMotion.InterferenceStruct) -> None:
        ...
    def InitJointCouplerStruct(self, coupler_struct: UF.UFMotion.JointCoupler) -> None:
        ...
    def InitJointLimitsStruct(self, joint_limits_struct: UF.UFMotion.JointLimits) -> None:
        ...
    def InitJointMotionInputStruct(self, motion_input_struct: UF.UFMotion.JointMotionInput) -> None:
        ...
    def InitJointStruct(self, joint_struct: UF.UFMotion.Joint) -> None:
        ...
    def InitLinkMassStruct(self, link_mass_struct: UF.UFMotion.LinkMassProperties) -> None:
        ...
    def InitLinkStruct(self, link_struct: UF.UFMotion.Link) -> None:
        ...
    def InitLinkVelocityStruct(self, link_velocity_struct: UF.UFMotion.LinkInitialVel) -> None:
        ...
    def InitMarkerStruct(self, marker_struct: UF.UFMotion.Marker) -> None:
        ...
    def InitMeasurementStruct(self, measurement_struct: UF.UFMotion.Measurement) -> None:
        ...
    def InitPointOnSurfaceConstraint(self, point_on_surf_data: UF.UFMotion.PointOnSurfaceData) -> None:
        ...
    def InitPtCrvStruct(self, pt_crv_struct: UF.UFMotion.PointCurveConstraint) -> None:
        ...
    def InitScalarForceTorqueStruct(self, scalar_struct: UF.UFMotion.ScalarForceTorque) -> None:
        ...
    def InitSolverParametersStruct(self, solver_params_struct: UF.UFMotion.SolverParameters) -> None:
        ...
    def InitSpringDamperStruct(self, spring_damper_struct: UF.UFMotion.SpringDamper) -> None:
        ...
    def InitStlParametersStruct(self, stl_params: UF.UFMotion.StlParameters) -> None:
        ...
    def InitTraceStruct(self, trace_struct: UF.UFMotion.TraceStruct) -> None:
        ...
    def InitVectorForceTorqueStruct(self, vector_struct: UF.UFMotion.VectorForceTorque) -> None:
        ...
    def Initialize(self) -> None:
        ...
    def Interference(self, interference_tag: Tag, step_num: int, interference_result: int) -> None:
        ...
    def IsInitialized(self, true_false: bool) -> None:
        ...
    def ListConnections(self, output_file_with_path: str) -> None:
        ...
    def Measure(self, measurement_tag: Tag, animation_step: int, measurement: float) -> None:
        ...
    def RemoveJointLimits(self, joint_tag: Tag) -> None:
        ...
    def RemoveJointMotionInput(self, joint_tag: Tag) -> None:
        ...
    def RemoveLinkInitialVelocity(self, link_tag: Tag) -> None:
        ...
    def RemoveLinkMassProperties(self, link_tag: Tag) -> None:
        ...
    def ReviewAdamsResFile(self, res_file: str) -> None:
        ...
    def ReviewResultFile(self, res_file: str) -> None:
        ...
    def Set2dContact(self, contact_tag: Tag, contact_struct: UF.UFMotion._2D_contact_) -> None:
        ...
    def Set3dContact(self, contact_tag: Tag, contact_struct: UF.UFMotion._3D_contact_) -> None:
        ...
    def Set3dContactMethod(self, contact_method: UF.UFMotion._3d_contact_method_, facet_contact_tolerance: int) -> None:
        ...
    def SetActiveSolution(self, active_solution: Tag) -> None:
        ...
    def SetAngularUnits(self, angle_units: UF.UFMotion.AngularUnitsType) -> None:
        ...
    def SetArticulationStopTolerance(self, stop_tolerance: float) -> None:
        ...
    def SetCylindricalBushing(self, bushing_tag: Tag, bushing_struct: UF.UFMotion.CylindricalBushing) -> None:
        ...
    def SetDamper(self, damper_tag: Tag, damper_struct: UF.UFMotion.SpringDamper) -> None:
        ...
    def SetFunction(self, function_tag: Tag, function_struct: UF.UFMotion.Function) -> None:
        ...
    def SetGeneralBushing(self, bushing_tag: Tag, bushing_struct: UF.UFMotion.GeneralBushing) -> None:
        ...
    def SetGravitationalConstants(self, gravitational_constants: float) -> None:
        ...
    def SetIconScaleFactor(self, scale: float) -> None:
        ...
    def SetJoint(self, joint_tag: Tag, joint_struct: UF.UFMotion.Joint) -> None:
        ...
    def SetJointCoupler(self, joint_coupler_tag: Tag, coupler_struct: UF.UFMotion.JointCoupler) -> None:
        ...
    def SetJointLimits(self, joint_tag: Tag, joint_limits_struct: UF.UFMotion.JointLimits) -> None:
        ...
    def SetJointMotionInput(self, joint_tag: Tag, input_struct: UF.UFMotion.JointMotionInput) -> None:
        ...
    def SetLink(self, link_tag: Tag, link_struct: UF.UFMotion.Link) -> None:
        ...
    def SetLinkInitialVelocity(self, link_tag: Tag, init_vel_struct: UF.UFMotion.LinkInitialVel) -> None:
        ...
    def SetLinkMassProperties(self, link_tag: Tag, mass_prop_struct: UF.UFMotion.LinkMassProperties) -> None:
        ...
    def SetLinkTransform(self, linkTag: Tag, transformMatrix: float) -> None:
        ...
    def SetMarker(self, marker_tag: Tag, marker_struct: UF.UFMotion.Marker) -> None:
        ...
    def SetNameDisplay(self, name_display: bool) -> None:
        ...
    def SetPointOnSurfaceConstraint(self, point_on_surface_tag: Tag, pt_on_surf_data: UF.UFMotion.PointOnSurfaceData) -> None:
        ...
    def SetPtCrvConstraint(self, pt_crv_tag: Tag, pt_crv_data: UF.UFMotion.PointCurveConstraint) -> None:
        ...
    def SetScalarForce(self, force_tag: Tag, force_struct: UF.UFMotion.ScalarForceTorque) -> None:
        ...
    def SetScalarTorque(self, torque_tag: Tag, torque_struct: UF.UFMotion.ScalarForceTorque) -> None:
        ...
    def SetSpring(self, spring_tag: Tag, spring_struct: UF.UFMotion.SpringDamper) -> None:
        ...
    def SetTraceExplosionToMaster(self, to_master: bool) -> None:
        ...
    def SetVectorForceTorque(self, vobject_tag: Tag, vector_struct: UF.UFMotion.VectorForceTorque) -> None:
        ...
    def SolveModel(self, time: float, num_steps: int) -> None:
        ...
    def SpreadsheetRunFromFile(self, spreadsheet_file: str, start_step: int, end_step: int, invoke_ui: bool) -> None:
        ...
    def StepArticulation(self, num_steps: int, total_steps: int) -> None:
        ...
    def Terminate(self) -> None:
        ...
    def TerminateArticulation(self) -> None:
        ...
    def Trace(self, trace_tag: Tag, step_number: int, new_object_tag: Tag) -> None:
        ...
    def TraceModel(self, step_num: int, target_layer: int, num_tags: int, geom_tags: typing.List[Tag]) -> None:
        ...
    def ValidateFunctionSyntax(self, function_string: str, num_lines: int) -> None:
        ...
    def WriteObjectInfo(self, num_objects: int, object_tags: typing.List[Tag], info_file_name: str) -> None:
        ...


    class VectorType(enum.Enum):
        VectorForce = 0
        VectorTorque = 1
    

    class UFMotionVectorForceTorque():
        name: str
        vtype: UF.UFMotion.VectorType
        link: Tag
        origin: Tag
        direction: Tag
        frame: UF.UFMotion.ReferenceFrame
        comp_functions: typing.List[Tag]
        magnitude_function: Tag
        reaction_link: Tag
    

    class VectorComponent(enum.Enum):
        Magnitude = 0
        XComponent = 1
        YComponent = 2
        ZComponent = 3
    

    class UFMotionTraceStruct():
        _object: Tag
        target_layer: int
    

    class UFMotionStlParameters():
        minimum_facet_length: float
        maximum_facet_length: float
        facet_tolerance: float
    

    class SpringDamperType(enum.Enum):
        UnknownSpringDamper = 0
        RevoluteSpringDamper = 1
        SliderSpringDamper = 2
        LinkSpringDamper = 3
    

    class UFMotionSpringDamper():
        name: str
        spr_dmp_type: UF.UFMotion.SpringDamperType
        joint: Tag
        link_1: Tag
        point_1: Tag
        pt1_coord: float
        link_2: Tag
        point_2: Tag
        pt2_coord: float
        spring_rate: float
        spring_preload: float
        spring_ref_length: float
        spring_ref_angle: float
        spring_init_length: float
        damping_rate: float
    

    class UFMotionSolverParameters():
        solver: UF.UFMotion.Solver
        max_step_size: float
        max_solver_error: float
        max_integrator_iterations: int
        max_kinematics_iterations: int
        max_statics_iterations: int
        use_mass_properties: int
    

    class Solver(enum.Enum):
        UnknownSolver = 0
        KinematicSolver = 1
        StaticDynamicSolver = 2
    

    class UFMotionScalarForceTorque():
        name: str
        attach_body: Tag
        origin_1: Tag
        origin_2: Tag
        force_function: Tag
        torque_function: Tag
        reaction_link: Tag
    

    class ReferenceFrame(enum.Enum):
        Absolute = 0
        FirstLink = 1
        SecondLink = 2
    

    class UFMotionPointOnSurfaceData():
        point_on_surface_tag: Tag
        point_tag: Tag
        point_link_tag: Tag
        num_face_tags: int
        face_tags: typing.List[Tag]
        face_link_tag: Tag
        display_scale: float
        entity_name: str
    

    class UFMotionPointCurveConstraint():
        name: str
        num_curve_tags: int
        curve: typing.List[Tag]
        point: Tag
    

    class MeasurementType(enum.Enum):
        UnknownMeasurement = 0
        DistanceMeasurement = 1
        AngleMeasurement = 2
    

    class UFMotionMeasurement():
        type: UF.UFMotion.MeasurementType
        object_1: Tag
        object_2: Tag
    

    class MarkerType(enum.Enum):
        UndefinedMarker = 0
        InertiaMarker = 1
        CofmMarker = 2
        UserDefinedMarker = 3
    

    class UFMotionMarker():
        name: str
        marker_type: UF.UFMotion.MarkerType
        attachment_tag: Tag
        orientation_tag: Tag
        origin_tag: Tag
        location: float
    

    class UFMotionLinkMassProperties():
        mass_center: Tag
        inertia_marker: Tag
        mass: float
        products_of_inertia: float
        user_defined: bool
    

    class UFMotionLinkInitialVel():
        linear_dir: Tag
        magnitude: float
        rotation_dir: Tag
        angular_mag: float
        rotation_csys: Tag
        rotation_vel: float
    

    class UFMotionLink():
        name: str
        num_geometry_tags: int
        geometry: typing.List[Tag]
    

    class JointType(enum.Enum):
        UnknownJoint = 0
        RevoluteJoint = 1
        SliderJoint = 2
        CylinderJoint = 3
        ScrewJoint = 4
        UniversalJoint = 5
        SphericalJoint = 6
        PlanarJoint = 7
        FixedJoint = 8
    

    class JointMotionInputType(enum.Enum):
        UnknownInput = 0
        FunctionInput = 1
        ConstantInput = 2
        HarmonicInput = 3
        ArticulationInput = 4
    

    class UFMotionJointMotionInput():
        input_type: UF.UFMotion.JointMotionInputType
        function: Tag
        displacement: float
        velocity: float
        acceleration: float
        amplitude: float
        frequency: float
        phase_angle: float
        harm_disp: float
    

    class UFMotionJointLimits():
        min: float
        max: float
    

    class JointCouplerType(enum.Enum):
        UnknownCoupler = 0
        RackAndPinionCoupler = 1
        GearCoupler = 2
        CableCoupler = 3
    

    class UFMotionJointCoupler():
        name: str
        jtc_type: UF.UFMotion.JointCouplerType
        joint_1: Tag
        joint_2: Tag
        ratio: float
        origin_tag: Tag
        orientation_tag: Tag
    

    class UFMotionJoint():
        name: str
        jt_type: UF.UFMotion.JointType
        snap_links: bool
        link_1: Tag
        link_2: Tag
        direction_1: Tag
        direction_2: Tag
        origin_1: Tag
        origin_2: Tag
        screw_ratio: float
    

    class UFMotionInterferenceStruct():
        solid_1: Tag
        solid_2: Tag
    

    class UFMotionGeneralBushing():
        name: str
        link_1: Tag
        origin_1: Tag
        direction_1: Tag
        link_2: Tag
        origin_2: Tag
        direction_2: Tag
        translational_stiffness: float
        translational_damping: float
        translational_preload: float
        torsional_stiffness: float
        torsional_damping: float
        torsional_preload: float
    

    class UFMotionFunction():
        name: str
        definition: str
        num_lines: int
    

    class FuncResultType(enum.Enum):
        FuncDisplacement = 0
        FuncVelocity = 1
        FuncAcceleration = 2
        FuncForce = 3
    

    class FuncRefFrameType(enum.Enum):
        FuncAbsoluteFrame = 0
        FuncRelativeFrame = 1
    

    class FuncComponentType(enum.Enum):
        FuncLinearMag = 0
        FuncXComp = 1
        FuncYComp = 2
        FuncZComp = 3
        FuncAngularMag = 4
        FuncEuler1Comp = 5
        FuncEuler2Comp = 6
        FuncEuler3Comp = 7
    

    class DispAngle(enum.Enum):
        EulerOne = 0
        EulerTwo = 1
        EulerThree = 2
    

    class UFMotionCylindricalBushing():
        name: str
        link_1: Tag
        origin_1: Tag
        direction_1: Tag
        link_2: Tag
        origin_2: Tag
        direction_2: Tag
        radial_stiffness: float
        longitudinal_stiffness: float
        conical_stiffness: float
        torsional_stiffness: float
        radial_damping: float
        longitudinal_damping: float
        conical_damping: float
        torsional_damping: float
    

    class UFMotionCurveCurveConstraint():
        name: str
        num_curve_1_tags: int
        curve_1: typing.List[Tag]
        num_curve_2_tags: int
        curve_2: typing.List[Tag]
    

    class UFMotionContactParameters():
        force_exponent: float
        material_damping: float
        penetration_depth: float
        static_friction: float
        slip_velocity: float
        dynamic_friction: float
        transition_velocity: float
    

    class AnlGeometryFormat(enum.Enum):
        StlFormat = 0
        ParasolidFormat = 1
        NoFormat = 2
        UnknownGeometryFormat = 3
    

    class AngularUnitsType(enum.Enum):
        DegreeUnits = 0
        RadianUnits = 1
    

    class _3d_contact_method_(enum.Enum):
        FacetedContact = 0
        PreciseContact = 1
        UnknownContactMethod = 2
    

    class _3D_contact_friction_(enum.Enum):
        _3D_CONTACT_NO_FRICTION = 0
        _3D_CONTACT_ALL_FRICTION = 1
    

    class _3D_contact_force_(enum.Enum):
        _3D_CONTACT_IMPACT = 0
        _3D_CONTACT_POISSON = 1
    

    class UFMotion_3D_contact_():
        name: str
        num_contact_side_1: int
        contact_side_1: typing.List[Tag]
        num_contact_side_2: int
        contact_side_2: typing.List[Tag]
        force_model_type: UF.UFMotion._3D_contact_force_
        friction_option: UF.UFMotion._3D_contact_friction_
        stiffness: float
        advanced: UF.UFMotion.ContactParameters
        restitution_coefficient: float
    

    class UFMotion_2D_contact_():
        name: str
        num_curve_1: int
        curve_1: typing.List[Tag]
        num_curve_2: int
        curve_2: typing.List[Tag]
        max_num_contact_points: int
        switch_material_side_1: bool
        switch_material_side_2: bool
        stiffness: float
        advanced: UF.UFMotion.ContactParameters
    

class UFMom(Utilities.NXRemotableObject):
    def AskAssocDoubleArray(self, mom: int, array_name: str, index_name: str, value: float) -> None:
        ...
    def AskAssocIntArray(self, mom: int, array_name: str, index_name: str, value: int) -> None:
        ...
    def AskAssocStringArray(self, mom: int, array_name: str, index_name: str, value: str) -> None:
        ...
    def AskDoubleArray(self, mom: int, array_name: str, num_of_values: int, values: float) -> None:
        ...
    def AskDoubleArray2d(self, mom: int, array_name: str, index1: int, index2: int, value: float) -> None:
        ...
    def AskIntArray(self, mom: int, array_name: str, num_of_values: int, values: int) -> None:
        ...
    def AskInterpFromParam(self, param: int, interp: int) -> None:
        ...
    def AskMom(self, param: int, mom_id: int) -> None:
        ...
    def AskString(self, mom_id: int, var_name: str, var_val: str) -> None:
        ...
    def AskStringArray(self, mom: int, array_name: str, num_of_values: int, values: bytes) -> None:
        ...
    def ExecuteCommand(self, mom: int, command: str) -> None:
        ...
    def ExtendXlator(self, mom_id: int, command_name: str, c_func: UF.UFMom.CommandFunc) -> None:
        ...
    def SetAssocDoubleArray(self, mom: int, array_name: str, index_name: str, value: float) -> None:
        ...
    def SetAssocIntArray(self, mom: int, array_name: str, index_name: str, value: int) -> None:
        ...
    def SetAssocStringArray(self, mom: int, array_name: str, index_name: str, value: str) -> None:
        ...
    def SetDouble(self, mom_id: int, var_name: str, var_val: float) -> None:
        ...
    def SetDoubleArray(self, mom: int, array_name: str, num_of_values: int, values: float) -> None:
        ...
    def SetInt(self, mom_id: int, var_name: str, var_val: int) -> None:
        ...
    def SetIntArray(self, mom: int, array_name: str, num_of_values: int, values: int) -> None:
        ...
    def SetString(self, mom_id: int, var_name: str, var_val: str) -> None:
        ...
    def SetStringArray(self, mom: int, array_name: str, num_of_values: int, values: str) -> None:
        ...


    

class UFModlTrex(Utilities.NXRemotableObject):
    def InitTrexDataSet(self, feature_data_set: UF.UFModlTrex.DataSet) -> None:
        ...


    class ToOption(enum.Enum):
        Distance = 0
        Percent = 1
        Surface = 2
    

    class RegionOption(enum.Enum):
        Keep = 0
        Remove = 1
    

    class ExtendMethod(enum.Enum):
        C2 = 0
        Linear = 1
        Reflected = 2
        Natural = 3
    

    class UFModlTrexDataSet():
        collector: Tag
        extend_val: float
        offset_val: float
        reversed: int
    

    

class UFModlSweep(Utilities.NXRemotableObject):
    def FreeTrimData(self, trim_object: UF.ModlSweepTrimObject) -> None:
        ...


class UFModl(Utilities.NXRemotableObject):
    def ActivePart(self, body_obj_id: Tag, flag: int) -> None:
        ...
    def AddThruFaces(self, feature_eid: Tag, number_of_faces: int, face_eids: typing.List[Tag]) -> None:
        ...
    def Ask2dtrimBsurf(self, face: Tag, opts: int, tolerance: float, bsurf: UF.UFModl.Bsurface, loop_count: int, edge_count: int, edge_sense: int, edge_bcurves: typing.List[Tag]) -> None:
        ...
    def AskAdjacFaces(self, face: Tag, adjacent_faces: typing.List[Tag]) -> None:
        ...
    def AskAliveEdge(self, edge: Tag, alive_edge: Tag) -> None:
        ...
    def AskAliveFace(self, face: Tag, alive_face: Tag) -> None:
        ...
    def AskAllMembersOfSet(self, set: Tag, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def AskAngleEdge(self, feature_obj_id: Tag, constraint: Tag, edit: int, fixed1: float, fixed2: float, feature1: float, feature2: float, how_far: str, tool: Tag, part: Tag) -> None:
        ...
    def AskAngleTolerance(self, tolerance: float) -> None:
        ...
    def AskBallGrooveParms(self, feature_obj_id: Tag, edit: int, groove_dia: str, ball_dia: str) -> None:
        ...
    def AskBallSlotParms(self, feature_obj_id: Tag, edit: int, ball_dia: str, depth: str, distance: str, thru_flag: int) -> None:
        ...
    def AskBendAllowanceFormula(self, feature_tag: Tag, exp_str: str) -> None:
        ...
    def AskBendOperation(self, operation_tag: Tag, bend_data: UF.UFModl.BendOperationData) -> None:
        ...
    def AskBlendParms(self, feature_obj_id: Tag, edit: int, radius: str) -> None:
        ...
    def AskBlockParms(self, feature_obj_id: Tag, edit: int, size: str) -> None:
        ...
    def AskBodyBoundaries(self, body_tag: Tag, num_boundaries: int, num_edges: int, edge_tags: typing.List[Tag]) -> None:
        ...
    def AskBodyConsistency(self, body_tag: Tag, num_tags: int, fault_tokens: int, fault_tags: typing.List[Tag]) -> None:
        ...
    def AskBodyDensity(self, body: Tag, units: UF.UFModl.DensityUnits, density: float) -> None:
        ...
    def AskBodyEdges(self, body: Tag, edge_list: typing.List[Tag]) -> None:
        ...
    def AskBodyFaces(self, body: Tag, face_list: typing.List[Tag]) -> None:
        ...
    def AskBodyFeats(self, body: Tag, feature_tag_list: typing.List[Tag]) -> None:
        ...
    def AskBodyFeatures(self, body_id: Tag, features_count: int, features_node: typing.List[UF.UFModl.Features]) -> None:
        ...
    def AskBodyStructures(self, body_tag: Tag, num_tags: int, fault_tags: typing.List[Tag]) -> None:
        ...
    def AskBodyType(self, body_id: Tag, body_type: int) -> None:
        ...
    def AskBodyTypePref(self, body_type: int) -> None:
        ...
    def AskBooleanWithRetainedOptions(self, feature_eid: Tag, sign: UF.FeatureSigns, original_target: Tag, original_tool: Tag, retain_target_body: bool, retain_tool_body: bool) -> None:
        ...
    def AskBossParms(self, feature_obj_id: Tag, edit: int, diameter: str, height: str, taper_angle: str) -> None:
        ...
    def AskBoundingBox(self, _object: Tag, bounding_box: float) -> None:
        ...
    def AskBoundingBoxAligned(self, _object: Tag, csys_tag: Tag, expand: bool, min_corner: float, directions: float, distances: float) -> None:
        ...
    def AskBoundingBoxExact(self, _object: Tag, csys_tag: Tag, min_corner: float, directions: float, distances: float) -> None:
        ...
    def AskBplane(self, feature_obj_id: Tag, s_section: UF.StringList, tol: float) -> None:
        ...
    def AskBsurf(self, face: Tag, bsurf: UF.UFModl.Bsurface) -> None:
        ...
    def AskBsurfKnotDisplay(self, face: Tag, state: bool) -> None:
        ...
    def AskBsurfPoleDisplay(self, face: Tag, state: bool) -> None:
        ...
    def AskCBoreHoleParms(self, feature_obj_id: Tag, edit: int, diameter1: str, diameter2: str, depth1: str, depth2: str, tip_angle: str, thru_flag: int) -> None:
        ...
    def AskCSunkHoleParms(self, feature_obj_id: Tag, edit: int, diameter1: str, diameter2: str, depth1: str, csink_angle: str, tip_angle: str, thru_flag: int) -> None:
        ...
    def AskChamferParms(self, feature_obj_id: Tag, edit: int, subtype: int, radius1: str, radius2: str, theta: str) -> None:
        ...
    def AskCircularIsetParms(self, feature_obj_id: Tag, edit: int, radius: str, number: str, angle: str) -> None:
        ...
    def AskCircularPatternFace(self, feature_tag: Tag, region: typing.List[UF.UFModl.DfoRegion], axis: Tag, n_pattern: int, angle: str) -> None:
        ...
    def AskCnncEdges(self, edge: Tag, reference: float, edges1: typing.List[Tag], edges2: typing.List[Tag]) -> None:
        ...
    def AskConeParms(self, feature_obj_id: Tag, edit: int, base_diameter: str, top_diameter: str, height: str, half_angle: str) -> None:
        ...
    def AskConstraintType(self, constraint: Tag, type: str) -> None:
        ...
    def AskConstraints(self, feature: Tag, constraints: typing.List[Tag]) -> None:
        ...
    def AskCurrentFeature(self, part: Tag, feature_id: Tag) -> None:
        ...
    def AskCurveClosed(self, tag: Tag) -> int:
        ...
    def AskCurveFitData(self, curve_fit_data: UF.UFModl.CurveFitData) -> None:
        ...
    def AskCurveFitMethod(self, fit_method: int) -> None:
        ...
    def AskCurveMesh(self, feature_obj_id: Tag, s_prim: UF.StringList, s_cross: UF.StringList, s_spine: UF.StringList, emphasis: int, body_type: int, spline_pts: int, tol: float, c_face_id: typing.List[Tag], c_flag: int) -> None:
        ...
    def AskCurveMesh1(self, feature_obj_id: Tag, s_prim: UF.StringList, s_cross: UF.StringList, s_spine: UF.StringList, emphasis: int, body_type: int, spline_pts: int, tol: float, c_collector_id: typing.List[Tag], c_flag: int) -> None:
        ...
    def AskCurveParm(self, curve_id: Tag, ref_pnt: float, parm: float, curve_pnt: float) -> None:
        ...
    def AskCurveParmNoExt(self, curve_id: Tag, ref_point: float, parm: float) -> None:
        ...
    def AskCurvePeriodicity(self, curve_id: Tag, status: int) -> None:
        ...
    def AskCurvePoints(self, curve_id: Tag, ctol: float, atol: float, stol: float, numpts: int, pts: float) -> None:
        ...
    def AskCurveProps(self, curve_id: Tag, parm: float, point: float, tangent: float, p_norm: float, b_norm: float, torsion: float, rad_of_cur: float) -> None:
        ...
    def AskCylPocketParms(self, feature_obj_id: Tag, edit: int, diameter: str, depth: str, floor_rad: str, taper_angle: str) -> None:
        ...
    def AskCylinderParms(self, feature_obj_id: Tag, edit: int, diameter: str, height: str) -> None:
        ...
    def AskDatumAxisParms(self, feature_id: Tag, origin: float, normal: float) -> None:
        ...
    def AskDatumCsysComponents(self, datum_csys_tag: Tag, csys_tag: Tag, origin: Tag, daxes: typing.List[Tag], dplanes: typing.List[Tag]) -> None:
        ...
    def AskDatumPlane(self, dplane_tag: Tag, dplane_point: float, dplane_normal: float) -> None:
        ...
    def AskDatumPlaneParms(self, feature_obj_id: Tag, origin: float, normal: float, offset: str, angle: str) -> None:
        ...
    def AskDatumPointAndDirection(self, datum_feature_tag: Tag, point: Tag, direction: Tag) -> None:
        ...
    def AskDaxisSize(self, daxis_tag: Tag, length: float) -> None:
        ...
    def AskDefaultDensity(self, units: UF.UFModl.DensityUnits, density: float) -> None:
        ...
    def AskDescriptorOfExp(self, exp: Tag, descriptor: str) -> None:
        ...
    def AskDistanceTolerance(self, tolerance: float) -> None:
        ...
    def AskDovetailSlotParms(self, feature_obj_id: Tag, edit: int, width: str, depth: str, angle: str, distance: str, thru_flag: int) -> None:
        ...
    def AskDynamicUpdate(self, update_type: int) -> None:
        ...
    def AskEdgeBlend(self, feature_obj_id: Tag, blend_data: UF.UFModl.EdgeBlendData) -> None:
        ...
    def AskEdgeBlend1(self, feature_obj_id: Tag, blend_data: UF.UFModl.EdgeBlendData) -> None:
        ...
    def AskEdgeBlendIsMult(self, feature_eid: Tag) -> bool:
        ...
    def AskEdgeBody(self, edge: Tag, body_obj_id: Tag) -> None:
        ...
    def AskEdgeFaces(self, edge: Tag, face_list: typing.List[Tag]) -> None:
        ...
    def AskEdgeFeats(self, edge_obj_id: Tag, feature_list: typing.List[Tag]) -> None:
        ...
    def AskEdgeSmoothness(self, edge_tag: Tag, tolerance: float, is_smooth: bool) -> None:
        ...
    def AskEdgeTolerance(self, edge_tag: Tag, tolerance: float) -> None:
        ...
    def AskEdgeType(self, edge_id: Tag, edge_type: int) -> None:
        ...
    def AskEdgeVerts(self, edge: Tag, point1: float, point2: float, vertex_count: int) -> None:
        ...
    def AskEnlarge(self, feat_obj_tag: Tag, face: Tag, type: int, percent_size: str, tolerance: float) -> None:
        ...
    def AskEntityParents(self, num_entities: int, entities: Tag, found_parent: bool, num_parent_entities: int, parent_entities: typing.List[Tag]) -> None:
        ...
    def AskExp(self, exp_name: str, exp_defn: str) -> None:
        ...
    def AskExpDescOfFeat(self, feature_obj_id: Tag, number_of_exps: int, descriptions: str, exps: typing.List[Tag]) -> None:
        ...
    def AskExpDescOfFrec(self, feature_obj_id: Tag, number_of_exps: int, descriptions: str, exps: typing.List[Tag]) -> None:
        ...
    def AskExpTagString(self, expression_tag: Tag, _string: str) -> None:
        ...
    def AskExpTagValue(self, expression_tag: Tag, value: float) -> None:
        ...
    def AskExpsOfFeature(self, feature: Tag, number_of_exps: int, exps: typing.List[Tag]) -> None:
        ...
    def AskExpsOfPart(self, part_tag: Tag, number_of_exps: int, exps: typing.List[Tag]) -> None:
        ...
    def AskExtreme(self, _object: Tag, dir1: float, dir2: float, dir3: float, subent: Tag, point: float) -> None:
        ...
    def AskExtrudeOffsetDir(self, feature_id: Tag, point: float, direction: float) -> None:
        ...
    def AskExtrusion(self, feature_obj_id: Tag, num_objects: int, objects: typing.List[Tag], trim_ptr: typing.List[UF.ModlSweepTrimObject], taper_angle: str, limits: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, direction: float) -> None:
        ...
    def AskFaceBlendLawRadii(self, feature: Tag, radii_values: float, rad_num: int) -> None:
        ...
    def AskFaceBlendLawRange1Radii(self, feature: Tag, radii_values: float, rad_num: int) -> None:
        ...
    def AskFaceBlendLawRange2Radii(self, feature: Tag, radii_values: float, rad_num: int) -> None:
        ...
    def AskFaceBody(self, face: Tag, body_obj_id: Tag) -> None:
        ...
    def AskFaceConstraint(self, feature_tag: Tag, region: typing.List[UF.UFModl.DfoRegion], constraint: typing.List[UF.UFModl.DfoConstraint]) -> None:
        ...
    def AskFaceData(self, face: Tag, type: int, point: float, dir: float, box: float, radius: float, rad_data: float, norm_dir: int) -> None:
        ...
    def AskFaceEdges(self, face: Tag, edge_list: typing.List[Tag]) -> None:
        ...
    def AskFaceFaceIntersect(self, body_tag: Tag, num_tags: int, fault_tags: typing.List[Tag]) -> None:
        ...
    def AskFaceFeats(self, face_obj_id: Tag, feature_list: typing.List[Tag]) -> None:
        ...
    def AskFaceGridCount(self, _object: Tag, u_count: int, v_count: int) -> None:
        ...
    def AskFaceMinRadii(self, face: Tag, num_radii: int, radii: float, positions: float, _params: float) -> None:
        ...
    def AskFaceParm(self, face_id: Tag, ref_pnt: float, parm: float, face_pnt: float) -> None:
        ...
    def AskFaceParm2(self, face_id: Tag, ref_pnt: float, parm: float, face_pnt: float) -> None:
        ...
    def AskFacePeriodicity(self, face_id: Tag, U_status: int, U_period: float, V_status: int, V_period: float) -> None:
        ...
    def AskFaceProps(self, face_id: Tag, param: float, point: float, u1: float, v1: float, u2: float, v2: float, unit_norm: float, radii: float) -> None:
        ...
    def AskFaceSelfIntersect(self, face_tag: Tag, fault_token: int, point: float) -> None:
        ...
    def AskFaceSmoothness(self, face_tag: Tag, is_smooth: bool) -> None:
        ...
    def AskFaceSpikes(self, face_tag: Tag, is_spike: bool) -> None:
        ...
    def AskFaceTopology(self, face_id: Tag, topo_type: int) -> None:
        ...
    def AskFaceTorusType(self, face: Tag, torus_type: int) -> None:
        ...
    def AskFaceType(self, face: Tag, type: int) -> None:
        ...
    def AskFaceUvMinmax(self, face_tag: Tag, uv_min_max: float) -> None:
        ...
    def AskFacepairParms(self, facepair_feature_obj_id: Tag, face_pair_type: int, midsrf_feature_obj_id: Tag, defining_face_1: Tag, defining_face_2: Tag, user_selected_midsurface: Tag, side_1: typing.List[Tag], side_2: typing.List[Tag], midsurface_sheet_body: Tag) -> None:
        ...
    def AskFeatBody(self, feature_obj_id: Tag, body_obj_id: Tag) -> None:
        ...
    def AskFeatDirection(self, feature_obj_id: Tag, dir_x: float, dir_y: float) -> None:
        ...
    def AskFeatDisplayName(self, feature_tag: Tag, feature_name: str) -> None:
        ...
    def AskFeatEdges(self, feature_obj_id: Tag, object_list: typing.List[Tag]) -> None:
        ...
    def AskFeatError(self, feature_tag: Tag, errNum: int, errMessage: str) -> None:
        ...
    def AskFeatFaces(self, feature_obj_id: Tag, object_list: typing.List[Tag]) -> None:
        ...
    def AskFeatFailList(self, failure_frec_list: typing.List[Tag]) -> None:
        ...
    def AskFeatLocation(self, feature_obj_id: Tag, location: float) -> None:
        ...
    def AskFeatName(self, feature_tag: Tag, feature_name: str) -> None:
        ...
    def AskFeatObject(self, feature: Tag, n_eids: int, eids: typing.List[Tag]) -> None:
        ...
    def AskFeatOrUdfSysname(self, feature_eid: Tag, feature_name: str) -> None:
        ...
    def AskFeatRelatives(self, feature_tag: Tag, num_parents: int, parent_array: typing.List[Tag], num_children: int, children_array: typing.List[Tag]) -> None:
        ...
    def AskFeatSysname(self, feature_eid: Tag, feature_name: str) -> None:
        ...
    def AskFeatTolerance(self, feature_obj_id: Tag, tolerance_exists: bool, tolerance: float) -> None:
        ...
    def AskFeatType(self, feature_obj_id: Tag, feature_type: str) -> None:
        ...
    def AskFeatWarningMessages(self, feature_eid: Tag, wanNum: int, wanMessage: str) -> None:
        ...
    def AskFeatureBoolean(self, feature_obj_id: Tag, boolean_status: UF.FeatureSigns) -> None:
        ...
    def AskFeatureSign(self, feature_obj_id: Tag, sign: UF.FeatureSigns) -> None:
        ...
    def AskFeaturesOfExp(self, exp: Tag, number_of_features: int, features: typing.List[Tag]) -> None:
        ...
    def AskFeaturesOfMirrorSet(self, mirror_set: Tag, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def AskFeaturesOfUdf(self, udf_tag: Tag, features: typing.List[Tag], num_feature: int) -> None:
        ...
    def AskFlangeParms(self, feature_tag: Tag, parameters: typing.List[UF.UFModl.FlangeData]) -> None:
        ...
    def AskFlangeProcFactor(self, flange: Tag, proc_factor: float) -> None:
        ...
    def AskFormableFeatureState(self, feature_tag: Tag, state: UF.UFModl.State, state_info: UF.UFModl.StateInfo) -> None:
        ...
    def AskFreeFormResult(self, free_form_result: int) -> None:
        ...
    def AskHollowData(self, feature_id: Tag, type: int, tolerance: float, thickness: str, n_pierced_faces: int, pierced_faces: typing.List[Tag], n_boundary_faces: int, boundary_faces: typing.List[Tag], n_offset_faces: int, offset_faces: typing.List[Tag], offset_thickness: str) -> None:
        ...
    def AskHollowParms(self, feature_obj_id: Tag, edit: int, thickness: str) -> None:
        ...
    def AskHorzDime(self, feature_obj_id: Tag, constraint: Tag, edit: int, _fixed: float, feature: float, fixc: float, feac: float, how_far: str, tool: Tag, part: Tag) -> None:
        ...
    def AskImmediateChildren(self, update_level: int) -> None:
        ...
    def AskImprEdges(self, feature_tag: Tag, n_edges: int, edges: typing.List[Tag]) -> None:
        ...
    def AskImprFacesParms(self, feature_tag: Tag, parms: UF.UFModl.ImprintFacesData) -> None:
        ...
    def AskImprLoopParms(self, feature_tag: Tag, parms: UF.UFModl.ImprintLoopData) -> None:
        ...
    def AskInputCurvesFromSection(self, section: Tag, n_loops: int, n_crv_each_loops: int, input_curves: typing.List[UF.ScSectionOutputData]) -> None:
        ...
    def AskInsetFlangeParms(self, feature_tag: Tag, parameters: typing.List[UF.UFModl.InsetFlangeData]) -> None:
        ...
    def AskInstance(self, feature_obj_id: Tag, instances_feature_list: typing.List[Tag]) -> None:
        ...
    def AskInstanceIset(self, feature_obj_id: Tag, iset_feature_obj_id: Tag) -> None:
        ...
    def AskInstancesOfFeature(self, feature_tag: Tag, feature_patterns: typing.List[Tag], n_feature_patterns: int) -> None:
        ...
    def AskLawExtension(self, law_extension: Tag, law_extension_data: UF.UFModl.LawextData) -> None:
        ...
    def AskLawExtension1(self, law_extension: Tag, law_extension_data: UF.UFModl.LawextData) -> None:
        ...
    def AskLinearIsetParms(self, feature_obj_id: Tag, edit: int, number_in_x: str, number_in_y: str, distance_x: str, distance_y: str) -> None:
        ...
    def AskLinkFacePlane(self, feature_obj_id: Tag, link_face_parms: Tag, cplane_csys: float) -> None:
        ...
    def AskLinkFaces(self, feature_eid: Tag, target_face_eid: Tag, tool_face_eid: Tag, dir_ref: Tag, ref_is_horizontal: bool) -> None:
        ...
    def AskLinkedExterior(self, feature_tag: Tag, ext_data: UF.UFModl.LinkedExt, num_groups: int, groups: typing.List[Tag], num_subfeats: int, subfeats: typing.List[Tag], mass_props: float) -> None:
        ...
    def AskListCount(self, list: typing.List[Tag], count: int) -> None:
        ...
    def AskListItem(self, list: typing.List[Tag], index: int, _object: Tag) -> None:
        ...
    def AskLocalScale(self, feature_tag: Tag, type: UF.UFModl.DfoScaleType, region: typing.List[UF.UFModl.DfoRegion], so_point: Tag, so_dir: Tag, so_csys: Tag, factor: str) -> None:
        ...
    def AskMassProps3d(self, objects: typing.List[Tag], num_objs: int, type: int, units: int, density: float, accuracy: int, acc_value: float, mass_props: float, statistics: float) -> None:
        ...
    def AskMaster(self, feature_obj_id: Tag, master_feature_obj_id: Tag) -> None:
        ...
    def AskMatchingFaceInInstance(self, face_tag: Tag, feat_instance: Tag, instanced_face: Tag) -> None:
        ...
    def AskMaxCurvature(self, eid: Tag, range: float, curva_type: int, max_curva: float, status: int) -> None:
        ...
    def AskMergedFaces(self, face: Tag, nfaces: int, faces: typing.List[Tag]) -> None:
        ...
    def AskMidsrfFeatureCreateMethod(self, feature_obj_id: Tag, adv_crt_and_trm: int) -> None:
        ...
    def AskMidsrfParms(self, feature_obj_id: Tag, facepair_list: typing.List[Tag]) -> None:
        ...
    def AskMinimumDist(self, object1: Tag, object2: Tag, guess1_given: int, guess1: float, guess2_given: int, guess2: float, min_dist: float, pt_on_obj1: float, pt_on_obj2: float) -> None:
        ...
    def AskMinimumDist2(self, object1: Tag, object2: Tag, guess1_given: int, guess1: float, guess2_given: int, guess2: float, min_dist: float, pt_on_obj1: float, pt_on_obj2: float, accuracy: float) -> None:
        ...
    def AskMinimumDist3(self, opt_level: int, object1: Tag, object2: Tag, guess1_given: int, guess1: float, guess2_given: int, guess2: float, min_dist: float, pt_on_obj1: float, pt_on_obj2: float, accuracy: float) -> None:
        ...
    def AskMirrorPatternFace(self, feature_tag: Tag, region: typing.List[UF.UFModl.DfoRegion], mirror_plane: Tag) -> None:
        ...
    def AskMisalignGeometry(self, obj_tag: Tag, matrix: float, tolerance: float, is_misaligned: bool) -> None:
        ...
    def AskMoveRegion(self, feature_tag: Tag, type: UF.UFModl.TransformType, region: typing.List[UF.UFModl.DfoRegion], transf_data: int) -> None:
        ...
    def AskNamedBodyObject(self, body_tag: Tag, object_type: int, object_name: str, _object: Tag) -> None:
        ...
    def AskNestedFrecs(self, feature: Tag, feature_list: typing.List[Tag]) -> None:
        ...
    def AskNextFeature(self, feature: Tag, next_feature: Tag) -> None:
        ...
    def AskObjDimensionality(self, object_id: Tag, dimensionality: int, data: float) -> None:
        ...
    def AskObject(self, ug_type: int, ug_subtype: int, _object: Tag) -> None:
        ...
    def AskObjectFeat(self, object_tag: Tag, feature_tag: Tag) -> None:
        ...
    def AskOffsetParms(self, feature_obj_id: Tag, edit: int, value: str) -> None:
        ...
    def AskOffsetRegion(self, feature_tag: Tag, region: typing.List[UF.UFModl.DfoRegion], offset: str) -> None:
        ...
    def AskOutOfDateFeatures(self, num_feature: int, features: typing.List[Tag]) -> None:
        ...
    def AskOwningFeatOfExp(self, exp: Tag, feature: Tag) -> None:
        ...
    def AskParaDist(self, feature_obj_id: Tag, constraint: Tag, edit: int, _fixed: float, feature: float, fixc: float, feac: float, how_far: str, tool: Tag, part: Tag) -> None:
        ...
    def AskParaEdge(self, feature_obj_id: Tag, constraint: Tag, edit: int, fixed1: float, fixed2: float, feature1: float, feature2: float, parallel: int, how_far: str, tool: Tag, part: Tag) -> None:
        ...
    def AskPatchBodyParms(self, feature_obj_id: Tag, target_body: Tag, tool_sheet: Tag, reverse: int) -> None:
        ...
    def AskPerpDist(self, feature: Tag, constraint: Tag, edit: int, fixed1: float, fixed2: float, feature1: float, feac: float, how_far: str, tool: Tag, part: Tag) -> None:
        ...
    def AskPlane(self, plane_tag: Tag, origin_point: float, plane_normal: float) -> None:
        ...
    def AskPlaneOfMirrorSet(self, mirror_set: Tag, plane: Tag) -> None:
        ...
    def AskPointAlongCurve(self, point: float, curve: Tag, offset: float, direction: int, tolerance: float, parameter: float) -> None:
        ...
    def AskPointAlongCurve2(self, point: float, curve: Tag, offset: float, direction: int, tolerance: float, point_along_curve: float, parameter: float) -> None:
        ...
    def AskPointContainment(self, point: float, body: Tag, pt_status: int) -> None:
        ...
    def AskPointsParms(self, feature_tag: Tag, num_points: int, points: typing.List[Tag]) -> None:
        ...
    def AskPreviousFeature(self, feature: Tag, prev_feature: Tag) -> None:
        ...
    def AskPrismParms(self, feature_tag: Tag, edit: int, diameter: str, height: str, number_of_sides: str) -> None:
        ...
    def AskProjCurves(self, proj_curve_feature: Tag, uf_curve_refs: typing.List[Tag]) -> None:
        ...
    def AskPromFeatOfSolid(self, prom_solid: Tag, prom_feat: Tag) -> None:
        ...
    def AskPromotionPath(self, prom_solid: Tag, full_path: bool, instance_path: typing.List[Tag], num_instances: int) -> None:
        ...
    def AskProperLegacyFeatName(self, feature_tag: Tag, feature_name: str) -> None:
        ...
    def AskQuiltType(self, quilt_tag: Tag, quilt_data: UF.UFModl.QuiltType) -> None:
        ...
    def AskReblendFace(self, feature_eid: Tag, reblend_data: UF.UFModl.ReblendFaceData) -> None:
        ...
    def AskRectGrooveParms(self, feature_obj_id: Tag, edit: int, groove_dia: str, width: str) -> None:
        ...
    def AskRectPadParms(self, feature_obj_id: Tag, edit: int, size: str, corner_rad: str, taper_angle: str) -> None:
        ...
    def AskRectPadParms1(self, feature_obj_id: Tag, edit: int, pad_length: int, size: str, corner_rad: str, taper_angle: str) -> None:
        ...
    def AskRectPocketParms(self, feature_obj_id: Tag, edit: int, length: str, corner_rad: str, floor_rad: str, taper_angle: str) -> None:
        ...
    def AskRectSlotParms(self, feature_obj_id: Tag, edit: int, width: str, depth: str, distance: str, thru_flag: int) -> None:
        ...
    def AskRectangularPatternFace(self, feature_tag: Tag, region: typing.List[UF.UFModl.DfoRegion], x_axis: Tag, axis: Tag, num_x: int, num_y: int, x_offset: str, y_offset: str) -> None:
        ...
    def AskReferencesOfFeatures(self, feature_array: typing.List[Tag], num_features: int, parents: typing.List[Tag], parent_names: str, num_parents: int) -> None:
        ...
    def AskRefitFaceFeatureData(self, refit: Tag, refit_data: UF.UFModl.RefitFaceData) -> None:
        ...
    def AskReplaceFace(self, feature_tag: Tag, target_faces: typing.List[Tag], num_target: int, non_blend_faces: typing.List[Tag], num_non_blend: int, tool_face: Tag, reverse_direction: bool) -> None:
        ...
    def AskResizeFace(self, feature_tag: Tag, target_faces: typing.List[Tag], num_target: int, non_blend_faces: typing.List[Tag], num_non_blend: int, parameter: str) -> None:
        ...
    def AskRevolution(self, feature_obj_id: Tag, num_objects: int, objects: typing.List[Tag], trim_ptr: typing.List[UF.ModlSweepTrimObject], limits: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, direction: float) -> None:
        ...
    def AskRipedge(self, ripedge_tag: Tag, ripedge_ufdata: UF.UFModl.RipedgeData) -> None:
        ...
    def AskRoughOffset(self, feature_tag: Tag, parms: UF.UFModl.RoughOffset) -> None:
        ...
    def AskRpoDescOfFeat(self, feature_obj_id: Tag, number_of_exps: int, descriptions: str, exps: typing.List[Tag]) -> None:
        ...
    def AskRpoDescOfFrec(self, feature_obj_id: Tag, number_of_exps: int, descriptions: str, exps: typing.List[Tag]) -> None:
        ...
    def AskRpoRoutine(self, user_rpo_routine: UF.UFModl.RpoFPT) -> None:
        ...
    def AskRuled(self, feature_obj_id: Tag, s_section: UF.StringList, s_spine: UF.StringList, alignment: int, value: float, body_type: int, tol: float) -> None:
        ...
    def AskRuled1(self, feature_obj_id: Tag, s_section: UF.StringList, s_spine: UF.StringList, alignment: int, value: float, body_type: int, tols: float) -> None:
        ...
    def AskScale(self, feature_tag: Tag, type: UF.ScaleType, so_point: Tag, so_dir: Tag, so_csys: Tag, factor: str) -> None:
        ...
    def AskSetFromName(self, name: str, set: Tag) -> None:
        ...
    def AskSetsOfMember(self, feature: Tag, sets: typing.List[Tag], number_of_sets: int) -> None:
        ...
    def AskSewSheetBody(self, feature_obj_eid: Tag, target_sheet_body: Tag, tool_sheet_bodies_count: int, tool_sheet_bodies: typing.List[Tag], tolerance: float) -> None:
        ...
    def AskSewSolidBody(self, feature_obj_eid: Tag, target_faces_count: int, target_faces: typing.List[Tag], tool_faces_count: int, tool_faces: typing.List[Tag], tolerance: float) -> None:
        ...
    def AskSharedEdges(self, face1: Tag, face2: Tag, shared_edges: typing.List[Tag]) -> None:
        ...
    def AskShowReportReference(self, reportReference: bool) -> None:
        ...
    def AskSilhouetteFlange(self, sflange_tag: Tag, sflange_data: UF.UFModl.SflangeData) -> None:
        ...
    def AskSimpleHoleParms(self, feature_obj_id: Tag, edit: int, diameter: str, depth: str, tip_angle: str, thru_flag: int) -> None:
        ...
    def AskSimplifyParms(self, feature_tag: Tag, simpl_parms: UF.UFModl.SimplData) -> None:
        ...
    def AskSketchOfSweep(self, sweep_obj_id: Tag, sketch_obj_id: Tag) -> None:
        ...
    def AskSmartContainerSubtype(self, smart_container_tag: Tag, smart_container_subtype: int) -> None:
        ...
    def AskSmbend(self, bend_tag: Tag, user_data: UF.UFModl.SmbendData) -> None:
        ...
    def AskSmbendCorner(self, bend_tag: Tag, user_data: UF.UFModl.SmbendCornerData) -> None:
        ...
    def AskSmbendCylinder(self, bend_tag: Tag, user_data: UF.UFModl.SmbendCylinderData) -> None:
        ...
    def AskSmcorner(self, smcorner_tag: Tag, smcorner_ufdata: UF.UFModl.SmcornerData) -> None:
        ...
    def AskSmcutout(self, cutout_tag: Tag, user_data: UF.UFModl.SmcutoutData) -> None:
        ...
    def AskSmhole(self, hole_tag: Tag, user_data: UF.UFModl.SmholeData) -> None:
        ...
    def AskSmpunch(self, user_data: UF.UFModl.SmpunchData, punch_tag: Tag) -> None:
        ...
    def AskSmslot(self, slot_tag: Tag, user_data: UF.UFModl.SmslotData) -> None:
        ...
    def AskSnipSurfaceFeatureData(self, snip: Tag, ask_usr_data_ptr: UF.UFModl.SnipsrfFeatureData) -> None:
        ...
    def AskSolidOfPromFeat(self, prom_feat: Tag, prom_solid: Tag) -> None:
        ...
    def AskSolidPunch(self, smspunch_tag: Tag, smspunch_ufdata: UF.UFModl.SolidPunchData) -> None:
        ...
    def AskSphereParms(self, feature_obj_id: Tag, edit: int, diameter: str) -> None:
        ...
    def AskSplitEdges(self, edge: Tag, nedges: int, edges: typing.List[Tag]) -> None:
        ...
    def AskSplitFaces(self, face: Tag, nfaces: int, faces: typing.List[Tag]) -> None:
        ...
    def AskStycornerData(self, frec_tag: Tag, styled_corner_data_out: UF.UFModl.StycornerData) -> None:
        ...
    def AskSubdivFaceParms(self, feature_obj_id: Tag, face: Tag, curves: typing.List[Tag], count: int, proj_type: int, vector: float) -> None:
        ...
    def AskSuppressExpTag(self, feature_tag: Tag, expression_tag: Tag) -> None:
        ...
    def AskSuppressFeature(self, feature: Tag, suppress: int) -> None:
        ...
    def AskSuppressList(self, feature_list: typing.List[Tag]) -> None:
        ...
    def AskSweep(self, feature_obj_id: Tag, s_guide: UF.StringList, s_section: UF.StringList, s_spine: UF.StringList, orientation: UF.MethodList, scaling: UF.MethodList, alignment: int, inter: int, body_type: int, tol: float) -> None:
        ...
    def AskSweepCurves(self, sweep_id: Tag, n_profile_curves: int, profile_curves: typing.List[Tag], n_guide_curves: int, guide_curves: typing.List[Tag]) -> None:
        ...
    def AskSweepDirection(self, feature_id: Tag, pos: float, dir: float) -> None:
        ...
    def AskSweepOfUdf(self, udf_eid: Tag, sweep_eid: Tag) -> None:
        ...
    def AskSweepParms(self, feature_obj_id: Tag, edit: int, taper_angle: str, limit1: str, limit2: str) -> None:
        ...
    def AskSymbThreadParms(self, thread_obj_id: Tag, parameters: UF.UFModl.SymbThreadData) -> None:
        ...
    def AskTSlotParms(self, feature_obj_id: Tag, edit: int, top_width: str, top_depth: str, bottom_width: str, bottom_depth: str, distance: str, thru_flag: int) -> None:
        ...
    def AskTaperFromEdges(self, feature_eid: Tag, type: int, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_edges: int, edges: typing.List[Tag], dist_tol: float, angle_tol: float) -> None:
        ...
    def AskTaperFromEdges1(self, feature_obj_id: Tag, taper_type: int, direction_tag: Tag, angle_str: str, taper_all_instances: bool, edge_collection: Tag, distance_tolerance: float, angle_tolerance: float) -> None:
        ...
    def AskTaperHoleParms(self, feature_obj_id: Tag, edit: int, diameter: str, taper_angle: str, depth: str, thru_flag: int) -> None:
        ...
    def AskTaperParms(self, feature_obj_id: Tag, edit: int, angle: str) -> None:
        ...
    def AskThickenSheetParms(self, thicken_sheet_tag: Tag, sheet_tag: Tag, first_offset: str, second_offset: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskThruCurves(self, feature_obj_id: Tag, s_section: UF.StringList, s_spine: UF.StringList, patch: int, alignment: int, value: float, vdegree: int, vstatus: int, body_type: int, tol: float, c_face_id: typing.List[Tag], c_flag: int) -> None:
        ...
    def AskThruCurves1(self, feature_obj_id: Tag, s_section: UF.StringList, s_spine: UF.StringList, patch: int, alignment: int, value: float, vdegree: int, vstatus: int, body_type: int, tol: float, c_collector_id: typing.List[Tag], c_flag: int) -> None:
        ...
    def AskThruFaces(self, feature_eid: Tag, face1: Tag, face2: Tag) -> None:
        ...
    def AskTimeStampOfFeature(self, feature: Tag, time_stamp: int) -> None:
        ...
    def AskTinyGeometry(self, obj_tag: Tag, tolerance: float, is_tiny: bool) -> None:
        ...
    def AskTorusParms(self, feature_tag: Tag, edit: int, major_diameter: str, minor_diameter: str) -> None:
        ...
    def AskUGrooveParms(self, feature_obj_id: Tag, edit: int, groove_dia: str, width: str, corner_rad: str) -> None:
        ...
    def AskUSlotParms(self, feature_obj_id: Tag, edit: int, width: str, depth: str, corner_rad: str, distance: str, thru_flag: int) -> None:
        ...
    def AskUdfDefinition(self, udf_tag: Tag, parents: typing.List[Tag], parents_prompt: str, num_parents: int, expression: typing.List[Tag], expression_prompt: str, num_expression: int) -> None:
        ...
    def AskUdfParms(self, feature_obj_id: Tag, udf_name: str, udf_prompt: str, udf_values: str, num_values: int) -> None:
        ...
    def AskUpdateErrorMessage(self, feature_id: Tag, error_message: str) -> None:
        ...
    def AskUpdateFailOption(self, current_option: UF.UFModl.UpdateOption) -> None:
        ...
    def AskUpdateUndoFeat(self, feat: Tag, feat_ifail: int) -> None:
        ...
    def AskUvPointsContainment(self, n_uvs: int, u_parms: float, v_parms: float, face_eid: Tag, pts_status: int) -> None:
        ...
    def AskVda4955Compliance(self, part: Tag, cfg_file_name: str, log_file_name: str, ceo_file_name: str) -> None:
        ...
    def AskVectorAngle(self, vector1: float, vector2: float, small_angle: float, large_angle: float) -> None:
        ...
    def AskVertDime(self, feature_obj_id: Tag, constraint: Tag, edit: int, _fixed: float, feature: float, fixc: float, feac: float, how_far: str, tool: Tag, part: Tag) -> None:
        ...
    def AskWrapAssembly(self, feature_tag: Tag, wrap_data: UF.UFModl.WrapAssem) -> None:
        ...
    def AskWrapGeometry(self, feature_tag: Tag, wrap_data: UF.UFModl.WrapGeom) -> None:
        ...
    def AskXformTagOfDatumCsys(self, datum_csys_tag: Tag) -> Tag:
        ...
    def AssignStringDirections(self, end_points: float, string_list1: UF.StringList) -> None:
        ...
    def AutoMidsrfFeature(self, feature_obj_id: Tag) -> None:
        ...
    def AutoMidsrfFeatureWOpts(self, feature_obj_id: Tag, autopairoptions: int, autoval: float) -> None:
        ...
    def BooleanUdf(self, udf_id: Tag, target_face: Tag, tool_face: Tag, tool_dir: float, num_target_faces: int, solid_target_faces: typing.List[Tag], num_tool_faces: int, solid_tool_faces: typing.List[Tag], included: bool, udf_meta_id: Tag) -> None:
        ...
    def BooleanUdf1(self, udf_id: Tag, target_face: Tag, tool_face: Tag, tool_dir: float, num_target_faces: int, target_faces: typing.List[Tag], num_tool_faces: int, tool_faces: typing.List[Tag], included: bool, target_body: Tag, flip: bool, udf_meta_id: Tag) -> None:
        ...
    def CalculateRefDir(self, feature_eid: Tag, face_eid: Tag, flip_face_normal: bool, ref_eid: Tag, ref_dir: float) -> None:
        ...
    def ChangeOffsetBaseFace(self, offset_feature: Tag, new_base_face: Tag) -> None:
        ...
    def CheckInterference(self, target: Tag, num_tools: int, tools: typing.List[Tag], results: int) -> None:
        ...
    def ClockInstance(self, feature_obj_id: Tag, clock_value1: str, clock_value2: str) -> None:
        ...
    def Compare(self, object1: Tag, object2: Tag, relation: int, equivalent: int) -> None:
        ...
    def CompareTopology(self, solid_object1: Tag, solid_object2: Tag, facet_tolerance: float, distance_tolerance: float, status: int) -> None:
        ...
    def ConvertToFixedDatum(self, datum_feature_tag: Tag) -> None:
        ...
    def CopyPasteFeatures(self, feature_array: typing.List[Tag], num_features: int, old_parents: typing.List[Tag], new_parents: typing.List[Tag], num_parents: int, expression_transfer_mode: int, parent_transfer_mode: int, new_feature_array: typing.List[Tag]) -> None:
        ...
    def Cre2dtrimBsurf(self, nu: int, nv: int, ku: int, kv: int, u_knot: float, v_knot: float, poles: float, loop_count: int, edge_counts: int, edge_senses: int, edge_bcurves: typing.List[Tag], edge_tol: float, bsurf_id: Tag, knot_fixup: int, pole_fixup: int) -> None:
        ...
    def CreChamferWithFlipOption(self, subtype: int, offset1: str, offset2: str, theta: str, edges: typing.List[Tag], flip_option: bool, feature_obj_id: Tag) -> None:
        ...
    def CreChamferWithInstanceAndFlipOption(self, subtype: int, offset1: str, offset2: str, theta: str, edges: typing.List[Tag], instance_option: bool, flip_option: bool, feature_obj_id: Tag) -> None:
        ...
    def CreDefFacepairFeat(self, midsrf_feature_obj_id: Tag, defining_face_1: Tag, defining_face_2: Tag, side_1: typing.List[Tag], side_2: typing.List[Tag], facepair_feature_obj_id: Tag) -> None:
        ...
    def CreSelFacepairFeat(self, midsrf_feature_obj_id: Tag, user_selected_midsurface: Tag, side_1: typing.List[Tag], side_2: typing.List[Tag], facepair_feature_obj_id: Tag) -> None:
        ...
    def CreTrimBsurf(self, nu: int, nv: int, ku: int, kv: int, u_knot: float, v_knot: float, poles: float, loop_count: int, edge_counts: int, edge_senses: int, edge_curves: typing.List[Tag], proj_curves: int, dist_tol: float, bsurf_id: Tag, knot_fixup: int, pole_fixup: int) -> None:
        ...
    def CreateBallGroove(self, location: float, direction: float, diame: str, width: str, face: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateBallSlot(self, location: float, tool_axis: float, direction: float, width: str, depth: str, distance: str, face_li: Tag, face_t1: Tag, face_t2: Tag, feature_tag: Tag) -> None:
        ...
    def CreateBendOperation(self, bend_data: UF.UFModl.BendOperationData, operation_tag: Tag) -> None:
        ...
    def CreateBlend(self, radius: str, edge_list: typing.List[Tag], smooth_overflow: int, cliff_overflow: int, notch_overflow: int, vrb_tool: float, feature_obj_id: Tag) -> None:
        ...
    def CreateBlendFaces(self, create_data: UF.UFModl.BlendFacesCreateData, limit_data: UF.UFModl.BlendFacesLimitData, feature_tag: Tag, num_bodies_created: int, bodies_created: typing.List[Tag], num_blend_faces: int, blend_faces: typing.List[Tag]) -> None:
        ...
    def CreateBlock(self, sign: UF.FeatureSigns, targ_tag: Tag, corner_pt: float, edge_len: str, blk_tag: Tag) -> None:
        ...
    def CreateBlock1(self, sign: UF.FeatureSigns, corner_pt: float, edge_len: str, blk_obj_id: Tag) -> None:
        ...
    def CreateBoss(self, location: float, direction: float, diame: str, height: str, angle: str, face: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateBplane(self, s_section: UF.StringList, tol: float, body_obj_id: Tag) -> None:
        ...
    def CreateBridgeFace(self, continuity_type: int, guide_type: int, primary_faces: typing.List[Tag], primary_edges: typing.List[Tag], primary_edges_dir: int, side_string1: UF.StringList, side_string2: UF.StringList, side_faces: typing.List[Tag], side_edges: typing.List[Tag], result_tag: Tag) -> None:
        ...
    def CreateBs2dEdges(self, nu: int, nv: int, ku: int, kv: int, u_knot: float, v_knot: float, poles: float, num_loops: int, edge_counts: int, edge_curves: typing.List[Tag], knot_fixup: int, pole_fixup: int) -> None:
        ...
    def CreateBsEdges(self, nu: int, nv: int, ku: int, kv: int, u_knot: float, v_knot: float, poles: float, num_loops: int, edge_counts: int, edge_curves: typing.List[Tag], knot_fixup: int, pole_fixup: int) -> None:
        ...
    def CreateBsurf(self, nu: int, nv: int, ku: int, kv: int, u_knot: float, v_knot: float, poles: float, bsurf_obj_id: Tag, knot_fixup: int, pole_fixup: int) -> None:
        ...
    def CreateBsurfThruPts(self, create_mode: int, u_closed_status: int, v_closed_status: int, u_degree: int, v_degree: int, num_rows: int, pts_info_per_row: typing.List[UF.UFModl.BsurfRowInfo], bsurf_obj_id: Tag) -> None:
        ...
    def CreateBsurface(self, surface: UF.UFModl.Bsurface, eid: Tag, num_states: int, states: typing.List[UF.UFCurve.State]) -> None:
        ...
    def CreateCBoreHole(self, location: float, direction: float, diameter1: str, depth1: str, diameter2: str, depth2: str, angle: str, face_li: Tag, face_t1: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateCSunkHole(self, location: float, direction: float, diameter1: str, depth1: str, diameter2: str, csink_angle: str, angle: str, face_li: Tag, face_t1: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateChamfer(self, subtype: int, offset1: str, offset2: str, theta: str, edges: typing.List[Tag], feature_obj_id: Tag) -> None:
        ...
    def CreateCircularIset(self, method: int, location: float, axis: float, number_str: str, angle_str: str, feature_list: typing.List[Tag], feature_obj_id: Tag) -> None:
        ...
    def CreateCircularPatternFace(self, region: UF.UFModl.DfoRegion, axis: Tag, n_pattern: int, angle: str, feature_tag: Tag) -> None:
        ...
    def CreateCone(self, sign: UF.FeatureSigns, targ_tag: Tag, origin: float, height: str, diam: str, direction: float, cone_tag: Tag) -> None:
        ...
    def CreateCone1(self, sign: UF.FeatureSigns, origin: float, height: str, diam: str, direction: float, cone_obj_id: Tag) -> None:
        ...
    def CreateCurveFromEdge(self, edge_id: Tag, ugcrv_id: Tag) -> None:
        ...
    def CreateCurveMesh(self, s_prim: UF.StringList, s_cross: UF.StringList, s_spine: UF.StringList, end_point: int, emphasis: int, body_type: int, spline_pts: int, boolean: UF.FeatureSigns, tol: float, c_face_id: typing.List[Tag], c_flag: int, body_obj_id: Tag) -> None:
        ...
    def CreateCyl1(self, sign: UF.FeatureSigns, origin: float, height: str, diam: str, direction: float, cyl_obj_id: Tag) -> None:
        ...
    def CreateCylPocket(self, location: float, direction: float, diame: str, depth: str, radius: str, angle: str, face: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateCylinder(self, sign: UF.FeatureSigns, targ_tag: Tag, origin: float, height: str, diam: str, direction: float, cyl_tag: Tag) -> None:
        ...
    def CreateDatumCsys(self, object_in_part: Tag, xform_tag: Tag, create_components: bool, datum_csys_feature: Tag) -> None:
        ...
    def CreateDatumCsysOffset(self, object_in_part: Tag, parent_datum_csys_tag: Tag, linear_offset: float, angular_offset: float, create_components: bool, datum_csys_tag: Tag) -> None:
        ...
    def CreateDoveTailSlot(self, location: float, tool_axis: float, direction: float, width: str, depth: str, angle: str, distance: str, face_li: Tag, face_t1: Tag, face_t2: Tag, feature_tag: Tag) -> None:
        ...
    def CreateEdgeBlend(self, blend_data: UF.UFModl.EdgeBlendData, blend_eid: Tag) -> None:
        ...
    def CreateEnlarge(self, face: Tag, type: int, percent_size: str, tolerance: float, feat_obj_tag: Tag) -> None:
        ...
    def CreateExp(self, expr_str: str) -> None:
        ...
    def CreateExpTag(self, _string: str, new_exp: Tag) -> None:
        ...
    def CreateExtrudeTrimOpts(self, extrude_array: typing.List[Tag], extrude_count: int, trim_ptr: UF.ModlSweepTrimObject, trim_options: UF.ModlSweepTrimOpts, taper_angle: str, limits: str, offsets: str, region_point: float, cut_specified: bool, solid_body_creation: bool, dir: float, sign: UF.FeatureSigns, objects: typing.List[Tag], object_count: int) -> None:
        ...
    def CreateExtrudeTrimOpts1(self, extrude_array: typing.List[Tag], extrude_count: int, trim_ptr: UF.ModlSweepTrimObject, trim_options: UF.ModlSweepTrimOpts, taper_angle: str, limits: str, offsets: str, region_point: float, cut_specified: bool, solid_body_creation: bool, dir: float, sign: UF.FeatureSigns, target_body: Tag, objects: typing.List[Tag], object_count: int) -> None:
        ...
    def CreateExtruded(self, objects: typing.List[Tag], taper_angle: str, limit: str, point: float, direction: float, sign: UF.FeatureSigns, features: typing.List[Tag]) -> None:
        ...
    def CreateExtruded1(self, objects: typing.List[Tag], taper_angle: str, limit: str, point: float, direction: float, sign: UF.FeatureSigns, target_body: Tag, features: typing.List[Tag]) -> None:
        ...
    def CreateExtruded2(self, objects: typing.List[Tag], taper_angle: str, limit: str, point: float, direction: float, sign: UF.FeatureSigns, features: typing.List[Tag]) -> None:
        ...
    def CreateExtrudedPath(self, objects: typing.List[Tag], path_objects: typing.List[Tag], point: float, direction: float, sign: UF.FeatureSigns, features: typing.List[Tag]) -> None:
        ...
    def CreateExtrudedPath1(self, objects: typing.List[Tag], path_objects: typing.List[Tag], point: float, direction: float, sign: UF.FeatureSigns, target_body: Tag, features: typing.List[Tag]) -> None:
        ...
    def CreateExtrusion(self, objects: typing.List[Tag], object_count: int, trim_data: UF.ModlSweepTrimObject, taper_angle: str, limits: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, direction: float, sign: UF.FeatureSigns, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateExtrusion1(self, objects: typing.List[Tag], object_count: int, trim_data: UF.ModlSweepTrimObject, taper_angle: str, limits: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, direction: float, sign: UF.FeatureSigns, target_body: Tag, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateExtrusion2(self, objects: typing.List[Tag], object_count: int, trim_data: UF.ModlSweepTrimObject, taper_angle: str, limits: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, direction: float, sign: UF.FeatureSigns, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateExtrusionDefault(self, extrude_array: typing.List[Tag], extrude_count: int, trim_ptr: UF.ModlSweepTrimObject, trim_options: UF.ModlSweepTrimOpts, taper_angle: str, limits: str, offsets: str, region_point: float, cut_specified: bool, solid_body_creation: bool, sketch_eid: Tag, reverse_default: bool, sign: UF.FeatureSigns, objects: typing.List[Tag], object_count: int) -> None:
        ...
    def CreateExtrusionDefault1(self, extrude_array: typing.List[Tag], extrude_count: int, trim_ptr: UF.ModlSweepTrimObject, trim_options: UF.ModlSweepTrimOpts, taper_angle: str, limits: str, offsets: str, region_point: float, cut_specified: bool, solid_body_creation: bool, sketch_eid: Tag, reverse_default: bool, sign: UF.FeatureSigns, target_body: Tag, objects: typing.List[Tag], object_count: int) -> None:
        ...
    def CreateExtrusionDir(self, extrude_array: typing.List[Tag], extrude_count: int, trim_ptr: UF.ModlSweepTrimObject, trim_options: UF.ModlSweepTrimOpts, taper_angle: str, limits: str, offsets: str, region_point: float, cut_specified: bool, solid_body_creation: bool, datum_eid: Tag, sign: UF.FeatureSigns, objects: typing.List[Tag], object_count: int) -> None:
        ...
    def CreateExtrusionPath(self, objects: typing.List[Tag], object_count: int, path_objects: typing.List[Tag], path: int, trim_data: UF.ModlSweepTrimObject, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, sign: UF.FeatureSigns, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateExtrusionPath1(self, objects: typing.List[Tag], object_count: int, path_objects: typing.List[Tag], path: int, trim_data: UF.ModlSweepTrimObject, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, sign: UF.FeatureSigns, target_body: Tag, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateFaceConstraint(self, region: UF.UFModl.DfoRegion, constraint: UF.UFModl.DfoConstraint, feature_tag: Tag) -> None:
        ...
    def CreateFaceOffset(self, offset: str, faces: typing.List[Tag], feature_obj_id: Tag) -> None:
        ...
    def CreateFaceTaper(self, location: float, direction: float, angle: str, faces: typing.List[Tag], feature_obj_id: Tag) -> None:
        ...
    def CreateFeatureOffset(self, offset: str, features: typing.List[Tag], feature_obj_id: Tag) -> None:
        ...
    def CreateFeatureTaper(self, location: float, direction: float, angle: str, original_feature: Tag, taper_feature: Tag) -> None:
        ...
    def CreateFittedSpline(self, spline_data: UF.SplineFit, max_err: float, max_err_pt: int, obj_id: Tag) -> None:
        ...
    def CreateFixedDaxis(self, point1: float, point2: float, daxis_tag: Tag) -> None:
        ...
    def CreateFixedDplane(self, point: float, direction: float, dplane_tag: Tag) -> None:
        ...
    def CreateFlange(self, orig: float, xdir: float, zdir: float, face: Tag, edge: Tag, thick: str, width: str, angle: str, length: str, radius: str, taper_l: str, taper_r: str, ang_tgl: int, len_tgl: int, rad_tgl: int, flange: Tag) -> None:
        ...
    def CreateFrenetDaxis(self, curve_tag: Tag, direction_tag: Tag, perc_string: str, direction_type: int, daxis_feid: Tag) -> None:
        ...
    def CreateGeodesicCurves(self, number_of_faces: int, face_eids: typing.List[Tag], start_pnt: float, start_dir: float, length: float, dist_tol: float, geodesiccurve_id: typing.List[Tag], geodesiccurve_cnt: int, achieved_length: float) -> None:
        ...
    def CreateHollow(self, thickness: str, faces: typing.List[Tag], feature_obj_id: Tag) -> None:
        ...
    def CreateImprFaces(self, parms: UF.UFModl.ImprintFacesData, feature_tag: Tag) -> None:
        ...
    def CreateImprLoop(self, parms: UF.UFModl.ImprintLoopData, feature_tag: Tag) -> None:
        ...
    def CreateInsetFlange(self, attach_face: Tag, reference_edge: Tag, position: float, xdirection: float, zdirection: float, parameters: UF.UFModl.InsetFlangeData, feature_tag: Tag) -> None:
        ...
    def CreateInstantiatedUdf(self, udf_definition_tag: Tag, cgm_file_name: str, old_parents: typing.List[Tag], new_parents: typing.List[Tag], num_parents: int, old_expression: typing.List[Tag], new_expression_value: str, num_expression: int, new_udf: Tag) -> None:
        ...
    def CreateIsoclineCurves(self, face_id: Tag, direction: float, angle: float, dist_tol: float, isocurve_id: typing.List[Tag], isocurve_cnt: int) -> None:
        ...
    def CreateIsocurve(self, face_id: Tag, uv_flag: int, parameter: float, dist_tol: float, isocurve_id: typing.List[Tag], isocurve_cnt: int) -> None:
        ...
    def CreateLaw(self, law_method: int, law_str1: str, law_str2: str, spine_str: UF.StringList, law_cv_str: UF.StringList, num_spine_points: int, spine_xyz: float, spine_values: float, base_line_tag: Tag, base_direction: int, uf_law_parms: int) -> None:
        ...
    def CreateLawExtension(self, law_extension_data: UF.UFModl.LawextData, law_extension: Tag) -> None:
        ...
    def CreateLinearIset(self, method: int, number_in_x: str, distance_x: str, number_in_y: str, distance_y: str, feature_list: typing.List[Tag], feature_obj_id: Tag) -> None:
        ...
    def CreateLinkedExterior(self, ext_data: UF.UFModl.LinkedExt, feature_tag: Tag) -> None:
        ...
    def CreateList(self, list: typing.List[Tag]) -> None:
        ...
    def CreateLocalScale(self, type: UF.UFModl.DfoScaleType, region: UF.UFModl.DfoRegion, so_point: Tag, so_dir: Tag, so_csys: Tag, factors: str, feature_tag: Tag) -> None:
        ...
    def CreateMidsrfFeature(self, target_body: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateMirrorBody(self, body: Tag, datum_plane: Tag, mirrored_body: Tag) -> None:
        ...
    def CreateMirrorPatternFace(self, region: UF.UFModl.DfoRegion, mirror_plane: Tag, feature_tag: Tag) -> None:
        ...
    def CreateMirrorSet(self, features: typing.List[Tag], number_of_feature: int, mirror_plane: Tag, mirror_set: Tag) -> None:
        ...
    def CreateMoveRegion(self, type: UF.UFModl.TransformType, region: UF.UFModl.DfoRegion, transf_data: int, feature_tag: Tag) -> None:
        ...
    def CreateMultiTransitionLaw(self, spine: UF.StringList, num_pts: int, pt_xyzs: float, pt_law_values: str, pt_trans_types: int, uf_law_parms: int) -> None:
        ...
    def CreateMultipleSews(self, target_sheet: Tag, num_tools: int, tools_sheet: typing.List[Tag], tolerance: float, disjoint_list: typing.List[Tag], sew_list: typing.List[Tag]) -> None:
        ...
    def CreateNonUniScale(self, body_eid: Tag, csys_type: int, scale_factors: str, feature_eid: Tag) -> None:
        ...
    def CreateOffsetRegion(self, region: UF.UFModl.DfoRegion, offset: str, feature_tag: Tag) -> None:
        ...
    def CreatePlane(self, origin_point: float, plane_normal: float, plane_tag: Tag) -> None:
        ...
    def CreatePointDirrDaxis(self, point: Tag, direction: Tag, daxis_tag: Tag) -> None:
        ...
    def CreatePointDirrDplane(self, point: Tag, direction: Tag, dplane_tag: Tag) -> None:
        ...
    def CreatePointsFeature(self, num_points: int, points: typing.List[Tag], feature_tag: Tag) -> None:
        ...
    def CreateProjCurves(self, curve_refs: typing.List[Tag], face_refs: typing.List[Tag], along_face_normal: int, proj_vector: float, proj_curve_feature: Tag) -> None:
        ...
    def CreatePromotion(self, body_occ: Tag, feature_tag: Tag) -> None:
        ...
    def CreateReblendFace(self, reblend_data: UF.UFModl.ReblendFaceData, reblend_eid: Tag) -> None:
        ...
    def CreateRectGroove(self, location: float, direction: float, diame: str, width: str, face: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateRectPad(self, location: float, direction: float, x_dir: float, size: str, radius: str, angle: str, face: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateRectPocket(self, location: float, direction: float, x_dir: float, len: str, corner: str, floor: str, angle: str, face: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateRectSlot(self, location: float, tool_axis: float, direction: float, width: str, depth: str, distance: str, face_li: Tag, face_t1: Tag, face_t2: Tag, feature_tag: Tag) -> None:
        ...
    def CreateRectangularPatternFace(self, region: UF.UFModl.DfoRegion, x_axis: Tag, y_axis: Tag, num_x: int, num_y: int, x_offset: str, y_offset: str, feature_tag: Tag) -> None:
        ...
    def CreateRefitFaceFeature(self, refit_data: UF.UFModl.RefitFaceData, refit: Tag) -> None:
        ...
    def CreateRelativeDaxis(self, num_refs: int, obj_eids: typing.List[Tag], point_select: int, daxis_feid: Tag) -> None:
        ...
    def CreateRelativeDplane(self, num_refs: int, object_tags: typing.List[Tag], point_select: int, which_plane: int, reference_point: float, angle_string: str, offset_string: str, num_dplanes: int, dplane_tag: typing.List[Tag]) -> None:
        ...
    def CreateReparamSheet(self, proj_type: int, drv_type: int, check_overlap: int, num_primary: int, prim_cvs: typing.List[Tag], num_cross: int, cros_cvs: typing.List[Tag], proj_vec: float, num_fs: int, faces: typing.List[Tag], tols: float, new_face: Tag, tol_achieved: int) -> None:
        ...
    def CreateReplaceFace(self, target_faces: typing.List[Tag], num_target: int, non_blend_faces: typing.List[Tag], num_non_blend: int, tool_face: Tag, reverse_direction: bool, feature_tag: Tag) -> None:
        ...
    def CreateResizeFace(self, target_faces: typing.List[Tag], num_target: int, non_blend_faces: typing.List[Tag], num_non_blend: int, new_parameter: str, feature_tag: Tag) -> None:
        ...
    def CreateReverseNormal(self, sheet_body_tag: Tag, option_flag: int, reverse_normal_tag: Tag) -> None:
        ...
    def CreateRevolution(self, objects: typing.List[Tag], _object: int, trim_data: UF.ModlSweepTrimObject, limit: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, axis_point: float, direction: float, sign: UF.FeatureSigns, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateRevolution1(self, objects: typing.List[Tag], _object: int, trim_data: UF.ModlSweepTrimObject, limit: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, axis_point: float, direction: float, sign: UF.FeatureSigns, target_body: Tag, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateRevolutionDir(self, objects: typing.List[Tag], _object: int, trim_data: UF.ModlSweepTrimObject, limit: str, offsets: str, region_point: float, region_specified: bool, solid_creation: bool, datum_tag: Tag, sign: UF.FeatureSigns, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateRevolved(self, obj_id_list: typing.List[Tag], limit: str, point: float, direction: float, sign: UF.FeatureSigns, feature_list: typing.List[Tag]) -> None:
        ...
    def CreateRevolved1(self, obj_id_list: typing.List[Tag], limit: str, point: float, direction: float, sign: UF.FeatureSigns, target_body: Tag, feature_list: typing.List[Tag]) -> None:
        ...
    def CreateRipedge(self, ripedge_ufdata: UF.UFModl.RipedgeData, ripedge_tag: Tag) -> None:
        ...
    def CreateRoughOffset(self, parms: UF.UFModl.RoughOffset, feature_tag: Tag) -> None:
        ...
    def CreateRpoConstraints(self, feature_obj_id: Tag, horz_dir_obj_id: Tag, vert_dir_obj_id: Tag, obj_id_target: typing.List[Tag], target_qualifier: int, obj_id_tool: typing.List[Tag], tool_qualifier: int, constraint_value: str, constraint_array: str, num_of_constrnts: int) -> None:
        ...
    def CreateRuled(self, s_section: UF.StringList, s_spine: UF.StringList, alignment: int, value: float, end_point: int, body_type: int, boolean: UF.FeatureSigns, tol: float, body_obj_id: Tag) -> None:
        ...
    def CreateRuled1(self, s_section: UF.StringList, s_spine: UF.StringList, alignment: int, value: float, end_point: int, body_type: int, boolean: UF.FeatureSigns, target_body: Tag, tol: float, body_obj_id: Tag) -> None:
        ...
    def CreateScale(self, type: UF.ScaleType, body_tags: typing.List[Tag], num_body_tags: int, so_point: Tag, so_dir: Tag, so_csys: Tag, factors: str, tags: typing.List[Tag]) -> None:
        ...
    def CreateSetOfFeature(self, name: str, features: typing.List[Tag], number_of_feature: int, hide_state: int, feature: Tag) -> None:
        ...
    def CreateSew(self, option: int, num_targets: int, targets: typing.List[Tag], num_tools: int, tools: typing.List[Tag], tolerance: float, type_body: int, disjoint_list: typing.List[Tag], sew_id: Tag) -> None:
        ...
    def CreateSilhouetteFlange(self, sflange_data: UF.UFModl.SflangeData, sflange_tag: Tag) -> None:
        ...
    def CreateSilhouetteFlangePipe(self, sflange_data: UF.UFModl.SflangeData, centerline_tag: Tag) -> None:
        ...
    def CreateSimpleHole(self, location: float, direction: float, diame: str, depth: str, angle: str, face_li: Tag, face_t1: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateSimplifiedCurve(self, curve_count: int, curves: typing.List[Tag], tolerance: float, segment_count: int, segments: typing.List[Tag]) -> None:
        ...
    def CreateSimplify(self, simpl_parms: UF.UFModl.SimplData, feature_tag: Tag, n_failing_wound_edges: int, failing_wound_edges: typing.List[Tag], n_retained_faces: int, n_removed_faces: int) -> None:
        ...
    def CreateSmbend(self, user_data: UF.UFModl.SmbendData, bend_tag: Tag) -> None:
        ...
    def CreateSmbendCorner(self, user_data: UF.UFModl.SmbendCornerData, bend_tag: Tag) -> None:
        ...
    def CreateSmbendCylinder(self, user_data: UF.UFModl.SmbendCylinderData, bend_tag: Tag) -> None:
        ...
    def CreateSmcorner(self, smcorner_ufdata: UF.UFModl.SmcornerData, smcorner_tag: Tag) -> None:
        ...
    def CreateSmcutout(self, user_data: UF.UFModl.SmcutoutData, cutout_tag: Tag) -> None:
        ...
    def CreateSmdFlange(self, attach_face: Tag, reference_edge: Tag, position: float, xdirection: float, zdirection: float, flange_data: UF.UFModl.FlangeData, feature_tag: Tag) -> None:
        ...
    def CreateSmhole(self, user_data: UF.UFModl.SmholeData, hole_tag: Tag) -> None:
        ...
    def CreateSmjoggle(self, joggle_data: UF.UFModl.SmjoggleData, joggle: Tag) -> None:
        ...
    def CreateSmpunch(self, user_data: UF.UFModl.SmpunchData, punch_tag: Tag) -> None:
        ...
    def CreateSmrelief(self, user_data: UF.UFModl.SmreliefData) -> None:
        ...
    def CreateSmslot(self, user_data: UF.UFModl.SmslotData, slot_tag: Tag) -> None:
        ...
    def CreateSnipSurfaceFeature(self, usr_data: UF.UFModl.SnipsrfFeatureData, snip_tag: Tag) -> None:
        ...
    def CreateSolidPunch(self, smspunch_ufdata: UF.UFModl.SolidPunchData, smspunch_tag: Tag) -> None:
        ...
    def CreateSphere(self, sign: UF.FeatureSigns, targ_tag: Tag, center: float, diam: str, sphere_tag: Tag) -> None:
        ...
    def CreateSphere1(self, sign: UF.FeatureSigns, center: float, diam: str, sphere_obj_id: Tag) -> None:
        ...
    def CreateSpline(self, nc: int, kc: int, knot: float, poles: float, spline_id: Tag, knot_fixup: int, pole_fixup: int) -> None:
        ...
    def CreateStringList(self, num_string: int, num_object: int, string_list1: UF.StringList) -> None:
        ...
    def CreateStycorner(self, styled_corner_data: UF.UFModl.StycornerData, frec_tag: Tag) -> None:
        ...
    def CreateSubdivFace(self, curve_refs: typing.List[Tag], count: int, face: Tag, proj_type: int, vector: float, feature_obj_id: Tag) -> None:
        ...
    def CreateSurfFromCloud(self, point_cnt: int, cloud: float, csys_matrix: float, bnd_corners: float, U_degree: int, V_degree: int, U_patches: int, V_patches: int, corner_switch: int, average_error: float, max_error: float, max_error_index: int, surface_tag: Tag) -> None:
        ...
    def CreateSweep(self, s_guide: UF.StringList, s_section: UF.StringList, s_spine: UF.StringList, orientation: UF.MethodList, scaling: UF.MethodList, alignment: int, inter: int, body_type: int, boolean: UF.FeatureSigns, tol: float, body_obj_id: Tag) -> None:
        ...
    def CreateSymbThread(self, parameters: UF.UFModl.SymbThreadData, thread_obj_id: Tag) -> None:
        ...
    def CreateSymbThread2(self, parameters: UF.UFModl.SymbThreadData, internal_thread: bool, thread_obj_id: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateTSlot(self, location: float, tool_axis: float, direction: float, t_width: str, t_depth: str, b_width: str, b_depth: str, distance: str, face_li: int, face_t1: int, face_t2: int, feature_tag: Tag) -> None:
        ...
    def CreateTaperFromEdges(self, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_edges: int, edges: typing.List[Tag], feature_tag: Tag) -> None:
        ...
    def CreateTaperFromFaces(self, point_tag: Tag, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_faces: int, faces: typing.List[Tag], feature_tag: Tag) -> None:
        ...
    def CreateTaperFromTangentFaces(self, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_faces: int, faces: typing.List[Tag], feature_eid: Tag) -> None:
        ...
    def CreateTaperSplitLine(self, point_tag: Tag, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_edges: int, edges: typing.List[Tag], dist_tol: float, angle_tol: float, feature_tag: Tag) -> None:
        ...
    def CreateThickenSheet(self, sheet_body_tag: Tag, first_offset: str, second_offset: str, sign: UF.FeatureSigns, thicken_sheet_tag: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateThruCurves(self, s_section: UF.StringList, s_spine: UF.StringList, patch: int, alignment: int, value: float, vdegree: int, vstatus: int, body_type: int, boolean: UF.FeatureSigns, tol: float, c_face_id: typing.List[Tag], c_flag: int, body_obj_id: Tag) -> None:
        ...
    def CreateTrimmedTube(self, objects: typing.List[Tag], object_count: int, trim_data: UF.ModlSweepTrimObject, diameters: str, sign: UF.FeatureSigns, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateTrimmedTube1(self, objects: typing.List[Tag], object_count: int, trim_data: UF.ModlSweepTrimObject, diameters: str, sign: UF.FeatureSigns, target_body: Tag, features: typing.List[Tag], number_of_features: int) -> None:
        ...
    def CreateTrueTaperFromEdges(self, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_edges: int, edges: typing.List[Tag], dist_tol: float, angle_tol: float, feature_eid: Tag) -> None:
        ...
    def CreateTube(self, path_list: typing.List[Tag], limit: str, sign: UF.FeatureSigns, feature_list: typing.List[Tag]) -> None:
        ...
    def CreateTube1(self, path_list: typing.List[Tag], limit: str, sign: UF.FeatureSigns, target_body: Tag, feature_list: typing.List[Tag]) -> None:
        ...
    def CreateUGroove(self, location: float, direction: float, diame: str, width: str, corner: str, face: Tag, feature_obj_id: Tag) -> None:
        ...
    def CreateUSlot(self, location: float, tool_axis: float, direction: float, width: str, depth: str, radius: str, distance: str, face_li: Tag, face_t1: Tag, face_t2: Tag, feature_tag: Tag) -> None:
        ...
    def CreateUniformScale(self, body_eid: Tag, csys_type: int, scale_factor: str, feature_eid: Tag) -> None:
        ...
    def CreateVariableHollow(self, tolerance: float, thickness: str, n_pierced_faces: int, pierced_faces: typing.List[Tag], n_boundary_faces: int, boundary_faces: typing.List[Tag], n_offset_faces: int, offset_faces: typing.List[Tag], offset_thickness: str, feature_id: Tag) -> None:
        ...
    def CreateVariableOffset(self, base_sheet: Tag, dist: str, uv_param: float, varoff_sheet: Tag) -> None:
        ...
    def CreateVariableTaperFromEdges(self, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_edges: int, edges: typing.List[Tag], num_points: int, points: float, angles: str, dist_tol: float, angle_tol: float, feature_tag: Tag) -> None:
        ...
    def CreateWrapAssembly(self, wrap_data: UF.UFModl.WrapAssem, feature_tag: Tag) -> None:
        ...
    def CreateWrapGeometry(self, wrap_data: UF.UFModl.WrapGeom, feature_tag: Tag) -> None:
        ...
    def DefaultRpoMenu(self, feature_eid: Tag) -> int:
        ...
    def DeleteBodyParms(self, body_list: typing.List[Tag]) -> None:
        ...
    def DeleteExp(self, exp_name: str) -> None:
        ...
    def DeleteExpTag(self, old_exp: Tag) -> None:
        ...
    def DeleteFeature(self, cmtags: typing.List[Tag]) -> None:
        ...
    def DeleteObjectParms(self, object_list: typing.List[Tag]) -> None:
        ...
    def DevchkAdjacentEdges(self, num_faces: int, faces: typing.List[Tag], tolerances: float, num_chk_points: int, num_devs: int, devs: typing.List[UF.UFModl.DevchkEeInfo]) -> None:
        ...
    def DevchkCurveToCurve(self, curve1_id: Tag, curve2_id: Tag, num_of_check_points: int, check_result: UF.UFModl.DeviationCheckData) -> int:
        ...
    def DevchkCurveToFace(self, curve_id: Tag, face_id: Tag, num_of_check_points: int, check_result: UF.UFModl.DeviationCheckData) -> int:
        ...
    def DevchkEdgeToEdge(self, edge1_id: Tag, face_of_edge1_id: Tag, edge2_id: Tag, face_of_edge2_id: Tag, num_of_check_points: int, check_result: UF.UFModl.DeviationCheckData) -> int:
        ...
    def DevchkEdgeToFace(self, edge_id: Tag, face_of_edge_id: Tag, second_face_id: Tag, num_of_check_points: int, check_result: UF.UFModl.DeviationCheckData) -> int:
        ...
    def DevchkFaceToFace(self, face1_id: Tag, face2_id: Tag, num_check_points_u: int, num_check_points_v: int, check_result: UF.UFModl.DeviationCheckData) -> int:
        ...
    def DissectExpString(self, exp_str: str, lhs_str: str, rhs_str: str, exp_tag: Tag) -> None:
        ...
    def DumpMidsurfFacepairReport(self, file_name_with_extn: str, midsrf_feature_obj_id: Tag) -> None:
        ...
    def EditBendAllowanceFormula(self, feature_tag: Tag, exp_str: str) -> None:
        ...
    def EditBendOperation(self, operation_tag: Tag, bend_data: UF.UFModl.BendOperationData) -> None:
        ...
    def EditBooleanWithRetainedOptions(self, feature_eid: Tag, new_target: Tag, new_tool: Tag) -> None:
        ...
    def EditBsurf(self, face_eid: Tag, bsurf: UF.UFModl.Bsurface) -> None:
        ...
    def EditCircularIset(self, feature_obj_id: Tag, number_str: str, angle_str: str, radius_str: str, rotation_point_id: Tag) -> None:
        ...
    def EditCircularPatternFace(self, feature_tag: Tag, region: UF.UFModl.DfoRegion, axis: Tag, n_pattern: int, angle: str) -> None:
        ...
    def EditDatumDirection(self, datum_feature_tag: Tag, new_direction: Tag) -> None:
        ...
    def EditDatumPoint(self, datum_feature_tag: Tag, new_point: Tag) -> None:
        ...
    def EditEdgeBlend(self, feature_eid: Tag, blend_data: UF.UFModl.EdgeBlendData) -> None:
        ...
    def EditEnlarge(self, feat_obj_tag: Tag, type: int, percent_size: str, tolerance: float) -> None:
        ...
    def EditExp(self, expr_str: str) -> None:
        ...
    def EditFaceConstraint(self, feature_tag: Tag, region: UF.UFModl.DfoRegion, constraint: UF.UFModl.DfoConstraint) -> None:
        ...
    def EditFaceGridCount(self, _object: Tag, u_count: int, v_count: int) -> None:
        ...
    def EditFaceJoin(self, opt: int, body_tag: Tag, face_tags: typing.List[Tag], result_tag: Tag) -> None:
        ...
    def EditFormableFeatureState(self, feature_tag: Tag, state: UF.UFModl.State, state_info: UF.UFModl.StateInfo) -> None:
        ...
    def EditHoleType(self, hole_feature: Tag, new_hole_type: UF.UFModl.HoleType) -> None:
        ...
    def EditHollow(self, feature_id: Tag, type: int, tolerance: float, thickness: str, n_pierced_faces: int, pierced_faces: typing.List[Tag], n_boundary_faces: int, boundary_faces: typing.List[Tag], n_offset_faces: int, offset_faces: typing.List[Tag], offset_thickness: str) -> None:
        ...
    def EditImportBodyFeature(self, input_tag: Tag, edit_option: UF.UFModl.ImportBodyFeatureEditOption, import_body_filename: str) -> None:
        ...
    def EditImportBodyFeatures(self, edit_option: UF.UFModl.ImportBodyFeatureEditOption) -> None:
        ...
    def EditImprFacesParms(self, feature_tag: Tag, parms: UF.UFModl.ImprintFacesData) -> None:
        ...
    def EditImprLoopParms(self, feature_tag: Tag, parms: UF.UFModl.ImprintLoopData) -> None:
        ...
    def EditInsetFlange(self, feature_tag: Tag, parameters: UF.UFModl.InsetFlangeData) -> None:
        ...
    def EditLawExtension(self, law_extension_data: UF.UFModl.LawextData, law_extension: Tag) -> None:
        ...
    def EditLinearIset(self, feature_obj_id: Tag, number_in_x: str, distance_x: str, number_in_y: str, distance_y: str) -> None:
        ...
    def EditLinkedExterior(self, feature_tag: Tag, ext_data: UF.UFModl.LinkedExt) -> None:
        ...
    def EditLocalScale(self, feature_tag: Tag, type: UF.UFModl.DfoScaleType, region: UF.UFModl.DfoRegion, so_point: Tag, so_dir: Tag, so_csys: Tag, factors: str) -> None:
        ...
    def EditMirrorPatternFace(self, feature_tag: Tag, region: UF.UFModl.DfoRegion, mirror_plane: Tag) -> None:
        ...
    def EditMirrorSet(self, mirror_set: Tag, features: typing.List[Tag], number_of_features: int, mirror_plane: Tag) -> None:
        ...
    def EditMoveRegion(self, feature_tag: Tag, type: UF.UFModl.TransformType, region: UF.UFModl.DfoRegion, transf_data: int) -> None:
        ...
    def EditOffsetRegion(self, feature_tag: Tag, region: UF.UFModl.DfoRegion, offset: str) -> None:
        ...
    def EditPatchBodyParms(self, feature: Tag, new_target: Tag, new_tool: Tag, new_face: Tag, new_reverse: int) -> None:
        ...
    def EditPlane(self, plane_tag: Tag, origin_point: float, plane_normal: float) -> None:
        ...
    def EditPointsParms(self, feature_tag: Tag, num_points: int, points: typing.List[Tag]) -> None:
        ...
    def EditReblendFace(self, feature_eid: Tag, reblend_data: UF.UFModl.ReblendFaceData) -> None:
        ...
    def EditRectangularPatternFace(self, feature_tag: Tag, region: UF.UFModl.DfoRegion, x_axis: Tag, y_axis: Tag, num_x: int, num_y: int, x_offset: str, y_offset: str) -> None:
        ...
    def EditRefitFaceFeature(self, refit_data: UF.UFModl.RefitFaceData, refit: Tag) -> None:
        ...
    def EditReplaceFace(self, feature_tag: Tag, target_faces: typing.List[Tag], num_target: int, non_blend_faces: typing.List[Tag], num_non_blend: int, tool_face: Tag, reverse_direction: bool) -> None:
        ...
    def EditResizeFace(self, feature_tag: Tag, target_faces: typing.List[Tag], num_target: int, non_blend_faces: typing.List[Tag], num_non_blend: int, new_parameter: str) -> None:
        ...
    def EditRipedge(self, ripedge_tag: Tag, ripedge_ufdata: UF.UFModl.RipedgeData) -> None:
        ...
    def EditRoughOffset(self, feature_tag: Tag, parms: UF.UFModl.RoughOffset) -> None:
        ...
    def EditScale(self, type: UF.ScaleType, tag: Tag, so_point: Tag, so_dir: Tag, so_csys: Tag, factors: str) -> None:
        ...
    def EditSetHideState(self, set: Tag, hide_state: int) -> None:
        ...
    def EditSetMembers(self, set: Tag, features: typing.List[Tag], number_of_feature: int) -> None:
        ...
    def EditSewSheetBody(self, feature_obj_eid: Tag, new_target_eid: Tag, tool_body_count: int, tool_body_eids: typing.List[Tag], tolerance: float) -> None:
        ...
    def EditSewSolidBody(self, feature_obj_eid: Tag, target_faces_count: int, target_faces: typing.List[Tag], tool_faces_count: int, tool_faces: typing.List[Tag], tolerance: float) -> None:
        ...
    def EditSilhouetteFlange(self, sflange_data: UF.UFModl.SflangeData, sflange_tag: Tag) -> None:
        ...
    def EditSimplifyParms(self, feature_tag: Tag, simpl_parms: UF.UFModl.SimplData, n_failing_wound_edges: int, failing_wound_edges: typing.List[Tag]) -> None:
        ...
    def EditSlotType(self, slot_feature: Tag, new_slot_type: UF.UFModl.SlotType) -> None:
        ...
    def EditSmbend(self, bend_tag: Tag, user_data: UF.UFModl.SmbendData) -> None:
        ...
    def EditSmbendCorner(self, bend_tag: Tag, user_data: UF.UFModl.SmbendCornerData) -> None:
        ...
    def EditSmbendCylinder(self, bend_tag: Tag, user_data: UF.UFModl.SmbendCylinderData) -> None:
        ...
    def EditSmcorner(self, smcorner_tag: Tag, smcorner_ufdata: UF.UFModl.SmcornerData) -> None:
        ...
    def EditSmcutout(self, cutout_tag: Tag, user_data: UF.UFModl.SmcutoutData) -> None:
        ...
    def EditSmdFlange(self, feature_tag: Tag, parameters: UF.UFModl.FlangeData) -> None:
        ...
    def EditSmhole(self, hole_tag: Tag, user_data: UF.UFModl.SmholeData) -> None:
        ...
    def EditSmpunch(self, user_data: UF.UFModl.SmpunchData, punch_tag: Tag) -> None:
        ...
    def EditSmslot(self, slot_tag: Tag, user_data: UF.UFModl.SmslotData) -> None:
        ...
    def EditSnipSurfaceFeature(self, usr_data: UF.UFModl.SnipsrfFeatureData, snip: Tag) -> None:
        ...
    def EditSolidPunch(self, smspunch_tag: Tag, smspunch_ufdata: UF.UFModl.SolidPunchData) -> None:
        ...
    def EditStycorner(self, styled_corner_data: UF.UFModl.StycornerData, frec_tag: Tag) -> None:
        ...
    def EditSubdivFace(self, edit_flag: int, feature_obj_id: Tag, remove_curve: Tag, add_curve: Tag, vector: float) -> None:
        ...
    def EditSweepCurves(self, sweep_id: Tag, n_profile_curves_removed: int, profile_curves_removed: typing.List[Tag], n_profile_curves_added: int, profile_curves_added: typing.List[Tag], n_guide_curves_removed: int, guide_curves_removed: typing.List[Tag], n_guide_curves_added: int, guide_curves_added: typing.List[Tag]) -> None:
        ...
    def EditSymbThread(self, thread_obj_id: Tag, parameters: UF.UFModl.SymbThreadData) -> None:
        ...
    def EditSymbThread2(self, thread_obj_id: Tag, internal_thread: bool, parameters: UF.UFModl.SymbThreadData) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def EditTaperFromEdges(self, feature_eid: Tag, type: int, direction_tag: Tag, angle_str: str, taper_all_instances: bool, num_edges: int, edges: typing.List[Tag], dist_tol: float, angle_tol: float) -> None:
        ...
    def EditWrapAssembly(self, feature_tag: Tag, wrap_data: UF.UFModl.WrapAssem) -> None:
        ...
    def EditWrapGeometry(self, feature_tag: Tag, wrap_data: UF.UFModl.WrapGeom) -> None:
        ...
    def EvalExp(self, exp_name: str, exp_value: float) -> None:
        ...
    def EvaluateCurve(self, curve_id: Tag, param: float, deriv_flag: int, pos_and_deriv: float) -> None:
        ...
    def EvaluateFace(self, face_tag: Tag, deriv_request: int, parms: float, eval_result: UF.ModlSrfValue) -> None:
        ...
    def ExportExp(self, file_spec: str) -> None:
        ...
    def ExportUdf(self, ip_prompts: str, ip_names: str, number_of_elements: int, sign: UF.FeatureSigns) -> None:
        ...
    def ExtractFace(self, face: Tag, mode: int, sheet_body: Tag) -> None:
        ...
    def FeatureCanBeCopied(self, feature_eid: Tag, copy_flag: bool) -> None:
        ...
    def FixBsurfaceData(self, degen_toler: float, bsurface: UF.UFModl.Bsurface, num_states: int, states: typing.List[UF.UFCurve.State]) -> None:
        ...
    def FormFeatures(self, n_features: int, feature_tag_array: typing.List[Tag], is_update_required: bool) -> None:
        ...
    def FreeBsurfData(self, bsurf: UF.UFModl.Bsurface) -> None:
        ...
    def FreeCompareData(self, mapping_data: UF.UFModl.ComparePartMapData) -> None:
        ...
    def FreeCompareData3(self, mapping_data: UF.UFModl.ComparePartMapData3) -> None:
        ...
    def FreeLaw(self, uf_law_parms: int) -> None:
        ...
    def FreeLawExtension(self, law_extension_data: UF.UFModl.LawextData, free_laws: bool) -> None:
        ...
    def FreeRefitFaceFeatureData(self, refit_data: UF.UFModl.RefitFaceData) -> None:
        ...
    def FreeRoughOffsetData(self, parms: UF.UFModl.RoughOffset) -> None:
        ...
    def FreeSilhouetteFlange(self, sflange_data: UF.UFModl.SflangeData) -> None:
        ...
    def FreeSnipSurfaceFeatureData(self, usr_data_ptr: UF.UFModl.SnipsrfFeatureData) -> None:
        ...
    def FreeStringList(self, string_list: UF.StringList) -> None:
        ...
    def FreeSymbThreadData(self, thread: UF.UFModl.SymbThreadData) -> None:
        ...
    def GenflgAskNumStates(self, genflg: Tag, num_states: int) -> None:
        ...
    def GenflgDeleteState(self, genflg: Tag, state_index: int) -> None:
        ...
    def GetCurveEdgeDirection(self, end_point: float, curve_edge_eid: Tag, direction: int) -> None:
        ...
    def GetDimensionData(self, exp: Tag, feature_tag: Tag, dim_data: UF.UFModl.DimensionData) -> None:
        ...
    def HideParentCurves(self, feature_tag: Tag, n_unch_disp_stat: int, unch_parents_disp_status: typing.List[UF.UFModl.ParentDispInfo], n_ch_disp_stat: int, ch_parents_disp_status: typing.List[UF.UFModl.ParentDispInfo]) -> None:
        ...
    def IdentifyExteriorUsingHl(self, num_bodies: int, bodies: typing.List[Tag], xforms: typing.List[Tag], num_dirs: int, direction: float, chordal_tol: float, resolution: int, num_faces: int, faces: typing.List[Tag], body_index: int) -> None:
        ...
    def IdentifyExteriorUsingRays(self, num_bodies: int, bodies: typing.List[Tag], xforms: typing.List[Tag], origin: float, chordal_tol: float, ray_type: int, num_faces: int, faces: typing.List[Tag], body_index: int) -> None:
        ...
    def ImportExp(self, file_spec: str, new_def: int) -> None:
        ...
    def ImportUdf(self, filename: str, dest_csys: float, dest_point: float, udf_id: Tag) -> None:
        ...
    def InitEdgeBlendPointMult(self, point_data: UF.UFModl.BlendPointData) -> None:
        ...
    def InitEdgeBlendSetMult(self, blend_set: UF.UFModl.EdgeBlendSet) -> None:
        ...
    def InitEdgeBlendSetbackMult(self, sb_data: UF.UFModl.EdgeBlendSetbackData) -> None:
        ...
    def InitEdgeBlendStopshortMult(self, ss_data: UF.UFModl.EdgeBlendStopshortData) -> None:
        ...
    def InitRipedgeUfdata(self, ripedge_ufdata: UF.UFModl.RipedgeData) -> None:
        ...
    def InitSilhouetteFlangeData(self, sflange_data: UF.UFModl.SflangeData) -> None:
        ...
    def InitSmcornerUfdata(self, smcorner_ufdata: UF.UFModl.SmcornerData) -> None:
        ...
    def InitStringList(self, string_list1: UF.StringList) -> None:
        ...
    def InitStycornerData(self, styled_corner_data: UF.UFModl.StycornerData) -> None:
        ...
    def InitializeCompareData(self, mapping_data: UF.UFModl.ComparePartMapData) -> None:
        ...
    def IntersectBodies(self, target: Tag, tool: Tag, num_result: int, resulting_bodies: typing.List[Tag]) -> None:
        ...
    def IntersectBodiesWithRetainedOptions(self, original_target: Tag, original_tool: Tag, retain_target_body: bool, retain_tool_body: bool, frec_eid: Tag) -> None:
        ...
    def IntersectCurveToCurve(self, curve1_id: Tag, curve2_id: Tag, num_intersections: int, data: float) -> None:
        ...
    def IntersectCurveToFace(self, curve_id: Tag, face_id: Tag, num_intersections: int, data: float) -> None:
        ...
    def IntersectCurveToPlane(self, curve_id: Tag, plane_id: Tag, num_intersections: int, data: float) -> None:
        ...
    def IsBodyConvergent(self, body: Tag, is_convergent_body: bool) -> None:
        ...
    def IsBodyFeature(self, feature: Tag, is_body_feature: bool) -> None:
        ...
    def IsBrowseableFeature(self, feature_tag: Tag, report_inactive_feature: bool, report_feature_unable_to_make_current: bool, is_browseable: bool) -> None:
        ...
    def IsDatumAxisReversed(self, datum_axis_tag: Tag, reversed: bool) -> None:
        ...
    def IsDatumPlaneReversed(self, datum_plane_tag: Tag, reversed: bool) -> None:
        ...
    def IsExpInPart(self, object_in_search_part: Tag, left_hand_side: str, is_exp_in_part: bool) -> None:
        ...
    def IsFeatureAHiddenSetMember(self, feature: Tag, hidden_member: bool) -> None:
        ...
    def IsFeatureASetMember(self, feature: Tag, flag: int) -> None:
        ...
    def IsGeometricExpression(self, exp_tag: Tag, flag: bool) -> None:
        ...
    def IsImportBodyFeature(self, input_tag: Tag, is_import_body_feature: bool) -> None:
        ...
    def IsodivideFace(self, sheet_id: Tag, div_param: float, div_dir: int, second_sheet_id: Tag) -> None:
        ...
    def IsotrimFace(self, sheet_id: Tag, trim_param: float) -> None:
        ...
    def MatchedgeAskData(self, medge_tag: Tag, uf_medge: typing.List[UF.UFModl.MatchedgeData]) -> None:
        ...
    def MatchedgeCheck(self, uf_data: UF.UFModl.MatchedgeData, continuity: int, num_pnts: int, deviation: float) -> None:
        ...
    def MatchedgeCreateFeature(self, uf_data: UF.UFModl.MatchedgeData, frec_tag: Tag) -> None:
        ...
    def MatchedgeEditFeature(self, uf_data: UF.UFModl.MatchedgeData, frec_tag: Tag) -> None:
        ...
    def ModelCompare(self, part1: Tag, body_eids_part1: Tag, transform_1: float, part2: Tag, body_eids_part2: Tag, transform_2: float, compare_feat_and_exp: bool, accuracy: UF.UFModl.CompareAccuracy, tolerance: float, identical_face_rule: UF.UFModl.CompareIdenticalfaceRule, uniquechangedfacerule: UF.UFModl.CompareChangeduniquefaceRule, launch_ui: bool, mapping_data: UF.UFModl.ComparePartMapData) -> None:
        ...
    def ModelCompare3(self, part1: Tag, body_eids_part1: Tag, transform_1: float, part2: Tag, body_eids_part2: Tag, transform_2: float, compare_options: UF.UFModl.CompareOptions, mapping_data: typing.List[UF.UFModl.ComparePartMapData3]) -> None:
        ...
    def MoveFeature(self, cmtag: typing.List[Tag], mode: int, real_data: float) -> None:
        ...
    def Operations(self, target: Tag, tool: Tag, sign: UF.FeatureSigns) -> None:
        ...
    def PasteFeatures(self, feature_array: typing.List[Tag], num_features: int, old_parents: typing.List[Tag], new_parents: typing.List[Tag], num_parents: int, expression_transfer_mode: int, parent_transfer_mode: int) -> None:
        ...
    def PatchBody(self, target_body: Tag, tool_sheet: Tag, reverse: int, feature_obj_id: Tag) -> None:
        ...
    def PreviewSimplify(self, simpl_parms: UF.UFModl.SimplData, n_retained_faces: int, retained_faces: typing.List[Tag], n_removed_faces: int, removed_faces: typing.List[Tag], n_leaks: int, n_leak_faces: int, leak_faces: typing.List[Tag[]]) -> None:
        ...
    def PromMapObjectDown(self, prom_tag: Tag, base_tag: Tag) -> None:
        ...
    def PromMapObjectUp(self, base_tag: Tag, prom_feat_tag: Tag, prom_tag: Tag) -> None:
        ...
    def PutListItem(self, list: typing.List[Tag], obj_id: Tag) -> None:
        ...
    def ReattachDirRef(self, feature_eid: Tag, ref_eid: Tag, ref_is_horizontal: int, delete_rpo: bool) -> None:
        ...
    def ReattachTargetFace(self, feature_eid: Tag, face_eid: Tag, point: float, flip: int, delete_rpo: bool) -> None:
        ...
    def ReattachThruFaces(self, feature_eid: Tag, number_of_faces: int, face_eids: typing.List[Tag], delete_rpo: bool) -> None:
        ...
    def ReattachToolFace(self, feature_eid: Tag, face_eid: Tag, delete_rpo: bool) -> None:
        ...
    def RecordFeatureUpdateWarnings(self, warning_option: bool) -> None:
        ...
    def RedefineReplaceFaces(self, feature_eid: Tag, number_of_faces: int, face_eids: typing.List[Tag]) -> None:
        ...
    def RedefineRpoConstraint(self, constraint: Tag, eid_target: Tag, tangent2arc1: int, eid_tool: Tag, tangent2arc2: int) -> None:
        ...
    def RedefineThickenSheet(self, thicken_sheet_tag: Tag, first_offset: str, second_offset: str, sheet_body_tag: Tag, target_body_tag: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RedefineTrimFaces(self, udf_id: Tag, n_trim_faces: int, trim_faces: typing.List[Tag], delete_rpo: bool) -> None:
        ...
    def RegisterCliffBlend(self, var_routine: UF.UFModl.CliffBlendFT) -> None:
        ...
    def RegisterRpoRoutine(self, routine: UF.UFModl.RpoFPT) -> None:
        ...
    def RegisterVarBlend(self, routine: UF.UFModl.VarBlendFT) -> None:
        ...
    def RemoveThruFaces(self, feature_eid: Tag) -> None:
        ...
    def RenameExp(self, old_exp_name: str, new_exp_name: str) -> None:
        ...
    def ReorderFeature(self, reference_feature: Tag, reposition_features: typing.List[Tag], method: int) -> None:
        ...
    def ReplaceBodyData(self, original_feature: Tag, new_body: Tag) -> None:
        ...
    def ReplaceBooleanBody(self, boolean_feature_obj_id: Tag, type: UF.UFModl.BooleanBody, new_body: Tag) -> None:
        ...
    def ReplaceFeatStrings(self, feature_obj_id: Tag, option: int, _string: UF.StringList, string_set: int, index: int) -> None:
        ...
    def ReplaceFeatures(self, original_features: typing.List[Tag], n_original_features: int, replacement_features: typing.List[Tag], n_replm_features: int, return_map: bool, use_copy_of_replacement: bool, parent_map: typing.List[UF.UFModl.ReplaceFeaturesStruct], n_parent_map: int) -> None:
        ...
    def ReplaceSweepStrings(self, sweep_feature_id: Tag, n_original_profile_objs: int, original_profile_objs: typing.List[Tag], n_new_profile_objs: int, new_profile_objs: typing.List[Tag], n_original_guide_objs: int, original_guide_objs: typing.List[Tag], n_new_guide_objs: int, new_guide_objs: typing.List[Tag]) -> None:
        ...
    def RequireUdfMappingForEdit(self, udf_insert_tag: Tag, mapping_is_required: bool, mapping_num_objects: int, mapping_objects: typing.List[Tag]) -> None:
        ...
    def RequireUdfMappingForInsert(self, udf_define_tag: Tag, mapping_is_required: bool, mapping_num_objects: int, mapping_objects: typing.List[Tag]) -> None:
        ...
    def ReverseDatumAxis(self, datum_axis_tag: Tag) -> None:
        ...
    def ReverseDatumPlane(self, datum_plane_tag: Tag) -> None:
        ...
    def ReverseDirRef(self, feature_eid: Tag, ref_eid: Tag, ref_is_horizontal: int, delete_rpo: bool, reverse: bool) -> None:
        ...
    def SetAngleTolerance(self, tolerance: float) -> None:
        ...
    def SetBodyDensity(self, body: Tag, units: UF.UFModl.DensityUnits, density: float) -> None:
        ...
    def SetBodyTypePref(self, body_type: int) -> None:
        ...
    def SetBsurfKnotDisplay(self, face: Tag, state: bool) -> None:
        ...
    def SetBsurfPoleDisplay(self, face: Tag, state: bool) -> None:
        ...
    def SetContainment(self, face_eid: Tag) -> None:
        ...
    def SetCurrentFeature(self, feature_id: Tag) -> None:
        ...
    def SetCurveFitData(self, curve_fit_data: UF.UFModl.CurveFitData) -> None:
        ...
    def SetCurveFitMethod(self, fit_method: int) -> None:
        ...
    def SetDatumCsysScaling(self, datum_csys_tag: Tag, scaling_on: bool) -> None:
        ...
    def SetDatumCsysVisibility(self, datum_csys_tag: Tag, visibility: bool) -> None:
        ...
    def SetDefaultDensity(self, density: float, units: UF.UFModl.DensityUnits) -> None:
        ...
    def SetDistanceTolerance(self, tolerance: float) -> None:
        ...
    def SetDynamicUpdate(self, update_type: int) -> None:
        ...
    def SetFaceBlendLawRadii(self, feature: Tag, radii_values: float, rad_num: int) -> None:
        ...
    def SetFaceBlendLawRange1Radii(self, feature: Tag, radii_values: float, rad_num: int) -> None:
        ...
    def SetFaceBlendLawRange2Radii(self, feature: Tag, radii_values: float, rad_num: int) -> None:
        ...
    def SetFeatTolerance(self, feature_obj_id: Tag, tolerance: float, update_part: bool) -> None:
        ...
    def SetFlangeProcFactor(self, flange: Tag, proc_factor: float) -> None:
        ...
    def SetFreeFormResult(self, free_form_result: int) -> None:
        ...
    def SetImmediateChildren(self, update_level: int) -> None:
        ...
    def SetMidsrfFeatureCreateMethod(self, feature_obj_id: Tag, adv_crt_and_trm: int) -> None:
        ...
    def SetRpoRefernce(self, reference: Tag, point: float, flip: int) -> None:
        ...
    def SetShowReportReference(self, reportReference: bool) -> None:
        ...
    def SetStartAndDirectionToSection(self, starting_object: Tag, starting_point: float, direction: float, section_tag: Tag) -> None:
        ...
    def SetSuppressExpTag(self, feature_tag: Tag, expression_tag: Tag) -> None:
        ...
    def SetSweepAxis(self, feature_id: Tag, dir: float) -> None:
        ...
    def SetSweepTolerances(self, feature_id: Tag, tolerance: float) -> None:
        ...
    def SetUdfParms(self, udf_id: Tag, prompt: str, values: str, number_of_parms: int) -> None:
        ...
    def SetUpdateFailOption(self, new_fail_option: UF.UFModl.UpdateOption) -> None:
        ...
    def SetXformTagOfDatumCsys(self, datum_csys_feature: Tag, xform_tag: Tag) -> None:
        ...
    def ShapePatternCreateDialog(self, pClientData: UF.UFModl.ShapePatternClientDialogData, response: int) -> None:
        ...
    def ShapePatternFreeClientData(self, pClientData: UF.UFModl.ShapePatternClientDialogData) -> None:
        ...
    def ShapePatternInitClientData(self, pClientData: UF.UFModl.ShapePatternClientDialogData) -> None:
        ...
    def SmoothBsurfaceData(self, cont_order_u: int, cont_order_v: int, dist_toler: float, ang_toler: float, bsurf: UF.UFModl.Bsurface, num_states: int, states: typing.List[UF.UFCurve.State]) -> None:
        ...
    def SortFeatures(self, feature1: Tag, feature2: Tag, result: int) -> None:
        ...
    def SplitBody(self, num_bodies: int, bodies: typing.List[Tag], cutting_body: Tag, num_split_bodies: int, split_bodies: typing.List[Tag]) -> None:
        ...
    def SplitBodyRetainTool(self, num_bodies: int, bodies: typing.List[Tag], cutting_body: Tag, num_split_bodies: int, split_bodies: typing.List[Tag]) -> None:
        ...
    def SubtractBodies(self, target: Tag, tool: Tag, num_result: int, resulting_bodies: typing.List[Tag]) -> None:
        ...
    def SubtractBodiesWithRetainedOptions(self, original_target: Tag, original_tool: Tag, retain_target_body: bool, retain_tool_body: bool, frec_eid: Tag) -> None:
        ...
    def SuppressFeature(self, feature_list: typing.List[Tag]) -> None:
        ...
    def TraceARay(self, num_bodies: int, bodies: typing.List[Tag], origin: float, direction: float, transform: float, num_desired: int, num_results: int, hit_list: typing.List[UF.UFModl.RayHitPointInfo]) -> None:
        ...
    def TransformEntities(self, num_entities: int, entities: typing.List[Tag], matrix: float) -> None:
        ...
    def TrimBody(self, target_body: Tag, tool_tag: Tag, direction_flag: int, trim_feature: Tag) -> None:
        ...
    def TrimMidsrfFeature(self, midsrf_feature_obj_id: Tag) -> None:
        ...
    def TrimSheet(self, sheet_body_tag: Tag, count_bounding_objects: int, bounding_objects: typing.List[UF.UFModl.TrimObject], projection_vector: float, point_key: int, point_count: int, point_coords: float, tolerance: float, number_gap_points: int, gap_points: float) -> None:
        ...
    def UdfFreeExpData(self, exp_data: UF.UFModl.UdfExpData) -> None:
        ...
    def UdfInitExpData(self, exp_data: UF.UFModl.UdfExpData) -> None:
        ...
    def UdfRpoMenu(self, feature_eid: Tag) -> int:
        ...
    def UnclockInstance(self, feature_obj_id: Tag) -> None:
        ...
    def UnclockIset(self, feature_obj_id: Tag) -> None:
        ...
    def UnformFeatures(self, n_features: int, feature_tag_array: typing.List[Tag], is_update_required: bool) -> None:
        ...
    def UniteBodies(self, target: Tag, tool: Tag) -> None:
        ...
    def UniteBodiesWithRetainedOptions(self, original_target: Tag, original_tool: Tag, retain_target_body: bool, retain_tool_body: bool, frec_eid: Tag) -> None:
        ...
    def UnregisterCliffBlend(self) -> None:
        ...
    def UnregisterRpoRoutine(self) -> None:
        ...
    def UnregisterUdfMappingRoutine(self) -> None:
        ...
    def UnregisterVarBlend(self) -> None:
        ...
    def UnsetContainment(self, face_eid: Tag) -> None:
        ...
    def UnsetSuppressExpTag(self, feature_tag: Tag) -> None:
        ...
    def UnsuppressFeature(self, feature_list: typing.List[Tag]) -> None:
        ...
    def Update(self) -> None:
        ...
    def UpdateAllFeatures(self) -> None:
        ...
    def UpdateForAnimation(self) -> None:
        ...
    def ValidateBody(self, num_bodies: int, bodies: typing.List[Tag], valid_info: int) -> None:
        ...


    class UFModlWrapGeom():
        close_gap: int
        dist_tol: float
        add_offset: str
        split_offset: str
        num_geoms: int
        geometry: typing.List[Tag]
        num_splits: int
        splits: typing.List[Tag]
    

    class UFModlWrapAssem():
        close_gap: int
        dist_tol: float
        add_offset: str
        split_offset: str
        num_geoms: int
        geometry: typing.List[Tag]
        geom_xforms: typing.List[Tag]
        num_splits: int
        splits: typing.List[Tag]
        split_xforms: typing.List[Tag]
    

    

    class UpdateOption(enum.Enum):
        UpdateNoOption = 0
        UpdateUndo = 1
        UpdateSuppress = 2
        UpdateSuppressAll = 3
        UpdateAccept = 4
        UpdateAcceptAll = 5
        UpdateInterrupt = 6
    

    class UFModlUdfsExp():
        type: int
        exp: str
        exp_name: str
        define_value: str
        num_def: int
        low_end: str
        high_end: str
        scale_type: int
    

    

    class UFModlUdfExpData():
        num_exps: int
        old_exps: typing.List[Tag]
        new_exp_values: str
    

    class UFModlTrimObject():
        object_tag: Tag
        curve_project_method: int
    

    class TrimBlendOptions(enum.Enum):
        UF_TRIM_AND_ATTACH = 0
        UF_TRIM_LONG_AND_ATTACH = 1
        UF_NO_TRIM_AND_ATTACH = 2
        UF_TRIM_ALL = 3
        UF_TRIM_BLEND = 4
        UF_NO_TRIM = 5
        UF_TRIM_BLEND_LONG = 6
        UF_TRIM_BLEND_SHORT = 7
    

    class TransformType(enum.Enum):
        UF_TRANSF_POINT_POINT = 0
        UF_TRANSF_DIRECTION_DISTANCE = 1
        UF_TRANSF_AXIS_ANGLE = 2
        UF_TRANSF_AXIS_AXIS = 3
    

    class UFModlSymbThreadData():
        cyl_face: Tag
        start_face: Tag
        axis_direction: float
        include_instances: int
        rotation: int
        length_flag: int
        tapered: int
        num_starts: int
        length: str
        form: str
        method: str
        callout: str
        major_dia: str
        minor_dia: str
        tapped_dia: str
        pitch: str
        angle: str
        internal_thread: bool
    

    

    class UFModlStycornerData():
        blend_faces: typing.List[Tag]
        num_base_faces: int
        base_faces: typing.List[Tag]
        split_curve_params: float
        interior_opt: int
        boundary_conds: int
        trim_attach_opt: int
        dist_tol: float
        angle_tol: float
        is_rectangular: bool
        crv_opt: typing.List[UF.UFModl.StycornerCrvOpt]
        trim_curve_opt: int
        interior_iso_u_crv_end_params: float
        interior_iso_v_crv_end_params: float
    

    class UFModlStycornerCrvOpt():
        shape_control: int
        start_tagmag: float
        end_tagmag: float
        depth: float
        skew: float
    

    class UFModlStateInfo():
        process_factor: float
        state_index: int
    

    class State(enum.Enum):
        UnformedState = 0
        FormedState = 1
        OtherState = 2
        UF_N_STATE_OPTS = 3
    

    class UFModlSolidPunchData():
        type: int
        thickness_option: int
        thickness: str
        target_face: Tag
        tool_body: Tag
        target_csys_pt: Tag
        tool_csys_pt: Tag
        n_pierce_faces: int
        pierce_faces: typing.List[Tag]
        is_pt_required: bool
    

    class SnipsurfRefitMethod(enum.Enum):
        SnipsurfRefitMethodNone = 0
        SnipsurfRefitMethodDegPatch = 1
        SnipsurfRefitMethodDegTol = 2
        SnipsurfRefitMethodPatchTol = 3
    

    class SnipsurfBoundaryType(enum.Enum):
        SnipsurfBoundaryTypeCurves = 0
        SnipsurfBoundaryTypePlane = 1
    

    class UFModlSnipsrfFeatureData():
        edit_face: Tag
        boundary_type: UF.UFModl.SnipsurfBoundaryType
        snip_cv_string: UF.StringList
        snipping_plane: Tag
        project_vector: float
        snip_or_divide: int
        region_point_uv: float
        project_method: int
        refit_method: UF.UFModl.SnipsurfRefitMethod
        refit_degree: int
        refit_patches: int
        tols: float
    

    class SmslotType(enum.Enum):
        UF_PUNCH_SMSLOT = 0
        UF_THROUGH_SMSLOT = 1
        UF_DEPTH_SMSLOT = 2
        UF_N_STYPE_OPTS = 3
    

    class UFModlSmslotData():
        length: str
        width: str
        depth: str
        edge1: Tag
        offset1: str
        edge2: Tag
        offset2: str
        slot_face: Tag
        through_face: Tag
        dir_method: UF.UFModl.SmholeDirectionType
        d_datum_axis: Tag
        d_vec_dir: float
        orient_method: UF.UFModl.SmholeDirectionType
        o_datum_axis: Tag
        o_vec_dir: float
        type: UF.UFModl.SmslotType
    

    class UFModlSmreliefData():
        base_face: Tag
        first_corner_edges: typing.List[Tag]
        second_corner_edges: typing.List[Tag]
        offset_corner: float
        first_corner_fillet_radius: str
        second_corner_fillet_radius: str
        os_circle_radius: str
        offset_distance: str
    

    class SmpunchTopType(enum.Enum):
        OFFSET_TOP_TYPE = 0
        FLAT_TOP_TYPE = 1
        ROUND_TOP_TYPE = 2
        CONE_TOP_TYPE = 3
    

    class UFModlSmpunchData():
        punch_type: UF.UFModl.PunchType
        top_type: UF.UFModl.SmpunchTopType
        proj_method: UF.UFModl.SmholeDirectionType
        tool_center: Tag
        placement_face: Tag
        n_curves: int
        curves: typing.List[Tag]
        num_cut_curve_sets: int
        cut_curve_sets: typing.List[UF.UFModl.SmpunchCutSets]
        datum_axis: Tag
        depth: str
        die_radius: str
        taper_angle: str
        punch_radius: str
        cone_depth: str
        proj_vector: float
        flip_discard_region: bool
        inside_or_out: bool
        auto_centroid: bool
    

    class UFModlSmpunchCutSets():
        num_curves: int
        curves: typing.List[Tag]
    

    class UFModlSmjoggleData():
        base_face: Tag
        ref_face1: Tag
        ref_face2: Tag
        trans_start_edge: Tag
        trans_end_edge: Tag
        base_edge: Tag
        point_on_rf1: float
        point_on_rf2: float
        num_clr_pts: int
        clr_point1: float
        clr_point2: float
        mat_direction: bool
        clr_dist: str
        bend_radius1: str
        bend_radius2: str
        transition_radius: str
        run: str
        table: bool
        edge_to_edge: bool
        mat_thickness: str
        bend_allowance_formula: str
    

    class SmholeType(enum.Enum):
        UF_DEPTH_SMHOLE = 0
        UF_THROUGH_SMHOLE = 1
        UF_PUNCH_SMHOLE = 2
        UF_N_TYPE_OPTS = 3
    

    class SmholeDirectionType(enum.Enum):
        UF_FACE_NORMALS = 0
        UF_ALONG_VECTOR = 1
        UF_ALONG_DATUM_AXIS = 2
        UF_N_DIRECTION_OPTS = 3
    

    class UFModlSmholeData():
        diameter: str
        depth: str
        tip_angle: str
        edge1: Tag
        offset1: str
        edge2: Tag
        offset2: str
        hole_face: Tag
        thru_face: Tag
        datum_axis: Tag
        method: UF.UFModl.SmholeDirectionType
        vec_dir: float
        type: UF.UFModl.SmholeType
    

    class SmcutoutType(enum.Enum):
        UF_PUNCH_SMCUTOUT = 0
        UF_THROUGH_SMCUTOUT = 1
        UF_N_SMCUTOUT_TYPE_OPTS = 2
    

    class UFModlSmcutoutData():
        placement_face: Tag
        n_curves: int
        curves: typing.List[Tag]
        proj_method: UF.UFModl.SmholeDirectionType
        proj_vector: float
        datum_axis: Tag
        flip_discard_region: bool
        type: UF.UFModl.SmcutoutType
        thru_face: Tag
    

    class UFModlSmcornerData():
        corner_type: int
        ref_edge: Tag
        ref_face: Tag
        butt_gap: str
        butt_overlap: str
        mc_offset: str
        mc_gap: str
        mc_linear_shape: bool
        use_enhanced_mach_corner: bool
        switch_parent_flag: bool
        simple_gap: str
        miter_toggle: bool
    

    class SmbendStatSide(enum.Enum):
        UF_SMBEND_INVALID_STAT_SIDE = -1
        UF_SMBEND_STAT_SIDE_AS_SPECIFIED = 0
        UF_SMBEND_STAT_SIDE_OPPOSITE_SIDE = 1
        UF_SMBEND_NUM_STAT_SIDES = 2
    

    class SmbendRadius(enum.Enum):
        UF_SMBEND_INVALID_RADIUS_TYPE = -1
        UF_SMBEND_INNER_RADIUS = 0
        UF_SMBEND_OUTER_RADIUS = 1
        UF_SMBEND_NUM_RADIUS_TYPES = 2
    

    class SmbendDirection(enum.Enum):
        UF_SMBEND_INVALID_BEND_DIR = -1
        UF_SMBEND_BEND_DIR_AS_SPECIFIED = 0
        UF_SMBEND_BEND_DIR_OPPPOSITE_SIDE = 1
        UF_SMBEND_NUM_BEND_DIRS = 2
    

    class UFModlSmbendData():
        base_face: Tag
        app_curve: Tag
        app_curve_type: UF.UFModl.SmbendCurve
        angle: str
        angle_type: UF.UFModl.SmbendAngle
        radius: str
        radius_type: UF.UFModl.SmbendRadius
        bend_dir: UF.UFModl.SmbendDirection
        stat_side: UF.UFModl.SmbendStatSide
        baf: str
    

    class UFModlSmbendCylinderData():
        base_face: Tag
        stat_side: UF.UFModl.SmbendStatSide
        baf: str
    

    class SmbendCurve(enum.Enum):
        UF_SMBEND_INVALID_CURVE_TYPE = -1
        UF_SMBEND_NONE = 0
        UF_SMBEND_BEND_CENTERLINE = 1
        UF_SMBEND_BEND_AXIS = 2
        UF_SMBEND_BEND_TANGENT_LINE = 3
        UF_SMBEND_CONTOUR_LINE = 4
        UF_SMBEND_MOLD_LINE = 5
        UF_SMBEND_NUM_CURVE_TYPES = 6
    

    class UFModlSmbendCornerData():
        base_edge: Tag
        radius: str
        radius_type: UF.UFModl.SmbendRadius
        stat_side: UF.UFModl.SmbendStatSide
        baf: str
    

    class SmbendAngle(enum.Enum):
        UF_SMBEND_INVALID_ANGLE_TYPE = -1
        UF_SMBEND_BEND_ANGLE = 0
        UF_SMBEND_INCLUDED_ANGLE = 1
        UF_SMBEND_NUM_ANGLE_TYPES = 2
    

    class SlotType(enum.Enum):
        UF_RECTANGULAR_SLOT = 0
        UF_BALL_END_SLOT = 1
        UF_U_SLOT = 2
        UF_T_SLOT = 3
        UF_DOVE_TAIL_SLOT = 4
    

    class UFModlSimplData():
        n_retained_faces: int
        retained_faces: typing.List[Tag]
        n_boundary_faces: int
        boundary_faces: typing.List[Tag]
        n_removed_faces: int
        removed_faces: typing.List[Tag]
        n_boundary_edges: int
        boundary_edges: typing.List[Tag]
        n_non_boundary_edges: int
        non_boundary_edges: typing.List[Tag]
        n_imprint_features: int
        imprint_features: typing.List[Tag]
        max_hole_dia_expression: Tag
    

    class UFModlShapePatternClientDialogData():
        PartName: str
        HoleName: str
        iCountRecommendedShape: int
        RecommendedShapeNames: str
        RecommendedShapeThumbnailImageNames: str
        RecommendedShapeLargeImageNames: str
        iCountOtherShape: int
        OtherShapeNames: str
        OtherShapeThumbnailImageNames: str
        OtherShapeLargeImageNames: str
        NoImageBmpName: str
        CurrentHoleShapePatternName: str
        CurrentLargeImageName: str
        iSelectedHoleShapeIndex: int
        bSelFromRecommendedGroup: bool
    

    class SflangeType(enum.Enum):
        SflangeBasic = 0
        SflangeAbsoluteGap = 1
        SflangeVisualGap = 2
    

    class SflangeTrim(enum.Enum):
        SflangeNoTrimSew = 0
        SflangeTrimSew = 1
        SflangeNoSew = 2
        SflangeNoTrim = 3
    

    class SflangeDir(enum.Enum):
        SflangeDirNormal = 0
        SflangeDirVector = 1
        SflangeDirNormalDraft = 2
        SflangeDirVectorDraft = 3
    

    class UFModlSflangeData():
        type: UF.UFModl.SflangeType
        dir_opt: UF.UFModl.SflangeDir
        trim_opt: UF.UFModl.SflangeTrim
        base_cont: UF.UFModl.SflangeContinuity
        flange_cont: UF.UFModl.SflangeContinuity
        base_scale: int
        flange_scale: int
        feature_tag: Tag
        curve: typing.List[UF.StringList]
        n_faces: int
        face_tags: typing.List[Tag]
        vec_tag: Tag
        radius: float
        gap: float
        centerline_tag: Tag
        radius_law_parms: int
        length_law_parms: int
        angle_law_parms: int
        distance_tol: float
        angle_tol: float
        vec_0: float
        vec_90: float
        merge_faces: bool
        create_pipe_only: bool
        flip_dir: bool
        flip_side: bool
        extend_pipe: bool
    

    class SflangeContinuity(enum.Enum):
        SflangeContinuityG0 = 0
        SflangeContinuityG1 = 1
        SflangeContinuityG2 = 2
    

    

    class UFModlRoughOffset():
        entities: typing.List[Tag]
        num_entities: int
        smart_csys: Tag
        offset_distance: str
        offset_deviation: str
        stepover_distance: str
        surf_method: UF.RsoSurfMethod
        surf_ctrl_type: UF.RsoSurfCtrlOption
        u_patches: int
        boundary_trim: UF.RsoTrimOption
    

    class UFModlRipedgeData():
        n_ripedges: int
        ripedges: typing.List[Tag]
        add_tangent: bool
        gap_type: int
        gap: str
        offset: str
        extension: str
        end_condition: int
    

    class UFModlReplaceFeaturesStruct():
        original_entity: Tag
        replacement_entity: Tag
    

    class UFModlRefitFaceTargetData():
        n_target_obj: int
        target_obj: typing.List[Tag]
        fit_direction_data: UF.UFModl.RefitFaceFitDirection
        max_checking_data: float
    

    class RefitFaceFitDirection(enum.Enum):
        RefitFaceRefitDirectionNoDirection = 0
        RefitFaceRefitDirectionXDirection = 1
        RefitFaceRefitDirectionYDirection = 2
        RefitFaceRefitDirectionZDirection = 3
        RefitFaceRefitDirectionViewDirection = 4
    

    class UFModlRefitFaceData():
        face: Tag
        target_data: typing.List[UF.UFModl.RefitFaceTargetData]
        direction_data: int
        method_data: int
        u_deg_int_data: int
        u_patch_int_data: int
        v_deg_int_data: int
        v_patch_int_data: int
        umin_cnstr_data: UF.UFModl.RefitFaceContinuity
        umax_cnstr_data: UF.UFModl.RefitFaceContinuity
        vmin_cnstr_data: UF.UFModl.RefitFaceContinuity
        vmax_cnstr_data: UF.UFModl.RefitFaceContinuity
        tolerance_real_data: float
        smoothness_real_data: float
        percentage_real_data: float
    

    class RefitFaceContinuity(enum.Enum):
        RefitFaceContinuityFree = 0
        RefitFaceContinuityG0 = 1
        RefitFaceContinuityG1 = 2
        RefitFaceContinuityG2 = 3
    

    class UFModlReblendFaceData():
        num_chains: int
        radius: str
        chain_data: typing.List[UF.UFModl.ReblendFace]
    

    class UFModlReblendFace():
        chained: bool
        n_faces: int
        faces_eid: typing.List[Tag]
    

    class UFModlRayHitPointInfo():
        hit_point: float
        hit_normal: float
        hit_face: Tag
        hit_body: Tag
    

    class QuiltType(enum.Enum):
        CurveMeshAlongFixedVector = 1
        CurveMeshAlongDriverNormals = 2
        BSurfaceAlongFixedVector = 3
        BSurfaceAlongDriverNormals = 4
        SelfRefit = 5
    

    class PunchType(enum.Enum):
        UF_EMBOSS_PUNCH = 0
        UF_LANCE_PUNCH = 1
        UF_SEMI_PIERCE_PUNCH = 2
        UF_COIN_PUNCH = 3
    

    class UFModlParentDispInfo():
        eid: Tag
        layer_number: int
        blank_status: int
        change_status: bool
    

    class UFModlMatchedgeData():
        edit_edge_tag: Tag
        match_target_type: int
        match_continuity: int
        match_dir_vector_tag: Tag
        count_of_targets: int
        target_entity_tags: typing.List[Tag]
        flow_control: int
        adjacent_vec: float
        side_lock: int
        opposite_lock: int
        match_exact: int
        match_end_to_end: int
        limit_pole_move: int
        move_direction_tag: Tag
        match_edge_degree: int
        match_edge_patches: int
        lateral_edge_degree: int
        lateral_edge_patches: int
    

    class UFModlLinkedExt():
        num_bodies: int
        bodies: typing.List[Tag]
        xforms: typing.List[Tag]
        num_faces: int
        faces: typing.List[Tag]
        xform_index: int
        group_results: int
        mass_props: bool
        delete_openings: bool
        at_timestamp: bool
    

    class LawextDirref(enum.Enum):
        LawextDirrefFace = 0
        LawextDirrefVector = 1
    

    class UFModlLawextData():
        ref_type: UF.UFModl.LawextDirref
        length_law_parms: int
        angle_law_parms: int
        curve: typing.List[UF.StringList]
        n_faces: int
        face_ids: typing.List[Tag]
        smart_dir: Tag
        spine: typing.List[UF.StringList]
        distance_tol: float
        angle_tol: float
        merge: int
        bisided: int
    

    class UFModlInsetFlangeData():
        flange_data: typing.List[UF.UFModl.FlangeData]
        inset_type: int
        lrelief_type: int
        rrelief_type: int
        inset: str
        lrelief: str
        rrelief: str
    

    class UFModlImprintLoopData():
        imprint_face: Tag
        imprint_datum_plane: Tag
    

    class UFModlImprintFacesData():
        n_imprint_faces: int
        imprint_faces: typing.List[Tag]
        imprint_datum_plane: Tag
    

    class ImportBodyFeatureEditOption(enum.Enum):
        ImportBodyFeatureUpdateLink = 0
        ImportBodyFeatureRedefineLink = 1
        ImportBodyFeatureDeleteLink = 2
    

    class HoleType(enum.Enum):
        UF_SIMPLE_HOLE = 0
        UF_COUNTER_BORE_HOLE = 1
        UF_COUNTER_SUNK_HOLE = 2
    

    class UFModlFlangeData():
        angle_type: int
        length_type: int
        radius_type: int
        ltaper_type: int
        rtaper_type: int
        reverse_direction: bool
        ref_line_type: int
        thickness: str
        width: str
        angle: str
        length: str
        radius: str
        left_joint_type: int
        right_joint_type: int
        ltaper: str
        rtaper: str
        lmiter: str
        rmiter: str
        lbutt: str
        rbutt: str
        bend_allowance_formula: str
    

    class UFModlFeatures():
        feat_count: int
        feat_tags: typing.List[Tag]
        feat_type: str
    

    class UFModlFaces():
        number_of_faces: int
        faces: typing.List[Tag]
        face_extension: UF.UFModl.FaceExtension
    

    class FaceExtension(enum.Enum):
        FaceExtensionNone = 0
        FaceExtensionLinear = 1
        FaceExtensionNatural = 2
        FaceExtensionCurv = 3
        FaceExtensionCirc = 4
    

    class UFModlEdgeBlendStopshortData():
        edge: Tag
        from_start: bool
        distance: str
        distance_exp: Tag
        status: int
    

    class UFModlEdgeBlendSetbackData():
        edge: Tag
        from_start: bool
        distance: str
        distance_exp: Tag
        status: int
    

    class UFModlEdgeBlendSet():
        edge_collector: Tag
        num_edges: int
        edges: typing.List[Tag]
        radius: str
        radius_exp: Tag
        status: int
    

    

    class UFModlEdgeBlendData():
        blend_type: int
        blend_instanced: bool
        blend_setback: bool
        vrb_tolerance: float
        blend_radius: str
        smooth_overflow: bool
        cliff_overflow: bool
        notch_overflow: bool
        number_edges: int
        edge_data: typing.List[UF.UFModl.BlendEdge]
    

    class UFModlDimensionData():
        type: int
        feature_tag: Tag
        value: float
        first_point: float
        second_point: float
        origin: float
        start_angle: float
        end_angle: float
        csys_tag: Tag
        drf_txt: str
        top_array: typing.List[Tag]
        num_top_array: int
        first_line: UF.UFCurve.Line
        second_line: UF.UFCurve.Line
    

    

    class DfoScaleType(enum.Enum):
        UF_LSCALE_TYPE_UNIFORM = 0
        UF_LSCALE_TYPE_AXISYMMETRIC = 1
        UF_LSCALE_TYPE_GENERAL = 2
    

    class UFModlDfoRegion():
        seed_faces: typing.List[Tag]
        num_seed: int
        boundary_faces: typing.List[Tag]
        num_boundary: int
        excluded_faces: typing.List[Tag]
        num_exclude: int
    

    class DfoConstraintType(enum.Enum):
        UF_distance_dim = 0
        UF_angle_dim = 1
        UF_coincident = 2
        UF_parallel_con = 3
        UF_perpen_con = 4
        UF_tangent_con = 5
    

    class UFModlDfoConstraint():
        type: UF.UFModl.DfoConstraintType
        from_face: Tag
        to_object: Tag
        thru_point: Tag
        value: str
    

    class UFModlDeviationCheckData():
        number_of_points_checked: int
        minimum_distance_error: float
        maximum_distance_error: float
        average_distance_error: float
        minimum_angle_error: float
        maximum_angle_error: float
        average_angle_error: float
        distance_errors: float
        angle_errors: float
        check_points: float
    

    class UFModlDevchkEeInfo():
        dev_type: int
        face_1_tag: Tag
        edge_1_pnt: float
        norm_1: float
        face_2_tag: Tag
        edge_2_pnt: float
        norm_2: float
        edge_dist: float
        norm_angle: float
    

    class DensityUnits(enum.Enum):
        PoundsInches = 1
        PoundsFeet = 2
        GramsCentimeters = 3
        KilogramsMeters = 4
    

    class UFModlCurveFitData():
        curve_fit_method: int
        maximum_degree: int
        maximum_segments: int
    

    class UFModlComparePartMapData3():
        part1: typing.List[UF.UFModl.ComparePartEntitiesData3]
        part2: typing.List[UF.UFModl.ComparePartEntitiesData3]
        identical_parts: bool
    

    class UFModlComparePartMapData():
        part1: UF.UFModl.ComparePartEntitiesData
        part2: UF.UFModl.ComparePartEntitiesData
        identical_parts: bool
    

    class UFModlComparePartEntitiesData3():
        edges: typing.List[UF.UFModl.CompareEntityInfo]
        faces: typing.List[UF.UFModl.CompareEntityInfo]
        features: typing.List[UF.UFModl.CompareEntityInfo]
        expressions: typing.List[UF.UFModl.CompareEntityInfo]
    

    class UFModlComparePartEntitiesData():
        edges: UF.UFModl.CompareEntityInfo
        faces: UF.UFModl.CompareEntityInfo
        features: UF.UFModl.CompareEntityInfo
        expressions: UF.UFModl.CompareEntityInfo
    

    class UFModlCompareOptions():
        version: int
        tolerance: float
        accuracy: UF.UFModl.CompareAccuracy
        compare_feat_and_exp: bool
        identical_face_rule: UF.UFModl.CompareIdenticalfaceRule
        continue_if_examine_geom_fails: bool
        generate_report: bool
    

    class CompareIdenticalfaceRule(enum.Enum):
        CompAlledges = 0
        CompOnlyexternal = 1
        CompNone = 2
        CompGeom = 3
    

    class CompareEntityType(enum.Enum):
        CompEntUnknown = 0
        CompEntIdentical = 1
        CompEntChanged = 2
        CompEntUnique = 3
        CompEntSuppressed = 4
        CompEntNotCompared = 5
    

    class UFModlCompareEntityMatch():
        entity_tag: Tag
        match_entity: Tag
        type: UF.UFModl.CompareEntityType
        max_deviation: float
        avg_deviation: float
    

    class UFModlCompareEntityInfo():
        num_entities: int
        entity_info: typing.List[UF.UFModl.CompareEntityMatch]
    

    class CompareChangeduniquefaceRule(enum.Enum):
        CompNonidenticalsfChanged = 0
        CompNonidenticalsfUnique = 1
    

    class CompareAccuracy(enum.Enum):
        CompDefault = 0
        CompCoarse = 1
        CompFine = 2
    

    

    class UFModlBsurfRowInfo():
        num_points: int
        points: float
        weight: float
    

    class UFModlBsurface():
        num_poles_u: int
        num_poles_v: int
        order_u: int
        order_v: int
        is_rational: int
        knots_u: float
        knots_v: float
        poles: float
    

    class BooleanBody(enum.Enum):
        TargetBody = 0
        ToolBody = 1
    

    class BlendRadiusTypes(enum.Enum):
        UF_CONSTANT = 0
        UF_LAW_CONTROLLED = 1
        UF_TANGENCY_CONTROLLED = 2
        UF_CONIC = 3
        UF_CONIC_AUTO_RHO = 4
        UF_DISC = 5
        UF_ISOPARAMETER = 6
        UF_MATCH_TANGENTS = 7
        UF_MATCH_CURVATURE = 8
    

    class UFModlBlendPointData():
        radius: str
        parameter: float
        radius_exp: Tag
        status: int
    

    class UFModlBlendPoint():
        radius: str
        parameter: float
    

    class UFModlBlendFacesLimitData():
        use_start_limit: bool
        start_limit: float
        use_end_limit: bool
        end_limit: float
        use_help_point: bool
        help_point: float
    

    class UFModlBlendFacesCreateData():
        first_set: typing.List[Tag]
        first_set_size: int
        flip_first_normal: bool
        second_set: typing.List[Tag]
        second_set_size: int
        flip_second_normal: bool
        propagate: bool
        cliff_edges: typing.List[Tag]
        n_cliff_edges: int
        thls: typing.List[Tag]
        n_thls: int
        proj_on_first_set: bool
        end_overflow: bool
        blend_tolerance: str
        trim_option: UF.UFModl.TrimBlendOptions
        radius_type: UF.UFModl.BlendRadiusTypes
        default_radius: str
        law_parameters: int
    

    class UFModlBlendEdge():
        edge: Tag
        cliff_edge: Tag
        number_points: int
        start_setback_dis: str
        end_setback_dis: str
        point_data: typing.List[UF.UFModl.BlendPoint]
    

    class BendOperationE(enum.Enum):
        BendOperationUnbend = 0
        BendOperationRebend = 1
        BendOperationBendToAngle = 2
    

    class UFModlBendOperationData():
        operation_type: UF.UFModl.BendOperationE
        bend_edge: Tag
        bend_face: Tag
        use_adjacent_bend_face: bool
        parent_operation: Tag
        target_angle: str
        baf: str
        use_global_baf: bool
    

class UFMisc(Utilities.NXRemotableObject):
    def SetProgramName(self, name: str) -> None:
        ...


class UFMfm(Utilities.NXRemotableObject):
    def AskAttributeType(self, machining_feature: int, attribute: str, type: UF.UFMfm.AttrValueType) -> None:
        ...
    def AskAttributes(self, machining_feature: int, count: int, attribute_names: str) -> None:
        ...
    def AskCandidateMachiningFeatureTypes(self, body_count: int, body_list: typing.List[Tag], type_count: int, candidate_type_names: str) -> None:
        ...
    def AskDoubleValueOfAttribute(self, machining_feature: int, attribute: str, original_value: float, overridden_value: float) -> None:
        ...
    def AskFeatureName(self, machining_feature: int, feature_name: str) -> None:
        ...
    def AskFeatureType(self, machining_feature: int, feature_type_name: str) -> None:
        ...
    def AskGeometryGroups(self, machining_feature: int, count: int, geometry_groups: typing.List[Tag]) -> None:
        ...
    def AskIntegerValueOfAttribute(self, machining_feature: int, attribute: str, original_value: int, overridden_value: int) -> None:
        ...
    def AskListOfFaces(self, machining_feature: int, count: int, face_list: typing.List[Tag]) -> None:
        ...
    def AskLogicalValueOfAttribute(self, machining_feature: int, attribute: str, original_value: bool, overridden_value: bool) -> None:
        ...
    def AskMachinedStatus(self, machining_feature: int, geometry_group: Tag, status: UF.UFMfm.MachinedStatus) -> None:
        ...
    def AskMachiningFeatureTypes(self, part_tag: Tag, count: int, feature_type_names: str) -> None:
        ...
    def AskMachiningFeaturesOfPart(self, part_tag: Tag, count: int, machining_features: int) -> None:
        ...
    def AskMachiningFeaturesOfType(self, part_tag: Tag, type_name: str, count: int, machining_features: int) -> None:
        ...
    def AskOverriddenStatus(self, machining_feature: int, overridden_status: bool) -> None:
        ...
    def AskSelectedFeaList(self, machining_features: int, count: int) -> None:
        ...
    def AskSourceType(self, machining_feature: int, source: UF.UFMfm.SourceType) -> None:
        ...
    def AskStringValueOfAttribute(self, machining_feature: int, attribute: str, original_value: str, overridden_value: str) -> None:
        ...
    def CleanSelectedFeaList(self) -> None:
        ...
    def CreateMachiningFeature(self, feature_type: str, count: int, face_list: typing.List[Tag], machining_feature: int) -> None:
        ...
    def CreateMachiningFeaturesFromModelingFeatures(self, body_count: int, body_list: typing.List[Tag], type_count: int, feature_types: str, count: int, machining_features: int) -> None:
        ...
    def CreateMachiningFeaturesFromRecognizedFeatures(self, body_count: int, body_list: typing.List[Tag], count: int, machining_features: int) -> None:
        ...
    def CreateMachiningFeaturesFromTaggedArcs(self, count: int, machining_features: int) -> None:
        ...
    def CreateMachiningFeaturesFromTaggedEdges(self, body_count: int, body_list: typing.List[Tag], count: int, machining_features: int) -> None:
        ...
    def CreateMachiningFeaturesFromTaggedFaces(self, body_count: int, body_list: typing.List[Tag], count: int, machining_features: int) -> None:
        ...
    def CreateMachiningFeaturesFromTaggedPoints(self, count_of_machining_features: int, machining_features: int) -> None:
        ...
    def CreateMachiningFeaturesFromUserDefinedFeatures(self, body_count: int, body_list: typing.List[Tag], type_count: int, feature_types: str, count: int, machining_features: int) -> None:
        ...
    def DeleteMachiningFeatures(self, count: int, machining_features: int) -> None:
        ...
    def HasSelectedFeaList(self, result: bool) -> None:
        ...
    def RecognizeHoles(self, body_list: typing.List[Tag], body_count: int, type_list: str, type_count: int, options: UF.UFMfm.RecognizeOptions, feature_count: int, machining_features: int) -> None:
        ...
    def SetDoubleUgAttribute(self, machining_feature: int, attribute: str, value: float) -> None:
        ...
    def SetDoubleValueOfAttribute(self, machining_feature: int, attribute: str, overridden_value: float) -> None:
        ...
    def SetFeatureName(self, machining_feature: int, feature_name: str) -> None:
        ...
    def SetIntUgAttribute(self, machining_feature: int, attribute: str, value: int) -> None:
        ...
    def SetIntegerValueOfAttribute(self, machining_feature: int, attribute: str, overridden_value: int) -> None:
        ...
    def SetLogicalValueOfAttribute(self, machining_feature: int, attribute: str, overridden_value: bool) -> None:
        ...
    def SetSelectedFeaList(self, machining_features: int, count: int) -> None:
        ...
    def SetStringUgAttribute(self, machining_feature: int, attribute: str, value: str) -> None:
        ...
    def SetStringValueOfAttribute(self, machining_feature: int, attribute: str, overridden_value: str) -> None:
        ...


    class SourceType(enum.Enum):
        SourceTypeUndefined = 0
        SourceTypeUserDefinedFeature = 1
        SourceTypeStandardFeature = 2
        SourceTypeTaggedEdge = 3
        SourceTypeTaggedFace = 4
        SourceTypeTaggedPoint = 5
        SourceTypeTaggedArc = 6
        SourceTypeRecognizedFeature = 7
    

    class UFMfmRecognizeOptions():
        ignore_cad: bool
    

    class MachinedStatus(enum.Enum):
        MachinedStatusEmpty = 0
        MachinedStatusRegenerate = 1
        MachinedStatusIncomplete = 2
        MachinedStatusComplete = 3
    

    class AttrValueType(enum.Enum):
        AttrValueTypeUndefined = 0
        AttrValueTypeLogical = 1
        AttrValueTypeInteger = 2
        AttrValueTypeDouble = 3
        AttrValueTypeString = 4
    

class UFMech(Utilities.NXRemotableObject):
    def CreateGearJoint(self, revolute_obj: Tag, rev_or_slider: Tag, contact_point: float, contact_orientation: float, joint_obj: Tag) -> None:
        ...


class UFMct(Utilities.NXRemotableObject):
    def ReplaceMachine(self, libref: str, retrieve_opt: int, mounting_opt: UF.NcmctSetupReplaceMode, ncmct_tag: Tag) -> None:
        ...
    def Retrieve(self, libref: str, ncmct_tag: Tag) -> None:
        ...


class UFMb(Utilities.NXRemotableObject):
    def AddActions(self, action_table: typing.List[UF.UFMb.Action]) -> None:
        ...
    def AskButtonId(self, button_name: str, button_id: int) -> None:
        ...
    def AskButtonSensitivity(self, button_id: int, state: UF.UFMb.State) -> None:
        ...
    def AskButtonTypeName(self, type: int, type_name: str) -> None:
        ...
    def AskStringResource(self, name: str, defvalue: str, value: str) -> None:
        ...
    def AskToggleState(self, button_id: int, state: UF.UFMb.State) -> None:
        ...
    def InitApplicationData(self, app_data: UF.UFMb.ApplicationData) -> None:
        ...
    def RegisterApplication(self, app: UF.UFMb.ApplicationData) -> None:
        ...
    def SetButtonSensitivity(self, button_id: int, state: UF.UFMb.State) -> None:
        ...
    def SetToggleState(self, button_id: int, state: UF.UFMb.State) -> None:
        ...


    class State(enum.Enum):
        On = 0
        Off = 1
    

    

    

    

    class CbStatus(enum.Enum):
        CbContinue = 0
        CbCancel = 1
        CbOverrideStandard = 2
        CbWarning = 3
        CbError = 4
    

    class UFMbCb():
        cb: UF.UFMb.CallbackT
        cb_data: int
    

    

    class UFMbApplicationData():
        id: int
        name: str
        init_proc: UF.UFMb.InitProcT
        exit_proc: UF.UFMb.ExitProcT
        enter_proc: UF.UFMb.EnterProcT
        drawings_supported: bool
        design_in_context_supported: bool
        supports_undo: bool
    

    class UFMbAction():
        action_name: str
        action_cb: UF.UFMb.Cb
    

class UFLib(Utilities.NXRemotableObject):
    def AskLibAttributeValues(self, db: int, ug_object: Tag, count: int, db_alias: str, values: str) -> None:
        ...
    def AskLibref(self, ug_object: Tag, libref: str) -> None:
        ...
    def AskRecordInRset(self, rset: int, record_num: int, count: int, values: str) -> None:
        ...
    def AskRsetCount(self, rset: int, count: int) -> None:
        ...
    def AskRsetMap(self, rset: int, count: int, attr_names: str, attr_types: bytes) -> None:
        ...
    def DeleteRset(self, rset: int) -> None:
        ...
    def ExecuteQuery(self, db: int, cls_name: str, query: str, count: int, rset: int) -> None:
        ...
    def ExecuteQueryForCount(self, db: int, cls_name: str, query: str, count: int) -> None:
        ...
    def FreeRsetMap(self, count: int, attr_names: str, attr_types: str) -> None:
        ...
    def MergeRsets(self, rset1: int, rset2: int, merged_rset: int) -> None:
        ...
    def SortRset(self, rset: int, sort_key: str, sorted_rset: int) -> None:
        ...


class UFLayer(Utilities.NXRemotableObject):
    def AskCategoryInfo(self, category: Tag, category_info: UF.UFLayer.CategoryInfo) -> None:
        ...
    def AskCategoryTag(self, category_name: str, category: Tag) -> None:
        ...
    def AskStatus(self, layer_number: int, layer_status: int) -> None:
        ...
    def AskWorkLayer(self, layer_number: int) -> None:
        ...
    def CreateCategory(self, category_info: UF.UFLayer.CategoryInfo, category: Tag) -> None:
        ...
    def CycleByLayer(self, layer_number: int, object_tag: Tag) -> None:
        ...
    def EditCategoryDescr(self, category: Tag, cat_descr: str) -> None:
        ...
    def EditCategoryLayer(self, category: Tag, layer_mask: bool) -> None:
        ...
    def EditCategoryName(self, category: Tag, cat_name: str) -> None:
        ...
    def SetAllButWork(self, layer_status: int) -> None:
        ...
    def SetManyLayersStatus(self, count_of_layers: int, changes: UF.UFLayer.StatusInfo) -> None:
        ...
    def SetStatus(self, layer_number: int, layer_status: int) -> None:
        ...


    class UFLayerStatusInfo():
        layer_number: int
        layer_status: int
    

    class UFLayerCategoryInfo():
        name: str
        layer_mask: bool
        descr: str
    

class UFKfUgmgr(Utilities.NXRemotableObject):
    def AskUserDfaClasses(self, folder_name: str, user_dfa_classes: str, num_classes: int) -> None:
        ...
    def AskUserDfaFuncs(self, folder_name: str, user_dfa_funcs: str, num_funcs: int) -> None:
        ...
    def InitializeExport(self, option: int) -> None:
        ...
    def InitializeImport(self, is_dfa_list: bool) -> None:
        ...
    def IsFolderExists(self, folder_name: str, folder_exists: bool) -> None:
        ...
    def IsItemDfaType(self, item_name: str, dfa_type: bool) -> None:
        ...
    def IsUserDfaClassExists(self, dfa_class_name: str, class_exists: bool) -> None:
        ...
    def IsUserDfaFuncExists(self, dfa_func_name: str, func_exists: bool) -> None:
        ...
    def ListUserClassesReferenced(self, part_tag: Tag, user_classes_list: str, num_classes: int) -> None:
        ...
    def ListUserFuncsReferenced(self, part_tag: Tag, user_funcs_list: str, num_funcs: int) -> None:
        ...


class UFKf(Utilities.NXRemotableObject):
    def AddSearchLibrary(self, path_name: str) -> None:
        ...
    def AdoptNxObjects(self, ug_objects: typing.List[Tag], number_of_objects: int, nx_type: bool, instances: int) -> None:
        ...
    def AdoptUgObjects(self, ug_objects: typing.List[Tag], number_of_objects: int, instances: int) -> None:
        ...
    def AskAllClasses(self, num_classes: int, classes: str) -> None:
        ...
    def AskAncestorClasses(self, class_name: str, n_ancestors: int, ancestor_names: str) -> None:
        ...
    def AskBaseUnitOfMeasure(self, measure: str, base_unit: str) -> None:
        ...
    def AskBoolean(self, value: int, data: bool) -> None:
        ...
    def AskClasses(self, filter_choice: UF.UFKf.ClassType, num_classes: int, classes: str) -> None:
        ...
    def AskDefaultFormula(self, rule: int, formula: str) -> None:
        ...
    def AskError(self, value: int, error: int) -> None:
        ...
    def AskFrame(self, value: int, data: float) -> None:
        ...
    def AskFusionObject(self, ug_object: Tag, instance: int) -> None:
        ...
    def AskInstance(self, value: int, instance: int) -> None:
        ...
    def AskInstanceClass(self, name_chain: str, class_name: str) -> None:
        ...
    def AskInstanceOfArgs(self, values: int, n_values: int, instance: int) -> None:
        ...
    def AskInteger(self, value: int, data: int) -> None:
        ...
    def AskList(self, value: int, list: int) -> None:
        ...
    def AskListCount(self, list: int, count: int) -> None:
        ...
    def AskListItem(self, list: int, index: int, value: int) -> None:
        ...
    def AskListOfInstance(self, name_chain: str, list_object: int) -> None:
        ...
    def AskMeasureOfValue(self, value: int, measure: str) -> None:
        ...
    def AskName(self, value: int, data: int) -> None:
        ...
    def AskNameChainOfInstance(self, instance: int, name_chain: str) -> None:
        ...
    def AskNameOfString(self, _string: str, name: int) -> None:
        ...
    def AskNumber(self, value: int, data: float) -> None:
        ...
    def AskNxClassesEnabled(self, object_in_part: Tag, nx_classes_enabled: bool) -> None:
        ...
    def AskParameterFormula(self, name_chain: str, param_name: str, formula: str) -> None:
        ...
    def AskParameterType(self, name_chain: str, param_name: str, data_type: str) -> None:
        ...
    def AskParameters(self, name_chain: str, parameter_names: str, num_params: int) -> None:
        ...
    def AskPoint(self, value: int, data: float) -> None:
        ...
    def AskRuleName(self, rule: int, rule_name: str) -> None:
        ...
    def AskRuleOfInstance(self, name_chain: str, rule_name: str, rule: int) -> None:
        ...
    def AskRuleOfName(self, class_name: str, rule_name: str, rule: int) -> None:
        ...
    def AskRuleTextOfReferencingObject(self, ug_object_tag: Tag, rule_text: str) -> None:
        ...
    def AskRuleType(self, rule: int, rule_type: str) -> None:
        ...
    def AskRuleTypes(self, num_types: int, data_types: str) -> None:
        ...
    def AskRules(self, name_chain: str, num_rules: int, rules: str) -> None:
        ...
    def AskRulesOfClass(self, class_name: str, num_rules: int, rules: int) -> None:
        ...
    def AskString(self, value: int, _string: str) -> None:
        ...
    def AskStringOfName(self, name: int, _string: str) -> None:
        ...
    def AskTag(self, value: int, data: Tag) -> None:
        ...
    def AskType(self, data: int, type: UF.UFKf.Type) -> None:
        ...
    def AskUgObject(self, instance: int, ug_object: Tag) -> None:
        ...
    def AskUser(self, value: int, data: int) -> None:
        ...
    def AskUserClassDir(self, dir: str) -> None:
        ...
    def AskValueOfListItem(self, list_obj: int, list_index: int, value_str: str, datatype: str, sub_list_obj: int) -> None:
        ...
    def AskVector(self, value: int, data: float) -> None:
        ...
    def CountListItems(self, list: int, n_items: int) -> None:
        ...
    def CreateChildRule(self, part_of_rule: Tag, name_chain: str, rule_name: str, child_class_name: str, num_parameters: int, parameter_names: str, parameter_rules: str, generated_name: str) -> None:
        ...
    def CreateRule(self, name_chain: str, rule_name: str, rule_type: str, rule_text: str, leading_comment: str) -> None:
        ...
    def CreateRuleNoUpdate(self, name_chain: str, rule_name: str, rule_type: str, rule_text: str, leading_comment: str) -> None:
        ...
    def DeleteClassRule(self, class_name: str, rule_name: str) -> None:
        ...
    def DeleteInstanceRule(self, name_chain: str, rule_name: str) -> None:
        ...
    def EvaluateRule(self, name_chain: str, value: int) -> None:
        ...
    def EvaluateRuleToString(self, name_chain: str, value: str) -> None:
        ...
    def FreeListObjectContents(self, list: int) -> None:
        ...
    def FreeRuleValue(self, value: int) -> None:
        ...
    def InitPart(self, part: Tag) -> None:
        ...
    def IsCachedRule(self, rule: int, cached: bool) -> None:
        ...
    def IsCanonicalRule(self, rule: int, canonical: bool) -> None:
        ...
    def IsChildListInstance(self, name_chain: str, is_list_instance: bool) -> None:
        ...
    def IsChildListRule(self, rule: int, is_child_list: bool) -> None:
        ...
    def IsChildRule(self, rule: int, child: bool) -> None:
        ...
    def IsDynamic(self, rule: int, dynamic: bool) -> None:
        ...
    def IsHiddenRule(self, rule: int, hidden: bool) -> None:
        ...
    def IsInitialized(self, is_initialized: bool) -> None:
        ...
    def IsLocal(self, class_name: str, rule: int, local: bool) -> None:
        ...
    def IsLookupRule(self, rule: int, lookup: bool) -> None:
        ...
    def IsMethod(self, rule: int, method: bool) -> None:
        ...
    def IsModifiableRule(self, rule: int, modifiable: bool) -> None:
        ...
    def IsParameterRule(self, rule: int, parameter: bool) -> None:
        ...
    def IsRuleComputed(self, name_chain: str, rule_name: str, evaluated: bool) -> None:
        ...
    def IsRuleInClass(self, class_name: str, rule_name: str, rule_in_class: bool) -> None:
        ...
    def IsUncachedRule(self, rule: int, uncached: bool) -> None:
        ...
    def ListPop(self, list: int, element: int, next: int) -> None:
        ...
    def ListPush(self, list: int, element: int, next: int) -> None:
        ...
    def MakeBoolean(self, data: bool, value: int) -> None:
        ...
    def MakeError(self, data: int, value: int) -> None:
        ...
    def MakeFrame(self, data: float, value: int) -> None:
        ...
    def MakeInstance(self, data: int, value: int) -> None:
        ...
    def MakeInteger(self, data: int, value: int) -> None:
        ...
    def MakeList(self, data: int, value: int) -> None:
        ...
    def MakeName(self, data: int, value: int) -> None:
        ...
    def MakeNumber(self, data: float, value: int) -> None:
        ...
    def MakePoint(self, data: float, value: int) -> None:
        ...
    def MakeString(self, data: str, value: int) -> None:
        ...
    def MakeTag(self, data: Tag, value: int) -> None:
        ...
    def MakeUser(self, data: int, value: int) -> None:
        ...
    def MakeVector(self, data: float, value: int) -> None:
        ...
    def RemoveAllRules(self) -> None:
        ...
    def RemoveRuleOnly(self, name_chain: str, rule_name: str) -> None:
        ...
    def Revert(self, class_name: str) -> None:
        ...
    def SetMeasureOfValue(self, value: int, measure: str) -> None:
        ...
    def SetNxClassesEnabled(self, object_in_part: Tag, nx_classes_enabled: bool) -> None:
        ...
    def SetUserClassDir(self, new_dirs: str, num_dirs: int) -> None:
        ...


    class Type(enum.Enum):
        Null = 0
        ErrorType = 1
        Any = 2
        Boolean = 3
        Defeval = 4
        Frame = 5
        Tag = 6
        Integer = 7
        List = 8
        Marker = 9
        Name = 10
        NoValue = 11
        Number = 12
        Instance = 13
        Point = 14
        String = 15
        Vector = 16
        User = 17
    

    

    class ClassType(enum.Enum):
        AskUserOnly = 0
        AskSystemOnly = 1
        AskAll = 2
    

class UFHmop(Utilities.NXRemotableObject):
    def AskHoleAxis(self, hmop_tag: Tag, rep_feature: int, smart_vector: Tag) -> None:
        ...
    def AskHoleDepth(self, hmop_tag: Tag, rep_feature: int, smart_point: Tag) -> None:
        ...
    def AskHoleTop(self, hmop_tag: Tag, rep_feature: int, smart_point: Tag) -> None:
        ...
    def SetHoleAxis(self, hmop_tag: Tag, rep_feature: int, smart_vector: Tag) -> None:
        ...
    def SetHoleDepth(self, hmop_tag: Tag, rep_feature: int, smart_point: Tag) -> None:
        ...
    def SetHoleTop(self, hmop_tag: Tag, rep_feature: int, smart_point: Tag) -> None:
        ...


class UFHelp(Utilities.NXRemotableObject):
    def ClearContext(self) -> None:
        ...
    def DisplayContext(self, app_context: str) -> None:
        ...
    def DisplayCurrentContext(self) -> None:
        ...
    def DisplayWv(self, map_file: str, locator: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def LoadMapFile(self, filename: str) -> None:
        ...
    def PopContext(self) -> None:
        ...
    def PushContext(self, app_context: str) -> None:
        ...
    def PushPrimaryContext(self, app_context: str) -> None:
        ...
    def ReloadMapFile(self, filename: str) -> None:
        ...
    def SetContextDebug(self, state: int) -> None:
        ...
    def UnloadMapFile(self, filename: str) -> None:
        ...


class UFGroup(Utilities.NXRemotableObject):
    def AddMemberToGroup(self, member_tag: Tag, group_tag: Tag) -> None:
        ...
    def AskAllOwningGroups(self, member_tag: Tag, num_owning_groups: int, owning_groups_p: typing.List[Tag]) -> None:
        ...
    def AskGroupData(self, group_tag: Tag, group_members: typing.List[Tag], count_of_members: int) -> None:
        ...
    def AskGroupOfTag(self, tag_of_interest: Tag, group_tag: Tag) -> None:
        ...
    def CreateGroup(self, group_members: typing.List[Tag], count_of_members: int, group_tag: Tag) -> None:
        ...
    def DelMemberFromGroup(self, member_tag: Tag, group_tag: Tag) -> None:
        ...
    def DelMemberWithRefresh(self, member_tag: Tag, group_tag: Tag) -> None:
        ...
    def IsUniqueMembershipGroup(self, group_tag: Tag, is_UMG: bool) -> None:
        ...
    def SetNonUniqueMembership(self, group_tag: Tag) -> None:
        ...
    def SetUniqueMembership(self, group_tag: Tag) -> None:
        ...
    def UngroupAll(self, group_tag: Tag) -> None:
        ...
    def UngroupTop(self, group_tag: Tag) -> None:
        ...


class UFGexp(Utilities.NXRemotableObject):
    def AskAngleParms(self, feature_tag: Tag, object1: Tag, qualifier1: UF.UFGexp.Qualifier, xform1: Tag, object2: Tag, qualifier2: UF.UFGexp.Qualifier, xform2: Tag) -> None:
        ...
    def AskDistanceParms(self, feature_tag: Tag, ref1: Tag, xform1: Tag, ref2: Tag, xform2: Tag) -> None:
        ...
    def AskLengthParms(self, feature_tag: Tag, ref_object: Tag, xform: Tag) -> None:
        ...
    def CreateAngle(self, from_object: Tag, qualifier1: UF.UFGexp.Qualifier, object1_xform: Tag, to_object: Tag, qualifier2: UF.UFGexp.Qualifier, object2_xform: Tag, feature_tag: Tag, exp_tag: Tag) -> None:
        ...
    def CreateDistance(self, from_object: Tag, object1_xform: Tag, to_object: Tag, object2_xform: Tag, feature_tag: Tag, exp_tag: Tag) -> None:
        ...
    def CreateLength(self, _object: Tag, xform: Tag, feature_tag: Tag, exp_tag: Tag) -> None:
        ...
    def EditAngle(self, feature_tag: Tag, new_from_object: Tag, qualifier1: UF.UFGexp.Qualifier, new_xform1: Tag, new_to_object: Tag, qualifier2: UF.UFGexp.Qualifier, new_xform2: Tag) -> None:
        ...
    def EditDistance(self, feature_tag: Tag, new_from_object: Tag, new_xform1: Tag, new_to_object: Tag, new_xform2: Tag) -> None:
        ...
    def EditLength(self, feature_tag: Tag, new_object: Tag, new_xform: Tag) -> None:
        ...


    class Qualifier(enum.Enum):
        None = 0
        StartPoint = 2
        EndPoint = 3
    

    class ZoneShape(enum.Enum):
        ShapePlanar = 0
        ShapeCylindrical = 1
        ShapeSpherical = 2
        ShapeOffset = 3
    

class UFGdt(Utilities.NXRemotableObject):
    def AddDatumIdentifier(self, tolerance_feature: Tag, datum_data: UF.UFGdt.DatumIdentifier) -> None:
        ...
    def AddDatumToFeature(self, feature: Tag, datum: Tag) -> None:
        ...
    def AddFcf(self, tolerance_feature: Tag, tolerance_data: UF.UFGdt.Fcf, fcf: Tag) -> None:
        ...
    def AddLeader(self, instance: Tag, spec: UF.UFGdt.LeaderSpec) -> None:
        ...
    def AddSizeTolerance(self, tolerance_feature: Tag, size_data: UF.UFGdt.SizeTolerance) -> None:
        ...
    def AskAnnotationTags(self, instance: Tag, tags: UF.UFGdt.AnnotationTags) -> None:
        ...
    def AskAppendedText(self, _object: Tag, location: UF.UFGdt.TextLocation, num_lines: int, appended_text: str) -> None:
        ...
    def AskAssociatedDatums(self, feature_instance: Tag, associated_datums: typing.List[Tag], num_associated_datums: int) -> None:
        ...
    def AskAssociationType(self, datum_instance: Tag, assoc_type: UF.UFGdt.DatumAssocType) -> None:
        ...
    def AskCalloutStrings(self, tolerance: Tag, num_callout_strings: int, callout_strings: typing.List[UF.UFGdt.CalloutString]) -> None:
        ...
    def AskCharacteristic(self, fcf: Tag, characteristic: UF.UFGdt.Characteristic) -> None:
        ...
    def AskComplexFeature(self, complex_sub_feature: Tag, complex_feature: Tag) -> None:
        ...
    def AskComplexSubFeatures(self, complex_feature: Tag, num_complex_sub_features: int, complex_sub_features: typing.List[Tag]) -> None:
        ...
    def AskComponentToleranceIndex(self, tolerance: Tag, index: int) -> None:
        ...
    def AskCompositeDrf(self, fcf: Tag, priority: UF.UFGdt.Precedence) -> None:
        ...
    def AskDatumByLabel(self, datum_label: str, datum: Tag) -> None:
        ...
    def AskDatumIdentParms(self, _base: Tag, datum_data: typing.List[UF.UFGdt.DatumIdentifier]) -> None:
        ...
    def AskDatumKeywords(self, datum: Tag, num_keywords: int, keywords: typing.List[UF.UFGdt.Keyword]) -> None:
        ...
    def AskDatumMultipleParms(self, multiple_datum: Tag, datum_data: typing.List[UF.UFGdt.MultipleDatum]) -> None:
        ...
    def AskDatumOfLabel(self, datum_label: str, datum_feature: Tag) -> None:
        ...
    def AskDatumOfTarget(self, target: Tag, datum: Tag) -> None:
        ...
    def AskDatumReferencers(self, _base: Tag, num_fcfs: int, fcfs: typing.List[Tag]) -> None:
        ...
    def AskDatumReferences(self, fcf: Tag, nth_frame: int, num_refs: int, datum_reference: typing.List[UF.UFGdt.DatumReference]) -> None:
        ...
    def AskDatumsOfFeature(self, datum_feature: Tag, datums: typing.List[Tag], num_datums: int) -> None:
        ...
    def AskDepthToleranceParms(self, tolerance_feature: Tag, depth_data: typing.List[UF.UFGdt.DepthTolerance]) -> None:
        ...
    def AskDescription(self, tolerance_feature: Tag, info: typing.List[UF.UFGdt.Description]) -> None:
        ...
    def AskDirectedDimension1(self, tolerance_feature: Tag, data: typing.List[UF.UFGdt.DirectedDimension1]) -> None:
        ...
    def AskDrf(self, drf: Tag, drf_data: typing.List[UF.UFGdt.DrfData]) -> None:
        ...
    def AskFaceFromIndex(self, geometry_index: int, geometry: Tag) -> None:
        ...
    def AskFaceIndex(self, geometry: Tag, geometry_index: int) -> None:
        ...
    def AskFaceIndexString(self, face_tag: Tag, index_string: str) -> None:
        ...
    def AskFaces(self, tolerance_feature: Tag, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def AskFcfDrf(self, fcf: Tag, drf: Tag) -> None:
        ...
    def AskFcfParms(self, fcf: Tag, fcf_data: typing.List[UF.UFGdt.Fcf]) -> None:
        ...
    def AskFcfTags(self, tolerance_feature: Tag, num_fcfs: int, fcfs: typing.List[Tag]) -> None:
        ...
    def AskFeatureOfDatum(self, datum: Tag, feature: Tag) -> None:
        ...
    def AskFeatureType(self, tolerance_feature: Tag, feature: UF.UFGdt.FeatureType) -> None:
        ...
    def AskFeaturesOfFace(self, face: Tag, tolerance_features: typing.List[Tag], num_tolerance_features: int) -> None:
        ...
    def AskGdtObjectDfaFile(self, gdt_object: Tag, dfa_file: str) -> None:
        ...
    def AskGdtViewMatrix(self, view: Tag, gdt_matrix: float) -> None:
        ...
    def AskGeometricDefinition(self, tolerance_feature: Tag, data: typing.List[UF.UFGdt.GeometricDefinition]) -> None:
        ...
    def AskIndexDisplay(self, index_display: UF.UFGdt.IndexDisplayType) -> None:
        ...
    def AskInstanceDisplayInformation(self, preference: bool) -> None:
        ...
    def AskKeywordName(self, part_tag: Tag, keyword_id: int, keyword_name: str) -> None:
        ...
    def AskKeywordText(self, part_tag: Tag, keyword_name: str, keyword_text: str) -> None:
        ...
    def AskLabelOfDatum(self, _base: Tag, datum_label: str) -> None:
        ...
    def AskLeader(self, instance: Tag, nth: int, spec: UF.UFGdt.LeaderSpec) -> None:
        ...
    def AskLimitsAndFitsToleranceParms(self, tolerance_feature: Tag, data: typing.List[UF.UFGdt.LimitsAndFitsTolerance]) -> None:
        ...
    def AskLinkedFeatures(self, tolerance_feature: Tag, num_linked: int, linked_features: typing.List[Tag]) -> None:
        ...
    def AskLoadComponentFlag(self, flag: bool) -> None:
        ...
    def AskMajorDiaFeatureOfSplineGear(self, tolerance_feature: Tag, major_dia_feature: Tag) -> None:
        ...
    def AskMinorDiaFeatureOfSplineGear(self, tolerance_feature: Tag, minor_dia_feature: Tag) -> None:
        ...
    def AskModlData(self, tolerance_feature: Tag, num_modl_sets: int, modl_sets: typing.List[UF.UFGdt.ModlData]) -> None:
        ...
    def AskModlFeatures(self, tolerance_feature: Tag, num_modl_features: int, modl_features: typing.List[Tag]) -> None:
        ...
    def AskNonFeatureEdgeSelection(self, allow_non_feature_edges: UF.UFGdt.EdgeSelectType) -> None:
        ...
    def AskNumLeaders(self, instance: Tag, num_leaders: int) -> None:
        ...
    def AskPitchDiaFeatureOfSplineGear(self, tolerance_feature: Tag, pitch_dia_feature: Tag) -> None:
        ...
    def AskProductAttributes(self, tolerance_feature: Tag, num_product_atts: int, product_atts: typing.List[Tag]) -> None:
        ...
    def AskProfileTolData(self, fcf: Tag, profile_type: UF.UFGdt.ProfileType, outside: UF.UFGdt.ToleranceValue) -> None:
        ...
    def AskPulledToleranceComponent(self, tolerance: Tag, component_part_occ: Tag) -> None:
        ...
    def AskSizeToleranceParms(self, tolerance_feature: Tag, size_data: typing.List[UF.UFGdt.SizeTolerance]) -> None:
        ...
    def AskSizeToleranceTag(self, tolerance_feature: Tag, size_tolerance: Tag) -> None:
        ...
    def AskSubFeatures(self, tolerance_feature: Tag, num_sub_features: int, sub_features: typing.List[Tag]) -> None:
        ...
    def AskSuperFeature(self, tolerance_feature: Tag, super_feature: Tag) -> None:
        ...
    def AskTableOfInstance(self, feature_instance: Tag, table: Tag) -> None:
        ...
    def AskTags(self, display_instance: Tag, curves: typing.List[Tag], num_curves: int, annotations: typing.List[Tag], num_annotations: int) -> None:
        ...
    def AskTargetAreaXhatch(self, target_inst: Tag, distance: float, angle: float) -> None:
        ...
    def AskTargetCylParms(self, target: Tag, data: typing.List[UF.UFGdt.TargetCylArea]) -> None:
        ...
    def AskTargetDiaParms(self, target: Tag, data: typing.List[UF.UFGdt.TargetDiaArea]) -> None:
        ...
    def AskTargetLineParms(self, target: Tag, data: typing.List[UF.UFGdt.DatumTargetLine]) -> None:
        ...
    def AskTargetPointParms(self, target: Tag, data: typing.List[UF.UFGdt.DatumTargetPoint]) -> None:
        ...
    def AskTargetRectParms(self, target: Tag, data: typing.List[UF.UFGdt.TargetRectArea]) -> None:
        ...
    def AskTargetUdefParms(self, target: Tag, data: typing.List[UF.UFGdt.TargetUdefArea]) -> None:
        ...
    def AskTargetsOfDatum(self, datum: Tag, num_targets: int, targets: typing.List[Tag]) -> None:
        ...
    def AskThreadToleranceParms(self, tolerance_feature: Tag, data: typing.List[UF.UFGdt.ThreadTolerance]) -> None:
        ...
    def AskTolFeatInstance(self, tolerance_feature: Tag, num_instances: int, feature_instances: typing.List[Tag]) -> None:
        ...
    def AskTolFeatOfInstance(self, feature_instance: Tag, tolerance_feature: Tag) -> None:
        ...
    def AskTolFeatTag(self, tolerance: Tag, tolerance_feature: Tag) -> None:
        ...
    def AskTolerance(self, tol_feat: Tag, type: UF.UFGdt.ToleranceType, tolerance: Tag) -> None:
        ...
    def AskToleranceFromIndex(self, index: int, requirement: Tag, fcf: Tag) -> None:
        ...
    def AskToleranceIndex(self, requirement: Tag, index: int) -> None:
        ...
    def AskToleranceIndexString(self, tolerance_tag: Tag, index_string: str) -> None:
        ...
    def AskToleranceTypes(self, tolerance_feature: Tag, num_types: int, types: typing.List[UF.UFGdt.ToleranceType]) -> None:
        ...
    def AskToleranceZone(self, fcf: Tag, nth_zone: int, zone: typing.List[UF.UFGdt.ToleranceZone], frame_mod: typing.List[UF.UFGdt.ModifierData]) -> None:
        ...
    def AskTolerances(self, tol_feat: Tag, tolerances: typing.List[Tag], num_tolerances: int, types: typing.List[UF.UFGdt.ToleranceType]) -> None:
        ...
    def AskTolerancingStandard(self, standard: UF.UFGdt.Standard) -> None:
        ...
    def AskUnitBasis(self, fcf: Tag, modifier: UF.UFGdt.ModifierTypes, data: UF.UFGdt.UnitBasis) -> None:
        ...
    def AskWallThicknessParms(self, tolerance_feature: Tag, size_data: typing.List[UF.UFGdt.SizeTolerance]) -> None:
        ...
    def BreakRelationship(self, tolerance_feature: Tag, relationship_type: UF.UFGdt.RelationType) -> None:
        ...
    def CreateDrf(self, drf_data: UF.UFGdt.DrfData, drf: Tag) -> None:
        ...
    def CreateInstance(self, type: UF.UFGdt.ToleranceType, tolerance_feature: Tag, view: Tag, edge: Tag, origin: float, attach_point: float, feature_instance: Tag) -> None:
        ...
    def CreateTableInstance(self, tolerance_feature: Tag, view: Tag, origin: float, feature_instance: Tag) -> None:
        ...
    def CreateTargetCylArea(self, target_data: UF.UFGdt.TargetCylArea, target_area: Tag) -> None:
        ...
    def CreateTargetDiaArea(self, target_data: UF.UFGdt.TargetDiaArea, target_area: Tag) -> None:
        ...
    def CreateTargetLine(self, target_data: UF.UFGdt.DatumTargetLine, target_line: Tag) -> None:
        ...
    def CreateTargetPoint(self, target_data: UF.UFGdt.DatumTargetPoint, point: Tag) -> None:
        ...
    def CreateTargetRectArea(self, target_data: UF.UFGdt.TargetRectArea, target_area: Tag) -> None:
        ...
    def CreateTargetUdefArea(self, target_data: UF.UFGdt.TargetUdefArea, target_area: Tag) -> None:
        ...
    def ExportDrawings(self, num_drawings: int, drawings: typing.List[Tag], target_part: Tag) -> None:
        ...
    def Free(self, type: UF.UFGdt.DataType, data: int) -> None:
        ...
    def HasDepthTolerance(self, tolerance_feature: Tag, has_depth_tolerance: bool) -> None:
        ...
    def HasDirectedDimension(self, tolerance_feature: Tag, has_directed_dimension: bool) -> None:
        ...
    def HasGeometricDefinition(self, tolerance_feature: Tag, has_geometric_definition: bool) -> None:
        ...
    def HasLimitsAndFitsTolerance(self, tolerance_feature: Tag, has_limits_and_fits_tolerance: bool) -> None:
        ...
    def HasSizeTolerance(self, tolerance_feature: Tag, has_size_tolerance: bool) -> None:
        ...
    def HasWallThickness(self, tolerance_feature: Tag, has_wall_thickness: bool) -> None:
        ...
    def InheritModelGdtToDrawing(self, member_view: Tag) -> None:
        ...
    def Init(self, type: UF.UFGdt.DataType, data: int) -> None:
        ...
    def IsComplexFeature(self, tolerance_tag: Tag, status: bool) -> None:
        ...
    def IsComplexSubFeature(self, tolerance_tag: Tag, status: bool) -> None:
        ...
    def IsCompositeTolerance(self, fcf: Tag, is_composite_tol: bool) -> None:
        ...
    def IsDatum(self, tolerance_feature: Tag, is_datum: bool) -> None:
        ...
    def IsDatumTarget(self, tolerance_feature: Tag, is_datum_target: bool) -> None:
        ...
    def IsFeatureOfSize(self, tolerance_feature: Tag, feature_of_size: bool) -> None:
        ...
    def IsGdtView(self, view: Tag, is_gdt_view: bool) -> None:
        ...
    def IsLinkedFeature(self, tolerance_feature: Tag, is_linked: bool) -> None:
        ...
    def IsModlBased(self, tolerance_feature: Tag, is_modl_based: bool) -> None:
        ...
    def IsPulledTolerance(self, tolerance_feature: Tag, status: bool) -> None:
        ...
    def IsRetained(self, tolerance_feature: Tag, is_retained: bool) -> None:
        ...
    def IsSingleDatumReferenceFrame(self, frame: Tag, is_single: bool) -> None:
        ...
    def IsUserDefinedKeyword(self, part_tag: Tag, keyword_id: int, status: bool) -> None:
        ...
    def PullTolerance(self, tolerance_feature: Tag, instance: Tag, new_feature_tag: Tag, create_instance: bool) -> None:
        ...
    def RemoveLeader(self, instance: Tag, nth: int) -> None:
        ...
    def ResetCalloutRules(self, part: Tag) -> None:
        ...
    def SetAppendedText(self, fcf_or_dim: Tag, location: UF.UFGdt.TextLocation, num_lines: int, appended_text: str) -> None:
        ...
    def SetCharacteristic(self, fcf: Tag, characteristic: UF.UFGdt.Characteristic) -> None:
        ...
    def SetCompositeDrf(self, fcf: Tag, priority: UF.UFGdt.Precedence) -> None:
        ...
    def SetDatumIdentifier(self, _base: Tag, datum_data: UF.UFGdt.DatumIdentifier) -> None:
        ...
    def SetDatumKeywords(self, datum: Tag, num_keywords: int, keywords: typing.List[UF.UFGdt.Keyword]) -> None:
        ...
    def SetDatumLabel(self, _base: Tag, datum_label: str) -> None:
        ...
    def SetDatumMultiple(self, multiple_datum: Tag, datum_data: UF.UFGdt.MultipleDatum) -> None:
        ...
    def SetDatumReferences(self, fcf: Tag, nth_frame: int, num_frames: int, datum_reference: UF.UFGdt.DatumReference) -> None:
        ...
    def SetDepthToleranceParms(self, tolerance_feature: Tag, depth_data: UF.UFGdt.DepthTolerance) -> None:
        ...
    def SetDescription(self, tolerance_feature: Tag, info: UF.UFGdt.Description) -> None:
        ...
    def SetDirectedDimension(self, tolerance_feature: Tag, data: UF.UFGdt.DirectedDimension) -> None:
        ...
    def SetDrf(self, drf: Tag, drf_data: UF.UFGdt.DrfData) -> None:
        ...
    def SetFaces(self, tolerance_feature: Tag, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def SetFcf(self, fcf: Tag, fcf_data: UF.UFGdt.Fcf) -> None:
        ...
    def SetFcfDrf(self, fcf: Tag, drf: Tag) -> None:
        ...
    def SetGeometricDefinition(self, tolerance_feature: Tag, data: UF.UFGdt.GeometricDefinition) -> None:
        ...
    def SetIndexDisplay(self, index_display: UF.UFGdt.IndexDisplayType) -> None:
        ...
    def SetInstanceDisplayInformation(self, preference: bool) -> None:
        ...
    def SetKeywordText(self, part_tag: Tag, keyword_name: str, keyword_text: str) -> None:
        ...
    def SetLimitsAndFitsToleranceParms(self, tolerance_feature: Tag, data: UF.UFGdt.LimitsAndFitsData) -> None:
        ...
    def SetLoadComponentFlag(self, flag: bool) -> None:
        ...
    def SetNonFeatureEdgeSelection(self, allow_non_feature_edges: UF.UFGdt.EdgeSelectType) -> None:
        ...
    def SetProfileTolData(self, fcf: Tag, profile_type: UF.UFGdt.ProfileType, outside: UF.UFGdt.ToleranceValue) -> None:
        ...
    def SetRegionParameters(self, region_thickness: float, crosshatch_on: bool, crosshatch_angle: float, crosshatch_distance: float) -> None:
        ...
    def SetSizeData(self, tolerance_feature: Tag, lim_fits: UF.UFGdt.LimitsAndFitsTolerance) -> None:
        ...
    def SetSizeToleranceParms(self, tolerance_feature: Tag, size_data: UF.UFGdt.SizeTolerance) -> None:
        ...
    def SetTargetAreaXhatch(self, target_inst: Tag, distance: float, angle: float) -> None:
        ...
    def SetThreadToleranceParms(self, tolerance_feature: Tag, data: UF.UFGdt.ThreadTolerance) -> None:
        ...
    def SetToleranceZones(self, fcf: Tag, num_zones: int, zones: typing.List[UF.UFGdt.ToleranceZone], mod_data: UF.UFGdt.ModifierData) -> None:
        ...
    def SetTolerancingStandard(self, standard: UF.UFGdt.Standard) -> None:
        ...
    def SetUnitBasis(self, fcf: Tag, modifier: UF.UFGdt.ModifierTypes, data: UF.UFGdt.UnitBasis) -> None:
        ...
    def SetWallThicknessParms(self, tolerance_feature: Tag, thickness_data: UF.UFGdt.SizeTolerance) -> None:
        ...
    def UpdateFeatures(self, num_features: int, features: typing.List[Tag]) -> None:
        ...
    def UpgradeLegacyFeature(self, num_annot: int, annotation_features: typing.List[Tag], num_faces: int, face_list: typing.List[Tag], feature: UF.UFGdt.FeatureType, origin: float, descript: UF.UFGdt.Description, tolerance_feature: Tag) -> None:
        ...


    class UFGdtUnitBasis():
        tolerance_expression: Tag
        length_expression: Tag
        width_expression: Tag
        decimal_format: int
        ub_decimal_format: int
    

    class TolFormat(enum.Enum):
        LimMinusBeforePlus = 0
        LimPlusBeforeMinus = 1
        LimMinusOverPlus = 2
        LimPlusOverMinus = 3
        PlusOverMinus = 4
        MinusOverPlus = 5
        PlusMinus = 6
        NoTolerance = 7
    

    class UFGdtToleranceZone():
        zone_shape: UF.UFGdt.ZoneShape
        planar_ref: Tag
        expression: Tag
        value: float
        decimal_format: int
        material_modifier: UF.UFGdt.MaterialModifier
    

    class UFGdtToleranceValue():
        expression: Tag
        value: float
        decimal_format: int
    

    class ToleranceType(enum.Enum):
        DatumTargetPointType = 0
        DatumTargetLineType = 1
        DatumIdentifierType = 3
        DatumMultipleType = 4
        GeometricToleranceType = 5
        SizeToleranceType = 6
        DatumTargetDiaType = 7
        DatumTargetRectType = 8
        DirectedDimensionType = 9
        DatumTargetCylType = 10
        WallThicknessType = 11
        DepthToleranceType = 12
        LimitsAndFitsToleranceType = 13
        ThreadToleranceType = 14
        DatumTargetUserDefinedType = 15
    

    class UFGdtThreadTolerance():
        thread_tol: typing.List[UF.UFGdt.ThreadData]
        modifier_data: typing.List[UF.UFGdt.ModifierData]
    

    class UFGdtThreadData():
        pitch_dia_grade: int
        pitch_dia_deviation: str
        grade: int
        deviation: str
        thread_class: int
    

    class TextLocation(enum.Enum):
        Above = 0
        Below = 1
        Before = 2
        After = 3
    

    class UFGdtTargetUdefArea():
        datum_feature: Tag
        target_index: int
        curves: typing.List[Tag]
        num_curves: int
        is_planar: bool
        np_data: UF.UFGdt.TargetNonPlanarData
    

    class UFGdtTargetRectArea():
        datum_feature: Tag
        target_index: int
        point: Tag
        is_planar: bool
        orientation: Tag
        length: UF.UFGdt.ToleranceValue
        height: UF.UFGdt.ToleranceValue
        location: float
    

    class UFGdtTargetNonPlanarData():
        project_normals: bool
        projection_vector: float
        point_key: int
        point_coords: float
    

    class UFGdtTargetDiaArea():
        datum_feature: Tag
        target_index: int
        point: Tag
        diameter: UF.UFGdt.ToleranceValue
        inner_dia: UF.UFGdt.ToleranceValue
        is_planar: bool
        orientation: Tag
        location: float
    

    class UFGdtTargetCylArea():
        datum_feature: Tag
        target_index: int
        start_point: Tag
        end_point: Tag
        start_location: float
        end_location: float
    

    class UFGdtSurfaceParms():
        num_faces: int
        faces: typing.List[Tag]
    

    class StubDirection(enum.Enum):
        StubLeft = 1
        StubRight = 2
        StubUp = 3
        StubDown = 4
    

    class UFGdtStatisticalInfo():
        other_statistical_data: int
    

    class Standard(enum.Enum):
        NoStandard = 0
        Ansi1982 = 1
        Asme1994 = 2
        Iso1983 = 3
    

    class SizeValueType(enum.Enum):
        NoSize = 0
        LinearSize = 1
        RadialSize = 2
        DiametralSize = 3
        AngularMajorSize = 4
        AngularMinorSize = 5
    

    class UFGdtSizeTolerance():
        value_type: UF.UFGdt.SizeValueType
        dimension: Tag
        nominal_value: float
        upper_tol: UF.UFGdt.ToleranceValue
        lower_tol: UF.UFGdt.ToleranceValue
        tol_format: UF.UFGdt.TolFormat
        modifier_data: typing.List[UF.UFGdt.ModifierData]
        decimal_format: int
    

    class RelationType(enum.Enum):
        PullRelationType = 0
    

    class UFGdtProjZone():
        expression: Tag
        value: float
        decimal_format: int
        direction: Tag
    

    class ProfileType(enum.Enum):
        ProfileEqBilateral = 0
        ProfileUnilateralOut = 1
        ProfileUnilateralIn = 2
        ProfileUneqBilateral = 3
    

    class UFGdtProductAttribute():
        num_attributes: int
        attributes: typing.List[UF.UFPd.ProductAttribute]
    

    class Precedence(enum.Enum):
        PrecedenceNone = 0
        PrecedencePrimary = 1
        PrecedenceSecondary = 2
        PrecedenceTertiary = 3
    

    class UFGdtPoint():
        coords: float
    

    class PatternType(enum.Enum):
        NoPattern = 0
        RadialPattern = 1
        RectangularPattern = 2
        ArbitraryPattern = 3
    

    class UFGdtMultipleDatum():
        num_datums: int
        datum_features: typing.List[Tag]
        def_feat: Tag
    

    class ModlParameter(enum.Enum):
        ModlParamInvalid = 0
        ModlParamNone = 1
        ModlParamAll = 2
        ModlParamHole = 3
        ModlParamCounterbore = 4
        ModlParamCountersink = 5
        ModlParamXLength = 6
        ModlParamYLength = 7
        ModlParamXLengthTop = 8
        ModlParamYLengthTop = 9
    

    class UFGdtModlData():
        num_modl_features: int
        modl_feature_list: typing.List[Tag]
        modl_param: UF.UFGdt.ModlParameter
        face_map: Tag
    

    class ModifierTypes(enum.Enum):
        FreeState = 0
        UnitBasisLength = 1
        UnitBasisArea = 2
        ProjectedZone = 3
        Statistical = 4
        NoModifiers = 5
        MaxBonus = 6
        PatternCount = 7
        IndividualCount = 8
        SepReqt = 9
        SimReqt = 10
        Boundary = 11
        AllOver = 12
        AvgDia = 13
        CoaxHoleCount = 14
        NonMandatoryMfgData = 15
        NoPerfectMmcForm = 16
        PerfectMmcOrientation = 17
        PerfectMmcCoaxiality = 18
        PerfectMmcSymFeatLoc = 19
        SurfaceCount = 20
        Thru = 21
        ThruHole = 22
    

    class UFGdtModifierData():
        num_modifiers: int
        modifier_types: typing.List[UF.UFGdt.ModifierTypes]
        proj_zone: typing.List[UF.UFGdt.ProjZone]
        unit_length: typing.List[UF.UFGdt.UnitBasis]
        unit_area: typing.List[UF.UFGdt.UnitBasis]
        statistics: typing.List[UF.UFGdt.StatisticalInfo]
        bonus_tol: typing.List[UF.UFGdt.ToleranceValue]
        num_keywords: int
        keywords: typing.List[UF.UFGdt.Keyword]
    

    class MaterialModifier(enum.Enum):
        Mmc = 0
        Lmc = 1
        Rfs = 2
        Tangential = 3
        NoMod = 4
    

    class UFGdtLimitsAndFitsTolerance():
        limits_and_fits_data: typing.List[UF.UFGdt.LimitsAndFitsData]
        plus_minus_data: typing.List[UF.UFGdt.SizeTolerance]
    

    class LimitsAndFitsDisplayType(enum.Enum):
        DefaultDisplayType = 0
        LimitsDisplayType = 1
        ToleranceDisplayType = 2
        NormalDisplayType = 3
    

    class UFGdtLimitsAndFitsData():
        deviation: str
        fit_type: str
        fit_grade: int
        tol_grade: int
        dim_precision: int
        display_type: UF.UFGdt.LimitsAndFitsDisplayType
    

    class LeaderType(enum.Enum):
        LeaderNonTerminated = 0
        LeaderDatum = 1
        LeaderArrowhead = 2
        LeaderDot = 3
    

    class UFGdtLeaderSpec():
        view: Tag
        terminator: Tag
        attach_point: UF.UFGdt.Point
        stub_points: typing.List[UF.UFGdt.Point]
        num_intermediates: int
        intermediates: typing.List[UF.UFGdt.Point]
        type: UF.UFGdt.LeaderType
        is_profile_leader: bool
        filled: bool
        all_around: bool
        all_around_diameter: float
        dot_diameter: float
        arrowhead_length: float
        arrowhead_angle: float
        stub_length: float
        direction: UF.UFGdt.StubDirection
        profile_term2: Tag
        profile_attach: UF.UFGdt.Point
        profile_ldr_length: float
        leader_color: int
        leader_font: int
        leader_width: int
        arrowhead_color: int
        arrowhead_font: int
        arrowhead_width: int
        arrow_info: UF.UFDrf.ArrowInfo
    

    class UFGdtKeyword():
        id: int
    

    class IndexDisplayType(enum.Enum):
        Unique = 0
        PartBased = 1
    

    class GeometricDefinitionType(enum.Enum):
        AllGeometry = 0
        PlanarOrientation = 1
        PlanarCrossSection = 2
        Region = 3
        Point = 4
        RectangularRegion = 5
        CircularRegion = 6
    

    class UFGdtGeometricDefinition():
        type: UF.UFGdt.GeometricDefinitionType
        so_tag: Tag
        radius: float
        trimmed_sheet: Tag
    

    class FeatureType(enum.Enum):
        GeneralFeature = 0
        SlotFeature = 1
        TabFeature = 2
        HoleFeature = 3
        PinFeature = 4
        SocketFeature = 5
        BallFeature = 6
        ElongatedHoleFeature = 7
        PlaneFeature = 8
        BoundedFeature = 9
        TaperedHoleFeature = 10
        TaperedPinFeature = 11
        HollowTorusFeature = 12
        SolidTorusFeature = 13
        HollowRevolvedFeature = 14
        SolidRevolvedFeature = 15
        CounterboreHoleFeature = 16
        CountersinkHoleFeature = 17
        EdgeBlendFeature = 18
        ThicknessGapFeature = 19
        SteppedShaftFeature = 20
        SteppedHoleFeature = 21
        ComplexElongatedHoleFeature = 22
        OpposedPointFeature = 23
        OpposedLineFeature = 24
        ThreadFeature = 25
        ModelAxisFeature = 26
        ModelPlaneFeature = 27
        SplineFeature = 28
        GearFeature = 29
        CircularToothThicknessFeature = 30
        CircularSpaceWidthFeature = 31
        PinMeasurementFeature = 32
    

    

    class UFGdtFcf():
        characteristic: UF.UFGdt.Characteristic
        num_frames: int
        data_frame: typing.List[UF.UFGdt.DataFrame]
    

    class EdgeSelectType(enum.Enum):
        EdgeSelectOn = 1
        EdgeSelectOff = 2
        EdgeSelectAlways = 3
    

    class UFGdtDrfReference():
        datum_reference: UF.UFGdt.DatumReference
        definition: Tag
    

    class UFGdtDrfData():
        name: str
        description: str
        primary: typing.List[UF.UFGdt.DrfReference]
        secondary: typing.List[UF.UFGdt.DrfReference]
        tertiary: typing.List[UF.UFGdt.DrfReference]
    

    class DirectedDimensionType(enum.Enum):
        LinearDirectedDimension = 0
        AngularDirectedDimension = 1
    

    class UFGdtDirectedDimension1():
        type: UF.UFGdt.DirectedDimensionType
        size_data: typing.List[UF.UFGdt.SizeTolerance]
        origin: Tag
        origin_surfs: typing.List[UF.UFGdt.SurfaceParms]
        origin_def: UF.UFGdt.GeometricDefinition
    

    class UFGdtDirectedDimension():
        type: UF.UFGdt.DirectedDimensionType
        size_data: UF.UFGdt.SizeTolerance
        origin: Tag
        origin_surfs: typing.List[UF.UFGdt.SurfaceParms]
        origin_def: UF.UFGdt.GeometricDefinition
    

    class UFGdtDescription():
        name: str
        description: str
    

    class UFGdtDepthTolerance():
        nominal_value: float
        upper_tol: UF.UFGdt.ToleranceValue
        lower_tol: UF.UFGdt.ToleranceValue
        tol_format: UF.UFGdt.TolFormat
        decimal_format: int
    

    class UFGdtDatumTargetPoint():
        point_on_surface: Tag
        point_data: float
        datum_feature: Tag
        target_index: int
    

    class UFGdtDatumTargetLine():
        start_point: Tag
        end_point: Tag
        start_data: float
        end_data: float
        datum_feature: Tag
        target_index: int
    

    class UFGdtDatumReference():
        datum_feature: Tag
        material_condition: typing.List[UF.UFGdt.MaterialModifier]
        num_modifiers: int
    

    class UFGdtDatumIdentifier():
        datum_label: str
        def_feat: Tag
        is_individual: bool
    

    class DatumAssocType(enum.Enum):
        FeatureEdge = 0
        DottedDatum = 1
        AttachedToFcf = 2
        AttachedToStub = 3
        DirectedDatum = 4
        ExtensionLine = 5
    

    class DataType(enum.Enum):
        DataFrameType = 0
        DatumIdentType = 1
        DatumRefType = 2
        DescriptType = 3
        DirectedDimType = 4
        FcfType = 5
        ModDataType = 6
        MultiDatumType = 7
        SizeTolType = 8
        StatisticalType = 9
        SurfaceParmsType = 10
        TargetPointType = 11
        TargetLineType = 12
        TargetAreaType = 13
        TolValueType = 14
        TolZoneType = 15
        FeatParmsType = 16
        DiaAreaType = 17
        RectAreaType = 18
        CylAreaType = 19
        UdefAreaType = 20
        AnnotationTagsType = 21
        CalloutStrType = 22
        DepthTolType = 23
        LimFitsTolType = 24
        DatumRefFrameType = 25
        ThreadType = 26
        ModlDataType = 27
        ProductAttType = 28
    

    class UFGdtDataFrame():
        tolerance_zone: typing.List[UF.UFGdt.ToleranceZone]
        primary: typing.List[UF.UFGdt.DatumReference]
        secondary: typing.List[UF.UFGdt.DatumReference]
        tertiary: typing.List[UF.UFGdt.DatumReference]
        modifier_data: typing.List[UF.UFGdt.ModifierData]
    

    class Characteristic(enum.Enum):
        StraightnessType = 0
        FlatnessType = 1
        CircularType = 2
        CylindricalType = 3
        LineProfileType = 4
        SurfaceProfileType = 5
        AngularType = 6
        PerpendicularType = 7
        ParallelType = 8
        PositionType = 9
        ConcentricType = 10
        SymmetricType = 11
        CircularRunoutType = 12
        TotalRunoutType = 13
    

    class UFGdtCalloutString():
        tolerance: Tag
        type: UF.UFGdt.ToleranceType
        _string: str
    

    class UFGdtAnnotationTags():
        dimension_tags: typing.List[Tag]
        num_dimension_tags: int
        feature_control_frame_tags: typing.List[Tag]
        num_feature_control_frame_tags: int
        appended_text_tags: typing.List[Tag]
        num_appended_text_tags: int
        num_non_dimensional_leaders: int
    

class UFForgeo(Utilities.NXRemotableObject):
    def RegisterSurface(self, create_function: UF.UFForgeo.CreateSurfaceFT, ask_params_function: UF.UFForgeo.AskSurfaceParamsFT, evaluate_function: UF.UFForgeo.EvaluateSurfaceFT) -> None:
        ...


    

    

    

class UFFltr(Utilities.NXRemotableObject):
    def AskBoxOfAssy(self, assy: Tag, centroid: float, corner: float, orientation: float) -> None:
        ...
    def AskBoxZone(self, box_zone: Tag, name: str, centroid: float, corner: float, matrix: float) -> None:
        ...
    def AskFilter(self, filter_tag: Tag, name: str, condition: str) -> None:
        ...
    def AskPlaneZone(self, plane_zone: Tag, name: str, origin: float, matrix: float) -> None:
        ...
    def AutoCreateBoxZones(self, part_tag: Tag, prefix_text: str, num_in_dir: int, use_part_volume: bool, user_spec_vol: float, user_spec_origin: float, zone_list: typing.List[Tag], num_zones_created: int) -> None:
        ...
    def AutoCreatePlaneZones(self, part_tag: Tag, prefix_text: str, num_in_dir: int, use_part_disp: bool, user_spec_z_disp: float, user_spec_origin: float, zone_list: typing.List[Tag], num_zones_created: int) -> None:
        ...
    def CreateBoxZone(self, part_tag: Tag, name: str, centroid: float, corner: float, orientation: float, zone_tag: Tag) -> None:
        ...
    def CreateFilter(self, part_tag: Tag, name: str, condition: str, zone_tag: Tag) -> None:
        ...
    def CreatePlaneZone(self, part_tag: Tag, name: str, origin: float, orientation: float, zone_tag: Tag) -> None:
        ...
    def EditBoxZone(self, zone: Tag, name: str, centroid: float, corner: float, matrix: float) -> None:
        ...
    def EditFilter(self, filter_tag: Tag, name: str, condition: str) -> None:
        ...
    def EditPlaneZone(self, zone: Tag, name: str, origin: float, matrix: float) -> None:
        ...
    def EvaluateFilter(self, input_object: Tag, filter_tag: Tag, result: bool) -> None:
        ...
    def IsObjAbovePlaneZone(self, zone: Tag, _object: Tag, result: bool) -> None:
        ...
    def IsObjInsideBoxZone(self, distance: float, zone: Tag, _object: Tag, result: bool) -> None:
        ...
    def IsObjIntsctZone(self, distance: float, zone: Tag, _object: Tag, result: bool) -> None:
        ...
    def ObjectHasBox(self, _object: Tag, has_box: bool) -> None:
        ...
    def UpdateStructure(self, part: Tag) -> None:
        ...


class UFFbmGeom(Utilities.NXRemotableObject):
    def AskAccessibilityVectors(self, fbm_geom_tag: Tag, representative_feature: int, count: int, smart_vectors: typing.List[Tag]) -> None:
        ...
    def AskAvailableCriteria(self, fbm_geom_tag: Tag, count: int, criteria_list: str) -> None:
        ...
    def AskDoubleOfCriteria(self, fbm_geom_tag: Tag, ncfeat_object: int, criterion: str, value: float) -> None:
        ...
    def AskDoubleValueOfClassifiedCrit(self, fbm_geom_tag: Tag, criterion: str, classified_set_list: int, classified_set_index: int, value: float) -> None:
        ...
    def AskFeatureEntities(self, fbm_geom_tag: Tag, representative_feature: int, count: int, entities: typing.List[Tag]) -> None:
        ...
    def AskFeatureName(self, fbm_geom_tag: Tag, feature_name: str) -> None:
        ...
    def AskFeatures(self, fbm_geom_tag: Tag, count: int, ncfeat_objs: int) -> None:
        ...
    def AskIntValueOfClassifiedCrit(self, fbm_geom_tag: Tag, criterion: str, classified_set_list: int, classified_set_index: int, value: int) -> None:
        ...
    def AskIntegerOfCriteria(self, fbm_geom_tag: Tag, ncfeat_obj: int, criterion: str, value: int) -> None:
        ...
    def AskListOfFeatureNames(self, fbm_geom_tag: Tag, count: int, feature_names: str) -> None:
        ...
    def AskLogicalOfCriteria(self, fbm_geom_tag: Tag, ncfeat_obj: int, criterion: str, value: bool) -> None:
        ...
    def AskLogicalValueOfClassifiedCrit(self, fbm_geom_tag: Tag, criterion: str, classified_set_list: int, classified_set_index: int, value: bool) -> None:
        ...
    def AskRepresentativeFeatures(self, fbm_geom_tag: Tag, count: int, rep_feature_list: int) -> None:
        ...
    def AskStringOfCriteria(self, fbm_geom_tag: Tag, ncfeat_obj: int, criterion: str, value: str) -> None:
        ...
    def AskStringValueOfClassifiedCrit(self, fbm_geom_tag: Tag, criterion: str, classified_set_list: int, classified_set_index: int, value: str) -> None:
        ...
    def AskTypeOfCriterion(self, fbm_geom_tag: Tag, criterion: str, type: UF.UFFbmGeom.CritValueType) -> None:
        ...
    def AskUsedCriteria(self, fbm_geom_tag: Tag, count: int, used_criteria_list: str) -> None:
        ...
    def ClassifyByCriteria(self, fbm_geom_tag: Tag, num_of_criteria: int, criteria: str, num_of_classified_sets: int, classified_set_list: int) -> None:
        ...
    def Create(self, type: str, subtype: str, parent_geom: Tag, new_object: Tag) -> None:
        ...
    def FreeClassifiedSetList(self, fbm_geom_tag: Tag, classified_set_list: int) -> None:
        ...
    def RemoveAccessibilityVectors(self, fbm_geom_tag: Tag, representative_feature: int) -> None:
        ...
    def RemoveFeature(self, fbm_geom_tag: Tag, feature: int) -> None:
        ...
    def SetAccessibilityVectors(self, fbm_geom_tag: Tag, representative_feature: int, count: int, smart_vectors: typing.List[Tag]) -> None:
        ...
    def SetClassifiedFeatures(self, fbm_geom_tag: Tag, classified_set_list: int, classified_set_index: int) -> None:
        ...
    def SetFeatureName(self, fbm_geom_tag: Tag, feature_name: str) -> None:
        ...


    class CritValueType(enum.Enum):
        CritValueTypeUndefined = 0
        CritValueTypeLogical = 1
        CritValueTypeInteger = 2
        CritValueTypeDouble = 3
        CritValueTypeString = 4
    

class UFFam(Utilities.NXRemotableObject):
    def AddMember(self, family: Tag, member_data: UF.UFFam.MemberData, member_index: int) -> None:
        ...
    def AskAttributeData(self, attribute: Tag, attribute_data: UF.UFFam.AttributeData) -> None:
        ...
    def AskClassCount(self, class_count: int) -> None:
        ...
    def AskClassData(self, subtype: int, class_data: UF.UFFam.ClassData) -> None:
        ...
    def AskClassName(self, subtype: int, name: str) -> None:
        ...
    def AskFamilyData(self, family: Tag, family_data: UF.UFFam.FamilyData) -> None:
        ...
    def AskInstanceData(self, instance: Tag, family: Tag, member_index: int) -> None:
        ...
    def AskMemberColumnData(self, family: Tag, attribute_index: int, member_data: UF.UFFam.MemberData) -> None:
        ...
    def AskMemberRowData(self, family: Tag, member_index: int, member_data: UF.UFFam.MemberData) -> None:
        ...
    def CheckAttributeStatus(self, attribute: Tag) -> None:
        ...
    def CheckFamilyStatus(self, family: Tag) -> None:
        ...
    def CheckMemberStatus(self, family: Tag, member_index: int) -> None:
        ...
    def CreateAttribute(self, attribute_data: UF.UFFam.AttributeData, attribute: Tag) -> None:
        ...
    def CreateFamily(self, family_data: UF.UFFam.FamilyData, family: Tag) -> None:
        ...
    def CreateInstance(self, family: Tag, member_index: int, instance: Tag) -> None:
        ...
    def DeleteInstance(self, instance: Tag) -> None:
        ...
    def DeleteMember(self, family: Tag, member_index: int) -> None:
        ...
    def EditAttribute(self, attribute: Tag, attribute_data: UF.UFFam.AttributeData) -> None:
        ...
    def EditFamily(self, family: Tag, family_data: UF.UFFam.FamilyData) -> None:
        ...
    def EditMember(self, family: Tag, member_index: int, member_data: UF.UFFam.MemberData) -> None:
        ...
    def EvaluateIntentData(self, intent_data: UF.UFFam.IntentData, match_count: int, match_indices: int) -> None:
        ...
    def FreeClassData(self, class_data: UF.UFFam.ClassData) -> None:
        ...


    class UFFamMemberData():
        value_count: int
        values: str
    

    class UFFamIntentData():
        family: Tag
        member_index: int
        attribute_count: int
        attributes: typing.List[Tag]
        match_criteria: str
        name: str
    

    class UFFamFamilyData():
        subtype: int
        attribute_count: int
        member_count: int
        attributes: typing.List[Tag]
        name: str
    

    class UFFamClassData():
        subtype: int
        attribute_count: int
        attribute_data: typing.List[UF.UFFam.AttributeData]
        name: str
    

    class UFFamAttributeData():
        subtype: int
        base_object: Tag
        rules: str
        value: str
        name: str
    

class UFFacet(Utilities.NXRemotableObject):
    def AddFacetToModel(self, model: Tag, num_vertices: int, vertices: float, normals: float, adjacent_facet_ids: int, new_facet_id: int) -> None:
        ...
    def AskAdjacentFacet(self, model: Tag, facet_id: int, edge_id: int, adjacent_facet_id: int, edge_id_in_adjacent_facet: int) -> None:
        ...
    def AskAvailableSolid(self, model: Tag, solid: Tag) -> None:
        ...
    def AskDefaultParameters(self, parameters: UF.UFFacet.Parameters) -> None:
        ...
    def AskEdgeConvexity(self, model: Tag, facet_id: int, edge_in_facet: int, convexity: int) -> None:
        ...
    def AskFaceIdOfFacet(self, model: Tag, facet_id: int, face_id: int) -> None:
        ...
    def AskFaceIdOfSolidFace(self, model: Tag, face_tag: Tag, face_id: int) -> None:
        ...
    def AskMaxFacetVerts(self, model: Tag, num_facets: int) -> None:
        ...
    def AskModelParameters(self, model: Tag, parameters: UF.UFFacet.Parameters) -> None:
        ...
    def AskModelsOfSolid(self, solid: Tag, n_faceted_models: int, faceted_models: typing.List[Tag]) -> None:
        ...
    def AskNFacetsInModel(self, model: Tag, num_facets: int) -> None:
        ...
    def AskNormalsOfFacet(self, model: Tag, facet_id: int, num_vertices: int, normals: float) -> None:
        ...
    def AskNumFaces(self, model: Tag, num_faces: int) -> None:
        ...
    def AskNumFacetsInFace(self, model: Tag, face_id: int, num_facets: int) -> None:
        ...
    def AskNumVertsInFacet(self, model: Tag, facet_id: int, num_vertices: int) -> None:
        ...
    def AskParamsOfFacet(self, model: Tag, facet_id: int, num_params: int, _params: float) -> None:
        ...
    def AskPlaneEquation(self, model: Tag, facet_id: int, plane_normal: float, d_coefficient: float) -> None:
        ...
    def AskSolidFaceOfFaceId(self, model: Tag, face_id: int, face_tag: Tag) -> None:
        ...
    def AskSolidFaceOfFacet(self, model: Tag, facet_id: int, face_tag: Tag) -> None:
        ...
    def AskSolidOfModel(self, model: Tag, solid: Tag) -> None:
        ...
    def AskSurfaceDataForFace(self, facet_face: Tag, type: int, pos: float, dir: float, radius: float, radius_data: float, sense: bool, from_cached_analytics: bool) -> None:
        ...
    def AskVertexConvexity(self, model: Tag, facet_id: int, vertex_in_facet: int, convexity: int) -> None:
        ...
    def AskVerticesOfFacet(self, model: Tag, facet_id: int, num_vertices: int, vertices: float) -> None:
        ...
    def CreateModel(self, object_in_part: Tag, model: Tag) -> None:
        ...
    def CycleFacets(self, model: Tag, facet_id: int) -> None:
        ...
    def CycleFacetsInFace(self, model: Tag, face_id: int, facet_id: int) -> None:
        ...
    def DelFacetFromModel(self, model: Tag, facet_id: int) -> None:
        ...
    def DeleteAllFacetsFromModel(self, model: Tag) -> None:
        ...
    def DisassocFromSolid(self, model: Tag) -> None:
        ...
    def FacetSolid(self, solid_entity: Tag, parameters: UF.UFFacet.Parameters, facet_model: Tag) -> None:
        ...
    def FindEdgeInFacet(self, model: Tag, facet_id: int, vertex_1: float, vertex_2: float, sense: int, edge_id: int) -> None:
        ...
    def IsFacetConvex(self, model: Tag, facet_id: int, is_convex: bool) -> None:
        ...
    def IsModelConvex(self, model: Tag, is_convex: bool) -> None:
        ...
    def IsModelUpToDate(self, model: Tag, up_to_date: bool) -> None:
        ...
    def ModelEditsDone(self, model: Tag) -> None:
        ...
    def RebuildAdjacencies(self, model: Tag) -> None:
        ...
    def SetAdjacentFacet(self, model: Tag, facet_id: int, edge: int, adjacent_facet_id: int) -> None:
        ...
    def SetDefaultParameters(self, parameters: UF.UFFacet.Parameters) -> None:
        ...
    def SetVertexOfFacet(self, model: Tag, facet_id: int, vertex_in_facet: int, location: float) -> None:
        ...
    def UpdateModel(self, model: Tag, parameters: UF.UFFacet.Parameters) -> None:
        ...


    class UFFacetParameters():
        version: int
        max_facet_edges: int
        specify_surface_tolerance: bool
        surface_dist_tolerance: float
        surface_angular_tolerance: float
        specify_curve_tolerance: bool
        curve_dist_tolerance: float
        curve_angular_tolerance: float
        curve_max_length: float
        specify_convex_facets: bool
        specify_max_facet_size: bool
        max_facet_size: float
        number_storage_type: int
        specify_parameters: bool
        specify_view_direction: bool
        silh_view_direction: float
        silh_chord_tolerance: float
        store_face_tags: bool
    

class UFEvalsf(Utilities.NXRemotableObject):
    def AskFaceUvMinmax(self, evaluator: int, uv_min_max: float) -> None:
        ...
    def AskMinimumFaceDist(self, evaluator: int, point: float, srf_pos3: UF.UFEvalsf.Pos3) -> None:
        ...
    def Evaluate(self, evaluator: int, deriv_flag: int, uv_pair: float, surf_eval: UF.ModlSrfValue) -> None:
        ...
    def EvaluateArray(self, evaluator: int, deriv_flag: int, num_points: int, uv_pairs: float, surf_evals: typing.List[UF.ModlSrfValue]) -> None:
        ...
    def FindClosestPoint(self, evaluator: int, point: float, srf_pos3: UF.UFEvalsf.Pos3) -> None:
        ...
    def FindClosestPoint2(self, evaluator: int, point: float, srf_pos3: UF.UFEvalsf.Pos3) -> None:
        ...
    def Free(self, evaluator: int) -> None:
        ...
    def Initialize(self, face_tag: Tag, evaluator: int) -> None:
        ...
    def Initialize2(self, face_tag: Tag, evaluator: int) -> None:
        ...


    class UFEvalsfPos3():
        distance: float
        uv: float
        pnt3: float
    

class UFEval(Utilities.NXRemotableObject):
    def AskArc(self, evaluator: int, arc: UF.UFEval.Arc) -> None:
        ...
    def AskEllipse(self, evaluator: int, ellipse: UF.UFEval.Ellipse) -> None:
        ...
    def AskHyperbola(self, evaluator: int, hyperbola: UF.UFEval.Hyperbola) -> None:
        ...
    def AskLimits(self, evaluator: int, limits: float) -> None:
        ...
    def AskLine(self, evaluator: int, line: UF.UFEval.Line) -> None:
        ...
    def AskParabola(self, evaluator: int, parabola: UF.UFEval.Parabola) -> None:
        ...
    def AskSpline(self, evaluator: int, spline: UF.UFEval.Spline) -> None:
        ...
    def AskSplineControlPts(self, evaluator: int, n_points: int, points: float) -> None:
        ...
    def AskSplineKnots(self, evaluator: int, n_knots: int, knots: float) -> None:
        ...
    def Copy(self, evaluator: int, evaluator_copy: int) -> None:
        ...
    def Evaluate(self, evaluator: int, n_derivatives: int, parm: float, point: float, derivatives: float) -> None:
        ...
    def EvaluateClosestPoint(self, evaluator: int, reference_point: float, parm: float, closest_point: float) -> None:
        ...
    def EvaluateUnitVectors(self, evaluator: int, parm: float, point: float, tangent: float, normal: float, binormal: float) -> None:
        ...
    def Free(self, evaluator: int) -> None:
        ...
    def Initialize(self, tag: Tag, evaluator: int) -> None:
        ...
    def Initialize2(self, tag: Tag, evaluator: int) -> None:
        ...
    def IsArc(self, evaluator: int, is_arc: bool) -> None:
        ...
    def IsEllipse(self, evaluator: int, is_ellipse: bool) -> None:
        ...
    def IsEqual(self, evaluator1: int, evaluator2: int, is_equal: bool) -> None:
        ...
    def IsHyperbola(self, evaluator: int, is_hyperbola: bool) -> None:
        ...
    def IsLine(self, evaluator: int, is_line: bool) -> None:
        ...
    def IsParabola(self, evaluator: int, is_parabola: bool) -> None:
        ...
    def IsPeriodic(self, evaluator: int, is_periodic: bool) -> None:
        ...
    def IsSpline(self, evaluator: int, is_spline: bool) -> None:
        ...


    class UFEvalSpline():
        is_periodic: bool
        is_rational: bool
        order: int
        num_knots: int
        num_control: int
    

    class UFEvalParabola():
        limits: float
        k1: float
        center: float
        x_axis: float
        y_axis: float
    

    class UFEvalLine():
        length: float
        start: float
        end: float
        unit: float
    

    class UFEvalHyperbola():
        limits: float
        k1: float
        k2: float
        center: float
        x_axis: float
        y_axis: float
    

    class UFEvalEllipse():
        is_periodic: bool
        limits: float
        minor: float
        major: float
        center: float
        x_axis: float
        y_axis: float
    

    class UFEvalArc():
        is_periodic: bool
        limits: float
        radius: float
        center: float
        x_axis: float
        y_axis: float
    

    class ZigZagDir(enum.Enum):
        ZigZagDirZig = 0
        ZigZagDirZag = 1
    

class UFDrpos(Utilities.NXRemotableObject):
    def AskCustomFeed(self, drpos: int, feed_use: UF.UFDrpos.FeedUse, feed_unit: UF.UFDrpos.FeedUnit, feed_value: float) -> None:
        ...
    def AskDriveDirection(self, drpos: int, dir: float) -> None:
        ...
    def AskGridParams(self, drpos: int, uv: float) -> None:
        ...
    def AskPosition(self, drpos: int, pos: float) -> None:
        ...
    def AskProjVec(self, drpos: int, proj_vec: float) -> None:
        ...
    def AskSurfaceIdentifier(self, drpos: int, eid: Tag) -> None:
        ...
    def AskSurfaceParams(self, drpos: int, uv: float) -> None:
        ...
    def AskToolAxis(self, drpos: int, tool_axis: float) -> None:
        ...
    def AskType(self, drpos: int, type: UF.UFDrpos.Type) -> None:
        ...
    def AskUserData(self, drpos: int, user_data: int) -> None:
        ...
    def AskZigZagDir(self, drpos: int, zig_zag_dir: UF.UFDrpos.ZigZagDir) -> None:
        ...
    def CreateCut(self, drpos: int, pos: float, dir: float) -> None:
        ...
    def CreateFinalLift(self, drpos: int) -> None:
        ...
    def CreateFirstCut(self, drpos: int, pos: float, dir: float) -> None:
        ...
    def CreateLocalLift(self, drpos: int) -> None:
        ...
    def CreateStepover(self, drpos: int, pos: float, dir: float) -> None:
        ...
    def Delete(self, drpos: int) -> None:
        ...
    def SetCustomFeed(self, drpos: int, feed_use: UF.UFDrpos.FeedUse, feed_unit: UF.UFDrpos.FeedUnit, feed_value: float) -> None:
        ...
    def SetDriveDirection(self, drpos: int, dir: float) -> None:
        ...
    def SetPosition(self, drpos: int, pos: float) -> None:
        ...
    def SetProjVec(self, drpos: int, proj_vec: float) -> None:
        ...
    def SetToolAxis(self, drpos: int, tool_axis: float) -> None:
        ...
    def SetUserData(self, drpos: int, user_data: int) -> None:
        ...
    def SetZigZagDir(self, drpos: int, zig_zag_dir: UF.UFDrpos.ZigZagDir) -> None:
        ...


    class Type(enum.Enum):
        TypeNone = 0
        TypeCut = 1
        TypeFirstCut = 2
        TypeStepover = 10
        TypeLocalLift = 50
        TypeFinalLift = 51
    

    class FeedUse(enum.Enum):
        FeedUseDefault = 0
        FeedUseCustom = 1
    

    class FeedUnit(enum.Enum):
        FeedUnitNone = 0
        FeedUnitPerMin = 1
        FeedUnitPerRev = 2
    

class UFDrf(Utilities.NXRemotableObject):
    def AddAssortpartToAnn(self, annotation_tag: Tag, number_of_objects: int, list_of_objects: typing.List[Tag]) -> None:
        ...
    def AddCompoundWeldSymbol(self, weld_symbol: Tag, top_info: UF.UFDrf.WeldSymInfo, bottom_info: UF.UFDrf.WeldSymInfo) -> None:
        ...
    def AddControllingExp(self, _object: Tag, exp_id: Tag) -> None:
        ...
    def AddSymbolToObject(self, symbol_data: UF.UFDrf.SymbolCreateData, object_tag: Tag) -> None:
        ...
    def AddToDimension(self, entity_id: int, segment_num: int, ann_data: int, text_type: int, text_position: int, relative_just: int, line_space: int, number_lines: int, text_array: str) -> None:
        ...
    def AreDraftObjectsConst(self, objs: int, check_view_data: bool) -> None:
        ...
    def AskAngObjSuppressZeros(self, _object: Tag, option: UF.UFDrf.AngularSuppressZeros) -> None:
        ...
    def AskAngObjUnitsFormat(self, _object: Tag, nominal_format: UF.UFDrf.AngularUnits, tolerance_format: UF.UFDrf.AngularUnits) -> None:
        ...
    def AskAnnArcSegAngles(self, arc_segment: int, ann_data: int, arc_angles: float) -> None:
        ...
    def AskAnnData(self, annotation_tag: Tag, search_mask: int, cycle_flag: int, ann_data: int, ann_data_type: int, ann_data_form: int, num_segments: int, ann_origin: float, radius_angle: float) -> None:
        ...
    def AskAnnLineSegEnds(self, line_segment: int, ann_data: int, line_endpoints: float) -> None:
        ...
    def AskAnnotationTemplate(self, annotation_template_name: str) -> None:
        ...
    def AskAnnotationTextBox(self, annotation: Tag, upper_left: float, length: float, height: float) -> None:
        ...
    def AskAppendedText(self, dimension: Tag, num_text: int, appended_text: typing.List[UF.UFDrf.AppendedText]) -> None:
        ...
    def AskAreafillData(self, areafill_id: Tag, areafill_data: UF.UFDrf.Areafill) -> None:
        ...
    def AskArrowData(self, data_block: int, arrow_type: int, filled: int, origin: float, arrow_angle: float, include_angle: float, arrow_height: float, arrow_length: float) -> None:
        ...
    def AskAssocExp(self, object_tag: Tag, exp_tag: Tag) -> None:
        ...
    def AskAssociativeOrigin(self, drafting_entity: Tag, origin_data: typing.List[UF.UFDrf.AssociativeOrigin], origin: float) -> None:
        ...
    def AskAssociativityData(self, _object: Tag, num_associativities: int, associativity_data: typing.List[UF.UFDrf.ObjectAssocData]) -> None:
        ...
    def AskBoundaries(self, draft_aid_tag: Tag, num_boundaries: int, boundary_tags: typing.List[Tag]) -> None:
        ...
    def AskCalloutOfAnnotation(self, annotation: Tag, callout: Tag) -> None:
        ...
    def AskCalloutRowMembers(self, callout: Tag, row: int, num_members: int, members: typing.List[Tag]) -> None:
        ...
    def AskCenterlineInfo(self, centerline_tag: Tag, centerline_type: UF.UFDrf.ValidClineForm, centerline_origin: float, centerline_info: typing.List[UF.UFDrf.CenterlineInfo]) -> None:
        ...
    def AskChamferDimensionData(self, cham_dim_tag: Tag, cham_dim_data: UF.UFDrf.ChamferDimensionData) -> None:
        ...
    def AskControllingExp(self, _object: Tag, exp_id: Tag) -> None:
        ...
    def AskControllingMemberOfCallout(self, callout: Tag, controlling_member: Tag) -> None:
        ...
    def AskCustomSymbolAngle(self, symbol_tag: Tag, angle: float) -> None:
        ...
    def AskCustomSymbolAttachLocations(self, symbol: Tag, locations: typing.List[Tag]) -> None:
        ...
    def AskCustomSymbolLeader(self, symbol: Tag, leader_data: typing.List[UF.UFDrf.LeaderData]) -> None:
        ...
    def AskCustomSymbolName(self, custom_symbol: Tag, symbol_name: str) -> None:
        ...
    def AskCustomSymbolScale(self, symbol_tag: Tag, scale: float) -> None:
        ...
    def AskDiameterRadiusPreferences(self, diameter_radius_preferences: UF.UFDrf.DiameterRadiusPreferences) -> None:
        ...
    def AskDimAppendedTextSpaceFactor(self, dimension: Tag, space_factor: float) -> None:
        ...
    def AskDimDimLineSpaceFactor(self, dimension: Tag, space_factor: float) -> None:
        ...
    def AskDimInspectionType(self, dim_tag: Tag, inspection_type: UF.UFDrf.InspectionType) -> None:
        ...
    def AskDimReferenceType(self, dim_tag: Tag, ref_type: UF.UFDrf.ReferenceSymbolType) -> None:
        ...
    def AskDimToleranceTextSpaceFactor(self, dimension: Tag, space_factor: float) -> None:
        ...
    def AskDimensionPreferences1(self, dimension_preferences: typing.List[UF.UFDrf.DimensionPreferences1]) -> None:
        ...
    def AskDimensionSetOffset(self, dimension: Tag, offset: float) -> None:
        ...
    def AskDimensionText(self, dimension: Tag, num_main_text: int, main_text: str, num_dual_text: int, dual_text: str) -> None:
        ...
    def AskDimensionsOfSet(self, dimension_set: Tag, sub_dimensions: typing.List[Tag], num: int) -> None:
        ...
    def AskDispParms(self, ir1: int, rr2: float) -> None:
        ...
    def AskDoglegInfo(self, orddim_tag: Tag, dogleg_info: UF.UFDrf.DoglegInfo) -> None:
        ...
    def AskDraftAidTextInfo(self, draft_aid_tag: Tag, num_text: int, text_info: typing.List[UF.UFDrf.DraftAidTextInfo]) -> None:
        ...
    def AskEmbeddedUdsFontInfo(self, symbol_font_tag: Tag, symbol_name: str, num_of_strokes: int, stroke_info: typing.List[UF.UFDrf.StrokeInfo]) -> None:
        ...
    def AskFoldedRadiusInfo(self, frdim_tag: Tag, frdim_info: UF.UFDrf.FoldedRadiusInfo) -> None:
        ...
    def AskGdtSymbolInfo(self, gdt_symbol_tag: Tag, gdt_symbol_origin: float, gdt_symbol_info: typing.List[UF.UFDrf.GdtSymbolInfo]) -> None:
        ...
    def AskHatchFillPreferences(self, hatch_fill_preferences: UF.UFDrf.HatchFillPreferences) -> None:
        ...
    def AskIdSymbolGeometry(self, id_symbol: Tag, num_lines: int, lines: float, num_arcs: int, arcs: typing.List[UF.UFDrf.ArcInfo]) -> None:
        ...
    def AskIdSymbolInfo(self, id_symbol_tag: Tag, id_symbol_type: UF.UFDrf.IdSymbolType, id_symbol_origin: float, id_symbol_info: typing.List[UF.UFDrf.IdSymbolInfo]) -> None:
        ...
    def AskIdSymbolType(self, id_symbol_tag: Tag, id_symbol_type: UF.UFDrf.IdSymbolType) -> None:
        ...
    def AskImageData(self, image: Tag, data: UF.UFDrf.ImageData) -> None:
        ...
    def AskLabelInfo(self, label_tag: Tag, label_origin: float, label_info: typing.List[UF.UFDrf.LabelInfo]) -> None:
        ...
    def AskLetteringPreferences(self, lettering_preferences: UF.UFDrf.LetteringPreferences) -> None:
        ...
    def AskLineArrowPreferences(self, line_arrow_preferences: UF.UFDrf.LineArrowPreferences) -> None:
        ...
    def AskNarrowDimensionData(self, dimension_tag: Tag, narrow_data: UF.UFDrf.NarrowDimensionInfo) -> None:
        ...
    def AskNumberBlocks(self, annotation_tag: Tag, num_block: int) -> None:
        ...
    def AskNumberRowsInCallout(self, callout: Tag, num_rows: int) -> None:
        ...
    def AskObjSuppressPreZeros(self, _object: Tag, option: bool) -> None:
        ...
    def AskObjTextAboveLdr(self, _object: Tag, option: UF.UFDrf.TextAboveLeader) -> None:
        ...
    def AskObjectPreferences(self, drf_object_tag: Tag, mpi: int, mpr: float, radius_val: str, diameter_val: str) -> None:
        ...
    def AskObjectsControlledByExp(self, exp_id: Tag, num_objs: int, objects: typing.List[Tag]) -> None:
        ...
    def AskOrdoriginInfo(self, ordorigin_tag: Tag, origin_disp: UF.UFDrf.OrddispInfo, num_assoc: int, assoc_objects: typing.List[UF.UFDrf.AssocInfo]) -> None:
        ...
    def AskOrigin(self, annotation: Tag, origin: float) -> None:
        ...
    def AskParentOfInheritedPmi(self, inherited_pmi: Tag, parent: Tag) -> None:
        ...
    def AskPlotDrawingImages(self, plot_images: bool) -> None:
        ...
    def AskPreferences(self, mpi: int, mpr: float, radius_value: str, diameter_value: str) -> None:
        ...
    def AskRetainColorFontWidth(self, color: int, font: int, width: int) -> None:
        ...
    def AskRetainedState(self, state: UF.UFDrf.RetainedState) -> None:
        ...
    def AskSbfFile(self, sbf_name: str) -> None:
        ...
    def AskSetOfDimension(self, dimension: Tag, dimension_set: Tag) -> None:
        ...
    def AskSuppressPreZeros(self, option: bool) -> None:
        ...
    def AskSuppressViewUpdate(self, suppress_view_update: bool) -> None:
        ...
    def AskSymbolData(self, symbol_tag: Tag, symbol_data: UF.UFDrf.SymbolData) -> None:
        ...
    def AskSymbolDataFromName(self, sbf_name: str, symbol_names: str, num_symbols: int, symbol_info: typing.List[UF.UFDrf.UdSymbolFontInfo]) -> None:
        ...
    def AskSymbolMirrorAndFlip(self, symbol_tag: Tag, mirrored: bool, flip: bool) -> None:
        ...
    def AskSymbolPreferences(self, symbol_preferences: UF.UFDrf.SymbolPreferences) -> None:
        ...
    def AskSymbolsUsed(self, object_tag: Tag, num_symbol_fonts: int, symbol_font_tags: typing.List[Tag]) -> None:
        ...
    def AskTextAboveLeader(self, option: UF.UFDrf.TextAboveLeader) -> None:
        ...
    def AskTextData(self, ip1: int, ann_data: int, cr3: str, ir4: int, ir5: int) -> None:
        ...
    def AskUdSymbolFontInfo(self, ud_symbol_tag: Tag, num_symbols: int, font_info: typing.List[UF.UFDrf.UdSymbolFontInfo]) -> None:
        ...
    def AskUdsObjectSize(self, _object: Tag, uds_size: UF.UFDrf.UdsSize) -> None:
        ...
    def AskUnitsFormatPreferences(self, units_format_preferences: UF.UFDrf.UnitsFormatPreferences) -> None:
        ...
    def AskVerticalNote(self, note: Tag, is_vertical: bool) -> None:
        ...
    def AskWeldSymbol(self, weld_symbol_tag: Tag, label_origin: float, label_info: typing.List[UF.UFDrf.LabelInfo], symbol_data: UF.UFDrf.WeldSymbols) -> None:
        ...
    def CountTextSubstring(self, segment_number: int, ann_data: int, number_of_substring: int) -> None:
        ...
    def CreTextBlock(self, entity_id: int, text_type: int, text_origin: float, number_lines: int, text_array: str) -> None:
        ...
    def Create3ptClineFbolt(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], centerline_tag: Tag) -> None:
        ...
    def Create3ptClineFcir(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], centerline_tag: Tag) -> None:
        ...
    def Create3ptClinePbolt(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], centerline_tag: Tag) -> None:
        ...
    def Create3ptClinePcir(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], centerline_tag: Tag) -> None:
        ...
    def CreateAngularDim(self, dimension_form: int, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateArclengthDim(self, _object: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateAreafill(self, num_bounds: int, num_obj_bnd: int, object_list: typing.List[Tag], view_tag: Tag, areafill_tag: Tag) -> None:
        ...
    def CreateAssortpartAid(self, arc: UF.UFDrf.AssortpartArc, arrow: UF.UFDrf.AssortpartArrow, line: UF.UFDrf.AssortpartLine, text: UF.UFDrf.AssortpartText, assorted_parts_tag: Tag) -> None:
        ...
    def CreateAssortpartDim(self, arc: UF.UFDrf.AssortpartArc, arrow: UF.UFDrf.AssortpartArrow, line: UF.UFDrf.AssortpartLine, text: UF.UFDrf.AssortpartText, assorted_parts_tag: Tag) -> None:
        ...
    def CreateBlockCline(self, defining_obj_list: UF.UFDrf.Object, limiting_obj_list: UF.UFDrf.Object, centerline_tag: Tag) -> None:
        ...
    def CreateChamferDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, dim_text: UF.UFDrf.Text, dim_3d_origin: float, dim_tag: Tag) -> None:
        ...
    def CreateConcirDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateCptClineFbolt(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], center_point: UF.UFDrf.Object, centerline_tag: Tag) -> None:
        ...
    def CreateCptClineFcir(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], center_point: UF.UFDrf.Object, centerline_tag: Tag) -> None:
        ...
    def CreateCptClinePbolt(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], center_point: UF.UFDrf.Object, centerline_tag: Tag) -> None:
        ...
    def CreateCptClinePcir(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], center_point: UF.UFDrf.Object, centerline_tag: Tag) -> None:
        ...
    def CreateCrosshatch(self, num_bounds: int, num_obj_bnd: int, object_list: typing.List[Tag], view_tag: Tag, crosshatch_tag: Tag) -> None:
        ...
    def CreateCustomSymbolInstance(self, symbol_definition: UF.UFDrf.CustomSymbol, new_symbol_tag: Tag) -> None:
        ...
    def CreateCylindricalDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateDiameterDim(self, _object: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateFoldedradiusDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, fold_location: float, fold_angle: float, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateGdtSymbol(self, num_lines_text: int, text_string: str, origin_3d: float, leader_type: UF.UFDrf.LeaderType, leader_attach_type: UF.UFDrf.LeaderAttachType, _object: UF.UFDrf.Object, model_pos_3d: float, frame_corner: UF.UFDrf.FrameCorner, gdt_symbol_tag: Tag) -> None:
        ...
    def CreateGdtSymbolWithMultipleLeaders(self, num_lines_text: int, text_string: str, gdt_symbol_origin: float, leader: UF.UFDrf.GdtLeader, frame_corner: UF.UFDrf.FrameCorner, gdt_symbol_tag: Tag) -> None:
        ...
    def CreateHoleDim(self, _object: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateHorizontalBaselineDimension(self, object_set: typing.List[UF.UFDrf.Object], num_of_objects: int, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateHorizontalChainDimension(self, object_set: UF.UFDrf.Object, num_of_objects: int, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateHorizontalDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateIdSymbol(self, id_symbol_type: UF.UFDrf.IdSymbolType, upper_text_string: str, lower_text_string: str, origin_3d: float, leader_mode: UF.UFDrf.LeaderMode, leader_attach_type: UF.UFDrf.LeaderAttachType, _object: UF.UFDrf.Object, model_pos_3d: float, id_symbol_tag: Tag) -> None:
        ...
    def CreateImage(self, image_name: str, drawing_sheet: Tag, origin: float, image: Tag) -> None:
        ...
    def CreateImageFromFile(self, file_name: str, drawing_sheet: Tag, origin: float, image: Tag) -> None:
        ...
    def CreateLabel(self, num_lines_text: int, text_string: str, origin_3d: float, leader_attach_type: UF.UFDrf.LeaderAttachType, _object: UF.UFDrf.Object, model_pos_3d: float, label_tag: Tag) -> None:
        ...
    def CreateLinearCline(self, num_cline_objs: int, cline_obj_list: typing.List[UF.UFDrf.Object], centerline_tag: Tag) -> None:
        ...
    def CreateNonAssocHatch(self, num_lines: int, hatch_lines: float, matrix: Tag, view: Tag, color: int, line_width: int, new_hatch: Tag) -> None:
        ...
    def CreateNote(self, num_lines_text: int, text_string: str, origin_3d: float, orientation: int, note_tag: Tag) -> None:
        ...
    def CreateOffctrptCx(self, cline_object: UF.UFDrf.Object, distance: float, offctrpt_tag: Tag) -> None:
        ...
    def CreateOffctrptCy(self, cline_object: UF.UFDrf.Object, distance: float, offctrpt_tag: Tag) -> None:
        ...
    def CreateOffctrptFx(self, cline_object: UF.UFDrf.Object, center_point: UF.UFDrf.Object, offctrpt_tag: Tag) -> None:
        ...
    def CreateOffctrptFy(self, cline_object: UF.UFDrf.Object, center_point: UF.UFDrf.Object, offctrpt_tag: Tag) -> None:
        ...
    def CreateOffctrptNx(self, cline_object: UF.UFDrf.Object, distance: float, offctrpt_tag: Tag) -> None:
        ...
    def CreateOffctrptNy(self, cline_object: UF.UFDrf.Object, distance: float, offctrpt_tag: Tag) -> None:
        ...
    def CreateOffcylClineObj(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, center_point: UF.UFDrf.Object, centerline_tag: Tag) -> None:
        ...
    def CreateOffcylClineOff(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, distance: float, centerline_tag: Tag) -> None:
        ...
    def CreateOrddimension(self, margin_origin_tag: Tag, dimension_type: int, _object: UF.UFDrf.Object, dogleg_angle: float, dogleg_distance: float, drf_text: UF.UFDrf.Text, text_origin_flag: int, origin_3d: float, dimension_tag: Tag) -> None:
        ...
    def CreateOrdinateDim(self, np1: Tag, ip2: int, np3: Tag, ip4: int, ip5: int, rp6: float, rp7: float, cp8: str, ip9: int, cp10: str, ip11: int, rp12: float, nr13: Tag) -> None:
        ...
    def CreateOrdinateMargin(self, ip1: int, np2: Tag, np3: Tag, rp4: float, rp5: float, rp6: float, nr7: Tag) -> None:
        ...
    def CreateOrdinateOrigin(self, np1: Tag, ip2: int, ip3: int, ip4: int, ip5: int, ip6: int, cp7: str, nr8: Tag) -> None:
        ...
    def CreateOrdmargin(self, margin_type: int, ordinate_origin_tag: Tag, _object: UF.UFDrf.Object, margin_xy_point: float, margin_xy_direction: float, offset_distance: float, margin_tag: Tag) -> None:
        ...
    def CreateOrdorigin(self, _object: UF.UFDrf.Object, positive_quad_id: int, arr_dim_line_display: int, origin_symbol_display: int, user_object_name: str, origin_tag: Tag) -> None:
        ...
    def CreateParallelDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreatePerpendicularDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateRadiusDim(self, _object: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateSbfFile(self, sbf_name: str) -> None:
        ...
    def CreateSideSeam(self, weld_symbol_tag: Tag, view_tag: Tag, _object: Tag, point: float, weld_symbol_data: UF.UFDrf.WeldSymbols) -> None:
        ...
    def CreateSymCline(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, centerline_tag: Tag) -> None:
        ...
    def CreateSymbolFont(self, symbol_name: str, symbol_factor: float, symbol_anchor: float, symbol_orient: float, num_objects: int, _object: typing.List[Tag]) -> None:
        ...
    def CreateTopSeam(self, weld_symbol_tag: Tag, view_tag: Tag, num_objects: int, objects: typing.List[Tag], flip: bool, weld_symbol_data: UF.UFDrf.WeldSymbols) -> None:
        ...
    def CreateVerticalBaselineDimension(self, object_set: typing.List[UF.UFDrf.Object], num_of_objects: int, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateVerticalChainDimension(self, object_set: typing.List[UF.UFDrf.Object], num_of_objects: int, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateVerticalDim(self, object1: UF.UFDrf.Object, object2: UF.UFDrf.Object, drf_text: UF.UFDrf.Text, dimension_3d_origin: float, dimension_tag: Tag) -> None:
        ...
    def CreateWeldSymbol(self, origin_3d: float, leader_attach_type: UF.UFDrf.LeaderAttachType, _object: UF.UFDrf.Object, model_pos_3d: float, weld_symbol_data: UF.UFDrf.WeldSymbols, weld_symbol_tag: Tag) -> None:
        ...
    def CreateXhatch(self, op_type: int, nmbnds: int, numels: int, elems: typing.List[Tag], xhat_eid: Tag) -> None:
        ...
    def EditDimAssoc(self, dimension_tag: Tag, old_leader_position: float, new_leader_position: float, new_assoc_type: int, new_assoc_object: UF.UFDrf.Object) -> None:
        ...
    def EditWeldSymbol(self, weld_symbol_tag: Tag, weld_symbol_data: UF.UFDrf.WeldSymbols) -> None:
        ...
    def FlipImageAboutHeight(self, image: Tag) -> None:
        ...
    def FlipImageAboutWidth(self, image: Tag) -> None:
        ...
    def Frdim(self, np1: Tag, np2: Tag, ip3: int, ip4: int, rp5: float, rp6: float, cp7: str, ip8: int, cp9: str, rp10: float, nr11: Tag) -> None:
        ...
    def FreeCompData(self, objs: int) -> None:
        ...
    def GetCharFont(self, font_index: int, cfont: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def GetSymbolDivider(self, segment_number: int, ann_data: int, divider_instance: int, start_point: float, end_point: float) -> None:
        ...
    def GetTextBars(self, segment_number: int, ann_data: int, number_of_bars: int, bar_type: int, offset_to_bar: int, bar_position: float) -> None:
        ...
    def GetTextSubstring(self, segment_number: int, ann_data: int, substring_instance: int, text_type: int, number_of_substring: int, substring: str, substring_position: float, substring_characteristic: float) -> None:
        ...
    def GetXhatchParms(self, xhat_eid: Tag, mat_name: str, int_parms: int, real_parms: float, rtc: int) -> None:
        ...
    def HasAssociativeOrigin(self, drafting_entity: Tag, has_associative_origin: bool) -> None:
        ...
    def InheritFeatureData(self, feature_pre_v13_sketch_count: int, features_pre_v13_sketches: typing.List[Tag], part_occs: typing.List[Tag], view_count: int, views: typing.List[Tag], inherit_type: UF.UFDrf.InheritType) -> None:
        ...
    def InitAssociativityData(self, associativity_data: UF.UFDrf.ObjectAssocData) -> None:
        ...
    def InitAssortpartArc(self, assortpart_arc: UF.UFDrf.AssortpartArc) -> None:
        ...
    def InitAssortpartArrow(self, assortpart_arrow: UF.UFDrf.AssortpartArrow) -> None:
        ...
    def InitAssortpartLine(self, assortpart_line: UF.UFDrf.AssortpartLine) -> None:
        ...
    def InitAssortpartText(self, assortpart_text: UF.UFDrf.AssortpartText) -> None:
        ...
    def InitImageData(self, data: UF.UFDrf.ImageData) -> None:
        ...
    def InitLineObject(self, line_object: UF.UFDrf.LineObject) -> None:
        ...
    def InitObjectStructure(self, _object: UF.UFDrf.Object) -> None:
        ...
    def InitSymbolCreateData(self, symbol_data: UF.UFDrf.SymbolCreateData) -> None:
        ...
    def InitializeCustomSymbolData(self, symbol_definition: UF.UFDrf.CustomSymbol) -> None:
        ...
    def InitializeCustomSymbolTextData(self, symbol_text: UF.UFDrf.CustomSymbolText) -> None:
        ...
    def InitializeLeaderData(self, leader: UF.UFDrf.Leader) -> None:
        ...
    def IsAnnotationRetained(self, annotation: Tag, is_retained: bool) -> None:
        ...
    def IsBlockCenterline(self, object_tag: Tag, is_block_cline: bool) -> None:
        ...
    def IsChamferDimension(self, dim_tag: Tag, is_cham_dim: bool) -> None:
        ...
    def IsInheritedPmi(self, annotation: Tag, inherited: bool) -> None:
        ...
    def IsNarrowDimension(self, dimension_tag: Tag, is_narrow_dimension: bool) -> None:
        ...
    def IsObjectOutOfDate(self, _object: Tag, out_of_date: bool) -> None:
        ...
    def IsPmiDisplayInstance(self, _object: Tag, is_display_instance: bool) -> None:
        ...
    def IsSbfSymbol(self, symbol: Tag, is_sbf: bool) -> None:
        ...
    def MarginToCline(self, part_tag: Tag) -> None:
        ...
    def PlaceSymbol(self, symbol_data: UF.UFDrf.SymbolCreateData, is_inverted: bool, is_mirrored: bool, symbol_tag: Tag) -> None:
        ...
    def RecordDraftObjects(self, objs: int, record_view_data: bool) -> None:
        ...
    def RemoveControllingExp(self, _object: Tag) -> None:
        ...
    def RenderArrowhead(self, part: Tag, ann: Tag, arrow_info: UF.UFDrf.ArrowInfo, use_arrow_z: bool, render_table: UF.UFDrf.RenderTable, client: int) -> None:
        ...
    def RenderText(self, part: Tag, ann: Tag, num_lines: int, text: str, text_info: UF.UFDrf.DraftAidTextInfo, render_table: UF.UFDrf.RenderTable, client: int) -> None:
        ...
    def RotateImage(self, image: Tag, angle: float) -> None:
        ...
    def SetAnnotationTemplate(self, annotation_template_name: str) -> None:
        ...
    def SetAreafillAngle(self, areafill_id: Tag, angle: float) -> None:
        ...
    def SetAreafillMaterial(self, areafill_id: Tag, material: UF.UFDrf.ValidMaterial) -> None:
        ...
    def SetAreafillScale(self, areafill_id: Tag, scale: float) -> None:
        ...
    def SetAssociativeOrigin(self, drafting_entity: Tag, origin_data: UF.UFDrf.AssociativeOrigin, origin: float) -> None:
        ...
    def SetAssociativityData(self, _object: Tag, num_associativities: int, associativity_data: typing.List[UF.UFDrf.ObjectAssocData]) -> None:
        ...
    def SetChamferDimensionData(self, cham_dim_tag: Tag, cham_dim_data: UF.UFDrf.ChamferDimensionData) -> None:
        ...
    def SetCustomSymbolAngle(self, symbol_tag: Tag, angle: float) -> None:
        ...
    def SetCustomSymbolScale(self, symbol_tag: Tag, scale: float) -> None:
        ...
    def SetCustomerSbfFile(self) -> None:
        ...
    def SetCylDim(self, dim_obj: Tag, double_flag: int, status: int) -> None:
        ...
    def SetDiameterRadiusPreferences(self, diameter_radius_preferences: UF.UFDrf.DiameterRadiusPreferences) -> None:
        ...
    def SetDimAppendedTextSpaceFactor(self, dimension: Tag, space_factor: float) -> None:
        ...
    def SetDimDimLineSpaceFactor(self, dimension: Tag, space_factor: float) -> None:
        ...
    def SetDimInspectionType(self, dim_tag: Tag, inspection_type: UF.UFDrf.InspectionType) -> None:
        ...
    def SetDimReferenceType(self, dim_tag: Tag, ref_type: UF.UFDrf.ReferenceSymbolType) -> None:
        ...
    def SetDimToleranceTextSpaceFactor(self, dimension: Tag, space_factor: float) -> None:
        ...
    def SetDimensionPreferences(self, dimension_preferences: UF.UFDrf.DimensionPreferences) -> None:
        ...
    def SetDimensionPreferences1(self, dimension_preferences: UF.UFDrf.DimensionPreferences1) -> None:
        ...
    def SetDimensionSetOffset(self, dimension: Tag, offset: float) -> None:
        ...
    def SetDispParms(self, ip1: int, rp2: float) -> None:
        ...
    def SetDraftCommon(self, _object: Tag) -> None:
        ...
    def SetHatchFillPreferences(self, hatch_fill_preferences: UF.UFDrf.HatchFillPreferences) -> None:
        ...
    def SetImageAlignPosition(self, image: Tag, align_position: UF.UFDrf.AlignPosition) -> None:
        ...
    def SetImageAspectRatioLock(self, image: Tag, lock_aspect_ratio: bool) -> None:
        ...
    def SetImageHeight(self, image: Tag, height: float) -> None:
        ...
    def SetImageWidth(self, image: Tag, width: float) -> None:
        ...
    def SetLetteringPreferences(self, lettering_preferences: UF.UFDrf.LetteringPreferences) -> None:
        ...
    def SetLineArrowPreferences(self, line_arrow_preferences: UF.UFDrf.LineArrowPreferences) -> None:
        ...
    def SetNarrowDimensionData(self, dimension_tag: Tag, narrow_data: UF.UFDrf.NarrowDimensionInfo) -> None:
        ...
    def SetObjectPreferences(self, drf_object_tag: Tag, mpi: int, mpr: float, radius_val: str, diameter_val: str) -> None:
        ...
    def SetOrigin(self, annotation: Tag, new_origin: float) -> None:
        ...
    def SetPlotDrawingImages(self, plot_images: bool) -> None:
        ...
    def SetPreferences(self, mpi: int, mpr: float, radius_val: str, diameter_val: str) -> None:
        ...
    def SetRetainColorFontWidth(self, color: int, font: int, width: int) -> None:
        ...
    def SetRetainedState(self, state: UF.UFDrf.RetainedState) -> None:
        ...
    def SetSpecifiedSbfFile(self, sbf_name: str) -> None:
        ...
    def SetSuppressPreZeros(self, option: bool) -> None:
        ...
    def SetSuppressViewUpdate(self, suppress_view_update: bool) -> None:
        ...
    def SetSymbolPreferences(self, symbol_preferences: UF.UFDrf.SymbolPreferences) -> None:
        ...
    def SetTextAboveLeader(self, option: UF.UFDrf.TextAboveLeader) -> None:
        ...
    def SetTolerance(self, tolerance: int) -> None:
        ...
    def SetUdsSize(self, uds_size: UF.UFDrf.UdsSize) -> None:
        ...
    def SetUgdefaultSbfFile(self) -> None:
        ...
    def SetUnitsFormatPreferences(self, units_format_preferences: UF.UFDrf.UnitsFormatPreferences) -> None:
        ...
    def SetVerticalNote(self, note: Tag, is_vertical: bool) -> None:
        ...
    def SetWeldSymbolStandard(self, standard: str) -> None:
        ...
    def SetXhatchMat(self, file_name: str, material_name: str, util: int) -> None:
        ...
    def TransferToDrawing(self, annotation: Tag, member_view: Tag, drawing: Tag, in_drawing_plane: bool) -> None:
        ...
    def UpdateViews(self, drawing_name: str, method: int, view_name: str) -> None:
        ...


    class UFDrfWeldSymInfo():
        finish_type: UF.UFDrf.WeldFinishTypes
        contour_type: UF.UFDrf.WeldContourTypes
        weld_type: UF.UFDrf.WeldSymbolTypes
        size_code: UF.UFDrf.WeldSizeCode
        angle: str
        num_root_depth: str
        size: str
        pitch: str
    

    class WeldSymExtType(enum.Enum):
        WeldSymExtNone = 0
        WeldSymExtDogLeg = 1
        WeldSymExtBox = 2
    

    class WeldSymbolTypes(enum.Enum):
        WeldNoSymbol = 0
        WeldButtWithReSymbol = 1
        WeldSquareButtSymbol = 2
        WeldGrooveVSymbol = 3
        WeldVWithBrfSymbol = 4
        WeldBevelSymbol = 5
        WeldBevelWithBrfSymbol = 6
        WeldUSymbol = 7
        WeldJSymbol = 8
        WeldFlareVSymbol = 9
        WeldFlareBevelSymbol = 10
        WeldKGrooveSymbol = 11
        WeldFilletSymbol = 12
        WeldStakeSymbol = 13
        WeldPlugSlotSymbol = 14
        WeldEdgeSymbol = 15
        WeldEdge2Symbol = 16
        WeldSpotSymbol = 17
        WeldSpot2Symbol = 18
        WeldSeamSymbol = 19
        WeldSeam2Symbol = 20
        WeldStpFlankVSymbol = 21
        WeldStpFlankBevelSymbol = 22
        WeldBackingSymbol = 23
        WeldStudSymbol = 24
        WeldSurfacingSymbol = 25
        WeldSurfaceJointSymbol = 26
        WeldInclinedJointSymbol = 27
        WeldFoldJointSymbol = 28
    

    class UFDrfWeldSymbols():
        sym_info_top: UF.UFDrf.WeldSymInfo
        sym_info_bottom: UF.UFDrf.WeldSymInfo
        extension: UF.UFDrf.WeldSymExtType
        ident_line_type: UF.UFDrf.WeldIdentLineType
        peripheral_flag: int
        field_flag: int
        staggered_flag: int
        center_flag: int
        num_lines: int
        symbol_standard: str
        reference_text: str
        scale_factor: float
    

    class WeldSizeCode(enum.Enum):
        WeldNoCode = -1
        WeldCodeA = 0
        WeldCodeC = 1
        WeldCodeD = 2
        WeldCodeS = 3
        WeldCodeZ = 4
        WeldCodeP = 5
    

    class WeldIdentLineType(enum.Enum):
        WeldSymNoIdentLine = 1
        WeldSymIdentLineTop = 2
        WeldSymIdentLineBottom = 3
    

    class WeldFinishTypes(enum.Enum):
        WeldNoFinish = 0
        WeldChipFinish = 1
        WeldGrindFinish = 2
        WeldHammerFinish = 3
        WeldMachineFinish = 4
        WeldRollFinish = 5
        WeldPeenFinish = 6
    

    class WeldContourTypes(enum.Enum):
        WeldNone = 0
        WeldConvex = 1
        WeldFlush = 2
        WeldConcave = 3
        WeldBlendedToes = 4
        WeldBackingPerm = 5
        WeldBackingRemv = 6
        WeldMeltThrough = 7
    

    class VerticalTextJust(enum.Enum):
        TextTop = 1
        TextMiddle = 2
        TextBottom = 3
    

    class ValidMaterial(enum.Enum):
        Corkfeltfiber = 1
        Soundinsulation = 2
        Concrete = 3
        Earth = 4
        Rock = 5
        Sand = 6
        Liquids = 7
        Woodacrossgrain = 8
        Woodwithgrain = 9
    

    class ValidClineForm(enum.Enum):
        LinearCline = 1
        CptClineFcir = 2
        CptClinePcir = 3
        CptClineFbolt = 4
        CptClinePbolt = 5
        _3pt_cline_fcir = 6
        _3pt_cline_pcir = 7
        _3pt_cline_fbolt = 8
        _3pt_cline_pbolt = 9
        OffcylClineOff = 10
        OffcylClineObj = 11
        SymmetricalCline = 12
        OffctrptNx = 13
        OffctrptCx = 14
        OffctrptFx = 15
        OffctrptNy = 16
        OffctrptCy = 17
        OffctrptFy = 18
        BlockCline = 19
    

    class UFDrfUnitsFormatPreferences():
        dimension_linear_units: UF.UFDrf.LinearUnits
        linear_fraction_type: UF.UFDrf.FractionType
        decimal_point_character: UF.UFDrf.DecimalPointCharacter
        display_trailing_zeros: bool
        dimension_tolerance_placement: UF.UFDrf.TolerancePlacement
        dimension_angular_format: UF.UFDrf.AngularUnits
        dim_angular_format_tolerance: UF.UFDrf.AngularUnits
        angular_suppress_zeros: UF.UFDrf.AngularSuppressZeros
        dual_dimension_format: UF.UFDrf.DualDimensionFormat
        dual_dimension_units: UF.UFDrf.LinearUnits
        dual_fraction_type: UF.UFDrf.FractionType
        dual_convert_tolerance: bool
    

    class UdSymbolPenType(enum.Enum):
        UdSymbolMove = 0
        UdSymbolDraw = 1
    

    class UFDrfUdSymbolFontInfo():
        anchor_point: int
        orientation_point: int
        factor: float
        length: float
        height: float
        num_stroke: int
        stroke_info: typing.List[UF.UFDrf.StrokeInfo]
    

    class UdsSizeType(enum.Enum):
        LengthHeight = 0
        ScaleAspectRatio = 1
    

    class UFDrfUdsSize():
        uds_size_type: UF.UFDrf.UdsSizeType
        length_or_scale: float
        height_or_aspect_ratio: float
    

    class TrimDimLineStyle(enum.Enum):
        DontTrimDimLine = 0
        TrimDimLine = 1
    

    class ToleranceType(enum.Enum):
        NoTolerance = 1
        LimitOneLine = 2
        LimitTwoLines = 3
        BilateralOneLine = 4
        BilateralTwoLines = 5
        UnilateralAbove = 6
        UnilateralBelow = 7
        BasicTol = 8
        ReferenceTol = 9
        LimitLargerFirst = 10
        LimitLargerBelow = 11
        NotToScaleTol = 12
        DiameterReferenceTol = 13
        LimitAndFit = 14
        BasicDimNotToScaleTol = 15
        MaxNumTol = 16
    

    class TolerancePlacement(enum.Enum):
        ToleranceBelowDimension = 1
        ToleranceAfterDimension = 2
        ToleranceAboveDimension = 3
    

    class TextType(enum.Enum):
        DimText = 1
        DualDimText = 2
        ToleranceText = 3
        DualToleranceText = 4
        RadDiaText = 5
        TextAppAtCreation = 6
        TextAppAtEditing = 7
    

    class TextJust(enum.Enum):
        TextLeft = 1
        TextCenter = 2
        TextRight = 3
    

    class UFDrfTextCfw():
        color: int
        font: int
        width: UF.UFDrf.LineWidth
    

    class TextArrowPlacement(enum.Enum):
        AutoPlacement = 1
        PlacementManualArrowsIn = 2
        PlacementManualArrowsOut = 3
        PlacementManualArrowsSameDirection = 4
    

    class TextAboveLeader(enum.Enum):
        NoTextAboveLeader = 0
        LeaderBottomTextMax = 1
        LeaderBottomTextMaxUnderline = 2
        LeaderBottomText = 3
        LeaderBottomTextUnderline = 4
        LeaderTopTextMax = 5
        LeaderTopTextMaxUnderline = 6
        LeaderTopText = 7
        LeaderTopTextUnderline = 8
    

    class UFDrfText():
        user_dim_text: str
        lines_app_text: int
        appended_text: str
    

    class UFDrfSymbolPreferences():
        id_symbol_size: float
        id_symbol_cfw: UF.UFDrf.Cfw
        user_defined_symbol_cfw: UF.UFDrf.Cfw
        centerline_symbol_cfw: UF.UFDrf.Cfw
        intersection_symbol_cfw: UF.UFDrf.Cfw
        target_symbol_cfw: UF.UFDrf.Cfw
        gdt_symbol_cfw: UF.UFDrf.Cfw
    

    class UFDrfSymbolInstance():
        master: Tag
        is_gap: bool
        origin: float
        parameter_on_element: float
        symbol_length: float
        symbol_height: float
        creation_mask: int
        record_number: int
        segment_number: int
        is_mirrored: bool
        is_reflected: bool
    

    class UFDrfSymbolData():
        anchor_point: float
        orient_point: float
        angle: float
        length: float
        height: float
        symbol_font_tag: Tag
    

    class UFDrfSymbolCreateData():
        symbol_name: str
        angle: float
        length: float
        height: float
        anchor_tag: Tag
    

    class SymbolConnectionType(enum.Enum):
        LeftLeaderConnection = 0
        RightLeaderConnection = 1
    

    class UFDrfSymbolConnection():
        connection_type: UF.UFDrf.SymbolConnectionType
        connection_point: Tag
    

    class UFDrfStrokeInfo():
        pen_status: UF.UFDrf.UdSymbolPenType
        x_length: int
        y_length: int
    

    class StackAlignPosition(enum.Enum):
        StackAlignAbove = 0
        StackAlignBelow = 1
        StackAlignLeft = 2
        StackAlignRight = 3
    

    

    

    class RetainedState(enum.Enum):
        KeepRetainedAnnotations = 0
        DeleteRetainedAnnotations = 1
    

    class RenderTextStatus(enum.Enum):
        RenderCannotRenderSymbol = -2
        RenderCannotRenderChar = -1
        RenderOk = 0
        RenderDrawn = 1
        RenderNotDrawn = 2
    

    class UFDrfRenderTable():
        begin_line: UF.UFDrf.BeginLineFnT
        end_line: UF.UFDrf.EndLineFnT
        set_to_position: UF.UFDrf.SetToPositionFnT
        draw_to_position: UF.UFDrf.DrawToPositionFnT
        draw_arc: UF.UFDrf.DrawArcFnT
        draw_char: UF.UFDrf.DrawCharFnT
        draw_standard_font_string: UF.UFDrf.DrawStandardFontStringFnT
        draw_user_symbol: UF.UFDrf.DrawUserSymbolFnT
        set_cfw: UF.UFDrf.SetCfwFnT
        push_orientation: UF.UFDrf.PushOrientationFnT
        pop_orientation: UF.UFDrf.PopOrientationFnT
        fill_region: UF.UFDrf.FillRegionFnT
        standardFontFunCharSize: float
    

    class ReferenceSymbolType(enum.Enum):
        NoReferenceSymbol = 0
        WithReferenceSymbol = 1
    

    class RadiusSymbol(enum.Enum):
        RadiusUseR = 1
        RadiusUseRad = 2
        UserDefinedRadiusSymbol = 3
        RadiusUseSr = 4
        RadiusUseCr = 5
    

    class QuadrantType(enum.Enum):
        QuadrantOne = 1
        QuadrantTwo = 2
        QuadrantThree = 3
        QuadrantFour = 4
        QuadrantFive = 5
    

    

    

    class OrdoriginDisplayType(enum.Enum):
        OrdoriginUdSymbol = 0
        OrdoriginHorVerDim = 1
        OrdoriginHorizontalDim = 2
        OrdoriginVerticalDim = 3
        OrdoriginName = 4
    

    class UFDrfOrddispInfo():
        quadrant: UF.UFDrf.QuadrantType
        name_display: UF.UFDrf.OrdoriginDisplayType
        origin_name: str
        arr_display: UF.UFDrf.OrdarrowLineType
        symfont: int
    

    class OrdarrowLineType(enum.Enum):
        OrdarrowLineNoDisplay = 0
        OrdarrowLineDisplay = 1
    

    class ObjectAssocPointType(enum.Enum):
        NoPointType = 0
        ControlPointPointType = 1
        ArcCenterPointType = 2
        TangentPointType = 3
        IntersectionPointType = 4
        ScreenPositionPointType = 5
        CylindricalFaceType = 6
        PointOnCurvePointType = 7
        OffsetCirclePointType = 8
        SplinePolePointType = 9
        ConicAnchorPointType = 10
        SplineDefPointType = 11
        RoutingPointType = 12
    

    class ObjectAssocLineType(enum.Enum):
        NoLineType = 0
        ExistingLineType = 1
        PointVectorLineType = 2
        ExtensionLineType = 3
        CenterlineComponentLineType = 4
        EnteredAngleLineType = 5
        HorizontalRightLineType = 6
        VerticalUpLineType = 7
        HorizontalLeftLineType = 8
        VerticalDownLineType = 9
        BaseLineType = 10
    

    class UFDrfObjectAssocData():
        assoc_object_1: Tag
        assoc_object_2: Tag
        object_view: Tag
        point_type: UF.UFDrf.ObjectAssocPointType
        line_type: UF.UFDrf.ObjectAssocLineType
        base_pt_1: float
        base_pt_2: float
        entered_angle: float
        assoc_point: float
    

    class UFDrfObject():
        object_tag: Tag
        object_view_tag: Tag
        object_assoc_type: UF.UFDrf.AssocType
        object_assoc_modifier: int
        object2_tag: Tag
        assoc_dwg_pos: float
    

    class NarrowDimensionTextOrientation(enum.Enum):
        NarrowHorizontal = 0
        NarrowParallel = 1
    

    class UFDrfNarrowDimensionInfo():
        display_type: UF.UFDrf.NarrowDimensionDisplayType
        text_orientation: UF.UFDrf.NarrowDimensionTextOrientation
        leader_angle: float
        text_offset: float
    

    class NarrowDimensionDisplayType(enum.Enum):
        NarrowDisplayNone = 0
        NarrowDisplayNoLeader = 1
        NarrowDisplayWithLeaderNoStub = 2
        NarrowDisplayTextAboveStub = 3
        NarrowDisplayTextAfterStub = 4
    

    class LineWidth(enum.Enum):
        Normal = 1
        Thick = 2
        Thin = 3
        ThicknessOne = 6
        ThicknessTwo = 7
        ThicknessThree = 8
        ThicknessFour = 9
        ThicknessFive = 10
        ThicknessSix = 11
        ThicknessSeven = 12
        ThicknessEight = 13
        ThicknessNine = 14
    

    class UFDrfLineObject():
        line_assoc_type: UF.UFDrf.AssocLineType
        object1: UF.UFDrf.Object
        point_object2: UF.UFDrf.Object
    

    class LinearUnits(enum.Enum):
        Millimeters = 1
        Meters = 2
        Inches = 3
        ArchitecturalFeetInches = 4
        EngineeringFeetInches = 5
    

    class UFDrfLineArrowPreferences():
        first_arrow_type: UF.UFDrf.ArrowheadAndFillType
        second_arrow_type: UF.UFDrf.ArrowheadAndFillType
        leader_location: UF.UFDrf.VerticalTextJust
        arrowhead_length: float
        arrowhead_included_angle: float
        dot_arrowhead_diameter: float
        stub_length: float
        text_to_line_distance: float
        line_past_arrow_distance: float
        oblique_extension_line_angle: float
        first_pos_to_extension_line_distance: float
        second_pos_to_extension_line_distance: float
        datum_length_past_arrow: float
        text_over_stub_factor: float
        first_extension_line_cfw: UF.UFDrf.Cfw
        first_arrowhead_cfw: UF.UFDrf.Cfw
        first_arrow_line_cfw: UF.UFDrf.Cfw
        second_extension_line_cfw: UF.UFDrf.Cfw
        second_arrowhead_cfw: UF.UFDrf.Cfw
        second_arrow_line_cfw: UF.UFDrf.Cfw
        arrow_out_length_factor: float
        allAroundSymbolSize: float
    

    class UFDrfLetteringPreferences():
        align_position: UF.UFDrf.AlignPosition
        horiz_text_just: UF.UFDrf.TextJust
        gdt_frame_height_factor: float
        angle: float
        dimension_text: UF.UFDrf.Lettering
        appended_text: UF.UFDrf.Lettering
        tolerance_text: UF.UFDrf.Lettering
        general_text: UF.UFDrf.Lettering
        dim_dim_line_space_factor: float
        dim_app_text_space_factor: float
        dim_tol_text_space_factor: float
    

    class UFDrfLettering():
        size: float
        character_space_factor: float
        aspect_ratio: float
        line_space_factor: float
        cfw: UF.UFDrf.TextCfw
    

    class LeaderType(enum.Enum):
        LeaderTypeNone = 1
        LeaderTypeLine = 2
        LeaderTypeExtLine = 3
        LeaderTypeDatum = 4
        LeaderTypeMaximum = 5
    

    class LeaderSide(enum.Enum):
        LeaderSideLeft = 0
        LeaderSideRight = 1
    

    class LeaderOrientation(enum.Enum):
        NoStub = 0
        LeaderLeft = 1
        LeaderRight = 2
        LeaderTop = 3
        LeaderBottom = 4
    

    class LeaderMode(enum.Enum):
        WithoutLeader = 1
        WithLeader = 2
    

    class UFDrfLeaderInfo():
        leader_attach_type: typing.List[UF.UFDrf.LeaderAttachType]
        num_linebks: int
        leader_pnts: typing.List[UF.UFDrf.DraftAidLine]
        num_assoc_objs: int
        assoc_objs: typing.List[UF.UFDrf.AssocInfo]
    

    class UFDrfLeaderData():
        num_leaders: int
        associativity_data: typing.List[UF.UFDrf.ObjectAssocData]
        leader_orientation: UF.UFDrf.LeaderOrientation
        intermediate_points: typing.List[UF.UFDrf.IntermediatePoints]
    

    class LeaderAttachType(enum.Enum):
        LeaderAttachObject = 1
        LeaderAttachScreen = 2
        LeaderAttachTriangle = 3
    

    class UFDrfLeader():
        num_leaders: int
        leader_terminators: typing.List[Tag]
        leader_orientation: UF.UFDrf.LeaderOrientation
        intermediate_points: typing.List[UF.UFDrf.IntermediatePoints]
    

    class UFDrfLabelInfo():
        num_text: int
        text_info: typing.List[UF.UFDrf.DraftAidTextInfo]
        num_leaders: int
        leader_info: typing.List[UF.UFDrf.LeaderInfo]
        num_arrows: int
        arrow_info: typing.List[UF.UFDrf.ArrowInfo]
    

    class UFDrfIntermediatePoints():
        num_points: int
        points: float
    

    class InspectionType(enum.Enum):
        NoInspection = 0
        WithInspection = 1
    

    class InheritType(enum.Enum):
        InheritFeatureParameters = 1
        InheritPositionalDimensions = 2
        InheritParametersAndPositions = 3
    

    class UFDrfImageData():
        image_name: str
        drawing_sheet: Tag
        aspect_ratio_locked: bool
        width: float
        height: float
        alignment_position: UF.UFDrf.AlignPosition
        origin: float
        width_dir: float
        height_dir: float
    

    class IdSymbolType(enum.Enum):
        SymCircle = 1
        SymDivcir = 2
        SymSquare = 3
        SymDivsqr = 4
        SymHexagon = 5
        SymDivhex = 6
        SymTriup = 7
        SymTridown = 8
        SymDatum = 9
        SymRoundbox = 10
        SymUnderline = 11
        SymMaximum = 12
    

    class UFDrfIdSymbolInfo():
        size: float
        num_text: int
        text_info: typing.List[UF.UFDrf.DraftAidTextInfo]
        num_leaders: int
        leader_info: typing.List[UF.UFDrf.LeaderInfo]
        num_arrows: int
        arrow_info: typing.List[UF.UFDrf.ArrowInfo]
    

    class UFDrfHatchFillPreferences():
        hatch_distance: float
        hatch_angle: float
        hatch_tolerance: float
        hatch_file: str
        hatch_material: str
        area_fill_material: UF.UFDrf.AreaFillMaterial
        area_fill_scale: float
        area_fill_angle: float
        color: int
        width: UF.UFDrf.LineWidth
    

    class UFDrfGdtSymbolInfo():
        num_text: int
        text_info: typing.List[UF.UFDrf.DraftAidTextInfo]
        num_leaders: int
        leader_info: typing.List[UF.UFDrf.LeaderInfo]
        num_arrows: int
        arrow_info: typing.List[UF.UFDrf.ArrowInfo]
    

    class UFDrfGdtLeaderData():
        _object: Tag
        view: Tag
        point: float
        intermediate_points: UF.UFDrf.IntermediatePoints
    

    class UFDrfGdtLeader():
        leader_type: UF.UFDrf.LeaderType
        leader_side: UF.UFDrf.LeaderSide
        num_leaders: int
        leader_data: typing.List[UF.UFDrf.GdtLeaderData]
    

    class FrameCorner(enum.Enum):
        FrameNone = 0
        FrameUpperLeft = 1
        FrameUpperRight = 2
        FrameLowerLeft = 3
        FrameLowerRight = 4
    

    class FractionType(enum.Enum):
        Decimal = 1
        HalfSizeFraction = 2
        TwoThirdSizeFraction = 3
        FullSizeFraction = 4
    

    class FractionDenominator(enum.Enum):
        FractionDenom1 = 1
        FractionDenom2 = 2
        FractionDenom4 = 4
        FractionDenom8 = 8
        FractionDenom16 = 16
        FractionDenom32 = 32
        FractionDenom64 = 64
    

    class UFDrfFoldedRadiusInfo():
        fold_location: float
        fold_angle: float
        fold_offset: float
    

    

    class ExtensionLineDisplay(enum.Enum):
        DisplayTwoExtLines = 1
        DisplayExtLine1 = 2
        DisplayExtLine2 = 3
        DisplayNoExtLine = 4
    

    

    class DualDimensionFormat(enum.Enum):
        DualDimensionBelow = 1
        DualDimensionAfter = 2
        DualDimensionAbove = 3
        DualDimensionBefore = 4
        NoDualDimension = 5
    

    

    

    

    

    

    class UFDrfDraftAidTextInfo():
        text_type: UF.UFDrf.TextType
        text_font: int
        size: float
        angle: float
        origin: float
        length: float
        height: float
        distance: float
        aspect_ratio: float
        gap: float
        line_spacing: float
        num_lines: int
        text: typing.List[UF.UFDrf.DraftAidText]
    

    class UFDrfDraftAidText():
        num_chars: int
        _string: str
        num_ints: int
        full_num_chars: int
        full_string: str
    

    class UFDrfDraftAidLine():
        sequence_number: int
        num_symbols: int
        symbol_data: typing.List[UF.UFDrf.SymbolInstance]
        num_segments: int
        segment_pnts: float
    

    class DoglegType(enum.Enum):
        OrddimensionNoDogleg = 1
        OrddimensionDogleg = 2
    

    class UFDrfDoglegInfo():
        dogleg_type: UF.UFDrf.DoglegType
        dogleg_angle: float
        dogleg_distance: float
    

    class UFDrfDimLineInfo():
        line_pnts: typing.List[UF.UFDrf.DraftAidLine]
        num_assoc_objs: int
        assoc_objs: typing.List[UF.UFDrf.AssocInfo]
    

    class UFDrfDimInfo():
        num_text: int
        text_info: typing.List[UF.UFDrf.DraftAidTextInfo]
        num_lines: int
        dim_line_info: typing.List[UF.UFDrf.DimLineInfo]
        num_arcs: int
        arc_info: typing.List[UF.UFDrf.ArcInfo]
        num_arrows: int
        arrow_info: typing.List[UF.UFDrf.ArrowInfo]
    

    class UFDrfDimensionPreferences1():
        tolerance_type: UF.UFDrf.ToleranceType
        upper_tolerance_english: float
        lower_tolerance_english: float
        upper_tolerance_metric: float
        lower_tolerance_metric: float
        upper_tolerance_deg: float
        lower_tolerance_deg: float
        dimension_value_dp: int
        tolerance_value_dp: int
        dual_dimension_value_dp: int
        dual_tolerance_value_dp: int
        angular_dimension_value_dp: int
        angular_tolerance_value_dp: int
        dim_fraction_denominator: UF.UFDrf.FractionDenominator
        dual_fraction_denominator: UF.UFDrf.FractionDenominator
        text_arrow_placement: UF.UFDrf.TextArrowPlacement
        extension_line_display: UF.UFDrf.ExtensionLineDisplay
        arrow_display: UF.UFDrf.ArrowDisplay
        line_between_arrows: bool
        orientation: UF.UFDrf.DimensionOrientation
        text_angle: float
        baseline_offset: float
        chain_offset: float
        narrow_dimension_data: typing.List[UF.UFDrf.NarrowDimensionInfo]
        narrow_dimension_arrowhead_type: UF.UFDrf.ArrowheadAndFillType
        chamfer_dimension_data: typing.List[UF.UFDrf.ChamferDimensionData]
        dim_inspection_type: UF.UFDrf.InspectionType
        dim_reference_type: UF.UFDrf.ReferenceSymbolType
        trim_dim_line: UF.UFDrf.TrimDimLineStyle
    

    class UFDrfDimensionPreferences():
        tolerance_type: UF.UFDrf.ToleranceType
        upper_tolerance_english: float
        lower_tolerance_english: float
        upper_tolerance_metric: float
        lower_tolerance_metric: float
        upper_tolerance_deg: float
        lower_tolerance_deg: float
        dimension_value_dp: int
        tolerance_value_dp: int
        dual_dimension_value_dp: int
        dual_tolerance_value_dp: int
        angular_dimension_value_dp: int
        angular_tolerance_value_dp: int
        dim_fraction_denominator: UF.UFDrf.FractionDenominator
        dual_fraction_denominator: UF.UFDrf.FractionDenominator
        text_arrow_placement: UF.UFDrf.TextArrowPlacement
        extension_line_display: UF.UFDrf.ExtensionLineDisplay
        arrow_display: UF.UFDrf.ArrowDisplay
        line_between_arrows: bool
        orientation: UF.UFDrf.DimensionOrientation
        text_angle: float
        baseline_offset: float
        chain_offset: float
        narrow_dimension_data: UF.UFDrf.NarrowDimensionInfo
        narrow_dimension_arrowhead_type: UF.UFDrf.ArrowheadAndFillType
        chamfer_dimension_data: UF.UFDrf.ChamferDimensionData
        dim_inspection_type: UF.UFDrf.InspectionType
        dim_reference_type: UF.UFDrf.ReferenceSymbolType
        trim_dim_line: UF.UFDrf.TrimDimLineStyle
    

    class DimensionOrientation(enum.Enum):
        DimensionTextHorizontal = 1
        DimensionTextAligned = 2
        DimensionTextOverDimensionLine = 3
        DimensionTextByAngle = 4
        DimensionTextPerpendicular = 5
        DimensionTextSplitByDimensionLine = 6
    

    class DiameterSymbol(enum.Enum):
        DiameterUseDia = 1
        StandardDiameterSymbol = 2
        UserDefinedDiameterSymbol = 3
        SphericalDiameterSymbol = 4
    

    class UFDrfDiameterRadiusPreferences():
        diameter_symbol_type: UF.UFDrf.DiameterSymbol
        diameter_symbol: str
        radius_symbol_type: UF.UFDrf.RadiusSymbol
        radius_symbol: str
        diameter_radius_placement: UF.UFDrf.DiameterRadiusPlacement
        text_above_leader: UF.UFDrf.TextAboveLeader
        symbol_to_dimension_text_distance: float
        folded_radius_angle: float
    

    class DiameterRadiusPlacement(enum.Enum):
        DiaRadBelow = 1
        DiaRadAfter = 2
        DiaRadAbove = 3
        DiaRadBefore = 4
        DiaRadOmit = 5
    

    class DecimalPointCharacter(enum.Enum):
        DecimalPointPeriod = 1
        DecimalPointComma = 2
    

    class CustomSymbolTextType(enum.Enum):
        MandatoryText = 0
        PartiallyControlledText = 1
        FullyControlledText = 2
        ArbitraryText = 3
        IntegerText = 4
        RealText = 5
        RuleText = 6
    

    class UFDrfCustomSymbolText():
        note_tag: Tag
        text_type: UF.UFDrf.CustomSymbolTextType
        title: str
        min_value: float
        max_value: float
        current_value: float
        optional_strings: str
        num_optional_strings: int
        current_option: int
        simple_text: str
    

    class UFDrfCustomSymbol():
        geometry: typing.List[Tag]
        num_geometry: int
        text: typing.List[UF.UFDrf.CustomSymbolText]
        num_text: int
        anchor_point: Tag
        connections: typing.List[UF.UFDrf.SymbolConnection]
        num_connections: int
        leader: typing.List[UF.UFDrf.Leader]
        angle: float
        scale: float
        origin: float
    

    class ChamferDimensionSymbolType(enum.Enum):
        ChamferNoneSymbol = 1
        ChamferPrefixSymbol = 2
        ChamferSuffixSymbol = 3
    

    class ChamferDimensionStubType(enum.Enum):
        ChamferTextaboveLeaderNostub = 1
        ChamferTextafterLeaderNostub = 2
        ChamferTextaboveStub = 3
        ChamferTextafterStub = 4
    

    class ChamferDimensionLeaderType(enum.Enum):
        ChamferPerpendicularLeader = 1
        ChamferParallelLeader = 2
        ChamferLinearChamferDim = 3
    

    class ChamferDimensionForm(enum.Enum):
        ChamferFormSymbol = 1
        ChamferFormSize = 2
        ChamferFormSizeangle = 3
        ChamferFormAnglesize = 4
    

    class UFDrfChamferDimensionData():
        form: UF.UFDrf.ChamferDimensionForm
        stub_type: UF.UFDrf.ChamferDimensionStubType
        leader_type: UF.UFDrf.ChamferDimensionLeaderType
        symbol_type: UF.UFDrf.ChamferDimensionSymbolType
        symbol_name: str
        space_factor: float
    

    class UFDrfCfw():
        color: int
        font: int
        width: UF.UFDrf.LineWidth
    

    class UFDrfCenterlineInfo():
        num_lines: int
        line_info: typing.List[UF.UFDrf.DraftAidLine]
        num_arcs: int
        arc_info: typing.List[UF.UFDrf.ArcInfo]
        num_assoc_objs: int
        assoc_objs: typing.List[UF.UFDrf.AssocInfo]
    

    

    class UFDrfAssortpartText():
        num_text: int
        num_lines_text: int
        text: str
        text_origin: float
    

    class UFDrfAssortpartLine():
        num_lines: int
        num_line_segments: int
        line_data: float
    

    class UFDrfAssortpartArrow():
        num_arrows: int
        arrowhead_subtype: int
        arrow_data: float
    

    class UFDrfAssortpartArc():
        num_arcs: int
        num_arc_segments: int
        arc_data: float
    

    class AssocType(enum.Enum):
        AssocTypeNone = 0
        EndPoint = 1
        ArcCenter = 2
        Tangency = 3
        Intersection = 4
        DwgPos = 5
        UtilitySymbol = 9
        SmartPoint = 10
        OnAnnotation = 11
        OnStub = 12
        AssocTypeMaximum = 13
    

    class AssocLineType(enum.Enum):
        AssocLineTypeNone = 0
        ExistingLine = 1
        TwoPoints = 2
        DwgLine = 3
        AssocLineTypeMax = 4
    

    class UFDrfAssocInfo():
        assoc_object_tag: Tag
        assoc_object_view_tag: Tag
        assoc_type: UF.UFDrf.AssocType
        assoc_modifier: int
    

    class AssociativeOriginType(enum.Enum):
        OriginDrag = 0
        OriginRelativeToView = 1
        OriginRelativeToGeometry = 2
        OriginVerticallyAligned = 3
        OriginHorizontallyAligned = 4
        OriginAlignedWithArrows = 5
        OriginAtAPoint = 6
        OriginOffsetFromText = 7
        OriginStack = 8
    

    class UFDrfAssociativeOrigin():
        origin_type: UF.UFDrf.AssociativeOriginType
        view_eid: Tag
        view_of_geometry: Tag
        point_on_geometry: Tag
        vert_annotation: Tag
        vert_alignment_position: UF.UFDrf.AlignPosition
        horiz_annotation: Tag
        horiz_alignment_position: UF.UFDrf.AlignPosition
        aligned_annotation: Tag
        dimension_line: int
        associated_view: Tag
        associated_point: Tag
        offset_annotation: Tag
        offset_alignment_position: UF.UFDrf.AlignPosition
        x_offset_factor: float
        y_offset_factor: float
        stack_annotation: Tag
        stack_alignment_position: UF.UFDrf.StackAlignPosition
    

    class ArrowType(enum.Enum):
        ArrowClosed = 1
        ArrowOpen = 2
        ArrowCross = 3
        ArrowDot = 4
        ArrowSym = 5
        ArrowNone = 6
        DatumArrow = 7
        ArrowSolidClosed = 8
        ArrowDoubleClosed = 9
        ArrowDoubleSolidClosed = 10
        ArrowDoubleOpen = 11
        ArrowIntegral = 12
        ArrowBox = 13
        ArrowTopOpen = 14
        ArrowBottomOpen = 15
    

    class UFDrfArrowInfo():
        sequence_number: int
        arrow_type: UF.UFDrf.ArrowType
        arrow_fill: UF.UFDrf.ArrowFillType
        arrow_origin: float
        arrow_angle: float
        arrow_include_angle: float
        arrow_height: float
        arrow_width: float
    

    class ArrowheadAndFillType(enum.Enum):
        FilledDot = -1
        FilledArrow = 0
        ClosedArrow = 1
        OpenArrow = 2
        CrossArrow = 3
        DotArrow = 4
        OriginSymbolArrow = 5
        NoArrow = 6
        ClosedSolidArrow = 8
        ClosedDoubleArrow = 9
        ClosedDoubleSolidArrow = 10
        OpenDoubleArrow = 11
        IntegralArrow = 12
        BoxArrow = 13
        FilledBox = 14
        FilledDoubleArrow = 15
    

    class ArrowFillType(enum.Enum):
        ArrowNoFill = 0
        ArrowFilled = 1
    

    class ArrowDisplay(enum.Enum):
        DisplayTwoArrows = 1
        DisplayArrow1 = 2
        DisplayArrow2 = 3
        DisplayNoArrows = 4
    

    class AreaFillMaterial(enum.Enum):
        CorkFelt = 1
        SoundInsulation = 2
        Concrete = 3
        Earth = 4
        Rock = 5
        Sand = 6
        Liquids = 7
        WoodAcrossGrain = 8
        WoodAlongGrain = 9
        SolidFill = 10
    

    class UFDrfAreafill():
        material: UF.UFDrf.ValidMaterial
        scale: float
        angle: float
        tolerance: float
    

    class UFDrfArcInfo():
        arc_type: int
        sequence_number: int
        arc_center: float
        radius: float
        start_angle: float
        end_angle: float
        num_symbols: int
        symbol_data: typing.List[UF.UFDrf.SymbolInstance]
        num_assoc_objs: int
        assoc_objs: typing.List[UF.UFDrf.AssocInfo]
    

    class AppendedTextLocation(enum.Enum):
        AppendedTextBefore = 0
        AppendedTextAfter = 1
        AppendedTextAbove = 2
        AppendedTextBelow = 3
    

    class UFDrfAppendedText():
        location: UF.UFDrf.AppendedTextLocation
        num_lines: int
        text: str
    

    class AngularUnits(enum.Enum):
        FractionalDegrees = 1
        WholeDegrees = 2
        DegreesMinutes = 3
        DegreesMinutesSeconds = 4
    

    class AngularSuppressZeros(enum.Enum):
        AngDisplayZeros = 1
        AngSuppressLeadingZeros = 2
        AngSuppressAnyZeros = 3
        AngSuppressTrailingZeros = 4
    

    class AlignPosition(enum.Enum):
        AlignTopLeft = 1
        AlignTopCenter = 2
        AlignTopRight = 3
        AlignMidLeft = 4
        AlignMidCenter = 5
        AlignMidRight = 6
        AlignBottomLeft = 7
        AlignBottomCenter = 8
        AlignBottomRight = 9
    

class UFDraw(Utilities.NXRemotableObject):
    def AddAuxiliaryView(self, drawing_tag: Tag, parent_view_tag: Tag, hinge_line_tag: Tag, dwg_reference_point: float, aux_view_tag: Tag) -> None:
        ...
    def AddCircDetailView(self, drawing_tag: Tag, parent_view_tag: Tag, center_pt_tag: Tag, circle_pt_tag: Tag, view_scale: float, dwg_reference_point: float, detail_view_tag: Tag) -> None:
        ...
    def AddDetailView(self, drawing_tag: Tag, parent_view_tag: Tag, xy1: float, xy2: float, view_scale: float, dwg_reference_point: float, detail_view_tag: Tag) -> None:
        ...
    def AddOrthographicView(self, drawing_tag: Tag, parent_view_tag: Tag, projection_direction: UF.UFDraw.ProjDir, dwg_reference_point: float, ortho_view_tag: Tag) -> None:
        ...
    def AddSxlineSxseg(self, sxline_tag: Tag, sxseg_type: UF.UFDraw.SxsegType, sxline_leg: UF.UFDraw.SxlineLeg, _object: UF.UFDrf.Object, sxseg_tag: Tag) -> None:
        ...
    def AddSxseg(self, sxline_tag: Tag, sxseg_data: UF.UFDraw.SxlineSxsegs, sxseg_tag: Tag) -> None:
        ...
    def AskAutoUpdate(self, view_tag: Tag, auto_update: bool) -> None:
        ...
    def AskBodySilsInView(self, body_tag: Tag, view_tag: Tag, num_silhouettes: int, silhouette_tags: typing.List[Tag]) -> None:
        ...
    def AskBorderColor(self, border_color: int) -> None:
        ...
    def AskBorderDisplay(self, border_display: bool) -> None:
        ...
    def AskBoundByObjects(self, view_tag: Tag, num_objects: int, bounded_objects: typing.List[Tag]) -> None:
        ...
    def AskBoundaryCurves(self, view_tag: Tag, tolerance: float, num_curves: int, boundary_curves: typing.List[UF.UFDraw.ViewBoundary]) -> None:
        ...
    def AskBoundaryType(self, view_tag: Tag, boundary_type: UF.UFDraw.BoundaryType) -> None:
        ...
    def AskBreakRegionData(self, region: Tag, break_region_data: UF.UFDraw.BreakRegionData) -> None:
        ...
    def AskBreakRegions(self, view_tag: Tag, num_regions: int, break_regions: typing.List[Tag]) -> None:
        ...
    def AskBreakoutData(self, breakline: Tag, view_tag: Tag, breakout_data: UF.UFDraw.BreakoutData) -> None:
        ...
    def AskCompSectionInView(self, component: Tag, sx_view: Tag, sx_property: UF.UFDraw.CompSectionInView) -> None:
        ...
    def AskCurrentDrawing(self, drawing_tag: Tag) -> None:
        ...
    def AskCurveGroupMembers(self, curve_group: Tag, curves: typing.List[Tag], curve_count: int) -> None:
        ...
    def AskCurveOfSxedge(self, sxseg_tag: Tag, curve_tag: Tag) -> None:
        ...
    def AskDisplayState(self, view_type: int) -> None:
        ...
    def AskDisplayedObjects(self, view: Tag, num_objects: int, objects: typing.List[Tag]) -> None:
        ...
    def AskDmvRotationPlane(self, view: Tag, plane: Tag) -> None:
        ...
    def AskDraftingCurveParents(self, input_curve_tag: Tag, parents_count: int, parents: typing.List[Tag]) -> None:
        ...
    def AskDraftingCurveType(self, input_curve_tag: Tag, curve_type: UF.UFDraw.DraftingCurveType) -> None:
        ...
    def AskDrawingOfView(self, member_view: Tag, drawing: Tag) -> None:
        ...
    def AskDrawingRefPt(self, view_tag: Tag, reference_pt: float) -> None:
        ...
    def AskDrawings(self, num_drawings: int, drawing_tags: typing.List[Tag]) -> None:
        ...
    def AskFaceOfSil(self, silhouette_tag: Tag, face_tag: Tag) -> None:
        ...
    def AskFaceSilsInView(self, face_tag: Tag, view_tag: Tag, num_silhouettes: int, sil_tags: typing.List[Tag]) -> None:
        ...
    def AskFoldedSxline(self, sxline_tag: Tag, step_dir: float, arrow_dir: float, pview_tag: Tag, num_sxviews: int, sxview_tags: typing.List[Tag], num_sxsegs: int, sxseg_tags: typing.List[Tag], sxline_status: UF.UFDraw.SxlineStatus) -> None:
        ...
    def AskGroupOfCurve(self, curve_tag: Tag, group_tag: Tag, group_type: int, group_subtype: int) -> None:
        ...
    def AskHalfSxline(self, sxline_tag: Tag, step_dir: float, arrow_dir: float, pview_tag: Tag, num_sxviews: int, sxview_tags: typing.List[Tag], num_sxsegs: int, sxseg_tags: typing.List[Tag], sxline_status: UF.UFDraw.SxlineStatus) -> None:
        ...
    def AskNumDrawings(self, num_drawings: int) -> None:
        ...
    def AskNumViews(self, drawing_tag: Tag, num_views: int) -> None:
        ...
    def AskPictorialSxline(self, sxline_tag: Tag, sxline_type: UF.UFDraw.SxlineType, cut_dir: float, arrow_dir: float, parent_view_tag: Tag, num_sxviews: int, sxview_tags: typing.List[Tag], num_sxsegs: int, sxseg_tags: typing.List[Tag], pictorial_sxview: bool, sxline_status: UF.UFDraw.SxlineStatus) -> None:
        ...
    def AskRenderSetObjects(self, render_set: Tag, number_objects: int, objects: typing.List[Tag]) -> None:
        ...
    def AskRenderSetParms(self, render_set: Tag, render_parms: UF.UFDraw.RenderPrefs) -> None:
        ...
    def AskRenderSets(self, number_render_sets: int, render_sets: typing.List[Tag]) -> None:
        ...
    def AskRenderSetsOfView(self, view: Tag, number_render_sets: int, render_sets: typing.List[Tag]) -> None:
        ...
    def AskRevolvedSxline(self, sxline_tag: Tag, step_dir: float, arrow_dir: float, pview_tag: Tag, rotpt_object: UF.UFDrf.Object, num_sxviews: int, sxview_tags: typing.List[Tag], num_sxsegs: int, num_leg1_sxsegs: int, cut_plane_leg: UF.UFDraw.SxlineLeg, sxseg_tags: typing.List[Tag], sxline_status: UF.UFDraw.SxlineStatus) -> None:
        ...
    def AskSimpleSxline(self, sxline_tag: Tag, step_dir: float, arrow_dir: float, pview_tag: Tag, num_sxviews: int, sxview_tags: typing.List[Tag], num_sxsegs: int, sxseg_tags: typing.List[Tag], sxline_status: UF.UFDraw.SxlineStatus) -> None:
        ...
    def AskSimplifiedCurve(self, master_curve_tag: Tag, view_tag: Tag, flat_arc_to_line: bool, tolerance: float, num_segments: int, segments: typing.List[Tag]) -> None:
        ...
    def AskSolidOfSection(self, sxsolid_tag: Tag, solid_tag: Tag) -> None:
        ...
    def AskSteppedSxline(self, sxline_tag: Tag, step_dir: float, arrow_dir: float, pview_tag: Tag, num_sxviews: int, sxview_tags: typing.List[Tag], num_sxsegs: int, sxseg_tags: typing.List[Tag], sxline_status: UF.UFDraw.SxlineStatus) -> None:
        ...
    def AskSuppressViewUpdat(self, suppress_view_update: bool) -> None:
        ...
    def AskSxedgesOfSxsolid(self, sxsolid_tag: Tag, num_sxedges: int, sxedge_tags: typing.List[Tag]) -> None:
        ...
    def AskSxlineDefaultPrfs(self, arrow_parms: UF.UFDraw.ArrowParms, sxline_display: UF.UFDraw.SxlineDisplay) -> None:
        ...
    def AskSxlineDisplay(self, sxline_tag: Tag, arrow_parms: UF.UFDraw.ArrowParms, sxline_display: UF.UFDraw.SxlineDisplay) -> None:
        ...
    def AskSxlineOfSxview(self, sxview_tag: Tag, sxline_tag: Tag) -> None:
        ...
    def AskSxlineSxseg(self, sxseg_tag: Tag, sxseg_info: UF.UFDraw.SxsegInfo, curve_tag: Tag, _object: typing.List[UF.UFDrf.Object]) -> None:
        ...
    def AskSxlineType(self, sxline_tag: Tag, sxline_type: UF.UFDraw.SxlineType) -> None:
        ...
    def AskSxsolidsOfSxview(self, sxview_tag: Tag, leg_num: UF.UFDraw.SxlineLeg, num_sxsolids: int, sxsolid_tags: typing.List[Tag]) -> None:
        ...
    def AskSxviewDisplay(self, view_tag: Tag, sxview_parms: UF.UFDraw.SxviewPrfs) -> None:
        ...
    def AskTabularNoteDefaults(self, _params: UF.UFDraw.TabnotParams) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskTabularNoteParams(self, tabular_note: Tag, _params: UF.UFDraw.TabnotParams, eval_data: UF.UFDraw.TabnotEvalData) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskUnfoldedSxline(self, sxline_tag: Tag, step_dir: float, arrow_dir: float, pview_tag: Tag, num_sxviews: int, sxview_tags: typing.List[Tag], num_sxsegs: int, sxseg_tags: typing.List[Tag], sxline_status: UF.UFDraw.SxlineStatus) -> None:
        ...
    def AskViewAnchor(self, view_tag: Tag, anchor_point: Tag) -> None:
        ...
    def AskViewAngle(self, view_tag: Tag, angle_value: float) -> None:
        ...
    def AskViewBorders(self, view_tag: Tag, view_borders: float) -> None:
        ...
    def AskViewDisplay(self, view_tag: Tag, view_parms: UF.UFDraw.ViewPrfs) -> None:
        ...
    def AskViewLabel(self, view_tag: Tag, view_label_tag: Tag) -> None:
        ...
    def AskViewLabelParms(self, view_label_tag: Tag, view_label_parms: UF.UFDraw.ViewLabelParms) -> int:
        ...
    def AskViewNotes(self, view_tag: Tag, num_notes: int, note_tags: typing.List[Tag]) -> None:
        ...
    def AskViewOfDrawing(self, drawing: Tag, view: Tag) -> None:
        ...
    def AskViewOfNote(self, note_tag: Tag, view_tag: Tag) -> None:
        ...
    def AskViewOfViewLabel(self, view_label_tag: Tag, view_tag: Tag) -> None:
        ...
    def AskViewParmScale(self, view_tag: Tag, exp_tag: Tag, scale_value: float) -> None:
        ...
    def AskViewScale(self, view_tag: Tag, exp_tag: Tag, scale_value: float) -> None:
        ...
    def AskViewStatus(self, view_tag: Tag, view_status: UF.UFDraw.ViewStatus) -> None:
        ...
    def AskViewThdAppPitch(self, view: Tag, app_pitch: float) -> None:
        ...
    def AskViewThdMeth(self, view: Tag, method: int) -> None:
        ...
    def AskViews(self, drawing_tag: Tag, num_views: int, view_tag: typing.List[Tag]) -> None:
        ...
    def AskXhatchOfSxsolid(self, sxsolid_tag: Tag, xhatch_tag: Tag) -> None:
        ...
    def AttachNoteToView(self, note_tag: Tag, view_tag: Tag) -> None:
        ...
    def CopyView(self, view_tag: Tag, new_view: Tag) -> None:
        ...
    def CreateBreakRegion(self, view_tag: Tag, anchor_point: Tag, num_curves: int, curves: typing.List[UF.UFDraw.BreakRegionBoundary], break_region: Tag) -> None:
        ...
    def CreateBreakout(self, view_tag: Tag, breakout_data: UF.UFDraw.BreakoutData, breakline: Tag) -> None:
        ...
    def CreateRenderSet(self, render_set_name: str, render_parms: UF.UFDraw.RenderPrefs, render_set: Tag) -> None:
        ...
    def CreateSimpleSxview(self, dwg_tag: Tag, sxview_scale: float, step_dir: float, arrow_dir: float, pview_tag: Tag, cut_object: UF.UFDrf.Object, view_placement_pt: float, sxview_tag: Tag) -> None:
        ...
    def CreateSimplifiedCurve(self, master_curve_tag: Tag, view_tag: Tag, flat_arc_to_line: bool, num_segments: int, segments: typing.List[Tag]) -> None:
        ...
    def CreateTabularNote(self, _params: UF.UFDraw.TabnotParams, new_tabular_note: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateViewLabel(self, view_tag: Tag, view_label_parms: UF.UFDraw.ViewLabelParms, view_label_tag: Tag) -> None:
        ...
    def DefineBoundByObjects(self, view_tag: Tag, num_objects: int, bounded_objects: typing.List[Tag]) -> None:
        ...
    def DefineViewAutoRect(self, view_tag: Tag) -> None:
        ...
    def DefineViewBoundary(self, view_tag: Tag, curve_count: int, boundary_curves: typing.List[UF.UFDraw.DefineBoundary]) -> None:
        ...
    def DefineViewBoundary1(self, view_tag: Tag, curve_count: int, boundary_curves: typing.List[UF.UFDraw.DefineBoundary]) -> None:
        ...
    def DefineViewManualRect(self, view_tag: Tag, view_borders: float) -> None:
        ...
    def DeleteDrawing(self, drawing_tag: Tag) -> None:
        ...
    def DeleteSxlineSxseg(self, sxseg_tag: Tag) -> None:
        ...
    def DeleteTabnotCell(self, tabular_note: Tag, row: int, col: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DeleteViewLabel(self, view_tag: Tag) -> None:
        ...
    def DetachNoteFromView(self, note_tag: Tag) -> None:
        ...
    def EditBoundaryPoint(self, defining_point: Tag, new_point: Tag, view_tag: Tag) -> None:
        ...
    def EditSxlineDisplay(self, sxline_tag: Tag, arrow_parms: UF.UFDraw.ArrowParms, sxline_display: UF.UFDraw.SxlineDisplay) -> None:
        ...
    def EraseSxviewObjects(self, view: Tag, num_objects: int, objects: typing.List[Tag]) -> None:
        ...
    def GetViewModelViewPart(self, view: Tag, model_view_partname: str) -> None:
        ...
    def ImportView(self, drawing_tag: Tag, view_tag: Tag, dwg_reference_point: float, view_info: UF.UFDraw.ViewInfo, draw_view_tag: Tag) -> None:
        ...
    def InitializeViewInfo(self, view_info: UF.UFDraw.ViewInfo) -> None:
        ...
    def IsDraftingComponent(self, component: Tag, is_drafting_component: bool) -> None:
        ...
    def IsObjectOutOfDate(self, _object: Tag, out_of_date: bool) -> None:
        ...
    def IsSxview(self, view_tag: Tag, is_a_sxview: bool) -> None:
        ...
    def IsThreadCurve(self, curve_tag: Tag, is_thread_curve: bool) -> None:
        ...
    def MoveSxlineRotpt(self, sxline_tag: Tag, new_object: UF.UFDrf.Object) -> None:
        ...
    def MoveSxlineSxseg(self, sxseg_tag: Tag, new_object: UF.UFDrf.Object) -> None:
        ...
    def MoveSxseg(self, sxseg_tag: Tag, sxseg_data: UF.UFDraw.SxlineSxsegs) -> None:
        ...
    def MoveView(self, view_tag: Tag, drawing_reference_point: float) -> None:
        ...
    def MoveViewToDrawing(self, view_tag: Tag, drawing_tag: Tag) -> None:
        ...
    def OpenDrawing(self, drawing_tag: Tag) -> None:
        ...
    def ReadTabnotCell(self, tabular_note: Tag, row: int, col: int, _params: UF.UFDraw.TabnotCellParams, eval_data: UF.UFDraw.TabnotCellEvalData) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def ReadTabnotColWdt(self, tabular_note: Tag, col: int, width: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def ReadTabnotRowHgt(self, tabular_note: Tag, row: int, height: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RedefineSxlineHinge(self, sxline_tag: Tag, hinge_line: UF.UFDrf.LineObject, arrow_same_dir: bool) -> None:
        ...
    def RemoveBreakRegion(self, break_region: Tag, delete_curves: bool) -> None:
        ...
    def RemoveBreakout(self, breakline: Tag, delete_curves: bool) -> None:
        ...
    def RemoveDmvRotationPlane(self, view: Tag) -> None:
        ...
    def RenameDrawing(self, drawing_tag: Tag, new_drawing_name: str) -> None:
        ...
    def RetrieveDrawingCgm(self, file_name: str, out_file_names: str, num_sheets: int) -> None:
        ...
    def SetAutoUpdate(self, view_tag: Tag, auto_update: bool) -> None:
        ...
    def SetBorderColor(self, border_color: int) -> None:
        ...
    def SetBorderDisplay(self, border_display: bool) -> None:
        ...
    def SetBoundaryAssoc(self, view: Tag, curve_count: int, boundary_curves: typing.List[UF.UFDraw.ViewBoundary]) -> None:
        ...
    def SetBreakRegionData(self, break_region: Tag, break_region_data: UF.UFDraw.BreakRegionData) -> None:
        ...
    def SetBreakoutData(self, breakline: Tag, breakout_data: UF.UFDraw.BreakoutData, new_breakline: Tag) -> None:
        ...
    def SetCompSectionInView(self, component: Tag, sx_view: Tag, sx_property: UF.UFDraw.CompSectionInView) -> None:
        ...
    def SetDisplayState(self, view_type: int) -> None:
        ...
    def SetDmvRotationPlane(self, view: Tag, plane: Tag, x_vector: Tag) -> None:
        ...
    def SetDrawingRefPt(self, drawing_tag: Tag, view_tag: Tag, reference_pt: float) -> None:
        ...
    def SetRenderSetObjects(self, render_set: Tag, number_objects: int, objects: typing.List[Tag]) -> None:
        ...
    def SetRenderSetParms(self, render_set: Tag, render_parms: UF.UFDraw.RenderPrefs) -> None:
        ...
    def SetRenderSetsForView(self, view: Tag, number_render_sets: int, render_sets: typing.List[Tag]) -> None:
        ...
    def SetSuppressViewUpdat(self, suppress_view_update: bool) -> None:
        ...
    def SetSxlineDefaultPrfs(self, arrow_parms: UF.UFDraw.ArrowParms, sxline_display: UF.UFDraw.SxlineDisplay) -> None:
        ...
    def SetSxviewDisplay(self, view_tag: Tag, sxview_parms: UF.UFDraw.SxviewPrfs) -> None:
        ...
    def SetTabularNoteParams(self, tabular_note: Tag, _params: UF.UFDraw.TabnotParams) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetViewAnchor(self, view_tag: Tag, anchor_point: Tag) -> None:
        ...
    def SetViewAngle(self, view_tag: Tag, angle: float) -> None:
        ...
    def SetViewDisplay(self, view_tag: Tag, view_parms: UF.UFDraw.ViewPrfs) -> None:
        ...
    def SetViewLabelParms(self, view_label_tag: Tag, view_label_parms: UF.UFDraw.ViewLabelParms) -> None:
        ...
    def SetViewParmScale(self, view: Tag, exp_tag: Tag) -> None:
        ...
    def SetViewScale(self, view_tag: Tag, scale: float) -> None:
        ...
    def SetViewStatus(self, view_tag: Tag, view_status: UF.UFDraw.ViewStatus) -> None:
        ...
    def SetViewThdAppPitch(self, view: Tag, app_picth: float) -> None:
        ...
    def SetViewThdMeth(self, view: Tag, method: int) -> None:
        ...
    def UpdOutOfDateViews(self, drawing_tag: Tag) -> None:
        ...
    def UpdateOneView(self, drawing_tag: Tag, view_tag: Tag) -> None:
        ...
    def UpdateTabnot(self, tabular_note: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def WriteTabnotCell(self, tabular_note: Tag, row: int, col: int, _params: UF.UFDraw.TabnotCellParams) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def WriteTabnotColWdt(self, tabular_note: Tag, col: int, width: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def WriteTabnotRowHgt(self, tabular_note: Tag, row: int, height: float) -> None:
        """[Obsolete("Deprecated")"""
        ...


    class VirtualIntersect(enum.Enum):
        VirtualIntersectOff = 0
        VirtualIntersectOn = 1
    

    class ViewStatus(enum.Enum):
        ActiveView = 1
        ReferenceView = 2
    

    class UFDrawViewPrfs():
        hidden_line: UF.UFDraw.HiddenLine
        hidden_line_color: int
        hidden_line_font: int
        hidden_line_width: int
        edge_hiding_edge: UF.UFDraw.EdgeHidingEdge
        smooth: UF.UFDraw.Smooth
        tolerance: float
        silhouettes: UF.UFDraw.Silhouette
        uvhatch: UF.UFDraw.Uvhatch
        smooth_edge_color: int
        smooth_edge_font: int
        smooth_edge_width: int
        smooth_edge_gap: UF.UFDraw.Gap
        smooth_edge_gap_size: float
        virtual_intersect: UF.UFDraw.VirtualIntersect
        virtual_intersect_color: int
        virtual_intersect_font: int
        virtual_intersect_width: int
        virtual_intersect_gap: UF.UFDraw.Gap
        virtual_intersect_gap_size: float
        extracted_edges: UF.UFDraw.ExtractedEdges
        visible_line_color: int
        visible_line_font: int
        visible_line_width: int
        interfering_solids: int
        referenced_edges_only: bool
        edges_hidden_by_own_solid: bool
        simplify_small_features: int
        small_feature_tolerance: float
        traceline_visible_color: int
        traceline_visible_font: int
        traceline_visible_width: int
        traceline_hidden_color: int
        traceline_hidden_font: int
        traceline_hidden_width: int
        traceline_gap: UF.UFDraw.Gap
        traceline_gap_size: float
    

    class ViewLabelViewTextType(enum.Enum):
        ViewLabelViewName = 1
        ViewLabelPrefixAndLetter = 2
    

    class ViewLabelScalePosition(enum.Enum):
        ViewLabelBelow = 1
        ViewLabelAbove = 2
        ViewLabelBefore = 3
        ViewLabelAfter = 4
    

    class ViewLabelScaleFormat(enum.Enum):
        ViewLabelRatio = 1
        ViewLabelVerticalFraction = 2
        ViewLabelHorizontalFraction = 3
        ViewLabelNx = 4
    

    class ViewLabelPosition(enum.Enum):
        ViewLabelBelowBoundary = 1
        ViewLabelAboveBoundary = 2
    

    class ViewLabelParmType(enum.Enum):
        ViewLabelOtherView = 1
        ViewLabelDetailView = 2
        ViewLabelSectionView = 3
        ViewLabelProjectedView = 4
    

    class UFDrawViewLabelParms():
        view_label_parm_type: UF.UFDraw.ViewLabelParmType
        view_label_type: UF.UFDraw.ViewLabelViewTextType
        letter_format: UF.UFDraw.ViewLabelLetterFormat
        view_label_position: UF.UFDraw.ViewLabelPosition
        view_scale_position: UF.UFDraw.ViewLabelScalePosition
        view_scale_value_format: UF.UFDraw.ViewLabelScaleFormat
        view_label_text_to_stub_format: UF.DrfViewLabelTextToStubFormat
        letter_size_factor: float
        view_scale_prefix_factor: float
        view_scale_text_factor: float
        view_label: bool
        scale_label: bool
        view_label_customize: bool
        scale_parentheses: bool
        view_label_prefix: str
        scale_label_prefix: str
        view_letter: str
        parent_label_type: UF.UFDraw.LabelOnParentType
        text_to_gap_factor: float
        parent_vw_lbl_prefix: str
        show_rotation_symbol: bool
        show_rotation_angle: bool
        secondary_indexing_align: UF.UFDraw.SecondaryIndexingAlign
        subscript_size_factor: float
    

    class ViewLabelLetterFormat(enum.Enum):
        ViewLabelSingleLetter = 1
        ViewLabelDashedLetter = 2
    

    class UFDrawViewInfo():
        view_status: UF.UFDraw.ViewStatus
        anchor_point: Tag
        view_scale: float
        use_ref_pt: bool
        clean_model_view: bool
        inherit_boundary: bool
        transfer_annotation: bool
        inherit_pmi: bool
        model_name: str
        arrangement_name: str
    

    class UFDrawViewBoundary():
        curve_tag: Tag
        const_status: bool
        point_count: int
        defining_points: typing.List[Tag]
        hatch_tag: Tag
    

    class Uvhatch(enum.Enum):
        UvhatchOff = 0
        UvhatchOn = 1
    

    class UFDrawTabnotParams():
        position: float
        range_start: UF.UFDraw.TabnotCell
        range_end: UF.UFDraw.TabnotCell
        title_cell: UF.UFDraw.TabnotCell
        ug_aspect_ratio: float
        border_type: UF.UFDraw.TabnotBorderType
        border_width: float
        use_title_cell: bool
        use_grid_lines: bool
        use_vert_grid_lines: bool
        use_horiz_grid_lines: bool
        use_row_hdr_grid_lines: bool
        use_col_hdr_grid_lines: bool
        auto_size_cells: bool
    

    class UFDrawTabnotLine():
        start: float
        end: float
    

    class TabnotJust(enum.Enum):
        TabnotJustLeft = 1
        TabnotJustCenter = 2
        TabnotJustRight = 3
        TabnotJustTop = 4
        TabnotJustMiddle = 5
        TabnotJustBottom = 6
    

    class UFDrawTabnotEvalData():
        table_start: UF.UFDraw.TabnotCell
        table_end: UF.UFDraw.TabnotCell
        nm_lines: int
        lines: typing.List[UF.UFDraw.TabnotLine]
    

    class UFDrawTabnotCellParams():
        cell_text: str
        ug_font: str
        ug_text_height: float
        horiz_just: UF.UFDraw.TabnotJust
        vert_just: UF.UFDraw.TabnotJust
        text_angle: float
        is_bold: bool
        is_italic: bool
        is_underlined: bool
        is_wrapped: bool
        strikethru: bool
        is_hidden: bool
    

    class UFDrawTabnotCellEvalData():
        text_position: float
        eval_text: str
    

    class UFDrawTabnotCell():
        row: int
        col: int
    

    class TabnotBorderType(enum.Enum):
        TabnotBorderTypeNone = 1
        TabnotBorderTypeSingle = 2
        TabnotBorderTypeDouble = 3
    

    class UFDrawSxviewPrfs():
        sx_section_sheet_body: UF.UFDraw.SxSectionSheetBody
        sx_background: UF.UFDraw.SxBackground
        sx_crosshatch: UF.UFDraw.SxCrosshatch
        sx_assy_xhatch: UF.UFDraw.SxAssyXhatch
        xhatch_adj_toler: float
    

    class SxsegType(enum.Enum):
        SxsegArrow = 1
        SxsegCut = 2
        SxsegBend = 3
    

    class SxsegMode(enum.Enum):
        UserDefinedSxseg = 1
        SystemDefinedSxseg = 2
    

    class UFDrawSxsegInfo():
        sxseg_type: UF.UFDraw.SxsegType
        leg_num: UF.UFDraw.SxlineLeg
        sxseg_mode: UF.UFDraw.SxsegMode
        highlight_status: UF.UFDraw.SxsegHighlight
        sxseg_angle: float
    

    class SxsegHighlight(enum.Enum):
        Unhighlighted = 0
        Highlighted = 1
    

    class SxSectionSheetBody(enum.Enum):
        SxSectionSheetBodyOff = 0
        SxSectionSheetBodyOn = 1
    

    class SxlineType(enum.Enum):
        SimpleSxline = 1
        SteppedSxline = 2
        RevolvedSxline = 3
        HalfSxline = 4
        UnfoldedSxline = 5
        Breakline = 6
        FoldedSxline = 7
    

    class UFDrawSxlineSxsegs():
        sxseg_type: UF.UFDraw.SxsegType
        sxseg_object: typing.List[UF.UFDrf.Object]
        sxseg_angle: float
    

    class SxlineStatus(enum.Enum):
        InvalidSxline = 0
        ValidSxline = 1
        SxlineSxsegLostAssoc = 2
        SxlineRotptLostAssoc = 3
        SxlineRotptOrSxsegLostAssoc = 4
    

    class SxlineLeg(enum.Enum):
        SxlineLeg1 = 1
        SxlineLeg2 = 2
    

    class SxlineDisplay(enum.Enum):
        NoDisplaySxline = 1
        DisplaySxline = 2
    

    class SxCrosshatch(enum.Enum):
        SxCrosshatchOff = 0
        SxCrosshatchOn = 1
    

    class SxBackground(enum.Enum):
        SxBackgroundOff = 0
        SxBackgroundOn = 1
    

    class SxAssyXhatch(enum.Enum):
        SxAssyXhatchOff = 0
        SxAssyXhatchOn = 1
    

    class Smooth(enum.Enum):
        SmoothOff = 0
        SmoothOn = 1
    

    class Silhouette(enum.Enum):
        SilhouettesOff = 0
        SilhouettesOn = 1
    

    class SecondaryIndexingAlign(enum.Enum):
        SecondaryIndexingInline = 0
        SecondaryIndexingSubscript = 1
    

    class UFDrawRenderPrefs():
        hidden_line: UF.UFDraw.HiddenLine
        hidden_line_color: int
        hidden_line_font: int
        hidden_line_width: int
        edge_hiding_edge: UF.UFDraw.EdgeHidingEdge
        visible_line_color: int
        visible_line_font: int
        visible_line_width: int
        referenced_edges_only: bool
        edges_hidden_by_own_solid: bool
    

    class ProjDir(enum.Enum):
        ProjectInfer = 0
        ProjectAbove = 1
        ProjectRight = 2
        ProjectBelow = 3
        ProjectLeft = 4
    

    class LabelOnParentType(enum.Enum):
        ParentViewLabelNoDisplay = 0
        ParentViewLabelBoundary = 1
        ParentViewLabelCircle = 1
        ParentViewLabelNote = 2
        ParentViewLabelLabel = 3
        ParentViewLabelEmbedded = 4
        ParentViewLabelTrueBoundary = 5
    

    class HiddenLine(enum.Enum):
        HiddenLineRemovalOff = 0
        HiddenLineRemovalOn = 1
    

    class UFDrawHalfSxsegs():
        bend_object: typing.List[UF.UFDrf.Object]
        cut_object: typing.List[UF.UFDrf.Object]
        arrow_object: typing.List[UF.UFDrf.Object]
    

    class Gap(enum.Enum):
        GapOff = 0
        GapOn = 1
    

    class ExtractedEdges(enum.Enum):
        ExtractedEdgesOff = 0
        ExtractedEdgesOn = 1
    

    class EdgeHidingEdge(enum.Enum):
        EdgeHidingEdgeOff = 0
        EdgeHidingEdgeOn = 1
    

    class DraftingCurveType(enum.Enum):
        UnknownType = -1
        ExtractedEdgeType = 1
        SilhouetteCurveType = 2
        ThreadSilhouetteCurveType = 3
        SectionEdgeType = 4
        ThreadSectionEdgeType = 5
        ViCurveType = 6
        UvhatchCurveType = 7
        TraceLineType = 8
        SimplifiedCurveType = 9
        InterferenceCurveType = 10
        ExtractedModelCurveType = 11
        ExtractedModelPointType = 12
    

    class UFDrawDefineBoundary():
        curve_tag: Tag
    

    class CompSectionInView(enum.Enum):
        NonSectioned = 0
        Sectioned = 1
        NotViewSpecified = 2
    

    class UFDrawBreakRegionData():
        view_tag: Tag
        position_type: UF.UFDraw.BreakPositionType
        distance: float
        reference_regions: typing.List[Tag]
        alignment_vectors: typing.List[Tag]
    

    class UFDrawBreakRegionBoundary():
        curve_tag: Tag
        construction_curve: bool
        hatch_curve: bool
    

    class BreakPositionType(enum.Enum):
        BreakPositionInferred = 0
        BreakPositionDistance = 1
        BreakPositionTwoRegions = 2
        BreakPositionDefault = 3
    

    class UFDrawBreakoutData():
        base_point: Tag
        extrusion_vector: Tag
        num_curves: int
        curves: typing.List[Tag]
        const_status: bool
        cut_thru_model: bool
        hidden_line_hatching: bool
    

    class BoundaryType(enum.Enum):
        BreakDetailType = 1
        ManualRectangleType = 2
        AutomaticRectangleType = 3
        BoundByObjectsType = 4
    

    class ArwHeadType(enum.Enum):
        AnsiArrow = 1
        IsoArrow = 2
        Iso128 = 3
        Jis = 4
        Gb = 5
    

    class ArwHeadCntl(enum.Enum):
        ClosedArrowhead = 1
        OpenArrowhead = 2
        FilledArrowhead = 3
    

    class UFDrawArrowParms():
        size: float
        total_length: float
        incl_angle: float
        past_part_dist: float
        stub_len: float
        head_type: UF.UFDraw.ArwHeadType
        head_control: UF.UFDraw.ArwHeadCntl
    

class UFDpud(Utilities.NXRemotableObject):
    def AskDpud(self, exit_id: int, dpud_id: int) -> None:
        ...
    def AskDrpos0(self, dpud: int, drpos: int) -> None:
        ...
    def AskDrpos1(self, dpud: int, drpos: int) -> None:
        ...
    def AskDrpos2(self, dpud: int, drpos: int) -> None:
        ...
    def AskOper(self, dpud: int, oper: int) -> None:
        ...
    def AskProjOption(self, dpud: int, proj_option: UF.UFDpud.ProjOption) -> None:
        ...
    def AskProjVec(self, dpud: int, proj_vec: float) -> None:
        ...
    def AskPurpose(self, dpud: int, purpose: UF.UFDpud.Purpose) -> None:
        ...
    def AskRatio(self, dpud: int, ratio: float) -> None:
        ...
    def AskTaxisOption(self, dpud: int, taxis_option: UF.UFDpud.TaxisOption) -> None:
        ...
    def AskToolAxis(self, dpud: int, tool_axis: float) -> None:
        ...
    def SetUserDataSize(self, dpud: int, size: int) -> None:
        ...


    class TaxisOption(enum.Enum):
        TaxisConstant = 0
        TaxisVariable = 1
        TaxisUserDefined = 2
    

    class Purpose(enum.Enum):
        UserParams = 0
        TaxisParams = 1
        ProjParams = 2
        InitProcessor = 3
        GetUserDataSize = 4
        GetNext = 5
        GetIntermediate = 6
        Rewind = 7
        StopProcessor = 8
    

    class ProjOption(enum.Enum):
        ProjConstant = 0
        ProjVariable = 1
        ProjUserDefined = 2
    

class UFDisp(Utilities.NXRemotableObject):
    def ActivateGrid(self, product_context: UF.UFDisp.GridContext) -> None:
        ...
    def AddItemToDisplay(self, object_id: Tag) -> None:
        ...
    def AskClosestColor(self, clr_model: int, clr_values: float, clr_cmp_mtd: int, clr_num: int) -> None:
        ...
    def AskClosestColorInDisplayedPart(self, color_name: UF.UFDisp.ColorName, color_index: int) -> None:
        ...
    def AskClosestColorInPart(self, object_in_part: Tag, color_name: UF.UFDisp.ColorName, color_index: int) -> None:
        ...
    def AskColor(self, clr_num: int, clr_model: int, clr_name: str, clr_values: float) -> None:
        ...
    def AskColorCount(self, count: int) -> None:
        ...
    def AskCurrentGridContext(self) -> UF.UFDisp.GridContext:
        ...
    def AskCurrentlySelectedMaterial(self, material_source: UF.UFDisp.MaterialSource, material_tag: Tag, material_full_archive_name: str) -> None:
        ...
    def AskDecals(self, object_tag: Tag, num_decals: int, decal_materials: typing.List[Tag]) -> None:
        ...
    def AskDisplay(self, display_code: int) -> None:
        ...
    def AskDisplayContext(self, context: int, inquiry: UF.UFDisp.Inquire) -> None:
        ...
    def AskDrawingDisplay(self, drawing_display: UF.UFDisp.DrawingDisplayData) -> None:
        ...
    def AskGeometryOfMaterial(self, material_tag: Tag, object_count: int, object_tags: typing.List[Tag]) -> None:
        ...
    def AskGridParameters(self, product_context: UF.UFDisp.GridContext, output_grid: UF.UFDisp.Grid) -> None:
        ...
    def AskLibraryMaterialLwaUserAreaData(self, material_full_archive_name: str, attribute_string_key: str, attribute_data: str) -> None:
        ...
    def AskMaterial(self, object_tag: Tag, material_tag: Tag, material_name: str) -> None:
        ...
    def AskMaterialsInPart(self, part_tag: Tag, material_format_type: UF.UFDisp.MaterialFormatType, material_count: int, material_tags: typing.List[Tag], material_names: str) -> None:
        ...
    def AskModelBounds(self, model_bounds_obj: Tag, model_bounds: float) -> None:
        ...
    def AskModelBoundsTag(self, model_bounds_object: Tag) -> None:
        ...
    def AskNameDisplayStatus(self, current_status: int) -> None:
        ...
    def AskNameViewStatus(self, current_status: int) -> None:
        ...
    def AskSrfanlParams(self, _params: UF.UFDisp.SrfanlData) -> None:
        ...
    def AskSystemParameters(self, system_parameters: UF.UFDisp.SystemParams) -> None:
        ...
    def AskTextureSpaceInfo(self, material_tag: Tag, ts_info_ptr: UF.UFDisp.TextureSpaceInfo, ts_info_defined: int) -> None:
        ...
    def AskWorkPartMaterialLwaUserAreaData(self, material_tag: Tag, attribute_string_key: str, attribute_data: str) -> None:
        ...
    def AskWorkPlaneDimClr(self, color: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskWorkPlaneEmphasis(self, emphasis: int) -> None:
        ...
    def AskWorkPlaneSel(self, _override: int) -> None:
        ...
    def AssignMaterial(self, material_tag: Tag, object_tag: Tag) -> None:
        ...
    def BatchShade(self, filename: str, x_size: int, y_size: int, method: UF.UFDisp.ShadeMethod) -> None:
        ...
    def BatchShadeOptions(self, filename: str, x_size: int, y_size: int, method: UF.UFDisp.ShadeMethod, options: UF.UFDisp.ShadeOptions) -> None:
        ...
    def ComputeModelBounds(self, bounds_computed: bool, model_bounds: float) -> None:
        ...
    def Conehead(self, display_flag: int, coord: float, vector: float, anchor_flag: int) -> None:
        ...
    def CopyLwaArchiveMaterialToWorkPart(self, material_name: str, material_tag: Tag) -> None:
        ...
    def CopyMaterial(self, material_tag: Tag, new_material_tag: Tag, new_material_name: str) -> None:
        ...
    def CreateAnimation(self, filename: str, animation_name: str, first_frame: int, last_frame: int) -> None:
        ...
    def CreateFramedImage(self, filename: str, format: UF.UFDisp.ImageFormat, color: UF.UFDisp.BackgroundColor, upper_left_corner: int, width: int, height: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateImage(self, filename: str, format: UF.UFDisp.ImageFormat, color: UF.UFDisp.BackgroundColor) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateMaterial(self, studio_system_material_name: str, new_material_tag: Tag, new_material_name: str) -> None:
        ...
    def DeactivateGrid(self, product_context: UF.UFDisp.GridContext, restore_prev_context_grid: bool) -> None:
        ...
    def DeleteMaterial(self, material_tag: Tag) -> None:
        ...
    def DisplayArc(self, matrix: float, start_angle: float, end_angle: float, arc_center: float, radius: float, context: int) -> None:
        ...
    def DisplayCircle(self, matrix: float, circle_center: float, radius: float, filled: bool, context: int) -> None:
        ...
    def DisplayOgpArc(self, view_tag: Tag, orientation: float, start_angle: float, end_angle: float, center: float, radius: float) -> None:
        ...
    def DisplayOgpCircle(self, view_tag: Tag, orientation: float, center: float, radius: float) -> None:
        ...
    def DisplayOgpLine(self, view_tag: Tag, pos1: float, pos2: float) -> None:
        ...
    def DisplayOgpPolyline(self, view_tag: Tag, pos_array: float, pos_count: int) -> None:
        ...
    def DisplayPoints(self, points: float, num_points: int, marker_type: UF.UFDisp.PolyMarker, context: int) -> None:
        ...
    def DisplayPolygon(self, points: float, num_points: int, filled: bool, context: int) -> None:
        ...
    def DisplayPolyline(self, poly_points: float, num_points: int, context: int) -> None:
        ...
    def DisplayRpoDimensions(self, feature_tag: Tag, exp_count: int, exp_tags: typing.List[Tag], view_option: int, color_option: int, color: int) -> None:
        ...
    def DisplaySketDimensions(self, sketch_tag: Tag, exp_count: int, exp_tags: typing.List[Tag], view_option: int, color_option: int, color: int) -> None:
        ...
    def DisplayTemporaryArc(self, view_tag: Tag, which_views: UF.UFDisp.ViewType, matrix: float, start_angle: float, end_angle: float, arc_center: float, radius: float, attrib: UF.UFObj.DispProps) -> None:
        ...
    def DisplayTemporaryLine(self, view_tag: Tag, which_views: UF.UFDisp.ViewType, start_line: float, end_line: float, attrib: UF.UFObj.DispProps) -> None:
        ...
    def DisplayTemporaryPoint(self, view_tag: Tag, which_views: UF.UFDisp.ViewType, markerpos: float, color: UF.UFObj.DispProps, marker_type: UF.UFDisp.PolyMarker) -> None:
        ...
    def DisplayTemporaryText(self, view_tag: Tag, which_views: UF.UFDisp.ViewType, text: str, text_coord: float, ref_point: UF.UFDisp.TextRef, color: UF.UFObj.DispProps, char_size: float, hardware: int) -> None:
        ...
    def DisplayText(self, text: str, text_coord: float, ref_point: UF.UFDisp.TextRef, context: int) -> None:
        ...
    def ExportWindowsMetafile(self, output_type: UF.UFDisp.WmfOutput, file_spec: str) -> None:
        ...
    def FreeTempFacetData(self) -> None:
        ...
    def GenerateTextureCoordinates(self, ts_info: UF.UFDisp.TextureSpaceInfo, face_facet_data: UF.UFDisp.FaceFacetData, texture_coords: float) -> None:
        ...
    def GetConeheadAttrb(self, attributes: UF.UFDisp.ConeheadAttrbSTag) -> None:
        ...
    def GetFacetData(self, object_tag: Tag, num_faces: int, face_facet_data: typing.List[UF.UFDisp.FaceFacetData]) -> None:
        ...
    def J3dGeometry(self, wireframe: int, num_entities: int, entity_list: typing.List[UF.UFDisp.J3dEntity]) -> None:
        ...
    def LabeledConehead(self, display_flag: int, coord: float, vector: float, anchor_flag: int, label: str) -> None:
        ...
    def LoadColorTable(self) -> None:
        ...
    def MakeDisplayUpToDate(self) -> None:
        ...
    def OpenLwaArchiveMaterialsLibrary(self, lwa_archive_library_name: str) -> None:
        ...
    def PrintWindowUgImage(self, format: int, color_usage: int) -> None:
        ...
    def Refresh(self) -> None:
        ...
    def RegenerateDisplay(self) -> None:
        ...
    def RegenerateView(self, view_tag: Tag) -> None:
        ...
    def RemoveMaterialAssignment(self, object_tag: Tag) -> None:
        ...
    def ResetConeheadAttrb(self) -> None:
        ...
    def SetColor(self, clr_num: int, clr_model: int, clr_name: str, clr_values: float) -> None:
        ...
    def SetConeheadAttrb(self, attributes: UF.UFDisp.ConeheadAttrbSTag) -> None:
        ...
    def SetDisplay(self, display_code: int) -> None:
        ...
    def SetDrawingDisplay(self, drawing_display: UF.UFDisp.DrawingDisplayData) -> None:
        ...
    def SetGridParameters(self, product_context: UF.UFDisp.GridContext, input_grid: UF.UFDisp.Grid) -> None:
        ...
    def SetHighlight(self, object_id: Tag, action_switch: int) -> None:
        ...
    def SetHighlights(self, object_count: int, object_list: typing.List[Tag], action_switch: int) -> None:
        ...
    def SetModelBounds(self, model_bounds_object: Tag, model_bounds: float) -> None:
        ...
    def SetNameDisplayStatus(self, new_status: int) -> None:
        ...
    def SetNameViewStatus(self, new_status: int) -> None:
        ...
    def SetSrfanlParams(self, _params: UF.UFDisp.SrfanlData) -> None:
        ...
    def SetSystemParameters(self, system_parameters: UF.UFDisp.SystemParams) -> None:
        ...
    def SetTextureSpaceInfo(self, material_tag: Tag, ts_info_ptr: UF.UFDisp.TextureSpaceInfo) -> None:
        ...
    def SetWorkPlaneDimClr(self, dim_color: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetWorkPlaneEmphasis(self, emphasis: int) -> None:
        ...
    def SetWorkPlaneSel(self, _override: int) -> None:
        ...
    def UpdateMaterialDisplayOfGeometry(self, object_count: int, object_list: typing.List[Tag]) -> None:
        ...


    class WmfOutput(enum.Enum):
        WmfToClipboard = 0
        WmfToFile = 1
    

    class ViewType(enum.Enum):
        UseViewTag = 0
        UseActivePlus = 1
        UseCursor = 2
        UseActiveMinus = 3
        UseWorkView = 4
    

    class TextureSpaceType(enum.Enum):
        ArbitraryPlaneTextureSpace = 0
        CylindricalTextureSpace = 1
        SphericalTextureSpace = 2
        AutoaxisTextureSpace = 3
        UvTextureSpace = 4
        UseCameraDirectionPlaneTextureSpace = 5
    

    class UFDispTextureSpaceInfo():
        type: UF.UFDisp.TextureSpaceType
        ts_scale: float
        ts_scale1: float
        aspect_ratio: float
        origin: float
        normal_vector: float
        up_vector: float
        center_point: float
        camera_direction_plane_option: int
    

    class TextRef(enum.Enum):
        Topleft = 1
        Topcenter = 2
        Topright = 3
        Middleleft = 4
        Middlecenter = 5
        Middleright = 6
        Bottomleft = 7
        Bottomcenter = 8
        Bottomright = 9
        Systemdefault = 0
    

    class UFDispSystemParams():
        tolerance: float
        dash_size: float
        space_size: float
        symbol_size: float
        facet_edge_tol: float
        facet_chord_tol: float
        facet_angle_tol: float
        color: int
        preselection_color: int
        handle_color: int
        font: int
        view_display: int
        line_width_display: int
        show_shaded_face_edges: bool
        use_face_edges_color: bool
        face_edges_color: int
        hidden_shaded_face_edges: int
        hidden_geometry_color: int
        random_color_displayed: bool
        random_color_object_type: int
    

    class UFDispSrfanlData():
        spike_length: float
        ref_plane: float
        ref_vector: float
        mid_value: float
        scale_factor: float
        anal_facet_edge_tol: float
        anal_facet_chord_tol: float
        anal_facet_angle_tol: float
        anal_facet_width_tol: float
        surf_anal_data: int
        surf_anal_fineness: int
        refl_type: int
        num_refl_lines: int
        refl_horiz_vert: int
        thick_refl_lines: int
        reflectivity: int
        refl_move_type: int
        refl_move_position: int
        refl_smooth_lines: int
        refl_user_image_filename: str
        num_contours: int
        surf_anal_display: int
        legend_color_type_gaussian: int
        legend_color_num_gaussian: int
        surf_anal_display_mean: int
        mid_value_mean: float
        scale_factor_mean: float
        legend_color_type_mean: int
        legend_color_num_mean: int
        surf_anal_display_max: int
        mid_value_max: float
        scale_factor_max: float
        legend_color_type_max: int
        legend_color_num_max: int
        surf_anal_display_min: int
        mid_value_min: float
        scale_factor_min: float
        legend_color_type_min: int
        legend_color_num_min: int
        surf_anal_display_normal: int
        mid_value_normal: float
        scale_factor_normal: float
        legend_color_type_normal: int
        legend_color_num_normal: int
        surf_anal_display_sec: int
        mid_value_sec: float
        scale_factor_sec: float
        legend_color_type_sec: int
        legend_color_num_sec: int
        surf_anal_display_u: int
        mid_value_u: float
        scale_factor_u: float
        legend_color_type_u: int
        legend_color_num_u: int
        surf_anal_display_v: int
        mid_value_v: float
        scale_factor_v: float
        legend_color_type_v: int
        legend_color_num_v: int
        surf_anal_display_slope: int
        mid_value_slope: float
        scale_factor_slope: float
        legend_color_type_slope: int
        legend_color_num_slope: int
        surf_anal_display_distance: int
        mid_value_distance: float
        scale_factor_distance: float
        legend_color_type_distance: int
        legend_color_num_distance: int
        surf_anal_display_refl: int
    

    class ShadePlot(enum.Enum):
        PlotFine = 0
        PlotMedium = 1
        PlotRough = 2
        PlotCoarse = 3
    

    class UFDispShadeOptions():
        format: UF.UFDisp.ShadeFormat
        display: UF.UFDisp.ShadeDisplay
        resolution: int
        plot_quality: UF.UFDisp.ShadePlot
        generate_shadows: bool
        facet_quality: float
        transparent_shadows: bool
        disable_raytracing: bool
        fixed_camera_viewing: bool
        super_sample: int
        subdivision_depth: int
        raytrace_memory: int
        radiosity_quality: int
        distribute_excess_light: bool
        use_midpoint_sampling: bool
    

    class ShadeMethod(enum.Enum):
        Flat = 0
        Gouraud = 1
        Phong = 2
        HighQuality = 3
        Preview = 4
        PhotoReal = 5
        Raytrace = 6
    

    class ShadeFormat(enum.Enum):
        FormatRaster = 0
        FormatQtvrPanorama = 1
        FormatQtvrObjectLow = 2
        FormatQtvrObjectHigh = 3
    

    class ShadeDisplay(enum.Enum):
        DisplayRgbPlusNoise = 0
        DisplayFsRgb = 1
        DisplayFsRgbPlusNoise = 2
        DisplayMonochrome = 3
        DisplayGrayScale = 4
        DisplayNearestRgb = 5
        DisplayOrderedDither = 6
        DisplayTcPlusNoise = 7
    

    class PolyMarker(enum.Enum):
        NoMarker = 0
        Point = 1
        Dot = 2
        Asterisk = 3
        Circle = 4
        Poundsign = 5
        X = 6
        Gridpoint = 7
        Square = 8
        TriangleMarker = 9
        Diamond = 10
        Centerline = 11
        ConsFix = 12
        ConsHorizontal = 13
        ConsVertical = 14
        ConsParallel = 15
        ConsPerpendicular = 16
        ConsTangent = 17
        ConsConcentric = 18
        ConsCoincident = 19
        ConsCollinear = 20
        ConsPointOnCurve = 21
        ConsMidpoint = 22
        ConsEqualLength = 23
        ConsEqualRadius = 24
        ConsConstantLength = 25
        ConsConstantAngle = 26
        ConsMirror = 27
        DimRadius = 28
        DimDiameter = 29
        DimParallel = 30
        DimPerpendicular = 31
        ConsSlope = 32
        ConsString = 33
        ConsUniformScaled = 34
        ConsNonUniformScaled = 35
        ConsAssocTrim = 36
        ConsAssocOffset = 37
        _2T_RES_SPOT_WELD = 38
        _3T_RES_SPOT_WELD = 39
        _4T_RES_SPOT_WELD = 40
        _2T_DC_SPOT_WELD = 41
        _3T_DC_SPOT_WELD = 42
        _4T_DC_SPOT_WELD = 43
        _2T_KPC_SPOT_WELD = 44
        _3T_KPC_SPOT_WELD = 45
        _4T_KPC_SPOT_WELD = 46
        _2T_PROC_SPOT_WELD = 47
        _3T_PROC_SPOT_WELD = 48
        _4T_PROC_SPOT_WELD = 49
        ArcSpotWeld = 50
        ClinchWeld = 51
        Anchor = 52
        LeftLeaderConnection = 53
        RightLeaderConnection = 54
        FilledCircle = 55
        FilledSquare = 56
        LargeFilledSquare = 57
        DatumPoint = 58
        SnappingDiamond = 59
        CircleInCircle = 60
        CircleInSquare = 61
        SquareInSquare = 62
        FilledLeftTriangle = 63
        FilledRightTriangle = 64
        FilledUpTriangle = 65
        FilledDownTriangle = 66
        FilledLeftTriangleInCircle = 67
        FilledRightTriangleInCircle = 68
        FilledUpTriangleInCircle = 69
        FilledDownTriangleInCircle = 70
        FilledLeftTriangleInSquare = 71
        FilledRightTriangleInSquare = 72
        FilledUpTriangleInSquare = 73
        FilledDownTriangleinSquare = 74
        RoundedCross = 75
        FilledDiamond = 76
        UpDownTriangles = 77
        LeftRightTriangles = 78
        SmallWheel = 79
        LargeWheel = 80
        HollowCircle = 81
        PreviewPerpendicular = 82
        PreviewHorizontal = 83
        PreviewVertical = 84
        PreviewTangent = 85
        PreviewParallel = 86
        PreviewPointOnCurve = 87
        PreviewCollinear = 88
        Ruler = 89
        Protractor = 90
        SketchNotebook = 91
        ArcEndPoint = 92
        _2_PT_ARC_MARKER = 93
        BigAsterisk = 94
        LineInCircle = 95
        PlusInCircle = 96
        CenterOfRotation = 97
        PreviewX = 98
        PreviewY = 99
        PreviewZ = 100
        _2T_GENERAL_SPOT_WELD = 101
        _3T_GENERAL_SPOT_WELD = 102
        _4T_GENERAL_SPOT_WELD = 103
        _2T_VITAL_SPOT_WELD = 104
        _3T_VITAL_SPOT_WELD = 105
        _4T_VITAL_SPOT_WELD = 106
        _2T_IMPORTANT_SPOT_WELD = 107
        _3T_IMPORTANT_SPOT_WELD = 108
        _4T_IMPORTANT_SPOT_WELD = 109
        _2T_SEMIPANEL_SPOT_WELD = 110
        _3T_SEMIPANEL_SPOT_WELD = 111
        _4T_SEMIPANEL_SPOT_WELD = 112
        SpotWeldNut = 113
        SpotWeldStud = 114
        _2T_CLINCH_PUNCH = 115
        _2T_CLINCH_BUTTON = 116
        _2T_BRACKET = 117
        _2T_POP_RIVET = 118
        _3T_POP_RIVET = 119
        _4T_POP_RIVET = 120
        _2T_SELF_PIERCE_RIVET_HEAD_SIDE = 121
        _3T_SELF_PIERCE_RIVET_HEAD_SIDE = 122
        _4T_SELF_PIERCE_RIVET_HEAD_SIDE = 123
        _2T_SELF_PIERCE_RIVET_HEAD_SIDE_CONTROL_DELTA = 124
        _3T_SELF_PIERCE_RIVET_HEAD_SIDE_CONTROL_DELTA = 125
        _4T_SELF_PIERCE_RIVET_HEAD_SIDE_CONTROL_DELTA = 126
        _2T_SELF_PIERCE_RIVET_BUTTON_SIDE = 127
        _3T_SELF_PIERCE_RIVET_BUTTON_SIDE = 128
        _4T_SELF_PIERCE_RIVET_BUTTON_SIDE = 129
        _2T_SELF_PIERCE_RIVET_BUTTON_SIDE_CONTROL_DELTA = 130
        _3T_SELF_PIERCE_RIVET_BUTTON_SIDE_CONTROL_DELTA = 131
        _4T_SELF_PIERCE_RIVET_BUTTON_SIDE_CONTROL_DELTA = 132
        _2T_FLOW_DRILL_SCREWS_HEAD_SIDE = 133
        _3T_FLOW_DRILL_SCREWS_HEAD_SIDE = 134
        _4T_FLOW_DRILL_SCREWS_HEAD_SIDE = 135
        _2T_FLOW_DRILL_SCREWS_HEAD_SIDE_CONTROL_DELTA = 136
        _3T_FLOW_DRILL_SCREWS_HEAD_SIDE_CONTROL_DELTA = 137
        _4T_FLOW_DRILL_SCREWS_HEAD_SIDE_CONTROL_DELTA = 138
        _2T_FLOW_DRILL_SCREWS_BUTTON_SIDE = 139
        _3T_FLOW_DRILL_SCREWS_BUTTON_SIDE = 140
        _4T_FLOW_DRILL_SCREWS_BUTTON_SIDE = 141
        _2T_FLOW_DRILL_SCREWS_BUTTON_SIDE_CONTROL_DELTA = 142
        _3T_FLOW_DRILL_SCREWS_BUTTON_SIDE_CONTROL_DELTA = 143
        _4T_FLOW_DRILL_SCREWS_BUTTON_SIDE_CONTROL_DELTA = 144
        CenterGravityMeasurement = 145
        InvalidMarker = 146
    

    class MaterialSource(enum.Enum):
        LwMaterialInMaterialsLibrary = 0
        LwMaterialInMaterialsInPartPalette = 1
    

    class MaterialFormatType(enum.Enum):
        ShAuthor = 0
        ShIrayplus = 1
        ShMax = 2
    

    class UFDispJ3dEntity():
        eid: Tag
        vectors: int
        has_transform: int
        transform: float
        point_list: float
        normal_list: float
        points_per_strip: int
        num_strips: int
        total_points: int
        sheet: int
        color: float
        name: str
    

    class UFDispInquire():
        context_running: UF.UFDisp.Context
        is_view_mode_valid: bool
        view_mode: int
        is_atten_pt_valid: bool
        atten_pt: float
        is_draw_open_disp: bool
        view_tag: Tag
    

    class ImageFormat(enum.Enum):
        Png = 0
        Jpeg = 1
        Tiff = 2
        CompressedTiff = 3
        Gif = 4
        Xwd = 5
        Bmp = 6
    

    class GridType(enum.Enum):
        PolarGrid = 0
        RectangularGrid = 1
    

    class GridContext(enum.Enum):
        SketchGrid = 0
        DrawingGrid = 1
        ModelGrid = 2
        ShedGrid = 3
        NullGrid = 4
    

    class UFDispGrid():
        show_grid: bool
        show_labels: bool
        snap_to_grid: bool
        grid_color: int
        grid_type: UF.UFDisp.GridType
        grid_non_uniform: bool
        grid_on_top: bool
        rectangular_grid_emphasis: bool
        grid_unit_x: float
        grid_unit_y: float
        grid_line_every_x: int
        grid_line_every_y: int
        grid_emphasis_every_x: int
        grid_emphasis_every_y: int
        polar_grid_emphasis: bool
        grid_angular_unit: float
        grid_angular_line_every: int
        grid_angular_emphasis_every: int
        grid_radial_unit: float
        grid_radial_circle_every: int
        grid_radial_emphasis_every: int
    

    class FacetType(enum.Enum):
        Triangle = 0
        Polygon = 1
        Tristrip = 2
    

    class UFDispFacet():
        vertices: float
        normals: float
    

    class UFDispFaceFacetData():
        face_tag: Tag
        uvs_available: bool
        num_vertices: int
        num_facets: int
        num_vertex_per_facet: int
        vertex_indices: int
        coords: float
        normals: float
        uvs: float
    

    class UFDispDrawingDisplayData():
        monochrome_display: bool
        system_color: int
        preselection_color: int
        foreground_color: int
        background_color: int
        show_widths: bool
    

    class Context(enum.Enum):
        Display = 0
        Fit = 1
        SelectSing = 2
        SelectBox = 3
        Atten = 4
        ScreenSizeFit = 5
    

    class UFDispConeheadAttrbSTag():
        staff_length: float
        total_length: float
        cone_radius: float
        color: int
        font: int
        density: int
    

    class ColorName(enum.Enum):
        PaleWeakYellowName = 0
        PaleDullYellowName = 1
        LightFadedYellowName = 2
        LightHardYellowName = 3
        PaleWeakCyanName = 4
        PaleWeakGreenName = 5
        PaleDullSpringName = 6
        LightSpringYellowName = 7
        LightYellowSpringName = 8
        YellowYellowSpringName = 9
        PaleDullCyanName = 10
        PaleDullTealName = 11
        PaleDullGreenName = 12
        LightSpringGreenName = 13
        LightHardSpringName = 14
        SpringSpringYellowName = 15
        LightFadedCyanName = 16
        LightTealCyanName = 17
        LightTealGreenName = 18
        LightFadedGreenName = 19
        LightGreenSpringName = 20
        SpringSpringGreenName = 21
        LightHardCyanName = 22
        LightCyanTealName = 23
        LightHardTealName = 24
        LightGreenTealName = 25
        LightHardGreenName = 26
        GreenGreenSpringName = 27
        CyanCyanTealName = 28
        TealTealCyanName = 29
        TealTealGreenName = 30
        GreenGreenTealName = 31
        PaleWeakMagentaName = 32
        PaleWeakRedName = 33
        PaleDullOrangeName = 34
        LightOrangeYellowName = 35
        LightYellowOrangeName = 36
        YellowYellowOrangeName = 37
        PaleWeakBlueName = 38
        PaleGrayName = 39
        LightWeakYellowName = 40
        LightDullYellowName = 41
        MediumFadedYellowName = 42
        DarkHardYellowName = 43
        PaleDullAzureName = 44
        LightWeakCyanName = 45
        LightWeakGreenName = 46
        LightDullSpringName = 47
        MediumSpringYellowName = 48
        DarkYellowSpringName = 49
        LightAzureCyanName = 50
        LightDullCyanName = 51
        LightDullTealName = 52
        LightDullGreenName = 53
        MediumSpringGreenName = 54
        DarkHardSpringName = 55
        LightCyanAzureName = 56
        MediumFadedCyanName = 57
        MediumTealCyanName = 58
        MediumTealGreenName = 59
        MediumFadedGreenName = 60
        DarkGreenSpringName = 61
        CyanCyanAzureName = 62
        DarkHardCyanName = 63
        DarkCyanTealName = 64
        DarkHardTealName = 65
        DarkGreenTealName = 66
        DarkHardGreenName = 67
        PaleDullMagentaName = 68
        PaleDullPinkName = 69
        PaleDullRedName = 70
        LightOrangeRedName = 71
        LightHardOrangeName = 72
        OrangeOrangeYellowName = 73
        PaleDullVioletName = 74
        LightWeakMagentaName = 75
        LightWeakRedName = 76
        LightDullOrangeName = 77
        MediumOrangeYellowName = 78
        DarkYellowOrangeName = 79
        PaleDullBlueName = 80
        LightWeakBlueName = 81
        MediumWeakYellowName = 82
        DarkDullYellowName = 83
        DarkFadedYellowName = 84
        LightAzureBlueName = 85
        LightDullAzureName = 86
        MediumWeakCyanName = 87
        MediumWeakGreenName = 88
        DarkDullSpringName = 89
        DarkSpringYellowName = 90
        LightHardAzureName = 91
        MediumAzureCyanName = 92
        DarkDullCyanName = 93
        DarkDullTealName = 94
        DarkDullGreenName = 95
        DarkSpringGreenName = 96
        AzureAzureCyanName = 97
        DarkCyanAzureName = 98
        DarkFadedCyanName = 99
        DarkTealCyanName = 100
        DarkTealGreenName = 101
        DarkFadedGreenName = 102
        LightFadedMagentaName = 103
        LightPinkMagentaName = 104
        LightPinkRedName = 105
        LightFadedRedName = 106
        LightRedOrangeName = 107
        OrangeOrangeRedName = 108
        LightVioletMagentaName = 109
        LightDullMagentaName = 110
        LightDullPinkName = 111
        LightDullRedName = 112
        MediumOrangeRedName = 113
        DarkHardOrangeName = 114
        LightVioletBlueName = 115
        LightDullVioletName = 116
        MediumWeakMagentaName = 117
        MediumWeakRedName = 118
        DarkDullOrangeName = 119
        DarkOrangeYellowName = 120
        LightFadedBlueName = 121
        LightDullBlueName = 122
        MediumWeakBlueName = 123
        DarkWeakYellowName = 124
        ObscureDullYellowName = 125
        LightBlueAzureName = 126
        MediumAzureBlueName = 127
        DarkDullAzureName = 128
        DarkWeakCyanName = 129
        DarkWeakGreenName = 130
        ObscureDullSpringName = 131
        AzureAzureBlueName = 132
        DarkHardAzureName = 133
        DarkAzureCyanName = 134
        ObscureDullCyanName = 135
        ObscureDullTealName = 136
        ObscureDullGreenName = 137
        LightHardMagentaName = 138
        LightMagentaPinkName = 139
        LightHardPinkName = 140
        LightRedPinkName = 141
        LightHardRedName = 142
        RedRedOrangeName = 143
        LightMagentaVioletName = 144
        MediumFadedMagentaName = 145
        MediumPinkMagentaName = 146
        MediumPinkRedName = 147
        MediumFadedRedName = 148
        DarkRedOrangeName = 149
        LightHardVioletName = 150
        MediumVioletMagentaName = 151
        DarkDullMagentaName = 152
        DarkDullPinkName = 153
        DarkDullRedName = 154
        DarkOrangeRedName = 155
        LightBlueVioletName = 156
        MediumVioletBlueName = 157
        DarkDullVioletName = 158
        DarkWeakMagentaName = 159
        DarkWeakRedName = 160
        ObscureDullOrangeName = 161
        LightHardBlueName = 162
        MediumFadedBlueName = 163
        DarkDullBlueName = 164
        DarkWeakBlueName = 165
        ObscureGrayName = 166
        ObscureWeakYellowName = 167
        BlueBlueAzureName = 168
        DarkBlueAzureName = 169
        DarkAzureBlueName = 170
        ObscureDullAzureName = 171
        ObscureWeakCyanName = 172
        ObscureWeakGreenName = 173
        MagentaMagentaPinkName = 174
        PinkPinkMagentaName = 175
        PinkPinkRedName = 176
        RedRedPinkName = 177
        MagentaMagentaVioletName = 178
        DarkHardMagentaName = 179
        DarkMagentaPinkName = 180
        DarkHardPinkName = 181
        DarkRedPinkName = 182
        DarkHardRedName = 183
        VioletVioletMagentaName = 184
        DarkMagentaVioletName = 185
        DarkFadedMagentaName = 186
        DarkPinkMagentaName = 187
        DarkPinkRedName = 188
        DarkFadedRedName = 189
        VioletVioletBlueName = 190
        DarkHardVioletName = 191
        DarkVioletMagentaName = 192
        ObscureDullMagentaName = 193
        ObscureDullPinkName = 194
        ObscureDullRedName = 195
        BlueBlueVioletName = 196
        DarkBlueVioletName = 197
        DarkVioletBlueName = 198
        ObscureDullVioletName = 199
        ObscureWeakMagentaName = 200
        ObscureWeakRedName = 201
        DarkHardBlueName = 202
        DarkFadedBlueName = 203
        ObscureDullBlueName = 204
        ObscureWeakBlueName = 205
        BlackName = 206
        CharcoalGrayName = 207
        DarkGrayName = 208
        IronGrayName = 209
        GraniteGrayName = 210
        MediumGrayName = 211
        SilverGrayName = 212
        SmokeGrayName = 213
        LightGrayName = 214
        AshGrayName = 215
        PowderGrayName = 216
        WhiteName = 217
        MagentaName = 218
        DeepMagentaName = 219
        StrongMagentaName = 220
        MediumMagentaName = 221
        PaleMagentaName = 222
        RedName = 223
        DeepRedName = 224
        StrongRedName = 225
        MediumRedName = 226
        PaleRedName = 227
        OrangeName = 228
        DeepOrangeName = 229
        StrongOrangeName = 230
        MediumOrangeName = 231
        PaleOrangeName = 232
        YellowName = 233
        DeepYellowName = 234
        StrongYellowName = 235
        MediumYellowName = 236
        PaleYellowName = 237
        LimeName = 238
        DeepLimeName = 239
        StrongLimeName = 240
        MediumLimeName = 241
        PaleLimeName = 242
        GreenName = 243
        DeepGreenName = 244
        StrongGreenName = 245
        MediumGreenName = 246
        PaleGreenName = 247
        EmeraldName = 248
        DeepEmeraldName = 249
        StrongEmeraldName = 250
        MediumEmeraldName = 251
        PaleEmeraldName = 252
        CyanName = 253
        DeepCyanName = 254
        StrongCyanName = 255
        MediumCyanName = 256
        PaleCyanName = 257
        CornflowerName = 258
        DeepCornflowerName = 259
        StrongCornflowerName = 260
        MediumCornflowerName = 261
        PaleCornflowerName = 262
        BlueName = 263
        DeepBlueName = 264
        StrongBlueName = 265
        MediumBlueName = 266
        PaleBlueName = 267
        CobaltName = 268
        DeepCobaltName = 269
        StrongCobaltName = 270
        MediumCobaltName = 271
        PaleCobaltName = 272
        PurpleName = 273
        DeepPurpleName = 274
        StrongPurpleName = 275
        MediumPurpleName = 276
        PalePurpleName = 277
        BrownName = 278
        DeepBrownName = 279
        StrongBrownName = 280
        MediumBrownName = 281
        PaleBrownName = 282
        DeepFuchsiaName = 283
        StrongFushciaName = 284
        MediumFuchsiaName = 285
        PaleFuchsiaName = 286
        DeepMaroonName = 287
        StrongMaroonName = 288
        MediumMaroonName = 289
        PaleMaroonName = 290
        DeepCoralName = 291
        StrongCoralName = 292
        MediumCoralName = 293
        PaleCoralName = 294
        DeepGoldName = 295
        StrongGoldName = 296
        MediumGoldName = 297
        PaleGoldName = 298
        DeepKhakiName = 299
        StrongKhakiName = 300
        MediumKhakiName = 301
        PaleKhakiName = 302
        DeepPineName = 303
        StrongPineName = 304
        MediumPineName = 305
        PalePineName = 306
        DeepSeaName = 307
        StrongSeaName = 308
        MediumSeaName = 309
        PaleSeaName = 310
        DeepTurquoiseName = 311
        StrongTurquoiseName = 312
        MediumTurquoiseName = 313
        PaleTorquoiseName = 314
        DeepSteelName = 315
        StrongSteelName = 316
        MediumSteelName = 317
        PaleSteelName = 318
        DeepMidnightName = 319
        StrongMidnightName = 320
        MediumMidnightName = 321
        PaleMidnightName = 322
        DeepIndigoName = 323
        StrongIndigoName = 324
        MediumIndigoName = 325
        PaleIndigoName = 326
        DeepStoneName = 327
        StrongStoneName = 328
        MediumStoneName = 329
        PaleStoneName = 330
        DeepPlumName = 331
        StrongPlumName = 332
        MediumPlumName = 333
        PalePlumName = 334
        DeepCrimsonName = 335
        StrongCrimsonName = 336
        MediumCrimsonName = 337
        PaleCrimsonName = 338
        DeepCarrotName = 339
        StrongCarrotName = 340
        MediumCarrotName = 341
        PaleCarrotName = 342
        DeepOliveName = 343
        StrongOliveName = 344
        MediumOliveName = 345
        PaleOliveName = 346
        DeepLeafName = 347
        StrongLeafName = 348
        MediumLeafName = 349
        PaleLeafName = 350
        DeepForestName = 351
        StrongForestName = 352
        MediumForestName = 353
        PaleForestName = 354
        DeepMossName = 355
        StrongMossName = 356
        MediumMossName = 357
        PaleMossName = 358
        DeepTealName = 359
        StrongTealName = 360
        MediumTealName = 361
        PaleTealName = 362
        DeepAzureName = 363
        StrongAzureName = 364
        MediumAzureName = 365
        PaleAzureName = 366
        DeepRoyalName = 367
        StrongRoyalName = 368
        MediumRoyalName = 369
        PaleRoyalName = 370
        DeepVioletName = 371
        StrongVioletName = 372
        MediumVioletName = 373
        PaleVioletName = 374
        DeepUmberName = 375
        StrongUmberName = 376
        MediumUmberName = 377
        PaleUmberName = 378
        DeepPinkName = 379
        StrongPinkName = 380
        MediumPinkName = 381
        PalePinkName = 382
        DeepSalmonName = 383
        StrongSalmonName = 384
        MediumSalmonName = 385
        PaleSalmonName = 386
        DeepPeachName = 387
        StrongPeachName = 388
        MediumPeachName = 389
        PalePeachName = 390
        DeepLemonName = 391
        StrongLemonName = 392
        MediumLemonName = 393
        PaleLemonName = 394
        DeepPistachioName = 395
        StrongPistachioName = 396
        MediumPistachioName = 397
        PalePistachioName = 398
        DeepSpringName = 399
        StrongSpringName = 400
        MediumSpringName = 401
        PaleSpringName = 402
        DeepMintName = 403
        StrongMintName = 404
        MediumMintName = 405
        PaleMintName = 406
        DeepAquaName = 407
        StrongAquaName = 408
        MediumAquaName = 409
        PaleAquaName = 410
        DeepSkyName = 411
        StrongSkyName = 412
        MediumSkyName = 413
        PaleSkyName = 414
        DeepIceName = 415
        StrongIceName = 416
        MediumIceName = 417
        PaleIceName = 418
        DeepLavenderName = 419
        StrongLavenderName = 420
        MediumLavenderName = 421
        PaleLavenderName = 422
        DeepTanName = 423
        StrongTanName = 424
        MediumTanName = 425
        PaleTanName = 426
        MaxColorName = 427
    

    class BackgroundColor(enum.Enum):
        Original = 0
        White = 1
        InvalidColor = 2
    

class UFDirpath(Utilities.NXRemotableObject):
    def Append(self, self: Tag, append: Tag) -> None:
        ...
    def AppendFromDirs(self, self: Tag, count: int, dirs: str) -> None:
        ...
    def AppendFromEnv(self, self: Tag, env: str) -> None:
        ...
    def AskCurrDir(self, self: Tag, dir: str) -> None:
        ...
    def AskDirCount(self, self: Tag) -> int:
        ...
    def AskDirIndex(self, self: Tag) -> int:
        ...
    def AskDirs(self, self: Tag, count: int, dirs: str) -> None:
        ...
    def AskNextDir(self, self: Tag, dir: str) -> None:
        ...
    def AskNthDir(self, self: Tag, index: int, dir: str) -> None:
        ...
    def AskPrevDir(self, self: Tag, dir: str) -> None:
        ...
    def CreateFromDirs(self, count: int, dirs: str, retval_tag: Tag) -> None:
        ...
    def CreateFromEnv(self, env: str, retval_tag: Tag) -> None:
        ...
    def FindFile(self, self: Tag, name: str, fpath: str) -> None:
        ...
    def StartDirIteration(self, self: Tag) -> None:
        ...


class UFDieeng(Utilities.NXRemotableObject):
    def CreateDolReportFile(self, report_file_name: str) -> None:
        ...


class UFDie(Utilities.NXRemotableObject):
    def AskDrawFaces(self, type_of_tool: int, num_faces: int, faces: typing.List[Tag]) -> None:
        ...
    def AskMaterialProperties(self, metal_thickness: float, material_type_tag: Tag) -> None:
        ...


class UFDbcMld(Utilities.NXRemotableObject):
    def AskDbcMld(self, exit_id: int, dbc_mld_id: int) -> None:
        ...
    def AskSheet(self, _object: int, sheet: int) -> None:
        ...
    def Create(self, _object: int) -> None:
        ...
    def Delete(self, _object: int) -> None:
        ...
    def ExecCommand(self, dbc_mld_id: int, command: str) -> None:
        ...
    def SetInterpResult(self, _object: int, result: str) -> None:
        ...
    def SetSheet(self, _object: int, sheet: int) -> None:
        ...


class UFCutter(Utilities.NXRemotableObject):
    def AskHolderData(self, object_tag: Tag, count: int, data: typing.List[UF.UFCutter.HolderSection]) -> None:
        ...
    def AskSectionCount(self, object_tag: Tag, count: int) -> None:
        ...
    def AskTrackingPointCount(self, object_tag: Tag, count: int) -> None:
        ...
    def AskTrackingPointData(self, object_tag: Tag, count: int, data: typing.List[UF.UFCutter.TrackingPointData]) -> None:
        ...
    def AskTurnTrackingPointData(self, object_tag: Tag, count: int, data: typing.List[UF.UFCutter.TurnTrackingPointData]) -> None:
        ...
    def AskTypeAndSubtype(self, object_id: Tag, type: int, subtype: int) -> None:
        ...
    def Create(self, type_name: str, subtype_name: str, new_object: Tag) -> None:
        ...
    def CreateHolderSection(self, object_tag: Tag, data: UF.UFCutter.HolderSection) -> None:
        ...
    def CreateTrackingPoint(self, object_tag: Tag, data: UF.UFCutter.TrackingPointData) -> None:
        ...
    def CreateTurnTrackingPoint(self, object_tag: Tag, data: UF.UFCutter.TurnTrackingPointData) -> None:
        ...
    def DeleteHolderSection(self, object_tag: Tag, index: int) -> None:
        ...
    def DeleteTrackingPoint(self, cutter_tag: Tag, index: int) -> None:
        ...
    def EditHolderSection(self, object_tag: Tag, index: int, data: UF.UFCutter.HolderSection) -> None:
        ...
    def Retrieve(self, libref: str, tool_tag: Tag) -> None:
        ...
    def SetTrackingPointData(self, object_tag: Tag, index: int, data: UF.UFCutter.TrackingPointData) -> None:
        ...
    def SetTurnTrackingPointData(self, object_tag: Tag, index: int, data: UF.UFCutter.TurnTrackingPointData) -> None:
        ...
    def UpdateFromLib(self, tool_tag: Tag) -> None:
        ...


    class UFCutterTurnTrackingPointData():
        tlangl: float
        radius: float
        xoff: float
        yoff: float
        adjust: int
        cutcom: int
        radiusid: int
        cluster: int
        name: str
    

    class UFCutterTrackingPointData():
        diameter: float
        distance: float
        zoff: float
        adjust: int
        cutcom: int
        zoff_status: int
        adjust_status: int
        cutcom_status: int
        name: str
    

    class UFCutterHolderSection():
        diameter: float
        length: float
        taper: float
        corner: float
    

class UFCutLevels(Utilities.NXRemotableObject):
    def AddLevelsUsingGeom(self, operation_tag: Tag, num_to_add: int, geom_tags: Tag, max_depth_per_cut: float, cut_levels: UF.UFCutLevels.CutLevelsStruct) -> None:
        ...
    def AddLevelsUsingZ(self, operation_tag: Tag, num_to_add: int, z_levels: float, max_depth_per_cut: float, cut_levels: UF.UFCutLevels.CutLevelsStruct) -> None:
        ...
    def AskLevel(self, cut_levels: UF.UFCutLevels.CutLevelsStruct, index: int, level_data_ptr_addr: typing.List[UF.CutLevelSingle]) -> None:
        ...
    def AskTopOffLevel(self, cut_levels: UF.UFCutLevels.CutLevelsStruct, index: int, level_data_ptr_addr: typing.List[UF.CutLevelSingle]) -> None:
        ...
    def DeleteLevel(self, operation_tag: Tag, delete_level: int, cut_levels: UF.UFCutLevels.CutLevelsStruct) -> None:
        ...
    def EditLevelUsingGeom(self, operation_tag: Tag, edit_level: int, geom_tag: Tag, max_depth_per_cut: float, cut_levels: UF.UFCutLevels.CutLevelsStruct) -> None:
        ...
    def EditLevelUsingZ(self, operation_tag: Tag, edit_level: int, z_level: float, max_depth_per_cut: float, cut_levels: UF.UFCutLevels.CutLevelsStruct) -> None:
        ...
    def Free(self, cut_levels_ptr_addr: typing.List[UF.UFCutLevels.CutLevelsStruct]) -> None:
        ...
    def Load(self, operation_tag: Tag, cut_levels_ptr_addr: typing.List[UF.UFCutLevels.CutLevelsStruct]) -> None:
        ...
    def ResetToDefault(self, operation_tag: Tag) -> None:
        ...
    def SetRangeType(self, operation_tag: Tag, range_type: UF.ParamClvRangeType, cut_levels: UF.UFCutLevels.CutLevelsStruct) -> None:
        ...


    class UFCutLevelsCutLevelsStruct():
        num_levels: int
        cut_levels: typing.List[UF.CutLevelSingle]
        num_top_off_levels: int
        top_off_levels: typing.List[UF.CutLevelSingle]
    

class UFCurveLineArc(Utilities.NXRemotableObject):
    def IsArcEqual(self, arc1: Tag, arc2: Tag) -> int:
        ...
    def IsLineEqual(self, line1: Tag, line2: Tag) -> int:
        ...


class UFCurve(Utilities.NXRemotableObject):
    def AddFacesOcfData(self, face_tag: Tag, uf_offset_data: UF.UFCurve.OcfData) -> None:
        ...
    def AddStringToOcfData(self, string_tag: Tag, offset_direction: int, num_offsets: int, offset_distances: typing.List[UF.UFCurve.OcfValues], uf_offset_data: UF.UFCurve.OcfData) -> None:
        ...
    def AskAnalysisDisplay(self, curve_tag: Tag, analysis_display_options: UF.UFCurve.AnalysisDisplay) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskArcData(self, arc: Tag, arc_coords: UF.UFCurve.Arc) -> None:
        ...
    def AskArcLength(self, curve_tag: Tag, start_param: float, end_param: float, unit_flag: UF.ModlUnits, arc_length: float) -> None:
        ...
    def AskBridgeFeature(self, bridge_feature: Tag, bridge_data: UF.UFCurve.BridgeData) -> None:
        ...
    def AskCentroid(self, curve_id: Tag, centroid: float) -> None:
        ...
    def AskCombineCurves(self, combine_curve_feature: Tag, first_curve_tag: Tag, first_dir: UF.UFCurve.CombineCurvesDirection, second_curve_tag: Tag, second_dir: UF.UFCurve.CombineCurvesDirection, tol: str, curve_list: typing.List[Tag]) -> None:
        ...
    def AskConicData(self, conic: Tag, conic_data: UF.UFCurve.Conic) -> None:
        ...
    def AskCurveFitData(self, curve_feature: Tag, curve_fit_data: UF.UFModl.CurveFitData) -> None:
        ...
    def AskCurveInflections(self, curve_eid: Tag, proj_matrx: float, range: float, num_infpts: int, inf_pts: float) -> None:
        ...
    def AskCurveStruct(self, curve_id: Tag, curve_struct: typing.List[UF.UFCurve.Struct]) -> None:
        ...
    def AskCurveStructData(self, curve_struct: UF.UFCurve.Struct, type: int, curve_data: float) -> None:
        ...
    def AskCurveTurnAngle(self, curve: Tag, orientation: float, angle: float) -> None:
        ...
    def AskFeatureCurves(self, curve_feature_id: Tag, num_curves: int, feature_curves: typing.List[Tag]) -> None:
        ...
    def AskIntCurveParents(self, int_curve: Tag, int_curve_object: Tag, input_objects: typing.List[Tag]) -> None:
        ...
    def AskIntCurves(self, int_curve_object: Tag, num_curves: int, intersection_curves: typing.List[Tag]) -> None:
        ...
    def AskIntParms(self, int_curve_object: Tag, num_objects_set_1: int, object_set_1: typing.List[Tag], num_objects_set_2: int, object_set_2: typing.List[Tag]) -> None:
        ...
    def AskIntParmsSc(self, int_curve_object: Tag, num_objects_set_1: int, object_set_1: typing.List[Tag], num_objects_set_2: int, object_set_2: typing.List[Tag], set1_is_collector: bool, set2_is_collector: bool) -> None:
        ...
    def AskIsocline(self, isocline_feat: Tag, face_cnt: int, faces: typing.List[Tag], direction: float, start_angle: str, end_angle: str, step_angle: str, curve_cnt: int, curves: typing.List[Tag]) -> None:
        ...
    def AskJoinedParms(self, joined_curve_feature: Tag, uf_curve_string: UF.StringList, creation_method: int, tols: float) -> None:
        ...
    def AskLineArcData(self, line_arc_feat_id: Tag, line_arc_data: UF.UFCurve.LineArc) -> None:
        ...
    def AskLineArcOutput(self, line_arc_feat_id: Tag, line_arc_id: Tag) -> None:
        ...
    def AskLineData(self, line: Tag, line_coords: UF.UFCurve.Line) -> None:
        ...
    def AskOcfData(self, feature: Tag, offset_data: typing.List[UF.UFCurve.OcfData]) -> None:
        ...
    def AskOffsetCurves(self, offset_curve_object: Tag, num_curves: int, offset_curves: typing.List[Tag]) -> None:
        ...
    def AskOffsetDirection(self, input_curves: UF.StringList, offset_direction_vector: float, draft_direction_vector: float, base_point: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskOffsetDirection2(self, input_curves: UF.StringList, offset_direction_vector: float, draft_direction_vector: float, base_point: float) -> None:
        ...
    def AskParameterization(self, _object: Tag, param_range: float, periodicity: int) -> None:
        ...
    def AskPointData(self, point: Tag, point_coords: float) -> None:
        ...
    def AskProjCurveParents(self, proj_curve: Tag, defining_feature: Tag, defining_target: Tag, defining_curve: Tag) -> None:
        ...
    def AskProjCurves(self, proj_curve_feature: Tag, n_curve_refs: int, curve_refs: typing.List[Tag]) -> None:
        ...
    def AskSplineData(self, spline_tag: Tag, spline_data: UF.UFCurve.Spline) -> None:
        ...
    def AskSplineFeature(self, feature_id: Tag, spline: Tag) -> None:
        ...
    def AskSplineSap(self, curve_tag: Tag, display_flag: int, scale_factor: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskSplineThruPts(self, spline_tag: Tag, degree: int, periodicity: int, num_points: int, point_data: typing.List[UF.UFCurve.PtSlopeCrvatr], parameters: float) -> None:
        ...
    def AskWrapCurveParents(self, curve_tag: Tag, defining_face: Tag, defining_plane: Tag, defining_curve: Tag, wrap_curve_object: Tag) -> None:
        ...
    def AskWrapCurves(self, wrap_curve_object: Tag, num_output_curves: int, output_curves: typing.List[Tag]) -> None:
        ...
    def AskWrapParms(self, wrap_curve_object: Tag, wrap_data: UF.UFCurve.WrapData) -> None:
        ...
    def AutoJoinCurves(self, crv_list: typing.List[Tag], crv_num: int, join_type: int, join_list: typing.List[Tag], join_num: int) -> None:
        ...
    def ConvertConicToGen(self, conic_data: UF.UFCurve.Conic, gen_conic_data: UF.UFCurve.Genconic) -> None:
        ...
    def ConvertConicToStd(self, gen_conic_data: UF.UFCurve.Genconic, conic_data: UF.UFCurve.Conic, sense: bool) -> None:
        ...
    def CreateArc(self, arc_coords: UF.UFCurve.Arc, arc: Tag) -> None:
        ...
    def CreateArcThru3pts(self, create_flag: int, first_point: float, second_point: float, third_point: float, arc_tag: Tag) -> None:
        ...
    def CreateBridgeCurve(self, bridge_method: int, curve_ids: typing.List[Tag], parms: float, reverse_tangent: int, bridge_id: Tag) -> None:
        ...
    def CreateBridgeFeature(self, bridge_data: UF.UFCurve.BridgeData, bridge_feature: Tag) -> None:
        ...
    def CreateCombineCurves(self, first_curve_tag: Tag, first_dir: UF.UFCurve.CombineCurvesDirection, second_curve_tag: Tag, second_dir: UF.UFCurve.CombineCurvesDirection, curve_aprox_tol: str, combine_curve_feature: Tag) -> None:
        ...
    def CreateConic(self, conic_data: UF.UFCurve.Conic, conic: Tag) -> None:
        ...
    def CreateFillet(self, type: int, curve_objs: typing.List[Tag], center: float, radius: float, trim_opts: int, arc_opts: int, fillet_obj: Tag) -> None:
        ...
    def CreateIntObject(self, num_objects_set_1: int, object_set_1: typing.List[Tag], num_objects_set_2: int, object_set_2: typing.List[Tag], int_curve_object: Tag) -> None:
        ...
    def CreateIsocline(self, face_cnt: int, faces: typing.List[Tag], direction: float, start_angle: str, end_angle: str, step_angle: str, isocline_feat: Tag) -> None:
        ...
    def CreateJoinedCurve(self, uf_curve_list: typing.List[Tag], creation_method: int, joined_curve: Tag, status: int) -> None:
        ...
    def CreateJoinedFeature(self, uf_curve_string: UF.StringList, creation_method: int, joined_curve_feature: Tag, status: int) -> None:
        ...
    def CreateLine(self, line_coords: UF.UFCurve.Line, line: Tag) -> None:
        ...
    def CreateLineArc(self, line_arc_data: UF.UFCurve.LineArc, line_arc_feat_id: Tag) -> None:
        ...
    def CreateOcfFeature(self, offset_data: UF.UFCurve.OcfData, feature: Tag) -> None:
        ...
    def CreatePoint(self, point_coords: float, point: Tag) -> None:
        ...
    def CreateProjCurves(self, n_curve_refs: int, curve_refs: typing.List[Tag], n_face_refs: int, face_refs: typing.List[Tag], copy_flag: int, proj_data: UF.UFCurve.Proj, proj_curve_feature: Tag) -> None:
        ...
    def CreateProjCurves1(self, n_curve_refs: int, curve_refs: typing.List[Tag], n_face_refs: int, face_refs: typing.List[Tag], copy_flag: int, proj_data: UF.UFCurve.Proj1, proj_curve_feature: Tag) -> None:
        ...
    def CreateShadowCurves(self, solid_count: int, solid_array: typing.List[Tag], view_tag: Tag, shadow_curve_count: int, shadow_curves: typing.List[Tag]) -> None:
        ...
    def CreateShadowOutline(self, solid_count: int, solid_array: typing.List[Tag], view: Tag, loop_count: int, count_array: int, curve_array: typing.List[Tag[]], tol: float) -> None:
        ...
    def CreateSilhouette(self, solid: Tag, view: Tag, count: int, curves: typing.List[Tag]) -> None:
        ...
    def CreateSimplifiedCurve(self, curves_count: int, curves: typing.List[Tag], tolerance: float, segments_count: int, segments: typing.List[Tag]) -> None:
        ...
    def CreateSpline(self, spline_data: UF.UFCurve.Spline, spline_tag: Tag, num_states: int, states: typing.List[UF.UFCurve.State]) -> None:
        ...
    def CreateSplineFeature(self, spline: Tag, feature_id: Tag) -> None:
        ...
    def CreateSplineThruPts(self, degree: int, periodicity: int, num_points: int, point_data: typing.List[UF.UFCurve.PtSlopeCrvatr], parameters: float, save_def_data: int, spline_tag: Tag) -> None:
        ...
    def CreateWrapObject(self, wrap_data: UF.UFCurve.WrapData, wrap_curve_object: Tag) -> None:
        ...
    def EditArcData(self, arc: Tag, arc_coords: UF.UFCurve.Arc) -> None:
        ...
    def EditBridgeFeature(self, bridge_feature: Tag, bridge_data: UF.UFCurve.BridgeData) -> None:
        ...
    def EditByCurveFitData(self, curve_feature: Tag, curve_fit_data: UF.UFModl.CurveFitData) -> None:
        ...
    def EditCombineCurves(self, combine_curve_feature: Tag, first_curve_tag: Tag, first_dir: UF.UFCurve.CombineCurvesDirection, second_curve_tag: Tag, second_dir: UF.UFCurve.CombineCurvesDirection, curve_aprox_tol: str) -> None:
        ...
    def EditConicData(self, conic: Tag, conic_data: UF.UFCurve.Conic) -> None:
        ...
    def EditIntObject(self, num_object_set_1: int, object_set_1: typing.List[Tag], num_object_set_2: int, object_set_2: typing.List[Tag], int_curve_object: Tag) -> None:
        ...
    def EditIsocline(self, isocline_feat: Tag, face_cnt: int, faces: typing.List[Tag], direction: float, start_angle: str, end_angle: str, step_angle: str) -> None:
        ...
    def EditJoinedFeature(self, joined_curve_feature: Tag, uf_curve_string: UF.StringList, creation_method: int, tols: float) -> None:
        ...
    def EditLength(self, curve: Tag, method: int, length: float, location: int, ext_type: int) -> None:
        ...
    def EditLineArc(self, line_arc_feat_id: Tag, line_arc_data: UF.UFCurve.LineArc) -> None:
        ...
    def EditLineData(self, line: Tag, line_coords: UF.UFCurve.Line) -> None:
        ...
    def EditMoveMultPoints(self, curve_tag: Tag, mmcp_dat: UF.CurveBcmmcp) -> None:
        ...
    def EditOcfFeature(self, offset_data: UF.UFCurve.OcfData, feature: Tag) -> None:
        ...
    def EditPointData(self, point: Tag, point_coords: float) -> None:
        ...
    def EditProjCurves(self, proj_curve_feature: Tag, n_curve_refs: int, curve_refs: typing.List[Tag], n_face_refs: int, face_refs: typing.List[Tag], proj_data: UF.UFCurve.Proj) -> None:
        ...
    def EditProjCurves1(self, proj_curve_feature: Tag, n_curve_refs: int, curve_refs: typing.List[Tag], n_face_refs: int, face_refs: typing.List[Tag], proj_data: UF.UFCurve.Proj1) -> None:
        ...
    def EditSplineFeature(self, spline: Tag, feature_id: Tag) -> None:
        ...
    def EditSplineThruPts(self, spline_tag: Tag, degree: int, periodicity: int, num_points: int, point_data: typing.List[UF.UFCurve.PtSlopeCrvatr], parameters: float, save_def_data: int) -> None:
        ...
    def EditTrimCurve(self, curve_tag: Tag, bounding_id: Tag, ref_point: float, int_point: float, ext_ind: int) -> None:
        ...
    def EditWithTemplate(self, edit_id: Tag, template_id: Tag, error_data: UF.UFCurve.FitError) -> None:
        ...
    def EditWrapObject(self, wrap_data: UF.UFCurve.WrapData, wrap_curve_object: Tag) -> None:
        ...
    def EvaluateCurve(self, curve: Tag, param: float, deriv_flag: int, pos_and_deriv: float) -> None:
        ...
    def EvaluateCurveStructure(self, curve_data_ptr: UF.UFCurve.Struct, param: float, deriv_flag: int, pos_and_deriv: float) -> None:
        ...
    def FixSplineData(self, spl: UF.UFCurve.Spline, toler: float, num_states: int, states: typing.List[UF.UFCurve.State]) -> None:
        ...
    def FreeCurveStruct(self, curve_struct: UF.UFCurve.Struct) -> None:
        ...
    def InitOcfData(self, uf_offset_data: UF.UFCurve.OcfData) -> None:
        ...
    def InitProjCurvesData(self, proj_data: UF.UFCurve.Proj) -> None:
        ...
    def InitProjCurvesData1(self, proj_data: UF.UFCurve.Proj1) -> None:
        ...
    def Intersect(self, curve: Tag, entity: Tag, ref_point: float, out_info: UF.UFCurve.IntersectInfo) -> None:
        ...
    def IsSplineInSync(self, spline_tag: Tag, is_sync: bool) -> None:
        ...
    def IsSplineSelfInt(self, spline_tag: Tag, is_self_intersecting: bool) -> None:
        ...
    def ModifyOffsetsInString(self, string_tag: Tag, uf_offset_data: UF.UFCurve.OcfData, num_offsets: int, offset_distance: typing.List[UF.UFCurve.OcfValues]) -> None:
        ...
    def OcfAskCurves(self, feature_eid: Tag, num_curves: int, offset_curves: typing.List[Tag]) -> None:
        ...
    def OcfOffsetPtDirection(self, uf_string_tag: Tag, uf_face_collector_tag: Tag, offset_point: float, offset_direction: float) -> None:
        ...
    def RemoveStringFromOcfData(self, string_tag: Tag, uf_offset_data: UF.UFCurve.OcfData) -> None:
        ...
    def SectionAskParallelData(self, section_curves_feature: Tag, general_data: UF.UFCurve.SectionGeneralData, parallel_data: UF.UFCurve.SectionParallelData) -> None:
        ...
    def SectionAskPerpcrvData(self, section_curves_feature: Tag, general_data: UF.UFCurve.SectionGeneralData, perpcrv_data: UF.UFCurve.SectionPerpcrvData) -> None:
        ...
    def SectionAskPlanesData(self, section_curves_feature: Tag, general_data: UF.UFCurve.SectionGeneralData, planes_data: UF.UFCurve.SectionPlanesData) -> None:
        ...
    def SectionAskRadialData(self, section_curves_feature: Tag, general_data: UF.UFCurve.SectionGeneralData, radial_data: UF.UFCurve.SectionRadialData) -> None:
        ...
    def SectionAskType(self, section_curves_feature: Tag, plane_type: int) -> None:
        ...
    def SectionCurveAskParents(self, section_curve: Tag, section_curves_feature: Tag, plane_type: int, defining_object: Tag, sectioning_objects: typing.List[Tag]) -> None:
        ...
    def SectionFromParallelPlanes(self, general_data: UF.UFCurve.SectionGeneralData, parallel_data: UF.UFCurve.SectionParallelData, section_curves: Tag) -> None:
        ...
    def SectionFromPerpcrvPlanes(self, general_data: UF.UFCurve.SectionGeneralData, perpcrv_data: UF.UFCurve.SectionPerpcrvData, section_curves: Tag) -> None:
        ...
    def SectionFromPlanes(self, general_data: UF.UFCurve.SectionGeneralData, planes_data: UF.UFCurve.SectionPlanesData, section_curves: Tag) -> None:
        ...
    def SectionFromRadialPlanes(self, general_data: UF.UFCurve.SectionGeneralData, radial_data: UF.UFCurve.SectionRadialData, section_curves: Tag) -> None:
        ...
    def SetAnalysisDisplay(self, curve_tag: Tag, analysis_display_options: UF.UFCurve.AnalysisDisplay) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetSplineSap(self, curve_tag: Tag, display_flag: int, scale_factor: float) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SmoothSplineData(self, spline_data: UF.UFCurve.Spline, cont_order: int, distance_toler: float, angle_toler: float, num_states: int, states: typing.List[UF.UFCurve.State]) -> None:
        ...
    def SmoothSplineDataSt(self, spline_data: UF.UFCurve.Spline, cont_order: int, dist_toler: float, ang_toler: float, num_states: int, states: typing.List[UF.UFCurve.State]) -> None:
        ...


    class WrapType(enum.Enum):
        Wrap = 0
        Unwrap = 1
    

    class UFCurveWrapData():
        wrap_unwrap_sw: UF.UFCurve.WrapType
        num_wrap_faces: int
        wrap_faces: typing.List[Tag]
        wrap_plane: Tag
        num_input_curves: int
        input_curves: typing.List[Tag]
        cut_line_angle: str
        distance_tol: float
        angle_tol: float
    

    class UFCurveTrimMult():
        num_bound1_pts: int
        bound1_pts: float
        num_bound2_pts: int
        bound2_pts: float
    

    class UFCurveStruct():
        crv_data: int
        crv_type: int
        crv_t0: float
        crv_tscale: float
        curve_periodic: int
    

    class UFCurveState():
        state_code: int
        flag: int
        value: float
    

    class UFCurveSpline():
        num_poles: int
        order: int
        is_rational: int
        knots: float
        poles: float
        start_param: float
        end_param: float
    

    class UFCurveSectionRadialData():
        base_axis: Tag
        base_point: Tag
        step_angle: float
        start_angle: float
        end_angle: float
    

    class UFCurveSectionPlanesData():
        planes: typing.List[Tag]
        num_planes: int
    

    class UFCurveSectionPerpcrvData():
        curve_eid: Tag
        direction: int
        space_meth: int
        num_points: int
        start_pct: float
        end_pct: float
        ratio: float
        chord_tol: float
        increment: float
    

    class UFCurveSectionParallelData():
        base_plane: Tag
        step_distance: float
        start_distance: float
        end_distance: float
    

    class UFCurveSectionGeneralData():
        objects: typing.List[Tag]
        num_objects: int
        associate: int
        grouping: int
        join_type: int
        tolerance: float
        curve_fit_data: UF.UFModl.CurveFitData
    

    class UFCurvePtSlopeCrvatr():
        point: float
        slope_type: int
        slope: float
        crvatr_type: int
        crvatr: float
    

    class UFCurveProj1():
        proj_data: UF.UFCurve.Proj
        proj_vector: Tag
        x_vector_tag: Tag
        join_type: UF.UFCurve.JoinTypes
        curve_fit_data: UF.UFModl.CurveFitData
    

    class UFCurveProj():
        proj_type: int
        proj_pnt: Tag
        proj_vec: float
        x_vector: float
        multiplicity: int
        arcl_option: int
        angle: float
        ref_pnt: float
    

    class PrincipalAxis(enum.Enum):
        XAxis = 0
        YAxis = 1
        ZAxis = 2
    

    class UFCurveOcfValues():
        _string: str
    

    class OcfTrimMethod(enum.Enum):
        OcfNoExtension = 0
        OcfTangent = 1
    

    class UFCurveOcfStringData():
        string_tag: Tag
        offset_direction: int
        num_offsets: int
        offset_distances: typing.List[UF.UFCurve.OcfValues]
    

    class OcfSpanMethod(enum.Enum):
        OcfSpanNone = 0
        OcfSpanQuilt = 1
    

    class OcfMethod(enum.Enum):
        OcfChordal = 0
        OcfArclength = 1
        OcfGeodesic = 2
        OcfTangential = 3
    

    class UFCurveOcfFaceData():
        face_tag: Tag
    

    class UFCurveOcfData():
        string_data: typing.List[UF.UFCurve.OcfStringData]
        num_string_data: int
        face_data: typing.List[UF.UFCurve.OcfFaceData]
        cross_boundary_mode: UF.UFCurve.OcfCrossBoundaries
        offset_method: UF.UFCurve.OcfMethod
        trim_method: UF.UFCurve.OcfTrimMethod
        span_method: UF.UFCurve.OcfSpanMethod
        dist_tol: float
        ang_tol: float
        string_tol: float
    

    class OcfCrossBoundaries(enum.Enum):
        OcfCrossBoundariesNone = 0
        OcfCrossBoundaries = 1
    

    class LineArcType(enum.Enum):
        AssoNone = -1
        AssoLine = 0
        AssoArc = 1
    

    class UFCurveLineArc():
        curve_type: UF.UFCurve.LineArcType
        arc_constraint_subtype: UF.UFCurve.AssoArcSubtype
        constraints: typing.List[UF.UFCurve.Constraint]
        limits: typing.List[UF.UFCurve.Limit]
        plane_of_curve: Tag
        complement: bool
        closed: bool
        is_associative: bool
    

    class UFCurveLine():
        start_point: float
        end_point: float
    

    class LimitType(enum.Enum):
        LimitToConstraint = 0
        LimitValue = 1
        LimitToEntity = 2
    

    class UFCurveLimit():
        limit_type: UF.UFCurve.LimitType
        value: float
        limiting_obj: Tag
        help_data: UF.UFCurve.HelpData
    

    class JoinTypes(enum.Enum):
        NoJoin = 0
        CubicJoin = 1
        GeneralJoin = 2
        QuinticJoin = 3
    

    class UFCurveIntersectInfo():
        type_of_intersection: int
        curve_point: float
        curve_parm: float
        entity_parms: float
    

    class HelpDataType(enum.Enum):
        HelpDataNone = 0
        HelpDataParameter = 1
        HelpDataValue = 2
    

    class UFCurveHelpData():
        help_data_type: UF.UFCurve.HelpDataType
        value: float
        parameter: float
    

    class UFCurveGenconic():
        matrix_tag: Tag
        coefficients: float
        start_pt: float
        end_pt: float
    

    class UFCurveFitError():
        max_error: float
        avg_error: float
        point_with_max_error: int
        interpolated: int
    

    class EndType(enum.Enum):
        Start = 0
        End = 1
        Middle = 2
        Center = 3
    

    class UFCurveDirectionStructU():
        vector: float
    

    class Direction(enum.Enum):
        AlongPlanarCurveNormals = 0
        AlongFixedVector = 1
    

    class ConstraintType(enum.Enum):
        ConstraintNone = -1
        Coincident = 0
        Tangent = 1
        Normal = 2
        Angle = 3
        AlongX = 4
        AlongY = 5
        AlongZ = 6
        Radius = 7
    

    class UFCurveConstraint():
        constraint_type: UF.UFCurve.ConstraintType
        end_type: UF.UFCurve.EndType
        object_tag: Tag
        value: float
        help_data: UF.UFCurve.HelpData
    

    class UFCurveConic():
        matrix_tag: Tag
        conic_type: int
        rotation_angle: float
        start_param: float
        end_param: float
        center: float
        k1: float
        k2: float
    

    class UFCurveCombineCurvesDirection():
        direction_type: UF.UFCurve.Direction
        direction_struct: UF.UFCurve.DirectionStructU
    

    class BridgeMethod(enum.Enum):
        MatchTangentEnds = 0
        MatchTangentPeak = 1
        MatchCurvatureEnds = 2
        MatchCurvaturePeak = 3
        InheritShape = 4
        TangentConic = 5
    

    class UFCurveBridgeData():
        method: UF.UFCurve.BridgeMethod
        input_curve1: typing.List[UF.StringList]
        input_curve2: typing.List[UF.StringList]
        matchpt_parms: str
        match_point: typing.List[Tag]
        reverse_tangents: bool
        shape_control1: str
        shape_control2: str
        stiffness_method: int
        inherit_curve: typing.List[UF.StringList]
    

    class AssoArcSubtype(enum.Enum):
        LineArcThreePointArc = 0
        AssoArcFromCenter = 1
    

    class UFCurveArc():
        matrix_tag: Tag
        start_angle: float
        end_angle: float
        arc_center: float
        radius: float
    

    class UFCurveAnalysisDisplay():
        curvature_comb_scale_factor: float
        show_control_polygon: bool
        show_curvature_comb: bool
        show_inflections: bool
        show_peaks: bool
        show_knots: bool
        comb_density: float
        comb_interneedle_density: int
        ustart: float
        uend: float
        use_max_length: bool
        max_length: float
        proj_choice: int
        specified_dir: float
    

class UFCsys(Utilities.NXRemotableObject):
    def AskCsysInfo(self, csys_id: Tag, matrix_id: Tag, csys_origin: float) -> None:
        ...
    def AskMatrixOfObject(self, object_id: Tag, matrix_id: Tag) -> None:
        ...
    def AskMatrixValues(self, matrix_id: Tag, matrix_values: float) -> None:
        ...
    def AskWcs(self, wcs_id: Tag) -> None:
        ...
    def CreateCsys(self, csys_origin: float, matrix_id: Tag, csys_id: Tag) -> None:
        ...
    def CreateMatrix(self, matrix_values: float, matrix_id: Tag) -> None:
        ...
    def CreateTempCsys(self, csys_origin: float, matrix_id: Tag, csys_id: Tag) -> None:
        ...
    def EditMatrixOfObject(self, object_id: Tag, matrix_id: Tag) -> None:
        ...
    def MapPoint(self, input_csys: int, input_point: float, output_csys: int, output_point: float) -> None:
        ...
    def SetOrigin(self, csys_tag: Tag, origin: float) -> None:
        ...
    def SetWcs(self, csys_id: Tag) -> None:
        ...
    def SetWcsDisplay(self, display_status: int) -> None:
        ...


class UFConstants(Utilities.NXRemotableObject):



































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































    def __init__(self) -> None: ...


class UFClsf(Utilities.NXRemotableObject):
    def Import(self, part_tag: Tag, clsf_name: str) -> None:
        ...


class UFClone(Utilities.NXRemotableObject):
    def AddAssembly(self, part_name: str, load_status: UF.UFPart.LoadStatus) -> int:
        ...
    def AddPart(self, part_name: str) -> None:
        ...
    def ApplyDefaults(self, naming_failures: UF.UFClone.NamingFailures) -> None:
        ...
    def ApplySelectiveExportXml(self, xml_file: str, load_status: UF.UFPart.LoadStatus) -> None:
        ...
    def AskAction(self, input_part_name: str, action_type: UF.UFClone.Action) -> None:
        ...
    def AskAssocFileCopy(self, input_part_name: str, copy_associated: bool) -> None:
        ...
    def AskAssocFileDir(self, input_part_name: str, assoc_file_dir: str) -> None:
        ...
    def AskAssocFileRootDir(self, root_directory: str) -> None:
        ...
    def AskAttachLogFile(self, attach_log_file: bool) -> None:
        ...
    def AskCi(self, input_part_name: str, checkin_data: typing.List[UF.UFClone.CheckinData]) -> None:
        ...
    def AskCiCommentChecking(self, input_part_name: str, error_unless_comments_match: bool, comment: str) -> None:
        ...
    def AskCloneRelatedCae(self, rel_cae: UF.UFClone.CloneRelCae) -> None:
        ...
    def AskCloneRelatedDwgs(self, rel_dwgs: bool) -> None:
        ...
    def AskCo(self, input_part_name: str, checkout_data: typing.List[UF.UFClone.CheckoutData]) -> None:
        ...
    def AskCvtCallbacks(self, n_callbacks: int, points: typing.List[UF.UFClone.ConvertCb], names: str, descriptions: str) -> None:
        ...
    def AskDefAction(self, action: UF.UFClone.Action) -> None:
        ...
    def AskDefAssocFileCopy(self, copy_associated: bool) -> None:
        ...
    def AskDefCi(self, checkin_data: typing.List[UF.UFClone.CheckinData]) -> None:
        ...
    def AskDefCiCommentChecking(self, error_unless_comments_match: bool, comment: str) -> None:
        ...
    def AskDefCo(self, checkout_data: typing.List[UF.UFClone.CheckoutData]) -> None:
        ...
    def AskDefDirectory(self, directory_name: str) -> None:
        ...
    def AskDefFolder(self, folder_name: str) -> None:
        ...
    def AskDefGroup(self, group: str) -> None:
        ...
    def AskDefItemType(self, item_type: str) -> None:
        ...
    def AskDefNaming(self, naming: UF.UFClone.NamingTechnique) -> None:
        ...
    def AskDefOwner(self, owner: str) -> None:
        ...
    def AskDefPdmDesc(self, pdm_desc: str) -> None:
        ...
    def AskDefPdmName(self, pdm_name: str) -> None:
        ...
    def AskDefValidationOptions(self, validation_options: typing.List[UF.UFClone.ValidationOpts]) -> None:
        ...
    def AskDryrun(self, dryrun: bool) -> None:
        ...
    def AskFamilyTreatment(self, treatment: UF.UFClone.FamilyTreatment) -> None:
        ...
    def AskGroup(self, input_part_name: str, group: str) -> None:
        ...
    def AskItemType(self, input_part_name: str, item_type: str) -> None:
        ...
    def AskLogfile(self, log_file_name: str) -> None:
        ...
    def AskNaming(self, input_part_name: str, naming_technique: UF.UFClone.NamingTechnique, output_part_spec: str) -> None:
        ...
    def AskNtfyCallbacks(self, n_callbacks: int, points: typing.List[UF.UFClone.NotifyCb], names: str, descriptions: str) -> None:
        ...
    def AskOperationClass(self, operation_class: UF.UFClone.OperationClass) -> None:
        ...
    def AskOwner(self, input_part_name: str, owner: str) -> None:
        ...
    def AskPartState(self, input_part_name: str, state: UF.UFClone.PartStateS) -> None:
        ...
    def AskPdmDesc(self, input_part_name: str, pdm_desc: str) -> None:
        ...
    def AskPdmName(self, input_part_name: str, pdm_name: str) -> None:
        ...
    def AskRevUp(self, rev_up: bool) -> None:
        ...
    def AskValidationAbortOption(self, abort_import: bool) -> None:
        ...
    def AskValidationOptions(self, input_part_name: str, validation_options: typing.List[UF.UFClone.ValidationOpts]) -> None:
        ...
    def Base64ToBytes(self, bytes: bytes, nbytes: int, data: str, offset: int, length: int) -> None:
        ...
    def Decode(self, aesKey: bytes, inp_string: str, str_length: int, decoded_str: str) -> None:
        ...
    def EnsureDefDirectory(self, directory_name: str) -> None:
        ...
    def ExecuteLogFile(self, operation_class: UF.UFClone.OperationClass, logfile_name: str, options: UF.UFClone.ExLogOpts) -> None:
        ...
    def FreeValidationOptions(self, validation_options: UF.UFClone.ValidationOpts) -> None:
        ...
    def GenerateReport(self) -> None:
        ...
    def GetKey(self, aesKey: bytes) -> None:
        ...
    def InitLogFileFailure(self, logfile_failures: UF.UFClone.LogFileFailure) -> None:
        ...
    def InitNamingFailures(self, failures: UF.UFClone.NamingFailures) -> None:
        ...
    def Initialise(self, operation_class: UF.UFClone.OperationClass) -> None:
        ...
    def Iterate(self, part_name: str) -> None:
        ...
    def LoadCrypt(self) -> None:
        ...
    def LoadLogfile(self, log_file_name: str, naming_failures: UF.UFClone.NamingFailures, logfile_failure: UF.UFClone.LogFileFailure, load_status: UF.UFPart.LoadStatus) -> None:
        ...
    def PartUnderSpecified(self, part_name: str, is_under_specified: bool) -> None:
        ...
    def PerformClone(self, naming_failures: UF.UFClone.NamingFailures) -> None:
        ...
    def RegisterCvtCallback(self, cb: UF.UFClone.ConvertCb, callback: UF.UFClone.ConvertCallbackT, name: str, description: str, relative_callback: str, before_or_after_relative: bool) -> None:
        ...
    def RegisterNtfyCallback(self, cb: UF.UFClone.NotifyCb, callback: UF.UFClone.NotifyCallbackT, name: str, description: str, relative_callback: str, before_relative: bool) -> None:
        ...
    def RemoveCvtCallback(self, cb: UF.UFClone.ConvertCb, name: str, callback_removed: UF.UFClone.ConvertCallbackT) -> None:
        ...
    def RemoveNtfyCallback(self, cb: UF.UFClone.NotifyCb, name: str, callback_removed: UF.UFClone.NotifyCallbackT) -> None:
        ...
    def ResetToDefault(self) -> None:
        ...
    def SetAction(self, input_part_name: str, action_type: UF.UFClone.Action, replacement_part: str) -> None:
        ...
    def SetAssocFileCopy(self, input_part_name: str, copy_associated: bool) -> None:
        ...
    def SetAssocFileDir(self, input_part_name: str, assoc_file_dir: str) -> None:
        ...
    def SetAssocFileRootDir(self, root_directory: str) -> None:
        ...
    def SetAttachLogFile(self, attach_log_file: bool) -> None:
        ...
    def SetCi(self, input_part_name: str, checkin_data: UF.UFClone.CheckinData) -> None:
        ...
    def SetCiCommentChecking(self, input_part_name: str, error_unless_comments_match: bool, comment: str) -> None:
        ...
    def SetCloneRelatedCae(self, rel_cae: UF.UFClone.CloneRelCae) -> None:
        ...
    def SetCloneRelatedDwgs(self, rel_dwgs: bool) -> None:
        ...
    def SetCo(self, input_part_name: str, checkout_data: UF.UFClone.CheckoutData) -> None:
        ...
    def SetDefAction(self, action: UF.UFClone.Action) -> None:
        ...
    def SetDefAssocFileCopy(self, copy_associated: bool) -> None:
        ...
    def SetDefCi(self, checkin_data: UF.UFClone.CheckinData) -> None:
        ...
    def SetDefCiCommentChecking(self, error_unless_comments_match: bool, comment: str) -> None:
        ...
    def SetDefCo(self, checkout_data: UF.UFClone.CheckoutData) -> None:
        ...
    def SetDefDirectory(self, directory_name: str) -> None:
        ...
    def SetDefFolder(self, folder_name: str) -> None:
        ...
    def SetDefGroup(self, group: str) -> None:
        ...
    def SetDefItemType(self, item_type: str) -> None:
        ...
    def SetDefNaming(self, naming_technique: UF.UFClone.NamingTechnique) -> None:
        ...
    def SetDefOwner(self, owner: str) -> None:
        ...
    def SetDefPdmDesc(self, pdm_desc: str) -> None:
        ...
    def SetDefPdmName(self, pdm_name: str) -> None:
        ...
    def SetDefValidationOptions(self, validation_options: UF.UFClone.ValidationOpts) -> None:
        ...
    def SetDryrun(self, dryrun: bool) -> None:
        ...
    def SetFamilyTreatment(self, treatment: UF.UFClone.FamilyTreatment) -> None:
        ...
    def SetGroup(self, input_part_name: str, group: str) -> None:
        ...
    def SetIdentifierDisplayRule(self, identifier_display_rule_name: str) -> None:
        ...
    def SetItemType(self, input_part_name: str, item_type: str) -> None:
        ...
    def SetLogfile(self, log_file_name: str) -> None:
        ...
    def SetNameRule(self, name_rule: UF.UFClone.NameRuleDef, naming_failures: UF.UFClone.NamingFailures) -> None:
        ...
    def SetNaming(self, input_part_name: str, naming_technique: UF.UFClone.NamingTechnique, output_part_name: str) -> None:
        ...
    def SetOwner(self, input_part_name: str, owner: str) -> None:
        ...
    def SetPdmDesc(self, input_part_name: str, pdm_desc: str) -> None:
        ...
    def SetPdmName(self, input_part_name: str, pdm_name: str) -> None:
        ...
    def SetPropagateActions(self, propagate_actions: bool) -> None:
        ...
    def SetRevUp(self, rev_up: bool) -> None:
        ...
    def SetValidationAbortOption(self, abort_import: bool) -> None:
        ...
    def SetValidationOptions(self, input_part_name: str, validation_options: UF.UFClone.ValidationOpts) -> None:
        ...
    def StartIteration(self) -> None:
        ...
    def StopIteration(self) -> None:
        ...
    def Terminate(self) -> None:
        ...
    def UnapplyDefaults(self, naming_failures: UF.UFClone.NamingFailures) -> None:
        ...


    class UFCloneValidationOpts():
        mode: UF.UFClone.ValidationMode
        validation_rule: str
        treat_warning_as_pass: bool
        treat_outdated_as_pass: bool
    

    class ValidationMode(enum.Enum):
        NoValidation = 0
        ImportFromPart = 1
        RunValidation = 2
        RunValidationHybrid = 3
    

    class PartStateS(enum.Enum):
        PresentState = 0
        LostState = 1
        NonmasterState = 2
        RefnonmasterState = 3
        NameOnlyState = 4
    

    class OperationClass(enum.Enum):
        CloneOperation = 0
        EditOperation = 1
        ImportOperation = 2
        ExportOperation = 3
    

    class NotifyResponse(enum.Enum):
        Continue = 0
        Cut = 1
        Forbid = 2
        NotifyError = 3
    

    class NotifyCb(enum.Enum):
        InitialiseCb = 0
        TerminateCb = 1
        BegAssyLoadCb = 2
        EndAssyLoadCb = 3
        BegAssyNcLoadCb = 4
        EndAssyNcLoadCb = 5
        BegPartLoadCb = 6
        EndPartLoadCb = 7
        BegPartLoadNcCb = 8
        EndPartLoadNcCb = 9
        BegPerformCb = 10
        EndPerformCb = 11
        BegApplyDefsCb = 12
        EndApplyDefsCb = 13
        BegSetDefActionCb = 14
        EndSetDefActionCb = 15
        BegSetActionCb = 16
        EndSetActionCb = 17
        BegSetNameRuleCb = 18
        EndSetNameRuleCb = 19
        BegSetDefNamingCb = 20
        EndSetDefNamingCb = 21
        BegSetNamingCb = 22
        EndSetNamingCb = 23
        BegSetNameCb = 24
        EndSetNameCb = 25
        BegSetDefPdmNameCb = 26
        EndSetDefPdmNameCb = 27
        BegSetPdmNameCb = 28
        EndSetPdmNameCb = 29
        BegSetDefItemTypeCb = 30
        EndSetDefItemTypeCb = 31
        BegSetItemTypeCb = 32
        EndSetItemTypeCb = 33
        BegSetDefPdmDescCb = 34
        EndSetDefPdmDescCb = 35
        BegSetPdmDescCb = 36
        EndSetPdmDescCb = 37
        BegSetDefCoCb = 38
        EndSetDefCoCb = 39
        BegSetCoCb = 40
        EndSetCoCb = 41
        BegPartCo = 42
        EndPartCo = 43
        BegSetDefCiCb = 44
        EndSetDefCiCb = 45
        BegSetCiCb = 46
        EndSetCiCb = 47
        BegPartCi = 48
        EndPartCi = 49
        BegPartCloneCb = 50
        EndPartCloneCb = 51
        BegOccReportCb = 52
        BegNonoccReportCb = 53
        ReportCb = 54
        EndReportCb = 55
    

    

    class NamingTechnique(enum.Enum):
        Autogen = 0
        Autotranslate = 1
        NamingRule = 2
        UserName = 3
        DefaultNaming = 4
        AltidAutotranslate = 5
    

    class UFCloneNamingFailures():
        n_failures: int
        statuses: int
        input_names: str
        output_names: str
    

    class NameRuleType(enum.Enum):
        PrependString = 0
        AppendString = 1
        ReplaceString = 2
        Rename = 3
    

    class UFCloneNameRuleDef():
        type: UF.UFClone.NameRuleType
        base_string: str
        new_string: str
    

    class UFCloneLogFileFailure():
        line_number: int
        input_part_name: str
        invalid_token: str
    

    class FamilyTreatment(enum.Enum):
        TreatAsLost = 0
        StripFamilyStatus = 1
        GiveError = 2
    

    class UFCloneExLogOpts():
        allow_missing_components: bool
        allow_out_of_sync_bvrs: bool
    

    class ConvertResponse(enum.Enum):
        UseSupplied = 0
        NotConverted = 1
        NoConversion = 2
        ConvertError = 3
    

    class ConvertCb(enum.Enum):
        UserNameConvert = 0
        PartTypeConvert = 1
        PartNameConvert = 2
        PartDescConvert = 3
        PartOwnUserConvert = 4
        PartOwnGroupConvert = 5
        PartCheckoutConvert = 6
        AssocFileDirConvert = 7
    

    

    class CloneRelCae(enum.Enum):
        CloneSimFemIdeal = 0
        CloneFemIdeal = 1
        CloneIdeal = 2
        CloneNone = 3
    

    class UFCloneCheckoutData():
        checkout: bool
        comment: str
    

    class UFCloneCheckinData():
        checkin: bool
        error_if_no_co: bool
    

    class Action(enum.Enum):
        Clone = 0
        Retain = 1
        Replace = 2
        Overwrite = 3
        UseExisting = 4
        DefaultAction = 5
        Exclude = 6
        NewRevision = 7
    

class UFClear(Utilities.NXRemotableObject):
    def AskAnalysisMode(self, dataset: Tag, analysis_mode: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskDatasetName(self, dataset: Tag, name: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskDatasetVersion(self, dataset: Tag, version: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskDefaultClearZone(self, dataset: Tag, def_clr_zone: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskExcludeRules(self, dataset: Tag, exclude_rules: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskInterfData(self, dataset: Tag, object1: Tag, object2: Tag, interf_data: UF.UFClear.InterfData) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskNextDataset(self, part_tag: Tag, dataset: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskNextInterf(self, dataset: Tag, object1: Tag, object2: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskNumLists(self, dataset: Tag, num_lists: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskObjAllButList(self, dataset: Tag, which_list: int, list_size: int, tag_array: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskObjList(self, dataset: Tag, which_list: int, list_type: int, list_size: int, tag_array: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskObjectClearZone(self, dataset: Tag, _object: Tag, clr_zone: Tag, source: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPairClearZone(self, dataset: Tag, object1: Tag, object2: Tag, clr_zone: Tag, source: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPreferences(self, dataset: Tag, preferences: UF.UFClear.Pref) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskResults(self, dataset: Tag, summary: UF.UFClear.Summary) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CopyDataset(self, dataset: Tag, name: str, mode: int, new_dataset: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CountDatasets(self, part_tag: Tag, num: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CountInterferences(self, dataset: Tag, num_interf: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CreateDataset(self, part_tag: Tag, name: str, dataset: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DeleteAll(self, part_tag: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DeleteDataset(self, dataset: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DeleteInterf(self, dataset: Tag, object1: Tag, object2: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DoClearanceAnalysis(self, dataset: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def FindDataset(self, part_tag: Tag, name: str, dataset: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def IsPairChanged(self, dataset: Tag, object1: Tag, object2: Tag, is_changed: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def IsPairIncluded(self, dataset: Tag, object1: Tag, object2: Tag, include_it: bool, reason: int, text: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def RenameDataset(self, dataset: Tag, name: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetAnalysisMode(self, dataset: Tag, analysis_mode: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetDefaultClearZone(self, dataset: Tag, def_clr_zone: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetExcludeRules(self, dataset: Tag, exclude_rules: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetInterfText(self, dataset: Tag, object1: Tag, object2: Tag, text: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetObjList(self, dataset: Tag, which_list: int, list_type: int, list_size: int, tag_array: typing.List[Tag]) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetObjectClearZone(self, dataset: Tag, _object: Tag, clr_zone: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPairClearZone(self, dataset: Tag, object1: Tag, object2: Tag, clr_zone: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPairExclusion(self, dataset: Tag, object1: Tag, object2: Tag, text: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPairInclusion(self, dataset: Tag, object1: Tag, object2: Tag, text: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetPreferences(self, dataset: Tag, preferences: UF.UFClear.Pref) -> None:
        """[Obsolete("Deprecated")"""
        ...


    class UFClearSummary():
        start_time: int
        end_time: int
        run_time: int
        version: int
        analysis_mode: int
        num_lists: int
        n_list1: int
        n_list2: int
        n_pairs: int
        excluded_pairs: int
        changed_pairs: int
        changed_objs: int
        checked_pairs: int
        new_n_hard: int
        new_n_soft: int
        new_n_touching: int
        new_n_containment: int
        new_n_all_interf: int
        n_hard: int
        n_soft: int
        n_touching: int
        n_containment: int
        n_all_interf: int
        job_aborted: int
        num_zones: int
    

    class UFClearPref():
        interactive_msg_filter: int
        save_interference: bool
        interference_layer: int
        interference_color: int
        interf_attn_color: int
        parent_attn_color: int
    

    class UFClearInterfData():
        type: int
        new_interference: bool
        n_bodies: int
        interf_bodies: typing.List[Tag]
        point1: float
        point2: float
        text: str
        interf_num: int
    

class UFCgm(Utilities.NXRemotableObject):
    def AskDefaultCustomColors(self, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def AskDefaultCustomWidths(self, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def AskDefaultExportOptions(self, export_options: UF.UFCgm.ExportOptions) -> None:
        ...
    def AskSessionCustomColors(self, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def AskSessionCustomWidths(self, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def AskSessionExportOptions(self, export_options: UF.UFCgm.ExportOptions) -> None:
        ...
    def ExportCgm(self, drawing_sheet: Tag, export_options: UF.UFCgm.ExportOptions, file_name: str) -> None:
        ...
    def ImportCgm(self, file_name: str, import_options: UF.UFCgm.ImportOptions) -> None:
        ...
    def InitImportOptions(self, import_options: UF.UFCgm.ImportOptions) -> None:
        ...
    def RegisterCallbacks(self, pre_export: UF.UFCgm.PreExportFT, post_export: UF.UFCgm.PostExportFT, export_error: UF.UFCgm.ExportErrorFT) -> None:
        ...
    def SetSessionCustomColors(self, custom_colors: UF.UFCgm.CustomColors) -> None:
        ...
    def SetSessionCustomWidths(self, custom_widths: UF.UFCgm.CustomWidths) -> None:
        ...
    def SetSessionExportOptions(self, export_options: UF.UFCgm.ExportOptions) -> None:
        ...
    def UnregisterCallbacks(self, pre_export: UF.UFCgm.PreExportFT, post_export: UF.UFCgm.PostExportFT, export_error: UF.UFCgm.ExportErrorFT) -> None:
        ...


    class WidthUse(enum.Enum):
        WidthSingle = 0
        WidthByWidth = 1
        WidthByColor = 2
    

    class WidthSingle(enum.Enum):
        WidthStd = 0
        WidthCustom = 1
        WidthUser = 2
    

    class Widths(enum.Enum):
        StandardWidths = 0
        SingleWidth = 1
        Custom3Widths = 2
        CustomPaletteWidths = 3
        DefaultFileWidths = 4
    

    class UFCgmWidthCustom():
        width: float
        name: str
    

    class UFCgmWidthColor():
        width: float
        width_source: int
    

    class VdcMode(enum.Enum):
        IntegerVdc = 0
        RealVdc = 1
    

    class Units(enum.Enum):
        Millimeters = 0
        Inches = 1
    

    class TextMode(enum.Enum):
        TextAsPolylines = 0
        TextAsCharacters = 1
        TextBestFit = 2
        TextReserved1 = 3
        TextReserved2 = 4
    

    class SizeMode(enum.Enum):
        SizeByScale = 0
        SizeByDimensions = 1
    

    class UFCgmSize():
        mode: UF.UFCgm.SizeMode
        scale: float
        dimensions: UF.UFCgm.Dimensions
    

    

    

    class UFCgmImportOptions():
        allow_new_drawing: bool
    

    class Fonts(enum.Enum):
        _1_CALS_FONT = 0
        _4_CALS_FONTS = 1
        NxFonts = 2
        DefaultFileFonts = 3
    

    class ExportSource(enum.Enum):
        DrawingSheet = 0
        CurrentDisplayIsDrawingSheet = 1
        CurrentDisplayIsModelingLayout = 2
    

    class ExportReason(enum.Enum):
        PlotReason = 0
        ExportReason = 1
        PrintReason = 2
        CopyDisplayReason = 3
        PdfReason = 4
        MiscApplReason = 5
        PdfHiddenTextReason = 6
        VisedHiddenTextReason = 7
        MaxReasons = 8
    

    class UFCgmExportOptions():
        colors: UF.UFCgm.Colors
        widths: UF.UFCgm.Widths
        vdc_mode: UF.UFCgm.VdcMode
        size: UF.UFCgm.Size
        text_mode: UF.UFCgm.TextMode
        fonts: UF.UFCgm.Fonts
        reason: UF.UFCgm.ExportReason
        tolerance: float
    

    

    class UFCgmDimensions():
        units: UF.UFCgm.Units
        dimensions: float
        boundingBox: float
    

    class UFCgmCustomWidths():
        units: int
        use: UF.UFCgm.WidthUse
        single: UF.UFCgm.WidthSingle
        single_width: float
        single_source: int
        custom: typing.List[UF.UFCgm.WidthCustom]
        color: typing.List[UF.UFCgm.WidthColor]
    

    class UFCgmCustomColors():
        colors: typing.List[UF.UFCgm.Color]
    

    class Colors(enum.Enum):
        AsDisplayedColors = 0
        PartColors = 1
        CustomPaletteColors = 2
        BlackOnWhite = 3
        LegacyColors = 4
        ColorByWidth = 5
    

    class UFCgmColor():
        clr_index: int
        clr_name: str
        clr_vals: float
        favorite_index: int
    

class UFCfi(Utilities.NXRemotableObject):
    def AskFileExist(self, file_spec: str, status: int) -> None:
        ...
    def GetUniqueFilename(self, fname: str) -> None:
        ...
    def Spawn(self, program: str, num_args: int, arguments: str, is_concur: bool, process_id: int) -> None:
        ...
    def SpawnCheckStatus(self, process_id: int, still_running: bool, return_status: int) -> None:
        ...


class UFCamtext(Utilities.NXRemotableObject):
    def AppendItems(self, object_tag: Tag, count: int, entity_list: typing.List[Tag]) -> None:
        ...
    def AskItemEntity(self, item: int, entity: Tag) -> None:
        ...
    def AskItems(self, object_tag: Tag, count: int, items: int) -> None:
        ...
    def DeleteGeometry(self, object_tag: Tag) -> None:
        ...
    def DeleteItem(self, object_tag: Tag, item: int) -> None:
        ...


class UFCamPrepro(Utilities.NXRemotableObject):
    def InitModule(self) -> None:
        ...
    def MarkModelAsCam(self, model: Tag) -> None:
        ...


class UFCamPref(Utilities.NXRemotableObject):
    def AskDataType(self, pref: UF.UFCamPref.CamPrefEnum, type: UF.UFParam.Type) -> None:
        ...
    def AskIntegerValue(self, pref: UF.UFCamPref.CamPrefEnum, value: int) -> None:
        ...
    def AskLogicalValue(self, pref: UF.UFCamPref.CamPrefEnum, value: bool) -> None:
        ...
    def SetIntegerValue(self, pref: UF.UFCamPref.CamPrefEnum, value: int) -> None:
        ...
    def SetLogicalValue(self, pref: UF.UFCamPref.CamPrefEnum, value: bool) -> None:
        ...


    class CamPrefEnum(enum.Enum):
        BlankGeomColor = 0
        BlankGeomType = 1
        CheckGeomColor = 2
        CheckGeomType = 3
        ClearanceGeomColor = 4
        ClsfDecimalPlace = 5
        RefreshBefPathReplay = 6
        CollectInstances = 7
        CutAreaGeomColor = 8
        CutAreaGeomType = 9
        DriveGeomColor = 10
        GenerateInstance = 11
        InfoCsys = 12
        McsLinkToRcs = 13
        PartGeomColor = 14
        PartGeomType = 15
        PauseAftPath = 16
        RefreshBefPathGenerate = 17
        RelocateParameters = 18
        RunProcessAssistant = 19
        SuspectBoundingBoxColor = 20
        TransformToolpath = 21
        TrimGeomColor = 22
        UncutGeomColor = 23
        UnlinkInstance = 24
        UpdatePostFromTool = 25
        ForceLoadAndTurretTool = 26
        UseCustomizedInterface = 27
        VisibleScrollableItems = 28
        VisualizeToolDisplayColor = 29
        VisualizeGougeColor = 30
        VisualizeCollisionColor = 31
        VisualizeExcessMaterialColor = 32
        VisualizeAutoBlockColor = 33
        VisualizeDmrTool1Color = 34
        VisualizeDmrTool2Color = 35
        VisualizeDmrTool3Color = 36
        VisualizeDmrTool4Color = 37
        VisualizeDmrTool5Color = 38
        OrientWcsToMcs = 39
        CreFeaGrpInManuFeaMang = 40
        AutosetMachiningData = 41
        AutomaticallyUpdateWhenLoading = 42
    

class UFCamgeom(Utilities.NXRemotableObject):
    def AppendCustomPoints(self, object_tag: Tag, point_type: UF.UFCamgeom.CustomPointType, count: int, point_data: typing.List[UF.UFCamgeom.CustomPoint]) -> None:
        ...
    def AppendItems(self, object_tag: Tag, geometry_type: UF.CamGeomType, count: int, entity_list: typing.List[Tag], app_data: typing.List[UF.UFCamgeom.AppData]) -> None:
        ...
    def AskCollectorItems(self, object_tag: int, count: int, items: typing.List[Tag]) -> None:
        ...
    def AskCustomPoints(self, object_tag: Tag, point_type: UF.UFCamgeom.CustomPointType, count: int, point_data: typing.List[UF.UFCamgeom.CustomPoint]) -> None:
        ...
    def AskGeomProvider(self, object_tag: Tag, geometry_type: UF.CamGeomType, provider_tag: Tag) -> None:
        ...
    def AskItemAppData(self, item: int, app_data: UF.UFCamgeom.AppData) -> None:
        ...
    def AskItemEntity(self, item: int, entity: Tag) -> None:
        ...
    def AskItemMaxmin(self, object_tag: Tag, geometry_type: UF.CamGeomType, entity: Tag, maxmin: float) -> None:
        ...
    def AskItems(self, object_tag: Tag, geometry_type: UF.CamGeomType, count: int, items: int) -> None:
        ...
    def DeleteCustomPoints(self, object_tag: Tag, point_type: UF.UFCamgeom.CustomPointType) -> None:
        ...
    def DeleteGeometry(self, object_tag: Tag, geometry_type: UF.CamGeomType) -> None:
        ...
    def DeleteItem(self, object_tag: Tag, geometry_type: UF.CamGeomType, item: int) -> None:
        ...
    def EvalSurface(self, object_tag: Tag, geometry_type: UF.CamGeomType, entity: Tag, uv: float, srf_value: UF.ModlSrfValue) -> None:
        ...
    def SetItemAppData(self, object_tag: Tag, geometry_type: UF.CamGeomType, item: int, app_data: UF.UFCamgeom.AppData) -> None:
        ...


    class CustomPointType(enum.Enum):
        PredrillEngageType = 0
        CutRegionStartType = 1
    

    class UFCamgeomCustomPoint():
        point_tag: Tag
        point_acs: float
        upper_depth: float
        lower_depth: float
        depth: float
    

    class UFCamgeomAppData():
        has_stock: int
        stock: float
        has_cut_stock: int
        cut_stock: float
        has_tolerances: int
        tolerances: float
        has_feedrate: int
        feedrate_unit: UF.CamFeedrateUnit
        feedrate_value: float
        has_offset: int
        offsetType: int
        nominalOffset: float
        offset: float
        has_avoidance_type: int
        avoidance_type: UF.CamAvoidanceType
    

class UFCambndWedm(Utilities.NXRemotableObject):
    def AppendItemUde(self, item: int, pass_num: int, set_type: UF.CambndUdeSetType, ude_name: str, ude: int, response: bool) -> None:
        ...
    def AskItemUdes(self, item: int, set_type: UF.CambndUdeSetType, pass_num: int, num_udes: int, udes: int) -> None:
        ...
    def DeleteAllItemUdes(self, item: int, set_type: UF.CambndUdeSetType) -> None:
        ...
    def DeleteItemUde(self, item: int, pass_num: int, set_type: UF.CambndUdeSetType, ude: int) -> None:
        ...


class UFCambnd(Utilities.NXRemotableObject):
    def AppendBndFromCurve(self, object_tag: Tag, type: UF.CamGeomType, count: int, curves: typing.List[Tag], boundary_data: UF.UFCambnd.BoundaryData, app_data: typing.List[UF.UFCambnd.AppData]) -> None:
        ...
    def AppendBndFromFace(self, object_tag: Tag, type: UF.CamGeomType, face: Tag, boundary_data: UF.UFCambnd.BoundaryData) -> None:
        ...
    def AppendItemUde(self, item: int, set_type: UF.CambndUdeSetType, ude_name: str, ude: int, response: bool) -> None:
        ...
    def AskBoundaries(self, object_tag: Tag, type: UF.CamGeomType, count: int, boundaries: int) -> None:
        ...
    def AskBoundaryAppData(self, boundary: int, app_data: UF.UFCambnd.AppData) -> None:
        ...
    def AskBoundaryData(self, boundary: int, boundary_data: UF.UFCambnd.BoundaryData) -> None:
        ...
    def AskBoundaryGroupData(self, boundary: int, group_data: UF.UFCambnd.GroupData) -> None:
        ...
    def AskBoundaryItems(self, boundary: int, count: int, items: int) -> None:
        ...
    def AskItemAppData(self, item: int, app_data: UF.UFCambnd.AppData) -> None:
        ...
    def AskItemEntity(self, item: int, entity: Tag) -> None:
        ...
    def AskItemGroupData(self, item: int, group_data: UF.UFCambnd.GroupData) -> None:
        ...
    def AskItemUdes(self, item: int, set_type: UF.CambndUdeSetType, num_udes: int, udes: int) -> None:
        ...
    def CanAcceptItemUde(self, item: int, set_type: UF.CambndUdeSetType, ude_name: str, response: bool) -> None:
        ...
    def DeleteAllItemUdes(self, item: int, set_type: UF.CambndUdeSetType) -> None:
        ...
    def DeleteBoundaries(self, object_tag: Tag, type: UF.CamGeomType) -> None:
        ...
    def DeleteBoundary(self, object_tag: Tag, type: UF.CamGeomType, boundary: int) -> None:
        ...
    def DeleteItemUde(self, item: int, set_type: UF.CambndUdeSetType, ude: int) -> None:
        ...
    def IsInherited(self, object_tag: Tag, type: UF.CamGeomType, response: bool) -> None:
        ...
    def SetBoundaryAppData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, app_data: UF.UFCambnd.AppData) -> None:
        ...
    def SetBoundaryGroupData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, group_data: UF.UFCambnd.GroupData) -> None:
        ...
    def SetBoundaryPlane(self, boundary: int, bnd_origin: float, bnd_matrix: float) -> None:
        ...
    def SetItemAppData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, app_data: UF.UFCambnd.AppData) -> None:
        ...
    def SetItemGroupData(self, object_tag: Tag, type: UF.CamGeomType, boundary: int, item: int, group_data: UF.UFCambnd.GroupData) -> None:
        ...


    class UFCambndGroupData():
        has_offset: int
        offsetType: int
        offset: float
        nominalOffset: float
    

    class UFCambndBoundaryData():
        boundary_type: UF.CamBoundaryType
        plane_type: int
        origin: float
        matrix: float
        material_side: UF.CamMaterialSide
        ignore_holes: int
        ignore_islands: int
        ignore_chamfers: int
        app_data: typing.List[UF.UFCambnd.AppData]
    

    class UFCambndAppData():
        has_stock: int
        stock: float
        has_tolerances: int
        tolerances: float
        has_feedrate: int
        feedrate_unit: UF.CamFeedrateUnit
        feedrate_value: float
        has_blank_distance: int
        blank_distance: float
        has_tool_position: int
        tool_position: UF.CamToolPosition
    

class UFCam(Utilities.NXRemotableObject):
    def AskAutoBlank(self, object_tag: Tag, geom_type: UF.UFCam.BlankGeomType, offset: float) -> None:
        ...
    def AskBlankMatlDbObject(self, db_obj: int) -> None:
        ...
    def AskCamPreferences(self, prefs: UF.UFCam.Preferences) -> None:
        ...
    def AskClearPlaneData(self, object_tag: Tag, origin: float, normal: float) -> None:
        ...
    def AskClearPlaneStatus(self, object_tag: Tag, status: UF.ParamClrplaneStatus) -> None:
        ...
    def AskClearPlaneTag(self, object_tag: Tag, target_tag: Tag) -> None:
        ...
    def AskClearPlaneUsage(self, object_tag: Tag, usage: UF.ParamClrplaneUsage) -> None:
        ...
    def AskConfigFile(self, cam_config_filename: str) -> None:
        ...
    def AskCutterDbObject(self, db_obj: int) -> None:
        ...
    def AskDocTemplateName(self, doc_template_filename: str) -> None:
        ...
    def AskFSDbObject(self, db_obj: int) -> None:
        ...
    def AskLowerLimitPlaneData(self, object_tag: Tag, origin: float, normal: float) -> None:
        ...
    def AskLowerLimitPlaneStatus(self, object_tag: Tag, status: UF.ParamLwplaneStatus) -> None:
        ...
    def AskLowerLimitPlaneTag(self, object_tag: Tag, target_tag: Tag) -> None:
        ...
    def AskLowerLimitPlaneUsage(self, object_tag: Tag, usage: UF.ParamLwplaneUsage) -> None:
        ...
    def AskMachToolDbObject(self, db_obj: int) -> None:
        ...
    def AskOptTemplateObject(self, opt_object: int) -> None:
        ...
    def AskPostTemplateName(self, post_template_filename: str) -> None:
        ...
    def AskToolMatlDbObject(self, db_obj: int) -> None:
        ...
    def InitSession(self) -> None:
        ...
    def IsSessionInitialized(self, answer: bool) -> None:
        ...
    def OptAddTemplatePart(self, filespec: str) -> None:
        ...
    def OptAddType(self, filespec: str) -> None:
        ...
    def OptAskClsfNames(self, count: int, names: str) -> None:
        ...
    def OptAskDocNames(self, count: int, names: str) -> None:
        ...
    def OptAskObject(self, subtype_class: UF.UFCam.OptStypeCls, type: str, subtype: str, param: Tag) -> None:
        ...
    def OptAskPostNames(self, count: int, names: str) -> None:
        ...
    def OptAskSubtypes(self, opt_type_name: str, subtype_class: UF.UFCam.OptStypeCls, count: int, subtypes: str) -> None:
        ...
    def OptAskTypes(self, count: int, type_names: str) -> None:
        ...
    def ReinitOpt(self, template_filename: str) -> None:
        ...
    def ReinitSession(self, config_file: str) -> None:
        ...
    def SetAutoBlank(self, object_tag: Tag, geom_type: UF.UFCam.BlankGeomType, offset: float) -> None:
        ...
    def SetCamPreferences(self, prefs: UF.UFCam.Preferences) -> None:
        ...
    def SetClearPlaneData(self, object_tag: Tag, origin: float, normal: float) -> None:
        ...
    def SetClearPlaneStatus(self, object_tag: Tag, status: UF.ParamClrplaneStatus) -> None:
        ...
    def SetClearPlaneTag(self, object_tag: Tag, target_tag: Tag) -> None:
        ...
    def SetClearPlaneUsage(self, object_tag: Tag, usage: UF.ParamClrplaneUsage) -> None:
        ...
    def SetLowerLimitPlaneData(self, object_tag: Tag, origin: float, normal: float) -> None:
        ...
    def SetLowerLimitPlaneStatus(self, object_tag: Tag, status: UF.ParamLwplaneStatus) -> None:
        ...
    def SetLowerLimitPlaneTag(self, object_tag: Tag, target_tag: Tag) -> None:
        ...
    def SetLowerLimitPlaneUsage(self, object_tag: Tag, usage: UF.ParamLwplaneUsage) -> None:
        ...
    def SetMaterial(self, object_tag: Tag, libref: str) -> None:
        ...
    def UpdateListObjectCustomization(self, object_tags: Tag) -> None:
        ...
    def UpdateSingleObjectCustomization(self, object_tag: Tag) -> None:
        ...
    def WizardAskCurrentObject(self, param_tag: Tag) -> None:
        ...
    def WizardSetCurrentObject(self, param_tag: Tag) -> None:
        ...


    class UFCamPreferences():
        blank_geom_color: int
        blank_geom_type: int
        check_geom_color: int
        check_geom_type: int
        clearance_geom_color: int
        clsf_decimal_place: int
        clsf_replay_advanced: bool
        clsf_replay_refresh: bool
        clsf_replay_vericut: bool
        clsf_type: int
        collect_instances: bool
        create_tool_lib_entry: bool
        cut_area_geom_color: int
        cut_area_geom_type: int
        delete_param_set: bool
        drive_geom_color: int
        generate_instance: bool
        info_csys: int
        macro_only: bool
        mcs_link_to_rcs: int
        mcs_stat: int
        parent_display: bool
        part_geom_color: int
        part_geom_type: int
        pause_aft_path: bool
        rcs_disp_stat: int
        rcs_inv_matrix: float
        rcs_map_stat: int
        rcs_origin: float
        rcs_stat: int
        refresh_bef_path: bool
        show_edited_status: bool
        show_standard_type: bool
        show_template_type: bool
        show_tool_name: bool
        template_tool: bool
        toolpath_only: bool
        template_set_used: str
        transform_toolpath: bool
        trim_geom_color: int
        uncut_geom_color: int
        unlink_instance: bool
        use_customized_interface: bool
        visible_scrollable_items: int
        automatically_update_when_loading: bool
    

    class OptStypeCls(enum.Enum):
        OptStypeClsSetup = 0
        OptStypeClsOper = 1
        OptStypeClsProg = 2
        OptStypeClsTool = 3
        OptStypeClsMethod = 4
        OptStypeClsGeom = 5
        OptStypeClsLast = 6
    

    class BlankGeomType(enum.Enum):
        FeatureGeomType = 0
        GeometryGeomType = 1
        FacetGeomType = 2
        AutoBlockType = 3
        OffsetFromPartType = 4
    



    class TopoSource(enum.Enum):
        AppBodySource = 0
        AppTrimsurfSource = 1
        UgoBodySource = 2
        UgoTrimsurfSource = 3
    

    class Orientation(enum.Enum):
        OrientationReverse = -1
        OrientationNone = 0
        OrientationForward = 1
    

    class UFBrepOptions():
        count: int
        options: int
        opt_data: float
    

    class UFBrepMapping():
        count: int
        source: typing.List[UF.UFBrep.GeomType]
        extracted: typing.List[UF.UFBrep.GeomType]
    

    class GeomType(enum.Enum):
        GeomAll = 0
        PointGeom = 1
        CurveAll = 100
        LineGeom = 101
        SplineGeom = 102
        ArcGeom = 103
        EllipseGeom = 104
        HyperbolaGeom = 105
        ParabolaGeom = 106
        IntersectionGeom = 107
        CompositeGeom = 108
        SurfaceAll = 200
        CylinderGeom = 201
        ConeGeom = 202
        SphereGeom = 203
        TorusGeom = 204
        RevolveGeom = 205
        ExtrudeGeom = 206
        BsurfaceGeom = 207
        OffsetGeom = 208
        PlaneGeom = 209
        BlendGeom = 210
        ForsurfGeom = 211
        SpecialBase = 300
        UvboxGeom = 301
        TagGeom = 302
    

    

class UFBound(Utilities.NXRemotableObject):
    def AskBoundaryData(self, boundary_tag: Tag, boundary_data: UF.UFBound.AllData) -> None:
        ...
    def AskNumberOfBoundaries(self, _object: Tag, no_of_members: int) -> None:
        ...
    def CreateBoundary(self, open_closed_flag: int, view_tag: Tag, tol: UF.UFBound.Tolerance, num_members: int, object_list: typing.List[UF.UFBound.Object], bound_tag: Tag) -> None:
        ...


    class UFBoundTolerance():
        tol_specified: int
        into_tolerance: float
        out_tolerance: float
    

    class UFBoundObject():
        object_tag: Tag
        on_tangent_to_flag: int
    

    class UFBoundMemberData():
        member_tag: Tag
        on_tangent_to_flag: int
        contiguity_flag: int
        parameter_range: float
        midpoint: float
        direction_vec: float
    

    class UFBoundAllData():
        num_members: int
        open_closed_flag: int
        plane_matrix: Tag
        minimum_distance: float
        maxmin_box: float
        tolerance: float
        members_data: typing.List[UF.UFBound.MemberData]
    

class UFAttr(Utilities.NXRemotableObject):
    def AskLocked(self, _object: Tag, title: str, locked: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def AskPartAttribute(self, attribute: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CountAttributes(self, _object: Tag, type: int, count: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def CountUserAttributeTitles(self, _object: Tag, iter: UF.UFAttr.Iterator, count: int) -> None:
        ...
    def CountUserAttributes(self, _object: Tag, iter: UF.UFAttr.Iterator, count: int) -> None:
        ...
    def Delete(self, _object: Tag, type: int, title: str) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DeleteAll(self, _object: Tag, type: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def DeleteUserAttributeWithTitleAndType(self, _object: Tag, title: str, type: int, index: int, update: bool) -> None:
        ...
    def DeleteUserAttributes(self, _object: Tag, iter: UF.UFAttr.Iterator, update: bool) -> None:
        ...
    def FindAttribute(self, _object: Tag, type: int, title: str, title_type: int) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def FreeUserAttributeInfoArray(self, count: int, info: typing.List[UF.UFAttr.Info]) -> None:
        ...
    def FreeUserAttributeInfoStrings(self, info: UF.UFAttr.Info) -> None:
        ...
    def FreeUserAttributeIteratorStrings(self, iterator: UF.UFAttr.Iterator) -> None:
        ...
    def GetBoolUserAttribute(self, _object: Tag, title: str, index: int, value: bool, has_attribute: bool) -> None:
        ...
    def GetComputationalTimeUserAttribute(self, _object: Tag, title: str, index: int, value: int, has_attribute: bool) -> None:
        ...
    def GetIntegerUserAttribute(self, _object: Tag, title: str, index: int, value: int, has_attribute: bool) -> None:
        ...
    def GetNextUserAttribute(self, _object: Tag, iter: UF.UFAttr.Iterator, info: UF.UFAttr.Info, has_attribute: bool) -> None:
        ...
    def GetNullUserAttribute(self, _object: Tag, title: str, index: int, has_attribute: bool) -> None:
        ...
    def GetRealUserAttribute(self, _object: Tag, title: str, index: int, value: float, unit_type: Tag, has_attribute: bool) -> None:
        ...
    def GetReferenceStringOfUserAttribute(self, _object: Tag, title: str, index: int, reference_string: str, has_attribute: bool) -> None:
        ...
    def GetStringTimeUserAttribute(self, _object: Tag, title: str, index: int, time_string: str, has_attribute: bool) -> None:
        ...
    def GetStringUserAttribute(self, _object: Tag, title: str, index: int, string_value: str, has_attribute: bool) -> None:
        ...
    def GetUserAttribute(self, _object: Tag, iter: UF.UFAttr.Iterator, info: UF.UFAttr.Info, has_attribute: bool) -> None:
        ...
    def GetUserAttributeLock(self, _object: Tag, iter: UF.UFAttr.Iterator, is_locked: bool, has_attribute: bool) -> None:
        ...
    def GetUserAttributeLockWithTitleAndType(self, _object: Tag, title: str, type: int, index: int, is_locked: bool, has_attribute: bool) -> None:
        ...
    def GetUserAttributeWithTitleAndType(self, _object: Tag, title: str, type: int, index: int, info: UF.UFAttr.Info, has_attribute: bool) -> None:
        ...
    def GetUserAttributes(self, _object: Tag, iter: UF.UFAttr.Iterator, num_attributes: int, info: typing.List[UF.UFAttr.Info]) -> None:
        ...
    def GetUserAttributesInFile(self, part_name: str, iter: UF.UFAttr.Iterator, num_attributes: int, info: typing.List[UF.UFAttr.Info]) -> None:
        ...
    def HasUserAttribute(self, _object: Tag, iter: UF.UFAttr.Iterator, has_attribute: bool) -> None:
        ...
    def HasUserAttributeWithTitleAndType(self, _object: Tag, title: str, type: int, index: int, has_attribute: bool) -> None:
        ...
    def InitUserAttributeInfo(self, info: UF.UFAttr.Info) -> None:
        ...
    def InitUserAttributeIterator(self, iter: UF.UFAttr.Iterator) -> None:
        ...
    def ReleaseUserAttributeIterator(self, iter: UF.UFAttr.Iterator) -> None:
        ...
    def SetBoolUserAttribute(self, _object: Tag, title: str, index: int, value: bool, update: bool) -> None:
        ...
    def SetComputationalTimeUserAttribute(self, _object: Tag, title: str, index: int, value: int, update: bool) -> None:
        ...
    def SetIntegerUserAttribute(self, _object: Tag, title: str, index: int, value: int, update: bool) -> None:
        ...
    def SetLocked(self, _object: Tag, title: str, locked: bool) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def SetNullUserAttribute(self, _object: Tag, title: str, index: int, update: bool) -> None:
        ...
    def SetRealUserAttribute(self, _object: Tag, title: str, index: int, value: float, unit_type: Tag, update: bool) -> None:
        ...
    def SetReferenceStringUserAttribute(self, _object: Tag, title: str, index: int, reference_string: str, update: bool) -> None:
        ...
    def SetStringTimeUserAttribute(self, _object: Tag, title: str, index: int, value: str, update: bool) -> None:
        ...
    def SetStringUserAttribute(self, _object: Tag, title: str, index: int, value: str, update: bool) -> None:
        ...
    def SetTimeStringFormat(self, new_format: str, old_format: str) -> None:
        ...
    def SetUserAttribute(self, _object: Tag, info: UF.UFAttr.Info, update: bool) -> None:
        ...
    def SetUserAttributeLockWithTitleAndType(self, objectTag: Tag, title: str, type: int, _lock: bool) -> None:
        ...
    def SetUserAttributeLocks(self, _object: Tag, iter: UF.UFAttr.Iterator, locked: bool) -> None:
        ...


    class UFAttrIterator():
        category: str
        check_category: bool
        title: str
        type: int
        index: int
        include_also_unset: bool
        include_only_unset: bool
        include_only_pdm_based: bool
        __initialized: int
    

    class UFAttrInfo():
        type: int
        category: str
        title: str
        alias: str
        bool_value: bool
        integer_value: int
        real_value: float
        unit_type: Tag
        unit_name: str
        expression: Tag
        string_value: str
        time_value: int
        time_string: str
        reference_string: str
        inherited: bool
        _override: bool
        locked: bool
        owned_by_system: bool
        required: bool
        unset: bool
        array: bool
        index: int
        pdm_based: bool
        __initialized: int
    

class UFAssem(Utilities.NXRemotableObject):
    def ActivateSequence(self, sequence: Tag) -> None:
        ...
    def AddPartToAssembly(self, parent_part: Tag, part: str, refset_name: str, instance_name: str, origin: float, csys_matrix: float, layer: int, instance: Tag, error_status: UF.UFPart.LoadStatus) -> None:
        ...
    def AddRefSetMembers(self, ref_set: Tag, member_count: int, ref_set_members: typing.List[Tag]) -> None:
        ...
    def AddSequencingView(self, view: Tag) -> None:
        ...
    def AddToCset(self, cset: Tag, component: Tag, level: bool) -> None:
        ...
    def ApplyToCset(self, cset: Tag, fn: UF.UFAssem.CsetFnT, app_data: int) -> None:
        ...
    def ApplyToCsetMembers(self, cset: Tag, fn: UF.UFAssem.CsetFnT, app_data: int) -> None:
        ...
    def AskActiveArrangement(self, part: Tag, arrangement: Tag) -> None:
        ...
    def AskActiveSequence(self, sequence: Tag) -> None:
        ...
    def AskAllCompCset(self, part: Tag, cset: Tag) -> None:
        ...
    def AskAllPartOccChildren(self, part_occur: Tag, child_part_occs: typing.List[Tag]) -> int:
        ...
    def AskArrangementsInPart(self, part: Tag, n_arrangements: int, arrangements: typing.List[Tag]) -> None:
        ...
    def AskArraysInPart(self, part_tag: Tag, num_arrays: int, array_tags: typing.List[Tag]) -> None:
        ...
    def AskArraysOfInst(self, instance: Tag, num_arrays: int, arrays: typing.List[Tag]) -> None:
        ...
    def AskAssemLoadOptions(self, options: UF.UFAssem.LoadOptions) -> None:
        ...
    def AskAssemOptions(self, options: UF.UFAssem.Options) -> None:
        ...
    def AskAutoAddNewComps(self, ref_set: Tag, add_new_comps: bool) -> None:
        ...
    def AskBodiesOfAssemblyCut(self, frec: Tag, n_target_bodies: int, target_body_tags: typing.List[Tag], n_tool_bodies: int, tool_body_tags: typing.List[Tag]) -> None:
        ...
    def AskChildOfInstance(self, instance: Tag) -> Tag:
        ...
    def AskCompExplosion(self, explosion: Tag, component: Tag, status: UF.UFAssem.ExplStatus, transform: float) -> None:
        ...
    def AskCompPosition(self, explosion: Tag, component: Tag, transform: float) -> None:
        ...
    def AskComponentData(self, component: Tag, part_name: str, refset_name: str, instance_name: str, origin: float, csys_matrix: float, transform: float) -> None:
        ...
    def AskCostOfSequence(self, sequence: Tag, cost: float) -> None:
        ...
    def AskCostOfStep(self, step: Tag, cost: float) -> None:
        ...
    def AskCurrentFrame(self, sequence: Tag, current_frame: int) -> None:
        ...
    def AskCurrentStep(self, sequence: Tag, step: Tag) -> None:
        ...
    def AskDefaultArrangement(self, part: Tag, arrangement: Tag) -> None:
        ...
    def AskDefaultRefSets(self, n_ref_sets: int, default_ref_sets: str) -> None:
        ...
    def AskDeformableDefinition(self, part: Tag, deformable_feature: Tag) -> None:
        ...
    def AskDeformableDefinitionData(self, deformable_feature_tag: Tag, deform_data: UF.UFAssem.DeformData) -> None:
        ...
    def AskDeformedDefinitionData(self, deformed_feature_tag: Tag, deformed_data: UF.UFAssem.DeformedDefinitionData) -> None:
        ...
    def AskDisplayedDeformationOfPartOcc(self, part_occ: Tag, deformed_feature: Tag) -> None:
        ...
    def AskExplodedObject(self, explosion: Tag, old_object: Tag, new_object: Tag) -> None:
        ...
    def AskExplosionVector(self, component: Tag, vector: float) -> None:
        ...
    def AskExplosions(self, part_tag: Tag, n_explosions: int, explosion_tags: typing.List[Tag]) -> None:
        ...
    def AskHiddenComps(self, view: Tag, components: typing.List[Tag], count: int) -> None:
        ...
    def AskInstOfPartOcc(self, part_occur: Tag) -> Tag:
        ...
    def AskInstanceIntent(self, instance: Tag, instance_intent: UF.UFAssem.InstanceIntent) -> None:
        ...
    def AskInstanceOfName(self, parent_part: Tag, instance_name: str) -> Tag:
        ...
    def AskIsetArrayData(self, array: Tag, array_data: UF.UFAssem.IsetArrayData, components: typing.List[Tag]) -> None:
        ...
    def AskLastFilter(self, part: Tag, filter_tag: Tag, cset_tag: Tag) -> None:
        ...
    def AskMcArrayData(self, array: Tag, array_data: UF.UFAssem.McArrayData, components: typing.List[Tag]) -> None:
        ...
    def AskNameOfArrangement(self, arrangement: Tag, name: str) -> None:
        ...
    def AskOccsOfEntity(self, _object: Tag, occurrences: typing.List[Tag]) -> int:
        ...
    def AskOccsOfPart(self, parent_part: Tag, part: Tag, part_occs: typing.List[Tag]) -> int:
        ...
    def AskOrientation(self, ref_set_tag: Tag, origin: float, orientation: float) -> None:
        ...
    def AskParentComponent(self, occur: Tag, parent: Tag) -> None:
        ...
    def AskParentOfInstance(self, instance: Tag) -> Tag:
        ...
    def AskPartNameOfChild(self, instance: Tag, part_fspec: str) -> None:
        ...
    def AskPartOccChildren(self, part_occur: Tag, child_part_occs: typing.List[Tag]) -> int:
        ...
    def AskPartOccOfInst(self, parent_part_occ: Tag, instance: Tag) -> Tag:
        ...
    def AskPartOccSuppressState(self, part_occ: Tag, suppressed: bool, parent_suppressed: bool) -> None:
        ...
    def AskPartOccsOfInst(self, instance: Tag, part_occs: typing.List[Tag]) -> int:
        ...
    def AskPartOccurrence(self, occurrence: Tag) -> Tag:
        ...
    def AskPartOccurrenceOfStep(self, step: Tag, num_part_occs: int, part_occs: typing.List[Tag]) -> None:
        ...
    def AskPrototypeOfOcc(self, occurrence: Tag) -> Tag:
        ...
    def AskRefSetData(self, ref_set: Tag, ref_set_name: str, origin: float, matrix: float, num_members: int, members: typing.List[Tag]) -> None:
        ...
    def AskRefSetMembers(self, ref_set: Tag, ret_count: int, members: typing.List[Tag]) -> None:
        ...
    def AskRefSets(self, ref_set_member: Tag, num_ref_sets: int, ref_sets: typing.List[Tag]) -> None:
        ...
    def AskRootPartOcc(self, part: Tag) -> Tag:
        ...
    def AskSaveTrueshape(self, save_trueshape_data: bool) -> None:
        ...
    def AskSequenceDescription(self, sequence: Tag, desc: str) -> None:
        ...
    def AskSequenceDuration(self, sequence: Tag, duration: int) -> None:
        ...
    def AskSequenceName(self, sequence: Tag, name: str) -> None:
        ...
    def AskSequenceType(self, sequence: Tag, seq_type: int) -> None:
        ...
    def AskSequencesInPart(self, part: Tag, num_sequences: int, sequences: typing.List[Tag]) -> None:
        ...
    def AskStableIdOfInstance(self, instance_tag: Tag, stable_id: str) -> None:
        ...
    def AskStepDuration(self, step: Tag, duration: int) -> None:
        ...
    def AskStepElementDurations(self, step: Tag, num_durations: int, durations: int) -> None:
        ...
    def AskStepIncrement(self, sequence: Tag, increment: int) -> None:
        ...
    def AskStepNumber(self, step: Tag, ask_step_number: int) -> None:
        ...
    def AskStepType(self, step: Tag, step_type: int) -> None:
        ...
    def AskSteps(self, sequence: Tag, num_steps: int, steps: typing.List[Tag]) -> None:
        ...
    def AskStepsOfPartOcc(self, sequence: Tag, part_occ: Tag, num_steps: int, steps: typing.List[Tag]) -> None:
        ...
    def AskSuppressState(self, instance: Tag, suppressed: bool) -> None:
        ...
    def AskSuppressionExp(self, instance: Tag, exp: Tag) -> None:
        ...
    def AskTimeOfSequence(self, sequence: Tag, time: float) -> None:
        ...
    def AskTimeOfStep(self, step: Tag, time: float) -> None:
        ...
    def AskTransformOfOcc(self, occurrence: Tag, transform: float) -> None:
        ...
    def AskTypeOfArray(self, array: Tag, type: int) -> None:
        ...
    def AskUnprocessedPartoccs(self, sequence: Tag, num_unprocessed_partoccs: int, unprocessed_partoccs: typing.List[Tag]) -> None:
        ...
    def AskUsedArrangement(self, component: Tag, arrangement: Tag) -> None:
        ...
    def AskViewExplosion(self, view: Tag, explosion: Tag) -> None:
        ...
    def AskWorkOccurrence(self) -> Tag:
        ...
    def AskWorkPart(self) -> Tag:
        ...
    def CaptureArrangementFromCurrentSequence(self, arrangement_name: str, arrangement: Tag, warnings_count: int, warnings: int) -> None:
        ...
    def CaptureArrangementFromCurrentSequenceExtended(self, arrangement_name: str, ignore_constraints: bool, arrangement: Tag, warnings_count: int, warnings: int) -> None:
        ...
    def CheckArrayStatus(self, array: Tag) -> None:
        ...
    def ConvertPrev16Aligns(self, n_aligns_to_convert: int, aligns_to_convert: UF.UFAssem.Prev16Align, n_messages: int, messages: typing.List[UF.UFAssem.Prev16Align]) -> None:
        ...
    def CopyExplosion(self, source_explosion: Tag, source_component: Tag, destination_explosion: Tag, destination_component: Tag) -> None:
        ...
    def CountEntsInPartOcc(self, part_occur: Tag) -> None:
        ...
    def CountObjsInComp(self, comp_tag: Tag, returned_count: int) -> None:
        ...
    def CountRefSetsIn(self, _object: Tag) -> None:
        ...
    def CreateAssemblyCut(self, part: Tag, blank_tool_bodies: bool, n_target_body_occs: int, target_body_occs: typing.List[Tag], n_tool_bodies: int, tool_bodies: typing.List[Tag], acut_tag: Tag) -> None:
        ...
    def CreateComponentPart(self, parent_part: Tag, new_part_name: str, refset_name: str, instance_name: str, units: int, layer: int, origin: float, csys_matrix: float, n_objects: int, objects: typing.List[Tag], instance: Tag) -> None:
        ...
    def CreateConstrainedIsetArray(self, array_data: UF.UFAssem.IsetArrayData, array: Tag) -> None:
        ...
    def CreateCset(self, part: Tag, name: str, _object: Tag) -> None:
        ...
    def CreateDeformablePart(self, data: UF.UFAssem.DeformData, deformable_feature: Tag) -> None:
        ...
    def CreateExplosion(self, display_part_tag: Tag, explosion_name: str, explosion_tag: Tag) -> None:
        ...
    def CreateIsetArray(self, array_data: UF.UFAssem.IsetArrayData, array: Tag) -> None:
        ...
    def CreateMcArray(self, array_data: UF.UFAssem.McArrayData, array: Tag) -> None:
        ...
    def CreateRefSet(self, ref_set_name: str, origin: float, matrix: float, ref_set_members: typing.List[Tag], num_members: int, ref_set_tag: Tag) -> None:
        ...
    def CreateSequence(self, name: str, part: Tag, sequence: Tag) -> None:
        ...
    def CreateStep(self, sequence: Tag, part_occurrence: Tag, step_type: int, time: float, cost: float, description: str, insert_at_step: Tag, step: Tag) -> None:
        ...
    def CreateTypedSequence(self, name: str, sequence_type: int, part: Tag, sequence: Tag) -> None:
        ...
    def CycleEntsInPartOcc(self, part_occur: Tag, object_occur: Tag) -> Tag:
        ...
    def CycleInstOfPart(self, part: Tag, instance: Tag) -> Tag:
        ...
    def CycleObjsInComp(self, component: Tag, member: Tag) -> None:
        ...
    def DeformPart(self, deform_data: UF.UFAssem.DeformPartData, deform_warnings: UF.UFAssem.DeformPartWarnings) -> None:
        ...
    def DeleteArray(self, array: Tag, delete_all: bool) -> None:
        ...
    def DeleteExplosion(self, explosion: Tag) -> None:
        ...
    def DeleteSequence(self, sequence: Tag) -> None:
        ...
    def DeleteStep(self, step: Tag) -> None:
        ...
    def EditAssemblyCut(self, frec_tag: Tag, n_target_bodies: int, target_body_tags: typing.List[Tag], n_tool_bodies: int, tool_body_tags: typing.List[Tag], blank_tool_bodies: bool) -> None:
        ...
    def EditIsetArray(self, array: Tag, array_data: UF.UFAssem.IsetArrayData) -> None:
        ...
    def EditMcArray(self, array: Tag, array_data: UF.UFAssem.McArrayData) -> None:
        ...
    def EditRefSetData(self, ref_set_tag: Tag, origin: float, matrix: float) -> None:
        ...
    def EnsureChildLoaded(self, instance: Tag, load_status: UF.UFPart.LoadStatus) -> None:
        ...
    def EvalInstanceIntent(self, instance: Tag, apply_result: bool, instance_status: UF.UFAssem.InstanceStatus) -> None:
        ...
    def ExplodeComponent(self, explosion: Tag, part_occurrence: Tag, transform: float) -> None:
        ...
    def FindImmedOldComps(self, part: Tag, immediate_components: typing.List[Tag], n_immediate_components: int) -> None:
        ...
    def FindOccurrence(self, part_occur: Tag, object_prototype: Tag) -> Tag:
        ...
    def FindPrev16AlignsToCheck(self, part_tag: Tag, recurse: bool, n_aligns_to_check: int, aligns_to_check: typing.List[UF.UFAssem.Prev16Align]) -> None:
        ...
    def FreeDeformWarningsData(self, warnings: UF.UFAssem.DeformPartWarnings) -> None:
        ...
    def FreePrev16Aligns(self, n_aligns: int, aligns: UF.UFAssem.Prev16Align) -> None:
        ...
    def GetOccInWorkOcc(self, part_occ: Tag, occ_in_work: Tag) -> None:
        ...
    def GetRefSetInst(self, _object: Tag, number: int) -> Tag:
        ...
    def HideComponent(self, component: Tag, view: Tag) -> None:
        ...
    def IgnorePartOcc(self, sequence: Tag, part_occ: Tag) -> None:
        ...
    def InitDeformPartData(self, deform_part: UF.UFAssem.DeformPartData) -> None:
        ...
    def InitializeSequencing(self) -> None:
        ...
    def InitializeSequencingKeepLayout(self) -> None:
        ...
    def IsComponentNgc(self, component_tag: Tag) -> bool:
        ...
    def IsIgnored(self, sequence: Tag, part_occ: Tag, ignored: bool) -> None:
        ...
    def IsMemberOfCset(self, cset: Tag, component: Tag, result: bool) -> None:
        ...
    def IsOccurrence(self, entity: Tag) -> bool:
        ...
    def IsPartDeformable(self, part: Tag) -> bool:
        ...
    def IsPartOccurrence(self, occurrence: Tag) -> bool:
        ...
    def IsPreassembled(self, sequence: Tag, part_occ: Tag, preassembled: bool) -> None:
        ...
    def IsRefSetMember(self, potential_member: Tag, member_flag: bool) -> None:
        ...
    def MakeCurrentStep(self, step: Tag) -> None:
        ...
    def MoveStep(self, step_to_be_moved: Tag, insert_at_step: Tag) -> None:
        ...
    def OccIsInWorkPart(self, part_occ: Tag, is_in_work: bool) -> None:
        ...
    def PartIsDescendant(self, parent_part: Tag, descendent_part: Tag) -> bool:
        ...
    def PlaybackAnimateToFrame(self, sequence: Tag, target_frame: int, frame_skip: int) -> None:
        ...
    def PlaybackSeekToFrame(self, sequence: Tag, target_frame: int) -> None:
        ...
    def PlaybackSequence(self, sequence: Tag, playback_command: int) -> None:
        ...
    def PreassemblePartocc(self, sequence: Tag, part_occ: Tag) -> None:
        ...
    def RegisterAnimationCallback(self, callback: UF.UFAssem.AnimationCallbackFT, user_data: int) -> None:
        ...
    def RemoveFromCset(self, cset: Tag, component: Tag) -> None:
        ...
    def RemoveIgnored(self, sequence: Tag, part_occ: Tag) -> None:
        ...
    def RemoveInstance(self, instance: Tag) -> None:
        ...
    def RemovePreassembled(self, sequence: Tag, part_occ: Tag) -> None:
        ...
    def RemoveRefSetMembers(self, ref_set: Tag, member_count: int, ref_set_members: typing.List[Tag]) -> None:
        ...
    def RemoveSequencingView(self, view: Tag) -> None:
        ...
    def RenameInstance(self, instance: Tag, new_name: str) -> None:
        ...
    def ReplaceRefset(self, count: int, target_tags: typing.List[Tag], new_refset_name: str) -> None:
        ...
    def RepositionInstance(self, instance: Tag, new_origin: float, new_csys_matrix: float) -> None:
        ...
    def RepositionPartOccurrence(self, part_occ: Tag, xform: float, option: UF.UFAssem.LevelOption) -> None:
        ...
    def RestoreLoadOptions(self, load_options_file: str) -> None:
        ...
    def RestoreWorkPartContextQuietly(self, previous_work_part_context: int) -> None:
        ...
    def RevertExplodeComp(self, explosion: Tag, component: Tag) -> None:
        ...
    def SetActiveArrangement(self, arrangement: Tag) -> None:
        ...
    def SetAssemLoadOptions(self, options: UF.UFAssem.LoadOptions) -> None:
        ...
    def SetAssemOptions(self, options: UF.UFAssem.Options) -> None:
        ...
    def SetAutoAddNewComps(self, ref_set: Tag, add_new_comps: bool) -> None:
        ...
    def SetCostOfStep(self, step: Tag, assign_cost: float) -> None:
        ...
    def SetDefaultArrangement(self, arrangement: Tag) -> None:
        ...
    def SetDefaultRefSets(self, n_ref_sets: int, default_ref_sets: str) -> None:
        ...
    def SetInstanceIntent(self, instance: Tag, instance_intent: UF.UFAssem.InstanceIntent) -> None:
        ...
    def SetRefSetByCset(self, cset: Tag, cname: str) -> None:
        ...
    def SetSaveTrueshape(self, save_trueshape_data: bool) -> None:
        ...
    def SetSearchDirectories(self, count: int, dir_list: str, sub_dir: bool) -> None:
        ...
    def SetSequenceDescription(self, sequence: Tag, desc: str) -> None:
        ...
    def SetSequenceName(self, sequence: Tag, name: str) -> None:
        ...
    def SetStepIncrement(self, sequence: Tag, increment: int) -> None:
        ...
    def SetSuppressionExp(self, instance: Tag, exp_string: str, exp_tag: Tag) -> None:
        ...
    def SetTimeOfStep(self, step: Tag, assign_time: float) -> None:
        ...
    def SetUsedArrangement(self, component: Tag, arrangement: Tag) -> None:
        ...
    def SetViewExplosion(self, view: Tag, explosion: Tag) -> None:
        ...
    def SetWorkOccurrence(self, part_occur: Tag) -> None:
        ...
    def SetWorkPart(self, part: Tag) -> None:
        ...
    def SetWorkPartContextQuietly(self, part_tag: Tag, previous_work_part_context: int) -> None:
        ...
    def SetWorkPartQuietly(self, part: Tag, previous_work_part: Tag) -> None:
        """[Obsolete("Deprecated")"""
        ...
    def ShowComponent(self, component: Tag, view: Tag) -> None:
        ...
    def SubstituteComponent(self, instance: Tag, new_part_version: str, new_comp_name: str, new_refset_name: str, layer: int, load_status: UF.UFPart.LoadStatus) -> None:
        ...
    def SuppressArray(self, array: Tag) -> None:
        ...
    def SuppressInstances(self, n_instances: int, instances: typing.List[Tag], failures: int) -> None:
        ...
    def TerminateSequencing(self) -> None:
        ...
    def UnexplodeComponent(self, explosion: Tag, part_occurrence: Tag) -> None:
        ...
    def UnsetSuppressionExp(self, instance: Tag) -> None:
        ...
    def UnsuppressArray(self, array: Tag) -> None:
        ...
    def UnsuppressInstances(self, n_instances: int, instances: typing.List[Tag], failures: int) -> None:
        ...
    def UpdateComponentGroup(self, part_tag: Tag, component_group_name: str, do_update_structure: bool) -> None:
        ...
    def UpgradeToInstances(self, part: Tag, n_components: int, components: typing.List[Tag], recurse: bool, create_component: bool, upgrade_status: UF.UFAssem.UpgradeStatus) -> bool:
        ...
    def UseAlternate(self, instance: Tag, new_part: str, new_comp_name: str, new_refset_name: str, load_status: UF.UFPart.LoadStatus) -> None:
        ...
    def WhereIsPartUsed(self, part: Tag, parent_parts: typing.List[Tag]) -> int:
        ...
    def WhereUsedReport(self, comp_name: str, dir: str, search_opt: int, do_all_levels: bool, load_status: UF.UFPart.LoadStatus) -> None:
        ...


    class UFAssemUpgradeStatus():
        failed: bool
        n_components: int
        component_names: str
        statuses: int
    

    class UFAssemPrev16Align():
        part: Tag
        condition_tag: Tag
        condition_name: str
        constraint_index: int
        constraint_name: str
        offset: Tag
        offset_name: str
        offset_value: float
        message: str
        reason: str
    

    class UFAssemOptions():
        load_options: int
        parts_list: int
        update: int
        emphasize: int
        emphasize_color: int
        failure_action: int
        maintain_work_part: int
        load_latest: int
        load_components: int
        load_fully: int
        use_lightweight_representations: int
        load_substitution: int
        apply_to_all_levels: int
        load_wave_data: int
        load_wave_parents: int
        auto_regen_pfm_option: int
        managed_mode_load_options: int
    

    class UFAssemMcArrayData():
        array_subtype: int
        master_component: Tag
        template_component: Tag
        dimensions: typing.List[Tag]
        axis_definitions: typing.List[Tag]
        offsets: typing.List[Tag]
        array_name: str
    

    class UFAssemLoadOptions():
        load_options: int
        failure_action: int
        load_latest: int
        load_components: int
        part_load_option: int
        load_substitution: int
        apply_to_all_levels: int
        load_wave_data: int
        load_wave_parents: int
        auto_regen_pfm_option: int
        managed_mode_load_options: int
    

    class LevelOption(enum.Enum):
        UseStrictLevel = 0
        UseExistingLevel = 1
        EstablishOverride = 2
    

    class UFAssemIsetArrayData():
        feature_iset: Tag
        template_component: Tag
        dimensions: int
        array_name: str
    

    class UFAssemInstanceStatus():
        child_changed: bool
        current_child: Tag
        previous_child: Tag
        info: str
    

    class UFAssemInstanceIntent():
        fam_intent: typing.List[UF.UFFam.IntentData]
    

    class ExplStatus(enum.Enum):
        Unexploded = 0
        Exploded = 1
        RevertExploded = 2
    

    class UFAssemDeformPartWarnings():
        num_warnings: int
        expressions_with_warnings: typing.List[Tag]
        warning_codes: int
        warning_strings: str
    

    class UFAssemDeformPartData():
        convert_units_on_modified_parts: bool
        convert_units_on_read_only_modified_parts: bool
        part_occ_to_deform: Tag
        num_parents: int
        old_parents: typing.List[Tag]
        new_parents: typing.List[Tag]
        num_expressions: int
        old_expressions: typing.List[Tag]
        new_expression_values: str
        deformed_feature_tag: Tag
    

    class UFAssemDeformedDefinitionData():
        part_occ: Tag
        parents: typing.List[Tag]
        parent_prompts: str
        num_parents: int
        expressions: typing.List[Tag]
        expression_prompts: str
        num_expressions: int
        help_string: str
    

    class UFAssemDeformData():
        part_occ: Tag
        udfs_data: typing.List[UF.UFModl.UdfsDefData]
        help_url_string: str
    

    

    

class UFAbort(Utilities.NXRemotableObject):
    def AskFlagStatus(self, flag: bool) -> None:
        ...
    def ClearAbort(self) -> None:
        ...
    def DisableAbort(self) -> None:
        ...
    def EnableAbort(self) -> None:
        ...


class UF(Utilities.NXRemotableObject):
    def AddCallbackFunction(self, reason: UF.CallbackReason, fn: UF.UF.CallbackFnT, user_data: int, function_id: int) -> None:
        ...
    def AllocateMemory(self, nbytes: int) -> int:
        ...
    def AskApplicationModule(self, module_id: int) -> None:
        ...
    def AskCodeset(self, codeset: UF.Codeset) -> None:
        ...
    def AskGripArgs(self, argument_count: int, gruf_arg_list: UF.Args) -> None:
        ...
    def AskLoadStateForPartFile(self, partFileName: str, loadState: UF.PartLoadState) -> None:
        ...
    def AskLoadStateOfPart(self, part: Tag, loadState: UF.PartLoadState) -> None:
        ...
    def AskSyslogFilename(self, filename: str) -> None:
        ...
    def AskSystemInfo(self, info: UF.SystemInfo) -> None:
        ...
    def BeginTimer(self, timer: int) -> None:
        ...
    def DecodeAuthFile(self, key: int, input_file: str, out_mem: int) -> None:
        ...
    def EncodeAuthFile(self, key: int, input_file: str, output_file: str) -> None:
        ...
    def EndTimer(self, timer: int, values: UF.TimerValues) -> None:
        ...
    def FindAllSubdirectories(self, subdirectory: str, num_found: int, path: str) -> None:
        ...
    def FindFile(self, subdirectory: str, filename: str, path: str) -> None:
        ...
    def Free(self, data: int) -> None:
        ...
    def GetCustomerDefault(self, name: str, units: int, default_value: str) -> None:
        ...
    def GetFailMessage(self, fail_code: int, message: str) -> None:
        ...
    def GetRelease(self, release: str) -> None:
        ...
    def GetReservedLicenses(self, context_name: str, n_licenses: int, licenses: str) -> None:
        ...
    def GetTranslatedFailMessage(self, fail_code: int, message: str) -> None:
        ...
    def InitializeDm(self) -> None:
        ...
    def IsInitialized(self) -> int:
        ...
    def IsUgmanagerActive(self, is_active: bool) -> None:
        ...
    def OutputCopyright(self, output_line_of_text: UF.UF.OutputLineOfTextFT) -> None:
        ...
    def PrintSyslog(self, message: str, trace: bool) -> None:
        ...
    def ReallocateMemory(self, data: int, nbytes: int) -> int:
        ...
    def Release(self, license: str, context_name: str) -> None:
        ...
    def ReleaseAll(self, context_name: str) -> None:
        ...
    def RemoveCallbackFunction(self, function_id: int) -> None:
        ...
    def Reserve(self, license: str, context_name: str) -> None:
        ...
    def SetRetiringFlag(self, value: int) -> None:
        ...
    def SetVariable(self, variable: str, value: str) -> None:
        ...
    def TranslateVariable(self, variable: str, translation: str) -> None:
        ...
    def UnloadLibrary(self, library_name: str) -> None:
        ...


    

    

    

class UdeSetType(enum.Enum):
    UdeStartSet = 0
    UdeEndSet = 1
    UdeMachCntrlOperSet = 2


class TimerValues():
    cpu_time: float
    real_time: float


class SystemInfo():
    date_buf: str
    user_name: str
    program_name: str
    node_name: str
    machine_type: str
    os_name: str
    os_version: str
    physical_memory: int
    bundles_used: str
    number_of_bundles: int


class SvKimDegofDirection(enum.Enum):
    SvKimDegofDirectionNone = 0
    SvKimDegofDirectionXPositive = 1
    SvKimDegofDirectionXNegative = 2
    SvKimDegofDirectionYPositive = 3
    SvKimDegofDirectionYNegative = 4
    SvKimDegofDirectionZPositive = 5
    SvKimDegofDirectionZNegative = 6


class StringList():
    num: int
    _string: int
    dir: int
    id: typing.List[Tag]


class SplineFit():
    points: float
    slopes: float
    weights: float
    tolerance: float
    num_of_points: int
    slope_flag: int
    num_of_weights: int
    weight_positions: int
    num_of_segments: int
    degree: int


class SimKimDegofTypes(enum.Enum):
    SimKimDegofTypeNone = 0
    SimKimDegofLinear = 1
    SimKimDegofRotary = 2


class SfmcResult(enum.Enum):
    SFMC_passed_check = 0
    SFMC_failed_check = 1
    SFMC_error_with_check = 2
    SFMC_check_does_not_apply = 3


class SfLegendTitle():
    num_strs: int
    strs: str


class SfLegendTextJustification(enum.Enum):
    LegendLeftJustifiedText = 1
    LegendCenterJustifiedText = 2
    LegendRightJustifiedText = 3




class SfLegendIndexColorAttr():
    attr_mask: int
    width_percent: int
    smooth_sw: bool
    num_values: int
    values: float


class SfLegendIndexAttr():
    attr_mask: int
    height_percent: int
    color_attr: UF.SfLegendIndexColorAttr
    text_attr: UF.SfLegendIndexTextAttr


class SfLegendAttr():
    attr_mask: int
    width_percent: int
    border_sw: bool
    font_size: float
    font_color: int
    header: UF.SfLegendTitle
    index_attr: UF.SfLegendIndexAttr
    footer: UF.SfLegendTitle
    layout_type: int
    view_port_id: int


class SfLangTimeDepend(enum.Enum):
    SfLangSteadyTimeDepend = 1


class SfLangProblemAbstract(enum.Enum):
    SfLangSimpleProbAbstract = 1
    SfLangAxisymProbAbstract = 2
    SfLangMixedProbAbstract = 3


class SfLangLinearity(enum.Enum):
    SfLangLinearLinearity = 1
    SfLangNonlinearLinearity = 2


class SfLangAnalysisType(enum.Enum):
    SfLangAnalysisUnknown = 0
    SfLangAnalysisStructural = 1
    SfLangAnalysisThermal = 2
    SfLangAnalysisFlow = 3
    SfLangAnalysisCoupled = 4
    SfLangAnalysisMapping = 5


class SfColorAttr():
    num_ranges: int
    ranges: float
    rgb_values: float


class ScSectionOutputData():
    output_object: Tag
    start_connected_object: Tag
    start_point: float
    end_connected_object: Tag
    end_point: float


class ScaleType(enum.Enum):
    ScaleTypeUniform = 0
    ScaleTypeAxisymmetric = 1
    ScaleTypeGeneral = 2


class RsoTrimOption(enum.Enum):
    RsoTrimOptNo = 0
    RsoTrimOptYes = 1
    RsoTrimOptBndCurve = 2
    RsoNumTrimOpts = 3


class RsoSurfMethod(enum.Enum):
    RsoSurfMethodCloud = 0
    RsoSurfMethodThru = 1
    RsoSurfMethodRoughFit = 2
    RsoNumSurfMethodOptions = 3


class RsoSurfCtrlOption(enum.Enum):
    RsoSurfCtrlBySystem = 0
    RsoSurfCtrlByUser = 1
    RsoNumSurfCtrlOptions = 2


class PdBusModfrType(enum.Enum):
    PdBusModfrStringType = 0
    PdBusModfrListType = 1
    PdBusModfrUrlType = 2
    PdBusModfrRevisionType = 3
    PdBusModfrSafetyClassType = 4
    PdBusModfrCustomerValueType = 5


class PartLoadState(enum.Enum):
    PartNotLoaded = 0
    PartFullyLoaded = 1
    PartPartiallyLoaded = 2
    PartMinimallyLoaded = 3


class ParamTurnWorkpieceType(enum.Enum):
    ParamTurnWorkpieceTypeUndefined = -1
    ParamTurnWorkpieceTypeCylinder = 0
    ParamTurnWorkpieceTypeTube = 1
    ParamTurnWorkpieceTypeCurves = 3
    ParamTurnWorkpieceTypeWorkspace = 6


class ParamTurnWorkpieceDirection(enum.Enum):
    ParamTurnWorkpieceDirectionTowardsHeadStock = -1
    ParamTurnWorkpieceDirectionFromHeadStock = 1


class ParamTtmoprSubopType(enum.Enum):
    ParamTtmoprSubopTypeRapid = 0
    ParamTtmoprSubopTypeLinfeed = 1
    ParamTtmoprSubopTypeSetEngage = 4
    ParamTtmoprSubopTypeSetRetract = 5
    ParamTtmoprSubopTypeFollowCurve = 6
    ParamTtmoprSubopTypeMce = 7


class ParamLwplaneUsage(enum.Enum):
    ParamOutputWarningOnly = 0
    ParamProjectToLwplaneAlongNormalToPlane = 1
    ParamProjectToLwplaneAlongToolAxis = 2


class ParamLwplaneStatus(enum.Enum):
    ParamLwplaneStatusUndefined = 0
    ParamLwplaneStatusDefinedAndActive = 1
    ParamLwplaneStatusDefinedAndInactive = 2


class ParamClvRangeType(enum.Enum):
    ParamClvRangeAutoGenerate = 0
    ParamClvRangeUserDefined = 1
    ParamClvRangeSingle = 2


class ParamClrplaneUsage(enum.Enum):
    ParamClrplaneUsageAtOperationStartAndEnd = 1
    ParamClrplaneUsageAtOperationStartOnly = 2
    ParamClrplaneUsageAtOperationEndOnly = 3
    ParamClrplaneUsageAtStartMinClearanceAtEnd = 4
    ParamClrplaneUsageAtEndMinClearanceAtStart = 5


class ParamClrplaneStatus(enum.Enum):
    ParamClrplaneUndefined = 0
    ParamClrplaneDefineAndActive = 1
    ParamClrplaneDefineAndInactive = 2


class OprbndUdeSetType(enum.Enum):
    OprbndUdeUndefined = 0
    OprbndUdeStartSet = 1
    OprbndUdeEndSet = 2


class NcmctSetupReplaceMode(enum.Enum):
    NcmctSetupReplaceNone = 0
    NcmctOrientMachineZeroToMcs = 1
    NcmctUseAssemblyPositioning = 2
    NcmctUsePartMountJunction = 3
    NcmctUseOldMachineTransform = 4
    NcmctKeepAssemblyConstraints = 5


class MotnMotionType(enum.Enum):
    MotionTranslation = 0
    MotionRotation = 1


class MotionPvExportType(enum.Enum):
    MotionPvExportVfm = 0
    MotionPvExportVfmAndJt = 1


class ModlUnits(enum.Enum):
    ModlUnitsPart = 0
    ModlInch = 1
    ModlMmeter = 2
    ModlCmeter = 3
    ModlMeter = 4


class ModlSweepTrimSigns(enum.Enum):
    ModlSweepTrimNone = 0
    ModlSweepTrimToFace = 1
    ModlSweepTrimBetwTwoFaces = 2
    ModlSweepTrimToAll = 3


class ModlSweepTrimOpts(enum.Enum):
    DO_NOT_EXTEND_TRIM_FACE = 0
    DO_NOT_EXTEND_AND_EXTEND_TRIM_FACE = 1
    EXTEND_FIRST_TRIM_FACE = 2
    EXTEND_SECOND_TRIM_FACE = 4
    EXTEND_BOTH_TRIM_FACES = 6


class ModlSweepTrimObject():
    trim_objects: typing.List[Tag]
    trim_count: int
    sign: UF.ModlSweepTrimSigns
    thru_bodies: typing.List[Tag]
    num_thru_bodies: int


class ModlSrfValue():
    srf_pos: float
    srf_du: float
    srf_dv: float
    srf_unormal: float
    srf_d2u: float
    srf_dudv: float
    srf_d2v: float
    srf_d3u: float
    srf_d2udv: float
    srf_dud2v: float
    srf_d3v: float
    srf_normal: float


class MethodList():
    method: int
    inter: int
    id: Tag
    value: float
    s_curve: typing.List[UF.StringList]


class MbActivatedButton():
    id: int
    type: int
    name: str
    menubar_name: str
    num_ancestors: int
    ancestors: str
    app_id: int


class ImportPartModes():
    layer_mode: int
    group_mode: int
    csys_mode: int
    plist_mode: int
    view_mode: int
    cam_mode: bool
    use_search_dirs: bool


class FeatureSigns(enum.Enum):
    Nullsign = 0
    Positive = 1
    Negative = 2
    Unsigned = 3
    NoBoolean = 4
    TopTarget = 5
    Unite = 6
    Subtract = 7
    Intersect = 8
    DeformPositive = 9
    DeformNegative = 10


class EplibPartLibPart():
    num_charx: int
    charx: typing.List[UF.EplibCharx]


class EplibCharxValueU():
    i_value: int
    r_value: float
    s_value: str


class EplibCharx():
    type: int
    title: str
    value: UF.EplibCharxValueU


class DrfViewLabelTextToStubFormat(enum.Enum):
    DrawParentViewLabelTextBeforeStub = 0
    DrawParentViewLabelTextAboveStub = 1


class CutLevelSingle():
    entity_tag: Tag
    z_level: float
    local_cut_depth: float


class CurveBcmmcp():
    lim_par1: float
    lim_par2: float
    disp_par1: float
    disp_par2: float
    distance1: float
    distance2: float
    vector1: float
    vector2: float
    dir_pt1: float
    dir_pt2: float
    displace_method1: int
    displace_method2: int


class Codeset(enum.Enum):
    CodesetNotInitialized = -2
    CodesetNotSupport = -1
    CodesetAscii = 0
    CodesetIso88591 = 1
    CodesetEuc = 2
    CodesetSjis = 3
    CodesetIso88594 = 4
    CodesetIso88595 = 5
    CodesetIso88598 = 6
    CodesetBig5 = 7
    CodesetNt866 = 8
    CodesetIso88592 = 9
    CodesetNt852 = 10
    CodesetNt862 = 11
    CodesetKsc5601 = 12
    CodesetGb2312 = 13
    CodesetNt1251 = 14
    CodesetNt1255 = 15
    CodesetNt1250 = 16
    CodesetNt1252 = 17
    CodesetIso885915 = 18
    CodesetNt1253 = 19
    CodesetIso88597 = 20
    CodesetUtf8 = 21
    CodesetNt1254 = 22
    CodesetNt1257 = 23
    CodesetNt1256 = 24
    CodesetIso88596 = 25
    CodesetIso885911 = 26
    CodesetNt1258 = 27


class CamToolPosition(enum.Enum):
    CamToolPositionUndefined = 0
    CamToolPositionOn = 1
    CamToolPositionTanto = 2


class CamMaterialSide(enum.Enum):
    CamMaterialSideUndefined = 0
    CamMaterialSideInLeft = 1
    CamMaterialSideOutRight = 2


class CamGeomType(enum.Enum):
    CamPart = 0
    CamBlank = 1
    CamCheck = 2
    CamTrim = 3
    CamCutArea = 4
    CamWall = 5
    CamDrive = 6


class CamFeedrateUnit(enum.Enum):
    CamFeedrateUnitNone = 0
    CamFeedrateUnitPerMinute = 1
    CamFeedrateUnitPerRevolution = 2


class CamBoundaryType(enum.Enum):
    CamBoundaryTypeClosed = 0
    CamBoundaryTypeOpen = 1


class CambndUdeSetType(enum.Enum):
    CambndUdeUndefined = 0
    CambndUdeStartSet = 1
    CambndUdeEndSet = 2


class CamAvoidanceType(enum.Enum):
    CamAvoidanceTypeNone = 0
    CamAvoidanceTypeWarning = 1
    CamAvoidanceTypeStepover = 2
    CamAvoidanceTypeLift = 3


class CallConvCdeclAttribute(System.Attribute):
    def __init__(self) -> None: ...


class CallbackReason(enum.Enum):
    CreatePartReason = 0
    OpenPartReason = 1
    SavePartReason = 2
    SaveAsPartReason = 3
    ClosePartReason = 4
    ModifiedPartReason = 5
    RenamePartReason = 6
    ChangeWorkPartReason = 7
    PostSaveAsPartReason = 8
    MaxReason = 9


class Args():
    type: int
    length: int
    address: int


