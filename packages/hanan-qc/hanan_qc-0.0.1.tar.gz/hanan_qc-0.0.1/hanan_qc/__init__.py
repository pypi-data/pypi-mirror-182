import qiskit

# Define a function to parse the user input
def parse_input(input_string):
    # Split the input string into a list of tokens
    tokens = input_string.split()

    # Extract the number of qubits and classical bits from the first two tokens
    num_qubits = int(tokens[0])
    num_classical_bits = int(tokens[1])

    # Initialize an empty list of gates
    gates = []

    # Iterate through the remaining tokens and extract the gate information
    for i in range(2, len(tokens), 3):
        # Extract the gate type, qubit index, and optional angle parameter
        gate_type = tokens[i]
        qubit_index = int(tokens[i+1])
        if tokens[i+2].isnumeric():
            angle = float(tokens[i+2])
        else:
            angle = None

        # Add the gate information to the gates list
        gates.append((gate_type, qubit_index, angle))

    return num_qubits, num_classical_bits, gates

# Define a function to create a quantum circuit
def create_quantum_circuit(num_qubits, num_classical_bits, gates):
    # Create a quantum circuit with the specified number of qubits and classical bits
    circuit = qiskit.QuantumCircuit(num_qubits, num_classical_bits)

    # Iterate through the gates and apply them to the quantum circuit
    for gate_type, qubit_index, angle in gates:
        if gate_type == 'X':
            circuit.x(qubit_index)
        elif gate_type == 'Y':
            circuit.y(qubit_index)
        elif gate_type == 'Z':
            circuit.z(qubit_index)
        elif gate_type == 'H':
            circuit.h(qubit_index)
        elif gate_type == 'S':
            circuit.s(qubit_index)
        elif gate_type == 'T':
            circuit.t(qubit_index)
        elif gate_type == 'RX':
            circuit.rx(angle, qubit_index)
        elif gate_type == 'RY':
            circuit.ry(angle, qubit_index)
        elif gate_type == 'RZ':
            circuit.rz(angle, qubit_index)
        elif gate_type == 'U1':
            circuit.u1(angle, qubit_index)
        elif gate_type == 'U2':
            circuit.u2(angle[0], angle[1], qubit_index)
        elif gate_type == 'U3':
            circuit.u3(angle[0], angle[1], angle[2], qubit_index)

    return circuit