import sys
import skimage.io
import skimage.viewer
import skimage.color

# # read input image, based on filename parameter
# image = skimage.io.imread(fname=sys.argv[1])
#
# # display original image
# viewer = skimage.viewer.ImageViewer(image)
# #viewer.show()
#
# # convert to grayscale and display
# gray_image = skimage.color.rgb2gray(image)
# viewer = skimage.viewer.ImageViewer(gray_image)
# #viewer.show()


def binary_little_endian_to_int(array):
    byte_sum = 0
    multiplier = 1
    for byte in array:
        byte_sum += byte * multiplier
        multiplier *= 2**8
    return byte_sum


def binary_little_endian_to_string(array):
    return array.decode()


with open("sample_640×426.bmp", "rb") as image:
    f = image.read()
    b = bytearray(f)


def print_file_attributes(array):
    file_attributes = {
        'header field': (0, 2, binary_little_endian_to_string),
        'file size in bytes': (2, 4, binary_little_endian_to_int),
        'offset': (10, 4, binary_little_endian_to_int),
        'size of DIB header': (14, 4, binary_little_endian_to_int),
        'width': (18, 4, binary_little_endian_to_int),
        'height': (22, 4, binary_little_endian_to_int),
        'number of color planes': (26, 2, binary_little_endian_to_int),
        'bits per pixel': (28, 2, binary_little_endian_to_int),
        'compression method': (30, 4, binary_little_endian_to_int),
        'size of the raw bitmap data': (34, 4, binary_little_endian_to_int),
        'horizontal resolution of the image': (38, 4, binary_little_endian_to_int),
        'vertical resolution of the image': (42, 4, binary_little_endian_to_int),
        'number of colors in the color palette': (46, 4, binary_little_endian_to_int),
        'number of important colors used': (50, 4, binary_little_endian_to_int),
        'units for the horizontal and vertical resolutions ': (54, 2, binary_little_endian_to_int),
        'padding': (56, 2, binary_little_endian_to_int),
        'direction in which the bits fill the bitmap': (58, 2, binary_little_endian_to_int),
        'halftoning algorithm': (60, 2, binary_little_endian_to_int),
    }

    compression_methods = {
        0: 'BI_RGB',
        1: 'BI_RLE8',
        2: 'BI_RLE4',
        3: 'BI_BITFIELDS',
        4: 'BI_JPEG',
        5: 'BI_PNG',
        6: 'BI_ALPHABITFIELDS',
        11: 'BI_CMYK',
        12: 'BI_CMYKRLE8',
        13: 'BI_CMYKRLE4',
    }

    halftoning_algorithms = {
        0: 'none',
        1: 'Error diffusion',
        2: 'PANDA: Processing Algorithm for Noncoded Document Acquisition',
        3: 'Super-circle',
    }

    for key, value in file_attributes.items():
        offset, size, function = value
        attribute_value = function(b[offset:(offset+size)])
        if key == 'compression method':
            for compression_key in compression_methods:
                if attribute_value == compression_key:
                    print(f"{key} = {compression_methods[compression_key]}")
        if key == 'halftoning algorithm':
            for halftoning_key in halftoning_algorithms:
                if attribute_value == halftoning_key:
                    print(f"{key} = {halftoning_algorithms[halftoning_key]}")
        else:
            print(f"{key} = {attribute_value}")


print_file_attributes(b)
