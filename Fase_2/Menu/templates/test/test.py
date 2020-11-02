from django.test import SimpleTestCase
from Menu.forms import Contacto

class testFormulario(SimpleTestCase):
    
    def test_Contacto_valid_data(self):
        form=Contacto(data={
            'email':'uwuwuwu@ggmail.com'    
            'nombre':'el tunas'
            'apellido':'el mufas'
            'fono':'+569696969'
            'direccion':'calle falsa 123'
            'fecha':'01-11-2020'
            'motivo':'Problemas con tu Pedido'
        })
        self.assertTrue(form.is_valid())


    def test_Contacto_no_data(sellf):
        form=Contacto(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)