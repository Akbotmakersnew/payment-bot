Import io

Import API_HASH, API_ID, BOT_TOKEN

Bot = Client(
    "Payment-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """ Hai Dear {},
Iam a payment bot😁.Do you want to make your own Payment bot?
Use public repo Maintained by: [JOKER TG](https://t.me/IAM_A_JOKER)
[Click here to Pay](https://t.me/IAM_A_JOKER)
"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('❤ Source', url=f"https://github.com/Akbotmakersnew/Payment-bot"), 
        InlineKeyboardButton('👥 Support', url=f"https://t.me/Ls_Supportz")
        ]]
    )

Bot.run()
