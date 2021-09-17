from django.shortcuts import render,HttpResponse
import joblib
# Create your views here.
model = joblib.load('student_mark_predicted.pkl')
print(model)

def home(request):
	return render(request,'student_mark/home.html')

def predict(request):
	if request.method=="POST":
		number = request.POST.get('number')
		output = model.predict([[number]])[0][0].round(2)
	return render(request,'student_mark/home.html',{'number':number,'output':output})
