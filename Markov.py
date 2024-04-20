import numpy as np
import yfinance as yf

def perform_markov_analysis(ticker):
    # Define the states based on price ranges
    states = ['low', 'medium', 'high']

    # Download historical stock data
    stock_data = yf.download(ticker, start='2022-01-01', end='2023-04-14')['Adj Close']

    # Get the most recent price (Friday's closing price)
    latest_price = stock_data[-1]

    # Define the price ranges for each state
    low_range = (stock_data.min(), np.percentile(stock_data, 33))
    medium_range = (np.percentile(stock_data, 33), np.percentile(stock_data, 66))
    high_range = (np.percentile(stock_data, 66), stock_data.max())

    # Assign states to each price in the historical data
    state_sequence = []
    for price in stock_data:
        if low_range[0] <= price < low_range[1]:
            state_sequence.append('low')
        elif medium_range[0] <= price < medium_range[1]:
            state_sequence.append('medium')
        else:
            state_sequence.append('high')

    # Calculate transition probabilities
    transition_matrix = np.zeros((len(states), len(states)))
    for i in range(len(state_sequence) - 1):
        current_state = state_sequence[i]
        next_state = state_sequence[i + 1]
        transition_matrix[states.index(current_state)][states.index(next_state)] += 1

    transition_matrix = transition_matrix / transition_matrix.sum(axis=1, keepdims=True)

    print(f"Transition Matrix for {ticker}:")
    print(transition_matrix)

    print(f"\nTransition Probabilities for {ticker}:")
    for i in range(len(states)):
        for j in range(len(states)):
            print(f"Probability of transitioning from {states[i]} to {states[j]}: {transition_matrix[i][j]:.2%}")

    # Identify the current state of the asset
    current_state = ''
    if low_range[0] <= latest_price < low_range[1]:
        current_state = 'low'
    elif medium_range[0] <= latest_price < medium_range[1]:
        current_state = 'medium'
    else:
        current_state = 'high'

    print(f"\nCurrent State of {ticker}: {current_state}\n")

# Perform Markov chain analysis for MSTR and CLSK
perform_markov_analysis('MSTR')
perform_markov_analysis('CLSK')