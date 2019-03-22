"""
Exam 1, problem 1. 15 Points
Authors: Every CSSE faculty member, Dr. Brackin, and Keely Stevenson.
"""
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """

    ###########################################################################
    # UN-comment tests as you work the problems.
    ###########################################################################


    run_test_init()
    run_test_go_to_floor()
    run_test_get_passengers()
    test_passengers_exit()


###############################################################################
# The   Elevator class (and its methods) begins here.
###############################################################################

class Elevator(object):
    """
    An Elevator has:
        -- OCCUPANTS, which is the number of humans currently on the elevator,
        -- CAPACITY, which is the maximum number of humans allowed on the elevator,
        -- NUMBER OF FLOORS, which is a non-negative integer and is the number of floors
                             that the elevator can access,
        -- CURRENT FLOOR is the floor at which the elevator resides.
                         The CURRENT FLOOR can never be greater than the NUMBER OF FLOORS.
    """

    def __init__(self, capacity, num_floors):
        """
        What comes in:
          -- self
          -- An integer that is the maximum number of humans allowed on the elevator
          -- An integer that is the number of floors that the elevator reaches
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Maintains the number of humans on the elevator
          -- Maintains a record of the current floor
          -- Also initializes other instance variables as needed
              by other methods.
        Examples:
          e1 = Elevator(20, 18)
          #   e1.capacity is 20
          #   e1.num_floors is 18

          e2 = Elevator(10, 8)
          #   e2.capacity is 10
          #   e2.num_floors is 8

        Type hints:
          :type capacity: int
          :type num_floors: int
        """
        # ---------------------------------------------------------------------
        #     DONE: 2. Implement and test this function. (3 pts)
        #     See the testing code (below) for more examples.
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        self.capacity = capacity
        self.occupants = 0
        self.num_floors = num_floors
        self.current_floor = 1


    def go_to_floor(self,floor):
        """
        What comes in:
          -- self
          -- a positive integer, floor, that is the desired floor
        What goes out:
          --Returns False if the floor requested is not a valid floor
          --Returns True if the floor is updated to the requested floor
        Side effects:
          -- Sets the elevator's current floor to floor given, unless
             the value of floor is greater than the number of floors allowed.
             If the value of floor is greater than the number of floors allowed,
             the elevator remains where it is.
        Examples:
          e1 = Elevator(20, 18)
          e1.go_to_floor(4)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   the current floor is set to 4
          #   True is returned by the method

          e1 = Elevator(20, 18)
          e1.go_to_floor(35)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   the current floor does not change
          #   False is returned by the method
        """
        # ---------------------------------------------------------------------
        #     DONE: 4. Implement the go_to_floor method. (3 pts)
        #     Write the testing code (below) before writing this method.
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        if floor > self.num_floors:
            return False
        else:
            self.current_floor = floor
            return True


    def get_passengers(self,num_passengers):
        """
        What comes in:
          -- self
          -- a positive integer, num_passengers, that is
             number of passengers who want to get on the elevator
        What goes out:
          -- Returns False if adding the passengers will exceed
             the capacity of the elevator
        Side effects:
          -- Updates the number of passengers on the elevator, unless
             the total of passengers will be greater than the maximum capacity.
             If the total will be greater than the maximum capacity,
             no one is allowed to enter the elevator.
        Examples:
          e1 = Elevator(20, 18)
          e1.get_passengers(4)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   you will update the number of people on the elevator
          #   unless the capacity has already been exceeded.
          #   True is returned if all passengers are successfully added

          e1 = Elevator(20, 18)
          e1.get_passengers(35)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   this exceeds the number of allowed passengers
          #   no passengers are added
          #   False is returned by the method
        """
# ---------------------------------------------------------------------
#     DONE: 6. Implement the get_passengers method. (3 pts)
#     Write the testing code (below) before writing this function.
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
        new_occupancy = self.occupants + num_passengers
        if new_occupancy > self.capacity:
            return False
        else:
            self.occupants = new_occupancy
            return True

# ---------------------------------------------------------------------
#     DONE: 7. Write methods, AS NEEDED, to allow passengers to exit
#      the elevator.  Show that your solution works with a test case. (2 pts)
#     Write the testing code (below) before writing this function.
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
    def passengers_exit(self, num_passengers):
        """ Allows passengers to exit the elevator, returns True if there are enough passengers
            to leave and returns False if there are not. Adjusts the number of occupants as
            necessary"""
        if self.occupants < num_passengers:
            return False
        else:
            self.occupants = self.occupants - num_passengers
            return True

def test_passengers_exit():
    """Tests the passengers_exit function above"""
    # Test 1:
    e1 = Elevator(15, 30)
    e1.get_passengers(3)
    e1.go_to_floor(5)
    actual = e1.passengers_exit(2)
    print('Test 1:')
    print('Expected passengers exit:', True)
    print('Expected occupancy: ', 1)
    print('Actual passengers exit:', actual)
    print('Actual occupancy:    ', e1.occupants)

    # Test 2:
    e2 = Elevator(6, 13)
    e2.get_passengers(4)
    e2.go_to_floor(11)
    e2.get_passengers(1)
    e2.go_to_floor(3)
    actual = e2.passengers_exit(6)
    print('Expected passengers exit:', False)
    print('Expected occupancy: ', 5)
    print('Actual passengers exit:', actual)
    print('Actual occupancy:    ', e2.occupants)

###############################################################################
# The TEST functions for the  Elevator  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the Elevator class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Elevator class.')
    print('-----------------------------------------------------------')

    # Test 1:  Creates elevator for small building.
    e1 = Elevator(20, 18)
    expected_capacity = 20
    expected_num_floors = 18
    print("Expected:", expected_capacity, expected_num_floors)
    print("Actual:  ", e1.capacity, e1.num_floors)
    if (expected_capacity == e1.capacity) and (expected_num_floors == e1.num_floors):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()


def run_test_go_to_floor():
    """ Tests the   go_to_floor method of the Elevator class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   go_to_floor   method of the Elevator class.')
    print('-----------------------------------------------------------')
    #     DONE: 3. Write tests for the go_to_floor method. (2 pts)
    #     A recommended format is shown below.  Be sure to
    #     add your actual code where indicated.  Include two
    #     test cases - one that works and one that returns False
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    # Test 1:  Sends elevator to 4th floor.
    e1 = Elevator(20, 18)
    expected_capacity = 20
    expected_num_floors = 18
    expected_go_to_floor = 4
    print('Expected: go_to_floor returns :', True)
    print("Expected:", expected_capacity, expected_num_floors, expected_go_to_floor)
    ################################################################
    #
    #     Add your values for actual below here
    #
    ################################################################
    print()
    answer = e1.go_to_floor(4)
    print('Actual: go_to_floor returns :',answer)
    print('Actual:  ', e1.capacity, e1.num_floors, e1.current_floor)
    print()

    # Test 2:
    e2 = Elevator(11, 6)
    expected_capacity = 11
    expected_num_floors = 6
    expected_go_to_floor = 2
    print('Expected: go_to_floor returns:', False)
    print('Expected:', expected_capacity, expected_num_floors, expected_go_to_floor)
    print()
    e2.go_to_floor(2)
    answer = e2.go_to_floor(8)
    print('Actual: go_to_floor returns:', answer)
    print('Actual:', e2.capacity, e2.num_floors, e2.current_floor)


