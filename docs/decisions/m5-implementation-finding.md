# M5 Implementation Finding
While there were many finding that resulted after fully building the Minimal Prototype, there were a few discoveries and revisions that stood out to me when I was building the program. They are listed below.

- The main facet of the implementation process and how it relates to the text prototype is that it proves that the text menu structure was sound enough on it's own to be run in Flask without any overarching changes beyond just the flask additions. All of the basic features of the program work as they did in the text prototype.

- The setup of the pause feature in the flask implementation works as intended with just one problem as it stands currently, but if the program were to introduce more problems in the future, then the server would have to individually store the current problem in order for the session to be reinstated.

- The hard-coded session id of ```maya-1``` leaves the identity-session approach question from Module 3 unresolved, since this session ID always assumes the same learner, instead of assigning a unique ID when a session begins. This may be adressed in the future.