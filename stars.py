# Part I
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr):
    for i in arr:
        print "*" * i

draw_stars(x)

# Part II
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(arr):
    for i in arr:
        if isinstance(i, str):
           print i[0].lower() * len(i)
        else:  
            print "*" * i
 
draw_stars(x)