""" To create for only computer using's graph"""
import pandas as pd
import pygal as pg
def com(whatyear, whatfilter, num=0):
    """
        Plot only Computer using graph
        com(whatyear, whatfilter)
    """
    #whatyear = 2559, 2558, 2557, 2556, 2555, 2554, 2553, all
    #whatfilter = location, activity, region
    last, last_all, filter_text = ' in ' + whatyear, '', ''
    if whatfilter.lower() == 'region':
        last = ' per day in '+whatyear
    else:
        filter_text = 'and ages'
    if whatyear.lower() == 'all' :
        last_all, last = ' years', ' of '+whatyear

    data = call_data(whatyear, whatfilter, num)
    info = select_data(data, whatyear, whatfilter)
    print(data)
    print(info)

    #plotting graph all years use line grapah / single year uses bar graph
    head_graph = 'Number of computer users by '+whatfilter+' '+filter_text+' to use computer'+last+last_all
    if whatyear == 'all':
        chart = pg.Line(title=head_graph+'  (100%)')
        data_head = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
        kind = list((data[num])[whatfilter])
        print(kind)
        for yrs in range(len(kind)):
            chart.add(kind[yrs], info[yrs])

    else: #single year
        chart = pg.Bar(title=head_graph+'  (100%)')
        data_head = [i for i in data[whatfilter]]
        kind = list(data)[2:]
        for i in range(len(kind)):
            chart.add(kind[i], info[i])
    chart.x_labels = [i for i in data_head]
    chart.render_to_file('../graph/Graph_com.svg')

def call_data(whatyear, whatfilter, num):
    """This function call data and return data
       This function return data_head and data"""
    #0, 1, 2 = location, activity, region
    num = 0 #Table12 location
    if whatfilter.lower() == 'activity': num = 1 #Tab14 activity
    if whatfilter.lower() == 'region': num = 2 #Tab16 region
    find_data = {'2559':['../data/59/Tab12.csv', \
                         '../data/59/Tab14.csv', \
                         '../data/59/Tab16.csv'],
                 '2558':['../data/58/Tab12.csv', \
                         '../data/58/Tab14.csv', \
                         '../data/58/Tab16.csv'],
                 '2557':['../data/57/Tab12.csv', \
                         '../data/57/Tab14.csv', \
                         '../data/57/Tab16.csv'],
                 '2556':['../data/56/Tab12.csv', \
                         '../data/56/Tab14.csv', \
                         '../data/56/Tab16.csv'],
                 '2555':['../data/55/Tab12.csv', \
                         '../data/55/Tab14.csv', \
                         '../data/55/Tab16.csv'],
                 '2554':['../data/54/Tab12.csv', \
                         '../data/54/Tab14.csv', \
                         '../data/54/Tab16.csv'],
                 '2553':['../data/53/Tab12.csv', \
                         '../data/53/Tab14.csv', \
                         '../data/53/Tab16.csv']}
    if whatyear == 'all':
        year = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
        data = [call_data(i, whatfilter, num) for i in year]
    else:
        data = pd.read_csv(find_data[whatyear][num])
    return data

