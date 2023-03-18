import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException, InvalidPaymentException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# add required test cases below
# Test 1 - bun must be the first selection (can't add patties/toppings without a bun choice)
''' gnb5 3/18/23 '''
def test_bun_first_selection(machine):
    with pytest.raises(InvalidStageException):
        # try to add a patty without selecting a bun first
        print("add a patty without selecting a bun first raises InvalidStageException")
        machine.handle_patty("veggie")
    
    with pytest.raises(InvalidStageException):
        # try to add toppings without selecting a bun first
        print("add toppings without selecting a bun first raises InvalidStageException")
        machine.handle_toppings("cheese")

        

# Test 2 - can only add patties if they're in stock
''' gnb5 3/18/23 '''
def test_patties_in_stock(machine):
    machine.reset()
    # make sure there are initial patties in stock
    print(machine.patties[0])
    assert machine.patties[0].quantity > 0
    assert machine.patties[1].quantity > 0
    print(machine.patties[2])
    assert machine.patties[2].quantity > 0

    # select a bun first
    machine.handle_bun("white burger bun")

    # add a patty that's in stock
    # had to change the initial quatity of beef patties to 2
    machine.handle_patty("beef")
    assert machine.remaining_patties == 2
    assert machine.patties[2].quantity == 1 #assuming that the initial quantity is 10 for beef patties

    # try to add a patty that's out of stock
    machine.handle_patty("beef")
    
    with pytest.raises(OutOfStockException):
        machine.handle_patty("beef")
    

# Test 3 - can only add toppings if they're in stock
''' gnb5 3/18/23 '''
def test_toppings_in_stock(machine):
    machine.reset()

    machine.handle_bun("white burger bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")

    # Set the quantity of the "BBQ" topping to 0
    machine.toppings[7].quantity = 0
    assert machine.toppings[7].quantity == 0

    # Try to add the "BBQ" topping, which should raise an OutOfStockException
    with pytest.raises(OutOfStockException):
        machine.handle_toppings("bbq")

    # Add a topping that is in stock to verify that toppings can still be added
    machine.handle_toppings("cheese")
    assert len(machine.inprogress_burger) == 3

#  Test 4 - Can add up to 3 patties of any combination
def test_adding_patties(machine):
    machine.reset()
    #increment beef patties to 1 
    machine.patties[2].quantity = 1
    print(len(machine.inprogress_burger))
    # select a bun first
    machine.handle_bun("white burger bun")

    # add 3 patties
    machine.handle_patty("beef")
    machine.handle_patty("turkey")
    machine.handle_patty("veggie")

    # verify that all 3 patties are in the inprogress burger list
    assert len(machine.inprogress_burger) == 4
    assert machine.inprogress_burger[1].name.lower() == "beef"
    assert machine.inprogress_burger[2].name.lower() == "turkey"
    assert machine.inprogress_burger[3].name.lower() == "veggie"

    # try to add another patty, which should raise an ExceededRemainingChoicesException
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_patty("beef")

    print(len(machine.inprogress_burger))

# Test 5 - Can add up to 3 toppings of any combination

def test_adding_toppings(machine):
    machine.reset()
    print(len(machine.inprogress_burger))
    #BBQ gets quantity of 5
    machine.toppings[7].quantity = 5

    # select a bun first
    machine.handle_bun("white burger bun")
    machine.handle_patty("next")
    print(len(machine.inprogress_burger))
    # add some toppings
    machine.handle_toppings("lettuce")
    machine.handle_toppings("tomato")
    machine.handle_toppings("bbq")

    # check the in-progress burger
    assert len(machine.inprogress_burger) == 4
    assert machine.inprogress_burger[1].name == "Lettuce"
    assert machine.inprogress_burger[2].name == "Tomato"
    assert machine.inprogress_burger[3].name == "BBQ"

    # try to add a fourth topping
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_toppings("pickle")

    # check that the in-progress burger hasn't changed
    assert len(machine.inprogress_burger) == 4
    assert machine.inprogress_burger[1].name == "Lettuce"
    assert machine.inprogress_burger[2].name == "Tomato"
    assert machine.inprogress_burger[3].name == "BBQ"

# Test 6 - cost must be calculated properly based on the choices (check for currency format as part of this) (test case should have a few permutations of at least 3 valid burgers)
def test_cost_calculation(machine):
    machine.reset()
    machine.patties[2].quantity = 5
    # Test a few permutations of valid burgers
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == 1.0
    machine.handle_pay(1.0,"1.0")
    

    # A burger with no toppings or extra patties
    machine.reset()
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == 2.0
    machine.handle_pay(2.0, "2.0")
    
    # A burger with two toppings and one extra patty
    machine.reset()
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == 3.5
    machine.handle_pay(3.5, "3.5")

    # Test invalid currency format
    machine.reset()
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_toppings("done")
    with pytest.raises(InvalidPaymentException):
        machine.handle_pay(100, "invalid currency format")