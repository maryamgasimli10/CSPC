# CSPC — Computer Science for Physics and Chemistry
## Lab A Work
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
---
## PW1 - Lab A: Reproducible Foundations
**What I built:**
- Set up CSPC Git repository with a virtual environment, verified unit tests for radioactive decay simulation using pytest, and benchmarked NumPy speedup against standard Python loops.

**Speed comparison (loop vs NumPy):**
- loop: 0.0114 s
- numpy: 0.0025 s
- speed-up: 4.60x faster
**Tests:** all passing? yes
**Conclusion:**
- Successfully established a reproducible Python environment. Verified that vectorizing array operations with NumPy provides a 4.60x speedup over pure Python loops.  because my computer couldn't download conda with permission of my teacher i replaced it with uv

##PW1 - Lab B:
**What i built:**
A Python script (plot.py) reading decay_observed.csv and creating a $1 \times 2$ subplot comparing raw data to the analytical law $N_0 e^{-\lambda t}$.   A Snakefile pipeline automating the generation of figure.png
**Data vs Analytical Match:
The observed decay data closely follows the theoretical exponential curve ($\lambda = 0.3$) across all time steps.  
 Snakemake Pipeline:
 Tracks file timestamps to run plot.py only when input files change, avoiding redundant runs when outputs are up to date**
** conclusion**
Successfully integrated data visualization with workflow automation, ensuring figures remain reproducible and automatically rebuilt upon data changes.