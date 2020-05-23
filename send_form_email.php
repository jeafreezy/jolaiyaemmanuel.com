<?php
if ($_SERVER['REQUEST_METHOD'] === "POST") {
  if (empty($_POST['email'])) {
    $emailError = 'Email is empty';
  } else {
    $email = $_POST['email'];

    // validating the email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
      $emailError = 'Invalid email';
    }
  }
  if (empty($_POST['subject'])) {
    $messageError = 'Subject is empty';
  } else {
    $subject = $_POST['subject'];
  }
  if (empty($_POST['message'])) {
    $messageError = 'Message is empty';
  } else {
    $message = $_POST['message'];
  }
  if (empty($emailError) && empty($messageError)) {
    $date = date('j, F Y h:i A');

    $emailBody = "
      <html>
      <head>
        <title>$email is contacting you</title>
      </head>
      <body style=\"background-color:#fafafa;\">
        <div style=\"padding:20px;\">
          <br>
          Email: <span style=\"color:#888\">$email</span>
          <br>

          Subject: <div style=\"color:#888\">$subject</div>
            <br>
          Message: <div style=\"color:#888\">$message</div>
        </div>
      </body>
      </html>
    ";

    $headers =  'From: Contact Form <contact@mydomain.com>' . "\r\n" .
            "Reply-To: $email" . "\r\n" .
            "MIME-Version: 1.0\r\n" . 
          "Content-Type: text/html; charset=iso-8859-1\r\n";

    $to = 'jolaiyaemmanuel@gmail.com';
    $subject = 'Contacting you';

    if (mail($to, $subject, $emailBody, $headers)) {
      $sent = true; 
    }
  }
}
?>

<strong>Message received,I'll get back to you shortly...</strong><br>
<a href="index.html">Return to page</a>