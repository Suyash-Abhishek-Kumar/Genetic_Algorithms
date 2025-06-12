# 🚀 Finding the Dot: Genetic Algorithm Rocket Simulation

This project simulates a population of rockets navigating to a target (the dot) using a **Genetic Algorithm**. Rockets evolve their paths over generations to reach the goal while avoiding obstacles, which can be added or erased during runtime.

> 📁 This is **one of three** Genetic Algorithm projects in the repo. Core GA concepts (fitness, mutation, reproduction, etc.) are explained in the [main repo README](../README.md).

---

## 📂 Project Overview

| File | Description |
|------|-------------|
| `dna.py` | DNA class defining the rockets' movement genes, crossover, and mutation logic. |
| `rocket.py` | Rocket class handling movement, fitness calculation, and visualization. |
| `vector.py` | Vector2D class for handling rocket movement directions and magnitudes. |
| `population.py` | Manages the rocket population, including evaluation, selection, and reproduction. |
| `screen.py` | Main script using `pygame` for the GUI, obstacle interaction, and runtime display. |

---

## 🎯 Selection Method Used: **Accept-Reject Algorithm**

This project uses the **Accept-Reject Algorithm** to select rockets for reproduction.

### 🧠 How It Works:

- Each rocket’s fitness is normalized by dividing by total population fitness.
- A random number is generated between 0 and 1.
- The algorithm iterates through the population, accumulating normalized fitness values.
- When the accumulated sum exceeds the random number, that rocket is selected as a parent.

This ensures fitter rockets have a higher probability of selection, while less fit ones still get a chance—preserving diversity in the gene pool.

---

## ▶️ How to Run

1. Install requirements:
   ```bash
   pip install pygame
2. Run the program:
   ```bash
   python screen.py
## 🖼️ How It Works
Objective: Rockets start at the bottom center and attempt to reach a black dot near the top.

### Obstacles:

- Right-click + drag → Add obstacles.

- Left-click → Erase obstacles.

### Fitness:

- Based on distance to the target.

- 10× boost for reaching the target.

- 0.1× penalty for crashing into obstacles or screen boundaries.

### Evolution:

- Crossover + mutation evolve better rocket paths.

- Mutation rate dynamically adjusts based on generation performance.

### Display:

- Shows generation, mutation rate, lifetime, and average accuracy.

## 📸 Screenshots
