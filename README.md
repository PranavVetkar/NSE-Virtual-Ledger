# NSE-Virtual-Ledger

A simple Python-based virtual ledger for tracking paper trades in the NSE (National Stock Exchange). This tool allows you to log BUY and SELL transactions and maintain a running summary of your current holdings.

## 🚀 Features

- **Trade Logging**: Easily record BUY and SELL orders with timestamps, symbol, quantity, and price.
- **Persistent Storage**: Trades are automatically saved to `trade_log.csv`.
- **Portfolio Summary**: Calculates net quantity for each stock in your portfolio.
- **Clean Interface**: Simple console-based output.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PranavVetkar/NSE-Virtual-Ledger.git
   cd NSE-Virtual-Ledger
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Usage

Run the main script to log sample trades and view your holdings:

```bash
python virtual_ledger.py
```

## 🖥️ Example Output

When you run the script, you will see output similar to this:

```text
✅ BUY Logged: 10 shares of RELIANCE.NS at ₹1418.8
✅ SELL Logged: 5 shares of RELIANCE.NS at ₹1430.0

--- Current Paper Holdings ---
Symbol
RELIANCE.NS    5
Name: Net_Qty, dtype: int64
```

## 📂 Project Structure

- `virtual_ledger.py`: The core logic for logging trades and summarizing the portfolio.
- `trade_log.csv`: Automatically generated CSV file containing your transaction history.
- `requirements.txt`: Python dependencies required for the project.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
