import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.UI

def main():
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    # ---------------------------------------
    # Create Sketch (example: rectangle)
    # ---------------------------------------
    sketches = workPart.Sketches
    origin = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal = NXOpen.Vector3d(0.0, 0.0, 1.0)
    datumPlane = workPart.Planes.CreatePlane(origin, normal, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # Use SimpleSketchInPlaceBuilder for parametric sketch
    sketchBuilder = sketches.CreateSimpleSketchInPlaceBuilder()
    sketchBuilder.PlaneReference = datumPlane
    sketch = sketchBuilder.Commit()
    
    # Activate sketch (view oriented)
    sketch.Activate(NXOpen.Sketch.ViewReorient.TrueValue)

    # ---------------------------------------
    # Draw a simple rectangle
    # ---------------------------------------
    line1 = workPart.Curves.CreateLine(NXOpen.Point3d(-50.0, -30.0, 0.0), NXOpen.Point3d(50.0, -30.0, 0.0))
    line2 = workPart.Curves.CreateLine(NXOpen.Point3d(50.0, -30.0, 0.0), NXOpen.Point3d(50.0, 30.0, 0.0))
    line3 = workPart.Curves.CreateLine(NXOpen.Point3d(50.0, 30.0, 0.0), NXOpen.Point3d(-50.0, 30.0, 0.0))
    line4 = workPart.Curves.CreateLine(NXOpen.Point3d(-50.0, 30.0, 0.0), NXOpen.Point3d(-50.0, -30.0, 0.0))

    for line in [line1, line2, line3, line4]:
        sketch.AddGeometry(line, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    sketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)

    # ---------------------------------------
    # Ask user for extrusion height using NX dialog
    # ---------------------------------------
    theUI = NXOpen.UI.GetUI()
    height_str = theUI.InputBox("Enter extrusion height (mm):", "Extrusion Height", "100")
    
    if height_str is None:
        theUI.NXMessageBox.Show("Info", NXOpen.NXMessageBox.DialogType.Information, "Extrusion cancelled.")
        return

    try:
        height = float(height_str)
    except ValueError:
        theUI.NXMessageBox.Show("Error", NXOpen.NXMessageBox.DialogType.Error, "Invalid input for height.")
        return

    # ---------------------------------------
    # Create Extrude feature
    # ---------------------------------------
    extrudeBuilder = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    # Create section from sketch
    section = workPart.Sections.CreateSection(NXOpen.Section.AllowTypes.OnlyCurves)
    section.AddToSection([line1, line2, line3, line4], NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null,
                         NXOpen.Point3d(0.0,0.0,0.0), NXOpen.Section.Mode.Create, False)
    extrudeBuilder.Section = section

    # Set extrusion height
    extrudeBuilder.Limits.StartExtend.Value.SetFormula("0")
    extrudeBuilder.Limits.EndExtend.Value.SetFormula(str(height))
    extrudeBuilder.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

    # Commit extrusion
    extrudeBuilder.CommitFeature()
    extrudeBuilder.Destroy()
    
    theUI.NXMessageBox.Show("Success", NXOpen.NXMessageBox.DialogType.Information, f"Extrusion created with height {height} mm.")

if __name__ == "__main__":
    main()
