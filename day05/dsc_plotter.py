import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_dsc_plot(file_path):
    """
    Reads DSC data from a CSV, identifies the peak temperature for analysis,
    and generates a clean labeled plot without annotations.
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return False

        # Load data, skipping the first metadata row
        data = pd.read_csv(file_path, skiprows=1)
        
        # Clean column names in case of trailing spaces
        data.columns = data.columns.str.strip()
        
        x_data = data['Temperature']
        y_data = data['Heat Flow (Normalized)']
        
        # ANALYSIS: Find the peak temperature (for terminal output only)
        peak_idx = y_data.idxmax()
        peak_temp = x_data.iloc[peak_idx]
        
        # Create the plot
        plt.figure(figsize=(12, 7))
        plt.plot(x_data, y_data, color='darkblue', label='Heat Flow Curve', linewidth=1.5)
        
        # Formatting the plot (Clean version)
        plt.title(f'Thermal Analysis: {file_path}', fontsize=14)
        plt.xlabel('Temperature (°C)', fontsize=12)
        plt.ylabel('Heat Flow (Normalized) (W/g)', fontsize=12)
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()
        
        # Save output
        output_image = "dsc_analysis_output.png"
        plt.savefig(output_image)
        
        print("-" * 30)
        print(f"Analysis Results for: {file_path}")
        print(f"Peak Temperature identified at: {peak_temp:.2f}°C")
        print(f"Graph saved as: {output_image}")
        print("-" * 30)
        
        return True
    except Exception as e:
        print(f"Error during processing: {e}")
        return False

if __name__ == "__main__":
    # Ensure the filename matches your file in the day05 folder
    filename = '10-ec-165c-annealing-18h-air.csv'
    generate_dsc_plot(filename)
