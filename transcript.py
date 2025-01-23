#post put delete

@app.post(/user/)
async def user(user: User):
  if type(search_user(user.id)) == User:
    return {"Error": : "User already exists"}
  else:
      users_list.append(user)
  


