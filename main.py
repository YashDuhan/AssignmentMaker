import os
from PIL import Image, ImageFont, ImageDraw

#Universal-Decleration
final_output = "./output_image/final_output.jpg"
template_image = "./sample_image/Assignment_template.jpg"
font_final = "./font/IndieFlower-Regular.ttf"
x,y = 177,80  #coordinates for the page
font_size = 70 

i = 0
while ( i == 0): #iteratively repeating the user-panel
    #user-panel
    print("1.Write your Assignment\n2.Remove the already existing output image\n3.Make a PDF\n4.Remove the already existing pdf file\n5.Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("Select font")
        print("1. IndieFlower\n2. Kristi\n3. Kalam\n4. Sue Ellen Francisco\n5. Desyrel\n6. Blokletters  ")
        font_choice = int(input("Enter your choice : "))
        if font_choice == 1:
            font_final = "./font/IndieFlower-Regular.ttf"
            font_size = 70
        elif font_choice == 2:
            font_final = "./font/Kristi.ttf"
            font_size = 90
            x,y = 174,80
        elif font_choice == 3:
            font_final = "./font/Kalam-Light.ttf"
            font_size = 82
            x,y = 180,90
        elif font_choice == 4:
            font_final = "./font/SueEllenFrancisco.ttf"
            font_size = 70
        elif font_choice == 5:
            font_final = "./font/DESYREL.ttf"
            font_size = 70
        elif font_choice == 6:
            font_final = "./font/Blokletters-Potlood.ttf"
            font_size = 60
            x,y = 180,110
        else:
            print("Invalid Font..\nIndieFlower will be your new default font")
            
        #to avoid file from getting overwritten
        if os.path.isfile(final_output):
            print("An instance of Final Output image already exists and will be deleted upon execution\nThe program is now paused, Kindly take a backup of that file")
            user_input = input("Press any key to proceed : ")
            os.remove(final_output)

        #writing operations
        with open('input_file.txt') as my_file:
            my_file.seek(0, os.SEEK_END) #to check if the file is empty or not
            if my_file.tell():
                my_file.seek(0)
                print("ok") #Status Ok
                #reading lines
                input_text = open('input_file.txt','r').read()
                print(input_text) #printing the lines


                assignment_image = Image.open(template_image)
                written_font = ImageFont.truetype(font_final,font_size)
                draw = ImageDraw.Draw(assignment_image)
                for line in input_text:
                    draw.text((x,y), input_text, fill=(1,22,55), font= written_font)
                    break
                assignment_image.save(final_output)
            else:
                print("File is Empty\nExecution Failed")

    elif choice == 2:
        if os.path.isfile(final_output):
            os.remove(final_output)
            print("Deleted Successfully...")
        else:
            print("File doesn't exist..")
    
    elif choice == 5:
        i = 1
    else:
        print("Invalid Choice\nTry Again\n")
