from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class hr_mas_org(models.Model):
    org_name = models.CharField(max_length=80, db_index=True, default=None)
    org_address1 = models.CharField(max_length=80, db_index=True, null=True)
    org_address2 = models.CharField(max_length=80, db_index=True, null=True)
    org_address3 = models.CharField(max_length=80, db_index=True, null=True)
    org_city = models.CharField(max_length=50, db_index=True, null=True)
    org_state = models.CharField(max_length=50, db_index=True, null=True)
    org_pincode = models.CharField(max_length=6, db_index=True, null=True)
    
class hr_mas_loc(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='locations')
    location = models.CharField(max_length=55, default=None, db_index=True)

class hr_mas_dept(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='departments')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='departments')
    department = models.CharField(max_length=55, default=None, db_index=True)
    
class hr_mas_grade(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='grade')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='grade')
    grade = models.CharField(max_length=55, default=None, db_index=True)

class hr_mas_subdept(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='subdepartments')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='subdepartments')
    subdepartment = models.CharField(max_length=55, default=None, db_index=True)

class hr_mas_desig(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='designations')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='designations')
    designation = models.CharField(max_length=55, default=None, db_index=True)

class hr_mas_cadre(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='cadres')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='cadres_location')
    card = models.CharField(max_length=55, db_index=True, default=None)

class hr_mas_section(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='sections')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='sections_location')
    section = models.CharField(max_length=55, db_index=True, default=None)

class hr_mas_subsection(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='subsections')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='subsections_location')
    sub_section = models.CharField(max_length=55, db_index=True, default=None)
    
    
class hr_mas_division(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='division')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='division')
    division = models.CharField(max_length=55, db_index=True, default=None)
    
class hr_mas_costcentre(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='cost')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='cost')
    costcentre = models.CharField(max_length=55, db_index=True, default=None)
    
    
class hr_mas_company(models.Model):
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='company')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='company')
    
    company = models.CharField(max_length=65, db_index=True, default=None, null=True, blank=True)
    area = models.CharField(max_length=55, db_index=True, default=None, null=True)
    city = models.CharField(max_length=55, db_index=True, default=None, null=True)
    state = models.CharField(max_length=55, db_index=True, default=None, null=True)
    pincode = models.CharField(max_length=6, db_index=True, default=None, null=True)
    phone = models.CharField(max_length=55, db_index=True, default=None, null=True)
    
    email = models.EmailField(max_length=55, db_index=True, default=None, null=True)
    pfcodeno = models.CharField(max_length=55, db_index=True, default=None, null=True)
    esicodeno = models.CharField(max_length=55, db_index=True, default=None, null=True)
    
    emprdesignation = models.CharField(max_length=55, db_index=True, default=None, null=True)
    emprraddress1 = models.CharField(max_length=55, db_index=True, default=None, null=True)
    # Done till
    emprraddress2 = models.CharField(max_length=55, db_index=True, default=None, null=True)
    emprraddress3 = models.CharField(max_length=55, db_index=True, default=None, null=True)
    esilocaloffice = models.CharField(max_length=55, db_index=True, default=None, null=True)
    esistation = models.CharField(max_length=55, db_index=True, default=None, null=True)
    addressline = models.CharField(max_length=120, db_index=True, default=None, null=True)
    location = models.CharField(max_length=55, db_index=True, default=None, null=True)
    dayscalc = models.DecimalField(max_digits=7, decimal_places=2, db_index=True, default=None, null=True)
    namemanager = models.CharField(max_length=120, db_index=True, default=None, null=True)
    district = models.CharField(max_length=120, db_index=True, default=None, null=True)
    faclicenceno = models.CharField(max_length=120, db_index=True, default=None, null=True)
    dooe = models.DateField(db_index=True, default=None, null=True)
    doce = models.DateField(db_index=True, default=None, null=True)
    mbonus = models.CharField(max_length=1, db_index=True, default=None, null=True)
    compprefix = models.CharField(max_length=5, db_index=True, default=None, null=True)


