# T-Test Calculator

A comprehensive statistical analysis tool for performing various types of t-tests with detailed results and visualizations.

## Project Structure

```
data-analy/
├── main.py                    # Main entry point
├── requirements.txt           # Project dependencies
├── README.md                 # Project documentation
├── utils/                    # Utility modules
│   ├── __init__.py
│   ├── input_validators.py   # Input validation functions
│   ├── stats_utils.py        # Statistical utility functions
│   └── plotting.py           # Plotting and visualization functions
└── tests/                    # T-test implementations
    ├── __init__.py
    ├── one_sample_test.py     # One-sample t-test
    ├── two_sample_test.py     # Two-sample independent t-test
    └── paired_test.py         # Paired t-test
```

## Features

### Supported Tests
1. **One-Sample T-Test**: Compare sample mean against a known population mean
2. **Two-Sample Independent T-Test**: Compare means of two independent groups
3. **Paired T-Test**: Compare means of paired observations

### Statistical Features
- Automatic assumption checking (normality, equal variances)
- One-tailed and two-tailed testing options
- Effect size calculation (Cohen's d)
- Confidence intervals
- Comprehensive result interpretation
- Data visualizations (box plots)

### Input Validation
- Robust input validation for all user inputs
- Clear error messages and retry prompts
- Support for both positive and negative numbers where appropriate

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main program:
```bash
python main.py
```

Follow the interactive prompts to:
1. Choose your test type
2. Enter your data
3. Select test parameters (one-tailed vs two-tailed)
4. View detailed results and visualizations

## Example Usage

### One-Sample T-Test
```
Enter sample data (comma separated): 12.5, 13.1, 11.8, 12.9, 13.2, 12.1, 12.7
Enter the population mean to test against (H0 mean): 12.0
Choose test type ('one-tailed' or 'two-tailed'): two-tailed
```

### Two-Sample Independent T-Test
```
Enter sample size for Group 1: 20
Enter mean for Group 1: 75.5
Enter standard deviation for Group 1: 8.2
Enter sample size for Group 2: 22
Enter mean for Group 2: 72.1
Enter standard deviation for Group 2: 7.8
```

### Paired T-Test
```
Enter number of paired observations: 10
Enter data for Group 1 (before/condition 1):
Enter value 1: 85.2
Enter value 2: 87.1
...
```

## Module Documentation

### utils/input_validators.py
Contains functions for validating user input:
- `get_positive_int()`: Validates positive integers
- `get_positive_float()`: Validates positive floats
- `get_float()`: Validates any float
- `get_test_type()`: Validates test type selection
- `get_direction()`: Validates direction for one-tailed tests

### utils/stats_utils.py
Contains statistical utility functions:
- `display_descriptive_stats()`: Shows descriptive statistics
- `check_normality()`: Performs Shapiro-Wilk normality test
- `calculate_power()`: Calculates statistical power
- `calculate_effect_size()`: Calculates Cohen's d
- `interpret_effect_size()`: Interprets effect size magnitude

### utils/plotting.py
Contains visualization functions:
- `plot_boxplot_single()`: Single group box plot
- `plot_boxplot_two_groups()`: Two group comparison
- `plot_paired_data()`: Paired data visualization

### tests/
Contains the main test implementations:
- `one_sample_test.py`: One-sample t-test logic
- `two_sample_test.py`: Independent samples t-test logic
- `paired_test.py`: Paired samples t-test logic

## Dependencies

- numpy: Numerical computations
- scipy: Statistical functions
- matplotlib: Data visualization

## Benefits of This Structure

1. **Modularity**: Each functionality is separated into logical modules
2. **Maintainability**: Easy to update individual components
3. **Reusability**: Utility functions can be reused across different tests
4. **Readability**: Clean, organized code structure
5. **Testability**: Each module can be tested independently
6. **Scalability**: Easy to add new test types or features

## Future Enhancements

- Add ANOVA tests
- Include non-parametric alternatives
- Add data import from CSV files
- Implement sample size calculations
- Add more visualization options
