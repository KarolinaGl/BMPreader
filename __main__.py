from BmpFile import BmpFile


if __name__ == '__main__':
    file = BmpFile('fourier1.bmp')
    # file = BmpFile('BITMAPCOREHEADER.bmp')
    # file = BmpFile('color_table1.bmp')
    # file = BmpFile('color_table2.bmp')
    # file = BmpFile('rgb24prof.bmp') # profil kolorów
    # file = BmpFile('sample_640×426.bmp')

    file.print_file_attributes()
    file.print_color_profile()
    # file.print_color_table()
    # file.fourier()
    # file.anonymization()

    print("===============")

    # file = BmpFile('output_file.bmp')
    # file.print_file_attributes()
    # file.print_color_table()
    # file.print_color_profile()
    # file.show()
