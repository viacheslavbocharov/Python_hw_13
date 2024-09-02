class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        if min_value > current or max_value < current:
            raise ValueError(
                f"Current value must be between min({min_value}) and max({max_value})"
            )
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            print(
                f'The current value must be between min({self.min_value}) '
                f'and max({self.max_value})'
            )

    def set_max(self, max_max):
        if max_max > self.min_value and max_max >= self.current:
            self.max_value = max_max
        else:
            print(
                f"The maximum value cannot be less than minimum({self.min_value}) "
                f"or current({self.current}) value"
            )

    def set_min(self, min_min):
        if min_min < self.max_value and min_min <= self.current:
            self.min_value = min_min
        else:
            print(
                f"The minimum value cannot be more than maximum({self.max_value}) "
                f"or current({self.current}) value"
            )

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("The current value reached the maximum")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("The current value reached the minimum")

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print(counter.get_current())
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
