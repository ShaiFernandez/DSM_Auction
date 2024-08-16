# DSM Auction Simulation Program

## Table of Contents
* Overview
* Installation
* Usage
* Modules Description
* Configuration
* Dependencies
* Contributing
* License



## Overview
This project is an auction simulation program that models the behavior of bidders and sellers in a dynamic auction environment. The program uses a MongoDB database to store and manage auction data and supports various auction strategies and configurations.

## Installation
### Prerequisites
* Python 3
* MongoDB (either local or cloud-based like MongoDB Atlas)
* pip (Python package installer)

### Installation Steps
1. Clone the repository:
```python
git clone https://github.com/your-repository.git
cd your-repository
```
2. Install required Python packages:
```python
pip install -r requirements.txt
```
Set up MongoDB:
* Create a MongoDB database and collections for bidders and sellers.
* Update the uri in the main.py file with your MongoDB connection string.

## Usage
To run the auction simulation, execute the "main.py" script:
```python
python main.py
```

### Key Features
* **Auction Simulation**: Simulates auction rounds with multiple bidders and sellers.
* **Behavior Modeling**: Includes different behavioral strategies for bidders and sellers.
* **Data Management**: Uses MongoDB for storing auction-related data.
* **Custom Configurations**: Easily configurable auction parameters.
