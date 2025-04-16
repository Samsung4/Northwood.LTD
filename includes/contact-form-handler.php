<?php
// contact-form-handler.php

// Only process POST requests
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Set the recipient email address
    $to = 'info@northwood.ltd';

    // Set the email subject
    $subject = 'New Contact Form Submission';

    // Get the form fields and remove whitespace.
    $name            = isset($_POST['Name-2']) ? strip_tags(trim($_POST['Name-2'])) : '';
    $email           = isset($_POST['Email-2']) ? filter_var(trim($_POST['Email-2']), FILTER_SANITIZE_EMAIL) : '';
    $phone           = isset($_POST['Phone-Number-2']) ? strip_tags(trim($_POST['Phone-Number-2'])) : '';
    $projectLocation = isset($_POST['Project-Location']) ? strip_tags(trim($_POST['Project-Location'])) : '';
    $message         = isset($_POST['Message-2']) ? strip_tags(trim($_POST['Message-2'])) : '';

    // Check that data was sent to the mailer.
    if ( empty($name) || empty($email) || empty($phone) || empty($message) ) {
        // Set a 400 (bad request) response code and exit.
        http_response_code(400);
        echo "Please complete the form and try again.";
        exit;
    }

    // Build the email content.
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Phone: $phone\n";
    $email_content .= "Project Location: $projectLocation\n\n";
    $email_content .= "Message:\n$message\n";

    // Build the email headers.
    $headers = "From: $name <$email>";

    // Send the email.
    if (mail($to, $subject, $email_content, $headers)) {
        // Set a 200 (okay) response code.
        http_response_code(200);
        echo "Thank You! Your message has been sent.";
    } else {
        // Set a 500 (internal server error) response code.
        http_response_code(500);
        echo "Oops! Something went wrong and we couldn't send your message.";
    }

} else {
    // Not a POST request, set a 403 (forbidden) response code.
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>
