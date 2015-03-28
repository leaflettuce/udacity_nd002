from pymongo import MongoClient
import pprint
client = MongoClient('localhost:27017')
db = client['udacity']


#MongoDB Queries Seperated into different functions

def test_data_stats(db):      #initial find queries for basic data stats

    total_docs = db.cbus.find().count()    #total docs
    nodes = db.cbus.find({'type': 'node'}).count()   #total nodes
    ways = db.cbus.find({'type': 'way'}).count()   #total ways
    streets = db.cbus.find({'address.street': {'$exists': 1}}).count()  #number of streets
    users = len(db.cbus.distinct('created.user'))   #total users that input
    shops = db.cbus.find({'shop':{'$exists': 1}}).count()  #total shop count
    cities = len(db.cbus.distinct('address.city'))   #number of unique cities

    print '''total docs == %d
    nodes == %d
    ways == %d
    street count == %d
    users == %d
    shops == %d
    cities == %d''' % (total_docs, nodes, ways, streets, users, shops, cities)

def get_top_users(db):   #top 10 users with most entries
    pprint.pprint(db.cbus.aggregate([{"$group":{"_id":"$created.user",
                                          "count":{"$sum":1}}},
                                     { "$sort":{"count":-1}},
                                     {'$limit': 10}]))

def get_streets(db):  #list out of street names     // primarily to double check my code re-abbreviated correctly
    streets = db.cbus.aggregate([{'$match': {'address.street' : {'$exists': 1}}},
                                  {'$group' : {'_id': '$address.street',
                                         'count': {'$sum': 1}}},
                                  {'$sort': {'count' : -1}}])
    pprint.pprint(streets)

