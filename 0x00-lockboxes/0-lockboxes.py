#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    openedBoxes= {}
    listBoxes = [0]

    while listBoxes:
        boxNum = listBoxes.pop(0)
        openedBoxes[boxNum] = 1
        for key in boxes[boxNum]:
            if key > -1 and key < len(boxes) and not openedBoxes.get(key)\
                    and (key not in listBoxes):
                listBoxes.append(key)

    return True if (len(openedBoxes) == len(boxes)) else False