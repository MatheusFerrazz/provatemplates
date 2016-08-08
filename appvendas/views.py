from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appvendas.forms import *
from django.forms import formset_factory
from django.http.request import QueryDict
from django.contrib import messages
from appvendas.models import *
# Create your views here..

def home(request):
    return render(request,'base.html')

#Funções produto

def home(request):
    return render(request,'base.html')

def exibirproduto(request,id_produto):

    produto=Produto.objects.get(id=id_produto)
    return render(request,'exibirproduto.html',{'produto':produto})

def produto_list(request):
    criterio = request.GET.get('criterio')

    if(criterio):
        produtos = Produto.objects.filter(descricao__contains=criterio)
    else:
        produtos = Produto.objects.all().order_by('descricao')
        criterio = ""
        # Cria o mecanimos de paginação
    paginator = Paginator(produtos, 10)
    page = request.GET.get('page')
    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    dados= {'produtos':produtos, 'criterio':criterio,'paginator':paginator,'page_obj':produtos}
    return render(request,'produto/produto_list.html',dados)

def produto_new(request):
    if(request.method=="POST"):
        form=ProdutoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
        dados = {"form":form}
        return  render(request,'produto/produto_form.html',dados)

def produto_update(request, pk):
    produto = Produto.objects.get(id=pk)
    if(request.method=="POST"):
        form=ProdutoForm(request.POST, instance=produto)
        if(form.is_valid()):
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
        dados = {"form":form,'produto':produto}
        return  render(request,'produto/produto_form.html',dados)

def produto_delete(request,pk):
    produto=Produto.objects.get(id=pk)
    try:
        produto.delete()
    except IntegrityError:
        messages.error(request, 'Produto Vinculado a uma Venda')
        return redirect('produto_list')
    return redirect('produto_list')

#Funções cliente

def cliente_list(request):
    criterio = request.GET.get('criterio')

    if(criterio):
        clientes = Cliente.objects.filter(nome__contains=criterio)
    else:
        clientes = Cliente.objects.all().order_by('nome')
        criterio = ""
    # Cria o mecanimos de paginação
    paginator = Paginator(clientes, 10)
    page = request.GET.get('page')
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

    dados= {'clientes':clientes, 'criterio':criterio,'paginator':paginator,'page_obj':clientes}
    return render(request, 'cliente/cliente_list.html', dados)


def cliente_new(request):
    if(request.method=="POST"):
        form=ClienteForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
        dados = {"form":form}
        return  render(request, 'cliente/cliente_form.html', dados)

def cliente_update(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if(request.method=="POST"):
        form=ClienteForm(request.POST, instance=cliente)
        if(form.is_valid()):
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
        dados = {"form":form,'cliente':cliente}
        return  render(request, 'cliente/cliente_form.html', dados)

def cliente_delete(request,pk):
    cliente=Cliente.objects.get(id=pk)
    try:
        cliente.delete()
    except IntegrityError:
        messages.error(request, 'Cliente Vinculado a uma Venda')
        return redirect('cliente_list')
    return redirect('cliente_list')


# Funções funcionário

def funcionario_list(request):
    criterio = request.GET.get('criterio')

    if(criterio):
        funcionarios = Funcionario.objects.filter(nome__contains=criterio)
    else:
        funcionarios = Funcionario.objects.all().order_by('nome')
        criterio = ""
    # Cria o mecanimos de paginação
    paginator = Paginator(funcionarios, 10)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios = paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)

    dados= {'funcionarios':funcionarios, 'criterio':criterio, 'paginator':paginator,'page_obj':funcionarios}
    return render(request,'funcionario/funcionario_list.html', dados)


def funcionario_new(request):
    if(request.method=="POST"):
        form=FuncionarioForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm()
        dados = {"form":form}
        return  render(request, 'funcionario/funcionario_form.html', dados)

def funcionario_update(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    if(request.method=="POST"):
        form=FuncionarioForm(request.POST, instance=funcionario)
        if(form.is_valid()):
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)
        dados = {"form":form, 'funcionario':funcionario}
        return  render(request, 'funcionario/funcionario_form.html', dados)

def funcionario_delete(request,pk):
    funcionario=Funcionario.objects.get(id=pk)
    try:
        funcionario.delete()
    except IntegrityError:
        messages.error(request, 'Funcionário Vinculado a uma Venda')
        return redirect('funcionario_list')
    return redirect('funcionario_list')

# Funções unidade

