def star (one):
    i=one
    for x in range(i):
        space=("_"*(x))
        num_stars = "*"*(2*(i-x)-1)
        print(space+num_stars)
star (17)
print()
star(5)


#