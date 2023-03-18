import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

'''
# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False

'''


# add required test cases below
# Test 1 - bun must be the first selection (can't add patties/toppings without a bun choice)
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
def test_patties_in_stock(machine):
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
def test_toppings_in_stock(machine):
    machine.handle_bun("white burger bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")

    # Set the quantity of the "Lettuce" topping to 0
    machine.toppings[7].quantity = 0
    assert machine.toppings[7].quantity == 0

    # Try to add the "Lettuce" topping, which should raise an OutOfStockException
    with pytest.raises(OutOfStockException):
        machine.handle_toppings("bbq")

    # Add a topping that is in stock to verify that toppings can still be added
    machine.handle_toppings("cheese")
    assert len(machine.inprogress_burger) == 6

