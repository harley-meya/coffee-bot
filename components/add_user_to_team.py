from meya import Component


class AddUser(Component):

    def start(self):
        
        team = self.db.table("teams").filter(team_name=self.db.user.get("team_name"))[0]
        team["team_members"].append(self.db.user.id)
        
        message = self.create_message(text="You've been added to the team!")
        return self.respond(message=message, action="next")
