from django.shortcuts import ( render_to_response,HttpResponseRedirect,
                            redirect )
from afrikimage.models import * 
from form import ( SearchForm , PhotoForm , Autorform , LieuxForm , 
                   PersonneForm , Modif_Autorform , modif_photoform ,
                   ActionForm , ObjetForm , HabillementForm , ImageForm,
                   LoginForm)
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.http import Http404
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.formsets import formset_factory
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required


def my_custom_404_view(request):
    """
    """
    return render_to_response('404.html', {})


def login(request):
    if request.user.is_authenticated():

        try:
            if request.user.\
                       groups.values_list()[0][1] in \
                                            ['admin']:
                return redirect('home')

            if request.user.\
                      groups.values_list()[0][1] in \
                                        ['user']:
                return redirect('home')
        except IndexError:
            raise Http404
    else:
        context= {}
        state = u'Identifiez vous...'
        username  = ''
        password = ''
        context.update(csrf(request))
        form = LoginForm()
        context.update({'form':form})
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    state = u"Connecte"
                    return redirect('home')
            else:
                state= u"votre nom d\'utilisateur/mot de passe est incorect"
        context.update({'form':form , 'state':state })
    return render_to_response('login.html', context )
    
def logout (request):
    
    django_logout(request)

    return redirect('/')
    
    
@login_required
def home(request):
    user = request.user
    a = Photo.objects.order_by("-date")[:5]
    
    return render_to_response('home.html',{'a':a ,'user':user})
@login_required
def photographe (request,*args, **kwargs):
    user = request.user
    num = kwargs["num"] or 1
    photo = Photo.objects.all()
    photogr = Auteur.objects.all()
    paginator = Paginator(photogr,25)
    try:
        page = paginator.page(int(num))
    except EmptyPage:
        raise Http404
    #s'execute si le numero de la page est 2
    page.is_before_first = (page.number == 2)
    #si le numero de la page est egale au numero de l'avant 
    #de l'anvant dernier
    page.is_before_last = (page.number == paginator.num_pages - 1)
    #on constitue l'url de la page suivante
    page.url_next = reverse('photographe', args=[int(num) + 1])
    #on constititue l'url de page precedente
    page.url_previous = reverse('photographe',args=[int(num) - 1])
    #constitue l'url de la premiere page
    page.url_first = reverse('photographe')
    #on constitue l'url de la derniere page
    page.url_last = reverse('photographe', args = [paginator.num_pages])
    ctx = {'page':page,'paginator':paginator,'photogr':photogr ,\
            'user':user , 'photo':photo}
    return render_to_response('photographe.html', ctx)

@login_required
def infoauteur(request,*args, **kwargs):
    id_ = kwargs["id"]
    user = request.user
    autor = Auteur.objects.filter(id = id_)
    for photograph in autor:
        auteur = photograph.nom
    autor.photo_auteur = Photo.objects.filter(photographe__nom = auteur ).count()
    context = {'autor':autor , 'user':user}
    return render_to_response('infoauteur.html',context)

@login_required
def galerie(request,*args, **kwargs):
    num = kwargs["num"] or 1
    user = request.user
    photo = Photo.objects.select_related().order_by("photographe__nom")
    paginator = Paginator(photo,20)
    try:
        page = paginator.page(int(num))
        
    except EmptyPage:

        raise Http404
    #s'execute si le numero de la page est 2
    page.is_before_first = (page.number == 2)
    #si le numero de la page est egale au numero de l'avant 
    #de l'anvant dernier
    page.is_before_last = (page.number == paginator.num_pages - 1)
    #on constitue l'url de la page suivante
    page.url_next = reverse('galerie', args=[int(num) + 1])
    #on constititue l'url de page precedente
    page.url_previous = reverse('galerie',args=[int(num) - 1])
    #constitue l'url de la premiere page
    page.url_first = reverse('galerie')
    #on constitue l'url de la derniere page
    page.url_last = reverse('galerie', args = [paginator.num_pages])
    ctx = {'page':page,'paginator':paginator,'photo':photo ,'user':user}
    
    return render_to_response('galerie.html',ctx)

