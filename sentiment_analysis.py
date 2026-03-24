# ==============================
# SENTIMENT KEYWORDS
# ==============================

POSITIVE_WORDS = [
    "confident", "good", "strong", "experienced",
    "skilled", "ready", "interested", "motivated"
]

NEGATIVE_WORDS = [
    "not sure", "maybe", "weak", "no experience",
    "difficult", "problem", "can't", "unable"
]


# ==============================
# SENTIMENT SCORE FUNCTION
# ==============================

def sentiment_score(answer):

    answer = answer.lower()

    pos_score = 0
    neg_score = 0

    for word in POSITIVE_WORDS:
        if word in answer:
            pos_score += 1

    for word in NEGATIVE_WORDS:
        if word in answer:
            neg_score += 1

    return pos_score, neg_score


# ==============================
# SENTIMENT CLASSIFICATION
# ==============================

def classify_sentiment(answer):

    pos, neg = sentiment_score(answer)

    if pos > neg:
        return "Positive"

    elif neg > pos:
        return "Negative"

    else:
        return "Neutral"


# ==============================
# FINAL SENTIMENT OUTPUT
# ==============================

def analyze_sentiment(answer):

    pos, neg = sentiment_score(answer)
    sentiment = classify_sentiment(answer)

    return {
        "answer": answer,
        "positive_score": pos,
        "negative_score": neg,
        "sentiment": sentiment
    }


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    sample_answers = [
        "I am very confident and motivated",
        "Maybe I am not sure about this",
        "I have experience in python",
        "I can't handle this task",
        "I am ready to join immediately"
    ]

    for ans in sample_answers:
        result = analyze_sentiment(ans)

        print("\nAnswer:", ans)
        print("Sentiment Analysis:", result)