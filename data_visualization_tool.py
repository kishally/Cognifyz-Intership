# Task 2: Create a Data Visualization Tool
'''Build a tool that takes a dataset and generates interactive visualizations 
using libraries such as Matplotlib, Seaborn, or Plotly. This task will enhance 
their understanding of data visualization principles and plotting techniques'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_dataset():
    file_path = input("Enter the path to your data file (CSV or Excel): ").strip()
    
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, on_bad_lines='skip') 
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            print("Unsupported file format. Please use .csv or .xlsx")
            return None

        print("Dataset loaded successfully!")
        print("vailable columns:", list(df.columns))
        return df

    except FileNotFoundError:
        print("File not found. Check your path.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def plot_data(df):
    print("\nChoose a plot type:")
    print("1. Line\n2. Bar\n3. Scatter\n4. Histogram")
    choice = input("Enter choice (1-4): ").strip()

    x_col = input("Enter the X-axis column: ").strip() #Restaurant Name
    y_col = input("Enter the Y-axis column (or leave blank for Histogram): ").strip()
    #Rating text
    try:
        if choice == '1':
            sns.lineplot(x=df[x_col], y=df[y_col])
        elif choice == '2':
            sns.barplot(x=df[x_col], y=df[y_col])
        elif choice == '3':
            sns.scatterplot(x=df[x_col], y=df[y_col])
        elif choice == '4':
            sns.histplot(df[x_col], kde=True)
        else:
            print("Invalid choice.")
            return

        plt.title(f"{x_col} vs {y_col}" if y_col else f"{x_col} Distribution")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Plotting Error: {e}")

# Main
df = load_dataset()
if df is not None:
    plot_data(df)
