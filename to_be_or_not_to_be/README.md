# 🧬 To Be or Not To Be: Evolving Strings with a Genetic Algorithm

This project evolves a population of random strings toward a target phrase using a genetic algorithm. The default target is:

> **"To be or not to be"**

> 📁 This is **one of three** Genetic Algorithm projects in the repo. Core GA concepts (fitness, brute force selection, mutation, and reproduction) are explained in the [main repo README](../README.md).

---

## 📂 Project Overview

| File | Description |
|------|-------------|
| `dna.py` | Represents the DNA of an individual string. Handles gene initialization, fitness calculation, crossover, and mutation. |
| `population.py` | Manages the population: natural selection, reproduction, fitness evaluation, and generation tracking. |
| `tbontbitq.py` | The GUI script (using `pygame`) that visualizes the current best string, average fitness, and history of best phrases per generation. |

---

## 🧠 Highlights

- **Target Matching**: Individuals are scored based on how many characters match the target string.
- **Brute Force Selection**: A mating pool is built based on scaled fitness, giving fitter individuals higher reproductive chances.
- **Character-Level Genes**: Genes are characters (A–z, space, period, question mark).
- **Live GUI**: Real-time updates show the best string and progress over generations.

---

## ▶️ How to Run

1. Install requirements:
   ```bash
   pip install pygame
2. Run the program:

   ```bash
   python tbontbitq.py

## 🖼️ Screenshots
<img src="https://github.com/user-attachments/assets/c46b9c5f-fb2b-4d0b-9671-14d350c5b64e" width="400">
<img src="https://github.com/user-attachments/assets/cf0bf8f0-779c-41dd-942a-dd8ff6414d02" width="400">
