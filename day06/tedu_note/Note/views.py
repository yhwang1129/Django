from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Note.models import Note

# Create your views here.

def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            #检查cookies
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                #回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return wrap
@check_login#装饰器
def add_note(request):

    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        #处理数据
        uid = request.session['uid']
        title = request.POST['title']
        content = request.POST['content']

        Note.objects.create(title=title, content=content, user_id=uid)

        return HttpResponseRedirect('/note/all')

def list_view(request):

    user_id = request.session['uid']
    all_note = Note.objects.filter(user_id=user_id, is_active=True)

    return render(request, 'note/list_note.html', locals())

def update_view(request, note_id):

    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('--update note error is %s'%(e))
        return HttpResponse('--The note is not existed')

    if request.method == 'GET':

        return render(request, 'note/update_note.html', locals())

    elif request.method == 'POST':

        title =request.POST['title']
        content = request.POST['content']
        #改
        note.title = title
        note.content = content
        #存
        note.save()

        return HttpResponseRedirect('/note/all')

def delete_view(request):
    #通过获取查询字符串 note_id 拿到要del的note的id
    note_id = request.GET.get('note_id')
    if not note_id:
        return HttpResponse('---请求异常')
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('--delete note error is %s'%(e))
        return HttpResponse('---note_id is error')
    #将其is_active 改成False
    note.is_active = False
    note.save()
    #302跳转到all
    return HttpResponseRedirect('/note/all')