"""
One-sample t-test implementation.
"""
import numpy as np
from scipy import stats
from utils.input_validators import get_test_type, get_direction
from utils.plotting import plot_boxplot_single

def one_sample_t_test():
    """Perform one-sample t-test."""
    print("\n--- One-Sample T-Test ---")
    
    # Get sample data
    raw_input = input("Enter sample data (comma separated): ")
    data = np.array([float(x.strip()) for x in raw_input.split(",")])
    
    # Get test parameters
    mu_0 = float(input("Enter the population mean to test against (H0 mean): "))
    test_type = get_test_type()
    direction = None
    if test_type == "one-tailed":
        direction = get_direction()
    
    # Calculate statistics
    n = len(data)
    mean_sample = np.mean(data)
    std_dev = np.std(data, ddof=1)
    se = std_dev / np.sqrt(n)
    
    # Perform one-sample t-test
    t_stat, p_two_tailed = stats.ttest_1samp(data, popmean=mu_0)
    
    # Adjust p-value for one-tailed test
    if test_type == "one-tailed":
        if direction == "greater":
            p_val = p_two_tailed / 2 if t_stat > 0 else 1 - p_two_tailed / 2
        elif direction == "less":
            p_val = p_two_tailed / 2 if t_stat < 0 else 1 - p_two_tailed / 2
        else:
            raise ValueError("Invalid direction.")
    else:
        p_val = p_two_tailed
    
    # Calculate critical values
    alpha = 0.05
    df = n - 1
    t_crit = stats.t.ppf(1 - alpha/2, df) if test_type == "two-tailed" else stats.t.ppf(1 - alpha, df)
    
    # Display results
    print("\n--- Results ---")
    print(f"Sample Size: {n}")
    print(f"Sample Mean: {mean_sample:.3f}")
    print(f"Standard Deviation: {std_dev:.3f}")
    print(f"Standard Error: {se:.3f}")
    print(f"Population Mean (H0): {mu_0}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"Degrees of Freedom: {df}")
    print(f"p-value: {p_val:.4f}")
    print(f"Critical t-value: ±{t_crit:.3f}" if test_type=="two-tailed" else f"Critical t-value: {t_crit:.3f}")
    
    # Hypothesis conclusion
    if p_val < alpha:
        print("✅ Reject the null hypothesis.")
    else:
        print("❌ Fail to reject the null hypothesis.")
    
    # Create visualization
    plot_boxplot_single(data, "One-Sample Data Distribution", "Sample", "lightgreen")
