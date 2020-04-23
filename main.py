import json
import time
import string
from builtins import input

import requests, ctypes
from datetime import datetime

# creating names for images with date and time


PIC_DIR = "D:\Pictures\Pictures\wallpaper\\"
now = datetime.now()
pic_name = PIC_DIR + now.strftime("%d%m%Y%H%M%S")
pic_name = pic_name + ".jpeg"


class GetImage():

    # 初始化常用变量
    def __init__(self, pic_name):
        self.pic_name = pic_name

    # 从Unsplash下载并保存图片
    def get_img_from_unsplash(self):
        # 使用Unsplash随机图片，过滤大小为1920*1280
        url = "https://source.unsplash.com/random/1920x1080"
        print("")
        print("* 正在获取图片，请稍等···")
        try:
            r = requests.get(url)
            with open(self.pic_name, 'wb') as image:
                image.write(r.content)
            print("* 图片已保存")
        except:
            print("* 图片保存失败，请重试")

    def get_img_from_bing(self):
        searchURL = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
        print("* 正在获取图片，请稍等···")
        try:
            response = requests.get(searchURL)
            data = json.loads(response.text)
            resultURL = 'https://cn.bing.com' + data['images'][0]['url']
            response = requests.get(resultURL)
            with open(self.pic_name, 'wb') as img:
                img.write(response.content)
        except:
            print("* 图片保存失败，请重试")

    # 使用Cpython接口调用Windows API改变壁纸
    def set_new_wallpaper(self):
        print("* 正在设置壁纸，请稍后···")
        print("* 成功更换壁纸")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.pic_name, 0)

    def auto_change_wallpaper(self,seconds=15):
        print("* 请输入图片源: \n * us:Unsplash \t bing:Bing:")
        while True:
            img_src = input()
            if img_src == "us" or "bing":
                break
            else:
                print("输入有误请重新输入！")
                continue
        while True:
            if img_src == "us":
                GetImage.get_img_from_unsplash(self)
                GetImage.set_new_wallpaper(self)
                print("%d 秒后自动更新壁纸..."%seconds)
            elif img_src == "bing":
                GetImage.get_img_from_bing(self)
                GetImage.set_new_wallpaper(self)
                print("%d 秒后自动更新壁纸..."%seconds)
            time.sleep(seconds)

def main():
    # 实例化类
    img = GetImage(pic_name)
    # 从Unsplash抓取图片
    # img.get_img_from_unsplash()
    # 从bing首页抓取图片
    # img.get_img_from_bing()
    # 设置壁纸
    # img.set_new_wallpaper()
    img.auto_change_wallpaper()


# running the main() script
if __name__ == "__main__":
    main()
