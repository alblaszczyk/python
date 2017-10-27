headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
for i in headlines:
    if len(news_ticker) + len(i) <= 140:
        news_ticker = i + " " + "".join(news_ticker)
    else:
        if len(news_ticker) < 140:
            news_ticker += (i[:(140 - len(news_ticker))])
print(news_ticker)
