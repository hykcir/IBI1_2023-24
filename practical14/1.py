import datetime

def parse_with_dom(file_path):
    # use the datetime funciton to record the start time and end time in order to calculate the time interval of the process
    start_time= datetime.datetime.now()
    
    import xml.dom.minidom
    # parse the xml file
    DOMTree = xml.dom.minidom.parse(file_path) 
    terms = DOMTree.getElementsByTagName('term')
    molecular_function=0
    biological_process=0
    cellular_component=0
    # get all 'term' elements from the parsed xml and then get th 'namespace' elements
    for term in terms:
        namespaces = term.getElementsByTagName('namespace')
        for namespace in namespaces:
            # for each 'namespace', get its value and strip the whitespace and other useless elements
            ontology = namespace.firstChild.nodeValue.strip()
            # increment the count for different namespace value
            if ontology == 'molecular_function':
                molecular_function += 1
            elif ontology == 'biological_process':
                biological_process += 1
            elif ontology == 'cellular_component':
                cellular_component += 1
    end_time =datetime.datetime.now()
    time_taken = end_time - start_time
    print("Time taken (DOM):", time_taken)
    print("Molecular function (DOM):",molecular_function)
    print("Biological process (DOM):",biological_process)
    print("Cellular component (DOM):",cellular_component)
    lib={'Molecular function':molecular_function,'Biological process':biological_process,'Cellular component':cellular_component}
    import matplotlib.pyplot as plt
    # extract the headings and their corresponding stistical value
    ontologies = list(lib.keys())
    counts=list(lib.values())
    plt.bar(ontologies, counts, color=['blue', 'green', 'red'])
    plt.xlabel('Ontology')
    plt.ylabel('Number of Terms')
    plt.title('Number of GO Terms by Ontology (DOM)')
    plt.show()
    return
    
dom_term_count = parse_with_dom("/Users/rickyh/Desktop/go_obo.xml")

import xml.sax
# build an empty dictionary for updating 'namespace' elements
ontology_dict = {}
# use the datetime funciton to record the start time and end time in order to calculate the time interval of the process
start_time = datetime.datetime.now()
class GOhandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ''
        self.namespace = ''

    # set 'currentdata' to the current element name
    def startElement(self, name, attrs):
        self.currentdata = name

    def endElement(self, name):
        if self.currentdata == 'namespace':
            ontology_name = self.namespace.strip()
            #  update 'ontology_dict' and count the occurance of the different 'namespace's
            if ontology_name in ontology_dict:
                ontology_dict[ontology_name] += 1
            else:
                ontology_dict[ontology_name] = 1
            # reset the 'self.namespace' to an empty string in case it carry the previous data to the next namspace 
        self.namespace=''

    # find and accumulate the content of the element : 'namespace'
    def characters(self, content):
        if self.currentdata == 'namespace':
            self.namespace += content

def count_namespace_occurrences(xml_file):
    # create an xml parser and  set its contetnt handler to 'GOhandler'
    handler = GOhandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    # parse the xml file
    parser.parse(xml_file)
    end_time = datetime.datetime.now()
    time_taken = end_time - start_time
    print("Time taken (SAX):", time_taken)
    return ontology_dict
ontology_counts = count_namespace_occurrences("/Users/rickyh/Desktop/go_obo.xml")

print("Namespace Occurances (SAX):", ontology_dict)
import matplotlib.pyplot as plt
ontologies=list(ontology_dict.keys())
counts=list(ontology_dict.values())
plt.bar(ontologies,counts,color=['blue', 'green', 'red'])
plt.xlabel('Ontology')
plt.ylabel('Number of Terms')
plt.title('Number of GO Terms by Ontology (SAX)')
plt.show()

# SAX is faster than DOM
