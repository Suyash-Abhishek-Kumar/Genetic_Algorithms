# 🌸 Interactive Selection: Evolving Flowers

This project visualizes the evolution of flowers using a **Genetic Algorithm** where user interaction guides natural selection. Hovering over flowers boosts their fitness, influencing which traits survive into the next generation.

> 📁 This is **one of three** Genetic Algorithm projects in the repo. Core GA concepts (fitness, mutation, reproduction, etc.) are explained in the [main repo README](../README.md).

---

## 📂 Project Overview

| File | Description |
|------|-------------|
| `dna.py` | DNA class with gene generation, crossover, and mutation logic. |
| `flower.py` | Flower class that converts genes into visible traits and responds to user interaction. |
| `population.py` | Manages the entire flower population, including selection and reproduction. |
| `sketch.py` | Main script using `pygame` to run the UI and handle interactions. |

---

## 🎯 Selection Method Used: **Weighted Selection**

This project uses **Weighted (Roulette Wheel) Selection** to decide which flowers reproduce.

### 🧠 How It Works:
Each flower’s chance to be selected is proportional to its fitness.  
- A random number is chosen.
- The algorithm walks through the population, subtracting fitness values.
- The individual that causes the counter to drop below zero is selected.

This ensures flowers with higher fitness are more likely (but not guaranteed) to be chosen, maintaining diversity and avoiding premature convergence.

---

## ▶️ How to Run

1. Install requirements:
   ```bash
   pip install pygame
2. Run the program:
   ```bash
   python sketch.py

## 🖼️ Screenshots
