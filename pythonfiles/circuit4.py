from qiskit import QuantumCircuit

#Make a custom gate
gatesource = QuantumCircuit(2)
gatesource.x(0)
gatesource.cx(0,1)
gatesource.x(0)
xcnotxgate = gatesource.to_gate()
gatesource.draw(output="mpl")

customgateqc = QuantumCircuit(2)
customgateqc.append(xcnotxgate,[0,1])
customgateqc.draw(output="mpl")
customgateqc.decompose().draw(output="mpl")