def select_data(data, whatyear, whatfilter=''):
    """Work like a filter to select data for plotting"""
    whatfilter_type, kind = '', ''
    info, infos = [], []
    if whatyear == 'all':
        if whatfilter == "region":
            whatfilter_type = float(input('A time(hours) you want to define: '))
            if whatfilter_type < 1:
                kind = 'Less than 1 hour'
            if whatfilter_type >= 1 and whatfilter_type < 2:
                kind = '1-2 hours'
            if whatfilter_type >= 2 and whatfilter_type < 3:
                kind = '2-3 hours'
            if whatfilter_type >= 3 and whatfilter_type < 4:
                kind = '3-4 hours'
            if whatfilter_type >= 4 and whatfilter_type < 5:
                kind = '4-5 hours'
            if whatfilter_type >= 5 and whatfilter_type < 6:
                kind = '5-6 hours'
            if whatfilter_type >= 6: #> 6 hours
                kind = 'More than 6 hours' #get kind of region(ages)
        if whatfilter == "location" or whatfilter == "activity":
            whatfilter_type = float(input("An ages(years) you want to define: "))
            if whatfilter_type < 11:
                kind = '6-10 years'
            if whatfilter_type >= 11 and whatfilter_type < 15:
                kind = '11-14 years'
            if whatfilter_type >= 15 and whatfilter_type < 20:
                kind = '15-19 years'
            if whatfilter_type >= 20 and whatfilter_type < 25:
                kind = '20-24 years'
            if whatfilter_type >= 25 and whatfilter_type < 30:
                kind = '25-29 years'
            if whatfilter_type >= 30 and whatfilter_type < 35:
                kind = '30-34 years'
            if whatfilter_type >= 35 and whatfilter_type < 40:
                kind = '35-39 years'
            if whatfilter_type >= 40 and whatfilter_type < 50:
                kind = '40-49 years'
            if whatfilter_type >= 50 and whatfilter_type < 60:
                kind = '50-59 years'
            if whatfilter_type >= 60: # >60 years
                kind = '60 years and over' #get kind of location and activity(hrs)
        infos = [[[(data[yrs][kind][i]*100)/data[yrs]['Total'][i] for i in \
                range(len(data[yrs][kind]))]] for yrs in range(len(data))]
        info = [[infos[j][i] for j in range(len(infos))] for i in range(len(infos[0]))]
        # for yrs in range(len(data)):
        #     memo = [(data[yrs][kind][i]*100)/data[yrs]['Total'][i] for i in range(len(data[yrs][kind]))]
        #     infos.append(memo)
        # for i in range(len(infos[0])):
        #     memo = [infos[j][i] for j in range(len(infos))]
        #     info.append(memo)
        print('infos:', infos)
        print()
    else: #region, activity, location
        info = [[(data[kind][i]*100)/data['Total'][i] for i in \
                range(len(data[kind]))] for kind in list(data)[2:]]
        # if whatfilter == 'region':
        #     info = [[(data['Less than 1 hour'][i]*100) / data['Total'][i] for i in range(len(data['Less than 1 hour']))], \
        #             [(data['1-2 hours'][i]*100) / data['Total'][i] for i in range(len(data['1-2 hours']))], \
        #             [(data['2-3 hours'][i]*100) / data['Total'][i] for i in range(len(data['2-3 hours']))], \
        #             [(data['3-4 hours'][i]*100) / data['Total'][i] for i in range(len(data['3-4 hours']))], \
        #             [(data['4-5 hours'][i]*100) / data['Total'][i] for i in range(len(data['4-5 hours']))], \
        #             [(data['5-6 hours'][i]*100) / data['Total'][i] for i in range(len(data['5-6 hours']))], \
        #             [(data['More than 6 hours'][i]*100) / data['Total'][i] for i in range(len(data['More than 6 hours']))]]
        # if whatfilter == 'location' or whatfilter == 'activity':
        #     # for kind in sorted(data)[:-1]:
        #     #     memo = [(data[kind][i]*100)/data['Total'][i] for i in range(len(data[kind])-1)]
        #     #     info.append(memo)
        #     info = [[(data['6-10 years'][i]*100)/data['Total'][i] for i in range(len(data['6-10 years']))], \
        #             [(data['11-14 years'][i]*100)/data['Total'][i] for i in range(len(data['11-14 years']))], \
        #             [(data['15-19 years'][i]*100)/data['Total'][i] for i in range(len(data['15-19 years']))], \
        #             [(data['20-24 years'][i]*100)/data['Total'][i] for i in range(len(data['20-24 years']))], \
        #             [(data['25-29 years'][i]*100)/data['Total'][i] for i in range(len(data['25-29 years']))], \
        #             [(data['30-34 years'][i]*100)/data['Total'][i] for i in range(len(data['30-34 years']))], \
        #             [(data['35-39 years'][i]*100)/data['Total'][i] for i in range(len(data['35-39 years']))], \
        #             [(data['40-49 years'][i]*100)/data['Total'][i] for i in range(len(data['40-49 years']))], \
        #             [(data['50-59 years'][i]*100)/data['Total'][i] for i in range(len(data['50-59 years']))], \
        #             [(data['60 years and over'][i]*100)/data['Total'][i] for i in range(len(data['60 years and over']))]]
    return info

com(input(), input())
