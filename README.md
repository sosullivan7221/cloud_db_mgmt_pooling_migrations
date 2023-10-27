# cloud_db_mgmt_pooling_migrations
Connection Pooling and Database Migrations with Azure and GCP

## Database Schema

The Azure Database contained two tables, a patient's table and a patient demographic table, which is linked to the patient ID number in the patient table. The GCP Database contains two tables, a patient table and a medications table, which is linked to the patient ID number in the patient table. These relationships can be seen in the ERD diagram screenshots.

## Migration Process

1. Create a MySQL instance in either Azure or GCP.
2. Create a migrations.py file and establish a connection to your MySQL database. If tables already exist, you can insert them into the migrations.py file along with any new tables to modify them.
3. Run 'pip install sqlalchemy alembic mysql-connector-python' in the terminal
4. Run 'alembic init migrations' in the terminal. This will create a number of new files.
5. In alembic.ini, change the sqlalchemyurl variable to equal the url to your MySQL instance.
6. In env.py, uncomment and edit lines 19-20 and modify them to import Base from your migrations.py file.
7. Run 'alembic revision --autogenerate -m "create tables"' in the terminal.
8. Run 'alembic upgrade head' to push the changes. You can save the migration by running 'alembic upgrade head --sql > migration.sql'
9. Check the database to see the changes.

## Migration Notes/Error

During the migration process, there are two notes to be made. First, I ran into an issue in my Azure Database where only one of the two tables that I wanted to add was being added by running the migrations_azure.py file. This was resolved when I realized my foreign key was not linked to the primary key in my other table but to another variable. This was giving me an error, and when fixing this relationship both tables were added. Second, in my migrations.py files for both Azure and GCP, I did not include the original tables in my schema in the file, which resulted in them being dropped in the migrations.sql files. My initial understanding was that changes would only be marked to any tables that I had included in my migrations.py file. However, by not including them it seems that alembic interpreted it as I wanted to drop those tables from my MySQL database, resulting in the DROP TABLE commands being in the migrations.sql files. This was the observable change in my Azure database, and in GCP I additionally modified some of the rows in my doctor table, which are documented in the migrations.sql file. 
