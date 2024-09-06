import random
import hm_resource
print(hm_resource.logo)
print("\n")
selected_word = random.choice(hm_resource.word_list)

# print(selected_word)

ans = []
for i in range(0,len(selected_word)):
    print("_",end = '')
    ans.append("_")
print("  ", len(ans))

i = 0
while "_" in ans :
    print(f"*************** {i}/6 lives left ***************")
    user_letter = input("\nGuess a letter : ").strip().lower()
    correct = False
    for j in range(0,len(selected_word)):
        if selected_word[j] == user_letter and ans[j] != user_letter:
            ans[j] = user_letter
            correct = True
            break
    if not correct:
        i+=1
    print(hm_resource.stages[i])

    for el in ans:
        print(el,end="")
    print("\n")

    if i == len(hm_resource.stages)-1:
        print("\nGAME OVER")
        break
    elif "_" not in ans:
        print("\nYOU WIN")

print(f"The correct word was : {selected_word}")


    