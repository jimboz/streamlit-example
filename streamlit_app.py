# from collections import namedtuple
# import altair as alt
# import math
# import pandas as pd
# import streamlit as st

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_circle(radius):
    fig, ax = plt.subplots(figsize=(6, 6))
    circle = plt.Circle((0, 0), radius, color='g', fill=False)
    ax.add_artist(circle)
    ax.set_xlim(-radius-1, radius+1)
    ax.set_ylim(-radius-1, radius+1)
    ax.set_aspect('equal', 'box')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    st.pyplot(fig)

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

with st.echo(code_location='below'):
    st.title("Draw a Circle")
    radius = st.slider("Select a radius:", 1, 10, 5)
    draw_circle(radius)
    
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
