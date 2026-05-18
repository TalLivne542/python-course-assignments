Web Database Integration (Crystallography Open Database)

## Task Description
As a materials science/chemistry studentt, I chose to integrate my script with the **Crystallography Open Database (COD)**.

## About the Database
The **Crystallography Open Database (COD)** is an open-access web repository containing over 500,000 crystal structures of organic, inorganic, and organometallic compounds. It provides structural data files (.cif format) that detail atom positions, symmetry groups, and unit cell dimensions.

## Data Processing Logic
The script automated the following steps:
1. **Web Request:** Dynamically queries the COD web server using a specific Crystal Structure ID.
2. **File Extraction:** Downloads the `.cif` text file directly into the local directory.
3. **Data Parsing:** Filters the file to extract the lattice parameters ($a, b, c$) while handling formatting artifacts (like error boundaries in brackets).
4. **Analysis:** Computes the approximate volume of the crystal's unit cell ($V = a \times b \times c$) and outputs the results.

## AI 
I used **Gemini 3 Flash** 

I provided the following prompt to the AI:
> "Write a Python script for Day 06 that connects to a scientific database in the field of materials science or chemistry (like a crystal structures database).
> The script should download a crystal file from a URL using a given ID, parse the file to extract the unit cell length parameters (a, b, c), and calculate the unit cell volume.
> Include an automated test suite with Pytest and ensure the working directory is set automatically."

