import random

class sirmodel:
    def __init__(self, population, initial_infected, gamma, beta):
        self.p=population
        self.i=initial_infected
        self.gamma=gamma #recovery rate
        self.beta=beta #infection probability
        self.s=self.p-self.i
        self.r=0
        #define the array by using []
        self.i_values=[self.i]
        self.s_values=[self.s]
        self.r_values=[self.r]
    # code to proccess the data as a model
    def run(self,days):
        for i in range(days):
            new_i=self.s * self.beta * self.i /self.p
            new_r=self.i * self.gamma
            #now calculate the updating number of the 3 sorts of people: infected, recoverd and suspecticle
            self.s -= new_i
            self.i += new_i-new_r
            self.r += new_r
            #use the append() command to add the elements into the array
            self.i_values.append(self.i)
            self.s_values.append(self.s)
            self.r_values.append(self.r)
    #plot the image
    def print(self):
        import matplotlib.pyplot as plt
        plt.plot(self.i_values,label='infected')
        plt.plot(self.s_values,label='suspectible')
        plt.plot(self.r_values,label='recoveries')
        plt.xlabel('Days')
        plt.ylabel('number of people')
        plt.title('sir model')
        plt.legend()
        plt.savefig("/Users/rickyh/Desktop/sirfigure.png",format="png")
        plt.show()

population=10000
initial_infected=1
gamma=0.05 
beta=0.3
days=1000

model=sirmodel(population, initial_infected,gamma,beta)
model.run(days)
model.print()



            

        
