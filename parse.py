import xml.etree.ElementTree as ET
tree = ET.parse('cos.xml')
cs_root = tree.getroot()
course_prereq_dict = {}
course_overlap_dict = {}
for course in cs_root:
	pre_req = course.find('course_prereq')
	overlap = course.find('course_overlap')
	course_id = course.attrib['id']
	course_prereq_dict[course_id] = []
	course_overlap_dict[course_id] = []

	 
	for pre_reqs in pre_req.findall('ir'):
		course_prereq_dict[course_id].append(pre_reqs.attrib['refid'])

	for overlaps in overlap.findall('ir'):
		course_overlap_dict[course_id].append(overlaps.attrib['refid'])
	
print len(course_prereq_dict),len(course_overlap_dict)	