@login_required
def add_photo(request, *args, **kwargs):
    c = {}
    lie = kwargs["num"]
    per = kwargs["id"]
    act = kwargs['actid']
    obj = kwargs['objid']
    hab = kwargs['habid']
    img = kwargs['img']
    group_users = request.user.groups.values_list()
    user = request.user
    c.update(csrf(request))
    lieu = Lieux.objects.get(id= lie)
    personne = Personne.objects.get(id = per)
    action = Action.objects.get(id = act)
    objet = Objet.objects.get(id= obj)
    habillement = Habillement_bijoux.objects.get(id = hab)
    image = Image_p.objects.get(id = img )
    if group_users[0][1] in ['admin']:
        form = PhotoForm()
        form = PhotoForm(initial={'lieux':lieu.id ,'personne':personne.id,\
                                  'action':action.id,'objet':objet.id,\
                                  'habillement':habillement.id ,\
                                  'photo':image.id })
        c =({'form':form})
        #~ from ipdb import set_trace; set_trace()
        if request.method == 'POST':
            #~ from ipdb import set_trace; set_trace()
            form = PhotoForm(request.POST,request.FILES)
            #~ from ipdb import set_trace; set_trace()
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('ajout_lieux'))
        c.update({'form':form , 'user':user})
        c.update(csrf(request))
    else:
        message = "message"
        c.update({"user":user , "message":message})
    return render_to_response('add_photo.html',c)

@login_required
def delete_confirm_photo (request , *args, **kwargs):
    ctx = {}
    photo_id = kwargs["num"]
    group_users = request.user.groups.values_list()
    user = request.user
    if group_users[0][1] in ['admin']:
        photo = Photo.objects.get(id = photo_id)
        photo.url = reverse('delete_confirm_photo', args = [photo_id])
        ctx.update({'photo':photo , 'user':user})
    else:
        message = "message"
        ctx.update ({"message":message , 'user':user })
    return render_to_response('delete_photo.html', ctx )

@login_required
def deleting_photo (request , *args, **kwargs):
    photo_id = kwargs["num"]
    photo = Photo.objects.get(id = photo_id)
    photo.delete()
    photos = Photo.objects.all()
    for photo in photos :
        photo.save()
    return HttpResponseRedirect(reverse('info_photo'))

@login_required
def add_image (request,*args, **kwargs):
    c = {}
    lie = kwargs["num"]
    per = kwargs["id"]
    act = kwargs['actid']
    obj = kwargs['objid']
    hab = kwargs['habid']
    group_users = request.user.groups.values_list()
    user = request.user
    c.update(csrf(request))
    if group_users[0][1] in ['admin']:
        form = ImageForm ()
        c.update({'form':form})
        if request.method == 'POST':
            form = ImageForm (request.POST,request.FILES)
            if form.is_valid ():
                #~ from ipdb import set_trace; set_trace()
                form.save()
                id_img = form.instance.id
                #~ from ipdb import set_trace; set_trace()
                return HttpResponseRedirect(reverse('ajoutphoto',\
                 args =[int(lie) , int(per) , int(act) ,int(obj) , int(hab) , id_img]))
        c.update({'form':form , 'user':user})
        c.update(csrf(request))
    else:
        message = "message"
        c.update({'user':user , 'message':message})
    return render_to_response ('add_image.html', c)

@login_required
def info_photo (request,*args, **kwargs):
    
    num = kwargs["num"] or 1
    user = request.user
    photo = Photo.objects.all()
    paginator = Paginator(photo,1)
    try:
        page = paginator.page(int(num))
        
    except EmptyPage:

        raise Http404
    #s'execute si le numero de la page est 2
    page.is_before_first = (page.number == 2)
    #si le numero de la page est egale au numero de l'avant 
    #de l'anvant dernier
    page.is_before_last = (page.number == paginator.num_pages - 1)
    #on constitue l'url de la page suivante
    page.url_next = reverse('info_photo', args=[int(num) + 1])
    #on constititue l'url de page precedente
    page.url_previous = reverse('info_photo',args=[int(num) - 1])
    #constitue l'url de la premiere page
    page.url_first = reverse('info_photo')
    #on constitue l'url de la derniere page
    page.url_last = reverse('info_photo', args = [paginator.num_pages])
    #~ num_page = page.number
    ctx = {'page':page,'paginator':paginator , 'user':user }
    return render_to_response('info_photo.html',ctx)

