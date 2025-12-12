# config.py

# Default IFC classes to preselect in the UI
DEFAULT_IFC_CLASSES = {"IfcWall", "IfcDoor", "IfcSpace", "IfcSlab", "IfcColumn", "IfcBeam", "IfcWindow", "IfcStair", "IfcFoundation", "IfcBuilding", "IfcMaterial"}

# Default attributes per IFC class
DEFAULT_ATTRIBUTES = {
    "IfcWall": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcDoor": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcSpace": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcSlab": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcColumn": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcBeam": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcWindow": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcStair": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
    "IfcFoundation": ["Name", "Objektname", "Abrechnungsart", "Volumen", "Fläche", "Layer", "Material"],
}
