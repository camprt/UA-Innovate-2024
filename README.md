# UA-Innovate-2024
Materials used for our 1st place submission to the UA Innovate Annual Hackathon Social Innovation Category.

Created to solve the problem presented by International Paper: design a system that can help the company reach 0 employee injuries surrounding heavy machinery such as Paper machines and corrugators.

Our solution implements computer vision and simple state machines to detect possibly dangeorus situations before they occur and take action accordingly.

"Activity_Diagram.png" - shows a UML-style activity diagram demonstrating how our system moves between different states to either issue warnings to employees or stop that machine part entirely. Our system ensures that the entire machine will not need to be shut down unless in the most dire of circumstances, but can still pre-emptively determine when a nearby person might be in danger, and stop the machine if necessary.

"CV_demo.py" - a python program that uses the open-source computer visiion library OpenCV to detect movement and position. Exits/shuts down when certain borders are crossed, similar to how our system might theoretically respond to real-life movement around machines.

"FSM_diagram.png" - diagram corresponding to the finite state machine for the system.

"FSM_pseudocode.txt" - psuedocode version of the finite state machine,

"Final_Presentation.pdf" - presentation file that we used to present our final product.
