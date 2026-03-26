Implement any one of the following Expert System
I. Information management
II. Hospitals and medical facilities
III. Help desks management
IV. Employee performance evaluation
V. Stock market trading
VI. Airline scheduling and cargo schedules



Group C
Assignment 6:
Aim/Title: Implement any one of the following Expert System I.Information
managements II. Hospitals and medical facilities III. Help desks management IV.
Employee performance evaluation V. Stock market trading VI. Airline scheduling
and cargo schedules
Objective: To understand the use of Expert system for Hospital and Medical
Facilities.
Requirements:
Hardware Requirement:
Object: PC, Laptop
Software Requirement:
Operating System: Windows 7,8,10/11
Specification: Core i3,i5 or above
Specified Language: C++, Java, Python
Software: Visual Studio Code, IntelliJ
Theory:
What is an Expert System?
In artificial intelligence (AI), an expert system is a computer-based decision-making system. It is
designed to solve complex problems. To do so, it applies knowledge and logical reasoning and
adheres to certain rules. An expert system is one of the first successful forms of artificial
intelligence
Component Of Expert System:
● User interface – It is the most important part of the expert system software. The user
interface transfers the queries of the user and into the inference engine. Then it shows the
results to the user. It acts as a two-way communicator between the expert system and the
user.
 Fig: Component Of Expert System
