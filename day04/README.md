The New Feature: Moisture Compensation LogicIn this version 
I decided to upgrade the calculator to handle real-world laboratory conditions. 
Many polymers, such as Polyamides (Nylon), are hygroscopic and absorb moisture from the environment. 
This moisture adds "dead weight" to the sample, which leads to an underestimated enthalpy value in DSC tests.
The Innovation:I instructed the system to implement a Moisture Compensation feature. The user can now input the moisture content percentage. 
The calculator then isolates the dry polymer mass and corrects the enthalpy before calculating the final crystallinity percentage.

The Formula:$$\Delta H_{corrected} = \frac{\Delta H_{measured}}{1 - (\text{Moisture}\% / 100)}$$. 

I used Gemini 3 Flash (by Google).
My instructions to Gemini included: Refactoring the Library: I want to add moisture compensation to the calculate_crystallinity function. 
Update the logic to accept an optional moisture parameter and use it to adjust the measured enthalpy.
Updating User Interfaces: Modify all my existing interface files (gui_calc.py, interactive_calc.py, and cli_calc.py) to include a new input field for moisture. 
Ensure it defaults to 0% if the user provides no input.
Advanced Testing: Write a dedicated test case for test_logic.py that specifically checks the math behind the moisture correction to ensure the results are physically accurate.
