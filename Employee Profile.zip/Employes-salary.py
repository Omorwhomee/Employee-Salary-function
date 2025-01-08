import pandas as pd
import os
import csv
import zipfile

## Import the salary data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

## Create Employee Function
def get_employee_details(employee_name, employee_data):
    try:
        details = employee_data[employee_data['Name'] == employee_name]
        if not details.empty:
            return details.to_dict('records')[0]
        else:
            raise ValueError(f"No employee found with name {employee_name}")
    except Exception as e:
        print(f"Error: {e}")
        return None

## Data Processing with Dictionary
def create_employee_dict(data):
    try:
        return data.set_index('Name').to_dict(orient='index')
    except Exception as e:
        print(f"Error processing data: {e}")
        return {}

## Export Employee Details to a CSV in a ZIP file
def export_employee_details(employee_details, output_dir="Employee Profile"):
    os.makedirs(output_dir, exist_ok=True)
    csv_file = os.path.join(output_dir, "employee_details.csv")
    try:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=employee_details.keys())
            writer.writeheader()
            writer.writerow(employee_details)

        # Create ZIP file
        zip_file = f"{output_dir}.zip"
        with zipfile.ZipFile(zip_file, 'w') as zf:
            zf.write(csv_file, os.path.basename(csv_file))
        print(f"Employee details exported and zipped at {zip_file}")
    except Exception as e:
        print(f"Error exporting data: {e}")

# Main employee workflow
if __name__ == "__main__":
    file_path = "salary_data.csv"  # Replace with the correct path
    salary_data = load_data(file_path)
    print("Current Directory:", os.getcwd())
    
    if salary_data is not None:
        employee_dict = create_employee_dict(salary_data)
        print("Employee Dictionary Created!")
        
        # Example: Fetch and export a specific employee's details
        emp_name = input("Enter Employee Name: ")
        details = get_employee_details(emp_name, salary_data)
        if details:
            export_employee_details(details)

            
