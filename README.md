# BFO Rule Testing Program (Cellular Automata – Parity Problem)

This repository contains a program developed to test and analyze different variants of the **BFO rule** in the context of **cellular automata solving the parity problem**.

The implemented variants include:

* **BFOc** – the corrected version
* **BFOm** – a modified variant

##  Purpose

The main goal of this project is to simulate and compare how different BFO rule variants behave when applied to the **parity problem** in cellular automata.

The parity problem consists in designing a cellular automaton that converges to:

* all **1s** if the initial configuration contains an **odd** number of 1s,
* all **0s** if the number of 1s is **even**.

This program was used to investigate and validate corrections to the original **BFOo** rule.

##  Research Context

In our work, we provide a fix to the **BFOo** rule along with a full formal proof of correctness. The corrected version, called **BFOc** (*c* for *corrected*), eliminates issues observed in specific faulty initial configurations.

This result is important because it demonstrates that:

> A single-rule solution to the parity problem does exist,


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
<size_of_initial_configuration> — odd integer ≤ 35 specifying the configuration size
all — (optional) runs the program for all odd sizes from 5 up to the given size



### Notes
* Requires an odd integer ≤ 35 as the main argument.
* An optional `all` argument enables processing for all odd sizes from 5 up to the given value.
* Invalid, missing, or out-of-range input may result in an error.




