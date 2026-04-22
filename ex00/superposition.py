from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram


qc = QuantumCircuit(2, 2, name='Bell State')


qc.h(0)  

qc.measure(0)

# Symuluj
simulator = AerSimulator()
job = simulator.run(qc, shots=500)
result = job.result()
counts = result.get_counts()

print("Wyniki pomiar  w:")
print(counts)

# Wizualizacja
plot_histogram(counts)
plt.savefig('/app/results.png')
print("Histogram zapisany do results.png")