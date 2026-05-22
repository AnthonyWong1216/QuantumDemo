from qiskit import QuantumCircuit

#Make a qubit setter
instrsource = QuantumCircuit(1)
instrsource.reset(0)
instrsource.x(0)
setqubit = instrsource.to_instruction()

custominstrqc = QuantumCircuit(2)
custominstrqc.append(setqubit,[0])
custominstrqc.append(setqubit,[1])
custominstrqc.decompose().draw(output="mpl")