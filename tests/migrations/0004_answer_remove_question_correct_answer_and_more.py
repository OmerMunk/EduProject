# Generated by Django 4.0.3 on 2022-03-12 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_testexecuted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='wrong_answer1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='wrong_answer2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='wrong_answer3',
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='testexecuted',
            name='correct',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testexecuted',
            name='wrong',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='MakeTest',
            fields=[
                ('test_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tests.test')),
                ('answers', models.ManyToManyField(to='tests.answer')),
            ],
            options={
                'abstract': False,
            },
            bases=('tests.test',),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tests.question'),
        ),
    ]