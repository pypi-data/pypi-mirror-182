QuantGates
QuantGates is a simple desktop application that allows users to visualize the effect of single qubit quantum gates on the Bloch sphere. It is implemented in Python using the tkinter library for the UI and the qiskit library for quantum computing simulations.

Features
Input and apply single qubit quantum gates to the quantum circuit
Visualize the effect of the applied gates on the Bloch sphere in a separate window
Track the applied gates in the display
Clear the display and reset the circuit to the initial state
Requirements
Python 3
qiskit
tkinter
Usage
Clone the repository or download the zip file
Install the required libraries: pip install qiskit and pip install tkinter (Note: you may need to create a new virtual environment for the installation)
Navigate to the project directory and run python main.py to start the application
Input and apply the desired quantum gates using the buttons in the UI
Click on the "Visualize Circuit" button to visualize the effect of the applied gates on the Bloch sphere in a separate window
Click on the "Clear" button to clear the display and reset the circuit to the initial state
Quantum Gates
The following quantum gates are available in the application:

X-gate (Pauli-X gate)
Y-gate (Pauli-Y gate)
Z-gate (Pauli-Z gate)
Rx-gate (Rotation about x-axis)
Ry-gate (Rotation about y-axis)
Rz-gate (Rotation about z-axis)
S-gate (Phase shift gate)
Sd-gate (Conjugate of phase shift gate)
T-gate (T gate)
Td-gate (Conjugate of T gate)
Hadamard gate (Hadamard gate)

Limitations
The application can only visualize single qubit quantum gates
The application does not support measurements, as the state vector collapses into one of the basis vectors upon measurement
The maximum number of gates that can be applied is 10

Future Work
Support for multi-qubit gates
Support for measurements
Option to input custom gates
Improved UI design

Credits
Qiskit for providing the quantum computing simulation library
tkinter for providing the UI library