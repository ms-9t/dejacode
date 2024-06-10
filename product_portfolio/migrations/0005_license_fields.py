# Generated by Django 5.0.6 on 2024-06-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_portfolio", "0004_alter_scancodeproject_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="license_expression",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text='On a product in DejaCode, a license expression defines the relationship of one or more licenses to that software as declared by its licensor. More than one applicable license can be expressed as "license-key-a AND license-key-b". A choice of applicable licenses can be expressed as "license-key-a OR license-key-b", and you can indicate the primary (preferred) license by placing it first, on the left-hand side of the OR relationship. The relationship words (OR, AND) can be combined as needed, and the use of parentheses can be applied to clarify the meaning; for example "((license-key-a AND license-key-b) OR (license-key-c))". An exception to a license can be expressed as "license-key WITH license-exception-key".',
                max_length=1024,
            ),
        ),
        migrations.AlterField(
            model_name="productcomponent",
            name="license_expression",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text='The License Expression assigned to a DejaCode Product Package or Product Component is an editable value equivalent to a "concluded license" as determined by a curator who has performed analysis to clarify or correct the declared license expression, which may have been assigned automatically (from a scan or an associated package definition) when the Package or Component was originally created, or which may require the assertion of a choice of license.A license expression defines the relationship of one  or more licenses to a software object. More than one applicable license can be expressed as "license-key-a AND license-key-b". A choice of applicable licenses can be expressed as "license-key-a OR license-key-b", and you can indicate the primary (preferred) license by placing it first, on the left-hand side of the OR relationship. The relationship words (OR, AND) can be combined as needed, and the use of parentheses can be applied to clarify the meaning; for example "((license-key-a AND license-key-b) OR (license-key-c))". An exception to a license can be expressed as "license-key WITH license-exception-key".',
                max_length=1024,
                verbose_name="Concluded license expression",
            ),
        ),
        migrations.AlterField(
            model_name="productpackage",
            name="license_expression",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text='The License Expression assigned to a DejaCode Product Package or Product Component is an editable value equivalent to a "concluded license" as determined by a curator who has performed analysis to clarify or correct the declared license expression, which may have been assigned automatically (from a scan or an associated package definition) when the Package or Component was originally created, or which may require the assertion of a choice of license.A license expression defines the relationship of one  or more licenses to a software object. More than one applicable license can be expressed as "license-key-a AND license-key-b". A choice of applicable licenses can be expressed as "license-key-a OR license-key-b", and you can indicate the primary (preferred) license by placing it first, on the left-hand side of the OR relationship. The relationship words (OR, AND) can be combined as needed, and the use of parentheses can be applied to clarify the meaning; for example "((license-key-a AND license-key-b) OR (license-key-c))". An exception to a license can be expressed as "license-key WITH license-exception-key".',
                max_length=1024,
                verbose_name="Concluded license expression",
            ),
        ),
    ]
