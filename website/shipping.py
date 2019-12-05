from geopy.distance import distance


class BaseShipping():

    def __init__(self, length, width, height, weight, lat1, long1):
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight
        self.latitude = lat1
        self.longitude = long1
        self.warehouse_latitude = 51.475721
        self.warehouse_longitude = 0.353204

    def volume(self):
        return self.width*self.height*self.length

    def calculate_distance(self):
        p1 = (self.latitude, self.longitude)
        p2 = (self.warehouse_latitude, self.warehouse_longitude)
        return distance(p1, p2).miles

    def set_warehouse_location(self, lat, long):
        self.latitude = lat
        self.longitude = long


class Hermes(BaseShipping):
    # basic quality shipping
    COMPANY_NAME = 'MyHermes'
    COMPANY_PREMIUM = 0.2
    TRACKING_FEE = 1
    SIGNATURE_FEE = 1.2

    def twentyfourhours(self):
        SHIPPING_PREMIUM = 0.139
        DELIVERY_TIME = 24

        shippingCost = self.volume()*self.weight
        shippingCost = float(shippingCost)*self.calculate_distance()
        shippingCost = shippingCost*SHIPPING_PREMIUM
        shippingCost = shippingCost*RoyalMail.COMPANY_PREMIUM
        shippingCostNormalised = (round((shippingCost/14960)*0.06, 2))

        if shippingCostNormalised < 1:
            shippingCostNormalised = shippingCostNormalised *95


        dct = {}
        dct['company_time'] = Hermes.COMPANY_NAME
        dct['delivery_time'] = DELIVERY_TIME
        dct['shipping_cost'] = "{:.2f}".format(shippingCostNormalised)
        dct['tracking'] = Hermes.TRACKING_FEE
        dct['signature'] = Hermes.SIGNATURE_FEE
        return dct

    def fortyEightHours(self):
        SHIPPING_PREMIUM = 0.13
        DELIVERY_TIME = 48
        
        shippingCost = self.volume()*self.weight
        shippingCost = float(shippingCost)*self.calculate_distance()
        shippingCost = shippingCost*SHIPPING_PREMIUM
        shippingCost = shippingCost*RoyalMail.COMPANY_PREMIUM
        shippingCostNormalised = (round((shippingCost/15000)*0.03, 2))

        if shippingCostNormalised < 1:
            shippingCostNormalised = shippingCostNormalised *95

        dct = {}
        dct['company_time'] = Hermes.COMPANY_NAME
        dct['delivery_time'] = DELIVERY_TIME
        dct['shipping_cost'] = "{:.2f}".format(shippingCostNormalised)
        dct['tracking'] = Hermes.TRACKING_FEE
        dct['signature'] = Hermes.SIGNATURE_FEE
        return dct


class RoyalMail(BaseShipping):
    # medium quality shipping

    COMPANY_NAME = 'Royal Mail'
    COMPANY_PREMIUM = 0.5
    TRACKING_FEE = 1.5
    SIGNATURE_FEE = 2

    def twentyfourhours(self):
        SHIPPING_PREMIUM = 0.2
        DELIVERY_TIME = 24

        shippingCost = self.volume()*self.weight
        shippingCost = float(shippingCost)*self.calculate_distance()
        shippingCost = shippingCost*SHIPPING_PREMIUM
        shippingCost = shippingCost*RoyalMail.COMPANY_PREMIUM
        shippingCostNormalised = (round((shippingCost/15000)*0.05, 2))

        if shippingCostNormalised < 1:
            shippingCostNormalised = shippingCostNormalised *95        
        dct = {}
        dct['company_time'] = RoyalMail.COMPANY_NAME
        dct['delivery_time'] = DELIVERY_TIME
        dct['shipping_cost'] = "{:.2f}".format(shippingCostNormalised)
        dct['tracking'] = RoyalMail.TRACKING_FEE
        dct['signature'] = RoyalMail.SIGNATURE_FEE
        return dct

    def fortyEightHours(self):
        SHIPPING_PREMIUM = 0.15
        DELIVERY_TIME = 48

        shippingCost = self.volume()*self.weight
        shippingCost = float(shippingCost)*self.calculate_distance()
        shippingCost = shippingCost*SHIPPING_PREMIUM
        shippingCost = shippingCost*RoyalMail.COMPANY_PREMIUM
        shippingCostNormalised = (round((shippingCost/15000)*0.03, 2))

        if shippingCostNormalised < 1:
            shippingCostNormalised = shippingCostNormalised *95

        dct = {}
        dct['company_time'] = RoyalMail.COMPANY_NAME
        dct['delivery_time'] = DELIVERY_TIME
        dct['shipping_cost'] = "{:.2f}".format(shippingCostNormalised)
        dct['tracking'] = RoyalMail.TRACKING_FEE
        dct['signature'] = RoyalMail.SIGNATURE_FEE
        return dct


def calculate_all(length, width, height, weight, lat, long):
    allAnswers = []
    royalmail = RoyalMail(length, width, height, weight, lat, long)
    allAnswers.append(royalmail.twentyfourhours())
    allAnswers.append(royalmail.fortyEightHours())

    royalmail = Hermes(length, width, height, weight, lat, long)
    allAnswers.append(royalmail.twentyfourhours())
    allAnswers.append(royalmail.fortyEightHours())
    return allAnswers


if __name__ == "__main__":
    # royalmail = RoyalMail(20, 30, 40, 50, 51.5611536, 0.072898)
    # print(royalmail.twentyfourhours())
    # print(royalmail.fortyEightHours())

    # royalmail = Hermes(20, 30, 40, 50, 51.5611536, 0.072898)
    # print(royalmail.twentyfourhours())
    # print(royalmail.fortyEightHours())
    calculate_all(20, 30, 40, 50, 51.5611536, 0.072898)
