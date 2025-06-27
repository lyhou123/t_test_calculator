"""
Paired t-test implementation.
"""
import numpy as np
from scipy import stats
from utils.input_validators import get_positive_int, get_float, get_test_type, get_direction
from utils.stats_utils import calculate_effect_size, interpret_effect_size, adjust_pvalue_for_one_tailed
from utils.plotting import plot_paired_data

def paired_t_test():
    """Perform paired t-test."""
    print("\n--- Paired T-Test ---")
    n = get_positive_int("Enter number of paired observations: ")
    
    # Get paired data
    print("Enter data for Group 1 (before/condition 1):")
    group1_data = []
    for i in range(n):
        value = get_float(f"Enter value {i+1}: ")
        group1_data.append(value)
    
    print("Enter data for Group 2 (after/condition 2):")
    group2_data = []
    for i in range(n):
        value = get_float(f"Enter value {i+1}: ")
        group2_data.append(value)
    
    # Convert to numpy arrays
    group1 = np.array(group1_data)
    group2 = np.array(group2_data)
    differences = group1 - group2
    
    # Test parameters
    test_type = get_test_type()
    direction = None
    if test_type == "one-tailed":
        direction = get_direction()
    
    # Perform paired t-test
    t_stat, p_two_tailed = stats.ttest_rel(group1, group2)
    
    # Adjust p-value for one-tailed test
    if test_type == "one-tailed":
        p_val = adjust_pvalue_for_one_tailed(p_two_tailed, t_stat, direction)
    else:
        p_val = p_two_tailed
    
    # Calculate statistics
    mean_diff = np.mean(differences)
    std_diff = np.std(differences, ddof=1)
    df = n - 1
    alpha = 0.05
    
    # Calculate critical values
    if test_type == "two-tailed":
        t_crit = stats.t.ppf(1 - alpha/2, df)
    else:
        t_crit = stats.t.ppf(1 - alpha, df)
    
    # Effect size for paired data
    cohens_d = calculate_effect_size(mean_diff, std_diff)
    
    # Confidence interval for mean difference
    margin_error = t_crit * (std_diff / np.sqrt(n))
    ci_lower = mean_diff - margin_error
    ci_upper = mean_diff + margin_error
    
    # Display results
    print("\n--- Results ---")
    print(f"Group 1 Mean: {np.mean(group1):.3f}")
    print(f"Group 2 Mean: {np.mean(group2):.3f}")
    print(f"Mean Difference: {mean_diff:.3f}")
    print(f"Standard Deviation of Differences: {std_diff:.3f}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"Degrees of Freedom: {df}")
    print(f"p-value: {p_val:.4f}")
    print(f"Critical t-value: ±{t_crit:.3f}" if test_type=="two-tailed" else f"Critical t-value: {t_crit:.3f}")
    print(f"95% CI for Mean Difference: [{ci_lower:.3f}, {ci_upper:.3f}]")
    print(f"Cohen's d (effect size): {cohens_d:.3f}")
    print(f"Effect size interpretation: {interpret_effect_size(cohens_d)}")
    
    # Hypothesis conclusion
    if p_val < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")
    
    # Create visualization
    plot_paired_data(group1, group2, differences)
