from simulations.betting_simulation import BettingSimulation
from strategy.betting_strategy import FlatBettingStrategy, MartingaleStrategy, PercentageBettingStrategy, FibonacciStrategy
from simulations.results import SimulationResults
from strategy.betting_strategy import BettingStrategy

def select_strategy() -> BettingStrategy:
    print("Select a betting strategy:")
    print("1. Flat Betting")
    print("2. Martingale")
    print("3. Percentage of Balance")
    print("4. Fibonacci")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        fixed_bet = int(input("Enter the fixed bet amount: "))
        return FlatBettingStrategy(fixed_bet)
    elif choice == 2:
        initial_bet = int(input("Enter the initial bet amount: "))
        return MartingaleStrategy(initial_bet)
    elif choice == 3:
        percentage = float(input("Enter the percentage of balance to bet (e.g., 0.1 for 10%): "))
        return PercentageBettingStrategy(percentage)
    elif choice == 4:
        return FibonacciStrategy()
    else:
        print("Invalid choice, defaulting to Flat Betting with a bet of 10")
        return FlatBettingStrategy(10)

def main():
    initial_balance = 1000
    num_rounds = 1000
    num_decks = 6
    strategy = select_strategy()
    
    use_basic_strategy = 'y'

    simulation = BettingSimulation(initial_balance, strategy, use_basic_strategy=use_basic_strategy, num_decks=num_decks)
    results, bets = simulation.run_simulation(num_rounds)
    
    SimulationResults.plot_results(results, bets, initial_balance)

if __name__ == "__main__":
    main()
