import matplotlib.pyplot as plt

class SimulationResults:
    @staticmethod
    def plot_results(results, bets, initial_balance):
        if results:
            fig, ax1 = plt.subplots()

            # Plot the balance over rounds
            ax1.plot(results, label='Balance over rounds', color='blue')
            ax1.axhline(y=initial_balance, color='r', linestyle='--', label='Initial Balance')
            ax1.set_xlabel('Rounds')
            ax1.set_ylabel('Balance', color='blue')
            ax1.tick_params(axis='y', labelcolor='blue')

            # Create a second y-axis to plot the bets
            ax2 = ax1.twinx()
            ax2.bar(range(len(bets)), bets, alpha=0.3, label='Bets per round', color='orange')
            ax2.set_ylabel('Bets', color='orange')
            ax2.tick_params(axis='y', labelcolor='orange')

            fig.tight_layout()
            fig.suptitle('Simulation Results', y=1.05)
            ax1.legend(loc='upper left')
            ax2.legend(loc='upper right')
            plt.show()
        else:
            print("No results to plot.")
