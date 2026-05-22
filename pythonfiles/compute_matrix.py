from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

simulator = Aer.get_backend("aer_simulator")

circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and acting on qubit 1
circuit.cx(0, 1)

# Save the matrix of the circuit until this point
circuit.save_unitary()

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit)

result = job.result()

# Print the unitary matrix representation of circuit
print(result.get_unitary(circuit,3)) # 3 is the number of digits of precision

# Draw the circuit. Will open a separate window if Spyder was set up correctly.
circuit.draw(output = "mpl")

