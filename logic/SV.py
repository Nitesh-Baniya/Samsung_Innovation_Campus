def process_sv(question="What does Sita do?"):
    input_info = "Snigdh eats.Ram eats.Snigdh sits.Sita falls."
    input_info = input_info.rstrip(".")  # Remove last full stop
    list_of_SV_sentences = input_info.split(".")
    Verb_list = ["eats", "sits", "falls"]
    Subject_list = ["Snigdh", "Ram", "Sita"]

    broken_sentences = [sentence.split(" ") for sentence in list_of_SV_sentences]

    # Build a relation dict with original casing
    relation_dict = {}
    for idx, words in enumerate(broken_sentences):
        for word in words:
            relation_dict.setdefault(word, []).append(idx)

    # Process question
    question = question.strip().rstrip("?")
    question_words = question.split(" ")

    # Normalize subject case
    Subject_list_lower = [s.lower() for s in Subject_list]
    if len(question_words) != 4:
        return ["Invalid question format."]

    q_word, q_aux, q_subject_raw, q_verb = [w.lower() for w in question_words]
    q_subject = q_subject_raw.lower()

    results = []

    if q_word == "what" and q_aux == "does" and q_verb == "do" and q_subject in Subject_list_lower:
        original_subject = Subject_list[Subject_list_lower.index(q_subject)]
        for idx in relation_dict.get(original_subject, []):
            results.append(broken_sentences[idx][1])

    if not results:
        results = ["No matching sentence found."]

    return results
