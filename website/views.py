import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Max
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from website import models, shipping
from website.models import Auction, Bid, Profile

from .forms import AuctionForm

# Create your views here.
appname = 'Auctioneer'


def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try:
                user = User.objects.get(username=username)
            except models.Profile.user.DoesNotExist:
                raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request, 'website/login.html', {'appname': appname})
    return mod_view


def profile(request):
    if 'username' in request.session:
        loggedin = True
        user = User.objects.get(username=request.session['username'])
        profile = user.profile

        try:
            bids = Bid.objects.filter(userid=profile)
        except Exception as e:
            bids = None

        auctions = Auction.objects.filter(auctionOpen=False)
        a = []

        for b in bids:
            if Auction.objects.filter(winningBid=b) != None:
                auction = Auction.objects.filter(winningBid=b)
                if auction.count() != 0:
                    a.append(auction[0])

        if len(a) == 0:
            displayShip = False
        else:
            displayShip = True
        context = {
            'loggedin': loggedin,
            'user': user,
            'bids': bids,
            'auctions': a,
            'username': request.session['username'],
            'displayShipping': displayShip
        }
        return render(request, 'website/viewprofile.html', context)
    else:
        return redirect('login')


def index(request):
    loggedin = False
    if 'username' in request.session:
        username = request.session['username']
        loggedin = True
        context = {'appname': appname,
                   'loggedin': loggedin,
                   'username': username}
        return render(request, 'website/index.html', context)
    context = {'appname': appname,
               'loggedin': loggedin, }
    return render(request, 'website/index.html', context)


def closed_auctions(request):
    loggedin = False
    if 'username' in request.session:
        username = request.session['username']
        loggedin = True
        closed = Auction.objects.filter(auctionOpen=False)
        context = {'auctions': closed,
                   'loggedin': loggedin,
                   'username': username,
                   }
        return render(request, 'website/closed.html', context)
    closed = Auction.objects.filter(auctionOpen=False)
    context = {'auctions': closed}
    return render(request, 'website/closed.html', context)


def search(request):
    search = request.POST['search-input']
    pk = search
    results = Auction.objects.filter(title__icontains=search, auctionOpen=True)
    loggedin = False
    if 'username' in request.session:
        username = request.session['username']
        loggedin = True
        return render(request, 'website/search.html', {
            'results': results,
            'loggedin': loggedin,
            'username': username,
        })
    return render(request, 'website/search.html', {
        'results': results,
        'loggedin': loggedin,
    })


def search_json(request):
    search = request.POST['search-input']
    pk = search
    results = Auction.objects.filter(title__icontains=search, auctionOpen=True)
    return JsonResponse({
        'results': list(results.values()),
    })


def signup(request):
    context = {'appname': appname}
    return render(request, 'website/signup.html', context)


def register(request):
    if 'username' in request.POST and 'password' in request.POST:
        u = request.POST['username']
        p = request.POST['password']
        email = request.POST['email']
        dob = request.POST['dob']
        dob_dateobj = datetime.date.fromisoformat(str(dob))

        user = User()
        user.username = u
        user.set_password(p)
        user.email = email

        profile = models.Profile()
        profile.birth_date = dob_dateobj
        profile.user = user

        try:
            user.save()
        except IntegrityError:
            messages.error(request, 'the username ' + u + ' is already taken')
            return redirect('signup')
        except Exception as e:
            raise Http404('error')

            # raise Http404(
            #     'Username '+u+' already taken: Usernames must be unique')
        try:
            profile.save()
        except Exception as e:
            print(e)
        context = {
            'appname': appname,
            'username': u
        }
        # return render(request, 'website/index.html', context)
        return redirect('index')

    else:
        raise Http404('POST data missing')


