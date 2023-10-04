import os
import json
from matplotlib import pyplot

'''
code = 1: 4-qubit with 17 levels (Random Algorithm)
code = 2: 10-qubit with 12 levels (Random Algorithm)
code = 3: 7-qubit with 18 levels (Random Algorithm)
code = 4: 2-qubit with 2 levels (entanglement)
code = 5: 4-qubits with 5 levels (full adder with 4-qubits)
code = 6: 5-qubits with 6 levels (full adder with 5-qubits)
'''
circuit_code = 6

if circuit_code == 1:
    qubits = 4
    circuit_levels = 17
elif circuit_code == 2:
    qubits = 10
    circuit_levels = 12
elif circuit_code == 3:
    qubits = 7
    circuit_levels = 18
elif circuit_code == 4:
    qubits = 2
    circuit_levels = 2
elif circuit_code == 5:
    qubits = 4
    circuit_levels = 5
elif circuit_code == 6:
    qubits = 5
    circuit_levels = 6
else:
    raise Exception('Invalid circuit code!')

# ----------------------------------------------------------------------------------
circuit_algorithm = 'Random'
exp_number = 1
results_directory = 'circuit{}_qubits{}_levels{}_algo.{}_circuit_exp#{}'.format(
    circuit_code, qubits, circuit_levels, circuit_algorithm, exp_number)
log_filename = 'config.json'
log_path = os.path.join(results_directory, log_filename)
# -------------------------------------------------------------------------------------
with open(log_path, 'r') as jf:
    config = json.load(jf)
# --------------------------------------------------------------------------------------
history = config.get('history')

# plot loss information during training
pyplot.title('Loss / Mean Squared Error')
pyplot.plot(history['loss'], label='train')
pyplot.plot(history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

# ----------------------------------------------------------------------------------------

# plot accuracy information during training
pyplot.title('Accuracy / R2')
pyplot.plot(history['R2'], label='train')
pyplot.plot(history['val_R2'], label='test')
pyplot.legend()
pyplot.show()
