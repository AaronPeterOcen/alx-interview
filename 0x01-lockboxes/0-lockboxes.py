#!/usr/bin/python3
"""
working with lockboxes
"""


def canUnlockAll(boxes):
    """ n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.
    a method that determines if all the boxes can be opened. """
    if not boxes or type(boxes) is not list:
        return False
    unlocked_boxes = [0]
    for i in unlocked_boxes:
        for key in boxes[i]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)
    return len(unlocked_boxes) == len(boxes)
