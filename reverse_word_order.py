def reverse_word_order(n):
    a = n.split()
    return a[::-1]

if __name__ == "__main__":
    n = input('enter the text you want to reverse:')
    print(reverse_word_order(n))