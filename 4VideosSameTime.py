# Joan Bosco Olives Florit NIA: 217056
from Resize_Convert_GUI import vp8, vp9, h265, av1
import os

'''
Al crear videos iguales que se usan en los dos scripts, y van a tener nombres iguales, normalmente en la ejecucion 
se pide si se quiere sobrescribir el video, en caso de que ya exista. Perfectamente se puede denegar con 'N' en la 
pesatanya de Run, ya que asi se ahorra el tiempo de generar ese video de nuevo.
'''


def main():
    path = 'BBB_10sec.mp4'
    # Generamos un video 480p, por si aún no se ha generado en el primer ejercicio
    # de esta forma no importa que script se ejectue primero
    os.system('ffmpeg -i ' + path + ' -s 640x480 -c:a copy 480p.mp4')
    bitrates = ['500k',  # listamos los diferentes bitrates
                '300k',
                '200k',
                '100k']

    # para cada uno de los bitrates generamos un video diferentes pero con el mismo codec, van a ser usados los 4
    # para generar un video estacado de 4 videos.
    for i in range(len(bitrates)):
        vp8('480p', bitrates[i])

    os.system(
        'ffmpeg -i 500k480p-vp8.webm -i 300k480p-vp8.webm -i 200k480p-vp8.webm -i 100k480p-vp8.webm -filter_complex hstack=inputs=4 4stackVP8.webm')

    for i in range(len(bitrates)):
        vp9('480p', bitrates[i])

    os.system(
        'ffmpeg -i 500k480p-vp9.webm -i 300k480p-vp9.webm -i 200k480p-vp9.webm -i 100k480p-vp9.webm -filter_complex hstack=inputs=4 4stackVP9.webm')

    for i in range(len(bitrates)):
        h265('480p', bitrates[i])

    os.system(
        'ffmpeg -i 500k480p-h265.mp4 -i 300k480p-h265.mp4 -i 200k480p-h265.mp4 -i 100k480p-h265.mp4 -filter_complex hstack=inputs=4 4stackH265.mp4')

    for i in range(len(bitrates)):
        av1('480p', bitrates[i])

    os.system(
        'ffmpeg -i 500k480p-av1.mkv -i 300k480p-av1.mkv -i 200k480p-av1.mkv -i 100k480p-av1.mkv -filter_complex hstack=inputs=4 4stackAV1.mkv')


if __name__ == "__main__":
    main()
