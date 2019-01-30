import gym
env = gym.make('MyEnv-v0')

while(1): 
	observation = env.reset()
	env.render() 
'''for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(reward) 
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break '''
