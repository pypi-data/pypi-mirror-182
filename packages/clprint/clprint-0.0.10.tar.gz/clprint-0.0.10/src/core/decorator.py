class ColorAssigner():
    """
        This class is used to assign color to the print function.
    """

    def __init__(self, color, isHighlight=False):
        self.color = color
        self.isHighlight = isHighlight

    def decorate(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print(self.color, end='')

            if self.isHighlight:
                print()
                print('------------------------------------')
                print()
            func(*args, **kwargs)
            if self.isHighlight:
                print()
                print('------------------------------------')
                print()
            print('\033[0m', end='')
        return wrapper


clprint_colors = {
    'red': ColorAssigner('\033[91m'),
    'green': ColorAssigner('\033[92m'),
    'blue': ColorAssigner('\033[94m'),
    'yellow': ColorAssigner('\033[93m'),
    'purple': ColorAssigner('\033[95m'),
}

clprint_highlighters = {
    'red': ColorAssigner('\033[91m', True),
    'green': ColorAssigner('\033[92m', True),
    'blue': ColorAssigner('\033[94m', True),
    'yellow': ColorAssigner('\033[93m', True),
    'purple': ColorAssigner('\033[95m', True),
}
