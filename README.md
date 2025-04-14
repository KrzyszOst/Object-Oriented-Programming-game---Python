# 🌍 2D Virtual World Simulator (OOP Project - Pyhon version) 🧬

This is a university project for the **Object-Oriented Programming** course.  
The goal was to implement a 2D life simulation using Python and a GUI library.

## 🧠 Project Overview

- 🧬 Object-Oriented structure with abstract base class `Organism`
- 🧍 Player-controlled `Human` with **activatable special ability**
- 🐾 Animals and 🌱 Plants with unique behaviors and interactions
- 🔁 Turn-based system with action order based on initiative & age
- 🧩 GUI-based visualization (e.g. Tkinter or PyQt)
- 💾 Optional saving/loading of simulation state

## 🦁 Life Forms Implemented

### 🐾 Animals:
- **Wolf** — strong, fights others  
- **Sheep** — peaceful, simple behavior  
- **Fox** — avoids stronger organisms  
- **Turtle** — slow, reflects weak attacks  
- **Antelope** — moves in wide range, can flee  
- **Cyber-sheep** — seeks out Sosnowsky's hogweed

### 🌱 Plants:
- **Grass** — default behavior  
- **Sow Thistle** — spreads 3x per turn  
- **Guarana** — boosts strength of the eater  
- **Belladonna** — kills any animal that eats it  
- **Sosnowsky's Hogweed** — toxic to nearby animals  

## 🧍 Human

- Moves with **arrow keys** (or via GUI buttons/keys)
- Has a **special ability** (e.g. immortality, purification, speed boost)
- Active for **5 rounds**, then cooldown for **5 rounds**
- Only one human on the map at any time

## 🖼️ GUI Features

- Grid-based map with colored or symbolic representation of organisms  
- Console/message box with **logs** of key events: fights, births, deaths  
- Control panel for turn progression, saving, loading, and ability activation  
- Optional: Add new organisms by clicking on empty cells  

## 🧱 Installation & Run

Ensure Python 3 is installed with your chosen GUI library (e.g. Tkinter or PyQt5).

```bash
git clone https://github.com/yourusername/oop-world-simulator-python.git
cd oop-world-simulator-python
python main.py
