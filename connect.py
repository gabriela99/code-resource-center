import psycopg2

new_db = 'crc'

# Connect to an existing database
conn = psycopg2.connect("dbname='{}' user=postgres password=admin".format (new_db))

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE IF NOT EXISTS public.first (id bigserial NOT NULL, firstname character varying(50), lastname character varying(50) NOT NULL, PRIMARY KEY (id)) WITH (OIDS = TRUE);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO public.first (firstname, lastname) VALUES (%s, %s)",("your", "name"))

# Query the database and obtain data as Python objects
cur.execute("SELECT id, firstname, lastname FROM first;")
for row in cur:
    print (row)

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()


# When running this script you should get a result like this:
# /Users/code/anaconda3/envs/code/bin/python3.6 "./connect.py"
# (1, 'your', 'name')

# Process finished with exit code 0
