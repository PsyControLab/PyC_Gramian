# Controllability Gramian Calculator for Discrete Systems

## Description

PyC_gram is a Python module designed for computing the Controllability Gramian of discrete linear dynamical systems. This tool extends the functionality of the `python-control` library, specifically tailored to handle discrete systems with stability checks. It provides an efficient and user-friendly way to analyze control energy in linear dynamical systems, leveraging the Slycot library's `sb03md` function for robust computations.

## Features

- Calculation of the Controllability Gramian for discrete linear systems.
- Stability check for the system before computing the Gramian.
- Integration with pandas DataFrames for batch processing of systems.
- Additional functions for analyzing eigenvalues of the Gramian.

## Installation

To use PyC_gram, you need to have Python installed along with the `numpy`, `control`, and `slycot` packages. You can install these dependencies using pip:

```bash
git clone https://github.com/PsyControl/PyC_Gramian.git
cd PyC_Gramian
pip install numpy control slycot
```

## Usage
Here's a basic example of how to use PyC_gram:

```python
import pandas as pd
import numpy as np
import control as ct
from PyC_Gramian import  PyC_compute_gramians

# Example DataFrame with 'A_Norm' and 'B_matrice' columns
# df = ...

df_with_grams = PyC_compute_gramians(df)
df_with_grams.head(2)
```

## Credits

This project is built upon the python-control library and uses the Slycot library's sb03md function for computations.

```vbent

This README.md file can be rendered as a GitHub document, which is suitable for viewing on GitHub repositories. You can modify it as needed to better fit your project's details.
```