@login_required
def dashphoto (request , *args, **kwargs):
    id_photo = kwargs["num"]
    user = request.user
    photo = Photo.objects.get(id =id_photo )
    
    # formatage des index
    #index personne
    
    index_pers = [persexe['name'] for persexe in photo.personne.sexe.values()]
    index_pers2 =[percategorie_dage['name'] for percategorie_dage in photo.personne.categorie_dage.values()]
    index_pers3 = [pernombre_personne['name'] for pernombre_personne in photo.personne.nombre_personne.values()]
    index_pers4 = [perprise_de_vue['name'] for perprise_de_vue in photo.personne.prise_de_vue.values()]
    index_pers5 = [perpose['name'] for perpose in photo.personne.pose.values()]
    index_pers6 = [perposition['name'] for perposition in photo.personne.position.values()]
    index_pers.extend(index_pers2)
    index_pers.extend(index_pers3)
    index_pers.extend(index_pers4)
    index_pers.extend(index_pers5)
    index_pers.extend(index_pers6)
    
    # index habilllement et bijoux
    
    index_habit =  [hab_habillement['name'] for hab_habillement in photo.habillement.habillement.values()]
    index_habit2 = [hab_type_habillement['name'] for hab_type_habillement in photo.habillement.type_habillement.values()]
    index_habit3 = [hab_Vetement['name'] for hab_Vetement in photo.habillement.Vetement.values()]
    index_habit4 = [hab_chaussures['name'] for hab_chaussures in photo.habillement.chaussures.values()]
    index_habit5 = [hab_bijoux['name'] for hab_bijoux in photo.habillement.bijoux.values()]
    index_habit6 = [hab_coiffe['name'] for hab_coiffe in photo.habillement.coiffe.values()]
    index_habit.extend(index_habit2)
    index_habit.extend(index_habit3)
    index_habit.extend(index_habit4)
    index_habit.extend(index_habit5)
    index_habit.extend(index_habit6)
    
    # index object 
    
    index_obj = [obj_objet_naturel['name'] for obj_objet_naturel in photo.objet.objet_naturel.values()]
    index_obj2 = [obj_objet_fabrique['name'] for obj_objet_fabrique in photo.objet.objet_fabrique.values()]
    index_obj3 = [obj_objet_domestique['name'] for obj_objet_domestique in photo.objet.objet_domestique.values()]
    index_obj4 = [obj_objet_travail['name'] for obj_objet_travail in photo.objet.objet_travail.values()]
    index_obj5 = [obj_vehicule['name'] for obj_vehicule in photo.objet.vehicule.values()]
    index_obj6 = [obj_objet_loisir['name'] for obj_objet_loisir in photo.objet.objet_loisir.values()]
    index_obj7 = [obj_objet_decoratif['name'] for obj_objet_decoratif in photo.objet.objet_decoratif.values()]
    index_obj.extend(index_obj2)
    index_obj.extend(index_obj3)
    index_obj.extend(index_obj4)
    index_obj.extend(index_obj5)
    index_obj.extend(index_obj6)
    index_obj.extend(index_obj7)
    ctx = {'photo':photo , 'index_pers':index_pers,\
                        'index_habit':index_habit,\
                        'index_obj':index_obj ,\
                        'user':user ,\
                        }
    return render_to_response ('dashphoto.html', ctx )

@login_required
def modif_photo(request , *args, **kwargs):
    ph_id = int(kwargs["id"])
    num_page = kwargs['num_page']
    img_id = kwargs["num"]
    id_lieu  = kwargs['lieu_id']
    group_users = request.user.groups.values_list()
    user = request.user
    context = {}
    context.update(csrf(request))
    if group_users[0][1] in ['admin']:
        form = modif_photoform ()
        context.update({'form':form , 'user':user})
        photo =  Photo.objects.get(id=ph_id)
        url_image = reverse ('modif_image', args = [photo.photo.id , photo.id , num_page])
        url_lieu = reverse ('modif_lieu' , args = [photo.lieux.id , photo.id , num_page])
        url_action = reverse ('modif_action' ,args =[photo.action.id , photo.id , num_page])
        url_objet = reverse ('modif_objet' ,args = [photo.objet.id , photo.id , num_page])
        url_personne = reverse('modif_personne',args=[photo.personne.id ,photo.id , num_page])
        url_habit = reverse ('modif_habit', args = [photo.habillement.id ,photo.id , num_page])
        data = {}
        # si l'id de l'image existe on remplace cet id par celle de la photo
        # existante
        if img_id or id_lieu :
            image = Image_p.objects.get(id = img_id)
            data =  {
                        'photographe': photo.photographe.id ,\
                        'theme' : photo.theme.id ,\
                        'format' : photo.format ,\
                        'mode' : photo.mode , \
                        'date' : photo.date ,\
                        'type_p':photo.type_p ,\
                        'personne':photo.personne.id ,\
                        'action' : photo.action.id ,\
                        'photo' : image.id ,\
                        'habillement':photo.habillement.id ,\
                        'objet' : photo.objet.id ,\
                        'lieux' : photo.lieux.id ,\
                        'appareil':photo.appareil ,\
                        'sens' : photo.sens ,\
                        'description': photo.description ,\
                    }
        else:
                    data =  {
                        'photographe': photo.photographe.id ,\
                        'theme' : photo.theme.id ,\
                        'format' : photo.format ,\
                        'mode' : photo.mode , \
                        'date' : photo.date ,\
                        'type_p':photo.type_p ,\
                        'personne':photo.personne.id ,\
                        'action' : photo.action.id ,\
                        'photo' : photo.photo.id ,\
                        'habillement':photo.habillement.id ,\
                        'objet' :photo.objet.id  ,\
                        'lieux' : photo.lieux.id ,\
                        'appareil':photo.appareil ,\
                        'sens' : photo.sens ,\
                        'description': photo.description ,\
                    }

        form = modif_photoform (data)
        context.update({'form':form ,'url_image':url_image,\
                        'url_lieu': url_lieu , 'url_action':url_action ,\
                        'url_objet':url_objet ,'url_personne':url_personne,\
                        'url_habit':url_habit})
        if request.method == 'POST':
            form = modif_photoform(request.POST,request.FILES)
            if form.is_valid():
                photo.photographe_id = request.POST['photographe']
                photo.theme_id =  request.POST['theme']
                photo.format = request.POST['format']
                photo.mode = request.POST['mode']
                photo.date = request.POST['date']
                photo.type_p = request.POST['type_p']
                photo.photo_id = request.POST['photo']
                photo.personne_id = request.POST['personne']
                photo.action_id = request.POST['action']
                photo.habillement_id = request.POST['habillement']
                photo.objet_id = request.POST['objet']
                photo.lieux_id = request.POST['lieux']
                photo.appareil = request.POST['appareil']
                photo.sens = request.POST['sens']
                photo.description = request.POST['description']
                photo.save ()
                return HttpResponseRedirect(reverse('info_photo',args=[num_page]))
    else:
        message = "message"
        context.update ({"message":message ,'user':user})
    return render_to_response('modif_photo.html',context)

