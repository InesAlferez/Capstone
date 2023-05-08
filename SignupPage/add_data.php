<?php

// Database connection details
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database_name";

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check if the connection was successful
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the data from the form
$name = $_POST['name'];
$email = $_POST['email'];
$phone = $_POST['phone'];

// Insert the data into the table
$sql = "INSERT INTO patientaccounts (first_name, last_name, pet_name,  email, username, password) VALUES ('$first_name', '$last_name', '$pet_name', '$email', '$usernane', '$password')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the database connection
$conn->close();

?>
