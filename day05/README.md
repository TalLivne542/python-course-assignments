Task Description
I developed a Python tool that automates the processing of raw experimental data from a DSC (Differential Scanning Calorimetry) machine. 
The script processes the laboratory file 10-ec-165c-annealing-18h-air.csv:
Smart Parsing: The code is designed to handle a specific lab format: it skips the first title row, identifies column names from the second row, and ignores the third row (units) to ensure numerical integrity.
Visual Output: The program generates a graph saved as dsc_analysis_output.png.
AI tool- I used Gemini 3 Flash 
AI Prompts- "Write a Python script that processes a raw DSC CSV file. The file has a title in the first row, headers in the second, and units in the third; the data itself starts from the fourth row. 
The script should: Extract 'Temperature' for the X-axis and 'Heat Flow (Normalized)' for the Y-axis.
Generate an aesthetic graph with grid lines and proper labels using Matplotlib.
Write a test suite using Pytest to verify that the file is read correctly and the graph is generated."
