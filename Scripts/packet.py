
class Attribute(object):
	def __init__(self, attr):
		self.description = ""
		self.type = ""
		if 'description' in attr:
			self.description = attr['description']
		if 'type' in attr:
			self.type = attr
		else:
			raise TypeError('Type attribute not defined')
			
class Packet(object):
	def __init__(self, pkt):
		self.