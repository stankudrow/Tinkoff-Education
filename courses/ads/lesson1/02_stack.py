#!/usr/bin/env python3
"""Stack implementation."""


from typing import Any, Optional, Sequence


class Stack:
    """Stack."""

    def __init__(self, seq: Optional[Sequence] = None):
        if seq is None:
            self._stack = []
        else:
            self._stack = list(seq)

    def __bool__(self) -> bool:
        """Returns the boolean value of the stack."""
        return bool(self._stack)

    def __len__(self) -> int:
        """Return the length/size of the stack."""
        return len(self._stack)

    def clear(self):
        """Clear the stack."""
        self._stack.clear()

    def pop(self) -> Any:
        """Pops the top element from the stack."""
        return self._stack.pop()

    def push(self, value):
        """Push the value onto the stack."""
        self._stack.append(value)

    @property
    def top(self) -> Any:
        """Returns the top element.

        Raises
        ------
        IndexError
            if the stack is empty.
        """
        return self._stack[-1]


if __name__ == "__main__":
    stack = Stack()
    while (command := input("command: ")) != "exit":
        match command:
            case "push":
                args = input("push: ").split()
                for arg in args:
                    stack.push(arg)
                print("OK")
            case "pop":
                if stack:
                    print(stack.pop())
                else:
                    print("Error")
            case "back":  # top
                if stack:
                    print(stack.top)
                else:
                    print("Error")
            case "size":
                print(len(stack))
            case "clear":
                stack.clear()
                print("OK")
            case _:
                print(f"Unknown command `{command}`.")
    print("Bye")
