import xml.etree.ElementTree as ET
tree = ET.parse('cos.xml')
cs_root = tree.getroot()
courses = {}
course_prereq_dict = {}
course_overlap_dict = {}
for course in cs_root:
	pre_req = course.find('course_prereq')
	overlap = course.find('course_overlap')
	course_id = course.attrib['id']
	courses[course_id] = 1
	course_prereq_dict[course_id] = []
	course_overlap_dict[course_id] = []

	 
	for pre_reqs in pre_req.findall('ir'):
		course_prereq_dict[course_id].append(pre_reqs.attrib['refid'])

	for overlaps in overlap.findall('ir'):
		course_overlap_dict[course_id].append(overlaps.attrib['refid'])
	
print len(course_prereq_dict),len(course_overlap_dict)	

def add_course(course_id):
	new_course = ET.Element("course")
	new_course.set('id',course_id)
	new_element = ET.Element("course_no")
	new_element.text = str(course_id)
	new_course.append(new_element)
	ET.SubElement(new_course,"course_title")
	ET.SubElement(new_course,"course_category_CS1")
	ET.SubElement(new_course,"course_category_CS51")
	ET.SubElement(new_course,"course_category_CS52")
	ET.SubElement(new_course,"course_category_MCS")
	ET.SubElement(new_course,"course_credits")
	ET.SubElement(new_course,"course_prereq")
	ET.SubElement(new_course,"course_overlap")
	ET.SubElement(new_course,"course_content")
	cs_root.append(new_course)

for course in course_prereq_dict:
	for prereq_course in course_prereq_dict[course]:
		if prereq_course not in courses:
			courses[prereq_course] = 1
			add_course(prereq_course)
			print prereq_course, course_prereq_dict[course]

for course in course_overlap_dict:
	for overlap_course in course_overlap_dict[course]:
		if overlap_course not in courses:
			courses[overlap_course] = 1
			add_course(overlap_course)
			print overlap_course, course_overlap_dict[course]


def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

cs_root = indent(cs_root)


tree.write("cos.xml",encoding='UTF-8', xml_declaration=True)