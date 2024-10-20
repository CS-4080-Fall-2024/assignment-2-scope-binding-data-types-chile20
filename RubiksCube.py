# This code generates a rubik's code in any size and color combo
# Rotating face function is used to demo the effectiveness of the structure
# But I don't have time to finish the full implementation to solve it for extra credit

import random

# Helper function to rotate a 2D list (face) clockwise or counterclockwise
def rotate_90_clockwise(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_90_counterclockwise(matrix):
    return rotate_90_clockwise(rotate_90_clockwise(rotate_90_clockwise(matrix)))

# Class to represent a single face of the cube
class Face:
    def __init__(self, color, size):
        self.grid = [[color] * size for _ in range(size)]

    def rotate(self, clockwise=True):
        if clockwise:
            self.grid = rotate_90_clockwise(self.grid)
        else:
            self.grid = rotate_90_counterclockwise(self.grid)

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.grid])

# Class to represent the Rubik's Cube
class RubikCube:
    def __init__(self, size=3, colors=None):
        # White, Red, Blue, Orange, Green, Yellow
        default_colors = ['W', 'R', 'B', 'O', 'G', 'Y']
        self.size = size
        colors = colors or default_colors

        if len(colors) != 6:
            raise ValueError("Exactly 6 colors must be provided.")

        # Initialize the cube faces: Top, Front, Right, Back, Left, Bottom
        self.faces = {
            "Top": Face(colors[0], size),
            "Front": Face(colors[1], size),
            "Right": Face(colors[2], size),
            "Back": Face(colors[3], size),
            "Left": Face(colors[4], size),
            "Bottom": Face(colors[5], size),
        }

    def rotate_face(self, face_name, clockwise=True):
        """Rotates a specific face and shifts adjacent face rows/columns."""
        self.faces[face_name].rotate(clockwise)

        # Rotating adjacent rows/columns based on the face rotated
        if face_name == "Top":
            self._rotate_row(["Front", "Right", "Back", "Left"], 0, clockwise)
        elif face_name == "Bottom":
            self._rotate_row(["Front", "Left", "Back", "Right"], -1, clockwise)
        elif face_name == "Front":
            self._rotate_column(["Top", "Right", "Bottom", "Left"], -1, clockwise)
        elif face_name == "Back":
            self._rotate_column(["Top", "Left", "Bottom", "Right"], 0, not clockwise)
        elif face_name == "Left":
            self._rotate_column(["Top", "Front", "Bottom", "Back"], 0, clockwise)
        elif face_name == "Right":
            self._rotate_column(["Top", "Back", "Bottom", "Front"], -1, not clockwise)

    def _rotate_row(self, faces, row, clockwise):
        """Shift a row across 4 adjacent faces."""
        if clockwise:
            temp = self.faces[faces[-1]].grid[row]
            for i in range(len(faces) - 1, 0, -1):
                self.faces[faces[i]].grid[row] = self.faces[faces[i - 1]].grid[row]
            self.faces[faces[0]].grid[row] = temp
        else:
            temp = self.faces[faces[0]].grid[row]
            for i in range(len(faces) - 1):
                self.faces[faces[i]].grid[row] = self.faces[faces[i + 1]].grid[row]
            self.faces[faces[-1]].grid[row] = temp

    def _rotate_column(self, faces, col, clockwise):
        """Shift a column across 4 adjacent faces."""
        temp = [self.faces[faces[-1]].grid[i][col] for i in range(self.size)]
        if clockwise:
            for i in range(len(faces) - 1, 0, -1):
                for j in range(self.size):
                    self.faces[faces[i]].grid[j][col] = self.faces[faces[i - 1]].grid[j][col]
            for j in range(self.size):
                self.faces[faces[0]].grid[j][col] = temp[j]
        else:
            for i in range(len(faces) - 1):
                for j in range(self.size):
                    self.faces[faces[i]].grid[j][col] = self.faces[faces[i + 1]].grid[j][col]
            for j in range(self.size):
                self.faces[faces[-1]].grid[j][col] = temp[j]

    def __str__(self):
        result = []
        for name, face in self.faces.items():
            result.append(f"{name}:\n{face}\n")
        return '\n'.join(result)

    def randomize(self, moves=20):
        """Randomize the cube by applying a series of random rotations."""
        faces = ["Top", "Bottom", "Front", "Back", "Left", "Right"]
        for _ in range(moves):
            face = random.choice(faces)
            clockwise = random.choice([True, False])
            self.rotate_face(face, clockwise)

# Initialize and print the cube
cube = RubikCube(size=3)

print("Initial Cube:")
print(cube)

# Try rotating left face clockwise
cube.rotate_face("Left", clockwise=True)

print("Rotated left face clockwise:")
print(cube)

# Randomize the cube with 30 moves
cube.randomize(30)

print("Randomized Cube:")
print(cube)