from collections import deque

class Rotor:
    counter = None
    wheel_idx = None
    wheel = None
    max_char = None
    nth_rotor = None
    reflector = None

    def __init__(self, wheel, nth_rotor, reflector=False) -> None:
        self.counter = 0
        self.wheel = wheel
        self.wheel_idx = [i for i in range(len(wheel))]
        self.max_char = len(wheel)
        self.nth_rotor = nth_rotor
        self.reflector = reflector
    
    def set_start(self, start=0):
        self.rotate_wheel(start)
    
    def rotate_wheel(self,rot=1):
        tmp = deque(self.wheel)
        tmp.rotate(-rot)
        self.wheel = list(tmp)

        tmp = deque(self.wheel_idx)
        tmp.rotate(-rot)
        self.wheel_idx = list(tmp)
        

    def left_to_right(self,idx) -> int:
        '''
            |2  C|
        --> |1  A|
            |0  B| -->
        '''
        self.counter += 1
        if self.counter % (self.max_char**(self.nth_rotor-1)) == 0:
            self.rotate_wheel()
        
        left_side_val = self.wheel_idx[idx]
        return left_side_val if self.reflector else self.wheel.index(left_side_val)
        

    def right_to_left(self,idx) -> int:
        '''
            |2  C|
        <-- |1  A|
            |0  B| <--
        '''
        right_side_val = idx if self.reflector else self.wheel[idx]
        return self.wheel_idx.index(right_side_val)

def enigma(key=None, text='test'):
    # key       : kunci, berupa 3 huruf alfabet
    # text      : plaintext apabila enkripsi, ciphertext apabila dekripsi

    # Tentukan alfabet rotor
    # alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
    #           'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    rotor1 = Rotor(
        wheel=[22, 16, 23, 0, 21, 13, 17, 19, 2, 9, 4, 8, 24, 3, 5, 25, 11, 10, 18, 6, 14, 15, 12, 20, 1, 7],
        nth_rotor=1) 
    rotor2 = Rotor(
        wheel=[7, 2, 20, 18, 3, 5, 0, 8, 14, 10, 16, 23, 17, 24, 4, 13, 11, 22, 12, 1, 15, 19, 6, 9, 21, 25],
        nth_rotor=2)
    rotor3 = Rotor(
        wheel=[17, 10, 18, 3, 8, 11, 4, 14, 7, 5, 12, 0, 22, 16, 23, 1, 13, 9, 19, 6, 2, 21, 15, 25, 24, 20],
        nth_rotor=3,
        reflector=True)

    reflektor = {10: 5, 24: 13, 15: 21, 18: 4, 17: 1, 0: 19, 23: 22, 7: 2,
    25: 6, 11: 9, 14: 12, 8: 16, 3: 20, 5: 10, 13: 24, 21: 15, 4: 18,
    1: 17, 19: 0, 22: 23, 2: 7, 6: 25, 9: 11, 12: 14, 16: 8, 20: 3}

    text_clean = ''
    key_clean = ''

    # Ambil hanya alfabet, selain itu dihilangkan
    for char in text:
        if char.isalpha():
            text_clean += char.upper()

    for char in key:
        if char.isalpha():
            key_clean += char.upper()
    
    # Apabila panjang kunci bukan 3 tidak menghasilkan apa-apa
    if (len(key_clean) != 3) or key_clean is None:
        key_clean == 'AAA'

    # Posisi rotor teratas
    rotor1.set_start(ord(key_clean[0])-ord('A'))
    rotor2.set_start(ord(key_clean[1])-ord('A'))
    rotor3.set_start(ord(key_clean[2])-ord('A'))

    # Enkripsi
    hasil = ''
    for char in text_clean:

        idx1l = rotor1.left_to_right(ord(char)-ord('A'))
        idx2l = rotor2.left_to_right(idx1l)
        idx3l = rotor3.left_to_right(idx2l)


        reflect = reflektor[idx3l]

        idx3r = rotor3.right_to_left(reflect)
        idx2r = rotor2.right_to_left(idx3r)
        idx1r = rotor1.right_to_left(idx2r)

        hasil += chr(ord('A') + idx1r)
        

    return hasil

print(enigma('ABC', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))
print(enigma('ABC', 'TWGBOJREOCPGFNSPEQTIZPCSUFGMSIFGWERVTRTDEDPGTIYEPSZCOMYIHIWDYQO'))

print(enigma('ASD', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))
print(enigma('ASD', 'TWGBOJREOCPGFNSPEQTIZPCSUFGMSIFGWERVTRTDEDPGTIYEPSZCOMYIHIWDYQO'))