import matplotlib.pyplot as plt

def plot_data(data):
    plt.plot(data['index'], data['value'])
    plt.title('Data Visualization')
    plt.show()