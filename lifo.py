import queue 

my_stack = queue.LifoQueue(maxsize=0)

my_stack.put('a')
my_stack.put('b')
my_stack.put('z')
print(my_stack.empty())