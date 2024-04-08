from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def secondpage(request):
    return render(request, 'main/secondpage.html')

def mainpage(request):
    context = {
        'generation': 12,
        'elements': ['Model', 'Templete', 'View', 'URLconf'],
        'info':{'데이터베이스에 저장되는 데이터', '사용자에게 보여지는 부분', '웹 요청을 받고 전달받은 데이터들을 해당 어플리케이션의 로직으로 가공, 템플릿에 결과 전송', 'view와 template을 이어주는 역할'}
    }
    return render(request, 'main/mainpage.html', context)