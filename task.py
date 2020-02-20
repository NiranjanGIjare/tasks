class task:
	def __init__(self,identity,time_created,title,status,description="",deadline=""):
		self.identity=identity
		self.time_created=time_created
		self.title=title
		self.description=description
		self.status=status
		self.deadline=deadline
