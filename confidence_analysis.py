import re


# ==============================
# HESITATION WORDS
# ==============================

HESITATION_WORDS = ["um", "uh", "maybe", "not sure", "i think", "kind of"]


# ==============================
# DETECT HESITATION
# ==============================

def detect_hesitation(answer):

    count = 0
    answer_lower = answer.lower()

    for word in HESITATION_WORDS:
        if word in answer_lower:
            count += 1

    return count


# ==============================
# RESPONSE LENGTH SCORE
# ==============================

def response_length_score(answer):

    word_count = len(answer.split())

    if word_count < 3:
        return 2   # too short

    elif word_count < 8:
        return 5   # moderate

    else:
        return 8   # good


# ==============================
# CONFIDENCE SCORE
# ==============================

def confidence_score(answer):

    hesitation_count = detect_hesitation(answer)

    if hesitation_count > 1:
        return 3   # low confidence

    elif hesitation_count == 1:
        return 5   # medium

    else:
        return 8   # high confidence


# ==============================
# COMMUNICATION STRENGTH
# ==============================

def communication_strength(answer):

    length = response_length_score(answer)
    confidence = confidence_score(answer)

    score = (length + confidence) / 2

    if score >= 7:
        return "Strong"

    elif score >= 4:
        return "Moderate"

    else:
        return "Weak"


# ==============================
# MAIN ANALYSIS FUNCTION
# ==============================

def analyze_confidence(answer):

    hesitation = detect_hesitation(answer)
    length_score = response_length_score(answer)
    confidence = confidence_score(answer)
    strength = communication_strength(answer)

    return {
        "answer": answer,
        "hesitation_count": hesitation,
        "length_score": length_score,
        "confidence_score": confidence,
        "communication_strength": strength
    }


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    sample_answers = [
        "Um I think I have some experience",
        "I have 2 years of experience in audit and excel",
        "yes",
        "Maybe I can join after one month",
        "I am very confident and ready to join immediately"
    ]

    for ans in sample_answers:
        result = analyze_confidence(ans)

        print("\nAnswer:", ans)
        print("Confidence Analysis:", result)