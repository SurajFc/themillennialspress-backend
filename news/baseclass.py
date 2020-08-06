from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AbstractBaseClassApiView(APIView):
    @property
    def serializer_class(self):
        # Our serializer depending on type
        raise NotImplementedError

    @property
    def model(self):
        # Our model depending on type
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        try:
            x = self.model.objects.all()
            ser = self.serializer_class(x, many=True)
            return Response(ser.data)
        except self.model.DoesNotExist:
            pass

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
