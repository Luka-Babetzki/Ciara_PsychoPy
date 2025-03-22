# Setup trial clock
trialClock = core.Clock()

# Create checker stimulus
checker = visual.ImageStim(
    win=win,
    name='checker', 
    image='checker.jpg',
    pos=(0, 0),
    size=(5, 5),
    units='cm'
)

# If image fails, use pattern instead
if not os.path.exists('checker.jpg'):
    checker = visual.RadialStim(
        win=win, 
        radialCycles=4, 
        angularCycles=8,
        size=(5, 5),
        units='cm'
    )

# Hide checker initially
checker.setAutoDraw(False)

# Variables for timing
t = 0
checker.waiting = True
checker.drawing = False
checkerOnset = random.randint(2, 4)  # First appearance time

# Data storage
checkerOnsets = []
checkerISIs = []