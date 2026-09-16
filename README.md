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