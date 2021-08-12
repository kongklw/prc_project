import casbin

e = casbin.Enforcer("/home/konglingwen/Desktop/pracSpace/prc_project/usermanage/model.conf",
                    "/home/konglingwen/Desktop/pracSpace/prc_project/usermanage/policy.csv")

sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

if e.enforce(sub, obj, act):
    # permit alice to read data1
    pass
else:
    # deny the request, show an error
    pass


roles = e.get_roles_for_user("alice")