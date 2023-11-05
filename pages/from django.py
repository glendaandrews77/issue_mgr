from django.db import migrations

def populate_team(apps, schema_editor):
    entries = {
        "alpha": "The A team",
        "bravo": "The B team",
        "Charlie": "The C team",
        "delta": "The D team"
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in entries.items():
        team_obj = Team(name=key, description=value)
        team_obj.save()

def populate_role(apps, schema_editor):
    entries = {
        "developer": "The person who writes the code and builds the product",
        "scrum master": "The team's coach",
        "product owner": "The person who has ownership over the delivery of the product"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_team),
        migrations.RunPython(populate_role),
    ]
