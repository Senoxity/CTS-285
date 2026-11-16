# PROMPTS.md
List of AI prompts used in this project, dated.

[11/13/26 11:28AM] I'm working on a text-only prototype recreation of the Dataman Calculator from 1977. I need help creating a pause-and-restore system for the program, so that if the user chooses to pause the program when a problem is given, the program stores the user's current state, and when they unpause, they return to the exact state that they paused at. Attached are the prototype files, a product backlog, and the requirements for the completed prototype.

* The pause feature must function as the Acceptance Criteria describes in the backlog (look for US-03)
* Only worry about the functional requirements in the image for now. the other parts (making new pytests, updating README files, etc.) will either be done by me, or we will do them together when the feature is finished.
* I would much prefer if you told me how to implement the feature on my own, rather than have you do all the work.
* The state must be stored in a .JSON file, similar to how the Memory Bank is stored.

[11/13/26 1:22PM] I'm trying to run the program to test it but entering practice at the menu just resets back to the menu instead of opening a problem

[11/16/26 12:19PM] Now we can move on to making the new pytest files. Create two pytest files that test the basic functionality of the answer checker and memory bank features respectively, and print their output/results into the Terminal. I'm choosing to keep try_pause.py from earlier, so for now you don't need to make that.