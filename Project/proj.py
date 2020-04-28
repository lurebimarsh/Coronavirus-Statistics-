from project import *
import pandas as pd


root = Tk()

root.state('zoomed')
header = Label(root, text='Coronavirus Comparison', font='Monsterrat 30 bold ')
header.grid(row=0, column=0, padx = 450, pady=20)

buttonframe = LabelFrame(root, text='Chart Option', padx=20, pady=20)
buttonframe.grid(row=6)

prompt = LabelFrame(root, text="ENTER COUNTRY NAME(S)", width=100, pady=10, padx=10)
prompt.grid(row=2, column=0, pady=0, padx=25)

country = Entry(prompt, width=100,  bd=3,  font='Monsterrat 15', justify='center')
country.grid(padx=10, ipady=10, pady=10, row=3)

def barplot():

    width=0.02
    hello= country.get().replace(' ','').split(',')
    countries_list=[]
    for i in hello:
        countries_list.append(i.capitalize())
    tot, death, active, rec = [],[],[],[]
    for nation in countries_list:
        x_axis, y_axis= [],[]
        dictionary = get_stats(nation)
        for key in dictionary:
            x_axis.append(key)
            if dictionary[key].replace(' ','')=='':
                y_axis.append(0)
                continue
            y_axis.append((dictionary[key].replace(',','')))

        tot.append(int(y_axis[1]))
        death.append(int(y_axis[3]))
        active.append(int(y_axis[5]))
        rec.append(int(y_axis[6]))

    plot_dict = {'Total Cases':tot,'Deaths':death, 'Recovered':rec, 'Active':active }
    print (plot_dict)
    df = pd.DataFrame(plot_dict).T

    df.plot(kind="bar")
    ax = df.plot(kind='bar', rot=0)
    ax.legend(countries_list)
    plt.show()


def totalcases():

    a,b,length,c = [],[],[],[]
    countries_list= country.get().lower().replace(' ','').split(',')

    tick = []
    for nation in countries_list:
        y_axis_final = []
        cumsum=0

        dictionary= {}

        x_axis, y_axis = [], []

        c.append(nation)

        dictionary = get_cases(nation, 'graph-cases-daily')

        for key in dictionary:
            x_axis.append(key.replace('"',''))
            if dictionary[key]=='null':
                y_axis.append(0)
                continue
            y_axis.append(int(dictionary[key]))


        for element in y_axis:
            cumsum += element
            y_axis_final.append(cumsum)


        a.append(x_axis)
        b.append(y_axis_final)

        length.append(len(x_axis))

        del x_axis
        del y_axis

    minlength = int(min(length))


    for x,y,z in zip(a,b,c):
        plt.plot(x,y,label=z.upper())

    for i in range(0,len(a[0]),10):
            tick.append(a[0][i])

    plt.xticks(tick, rotation=60)
    plt.legend()
    ab = plt.get_current_fig_manager()
    ab.window.state('zoomed')
    plt.tight_layout()
    plt.title('TOTAL CORONAVIRUS CASES')
    plt.subplots_adjust(left=0.06, bottom=0.11, right=0.95, top=0.94, wspace=0.2, hspace=0.2)
    plt.show()

def activecases():
    a,b,length,c = [],[],[],[]
    countries_list= country.get().lower().replace(' ','').split(',')

    tick = []
    for nation in countries_list:
        y_axis_final = []
        cumsum=0

        dictionary= {}

        x_axis, y_axis = [], []

        c.append(nation)

        dictionary = get_cases(nation, 'graph-active-cases-total')

        for key in dictionary:
            x_axis.append(key.replace('"',''))
            if dictionary[key]=='null':
                y_axis.append(0)
                continue
            y_axis.append(int(dictionary[key]))

        print (len(x_axis), len(y_axis))

        # for element in y_axis:
        #     cumsum += element
        #     y_axis_final.append(cumsum)
        y_axis_final=y_axis


        a.append(x_axis)
        b.append(y_axis_final)

        length.append(len(x_axis))

        del x_axis
        del y_axis

    minlength = int(min(length))


    for x,y,z in zip(a,b,c):
        plt.plot(x,y,label=z.upper())

    for i in range(0,len(a[0]),10):
            tick.append(a[0][i])

    plt.xticks(tick, rotation=60)
    plt.legend()
    ab = plt.get_current_fig_manager()
    ab.window.state('zoomed')
    plt.tight_layout()
    plt.title('ACTIVE CORONAVIRUS CASES')
    plt.subplots_adjust(left=0.06, bottom=0.11, right=0.95, top=0.94, wspace=0.2, hspace=0.2)
    plt.show()

def deaths():

    a,b,length,c = [],[],[],[]
    countries_list= country.get().lower().replace(' ','').split(',')

    tick = []
    for nation in countries_list:
        y_axis_final = []
        cumsum=0

        dictionary= {}

        x_axis, y_axis = [], []

        c.append(nation)

        dictionary = get_cases(nation, 'graph-deaths-daily')

        for key in dictionary:
            x_axis.append(key.replace('"',''))
            if dictionary[key]=='null':
                y_axis.append(0)
                continue
            y_axis.append(int(dictionary[key]))

        print (len(x_axis), len(y_axis))

        for element in y_axis:
            cumsum += element
            y_axis_final.append(cumsum)


        a.append(x_axis)
        b.append(y_axis_final)

        length.append(len(x_axis))

        del x_axis
        del y_axis

    minlength = int(min(length))


    for x,y,z in zip(a,b,c):
        plt.plot(x,y,label=z.upper())

    for i in range(0,len(a[0]),10):
            tick.append(a[0][i])

    plt.xticks(tick, rotation=60)
    plt.legend()
    ab = plt.get_current_fig_manager()
    ab.window.state('zoomed')
    plt.tight_layout()
    plt.title('TOTAL CORONAVIRUS DEATHS')
    plt.subplots_adjust(left=0.06, bottom=0.11, right=0.95, top=0.94, wspace=0.2, hspace=0.2)
    plt.show()

def get_text():
    pass

total = Button(buttonframe, borderwidth=1, text=' Total Cases ',font='arial 13', command=totalcases, height=2, width=20)
active = Button(buttonframe,borderwidth=1, text='Active Cases',font='arial 13', command=activecases, height=2, width=20)
death = Button(buttonframe, borderwidth=1,text='Total Deaths ',font='arial 13', command=deaths, height=2, width=20)
bar= Button(buttonframe, text='Bar Chart', font='arial 13', command=barplot, height=2, width=20)

total.grid(row=6,column=0, pady=5)
active.grid(row=6, column=1, pady=5)
death.grid(row=6, column=2, pady=5)
bar.grid(row=7, column=0, pady=2)

root.mainloop()
