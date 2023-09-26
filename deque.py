from collections import deque

d = deque()

# Append right
d.append('a')
d.append('b')

# Append left
d.appendleft('b')

# Add many elements on right
d.extend('cdef')

# Add many elements on left
d.extendleft('fdsa')

# Add on position 5
d.insert(5, 'k')

# Remove on right
d.pop()

# Remove on left
d.popleft()

# Remove specific element
d.remove('b')

# Reverse
d.reverse()

# Brings the first element to the front of the deck
d.rotate()

# Clear all
d.clear()

print(d)