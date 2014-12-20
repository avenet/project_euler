from num2word_EN import to_card

result = 0

for n in xrange(1,1001):
    number_word = to_card(n)
    print number_word
    result += len([x for x in number_word if x.isalpha()])

print result