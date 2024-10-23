def main():
    salary = 129000
    bonus1 = 50100
    bonus2 = 33100
    rsu = 111531
    rsu_vest = [0.05, 0.15, 0.4, 0.4]

    year1 = salary + bonus1 + (rsu * rsu_vest[0])
    year2 = salary + bonus2 + (rsu * rsu_vest[1])
    year3 = salary + (rsu * rsu_vest[2])
    year4 = salary + (rsu * rsu_vest[3])
    avg = (year1 + year2 + year3 + year4) / 4
    print(f'intern salary: ${12 * 9100}')
    print(f'year 1: ${year1}\nyear 2: ${year2}\nyear 3: ${year3}\nyear 4: ${year4}\n')
    print(f'average: ${avg}')



main()