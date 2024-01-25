

## APIView、GenericAPIView、基于Mixin混合类、ViewSet、ModelViewSet 的演变过程

```django
# -------------基于APIView------------------------
# 对于获取全部数据和获取单独一个数据的功能，需要用两个类来实现

class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        # 构建序列化器
        serializer = BookSerializers(instance=book_list, many=True)
        return Response(serializer.data)


def post(self, request):
    serializer = BookSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors)


class BookViewDetail(APIView):

    def get(self, request, id):
        print(id)
        book = Book.objects.get(id=id)
        serializer = BookSerializers(instance=book, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        update_book = Book.objects.get(pk=id)

        serializer = BookSerializers(instance=update_book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)
        return Response()



# -------------基于GenericAPIView------------------------------------------------
# 对于获取全部数据和获取单独一个数据的功能，同样需要用两个类来实现

class BookView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)



class BookViewDetail(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request, pk):
        print(id)
        serializer = BookSerializers(instance=self.get_object(), many=False)
        return Response(serializer.data)

    def put(self, request, pk):

        serializer = BookSerializers(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)



# -------------基于Mixin混合类--------------
# 对于获取全部数据和获取单独一个数据的功能，只需写一个类，但是要基于几个类

class BookView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)



class BookViewDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)



# -------------再封装（类的合并）-------------------

class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


-------------ViewSet------------------------------------------------

class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers



# -------------ModelViewSet------------------------------------------------


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

```