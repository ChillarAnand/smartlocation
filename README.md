## Documentation

This is a simple JSON REST API to create, update, delete, and retreive information about `providers`, `service areas`. A simple api to query service areas with latitude & longitude is provided.


### Providers

#### Create provider

**Request/Response:**

|Request/Response|	Description|
| ------------- |-------------|
|Request URL	| http://188.166.228.50/api/v1/providers/ |
|Request Type	|POST|
|Response Type	|json|
|Response|	[{"name":"","email":null,"language":"kjhfd","phone_number":"dhf","currency":"dsd","pk":12}]|

**Fields:**

|Parameter	|Description|
| ------------- |-------------:|
|name| name of provider|
|email|email of provider|
|language|language of provider|
|phone_number| phone number of provider|
|currency| currency code of provider, eg: USD|

**Example:**

```sh
$ curl -X POST http://188.166.228.50/api/v1/providers/ -d "name=john&language=eng&currency=USD&email=a@a.com"
```

#### List providers

#### Update provider

#### Delete provider



### Service Area

#### Create Service Area

**Request/Response:**

|Request/Response|	Description|
| ------------- |-------------|
|Request URL	| http://188.166.228.50/api/v1/serviceareas/ |
|Request Type	|POST|
|Response Type	|json|
|Response|	[{"provider":"http://188.166.228.50/api/v1/providers/12/","name":"test","price":"200.00","polygon":"[[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]]]","pk":1}]|

**Fields:**

|Parameter	|Description|
| ------------- |-------------:|
|name| name of area|
|price| price of in this area |
|polygon| GeoJson polygon coordinates of the area|
|provider| name of provider|

**Example:**

```sh
curl -X POST http://188.166.228.50/api/v1/serviceareas/ -d "price=200.2&provider=http://188.166.228.50/api/v1/providers/12/&polygon=[[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]]]&name=atlanta"
```


#### Search service area

**Request/Response:**

|Request/Response|	Description|
| ------------- |-------------|
|Request URL	| http://188.166.228.50/api/v1/find_service_areas|
|Request Type	|GET|
|Response Type	|json|
|Response|	[{"name":"test","provider":"","price":200.0}]|


**Parameters:**

|Parameter	|Description|
| ------------- |-------------:|
|latitude| latitude of the location|
|longitude|longitude of the location|

```sh
curl http://188.166.228.50/api/v1/find_service_areas?latitude=0.6&longitude=100.5
```
