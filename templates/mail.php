<?php

// Define some constants
define( "RECIPIENT_NAME", "Name" );
define( "RECIPIENT_EMAIL", "name@mail.com" );

// Read the form values
$success = false;
$userFirstName = isset( $_POST['firstname'] ) ? preg_replace( "/[^\s\S\.\-\_\@a-zA-Z0-9]/", "", $_POST['firstname'] ) : "";
$userLastName = isset( $_POST['lastname'] ) ? preg_replace( "/[^\s\S\.\-\_\@a-zA-Z0-9]/", "", $_POST['lastname'] ) : "";
$senderEmail = isset( $_POST['email'] ) ? preg_replace( "/[^\.\-\_\@a-zA-Z0-9]/", "", $_POST['email'] ) : "";
$userPhone = isset( $_POST['tel'] ) ? preg_replace( "/[^\s\S\.\-\_\@a-zA-Z0-9]/", "", $_POST['tel'] ) : "";
$message = isset( $_POST['message'] ) ? preg_replace( "/(From:|To:|BCC:|CC:|Phone:|Content-Type:)/", "", $_POST['message'] ) : "";

// If all values exist, send the email
if ( $userFirstName && $userLastName && $senderEmail && $userPhone && $message) {
  $recipient = RECIPIENT_NAME . " <" . RECIPIENT_EMAIL . ">";
  $headers = " From: " . $userFirstName . $userLastName . "";
  $msgBody = " Email: ". $senderEmail . " Phone: ". $userPhone . " Message: " . $message . "";
  $success = mail( $recipient, $headers, $msgBody );

  //Set Location After Successsfull Submission
  header('Location: contact.html?message=Successfull');
}

else{
    //Set Location After Unsuccesssfull Submission
    header('Location: contact.html?message=Failed');    
}

?>