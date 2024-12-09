import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset():
    """Loads a CSV file into a pandas DataFrame."""
    file_path = input("Enter the path to your CSV file: ")
    try:
        data = pd.read_csv(file_path)
        print("\nDataset loaded successfully!")
        print("Here are the first 5 rows of your dataset:\n")
        print(data.head())
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty. Please provide a valid dataset.")
        return None

def visualize_data(data):
    """Generates a visualization based on user choice."""
    print("\nChoose a visualization type:")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Scatter Plot")
    print("4. Pie Chart")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    try:
        if choice in ('1', '2', '3'):
            x_col = input("Enter the column name for the X-axis: ")
            y_col = input("Enter the column name for the Y-axis: ")
            
            if x_col not in data.columns or y_col not in data.columns:
                print("Invalid column names. Please try again.")
                return
            
            if choice == '1':  # Bar Chart
                sns.barplot(x=data[x_col], y=data[y_col])
            elif choice == '2':  # Line Chart
                plt.plot(data[x_col], data[y_col])
            elif choice == '3':  # Scatter Plot
                sns.scatterplot(x=data[x_col], y=data[y_col])
            
            plt.title(f"{x_col} vs {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        
        elif choice == '4':  # Pie Chart
            pie_col = input("Enter the column name for the pie chart values: ")
            if pie_col not in data.columns:
                print("Invalid column name. Please try again.")
                return
            
            data[pie_col].value_counts().plot.pie(autopct="%1.1f%%")
            plt.title(f"Pie Chart for {pie_col}")
            plt.ylabel("")  # Hide the Y-axis label
            plt.show()
        else:
            print("Invalid choice. Please select a valid visualization type.")
    except Exception as e:
        print(f"An error occurred: {e}")

def data_visualization_tool():
    print("Welcome to the Data Visualization Tool!")
    data = load_dataset()
    if data is not None:
        while True:
            visualize_data(data)
            more = input("\nDo you want to create another visualization? (yes/no): ").lower()
            if more not in ('yes', 'y'):
                print("Thank you for using the Data Visualization Tool!")
                break

# Start the tool
data_visualization_tool()
