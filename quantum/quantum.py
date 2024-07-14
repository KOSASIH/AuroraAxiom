from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

class AuroraAxiomQuantum:
    def __init__(self):
        self.qc = QuantumCircuit(2, 2)

    def add_gate(self, gate_type, qubits):
        if gate_type == 'h':
            self.qc.h(qubits)
        elif gate_type == 'cx':
            self.qc.cx(qubits[0], qubits[1])

    def run_circuit(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.qc, backend, shots=1000)
        result = job.result()
        counts = result.get_counts(self.qc)
        return counts

quantum = AuroraAxiomQuantum()
