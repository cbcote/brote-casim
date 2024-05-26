import matplotlib.pyplot as plt

class SimulationResults:
    @staticmethod
    def plot_results(results: list) -> None:
        """
        Plot the results of a betting simulation
        
        Args:
            results (list): A list of player balances after each round
        """
        plt.plot(results)
        plt.xlabel('Rounds')
        plt.ylabel('Balance')
        plt.title('Simulation Results')
        plt.show()
