from collections import deque

def asteroidCollision(asteroids: 'list[int]') -> 'list[int]':
    
    stack = []
    asteroids = deque(asteroids)

    while len(asteroids) > 0:        
        
        new = asteroids.popleft()
        if len(stack) == 0 or new > 0 or stack[-1] < 0:
            stack.append(new)
            continue
        
        while new < 0 and stack[-1] >= 0 and len(stack) > 0:
            if -new == stack[-1]:
                stack.pop()
                break
            elif -new < stack[-1]:
                break
            else:
                stack.pop()
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(new)
                    break
    return stack