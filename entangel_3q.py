from qiskit import QuantumCircuit

ent_circ = QuantumCircuit(3)

ent_circ.h(0)
ent_circ.cx(0, 1)
ent_circ.cx(1, 2)