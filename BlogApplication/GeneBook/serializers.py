from rest_framework import serializers
from datetime import datetime
from .models import GeneBank

class GeneBank:
    """This is a blueprint for creating GeneBank instances/objects"""
    def __init__(self, sample_id, barcode_sequence, primer_sequence, gene, region, site, description, created=None):
        self.sample_id = sample_id
        self.barcode_sequence = barcode_sequence
        self.primer_sequence = primer_sequence
        self.gene = gene
        self.region = region
        self.site = site
        self.description = description
        self.created = created or datetime.now()

gene = GeneBank(sample_id="", barcode_sequence="", primer_sequence="", gene="", region="", site="", description="")

"""This is an instance."""
class GeneBankSerializer(serializers.Serializer):
    
    """This is a custom serializer. It serializes a genebank object on line 11"""
    sample_id = serializers.CharField()
    barcode_sequence = serializers.CharField(max_length=50)
    primer_sequence = serializers.CharField()
    gene = serializers.CharField()
    region = serializers.CharField()
    site = serializers.CharField()
    description = serializers.CharField()
    created = serializers.DateTimeField()

    def create(self, validated_data):
        """This logic is commonly applied at workplaces"""
        return GeneBank(**validated_data)
    
    def update(self, instance, validated_data):
        instance.sample_id = validated_data.get("sample_id")
        instance.barcode_sequence = validated_data.get("barcode_sequence")
        instance.primer_sequence = validated_data.get("primer_sequence")
        instance.gene = validated_data.get("gene")
        instance.region = validated_data.get("region")
        instance.site = validated_data.get("site")
        instance.description = validated_data.get("description")
        instance.created = validated_data.get("created")

        return instance