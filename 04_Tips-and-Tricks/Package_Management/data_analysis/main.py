from scripts.data_analysis import load_data, calculate_statistics
from scripts.data_visualization import plot_data

def main():

    filepath = './data/sample_data.csv'
    data = load_data(filepath)

    mean = calculate_statistics(data)
    print("Mean:", mean)

    plot_data(data)

if __name__ == "__main__":
    main()