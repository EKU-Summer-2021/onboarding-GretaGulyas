"""
    Main class.
"""
from src.csv_read import read_csv_pandas
from src.knapsack_problem import KnapsackProblem

if __name__ == '__main__':
    CSV_KP = "https://raw.githubusercontent.com/EKU-Summer-2021/" \
             "intelligent_system_data/main/Intel" \
             "ligent%20System%20Data" \
             "/KP/KP_10.csv "
    dataframe = read_csv_pandas(CSV_KP)
    ksp = KnapsackProblem(dataframe)
    print(ksp.data)
    print(ksp.cost([0, 1, 0, 0, 0, 1]))
    # print(ksp.data["weight"][0])
