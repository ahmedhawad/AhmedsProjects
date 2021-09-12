import numpy as np
import matplotlib.pyplot as plt
import random
import simpy
from parameters import *
# this file creates the population class with one parent class Person, and three subclasses: 1.Uninfected 2. Infected 3. Dead


lengh_of_sim = 100  # days     #how long does the simulation last

# First number of people to infect

# number of people that are first infected by the virus, not by a person
number_of_patient_zeros = int(Population * .01)


# When someone gets infected:
# each day they are infected, the counter decreases by 1
time_at_infection = 6  # starts count down times at this time
time_to_infect_others_a = 4  # this time it infects someone
time_to_infect_others_b = 3  # this time it infects someone
time_to_recover = 2  # this time there is a chance to recover
time_to_die = 1  # at this time th person dies


# When someone new is infected:
n_to_infect = 1  # max number of people to get infected from an infected
"""infection_chance = random.choice(True,False) #50/50 chance #this coe is in #Virus.chancce_to_infect()
"""

# random.seed(42) #this will keep all randomly generated values constant, Keep this line will testing

############################################################################################################################
# "Person" parent class with 3 subclasses 1. Uninfected 2. Infected 3. Dead


class Person:
    database = []  # list of everyone in the simulation
    people = len(database)  # number of people everywhere

    def __init__(self, ID, age, pre_existing_condition, infection_status=False, alive=True, immunity=False, viremia=0, infected=0):
        """
        Are these the only things we want to be tracked?

        Immunity = True or false based on time period, 21-25 days

        Infected = []

        Viremia will be a range

        """
        # still have to add viremia, idk how it changes, int or bool?

        self.ID = ID  # Unique ID number per person
        self.age = age  # age
        self.pre_existing_condition = pre_existing_condition  # pre existing condtiiton T/F
        self.infection_status = infection_status  # T/F
        self.alive = alive  # T/F
        # T/F, after someone recovers they remain immune forever, currently
        self.immunity = immunity
        if viremia == 0:
            self.viremia = 0
        else:
            self.viremia = viremia
        self.viremia = viremia
        if infected == 0:
            self.infected = []
        else:
            self.infected = infected

        Person.database.append(self)

    @staticmethod
    def generate_pre_existing_conditions():
        """
        Assigns pre-existing conditions to the correct number of people, randomly selected
        """
        num_pre_cond = int(Pre_existing_conditions *
                           Population)  # calculates how many people need to have a pre-existing condition

        # generates list of random people to be assigned having a preexisting condition k number of times
        chosen_pre_cond_list = random.choices(
            range(1, Population + 1), k=num_pre_cond)

        # nested loop checking all instances of Person and compariing IDs to chosen IDs to to make pre_ex_cond true
        for person in Person.database:  # prints the string func of the class
            for chosen_id in chosen_pre_cond_list:
                if person.ID == chosen_id:
                    person.pre_existing_condition = True

    @staticmethod
    def assign_ages(bracket, percent):
        """
        Assigns ages based on age bracket and number of people desired per bracket

        Matches the string version of the number of desired ppl in the age, and randomly chooses a number within the bracket the amount of times wainter
        """

        if bracket == "one_ten":
            # for i in range(int(Population * percent)):
            return random.randint(1, 10)
        elif bracket == "eleven_twenty":
            # for i in range(int(Population * percent)):
            return random.randint(11, 20)
        elif bracket == "twentyone_thirty":
            # for i in range(int(Population * percent)):
            return random.randint(21, 30)
        elif bracket == "thirtyone_forty":
            # for i in range(int(Population * percent)):
            return random.randint(31, 40)
        elif bracket == "fortyone_fifty":
            # for i in range(int(Population * percent)):
            return random.randint(41, 50)
        elif bracket == "fiftyone_sixty":
            # for i in range(int(Population * percent)):
            return random.randint(51, 60)
        elif bracket == "sixtyone_seventy":
            # for i in range(int(Population * percent)):
            return random.randint(61, 70)
        elif bracket == "seventyone_eighty":
            # for i in range(int(Population * percent)):
            return random.randint(71, 80)
        elif bracket == "eightyone_ninety":
            # for i in range(int(Population * percent)):
            return random.randint(81, 90)
        elif bracket == "ninetyone_hundred":
            # for i in range(int(Population * percent)):
            return random.randint(91, 100)
        else:
            print("Error assigning age")

    @staticmethod
    def generate_population():
        """
        generates the entire population with age,


        Looks how many people in each age bracket are needed, Adds them as Uninfected class, Person.assign_ages() 
        to generate correct age, then after creating everyone, uses Person.generate_pre_existing_conditions() to add the current number of pre_ex_cond

        """
        the_id = 1  # used to make id number
        everyone_list = []  # temporary list to store all people generated

        for i in range(int(Population * one_ten)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "one_ten", one_ten), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * eleven_twenty)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "eleven_twenty", eleven_twenty), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * twentyone_thirty)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "twentyone_thirty", twentyone_thirty), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * thirtyone_forty)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "thirtyone_forty", thirtyone_forty), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * fortyone_fifty)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "fortyone_fifty", fortyone_fifty), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * fiftyone_sixty)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "fiftyone_sixty", fiftyone_sixty), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * sixtyone_seventy)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "sixtyone_seventy", sixtyone_seventy), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * seventyone_eighty)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "seventyone_eighty", seventyone_eighty), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * eightyone_ninety)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "eightyone_ninety", eightyone_ninety), False, False, True, 0, 0))
            the_id += 1

        for i in range(int(Population * ninetyone_hundred)):
            everyone_list.append(Uninfected(the_id, Person.assign_ages(
                "ninetyone_hundred", ninetyone_hundred), False, False, True, 0, 0))
            the_id += 1
        # gives the correct number people a preexisting condition
        Person.generate_pre_existing_conditions()

    @staticmethod
    def print_databases():
        """
        Prints all the subclasses data bases, not everyoien at once
        """

        print("\nSimulation Test:", Title)
        print("Uninfected:")
        for i in Uninfected.uninfected_database:  # prints the string func of the class
            print(i)
        print("Infected:")
        for i in Infected.infected_database:  # prints the string func of the class
            print(i)
        print("Dead:")
        for i in Dead.dead_database:
            print(i)

        # print("Entire Population:")
        # for i in Person.database:
        #     print(i)

    @staticmethod
    def database_quantaties():
        """
        returns data base quantites for each subclass
        """

        return ("Uninfected:{}\nInfected:{}\nDead:{}\n".format(len(Uninfected.uninfected_database), len(Infected.infected_database), len(Dead.dead_database)))

    @staticmethod
    def print_database_quantaties():
        """
        Prints all the subclasses data bases, not everyoien at once
        """

        print("Uninfected:{}\nInfected:{}\nDead:{}\n".format(len(
            Uninfected.uninfected_database), len(Infected.infected_database), len(Dead.dead_database)))

    @staticmethod
    def who_infected_who():
        """
        prints a list of which person ID infected wich person ID
        """
        print("\nWho Infected Who:")
        for person in Person.database:
            if len(person.infected):
                print("{} infected : {}".format(person.ID, person.infected))

    def __str__(self):
        """
        returnts all parameters for Person class
        """

        return "ID: {} Age: {} Pre-Cond: {} Inf_Status:{} Alive:{} Immunity:{} Viremia:{} Infected:{}".format(self.ID, self.age, self.pre_existing_condition, self.infection_status, self.alive, self.immunity, self.viremia, self.infected)


