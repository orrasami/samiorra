from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Galeria(Base):
    galeria = models.CharField('Galeria', max_length=30)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'

    def __str__(self):
        return self.galeria

    class Meta:
        db_table = 'galerias'


class Foto(Base):
    nome = models.CharField('Nome', max_length=30)
    ordem = models.PositiveIntegerField(unique=False)
    galeria = models.ForeignKey(Galeria, verbose_name='Galeria', on_delete=models.CASCADE)
    imagem = StdImageField(upload_to='fotos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'fotos'


def fotos_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(fotos_pre_save, sender=Foto)
