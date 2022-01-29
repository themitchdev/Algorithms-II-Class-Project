from ChainingHash import ChainingHashTable
from packages import *
from Distance import distance_calc

class Truck(ChainingHashTable):
    sorted_addresses = []
    total_miles = 0
    start_time = ""

    def set_start_time(self, start_time):
        Truck.start_time = start_time
        # for i in range(40):
        #     if package_list.search(i) is not None and package_list.start_time is None:
        #         package_list.search(i).start_time = start_time
        #

    def sort(self):
        #self.hashmap = hashmap
        distance = 1000
        start = self.search(0)
        temp_list = []
        final_list = []
        min_distance = 1000
        for i in range(41):

            for j in range(1, 41):
                if self.search(j) is not None:
                    next = self.search(j)

                    temp_distance = distance_calc.get_distance(start.street, next.street)
                    if temp_distance <= min_distance:
                        min_distance = temp_distance
                        #print(min_distance)
                        if len(temp_list) > 0:
                            if temp_list[len(temp_list)-1][1].street == next.street:
                                temp_list.append([temp_distance, next])
                            else:
                                temp_list = []
                                temp_list.append([temp_distance, next])
                        else:
                            #print(next.street)
                            temp_list = []
                            temp_list.append([temp_distance, next])

            if len(final_list) > 10:
                if start == temp_list[len(temp_list) - 1][1]:
                    break

            for k in temp_list:
                self.remove(k[1].packageid)
                final_list.append(k)
            min_distance = 1000
            self.remove(start.packageid)
            start = final_list[len(final_list)-1][1]

        self.sorted_addresses = final_list

    def return_to_hub(self):
        last_address = self.sorted_addresses[-1][1].street
        last_timestamp = self.sorted_addresses[-1][1].time
        hub = package_list.search(0).street
        distance_to_hub = distance_calc.get_distance(last_address, hub)
        package_list.search(0).set_timestamp(last_timestamp, distance_to_hub)
        Truck.start_time = package_list.search(0).time
        # print(last_address)
        # print(last_timestamp)
        # print(hub)
        # print(distance_to_hub)
        # print(package_list.search(0).time)

    def deliver(self):
        total_time = self.start_time
        previous_address = Package("", "", "", "", "", "", "", "")

        for i in self.sorted_addresses:
            if i[1].street != previous_address.street:
                self.total_miles += i[0]
                i[1].set_timestamp(total_time, i[0])
                total_time = i[1].time
                i[1].start_time = self.start_time
            else:
                i[1].time = previous_address.time
                i[1].start_time = self.start_time
            previous_address = i[1]
            # print(i[1].street)
            # print(i[1].time)




    def get_total_miles(self):
        self.total_miles = 0
        for i in self.sorted_addresses:
            self.total_miles += i[0]
        # for i in range(1, 40):
        #     print(package_list.search(i).packageid)
        #     print(package_list.search(i).time)

        return self.total_miles


truck1 = Truck(16)
truck1.insert(0, package_list.search(0))
truck1.insert(2, package_list.search(2))
truck1.insert(7, package_list.search(7))
truck1.insert(10, package_list.search(10))
truck1.insert(13, package_list.search(13))
truck1.insert(14, package_list.search(14))
truck1.insert(15, package_list.search(15))
truck1.insert(16, package_list.search(16))
truck1.insert(19, package_list.search(19))
truck1.insert(20, package_list.search(20))
truck1.insert(21, package_list.search(21))
truck1.insert(24, package_list.search(24))
truck1.insert(27, package_list.search(27))
truck1.insert(29, package_list.search(29))
truck1.insert(33, package_list.search(33))
truck1.insert(35, package_list.search(35))
truck1.insert(39, package_list.search(39))

truck2 = Truck(16)
truck2.insert(0, package_list.search(0))
truck2.insert(3, package_list.search(3))
truck2.insert(8, package_list.search(8))
truck2.insert(30, package_list.search(30))
truck2.insert(5, package_list.search(5))
truck2.insert(37, package_list.search(37))
truck2.insert(38, package_list.search(38))
truck2.insert(6, package_list.search(6))
truck2.insert(12, package_list.search(12))
truck2.insert(17, package_list.search(17))
truck2.insert(31, package_list.search(31))
truck2.insert(32, package_list.search(32))
truck2.insert(36, package_list.search(36))
truck2.insert(18, package_list.search(18))
truck2.insert(9, package_list.search(9))

truck3 = Truck(11)
truck3.insert(0, package_list.search(0))

truck3.insert(1, package_list.search(1))
truck3.insert(4, package_list.search(4))
truck3.insert(28, package_list.search(28))
truck3.insert(40, package_list.search(40))
truck3.insert(25, package_list.search(25))
truck3.insert(26, package_list.search(26))
truck3.insert(34, package_list.search(34))
truck3.insert(11, package_list.search(11))
truck3.insert(23, package_list.search(23))
truck3.insert(22, package_list.search(22))

truck1.set_start_time("8:00")
truck1.sort()
truck1.deliver()
truck2.set_start_time("9:05")
truck2.sort()
truck2.deliver()
truck1.return_to_hub()
truck3.sort()
truck3.deliver()




