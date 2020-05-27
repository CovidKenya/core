from datetime import datetime

from cases.models import VisualCountry, VisualCases, VisualDeaths, VisualRecovered


def save_historical_data(data):
    countries_saved = VisualCountry.objects.all()
    #

    for obj in data:

        #
        if countries_saved.filter(name__exact=obj["country"]).exists():
            country = countries_saved.get(name__exact=obj["country"])
        else:
            con = VisualCountry(name=obj["country"])
            con.save()
            country = con

        # Cases
        cases_list = []

        try:
            for case in obj["timeline"]["cases"]:
                number = obj["timeline"]["cases"][case]
                date = datetime.strptime(case, "%m/%d/%y").date()
                cases_list.append(VisualCases(country=country, date=date, cases=number))

            VisualCases.objects.bulk_create(cases_list)
        except Exception as error:
            # handle any other error
            raise error

        # Deaths
        deaths_list = []
        try:
            for death in obj["timeline"]["deaths"]:
                number = obj["timeline"]["deaths"][death]
                date = datetime.strptime(death, "%m/%d/%y").date()
                deaths_list.append(VisualDeaths(country=country, date=date, deaths=number))

            VisualDeaths.objects.bulk_create(deaths_list)
        except Exception as error:
            # handle any other error
            raise error

        # Recovered
        recovered_list = []
        try:
            for rec in obj["timeline"]["recovered"]:
                number = obj["timeline"]["recovered"][rec]
                date = datetime.strptime(rec, "%m/%d/%y").date()
                recovered_list.append(VisualRecovered(country=country, date=date, recovered=number))

            VisualRecovered.objects.bulk_create(recovered_list)

        except Exception as error:
            # handle any other error
            raise error
