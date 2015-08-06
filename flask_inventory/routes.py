from flask_inventory import app
from flask import render_template, request, flash, session, url_for, redirect,jsonify
from models import Report, Cube, Table, Element, Column, CubeStructure, Document, Glossary


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/link')
def link():
	return render_template('link.html')

@app.route('/reports')
def reports():

	return render_template('show_reports.html', reports = Report.query.order_by(Report.report_id).all())

@app.route('/glossary')
def glossary():

	return render_template('show_glossary.html', glossary = Glossary.query.order_by(Glossary.glossary_term).all())

@app.route('/cubes')
def cubes():

	return render_template('show_cubes.html', cubes = Cube.query.order_by(Cube.cube_name).all())

@app.route('/tables')
def tables():

	return render_template('show_tables.html', tables = Table.query.order_by(Table.table_name).all())

@app.route('/documents')
def documents():

	return render_template('show_documents.html', documents = Document.query.order_by(Document.document_type).all())

@app.route('/elements/<selected_report>')
def elements(selected_report):

	return render_template('show_elements.html',
		elements = Element.query.filter_by(report_id=selected_report).all(),
		this_report = Report.query.filter_by(report_id=selected_report).first()
		)

@app.route('/columns/<selected_table>')
def columns(selected_table):

	return render_template('show_columns.html',
		columns = Column.query.filter_by(table_name=selected_table).all(),
		this_table = Table.query.filter_by(table_name=selected_table).first()
		)

@app.route('/cube_structure/<selected_cube>')
def cube_structure(selected_cube):

	return render_template('show_cube_structure.html',
		structure = CubeStructure.query.filter_by(cube_name=selected_cube).all(),
		this_cube = Cube.query.filter_by(cube_name=selected_cube).first()
		)


