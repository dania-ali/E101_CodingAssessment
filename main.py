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
                
# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    
    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

if __name__ == "__main__":
    main()

