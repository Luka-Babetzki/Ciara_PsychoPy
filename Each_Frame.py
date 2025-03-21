### displaychecker – Each Frame ###
# Check for termination key during the trial
if trial_key.keys == 't':
    trialselectloop.finished = True
    continueRoutine = False

# Update the current time from the trial clock
t = trialClock.getTime()

# If the checker is not currently visible and not already waiting, set a new ISI
if not checker.drawing and not checker.waiting:
    # Choose a random interval between 2 and 4 seconds
    checkerISI = randint(2, 4)
    print('checkerISI', checkerISI)
    checkerISIs.append(checkerISI)
    # Set the time when the checker should appear
    checkerOnset = t + checkerISI
    checker.waiting = True

# When waiting and the time has come to display the checker
elif not checker.drawing and checker.waiting:
    if t >= checkerOnset:
        # Randomly choose a new position from the list and update the checker's position
        currentCheckerPos = choice(checkerPositions)
        checker.pos = currentCheckerPos
        print('Checker position:', currentCheckerPos)
        
        print('playing')
        checker.setAutoDraw(True)
        checkerOnsets.append(t)
        checker.drawing = True
        checker.waiting = False
        
        # Increment the checker count and send a trigger via parallel port
        checker_count += 1
        parallel.setPin(4, 1)

# When the checker is currently displayed, remove it after 0.1 seconds (minus a frame tolerance)
elif checker.drawing:
    # frameTolerance should be defined elsewhere (or set it as a small number, e.g., 0.005)
    if t >= checkerOnset + 0.1 - frameTolerance:
         checker.tStop = t  # record when it stopped
         checker.frameNStop = frameN  # record the frame index
         checker.setAutoDraw(False)
         checker.drawing = False
         parallel.setPin(4, 0)
