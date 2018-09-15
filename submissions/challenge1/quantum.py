"""
Submission by juan (kingdom5500)
994 bytes
"""

reverse_polish = lambda expression: ((lambda PolishStack, split: ((lambda stack: tuple(stack.push(float(item)) if item.isdigit() else stack.operate(item) for item in split(expression)) and stack.pop())(stack=PolishStack())))(PolishStack = type("Stack", (), {"__init__": lambda self: (setattr(self, "_tuple", ())), "push": lambda self, item: (setattr(self, "_tuple", (item, *self._tuple))), "pop": lambda self: ((lambda tmp: tmp.add(self._tuple[0] if self._tuple else None) or setattr(self, "_tuple", self._tuple[1:]) or tmp.pop())(set())), "operate": lambda self, operator: ((lambda operation: self.push(operation(*(self.pop(), self.pop())[::-1])))(operation = {"+": float.__add__, "-": float.__sub__, "/": float.__truediv__, "*": float.__mul__, "^": float.__pow__}[operator]))}), split = lambda string: ((lambda spaces: (string[start:end - 1] for start, end in zip((0, *spaces), (*spaces, len(string) + 1))))(spaces = tuple(index + 1 for index, char in enumerate(string) if char.isspace())))))

