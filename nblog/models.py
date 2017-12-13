from django.db import models

# Create your models here.
from new_blog import settings

STATUS = {
        0: u'正常',
        1: u'草稿',
        2: u'删除',
}
NEWS = {
        0: u'oschina',
        1: u'chiphell',
        2: u'freebuf',
        3: u'cnBeta',
}

class Nav(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'nav')
    url = models.CharField(max_length=200, blank=True, null=True,
                           verbose_name=u'url')

    status = models.IntegerField(default=0, choices=STATUS.items(),
                                 verbose_name=u'status')
    create_time = models.DateTimeField(u'created', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u"nav"
        ordering = ['-create_time']
       # app_label = string_with_title('blog', u"博客管理")

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'name')
   # parent = models.ForeignKey('self', default=None, blank=True, null=True,
                           #    verbose_name=u'parent')
    rank = models.IntegerField(default=0, verbose_name=u'rank')
    status = models.IntegerField(default=0, choices=STATUS.items(),
                                 verbose_name=u'status')

    create_time = models.DateTimeField(u'created', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'category'
        ordering = ['rank', '-create_time']
       # app_label = string_with_title('blog', u"博客管理")

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('category-detail-view', args=(self.name,))

    def __unicode__(self):
        if self.parent:
            return '%s-->%s' % (self.parent, self.name)
        else:
            return '%s' % (self.name)

    __str__ = __unicode__

class Post(models.Model):
   # author = models.ForeignKey(settings.AUTH_USER_MODEL)
   # category = models.ForeignKey(Category,  verbose_name=u'category')
    title = models.CharField(max_length=100)
    en_title = models.CharField(max_length=100)
    img = models.CharField(max_length=200,
                           default='/static/img/article/default.jpg')
    tags = models.CharField(max_length=200, null=True, blank=True,
                            verbose_name=u'tags', help_text=u'help text')
    summary = models.TextField(verbose_name=u'summary')
    content = models.TextField(verbose_name=u'content')
    view_times = models.IntegerField(default=0)
    zan_times = models.IntegerField(default=0)

    is_top = models.BooleanField(default=False, verbose_name=u'top')
    rank = models.IntegerField(default=0, verbose_name=u'rank')
    status = models.IntegerField(default=0, choices=STATUS.items(),
                                 verbose_name='status')
    pub_time = models.DateTimeField(default=False, verbose_name=u'published')
    create_time = models.DateTimeField(u'created', auto_now_add=True)
    update_time = models.DateTimeField(u'updated', auto_now=True)

    def get_tags(self):
        tags_list = self.tags.split(',')
        while '' in tags_list:
            tags_list.remove('')

        return tags_list

    class Meta:
        verbose_name_plural = verbose_name = u'post'
        ordering = ['rank', '-is_top', '-pub_time', '-create_time']
       # app_label = string_with_title('blog', u"博客管理")

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('article-detail-view', args=(self.en_title,))

    def __unicode__(self):
            return self.title

    __str__ = __unicode__

class Column(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'name')
    summary = models.TextField(verbose_name=u'summary')
    post = models.ManyToManyField(Post, verbose_name=u'post')
    status = models.IntegerField(default=0, choices=STATUS.items(),
                                 verbose_name='status')
    create_time = models.DateTimeField(u'created',
                                       auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'专栏'
        ordering = ['-create_time']
     #   app_label = string_with_title('blog', u"博客管理")

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('column-detail-view', args=(self.name,))

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

class Carousel(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'title')
    summary = models.TextField(blank=True, null=True, verbose_name=u'summary')
    img = models.CharField(max_length=200, verbose_name=u'image',
                           default='/static/img/carousel/default.jpg')
    #post = models.ForeignKey(Post, verbose_name=u'post')
    create_time = models.DateTimeField(u'created', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'carousel'
        ordering = ['-create_time']
       # app_label = string_with_title('blog', u"博客管理")


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'news')
    summary = models.TextField(verbose_name=u'summary')
    news_from = models.IntegerField(default=0, choices=NEWS.items(),
                                    verbose_name='news_form')
    url = models.CharField(max_length=200, verbose_name=u'url')
    create_time = models.DateTimeField(u'created', auto_now_add=True)
    pub_time = models.DateTimeField(default=False, verbose_name=u'published')

    class Meta:
        verbose_name_plural = verbose_name = u'news'
        ordering = ['-title']
      #  app_label = string_with_title('blog', u"博客管理")

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('news-detail-view', args=(self.pk,))

    def __unicode__(self):
        return self.title

    __str__ = __unicode__
