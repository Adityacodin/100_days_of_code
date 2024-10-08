import turtle
import pandas

scr = turtle.Screen()
ttl = turtle.Turtle()
ttl.penup()
ttl.hideturtle()
scr.title('U.S. States Game')
image = 'blank_states_img.gif'
scr.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0
state_data = pandas.read_csv('50_states.csv')
state_list = state_data.state.to_list() 
# x_list = state_data['x'].to_list()
# y_list = state_data['y'].to_list()
state_buffer = []
count = 0

# ttl.color('green')
# def state_dots():
#     for index in range(len(x_list)):
#         ttl.goto((x_list[index],y_list[index]))
#         ttl.write('*')
#     ttl.color('black')

# def get_coor(xc,yc):
#     for index in range(len(x_list)):
#         if xc >= x_list[index] - 10 or xc <= x_list[index] + 10:
#             if yc >= y_list[index] - 10 or yc <= y_list[index] + 10:
#                 return (x_list[index],y_list[index])
#     return 0

# def get_mouse_click_coor(x,y):
#     coor = get_coor(x,y)
#     print(coor)
#     if x in x_list and y in y_list:
#         stt_nm = state_data[state_data['x'] == x]['state'].values[0]
#         ttl.goto(coor)
#         ttl.write(stt_nm)
#     else :
#         pass

# turtle.onscreenclick(get_mouse_click_coor)
# state_dots()

while game_is_on :
    ip = turtle.textinput("Guess States", "Whats the state's name")
    if ip.lower() == 'exit':
        break
    elif not ip.title() in state_list or ip == None:
        continue
    else:
        state = state_data[state_data['state'] == ip.title()]['state']
        x = state_data[state_data.state == ip.title()]['x']
        y = state_data[state_data.state == ip.title()]['y']
        state_name = state.values[0]
        x_cor = x.values[0]
        y_cor = y.values[0]
        ttl.goto((x_cor,y_cor))
        ttl.write(state_name)
        state_buffer.append(state_name)
        score+=1
        scr.title(f"{score}/50 states correct")
        if score == 50:
            scr.title('50/50 You Win')
            break

learn_state = [state for state in state_list if not state in state_buffer]

dt = pandas.DataFrame({'State':learn_state})
dt.to_csv('states_tolearn.csv')


