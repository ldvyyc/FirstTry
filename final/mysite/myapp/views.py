from django.shortcuts import render,redirect
from myapp.models import DataList
from django.db.models import Q
from django.core.paginator import Paginator
import time
# Create your views here.

def ShowContent(request):
    return redirect("/content/0")

def NoneToShowContent(request):
    return redirect("/content/0")

def ShowFirstAuthorList(request):
    db = DataList.objects.order_by("up主id").distinct()
    dc = []
    datalists = []
    for data in db:
        if data.up主id in datalists:
            continue
        else:
            datalists.append(data.up主id)
            dc.append(data)
    dc = dc[0:30]
    return render(request, 'AuthorList.html', {'data': dc})

def TurnTo(request,Search_ID):
    if request.method == "POST":
        get_page = request.POST.get("pagee")
        get_page = int(get_page)
        pageto = get_page*30 - 30
        pageto = str(pageto)
        return redirect("/content/"+pageto)
    Search_ID = int(Search_ID)
    db=DataList.objects.all()[Search_ID:Search_ID+30]
    PageNum = int(Search_ID/30 + 1)
    if PageNum==1:
        return render(request, 'contentFirstPage.html', {'data': db, 'page': PageNum})
    if PageNum==2:
        return render(request, 'contentSecondPage.html', {'data': db, 'page': PageNum})
    if PageNum==3:
        return render(request, 'contentThirdPage.html', {'data': db, 'page': PageNum})
    if PageNum==166:
        return render(request, 'contentLastPageUp2.html', {'data': db, 'page': PageNum})
    if PageNum==167:
        return render(request, 'contentLastPageUp1.html', {'data': db, 'page': PageNum})
    if PageNum==168:
        return render(request, 'contentLastPage.html', {'data': db, 'page': PageNum})
    else:
        Page_id = PageNum*30 - 30
        Pageup1 = PageNum-1
        PageUp1_id = Pageup1*30 - 30
        Pagedown1 = PageNum+1
        Pagedown1_id = Pagedown1*30 - 30
    return render(request,'content.html',{'data':db, 'pagenow':PageNum, 'pagenow_id':Page_id, 'pageup1': Pageup1, 'pageup1_id': PageUp1_id, 'pagedown1': Pagedown1, 'pagedown1_id':Pagedown1_id})


def DetailShow(request,Search_ID):
    Search_ID = int(Search_ID)
    db = DataList.objects.get(id=Search_ID)
    return render(request, 'Detail.html', {'data': db})

def AuthorLists(request,Author_ID):
    if request.method == "POST":
        get_page = request.POST.get("pagee")
        get_page = int(get_page)
        pageto = get_page*30 - 30
        pageto = str(pageto)
        return redirect("/authorlist/"+pageto)
    Author_ID = int(Author_ID)
    db = DataList.objects.order_by("up主id").distinct()
    dc = []
    datalists = []
    PageNum = int(Author_ID / 30 + 1)
    for data in db:
        if data.up主id in datalists:
            continue
        else:
            datalists.append(data.up主id)
            dc.append(data)
    dc = dc[Author_ID:Author_ID+30]
    if PageNum==1:
        return render(request, 'authorlistFirstPage.html', {'data': dc, 'page': PageNum})
    if PageNum==2:
        return render(request, 'authorlistSecondPage.html', {'data': dc, 'page': PageNum})
    if PageNum==3:
        return render(request, 'authorlistThirdPage.html', {'data': dc, 'page': PageNum})
    if PageNum==32:
        return render(request, 'authorlistLastPageUp2.html', {'data': dc, 'page': PageNum})
    if PageNum==33:
        return render(request, 'authorlistLastPageUp1.html', {'data': dc, 'page': PageNum})
    if PageNum==34:
        return render(request, 'authorlistLastPage.html', {'data': dc, 'page': PageNum})
    else:
        Page_id = PageNum*30 - 30
        Pageup1 = PageNum-1
        PageUp1_id = Pageup1*30 - 30
        Pagedown1 = PageNum+1
        Pagedown1_id = Pagedown1*30 - 30
    return render(request, 'AuthorList.html', {'data': dc, 'pagenow':PageNum, 'pagenow_id':Page_id, 'pageup1': Pageup1, 'pageup1_id': PageUp1_id, 'pagedown1': Pagedown1, 'pagedown1_id':Pagedown1_id})

def AuthorShow(request,Search_Author):
    Search_Author = str(Search_Author)
    # da = DataList.objects.get(up主名称=Search_Author)
    # A_name = da.up主名称
    # A_ID = da.up主id
    # A_des = da.up主介绍
    # A_fol = da.up主关注人数
    # A_Img = da.up主头像
    db = DataList.objects.filter(up主名称=Search_Author)
    for i in db:
        A_name = i.up主名称
        A_ID = i.up主id
        A_des = i.up主介绍
        A_fol = i.up主关注人数
        A_Img = i.up主头像
        break
    return render(request, 'Author.html', {'data': db,'namee': A_name,'idd': A_ID, 'dess': A_des, 'foll': A_fol, 'imgg': A_Img})

def Search_base(request):
    return render(request, 'Search_base.html')

