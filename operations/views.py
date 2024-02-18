from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HelloWorldView(View):
    
    def get(self,request,*args,**kwargs):
         
        print("hello world")
        return render(request,"helloworld.html")
    
class GoodMorningView(View):
     
    def get(self,request,*args,**kwargs):
          
        print("good morning")
        return render(request,"gm.html")
    
class GoodAfterNoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"ga.html")
    




class AdditionView(View):


    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)    
        print(result)
        return render(request,'add.html',{"output":result})


    
class SubtractionView(View):


    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    

    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print(result)
        return render(request,'sub.html',{"output":result})
    




class MultiplicationView(View):


    def get(self,request,*args,**kwargs):
        return render(request,'mul.html')
    

    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print(result)
        return render(request,'mul.html',{"output":result})
    

    
class DivisionView(View):


    def get(self,request,*args,**kwargs):
        return render(request,'div.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        print(result)
        return render(request,'div.html',{"output":result})
    


    
class CubeView(View):


    def get(self,request,*args,**kwargs):
        return render(request,'cube.html')
    

    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        result=int(n)**3
        print(result)
        return render(request,'cube.html',{"output":result})
        

class FactorialView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'fact.html')
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        fact=1
        for i in range(1,int(n)+1):
            fact=fact*i
        print(fact)
        return render(request,'fact.html',{"output":fact})



# leapyear

class LeapyearView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'leap.html')
    
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))
        if((year%100==0 and year%400==0) or (year%100!=0 and year%4==0)):
            result=f"{year} is leap year"
        else:
            result=f"{year} is not leap year"
        return render(request,'leap.html',{"output":result})


class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')
    



class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'bmi.html')
    
    def post(self,request,*args,**kwargs):
        weight=int(request.POST.get("weight"))
        height_cm=int(request.POST.get("height"))
        bmi=weight/(height_cm/100)**2
        return render(request,'bmi.html',{"output":bmi})
    


# oddeven

class OddEvenView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'oddeven.html')
    
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        if n%2==0 :
            result=f"{n} is even"
        else:
            result=f"{n} is odd"
        return render(request,'leap.html',{"output":result})

    
    
# prime
class PrimeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'prime.html')
    
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        for i in range(2,n):
            if n%i==0:
                result=f"{False} ;not prime"
                break
            else:
                result=f"{True} ; is prime"
        return render(request,'leap.html',{"output":result})


class EmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"emi.html")
    def post(self,request,*args,**kwargs):
        p=int(request.POST.get("amount"))
        r=int(request.POST.get("interest"))/1200
        n=int(request.POST.get("tenure"))*12
        emi=p*r*(1+r)**n/((1+r)**n-1)
        total_payable_amount=emi*n
        total_interest_payable=total_payable_amount-p
        print(total_payable_amount)
        print(total_interest_payable)
        return render(request,"emi.html",{"emi":emi,"total_amount":total_payable_amount,"interest_amount":total_interest_payable})