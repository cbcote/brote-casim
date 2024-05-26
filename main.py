from simulations.betting_simulation import BettingSimulation
from simulations.strategy import FlatBettingStrategy, MartingaleStrategy
from simulations.results import SimulationResults

def main():
    initial_balance = 100
    num_rounds = 100
    strategy = FlatBettingStrategy(10)  # or MartingaleStrategy(10)

    simulation = BettingSimulation(initial_balance, strategy)
    results = simulation.run_simulation(num_rounds)
    
    SimulationResults.plot_results(results)

if __name__ == "__main__":
    main()
