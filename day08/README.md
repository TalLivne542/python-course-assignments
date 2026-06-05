# Polymer Crystallinity Analyzer — Web API Service

## 1. Task Overview
The objective of this project is to transition a standalone scientific computing script into a scalable, production-ready web service. Building upon the core chemical and thermodynamic calculations established in our previous work, this iteration isolates the analytical software layer from any specific user interface and exposes it as a globally accessible **Web API**.

Rather than utilizing traditional frameworks like Flask, the backend infrastructure for this service is engineered using **FastAPI** to benefit from native asynchronous capabilities, automated input validation via Pydantic, and self-documenting interactive interfaces.

---

## 2. Scientific & Mathematical Background
This application computes the absolute crystallinity percentage ($X_c$) of various semicrystalline polymers based on measured melting enthalpy ($\Delta H_m$) obtained via Differential Scanning Calorimetry (DSC). 

To ensure high accuracy in real-world laboratory environments, the system evaluates the raw material inputs and performs a **moisture content correction**. The chemical logic applies the following thermodynamic equations sequentially:

1. **Moisture Content Correction:**
   Adjusts the measured melting enthalpy to account for the non-polymeric water mass fraction within the sample:
   $$\Delta H_{m,\text{corrected}} = \frac{\Delta H_{m,\text{measured}}}{1 - \left(\frac{\text{Moisture \%}}{100}\right)}$$

2. **Crystallinity Percentage Calculation:**
   Determines the crystalline ratio by benchmarking the corrected enthalpy against the reference thermodynamic enthalpy of a 100% crystalline matrix ($\Delta H_m^0$) sourced from the internal polymer database:
   $$X_c (\%) = \left( \frac{\Delta H_{m,\text{corrected}}}{\Delta H_m^0} \right) \times 100$$

---

## 3. Project Architecture & File System
The project enforces a strict **Separation of Concerns (SoC)** workflow. All computational mechanics are decoupled from the web-handling servers, allowing independent testing and maintenance.

```text
├── polymer_logic.py      # Core Business Logic (Thermodynamic formulas & chemical database)
├── app.py                # Web Application Layer (FastAPI routes, request/response lifecycle)
├── test_project.py       # Dual-Layer Testing Suite (Isolated unit tests + API integration tests)
└── requirements.txt      # System Dependency Manifest
```

AI tool- I used Gemini 3 Flash AI Prompts
I am refactoring an existing Python script that handles scientific polymer crystallinity calculations. 
Please decouple the analytical logic from the rest of the application and place it into an isolated module at core/polymer_logic.py to serve as pure business logic. 
Then, wrap this logic inside a modern, high-performance web service layer using the FastAPI framework in app.py. 
The application should expose a POST endpoint at /calculate that parses input via a structured Pydantic model and handles validation errors gracefully.
