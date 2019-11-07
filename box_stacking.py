# O(n^3) solution
boxes = [(2, 1, 4), (4, 1, 2), (5, 3, 2), (5, 2, 3), (4, 2, 1), (3, 2, 5)]
BP = [box[2] for box in boxes]
box_below = [None for _ in boxes]


def box_is_smaller(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    if x1 < x2 and y1 < y2:
        return True
    else:
        return False


for _ in boxes:
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if i == j:
                pass
            else:
                BP[i] = boxes[i][2] + BP[j] if box_is_smaller(boxes[i], boxes[j]) else BP[i]
                if box_is_smaller(boxes[i], boxes[j]):
                    box_below[i] = j

print(max(BP))
