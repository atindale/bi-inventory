from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Report(db.Model):
	__tablename__ = 'reports'

	report_key = db.Column(db.Integer, primary_key = True)
	business_unit = db.Column(db.String(45))
	report_id = db.Column(db.String(45))
	report_name = db.Column(db.String(45))
	report_description = db.Column(db.String(100))
	report_owner = db.Column(db.String(45))
	report_source = db.Column(db.String(45))
	report_source_type = db.Column(db.String(45))

	def __init__(self, business_unit, report_id, report_name, report_description, report_owner, report_source, report_source_type):
		self.business_unit = business_unit
		self.report_id = report
		self.report_name = report_name
		self.report_description = report_description
		self.report_owner = report_owner
		self.report_source = report_source
		self.report_source_type = report_source_type


class Cube(db.Model):
	__tablename__ = 'cubes'

	cube_key = db.Column(db.Integer, primary_key = True)
	business_unit = db.Column(db.String(45))
	cube_name = db.Column(db.String(45))
	cube_description = db.Column(db.String(45))
	cube_source = db.Column(db.String(45))

	def __init__(self, business_unit, cube_name, cube_description, cube_source):
		self.business_unit = business_unit
		self.cube_name = cube_name
		self.cube_description = cube_description
		self.cube_source = cube_source


class Glossary(db.Model):
	__tablename__ = 'glossary'

	glossary_key = db.Column(db.Integer, primary_key = True)
	glossary_term = db.Column(db.String(100))
	glossary_term_description = db.Column(db.String(200))
	glossary_owner = db.Column(db.String(45))

	def __init__(self, glossary_term, glossary_term_description, glossary_owner):
		self.glossary_term = cglossary_termube_name
		self.glossary_term_description = glossary_term_description
		self.glossary_owner = glossary_owner

class CubeStructure(db.Model):
	__tablename__ = 'cube_structure'

	cube_structure_key = db.Column(db.Integer, primary_key = True)
	cube_name = db.Column(db.String(45))
	structure_type = db.Column(db.String(45))
	structure_name = db.Column(db.String(45))
	structure_parts = db.Column(db.String(45))

	def __init__(self, cube_name, structure_type, structure_name, structure_parts):
		self.cube_name = cube_name
		self.structure_type = structure_type
		self.structure_name = structure_name
		self.structure_parts = structure_parts


class Table(db.Model):
	__tablename__ = 'tables'

	table_key = db.Column(db.Integer, primary_key = True)
	table_name = db.Column(db.String(45))
	table_description = db.Column(db.String(100))
	update_frequency = db.Column(db.String(45))

	def __init__(self, table_name, update_frequency, table_description):
		self.table_name = table_name
		self.table_description = table_description
		self.update_frequency = update_frequency


class Element(db.Model):
	__tablename__ = 'elements'

	element_key = db.Column(db.Integer, primary_key = True)
	report_id = db.Column(db.String(45))
	element_name = db.Column(db.String(45))
	element_description = db.Column(db.String(100))
	element_notes = db.Column(db.String(100))

	def __init__(self, report_id, element_name, element_description, element_notes):
		self.report_id = report_id
		self.element_name = element_name
		self.element_description = element_description
		self.element_notes = element_notes


class Document(db.Model):
	__tablename__ = 'documents'

	document_key = db.Column(db.Integer, primary_key = True)
	document_type = db.Column(db.String(45))
	document_name = db.Column(db.String(100))
	document_filename = db.Column(db.String(100))
	document_description = db.Column(db.String(200))

	def __init__(self, document_type, document_name, document_filename, document_description):
		self.document_type = document_type
		self.document_name = document_name
		self.document_filename = document_filename
		self.document_description = document_description


class Column(db.Model):
	__tablename__ = 'columns'

	column_key = db.Column(db.Integer, primary_key = True)
	table_name = db.Column(db.String(45))
	column_name = db.Column(db.String(45))
	column_format = db.Column(db.String(100))
	column_length = db.Column(db.Integer)
	column_label = db.Column(db.String(100))

	def __init__(self, table_name, column_name, column_format, column_length, column_label):
		self.table_name = table_name
		self.column_name = column_name
		self.column_format = column_format
		self.column_length = column_length
		self.column_label = column_label


