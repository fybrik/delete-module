package dataapi.authz

rule[{}] {
  description := "allow the delete operation"
  input.action.actionType == "delete"
}