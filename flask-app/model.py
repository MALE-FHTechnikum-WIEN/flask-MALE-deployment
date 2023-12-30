import rpy2.robjects as robjects
from rpy2.robjects import conversion, default_converter


'''
    This function will be called when the 'POST' request is sent to the flask application.
'''
def run_model(sepal_length, sepal_width):

    # Input validation checking if the function parameters are not empty.
    if (sepal_length == '' or sepal_length == None) or (sepal_width == '' or sepal_width == None):
        return -1

    '''
    This will ensure that the flask and rpy2 code do not interfere with each other by setting the rules for conversion.
    Due to the flask threaded and rpy2 threaded implementation, both cannot run concurrently in threads.
    '''
    with conversion.localconverter(default_converter):

        # Robject allow to embed R code inside python and execute it
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

        # Return as a string robjects
        return str(robjects.r('predict_iris()')[0])
