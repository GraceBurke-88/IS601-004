from datetime import datetime
import copy
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    #check if current datetime is displaying correctly
    now = datetime.now()
    print("now =", now)
    # update lastActivity with the current datetime value
    task["lastActivity"] = now
    # set the name, description, and due date (all must be provided)
    # --> add new key value pairs
    if not name or not description or not due:
        print("Missing input")
    else:
        task["name"] = name
        print(task["name"])
        task["description"] = description
        print(task["description"])
        task["due"] = due
    # due date must match one of the formats mentioned in str_to_datetime()
        try:
            task["due"] = str_to_datetime(due)
        except ValueError:
            print("Error: Due date must match one of the following visual format: mm/dd/yy hh:mm:ss")
            return "Error: Due date must match one of the following visual format: mm/dd/yy hh:mm:ss"
        # add the new task to the tasks list
        else:
            tasks.append(task)
        # output a message confirming the new task was added or if the addition was rejected due to missing data
        print("Task added successfully: Name - {}, Description - {}, Due - {}".format(name, description, due))
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    gnb5 implemented on 2/18/23
    -------------------
    First I had to update the 'lastActivity' to have the current datatime value. 
    I used a print statement to make sure the datetime value was working correctly.
    Then I checked if there was input for all the values and if not print an error message.
    To set name/desc/due date I add in new key value pairs to the 'task' list.
    To check if current due dates matches a format of str_to_datetime() I used a 
    try: tests the code for errors (tests if due date matches str_to_datetime(due) format, a
    except: handles the error - prompts for a new input that has the correct format, 
    and else: append the task to the list if the formatting is correct.
    Last added and print statement and saved everything.
    '''
    

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    task = tasks[index]
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Error: Invalid index provided.")
        return
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    name = input(f"What's the name of this task? (Current value: {task['name']}) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (Current value: {task['description']}) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (Current value: {task['due']}) \n").strip()
    #pass the extracted input to update_task
    update_task(index, name=name, description=desc, due=due)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    gnb5 implemented on 2/18/23
    ------------------- 
    1. for the index passed through, found the task item in the list at that index
    2. if out of bounds (less index of 0 or greater than the length of the list) prints error message/ returns 
    3. Replaced TODO w/current value of each key which was found for the current task
    4. Passed index, name, description, and due parameters to the update_task function
    '''

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    task = tasks[index]
    # create a copy of the original task
    #https://medium.com/@ihuomacbasil/copy-in-python-deep-copy-and-shallow-copy-59b51bda7cde
    orig_task = task.copy()
    print(orig_task)
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Error: Invalid index provided.")
        return
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    if name:
        task["name"] = name
    if description:
        task["description"] = description
    if due:
        try:
            task["due"] = due
        except ValueError:
            print("Error: Due date must match one of the following visual format: mm/dd/yy hh:mm:ss")
            return "Error: Due date must match one of the following visual format: mm/dd/yy hh:mm:ss"
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    if orig_task != task:
        print("Task updated, items were changed.")
    else:
        print("Task not updated, no items were changed.")
    # update lastActivity with the current datetime value
    task["lastActivity"] = datetime.now()
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    gnb5 implemented on 2/20/23
    -------------------
    #1 find the task by index
    --> for the index passed through, found the task item in the list at that index
    #2	consider index out-of-bounds scenarios and include an appropriate message(s) for invalid index
    --> if out of bounds (less index of 0 or greater than the length of the list) prints error message/ returns 
    #3	update incoming task data if it's provided (if it's not provided use the original task property value)
    https://www.sololearn.com/Discuss/1582033/how-to-check-if-input-is-empty-in-python
    --> If provided (use if statements and 'true' if that variable is provided) then set the original task property value to the new value
    #4	update lastActivity with the current datetime value
    --> use datetime.now() module and set it equal to the last activity at the current task index
    #5	output that the task was updated if any items were changed, otherwise mention task was not updated
    --> Used an if/else statement, I have a variable set before any changes were made to save a local copy of the original task. If the original task has changed prints that items were changed, else prints there were no changes.
    #6	make sure save() is still called last in this function
    --> call save() at the end

    was running twice realized I had two calls to update_task in the process_update function
    '''

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    task = tasks[index]
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Error: Invalid index provided.")
        return
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    if task["done"]:
        task["lastActivity"] = datetime.now()
        print("Already done.")
    else:
        task["done"] = datetime.now()
        task["lastActivity"] = datetime.now()
        print("Task marked as done.")
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    gnb5 implemented on 2/20/23
    -------------------
    #1 find the task by index
    --> for the index passed through, found the task item in the list at that index
    #2	consider index out-of-bounds scenarios and include an appropriate message(s) for invalid index
    --> if out of bounds (less index of 0 or greater than the length of the list) prints error message/ returns 
    #3	if it's not done, record the current datetime as the value
    --> set 'done' property value to current datetime (using datetime.now()). Also, update lastActivity to the current time. 
    Last, printed out a message that the task was completed.
    #4	If it is done, print a message saying it's already completed
    -->  Update lastActivity to the current time (used datetime.now()), and use print to display a message that it's already done.
    #5	make sure save() is still called last in this function
    --> call save() at the end

    '''



def view_task(index):
    """ View more info about a specific task fetch by index """
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Error: Invalid index provided.")
        return
    # find task from list by index
    task = tasks[index]
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #task = {}
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    '''
    gnb5 implemented on 2/20/23
    -------------------
    #1 find the task by index
    --> for the index passed through, found the task item in the list at that index
    #2	consider index out-of-bounds scenarios and include an appropriate message(s) for invalid index
    --> if out of bounds (less index of 0 or greater than the length of the list) prints error message/ returns 
    #3	utilize the given print statement when a task is found
    '''

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Error: Invalid index provided.")
        return
    # delete/remove task from list by index
    del tasks[index]
    # message should show if it was successful or not
    print("Task deleted.")
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    save()
    '''
    gnb5 implemented on 2/20/23
    -------------------
    #1 find the task by index
    --> for the index passed through, found the task item in the list at that index
    #2	consider index out-of-bounds scenarios and include an appropriate message(s) for invalid index
    --> if out of bounds (less index of 0 or greater than the length of the list) prints error message/ returns 
    #3	delete/remove task from list by index
    source: https://www.programiz.com/python-programming/del
    --> use 'del' to delete items at a given index
    '''

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    incomplete_tasks = []
    for task in tasks:
        if not task['done']:
            incomplete_tasks.append(task)
    list_tasks(incomplete_tasks)
    '''
    gnb5 implemented on 2/20/23
    -------------------
    #1 generate a list of tasks where the task is not done
    --> Used a for loop to get tasks that are not done (aka 'false'), used .append to add them to the list
    #2 pass that list into list_tasks()
    --> code already provided
    '''

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    overdue_tasks = []
    now = datetime.now()
    for task in tasks:
    # generate a list of tasks where the due date is older than now and that are not complete
        if not task['done'] and task['due'] is not None:
            due_date = str_to_datetime(task['due'])
            if due_date < now:
                overdue_tasks.append(task)
    list_tasks(overdue_tasks)
    '''
    gnb5 implemented on 2/20/23
    -------------------
    #1generate a list of tasks where the due date is older than now and that are not complete
    --> Used a for loop to get tasks that are not done (aka 'false') and have a due date property
        covert the due date to datetime format using the provided function
        used comparison operator to find overdue times and used .append to add them to the list
    #2 pass that list into list_tasks()
    --> code already provided
    '''


def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Error: Invalid index provided, cannot provide time remaining.")
        return
    # get the task by index
    task = tasks[index]
    now = datetime.now()
    # get the days, hours, minutes, seconds between the due date and now
    time_remaining = str_to_datetime(task['due']) - now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    if time_remaining.total_seconds() < 0:
        overdue_time = abs(time_remaining)
        print(f"Task {index} is overdue by {overdue_time.days} days, {overdue_time.seconds // 3600} hours, {(overdue_time.seconds // 60) % 60} minutes, and {overdue_time.seconds % 60} seconds")
    else:
        print(f"Task {index} is due in {time_remaining.days} days, {time_remaining.seconds // 3600} hours, {(time_remaining.seconds // 60) % 60} minutes, and {time_remaining.seconds % 60} seconds.")
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #task = {}

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()