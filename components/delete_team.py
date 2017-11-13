from meya import Component

class DeleteTeam(Component):
    
    def start(self):
        
        team = self.db.table("teams").filter(team_name=self.db.user.get("team_name"))
        
        # Make sure the team exists
        if len(team) < 1:
            message = self.create_message(text="That team doesn't exist!")
            return self.respond(message=message, action="next")
        else:
            team = team[0]    
        
        self.db.table("teams").delete(team["id"])
        self.db.user.set("team_name", "")
        self.db.user.set("team_password", "")

        message = self.create_message(text="Your team has been deleted!")
        return self.respond(message=message, action="next")