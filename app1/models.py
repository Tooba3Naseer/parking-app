from django.db import models
import datetime as dt

# Create your models here.


class parkingSlots(models.Model):
	choices_time = [(1,"10 sec"),(2,"15 min"), (3,"20 min"), (4,"1 hour")]
	slot_no = models.CharField(max_length = 20)
	car_no = models.CharField(max_length = 20)
	start_time = models.DateTimeField(auto_now_add = True)
	updated_time = models.DateTimeField(auto_now = True)
	charged = models.BooleanField(default = False)
	limit_reached = models.BooleanField(default = False)
	limit = models.PositiveIntegerField(choices= choices_time, default=1)

	def due_time(self):
		if self.limit == 1:
			due = self.start_time + dt.timedelta(seconds=10)
		elif self.limit == 2:
			due = self.start_time + dt.timedelta(minutes=15)
		elif self.limit == 3:
			due = self.start_time + dt.timedelta(minutes = 20)
		else:
			due = self.start_time + dt.timedelta(hours = 1)
		return due
