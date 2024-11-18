

# **DaCrypta Bot**

DaCrypta Bot is a Telegram bot that provides features for managing wallets, performing cryptocurrency swaps, viewing TON blockchain transactions, and more. The bot leverages the `pytoncenter` library for interacting with the TON blockchain TestNet and provides a user-friendly interface for various operations.

---

## **Features**

1. **User Authentication**:
   - Register, login, and logout functionality to secure user data.
   
2. **Wallet Management**:
   - Create and manage wallets.
   - Add balance to wallets.
   - View wallet details and balances.
   
3. **Crypto Swapper**:
   - Swap TON to Jetton and vice versa.
   - Fetch and display Jetton details.

4. **Transaction Viewer**:
   - View recent transactions for a given TON wallet address.

---

## **Project Structure**

```
project_directory/
├── bot_main.py          # Main bot file
├── auth_logic.py        # User authentication logic
├── wallet_logic.py      # Wallet management logic
├── swapper_logic.py     # Crypto swapper and transaction viewer logic
```

---

### **File Details**

#### **1. `bot_main.py`**
- **Purpose**: 
  - Entry point for the Telegram bot.
  - Registers all command handlers and integrates the logic from other files.
- **Key Features**:
  - `/start`: Displays a welcome message and options menu.
  - Callback query handler for navigating between bot features.
  - Integrates handlers from `auth_logic.py`, `wallet_logic.py`, and `swapper_logic.py`.

---

#### **2. `auth_logic.py`**
- **Purpose**:
  - Provides basic user authentication functionality to secure access to bot features.
- **Key Features**:
  - `/register <password>`: Register a new user with a password.
  - `/login <password>`: Authenticate an existing user.
  - `/logout`: Logout the user.
- **In-Memory Storage**:
  - User credentials and authentication status are stored in a dictionary. Replace this with a database for production.

---

#### **3. `wallet_logic.py`**
- **Purpose**:
  - Handles wallet management for users.
- **Key Features**:
  - `/create_wallet <name>`: Create a new wallet for the user.
  - `/view_wallets`: View all wallets and their balances.
  - `/add_balance <wallet_id> <amount>`: Add a specified amount to a wallet's balance.
  - `/delete_wallet <wallet_id>`: Delete a wallet by its ID.
- **In-Memory Wallet Storage**:
  - Wallets are stored in a dictionary for simplicity. Replace this with a persistent storage solution for production.

---

#### **4. `swapper_logic.py`**
- **Purpose**:
  - Manages cryptocurrency swaps and transaction viewing functionality.
- **Key Features**:
  - `/swap_to_jetton <wallet_address> <jetton_address> <amount>`: Swap TON to Jetton.
  - `/swap_to_native <wallet_address> <jetton_address> <amount>`: Swap Jetton to TON.
  - `/jetton_info <jetton_address>`: Fetch details about a specific Jetton.
  - `/view_transactions <wallet_address>`: View recent transactions for a wallet address using `pytoncenter`.
- **Blockchain Interaction**:
  - Uses the `pytoncenter` library to interact with the TON blockchain TestNet.

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/DaCrypta-Bot.git
   cd DaCrypta-Bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure the following libraries are installed:
   - `python-telegram-bot`
   - `pytoncenter`

3. **Set Up Environment Variables**:
   Create a `.env` file or replace directly in the code:
   ```bash
   TONCENTER_API_KEY="your_toncenter_api_key"
   TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
   ```

4. **Run the Bot**:
   ```bash
   python bot_main.py
   ```

---

## **How to Use**

1. **Start the Bot**:
   - Send `/start` to the bot in Telegram to view the main menu.

2. **Authentication**:
   - `/register <password>`: Register a new account.
   - `/login <password>`: Log in to your account.
   - `/logout`: Log out.

3. **Wallet Management**:
   - `/create_wallet <name>`: Create a new wallet.
   - `/view_wallets`: List all your wallets with balances.
   - `/add_balance <wallet_id> <amount>`: Add a specific amount to your wallet balance.
   - `/delete_wallet <wallet_id>`: Remove a wallet.

4. **Crypto Exchange**:
   - `/swap_to_jetton <wallet_address> <jetton_address> <amount>`: Swap TON to Jetton.
   - `/swap_to_native <wallet_address> <jetton_address> <amount>`: Swap Jetton to TON.
   - `/jetton_info <jetton_address>`: Get Jetton details.

5. **Transaction Viewer**:
   - `/view_transactions <wallet_address>`: View recent transactions for a TON wallet address.

---

## **Testing**

- Use **TestNet Wallets**:
  Ensure the wallet addresses are from the TON TestNet.

- Example TestNet Wallet Address:
  ```
  EQCwCp3tnzUI4ayCQohm3fjFc-DN7kWdpnHmk-HfB9yzE_a8
  ```

---

## **Future Improvements**

1. **Database Integration**:
   - Replace in-memory storage with a database like SQLite, PostgreSQL, or MongoDB.

2. **Advanced Security**:
   - Hash and securely store user passwords.
   - Use JWT or OAuth for authentication.

3. **MainNet Support**:
   - Add configuration for switching between TestNet and MainNet.

4. **Enhanced Wallet Features**:
   - Support for multiple cryptocurrencies and Jettons.
   - Real-time notifications for transactions.

5. **Error Handling**:
   - Improve resilience against API errors and invalid inputs.

---

## **Contributing**

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit and push your changes.
4. Open a pull request.
