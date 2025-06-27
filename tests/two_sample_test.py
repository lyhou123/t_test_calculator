"""
Two-sample independent t-test implementation.
"""
import numpy as np
from scipy import stats
from utils.input_validators import get_positive_int, get_float, get_positive_float, get_test_type
from utils.stats_utils import welch_degrees_of_freedom, calculate_effect_size, interpret_effect_size, adjust_pvalue_for_one_tailed
from utils.plotting import plot_boxplot_two_groups

def two_sample_t_test():
    """Perform two-sample independent t-test."""
    print("\n--- Two-Sample Independent T-Test ---")
    
    # Input group 1
    n1 = get_positive_int("Enter sample size for Group 1: ")
    mean1 = get_float("Enter mean for Group 1: ")
    std1 = get_positive_float("Enter standard deviation for Group 1: ")
    
    # Input group 2
    n2 = get_positive_int("Enter sample size for Group 2: ")
    mean2 = get_float("Enter mean for Group 2: ")
    std2 = get_positive_float("Enter standard deviation for Group 2: ")
    
    # Test parameters
    test_type = get_test_type()
    direction = None
    if test_type == "one-tailed":
        direction = input("Choose direction ('greater' if Group1 > Group2, 'less' if Group1 < Group2): ").strip().lower()
    
    # Generate sample data
    np.random.seed(42)
    group1 = np.random.normal(loc=mean1, scale=std1, size=n1)
    np.random.seed(24)
    group2 = np.random.normal(loc=mean2, scale=std2, size=n2)
    
    # Test for equal variances
    levene_stat, levene_p = stats.levene(group1, group2)
    equal_var = levene_p >= 0.05
    
    # Perform t-test
    t_stat, p_two_tailed = stats.ttest_ind(group1, group2, equal_var=equal_var)
    
    # Adjust p-value for one-tailed test
    if test_type == "one-tailed":
        p_val = adjust_pvalue_for_one_tailed(p_two_tailed, t_stat, direction)
    else:
        p_val = p_two_tailed
    
    # Calculate degrees of freedom
    if not equal_var:
        df = welch_degrees_of_freedom(np.std(group1, ddof=1), np.std(group2, ddof=1), n1, n2)
    else:
        df = n1 + n2 - 2
    
    # Calculate critical values
    alpha = 0.05
    if test_type == "two-tailed":
        t_crit = stats.t.ppf(1 - alpha/2, df)
    else:
        t_crit = stats.t.ppf(1 - alpha, df)
    
    # Calculate effect size and confidence interval
    mean_diff = np.mean(group1) - np.mean(group2)
    pooled_std = np.sqrt(((n1-1)*np.var(group1, ddof=1) + (n2-1)*np.var(group2, ddof=1)) / (n1+n2-2))
    cohens_d = calculate_effect_size(mean_diff, pooled_std)
    
    # Calculate confidence interval for mean difference
    if equal_var:
        pooled_se = pooled_std * np.sqrt(1/n1 + 1/n2)
    else:
        pooled_se = np.sqrt(np.var(group1, ddof=1)/n1 + np.var(group2, ddof=1)/n2)
    
    margin_error = t_crit * pooled_se
    ci_lower = mean_diff - margin_error
    ci_upper = mean_diff + margin_error
    
    # Display results
    print("\n--- Results ---")
    print(f"Group 1 Mean: {np.mean(group1):.3f}")
    print(f"Group 2 Mean: {np.mean(group2):.3f}")
    print(f"Mean Difference: {mean_diff:.3f}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"Degrees of Freedom: {df:.3f}")
    print(f"p-value: {p_val:.4f}")
    print(f"Critical t-value: ±{t_crit:.3f}" if test_type=="two-tailed" else f"Critical t-value: {t_crit:.3f}")
    print(f"95% CI for Mean Difference: [{ci_lower:.3f}, {ci_upper:.3f}]")
    print(f"Cohen's d (effect size): {cohens_d:.3f}")
    print(f"Equal Variances Assumed? {'Yes' if equal_var else 'No'}")
    print(f"Effect size interpretation: {interpret_effect_size(cohens_d)}")
    
    # Hypothesis conclusion
    if p_val < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")
    
    # Create visualization
    plot_boxplot_two_groups(group1, group2)
