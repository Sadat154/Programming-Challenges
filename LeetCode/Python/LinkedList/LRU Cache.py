class Node:
    def __init__(self, key, value):
        self.key = key      # for LRU Cache, you usually store key and value
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0) # Most recently used
        self.tail = Node(0, 0) # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}


    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)

        if node == -1:
            return -1

        self._remove(node)
        self._add_to_front(node)




        return node.value



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            # Remove the LRU from the list and cache
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]



# ###class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.cap = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#
#         if len(self.cache) > self.cap:
#             self.cache.popitem(last=False)
