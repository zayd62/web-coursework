
# Report

  

## login details

  

- admin username: zayd

- admin Password: zayd

  

there are also other users in the database as mentioned in the `arr` below. The `arr` is in the format `username`, `password`, `email`, `date of birth`

  

```python

arr = [

['ashley', '93da4e5be2', 'ashley@test.com',

datetime.date.fromisoformat(str("1995-11-25"))],

['mujib', 'fb0322f2c8', 'mujib@test.com',

datetime.date.fromisoformat(str("2000-07-04"))],

['bob', '43af62ec6c', 'bob@test.com',

datetime.date.fromisoformat(str("1985-02-25"))],

['mary', 'password', 'mary@test.com',

datetime.date.fromisoformat(str("1977-01-01"))],

]

```

## Extra feature

  

The extra feature is an estimated shipping cost. The user selects the item he has won and the delivery address. The cost is calulated taking into account various attributes.

  

The following attributes are part of the `Auction` model:

  

- length `[Attribute 1]`

- width `[Attribute 2]`

- height `[Attribute 3]`

- weight `[Attribute 4]`

  

The next attribute (`[Attribute 5]`) used is a set of co-ordinates. These values are hardcoded in the file `shipping.py` and takes the following values:

  

- latitude = 51.475721

- longitude = 0.353204

  

The final attribute (`[Attribute 6]`) is the `shipping address`. This is obtained by:

  

1. user typing in address

2. using [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)

  

Another attribute (`[Attribute 7]`) is the distance between the `item location (warehouse)` and `shipping address`. The [geopy](https://pypi.org/project/geopy/) package is used to calculate the distance from `[Attribute 5]` and `[Attribute 6]`

  

There are multiple delivery provider with several delivery products per provider. Each delivery product has an algorithm that uses the seven attributes as well as several constants to calculate a cost.

  

The delivery data is exposed behind a `POST` request and when a request is sent, the cost for all the available services are calulated and returned as `JSON` and then JQuery is then used to build a table displaying the information