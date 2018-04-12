import cherrypy
import redis

import read_store_csv

html_code = """
        <html>
        <head>
        <title>Top 10 Companies </title>
        <style type="text/css">
        	table, th, td {
    		border: 1px solid black;
						}
			table {
				width: 100%;
				height: 70%;
			}

			body
			{
				background: pink ;
				font-size: 40px;
			}

		</style>
        </head>
        <body>
        	 <div class="topnav">
  				<a class="inactive" href="index">Home</a>
  				<a href="about">About</a>
  				<a href="contact">Contact</a>
  				<input type="text" placeholder="Search.." action="query" name="company" style="float: right;">
			</div> 
        	<div>"""


class HelloWOrld(object):
    @cherrypy.expose
    def index(msg=html_code):
        data = read_store_csv.read_csv()
        top_ten_data = read_store_csv.get_top_ten(data, column="CLOSE")
        # CSS code is embedded above"
        msg += """
        
        	<hr>Top 10 Companies based on CLOSE value<hr/>
        	</div>
        	<br/>
        	<br/>
        	<div>
        	<table >
        		<tr>
        			<th>CODE</th>
        			<th>NAME</th>
        			<th>OPEN</th>
        			<th>HIGH</th>
        			<th>LOW</th>
        			<th>CLOSE</th>
        		</tr>"""

        for (index, code, name, opn, high, low, close) in top_ten_data.itertuples():
            msg += """
        		<tr>
        		<td>{}</td>
        		<td>{}</td>
        		<td>{}</td>
        		<td>{}</td>
        		<td>{}</td>
        		<td>{}</td>
        		</tr>
        	""".format(code, name, opn, high, low, close)

        msg += "</table></div></body></html>"
        return msg

    @cherrypy.expose
    def about(msg=html_code):
        msg += """
    	<div> Developed by Gaurav Kumar (@gauravssnl)
    	</div>
    	<body>
    	</html>
    	"""
        return msg

    @cherrypy.expose
    def contact(msg=html_code):
    	msg += """
    	<div> 
    		Name : Gaurav Kumar <br/>

    		Github Profile: <a href="https://github.com/gauravssnl"> @gauravssnl </a>
    		<br/>
    	</div>
    	<body>
    	</html>
    	"""
    	return msg


if __name__ == '__main__':
    cherrypy.quickstart(HelloWOrld)
