from databaseConn.connection import create_connection
conn = create_connection()
mycursor = conn.cursor()

class Citizen:
    def __init__(self, name, NIC, age, state):
        self.name = name
        self.NIC = NIC
        self.age = age
        self.state = state

def addNewCitizen():
    NIC = int(input("Enter your National ID Card Number (ex. 2933): "))
    query = "SELECT * FROM citizen WHERE id = %s"
    mycursor.execute(query, (NIC,))
    result = mycursor.fetchone()
    if result:
        print("You already registered")
    else:
        name = input("Enter your Name: ")
        age = int(input("Enter your Age: "))
        
        state = "SELECT * FROM province"
        mycursor.execute(state)
        state_details = mycursor.fetchall()
        print("\nProvince Code \t Name")
        for state in state_details:
            print(state[0], "\t\t", state[1])
            
        state = int(input("Enter your province Code: "))
        if state > 1004 or state < 1001:
            print("Wrong Province code...try again")
            state = int(input("Enter your province Code: "))

        citizen = Citizen(name, NIC, age, state)

        query = "INSERT INTO citizen (name, id, age, state) VALUES (%s, %s, %s, %s)"
        values = (citizen.name, citizen.NIC, citizen.age, citizen.state)

        mycursor.execute(query, values)
        conn.commit()
        print("Successfully added")

