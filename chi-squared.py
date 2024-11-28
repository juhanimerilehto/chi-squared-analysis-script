import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def perform_chisquare_analysis(excel_path='data.xlsx',
                             row_variable='RowVar',     # First categorical variable
                             col_variable='ColVar',     # Second categorical variable
                             output_prefix='chisquare'):
    """
    Performs Chi-Square test of independence between two categorical variables.
    
    Parameters:
    -----------
    excel_path : str
        Path to Excel file containing the data
    row_variable : str
        Name of first categorical variable
    col_variable : str
        Name of second categorical variable
    output_prefix : str
        Prefix for output files
    """
    
    # Read the data
    print(f"Reading data from {excel_path}...")
    df = pd.read_excel(excel_path)
    
    # Create contingency table
    contingency_table = pd.crosstab(df[row_variable], df[col_variable])
    
    # Perform chi-square test
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    
    # Calculate effect size (Cramer's V)
    n = contingency_table.sum().sum()
    min_dim = min(contingency_table.shape) - 1
    cramer_v = np.sqrt(chi2 / (n * min_dim))
    
    # Create results dictionary
    results = {
        'Test Type': 'Chi-Square Test of Independence',
        'Chi-Square Statistic': chi2,
        'p-value': p_value,
        'Degrees of Freedom': dof,
        'Sample Size': n,
        "Cramer's V": cramer_v,
        'Significant': 'Yes' if p_value < 0.05 else 'No'
    }
    
    # Create expected frequencies DataFrame
    expected_df = pd.DataFrame(
        expected,
        index=contingency_table.index,
        columns=contingency_table.columns
    )
    
    # Calculate standardized residuals
    observed = contingency_table.values
    std_residuals = (observed - expected) / np.sqrt(expected)
    residuals_df = pd.DataFrame(
        std_residuals,
        index=contingency_table.index,
        columns=contingency_table.columns
    )
    
    # Create timestamp for file naming
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save results to Excel
    excel_output = f'{output_prefix}_results_{timestamp}.xlsx'
    with pd.ExcelWriter(excel_output) as writer:
        pd.DataFrame([results]).to_excel(
            writer, sheet_name='Test Results', index=False
        )
        contingency_table.to_excel(
            writer, sheet_name='Observed Frequencies'
        )
        expected_df.to_excel(
            writer, sheet_name='Expected Frequencies'
        )
        residuals_df.to_excel(
            writer, sheet_name='Standardized Residuals'
        )
    
    print("\nResults saved to:", excel_output)
    
    # Create visualizations
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Observed Frequencies Heatmap
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='YlOrRd', ax=ax1)
    ax1.set_title('Observed Frequencies')
    
    # 2. Expected Frequencies Heatmap
    sns.heatmap(expected_df, annot=True, fmt='.1f', cmap='YlOrRd', ax=ax2)
    ax2.set_title('Expected Frequencies')
    
    # 3. Standardized Residuals Heatmap
    sns.heatmap(residuals_df, annot=True, fmt='.2f', 
                cmap='RdBu', center=0, ax=ax3)
    ax3.set_title('Standardized Residuals')
    
    # 4. Grouped Bar Plot
    contingency_table.plot(kind='bar', ax=ax4)
    ax4.set_title('Grouped Bar Plot of Frequencies')
    ax4.set_xlabel(row_variable)
    ax4.set_ylabel('Count')
    ax4.legend(title=col_variable)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    # Save plot
    plot_output = f'{output_prefix}_plot_{timestamp}.png'
    plt.savefig(plot_output, dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Plot saved to:", plot_output)
    
    # Print results to terminal
    print("\nChi-Square Test Results:")
    print("----------------------")
    print(f"Chi-square statistic: {chi2:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Degrees of freedom: {dof}")
    print(f"Cramer's V: {cramer_v:.4f}")
    print(f"Significant: {'Yes' if p_value < 0.05 else 'No'}")
    print("\nContingency Table:")
    print(contingency_table)

if __name__ == "__main__":
    # Example usage:
    # Modify these parameters according to your data
    perform_chisquare_analysis(
        excel_path='data.xlsx',
        row_variable='RowVar',
        col_variable='ColVar',
        output_prefix='chisquare'
    )