import random
import os


GRID_WIDTH = 20
GRID_HEIGHT = 10
WALL = '#'
FLOOR = '.'
PLAYER = '@'
EMPTY = ' '


grid = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
player_x, player_y = 1, 1


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_walls():
    for x in range(GRID_WIDTH):
        grid[0][x] = WALL
        grid[GRID_HEIGHT - 1][x] = WALL
    for y in range(GRID_HEIGHT):
        grid[y][0] = WALL
        grid[y][GRID_WIDTH - 1] = WALL


def generate_room():
    room_width = random.randint(3, 6)
    room_height = random.randint(3, 6)
    room_x = random.randint(1, GRID_WIDTH - room_width - 1)
    room_y = random.randint(1, GRID_HEIGHT - room_height - 1)
    
    for y in range(room_y, room_y + room_height):
        for x in range(room_x, room_x + room_width):
            grid[y][x] = FLOOR
    
    return room_x, room_y


def generate_corridor(x1, y1, x2, y2):
    if x1 != x2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] = FLOOR
    if y1 != y2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x2] = FLOOR


def generate_level():
    draw_walls()
    rooms = []
    for _ in range(random.randint(3, 5)):
        room_x, room_y = generate_room()
        rooms.append((room_x, room_y))
    for i in range(1, len(rooms)):
        generate_corridor(rooms[i - 1][0], rooms[i - 1][1], rooms[i][0], rooms[i][1])


def render():
    clear_screen()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if x == player_x and y == player_y:
                print(PLAYER, end='')
            else:
                print(grid[y][x], end='')
        print()


def move_player(dx, dy):
    global player_x, player_y
    new_x = player_x + dx
    new_y = player_y + dy
    if grid[new_y][new_x] == FLOOR:
        player_x = new_x
        player_y = new_y


def game_loop():
    global player_x, player_y
    generate_level()
    render()
    
    while True:
        command = input("Enter input : ").lower()
        render()
        if command == "z":
            move_player(0, -1)
        elif command == "s":
            move_player(0, 1)
        elif command == "q":
            move_player(-1, 0)
        elif command == "d":
            move_player(1, 0)
        elif command == 'm':
            print("Quitting")
            break

if __name__ == "__main__":
    game_loop()
