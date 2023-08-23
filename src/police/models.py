from django.db import models
from django.contrib.auth.models import User
# from case.models import Case


def image_upload_location(instance, filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_images/%Y/%m/%d/', filename)

def video_upload_location(instance, filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_videos/%Y/%m/%d/', filename)

def doc_upload_location(instance, filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_docs/%Y/%m/%d/', filename)

def audio_upload_location(instance, filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_audios/%Y/%m/%d/', filename)


designation_choice = (
    ('DGP', 'Director General of Police'),
    ('ADGP', 'Addl. Director General of Police'),
    ('IGP', 'Inspector General of Police'),
    ('DIGP', 'Deputy Inspector General of Police'),
    ('SPDCP', 'Superintendent of police Deputy Commissioner of Police(Selection Grade)'),
    ('SPDCPJ', 'Superintendent of police Deputy Commissioner of Police(Junior Management Grade)'),
    ('ASPADCP', 'Addl. Superintendent of police Addl.Deputy Commissioner of Police'),
    ('ASP', 'Assistant Superintendent of Police'),
    ('INSP', 'Inspector of Police'),
    ('SUB_INSP', 'Sub Inspector of Police.'),
    ('HVLDRM', 'Asst. Sub. Inspector/Havildar Major'),
    ('HVLDR', 'Havildar.'),
    ('LN', 'Lance Naik.'),
    ('CONS', 'Constable.'),
)


class Police(User):
    police_id = models.CharField(max_length=20)
    designation = models.CharField(max_length=10, choices=designation_choice, null=True)
    ward = models.ForeignKey('Ward', null=True, on_delete=models.SET_NULL)  # Add on_delete argument
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Police'

    def __str__(self):
        return self.username


ward_choice = (
    ('RJ14W01', 'Mansarovar'),
    ('RJ14W02', 'Jagatpura'),
    ('RJ14W03', 'Sanganer'),
    ('RJ14W04', 'Kachi Basti'),
    ('RJ14W05', 'Malviya Nagar'),
    ('RJ14W06', 'Bani Park'),
    ('RJ14W07', 'Sitapura'),
    ('RJ14W08', 'Raja Park'),
    ('RJ14W09', 'Triveni Nagar'),
    ('RJ14W10', 'Badi Chopat'),
    ('RJ14W11', 'Chandpole'),
)


class Ward(models.Model):
    id = models.CharField(max_length=10, primary_key=True, choices=ward_choice)
    address = models.CharField(max_length=255, blank=False)

    def get_contacts(self):
        contact_list = [i.contact for i in Ward.objects.get(id=self.id).contact_set]
        return contact_list

    def __str__(self):
        return self.id


class Contact(models.Model):
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE)
    contact = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.ward


class Criminal(models.Model):
    name = models.CharField(max_length=255, blank=False)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField()
    caste = models.CharField(max_length=255)
    ward = models.ForeignKey(Ward, null=True, on_delete=models.SET_NULL)
    birth_mark_desc = models.TextField()
    height = models.CharField(max_length=255)
    complexion = models.CharField(max_length=255)
    eyes = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Evidence(models.Model):
    case = models.ForeignKey('case.Case', blank=True, null=True, on_delete=models.SET_NULL, related_name='police_evidence')
    evidence_type = models.CharField(max_length=255)
    details = models.TextField()
    image = models.ImageField(upload_to=image_upload_location, null=True, blank=True)
    video = models.FileField(upload_to=video_upload_location, null=True, blank=True)
    document = models.FileField(upload_to=doc_upload_location, null=True, blank=True)
    audio = models.FileField(upload_to=audio_upload_location, null=True, blank=True)

    def __str__(self):
        return self.details