@login_required
def modif_image (request , *args, **kwargs):
    image_id = kwargs['id']
    modif_id = kwargs["num"]
    page_id = kwargs["page"]
    user = request.user
    context = {}
    context.update(csrf(request))
    image = Image_p.objects.get(id = image_id)
    form = ImageForm    ( initial = {   'title':image.title ,\
                                        'serie':image.serie ,\
                                        'image':image.image 
                                    }
                        )
    context.update({'form':form , 'user':user })
    #~ from ipdb import set_trace; set_trace()
    if request.method == 'POST':
        form = ImageForm (request.POST,request.FILES)
        if form.is_valid ():
            form.save()
            id_img = form.instance.id
            print id_img
            #~ from ipdb import set_trace; set_trace()
            return HttpResponseRedirect (reverse('modif_photo', args =[modif_id , page_id , id_img ]))
    return render_to_response ('modif_image.html', context)

@login_required
def modif_lieu(request , *args, **kwargs):
    lieu_id = kwargs['id']
    modif_id = kwargs["num"]
    page_id = kwargs["page"]
    user = request.user
    context = {}
    context.update(csrf(request))
    lieu = Lieux.objects.get(id = lieu_id)
    form = LieuxForm ()
    context.update({'form':form , 'user':user})
    if request.method == 'POST':
        form = LieuxForm(request.POST)
        if form.is_valid():
            form.save()
            id_lieu = form.instance.id
            photo = Photo.objects.get(id = modif_id)
            photo.lieux_id = id_lieu
            photo.save()
            return HttpResponseRedirect (reverse('modif_photo', args =[modif_id , page_id]))
    return render_to_response ('modif_lieu.html',context)

@login_required
def modif_action (request , *args , **kwargs):
    action_id = kwargs['id']
    modif_id = kwargs['num']
    page_id = kwargs["page"]
    user = request.user
    context = {}
    context.update(csrf(request))
    action = Action.objects.get(id = action_id)
    form = ActionForm ()
    context.update({'form':form, 'user':user})
    if request.method == 'POST':
        form = ActionForm (request.POST)
        if form.is_valid():
            form.save()
            id_action = form.instance.id
            photo = Photo.objects.get(id = modif_id)
            photo.action_id = id_action
            photo.save()
            return HttpResponseRedirect (reverse('modif_photo',args = [modif_id , page_id]))
    return render_to_response ('modif_action.html', context)

@login_required
def modif_objet (request , *args , **kwargs):
    objet_id = kwargs['id']
    modif_id = kwargs['num']
    page_id = kwargs["page"]
    user = request.user
    context = {}
    context.update(csrf(request))
    form = ObjetForm()
    context.update({'form':form , 'user':user})
    if request.method == 'POST':
        form = ObjetForm (request.POST)
        if form.is_valid():
            form.save()
            photo = Photo.objects.get ( id = modif_id)
            photo.objet_id = form.instance.id
            photo.save()
            return HttpResponseRedirect (reverse('modif_photo',args=[modif_id , page_id]))
    return render_to_response ('modif_objet.html', context)

