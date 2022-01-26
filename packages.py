import csv
from ChainingHash import ChainingHashTable
import datetime
from Distance import distance_calc


class Package(ChainingHashTable):
    start_time = "8:00"

    def __init__(self, packageid = None, street = None, city = None, state = None, zipcode = None, eta = None, weight = None, comment = None):
        ChainingHashTable.__init__(self)
        self.packageid = packageid
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.eta = eta
        self.weight = weight
        self.comment = comment
        self.time = None
        self.start_time = None

    def set_timestamp(self, time, distance_travelled):
        self.time = time.split(':')
        self.time = datetime.datetime(year=100, month=1, day=1, hour=int(self.time[0]), minute=int(self.time[1]), second=0)
        time_elapsed = distance_travelled / 18
        mins_raw = time_elapsed * 60
        mins = int(mins_raw)
        secs = (mins_raw - mins) * 60
        secs = int(secs)
        self.time = self.time + datetime.timedelta(hours=0, minutes=mins, seconds=secs)
        self.time = str(self.time.time())
        return time

    def status_one_package(self, user_num, string_user_time):
        status = None
        package = package_list.search(user_num)
        delivered_time = package.time
        delivered_time = delivered_time.split(":")
        str_user_time = string_user_time
        user_time = [0,0]
        begin_time = package.start_time.split(":")

        for i in range(0, len(delivered_time)):
            delivered_time[i] = int(delivered_time[i])

        #for i in range(0, len(begin_time)):
        begin_time[0] = int(begin_time[0])
        begin_time[1] = int(begin_time[1])

        for i in range(0, len(string_user_time)):
            user_time[i] = int(string_user_time[i])

        if user_time[0] < begin_time[0] or (user_time[0] == begin_time[0] and user_time[1] < begin_time[1]):
            status = "at HUB"
        elif user_time[0] > delivered_time[0] or (user_time[0] == delivered_time[0] and user_time[1] > delivered_time[1]):

            status = "delivered"
        else:
            status = "in transit"

        string = f"At {self.color.CYAN}{':'.join(str_user_time)}{self.color.END} package with {self.color.BLUE}ID# {str(package.packageid)} {self.color.END}and with delivery address: {self.color.YELLOW}{package.street}, {package.city}, {package.zipcode}{self.color.END} was {self.color.GREEN}{status}{self.color.END}"

        print(string)

    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    def status_all_packages(self, user_time):
        for i in range(40):
            if package_list.search(i).time is not None:
                self.status_one_package(i, user_time)


package_list = Package(40)

with open ('packageFile.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        pid = int(row[0])
        pstreet = row[1]
        pcity = row[2]
        pstate = row[3]
        pzipcode = row[4]
        peta = row[5]
        pweight = row[6]
        pcomment = row[7]
        p = Package(pid, pstreet, pcity, pstate, pzipcode, peta, pweight, pcomment)
        package_list.insert(pid, p)

hub = Package(0, "4001 South","","","","","","")
package_list.insert(0,hub)








