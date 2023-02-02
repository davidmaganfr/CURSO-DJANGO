from django import forms

class CommentForm(forms.Form):
    name= forms.CharField(label='Escribe tu nombre:', max_length=100, help_text='100 caracteres maximo')
    url= forms.URLField(label='Tu sitio web', required=False, initial='http://')
    comment= forms.CharField(label='Comentario')

class ContactForm(forms.Form):
    name= forms.CharField(label='Nombre', max_length=50, widget= forms.TextInput(attrs={'class':'form-control'})) #Esto permite dar estilo a esta clase
    email= forms.EmailField(label='Email', max_length=50, widget= forms.EmailInput(attrs={'class':'form-control'}))
    messagge= forms.CharField(label='Mensaje', widget= forms.Textarea(attrs={'class':'form-control'}))
    
    def clean_name(self): #AÑADE VALIDACIONES EXTRA AL NOMBRE
        name= self.cleaned_data.get('name')
        if name != 'Open':
            raise forms.ValidationError('Tan solo el valor Open esta permitido')
        else:
            return name