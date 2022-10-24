import sys


class Node:
    def __init__(self, key, el, prev, later=None):
        self.key = key
        self.el = el
        self.prev = prev
        self.after = later


class MyLinkedMap:
    def __init__(self, size=9767):
        self.hash = lambda x: sum([ord(i) for i in x]) % size
        self.data = [[] for _ in range(size)]
        self.current_prev = None

    def put(self, key, el):
        tmp_hash = self.hash(key)
        for ix, k in enumerate(self.data[tmp_hash]):
            if k.key == key:
                k.el = el
                return
        self.data[tmp_hash].append(Node(key, el, self.current_prev))
        if not (self.current_prev is None):
            self.current_prev.after = self.data[tmp_hash][-1]
        self.current_prev = self.data[tmp_hash][-1]

    def delete(self, key):
        tmp_hash = self.hash(key)
        for ix, k in enumerate(self.data[tmp_hash]):
            if k.key == key:
                deleted = self.data[tmp_hash].pop(ix)
                if not (deleted.prev is None):
                    deleted.prev.after = deleted.after
                if not (deleted.after is None):
                    deleted.after.prev = deleted.prev
                else:
                    self.current_prev = deleted.prev
                break

    def get(self, key):
        for i in self.data[self.hash(key)]:
            if i.key == key:
                return i
        return None


myset = MyLinkedMap()

for line in sys.stdin:
    if line[0:2] == 'pu':
        myset.put(line.split()[1], line.split()[2])
    elif line[0] == 'd':
        myset.delete(line.split()[1])
    elif line[0] == 'g':
        got = myset.get(line.split()[1])
        print('none' if got is None else got.el)
    elif line[0] == 'n':
        got = myset.get(line.split()[1])
        if got is None:
            print('none')
        else:
            got = got.after
            print('none' if got is None else got.el)
    else:
        got = myset.get(line.split()[1])
        if got is None:
            print('none')
        else:
            got = got.prev
            print('none' if got is None else got.el)