global video_name
global dd
global timelapse
global cnt
global page

def Search_content(request):
    if request.method == "GET":
        return render(request, 'Search_Video.html')
    elif request.method == "POST":
        start = time.perf_counter()
        get_videos = request.POST.get("video_")
        get_videos = str(get_videos)
        global video_name
        video_name = get_videos
        if get_videos is not None:
            db = DataList.objects.filter(视频名称__contains=get_videos)
            dc = DataList.objects.filter(简介__contains=get_videos)
            global dd
            dd = []
            datalist = []
            global cnt
            cnt = 0
            for x in db:
                if x.视频名称 in datalist:
                    continue
                else:
                    datalist.append(x.视频名称)
                    dd.append(x)
                    cnt = cnt+1
            for y in dc:
                if y.视频名称 in datalist:
                    continue
                else:
                    datalist.append(y.视频名称)
                    dd.append(y)
                    cnt = cnt + 1
            end = time.perf_counter()
            global timelapse
            timelapse = end-start

            return redirect("/Search/contentshow")
            # return render(request, "ContentSearchShow.html", {'data':dd,'count':cnt,'time':timelapse, 'page':page})
        else:
            return redirect("/Search/content")
    else:
        ...

def Search_Content_Show(request):
    if request.method == "POST":
        get_page = request.POST.get("pagee")
        get_page = str(get_page)
        return redirect("/Search/contentshow?page="+get_page)

    paginator = Paginator(dd, 30)
    page_num = int(request.GET.get('page', 1))
    global page
    page = paginator.page(page_num)
    tot = paginator.num_pages
    totUp1 = tot - 1
    totUp2 = tot - 2
    totUp3 = tot - 3
    totUp4 = tot - 4
    return render(request, "ContentSearchShow.html", {'data': dd, 'count': cnt, 'time': timelapse, 'page': page, 'Up1': totUp1, 'Up2': totUp2, 'Up3': totUp3, 'Up4': totUp4, 'tot': tot, 'video_name': video_name})

def Search_Content_Show_Pages(request,pages):
    paginator = Paginator(dd, 30)
    page_num = int(pages)
    global page
    page = paginator.page(page_num)
    tot = paginator.num_pages
    totUp1 = tot - 1
    totUp2 = tot - 2
    totUp3 = tot - 3
    totUp4 = tot - 4
    return render(request, "ContentSearchShow.html", {'data': dd, 'count': cnt, 'time': timelapse, 'page': page, 'Up1': totUp1, 'Up2': totUp2, 'Up3': totUp3, 'Up4': totUp4, 'tot': tot, 'video_name': video_name})

global author_name
global de
global timelapse_author
global cntt
global Page_author

def Search_author(request):
    if request.method == "GET":
        return render(request, 'Search_Author.html')
    elif request.method == "POST":
        start = time.perf_counter()
        get_authors = request.POST.get("author_")
        get_authors = str(get_authors)
        global author_name
        author_name = get_authors
        if get_authors is not None:
            da = DataList.objects.filter(Q(up主名称__icontains=get_authors)| Q(up主id__icontains=get_authors) | Q(up主介绍__icontains=get_authors))
            global de
            de = []
            datalist = []
            global cntt
            cntt = 0
            for x in da:
                if x.up主名称 in datalist:
                    continue
                else:
                    datalist.append(x.up主名称)
                    de.append(x)
                    cntt = cntt+1
            end = time.perf_counter()
            global timelapse_author
            timelapse_author = end-start

            # return render(request, "AuthorSearchShow.html", {'data': de,'count':cnt, 'time':timelapse})
            return redirect("/Search/authorshow")
        else:
            return redirect("/Search/author")
    else:
        ...

def Search_Author_Show(request):
    if request.method == "POST":
        get_page = request.POST.get("pagee")
        get_page = str(get_page)
        return redirect("/Search/authorshow?page="+get_page)

    paginator = Paginator(de, 30)
    page_num = int(request.GET.get('page', 1))
    global Page_author
    Page_author = paginator.page(page_num)
    tot = paginator.num_pages
    totUp1 = tot - 1
    totUp2 = tot - 2
    totUp3 = tot - 3
    totUp4 = tot - 4
    return render(request, "AuthorSearchShow.html", {'data': de, 'count': cntt, 'time': timelapse_author, 'page': Page_author, 'Up1': totUp1, 'Up2': totUp2, 'Up3': totUp3, 'Up4': totUp4, 'tot': tot, 'author_name': author_name})

def Search_Author_Show_Pages(request,pages):
    paginator = Paginator(de, 30)
    page_num = int(pages)
    global Page_author
    Page_author = paginator.page(page_num)
    tot = paginator.num_pages
    totUp1 = tot - 1
    totUp2 = tot - 2
    totUp3 = tot - 3
    totUp4 = tot - 4
    return render(request, "AuthorSearchShow.html",{'data': de, 'count': cntt, 'time': timelapse_author, 'page': Page_author, 'Up1': totUp1, 'Up2': totUp2, 'Up3': totUp3, 'Up4': totUp4, 'tot': tot, 'author_name': author_name})
