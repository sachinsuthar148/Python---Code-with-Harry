import os

if __name__ == '__main__':
    print("Welcome to Sachin Speaker")
    while True:
        x=input("Enter what you want to pronounce :")
        if x=="quit":
            os.system( f'''"  PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('bye bye friend');"''')
            break
        command = f'''"  PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''
        os.system(command)
