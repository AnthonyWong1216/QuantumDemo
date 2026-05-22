from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor


qinstance = QuantumInstance(Aer.get_backend('qasm_simulator'))
shor = Shor(quantum_instance=qinstance)

result = shor.factor(N=15, a=7)
print('Factors:', result.factors)