from django.db import models
import markdown

# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()


CATEGORY = (('business', 'ビジネス'), ('life', 'ライフ'), ('other', 'その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices= CATEGORY
    )
    def __str__(self):
        return self.title
    def markdown_to_html(self):
        #マークダウンをHTMLに変換・出力
        md = markdown.Markdown(
            extensions=['extra', 'admonition', 'sane_lists', 'toc']
        )
        html = md.convert(self.content)
        return html
    def overview(self):
        overview = self.content
        return overview[:20]