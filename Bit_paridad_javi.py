import random as rnd
import copy
import matplotlib.pyplot as plt
import numpy as np


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
        self.probabilities = ()
        self.probabilities = self.calculate_probabilities()

    def get_n(self):

        return self.n

    def get_start(self):

        return self.start

    def get_finish(self):

        return self.finish

    #Corregir
    def get_total_messages(self):

        return len(range(self.start, self.finish +1)) * self.n, "mal"

    def get_messages_raw(self):

        return self.messages_raw

    def get_messages_parity(self):

        return self.messages_parity

    def get_messages_parity_alterated(self):

        return self.messages_parity_alterated

    def get_probabilities(self):

        return self.probabilities

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
        #Cambiar variable de control
        step = (len(range(self.start, self.finish)) * self.n ) // 20
        for i in range(self.start, self.finish, step):
            for j in range(0, self.n):
                messages_rep.append(self.generate_bit_message(i))
        return messages_rep

    def add_parity_bit_to_messages(self):

        aux_messages_parity = copy.deepcopy(self.messages_raw)
        #aux_messags_parity = self.messages_raw --> Actualizaba el atributo todo el rato
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

    def calculate_probabilities(self):

        altered_messages_counter = 0
        altered_and_detected_messages_counter = 0

        for i in range(len(self.messages_parity_alterated)):
            received_message_satisfies_parity =  sum(self.messages_parity_alterated[i]) % 2 == 0

            if self.messages_parity[i] != self.messages_parity_alterated[i]:
                altered_messages_counter += 1
                if not received_message_satisfies_parity:
                    altered_and_detected_messages_counter +=1
            altered_and_no_detected_messages_counter = altered_messages_counter - altered_and_detected_messages_counter

        return altered_messages_counter, altered_and_detected_messages_counter, altered_and_no_detected_messages_counter

    def calculate_separate_probabilities(self):
        pass

    def test_plot_results(self):
        n_groups = 10
        means_frank = (90, 55, 40, 65, 90, 55, 40, 65, 10, 67)
        means_guido = (85, 62, 54, 20, 90, 55, 40, 65, 20, 90)

        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rects1 = plt.bar(index, means_frank, bar_width,
                         alpha=opacity,
                         color='b',
                         label='alterados y no detectados')

        rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                         alpha=opacity,
                         color='r',
                         label='alterados y detectados')

        plt.xlabel('Person')
        plt.ylabel('Scores')
        plt.title('Resultados del método del bit de paridad')
        plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
        plt.legend()

        plt.tight_layout()
        plt.show()


#Testing
# De 10 hasta 19(longitud de los mensajes) y generamos 2 de cada longitud con una probabilidad de alteracion de bit 0.8
bitp = Bit_paridad_javi(10, 500, 2,0.8)
print("\n")
print("Mensajes originales")
print(bitp.get_messages_raw())
print("\n")
print("Mensajes con bit de paridad añadido")
print(bitp.get_messages_parity())
print("\n")
print("Mensajes alterados")
print(bitp.get_messages_parity_alterated())
print("\n")
print("Numero de mensajes alterados {}".format(len(bitp.get_messages_parity_alterated())))
#print("Mensajes totales generados {}".format(bitp.get_total_messages()))
print("Mensajes alterados: {}".format(bitp.get_probabilities()[0]))
print("Mensajes alterados y detectaados {}".format(bitp.get_probabilities()[1]))
print("Mensajes alterados y  no detectados {}".format(bitp.get_probabilities()[2]))
#print( (len(range(bitp.get_start(), bitp.get_finish())) * bitp.get_n()) // 6)
print("Numero de mensajes generados {}".format(len(bitp.get_messages_parity_alterated())))

for message in bitp.get_messages_parity_alterated():
    print(len(message))

bitp.test_plot_results()




