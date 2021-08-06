from django.db import models

# Create your models here.
class Info(models.Model):
    ten = models.CharField(verbose_name='Tên sản phẩm',max_length=265)
    gia_goc = models.FloatField(verbose_name='Giá gốc',default=0)
    gia_sale = models.FloatField(verbose_name='Giá sale', default=0)
    sale_rate= models.CharField(verbose_name='Phần trăm sale',max_length=10)
    con_hang = models.CharField(verbose_name='Còn hàng',max_length=100, null=True)
    luot_danh_gia = models.IntegerField(verbose_name='Số đánh giá', default=0)
    sao = models.IntegerField(verbose_name='Số sao', default=0)
    link_sp = models.URLField(verbose_name='Link sản phẩm', max_length=265, null=True)
    anh_sp = models.ImageField(verbose_name='Ảnh sản phẩm', upload_to = 'media_anh', blank=True)

    def __str__(self):
        return self.ten
