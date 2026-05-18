import urllib.request
import os

# Set working directory to the folder of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

def download_and_analyze_crystal(crystal_id):
    """
    Downloads crystal structure data from the Crystallography Open Database (COD)
    and extracts basic unit cell parameters.
    """
    # URL for the requested crystal ID in CIF (Crystallography Information File) format
    url = f"http://www.crystallography.net/cod/{crystal_id}.cif"
    output_file = f"crystal_{crystal_id}.cif"
    
    try:
        print(f"Connecting to Crystallography Database to fetch Crystal ID: {crystal_id}...")
        # Download the file from the web database
        urllib.request.urlretrieve(url, output_file)
        print(f"Success: Data saved to {output_file}")
        
        # Processing the downloaded data
        cell_parameters = {}
        with open(output_file, 'r') as file:
            for line in file:
                # Look for unit cell lengths in the database file
                if "_cell_length_a" in line:
                    cell_parameters['a'] = float(line.split()[1].split('(')[0])
                elif "_cell_length_b" in line:
                    cell_parameters['b'] = float(line.split()[1].split('(')[0])
                elif "_cell_length_c" in line:
                    cell_parameters['c'] = float(line.split()[1].split('(')[0])
        
        if len(cell_parameters) == 3:
            # Simple Processing: Calculate approximate unit cell volume (assuming orthogonal axes for simplicity)
            volume = cell_parameters['a'] * cell_parameters['b'] * cell_parameters['c']
            
            print("-" * 30)
            print(f"Analysis Results for Crystal {crystal_id}:")
            print(f"Lattice Parameters: a={cell_parameters['a']}, b={cell_parameters['b']}, c={cell_parameters['c']}")
            print(f"Calculated Unit Cell Volume: {volume:.2f} Å³")
            print("-" * 30)
            return True, volume
        else:
            print("Error: Could not find all cell parameters in the downloaded file.")
            return False, 0
            
    except Exception as e:
        print(f"Failed to fetch or process data: {e}")
        return False, 0

if __name__ == "__main__":
    # ID 1011110 represents a known Silicon/Quartz crystal structure in the database
    download_and_analyze_crystal("1011110")
