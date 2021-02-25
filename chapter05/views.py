from django.shortcuts import render

# Create your views here.
def work01(request):
    context = {
        "title" : "ワーク01",
        "links" : {
            "Youtube" : "https://www.youtube.com/",
            "Amazon" : "https://www.amazon.co.jp/",
            "Instagram" : "https://www.instagram.com/",
        }
    }
    return render(request, "chapter05/work01.html", context)


def work02(request):
    context = {
        "title" : "ワーク02",
    }
    return render(request, "chapter05/work02.html", context)


def work03a(request):
    context = {
        "title" : "ワーク03a"
    }
    return render(request, "chapter05/work03a.html", context)


def work03b(request):
    context = {
        "title" : "ワーク03b"
    }
    
    # GETパラメータの取得
    name = request.GET["name"]
    age = request.GET["age"]
    
    # GETパラメータを辞書にする
    data = {
        "name" : name,
        "age" : age,
    }
    
    # GETパラメータの代入
    context["data"] = data
    return render(request, "chapter05/work03b.html", context)


def work04a(request):
    context = {
        "title" : "ワーク04a"
    }
    return render(request, "chapter05/work04a.html", context)


def work04b(request):
    context = {
        "title" : "ワーク04b"
    }
    
    data = {
        "name" : "",
        "age" : "",
    }
    
    # GETパラメータの取得
    if "name" in request.GET :
        data["name"] = request.GET["name"]
    if "age" in request.GET :
        data["age"] = request.GET["age"]

    # GETパラメータの代入
    context["data"] = data
    return render(request, "chapter05/work04b.html", context)


def work05a(request):
    context = {
        "title" : "ワーク05a"
    }
    return render(request, "chapter05/work05a.html", context)


def work05b(request):
    context = {
        "title" : "ワーク05b"
    }
    
    data  = {
        "name" : "",
        "age" : "",
    }
    # POSTパラメータの取得
    if "name" in request.POST :
        data["name"] = request.POST["name"]
    if "age" in request.POST :
        data["age"] = request.POST["age"]
    
    # POSTパラメータの代入
    context["data"] = data
    return render(request, "chapter05/work05b.html", context)


def work06(request):
    context = {
        "title" : "ワーク06"
    }

    data  = {
        "name" : "",
        "age" : "",
    }
    if request.method == "POST" :
        # POSTパラメータがあれば、代入する
        if "name" in request.POST :
            data["name"] = request.POST["name"]
        if "age" in request.POST :
            data["age"] = request.POST["age"]
    
    # 代入
    context["data"] = data
    return render(request, "chapter05/work06.html", context)


def work07(request):
    context = {
        "title" : "ワーク07"
    }

    data  = {
        "age" : "",
    }
    if request.method == "POST" :
        # POSTパラメータがあれば、代入する
        if "age" in request.POST :
            data["age"] = int(request.POST["age"])
    
    # 代入
    context["data"] = data
    return render(request, "chapter05/work07.html", context)


def work08(request, name):
    context = {
        "title" : "ワーク08",
        "data" : {
            "name" : name,
        },
    }
    return render(request, "chapter05/work08.html", context)


def work09(request, name, age):
    context = {
        "title" : "ワーク09",
        "data" : {
            "name" : name,
            "age" : age,
        },
    }
    return render(request, "chapter05/work09.html", context)


def work10(request):
    context = {
        "title" : "ワーク10",
    }
    
    data = {
        "music" : "",
        "movie" : "",
    }
    
    if request.method == "POST" :
        if "music" in request.POST :
            data["music"] = request.POST["music"]
        if "movie" in request.POST :
            data["movie"] = request.POST["movie"]
    
    context["data"] = data
    return render(request, "chapter05/work10.html", context)


def work11(request):
    context = {
        "title" : "ワーク11",
    }
    
    data = {
        "name" : "",
        "score" : "",
    }
    
    if request.method == "POST" :
        if "name" in request.POST :
            data["name"] = request.POST["name"]
        if "score" in request.POST :
            data["score"] = int(request.POST["score"])
    
    context["data"] = data
    return render(request, "chapter05/work11.html", context)

