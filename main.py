import threading
import time

total = 0


def add_item():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item 1')
        total += 1
    print('Creation 1 is done')


def add_item_2():
    global total
    for i in range(7):
        time.sleep(2)
        print('added item 2')
        total += 1
    print('creation 2 is done')


# function limits_items() will diminish the value of total
def limits_items():
    global total
    while True:
        if total > 5:
            print('overload')
            total -= 3
            print('substracted 3')
        else:
            time.sleep(1)
            print('waiting')


# Create threads on the functions
creator1 = threading.Thread(target=add_item)
creator2 = threading.Thread(target=add_item_2)

""" daemon = true means that when the threads above will finish the program will automatically 
break the thread and execute the main program"""
limitor = threading.Thread(target=limits_items, daemon=True)

#Launch the threads
creator1.start()
creator2.start()
limitor.start()

# the main program will be executed only after the end of the thread's program
creator1.join()
creator2.join()


print('Our ending value Total is equal to ', total)