● Inference engine – The inference engine is the central processing unit of the expert
system. An inference engine works on rules and regulations to solve complex problems. It
uses information from the knowledge base. It smartly selects factual data and rules, and
processes and applies them to answer the user’s query. It also gives proper reasoning about
the data in the knowledge base. This helps detect and deduce complex problems and
prevents recurrence. And the last, the inference engine formulates conclusions.
The inference engine has the following strategies:
Forward chaining – Answers the question, “What can happen in the future?”
1. Backward chaining – Answers the question, “Why did this happen?”
● Knowledge base – The knowledge base is the information center. It contains all the
information about problem domains. It is like a large repository of information collected
from various experts.
Knowledge Base Components
Factual and heuristic knowledge is stored in the knowledge base.
● Factual Knowledge − Information pertaining to knowledge engineers.
● Heuristic Knowledge − Ability to evaluate and guess.
Capabilities Of Expert System:
Other Key Terms used in Expert System:
Apart from the expert system components listed above, the following terms are also extensively
used when discussing expert systems.
● Facts and rules – A fact is a small piece of important knowledge. Facts have limited use.
An expert system selects the rules to solve a problem.
● Knowledge acquisition – Knowledge acquisition refers to the method used to extract
domain-specific information by an expert system. The process begins by acquiring
knowledge from a human expert, converting human knowledge into facts and rules, and
finally feeding those rules into the knowledge base.
Algorithm:
from pyknow import *
diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {

    def preprocess():
global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
diseases = open("diseases.txt")
diseases_t = diseases.read()
diseases_list = diseases_t.split("\n")
diseases.close()
for disease in diseases_list:
disease_s_file = open("Disease symptoms/" + disease + ".txt")
disease_s_data = disease_s_file.read()
s_list = disease_s_data.split("\n")
diseases_symptoms.append(s_list)
symptom_map[str(s_list)] = disease
disease_s_file.close()
disease_s_file = open("Disease descriptions/" + disease + ".txt")
disease_s_data = disease_s_file.read()
d_desc_map[disease] = disease_s_data
disease_s_file.close()
disease_s_file = open("Disease treatments/" + disease + ".txt")
disease_s_data = disease_s_file.read()
d_treatment_map[disease] = disease_s_data
disease_s_file.close()
def identify_disease(*arguments):
symptom_list = []
for symptom in arguments:
symptom_list.append(symptom)
# Handle key error
return symptom_map[str(symptom_list)]
def get_details(disease):
return d_desc_map[disease]
def get_treatments(disease):
return d_treatment_map[disease]
def if_not_matched(disease):
print("")
id_disease = disease
disease_details = get_details(id_disease)
treatments = get_treatments(id_disease)
print("")
print("The most probable disease that you have is %s\n" %(id_disease))
print("A short description of the disease is given below :\n")
print(disease_details+"\n")
print("The common medications and procedures suggested by other real doctors
are: \n")
print(treatments+"\n")
# @my_decorator is just a way of saying just_some_function =
my_decorator(just_some_function)
#def identify_disease(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue,
restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
@DefFacts()
def _initial_action(self):
print("")
print("Hi! I am Dr.Yar, I am here to help you make your health better.")
print("For that you'll have to answer a few questions about your conditions")
print("Do you feel any of the following symptoms:")
print("")
yield Fact(action="find_disease")
@Rule(Fact(action='find_disease'), NOT(Fact(headache=W())),salience = 1)
def symptom_0(self):
self.declare(Fact(headache=input("headache: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())),salience = 1)
def symptom_1(self):
self.declare(Fact(back_pain=input("back pain: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())),salience = 1)
def symptom_2(self):
self.declare(Fact(chest_pain=input("chest pain: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(cough=W())),salience = 1)
def symptom_3(self):
self.declare(Fact(cough=input("cough: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())),salience = 1)
def symptom_4(self):
self.declare(Fact(fainting=input("fainting: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())),salience = 1)
def symptom_5(self):
self.declare(Fact(fatigue=input("fatigue: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())),salience = 1)
def symptom_6(self):
self.declare(Fact(sunken_eyes=input("sunken eyes: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())),salience = 1)
def symptom_7(self):
self.declare(Fact(low_body_temp=input("low body temperature: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())),salience = 1)
def symptom_8(self):
self.declare(Fact(restlessness=input("restlessness: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())),salience = 1)
def symptom_9(self):
self.declare(Fact(sore_throat=input("sore throat: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(fever=W())),salience = 1)
def symptom_10(self):
self.declare(Fact(fever=input("fever: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())),salience = 1)
def symptom_11(self):
self.declare(Fact(nausea=input("Nausea: ")))
@Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())),salience = 1)
def symptom_12(self):
self.declare(Fact(blurred_vision=input("blurred_vision: ")))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"
),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"
),Fact(nausea="yes"),Fact(blurred_vision="no"))
def disease_0(self):
self.declare(Fact(diseas
self.declare(Fact(disease="Jaundice"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),
Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),
Fact(nausea="no"),Fact(blurred_vision="no"))
def disease_1(self):
self.declare(Fact(disease="Alzheimers"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"
),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no")
,Fact(nausea="no"),Fact(blurred_vision="no"))
def disease_2(self):
self.declare(Fact(disease="Arthritis"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no
"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no
"),Fact(nausea="no"),Fact(blurred_vision="no"))
def disease_3(self):
self.declare(Fact(disease="Tuberculosis"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no
"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no
"),Fact(nausea="no"),Fact(blurred_vision="no"))
def disease_4(self):
self.declare(Fact(disease="Asthma"))
@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no
"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no
"),Fact(nausea="no"),Fact(blurred_vision="no"))
def disease_5(self):
self.declare(Fact(disease="Sinusitis"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"
),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no")
,Fact(nausea="no"),Fact(blurred_vision="no"))
def disease_6(self):
self.declare(Fact(disease="Epilepsy"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"
),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no")
,Fact(nausea="yes"),Fact(blurred_vision="no"))
def disease_7(self):
self.declare(Fact(disease="Heart Disease"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"
),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no")
,Fact(nausea="yes"),Fact(blurred_vision="yes"))
def disease_8(self):
self.declare(Fact(disease="Diabetes"))
@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),
Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),
Fact(nausea="yes"),Fact(blurred_vision="yes"))
def disease_9(self):
self.declare(Fact(disease="Glaucoma"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"
),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no")
,Fact(nausea="yes"),Fact(blurred_vision="no"))
def disease_10(self):
self.declare(Fact(disease="Hyperthyroidism"))
@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),
Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),
Fact(nausea="yes"),Fact(blurred_vision="no"))
def disease_11(self):
self.declare(Fact(disease="Heat Stroke"))
@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(che
st_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="no"
),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"
),Fact(nausea="no"),Fact(blurred_vision="no"))
def disease_12(self):
self.declare(Fact(disease="Hypothermia"))
@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
def disease(self, disease):
print("")
id_disease = disease
disease_details = get_details(id_disease)
treatments = get_treatments(id_disease)
print("")
print("The most probable disease that you have is %s\n" %(id_disease))
print("A short description of the disease is given below :\n")
print(disease_details+"\n")
print("The common medications and procedures suggested by other real doctors
are: \n")
print(treatments+"\n")
@Rule(Fact(action='find_disease'),
Fact(headache=MATCH.headache),
Fact(back_pain=MATCH.back_pain),
Fact(chest_pain=MATCH.chest_pain),
Fact(cough=MATCH.cough),
Fact(fainting=MATCH.fainting),
Fact(sore_throat=MATCH.sore_throat),
Fact(fatigue=MATCH.fatigue),
Fact(low_body_temp=MATCH.low_body_temp),
Fact(restlessness=MATCH.restlessness),
Fact(fever=MATCH.fever),
Fact(sunken_eyes=MATCH.sunken_eyes),
Fact(nausea=MATCH.nausea),
Fact(blurred_vision=MATCH.blurred_vision),N
Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),sa
lience = -999)
def not_matched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat,
fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
print("\nDid not find any disease that matches your exact symptoms")
lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue,
restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
max_count = 0
max_disease = ""
for key,val in symptom_map.items():
count = 0
temp_list = eval(key)
for j in range(0,len(lis)):
if(temp_list[j] == lis[j] and lis[j] == "yes"):
count = count + 1
if count > max_count:
max_count = count
max_disease = val
if_not_matched(max_disease)
if __name__ == "__main__":
preprocess()
engine = Greetings()
while(1):
engine.reset() # Prepare the engine for the execution.
engine.run() # Run it!
print("Would you like to diagnose some other symptoms?")
if input() == "no":
exit()
#print(engine.facts)
Output:
Conclusion:
In this assignment we have successfully implemented the Expert System of Hospitals and Medical
facilities