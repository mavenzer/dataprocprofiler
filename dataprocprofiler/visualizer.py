
import matplotlib.pyplot as plt

def plot_execution_times(data):
    functions, times = zip(*sorted(data.items(), key=lambda item: item[1]))
    plt.bar(functions, times)
    plt.xlabel('Function')
    plt.ylabel('Execution Time (s)')
    plt.title('Function Execution Times')
    plt.xticks(rotation=45)
    plt.show()
