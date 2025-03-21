# Ciara PsychoPy

## Overview
This PsychoPy experiment is designed to display a video of Disney's *Fantasia* while periodically flashing a checkerboard stimulus at one of eight possible locations. The checkers appear randomly every 2-4 seconds and alternate between four perifoveal positions (near the corners of the video) and four peripheral positions (around the video border). The experiment also integrates parallel port triggers for external synchronization.

## Features
- Displays *Fantasia* video as the main stimulus
- Flashes a checkerboard stimulus at random intervals (2-4 seconds)
- Checker positions are randomized across eight predefined locations
- Uses a parallel port trigger for external synchronization
- Allows early termination using a designated key

## Folder Structure
```
/Project_Folder
│── FantasiaExperiment.psyexp  # PsychoPy experiment file
│── checker.jpg                # Checkerboard image
│── Fantasia1min30.mp4         # Movie file used in the experiment
│── README.md                  # Documentation file
│── /data                      # Folder for storing output data
```

## Code Structure
The experiment consists of three key sections in PsychoPy’s *Code Component*:

### Begin Experiment
- Initializes parallel port communication
- Defines checker positions (perifoveal and peripheral)
- Sets up a counter for the number of checker displays

### Begin Routine
- Initializes the checker stimulus
- Optionally loads and auto-plays the video
- Prepares lists to log onset times and inter-stimulus intervals (ISIs)

### Each Frame
- Checks for an experiment termination key
- Randomly selects a time delay (2-4s) before displaying the checker
- Randomly selects one of eight positions for the checker
- Displays the checker for 0.1 seconds, then removes it
- Sends a parallel port trigger when the checker appears

## Requirements
### Software
- PsychoPy 2023.1+ (Standalone or Coder Mode)
- Windows (recommended for parallel port functionality)

### Hardware
- A display monitor compatible with PsychoPy
- Parallel port (for synchronization, if needed)

## Installation and Setup
1. **Download and install PsychoPy**: [https://www.psychopy.org/download.html](https://www.psychopy.org/download.html)
2. **Extract the project files** into a working directory
3. **Ensure dependencies are installed** (if running in Coder mode):
   ```sh
   pip install psychopy
   ```
4. **Run the experiment**:
   - Open `FantasiaExperiment.psyexp` in PsychoPy
   - Click **Run** to start the experiment

## Troubleshooting
### Checkers Not Displaying?
- Ensure `checker.jpg` is in the same directory as the experiment file
- Verify that the checker positions match the screen resolution

### Parallel Port Not Working?
- Confirm that the port address (`0x0378`) is correct for your machine
- Run PsychoPy in administrator mode

### Video Not Playing?
- Ensure the correct file path is set in the video component
- Try converting the video to a different format (e.g., `.mp4` with lower resolution)

## Acknowledgments
This experiment was designed for psychological research and visual perception studies using PsychoPy.

For further modifications or questions, please contact the experiment creator.

---
*Last Updated: March 2025*

