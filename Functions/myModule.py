print("This is myModule")

def findIndex(listName, item):
    for i, value in enumerate(listName):
        if value == item:
            return i
    return -1