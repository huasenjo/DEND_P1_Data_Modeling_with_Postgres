## Data Modeling with Postgres

In this project, I apply data modeling with Postgres and build an ETL pipeline using Python, also defined a fact table and dimension for a star schema. Also i write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Project Repository files
In the repository files you can see this list files
- create_tables.py
- etl.py
- test.ipynb
- etl.ipynb
- README.md
- data folder

## ETL Process.
The ETL process is the file to run all pipeline to the project, connect to database, processes a song and log files to dataset, extracts the song, artist, time, users information from files and finally insert it into tables.

## BD Model
(![star_model_project](https://user-images.githubusercontent.com/35740728/56818375-84047f80-6815-11e9-90bb-2548ab334b96.png))

## Prerequisites

If you want to run the project locally, you will need to install the following:

Tools:
- Python 3.0 or higher
- Postgresql 9.2 or higher
- Jupyter Notebook


Create BD in postgresql
- dbname=sparkifydb user=student password=student

## Installation

For this case, it is not necessary to install an environment as it is done in the workspace provided by UDACITY

## Usage

### UDACITY Workspace

- Run the file create_tables.py, open test.ipynb and run '%run -i create_tables.py', 
- Run the file etl.py.
- Open the file test.ipynb and execute the tests to validate the results.

### Local Workspace

- Open the console and go to the root folder of the project and run the python command 'python create_tables.py'
- Run the python command 'python etl.py'
- Run command 'jupyter notebook' and open te jupyter notebook 'test.ipynb'
- Validate the results obtained from etl.py (run cells the notebook)

## Credits

Rodrigo Asenjo.

