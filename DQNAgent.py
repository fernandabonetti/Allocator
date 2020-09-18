import random
import numpy as np
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

		self.epsilon = 1.0
		self.epsilon_decay = 0.995
		self.epsilon_min = 0.01

		self.model = self._build_model()
		self.model.summary()
		#self.target_model = self._build_model()

	def _build_model(self):
		model = Sequential()
		model.add(Dense(6, input_shape=(6,), activation='relu'))
		model.add(Dense(49, activation='relu')) 
		model.add(Dense(self.action_size, activation='linear')) # 49 actions on output layer
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
			target = reward
			 
			if not done:
				target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
			q_future = self.model.predict(state)
			q_future[0][action] = target
			self.model.fit(state, q_future, epochs=1, verbose=0) 

		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay

	def target_train(self):
		weights = self.model.get_weights()
		self.target_model.set_weights(weights)
	
	# Load previously trained weights from HDF5 file
	def load(self, name):
		self.model.load_weights(name)

	def save(self, name):
		self.model.save_weights(name) 