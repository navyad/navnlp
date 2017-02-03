from nltk.book import *


class TestFreqDist:

	def __init__(self, text):
		self.text = text
		# freq consists of all samples of text with their corresponding counts
		self.freq_dist = FreqDist(text)

	def __has_sample(self, sample):
		return self.freq_dist.has_key(sample)

	def distinct_samples(self):
		return self.freq_dist.keys()

	def max_sample(self):
		"""
		return most occured sample
		"""
		return self.freq_dist.max()

	def hapaxes(self):
		"""
		list of samples which occured only once
		"""
		return self.freq_dist.hapaxes()

	def sample_count(self, sample):
		"""
		number of times a sample has coccured in text
		"""
		return self.freq_dist[sample] if self.__has_sample(sample) else 0

	def sample_frequency(self, sample):
		return self.freq_dist.freq(sample)
		

