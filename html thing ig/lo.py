from pynput.keyboard import Listener, Controller, Key, KeyCode
import threading
import time

wordlist = "Aatrox, ahri, akali, alistar, amumu, anivia, annie, ashe, aurelion sol, azir, bard, blitzcrank, brand, braum, caitlyn, camille, cassiopeia, chogath, corki, darius, diana, dr mundo, draven, ekko, elise, evelynn, ezreal, fiddlesticks, fiora, fizz, galio, gangplank, garen, gnar, gragas, graves, hecarim, heimerdinger, illaoi, irelia, ivern, janna, jarvan iv , jax, jayce, jhin, jinx, kaisa, kalista, karma, karthus, kassadin, katarina, kayle, kayn, kennen, khazix, kindred, kled, kogmaw, leblanc, lee sin, leona, lissandra, lucian, lulu, lux, malphite, malzahar, maoki, master yi, miss fortune, mordekaiser, morgana, nami, nasus, nautilus, neeko, nidalee, nocturne, nunu, olaf, orianna, ornn, pantheon, poppy, pyke, quinn, rakan, rammus, reksai, renekton, rengar, riven, rumble, ryze, sejuani, shaco, shen, shyvana, singed, sion, sivir, skarner, sona, soraka, swain, sylas, syndra, tahm kench, taliyah, talon, taric, teemo, thresh, tristana, trundle, tryndamere, twisted fate, twitch, udyr, urgot, varus, vayne, veigar, velkoz, vi, viktor, vladimir, volibear, warwick, wukong, xayah, xerath, xin zhao, yasuo, yorick, yuumi, zac, zed, ziggs, zilean, zoe, zyra".split(
    ", ")


class lulw:
    def thing(self):
        global currentkey
        global auto
        while True:
            if self.stop == True:
                break
            localkey = currentkey
            keyboard = Controller()
            for x in wordlist:
                if self.stop == True:
                    break
                if len(x) == currentkey:
                    keyboard.type(x)
                    time.sleep(.5)
                    keyboard.press(Key.ctrl)
                    keyboard.press("a")
                    keyboard.release("a")
                    keyboard.release(Key.ctrl)
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                    if self.auto == True:
                        print("YES")
                        time.sleep(.1)
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        time.sleep(.5)
                if currentkey == 0:
                    keyboard.type(x)
                    time.sleep(.5)
                    keyboard.press(Key.ctrl)
                    keyboard.press("a")
                    keyboard.release("a")
                    keyboard.release(Key.ctrl)
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                    if self.auto == True:
                        print("YES")
                        time.sleep(.1)
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        time.sleep(.5)
                if currentkey != localkey:
                    break

    def start(self):
        self.t = threading.Thread(target=self.thing)
        self.stop = False
        self.t.start()

    def stop1(self):
        self.stop = True
        self.t.join()

    def autos1(self):
        self.auto = True
        print("auto")
    def autos(self):
        self.auto = False

    def __init__(self):
        self.stop = True
        self.auto = False


llulw = lulw()

currentkey = 0


def lolp(key):
    keyl = str(key)
    if keyl == "Key.enter":
        print("asd")
    global currentkey
    if keyl == '\'0\'':
        currentkey = 0
    if keyl == '\'1\'':
        currentkey = 0
    if keyl == '\'2\'':
        currentkey = 2
    if keyl == '\'3\'':
        currentkey = 3
    if keyl == '\'4\'':
        currentkey = 4
    if keyl == '\'5\'':
        currentkey = 5
    if keyl == '\'6\'':
        currentkey = 6
    if keyl == '\'7\'':
        currentkey = 7
    if keyl == '\'8\'':
        currentkey = 8
    if keyl == '\'9\'':
        currentkey = 9
    if keyl == "Key.down":
        if llulw.stop == True:
            llulw.start()
        else:
            llulw.stop1()
    if keyl == "Key.right":
        if llulw.auto == True:
            llulw.autos()
        else:
            llulw.autos1()
    if keyl == "Key.left":
        keyboard2 = Controller()
        keyboard2.press(Key.enter)


with Listener(on_press=lolp) as listener:
    listener.join()
