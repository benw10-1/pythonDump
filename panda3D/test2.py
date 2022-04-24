import os

rd = r"C:\Users\benja\PycharmProjects\unoGame\assets\toConvert"

for sd, d, f in os.walk(rd):
    for file in f:
        splt = file.split(".")
        os.system("blend2bam " + os.path.join(rd, file) + r" C:\Users\benja\PycharmProjects\unoGame\assets\bams\{}.bam".format(splt[0]) + r" --blender-dir D:\Steam\steamapps\common\Blender")