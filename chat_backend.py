def answer_query(user_message, history):
    return (
        "👋 Backend is connected!\n\n"
        f"You asked: **{user_message}**\n\n"
        f"Messages so far in this chat: {len(history)}"
    )
