from django.shortcuts import render, redirect
from excel.Forms import FileForm


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = FileForm()
    return render(request, 'excel/index.html', {'form': form})
