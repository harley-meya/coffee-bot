from meya import Component


class RemoveUser(Component):
    
    def start(self):
        
        team = self.db.table("teams").filter(team_name=self.db.user.get("team_name"))[0]
        team["team_members"].remove(self.db.user.id)
        self.db.table("teams").update(team["id"], team["team_members"])
        self.db.user.set("team_name", "")
        self.db.user.set("team_password", "")
        
        return self.respond(message=None, action="next")