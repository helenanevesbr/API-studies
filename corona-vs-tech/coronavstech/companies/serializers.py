from rest_framework import serializers

# Serializers in DRF (Django Rest Framework) allow complex data types, such as Django models, to be converted to Python data types that can then be easily rendered into JSON, XML, or other content types.
# Because JSON is a serialized format suitable for API responses. It will also handle the inverse operation, i.e., parsing incoming API request data and converting it to a format suitable for creating or updating a Company model instance.

from companies.models import Company

class CompanySerializer(serializers.ModelSerializer):
    # The ModelSerializer is a type of DRF serializer that automatically generates fields and validations based on the associated Django model.

    class Meta:
        model = Company
        #  the associated model for this serializer is the Company model

        fields = ["id", "name", "status", "application_link", "last_update", "notes"]
        # When an instance of the Company model is serialized using this serializer, only these fields will be included in the output.