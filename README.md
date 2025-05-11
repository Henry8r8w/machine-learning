## Project Structure
### Monte Carlo
An analytical perspective that performs expectation ($\mathbb{E}[X]$) estimation based on probabilistic weighting, which outperforms most numerical integration techniques on fixed range that fall short in higher-dimensional cases.

A textbook example use case is to simulate $\pi$, where the program generates random points in a square and checks how many fall inside a circle.


![pi-setimation](https://github.com/Henry8r8w/probabilitics-machine-learning/blob/main/codes/monte%20carlo/outputs/processed/pi_estimate_convergence.png)
![rain_drop_plot](https://github.com/Henry8r8w/probabilitics-machine-learning/blob/main/codes/monte%20carlo/outputs/processed/rain_drop_plot.png)
```
# Based on Monte Carlo Project #

├── codes/
│   └── monte-carlo/
│       ├── simulations/
│       │   └── pi-simulation-exp.cpp     # C++ simulation script for generating raw data
│       ├── outputs/
│       │   ├── raw/                      # raw data output from C++ (.csv)
│       │   └── processed/                # final plots saved as PNGs
│       └── pi-visualizer.py            
│
├── notes/
│   └── monte-carlo-approximation.md      # obsidian note
│
└── README.md                            
 
```

## Reference
[1] K. P. Murphy, *Probabilistic Machine Learning: An Introduction*, MIT Press, 2023
