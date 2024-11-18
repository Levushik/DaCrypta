from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from pytoncenter import get_client
from pytoncenter.v3.models import GetTransactionsRequest

# Initialize the TON Center client for TestNet
TONCENTER_API_KEY = "bc1afb4c1464f96566df9c15db07c7f878e5b04ab37714f32e8f7ca996b0febc"
client = get_client(version="v3", network="testnet", api_key=TONCENTER_API_KEY)

# Fetch transactions using pytoncenter
async def fetch_ton_transactions(address: str, limit: int = 10):
    """
    Fetch the latest transactions for a given wallet address.
    :param address: Wallet address to fetch transactions for.
    :param limit: Number of transactions to fetch.
    :return: List of transactions.
    """
    request = GetTransactionsRequest(address=address, limit=limit)
    transactions = await client.get_transactions(request)
    return transactions

# Command: /view_transactions <wallet_address>
async def view_transactions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    View transactions for a given wallet address.
    Usage: /view_transactions <wallet_address>
    """
    if not context.args:
        await update.message.reply_text("Usage: /view_transactions <wallet_address>")
        return

    wallet_address = context.args[0]
    await update.message.reply_text(f"Fetching transactions for address {wallet_address}...")

    try:
        transactions = await fetch_ton_transactions(wallet_address)
        if not transactions:
            await update.message.reply_text("No transactions found for this address.")
            return

        message = f"📜 *Transactions for {wallet_address}:*\n\n"
        for txn in transactions:
            message += (
                f"🔹 *Hash*: `{txn.hash}`\n"
                f"🔹 *Type*: {txn.type}\n"
                f"🔹 *Amount*: {txn.value / 1e9:.2f} TON\n"
                f"🔹 *Timestamp*: {txn.created_at}\n\n"
            )
        await update.message.reply_text(message, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Failed to fetch transactions: {e}")

# Placeholder for swapper logic
async def swap_to_jetton(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Usage: /swap_to_jetton <wallet_address> <jetton_address> <amount>")
        return
    wallet_address, jetton_address, amount = args[0], args[1], args[2]
    await update.message.reply_text(
        f"Swapping {amount} TON to Jetton {jetton_address} using wallet {wallet_address} (mock implementation)."
    )

async def swap_to_native(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Usage: /swap_to_native <wallet_address> <jetton_address> <amount>")
        return
    wallet_address, jetton_address, amount = args[0], args[1], args[2]
    await update.message.reply_text(
        f"Swapping {amount} Jetton {jetton_address} to TON using wallet {wallet_address} (mock implementation)."
    )

async def jetton_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /jetton_info <jetton_address>")
        return
    jetton_address = context.args[0]
    await update.message.reply_text(
        f"Fetching Jetton info for {jetton_address} (mock implementation)."
    )

# Handlers for swapper logic
swapper_handlers = [
    CommandHandler("swap_to_jetton", swap_to_jetton),
    CommandHandler("swap_to_native", swap_to_native),
    CommandHandler("jetton_info", jetton_info),
    CommandHandler("view_transactions", view_transactions),
]