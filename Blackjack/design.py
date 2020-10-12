from tkinter import LEFT,Y

#Argumetns for Design:
table_font = 'Helvetica'

background_color = '#FF6666'

font_small  = (table_font,26)
font_medium = (table_font,36)
font_large  = (table_font,60)

#Buttons:
button_args = {
    'fg': '#FFFFFF',
    'font' : font_small
}


#Arguments for packing
pack_left_and_fill_y = {
    'side' : LEFT,
    'fill' : Y
}

#Frame properties
hightlight_frame_with_white = {
    'highlightthickness' : 1,
    'highlightcolor' : '#FFFFFF',
    'highlightbackground' : '#FFFFFF'
}
