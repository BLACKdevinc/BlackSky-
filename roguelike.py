

class RogueLike:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.player_pos = [1, 1]
        self.exit_pos = [width - 2, height - 2]
        self.level = self.generate_level()
        self.level[self.exit_pos[1]][self.exit_pos[0]] = "E"

    def generate_level(self):
        # Create an empty grid
        level = [["#" for _ in range(self.width)] for _ in range(self.height)]
        
        # Create random walk paths
        x, y = 1, 1  # Start position
        level[y][x] = "."
        
        for _ in range(self.width * self.height // 2):
            direction = random.choice(["up", "down", "left", "right"])
            if direction == "up" and y > 1:
                y -= 1
            elif direction == "down" and y < self.height - 2:
                y += 1
            elif direction == "left" and x > 1:
                x -= 1
            elif direction == "right" and x < self.width - 2:
                x += 1
            level[y][x] = "."
        
        return level

    def display_level(self):
        for y, row in enumerate(self.level):
            for x, cell in enumerate(row):
                if [x, y] == self.player_pos:
                    print("@", end="")  
                else:
                    print(cell, end="")
            print()
        print()

    def move_player(self, direction):
        x, y = self.player_pos
        if direction == "z" and y > 0 and self.level[y - 1][x] in [".", "E"]:
            self.player_pos[1] -= 1
        elif direction == "s" and y < self.height - 1 and self.level[y + 1][x] in [".", "E"]:
            self.player_pos[1] += 1
        elif direction == "q" and x > 0 and self.level[y][x - 1] in [".", "E"]:
            self.player_pos[0] -= 1
        elif direction == "d" and x < self.width - 1 and self.level[y][x + 1] in [".", "E"]:
            self.player_pos[0] += 1

    def play(self):
        
        
        while True:
            os.system('clear')
            self.display_level()
            if self.player_pos == self.exit_pos:
                print("Congratulations! You reached the exit!")
                break
            
            move = input("Your move: ").lower()
            if move == "q":
                break
            elif move in ["z", "q", "s", "d"]:
                self.move_player(move)
            else:
                print("Invalid input! Use W/A/S/D to move, or Q to quit.")


