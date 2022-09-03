from rest_framework import serializers
from product import models

class dataserializer(serializers.ModelSerializer):
    eb = serializers.SerializerMethodField()
    
    def get_eb(self,obj):
        if obj.id < 2:
            eb="Early Bird"
        else:
            eb="Late Comer"
        return eb
    
    class Meta:
        model = models.products
        fields = ['id','nm','desc','eb']
