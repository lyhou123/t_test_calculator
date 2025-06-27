"""
Statistical utilities for data analysis.
"""
import numpy as np
from scipy import stats
from scipy.stats import nct

def display_descriptive_stats(data, label="Data"):
    """Display descriptive statistics for a dataset."""
    print(f"\n--- Descriptive Statistics for {label} ---")
    print(f"Count: {len(data)}")
    print(f"Mean: {np.mean(data):.3f}")
    print(f"Median: {np.median(data):.3f}")
    print(f"Standard Deviation: {np.std(data, ddof=1):.3f}")
    print(f"Variance: {np.var(data, ddof=1):.3f}")
    print(f"Minimum: {np.min(data):.3f}")
    print(f"Maximum: {np.max(data):.3f}")
    print(f"25th Percentile: {np.percentile(data, 25):.3f}")
    print(f"75th Percentile: {np.percentile(data, 75):.3f}")

def check_normality(data, label="Data"):
    """Check normality assumption using Shapiro-Wilk test."""
    if len(data) < 3:
        print(f"\n--- Normality Check for {label} ---")
        print("Sample size too small for normality test.")
        return
    
    stat, p_val = stats.shapiro(data)
    print(f"\n--- Normality Check for {label} ---")
    print(f"Shapiro-Wilk Test Statistic: {stat:.3f}")
    print(f"p-value: {p_val:.4f}")
    
    if p_val > 0.05:
        print("Data appears to be normally distributed (p > 0.05)")
    else:
        print("Data may not be normally distributed (p ≤ 0.05)")
        print("Consider using non-parametric tests if sample size is small.")

def calculate_power(effect_size, n, alpha=0.05):
    """Calculate statistical power for a t-test."""
    # Calculate non-centrality parameter
    ncp = effect_size * np.sqrt(n)
    
    # Critical t-value for two-tailed test
    t_crit = stats.t.ppf(1 - alpha/2, n-1)
    
    # Calculate power using non-central t-distribution
    power = 1 - nct.cdf(t_crit, n-1, ncp) + nct.cdf(-t_crit, n-1, ncp)
    
    return power

def calculate_effect_size(mean_diff, pooled_std):
    """Calculate Cohen's d effect size."""
    return mean_diff / pooled_std

def interpret_effect_size(cohens_d):
    """Interpret Cohen's d effect size."""
    if abs(cohens_d) < 0.2:
        return "negligible"
    elif abs(cohens_d) < 0.5:
        return "small"
    elif abs(cohens_d) < 0.8:
        return "medium"
    else:
        return "large"

def adjust_pvalue_for_one_tailed(p_two_tailed, t_stat, direction):
    """Adjust p-value for one-tailed test."""
    if direction == "greater":
        return p_two_tailed / 2 if t_stat > 0 else 1 - p_two_tailed / 2
    elif direction == "less":
        return p_two_tailed / 2 if t_stat < 0 else 1 - p_two_tailed / 2
    else:
        raise ValueError("Invalid direction.")

def welch_degrees_of_freedom(s1, s2, n1, n2):
    """Calculate Welch's degrees of freedom for unequal variances."""
    num = (s1**2/n1 + s2**2/n2)**2
    denom = ((s1**2/n1)**2 / (n1-1)) + ((s2**2/n2)**2 / (n2-1))
    return num / denom
