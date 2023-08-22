import matplotlib.pyplot as plt
from databaseConn.connection import create_connection

conn = create_connection()
mycursor = conn.cursor()


def vote_results():
    print("Political Party Name \t Result")
    result = "SELECT * FROM politicalparty ORDER BY results DESC"
    mycursor.execute(result)
    party_details = mycursor.fetchall()

    party_names = []
    result_counts = []
    
    for party in party_details:
        party_names.append(party[1])
        result_counts.append(party[2])
        print("\t", party[1], "\t\t", party[2])

    # Create the bar chart
    plt.bar(party_names, result_counts)

    # Add labels and title
    plt.xlabel('Political Party')
    plt.ylabel('Result Count')
    plt.title('Vote Results')

    # Rotate x-axis labels if needed
    plt.xticks(rotation=45)

    # Display the chart
    plt.show()

def candidate_result():
    print("\n\nCandidate Name \t\t Result")
    result = "SELECT * FROM candidates ORDER BY vote_count DESC"
    mycursor.execute(result)
    candidate_details = mycursor.fetchall()

    candidate_names = []
    result_counts = []
    
    for candidate in candidate_details:
        candidate_names.append(candidate[1])
        result_counts.append(candidate[6])
        print("\t", candidate[1], "\t", candidate[6])

    # Create the bar chart
    plt.bar(candidate_names, result_counts)

    # Add labels and title
    plt.xlabel('Candidate')
    plt.ylabel('Result Count')
    plt.title('Vote Results')

    # Rotate x-axis labels if needed
    plt.xticks(rotation=45)

    # Display the chart
    plt.show()

def result_state():
    print("\n\nProvince \t\t Candidate Name \tResult\n")
    state = "SELECT * FROM province"
    mycursor.execute(state)
    state_details = mycursor.fetchall()

    for state in state_details:
        candidate_state = state[0]
    
        result = "SELECT * FROM candidates WHERE state = %s ORDER BY vote_count DESC"
        mycursor.execute(result,(candidate_state,))
        candidate_details = mycursor.fetchall()
        
        for candidate in candidate_details:
            print(state[1], "\t", candidate[1], "\t\t",candidate[6])