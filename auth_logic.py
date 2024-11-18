from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# In-memory user storage (replace with a database for production)
users = {}

# Command: /register <password>
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /register <password>")
        return

    user_id = update.effective_user.id
    password = context.args[0]

    if user_id in users:
        await update.message.reply_text("You are already registered.")
        return

    # Register the user
    users[user_id] = {"password": password}
    await update.message.reply_text("✅ Registration successful! You can now log in using /login <password>.")

# Command: /login <password>
async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /login <password>")
        return

    user_id = update.effective_user.id
    password = context.args[0]

    if user_id not in users:
        await update.message.reply_text("❌ You are not registered. Use /register <password> to sign up.")
        return

    if users[user_id]["password"] == password:
        users[user_id]["is_authenticated"] = True
        await update.message.reply_text("✅ Login successful!")
    else:
        await update.message.reply_text("❌ Incorrect password. Please try again.")

# Command: /logout
async def logout(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id

    if user_id in users and users[user_id].get("is_authenticated", False):
        users[user_id]["is_authenticated"] = False
        await update.message.reply_text("✅ You have been logged out.")
    else:
        await update.message.reply_text("❌ You are not logged in.")

# Middleware: Check if the user is authenticated
async def is_authenticated(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user_id = update.effective_user.id
    return users.get(user_id, {}).get("is_authenticated", False)

# Handlers for authentication
auth_handlers = [
    CommandHandler("register", register),
    CommandHandler("login", login),
    CommandHandler("logout", logout),
]
