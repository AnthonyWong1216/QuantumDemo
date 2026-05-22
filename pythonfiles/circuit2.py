#Construct dynamically
from qiskit import QuantumCircuit
from qiskit.circuit.library import CXGate
qc = QuantumCircuit(3)
cxg = CXGate()
qc.append(cxg,[0,1])
qc.append(cxg,[0,1])
qc.draw(output="mpl")