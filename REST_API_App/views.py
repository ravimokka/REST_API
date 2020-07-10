from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *
from django.conf import settings

FILE_PATH = settings.MEDIA_URL


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


def querySet_to_list(qs):
    return [dict(q) for q in qs]


class FetchAPIData(APIView):
    def get(self, request, *args, **kwargs):
        global massage
        try:
            response_data = []
            shop_querySet = Shops.objects.filter(pk=request.query_params.get('shop_id', None))
            if shop_querySet:
                for i in shop_querySet:
                    category_querySet = i.children.all()
                    category_data = i.children.all().values()
                    if category_querySet:
                        for j in category_data:
                            cate_data = dict(j)
                            cate_list = {'id': cate_data['id'], 'category_name': cate_data['category_name']}
                            if cate_data['parent_cat'] != 'Null':
                                for x in category_querySet:
                                    product_querySet = x.children.all()
                                    product_data = x.children.filter(category_id_id=cate_data['id']).values()
                                    pro_data = querySet_to_list(product_data)
                                    if product_querySet:
                                        if len(pro_data) > 0:
                                            product_list = []
                                            for p in pro_data:
                                                pro_dict = {'id': p['id'], 'product_name': p['product_name'], 'product_image':[]}
                                                for y in product_querySet:
                                                    media_querySet = y.children.filter(product_id_id=p['id'])
                                                    if len(media_querySet) > 0:
                                                        print(media_querySet)
                                                        p_img = [md.product_image.url for md in media_querySet]
                                                        pro_dict['product_image'].append(p_img)
                                                    else:
                                                        pass
                                                product_list.append(pro_dict)
                                            cate_list['product'] = product_list
                                        else:
                                            pass
                                    else:
                                        pass
                                        # cate_list['product'] = []
                                response_data.append(cate_list)
                                massage = 'successfully fetched data'
                            else:
                                response_data.append(cate_list)
                    else:
                        response_data.append({'massage': 'no records available for ' + i.shop_name})
                        massage = "no data found"
            else:
                massage = "no data found"
            return Response(status=status.HTTP_200_OK, data={'status': 200, 'data': response_data, 'massage': massage})
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"data": False})
