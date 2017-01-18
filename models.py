from django.db import models

##Models

class StudentContactDetails(models.Model):
    stu_rollno =  models.CharField(max_length=12) 
    stu_firstname =  models.CharField(max_length=30) 
    stu_mobilephone =  models.IntegerField() 
    stu_emailid =  models.CharField(max_length=40)

class StudentPersonal(models.Model):  
    MARITAL_STATUS= (  
            ('Single', 'Single'),  
            ('Married', 'Married'), 
    ) 
    stu_rollno =  models.ForeignKey(StudentContactDetails)  
    stu_fathername =  models.CharField(max_length=30)
    stu_mothername =  models.CharField(max_length=30)  
    stu_dob =  models.DateField()
    stu_maritalstatus =  models.CharField(max_length=7, choices=MARITAL_STATUS)  
    
class StudentSkills(models.Model):  
    stu_rollno =  models.ForeignKey(StudentContactDetails)   
    skill =  models.CharField(max_length=30)  
class StudentEduQualification(models.Model):  
    stu_rollno =  models.ForeignKey(StudentContactDetails)  
    course =  models.CharField(max_length=15) 
    marksObtained =   models.IntegerField()  

class StudentProjects(models.Model):  
    stu_rollno =  models.ForeignKey(StudentContactDetails)  
    projectName =  models.CharField(max_length=50)  
    
class StudentCertifications(models.Model):  
    CERTIFICATE_TYPE = (  
            ('Participated', 'Participated'),
            ('Attended', 'Attended'),  
            ('Volunteered', 'Volunteered'),  
            ('Won', 'Won'),  
            ('Conducted', 'Conducted'),  
            ('Co-ordinated', 'Co-ordinated'), 
    )
    stu_rollno =  models.ForeignKey(StudentContactDetails)  
    certificateType =  models.CharField(max_length=13, choices=CERTIFICATE_TYPE)

class StudentAwards(models.Model):
    stu_rollno =  models.ForeignKey(StudentContactDetails)  
    topic =  models.CharField(max_length=50)  
    
class StudentActivities(models.Model):  
    stu_rollno =  models.ForeignKey(StudentContactDetails)  
    activity =  models.CharField(max_length=30)  
