import rpy2.robjects as robjects
from rpy2.robjects import conversion, default_converter


def run_model(predict_value): 
#The function that will be called when the 'POST' request will be sent to our Flask Server

    with conversion.localconverter(default_converter):
        #robject is the object in which you can write your R code

        robjects.r(f'''
                   predict_iris <- function() {{

                       library(randomForest)

                       # Load the iris_model.rds file
                       rf_model <- readRDS("iris_model.rds")

                       # Replace `new_sepal_length` with the actual Sepal.Length value you want to predict
                       new_data_point <- data.frame(Sepal.Length = {predict_value})

                       # Make predictions using the trained Random Forest model
                       prediction <- predict(rf_model, newdata = new_data_point)

                       return(as.character(prediction))
                       }}
                   ''')

        # Call the R function and get the predictions
        return str(robjects.r('predict_iris()')[0])

