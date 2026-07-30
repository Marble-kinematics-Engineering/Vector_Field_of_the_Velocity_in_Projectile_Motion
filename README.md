# Title

Vector_Field_of_the_Velocity_in_Projectile_Motion.py

## Abstract

This work presents a detailed study on projectile motion when two macroscopically neutral metallic spheres meet at their trajectory apex.

It is shown that conventional physics textbooks, as well as current digital academic resources, omit the analytical treatment of the exceptional kinematic case in which two independent projectiles coincide simultaneously in the air at their maximum height.

Through an experimental analysis documented by high-precision videography and advanced integral and differential calculus tools, a standardized modular kinematic experimentation platform was deployed. This empirical setup, combined with rigorous classical mechanics, provides a reproducible environment with high educational and metrological value.

Following systematic data extraction from a high-speed frame-by-frame collision analysis, the primary hypothesis is reinforced. The post-collision kinematics provide empirical evidence that individual ball velocities experience a localized increase. This step-like velocity shift reveals the action of an anomalous short-range attractive force acting exclusively at the ápex. This ansatz is formalized herein, demonstrating that the proposed analytical model accurately predicts the geometric scattering and physical behavior of the spheres.

Consequently, the experimental validity of this study relies on monitoring the projectiles' localized temperature at the impact boundary. As demonstrated analytically, mitigating thermal noise and ensuring strict molecular stability remain mandatory parameters to validate the non-conservative energy balance.

## Citation

If you use this code or the executable in your research, please cite the original technical article using the following format:

Hidalgo Fernández, J. (2026). Vector Field of the Velocity in Projectile Motion: Mathematical Modeling and Empirical Validation [Open Researcher and Contributor ID]. ORCID. https://orcid.org/0009-0006-5044-9430

Hidalgo Fernández, J. (2026). Vector Field of the Velocity in Projectile Motion: Mathematical Modeling and Empirical Validation [Includes supplement: Lagrangian formalism, coupling at the apex and Empirical validation of the new central field: Technical Supplement and Analytical Expansion of the Original]. Amazon KDP. https://www.amazon.es/dp/B0H89Y5V37

Hidalgo Fernández, J. (2026). Vector Field of the Velocity in Projectile Motion: Mathematical Modeling and Empirical Validation [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.20960044

Hidalgo Fernández, J. (2026). Vector Field of the Velocity in Projectile Motion: Mathematical Modeling and Empirical Validation [Preprint]. ai.ViXrA. https://ai.vixra.org/abs/2606.0060

Hidalgo Fernández, J. (2026). Vector Field of the Velocity in Projectile Motion: Mathematical Modeling and Empirical Validation [Preprint]. Figshare. https://doi.org/10.6084/m9.figshare.32813108

## Instructions

### Open-Access Code Distribution and Verifiability

The computational animations and numerical simulations associated with the trajectory graphs were executed using script architectures written in Python. Adhering strictly to the Open Science philosophy, both the complete source code and the standalone executable environment are distributed openly under a Creative Commons license via GitHub, with permanent cryptographic archiving in repositories such as CERN Zenodo, Figshare, and ai.viXra. This framework enables independent researchers to execute, replicate, and verify the predictive capacity of the kinematic formulations against real-world data tracks.

### Resolution of the Vertex Indeterminacy via Infinitesimal Phase Shift

In classical projectile kinematics, modeling the exact coordinate transitions at the trajectory vertex (t - t_apex ) introduces a structural mathematical indeterminacy (1/0) within the density functions, a boundary singularity traditionally resolved only through analytical limits or discarded as an unphysical idealization.

To bridge the gap between abstract classical mechanics and physical field behavior, this research introduces an experimental field physics model that breaks with the ideal theoretical paradigm. By implementing an empirical infinitesimal phase shift quantified on the order of  1E15—derived directly from high-resolution hyper slow-motion tracking—the numerical singularity is bypassed. This operational ansatz assumes that absolute zero temporal alignment does not occur during the physical impact configuration at the apex, replacing the infinite density prediction with a continuous, deterministically stable state function.

## Installation and Execution

To run the source code for this project, you need to have **Python 3** installed on your system.

### 1. Clone the repository or download the code

Download the file `Vector_Field_of_the_Velocity_in_Projectile_Motion.py` directly or clone this repository to your computer.

### 2. Install Dependencies

If your code uses external libraries that don't come with Python by default (such as `numpy`, `pandas`, `torch`, `tensorflow`, etc.), run the following command in your terminal to install them:

```bash
pip install -r requirements.txt
```

*(Note: If you don't use external libraries, you can skip this step #2).*

### 3. Run the Script

Open your terminal in the folder where you saved the file and run the following command:

```bash
python Vector_Field_of_the_Velocity_in_Projectile_Motion.py
```

**Don't have Python installed?** If you just want to run the program without configuring any code, go to the **Releases** section on the right of this repository and download the executable version directly.