def bid_json(request):
    if 'username' not in request.session:
        return JsonResponse({
            'message': "Login to bid",
        })
    aucID = request.POST['auction']
    amount = request.POST['amount']
    auction = Auction.objects.get(id=aucID)
    highestBid = request.POST['highestBid']

    if(amount <= highestBid and highestBid != "None" and amount < 0):
        return JsonResponse(
            {
                'user': request.session['username'],
                'message': "Amount below min",
                'highestBid': highestBid
            }
        )
    user = request.session['username']
    userobj = User.objects.get(username=user)
    userid = userobj.id
    profile = Profile.objects.get(user=userobj)
    newBid = Bid(
        amount=amount,
        userid=profile,
        auctionid=auction
    )
    newBid.save()
    return JsonResponse({
        'message': "Bid Created",
        'newAmount': newBid.amount,
    })


def createAuction(request):
    if(request.method == "GET"):
        username = request.session['username']
        form = AuctionForm
        username = request.session['username']
        loggedin = False
        if username != None:
            loggedin = True
        context = {
            'username': username,
            'form': form,
            'loggedin': loggedin,
        }
        return render(request, 'website/createAuc.html', context)


def auction_closed():
    pass


def auction(request, id):
    auction = Auction.objects.get(id=id)
    bids = Bid.objects.filter(auctionid=id)
    highestBid = bids.aggregate(Max('amount'))
    startingBid = auction.startingPrice
    if highestBid['amount__max'] is None:
        highestBid['amount__max'] = startingBid
    loggedin = False
    if 'username' in request.session:
        loggedin = True
        username = request.session['username']
        context = {
            'auction': auction,
            'username': username,
            'highest': highestBid,
            'loggedin': loggedin,
            'auctionCloseISOFormat': datetime.datetime.isoformat(auction.auctionCloseTimestamp)
        }
        return render(request, 'website/auction.html', context)
    context = {
        'auction': auction,
        'highest': highestBid,
        'loggedin': loggedin,
    }
    return render(request, 'website/auction.html', context)


def auction_json(request):
    title = request.POST['title']
    description = request.POST['description']
    username = request.session['username']
    user = User.objects.get(username=username)

    newAuction = Auction(
        title=title,
        owner=user,
        description=description,
        startingPrice=request.POST['starting'],
        picture=request.FILES['picture'],
        auctionCloseTimestamp=datetime.datetime.fromisoformat(
            request.POST['auctionEnd']),
        length=request.POST['length'],
        width=request.POST['width'],
        height=request.POST['height'],
        weight=request.POST['weight']
    )
    newAuction.save()
    return redirect('profile')


def login(request):
    if not ('username' in request.POST and 'password' in request.POST):
        context = {'appname': appname}
        return render(request, 'website/login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try:
            member = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Your username or password is incorrect')
            return redirect('login')
        if member.check_password(password):
            # remember user in session variable
            request.session['username'] = username
            request.session['password'] = password
            context = {
                'appname': appname,
                'username': username,
                'loggedin': True
            }
            response = render(request, 'website/index.html', context)

            # remember last login in cookie
            now = datetime.datetime.utcnow()
            max_age = 365 * 24 * 60 * 60  # one year
            delta = now + datetime.timedelta(seconds=max_age)
            format = "%a, %d-%b-%Y %H:%M:%S GMT"
            expires = datetime.datetime.strftime(delta, format)
            response.set_cookie('last_login', now, expires=expires)
            return response
        else:
            # raise Http404('Wrong password')
            messages.error(request, 'Your username or password is incorrect')
            return redirect('login')


def getshipping(request):
    print("hello")
    dest_latitude = request.POST['latitude']
    dest_longitude = request.POST['longitude']
    auctionid = request.POST['product']
    auctionobj = Auction.objects.filter(pk=request.POST['product'])[0]
    auctionobj_length = auctionobj.length
    auctionobj_width = auctionobj.width
    auctionobj_height = auctionobj.height
    auctionobj_weight = auctionobj.weight

    try:
        data = shipping.calculate_all(auctionobj_length, auctionobj_width,
                                      auctionobj_height, auctionobj_weight, dest_latitude, dest_longitude)
        return JsonResponse(data, safe=False)
    except Exception as e:
        # failed to get shipping data
        return JsonResponse({"status": "failed"})

    


@loggedin
def logout(request, user):
    request.session.flush()
    context = {'appname': appname}
    return render(request, 'website/index.html', context)
