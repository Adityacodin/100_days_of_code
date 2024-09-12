# # scope - reach

# weapons = "ak"

# def inc_enemies():
#     enemies = 2
#     print(f"inside func: {enemies}")
#     print(weapons)

# inc_enemies()
# print(weapons)
# print(f"outside func: {enemies}")
# # Variable enemies has a local scope in this example
# # Variable weapons has a global scope in this example

# # global scope function
# def global_func():
#     # local scope function
#     def local_func():
#         pass


level = 3
enemies = [1,2,3]
if level < 5:
    new_enemy = enemies[0]

print(new_enemy)