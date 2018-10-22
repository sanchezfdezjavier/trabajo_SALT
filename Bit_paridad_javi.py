import random as rnd
import copy


class Bit_paridad_javi():

    def __init__(self, start, finish, n, p):
        self.start = start
        self.finish = finish
        self.n = n
        self.p = p
        self.messages_raw = []
        self.messages_raw = self.generate_messages_from_to()
        self.messages_parity = []
        self.messages_parity = self.add_parity_bit_to_messages()
        self.messages_parity_alterated = []
        self.messages_parity_alterated = self.alterate_messages()

    def get_messages_raw(self):

        return self.messages_raw

    def get_messages_parity(self):

        return self.messages_parity

    def get_messages_parity_alterated(self):

        return self.messages_parity_alterated

    def toString(self):

        print("Generamos ", self.n, " mensajes de cada longitud.")
        print("Los cuales van de ", self.start, " hasta ", self.finish)

    def generate_bit_message(self, l):

        list = []
        for i in range(l):
            random_bit = rnd.choice([0,1])
            list.append(random_bit)
        return list

    def generate_messages_from_to(self):

        messages_rep = []
        for i in range(self.start, self.finish +1):
            for j in range(0, self.n):
                messages_rep.append(self.generate_bit_message(i))
        return messages_rep

    def add_parity_bit_to_messages(self):

        aux_messages_parity = copy.deepcopy(self.messages_raw)
        #aux_messags_parity = self.messages_raw --> Actualizaba el atributo todo el rato.
        for i in range(len(self.messages_raw)):
            parity_bit = sum(self.messages_raw[i])%2
            aux_messages_parity[i].append(parity_bit)
        return aux_messages_parity

    def alterate_messages(self):

        aux_messages_parity_alterated = copy.deepcopy(self.messages_parity)

        for i in range(len(self.get_messages_parity())):
            for j in range(len(self.get_messages_parity()[i])):
                alterate = rnd.random() < self.p
                if alterate:
                    aux_messages_parity_alterated[i][j] = 1 - aux_messages_parity_alterated[i][j]

        return aux_messages_parity_alterated



#Testing
bitp = Bit_paridad_javi(2,4 ,2, 0.01)
print("\n\n\n")
print("Mensajes originales")
print(bitp.get_messages_raw())
print("\n\n\n")
print("Mensajes con bit de paridad añadido")
print(bitp.get_messages_parity())
print("\n\n\n")
print("Mensajes alterados")
print(bitp.get_messages_parity_alterated())


