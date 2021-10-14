from rest_framework import serializers
from snippets.models import Employee    

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_name','emp_branch','emp_salary','emp_phoneno','emp_location']

        