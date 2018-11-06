from django.db import models

# Create your models here.



class Author(models.Model):
    id = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=32)
    aplace = models.CharField(max_length=32)




class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=32)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    #与Publish建立一对多的关系（一个出版社可以出版多种书籍）,生成一个输入字段   （不添加to_field 默认添加为主键 后面那个添加上，不然会报错）
    publish = models.ForeignKey(to='Publish',to_field='id',null=True,on_delete=models.CASCADE)
    author = models.ForeignKey(to='Author',to_field='id',null=True,on_delete=models.CASCADE)
    #  注意添加 null= Ture
    #  author = models.OneToOneField('Author')是一对一  （这样的话，作者只能使用一次，只能写1本书，不能给出多本书，唯一性 ）
    # 与Author表建立多对多的关系（作者可以是多个，出版社也可以是多个）,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    # publish=models.ForeignKey(to="Publish",to_field="pid",null=True,on_delete=models.CASCADE)
    # authors=models.ManyToManyField(to='Author',)

