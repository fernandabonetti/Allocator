import random
import numpy as np
import logging
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class DQNAgent():

	def __init__(self, state_size, action_size, a, b, peak):
		self.state_size = state_size
		self.action_size = action_size
		self.replay_memory = deque(maxlen=1000)

		# Discount and Learning Rate
		self.gamma = 0.95
		self.alpha = 0.001
		self.tau = 0.01

		self.epsilon = 0.1
		self.epsilon_decay = 0.999
		self.epsilon_min = 0.01

		self.model = self._build_model()
		#self.model.load_weights("model_output/weights_850.hdf5")
		self.target_model = self._build_model()

	def _build_model(self):
		model = Sequential()
		model.add(Dense(70, input_shape=(6,), activation='relu'))
		model.add(Dense(100, activation='relu')) 
		model.add(Dense(self.action_size, activation='linear')) # 100 actions on output layer
		model.compile(loss='mse', optimizer=Adam(lr=self.alpha))
		return model

	def store_experience(self, state, action, reward, next_state, done):
		self.replay_memory.append((state, action, reward, next_state, done))
			
	def sample_action(self, state):
		if self.epsilon >= np.random.rand():
			return random.randrange(self.action_size)
		action_values = self.model.predict(state)
		return np.argmax(action_values[0])  

	def replay(self, batch_size): 
		minibatch = random.sample(self.replay_memory, batch_size) 
		for state, action, reward, next_state, done in minibatch:
			target = self.target_model.predict(state)
			if done:
				target[0][action] = reward
			else:			
				q_future = np.amax(self.model.predict(next_state)[0])
				target[0][action] = reward + q_future * self.gamma
			history = self.model.fit(state, target, epochs=1, verbose=0)
			print(history.history['loss'])
			 
		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay

	def target_train(self):
		online_weights = self.model.get_weights()
		target_weights = self.target_model.get_weights()
		for i in range(len(target_weights)):
			target_weights[i] = online_weights[i] * self.tau + (1 - self.tau) * target_weights[i]
		self.target_model.set_weights(target_weights)
	
	# Load previously trained weights from HDF5 file
	def load(self, name):
		self.model.load_weights(name)

	def save(self, name):
		self.model.save_weights(name) 
