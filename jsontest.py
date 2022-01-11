import json

with open("data.json") as datafile:    
    data = json.load(datafile) 

check_state = data['incident']['state']
result_tuple = data['incident']['summary']
if check_state == 'open':
    event_type = 'ALERT'
else: 
    event_type = 'RESOLVE'
    result_tuple = f"{result_tuple} - RESOLVED!"
check_tuple = "{" + "\"Policy name\": " + data['incident']['policy_name'] + ", \"Condition Name\": " + data['incident']['condition_name'] + ", \"URL\": " + data['incident']['url'] + "}"
print(result_tuple)
print(check_tuple)