import rpy2.robjects as robjects
from rpy2.robjects import conversion, default_converter


def run_model(sepal_length, sepal_width): 
#The function that will be called when the 'POST' request will be sent to our Flask Server
    
    #Those condition are just to prevent from any crashes of the server is the user didn't type all the parameters in the inputs
    if (sepal_length == '' or sepal_length == None) or (sepal_width == '' or sepal_width == None):
        return -1
    

    print(sepal_width, sepal_length)
    
    with conversion.localconverter(default_converter):
        #robject is the object in which you can write your R code

        robjects.r(f'''
                   predict_iris <- function() {{

                       library(randomForest)

                       # Load the iris_model.rds file
                       rf_model <- readRDS("iris_model.rds")

                       # Replace `new_sepal_length` with the actual Sepal.Length value you want to predict
                       new_data_point <- data.frame(Sepal.Length = {sepal_length}, Sepal.Width = {sepal_width})

                       # Make predictions using the trained Random Forest model
                       prediction <- predict(rf_model, newdata = new_data_point)

                       return(as.character(prediction))
                       }}
                   ''')

        # Call the R function and get the predictions
        return str(robjects.r('predict_iris()')[0])

