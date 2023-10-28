<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $to = $_POST["user_email"];
  $subject = "Welcome to our website!";
  $message = "Thank you for signing up to our website. We hope you enjoy your experience!";
  $headers = "From: webmaster@example.com" . "\r\n" .
             "Reply-To: webmaster@example.com" . "\r\n" .
             "X-Mailer: PHP/" . phpversion();

  if (mail($to, $subject, $message, $headers)) {
    echo "Thank you for signing up! A welcome message has been sent to your email.";
  } else {
    echo "Sorry, there was an error sending the welcome message. Please try again later.";
  }
}
?>