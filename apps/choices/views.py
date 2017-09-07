# _*_ coding:utf-8 _*_
from datetime import datetime,timedelta
import json

from django.shortcuts import render,get_object_or_404
from django.views.generic.base import View
from django.contrib.auth import logout
from django.http import HttpResponse,JsonResponse
# Create your views here.
from users.models import QuestionNaire
from choices.models import MyChoice,MyText,MyQuestion,Content,AnserTime


class QuNaDetailView(View):
    def get(self,request,quna_id):
        quan = get_object_or_404(QuestionNaire,pk=quna_id)
        myq1 = quan.myquestion_set.all().order_by('orde')
        return render(request, 'choices/QuNaDetail.html', {'questionnaire': quan, 'myquestion': myq1, 'error': ''})


class QuNaReleaseView(View):
    def get(self,request,quna_id):
        logout(request)
        quan = get_object_or_404(QuestionNaire,pk=quna_id)
        myq1 = quan.myquestion_set.all().order_by('orde')
        return render(request, 'choices/QuNaRelease.html', {'questionnaire': quan, 'myquestion': myq1, 'error': ''})
    def post(self,request,quna_id):
        quan = get_object_or_404(QuestionNaire,pk=quna_id)
        myq1 = quan.myquestion_set.all().order_by('orde')
        error={}
        for myquestion in myq1:
            if myquestion.type == '1':               # 单选题
                a = '%d' % myquestion.id
                try:
                    my_choice = MyChoice.objects.get(pk=request.POST[a])
                    my_choice.num += 1
                    my_choice.save()
                except:
                    error["A"]="您有选择题未选"
            else:
                fag = True
                for choice in myquestion.mychoice_set.all():
                    a = '%d'%choice.id
                    try:
                        my_choice = MyChoice.objects.get(pk=request.POST[a])
                        my_choice.num +=1
                        fag=False
                        my_choice.save()
                    except:
                        pass
                    try:
                        my_choice = MyChoice.objects.get(pk=request.POST['choice'])
                        my_choice.num +=1
                        fag=False
                        my_choice.save()
                    except:
                        pass
                for text in myquestion.mytext_set.all():
                    fag=False
                    a = str(myquestion.id)+str(text.id)
                    try:
                        content=request.POST[a]
                        if content:
                            my_content = Content(mytext=text)
                            my_content.name = content
                            my_content.save()
                    except:
                        pass
                if fag:
                    error["A"] = "您有选择题未选"
        if error:
            error['questionnaire']=quan
            error['myquestion']=myq1
            return render(request, 'choices/QuNaRelease.html', error)
        else:
            AnTi=AnserTime(question=quan)
            AnTi.save()
            quan.num += 1
            quan.save()
            return render(request,'result.html',{'message':'感谢您对问卷调查的填写'})


class QuNaAddView(View):
    def get(self, request):
        return render(request, 'choices/QuNaAdd.html')
    def post(self, request):
        title = request.POST.get('title', '')
        try:
            title1 = QuestionNaire.objects.get(title=title)
            if title1:
                return render(request, 'choices/QuNaAdd.html', {'error': '问卷调查名重复'})
        except:
            if title:
                QuNa = QuestionNaire(user=request.user,title=title, put_time=datetime.now())
                QuNa.save()
                return render(request, 'index.html')
            else:
                return render(request, 'choices/QuNaAdd.html', { 'error': '添加失败'})


class QuNaAdd1View(View):

    def post(self,request):
        title = request.POST.get('title', '')
        try:
            title1 = QuestionNaire.objects.get(title=title)
            if title1:
                # return HttpResponse('{"status":"fail","msg":"问卷调查名重复"}', content_type='application/json')
                return HttpResponse(json.dumps({"status":"fail","msg":"问卷调查名重复"}), content_type='application/json')
        except:
            if title:
                QuNa = QuestionNaire(user=request.user,title=title, put_time=datetime.now())
                QuNa.save()
                # {'status': 'success', 'msg':' 添加问卷成功', 'questionnaire':QuNa} 不可以
                # {"status": "success", "msg":" 添加问卷成功", "questionnaire": QuNa} 不可以
                # {"status": "success", "msg":" 添加问卷成功", "questionnaire": "QuNa"} 可以
                # {JsonResponse({'status': 'success', 'msg':' 添加问卷成功', 'questionnaire':'QuNa'} 可以
                return JsonResponse({
                    'status': 'success',
                    'msg': '添加问卷成功',
                    'QuNaId': QuNa.id,
                    'QuNaTitle': QuNa.title,
                    'QuNaNd': QuNa.num
                })
            else:
                return HttpResponse('{"status":"success","msg":"添加失败"}', content_type='application/json')


class QuNairedelectView(View):
    def get(self,request,quna_id):
        QuNa = QuestionNaire.objects.get(id=quna_id)
        num = QuNa.id
        QuNa.delete()
        return JsonResponse({'QuNaId': num})


class QuNaResultView(View):
    def get(self,request,quna_id):
        q1 = get_object_or_404(QuestionNaire, pk=quna_id)
        myq1 = q1.myquestion_set.all().order_by('orde')
        NowTimes = datetime.now()
        Timelist0 = []
        Timelist1 = []
        for i in range(0,31):
            NowTime = NowTimes - timedelta(days=i)
            MyTime = NowTimes - timedelta(days=(i+1))
            MyNum = AnserTime.objects.filter(anser_time__range=(MyTime,NowTime)).count()
            NowTime = NowTime.strftime('%m-%d')
            Timelist0.append(NowTime)
            Timelist1.append(MyNum)
        return render(request, 'choices/QuNaResult.html', {'questionnaire': q1, 'myquestion': myq1,'Timelist0':Timelist0,'Timelist1':Timelist1})


