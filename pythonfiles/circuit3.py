from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

#Bind parameters

#make a template circuit
qc = QuantumCircuit(3)
qc.initialize([0,0,0,0,0,0,0,1])#initial state vector
param0 = Parameter("angle0")
param1 = Parameter("angle1")
param2 = Parameter("angle2")
qc.h(0)
qc.h(1)
qc.h(2)
qc.p(param0,0)
qc.p(param1,1)
qc.p(param2,2)
qc.draw(output="mpl")

#make a circuit from the template
#NOTE bind_parameters has become assign_parameters in the latest version of qiskit
qcinstance = qc.assign_parameters({param0:0.0  , param1:0.1 , param2:0.2 })
qcinstance.draw(output="mpl")