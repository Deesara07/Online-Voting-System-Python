from databaseConn.connection import create_connection

conn = create_connection()
mycursor = conn.cursor()

def apply_election():
    NIC = int(input("Enter your National ID Card Number (ex. 2933): "))
    query = "SELECT * FROM citizen WHERE id = %s"
    mycursor.execute(query, (NIC,))
    result = mycursor.fetchone()

    if result:
        query = "SELECT * FROM candidates WHERE Cid = %s"
        mycursor.execute(query, (NIC,))
        result_2 = mycursor.fetchone()
        
        if result_2:
            print("You already registered for election")
        else:
            name = result[1]
            age = result[2]
            state = result[3]

            print("Name:", name)
            print("Age:", age)
            print("State:", state)

            edu_qualification = input("Enter your educational qualification: ")

            parties_query = "SELECT Pid, name FROM politicalparty"
            mycursor.execute(parties_query)
            party_names = mycursor.fetchall()

            print("\nRegister Number\t Name")
            for party in party_names:
                print(party[0], "\t\t", party[1])

            partyID = int(input("Select your political party ID: "))

            query = "INSERT INTO candidates (Cid, name, age, state, education, Pid) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (NIC, name, age, state, edu_qualification, partyID)

            mycursor.execute(query, values)
            conn.commit()
            print("\nYou Successfully Register for election\n")

    else:
        print("Invalid National ID Card Number.")
        exit()
