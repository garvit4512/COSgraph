<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<body style="font-family:Arial;font-size:12pt;background-color:#EEEEEE">
<xsl:for-each select="CSITcourses/course">
  <div style="background-color:teal;color:white;padding:4px">
    <span style="font-weight:bold"><xsl:value-of select="course_no"/>: </span>
    <xsl:value-of select="course_title"/>
     </div>
     <div style="margin-left:20px;margin-bottom:1em;font-size:10pt">
       <p style="font-weight:bold;color:red">Course Categories:
       <xsl:value-of select="course_category_CS1"/>,
       <xsl:value-of select="course_category_CS51"/>,
       <xsl:value-of select="course_category_CS52"/>,
       <xsl:value-of select="course_category_MCS"/>
       </p>
       <p><xsl:value-of select="course_credits"/></p>
       <p>Pre-requisites: 
       <a id="{@id}"><xsl:value-of select="course_prereq"/></a></p>
       <p>Overlaps with: 
         <a id="{@id}"><xsl:value-of select="course_overlap"/></a></p>
	 <p><span style="font-style:italic"> <xsl:value-of select="course_content"/> </span>
	 </p>
     </div>
</xsl:for-each>
</body>
</html>
