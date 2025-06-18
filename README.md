# DRDA – [D]ynamic [R]obotic [D]esign [A]ctivities


DRDA is a modular robotic framework for dual-robot pick-and-place tasks, designed for architectural and fabrication workflows using ABB IRB 6700 robots.

It combines [COMPAS RRC](https://github.com/compas-rrc/compas_rrc) with Docker, Jupyter, and parametric frame exports from Grasshopper to enable a full digital-to-robotic pipeline.

> 🛠️ Based on: [COMPAS RRC](https://github.com/compas-rrc/compas_rrc) and [compas_rrc_start](https://github.com/compas-rrc/compas_rrc_start)

---




## Features

- Dual ABB robot control
- COMPAS RRC integration
- Dockerized ROS setup
- Modular Python scripts
- Jupyter-based debugging
- Parametric frame control

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
git clone https://github.com/nurbsmachine/DRDA.git

cd DRDA
```
###  2. Initialize Submodules
```bash
git submodule update --init --recursive
```

```md
> ℹ️ If `external/compas_rrc/` is included, it contains the official [COMPAS RRC](https://github.com/compas-rrc/compas_rrc) as a Git submodule. Run the command above to initialize it.
```

### 3. Install Dependencies (Recommended via Conda)

If using Anaconda:

```bash
conda create -n drda python=3.9
conda activate drda
pip install compas compas_rrc jupyterlab ipywidgets
```
if using pip:

```
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

```

###  4. Launch Docker Environment

 This will launch : 
 ROS Master,
 Compas RRC Drivers for /rob1 and /rob2 
```bash
cd docker
docker compose up --build

```
This will start:
- ROS Master node
- COMPAS RRC drivers for `/rob1` and `/rob2`
- It connects to ABB OmniCore via IP and streaming ports (e.g., 30101, 30201)
Make sure your RobotStudio simulation or real robot is reachable at the configured IP.

---

## 🤖 Robot Workflow Overview

- Hardware: ABB IRB 6700 (dual robot setup)
- Controller: OmniCore
- Control via: COMPAS RRC, ROS (Docker), Python
- Frame logic: Frames are exported from Grasshopper, structured in JSON, and used for pick/place paths
- Gripper control: Via `SetDigital` I/O commands
- Motion execution: `MoveToFrame`, `Translation.from_vector(...)` for approach/retreat logic


## 📚 Example Notebooks

Check the `notebooks/` folder for Jupyter-based control logic.

- `rrc_picknplace altpunk.ipynb`: Executes dual-robot pick-and-place cycle using predefined frames.


## Tips
> 💡 Tip: Always test movements in RobotStudio before executing on real robots.


## Credits
This repo builds upon the following open-source projects:

- [COMPAS RRC](https://github.com/compas-rrc/compas_rrc) – Remote robot control framework by ETH Zurich
- [compas_rrc_start](https://github.com/compas-rrc/compas_rrc_start) – Starter environment with Docker integration


---

## 🙌 Acknowledgements

This project was made possible through the support and mentorship of two key individuals:

### 🎓 Thesis Advisor: [Júlia Marsal Perendreu](https://www.linkedin.com/in/juliamarsalrobotics/) ([GitHub](https://github.com/roboticswithjulia))

For guiding the research direction of DRDA and helping shape the architectural and robotic vision  
that drives this system. Their insights into fabrication logic, design constraints, and modularity  
pushed this project to operate not just technically — but intelligently.

### 👨‍🏫 Faculty Advisor: [Huanyu Li](https://www.linkedin.com/in/huanyu-li-457590268/) ([GitHub](https://github.com/HuanyuL))

For being the backbone of the execution. From hands-on debugging of ROS-Docker systems  
to helping structure the motion logic, signal synchronization, and simulation pipelines,  
this project wouldn’t have run — literally — without their relentless support.

Their mentorship transformed this workflow from a set of ideas into a working robotic system.

---

> 🙏 To both: thank you for believing in this work and pushing me to take it further.

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.
