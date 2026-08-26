from src.handler import (
    handle_name, handle_greeting, handle_farewell_check, handle_recall,
    handle_ask_name, handle_farewell, handle_thanks, handle_help,
    handle_identity, handle_location, handle_forget_me,
)

handlers = {
    "name": handle_name,
    "greeting": handle_greeting,
    "farewell_check": handle_farewell_check,
    "recall": handle_recall,
    "ask_name": handle_ask_name,
    "farewell": handle_farewell,
    "thanks": handle_thanks,
    "help": handle_help,
    "identity": handle_identity,
    "location": handle_location,
    "forget_me": handle_forget_me,
}