import xml.etree.ElementTree as ET

# Function for adding a new course in the list of courses
def add_course(course_id, root):
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
	root.append(new_course)
	return root

# Function for indenting the entire xml file in a readable format
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


def get_edges():
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
	# Dictionary for pre requisite and overlapping courses created 

	# This part finds and adds those courses which are not already present in the courses list
	for course in course_prereq_dict:
		for prereq_course in course_prereq_dict[course]:
			if prereq_course not in courses:
				courses[prereq_course] = 1
				cs_root = add_course(prereq_course,cs_root)
				print prereq_course, course_prereq_dict[course]
	
	for course in course_overlap_dict:
		for overlap_course in course_overlap_dict[course]:
			if overlap_course not in courses:
				courses[overlap_course] = 1
				cs_root = add_course(overlap_course,cs_root)
				print overlap_course, course_overlap_dict[course]
	
	# Update the xml file with the new courses
	cs_root = indent(cs_root)
	tree.write("cos.xml",encoding='UTF-8', xml_declaration=True)
	return course_prereq_dict, course_overlap_dict

course_prereq_dict, course_overlap_dict = get_edges()