class HrEmpsInfo(models.Model):
    empid = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    emp_pro_pic = models.ImageField(upload_to='employees/pics', default='/static/media/person.svg')
    nationallity = models.CharField(max_length=20, null=True, default=None)
    religion = models.CharField(max_length=3, null=True, default=None)
    pancardno = models.CharField(max_length=25, null=True, default=None)
    voteridno = models.CharField(max_length=25, null=True, default=None)
    dvlicenceno = models.CharField(max_length=25, null=True, default=None)
    passportno = models.CharField(max_length=25, null=True, default=None)
    docno = models.CharField(max_length=25, null=True, default=None)
    pricontactno = models.CharField(max_length=25, null=True, default=None)
    seccontactno = models.CharField(max_length=25, null=True, default=None)
    address1 = models.CharField(max_length=55, null=True, default=None)
    address2 = models.CharField(max_length=55, null=True, default=None)
    address3 = models.CharField(max_length=55, null=True, default=None)
    city = models.CharField(max_length=55, null=True, default=None)
    state = models.CharField(max_length=55, null=True, default=None)
    pincode = models.CharField(max_length=10, null=True, default=None)
    peaddress1 = models.CharField(max_length=55, null=True, default=None)
    peaddress2 = models.CharField(max_length=55, null=True, default=None)
    peaddress3 = models.CharField(max_length=55, null=True, default=None)
    pecity = models.CharField(max_length=55, null=True, default=None)
    pestate = models.CharField(max_length=55, null=True, default=None)
    pepincode = models.CharField(max_length=10, null=True, default=None)
    languesknown = models.CharField(max_length=70, null=True, default=None)
    height = models.CharField(max_length=20, null=True, default=None)
    weight = models.CharField(max_length=20, null=True, default=None)
    idmark = models.CharField(max_length=40, null=True, default=None)
    langspeak = models.CharField(max_length=55, null=True, default=None)
    langread = models.CharField(max_length=55, null=True, default=None)
    langwrite = models.CharField(max_length=55, null=True, default=None)
    educat1 = models.CharField(max_length=55, null=True, default=None)
    educat1year = models.CharField(max_length=10, null=True, default=None)
    educat1div = models.CharField(max_length=10, null=True, default=None)
    educat1per = models.CharField(max_length=10, null=True, default=None)
    educat2 = models.CharField(max_length=55, null=True, default=None)
    educat2year = models.CharField(max_length=10, null=True, default=None)
    educat2div = models.CharField(max_length=10, null=True, default=None)
    educat2per = models.CharField(max_length=10, null=True, default=None)
    educat3 = models.CharField(max_length=55, null=True, default=None)
    educat3year = models.CharField(max_length=10, null=True, default=None)
    educat3div = models.CharField(max_length=10, null=True, default=None)
    educat3per = models.CharField(max_length=10, null=True, default=None)
    educat4 = models.CharField(max_length=55, null=True, default=None)
    educat4year = models.CharField(max_length=10, null=True, default=None)
    educat4div = models.CharField(max_length=10, null=True, default=None)
    educat4per = models.CharField(max_length=10, null=True, default=None)
    educat5 = models.CharField(max_length=55, null=True, default=None)
    educat5year = models.CharField(max_length=10, null=True, default=None)
    educat5div = models.CharField(max_length=10, null=True, default=None)
    educat5per = models.CharField(max_length=10, null=True, default=None)
    educat6 = models.CharField(max_length=55, null=True, default=None)
    educat6year = models.CharField(max_length=10, null=True, default=None)
    educat6div = models.CharField(max_length=10, null=True, default=None)
    educat6per = models.CharField(max_length=10, null=True, default=None)
    educat7 = models.CharField(max_length=55, null=True, default=None)
    educat7year = models.CharField(max_length=10, null=True, default=None)
    educat7div = models.CharField(max_length=10, null=True, default=None)
    educat7per = models.CharField(max_length=10, null=True, default=None)
    totalexperience = models.CharField(max_length=10, null=True, default=None)
    employer1 = models.CharField(max_length=55, null=True, default=None)
    post1 = models.CharField(max_length=30, null=True, default=None)
    fromto1 = models.CharField(max_length=20, null=True, default=None)
    reason1 = models.CharField(max_length=20, null=True, default=None)
    employer2 = models.CharField(max_length=55, null=True, default=None)
    post2 = models.CharField(max_length=30, null=True, default=None)
    fromto2 = models.CharField(max_length=20, null=True, default=None)
    reason2 = models.CharField(max_length=20, null=True, default=None)
    employer3 = models.CharField(max_length=55, null=True, default=None)
    post3 = models.CharField(max_length=30, null=True, default=None)
    fromto3 = models.CharField(max_length=20, null=True, default=None)
    reason3 = models.CharField(max_length=20, null=True, default=None)
    employer4 = models.CharField(max_length=55, null=True, default=None)
    post4 = models.CharField(max_length=30, null=True, default=None)
    fromto4 = models.CharField(max_length=20, null=True, default=None)
    reason4 = models.CharField(max_length=20, null=True, default=None)
    employer5 = models.CharField(max_length=55, null=True, default=None)
    post5 = models.CharField(max_length=30, null=True, default=None)
    fromto5 = models.CharField(max_length=20, null=True, default=None)
    reason5 = models.CharField(max_length=20, null=True, default=None)
    employer6 = models.CharField(max_length=55, null=True, default=None)
    post6 = models.CharField(max_length=30, null=True, default=None)
    fromto6 = models.CharField(max_length=20, null=True, default=None)
    reason6 = models.CharField(max_length=20, null=True, default=None)
    relative1 = models.CharField(max_length=55, null=True, default=None)
    ageyob1 = models.CharField(max_length=12, null=True, default=None)
    relation1 = models.CharField(max_length=12, null=True, default=None)
    relative1pro = models.CharField(max_length=25, null=True, default=None)
    relative2 = models.CharField(max_length=55, null=True, default=None)
    ageyob2 = models.CharField(max_length=12, null=True, default=None)
    relation2 = models.CharField(max_length=12, null=True, default=None)
    relative2pro = models.CharField(max_length=25, null=True, default=None)
    relative3 = models.CharField(max_length=55, null=True, default=None)
    ageyob3 = models.CharField(max_length=12, null=True, default=None)
    relation3 = models.CharField(max_length=12, null=True, default=None)
    relative3pro = models.CharField(max_length=25, null=True, default=None)
    relative4 = models.CharField(max_length=55, null=True, default=None)
    ageyob4 = models.CharField(max_length=12, null=True, default=None)
    relation4 = models.CharField(max_length=12, null=True, default=None)
    relative4pro = models.CharField(max_length=25, null=True, default=None)
    relative5 = models.CharField(max_length=55, null=True, default=None)
    ageyob5 = models.CharField(max_length=12, null=True, default=None)
    relation5 = models.CharField(max_length=12, null=True, default=None)
    relative5pro = models.CharField(max_length=25, null=True, default=None)
    relative6 = models.CharField(max_length=55, null=True, default=None)
    ageyob6 = models.CharField(max_length=12, null=True, default=None)
    relation6 = models.CharField(max_length=12, null=True, default=None)
    relative6pro = models.CharField(max_length=25, null=True, default=None)
    relative7 = models.CharField(max_length=55, null=True, default=None)
    ageyob7 = models.CharField(max_length=12, null=True, default=None)
    relation7 = models.CharField(max_length=12, null=True, default=None)
    relative7pro = models.CharField(max_length=25, null=True, default=None)
    relative8 = models.CharField(max_length=55, null=True, default=None)
    ageyob8 = models.CharField(max_length=12, null=True, default=None)
    relation8 = models.CharField(max_length=12, null=True, default=None)
    relative8pro = models.CharField(max_length=25, null=True, default=None)
    relative9 = models.CharField(max_length=55, null=True, default=None)
    ageyob9 = models.CharField(max_length=12, null=True, default=None)
    relation9 = models.CharField(max_length=12, null=True, default=None)
    relative9pro = models.CharField(max_length=25, null=True, default=None)
    esino = models.CharField(max_length=55, null=True, default=None)
    esiempr = models.CharField(max_length=55, null=True, default=None)
    localoffice = models.CharField(max_length=55, null=True, default=None)
    esinomi = models.CharField(max_length=12, null=True, default=None)
    esipartic = models.CharField(max_length=25, null=True, default=None)
    esifamily = models.CharField(max_length=25, null=True, default=None)
    pfacno = models.CharField(max_length=25, null=True, default=None)
    pfnomes = models.CharField(max_length=25, null=True, default=None)
    pfshares = models.CharField(max_length=25, null=True, default=None)
    pfcpension = models.CharField(max_length=25, null=True, default=None)
    pfwpension = models.CharField(max_length=25, null=True, default=None)
    granomes = models.CharField(max_length=12, null=True, default=None)
    grashares = models.CharField(max_length=25, null=True, default=None)
    witness1 = models.CharField(max_length=55, null=True, default=None)
    witness1add = models.CharField(max_length=120, null=True, default=None)
    witness2 = models.CharField(max_length=55, null=True, default=None)
    witness2add = models.CharField(max_length=120, null=True, default=None)
    anyrelative = models.CharField(max_length=1, null=True, default=None)
    relativename = models.CharField(max_length=55, null=True, default=None)
    relationship = models.CharField(max_length=20, null=True, default=None)

    class Meta:
        unique_together = ('empid',)


