from django.db import models

# Create your models here.
class Info(models.Model):
    ten = models.CharField(verbose_name='Tên sản phẩm',max_length=265)
    gia_goc = models.CharField(verbose_name='Giá gốc',max_length=50)
    gia_sale = models.CharField(verbose_name='Giá sale',max_length=50)
    sale_rate= models.CharField(verbose_name='Phần trăm sale',max_length=10)
    con_hang = models.CharField(verbose_name='Còn hàng',max_length=100, null=True)
    luot_danh_gia = models.CharField(verbose_name='Số đánh giá',max_length=100, default=0)
    sao = models.CharField(verbose_name='Số sao',max_length=100, default=0)
    link_sp = models.URLField(verbose_name='Link sản phẩm', max_length=100, null=True)

    def __str__(self):
        return self.ten
