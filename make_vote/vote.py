from databaseConn.connection import create_connection

conn = create_connection()
mycursor = conn.cursor()

def make_vote():
    id = int(input("Enter your National ID Card Number (ex. 2033): "))
    query = "SELECT * FROM citizen WHERE id = %s"
    mycursor.execute(query, (id,))
    result = mycursor.fetchone()

    if result:
        status = result[4]  # Assuming status is the 5th column (index 4) in the citizen table
        if status == 0:
            state = result[3]  # Assuming state is the 4th column (index 3) in the citizen table

            print("\n\tYour Details\n")
            print("Name:", result[1])
            print("Age:", result[2])
            print("State:", result[3])
            
            count = 0
            while count < 3:

                parties_query = "SELECT Pid, name FROM politicalparty"
                mycursor.execute(parties_query)
                party_names = mycursor.fetchall()

                print("\n\tSelect Your Political Party\n")

                for party_name in party_names:
                    print(party_name[0], party_name[1])

                selected_party = input("Enter the ID of the political party: ")

                candidate_query = "SELECT Cid, name, age, education FROM candidates WHERE state = %s AND Pid = %s"
                mycursor.execute(candidate_query, (state, selected_party))
                candidate_names = mycursor.fetchall()
                vote_query_party = "UPDATE politicalparty SET results = results + 1 WHERE Pid = %s"
                mycursor.execute(vote_query_party, (selected_party,))
                conn.commit()

                print("\n\tSelect Candidate\n")
                print("ID\t Name\t\t Age \t Education qulification\n")

                for candidate in candidate_names:
                    candidate_id = candidate[0]
                    candidate_name = candidate[1]
                    candidate_age = candidate[2]
                    candidate_education = candidate[3]
                    
                    print(candidate_id, "\t", candidate_name, "\t", candidate_age, "\t", candidate_education, "\n")
                    
                selectID = int(input("Make your vote: "))
                vote_query = "UPDATE candidates SET vote_count = vote_count + 1 WHERE Cid = %s"
                mycursor.execute(vote_query, (candidate_id,))
                conn.commit()
                count += 1    
            
            vote_done = "UPDATE citizen SET status = 1 WHERE id = %s"
            mycursor.execute(vote_done, (id,))
            conn.commit()
            print("Your Vote is Done...Thank you")

            
        else:
            print("You have already voted.")
    else:
        print("Invalid ID Card Number.")
