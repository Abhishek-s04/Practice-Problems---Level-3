# The following are the details of trains:
# List of train details
train_list = [
    {"train_no": 16453, "name": "Prasanti Express", "from": "SBC", "to": "BBS", 
     "days_of_run": ['Mo', 'We', 'Th'], "sleeper_fare": 600, "ac_fare": 987},
    
    {"train_no": 25627, "name": "Karnataka Express", "from": "SBC", "to": "DEC", 
     "days_of_run": ['Su', 'Tu'], "sleeper_fare": 1600, "ac_fare": 2500},
    
    {"train_no": 22642, "name": "Trivandrum SF Express", "from": "VSKP", "to": "TVM", 
     "days_of_run": ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'], "sleeper_fare": 800, "ac_fare": 1256},
    
    {"train_no": 22905, "name": "Okha Howrah Express", "from": "ST", "to": "KOAA", 
     "days_of_run": ['We', 'Sa'], "sleeper_fare": 987, "ac_fare": 2879}
]

# Function to get the train name and details by train number
def get_train_name(train_no):
    for train in train_list:
        if train["train_no"] == train_no:
            return train
    return "Invalid Train_no"

# Function to get the train numbers running on a particular day
def get_trains_for_day(day_of_run):
    valid_days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    
    if day_of_run not in valid_days:
        return "Invalid day"
    
    trains_running = []
    for train in train_list:
        if day_of_run in train["days_of_run"]:
            trains_running.append(train["train_no"])
    
    return trains_running

# Function to calculate the total fare based on the passenger details
def get_total_fare(train_no, passenger_dict):
    # Find the train details using the train number
    train = get_train_name(train_no)
    
    # If the train number is invalid, return the error message
    if train == "Invalid Train_no":
        return "Invalid Train_no"
    
    # Calculate the total fare
    total_fare = 0
    sleeper_fare = passenger_dict.get("sleeper", 0) * train["sleeper_fare"]
    ac_fare = passenger_dict.get("ac", 0) * train["ac_fare"]
    total_fare = sleeper_fare + ac_fare
    
    return total_fare

train_no = 25627
day_of_run = "We"
passenger_dict = {"sleeper": 10, "ac": 10}

print(get_train_name(train_no))  
print(get_trains_for_day(day_of_run)) 
print(get_total_fare(22642, passenger_dict)) 
