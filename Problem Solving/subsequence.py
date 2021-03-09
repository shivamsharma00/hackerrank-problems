def longpalin(s, k1):
    uniq_alpha = ""
    big_mark = 'b'
    check_mark = 'c'
    big_subseq_s = big_subsequence(s)
    print("biggest subsequence before - "+str(big_subseq_s))
    count_main = 0
    # store unique alphabets
    if k1 == 0:
        uniq_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "w", "x", "y", "z"]
    else:
        uniq_alpha = set(s)
    uniq_count = len(uniq_alpha)
    print("Unique alphabets -"+str(uniq_count))
    # print(big_subseq_s)
    for u in uniq_alpha:

        for r in range(0, (len(s)+1)):
            # print("r-"+str(r))
            new_string = ""
            p_count = 0

            if r == len(s):
                new_string = s+u
            else:
                for new in s:
                    if p_count == r:
                        new_string = new_string + u    
                    new_string = new_string + new
                    p_count = p_count + 1
                    # print("IN COUNT="+str(p_count))
                           
            print("New string - "+str(new_string))
            c = subsequence(s=new_string, k1=k, big_s=big_subseq_s, mark="c")
            print("count of biggest subsequence-"+str(c))
            count_main = count_main + c
            print("add- "+str(count_main))
    print(count_main)




        


def subsequence(s="", k1=0, big_s=0, mark="c"):
    size = len(s)
    palin_count = 0
    # word_len = size-(big_s+k1)
    # for i in range(word_len, size+1):
    i = big_s+k1
    for k in range(0, ((size-i) + 1)):
        word = ""
        palin_word = ""
        for j in range(k, (k+i)):
            word = word + (s[j])
        for alp in word:
            palin_word = alp + palin_word
        # print(str(word)+"--"+str(palin_word))
        if word == palin_word:
            # if len(word)>palin_count:
            palin_count = palin_count+1
    return palin_count
    
def big_subsequence(s):
    size = len(s)
    sub_count = 1
    for i in range(2, size):
        for k in range(0, ((size-i) + 1)):
            word = ""
            palin_word = ""
            for j in range(k, (k+i)):
                word = word + (s[j])
            for alp in word:
                palin_word = alp + palin_word
            # print(str(word)+"--"+str(palin_word))
            if word == palin_word:
                if len(word)>sub_count:
                    sub_count = len(word)
    return sub_count
    


s="aba"
k =0
longpalin(s, k)