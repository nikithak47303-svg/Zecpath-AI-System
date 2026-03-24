from confidence_analysis import analyze_confidence
from sentiment_analysis import analyze_sentiment
from answer_understanding_engine import build_structured_answer


# ==============================
# BEHAVIOR ANALYSIS FUNCTION
# ==============================

def analyze_behavior(answer):

    confidence = analyze_confidence(answer)
    sentiment = analyze_sentiment(answer)
    understanding = build_structured_answer(answer)

    # ==============================
    # DECISION LOGIC
    # ==============================

    behavior_score = 0

    # Confidence weight
    if confidence["communication_strength"] == "Strong":
        behavior_score += 2
    elif confidence["communication_strength"] == "Moderate":
        behavior_score += 1

    # Sentiment weight
    if sentiment["sentiment"] == "Positive":
        behavior_score += 2
    elif sentiment["sentiment"] == "Neutral":
        behavior_score += 1

    # Answer quality
    if understanding["final_status"] == "valid":
        behavior_score += 2
    elif understanding["final_status"] == "review":
        behavior_score += 1

    # ==============================
    # FINAL BEHAVIOR LABEL
    # ==============================

    if behavior_score >= 5:
        behavior = "Strong Candidate"

    elif behavior_score >= 3:
        behavior = "Average Candidate"

    else:
        behavior = "Weak Candidate"

    return {
        "answer": answer,
        "confidence": confidence,
        "sentiment": sentiment,
        "understanding": understanding,
        "behavior_score": behavior_score,
        "behavior_label": behavior
    }


# ==============================
# MULTIPLE ANSWER ANALYSIS
# ==============================

def analyze_candidate_behavior(answers):

    results = []
    total_score = 0

    for ans in answers:
        result = analyze_behavior(ans)
        results.append(result)
        total_score += result["behavior_score"]

    avg_score = total_score / len(answers)

    # Final behavior summary
    if avg_score >= 5:
        final_label = "Strong Candidate"
    elif avg_score >= 3:
        final_label = "Average Candidate"
    else:
        final_label = "Weak Candidate"

    return {
        "per_answer_behavior": results,
        "average_behavior_score": round(avg_score, 2),
        "final_behavior_label": final_label
    }


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    sample_answers = [
        "I have 2 years of experience in audit and excel",
        "I know python and sql",
        "Maybe I can join after one month",
        "yes",
        "I am confident and ready to work"
    ]

    final_result = analyze_candidate_behavior(sample_answers)

    print("\nBehavioral Analysis Report:\n")
    print(final_result)