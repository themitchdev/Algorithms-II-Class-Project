import csv


class LookUpDistance:
    def __init__(self):
        self.address_list = []
        self.address_list2 = []


    def add(self, alist):
        self.address_list.append(alist)

    def add2(self, alist2):
        self.address_list2.append(alist2)

    def get_distance(self, address1, address2):
        from_address = address1
        to_address = address2

        if from_address == to_address:
            return 0

        from_index = self.address_list2.index(from_address)
        to_index = self.address_list2.index(to_address)

        if to_index > from_index:
            temp = from_index
            from_index = to_index
            to_index = temp

        return float  (self.address_list[from_index][to_index+2])


distance_calc = LookUpDistance()

with open('distanceFile.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        distance_calc.add(row)
        distance_calc.add2(row[1])
#
# start = "4001 South"
# next_address = "4300 S 1300 E"
# distance = distance_calc.get_distance(next_address, start)
# print(distance)
# distance = distance_calc.get_distance(start, next_address)
# print(distance)

# for i in distance_calc.address_list:
#     print(i)
