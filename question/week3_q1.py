# ---------------------------------------------------------------------
# 
# File          : week3_q1.py  
# Created       : 04/10/2021 18:49
# Authort       : Lukasz S.
# Version       : v1.0.0
# Licencing     : (C) 2021 Lukasz S.
#
# Description   :
# ---------------------------------------------------------------------


if __name__ == '__main__':
    while 1:
        print('Enter number from 0 to 10')
        number = input()
        number = int(number)
        if (number == 3):
            break
        print ('Do you want try again! y/n')
        try_again = input()
        try_again = str(try_again)
        if (try_again == 'n'):
            print ('you lost!')
            quit()

    print ('You win)')

