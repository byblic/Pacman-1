import argparse

class GameSettings:
    def init(self):
        self.difficulty = 'medium'
        self.bg_color = 'black'
        self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Pac-Man Game Settings")
        parser.add_argument('--difficulty', type=str, choices=['easy', 'medium', 'hard'], default='hard', help="Set the game difficulty")
        parser.add_argument('--bg_color', type=str, choices=['black', 'pink', 'gray'], default='pink', help="Set the background color")
        args = parser.parse_args()
        self.difficulty = args.difficulty
        self.bg_color = args.bg_color

        # Set delays based on difficulty
        global pacman_move_delay, ghost_move_delay, mouth_anim_delay
        if self.difficulty == 'easy':
            pacman_move_delay = 200
            ghost_move_delay = 500
            mouth_anim_delay = 600
        elif self.difficulty == 'medium':
            pacman_move_delay = 150
            ghost_move_delay = 400
            mouth_anim_delay = 500
        else:  # 'hard' 
            pacman_move_delay = 100
            ghost_move_delay = 300
            mouth_anim_delay = 400

        # Set background color
        global BG_COLOR, PINK, GRAY, BLACK
        PINK = (255, 192, 203)
        GRAY = (80, 80, 80)
        BLACK = (0, 0, 0)

        if self.bg_color == 'pink':
            BG_COLOR = PINK
        elif self.bg_color == 'gray':
            BG_COLOR = GRAY
        else:
            BG_COLOR = BLACK

CELL_SIZE = 40
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Maze:
    def __init__(self):
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,1,1,1,0,1,0,1,0,1,0,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]

    def draw(self, screen):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE + 50, CELL_SIZE, CELL_SIZE))
                elif self.grid[y][x] == 0:
                    pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2 + 50), 3)


pygame.init()

class Game:
    def __init__(self):
        self.settings = GameSettings()
        self.pacman = PacMan()
        self.ghosts = [Ghost(1, 13, (255, 0, 0))]
        self.maze = Maze()
        self.score_manager = ScoreManager()
        self.game_state = GameState.PLAYING
