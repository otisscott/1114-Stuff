def remove_all(xs, elem):
    """
    :param xs:
    :param elem:
    :return:
    """
    for each in xs:
        if each == elem:
            xs.remove(each)
    print(xs)


def main():
    remove_all(["this", "that", "thy", "tho", "they"], "that")


main()
