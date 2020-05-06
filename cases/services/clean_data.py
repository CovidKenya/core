

def remove_provinces(data, date_range):
    countries_with_provinces = []
    names_of_countries_with_prov = []

    # get countries with provinces
    for country in data[:]:
        if country['province'] != None:
            if country['country'] not in names_of_countries_with_prov:
                names_of_countries_with_prov.append(country['country'])
            countries_with_provinces.append(data.pop(data.index(country)))
        else:
            pass

    # deal with countries with provinces
    for country_name in names_of_countries_with_prov[:]:  # for each country,
        countries = list(
            filter(lambda x: x['country'] == country_name, countries_with_provinces))
        names_of_countries_with_prov.remove(country_name)
        # calculate total cases, deaths & recovered per day
        cases = {}
        recovered = {}
        deaths = {}
        for date in date_range:
            cs = 0
            dt = 0
            rc = 0
            # per province
            for prov in countries:
                cs += prov["timeline"]["cases"][date]
                dt += prov["timeline"]["deaths"][date]
                rc += prov["timeline"]["recovered"][date]
            cases[date] = cs
            recovered[date] = rc
            deaths[date] = dt
        totals = ({'country': country_name, 'province': None, 'timeline': {
            'cases': cases, 'deaths': deaths, 'recovered': recovered}})
        data.append(totals)

    return data
