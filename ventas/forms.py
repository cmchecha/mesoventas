from django import forms
from django.contrib.auth.models import User
from ventas.models import Producto, Cliente, Venta, DetalleVenta
from django.forms import ModelForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio','existencias',)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'nit','direccion',)

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('cliente', 'productos',)
        
        def __init__ (self, *args, **kwargs):
            super(VentaForm, self).__init__(*args, **kwargs)
            self.fields["productos"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["productos"].help_text = "Ingrese productos: "
            self.fields["productos"].queryset = Producto.objects.all()