import numpy as np
import csv

class StatisticsOperations:

    def get_array(self):
        data = list(map(float , input("Enter Number Seperated By Space: ").split()))
        return np.array(data)
    
    def load_from_csv(self, file_path, column_index):
        try:
            file_path = file_path.strip().replace('"', '').replace("'", "")

            data = []

            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)

                # Check if column index is valid
                if column_index < 0 or column_index >= len(header):
                    print("Invalid column index!")
                    print("Available columns (with index):")
                    for i, col in enumerate(header):
                        print(i, "→", col)
                    return None

                for row in reader:
                    try:
                        data.append(float(row[column_index]))
                    except ValueError:
                        print("Non-numeric value found. Skipping row.")

            if len(data) == 0:
                print("No numeric data found in selected column.")
                return None

            return np.array(data)

        except FileNotFoundError:
            print("File not found. Please check path.")
            return None

        except Exception as e:
            print("Error loading CSV:", e)
            return None

    def mean(self , data):
        return np.mean(data)
    
    def median(self , data):
        return np.median(data)
    
    def variance(self , data):
        return np.var(data)
    
    def standard_deviation(self , data):
        return np.std(data)
    
    def minimum(self , data):
        return np.min(data)
    
    def maximum(self , data):
        return np.max(data)
    
    def percentile(self , x , y):
        return np.corrcoef(x, y)[0, 1] #correlation coefficient between two arrays x and y