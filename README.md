# DSM Auction Simulation Program

## Overview
This program is designed to simulate a market environment demand-supply matchmaking (DSM) involving bidders and sellers within various geographic locations. It uses a combination of random behavior generation, geographic data, and configuration parameters to run simulations and output data in a structured format.

## Features
* **Behavior Simulation**: Generates behaviors for different participants based on aggressiveness, market price factors, and other parameters.
* **Geographic Data**: Utilizes city data to simulate interactions based on real-world locations.
* **Configuration**: Fully customizable simulation parameters via a YAML configuration file.
* **Data Export**: Output simulation results to Excel for further analysis.
* **Database Integration**: Uses MongoDB to manage and store data related to bidders, sellers, and other entities.

## Installation
### Prerequisites
* Python 3
* MongoDB (either local or cloud-based like MongoDB Atlas)
* pip (Python package installer)

### Installation Steps
1. Clone the repository:
```python
git clone https://github.com/ShaiFernandez/DSM_Auction.git
```
2. Install required Python packages:
```python
pip install -r requirements.txt
```
Set up MongoDB:
* Create a MongoDB database and collections for bidders and sellers.
* Update the uri in the main.py file with your MongoDB connection string.

## Configuration
The simulation parameters are controlled through the **config.yaml** file. Key parameters include:

* seed: Random seed for reproducibility.
* sellers: Number of sellers in the simulation.
* bidders: Number of bidders in the simulation.
* resource-usage, distance-limit, distance-penalty, etc.: Various settings that control the behavior of the simulation.

## Usage
1. **Run the simulation**:
To run the auction simulation, execute the "main.py" script:
```python
python main.py
```
2. **Export Data**:
Data will be automatically exported to an Excel file based on the results of the simulation.

## Files
* Behaviour.py: Handles the generation of participant behaviors.
* Cities.py: Contains geographic data used in the simulation.
* config.yaml: Configuration file for simulation parameters.
* excelData.py: Exports simulation data to Excel.
* main.py: The main script that runs the simulation.
* maps_coordinates.py: Generates random geographic coordinates for simulation purposes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
