# 🧠 Genetic Algorithm Projects Collection

This repository contains **three interactive projects** built using **Genetic Algorithms (GA)**, each with a different evolutionary goal:

1. 🌸 [Interactive Selection](./InteractiveSelection/) – Evolve beautiful flowers based on user interaction.
2. 🧬 [To Be or Not To Be](./To_be_or_not_to_be/) – Evolve a string to match a target phrase.
3. 🚀 [Finding the Dot](./FindingTheDot/) – Guide rockets to a target while avoiding obstacles.

These projects demonstrate the **core components** of Genetic Algorithms in visually engaging and intuitive ways.

---

## 📚 What is a Genetic Algorithm?

A **Genetic Algorithm** is a nature-inspired search heuristic based on the process of **natural selection**. It's commonly used for optimization problems where traditional methods struggle.

---

## 🔁 Key Concepts

### 🧬 DNA (Genes)
Each individual (flower, string, rocket) contains a DNA object, which is a set of genes. These genes define the traits/behavior of that individual.

---

### 🧠 Fitness Function
The **fitness** of an individual is a score that reflects how well it performs the desired task:

| Project | Fitness Criteria |
|--------|------------------|
| Interactive Selection | How often a user hovers over the flower |
| To Be or Not To Be | Number of characters matching the target phrase |
| Finding the Dot | Distance to the target + penalty for crashing |

---

### 💑 Reproduction (Crossover)
Two individuals are selected as parents to produce a child. Their DNA is **crossovered** at a random midpoint, blending traits from both.

---

### 🔄 Mutation
Mutation introduces small random changes in DNA to maintain diversity and avoid local optima.

Example:  
If a gene was `'A'`, it might randomly mutate to `'Q'`.

---

## 🧪 Selection Techniques Used

| Project | Selection Method |
|---------|------------------|
| Interactive Selection | Weighted (Roulette Wheel) Selection |
| To Be or Not To Be | Brute Force via Mating Pool |
| Finding the Dot | Accept-Reject Algorithm |

---

## ▶️ How to Run Any Project

1. Install the dependency:
   ```bash
   pip install pygame
2. Navigate to the project folder and run:
   ```bash
   python <main_script>.py
Each project has its own README inside its folder with detailed instructions.

## 🛠 Technologies Used
- Python 3
- pygame for visualization
- Object-oriented design
- Custom fitness and selection logic

## 🌱 Why This Repo?
This repo was created to explore Genetic Algorithms in a hands-on, visual way. By working through these mini-projects, you’ll understand how evolution-like behavior emerges from simple rules and randomness.

## 📎 Links to Individual Projects
🌸 [Interactive Selection](./InteractiveSelection/)

🧬 [To Be or Not To Be](./To_be_or_not_to_be/)

🚀 [Finding the Dot](./FindingTheDot/)

