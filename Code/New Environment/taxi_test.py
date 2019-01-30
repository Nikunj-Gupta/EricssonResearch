import gym 
import os 
import time 

#env = gym.make('Taxi-v2') 
env = gym.make('MyTaxiEnv-v0') 

'''
env.reset() 
env.render() 
''' 
total_rewards = 0 
for i in range(100): 
	env.reset() 
	rewards = 0 
	for _ in range(100): #timesteps 
		os.system("clear") 
		env.render() 
		temp = env.step(env.action_space.sample()) # take a random action 
		taxirow, taxicol, passidx, destidx = env.decode(temp[0]) 
		print "Decoded State: ", taxirow, taxicol, passidx, destidx 
		if(temp[1] > 0): 
			rewards += temp[1] 
		if(temp[2]): 
			break 
		time.sleep(0.5) 
	total_rewards += rewards 
print "Total Rewards: ", total_rewards 


''' 
import gym 
import numpy as np 

#env = gym.make("Taxi-v2") 
env = gym.make("MyTaxiEnv-v0") 

print "State (encoded) ", env.reset() 
env.render() 
#print env.newstep(env.action_space.sample(), env.step(env.action_space.sample())) 
''' 





'''
print(state) 
taxirow, taxicol, passidx, destidx = env.decode(state)
print taxirow, taxicol, passidx, destidx 
env.render() 
print env.action_space.sample() 
'''
#	
#print env.step() 



'''
n_states = env.observation_space.n 
n_actions = env.action_space.n 

state = env.reset()
counter = 0
g = 0
reward = None
while reward != 20:
    state, reward, done, info = env.step(env.action_space.sample())
    print state, 
    print reward 
    counter += 1
    g += reward
print("Solved in {} Steps with a total reward of {}".format(counter,g))
''' 
