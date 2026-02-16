import pandas as pd
from datetime import datetime
import os

class VirtualLedger:
    def __init__(self, log_file="trade_log.csv"):
        self.log_file = log_file
        if not os.path.exists(self.log_file):
            df = pd.DataFrame(columns=['Timestamp', 'Symbol', 'Type', 'Quantity', 'Price', 'Total_Value'])
            df.to_csv(self.log_file, index=False)

    def log_trade(self, symbol, order_type, quantity, price):
        """Logs a buy or sell transaction"""
        total_value = quantity * price
        new_trade = {
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Symbol': symbol.upper(),
            'Type': order_type.upper(),
            'Quantity': quantity,
            'Price': round(price, 2),
            'Total_Value': round(total_value, 2)
        }
        
        df = pd.DataFrame([new_trade])
        df.to_csv(self.log_file, mode='a', header=False, index=False)
        print(f"✅ {order_type} Logged: {quantity} shares of {symbol} at ₹{price}")

    def get_portfolio_summary(self):
        """Reads the log and calculates current holdings"""
        df = pd.read_csv(self.log_file)
        if df.empty: return "Empty Portfolio"

        summary = df.copy()
        summary['Net_Qty'] = summary.apply(lambda x: x['Quantity'] if x['Type'] == 'BUY' else -x['Quantity'], axis=1)
        return summary.groupby('Symbol')['Net_Qty'].sum()

ledger = VirtualLedger()

ledger.log_trade("RELIANCE.NS", "BUY", 10, 1418.80)
ledger.log_trade("RELIANCE.NS", "SELL", 5, 1430.00)

print("\n--- Current Paper Holdings ---")
print(ledger.get_portfolio_summary())