@login_required
def modif_personne (request , *args , **kwargs):
    personne_id = kwargs['id']
    modif_id = kwargs['num']
    page_id = kwargs["page"]
    user = request.user
    context = {}
    context.update(csrf(request))
    form = PersonneForm ()
    context.update({'form':form , 'user':user})
    if request.method == 'POST':
        form = PersonneForm (request.POST)
        if form.is_valid():
            form.save()
            photo = Photo.objects.get(id = modif_id)
            photo.personne_id = form.instance.id
            photo.save()
            return HttpResponseRedirect (reverse ('modif_photo',args=[modif_id , page_id]))
    return render_to_response ('modif_personne.html', context )

@login_required
def modif_habit (request, *args , **kwargs):
    habit_id = kwargs['id']
    modif_id = kwargs['num']
    page_id = kwargs["page"]
    user = request.user
    context = {}
    context.update(csrf(request))
    form = HabillementForm ()
    context.update({'form':form ,'user':user})
    if request.method == "POST":
        form = HabillementForm (request.POST)
        if form.is_valid():
            form.save()
            photo = Photo.objects.get ( id = modif_id)
            photo.habillement_id = form.instance.id 
            photo.save()
            return HttpResponseRedirect (reverse ('modif_photo',args=[modif_id , page_id]))
    return render_to_response ('modif_habit.html', context )

@login_required
def auteur (request):
    user = request.user
    liste1 = [b.nom  for b in Auteur.objects.all() ]
    liste2 = [u.prenom for u in Auteur.objects.all()]
    #liste = liste1 + liste2
    liste = ['djire', 'traore', 'bintou', 'diallo', 'coulibaly', 'lassana', 'beydi', 'diarra', 'mahamoudou', 'aminata']
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(photo__title__icontains=query) |
            Q(photographe__nom__icontains=query) |
            Q(photographe__prenom__icontains = query ) |
            Q(theme__categorie__icontains = query) |
            Q(theme__theme__nom__icontains = query) |
            Q(mode__icontains = query) |
            Q(sens__icontains = query) |
            Q(date__icontains = query) |
            Q(description__icontains = query) |

            Q(personne__sexe__name__icontains = query ) |
            Q(personne__categorie_dage__name__icontains = query ) |
            Q(personne__nombre_personne__name__icontains = query ) |
            Q(personne__prise_de_vue__name__icontains = query ) |
            Q(personne__pose__name__icontains= query ) | 
            Q(personne__position__name__icontains = query ) |

            Q(objet__objet_naturel__name__icontains = query ) |
            Q(objet__objet_fabrique__name__icontains = query ) |
            Q(objet__objet_domestique__name__icontains = query ) |
            Q(objet__objet_travail__name__icontains = query ) |
            Q(objet__vehicule__name__icontains = query ) |
            Q(objet__objet_loisir__name__icontains = query ) |
            Q(objet__objet_decoratif__name__icontains = query ) |
            
            Q(habillement__habillement__name__icontains = query ) |
            Q(habillement__type_habillement__name__icontains = query ) |
            Q(habillement__Vetement__name__icontains = query ) |
            Q(habillement__chaussures__name__icontains = query ) |
            Q(habillement__bijoux__name__icontains = query ) |
            Q(habillement__coiffe__name__icontains = query )
        )
        
        resultat = Photo.objects.filter(qset).distinct()
        #~ from ipdb import set_trace; set_trace()
    else:
        resultat = []
    ctx={'resultat':resultat , 'query':query , 'user':user , 'liste':liste}
    return render_to_response('auteur.html',ctx)

@login_required
def add_autor(request):
    c = {}
    c.update(csrf(request))
    group_users = request.user.groups.values_list()
    user = request.user
    if group_users[0][1] in ['admin']:
        form = Autorform ()
        c.update({'form':form , 'user':user})
        if request.method == 'POST':
            form = Autorform (request.POST)
            data =  {
                        'nom': request.POST['nom'],\
                        'prenom':request.POST['prenom'],\
                        'nationalite':request.POST['nationalite'],\
                        'date1': request.POST['date1'],\
                        'adresse':request.POST['adresse'],\
                        'email':request.POST['email'],\
                        'experience': request.POST['experience'],\
                    }

            #~ from ipdb import set_trace; set_trace()
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('photographe'))

        c.update({'form':form})
    else:
        message =  u"message"
        c.update({'message':message})
    return render_to_response('add_autor.html', c )

@login_required
def delete_confirm_auteur (request , *args, **kwargs):
    ctx = {}
    auteur_id = kwargs["num"]
    group_users = request.user.groups.values_list()
    user = request.user
    if group_users[0][1] in ['admin']:
        auteur  = Auteur.objects.get(id = auteur_id)
        ctx.update ({'auteur':auteur , 'user':user})
    else:
        message = "message"
        ctx.update({'message':message , 'user':user})
    return render_to_response('deleting_auteur.html', ctx)

