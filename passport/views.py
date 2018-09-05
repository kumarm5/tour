from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from gallery.models import GalleryMenu, GalleryImages
from news.models import NewsInfo
from tour_packages.models import Topics

# Create your views here.

class PassportView(TemplateView):
    def get(self, request, **kwargs):
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'passport.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, **kwargs):
        passport_form = PassportInfo.objects.create(application=request.POST['application'], application_type=request.POST['application_type'], pass_booklet=request.POST['pass_booklet'], given_name=request.POST['given_name'], given_name_surname=request.POST['given_name_surname'], gender=request.POST['gender'], other_known_name=request.POST['other_known_name'], name_change=request.POST['name_change'], date_of_birth=request.POST['date_of_birth'], is_place_of_birth=request.POST['is_place_of_birth'], place_of_birth=request.POST['place_of_birth'], applicant_state=request.POST['applicant_state'], applicant_district=request.POST['applicant_district'], applicant_marital_status=request.POST['applicant_marital_status'], applicant_citizenship=request.POST['applicant_citizenship'], applicant_pan_no=request.POST['applicant_pan_no'], applicant_voter_id=request.POST['applicant_voter_id'], emp_type=request.POST['emp_type'], govern_service=request.POST['govern_service'], educational_qualification=request.POST['educational_qualification'], non_ncr=request.POST['non_ncr'], visible_mark=request.POST['visible_mark'], applicant_aadhaar_num=request.POST['applicant_aadhaar_num'], family_father_name=request.POST['family_father_name'], family_father_surname=request.POST['family_father_surname'], family_mother_name=request.POST['family_mother_name'], family_mother_surname=request.POST['family_mother_surname'], legal_guardian_given_name=request.POST['legal_guardian_given_name'], legal_guardian_given_surname=request.POST['legal_guardian_given_surname'], father_or_legal_guardian_passport_number=request.POST['father_or_legal_guardian_passport_number'], father_or_legal_guardian_nationality=request.POST['father_or_legal_guardian_nationality'], mother_or_legal_guardian_passport_number=request.POST['mother_or_legal_guardian_passport_number'], mother_or_legal_guardian_nationality=request.POST['mother_or_legal_guardian_nationality'], present_address_out_of_india=request.POST['present_address_out_of_india'], residing_since=request.POST['residing_since'], house_no_and_street_name=request.POST['house_no_and_street_name'], present_city=request.POST['present_city'], present_state=request.POST['present_state'], present_district=request.POST['present_district'], present_police_station=request.POST['present_police_station'], present_pin_code=request.POST['present_pin_code'], present_mob_num=request.POST['present_mob_num'], present_tele_num=request.POST['present_tele_num'], present_email_id=request.POST['present_email_id'], present_permanent_add_available=request.POST['present_permanent_add_available'], present_permanent_add_same=request.POST['present_permanent_add_same'], emergency_name_and_address=request.POST['emergency_name_and_address'], emergency_mobile_number=request.POST['emergency_mobile_number'], emergency_telephone_number=request.POST['emergency_telephone_number'], emergency_email_id=request.POST['emergency_email_id'], ever_hold_ic=request.POST['ever_hold_ic'], da_available=request.POST['da_available'], applied_passport_not_issued=request.POST['applied_passport_not_issued'], criminal_state=request.POST['criminal_state'], convicted_court=request.POST['convicted_court'], passport_deny=request.POST['passport_deny'], passport_impounded=request.POST['passport_impounded'], political_asylum=request.POST['political_asylum'], emergency_certificate=request.POST['emergency_certificate'])

        if passport_form:
            html_message = '\
                <br>\
                <p>Regards and Thanks,</p>\
                <p>TTH- Team</p>\
                <p><strong>Tanish Travel Hut</strong></p>\
                <p>Email:&nbsp;<a href="mailto:tanishtravels24@yahoo.co.in" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88159" rel="nofollow" target="_blank">tanishtravels24@yahoo.co.in</a></p>\
                <p>Register yourself&nbsp;&amp; get exciting rates on our Online Travel Portal:&nbsp;<a href="http://tthboutique.com/" rel="nofollow" target="_blank">http://tthboutique.com</a>&nbsp;</p>\
                <p>Website:&nbsp;<a href="http://www.tanishtravelhut.com/" target="_blank">www.tanishtravelhut.com</a></p>\
                <p>Contact&nbsp; :09890176353, 09420177963.</p>\
                <p><strong>FLIGHTS</strong>&nbsp;|<strong>&nbsp;</strong><strong>HOLIDAYS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>CAR RENTALS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;VISAS&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>BUS</strong><strong>&nbsp;|</strong>&nbsp;<strong>HOTELS</strong><strong>&nbsp;</strong><strong>|</strong>&nbsp;<strong>TRAVEL INSURANCE&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>FOREX&nbsp;</strong><strong>| INT&#39;L SIM CARD</strong><strong>|</strong><strong>&nbsp;</strong><strong>PASSPORT ASSISTANCE</strong></p>       <p><strong>-------------------------------------------------------------------------------&nbsp;</strong></p>\
                <p><strong>Tanish Group:</strong></p>\
                <p><strong>TANISH PROPERTY HUT &amp; CONSULTANT PVT LTD / SHWETA&#39;S FOOD / EXPLORA TOURISM</strong><strong>&nbsp;</strong><strong>/ TULSI COLLECTION /</strong></p>\
                <p><strong>JAI &nbsp;ENTERPRISES</strong><strong>/ OPTION FITNESS EQUIPMENT&#39;S</strong></p>\
                <p>Please take care of the environment, print only if necessary.</p>\
                <p><em>Note: This email message is for the sole use of the intended recipient(s) and may contain CONFIDENTIAL and PRIVILEGED information. Any unauthorized review; use, disclosure or distribution is prohibited.&nbsp; If you are not the intended recipient, please contact the sender by reply email and destroy all copies of the original message and any attachments. The recipient should check this email and any attachments for the presence of viruses. Tanish&nbsp;Travel Hut&nbsp;accepts no liability for any damage caused by any virus transmitted by this email.</em></p>'

            given_name = request.POST['given_name']

            html_message = given_name+' has successfully submitted the passport form.'+'<br>'+html_message

            email_message = EmailMessage('Passport Form', html_message, 'tanishtravels24@yahoo.co.in', [],['tanishtravels24@yahoo.co.in'])
            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, 'Passport form has been submitted successfully.')
        else:
            messages.error(request, 'Passport form submission Failed.')

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'passport.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
