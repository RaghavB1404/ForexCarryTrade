import pandas as pd
import numpy as np

class CarryTradeStrategy:
    def __init__(self, data, base_currency, target_currency, lookback_period=20):
        self.data = data
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.lookback_period = lookback_period
    
    def calculate_interest_rate_differential(self):
        self.data['interest_rate_diff'] = (
            self.data[f'{self.target_currency}_rate'] - 
            self.data[f'{self.base_currency}_rate']
        )
    
    def generate_signals(self):
        self.data['signal'] = np.where(
            self.data['interest_rate_diff'] > 0, 1,
            np.where(self.data['interest_rate_diff'] < 0, -1, 0)
        )
    
    def calculate_returns(self):
        self.data['returns'] = self.data[f'{self.base_currency}{self.target_currency}'].pct_change()
        self.data['strategy_returns'] = self.data['signal'].shift(1) * self.data['returns']
    
    def calculate_performance_metrics(self):
        cumulative_returns = (1 + self.data['strategy_returns']).cumprod()
        total_return = cumulative_returns.iloc[-1] - 1
        sharpe_ratio = np.sqrt(252) * self.data['strategy_returns'].mean() / self.data['strategy_returns'].std()
        max_drawdown = (cumulative_returns / cumulative_returns.cummax() - 1).min()
        
        return {
            'Total Return': total_return,
            'Sharpe Ratio': sharpe_ratio,
            'Max Drawdown': max_drawdown
        }
    
    def run_strategy(self):
        self.calculate_interest_rate_differential()
        self.generate_signals()
        self.calculate_returns()
        return self.calculate_performance_metrics()

if __name__ == "__main__":
    dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'USDEUR': np.random.normal(1.1, 0.05, len(dates)),
        'USD_rate': np.random.uniform(0.01, 0.03, len(dates)),
        'EUR_rate': np.random.uniform(0, 0.02, len(dates))
    })
    data.set_index('Date', inplace=True)
    
    strategy = CarryTradeStrategy(data, 'USD', 'EUR')
    results = strategy.run_strategy()
    
    print("Strategy Performance:")
    for metric, value in results.items():
        print(f"{metric}: {value:.4f}")