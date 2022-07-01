import random


class PrisonersProblem:
    found = int()  # number of prisoners that found box with their number
    not_found = int()  # number of prisoners that does not found box with their number
    dictionary = dict()  # dictionary for boxes with numbers k:box v:prisoner number

    def __init__(self, number_of_prisoners: int, max_tries: int = None):
        self.number_of_prisoners = number_of_prisoners
        if not max_tries:
            self.max_tries = self.number_of_prisoners // 2
        else:
            self.max_tries = max_tries
        self.__initialize_dictionary()

    def __generate_number(self) -> int:
        # rn = random.randrange(1, self.number_of_prisoners + 1)
        # while rn in self.dictionary.values():
        #     rn = random.randrange(1, self.number_of_prisoners + 1)
        # return rn
        while (rn := random.randrange(1, self.number_of_prisoners + 1)) in self.dictionary.values():
            pass
        return rn

    def __initialize_dictionary(self):
        """
        initialize dictionary
        key: box number
        value: prisoner number
        """
        for prisoner in range(self.number_of_prisoners):
            self.dictionary.setdefault(prisoner + 1, self.__generate_number())

    def percentage_of_finding_box_with_right_number(self) -> float:
        """
        calculates percentage chance of finding right number inside box
        :return: percentage chance of finding right number inside box
        """
        total = int()
        for x in range(self.max_tries + 1, self.number_of_prisoners + 1):
            total += 1 / x
        return (1 - total) * 100

    def __get_value(self, key: int) -> int:
        """
        used for searching right prisoner number using prisoner number found in box
        :param key: box number
        :return: prisoner number
        """
        return self.dictionary.get(key)

    def start(self, toggle_output: bool = True) -> None:
        """
        value found inside a box is a box number that will be opened afterwards. (it creates cycle)
        :param toggle_output: printing the output
        :return: None
        """
        for prisoner in range(1, self.number_of_prisoners + 1):  # loops through all prisoners
            number_of_tries = 1  # number of tries used for searching their number
            value = self.__get_value(prisoner)  # gets box value from prisoner
            while value != prisoner:  # repeats until the value equals to prisoner
                if number_of_tries == self.max_tries:  # checks if number of tries is equals to half of the prisoners
                    if toggle_output:  # printing the output
                        print(f"Prisoner {prisoner} does not found their number. Number of tries: {number_of_tries}")
                    self.not_found += 1  # adds one to prisoners that does not found their number
                    break  # breaks the while loop, because prisoner does not found their number

                value = self.__get_value(value)  # passes the value as box and returns prisoner number
                number_of_tries += 1  # number of tries increases by one

            else:  # if the value equals to prisoner number
                if toggle_output:  # printing the output
                    print(f"Prisoner {prisoner} Found their number. Number of tries: {number_of_tries}")
                self.found += 1  # adds one to prisoners that found their number


if __name__ == '__main__':
    p = PrisonRiddle(number_of_prisoners=100, max_tries=69)
    p.start()

    # print(p.dictionary)
    # print(p.percentage_of_finding_box_with_right_number())
    # print(p.found, p.not_found)
