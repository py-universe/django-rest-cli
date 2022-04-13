"""
templates for serializers
"""

SERIALIZER = """

class %(model)sSerializer(serializers.ModelSerializer):

    class Meta:
        model = %(model)s
        fields = '__all__'
"""

IMPORTS = """from rest_framework import serializers

from %(app)s.models import %(model)s
"""
