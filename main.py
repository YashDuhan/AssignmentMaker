import os, enchant
from PIL import Image, ImageFont, ImageDraw

#Universal_args
FINAL_OUTPUT = "./output_image/final_output.jpg"
TEMPLATE_IMAGE = "./sample_image/Assignment_template.jpg"
FONT_FINAL = "./font/IndieFlower-Regular.ttf"
X, Y = 177, 80  # default coordinates for the page
FONT_SIZE = 70
PDF_OUTPUT = './PDF/pdf_output/output.pdf'

def select_font():
    print("Select A font")
    print("1. IndieFlower\n2. Kristi\n3. Kalam\n4. Sue Ellen Francisco\n5. Desyrel\n6. Blokletters  ")
    font_choice = int(input("Enter your choice : "))
    if font_choice == 1:
        return "./font/IndieFlower-Regular.ttf", 70, 177, 80
    elif font_choice == 2:
        return "./font/Kristi.ttf", 90, 174, 80
    elif font_choice == 3:
        return "./font/Kalam-Light.ttf", 82, 180, 90
    elif font_choice == 4:
        return "./font/SueEllenFrancisco.ttf", 70, 177, 80
    elif font_choice == 5:
        return "./font/DESYREL.ttf", 70, 177, 80
    elif font_choice == 6:
        return "./font/Blokletters-Potlood.ttf", 60, 180, 110
    else:
        print("Invalid Font..\nIndieFlower will be your new default font")
        return "./font/IndieFlower-Regular.ttf", 70, 177, 80

def create_assignment_image():
    font_final, font_size, x, y = select_font()

    if os.path.isfile(FINAL_OUTPUT):
        print("An instance of Final Output image already exists and will be deleted upon execution\nThe program is now paused, Kindly take a backup of that file")
        user_input = input("Press any key to proceed : ")
        os.remove(FINAL_OUTPUT)

    with open('input_file.txt') as my_file:
        my_file.seek(0, os.SEEK_END)  # to check if the file is empty or not
        if my_file.tell():
            my_file.seek(0)
            print("ok")  # Status Ok
            # reading lines
            input_text = open('input_file.txt', 'r').read()
            print(input_text)  # printing the lines

            assignment_image = Image.open(TEMPLATE_IMAGE)
            written_font = ImageFont.truetype(font_final, font_size)
            draw = ImageDraw.Draw(assignment_image)
            for line in input_text:
                draw.text((x, y), input_text, fill=(1, 22, 55), font=written_font)
                break
            assignment_image.save(FINAL_OUTPUT)
        else:
            print("File is Empty\nExecution Failed")

def remove_output_image():
    if os.path.isfile(FINAL_OUTPUT):
        os.remove(FINAL_OUTPUT)
        print("Deleted Successfully...")
    else:
        print("File doesn't exist..")

def make_pdf():
    # Need to wait
    pass

def remove_pdf():
    if os.path.isfile(PDF_OUTPUT):
        os.remove(PDF_OUTPUT)
        print("Deleted Successfully...")
    else:
        print("File doesn't exist..")

def exit_program():
    print("Exiting program...")
    exit()

def spell_check():
    # this functions is buggier 
    with open('input_file.txt','r') as file:
        text = file.read()
    
    #splitting the text into word by word
    words = text.split() 
    #creating an object to check the english words 
    dictionary = enchant.Dict("en_US")

    for word in words:
        if not dictionary.check(word):
            # Get a list of suggestions for the misspelled word
            suggestions = dictionary.suggest(word)

            # Print the misspelled word and its suggestions
            print("Error: ",{word})
            print("Suggestions:")
            for suggestion in suggestions:
                print(suggestion)

            #Asking users if they want to fix it
            fix = input("Do you want to fix this error? (y/n): ")
            if fix == 'y' or 'Y':
                # Replace the misspelled word with the first suggestion
                text = text.replace(word, suggestions[0])
            else:
                print("Ok")

def main():
    while True:
        print("1. Write your Assignment\n2. Remove the already existing output image\n3. Make a PDF\n4. Remove the already existing output PDF\n5. Spell Check\n6. Exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            create_assignment_image()
        elif choice == 2:
            remove_output_image()
        elif choice == 3:
            make_pdf()
        elif choice == 4:
            remove_pdf()
        elif choice == 5:
            spell_check_choice = input("This Function might take a lot of time for you to check errors one by one\nDo you want to continue? (y/n)")
            if spell_check_choice == 'y' or 'Y':
                spell_check()
            else:
                main() 
        elif choice == 6:
            exit_program()
        else:
            print("Invalid Option")
            main()

main()
