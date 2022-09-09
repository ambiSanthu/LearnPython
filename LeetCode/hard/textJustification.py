
def fullJustify(words, maxWidth):
    tmp_word = ""
    output = list()
    
    for word in words:
        len_word = 0
        if tmp_word:
            tmp_word = tmp_word + ' ' + word + ' '
        else:
             tmp_word = word + ' '   
        len_word = len(tmp_word)
        print(len_word)
        if len_word == maxWidth or len_word-1 == maxWidth:
            output.append(tmp_word.rstrip(' '))
            tmp_word = ""
        elif len_word < maxWidth:
            tmp_word = tmp_word + ' '
        else:
            tmp_word_list = tmp_word.strip().split(" ")
            del tmp_word_list[-1]
            output.append(" ".join(tmp_word_list))
            tmp_word = word.rstrip(' ') + " "
        tmp_word = tmp_word.rstrip()
    
    if tmp_word:
        output.append(tmp_word.rstrip(' '))
    count = 0
    count_output = len(output)
    final_output = []
    #print(output)
    for word in output:
        #(word,len(word))
        final_word = ""
        count = count + 1
        less = 0
        if len(word) < maxWidth:
            less = maxWidth - len(word)
        #print(count,count_output)
        if count == count_output:
            final_output.append(output[-1] + " "*less)
            return final_output
            
        word_list = word.split()
        wordlistlen = len(word_list)
        less = less + word.count(" ")
        if wordlistlen == 1:
            final_word = word + " "*less
            final_output.append(final_word)
            continue
            
        spaces = less // (wordlistlen-1)
        extra = less % (wordlistlen-1)
        #(wordlistlen,less,spaces,extra)
        
        
        for i in range(0,wordlistlen):
            if extra:
                final_word = final_word + word_list[i] + (" ")*spaces + " "
                extra = extra - 1
            else:
                final_word = final_word + word_list[i] + (" ")*spaces 
        print(final_word)
        final_output.append(final_word.rstrip())
        print(final_output)
    return final_output


words1 = ["This", "is", "an", "example", "of", "text", "justification."]
n1 = 16
words2 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
n2 = 20
word3 = ["a","b","c","d","e"]
n3 = 3

fullJustify(words1,n1)
fullJustify(words2,n2)
fullJustify(words3,n3)

