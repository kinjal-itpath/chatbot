import sqlite3   
def insert_data(requirement, mockup,  timeline, budget, name, email, phone):
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")
    # cursor.execute('''CREATE TABLE   d8(
    #     id integer PRIMARY KEY,s
    #     application VARCHAR,
    #     requirement VARCHAR,
    #     mockup VARCHAR,
    #     timeline VARCHAR, 
    #     budget VARCHAR,
    #     name VARCHAR,
    #     email VARCHAR,
    #     phone INTEGER
    # );''')
    cursor.execute('''INSERT INTO d3(requirement, mockup, timeline, budget, name, email, phone) VALUES ( ?, ?, ?, ?, ?, ?,?)''', (requirement, mockup,  timeline, budget, name, email, phone))
    
        
    print("Table created successfully........")

    # Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()
    # print("data inserted")
# if __name__ == "__main__":
#     insert_data('web for business','design', 'with in month', 2000, 'darpan', 'qwerty@gmail.com', 987654321)