def run_test_get_passengers():
    """ Tests the   get_passengers method of the Elevator class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_passengers   method of the Elevator class.')
    print('-----------------------------------------------------------')
    #     DONE: 5. Write tests for the get_passengers method. (2 pts)
    #     A recommended format is shown below.  Be sure to
    #     add your actual code where indicated.  Include several
    #     test cases - at least one that works
    #     and one that returns False
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    # Test 1:  Adds 2 passengers to an empty elevator.
    e1 = Elevator(20, 18)
    expected_capacity = 20
    expected_num_floors = 18
    expected_num_passengers = 2
    print('Expected passengers returns ', True)
    print("Expected:", expected_capacity, expected_num_floors, expected_num_passengers)

    ################################################################
    #
    #     Add your values for actual below here
    #
    ################################################################
    actual = e1.get_passengers(2)
    print("Actual passengers returns:  ", actual)
    print('Actual:  ', e1.capacity, e1.num_floors, e1.occupants)
    print()

    # Test 2:
    e2 = Elevator(10, 30)
    expected_capacity = 10
    expected_num_floors = 30
    expected_num_passengers = 3
    print('Expected passengers returns:', False)
    print('Expected:', expected_capacity, expected_num_floors, expected_num_passengers)
    e2.get_passengers(3)
    e2.go_to_floor(6)
    actual = e2.get_passengers(16)
    print('Actual passengers returns:', actual)
    print('Actual:', e2.capacity, e2.num_floors, e2.occupants)


def print_failure_message():
    print('  *** FAILED the above test. ***')

    """ Prints a message . """


main()