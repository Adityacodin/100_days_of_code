import colorgram

colors = colorgram.extract("C:/Users/33333333333333333333/100_days_ofcode/day_18/hirst_painting/spots.jpg",35)
c_list = []
for color in colors:
    r_g_b = color.rgb
    c_list.append((r_g_b.r,r_g_b.g,r_g_b.b))
print(c_list)
print(len(c_list))