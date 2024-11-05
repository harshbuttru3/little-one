# Baby Traits Generator

A playful Python project to create a "baby" that inherits traits from two "parents" named Harsh and Dhruvi. This project demonstrates basic Python class usage, randomization, and dictionary manipulation.

## Project Overview

This code simulates creating a "baby" by combining the traits of two parents. Each time you run the code, a unique baby with a randomized name and a blend of traits from the parents is generated!

## How It Works

- The code defines a `Baby` class.
- When a `Baby` object is created, it:
  - Randomly generates a name for the baby by combining elements from the names "Harsh" and "Dhruvi."
  - Inherits various traits from each parent (like hair color, eye color, height, etc.).
  - Randomly selects each trait from either "Mom" or "Dad."
  
## Traits

The traits considered in this project include:
- `hair_color`
- `eye_color`
- `height`
- `intelligence`

Each trait has a value defined for both parents (Mom and Dad), and the baby's traits are randomly selected from one of the parents for each trait.

## Usage

1. Clone this repository or download the code.
2. Run `baby_traits.py` in a Python environment:

   ```bash
   python baby_traits.py
