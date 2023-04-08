import os
from PIL import Image, ImageFont, ImageDraw

final_output = "./output_image/final_output.jpg"

#to avoid file from getting overwritten
if os.path.isfile(final_output):
    print("An instance of Final Output image already exists and will be deleted upon execution\nThe program is now paused, Kindly take a backup of that file")
    user_input = input("Press any key to proceed : ")
    os.remove(final_output)



with open('input_file.txt') as my_file:
    my_file.seek(0, os.SEEK_END) #to check if the file is empty or not
    if my_file.tell():
        my_file.seek(0)
        print("ok") #Status Ok
        #reading lines
        input_text = open('input_file.txt','r').read()
        print(input_text) #printing the lines


        assignment_image = Image.open("./sample_image/Assignment_template.jpg")
        written_font = ImageFont.truetype("./font/IndieFlower-Regular.ttf",70)
        draw = ImageDraw.Draw(assignment_image)
        x,y = 177,80  #coordinates of the page
        for line in input_text:
            draw.text((x,y), input_text, fill=(1,22,55), font= written_font)
            break



        assignment_image.save(final_output)
    else:
        print("File is Empty\nExecution Failed")




