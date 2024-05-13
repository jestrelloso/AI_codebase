# Generated by Django 5.0.4 on 2024-05-04 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_codeexplainer_quiz_codeexplainer_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codeexplainer',
            old_name='question',
            new_name='_question',
        ),
        migrations.AddField(
            model_name='codeexplainer',
            name='_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='code_explainer', to='api.answer'),
        ),
    ]