class Uninfected(Person):
    """
    Stores everyone alive uninfected
    """
    uninfected_database = []
    uninfected_people = len(uninfected_database)

    def __init__(self, ID, age, pre_existing_condition, infection_status=False, alive=True, immunity=False, viremia=0, infected=0):
        super().__init__(ID, age, pre_existing_condition,
                         infection_status, alive, immunity, viremia, infected)
        Uninfected.uninfected_database.append(self)


class Infected(Person):
    """
    Stores everyone infected alive

    Has parameter time_lieft, starts at time "time_at_infection", used to execute infections, recovery, death at different times. 
    """
    infected_database = []
    infected_people = len(infected_database)

    def __init__(self, ID, age, pre_existing_condition, infection_status=False, alive=True, immunity=False, viremia=0, infected=0, time_left=time_at_infection):
        super().__init__(ID, age, pre_existing_condition,
                         infection_status, alive, immunity, viremia, infected)
        Infected.infected_database.append(self)
        self.time_left = time_left


class Dead(Person):
    """
    stores all dead peeple
    """
    dead_database = []
    uninfected_people = len(dead_database)

    def __init__(self, ID, age, pre_existing_condition, infection_status=False, alive=True, immunity=False, viremia=0, infected=0):
        super().__init__(ID, age, pre_existing_condition,
                         infection_status, alive, immunity, viremia, infected)
        Dead.dead_database.append(self)


