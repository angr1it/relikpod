from relikpod.config import coref_nlp


# Coreference resolution function
def coref_text(text: str) -> str:
    """
    Resolves coreferences in the given text using the coreferee library.

    Args:
        text (str): The input text to resolve coreferences in.

    Returns:
        str: The text with coreferences resolved.
    """
    coref_doc = coref_nlp(text)
    resolved_text = ""
    for token in coref_doc:
        repres = coref_doc._.coref_chains.resolve(token)
        if repres:
            resolved_text += " " + " and ".join(
                [
                    (
                        t.text
                        if t.ent_type_ == ""
                        else [e.text for e in coref_doc.ents if t in e][0]
                    )
                    for t in repres
                ]
            )
        else:
            resolved_text += " " + token.text
    return resolved_text