class hr_emps(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    org_id = models.ForeignKey(hr_mas_org, on_delete=models.CASCADE, related_name='employees')
    loc_id = models.ForeignKey(hr_mas_loc, on_delete=models.CASCADE, related_name='employees_locations')
    
    dept_id = models.ForeignKey(hr_mas_dept, on_delete=models.CASCADE, related_name='employees_departments', null=True)
    subdept_id = models.ForeignKey(hr_mas_subdept, on_delete=models.CASCADE, related_name='employees_subdepartments', null=True)
    desig_id = models.ForeignKey(hr_mas_desig, on_delete=models.CASCADE, related_name='employees_designations', null=True)
    sect_id = models.ForeignKey(hr_mas_section, on_delete=models.CASCADE, related_name='employees_sections', null=True)
    subsec_id = models.ForeignKey(hr_mas_subsection, on_delete=models.CASCADE, related_name='employees_subsections', null=True)
    cadre_id = models.ForeignKey(hr_mas_cadre, on_delete=models.CASCADE, related_name='employees_cadres', null=True)
    grade_id = models.ForeignKey(hr_mas_grade, on_delete=models.CASCADE, related_name='employees_grade', null=True)
    div_id = models.ForeignKey(hr_mas_division, on_delete=models.CASCADE, related_name='employees_division', null=True)
    cost_id = models.ForeignKey(hr_mas_costcentre, on_delete=models.CASCADE, related_name='employees_cost', null=True)
    comp_id = models.ForeignKey(hr_mas_company, on_delete=models.CASCADE, related_name='employees_company', null=True)
    emp_info_dbsf = models.ForeignKey(HrEmpsInfo, on_delete=models.CASCADE, default="", related_name='employees_info')
    emp_name = models.CharField(max_length=80, db_index=True, default=None, null=True)
    card = models.CharField(max_length=12, db_index=True, default=None, null=True)
    emptitle = models.CharField(max_length=10, db_index=True, default=None, null=True)
    empname = models.CharField(max_length=55, db_index=True, default=None, null=True)
    fhname = models.CharField(max_length=55, db_index=True, default=None, null=True)
    fhflag = models.CharField(max_length=1, db_index=True, default=None, null=True)
    mname = models.CharField(max_length=55, db_index=True, default=None, null=True)
    sname = models.CharField(max_length=55, db_index=True, default=None, null=True)
    doj = models.DateField(db_index=True, default=None, null=True)
    doc = models.DateField(db_index=True, default=None, null=True)
    dor = models.DateField(db_index=True, default=None, null=True)
    dorreason = models.CharField(max_length=55, db_index=True, default=None, null=True)
    dorremark = models.CharField(max_length=55, db_index=True, default=None, null=True)
    dol = models.DateField(db_index=True, default=None, null=True)
    dolreason = models.CharField(max_length=55, db_index=True, default=None, null=True)
    paymenttype = models.CharField(max_length=10, db_index=True, default=None, null=True)
    accountno = models.CharField(max_length=25, db_index=True, default=None)
    bank_id = models.DecimalField(max_digits=7, decimal_places=0, db_index=True, default=None, null=True)
    ifsccode = models.CharField(max_length=25, db_index=True, default=None, null=True)
    branch = models.CharField(max_length=25, db_index=True, default=None, null=True)
    pf = models.CharField(max_length=1, db_index=True, default=None, null=True)
    pflimits = models.CharField(max_length=1, db_index=True, default=None, null=True)
    fpf = models.CharField(max_length=1, db_index=True, default=None, null=True)
    vpf = models.CharField(max_length=1, db_index=True, default=None, null=True)
    pfcode = models.CharField(max_length=35, db_index=True, default=None, null=True)
    pfuanno = models.CharField(max_length=35, db_index=True, default=None, null=True)
    doepf = models.DateField(db_index=True, default=None, null=True)
    pfabry = models.CharField(max_length=1, db_index=True, default=None, null=True)
    esi = models.CharField(max_length=1, db_index=True, default=None, null=True)
    esicode = models.CharField(max_length=55, db_index=True, default=None, null=True)
    dispensary = models.CharField(max_length=55, db_index=True, default=None, null=True)
    lwf = models.CharField(max_length=1, db_index=True, default=None, null=True)
    lwfno = models.CharField(max_length=25, db_index=True, default=None, null=True)
    emptype = models.CharField(max_length=1, db_index=True, default=None, null=True)
    wagescalc = models.CharField(max_length=1, db_index=True, default=None, null=True)
    
    earn1 = models.DecimalField(max_digits=12, decimal_places=2, default=None, null=True)
    earn2 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn3 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn4 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn5 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn6 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn7 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn8 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn9 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    earn10 = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    gross = models.DecimalField(max_digits=12, decimal_places=2, default=None, null=True)
    foodrate = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    otsrate = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    nightrate = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    shrate = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, default=None, null=True)
    busroute = models.CharField(max_length=20, db_index=True, default=None, null=True)
    dob = models.DateField(db_index=True, default=None, null=True)
    gender = models.CharField(max_length=20, default=None, null=True)
    bloodgroup = models.CharField(max_length=5, default=None, null=True)
    mstatus = models.CharField(max_length=1, default=None, null=True)
    region = models.CharField(max_length=20, default=None, null=True)
    mobileno = models.CharField(max_length=20, default=None, null=True)
    aadhaarno = models.CharField(max_length=20, default=None, null=True)
    email = models.EmailField(max_length=255, default=None, null=True)
    shifttype = models.CharField(max_length=10, default=None, null=True)
    shiftoption = models.CharField(max_length=10, default=None, null=True)
    dutyhrs = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, default=None, null=True)
    
    ot = models.CharField(max_length=1,  default=None, null=True)
    
    otbs = models.CharField(max_length=1,  default=None, null=True)
    
    otas = models.CharField(max_length=1,  default=None, null=True)
    
    otr = models.CharField(max_length=1,  default=None, null=True)
    
    offday1 = models.CharField(max_length=3,  default=None, null=True)
    
    offday2 = models.CharField(max_length=3, db_index=True, default=None, null=True)
    
    offday3 = models.CharField(max_length=3,  default=None, null=True)
    
    offday1c = models.CharField(max_length=3,  default=None, null=True)
    
    cl = models.DecimalField(max_digits=7, decimal_places=2,  default=None, null=True)
    sl = models.DecimalField(max_digits=7, decimal_places=2,  default=None, null=True)
    el = models.DecimalField(max_digits=7, decimal_places=2,  default=None, null=True)
    
    introducer = models.CharField(max_length=55,  default=None, null=True)
    
    hodlogin_id = models.DecimalField(max_digits=7, decimal_places=2,  default=None, null=True)
    
    loginid = models.CharField(max_length=10,  default=None, null=True)
    
    logintype = models.CharField(max_length=20,  default=None, null=True)
    
    place = models.CharField(max_length=40,  default=None, null=True)
    
    entrydate = models.DateField( default=None, null=True)
    
    createdby = models.CharField(max_length=40,  default=None, null=True)
    
    createddate = models.DateField(db_index=True, default=None, null=True)
    
    changedby = models.CharField(max_length=40,  default=None, null=True)
    
    changeddate = models.DateField( default=None, null=True)
    
    education = models.CharField(max_length=55,  default=None, null=True)
    
    experience = models.CharField(max_length=55,  default=None, null=True)
    
    interviewdate = models.DateField( default=None, null=True)
    
    int_by = models.CharField(max_length=55,  default=None, null=True)
    
    app_by = models.CharField(max_length=55,  default=None, null=True)
    
    dojshow = models.CharField(max_length=10,  default=None, null=True)
    
    verify = models.CharField(max_length=10,  default=None, null=True)
    
    verifyby = models.CharField(max_length=55,  default=None, null=True)
    
    verifydate = models.DateField(max_length=55,  default=None, null=True)
    
    app_date = models.DateField(max_length=55,  default=None, null=True)
    
    verifysalary = models.DecimalField(max_digits=12, decimal_places=2,  default=None, null=True)
    
    salary = models.DecimalField(max_digits=12, decimal_places=2,  default=None, null=True)
    
    ctcsalary = models.DecimalField(max_digits=12, decimal_places=2,  default=None, null=True)
    
    emprpf = models.DecimalField(max_digits=10, decimal_places=2,  default=None, null=True)
    
    emprlwf = models.DecimalField(max_digits=10, decimal_places=2,  default=None, null=True)
    
    otsh = models.CharField(max_length=10,  default=None, null=True)
    
    loginpw = models.CharField(max_length=25,  default=None, null=True)
    
    lastpdate = models.DateField( default=None, null=True)
    
    active = models.BooleanField( default=None, null=True)
    
    oldcodeno = models.CharField(max_length=12,  default=None, null=True)






