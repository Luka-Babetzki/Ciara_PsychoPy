### displaychecker – Begin Routine ###
from psychopy import core, visual, event

# Initialize the trial clock
trialClock = core.Clock()

# Check for termination key
if trial_key.keys == 't':
    trialselectloop.finished = True
    continueRoutine = False

# (Optional) Movie stimulus – uncomment and adjust if needed:
# movie = visual.MovieStim3(
#     win=win, name='movie', units='cm',
#     noAudio=False,
#     filename='C:\\Infant Fantasia TEST\\Fantasia1min30.mp4',
#     ori=0, pos=(0, 0), opacity=1,
#     loop=True,
#     size=[22.5,12.5],
#     depth=-1.0,
# )
# movie.setAutoDraw(True)

# Initialize the checker stimulus.
# Note: The size is reduced from (30,30) to (15,15) so it fits better around the video.
checker = visual.ImageStim(
    win=win,
    name='checker', units='cm',
    image='checker.jpg', mask=None,
    ori=0, pos=(0, 0), size=(15, 15),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0
)
checker.drawing = False
checker.setAutoDraw(False)
checker.waiting = False

# Duration of the trial (in seconds)
trialduration = 90

# Lists to record onsets and inter-stimulus intervals (ISIs)
checkerOnsets = []
checkerISIs = []

# Variable to hold the next onset time for the checker
checkerOnset = None
