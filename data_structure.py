import time
import random

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        # return self.items == []
        return not self.items
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def simulate_line(till_show, max_time):
    pq = Queue()
    tix_sold = []
    for i in range(100):
        pq.enqueue("person" + str(i))
    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
    return tix_sold

if __name__ == "__main__":
    # cabinet1 = Stack()
    # print(cabinet1.is_empty())
    # cabinet1.push(11)
    # print(cabinet1.is_empty())
    # cabinet1.pop()
    # print(cabinet1.is_empty())
    # cabinet2 = Stack()
    # for i in range(5):
    #     cabinet2.push(i)
    # print(cabinet2.peek())
    # print(cabinet2.size())
    # a_queue = Queue()
    # print(a_queue.is_empty())
    # a_queue.enqueue(11)
    # print(a_queue.is_empty())
    # a_queue.dequeue()
    # print(a_queue.is_empty())
    # b_queue = Queue()
    # for i in range(5):
    #     b_queue.enqueue(i)
    # print(b_queue.size())
    sold = simulate_line(50, 2)
    print(sold)
