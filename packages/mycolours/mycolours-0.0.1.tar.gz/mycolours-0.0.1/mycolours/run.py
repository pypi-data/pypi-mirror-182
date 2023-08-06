import cython
def pic(pic_pos,pixel = (100,100)):
    from PIL import Image
    return_list=[]
    def RGB_to_Hex(rgb):

        RGB = rgb # 将RGB格式划分开来
        color = '#'
        for i in RGB:
            num = int(i)
            # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
            color += str(hex(num))[-2:].replace('x', '0').upper()
        return color

    from PIL import Image

    im = Image.open(pic_pos)
    pixel_y=list(pixel)[1]
    pixel_x=list(pixel)[0]
    pix_list=[]

    yrange=im.size[1]
    xrange=im.size[0]
    for y in range(int(yrange *(1/(yrange /pixel_y)))):
        for x in range(int(xrange*(1/(xrange/pixel_x)))):
            pix = im.getpixel((x*xrange//pixel_x, y*(xrange//pixel_y)))
            pix_list.append(RGB_to_Hex(pix))
        return_list.append(pix_list)
    return return_list