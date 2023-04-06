from django.db import migrations


def populate_db(apps, schema_editor):
    Calc = apps.get_model('calculator', 'Operator')

    addition = Calc(symbol="+", name="addition")
    addition.save()

    subtraction = Calc(symbol="-", name="subtraction")
    subtraction.save()

    multiplication = Calc(symbol="*", name="multiplication")
    multiplication.save()

    division = Calc(symbol="/", name="division")
    division.save()

    remainder = Calc(symbol="%", name="remainder")
    remainder.save()

    exponentiation = Calc(symbol="**", name="exponentiation")
    exponentiation.save()


class Migration(migrations.Migration):
    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