def unidade_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        unidades=Unidade.objects.filter(descricao__contains=criterio).order_by('descricao')
    else:
        unidades=Unidade.objects.all().order_by('descricao')
        criterio=""
    #Cria o mecanimos de paginação
    paginator=Paginator(unidades,10)
    page=request.GET.get('page')
    try:
        unidades=paginator.page(page)
    except PageNotAnInteger:
        unidades=paginator.page(1)
    except EmptyPage:
        unidades=paginator.page(paginator.num_pages)

    dados={'unidades':unidades,'criterio':criterio,'paginator':paginator,'page_obj':unidades}
    return render(request, 'unidade/unidade_list.html', dados)

def unidade_detail(request, pk):
    unidade=Unidade.objects.get(id=pk)
    return render(request, 'unidade/unidade_detail.html', {'unidade':unidade})

def unidade_new(request):
    if (request.method=="POST"):
        form=UnidadeForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('unidade_list')
    else:
        form=UnidadeForm()
        dados={'form':form}
        return render(request, 'unidade/unidade_form.html', dados)

def unidade_update(request,pk):
    unidade=Unidade.objects.get(id=pk)
    if (request.method=="POST"):
        form=UnidadeForm(request.POST,instance=unidade)
        if (form.is_valid()):
            form.save()
            return redirect('unidade_list')
    else:
        form=UnidadeForm(instance=unidade)
        dados={'form':form,'unidade':unidade}
        return render(request, 'unidade/unidade_form.html', dados)

def unidade_delete(request,pk):
    unidade=Unidade.objects.get(id=pk)
    try:
        unidade.delete()
    except IntegrityError:
        messages.error(request, 'Unidade Vinculado a um Produto')
        return redirect('unidade_list')
    return redirect('unidade_list')

# Funções Cargo

def cargo_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        cargos=Cargo.objects.filter(descricao__contains=criterio)
    else:
        cargos=Cargo.objects.all().order_by('descricao')
        criterio=""
    #Cria o mecanimos de paginação
    paginator=Paginator(cargos,10)
    page=request.GET.get('page')
    try:
        cargos=paginator.page(page)
    except PageNotAnInteger:
        cargos=paginator.page(1)
    except EmptyPage:
        cargos=paginator.page(paginator.num_pages)

    dados={'cargos':cargos,'criterio':criterio,'paginator':paginator,'page_obj':cargos}
    return render(request, 'cargo/cargo_list.html', dados)

def cargo_new(request):
    if (request.method=="POST"):
        form=CargoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('cargo_list')
    else:
        form=CargoForm()
        dados={'form':form}
        return render(request, 'cargo/cargo_form.html', dados)

def cargo_update(request,pk):
    cargo=Cargo.objects.get(id=pk)
    if (request.method=="POST"):
        form=CargoForm(request.POST,instance=cargo)
        if (form.is_valid()):
            form.save()
            return redirect('cargo_list')
    else:
        form=CargoForm(instance=cargo)
        dados={'form':form,'cargo':cargo}
        return render(request, 'cargo/cargo_form.html', dados)

def cargo_delete(request,pk):
    cargo=Cargo.objects.get(id=pk)
    try:
        cargo.delete()
    except IntegrityError:
        messages.error(request, 'Cargo Vinculado a um Funcionário')
        return redirect('cargo_list')
    return redirect('cargo_list')


'''
QUE DANADO É ISSO AQUI OMEEE ! ? ! ?
         _
        | |
        | |
       _| |_
       \   /
        \_/
'''
def listarvendas(request):
    vendas=Venda.objects.all()
    lista={'vendas':vendas}
    return render(request,'vendas.html',lista)

def listarclientes(request):
    clientes=Cliente.objects.all().order_by('nome')
    lista={'clientes':clientes}
    return render(request,'clientes.html',lista)

def exibircliente(request,idcliente):
    cliente=Cliente.objects.get(id=idcliente)
    contexto={'cliente':cliente}
    return render(request,'exibircliente.html',contexto)

def listarcargos(request):
    cargos=Cargo.objects.all().order_by('descricao')
    lista={'cargos':cargos}
    return render(request,'cargos.html',lista)

def listarfuncionrios(request):
    funcionarios=Funcionario.objects.all().order_by('nome')
    lista={'funcionarios':funcionarios}
    return render(request,'funcionarios.html',lista)

def exibirfuncionario(request,idfuncionario):
    funcionario=Funcionario.objects.get(id=idfuncionario)
    contexto={'funcionario':funcionario}
    return render(request,'exibirfuncionario.html',contexto)
