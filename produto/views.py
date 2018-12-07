from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm


@login_required
def produto_list(request):
    lista_produto = Produto.objects.all()
    return render(request, 'produto.html', {'lista_produto': lista_produto})


@login_required
def novo_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produto_list')

    return render(request, 'produto_formulario.html', {'form': form})


@login_required
def produto_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produto_list')

    return render(request, 'produto_formulario.html', {'form': form})


@login_required
def produto_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')

    return render(request, 'produto_confirmar_exclusao.html', {'produto': produto})