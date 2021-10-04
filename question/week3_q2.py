# ---------------------------------------------------------------------
#
# File          : ${NAME}.py
# Created       : ${DATE} ${TIME}
# Authort       : Lukasz S.
# Version       : v1.0.0
# Licencing     : (C) 2021 Lukasz S.
#
# Description   : Week 3 question 2
# ---------------------------------------------------------------------

book_1 = "The Godfather - Mario Puzo"
book_2 = "The Sicilian - Mario Puzo"
book_3 = "The Last Don - - Mario Puzo"
book_4 = "The Storyteller - Dave Grohl"
book_5 = "And Awaye - Bob Mortimer"

price_book_1 = 6.99
price_book_2 = 9.99
price_book_3 = 5.25
price_book_4 = 6.75
price_book_5 = 8.95


print("{0:<32} {1:6}".format("Title", "Price"))
print("")
print("{0:<30} {1:6.2f}".format(book_1, price_book_1))
print("{0:<30} {1:6.2f}".format(book_2, price_book_2))
print("{0:<30} {1:6.2f}".format(book_3, price_book_3))
print("{0:<30} {1:6.2f}".format(book_4, price_book_4))
print("{0:<30} {1:6.2f}".format(book_5, price_book_5))
print("_"*37)
print("{0:<30} {1:6.2f}".format("Total", float(price_book_1)+float(price_book_2)+float(price_book_3)+float(price_book_4)+float(price_book_5)))