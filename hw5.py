import string


def main(filename):import string


def main(filename):
    # read file into lines
    #lines = open('i_have_a_dream.txt').readlines()
    lines = open(filename).readlines()

    all_words = []

    # extract all words from lines
    for line in lines:
        line = line.strip()
        words = line.split()
    
        for word in words:
            word = word.strip(string.punctuation)
            if word:
                all_words.append(word)


    # compute word count from all_words
    from collections import Counter

    word_counter = Counter(all_words)

    #word_counter.most_common() #

    import csv
    csv_file = open('wordcount.csv','w')


    with open('wordcount.csv','w', newline='') as csv_file:
        writer = csv.writer(csv_file)
    
        writer.writerow(['word', 'count'])
    
    #for word, count in word_counter.most_common():
        #writer.writerow(['word', 'count'])
        writer.writerows(word_counter.most_common())
    #微軟的bug

    import json

    json.dump(word_counter.most_common(),open('wordcount.json', 'w'))


    import pickle
    f = open('wordcount.pkl', 'wb')
    #pickle.dump(word_counter.most_common(),open('wordcount.pkl', 'wb'))
    pickle.dump(word_counter.most_common(),f)
    f.close()


    # dump to a csv file named "wordcount.csv":
   
    # dump to a json file named "wordcount.json"
    ...

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")
