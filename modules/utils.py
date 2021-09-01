def parse_list(names: list) -> list:
    """
    Parse strings in multi query methods
    string can be in format
    ["\"name\", \"name2"\"]
    """

    def remove_prefix(text: str, prefix: str):
        return text[text.startswith(prefix) and len(prefix):]

    def remove_postfix(text: str, postfix: str):
        if text.endswith(postfix):
            text = text[:-len(postfix)]
        return text

    if names is None:
        return None

    names = names[0].split(",")

    names = [remove_prefix(n.strip(), "\"") for n in names]
    names = [remove_postfix(n.strip(), "\"") for n in names]

    return names
