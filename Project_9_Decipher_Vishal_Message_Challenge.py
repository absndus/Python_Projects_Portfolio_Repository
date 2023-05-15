#File: Project_9_Decipher_Vishal_Message_Challenge.py
#Author: Albert Schultz
#Date: 05/15/2023
#Version: 1.00
#Descriptions: This project script goes through the process of deciphering Vishal's message using various Python skills.

#Create required variables needed for this script to run.
v_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alphabet = "abcdefghijklmnopqrstuvwxyz"
translated_message = ""

#Run the character in message for loop to decode Vishal's message received.
for character in v_message:
    if character in alphabet:
        character_value = alphabet.find(character)
        translated_message += alphabet[(character_value + 10) % 26]
    else:
        translated_message += character

#Print the translated message to console
print(f"Decoded message from Vishal: {translated_message}\n")

#Encode the message and send it back to Vishal's inbox.
message_for_v = "hey vishal! This is so cool, thanks for showing me! What else do you got?"
translated_message_for_v = ""

for character in message_for_v:
    if character in alphabet:
        character_value = alphabet.find(character)
        translated_message_for_v += alphabet[(character_value - 10) % 26]
    else:
        translated_message_for_v += character

#Print the translaged message for Vishal.
print(f"Encoded Message to Vishal: {translated_message_for_v}\n")

#Let's make functions for decoding and decoding message. :)
def caesar_decode(message, offset):
    decode_message = ""
    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            decode_message += alphabet[(character_value + offset) % 26]
        else:
            decode_message += character
    return decode_message

def caesar_encode(message, offset):
    encoded_message = ""
    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            encoded_message += alphabet[(character_value - offset) % 26]
        else:
            encoded_message += character
    return encoded_message

#Let's sample the encode and decode messge functions using a set of messages.
message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(caesar_decode(message_one, 10))

message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(caesar_decode(message_two, 14))

#Decode Vishal's most recent message.
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(caesar_decode(brute_force_message, i)))