# Generated by Django 5.1.3 on 2024-11-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myApp', '0002_delete_cakdobe'),
    ]

    operations = [
        migrations.CreateModel(
            name='CakDobe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vzs_sifra', models.CharField(max_length=100)),
                ('vzs_naziv', models.TextField()),
                ('tip_vzs', models.CharField(max_length=100)),
                ('povprecna_cd_zelo_h', models.FloatField(blank=True, null=True)),
                ('povprecna_cd_hitro', models.FloatField(blank=True, null=True)),
                ('povprecna_cd_redno', models.FloatField(blank=True, null=True)),
                ('st_izvajalcev_bolnisnica', models.FloatField(blank=True, null=True)),
                ('st_izvajalcev_zdravstveni_dom', models.FloatField(blank=True, null=True)),
                ('st_izvajalcev_zasebnik', models.FloatField(blank=True, null=True)),
                ('st_cakajocih_zelo_h', models.FloatField(blank=True, null=True)),
                ('st_cakajocih_hitro', models.FloatField(blank=True, null=True)),
                ('st_cakajocih_redno', models.FloatField(blank=True, null=True)),
                ('st_cakajocih_vsota', models.FloatField(blank=True, null=True)),
                ('st_vs_cakajocih_bolnisnica', models.FloatField(blank=True, null=True)),
                ('st_vs_cakajocih_zdravstveni_dom', models.FloatField(blank=True, null=True)),
                ('st_vs_cakajocih_zasebnik', models.FloatField(blank=True, null=True)),
                ('nad_dop_cd_zelo_h', models.FloatField(blank=True, null=True)),
                ('nad_dop_cd_hitro', models.FloatField(blank=True, null=True)),
                ('nad_dop_cd_redno', models.FloatField(blank=True, null=True)),
                ('nad_dop_cd_vsota', models.FloatField(blank=True, null=True)),
                ('nad_dop_cd_vsota_bolnisnica', models.FloatField(blank=True, null=True)),
                ('nad_dop_cd_vsota_zdravstveni_dom', models.FloatField(blank=True, null=True)),
                ('nad_dop_cd_vsota_zasebnik', models.FloatField(blank=True, null=True)),
                ('recorded_date', models.DateField()),
            ],
        ),
    ]