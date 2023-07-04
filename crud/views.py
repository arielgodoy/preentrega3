from django.shortcuts import render, redirect
from .models import Documento,Propiedades,Propietario
from .forms import DocForm,BuscaDocs,PropForm,BuscaProps,PropietarioForm,BuscaPropietario

# Create your views here.
def inicio(request):   
    return render(request,"base.html")  



def listarPropietarios(request):
    form = BuscaPropietario(request.GET)
    if form.is_valid():
        filtro = form.cleaned_data['nombre']        
        propietarios = Propietario.objects.filter(nombre__icontains=filtro)        
    else:
        print("No es Valido ")    
    return render(request,"listapropietarios.html",{'form':form,'propietarios':propietarios}) 



def listarDocs(request):
    form = BuscaDocs(request.GET)
    if form.is_valid():
        filtro = form.cleaned_data['titulo']        
        docs = Documento.objects.filter(titulo__icontains=filtro)        
    else:
        print("No es Valido ")    
    return render(request,"listadocs.html",{'form':form,'docs':docs}) 

def listarPropiedades(request):
    form = BuscaProps(request.GET)
    if form.is_valid():
        filtro = form.cleaned_data['rol']        
        props = Propiedades.objects.filter(rol__icontains=filtro)        
    else:
        print("No es Valido ")    
    return render(request,"listapropiedades.html",{'form':form,'props':props}) 





def creaDocs(request):  
    if request.method == "POST":  
        form = DocForm(request.POST)  
        if form.is_valid():  
            try:  
                if form.save():
                    print("todo ok 2")
                model = form.instance        

                return redirect('listarDocs')  
            except:  
                pass  
    else:  
        form = DocForm()  
    return render(request,'creadoc.html',{'form':form})  

def creaPropiedades(request):  
    if request.method == "POST":  
        form = PropForm(request.POST)  
        if form.is_valid():  
            try:  
                if form.save():
                    print("todo ok 2")
                model = form.instance       

                return redirect('listarPropiedades')  
            except:  
                pass  
    else:  
        form = PropForm()  
    return render(request,'creaPropiedad.html',{'form':form}) 






def creaPropietario(request):  
    if request.method == "POST":  
        form = PropietarioForm(request.POST)  
        if form.is_valid():  
            try:  
                if form.save():
                    print("todo ok 2")
                model = form.instance       

                return redirect('listarPropietarios')  
            except:  
                pass  
    else:  
        form = PropietarioForm()  
    return render(request,'creaPropietario.html',{'form':form})  



def updateDocs(request, id):  
    doc = Documento.objects.get(id=id)
    form = DocForm(initial={'titulo': doc.titulo, 'descripcion': doc.descripcion, 'autor': doc.autor, 'anio': doc.anio})
    if request.method == "POST":  
        form = DocForm(request.POST, instance=doc)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('listarDocs')  
            except Exception as e: 
                pass    
    return render(request,'docupdate.html',{'form':form})  

def updatePropiedades(request, id):  
    prop = Propiedades.objects.get(id=id)
    form = PropForm(initial={'rol': prop.rol, 'direccion': prop.direccion, 'rut': prop.rut})
    if request.method == "POST":  
        form = PropForm(request.POST, instance=prop)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('listarPropiedades')  
            except Exception as e: 
                pass    
    return render(request,'propiedadupdate.html',{'form':form})  


def updatePropietario(request, id):  
    propietario = Propietario.objects.get(id=id)
    form = PropietarioForm(initial={'nombre': propietario.nombre, 'direccion': propietario.direccion, 'fono': propietario.fono})
    if request.method == "POST":  
        form = PropietarioForm(request.POST, instance=propietario)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('listarPropietarios')  
            except Exception as e: 
                pass    
    return render(request,'propietarioupdate.html',{'form':form})  


def deleteDocs(request, id):
    doc = Documento.objects.get(id=id)
    try:
        doc.delete()
    except:
        pass
    return redirect('listarDocs')



def deletePropiedades(request, id):
    prop = Propiedades.objects.get(id=id)
    try:
        prop.delete()
    except:
        pass
    return redirect('listarPropiedades')

def deletePropietario(request, id):
    propietario = Propietario.objects.get(id=id)
    try:
        propietario.delete()
    except:
        pass
    return redirect('listarPropietarios')