from PIL import Image,ImageDraw,ImageFont
import random
import os
import string
import time


class OdinhjCapcha:
    font_path = os.path.join(os.path.dirname(__file__),'KhmerOS.ttf')
    number = 4
    size = (100,40)
    bgcolor = (0,0,0)
    random.seed(int(time.time()))
    fontcolor = (random.randint(200,255),random.randint(100,253),random.randint(100,255))
    font_size = 20
    linecolor =  (random.randint(0,255),random.randint(0,253),random.randint(0,255))
    draw_line = True
    drow_point = True
    SOURCE = list(string.ascii_letters)
    for index in range(0,10):
        SOURCE.append(str(index))

    @classmethod
    def __gene_item(cls):
        """
        绘制字体
        :return:
        """
        return ''.join(random.sample(cls.SOURCE,cls.number))

    @classmethod
    def __gene_line(cls,draw,width,height):
        """
        绘制干扰线
        :param draw:
        :param width:
        :param height:
        :return:
        """
        begin = (random.randint(0,width),random.randint(0,height))
        end = (random.randint(0,width),random.randint(0,height))
        draw.line([begin,end],fill = cls.linecolor)

    @classmethod
    def __gene_point(cls,draw,point_chance,width,height):
        """
        绘制点
        :param draw:
        :param point_chance:
        :param width:
        :param height:
        :return:
        """
        chance = min(0,max(0,int(point_chance)))
        for w in range(width):
            for h in range(height):
                temp = random.randint(0,100)
                if temp > 100 -chance:
                    draw.point((w,h),fill=(56,77,44))

    @classmethod
    def gene_code(cls):
        """
        绘制验证码
        :return:
        """
        width,height = cls.size
        image = Image.new('RGBA',(width,height),cls.bgcolor)
        font = ImageFont.truetype(cls.font_path,cls.font_size)
        draw = ImageDraw.Draw(image)
        text = cls.__gene_item()
        font_width,font_heoght = font.getsize(text)
        draw.text(((width-font_width)/2,(height-font_heoght)/2),text,font=font,fill=(255,255,255))

        if cls.draw_line:
            for i in range(0,10):
                cls.__gene_line(draw,width,height)
        if cls.drow_point:
            cls.__gene_point(draw,80,width,height)

        return (text,image)