@login_required
def deleting_auteur (request , *args, **kwargs):
    auteur_id = kwargs["num"]
    user = request.user
    auteur  = Auteur.objects.get(id = auteur_id)
    auteur.delete()
    auteurs = Auteur.objects.all()
    for auteur in auteurs :
        auteur.save()
    return HttpResponseRedirect (reverse ('photographe',{'user':user}))

@login_required
def modif_auteur(request,*args, **kwargs):
    id_autor = kwargs["id"]
    group_users = request.user.groups.values_list()
    user = request.user
    context = {}
    context.update(csrf(request))
    if group_users[0][1] in ['admin']:
        form = Modif_Autorform()
        context.update({'form':form , 'user':user})
        autor = Auteur.objects.get (id = id_autor)
        data = {}
        data =  {   'nom' : autor.nom ,\
                    'prenom' : autor.prenom ,\
                    'nationalite' : autor.nationalite ,\
                    'date1' : autor.date1 ,\
                    'adresse' : autor.adresse ,\
                    'email' : autor.email ,\
                    'experience' : autor.experience ,\
                }
        form = Modif_Autorform (data)
        context.update({'form':form})
        if request.method == 'POST':
            form = Modif_Autorform(request.POST)
            if form.is_valid ():
                autor.nom = request.POST['nom']
                autor.prenom = request.POST['prenom']
                autor.nationalite = request.POST['nationalite']
                autor.date1 = request.POST['date1']
                autor.adresse = request.POST['adresse']
                autor.email = request.POST['email']
                autor.experience = request.POST['experience']
                autor.save()
                return HttpResponseRedirect(reverse('photographe'))
        context.update(csrf(request))
    else:
        message = "message"
        context.update ({'message':message , 'user':user })
    return render_to_response('modif_auteur.html', context)

@login_required
def add_lieux(request):
    context = {}
    context.update(csrf(request))
    group_users = request.user.groups.values_list()
    user = request.user
    if group_users[0][1] in ['admin']:
        form = LieuxForm()
        context.update({'form':form , 'user':user})
        lieu =Lieux()
        if request.method == 'POST':

            lieu.cadre = request.POST.get('cadre') or ''
            lieu.saison =  request.POST.get('saison') or ''
            lieu.type_in = request.POST.get('type_in') or ''
            lieu.type_ex = request.POST.get('type_ex') or ''
            lieu.moment = request.POST.get('moment') or ''
            lieu.pays   = request.POST.get('pays')
            lieu.ville  = request.POST.get('ville')
            doublon = Lieux.objects.filter(cadre = lieu.cadre ,\
                                           saison = lieu.saison ,\
                                           type_in =lieu.type_in ,\
                                           type_ex = lieu.type_ex ,\
                                           moment = lieu.moment ,\
                                           pays = lieu.pays ,\
                                           ville = lieu.ville)

            if not doublon:
                lieu.save()
                return HttpResponseRedirect(reverse('ajout_personne',args =[lieu.id]))
            else:
                a  = doublon[0]
                return HttpResponseRedirect(reverse('ajout_personne',args =[a.id]))

        context.update(csrf(request))
    else:
        message = "message"
        context.update ({"message":message , 'user':user })
    return render_to_response('add_lieux.html',context,)

@login_required
def add_personne(request,*args, **kwargs):
    id_ = kwargs["id"]
    group_users = request.user.groups.values_list()
    user = request.user
    context = {}
    context.update(csrf(request))
    if group_users[0][1] in ['admin']:
        form = PersonneForm ()
        context.update({'form':form ,'user':user})
        personne = Personne()
        if request.method == 'POST':
            form = PersonneForm (request.POST)
            if form.is_valid():
                persexe = request.POST.get('sexe')
                percategorie_dage = request.POST.get('categorie_dage') 
                pernombre_personne = request.POST.get('nombre_personne')
                perprise_de_vue = request.POST.get('prise_de_vue')
                perpose = request.POST.get('pose')
                perposition = request.POST.get('position')
                doublon = Personne.objects.filter (  sexe = persexe,\
                                        categorie_dage=percategorie_dage,\
                                        nombre_personne = pernombre_personne,\
                                        prise_de_vue = perprise_de_vue ,\
                                        pose = perpose ,\
                                        position = perposition)
                if not doublon:
                    
                    form.save()
                    return HttpResponseRedirect(reverse('ajout_action',args =[int(id_) ,form.instance.id]))
                else:
                    a = doublon[0]
                    return HttpResponseRedirect(
                                    reverse('ajout_action', args = [id_ ,a.id])
                                            )
        context.update({'form':form })
    else:
        message = "message"
        context.update ({'message':message , 'user':user })
    return render_to_response('add_personne.html',context)

