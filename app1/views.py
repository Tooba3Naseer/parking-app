from django.shortcuts import render,redirect,get_object_or_404
from app1.models import parkingSlots
from . import forms
import pygal
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa

# Create your views here.
def Fpage(request):
	return render(request,'FPage.html')

def index(request):
	return render(request,'index.html')

def index2(request):
	return render(request,'index2.html')

def parkingform(request):
	form = forms.parkingForm()
	if request.method =='POST':
		form = forms.parkingForm(request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.save()
			return redirect("/index")
	template_name="form.html"
	context = {"form":form}
	return render(request,template_name,context)

def parkList(request):
	listt = parkingSlots.objects.all()
	my_dict = {'insert_me':listt}
	return render(request,'parkingList.html',context=my_dict)

def Edit_p(request, p_id):
	obj = get_object_or_404(parkingSlots,id= p_id)
	form = forms.parkingForm(None, None,instance=obj)
	if request.method == 'POST':
		form = forms.parkingForm(request.POST, request.FILES or None,instance=obj)
		if form.is_valid():
			form.save()
			return redirect("/parkinglist")
	template_name = "edit.html"
	context = {"form":form}
	return render(request,template_name,context)


def Delete_p(request, p_id):
	obj = get_object_or_404(parkingSlots,id= p_id)
	if request.method == "POST":
		obj.delete()
		return redirect("/parkinglist")
	template_name="delete.html"
	context = {"object":obj}
	return render(request,template_name,context)

def notification(request):
	objs = parkingSlots.objects.filter(limit_reached = False)
	for obj in objs:
		obj.save()
		if obj.due_time() <= obj.updated_time:
			obj.limit_reached = True
			obj.save()
	notif = parkingSlots.objects.filter(limit_reached = True, charged=False)
	context = {'insert_me': notif}
	return render(request,"notification.html",context)

def charged(request, p_id):
	obj = parkingSlots.objects.get(id= p_id)
	obj.charged = True
	obj.save()
	return render(request,"index.html")

def pdfview(request):
	cars = parkingSlots.objects.all()
	cars_total = cars.count()
	c_car = cars.filter(charged = True)
	unc_cars = cars.filter(charged = False)
	template="pdfview.html"
	context={"cars":cars,"Unchrg":unc_cars.count(),"Chrg":c_car.count(),"total":cars_total,"pagesize":'A4'}
	return render_to_pdf(template,context)

def render_to_pdf(template_src, context_dict):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))