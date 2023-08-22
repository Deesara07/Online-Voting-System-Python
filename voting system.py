import mysql.connector
import display.mainview as view
import menukey.selection as menukey
from databaseConn.connection import create_connection
import registration.register as register
import election_Apply.apply as apply
import make_vote.vote as vote
import vote_results.result as result
import clean.clean as clean
conn = create_connection()
mycursor = conn.cursor()

class Citizen:
    def __init__(self, name, NIC, age, state):
        self.name = name
        self.NIC = NIC
        self.age = age
        self.state = state

class Candidate(Citizen):
    def __init__(self, name, NIC, age, education, state):
        super().__init__(name, NIC, age, state)
        self.education = education

view.startview()
user_input = 0
user_input = menukey.get_input()

if(user_input == 1):
    view.citizenReg()
    register.addNewCitizen()
    
elif(user_input == 2):
    view.candidateReg()
    apply.apply_election()
    
elif(user_input == 3):
    view.makeVote()
    vote.make_vote()
elif(user_input == 4):
    view.result()
    result.vote_results()
    result.candidate_result()
    result.result_state()
    
elif(user_input == 5):
    clean.clean_result()
    view.clean()
    
else:
    exit()
    