@login_required
def add_action(request,*args, **kwargs):
    lie_id = kwargs ['lied']
    per_id = int(kwargs ['persid'])
    group_users = request.user.groups.values_list()
    user = request.user
    context = {}
    context.update(csrf(request))
    if group_users[0][1] in ['admin']:
        form = ActionForm ()
        context.update({'form':form , 'user':user})
        action = Action()
        if request.method == 'POST':
            action.action_personnage = request.POST.get('action_personnage') or ''
            action.type_pose = request.POST.get('type_pose') or ''
            action.Cadre_action = request.POST.get('Cadre_action') or ''
            doublon = Action.objects.filter(
                            action_personnage=action.action_personnage,\
                                            type_pose = action.type_pose,\
                                            Cadre_action = action.Cadre_action)
            if not doublon :
                action.save()
                return HttpResponseRedirect(
                        reverse(
                'ajout_objet', args=[int(lie_id) , int(per_id) , action.id]
                                )
                                )
            else:
                a = doublon[0]
                return HttpResponseRedirect (reverse('ajout_objet',\
                                args=[int(lie_id) , int(per_id) , a.id]))
            
        context.update({'form':form})
    else:
        message = "message"
        context.update ({'user':user , 'message':message })
    return render_to_response ('add_action.html',context)

@login_required
def add_objet(request,*args, **kwargs):
    lie_id = kwargs ['lied']
    per_id = kwargs ['persid']
    act_id = kwargs ['actid']
    group_users = request.user.groups.values_list()
    user = request.user
    context = {}
    context.update(csrf(request))
    if group_users[0][1] in ['admin']:
        form = ObjetForm ()
        context.update({'form':form , 'user':user})
        if request.method == 'POST':
            form = ObjetForm (request.POST)
            objet = Objet()
            if form.is_valid():
                obj_naturel = request.POST.get ('objet_naturel')
                obj_fabrique = request.POST.get ('objet_fabrique')
                obj_domestique = request.POST.get ('objet_domestique')
                obj_travail = request.POST.get ('objet_travail')
                vehicule  = request.POST.get ('vehicule')
                obj_loisir = request.POST.get ('objet_loisir')
                obj_decoratif = request.POST.get('objet_decoratif')
                doublon = Objet.objects.filter(objet_naturel= obj_naturel,\
                                        objet_fabrique= obj_fabrique ,\
                                        objet_domestique = obj_domestique,\
                                        objet_travail = obj_travail ,\
                                        vehicule = vehicule , \
                                        objet_loisir= obj_loisir, \
                                        objet_decoratif = obj_decoratif)
                if not doublon:
                    form.save()
                    return HttpResponseRedirect(reverse
                                ('ajout_habit',\
                 args=[int(lie_id) , int(per_id) , int(act_id) ,form.instance.id]))
                else:
                    a = doublon[0]
                    return HttpResponseRedirect (reverse
                                    ('ajout_habit',\
                       args=[int(lie_id) , int(per_id) , int(act_id) ,a.id])
                                                )
        context.update({'form':form})
    else:
        message = "message"
        context.update ({'user':user , 'message':message })
    return render_to_response ('add_objet.html',context)

@login_required
def add_habillement(request,*args, **kwargs):
    lie_id = kwargs ['lied']
    per_id = kwargs ['persid']
    act_id = kwargs ['actid']
    obj_id = kwargs ['objid']
    group_users = request.user.groups.values_list()
    user = request.user
    context = {}
    context.update(csrf(request))
    if group_users[0][1] in ['admin']:
        form = HabillementForm ()
        context.update({'form':form , 'user':user})
        if request.method == 'POST':
            form = HabillementForm(request.POST)
            if form.is_valid():
                habillement = request.POST.get('habillement')
                type_habillement = request.POST.get('type_habillement')
                Vetement = request.POST.get('Vetement')
                chaussures = request.POST.get('chaussures')
                bijoux = request.POST.get('bijoux')
                coiffe = request.POST.get('coiffe')
                doublon= Habillement_bijoux.objects.filter(habillement=habillement,\
                                                type_habillement= type_habillement,\
                                                Vetement = Vetement ,\
                                                chaussures = chaussures , \
                                                bijoux = bijoux ,\
                                                coiffe = coiffe)
                if not doublon:
                    form.save()
                    return HttpResponseRedirect(reverse
                        ('image',\
                 args=[int(lie_id) , int(per_id) , int(act_id) ,int(obj_id) , form.instance.id]))
                else:
                    a = doublon[0]
                    return HttpResponseRedirect (reverse
                            ('image',\
                    args=[int(lie_id) , int(per_id) , int(act_id) ,int(obj_id), a.id]))
        context.update({'form':form})
    else:
        message = "message"
        context.update ({"message":message , 'user':user})
    return render_to_response ('add_habit.html',context)

