from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

#
# from progEng.models import Citizen, Income
#
from progEng.models import Income, Citizen, Zarplata, Persona


class IncomeSerializer(serializers.ModelSerializer):
    # date = serializers.DateField()
    class Meta:
        model = Income
        fields = ('date', 'income')


class CitizenSerializer(serializers.ModelSerializer):
    incomes = IncomeSerializer(many=True)

    class Meta:
        model = Citizen
        fields = ('fullname', 'city', 'profession', 'age', 'incomes')

    def create(self, validated_data):
        tasks = validated_data.pop('incomes')
        instance = Citizen.objects.create(**validated_data)
        for task_data in tasks:
            Income.objects.create(citizen_id=instance, **task_data)
        return instance

    def update(self, instance, validated_data):
        tasks = validated_data.pop('incomes')
        citizen = instance.incomes.all()
        citizen = list(citizen)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.city = validated_data.get('city', instance.city)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.age = validated_data.get('age', instance.age)
        instance.save()

        for task in tasks:
            inco = citizen.pop(0)
            inco.date = task.get('date', inco.date)
            inco.income = task.get('income', inco.income)
            inco.save()
        return instance


class ZarplataSerializer(serializers.ModelSerializer):
    # date = serializers.DateField()
    class Meta:
        model = Zarplata
        fields = ('data', 'income')

# разряды в боксе новичек, 3 разряд, 2 разряд, 3 разряд, КМС
class PersonaSerializer(serializers.ModelSerializer):
    zarplats = ZarplataSerializer(many=True)

    class Meta:
        model = Persona
        fields = ('fullname', 'city', 'club', 'age', 'vid_s', 'zarplats')

    def create(self, validated_data):
        tasks = validated_data.pop('zarplats')
        instance = Persona.objects.create(**validated_data)
        for task_data in tasks:
            Zarplata.objects.create(citizen_id=instance, **task_data)
        return instance

    def update(self, instance, validated_data):
        tasks = validated_data.pop('zarplats')
        citizen = instance.zarplats.all()
        citizen = list(citizen)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.city = validated_data.get('city', instance.city)
        instance.profession = validated_data.get('club', instance.profession)
        instance.age = validated_data.get('age', instance.age)
        instance.vid_s = validated_data.get('vid_s', instance.vid_s)
        instance.save()

        for task in tasks:
            inco = citizen.pop(0)
            inco.data = task.get('data', inco.data)
            inco.income = task.get('income', inco.income)
            inco.save()
        return instance
