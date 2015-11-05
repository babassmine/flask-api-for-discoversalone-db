#!/usr/bin/python
from flask import Flask,jsonify,abort, make_response
import MySQLdb, re

app = Flask(__name__)

db = MySQLdb.connect("localhost", "root", ENV["password"], "db_name")

@app.route('/api/v1.0/all', methods=['GET'])
def all():
	hotels = get_hotels()
	return jsonify({'HOTELS': hotels})
	


@app.route('/api/v1.0/hotels', methods=['GET'])
def get_hotels():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM hotels")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()

	except:
		print "Error: unable to fetch data hotels"
	return jsonify({'response': 'Success', 'body':response})

@app.route('/api/v1.0/casino', methods=['GET'])
def get_casino():
	response = []
	
	db = MySQLdb.connect("localhost", "root",ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM casinogaming")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data hotels"
	return jsonify({'response': 'Success', 'body':response})

@app.route('/api/v1.0/guesthouses', methods=['GET'])
def get_gh():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM guesthouses")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data hotels"
	return jsonify({'response': 'Success', 'body':response})
	
@app.route('/api/v1.0/nightclubs', methods=['GET'])
def get_nightclubs():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM nightclubs")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data hotels"
	return jsonify({'response': 'Success', 'body':response})

@app.route('/api/v1.0/restaurants', methods=['GET'])
def get_rest():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM resturants")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data hotels"
	return jsonify({'response': 'Success', 'body':response})
	
@app.route('/api/v1.0/lodges', methods=['GET'])
def get_lodges():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM lodges")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data lodges"
	return jsonify({'response': 'Success', 'body':response})
	
@app.route('/api/v1.0/snacks', methods=['GET'])
def get_snacks():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM snacks")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data lodges"
	return jsonify({'response': 'Success', 'body':response})
	
@app.route('/api/v1.0/newdev', methods=['GET'])
def get_dev():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM newdevelopment")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Name"] = re.sub(r'\s\'\s', "",reading[1].replace("',",",").replace("''","'").strip().rstrip('\''), flags=re.IGNORECASE)
			line["Address"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().rstrip('\'')
			line["Region"] = reading [3].replace("',",",").replace("''","'").strip().strip('\'')
			line["Email"] = reading[4].replace("',",",").replace("''","'").replace(" ", "").strip().rstrip('\'')
			line["Website"] = reading[5].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Rating"] = reading[6].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Phone No"] = reading[7].replace("',",",").replace("''","'").strip().rstrip('\'')
			line["GoeCoord"] = str(reading[8]).replace("',",",").replace("''","'").strip().rstrip('\'')
			line["Fbook"] = reading[9].replace("',",",").replace("''","'").strip().rstrip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data lodges"
	return jsonify({'response': 'Success', 'body':response})


@app.route('/api/v1.0/landmarks', methods=['GET'])
def get_landm():
	response = []
	
	db = MySQLdb.connect("localhost", "root", ENV["password"], "ExploreSL")

	curs = db.cursor()
	try:
		curs.execute("SELECT * FROM landmarks")
		for reading in curs.fetchall():
			line = {}
			line["id"] = str(reading[0]).replace("',",",").replace("''","'").strip().strip('\'')
			line["Name"] = reading[1].replace("'", "").strip().strip('\'')
			line["Image"] = reading [2].replace("',",",").replace("''","'").replace("\" ", "\"").strip().strip('\'')
			line["Link"] = str(reading[3]).replace("',",",").replace("''","'").strip().strip('\'')
			response.append(line)
		db.close()
	except:
		print "Error: unable to fetch data lodges"
	return jsonify({'response': 'Success', 'body':response})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'response': 'failed'}), 404)

if __name__ == '__main__':
    app.run(debug=True, port=ENV["port"], host=ENV["host"])
