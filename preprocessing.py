#preprocessing.py

import ifcopenshell
import tempfile
import os

def load_ifc_model(file):
    #Lädt das IFC-Modell in den Speicher
    #Akzeptiert Dateipfade aber auch Streamlit UploadedFile-Objekte
    try:
        #in temporäre Datei schreiben
        if hasattr(file, 'read'):
            with tempfile.NamedTemporaryFile(suffix='.ifc', delete=False) as tmp:
                tmp.write(file.read())
                tmp_path = tmp.name
            try:
                model = ifcopenshell.open(tmp_path)
            finally:
                os.unlink(tmp_path)
        else:
            #Regulärer Dateipfad
            model = ifcopenshell.open(file)
        return model
    except Exception as e:
        raise ValueError(f"Fehler beim Einlesen der IFC-Datei: {e}")


def detect_ifc_classes(model):
    #Liefert alle im Modell vorkommenden IFC-Klassen
    return sorted(set(ent.is_a() for ent in model))


def detect_attributes_for_class(model, ifc_class):
    #Gibt alle Attribute einer Beispiel-Entity zurück
    sample_entities = model.by_type(ifc_class)

    if not sample_entities:
        return []

    return sorted(sample_entities[0].__dict__.keys())


def extract_attributes(model, selected_classes, selected_attributes):
    #Extrahiert die gewünschten Attribute aus dem IFC-Modell
    import pandas as pd
    rows = []

    for ifc_class in selected_classes:
        entities = model.by_type(ifc_class)

        for ent in entities:
            row = {"IfcClass": ifc_class}
            for attr in selected_attributes.get(ifc_class, []):
                row[attr] = getattr(ent, attr, None)
            rows.append(row)

    return pd.DataFrame(rows)
