#main.py

import streamlit as st
import pandas as pd

from preprocessing import (
    load_ifc_model,
    detect_ifc_classes,
    detect_attributes_for_class,
    extract_attributes
)

from utils import to_excel
from config import DEFAULT_IFC_CLASSES, DEFAULT_ATTRIBUTES



# STREAMLIT UI
st.set_page_config(page_title="IFC Attribute Extractor", layout="wide")

st.title("IFC Attributextraktor")
st.write("Extrahiere Attribute aus IFC-Dateien und exportiere sie als Exceltabelle")




#Datei-Upload
uploaded_file = st.file_uploader("IFC-Datei hochladen", type=["ifc"])



if uploaded_file:
    model = load_ifc_model(uploaded_file)
    st.success("IFC-Datei wurde erfolgreich geladen")

    #IFC-Klassen erkennen
    all_classes = detect_ifc_classes(model)

    #1.Klassen auswählen
    st.subheader("1️⃣ IFC-Klassen auswählen")
    #Filter berücksichtigt nur vordefinierte Klassen, die im IFC vorhanden sind
    default_classes = [cls for cls in DEFAULT_IFC_CLASSES if cls in all_classes]
    selected_classes = st.multiselect(
        "Wähle die IFC-Klassen:",
        all_classes,
        default=default_classes
    )

    

    #2.Attribute auswählen
    selected_attributes = {}

    if selected_classes:
        st.subheader("2️⃣ Attribute auswählen")

        for ifc_class in selected_classes:
            attrs = detect_attributes_for_class(model, ifc_class)

            # Filter defaults to only include attributes that exist in the class
            default_attrs = DEFAULT_ATTRIBUTES.get(ifc_class, ["Name"])
            filtered_defaults = [attr for attr in default_attrs if attr in attrs]

            chosen_attrs = st.multiselect(
                f"Attribute für {ifc_class}:",
                attrs,
                default=filtered_defaults
            )

            selected_attributes[ifc_class] = chosen_attrs



    #3.Extraktion starten
    if st.button("📥 Attribute extrahieren"):
        df = extract_attributes(model, selected_classes, selected_attributes)

        st.subheader("3️⃣ Ausgelesene Daten")
        st.dataframe(df, use_container_width=True)

    

        #4.Export als Exceldatei
        excel_data = to_excel(df)
        st.download_button(
            "📤 Export als Excel (.xlsx)",
            data=excel_data,
            file_name="ifc_attribute.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
