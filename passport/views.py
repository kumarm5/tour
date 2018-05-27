from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.contrib import messages

# Create your views here.

class PassportView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'passport.html', context={})

    def post(self, request, **kwargs):
        passport_form = PassportInfo.objects.create(application=request.POST['application'], application_type=request.POST['application_type'], pass_booklet=request.POST['pass_booklet'], given_name=request.POST['given_name'], given_name_surname=request.POST['given_name_surname'], gender=request.POST['gender'], other_known_name=request.POST['other_known_name'], name_change=request.POST['name_change'], date_of_birth=request.POST['date_of_birth'], is_place_of_birth=request.POST['is_place_of_birth'], place_of_birth=request.POST['place_of_birth'], applicant_state=request.POST['applicant_state'], applicant_district=request.POST['applicant_district'], applicant_marital_status=request.POST['applicant_marital_status'], applicant_citizenship=request.POST['applicant_citizenship'], applicant_pan_no=request.POST['applicant_pan_no'], applicant_voter_id=request.POST['applicant_voter_id'], emp_type=request.POST['emp_type'], govern_service=request.POST['govern_service'], educational_qualification=request.POST['educational_qualification'], non_ncr=request.POST['non_ncr'], visible_mark=request.POST['visible_mark'], applicant_aadhaar_num=request.POST['applicant_aadhaar_num'], family_father_name=request.POST['family_father_name'], family_father_surname=request.POST['family_father_surname'], family_mother_name=request.POST['family_mother_name'], family_mother_surname=request.POST['family_mother_surname'], legal_guardian_given_name=request.POST['legal_guardian_given_name'], legal_guardian_given_surname=request.POST['legal_guardian_given_surname'], father_or_legal_guardian_passport_number=request.POST['father_or_legal_guardian_passport_number'], father_or_legal_guardian_nationality=request.POST['father_or_legal_guardian_nationality'], mother_or_legal_guardian_passport_number=request.POST['mother_or_legal_guardian_passport_number'], mother_or_legal_guardian_nationality=request.POST['mother_or_legal_guardian_nationality'], present_address_out_of_india=request.POST['present_address_out_of_india'], residing_since=request.POST['residing_since'], house_no_and_street_name=request.POST['house_no_and_street_name'], present_city=request.POST['present_city'], present_state=request.POST['present_state'], present_district=request.POST['present_district'], present_police_station=request.POST['present_police_station'], present_pin_code=request.POST['present_pin_code'], present_mob_num=request.POST['present_mob_num'], present_tele_num=request.POST['present_tele_num'], present_email_id=request.POST['present_email_id'], present_permanent_add_available=request.POST['present_permanent_add_available'], present_permanent_add_same=request.POST['present_permanent_add_same'], emergency_name_and_address=request.POST['emergency_name_and_address'], emergency_mobile_number=request.POST['emergency_mobile_number'], emergency_telephone_number=request.POST['emergency_telephone_number'], emergency_email_id=request.POST['emergency_email_id'], ever_hold_ic=request.POST['ever_hold_ic'], da_available=request.POST['da_available'], applied_passport_not_issued=request.POST['applied_passport_not_issued'], criminal_state=request.POST['criminal_state'], convicted_court=request.POST['convicted_court'], passport_deny=request.POST['passport_deny'], passport_impounded=request.POST['passport_impounded'], political_asylum=request.POST['political_asylum'], emergency_certificate=request.POST['emergency_certificate'])

        if passport_form:
            messages.success(request, 'Passport form has been submitted successfully.')
        else:
            messages.error(request, 'Passport form submission Failed.')


        return render(request, 'passport.html', context={})