@login_required
def search_lieu (request):
    context = {}
    context.update(csrf(request))
    user = request.user
    form = LieuxForm()
    context.update({'form':form , 'user':user})
    if request.method == 'POST':
        cadre = request.POST.get('cadre') or ''
        saison = request.POST.get('saison') or ''
        type_in = request.POST.get('type_in') or ''
        type_ex = request.POST.get('type_ex') or ''
        moment = request.POST.get('moment')  or ''
        pays = request.POST.get('pays') or ''
        ville  = request.POST.get('ville') or ''
        response = Photo.objects.filter(lieux__cadre = cadre , \
                                        lieux__saison = saison , \
                                        lieux__type_in = type_in , \
                                        lieux__type_ex = type_ex , \
                                        lieux__moment = moment , \
                                        lieux__pays = pays ,\
                                        lieux__ville = ville )
        print response
                                        
        context.update( {'response':response} )
    context.update(csrf(request))
    return render_to_response ('search_lieu.html' , context )

@login_required
def search_action (request):
    context = {}
    context.update(csrf(request))
    user = request.user
    form = ActionForm ()
    context.update({'form':form , 'user':user})
    if request.method == 'POST':
        action_personnage = request.POST.get('action_personnage') or ''
        type_pose = request.POST.get('type_pose') or ''
        Cadre_action = request.POST.get('Cadre_action') or ''
        response = Photo.objects.filter (action__action_personnage = action_personnage , \
                        action__type_pose = type_pose , \
                        action__Cadre_action  = Cadre_action )
        context.update( {'response':response} )
    context.update(csrf(request))
    return render_to_response ( 'search_action.html', context )

@login_required
def search_personne (request):
    context = {}
    context.update(csrf(request))
    user = request.user
    form = PersonneForm ()
    context.update({'form':form , 'user':user})
    if request.method == 'POST':
        form = PersonneForm (request.POST)
        if form.is_valid():
            sexe = request.POST.get('sexe')
            categorie_dage = request.POST.get('categorie_dage')
            nombre_personne = request.POST.get('nombre_personne')
            prise_de_vue = request.POST.get('prise_de_vue')
            pose = request.POST.get('pose') 
            position = request.POST.get('position')
            response = Photo.objects.filter (personne__sexe = sexe ,\
                                    personne__categorie_dage = categorie_dage,\
                                    personne__nombre_personne = nombre_personne,\
                                    personne__prise_de_vue = prise_de_vue ,\
                                    personne__pose = pose ,\
                                    personne__position = position)
            context.update( {'response':response} )
        context.update(csrf(request))
    
    return render_to_response ('search_personne.html', context )

@login_required
def search_habit (request):
    context = {}
    context.update(csrf(request))
    user = request.user
    form = HabillementForm ()
    context.update({'form':form ,'user':user})
    if request.method == 'POST':
        form = HabillementForm(request.POST)
        if form.is_valid():
            habillement = request.POST.get('habillement')
            type_habillement = request.POST.get('type_habillement')
            Vetement = request.POST.get('Vetement')
            chaussures = request.POST.get('chaussures')
            bijoux = request.POST.get('bijoux')
            coiffe = request.POST.get('coiffe')
            response = Photo.objects.filter(habillement__habillement = habillement,\
                                            habillement__type_habillement = type_habillement,\
                                            habillement__Vetement = Vetement ,\
                                            habillement__chaussures = chaussures , \
                                            habillement__bijoux = bijoux ,\
                                            habillement__coiffe = coiffe)
            context.update( {'response':response} )
        context.update(csrf(request))
    return render_to_response ('search_habit.html' , context )

@login_required
def search_objet (request):
    context = {}
    context.update(csrf(request))
    user = request.user
    form = ObjetForm ()
    context.update({'form':form , 'user':user})
    if request.method == 'POST':
        form = ObjetForm (request.POST)
        objet = Objet()
        if form.is_valid():
            obj_naturel = request.POST.get ('objet_naturel')
            obj_fabrique = request.POST.get ('objet_fabrique')
            obj_domestique = request.POST.get ('objet_domestique')
            obj_travail = request.POST.get ('objet_travail')
            vehicule  = request.POST.get ('vehicule')
            obj_loisir = request.POST.get ('objet_loisir')
            obj_decoratif = request.POST.get('objet_decoratif')
            response = Photo.objects.filter(objet__objet_naturel= obj_naturel,\
                                    objet__objet_fabrique= obj_fabrique ,\
                                    objet__objet_domestique = obj_domestique,\
                                    objet__objet_travail = obj_travail ,\
                                    objet__vehicule = vehicule , \
                                    objet__objet_loisir= obj_loisir, \
                                    objet__objet_decoratif = obj_decoratif)
            context.update( {'response':response} )
        context.update(csrf(request))
    return render_to_response ('search_objet.html' , context )
