def explain_code(code):
    if "for" in code:
        return "This code uses a loop."
    elif "def" in code:
        return "This code defines a function."
    elif "return" in code:
        return "This code returns a value."
    else:
        return "General Python logic."