from qiskit import QuantumCircuit

all_ = range(4)

def oracle(qc, all_=all_):
    qc.x([0, 1, 3])
    CZ_(qc)
    qc.x([0, 1, 3])



def CZ_(qc, all_=all_):
    qc.barrier()
    qc.h(3)
    
    qc.mcx(list(range(3)), 3)
    
    qc.h(3)
    qc.barrier()


def grover_dfsr(qc, all_=all_):
    qc.h(all_)
    qc.x(all_)
    CZ_(qc)
    qc.x(all_)
    qc.h(all_)


grover_circ = QuantumCircuit(4)
n = 3


grover_circ.h(all_)
for _ in range(n):
    oracle(grover_circ)
    grover_dfsr(grover_circ)

grover_circ.measure_all()


# shots = 100

# result = StatevectorSampler().run([grover_circ], shots=shots).result()

# counts = result[0].data.meas.get_counts()

# plot_histogram({p: c / shots for p, c in counts.items()})