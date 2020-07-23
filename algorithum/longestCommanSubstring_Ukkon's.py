def longestCommonSubstring(s, t):
    len_s = len(s)
    string = s + '#' + t + '$'
    len_string = len(string)
    max_len = 0

    class LeafNode():
        def __init__(self, from_first_word):
            self.from_first_word = from_first_word

        @property
        def has_s_leaves(self):
            return self.from_first_word

        @property
        def has_t_leaves(self):
            return not self.from_first_word

    class InternalNode():
        def __init__(self, root_length):
            self.edges = {}
            self.link = None
            self.root_length = root_length
            self.has_s_leaves = False
            self.has_t_leaves = False
            self.already_counted = False

        def __getitem__(self, key):
            return self.edges[key]

        def __setitem__(self, key, edge):
            self.edges[key] = edge
            self.has_s_leaves = self.has_s_leaves or edge.dest.has_s_leaves
            self.has_t_leaves = self.has_t_leaves or edge.dest.has_t_leaves

        def __contains__(self, key):
            return key in self.edges

    class Edge:
        def __init__(self, dest, start, end):
            self.dest = dest
            self.start = start
            self.end = end
            self.length = self.end - self.start

    root = InternalNode(0)

    class Cursor():
        def __init__(self):
            self.node = root
            self.edge = None
            self.idx = 0
            self.lag = -1

        def is_followed_by(self, letter):
            if self.idx == 0:
                return letter in self.node
            return letter == string[self.node[self.edge].start + self.idx]

        def defer(self, letter):
            self.idx += 1
            if self.edge is None:
                self.edge = letter
            edge = self.node[self.edge]
            if self.idx == edge.length:
                self.node = edge.dest
                self.edge = None
                self.idx = 0

        def post_insert(self, i):
            self.lag -= 1
            if self.node is root:
                if self.idx > 1:
                    self.edge = string[i - self.lag]
                    self.idx -= 1
                else:
                    self.idx = 0
                    self.edge = None
            self.node = self.node.link if self.node.link else root
            while self.edge and self.idx >= self.node[self.edge].length:
                edge = self.node[self.edge]
                self.node = edge.dest
                if self.idx == edge.length:
                    self.idx = 0
                    self.edge = None
                else:
                    self.idx -= edge.length
                    self.edge = string[i - self.lag + self.node.root_length]

        def split_edge(self):
            edge = self.node[self.edge]
            middle_node = InternalNode(self.node.root_length + self.idx)
            midpoint = edge.start + self.idx
            next_edge = Edge(edge.dest, midpoint, edge.end)
            middle_node[string[midpoint]] = next_edge
            edge.dest = middle_node
            edge.end = midpoint
            edge.length = midpoint - edge.start
            return middle_node
    cursor = Cursor()
    from_first_word = True
    dummy = InternalNode(0)
    for i, letter in enumerate(string):
        if from_first_word and i > len_s:
            from_first_word = False
        cursor.lag += 1
        prev = dummy
        while cursor.lag >= 0:
            if cursor.is_followed_by(letter):
                prev.link = cursor.node
                cursor.defer(letter)
                break
            elif cursor.idx != 0:
                stem = cursor.split_edge()
            else:
                stem = cursor.node
            stem[letter] = Edge(LeafNode(from_first_word), i, float("Inf"))
            if i > len_s and not stem.already_counted and stem.has_s_leaves and stem.has_t_leaves:
                stem.already_counted = True
                if stem.root_length > max_len:
                    max_len = stem.root_length
            prev.link = prev = stem
            cursor.post_insert(i)
    return max_len


s, t = "zxabcdezy", "yzabcdezx"
print(longestCommonSubstring(s, t))