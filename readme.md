Init project:
cd into the folder (cd path/to/SimplePython)
pip install -r requirements.txt
Note: change user and password in file connector.py to your user (with permission to create tables, procedure, 
function, ...)

Create tables for project:
python tables.py

Init some data:
python seed.py
Note: when run seed need drop tables and create tables again

Create procedures and functions needed for project in file Project.sql

Usage:
python main.py

Drop tables:
python drop_tables;