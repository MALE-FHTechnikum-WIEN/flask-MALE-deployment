# Load the iris dataset
data(iris)

# Train a simple model (e.g., using random forests)
model <- randomForest(Species ~ ., data = iris)

# Save the model to a file
saveRDS(model, "iris_model.rds")
