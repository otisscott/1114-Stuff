respellings = {
    "teh": "the",
    "relevent": "relevant",
    "lite": "light",
    "lol": "haha"
}


def respell(sentence):
    """
    sig: str -> str
    This function takes a string and corrects commonly misspelled words in it from a dict
    """
    word_list = sentence.split(" ")
    for word in range(len(word_list)):
        if word_list[word] in respellings:
            word_list[word] = respellings[word_list[word]]
    final = " ".join(word_list)
    return final


def word_positions(sentence):
    """
    sig:  str -> dict (str, list (int))
    This function takes a sentence and returns a dict containing each word in the sentence with the position(s) in which it occurs
    """
    word_list = sentence.split(" ")
    positions = {}
    for word in range(len(word_list)):
        if word_list[word] in positions:
            positions[word_list[word]].append(word)
        else:
            positions[word_list[word]] = [word]
    return positions


def commonest(positions):
    """
    sig: dict(str, list(int)) -> str
    This function takes a dict containing words and lists of where the words occur in a sentence and returns the most common word
    """
    most_common = ""
    count = 0
    for word in positions:
        if len(positions[word]) > count:
            most_common = word
            count = len(positions[most_common])
    return most_common


def main():
    """
    sig: None -> None
    This function is used to test the other functions in the file
    """
    bad_sentence = "I ate teh whole thing lol and it was really tasty lol"
    good_sentence = respell(bad_sentence)
    print(good_sentence)
    position_tester = "'It was the best of times it was the worst of times"
    print(word_positions(good_sentence))
    print(word_positions(position_tester))
    print(commonest(word_positions("He thought a thought he'd never thought before")))


main()