class QuNaEditView(View):
    def get(self,request,quna_id):
        quna = QuestionNaire.objects.get(id=quna_id)
        choices = ['单选', '多选', '填空']
        myq1 = quna.myquestion_set.all().order_by('orde')
        return render(request, 'choices/QuNaEdit.html', {'questionnaire': quna, 'choices': choices,'myquestion':myq1})
    def post(self,request,quna_id):
        quna = QuestionNaire.objects.get(id=quna_id)
        choices = ['单选', '多选', '填空']
        qu = quna.myquestion_set.all().order_by('orde')
        if request.method == 'POST':
            choice = request.POST.get('select','')
            if choice == u'填空':
                choice= 'A'
                return render(request,'choices/QuAdd.html',{'choice':choice,'questionnaire':quna})
            elif choice == u'单选':
                choice = 'B'
                return render(request, 'choices/QuAdd.html', {'choice': choice, 'questionnaire': quna})
            else:
                choice = 'C'
                return render(request,'choices/QuAdd.html',{'choice':choice,'questionnaire':quna})
        else:
            return render(request,'choices/QuNaEdit.html',{'questionnaire':quna,'choices':choices,'myquestion':qu})


# ------------------------------------------------------------------------
class QuMoveView(View):
    def get(self,request,qu_id,my_id):
        myq1 = MyQuestion.objects.get(id=qu_id)
        quna1 = myq1.question
        if my_id == u'1':
            myq2 = MyQuestion.objects.get(question=quna1, orde=myq1.orde + 1)
        else:
            myq2 = MyQuestion.objects.get(question=quna1, orde=myq1.orde - 1)
        myq1.orde, myq2.orde = myq2.orde, myq1.orde
        myq1.save()
        myq2.save()
        return JsonResponse({"myqu":qu_id,"Type":my_id})


class QuAddView(View):
    def get(self,request,quna_id,choice):
        quna = QuestionNaire.objects.get(id=quna_id)
        return render(request, 'choices/QuAdd.html', {'questionnaire': quna, 'choice': choice})
    def post(self,request,quna_id,choice):
        quna = QuestionNaire.objects.get(id=quna_id)
        num = quna.myquestion_set.all().count()
        choices = ['单选', '多选', '填空']
        question = request.POST.get('question','')
        content = request.POST.get('content','')
        mq1 = MyQuestion(question=quna,name=question)
        mq1.orde = num
        if choice == u'A':    # 填空
            mq1.type ='3'
            mq1.save()
            mytext = MyText(question=mq1,name='')
            mytext.save()
        elif choice == u'C':  # 多选
            mq1.type ='2'
            mq1.save()
            mychoice = MyChoice(question=mq1,name=content)
            mychoice.save()
        else:                  # 单选
            mq1.type ='1'
            mq1.save()
            mychoice = MyChoice(question=mq1, name=content)
            mychoice.save()
        mq1.save()
        try:
            myq1 = quna.myquestion_set.all().order_by('orde')
            return render(request, 'choices/QuNaEdit.html', {'questionnaire': quna, 'choices': choices, 'myquestion': myq1})
        except Exception as e:
            print 'ok'


class QuDelectView(View):
    def get(self,request,quna_id,qu_id):
        q1 = QuestionNaire.objects.get(id=quna_id)
        choices = ['单选', '多选', '填空']
        myq1 = MyQuestion.objects.get(id=qu_id)
        num = q1.myquestion_set.all().count()
        begain = myq1.orde
        myq1.delete()
        for i in range(begain + 1, num):
            other_myq1 = MyQuestion.objects.get(question=q1, orde=i)
            other_myq1.orde -= 1
            other_myq1.save()
        myq1 = q1.myquestion_set.all().order_by('orde')
        return render(request, 'choices/QuNaEdit.html',{'questionnaire': q1, 'choices': choices, 'myquestion': myq1})


class ChoiceAddView(View):
    def get(self,request,quna_id,qu_id):
        q1 = get_object_or_404(QuestionNaire, pk=quna_id)
        myq1 = get_object_or_404(MyQuestion, pk=qu_id)
        return render(request, 'choices/ChiceAdd.html', {'questionnaire': q1, 'myquestion': myq1})
    def post(self,request,quna_id,qu_id):
        q1 = get_object_or_404(QuestionNaire, pk=quna_id)
        myq1 = get_object_or_404(MyQuestion, pk=qu_id)
        choices = ['单选', '多选', '填空']
        text = request.POST.get('title','')
        choice = MyChoice(question=myq1,name=text)
        choice.save()
        myq1 = q1.myquestion_set.all().order_by('orde')
        return render(request, 'choices/QuNaEdit.html', {'questionnaire': q1,'myquestion': myq1, 'choices': choices})


class ChoiceDelectView(View):
    def get(self,request,quna_id,answer_id):
        choice = get_object_or_404(MyChoice, pk=answer_id)
        choice.delete()
        choices = ['单选', '多选', '填空']
        q1 = get_object_or_404(QuestionNaire, pk=quna_id)
        myq1 = q1.myquestion_set.all().order_by('orde')
        return render(request, 'choices/QuNaEdit.html',{'questionnaire': q1, 'choices': choices, 'myquestion': myq1})