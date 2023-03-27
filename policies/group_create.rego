package group.create

default allow = false

allow {
  input.user.is_superuser == true
}

allow {
  input.method == "POST"
  input.user.role == "owner"
  input.user.companies_owned[_] == input.data.company
}
