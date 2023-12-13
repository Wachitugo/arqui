from django import forms
from mecanico.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['RUN', 'DV', 'PNOMBRE', 'SNOMBRE', 'APPATERNO', 'APMATERNO', 'DIRECCION', 'NOM_USUARIO', 'CONTRASENA', 'CORREO', 'NRO_TELEFONICO']
        labels = {
            'RUN': 'RUN',
            'DV': 'DV',
            'PNOMBRE': 'Primer Nombre',
            'SNOMBRE': 'Segundo Nombre',
            'APPATERNO': 'Apellido Paterno',
            'APMATERNO': 'Apellido Materno',
            'DIRECCION': 'Dirección',
            'NOM_USUARIO': 'Nombre de Usuario',
            'CONTRASENA': 'Contraseña',
            'CORREO': 'Correo Electrónico',
            'NRO_TELEFONICO': 'Teléfono',
        }
        widgets = {
            'CONTRASENA': forms.PasswordInput(),
        }

