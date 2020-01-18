"""
Model information Class
Params: array of information 
Purpose: Contains information pertaining to a specific model
Process: the data that is being pass into the class,

!as of (2020-01) my thoughts about this code is that this might not be the most-correct
way of creating the object. Hope to improve in future, when I have more knowledge.

TODO:
 make classes for when program has this data (Inheritance ??)
    1 -> being extracted from the csv
    2 -> called from teh db, so report can be made

"""
from .sql_commands.sql_commands import get_sql_modelName_detail, get_sql_modelID_stiffness
class Model_Info:
    def __init__(self, model_detail, analysis_values):
        self.detail  =  model_detail
        self.id = model_detail[0] # need from DB
        self.name = model_detail[1]
        self.base = model_detail[2]
        self.weight = model_detail[3]
        self.description = model_detail[4]
        self.date = model_detail[5] # need from DB
        self.results = analysis_values

    def sql_detail_value(self):
        return self.detail

    def newton_mm_values(self):
        stiffness = []
        for index in self.results:
            stiffness.append(index[-2])
            
        return stiffness

    def __repr__(self):
        return(f'Model {self.name} has weight of {self.weight}. It is based on {self.base}.')

class Model_Results:
    pass

def model_construct(db_file, model_name):
    model_detail = get_sql_modelName_detail(db_file, model_name)
    model_stiffness = get_sql_modelID_stiffness(db_file, model_detail[0])
    model = Model_Info(model_detail, model_stiffness)
    return model
