from django.db import models

# Create your models here.

class Meeting(models.Model):
    id = models.BigIntegerField(max_length=20,primary_key=True)
    name = models.CharField(max_length=60,null=True)
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    address = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=1000,null=True)
    status = models.IntegerField(max_length=1, null=True)
    crUserid = models.BigIntegerField(max_length=20,null=True)
    crTime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'tb_meeting'  # 指明数据库表名


    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name

