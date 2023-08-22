from databaseConn.connection import create_connection

conn = create_connection()
mycursor = conn.cursor()

def clean_result():
    clean_party = "UPDATE politicalparty SET results = 0"
    clean_candidate = "UPDATE candidates SET vote_count = 0"
    
    mycursor.execute(clean_party)
    mycursor.execute(clean_candidate)
    conn.commit()
clean_result()
