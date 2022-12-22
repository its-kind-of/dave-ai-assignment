from flask import Flask, render_template, request
import pickle
#import numpy as np


app = Flask(__name__)

#-----------------------------------------------------------------------------------------------
# created a class
class BusStop:

    # created the constructor to accept the number of people & buses
    def __init__(self, number_of_people, number_of_buses):
        # defined the data
        self.number_of_people = number_of_people
        self.number_of_buses = number_of_buses

    # created the instance method
    def do_allocation(self):
        """
        This function will accept the two user inputs int (number of people and busses)
        return: array of number of people got into first bus, number of people got into second bus, and so on...

        """
        # array of containing the number people got into bus vice versa.
        allocation = []
        # capacity of the bus
        capacity = 1
        # loop in range with bus counts
        for i in range(self.number_of_buses):
            # checking if the number of people is greater than capacity of the bus
            if self.number_of_people > capacity:
                # if true then will append the capacity containing value to the allocation array
                allocation.append(capacity)
                # and then decreasing the capacity as person will occupy the spacy
                self.number_of_people -= capacity
            else:
                # if false then appending the number of people to the array
                allocation.append(self.number_of_people)
                # setting the number of people to null
                self.number_of_people = 0

            # updating the capacity with sum of last two values of the allocation array
            capacity = sum(allocation[-2:])

        # returning the allocation array
        return allocation


#-----------------------------------------------------------------------------------------------


@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def home():
    people = int(request.form['a'])
    bus = int(request.form['b'])

    # creating the object
    people_count = BusStop(number_of_people=people, number_of_buses=bus)

    # calling the instance method
    output = people_count.do_allocation()
    return render_template('index.html', output=output)


if __name__ == "__main__":
    app.run(debug=True)