import cv2
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv, rgba2rgb

from more_itertools import chunked

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

from constants import BITMAPV5HEADER, BITMAPFILEHEADER_SIZE, COMPRESSION_METHODS, HALFTONING_ALGORITHMS, DIB_HEADERS, \
    COLOR_PROFILE, DIB_HEADERS_TO_ATTRIBUTES, BITMAPCOREHEADER, ATTRIBUTES_TO_DELETE
from utilities import binary_little_endian_to_int, binary_to_string, binary_big_endian_to_int


class BmpFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        with open(self.file_name, "rb") as image:
            f = image.read()
            b = bytearray(f)
        return b

    def show(self):
        image = imread(self.file_name)
        imshow(image)
        plt.show()

    def get_dib_header_size(self):
        array = BmpFile.open_file(self)
        dib_header_offset = BITMAPV5HEADER['size of DIB header'][0]
        dib_header_field_size = BITMAPV5HEADER['size of DIB header'][1]
        return binary_little_endian_to_int(array[dib_header_offset:(dib_header_offset + dib_header_field_size)])

    def get_dict_value(self, attribute_name, dict_name):
        array = BmpFile.open_file(self)
        offset = dict_name[attribute_name][0]
        field_size = dict_name[attribute_name][1]
        return dict_name[attribute_name][2](array[offset:(offset + field_size)])

    def print_file_attributes(self):
        array = BmpFile.open_file(self)

        for key, value in DIB_HEADERS_TO_ATTRIBUTES[self.get_dib_header_size()].items():
            offset, size, function = value
            if offset + size - BITMAPFILEHEADER_SIZE > self.get_dib_header_size():
                continue
            attribute_value = function(array[offset:(offset + size)])
            if key == 'compression method':
                for compression_key in COMPRESSION_METHODS:
                    if attribute_value == compression_key:
                        print(f"{key} = {COMPRESSION_METHODS[compression_key]}")
            elif key == 'halftoning algorithm':
                for halftoning_key in HALFTONING_ALGORITHMS:
                    if attribute_value == halftoning_key:
                        print(f"{key} = {HALFTONING_ALGORITHMS[halftoning_key]}")
            elif key == 'size of DIB header':
                for DIB_key in DIB_HEADERS:
                    if attribute_value == DIB_key:
                        print(f"{key} = {attribute_value} => {DIB_HEADERS[DIB_key]}")
            else:
                print(f"{key} = {attribute_value}")

    def print_color_profile(self):
        array = BmpFile.open_file(self)

        if self.get_dib_header_size() >= 124 and self.get_dict_value('ICC profile size', BITMAPV5HEADER) > 0:
            ICC_offset = self.get_dict_value('ICC profile data offset', BITMAPV5HEADER)
            ICC_size = self.get_dict_value('ICC profile size', BITMAPV5HEADER)

            offset = ICC_offset + BITMAPFILEHEADER_SIZE
            ICC_data = array[offset:offset + ICC_size]

            for key, value in COLOR_PROFILE.items():
                offset, size, function = value
                attribute_value = function(ICC_data[offset:(offset + size)])
                print(f"{key} = {attribute_value}")
        else:
            print('No color profile found')

    def fourier(self):
        img = cv2.imread(self.file_name, 0)

        plt.subplot(231)
        plt.imshow(img, cmap='gray')
        plt.title("Original Image")

        # fft - Compute the one-dimensional discrete Fourier Transform
        # fft2 - Compute the 2-dimensional discrete Fourier Transform
        original = np.fft.fft2(img)
        plt.subplot(232), plt.imshow(np.log(1 + np.abs(original)), "gray"), plt.title("Spectrum")

        # fftshift - Shift the zero-frequency component to the center of the spectrum
        center = np.fft.fftshift(original)
        plt.subplot(233), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Centered spectrum")

        plt.subplot(234), plt.imshow(np.angle(original), "gray"), plt.title("Phase angle")

        inv_center = np.fft.ifftshift(center)
        processed_img = np.fft.ifft2(inv_center)
        plt.subplot(235), plt.imshow(np.abs(processed_img), "gray"), plt.title("Inverse transform")

        plt.show()

    def anonymization(self):
        array = BmpFile.open_file(self)

        if self.get_dib_header_size() > 124 and self.get_dict_value('ICC profile size', BITMAPV5HEADER) > 0:
            ICC_offset = self.get_dict_value('ICC profile data offset', BITMAPV5HEADER)
            ICC_size = self.get_dict_value('ICC profile size', BITMAPV5HEADER)
            full_offset = ICC_offset + BITMAPFILEHEADER_SIZE

            for key, value in COLOR_PROFILE.items():
                offset, size, function = value
                for i in range(full_offset + offset, full_offset + offset + size):
                    array[i] = 0

        for key, value in ATTRIBUTES_TO_DELETE.items():
            offset, size, function = value
            if 12 < self.get_dib_header_size() < offset + size - BITMAPFILEHEADER_SIZE:
                continue
            for i in range(offset, offset + size):
                array[i] = 0

        if self.get_dib_header_size() >= 12:
            with open("output_file.bmp", "wb") as file:
                file.write(array)

    def print_color_table(self):
        array = BmpFile.open_file(self)

        number_of_palette_colors = self.get_dict_value('number of colors in the color palette', BITMAPV5HEADER)
        if self.get_dib_header_size() > 16 and self.get_dict_value('bits per pixel', BITMAPV5HEADER) <= 8:
            print("Color table:")
            table = []
            for i in range(number_of_palette_colors):
                offset = BITMAPFILEHEADER_SIZE + self.get_dib_header_size() + 4 * i
                print("i={:<7} R: {:<7} G: {:<7} B: {:<7}".format(i+1, array[offset:offset+4][2],
                                                                  array[offset:offset+4][1], array[offset:offset+4][0]))
                table.append([array[offset:offset + 4][2], array[offset:offset + 4][1], array[offset:offset + 4][0]])
            for i in list(reversed(range(1, 41))):
                if number_of_palette_colors % i == 0:
                    indices = list(chunked(range(number_of_palette_colors), i))
                    break
            numpy_array = np.array(table, dtype=np.uint8)
            numpy_indices = np.array(indices)
            io.imshow(numpy_array[numpy_indices])
            plt.show()
        else:
            print('No color pallete found')
