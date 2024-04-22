import config, random, os, time
a = 0
while a <= 500:
    print(random.randint(0,215125215))
    if random.randint(1,2) == 1:
        print("Validated")
    else:
        print("Invalid, fixing")
        a -= 1
    a += 1

config.CussLine = "-JG"

config.EnableCustomLogo = True
config.CustomLogo = (r"""

    


   ___ _____  _     _____ _____ _____  _   _ 
  |_  |  __ \| |   |_   _|_   _/  __ \| | | |
    | | |  \/| |     | |   | | | /  \/| |_| |
    | | | __ | |     | |   | | | |    |  _  |
/\__/ / |_\ \| |_____| |_  | | | \__/\| | | |
\____/ \____/\_____/\___/  \_/  \____/\_| |_/
                                             
                                             

                                


""")

def glitchcommline():
    os.system("cls")
    print("[J-Glitch WARN] THIS IS RUNNING OUTSIDE OF KERNAL AND BIOS!")
    print("ADVANCED USERS ONLY!!!")
    input()
    os.system("cls")
    x = input("G:/")
    if x == "removebiospass":
        config.AutoLockBIOS = False
        config.PassPermlock = ""
        print("Done!")
        input()
        import JOSv4
        JOSv4.commline()
    

def GlitchSel():
    x = input("Input custom commline or default (1/2):")
    if x == "1":
        glitchcommline()
    else:
        import JOSv4
        JOSv4.commline()


GlitchSel()