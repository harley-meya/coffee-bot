from meya import Component


class CreateTeam(Component):
    
    def start(self):
        
        team_name = self.db.user.get("team_name")
        team_password = self.db.user.get("team_password")
        
        self.db.table("teams").add({"team_name": team_name, "team_password": team_password, "team_members": [self.db.user.id]})

        message = self.create_message(text="Team successfully created!")
        return self.respond(message=message, action="next")