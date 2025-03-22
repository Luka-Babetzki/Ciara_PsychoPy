# Get current time
t = trialClock.getTime()

# Check for exit key
if 't' in event.getKeys() or 'escape' in event.getKeys():
    core.quit()

# Check if time to show checker
if not checker.drawing and checker.waiting and t >= checkerOnset:
    # Show checker at random position
    checker.pos = random.choice(checker_positions)
    checker.setAutoDraw(True)
    
    # Record data
    checkerOnsets.append(t)
    checker_count += 1
    
    # Update status
    checker.drawing = True
    checker.waiting = False

# Check if time to hide checker (after 100ms display)
elif checker.drawing and t >= checkerOnset + 0.1:
    # Hide checker
    checker.setAutoDraw(False)
    checker.drawing = False
    
    # Prepare for next checker
    isi = random.randint(2, 4)
    checkerISIs.append(isi)
    checkerOnset = t + isi
    checker.waiting = True
    
# Update screen
win.flip()