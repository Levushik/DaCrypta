from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# In-memory wallets storage (user_id -> wallet data)
wallets = {}

# Command: /create_wallet <name>
async def create_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    wallet_name = context.args[0] if context.args else "Default Wallet"
    wallet_id = len(wallets) + 1

    wallets[wallet_id] = {"name": wallet_name, "user_id": user_id, "balance": 0.0}
    await update.message.reply_text(f"Wallet '{wallet_name}' created successfully! Wallet ID: {wallet_id}")

# Command: /view_wallets
async def view_wallets(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    user_wallets = [
        f"ID: {wid}, Name: {w['name']}, Balance: {w['balance']:.2f} TON"
        for wid, w in wallets.items()
        if w["user_id"] == user_id
    ]
    if not user_wallets:
        await update.message.reply_text("No wallets found.")
        return
    await update.message.reply_text("\n".join(user_wallets))

# Command: /add_balance <wallet_id> <amount>
async def add_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /add_balance <wallet_id> <amount>")
        return

    wallet_id, amount = context.args
    wallet_id = int(wallet_id)
    amount = float(amount)

    if wallet_id not in wallets:
        await update.message.reply_text(f"Wallet ID {wallet_id} not found.")
        return

    wallet = wallets[wallet_id]
    wallet["balance"] += amount
    await update.message.reply_text(
        f"✅ {amount:.2f} TON added to wallet '{wallet['name']}'! New balance: {wallet['balance']:.2f} TON"
    )

# Command: /delete_wallet <wallet_id>
async def delete_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /delete_wallet <wallet_id>")
        return

    wallet_id = int(context.args[0])
    if wallet_id in wallets:
        del wallets[wallet_id]
        await update.message.reply_text(f"Wallet '{wallet_id}' deleted successfully.")
    else:
        await update.message.reply_text(f"Wallet '{wallet_id}' not found.")

# Handlers for wallet logic
wallet_handlers = [
    CommandHandler("create_wallet", create_wallet),
    CommandHandler("view_wallets", view_wallets),
    CommandHandler("add_balance", add_balance),
    CommandHandler("delete_wallet", delete_wallet),
]
