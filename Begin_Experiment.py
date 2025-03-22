from psychopy import core, visual, event, data
import random
import os

# Setup window
win = visual.Window(size=(1024, 768), fullscr=True, color=[-1,-1,-1], units='cm')

# Create data file
thisExp = data.ExperimentHandler(name='CheckerExperiment', 
                               dataFileName='checker_data')

# Define checker positions
checker_positions = [
    (-10, 10), (10, 10), (-10, -10), (10, -10),  # Perifoveal
    (-15, 15), (15, 15), (-15, -15), (15, -15)   # Peripheral
]

# Counter for checkers shown
checker_count = 0