from meya import Component


class CheckTeamExists(Component):
    
    def start(self):
        
        team_name = self.db.user.get("team_name")
        action = "exists" if len(self.db.table("teams").filter(team_name=team_name)) > 0 else "not_exists"
        
        return self.respond(message=None, action=action)