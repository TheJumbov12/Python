import os, time, random
from subprocess import call
os.system("pip install keyboard psutil")
import psutil
import keyboard
import config
import JOSv4
keyboard.press_and_release("F11")
os.system("cls")

global KernalMode
Permlock = False
KernalMode = False



def wait(x):
    time.sleep(x)

def Logo():
    if config.EnableCustomLogo == False:
        logo = (r"""

    ___  ________  ________      
   |\  \|\   __  \|\   ____\     
   \ \  \ \  \|\  \ \  \___|_    
 __ \ \  \ \  \\\  \ \_____  \   
|\  \\_\  \ \  \\\  \|____|\  \  
\ \________\ \_______\____\_\  \ 
 \|________|\|_______|\_________\
                     \|_________|
                                 
                                 


""")
        print(logo)
    else:
        try:
            logo = config.CustomLogo
            print(logo)
            print("Powered by JOS")
        except:
            FatelError("BIOS_LOGO_ERR_LOAD", True)

def Clear():
    os.system("cls")

def Error(x):
    try:
        Clear()
        print(f"An error has occured! CODE: {x}")
        input()
        Clear()
        print("Loading JOS...")
        wait(2)
        Clear()
        JOSv4.commlinein = None
        JOSv4.commline()
    except:
        Clear()
        Logo()
        print("Fatel ERR: Error handeler failed to run! This is really bad. Like bad bad, bailing!!!")
        input()
        Clear()

def FatelError(x,y):
    print(f"A fatel error has occured! CODE: {x}")
    if y == True:
        wait(3)
        print("JOS/BIOS cannot be recovered by auto-recover! Bailing!!")
        input()
        Clear()
    else:
        print("Trying to recover JOS/BIOS, stand-by...")
        wait(5)
        Clear()
        if Permlock == False:
            print("Recovered by auto-recover! Press enter to enter BIOS then enter 'loadJOS' to load JOS")
            input()
            Clear()
            BIOS()
        else:
            print("Recovered by auto-recover! Press enter to reload JOS!")
            input()
            JOSv4.commline()

def Kernal():
    a = 0
    while a <= 10000:
        print(random.randint(0,5128329852364218713252))
        a += 1
    input("Press enter to return to BIOS")
    BIOS()




def StartUp():
    try:
        print(config.CussLine)
        x = 0
        while x <= 100:
            wait(.1)
            print(f"Loading JOS | {x}%")
            Clear()
            x += random.randint(1,4)
        Clear()
        JOSv4.commline()
    except:
        Clear()
        Logo()
        print(" ")
        Error("JOS_BOOT_FAIL_PANIC")
        input()
        Clear()
        print("Loading BIOS...")
        wait(5)
        Clear()
        try:
            BIOS()
        except:
            FatelError("BIOS_FAILURE_FATEL", False)


def BIOS():
    try:
        BIOSNum = input("/:/")
        if BIOSNum == "loadJOS":
            try:
                global KernalMode
                KernalMode = False
                StartUp()
            except:
                Clear()
                Logo()
                print(" ")
                FatelError("JOS_PANIC", False)
        elif BIOSNum == "loadJOS -P":
            global Permlock
            global PassPermlock
            PassPermlock = input("Pasword to unlock BIOS:")
            Permlock = True
            StartUp()
        elif BIOSNum == "previewsyssettings":
            print(f"Auto BIOS Lock: {config.AutoLockBIOS}")
            print(f"BIOS Password: ----")
            print(f"Custom Logo: {config.EnableCustomLogo}")
            print(f"Custom Var Line {config.CussLine}")
            input("Press enter to return")
            BIOS()
        elif BIOSNum == "loadWindows":
            print("Loading Windows...")
            wait(.01)
        elif BIOSNum == "loadlinux":
            print("Error")
            input()
            BIOS()
        elif BIOSNum == "loadJOS -k":
            KernalMode = True
            a = 0
            while a <= 10000:
                print(random.randint(0,5128329852364218713252))
                a += 1
            wait(2)
            Clear()
            JOSv4.commline()
        elif BIOSNum == "kernalinfodump":
            Kernal()
        elif BIOSNum == "CrashHandleTest":
            print("Warning: This is stop BIOS/JOS")
            input()
            Error("BIOS_TEST_CODE")
            keyboard.press_and_release(ctrl+C)
            FatelError("BIOS_TEST_CODE", True)
        elif BIOSNum == "quit":
            Clear()
            print("Stopping system BIOS function | Dx00210")
            wait(2)
        elif BIOSNum == "excute":
            import JG
        elif BIOSNum != "loadlinux" or "loadWindows" or "loadJOS":
            Clear()
            print("Invalid Input")
            wait(1)
            Clear()
            BIOS()
    except:
        Clear()
        FatelError("BIOS_FATEL_ERROR", False)




def bootmenu():
    try:
        print("""
[1] = BIOS
[2] = JOS
[3] = Windows
===================
            """)
        try:
            BIOSSel = input("-=")
        except:
            Clear()
            BIOS()
        BIOSSel = int(BIOSSel)
        if BIOSSel == 2:
            os.system("cls")
            try:
                StartUp()
            except:
                Clear()
                Logo()
                print(" ")
                print("Failed to load JOS. Press enter to restart...")
                input()
                print("Restarting...")
                wait(3)
                Clear()
                StartUp()
        elif BIOSSel == 3:
            Clear()
        elif BIOSSel == 1:
            os.system("cls")
            BIOS()
        elif BIOSSel <= 3:
            print(f"Loading JOS as {BIOSSel} is not an option")
            time.sleep(1)
            input()
        elif BIOSSel != 3 or 2 or 1:
            BIOS()
        elif BIOSSel == None:
            print(f"Loading JOS as {BIOSSel} is not an option")
            time.sleep(1)
            input()
    except:
        Clear()
        FatelError("KERNAL_PANIC_WARN", True)

if config.AutoLockBIOS == True:
    if config.PassPermlock != None:
        PassPermlock = config.PassPermlock
    else:
        PassPermlock = "pijadpigjaidjg90-ai939gjaeigj9900093j2itgoajgpa-f0dsif0i-0q2i-39wjepifjapg0-oi-91j9iwj9p10oi-ed9ia9jpijg0-2gioekapojfgie0gi-2-3itpoejapidjgopaidpogje9u930i10okmwkjsgpokok[okg93i2jgpoiqeogj-02i]"
    Permlock = True
    StartUp()


if config.AutoLockBIOS != True:
    bootmenu()
else:
    print("Bypassing bootmenu because of policy")
    Clear()