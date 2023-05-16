#File: Project_10_Make_Initials.py
#Author: Albert Schultz
#Date: 05/15/2023
#Version: 1.00
#Descriptions: This project script automatically detects the first letter of the first, middle, and last name and outputs the letter in block form, vertically.

#Create required variables needed for this script to run.
name = input("Enter your first, middle, and last name: ")

#Create an 3 letter initial builder function that extracts the three letters from the name variable of the user's first, middle, and last name.
def initial_name_builder(name):
    name_first_last_split = name.split(' ')
    first_name = name_first_last_split[0]
    middle_name = name_first_last_split[1]
    last_name = name_first_last_split[2]
    f_initial = first_name[0]
    m_initial = middle_name[0]
    l_initial = last_name[0]
    return f_initial + m_initial + l_initial

initial_name = str(initial_name_builder(name))

#Database of the pre-defined block alphabet.
def alphabet_block_initializer(initial_name):
    nameA = """
       AAA
      A   A
      A   A
      AAAAA
      A   A
      A   A
      A   A
    """

    nameB = """
      BBBB
      B   b
      B   B
      BBBB
      B   B
      B   B
      BBBB
    """

    nameC = """
       CCC
      C   C
      C
      C
      C
      C   C
       CCC
    """

    nameD = """
      DDDD
      D   D
      D   D
      D   D
      D   D
      D   D
      DDDD
    """

    nameE = """
      EEEEE
      E
      E
      EEEEE
      E
      E
      EEEEE
    """

    nameF = """
      FFFFF
      F
      F
      FFFFF
      F
      F
      F
    """

    nameG = """
       GGG
      G   G
      G
      G GGG
      G   G
      G   G
       GGG
    """

    nameH = """
      H   H
      H   H
      H   H
      HHHHH
      H   H
      H   H
      H   H
    """

    nameI = """
      IIIII
        I
        I
        I
        I
        I
      IIIII
    """

    nameJ = """
       JJJJ
         J
         J
         J
      j  J
      j  J
       JJ
    """

    nameK = """
      K   K
      K  K
      K K
      KK
      K K
      K  K
      K   K
    """

    nameL = """
      L
      L
      L
      L
      L
      L
      LLLLL
    """

    nameM = """
      M   M
      MM MM
      M M M
      M   M
      M   M
      M   M
      M   M
    """

    nameN = """
      N   N
      NN  N
      N N N
      N  NN
      N   N
      N   N
      N   N
    """

    nameO = """
       OOO
      O   O
      O   O
      O   O
      O   O
      O   O
       OOO
    """

    nameP = """
      PPPP
      P   P
      P   P
      PPPP
      P
      P
      P
    """

    nameQ = """
       QQQ
      Q   Q
      Q   Q
      Q   Q
      Q   Q
      Q  QQ
       QQQQ
           Q
    """

    nameR = """
      RRRR
      R   R
      R   R
      RRRR
      R   R
      R   R
      R   R
    """

    nameS = """
       SSS
      S   S
      S   
       SS
         SS
      S   S
       SSS
    """

    nameT = """
      TTTTT
        T
        T
        T
        T
        T
        T
    """

    nameU = """
      U   U
      U   U
      U   U
      U   U
      U   U
      U   U
       UUU
    """

    nameV = """
      V   V
      V   V
      V   V
      V   V
       V V
       V V
        V
    """

    nameW = """
      W   W
      W   W
      W   W
      W   W
      W W W
      W W W
       W W
    """

    nameX = """
      X   X
      X   X
       X X
        X
       X X
      X   X
      X   X
    """

    nameY = """
      Y   Y
      Y   Y 
       Y Y
        Y
        Y
        Y
        Y
    """

    nameZ = """
      ZZZZZZ
           Z
          Z
         Z
        Z
       Z
      ZZZZZZ
    """

    #Create elifs statements.
    if initial_name[0] == 'A':
        print(nameA)
    elif initial_name[0] == 'B':
        print(nameB)
    elif initial_name[0] == 'C':
        print(nameC)
    elif initial_name[0] == 'D':
        print(nameD)
    elif initial_name[0] == 'E':
        print(nameE)
    elif initial_name[0] == 'F':
        print(nameF)
    elif initial_name[0] == 'G':
        print(nameG)
    elif initial_name[0] == 'H':
        print(nameH)
    elif initial_name[0] == 'I':
        print(nameI)
    elif initial_name[0] == 'J':
        print(nameJ)
    elif initial_name[0] == 'K':
        print(nameK)
    elif initial_name[0] == 'L':
        print(nameL)
    elif initial_name[0] == 'M':
        print(nameM)
    elif initial_name[0] == 'N':
        print(nameN)
    elif initial_name[0] == 'O':
        print(nameO)
    elif initial_name[0] == 'P':
        print(nameP)
    elif initial_name[0] == 'Q':
        print(nameQ)
    elif initial_name[0] == 'R':
        print(nameR)
    elif initial_name[0] == 'S':
        print(nameS)
    elif initial_name[0] == 'T':
        print(nameT)
    elif initial_name[0] == 'U':
        print(nameU)
    elif initial_name[0] == 'V':
        print(nameV)
    elif initial_name[0] == 'W':
        print(nameW)
    elif initial_name[0] == 'X':
        print(nameX)
    elif initial_name[0] == 'Y':
        print(nameY)
    elif initial_name[0] == 'Z':
        print(nameZ)
    else:
        print("Please enter your name with a space between first, middle, and last name.")

    if initial_name[1] == 'A':
        print(nameA)
    elif initial_name[1] == 'B':
        print(nameB)
    elif initial_name[1] == 'C':
        print(nameC)
    elif initial_name[1] == 'D':
        print(nameD)
    elif initial_name[1] == 'E':
        print(nameE)
    elif initial_name[1] == 'F':
        print(nameF)
    elif initial_name[1] == 'G':
        print(nameG)
    elif initial_name[1] == 'H':
        print(nameH)
    elif initial_name[1] == 'I':
        print(nameI)
    elif initial_name[1] == 'J':
        print(nameJ)
    elif initial_name[1] == 'K':
        print(nameK)
    elif initial_name[1] == 'L':
        print(nameL)
    elif initial_name[1] == 'M':
        print(nameM)
    elif initial_name[1] == 'N':
        print(nameN)
    elif initial_name[1] == 'O':
        print(nameO)
    elif initial_name[1] == 'P':
        print(nameP)
    elif initial_name[1] == 'Q':
        print(nameQ)
    elif initial_name[1] == 'R':
        print(nameR)
    elif initial_name[1] == 'S':
        print(nameS)
    elif initial_name[1] == 'T':
        print(nameT)
    elif initial_name[1] == 'U':
        print(nameU)
    elif initial_name[1] == 'V':
        print(nameV)
    elif initial_name[1] == 'W':
        print(nameW)
    elif initial_name[1] == 'X':
        print(nameX)
    elif initial_name[1] == 'Y':
        print(nameY)
    elif initial_name[1] == 'Z':
        print(nameZ)
    else:
        print("Please enter your name with a space between first, middle, and last name.")

    if initial_name[2] == 'A':
        print(nameA)
    elif initial_name[2] == 'B':
        print(nameB)
    elif initial_name[2] == 'C':
        print(nameC)
    elif initial_name[2] == 'D':
        print(nameD)
    elif initial_name[2] == 'E':
        print(nameE)
    elif initial_name[2] == 'F':
        print(nameF)
    elif initial_name[2] == 'G':
        print(nameG)
    elif initial_name[2] == 'H':
        print(nameH)
    elif initial_name[2] == 'I':
        print(nameI)
    elif initial_name[2] == 'J':
        print(nameJ)
    elif initial_name[2] == 'K':
        print(nameK)
    elif initial_name[2] == 'L':
        print(nameL)
    elif initial_name[2] == 'M':
        print(nameM)
    elif initial_name[2] == 'N':
        print(nameN)
    elif initial_name[2] == 'O':
        print(nameO)
    elif initial_name[2] == 'P':
        print(nameP)
    elif initial_name[2] == 'Q':
        print(nameQ)
    elif initial_name[2] == 'R':
        print(nameR)
    elif initial_name[2] == 'S':
        print(nameS)
    elif initial_name[2] == 'T':
        print(nameT)
    elif initial_name[2] == 'U':
        print(nameU)
    elif initial_name[2] == 'V':
        print(nameV)
    elif initial_name[2] == 'W':
        print(nameW)
    elif initial_name[2] == 'X':
        print(nameX)
    elif initial_name[2] == 'Y':
        print(nameY)
    elif initial_name[2] == 'Z':
        print(nameZ)
    else:
        print("Please enter your name with a space between first, middle, and last name.")
#Preview the initials of the person's name.
print(f"Your initials are, {initial_name}.")
alphabet_block_initializer(initial_name)