from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class guild(models.Model):
    guild = models.CharField(primary_key=True,max_length=200,unique=True)
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class state(models.Model):
    state = models.CharField(primary_key=True,max_length=200,unique=True)
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=User)
def create(sender,instance,created,**kwargs):
    if created:
        Member.objects.create(account=instance)

class Member(models.Model):
    account=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    Nickname = models.CharField(max_length=200,default="預設",unique=True)
    Identity = models.ForeignKey(guild, on_delete = models.SET_NULL, null = True,unique=False)
    Characters_number = models.IntegerField(default=0)
    Timestamp = models.DateTimeField(auto_now_add=True,null=True)
    Update=models.DateTimeField(auto_now=True)
    def __self__(self):
        return self.Nickname


class Character(models.Model):
    Name = models.CharField(primary_key=True,max_length=200,unique=True)
    account = models.ForeignKey(Member, on_delete=models.CASCADE,unique=False)
    Timestamp = models.DateTimeField(auto_now_add=True,max_length=200)
    Update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Name)
@receiver(post_save, sender=Character)
def create(sender,instance,created,**kwargs):
    if created:
        Plate_shoes.objects.create(Name=instance)
        Plate_armor.objects.create(Name=instance)
        Plate_helmet.objects.create(Name=instance)
        Sword.objects.create(Name=instance)
        Axe.objects.create(Name=instance)
        Mace.objects.create(Name=instance)
        Gloves.objects.create(Name=instance)
        Crossbow.objects.create(Name=instance)
        Shield.objects.create(Name=instance)

class Order(models.Model):
    Id = models.AutoField(primary_key=True)
    publisher = models.ForeignKey(Member, on_delete=models.CASCADE)
    State = models.ForeignKey(state,on_delete = models.SET_NULL, null = True)
    Start_time = models.DateTimeField(auto_now_add=True,help_text='Start date',)
    End_time = models.DateTimeField('End time')
    Product_Name = models.CharField(max_length=200)
    Price = models.IntegerField()
    Count = models.IntegerField()
    PS = models.TextField(blank=True, null=True)
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Provider_details(models.Model):
    Provider = models.ForeignKey(Member, on_delete=models.CASCADE)
    Order_Id = models.ForeignKey(Order, on_delete=models.CASCADE)
    PS = models.TextField(blank=True, null=True)
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Plate_shoes(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="鐵甲鞋製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="士兵鞋製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="騎士鞋製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="守衛鞋製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="守墓人之靴製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="惡魔之靴製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="審判長靴制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="英勇之靴製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Plate_armor(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="盔甲製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="士兵盔甲製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="騎士盔甲製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="守衛盔甲製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="守墓人盔甲製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="惡魔盔甲製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="審判盔甲制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="英勇盔甲製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Plate_helmet(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="頭盔製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="士兵頭盔製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="騎士頭盔製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="守衛頭盔製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="守墓人頭盔製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="惡魔頭盔製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="審判頭盔制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="英勇頭盔製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Sword(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="劍製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="闊劍製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="闊刃大劍製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="雙劍製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="王者之劍製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="斷水劍製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="雙刀制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="傭王闊刃大劍製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Axe(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="斧製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="戰斧製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="巨斧大劍製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="戰戟製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="召喚神斧製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="赤炎鐮刀製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="熊爪神斧制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="裂域斧製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Mace(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="錘杖製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="錘杖製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="重型錘杖製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="晨星製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="基石錘杖製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="夢魘錘杖製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="卡姆蘭錘杖制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="守誓雙錘製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Gloves(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="戰鬥手套製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="格鬥手套製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="戰鬥護碗製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="尖刺護手製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="烏鴉之爪製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="煉獄火之手製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="熊爪士之擊制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="阿瓦隆之拳製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Crossbow(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="十字弓製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="十字弓製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="重型十字弓製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="輕便十字弓製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="愁淵連弩製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="霹靂連弩製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact3 = models.IntegerField(help_text="圍城弩制造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact4 = models.IntegerField(help_text="朔能炮製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)

class Shield(models.Model):
    Name = models.OneToOneField(Character,primary_key=True, on_delete=models.CASCADE)
    Inner = models.IntegerField(help_text="盾牌製造內圈",null=False,default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal1 = models.IntegerField(help_text="盾牌製造外圈",null=False,default=0 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal2 = models.IntegerField(help_text="石棺之膚製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    normal3 = models.IntegerField(help_text="怯懦之盾製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact1 = models.IntegerField(help_text="破面之盾製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    artifact2 = models.IntegerField(help_text="星域神盾製造外圈",null=False,default=0 , validators=[MinValueValidator(0), MaxValueValidator(100)])
    Timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Update = models.DateTimeField(auto_now=True)