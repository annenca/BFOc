# BFO Rule Testing Program (Cellular Automata – Parity Problem)

This repository contains a program developed to test and analyze different variants of the **BFO rule** in the context of **cellular automata solving the parity problem**.

The implemented variants include:

* **BFOc** – the corrected version of the original BFO rule defined in [3].
* **BFOm** – the modified variant of the of the oryginal BFO rule defined in [2].

##  Purpose

The main goal of this project is to simulate and compare how different BFO rule variants behave when applied to the **parity problem** in cellular automata.

The parity problem consists in designing a cellular automaton that converges to:

* all **1s** if the initial configuration contains an **odd** number of 1s,
* all **0s** if the initial configuration contains an **even** number of 1s.

According to formulation of the problem, the length of the considered initial configuration has to be odd. 

##  Research Context

In 2013, the authors of [1] proposed the first candidate rule for solving the parity problem (the BFO rule). Unfortunately, it was later shown to be incorrect. The same authors then introduced a modified version (BFOm), which was successfully tested computationally; however, no formal mathematical proof was provided. In 2025, the authors of [3] proposed a corrected version of the BFO rule, called BFOc, for which a rigorous mathematical proof was established, confirming that it solves the parity problem.


##  Features

* Simulation of **cellular automata solving the parity problem**
* Implementation of **BFOc and BFOm**
* Detection of convergence to correct parity states
* Step-by-step temporal evolution tracking


##  Usage

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Run a simulation with a selected rule:


To run the script, use the following command:

```bash
python BFOc.py <size_of_initial_configuration> [all]
python BFOm.py <size_of_initial_configuration> [all]
```

where:
<size_of_initial_configuration> - odd integer ≤ 35 specifying the configuration size

all - (optional) runs the program for all odd sizes from 5 up to the given size



### Notes
* Requires an odd integer ≤ 35 as the main argument.
* An optional `all` argument enables processing for all odd sizes from 5 up to the given value.
* Invalid, missing, or out-of-range input may result in an error.

### References
[1] Betel, H., Oliveira, P.P.B., Flocchini, P. 
Solving the parity problem in one-dimensional cellular automata. 
Natural Computing 12(3), 323–337 (2013) 
https://doi.org/10.1007/s11047-013-9374-9

[2] Betel, H., Balbi, P.P., Flocchini, P., Meo Martins, C.L. 
Solving the Parity Problem in One-Dimensional Cellular Automata: Proposal of a fix to the BFO rule.
Unpublished manuscript (2016).

[3] Wolnik B., Nenca A., Balbi P.P., De Baets B.,
Cellular automata can really solve the parity problem,
arXiv:2501.08684, 2025.
https://arxiv.org/abs/2501.08684

