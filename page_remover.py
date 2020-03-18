    #This programs removes selected pages form a pdf file.

    #Created at 18.03.20 by Tarik.

from PyPDF2 import PdfFileWriter,PdfFileReader
import sys
import os


def getPdfFile():
    global input_file
    input_file=PdfFileReader(input_file_name,'rb')
    global output_file
    output_file = PdfFileWriter()


def get_remove_pages():
    page_count = input_file.numPages
    print("your file has " + str(page_count) + " pages.Type te pages to delete (use ').")
    pages_to_delete = input()
    del_list_str= pages_to_delete.split(",")
    print("Deleting pages...")

    del_list_int=[]
    for i in del_list_str:
        del_list_int.append(int(i)-1)
    for i in range(input_file.numPages):
        if i not in del_list_int:
            page = input_file.getPage(i)
            output_file.addPage(page)


def saveFile():
    strTemp='new_'+input_file_name
    with open(strTemp , 'wb') as f:
        output_file.write(f)
    print("-------------> The new file succesfully saved as " + strTemp)


def main():
    if len(sys.argv) != 2:
        print("usage ---->  python page_remover.py your_file_name")
        exit(1)
    else:
        global input_file_name
        input_file_name = sys.argv[1]
        if not (os.path.exists(input_file_name)):
            print("File not found!!")
        getPdfFile()
        get_remove_pages()
        print("Saving File...")
        saveFile()

        exit()



if __name__ == '__main__' :
        main()
