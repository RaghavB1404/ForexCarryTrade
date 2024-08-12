Carry Trade Strategy Implementation
Overview
This project implements a basic quantitative trading strategy for carry trades, primarily used in forex markets. The strategy aims to profit from the interest rate differential between two currencies.
Features

Calculates interest rate differentials
Generates trading signals based on interest rate differences
Computes strategy returns
Calculates key performance metrics (Total Return, Sharpe Ratio, Max Drawdown)

Requirements

Python 3.7+
pandas
numpy

Installation

Clone this repository:
Copygit clone https://github.com/RaghavB1404/ForexCarryTrade.git

Install the required packages:
Copypip install pandas numpy


Usage

Import the necessary libraries and the CarryTradeStrategy class:
import pandas as pd
import numpy as np
from carry_trade_strategy import CarryTradeStrategy

Prepare your data. The data should be a pandas DataFrame with the following columns:

Date (as index)
Currency pair exchange rate (e.g., 'USDEUR')
Base currency interest rate (e.g., 'USD_rate')
Target currency interest rate (e.g., 'EUR_rate')


Initialize and run the strategy:
strategy = CarryTradeStrategy(data, 'USD', 'EUR')
results = strategy.run_strategy()

print("Strategy Performance:")
for metric, value in results.items():
    print(f"{metric}: {value:.4f}")


Customization
You can customize the strategy by modifying the following:

lookback_period in the CarryTradeStrategy initialization
Signal generation logic in the generate_signals method
Performance metrics calculation in the calculate_performance_metrics method

Limitations and Future Improvements
This implementation is a basic version of a carry trade strategy. Potential improvements include:

Incorporating transaction costs
Implementing more sophisticated entry/exit rules
Adding risk management techniques
Including additional performance metrics
Optimizing parameters using historical data

Disclaimer
This code is for educational and research purposes only. It is not financial advice and should not be used for actual trading without thorough testing and customization to your specific needs and risk tolerance.
Contributing
Contributions to improve the strategy or extend its functionality are welcome. Please feel free to submit a pull request or open an issue to discuss potential changes.
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
