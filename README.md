**Quantum-Circuit-NN**

*This repository is organized as follows:*

    1- codes directory:
        There are 3 files in this directory.
            - Quantum-Circuit-Dataset-Generator.ipynb
                It is a jupyter notebook file that use qiskit library to generate dataset needed for training MLP network
                and test the trained results.

            - colab_notebook_link.txt
                It contains a link to google colab notebook:
                    [colab notebook link!](https://colab.research.google.com/drive/1Up1LgiYH_ZEUb4XJEpqJjcF3vQop3aZG?usp=sharing)

            - visualize_history.py
                It contains some simple code to visualize loss and accuracy of training process.
    
    2- data_and_results directory
        It contains 4 other directory. each of them contains data and results for one of circuits that we tested.
            - Circuit#1: 4-qubits, 17 levels, Random
            - Circuit#4: 2-qubits, 2 levels, Entanglement
            - Circuit#5: 4-qubits, 5 levels, Full Adder
            - Circuit#6: 5-qubits, 6 levels, Full Adder