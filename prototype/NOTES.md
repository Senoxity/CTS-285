# NOTES.md
Working notes file for Dataman Prototype. Entries will be dated with date/time. Comments will be included in the code for smaller notes/warnings.

### Date Format
Dates will be added before entries in [brackets], using MM/DD/YY formatting. Time will be included in the same grouping, using 12-hour time.
### Sample Entry
[1/23/26 11:30AM] Basic structure implemented.

## Decision Card
This isn't necessarily required but I wanted to make one anyway for the sake of clarity.

Slice: <US-03: Mid-Practice Pause Functionality>  
Acceptance criterion: The program enters a paused state when a pause command is entered. The progress is saved, and restored when the user enters "unpause". Same effect for if the program is interrupted.  
Rule: Pause command functionality  
Data: Current user progress at the moment of pause  
Design decision: Rule lives in the logic layer, and the saved state lives in the data layer in the form of a .json file.  

## Notes Begin Here
[11/10/26 3:37PM] Document created.
[11/11/26 12:25PM] TO-DO.md created.
[11/11/26 12:44PM] M4 Bonus template imported. Old pytests removed. Tasks checked off in TO-DO.md (TO-DO updates won't be recorded from here forward).
[11/13/26 11:28AM] Claude prompted with instructions on how to add pause functionality.
[11/13/26 11:45AM] Added new methods save_pause, load_pause, and clear_pause.
[11/13/26 11:47AM] Edited JsonFileStore method to write pause states to .json files
[11/13/26 12:32PM] Finished work on store.py and logic.py with new methods. Working to add functionality in app.py now.
[11/13/26 12:35PM] Added try_pause.py for testing the new pause methods, courtesy of Claude (included in initial prompt).
[11/13/26 12:51PM] New functions added to app.py to allow the user to enter "pause" to invoke paused state, and "unpause' to restore.
[11/13/26 12:54PM] Safeguard added so that ending the input counts as a pause.


