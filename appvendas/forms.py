from django.forms import ModelForm

from appvendas.models import *

class UnidadeForm(ModelForm):
   class Meta:
       model=Unidade
       fields=('descricao','sigla')

class ProdutoForm(ModelForm):
    class Meta:
        model= Produto
        fields=('descricao','valorUnitario','unidade')

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        fields=('__all__')

class CargoForm(ModelForm):
    class Meta:
        model= Cargo
        fields=('__all__')

class FuncionarioForm(ModelForm):
    class Meta:
        model=Funcionario
        fields=('nome','telefone','email','cargo','matricula')


