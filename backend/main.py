from fastapi import FastAPI
import database,models,auth,chatmodel
app=FastAPI(title="EdTech API")

models.Base.metadata.create_all(bind=database.engine)

app.include_router(auth.router,prefix="/auth")
app.include_router(chatmodel.router,prefix="/suggest")
@app.get("/")
def home():
    return{"Message":"EdTech API"}
