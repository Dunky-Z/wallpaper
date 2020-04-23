import json
import requests, ctypes
from datetime import datetime

# creating names for images with date and time


PIC_DIR = "D:\Pictures\Pictures\wallpaper\\"
now = datetime.now()
pic_name = PIC_DIR + now.strftime("%d%m%Y%H%M%S")
pic_name = pic_name + ".jpeg"

# 使用Unsplash随机图片，过滤大小为4096*2160
url = "https://source.unsplash.com/random/4096x2160"


class GetImage():

    # 初始化常用变量
    def __init__(self, pic_name, url):
        self.pic_name = pic_name
        self.url = url

    # 从Unsplash下载并保存图片
    def get_img_from_unsplash(self):
        print("")
        print("* 正在获取图片，请稍等···")
        try:
            r = requests.get(self.url)
            with open(self.pic_name, 'wb') as image:
                image.write(r.content)
            print("* 图片已保存")
        except:
            print("* 图片保存失败，请重试")

    def get_imag_from_bing(self):
        searchURL = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
        response = requests.get(searchURL)
        data = json.loads(response.text)

        resultId = data['images'][0]['hsh']
        resultURL = 'https://cn.bing.com' + data['images'][0]['url']
        print("* 正在获取图片，请稍等···")
        response = requests.get(resultURL)
        with open(self.pic_name, 'wb') as img:
            img.write(response.content)

    # 使用Cpython接口调用Windows API改变壁纸
    def set_new_wallpaper(self):
        print("* 正在设置壁纸，请稍后···")
        print("* 成功更换壁纸")
        print(self.pic_name)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.pic_name, 0)


def main():
    # 实例化类
    img = GetImage(pic_name, url)
    # 从Unsplash抓取图片
    #img.get_img_from_unsplash()
    # 从bing首页抓取图片
    img.get_imag_from_bing()
    # 设置壁纸
    img.set_new_wallpaper()


# running the main() script
if __name__ == "__main__":
    main()
