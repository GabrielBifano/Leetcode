# Keys and Rooms
# Medium

def canVisitAllRooms(rooms: 'list[list[int]]') -> bool:

    d = {}
    def visit(node, d, rooms):
        if d.get(node, False):
            return
        d[node] = True
        for key in rooms[node]:
            visit(key, d, rooms)

    visit(0, d, rooms)
    if len(d) < len(rooms): return False
    else: return True