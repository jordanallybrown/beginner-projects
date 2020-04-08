''''
Author: Jordan (jordanallybrown)
Problem: 99 Bottles, print out all the lyrics of 99 bottles of beer on the wall

e.g.
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.

'''

def ninetyNineBottles(n=99):
    '''
    Prints out the lyrics of the song "99 bottles of beer on the wall", with the number
     of bottles being variable

    :param n: number of bottles to begin count down in song
    :return: prints out the lyrics starting from n to 0
    '''
    bottlesLyric = "%s %s of beer"
    totalBottles = n
    while n >= 0:
        if n == 0:
            lyric = bottlesLyric % (totalBottles, "bottles")
            print("No more bottles of beer on the wall, no more bottles of beer.\n"
                  "Go to the store and buy some more, %s on the wall.\n" % lyric)
        else:
            if n == 1:
                lyric = bottlesLyric % (n, "bottle")
            else:
                lyric = bottlesLyric % (n, "bottles")
            print("%s on the wall, %s.\nTake one down and pass it around, %s on the wall." % ((lyric,)*3))
        n -= 1


def main():
    ninetyNineBottles()


main()