class HrAttendata(models.Model):
    empid = models.ForeignKey(hr_emps, on_delete=models.CASCADE)
    attndate = models.DateField()
    paycode = models.CharField(max_length=10, null=True, default=None)
    intime = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    outtime = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    breakout = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    breakin = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    hour = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    ot = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    otrate = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    otamt = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None)
    earlyarrival = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    latearrival = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    earlydeparture = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    latedeparture = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    status = models.CharField(max_length=10, null=True, default=None)
    remark = models.CharField(max_length=40, null=True, default=None)
    updationdate = models.DateField(null=True, default=None)
    latefrequency = models.DecimalField(max_digits=2, decimal_places=0, null=True, default=None)
    shift = models.CharField(max_length=3, null=True, default=None)
    shiftstart = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    shiftend = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    workhours = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    workextra = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    workless = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    present = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    absent = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    tour = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    leaves = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    off = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    holiday = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    otregister = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    otrateregister = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    otamtregister = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None)
    protect = models.CharField(max_length=1, null=True, default=None)
    earlyfrequency = models.DecimalField(max_digits=2, decimal_places=0, null=True, default=None)
    breakhour = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    presentpaid = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    absentpaid = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    leavepaid = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    tourpaid = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    offpaid = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    holidaypaid = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    excesslunch = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    excesslunchdays = models.DecimalField(max_digits=2, decimal_places=0, null=True, default=None)
    in_otr = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    out_otr = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    hour_otr = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    rate_otr = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    payment_otr = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    overstay = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    losshours = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    userid = models.DecimalField(max_digits=3, decimal_places=0, null=True, default=None)
    m_ot = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    sex = models.CharField(max_length=1, null=True, default=None)
    p_ot = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    in2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    s_ot = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    out2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    ot3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    in3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    out3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    out4 = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None)
    ot4 = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None)
    in4 = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None)
    in5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    out5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    ot5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    hour5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    ot2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    foodamt = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    foodamtregister = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    department = models.CharField(max_length=40, null=True, default=None)
    dlycost = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    hour2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    shamt = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None)
    hour3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    hour4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    nightct = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    sunhdct = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    teact = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    min = models.CharField(max_length=1, null=True, default=None)
    mout = models.CharField(max_length=1, null=True, default=None)
    minapp = models.DecimalField(max_digits=1, decimal_places=0, null=True, default=None)
    moutapp = models.DecimalField(max_digits=1, decimal_places=0, null=True, default=None)
    presentpaidc = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    offpaidc = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    holidaypaidc = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    leavepaidc = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    tourpaidc = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    absentc = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    statusc = models.CharField(max_length=10, null=True, default=None)
    shiftc = models.CharField(max_length=3, null=True, default=None)

    class Meta:
        unique_together = ('empid', 'attndate')



