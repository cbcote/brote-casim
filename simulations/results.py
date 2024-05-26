import matplotlib.pyplot as plt

class SimulationResults:
    @staticmethod
    def plot_results(results):
        plt.plot(results)
        plt.xlabel('Rounds')
        plt.ylabel('Balance')
        plt.title('Simulation Results')
        plt.show()
