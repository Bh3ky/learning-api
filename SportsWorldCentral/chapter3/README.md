# Understanding SQL Syntax

- in the tables we have created we can see that each column has a data type defined.
- INTEGER = for identifier values
- VARCHAR = for names and text fields
- DATE = for date fields
- FLOAT = for scoring value fields that have a decimal

- Note: each table has a PRIMARY KEY() constraint on the table's identifier field which ensures that these values are unique in each table.

- each table is related to at least one other table. this is accomplished using FOREIGN KEY statement in the child table, which references the primary key in the parent table.

- Note: association tables serve as a child which associates two separate parent tables. 

the command 'PRAGMA foreign_keys = ON; ' turns on foreign key enforcement which prevents someone from insterting a record which is not in a particular table using a different key. 

## Prompts to load the data

sqlite> PRAGMA foreign_keys = ON;
sqlite> .mode csv
sqlite> .import --skip 1 data/player_data.csv player
sqlite> .import --skip 1 data/performance_data.csv performance
sqlite> .import --skip 1 data/league_data.csv league
sqlite> .import --skip 1 data/team_data.csv team
sqlite> .import --skip 1 data/team_player_data.csv team_player


- when accessing the data we have just imported using Python, we use an ORM which handles the process of reading database tables and creating Python objects from them. Python ORM: SQLAlchemy.

- QUE: How do we verify that our code still works after updating a library??
    - use of virtual environments and regression tests. 