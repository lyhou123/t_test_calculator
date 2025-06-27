"""
T-Test Calculator - Main Entry Point
A comprehensive statistical analysis tool for performing various t-tests.
"""

# Import the test functions from their respective modules
from tests.one_sample_test import one_sample_t_test
from tests.two_sample_test import two_sample_t_test
from tests.paired_test import paired_t_test

def main():
    """Main function to run the T-Test Calculator."""
    print("=" * 50)
    print("    Welcome to the T-Test Calculator!")
    print("=" * 50)
    print("Choose the test type:")
    print("1. One-sample t-test")
    print("2. Two-sample independent t-test")
    print("3. Paired t-test")
    print("-" * 50)
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    if choice == '1':
        one_sample_t_test()
    elif choice == '2':
        two_sample_t_test()
    elif choice == '3':
        paired_t_test()
    else:
        print("❌ Invalid choice. Please run the program again and enter 1, 2, or 3.")
        return

    print("\n" + "=" * 50)
    print("    Thank you for using T-Test Calculator!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check your input and try again.")