class HrUserlogs(models.Model):
    usertidno = models.DecimalField(max_digits=12, decimal_places=0)
    username = models.CharField(max_length=20, null=True, default=None)
    ipaddress = models.CharField(max_length=20, null=True, default=None)
    computername = models.CharField(max_length=20, null=True, default=None)
    loginstartdt = models.DateTimeField(null=True, default=None)
    loginenddt = models.DateTimeField(null=True, default=None)
    upprocess = models.CharField(max_length=1, null=True, default=None)
    upprocessstart = models.DateTimeField(null=True, default=None)
    upprocessend = models.DateTimeField(null=True, default=None)
    manualentry = models.DecimalField(max_digits=5, decimal_places=0, null=True, default=None)
    masterchange = models.DecimalField(max_digits=5, decimal_places=0, null=True, default=None)
    modifyentry = models.DecimalField(max_digits=5, decimal_places=0, null=True, default=None)

    class Meta:
        unique_together = ('usertidno',)

class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=193)
    pbc_tid = models.IntegerField(null=True, default=None)
    pbc_ownr = models.CharField(max_length=193)
    pbc_cnam = models.CharField(max_length=193)
    pbc_cid = models.SmallIntegerField(null=True, default=None)
    pbc_labl = models.CharField(max_length=254, null=True, default=None)
    pbc_lpos = models.SmallIntegerField(null=True, default=None)
    pbc_hdr = models.CharField(max_length=254, null=True, default=None)
    pbc_hpos = models.SmallIntegerField(null=True, default=None)
    pbc_jtfy = models.SmallIntegerField(null=True, default=None)
    pbc_mask = models.CharField(max_length=31, null=True, default=None)
    pbc_case = models.SmallIntegerField(null=True, default=None)
    pbc_hght = models.SmallIntegerField(null=True, default=None)
    pbc_wdth = models.SmallIntegerField(null=True, default=None)
    pbc_ptrn = models.CharField(max_length=31, null=True, default=None)
    pbc_bmap = models.CharField(max_length=1, null=True, default=None)
    pbc_init = models.CharField(max_length=254, null=True, default=None)
    pbc_cmnt = models.CharField(max_length=254, null=True, default=None)
    pbc_edit = models.CharField(max_length=31, null=True, default=None)
    pbc_tag = models.CharField(max_length=254, null=True, default=None)

    class Meta:
        unique_together = ('pbc_tnam', 'pbc_ownr', 'pbc_cnam')
        
