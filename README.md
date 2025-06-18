# DRDA – Dynamic Robotic Design Activities

A modular, deployable system for robotic design and assembly using dual ABB IRB 6700 robots.  
This repository contains all code, configuration, and workflows required to simulate and execute robotic pick-and-place tasks using COMPAS RRC and Docker.

---

## 📦 Repo Structure

├── notebooks/ # Jupyter Notebooks for simulations, tests
├── src/robot/ # Python modules and robotic control logic
├── docker/ # Docker setup for ROS & COMPAS RRC
│ └── compas_rrc_driver/ # Driver container files (adapted or copied)
├── external/compas_rrc/ # Git submodule of official COMPAS RRC (optional)
├── .gitignore
├── requirements.txt
└── README.md



---

##  Getting Started

###  1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/DRDA.git
cd DRDA

###  2. Initialize Submodules
git submodule update --init --recursive

###  3. Launch Docker Environment

## This will launch : 
# ROS Mter
# Compas RRC Drivers for /rob1 and /rob2 

cd docker
docker compose up --build

###  4. Launch Docker Environment