from MatrixOperations import MatrixOperations
import StatisticsOperations

matrix = MatrixOperations()
statistics = StatisticsOperations.StatisticsOperations()

while True:
    print("\nChoose an Operation:")
    print("1. Matrix Operations")
    print("2. Statistics Operations")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nMatrix Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Inverse")

        op = input("Enter the operation you want to perform: ")

        if op in ['1', '2', '3']:
            A = matrix.create_matrix()
            B = matrix.create_matrix()

            if op == '1':
                print("Result of Addition:" , matrix.add(A , B))
            if op == '2':
                print("Result of Subtraction:" , matrix.subtract(A , B))
            if op == '3':
                print("Result of Multiplication:" , matrix.multiply(A , B))

        elif op in ['4', '5', '6']:
            A = matrix.create_matrix()

            if op == '4':
                print("Result of Transpose:" , matrix.transpose(A))
            if op == '5':
                print("Result of Determinant:" , matrix.determinant(A))
            if op == '6':
                print("Result of Inverse:" , matrix.inverse(A))

    elif choice == '2':

        print("\n1.Manually Input Data")
        print("2.Load Data from CSV")
        data_choice = input("Enter your choice: ")

        if data_choice == '1':
            data = statistics.get_array()
            print("Data Loaded Successfully.")

        elif data_choice == '2':
            file_path = input("Enter the CSV file path: ")
            column_index = int(input("Enter column index(Starting From 0): "))
            data = statistics.load_from_csv(file_path , column_index)

            if data.size > 0:
                print("Data Loaded Successfully.")
            else:
                print("Failed to load data from CSV.")
                continue
        
        print("\nStatistics Operations:")
        print("1. Mean")
        print("2. Median")
        print("3. Variance")
        print("4. Standard Deviation")
        print("5. Minimum")
        print("6. Maximum")

        op = input("Enter the operation you want to perform: ")
        if op in ['1', '2', '3', '4', '5', '6']:
            data = statistics.get_array()

            if op == '1':
                print("Mean:" , statistics.mean(data))
            if op == '2':
                print("Median:" , statistics.median(data))
            if op == '3':
                print("Variance:" , statistics.variance(data))
            if op == '4':
                print("Standard Deviation:" , statistics.standard_deviation(data))
            if op == '5':
                print("Minimum:" , statistics.minimum(data))
            if op == '6':
                print("Maximum:" , statistics.maximum(data))
        elif op == '7':
            print("Enter First Dataset:")
            x = statistics.get_array()
            print("Enter Second Dataset:")
            y = statistics.get_array()
            print("Correlation Coefficient:" , statistics.percentile(x , y))

    elif choice == '3':
        print("Exiting the program.")
        break
    else:        
        print("Invalid choice. Please try again.")

    
          