def get_amenities(db): #list of top 10 amenities in data
    amenities =  db.cbus.aggregate([{'$match': {'amenity' : {'$exists': 1}}},
                                    {'$group': {'_id': '$amenity',
                                                'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}},
                                    {'$limit': 10}])
    pprint.pprint(amenities)

def start_search(db):   #queries to find start date count.   only 2
    print db.cbus.distinct('start_date')
    print len(db.cbus.distinct('start_date'))

def get_shop(db):  #list number of shops in descending order
    shop =  db.cbus.aggregate([{'$match': {'shop' : {'$exists': 1}}},
                                    {'$group': {'_id': '$shop',
                                                'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}}])
    pprint.pprint(shop)

def get_cuisine(db):   #top 10 cuisine types
    cuisine =  db.cbus.aggregate([{'$match': {'cuisine' : {'$exists': 1}}},
                                    {'$group': {'_id': '$cuisine',
                                                'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}},
                                    {'$limit': 10}])
    pprint.pprint(cuisine)

def get_history(db):   #find and list iun descending order all historic sites in city
    history =  db.cbus.aggregate([{'$match': {'historic' : {'$exists': 1}}},
                                    {'$group': {'_id': '$historic',
                                                'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}},
                                    {'$limit': 10}])
    pprint.pprint(history)

def religion_types(db):    #list in descending all place of worship types and count
    type = db.cbus.aggregate([{'$match': {'amenity' : 'place_of_worship'}},
                                    {'$group': {'_id': '$religion',
                                                'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}}])

    pprint.pprint(type)

def get_cafe_list(db):  #list of cafes in city, including street number and name if available
    cafes = db.cbus.aggregate([{'$match': {'amenity' : 'cafe'}},
                                    {'$group': {'_id': '$name',
                                                'number': {'$push': '$address.housenumber'},
                                                'street': {'$push': '$address.street'}}}])

    pprint.pprint(cafes)

def bookshop_list(db):  #list of bookstores in city, including street number and name if available
    bookshops = db.cbus.aggregate([{'$match': {'shop' : 'books'}},
                                    {'$group': {'_id': '$name',
                                                'number': {'$push': '$address.housenumber'},
                                                'street': {'$push': '$address.street'}}}])
    pprint.pprint(bookshops)

def coffee_and_books(db):  #list of cafes and bookstores, grouped together via post code
    groups = db.cbus.aggregate([{'$match': {'$or': [{'$and': [{'amenity' : 'cafe'},                     #--|
                                                              {'address.postcode': {'$exists': 1}}]},   #  |- finds all cafes and
                                                    {'$and': [{'shop' : 'books'},                       #  |- bookstores that include
                                                              {'address.postcode': {'$exists': 1}}]}]}},#--|- a post code
                                {'$project': {'_id': '$address.postcode',
                                              'coffee': {'$cond': [{'$eq': ['$amenity', 'cafe']}, '$name','$null']}, #-conditions to split each
                                              'books': {'$cond': [{'$eq': ['$shop', 'books']}, '$name', '$null']}}}, #- category into its separate
                                {'$group':{'_id': '$_id',                                                            #- grouping.  (cafe/books)
                                            'coffee': {'$push': '$coffee'},    #finally groups them all via post code
                                            'books': {'$push': '$books'}}}])   #with a book and cafe category nestled



    pprint.pprint(groups)

def aikido(db):   #query to find any dojos or aikido locations,  then includes address is available
    dojos = db.cbus.aggregate([{'$match': {'$or' : [{'sport' : 'aikido'},
                                           {'amenity': 'dojo'}]}},
                                {'$group': {'_id': '$name',
                                            'number': {'$push': '$address.housenumber'},
                                            'street': {'$push': '$address.street'}}}])
    pprint.pprint(dojos)    # returns None,   bummer

def see_postcodes(db):   #returns a list of post codes and count of number of times returned with names under
     post = db.cbus.aggregate([{'$match': {'address.postcode' : {'$exists': 1}}},  #used to query find names
                                  {'$group' : {'_id': '$address.postcode',         #to then manually set update
                                                'name':{'$push': '$name'},         # and fixed wrong codes
                                         'count': {'$sum': 1}}},
                                  {'$sort': {'count' : -1}}])
     pprint.pprint(post)

def fix_post(db):
    db.cbus.update({'name': 'The Wellington School'},   # set update for named location found from see_postcodes function
        {'$set': {'address.postcode': '43220'}})        #had to manually change for each wrong code,   but allowed for
                                                        #flexibility and limited mistakes

def add_coffee_info(db):   #  queries for finding info regarding coffee shops in columbus.  Additional ideas comes from this
    number = db.cbus.find({'amenity': 'cafe'}).count()  # number of shops in city

    shop_zip = db.cbus.aggregate([{'$match': {'$and': [{'shop':{'$exists': 1}},       #groups cafe count via post code
                                                     {'address.postcode': {'$exists': 1}}]}},
                                {'$group':{'_id': '$address.postcode',
                                            'count': {'$sum': 1}}},
                                 {'$sort': {'count': -1}}])

    shop_street = db.cbus.aggregate([{'$match': {'$and': [{'shop':{'$exists': 1}},    #find shops per street
                                                     {'address.street': {'$exists': 1}}]}},  # used to discover popular
                                {'$group':{'_id': '$address.street',                        # locations
                                            'count': {'$sum': 1}}},
                                 {'$sort': {'count': -1}}])

    clothes = db.cbus.aggregate([{'$match': {'$or': [{'shop' : 'clothes'},{'shop': 'doityourself'},  #limited this query
                                                     {'shop': 'books'},{'shop': 'convenience'}]}},  #to shops I considered
                                    {'$group': {'_id': '$address.postcode',                         #'walk up' types.
                                                'count': {'$sum': 1}}},                    #proper to set a cafe near
                                    {'$sort': {'count': -1}}])

    print number
    pprint.pprint(shop_zip)
    pprint.pprint(shop_street)
    pprint.pprint(clothes)

def main():            #list of all function returns //  tagged out until i wanted to see return.
    #start_search(db)
    #test_data_stats(db)
    #get_top_users(db)
    #get_streets(db)
    #get_amenities(db)
    #add_coffee_info(db)
    #get_cafe_list(db)
    #religion_types(db)
    #get_cuisine(db)
    #get_history(db)
    #get_shop(db)
    #bookshop_list(db)
    #aikido(db)
    #coffee_and_books(db)
    #see_postcodes(db)
    #fix_post(db)
    pass

main()