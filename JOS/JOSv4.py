import os, time, random
os.system("pip install keyboard")
import keyboard
import BIOS
import config
Started = False
"""
Functions

"""


"""
Command Line

"""

def commline():
    try:
        BIOS.Clear()
        if BIOS.KernalMode == True:
            print("[BIOS Warning] Kernal Debug loaded!")
        if BIOS.Permlock == True:
            print("[BIOS WARN] BIOS Loader locked!")
        BIOS.Logo()
        commlinein = input("J:/")
        if commlinein == "windows":
            Close = True
            print("Shutting down JOS")
            keyboard.press(Alt)
            keyboard.press_and_release(F4)
        elif commlinein == "shutdown":
            BIOS.Clear()
            sdshut = input("Would you like to shutdown? [y/n]")
            if sdshut == "y" or "Y":
                os.system("shutdown /s")
                while True:
                    print("Shutdown:Init")
                    print("Shutdown:Saving System Info x0x")
                    print("Shutdown:Finished")
                    BIOS.wait(.01)
                    BIOS.Clear()
            else:
                commline()
        elif commlinein == "BIOS":
            if BIOS.Permlock == False:
                BIOS.Clear()
                BIOS.Logo()
                print(" ")
                print("Loading BIOS")
                BIOS.wait(3)
                BIOS.Clear()
                BIOS.BIOS()
            else:
                BIOS.Logo()
                print(" ")
                print("[BIOS WARN] BIOS Locked!")
                BIOS.Error("BIOS_JOS_LOCK_INIT_COM_TRU")
        elif commlinein == "info":
            BIOS.Clear()
            print("Version: v?.?.?")
            print("Logging in as Admin")
            print("Running JOS")
            input("Press enter to go back...")
            BIOS.Clear()
            commline()
        elif commlinein == "Debug-Crash":
            BIOS.FatelError("JOS_INIT_ERR_COMMAND", True)
        elif commlinein == "unlockbios":
            try:
                if BIOS.Permlock == True:
                    BIOS.Clear()
                    BIOS.Logo()
                    passpermlockin = input("Password:")
                    if passpermlockin == BIOS.PassPermlock:
                        BIOS.Permlock = False
                        BIOS.Clear()
                        BIOS.Logo()
                        print(" ")
                        print("BIOS Unlocked!")
                        input("Press enter to load BIOS")
                        BIOS.Clear()
                        BIOS.BIOS()
                    else:
                        BIOS.Clear()
                        BIOS.Logo()
                        print(" ")
                        print("Wrong Password!")
                        input("Press enter to return to command line.")
                        BIOS.Clear()
                        commline()
                else:
                    BIOS.Error("BIOS_NOT_LOCKED")
            except:
                BIOS.Clear()
                BIOS.FatelError("NO_CODE", False)

        elif commlinein == "Glitch-BIOS-Force":
            if config.CussLine == "-JG":
                BIOS.PassPermlock = ""
                BIOS.Clear()
                BIOS.Logo()
                print("Working on it, boss!")
                BIOS.wait(3)
                BIOS.Clear()
                import JG
            else:
                commline()
        elif commlinein != "info" or "BIOS" or "shutdown" or "windows":
            BIOS.Error("Command_Not_Found")
            BIOS.wait(2)
            commline()
        
        elif commlinein == None:
            commline()
    except:
        if Close != True:
            BIOS.Error("Err_No_Code")
            BIOS.Clear()
            BIOS.BIOS()



"""
Boot Loading

"""
 # Moved to BIOS
