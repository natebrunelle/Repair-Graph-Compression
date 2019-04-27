# Modified from: https://www.geeksforgeeks.org/priority-queue-in-python/

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def empty(self):
        return len(self.queue) == ()

    def insert(self, data):
        self.queue.append(data)

    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item

        except IndexError:
            print()
            exit()