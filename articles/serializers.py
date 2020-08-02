from rest_framework.serializers import ModelSerializer
from .models import Donation


class DonationSerializers(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Donation
