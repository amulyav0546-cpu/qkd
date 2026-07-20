import os
import matplotlib.pyplot as plt

os.makedirs("output", exist_ok=True)


def plot_graph(
    x,
    y,
    xlabel,
    ylabel,
    title,
    filename,
    marker="o",
    linestyle="-"
):

    plt.figure(figsize=(8, 5), dpi=300)

    plt.plot(
        x,
        y,
        marker=marker,
        linewidth=2.5,
        markersize=6,
        linestyle=linestyle,
    )

    plt.title(title, fontsize=15)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    plt.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.close()


def plot_comparison(
    x,
    existing,
    proposed,
    xlabel,
    ylabel,
    title,
    filename
):

    plt.figure(figsize=(8, 5), dpi=300)

    plt.plot(
        x,
        existing,
        marker="s",
        linewidth=2.5,
        label="Existing Framework",
    )

    plt.plot(
        x,
        proposed,
        marker="o",
        linewidth=2.5,
        label="Proposed Framework",
    )

    plt.title(title, fontsize=15)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    plt.grid(True, linestyle="--", alpha=0.5)

    plt.legend()

    plt.tight_layout()

    plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.close()