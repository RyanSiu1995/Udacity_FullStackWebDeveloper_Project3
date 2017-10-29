import psycopg2 as psql

# Simple remark in table structure:
# 
# TABLE articles (
#     author integer NOT NULL,
#     title text NOT NULL,
#     slug text NOT NULL,
#     lead text,
#     body text,
#     "time" timestamp with time zone DEFAULT now(),
#     id integer NOT NULL
# )
# 
# TABLE authors (
#     name text NOT NULL,
#     bio text,
#     id integer NOT NULL
# )
# 
# TABLE log (
#     path text,
#     ip inet,
#     method text,
#     status text,
#     "time" timestamp with time zone DEFAULT now(),
#     id integer NOT NULL
# )

class Logs:
	def __init__(self, name):
		self.name = name

if __name__ == "__main__":
	log = Logs('h')