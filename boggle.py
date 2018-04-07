import ui
from random import randint
import time

w,h = ui.get_screen_size()
view = ui.View(bg_color='white', frame=(0,0,w,h))

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

def roll(die_number, dice):
	this_roll = randint(0,5)
	the_letter = dice[die_number][this_roll]
	return the_letter

def button_press(self):
	print('button was pressed')
	self.title = "Re-roll"
	label1.text = str(roll(0, dice))
	label2.text = str(roll(1, dice))
	label3.text = str(roll(2, dice))
	label4.text = str(roll(3, dice))
	label5.text = str(roll(4, dice))
	label6.text = str(roll(5, dice))
	label7.text = str(roll(6, dice))
	label8.text = str(roll(7, dice))
	label9.text = str(roll(8, dice))
	label10.text = str(roll(9, dice))
	label11.text = str(roll(10, dice))
	label12.text = str(roll(11, dice))
	label13.text = str(roll(12, dice))
	label14.text = str(roll(13, dice))
	label15.text = str(roll(14, dice))
	label16.text = str(roll(15, dice))
	#label1.text = str(1)
	#label2.text = str(2)
	#label3.text = str(3)
	#label4.text = str(4)

square = 125
grid = 4
mg = 12
button1 = ui.Button(name = 'button1', bg_color='lightblue', frame=(w/2-120,h-150,240,100))

# row 1
label1 = ui.Label(name = 'label1', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2- (2*square+(3*mg)),square, square))
label2 = ui.Label(name = 'label2', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2- (2*square+(3*mg)),square, square))
label3 = ui.Label(name = 'label3', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2- (2*square+(3*mg)),square, square))
label4 = ui.Label(name = 'label4', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2- (2*square+(3*mg)),square, square))

# row 2
label5 = ui.Label(name = 'label1', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2-(square+mg),square, square))
label6 = ui.Label(name = 'label2', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2-(square+mg),square, square))
label7 = ui.Label(name = 'label3', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2-(square+mg),square, square))
label8 = ui.Label(name = 'label4', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2-(square+mg),square, square))

# row 3
label9 = ui.Label(name = 'label1', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2+mg,square, square))
label10 = ui.Label(name = 'label2', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2+mg,square, square))
label11 = ui.Label(name = 'label3', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2+mg,square, square))
label12 = ui.Label(name = 'label4', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2+mg,square, square))

# row 4
label13 = ui.Label(name = 'label1', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(2*square+(3*mg)),h/2+ (square+(3*mg)),square, square))
label14 = ui.Label(name = 'label2', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2-(square+mg),h/2+(square+(3*mg)),square, square))
label15 = ui.Label(name = 'label3', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+mg,h/2+ (square+(3*mg)),square, square))
label16 = ui.Label(name = 'label4', bg_color='lightgreen',font =('Arial Rounded MT Bold', square-mg), frame=(w/2+(square + 3*mg),h/2+ (square+(3*mg)),square, square))

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

button1.title = 'Roll'
button1.action = button_press

view.add_subview(button1)
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



view.present(hide_title_bar=True)
