# Chi-Squared analysis script

**Version 1.0**
### Creator: Juhani Merilehto - @juhanimerilehto - Jyväskylä University of Applied Sciences (JAMK), Likes institute

![JAMK Likes Logo](./assets/likes_str_logo.png)

## Overview

Chi-Squared Test script. This Python-based tool enables automated analysis of categorical variable relationships using chi-squared tests of independence. Developed for the Strategic Exercise Information and Research unit in Likes Institute, at JAMK University of Applied Sciences, this module provides comprehensive contingency table analysis, effect size calculations, and detailed visualizations of categorical relationships.

## Features

- **Complete Chi-Square Analysis**: Tests of independence with effect sizes
- **Contingency Tables**: Automated creation and analysis of frequency tables
- **Effect Size Calculations**: Cramer's V and standardized residuals
- **Advanced Visualizations**: Heatmaps, grouped bar plots, residual analysis
- **Excel Integration**: Multi-sheet results with observed and expected frequencies
- **Terminal Feedback**: Clear presentation of test statistics and p-values

## Hardware Requirements

- **Python:** 3.8 or higher
- **RAM:** 8GB recommended
- **Storage:** 1GB free space for analysis outputs
- **OS:** Windows 10/11, MacOS, or Linux

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/juhanimerilehto/chi-squared-script.git
cd chi-squared-script
```

### 2. Create a virtual environment:
```bash
python -m venv stats-env
source stats-env/bin/activate  # For Windows: stats-env\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python chi-squared.py
```

With custom parameters:
```bash
python chi-squared.py --excel_path "your_data.xlsx" --row_variable "RowVar" --col_variable "ColVar"
```

## Configuration Parameters

- `excel_path`: Path to Excel file (default: 'data.xlsx')
- `row_variable`: First categorical variable (default: 'RowVar')
- `col_variable`: Second categorical variable (default: 'ColVar')
- `output_prefix`: Prefix for output files (default: 'chisquare')

## File Structure

```plaintext
├── chi-squared-script/
│   ├── assets/
│   │   └── likes_str_logo.png
│   ├── chi-square.py
│   ├── requirements.txt
│   └── README.md
```

## Credits

- **Juhani Merilehto (@juhanimerilehto)** – Specialist, Data and Statistics
- **JAMK Likes** – Organization sponsor

## License

This project is licensed for free use under the condition that proper credit is given to Juhani Merilehto (@juhanimerilehto) and JAMK Likes institute. You are free to use, modify, and distribute this project, provided that you mention the original author and institution and do not hold them liable for any consequences arising from the use of the software.