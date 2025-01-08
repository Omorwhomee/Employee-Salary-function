
# Step 6: Unzip and display data
unzip_and_display <- function(zip_file, output_dir = "Employee Profile") {
  if (!file.exists(zip_file)) {
    stop("Error: ZIP file not found!")
  }
  
  # Unzip the file
  unzip(zip_file, exdir = output_dir)
  
  # Find and read CSV file
  csv_file <- list.files(output_dir, pattern = "*.csv", full.names = TRUE)
  if (length(csv_file) == 0) {
    stop("Error: No CSV file found in the unzipped folder!")
  }
  
  # Display CSV content
  data <- read.csv(csv_file)
  print(data)
}

# Main Workflow
zip_file <- "Employee Profile.zip"  # Replace with correct path
unzip_and_display(zip_file)
