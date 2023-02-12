from variables.models import Variable
from ..models import Measurement


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(measure_pk):
    measurement = Measurement.objects.get(pk=measure_pk)
    return measurement


def create_measurement(measure):
    variables_pk = Variable.objects.get(pk=measure["variable"])
    measurement = Measurement(
        variable=variables_pk, value=measure["value"], unit=measure["unit"], place=measure["place"])
    measurement.save()
    return measurement


def update_measurement(measure_pk, new_measure):
    measurement = get_measurement(measure_pk)
    measurement.value = new_measure["value"]
    measurement.unit = new_measure["unit"]
    measurement.place = new_measure["place"]
    measurement.save()
    return measurement


def delete_measurement(measure_pk):
    measurement = Measurement.objects.get(pk=measure_pk)
    measurement.delete()
    return measurement


def delete_measurements():
    measurements = Measurement.objects.all()
    for measurement in measurements:
        measurement.delete()
