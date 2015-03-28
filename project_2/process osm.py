__author__ = 'Andy Trick'
__project__= 'Project 2 - MongoDB'
#taken from lesson 6.12 of udacity data wrangling
import xml.etree.cElementTree as ET
import re
import codecs
import json
import pprint


problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')    #setting problem chars
created = [ "version", "changeset", "timestamp", "user", "uid"]   #setting created sublist


def shape_element(element):  #shapes json return
    node = {'created': {}, 'pos': [0.0, 0.0], 'address' : {}}
    if element.tag == "node" or element.tag == "way" :#finds if type is node or way then sets to json
        if element.tag == 'node':
            node['type'] = 'node'
        else:
            node['type'] = 'way'

        for key, val in element.attrib.items():   #pulls first level keys and values
            #print key, val
            if key in created:     #check vs created list above,  if yes returns into nestled 'created'
                node['created'][key] = val
            elif key == 'lat':                #sets pos to lat and lon
                node['pos'][0] = val
            elif key == 'lon':
                node['pos'][1] = val
            else:
                node[key] = val

        for tag in element.findall('tag'):   #pulls tag keys and values
            k = tag.get('k')
            v = tag.get('v')
            # old is handmade dict.   connects incorrect abbr.s to correct
            old = {' Ave.' : ' Ave', ' Avenue' : ' Ave',' Blvd.' : ' Blvd', ' Boulevard': ' Blvd', ' Cir': ' Circle', ' Ct':' Court', ' dr': ' Dr',
                   ' Drive': " Dr", ' E' : ' East', ' Lane': ' Ln', ' N': ' North', ' Parkwa': ' Pkwy', ' Parkway': ' Pkwy', ' Pky': ' Pkwy',
                   ' Pl': ' Place', ' rd': ' Road', ' Rd': ' Road', ' Rd.': ' Road', ' S' : ' South', ' St': ' Street', ' St.': ' Street'}
            if re.search(problemchars, k) is None:  #if no problem chars
                if ':' in k:
                    if ':' in k[k.find(':')+1:]:   #checks if : is in only once
                        pass
                    elif k.startswith("addr:"):  #if one :,  checks if its an address
                        if k == 'addr:street':  #checks for street
                            for i in old:   #for each key in old
                                if v.endswith(i):  #if value of addr:street ends with a key in old dict
                                    end = v.find(i)             # --|
                                    add_to = v[:end]            #   |
                                    final = add_to + old[i]     # --|- this section changes incorrect abbrs to correct
                                    node['address']['street'] = final
                        else:  #else sets to address subcategory
                            node['address'][k[5:]] = v
                        #print node['address']
                    else:  #else puts into json on first level using key val pair
                        node[k] = v
                else:    #same as above
                    node[k] = v

       # pprint.pprint(node)
        return node

    else:
        return None


def process_map(file_in, pretty = False):   #processes osm to json
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)  #sets file out name
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):    #sets iterparse to save on memory
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data


data = process_map('columbus', False)   #pulls in columbus.osm
#pprint.pprint(data)