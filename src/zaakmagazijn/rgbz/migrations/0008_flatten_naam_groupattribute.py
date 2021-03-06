# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-25 09:14
from __future__ import unicode_literals

from django.db import migrations


def flatten_naam_naamaanschrijving(apps, schema_editor):
    NatuurlijkPersoon = apps.get_model('rgbz.NatuurlijkPersoon')

    for nps in NatuurlijkPersoon.objects.all():
        nps.naam_voornamen = nps.naam.voornamen
        nps.naam_geslachtsnaam = nps.naam.geslachtsnaam
        nps.naam_adelijke_titel = nps.naam.adelijke_titel

        if nps.naam.voorvoegsel_geslachtsnaam:
            nps.voorvoegsel_geslachtsnaam_voorvoegselnummer = nps.naam.voorvoegsel_geslachtsnaam.voorvoegselnummer
            nps.voorvoegsel_geslachtsnaam_lo3_voorvoegsel = nps.naam.voorvoegsel_geslachtsnaam.lo3_voorvoegsel
            nps.voorvoegsel_geslachtsnaam_voorvoegsel = nps.naam.voorvoegsel_geslachtsnaam.voorvoegsel
            nps.voorvoegsel_geslachtsnaam_scheidingsteken = nps.naam.voorvoegsel_geslachtsnaam.scheidingsteken

        nps.naam_aanschrijving_voorletters_aanschrijving = nps.naam_aanschrijving.voorletters_aanschrijving
        nps.naam_aanschrijving_voornamen_aanschrijving = nps.naam_aanschrijving.voornamen_aanschrijving
        nps.naam_aanschrijving_geslachtsnaam_aanschrijving = nps.naam_aanschrijving.geslachtsnaam_aanschrijving
        nps.naam_aanschrijving_aanhef_aanschrijving = nps.naam_aanschrijving.aanhef_aanschrijving
        nps.save()


class Migration(migrations.Migration):

    dependencies = [
        ('rgbz', '0007_auto_20171123_1209'),
    ]

    operations = [
        migrations.RunPython(flatten_naam_naamaanschrijving)
    ]
