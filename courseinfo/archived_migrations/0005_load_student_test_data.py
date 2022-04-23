from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

STUDENTS = [

    {
        'first_name': 'Elizabeth',
        'last_name': 'Wilson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Victor',
        'last_name': 'Lewis',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Christopher',
        'last_name': 'Paterson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Nicola',
        'last_name': 'Powell',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Ava',
        'last_name': 'White',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Fiona',
        'last_name': 'Bower',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Owen',
        'last_name': 'Reid',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lily',
        'last_name': 'Miller',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Deirdre',
        'last_name': 'Gill',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Neil',
        'last_name': 'Marshall',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Emily',
        'last_name': 'Sanderson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Jessica',
        'last_name': 'King',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Adrian',
        'last_name': 'Ogden',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Gabrielle',
        'last_name': 'Lee',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Joshua',
        'last_name': 'Abraham',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Brian',
        'last_name': 'Hill',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Bernadette',
        'last_name': 'Buckland',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Theresa',
        'last_name': 'Thomson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Ella',
        'last_name': 'Burgess',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Donna',
        'last_name': 'James',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Audrey',
        'last_name': 'Hudson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Charles',
        'last_name': 'Newman',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Adrian',
        'last_name': 'Black',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Wright',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Dorothy',
        'last_name': 'McLean',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Stephen',
        'last_name': 'Glover',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Gabrielle',
        'last_name': 'Poole',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Owen',
        'last_name': 'Edmunds',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Amelia',
        'last_name': 'Bower',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Ava',
        'last_name': 'Graham',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Adam',
        'last_name': 'Taylor',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lily',
        'last_name': 'Ross',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Joseph',
        'last_name': 'Skinner',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Grace',
        'last_name': 'Greene',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Ryan',
        'last_name': 'Parr',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Peter',
        'last_name': 'Russell',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'William',
        'last_name': 'Mills',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Sharp',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Chloe',
        'last_name': 'Anderson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lisa',
        'last_name': 'Bond',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Boris',
        'last_name': 'Paterson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Sam',
        'last_name': 'Wilkins',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Max',
        'last_name': 'Lyman',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Una',
        'last_name': 'Pullman',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Austin',
        'last_name': 'Wilkins',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Powell',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Neil',
        'last_name': 'Grant',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Maria',
        'last_name': 'Piper',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Andrea',
        'last_name': 'Walsh',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Anne',
        'last_name': 'Clark',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Tim',
        'last_name': 'Nolan',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Victor',
        'last_name': 'Welch',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Alan',
        'last_name': 'Davidson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Charles',
        'last_name': 'Churchill',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Jessica',
        'last_name': 'Duncan',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Martin',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Maria',
        'last_name': 'Arnold',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Sophie',
        'last_name': 'Clark',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Jacob',
        'last_name': 'Bailey',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Harry',
        'last_name': 'Churchill',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Karen',
        'last_name': 'Lyman',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Trevor',
        'last_name': 'Hunter',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Stephen',
        'last_name': 'Lee',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Vanessa',
        'last_name': 'Underwood',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Richard',
        'last_name': 'Kelly',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Amelia',
        'last_name': 'Campbell',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Zoe',
        'last_name': 'McLean',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Sam',
        'last_name': 'Forsyth',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Phil',
        'last_name': 'Wright',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Maria',
        'last_name': 'Hudson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Diana',
        'last_name': 'Mackay',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Stewart',
        'last_name': 'Ellison',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Sue',
        'last_name': 'Edmunds',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Karen',
        'last_name': 'Ogden',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Carol',
        'last_name': 'Martin',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Oliver',
        'last_name': 'Wilkins',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Adam',
        'last_name': 'Bower',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Katherine',
        'last_name': 'Clarkson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Carol',
        'last_name': 'Turner',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Ian',
        'last_name': 'James',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Una',
        'last_name': 'McLean',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Heather',
        'last_name': 'Clark',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Liam',
        'last_name': 'Ellison',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Madeleine',
        'last_name': 'Gill',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Warren',
        'last_name': 'Berry',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Yvonne',
        'last_name': 'Lyman',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Claire',
        'last_name': 'Abraham',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Andrea',
        'last_name': 'Hemmings',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Claire',
        'last_name': 'Clarkson',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Max',
        'last_name': 'Mackenzie',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Luke',
        'last_name': 'Ince',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Samantha',
        'last_name': 'Tucker',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'James',
        'last_name': 'Lewis',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Wendy',
        'last_name': 'Cornish',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Evan',
        'last_name': 'Hamilton',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Caroline',
        'last_name': 'Lee',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Stephanie',
        'last_name': 'Smith',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Lily',
        'last_name': 'Jones',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Melanie',
        'last_name': 'Peake',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Richard',
        'last_name': 'Smith',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Neil',
        'last_name': 'Randall',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'John',
        'last_name': 'Quinn',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Emma',
        'last_name': 'Bell',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Stephanie',
        'last_name': 'Forsyth',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Claire',
        'last_name': 'Young',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Felicity',
        'last_name': 'Avery',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Robert',
        'last_name': 'Glover',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Paul',
        'last_name': 'Tucker',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Abigail',
        'last_name': 'Morrison',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Carl',
        'last_name': 'Ross',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Jack',
        'last_name': 'Parr',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Owen',
        'last_name': 'Ogden',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Grace',
        'last_name': 'Ball',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Felicity',
        'last_name': 'Hill',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Dylan',
        'last_name': 'Fisher',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Angela',
        'last_name': 'Black',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Carolyn',
        'last_name': 'Murray',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Michelle',
        'last_name': 'Morrison',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Penelope',
        'last_name': 'Glover',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Frank',
        'last_name': 'Newman',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Penelope',
        'last_name': 'Blake',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Theresa',
        'last_name': 'Russell',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Trevor',
        'last_name': 'Cameron',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Stephen',
        'last_name': 'Cornish',
        'disambiguator': 'Testing',
    },
    {
        'first_name': 'Anthony',
        'last_name': 'Parr',
        'disambiguator': 'Testing',
    },

]


def add_student_data(apps, schema_editor):
    student_class = apps.get_model('courseinfo', 'Student')
    for student in STUDENTS:
        try:
            duplicate_object = student_class.objects.get(
                first_name=student['first_name'],
                last_name=student['last_name'],
                disambiguator=student['disambiguator']
            )
            print('Duplicate student entry not added to student table:', student['first_name'], student['last_name'])
        except ObjectDoesNotExist:
            student_object = student_class.objects.create(
                first_name=student['first_name'],
                last_name=student['last_name'],
                disambiguator=student['disambiguator']
            )


def remove_student_data(apps, schema_editor):
    student_class = apps.get_model('courseinfo', 'Student')
    for student in STUDENTS:
        student_object = student_class.objects.get(
            first_name=student['first_name'],
            last_name=student['last_name'],
            disambiguator=student['disambiguator']
        )
        student_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0004_load_instructor_test_data'),
    ]

    operations = [
        migrations.RunPython(
            add_student_data,
            remove_student_data
        )
    ]
