"""
Plotting utilities for statistical visualizations.
"""
import matplotlib.pyplot as plt

def plot_boxplot_single(data, title="Data Distribution", label="Sample", color="lightgreen"):
    """Plot a single boxplot."""
    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=[label], patch_artist=True, boxprops=dict(facecolor=color))
    plt.title(title)
    plt.ylabel("Values")
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_boxplot_two_groups(group1, group2, title="Two-Sample Data Distribution", 
                           labels=["Group 1", "Group 2"], color="lightblue"):
    """Plot boxplots for two groups."""
    plt.figure(figsize=(10, 6))
    plt.boxplot([group1, group2], labels=labels, patch_artist=True,
                boxprops=dict(facecolor=color))
    plt.title(title)
    plt.ylabel("Values")
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_paired_data(group1, group2, differences):
    """Plot paired data with differences."""
    plt.figure(figsize=(10, 6))
    
    plt.subplot(1, 2, 1)
    plt.boxplot([group1, group2], labels=["Group 1", "Group 2"], patch_artist=True,
                boxprops=dict(facecolor="lightcoral"))
    plt.title("Paired Data Distribution")
    plt.ylabel("Values")
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.boxplot(differences, labels=["Differences"], patch_artist=True,
                boxprops=dict(facecolor="lightgreen"))
    plt.title("Differences (Group 1 - Group 2)")
    plt.ylabel("Difference Values")
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