############################################################################################################################

class Virus(object):
    """

    This class is what does the infecting. Infecting happens in Virus.run()

    Stores patient zero
    """

    patient_zero = []

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())  # starts the whole process

    def run(self):
        """
        Generates population

        Infects patient zero(s)


        Runs Virus.while_infected()

        """
        next_day = 1  # move this number of days

        Person.generate_population()  # generates the entire population

        # loops n_to_infect times to infect the first people
        for i in range(number_of_patient_zeros):
            Virus.first_to_be_infected()

        while True:
            print("Day:{}\n{}".format(self.env.now, Person.database_quantaties()))

            print(self.env.now)

            Virus.while_infected()

            # Person.print_databases()

            yield self.env.timeout(next_day)  # moves "next_day" days at a time

    @staticmethod
    def infect(given_id, infector_id=None, is_patient_zero=False):  # uninfected_to_infected
        """
        Moves someone from Uninfected to Infected

        Removes them from person, then readds them to eliminate duplicates

        infector_id is the person who is doing the infecting, if number is present then given_id is added to infector_id's infected list. If none, nothing

        is_patient_zero is if this is the first person infected in the simulation, False does nothing, True adds the given_id to Virus.patient_zero list
        """
        # Structure:  ID, age, pre_existing_condition, infection_status, alive, immunity, viremia, infected
        for person in Uninfected.uninfected_database:
            if person.ID == given_id:
                Uninfected.uninfected_database.remove(person)
                Person.database.remove(person)
                Infected(person.ID, person.age, person.pre_existing_condition, True, person.alive,
                         person.immunity, person.viremia, person.infected, time_at_infection)
                if infector_id is not None:
                    for i in Infected.infected_database:
                        if i.ID == infector_id:
                            i.infected.append(person.ID)
        if is_patient_zero == True:
            Virus.patient_zero.append(given_id)

    @staticmethod
    def recover(given_id):  # infected_to_uninfected
        """
        Moves someone from Infected to Uninfected

        Removes them from person, then readds them to eliminate duplicates
        """
        # Structure:  ID, age, pre_existing_condition, infection_status, alive, immunity, viremia, infected
        for person in Infected.infected_database:
            if person.ID == given_id:
                Infected.infected_database.remove(person)
                Person.database.remove(person)
                Uninfected(person.ID, person.age, person.pre_existing_condition,
                           False, person.alive, True, person.viremia, person.infected)

    @staticmethod
    def kill(given_id):  # infected_to_dead
        """
        Moves someone from Infected to Uninfected

        Removes them from person, then readds them to eliminate duplicates
        """
        # Structure:  ID, age, pre_existing_condition, infection_status, alive, immunity, viremia, infected
        for person in Infected.infected_database:
            if person.ID == given_id:
                Infected.infected_database.remove(person)
                Person.database.remove(person)
                Dead(person.ID, person.age, person.pre_existing_condition,
                     person.infection_status, False, person.immunity, person.viremia, person.infected)

    @staticmethod
    def first_to_be_infected():
        """
        Chooses 1 radndom perosn to infect from uninfected list(will update to everyone alive)
        """
        # Randomly chosen for now
        # chooses n number of people from uninfected
        infect_this_person = [random.choice(Uninfected.uninfected_database)]
        for person in infect_this_person:
            Virus.infect(person.ID, None, True)

    @staticmethod
    def while_infected():
        """
        Looks at last position in Infected and when it reaches day 1
        """
        for person in Infected.infected_database:  # counts down time_left
            person.time_left -= 1  # removes 1 from time left

            if person.time_left == time_to_infect_others_a:  # if at this time, infect someone
                for i in range(n_to_infect):
                    Virus.chance_to_infect(person.ID)

            elif person.time_left == time_to_infect_others_b:  # if at this time infect someone
                for i in range(n_to_infect):
                    Virus.chance_to_infect(person.ID)

            elif person.time_left == time_to_recover:  # if at this time chance to recover
                Virus.chance_to_recover(person.ID)

            elif person.time_left == time_to_die:  # if at this time, kill
                Virus.kill(person.ID)

    @staticmethod
    def chance_to_infect(given_id):
        """
        Chooses whether 1 person will be infected or not(random not taking into account )

        If True:
            -Chooses 1 person from Uninfected.uninfected_database to infect
            -Adds newly infected person is added to the list of those the infector infected.

        If False, does nothing
        """

        infection_chance = random.choices(
            [True, False], [.5, .5])  # 51/49 chance to infect
        # chooses 1 person from uninfected
        infect_person = random.choice(Uninfected.uninfected_database)
        # probleim is infect person returns 2 values
        if infection_chance[0] == True:  # if infection chance is True,
            # infect the chosen person
            Virus.infect(infect_person.ID, given_id)

        #     for person in Infected.infected_database: #adds the newly infected person to the list that the infector infected
        #         if person.ID == given_id:
        #             person.infected.append(infect_person.id)

    @staticmethod
    def chance_to_recover(given_id):
        """
        Chooses whether person will recover or not. 

        If True, person recovers

        If False, does nothing
        """

        # 75% chance the person recovers
        infection_chance = random.choices((True, False), [.55, .45])

        if infection_chance[0] == True:
            Virus.recover(given_id)

    @staticmethod
    def practice_run():
        """

        Does some example infections roceveries and kills.
        """

        Person.generate_population()

        Virus.infect(1, None, True)  # 1 is patient zero
        Virus.infect(4, 1)  # 1 infects 4
        Virus.infect(6, 1)  # 1 infects 6
        Virus.infect(3, 4)  # 4 infects 3
        Virus.infect(17, 3)  # 3 infects 4

        Virus.kill(1)  # 1 dies
        Virus.recover(4)  # 4 recovers

        Virus.chance_to_recover(3)  # 3 is given a chance to recover
        Virus.chance_to_recover(17)  # 17 is given a chance to recover
        print(Person.print_databases())  # prints totals in each subclass


def start():
    """
    This runs the simulation
    """
    env = simpy.Environment()  # defining that env is a simpy envirnment class

    car = Virus(env)  # starts the procces of the simulation the func
    env.run(until=lengh_of_sim+1)


# Virus.practice_run()
# Person.who_infected_who()
# print(Virus.patient_zero)


############################################################################################################################
#                                                           Tests                                                          #
############################################################################################################################

#####Start Simulation#####


print("starting")

start()


print("done")


#####Practice Run#####

Virus.practice_run()

Person.who_infected_who()

print(Virus.patient_zero)


############################################################################################################################
#                                                          Graphing                                                        #
############################################################################################################################
names = ['Uninfected', 'Infected', 'Dead']
values = [len(Uninfected.uninfected_database), len(
    Infected.infected_database), len(Dead.dead_database)]

plt.figure(figsize=(10, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Simulation Plotting')  # Categorical Plotting
plt.show()  # This plots the graphs
############################################################################################################################
