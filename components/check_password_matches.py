from meya import Component


class CheckPassword(Component):

    def start(self):
        
        team_name = self.db.user.get("team_name")
        test_pwd = self.db.user.get("team_password")
        password = self.db.table("teams").filter(team_name=team_name)[0]["team_password"]
        
        action = "match" if test_pwd == password else "not_match"
        
        return self.respond(message=None, action=action)
