# Joan Bosco Olives Florit NIA: 217056
import os
import tkinter
from tkinter import *
from tkinter import ttk

'''
Al crear videos iguales que se usan en los dos scripts, y van a tener nombres iguales, normalmente en la ejecucion 
se pide si se quiere sobrescribir el video, en caso de que ya exista. Perfectamente se puede denegar con 'N' en la 
pesatanya de Run, ya que asi se ahorra el tiempo de generar ese video de nuevo.
'''


# this function create 4 videos with different size's
def resize_video(path):
    os.system('ffmpeg -i ' + path + ' -s 1280x720 -c:a copy 720p.mp4')
    os.system('ffmpeg -i ' + path + ' -s 640x480 -c:a copy 480p.mp4')
    os.system('ffmpeg -i ' + path + ' -s 360x240 -c:a copy 360x240.mp4')
    os.system('ffmpeg -i ' + path + ' -s 160x120 -c:a copy 160x120.mp4')


# 4 next different functions convert the codecs
def vp8(path, bitrate='500k'):
    os.system(
        'ffmpeg -i ' + path + '.mp4' + ' -c:v libvpx  -c:a libvorbis -b:v ' + bitrate + ' ' + bitrate + path + '-VP8.webm')


def vp9(path, bitrate='500k'):
    os.system(
        'ffmpeg -i ' + path + '.mp4' + ' -c:v libvpx-vp9  -c:a libvorbis -b:v ' + bitrate + ' ' + bitrate + path + '-VP9.webm')


def h265(path, bitrate='500k'):
    os.system(
        'ffmpeg -i ' + path + '.mp4' + ' -c:v libx265 -c:a libvorbis -b:v ' + bitrate + ' ' + bitrate + path + '-h265.mp4')


def av1(path, bitrate='500k'):
    os.system('ffmpeg -i ' + path + '.mp4' + ' -c:v libaom-av1 -b:v ' + bitrate + ' ' + bitrate + path + '-av1.mkv')


def main():
    path = 'BBB_10sec.mp4'
    root = Tk()
    root.title("S3 - By Boscoolives")
    root.geometry("400x650")

    label = tkinter.Label(root,
                          text="First use 'Resize BBT Video' Button to create\n 4 resized formats: 720 480 240 120",
                          bg="red", font="Helvectica 12 bold italic")
    label.pack()
    # resizes videos, necessary to  use other buttons!!
    boton1 = tkinter.Button(root, text="Resize BBT Video", command=lambda: resize_video(path))
    boton1.pack()

    labelvp8 = tkinter.Label(root, text="-----VP8-----", font="Helvectica 12 bold", fg="blue")
    labelvp8.pack(fill=tkinter.X)
    boton2 = tkinter.Button(root, text="vp8 - 720", command=lambda: vp8('720p'))
    boton2.pack()
    boton3 = tkinter.Button(root, text="vp8 - 480", command=lambda: vp8('480p'))
    boton3.pack()
    boton4 = tkinter.Button(root, text="vp8 - 360x240", command=lambda: vp8('360x240'))
    boton4.pack()
    boton5 = tkinter.Button(root, text="vp8 - 160x120", command=lambda: vp8('160x120'))
    boton5.pack()

    labelvp9 = tkinter.Label(root, text="-----VP9-----", font="Helvectica 12 bold", fg="blue")
    labelvp9.pack()
    boton6 = tkinter.Button(root, text="vp9 - 720", command=lambda: vp9('720p'))
    boton6.pack()
    boton7 = tkinter.Button(root, text="vp9 - 480", command=lambda: vp9('480p'))
    boton7.pack()
    boton8 = tkinter.Button(root, text="vp9 - 360x240", command=lambda: vp9('360x240'))
    boton8.pack()
    boton9 = tkinter.Button(root, text="vp9 - 160x120", command=lambda: vp9('160x120'))
    boton9.pack()

    labelh265 = tkinter.Label(root, text="-----H265-----", font="Helvectica 12 bold", fg="blue")
    labelh265.pack()
    boton10 = tkinter.Button(root, text="h265 - 720", command=lambda: h265('720p'))
    boton10.pack()
    boton11 = tkinter.Button(root, text="h265 - 480", command=lambda: h265('480p'))
    boton11.pack()
    boton12 = tkinter.Button(root, text="h265 - 360x240", command=lambda: h265('360x240'))
    boton12.pack()
    boton13 = tkinter.Button(root, text="h265 - 160x120", command=lambda: h265('160x120'))
    boton13.pack()

    labelAV1 = tkinter.Label(root, text="-----AV1-----", font="Helvectica 12 bold", fg="blue")
    labelAV1.pack()
    boton14 = tkinter.Button(root, text="av1 - 720", command=lambda: av1('720p'))
    boton14.pack()
    boton15 = tkinter.Button(root, text="av1 - 480", command=lambda: av1('480p'))
    boton15.pack()
    boton16 = tkinter.Button(root, text="av1 - 360x240", command=lambda: av1('360x240'))
    boton16.pack()
    boton17 = tkinter.Button(root, text="av1 - 160x120", command=lambda: av1('160x120'))
    boton17.pack()

    label.mainloop()


if __name__ == "__main__":
    main()
