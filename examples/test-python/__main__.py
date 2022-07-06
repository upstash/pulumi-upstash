# """A Python Pulumi program"""

import  pulumi
import upstash_upstash as upstash


example_db_data = upstash.get_redis_database(database_id="d972343a-3d6f-4810-b542-66ba34a6b501")

pulumi.export("db:", example_db_data)

upstash.GetRedisDatabaseResult(database_id="d972343a-3d6f-4810-b542-66ba34a6b501")

createdTeam = upstash.Team("teamPython", team_name="teamPythona", copy_cc=False, team_members={"bylmaz744@gmail.com": "owner", "burak@upstash.com": "admin"} )

pulumi.export("team", createdTeam)
