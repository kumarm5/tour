from django.db import models
from django.utils.timezone import now
# Create your models here.

class PassportInfo(models.Model):
    STATUS_CHOICES = (
        ("GENERATED", "GENERATED"),
        ("IN-PROCESS", "IN-PROCESS"),
        ("PENDING", "PENDING"),
        ("COMPLETED", "COMPLETED"),        
    )

    application = models.CharField(max_length=800, null=True, blank=True, verbose_name='Applying for')
    application_type = models.CharField(max_length=800, null=True, blank=True, verbose_name='Type of Application')
    pass_booklet = models.CharField(max_length=800, null=True, blank=True, verbose_name='Type of Passport Booklet')
    given_name = models.CharField(max_length=800, null=True, blank=True, verbose_name='Given Name')
    given_name_surname = models.CharField(max_length=800, verbose_name='Surname')
    gender = models.CharField(max_length=800, null=True, blank=True, verbose_name='Gender')
    other_known_name = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever been known by other names ?')
    name_change = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever changed your name ?')
    date_of_birth = models.CharField(max_length=800, null=True, blank=True, verbose_name='Date of Birth')
    is_place_of_birth = models.CharField(max_length=800, null=True, blank=True, verbose_name='Is your Place of Birth out of India ?')
    place_of_birth = models.CharField(max_length=800, null=True, blank=True, verbose_name='Place of Birth')
    applicant_state = models.CharField(max_length=800, null=True, blank=True, verbose_name='State/UT')
    applicant_district = models.CharField(max_length=800, null=True, blank=True, verbose_name='District')
    applicant_marital_status = models.CharField(max_length=800, null=True, blank=True, verbose_name='Marital Status')
    applicant_citizenship = models.CharField(max_length=800, null=True, blank=True, verbose_name='Citizenship of India by')
    applicant_pan_no = models.CharField(max_length=800, null=True, blank=True, verbose_name='PAN')
    applicant_voter_id = models.CharField(max_length=800, null=True, blank=True, verbose_name='Voter Id')
    emp_type = models.CharField(max_length=800, null=True, blank=True, verbose_name='Employment Type')
    govern_service = models.CharField(max_length=800, null=True, blank=True, verbose_name='Is either of your parent (in case of minor)/spouse, a government servant?')
    educational_qualification = models.CharField(max_length=800, null=True, blank=True, verbose_name='Educational Qualification')
    non_ncr = models.CharField(max_length=800, null=True, blank=True, verbose_name='Is applicant eligible for Non-ECR category ?')
    visible_mark = models.CharField(max_length=800, null=True, blank=True, verbose_name='Visible distinguishing Mark')
    applicant_aadhaar_num = models.CharField(max_length=800, null=True, blank=True, verbose_name='Aadhaar Number')
    family_father_name = models.CharField(max_length=800, null=True, blank=True, verbose_name='Father\'s Given Name')
    family_father_surname = models.CharField(max_length=800, null=True, blank=True, verbose_name='Surname')
    family_mother_name = models.CharField(max_length=800, null=True, blank=True, verbose_name='Mother\'s Given Name')
    family_mother_surname = models.CharField(max_length=800, null=True, blank=True, verbose_name='Surname')
    spouse_name = models.CharField(max_length=800, null=True, blank=True, verbose_name='Spouse\'s Given Name')
    spouse_surname = models.CharField(max_length=800, null=True, blank=True, verbose_name='Surname')
    legal_guardian_given_name = models.CharField(max_length=800, null=True, blank=True, verbose_name='Legal Guardian\'s Given Name')
    legal_guardian_given_surname = models.CharField(max_length=800, null=True, blank=True, verbose_name='Surname')
    father_or_legal_guardian_passport_number = models.CharField(max_length=800, null=True, blank=True, verbose_name='Father/Legal Guardian\'s File/Passport Number')
    father_or_legal_guardian_nationality = models.CharField(max_length=800, null=True, blank=True, verbose_name='Father/Legal Guardian\'s Nationality, If not Indian')
    mother_or_legal_guardian_passport_number = models.CharField(max_length=800, null=True, blank=True, verbose_name='Mother/Legal Guardian\'s File/Passport Number')
    mother_or_legal_guardian_nationality = models.CharField(max_length=800, null=True, blank=True, verbose_name='Mother/Legal Guardian\'s Nationality, If not Indian')
    present_address_out_of_india = models.CharField(max_length=800, null=True, blank=True, verbose_name='Is your present address out of India ?')
    residing_since = models.CharField(max_length=800, null=True, blank=True, verbose_name='Residing Since')
    house_no_and_street_name = models.CharField(max_length=800, null=True, blank=True, verbose_name='House No. and Street Name')
    present_city = models.CharField(max_length=800, null=True, blank=True, verbose_name='Village/Town/City')
    present_state = models.CharField(max_length=800, null=True, blank=True, verbose_name='State/UT')
    present_district = models.CharField(max_length=800, null=True, blank=True, verbose_name='District')
    present_police_station = models.CharField(max_length=800, null=True, blank=True, verbose_name='Police Station')
    present_pin_code = models.CharField(max_length=800, null=True, blank=True, verbose_name='Pin Code')
    present_mob_num = models.CharField(max_length=800, null=True, blank=True, verbose_name='Mobile Number')
    present_tele_num = models.CharField(max_length=800, null=True, blank=True, verbose_name='Telephone Number')
    present_email_id = models.CharField(max_length=800, null=True, blank=True, verbose_name='E-Mail Id')
    present_permanent_add_available = models.CharField(max_length=800, null=True, blank=True, verbose_name='Is Permanent Address Available ?')
    present_permanent_add_same = models.CharField(max_length=800, null=True, blank=True, verbose_name='Is your permanent address same as present address ?')
    emergency_name_and_address = models.CharField(max_length=800, null=True, blank=True, verbose_name='Name and Address')
    emergency_mobile_number = models.CharField(max_length=800, null=True, blank=True, verbose_name='Mobile Number')
    emergency_telephone_number = models.CharField(max_length=800, null=True, blank=True, verbose_name='Telephone Number')
    emergency_email_id = models.CharField(max_length=800, null=True, blank=True, verbose_name='E-Mail Id')
    ever_hold_ic = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever held/hold any Identity Certificate ?')
    da_available = models.CharField(max_length=800, null=True, blank=True, verbose_name='Details of Previous/Current Diplomatic/Official Passport.')
    applied_passport_not_issued = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever applied for passport, but not issued ?')
    criminal_state = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever been charged with criminal proceedings or is any arrest warrant/summon pending before a court in India ?')
    convicted_court = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you at any time during the period of 5 years immediately preceding the date of this application been convicted by a court in India for any criminal offence and sentenced to imprisonment for two years and more ?')
    passport_deny = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever been refused/denied passport ?')
    passport_impounded = models.CharField(max_length=800, null=True, blank=True, verbose_name='Has your passport ever been impounded or revoked ?')
    political_asylum = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever applied for or been granted political asylum to/by any foreign country ?')
    emergency_certificate = models.CharField(max_length=800, null=True, blank=True, verbose_name='Have you ever returned to India on Emergency Certificate (EC) or were ever deported or repatriated ?')
    comment = models.TextField(null=True, blank=True, verbose_name='Comment')
    created_at = models.DateTimeField(default=now, verbose_name='Created At')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="GENERATED")

    def __str__(self):
        return self.given_name

    class Meta:
        verbose_name = 'Passport'
        verbose_name_plural = 'Passports'

