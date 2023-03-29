package rbac
import future.keywords.in
import data.teams
import data.company_entities

default allow = false

allow {
  input.user.role == "admin"
}

allow {
  stuff_methods[_] == input.method
  input.user.role == "stuff"
}

allow {
  input.user.role == "organisation_admin"
  company_entities[input.user.company_id][input.instance_name][input.data.instance_id]
}

allow {
  employee_methods[_] == input.method
  input.user.role == "employee"
  team_permissions = {x | x:= teams[input.user.team_id][_]}
  instance_permissions = {x | x:= company_entities[input.user.company_id][input.instance_name][input.data.instance_id][_]}
  team_permissions & instance_permissions != set()
}

allow {
  employee_methods[_] == input.method
  input.user.role == "employee"
  company_entities[input.user.company_id][input.instance_name][input.data.instance_id] == []
}

stuff_methods = {
  "GET", "POST", "PUT"
}

employee_methods = {
 "GET", "POST"
}
