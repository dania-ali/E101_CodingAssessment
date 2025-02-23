# main.py

import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    
#Function to find suitable docking bays based on ship size
def find_docking_bays(db.incoming_ships, db.incoming_ships):
    #intializing a dictionary for the scheduele, will append apprpriate data later
    docking_scheduele = []
    #goes through checking each ship
    for ship in incoming_ships:
        #goes through each bay
        for bay in docking_bays:
            #used learnpython.com to find syntax for using dictionary data
            if ship['size'] == bay['size']:
                #appending the appropriate data to the scedhuele
                docking_scheduele.append({'ship': ship['ship_name'], 'bay': bay['bay_id']})
    #returns data to user
    return docking_scheduele

def timeslot_availability(arrival_time, departure_time, bay_scheduele):
    for reservation in bay_scheduele:
        #cases that would cause an overlap: new ship arrives before current ship leaves
        #new ship leaves after current ship arrives
        if (arrival_time < booked_departure and departure_time > booked_arrival):
            #tell user theres a conflict
            return False
        #otherwise there is no conflict
        return True

def format_scheduele(docking_bays):
    #intiliazing the formatted scheduele
    formatted_scheduele = []
    #goes through each bay
    for bay in docking_bays:
        #goes through each reservation in the sceduele created above
        for reservation in docking_scheduele:
            #creates the format
            formatted_scheduele.append(f"Bay {bay_id}: {ship_name} - {arrival_time} to {departure_time}")
    #sends formatted scheduele back to user
    return formatted_scheduele

# prints the scehdele
schedule = find_docking_bays(incoming_ships, docking_bays)
for entry in schedule:
    print(f"{entry['ship']} -> Bay {entry['bay']}")

# Prints formatted schedule
formatted_schedule = format_docking_schedule(docking_bays)
for entry in formatted_schedule:
    print(entry)

if __name__ == "__main__":
    main()

