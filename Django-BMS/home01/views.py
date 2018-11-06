from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from home01.models import Book, Publish, Author
# 测试
def oneviews(request):

    return render(request, 'index.html')


# 查看
def lookbook(request):

    books = Book.objects.all()
    # print(books)
    # print(books.first())
    #
    return render(request,'base.html',{'books':books})

# 添加
def addbook(request):
    # 注意post都是大写
    if request.method =='POST':
        # 获取提交的数据
        title = request.POST.get('title')
        pub_date = request.POST.get('datetime')
        author_id= request.POST.get('author')
        price = request.POST.get('price')
        publish_id = request.POST.get('publishlist')
        # print(title,pub_date,author_id,price,publish_id)

        newbook = Book.objects.create(title=title,price=price,pub_date=pub_date,author_id=author_id,publish_id=publish_id)

        return redirect('/look/')

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request,'add.html',{'publish_list':publish_list,'author_list':author_list})

# 修改
def editbook(request,edit_book_id):
    # 可以修改提交，也可以不修改用原来的提交
    edit_book_obj = Book.objects.filter(pk=edit_book_id).first()

    if request.method == "POST":
        title = request.POST.get('title')
        pub_date = request.POST.get('datetime')
        author_id = request.POST.get('author')
        price = request.POST.get('price')
        publish_id = request.POST.get('publishlist')

        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,pub_date=pub_date,author_id=author_id,publish_id=publish_id)

        return redirect("/look/")


    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request, 'edit.html', {'edit_book_obj':edit_book_obj,'publish_list': publish_list, 'author_list': author_list})

# 删除
def deletebook(request,delete_book_id):

    Book.objects.filter(pk=delete_book_id).delete()


    return redirect('/look/')


#作者查看
def aut_more(request,show_aut_more):


    id = Book.objects.filter(pk=show_aut_more).values('author_id').first()
    print(id['author_id'])
    id = id['author_id']

    aut_more = Book.objects.filter(author_id=id)
    print(aut_more)


    return render(request,'aut_more.html',{'aut_more':aut_more})

# 出版社查看
def pub_more(request,show_pub_more):

    id = Book.objects.filter(pk=show_pub_more).values('publish_id').first()
    print(id['publish_id'])
    id = id['publish_id']


    pub_more = Book.objects.filter(publish_id=id)
    print(show_pub_more)



    return render(request,'pub_more.html',{'pub_more':pub_more})