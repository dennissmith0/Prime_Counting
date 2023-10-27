import sqlite3

# Create a new SQLite database in memory
# You can also create on disk by replacing ":memory:" with a filename
conn = sqlite3.connect(':memory:')

# Create a table for primes
conn.execute('''
CREATE TABLE PRIMES (
    ID INT PRIMARY KEY NOT NULL,
    PRIME_NUMBER INT NOT NULL
);''')

# Create a table for twin primes
conn.execute('''
CREATE TABLE TWIN_PRIMES (
    ID INT PRIMARY KEY NOT NULL,
    SMALLER_PRIME INT NOT NULL,
    LARGER_PRIME INT NOT NULL
);''')

# Create a table for blocked numbers
conn.execute('''
CREATE TABLE BLOCKED_NUMBERS (
    ID INT PRIMARY KEY NOT NULL,
    BLOCKED_NUMBER INT NOT NULL
);''')

# Commit the changes and close the connection for now
conn.commit()

# Just a message to indicate that tables were created
"SQLite tables for primes, twin primes, and blocked numbers have been created."
