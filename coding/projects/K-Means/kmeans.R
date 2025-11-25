set.seed(123)
x <- rnorm(50, mean = 5)
y <- rnorm(50, mean = 8)
data <- data.frame(x, y)

#  k-means clustering
clusters <- kmeans(data, centers = 3)

# Printing  cluster results
cat("Cluster centers:\n")
print(clusters$centers)

cat("\nCluster assignments:\n")
print(clusters$cluster)

# plot
png("kmeans_clusters.png", width = 600, height = 450)
plot(data$x, data$y, col = clusters$cluster, pch = 19,
     main = "K-Means Clustering in R",
     xlab = "X Value", ylab = "Y Value")
points(clusters$centers, col = 1:3, pch = 8, cex = 2, lwd = 2)
dev.off()

cat("\nSaved plot: kmeans_clusters.png\n")
