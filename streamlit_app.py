import streamlit as st
from PIL import Image


st.set_page_config(page_title="ASFiNAG Datenstruktur-Tool", page_icon="asfinag.ico", initial_sidebar_state="collapsed")

## Streamlit app starts here
image = Image.open("asfinag_logo.png")
st.image(image, caption='Datenstruktur-Tool© - WORKFLOW')
st.write('---')


# Load your images
image1 = Image.open('01.PNG')
image2 = Image.open('21.PNG')
image3 = Image.open('07.PNG')
image4 = Image.open('08.PNG')
image5 = Image.open('11.PNG')
image6 = Image.open('13.PNG')

# Set the title of the app
st.title('Workflow für Revit-User')
st.write('Am Beispiel des Datenstruktur-Elements "Fahrbahnplatte" werden die Parameter mit dem kostenlosen Revit-Plugin "ParaManager" in 5 Schritten einfach, schnell und fehlerfrei eingespielt.')

'---'

# Display the first step and the first image
st.subheader('Ausgangssituation: Beispiel-Element ohne DS-Parameter')
st.image(image1)


'---'

# Display the second step and the second image
st.subheader('Schritt 1: Auswahl des Elements im DS-Tool und Download des Shared Parameter Files')
st.image(image2)

'---'

# Display the second step and the second image
st.subheader('Schritt 2: ParaManger öffnen und im Tab "Families" nach "Fahrbahnplatte" (Name der Revit-Familie) filtern.')
st.image(image3)

'---'

# Display the second step and the second image
st.subheader('Schritt 3: Shared Parameter File importieren')
st.image(image4)

'---'

# Display the second step and the second image
st.subheader('Schritt 5: Alle Parameter der Datei auswählen und einspielen (Import + Apply).')
st.image(image5)

'---'

# Display the second step and the second image
st.header('Ergebnis: Beispiel-Element mit DS-Parameter')
st.image(image6)

