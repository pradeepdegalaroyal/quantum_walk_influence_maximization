import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Operator
import networkx as nx
import matplotlib.pyplot as plt
from scipy.linalg import expm

def create_social_network(n_nodes=10):
    """Creates a sample social network with a scale-free structure."""
    G = nx.barabasi_albert_graph(n_nodes, 2, seed=42)
    return G

def adjacency_matrix(G, n):
    """Returns the adjacency matrix of the network."""
    return np.array(nx.adjacency_matrix(G).todense())

def quantum_walk_operator(A, t):
    """Defines the quantum walk evolution operator U(t) = exp(-iAt)."""
    return expm(-1j * A * t)

def quantum_walk_circuit(n, A, t):
    """Constructs a quantum circuit for a quantum walk on the network."""
    qc = QuantumCircuit(n)
    # Initial superposition over all nodes
    qc.h(range(n))
    # Apply quantum walk operator
    walk_op = Operator(quantum_walk_operator(A, t))
    qc.unitary(walk_op, range(n), label='Quantum Walk')
    # Measure all qubits
    qc.measure_all()
    return qc

def identify_influential_nodes(G, counts, n, top_k=3):
    """Identifies the top-k most influential nodes based on quantum walk probabilities."""
    probabilities = np.zeros(n)
    for state, count in counts.items():
        for i in range(min(len(state), n)):
            if state[i] == '1':
                probabilities[i] += count
    probabilities /= sum(counts.values())
    
    # Select top-k nodes with highest probabilities
    influential_nodes = np.argsort(probabilities)[-top_k:]
    influence_scores = probabilities[influential_nodes]
    
    return influential_nodes, probabilities, influence_scores

def simulate_influence(G, seed_nodes, steps=3):
    """Simulates influence spread using a simple linear threshold model."""
    n = len(G.nodes)
    active = set(seed_nodes)
    threshold = 0.3  # Activation threshold
    for _ in range(steps):
        new_active = set()
        for node in G.nodes:
            if node not in active:
                neighbors = list(G.neighbors(node))
                active_neighbors = sum(1 for neighbor in neighbors if neighbor in active)
                if active_neighbors / max(len(neighbors), 1) >= threshold:
                    new_active.add(node)
        active.update(new_active)
    return len(active)

def visualize_results(G, influential_nodes, probabilities, influence_scores):
    """Visualizes the network, influential nodes, and probabilities."""
    plt.figure(figsize=(12, 8))
    
    # Network visualization
    pos = nx.spring_layout(G, seed=42)
    plt.subplot(2, 1, 1)
    node_colors = ['red' if i in influential_nodes else 'lightblue' for i in G.nodes]
    nx.draw(G, pos, node_color=node_colors, with_labels=True, node_size=500, font_size=10)
    plt.title(f"Influence Maximization: Top {len(influential_nodes)} Influential Nodes")
    
    # Probability distribution
    plt.subplot(2, 1, 2)
    plt.bar(range(len(probabilities)), probabilities, color='lightblue')
    plt.bar(influential_nodes, influence_scores, color='red')
    plt.xlabel("Node")
    plt.ylabel("Quantum Walk Probability")
    plt.title("Quantum Walk Probabilities (Influential Nodes in Red)")
    plt.tight_layout()
    plt.show()

def run_quantum_walk_influence_maximization(n_nodes=10, t=1.0, shots=1024, top_k=3):
    """Runs the quantum walk-based influence maximization algorithm."""
    # Create social network
    G = create_social_network(n_nodes)
    n = n_nodes
    
    # Run quantum walk
    A = adjacency_matrix(G, n)
    circuit = quantum_walk_circuit(n, A, t)
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=shots)
    counts = job.result().get_counts()
    
    # Identify influential nodes
    influential_nodes, probabilities, influence_scores = identify_influential_nodes(G, counts, n, top_k)
    
    # Simulate influence spread
    influence_spread = simulate_influence(G, influential_nodes)
    
    return G, influential_nodes, probabilities, influence_scores, influence_spread

if __name__ == "__main__":
    # Parameters
    n_nodes = 10
    t = 1.0  # Evolution time
    shots = 1024
    top_k = 3
    
    # Run algorithm
    G, influential_nodes, probabilities, influence_scores, influence_spread = run_quantum_walk_influence_maximization(n_nodes, t, shots, top_k)
    
    # Output results
    print(f"Influential nodes: {list(influential_nodes)}")
    print(f"Influence scores: {influence_scores}")
    print(f"Influence spread: {influence_spread} nodes activated")
    
    # Visualize
    visualize_results(G, influential_nodes, probabilities, influence_scores)
