import sys
import re
import xlsxwriter
import codesystem
import encyrption
encodeChoice = 0

while (encodeChoice < 1 or encodeChoice > 2):
    try:
        # Get encoded choice
        encodeChoice = int(input('Messaging Code System:\n1: Encryption\n2: Morse Code\n3: Pigeon Carrier\nEnter the number corresponding to your encoding choice:'))
    except ValueError:
        # Make sure it is a valid number
        print("That wasn't a proper choice.")
    

textBlock = []
while True:
    sourceText = input('\nType text to encode one line at a time. Press enter to start a new line. Type Q in a separate line to end the message.')
    if sourceText.lower() == 'q':
        break
    textBlock.append(sourceText)

for textData in textBlock:
    if encodeChoice == 2:
        codesystem.Transmitter.encodeToMorse(textData)
    if encodeChoice == 1:
        encryption.encryption.shift(textData)
    if encodeChouce == 3:


