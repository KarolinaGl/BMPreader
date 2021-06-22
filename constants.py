from utilities import binary_to_string, binary_little_endian_to_int, binary_big_endian_to_int

BITMAPFILEHEADER_SIZE = 14

BITMAPFILEHEADER = {
    'header field': (0, 2, binary_to_string),
    'file size in bytes': (2, 4, binary_little_endian_to_int),
    'offset': (10, 4, binary_little_endian_to_int),
}

BITMAPCOREHEADER = {
    'size of DIB header': (14, 4, binary_little_endian_to_int),
    'width': (18, 2, binary_little_endian_to_int),
    'height': (20, 2, binary_little_endian_to_int),
    'number of color planes': (22, 2, binary_little_endian_to_int),
    'bits per pixel': (24, 2, binary_little_endian_to_int),
}

BITMAPINFOHEADER = {
    'header field': (0, 2, binary_to_string),
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
}

BITMAPV4HEADER = {
    'header field': (0, 2, binary_to_string),
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
    'red channel bitmask ': (54, 4, binary_little_endian_to_int),
    'green channel bitmask': (58, 4, binary_little_endian_to_int),
    'blue channel bitmask': (62, 4, binary_little_endian_to_int),
    'alpha channel bitmask': (66, 4, binary_little_endian_to_int),
    'color space type': (70, 4, binary_little_endian_to_int),
    'color space endpoints': (74, 36, binary_little_endian_to_int),
    'gamma for red channel': (110, 4, binary_little_endian_to_int),
    'gamma for green channel': (114, 4, binary_little_endian_to_int),
    'gamma for blue channel': (118, 4, binary_little_endian_to_int),
}

BITMAPV5HEADER = {
    'header field': (0, 2, binary_to_string),
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
    'red channel bitmask ': (54, 4, binary_little_endian_to_int),
    'green channel bitmask': (58, 4, binary_little_endian_to_int),
    'blue channel bitmask': (62, 4, binary_little_endian_to_int),
    'alpha channel bitmask': (66, 4, binary_little_endian_to_int),
    'color space type': (70, 4, binary_little_endian_to_int),
    'color space endpoints': (74, 36, binary_little_endian_to_int),
    'gamma for red channel': (110, 4, binary_little_endian_to_int),
    'gamma for green channel': (114, 4, binary_little_endian_to_int),
    'gamma for blue channel': (118, 4, binary_little_endian_to_int),
    'intent': (122, 4, binary_little_endian_to_int),
    'ICC profile data offset': (126, 4, binary_little_endian_to_int),
    'ICC profile size': (130, 4, binary_little_endian_to_int),
    'reserved': (134, 4, binary_little_endian_to_int),
}

COMPRESSION_METHODS = {
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

HALFTONING_ALGORITHMS = {
    0: 'none',
    1: 'Error diffusion',
    2: 'PANDA: Processing Algorithm for Noncoded Document Acquisition',
    3: 'Super-circle',
}

DIB_HEADERS = {
    12: 'BITMAPCOREHEADER',
    64: 'OS22XBITMAPHEADER',
    16: 'OS22XBITMAPHEADER',
    40: 'BITMAPINFOHEADER',
    52: 'BITMAPV2INFOHEADER',
    56: 'BITMAPV3INFOHEADER',
    108: 'BITMAPV4HEADER',
    124: 'BITMAPV5HEADER',
}

DIB_HEADERS_TO_ATTRIBUTES = {
    12: BITMAPCOREHEADER,
    40: BITMAPINFOHEADER,
    108: BITMAPV4HEADER,
    124: BITMAPV5HEADER,
}

COLOR_PROFILE = {
    'Profile size': (0, 4, binary_big_endian_to_int),
    'Preferred CMM type': (4, 4, binary_big_endian_to_int),
    'Profile/Device class': (12, 4, binary_to_string),
    'Colour space of data': (16, 4, binary_to_string),
    'PCS': (20, 4, binary_to_string),
    'Number of the year': (24, 2, binary_big_endian_to_int),
    'Number of the month': (26, 2, binary_big_endian_to_int),
    'Number of the day of the month': (28, 2, binary_big_endian_to_int),
    'Number of hours': (30, 2, binary_big_endian_to_int),
    'Number of minutes': (32, 2, binary_big_endian_to_int),
    'Number of seconds': (34, 2, binary_big_endian_to_int),
    'profile file signature': (36, 4, binary_to_string),
    'Primary platform signature': (40, 4, binary_to_string),
}

ATTRIBUTES_TO_DELETE = {
    'file size in bytes': (2, 4, binary_little_endian_to_int),
    'number of color planes': (26, 2, binary_little_endian_to_int),
    'compression method': (30, 4, binary_little_endian_to_int),
    'size of the raw bitmap data': (34, 4, binary_little_endian_to_int),
    'horizontal resolution of the image': (38, 4, binary_little_endian_to_int),
    'vertical resolution of the image': (42, 4, binary_little_endian_to_int),
    'number of colors in the color palette': (46, 4, binary_little_endian_to_int),
    'number of important colors used': (50, 4, binary_little_endian_to_int),
    'red channel bitmask ': (54, 4, binary_little_endian_to_int),
    'green channel bitmask': (58, 4, binary_little_endian_to_int),
    'blue channel bitmask': (62, 4, binary_little_endian_to_int),
    'alpha channel bitmask': (66, 4, binary_little_endian_to_int),
    'color space type': (70, 4, binary_little_endian_to_int),
    'color space endpoints': (74, 36, binary_little_endian_to_int),
    'gamma for red channel': (110, 4, binary_little_endian_to_int),
    'gamma for green channel': (114, 4, binary_little_endian_to_int),
    'gamma for blue channel': (118, 4, binary_little_endian_to_int),
    'intent': (122, 4, binary_little_endian_to_int),
    'ICC profile data': (126, 4, binary_little_endian_to_int),
    'ICC profile size': (130, 4, binary_little_endian_to_int),
    'reserved': (134, 4, binary_little_endian_to_int),
}