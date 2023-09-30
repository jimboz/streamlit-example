# from collections import namedtuple
# import altair as alt
# import math
# import pandas as pd
# import streamlit as st

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Maze Dimensions
ROWS, COLS = 10, 10

# Directions for movement
DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

# Initialize maze with all walls
maze = np.ones((ROWS, COLS), dtype=int)

# Start and End points
start, end = (1, 1), (ROWS - 2, COLS - 2)

# Create a path (For simplicity, we're creating a straight path)
for i in range(1, ROWS-1):
    maze[i][1:COLS-1] = 0

maze[end] = 2  # Mark the end point

player_position = list(start)


def draw_maze(maze, position):
    """Display the maze with the player's current position."""
    display = maze.copy()
    print(maze)
    # display[position[0], position[1]] = 3
    st.image(display, caption="Maze", width=300, channels="GRAY")


def move(direction, position):
    """Move the player in the given direction."""
    new_position = list(position)
    move = DIRECTIONS[direction]
    new_position[0] += move[0]
    new_position[1] += move[1]

    print(maze)

    # Check for walls
    if maze[new_position[0], new_position[1]] == 1:
        return position
    return tuple(new_position)


st.title("Maze Puzzle")

draw_maze(maze, player_position)

move_direction = st.selectbox("Choose a direction", list(DIRECTIONS.keys()))

player_position = move(move_direction, player_position)

if player_position == end:
    st.success("You've reached the end!")
else:
    st.write("Move to reach the end!")

# def draw_circle(radius):
#     fig, ax = plt.subplots(figsize=(6, 6))
#     circle = plt.Circle((0, 0), radius, color='m', fill=False)
#     ax.add_artist(circle)
#     ax.set_xlim(-radius-1, radius+1)
#     ax.set_ylim(-radius-1, radius+1)
#     ax.set_aspect('equal', 'box')
#     ax.grid(True, which='both', linestyle='--', linewidth=0.5)
#     ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
#     ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
#     st.pyplot(fig)

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# with st.echo(code_location='below'):
#     st.title("Draw a Circle")
#     radius = st.slider("Select a radius:", 1, 10, 5)
#     draw_circle(radius)
    
# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))
