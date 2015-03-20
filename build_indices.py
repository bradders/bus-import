#!/bin/python

import MySQLdb
import datetime
import time
import settings


def convert_date_string_to_timestamp(date_string):
    """ converts a string of the format YYYYMMDD into a unix timestamp """
    year = date_string[:4]
    month = date_string[4:6]
    day = date_string[6:]
    d = datetime.datetime(int(year), int(month), int(day))
    return time.mktime(d.timetuple())
    

def convert_time_string_to_seconds(time_string):
    """ converts a string of the format HH:MM:SS into the number of seconds since the start of the day """
    # we can't use the time module because it restricts timetuples to 0..23, etc -- GTFS does not; for time ranges stretching into the next day, you're supposed to use e.g. 23:30-24:30 for a 1-hr 11:30p-12:30a trip
    parts = time_string.split(':')
    return (int(parts[0])*3600) + (int(parts[1])*60) + int(parts[2])


def calendar(connection):
    """ Creates numeric keys for date fields in the calendar table """
    cursor = connection.cursor()
    insert_cursor = connection.cursor()    
    
    cursor.execute("SELECT service_id, start_date, end_date FROM calendars;")
    row = cursor.fetchone()
    while row is not None:
        service_id = row[0]
        start_date = row[1]
        end_date = row[2]
        sql = "UPDATE calendars SET start_date_timestamp='%s', end_date_timestamp='%s' WHERE service_id='%s' AND start_date='%s' AND end_date='%s'" % (convert_date_string_to_timestamp(start_date), convert_date_string_to_timestamp(end_date), service_id, start_date, end_date)
        insert_cursor.execute(sql)
        row = cursor.fetchone()
        
    cursor.close()
    insert_cursor.close()
    
    
def calendar_dates(connection):
    """ Creates numeric keys for date fields in the calendar_dates table """    
    cursor = connection.cursor()
    insert_cursor = connection.cursor()

    cursor.execute("SELECT service_id, date FROM calendar_dates;")
    row = cursor.fetchone()
    while row is not None:
        service_id = row[0]
        date = row[1]
        sql = "UPDATE calendar_dates SET date_timestamp='%s' WHERE service_id='%s' AND date='%s'" % (convert_date_string_to_timestamp(date), service_id, date)
        insert_cursor.execute(sql)
        row = cursor.fetchone()
        
    cursor.close()
    insert_cursor.close()

def route_colors(connection):
    """ Creates additional information for routes """
    cursor = connection.cursor()
    insert_cursor = connection.cursor()

    cursor.execute("SELECT * FROM route_colors")
    row = cursor.fetchone()
    while row is not None:
        route_id = row[1]
        route_color = row[2]
        sql = "UPDATE routes SET route_color='%s' WHERE route_id='%s'" % (route_color, route_id)
        insert_cursor.execute(sql)
        row = cursor.fetchone()

    cursor.close()
    insert_cursor.close()

    cursor = connection.cursor()
    insert_cursor = connection.cursor()

    cursor.execute("SELECT * FROM routes")
    row = cursor.fetchone()
    while row is not None:
        route_id = row[1]
        area_id = 0
        if route_id.endswith("-Whistler"):
            area_id = 1
        elif route_id.endswith("-Victoria"):
	        area_id = 2
        elif route_id.endswith("-KelownaRegional"):
	        area_id = 3
        elif route_id.endswith("-Squamish"):
	        area_id = 4
	    
        sql = "UPDATE routes SET area_id='%s' WHERE route_id='%s'" % (area_id, route_id)
        insert_cursor.execute(sql)
        row = cursor.fetchone()

    cursor.close()
    insert_cursor.close()
	
def stop_times(connection):
    """ Creates numeric keys for date fields in the stop_times table """
    cursor = connection.cursor()
    insert_cursor = connection.cursor()
    another_cursor = connection.cursor()
    
    cursor.execute("SELECT trip_id, arrival_time, departure_time, stop_id FROM stop_times;")
    row = cursor.fetchone()
    while row is not None:
        trip_id = int(row[0])
        arrival_time = row[1]
        departure_time = row[2]
        stop_id = int(row[3])
        sql = "UPDATE stop_times SET arrival_time_seconds=%d, departure_time_seconds=%d WHERE trip_id=%d AND stop_id=%d AND arrival_time='%s' AND departure_time='%s'" % (convert_time_string_to_seconds(arrival_time), convert_time_string_to_seconds(departure_time), trip_id, stop_id, arrival_time, departure_time)
        insert_cursor.execute(sql)
        row = cursor.fetchone()
        
    cursor.close()
    insert_cursor.close()


def main():
    conn = MySQLdb.connect (host=settings.MYSQL_HOST, user=settings.MYSQL_USER, passwd=settings.MYSQL_PASSWORD, db=settings.MYSQL_DATABASE)
    
    print 'processing route colors'
    route_colors(conn)

    print 'processing calendar'
    calendar(conn)

    print 'processing calendar_dates'
    calendar_dates(conn)
    
    #print 'processing stop_times'
    #stop_times(conn)
    
    conn.close()

    print 'done'
    
    
if __name__ == '__main__':
    main()