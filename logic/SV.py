def process_sv(question="What does Sita do?"):
    input_info = "Snigdh eats.Ram eats.Snigdh sits.Sita falls."
    input_info = input_info[:-1]  # Remove last full stop
    list_of_SV_sentences = input_info.split(".")
    Subject_list = ["Snigdh", "Ram", "Sita"]
    Verb_list = ["eats", "sits", "falls"]
    broken_list_of_SV_sentences = []

    for sentence in list_of_SV_sentences:
        word_list = sentence.split(" ")
        broken_list_of_SV_sentences.append(word_list)

    dict_of_relation = {}
    for idx, sentence in enumerate(broken_list_of_SV_sentences):
        for word in sentence:
            if word in dict_of_relation:
                if idx not in dict_of_relation[word]:
                    dict_of_relation[word].append(idx)
            else:
                dict_of_relation[word] = [idx]

    question = question[:-1]  # Remove question mark
    question_word_list = question.split(" ")

    # Normalize case for subject matching
    Subject_list_lower = [s.lower() for s in Subject_list]
    question_subject = question_word_list[2].lower()

    results = []
    if (question_word_list[0].lower() == "what" and
        question_word_list[1].lower() == "does" and
        question_subject in Subject_list_lower and
        question_word_list[3].lower() == "do"):

        # Get original subject with proper case to use as key in dict_of_relation
        # because dict_of_relation keys have case-sensitive words from input_info
        # So find original Subject_list item matching lower case
        original_subject = Subject_list[Subject_list_lower.index(question_subject)]

        for index in dict_of_relation.get(original_subject, []):
            results.append(broken_list_of_SV_sentences[index][1])

    if not results:
        results = ["No matching sentence found."]

    print(f"{results=}")
    return results
