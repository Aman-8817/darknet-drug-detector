# nlp_detection.py

import spacy
from spacy.matcher import PhraseMatcher

# Load English model
nlp = spacy.load("en_core_web_sm")

# Suspicious keywords/phrases
keywords = ["coke", "ganja", "MDMA", "white powder", "pills", "cocaine", "heroin", "marijuana", "cannabis", "ecstasy"]

# Create PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(text) for text in keywords]
matcher.add("DRUGTERMS", patterns)

def detect_suspicious(text):
    doc = nlp(text)
    matches = matcher(doc)
    flagged_terms = []
    for match_id, start, end in matches:
        span = doc[start:end]
        flagged_terms.append(span.text)
    return flagged_terms

if __name__ == "__main__":
    test_text = "New shipment of cocaine and ecstasy available discreetly."
    flagged = detect_suspicious(test_text)
    print(f"Flagged Terms: {flagged}")
