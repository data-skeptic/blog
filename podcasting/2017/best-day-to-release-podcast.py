import ConfigParser
import MySQLdb as mdb
import pandas as pd

propertiesFile = "../../my.properties"
cp = ConfigParser.ConfigParser()
cp.readfp(open(propertiesFile))

db_host     = cp.get('Params', 'db_host')
db_user     = cp.get('Params', 'db_user')
db_password = cp.get('Params', 'db_password')
db_db       = 'podcasts'

conn = mdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_db)

query = """
select DAYNAME(pubDate) as dow
, DAYOFWEEK(pubDate) as dowi
, count(*) as episodes
, count(distinct podcast_id) as podcasts
from podcasts.episodes
where pubDate > '2016-01-01'
and pubDate < '2017-01-01'
group by DAYNAME(pubDate)
ORDER BY DAYOFWEEK(pubDate)
"""

df = pd.read_sql(query, conn)

df['episodes'] = df['episodes'] / df['episodes'].sum()
df['podcasts'] = df['podcasts'] / df['podcasts'].sum()

def plot1():
	plt.bar(df.index, df.episodes)
	plt.xticks(df.index + 0.4, df.dow, rotation=45)
	plt.title('Podcast episodes released by day')
	plt.ylabel('%')
	plt.show()

def plot2():
	plt.bar(df.index, df.podcasts)
	plt.xticks(df.index + 0.4, df.dow, rotation=45)
	plt.title('Podcast typical released by day')
	plt.ylabel('%')
	plt.show()
