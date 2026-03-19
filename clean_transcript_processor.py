import re

# ==============================
# FILLER WORDS LIST
# ==============================

FILLER_WORDS = [
    "um", "uh", "like", "you know", "actually", "basically",
    "so", "well", "hmm"
]

# ==============================
# REMOVE FILLER WORDS
# ==============================

def remove_fillers(text):
    pattern = r'\b(' + '|'.join(FILLER_WORDS) + r')\b'
    cleaned = re.sub(pattern, '', text, flags=re.IGNORECASE)
    return cleaned


# ==============================
# CLEAN TEXT FUNCTION
# ==============================

def clean_transcript(text):

    # 1. Remove filler words
    text = remove_fillers(text)

    # 2. Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # 3. Normalize case
    text = text.strip().lower()

    # 4. Fix punctuation (basic)
    if not text.endswith('.'):
        text += '.'

    return text


# ==============================
# HANDLE PARTIAL / INTERRUPTED SPEECH
# ==============================

def handle_partial_sentences(text):

    # Remove incomplete trailing words
    text = re.sub(r'\b\w{1,2}$', '', text)

    return text.strip()


# ==============================
# MAIN PROCESSOR FUNCTION
# ==============================

def process_transcript(raw_text):

    text = clean_transcript(raw_text)
    text = handle_partial_sentences(text)

    return text


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    raw_input_text = "Um hi I am Arjun uh I completed my MBA like in finance and I have two years experience"

    cleaned = process_transcript(raw_input_text)

    print("Raw Text:")
    print(raw_input_text)

    print("\nCleaned Text:")
    print(cleaned)