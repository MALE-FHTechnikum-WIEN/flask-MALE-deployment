library(randomForest)
data(iris)

# Train the Random Forest model
rf_model <- randomForest(Species ~ Sepal.Length, data = iris, ntree = 500)
# rf_model <- randomForest(Species ~ ., data = iris, ntree = 500)

# Save the model to a file
saveRDS(rf_model, "iris_model.rds")