class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=30)
    pbe_edit = models.CharField(max_length=254, null=True, default=None)
    pbe_type = models.SmallIntegerField(null=True, default=None)
    pbe_cntr = models.IntegerField(null=True, default=None)
    pbe_seqn = models.SmallIntegerField()
    pbe_flag = models.IntegerField(null=True, default=None)
    pbe_work = models.CharField(max_length=32, null=True, default=None)

    class Meta:
        unique_together = ('pbe_name', 'pbe_seqn')
        

class Pbcatfmt(models.Model):
    pbf_name = models.CharField(max_length=30)
    pbf_frmt = models.CharField(max_length=254, null=True, default=None)
    pbf_type = models.SmallIntegerField(null=True, default=None)
    pbf_cntr = models.IntegerField(null=True, default=None)

    class Meta:
        unique_together = ('pbf_name',)

class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=193)
    pbt_tid = models.IntegerField(null=True, default=None)
    pbt_ownr = models.CharField(max_length=193)
    pbd_fhgt = models.SmallIntegerField(null=True, default=None)
    pbd_fwgt = models.SmallIntegerField(null=True, default=None)
    pbd_fitl = models.CharField(max_length=1, null=True, default=None)
    pbd_funl = models.CharField(max_length=1, null=True, default=None)
    pbd_fchr = models.SmallIntegerField(null=True, default=None)
    pbd_fptc = models.SmallIntegerField(null=True, default=None)
    pbd_ffce = models.CharField(max_length=18, null=True, default=None)
    pbh_fhgt = models.SmallIntegerField(null=True, default=None)
    pbh_fwgt = models.SmallIntegerField(null=True, default=None)
    pbh_fitl = models.CharField(max_length=10, null=True, default=None)
    pbh_funl = models.CharField(max_length=10, null=True, default=None)
    pbh_fchr = models.SmallIntegerField(null=True, default=None)
    pbh_fptc = models.SmallIntegerField(null=True, default=None)
    pbh_ffce = models.CharField(max_length=18, null=True, default=None)
    pbl_fhgt = models.SmallIntegerField(null=True, default=None)
    pbl_fwgt = models.SmallIntegerField(null=True, default=None)
    pbl_fitl = models.CharField(max_length=10, null=True, default=None)
    pbl_funl = models.CharField(max_length=10, null=True, default=None)
    pbl_fchr = models.SmallIntegerField(null=True, default=None)
    pbl_fptc = models.SmallIntegerField(null=True, default=None)
    pbl_ffce = models.CharField(max_length=18, null=True, default=None)
    pbt_cmnt = models.CharField(max_length=254, null=True, default=None)

    class Meta:
        unique_together = ('pbt_tnam', 'pbt_ownr')

class Pbcatvld(models.Model):
    pbv_name = models.CharField(max_length=30)
    pbv_vald = models.CharField(max_length=254, null=True, default=None)
    pbv_type = models.SmallIntegerField(null=True, default=None)
    pbv_cntr = models.IntegerField(null=True, default=None)
    pbv_msg = models.CharField(max_length=254, null=True, default=None)

    class Meta:
        unique_together = ('pbv_name',)
        

# class CustomUser(AbstractUser):
#     username = None
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     father_husband_name = models.CharField(max_length=50)
#     designation = models.CharField(max_length=50)
#     USERID = models.CharField(max_length=6, unique=True, default=None)
#     password = models.CharField(max_length=200, default=None)
#     USERNAME_FIELD = 'USERID'
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} is {self.designation} at Megasoft'



# UTILITIES
class announcments(models.Model):
    title = models.CharField(max_length=100, default=None)
    announcment_date = models.DateTimeField(auto_now_add=True)
    announcment_description = models.TextField(default=None)