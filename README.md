# Time_interleaved_Sampling
Simulation of a time-interleaved sampling system demonstrating improved impulse detection compared to standard low-rate sampling using parallel interleaved branches.
# Time-Interleaved Sampling System Simulation

This project simulates a **time-interleaved sampling system** and compares it with a standard 10 Hz sampler for detecting a short impulse signal.

The simulation demonstrates how parallel sampling branches can improve temporal resolution and prevent missed events that may occur with low-rate sampling.

---

## Overview

- A continuous-time impulse is placed at a specific time instant.
- A **standard 10 Hz sampler** attempts to detect the impulse.
- A **designed system with 10 parallel sampling branches** is used to achieve an effective 100 Hz sampling rate through interleaving.
- Results are visualized using Matplotlib.

---

## Features

- Continuous-time signal simulation (1000 Hz resolution)
- Standard 10 Hz sampling
- Time-interleaved sampling using 10 parallel branches
- Automatic detection verification
- Clear visualization of all stages

---

## Technologies Used

- Python 3
- NumPy
- Matplotlib

---

   ```bash
   git clone https://github.com/your-username/time-interleaved-sampling.git
