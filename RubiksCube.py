# Function to randomize the cube with a given number of moves
def randomize_cube(cube, moves=20):
    return False


# Create a custom rubik's cube with specified size and colors
def create_custom_cube(size, colors=None):
    # Default colors if none provided (White, Red, Blue, Orange, Green, Yellow)
    default_colors = ['W', 'R', 'B', 'O', 'G', 'Y']

    # Use provided colors or fallback to defaults
    if colors is None:
        colors = default_colors

    if len(colors) != 6:
        raise ValueError("Exactly 6 colors must be provided.")

    # Initialize cube with the given size and colors
    cube = [
        [[colors[0]] * size for _ in range(size)],  # Top
        [[colors[1]] * size for _ in range(size)],  # Front
        [[colors[2]] * size for _ in range(size)],  # Right
        [[colors[3]] * size for _ in range(size)],  # Back
        [[colors[4]] * size for _ in range(size)],  # Left
        [[colors[5]] * size for _ in range(size)],  # Bottom
    ]

    # Randomize the cube by applying random moves
    randomize_cube(cube, 30)

    return cube


# Function to print the cube layout
def print_cube(cube):
    face_names = ["Top", "Front", "Right", "Back", "Left", "Bottom"]

    for face_index, face in enumerate(cube):
        print(f"{face_names[face_index]}:")
        for row in face:
            print(' '.join(row))
        print()


cube_size = 3
cube = create_custom_cube(cube_size)

print("Initial Cube:")
print_cube(cube)