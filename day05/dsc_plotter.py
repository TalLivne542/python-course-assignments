import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_dsc_plot(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return False

        # 1. Read the header (column names) from the 2nd row (index 1)
        columns_row = pd.read_csv(file_path, skiprows=1, nrows=0).columns.tolist()
        
        # 2. Read the actual data starting from the 4th row (index 3)
        # We skip the first 3 rows: Header title, Column names, and Units.
        data = pd.read_csv(file_path, skiprows=3, names=columns_row)
        
        # Clean column names
        data.columns = data.columns.str.strip()
        
        # Convert columns to numeric (in case units caused issues)
        x_data = pd.to_numeric(data['Temperature'], errors='coerce')
        y_data = pd.to_numeric(data['Heat Flow (Normalized)'], errors='coerce')
        
        # Remove any NaN rows that might have been created
        valid_data = data.dropna(subset=['Temperature', 'Heat Flow (Normalized)'])
        x_data = valid_data['Temperature']
        y_data = valid_data['Heat Flow (Normalized)']

        # ANALYSIS: Peak Detection
        peak_idx = y_data.idxmax()
        peak_temp = x_data.iloc[peak_idx]
        
        # Plotting
        plt.figure(figsize=(12, 7))
        plt.plot(x_data, y_data, color='darkblue', linewidth=1.5)
        plt.title(f'Thermal Analysis: {file_path}', fontsize=14)
        plt.xlabel('Temperature (°C)', fontsize=12)
        plt.ylabel('Heat Flow (Normalized) (W/g)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5)
        
        output_image = "dsc_analysis_output.png"
        plt.savefig(output_image)
        
        print("-" * 30)
        print(f"Analysis Results for: {file_path}")
        print(f"Peak Temperature identified at: {peak_temp:.2f}°C")
        print("-" * 30)
        
        return True
    except Exception as e:
        print(f"Error during processing: {e}")
        return False

if __name__ == "__main__":
    filename = '10-ec-165c-annealing-18h-air.csv'
    generate_dsc_plot(filename)
