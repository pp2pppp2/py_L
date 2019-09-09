def isFull():
    global rear,front
    return (rear+1) % len(Q) == front
def isEmpty():
    global front,rear
    return front == rear
def enQueue(item):
    global rear
    if isFull(): print("Queue FULL")
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty(): print("Queue EMPTY")
    else:
        front = (front + 1) % len(Q)
        return Q[front]

def Qpeek():
    return Q[front+1]

SIZE = 3
Q = [0] * SIZE
front , rear = 0 , 0

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(front)
print(rear)
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
print(Q)
print(isFull())

print(deQueue())
print(deQueue())
print(deQueue())


Q = []

Q.append(1)
Q.append(2)
Q.append(3)
print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))

