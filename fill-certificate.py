from tkinter import Image
from PIL import Image, ImageDraw,ImageFont

NAME_HEIGHT = 1170
INPUT_FILE = 'input.txt'
FONT_TYPE = 'arial.ttf'
FONT_SIZE = 125

def fillOut(certificate_file, person_name, file_name):
    img = Image.open(certificate_file)
    width, height = img.size


    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_TYPE, FONT_SIZE)
    w, h = draw.textsize(person_name, font=font)
    draw.text(((width-w)/2,NAME_HEIGHT-h), person_name, fill='black', font=font)
    img.save('filled/'+file_name, 'PDF')


def takeInput(input_file):
    file = open(input_file, 'r')
    linhas = file.readlines()

    for i in range(len(linhas)):
        linhas[i] = linhas[i].replace("\n",'')

    return linhas

def certificates():
    inputs = takeInput(INPUT_FILE)
    model_file = inputs.pop(0)

    for name in inputs:
        file = name.replace(' ', '')
        file += '-certificate.pdf'
        fillOut(model_file, name, file)


if __name__ == '__main__':
    certificates()