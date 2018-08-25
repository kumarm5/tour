from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from django.core.mail import EmailMessage
from news.models import NewsInfo

# Create your views here.

class CabRentalCities(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        cities = Cities.objects.all()
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'cab-rental-cities.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'cities': cities, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class Tariff(TemplateView):
    def get(self, request, *args, **kwargs):
        city_id = kwargs['id']

        try:
            city_detail = Cities.objects.get(pk=city_id)
        except:
            city_detail = None

        try:
            term_and_cond = TermsAndCondition.objects.get(city = city_id)
        except:
            term_and_cond = None

        tariff_details = TariffDetails.objects.filter(pk=city_id)

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        return render(request, 'car-tariff.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond, 'city_detail': city_detail, 'tariff_details': tariff_details, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class TariffDetailEnquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        tariff_id = kwargs['id']

        try:
            tariff_detail = TariffDetails.objects.get(pk=tariff_id)
        except:
            tariff_detail = None

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        return render(request, 'tariff-enquiry.html', context={ 'tariff_detail': tariff_detail, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        tariff_enquiry = TariffEnquiry.objects.create(username = username, mobile_num = mobile_num, email_id = email_id, subject = subject, message = message)

        if tariff_enquiry:
            html_message = '\
                <br>\
                <p>Regards and Thanks,</p>\
                <p>Jai D Solanki&nbsp;<strong>(Managing&nbsp;Partner)</strong></p>\
                <p><strong>Tanish Travel Hut</strong></p>\
                <p><strong>HO :</strong>&nbsp;Sr No: 33, Ceratec City, Ph-2, No: 702 ,</p>\
                <p>D wing , Katraj Kondhwa Road,</p>\
                <p>Tilekar Nagar, Yewalewadi, Pune -411048.</p>\
                <p>Email:&nbsp;<a href="mailto:tanishtravels24@yahoo.co.in" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88159" rel="nofollow" target="_blank">tanishtravels24@yahoo.co.in</a></p>\
                <p>Only&nbsp;For Acc.Use:&nbsp;<a href="mailto:accounts.tanishtravels@yahoo.com" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88156" rel="nofollow" target="_blank">accounts.tanishtravels@yahoo.com</a></p>\
                <p>Register yourself&nbsp;&amp; get exciting rates on our Online Travel Portal:&nbsp;<a href="http://tthboutique.com/" rel="nofollow" target="_blank">http://tthboutique.com</a>&nbsp;</p>\
                <p>Website:&nbsp;<a href="http://www.tanishtravelhut.com/" target="_blank">www.tanishtravelhut.com</a></p>\
                <p>Contact&nbsp; :09890176353, 09420177963.</p>\
                <p><strong>FLIGHTS</strong>&nbsp;|<strong>&nbsp;</strong><strong>HOLIDAYS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>CAR RENTALS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;VISAS&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>BUS</strong><strong>&nbsp;|</strong>&nbsp;<strong>HOTELS</strong><strong>&nbsp;</strong><strong>|</strong>&nbsp;<strong>TRAVEL INSURANCE&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>FOREX&nbsp;</strong><strong>| INT&#39;L SIM CARD</strong></p>\
                <p><strong>Download our Mobile App from play store type. Tanish Travel hut</strong></p>\
                <p><strong>Like our Face book page:&nbsp;<a href="https://www.facebook.com/tanishtravelhutpune/" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_87994" rel="nofollow" target="_blank">https://www.facebook.com/tanishtravelhutpune/</a></strong></p>\
                <p>Linked&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;:&nbsp;<a href="http://www.linkedin.com/in/tanishtravelhutpune/" target="_blank">www.linkedin.com/in/tanishtravelhutpune/</a>&nbsp;</p>\
                <p><strong>Twitter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :&nbsp;<a href="http://twitter.com/tanishtravelhut" target="_blank">twitter.com/tanishtravelhut</a></strong></p>\
                <p><strong>Instagram&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;:&nbsp;<a href="http://www.instagram.com/jaisolanki24/" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88335" rel="nofollow" target="_blank">www.instagram.com/tanishtravelhutpune/</a></strong></p>\
                <p><strong>Skype&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp;<a href="http://www.instagram.com/jaisolanki24/" rel="nofollow" target="_blank">jaisolanki2012/</a></strong></p>\
                <p><strong>Save No. In your Mobile:&nbsp;09890176353&nbsp;to get latest offers &amp; Updates.</strong></p>\
                <p><strong>-------------------------------------------------------------------------------&nbsp;</strong></p>\
                <p><strong>Tanish Group:</strong></p>\
                <p><strong>TANISH PROPERTY HUT &amp; CONSULTANT PVT LTD / SHWETA&#39;S FOOD / EXPLORA TOURISM</strong><strong>&nbsp;</strong><strong>/ TULSI COLLECTION /</strong></p>\
                <p><strong>JAI &nbsp;ENTERPRISES</strong><strong>/ OPTION FITNESS EQUIPMENT&#39;S</strong></p>\
                <p><strong>P</strong>&nbsp;Please take care of the environment, print only if necessary.</p>\
                <p><em>Note: This email message is for the sole use of the intended recipient(s) and may contain CONFIDENTIAL and PRIVILEGED information. Any unauthorized review; use, disclosure or distribution is prohibited.&nbsp; If you are not the intended recipient, please contact the sender by reply email and destroy all copies of the original message and any attachments. The recipient should check this email and any attachments for the presence of viruses. Tanish&nbsp;Travel Hut&nbsp;accepts no liability for any damage caused by any virus transmitted by this email.</em></p>'

            html_message = 'User Name is '+username+'<br>Mobile Number is '+mobile_num+'<br>Email Id is '+email_id+'<br>Subject is '+subject+'<br>Message is '+message+'<br>'+html_message

            email_message = EmailMessage(subject, html_message, 'tanishtravels24@yahoo.co.in', [email_id],['tanishtravels24@yahoo.co.in'])
            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, 'Enquiry has been sent successfully.')
        else:
            messages.error(request, 'Enquiry Failed.')

        tariff_id = kwargs['id']

        try:
            tariff_detail = TariffDetails.objects.get(pk=tariff_id)
        except:
            tariff_detail = None
        
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        return render(request, 'tariff-enquiry.html', context={ 'tariff_detail': tariff_detail, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class CabRegisteration(TemplateView):
    def get(self, request, *args, **kwargs):
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'cab-registeration.html', context={ 'footer_news': footer_news, 'footer_galleries': footer_galleries })
        
    def post(self, request, *args, **kwargs):
        
        agency_name = request.POST.get('agency_name')
        full_name = request.POST.get('full_name')
        mobile_no = request.POST.get('mobile_no')
        email_id = request.POST.get('email_id')
        bank_name = request.POST.get('bank_name')
        account_no = request.POST.get('account_no')
        name_in_account = request.POST.get('name_in_account')
        ifsc_code = request.POST.get('ifsc_code')
        branch = request.POST.get('branch')
        address = request.POST.get('address')

        register = CabRegister.objects.create(agency_name=agency_name, full_name=full_name, mobile_no=mobile_no, email_id=email_id, bank_name=bank_name, account_no=account_no, name_in_account=name_in_account, ifsc_code=ifsc_code, branch=branch, address=address)

        cabreg = CabRegister.objects.last()
        type_veh = request.POST.getlist('type_veh')
        purchase_date = request.POST.getlist('purchase_date')
        cab_no = request.POST.getlist('cab_no')

        for i in range(len(cab_no)):
            RegisterVehicle.objects.create(cabregister=register, type_vehicle=type_veh[i], purchase_date=purchase_date[i], cab_no=cab_no[i])

        if register:
            html_message = '\
                <br>\
                <p>Regards and Thanks,</p>\
                <p>Jai D Solanki&nbsp;<strong>(Managing&nbsp;Partner)</strong></p>\
                <p><strong>Tanish Travel Hut</strong></p>\
                <p><strong>HO :</strong>&nbsp;Sr No: 33, Ceratec City, Ph-2, No: 702 ,</p>\
                <p>D wing , Katraj Kondhwa Road,</p>\
                <p>Tilekar Nagar, Yewalewadi, Pune -411048.</p>\
                <p>Email:&nbsp;<a href="mailto:tanishtravels24@yahoo.co.in" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88159" rel="nofollow" target="_blank">tanishtravels24@yahoo.co.in</a></p>\
                <p>Only&nbsp;For Acc.Use:&nbsp;<a href="mailto:accounts.tanishtravels@yahoo.com" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88156" rel="nofollow" target="_blank">accounts.tanishtravels@yahoo.com</a></p>\
                <p>Register yourself&nbsp;&amp; get exciting rates on our Online Travel Portal:&nbsp;<a href="http://tthboutique.com/" rel="nofollow" target="_blank">http://tthboutique.com</a>&nbsp;</p>\
                <p>Website:&nbsp;<a href="http://www.tanishtravelhut.com/" target="_blank">www.tanishtravelhut.com</a></p>\
                <p>Contact&nbsp; :09890176353, 09420177963.</p>\
                <p><strong>FLIGHTS</strong>&nbsp;|<strong>&nbsp;</strong><strong>HOLIDAYS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>CAR RENTALS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;VISAS&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>BUS</strong><strong>&nbsp;|</strong>&nbsp;<strong>HOTELS</strong><strong>&nbsp;</strong><strong>|</strong>&nbsp;<strong>TRAVEL INSURANCE&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>FOREX&nbsp;</strong><strong>| INT&#39;L SIM CARD</strong></p>\
                <p><strong>Download our Mobile App from play store type. Tanish Travel hut</strong></p>\
                <p><strong>Like our Face book page:&nbsp;<a href="https://www.facebook.com/tanishtravelhutpune/" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_87994" rel="nofollow" target="_blank">https://www.facebook.com/tanishtravelhutpune/</a></strong></p>\
                <p>Linked&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;:&nbsp;<a href="http://www.linkedin.com/in/tanishtravelhutpune/" target="_blank">www.linkedin.com/in/tanishtravelhutpune/</a>&nbsp;</p>\
                <p><strong>Twitter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :&nbsp;<a href="http://twitter.com/tanishtravelhut" target="_blank">twitter.com/tanishtravelhut</a></strong></p>\
                <p><strong>Instagram&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;:&nbsp;<a href="http://www.instagram.com/jaisolanki24/" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88335" rel="nofollow" target="_blank">www.instagram.com/tanishtravelhutpune/</a></strong></p>\
                <p><strong>Skype&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp;<a href="http://www.instagram.com/jaisolanki24/" rel="nofollow" target="_blank">jaisolanki2012/</a></strong></p>\
                <p><strong>Save No. In your Mobile:&nbsp;09890176353&nbsp;to get latest offers &amp; Updates.</strong></p>\
                <p><strong>-------------------------------------------------------------------------------&nbsp;</strong></p>\
                <p><strong>Tanish Group:</strong></p>\
                <p><strong>TANISH PROPERTY HUT &amp; CONSULTANT PVT LTD / SHWETA&#39;S FOOD / EXPLORA TOURISM</strong><strong>&nbsp;</strong><strong>/ TULSI COLLECTION /</strong></p>\
                <p><strong>JAI &nbsp;ENTERPRISES</strong><strong>/ OPTION FITNESS EQUIPMENT&#39;S</strong></p>\
                <p><strong>P</strong>&nbsp;Please take care of the environment, print only if necessary.</p>\
                <p><em>Note: This email message is for the sole use of the intended recipient(s) and may contain CONFIDENTIAL and PRIVILEGED information. Any unauthorized review; use, disclosure or distribution is prohibited.&nbsp; If you are not the intended recipient, please contact the sender by reply email and destroy all copies of the original message and any attachments. The recipient should check this email and any attachments for the presence of viruses. Tanish&nbsp;Travel Hut&nbsp;accepts no liability for any damage caused by any virus transmitted by this email.</em></p>'

            html_message = 'Agency Name: '+agency_name+'<br>'+'Full Name: '+full_name+'<br>'+'Mobile No: '+mobile_no+'<br>'+'Email Id: '+email_id+'<br>'+html_message

            msg = EmailMessage('Cab Registration', html_message, 'tanishtravels24@yahoo.co.in', [],['tanishtravels24@yahoo.co.in'])
            msg.content_subtype = "html"
            msg.send()

            messages.success(request, 'Cab registration successful')
        else:
            messages.error(request, 'Cab registration failed')

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        return render(request, 'cab-registeration.html', context={ 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class PickDropLive(TemplateView):
    def get(self, request, *args, **kwargs):
        timechange = TimeChange.objects.last()
        term_and_cond = PickUpDropLiveTerms.objects.last()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        pickdroplivetrip = PickDropLiveTrip.objects.filter(status = True)

        return render(request, 'pick-drop-live.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond, 'timechange': timechange, 'footer_news': footer_news, 'footer_galleries': footer_galleries, 'pickdroplivetrip': pickdroplivetrip })

    def post(self, request, *args, **kwargs):
        term_and_cond = PickUpDropLiveTerms.objects.last()
        timechange = TimeChange.objects.last()

        booking_type = request.POST.get('formname')
        airport = request.POST.get('airport')
        pick_up_point = request.POST.get('pick_up_point')
        trip_route = request.POST.get('trip_route')
        num_of_seats = request.POST.get('num_of_seats') 
        flight_date = request.POST.get('flight_date')

        flight_hr = request.POST.get('flight_hr')
        flight_min = request.POST.get('flight_min')

        flight_time = flight_hr+':'+flight_min

        cab_date = request.POST.get('cab_date')
        cab_departure_time = request.POST.get('cab_departure_time')
        cab_pickup_time = request.POST.get('cab_pickup_time')
        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pick_up_address = request.POST.get('pick_up_address')
        drop_address = request.POST.get('drop_address')
        message = request.POST.get('message')

        try:
            pickupdroplive = PickUpDropLive.objects.create(booking_type = booking_type, airport = airport, pick_up_point = pick_up_point, trip_route = trip_route, num_of_seats = num_of_seats, flight_date = flight_date, flight_time = flight_time, cab_date = cab_date,  cab_departure_time = cab_departure_time, cab_pickup_time = cab_pickup_time, mobile_num = mobile_num, email_id = email_id, first_name = first_name, last_name = last_name, pick_up_address = pick_up_address, drop_address = drop_address, message = message)
        except:
            pickupdroplive = None

        if pickupdroplive:
            messages.success(request, 'Request has been sent successfully.')
        else:
            messages.error(request, 'Request Failed.')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        pickdroplivetrip = PickDropLiveTrip.objects.filter(status = True)

        return render(request, 'pick-drop-live.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond, 'timechange': timechange, 'footer_news': footer_news, 'footer_galleries': footer_galleries, 'pickdroplivetrip': pickdroplivetrip })

class ExtraPickDrop(TemplateView):
    def get(self, request, *args, **kwargs):
        term_and_cond = ExtraPickUpDropTerms.objects.last()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        return render(request, 'extra-pick-drop.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, *args, **kwargs):
        term_and_cond = TermsAndCondition.objects.last()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        vehicle_id = request.POST.get('vehicle_id')

        route_vehicle = ExtraPickUpDrop.objects.get(pk=vehicle_id)

        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pick_up_date = request.POST.get('pick_up_date')
        pick_up_time = request.POST.get('pick_up_time')
        pickup_address_with_landmark = request.POST.get('pickup_address_with_landmark')
        drop_address_with_landmark = request.POST.get('drop_address_with_landmark')
        message = request.POST.get('message')

        vehicle_request = ExtraPickUpDropRequest.objects.create(route_vehicle = route_vehicle, mobile_num = mobile_num,  email_id = email_id, first_name = first_name, last_name = last_name, pick_up_date = pick_up_date, pick_up_time = pick_up_time, pickup_address_with_landmark = pickup_address_with_landmark, drop_address_with_landmark = drop_address_with_landmark, message = message)

        if vehicle_request:
            messages.success(request, 'Request has been sent successfully.')
        else:
            messages.error(request, 'Request Failed.')

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        return render(request, 'extra-pick-drop.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

def get_vehicles(request):
    vehiclemaster = VehicleMaster.objects.all().values('vehicle_name')
    vehicles = list(vehiclemaster)
    return JsonResponse(vehicles, safe=False)

def get_from_location(request):
    fromlocation = ExtraPickUpDrop.objects.all().values('fromlocation').distinct()
    fromlocation = list(fromlocation)
    return JsonResponse(fromlocation, safe=False)

def get_to_location(request):
    tolocation = ExtraPickUpDrop.objects.all().values('tolocation').distinct()
    tolocation = list(tolocation)
    return JsonResponse(tolocation, safe=False)

def get_extra_vehicle(request, *args, **kwargs):
    from_location = request.GET.get('from_location')
    to_location = request.GET.get('to_location')
    extra_vehicle = ExtraPickUpDrop.objects.filter(fromlocation = from_location, tolocation = to_location).values('id','vehicleimage','vehiclename','vehiclecategory','vehicleprice','status')
    extra_vehicle = list(extra_vehicle)
    return JsonResponse(extra_vehicle, safe=False)
