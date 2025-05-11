import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os



os.makedirs("../outputs/processed", exist_ok=True)

def rain_drop_run():
    df = pd.read_csv("../outputs/raw/pi_points.csv")

    in_points = df[df["label"] == 1]
    out_points = df[df["label"] == 0]

    plt.figure(figsize=(6, 6))
    plt.scatter(in_points["x"], in_points["y"], color="blue", label="Inside Circle", alpha=0.6)
    plt.scatter(out_points["x"], out_points["y"], color="red", label="Outside Circle", alpha=0.6)
    plt.gca().set_aspect("equal")
    plt.title("Monte Carlo Points: Inside vs Outside")
    plt.legend()
    plt.grid(True)
    plt.savefig("../outputs/processed/rain_drop_plot.png")
    plt.show()

def pi_estimate():
    df = pd.read_csv("../outputs/raw/pi_estimates.csv")

    plt.figure()
    plt.plot(df["sample"], df["pi_estimate"], label="Estimated $\pi$")
    plt.axhline(np.pi, color="black", linestyle="--", label="True $\pi$")
    plt.xlabel("Sample Number")
    plt.ylabel("$\pi$ Estimate")
    plt.title("Convergence of $\pi$ Estimate")
    plt.legend()
    plt.grid(True)
    plt.savefig("../outputs/processed/pi_estimate_convergence.png")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pi-visualizer.py [pi_estimate | rain_drop_run]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "pi_estimate":
        pi_estimate()
    elif mode == "rain_drop_run":
        rain_drop_run()
    else:
        print("Unknown mode:", mode)
        print("Use: python pi-visualizer.py [pi_estimate | rain_drop_run]")

