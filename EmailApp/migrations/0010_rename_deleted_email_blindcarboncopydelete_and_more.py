# Generated by Django 4.1.3 on 2023-01-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmailApp', '0009_alter_email_receiver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='Deleted',
            new_name='BlindCarbonCopyDelete',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='Draft',
            new_name='BlindCarbonCopyDraft',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='Important',
            new_name='BlindCarbonCopyImportant',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='Label',
            new_name='BlindCarbonCopyLabel',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='Read',
            new_name='BlindCarbonCopyRead',
        ),
        migrations.AddField(
            model_name='email',
            name='BlindCarbonCopyTrash',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='CarbonCopyDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='CarbonCopyDraft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='CarbonCopyImportant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='CarbonCopyLabel',
            field=models.CharField(choices=[('None', 'None'), ('Personal', 'Personal'), ('Important', 'Important'), ('Private', 'Private'), ('Company', 'Company')], default='None', max_length=10),
        ),
        migrations.AddField(
            model_name='email',
            name='CarbonCopyRead',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='CarbonCopyTrash',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='ReceiverDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='ReceiverDraft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='ReceiverImportant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='ReceiverLabel',
            field=models.CharField(choices=[('None', 'None'), ('Personal', 'Personal'), ('Important', 'Important'), ('Private', 'Private'), ('Company', 'Company')], default='None', max_length=10),
        ),
        migrations.AddField(
            model_name='email',
            name='ReceiverRead',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='ReceiverTrash',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='SenderDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='SenderDraft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='SenderImportant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='SenderLabel',
            field=models.CharField(choices=[('None', 'None'), ('Personal', 'Personal'), ('Important', 'Important'), ('Private', 'Private'), ('Company', 'Company')], default='None', max_length=10),
        ),
        migrations.AddField(
            model_name='email',
            name='SenderTrash',
            field=models.BooleanField(default=False),
        ),
    ]
