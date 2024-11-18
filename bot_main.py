from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from wallet_logic import wallet_handlers
from swapper_logic import swapper_handlers
from auth_logic import auth_handlers, is_authenticated

# Bot token
TOKEN = "7561714682:AAERsQvi_Dij2OGeJ30YqvaYLocyceEiI4U"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message with menu options."""
    keyboard = [
        [InlineKeyboardButton("🔐 User Authentication", callback_data="auth")],
        [InlineKeyboardButton("💼 Wallet", callback_data="wallet")],
        [InlineKeyboardButton("💱 Crypto Exchange", callback_data="exchange")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to DaCrypta Bot! Choose an option:", reply_markup=reply_markup)

# Callback query handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "auth":
        await query.edit_message_text(
            "🔐 Authentication Commands:\n"
            "- /register <password>: Register an account.\n"
            "- /login <password>: Log in to your account.\n"
            "- /logout: Log out."
        )
    elif data == "wallet":
        if not await is_authenticated(update, context):
            await query.edit_message_text("❌ Please log in first using /login <password>.")
            return
        await query.edit_message_text(
            "💼 Wallet Commands:\n"
            "- /create_wallet <name>: Create a wallet.\n"
            "- /view_wallets: View all wallets.\n"
            "- /add_balance <wallet_id> <amount>: Add balance to a wallet.\n"
            "- /delete_wallet <wallet_id>: Delete a wallet."
        )
    elif data == "exchange":
        if not await is_authenticated(update, context):
            await query.edit_message_text("❌ Please log in first using /login <password>.")
            return
        await query.edit_message_text(
            "💱 Crypto Exchange Commands:\n"
            "- /swap_to_jetton <wallet_address> <jetton_address> <amount>: Swap TON to Jetton.\n"
            "- /swap_to_native <wallet_address> <jetton_address> <amount>: Swap Jetton to TON.\n"
            "- /jetton_info <jetton_address>: Get Jetton information.\n"
            "- /view_transactions: View available TON transactions."
        )


# Main function to set up the bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Add start and callback handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Register authentication handlers
    for handler in auth_handlers:
        application.add_handler(handler)

    # Register wallet and swapper handlers
    for handler in wallet_handlers + swapper_handlers:
        application.add_handler(handler)

    # Start the bot
    application.run_polling()
    print("Bot is running...")

if __name__ == "__main__":
    main()
