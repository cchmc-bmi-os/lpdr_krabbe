from django.shortcuts import render
import json

diagnosis = [
    {'id': '1', 'name' : 'EIKD', 'value':109},
    {'id': '2', 'name' : 'LOKD', 'value': 26},
    {'id': '3', 'name' : 'LIKD', 'value' : 20},
    {'id': '4', 'name' : 'Unaffected', 'value': 13},
    {'id': '5', 'name' : 'Pre-symp EIKD', 'value' : 12},
    {'id': '6', 'name' : 'Adult', 'value': 5},
    {'id': '7', 'name' : 'Pre-symp LOKD', 'value': 5},
    {'id': '8', 'name' : 'Adolescent', 'value': 3},
    {'id': '9', 'name' : 'High Risk', 'value': 3},
    ]



genders = [
    {'name' : 'Male', 'y' : 97},
    {'name' : 'Female', 'y' : 88},
]


placebirth = [
    {'name' : 'US', 'code' : 'US', 'value' : 146},
    {'name' : 'Canada', 'code' : 'CA', 'value' : 12},
    {'name' : 'United Kingdom', 'code' : 'GB', 'value' : 9},
    {'name' : 'Sweden', 'code' : 'SE', 'value' : 4},
    {'name' : 'Brazil', 'code' : 'BR', 'value' : 2},
    {'name' : 'Australia', 'code' : 'AU', 'value' : 1},
    {'name' : 'Belgium', 'code' : 'BE', 'value' : 1},
    {'name' : 'Gauteng', 'code' : 'BE', 'value' : 1},
    {'name' : 'Germany', 'code' : 'DE', 'value' : 1},
    {'name' : 'India', 'code' : 'DE', 'value' : 1},
    {'name' : 'Italy', 'code' : 'DE', 'value' : 1},
    {'name' : 'New Zealand', 'code' : 'DE', 'value' : 1}
]


def data_summary(request):
    return render(request, 'data_summary.html', {
        'DIAGNOSIS': json.dumps(diagnosis),
        'GENDERS': json.dumps(genders),
        'PLACEBIRTH': json.dumps(placebirth)
    })

