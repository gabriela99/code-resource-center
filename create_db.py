import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

new_db = 'crc'

conn = psycopg2.connect("dbname=postgres user=postgres password=admin")

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # needed for python to create a DB

cur = conn.cursor()
cur.execute ("SELECT datname FROM pg_database WHERE datname = '{}'".format(new_db))

found = False
for row in cur:
    if new_db in row:
        found = True

if not found:
    cur.execute("CREATE DATABASE {} OWNER postgres".format(new_db))
    print ("Database created.")
else:
    print ("Database already found.")

# Close communication with the database
cur.close()
conn.close()

# on the first run, this script should show something similar to:
# /Users/code/anaconda3/envs/code/bin/python3.6 "./create_db.py"
# Database created.
#
# Process finished with exit code 0



# on subsequent runs, this script should show something similar to:
# /Users/code/anaconda3/envs/code/bin/python3.6 "./create_db.py"
# Database already found.

# Process finished with exit code 0


# trouble shooting:
# - Don't forget to set your username and password in line 6
# - check if psycopg2 is installed in your anaconda environment
# - check if your project interpreter is set under: settings -> project:yourname -> Project Interpreter
#       it should point to the desired anaconda environment where you installed psycopg2
