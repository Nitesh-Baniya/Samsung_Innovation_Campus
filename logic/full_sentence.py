from sortedcontainers import SortedSet

# A+S+Ad+V+A+Osentences

def process_full_sentences(question):

    input_info = 'Ram eats banana.Hari fights lion.Sita eats apple.\
    Gita shoots lion.Ramesh throws laptop.Ram smashes banana.\
    Basanta eats banana.Ram eats apple.Hari hits Gita.Hari falls.\
    Fat Hari fights tiger.Small Hari eats carrot.Scary Tom beats chicken.\
    Ramesh furiously throws towel.Hari lightly hits Gita.\
    Magnus quickly wins Hari.Sagar kicks large house.\
    Basanta eats big banana.Quick Gita slowly eats apple.Ram happily eats fresh apple.\
    Ram disgustingly smashes rotten banana.Fat Hari slowly eats big carrot.\
    Slow Tom sadly writes stupid poem.Large Tom disgustingly smashes small house.\
    Large Tom hits quick Gita.'

    adjective_list= SortedSet(["fat","small","scary","large","big","quick","fresh","rotten","slow","stupid"]) #changed
    input_info = input_info[:-1]

    list_of_SV_sentences= input_info.split(".")
    broken_list_of_SV_sentences = []

    for sentence in list_of_SV_sentences:
        word_list = sentence.split(" ")
        if word_list[0].lower() in adjective_list:
            word_list[0] = word_list[0].lower()
        broken_list_of_SV_sentences.append(word_list)
        
    # print(f"{broken_list_of_SV_sentences =}")
    dict_of_relation = {}
    for sentence in broken_list_of_SV_sentences:
        for word in sentence:
            sentence_index = broken_list_of_SV_sentences.index(sentence)
            if word in dict_of_relation.keys():
                if sentence_index not in dict_of_relation[word]:
                    dict_of_relation[word].add(sentence_index)  #changed
            else:
                dict_of_relation[word] = {sentence_index} #changed
        subject_adj_flag = 0
        object_adj_flag = 0
        if sentence[0] in adjective_list:
            subject_adj_flag = 1
            compound_word = sentence[0]+" "+sentence[1]
            if compound_word in dict_of_relation.keys():
                if sentence_index not in dict_of_relation[compound_word]:
                    dict_of_relation[compound_word].add(sentence_index)  #changed
            else:
                dict_of_relation[compound_word] = {sentence_index}  #changed
        if sentence[-2] in adjective_list:
            object_adj_flag = 1
            compound_word = sentence[-2]+" "+sentence[-1]
            if compound_word in dict_of_relation.keys():
                if sentence_index not in dict_of_relation[compound_word]:
                    dict_of_relation[compound_word].add(sentence_index)   #changed
            else:
                dict_of_relation[compound_word] = {sentence_index}  #changed
        if len(sentence)-subject_adj_flag-object_adj_flag==4:
            compound_word = sentence[1+subject_adj_flag]+" "+sentence[2+subject_adj_flag]
            if compound_word in dict_of_relation.keys():
                if sentence_index not in dict_of_relation[compound_word]:
                    dict_of_relation[compound_word].add(sentence_index)  #changed
            else:
                dict_of_relation[compound_word] = {sentence_index}  #changed
    # print(dict_of_relation)


    # question = "What is done to Gita?"
    question = question[:-1]
    question_word_list = question.split(" ")
    question_word_list.extend(["","","","","","","","","","",""])

    results = []

    if question_word_list[0] == "Explain" and question_word_list[1] == "all" and question_word_list[2] == "occuring":
        if question_word_list[4] == "":
            for index in dict_of_relation[question_word_list[3]]:
                # print(list_of_SV_sentences[index])
                results.append(list_of_SV_sentences[index])
        else:
            for index in dict_of_relation[question_word_list[3]+" "+question_word_list[4]]:
                # print(list_of_SV_sentences[index])
                results.append(list_of_SV_sentences[index])


    elif question_word_list[0] == "What" and question_word_list[1]=="is" and question_word_list[2] == "done" and question_word_list[3] =="to":
        if question_word_list[5] == "":
            for index in dict_of_relation[question_word_list[4]]:
                if broken_list_of_SV_sentences[index][-1] == question_word_list[4]:
                    # print(list_of_SV_sentences[index])
                    results.append(list_of_SV_sentences[index])
        else:
            for index in dict_of_relation[question_word_list[4]+" "+question_word_list[5]]:
                if broken_list_of_SV_sentences[index][-1] == question_word_list[5]:
                    # print(list_of_SV_sentences[index])
                    results.append(list_of_SV_sentences[index])

    elif question_word_list[0] == "What" and question_word_list[1] =="does" and ((question_word_list[3] =="do" and question_word_list[4] =="to") or (question_word_list[4] == "do" and question_word_list[5] == "to")):
        if question_word_list[3] == "do" and question_word_list[6] == "":
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]]) & set(dict_of_relation[question_word_list[5]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] or broken_list_of_SV_sentences[sentence_index][1] == question_word_list[2]:
                    # print(list_of_SV_sentences[sentence_index])
                    results.append(list_of_SV_sentences[sentence_index])

        elif question_word_list[3] == "do":
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]]) & set(dict_of_relation[question_word_list[5]+" "+question_word_list[6]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] or broken_list_of_SV_sentences[sentence_index][1] == question_word_list[2]:
                    print(list_of_SV_sentences[sentence_index])
        elif question_word_list[4] == "do" and question_word_list[7] == "":
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]+" "+question_word_list[3]]) & set(dict_of_relation[question_word_list[6]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] and broken_list_of_SV_sentences[sentence_index][1] == question_word_list[3]:
                    # print(list_of_SV_sentences[sentence_index])
                        results.append(list_of_SV_sentences[sentence_index])

        else:
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]+" "+question_word_list[3]]) & set(dict_of_relation[question_word_list[6]+" "+question_word_list[7]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] and broken_list_of_SV_sentences[sentence_index][1] == question_word_list[3]:
                    # print(list_of_SV_sentences[sentence_index])
                        results.append(list_of_SV_sentences[sentence_index])
            
    elif question_word_list[0] == "What" and question_word_list[1] == "does" and (question_word_list[3] == "do" or question_word_list[4]== "do"):
        if question_word_list[3] == "do":
            for index in dict_of_relation[question_word_list[2]]:
                if broken_list_of_SV_sentences[index][0] == question_word_list[2] or broken_list_of_SV_sentences[index][1] == question_word_list[2]:
                    # print(list_of_SV_sentences[index])
                    results.append(list_of_SV_sentences[index])
                    
        else:
            for index in dict_of_relation[question_word_list[2]+" "+question_word_list[3]]:
                if broken_list_of_SV_sentences[index][0] == question_word_list[2] and broken_list_of_SV_sentences[index][1] == question_word_list[3]:
                    # print(list_of_SV_sentences[index])
                    results.append(list_of_SV_sentences[index])

    elif (question_word_list[0] == "What" or question_word_list[0] == "Who") and question_word_list[1] == "does":
        if question_word_list[4] == "":
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]]) & set(dict_of_relation[question_word_list[3]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] or broken_list_of_SV_sentences[sentence_index][1] == question_word_list[2]:
                    # print(list_of_SV_sentences[sentence_index])
                    results.append(list_of_SV_sentences[sentence_index])

        elif question_word_list[2] in adjective_list and question_word_list[5] == "":
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]+" "+question_word_list[3]]) & set(dict_of_relation[question_word_list[4]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] and broken_list_of_SV_sentences[sentence_index][1] == question_word_list[3]:
                    # print(list_of_SV_sentences[sentence_index])
                    results.append(list_of_SV_sentences[sentence_index])

        elif question_word_list[5] == "":
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]]) & set(dict_of_relation[question_word_list[3]+" "+ question_word_list[4]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] or broken_list_of_SV_sentences[sentence_index][1] == question_word_list[2]:
                    # print(list_of_SV_sentences[sentence_index])
                    results.append(list_of_SV_sentences[sentence_index])
                    
        else:
            sentences_with_both = list(set(dict_of_relation[question_word_list[2]+" "+question_word_list[3]]) & set(dict_of_relation[question_word_list[4]+" "+ question_word_list[5]]))
            for sentence_index in sentences_with_both:
                if broken_list_of_SV_sentences[sentence_index][0] == question_word_list[2] and broken_list_of_SV_sentences[sentence_index][1] == question_word_list[3]:
                    # print(list_of_SV_sentences[sentence_index])
                    results.append(list_of_SV_sentences[sentence_index])
        

    elif (question_word_list[0] == "What" or question_word_list[0] == "Who") and question_word_list[1] == "is": 
        if question_word_list[3] != "":
            for index in dict_of_relation[question_word_list[2]+" "+question_word_list[3]]:
                if broken_list_of_SV_sentences[index][-2] in adjective_list:
                    # print(broken_list_of_SV_sentences[index][-2]+" "+broken_list_of_SV_sentences[index][-1])
                    results.append(broken_list_of_SV_sentences[index][-2]+" "+broken_list_of_SV_sentences[index][-1])
                else:
                    # print(broken_list_of_SV_sentences[index][-1])
                    results.append(broken_list_of_SV_sentences[index][-1])

        else:
            for index in dict_of_relation[question_word_list[2]]:
                if broken_list_of_SV_sentences[index][-2] in adjective_list:
                    # print(broken_list_of_SV_sentences[index][-2]+" "+broken_list_of_SV_sentences[index][-1])
                    results.append(broken_list_of_SV_sentences[index][-2]+" "+broken_list_of_SV_sentences[index][-1])
                else:
                    # print(broken_list_of_SV_sentences[index][-1])
                    results.append(broken_list_of_SV_sentences[index][-1])

    else:
        if not(question_word_list[1][-2:] == "ly"):
            if question_word_list[2] == "":
                for index in dict_of_relation[question_word_list[1]]:
                    if broken_list_of_SV_sentences[index][0] in adjective_list:
                        # print(broken_list_of_SV_sentences[index][0]+" "+broken_list_of_SV_sentences[index][1])
                        results.append(broken_list_of_SV_sentences[index][0]+" "+broken_list_of_SV_sentences[index][1])
                    else:
                        # print(broken_list_of_SV_sentences[index][0])
                        results.append(broken_list_of_SV_sentences[index][0])
            else:
                if question_word_list[3] == "":
                    sentences_with_both = list(set(dict_of_relation[question_word_list[1]]) & set(dict_of_relation[question_word_list[2]]))
                    for index in sentences_with_both:
                        # print(list_of_SV_sentences[index])
                        results.append(list_of_SV_sentences[index])
                else:
                    sentences_with_both = list(set(dict_of_relation[question_word_list[1]]) & set(dict_of_relation[question_word_list[2] + " " + question_word_list[3]]))
                    for index in sentences_with_both:
                        # print(list_of_SV_sentences[index])
                        results.append(list_of_SV_sentences[index])
                
    
        else:
            if question_word_list[3] == "":
                for index in dict_of_relation[question_word_list[1]+ " "+question_word_list[2]]:
                    if broken_list_of_SV_sentences[index][0] in adjective_list:
                        # print(broken_list_of_SV_sentences[index][0]+" "+broken_list_of_SV_sentences[index][1])
                        results.append(broken_list_of_SV_sentences[index][0]+" "+broken_list_of_SV_sentences[index][1])
                    else:
                        # print(broken_list_of_SV_sentences[index][0])
                        results.append(broken_list_of_SV_sentences[index][0])
            else:
                if question_word_list[4] == "":
                    sentences_with_both = list(set(dict_of_relation[question_word_list[1] + " "+ question_word_list[2]]) & set(dict_of_relation[question_word_list[3]]))
                    for index in sentences_with_both:
                        # print(list_of_SV_sentences[index])
                        results.append(list_of_SV_sentences[index])
                else:
                    sentences_with_both = list(set(dict_of_relation[question_word_list[1] + " " + question_word_list[2]]) & set(dict_of_relation[question_word_list[3] + " " + question_word_list[4]]))
                    for index in sentences_with_both:
                        # print(list_of_SV_sentences[index])
                        results.append(list_of_SV_sentences[index])
                        
    return results

# from sortedcontainers import SortedSet

# def process_full_sentences(question):
#     input_info = (
#         'Ram eats banana.Hari fights lion.Sita eats apple.'
#         'Gita shoots lion.Ramesh throws laptop.Ram smashes banana.'
#         'Basanta eats banana.Ram eats apple.Hari hits Gita.Hari falls.'
#         'Fat Hari fights tiger.Small Hari eats carrot.Scary Tom beats chicken.'
#         'Ramesh furiously throws towel.Hari lightly hits Gita.'
#         'Magnus quickly wins Hari.Sagar kicks large house.'
#         'Basanta eats big banana.Quick Gita slowly eats apple.Ram happily eats fresh apple.'
#         'Ram disgustingly smashes rotten banana.Fat Hari slowly eats big carrot.'
#         'Slow Tom sadly writes stupid poem.Large Tom disgustingly smashes small house.'
#         'Large Tom hits quick Gita.'
#     )

#     adjective_list = SortedSet(["fat", "small", "scary", "large", "big", "quick", "fresh", "rotten", "slow", "stupid"])

#     input_info = input_info.strip(".")
#     list_of_SV_sentences = input_info.split(".")
#     broken_list_of_SV_sentences = []

#     for sentence in list_of_SV_sentences:
#         word_list = sentence.split(" ")
#         if word_list[0].lower() in adjective_list:
#             word_list[0] = word_list[0].lower()
#         broken_list_of_SV_sentences.append(word_list)

#     dict_of_relation = {}

#     for sentence_index, sentence in enumerate(broken_list_of_SV_sentences):
#         for word in sentence:
#             dict_of_relation.setdefault(word, set()).add(sentence_index)

#         subject_adj_flag = 0
#         object_adj_flag = 0

#         # Subject Adjective
#         if sentence[0] in adjective_list:
#             subject_adj_flag = 1
#             compound_word = sentence[0] + " " + sentence[1]
#             dict_of_relation.setdefault(compound_word, set()).add(sentence_index)

#         # Object Adjective
#         if sentence[-2] in adjective_list:
#             object_adj_flag = 1
#             compound_word = sentence[-2] + " " + sentence[-1]
#             dict_of_relation.setdefault(compound_word, set()).add(sentence_index)

#         # Adverb + Verb
#         if len(sentence) - subject_adj_flag - object_adj_flag == 4:
#             compound_word = sentence[1 + subject_adj_flag] + " " + sentence[2 + subject_adj_flag]
#             dict_of_relation.setdefault(compound_word, set()).add(sentence_index)

#     # Process Question
#     question = question.strip("?")
#     question_word_list = question.split(" ")
#     question_word_list.extend([""] * 10)
#     results = []

#     def fetch_sentences(indices):
#         return [list_of_SV_sentences[i] for i in sorted(indices)]

#     if question_word_list[0] == "Explain" and question_word_list[1] == "all" and question_word_list[2] == "occuring":
#         key = question_word_list[3] + (" " + question_word_list[4] if question_word_list[4] else "")
#         results = fetch_sentences(dict_of_relation.get(key, []))

#     elif question_word_list[:4] == ["What", "is", "done", "to"]:
#         key = question_word_list[4] + (" " + question_word_list[5] if question_word_list[5] else "")
#         indices = dict_of_relation.get(key, [])
#         for i in indices:
#             if broken_list_of_SV_sentences[i][-1] in key:
#                 results.append(list_of_SV_sentences[i])

#     elif question_word_list[0] == "What" and question_word_list[1] == "does" and "do" in question_word_list:
#         subj = question_word_list[2]
#         if question_word_list[3] == "do":
#             obj_key = question_word_list[5] + (" " + question_word_list[6] if question_word_list[6] else "")
#         else:
#             subj = question_word_list[2] + " " + question_word_list[3]
#             obj_key = question_word_list[6] + (" " + question_word_list[7] if question_word_list[7] else "")

#         indices = set(dict_of_relation.get(subj, [])) & set(dict_of_relation.get(obj_key, []))
#         for i in indices:
#             if " ".join(broken_list_of_SV_sentences[i][:2]) == subj or broken_list_of_SV_sentences[i][0] == subj:
#                 results.append(list_of_SV_sentences[i])

#     elif question_word_list[:2] == ["What", "does"] and "do" in question_word_list:
#         subj_key = question_word_list[2] + (" " + question_word_list[3] if question_word_list[3] != "do" else "")
#         indices = dict_of_relation.get(subj_key, [])
#         for i in indices:
#             if " ".join(broken_list_of_SV_sentences[i][:2]) == subj_key or broken_list_of_SV_sentences[i][0] == question_word_list[2]:
#                 results.append(list_of_SV_sentences[i])

#     elif question_word_list[0] in ["What", "Who"] and question_word_list[1] == "does":
#         subj = question_word_list[2]
#         obj = question_word_list[3] + (" " + question_word_list[4] if question_word_list[4] else "")

#         if question_word_list[2] in adjective_list:
#             subj = question_word_list[2] + " " + question_word_list[3]
#             obj = question_word_list[4] + (" " + question_word_list[5] if question_word_list[5] else "")

#         indices = set(dict_of_relation.get(subj, [])) & set(dict_of_relation.get(obj, []))
#         for i in indices:
#             if " ".join(broken_list_of_SV_sentences[i][:2]) == subj or broken_list_of_SV_sentences[i][0] == subj:
#                 results.append(list_of_SV_sentences[i])

#     elif question_word_list[0] in ["What", "Who"] and question_word_list[1] == "is":
#         key = question_word_list[2] + (" " + question_word_list[3] if question_word_list[3] else "")
#         indices = dict_of_relation.get(key, [])
#         for i in indices:
#             last_two = broken_list_of_SV_sentences[i][-2:]
#             if last_two[0] in adjective_list:
#                 results.append(" ".join(last_two))
#             else:
#                 results.append(last_two[-1])

#     return results
