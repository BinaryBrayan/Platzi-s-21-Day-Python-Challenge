def triangle(size,character):
    spaces=' '
    repet=1
    for x in range(size):
       print(spaces*(size-(x+1)),character*(repet),spaces*(size-(x+1)))
       repet+=2

triangle(3,'*')