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
[11/11/26 12:44PM] M4 Bonus template imported. Old pytests removed. Tasks checked off in TO-DO.md.

