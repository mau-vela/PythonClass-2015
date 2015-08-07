class Clock(object):
	def __init__(self, hour, minutes=0):
		self.minutes = minutes
		self.hour = hour
		
	@classmethod
	def at(cls, hour, minutes=0):
		return cls(hour, minutes)
		
	def __str__(self):
		if self.hour<10: hour2="0"+str(self.hour)
		else: hour2=str(self.hour)
		if self.minutes<10: minute2="0"+str(self.minutes)
		else: minute2=str(self.minutes)
		return '%s:%s' % (hour2, minute2)
		
	def __add__(self,minutes):
		sum_minutes=minutes+self.minutes
		minutes3=sum_minutes%60
		hour3=int(sum_minutes/60)+self.hour
		if hour3>23: hour3=24*int(hour3/24)-int(hour3/24)*24+(hour3%24)
		return Clock(hour3,minutes3)
		
	def __sub__(self,minutes):
		return self + (-1)*minutes
    
    def __eq__(self, other):
    
    def __ne__(self, other):
