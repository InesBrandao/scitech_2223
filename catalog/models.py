from django.db import models

# Create your models here.
class Books(models.Model):
    title= models.CharField('Título do livro',max_length=200)
    
    author=models.ForeignKey('Author', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Author(models.Model):
    name=models.CharField('Nome do autor',max_length=200)

    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    genretype=models.CharField('Género do livro', max_length=101)
    
    book = models.ForeignKey('Books',on_delete=models.PROTECT)

    def __str__(self):
        return self.genretype
    
class Editor(models.Model):
    editorname=models.CharField('Nome de Editora', max_length=101)
    edited=models.ForeignKey('Books', on_delete=models.PROTECT)
    def __str__(self):
        return self.editorname