# def process_svo(question):
#     input_info = 'Ram eats banana.Hari fights lion.Sita eats apple.' \
#                  'Gita shoots lion.Ramesh throws laptop.Ram smashes banana.' \
#                  'Basanta eats banana.Ram eats apple.Hari hits Gita.Hari falls.'

#     input_info = input_info[:-1]
#     list_of_SV_sentences = input_info.split(".")
#     broken_list_of_SV_sentences = []
#     for sentence in list_of_SV_sentences:
#         word_list = sentence.split(" ")
#         broken_list_of_SV_sentences.append(word_list)

#     dict_of_relation = {}
#     for sentence in broken_list_of_SV_sentences:
#         for word in sentence:
#             sentence_index = broken_list_of_SV_sentences.index(sentence)
#             if word in dict_of_relation.keys():
#                 if sentence_index not in dict_of_relation[word]:
#                     dict_of_relation[word].append(sentence_index)
#             else:
#                 dict_of_relation[word] = [sentence_index]

#     question = question[:-1]
#     question_word_list = question.split(" ")
#     question_word_list.extend(["", "", "", ""])
#     result = []

#     if question_word_list[0] == "Explain" and question_word_list[1] == "all" and question_word_list[2] == "occuring":
#         for index in dict_of_relation.get(question_word_list[3], []):
#             # print(list_of_SV_sentences[index])
#             result.append(list_of_SV_sentences[index])

#     elif question_word_list[0] == "What" and question_word_list[1] == "is" and question_word_list[2] == "done" and question_word_list[3] == "to":
#         for index in dict_of_relation.get(question_word_list[4], []):
#             # print(list_of_SV_sentences[index])
#             result.append(list_of_SV_sentences[index])

#     elif question_word_list[0] == "What" and question_word_list[1] == "does" and question_word_list[3] == "do" and question_word_list[4] == "to":
#         sentences_with_both = list(set(dict_of_relation.get(question_word_list[2], [])) & set(dict_of_relation.get(question_word_list[5], [])))
#         for sentence_index in sentences_with_both:
#             if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2]:
#                 # print(list_of_SV_sentences[sentence_index])
#                 result.append(list_of_SV_sentences[sentence_index])

#     elif question_word_list[0] == "What" and question_word_list[1] == "does" and question_word_list[3] == "do":
#         for index in dict_of_relation.get(question_word_list[2], []):
#             # print(list_of_SV_sentences[index])
#             result.append(list_of_SV_sentences[index])

#     elif (question_word_list[0] == "What" or question_word_list[0] == "Who") and question_word_list[1] == "does":
#         sentences_with_both = list(set(dict_of_relation.get(question_word_list[2], [])) & set(dict_of_relation.get(question_word_list[3], [])))
#         for sentence_index in sentences_with_both:
#             if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2]:
#                 # print(list_of_SV_sentences[sentence_index])
#                 result.append(list_of_SV_sentences[sentence_index])

#     elif (question_word_list[0] == "What" or question_word_list[0] == "Who") and question_word_list[1] == "is" and (
#         question_word_list[2][-2:] == "ed" or question_word_list[2][-2:] == "en" or question_word_list[2][-1] == "t"):
#         if question_word_list[2][-2:] == "ed":
#             verb = question_word_list[2][:-2]
#         elif question_word_list[2][-2:] == "en":
#             verb = question_word_list[2][:-2]
#         else:
#             verb = question_word_list[2]
#         for index in dict_of_relation.get(verb + "s", []):
#             # print(broken_list_of_SV_sentences[index][2])
#             result.append(broken_list_of_SV_sentences[index][2])

#     else:
#         for index in dict_of_relation.get(question_word_list[1], []):
#             # print(broken_list_of_SV_sentences[index][0])
#             result.append(broken_list_of_SV_sentences[index][0])

#     return result

def process_svo(question):
    input_info = 'Ram eats banana.Hari fights lion.Sita eats apple.' \
                 'Gita shoots lion.Ramesh throws laptop.Ram smashes banana.' \
                 'Basanta eats banana.Ram eats apple.Hari hits Gita.Hari falls.'

    input_info = input_info.rstrip(".")
    list_of_SV_sentences = input_info.split(".")
    
    broken_list_of_SV_sentences = [sentence.split(" ") for sentence in list_of_SV_sentences]

    # Create lowercase version of all words for matching
    dict_of_relation = {}
    for idx, sentence in enumerate(broken_list_of_SV_sentences):
        for word in sentence:
            word_lower = word.lower()
            dict_of_relation.setdefault(word_lower, []).append(idx)

    # Prepare the question
    question = question.strip().rstrip("?")
    question_word_list = question.split(" ")
    question_word_list = [w.lower() for w in question_word_list]
    question_word_list.extend([""] * (10 - len(question_word_list)))  # ensure at least 10 elements


    result = []

    # Pattern 1: Explain all occuring X
    if question_word_list[0] == "explain" and question_word_list[1] == "all" and question_word_list[2] == "occuring":
        result.extend([list_of_SV_sentences[i] for i in dict_of_relation.get(question_word_list[3], [])])

    # Pattern 2: What is done to X
    elif question_word_list[0] == "what" and question_word_list[1] == "is" and question_word_list[2] == "done" and question_word_list[3] == "to":
        result.extend([list_of_SV_sentences[i] for i in dict_of_relation.get(question_word_list[4], [])])

    # Pattern 3: What does X do to Y
    elif question_word_list[0] == "what" and question_word_list[1] == "does" and question_word_list[3] == "do" and question_word_list[4] == "to":
        s_indices = dict_of_relation.get(question_word_list[2], [])
        o_indices = dict_of_relation.get(question_word_list[5], [])
        common_indices = set(s_indices) & set(o_indices)
        for i in common_indices:
            if broken_list_of_SV_sentences[i][0].lower() == question_word_list[2]:
                result.append(list_of_SV_sentences[i])

    # Pattern 4: What does X do
    elif question_word_list[0] == "what" and question_word_list[1] == "does" and question_word_list[3] == "do":
        result.extend([list_of_SV_sentences[i] for i in dict_of_relation.get(question_word_list[2], [])])

    # Pattern 5: What/Who does X Y
    elif (question_word_list[0] == "what" or question_word_list[0] == "who") and question_word_list[1] == "does":
        s_indices = dict_of_relation.get(question_word_list[2], [])
        v_indices = dict_of_relation.get(question_word_list[3], [])
        common_indices = set(s_indices) & set(v_indices)
        for i in common_indices:
            if broken_list_of_SV_sentences[i][0].lower() == question_word_list[2]:
                result.append(list_of_SV_sentences[i])

    # Pattern 6: What/Who is VERBed (passive)
    elif (question_word_list[0] == "what" or question_word_list[0] == "who") and question_word_list[1] == "is" and (
        question_word_list[2].endswith("ed") or question_word_list[2].endswith("en") or question_word_list[2].endswith("t")):
        verb_stem = question_word_list[2]
        if verb_stem.endswith("ed") or verb_stem.endswith("en"):
            verb_stem = verb_stem[:-2]
        elif verb_stem.endswith("t"):
            verb_stem = verb_stem[:-1]
        results = dict_of_relation.get(verb_stem + "s", [])
        for i in results:
            result.append(broken_list_of_SV_sentences[i][2])

    # Fallback: use second word as key
    else:
        result.extend([broken_list_of_SV_sentences[i][0] for i in dict_of_relation.get(question_word_list[1], [])])

    return result
