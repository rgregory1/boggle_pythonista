import ui
from random import randint
import time
import random
import json

w,h = ui.get_screen_size()
view = ui.View(bg_color='#0D76A8', frame=(0,0,w,h))

def run_async(func):
   from threading import Thread
   from functools import wraps

   @wraps(func)
   def async_func(*args, **kwargs):
      func_hl = Thread(target = func, args = args, kwargs = kwargs)
      func_hl.start()
      return func_hl

   return async_func

dice = {0: ['A', 'A', 'E', 'E', 'G', 'N'],
        1: ['E', 'L', 'R', 'T', 'T', 'Y'],
        2: ['A', 'O', 'O', 'T', 'T', 'W'],
        3: ['A', 'B', 'B', 'J', 'O', 'O'],
        4: ['E', 'H', 'R', 'T', 'V', 'W'],
        5: ['C', 'I', 'M', 'O', 'T', 'U'],
        6: ['D', 'I', 'S', 'T', 'T', 'Y'],
        7: ['E', 'I', 'O', 'S', 'S', 'T'],
        8: ['D', 'E', 'L', 'R', 'V', 'Y'],
        9: ['A', 'C', 'H', 'O', 'P', 'S'],
        10: ['H', 'I', 'M', 'N', 'Q', 'U'],
        11: ['E', 'E', 'I', 'N', 'S', 'U'],
        12: ['E', 'E', 'G', 'H', 'N', 'W'],
        13: ['A', 'F', 'F', 'K', 'P', 'S'],
        14: ['H', 'L', 'N', 'N', 'R', 'Z'],
        15: ['D', 'E', 'I', 'L', 'R', 'X']}

def roll_all_dice(dice):
    dice_rolls = []
    for die in dice:
        this_roll = randint(0,5)
        the_letter = dice[die][this_roll]
        dice_rolls.append(the_letter)
    random.shuffle(dice_rolls)
    return dice_rolls


def button_press(self):
	print('button was pressed')
	self.title = "Play Game"
	dice_rolls = roll_all_dice(dice)
	label1.text = str(dice_rolls[0])
	label2.text = str(dice_rolls[1])
	label3.text = str(dice_rolls[2])
	label4.text = str(dice_rolls[3])
	label5.text = str(dice_rolls[4])
	label6.text = str(dice_rolls[5])
	label7.text = str(dice_rolls[6])
	label8.text = str(dice_rolls[7])
	label9.text = str(dice_rolls[8])
	label10.text = str(dice_rolls[9])
	label11.text = str(dice_rolls[10])
	label12.text = str(dice_rolls[11])
	label13.text = str(dice_rolls[12])
	label14.text = str(dice_rolls[13])
	label15.text = str(dice_rolls[14])
	label16.text = str(dice_rolls[15])
	with open('dice_rolls.json', 'w') as f:
		json.dump(dice_rolls, f)
	countdown()
	main_button.action = show_letters


def show_letters(self):
	with open('dice_rolls.json') as f:
		dice_rolls = json.load(f)
	label1.text = str(dice_rolls[0])
	label2.text = str(dice_rolls[1])
	label3.text = str(dice_rolls[2])
	label4.text = str(dice_rolls[3])
	label5.text = str(dice_rolls[4])
	label6.text = str(dice_rolls[5])
	label7.text = str(dice_rolls[6])
	label8.text = str(dice_rolls[7])
	label9.text = str(dice_rolls[8])
	label10.text = str(dice_rolls[9])
	label11.text = str(dice_rolls[10])
	label12.text = str(dice_rolls[11])
	label13.text = str(dice_rolls[12])
	label14.text = str(dice_rolls[13])
	label15.text = str(dice_rolls[14])
	label16.text = str(dice_rolls[15])
	main_button.action = button_press
	self.title = 'Play Again'

