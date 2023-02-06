from django.forms import ModelForm
from .models import Employee

#VINCULACION DE NUESTRO FORMULARIO A NUESTRO MODELO
class EmployeeForm(ModelForm):
    class Meta:
        model= Employee
        fields= '__all__' # Esto hace referencia a los campos['name', 'last_name', 'email']
        # exclude= ('email',)  Excluye el elemento email
    

        
