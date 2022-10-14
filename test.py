import spacy
nlp = spacy.load("en_core_web_lg")


def remove_stop_words(text):
    '''Removes stop words from text'''
    doc = nlp(text.lower())

    result = [
        token.text for token in doc if token.text not in nlp.Defaults.stop_words]
    return " ".join(result)


def main():
    case_a = "This is a sentence."
    case_b = "This is also a sentence."

    doc = nlp(remove_stop_words(case_a))
    doc2 = nlp(remove_stop_words(case_b))

    print(doc.similarity(doc2))


if __name__ == "__main__":
    main()
