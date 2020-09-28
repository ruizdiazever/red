from django.db.models import Model, CharField, TextField, DateTimeField, SmallIntegerField
from ckeditor.fields import RichTextField

class Page(Model):
    title = CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name='Contenido')
    ordering = SmallIntegerField(verbose_name='Orden', default=0)
    created = DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ['ordering','title']

    def __str__(self):
        return self.title
