# Room Allocation System

When a new Fellow joins Andela (both in **Kenya** and **Nigeria**), they are assigned an office space and an optional living space if they choose to opt in. When a new Staff member joins, they are assigned an office space only.

In this exercise, you will be required to digitize and randomize a room allocation system for one of Andela Nigeria's facilities, _the Amity_.

The system has the following constraints

- Rooms in Amity can either be living spaces or office spaces.
- An office can accommodate a maximum of 6 people.
- A living space can accommodate a maximum of 4 people.
- A person to be allocated can either be a fellow or staff.
- Staff cannot be allocated living spaces.
- Since Living spaces are optional for fellows, they can to get one or not
- The system to be designed should allocate spaces to people randomly and automatically.

**Expected Functionality**

A command line interface using `docopt` that has the following commands :-

- `create_room <room_type> <room_name>` - Creates rooms in the Dojo
- `add_person <person_name> <FELLOW|STAFF> [wants_accommodation]` - Adds a person to the system and allocates the person to a random room. _wants_accommodation_ is an optional argument which can be either **Y** or **N**. The default value if not provided is **N**.
- `print_room <room_name>` - Prints the names of all the people in room_name on the screen.
- `print_allocations [-o=filename]` - Prints a list of allocations onto the screen. Specifying the optional `-o option` here outputs the registered allocations to a txt file.
- `print_unallocated [-o=filename]` - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.
- `reallocate_person <person_identifier> <new_room_name>` - Reallocate the person with person_identifier to new_room_name.
- `load_people` - Adds people to rooms from a txt file.
- `save_state [--db=sqlite_database]` - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.
- `load_state <sqlite_database>` - Loads data from a database into the application.