square = 125
grid = 4
mg = 12
main_button = ui.Button(name = 'main_button', bg_color='#0D3C64', tint_color='white', frame=(w/2-120,h-150,240,100))
main_button.title = 'Roll'
main_button.action = button_press


# row 1
label1 = ui.Label(name = 'label1', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2- (2*square+(3*mg)),square, square))
label2 = ui.Label(name = 'label2', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2- (2*square+(3*mg)),square, square))
label3 = ui.Label(name = 'label3', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2- (2*square+(3*mg)),square, square))
label4 = ui.Label(name = 'label4', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2- (2*square+(3*mg)),square, square))

# row 2
label5 = ui.Label(name = 'label1', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2-(square+mg),square, square))
label6 = ui.Label(name = 'label2', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2-(square+mg),square, square))
label7 = ui.Label(name = 'label3', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2-(square+mg),square, square))
label8 = ui.Label(name = 'label4', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2-(square+mg),square, square))

# row 3
label9 = ui.Label(name = 'label1', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2+mg,square, square))
label10 = ui.Label(name = 'label2', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2+mg,square, square))
label11 = ui.Label(name = 'label3', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2+mg,square, square))
label12 = ui.Label(name = 'label4', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2+mg,square, square))

# row 4
label13 = ui.Label(name = 'label1', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2+ (square+(3*mg)),square, square))
label14 = ui.Label(name = 'label2', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2+(square+(3*mg)),square, square))
label15 = ui.Label(name = 'label3', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2+ (square+(3*mg)),square, square))
label16 = ui.Label(name = 'label4', bg_color='#E3DAC9',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2+ (square+(3*mg)),square, square))

@ui.in_background
def countdown():
	for i in range(0,6):
		print(i)
		timer.text=str(5 - i)
		time.sleep(1)
	label1.text = ''
	label2.text = ''
	label3.text = ''
	label4.text = ''
	label5.text = ''
	label6.text = ''
	label7.text = ''
	label8.text = ''
	label9.text = ''
	label10.text = ''
	label11.text = ''
	label12.text = ''
	label13.text = ''
	label14.text = ''
	label15.text = ''
	label16.text = ''
	main_button.title = 'Show Letters'

# timer = ui.Button(name = 'timer', bg_color='yellow', frame=(100, 100, 200, 100))
#
# timer.title = '180'
# timer.action = countdown

timer = ui.Label(name = 'timer', bg_color='#0D3C64',font =('Arial Rounded MT Bold', 75), text_color='white', frame=(100, 100, 200, 100))
timer.alignment = ui.ALIGN_CENTER
timer.text = '180'



label1.alignment = ui.ALIGN_CENTER
label2.alignment = ui.ALIGN_CENTER
label3.alignment = ui.ALIGN_CENTER
label4.alignment = ui.ALIGN_CENTER
label5.alignment = ui.ALIGN_CENTER
label6.alignment = ui.ALIGN_CENTER
label7.alignment = ui.ALIGN_CENTER
label8.alignment = ui.ALIGN_CENTER
label9.alignment = ui.ALIGN_CENTER
label10.alignment = ui.ALIGN_CENTER
label11.alignment = ui.ALIGN_CENTER
label12.alignment = ui.ALIGN_CENTER
label13.alignment = ui.ALIGN_CENTER
label14.alignment = ui.ALIGN_CENTER
label15.alignment = ui.ALIGN_CENTER
label16.alignment = ui.ALIGN_CENTER


view.add_subview(main_button)
view.add_subview(label1)
view.add_subview(label2)
view.add_subview(label3)
view.add_subview(label4)
view.add_subview(label5)
view.add_subview(label6)
view.add_subview(label7)
view.add_subview(label8)
view.add_subview(label9)
view.add_subview(label10)
view.add_subview(label11)
view.add_subview(label12)
view.add_subview(label13)
view.add_subview(label14)
view.add_subview(label15)
view.add_subview(label16)
view.add_subview(timer)


view.present(hide_title_bar=True)
