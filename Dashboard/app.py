import os
import csv
from io import StringIO
from flask import Flask, render_template, jsonify, request, Response
import psycopg2

app = Flask(__name__, template_folder=os.path.abspath("Dashboard/templates"))

def get_data():
    table_name = request.args.get('series')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    # Retrieve environment variables
    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]

    # Connect to the database
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DB,
    )

    cur = conn.cursor()
    if start_date == "" or start_time == "" or end_date == "" or end_time == "":
        query = f"SELECT time, value FROM \"{table_name}\""
    else:
        query = f"SELECT time, value FROM \"{table_name}\" WHERE time >= '{start_date} {start_time}'::timestamp AND time <= '{end_date} {end_time}'::timestamp"

    cur.execute(query)
    data = cur.fetchall()

    conn.close()

    return data


@app.route('/download_csv')
def download_csv():
    table_name = request.args.get('series')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    # Retrieve data
    data = get_data()

    # Create a CSV file from the data
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Time', 'Value'])
    cw.writerows(data)
    output = si.getvalue()

    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition": f"attachment;filename={table_name}_{start_date}_{end_date}_{start_time}_{end_time}.csv",
            "Content-Type": "text/csv; charset=utf-8",
        },
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/data")
def data():
    # Retrieve data
    data = get_data()

    # Transform the data into JSON format
    trace = {
        "x": [str(x[0]) for x in data],
        "y": [str(x[1]) for x in data],
        "mode": "lines",
        "name": "Sample Time Series",
    }

    layout = {
        "title": "Time Series Data",
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Value"},
    }

    # Combine trace and layout into a single JSON object
    plot_data = {"data": [trace], "layout": layout}

    return jsonify(plot_data)


def main():
    app.run(host="0.0.0.0", port=8888)


if __name__ == "__main__":
    main()
