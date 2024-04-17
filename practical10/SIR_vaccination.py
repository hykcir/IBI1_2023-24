import random
import matplotlib.pyplot as plt
class sirmodel:
    def __init__(self, population, initial_infected, gamma, beta, vaccination_rate):
        self.p=population
        self.i=initial_infected
        self.gamma=gamma #recovery rate
        self.beta=beta # infection probability
        self.v=self.p * vaccination_rate #vaccinated people
        self.s=self.p-self.i-self.v
        self.r=0
        #define an array
        self.i_values=[self.i]
        
    #code to proce the data as a model
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
            
    
def plot_models(models):
    #given there are multiple situations to illustrate in one image, there will be more than 1 "model"
    for model in models:
        plt.plot(model.i_values,label=f'vaccination_rate:{model.v * 100/model.p}%') # make sure the label matches the figure it represent (which vaccination rate) well
        
       

population=10000
initial_infected=1
gamma=0.05 
beta=0.3 
days=1000

models=[]
for percent in range(0,101,10):# the chosen percentage start at 0 and increase at a ladder of 10%
    vaccination_rate=percent/100
    model=sirmodel(population, initial_infected, gamma,beta, vaccination_rate)
    model.run(days) 
    models.append(model) # to ensure all the curves appear on the same image
    
plot_models(models)
plt.xlabel('Days')
plt.ylabel('number of people')
plt.title('sir model under different vaccination rate ')
plt.legend()
plt.savefig("/Users/rickyh/Desktop/sir_vaccination_rate.png",format="png")
plt.show()


            

        
