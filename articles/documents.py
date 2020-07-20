
from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry

from .models import Articles,Category

@registry.register_document
class ArticleDocument(Document):
    category = fields.ObjectField(properties={
        'id': fields.TextField(),
        'name': fields.TextField(),
        'image': fields.FileField(),
    })
    cover = fields.FileField()
    tags = fields.ListField(fields.TextField())
    
    class Index:
        name= 'articles'
        settings = {'number_of_shards': 1,'number_of_replicas': 1}
    
    class Django:
        model = Articles 
        fields = [ 'updated_at','title','subtitle', 'author_name','user', 'realease','is_active','slug' ]
        # related_models = [Category] 

    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super(ArticleDocument, self).get_queryset().select_related(
            'category'
        )