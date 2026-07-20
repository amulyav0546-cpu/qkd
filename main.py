import numpy as np

from parameters import *

from simulation import estimate_key_rate

from optimizer import optimize_key_rate

from plots import plot_graph

from utils import print_result

#########################################
# Distance Analysis
#########################################

distances = np.arange(10,110,10)

distance_results = []

for d in distances:

    rate = estimate_key_rate(
        d,
        QBER,
        DETECTOR_EFFICIENCY,
        CHANNEL_LOSS,
        BETA,
        NETWORK_FACTOR
    )

    distance_results.append(rate)

plot_graph(
    distances,
    distance_results,
    "Distance (km)",
    "Secret Key Rate",
    "Secret Key Rate vs Distance",
    "output/distance_vs_keyrate.png"
)

#########################################
# QBER Analysis
#########################################

qbers = np.linspace(0.01,0.08,8)

qber_results = []

for q in qbers:

    rate = estimate_key_rate(
        DISTANCE,
        q,
        DETECTOR_EFFICIENCY,
        CHANNEL_LOSS,
        BETA,
        NETWORK_FACTOR
    )

    qber_results.append(rate)

plot_graph(
    qbers,
    qber_results,
    "QBER",
    "Secret Key Rate",
    "Secret Key Rate vs QBER",
    "output/qber_vs_keyrate.png"
)

#########################################
# Detector Efficiency
#########################################

detectors = np.linspace(0.5,1.0,10)

detector_results = []

for eta in detectors:

    rate = estimate_key_rate(
        DISTANCE,
        QBER,
        eta,
        CHANNEL_LOSS,
        BETA,
        NETWORK_FACTOR
    )

    detector_results.append(rate)

plot_graph(
    detectors,
    detector_results,
    "Detector Efficiency",
    "Secret Key Rate",
    "Secret Key Rate vs Detector Efficiency",
    "output/detector_vs_keyrate.png"
)

#########################################
# Existing vs Proposed
#########################################

existing = []

proposed = []

for d in distances:

    existing.append(
        estimate_key_rate(
            d,
            QBER,
            DETECTOR_EFFICIENCY,
            CHANNEL_LOSS,
            BETA,
            1.0
        )
    )

    proposed.append(
        estimate_key_rate(
            d,
            QBER,
            DETECTOR_EFFICIENCY,
            CHANNEL_LOSS,
            BETA,
            NETWORK_FACTOR
        )
    )

import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))

plt.plot(distances, existing, label="Existing")

plt.plot(distances, proposed, label="Proposed")

plt.xlabel("Distance (km)")
plt.ylabel("Secret Key Rate")

plt.title("Existing vs Proposed Framework")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("output/comparison.png")

plt.close()

#########################################

best = optimize_key_rate(proposed)

print_result("Best Estimated Key Rate", best)