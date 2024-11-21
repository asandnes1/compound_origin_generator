# Compound Origin Generator

I want to learn how to implement AI tools in Python applications. Therefore, this project aims to use AI to generate an origin story about a molecule whose data is extracted from Pubchem using PubChemPy.

Components:
- Input field
- Dropdown
- Datatable
- Image
- Textbox

By giving one or a series of strings representing molecule names (eg., glucose insulin) as input, PubChemPy fetches relevant data from the database of Pubchem. The extractable data can be chosen in the dropdown.
The chemical structure is drawn by RDKit for all prompted molecules, and the Gemini 1.5 Flash AI model generates an origin story based on he molecule name in a static prompt.

Technologies used:

- Python version 3.10.14
- dash==2.17.1
- pubchempy==1.0.4
- ag-grid==23.1.0
- rdkit==2024.03.5
- Gemini 1.5 Flash

This project offers a practical solution for exploring chemical compounds while also adding educational and storytelling elements to enhance the user experience.
