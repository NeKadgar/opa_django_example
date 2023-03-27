package company

default allow = false

allow {
  input.user.is_superuser == true
}

allow {
  input.user.role == "owner"
  input.method == "POST"
}
