def extract_text(file_path):
    """
    Reads resume file and returns text.
    Tries multiple encodings to avoid decode errors.
    """

    try:
        # Try UTF-8 first
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except UnicodeDecodeError:
        try:
            # Try Windows encoding
            with open(file_path, "r", encoding="latin-1") as file:
                return file.read()
        except Exception as e:
            print("Error reading file:", e)
            return ""

    except Exception as e:
        print("Error reading file:", e)
        return ""