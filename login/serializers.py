from rest_framework import serializers
from .models import UserScheduleDB


class UserScheduleSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserScheduleDB
        fields = ('student_code', 'time', 'A', 'B', 'C', 'D', 'E', 'F', 'time50', 'A50', 'B50','C50','D50','E50','F50')

    def create(self, data):
        return UserScheduleDB.objects.create(**data)