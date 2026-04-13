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
* Support for arbitrary initial configurations
* Detection of convergence to correct parity states
* Step-by-step temporal evolution tracking
* Easy comparison between rule behaviors


##  Usage

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Run a simulation with a selected rule:


To run the script, use the following command:

```bash
python BFOc.py <d>
python BFOm.py <d> 
```

where:

* `d` is a **positive odd integer** (e.g., 1, 3, 5, 7, ...)

### Example

```bash
python.exe BFOc 5  --rule BFOc with configurations of size 5
```

### Notes

* The program expects exactly one argument.
* The value of `d` must be **odd**.
* If an even number or no argument is provided, the program may return an error.




