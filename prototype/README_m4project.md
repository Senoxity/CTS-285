This project was created as the Module 4 Project for CTS-285, Systems Analysis and Design.

Created November 10, 2026

The project was created to identify and revise the basic functionality of the DataMan calculator, in order to create a basis for a modern rendition of the program. The project was intended to be a text-only prototype that the next module would build off of using Flask, which is why the prototype does everything in a terminal window.

While revisions of the base program were kept to a minimum, the flow of the answer checker fuctionality was modified to better allow the pause feature to be added, and for the program state to be properly stored. Now, the program can pause and unpause mid-session, and can restore the user's progress if the program is terminated due to real-time modification of the .json file where the data is stored.

As the program stands currently, it accurately tests and runs the basic core functionality of the original DataMan calculator, while also adding a new feature that can be carried over to the next phase of the project. Pytest files included with the program can help if any bugs or other business logic issues are to arise later.

The intention of the program and how the project will be used as the Dataman Project shifts to front-end development is still unclear, as stakeholders have yet to determine a visual style, and insight about UI design using flask is limited.