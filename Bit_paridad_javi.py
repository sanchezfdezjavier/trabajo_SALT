import random as rnd
import copy
import matplotlib.pyplot as plt
import numpy as np


class Bit_paridad_javi():

    def __init__(self, start, finish, n, p):
        self.step = 0
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
        self.probabilities = self.calculate_statistics()
        self.separate_statistics  = self.calculate_separate_statistics()

    #Getters
    def get_n(self):

        return self.n

    def get_start(self):

        return self.start

    def get_finish(self):

        return self.finish

    def get_total_messages(self):

        return len(self.messages_parity_alterated)

    def get_messages_raw(self):

        return self.messages_raw

    def get_messages_parity(self):

        return self.messages_parity

    def get_messages_parity_alterated(self):

        return self.messages_parity_alterated

    def get_probabilities(self):

        return self.probabilities


    def get_separate_statistics(self):

        return self.separate_statistics

    def get_length_group_messages(self):
        aux_length = []

        for message in self.messages_parity_alterated:
            aux_length.append(len(message))

        return aux_length
    # To print the charts indexes.
    def get_length_group_messages_simplified(self):

        aux_length = []

        for message in self.messages_parity_alterated:
            aux_length.append(len(message))
        set_length = set(aux_length)

        return_list = []

        for long in set_length:
            return_list.append(long)

        return_list.sort()
        return return_list


    def toString(self):

        print("Generamos ", self.n, " mensajes de cada longitud.")
        print("Los cuales van de ", self.start, " hasta ", self.finish)


    #Generates random message with a specified length
    def generate_bit_message(self, l):

        list = []
        for i in range(l):
            random_bit = rnd.choice([0,1])
            list.append(random_bit)
        return list

    #Generates messages groups. Each group has 'n' messages with a linear spaced length based on start and finish inputs
    def generate_messages_from_to(self):

        messages_rep = []
        #Cambiar variable de control
        self.step = (len(range(self.start, self.finish)) * self.n ) // 20 #This parameter controls the number of groups
        for i in range(self.start, self.finish, self.step):
            for j in range(0, self.n):
                messages_rep.append(self.generate_bit_message(i))
        return messages_rep

    #Adds the parity biy at the end of the message
    def add_parity_bit_to_messages(self):

        aux_messages_parity = copy.deepcopy(self.messages_raw)
        for i in range(len(self.messages_raw)):
            parity_bit = sum(self.messages_raw[i])%2
            aux_messages_parity[i].append(parity_bit)
        return aux_messages_parity

    #Modifies messages bits using the p given by the user
    def alterate_messages(self):

        aux_messages_parity_alterated = copy.deepcopy(self.messages_parity)

        for i in range(len(self.get_messages_parity())):
            for j in range(len(self.get_messages_parity()[i])):
                alterate = rnd.random() < self.p
                if alterate:
                    aux_messages_parity_alterated[i][j] = 1 - aux_messages_parity_alterated[i][j]

        return aux_messages_parity_alterated

    #Calculate the statistics for the whole group of messages
    def calculate_statistics(self):

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

    #Calculates the statistics for each group of messages
    def calculate_separate_statistics(self):

        altered_messages_counter = 0
        altered_and_detected_messages_counter = 0
        altered_and_no_detected_messages_counter = 0
        return_list = []

        counter = 0
        for i in range(len(self.messages_parity_alterated)):
            if counter > 1:
                return_list.append(aux_list)
                altered_messages_counter = 0
                altered_and_detected_messages_counter = 0
                altered_and_no_detected_messages_counter = 0
                aux_list = []
                counter = 0
            else:
                received_message_satisfies_parity = sum(self.messages_parity_alterated[i]) % 2 == 0

                if self.messages_parity[i] != self.messages_parity_alterated[i]:
                    altered_messages_counter += 1
                    if not received_message_satisfies_parity:
                        altered_and_detected_messages_counter += 1
                altered_and_no_detected_messages_counter = altered_messages_counter - altered_and_detected_messages_counter
                aux_list = [altered_messages_counter, altered_and_detected_messages_counter, altered_and_no_detected_messages_counter]
                counter += 1

        return return_list

    #Testing graphs

    def test_barchart_results(self):

        n_groups = len(self.separate_statistics)

        #Genera cada eje del barchart
        x1_altered_messages= []
        for probs in self.separate_statistics:
            x1_altered_messages.append(probs[0])

        x2_altered_and_detected_messages= []
        for probs2 in self.separate_statistics:
            x2_altered_and_detected_messages.append(probs[1])

        # create plot
        fig, ax = plt.subplots()
        index = [11,12,13,14,15]
        prev_length = -1
        length = -1

        #for message in self.messages_parity_alterated:

         #   length = len(message)
         #   if prev_length != length:
         #       index.append(len(message))
        #       prev_length = len(message)
        #  else:
         #       continue

        bar_width = 0.25
        opacity = 0.8

        rects1 = plt.bar(index, x1_altered_messages, bar_width,
                         alpha=opacity,
                         color='b',
                         label='alterados y no detectados')

        rects2 = plt.bar(index + bar_width, x2_altered_and_detected_messages, bar_width,
                         alpha=opacity,
                         color='r',
                         label='alterados y detectados')


    def plot_conclusions(self):
        pass

    def test_histogram_plot(self):
        values = [10,20.30,40,50,60]
        plt.hist(values, bins=[1,2,3,4,5,6], rwidth = 0.5, color = 'r')


# Testing

bitp = Bit_paridad_javi(10, 20, 2, 0.5)
print("\n")
print("Mensajes originales")
# print(bitp.get_messages_raw())
print("\n")
print("Mensajes con bit de paridad añadido")
# print(bitp.get_messages_parity())
print("\n")
print("Mensajes alterados")
#print(bitp.get_messages_parity_alterated())
print("\n")
print("Numero de mensajes alterados {}".format(len(bitp.get_messages_parity_alterated())))
print("Mensajes totales generados {}".format(bitp.get_total_messages()))
print("Mensajes alterados: {}".format(bitp.get_probabilities()[0]))
print("Mensajes alterados y detectaados {}".format(bitp.get_probabilities()[1]))
print("Mensajes alterados y  no detectados {}".format(bitp.get_probabilities()[2]))
print( (len(range(bitp.get_start(), bitp.get_finish())) * bitp.get_n()) // 6)
print("Numero de mensajes generados {}".format(len(bitp.get_messages_parity_alterated())))
print(bitp.calculate_statistics())
print(bitp.calculate_separate_statistics())

#for message in bitp.get_messages_parity_alterated():
    #print(len(message))

print("Longitud de todos los mensajes")
for message in bitp.get_messages_parity_alterated():
    print(len(message))

bitp.test_histogram_plot()



#Testing
bitp = Bit_paridad_javi(20, 40, 5, 1)
print("\n")
print("Mensajes generados: {}".format(len(bitp.get_messages_parity_alterated())))
print("1-> Las longitudes de los grupos de mensajes generados son:\n {}".format(bitp.get_length_group_messages()))
print("\n\n")
print("2-> Las longitudes(simplificadas) de los grupos de mensajes generados son:\n {}".format(bitp.get_length_group_messages_simplified()))
print("\n\n")
print("3--> Las probabilidades generales son: {}".format(bitp.get_probabilities()))
print("\n\n")
print("4--> Las probabilidades por cada grupo de longitud n son:\n {}".format(bitp.calculate_separate_statistics()))

