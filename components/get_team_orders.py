from meya import Component


class GetOrders(Component):
    
    def start(self):
        
        team = self.db.table("teams").filter(team_name=self.db.user.get("team_name"))[0]
        orders = ""
        
        members = team["team_members"]
        for member_id in members:
            member = self.db.users.get(member_id)
            orders += member["name"] + ": " + member["order"] + "\n"
        
        message = self.create_message(text=orders)
        return self.respond(message=message, action="next")