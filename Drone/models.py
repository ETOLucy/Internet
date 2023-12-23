from django.db import models

# Create your models here.
class Drone(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    explain = models.CharField(max_length=255)
    ps = models.CharField(max_length=10)
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
        # 价格字段，最多10位数字，其中小数部分2位
    price_before = models.DecimalField(max_digits=10, decimal_places=2)
    price_current = models.DecimalField(max_digits=10, decimal_places=2)
    introduction = models.CharField(max_length=255,default='参数111')
    use_case = models.CharField(max_length=255,default='适用场景111')
    select_1 = models.CharField(max_length=100,default='属性')
    select_2 = models.CharField(max_length=100,default='属性')
    select_3 = models.CharField(max_length=100,default='属性')
    op11 = models.CharField(max_length=100,default='其他')
    op12 = models.CharField(max_length=100,default='其他')
    op13 = models.CharField(max_length=100,default='其他')
    op14 = models.CharField(max_length=100,default='其他')
    op21 = models.CharField(max_length=100,default='其他')
    op22 = models.CharField(max_length=100,default='其他')
    op23 = models.CharField(max_length=100,default='其他')
    op24 = models.CharField(max_length=100,default='其他')
    op31 = models.CharField(max_length=100,default='其他')
    op32 = models.CharField(max_length=100,default='其他')
    op33 = models.CharField(max_length=100,default='其他')
    op34 = models.CharField(max_length=100,default='其他')

    # images
    img = models.ImageField(upload_to='img',default='/statics/images/bg.jpg')



class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

