from rest_framework import serializers
from . import models
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['id','user','address','email','cin','RIB']
    
    def __init__(self, *agr, **kwargs):
        super(VendorSerializer, self).__init__(*agr, **kwargs)
        #self.Meta.depth = 1  
        
class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['id','user','address','email','cin','RIB']
        
    def __init__(self, *agr, **kwargs):
        super(VendorDetailSerializer, self).__init__(*agr, **kwargs)
        #self.Meta.depth = 1 
        
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Product
        fields=['id','category','vendor','title','detail','price']
        
    def __init__(self, *agr, **kwargs):
        super(ProductListSerializer, self).__init__(*agr, **kwargs)
        #self.Meta.depth = 1   
        
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Product
        fields=['id','category','vendor','title','detail','price']
        
    def __init__(self, *agr, **kwargs):
        super(ProductDetailSerializer, self).__init__(*agr, **kwargs)
        #self.Meta.depth = 1   

        class VendorSerializer(serializers.ModelSerializer):                                                                
            class Meta:
                model= models.Vendor
                fields=['id','user','address','email','cin','RIB']
    
    def __init__(self, *agr, **kwargs):
        super(VendorSerializer, self).__init__(*agr, **kwargs)
       # self.Meta.depth = 1  

  # Customer 
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Customer 
        fields=['id','user','mobile']
    
    def __init__(self, *agr, **kwargs):
        super(CustomerSerializer, self).__init__(*agr, **kwargs)
        self.Meta.depth = 1  
     
class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Customer
        fields=['id','user','mobile']
        
    def __init__(self, *agr, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*agr, **kwargs)
        self.Meta.depth = 1 