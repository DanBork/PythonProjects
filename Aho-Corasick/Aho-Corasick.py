class AhoCorasick:
    def __init__(self):
        self.tree = {}
        self.output = {}
        self.fail = {}

    def add_pattern(self, pattern):     # Add each character of a pattern to the tree, marking it in self.output
        current_node = self.tree
        for char in pattern:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        if id(current_node) not in self.output:
            self.output[id(current_node)] = []
        self.output[id(current_node)].append(pattern)

    def build(self):    # build the tree
        # Initialize the fail function for the root's children
        queue = []
        for char, child in self.tree.items():
            self.fail[id(child)] = self.tree
            queue.append(child)

        # SCan over tree to construct fail links
        while queue:
            current_node = queue.pop(0)

            for char, child in current_node.items():
                queue.append(child)

                # Set fail link
                fail_node = self.fail[id(current_node)]
                while fail_node is not None and char not in fail_node:
                    fail_node = self.fail.get(id(fail_node))
                self.fail[id(child)] = fail_node[char] if fail_node else self.tree

                # Merge output of fail link into the child
                if id(self.fail[id(child)]) in self.output:
                    if id(child) not in self.output:
                        self.output[id(child)] = []
                    self.output[id(child)].extend(self.output[id(self.fail[id(child)])])

    def search(self, text):     # search for all the patterns in text
        current_node = self.tree
        results = []

        for i, char in enumerate(text):
            # Follow fail links if necessary
            while current_node is not None and char not in current_node:
                current_node = self.fail.get(id(current_node))

            if current_node is None:
                current_node = self.tree
                continue

            current_node = current_node[char]
            if id(current_node) in self.output:
                for pattern in self.output[id(current_node)]:
                    results.append((i - len(pattern) + 1, pattern))

        return results


# Example pattern and text
patterns = ["co", "nut", "con"]
text = "coconut nut"

test = AhoCorasick()
for pattern in patterns:
    test.add_pattern(pattern)

test.build()
results = test.search(text)

print("Matches:", results)