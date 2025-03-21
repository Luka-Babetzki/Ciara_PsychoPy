### displaychecker – Begin Experiment ###
from psychopy import parallel
from random import randint, choice

# Set up parallel port (make sure the port address is correct)
parallel.setPortAddress(0x0378)
parallel.setData(0)

# Count how many checkers have appeared
checker_count = 0

# Define the 8 possible positions (in cm)
# Four positions for perifoveal (closer to the video’s corners) 
# and four for peripheral (more offset outside the video frame)
checkerPositions = [
    (-10, 6),   # top-left perifoveal
    (10, 6),    # top-right perifoveal
    (-10, -6),  # bottom-left perifoveal
    (10, -6),   # bottom-right perifoveal
    (-12, 8),   # top-left peripheral
    (12, 8),    # top-right peripheral
    (-12, -8),  # bottom-left peripheral
    (12, -8)    # bottom-right peripheral
]
