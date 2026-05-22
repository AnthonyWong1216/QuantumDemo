from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  # The modern way to use Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Create the Circuit (3 bits)
qc = QuantumCircuit(3)
qc.h(0)          # Put qubit 0 in superposition
qc.cx(0, 1)      # Entangle qubit 0 and 1
qc.cx(1, 2)      # Entangle qubit 1 and 2

# Add measurements so we can see results
qc.measure_all()

# --- PART A: THE CIRCUIT DIAGRAM ---
print("Generating Circuit Diagram...")
try:
    # We use 'mpl' for a nice looking diagram
    circuit_draw = qc.draw('mpl')
    circuit_draw.savefig("circuit1_diagram.png")
    print("Saved circuit1_diagram.png")
except Exception as e:
    print(f"Could not save diagram with 'mpl': {e}")
    circuit_draw = qc.draw() # Fallback to text

# --- PART B: THE PROBABILITY GRAPH (THE MODERN WAY) ---
print("Running simulation using AerSimulator...")

# In Qiskit 1.0+, we create a simulator object and 'run' the circuit through it
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()

# Get the counts (e.g., {'000': 512, '111': 512})
counts = result.get_counts()
print(f"Simulation results: {counts}")

# Create the Histogram graph
table_graph = plot_histogram(counts)
table_graph.savefig("circuit1_table.png")
print("Saved circuit1_table.png")

# --- PART C: POP UP EVERYTHING ---
print("Done! Popping up windows...")

# 1. Show the Circuit Diagram
plt.figure()
if hasattr(circuit_draw, 'show'):
    circuit_draw.show()
else:
    print(circuit_draw)

# 2. Show the Probability Histogram (The "Table" of results)
plt.figure()
plt.show()